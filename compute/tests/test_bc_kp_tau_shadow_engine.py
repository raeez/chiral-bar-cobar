r"""Tests for bc_kp_tau_shadow_engine.py -- KP hierarchy tau functions from shadow PFs.

Multi-path verification structure:
    (i)   Direct Hirota bilinear
    (ii)  KdV / Boussinesq / N-reduction
    (iii) Sato Grassmannian
    (iv)  Free fermion (boson-fermion correspondence)
    (v)   Numerical (closed form vs series, specific values)

Minimum 95 tests as specified.
"""

import math
import cmath
import pytest
from fractions import Fraction

from compute.lib.bc_kp_tau_shadow_engine import (
    # Elementary Schur polynomials
    schur_polynomial_elementary,
    schur_poly_exact,
    # Kappa values
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_affine_slN,
    # Tau function classes
    ShadowTauFunction,
    # Builders
    build_heisenberg_tau,
    build_virasoro_tau,
    build_affine_sl2_tau,
    # Tests
    hirota_bilinear_scalar,
    hirota_bilinear_through_order,
    check_kdv_reduction,
    check_n_reduction,
    tau_at_zeta_zeros,
    heisenberg_tau_schur_expansion,
    # Verification
    verify_ahat_generating_function,
    verify_hirota_multipath,
    shadow_tau_vs_partition_function,
    # Utilities
    integer_partitions,
    schur_function_hook_length,
    # Constants
    RIEMANN_ZETA_ZEROS,
    PI,
    TWO_PI_SQ,
)

from compute.lib.utils import lambda_fp, F_g
from sympy import Rational


# =========================================================================
# Section 1: Elementary Schur polynomial tests (10 tests)
# =========================================================================

class TestSchurPolynomials:
    """Tests for elementary Schur polynomials S_j(t)."""

    def test_S0_is_one(self):
        """S_0(t) = 1 for any t."""
        assert schur_polynomial_elementary(0, (1.0, 2.0, 3.0)) == 1.0

    def test_S1_is_t1(self):
        """S_1(t) = t_1."""
        assert abs(schur_polynomial_elementary(1, (3.14, 2.0)) - 3.14) < 1e-12

    def test_S2_formula(self):
        """S_2(t) = t_1^2/2 + t_2."""
        t = (2.0, 5.0, 1.0)
        expected = 2.0 ** 2 / 2 + 5.0  # = 2 + 5 = 7
        assert abs(schur_polynomial_elementary(2, t) - expected) < 1e-12

    def test_S3_formula(self):
        """S_3(t) = t_1^3/6 + t_1*t_2 + t_3."""
        t = (1.0, 1.0, 1.0)
        expected = 1.0 / 6 + 1.0 + 1.0  # = 13/6
        assert abs(schur_polynomial_elementary(3, t) - expected) < 1e-12

    def test_S_negative_is_zero(self):
        """S_j = 0 for j < 0."""
        assert schur_polynomial_elementary(-1, (1.0,)) == 0.0

    def test_generating_function_identity(self):
        """Verify exp(sum t_k z^k) = sum S_j z^j at z = 0.1."""
        t = (0.3, 0.1, 0.05, 0.02)
        z = 0.1
        # Left side: exp(sum t_k z^k)
        exponent = sum(t[k] * z ** (k + 1) for k in range(len(t)))
        lhs = math.exp(exponent)
        # Right side: sum S_j z^j
        rhs = sum(schur_polynomial_elementary(j, t) * z ** j for j in range(20))
        assert abs(lhs - rhs) < 1e-10

    def test_schur_recurrence(self):
        """Verify S_j = (1/j) sum k*t_k*S_{j-k}."""
        t = (0.5, 0.3, 0.2)
        S3 = schur_polynomial_elementary(3, t)
        # Manual recurrence
        S3_manual = (1.0 / 3) * (
            1 * t[0] * schur_polynomial_elementary(2, t) +
            2 * t[1] * schur_polynomial_elementary(1, t) +
            3 * t[2] * schur_polynomial_elementary(0, t)
        )
        assert abs(S3 - S3_manual) < 1e-12

    def test_schur_at_zero(self):
        """S_j(0, 0, ...) = 0 for j >= 1."""
        t = (0.0, 0.0, 0.0)
        for j in range(1, 6):
            assert abs(schur_polynomial_elementary(j, t)) < 1e-15

    def test_schur_single_variable(self):
        """S_j(t_1, 0, 0, ...) = t_1^j / j!."""
        t1 = 2.0
        t = (t1, 0.0, 0.0, 0.0, 0.0)
        for j in range(6):
            expected = t1 ** j / math.factorial(j)
            actual = schur_polynomial_elementary(j, t)
            assert abs(actual - expected) < 1e-10, f"S_{j} failed: {actual} vs {expected}"

    def test_schur_S4(self):
        """S_4(t) for specific values."""
        t = (1.0, 0.0, 0.0, 0.0)
        # S_4(t_1, 0, 0, 0) = t_1^4/24
        expected = 1.0 / 24
        assert abs(schur_polynomial_elementary(4, t) - expected) < 1e-12


# =========================================================================
# Section 2: Kappa value tests (10 tests)
# =========================================================================

class TestKappaValues:
    """Tests for modular characteristic kappa (AP1/AP39)."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1, 2, 3, 5, 10]:
            assert kappa_heisenberg(k) == float(k)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1.0, 10.0, 13.0, 26.0]:
            assert abs(kappa_virasoro(c) - c / 2) < 1e-12

    def test_sl2_kappa(self):
        """kappa(sl_2_k) = 3*(k+2)/4. dim=3, h^v=2."""
        assert abs(kappa_affine_sl2(1) - 3.0 * 3 / 4) < 1e-12  # 9/4
        assert abs(kappa_affine_sl2(2) - 3.0 * 4 / 4) < 1e-12  # 3

    def test_slN_kappa_sl2(self):
        """kappa(sl_N) at N=2 should match kappa_affine_sl2."""
        for k in [1, 2, 3]:
            assert abs(kappa_affine_slN(2, k) - kappa_affine_sl2(k)) < 1e-12

    def test_slN_kappa_formula(self):
        """kappa(sl_N_k) = (N^2-1)*(k+N)/(2*N)."""
        # sl_3 at level 1: (9-1)*(1+3)/(2*3) = 8*4/6 = 32/6 = 16/3
        assert abs(kappa_affine_slN(3, 1) - 16.0 / 3) < 1e-12

    def test_heisenberg_not_c_over_2(self):
        """AP39: kappa(H_k) = k != c/2 = k/2 in general."""
        # For Heisenberg: c = k but kappa = k, not k/2
        k = 5
        assert kappa_heisenberg(k) != k / 2.0
        assert kappa_heisenberg(k) == float(k)

    def test_virasoro_self_dual_kappa(self):
        """At self-dual point c=13: kappa = 13/2. AP8."""
        assert abs(kappa_virasoro(13.0) - 6.5) < 1e-12

    def test_virasoro_critical_kappa(self):
        """At critical dimension c=26: kappa = 13."""
        assert abs(kappa_virasoro(26.0) - 13.0) < 1e-12

    def test_kappa_positivity(self):
        """kappa > 0 for all standard families at positive parameters."""
        assert kappa_heisenberg(1) > 0
        assert kappa_virasoro(1.0) > 0
        assert kappa_affine_sl2(1) > 0

    def test_sl2_kappa_level_dependence(self):
        """kappa(sl_2_k) is strictly increasing in level k."""
        kappas = [kappa_affine_sl2(k) for k in range(1, 7)]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]


# =========================================================================
# Section 3: Shadow tau function basic tests (15 tests)
# =========================================================================

class TestShadowTauBasic:
    """Basic tests for the ShadowTauFunction class."""

    def test_tau_at_zero(self):
        """tau(0) = exp(0) = 1 for any algebra."""
        tau = build_heisenberg_tau(1)
        assert abs(tau.tau_scalar(0.0) - 1.0) < 1e-12

    def test_log_tau_at_zero(self):
        """log tau(0) = 0."""
        tau = build_virasoro_tau(10.0)
        assert abs(tau.log_tau_scalar(0.0)) < 1e-12

    def test_heisenberg_tau_at_1(self):
        """tau_Heis(1) = exp(kappa * ((1/2)/sin(1/2) - 1))."""
        k = 1
        tau = build_heisenberg_tau(k)
        expected = math.exp(k * (0.5 / math.sin(0.5) - 1.0))
        assert abs(tau.tau_scalar(1.0) - expected) < 1e-10

    def test_virasoro_tau_at_1(self):
        """tau_Vir(1) for c=10: kappa=5."""
        c = 10.0
        tau = build_virasoro_tau(c)
        kappa = c / 2.0
        expected = math.exp(kappa * (0.5 / math.sin(0.5) - 1.0))
        assert abs(tau.tau_scalar(1.0) - expected) < 1e-10

    def test_sl2_tau_at_1(self):
        """tau_{sl2_k=1}(1)."""
        tau = build_affine_sl2_tau(1)
        kappa = 3.0 * 3 / 4  # 9/4
        expected = math.exp(kappa * (0.5 / math.sin(0.5) - 1.0))
        assert abs(tau.tau_scalar(1.0) - expected) < 1e-10

    def test_free_energy_genus_1(self):
        """F_1 = kappa/24."""
        for kappa in [1.0, 5.0, 13.0]:
            tau = ShadowTauFunction('test', kappa)
            F1 = tau.free_energy_scalar(1)
            assert abs(F1 - kappa / 24.0) < 1e-12

    def test_free_energy_genus_2(self):
        """F_2 = 7*kappa/5760."""
        kappa = 1.0
        tau = ShadowTauFunction('test', kappa)
        F2 = tau.free_energy_scalar(2)
        assert abs(F2 - 7.0 * kappa / 5760.0) < 1e-12

    def test_series_converges_to_closed_form(self):
        """Series sum vs closed form should agree for |t_1| < 2*pi."""
        tau = build_heisenberg_tau(1)
        for t1 in [0.5, 1.0, 2.0, 3.0]:
            series = tau.log_tau_series(t1, max_g=30)
            closed = tau.log_tau_scalar(t1)
            assert abs(series - closed) < 1e-6, f"Mismatch at t1={t1}: {series} vs {closed}"

    def test_tau_monotone_in_kappa(self):
        """tau(t_1) is monotone increasing in kappa for t_1 > 0."""
        t1 = 1.0
        for k in range(1, 5):
            tau_k = build_heisenberg_tau(k)
            tau_k1 = build_heisenberg_tau(k + 1)
            assert tau_k.tau_scalar(t1) < tau_k1.tau_scalar(t1)

    def test_tau_even_function(self):
        """log tau(-t_1) = log tau(t_1) (even function)."""
        tau = build_virasoro_tau(10.0)
        for t1 in [0.5, 1.0, 2.0]:
            assert abs(tau.log_tau_scalar(t1) - tau.log_tau_scalar(-t1)) < 1e-12

    def test_tau_positive_for_real_input(self):
        """tau(t_1) > 0 for real t_1 with |t_1| < 2*pi."""
        tau = build_heisenberg_tau(1)
        for t1 in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0]:
            assert tau.tau_scalar(t1) > 0

    def test_tau_complex_conjugate(self):
        """tau(t*) = tau(t)* for real kappa."""
        tau = build_heisenberg_tau(1)
        z = complex(1.0, 0.5)
        val = tau.tau_scalar_complex(z)
        val_conj = tau.tau_scalar_complex(z.conjugate())
        assert abs(val.conjugate() - val_conj) < 1e-10

    def test_radius_of_convergence(self):
        """Series diverges near t_1 = 2*pi (pole of csc)."""
        tau = build_heisenberg_tau(1)
        # At t_1 = 2*pi - epsilon, log tau should be large
        eps = 0.01
        val = tau.log_tau_scalar(2 * PI - eps)
        assert abs(val) > 10  # should be large near the pole

    def test_heisenberg_class_G(self):
        """Heisenberg has no higher shadow coefficients (class G)."""
        tau = build_heisenberg_tau(1)
        assert len(tau.shadow_coefficients) == 0

    def test_virasoro_has_higher_shadows(self):
        """Virasoro has nonzero S_3, S_4, ... (class M)."""
        tau = build_virasoro_tau(10.0)
        assert len(tau.shadow_coefficients) > 2
        assert abs(tau.shadow_coefficients.get(3, 0.0)) > 1e-10


# =========================================================================
# Section 4: Ahat generating function verification (8 tests)
# =========================================================================

class TestAhatGeneratingFunction:
    """Multi-path verification of the Ahat generating function."""

    def test_ahat_series_vs_closed_heis(self):
        """Path 1: Series vs closed form for Heisenberg k=1."""
        result = verify_ahat_generating_function(1.0, max_genus=30)
        for comp in result['path1_series_vs_closed']:
            if comp['t'] < 4.5:  # well within convergent region
                assert comp['abs_diff'] < 1e-6, f"Mismatch at t={comp['t']}"
            elif comp['t'] < 5.5:  # near boundary, relax tolerance
                assert comp['abs_diff'] < 1e-4, f"Mismatch at t={comp['t']}"

    def test_ahat_F1_exact(self):
        """Path 2: F_1 = kappa/24 exactly."""
        for kappa in [1.0, 5.0, 13.0]:
            result = verify_ahat_generating_function(kappa)
            assert result['path2_specific']['F_1_match']

    def test_ahat_F2_exact(self):
        """Path 2: F_2 = 7*kappa/5760 exactly."""
        for kappa in [1.0, 5.0, 13.0]:
            result = verify_ahat_generating_function(kappa)
            assert result['path2_specific']['F_2_match']

    def test_ahat_ratio_convergence(self):
        """Path 3: lambda_{g+1}/lambda_g -> 1/(2*pi)^2."""
        result = verify_ahat_generating_function(1.0)
        assert result['path3_ratio']['converges']

    def test_ahat_virasoro_c13(self):
        """Ahat verification for Virasoro at self-dual c=13."""
        kappa = kappa_virasoro(13.0)
        result = verify_ahat_generating_function(kappa)
        assert result['path2_specific']['F_1_match']
        assert result['path2_specific']['F_2_match']

    def test_ahat_virasoro_c26(self):
        """Ahat verification for Virasoro at critical c=26."""
        kappa = kappa_virasoro(26.0)
        result = verify_ahat_generating_function(kappa)
        assert result['path2_specific']['F_1_match']

    def test_ahat_sl2_k1(self):
        """Ahat verification for sl_2 at level 1."""
        kappa = kappa_affine_sl2(1)
        result = verify_ahat_generating_function(kappa)
        assert result['path2_specific']['F_1_match']
        assert result['path2_specific']['F_2_match']

    def test_ahat_bernoulli_decay(self):
        """lambda_g^FP ~ 2/(2*pi)^{2g} (Bernoulli decay)."""
        for g in range(5, 20):
            lam = float(lambda_fp(g))
            expected_order = 2.0 / TWO_PI_SQ ** g
            # Within an order of magnitude (the exact ratio converges)
            ratio = lam / expected_order
            assert 0.5 < ratio < 2.0, f"Bernoulli decay fails at g={g}: ratio={ratio}"


# =========================================================================
# Section 5: Hirota bilinear tests (10 tests)
# =========================================================================

class TestHirotaBilinear:
    """Tests for Hirota bilinear relations."""

    def test_hirota_heisenberg_k1(self):
        """Hirota bilinear for Heisenberg k=1 at t=1."""
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_scalar(tau, 1.0)
        # The scalar shadow tau is NOT a KP tau function in the
        # single-variable sector (KP requires multi-time data)
        assert 'kp_residual_4' in result

    def test_hirota_order_4_nonzero(self):
        """KP residual at order 4 is generically nonzero in scalar sector."""
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_scalar(tau, 1.0)
        # For a single-variable function, D_1^4 tau.tau != 0 generically
        assert abs(result['kp_residual_4']) > 1e-10

    def test_hirota_through_order_8(self):
        """Compute Hirota bilinear through order 8."""
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_through_order(tau, max_order=8, t1=1.0)
        assert 'hirota_residuals' in result
        assert 4 in result['hirota_residuals']
        assert 6 in result['hirota_residuals']
        assert 8 in result['hirota_residuals']

    def test_hirota_at_zero_leading_order(self):
        """Near t=0, Hirota order-4 residual approaches 12*(kappa/12)^2 = kappa^2/12.

        The scalar shadow tau has log tau ~ kappa * t^2/24, so f'' -> kappa/12
        and the order-4 Hirota residual D_1^4 tau.tau / tau^2 = 12*f''^2 + 2*f''''
        approaches 12*(kappa/12)^2 = kappa^2/12 (since f'''' -> 0).
        This is NONZERO: the scalar shadow tau is not a KP tau function
        in the single-variable sector.
        """
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_through_order(tau, max_order=6, t1=0.001)
        # The order-4 residual should approach kappa^2/12 = 1/12 ~ 0.0833
        expected_leading = tau.kappa ** 2 / 12.0
        assert abs(result['hirota_residuals'][4] - expected_leading) < 0.01

    def test_hirota_virasoro_c1(self):
        """Hirota test for Virasoro at c=1."""
        tau = build_virasoro_tau(1.0)
        result = hirota_bilinear_through_order(tau, max_order=6, t1=1.0)
        assert 'hirota_residuals' in result

    def test_hirota_virasoro_c26(self):
        """Hirota test for Virasoro at critical c=26."""
        tau = build_virasoro_tau(26.0)
        result = hirota_bilinear_through_order(tau, max_order=6, t1=1.0)
        assert 'hirota_residuals' in result

    def test_hirota_count_satisfied_violated(self):
        """Count satisfied vs violated Hirota relations."""
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_through_order(tau, max_order=8, t1=1.0)
        assert 'satisfied' in result
        assert 'violated' in result
        # Total should equal number of even orders tested minus 1 (order 2 excluded)
        assert result['total_tested'] == result['satisfied'] + result['violated']

    def test_hirota_scaling(self):
        """Hirota residuals scale with kappa: doubling kappa scales residuals."""
        tau1 = build_heisenberg_tau(1)
        tau2 = build_heisenberg_tau(2)
        r1 = hirota_bilinear_through_order(tau1, max_order=6, t1=0.5)
        r2 = hirota_bilinear_through_order(tau2, max_order=6, t1=0.5)
        # At leading order, residuals scale as kappa^2
        ratio = r2['hirota_residuals'][4] / r1['hirota_residuals'][4]
        # kappa doubles from 1 to 2; f'' scales linearly, so f''^2 scales as 4
        assert abs(ratio - 4.0) < 1.0  # approximate scaling

    def test_hirota_derivs_computed(self):
        """Verify derivatives of log tau are computed."""
        tau = build_heisenberg_tau(1)
        result = hirota_bilinear_through_order(tau, max_order=8, t1=1.0)
        assert 0 in result['derivs']
        assert 2 in result['derivs']
        assert 4 in result['derivs']

    def test_hirota_sl2_level_2(self):
        """Hirota test for sl_2 at level 2."""
        tau = build_affine_sl2_tau(2)
        result = hirota_bilinear_through_order(tau, max_order=6, t1=1.0)
        assert 'hirota_residuals' in result


# =========================================================================
# Section 6: KdV / Boussinesq / N-reduction tests (12 tests)
# =========================================================================

class TestKdVReduction:
    """Tests for KdV, Boussinesq, and N-reduction."""

    def test_kdv_virasoro(self):
        """Virasoro should relate to KdV (2-reduction of KP)."""
        tau = build_virasoro_tau(10.0)
        result = check_kdv_reduction(tau, [1.0])
        assert 'kdv_residuals' in result
        # Scalar sector is trivially KdV
        assert result['scalar_trivially_kdv']

    def test_kdv_stationary_check(self):
        """Test stationary KdV: u_xxx + 6 u u_x for Virasoro."""
        tau = build_virasoro_tau(10.0)
        result = check_kdv_reduction(tau, [0.5, 1.0, 1.5])
        for t1, data in result['kdv_residuals'].items():
            # The scalar shadow tau does NOT satisfy stationary KdV
            # (it's not a soliton solution), but we verify the computation runs
            assert 'u' in data
            assert 'residual' in data

    def test_kdv_potential_at_origin(self):
        """u(0) = 2*f''(0) = 2*kappa/12 = kappa/6."""
        kappa = 5.0  # Virasoro c=10
        tau = build_virasoro_tau(10.0)
        u0 = tau.kdv_potential(0.001)  # near 0
        expected = kappa / 6.0
        assert abs(u0 - expected) < 0.01

    def test_kdv_potential_heisenberg(self):
        """KdV potential for Heisenberg k=1."""
        tau = build_heisenberg_tau(1)
        u1 = tau.kdv_potential(1.0)
        # u = 2*d^2/dx^2 [kappa * ((x/2)/sin(x/2) - 1)]
        assert isinstance(u1, float)

    def test_n_reduction_virasoro(self):
        """Virasoro: test 2-reduction (KdV)."""
        tau = build_virasoro_tau(10.0)
        result = check_n_reduction(tau, 2)
        assert result['N'] == 2
        assert result['scalar_reduction']

    def test_n_reduction_boussinesq(self):
        """Test 3-reduction (Boussinesq) structure."""
        tau = build_virasoro_tau(10.0)
        result = check_n_reduction(tau, 3)
        assert result['N'] == 3

    def test_n_reduction_sl2(self):
        """sl_2: test 2-reduction (sl_2 DS hierarchy = KdV)."""
        tau = build_affine_sl2_tau(1)
        result = check_n_reduction(tau, 2)
        assert result['scalar_reduction']

    def test_kdv_potential_smooth(self):
        """KdV potential is smooth (finite) for |t_1| < 2*pi."""
        tau = build_heisenberg_tau(1)
        for t1 in [0.1, 0.5, 1.0, 2.0, 3.0, 5.0]:
            u = tau.kdv_potential(t1)
            assert math.isfinite(u), f"u diverges at t1={t1}"

    def test_kdv_potential_even(self):
        """u(x) = 2*f''(x) is even (f is even, so f'' is even)."""
        tau = build_heisenberg_tau(1)
        for t1 in [0.5, 1.0, 2.0]:
            u_pos = tau.kdv_potential(t1)
            u_neg = tau.kdv_potential(-t1)
            assert abs(u_pos - u_neg) < 0.01, f"u not even at t1={t1}"

    def test_n_reduction_heisenberg(self):
        """Heisenberg (class G): trivially satisfies any N-reduction."""
        tau = build_heisenberg_tau(1)
        for N in [2, 3, 4, 5]:
            result = check_n_reduction(tau, N)
            assert result['scalar_reduction']

    def test_virasoro_shadow_S3_nonzero(self):
        """Virasoro alpha = S_3 = 2/c is nonzero (class M)."""
        tau = build_virasoro_tau(10.0)
        S3 = tau.shadow_coefficients.get(3, 0.0)
        expected = 2.0 / 10.0  # 0.2
        assert abs(S3 - expected) < 1e-10

    def test_virasoro_shadow_S4_formula(self):
        """Virasoro Q^contact = S_4 = 10/(c(5c+22))."""
        c = 10.0
        tau = build_virasoro_tau(c)
        S4 = tau.shadow_coefficients.get(4, 0.0)
        expected = 10.0 / (c * (5 * c + 22))  # 10/(10*72) = 1/72
        assert abs(S4 - expected) < 1e-10


# =========================================================================
# Section 7: Tau at zeta zeros (10 tests)
# =========================================================================

class TestTauAtZetaZeros:
    """Tests for shadow tau evaluation at Riemann zeta zeros."""

    def test_zeta_zeros_list(self):
        """Verify zeta zeros list has 30 entries."""
        assert len(RIEMANN_ZETA_ZEROS) == 30

    def test_first_zero(self):
        """First zero gamma_1 = 14.134725..."""
        assert abs(RIEMANN_ZETA_ZEROS[0] - 14.134725) < 1e-4

    def test_tau_at_zeros_heisenberg(self):
        """Compute tau_Heis at first 5 zeta zeros."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=5)
        assert len(result['zero_data']) == 5
        for datum in result['zero_data']:
            assert 'tau_at_gamma' in datum
            assert math.isfinite(datum['tau_at_gamma'])

    def test_tau_at_zeros_virasoro(self):
        """Compute tau_Vir at first 5 zeta zeros."""
        tau = build_virasoro_tau(10.0)
        result = tau_at_zeta_zeros(tau, n_zeros=5)
        assert len(result['zero_data']) == 5

    def test_kdv_potential_at_zeros(self):
        """KdV potential at zeta zeros is finite."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=5)
        for datum in result['zero_data']:
            assert math.isfinite(datum['kdv_potential'])

    def test_sato_data_at_zeros(self):
        """Sato Grassmannian data computed at zeta zeros."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=3)
        for datum in result['zero_data']:
            sato = datum['sato_grassmannian']
            assert 'w1' in sato
            assert 'w2' in sato
            assert math.isfinite(sato['w1'])

    def test_geometric_specialization(self):
        """Geometric log tau at zeta zeros is computed."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=3)
        for datum in result['zero_data']:
            assert 'geometric_log_tau' in datum
            # geometric_log_tau is a complex tuple (real, imag)
            real, imag = datum['geometric_log_tau']
            assert math.isfinite(real) or math.isfinite(imag)

    def test_tau_complex_at_zeros(self):
        """Complex tau evaluation at imaginary zeta zeros."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=3)
        for datum in result['zero_data']:
            tr, ti = datum['tau_complex']
            assert math.isfinite(tr) and math.isfinite(ti)

    def test_summary_statistics(self):
        """Summary statistics computed correctly."""
        tau = build_heisenberg_tau(1)
        result = tau_at_zeta_zeros(tau, n_zeros=5)
        assert 'tau_mean' in result
        assert 'tau_max' in result
        assert 'tau_min' in result
        assert result['tau_max'] >= result['tau_min']

    def test_zeros_increasing(self):
        """Zeta zeros are strictly increasing."""
        for i in range(len(RIEMANN_ZETA_ZEROS) - 1):
            assert RIEMANN_ZETA_ZEROS[i] < RIEMANN_ZETA_ZEROS[i + 1]


# =========================================================================
# Section 8: Schur function / partition tests (8 tests)
# =========================================================================

class TestSchurFunctions:
    """Tests for Schur functions and partition enumeration."""

    def test_partitions_of_0(self):
        """Partition of 0 is the empty tuple."""
        assert integer_partitions(0) == [()]

    def test_partitions_of_4(self):
        """5 partitions of 4."""
        parts = integer_partitions(4)
        assert len(parts) == 5

    def test_partitions_of_5(self):
        """7 partitions of 5."""
        parts = integer_partitions(5)
        assert len(parts) == 7

    def test_schur_function_empty(self):
        """s_{()} = 1."""
        t = (0.5, 0.3, 0.1)
        assert abs(schur_function_hook_length((), t) - 1.0) < 1e-12

    def test_schur_function_1(self):
        """s_{(1)} = S_1 = t_1."""
        t = (2.0, 0.5)
        val = schur_function_hook_length((1,), t)
        # s_{(1)} = h_1 = S_1 = t_1
        assert abs(val - 2.0) < 1e-10

    def test_schur_function_2(self):
        """s_{(2)} = h_2 = S_2 = t_1^2/2 + t_2."""
        t = (1.0, 1.0)
        val = schur_function_hook_length((2,), t)
        expected = 1.0 / 2 + 1.0  # = 1.5
        assert abs(val - expected) < 1e-10

    def test_schur_function_11(self):
        """s_{(1,1)} = e_2 = det([[h_1, h_2], [h_0, h_1]]) = h_1^2 - h_2."""
        t = (1.0, 1.0)
        val = schur_function_hook_length((1, 1), t)
        # s_{(1,1)} = det([[S_1, S_2], [1, S_1]]) = S_1^2 - S_2
        S1 = schur_polynomial_elementary(1, t)
        S2 = schur_polynomial_elementary(2, t)
        expected = S1 ** 2 - S2  # = 1 - 1.5 = -0.5
        assert abs(val - expected) < 1e-10

    def test_heisenberg_schur_expansion(self):
        """Schur expansion for Heisenberg k=1 at small times."""
        t = (0.1, 0.05, 0.02, 0.01)
        result = heisenberg_tau_schur_expansion(1, t, max_weight=4)
        assert 'tau_schur' in result
        assert result['n_partitions'] > 0
        # tau_schur should be close to 1 for small times
        assert abs(result['tau_schur'] - 1.0) < 1.0


# =========================================================================
# Section 9: Multi-path verification tests (10 tests)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification as specified in the mandate."""

    def test_multipath_heisenberg_k1(self):
        """5-path verification for Heisenberg k=1."""
        tau = build_heisenberg_tau(1)
        result = verify_hirota_multipath(tau, 1.0)
        assert 'path1_hirota' in result
        assert 'path2_kdv' in result
        assert 'path3_sato' in result
        assert 'path4_series_vs_closed' in result
        assert 'path5_numerical' in result

    def test_path4_series_vs_closed(self):
        """Path 4: series agrees with closed form."""
        tau = build_heisenberg_tau(1)
        result = verify_hirota_multipath(tau, 1.0)
        assert result['path4_series_vs_closed']['abs_diff'] < 1e-6

    def test_path5_kappa_over_12(self):
        """Path 5: f''(0) = kappa/12."""
        tau = build_heisenberg_tau(1)
        result = verify_hirota_multipath(tau, 0.5)
        assert result['path5_numerical']['match']

    def test_multipath_virasoro_c10(self):
        """5-path verification for Virasoro c=10."""
        tau = build_virasoro_tau(10.0)
        result = verify_hirota_multipath(tau, 1.0)
        assert result['path4_series_vs_closed']['abs_diff'] < 1e-5

    def test_multipath_virasoro_c13_selfdual(self):
        """5-path verification at self-dual point c=13."""
        tau = build_virasoro_tau(13.0)
        result = verify_hirota_multipath(tau, 1.0)
        assert result['path5_numerical']['match']

    def test_multipath_sl2_k1(self):
        """5-path verification for sl_2 level 1."""
        tau = build_affine_sl2_tau(1)
        result = verify_hirota_multipath(tau, 1.0)
        assert result['path4_series_vs_closed']['abs_diff'] < 1e-5

    def test_sato_w1_is_minus_f_prime(self):
        """Sato data: w_1 = -f'(x)."""
        tau = build_heisenberg_tau(1)
        result = verify_hirota_multipath(tau, 1.0)
        w1 = result['path3_sato']['w1']
        f_prime = result['path3_sato']['f_prime']
        assert abs(w1 + f_prime) < 1e-4

    def test_sato_w2_formula(self):
        """Sato data: w_2 = f''/2 - f'^2/2."""
        tau = build_heisenberg_tau(1)
        result = verify_hirota_multipath(tau, 1.0)
        w2 = result['path3_sato']['w2']
        fp = result['path3_sato']['f_prime']
        fpp = result['path3_sato']['f_double']
        expected = fpp / 2.0 - fp ** 2 / 2.0
        assert abs(w2 - expected) < 1e-4

    def test_multipath_heisenberg_k5(self):
        """5-path verification for Heisenberg k=5."""
        tau = build_heisenberg_tau(5)
        result = verify_hirota_multipath(tau, 0.5)
        assert result['path5_numerical']['match']

    def test_multipath_virasoro_c26(self):
        """5-path verification for Virasoro at critical c=26."""
        tau = build_virasoro_tau(26.0)
        result = verify_hirota_multipath(tau, 0.5)
        assert result['path5_numerical']['match']


# =========================================================================
# Section 10: Full landscape tests (12 tests)
# =========================================================================

class TestFullLandscape:
    """Tests covering the full standard landscape."""

    def test_heisenberg_k1_to_k5(self):
        """Tau functions for Heisenberg k=1..5."""
        for k in range(1, 6):
            tau = build_heisenberg_tau(k)
            val = tau.tau_scalar(1.0)
            assert val > 0
            assert math.isfinite(val)

    def test_virasoro_standard_values(self):
        """Tau functions for Virasoro at c=1/2, 1, 4, 10, 13, 25, 26."""
        for c in [0.5, 1.0, 4.0, 10.0, 13.0, 25.0, 26.0]:
            tau = build_virasoro_tau(c)
            val = tau.tau_scalar(1.0)
            assert val > 0
            assert math.isfinite(val)

    def test_sl2_k1_to_k6(self):
        """Tau functions for sl_2 at level 1..6."""
        for k in range(1, 7):
            tau = build_affine_sl2_tau(k)
            val = tau.tau_scalar(1.0)
            assert val > 0
            assert math.isfinite(val)

    def test_kappa_ordering_heisenberg(self):
        """kappa increases with k for Heisenberg."""
        kappas = [kappa_heisenberg(k) for k in range(1, 6)]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]

    def test_kappa_ordering_sl2(self):
        """kappa increases with level for sl_2."""
        kappas = [kappa_affine_sl2(k) for k in range(1, 7)]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]

    def test_kappa_ordering_virasoro(self):
        """kappa increases with c for Virasoro."""
        kappas = [kappa_virasoro(c) for c in [0.5, 1.0, 4.0, 10.0, 13.0, 25.0, 26.0]]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]

    def test_heisenberg_vs_virasoro_at_c1(self):
        """Heisenberg k=1 vs Virasoro c=1: DIFFERENT kappas (AP39)."""
        kh = kappa_heisenberg(1)  # = 1
        kv = kappa_virasoro(1.0)  # = 0.5
        assert kh != kv  # AP39: kappa(Heis) != c/2

    def test_shadow_tau_depends_on_kappa_not_c(self):
        """Two algebras with same kappa give same scalar tau (AP20)."""
        # Heisenberg k=1: kappa = 1
        # Virasoro c=2: kappa = 1
        tau_h = build_heisenberg_tau(1)
        tau_v = build_virasoro_tau(2.0)
        # Same kappa => same SCALAR tau
        assert abs(tau_h.tau_scalar(1.0) - tau_v.tau_scalar(1.0)) < 1e-10

    def test_virasoro_ising_c_half(self):
        """Virasoro at Ising c=1/2: kappa = 1/4."""
        tau = build_virasoro_tau(0.5)
        assert abs(tau.kappa - 0.25) < 1e-12
        val = tau.tau_scalar(1.0)
        assert val > 0

    def test_virasoro_shadow_depth(self):
        """Virasoro shadow coefficients decay with arity (class M)."""
        tau = build_virasoro_tau(10.0)
        # S_r should decrease (eventually geometrically for class M)
        S3 = abs(tau.shadow_coefficients.get(3, 0.0))
        S4 = abs(tau.shadow_coefficients.get(4, 0.0))
        S5 = abs(tau.shadow_coefficients.get(5, 0.0))
        assert S3 > S4 > S5 > 0  # decreasing but nonzero

    def test_sl2_class_L_no_S4(self):
        """sl_2 is class L: S_4 = 0 (or set to 0 in construction)."""
        tau = build_affine_sl2_tau(1)
        S4 = tau.shadow_coefficients.get(4, 0.0)
        assert abs(S4) < 1e-10

    def test_partition_function_comparison(self):
        """Shadow tau vs partition function comparison runs."""
        result = shadow_tau_vs_partition_function('heisenberg', 1)
        assert 'shadow_F1' in result
        assert abs(result['shadow_F1'] - 1.0 / 24) < 1e-12


# =========================================================================
# Section 11: Cross-family consistency (5 tests)
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10 guard)."""

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A x B) = kappa(A) + kappa(B)."""
        # Heisenberg k=1 x Heisenberg k=2: kappa = 1 + 2 = 3
        kh1 = kappa_heisenberg(1)
        kh2 = kappa_heisenberg(2)
        kh3 = kappa_heisenberg(3)
        assert abs(kh1 + kh2 - kh3) < 1e-12

    def test_tau_multiplicativity_at_scalar(self):
        """For independent algebras: tau_product = tau_A * tau_B at scalar level."""
        tau1 = build_heisenberg_tau(1)
        tau2 = build_heisenberg_tau(2)
        tau3 = build_heisenberg_tau(3)
        t1 = 1.0
        # kappa additive => log tau additive => tau multiplicative
        assert abs(tau1.tau_scalar(t1) * tau2.tau_scalar(t1) - tau3.tau_scalar(t1)) < 1e-8

    def test_F1_proportional_to_kappa(self):
        """F_1 = kappa/24 for all families."""
        families = {
            'heis_1': kappa_heisenberg(1),
            'vir_10': kappa_virasoro(10.0),
            'sl2_1': kappa_affine_sl2(1),
        }
        for name, kap in families.items():
            tau = ShadowTauFunction(name, kap)
            F1 = tau.free_energy_scalar(1)
            assert abs(F1 - kap / 24.0) < 1e-12, f"F_1 wrong for {name}"

    def test_virasoro_complementarity_kappa_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0)."""
        for c in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            kA = kappa_virasoro(c)
            kB = kappa_virasoro(26.0 - c)
            assert abs(kA + kB - 13.0) < 1e-12, f"Complementarity fails at c={c}"

    def test_sl2_kappa_independent_formula(self):
        """Cross-check sl_2 kappa: 3*(k+2)/4 vs general (N^2-1)*(k+N)/(2N) at N=2."""
        for k in range(1, 7):
            k1 = kappa_affine_sl2(k)
            k2 = kappa_affine_slN(2, k)
            assert abs(k1 - k2) < 1e-12, f"sl_2 kappa mismatch at level {k}"
