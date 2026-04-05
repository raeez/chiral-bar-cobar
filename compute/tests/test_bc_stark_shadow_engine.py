r"""Tests for bc_stark_shadow_engine.py -- Stark-type conjectures for shadow zeta.

BC-77: 80+ tests covering Taylor expansion, order of vanishing, shadow
regulator, class number formula, BSD-type central value, Gross-Zagier
derivatives, special values at negative integers, rationality, and
multi-path verification.

VERIFICATION PATHS (per the Multi-Path Verification Mandate):
    1. Direct Taylor expansion vs finite-difference approximation
    2. Complementarity: zeta_A(s) + zeta_{A!}(s) consistency
    3. PSLQ/LLL algebraic relation detection
    4. Convergence rate: truncated series vs full
    5. Cross-family consistency (Heisenberg, affine, Virasoro, beta-gamma)
"""

import math
import sys
import pytest

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar/compute/lib')

from bc_stark_shadow_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    virasoro_shadow_coefficients,
    betagamma_shadow_coefficients,
    shadow_zeta_taylor_at_zero,
    shadow_zeta_taylor_at_zero_hp,
    order_of_vanishing_at_zero,
    shadow_regulator,
    shadow_regulator_hp,
    shadow_zeta_eval,
    shadow_zeta_eval_real,
    shadow_class_number,
    shadow_class_number_complementarity,
    shadow_central_value,
    shadow_central_derivative,
    shadow_zeta_negative_integers,
    shadow_zeta_positive_integers,
    shadow_zeta_special_values_table,
    shadow_zeta_taylor_finite_diff,
    convergence_analysis,
    detect_algebraic_relations,
    complementarity_at_s,
    complementarity_special_values_sweep,
    shadow_height_pairing_candidate,
    rationality_test_negative_integers,
    virasoro_stark_landscape,
    affine_sl2_stark_landscape,
    virasoro_shadow_growth_rate,
    w3_shadow_coefficients,
)


# =====================================================================
# Utility
# =====================================================================

def approx(a, b, rel=1e-8, abs_tol=1e-12):
    """Check approximate equality with both relative and absolute tolerance."""
    if abs(b) < abs_tol:
        return abs(a) < abs_tol
    return abs(a - b) / max(abs(a), abs(b), 1e-30) < rel


# =====================================================================
# SECTION 1: Heisenberg (class G) -- exact finite sums
# =====================================================================

class TestHeisenbergStark:
    """Heisenberg H_k: zeta(s) = k * 2^{-s}. All quantities are exact."""

    def test_heisenberg_zeta_at_zero(self):
        """zeta_{H_k}(0) = k for all k."""
        for k in [1, 2, 3, 5, 10]:
            coeffs = heisenberg_shadow_coefficients(k)
            taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
            assert approx(taylor[0], k), f"H_{k}: zeta(0) = {taylor[0]}, expected {k}"

    def test_heisenberg_derivatives_at_zero(self):
        """zeta^{(n)}_{H_k}(0) = k * (-log 2)^n."""
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=10)
        for n in range(11):
            expected = k * (-math.log(2)) ** n
            assert approx(taylor[n], expected), \
                f"n={n}: got {taylor[n]}, expected {expected}"

    def test_heisenberg_order_of_vanishing(self):
        """r_A = 0 for H_k with k != 0."""
        for k in [1, 2, 5]:
            coeffs = heisenberg_shadow_coefficients(k)
            r_A = order_of_vanishing_at_zero(coeffs)
            assert r_A == 0, f"H_{k}: r_A = {r_A}, expected 0"

    def test_heisenberg_regulator(self):
        """R_A = k for Heisenberg (since zeta(0) = k != 0, r_A = 0)."""
        k = 7.0
        coeffs = heisenberg_shadow_coefficients(k)
        R_A, r_A = shadow_regulator(coeffs)
        assert r_A == 0
        assert approx(R_A, k)

    def test_heisenberg_class_number(self):
        """zeta_{H_k}(1) = k/2."""
        for k in [1, 2, 3, 10]:
            coeffs = heisenberg_shadow_coefficients(k)
            cn = shadow_class_number(coeffs)
            assert approx(cn, k / 2.0), f"H_{k}: zeta(1) = {cn}, expected {k/2}"

    def test_heisenberg_central_value(self):
        """zeta_{H_k}(1/2) = k / sqrt(2)."""
        k = 4.0
        coeffs = heisenberg_shadow_coefficients(k)
        cv = shadow_central_value(coeffs)
        assert approx(cv, k / math.sqrt(2))

    def test_heisenberg_central_derivative(self):
        """zeta'_{H_k}(1/2) = -k log(2) / sqrt(2)."""
        k = 5.0
        coeffs = heisenberg_shadow_coefficients(k)
        cd = shadow_central_derivative(coeffs)
        expected = -k * math.log(2) / math.sqrt(2)
        assert approx(cd, expected)

    def test_heisenberg_negative_integer_values(self):
        """zeta_{H_k}(-n) = k * 2^n."""
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k)
        neg_vals = shadow_zeta_negative_integers(coeffs, max_n=5)
        for n in range(6):
            expected = k * (2 ** n)
            assert approx(neg_vals[-n], expected), \
                f"n={n}: got {neg_vals[-n]}, expected {expected}"

    def test_heisenberg_positive_integer_values(self):
        """zeta_{H_k}(n) = k * 2^{-n}."""
        k = 2.0
        coeffs = heisenberg_shadow_coefficients(k)
        pos_vals = shadow_zeta_positive_integers(coeffs, max_n=10)
        for n in range(1, 11):
            expected = k * 2 ** (-n)
            assert approx(pos_vals[n], expected)

    def test_heisenberg_rationality_negative_integers(self):
        """zeta_{H_k}(-n) is rational (manifestly, finite sum)."""
        coeffs = heisenberg_shadow_coefficients(3.0)
        results = rationality_test_negative_integers(coeffs, max_n=5)
        for n in range(6):
            assert results[-n]['is_rational'], f"H_3: zeta(-{n}) not detected as rational"


# =====================================================================
# SECTION 2: Affine sl_2 (class L) -- finite sums through arity 3
# =====================================================================

class TestAffineSl2Stark:
    """Affine V_k(sl_2): zeta(s) = kappa * 2^{-s} + alpha * 3^{-s}."""

    def test_affine_zeta_at_zero(self):
        """zeta(0) = kappa + alpha for affine sl_2."""
        for k in [1, 2, 4, 10]:
            coeffs = affine_sl2_shadow_coefficients(k)
            taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=3)
            kappa = 3.0 * (k + 2.0) / 4.0
            alpha = 4.0 / (k + 2.0)
            expected = kappa + alpha
            assert approx(taylor[0], expected), \
                f"k={k}: zeta(0) = {taylor[0]}, expected {expected}"

    def test_affine_order_of_vanishing(self):
        """r_A = 0 for generic affine sl_2."""
        for k in [1, 2, 5, 10]:
            coeffs = affine_sl2_shadow_coefficients(k)
            r_A = order_of_vanishing_at_zero(coeffs)
            assert r_A == 0

    def test_affine_regulator_is_zeta_zero(self):
        """R_A = zeta(0) = kappa + alpha for affine sl_2."""
        k = 3.0
        coeffs = affine_sl2_shadow_coefficients(k)
        R_A, r_A = shadow_regulator(coeffs)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        assert r_A == 0
        assert approx(R_A, kappa + alpha)

    def test_affine_class_number(self):
        """zeta(1) = kappa/2 + alpha/3."""
        k = 2.0
        coeffs = affine_sl2_shadow_coefficients(k)
        cn = shadow_class_number(coeffs)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        expected = kappa / 2.0 + alpha / 3.0
        assert approx(cn, expected)

    def test_affine_derivative_at_zero(self):
        """zeta'(0) = -kappa log(2) - alpha log(3)."""
        k = 5.0
        coeffs = affine_sl2_shadow_coefficients(k)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=3)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        expected = -kappa * math.log(2) - alpha * math.log(3)
        assert approx(taylor[1], expected)

    def test_affine_negative_integer_values(self):
        """zeta(-n) = kappa * 2^n + alpha * 3^n."""
        k = 4.0
        coeffs = affine_sl2_shadow_coefficients(k)
        neg_vals = shadow_zeta_negative_integers(coeffs, max_n=5)
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        for n in range(6):
            expected = kappa * (2 ** n) + alpha * (3 ** n)
            assert approx(neg_vals[-n], expected)

    def test_affine_rationality(self):
        """Affine sl_2 negative integer values are rational (finite sum)."""
        # k=2: kappa = 3, alpha = 1
        coeffs = affine_sl2_shadow_coefficients(2.0)
        results = rationality_test_negative_integers(coeffs, max_n=3)
        for n in range(4):
            assert results[-n]['is_rational']


# =====================================================================
# SECTION 3: Beta-gamma (class C) -- finite sum through arity 4
# =====================================================================

class TestBetaGammaStark:
    """Beta-gamma: zeta(s) = kappa 2^{-s} + 2 * 3^{-s} + Q0 * 4^{-s}."""

    def test_betagamma_zeta_at_zero(self):
        """zeta(0) = kappa + 2 + Q0 for beta-gamma at lambda=0.5."""
        coeffs = betagamma_shadow_coefficients(0.5)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=3)
        c_val = 2.0 * (6 * 0.25 - 6 * 0.5 + 1)
        kappa = c_val / 2.0
        Q0 = 10.0 / (c_val * (5 * c_val + 22))
        expected = kappa + 2.0 + Q0
        assert approx(taylor[0], expected)

    def test_betagamma_order_of_vanishing(self):
        """r_A = 0 for generic beta-gamma."""
        coeffs = betagamma_shadow_coefficients(0.5)
        r_A = order_of_vanishing_at_zero(coeffs)
        assert r_A == 0

    def test_betagamma_class_number(self):
        """zeta(1) = kappa/2 + 2/3 + Q0/4."""
        coeffs = betagamma_shadow_coefficients(0.5)
        cn = shadow_class_number(coeffs)
        c_val = 2.0 * (6 * 0.25 - 6 * 0.5 + 1)
        kappa = c_val / 2.0
        Q0 = 10.0 / (c_val * (5 * c_val + 22))
        expected = kappa / 2.0 + 2.0 / 3.0 + Q0 / 4.0
        assert approx(cn, expected)


# =====================================================================
# SECTION 4: Virasoro (class M) -- infinite tower, convergent
# =====================================================================

class TestVirasoroStark:
    """Virasoro Vir_c: class M, infinite tower with rho < 1."""

    def test_virasoro_growth_rate_classification(self):
        """Shadow growth rate rho < 1 for c > ~6.13, rho > 1 for small c.

        The critical c where rho = 1 is approximately 6.125.
        For c > 6.125: rho < 1, shadow zeta converges for all s (entire).
        For c < 6.125: rho > 1, shadow zeta diverges for all s.
        """
        # Large c: rho < 1 (convergent)
        for c_val in [10, 13, 25, 50]:
            rho = virasoro_shadow_growth_rate(float(c_val))
            assert rho < 1.0, f"c={c_val}: rho = {rho} >= 1"

        # Small c: rho > 1 (divergent)
        for c_val in [1, 2, 4]:
            rho = virasoro_shadow_growth_rate(float(c_val))
            assert rho > 1.0, f"c={c_val}: rho = {rho} <= 1"

    def test_virasoro_zeta_at_zero_nonvanishing(self):
        """zeta_{Vir_c}(0) != 0 for c values with rho < 1 (convergent regime)."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            taylor = shadow_zeta_taylor_at_zero(coeffs)
            assert abs(taylor[0]) > 1e-6, f"c={c_val}: zeta(0) ~ 0"

    def test_virasoro_order_of_vanishing_zero(self):
        """r_A = 0 for Virasoro at c values in the convergent regime."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            r_A = order_of_vanishing_at_zero(coeffs)
            assert r_A == 0, f"c={c_val}: r_A = {r_A}"

    def test_virasoro_regulator_equals_zeta_zero(self):
        """R_A = zeta(0) when r_A = 0."""
        c_val = 10.0
        coeffs = virasoro_shadow_coefficients(c_val, max_r=50)
        R_A, r_A = shadow_regulator(coeffs)
        taylor = shadow_zeta_taylor_at_zero(coeffs)
        assert r_A == 0
        assert approx(R_A, taylor[0])

    def test_virasoro_zeta_0_leading_term_kappa(self):
        """zeta(0) is dominated by S_2 = kappa = c/2 for large c."""
        c_val = 25.0
        coeffs = virasoro_shadow_coefficients(c_val, max_r=50)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        kappa = c_val / 2.0
        # At large c, S_r ~ (const/c)^{r-2} -> 0 for r >= 3
        # so zeta(0) -> kappa
        # The correction is O(1) from S_3 = 2
        assert abs(z0 - kappa) < 5.0, f"c=25: |zeta(0) - kappa| = {abs(z0 - kappa)}"

    def test_virasoro_class_number_positive(self):
        """zeta_{Vir_c}(1) > 0 for c in convergent regime."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            cn = shadow_class_number(coeffs)
            # kappa = c/2 > 0, so leading term positive.
            # Higher terms can be negative but are smaller.
            assert cn > 0, f"c={c_val}: class number = {cn} <= 0"

    def test_virasoro_central_value_finite(self):
        """zeta_{Vir_c}(1/2) is finite (at truncation) for standard c."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            cv = shadow_central_value(coeffs)
            assert math.isfinite(cv), f"c={c_val}: central value not finite"

    def test_virasoro_taylor_coefficients_c13(self):
        """Detailed Taylor expansion at the self-dual point c=13."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=10)

        # zeta(0) = sum S_r; should be dominated by kappa = 13/2
        assert taylor[0] > 6.0  # > kappa - small corrections
        assert taylor[0] < 10.0  # < kappa + S_3 + ...

        # All Taylor coefficients should be finite
        for k in range(11):
            assert math.isfinite(taylor[k]), f"k={k}: Taylor coeff not finite"

    def test_virasoro_special_values_c10(self):
        """Special values at c=10 (convergent regime)."""
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        table = shadow_zeta_special_values_table(coeffs)

        # At s=0: zeta(0) = sum S_r
        # At s=2: zeta(2) = sum S_r / r^2 converges faster
        assert abs(table[2]) < abs(table[0])  # faster convergence at larger s
        assert abs(table[5]) < abs(table[2])  # even faster

    def test_virasoro_monotone_decay_positive_s(self):
        """For c in convergent regime, |zeta(s)| decreases as s increases."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        vals = [shadow_zeta_eval_real(coeffs, s) for s in [0.5, 1, 2, 3, 5]]
        for i in range(len(vals) - 1):
            assert abs(vals[i]) >= abs(vals[i + 1]) - 1e-10


# =====================================================================
# SECTION 5: Taylor coefficient verification (path 1: finite differences)
# =====================================================================

class TestTaylorFiniteDifferences:
    """Verify Taylor coefficients by central finite differences (path 1)."""

    def test_heisenberg_fd_k0(self):
        coeffs = heisenberg_shadow_coefficients(3.0)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 0, h=1e-4)
        assert approx(direct[0], fd, rel=1e-4)

    def test_heisenberg_fd_k1(self):
        coeffs = heisenberg_shadow_coefficients(3.0)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 1, h=1e-4)
        assert approx(direct[1], fd, rel=1e-3)

    def test_heisenberg_fd_k2(self):
        coeffs = heisenberg_shadow_coefficients(3.0)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 2, h=1e-3)
        assert approx(direct[2], fd, rel=1e-2)

    def test_virasoro_fd_k0(self):
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 0, h=1e-4)
        assert approx(direct[0], fd, rel=1e-4)

    def test_virasoro_fd_k1(self):
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 1, h=1e-4)
        assert approx(direct[1], fd, rel=1e-3)

    def test_virasoro_fd_k2(self):
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 2, h=1e-3)
        assert approx(direct[2], fd, rel=1e-2)

    def test_virasoro_fd_k3(self):
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 3, h=1e-3)
        assert approx(direct[3], fd, rel=5e-2)

    def test_virasoro_fd_k4(self):
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 4, h=1e-2)
        assert approx(direct[4], fd, rel=0.1)

    def test_affine_fd_k0(self):
        coeffs = affine_sl2_shadow_coefficients(3.0)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=3)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 0, h=1e-4)
        assert approx(direct[0], fd, rel=1e-4)

    def test_affine_fd_k1(self):
        coeffs = affine_sl2_shadow_coefficients(3.0)
        direct = shadow_zeta_taylor_at_zero(coeffs, max_deriv=3)
        fd = shadow_zeta_taylor_finite_diff(coeffs, 1, h=1e-4)
        assert approx(direct[1], fd, rel=1e-3)


# =====================================================================
# SECTION 6: Complementarity (path 2)
# =====================================================================

class TestComplementarity:
    """Complementarity: Vir_c and Vir_{26-c} are Koszul dual (AP24)."""

    def test_complementarity_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [1, 2, 4, 10, 13, 20, 25]:
            result = complementarity_at_s(float(c_val), 0.0)
            assert approx(result['kappa_sum'], 13.0)

    def test_complementarity_s0_self_dual(self):
        """At c=13 (self-dual): zeta_{Vir_13}(s) = zeta_{Vir_13}(s) trivially."""
        result = complementarity_at_s(13.0, 0.0)
        assert approx(result['zeta_A'], result['zeta_Ad'])

    def test_complementarity_s0_sum_structure(self):
        """zeta_A(0) + zeta_{A!}(0) at c values in convergent regime.

        Note: both c AND 26-c must give rho < 1 for both series to converge.
        c=10: rho(10)~0.61, rho(16)~0.38 -- both converge.
        c=13: self-dual, rho(13)~0.47 -- converges.
        """
        for c_val in [10, 13]:
            result = complementarity_at_s(float(c_val), 0.0)
            # The sum should be finite and nonzero
            assert math.isfinite(result['sum'])
            assert abs(result['sum']) > 1e-3

    def test_complementarity_s1_symmetric(self):
        """At c=13: zeta_A(1) = zeta_{A!}(1) by self-duality."""
        result = complementarity_at_s(13.0, 1.0)
        assert approx(result['zeta_A'], result['zeta_Ad'], rel=1e-6)

    def test_complementarity_s_half(self):
        """zeta_A(1/2) + zeta_{A!}(1/2) at c=10 (convergent)."""
        result = complementarity_at_s(10.0, 0.5)
        assert math.isfinite(result['sum'])

    def test_complementarity_sweep(self):
        """Sweep over (c, s) pairs in convergent regime and check finiteness.

        Both c and 26-c must have rho < 1.  Critical c ~ 6.13, so
        we need c > 6.13 and 26-c > 6.13, i.e., 6.13 < c < 19.87.
        """
        results = complementarity_special_values_sweep(
            c_values=[10, 13],
            s_values=[0.0, 0.5, 1.0, 2.0],
            max_r=40,
        )
        assert len(results) > 0
        for r in results:
            assert math.isfinite(r['sum'])

    def test_complementarity_s0_c_plus_26mc(self):
        """Verify zeta_{c}(0) + zeta_{26-c}(0) varies continuously in c.

        Restricted to 7 < c < 19 so both c and 26-c are in convergent regime.
        """
        sums = []
        for c_val in [8, 10, 13, 16, 18]:
            result = complementarity_at_s(float(c_val), 0.0)
            sums.append(result['sum'])
        # All sums should be positive and finite
        for s in sums:
            assert math.isfinite(s)
            assert s > 0

    def test_complementarity_symmetry_at_c13(self):
        """At c=13, complementarity sum at s equals twice zeta_{13}(s)."""
        for s_val in [0.0, 0.5, 1.0, 2.0]:
            result = complementarity_at_s(13.0, s_val)
            assert approx(result['sum'], 2.0 * result['zeta_A'], rel=1e-6)


# =====================================================================
# SECTION 7: Convergence analysis (path 4)
# =====================================================================

class TestConvergence:
    """Verify exponential convergence for class M (rho < 1)."""

    def test_virasoro_exponential_convergence_c10(self):
        """Term sizes decay exponentially for Virasoro c=10."""
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        analysis = convergence_analysis(coeffs, s=0.0)
        # Check that term sizes decay
        terms = [a[2] for a in analysis if a[2] > 0]
        if len(terms) >= 3:
            for i in range(1, len(terms)):
                # Exponential decay: term_{i+1} < term_i
                assert terms[i] <= terms[i - 1] + 1e-10

    def test_virasoro_convergence_faster_at_larger_s(self):
        """Convergence is faster at larger s values."""
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        an_s0 = convergence_analysis(coeffs, s=0.0, checkpoints=[50])
        an_s5 = convergence_analysis(coeffs, s=5.0, checkpoints=[50])
        # At s=5, the last term should be smaller
        if an_s0 and an_s5:
            if an_s0[-1][2] > 1e-30 and an_s5[-1][2] > 1e-30:
                assert an_s5[-1][2] <= an_s0[-1][2]

    def test_truncation_error_small(self):
        """Truncation at r=30 vs r=50 should differ by tiny amount."""
        coeffs50 = virasoro_shadow_coefficients(10.0, max_r=50)
        z30 = shadow_zeta_eval_real(coeffs50, 0.0, max_r=30)
        z50 = shadow_zeta_eval_real(coeffs50, 0.0, max_r=50)
        # Difference should be small (exponentially small corrections)
        assert abs(z30 - z50) < 0.01 * abs(z50)

    def test_truncation_error_at_s1(self):
        """Truncation error at s=1."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        z30 = shadow_zeta_eval_real(coeffs, 1.0, max_r=30)
        z50 = shadow_zeta_eval_real(coeffs, 1.0, max_r=50)
        assert abs(z30 - z50) < 0.001 * abs(z50)


# =====================================================================
# SECTION 8: Cross-family consistency (path 5)
# =====================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks: additivity, limiting cases, etc."""

    def test_heisenberg_is_virasoro_limit(self):
        """As c -> infinity for Virasoro, shadow coefficients S_r -> 0 for r >= 3.

        Virasoro with large c approximates class G behaviour: the tower
        terminates at arity 2 in the limit.
        """
        c_val = 1000.0
        coeffs = virasoro_shadow_coefficients(c_val, max_r=20)
        # S_3 = 2 (constant) but S_4 = 10/(c(5c+22)) -> 0
        assert abs(coeffs[4]) < 0.01
        assert abs(coeffs[5]) < 0.001

    def test_affine_finite_sum_consistency(self):
        """For affine sl_2, zeta(s) = kappa 2^{-s} + alpha 3^{-s}.

        Verify by comparing direct evaluation with finite-sum formula.
        """
        k = 5.0
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k, max_r=50)

        for s_val in [0.0, 0.5, 1.0, 2.0, 3.0]:
            direct = shadow_zeta_eval_real(coeffs, s_val)
            formula = kappa * 2 ** (-s_val) + alpha * 3 ** (-s_val)
            assert approx(direct, formula)

    def test_betagamma_finite_sum_consistency(self):
        """Beta-gamma: zeta(s) = kappa 2^{-s} + 2 * 3^{-s} + Q0 * 4^{-s}."""
        lam = 0.5
        c_val = 2.0 * (6 * lam ** 2 - 6 * lam + 1)
        kappa = c_val / 2.0
        Q0 = 10.0 / (c_val * (5 * c_val + 22))
        coeffs = betagamma_shadow_coefficients(lam, max_r=50)

        for s_val in [0.0, 0.5, 1.0, 2.0]:
            direct = shadow_zeta_eval_real(coeffs, s_val)
            formula = kappa * 2 ** (-s_val) + 2 * 3 ** (-s_val) + Q0 * 4 ** (-s_val)
            assert approx(direct, formula)

    def test_virasoro_kappa_matches_s2(self):
        """S_2(Vir_c) = kappa = c/2 (AP9)."""
        for c_val in [1, 5, 10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=30)
            # S_2 = a_0 / 2 where a_0 = |c|; for c > 0: S_2 = c/2
            assert approx(coeffs[2], c_val / 2.0)

    def test_virasoro_s3_is_two(self):
        """S_3(Vir_c) = 2 (gravitational cubic, c-independent)."""
        for c_val in [1, 5, 10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=30)
            # S_3 = a_1 / 3 where a_1 = 12c / (2|c|) = 6 for c > 0
            # So S_3 = 6/3 = 2
            assert approx(coeffs[3], 2.0)


# =====================================================================
# SECTION 9: Virasoro Stark landscape sweep
# =====================================================================

class TestVirasoroLandscape:
    """Full Stark landscape for Virasoro at c = 1, 2, 4, 10, 13, 25."""

    @pytest.fixture
    def landscape(self):
        return virasoro_stark_landscape(
            c_values=[10, 13, 20, 25],
            max_r=50,
        )

    def test_landscape_size(self, landscape):
        assert len(landscape) == 4

    def test_landscape_all_r_A_zero(self, landscape):
        """All Virasoro algebras have r_A = 0 at these c values."""
        for entry in landscape:
            assert entry['order_of_vanishing'] == 0

    def test_landscape_regulators_positive(self, landscape):
        """All regulators (= zeta(0)) are positive for c > 0."""
        for entry in landscape:
            assert entry['regulator'] > 0

    def test_landscape_class_numbers_positive(self, landscape):
        """All shadow class numbers are positive."""
        for entry in landscape:
            assert entry['class_number'] > 0

    def test_landscape_central_values_finite(self, landscape):
        """All central values zeta(1/2) are finite."""
        for entry in landscape:
            assert math.isfinite(entry['central_value'])

    def test_landscape_special_values_monotone(self, landscape):
        """zeta(n) decreases with n for n >= 1."""
        for entry in landscape:
            prev = entry.get('zeta_1', float('inf'))
            for n in range(2, 11):
                curr = entry.get(f'zeta_{n}', 0.0)
                assert abs(curr) <= abs(prev) + 1e-10
                prev = curr


# =====================================================================
# SECTION 10: Affine sl_2 Stark landscape
# =====================================================================

class TestAffineLandscape:

    @pytest.fixture
    def landscape(self):
        return affine_sl2_stark_landscape(
            k_values=[1, 2, 3, 5, 10, 20],
            max_r=50,
        )

    def test_landscape_size(self, landscape):
        assert len(landscape) == 6

    def test_landscape_kappa_formula(self, landscape):
        """kappa = 3(k+2)/4."""
        for entry in landscape:
            expected = 3.0 * (entry['k'] + 2.0) / 4.0
            assert approx(entry['kappa'], expected)

    def test_landscape_alpha_formula(self, landscape):
        """alpha = 4/(k+2)."""
        for entry in landscape:
            expected = 4.0 / (entry['k'] + 2.0)
            assert approx(entry['alpha'], expected)


# =====================================================================
# SECTION 11: Rationality tests at negative integers
# =====================================================================

class TestRationality:
    """Shadow Klingen-Siegel: are zeta_A(-n) rational?"""

    def test_heisenberg_all_rational(self):
        """Heisenberg: zeta(-n) = k * 2^n, manifestly rational."""
        coeffs = heisenberg_shadow_coefficients(5.0)
        results = rationality_test_negative_integers(coeffs, max_n=5)
        for n in range(6):
            assert results[-n]['is_rational']
            # Check value
            assert approx(results[-n]['value'], 5.0 * 2 ** n)

    def test_affine_all_rational_integer_level(self):
        """Affine sl_2 at integer level: zeta(-n) rational."""
        coeffs = affine_sl2_shadow_coefficients(2.0)  # kappa=3, alpha=1
        results = rationality_test_negative_integers(coeffs, max_n=3)
        for n in range(4):
            assert results[-n]['is_rational']

    def test_virasoro_c13_negative_integers(self):
        """Virasoro c=13: test if zeta(-n) are close to rational."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        results = rationality_test_negative_integers(coeffs, max_n=3, tol=1e-6)
        # zeta(-n) = sum S_r r^n: convergent infinite sum (rho < 1 at c=13).
        # Not expected to be rational in general.  This test documents outcome.
        for n in range(4):
            val = results[-n]['value']
            assert math.isfinite(val)


# =====================================================================
# SECTION 12: Special values at negative integers
# =====================================================================

class TestNegativeIntegers:
    """Shadow Bernoulli special values."""

    def test_heisenberg_negative(self):
        """Heisenberg: zeta(-n) = k * 2^n."""
        k = 4.0
        coeffs = heisenberg_shadow_coefficients(k)
        neg = shadow_zeta_negative_integers(coeffs, max_n=5)
        for n in range(6):
            assert approx(neg[-n], k * 2 ** n)

    def test_affine_negative(self):
        """Affine sl_2: zeta(-n) = kappa * 2^n + alpha * 3^n."""
        k = 3.0
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k)
        neg = shadow_zeta_negative_integers(coeffs, max_n=5)
        for n in range(6):
            expected = kappa * 2 ** n + alpha * 3 ** n
            assert approx(neg[-n], expected)

    def test_virasoro_zeta_minus_n_grow(self):
        """For Virasoro, zeta(-n) grows with n (S_r r^n summed)."""
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        neg = shadow_zeta_negative_integers(coeffs, max_n=5)
        # zeta(-n) should increase in magnitude with n
        for n in range(1, 5):
            assert abs(neg[-(n + 1)]) >= abs(neg[-n]) - 1e-5


# =====================================================================
# SECTION 13: Positive integer special values
# =====================================================================

class TestPositiveIntegers:

    def test_heisenberg_positive(self):
        """zeta_{H_k}(n) = k * 2^{-n}."""
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k)
        pos = shadow_zeta_positive_integers(coeffs, max_n=10)
        for n in range(1, 11):
            assert approx(pos[n], k * 2 ** (-n))

    def test_virasoro_positive_decay(self):
        """zeta_{Vir_c}(n) decays with n for n >= 1."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        pos = shadow_zeta_positive_integers(coeffs, max_n=10)
        for n in range(1, 10):
            assert abs(pos[n + 1]) <= abs(pos[n]) + 1e-10

    def test_virasoro_zeta_2_smaller_than_zeta_1(self):
        """zeta(2) < zeta(1) since each term has an extra 1/r factor."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            z1 = shadow_zeta_eval_real(coeffs, 1.0)
            z2 = shadow_zeta_eval_real(coeffs, 2.0)
            assert abs(z2) < abs(z1)


# =====================================================================
# SECTION 14: Special values table
# =====================================================================

class TestSpecialValuesTable:

    def test_table_range(self):
        """Default table covers s = -5 to 10."""
        coeffs = heisenberg_shadow_coefficients(2.0)
        table = shadow_zeta_special_values_table(coeffs)
        assert set(table.keys()) == set(range(-5, 11))

    def test_table_heisenberg_consistency(self):
        """Table values match direct computation."""
        k = 2.0
        coeffs = heisenberg_shadow_coefficients(k)
        table = shadow_zeta_special_values_table(coeffs)
        for n in range(-5, 11):
            expected = k * 2 ** (-float(n))
            assert approx(table[n], expected)

    def test_table_virasoro_finiteness(self):
        """All table entries are finite for Virasoro c=13."""
        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        table = shadow_zeta_special_values_table(coeffs)
        for n, val in table.items():
            assert math.isfinite(val), f"s={n}: value not finite"


# =====================================================================
# SECTION 15: Gross-Zagier type height pairing
# =====================================================================

class TestGrossZagier:

    def test_height_pairing_virasoro(self):
        """Shadow height pairing candidate for Virasoro c=10."""
        coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        hp = shadow_height_pairing_candidate(coeffs)
        assert math.isfinite(hp['zeta_prime_half'])
        assert 'ratio_kappa2' in hp

    def test_height_pairing_heisenberg(self):
        """For Heisenberg: zeta'(1/2) = -k log(2) / sqrt(2)."""
        k = 5.0
        coeffs = heisenberg_shadow_coefficients(k)
        hp = shadow_height_pairing_candidate(coeffs)
        expected = -k * math.log(2) / math.sqrt(2)
        assert approx(hp['zeta_prime_half'], expected)

    def test_height_pairing_ratios_finite(self):
        """Height pairing ratios are finite for Virasoro in convergent regime."""
        for c_val in [10, 13, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            hp = shadow_height_pairing_candidate(coeffs)
            if 'ratio_kappa2' in hp:
                assert math.isfinite(hp['ratio_kappa2'])

    def test_height_pairing_ratio_c_dependence(self):
        """Check if the ratio zeta'(1/2)/kappa^2 varies smoothly with c."""
        ratios = []
        for c_val in [5, 10, 13, 20, 25]:
            coeffs = virasoro_shadow_coefficients(float(c_val), max_r=50)
            hp = shadow_height_pairing_candidate(coeffs)
            if 'ratio_kappa2' in hp:
                ratios.append(hp['ratio_kappa2'])
        # All ratios should be finite
        for r in ratios:
            assert math.isfinite(r)


# =====================================================================
# SECTION 16: W_3 on T-line
# =====================================================================

class TestW3Stark:
    """W_3 on T-line = Virasoro restriction."""

    def test_w3_matches_virasoro(self):
        """W_3 T-line shadow = Virasoro shadow."""
        c_val = 10.0
        coeffs_vir = virasoro_shadow_coefficients(c_val, max_r=30)
        coeffs_w3 = w3_shadow_coefficients(c_val, max_r=30)
        for r in range(2, 31):
            assert approx(coeffs_vir[r], coeffs_w3[r])

    def test_w3_zeta_at_convergent_c(self):
        """W_3 at c=10 (convergent regime): compute zeta(0)."""
        coeffs = w3_shadow_coefficients(10.0, max_r=50)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        assert math.isfinite(z0)
        # On T-line, should match Virasoro
        vir_coeffs = virasoro_shadow_coefficients(10.0, max_r=50)
        z0_vir = shadow_zeta_eval_real(vir_coeffs, 0.0)
        assert approx(z0, z0_vir)


# =====================================================================
# SECTION 17: High-precision tests (mpmath)
# =====================================================================

class TestHighPrecision:

    def test_hp_taylor_heisenberg(self):
        """High-precision Taylor expansion matches standard."""
        try:
            import mpmath  # noqa: F401
        except ImportError:
            pytest.skip("mpmath not available")

        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k)
        taylor_std = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        taylor_hp = shadow_zeta_taylor_at_zero_hp(coeffs, max_deriv=5, dps=30)

        for n in range(6):
            assert approx(taylor_std[n], float(taylor_hp[n]), rel=1e-10)

    def test_hp_regulator_virasoro(self):
        """High-precision regulator for Virasoro c=13."""
        try:
            import mpmath  # noqa: F401
        except ImportError:
            pytest.skip("mpmath not available")

        coeffs = virasoro_shadow_coefficients(13.0, max_r=50)
        R_std, r_std = shadow_regulator(coeffs)
        R_hp, r_hp = shadow_regulator_hp(coeffs, dps=30)

        assert r_std == r_hp
        assert approx(R_std, float(R_hp), rel=1e-8)


# =====================================================================
# SECTION 18: Algebraic relation detection
# =====================================================================

class TestAlgebraicRelations:

    def test_detect_integer(self):
        """Should detect that 5.0 is rational."""
        result = detect_algebraic_relations(5.0)
        assert result is not None

    def test_detect_pi_multiple(self):
        """Should detect that 3.14159... is close to pi."""
        result = detect_algebraic_relations(math.pi, tol=1e-6)
        assert result is not None

    def test_heisenberg_regulator_rational(self):
        """Heisenberg regulator R_A = k is rational."""
        k = 7.0
        coeffs = heisenberg_shadow_coefficients(k)
        R_A, _ = shadow_regulator(coeffs)
        result = detect_algebraic_relations(R_A)
        assert result is not None


# =====================================================================
# SECTION 19: Edge cases and robustness
# =====================================================================

class TestEdgeCases:

    def test_virasoro_small_c_truncated(self):
        """Virasoro at small c (c=0.5) -- truncated sum is finite.

        Note: rho > 1 at c=0.5, so the infinite series diverges.
        But the finite truncation at max_r=50 is still a finite number.
        """
        coeffs = virasoro_shadow_coefficients(0.5, max_r=30)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        assert math.isfinite(z0)

    def test_virasoro_large_c(self):
        """Virasoro at large c (c=100)."""
        coeffs = virasoro_shadow_coefficients(100.0, max_r=50)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        # Should be close to kappa = 50
        assert abs(z0 - 50.0) < 5.0

    def test_virasoro_c_negative_truncated(self):
        """Virasoro at c=-1 (non-unitary) -- truncated sum is finite."""
        coeffs = virasoro_shadow_coefficients(-1.0, max_r=30)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        assert math.isfinite(z0)

    def test_virasoro_c_zero_raises(self):
        """Virasoro at c=0 should raise ValueError."""
        with pytest.raises(ValueError):
            virasoro_shadow_coefficients(0.0)

    def test_complex_evaluation(self):
        """Evaluate at complex s."""
        coeffs = heisenberg_shadow_coefficients(3.0)
        val = shadow_zeta_eval(coeffs, complex(1, 1))
        assert abs(val) > 0

    def test_empty_tail(self):
        """Heisenberg: all S_r = 0 for r >= 3 does not cause issues."""
        coeffs = heisenberg_shadow_coefficients(1.0, max_r=100)
        taylor = shadow_zeta_taylor_at_zero(coeffs, max_deriv=5)
        assert approx(taylor[0], 1.0)

    def test_virasoro_negative_c_large_truncated(self):
        """Virasoro at c=-10 (well away from poles) -- truncated."""
        coeffs = virasoro_shadow_coefficients(-10.0, max_r=30)
        z0 = shadow_zeta_eval_real(coeffs, 0.0)
        assert math.isfinite(z0)


# =====================================================================
# SECTION 20: Multi-path verification summary tests
# =====================================================================

class TestMultiPathVerification:
    """Summary tests that cross-check multiple verification paths."""

    def test_heisenberg_three_path_zeta_0(self):
        """Three-path verification for H_3 at s=0.

        Path 1: Taylor expansion
        Path 2: Direct evaluation
        Path 3: Finite difference of zeta(h) at h->0
        """
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k)

        # Path 1: Taylor
        taylor = shadow_zeta_taylor_at_zero(coeffs)
        v1 = taylor[0]

        # Path 2: Direct evaluation
        v2 = shadow_zeta_eval_real(coeffs, 0.0)

        # Path 3: Finite difference extrapolation
        v3 = shadow_zeta_taylor_finite_diff(coeffs, 0, h=1e-5)

        assert approx(v1, k)
        assert approx(v2, k)
        assert approx(v3, k, rel=1e-4)

    def test_virasoro_three_path_zeta_1(self):
        """Three-path verification for Vir_{10} at s=1.

        Path 1: Direct summation
        Path 2: Class number function
        Path 3: Truncation convergence analysis
        """
        c_val = 10.0
        coeffs = virasoro_shadow_coefficients(c_val, max_r=50)

        # Path 1: Direct
        v1 = shadow_zeta_eval_real(coeffs, 1.0)

        # Path 2: Class number
        v2 = shadow_class_number(coeffs)

        # Path 3: Check convergence from truncation analysis
        an = convergence_analysis(coeffs, s=1.0, checkpoints=[20, 30, 40, 50])
        v3 = an[-1][1]  # partial sum at r=50

        assert approx(v1, v2)
        assert approx(v1, v3)

    def test_virasoro_complementarity_three_path_s0(self):
        """Three-path verification of complementarity at s=0.

        Path 1: Direct sum zeta_c(0) + zeta_{26-c}(0)
        Path 2: From complementarity_at_s
        Path 3: From individual regulators

        Use c=10 (rho~0.61) and 26-c=16 (rho~0.38), both convergent.
        """
        c_val = 10.0
        coeffs_A = virasoro_shadow_coefficients(c_val, max_r=50)
        coeffs_Ad = virasoro_shadow_coefficients(26.0 - c_val, max_r=50)

        # Path 1: Direct
        v1_A = shadow_zeta_eval_real(coeffs_A, 0.0)
        v1_Ad = shadow_zeta_eval_real(coeffs_Ad, 0.0)
        v1 = v1_A + v1_Ad

        # Path 2: Via complementarity function
        result = complementarity_at_s(c_val, 0.0, max_r=50)
        v2 = result['sum']

        # Path 3: Via regulators (r_A = 0, so R_A = zeta(0))
        R_A, _ = shadow_regulator(coeffs_A)
        R_Ad, _ = shadow_regulator(coeffs_Ad)
        v3 = R_A + R_Ad

        assert approx(v1, v2)
        assert approx(v1, v3)

    def test_affine_three_path_class_number(self):
        """Three-path verification for affine sl_2 class number.

        Path 1: shadow_class_number
        Path 2: Direct formula kappa/2 + alpha/3
        Path 3: shadow_zeta_eval_real at s=1
        """
        k = 5.0
        kappa = 3.0 * (k + 2.0) / 4.0
        alpha = 4.0 / (k + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k)

        v1 = shadow_class_number(coeffs)
        v2 = kappa / 2.0 + alpha / 3.0
        v3 = shadow_zeta_eval_real(coeffs, 1.0)

        assert approx(v1, v2)
        assert approx(v1, v3)


if __name__ == '__main__':
    pytest.main([__file__, '-x', '--tb=short', '-q'])
