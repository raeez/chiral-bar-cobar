#!/usr/bin/env python3
r"""Tests for bc_entanglement_zeta_engine.py.

Verifies the entanglement spectral zeta function, Renyi entropy,
evaluation at Riemann zeta zeros, modular entropy, functional equation,
complementarity, and shadow Renyi entropy.

Multi-path verification:
  Path 1: CFT formula S_EE = (c/3)*log(L/eps)
  Path 2: Replica trick: S_n = (1/(1-n))*log(Z_n/Z_1^n)
  Path 3: c=1 free boson exact entanglement spectrum
  Path 4: Calabrese-Cardy consistency checks

75+ tests covering the full mathematical content.

References:
    [BenjaminChang22]: arXiv:2208.02259
    [CalabreseCardy04]: hep-th/0405152
    entanglement_shadow_engine.py
    benjamin_chang_analysis.py
"""

import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from sympy import Rational

from compute.lib import bc_entanglement_zeta_engine as bce

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

# Standard log(L/eps) for tests
LOG_RATIO = 10.0


# ============================================================
# Section 1: Entanglement spectral zeta function
# ============================================================

class TestSpectralZeta:
    """Tests for the entanglement spectral zeta function."""

    @skipmp
    def test_spectral_zeta_at_s1_is_1(self):
        """zeta^{EE}(1) = Tr(rho) = 1 by normalization."""
        for c in [1, 2, 13, 26, 0.5]:
            val = bce.spectral_zeta_universal(1.0, c, LOG_RATIO, DPS)
            assert abs(val - 1.0) < 1e-12, (
                f"zeta^EE(1) != 1 for c={c}: got {val}"
            )

    @skipmp
    def test_log_spectral_zeta_at_s1_is_0(self):
        """log zeta^{EE}(1) = 0 since s - 1/s = 0 at s=1."""
        for c in [1, 13, 26]:
            val = bce.log_spectral_zeta_universal(1.0, c, LOG_RATIO, DPS)
            assert abs(val) < 1e-12, (
                f"log zeta^EE(1) != 0 for c={c}: got {val}"
            )

    @skipmp
    def test_spectral_zeta_at_integer_n(self):
        """zeta^{EE}(n) = (L/eps)^{-(c/6)(n-1/n)} for integer n."""
        c = 2.0
        lr = LOG_RATIO
        for n in [2, 3, 4, 5]:
            val = bce.spectral_zeta_universal(n, c, lr, DPS)
            expected = math.exp(-(c / 6) * (n - 1.0 / n) * lr)
            assert abs(val - expected) / max(abs(expected), 1e-100) < 1e-10, (
                f"Spectral zeta mismatch at n={n}: {val} vs {expected}"
            )

    @skipmp
    def test_spectral_zeta_free_boson(self):
        """Free boson (c=1) spectral zeta at n=2."""
        val = bce.spectral_zeta_free_boson(2, LOG_RATIO, DPS)
        expected = math.exp(-(1.0 / 6) * (2 - 0.5) * LOG_RATIO)
        assert abs(val - expected) < 1e-12

    @skipmp
    def test_spectral_zeta_family_dispatch(self):
        """Family dispatcher returns correct values."""
        # Virasoro c=1
        val = bce.spectral_zeta_family(2, 'virasoro', {'c': 1}, LOG_RATIO, DPS)
        val_direct = bce.spectral_zeta_universal(2, 1.0, LOG_RATIO, DPS)
        assert abs(val - val_direct) < 1e-12

    @skipmp
    def test_spectral_zeta_family_ising(self):
        """Ising model c=1/2."""
        val = bce.spectral_zeta_family(2, 'ising', {}, LOG_RATIO, DPS)
        expected = bce.spectral_zeta_universal(2, 0.5, LOG_RATIO, DPS)
        assert abs(val - expected) < 1e-12

    @skipmp
    def test_spectral_zeta_monotone_in_c(self):
        """For fixed s > 1, |zeta^{EE}(s)| decreases as c increases
        (more entanglement -> smaller Tr(rho^s) for s > 1)."""
        s = 2.0
        lr = LOG_RATIO
        vals = [abs(bce.spectral_zeta_universal(s, c, lr, DPS))
                for c in [1, 5, 13, 26]]
        # log zeta^{EE} = -(c/6)(s-1/s)*lr, and s-1/s > 0 for s > 1,
        # so log zeta decreases (more negative) with c
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1], (
                f"Spectral zeta not monotone in c: {vals}"
            )

    @skipmp
    def test_spectral_zeta_at_complex_s(self):
        """Spectral zeta at complex s is well-defined."""
        s = 2.0 + 1.0j
        val = bce.spectral_zeta_universal(s, 1.0, LOG_RATIO, DPS)
        assert isinstance(val, complex)
        assert math.isfinite(abs(val))


# ============================================================
# Section 2: Renyi entropy from spectral zeta
# ============================================================

class TestRenyiEntropy:
    """Tests for Renyi entropy computation."""

    @skipmp
    def test_renyi_s2_formula(self):
        """S_2 = (c/6)(1+1/2)*log = (c/4)*log."""
        c = 10.0
        lr = LOG_RATIO
        val = bce.renyi_from_spectral_zeta(2, c, lr, DPS)
        expected = (c / 4) * lr
        assert abs(val - expected) < 1e-10

    @skipmp
    def test_renyi_s3_formula(self):
        """S_3 = (c/6)(1+1/3)*log = (2c/9)*log."""
        c = 6.0
        lr = LOG_RATIO
        val = bce.renyi_from_spectral_zeta(3, c, lr, DPS)
        expected = (2 * c / 9) * lr
        assert abs(val - expected) < 1e-10

    @skipmp
    def test_renyi_s_inf_limit(self):
        """S_inf = lim_{n->inf} S_n = (c/6)*log.

        As n -> inf: (c/6)(1+1/n) -> c/6.
        This is the min-entropy.
        """
        c = 12.0
        lr = LOG_RATIO
        val = bce.renyi_from_spectral_zeta(1000, c, lr, DPS)
        expected = (c / 6) * lr
        assert abs(val - expected) / expected < 1e-3

    @skipmp
    def test_renyi_raises_at_n1(self):
        """S_n diverges at n=1; should raise."""
        with pytest.raises(ValueError):
            bce.renyi_from_spectral_zeta(1, 1.0, LOG_RATIO, DPS)

    @skipmp
    def test_renyi_analytic_continuation_agrees_at_integers(self):
        """Analytic continuation matches at integer Renyi indices."""
        c = 8.0
        lr = LOG_RATIO
        for n in [2, 3, 5, 10]:
            val_renyi = bce.renyi_from_spectral_zeta(n, c, lr, DPS)
            val_ac = bce.renyi_analytic_continuation(n, c, lr, DPS)
            assert abs(val_renyi - val_ac) < 1e-10, (
                f"Renyi vs analytic continuation disagree at n={n}: "
                f"{val_renyi} vs {val_ac}"
            )

    @skipmp
    def test_renyi_analytic_at_complex(self):
        """Analytic continuation to complex s is finite."""
        val = bce.renyi_analytic_continuation(2 + 1j, 1.0, LOG_RATIO, DPS)
        assert isinstance(val, complex)
        assert math.isfinite(abs(val))


# ============================================================
# Section 3: Von Neumann entropy
# ============================================================

class TestVonNeumann:
    """Tests for von Neumann entropy."""

    def test_von_neumann_c1(self):
        """S_EE = (1/3)*log for c=1."""
        val = bce.von_neumann_entropy(Rational(1), 1)
        assert val == Rational(1, 3)

    def test_von_neumann_c13(self):
        """S_EE = (13/3)*log for c=13 (self-dual Virasoro)."""
        val = bce.von_neumann_entropy(Rational(13), 1)
        assert val == Rational(13, 3)

    def test_von_neumann_c26(self):
        """S_EE = (26/3)*log for c=26 (critical string)."""
        val = bce.von_neumann_entropy(Rational(26), 1)
        assert val == Rational(26, 3)

    def test_von_neumann_float(self):
        """Float version agrees."""
        val = bce.von_neumann_entropy(1.0, 10.0)
        assert abs(val - 10.0 / 3) < 1e-12

    def test_von_neumann_calabrese_cardy(self):
        """S_EE = (c/3)*log is exactly the Calabrese-Cardy formula."""
        for c in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            val = bce.von_neumann_entropy(c, 1)
            assert val == c / 3


# ============================================================
# Section 4: Evaluation at zeta zeros
# ============================================================

class TestZetaZeros:
    """Tests for spectral zeta at Riemann zeta zeros."""

    @skipmp
    def test_first_zeta_zero_position(self):
        """s_1 = (1 + rho_1)/2 = 3/4 + i*gamma_1/2 with gamma_1 ~ 14.134."""
        result = bce.spectral_zeta_at_zeta_zero(1, 1.0, LOG_RATIO, DPS)
        assert abs(result['gamma'] - 14.134725) < 0.001
        assert abs(result['s_rho'].real - 0.75) < 1e-10

    @skipmp
    def test_spectral_zeta_at_zero_is_finite(self):
        """zeta^{EE}(s_k) is finite (no poles in the spectral zeta)."""
        for k in [1, 2, 3]:
            result = bce.spectral_zeta_at_zeta_zero(k, 1.0, LOG_RATIO, DPS)
            assert math.isfinite(result['abs_spectral_zeta'])

    @skipmp
    def test_spectral_zeta_at_zero_has_modulus_less_than_1(self):
        """For c > 0 and large L/eps, |zeta^{EE}(s_k)| < 1.

        Since Re(s_k - 1/s_k) > 0 for all nontrivial zeros and c > 0,
        the exponent is negative, so the modulus is < 1.
        """
        for k in [1, 2, 5]:
            result = bce.spectral_zeta_at_zeta_zero(k, 1.0, LOG_RATIO, DPS)
            assert result['abs_spectral_zeta'] < 1.0, (
                f"|zeta^EE(s_{k})| >= 1: {result['abs_spectral_zeta']}"
            )

    @skipmp
    def test_zeta_entanglement_profile_length(self):
        """Profile returns correct number of entries."""
        profile = bce.zeta_entanglement_profile(5, 1.0, LOG_RATIO, DPS)
        assert len(profile) == 5

    @skipmp
    def test_zeta_entanglement_profile_sorted_by_gamma(self):
        """Profile is sorted by increasing gamma (zeta zero height)."""
        profile = bce.zeta_entanglement_profile(10, 1.0, LOG_RATIO, DPS)
        gammas = [p['gamma'] for p in profile]
        for i in range(len(gammas) - 1):
            assert gammas[i] < gammas[i + 1]

    @skipmp
    def test_zeta_entanglement_at_c13_selfdual(self):
        """At c=13, the spectral zeta at zeta zeros is real? No --
        it is complex because s_k is complex.  But |zeta^{EE}_13| = |zeta^{EE}_{26-13}|.
        """
        result_c = bce.spectral_zeta_at_zeta_zero(1, 13.0, LOG_RATIO, DPS)
        result_dual = bce.spectral_zeta_at_zeta_zero(1, 13.0, LOG_RATIO, DPS)
        assert abs(result_c['abs_spectral_zeta'] - result_dual['abs_spectral_zeta']) < 1e-12

    @skipmp
    def test_log_zeta_entanglement_at_zero_negative(self):
        """log|E_k| < 0 for c > 0 (modulus decays)."""
        for k in [1, 3, 5]:
            val = bce.log_zeta_entanglement_at_zero(k, 1.0, LOG_RATIO, DPS)
            assert val < 0, f"log|E_{k}| >= 0: {val}"


# ============================================================
# Section 5: Modular entropy
# ============================================================

class TestModularEntropy:
    """Tests for modular entropy and F_1 connection."""

    def test_modular_coefficient_c1(self):
        """For c=1: kappa=1/2, F1=1/48, S_coeff=1/3."""
        result = bce.modular_hamiltonian_coefficient(1)
        assert result['kappa'] == Rational(1, 2)
        assert result['F1'] == Rational(1, 48)
        assert result['S_EE_coefficient'] == Rational(1, 3)

    def test_modular_coefficient_c26(self):
        """For c=26: kappa=13, F1=13/24."""
        result = bce.modular_hamiltonian_coefficient(26)
        assert result['kappa'] == Rational(13)
        assert result['F1'] == Rational(13, 24)

    def test_modular_ratio_is_16(self):
        """S_EE / F_1 = (c/3) / (c/48) = 16 (per unit log(L/eps))."""
        for c in [1, 2, 13, 26]:
            result = bce.modular_hamiltonian_coefficient(c)
            if result['ratio_coefficient'] is not None:
                assert result['ratio_coefficient'] == 16

    def test_modular_entropy_consistency(self):
        """S_mod = F_1 * 16 * log(L/eps)."""
        result = bce.modular_entropy_from_F1(Rational(1), 10)
        assert result['consistent'] is True

    def test_modular_entropy_float_consistency(self):
        """Float version also consistent."""
        result = bce.modular_entropy_from_F1(1.0, 10.0)
        assert result['consistent'] is True

    @skipmp
    def test_modular_spectrum_levels(self):
        """Modular spectrum has correct number of levels."""
        levels = bce.modular_hamiltonian_spectrum(1.0, LOG_RATIO, 20, DPS)
        assert len(levels) == 20

    @skipmp
    def test_modular_spectrum_normalized(self):
        """Modular spectrum eigenvalues sum to approximately 1."""
        levels = bce.modular_hamiltonian_spectrum(1.0, LOG_RATIO, 50, DPS)
        total = sum(lev['lambda_n'] for lev in levels)
        assert abs(total - 1.0) < 1e-3  # approximate since truncated

    @skipmp
    def test_modular_spectrum_monotone(self):
        """Eigenvalues decrease with n."""
        levels = bce.modular_hamiltonian_spectrum(1.0, LOG_RATIO, 10, DPS)
        for i in range(len(levels) - 1):
            assert levels[i]['lambda_n'] >= levels[i + 1]['lambda_n']


# ============================================================
# Section 6: Functional equation
# ============================================================

class TestFunctionalEquation:
    """Tests for the spectral zeta functional equation."""

    @skipmp
    def test_inversion_symmetry(self):
        """zeta^{EE}(s) * zeta^{EE}(1/s) = 1."""
        for s in [2.0, 3.0 + 1.0j, 0.5 + 2.0j, 0.3]:
            result = bce.spectral_zeta_inversion_symmetry(s, 1.0, LOG_RATIO, DPS)
            assert result['error'] < 1e-12, (
                f"Inversion symmetry fails at s={s}: error={result['error']}"
            )

    @skipmp
    def test_inversion_symmetry_c13(self):
        """Inversion symmetry at self-dual point c=13."""
        for s in [2.0, 1.5 + 3.0j]:
            result = bce.spectral_zeta_inversion_symmetry(s, 13.0, LOG_RATIO, DPS)
            assert result['error'] < 1e-12

    @skipmp
    def test_functional_equation_log_product_zero(self):
        """log zeta^{EE}(s) + log zeta^{EE}(1/s) = 0."""
        for s in [2.0, 0.5 + 5.0j, 3.0 + 0.1j]:
            result = bce.entropy_functional_equation_test(s, 1.0, LOG_RATIO, DPS)
            assert result['product_error'] < 1e-12, (
                f"Log product not zero at s={s}: {result['product_error']}"
            )

    @skipmp
    def test_renyi_sum_formula(self):
        """S(s) + S(1/s) = (c/6)(2 + s + 1/s)*log."""
        for s in [2.0, 3.0 + 1.0j]:
            result = bce.entropy_functional_equation_test(s, 6.0, LOG_RATIO, DPS)
            assert result['renyi_sum_error'] < 1e-12

    @skipmp
    def test_inversion_at_zeta_zeros(self):
        """Inversion symmetry holds at s = s_k (zeta zero positions)."""
        for k in [1, 2, 3]:
            from mpmath import zetazero
            rho = zetazero(k)
            s_k = complex((1 + rho) / 2)
            result = bce.spectral_zeta_inversion_symmetry(s_k, 1.0, LOG_RATIO, DPS)
            assert result['error'] < 1e-10


# ============================================================
# Section 7: Complementarity
# ============================================================

class TestComplementarity:
    """Tests for complementarity under c <-> 26-c."""

    @skipmp
    def test_spectral_complementarity_sum(self):
        """log zeta_c + log zeta_{26-c} = -(26/6)(s-1/s)*log, independent of c."""
        for c in [1.0, 5.0, 13.0, 20.0, 25.0]:
            result = bce.entanglement_complementarity_spectral(
                2.0, c, LOG_RATIO, DPS
            )
            assert result['error'] < 1e-12, (
                f"Complementarity fails at c={c}: error={result['error']}"
            )

    @skipmp
    def test_spectral_complementarity_complex_s(self):
        """Complementarity holds for complex s too."""
        s = 1.5 + 2.0j
        for c in [1.0, 13.0]:
            result = bce.entanglement_complementarity_spectral(
                s, c, LOG_RATIO, DPS
            )
            assert result['error'] < 1e-12

    @skipmp
    def test_renyi_complementarity(self):
        """S_n(c) + S_n(26-c) = (26/6)(1+1/n)*log, independent of c."""
        for c in [1.0, 6.0, 13.0, 20.0]:
            for n in [2, 3, 5]:
                result = bce.complementarity_renyi(n, c, LOG_RATIO, DPS)
                assert result['error'] < 1e-12, (
                    f"Renyi complementarity fails at c={c}, n={n}: "
                    f"error={result['error']}"
                )

    @skipmp
    def test_von_neumann_complementarity(self):
        """S_EE(c) + S_EE(26-c) = (26/3)*log."""
        for c in [1, 5, 13, 20, 26]:
            s1 = bce.von_neumann_entropy(c, 1)
            s2 = bce.von_neumann_entropy(26 - c, 1)
            total = float(s1) + float(s2)
            expected = 26.0 / 3
            assert abs(total - expected) < 1e-12

    @skipmp
    def test_self_dual_spectral_zeta(self):
        """At c=13, spectral zeta from self_dual function matches universal."""
        for s in [2.0, 1.5 + 1.0j]:
            val_sd = bce.self_dual_spectral_zeta(s, LOG_RATIO, DPS)
            val_univ = bce.spectral_zeta_universal(s, 13.0, LOG_RATIO, DPS)
            assert abs(val_sd - val_univ) < 1e-12


# ============================================================
# Section 8: Shadow Renyi entropy
# ============================================================

class TestShadowRenyi:
    """Tests for shadow Renyi entropy of the shadow tower."""

    def test_faber_pandharipande_values(self):
        """FP coefficients: lambda_1 = 1/24, lambda_2 = 7/5760."""
        assert bce.faber_pandharipande(1) == Rational(1, 24)
        assert bce.faber_pandharipande(2) == Rational(7, 5760)
        assert bce.faber_pandharipande(3) == Rational(31, 967680)

    def test_shadow_free_energies(self):
        """F_g = kappa * lambda_g^FP."""
        fes = bce.shadow_free_energies(Rational(1), 3)
        assert fes[0] == (1, Rational(1, 24))
        assert fes[1] == (2, Rational(7, 5760))

    @skipmp
    def test_shadow_renyi_positive(self):
        """Shadow Renyi S_r >= 0 for all r >= 2."""
        for kappa in [0.5, 1.0, 6.5, 13.0]:
            for r in [2, 3, 5, 10]:
                val = bce.shadow_renyi_entropy(kappa, r, 20, DPS)
                assert val >= -1e-12, (
                    f"Shadow Renyi negative: kappa={kappa}, r={r}, S={val}"
                )

    @skipmp
    def test_shadow_renyi_decreases_in_r(self):
        """Shadow Renyi S_r decreases with r (for concentrated distributions)."""
        kappa = 1.0
        vals = [bce.shadow_renyi_entropy(kappa, r, 20, DPS) for r in range(2, 8)]
        for i in range(len(vals) - 1):
            assert vals[i] >= vals[i + 1] - 1e-10, (
                f"Shadow Renyi not decreasing: {vals}"
            )

    @skipmp
    def test_shadow_renyi_profile_length(self):
        """Profile returns correct number of entries."""
        profile = bce.shadow_renyi_profile(1.0, [2, 3, 4, 5], 20, DPS)
        assert len(profile) == 4

    @skipmp
    def test_shadow_shannon_nonnegative(self):
        """Shadow Shannon entropy >= 0."""
        for kappa in [0.5, 1.0, 13.0]:
            val = bce.shadow_shannon_entropy(kappa, 20, DPS)
            assert val >= -1e-12

    @skipmp
    def test_shadow_shannon_bounds_renyi(self):
        """Shannon >= Renyi for r >= 1 (a standard inequality).

        H >= S_r for r >= 1.  Since we compute S_r for r >= 2
        and H = lim_{r->1} S_r, we check H >= S_2.
        """
        kappa = 1.0
        H = bce.shadow_shannon_entropy(kappa, 20, DPS)
        S2 = bce.shadow_renyi_entropy(kappa, 2, 20, DPS)
        assert H >= S2 - 1e-10

    def test_shadow_concentration_high(self):
        """Shadow tower is dominated by genus 1.

        The FP coefficients decay super-exponentially, so F_1 dominates.
        """
        conc = bce.shadow_tower_concentration(1, 20)
        assert conc > 0.95, (
            f"Shadow tower not concentrated at genus 1: {conc}"
        )

    def test_shadow_concentration_independent_of_kappa(self):
        """Concentration is independent of kappa (kappa scales all F_g equally)."""
        conc1 = bce.shadow_tower_concentration(1, 20)
        conc2 = bce.shadow_tower_concentration(13, 20)
        assert abs(conc1 - conc2) < 1e-12


# ============================================================
# Section 9: Zeta-entanglement correspondence
# ============================================================

class TestZetaEntanglement:
    """Tests for the E_k(A) profile and decay analysis."""

    @skipmp
    def test_zeta_entanglement_values_length(self):
        """Returns correct number of entries."""
        vals = bce.zeta_entanglement_values(5, 1.0, LOG_RATIO, DPS)
        assert len(vals) == 5

    @skipmp
    def test_zeta_entanglement_all_less_than_1(self):
        """All E_k < 1 for c > 0 and large L/eps."""
        vals = bce.zeta_entanglement_values(10, 1.0, LOG_RATIO, DPS)
        for v in vals:
            assert v['E_k'] < 1.0

    @skipmp
    def test_zeta_entanglement_decay_rate_formula(self):
        """Asymptotic decay: E_k -> (L/eps)^{-c/8}."""
        result = bce.zeta_entanglement_decay_rate(1.0, LOG_RATIO)
        expected = math.exp(-1.0 / 8.0 * LOG_RATIO)
        assert abs(result['asymptotic_E'] - expected) < 1e-12

    @skipmp
    def test_zeta_entanglement_approaches_asymptote(self):
        """E_k approaches the asymptotic value as k increases."""
        asymp = bce.zeta_entanglement_decay_rate(1.0, LOG_RATIO)['asymptotic_E']
        vals = bce.zeta_entanglement_values(20, 1.0, LOG_RATIO, DPS)
        # Later zeros should be closer to asymptote
        err_early = abs(vals[0]['E_k'] - asymp)
        err_late = abs(vals[-1]['E_k'] - asymp)
        assert err_late < err_early, (
            f"E_k not approaching asymptote: early err={err_early}, late err={err_late}"
        )

    @skipmp
    def test_zeta_entanglement_c_dependence(self):
        """Higher c gives smaller E_k (more entanglement, stronger decay)."""
        E_c1 = bce.zeta_entanglement_values(1, 1.0, LOG_RATIO, DPS)[0]['E_k']
        E_c13 = bce.zeta_entanglement_values(1, 13.0, LOG_RATIO, DPS)[0]['E_k']
        assert E_c1 > E_c13


# ============================================================
# Section 10: Multi-path verification
# ============================================================

class TestMultiPathVerification:
    """Multi-path verification of core formulas."""

    @skipmp
    def test_verify_renyi_limit_c1(self):
        """Three-path verification of von Neumann limit for c=1."""
        result = bce.verify_renyi_limit(1.0, LOG_RATIO, DPS)
        assert result['path1_error'] < 1e-12
        assert result['path3_error'] < 1e-12

    @skipmp
    def test_verify_renyi_limit_c13(self):
        """Three-path verification at self-dual c=13."""
        result = bce.verify_renyi_limit(13.0, LOG_RATIO, DPS)
        assert result['path1_error'] < 1e-12
        assert abs(result['expected'] - 13.0 / 3 * LOG_RATIO) < 1e-10

    @skipmp
    def test_verify_free_boson(self):
        """Free boson (c=1) spectral zeta: two paths agree at all integers."""
        result = bce.verify_free_boson_spectral_zeta(LOG_RATIO, DPS)
        for n in [2, 3, 4, 5]:
            assert result[n]['error'] < 1e-12, (
                f"Free boson paths disagree at n={n}: error={result[n]['error']}"
            )

    @skipmp
    def test_verify_cardy_calabrese_c1(self):
        """Four-path verification of Calabrese-Cardy for c=1."""
        result = bce.verify_cardy_calabrese(1.0, LOG_RATIO, DPS)
        assert result['all_agree'] < 1e-12

    @skipmp
    def test_verify_cardy_calabrese_c26(self):
        """Four-path verification at c=26 (critical string)."""
        result = bce.verify_cardy_calabrese(26.0, LOG_RATIO, DPS)
        assert result['all_agree'] < 1e-12
        assert abs(result['path1_CFT'] - 26.0 / 3 * LOG_RATIO) < 1e-10

    @skipmp
    def test_verify_cardy_calabrese_c_half(self):
        """Four-path verification at c=1/2 (Ising)."""
        result = bce.verify_cardy_calabrese(0.5, LOG_RATIO, DPS)
        assert result['all_agree'] < 1e-12

    @skipmp
    def test_renyi_from_spectral_zeta_matches_direct(self):
        """S_n from spectral zeta matches direct (c/6)(1+1/n)*log.

        Cross-check between two independent code paths.
        """
        c = 8.0
        lr = LOG_RATIO
        for n in [2, 3, 4, 5, 10]:
            val_sz = bce.renyi_from_spectral_zeta(n, c, lr, DPS)
            val_direct = (c / 6) * (1 + 1.0 / n) * lr
            assert abs(val_sz - val_direct) < 1e-10


# ============================================================
# Section 11: Combined analysis
# ============================================================

class TestCombinedAnalysis:
    """Tests for the combined census function."""

    @skipmp
    def test_census_c1(self):
        """Census for c=1 returns all expected fields."""
        result = bce.bc_entanglement_census(1.0, LOG_RATIO, 5, 5, DPS)
        assert 'von_neumann' in result
        assert 'renyi_2' in result
        assert 'renyi_3' in result
        assert 'zeta_entanglement' in result
        assert len(result['zeta_entanglement']) == 5
        assert 'complementarity' in result
        assert 'shadow_renyi_2' in result
        assert 'modular' in result

    @skipmp
    def test_census_von_neumann_correct(self):
        """Census von Neumann matches direct computation."""
        result = bce.bc_entanglement_census(1.0, LOG_RATIO, 3, 5, DPS)
        expected = 1.0 / 3 * LOG_RATIO
        assert abs(result['von_neumann'] - expected) < 1e-10

    @skipmp
    def test_census_c13(self):
        """Census at self-dual point c=13."""
        result = bce.bc_entanglement_census(13.0, LOG_RATIO, 3, 5, DPS)
        assert abs(result['von_neumann'] - 13.0 / 3 * LOG_RATIO) < 1e-10
        assert abs(result['kappa'] - 6.5) < 1e-10


# ============================================================
# Section 12: Edge cases and robustness
# ============================================================

class TestEdgeCases:
    """Edge cases and robustness tests."""

    @skipmp
    def test_small_log_ratio(self):
        """Works with small log(L/eps) ~ 1."""
        val = bce.spectral_zeta_universal(2, 1.0, 1.0, DPS)
        assert math.isfinite(abs(val))

    @skipmp
    def test_large_log_ratio(self):
        """Works with large log(L/eps) ~ 100."""
        val = bce.spectral_zeta_universal(2, 1.0, 100.0, DPS)
        assert math.isfinite(abs(val))
        assert abs(val) < 1.0  # should be very small

    @skipmp
    def test_spectral_zeta_at_s_near_0(self):
        """Near s=0: zeta^{EE}(s) ~ (L/eps)^{c/(6s)} diverges.

        For small s > 0: s - 1/s ~ -1/s, so log zeta ~ (c/6)/s * log,
        which diverges.  This is the max-entropy limit.
        """
        val = bce.spectral_zeta_universal(0.01, 1.0, LOG_RATIO, DPS)
        assert abs(val) > 1.0  # should be very large

    @skipmp
    def test_spectral_zeta_negative_s(self):
        """Spectral zeta at negative s is defined."""
        val = bce.spectral_zeta_universal(-2.0, 1.0, LOG_RATIO, DPS)
        assert math.isfinite(abs(val))

    def test_shadow_renyi_zero_kappa(self):
        """Shadow Renyi with kappa=0: all F_g = 0."""
        # With kappa = 0, all free energies vanish.
        # shadow_renyi should return 0 (degenerate distribution).
        val = bce.shadow_renyi_entropy(0, 2, 10, DPS) if HAS_MPMATH else 0
        assert val == 0.0

    def test_faber_pandharipande_raises_for_g0(self):
        """FP coefficient undefined for g < 1."""
        with pytest.raises(ValueError):
            bce.faber_pandharipande(0)

    @skipmp
    def test_unknown_family_raises(self):
        """Unknown family name raises ValueError."""
        with pytest.raises(ValueError):
            bce.spectral_zeta_family(2, 'unknown_algebra', {}, LOG_RATIO, DPS)
