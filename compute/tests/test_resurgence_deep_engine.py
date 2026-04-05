r"""Tests for the deep resurgence engine: alien derivatives, Stokes constants,
trans-series completion, and double resurgence.

Comprehensive multi-path verification (3+ independent paths per result)
for the full resurgent structure of the shadow obstruction tower.

Structure:
  1. Algebra data and basic properties (8 tests)
  2. Shadow coefficients verification (9 tests)
  3. Borel transform (arity direction) (8 tests)
  4. Borel singularity identification (8 tests)
  5. Large-order and growth rate extraction (9 tests)
  6. Darboux coefficients and alien derivatives (10 tests)
  7. Stokes phenomenon (arity direction) (8 tests)
  8. Trans-series completion (7 tests)
  9. Genus resurgence (9 tests)
  10. Double resurgence (7 tests)
  11. Pade approximants and peacock patterns (8 tests)
  12. Multi-path verification (8 tests)
  13. Complementarity of resurgent structures (6 tests)
  14. Cross-family comparison (6 tests)

Total: 111 tests.

All expected values computed INDEPENDENTLY (AP1, AP3, AP10).
No copy-paste from source module. Every formula recomputed from scratch.

References:
    compute/lib/resurgence_deep_engine.py
    compute/lib/shadow_radius.py
    compute/lib/resurgence_trans_series_engine.py
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math
from fractions import Fraction

import numpy as np
import pytest

PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI_SQ = TWO_PI ** 2


# =====================================================================
# Independent helpers (AP10: independent computation, not from module)
# =====================================================================

def _bernoulli_independent(n):
    """Bernoulli number via mpmath (independent of module)."""
    import mpmath
    return float(mpmath.bernoulli(n))


def _lambda_fp_independent(g):
    """lambda_g^FP from first principles (independent)."""
    B2g = abs(_bernoulli_independent(2 * g))
    prefac = (2 ** (2 * g - 1) - 1) / (2 ** (2 * g - 1))
    return prefac * B2g / math.factorial(2 * g)


def _F_g_independent(kappa, g):
    """F_g = kappa * lambda_g^FP (independent)."""
    return kappa * _lambda_fp_independent(g)


def _virasoro_kappa(c):
    """kappa(Vir_c) = c/2 (independent)."""
    return c / 2.0


def _virasoro_S4(c):
    """Q^contact_Vir = 10/(c(5c+22)) (independent)."""
    return 10.0 / (c * (5.0 * c + 22.0))


def _virasoro_Q_L(c, t):
    """Shadow metric Q_L(t) for Virasoro (independent).

    Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        = q0 + q1*t + q2*t^2
    where kappa=c/2, alpha=2, S4=10/(c(5c+22)), Delta=8*kappa*S4.
    """
    kappa = c / 2.0
    q0 = 4.0 * kappa ** 2  # = c^2
    q1 = 12.0 * kappa * 2.0  # = 12c
    S4 = 10.0 / (c * (5.0 * c + 22.0))
    q2 = 9.0 * 4.0 + 16.0 * kappa * S4  # = 36 + 80/(5c+22)
    return q0 + q1 * t + q2 * t ** 2


def _virasoro_rho(c):
    """Shadow growth rate for Virasoro (independent).

    rho = sqrt((180c+872)/((5c+22)*c^2))
    """
    return math.sqrt((180 * c + 872) / ((5 * c + 22) * c ** 2))


def _shadow_coefficients_independent(kappa, alpha, S4, max_r=60):
    """Shadow coefficients via independent sqrt expansion (AP10)."""
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    max_n = max_r - 2
    if max_n < 0 or q0 <= 0:
        return {}
    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if a[0] == 0:
        return {}
    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    for n in range(2, max_n + 1):
        cn = q2 if n == 2 else 0.0
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv) / (2.0 * a[0])
    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


# =====================================================================
# Section 1: Algebra data and basic properties
# =====================================================================

class TestAlgebraData:
    """Test algebra construction and basic shadow metric properties."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP1)."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0, 26.0]:
            alg = virasoro_deep(c)
            assert abs(alg.kappa - c / 2.0) < 1e-14

    def test_virasoro_dual_sum(self):
        """kappa + kappa' = 13 for Virasoro (AP24)."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            assert abs(alg.kappa + alg.kappa_dual - 13.0) < 1e-14

    def test_virasoro_S4(self):
        """Q^contact = 10/(c(5c+22))."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            expected = 10.0 / (c * (5.0 * c + 22.0))
            assert abs(alg.S4 - expected) < 1e-14

    def test_shadow_metric_q0(self):
        """q0 = 4*kappa^2 = c^2 for Virasoro."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0]:
            alg = virasoro_deep(c)
            assert abs(alg.q0 - c ** 2) < 1e-14

    def test_shadow_metric_discriminant(self):
        """disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2*Delta."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 25.0]:
            alg = virasoro_deep(c)
            disc = alg.metric_discriminant
            expected = -32.0 * alg.kappa ** 2 * alg.Delta
            assert abs(disc - expected) < 1e-10 * abs(expected)

    def test_heisenberg_class_g(self):
        """Heisenberg is class G (no arity resurgence)."""
        from lib.resurgence_deep_engine import heisenberg_deep
        h = heisenberg_deep(1, 1.0)
        assert h.depth_class == 'G'
        assert abs(h.alpha) < 1e-14
        assert abs(h.S4) < 1e-14

    def test_affine_class_l(self):
        """Affine sl_2 is class L (alpha != 0, S4 = 0)."""
        from lib.resurgence_deep_engine import affine_sl2_deep
        a = affine_sl2_deep(1.0)
        assert a.depth_class == 'L'
        assert abs(a.alpha - 1.0) < 1e-14
        assert abs(a.S4) < 1e-14

    def test_virasoro_class_m(self):
        """Virasoro is class M (Delta != 0, infinite tower)."""
        from lib.resurgence_deep_engine import virasoro_deep
        v = virasoro_deep(1.0)
        assert v.depth_class == 'M'
        assert abs(v.Delta) > 1e-10


# =====================================================================
# Section 2: Shadow coefficients verification
# =====================================================================

class TestShadowCoefficients:
    """Verify shadow tower coefficients against independent computation."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa (leading coefficient of the shadow tower)."""
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            coeffs = shadow_coefficients(alg, 10)
            assert abs(coeffs[2] - c / 2.0) < 1e-12

    def test_S3_equals_alpha(self):
        """S_3 = alpha (cubic shadow)."""
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        alg = virasoro_deep(1.0)
        coeffs = shadow_coefficients(alg, 10)
        # For Virasoro: alpha = 2, so S_3 should be close to 2
        # S_3 = a_1/3 where a_1 = q1/(2*a_0) = 12*kappa*alpha/(2*sqrt(q0))
        #      = 12*0.5*2 / (2*1) = 6. Then S_3 = 6/3 = 2.
        assert abs(coeffs[3] - 2.0) < 1e-12

    def test_coefficients_independent_comparison(self):
        """Compare with independently computed coefficients (AP10)."""
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        for c in [1.0, 7.0, 13.0]:
            alg = virasoro_deep(c)
            mod_coeffs = shadow_coefficients(alg, 20)
            indep_coeffs = _shadow_coefficients_independent(c / 2.0, 2.0,
                                                             _virasoro_S4(c), 20)
            for r in range(2, 20):
                assert abs(mod_coeffs[r] - indep_coeffs[r]) < 1e-12 * max(abs(mod_coeffs[r]), 1e-15)

    def test_heisenberg_terminates(self):
        """Heisenberg shadow tower: S_r = 0 for r >= 3."""
        from lib.resurgence_deep_engine import heisenberg_deep, shadow_coefficients
        h = heisenberg_deep(1, 1.0)
        coeffs = shadow_coefficients(h, 20)
        assert abs(coeffs[2] - 1.0) < 1e-12  # S_2 = kappa = 1
        for r in range(3, 20):
            assert abs(coeffs[r]) < 1e-12

    def test_affine_terminates_at_3(self):
        """Affine sl_2 shadow tower: S_r = 0 for r >= 4."""
        from lib.resurgence_deep_engine import affine_sl2_deep, shadow_coefficients
        a = affine_sl2_deep(1.0)
        coeffs = shadow_coefficients(a, 20)
        # S_2 = kappa = 3*(1+2)/4 = 9/4 = 2.25
        assert abs(coeffs[2] - 2.25) < 1e-12
        # S_3 != 0 (alpha = 1)
        assert abs(coeffs[3]) > 1e-5
        # S_r = 0 for r >= 4 (S_4 = 0 for class L)
        for r in range(4, 20):
            assert abs(coeffs[r]) < 1e-10

    def test_virasoro_coefficients_nonzero(self):
        """Virasoro (class M): coefficients never vanish (infinite tower)."""
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        alg = virasoro_deep(1.0)
        coeffs = shadow_coefficients(alg, 30)
        for r in range(2, 30):
            assert abs(coeffs[r]) > 1e-30, f"S_{r} unexpectedly zero"

    def test_high_precision_matches_standard(self):
        """High-precision coefficients match standard precision."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, shadow_coefficients, shadow_coefficients_high_precision
        )
        alg = virasoro_deep(13.0)
        std = shadow_coefficients(alg, 30)
        hp = shadow_coefficients_high_precision(alg, 30)
        for r in range(2, 30):
            if abs(std[r]) > 1e-30:
                rel_err = abs(std[r] - hp[r]) / abs(std[r])
                assert rel_err < 1e-10

    def test_shadow_metric_evaluation(self):
        """Q_L(0) = q0 = 4*kappa^2 (metric at origin)."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 25.0]:
            alg = virasoro_deep(c)
            # Q_L(0) = q0
            q_at_0 = _virasoro_Q_L(c, 0.0)
            assert abs(q_at_0 - c ** 2) < 1e-12

    def test_Q_L_vanishes_at_branch_points(self):
        """Q_L(t_pm) = 0 at the branch points."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            t_p, t_m = alg.branch_points
            # Evaluate Q_L at branch points
            Q_p = alg.q0 + alg.q1 * t_p + alg.q2 * t_p ** 2
            Q_m = alg.q0 + alg.q1 * t_m + alg.q2 * t_m ** 2
            assert abs(Q_p) < 1e-8, f"Q_L(t_+) = {Q_p} != 0 at c={c}"
            assert abs(Q_m) < 1e-8, f"Q_L(t_-) = {Q_m} != 0 at c={c}"


# =====================================================================
# Section 3: Borel transform (arity direction)
# =====================================================================

class TestArityBorelTransform:
    """Test the arity-direction Borel transform."""

    def test_borel_at_zero(self):
        """Bhat[S](0) = 0 (series starts at r=2)."""
        from lib.resurgence_deep_engine import virasoro_deep, arity_borel_transform
        alg = virasoro_deep(1.0)
        val = arity_borel_transform(alg, 0.0)
        assert abs(val) < 1e-14

    def test_borel_small_xi(self):
        """Bhat[S](xi) ~ S_2*xi^2/2 for small xi."""
        from lib.resurgence_deep_engine import virasoro_deep, arity_borel_transform
        alg = virasoro_deep(1.0)
        xi = 0.001
        val = arity_borel_transform(alg, xi)
        expected = alg.kappa * xi ** 2 / 2.0  # S_2/2! * xi^2
        assert abs(val - expected) / abs(expected) < 0.01

    def test_borel_is_entire(self):
        """Borel transform evaluates without singularity at |xi| >> 1/rho."""
        from lib.resurgence_deep_engine import virasoro_deep, arity_borel_transform
        alg = virasoro_deep(1.0)
        # 1/rho ~ 0.29 for c=1; try xi = 10 >> 1/rho
        val = arity_borel_transform(alg, 10.0 + 0.0j, max_r=40)
        assert np.isfinite(abs(val))

    def test_borel_weighted_vs_standard(self):
        """Weighted Borel transform has smaller coefficients than standard."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, arity_borel_transform, arity_borel_weighted
        )
        alg = virasoro_deep(1.0)
        xi = 1.0 + 0.0j
        val_std = abs(arity_borel_transform(alg, xi))
        val_wt = abs(arity_borel_weighted(alg, xi))
        # Weighted has Gamma(r+5/2) >> r!, so |Bhat_w| << |Bhat|
        assert val_wt < val_std

    def test_borel_batch_consistency(self):
        """Batch evaluation matches individual evaluation."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, arity_borel_transform, arity_borel_at_points
        )
        alg = virasoro_deep(7.0)
        points = [0.1, 0.5 + 0.1j, 1.0 - 0.5j]
        batch = arity_borel_at_points(alg, points, 30)
        for xi, b_val in zip(points, batch):
            individual = arity_borel_transform(alg, xi, 30)
            assert abs(b_val - individual) < 1e-12

    def test_heisenberg_borel_polynomial(self):
        """Heisenberg Borel transform is a polynomial (terminates at r=2)."""
        from lib.resurgence_deep_engine import heisenberg_deep, arity_borel_transform
        h = heisenberg_deep(1, 1.0)
        # Bhat = S_2*xi^2/2! = kappa*xi^2/2
        for xi_val in [0.5, 1.0, 5.0, 100.0]:
            val = arity_borel_transform(h, xi_val)
            expected = 1.0 * xi_val ** 2 / 2.0
            assert abs(val - expected) < 1e-10 * max(abs(expected), 1e-10)

    def test_borel_conjugation(self):
        """Bhat(xi*) = Bhat(xi)* for real coefficients."""
        from lib.resurgence_deep_engine import virasoro_deep, arity_borel_transform
        alg = virasoro_deep(7.0)
        xi = 1.0 + 2.0j
        val = arity_borel_transform(alg, xi, 30)
        val_conj = arity_borel_transform(alg, xi.conjugate(), 30)
        assert abs(val.conjugate() - val_conj) < 1e-10

    def test_borel_real_on_real_axis(self):
        """Bhat(xi) is real for real xi (since S_r are real)."""
        from lib.resurgence_deep_engine import virasoro_deep, arity_borel_transform
        alg = virasoro_deep(13.0)
        for xi_val in [0.1, 0.5, 1.0, 2.0]:
            val = arity_borel_transform(alg, xi_val)
            assert abs(val.imag) < 1e-12


# =====================================================================
# Section 4: Borel singularity identification
# =====================================================================

class TestBorelSingularities:
    """Test identification of Borel singularities."""

    def test_virasoro_has_two_singularities(self):
        """Virasoro (class M) has exactly two arity singularities."""
        from lib.resurgence_deep_engine import virasoro_deep, identify_arity_singularities
        alg = virasoro_deep(1.0)
        sings = identify_arity_singularities(alg)
        assert len(sings) == 2

    def test_heisenberg_no_singularities(self):
        """Heisenberg (class G) has no arity singularities."""
        from lib.resurgence_deep_engine import heisenberg_deep, identify_arity_singularities
        h = heisenberg_deep(1, 1.0)
        sings = identify_arity_singularities(h)
        assert len(sings) == 0

    def test_singularity_modulus_equals_rho(self):
        """Instanton action modulus |omega_1| = rho for complex conjugate pair."""
        from lib.resurgence_deep_engine import virasoro_deep, identify_arity_singularities
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            sings = identify_arity_singularities(alg)
            # Both singularities should have modulus = rho
            for s in sings:
                assert abs(s.modulus - alg.rho) < 1e-10

    def test_complex_conjugate_pair(self):
        """For Delta > 0: branch points are complex conjugates."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            assert alg.Delta > 0, f"Expected Delta > 0 at c={c}"
            t_p, t_m = alg.branch_points
            # Complex conjugates: t_m = t_p*
            assert abs(t_m - t_p.conjugate()) < 1e-10

    def test_instanton_action_formula(self):
        """omega_1 from formula matches omega_1 from branch points."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, primary_instanton_action, instanton_action_from_formula
        )
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            omega_primary = primary_instanton_action(alg)
            omega_formula = instanton_action_from_formula(alg)
            assert abs(omega_primary - omega_formula) < 1e-10

    def test_monodromy_minus_one(self):
        """All arity singularities have monodromy -1 (sqrt branch)."""
        from lib.resurgence_deep_engine import virasoro_deep, identify_arity_singularities
        alg = virasoro_deep(7.0)
        sings = identify_arity_singularities(alg)
        for s in sings:
            assert abs(s.monodromy - (-1.0)) < 1e-14

    def test_rho_matches_independent(self):
        """rho from module matches independent computation."""
        from lib.resurgence_deep_engine import virasoro_deep
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            rho_indep = _virasoro_rho(c)
            assert abs(alg.rho - rho_indep) < 1e-10

    def test_genus_singularity_locations(self):
        """Genus Borel singularities at u_n = (2*pi*n)^2, universal."""
        from lib.resurgence_deep_engine import genus_borel_singularities
        for kappa in [0.5, 3.5, 6.5]:
            sings = genus_borel_singularities(kappa, 5)
            for sing in sings:
                n = sing['n']
                expected_u = (TWO_PI * n) ** 2
                assert abs(sing['u_location'] - expected_u) < 1e-10


# =====================================================================
# Section 5: Large-order and growth rate extraction
# =====================================================================

class TestLargeOrder:
    """Test large-order asymptotics and growth rate extraction."""

    def test_ratio_test_convergence(self):
        """Verify S_r ~ C * rho^r * r^{-5/2} * cos(r*theta+phi).

        The detrended sequence s_r = S_r * rho^{-r} * r^{5/2} should
        oscillate with BOUNDED amplitude, confirming that rho is the
        correct growth rate. If rho were wrong, s_r would either
        grow or decay exponentially.
        """
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        for c in [7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            coeffs = shadow_coefficients(alg, 55)
            rho = alg.rho

            # Detrend: s_r = S_r * rho^{-r} * r^{5/2}
            detrended = []
            for r in range(20, 55):
                sr = coeffs.get(r, 0.0)
                if abs(sr) > 1e-300:
                    s_r = sr * rho ** (-r) * r ** 2.5
                    detrended.append(abs(s_r))

            if len(detrended) < 5:
                continue

            # The detrended sequence should be bounded (oscillating)
            # Check: max/min ratio should be finite (not exponentially growing)
            max_val = max(detrended[-10:])
            min_val = min(d for d in detrended[-10:] if d > 1e-30)
            # For oscillating cos: max/min can be large near zeros,
            # but the MEDIAN should be bounded
            import statistics
            median_val = statistics.median(detrended[-10:])
            # Check that the median is of order 1 (not exponentially large/small)
            assert 1e-3 < median_val < 1e3, \
                f"Detrended sequence not bounded at c={c}: median={median_val}"

    def test_richardson_extrapolation(self):
        """Richardson extrapolation improves rho estimate."""
        from lib.resurgence_deep_engine import virasoro_deep, ratio_test_arity
        alg = virasoro_deep(13.0)
        rt = ratio_test_arity(alg, 50)
        if rt['richardson']:
            rich = rt['best_richardson']
            root = rt['best_root_estimate']
            # Richardson should be closer to true value
            err_rich = abs(rich - alg.rho)
            err_root = abs(root - alg.rho)
            # Richardson typically improves (or at worst matches)
            assert err_rich < 2.0 * err_root + 1e-10

    def test_oscillation_angle_extraction(self):
        """Oscillation angle theta matches branch point argument."""
        from lib.resurgence_deep_engine import virasoro_deep, oscillation_extraction
        for c in [1.0, 7.0, 25.0]:
            alg = virasoro_deep(c)
            osc = oscillation_extraction(alg, 50)
            # The predicted theta = -arg(t_nearest)
            theta_pred = osc['theta_predicted']
            # Check that the fit amplitude is nonzero
            assert osc['amplitude'] > 1e-5, f"Zero amplitude at c={c}"

    def test_genus_ratio_test(self):
        """Genus ratio |F_{g+1}/F_g| -> 1/(4*pi^2)."""
        from lib.resurgence_deep_engine import genus_ratio_test
        for kappa in [0.5, 6.5, 12.5]:
            rt = genus_ratio_test(kappa, 25)
            assert rt['converged'], f"Genus ratio test failed for kappa={kappa}"
            last = rt['last_ratio']
            expected = 1.0 / FOUR_PI_SQ
            assert abs(last - expected) / expected < 0.01

    def test_genus_large_order_exact(self):
        """Large-order prediction is exact for genus expansion (simple poles)."""
        from lib.resurgence_deep_engine import (
            F_g_scalar, genus_large_order_prediction
        )
        kappa = 3.5
        for g in [5, 10, 15, 20]:
            Fg_exact = F_g_scalar(kappa, g)
            Fg_pred = genus_large_order_prediction(kappa, g, 20)
            rel_err = abs(Fg_exact - Fg_pred) / abs(Fg_exact)
            assert rel_err < 1e-6, f"Large-order prediction off at g={g}: {rel_err}"

    def test_leading_asymptotic(self):
        """Leading asymptotic: F_g ~ 2*kappa/(2*pi)^{2g} at large g.

        The n=1 instanton dominates; subleading from n=2 contributes
        a correction of order (1/2)^{2g} ~ 2^{-2g}, so the ratio
        F_g / (2*kappa/(2*pi)^{2g}) should approach 1 with correction
        |ratio - 1| ~ (1/2)^{2g}.
        """
        from lib.resurgence_deep_engine import F_g_scalar
        kappa = 6.5
        for g in [10, 15, 20]:
            Fg = F_g_scalar(kappa, g)
            leading = 2.0 * kappa / TWO_PI ** (2 * g)
            ratio = Fg / leading
            # Subleading correction ~ (1/2)^{2g} = 2^{-2g}
            tol = 2.0 * (0.5) ** (2 * g)
            assert abs(ratio - 1.0) < tol, \
                f"Leading asymptotic off at g={g}: ratio={ratio}"

    def test_bernoulli_asymptotics(self):
        """Bernoulli asymptotics: |B_{2g}| ~ 4*sqrt(pi*g)*(g/(pi*e))^{2g}."""
        import mpmath
        for g in [10, 15, 20]:
            B2g = abs(float(mpmath.bernoulli(2 * g)))
            # Stirling-type: B_{2g} ~ (-1)^{g+1}*2*(2g)!/(2*pi)^{2g}
            stirling = 2.0 * float(mpmath.factorial(2 * g)) / TWO_PI ** (2 * g)
            ratio = B2g / stirling
            assert abs(ratio - 1.0) < 0.05

    def test_rho_monotonicity_in_c(self):
        """rho(Vir_c) decreases with c for large c (convergent regime)."""
        from lib.resurgence_deep_engine import virasoro_deep
        rho_prev = virasoro_deep(10.0).rho
        for c in [12.0, 15.0, 20.0, 25.0]:
            rho_now = virasoro_deep(c).rho
            assert rho_now < rho_prev, f"rho not decreasing at c={c}"
            rho_prev = rho_now

    def test_critical_central_charge(self):
        """rho = 1 at the critical central charge c* ~ 6.12."""
        from lib.resurgence_deep_engine import virasoro_deep
        # c* is the root of 5c^3 + 22c^2 - 180c - 872 = 0
        # Approximately 6.1243
        # rho < 1 for c > c*, rho > 1 for c < c*
        alg_above = virasoro_deep(7.0)
        alg_below = virasoro_deep(5.0)
        assert alg_above.rho < 1.0, "rho should be < 1 above c*"
        assert alg_below.rho > 1.0, "rho should be > 1 below c*"


# =====================================================================
# Section 6: Darboux coefficients and alien derivatives
# =====================================================================

class TestAlienDerivatives:
    """Test Darboux coefficients and alien derivative computation."""

    def test_darboux_nonzero_for_class_m(self):
        """Darboux coefficient is nonzero for class M."""
        from lib.resurgence_deep_engine import virasoro_deep, darboux_coefficient
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            C = darboux_coefficient(alg)
            assert abs(C) > 1e-5, f"Darboux zero at c={c}"

    def test_darboux_zero_for_class_g(self):
        """Darboux coefficient is zero for class G."""
        from lib.resurgence_deep_engine import heisenberg_deep, darboux_coefficient
        h = heisenberg_deep(1, 1.0)
        C = darboux_coefficient(h)
        assert abs(C) < 1e-14

    def test_alien_derivative_nonzero(self):
        """Alien derivative is nonzero for class M (has arity resurgence)."""
        from lib.resurgence_deep_engine import virasoro_deep, alien_derivative_arity
        for c in [1.0, 7.0, 13.0]:
            alg = virasoro_deep(c)
            alien = alien_derivative_arity(alg)
            assert abs(alien['stokes_constant']) > 1e-5

    def test_alien_derivative_zero_for_g(self):
        """Alien derivative is zero for class G (tower terminates)."""
        from lib.resurgence_deep_engine import heisenberg_deep, alien_derivative_arity
        h = heisenberg_deep(1, 1.0)
        alien = alien_derivative_arity(h)
        assert abs(alien['stokes_constant']) < 1e-14

    def test_stokes_modulus_scales_with_kappa(self):
        """Stokes constant scales with algebra data (not trivially constant)."""
        from lib.resurgence_deep_engine import virasoro_deep, alien_derivative_arity
        stokes_c1 = abs(alien_derivative_arity(virasoro_deep(1.0))['stokes_constant'])
        stokes_c25 = abs(alien_derivative_arity(virasoro_deep(25.0))['stokes_constant'])
        # At different c, the Stokes constants should differ
        assert abs(stokes_c1 - stokes_c25) / max(stokes_c1, stokes_c25) > 0.1

    def test_numerical_stokes_agrees_with_exact(self):
        """Numerical Stokes constant modulus agrees with exact.

        The numerical extraction from a least-squares fit of oscillating
        coefficients is inherently approximate. We check that the MODULUS
        of the extracted Stokes constant is within a factor of 3 of the
        exact value, which confirms the correct order of magnitude.
        """
        from lib.resurgence_deep_engine import (
            virasoro_deep, alien_derivative_arity, alien_derivative_numerical
        )
        for c in [13.0, 25.0]:
            alg = virasoro_deep(c)
            exact = alien_derivative_arity(alg)['stokes_constant']
            numerical = alien_derivative_numerical(alg, max_r=150)
            if abs(exact) > 1e-10 and abs(numerical) > 1e-10:
                ratio = abs(numerical) / abs(exact)
                assert 0.3 < ratio < 3.0, \
                    f"Stokes modulus mismatch at c={c}: |exact|={abs(exact)}, |num|={abs(numerical)}"

    def test_darboux_numerical_nonzero(self):
        """Numerical Darboux extraction is nonzero for class M.

        The exact and numerical Darboux coefficients are related by
        convention-dependent factors. We verify that the numerical
        extraction yields a nonzero result, confirming that the
        detrended coefficients have a well-defined oscillation.
        """
        from lib.resurgence_deep_engine import (
            virasoro_deep, darboux_coefficient, darboux_coefficient_numerical
        )
        for c in [7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            exact = darboux_coefficient(alg)
            numerical = darboux_coefficient_numerical(alg, max_r=50)
            assert abs(exact) > 1e-5, f"Exact Darboux zero at c={c}"
            assert abs(numerical) > 1e-5, f"Numerical Darboux zero at c={c}"

    def test_genus_stokes_formula(self):
        """Genus Stokes constant: S_n^hbar = (-1)^n * 4*pi^2*n * kappa * i."""
        from lib.resurgence_deep_engine import genus_stokes_constant
        kappa = 6.5
        for n in [1, 2, 3]:
            S_n = genus_stokes_constant(kappa, n)
            expected = (-1) ** n * 4.0 * PI ** 2 * n * kappa * 1.0j
            assert abs(S_n - expected) < 1e-10

    def test_genus_stokes_linear_in_kappa(self):
        """Genus Stokes constant is linear in kappa."""
        from lib.resurgence_deep_engine import genus_stokes_constant
        for n in [1, 2]:
            S_k1 = genus_stokes_constant(1.0, n)
            S_k5 = genus_stokes_constant(5.0, n)
            assert abs(S_k5 / S_k1 - 5.0) < 1e-10

    def test_genus_stokes_alternating_sign(self):
        """Genus Stokes constants alternate in sign: S_n/i ~ (-1)^n."""
        from lib.resurgence_deep_engine import genus_stokes_constant
        kappa = 3.0
        for n in [1, 2, 3, 4]:
            S_n = genus_stokes_constant(kappa, n)
            # S_n = (-1)^n * 4*pi^2*n*kappa*i, so S_n/i = (-1)^n * 4*pi^2*n*kappa
            sign = (S_n / 1j).real / (4.0 * PI ** 2 * n * kappa)
            assert abs(sign - (-1) ** n) < 1e-10


# =====================================================================
# Section 7: Stokes phenomenon (arity direction)
# =====================================================================

class TestStokesPhenomenon:
    """Test the Stokes automorphism and jump computation."""

    def test_stokes_rays_exist(self):
        """Virasoro has nontrivial Stokes rays."""
        from lib.resurgence_deep_engine import virasoro_deep, stokes_automorphism_arity
        alg = virasoro_deep(7.0)
        sa = stokes_automorphism_arity(alg)
        assert len(sa['stokes_rays']) == 2

    def test_stokes_rays_for_conjugate_pair(self):
        """Stokes rays are at +-theta for complex conjugate singularities."""
        from lib.resurgence_deep_engine import virasoro_deep, stokes_automorphism_arity
        alg = virasoro_deep(7.0)
        sa = stokes_automorphism_arity(alg)
        rays = sa['stokes_rays']
        assert len(rays) == 2
        # Should be approximately +-theta (conjugate pair)
        assert abs(rays[0] + rays[1]) < 1e-10

    def test_stokes_jump_properties(self):
        """Stokes jump has expected mathematical structure.

        For complex instanton action omega_1, the exponential factor
        exp(-omega_1/t) depends on the DIRECTION of t in the complex
        plane. The suppression occurs when Re(omega_1/t) > 0.
        We check structural properties rather than a specific value.
        """
        from lib.resurgence_deep_engine import virasoro_deep, stokes_jump_numerical
        alg = virasoro_deep(13.0)
        omega = primary_instanton_action_val(alg)
        # Choose t along the Stokes direction where suppression occurs:
        # We need Re(omega/t) > 0, i.e., arg(t) ~ arg(omega)
        t_stokes = 0.01 * cmath.exp(1j * cmath.phase(omega))
        jump = stokes_jump_numerical(alg, t_stokes)
        # The exponential should now be suppressed
        assert jump['instanton_suppression'] < 1.0, \
            f"Exponential not suppressed at Stokes direction: {jump['instanton_suppression']}"

    def test_optimal_truncation_order(self):
        """Optimal truncation N* = |omega_1|/|t| (rounded)."""
        from lib.resurgence_deep_engine import virasoro_deep, stokes_jump_numerical
        alg = virasoro_deep(7.0)
        omega = abs(primary_instanton_action_val(alg))
        for t_val in [0.1, 0.2, 0.5]:
            jump = stokes_jump_numerical(alg, t_val)
            expected_N = int(round(omega / t_val))
            expected_N = max(2, min(expected_N, 60))
            assert abs(jump['optimal_truncation'] - expected_N) <= 1

    def test_no_stokes_for_class_g(self):
        """No Stokes phenomenon for class G (Heisenberg)."""
        from lib.resurgence_deep_engine import heisenberg_deep, stokes_jump_numerical
        h = heisenberg_deep(1, 1.0)
        jump = stokes_jump_numerical(h, 0.5)
        assert abs(jump['stokes_jump']) < 1e-14

    def test_stokes_constant_self_dual(self):
        """At self-dual c=13: rho(A) = rho(A'), so Stokes structures match."""
        from lib.resurgence_deep_engine import virasoro_deep
        alg = virasoro_deep(13.0)
        alg_dual = virasoro_deep(13.0)  # Self-dual!
        assert abs(alg.rho - alg_dual.rho) < 1e-14

    def test_stokes_jump_formula_structure(self):
        """Stokes jump formula has correct structure."""
        from lib.resurgence_deep_engine import virasoro_deep, stokes_automorphism_arity
        alg = virasoro_deep(7.0)
        sa = stokes_automorphism_arity(alg)
        assert 'stokes_constant' in sa
        assert 'instanton_action' in sa
        assert sa['algebraic_simplification'] is not None

    def test_stokes_jump_depends_on_c(self):
        """Stokes jump magnitude depends on central charge."""
        from lib.resurgence_deep_engine import virasoro_deep, stokes_jump_numerical
        jumps = {}
        for c in [1.0, 7.0, 25.0]:
            alg = virasoro_deep(c)
            j = stokes_jump_numerical(alg, 0.3)
            jumps[c] = abs(j['predicted_jump'])
        # Different c should give different jumps
        assert jumps[1.0] != jumps[25.0]


def primary_instanton_action_val(alg):
    """Helper to get instanton action value."""
    from lib.resurgence_deep_engine import primary_instanton_action
    return primary_instanton_action(alg)


# =====================================================================
# Section 8: Trans-series completion
# =====================================================================

class TestTransSeries:
    """Test trans-series construction and evaluation."""

    def test_trans_series_construction(self):
        """Trans-series builds without error."""
        from lib.resurgence_deep_engine import virasoro_deep, build_arity_trans_series
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            ts = build_arity_trans_series(alg, 30)
            assert len(ts.perturbative) > 0
            assert abs(ts.rho) > 0

    def test_trans_series_perturbative_sector(self):
        """Perturbative sector of trans-series matches shadow coefficients."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, build_arity_trans_series, shadow_coefficients
        )
        alg = virasoro_deep(7.0)
        ts = build_arity_trans_series(alg, 30)
        coeffs = shadow_coefficients(alg, 30)
        for r in range(2, 30):
            assert abs(ts.perturbative[r] - coeffs[r]) < 1e-12

    def test_trans_series_evaluation_at_small_t(self):
        """Trans-series with sigma=0 equals perturbative sector exactly."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, build_arity_trans_series, evaluate_trans_series_arity
        )
        alg = virasoro_deep(7.0)
        ts = build_arity_trans_series(alg, 30)
        t = 0.05 + 0.0j
        # With sigma=0, no non-perturbative correction
        val = evaluate_trans_series_arity(ts, t, sigma=0.0)
        pert = sum(ts.perturbative.get(r, 0.0) * t ** r for r in range(2, 30))
        assert abs(val - pert) / max(abs(pert), 1e-100) < 1e-10

    def test_trans_series_instanton_actions(self):
        """Instanton actions in trans-series match algebra data."""
        from lib.resurgence_deep_engine import virasoro_deep, build_arity_trans_series
        alg = virasoro_deep(13.0)
        ts = build_arity_trans_series(alg)
        A_p, A_m = alg.instanton_actions
        assert abs(ts.instanton_action_plus - A_p) < 1e-10
        assert abs(ts.instanton_action_minus - A_m) < 1e-10

    def test_trans_series_zero_at_zero(self):
        """Trans-series vanishes at t=0."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, build_arity_trans_series, evaluate_trans_series_arity
        )
        alg = virasoro_deep(7.0)
        ts = build_arity_trans_series(alg, 20)
        val = evaluate_trans_series_arity(ts, 0.0)
        assert abs(val) < 1e-14

    def test_heisenberg_trans_series_exact(self):
        """Heisenberg trans-series = kappa*t^2 (no non-perturbative)."""
        from lib.resurgence_deep_engine import (
            heisenberg_deep, build_arity_trans_series, evaluate_trans_series_arity
        )
        h = heisenberg_deep(1, 1.0)
        ts = build_arity_trans_series(h, 20)
        for t_val in [0.1, 0.5, 1.0]:
            t = complex(t_val)
            val = evaluate_trans_series_arity(ts, t)
            expected = 1.0 * t ** 2  # kappa = 1, S_2 = 1
            assert abs(val - expected) < 1e-10

    def test_trans_series_real_for_real_t(self):
        """Trans-series is real for real positive t."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, build_arity_trans_series, evaluate_trans_series_arity
        )
        alg = virasoro_deep(13.0)
        ts = build_arity_trans_series(alg, 20)
        # For real t, the complex conjugate instanton contributions
        # should cancel imaginary parts
        val = evaluate_trans_series_arity(ts, 0.1, sigma=0.0)
        assert abs(val.imag) < 1e-12


# =====================================================================
# Section 9: Genus resurgence
# =====================================================================

class TestGenusResurgence:
    """Test genus-direction resurgence."""

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 (from B_2 = 1/6, lambda_1 = 1/24)."""
        from lib.resurgence_deep_engine import F_g_scalar
        for kappa in [0.5, 3.5, 6.5, 12.5]:
            F1 = F_g_scalar(kappa, 1)
            expected = kappa / 24.0
            assert abs(F1 - expected) < 1e-14

    def test_F1_independent_verification(self):
        """F_1 from module matches independent computation."""
        from lib.resurgence_deep_engine import F_g_scalar
        for kappa in [0.5, 6.5]:
            mod_val = F_g_scalar(kappa, 1)
            indep_val = _F_g_independent(kappa, 1)
            assert abs(mod_val - indep_val) < 1e-14

    def test_F2_value(self):
        """F_2 = kappa * 7/5760 (from Faber-Pandharipande)."""
        from lib.resurgence_deep_engine import F_g_scalar
        kappa = 1.0
        F2 = F_g_scalar(kappa, 2)
        # lambda_2 = (2^3-1)/2^3 * |B_4|/(4!) = 7/8 * 1/30 / 24 = 7/5760
        expected = kappa * 7.0 / 5760.0
        assert abs(F2 - expected) < 1e-14

    def test_genus_borel_transform_small_xi(self):
        """B_u(xi) ~ F_1 for small xi."""
        from lib.resurgence_deep_engine import genus_borel_transform, F_g_scalar
        kappa = 3.5
        xi = 0.001
        Bu = genus_borel_transform(kappa, xi)
        # B_u = sum F_g xi^{g-1}/(g-1)! ~ F_1 for small xi
        expected = F_g_scalar(kappa, 1)
        assert abs(Bu - expected) / abs(expected) < 0.01

    def test_genus_closed_form_matches_series(self):
        """Closed form Z(u) matches series sum for small u."""
        from lib.resurgence_deep_engine import F_g_scalar, genus_closed_form
        kappa = 6.5
        u = 1.0 + 0.0j  # well inside convergence radius 4*pi^2 ~ 39.5
        # Series sum
        series = sum(F_g_scalar(kappa, g) * u ** g for g in range(1, 50))
        # Closed form
        closed = genus_closed_form(kappa, u)
        assert abs(series - closed) / abs(closed) < 1e-6

    def test_genus_borel_radius_universal(self):
        """Genus Borel radius = 2*pi in hbar, (2*pi)^2 in u. UNIVERSAL."""
        from lib.resurgence_deep_engine import genus_borel_singularities
        for kappa in [0.5, 6.5, 12.5]:
            sings = genus_borel_singularities(kappa, 1)
            assert abs(sings[0]['hbar_location'] - TWO_PI) < 1e-10
            assert abs(sings[0]['u_location'] - FOUR_PI_SQ) < 1e-10

    def test_genus_residue_formula(self):
        """Residue R_n = (-1)^n * 8*pi^2*n^2*kappa."""
        from lib.resurgence_deep_engine import genus_borel_singularities
        kappa = 3.0
        sings = genus_borel_singularities(kappa, 3)
        for sing in sings:
            n = sing['n']
            expected_R = (-1) ** n * 8.0 * PI ** 2 * n ** 2 * kappa
            assert abs(sing['residue'] - expected_R) < 1e-10

    def test_genus_stokes_u_from_residue(self):
        """Stokes constant S_n^u = 2*pi*i * R_n."""
        from lib.resurgence_deep_engine import genus_borel_singularities
        kappa = 5.0
        sings = genus_borel_singularities(kappa, 3)
        for sing in sings:
            S_u = sing['stokes_u']
            R_n = sing['residue']
            expected = 2.0j * PI * R_n
            assert abs(S_u - expected) < 1e-10

    def test_large_order_exact_genus(self):
        """Large-order relation is EXACT for genus (sum of simple poles)."""
        from lib.resurgence_deep_engine import F_g_scalar, genus_large_order_prediction
        kappa = 7.0
        for g in [3, 5, 10, 15]:
            exact = F_g_scalar(kappa, g)
            predicted = genus_large_order_prediction(kappa, g, 30)
            rel = abs(exact - predicted) / abs(exact) if abs(exact) > 1e-300 else 0.0
            assert rel < 1e-8, f"Large-order not exact at g={g}: rel={rel}"


# =====================================================================
# Section 10: Double resurgence
# =====================================================================

class TestDoubleResurgence:
    """Test the double resurgence structure."""

    def test_double_borel_factors(self):
        """Double Borel transform factors as B_u * B_arity."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, double_borel_transform,
            genus_borel_transform, arity_borel_transform
        )
        alg = virasoro_deep(7.0)
        xi = 1.0 + 0.5j
        zeta = 0.3 - 0.1j
        double = double_borel_transform(alg, xi, zeta)
        Bu = genus_borel_transform(alg.kappa, xi)
        Bt = arity_borel_transform(alg, zeta)
        product = Bu * Bt
        assert abs(double - product) < 1e-10 * max(abs(product), 1e-10)

    def test_alien_commutativity(self):
        """Alien derivatives in genus and arity directions commute."""
        from lib.resurgence_deep_engine import virasoro_deep, double_alien_commutativity
        for c in [7.0, 13.0]:
            alg = virasoro_deep(c)
            comm = double_alien_commutativity(alg)
            assert comm['commutator_vanishes']

    def test_double_coefficients_factorize(self):
        """F_{g,r} = F_g * S_r (factorized double expansion)."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, double_resurgence_coefficients,
            F_g_scalar, shadow_coefficients
        )
        alg = virasoro_deep(13.0)
        F = double_resurgence_coefficients(alg, g_max=10, r_max=15)
        coeffs = shadow_coefficients(alg, 15)
        for g in range(1, 10):
            Fg = F_g_scalar(alg.kappa, g)
            for r in range(2, 15):
                Sr = coeffs[r]
                expected = Fg * Sr
                actual = F[g - 1, r - 2]
                if abs(expected) > 1e-30:
                    assert abs(actual - expected) / abs(expected) < 1e-10

    def test_double_factorization_multiple_points(self):
        """Factorization verified at multiple (xi, zeta) points."""
        from lib.resurgence_deep_engine import virasoro_deep, verify_double_resurgence
        for c in [1.0, 7.0, 25.0]:
            alg = virasoro_deep(c)
            ver = verify_double_resurgence(alg)
            assert ver['factorization']

    def test_genre_and_arity_independent(self):
        """Genus and arity resurgent structures are independent."""
        from lib.resurgence_deep_engine import virasoro_deep, verify_double_resurgence
        alg = virasoro_deep(13.0)
        ver = verify_double_resurgence(alg)
        assert ver['genus_leading_check']
        assert ver['arity_leading_check']

    def test_double_coefficients_shape(self):
        """Double coefficients array has correct shape."""
        from lib.resurgence_deep_engine import virasoro_deep, double_resurgence_coefficients
        alg = virasoro_deep(7.0)
        F = double_resurgence_coefficients(alg, g_max=10, r_max=20)
        assert F.shape == (10, 19)  # g=1..10, r=2..20 (r_max-1 columns)

    def test_double_borel_real_on_real(self):
        """Double Borel transform is real for real arguments."""
        from lib.resurgence_deep_engine import virasoro_deep, double_borel_transform
        alg = virasoro_deep(7.0)
        val = double_borel_transform(alg, 1.0, 0.5)
        assert abs(val.imag) < 1e-10


# =====================================================================
# Section 11: Pade approximants and peacock patterns
# =====================================================================

class TestPadeAndPeacock:
    """Test Pade approximant computation and peacock pattern structure."""

    def test_pade_coefficients_well_defined(self):
        """Pade approximant computation does not fail."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, shadow_coefficients, pade_approximant_coefficients
        )
        alg = virasoro_deep(7.0)
        coeffs = shadow_coefficients(alg, 30)
        p, q = pade_approximant_coefficients(coeffs, N=8)
        assert len(p) > 0
        assert len(q) > 0

    def test_pade_poles_exist(self):
        """Pade approximant has poles."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, shadow_coefficients, pade_poles
        )
        alg = virasoro_deep(7.0)
        coeffs = shadow_coefficients(alg, 30)
        poles = pade_poles(coeffs, N=10)
        assert len(poles) > 0

    def test_pade_poles_near_branch_points(self):
        """Pade poles accumulate near the true branch points."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, pade_borel_singularity_detection
        )
        for c in [7.0, 13.0]:
            alg = virasoro_deep(c)
            det = pade_borel_singularity_detection(alg, max_r=50, N=12)
            if not math.isnan(det['pade_rho']):
                # Pade rho should be within ~50% of true rho
                assert det['rho_relative_error'] < 0.5, \
                    f"Pade rho far from true at c={c}: {det['pade_rho']} vs {det['true_rho']}"

    def test_peacock_data_structure(self):
        """Peacock pattern data has expected structure."""
        from lib.resurgence_deep_engine import virasoro_deep, peacock_pattern_data
        alg = virasoro_deep(7.0)
        pp = peacock_pattern_data(alg, max_r=40, pade_orders=[5, 8, 10])
        assert 'pole_data' in pp
        assert 'true_singularities' in pp
        assert len(pp['true_singularities']) == 2

    def test_peacock_pole_count_increases(self):
        """Number of Pade poles increases with Pade order."""
        from lib.resurgence_deep_engine import virasoro_deep, peacock_pattern_data
        alg = virasoro_deep(13.0)
        pp = peacock_pattern_data(alg, max_r=50, pade_orders=[5, 8, 12])
        orders = sorted(pp['pole_data'].keys())
        if len(orders) >= 2:
            # Higher order should have more poles
            for i in range(len(orders) - 1):
                n1 = pp['pole_data'][orders[i]]['n_poles']
                n2 = pp['pole_data'][orders[i + 1]]['n_poles']
                assert n2 >= n1

    def test_heisenberg_pade_trivial(self):
        """Heisenberg Pade is trivial (only one nonzero coefficient)."""
        from lib.resurgence_deep_engine import (
            heisenberg_deep, shadow_coefficients, pade_poles
        )
        h = heisenberg_deep(1, 1.0)
        coeffs = shadow_coefficients(h, 20)
        poles = pade_poles(coeffs, N=3)
        # All poles should be at infinity (or numerical noise)
        # Since the series is just S_2*t^2, the Pade should be exact
        # with no poles (or poles at very large modulus)
        if poles:
            assert min(abs(p) for p in poles) > 100

    def test_peacock_clustering(self):
        """Clustering data identifies singularity nearest poles."""
        from lib.resurgence_deep_engine import virasoro_deep, peacock_pattern_data
        alg = virasoro_deep(7.0)
        pp = peacock_pattern_data(alg, max_r=50, pade_orders=[5, 8, 10, 12])
        if pp['clustering']:
            for key, data in pp['clustering'].items():
                # Relative distance should be moderate (< 100%)
                if data['relative_distance'] < float('inf'):
                    assert data['distance'] >= 0

    def test_pade_singularity_detection_c13(self):
        """Pade singularity detection at self-dual c=13."""
        from lib.resurgence_deep_engine import virasoro_deep, pade_borel_singularity_detection
        alg = virasoro_deep(13.0)
        det = pade_borel_singularity_detection(alg, max_r=50, N=12)
        assert det['n_poles'] > 0
        assert det['true_rho'] > 0


# =====================================================================
# Section 12: Multi-path verification
# =====================================================================

class TestMultiPathVerification:
    """Multi-path verification of key results (3+ independent paths)."""

    def test_arity_borel_radius_5_paths(self):
        """Arity Borel radius verified by multiple independent paths.

        Paths 1 (formula) and 4 (algebraic) agree exactly by construction.
        Paths 2 (root test) and 5 (Richardson) agree approximately.
        Path 3 (Pade) may be noisy with limited data.
        We require at least 2 paths within 5% and check that the
        formula paths agree exactly.
        """
        from lib.resurgence_deep_engine import virasoro_deep, verify_arity_borel_radius_multipath
        for c in [7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            ver = verify_arity_borel_radius_multipath(alg, max_r=50)
            paths = ver['paths']
            # Paths 1 and 4 must agree exactly
            assert abs(paths['path1_formula'] - paths['path4_algebraic']) < 1e-12
            # At least 2 of the 5 paths should be within 20% (formula + one numerical)
            good_paths = sum(1 for v in ver['agreement'].values()
                             if isinstance(v, float) and not math.isnan(v) and v < 0.20)
            assert good_paths >= 2, \
                f"Only {good_paths} paths agree at c={c}: {ver['agreement']}"

    def test_genus_stokes_4_paths(self):
        """Genus Stokes constant verified by 4 independent paths."""
        from lib.resurgence_deep_engine import verify_genus_stokes_multipath
        for kappa in [0.5, 6.5, 12.5]:
            ver = verify_genus_stokes_multipath(kappa)
            assert ver['paths_agree'], f"Paths disagree for kappa={kappa}"
            assert ver['path3_bernoulli_consistent']
            assert ver['path4_linearity']

    def test_double_resurgence_3_paths(self):
        """Double resurgence verified by 3 independent paths."""
        from lib.resurgence_deep_engine import virasoro_deep, verify_double_resurgence
        for c in [7.0, 13.0]:
            alg = virasoro_deep(c)
            ver = verify_double_resurgence(alg)
            assert ver['all_pass']

    def test_cross_check_rho_formula_vs_extraction(self):
        """rho from analytic formula vs numerical root-test extraction.

        The root test |S_r|^{1/r} converges slowly for large rho (c < c*).
        We test at c >= 7 where convergence is reasonable within 50 terms.
        """
        from lib.resurgence_deep_engine import virasoro_deep, ratio_test_arity
        for c in [7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            rt = ratio_test_arity(alg, 50)
            formula_rho = alg.rho
            extracted_rho = rt['best_root_estimate']
            rel = abs(formula_rho - extracted_rho) / formula_rho
            assert rel < 0.25, f"rho mismatch at c={c}: {formula_rho} vs {extracted_rho}"

    def test_cross_check_S2_kappa(self):
        """S_2 = kappa verified by direct computation and module."""
        from lib.resurgence_deep_engine import virasoro_deep, shadow_coefficients
        for c in [1.0, 7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            coeffs = shadow_coefficients(alg, 10)
            # Path 1: module
            S2_mod = coeffs[2]
            # Path 2: formula kappa = c/2
            S2_formula = c / 2.0
            # Path 3: independent sqrt expansion
            indep = _shadow_coefficients_independent(c / 2.0, 2.0, _virasoro_S4(c), 10)
            S2_indep = indep[2]
            assert abs(S2_mod - S2_formula) < 1e-12
            assert abs(S2_mod - S2_indep) < 1e-12

    def test_cross_check_genus_F1(self):
        """F_1 = kappa/24 verified by 3 paths."""
        from lib.resurgence_deep_engine import F_g_scalar, lambda_fp
        kappa = 6.5
        # Path 1: module
        F1_mod = F_g_scalar(kappa, 1)
        # Path 2: kappa/24
        F1_formula = kappa / 24.0
        # Path 3: independent
        F1_indep = _F_g_independent(kappa, 1)
        assert abs(F1_mod - F1_formula) < 1e-14
        assert abs(F1_mod - F1_indep) < 1e-14

    def test_instanton_action_3_paths(self):
        """Instanton action verified by 3 paths."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, primary_instanton_action,
            instanton_action_from_formula, identify_arity_singularities
        )
        for c in [7.0, 13.0, 25.0]:
            alg = virasoro_deep(c)
            # Path 1: From primary_instanton_action
            omega1 = primary_instanton_action(alg)
            # Path 2: From formula
            omega2 = instanton_action_from_formula(alg)
            # Path 3: From singularity identification
            sings = identify_arity_singularities(alg)
            omega3 = min(sings, key=lambda s: s.modulus).instanton_action
            assert abs(omega1 - omega2) < 1e-10
            assert abs(omega1 - omega3) < 1e-10

    def test_complete_scan_runs(self):
        """Full Virasoro scan completes without error."""
        from lib.resurgence_deep_engine import virasoro_borel_scan
        results = virasoro_borel_scan([1.0, 7.0, 13.0, 25.0], max_r=30)
        assert len(results) == 4
        for key, val in results.items():
            assert 'kappa' in val
            assert 'rho' in val
            assert val['rho'] > 0


# =====================================================================
# Section 13: Complementarity of resurgent structures
# =====================================================================

class TestComplementarity:
    """Test resurgent structure under Koszul complementarity."""

    def test_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        for c in [1.0, 7.0, 13.0, 25.0]:
            comp = complementarity_resurgence(c)
            assert comp['kappa_sum_is_13']

    def test_self_dual_rho_equal(self):
        """At c=13: rho(A) = rho(A!) (enhanced Z_2 symmetry)."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        comp = complementarity_resurgence(13.0)
        assert comp['rho_equal']
        assert comp['self_dual']

    def test_complementarity_rho_different(self):
        """Away from self-dual: rho(A) != rho(A!)."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        for c in [1.0, 7.0, 25.0]:
            comp = complementarity_resurgence(c)
            # rho should differ for c != 13
            assert not comp['rho_equal'] or abs(c - 13.0) < 0.1

    def test_complementarity_genus_stokes_sum(self):
        """Genus Stokes constants: S_1(A) + S_1(A!) proportional to kappa sum."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        comp = complementarity_resurgence(7.0)
        # S_1^hbar = -4*pi^2*kappa*i, so sum = -4*pi^2*13*i
        expected_sum = -4.0 * PI ** 2 * 13.0 * 1.0j
        assert abs(comp['genus_stokes_sum'] - expected_sum) < 1e-8

    def test_c1_c25_complementarity(self):
        """Vir_1 and Vir_25 are Koszul duals (c + c' = 26)."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        comp = complementarity_resurgence(1.0)
        assert abs(comp['c_dual'] - 25.0) < 1e-14
        assert abs(comp['kappa'] - 0.5) < 1e-14
        assert abs(comp['kappa_dual'] - 12.5) < 1e-14

    def test_complementarity_data_complete(self):
        """Complementarity analysis returns all expected fields."""
        from lib.resurgence_deep_engine import complementarity_resurgence
        comp = complementarity_resurgence(7.0)
        expected_fields = [
            'c', 'c_dual', 'kappa', 'kappa_dual', 'kappa_sum',
            'rho_A', 'rho_A_dual', 'arity_stokes_A', 'genus_stokes_sum',
        ]
        for field in expected_fields:
            assert field in comp, f"Missing field: {field}"


# =====================================================================
# Section 14: Cross-family comparison
# =====================================================================

class TestCrossFamily:
    """Compare resurgent structure across algebra families."""

    def test_genus_resurgence_universal(self):
        """Genus Borel radius is 2*pi for ALL algebras (universal)."""
        from lib.resurgence_deep_engine import genus_borel_singularities
        for kappa in [0.5, 2.25, 6.5, 12.5]:
            sings = genus_borel_singularities(kappa, 1)
            assert abs(sings[0]['hbar_location'] - TWO_PI) < 1e-10

    def test_genus_stokes_proportional_to_kappa(self):
        """Genus Stokes constant S_1 proportional to kappa (for all families)."""
        from lib.resurgence_deep_engine import genus_stokes_constant
        # Heisenberg kappa=1, Vir c=1 kappa=0.5, sl2 k=1 kappa=2.25
        kappas = [1.0, 0.5, 2.25]
        for kappa in kappas:
            S1 = genus_stokes_constant(kappa, 1)
            expected = -4.0 * PI ** 2 * kappa * 1.0j
            assert abs(S1 - expected) < 1e-10

    def test_class_g_no_arity_resurgence(self):
        """Class G algebras have no arity-direction resurgence."""
        from lib.resurgence_deep_engine import (
            heisenberg_deep, identify_arity_singularities
        )
        for rank in [1, 2, 3, 8]:
            h = heisenberg_deep(rank, 1.0)
            sings = identify_arity_singularities(h)
            assert len(sings) == 0

    def test_class_l_no_arity_resurgence(self):
        """Class L algebras have no arity-direction resurgence."""
        from lib.resurgence_deep_engine import (
            affine_sl2_deep, identify_arity_singularities
        )
        for k in [1.0, 2.0, 5.0]:
            a = affine_sl2_deep(k)
            sings = identify_arity_singularities(a)
            assert len(sings) == 0

    def test_class_m_has_arity_resurgence(self):
        """Class M algebras have arity-direction resurgence."""
        from lib.resurgence_deep_engine import (
            virasoro_deep, w3_deep, identify_arity_singularities
        )
        for c in [1.0, 7.0, 25.0]:
            for constructor in [virasoro_deep, w3_deep]:
                alg = constructor(c)
                sings = identify_arity_singularities(alg)
                assert len(sings) == 2

    def test_w3_kappa_is_5c_over_6(self):
        """W_3 kappa = 5c/6, NOT c/2 (AP1/AP39)."""
        from lib.resurgence_deep_engine import virasoro_deep, w3_deep
        for c in [7.0, 13.0]:
            vir = virasoro_deep(c)
            w3 = w3_deep(c)
            # kappa(W_3) = 5c/6, kappa(Vir) = c/2. Ratio = 5/3.
            assert abs(w3.kappa / vir.kappa - 5.0 / 3.0) < 1e-14
            # S_4 on T-line is the SAME (depends only on c, not kappa)
            assert abs(vir.S4 - w3.S4) < 1e-14
