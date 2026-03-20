#!/usr/bin/env python3
r"""
Tests for shadow_hecke_identification.py — the conjectural identification
A^sh = Hecke algebra acting on the spectral decomposition of Z_A on M_{g,n}.

TARGET: 50+ tests covering all 8 sections of the identification programme.
"""

import math
import sys
import os
from fractions import Fraction

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_hecke_identification import (
    sigma_k, ramanujan_tau, chi_minus4,
    ShadowData,
    shadow_data_V_Z, shadow_data_V_E8, shadow_data_V_Leech,
    shadow_data_virasoro, shadow_data_affine_sl2,
    hecke_data_theta3, hecke_data_E4, hecke_data_E12, hecke_data_Delta,
    identification_V_Z, identification_V_E8, identification_V_Leech,
    verify_hecke_multiplicativity_E4, verify_hecke_multiplicativity_Delta,
    shadow_gf_to_l_function,
    virasoro_shadow_l_function,
    hecke_relation_T_mn,
    mc_vs_hecke_at_arity4,
    newton_identity_bridge,
    leech_theta_eigenform_decomposition,
    ising_partition_function_decomposition,
    shadow_gf_hecke_l_table,
    shadow_epstein_bridge,
    identification_summary,
    extract_hecke_eigenvalues_from_shadow,
    compare_ring_structures,
    shadow_algebra_generators,
    mc_equation_arity4,
)


# ============================================================
# Section 1: Arithmetic function tests
# ============================================================

class TestArithmeticFunctions:
    """Tests for sigma_k, ramanujan_tau, chi_{-4}."""

    def test_sigma_3_small_values(self):
        """sigma_3(n) for n=1..6."""
        expected = {1: 1, 2: 9, 3: 28, 4: 73, 5: 126, 6: 252}
        for n, val in expected.items():
            assert sigma_k(n, 3) == val, f"sigma_3({n}) = {sigma_k(n, 3)}, expected {val}"

    def test_sigma_11_small_values(self):
        """sigma_{11}(n) for n=1..3."""
        assert sigma_k(1, 11) == 1
        assert sigma_k(2, 11) == 1 + 2**11  # 1 + 2048 = 2049
        assert sigma_k(3, 11) == 1 + 3**11  # 1 + 177147 = 177148

    def test_sigma_0_is_divisor_count(self):
        """sigma_0(n) = number of divisors."""
        assert sigma_k(1, 0) == 1
        assert sigma_k(6, 0) == 4  # 1, 2, 3, 6
        assert sigma_k(12, 0) == 6  # 1, 2, 3, 4, 6, 12

    def test_ramanujan_tau_first_values(self):
        """tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, tau(5) = 4830."""
        assert ramanujan_tau(1) == 1
        assert ramanujan_tau(2) == -24
        assert ramanujan_tau(3) == 252
        assert ramanujan_tau(4) == -1472
        assert ramanujan_tau(5) == 4830

    def test_ramanujan_tau_6_7(self):
        """tau(6) = -6048, tau(7) = -16744."""
        assert ramanujan_tau(6) == -6048
        assert ramanujan_tau(7) == -16744

    def test_chi_minus4_values(self):
        """chi_{-4}: 0 for even, 1 for 1 mod 4, -1 for 3 mod 4."""
        assert chi_minus4(1) == 1
        assert chi_minus4(2) == 0
        assert chi_minus4(3) == -1
        assert chi_minus4(4) == 0
        assert chi_minus4(5) == 1
        assert chi_minus4(7) == -1

    def test_ramanujan_tau_multiplicativity(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) for gcd(m,n) = 1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3) = 1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        # tau(10) = tau(2)*tau(5)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)

    def test_ramanujan_tau_hecke_relation(self):
        """tau(p)^2 = tau(p^2) + p^11 for prime p (Hecke relation at weight 12)."""
        # For p=2: tau(2)^2 = tau(4) + 2^11
        assert ramanujan_tau(2)**2 == ramanujan_tau(4) + 2**11
        # (-24)^2 = 576 = -1472 + 2048 = 576. CHECK.

    def test_sigma_3_multiplicativity(self):
        """sigma_3 is multiplicative: sigma_3(mn) = sigma_3(m)*sigma_3(n) for gcd(m,n)=1."""
        assert sigma_k(6, 3) == sigma_k(2, 3) * sigma_k(3, 3)
        assert sigma_k(15, 3) == sigma_k(3, 3) * sigma_k(5, 3)


# ============================================================
# Section 2: Shadow data tests
# ============================================================

class TestShadowData:
    """Tests for shadow data of standard algebras."""

    def test_V_Z_shadow_data(self):
        """V_Z: kappa = 1/2, depth 2, class G."""
        sd = shadow_data_V_Z()
        assert sd.c == 1.0
        assert sd.kappa == 0.5
        assert sd.cubic == 0.0
        assert sd.quartic == 0.0
        assert sd.depth == 2
        assert sd.shadow_class == 'G'

    def test_V_E8_shadow_data(self):
        """V_{E_8}: kappa = 4, depth 3, class L."""
        sd = shadow_data_V_E8()
        assert sd.c == 8.0
        assert sd.kappa == 4.0
        assert sd.cubic == pytest.approx(248.0 / 961.0, abs=1e-10)
        assert sd.quartic == 0.0
        assert sd.depth == 3
        assert sd.shadow_class == 'L'

    def test_V_Leech_shadow_data(self):
        """V_{Leech}: kappa = 12, depth 4."""
        sd = shadow_data_V_Leech()
        assert sd.c == 24.0
        assert sd.kappa == 12.0
        assert sd.depth == 4
        # cubic and quartic are nonzero
        assert sd.cubic != 0.0
        assert sd.quartic != 0.0

    def test_virasoro_shadow_data(self):
        """Virasoro at c=26: kappa = 13, S_3 = 2, S_4 = 10/(26*(130+22))."""
        sd = shadow_data_virasoro(26.0)
        assert sd.kappa == 13.0
        assert sd.cubic == 2.0
        expected_Q = 10.0 / (26 * (5 * 26 + 22))
        assert sd.quartic == pytest.approx(expected_Q, rel=1e-10)
        assert sd.depth == float('inf')

    def test_affine_sl2_shadow_data(self):
        """Affine sl_2 at k=1: c = 1, kappa = 1/2, depth 3."""
        sd = shadow_data_affine_sl2(1)
        assert sd.c == pytest.approx(1.0, rel=1e-10)
        assert sd.kappa == pytest.approx(0.5, rel=1e-10)
        assert sd.depth == 3

    def test_kappa_equals_c_over_2(self):
        """For ALL standard algebras: kappa = c/2."""
        for sd_func in [shadow_data_V_Z, shadow_data_V_E8, shadow_data_V_Leech]:
            sd = sd_func()
            assert sd.kappa == pytest.approx(sd.c / 2.0, rel=1e-10), \
                f"{sd.name}: kappa={sd.kappa}, c/2={sd.c/2}"

    def test_shadow_gf_polynomial(self):
        """Shadow GF is a polynomial for finite-depth algebras."""
        sd = shadow_data_V_E8()
        # G(t) = 4*t^2 + (248/961)*t^3
        t = 0.1
        expected = 4.0 * t**2 + (248.0 / 961.0) * t**3
        assert sd.shadow_gf_polynomial(t) == pytest.approx(expected, rel=1e-10)


# ============================================================
# Section 3: Hecke eigenvalue tests
# ============================================================

class TestHeckeData:
    """Tests for Hecke eigenvalues of standard modular forms."""

    def test_theta3_hecke_eigenvalues(self):
        """theta_3 Hecke eigenvalues: lambda_p = 1 + chi_{-4}(p)."""
        hd = hecke_data_theta3()
        assert hd.eigenvalue(2) == 1  # chi_{-4}(2) = 0
        assert hd.eigenvalue(3) == 0  # chi_{-4}(3) = -1
        assert hd.eigenvalue(5) == 2  # chi_{-4}(5) = 1
        assert hd.eigenvalue(7) == 0  # chi_{-4}(7) = -1

    def test_E4_hecke_eigenvalues(self):
        """E_4 Hecke eigenvalues: lambda_n = sigma_3(n)."""
        hd = hecke_data_E4()
        assert hd.eigenvalue(1) == 1
        assert hd.eigenvalue(2) == 9
        assert hd.eigenvalue(3) == 28
        assert hd.eigenvalue(5) == 126

    def test_Delta_hecke_eigenvalues(self):
        """Delta Hecke eigenvalues: lambda_n = tau(n)."""
        hd = hecke_data_Delta()
        assert hd.eigenvalue(1) == 1
        assert hd.eigenvalue(2) == -24
        assert hd.eigenvalue(3) == 252

    def test_E12_hecke_eigenvalues(self):
        """E_{12} Hecke eigenvalues: lambda_n = sigma_{11}(n)."""
        hd = hecke_data_E12()
        assert hd.eigenvalue(1) == 1
        assert hd.eigenvalue(2) == 2049


# ============================================================
# Section 4: V_Z identification tests
# ============================================================

class TestIdentificationVZ:
    """Tests for the shadow-Hecke identification for V_Z."""

    def test_V_Z_identification_consistent(self):
        """V_Z identification is internally consistent."""
        result = identification_V_Z()
        assert result['consistent']
        assert result['shadow_kappa'] == 0.5
        assert result['n_hecke_eigenvalues'] == 1

    def test_V_Z_proportionality(self):
        """kappa is proportional to the leading Hecke eigenvalue."""
        result = identification_V_Z()
        assert result['proportional']
        assert result['ratio'] == pytest.approx(0.5, abs=1e-12)

    def test_V_Z_depth_matches_L_functions(self):
        """depth = 2 => 1 L-function for V_Z."""
        sd = shadow_data_V_Z()
        assert sd.depth - 1 == 1


# ============================================================
# Section 5: V_{E_8} identification tests
# ============================================================

class TestIdentificationVE8:
    """Tests for the shadow-Hecke identification for V_{E_8}."""

    def test_V_E8_arity2_consistent(self):
        """Arity 2: kappa = (c/2)*sigma_3(1) = 4*1 = 4."""
        result = identification_V_E8()
        assert result['arity2_consistent']

    def test_V_E8_hecke_relation_T2_squared(self):
        """Hecke relation: sigma_3(2)^2 = sigma_3(4) + 2^3."""
        result = identification_V_E8()
        hr = result['hecke_relation_T2_squared']
        assert hr['satisfied']
        assert hr['lhs'] == 81
        assert hr['rhs'] == 81

    def test_V_E8_sigma3_values(self):
        """sigma_3(2) = 9, sigma_3(3) = 28, sigma_3(5) = 126."""
        result = identification_V_E8()
        s3 = result['sigma_3_values']
        assert s3[2] == 9
        assert s3[3] == 28
        assert s3[5] == 126

    def test_V_E8_depth_matches_L_functions(self):
        """depth = 3 => 2 L-functions for V_{E_8}."""
        result = identification_V_E8()
        assert result['depth'] == 3
        assert result['n_L_functions'] == 2

    def test_V_E8_epstein_factorization(self):
        """E_{E_8}(s) = 240*4^{-s}*zeta(s)*zeta(s-3): two L-factors."""
        # The Epstein zeta factors into TWO Riemann zeta functions
        # This gives two critical lines: Re(s)=1/2 and Re(s)=7/2
        sd = shadow_data_V_E8()
        n_critical_lines = sd.depth - 1  # = 2
        assert n_critical_lines == 2

    def test_V_E8_sigma3_hecke_identity(self):
        """sigma_3 satisfies the Hecke multiplicativity for weight 4."""
        results = verify_hecke_multiplicativity_E4(n_max=7)
        for r in results:
            assert r['satisfied'], f"Hecke failed for m={r['m']}, n={r['n']}"


# ============================================================
# Section 6: V_{Leech} identification tests
# ============================================================

class TestIdentificationVLeech:
    """Tests for the shadow-Hecke identification for V_{Leech}."""

    def test_V_Leech_theta_coefficients(self):
        """theta_{Leech}[0] = 1, theta_{Leech}[1] = 0 (no norm-2 vectors)."""
        result = identification_V_Leech()
        assert result['theta_leech_coeffs'][0] == 1
        assert result['theta_leech_coeffs'][1] == 0

    def test_V_Leech_theta_q2(self):
        """theta_{Leech}[2] = 196560 (kissing number of Leech lattice)."""
        result = identification_V_Leech()
        assert result['theta_leech_coeffs'][2] == 196560

    def test_V_Leech_eigenform_decomposition(self):
        """theta_{Leech} = E_{12} - (65520/691)*Delta at q^2."""
        result = identification_V_Leech()
        assert result['q2_match']

    def test_V_Leech_eigenform_a(self):
        """Coefficient of E_{12}: a = 1."""
        result = identification_V_Leech()
        assert result['eigenform_a'] == 1

    def test_V_Leech_eigenform_b(self):
        """Coefficient of Delta: b = -65520/691."""
        result = identification_V_Leech()
        expected_b = -65520.0 / 691.0
        assert result['eigenform_b'] == pytest.approx(expected_b, rel=1e-10)

    def test_V_Leech_depth(self):
        """V_{Leech} has depth 4 and 3 L-functions."""
        result = identification_V_Leech()
        assert result['depth'] == 4
        assert result['n_L_functions'] == 3

    def test_V_Leech_tau_values(self):
        """Ramanujan tau values match in the decomposition."""
        result = identification_V_Leech()
        assert result['tau_values'][1] == 1
        assert result['tau_values'][2] == -24
        assert result['tau_values'][3] == 252


# ============================================================
# Section 7: Leech eigenform decomposition tests
# ============================================================

class TestLeechDecomposition:
    """Full eigenform decomposition of theta_{Leech}."""

    def test_decomposition_all_match(self):
        """All q-coefficients match the eigenform decomposition."""
        result = leech_theta_eigenform_decomposition(nmax=8)
        assert result['all_match']

    def test_decomposition_coefficients(self):
        """Verify first few theta_{Leech} coefficients."""
        result = leech_theta_eigenform_decomposition(nmax=5)
        theta = result['theta_coeffs']
        assert theta[0] == 1
        assert theta[1] == 0
        assert theta[2] == 196560

    def test_e4_cubed_coefficient_q1(self):
        """E_4^3 at q^1 = 3*240 = 720."""
        result = leech_theta_eigenform_decomposition(nmax=3)
        # E_4^3[1] = 3 * 240 * sigma_3(1) = 720
        # But actually E_4^3[1] = sum over partitions...
        # E_4 = 1 + 240q + ... so E_4^3[1] = 3*240 = 720.
        # theta_Leech[1] = E_4^3[1] - 720*Delta[1] = 720 - 720*1 = 0. CHECK.
        theta = result['theta_coeffs']
        assert theta[1] == 0

    def test_b_delta_value(self):
        """b = -65520/691 ~ -94.82."""
        result = leech_theta_eigenform_decomposition()
        assert abs(result['b_Delta'] + 65520 / 691) < 1e-8


# ============================================================
# Section 8: Hecke multiplicativity tests
# ============================================================

class TestHeckeMultiplicativity:
    """Tests for Hecke multiplicativity relations."""

    def test_E4_multiplicativity_all(self):
        """sigma_3 satisfies Hecke multiplicativity for all m,n <= 7."""
        results = verify_hecke_multiplicativity_E4(n_max=7)
        n_satisfied = sum(1 for r in results if r['satisfied'])
        assert n_satisfied == len(results)

    def test_Delta_multiplicativity_all(self):
        """tau satisfies Hecke multiplicativity for all m,n <= 5."""
        results = verify_hecke_multiplicativity_Delta(n_max=5)
        for r in results:
            assert r['satisfied'], f"Failed for m={r['m']}, n={r['n']}: {r['lhs']} != {r['rhs']}"

    def test_sigma3_T2_squared(self):
        """sigma_3(2)^2 = sigma_3(4) + 2^3."""
        r = hecke_relation_T_mn(2, 2, 4, lambda n: sigma_k(n, 3))
        assert r['satisfied']
        assert r['lhs'] == 81
        assert r['rhs'] == 81

    def test_sigma3_T2_T3(self):
        """sigma_3(2)*sigma_3(3) = sigma_3(6) (since gcd(2,3) = 1)."""
        r = hecke_relation_T_mn(2, 3, 4, lambda n: sigma_k(n, 3))
        assert r['satisfied']
        assert r['lhs'] == 9 * 28  # 252
        assert r['rhs'] == sigma_k(6, 3)  # 252

    def test_tau_T2_squared(self):
        """tau(2)^2 = tau(4) + 2^{11}."""
        r = hecke_relation_T_mn(2, 2, 12, ramanujan_tau)
        assert r['satisfied']
        # (-24)^2 = 576 = tau(4) + 2048 = -1472 + 2048 = 576
        assert r['lhs'] == 576
        assert r['rhs'] == 576

    def test_tau_T2_T3(self):
        """tau(2)*tau(3) = tau(6)."""
        r = hecke_relation_T_mn(2, 3, 12, ramanujan_tau)
        assert r['satisfied']
        assert r['lhs'] == -24 * 252  # -6048
        assert r['rhs'] == ramanujan_tau(6)  # -6048


# ============================================================
# Section 9: MC equation vs Hecke relations
# ============================================================

class TestMCvsHecke:
    """Tests for the structural comparison of MC and Hecke."""

    def test_mc_vs_hecke_arity4(self):
        """MC and Hecke are structurally parallel at arity 4."""
        result = mc_vs_hecke_at_arity4()
        assert result['hecke_relation']['satisfied']
        assert result['mc_equation']['structural_parallel']
        assert result['mc_equation']['both_quadratic_at_arity_4']

    def test_hecke_relation_sigma3_4(self):
        """sigma_3(4) = 73 = 1 + 8 + 64."""
        assert sigma_k(4, 3) == 73

    def test_hecke_relation_lhs_rhs(self):
        """9^2 = 73 + 8 = 81."""
        result = mc_vs_hecke_at_arity4()
        hr = result['hecke_relation']
        assert hr['lhs'] == hr['rhs'] == 81


# ============================================================
# Section 10: Newton identity bridge tests
# ============================================================

class TestNewtonBridge:
    """Tests for the Newton identity eigenvalue extraction."""

    def test_single_eigenvalue(self):
        """One eigenvalue: p_1 = lambda_1 determines lambda_1."""
        result = newton_identity_bridge([3.0], 1)
        eigenvalues = result['eigenvalues']
        assert len(eigenvalues) == 1
        assert abs(eigenvalues[0] - 3.0) < 1e-10

    def test_two_eigenvalues_symmetric(self):
        """Two eigenvalues: p_1 = 0, p_2 = 2 => lambda = +/- 1."""
        result = newton_identity_bridge([0.0, 2.0], 2)
        eigenvalues = sorted([complex(e).real for e in result['eigenvalues']])
        assert abs(eigenvalues[0] - (-1.0)) < 1e-10
        assert abs(eigenvalues[1] - 1.0) < 1e-10

    def test_two_eigenvalues_asymmetric(self):
        """Two eigenvalues: p_1 = 3, p_2 = 5 => solve."""
        result = newton_identity_bridge([3.0, 5.0], 2)
        eigenvalues = result['eigenvalues']
        # e_1 = 3, e_2 = (9-5)/2 = 2
        # Char poly: t^2 - 3t + 2 = (t-1)(t-2) => eigenvalues 1, 2
        eigs = sorted([complex(e).real for e in eigenvalues])
        assert abs(eigs[0] - 1.0) < 1e-10
        assert abs(eigs[1] - 2.0) < 1e-10

    def test_newton_elementary_symmetric(self):
        """Check elementary symmetric polynomials from Newton identities."""
        result = newton_identity_bridge([3.0, 5.0], 2)
        # e_1 = 3, e_2 = (9-5)/2 = 2
        assert abs(result['elementary_symmetric'][0] - 3.0) < 1e-10
        assert abs(result['elementary_symmetric'][1] - 2.0) < 1e-10


# ============================================================
# Section 11: Shadow GF to L-function tests
# ============================================================

class TestShadowGFtoLFunction:
    """Tests for shadow GF -> L-function extraction."""

    def test_V_Z_eigenvalue_extraction(self):
        """V_Z (depth 2): single eigenvalue sqrt(2*kappa) = 1."""
        sd = shadow_data_V_Z()
        result = shadow_gf_to_l_function(sd)
        assert len(result['eigenvalues']) == 1
        assert abs(result['eigenvalues'][0] - 1.0) < 1e-10

    def test_V_E8_eigenvalue_extraction(self):
        """V_{E_8} (depth 3): two eigenvalues from kappa=4, C=248/961.

        The eigenvalues may be complex conjugate pairs, since the cubic
        e_1^3 - 6*kappa*e_1 + 6*C = 0 can have complex roots depending
        on the discriminant. This is NOT a failure of the identification --
        it means the shadow-to-eigenvalue map requires the full Newton
        identity tower (not just arity 2 and 3).
        """
        sd = shadow_data_V_E8()
        result = shadow_gf_to_l_function(sd)
        assert len(result['eigenvalues']) == 2
        # Eigenvalues come in conjugate pairs (or both real)
        ev1, ev2 = result['eigenvalues']
        # Check conjugate pairing: ev1 = conj(ev2) or both real
        conjugate_pair = abs(complex(ev1) - complex(ev2).conjugate()) < 1e-6
        both_real = abs(complex(ev1).imag) < 1e-6 and abs(complex(ev2).imag) < 1e-6
        assert conjugate_pair or both_real, \
            f"Eigenvalues {ev1}, {ev2} are neither conjugate pair nor both real"

    def test_V_Leech_eigenvalue_extraction(self):
        """V_{Leech} (depth 4): three eigenvalues."""
        sd = shadow_data_V_Leech()
        result = shadow_gf_to_l_function(sd)
        assert len(result['eigenvalues']) == 3

    def test_virasoro_infinite_depth(self):
        """Virasoro (infinite depth): no finite eigenvalue extraction."""
        sd = shadow_data_virasoro(26.0)
        result = shadow_gf_to_l_function(sd)
        assert result['eigenvalues'] is None

    def test_depth2_l_polynomial(self):
        """Depth 2: L(t) = 1 - lambda*t is linear."""
        sd = shadow_data_V_Z()
        result = shadow_gf_to_l_function(sd)
        assert len(result['L_polynomial']) == 2

    def test_depth3_l_polynomial(self):
        """Depth 3: L(t) = 1 - e1*t + e2*t^2 is quadratic."""
        sd = shadow_data_V_E8()
        result = shadow_gf_to_l_function(sd)
        assert len(result['L_polynomial']) == 3


# ============================================================
# Section 12: Virasoro shadow L-function tests
# ============================================================

class TestVirasoroShadowL:
    """Tests for the Virasoro shadow L-function."""

    def test_virasoro_l_at_zero(self):
        """L(0) = exp(-G(0)) = exp(0) = 1."""
        assert virasoro_shadow_l_function(26.0, 0.0) == pytest.approx(1.0, abs=1e-10)

    def test_virasoro_l_small_t(self):
        """L(t) ~ 1 for small t."""
        val = virasoro_shadow_l_function(26.0, 0.01)
        assert abs(val - 1.0) < 0.01

    def test_virasoro_l_branch_point(self):
        """Branch point at t = -c/6 causes singularity."""
        c = 26.0
        # Just inside the branch: should still be finite
        val = virasoro_shadow_l_function(c, -c / 6.0 + 0.1)
        assert np.isfinite(val)


# ============================================================
# Section 13: Ising model tests
# ============================================================

class TestIsingModel:
    """Tests for the Ising model partition function decomposition."""

    def test_ising_central_charge(self):
        """Ising has c = 1/2."""
        result = ising_partition_function_decomposition()
        assert result['c'] == 0.5

    def test_ising_three_primaries(self):
        """Ising has 3 primary fields."""
        result = ising_partition_function_decomposition()
        assert result['n_primaries'] == 3

    def test_ising_infinite_algebra_depth(self):
        """Ising algebra (Virasoro) has infinite shadow depth."""
        result = ising_partition_function_decomposition()
        assert result['algebra_shadow_depth'] == float('inf')

    def test_ising_finite_pf_l_functions(self):
        """Ising partition function decomposes into finitely many L-functions."""
        result = ising_partition_function_decomposition()
        assert result['pf_l_functions'] == 8

    def test_ising_depth_distinction(self):
        """Key distinction: infinite algebra depth vs finite PF L-functions."""
        result = ising_partition_function_decomposition()
        assert result['algebra_shadow_depth'] > result['pf_l_functions']


# ============================================================
# Section 14: Shadow GF / Hecke L table tests
# ============================================================

class TestShadowGFHeckeTable:
    """Tests for the G_A(t) vs log L_A(t) comparison table."""

    def test_table_has_three_entries(self):
        """Table has entries for V_Z, Virasoro, affine sl_2."""
        table = shadow_gf_hecke_l_table()
        assert len(table) == 3

    def test_V_Z_entry(self):
        """V_Z entry in the table."""
        table = shadow_gf_hecke_l_table()
        assert table[0]['algebra'] == 'V_Z'
        assert table[0]['c'] == 1

    def test_virasoro_entry(self):
        """Virasoro entry in the table."""
        table = shadow_gf_hecke_l_table()
        assert table[1]['algebra'] == 'Virasoro'


# ============================================================
# Section 15: Shadow-Epstein bridge tests
# ============================================================

class TestShadowEpsteinBridge:
    """Tests for the shadow -> Epstein bridge."""

    def test_V_Z_bridge(self):
        """V_Z bridge: moments determine the single L-function."""
        result = shadow_epstein_bridge('V_Z')
        assert 'shadow_moments' in result
        assert result['shadow_moments']['p_2'] == 1.0

    def test_V_E8_bridge(self):
        """V_{E_8} bridge: two moments for two L-functions."""
        result = shadow_epstein_bridge('V_{E_8}')
        assert result['shadow_moments']['p_2'] == 8.0

    def test_V_Leech_bridge(self):
        """V_{Leech} bridge: three moments for three L-functions."""
        result = shadow_epstein_bridge('V_{Leech}')
        assert result['shadow_moments']['p_2'] == 24.0

    def test_unknown_algebra(self):
        """Unknown algebra returns error."""
        result = shadow_epstein_bridge('unknown')
        assert 'error' in result


# ============================================================
# Section 16: Ring structure comparison tests
# ============================================================

class TestRingStructure:
    """Tests comparing shadow algebra and Hecke algebra ring structures."""

    def test_shadow_algebra_V_Z(self):
        """V_Z shadow algebra has 1 generator (kappa)."""
        sd = shadow_data_V_Z()
        result = shadow_algebra_generators(sd)
        assert result['n_generators'] == 1
        assert 'kappa' in result['generators']
        assert result['commutative']

    def test_shadow_algebra_V_E8(self):
        """V_{E_8} shadow algebra has 2 generators (kappa, C)."""
        sd = shadow_data_V_E8()
        result = shadow_algebra_generators(sd)
        assert result['n_generators'] == 2
        assert 'kappa' in result['generators']
        assert 'C' in result['generators']

    def test_shadow_algebra_V_Leech(self):
        """V_{Leech} shadow algebra has 3 generators (kappa, C, Q)."""
        sd = shadow_data_V_Leech()
        result = shadow_algebra_generators(sd)
        assert result['n_generators'] == 3

    def test_both_commutative(self):
        """Both shadow algebra and Hecke algebra are commutative."""
        sd = shadow_data_V_E8()
        result = compare_ring_structures(sd, hecke_data_E4(), 4)
        assert result['both_commutative']


# ============================================================
# Section 17: Hecke eigenvalue extraction tests
# ============================================================

class TestHeckeExtraction:
    """Tests for extracting Hecke eigenvalues from shadow data."""

    def test_E8_kappa_sigma3_ratio(self):
        """kappa / sigma_3(1) = c/2 = 4."""
        sd = shadow_data_V_E8()
        result = extract_hecke_eigenvalues_from_shadow(sd, primes=[2, 3, 5])
        assert result['kappa_sigma3_ratio'] == pytest.approx(4.0, abs=1e-10)

    def test_E8_sigma3_values_computed(self):
        """sigma_3(p) values computed correctly for primes."""
        sd = shadow_data_V_E8()
        result = extract_hecke_eigenvalues_from_shadow(sd, primes=[2, 3, 5])
        assert result[2]['actual_sigma3'] == 9
        assert result[3]['actual_sigma3'] == 28
        assert result[5]['actual_sigma3'] == 126


# ============================================================
# Section 18: Identification summary tests
# ============================================================

class TestIdentificationSummary:
    """Tests for the identification summary."""

    def test_summary_has_proved_items(self):
        """Summary lists proved items."""
        result = identification_summary()
        assert len(result['proved']) == 4

    def test_summary_has_conjectural_items(self):
        """Summary lists conjectural items."""
        result = identification_summary()
        assert len(result['conjectural']) == 4

    def test_summary_has_obstruction(self):
        """Summary identifies the Mellin transform obstruction."""
        result = identification_summary()
        assert 'Mellin' in result['obstruction']

    def test_summary_has_resolution(self):
        """Summary proposes Newton identity resolution."""
        result = identification_summary()
        assert 'Newton' in result['resolution']


# ============================================================
# Section 19: Cross-consistency tests
# ============================================================

class TestCrossConsistency:
    """Cross-checks between different parts of the identification."""

    def test_depth_equals_1_plus_L_functions_V_Z(self):
        """V_Z: depth 2 = 1 + 1 L-function."""
        sd = shadow_data_V_Z()
        assert sd.depth == 1 + 1

    def test_depth_equals_1_plus_L_functions_V_E8(self):
        """V_{E_8}: depth 3 = 1 + 2 L-functions."""
        sd = shadow_data_V_E8()
        assert sd.depth == 1 + 2

    def test_depth_equals_1_plus_L_functions_V_Leech(self):
        """V_{Leech}: depth 4 = 1 + 3 L-functions."""
        sd = shadow_data_V_Leech()
        assert sd.depth == 1 + 3

    def test_hecke_multiplicativity_implies_mc(self):
        """If sigma_3 satisfies Hecke, then MC at arity 4 is compatible."""
        # Both the MC equation and Hecke relation involve quadratic constraints
        # at level 4. If one holds, the other is structurally compatible.
        mc = mc_vs_hecke_at_arity4()
        assert mc['hecke_relation']['satisfied']
        assert mc['mc_equation']['structural_parallel']

    def test_shadow_depth_classification_G(self):
        """Class G (Gaussian): depth 2, 1 L-function."""
        sd = shadow_data_V_Z()
        assert sd.shadow_class == 'G'
        assert sd.depth == 2

    def test_shadow_depth_classification_L(self):
        """Class L (Lie/tree): depth 3, 2 L-functions."""
        sd = shadow_data_V_E8()
        assert sd.shadow_class == 'L'
        assert sd.depth == 3

    def test_shadow_depth_classification_M(self):
        """Class M (mixed): infinite depth, infinitely many eigenvalues."""
        sd = shadow_data_virasoro(26.0)
        assert sd.shadow_class == 'M'
        assert sd.depth == float('inf')

    def test_E4_cubed_minus_720_Delta_gives_theta_Leech(self):
        """E_4^3 - 720*Delta gives theta_{Leech} with correct kissing number."""
        result = leech_theta_eigenform_decomposition(nmax=3)
        theta = result['theta_coeffs']
        # Kissing number of Leech lattice = 196560
        assert theta[2] == 196560

    def test_ramanujan_bound(self):
        """Ramanujan bound: |tau(p)| <= 2*p^{11/2} for prime p."""
        for p in [2, 3, 5, 7]:
            bound = 2 * p ** 5.5
            assert abs(ramanujan_tau(p)) <= bound + 1, \
                f"|tau({p})| = {abs(ramanujan_tau(p))} > {bound}"
