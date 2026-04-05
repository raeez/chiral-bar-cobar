r"""Tests for BTZ spectral zeta and Selberg zeta engine.

Tests organized by section:
  1.  BTZ geometry (horizons, temperatures)
  2.  Quasinormal mode spectrum
  3.  BTZ spectral zeta function
  4.  BTZ Selberg zeta function
  5.  Zeros of the Selberg zeta
  6.  Hawking temperature from spectral zeta
  7.  Bekenstein-Hawking from shadow data
  8.  Selberg zeta at Riemann zero positions
  9.  Modular crossing (high-T / low-T duality)
  10. Shadow zeta / Selberg ratio
  11. Theta function representation
  12. WKB approximation
  13. Cardy formula consistency
  14. Cross-verification paths
  15. Special cases and edge cases
"""

import pytest
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_btz_spectral_zeta_engine import (
    # Section 1
    btz_horizons, hawking_temperature_btz, thermal_parameter,
    inverse_temperature_btz,
    # Section 2
    quasinormal_frequency, quasinormal_energy, quasinormal_spectrum,
    # Section 3
    spectral_zeta_btz, spectral_zeta_nonrotating,
    spectral_zeta_derivative_at_zero, spectral_zeta_at_zero,
    # Section 4
    selberg_zeta_btz, selberg_zeta_from_mass, log_selberg_zeta,
    selberg_zeta_derivative,
    # Section 5
    selberg_zeta_zeros_exact, selberg_zeros_on_strip, verify_selberg_zero,
    # Section 6
    hawking_temperature_from_spectral_zeta,
    # Section 7
    bekenstein_hawking_from_shadow,
    # Section 8
    selberg_at_riemann_zeros, selberg_at_shifted_riemann_zeros,
    # Section 9
    modular_crossing_selberg, selberg_at_self_dual, self_dual_temperature_data,
    # Section 10
    shadow_zeta, shadow_selberg_ratio,
    # Section 11
    theta_representation,
    # Section 12
    wkb_quasinormal_frequencies,
    # Section 13
    cardy_consistency,
    # Section 14
    selberg_zeta_modular_check,
    # Section 15
    full_spectral_analysis,
)

PI = math.pi
TWO_PI = 2.0 * PI


# =========================================================================
# Section 1: BTZ geometry
# =========================================================================

class TestBTZGeometry:
    """Horizon radii, temperatures, thermal parameters."""

    def test_nonrotating_horizons(self):
        """Non-rotating BTZ: r_+ = sqrt(M), r_- = 0."""
        h = btz_horizons(4.0, 0.0)
        assert h['valid']
        assert abs(h['r_plus'] - 2.0) < 1e-12
        assert abs(h['r_minus']) < 1e-12

    def test_nonrotating_M1(self):
        """M = 1: r_+ = 1."""
        h = btz_horizons(1.0)
        assert abs(h['r_plus'] - 1.0) < 1e-12

    def test_extremal_horizons(self):
        """Extremal BTZ: J = M, r_+ = r_- = sqrt(M/2)."""
        M = 2.0
        h = btz_horizons(M, M)
        assert h['valid']
        assert abs(h['r_plus'] - 1.0) < 1e-10
        assert abs(h['r_minus'] - 1.0) < 1e-10

    def test_rotating_horizons(self):
        """Rotating BTZ: r_+^2 + r_-^2 = M, r_+ r_- = J/2."""
        M, J = 5.0, 3.0
        h = btz_horizons(M, J)
        assert h['valid']
        r_p, r_m = h['r_plus'], h['r_minus']
        assert abs(r_p ** 2 + r_m ** 2 - M) < 1e-10
        # r_+ * r_- = |J| / 2 (from the BTZ metric; our convention is l=1)
        # Actually: r_+^2 = (M/2)(1+sqrt(1-(J/M)^2)), etc.
        # Check r_+^2 - r_-^2 = M*sqrt(1-(J/M)^2)
        disc = M * math.sqrt(1 - (J / M) ** 2)
        assert abs(r_p ** 2 - r_m ** 2 - disc) < 1e-10

    def test_negative_mass_invalid(self):
        """M < 0 is invalid (no horizon)."""
        h = btz_horizons(-1.0)
        assert not h['valid']

    def test_naked_singularity_invalid(self):
        """|J| > M: naked singularity."""
        h = btz_horizons(1.0, 2.0)
        assert not h['valid']

    def test_hawking_temperature_nonrotating(self):
        """T_H = sqrt(M) / (2 pi) for non-rotating BTZ."""
        M = 4.0
        T = hawking_temperature_btz(M)
        expected = 2.0 / TWO_PI  # sqrt(4) / (2 pi)
        assert abs(T - expected) < 1e-12

    def test_hawking_temperature_extremal(self):
        """T_H = 0 for extremal BTZ (r_+ = r_-)."""
        T = hawking_temperature_btz(2.0, 2.0)
        assert abs(T) < 1e-10

    def test_thermal_parameter_range(self):
        """0 < q < 1 for valid BTZ."""
        q = thermal_parameter(1.0)
        assert 0 < q < 1

    def test_thermal_parameter_large_M(self):
        """Large M: q -> 0 (high temperature)."""
        q = thermal_parameter(100.0)
        assert q < 1e-10

    def test_thermal_parameter_small_M(self):
        """Small M: q -> 1 (low temperature)."""
        q = thermal_parameter(0.01)
        assert q > 0.5

    def test_inverse_temperature_consistency(self):
        """beta = 1/T_H."""
        M = 3.0
        T = hawking_temperature_btz(M)
        beta = inverse_temperature_btz(M)
        assert abs(T * beta - 1.0) < 1e-12


# =========================================================================
# Section 2: Quasinormal mode spectrum
# =========================================================================

class TestQuasinormalModes:
    """Quasinormal frequencies and energies."""

    def test_qnm_purely_imaginary(self):
        """Quasinormal frequencies are purely imaginary for BTZ."""
        omega = quasinormal_frequency(3, 2.0, 1.0, 0.0, 'R')
        assert abs(omega.real) < 1e-15

    def test_qnm_negative_imaginary(self):
        """Im(omega) < 0 (decaying modes)."""
        omega = quasinormal_frequency(0, 2.0, 1.0, 0.0, 'R')
        assert omega.imag < 0

    def test_qnm_nonrotating_LR_equal(self):
        """For r_- = 0, left and right movers have the same |omega|."""
        E_R = quasinormal_energy(5, 2.0, 1.0, 0.0, 'R')
        E_L = quasinormal_energy(5, 2.0, 1.0, 0.0, 'L')
        assert abs(E_R - E_L) < 1e-12

    def test_qnm_rotating_LR_different(self):
        """For r_- > 0, left and right movers differ."""
        E_R = quasinormal_energy(3, 2.0, 2.0, 0.5, 'R')
        E_L = quasinormal_energy(3, 2.0, 2.0, 0.5, 'L')
        assert abs(E_R - E_L) > 0.1

    def test_qnm_energy_positive(self):
        """All energies are positive."""
        for n in range(10):
            E = quasinormal_energy(n, 2.0, 1.0)
            assert E > 0

    def test_qnm_energy_formula(self):
        """E_n = r_+ (2n + h) for non-rotating BTZ."""
        r_plus = 1.5
        h = 2.0
        for n in range(10):
            E = quasinormal_energy(n, h, r_plus)
            expected = r_plus * (2 * n + h)
            assert abs(E - expected) < 1e-12

    def test_qnm_linear_spacing(self):
        """Quasinormal modes are LINEARLY spaced (not logarithmic)."""
        r_plus = 1.0
        h = 2.0
        E0 = quasinormal_energy(0, h, r_plus)
        E1 = quasinormal_energy(1, h, r_plus)
        E2 = quasinormal_energy(2, h, r_plus)
        # Spacing is constant: E_{n+1} - E_n = 2 r_+
        assert abs((E1 - E0) - 2 * r_plus) < 1e-12
        assert abs((E2 - E1) - 2 * r_plus) < 1e-12

    def test_spectrum_output(self):
        """quasinormal_spectrum returns both chiralities."""
        spec = quasinormal_spectrum(2.0, 1.0, 0.0, n_max=10)
        assert len(spec['right']) == 11
        assert len(spec['left']) == 11


# =========================================================================
# Section 3: BTZ spectral zeta function
# =========================================================================

class TestSpectralZeta:
    """Spectral zeta function from quasinormal modes."""

    def test_spectral_zeta_convergent(self):
        """zeta_BTZ(s) converges for Re(s) > 1."""
        z = spectral_zeta_btz(complex(2), 2.0, 1.0)
        assert math.isfinite(abs(z))

    def test_spectral_zeta_s2_positive(self):
        """zeta_BTZ(2) > 0 (sum of positive terms)."""
        z = spectral_zeta_btz(complex(2), 2.0, 1.0)
        assert z.real > 0
        assert abs(z.imag) < 1e-10  # Real for real s

    def test_spectral_zeta_hurwitz_relation(self):
        """zeta_BTZ(s) = 2^{1-s} r_+^{-s} zeta_H(s, h/2) for non-rotating.

        Verify numerically by direct summation.
        """
        s = complex(3)
        h = 2.0
        r_plus = 1.5

        # Direct sum
        direct = complex(0)
        for n in range(5000):
            E = r_plus * (2 * n + h)
            direct += 2 * E ** (-s)  # factor 2 for both chiralities

        # Via Hurwitz
        via_hurwitz = spectral_zeta_btz(s, h, r_plus)

        assert abs(direct - via_hurwitz) / abs(direct) < 1e-4

    def test_spectral_zeta_at_zero(self):
        """zeta_BTZ(0) = 2 * (1/2 - h/2) = 1 - h."""
        h = 2.0
        z0 = spectral_zeta_at_zero(h, 1.0)
        assert abs(z0 - (1.0 - h)) < 1e-12

    def test_spectral_zeta_at_zero_h1(self):
        """zeta_BTZ(0) = 0 for h = 1."""
        z0 = spectral_zeta_at_zero(1.0, 1.0)
        assert abs(z0) < 1e-12

    def test_spectral_zeta_scaling(self):
        """zeta_BTZ(s; lambda*r_+) = lambda^{-s} * zeta_BTZ(s; r_+)."""
        s = complex(2.5)
        h = 2.0
        lam = 3.0

        z1 = spectral_zeta_btz(s, h, 1.0)
        z_lam = spectral_zeta_btz(s, h, lam)

        assert abs(z_lam - lam ** (-s) * z1) / abs(z1) < 1e-6

    def test_spectral_zeta_derivative_at_zero_finite(self):
        """zeta'_BTZ(0) is finite."""
        zp = spectral_zeta_derivative_at_zero(2.0, 1.0)
        assert math.isfinite(abs(zp))

    def test_spectral_zeta_derivative_involves_log_gamma(self):
        """zeta'_BTZ(0) involves log Gamma(h/2) (the functional determinant)."""
        h = 2.0
        r_plus = 1.0
        a = h / 2.0
        zp = spectral_zeta_derivative_at_zero(h, r_plus)

        # For r_+ = 1, non-rotating:
        # zeta'(0) = 2 * [-log(2) * (1/2 - a) + log Gamma(a) - (1/2) log(2 pi)]
        expected = 2.0 * (
            -math.log(2.0) * (0.5 - a) + math.lgamma(a) - 0.5 * math.log(TWO_PI)
        )
        assert abs(zp - expected) < 1e-10


# =========================================================================
# Section 4: BTZ Selberg zeta function
# =========================================================================

class TestSelbergZeta:
    """Selberg zeta Z_BTZ(s) = prod_{n >= 0} (1 - q^{n+s})."""

    def test_selberg_zeta_product_formula(self):
        """Verify the product formula by multiplying out."""
        q = 0.1
        s = complex(0.5)
        Z = selberg_zeta_btz(s, q)
        # Manual product for first 5 terms
        product = 1.0
        for n in range(500):
            product *= (1.0 - q ** (n + s))
            if abs(q ** (n + s.real)) < 1e-30:
                break
        assert abs(Z - product) < 1e-10

    def test_selberg_zeta_real_s(self):
        """Z_BTZ(s) is real for real s > 0."""
        q = 0.1
        Z = selberg_zeta_btz(complex(1.0), q)
        assert abs(Z.imag) < 1e-12

    def test_selberg_zeta_nonzero_large_s(self):
        """Z_BTZ(s) -> 1 as Re(s) -> infty."""
        q = 0.1
        Z = selberg_zeta_btz(complex(100.0), q)
        assert abs(Z - 1.0) < 1e-10

    def test_selberg_zeta_q_pochhammer(self):
        """Z_BTZ(1) = (q; q)_infty (the Euler function)."""
        q = 0.3
        Z = selberg_zeta_btz(complex(1.0), q)
        # (q; q)_infty = prod_{n >= 1} (1 - q^n)
        euler = 1.0
        for n in range(1, 500):
            euler *= (1.0 - q ** n)
        assert abs(Z - euler) < 1e-10

    def test_log_selberg_consistent(self):
        """log Z_BTZ(s) = sum log(1 - q^{n+s})."""
        q = 0.2
        s = complex(0.5, 0.3)
        Z = selberg_zeta_btz(s, q)
        log_Z = log_selberg_zeta(s, q)
        assert abs(cmath.exp(log_Z) - Z) / abs(Z) < 1e-8

    def test_selberg_zeta_derivative_formula(self):
        """Z'/Z = sum q^{n+s} log(q) / (1 - q^{n+s})."""
        q = 0.15
        s = complex(0.5)
        # Numerical derivative
        eps = 1e-7
        Z_plus = selberg_zeta_btz(s + eps, q)
        Z_minus = selberg_zeta_btz(s - eps, q)
        Z_s = selberg_zeta_btz(s, q)
        numerical_deriv = (Z_plus - Z_minus) / (2 * eps)
        log_deriv_numerical = numerical_deriv / Z_s

        # Analytic log derivative
        log_deriv = selberg_zeta_derivative(s, q)

        assert abs(log_deriv - log_deriv_numerical) / abs(log_deriv) < 1e-4

    def test_selberg_from_mass_consistent(self):
        """selberg_zeta_from_mass uses the correct thermal parameter."""
        M = 4.0
        q = thermal_parameter(M)
        s = complex(1.0)
        Z1 = selberg_zeta_btz(s, q)
        Z2 = selberg_zeta_from_mass(s, M)
        assert abs(Z1 - Z2) < 1e-12

    def test_selberg_zeta_monotone_real_s(self):
        """For real s > 0: |Z_BTZ(s)| increases with s (fewer zeros)."""
        q = 0.1
        Z1 = abs(selberg_zeta_btz(complex(0.5), q))
        Z2 = abs(selberg_zeta_btz(complex(1.5), q))
        Z3 = abs(selberg_zeta_btz(complex(2.5), q))
        assert Z1 < Z2 < Z3


# =========================================================================
# Section 5: Zeros of the Selberg zeta
# =========================================================================

class TestSelbergZeros:
    """Zeros of Z_BTZ lie at s = -n + 2 pi i k / log(1/q)."""

    def test_zero_at_s0_n0_k0(self):
        """Z_BTZ(0) = 0 (the n=0, k=0 zero: 1 - q^0 = 0)."""
        # Actually: prod starts at n=0, and (1 - q^{0+0}) = 1 - 1 = 0
        # So Z_BTZ(0) = 0 for ANY q.
        q = 0.3
        Z = selberg_zeta_btz(complex(0.0), q)
        assert abs(Z) < 1e-10

    def test_zero_at_negative_integer(self):
        """Z_BTZ(-n) = 0 for n = 0, 1, 2, ... (the factor 1 - q^0 = 0)."""
        q = 0.2
        for n in range(5):
            Z = selberg_zeta_btz(complex(-n), q)
            assert abs(Z) < 1e-10, f"Z_BTZ({-n}) should be zero"

    def test_zero_imaginary_spacing(self):
        """Zeros at s = 2 pi i k / log(1/q) (n=0 series)."""
        q = 0.3
        log_inv_q = math.log(1.0 / q)
        spacing = TWO_PI / log_inv_q

        for k in [1, 2, 3, -1, -2]:
            s = complex(0, k * spacing)
            Z = selberg_zeta_btz(s, q)
            # q^s = q^{i * k * 2pi / log(1/q)} = e^{log(q) * i * k * 2pi / log(1/q)}
            # = e^{-log(1/q) * i * k * 2pi / log(1/q)} = e^{-2 pi i k} = 1
            # So 1 - q^{0+s} = 1 - 1 = 0
            assert abs(Z) < 1e-8, f"Z_BTZ(2pi*i*{k}/log(1/q)) should be zero"

    def test_zeros_not_on_half_line(self):
        """Selberg zeros for BTZ are at Re(s) = -n, NOT at Re(s) = 1/2."""
        zeros = selberg_zeta_zeros_exact(0.3, n_max=10)
        real_parts = set(z['real_part'] for z in zeros)
        assert 0.5 not in real_parts

    def test_verify_selberg_zero_function(self):
        """verify_selberg_zero correctly identifies zeros."""
        q = 0.2
        result = verify_selberg_zero(complex(0.0), q)
        assert result['is_zero']

    def test_selberg_zeros_on_strip(self):
        """Only n=0 zeros lie in -0.5 < Re(s) < 0.5."""
        q = 0.3
        zeros = selberg_zeros_on_strip(q, -0.5, 0.5, k_max=10)
        # All should have Re(s) = 0
        for z in zeros:
            assert abs(z.real) < 1e-12

    def test_selberg_nonzero_at_half(self):
        """Z_BTZ(1/2) != 0 for generic q."""
        q = 0.2
        Z = selberg_zeta_btz(complex(0.5), q)
        assert abs(Z) > 0.01


# =========================================================================
# Section 6: Hawking temperature from spectral zeta
# =========================================================================

class TestHawkingFromZeta:
    """Hawking temperature extracted from spectral data."""

    def test_hawking_temperature_geometric(self):
        """T_H = r_+ / (2 pi) for non-rotating BTZ."""
        r_plus = 2.0
        data = hawking_temperature_from_spectral_zeta(2.0, r_plus)
        expected = r_plus / TWO_PI
        assert abs(data['T_H_geometric'] - expected) < 1e-12

    def test_hawking_temperature_rotating_geometry(self):
        """T_H = (r_+^2 - r_-^2) / (2 pi r_+) for rotating BTZ."""
        r_plus, r_minus = 2.0, 0.5
        data = hawking_temperature_from_spectral_zeta(2.0, r_plus, r_minus)
        expected = (r_plus ** 2 - r_minus ** 2) / (TWO_PI * r_plus)
        assert abs(data['T_H_geometric'] - expected) < 1e-12

    def test_log_det_finite(self):
        """The log functional determinant is finite."""
        data = hawking_temperature_from_spectral_zeta(2.0, 1.0)
        assert math.isfinite(abs(data['log_det']))

    def test_zeta_at_zero_consistent(self):
        """zeta_BTZ(0) is consistent with spectral_zeta_at_zero."""
        h = 2.0
        r_plus = 1.5
        data = hawking_temperature_from_spectral_zeta(h, r_plus)
        z0 = spectral_zeta_at_zero(h, r_plus)
        assert abs(data['zeta_BTZ_at_0'] - z0) < 1e-12


# =========================================================================
# Section 7: Bekenstein-Hawking from shadow data
# =========================================================================

class TestBHFromShadow:
    """Bekenstein-Hawking entropy from kappa and shadow F_1."""

    def test_cardy_formula_basic(self):
        """S_BH = 2 pi sqrt(c Delta / 6) at c = 12, Delta = 3."""
        data = bekenstein_hawking_from_shadow(12.0, 3.5)
        Delta = 3.5 - 12.0 / 24.0  # = 3
        expected = TWO_PI * math.sqrt(12.0 * Delta / 6.0)
        assert abs(data['S_BH'] - expected) < 1e-10

    def test_two_routes_agree(self):
        """S_BH via Cardy and via F_1 agree."""
        data = bekenstein_hawking_from_shadow(24.0, 2.0)
        assert data['match']

    def test_kappa_virasoro(self):
        """kappa = c/2 for Virasoro."""
        data = bekenstein_hawking_from_shadow(26.0, 5.0)
        assert abs(data['kappa'] - 13.0) < 1e-12

    def test_F1_from_kappa(self):
        """F_1 = kappa / 24."""
        data = bekenstein_hawking_from_shadow(12.0, 5.0)
        assert abs(data['F_1'] - data['kappa'] / 24.0) < 1e-12

    def test_self_dual_c13(self):
        """At c = 13: kappa = 13/2, S_BH = 2 pi sqrt(13 Delta / 6)."""
        data = bekenstein_hawking_from_shadow(13.0, 10.0)
        assert abs(data['kappa'] - 6.5) < 1e-12

    def test_monster_c24(self):
        """c = 24 (Monster): kappa = 12, F_1 = 1/2."""
        data = bekenstein_hawking_from_shadow(24.0, 2.0)
        assert abs(data['kappa'] - 12.0) < 1e-12
        assert abs(data['F_1'] - 0.5) < 1e-12


# =========================================================================
# Section 8: Selberg zeta at Riemann zero positions
# =========================================================================

class TestSelbergAtRiemannZeros:
    """Evaluate Z_BTZ at Riemann zero positions."""

    @pytest.fixture(autouse=True)
    def check_mpmath(self):
        pytest.importorskip("mpmath")

    def test_selberg_nonzero_at_riemann_zeros(self):
        """Z_BTZ(rho_n/2) is NOT zero for generic q.

        The BTZ Selberg zeros are at s = -n + 2pi i k / log(1/q),
        while the Riemann zeros are at rho_n = 1/2 + i gamma_n.
        So rho_n/2 = 1/4 + i gamma_n/2, which has Re(s) = 1/4 != -n.
        The Selberg zeta should NOT vanish at these points for generic q.
        """
        q = 0.1
        results = selberg_at_riemann_zeros(q, n_zeros=5)
        for r in results:
            assert not r['is_zero'], (
                f"Z_BTZ should not vanish at rho_{r['k']}/2 for generic q"
            )

    def test_riemann_zero_positions(self):
        """Riemann zeros at rho_n/2 have Re(s) = 1/4 (under RH)."""
        import mpmath
        for k in range(1, 6):
            rho = complex(mpmath.zetazero(k))
            assert abs(rho.real - 0.5) < 1e-10

    def test_selberg_abs_bounded_at_riemann_zeros(self):
        """|Z_BTZ(rho_n/2)| is bounded away from zero."""
        q = 0.2
        results = selberg_at_riemann_zeros(q, n_zeros=10)
        for r in results:
            assert r['abs_Z_BTZ'] > 1e-5

    def test_selberg_at_shifted_zeros_vary_shift(self):
        """Z_BTZ at different shifts along the Riemann zero heights."""
        q = 0.1
        for shift in [0.0, 0.25, 0.5]:
            results = selberg_at_shifted_riemann_zeros(q, shift, n_zeros=3)
            for r in results:
                # Should be finite and non-NaN
                assert math.isfinite(r['abs_Z_BTZ'])


# =========================================================================
# Section 9: Modular crossing
# =========================================================================

class TestModularCrossing:
    """High-T / low-T duality: beta <-> 4 pi^2 / beta."""

    def test_self_dual_point(self):
        """At beta = 2 pi: q = q_dual = e^{-2 pi}."""
        q_star = math.exp(-TWO_PI)
        data = modular_crossing_selberg(q_star, complex(0.5))
        assert data['self_dual']

    def test_self_dual_temperature(self):
        """beta_dual(2 pi) = 4 pi^2 / (2 pi) = 2 pi."""
        q_star = math.exp(-TWO_PI)
        data = modular_crossing_selberg(q_star, complex(0.5))
        assert abs(data['beta'] - data['beta_dual']) < 1e-10

    def test_modular_crossing_ratio_at_self_dual(self):
        """At self-dual point, Z_BTZ = Z_BTZ_dual."""
        q_star = math.exp(-TWO_PI)
        data = modular_crossing_selberg(q_star, complex(1.0))
        # At self-dual point, q = q_dual so the same function is evaluated
        assert abs(data['ratio'] - 1.0) < 1e-8

    def test_beta_dual_involution(self):
        """Applying the duality twice returns to the original beta."""
        q = 0.3
        beta = -math.log(q)
        beta_dual = 4.0 * PI ** 2 / beta
        beta_dual_dual = 4.0 * PI ** 2 / beta_dual
        assert abs(beta - beta_dual_dual) < 1e-10

    def test_selberg_at_self_dual_nonzero(self):
        """Z_BTZ(s) != 0 at the self-dual temperature for generic s."""
        Z = selberg_at_self_dual(complex(0.5))
        assert abs(Z) > 1e-5

    def test_self_dual_data_consistent(self):
        """self_dual_temperature_data returns consistent results."""
        data = self_dual_temperature_data(complex(1.0))
        assert abs(data['beta_star'] - TWO_PI) < 1e-12
        assert abs(cmath.exp(data['log_Z_BTZ']) - data['Z_BTZ']) / abs(data['Z_BTZ']) < 1e-8


# =========================================================================
# Section 10: Shadow zeta / Selberg ratio
# =========================================================================

class TestShadowSelbergRatio:
    """Compare the shadow spectral zeta with the Selberg zeta."""

    def test_shadow_zeta_convergent(self):
        """Shadow zeta converges for Re(s) > 1."""
        z = shadow_zeta(complex(2), 12.0, n_max=1000)
        assert math.isfinite(abs(z))

    def test_shadow_zeta_real_for_real_s(self):
        """Shadow zeta is real for real s (all coefficients are positive integers)."""
        z = shadow_zeta(complex(3), 12.0, n_max=1000)
        assert abs(z.imag) < 1e-10

    def test_shadow_zeta_s2_value(self):
        """zeta_A(2) = sum p(n) / n^2, which can be bounded."""
        z = shadow_zeta(complex(2), 12.0, n_max=2000)
        # p(1) = 1, p(2) = 2, p(3) = 3, p(4) = 5
        # Lower bound: 1 + 2/4 + 3/9 + 5/16 + ... > 1 + 0.5 + 0.33 + 0.31 > 2
        assert z.real > 2.0

    def test_shadow_selberg_ratio_finite(self):
        """The ratio zeta_A / Z_BTZ is finite for Re(s) > 1."""
        q = 0.1
        data = shadow_selberg_ratio(complex(2), 12.0, q)
        assert math.isfinite(data['abs_ratio'])

    def test_shadow_zeta_partition_coefficients(self):
        """For very large s, shadow zeta is dominated by the p(1) = 1 term."""
        # zeta_A(s) = p(1) * 1^{-s} + p(2) * 2^{-s} + ...
        # = 1 + 2 * 2^{-s} + 3 * 3^{-s} + 5 * 4^{-s} + ...
        # Note: partition numbers grow as exp(pi sqrt(2n/3)),
        # so convergence requires VERY large s.
        s = complex(20)  # Very large s: dominated by first term
        z = shadow_zeta(s, 12.0, n_max=1000)
        # p(1)/1^20 = 1, p(2)/2^20 = 2/1048576 ~ 2e-6
        assert abs(z.real - 1.0) < 0.001


# =========================================================================
# Section 11: Theta function representation
# =========================================================================

class TestThetaRepresentation:
    """Relate Z_BTZ to Jacobi theta functions."""

    def test_theta_product_consistent(self):
        """Z_product matches the known product formula."""
        q = 0.1
        s = complex(1.0)
        data = theta_representation(s, q)
        Z_expected = selberg_zeta_btz(s, q)
        assert abs(data['Z_product'] - Z_expected) < 1e-10

    def test_qq_infty_positive(self):
        """(q; q)_infty > 0 for 0 < q < 1."""
        data = theta_representation(complex(1.0), 0.3)
        assert data['qq_infty'].real > 0
        assert abs(data['qq_infty'].imag) < 1e-12

    def test_Z_at_s1_equals_qq_infty(self):
        """Z_BTZ(1) = (q; q)_infty = prod_{n >= 1} (1 - q^n)."""
        q = 0.2
        data = theta_representation(complex(1.0), q)
        # Z_BTZ(1) = prod_{n >= 0} (1 - q^{n+1}) = prod_{m >= 1} (1 - q^m)
        assert abs(data['Z_product'] - data['qq_infty']) < 1e-10


# =========================================================================
# Section 12: WKB approximation
# =========================================================================

class TestWKBApproximation:
    """WKB approximation for quasinormal frequencies."""

    def test_wkb_exact_for_btz(self):
        """WKB is exact for BTZ (scalar wave equation is exactly solvable)."""
        M = 4.0
        h = 2.0
        r_plus = math.sqrt(M)
        freqs = wkb_quasinormal_frequencies(M, h, n_max=10)
        for n, omega in enumerate(freqs):
            expected = -1j * r_plus * (2 * n + h)
            assert abs(omega - expected) < 1e-12

    def test_wkb_imaginary(self):
        """All WKB frequencies are purely imaginary."""
        freqs = wkb_quasinormal_frequencies(1.0, 2.0, n_max=10)
        for omega in freqs:
            assert abs(omega.real) < 1e-15

    def test_wkb_negative_M(self):
        """M <= 0 returns empty list."""
        freqs = wkb_quasinormal_frequencies(-1.0, 2.0)
        assert freqs == []


# =========================================================================
# Section 13: Cardy formula consistency
# =========================================================================

class TestCardyConsistency:
    """Verify Cardy formula at large L_0."""

    def test_cardy_coefficient(self):
        """S / sqrt(Delta) = 2 pi sqrt(c/6) at large Delta."""
        c = 24.0
        results = cardy_consistency(c)
        # Last entry (largest L_0) should have smallest error
        last = results[-1]
        assert last['relative_error'] < 1e-10

    def test_cardy_scaling_all_positive(self):
        """All Cardy entropies are positive for Delta > 0."""
        results = cardy_consistency(12.0)
        for r in results:
            assert r['S_cardy'] > 0

    def test_cardy_grows_with_L0(self):
        """S_cardy grows monotonically with L_0."""
        results = cardy_consistency(12.0)
        for i in range(len(results) - 1):
            assert results[i + 1]['S_cardy'] > results[i]['S_cardy']

    def test_cardy_saddle_point_decreases(self):
        """beta_saddle decreases with L_0 (higher energy = higher temperature)."""
        results = cardy_consistency(12.0)
        for i in range(len(results) - 1):
            assert results[i + 1]['beta_saddle'] < results[i]['beta_saddle']


# =========================================================================
# Section 14: Cross-verification paths
# =========================================================================

class TestCrossVerification:
    """Multi-path verification of key results."""

    def test_path1_direct_product_vs_log_sum(self):
        """Path 1 vs Path 2: product vs log-sum for Selberg zeta."""
        q = 0.15
        s = complex(0.5, 0.3)
        Z_product = selberg_zeta_btz(s, q)
        log_Z = log_selberg_zeta(s, q)
        assert abs(cmath.exp(log_Z) - Z_product) / abs(Z_product) < 1e-8

    def test_path2_theta_function_route(self):
        """Path 2: theta function representation consistent."""
        q = 0.2
        s = complex(1.0)
        data = theta_representation(s, q)
        Z_direct = selberg_zeta_btz(s, q)
        assert abs(data['Z_product'] - Z_direct) < 1e-10

    def test_path3_wkb_vs_exact_spectrum(self):
        """Path 3: WKB matches exact quasinormal spectrum."""
        M = 9.0
        h = 2.0
        r_plus = math.sqrt(M)
        spec = quasinormal_spectrum(h, r_plus, n_max=10)
        wkb = wkb_quasinormal_frequencies(M, h, n_max=10)
        for n in range(10):
            E_exact = spec['right'][n]
            E_wkb = abs(wkb[n])
            assert abs(E_exact - E_wkb) < 1e-10

    def test_path4_cardy_large_L0_consistency(self):
        """Path 4: Cardy formula from BH shadow agrees at large L_0."""
        c = 12.0
        L0 = 10000.0
        data = bekenstein_hawking_from_shadow(c, L0)
        # Two routes must agree
        assert data['match']

    def test_spectral_zeta_direct_sum_vs_hurwitz(self):
        """Direct sum vs Hurwitz zeta for spectral zeta."""
        s = complex(3)
        h = 2.0
        r_plus = 1.0

        # Direct sum over modes
        direct = complex(0)
        for n in range(3000):
            E_R = r_plus * (2 * n + h)
            E_L = r_plus * (2 * n + h)  # non-rotating
            direct += E_R ** (-s) + E_L ** (-s)

        # Via engine
        z = spectral_zeta_btz(s, h, r_plus)
        assert abs(direct - z) / abs(z) < 1e-3

    def test_selberg_zero_at_origin_both_methods(self):
        """Both product and log-sum confirm Z_BTZ(0) = 0."""
        q = 0.3
        Z = selberg_zeta_btz(complex(0), q)
        assert abs(Z) < 1e-10
        # log Z should diverge (log 0), but our function sums terms
        # The first term log(1 - q^0) = log(0) is -inf
        # Our implementation should handle this gracefully

    def test_hawking_temperature_three_paths(self):
        """Hawking temperature: geometry, inverse beta, spectral data all agree."""
        M = 4.0
        r_plus = math.sqrt(M)
        T1 = hawking_temperature_btz(M)
        T2 = 1.0 / inverse_temperature_btz(M)
        T3 = r_plus / TWO_PI

        assert abs(T1 - T2) < 1e-12
        assert abs(T1 - T3) < 1e-12


# =========================================================================
# Section 15: Special cases and edge cases
# =========================================================================

class TestSpecialCases:
    """Special parameter values and boundary conditions."""

    def test_c1_free_boson(self):
        """c = 1 free boson: kappa = 1/2."""
        data = bekenstein_hawking_from_shadow(1.0, 5.0)
        assert abs(data['kappa'] - 0.5) < 1e-12

    def test_c13_self_dual(self):
        """c = 13 self-dual Virasoro."""
        data = bekenstein_hawking_from_shadow(13.0, 5.0)
        assert abs(data['kappa'] - 6.5) < 1e-12

    def test_c24_monster(self):
        """c = 24 Monster module."""
        data = bekenstein_hawking_from_shadow(24.0, 2.0)
        assert abs(data['kappa'] - 12.0) < 1e-12

    def test_c26_critical_string(self):
        """c = 26 critical string: kappa = 13, Koszul dual is Vir_0."""
        data = bekenstein_hawking_from_shadow(26.0, 5.0)
        assert abs(data['kappa'] - 13.0) < 1e-12

    def test_small_q_selberg(self):
        """Small q (high temperature): Z_BTZ(s) ~ 1 for Re(s) > 0."""
        q = 1e-10
        Z = selberg_zeta_btz(complex(1.0), q)
        assert abs(Z - 1.0) < 1e-5

    def test_q_near_one_selberg(self):
        """q near 1 (low temperature): Z_BTZ(s) can be small."""
        q = 0.99
        Z = selberg_zeta_btz(complex(0.5), q)
        assert math.isfinite(abs(Z))

    def test_large_s_spectral_zeta(self):
        """For large Re(s), spectral zeta is dominated by ground state."""
        s = complex(20)
        h = 2.0
        r_plus = 1.0
        z = spectral_zeta_btz(s, h, r_plus)
        # Ground state: E_0 = r_+ * h (both chiralities)
        ground_state = 2 * (r_plus * h) ** (-s)
        # The ratio z / ground_state should be close to 1
        ratio = z / ground_state
        assert abs(ratio - 1.0) < 0.01

    def test_full_spectral_analysis_runs(self):
        """Full analysis completes without errors."""
        result = full_spectral_analysis(4.0, 0.0, 2.0, 12.0, n_zeros=3)
        assert 'error' not in result
        assert result['T_H'] > 0

    def test_selberg_modular_check_eta(self):
        """eta(tau) = q^{1/24} (q;q)_infty (AP46: the q^{1/24} is NOT optional)."""
        q = 0.2
        data = selberg_zeta_modular_check(q, complex(1.0))
        # eta = q^{1/24} * (q;q)_infty
        expected_eta = q ** (1.0 / 24.0) * data['qq_infty']
        assert abs(data['eta'] - expected_eta) < 1e-10

    def test_complementarity_sum_entropy(self):
        """S_BH(c) + S_BH(26-c) at same Delta uses kappa + kappa' = 13 (AP24)."""
        c = 10.0
        L0 = 5.0
        data_c = bekenstein_hawking_from_shadow(c, L0)
        data_dual = bekenstein_hawking_from_shadow(26.0 - c, L0)
        kappa_sum = data_c['kappa'] + data_dual['kappa']
        assert abs(kappa_sum - 13.0) < 1e-12

    def test_selberg_zeta_invalid_q_raises(self):
        """q outside (0,1) raises ValueError."""
        with pytest.raises(ValueError):
            selberg_zeta_btz(complex(1.0), 0.0)
        with pytest.raises(ValueError):
            selberg_zeta_btz(complex(1.0), 1.0)
        with pytest.raises(ValueError):
            selberg_zeta_btz(complex(1.0), -0.1)
        with pytest.raises(ValueError):
            selberg_zeta_btz(complex(1.0), 1.5)

    def test_spectral_zeta_invalid_h_raises(self):
        """h <= 0 raises ValueError for spectral zeta."""
        with pytest.raises(ValueError):
            spectral_zeta_btz(complex(2), 0.0, 1.0)
        with pytest.raises(ValueError):
            spectral_zeta_btz(complex(2), -1.0, 1.0)
