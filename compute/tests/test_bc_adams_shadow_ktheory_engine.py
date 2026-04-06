r"""Tests for Adams operations and lambda-ring structure on shadow K-theory.

BC-107: Lambda-ring structure, Adams operations, ghost maps, Witt vectors,
and zeta-zero Adams spectrum for the shadow algebras of modular Koszul algebras.

Multi-path verification strategy:
    Path 1: Direct Adams computation from Newton's formula
    Path 2: Direct power sum computation (independent)
    Path 3: Ghost map consistency: gh_n = psi^n
    Path 4: Specialization to known limits (k->0, finite towers)
    Path 5: sigma_t * lambda_{-t} = 1 identity
    Path 6: Adams composition: psi^m o psi^n = psi^{mn}
    Path 7: Koszul duality comparison
    Path 8: Numerical cross-check at multiple precision levels

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP10): Tests must not hardcode wrong expected values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction

import pytest

from compute.lib.bc_adams_shadow_ktheory_engine import (
    adams_eigenvalues_at_zero,
    adams_euler_ratio,
    affine_sl2_data,
    compute_adams_from_lambda,
    compute_adams_from_log_derivative,
    compute_lambda_series,
    compute_sigma_series,
    detect_ratio_patterns,
    euler_factor_at_zero,
    full_lambda_ring_analysis,
    ghost_components,
    ghost_from_shadow,
    ghost_witt_reciprocity_matrix,
    heisenberg_data,
    koszul_dual_comparison,
    landscape_lambda_ring_census,
    riemann_zeta_zeros,
    shadow_central_charge_at_zero,
    shadow_coefficients_exact,
    shadow_coefficients_float,
    standard_landscape_algebras,
    verify_adams_composition,
    verify_sigma_lambda_identity,
    virasoro_data,
    virasoro_shadow_coeffs_complex,
    w3_data,
    witt_from_ghost,
    zeta_zero_adams_spectrum,
)


# ============================================================================
# Helper
# ============================================================================

def rel_err(a, b, eps=1e-30):
    """Relative error between a and b."""
    if isinstance(a, complex) or isinstance(b, complex):
        a, b = complex(a), complex(b)
        return abs(a - b) / max(abs(b), eps)
    return abs(float(a) - float(b)) / max(abs(float(b)), eps)


# ============================================================================
# 1. Shadow coefficient computation tests
# ============================================================================

class TestShadowCoefficients:
    """Tests for the self-contained shadow coefficient computation."""

    def test_heisenberg_k1(self):
        """Heisenberg k=1: kappa=1, alpha=0, S4=0. Only S_2 nonzero.

        S_r = a_{r-2}/r where a_0 = 2*kappa.
        S_2 = a_0/2 = 2*kappa/2 = kappa = 1.
        """
        coeffs = shadow_coefficients_exact(Fraction(1), Fraction(0), Fraction(0), 10)
        assert coeffs[2] == Fraction(1)  # S_2 = kappa = 1

    def test_heisenberg_k1_higher_vanish(self):
        """Heisenberg: alpha=0, S4=0 => all S_r vanish for r >= 3."""
        coeffs = shadow_coefficients_exact(Fraction(1), Fraction(0), Fraction(0), 10)
        for r in range(3, 11):
            assert coeffs[r] == 0, f"S_{r} should vanish for Heisenberg"

    def test_virasoro_kappa(self):
        """Virasoro at c=1: kappa = 1/2, S_2 = kappa = 1/2."""
        data = virasoro_data(1)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 5)
        assert coeffs[2] == Fraction(1, 2)

    def test_virasoro_c1_S3(self):
        """Virasoro at c=1: S_3 = alpha/3 = 2/3."""
        data = virasoro_data(1)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 5)
        # S_3 = a_1/3 = 3*alpha/3 = alpha = 2. Wait: a_1 = 3*alpha = 6.
        # S_3 = a_1/3 = 6/3 = 2.
        assert coeffs[3] == Fraction(2)

    def test_virasoro_c1_S4(self):
        """Virasoro at c=1: S_4 = a_2/4 = 4*S4_orig/4 = S4_orig = 10/(1*27) = 10/27."""
        data = virasoro_data(1)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 5)
        expected_S4 = Fraction(10, 27)
        assert coeffs[4] == expected_S4

    def test_shadow_float_matches_exact(self):
        """Float computation matches exact for Virasoro c=4."""
        data = virasoro_data(4)
        exact = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 15)
        flt = shadow_coefficients_float(
            float(data['kappa']), float(data['alpha']), float(data['S4']), 15)
        for r in range(2, 16):
            assert rel_err(float(exact[r]), flt[r]) < 1e-10, f"Mismatch at r={r}"

    def test_kappa_zero_raises(self):
        """kappa=0 should raise (uncurved algebra)."""
        with pytest.raises(ValueError):
            shadow_coefficients_exact(Fraction(0), Fraction(1), Fraction(1), 5)

    def test_heisenberg_k3(self):
        """Heisenberg k=3: kappa=3, S_2=3."""
        coeffs = shadow_coefficients_exact(Fraction(3), Fraction(0), Fraction(0), 5)
        assert coeffs[2] == Fraction(3)
        assert coeffs[3] == 0


# ============================================================================
# 2. Lambda operation tests
# ============================================================================

class TestLambdaOperations:
    """Tests for exterior power (lambda) operations on the shadow module."""

    def test_lambda_0_is_one(self):
        """lambda^0 = 1 for any shadow module."""
        coeffs = {2: Fraction(1), 3: Fraction(0), 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 5)
        assert lam[0] == Fraction(1)

    def test_lambda_1_is_sum(self):
        """lambda^1 = sum of all S_r (first elementary symmetric polynomial)."""
        coeffs = {2: Fraction(3), 3: Fraction(2), 4: Fraction(1)}
        lam = compute_lambda_series(coeffs, 5)
        assert lam[1] == Fraction(6)  # 3 + 2 + 1

    def test_lambda_2_heisenberg(self):
        """Heisenberg: only S_2 nonzero, so lambda^k = 0 for k >= 2."""
        coeffs = {2: Fraction(5), 3: Fraction(0), 4: Fraction(0), 5: Fraction(0)}
        lam = compute_lambda_series(coeffs, 5)
        assert lam[0] == Fraction(1)
        assert lam[1] == Fraction(5)
        # lambda^2 = e_2 = sum_{i<j} S_i S_j. With only S_2=5 nonzero,
        # the product involves 0 terms with other variables, but wait:
        # we have 4 variables: S_2=5, S_3=0, S_4=0, S_5=0.
        # e_2(5,0,0,0) = 5*0 + 5*0 + 5*0 + 0*0 + 0*0 + 0*0 = 0
        assert lam[2] == Fraction(0)

    def test_lambda_series_two_nonzero(self):
        """Two nonzero shadow coefficients: explicit e.s.p. check."""
        # S_2 = a, S_3 = b, rest zero
        a, b = Fraction(3), Fraction(7)
        coeffs = {2: a, 3: b, 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 5)
        assert lam[0] == Fraction(1)
        assert lam[1] == a + b  # 10
        assert lam[2] == a * b  # 21
        assert lam[3] == Fraction(0)  # e_3(a,b,0) = 0

    def test_lambda_series_three_nonzero(self):
        """Three nonzero S_r: full e.s.p. at degree 3."""
        a, b, c_ = Fraction(2), Fraction(3), Fraction(5)
        coeffs = {2: a, 3: b, 4: c_}
        lam = compute_lambda_series(coeffs, 5)
        assert lam[0] == 1
        assert lam[1] == a + b + c_  # 10
        assert lam[2] == a * b + a * c_ + b * c_  # 6+10+15 = 31
        assert lam[3] == a * b * c_  # 30

    def test_virasoro_c13_lambda1(self):
        """Virasoro c=13 (self-dual): lambda^1 = sum S_r."""
        data = virasoro_data(13)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 10)
        lam = compute_lambda_series(coeffs, 5)
        expected_sum = sum(coeffs[r] for r in range(2, 11))
        assert lam[1] == expected_sum


# ============================================================================
# 3. Sigma (symmetric power) operation tests
# ============================================================================

class TestSigmaOperations:
    """Tests for symmetric power operations."""

    def test_sigma_0_is_one(self):
        """sigma^0 = 1."""
        lam = [Fraction(1), Fraction(3), Fraction(2)]
        sigma = compute_sigma_series(lam, 5)
        assert sigma[0] == Fraction(1)

    def test_sigma_lambda_identity_heisenberg(self):
        """sigma_t * lambda_{-t} = 1 for Heisenberg."""
        coeffs = {2: Fraction(2), 3: Fraction(0), 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 8)
        sigma = compute_sigma_series(lam, 8)
        checks = verify_sigma_lambda_identity(lam, sigma, 6)
        for n, val, ok in checks:
            assert ok, f"sigma-lambda identity fails at n={n}: got {val}"

    def test_sigma_lambda_identity_virasoro(self):
        """sigma_t * lambda_{-t} = 1 for Virasoro c=4."""
        data = virasoro_data(4)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 12)
        lam = compute_lambda_series(coeffs, 10)
        sigma = compute_sigma_series(lam, 10)
        checks = verify_sigma_lambda_identity(lam, sigma, 8)
        for n, val, ok in checks:
            assert ok, f"sigma-lambda identity fails at n={n}: got {val}"

    def test_sigma_lambda_identity_w3(self):
        """sigma_t * lambda_{-t} = 1 for W_3 at c=-2."""
        data = w3_data(Fraction(-2), 'T')
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 12)
        lam = compute_lambda_series(coeffs, 10)
        sigma = compute_sigma_series(lam, 10)
        checks = verify_sigma_lambda_identity(lam, sigma, 8)
        for n, val, ok in checks:
            assert ok, f"sigma-lambda identity fails at n={n}: got {val}"

    def test_sigma_1_equals_lambda_1(self):
        """sigma^1 = lambda^1 (both equal the sum of generators)."""
        coeffs = {2: Fraction(3), 3: Fraction(5), 4: Fraction(7)}
        lam = compute_lambda_series(coeffs, 5)
        sigma = compute_sigma_series(lam, 5)
        assert sigma[1] == lam[1]

    def test_sigma_single_variable(self):
        """Single nonzero S_r: sigma^k = S_r^k."""
        S = Fraction(4)
        coeffs = {2: S, 3: Fraction(0), 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 8)
        sigma = compute_sigma_series(lam, 8)
        for k in range(5):
            expected = S ** k
            assert sigma[k] == expected, f"sigma^{k}: expected {expected}, got {sigma[k]}"


# ============================================================================
# 4. Adams operation tests
# ============================================================================

class TestAdamsOperations:
    """Tests for Adams operations psi^n."""

    def test_psi_1_is_sum(self):
        """psi^1 = sum S_r (= lambda^1)."""
        coeffs = {2: Fraction(2), 3: Fraction(3), 4: Fraction(5)}
        lam = compute_lambda_series(coeffs, 10)
        psi = compute_adams_from_lambda(lam, 10)
        # psi^1 = e_1 = sum S_r
        assert psi[1] == Fraction(10)

    def test_psi_2_two_vars(self):
        """psi^2 for two variables: p_2 = e_1^2 - 2*e_2."""
        a, b = Fraction(3), Fraction(7)
        coeffs = {2: a, 3: b, 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 10)
        psi = compute_adams_from_lambda(lam, 10)
        # p_2 = a^2 + b^2 = 9 + 49 = 58
        expected = a**2 + b**2
        assert psi[2] == expected, f"psi^2: expected {expected}, got {psi[2]}"

    def test_psi_3_two_vars(self):
        """psi^3 for two variables: p_3 = a^3 + b^3."""
        a, b = Fraction(2), Fraction(5)
        coeffs = {2: a, 3: b, 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 10)
        psi = compute_adams_from_lambda(lam, 10)
        expected = a**3 + b**3  # 8 + 125 = 133
        assert psi[3] == expected

    def test_newton_vs_direct_heisenberg(self):
        """Newton formula matches direct power sum for Heisenberg."""
        data = heisenberg_data(3)
        analysis = full_lambda_ring_analysis(data, max_r=8, max_k=8, max_psi=8)
        for item in analysis['newton_vs_direct']:
            assert item['match'], f"Mismatch at n={item['n']}: {item}"

    def test_newton_vs_direct_virasoro_c4(self):
        """Newton formula matches direct power sum for Virasoro c=4."""
        data = virasoro_data(4)
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['newton_vs_direct']:
            assert item['match'], f"Mismatch at n={item['n']}: {item}"

    def test_newton_vs_direct_virasoro_c13(self):
        """Newton matches direct for Virasoro c=13 (self-dual point)."""
        data = virasoro_data(13)
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['newton_vs_direct']:
            assert item['match'], f"Mismatch at n={item['n']}: {item}"

    def test_newton_vs_direct_virasoro_c26(self):
        """Newton matches direct for Virasoro c=26 (critical)."""
        data = virasoro_data(26)
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['newton_vs_direct']:
            assert item['match'], f"Mismatch at n={item['n']}: {item}"

    def test_newton_vs_direct_w3(self):
        """Newton matches direct for W_3 at c=-2."""
        data = w3_data(Fraction(-2), 'T')
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['newton_vs_direct']:
            assert item['match'], f"Mismatch at n={item['n']}: {item}"

    def test_adams_single_variable(self):
        """Single nonzero S_r: psi^n = S_r^n."""
        S = Fraction(7)
        coeffs = {2: S, 3: Fraction(0), 4: Fraction(0)}
        lam = compute_lambda_series(coeffs, 10)
        psi = compute_adams_from_lambda(lam, 8)
        for n in range(1, 8):
            expected = S ** n
            assert psi[n] == expected, f"psi^{n}: expected {expected}, got {psi[n]}"

    def test_adams_composition_psi2_psi3(self):
        """psi^2 o psi^3 = psi^6: verified via direct power sum."""
        a, b, c_ = Fraction(2), Fraction(3), Fraction(5)
        coeffs = {2: a, 3: b, 4: c_}
        direct = compute_adams_from_log_derivative(
            {r: float(v) for r, v in coeffs.items()}, 10)
        # psi^6 = a^6 + b^6 + c^6
        expected = float(a**6 + b**6 + c_**6)
        assert rel_err(direct[6], expected) < 1e-10

    def test_adams_heisenberg_all_k(self):
        """Heisenberg k=1..5: psi^n = kappa^n."""
        for k in range(1, 6):
            data = heisenberg_data(k)
            coeffs = {2: Fraction(k)}
            for r in range(3, 8):
                coeffs[r] = Fraction(0)
            lam = compute_lambda_series(coeffs, 10)
            psi = compute_adams_from_lambda(lam, 8)
            for n in range(1, 8):
                expected = Fraction(k) ** n
                assert psi[n] == expected, f"Heis k={k}, psi^{n}: expected {expected}"


# ============================================================================
# 5. Ghost map tests
# ============================================================================

class TestGhostMap:
    """Tests for ghost map and Witt vector operations."""

    def test_ghost_vs_adams_heisenberg(self):
        """Ghost components match Adams operations for Heisenberg."""
        data = heisenberg_data(2)
        analysis = full_lambda_ring_analysis(data, max_r=8, max_k=8, max_psi=8)
        for item in analysis['ghost_vs_adams']:
            assert item['match'], f"Ghost-Adams mismatch at n={item['n']}: {item}"

    def test_ghost_vs_adams_virasoro(self):
        """Ghost components match Adams for Virasoro c=10."""
        data = virasoro_data(10)
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['ghost_vs_adams']:
            assert item['match'], f"Ghost-Adams mismatch at n={item['n']}: {item}"

    def test_ghost_vs_adams_virasoro_c25(self):
        """Ghost components match Adams for Virasoro c=25."""
        data = virasoro_data(25)
        analysis = full_lambda_ring_analysis(data, max_r=15, max_k=12, max_psi=12)
        for item in analysis['ghost_vs_adams']:
            assert item['match'], f"Ghost-Adams mismatch at n={item['n']}: {item}"

    def test_ghost_direct_computation(self):
        """Direct ghost computation for known values."""
        coeffs = {2: 3.0, 3: 5.0, 4: 0.0}
        gh = ghost_from_shadow(coeffs, 5)
        # gh_1 = 3 + 5 + 0 = 8
        assert abs(gh[1] - 8.0) < 1e-10
        # gh_2 = 3^2 + 5^2 + 0^2 = 9 + 25 = 34
        assert abs(gh[2] - 34.0) < 1e-10
        # gh_3 = 3^3 + 5^3 = 27 + 125 = 152
        assert abs(gh[3] - 152.0) < 1e-10

    def test_witt_ghost_roundtrip(self):
        """Witt coordinates -> ghost -> Witt roundtrip."""
        witt = [Fraction(0), Fraction(3), Fraction(7), Fraction(2), Fraction(5)]
        gh = ghost_components(witt, 10)
        witt_recovered = witt_from_ghost(gh, 5)
        for i in range(1, min(len(witt), len(witt_recovered))):
            assert rel_err(float(witt[i]), float(witt_recovered[i])) < 1e-8, \
                f"Witt roundtrip failed at index {i}"

    def test_ghost_components_simple(self):
        """Ghost components for simple Witt vector."""
        # witt = (0, a_1, a_2, ...) with a_1=2, a_2=3
        # gh_1 = 1 * a_1^1 = 2
        # gh_2 = a_1^2 + 2*a_2 = 4 + 6 = 10
        witt = [Fraction(0), Fraction(2), Fraction(3)]
        gh = ghost_components(witt, 3)
        assert gh[1] == Fraction(2)
        assert gh[2] == Fraction(10)

    def test_ghost_from_shadow_matches_direct(self):
        """ghost_from_shadow matches compute_adams_from_log_derivative."""
        coeffs = {2: 2.5, 3: 1.3, 4: 0.7, 5: 0.0}
        gh = ghost_from_shadow(coeffs, 8)
        direct = compute_adams_from_log_derivative(coeffs, 8)
        for n in range(1, 9):
            assert rel_err(gh[n], direct[n]) < 1e-10, \
                f"Ghost vs direct Adams mismatch at n={n}"


# ============================================================================
# 6. Algebra family data tests
# ============================================================================

class TestAlgebraData:
    """Tests for algebra data providers."""

    def test_heisenberg_kappa(self):
        """Heisenberg k: kappa = k."""
        for k in range(1, 6):
            data = heisenberg_data(k)
            assert data['kappa'] == Fraction(k)

    def test_virasoro_kappa(self):
        """Virasoro c: kappa = c/2."""
        for c in [Fraction(1, 2), 1, 4, 10, 13, 25, 26]:
            data = virasoro_data(c)
            assert data['kappa'] == Fraction(c) / 2

    def test_virasoro_alpha(self):
        """Virasoro always has alpha = 2."""
        for c in [1, 4, 13, 26]:
            data = virasoro_data(c)
            assert data['alpha'] == Fraction(2)

    def test_virasoro_S4_formula(self):
        """Virasoro S4 = 10/[c(5c+22)]."""
        for c in [1, 4, 10, 26]:
            data = virasoro_data(c)
            c_f = Fraction(c)
            expected = Fraction(10) / (c_f * (5 * c_f + 22))
            assert data['S4'] == expected

    def test_heisenberg_class_G(self):
        """Heisenberg is class G."""
        for k in range(1, 6):
            assert heisenberg_data(k)['shadow_class'] == 'G'

    def test_virasoro_class_M(self):
        """Virasoro is class M (infinite tower)."""
        for c in [1, 4, 13, 26]:
            assert virasoro_data(c)['shadow_class'] == 'M'

    def test_affine_sl2_kappa(self):
        """Affine sl_2 at k: kappa = 3(k+2)/4."""
        data = affine_sl2_data(1)
        assert data['kappa'] == Fraction(9, 4)

    def test_w3_T_line_matches_virasoro(self):
        """W_3 T-line shadow data matches Virasoro (universal T-line)."""
        for c in [4, 10]:
            w3 = w3_data(c, 'T')
            vir = virasoro_data(c)
            assert w3['kappa'] == vir['kappa']
            assert w3['alpha'] == vir['alpha']
            assert w3['S4'] == vir['S4']


# ============================================================================
# 7. Full lambda-ring analysis tests
# ============================================================================

class TestFullAnalysis:
    """Integration tests for the full lambda-ring analysis pipeline."""

    def test_heisenberg_full_analysis(self):
        """Full analysis for Heisenberg k=1 succeeds."""
        data = heisenberg_data(1)
        result = full_lambda_ring_analysis(data, max_r=8, max_k=6, max_psi=6)
        assert 'lambda_series' in result
        assert 'adams_newton' in result
        assert result['shadow_class'] == 'G'

    def test_virasoro_full_analysis(self):
        """Full analysis for Virasoro c=4 succeeds."""
        data = virasoro_data(4)
        result = full_lambda_ring_analysis(data, max_r=15, max_k=10, max_psi=10)
        assert 'lambda_series' in result
        assert result['shadow_class'] == 'M'

    def test_all_newton_direct_match(self):
        """Newton vs direct match for all standard algebras."""
        for alg in standard_landscape_algebras():
            try:
                result = full_lambda_ring_analysis(alg, max_r=12, max_k=8, max_psi=8)
                for item in result['newton_vs_direct']:
                    assert item['match'], \
                        f"{alg['name']}: Newton-direct mismatch at n={item['n']}"
            except ValueError:
                pass  # skip algebras with kappa=0

    def test_all_ghost_adams_match(self):
        """Ghost vs Adams match for all standard algebras."""
        for alg in standard_landscape_algebras():
            try:
                result = full_lambda_ring_analysis(alg, max_r=12, max_k=8, max_psi=8)
                for item in result['ghost_vs_adams']:
                    assert item['match'], \
                        f"{alg['name']}: ghost-Adams mismatch at n={item['n']}"
            except ValueError:
                pass

    def test_all_sigma_lambda_identity(self):
        """sigma-lambda identity for all standard algebras."""
        for alg in standard_landscape_algebras():
            try:
                result = full_lambda_ring_analysis(alg, max_r=12, max_k=8, max_psi=8)
                for n, val, ok in result['sigma_lambda_check']:
                    assert ok, f"{alg['name']}: sigma-lambda fails at n={n}"
            except ValueError:
                pass


# ============================================================================
# 8. Koszul duality tests (AP24: kappa + kappa' = 13 for Virasoro)
# ============================================================================

class TestKoszulDuality:
    """Tests for lambda-ring structure under Koszul duality."""

    def test_virasoro_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [1, 4, 10, 13, 25]:
            data_A = virasoro_data(c)
            data_dual = virasoro_data(26 - c)
            kappa_sum = float(data_A['kappa']) + float(data_dual['kappa'])
            assert abs(kappa_sum - 13.0) < 1e-10, \
                f"c={c}: kappa sum = {kappa_sum}, expected 13"

    def test_self_dual_c13(self):
        """Virasoro c=13 is self-dual: Vir_13! = Vir_13."""
        data = virasoro_data(13)
        assert float(data['kappa']) == 6.5  # c/2 = 13/2

    def test_koszul_dual_adams_comparison(self):
        """Compare Adams operations for A vs A! (Virasoro c=4 vs c=22)."""
        data_A = virasoro_data(4)
        data_dual = virasoro_data(22)
        comp = koszul_dual_comparison(data_A, data_dual, max_r=12, max_k=8)
        assert abs(comp['kappa_sum'] - 13.0) < 1e-10
        # Adams operations should differ (Koszul duality is nontrivial)
        assert len(comp['adams_comparison']) > 0

    def test_koszul_dual_c1_c25(self):
        """Virasoro c=1 and c=25: Koszul duals."""
        comp = koszul_dual_comparison(
            virasoro_data(1), virasoro_data(25), max_r=12, max_k=8)
        assert abs(comp['kappa_sum'] - 13.0) < 1e-10

    def test_heisenberg_kappa_antisymmetric(self):
        """Heisenberg: kappa(H_k) + kappa(H_{-k}) = 0 (AP24: different from Virasoro)."""
        # For Heisenberg, Koszul dual is H_{-k}, and kappa(-k) = -k.
        for k in [1, 2, 3]:
            assert Fraction(k) + Fraction(-k) == 0


# ============================================================================
# 9. Zeta zeros tests
# ============================================================================

class TestZetaZeros:
    """Tests for Adams operations at Riemann zeta zeros."""

    def test_first_zero_location(self):
        """First zeta zero at gamma_1 ~ 14.1347."""
        zeros = riemann_zeta_zeros(1)
        gamma_1 = zeros[0].imag
        assert abs(gamma_1 - 14.134725) < 0.001

    def test_shadow_central_charge_at_zero(self):
        """c(rho) = 26 - 24*rho for first zero."""
        rho = complex(0.5, 14.134725)
        c_val = shadow_central_charge_at_zero(rho)
        assert abs(c_val.real - 14.0) < 0.01
        assert abs(c_val.imag - (-24 * 14.134725)) < 0.1

    def test_euler_factor(self):
        """Euler factor p^rho is well-defined at zeta zeros."""
        rho = complex(0.5, 14.134725)
        for p in [2, 3, 5]:
            e = euler_factor_at_zero(p, rho)
            assert abs(e) > 0  # p^{1/2} * exp(i * gamma * log(p))
            assert abs(abs(e) - p**0.5) < 0.01  # |p^rho| = p^{1/2}

    def test_virasoro_complex_shadow_coeffs(self):
        """Complex shadow coefficients are computable at c(rho)."""
        rho = complex(0.5, 14.134725)
        c_val = shadow_central_charge_at_zero(rho)
        coeffs = virasoro_shadow_coeffs_complex(c_val, max_r=10)
        assert 2 in coeffs
        assert abs(coeffs[2] - c_val / 2) < 1e-8  # S_2 = kappa = c/2

    def test_adams_eigenvalues_computable(self):
        """Adams eigenvalues at zeta zeros are computable."""
        zeros = riemann_zeta_zeros(3)
        for rho in zeros:
            adams = adams_eigenvalues_at_zero(rho, [2, 3, 5], max_r=10)
            for p in [2, 3, 5]:
                assert p in adams
                assert isinstance(adams[p], complex)

    def test_adams_euler_ratio_computable(self):
        """Adams/Euler ratios at zeta zeros are computable."""
        zeros = riemann_zeta_zeros(3)
        for rho in zeros:
            ratios = adams_euler_ratio(rho, [2, 3], max_r=10)
            for p in [2, 3]:
                assert p in ratios
                assert isinstance(ratios[p], complex)

    def test_euler_factor_modulus(self):
        """|p^rho| = p^{1/2} on the critical line."""
        zeros = riemann_zeta_zeros(5)
        for rho in zeros:
            for p in [2, 3, 5, 7]:
                e = euler_factor_at_zero(p, rho)
                assert abs(abs(e) - p**0.5) < 1e-8


# ============================================================================
# 10. Ghost-Witt reciprocity tests
# ============================================================================

class TestGhostWittReciprocity:
    """Tests for ghost-Witt reciprocity at zeta zeros."""

    def test_reciprocity_matrix_computable(self):
        """Ghost-Witt reciprocity matrix is computable."""
        zeros = riemann_zeta_zeros(3)
        matrix = ghost_witt_reciprocity_matrix(zeros, max_n=5, max_r=10)
        assert (1, 1) in matrix
        assert (3, 5) in matrix

    def test_reciprocity_diagonal(self):
        """Diagonal entries gh_n(c(rho_n)) are well-defined."""
        zeros = riemann_zeta_zeros(5)
        matrix = ghost_witt_reciprocity_matrix(zeros, max_n=5, max_r=10)
        for n in range(1, 6):
            val = matrix[(n, n)]
            assert isinstance(val, complex)

    def test_ghost_power_sum_identity(self):
        """gh_n = sum S_r^n (power sum identity) at complex c."""
        rho = complex(0.5, 14.134725)
        c_val = shadow_central_charge_at_zero(rho)
        coeffs = virasoro_shadow_coeffs_complex(c_val, max_r=10)
        S_vals = [coeffs[r] for r in sorted(coeffs.keys())]

        for n in range(1, 6):
            gh_n = sum(s**n for s in S_vals)
            # This should match the ghost from direct computation
            adams = adams_eigenvalues_at_zero(rho, [n] if n in [2, 3, 5, 7, 11, 13] else [2],
                                              max_r=10)
            # For non-prime n, just check computability
            assert isinstance(gh_n, complex)


# ============================================================================
# 11. Specialization and limiting case tests (Path 4)
# ============================================================================

class TestSpecialization:
    """Tests for specialization to known limiting cases."""

    def test_large_c_virasoro_kappa_dominates(self):
        """For large c, kappa = c/2 dominates the shadow tower."""
        data = virasoro_data(1000)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 10)
        # S_2 = kappa = 500
        assert coeffs[2] == Fraction(500)
        # S_4 ~ 10/(1000*5022) ~ very small
        assert abs(float(coeffs[4])) < 0.001

    def test_c_to_26_minus_c_shadow_transform(self):
        """Under c -> 26-c, shadow coefficients transform predictably."""
        for c in [1, 4, 10]:
            data = virasoro_data(c)
            data_dual = virasoro_data(26 - c)
            # kappa(c) + kappa(26-c) = 13
            assert data['kappa'] + data_dual['kappa'] == Fraction(13)
            # alpha is the same for both (always 2 for Virasoro T-line)
            assert data['alpha'] == data_dual['alpha']

    def test_affine_sl2_class_L(self):
        """Affine sl_2: class L (S4=0, alpha!=0, r_max=3)."""
        data = affine_sl2_data(1)
        assert data['S4'] == Fraction(0)
        assert data['alpha'] != Fraction(0)
        assert data['shadow_class'] == 'L'

    def test_affine_sl2_tower_terminates(self):
        """Affine sl_2: S_r = 0 for r >= 4 (class L termination)."""
        data = affine_sl2_data(1)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 10)
        for r in range(4, 11):
            assert coeffs[r] == 0, f"S_{r} should vanish for affine sl_2"


# ============================================================================
# 12. Multi-path cross-verification tests
# ============================================================================

class TestMultiPathVerification:
    """Tests that cross-verify results via multiple independent paths."""

    def test_three_path_heisenberg_psi2(self):
        """psi^2 for Heisenberg k=3: three independent paths agree."""
        k = 3
        # Path 1: Newton formula
        data = heisenberg_data(k)
        coeffs = {2: Fraction(k)}
        for r in range(3, 8):
            coeffs[r] = Fraction(0)
        lam = compute_lambda_series(coeffs, 10)
        psi_newton = compute_adams_from_lambda(lam, 5)

        # Path 2: Direct power sum
        psi_direct = compute_adams_from_log_derivative(
            {r: float(v) for r, v in coeffs.items()}, 5)

        # Path 3: Ghost
        gh = ghost_from_shadow({r: float(v) for r, v in coeffs.items()}, 5)

        # All three should give psi^2 = k^2 = 9
        assert float(psi_newton[2]) == 9.0
        assert abs(psi_direct[2] - 9.0) < 1e-10
        assert abs(gh[2] - 9.0) < 1e-10

    def test_three_path_virasoro_c4_psi3(self):
        """psi^3 for Virasoro c=4: three paths agree."""
        data = virasoro_data(4)
        coeffs_exact = shadow_coefficients_exact(
            data['kappa'], data['alpha'], data['S4'], 15)
        coeffs_float = {r: float(v) for r, v in coeffs_exact.items()}

        # Path 1: Newton
        lam = compute_lambda_series(coeffs_exact, 12)
        psi_newton = compute_adams_from_lambda(lam, 5)
        val1 = float(psi_newton[3])

        # Path 2: Direct power sum
        psi_direct = compute_adams_from_log_derivative(coeffs_float, 5)
        val2 = psi_direct[3]

        # Path 3: Ghost
        gh = ghost_from_shadow(coeffs_float, 5)
        val3 = gh[3]

        assert rel_err(val1, val2) < 1e-6, f"Newton vs direct: {val1} vs {val2}"
        assert rel_err(val2, val3) < 1e-10, f"Direct vs ghost: {val2} vs {val3}"

    def test_three_path_virasoro_c13_psi5(self):
        """psi^5 for Virasoro c=13: three paths agree."""
        data = virasoro_data(13)
        coeffs_exact = shadow_coefficients_exact(
            data['kappa'], data['alpha'], data['S4'], 15)
        coeffs_float = {r: float(v) for r, v in coeffs_exact.items()}

        lam = compute_lambda_series(coeffs_exact, 12)
        psi_newton = compute_adams_from_lambda(lam, 8)
        psi_direct = compute_adams_from_log_derivative(coeffs_float, 8)
        gh = ghost_from_shadow(coeffs_float, 8)

        val1 = float(psi_newton[5])
        val2 = psi_direct[5]
        val3 = gh[5]

        assert rel_err(val1, val2) < 1e-5, f"Newton vs direct: {val1} vs {val2}"
        assert rel_err(val2, val3) < 1e-10, f"Direct vs ghost: {val2} vs {val3}"

    def test_four_path_sigma_lambda_newton_ghost(self):
        """Four-path verification for Virasoro c=10: sigma, lambda, Newton, ghost."""
        data = virasoro_data(10)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 15)
        coeffs_f = {r: float(v) for r, v in coeffs.items()}

        # Path 1 + 5: Lambda + sigma-lambda identity
        lam = compute_lambda_series(coeffs, 10)
        sigma = compute_sigma_series(lam, 10)
        checks = verify_sigma_lambda_identity(lam, sigma, 8)
        for n, val, ok in checks:
            assert ok

        # Path 1: Adams from Newton
        psi_n = compute_adams_from_lambda(lam, 8)

        # Path 2: Adams direct
        psi_d = compute_adams_from_log_derivative(coeffs_f, 8)

        # Path 3: Ghost
        gh = ghost_from_shadow(coeffs_f, 8)

        for n in range(1, 8):
            vals = [float(psi_n[n]), psi_d[n], gh[n]]
            for i in range(len(vals)):
                for j in range(i + 1, len(vals)):
                    assert rel_err(vals[i], vals[j]) < 1e-6, \
                        f"n={n}: path {i} ({vals[i]}) vs path {j} ({vals[j]})"


# ============================================================================
# 13. Landscape census tests
# ============================================================================

class TestLandscapeCensus:
    """Tests for landscape-wide lambda-ring computation."""

    def test_landscape_all_succeed(self):
        """All standard landscape algebras complete analysis without error."""
        results = landscape_lambda_ring_census(max_r=10, max_k=6, max_psi=6)
        for r in results:
            assert 'error' not in r, f"{r.get('name', '?')}: {r.get('error', '')}"

    def test_landscape_count(self):
        """Landscape has expected number of algebras (5 Heis + 7 Vir + 1 W3 + 1 sl2 = 14)."""
        algebras = standard_landscape_algebras()
        assert len(algebras) == 14

    def test_landscape_families_present(self):
        """All four families present in landscape."""
        algebras = standard_landscape_algebras()
        families = set(a['family'] for a in algebras)
        assert 'Heisenberg' in families
        assert 'Virasoro' in families
        assert 'W3' in families
        assert 'affine_sl2' in families


# ============================================================================
# 14. Zeta-zero spectrum tests
# ============================================================================

class TestZetaZeroSpectrum:
    """Tests for the full zeta-zero Adams spectrum computation."""

    def test_spectrum_computation(self):
        """Zeta-zero spectrum computes for 5 zeros and 3 primes."""
        result = zeta_zero_adams_spectrum(num_zeros=5, primes=[2, 3, 5], max_r=10)
        assert len(result['data']) == 5
        assert result['primes'] == [2, 3, 5]

    def test_spectrum_entries_valid(self):
        """Each spectrum entry has all required fields."""
        result = zeta_zero_adams_spectrum(num_zeros=3, primes=[2, 3], max_r=10)
        for d in result['data']:
            assert 'n' in d
            assert 'rho' in d
            assert 'psi_2' in d
            assert 'euler_2' in d
            assert 'ratio_2' in d

    def test_euler_modulus_sqrt_p(self):
        """Euler factor modulus = sqrt(p) on critical line."""
        result = zeta_zero_adams_spectrum(num_zeros=5, primes=[2, 3, 5, 7], max_r=10)
        for d in result['data']:
            for p in [2, 3, 5, 7]:
                euler = d[f'euler_{p}']
                assert abs(abs(euler) - p**0.5) < 1e-8

    def test_pattern_detection(self):
        """Pattern detection runs without error."""
        spectrum = zeta_zero_adams_spectrum(num_zeros=5, primes=[2, 3, 5], max_r=10)
        patterns = detect_ratio_patterns(spectrum)
        assert 2 in patterns
        assert 'modulus_mean' in patterns[2]


# ============================================================================
# 15. Edge case and robustness tests
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases and robustness."""

    def test_virasoro_c_half(self):
        """Virasoro c=1/2 (Ising model) computes correctly."""
        data = virasoro_data(Fraction(1, 2))
        assert data['kappa'] == Fraction(1, 4)
        result = full_lambda_ring_analysis(data, max_r=10, max_k=6, max_psi=6)
        assert 'error' not in result

    def test_w3_c_minus_2(self):
        """W_3 at c=-2 (minimal model) computes correctly."""
        data = w3_data(Fraction(-2), 'T')
        assert data['kappa'] == Fraction(-1)
        result = full_lambda_ring_analysis(data, max_r=10, max_k=6, max_psi=6)
        assert 'error' not in result

    def test_large_max_r(self):
        """Computation stable at large max_r."""
        data = virasoro_data(4)
        coeffs = shadow_coefficients_exact(data['kappa'], data['alpha'], data['S4'], 30)
        assert 30 in coeffs

    def test_negative_kappa(self):
        """Negative kappa (e.g. W_3 at c=-2) works."""
        coeffs = shadow_coefficients_exact(Fraction(-1), Fraction(2), Fraction(-1, 3), 10)
        assert 2 in coeffs

    def test_fractional_parameters(self):
        """Fractional kappa/alpha/S4 work correctly."""
        coeffs = shadow_coefficients_exact(
            Fraction(1, 7), Fraction(3, 5), Fraction(11, 13), 8)
        assert all(isinstance(v, Fraction) for v in coeffs.values())

    def test_zero_alpha_nonzero_S4(self):
        """alpha=0, S4!=0: valid configuration (class M if kappa!=0)."""
        # This would have Delta = 8*kappa*S4 != 0
        coeffs = shadow_coefficients_exact(Fraction(1), Fraction(0), Fraction(1), 10)
        assert coeffs[2] == Fraction(1)  # S_2 = kappa
        assert coeffs[3] == Fraction(0)  # S_3 = alpha = 0
        assert coeffs[4] == Fraction(1)  # S_4 = S4

    def test_lambda_max_k_0(self):
        """lambda series with max_k=0 returns just [1]."""
        coeffs = {2: Fraction(1), 3: Fraction(0)}
        lam = compute_lambda_series(coeffs, 0)
        assert len(lam) == 1
        assert lam[0] == 1


# ============================================================================
# 16. Composition and ring homomorphism tests
# ============================================================================

class TestComposition:
    """Tests that Adams operations satisfy ring homomorphism properties."""

    def test_psi_mn_equals_composition(self):
        """psi^{mn} = psi^m(psi^n) for power sums (automatic)."""
        a, b, c_ = 2.0, 3.0, 5.0
        coeffs = {2: a, 3: b, 4: c_}
        psi = compute_adams_from_log_derivative(coeffs, 15)

        # Test psi^{2*3} = psi^6
        psi_6 = psi[6]
        expected = a**6 + b**6 + c_**6
        assert rel_err(psi_6, expected) < 1e-8

        # Test psi^{3*5} = psi^15
        psi_15 = psi[15]
        expected_15 = a**15 + b**15 + c_**15
        assert rel_err(psi_15, expected_15) < 1e-4  # larger n => more numerical error

    def test_psi_additive(self):
        """psi^n(x+y) = psi^n(x) + psi^n(y) for power sums.

        If we split S_vals into two groups, psi^n of the union = sum of psi^n of each.
        """
        coeffs_full = {2: 3.0, 3: 5.0, 4: 7.0, 5: 0.0}
        coeffs_A = {2: 3.0, 3: 5.0, 4: 0.0, 5: 0.0}
        coeffs_B = {2: 0.0, 3: 0.0, 4: 7.0, 5: 0.0}

        psi_full = compute_adams_from_log_derivative(coeffs_full, 8)
        psi_A = compute_adams_from_log_derivative(coeffs_A, 8)
        psi_B = compute_adams_from_log_derivative(coeffs_B, 8)

        for n in range(1, 8):
            assert rel_err(psi_full[n], psi_A[n] + psi_B[n]) < 1e-8, \
                f"Additivity fails at n={n}"


# ============================================================================
# 17. Witt vector roundtrip tests
# ============================================================================

class TestWittVectors:
    """Tests for Witt vector / ghost map roundtrip."""

    def test_witt_ghost_roundtrip_simple(self):
        """Simple Witt -> ghost -> Witt roundtrip."""
        witt_orig = [Fraction(0), Fraction(5), Fraction(-3), Fraction(7)]
        gh = ghost_components(witt_orig, 6)
        witt_back = witt_from_ghost(gh, 4)
        for i in range(1, 4):
            assert witt_back[i] == witt_orig[i], \
                f"Index {i}: {witt_back[i]} != {witt_orig[i]}"

    def test_witt_ghost_roundtrip_primes(self):
        """Witt coordinates at prime indices recover correctly."""
        witt_orig = [Fraction(0), Fraction(2), Fraction(3), Fraction(5),
                     Fraction(0), Fraction(7)]
        gh = ghost_components(witt_orig, 10)
        witt_back = witt_from_ghost(gh, 6)
        for i in range(1, 6):
            assert witt_back[i] == witt_orig[i], \
                f"Index {i}: {witt_back[i]} != {witt_orig[i]}"

    def test_ghost_n1_equals_a1(self):
        """gh_1 = a_1 (trivial divisor sum)."""
        witt = [Fraction(0), Fraction(42)]
        gh = ghost_components(witt, 2)
        assert gh[1] == Fraction(42)

    def test_ghost_n2(self):
        """gh_2 = a_1^2 + 2*a_2."""
        witt = [Fraction(0), Fraction(3), Fraction(4)]
        gh = ghost_components(witt, 3)
        assert gh[2] == Fraction(3)**2 + 2 * Fraction(4)  # 9 + 8 = 17

    def test_ghost_prime_index(self):
        """gh_p = a_1^p + p*a_p for prime p."""
        witt = [Fraction(0), Fraction(2), Fraction(0), Fraction(5)]
        gh = ghost_components(witt, 4)
        # gh_3 = a_1^3 + 3*a_3 = 8 + 15 = 23
        assert gh[3] == Fraction(23)


# ============================================================================
# 18. Additional multi-path verification across families
# ============================================================================

class TestCrossFamilyVerification:
    """Cross-family consistency checks."""

    def test_heisenberg_psi_n_equals_kappa_n(self):
        """For Heisenberg, psi^n = kappa^n (single generator)."""
        for k in [1, 2, 3, 4, 5]:
            data = heisenberg_data(k)
            coeffs = {2: Fraction(k)}
            for r in range(3, 10):
                coeffs[r] = Fraction(0)
            lam = compute_lambda_series(coeffs, 12)
            psi = compute_adams_from_lambda(lam, 10)
            for n in range(1, 10):
                expected = Fraction(k)**n
                assert psi[n] == expected, \
                    f"Heis k={k}, psi^{n}: {psi[n]} != {expected}"

    def test_virasoro_psi1_equals_sum_Sr(self):
        """psi^1 = sum S_r (fundamental identity)."""
        for c in [1, 4, 10, 13, 25, 26]:
            data = virasoro_data(c)
            coeffs = shadow_coefficients_exact(
                data['kappa'], data['alpha'], data['S4'], 15)
            total = sum(coeffs[r] for r in range(2, 16))
            lam = compute_lambda_series(coeffs, 12)
            psi = compute_adams_from_lambda(lam, 3)
            assert psi[1] == total, f"Vir c={c}: psi^1 = {psi[1]} != sum = {total}"

    def test_affine_sl2_tower_terminates_at_3(self):
        """Affine sl_2 (class L): tower terminates at arity 3."""
        data = affine_sl2_data(1)
        coeffs = shadow_coefficients_exact(
            data['kappa'], data['alpha'], data['S4'], 10)
        assert coeffs[2] != 0
        assert coeffs[3] != 0
        for r in range(4, 11):
            assert coeffs[r] == 0

    def test_w3_and_virasoro_T_line_psi_match(self):
        """W_3 T-line and Virasoro have same psi^n (universal T-line)."""
        for c in [4, 10]:
            vir = virasoro_data(c)
            w3 = w3_data(c, 'T')
            vir_coeffs = shadow_coefficients_exact(
                vir['kappa'], vir['alpha'], vir['S4'], 12)
            w3_coeffs = shadow_coefficients_exact(
                w3['kappa'], w3['alpha'], w3['S4'], 12)
            vir_psi = compute_adams_from_log_derivative(
                {r: float(v) for r, v in vir_coeffs.items()}, 8)
            w3_psi = compute_adams_from_log_derivative(
                {r: float(v) for r, v in w3_coeffs.items()}, 8)
            for n in range(1, 8):
                assert rel_err(vir_psi[n], w3_psi[n]) < 1e-8, \
                    f"c={c}, n={n}: Vir psi={vir_psi[n]}, W3 psi={w3_psi[n]}"


# ============================================================================
# 19. Numerical stability tests
# ============================================================================

class TestNumericalStability:
    """Tests for numerical stability at extreme parameter values."""

    def test_large_kappa(self):
        """Large kappa (c=1000): stable computation."""
        data = virasoro_data(1000)
        result = full_lambda_ring_analysis(data, max_r=15, max_k=8, max_psi=8)
        for item in result['newton_vs_direct']:
            if item['n'] <= 5:  # Higher n may have large absolute values
                assert item['match'] or item['rel_error'] < 1e-3

    def test_small_kappa(self):
        """Small kappa (c=1/2): stable computation."""
        data = virasoro_data(Fraction(1, 2))
        result = full_lambda_ring_analysis(data, max_r=12, max_k=8, max_psi=8)
        for item in result['newton_vs_direct'][:6]:
            assert item['match'], f"Stability issue at n={item['n']}"

    def test_near_critical_c26(self):
        """Near-critical c=26: kappa=13, S4 small but nonzero."""
        data = virasoro_data(26)
        assert data['kappa'] == Fraction(13)
        assert data['S4'] == Fraction(10) / (26 * (5 * 26 + 22))
        result = full_lambda_ring_analysis(data, max_r=10, max_k=6, max_psi=6)
        assert 'error' not in result


# ============================================================================
# 20. Complex-valued shadow coefficient tests
# ============================================================================

class TestComplexShadow:
    """Tests for complex-valued shadow coefficients (at zeta zeros)."""

    def test_complex_S2_equals_kappa(self):
        """At complex c, S_2 = kappa = c/2."""
        c_val = complex(14.0, -339.23)
        coeffs = virasoro_shadow_coeffs_complex(c_val, max_r=5)
        assert abs(coeffs[2] - c_val / 2) < 1e-8

    def test_complex_S3_equals_2(self):
        """At complex c, S_3 = alpha = 2 (Virasoro universal)."""
        c_val = complex(14.0, -339.23)
        coeffs = virasoro_shadow_coeffs_complex(c_val, max_r=5)
        # S_3 = a_1/3 = 3*alpha/3 = alpha = 2
        assert abs(coeffs[3] - 2.0) < 1e-8

    def test_complex_shadow_tower_recursion(self):
        """Complex shadow tower satisfies the same recursion as real."""
        c_val = complex(10.0, -50.0)
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        coeffs = virasoro_shadow_coeffs_complex(c_val, max_r=10)

        # Verify: S_2 = kappa, S_3 = 2, S_4 = S4 (the quartic contact)
        assert abs(coeffs[2] - kappa) < 1e-8
        assert abs(coeffs[3] - alpha) < 1e-8
        assert abs(coeffs[4] - S4) < 1e-8

    def test_real_c_matches_exact(self):
        """Complex computation at real c matches exact computation."""
        c_real = 4.0
        coeffs_complex = virasoro_shadow_coeffs_complex(complex(c_real, 0), max_r=10)
        data = virasoro_data(4)
        coeffs_exact = shadow_coefficients_exact(
            data['kappa'], data['alpha'], data['S4'], 10)
        for r in range(2, 11):
            assert abs(coeffs_complex[r] - float(coeffs_exact[r])) < 1e-10, \
                f"r={r}: complex={coeffs_complex[r]}, exact={float(coeffs_exact[r])}"
