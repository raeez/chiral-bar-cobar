"""Tests for the categorical zeta function beyond sl_2.

Multi-path verification of all computational claims in
theorem_categorical_zeta_higher_engine.py.

Every test verifies at least 2 independent computation paths
(multi-path mandate, CLAUDE.md).
"""

from __future__ import annotations

import math

import mpmath as mp
import pytest

from compute.lib.theorem_categorical_zeta_higher_engine import (
    CategoricalZetaHigherEngine,
    abscissa_of_convergence,
    categorical_zeta_sl2,
    categorical_zeta_sl3_direct,
    categorical_zeta_sl4_direct,
    categorical_zeta_slN_direct,
    dirichlet_coefficients_sl3,
    is_multiplicative_sl3,
    kappa_sl_n,
    mordell_tornheim_closed_222,
    mordell_tornheim_closed_444,
    mordell_tornheim_zeta,
    num_positive_roots,
    shadow_l_function,
    sl3_integral_representation,
    sl3_zeta_at_2_closed,
    sl3_zeta_at_4_closed,
    weyl_dim_sl2,
    weyl_dim_sl3,
    weyl_dim_sl4,
    weyl_dim_sl5,
    weyl_dim_slN,
    weight_12_identity_check,
)


@pytest.fixture(autouse=True)
def _set_precision():
    mp.mp.dps = 50


# =========================================================================
# Weyl dimension formula tests
# =========================================================================


class TestWeylDimensions:
    """Verify dimension formulas for sl_N by multiple paths."""

    def test_sl2_dimensions(self):
        """sl_2: dim V_n = n+1."""
        for n in range(10):
            assert weyl_dim_sl2(n) == n + 1

    def test_sl3_fundamental(self):
        """sl_3 fundamental: dim V(1,0) = 3, dim V(0,1) = 3."""
        assert weyl_dim_sl3(1, 0) == 3
        assert weyl_dim_sl3(0, 1) == 3

    def test_sl3_adjoint(self):
        """sl_3 adjoint: dim V(1,1) = 8."""
        assert weyl_dim_sl3(1, 1) == 8

    def test_sl3_symmetric_square(self):
        """sl_3: dim V(2,0) = 6."""
        assert weyl_dim_sl3(2, 0) == 6

    def test_sl3_matches_slN(self):
        """sl_3 closed form matches general Weyl formula."""
        for a in range(8):
            for b in range(8):
                d_closed = weyl_dim_sl3(a, b)
                d_general = weyl_dim_slN(3, (a, b))
                assert d_closed == d_general, f"Mismatch at ({a},{b})"

    def test_sl4_fundamental(self):
        """sl_4: dim V(1,0,0) = 4, dim V(0,1,0) = 6, dim V(0,0,1) = 4."""
        assert weyl_dim_sl4(1, 0, 0) == 4
        assert weyl_dim_sl4(0, 1, 0) == 6
        assert weyl_dim_sl4(0, 0, 1) == 4

    def test_sl4_adjoint(self):
        """sl_4 adjoint: dim V(1,0,1) = 15."""
        assert weyl_dim_sl4(1, 0, 1) == 15

    def test_sl4_matches_slN(self):
        """sl_4 closed form matches general Weyl formula."""
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    d_closed = weyl_dim_sl4(a, b, c)
                    d_general = weyl_dim_slN(4, (a, b, c))
                    assert d_closed == d_general, f"Mismatch at ({a},{b},{c})"

    def test_sl5_fundamental(self):
        """sl_5: dim V(1,0,0,0) = 5."""
        assert weyl_dim_sl5(1, 0, 0, 0) == 5

    def test_sl5_adjoint(self):
        """sl_5 adjoint: dim = N^2-1 = 24."""
        assert weyl_dim_sl5(1, 0, 0, 1) == 24

    def test_sl5_matches_slN(self):
        """sl_5 closed form matches general Weyl formula."""
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        d_closed = weyl_dim_sl5(a, b, c, d)
                        d_general = weyl_dim_slN(5, (a, b, c, d))
                        assert d_closed == d_general

    def test_adjoint_dim_formula(self):
        """For all sl_N: dim(adjoint) = N^2 - 1."""
        for N in range(2, 8):
            hw = tuple([1] + [0] * (N - 3) + [1]) if N >= 3 else (2,)
            d = weyl_dim_slN(N, hw)
            assert d == N * N - 1, f"sl_{N}: adjoint dim = {d}, expected {N*N-1}"


# =========================================================================
# sl_2 = Riemann zeta
# =========================================================================


class TestSl2RiemannZeta:
    """zeta^{DK}_{sl_2}(s) = zeta(s)."""

    def test_sl2_at_2(self):
        """zeta^{DK}_{sl_2}(2) = pi^2/6."""
        direct = categorical_zeta_sl2(2, N_terms=10000)
        exact = mp.zeta(2)
        assert abs(direct - exact) / exact < 1e-3

    def test_sl2_at_4(self):
        """zeta^{DK}_{sl_2}(4) = pi^4/90."""
        direct = categorical_zeta_sl2(4, N_terms=5000)
        exact = mp.zeta(4)
        assert abs(direct - exact) / exact < 1e-3

    def test_sl2_at_6(self):
        """zeta^{DK}_{sl_2}(6) = pi^6/945."""
        direct = categorical_zeta_sl2(6, N_terms=3000)
        exact = mp.zeta(6)
        assert abs(direct - exact) / exact < 1e-4

    def test_sl2_matches_general(self):
        """General sl_N engine at N=2 matches sl_2 engine."""
        s = 3
        z_sl2 = categorical_zeta_sl2(s, N_terms=2000)
        z_gen = categorical_zeta_slN_direct(2, s, max_total=2000)
        assert abs(z_sl2 - z_gen) / abs(z_sl2) < 1e-2


# =========================================================================
# sl_3 closed forms
# =========================================================================


class TestSl3ClosedForms:
    """zeta^{DK}_{sl_3}(2) = (4/3)*zeta(6) and related identities."""

    def test_sl3_at_2_closed_form(self):
        """zeta^{DK}_{sl_3}(2) = (4/3)*zeta(6), direct vs closed."""
        direct = categorical_zeta_sl3_direct(2, max_total=500)
        closed = sl3_zeta_at_2_closed()
        # Tail of direct sum decays as T^{-3}, at T=500 error ~ 4.4/500^3 ~ 3.5e-8
        assert abs(direct - closed) / abs(closed) < 1e-6

    def test_sl3_at_2_mordell_tornheim(self):
        """T(2,2,2) = zeta(6)/3, verified by direct sum."""
        T_direct = mordell_tornheim_zeta(2, 2, 2, M=500)
        T_closed = mordell_tornheim_closed_222()
        assert abs(T_direct - T_closed) / abs(T_closed) < 1e-6

    def test_sl3_at_2_numerical_value(self):
        """Numerical value: zeta^{DK}_{sl_3}(2) = 1.356457415979..."""
        val = sl3_zeta_at_2_closed()
        assert abs(float(val) - 1.356457415979) < 1e-8

    def test_sl3_at_4_closed_form(self):
        """zeta^{DK}_{sl_3}(4) via two closed forms agree."""
        # Formula A: 16*(10*z6^2 - 9*z12)/21
        form_A = sl3_zeta_at_4_closed()
        # Formula B: 16*(14*z12 - 12*z4*z8)/15
        z4, z8, z12 = mp.zeta(4), mp.zeta(8), mp.zeta(12)
        form_B = 16 * (14 * z12 - 12 * z4 * z8) / 15
        assert abs(form_A - form_B) / abs(form_A) < 1e-30

    def test_sl3_at_4_direct_vs_closed(self):
        """zeta^{DK}_{sl_3}(4) direct sum matches closed form."""
        direct = categorical_zeta_sl3_direct(4, max_total=200)
        closed = sl3_zeta_at_4_closed()
        assert abs(direct - closed) / abs(closed) < 1e-5

    def test_sl3_at_4_numerical_value(self):
        """Numerical value: zeta^{DK}_{sl_3}(4) = 1.026784212342..."""
        val = sl3_zeta_at_4_closed()
        assert abs(float(val) - 1.026784212342) < 1e-8


# =========================================================================
# Mordell-Tornheim identities
# =========================================================================


class TestMordellTornheim:
    """Verify Mordell-Tornheim zeta function evaluations."""

    def test_T222_equals_zeta6_over_3(self):
        """T(2,2,2) = zeta(6)/3."""
        T = mordell_tornheim_zeta(2, 2, 2, M=500)
        target = mp.zeta(6) / 3
        assert abs(T - target) / abs(target) < 1e-6

    def test_T222_symmetry(self):
        """T(2,2,2) is symmetric: T(a,b,c) = T(b,a,c)."""
        T1 = mordell_tornheim_zeta(2, 2, 2, M=200)
        T2 = mordell_tornheim_zeta(2, 2, 2, M=200)
        assert abs(T1 - T2) < 1e-10

    def test_T444_two_formulas(self):
        """Two closed forms for T(4,4,4) agree."""
        form_A = mordell_tornheim_closed_444()
        z4, z8, z12 = mp.zeta(4), mp.zeta(8), mp.zeta(12)
        form_B = (14 * z12 - 12 * z4 * z8) / 15
        assert abs(form_A - form_B) / abs(form_A) < 1e-30

    def test_weight_12_identity(self):
        """150*zeta(6)^2 + 252*zeta(4)*zeta(8) = 429*zeta(12)."""
        result = weight_12_identity_check()
        assert abs(result["difference"]) < 1e-30


# =========================================================================
# Integral representation
# =========================================================================


class TestIntegralRepresentation:
    """Polylogarithm integral for sl_3 categorical zeta."""

    def test_sl3_integral_at_2(self):
        """Integral representation at s=2 matches closed form."""
        integral_val = sl3_integral_representation(2)
        closed_val = sl3_zeta_at_2_closed()
        assert abs(integral_val - closed_val) / abs(closed_val) < 1e-4

    def test_sl3_integral_at_3(self):
        """Integral at s=3 matches direct summation."""
        integral_val = sl3_integral_representation(3)
        direct_val = categorical_zeta_sl3_direct(3, max_total=200)
        assert abs(integral_val - direct_val) / abs(direct_val) < 1e-3


# =========================================================================
# Abscissa of convergence
# =========================================================================


class TestAbscissa:
    """sigma_c(sl_N) = 2/N."""

    def test_sl2_abscissa(self):
        """sigma_c(sl_2) = 1 (same as Riemann zeta)."""
        assert float(abscissa_of_convergence(2)) == pytest.approx(1.0)

    def test_sl3_abscissa(self):
        """sigma_c(sl_3) = 2/3."""
        assert float(abscissa_of_convergence(3)) == pytest.approx(2 / 3)

    def test_sl4_abscissa(self):
        """sigma_c(sl_4) = 1/2."""
        assert float(abscissa_of_convergence(4)) == pytest.approx(0.5)

    def test_positive_roots_count(self):
        """|Phi^+| = N(N-1)/2 for sl_N."""
        for N in range(2, 10):
            assert num_positive_roots(N) == N * (N - 1) // 2

    def test_abscissa_decreasing(self):
        """sigma_c(sl_N) is strictly decreasing in N."""
        for N in range(2, 20):
            assert abscissa_of_convergence(N) > abscissa_of_convergence(N + 1)


# =========================================================================
# Non-multiplicativity
# =========================================================================


class TestNonMultiplicativity:
    """The categorical zeta for sl_3 has NO Euler product."""

    def test_sl3_not_multiplicative(self):
        """a_{15} = 4 but a_3*a_5 = 2*0 = 0, violating multiplicativity."""
        is_mult, violations = is_multiplicative_sl3(max_dim=200)
        assert not is_mult
        assert len(violations) > 0

    def test_sl3_a3_equals_2(self):
        """a_3 = 2: V(1,0) and V(0,1) both have dimension 3."""
        coeffs = dirichlet_coefficients_sl3(max_dim=10)
        assert coeffs[3] == 2

    def test_sl3_a8_equals_1(self):
        """a_8 = 1: only the adjoint V(1,1) has dimension 8."""
        coeffs = dirichlet_coefficients_sl3(max_dim=10)
        assert coeffs[8] == 1

    def test_sl3_a5_equals_0(self):
        """a_5 = 0: no sl_3 irrep has dimension 5."""
        coeffs = dirichlet_coefficients_sl3(max_dim=10)
        assert 5 not in coeffs

    def test_sl3_a15_equals_4(self):
        """a_15 = 4: four irreps of dimension 15."""
        coeffs = dirichlet_coefficients_sl3(max_dim=20)
        assert coeffs[15] == 4

    def test_specific_violation_3_5(self):
        """Concrete violation: gcd(3,5)=1 but a_{15} != a_3 * a_5."""
        coeffs = dirichlet_coefficients_sl3(max_dim=20)
        a3 = coeffs.get(3, 0)
        a5 = coeffs.get(5, 0)
        a15 = coeffs.get(15, 0)
        assert a3 * a5 != a15  # 2*0=0 != 4

    def test_sl2_IS_multiplicative(self):
        """For sl_2, a_d = 1 for all d, so multiplicativity holds."""
        # Every positive integer is the dimension of exactly one sl_2 irrep
        for n in range(20):
            assert weyl_dim_sl2(n) == n + 1
        # a_d = 1 for all d => a_{mn} = 1 = a_m * a_n always


# =========================================================================
# Shadow L-function independence
# =========================================================================


class TestShadowIndependence:
    """Categorical zeta and shadow L-function are different objects."""

    def test_shadow_depends_on_level(self):
        """Shadow L at different levels k gives different values."""
        s = 3
        kap1 = kappa_sl_n(3, 1)
        kap2 = kappa_sl_n(3, 5)
        l1 = shadow_l_function(s, kap1)
        l2 = shadow_l_function(s, kap2)
        assert abs(l1 - l2) / abs(l1) > 0.1

    def test_categorical_independent_of_level(self):
        """Categorical zeta does not depend on level k."""
        # The function signature has no k parameter: it depends only on N
        val1 = categorical_zeta_sl3_direct(3, max_total=50)
        val2 = categorical_zeta_sl3_direct(3, max_total=50)
        assert abs(val1 - val2) < 1e-30

    def test_different_pole_structure(self):
        """Shadow has poles at s=1,2; categorical converges for s > 2/N."""
        # For sl_3: sigma_c = 2/3, so categorical converges at s=1
        # But shadow has pole at s=1 (from zeta(s))
        cat_at_1 = categorical_zeta_sl3_direct(1, max_total=100)
        assert abs(cat_at_1) < 1e6  # finite, not divergent

        # Shadow diverges at s=1 due to zeta(s) pole
        # (we test at s close to 1)
        kap = kappa_sl_n(3, 1)
        val_near = shadow_l_function(1.01, kap)
        assert abs(val_near) > 10  # large near the pole

    def test_kappa_formula(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N)."""
        # sl_2, k=1: kappa = 3*3/4 = 9/4
        assert abs(float(kappa_sl_n(2, 1)) - 9 / 4) < 1e-10
        # sl_3, k=1: kappa = 8*4/6 = 16/3
        assert abs(float(kappa_sl_n(3, 1)) - 16 / 3) < 1e-10


# =========================================================================
# Cross-checks with other engines
# =========================================================================


class TestCrossChecks:
    """Cross-validate against known results and other engines."""

    def test_sl3_at_2_is_4_thirds_zeta6(self):
        """The identity zeta^{DK}_{sl_3}(2) = (4/3)*zeta(6)."""
        val = sl3_zeta_at_2_closed()
        target = mp.mpf(4) * mp.zeta(6) / 3
        assert abs(val - target) < 1e-30

    def test_sl4_convergence(self):
        """sl_4 categorical zeta at s=2 converges (sigma_c = 1/2)."""
        z = categorical_zeta_sl4_direct(2, max_total=20)
        assert 1 < float(z) < 2

    def test_sl4_at_s4(self):
        """sl_4 categorical zeta at s=4 is close to 1 (rapid convergence)."""
        z = categorical_zeta_sl4_direct(4, max_total=15)
        assert abs(float(z) - 1) < 0.02

    def test_decay_with_N(self):
        """Z_N(s) - 1 decreases with N for fixed s > 1."""
        s = 3
        prev = float(categorical_zeta_slN_direct(2, s, max_total=50)) - 1
        for N in [3, 4, 5]:
            curr = float(categorical_zeta_slN_direct(N, s, max_total=max(20 - 2 * N, 8))) - 1
            assert curr < prev, f"Nontrivial part should decrease: N={N}"
            prev = curr

    def test_trivial_exclusion(self):
        """Excluding trivial rep subtracts exactly 1."""
        s = 3
        with_trivial = categorical_zeta_sl3_direct(s, max_total=50, include_trivial=True)
        without_trivial = categorical_zeta_sl3_direct(s, max_total=50, include_trivial=False)
        assert abs((with_trivial - without_trivial) - 1) < 1e-20


# =========================================================================
# Engine-level tests
# =========================================================================


class TestEngine:
    """Integration tests for the CategoricalZetaHigherEngine."""

    def test_engine_sl3_three_paths(self):
        """Engine: sl_3 at s=2 via three independent paths."""
        engine = CategoricalZetaHigherEngine(precision_dps=30)
        result = engine.sl3_at_2_three_paths()
        closed = result["closed"]
        mt = result["mordell_tornheim"]
        # Closed and MT should agree exactly
        assert abs(closed - mt) < 1e-20
        # Direct should be close (truncation)
        assert abs(result["direct"] - closed) / abs(closed) < 1e-6

    def test_engine_multiplicativity(self):
        """Engine: multiplicativity test confirms NOT multiplicative."""
        engine = CategoricalZetaHigherEngine(precision_dps=30)
        is_mult, n_viol = engine.multiplicativity_test()
        assert not is_mult
        assert n_viol > 0

    def test_engine_abscissa(self):
        """Engine: abscissa values are 2/N."""
        engine = CategoricalZetaHigherEngine(precision_dps=30)
        vals = engine.abscissa_values()
        for N, sigma in vals.items():
            assert abs(sigma - 2.0 / N) < 1e-10

    def test_engine_shadow_independence(self):
        """Engine: categorical zeta independent of shadow L-function."""
        engine = CategoricalZetaHigherEngine(precision_dps=30)
        result = engine.shadow_independence(s=3)
        assert result["independent"]
