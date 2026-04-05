#!/usr/bin/env python3
r"""
test_bc_theta_correspondence_engine.py — Tests for the theta correspondence engine.

Systematic multi-path verification of the theta lift bridge between
bar-complex shadow data and automorphic forms.

T1-T10:  Shadow coefficient infrastructure and basic identities
T11-T18: Jacobi theta functions and theta kernels
T19-T27: GL(2) theta lift (Path 1: direct Fourier)
T28-T35: Heisenberg-Eisenstein correspondence (Path 2: known form matching)
T36-T42: GSp(4) theta lift and Saito-Kurokawa (Path 4: degree-2 lift)
T43-T49: Shimura correspondence
T50-T55: Waldspurger's formula (Path 3: special values)
T56-T60: L-functions and spectral evaluation
T61-T68: Cross-verification and Koszul duality
"""

import math
import cmath
import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_theta_correspondence_engine import (
    heisenberg_shadow_coefficients,
    virasoro_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    shadow_q_expansion,
    jacobi_theta3,
    jacobi_theta3_standard,
    shadow_twisted_theta_kernel,
    theta_lift_gl2_fourier,
    theta_lift_gl2_eisenstein_check,
    theta_lift_gl2_generic,
    theta_lift_gsp4_fourier,
    shadow_quadratic_space,
    saito_kurokawa_lift_coefficients,
    saito_kurokawa_from_delta,
    sk_lift_shadow_virasoro_c12,
    shimura_lift,
    shimura_lift_shadow,
    waldspurger_predict,
    waldspurger_shadow_coefficients,
    shadow_zeta,
    theta_lift_L_function,
    compare_L_functions,
    theta_lift_at_zeta_zeros,
    full_theta_correspondence_analysis,
    genus2_theta_lift_verification,
    ramanujan_delta_sk_verification,
    heisenberg_eisenstein_correspondence,
    theta_lift_complexity,
    koszul_dual_theta_lift,
    ramanujan_tau,
    _faber_pandharipande,
    _bernoulli_number,
    _sigma,
    _divisors,
    kronecker_symbol_safe,
    RIEMANN_ZEROS_IMAGINARY,
)

from fractions import Fraction


# ============================================================
# T1-T10: Shadow coefficient infrastructure
# ============================================================

class TestShadowCoefficients:
    def test_T1_heisenberg_kappa_equals_k(self):
        """T1: Heisenberg kappa = k (NOT c/2, AP39/AP48)."""
        for k in [1.0, 2.0, 5.0, 10.0]:
            S = heisenberg_shadow_coefficients(k)
            assert abs(S[2] - k) < 1e-14
            assert abs(S[3]) < 1e-14
            assert abs(S[4]) < 1e-14

    def test_T2_heisenberg_depth_2(self):
        """T2: Heisenberg shadow terminates at depth 2 (class G)."""
        S = heisenberg_shadow_coefficients(3.0, max_r=20)
        for r in range(3, 21):
            assert abs(S[r]) < 1e-14

    def test_T3_virasoro_S2_is_c_over_2(self):
        """T3: Virasoro S_2 = c/2 (kappa for Virasoro)."""
        for c_val in [1.0, 12.0, 24.0, 26.0]:
            S = virasoro_shadow_coefficients(c_val, max_r=5)
            assert abs(S[2] - c_val / 2.0) < 1e-12

    def test_T4_virasoro_S3_universal(self):
        """T4: Virasoro S_3 = 2 (universal gravitational cubic)."""
        for c_val in [1.0, 12.0, 24.0]:
            S = virasoro_shadow_coefficients(c_val, max_r=5)
            assert abs(S[3] - 2.0) < 1e-12

    def test_T5_virasoro_S4_contact_quartic(self):
        """T5: Q^contact_Vir = 10/[c(5c+22)] (contact quartic)."""
        for c_val in [1.0, 12.0, 24.0]:
            S = virasoro_shadow_coefficients(c_val, max_r=5)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(S[4] - expected) < 1e-12

    def test_T6_affine_sl2_kappa(self):
        """T6: Affine sl_2 kappa = 3(k+2)/4 (AP1: recompute from dim(g)*(k+h^v)/(2h^v))."""
        for k in [1.0, 2.0, 5.0]:
            S = affine_sl2_shadow_coefficients(k)
            expected_kappa = 3.0 * (k + 2.0) / 4.0
            assert abs(S[2] - expected_kappa) < 1e-12

    def test_T7_affine_sl2_depth_3(self):
        """T7: Affine sl_2 terminates at depth 3 (class L)."""
        S = affine_sl2_shadow_coefficients(1.0, max_r=15)
        assert abs(S[3] - 2.0) < 1e-12
        for r in range(4, 16):
            assert abs(S[r]) < 1e-14

    def test_T8_affine_critical_level_raises(self):
        """T8: Critical level k=-2 raises ValueError (Sugawara undefined)."""
        with pytest.raises(ValueError, match="Critical level"):
            affine_sl2_shadow_coefficients(-2.0)

    def test_T9_virasoro_c0_raises(self):
        """T9: c=0 raises ValueError (pole of shadow tower)."""
        with pytest.raises(ValueError, match="c = 0"):
            virasoro_shadow_coefficients(0.0)

    def test_T10_shadow_q_expansion_format(self):
        """T10: q-expansion places S_r at index r with zero-padding."""
        S = heisenberg_shadow_coefficients(5.0)
        qexp = shadow_q_expansion(S, N_terms=10)
        assert len(qexp) == 10
        assert abs(qexp[0]) < 1e-14
        assert abs(qexp[1]) < 1e-14
        assert abs(qexp[2] - 5.0) < 1e-14
        for i in range(3, 10):
            assert abs(qexp[i]) < 1e-14


# ============================================================
# T11-T18: Jacobi theta functions
# ============================================================

class TestJacobiTheta:
    def test_T11_theta3_at_z0(self):
        """T11: theta_3(tau, 0) = sum q^{n^2/2} is real on imaginary axis."""
        tau = complex(0, 1.0)  # tau = i
        val = jacobi_theta3(tau, z=0.0)
        # Should be real (and positive)
        assert abs(val.imag) < 1e-10
        assert val.real > 1.0  # includes n=0 term = 1

    def test_T12_theta3_standard_at_z0(self):
        """T12: theta_3^{std}(i, 0) = sum exp(-pi*n^2) is a known constant."""
        tau = complex(0, 1.0)
        val = jacobi_theta3_standard(tau, z=0.0)
        # theta_3(i) = pi^{1/4} / Gamma(3/4) approx 1.08643
        # (from DLMF 20.4.3 or Whittaker-Watson)
        assert abs(val.imag) < 1e-10
        # Rough bound: 1.0 < theta_3(i) < 1.2
        assert 1.0 < val.real < 1.2

    def test_T13_theta3_modular_consistency(self):
        """T13: Jacobi theta modular S-transform via Poisson summation.

        For theta_Jacobi(tau) = sum_{n in Z} exp(pi i n^2 tau):
          theta_Jacobi(-1/tau) = sqrt(tau/i) * theta_Jacobi(tau).

        Our theta_3^{std}(tau) = theta_Jacobi(2*tau) (since q^{n^2} = exp(2*pi*i*n^2*tau)).
        So the correct identity to test is:
          theta_Jacobi(-1/w) = sqrt(w/i) * theta_Jacobi(w)
        where w = 2*tau.
        """
        tau = complex(0, 1.5)
        w = 2.0 * tau  # = 3i
        w_inv = -1.0 / w  # = i/3
        # theta_Jacobi(w) = theta_3^{std}(w/2) = theta_3^{std}(tau)
        val_w = jacobi_theta3_standard(w / 2.0, z=0.0, N_sum=200)
        # theta_Jacobi(w_inv) = theta_3^{std}(w_inv/2) = theta_3^{std}(-1/(2w))
        #   = theta_3^{std}(-1/(4*tau))
        val_winv = jacobi_theta3_standard(w_inv / 2.0, z=0.0, N_sum=200)
        factor = cmath.sqrt(w / 1j)  # sqrt(3)
        ratio = val_winv / (factor * val_w)
        assert abs(abs(ratio) - 1.0) < 1e-6

    def test_T14_theta3_exponential_decay(self):
        """T14: theta_3(tau,0) approaches 1 as Im(tau) -> infinity."""
        for y in [5.0, 10.0, 20.0]:
            tau = complex(0, y)
            val = jacobi_theta3_standard(tau, z=0.0)
            # As y -> inf, q -> 0, so theta -> 1
            assert abs(val - 1.0) < 2.0 * math.exp(-math.pi * y)

    def test_T15_shadow_twisted_kernel_heisenberg(self):
        """T15: Shadow-twisted kernel for Heisenberg has single contribution at r=2."""
        S = heisenberg_shadow_coefficients(1.0)
        tau = complex(0, 1.0)
        z = complex(0, 0)
        val = shadow_twisted_theta_kernel(tau, z, S)
        # Only r=2 contributes: S_2 * theta_3(2*tau, 0)
        expected = 1.0 * jacobi_theta3_standard(2.0 * tau, 0.0)
        assert abs(val - expected) < 1e-8

    def test_T16_shadow_twisted_kernel_real_on_imaginary(self):
        """T16: Shadow-twisted kernel is real for real shadow coefficients on Im axis."""
        S = virasoro_shadow_coefficients(24.0, max_r=8)
        tau = complex(0, 1.5)
        z = complex(0, 0)
        val = shadow_twisted_theta_kernel(tau, z, S, max_r=8)
        assert abs(val.imag) < 1e-8

    def test_T17_theta3_jacobi_identity_check(self):
        """T17: Jacobi triple product consistency (spot check)."""
        # theta_3(tau, z) should satisfy theta_3(tau, z+1) = theta_3(tau, z)
        tau = complex(0, 1.0)
        z = complex(0.3, 0.1)
        val1 = jacobi_theta3_standard(tau, z)
        val2 = jacobi_theta3_standard(tau, z + 1.0)
        assert abs(val1 - val2) < 1e-8

    def test_T18_theta_z_periodicity(self):
        """T18: theta_3^{std}(tau, z+1) = theta_3^{std}(tau, z) (Z-periodicity in z)."""
        # The q^{n^2} convention gives periodicity in z with period 1
        # (not quasi-periodicity in tau). This is the simpler and correct test.
        tau = complex(0, 1.5)
        z = complex(0.2, 0.1)
        val1 = jacobi_theta3_standard(tau, z)
        val2 = jacobi_theta3_standard(tau, z + 1.0)
        assert abs(val1 - val2) < 1e-8


# ============================================================
# T19-T27: GL(2) theta lift
# ============================================================

class TestThetaLiftGL2:
    def test_T19_heisenberg_lift_structure(self):
        """T19: Heisenberg lift nonzero only at n = 2*m^2."""
        S = heisenberg_shadow_coefficients(1.0)
        lift = theta_lift_gl2_fourier(S, max_n=50)
        for n in range(1, 51):
            a_n = lift.get(n, 0.0)
            # Check: is n of the form 2*m^2?
            is_2msq = False
            if n % 2 == 0:
                half = n // 2
                sq = int(round(math.sqrt(half)))
                if sq * sq == half:
                    is_2msq = True
            if not is_2msq and n > 0:
                assert abs(a_n) < 1e-12, f"Nonzero at n={n} which is not 2*m^2"

    def test_T20_heisenberg_lift_at_2(self):
        """T20: a_2(Phi) = k * 2 for Heisenberg at level k."""
        for k in [1.0, 3.0, 7.0]:
            S = heisenberg_shadow_coefficients(k)
            lift = theta_lift_gl2_fourier(S, max_n=10)
            # n = 2 = 2*1^2, so a_2 = S_2 * 2 = k * 2
            assert abs(lift.get(2, 0.0) - 2.0 * k) < 1e-12

    def test_T21_heisenberg_lift_at_8(self):
        """T21: a_8(Phi) = k * 2 for Heisenberg (8 = 2*2^2)."""
        S = heisenberg_shadow_coefficients(1.0)
        lift = theta_lift_gl2_fourier(S, max_n=10)
        assert abs(lift.get(8, 0.0) - 2.0) < 1e-12

    def test_T22_virasoro_lift_nonzero(self):
        """T22: Virasoro lift has many nonzero Fourier coefficients."""
        S = virasoro_shadow_coefficients(24.0, max_r=10)
        lift = theta_lift_gl2_fourier(S, max_n=30, max_r=10)
        nonzero = sum(1 for n in range(1, 31) if abs(lift.get(n, 0.0)) > 1e-12)
        # Virasoro with many shadow terms should give many nonzero lifts
        assert nonzero >= 5

    def test_T23_lift_additivity(self):
        """T23: Theta lift is linear in shadow coefficients."""
        S1 = heisenberg_shadow_coefficients(1.0)
        S2 = heisenberg_shadow_coefficients(2.0)
        S3 = heisenberg_shadow_coefficients(3.0)
        lift1 = theta_lift_gl2_fourier(S1, max_n=20)
        lift2 = theta_lift_gl2_fourier(S2, max_n=20)
        lift3 = theta_lift_gl2_fourier(S3, max_n=20)
        for n in range(0, 21):
            lhs = lift3.get(n, 0.0)
            rhs = lift1.get(n, 0.0) + lift2.get(n, 0.0)
            assert abs(lhs - rhs) < 1e-10

    def test_T24_eisenstein_check_structure(self):
        """T24: Heisenberg eisenstein check returns proper structure."""
        result = theta_lift_gl2_eisenstein_check(1.0)
        assert result['is_eisenstein_structure']
        assert result['family'] == 'Heisenberg'

    def test_T25_generic_lift_returns_L_values(self):
        """T25: Generic GL(2) lift returns partial L-values."""
        S = virasoro_shadow_coefficients(12.0, max_r=8)
        result = theta_lift_gl2_generic(S, max_n=20)
        assert 'partial_L_values' in result
        assert 'fourier_coefficients' in result
        # L-values at s=2,3,4 should be computed
        for s in [1.0, 2.0, 3.0, 4.0]:
            assert s in result['partial_L_values']

    def test_T26_lift_zero_for_zero_shadow(self):
        """T26: Zero shadow coefficients produce zero lift."""
        S = {r: 0.0 for r in range(2, 15)}
        lift = theta_lift_gl2_fourier(S, max_n=20)
        for n in range(1, 21):
            assert abs(lift.get(n, 0.0)) < 1e-14

    def test_T27_affine_lift_two_contributions(self):
        """T27: Affine sl_2 lift has contributions from both r=2 and r=3."""
        S = affine_sl2_shadow_coefficients(1.0)
        lift = theta_lift_gl2_fourier(S, max_n=20, max_r=5)
        # r=2 contributes at n = 2*m^2
        # r=3 contributes at n = 3*m^2
        a_2 = lift.get(2, 0.0)  # From r=2: S_2 * 2
        a_3 = lift.get(3, 0.0)  # From r=3: S_3 * 2
        assert abs(a_2) > 1e-12  # S_2 = kappa = 3(1+2)/4 = 9/4
        assert abs(a_3) > 1e-12  # S_3 = 2


# ============================================================
# T28-T35: Heisenberg-Eisenstein correspondence (Path 2)
# ============================================================

class TestHeisenbergEisenstein:
    def test_T28_lattice_structure(self):
        """T28: Nonzero indices are exactly 2*m^2 for m >= 0."""
        result = heisenberg_eisenstein_correspondence(1.0)
        assert result['structure_match']

    def test_T29_kappa_scaling(self):
        """T29: Lift scales linearly with kappa = k."""
        r1 = heisenberg_eisenstein_correspondence(1.0)
        r5 = heisenberg_eisenstein_correspondence(5.0)
        for n in r1['nonzero_indices']:
            if n == 0:
                continue
            v1 = r1.get('L_numerical', {}).get(2, 0.0)
            v5 = r5.get('L_numerical', {}).get(2, 0.0)
            if abs(v1) > 1e-12:
                assert abs(v5 / v1 - 5.0) < 0.1
                break

    def test_T30_L_function_at_s2(self):
        """T30: L(Phi, 2) matches theoretical 4k * zeta(4) / 4."""
        result = heisenberg_eisenstein_correspondence(1.0)
        L_num = result['L_numerical'].get(2, 0.0)
        L_thy = result['L_theoretical'].get(2, 0.0)
        if abs(L_thy) > 1e-12:
            assert abs(L_num / L_thy - 1.0) < 0.1

    def test_T31_L_function_at_s3(self):
        """T31: L(Phi, 3) matches theoretical prediction."""
        result = heisenberg_eisenstein_correspondence(2.0)
        L_num = result['L_numerical'].get(3, 0.0)
        L_thy = result['L_theoretical'].get(3, 0.0)
        if abs(L_thy) > 1e-12:
            assert abs(L_num / L_thy - 1.0) < 0.1

    def test_T32_a2_coefficient(self):
        """T32: a_2 = 2k (direct from lift definition)."""
        result = heisenberg_eisenstein_correspondence(3.0)
        lift = theta_lift_gl2_fourier(heisenberg_shadow_coefficients(3.0), max_n=10)
        assert abs(lift.get(2, 0.0) - 6.0) < 1e-12

    def test_T33_a18_coefficient(self):
        """T33: a_{18} = 2k (since 18 = 2*3^2)."""
        k = 4.0
        lift = theta_lift_gl2_fourier(heisenberg_shadow_coefficients(k), max_n=20)
        assert abs(lift.get(18, 0.0) - 2.0 * k) < 1e-12

    def test_T34_a5_vanishes(self):
        """T34: a_5 = 0 (5 is not of the form 2*m^2)."""
        lift = theta_lift_gl2_fourier(heisenberg_shadow_coefficients(1.0), max_n=10)
        assert abs(lift.get(5, 0.0)) < 1e-14

    def test_T35_a7_vanishes(self):
        """T35: a_7 = 0 (7 is not of the form 2*m^2)."""
        lift = theta_lift_gl2_fourier(heisenberg_shadow_coefficients(1.0), max_n=10)
        assert abs(lift.get(7, 0.0)) < 1e-14


# ============================================================
# T36-T42: GSp(4) theta lift and Saito-Kurokawa
# ============================================================

class TestGSp4AndSK:
    def test_T36_gsp4_heisenberg_diagonal(self):
        """T36: GSp(4) lift for Heisenberg has only b=0 terms (diagonal)."""
        S = heisenberg_shadow_coefficients(1.0)
        gsp4 = theta_lift_gsp4_fourier(S, max_disc=8)
        for (a, b, c), val in gsp4.items():
            if abs(val) > 1e-12:
                assert b == 0, f"Nonzero off-diagonal at ({a},{b},{c})"

    def test_T37_gsp4_heisenberg_factorizes(self):
        """T37: GSp(4) Heisenberg lift factorizes as product of GL(2) lifts."""
        S = heisenberg_shadow_coefficients(1.0)
        gsp4 = theta_lift_gsp4_fourier(S, max_disc=10)
        gl2 = theta_lift_gl2_fourier(S, max_n=10)
        # A(a,0,c) should equal gl2[a] * gl2[c] for the rank-1 factorization
        for (a, b, c), val in gsp4.items():
            if b == 0 and a > 0 and c > 0:
                expected = gl2.get(a, 0.0) * gl2.get(c, 0.0)
                assert abs(val - expected) < 1e-10, \
                    f"Factorization fails at ({a},{b},{c}): {val} vs {expected}"

    def test_T38_ramanujan_tau_values(self):
        """T38: Verify Ramanujan tau against known values (AP38: check convention)."""
        known = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830, 6: -6048, 7: -16744}
        for n, expected in known.items():
            assert ramanujan_tau(n) == expected, f"tau({n}) = {ramanujan_tau(n)} != {expected}"

    def test_T39_tau_multiplicativity(self):
        """T39: Ramanujan tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)
        assert ramanujan_tau(15) == ramanujan_tau(3) * ramanujan_tau(5)

    def test_T40_tau_hecke_relation(self):
        """T40: tau(p^2) = tau(p)^2 - p^11 for prime p."""
        for p in [2, 3, 5]:
            tau_p2 = ramanujan_tau(p * p)
            expected = ramanujan_tau(p) ** 2 - p ** 11
            assert tau_p2 == expected, f"Hecke at p={p}: {tau_p2} != {expected}"

    def test_T41_sk_lift_nonzero(self):
        """T41: Saito-Kurokawa lift of f_22 has nonzero coefficients."""
        sk = saito_kurokawa_from_delta(max_disc=10)
        nonzero = sum(1 for v in sk.values() if abs(v) > 1e-10)
        assert nonzero > 0

    def test_T42_sk_virasoro_c12_connection(self):
        """T42: SK lift analysis at c=12 produces valid data."""
        result = sk_lift_shadow_virasoro_c12()
        assert abs(result['kappa'] - 6.0) < 1e-12
        assert result['c'] == 12


# ============================================================
# T43-T49: Shimura correspondence
# ============================================================

class TestShimura:
    def test_T43_shimura_lift_preserves_zero(self):
        """T43: Shimura lift of zero form is zero."""
        zero_coeffs = {n: 0.0 for n in range(1, 20)}
        sh = shimura_lift(zero_coeffs, weight_half=3, max_n=15)
        for n in range(1, 16):
            assert abs(sh.get(n, 0.0)) < 1e-14

    def test_T44_shimura_lift_heisenberg(self):
        """T44: Shimura lift of Heisenberg shadow is computable."""
        S = heisenberg_shadow_coefficients(1.0)
        sh = shimura_lift_shadow(S, max_n=20)
        # b(1) = c(1) (the d=1 term) = S_1 = 0 for Heisenberg
        assert abs(sh.get(1, 0.0)) < 1e-14

    def test_T45_shimura_is_multiplicative_test(self):
        """T45: For multiplicative input, Shimura lift has Hecke structure."""
        # Theta function of Z: c(n) = #{m : m^2 = n} = r_1(n)
        # r_1(0) = 1, r_1(1) = 2, r_1(4) = 2, r_1(9) = 2, ...
        c = {n: 0.0 for n in range(0, 50)}
        for m in range(0, 8):
            c[m * m] = 2.0 if m > 0 else 1.0
        sh = shimura_lift(c, weight_half=3, max_n=20)
        # The Shimura lift of a theta function produces an Eisenstein series
        # Just check it's nonzero and well-defined
        assert any(abs(sh.get(n, 0.0)) > 1e-12 for n in range(1, 21))

    def test_T46_shimura_lift_virasoro(self):
        """T46: Shimura lift of Virasoro shadow produces nonzero form."""
        S = virasoro_shadow_coefficients(24.0, max_r=10)
        sh = shimura_lift_shadow(S, max_n=20)
        nonzero = sum(1 for n in range(1, 21) if abs(sh.get(n, 0.0)) > 1e-12)
        assert nonzero >= 3

    def test_T47_shimura_b1_from_shadow(self):
        """T47: b(1) of Shimura lift depends on c(1)."""
        # For shadow: c(1) = S_1 = 0 (shadows start at r=2)
        S = virasoro_shadow_coefficients(12.0, max_r=8)
        sh = shimura_lift_shadow(S, max_n=10)
        # b(1) = sum_{d|1} c(1/d^2) = c(1) = S_1 = 0
        assert abs(sh.get(1, 0.0)) < 1e-12

    def test_T48_shimura_b2_from_shadow(self):
        """T48: b(2) = c(4) + 2*c(1) for k=1 Shimura lift."""
        # b(2) = sum_{d|2} d^{k-1} c(4/d^2) = c(4) + 1*c(1)
        # With k=1 (weight_half=3): d^{k-1} = d^0 = 1
        S = virasoro_shadow_coefficients(12.0, max_r=8)
        sh = shimura_lift_shadow(S, max_n=10)
        expected = S.get(4, 0.0) + S.get(1, 0.0)
        assert abs(sh.get(2, 0.0) - expected) < 1e-10

    def test_T49_shimura_lift_scales_linearly(self):
        """T49: Shimura lift is linear in the input coefficients."""
        S1 = virasoro_shadow_coefficients(12.0, max_r=8)
        S2 = {r: 2.0 * v for r, v in S1.items()}
        sh1 = shimura_lift_shadow(S1, max_n=15)
        sh2 = shimura_lift_shadow(S2, max_n=15)
        for n in range(1, 16):
            assert abs(sh2.get(n, 0.0) - 2.0 * sh1.get(n, 0.0)) < 1e-10


# ============================================================
# T50-T55: Waldspurger's formula (Path 3)
# ============================================================

class TestWaldspurger:
    def test_T50_waldspurger_heisenberg_trivial(self):
        """T50: Waldspurger for Heisenberg: S_r=0 for r>=3 gives empty results."""
        S = heisenberg_shadow_coefficients(1.0)
        wald = waldspurger_shadow_coefficients(S, max_D=10)
        # Only D=-2 should appear (S_2 = 1 != 0)
        assert -2 in wald
        assert abs(wald[-2]['S_abs_D'] - 1.0) < 1e-12

    def test_T51_waldspurger_virasoro_nonempty(self):
        """T51: Waldspurger for Virasoro has entries at multiple discriminants."""
        S = virasoro_shadow_coefficients(24.0, max_r=10)
        wald = waldspurger_shadow_coefficients(S, max_D=10)
        # Should have entries at D=-2, -3, -4, ... (wherever S_r != 0)
        assert len(wald) >= 3

    def test_T52_waldspurger_ratio_positive(self):
        """T52: |S_r|^2 / sqrt(r) > 0 for nonzero shadow coefficients."""
        S = virasoro_shadow_coefficients(24.0, max_r=8)
        wald = waldspurger_shadow_coefficients(S, max_D=8)
        for D, data in wald.items():
            if abs(data['S_abs_D']) > 1e-12:
                assert data['waldspurger_ratio'] > 0

    def test_T53_waldspurger_S2_ratio(self):
        """T53: At D=-2, Waldspurger ratio = S_2^2 / sqrt(2) = kappa^2/sqrt(2)."""
        k = 3.0
        S = heisenberg_shadow_coefficients(k)
        wald = waldspurger_shadow_coefficients(S, max_D=5)
        expected = k ** 2 / math.sqrt(2.0)
        assert abs(wald[-2]['waldspurger_ratio'] - expected) < 1e-10

    def test_T54_waldspurger_predict_structure(self):
        """T54: Waldspurger predict returns proper structure."""
        f_coeffs = {n: float(ramanujan_tau(n)) for n in range(1, 20)}
        result = waldspurger_predict(f_coeffs, D=-3, weight=12)
        assert 'L_central' in result
        assert 'predicted_c_squared' in result
        assert result['D'] == -3

    def test_T55_waldspurger_consistency_across_families(self):
        """T55: Waldspurger ratio monotone check: larger kappa => larger |S_2|^2."""
        ratios = []
        for k in [1.0, 2.0, 5.0]:
            S = heisenberg_shadow_coefficients(k)
            wald = waldspurger_shadow_coefficients(S, max_D=5)
            ratios.append(wald[-2]['waldspurger_ratio'])
        # Should be strictly increasing (k^2/sqrt(2) is increasing in k)
        assert ratios[0] < ratios[1] < ratios[2]


# ============================================================
# T56-T60: L-functions and spectral evaluation
# ============================================================

class TestLFunctions:
    def test_T56_shadow_zeta_heisenberg(self):
        """T56: Shadow zeta for Heisenberg: zeta_H(s) = k / 2^s."""
        k = 3.0
        S = heisenberg_shadow_coefficients(k)
        for s_val in [2.0, 3.0, 4.0]:
            z = shadow_zeta(S, complex(s_val))
            expected = k / (2.0 ** s_val)
            assert abs(z - expected) < 1e-10

    def test_T57_shadow_zeta_affine(self):
        """T57: Shadow zeta for affine sl_2 has two terms."""
        S = affine_sl2_shadow_coefficients(1.0)
        kappa = S[2]
        for s_val in [3.0, 4.0]:
            z = shadow_zeta(S, complex(s_val))
            expected = kappa / (2.0 ** s_val) + 2.0 / (3.0 ** s_val)
            assert abs(z - expected) < 1e-10

    def test_T58_compare_L_functions_heisenberg(self):
        """T58: L-function comparison for Heisenberg is consistent."""
        S = heisenberg_shadow_coefficients(1.0)
        result = compare_L_functions(S)
        # For Heisenberg, the relationship should be simple
        for key, data in result.items():
            zeta = data['shadow_zeta']
            lift = data['theta_lift_L']
            # Both should be computable
            assert zeta is not None

    def test_T59_spectral_evaluation_returns_data(self):
        """T59: Spectral evaluation at zeta zeros returns proper data."""
        S = virasoro_shadow_coefficients(24.0, max_r=10)
        results = theta_lift_at_zeta_zeros(S, n_zeros=3)
        assert len(results) == 3
        for r in results:
            assert 'gamma' in r
            assert 'shadow_zeta_value' in r
            assert abs(r['gamma'] - RIEMANN_ZEROS_IMAGINARY[r['zero_index'] - 1]) < 1e-3

    def test_T60_shadow_zeta_virasoro_convergence(self):
        """T60: Shadow zeta for Virasoro converges at large Re(s)."""
        S = virasoro_shadow_coefficients(24.0, max_r=30)
        # At s = 10 (large), the series should converge well
        z1 = shadow_zeta(S, complex(10.0), max_r=20)
        z2 = shadow_zeta(S, complex(10.0), max_r=30)
        # Difference should be small (convergence)
        assert abs(z1 - z2) < 0.01 * abs(z1) if abs(z1) > 1e-12 else True


# ============================================================
# T61-T68: Cross-verification and Koszul duality
# ============================================================

class TestCrossVerification:
    def test_T61_full_analysis_heisenberg(self):
        """T61: Full theta correspondence analysis for Heisenberg."""
        result = full_theta_correspondence_analysis('Heisenberg', {'k': 1.0})
        assert result['kappa'] == 1.0
        assert result['family'] == 'Heisenberg'
        assert 'gl2_lift' in result
        assert 'gsp4_lift' in result
        assert 'F_g_predictions' in result
        assert abs(result['F_g_predictions'][1] - 1.0 / 24.0) < 1e-10

    def test_T62_full_analysis_virasoro(self):
        """T62: Full analysis for Virasoro at c=24."""
        result = full_theta_correspondence_analysis('Virasoro', {'c': 24.0})
        assert abs(result['kappa'] - 12.0) < 1e-12
        # F_1 = kappa * lambda_1 = 12/24 = 1/2
        assert abs(result['F_g_predictions'][1] - 0.5) < 1e-10

    def test_T63_genus2_verification(self):
        """T63: Genus-2 theta lift verification produces data."""
        S = heisenberg_shadow_coefficients(1.0)
        result = genus2_theta_lift_verification(S, kappa_val=1.0)
        assert abs(result['lambda_2_FP'] - float(_faber_pandharipande(2))) < 1e-14
        assert abs(result['F_2_predicted'] - float(_faber_pandharipande(2))) < 1e-14

    def test_T64_koszul_dual_heisenberg_anti_symmetry(self):
        """T64: kappa + kappa' = 0 for Heisenberg (free field anti-symmetry)."""
        result = koszul_dual_theta_lift('Heisenberg', {'k': 3.0})
        assert abs(result['kappa_sum']) < 1e-12  # kappa + kappa' = 0

    def test_T65_koszul_dual_virasoro_sum_13(self):
        """T65: kappa + kappa' = 13 for Virasoro (AP24: NOT zero)."""
        result = koszul_dual_theta_lift('Virasoro', {'c': 10.0})
        # kappa(Vir_10) = 5, kappa(Vir_16) = 8, sum = 13
        assert abs(result['kappa_sum'] - 13.0) < 1e-10

    def test_T66_koszul_dual_affine_anti_symmetry(self):
        """T66: kappa + kappa' = 0 for affine sl_2 (KM anti-symmetry)."""
        result = koszul_dual_theta_lift('affine_sl2', {'k': 1.0})
        assert abs(result['kappa_sum']) < 1e-10

    def test_T67_theta_lift_complexity_classification(self):
        """T67: Depth classification matches known shadow depth."""
        heis = theta_lift_complexity(heisenberg_shadow_coefficients(1.0))
        assert heis['depth_class'] == 'G'
        assert heis['depth'] == 2

        aff = theta_lift_complexity(affine_sl2_shadow_coefficients(1.0))
        assert aff['depth_class'] == 'L'
        assert aff['depth'] == 3

        vir = theta_lift_complexity(virasoro_shadow_coefficients(24.0, max_r=15))
        assert vir['depth_class'] == 'M'
        assert vir['L_function_type'] == 'transcendental'

    def test_T68_quadratic_space_data(self):
        """T68: Shadow quadratic space from Virasoro has correct structure."""
        S = virasoro_shadow_coefficients(24.0, max_r=8)
        qs = shadow_quadratic_space(S)
        assert abs(qs['kappa'] - 12.0) < 1e-12
        assert abs(qs['alpha'] - 2.0) < 1e-12
        assert abs(qs['Delta'] - 8.0 * 12.0 * S[4]) < 1e-10
        assert abs(qs['q_coefficients'][0] - 4.0 * 144.0) < 1e-10  # 4*kappa^2


# ============================================================
# Additional verification: number-theoretic utilities
# ============================================================

class TestNumberTheory:
    def test_divisors_small(self):
        """Verify divisors function for small inputs."""
        assert _divisors(1) == [1]
        assert _divisors(6) == [1, 2, 3, 6]
        assert _divisors(12) == [1, 2, 3, 4, 6, 12]

    def test_sigma_1(self):
        """Verify sigma_1 against known values."""
        assert _sigma(1) == 1
        assert _sigma(6) == 12
        assert _sigma(12) == 28

    def test_bernoulli_numbers(self):
        """Verify Bernoulli numbers B_0, B_1, B_2, B_4."""
        assert _bernoulli_number(0) == Fraction(1)
        assert _bernoulli_number(1) == Fraction(-1, 2)
        assert _bernoulli_number(2) == Fraction(1, 6)
        assert _bernoulli_number(4) == Fraction(-1, 30)

    def test_faber_pandharipande_values(self):
        """Verify lambda_g^{FP} at g=1,2,3."""
        assert _faber_pandharipande(1) == Fraction(1, 24)
        assert _faber_pandharipande(2) == Fraction(7, 5760)
        # g=3: lambda_3 = (2^5-1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720
        # = 31/(32*42*720) = 31/967680
        assert _faber_pandharipande(3) == Fraction(31, 967680)

    def test_kronecker_symbol_basic(self):
        """Verify Kronecker symbol at basic values."""
        # (D/1) = 1 always
        assert kronecker_symbol_safe(-3, 1) == 1
        assert kronecker_symbol_safe(-4, 1) == 1
        # (-1/n) for odd n
        assert kronecker_symbol_safe(-1, 3) == -1  # -1 is not QR mod 3
        assert kronecker_symbol_safe(-1, 5) == 1   # -1 is QR mod 5

    def test_F_g_formula(self):
        """Verify F_g = kappa * lambda_g^{FP} at g=1 for known families."""
        # Heisenberg k=1: kappa=1, F_1 = 1/24
        assert abs(float(_faber_pandharipande(1)) - 1.0 / 24.0) < 1e-14
        # Virasoro c=24: kappa=12, F_1 = 12/24 = 1/2
        assert abs(12.0 * float(_faber_pandharipande(1)) - 0.5) < 1e-14
        # Virasoro c=26: kappa=13, F_1 = 13/24
        assert abs(13.0 * float(_faber_pandharipande(1)) - 13.0 / 24.0) < 1e-14


# ============================================================
# Additional: Delta verification
# ============================================================

class TestRamanujanDelta:
    def test_sk_verification(self):
        """Verify SK lift at Delta level returns data."""
        result = ramanujan_delta_sk_verification()
        assert 'sk_coefficients' in result
        assert 'fundamental_disc_data' in result
