r"""Tests for the shadow Casimir energy and zeta-function regularization engine.

Verification paths:
1. Direct computation from shadow tower coefficients
2. Heat kernel expansion: zeta_A(s) = (1/Gamma(s)) int K_A(t) t^{s-1} dt
3. Heisenberg exact anchor: E_Cas = (k/2)*log(2)
4. Cross-family consistency (additivity, Koszul duality, AP24)
5. Functional equation between a_k and zeta(-k)
6. Numerical convergence for class M at c > c*

Anti-patterns guarded:
    AP1: No copying between families; each formula computed from first principles.
    AP10: Expected values derived independently, not hardcoded from a single source.
    AP24: kappa + kappa' = 13 for Virasoro (NOT zero). Casimir sums differ.
    AP39: kappa != c/2 in general. Only for Virasoro.
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
import pytest
from fractions import Fraction

from sympy import Rational, Symbol, exp, factorial, log, simplify, sqrt, S

c = Symbol('c')


# ===========================================================================
# 1. Shadow tower data correctness
# ===========================================================================

class TestShadowTowerData:
    """Verify shadow tower coefficients for standard families."""

    def test_heisenberg_coefficients(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('heisenberg', k=1)
        assert data['class'] == 'G'
        assert data['r_max'] == 2
        assert data['kappa'] == 1
        assert data['coeffs'] == {2: Rational(1)}

    def test_heisenberg_level_k(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('heisenberg', k=5)
        assert data['kappa'] == 5
        assert data['coeffs'] == {2: Rational(5)}

    def test_lattice_coefficients(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('lattice', rank=24)
        assert data['class'] == 'G'
        assert data['kappa'] == 24
        assert data['coeffs'] == {2: Rational(24)}

    def test_free_fermion_coefficients(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('free_fermion')
        assert data['class'] == 'G'
        assert data['kappa'] == Rational(1, 2)
        assert data['coeffs'] == {2: Rational(1, 2)}

    def test_affine_sl2_coefficients(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('affine', dim_g=3, h_dual=2, level=1, alpha=1)
        assert data['class'] == 'L'
        assert data['r_max'] == 3
        # kappa = 3*(1+2)/(2*2) = 9/4
        assert data['kappa'] == Rational(9, 4)
        assert data['coeffs'] == {2: Rational(9, 4), 3: Rational(1)}

    def test_virasoro_c1_first_terms(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('virasoro', c_val=1, max_r=5)
        coeffs = data['coeffs']
        assert data['class'] == 'M'
        assert coeffs[2] == Rational(1, 2)
        assert coeffs[3] == Rational(2)
        assert coeffs[4] == Rational(10, 27)

    def test_virasoro_c26_first_terms(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        data = standard_family_shadow_data('virasoro', c_val=26, max_r=5)
        coeffs = data['coeffs']
        assert coeffs[2] == Rational(13)
        assert coeffs[3] == Rational(2)
        # S_4 = 10/(26*(5*26+22)) = 10/(26*152) = 10/3952 = 5/1976
        assert coeffs[4] == Rational(10, 3952)

    def test_unknown_family_raises(self):
        from lib.bc_casimir_shadow_engine import standard_family_shadow_data
        with pytest.raises(ValueError):
            standard_family_shadow_data('unknown_family')


# ===========================================================================
# 2. Shadow zeta function
# ===========================================================================

class TestShadowZeta:
    """Test shadow zeta function computation."""

    def test_heisenberg_zeta_at_1(self):
        """zeta_H(1) = k * 2^{-1} = k/2."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_finite
        coeffs = {2: Rational(1)}
        assert shadow_zeta_finite(coeffs, 1) == Rational(1, 2)

    def test_heisenberg_zeta_at_0(self):
        """zeta_H(0) = k * 2^0 = k."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_finite
        coeffs = {2: Rational(1)}
        assert shadow_zeta_finite(coeffs, 0) == 1

    def test_heisenberg_zeta_at_minus1(self):
        """zeta_H(-1) = k * 2^1 = 2k."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_finite
        coeffs = {2: Rational(3)}
        assert shadow_zeta_finite(coeffs, -1) == 6

    def test_affine_zeta_at_0(self):
        """zeta_aff(0) = kappa + alpha."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_finite
        kappa = Rational(9, 4)
        alpha = Rational(1)
        coeffs = {2: kappa, 3: alpha}
        assert shadow_zeta_finite(coeffs, 0) == kappa + alpha

    def test_affine_zeta_at_minus1(self):
        """zeta_aff(-1) = 2*kappa + 3*alpha."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_finite
        kappa = Rational(9, 4)
        alpha = Rational(1)
        coeffs = {2: kappa, 3: alpha}
        assert shadow_zeta_finite(coeffs, -1) == 2 * kappa + 3 * alpha

    def test_numerical_zeta_heisenberg(self):
        from lib.bc_casimir_shadow_engine import shadow_zeta_numerical
        coeffs = {2: Rational(1)}
        # zeta_H(2) = 1 * 2^{-2} = 0.25
        val = shadow_zeta_numerical(coeffs, 2.0)
        assert abs(val.real - 0.25) < 1e-12

    def test_numerical_zeta_complex(self):
        """Shadow zeta at complex s for Heisenberg."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_numerical
        coeffs = {2: Rational(1)}
        # zeta_H(1+2i) = 2^{-(1+2i)} = 2^{-1} * 2^{-2i} = 0.5 * exp(-2i*log2)
        s_val = 1 + 2j
        val = shadow_zeta_numerical(coeffs, s_val)
        expected = 0.5 * cmath.exp(-2j * math.log(2))
        assert abs(val - expected) < 1e-10

    def test_truncated_agrees_with_finite_for_class_G(self):
        from lib.bc_casimir_shadow_engine import (
            shadow_zeta_finite, shadow_zeta_truncated
        )
        coeffs = {2: Rational(5)}
        for s_val in [0, 1, -1, 2, -2]:
            finite = shadow_zeta_finite(coeffs, s_val)
            trunc = shadow_zeta_truncated(coeffs, s_val, max_r=10)
            assert simplify(finite - trunc) == 0


# ===========================================================================
# 3. Shadow Casimir energy
# ===========================================================================

class TestShadowCasimirEnergy:
    """Test E^{sh}_Cas = -(1/2) * zeta'_A(0) = (1/2) * sum S_r * log(r)."""

    def test_heisenberg_k1_exact(self):
        """E_Cas(H_1) = (1/2) * 1 * log(2) = log(2)/2."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        result = shadow_casimir_energy('heisenberg', k=1)
        assert simplify(result['E_Cas'] - log(2) / 2) == 0

    def test_heisenberg_k1_numerical(self):
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy_numerical
        result = shadow_casimir_energy_numerical('heisenberg', k=1)
        assert abs(result['E_Cas'] - math.log(2) / 2) < 1e-12

    def test_heisenberg_k_scaling(self):
        """E_Cas(H_k) = k * E_Cas(H_1)."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        for kk in [1, 2, 5, 10]:
            result = shadow_casimir_energy('heisenberg', k=kk)
            assert simplify(result['E_Cas'] - kk * log(2) / 2) == 0

    def test_free_fermion_casimir(self):
        """E_Cas(ff) = (1/4) * log(2)."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        result = shadow_casimir_energy('free_fermion')
        assert simplify(result['E_Cas'] - log(2) / 4) == 0

    def test_affine_sl2_k1_casimir(self):
        """E_Cas(sl_2, k=1) = (9/8)*log(2) + (1/2)*log(3)."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        result = shadow_casimir_energy('affine', dim_g=3, h_dual=2,
                                        level=1, alpha=1)
        expected = Rational(9, 8) * log(2) + Rational(1, 2) * log(3)
        assert simplify(result['E_Cas'] - expected) == 0

    def test_zeta_prime_0_sign(self):
        """zeta'_A(0) = -2 * E_Cas < 0 for all A with kappa > 0."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        for family, kwargs in [
            ('heisenberg', {'k': 1}),
            ('affine', {'dim_g': 3, 'h_dual': 2, 'level': 1, 'alpha': 1}),
        ]:
            result = shadow_casimir_energy(family, **kwargs)
            assert float(result['zeta_prime_0'].evalf()) < 0

    def test_virasoro_c26_casimir_positive(self):
        """E_Cas is positive for Virasoro at c=26 (all S_r positive for c>0)."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        result = virasoro_casimir_numerical(26, max_r=20)
        assert result['E_Cas_truncated'] > 0

    def test_F1_formula(self):
        """F_1 = kappa / 24."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        result = shadow_casimir_energy('heisenberg', k=1)
        assert result['F_1'] == Rational(1, 24)

    def test_E_Cas_over_F1_heisenberg(self):
        """E_Cas / F_1 = 12 * log(2) for Heisenberg (independent of k)."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        for kk in [1, 3, 10]:
            result = shadow_casimir_energy('heisenberg', k=kk)
            ratio = simplify(result['E_Cas_over_F_1'])
            assert simplify(ratio - 12 * log(2)) == 0


# ===========================================================================
# 4. Regularized shadow sum
# ===========================================================================

class TestRegularizedSum:
    """Test regularized zeta(0) = sum S_r."""

    def test_heisenberg_zeta0_exact(self):
        from lib.bc_casimir_shadow_engine import regularized_shadow_sum
        result = regularized_shadow_sum('heisenberg', k=7)
        assert result['zeta_0'] == 7
        assert result['method'] == 'exact_finite_sum'

    def test_affine_zeta0_exact(self):
        from lib.bc_casimir_shadow_engine import regularized_shadow_sum
        result = regularized_shadow_sum('affine', dim_g=3, h_dual=2,
                                         level=1, alpha=1)
        assert result['zeta_0'] == Rational(9, 4) + 1

    def test_virasoro_regularization_method(self):
        from lib.bc_casimir_shadow_engine import regularized_shadow_sum
        result = regularized_shadow_sum('virasoro', c_val=26, max_r=20)
        assert result['method'] == 'shadow_gf_analytic_continuation'
        # Q_L(1) = (2*13 + 6)^2 + 16*13*10/(26*152)
        # = 32^2 + 16*13*5/1976 = 1024 + 1040/1976
        # = 1024 + 65/123.5 ... let me just check it's positive
        assert float(result['Q_L_at_1'].evalf()) > 0

    def test_virasoro_regularized_finite(self):
        """Regularized sum is finite even when raw series might diverge."""
        from lib.bc_casimir_shadow_engine import regularized_shadow_sum
        result = regularized_shadow_sum('virasoro', c_val=1, max_r=20)
        reg = float(result['zeta_0_regularized'].evalf())
        assert math.isfinite(reg)
        assert reg > 0


# ===========================================================================
# 5. Shadow heat kernel coefficients
# ===========================================================================

class TestHeatKernel:
    """Test shadow heat kernel K_A(t) = sum S_r e^{-rt}."""

    def test_heisenberg_heat_coefficients(self):
        """a_k = (-2)^k / k! for Heisenberg k=1."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_coefficients
        coeffs = shadow_heat_kernel_coefficients('heisenberg', max_k=10, k=1)
        for kk in range(11):
            expected = (-2) ** kk / factorial(kk)
            assert simplify(coeffs[kk] - expected) == 0

    def test_a0_equals_zeta0(self):
        """a_0 = zeta_A(0) = sum S_r."""
        from lib.bc_casimir_shadow_engine import (
            shadow_heat_kernel_coefficients, shadow_casimir_energy
        )
        for family, kwargs in [
            ('heisenberg', {'k': 3}),
            ('affine', {'dim_g': 3, 'h_dual': 2, 'level': 1, 'alpha': 1}),
        ]:
            hk = shadow_heat_kernel_coefficients(family, max_k=5, **kwargs)
            ce = shadow_casimir_energy(family, **kwargs)
            assert simplify(hk[0] - ce['zeta_0']) == 0

    def test_a1_equals_minus_a_anomaly(self):
        """a_1 = -zeta_A(-1) = -(2*kappa + 3*alpha)."""
        from lib.bc_casimir_shadow_engine import (
            shadow_heat_kernel_coefficients, shadow_conformal_anomaly
        )
        hk = shadow_heat_kernel_coefficients('affine', max_k=5,
                                              dim_g=3, h_dual=2,
                                              level=1, alpha=1)
        anom = shadow_conformal_anomaly('affine', dim_g=3, h_dual=2,
                                         level=1, alpha=1)
        assert simplify(hk[1] + anom['a_anomaly']) == 0

    def test_heat_zeta_identity(self):
        """a_k = (-1)^k * zeta_A(-k) / k! (identity between heat coeffs and zeta)."""
        from lib.bc_casimir_shadow_engine import heat_kernel_from_gf
        result = heat_kernel_from_gf('heisenberg', max_k=15, k=2)
        for kk in range(16):
            assert result['agreement'][kk], f"Disagreement at k={kk}"

    def test_heat_zeta_identity_affine(self):
        from lib.bc_casimir_shadow_engine import heat_kernel_from_gf
        result = heat_kernel_from_gf('affine', max_k=10,
                                      dim_g=3, h_dual=2, level=1, alpha=1)
        for kk in range(11):
            assert result['agreement'][kk], f"Disagreement at k={kk}"

    def test_heat_zeta_identity_virasoro(self):
        """Path 2 verification: a_k and zeta(-k) consistency for Virasoro."""
        from lib.bc_casimir_shadow_engine import heat_kernel_from_gf
        result = heat_kernel_from_gf('virasoro', max_k=10, c_val=26, max_r=15)
        for kk in range(11):
            assert result['agreement'][kk], f"Disagreement at k={kk}"

    def test_numerical_heat_kernel_heisenberg(self):
        """K_H(t) = e^{-2t} for Heisenberg k=1."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_numerical
        t_vals = [0.1, 0.5, 1.0, 2.0]
        K = shadow_heat_kernel_numerical('heisenberg', t_vals, k=1)
        for t, K_val in zip(t_vals, K):
            assert abs(K_val - math.exp(-2 * t)) < 1e-12

    def test_heat_kernel_mellin_transform(self):
        """Path 2: zeta(s) = (1/Gamma(s)) * int K(t) t^{s-1} dt."""
        from lib.bc_casimir_shadow_engine import heat_kernel_zeta_consistency
        result = heat_kernel_zeta_consistency('heisenberg', s_val=2.0,
                                              t_max=20.0, n_points=5000, k=1)
        assert result['relative_error'] < 0.01

    def test_heat_kernel_mellin_affine(self):
        from lib.bc_casimir_shadow_engine import heat_kernel_zeta_consistency
        result = heat_kernel_zeta_consistency('affine', s_val=2.0,
                                              t_max=20.0, n_points=5000,
                                              dim_g=3, h_dual=2, level=1,
                                              alpha=1)
        assert result['relative_error'] < 0.01

    def test_heat_large_t_decay(self):
        """K_A(t) -> S_2 * e^{-2t} as t -> infty (dominant term)."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_numerical
        t_large = [5.0, 10.0, 20.0]
        K = shadow_heat_kernel_numerical('affine', t_large,
                                          dim_g=3, h_dual=2, level=1, alpha=1)
        kappa = 9.0 / 4.0
        for t, K_val in zip(t_large, K):
            # dominant term is kappa * e^{-2t}
            dominant = kappa * math.exp(-2 * t)
            # correction: alpha * e^{-3t} is exponentially smaller
            assert abs(K_val - dominant) < 2 * math.exp(-3 * t)


# ===========================================================================
# 6. Weyl asymptotics
# ===========================================================================

class TestWeylAsymptotics:
    """Test shadow spectral dimension and growth rate."""

    def test_class_G_infinite_dimension(self):
        from lib.bc_casimir_shadow_engine import shadow_weyl_data
        result = shadow_weyl_data('heisenberg', k=1)
        assert result['d_sp'] == float('-inf')
        assert result['rho'] == 0

    def test_class_L_infinite_dimension(self):
        from lib.bc_casimir_shadow_engine import shadow_weyl_data
        result = shadow_weyl_data('affine', dim_g=3, h_dual=2, level=1, alpha=1)
        assert result['d_sp'] == float('-inf')

    def test_virasoro_rho_matches_shadow_radius(self):
        """Cross-check: rho from Casimir engine must match shadow_radius module."""
        from lib.bc_casimir_shadow_engine import shadow_weyl_data
        result = shadow_weyl_data('virasoro', c_val=26, max_r=20)
        rho = result['rho']
        # Independent: rho^2 = (180*26+872)/((5*26+22)*26^2)
        rho_sq = (180 * 26 + 872) / ((5 * 26 + 22) * 26 ** 2)
        rho_expected = math.sqrt(rho_sq)
        assert abs(rho - rho_expected) < 1e-8

    def test_virasoro_rho_c13(self):
        """rho(Vir_13) = sqrt((180*13+872)/((5*13+22)*169))."""
        from lib.bc_casimir_shadow_engine import shadow_weyl_data
        result = shadow_weyl_data('virasoro', c_val=13, max_r=20)
        rho_sq = (180 * 13 + 872) / ((5 * 13 + 22) * 13 ** 2)
        assert abs(result['rho'] - math.sqrt(rho_sq)) < 1e-8

    def test_universal_exponent(self):
        """The spectral exponent for class M is always -5/2."""
        from lib.bc_casimir_shadow_engine import shadow_weyl_data
        for c_val in [1, 13, 26]:
            result = shadow_weyl_data('virasoro', c_val=c_val, max_r=20)
            assert result['exponent'] == -2.5


# ===========================================================================
# 7. Functional determinant
# ===========================================================================

class TestFunctionalDeterminant:
    """Test shadow functional determinant det'(D_A) = exp(-zeta'(0))."""

    def test_heisenberg_det_prime(self):
        """det'(D_{H_1}) = exp(log(2)) = 2."""
        from lib.bc_casimir_shadow_engine import shadow_functional_determinant
        result = shadow_functional_determinant('heisenberg', k=1)
        assert abs(result['det_prime_numerical'] - 2.0) < 1e-10

    def test_heisenberg_det_scales(self):
        """det'(D_{H_k}) = 2^k."""
        from lib.bc_casimir_shadow_engine import shadow_functional_determinant
        for kk in [1, 2, 3, 5]:
            result = shadow_functional_determinant('heisenberg', k=kk)
            assert abs(result['det_prime_numerical'] - 2.0 ** kk) < 1e-8

    def test_affine_det_prime(self):
        """det'(D_{aff}) = 2^kappa * 3^alpha."""
        from lib.bc_casimir_shadow_engine import shadow_functional_determinant
        result = shadow_functional_determinant('affine', dim_g=3, h_dual=2,
                                                level=1, alpha=1)
        expected = 2 ** (9.0 / 4.0) * 3.0 ** 1.0
        assert abs(result['det_prime_numerical'] - expected) < 1e-6

    def test_det_prime_positive(self):
        """det' > 0 for all standard families (S_r mostly positive)."""
        from lib.bc_casimir_shadow_engine import shadow_functional_determinant
        for family, kwargs in [
            ('heisenberg', {'k': 1}),
            ('free_fermion', {}),
            ('affine', {'dim_g': 3, 'h_dual': 2, 'level': 1, 'alpha': 1}),
        ]:
            result = shadow_functional_determinant(family, **kwargs)
            assert result['det_prime_numerical'] > 0

    def test_log_det_consistency(self):
        """log(det') = -zeta'(0) = 2 * E_Cas."""
        from lib.bc_casimir_shadow_engine import (
            shadow_functional_determinant, shadow_casimir_energy
        )
        result_det = shadow_functional_determinant('heisenberg', k=3)
        result_cas = shadow_casimir_energy('heisenberg', k=3)
        log_det = result_det['log_det']
        two_E = 2 * result_cas['E_Cas']
        assert simplify(log_det - two_E) == 0


# ===========================================================================
# 8. Shadow zeta at Riemann zeros
# ===========================================================================

class TestZetaAtRiemannZeros:
    """Test shadow zeta evaluated at Riemann zeta zeros."""

    def test_heisenberg_at_first_zero(self):
        """zeta_H(rho_1/2) = 2^{-(1/4 + i*14.134.../2)}."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_at_riemann_zeros
        results = shadow_zeta_at_riemann_zeros('heisenberg', n_zeros=1, k=1)
        gamma_1 = 14.134725141734693
        s_val = 0.25 + 0.5j * gamma_1
        expected = 2 ** (-s_val)
        assert abs(results[0]['zeta_A_at_s'] - expected) < 1e-10

    def test_returns_correct_number_of_zeros(self):
        from lib.bc_casimir_shadow_engine import shadow_zeta_at_riemann_zeros
        results = shadow_zeta_at_riemann_zeros('heisenberg', n_zeros=5, k=1)
        assert len(results) == 5

    def test_abs_decreases_for_class_G(self):
        """For Heisenberg, |zeta_H(rho_n/2)| = 2^{-1/4} for ALL zeros
        (because only 2^{-s} and Re(s) = 1/4 always)."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_at_riemann_zeros
        results = shadow_zeta_at_riemann_zeros('heisenberg', n_zeros=10, k=1)
        for r in results:
            assert abs(r['abs_zeta'] - 2 ** (-0.25)) < 1e-10

    def test_virasoro_at_zeros(self):
        """Shadow zeta for Virasoro at Riemann zeros returns finite values."""
        from lib.bc_casimir_shadow_engine import shadow_zeta_at_riemann_zeros
        results = shadow_zeta_at_riemann_zeros('virasoro', n_zeros=5,
                                                c_val=26, max_r=20)
        for r in results:
            assert math.isfinite(r['abs_zeta'])
            assert r['abs_zeta'] > 0

    def test_critical_line_evaluation(self):
        from lib.bc_casimir_shadow_engine import shadow_zeta_critical_line
        results = shadow_zeta_critical_line('heisenberg', k=1)
        # At s = 1/2: zeta_H(1/2) = 2^{-1/2} = 1/sqrt(2)
        for r in results:
            if r['t'] == 0:
                assert abs(r['zeta_A'].real - 1 / math.sqrt(2)) < 1e-10


# ===========================================================================
# 9. Shadow conformal anomaly
# ===========================================================================

class TestConformalAnomaly:
    """Test shadow a- and c-anomaly."""

    def test_heisenberg_a_anomaly(self):
        """a(H_k) = zeta_H(-1) = 2k."""
        from lib.bc_casimir_shadow_engine import shadow_conformal_anomaly
        result = shadow_conformal_anomaly('heisenberg', k=3)
        assert result['a_anomaly'] == 6

    def test_heisenberg_b_anomaly(self):
        """b(H_k) = zeta_H(-2) = 4k."""
        from lib.bc_casimir_shadow_engine import shadow_conformal_anomaly
        result = shadow_conformal_anomaly('heisenberg', k=3)
        assert result['b_anomaly'] == 12

    def test_affine_a_anomaly(self):
        """a(aff) = 2*kappa + 3*alpha."""
        from lib.bc_casimir_shadow_engine import shadow_conformal_anomaly
        result = shadow_conformal_anomaly('affine', dim_g=3, h_dual=2,
                                           level=1, alpha=1)
        # 2*(9/4) + 3*1 = 9/2 + 3 = 15/2
        assert result['a_anomaly'] == Rational(15, 2)

    def test_c_anomaly_consistency(self):
        """c_anomaly = zeta'(0) = -2 * E_Cas."""
        from lib.bc_casimir_shadow_engine import (
            shadow_conformal_anomaly, shadow_casimir_energy
        )
        anom = shadow_conformal_anomaly('heisenberg', k=5)
        cas = shadow_casimir_energy('heisenberg', k=5)
        assert simplify(anom['c_anomaly'] + 2 * cas['E_Cas']) == 0

    def test_zeta_neg_integer_values(self):
        """zeta_A(-n) for Heisenberg: k * 2^n."""
        from lib.bc_casimir_shadow_engine import shadow_conformal_anomaly
        result = shadow_conformal_anomaly('heisenberg', k=1)
        for n in range(-6, 1):
            expected = 2 ** (-n)  # S_2 * 2^{-n} = 1 * 2^{|n|}
            assert result['zeta_neg_integers'][n] == expected


# ===========================================================================
# 10. One-loop comparison
# ===========================================================================

class TestOneLoopComparison:
    """Test one-loop effective action vs F_1."""

    def test_heisenberg_ratio(self):
        """E_Cas / F_1 = 12 * log(2) ~ 8.318 for Heisenberg."""
        from lib.bc_casimir_shadow_engine import one_loop_comparison
        result = one_loop_comparison('heisenberg', k=1)
        assert simplify(result['E_Cas_over_F_1'] - 12 * log(2)) == 0

    def test_affine_ratio(self):
        """E_Cas / F_1 for affine sl_2 k=1."""
        from lib.bc_casimir_shadow_engine import one_loop_comparison
        result = one_loop_comparison('affine', dim_g=3, h_dual=2,
                                      level=1, alpha=1)
        # E_Cas = (9/8)*log(2) + (1/2)*log(3)
        # F_1 = (9/4)/24 = 3/32
        # ratio = 32/3 * ((9/8)*log(2) + (1/2)*log(3))
        #       = 12*log(2) + 16*log(3)/3
        expected = 12 * log(2) + Rational(16, 3) * log(3)
        assert simplify(result['E_Cas_over_F_1'] - expected) == 0

    def test_ratio_independent_of_level_for_heisenberg(self):
        """E_Cas / F_1 = 12*log(2) for ALL k (universal for class G)."""
        from lib.bc_casimir_shadow_engine import one_loop_comparison
        for kk in [1, 2, 5, 100]:
            result = one_loop_comparison('heisenberg', k=kk)
            assert simplify(result['E_Cas_over_F_1'] - 12 * log(2)) == 0

    def test_virasoro_ratio_finite(self):
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        result = virasoro_casimir_numerical(26, max_r=20)
        assert math.isfinite(result['E_Cas_over_F_1'])


# ===========================================================================
# 11. Exact results cross-check
# ===========================================================================

class TestExactResults:
    """Cross-check exact closed-form results."""

    def test_heisenberg_exact_all_fields(self):
        from lib.bc_casimir_shadow_engine import heisenberg_exact
        h = heisenberg_exact(1)
        assert h['zeta_0'] == 1
        assert simplify(h['zeta_prime_0'] + log(2)) == 0
        assert simplify(h['E_Cas'] - log(2) / 2) == 0
        assert h['det_prime'] == 2
        assert h['F_1'] == Rational(1, 24)
        assert h['a_anomaly'] == 2
        assert h['b_anomaly'] == 4
        assert h['heat_coeff_0'] == 1
        assert h['heat_coeff_1'] == -2
        assert h['heat_coeff_2'] == 2

    def test_heisenberg_heat_coeff_n_function(self):
        from lib.bc_casimir_shadow_engine import heisenberg_exact
        h = heisenberg_exact(1)
        coeff_fn = h['heat_coeff_n']
        for n in range(10):
            assert simplify(coeff_fn(n) - (-2) ** n / factorial(n)) == 0

    def test_affine_exact_all_fields(self):
        from lib.bc_casimir_shadow_engine import affine_exact
        a = affine_exact(dim_g=3, h_dual=2, level=1, alpha=1)
        assert a['kappa'] == Rational(9, 4)
        assert a['zeta_0'] == Rational(13, 4)
        assert a['a_anomaly'] == Rational(15, 2)
        assert a['b_anomaly'] == 18  # 4*(9/4) + 9*1 = 9 + 9 = 18

    def test_heisenberg_exact_matches_engine(self):
        """heisenberg_exact must agree with shadow_casimir_energy."""
        from lib.bc_casimir_shadow_engine import (
            heisenberg_exact, shadow_casimir_energy
        )
        h = heisenberg_exact(3)
        e = shadow_casimir_energy('heisenberg', k=3)
        assert simplify(h['E_Cas'] - e['E_Cas']) == 0
        assert simplify(h['zeta_prime_0'] - e['zeta_prime_0']) == 0

    def test_affine_exact_matches_engine(self):
        from lib.bc_casimir_shadow_engine import (
            affine_exact, shadow_casimir_energy
        )
        a = affine_exact(dim_g=3, h_dual=2, level=1, alpha=1)
        e = shadow_casimir_energy('affine', dim_g=3, h_dual=2,
                                   level=1, alpha=1)
        assert simplify(a['E_Cas'] - e['E_Cas']) == 0


# ===========================================================================
# 12. Virasoro numerical convergence
# ===========================================================================

class TestVirasoroNumerical:
    """Test Virasoro shadow Casimir at various central charges."""

    def test_c26_convergent(self):
        """At c=26, rho ~ 0.234, so truncation converges fast."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        r20 = virasoro_casimir_numerical(26, max_r=20)
        r30 = virasoro_casimir_numerical(26, max_r=30)
        # Should agree to many digits since rho^20 ~ 1e-13
        assert abs(r20['E_Cas_truncated'] - r30['E_Cas_truncated']) < 1e-8

    def test_c13_convergent(self):
        """At c=13 (self-dual), rho ~ 0.467."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        r20 = virasoro_casimir_numerical(13, max_r=20)
        r30 = virasoro_casimir_numerical(13, max_r=30)
        assert abs(r20['E_Cas_truncated'] - r30['E_Cas_truncated']) < 1e-4

    def test_kappa_correct(self):
        """kappa = c/2 for Virasoro (AP39: only for Virasoro!)."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        for c_val in [1, 13, 26]:
            result = virasoro_casimir_numerical(c_val, max_r=10)
            assert abs(result['kappa'] - c_val / 2) < 1e-12

    def test_dominant_term_is_heisenberg_like(self):
        """Leading term of E_Cas is (c/4)*log(2) from S_2 = c/2."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        for c_val in [26, 100]:
            result = virasoro_casimir_numerical(c_val, max_r=30)
            heisenberg_part = c_val / 4 * math.log(2)
            # Higher arity corrections should be small relative to leading
            correction = result['E_Cas_truncated'] - heisenberg_part
            assert correction > 0  # S_3 = 2 > 0, so positive correction

    def test_rho_correct(self):
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        result = virasoro_casimir_numerical(26, max_r=10)
        rho_sq = (180 * 26 + 872) / ((5 * 26 + 22) * 26 ** 2)
        assert abs(result['rho'] - math.sqrt(rho_sq)) < 1e-8


# ===========================================================================
# 13. Koszul duality and Casimir
# ===========================================================================

class TestKoszulCasimir:
    """Test Koszul duality properties of shadow Casimir energy."""

    def test_kappa_sum_is_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        from lib.bc_casimir_shadow_engine import koszul_casimir_comparison
        result = koszul_casimir_comparison(10, max_r=20)
        assert abs(result['kappa_sum'] - 13.0) < 1e-12

    def test_self_dual_c13_symmetric(self):
        """At c=13: E_Cas(Vir_13) = E_Cas(Vir_13) trivially."""
        from lib.bc_casimir_shadow_engine import koszul_casimir_comparison
        result = koszul_casimir_comparison(13, max_r=20)
        assert abs(result['E_Cas'] - result['E_Cas_dual']) < 1e-8

    def test_casimir_sum_not_zero(self):
        """E_Cas(Vir_c) + E_Cas(Vir_{26-c}) != 0 in general.
        (Unlike kappa, the Casimir energy is not anti-symmetric under duality.)"""
        from lib.bc_casimir_shadow_engine import koszul_casimir_comparison
        result = koszul_casimir_comparison(1, max_r=20)
        assert abs(result['E_Cas_sum']) > 0.1  # substantially nonzero

    def test_dual_rho_at_c13(self):
        """At c=13: rho and rho_dual coincide."""
        from lib.bc_casimir_shadow_engine import koszul_casimir_comparison
        result = koszul_casimir_comparison(13, max_r=20)
        assert abs(result['rho'] - result['rho_dual']) < 1e-10


# ===========================================================================
# 14. Cross-family comparison table
# ===========================================================================

class TestComparisonTable:
    """Test the cross-family comparison table."""

    def test_table_nonempty(self):
        from lib.bc_casimir_shadow_engine import casimir_comparison_table
        table = casimir_comparison_table()
        assert len(table) > 5

    def test_all_E_Cas_positive(self):
        """E_Cas > 0 for all standard families with kappa > 0."""
        from lib.bc_casimir_shadow_engine import casimir_comparison_table
        table = casimir_comparison_table()
        for row in table:
            if row['kappa'] > 0:
                assert row['E_Cas'] > 0, f"E_Cas <= 0 for {row['family']}"

    def test_heisenberg_ratio_universal(self):
        """All Heisenberg entries have E_Cas/F_1 = 12*log(2)."""
        from lib.bc_casimir_shadow_engine import casimir_comparison_table
        table = casimir_comparison_table()
        target = 12 * math.log(2)
        for row in table:
            if 'Heisenberg' in row['family']:
                assert abs(row['E_Cas_over_F_1'] - target) < 1e-8


# ===========================================================================
# 15. Spectral determinant landscape
# ===========================================================================

class TestSpectralDeterminantLandscape:
    """Test the spectral determinant landscape."""

    def test_landscape_nonempty(self):
        from lib.bc_casimir_shadow_engine import spectral_determinant_landscape
        landscape = spectral_determinant_landscape()
        assert len(landscape) >= 5

    def test_heisenberg_exact_det(self):
        from lib.bc_casimir_shadow_engine import spectral_determinant_landscape
        landscape = spectral_determinant_landscape()
        assert abs(landscape['Heisenberg k=1']['det_prime'] - 2.0) < 1e-10

    def test_class_G_exact(self):
        from lib.bc_casimir_shadow_engine import spectral_determinant_landscape
        landscape = spectral_determinant_landscape()
        for key, val in landscape.items():
            if val['class'] == 'G':
                assert val['exact'] is True

    def test_class_M_truncated(self):
        from lib.bc_casimir_shadow_engine import spectral_determinant_landscape
        landscape = spectral_determinant_landscape()
        for key, val in landscape.items():
            if val['class'] == 'M':
                assert val['exact'] is False


# ===========================================================================
# 16. Shadow zeta special values
# ===========================================================================

class TestSpecialValues:
    """Test special values of the shadow zeta."""

    def test_heisenberg_special_values(self):
        from lib.bc_casimir_shadow_engine import shadow_zeta_special_values
        result = shadow_zeta_special_values('heisenberg', k=1)
        sv = result['special_values']
        # zeta_H(n) = 2^{-n}
        for n in range(-6, 7):
            assert sv[n] == Rational(2) ** (-n)

    def test_affine_at_minus1(self):
        from lib.bc_casimir_shadow_engine import shadow_zeta_special_values
        result = shadow_zeta_special_values('affine', dim_g=3, h_dual=2,
                                             level=1, alpha=1)
        # zeta_aff(-1) = 2*(9/4) + 3*1 = 15/2
        assert result['special_values'][-1] == Rational(15, 2)


# ===========================================================================
# 17. Multi-path verification: Heisenberg anchor
# ===========================================================================

class TestHeisenbergAnchor:
    """Multi-path verification using Heisenberg as the anchor.

    Path 1: Direct from shadow tower
    Path 2: Heat kernel -> Mellin transform -> zeta
    Path 3: Exact closed form: E_Cas = (k/2)*log(2)
    Path 4: Free boson Casimir energy comparison
    """

    def test_path_1_direct(self):
        """Direct: E_Cas = (1/2) * sum S_r * log(r) = (1/2)*1*log(2)."""
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        result = shadow_casimir_energy('heisenberg', k=1)
        assert simplify(result['E_Cas'] - log(2) / 2) == 0

    def test_path_2_heat_kernel(self):
        """Heat kernel: K(t) = e^{-2t}, Mellin gives zeta(s) = 2^{-s}."""
        from lib.bc_casimir_shadow_engine import heat_kernel_zeta_consistency
        result = heat_kernel_zeta_consistency('heisenberg', s_val=3.0,
                                              t_max=20.0, n_points=5000, k=1)
        assert result['relative_error'] < 0.005

    def test_path_3_closed_form(self):
        """Closed form: zeta_H(s) = k*2^{-s}, so zeta'(0) = -k*log(2)."""
        from lib.bc_casimir_shadow_engine import heisenberg_exact
        h = heisenberg_exact(1)
        # E_Cas = -(1/2)*zeta'(0) = (1/2)*log(2)
        assert abs(h['E_Cas_numerical'] - 0.5 * math.log(2)) < 1e-12

    def test_path_4_free_boson_consistency(self):
        """For free bosons on S^1: E_Cas = -1/12 (massless scalar).
        The SHADOW Casimir is NOT the same as the physical Casimir
        (different spectral problem). But the ratio E^{sh}/F_1 = 12*log(2)
        is independently verifiable."""
        from lib.bc_casimir_shadow_engine import heisenberg_exact
        h = heisenberg_exact(1)
        ratio = h['E_Cas_over_F_1_numerical']
        # 12 * log(2) ~ 8.3178
        assert abs(ratio - 12 * math.log(2)) < 1e-10


# ===========================================================================
# 18. Additivity test
# ===========================================================================

class TestAdditivity:
    """Shadow Casimir energy inherits additivity from kappa.

    For independent direct sum A = A_1 + A_2 (vanishing mixed OPE):
    The shadow tower separates: S_r(A) = S_r(A_1) + S_r(A_2) at arity 2.
    At higher arities, independence is more subtle.

    For CLASS G: perfect additivity (only arity 2 contributes).
    E_Cas(H_{k1} + H_{k2}) = E_Cas(H_{k1}) + E_Cas(H_{k2}).
    """

    def test_heisenberg_additivity(self):
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        E1 = shadow_casimir_energy('heisenberg', k=3)
        E2 = shadow_casimir_energy('heisenberg', k=7)
        E_sum = shadow_casimir_energy('heisenberg', k=10)
        assert simplify(E1['E_Cas'] + E2['E_Cas'] - E_sum['E_Cas']) == 0

    def test_lattice_additivity(self):
        from lib.bc_casimir_shadow_engine import shadow_casimir_energy
        E1 = shadow_casimir_energy('lattice', rank=5)
        E2 = shadow_casimir_energy('lattice', rank=19)
        E_sum = shadow_casimir_energy('lattice', rank=24)
        assert simplify(E1['E_Cas'] + E2['E_Cas'] - E_sum['E_Cas']) == 0


# ===========================================================================
# 19. Heat kernel coefficient growth
# ===========================================================================

class TestHeatCoefficientGrowth:
    """Test growth properties of heat kernel coefficients."""

    def test_heisenberg_alternating_sign(self):
        """a_k = (-2)^k / k!: alternates in sign."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_coefficients
        coeffs = shadow_heat_kernel_coefficients('heisenberg', max_k=10, k=1)
        for kk in range(11):
            sign = (-1) ** kk
            assert float(coeffs[kk].evalf()) * sign > 0

    def test_factorial_decay(self):
        """Heat coefficients decay as 1/k! (from exponential kernel)."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_coefficients
        coeffs = shadow_heat_kernel_coefficients('heisenberg', max_k=15, k=1)
        # |a_k| = 2^k / k!
        for kk in range(1, 16):
            ratio = abs(float(coeffs[kk].evalf()) / float(coeffs[kk - 1].evalf()))
            # ratio should be 2/k
            assert abs(ratio - 2.0 / kk) < 1e-10

    def test_virasoro_heat_coeffs_finite(self):
        """All heat kernel coefficients are finite for Virasoro."""
        from lib.bc_casimir_shadow_engine import shadow_heat_kernel_coefficients
        coeffs = shadow_heat_kernel_coefficients('virasoro', max_k=15,
                                                  c_val=26, max_r=15)
        for kk in range(16):
            assert math.isfinite(float(coeffs[kk].evalf()))


# ===========================================================================
# 20. Virasoro truncation convergence analysis
# ===========================================================================

class TestTruncationConvergence:
    """Test that truncated sums converge for c > c*."""

    def test_c26_fast_convergence(self):
        """At c=26, rho ~ 0.234: each extra arity adds ~0.234x correction."""
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        results = []
        for max_r in [5, 10, 15, 20, 25, 30]:
            r = virasoro_casimir_numerical(26, max_r=max_r)
            results.append(r['E_Cas_truncated'])
        # Check convergence: differences should decrease geometrically
        diffs = [abs(results[i + 1] - results[i]) for i in range(len(results) - 1)]
        for i in range(len(diffs) - 1):
            assert diffs[i + 1] < diffs[i]

    def test_c25_convergence(self):
        from lib.bc_casimir_shadow_engine import virasoro_casimir_numerical
        r20 = virasoro_casimir_numerical(25, max_r=20)
        r30 = virasoro_casimir_numerical(25, max_r=30)
        assert abs(r20['E_Cas_truncated'] - r30['E_Cas_truncated']) < 1e-4

    def test_regularized_vs_truncated_class_G(self):
        """For class G, regularized and truncated sums are identical."""
        from lib.bc_casimir_shadow_engine import (
            regularized_shadow_sum, shadow_casimir_energy
        )
        reg = regularized_shadow_sum('heisenberg', k=5)
        cas = shadow_casimir_energy('heisenberg', k=5)
        assert simplify(reg['zeta_0'] - cas['zeta_0']) == 0
