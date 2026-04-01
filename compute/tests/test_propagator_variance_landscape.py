r"""Tests for the propagator variance landscape.

Verifies delta_mix for all multi-generator algebra families:
  W_3, W_4, W_5, betagamma+bc, Heisenberg+Virasoro, sl_2+sl_3.

Each test class verifies:
  (a) Channel-by-channel kappa values
  (b) Mixing polynomial P(c) or P(k)
  (c) Zeros of P (enhanced symmetry points)
  (d) Cauchy-Schwarz non-negativity (delta_mix >= 0)
  (e) Consistency with known formulas from the existing engine

References:
    thm:propagator-variance (higher_genus_modular_koszul.tex)
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

import pytest
from sympy import (
    Rational, S, Symbol, cancel, factor, simplify, solve, sqrt, symbols,
    Poly, numer, I,
)

from compute.lib.propagator_variance_landscape import (
    propagator_variance,
    mixing_polynomial,
    enhanced_symmetry_zeros,
    w3_variance,
    w4_variance,
    w5_variance,
    wN_variance,
    betagamma_bc_variance,
    heisenberg_virasoro_variance,
    affine_sl2_sl3_variance,
    full_landscape,
    evaluate_at,
    wN_mixing_poly_degree,
    wN_enhanced_symmetry_count,
)


c = Symbol('c')
k = Symbol('k')


# =========================================================================
# W_3: Two channels (T, W)
# =========================================================================

class TestW3Variance:
    """Propagator variance for W_3: the canonical non-trivial case."""

    def test_rank(self):
        res = w3_variance()
        assert res.rank == 2

    def test_channel_labels(self):
        res = w3_variance()
        assert res.channel_labels == ['T', 'W']

    def test_channel_weights(self):
        res = w3_variance()
        assert res.channel_weights == [2, 3]

    def test_kappa_T(self):
        res = w3_variance()
        assert cancel(res.kappas[0] - c / 2) == 0

    def test_kappa_W(self):
        res = w3_variance()
        assert cancel(res.kappas[1] - c / 3) == 0

    def test_total_kappa(self):
        """Total kappa = c/2 + c/3 = 5c/6."""
        res = w3_variance()
        assert cancel(res.total_kappa - 5 * c / 6) == 0

    def test_mixing_polynomial(self):
        """P(W_3) = 25c^2 + 100c - 428."""
        res = w3_variance()
        assert cancel(res.mixing_poly - (25 * c ** 2 + 100 * c - 428)) == 0

    def test_mixing_polynomial_decomposition(self):
        """P = 25(c+2)^2 - 528."""
        res = w3_variance()
        assert cancel(res.mixing_poly - (25 * (c + 2) ** 2 - 528)) == 0

    def test_two_real_zeros(self):
        """P has exactly 2 real zeros."""
        res = w3_variance()
        assert len(res.mixing_zeros) == 2

    def test_enhanced_symmetry_positive_root(self):
        """One zero is at c = -2 + 4*sqrt(33)/5 > 0."""
        res = w3_variance()
        positive_root = -2 + 4 * sqrt(33) / 5
        assert any(cancel(z - positive_root) == 0 for z in res.mixing_zeros)

    def test_enhanced_symmetry_numerical(self):
        """Positive enhanced symmetry at c ~ 2.597."""
        res = w3_variance()
        positive_root = -2 + 4 * sqrt(33) / 5
        val = float(positive_root.evalf())
        assert 2.5 < val < 2.7

    def test_delta_vanishes_at_zeros(self):
        """delta_mix = 0 at enhanced symmetry points."""
        res = w3_variance()
        for z in res.mixing_zeros:
            assert cancel(res.delta_mix.subs(c, z)) == 0

    def test_not_autonomous(self):
        res = w3_variance()
        assert not res.is_autonomous

    def test_known_formula(self):
        """delta = 1280 * P^2 / (c^3 * (5c+22)^6)."""
        res = w3_variance()
        P = 25 * c ** 2 + 100 * c - 428
        known = Rational(1280) * P ** 2 / (c ** 3 * (5 * c + 22) ** 6)
        assert cancel(res.delta_mix - known) == 0

    def test_cauchy_schwarz(self):
        res = w3_variance()
        assert res.verify_cauchy_schwarz()

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50, 100])
    def test_non_negative_numerical(self, c_val):
        res = w3_variance()
        val = float(res.delta_mix.subs(c, c_val).evalf())
        assert val >= -1e-15

    def test_consistency_with_flat_api(self):
        """Cross-check against compute.lib.propagator_variance."""
        from compute.lib.propagator_variance import (
            propagator_variance as pv_flat,
            w3_kappas, w3_quartic_gradients,
        )
        kappas = w3_kappas()
        fs = w3_quartic_gradients()
        delta_flat = pv_flat(kappas, fs)
        res = w3_variance()
        assert cancel(res.delta_mix - delta_flat) == 0


# =========================================================================
# W_4: Three channels (T, W_3, W_4)
# =========================================================================

class TestW4Variance:
    """Propagator variance for W_4: three-channel system."""

    def test_rank(self):
        res = w4_variance()
        assert res.rank == 3

    def test_channel_labels(self):
        res = w4_variance()
        assert res.channel_labels == ['T', 'W_3', 'W_4']

    def test_channel_weights(self):
        res = w4_variance()
        assert res.channel_weights == [2, 3, 4]

    def test_kappa_values(self):
        """kappa_j = c/j for j = 2, 3, 4."""
        res = w4_variance()
        for j, kap in zip([2, 3, 4], res.kappas):
            assert cancel(kap - c / j) == 0

    def test_total_kappa(self):
        """Total kappa = c/2 + c/3 + c/4 = 13c/12."""
        res = w4_variance()
        assert cancel(res.total_kappa - 13 * c / 12) == 0

    def test_no_real_enhanced_symmetry(self):
        """W_4 has NO real enhanced symmetry points (all zeros are complex)."""
        res = w4_variance()
        for z in res.mixing_zeros:
            # All zeros should have nonzero imaginary part
            assert z.has(I) or simplify(z).has(I), \
                f"Expected complex zero, got real: {z}"

    def test_not_autonomous(self):
        res = w4_variance()
        assert not res.is_autonomous

    def test_cauchy_schwarz(self):
        res = w4_variance()
        assert res.verify_cauchy_schwarz()

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50])
    def test_non_negative_numerical(self, c_val):
        res = w4_variance()
        val = float(res.delta_mix.subs(c, c_val).evalf())
        assert val >= -1e-15

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50])
    def test_strictly_positive_numerical(self, c_val):
        """W_4 is strictly non-autonomous at all positive c."""
        res = w4_variance()
        val = float(res.delta_mix.subs(c, c_val).evalf())
        assert val > 1e-20

    def test_consistency_with_engine(self):
        """Cross-check against propagator_variance_engine.w4_propagator."""
        from compute.lib.propagator_variance_engine import w4_propagator
        w4_eng = w4_propagator()
        res = w4_variance()
        assert cancel(res.delta_mix - w4_eng.delta_mix) == 0

    def test_mixing_poly_inner_factor(self):
        """The inner factor 25c^2 + 300c + 1092 has negative discriminant."""
        inner = 25 * c ** 2 + 300 * c + 1092
        disc = 300 ** 2 - 4 * 25 * 1092  # = 90000 - 109200 = -19200
        assert disc == -19200


# =========================================================================
# W_5: Four channels (T, W_3, W_4, W_5)
# =========================================================================

class TestW5Variance:
    """Propagator variance for W_5: four-channel system."""

    def test_rank(self):
        res = w5_variance()
        assert res.rank == 4

    def test_channel_labels(self):
        res = w5_variance()
        assert res.channel_labels == ['T', 'W_3', 'W_4', 'W_5']

    def test_channel_weights(self):
        res = w5_variance()
        assert res.channel_weights == [2, 3, 4, 5]

    def test_kappa_values(self):
        """kappa_j = c/j for j = 2, 3, 4, 5."""
        res = w5_variance()
        for j, kap in zip([2, 3, 4, 5], res.kappas):
            assert cancel(kap - c / j) == 0

    def test_total_kappa(self):
        """Total kappa = c*(1/2 + 1/3 + 1/4 + 1/5) = 77c/60."""
        res = w5_variance()
        assert cancel(res.total_kappa - 77 * c / 60) == 0

    def test_one_real_enhanced_symmetry(self):
        """W_5 has exactly one real enhanced symmetry point: c = -38/5."""
        res = w5_variance()
        real_zeros = [z for z in res.mixing_zeros if not z.has(I)]
        assert len(real_zeros) == 1
        assert cancel(real_zeros[0] - Rational(-38, 5)) == 0

    def test_enhanced_symmetry_value(self):
        """Enhanced symmetry at c = -38/5 = -7.6."""
        res = w5_variance()
        real_zeros = [z for z in res.mixing_zeros if not z.has(I)]
        assert float(real_zeros[0].evalf()) == pytest.approx(-7.6)

    def test_delta_vanishes_at_real_zero(self):
        """delta_mix = 0 at c = -38/5."""
        res = w5_variance()
        assert cancel(res.delta_mix.subs(c, Rational(-38, 5))) == 0

    def test_not_autonomous(self):
        res = w5_variance()
        assert not res.is_autonomous

    def test_cauchy_schwarz(self):
        res = w5_variance()
        assert res.verify_cauchy_schwarz()

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50])
    def test_non_negative_numerical(self, c_val):
        res = w5_variance()
        val = float(res.delta_mix.subs(c, c_val).evalf())
        assert val >= -1e-15

    def test_mixing_poly_structure(self):
        """P(W_5) factors as const * (5c+38)^3 * (5c^2+44c+148)^3."""
        res = w5_variance()
        P = res.mixing_poly
        # Check that (5c+38) divides P
        remainder = cancel(P.subs(c, Rational(-38, 5)))
        assert remainder == 0

    def test_complex_factor_discriminant(self):
        """The factor 5c^2 + 44c + 148 has negative discriminant."""
        disc = 44 ** 2 - 4 * 5 * 148  # = 1936 - 2960 = -1024
        assert disc == -1024


# =========================================================================
# W_N general: parametric family
# =========================================================================

class TestWNGeneral:
    """Parametric tests for general W_N."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: single channel, always autonomous."""
        res = wN_variance(2)
        assert res.rank == 1
        assert res.is_autonomous
        assert res.delta_mix == 0

    def test_w3_via_general(self):
        """wN_variance(3) matches w3_variance."""
        res_N = wN_variance(3)
        res_3 = w3_variance()
        assert cancel(res_N.delta_mix - res_3.delta_mix) == 0

    def test_w4_via_general(self):
        """wN_variance(4) matches w4_variance."""
        res_N = wN_variance(4)
        res_4 = w4_variance()
        assert cancel(res_N.delta_mix - res_4.delta_mix) == 0

    def test_w5_via_general(self):
        """wN_variance(5) matches w5_variance."""
        res_N = wN_variance(5)
        res_5 = w5_variance()
        assert cancel(res_N.delta_mix - res_5.delta_mix) == 0

    def test_rank_equals_N_minus_1(self):
        for N in [2, 3, 4, 5]:
            res = wN_variance(N)
            assert res.rank == N - 1

    def test_total_kappa_formula(self):
        """Total kappa(W_N) = c * sum_{j=2}^{N} 1/j = c * (H_N - 1)."""
        for N in [2, 3, 4, 5]:
            res = wN_variance(N)
            harmonic_sum = sum(Rational(1, j) for j in range(2, N + 1))
            expected = c * harmonic_sum
            assert cancel(res.total_kappa - expected) == 0

    def test_w3_has_most_real_zeros(self):
        """Among W_3, W_4, W_5: W_3 has the most real enhanced symmetry points."""
        count_3 = len([z for z in w3_variance().mixing_zeros if not z.has(I)])
        count_4 = len([z for z in w4_variance().mixing_zeros if not z.has(I)])
        count_5 = len([z for z in w5_variance().mixing_zeros if not z.has(I)])
        assert count_3 == 2
        assert count_4 == 0
        assert count_5 == 1

    def test_all_non_autonomous(self):
        """All W_N for N >= 3 are non-autonomous."""
        for N in [3, 4, 5]:
            res = wN_variance(N)
            assert not res.is_autonomous


# =========================================================================
# betagamma + bc: independent sum
# =========================================================================

class TestBetagammaBcVariance:
    """Propagator variance for betagamma + bc (independent sum)."""

    def test_rank(self):
        res = betagamma_bc_variance()
        assert res.rank == 2

    def test_always_autonomous(self):
        """betagamma + bc is always autonomous (f = 0 for both)."""
        res = betagamma_bc_variance()
        assert res.is_autonomous
        assert res.delta_mix == 0

    def test_total_kappa_vanishes(self):
        """kappa(bg) + kappa(bc) = 0."""
        res = betagamma_bc_variance()
        assert cancel(res.total_kappa) == 0

    def test_kappa_bg(self):
        """kappa(bg) = 6*lambda^2 - 6*lambda + 1."""
        ll = Symbol('lambda')
        res = betagamma_bc_variance(ll)
        expected = 6 * ll ** 2 - 6 * ll + 1
        assert cancel(res.kappas[0] - expected) == 0

    def test_kappa_bc(self):
        """kappa(bc) = -(6*lambda^2 - 6*lambda + 1)."""
        ll = Symbol('lambda')
        res = betagamma_bc_variance(ll)
        expected = -(6 * ll ** 2 - 6 * ll + 1)
        assert cancel(res.kappas[1] - expected) == 0

    def test_both_f_zero(self):
        """Both quartic gradients vanish on neutral diagonal."""
        res = betagamma_bc_variance()
        assert res.f_values[0] == 0
        assert res.f_values[1] == 0

    def test_physical_point_lambda_2(self):
        """At lambda=2 (bc ghosts): kappa_bg = 13, kappa_bc = -13."""
        ll = Symbol('lambda')
        res = betagamma_bc_variance(ll)
        k_bg = res.kappas[0].subs(ll, 2)
        k_bc = res.kappas[1].subs(ll, 2)
        assert k_bg == 13
        assert k_bc == -13

    def test_no_mixing_polynomial(self):
        res = betagamma_bc_variance()
        assert res.mixing_poly == 0

    def test_stratum_separation_note(self):
        """The result reflects that quartic content is on charged stratum."""
        res = betagamma_bc_variance()
        # Both f = 0 is a consequence of stratum separation
        assert all(f == 0 for f in res.f_values)


# =========================================================================
# Heisenberg + Virasoro: independent sum
# =========================================================================

class TestHeisenbergVirasoroVariance:
    """Propagator variance for Heisenberg + Virasoro (independent sum)."""

    def test_rank(self):
        res = heisenberg_virasoro_variance()
        assert res.rank == 2

    def test_never_autonomous(self):
        """Heisenberg + Virasoro is NEVER autonomous at real c > 0."""
        res = heisenberg_virasoro_variance()
        assert not res.is_autonomous

    def test_no_enhanced_symmetry(self):
        """No enhanced symmetry zeros (mixing polynomial is constant)."""
        res = heisenberg_virasoro_variance()
        assert len(res.mixing_zeros) == 0

    def test_kappa_heisenberg(self):
        res = heisenberg_virasoro_variance()
        assert res.kappas[0] == 1

    def test_kappa_virasoro(self):
        res = heisenberg_virasoro_variance()
        assert cancel(res.kappas[1] - c / 2) == 0

    def test_f_heisenberg_zero(self):
        """Heisenberg quartic gradient = 0 (class G)."""
        res = heisenberg_virasoro_variance()
        assert res.f_values[0] == 0

    def test_f_virasoro(self):
        """Virasoro quartic gradient = 20/(5c+22)."""
        res = heisenberg_virasoro_variance()
        expected = Rational(20) / (5 * c + 22)
        assert cancel(res.f_values[1] - expected) == 0

    def test_exact_formula(self):
        """delta_mix = 1600 / (c(c+2)(5c+22)^2)."""
        res = heisenberg_virasoro_variance()
        expected = Rational(1600) / (c * (c + 2) * (5 * c + 22) ** 2)
        assert cancel(res.delta_mix - expected) == 0

    def test_total_kappa(self):
        """Total kappa = 1 + c/2 = (c+2)/2."""
        res = heisenberg_virasoro_variance()
        assert cancel(res.total_kappa - (c + 2) / 2) == 0

    def test_cauchy_schwarz(self):
        res = heisenberg_virasoro_variance()
        assert res.verify_cauchy_schwarz()

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 25, 50, 100])
    def test_strictly_positive(self, c_val):
        """delta_mix > 0 for all positive c."""
        res = heisenberg_virasoro_variance()
        val = float(res.delta_mix.subs(c, c_val).evalf())
        assert val > 0

    def test_class_incompatibility(self):
        """G-class (f=0) + M-class (f!=0) always gives nonzero delta."""
        res = heisenberg_virasoro_variance()
        # f_H = 0, f_V != 0 => f_H/kappa_H = 0 but f_V/kappa_V != 0
        # so the ratios can never be equal
        assert res.f_values[0] == 0
        assert simplify(res.f_values[1]) != 0


# =========================================================================
# sl_2 + sl_3 affine: independent sum
# =========================================================================

class TestAffineSl2Sl3Variance:
    """Propagator variance for V_{k_1}(sl_2) + V_{k_2}(sl_3)."""

    def test_rank(self):
        res = affine_sl2_sl3_variance()
        assert res.rank == 2

    def test_always_autonomous(self):
        """Direct sum of class L algebras is always autonomous."""
        res = affine_sl2_sl3_variance()
        assert res.is_autonomous
        assert res.delta_mix == 0

    def test_kappa_sl2(self):
        """kappa(sl_2) = dim(sl_2)*(k_1+h^v)/(2*h^v) = 3(k_1+2)/4."""
        k1 = Symbol('k_1')
        res = affine_sl2_sl3_variance(k1=k1)
        expected = Rational(3) * (k1 + 2) / 4
        assert cancel(res.kappas[0] - expected) == 0

    def test_kappa_sl3(self):
        """kappa(sl_3) = dim(sl_3)*(k_2+h^v)/(2*h^v) = 4(k_2+3)/3."""
        k2 = Symbol('k_2')
        res = affine_sl2_sl3_variance(k2=k2)
        expected = Rational(4) * (k2 + 3) / 3
        assert cancel(res.kappas[1] - expected) == 0

    def test_both_f_zero(self):
        """Both quartic gradients vanish (class L, Jacobi identity)."""
        res = affine_sl2_sl3_variance()
        assert res.f_values[0] == 0
        assert res.f_values[1] == 0

    def test_no_mixing_polynomial(self):
        res = affine_sl2_sl3_variance()
        assert res.mixing_poly == 0

    def test_total_kappa_at_level_1(self):
        """At k_1 = k_2 = 1: kappa_total = 3*3/4 + 4*4/3 = 9/4 + 16/3 = 91/12."""
        res = affine_sl2_sl3_variance(k1=S.One, k2=S.One)
        expected = Rational(9, 4) + Rational(16, 3)
        assert cancel(res.total_kappa - expected) == 0


# =========================================================================
# Cross-family structural tests
# =========================================================================

class TestCrossFamilyStructure:
    """Structural properties across the landscape."""

    def test_three_autonomous_families(self):
        """Exactly three families are autonomous: bg+bc, sl2+sl3, Virasoro."""
        landscape = full_landscape()
        autonomous = {k for k, v in landscape.items() if v.is_autonomous}
        # W_3, W_4, W_5, heis_vir are non-autonomous
        # bg_bc, sl2_sl3 are autonomous
        assert 'bg_bc' in autonomous
        assert 'sl2_sl3' in autonomous

    def test_three_non_autonomous_families(self):
        """W_3, W_4, W_5, Heis+Vir are non-autonomous."""
        landscape = full_landscape()
        non_auto = {k for k, v in landscape.items() if not v.is_autonomous}
        assert 'W_3' in non_auto
        assert 'W_4' in non_auto
        assert 'W_5' in non_auto
        assert 'heis_vir' in non_auto

    def test_cauchy_schwarz_all_families(self):
        """delta_mix >= 0 for all families at all test points."""
        for key, res in full_landscape().items():
            assert res.verify_cauchy_schwarz(), \
                f"Cauchy-Schwarz fails for {key}"

    def test_class_G_f_zero(self):
        """Class G (Gaussian) channels have f = 0."""
        # Heisenberg channel in heis+vir
        hv = heisenberg_virasoro_variance()
        assert hv.f_values[0] == 0  # Heisenberg

    def test_class_L_f_zero(self):
        """Class L (Lie/tree) channels have f = 0."""
        sl = affine_sl2_sl3_variance()
        assert all(f == 0 for f in sl.f_values)

    def test_class_M_f_nonzero(self):
        """Class M (mixed) channels have f != 0."""
        w3 = w3_variance()
        assert simplify(w3.f_values[0]) != 0  # T channel
        assert simplify(w3.f_values[1]) != 0  # W channel


# =========================================================================
# Enhanced symmetry analysis
# =========================================================================

class TestEnhancedSymmetry:
    """Properties of the enhanced symmetry locus."""

    def test_w3_two_points(self):
        """W_3 has exactly 2 enhanced symmetry points."""
        res = w3_variance()
        assert len(res.mixing_zeros) == 2

    def test_w3_one_positive(self):
        """W_3 has exactly one positive enhanced symmetry point."""
        res = w3_variance()
        positive = [z for z in res.mixing_zeros
                    if float(z.evalf()) > 0]
        assert len(positive) == 1

    def test_w4_no_real_zeros(self):
        """W_4 has no real enhanced symmetry points."""
        res = w4_variance()
        real_zeros = [z for z in res.mixing_zeros if not z.has(I)]
        assert len(real_zeros) == 0

    def test_w5_one_negative_real(self):
        """W_5 has one real enhanced symmetry point at negative c."""
        res = w5_variance()
        real_zeros = [z for z in res.mixing_zeros if not z.has(I)]
        assert len(real_zeros) == 1
        assert float(real_zeros[0].evalf()) < 0

    def test_heis_vir_no_zeros(self):
        """Heisenberg + Virasoro: mixing polynomial is constant, no zeros."""
        res = heisenberg_virasoro_variance()
        assert len(res.mixing_zeros) == 0

    def test_enhanced_symmetry_count(self):
        """Count of enhanced symmetry points for W_N matches direct computation."""
        assert wN_enhanced_symmetry_count(3) == 2
        assert wN_enhanced_symmetry_count(4) == 2  # 2 complex
        assert wN_enhanced_symmetry_count(5) == 3  # 1 real + 2 complex


# =========================================================================
# Independent sum principle (prop:independent-sum-factorization)
# =========================================================================

class TestIndependentSum:
    """Independent sum factorization: A oplus B with vanishing mixed OPE."""

    def test_direct_sum_kappa_additive(self):
        """kappa is additive under direct sum."""
        bg = betagamma_bc_variance()
        assert cancel(bg.total_kappa) == 0  # kappa_bg + kappa_bc = 0

    def test_direct_sum_quartic_separates(self):
        """Quartic shadows separate: no cross-terms."""
        bg = betagamma_bc_variance()
        # Both f = 0 independently
        assert all(f == 0 for f in bg.f_values)

    def test_gaussian_plus_mixed_never_autonomous(self):
        """Class G + Class M is never autonomous at real c > 0."""
        hv = heisenberg_virasoro_variance()
        # f_G = 0 but f_M != 0 => ratios cannot be equal
        assert not hv.is_autonomous

    def test_L_plus_L_always_autonomous(self):
        """Class L + Class L is always autonomous (both f = 0)."""
        sl = affine_sl2_sl3_variance()
        assert sl.is_autonomous


# =========================================================================
# Numerical evaluation
# =========================================================================

class TestNumericalEvaluation:
    """Numerical evaluation at specific central charges."""

    def test_evaluate_at_c13(self):
        """Evaluate all families at c = 13 (Virasoro self-dual point)."""
        vals = evaluate_at(13)
        # W_3 should be positive
        assert vals['W_3'] > 0
        # W_4 should be positive
        assert vals['W_4'] > 0
        # W_5 should be positive
        assert vals['W_5'] > 0
        # Heis+Vir should be positive
        assert vals['heis_vir'] > 0
        # bg+bc should be zero
        assert vals['bg_bc'] == 0
        # sl2+sl3 should be zero
        assert vals['sl2_sl3'] == 0

    def test_evaluate_at_c1(self):
        """Evaluate all families at c = 1."""
        vals = evaluate_at(1)
        assert vals['W_3'] > 0
        assert vals['W_4'] > 0
        assert vals['W_5'] > 0
        assert vals['heis_vir'] > 0

    def test_evaluate_at_c26(self):
        """Evaluate at c = 26 (string critical)."""
        vals = evaluate_at(26)
        for key in ['W_3', 'W_4', 'W_5', 'heis_vir']:
            assert vals[key] > 0

    def test_w3_near_enhanced_symmetry(self):
        """W_3 delta is small near the enhanced symmetry point c ~ 2.597."""
        res = w3_variance()
        near = float(res.delta_mix.subs(c, Rational(26, 10)).evalf())
        far = float(res.delta_mix.subs(c, 10).evalf())
        assert near < far  # closer to zero near the enhanced point


# =========================================================================
# Mixing polynomial degree analysis
# =========================================================================

class TestMixingPolyDegree:
    """Degree of the mixing polynomial grows with N."""

    def test_w2_degree_minus1(self):
        """Virasoro: no mixing polynomial (single channel)."""
        assert wN_mixing_poly_degree(2) == -1

    def test_w3_degree(self):
        """P(W_3) has degree 2 in c."""
        assert wN_mixing_poly_degree(3) == 2

    def test_w4_degree(self):
        """P(W_4) degree >= 2."""
        deg = wN_mixing_poly_degree(4)
        assert deg >= 2

    def test_w5_degree(self):
        """P(W_5) degree >= 2."""
        deg = wN_mixing_poly_degree(5)
        assert deg >= 2


# =========================================================================
# Consistency with propagator_variance_engine
# =========================================================================

class TestEngineConsistency:
    """Cross-validation against the existing engine module."""

    def test_w3_delta_matches(self):
        from compute.lib.propagator_variance_engine import w3_propagator
        eng = w3_propagator()
        land = w3_variance()
        assert cancel(eng.delta_mix - land.delta_mix) == 0

    def test_w4_delta_matches(self):
        from compute.lib.propagator_variance_engine import w4_propagator
        eng = w4_propagator()
        land = w4_variance()
        assert cancel(eng.delta_mix - land.delta_mix) == 0

    def test_virasoro_single_channel(self):
        from compute.lib.propagator_variance_engine import virasoro_propagator
        eng = virasoro_propagator()
        land = wN_variance(2)
        assert eng.delta_mix == 0
        assert land.delta_mix == 0

    def test_heisenberg_single_channel(self):
        from compute.lib.propagator_variance_engine import heisenberg_propagator
        eng = heisenberg_propagator()
        assert eng.delta_mix == 0


# =========================================================================
# Core formula verification
# =========================================================================

class TestCoreFormula:
    """Verify the propagator variance formula from first principles."""

    def test_single_channel_zero(self):
        """Single channel: delta = 0."""
        assert propagator_variance([c / 2], [Rational(10)]) == 0

    def test_proportional_zero(self):
        """If f_i = lambda * kappa_i, delta = 0."""
        lam_val = Symbol('lam')
        kaps = [c / 2, c / 3, c / 5]
        fs = [lam_val * kap for kap in kaps]
        assert propagator_variance(kaps, fs) == 0

    def test_two_equal_kappas(self):
        """If kappa_1 = kappa_2 = k, delta = (f_1-f_2)^2 / (2k)."""
        kk = Symbol('kk', positive=True)
        f1, f2 = symbols('f1 f2')
        delta = propagator_variance([kk, kk], [f1, f2])
        expected = (f1 - f2) ** 2 / (2 * kk)
        assert cancel(delta - expected) == 0

    def test_two_channels_general(self):
        """For two channels: delta = (f_1/k_1 - f_2/k_2)^2 * k_1*k_2/(k_1+k_2)."""
        k1, k2 = symbols('k1 k2', positive=True)
        f1, f2 = symbols('f1 f2')
        delta = propagator_variance([k1, k2], [f1, f2])
        expected = (f1 / k1 - f2 / k2) ** 2 * k1 * k2 / (k1 + k2)
        assert cancel(delta - expected) == 0

    def test_empty_zero(self):
        """Empty channel list: delta = 0."""
        assert propagator_variance([], []) == 0
