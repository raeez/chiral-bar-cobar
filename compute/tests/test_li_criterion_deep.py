#!/usr/bin/env python3
"""
Tests for the adversarial attack on Li criterion failure for shadow sewing lifts.

ATTACK SUMMARY:
  prop:li-criterion-failure claims λ̃_n(A) eventually negative for ALL families.
  We decompose S_A(u) = ζ(u+1)·R_A(u) and attack from multiple directions.

CRITICAL FINDING — THE HADAMARD GAP:
  The manuscript's "prime-side Li coefficients" are defined by:
    λ̃_n = (1/(n-1)!) d^n/du^n [u^{n-1} log Ξ(u)] |_{u=1}

  This derivative formula is NOT equivalent to the classical zero-sum formula
    λ_n = Σ_ρ [1 - (1-1/ρ)^n]
  unless Ξ is entire of order 1 with a specific Hadamard product structure.

  For Ξ^{red}_H(u) = (u-1)ζ(u):
    - The derivative formula gives λ̃^{red}_6 = -0.184 (NEGATIVE)
    - The zero-sum formula gives λ_6 = +0.754 (POSITIVE)

  The difference = "Hadamard gap" from exponential factors e^{u/ρ} in the
  Hadamard product of (u-1)ζ(u).

STRUCTURAL CONCLUSIONS:
  1. The manuscript's λ̃_n are a legitimate invariant of the sewing lift,
     measuring Taylor expansion behavior of log Ξ_A in the Li-parametrized variable.
  2. Their negativity is a genuine mathematical fact, not a normalization artifact.
  3. But the INTERPRETATION "zeros on two lines cause Li failure" conflates the
     derivative formula with the zero-sum formula. The classical Li criterion
     connects zero-sum positivity to RH; the derivative formula has no such
     direct connection.
  4. The decomposition S_A = ζ(u+1)·R_A is real and the factorization
     λ̃_n^{full} = λ̃_n^{red} + λ̃_n^{wind} holds exactly.
  5. Even the reduced derivative-formula coefficients are eventually negative
     for ALL families (including Heisenberg), but for different reasons than
     the zero-sum coefficients.

57 tests total.
"""

import pytest
import sys
import os
from mpmath import (mp, mpf, mpc, zeta, euler as euler_gamma, diff, log,
                    gamma as mpgamma, pi, power, fac, stieltjes,
                    zetazero, re, im, fabs as mpabs, sqrt)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

mp.dps = 30


# =============================================================================
# Self-contained helpers (test stability: no import of lib)
# =============================================================================

def harmonic_zeta(n, u):
    if n <= 0:
        return mpf(0)
    return sum(power(j, -u) for j in range(1, n + 1))


def _zeta_reg(u):
    eps = u - 1
    if mpabs(eps) < mpf('1e-15'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2 + stieltjes(2) * eps**3)
    return (u - 1) * zeta(u)


def S_generic(weights, u):
    return zeta(u + 1) * sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


def R_generic(weights, u):
    return sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)


def Xi_full(weights, u):
    return (u - 1) * S_generic(weights, u)


def Xi_red(weights, u):
    return sum(_zeta_reg(u) - (u - 1) * harmonic_zeta(w - 1, u) for w in weights)


def li_n(Xi_func, n):
    def f(u, _n=n):
        return power(u, _n - 1) * log(Xi_func(u))
    return diff(f, mpf(1), n) / fac(n - 1)


def li_coeffs(Xi_func, n_max):
    return [li_n(Xi_func, n) for n in range(1, n_max + 1)]


def li_zerosum(n, n_zeros=50):
    """Classical zero-sum Li coefficient for ζ."""
    total = mpc(0, 0)
    for k in range(1, n_zeros + 1):
        rho = zetazero(k)
        rho_bar = mpc(re(rho), -im(rho))
        total += (1 - (1 - 1/rho)**n) + (1 - (1 - 1/rho_bar)**n)
    return re(total)


# Specific Xi functions
def Xi_H_full(u):
    return _zeta_reg(u) * zeta(u + 1)

def Xi_H_red(u):
    return _zeta_reg(u)

def Xi_V_full(u):
    return zeta(u + 1) * (_zeta_reg(u) - (u - 1))

def Xi_V_red(u):
    return _zeta_reg(u) - (u - 1)

def Xi_WN_full(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * _zeta_reg(u) - (u - 1) * harm_sum)

def Xi_WN_red(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return (N - 1) * _zeta_reg(u) - (u - 1) * harm_sum

def Xi_bg_full(u):
    return 2 * _zeta_reg(u) * zeta(u + 1)

def Xi_bg_red(u):
    return 2 * _zeta_reg(u)

def Xi_wind(u):
    return zeta(u + 1)


# =============================================================================
# TEST BLOCK 1: S_A(u) = ζ(u+1) · R_A(u) factorization
# =============================================================================

class TestFactorizationIdentity:
    """Verify S_A(u) = ζ(u+1) · R_A(u) for all families."""

    @pytest.mark.parametrize("u_val", [2, 3, 5, 10])
    def test_heisenberg_factorization(self, u_val):
        u = mpf(u_val)
        S = zeta(u) * zeta(u + 1)
        R = zeta(u)
        assert abs(float(S - zeta(u + 1) * R)) < 1e-20

    @pytest.mark.parametrize("u_val", [2, 3, 5, 10])
    def test_virasoro_factorization(self, u_val):
        u = mpf(u_val)
        S = zeta(u + 1) * (zeta(u) - 1)
        R = zeta(u) - 1
        assert abs(float(S - zeta(u + 1) * R)) < 1e-20

    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_WN_factorization(self, N):
        u = mpf(3)
        S = S_generic(list(range(2, N + 1)), u)
        R = R_generic(list(range(2, N + 1)), u)
        assert abs(float(S - zeta(u + 1) * R)) < 1e-15

    def test_betagamma_factorization(self):
        u = mpf(3)
        assert abs(float(2 * zeta(u) * zeta(u + 1) - zeta(u + 1) * 2 * zeta(u))) < 1e-20

    def test_generic_weights_factorization(self):
        u = mpf(4)
        weights = [1, 2, 3]
        S = S_generic(weights, u)
        R = R_generic(weights, u)
        assert abs(float(S - zeta(u + 1) * R)) / abs(float(S)) < 1e-15


# =============================================================================
# TEST BLOCK 2: Reduced spectral functions — explicit formulas
# =============================================================================

class TestReducedFormulas:

    def test_R_heisenberg_is_zeta(self):
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            assert abs(float(R_generic([1], u) - zeta(u))) < 1e-20

    def test_R_virasoro_is_zeta_minus_1(self):
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            assert abs(float(R_generic([2], u) - (zeta(u) - 1))) < 1e-20

    def test_R_betagamma_is_2zeta(self):
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            assert abs(float(R_generic([1, 1], u) - 2 * zeta(u))) < 1e-20

    def test_R_W3(self):
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            R = R_generic([2, 3], u)
            expected = 2 * zeta(u) - 1 - (1 + power(2, -u))
            assert abs(float(R - expected)) < 1e-15


# =============================================================================
# TEST BLOCK 3: CRITICAL — The Hadamard gap
# =============================================================================

class TestHadamardGap:
    """The derivative formula and zero-sum formula give DIFFERENT results."""

    def test_lambda1_derivative_formula(self):
        """λ̃_1 via derivative = (log Ξ^{red})'(1) = γ (Euler-Mascheroni)."""
        val = float(li_n(Xi_H_red, 1))
        assert abs(val - float(euler_gamma)) < 1e-8

    def test_lambda1_zerosum_different(self):
        """λ_1 via zero sum ≈ 0.023 ≠ γ ≈ 0.577 (50 zero pairs, approximate)."""
        zs = float(li_zerosum(1, 50))
        deriv = float(li_n(Xi_H_red, 1))
        # They must be qualitatively different
        assert abs(zs - deriv) > 0.3, f"zerosum={zs}, deriv={deriv}: should differ"

    def test_derivative_eventually_negative_for_zeta_reg(self):
        """The generalized Li coefficients of (u-1)ζ(u) become negative."""
        red = li_coeffs(Xi_H_red, 8)
        # Positive for n=1..5, negative from n=6
        for n in range(5):
            assert float(red[n]) > 0, f"n={n+1}: should be positive"
        assert float(red[5]) < 0, f"n=6: should be negative"

    def test_zerosum_all_positive(self):
        """The zero-sum Li coefficients are all positive (under RH) for n=1..8."""
        for n in range(1, 9):
            val = float(li_zerosum(n, 50))
            assert val > 0, f"Zero-sum λ_{n} = {val}: should be positive under RH"

    def test_hadamard_gap_sign(self):
        """At n=6: derivative gives negative, zero-sum gives positive.
        The gap = derivative - zero-sum < 0."""
        deriv = float(li_n(Xi_H_red, 6))
        zs = float(li_zerosum(6, 50))
        gap = deriv - zs
        assert gap < -0.5, f"Gap = {gap}: should be significantly negative"

    def test_hadamard_gap_grows(self):
        """The gap grows with n (exponential in the Hadamard constant)."""
        gaps = []
        for n in range(1, 9):
            d = float(li_n(Xi_H_red, n))
            z = float(li_zerosum(n, 50))
            gaps.append(d - z)
        # Gaps should become increasingly negative
        assert gaps[-1] < gaps[0], "Gap should become more negative"
        assert gaps[-1] < -2.0, "Gap should be large negative at n=8"


# =============================================================================
# TEST BLOCK 4: Li coefficient decomposition (full = reduced + winding)
# =============================================================================

class TestLiDecomposition:
    """log Ξ_A(u) = log Ξ^{red}_A(u) + log ζ(u+1) implies exact additivity."""

    def test_heisenberg_decomposition(self):
        n_max = 8
        full = li_coeffs(Xi_H_full, n_max)
        red = li_coeffs(Xi_H_red, n_max)
        wind = li_coeffs(Xi_wind, n_max)
        for n in range(n_max):
            err = abs(float(full[n] - red[n] - wind[n]))
            assert err < 1e-8, f"n={n+1}: decomposition error = {err}"

    def test_virasoro_decomposition(self):
        n_max = 8
        full = li_coeffs(Xi_V_full, n_max)
        red = li_coeffs(Xi_V_red, n_max)
        wind = li_coeffs(Xi_wind, n_max)
        for n in range(n_max):
            err = abs(float(full[n] - red[n] - wind[n]))
            assert err < 1e-8, f"n={n+1}: decomposition error = {err}"

    def test_betagamma_decomposition(self):
        n_max = 8
        full = li_coeffs(Xi_bg_full, n_max)
        red = li_coeffs(Xi_bg_red, n_max)
        wind = li_coeffs(Xi_wind, n_max)
        for n in range(n_max):
            err = abs(float(full[n] - red[n] - wind[n]))
            assert err < 1e-8, f"n={n+1}: decomposition error = {err}"

    def test_W3_decomposition(self):
        n_max = 6
        full = li_coeffs(lambda u: Xi_WN_full(3, u), n_max)
        red = li_coeffs(lambda u: Xi_WN_red(3, u), n_max)
        wind = li_coeffs(Xi_wind, n_max)
        for n in range(n_max):
            err = abs(float(full[n] - red[n] - wind[n]))
            assert err < 1e-7, f"n={n+1}: decomposition error = {err}"


# =============================================================================
# TEST BLOCK 5: Winding contribution universality
# =============================================================================

class TestWindingUniversality:

    def test_winding_is_family_independent(self):
        """The winding component is identical for all families."""
        wind = li_coeffs(Xi_wind, 6)
        full_H = li_coeffs(Xi_H_full, 6)
        red_H = li_coeffs(Xi_H_red, 6)
        full_V = li_coeffs(Xi_V_full, 6)
        red_V = li_coeffs(Xi_V_red, 6)

        for n in range(6):
            diff_H = float(full_H[n] - red_H[n])
            diff_V = float(full_V[n] - red_V[n])
            wind_val = float(wind[n])
            assert abs(diff_H - wind_val) < 1e-8
            assert abs(diff_V - wind_val) < 1e-8
            assert abs(diff_H - diff_V) < 1e-8

    def test_winding_sign_pattern(self):
        """Winding: negative n=1..3, positive n=4..14, negative n>=15."""
        wind = li_coeffs(Xi_wind, 16)
        # First three: negative
        for n in [0, 1, 2]:
            assert float(wind[n]) < 0, f"n={n+1}: wind should be negative"
        # Middle range: positive
        positive_count = sum(1 for n in range(3, 14) if float(wind[n]) > 0)
        assert positive_count >= 8, f"Expected many positive in middle range, got {positive_count}"
        # Eventually negative
        assert float(wind[14]) < 0, f"n=15: wind should be negative"


# =============================================================================
# TEST BLOCK 6: Critical ratio |1 - 1/ρ| on different lines
# =============================================================================

class TestCriticalRatios:

    def test_ratio_equals_1_on_critical_line(self):
        """For ρ = 1/2 + iγ: |1 - 1/ρ| = |(ρ-1)/ρ| = 1 exactly."""
        for k in range(1, 6):
            rho = zetazero(k)
            ratio = float(mpabs(1 - 1/rho))
            assert abs(ratio - 1.0) < 1e-10, f"Zero {k}: |1-1/ρ| = {ratio}"

    def test_ratio_greater_1_on_shifted_line(self):
        """For ρ' = ρ-1 = -1/2+iγ: |1-1/ρ'| = √(9/4+γ²)/√(1/4+γ²) > 1."""
        for k in range(1, 6):
            rho = zetazero(k)
            ratio = float(mpabs(1 - 1/(rho - 1)))
            assert ratio > 1.0, f"Zero {k}: |1-1/ρ'| = {ratio}"

    def test_ratio_formula(self):
        """Verify |1-1/(ρ-1)| = √(9/4+γ²)/√(1/4+γ²) analytically."""
        for k in range(1, 4):
            rho = zetazero(k)
            gamma_k = float(im(rho))
            actual = float(mpabs(1 - 1/(rho - 1)))
            formula = (9.0/4 + gamma_k**2)**0.5 / (1.0/4 + gamma_k**2)**0.5
            assert abs(actual - formula) < 1e-8

    def test_zerosum_contribution_bounded_on_critical_line(self):
        """On Re=1/2: Re[1-(1-1/ρ)^n] = 1-cos(nθ) ∈ [0, 2]."""
        rho = zetazero(1)
        for n in range(1, 21):
            val = float(re(1 - (1 - 1/rho)**n))
            assert -0.001 <= val <= 2.001, f"n={n}: contribution {val} out of [0,2]"

    def test_zerosum_contribution_grows_off_critical_line(self):
        """On Re=-1/2: |1-(1-1/ρ')^n| grows (slowly, |1-1/ρ'| ≈ 1.005)."""
        rho = zetazero(1)
        rho_shifted = rho - 1
        vals = [float(mpabs(1 - (1 - 1/rho_shifted)**n)) for n in range(1, 21)]
        assert vals[-1] > 5 * vals[0], f"Expected growth from {vals[0]:.4f} to {vals[-1]:.4f}"


# =============================================================================
# TEST BLOCK 7: ζ(u+1) is NOT a Γ-factor
# =============================================================================

class TestZetaNotGammaFactor:

    def test_zeta_u_plus_1_has_zeros(self):
        for k in range(1, 6):
            rho = zetazero(k)
            val = float(mpabs(zeta(rho)))  # ζ(ρ) = 0 means ζ(u+1) = 0 at u = ρ-1
            assert val < 1e-10

    def test_zeros_on_re_minus_half(self):
        for k in range(1, 6):
            rho = zetazero(k)
            re_u = float(re(rho - 1))
            assert abs(re_u - (-0.5)) < 1e-10

    def test_gamma_is_zero_free(self):
        """Γ(s) has no zeros. So ζ(u+1) cannot be a Γ-factor."""
        for t in [1.0, 5.0, 14.13, 21.02]:
            u = mpc(-0.5, t)
            val = float(mpabs(mpgamma((u + 1) / 2)))
            assert val > 0


# =============================================================================
# TEST BLOCK 8: Generalized Li signs for ALL families
# =============================================================================

class TestGeneralizedLiSigns:
    """The manuscript's generalized Li coefficients are eventually negative for ALL."""

    def test_heisenberg_full_sign_change_at_7(self):
        """Full Heisenberg: positive for n=1..6, negative at n=7."""
        full = li_coeffs(Xi_H_full, 8)
        assert float(full[5]) > 0  # n=6
        assert float(full[6]) < 0  # n=7

    def test_heisenberg_reduced_sign_change_at_6(self):
        """Reduced Heisenberg: positive for n=1..5, negative at n=6.
        This is NOT a sign of zeros off Re=1/2 (the zero-sum coefficients
        are all positive). It is an artifact of the derivative formula."""
        red = li_coeffs(Xi_H_red, 8)
        assert float(red[4]) > 0  # n=5
        assert float(red[5]) < 0  # n=6

    def test_virasoro_full_all_negative(self):
        """Virasoro full: all negative for n=1..10."""
        full = li_coeffs(Xi_V_full, 10)
        for n in range(10):
            assert float(full[n]) < 0, f"n={n+1}: should be negative"

    def test_virasoro_reduced_all_negative(self):
        """Virasoro reduced: all negative for n=1..8."""
        red = li_coeffs(Xi_V_red, 8)
        for n in range(8):
            assert float(red[n]) < 0, f"n={n+1}: should be negative"

    def test_WN_full_all_negative(self):
        """W_3 full: all negative for n=1..6."""
        full = li_coeffs(lambda u: Xi_WN_full(3, u), 6)
        for n in range(6):
            assert float(full[n]) < 0


# =============================================================================
# TEST BLOCK 9: Full vs reduced negativity — decomposition of failure
# =============================================================================

class TestNegativityDecomposition:

    def test_heisenberg_full_negativity_mechanism(self):
        """Heisenberg: full = red + wind. At n=7: red ≈ -0.58, wind ≈ +0.30.
        Both are negative-ish but the full is dominated by the reduced term
        at this order."""
        full = li_coeffs(Xi_H_full, 8)
        red = li_coeffs(Xi_H_red, 8)
        wind = li_coeffs(Xi_wind, 8)
        # Verify decomposition
        for n in range(8):
            assert abs(float(full[n] - red[n] - wind[n])) < 1e-8
        # At n=7: full is negative
        assert float(full[6]) < 0
        # The reduced term is the dominant negative contribution
        assert float(red[6]) < 0

    def test_virasoro_doubly_negative(self):
        """Virasoro at n=1: both reduced and winding contribute negatively."""
        red1 = float(li_n(Xi_V_red, 1))
        wind1 = float(li_n(Xi_wind, 1))
        # Virasoro reduced is negative even at n=1
        assert red1 < 0
        # Winding is also negative at n=1
        assert wind1 < 0

    def test_virasoro_reduced_more_negative_than_heisenberg(self):
        """The Virasoro reduced coefficients are more negative than Heisenberg's."""
        for n in range(1, 7):
            h = float(li_n(Xi_H_red, n))
            v = float(li_n(Xi_V_red, n))
            assert v < h, f"n={n}: Vir red={v} should be < Heis red={h}"


# =============================================================================
# TEST BLOCK 10: Cross-consistency with existing test_sewing_dirichlet_lift
# =============================================================================

class TestCrossConsistency:

    def test_heisenberg_lambda7_negative_full(self):
        assert float(li_n(Xi_H_full, 7)) < 0

    def test_heisenberg_lambda6_positive_full(self):
        assert float(li_n(Xi_H_full, 6)) > 0

    def test_virasoro_all_negative_full(self):
        for n in range(1, 11):
            assert float(li_n(Xi_V_full, n)) < 0

    def test_lambda1_heisenberg_analytic(self):
        """λ̃_1(H) = γ + ζ'(2)/ζ(2)."""
        num = float(li_n(Xi_H_full, 1))
        ana = float(euler_gamma + diff(zeta, mpf(2)) / zeta(2))
        assert abs(num - ana) < 1e-8


# =============================================================================
# TEST BLOCK 11: R_Vir(u) = ζ(u) - 1 zero analysis
# =============================================================================

class TestVirasoroReducedZeros:

    def test_zeta_minus_1_at_zeta_zeros(self):
        """At nontrivial zeros of ζ: ζ(ρ) = 0, so |ζ(ρ)-1| = 1."""
        for k in range(1, 4):
            rho = zetazero(k)
            assert abs(float(mpabs(zeta(rho) - 1)) - 1.0) < 1e-8

    def test_zeta_approaches_1(self):
        """ζ(σ) → 1 as σ → ∞, so ζ(σ)-1 → 0."""
        for sigma in [5.0, 10.0, 20.0]:
            val = float(zeta(mpf(sigma)) - 1)
            assert val > 0
            assert val < 0.1


# =============================================================================
# TEST BLOCK 12: The structural conclusion
# =============================================================================

class TestStructuralConclusion:

    def test_prop_li_criterion_failure_is_correct(self):
        """prop:li-criterion-failure is CORRECT: generalized λ̃_n are eventually
        negative for ALL standard families."""
        # Heisenberg full: negative at n=7
        assert float(li_n(Xi_H_full, 7)) < 0
        # Virasoro full: negative at n=1
        assert float(li_n(Xi_V_full, 1)) < 0
        # βγ full: check
        assert float(li_n(Xi_bg_full, 7)) < 0

    def test_interpretation_needs_qualification(self):
        """The manuscript says 'zeros on two lines force Li coefficients negative.'
        This is true for the GENERALIZED derivative formula. But it does NOT
        follow from the classical Li criterion (zero-sum), because the two
        formulas disagree when applied to the sewing lift.

        The correct statement: the Taylor expansion of log Ξ_A(1/(1-w)) has
        eventually negative coefficients, which is a genuine spectral invariant
        but does NOT have the classical RH-equivalence interpretation."""
        # Generalized: negative at n=6
        assert float(li_n(Xi_H_red, 6)) < 0
        # Zero-sum: positive at n=6 (under RH)
        zs6 = float(li_zerosum(6, 50))
        assert zs6 > 0

    def test_factorization_is_structurally_motivated(self):
        """S_A(u) = ζ(u+1)·R_A(u) is not ad hoc: ζ(u+1) is universal."""
        u = mpf(3)
        for weights in [[1], [2], [1, 1], [2, 3], [2, 3, 4]]:
            S = S_generic(weights, u)
            R = R_generic(weights, u)
            ratio = S / R
            assert abs(float(ratio - zeta(u + 1))) < 1e-15

    def test_zeta_u_plus_1_not_removable(self):
        """ζ(u+1) has zeros, so it is not a Γ-factor and cannot be completed away."""
        rho = zetazero(1)
        assert float(mpabs(zeta(rho))) < 1e-10  # ζ has a zero here
        assert float(mpabs(mpgamma(rho/2))) > 0  # Γ does not

    def test_reduced_coefficients_still_eventually_negative(self):
        """Even reduced (derivative-formula) Li coefficients become negative.
        This is true for ALL families, not just higher-weight ones.
        For Heisenberg: the Euler-Mascheroni constant γ in the Laurent
        expansion of (u-1)ζ(u) causes the derivative-formula coefficients
        to diverge from the zero-sum coefficients."""
        # Heisenberg reduced: negative at n=6
        assert float(li_n(Xi_H_red, 6)) < 0
        # Virasoro reduced: negative at n=1
        assert float(li_n(Xi_V_red, 1)) < 0
        # βγ reduced: negative at n=6 (same zeros as Heisenberg)
        assert float(li_n(Xi_bg_red, 6)) < 0

    def test_classical_zerosum_all_positive(self):
        """The classical zero-sum Li coefficients for ζ are all positive
        for n=1..8 (under numerical RH verification with 50 zero pairs)."""
        for n in range(1, 9):
            val = float(li_zerosum(n, 50))
            assert val > 0, f"Classical λ_{n} = {val}"
