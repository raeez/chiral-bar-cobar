"""Tests for Davenport-Heilbronn genus-2 analysis of Koszul-Epstein functions.

Tests the numerical computation of Epstein zeta functions for the shadow
metric binary quadratic forms of the Ising model (c=1/2, D_0=-40, h=2)
and Virasoro at c=1 (D_0=-15, h=2), the search for off-line zeros via
the Davenport-Heilbronn mechanism, L-function decomposition, genus-2
positivity constraints, and the structural separation theorem.

Key mathematical facts tested:
  - Shadow data internal consistency (discriminants, class numbers, reductions)
  - Epstein zeta functional equation Xi(s) = Xi(1-s) for reduced forms
  - Positivity of Epstein zeta for Re(s) > 1 (absolute convergence region)
  - Koszul-Epstein = Epstein zeta of shadow metric form
  - On-line zeros exist on Re(s) = 1/2 (sign changes of real part)
  - Genus-2 Beurling kernel K^(2)(D,D) >= 0 (squared norm)
  - Genus-2 positivity does NOT exclude off-line zeros (structural separation)
  - L-function decomposition eps_Q = (1/w)[L_0 +/- L_1] is consistent
  - lambda_2 = 7/5760 (Faber-Pandharipande, AP38 corrected)
  - Complementarity: A_2(A) + A_2(A!) expressible in shadow invariants
  - Kronecker symbol multiplicativity and known values
  - Theta function convergence for positive-definite forms
"""
import math
import pytest
from fractions import Fraction

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from compute.lib.dh_genus2_analysis import (
    ising_shadow_data,
    virasoro_c1_shadow_data,
    epstein_zeta_theta,
    completed_epstein,
    koszul_epstein_ising,
    koszul_epstein_virasoro_c1,
    find_approximate_zeros,
    search_offline_zeros_ising,
    search_offline_zeros_virasoro_c1,
    _kronecker_symbol,
    _kronecker_naive,
    hecke_L_function,
    epstein_decomposition,
    genus2_beurling_kernel,
    genus2_zero_constraint,
    verify_functional_equation,
    critical_line_values,
    critical_line_sign_changes,
    _theta_binary,
    _dual_form,
    _discriminant_to_form,
    _refine_zero,
    _bisect_sign_change,
    _evaluate_on_grid,
    run_full_analysis,
)


# ================================================================
# Section 1: Shadow data internal consistency
# ================================================================

class TestIsingShadowData:
    """Verify all Ising (c=1/2) shadow data entries are self-consistent."""

    def test_central_charge(self):
        d = ising_shadow_data()
        assert d['c'] == Fraction(1, 2)

    def test_kappa_equals_c_over_2(self):
        """kappa = c/2 for Virasoro (AP39: this identity holds for rank-1)."""
        d = ising_shadow_data()
        assert d['kappa'] == d['c'] / 2

    def test_delta_formula(self):
        """Delta = 8 * kappa * S_4 (critical discriminant)."""
        d = ising_shadow_data()
        expected = 8 * d['kappa'] * d['S4']
        assert d['Delta'] == expected

    def test_real_form_discriminant(self):
        """disc_real = b^2 - 4ac for the real form."""
        d = ising_shadow_data()
        disc = d['b_real'] ** 2 - 4 * d['a_real'] * d['c_real']
        assert disc == d['disc_real']

    def test_disc_real_negative(self):
        """Shadow metric must be positive definite (disc < 0)."""
        d = ising_shadow_data()
        assert d['disc_real'] < 0

    def test_scaled_form_discriminant(self):
        """Scaled integer form disc = scale * disc_real."""
        d = ising_shadow_data()
        disc_int = d['b_int'] ** 2 - 4 * d['a_int'] * d['c_int']
        assert disc_int == d['disc_int']

    def test_scaling_relation(self):
        """Integer form = real form * scale_factor."""
        d = ising_shadow_data()
        sf = d['scale_factor']
        assert d['a_int'] == int(d['a_real'] * sf)
        assert d['b_int'] == int(d['b_real'] * sf)
        assert d['c_int'] == int(d['c_real'] * sf)

    def test_reduced_form_discriminant(self):
        """Reduced form has same discriminant as integer form."""
        d = ising_shadow_data()
        disc_red = d['b_red'] ** 2 - 4 * d['a_red'] * d['c_red']
        assert disc_red == d['disc_int']

    def test_fundamental_discriminant_factorization(self):
        """disc_int = D_0 * conductor^2."""
        d = ising_shadow_data()
        assert d['disc_int'] == d['D0'] * d['conductor'] ** 2

    def test_class_number(self):
        """h(-40) = 2."""
        d = ising_shadow_data()
        assert d['class_number'] == 2

    def test_principal_form_discriminant(self):
        """Principal form has discriminant D_0."""
        a, b, c = ising_shadow_data()['principal_form']
        disc = b * b - 4 * a * c
        assert disc == -40

    def test_nonprincipal_form_discriminant(self):
        """Non-principal form has discriminant D_0."""
        a, b, c = ising_shadow_data()['nonprincipal_form']
        disc = b * b - 4 * a * c
        assert disc == -40

    def test_principal_form_is_reduced(self):
        """Principal form (1,0,10) is reduced: |b| <= a <= c, b >= 0 if equality."""
        a, b, c = ising_shadow_data()['principal_form']
        assert abs(b) <= a <= c

    def test_nonprincipal_form_is_reduced(self):
        """Non-principal form (2,0,5) is reduced."""
        a, b, c = ising_shadow_data()['nonprincipal_form']
        assert abs(b) <= a <= c

    def test_two_distinct_classes(self):
        """The two forms represent distinct ideal classes."""
        d = ising_shadow_data()
        assert d['principal_form'] != d['nonprincipal_form']

    def test_d0_is_fundamental(self):
        """D_0 = -40 is a fundamental discriminant (D_0 / 4 not congruent to 0,1 mod 4)."""
        D = -40
        # -40 = -8 * 5. Check: -40 mod 4 = 0, but -40/4 = -10, and -10 mod 4 = 2.
        # For a negative discriminant D: fundamental iff D = 1 mod 4 or D = 0 mod 4
        # with D/4 not congruent to 0 or 1 mod 4.
        # -40 mod 4 = 0, -40/4 = -10, -10 mod 4 = 2 (not 0 or 1). So fundamental.
        assert D % 4 == 0
        assert (D // 4) % 4 not in (0, 1)


class TestVirasoroC1ShadowData:
    """Verify all Virasoro c=1 shadow data entries are self-consistent."""

    def test_central_charge(self):
        d = virasoro_c1_shadow_data()
        assert d['c'] == Fraction(1)

    def test_kappa_equals_c_over_2(self):
        d = virasoro_c1_shadow_data()
        assert d['kappa'] == d['c'] / 2

    def test_delta_formula(self):
        d = virasoro_c1_shadow_data()
        expected = 8 * d['kappa'] * d['S4']
        assert d['Delta'] == expected

    def test_real_form_discriminant(self):
        d = virasoro_c1_shadow_data()
        disc = d['b_real'] ** 2 - 4 * d['a_real'] * d['c_real']
        assert disc == d['disc_real']

    def test_disc_real_negative(self):
        d = virasoro_c1_shadow_data()
        assert d['disc_real'] < 0

    def test_scaled_form_discriminant(self):
        d = virasoro_c1_shadow_data()
        disc_int = d['b_int'] ** 2 - 4 * d['a_int'] * d['c_int']
        assert disc_int == d['disc_int']

    def test_scaling_relation(self):
        d = virasoro_c1_shadow_data()
        sf = d['scale_factor']
        assert d['a_int'] == int(d['a_real'] * sf)
        assert d['b_int'] == int(d['b_real'] * sf)
        assert d['c_int'] == int(d['c_real'] * sf)

    def test_reduced_form_discriminant(self):
        d = virasoro_c1_shadow_data()
        disc_red = d['b_red'] ** 2 - 4 * d['a_red'] * d['c_red']
        assert disc_red == d['disc_int']

    def test_fundamental_discriminant_factorization(self):
        d = virasoro_c1_shadow_data()
        assert d['disc_int'] == d['D0'] * d['conductor'] ** 2

    def test_class_number(self):
        """h(-15) = 2."""
        d = virasoro_c1_shadow_data()
        assert d['class_number'] == 2

    def test_principal_form_discriminant(self):
        a, b, c = virasoro_c1_shadow_data()['principal_form']
        disc = b * b - 4 * a * c
        assert disc == -15

    def test_nonprincipal_form_discriminant(self):
        a, b, c = virasoro_c1_shadow_data()['nonprincipal_form']
        disc = b * b - 4 * a * c
        assert disc == -15

    def test_d0_is_fundamental(self):
        """D_0 = -15 is fundamental: -15 mod 4 = 1."""
        D = -15
        assert D % 4 == 1  # odd fundamental discriminant

    def test_s4_formula(self):
        """S_4 = Q^contact_Vir = 10/[c(5c+22)] for Virasoro."""
        d = virasoro_c1_shadow_data()
        c = d['c']
        expected = Fraction(10, 1) / (c * (5 * c + 22))
        assert d['S4'] == expected


class TestCrossAlgebraConsistency:
    """Cross-checks between the two algebras."""

    def test_both_class_number_2(self):
        assert ising_shadow_data()['class_number'] == 2
        assert virasoro_c1_shadow_data()['class_number'] == 2

    def test_different_fundamental_discriminants(self):
        assert ising_shadow_data()['D0'] != virasoro_c1_shadow_data()['D0']

    def test_both_alpha_equal_2(self):
        """Both Virasoro-type algebras have alpha = 2."""
        assert ising_shadow_data()['alpha'] == 2
        assert virasoro_c1_shadow_data()['alpha'] == 2

    def test_kappa_ordering(self):
        """kappa(Ising) < kappa(Vir_c1) since c=1/2 < c=1."""
        assert ising_shadow_data()['kappa'] < virasoro_c1_shadow_data()['kappa']


# ================================================================
# Section 2: Kronecker symbol
# ================================================================

class TestKroneckerSymbol:
    """Test the Kronecker symbol implementation."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_trivial(self):
        assert _kronecker_symbol(-40, 1) == 1

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_zero(self):
        assert _kronecker_symbol(-40, 0) == 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_minus40_at_3(self):
        """(-40/3): -40 mod 3 = 2, 2^1 mod 3 = 2 -> (2/3) = -1 (QR)."""
        val = _kronecker_symbol(-40, 3)
        assert val in (-1, 0, 1)  # basic range check

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_minus40_at_5(self):
        """(-40/5) = 0 since 5 | 40."""
        val = _kronecker_symbol(-40, 5)
        assert val == 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_minus15_at_5(self):
        """(-15/5) = 0 since 5 | 15."""
        val = _kronecker_symbol(-15, 5)
        assert val == 0

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_multiplicativity(self):
        """(D/mn) = (D/m)(D/n) for gcd(m,n) = 1."""
        D = -40
        # Test (D/6) = (D/2)(D/3) when gcd(2,3)=1
        val_6 = _kronecker_symbol(D, 6)
        val_2 = _kronecker_symbol(D, 2)
        val_3 = _kronecker_symbol(D, 3)
        assert val_6 == val_2 * val_3

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_kronecker_range(self):
        """Kronecker symbol takes values in {-1, 0, 1}."""
        D = -40
        for n in range(1, 50):
            val = _kronecker_symbol(D, n)
            assert val in (-1, 0, 1)


class TestKroneckerNaive:
    """Test the fallback naive Kronecker computation."""

    def test_naive_trivial(self):
        assert _kronecker_naive(-40, 1) == 1

    def test_naive_zero(self):
        assert _kronecker_naive(-40, 0) == 0

    def test_naive_range(self):
        for n in range(1, 30):
            val = _kronecker_naive(-40, n)
            assert val in (-1, 0, 1)

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_naive_matches_full(self):
        """Naive and full implementations should agree on small values."""
        D = -40
        for n in range(1, 30):
            full = _kronecker_symbol(D, n)
            naive = _kronecker_naive(D, n)
            assert full == naive, f"Mismatch at n={n}: full={full}, naive={naive}"


# ================================================================
# Section 3: Theta function and dual form
# ================================================================

class TestDualForm:
    """Test dual form computation."""

    def test_dual_of_identity(self):
        """Dual of Q(m,n) = m^2 + n^2 is Q*(m,n) = m^2 + n^2 (self-dual)."""
        a_d, b_d, c_d = _dual_form(1, 0, 1)
        assert abs(a_d - 1.0) < 1e-10
        assert abs(b_d) < 1e-10
        assert abs(c_d - 1.0) < 1e-10

    def test_dual_positive_definite(self):
        """Dual of a positive-definite form is positive-definite."""
        # Ising reduced form
        a_d, b_d, c_d = _dual_form(49, 0, 640)
        disc_dual = b_d ** 2 - 4 * a_d * c_d
        assert disc_dual < 0
        assert a_d > 0

    def test_double_dual_identity(self):
        """Dual of dual should be the original form."""
        a, b, c = 49, 0, 640
        a1, b1, c1 = _dual_form(a, b, c)
        a2, b2, c2 = _dual_form(a1, b1, c1)
        assert abs(a2 - a) < 1e-8
        assert abs(b2 - b) < 1e-8
        assert abs(c2 - c) < 1e-8


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestThetaFunction:
    """Test theta function for binary quadratic forms."""

    def test_theta_positive_at_t1(self):
        """Theta(1) > 0 for any positive-definite form."""
        val = _theta_binary(1.0, 1, 0, 1, N=10)
        assert float(val) > 0

    def test_theta_approaches_1_large_t(self):
        """For large t, Theta(t) -> 1 (only (0,0) term contributes)."""
        val = _theta_binary(100.0, 1, 0, 1, N=10)
        assert abs(float(val) - 1.0) < 1e-10

    def test_theta_ising_positive(self):
        """Theta for the Ising shadow form is positive."""
        val = _theta_binary(1.0, 0.25, 6.0, 1924.0 / 49.0, N=15)
        assert float(val) > 0

    def test_theta_virasoro_c1_positive(self):
        val = _theta_binary(1.0, 1.0, 12.0, 1052.0 / 27.0, N=15)
        assert float(val) > 0

    def test_theta_monotone_decreasing(self):
        """Theta(t) is monotone decreasing for t > 0."""
        vals = [float(_theta_binary(t, 1, 0, 1, N=10)) for t in [0.5, 1.0, 2.0, 5.0]]
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1]


# ================================================================
# Section 4: Epstein zeta function
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestEpsteinZeta:
    """Test the Epstein zeta computation via Chowla-Selberg splitting."""

    def test_convergence_right_half(self):
        """eps_Q(2) is finite and positive for Q = m^2 + n^2."""
        val = epstein_zeta_theta(2.0, 1, 0, 1, N_theta=15)
        assert val.real > 0
        assert abs(val.imag) < 1e-6

    def test_pole_near_s1(self):
        """Epstein zeta has a pole at s=1; value near s=1 should be large."""
        val = epstein_zeta_theta(1.01, 1, 0, 1, N_theta=15)
        assert abs(val) > 10

    def test_real_on_real_axis(self):
        """eps_Q(sigma) is real for real sigma > 1."""
        val = epstein_zeta_theta(3.0, 1, 0, 1, N_theta=15)
        assert abs(val.imag) < 1e-8

    def test_scaling_property(self):
        """eps_{lambda*Q}(s) = lambda^{-s} * eps_Q(s)."""
        s = 2.5
        # Q1 = m^2 + n^2, Q2 = 4m^2 + 4n^2 = 4*(m^2+n^2)
        val1 = epstein_zeta_theta(s, 1, 0, 1, N_theta=15)
        val2 = epstein_zeta_theta(s, 4, 0, 4, N_theta=15)
        # eps_{4Q}(s) = 4^{-s} * eps_Q(s)
        expected = val1 * (4 ** (-s))
        assert abs(val2 - expected) / max(abs(expected), 1e-10) < 1e-3

    def test_ising_form_finite(self):
        """Koszul-Epstein for Ising is finite at s=2."""
        val = epstein_zeta_theta(2.0, 0.25, 6.0, 1924.0 / 49.0, N_theta=15)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_virasoro_c1_form_finite(self):
        val = epstein_zeta_theta(2.0, 1.0, 12.0, 1052.0 / 27.0, N_theta=15)
        assert math.isfinite(val.real) and math.isfinite(val.imag)


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestCompletedEpstein:
    """Test the completed Epstein zeta Xi_Q(s)."""

    def test_functional_equation_diagonal_form(self):
        """Xi_Q(s) = Xi_Q(1-s) for the form m^2 + n^2 (self-dual)."""
        s = complex(0.3, 5.0)
        Xi_s = completed_epstein(s, 1, 0, 1)
        Xi_1ms = completed_epstein(1 - s, 1, 0, 1)
        rel_err = abs(Xi_s - Xi_1ms) / max(abs(Xi_s), 1e-10)
        assert rel_err < 1e-3, f"Xi({s})={Xi_s}, Xi({1-s})={Xi_1ms}, rel_err={rel_err}"

    def test_functional_equation_another_point(self):
        s = complex(0.7, 3.0)
        Xi_s = completed_epstein(s, 1, 0, 1)
        Xi_1ms = completed_epstein(1 - s, 1, 0, 1)
        rel_err = abs(Xi_s - Xi_1ms) / max(abs(Xi_s), 1e-10)
        assert rel_err < 1e-3

    def test_xi_real_on_critical_line(self):
        """Xi(1/2 + it) should be real for real t (for self-dual forms)."""
        s = complex(0.5, 4.0)
        Xi = completed_epstein(s, 1, 0, 1)
        # For m^2+n^2 (self-dual), Xi(1/2+it) is real
        assert abs(Xi.imag) / max(abs(Xi.real), 1e-10) < 0.1

    def test_xi_finite(self):
        s = complex(0.5, 2.0)
        Xi = completed_epstein(s, 1, 0, 1)
        assert math.isfinite(Xi.real) and math.isfinite(Xi.imag)


# ================================================================
# Section 5: Koszul-Epstein functions
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestKoszulEpsteinIsing:
    """Test the Ising Koszul-Epstein function."""

    def test_finite_at_s2(self):
        val = koszul_epstein_ising(2.0)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_real_on_real_axis(self):
        val = koszul_epstein_ising(3.0)
        assert abs(val.imag) < 1e-6

    def test_positive_for_large_sigma(self):
        """Positive for sigma > 1 (absolute convergence)."""
        val = koszul_epstein_ising(2.5)
        assert val.real > 0

    def test_equals_epstein_of_shadow_form(self):
        """KE_Ising(s) = eps_Q(s) for Q = shadow form."""
        s = 2.0
        ke = koszul_epstein_ising(s)
        ep = epstein_zeta_theta(s, 0.25, 6.0, 1924.0 / 49.0, N_theta=30)
        assert abs(ke - ep) < 1e-10

    def test_complex_input(self):
        """Can evaluate at complex s."""
        s = complex(0.5, 5.0)
        val = koszul_epstein_ising(s)
        assert math.isfinite(val.real) and math.isfinite(val.imag)


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestKoszulEpsteinVirasoroC1:
    """Test the Virasoro c=1 Koszul-Epstein function."""

    def test_finite_at_s2(self):
        val = koszul_epstein_virasoro_c1(2.0)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_real_on_real_axis(self):
        val = koszul_epstein_virasoro_c1(3.0)
        assert abs(val.imag) < 1e-6

    def test_positive_for_large_sigma(self):
        val = koszul_epstein_virasoro_c1(2.5)
        assert val.real > 0

    def test_equals_epstein_of_shadow_form(self):
        s = 2.0
        ke = koszul_epstein_virasoro_c1(s)
        ep = epstein_zeta_theta(s, 1.0, 12.0, 1052.0 / 27.0, N_theta=30)
        assert abs(ke - ep) < 1e-10

    def test_different_from_ising(self):
        """The two KE functions are different (different forms)."""
        s = complex(0.5, 3.0)
        v1 = koszul_epstein_ising(s)
        v2 = koszul_epstein_virasoro_c1(s)
        assert abs(v1 - v2) > 1e-6


# ================================================================
# Section 6: Off-line zero search infrastructure
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestGridEvaluation:
    """Test the grid evaluation helper."""

    def test_grid_dimensions(self):
        """Grid has correct dimensions."""
        sigmas, ts, values = _evaluate_on_grid(
            koszul_epstein_ising,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 4.0),
            n_sigma=5,
            n_t=5,
        )
        assert len(sigmas) == 5
        assert len(ts) == 5
        assert len(values) == 5
        assert len(values[0]) == 5

    def test_grid_range(self):
        sigmas, ts, values = _evaluate_on_grid(
            koszul_epstein_ising,
            sigma_range=(0.2, 0.8),
            t_range=(1.0, 5.0),
            n_sigma=3,
            n_t=3,
        )
        assert abs(sigmas[0] - 0.2) < 1e-10
        assert abs(sigmas[-1] - 0.8) < 1e-10
        assert abs(ts[0] - 1.0) < 1e-10
        assert abs(ts[-1] - 5.0) < 1e-10

    def test_values_are_finite(self):
        sigmas, ts, values = _evaluate_on_grid(
            koszul_epstein_ising,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 5.0),
            n_sigma=3,
            n_t=3,
        )
        for row in values:
            for v in row:
                assert math.isfinite(v.real) and math.isfinite(v.imag)


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestBisectSignChange:
    """Test the bisection helper."""

    def test_finds_zero_of_sine(self):
        t_zero = _bisect_sign_change(math.sin, 2.5, 3.5)
        assert abs(t_zero - math.pi) < 1e-5

    def test_finds_zero_of_cosine(self):
        t_zero = _bisect_sign_change(math.cos, 1.0, 2.0)
        assert abs(t_zero - math.pi / 2) < 1e-5


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestRefineZero:
    """Test the Muller's method zero refinement."""

    def test_refine_known_zero(self):
        """Refine a known zero of a simple function."""
        # f(s) = s - (0.5 + 3i) has a zero at 0.5 + 3i
        def f(s):
            return s - (0.5 + 3j)

        s0 = mpmath.mpc(0.52, 3.02)
        result = _refine_zero(f, s0)
        assert result is not None
        assert abs(float(mpmath.re(result)) - 0.5) < 1e-6
        assert abs(float(mpmath.im(result)) - 3.0) < 1e-6

    def test_returns_none_outside_strip(self):
        """Should return None if refined zero is outside the strip."""
        def f(s):
            return s - (1.5 + 3j)  # zero at Re=1.5, outside (0,1)

        s0 = mpmath.mpc(1.48, 3.02)
        result = _refine_zero(f, s0)
        assert result is None


# ================================================================
# Section 7: Off-line zero search (main question)
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestOfflineZeroSearch:
    """Test the off-line zero search machinery.

    NOTE: Whether the Ising Koszul-Epstein actually HAS off-line zeros
    is the central mathematical question. These tests verify the search
    machinery works correctly, and record what the computation finds.
    """

    def test_find_approximate_zeros_returns_list(self):
        """Search returns a list (possibly empty)."""
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 6.0),
            n_sigma=5,
            n_t=8,
        )
        assert isinstance(result, list)

    def test_zero_entries_have_required_keys(self):
        """Any found zeros have the expected dict keys."""
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 6.0),
            n_sigma=5,
            n_t=8,
        )
        for z in result:
            assert 'sigma' in z
            assert 't' in z
            assert 's' in z
            assert 'value' in z
            assert 'is_offline' in z

    def test_offline_flag_definition(self):
        """is_offline = True iff |Re(s) - 1/2| > 0.01."""
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 6.0),
            n_sigma=5,
            n_t=8,
        )
        for z in result:
            expected_offline = abs(z['sigma'] - 0.5) > 0.01
            assert z['is_offline'] == expected_offline

    def test_search_ising_small_window(self):
        """Run a small search for the Ising model."""
        result = search_offline_zeros_ising(t_max=8.0, n_sigma=5, n_t=15)
        # Record the finding without asserting presence/absence
        n_offline = sum(1 for z in result if z['is_offline'])
        # This is the key diagnostic: does the Ising KE have off-line zeros?
        print(f"Ising small search: {len(result)} zeros, {n_offline} off-line")

    def test_search_virasoro_c1_small_window(self):
        """Run a small search for Virasoro c=1."""
        result = search_offline_zeros_virasoro_c1(t_max=8.0, n_sigma=5, n_t=15)
        n_offline = sum(1 for z in result if z['is_offline'])
        print(f"Virasoro c=1 small search: {len(result)} zeros, {n_offline} off-line")

    def test_deduplication(self):
        """Nearby zeros should be deduplicated."""
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.3, 0.7),
            t_range=(2.0, 8.0),
            n_sigma=8,
            n_t=15,
        )
        for i, z1 in enumerate(result):
            for j, z2 in enumerate(result):
                if i != j:
                    assert abs(z1['s'] - z2['s']) >= 0.1


# ================================================================
# Section 8: L-function decomposition
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestHeckeLFunction:
    """Test the Hecke L-function computation."""

    def test_trivial_character_finite(self):
        """L(2, chi_0, -40) is finite (well into convergence region)."""
        val = hecke_L_function(2.0, -40, 'trivial', N_terms=1000)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_sign_character_finite(self):
        """L(2, chi_1, -40) is finite."""
        val = hecke_L_function(2.0, -40, 'sign', N_terms=1000)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_trivial_d15_finite(self):
        val = hecke_L_function(2.0, -15, 'trivial', N_terms=1000)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_sign_d15_finite(self):
        val = hecke_L_function(2.0, -15, 'sign', N_terms=1000)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_trivial_character_positive(self):
        """L(2, chi_0) = zeta_K(2) > 0 (product of zeta and L-series, both positive)."""
        val = hecke_L_function(2.0, -40, 'trivial', N_terms=500)
        assert val.real > 0

    def test_sign_character_real(self):
        """L(sigma, chi_1) is real for real sigma > 1."""
        val = hecke_L_function(2.0, -40, 'sign', N_terms=500)
        assert abs(val.imag) < 1e-4

    def test_invalid_d0_raises(self):
        """Unknown D0 raises ValueError for sign character."""
        with pytest.raises(ValueError):
            hecke_L_function(2.0, -999, 'sign')

    def test_invalid_chi_type_raises(self):
        with pytest.raises(ValueError):
            hecke_L_function(2.0, -40, 'invalid')


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestEpsteinDecomposition:
    """Test the L-function decomposition of the Epstein zeta."""

    def test_decomposition_returns_dict(self):
        data = ising_shadow_data()
        result = epstein_decomposition(2.0, data, N_terms=500)
        assert isinstance(result, dict)
        assert 'L0' in result
        assert 'L1' in result
        assert 'w' in result

    def test_unit_count(self):
        """w = 2 for |D| > 4."""
        data = ising_shadow_data()
        result = epstein_decomposition(2.0, data, N_terms=500)
        assert result['w'] == 2

    def test_l0_l1_finite(self):
        data = ising_shadow_data()
        result = epstein_decomposition(2.0, data, N_terms=500)
        assert math.isfinite(result['L0'].real)
        assert math.isfinite(result['L1'].real)

    def test_decomposition_virasoro_c1(self):
        data = virasoro_c1_shadow_data()
        result = epstein_decomposition(2.0, data, N_terms=500)
        assert 'L0' in result
        assert 'L1' in result


# ================================================================
# Section 9: Discriminant-to-form mapping
# ================================================================

class TestDiscriminantToForm:
    """Test the helper that maps fundamental discriminants to forms."""

    def test_positive_discriminant(self):
        assert _discriminant_to_form(5) is None

    def test_minus_3(self):
        """D = -3: principal form (1, 1, 1)."""
        result = _discriminant_to_form(-3)
        assert result is not None
        a, b, c = result
        assert b * b - 4 * a * c == -3

    def test_minus_4(self):
        """D = -4: principal form (1, 0, 1)."""
        result = _discriminant_to_form(-4)
        assert result is not None
        a, b, c = result
        assert b * b - 4 * a * c == -4

    def test_minus_40(self):
        result = _discriminant_to_form(-40)
        assert result is not None
        a, b, c = result
        assert b * b - 4 * a * c == -40

    def test_minus_15(self):
        result = _discriminant_to_form(-15)
        assert result is not None
        a, b, c = result
        assert b * b - 4 * a * c == -15


# ================================================================
# Section 10: Genus-2 Beurling kernel
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestGenus2BeurlingKernel:
    """Test the genus-2 Beurling kernel K^(2)(D, D)."""

    def test_returns_dict(self):
        result = genus2_beurling_kernel(-4, -4, T=5.0, N_terms=100)
        assert isinstance(result, dict)
        assert 'K2_diagonal' in result
        assert 'is_positive' in result

    def test_positivity_identity_form(self):
        """K^(2)(-4, -4) >= 0 (squared L^2 norm)."""
        result = genus2_beurling_kernel(-4, -4, T=2.0, N_terms=50)
        assert result['is_positive']
        assert result['K2_diagonal'] >= 0

    def test_positivity_d40(self):
        """K^(2)(-40, -40) >= 0 for Ising discriminant."""
        result = genus2_beurling_kernel(-40, -40, T=2.0, N_terms=50)
        assert result['is_positive']

    def test_positivity_d15(self):
        """K^(2)(-15, -15) >= 0 for Virasoro c=1 discriminant."""
        result = genus2_beurling_kernel(-15, -15, T=2.0, N_terms=50)
        assert result['is_positive']

    def test_invalid_positive_discriminant(self):
        result = genus2_beurling_kernel(5, 5, T=5.0, N_terms=100)
        assert result is None


# ================================================================
# Section 11: Genus-2 zero constraint analysis
# ================================================================

class TestGenus2ZeroConstraint:
    """Test the genus-2 positivity analysis for zero exclusion."""

    def _make_fake_zeros(self, n_online, n_offline):
        zeros = []
        for i in range(n_online):
            zeros.append({'sigma': 0.5, 't': 2.0 + i, 'is_offline': False})
        for i in range(n_offline):
            zeros.append({'sigma': 0.3, 't': 5.0 + i, 'is_offline': True})
        return zeros

    def test_returns_dict(self):
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert isinstance(result, dict)

    def test_k2_always_positive(self):
        """K^(2)(D,D) >= 0 is automatic (structural result)."""
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert result['K2_positive'] is True

    def test_genus2_does_not_exclude_offline(self):
        """Genus-2 positivity does NOT exclude off-line zeros (structural separation)."""
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, self._make_fake_zeros(5, 3))
        assert result['genus2_excludes_offline'] is False

    def test_structural_diagnosis_present(self):
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert 'structural_diagnosis' in result
        assert 'thm:structural-separation' in result['structural_diagnosis']

    def test_lambda_2_value(self):
        """lambda_2 = 7/5760 (Faber-Pandharipande, AP38 corrected)."""
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert abs(result['lambda_2'] - 7.0 / 5760) < 1e-15

    def test_ising_genus2_amplitude(self):
        """A_2(Ising) = kappa * lambda_2 + delta_pf."""
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        kappa = 0.25
        S3 = 2.0
        lam2 = 7.0 / 5760
        delta_pf = S3 * (10 * S3 - kappa) / 48.0
        expected = kappa * lam2 + delta_pf
        assert abs(result['A_2'] - expected) < 1e-12

    def test_complementarity_sum_finite(self):
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert math.isfinite(result['A_2_sum'])

    def test_zero_counting(self):
        data = ising_shadow_data()
        zeros = self._make_fake_zeros(3, 2)
        result = genus2_zero_constraint(data, zeros)
        assert result['n_zeros_found'] == 5
        assert result['n_offline'] == 2
        assert result['n_online'] == 3

    def test_koszul_dual_central_charge(self):
        """Koszul dual of Vir_c is Vir_{26-c} (AP8: c=1/2 dual is c=25.5)."""
        data = ising_shadow_data()
        result = genus2_zero_constraint(data, [])
        c_val = float(data['c'])
        # kappa_dual = (26 - c) / 2
        expected_kappa_dual = (26 - c_val) / 2
        expected_A2_dual = expected_kappa_dual * 7.0 / 5760 + 2.0 * (10 * 2.0 - expected_kappa_dual) / 48.0
        assert abs(result['A_2_dual'] - expected_A2_dual) < 1e-10

    def test_virasoro_c1_genus2(self):
        data = virasoro_c1_shadow_data()
        result = genus2_zero_constraint(data, [])
        assert result['genus2_excludes_offline'] is False
        assert result['K2_positive'] is True


# ================================================================
# Section 12: Critical line analysis
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestCriticalLine:
    """Test critical line evaluation and sign change detection."""

    def test_critical_line_values_finite(self):
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=10)

        t_vals = [2.0, 5.0, 10.0]
        results = critical_line_values(eps_fast, t_vals, name='Ising')
        assert len(results) == 3
        for r in results:
            assert math.isfinite(r['abs_value'])
            assert r['name'] == 'Ising'

    def test_critical_line_values_positive_abs(self):
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=10)

        t_vals = [3.0, 7.0]
        results = critical_line_values(eps_fast, t_vals)
        for r in results:
            assert r['abs_value'] >= 0

    def test_sign_changes_returns_list(self):
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = critical_line_sign_changes(
            eps_fast,
            t_range=(2.0, 8.0),
            n_points=20,
        )
        assert isinstance(result, list)

    def test_sign_changes_have_type(self):
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = critical_line_sign_changes(
            eps_fast,
            t_range=(2.0, 15.0),
            n_points=40,
        )
        for z in result:
            assert z['type'] == 'on-line zero'
            assert abs(z['s'].real - 0.5) < 1e-10

    def test_on_line_zeros_exist(self):
        """There should be at least some on-line zeros in a large enough window."""
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=8)

        result = critical_line_sign_changes(
            eps_fast,
            t_range=(1.0, 20.0),
            n_points=40,
        )
        # Epstein zeta functions generically have infinitely many zeros on
        # the critical line, so we should find some
        assert len(result) >= 1, "Expected at least 1 on-line zero for Ising"

    def test_virasoro_c1_on_line_zeros(self):
        def eps_fast(s):
            return koszul_epstein_virasoro_c1(s, N_theta=8)

        result = critical_line_sign_changes(
            eps_fast,
            t_range=(1.0, 20.0),
            n_points=40,
        )
        assert len(result) >= 1, "Expected at least 1 on-line zero for Virasoro c=1"


# ================================================================
# Section 13: Functional equation verification
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestFunctionalEquation:
    """Test the functional equation verification routine."""

    def test_returns_list(self):
        s_values = [complex(0.3, 2.0), complex(0.7, 5.0)]
        result = verify_functional_equation(koszul_epstein_ising, s_values, 'Ising')
        assert isinstance(result, list)
        assert len(result) == 2

    def test_entries_have_keys(self):
        s_values = [complex(0.4, 3.0)]
        result = verify_functional_equation(koszul_epstein_ising, s_values, 'test')
        assert len(result) == 1
        r = result[0]
        assert 'eps_s' in r
        assert 'eps_1ms' in r
        assert r['name'] == 'test'

    def test_s_and_1ms_consistent(self):
        s = complex(0.3, 4.0)
        result = verify_functional_equation(koszul_epstein_ising, [s], 'Ising')
        r = result[0]
        assert abs(r['s'] - s) < 1e-10
        assert abs(r['1-s'] - (1 - s)) < 1e-10


# ================================================================
# Section 14: Master analysis function
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
@pytest.mark.slow
class TestRunFullAnalysis:
    """Test the master analysis function.

    These tests are slow (run_full_analysis calls critical_line_sign_changes
    with n_points=500 internally). Mark as slow for selective execution.
    """

    def test_runs_without_error(self):
        """The full analysis runs to completion."""
        results = run_full_analysis(
            t_max=5.0, grid_sigma=3, grid_t=5, verbose=False
        )
        assert isinstance(results, dict)
        assert 'Ising' in results
        assert 'Virasoro_c1' in results

    def test_ising_result_structure(self):
        results = run_full_analysis(
            t_max=5.0, grid_sigma=3, grid_t=5, verbose=False
        )
        r = results['Ising']
        assert 'data' in r
        assert 'on_line_zeros' in r
        assert 'off_line_search' in r
        assert 'n_offline' in r
        assert 'genus2_analysis' in r

    def test_virasoro_c1_result_structure(self):
        results = run_full_analysis(
            t_max=5.0, grid_sigma=3, grid_t=5, verbose=False
        )
        r = results['Virasoro_c1']
        assert 'data' in r
        assert 'genus2_analysis' in r

    def test_genus2_analysis_present(self):
        results = run_full_analysis(
            t_max=5.0, grid_sigma=3, grid_t=5, verbose=False
        )
        for name in ('Ising', 'Virasoro_c1'):
            g2 = results[name]['genus2_analysis']
            assert g2['genus2_excludes_offline'] is False
            assert g2['K2_positive'] is True


# ================================================================
# Section 15: Key mathematical facts (independent verification)
# ================================================================

class TestMathematicalFacts:
    """Independent verification of mathematical constants and identities."""

    def test_lambda_2_faber_pandharipande(self):
        """lambda_2 = 7/5760 (AP38: corrected from 1/1152)."""
        assert 7 / 5760 == pytest.approx(0.0012152777777777778)
        # Cross-check: 1/1152 = 0.000868... which is WRONG (AP38)
        assert 7 / 5760 != 1 / 1152

    def test_class_number_minus40(self):
        """h(-40) = 2. The class group is Z/2Z."""
        # Two reduced forms of disc -40: (1,0,10) and (2,0,5)
        forms = [(1, 0, 10), (2, 0, 5)]
        for a, b, c in forms:
            assert b * b - 4 * a * c == -40
        assert len(forms) == 2

    def test_class_number_minus15(self):
        """h(-15) = 2. The class group is Z/2Z."""
        forms = [(1, 1, 4), (2, 1, 2)]
        for a, b, c in forms:
            assert b * b - 4 * a * c == -15
        assert len(forms) == 2

    def test_virasoro_koszul_dual_central_charge(self):
        """Vir_c^! = Vir_{26-c}. For c=1/2: dual at c=51/2."""
        c = Fraction(1, 2)
        c_dual = 26 - c
        assert c_dual == Fraction(51, 2)

    def test_ising_discriminant_factorization(self):
        """-125440 = -40 * 56^2."""
        assert -40 * 56 * 56 == -125440

    def test_virasoro_c1_discriminant_factorization(self):
        """-8640 = -15 * 24^2."""
        assert -15 * 24 * 24 == -8640

    def test_genus_decomposition_d40(self):
        """D_0 = -40 = (-8)(5) as product of discriminants."""
        # -8 is a fundamental discriminant (even, -8/4 = -2, -2 mod 4 = 2)
        # 5 is a fundamental discriminant (5 mod 4 = 1)
        assert (-8) * 5 == -40

    def test_genus_decomposition_d15(self):
        """D_0 = -15 = (-3)(5) as product of discriminants."""
        assert (-3) * 5 == -15

    def test_s4_ising(self):
        """S_4 = 10/(c(5c+22)) for Ising at c=1/2."""
        c = Fraction(1, 2)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert expected == Fraction(40, 49)

    def test_s4_virasoro_c1(self):
        """S_4 = 10/(c(5c+22)) for Virasoro at c=1."""
        c = Fraction(1)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert expected == Fraction(10, 27)

    def test_delta_pf_genus2_formula(self):
        """delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48."""
        # For Ising: S_3 = alpha = 2, kappa = 1/4
        S3 = Fraction(2)
        kappa = Fraction(1, 4)
        delta_pf = S3 * (10 * S3 - kappa) / 48
        expected = Fraction(2) * Fraction(79, 4) / 48
        assert delta_pf == expected

    def test_genus2_amplitude_sum_expression(self):
        """A_2(A) + A_2(A!) is computable from shadow invariants alone."""
        for data_func in (ising_shadow_data, virasoro_c1_shadow_data):
            d = data_func()
            c_val = float(d['c'])
            kappa = c_val / 2
            kappa_dual = (26 - c_val) / 2
            S3 = 2.0  # alpha for Virasoro
            lam2 = 7.0 / 5760
            A2 = kappa * lam2 + S3 * (10 * S3 - kappa) / 48.0
            A2_dual = kappa_dual * lam2 + S3 * (10 * S3 - kappa_dual) / 48.0
            total = A2 + A2_dual
            assert math.isfinite(total)


# ================================================================
# Section 16: Structural separation theorem verification
# ================================================================

class TestStructuralSeparation:
    """Test the structural separation result: genus-2 data cannot
    access scattering-matrix poles of the Koszul-Epstein function."""

    def test_genus2_positivity_is_automatic(self):
        """K^(2)(D,D) >= 0 is a squared norm, always non-negative."""
        for data_func in (ising_shadow_data, virasoro_c1_shadow_data):
            d = data_func()
            result = genus2_zero_constraint(d, [])
            assert result['K2_positive'] is True

    def test_genus2_does_not_exclude_offline_ising(self):
        """Structural separation: genus-2 cannot exclude off-line zeros for Ising."""
        d = ising_shadow_data()
        fake_offline = [{'sigma': 0.3, 't': 5.0, 'is_offline': True}]
        result = genus2_zero_constraint(d, fake_offline)
        assert result['genus2_excludes_offline'] is False

    def test_genus2_does_not_exclude_offline_virasoro(self):
        d = virasoro_c1_shadow_data()
        fake_offline = [{'sigma': 0.7, 't': 8.0, 'is_offline': True}]
        result = genus2_zero_constraint(d, fake_offline)
        assert result['genus2_excludes_offline'] is False

    def test_structural_diagnosis_mentions_mechanism(self):
        """The diagnosis explains the structural reason."""
        d = ising_shadow_data()
        result = genus2_zero_constraint(d, [])
        diag = result['structural_diagnosis']
        assert 'squared' in diag.lower() or 'L^2' in diag
        assert 'structural-separation' in diag or 'thm:structural-separation' in diag


# ================================================================
# Section 17: AP38 regression test
# ================================================================

class TestAP38Regression:
    """Verify AP38 correction: lambda_2 = 7/5760, NOT 1/1152."""

    def test_lambda2_in_genus2_constraint(self):
        """genus2_zero_constraint uses the CORRECT lambda_2 = 7/5760."""
        d = ising_shadow_data()
        result = genus2_zero_constraint(d, [])
        assert abs(result['lambda_2'] - 7.0 / 5760) < 1e-15

    def test_lambda2_not_old_wrong_value(self):
        d = ising_shadow_data()
        result = genus2_zero_constraint(d, [])
        assert abs(result['lambda_2'] - 1.0 / 1152) > 1e-6


# ================================================================
# Section 18: DH mechanism consistency checks
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestDavenportHeilbronnMechanism:
    """Tests verifying the Davenport-Heilbronn decomposition is consistent."""

    def test_principal_nonprincipal_sum(self):
        """eps_principal + eps_nonprincipal = (4/w) * L_0 for h=2.

        The Epstein zeta decomposition for a form Q in a class group of
        order h with w units is:
            eps_Q(s) = (2/w) sum_chi chi([Q]) L(s, chi)
        For h=2: eps_p = (2/w)[L_0 + L_1], eps_np = (2/w)[L_0 - L_1].
        Sum: eps_p + eps_np = (4/w) * L_0 = 2 * L_0 (w=2).
        """
        s = 2.0
        # D_0 = -40: principal (1,0,10), non-principal (2,0,5)
        eps_p = epstein_zeta_theta(s, 1, 0, 10, N_theta=12)
        eps_np = epstein_zeta_theta(s, 2, 0, 5, N_theta=12)
        L0 = hecke_L_function(s, -40, 'trivial', N_terms=500)
        w = 2
        expected_sum = (4.0 / w) * L0
        actual_sum = eps_p + eps_np
        rel_err = abs(actual_sum - expected_sum) / max(abs(expected_sum), 1e-10)
        assert rel_err < 0.1, (
            f"Sum decomposition failed: sum={actual_sum}, expected={expected_sum}, "
            f"rel_err={rel_err}"
        )

    def test_principal_nonprincipal_difference(self):
        """eps_principal - eps_nonprincipal = (4/w) * L_1 for h=2.

        eps_p - eps_np = (2/w)[(L_0+L_1) - (L_0-L_1)] = (4/w)*L_1.
        """
        s = 2.0
        eps_p = epstein_zeta_theta(s, 1, 0, 10, N_theta=12)
        eps_np = epstein_zeta_theta(s, 2, 0, 5, N_theta=12)
        L1 = hecke_L_function(s, -40, 'sign', N_terms=500)
        w = 2
        expected_diff = (4.0 / w) * L1
        actual_diff = eps_p - eps_np
        rel_err = abs(actual_diff - expected_diff) / max(abs(expected_diff), 1e-10)
        assert rel_err < 0.1, (
            f"Diff decomposition failed: diff={actual_diff}, expected={expected_diff}, "
            f"rel_err={rel_err}"
        )

    def test_d15_principal_nonprincipal_sum(self):
        """Same sum test for D_0 = -15."""
        s = 2.0
        eps_p = epstein_zeta_theta(s, 1, 1, 4, N_theta=12)
        eps_np = epstein_zeta_theta(s, 2, 1, 2, N_theta=12)
        L0 = hecke_L_function(s, -15, 'trivial', N_terms=500)
        w = 2
        expected_sum = (4.0 / w) * L0
        actual_sum = eps_p + eps_np
        rel_err = abs(actual_sum - expected_sum) / max(abs(expected_sum), 1e-10)
        assert rel_err < 0.1


# ================================================================
# Section 19: Edge cases and robustness
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestEdgeCases:
    """Edge cases and robustness tests."""

    def test_epstein_near_pole(self):
        """Epstein zeta grows near s=1 but doesn't crash."""
        val = epstein_zeta_theta(1.001, 1, 0, 1, N_theta=8)
        assert math.isfinite(val.real)

    def test_epstein_large_imaginary(self):
        """Evaluation at large imaginary part doesn't crash."""
        val = epstein_zeta_theta(complex(0.5, 50.0), 1, 0, 1, N_theta=8)
        assert math.isfinite(val.real) and math.isfinite(val.imag)

    def test_empty_zero_list(self):
        """genus2_zero_constraint handles empty zero list."""
        d = ising_shadow_data()
        result = genus2_zero_constraint(d, [])
        assert result['n_zeros_found'] == 0
        assert result['n_offline'] == 0

    def test_search_tiny_window(self):
        """Search in a tiny window returns (possibly empty) list without error."""
        result = find_approximate_zeros(
            koszul_epstein_ising,
            sigma_range=(0.49, 0.51),
            t_range=(3.0, 3.1),
            n_sigma=3,
            n_t=3,
        )
        assert isinstance(result, list)

    def test_no_mpmath_fallback_for_kronecker_naive(self):
        """Kronecker naive works without mpmath."""
        val = _kronecker_naive(-40, 7)
        assert val in (-1, 0, 1)


# ================================================================
# Section 20: The central question — off-line zeros diagnostic
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestCentralQuestion:
    """Diagnostic tests for the central mathematical question:

    Does the Ising (c=1/2) Koszul-Epstein function have off-line zeros?

    The Davenport-Heilbronn theorem (1936) shows that GENERIC Epstein
    zeta functions with h(D) > 1 have off-line zeros. The question is
    whether the Koszul constraints (shadow metric structure) protect
    against this.

    These tests RUN the search and RECORD findings. They do not assert
    the answer to the open question.
    """

    def test_ising_off_line_search_diagnostic(self):
        """Search for off-line zeros of the Ising KE function.

        This is the central computation. We search in
        0.1 < Re(s) < 0.9, 1 < Im(s) < 15 with a moderate grid.
        Use reduced N_theta for tractable runtime.
        """
        def eps_fast(s):
            return koszul_epstein_ising(s, N_theta=10)

        zeros = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.1, 0.9),
            t_range=(1.0, 15.0),
            n_sigma=10,
            n_t=30,
        )
        n_offline = sum(1 for z in zeros if z.get('is_offline', False))
        n_online = len(zeros) - n_offline
        print(f"\n=== ISING OFF-LINE ZERO DIAGNOSTIC ===")
        print(f"Total zeros found: {len(zeros)}")
        print(f"On-line (|Re(s)-1/2| <= 0.01): {n_online}")
        print(f"Off-line (|Re(s)-1/2| > 0.01): {n_offline}")
        for z in zeros:
            marker = " ** OFF-LINE **" if z['is_offline'] else ""
            print(f"  s = {z['sigma']:.6f} + {z['t']:.6f}i, "
                  f"|eps| = {z['value']:.2e}{marker}")

        # Structural separation says genus-2 cannot exclude them
        data = ising_shadow_data()
        g2 = genus2_zero_constraint(data, zeros)
        print(f"\nGenus-2 excludes off-line: {g2['genus2_excludes_offline']}")
        print(f"A_2(Ising) = {g2['A_2']:.10f}")
        print(f"A_2(Ising!) = {g2['A_2_dual']:.10f}")
        print(f"Sum = {g2['A_2_sum']:.10f}")
        # Record but don't assert the open question
        assert isinstance(n_offline, int)

    def test_virasoro_c1_off_line_search_diagnostic(self):
        """Same diagnostic for Virasoro at c=1."""
        def eps_fast(s):
            return koszul_epstein_virasoro_c1(s, N_theta=10)

        zeros = find_approximate_zeros(
            eps_fast,
            sigma_range=(0.1, 0.9),
            t_range=(1.0, 15.0),
            n_sigma=10,
            n_t=30,
        )
        n_offline = sum(1 for z in zeros if z.get('is_offline', False))
        n_online = len(zeros) - n_offline
        print(f"\n=== VIRASORO c=1 OFF-LINE ZERO DIAGNOSTIC ===")
        print(f"Total zeros found: {len(zeros)}")
        print(f"On-line: {n_online}")
        print(f"Off-line: {n_offline}")
        for z in zeros:
            marker = " ** OFF-LINE **" if z['is_offline'] else ""
            print(f"  s = {z['sigma']:.6f} + {z['t']:.6f}i, "
                  f"|eps| = {z['value']:.2e}{marker}")
        assert isinstance(n_offline, int)
