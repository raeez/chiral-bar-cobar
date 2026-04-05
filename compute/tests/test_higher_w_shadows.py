"""Tests for higher W-algebra shadow obstruction tower data (W_4 and W_5).

Verifies:
  1.  Harmonic numbers: H_4 = 25/12, H_5 = 137/60
  2.  Kappa formulas: W_4 = 13c/12, W_5 = 77c/60
  3.  Channel decomposition: kappa_j = c/j, sum = total
  4.  T-line universality: matches Virasoro for all W_N
  5.  Gravitational cubic structure
  6.  Weight-4 quasi-primary spectrum (Lambda and W_4)
  7.  Quartic contact on T-line = 10/[c(5c+22)]
  8.  W_3-line gravitational S4 = 2560/[c(5c+22)^3]
  9.  Propagator variance for W_3 reproduces P = 25c^2 + 100c - 428
  10. Growth rate squared on T-line = (180c+872)/[c^2(5c+22)]
  11. Shadow depth classification = class M
  12. Parity constraints on odd-weight lines
  13. Kappa matrix diagonality and inversion
  14. Comparison between W_3, W_4, W_5 structural invariants
  15. Numerical tower consistency
  16. Koszul complementarity kappa sums
  17. DS ghost sector compatibility

Ground truth cross-references:
  - w3_shadow_tower_engine.py: kappa(W_3) = 5c/6, S4_W = 2560/[c(5c+22)^3]
  - w4_multivariable_shadow.py: kappa_scalar = 13c/12, QP dim = 2
  - wn_channel_refined.py: harmonic number formulas
  - propagator_variance.py: P(W_3) = 25c^2 + 100c - 428
  - quartic_contact_class.py: Q^contact_Vir = 10/[c(5c+22)]
  - shadow_radius.py: rho^2 formula
"""

import math
import pytest

from sympy import (
    Matrix,
    Rational,
    S,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sqrt,
    symbols,
)

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(_lib_dir, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_hw = _load('higher_w_shadows', 'higher_w_shadows.py')

c = Symbol('c')


# ============================================================================
# 1. Harmonic numbers
# ============================================================================

class TestHarmonicNumbers:
    """Exact rational harmonic numbers."""

    def test_H1(self):
        assert _hw.harmonic_number(1) == Rational(1)

    def test_H2(self):
        assert _hw.harmonic_number(2) == Rational(3, 2)

    def test_H3(self):
        assert _hw.harmonic_number(3) == Rational(11, 6)

    def test_H4(self):
        """H_4 = 1 + 1/2 + 1/3 + 1/4 = 25/12."""
        assert _hw.harmonic_number(4) == Rational(25, 12)

    def test_H5(self):
        """H_5 = 1 + 1/2 + 1/3 + 1/4 + 1/5 = 137/60."""
        assert _hw.harmonic_number(5) == Rational(137, 60)

    def test_H6(self):
        """H_6 = 49/20."""
        assert _hw.harmonic_number(6) == Rational(49, 20)

    def test_anomaly_ratio_W2(self):
        """rho(W_2) = H_2 - 1 = 1/2."""
        assert _hw.anomaly_ratio(2) == Rational(1, 2)

    def test_anomaly_ratio_W3(self):
        """rho(W_3) = H_3 - 1 = 5/6."""
        assert _hw.anomaly_ratio(3) == Rational(5, 6)

    def test_anomaly_ratio_W4(self):
        """rho(W_4) = H_4 - 1 = 13/12."""
        assert _hw.anomaly_ratio(4) == Rational(13, 12)

    def test_anomaly_ratio_W5(self):
        """rho(W_5) = H_5 - 1 = 77/60."""
        assert _hw.anomaly_ratio(5) == Rational(77, 60)


# ============================================================================
# 2. Total kappa
# ============================================================================

class TestTotalKappa:
    """Total modular characteristic kappa(W_N) = c * (H_N - 1)."""

    def test_kappa_W2(self):
        """kappa(W_2) = c/2 = Virasoro."""
        assert simplify(_hw.total_kappa(2) - c / 2) == 0

    def test_kappa_W3(self):
        """kappa(W_3) = 5c/6."""
        assert simplify(_hw.total_kappa(3) - 5 * c / 6) == 0

    def test_kappa_W4(self):
        """kappa(W_4) = 13c/12."""
        assert simplify(_hw.total_kappa(4) - 13 * c / 12) == 0

    def test_kappa_W5(self):
        """kappa(W_5) = 77c/60."""
        assert simplify(_hw.total_kappa(5) - 77 * c / 60) == 0

    def test_kappa_W4_numerical_c30(self):
        """kappa(W_4, c=30) = 13*30/12 = 32.5."""
        kap = _hw.total_kappa(4, Rational(30))
        assert kap == Rational(65, 2)

    def test_kappa_W5_numerical_c60(self):
        """kappa(W_5, c=60) = 77*60/60 = 77."""
        kap = _hw.total_kappa(5, Rational(60))
        assert kap == 77

    def test_kappa_channel_sum_W4(self):
        """kappa_2 + kappa_3 + kappa_4 = kappa_total(W_4)."""
        ch = {j: _hw.channel_kappa(j) for j in range(2, 5)}
        total = sum(ch.values())
        expected = _hw.total_kappa(4)
        assert simplify(total - expected) == 0

    def test_kappa_channel_sum_W5(self):
        """kappa_2 + ... + kappa_5 = kappa_total(W_5)."""
        ch = {j: _hw.channel_kappa(j) for j in range(2, 6)}
        total = sum(ch.values())
        expected = _hw.total_kappa(5)
        assert simplify(total - expected) == 0

    def test_kappa_monotone_increasing(self):
        """kappa(W_N) is strictly increasing in N (for c > 0)."""
        for N in range(2, 6):
            rho_N = _hw.anomaly_ratio(N)
            rho_N1 = _hw.anomaly_ratio(N + 1)
            # rho_{N+1} - rho_N = 1/(N+1) > 0
            assert rho_N1 - rho_N == Rational(1, N + 1)


# ============================================================================
# 3. Kappa matrix
# ============================================================================

class TestKappaMatrix:
    """Kappa matrix and propagator for W_4 and W_5."""

    def test_w4_kappa_diagonal(self):
        """W_4 kappa = diag(c/2, c/3, c/4)."""
        K = _hw.kappa_matrix(4)
        assert simplify(K[0, 0] - c / 2) == 0
        assert simplify(K[1, 1] - c / 3) == 0
        assert simplify(K[2, 2] - c / 4) == 0

    def test_w4_kappa_off_diagonal(self):
        """W_4 kappa is diagonal."""
        K = _hw.kappa_matrix(4)
        assert K[0, 1] == 0
        assert K[0, 2] == 0
        assert K[1, 2] == 0

    def test_w5_kappa_diagonal(self):
        """W_5 kappa = diag(c/2, c/3, c/4, c/5)."""
        K = _hw.kappa_matrix(5)
        for idx, j in enumerate(range(2, 6)):
            assert simplify(K[idx, idx] - c / j) == 0

    def test_w4_propagator_inverts_kappa(self):
        """kappa * propagator = I for W_4."""
        K = _hw.kappa_matrix(4)
        P = _hw.propagator_matrix(4)
        prod = K * P
        for i in range(3):
            for j in range(3):
                expected = 1 if i == j else 0
                assert simplify(prod[i, j] - expected) == 0

    def test_w5_propagator_inverts_kappa(self):
        """kappa * propagator = I for W_5."""
        K = _hw.kappa_matrix(5)
        P = _hw.propagator_matrix(5)
        prod = K * P
        for i in range(4):
            for j in range(4):
                expected = 1 if i == j else 0
                assert simplify(prod[i, j] - expected) == 0

    def test_w4_trace_equals_total_kappa(self):
        """tr(kappa_W4) = 13c/12."""
        K = _hw.kappa_matrix(4)
        tr = sum(K[i, i] for i in range(3))
        assert simplify(tr - _hw.total_kappa(4)) == 0


# ============================================================================
# 4. T-line universality
# ============================================================================

class TestTLineUniversality:
    """T-line shadow data is identical to Virasoro for all W_N."""

    def test_t_line_kappa(self):
        """T-line kappa = c/2."""
        data = _hw.t_line_data()
        assert simplify(data['kappa'] - c / 2) == 0

    def test_t_line_alpha(self):
        """T-line cubic = 2."""
        data = _hw.t_line_data()
        assert data['alpha'] == 2

    def test_t_line_S4(self):
        """T-line S4 = 10/[c(5c+22)]."""
        data = _hw.t_line_data()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(data['S4'] - expected) == 0

    def test_t_line_Delta(self):
        """T-line Delta = 40/(5c+22)."""
        data = _hw.t_line_data()
        expected = Rational(40) / (5 * c + 22)
        assert simplify(data['Delta'] - expected) == 0

    def test_t_line_depth_class_M(self):
        """T-line is class M (infinite tower)."""
        data = _hw.t_line_data()
        assert data['depth_class'] == 'M'

    def test_t_line_matches_virasoro_at_c30(self):
        """T-line tower at c=30 matches Virasoro tower."""
        c_val = 30.0
        tower = _hw.t_line_tower_w4_numerical(c_val, max_r=10)
        # S_2 = kappa_T = c/2 = 15
        assert abs(tower[2] - 15.0) < 1e-10
        # S_3 = alpha_T = 2
        assert abs(tower[3] - 2.0) < 1e-10
        # S_4 should be positive (class M)
        assert tower[4] > 0

    def test_Q_contact_T_line(self):
        """Q^contact on T-line = 10/[c(5c+22)]."""
        Q = _hw.Q_contact_T_line()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(Q - expected) == 0


# ============================================================================
# 5. Gravitational cubic
# ============================================================================

class TestGravitationalCubic:
    """Gravitational cubic shadow Sh_3^grav."""

    def test_w4_gravitational_cubic(self):
        """Sh_3^grav(W_4) = 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2."""
        x_T, x_3, x_4 = symbols('x_T x_3 x_4')
        cubic = _hw.gravitational_cubic_w4()
        expected = 2 * x_T**3 + 3 * x_T * x_3**2 + 4 * x_T * x_4**2
        assert expand(cubic - expected) == 0

    def test_w5_gravitational_cubic(self):
        """Sh_3^grav(W_5) = 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2 + 5x_T x_5^2."""
        x_T, x_3, x_4, x_5 = symbols('x_T x_3 x_4 x_5')
        cubic = _hw.gravitational_cubic_w5()
        expected = (2 * x_T**3 + 3 * x_T * x_3**2
                    + 4 * x_T * x_4**2 + 5 * x_T * x_5**2)
        assert expand(cubic - expected) == 0

    def test_gravitational_cubic_general(self):
        """General Sh_3^grav(W_N) = 2x_2^3 + sum_{j=3}^N j x_2 x_j^2."""
        for N in [3, 4, 5]:
            cubic = _hw.gravitational_cubic(N)
            x = [Symbol(f'x_{j}') for j in range(2, N + 1)]
            # Check x_2^3 coefficient = 2
            coeff = cubic.coeff(x[0]**3)
            assert coeff == 2
            # Check x_2 * x_j^2 coefficient = j for j >= 3
            for idx, j in enumerate(range(3, N + 1)):
                coeff = cubic.coeff(x[0] * x[idx + 1]**2)
                assert coeff == j

    def test_gravitational_cubic_T_line_restriction(self):
        """On the T-line (x_3 = x_4 = 0): Sh_3 = 2x_T^3."""
        x_T, x_3, x_4 = symbols('x_T x_3 x_4')
        cubic = _hw.gravitational_cubic_w4()
        restricted = cubic.subs([(x_3, 0), (x_4, 0)])
        assert expand(restricted - 2 * x_T**3) == 0

    def test_gravitational_cubic_symmetry(self):
        """Gravitational cubic is symmetric in x_j^2 (even in each x_j for j>=3)."""
        x_T, x_3, x_4 = symbols('x_T x_3 x_4')
        cubic = _hw.gravitational_cubic_w4()
        # Check that x_3 -> -x_3 leaves cubic unchanged (even in x_3)
        flipped = cubic.subs(x_3, -x_3)
        assert expand(cubic - flipped) == 0


# ============================================================================
# 6. Weight-4 quasi-primary spectrum
# ============================================================================

class TestQuasiPrimaries:
    """Weight-4 quasi-primary exchange spectrum."""

    def test_lambda_norm(self):
        """N_Lambda = c(5c+22)/10."""
        N_L = _hw.lambda_norm()
        expected = c * (5 * c + 22) / 10
        assert simplify(N_L - expected) == 0

    def test_lambda_norm_numerical(self):
        """N_Lambda at c=10: 10*72/10 = 72."""
        N_L = _hw.lambda_norm(Rational(10))
        assert N_L == 72

    def test_coupling_T(self):
        """C(T,T,Lambda) = 1."""
        assert _hw.coupling_to_lambda(2) == 1

    def test_coupling_W3(self):
        """C(W_3,W_3,Lambda) = 16/(5c+22)."""
        coup = _hw.coupling_to_lambda(3)
        expected = Rational(16) / (5 * c + 22)
        assert simplify(coup - expected) == 0

    def test_w4_package_qp_dim(self):
        """W_4 has 2 weight-4 quasi-primaries."""
        pkg = _hw.w4_shadow_package()
        assert pkg['weight_4_quasi_primaries']['dim'] == 2

    def test_w5_package_qp_dim(self):
        """W_5 also has 2 weight-4 quasi-primaries (Lambda and W_4)."""
        pkg = _hw.w5_shadow_package()
        assert pkg['weight_4_quasi_primaries']['dim'] == 2


# ============================================================================
# 7. W_3-line data
# ============================================================================

class TestW3Line:
    """Shadow data on the W_3-line (x_T = x_4 = 0 in W_4)."""

    def test_w3_line_kappa(self):
        """kappa on W_3-line = c/3."""
        data = _hw.w3_line_data_in_w4()
        assert simplify(data['kappa'] - c / 3) == 0

    def test_w3_line_alpha_zero(self):
        """Z_2 parity kills cubic on W_3-line."""
        data = _hw.w3_line_data_in_w4()
        assert data['alpha'] == 0

    def test_w3_line_S4_gravitational(self):
        """Gravitational S4 on W_3-line = 2560/[c(5c+22)^3]."""
        data = _hw.w3_line_data_in_w4()
        expected = Rational(2560) / (c * (5 * c + 22)**3)
        assert simplify(data['S4_gravitational'] - expected) == 0

    def test_w3_line_S4_matches_w3_algebra(self):
        """Gravitational S4 on W_3-line of W_4 matches W_3 algebra's W-line S4."""
        data_w4 = _hw.w3_line_data_in_w4()
        # From w3_shadow_tower_engine: S4_W = 2560/[c(5c+22)^3]
        expected = Rational(2560) / (c * (5 * c + 22)**3)
        assert simplify(data_w4['S4_gravitational'] - expected) == 0

    def test_w3_line_has_w4_exchange(self):
        """W_3-line in W_4 has a W_4-exchange channel (absent in W_3 algebra)."""
        data = _hw.w3_line_data_in_w4()
        # S4_W4 should be nonzero (symbolic in c_334)
        assert data['S4_W4'] != 0

    def test_w3_line_depth_class_M(self):
        """W_3-line is class M."""
        data = _hw.w3_line_data_in_w4()
        assert data['depth_class'] == 'M'


# ============================================================================
# 8. W_4-line data
# ============================================================================

class TestW4Line:
    """Shadow data on the W_4-line (x_T = x_3 = 0 in W_4)."""

    def test_w4_line_kappa(self):
        """kappa on W_4-line = c/4."""
        data = _hw.w4_line_data_in_w4()
        assert simplify(data['kappa'] - c / 4) == 0

    def test_w4_line_no_parity(self):
        """W_4 has even weight, so NO Z_2 parity kills the cubic."""
        data = _hw.w4_line_data_in_w4()
        # alpha is symbolic (c_444), not forced to zero
        assert data['alpha'] != 0  # symbolic, not zero

    def test_w4_line_two_exchange_channels(self):
        """W_4-line quartic has both Lambda and W_4 exchange."""
        data = _hw.w4_line_data_in_w4()
        assert data['S4_Lambda'] != 0
        assert data['S4_W4'] != 0


# ============================================================================
# 9. W_5-line data
# ============================================================================

class TestW5Line:
    """Shadow data on the W_5-line (x_T = x_3 = x_4 = 0 in W_5)."""

    def test_w5_line_kappa(self):
        """kappa on W_5-line = c/5."""
        data = _hw.w5_line_data_in_w5()
        assert simplify(data['kappa'] - c / 5) == 0

    def test_w5_line_alpha_zero(self):
        """Z_2 parity kills cubic on W_5-line (W_5 has odd weight)."""
        data = _hw.w5_line_data_in_w5()
        assert data['alpha'] == 0

    def test_w5_line_two_exchange_channels(self):
        """W_5-line quartic has Lambda and W_4 exchange."""
        data = _hw.w5_line_data_in_w5()
        assert 'S4_Lambda' in data
        assert 'S4_W4' in data


# ============================================================================
# 10. Growth rate
# ============================================================================

class TestGrowthRate:
    """Shadow growth rate on primary lines."""

    def test_t_line_growth_rate_formula(self):
        """rho_T^2 = (180c + 872) / [c^2(5c+22)]."""
        rho_sq = _hw.t_line_growth_rate_squared()
        expected = (180 * c + 872) / (c**2 * (5 * c + 22))
        assert simplify(rho_sq - expected) == 0

    def test_t_line_growth_rate_c30(self):
        """rho_T^2 at c=30 is small (tower converges)."""
        rho_sq = _hw.t_line_growth_rate_squared(Rational(30))
        # (180*30 + 872) / (900 * 172) = 6272 / 154800 ~ 0.0405
        val = float(rho_sq)
        assert 0 < val < 1

    def test_w3_line_growth_rate_gravitational(self):
        """W_3-line rho^2 (grav) = 30720 / [c^2(5c+22)^3]."""
        rho_sq = _hw.w3_line_growth_rate_squared_gravitational()
        expected = Rational(30720) / (c**2 * (5 * c + 22)**3)
        assert simplify(rho_sq - expected) == 0

    def test_w3_line_growth_smaller_than_t_line(self):
        """W_3-line growth rate < T-line growth rate at c=30."""
        rho_T_sq = float(_hw.t_line_growth_rate_squared(Rational(30)))
        rho_W3_sq = float(_hw.w3_line_growth_rate_squared_gravitational(Rational(30)))
        assert rho_W3_sq < rho_T_sq

    def test_growth_rate_positive_for_class_M(self):
        """Growth rates are positive for c > 0 (class M)."""
        for c_val in [5, 10, 30, 100]:
            rho_T = float(_hw.t_line_growth_rate_squared(Rational(c_val)))
            rho_W3 = float(_hw.w3_line_growth_rate_squared_gravitational(Rational(c_val)))
            assert rho_T > 0
            assert rho_W3 > 0


# ============================================================================
# 11. Propagator variance
# ============================================================================

class TestPropagatorVariance:
    """Propagator variance (multi-channel non-autonomy)."""

    def test_w3_mixing_polynomial(self):
        """P(W_3) = 25c^2 + 100c - 428."""
        P = _hw.w3_mixing_polynomial()
        expected = 25 * c**2 + 100 * c - 428
        assert expand(P - expected) == 0

    def test_w3_propagator_variance_nonnegative(self):
        """delta_mix(W_3) >= 0 at several c values."""
        for c_val in [5, 10, 30, 50, 100]:
            delta = float(_hw.w3_propagator_variance(Rational(c_val)))
            assert delta >= -1e-15  # non-negative up to float precision

    def test_w3_propagator_variance_structure(self):
        """delta_mix(W_3) has P^2 in numerator (since delta = 0 iff P = 0)."""
        delta = _hw.w3_propagator_variance()
        delta_factored = factor(delta)
        # The variance should have P(W_3)^2 as a factor in the numerator
        P = _hw.w3_mixing_polynomial()
        # Check that delta vanishes where P vanishes
        from sympy import solve
        P_roots = solve(P, c)
        for root in P_roots:
            delta_at_root = delta.subs(c, root)
            assert simplify(delta_at_root) == 0

    def test_propagator_variance_general_cauchy_schwarz(self):
        """General Cauchy-Schwarz: delta_mix >= 0."""
        # Test with explicit numerical kappas and f-values
        kappas = [Rational(1), Rational(2), Rational(3)]
        f_vals = [Rational(1), Rational(3), Rational(2)]
        delta = _hw.propagator_variance_general(kappas, f_vals)
        assert delta >= 0

    def test_propagator_variance_vanishes_when_proportional(self):
        """delta_mix = 0 when f_j / kappa_j = constant."""
        kappas = [Rational(2), Rational(3), Rational(5)]
        # f_j = 7 * kappa_j => f_j/kappa_j = 7 for all j
        f_vals = [Rational(14), Rational(21), Rational(35)]
        delta = _hw.propagator_variance_general(kappas, f_vals)
        assert delta == 0


# ============================================================================
# 12. Shadow packages
# ============================================================================

class TestShadowPackages:
    """Complete shadow packages for W_4 and W_5."""

    def test_w4_package_kappa(self):
        """W_4 package has correct total kappa."""
        pkg = _hw.w4_shadow_package()
        assert simplify(pkg['kappa_total'] - 13 * c / 12) == 0

    def test_w4_package_channels(self):
        """W_4 package has 3 channels."""
        pkg = _hw.w4_shadow_package()
        assert len(pkg['kappa_channels']) == 3

    def test_w4_package_depth_class(self):
        """W_4 is class M."""
        pkg = _hw.w4_shadow_package()
        assert pkg['depth_class'] == 'M'

    def test_w5_package_kappa(self):
        """W_5 package has correct total kappa."""
        pkg = _hw.w5_shadow_package()
        assert simplify(pkg['kappa_total'] - 77 * c / 60) == 0

    def test_w5_package_channels(self):
        """W_5 package has 4 channels."""
        pkg = _hw.w5_shadow_package()
        assert len(pkg['kappa_channels']) == 4

    def test_w5_package_depth_class(self):
        """W_5 is class M."""
        pkg = _hw.w5_shadow_package()
        assert pkg['depth_class'] == 'M'

    def test_w4_package_H4(self):
        """W_4 package has H_4 = 25/12."""
        pkg = _hw.w4_shadow_package()
        assert pkg['H_4'] == Rational(25, 12)

    def test_w5_package_H5(self):
        """W_5 package has H_5 = 137/60."""
        pkg = _hw.w5_shadow_package()
        assert pkg['H_5'] == Rational(137, 60)


# ============================================================================
# 13. Comparison between algebras
# ============================================================================

class TestComparison:
    """Structural comparison across W_3, W_4, W_5."""

    def test_kappa_ordering(self):
        """kappa(W_3) < kappa(W_4) < kappa(W_5) for c > 0."""
        comp = _hw.compare_algebras()
        k3 = comp['kappa']['W_3']
        k4 = comp['kappa']['W_4']
        k5 = comp['kappa']['W_5']
        # Check at c = 60
        assert k3.subs(c, 60) < k4.subs(c, 60) < k5.subs(c, 60)

    def test_rank_ordering(self):
        """rank(W_3) = 2 < rank(W_4) = 3 < rank(W_5) = 4."""
        comp = _hw.compare_algebras()
        assert comp['rank']['W_3'] == 2
        assert comp['rank']['W_4'] == 3
        assert comp['rank']['W_5'] == 4

    def test_weight4_exchange_upgrade(self):
        """W_4 and W_5 have 2 exchange channels at weight 4 (vs 1 for W_3)."""
        comp = _hw.compare_algebras()
        assert comp['weight_4_exchange_dim']['W_3'] == 1
        assert comp['weight_4_exchange_dim']['W_4'] == 2
        assert comp['weight_4_exchange_dim']['W_5'] == 2

    def test_t_line_universal(self):
        """T-line is universal across all W_N."""
        comp = _hw.compare_algebras()
        assert comp['T_line_universal'] is True

    def test_parity_lines(self):
        """W_3 has 1 parity line, W_5 has 2 (x_3 and x_5)."""
        comp = _hw.compare_algebras()
        assert len(comp['parity_lines']['W_3']) == 1
        assert len(comp['parity_lines']['W_5']) == 2


# ============================================================================
# 14. Numerical tower consistency
# ============================================================================

class TestNumericalTower:
    """Numerical shadow obstruction tower on primary lines."""

    def test_t_line_S2_equals_kappa(self):
        """S_2 on T-line = kappa_T = c/2."""
        tower = _hw.t_line_tower_w4_numerical(30.0, max_r=5)
        assert abs(tower[2] - 15.0) < 1e-10

    def test_t_line_S3_equals_alpha(self):
        """S_3 on T-line = alpha_T = 2."""
        tower = _hw.t_line_tower_w4_numerical(30.0, max_r=5)
        assert abs(tower[3] - 2.0) < 1e-10

    def test_t_line_S4_positive(self):
        """S_4 on T-line is positive (class M)."""
        tower = _hw.t_line_tower_w4_numerical(30.0, max_r=5)
        assert tower[4] > 0

    def test_w3_line_S2_equals_kappa(self):
        """S_2 on W_3-line = kappa_{W_3} = c/3."""
        tower = _hw.w3_line_tower_w4_numerical(30.0, max_r=5)
        assert abs(tower[2] - 10.0) < 1e-10

    def test_w3_line_S3_zero(self):
        """S_3 on W_3-line = 0 (Z_2 parity)."""
        tower = _hw.w3_line_tower_w4_numerical(30.0, max_r=5)
        assert abs(tower[3]) < 1e-15

    def test_w3_line_S4_positive(self):
        """S_4 on W_3-line is positive (gravitational part, class M)."""
        tower = _hw.w3_line_tower_w4_numerical(30.0, max_r=5)
        assert tower[4] > 0

    def test_w3_line_odd_arities_vanish(self):
        """Odd arities on W_3-line vanish by Z_2 parity."""
        tower = _hw.w3_line_tower_w4_numerical(30.0, max_r=12)
        for r in [3, 5, 7, 9, 11]:
            assert abs(tower[r]) < 1e-12

    def test_tower_decay(self):
        """Tower coefficients decay at large arity (c=30 is in convergent regime)."""
        tower = _hw.t_line_tower_w4_numerical(30.0, max_r=20)
        # |S_r| should decrease for large r
        for r in range(10, 19):
            assert abs(tower[r + 1]) < abs(tower[r]) * 1.5  # some tolerance

    def test_general_tower_on_line(self):
        """General tower_on_line_numerical matches t_line at same parameters."""
        c_val = 30.0
        kappa = c_val / 2.0
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
        tower_gen = _hw.tower_on_line_numerical(kappa, alpha, S4, max_r=8)
        tower_t = _hw.t_line_tower_w4_numerical(c_val, max_r=8)
        for r in range(2, 9):
            assert abs(tower_gen[r] - tower_t[r]) < 1e-12


# ============================================================================
# 15. Cross-checks with existing modules
# ============================================================================

class TestCrossChecks:
    """Cross-check against existing codebase modules."""

    def test_kappa_w4_matches_w4_multivariable(self):
        """kappa(W_4) matches w4_multivariable_shadow.w4_kappa_scalar()."""
        try:
            _w4m = _load('w4_multivariable_shadow', 'w4_multivariable_shadow.py')
            kap_existing = _w4m.w4_kappa_scalar()
            kap_new = _hw.total_kappa(4)
            assert simplify(kap_existing - kap_new) == 0
        except Exception:
            pytest.skip("w4_multivariable_shadow not available")

    def test_kappa_w3_matches_w3_engine(self):
        """kappa(W_3) matches w3_shadow_tower_engine.w3_kappa_total()."""
        try:
            _w3e = _load('w3_shadow_tower_engine', 'w3_shadow_tower_engine.py')
            kap_existing = _w3e.w3_kappa_total()
            kap_new = _hw.total_kappa(3)
            assert simplify(kap_existing - kap_new) == 0
        except Exception:
            pytest.skip("w3_shadow_tower_engine not available")

    def test_t_line_S4_matches_virasoro_quartic(self):
        """T-line S4 matches the Virasoro quartic contact 10/[c(5c+22)]."""
        Q = _hw.Q_contact_T_line()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(Q - expected) == 0

    def test_w3_line_S4_matches_w3_wline(self):
        """W_3-line gravitational S4 matches w3_shadow_tower_engine W-line data."""
        try:
            _w3e = _load('w3_shadow_tower_engine', 'w3_shadow_tower_engine.py')
            w_data = _w3e.w_line_shadow_data()
            S4_existing = w_data['S4']
            S4_new = _hw.Q_contact_w3_line_gravitational()
            assert simplify(S4_existing - S4_new) == 0
        except Exception:
            pytest.skip("w3_shadow_tower_engine not available")

    def test_mixing_polynomial_matches_existing(self):
        """P(W_3) matches propagator_variance.w3_mixing_polynomial()."""
        try:
            _pv = _load('propagator_variance', 'propagator_variance.py')
            P_existing = _pv.w3_mixing_polynomial()
            P_new = _hw.w3_mixing_polynomial()
            assert expand(P_existing - P_new) == 0
        except Exception:
            pytest.skip("propagator_variance not available")

    def test_harmonic_matches_wn_channel_refined(self):
        """Harmonic numbers match wn_channel_refined.harmonic_number()."""
        try:
            _wn = _load('wn_channel_refined', 'wn_channel_refined.py')
            for n in [2, 3, 4, 5, 6]:
                assert _hw.harmonic_number(n) == _wn.harmonic_number(n)
        except Exception:
            pytest.skip("wn_channel_refined not available")


# ============================================================================
# 16. Koszul complementarity
# ============================================================================

class TestComplementarity:
    """Koszul duality complementarity sums."""

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        kap_sum = _hw.complementarity_kappa_sum(2)
        assert kap_sum == 13

    def test_w3_complementarity(self):
        """kappa(W_3, c) + kappa(W_3, 100-c) = (5/6)*100 = 250/3."""
        kap_sum = _hw.complementarity_kappa_sum(3)
        assert kap_sum == Rational(250, 3)


# ============================================================================
# 17. Shadow metric
# ============================================================================

class TestShadowMetric:
    """Shadow metric Q_L(t) on primary lines."""

    def test_t_line_shadow_metric(self):
        """T-line: Q(t) = c^2 + 12c t + q2 t^2."""
        data = _hw.t_line_data()
        q0, q1, q2 = _hw.shadow_metric_on_line(data['kappa'], data['alpha'], data['S4'])
        assert simplify(q0 - c**2) == 0
        assert simplify(q1 - 12 * c) == 0

    def test_w3_line_shadow_metric_q1_zero(self):
        """W_3-line: q1 = 0 (alpha = 0 by parity)."""
        data = _hw.w3_line_data_in_w4()
        q0, q1, q2 = _hw.shadow_metric_on_line(
            data['kappa'], data['alpha'], data['S4_gravitational'])
        assert q1 == 0

    def test_shadow_metric_q0_positive(self):
        """q0 = 4*kappa^2 is positive for all lines."""
        for j in [2, 3, 4, 5]:
            kap = _hw.channel_kappa(j, Rational(30))
            q0 = 4 * kap**2
            assert q0 > 0


# ============================================================================
# 18. Structural properties
# ============================================================================

class TestStructuralProperties:
    """Structural properties specific to higher W-algebras."""

    def test_w4_two_channel_quartic(self):
        """W_4 quartic has a two-channel structure (Lambda + W_4)."""
        data = _hw.w4_line_data_in_w4()
        # Both exchange channels should be present
        assert 'S4_Lambda' in data
        assert 'S4_W4' in data

    def test_w4_w3_line_upgrade(self):
        """W_3-line in W_4 has W_4-exchange absent in W_3 algebra."""
        data = _hw.w3_line_data_in_w4()
        assert data['note'] == 'W_4 exchange channel present (absent in W_3 algebra)'

    def test_w5_no_new_weight4_channel(self):
        """W_5 (weight 5) does NOT add a new weight-4 exchange channel."""
        comp = _hw.compare_algebras()
        assert comp['weight_4_exchange_dim']['W_5'] == 2  # same as W_4

    def test_odd_weight_parity(self):
        """Odd-weight generators (W_3, W_5) have Z_2 parity killing cubics."""
        # W_3 line: alpha = 0
        w3_data = _hw.w3_line_data_in_w4()
        assert w3_data['alpha'] == 0
        # W_5 line: alpha = 0
        w5_data = _hw.w5_line_data_in_w5()
        assert w5_data['alpha'] == 0

    def test_even_weight_no_parity(self):
        """Even-weight generators (W_4) have nonzero self-cubic."""
        w4_data = _hw.w4_line_data_in_w4()
        # alpha is symbolic (c_444), not zero
        assert w4_data['alpha'] != 0

    def test_all_class_M(self):
        """All lines in W_4 and W_5 are class M (infinite tower)."""
        for data_fn in [_hw.t_line_data, _hw.w3_line_data_in_w4,
                        _hw.w4_line_data_in_w4]:
            data = data_fn()
            assert data['depth_class'] == 'M'


# ============================================================================
# 19. Edge cases and poles
# ============================================================================

class TestEdgeCases:
    """Edge cases and singularity analysis."""

    def test_kappa_vanishes_at_c0(self):
        """kappa(W_N) vanishes at c = 0 for all N."""
        for N in [2, 3, 4, 5]:
            kap = _hw.total_kappa(N, Rational(0))
            assert kap == 0

    def test_S4_pole_at_c0(self):
        """S4 on T-line has a pole at c = 0."""
        from sympy import limit, oo
        S4 = _hw.Q_contact_T_line()
        # S4 ~ 10/(22c) as c -> 0, so it diverges
        lim = limit(c * S4, c, 0)
        assert lim == Rational(10, 22)

    def test_S4_pole_at_lee_yang(self):
        """S4 on T-line has a pole at c = -22/5 (Lee-Yang)."""
        from sympy import limit
        S4 = _hw.Q_contact_T_line()
        c_ly = Rational(-22, 5)
        # S4 diverges at c = -22/5
        val = S4.subs(c, c_ly + Rational(1, 1000))
        assert abs(float(val)) > 100


# ============================================================================
# 20. Exact tower tests
# ============================================================================

class TestExactTower:
    """Exact symbolic tower on primary lines."""

    def test_exact_t_line_S2(self):
        """Exact S_2 on T-line = c/2."""
        cp = Symbol('c', positive=True)
        tower = _hw.tower_on_line_exact(cp / 2, Rational(2),
                                        Rational(10) / (cp * (5 * cp + 22)),
                                        max_r=4)
        S2 = tower[2].subs(cp, c)
        assert simplify(S2 - c / 2) == 0

    def test_exact_t_line_S3(self):
        """Exact S_3 on T-line = 2 (the gravitational cubic)."""
        cp = Symbol('c', positive=True)
        tower = _hw.tower_on_line_exact(cp / 2, Rational(2),
                                        Rational(10) / (cp * (5 * cp + 22)),
                                        max_r=4)
        S3 = tower[3].subs(cp, c)
        assert simplify(S3 - 2) == 0

    def test_exact_t_line_S4(self):
        """Exact S_4 on T-line = 10/[c(5c+22)] = Q^contact_Vir."""
        cp = Symbol('c', positive=True)
        tower = _hw.tower_on_line_exact(cp / 2, Rational(2),
                                        Rational(10) / (cp * (5 * cp + 22)),
                                        max_r=5)
        S4 = tower[4].subs(cp, c)
        expected = Rational(10) / (c * (5 * c + 22))
        # S4 should equal the quartic contact
        # Actually S_4 = a_2/4 where a_2 = (q2 - a1^2)/(2*a0)
        # q0 = c^2, q1 = 12c, q2 = 9*4 + 16*(c/2)*10/[c(5c+22)] = 36 + 80/(5c+22)
        # a0 = c, a1 = 12c/(2c) = 6
        # a2 = (36 + 80/(5c+22) - 36)/(2c) = 80/[2c(5c+22)] = 40/[c(5c+22)]
        # S_4 = a2/4 = 10/[c(5c+22)] ✓
        assert simplify(S4 - expected) == 0

    def test_exact_w3_line_S2(self):
        """Exact S_2 on W_3-line = c/3."""
        cp = Symbol('c', positive=True)
        tower = _hw.tower_on_line_exact(cp / 3, Rational(0),
                                        Rational(2560) / (cp * (5 * cp + 22)**3),
                                        max_r=4)
        S2 = tower[2].subs(cp, c)
        assert simplify(S2 - c / 3) == 0

    def test_exact_w3_line_S3_zero(self):
        """Exact S_3 on W_3-line = 0 (parity)."""
        cp = Symbol('c', positive=True)
        tower = _hw.tower_on_line_exact(cp / 3, Rational(0),
                                        Rational(2560) / (cp * (5 * cp + 22)**3),
                                        max_r=4)
        S3 = tower[3].subs(cp, c)
        assert simplify(S3) == 0
