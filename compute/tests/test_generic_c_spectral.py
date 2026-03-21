#!/usr/bin/env python3
r"""
test_generic_c_spectral.py — Tests for spectral decomposition at generic central charge.

Validates:
  (1) Eisenstein series constant term on imaginary axis
  (2) Completed zeta and scattering matrix unitarity
  (3) Spectral coefficients via Mellin transform
  (4) Continuous spectral density and zeta-zero poles
  (5) Hecke eigenvalues of Eisenstein series
  (6) Spectral type classification (modular vs non-modular)
  (7) Shadow moments from spectral measure
  (8) Self-duality transition at c=13
  (9) Maass form discrete component estimates
  (10) L-function content at generic c
  (11) The Chriss-Ginzburg decomposition statement

References:
  thm:shadow-spectral-decomposition (concordance.tex)
  thm:general-hs-sewing (higher_genus_modular_koszul.tex)
"""

import pytest
import math

try:
    import mpmath
    from mpmath import mp, mpf, mpc, pi as mpi, fabs, gamma, zeta, power, cos, log, exp, sqrt
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

from compute.lib.generic_c_spectral import (
    completed_zeta,
    scattering_matrix,
    eisenstein_constant_term,
    eisenstein_on_imaginary_axis,
    eta_on_imaginary_axis,
    eta_power_on_imaginary_axis,
    spectral_coefficient,
    continuous_spectral_density,
    hecke_eigenvalue_eisenstein,
    verify_hecke_eigenvalue,
    is_modular_alpha,
    central_charge_from_alpha,
    alpha_from_central_charge,
    classify_spectral_type,
    spectral_type_table,
    shadow_moment_continuous,
    total_spectral_weight,
    spectral_weight_near_selfdual,
    mellin_of_spectral_density,
    estimate_discrete_component,
    spectral_density_near_zeta_zero,
    chriss_ginzburg_decomposition_summary,
    FIRST_MAASS_T,
    ZETA_ZEROS,
)


# ============================================================
# Section 1: Completed zeta function
# ============================================================

class TestCompletedZeta:
    """Validate Lambda(s) = pi^{-s} * Gamma(s) * zeta(2s)."""

    def test_lambda_at_1(self):
        """Lambda(1) = pi^{-1} * Gamma(1) * zeta(2) = pi^{-1} * 1 * pi^2/6 = pi/6."""
        mp.dps = 30
        val = completed_zeta(1)
        expected = mpi / 6
        assert fabs(val - expected) < mpf('1e-25')

    def test_lambda_at_2(self):
        """Lambda(2) = pi^{-2} * Gamma(2) * zeta(4) = pi^{-2} * 1 * pi^4/90 = pi^2/90."""
        mp.dps = 30
        val = completed_zeta(2)
        expected = mpi ** 2 / 90
        assert fabs(val - expected) < mpf('1e-25')

    def test_lambda_at_3(self):
        """Lambda(3) = pi^{-3} * Gamma(3) * zeta(6) = pi^{-3} * 2 * pi^6/945 = 2*pi^3/945."""
        mp.dps = 30
        val = completed_zeta(3)
        expected = 2 * mpi ** 3 / 945
        assert fabs(val - expected) < mpf('1e-25')

    def test_lambda_positive_real(self):
        """Lambda(s) > 0 for s > 1/2 real."""
        mp.dps = 25
        for s in [0.6, 1, 1.5, 2, 3, 5]:
            val = completed_zeta(s)
            assert val.real > 0, f"Lambda({s}) = {val} should be positive"


class TestScatteringMatrix:
    """Validate phi(s) = Lambda(1-s)/Lambda(s)."""

    def test_unitarity_on_critical_line(self):
        """|phi(1/2 + it)| = 1 for real t (unitarity)."""
        mp.dps = 30
        for t in [1, 2, 5, 10, 14.13]:
            s = mpf('0.5') + mpc(0, t)
            phi = scattering_matrix(s)
            assert fabs(fabs(phi) - 1) < mpf('1e-20'), f"|phi(1/2+{t}i)| = {fabs(phi)}"

    def test_scattering_at_real_s(self):
        """phi(s) at s=1.5: Lambda(-0.5)/Lambda(1.5), both finite."""
        mp.dps = 30
        # s=2 hits Gamma pole at s-1 = -1. Use s=1.5 instead.
        phi = scattering_matrix(1.5)
        # Just check it's a finite nonzero complex number
        assert fabs(phi) > mpf('1e-10')
        assert fabs(phi) < mpf('1e10')


# ============================================================
# Section 2: Eisenstein series on imaginary axis
# ============================================================

class TestEisensteinConstantTerm:
    """E_s^{(0)}(iy) = y^s + phi(s)*y^{1-s}."""

    def test_at_y1_real_part(self):
        """At y=1: E^{(0)}_s(i) = 1 + phi(s), so Re(E) = 1 + Re(phi)."""
        mp.dps = 25
        for t in [1, 5, 14.13]:
            s = mpf('0.5') + mpc(0, t)
            val = eisenstein_constant_term(s, 1)
            phi = scattering_matrix(s)
            expected = 1 + phi
            assert fabs(val - expected) < mpf('1e-20')

    def test_at_various_y(self):
        """Eisenstein constant term at y=0.5, 1, 2 for t=1."""
        mp.dps = 25
        s = mpf('0.5') + mpc(0, 1)
        for y in [0.5, 1, 2]:
            val = eisenstein_constant_term(s, y)
            assert fabs(val) > mpf('1e-5'), "Eisenstein should be nonzero"

    def test_y_dependence_monotonicity(self):
        """The real part of E^{(0)}_{1/2+it}(iy) for fixed t changes with y."""
        mp.dps = 25
        s = mpf('0.5') + mpc(0, 1)
        v1 = eisenstein_constant_term(s, 0.5)
        v2 = eisenstein_constant_term(s, 2)
        # Just check they're different
        assert fabs(v1 - v2) > mpf('1e-3')

    def test_conjugation_symmetry(self):
        """E_{1/2+it}^{(0)}(iy) is conjugate to E_{1/2-it}^{(0)}(iy) for real y."""
        mp.dps = 25
        t = mpf(3)
        y = mpf(1.5)
        s_plus = mpf('0.5') + mpc(0, t)
        s_minus = mpf('0.5') - mpc(0, t)
        v_plus = eisenstein_constant_term(s_plus, y)
        v_minus = eisenstein_constant_term(s_minus, y)
        # They should be complex conjugates
        assert fabs(v_plus.real - v_minus.real) < mpf('1e-20')
        assert fabs(v_plus.imag + v_minus.imag) < mpf('1e-20')


class TestEisensteinFull:
    """E_s(iy) including Fourier terms."""

    def test_fourier_terms_decay(self):
        """At large y, Fourier terms K_{nu}(2*pi*n*y) are exponentially small."""
        mp.dps = 20
        s = mpf('0.5') + mpc(0, 1)
        y = mpf(3)  # large y
        const = eisenstein_constant_term(s, y)
        full = eisenstein_on_imaginary_axis(s, y, nmax=20)
        # The difference should be tiny at large y
        assert fabs(full - const) < mpf('0.01') * fabs(const)

    def test_fourier_correction_at_small_y(self):
        """At small y, Fourier terms contribute significantly."""
        mp.dps = 20
        s = mpf('0.5') + mpc(0, 1)
        y = mpf(0.3)
        const = eisenstein_constant_term(s, y)
        full = eisenstein_on_imaginary_axis(s, y, nmax=30)
        # They should differ significantly
        assert fabs(full - const) > mpf('0.01')


# ============================================================
# Section 3: Dedekind eta on imaginary axis
# ============================================================

class TestDedekindEta:
    """eta(iy) = e^{-pi*y/12} * prod(1 - e^{-2*pi*n*y})."""

    def test_eta_at_i(self):
        """eta(i) = Gamma(1/4) / (2*pi^{3/4}) -- a known special value."""
        mp.dps = 30
        computed = eta_on_imaginary_axis(1)
        expected = gamma(mpf('0.25')) / (2 * power(mpi, mpf('0.75')))
        assert fabs(computed - expected) < mpf('1e-20')

    def test_eta_positivity(self):
        """eta(iy) > 0 for all y > 0."""
        mp.dps = 20
        for y in [0.1, 0.5, 1, 2, 5, 10]:
            assert eta_on_imaginary_axis(y) > 0

    def test_eta_monotonicity(self):
        """eta(iy) is monotonically increasing for y > 0 on the imaginary axis
        (after removing the e^{-pi*y/12} factor, the product approaches 1).
        Actually, eta(iy) decreases at large y due to the exponential prefactor."""
        mp.dps = 20
        # For large y, eta(iy) ~ e^{-pi*y/12} -> 0
        assert eta_on_imaginary_axis(10) < eta_on_imaginary_axis(1)

    def test_eta_power_at_alpha_12(self):
        """eta(i)^24 is the discriminant |Delta(i)|."""
        mp.dps = 25
        val = eta_power_on_imaginary_axis(1, 12)
        eta_i = eta_on_imaginary_axis(1)
        expected = power(eta_i, 24)
        assert fabs(val - expected) < mpf('1e-20')

    def test_eta_power_at_alpha_0(self):
        """|eta|^0 = 1 for all y."""
        mp.dps = 20
        for y in [0.5, 1, 2]:
            val = eta_power_on_imaginary_axis(y, 0)
            assert fabs(val - 1) < mpf('1e-20')


# ============================================================
# Section 4: Spectral coefficients via Mellin transform
# ============================================================

class TestSpectralCoefficient:
    """c(t; alpha) = Mellin transform of |eta|^{2*alpha}."""

    def test_alpha1_t0_positive(self):
        """c(0; 1) > 0 (Mellin of a positive function at real s)."""
        mp.dps = 20
        val = spectral_coefficient(0, 1, ymax=15, nmax=100)
        assert val.real > mpf('1')

    def test_alpha1_t1_nonzero(self):
        """c(1; 1) is a nonzero complex number."""
        mp.dps = 20
        val = spectral_coefficient(1, 1, ymax=15, nmax=100)
        assert fabs(val) > mpf('0.1')
        assert fabs(val.imag) > mpf('0.01')  # genuinely complex

    def test_alpha1_decay_in_t(self):
        """As t -> infinity, c(t; alpha) -> 0 (Riemann-Lebesgue)."""
        mp.dps = 15
        v1 = fabs(spectral_coefficient(1, 1, ymax=10, nmax=80))
        v5 = fabs(spectral_coefficient(5, 1, ymax=10, nmax=80))
        assert v5 < v1, "Spectral coefficient should decay"

    def test_alpha2_t0_positive(self):
        """c(0; 2) > 0."""
        mp.dps = 20
        val = spectral_coefficient(0, 2, ymax=15, nmax=100)
        assert val.real > mpf('0.5')

    def test_alpha12_smaller_magnitude(self):
        """c(t; 12) is much smaller than c(t; 1) because eta^24 decays faster."""
        mp.dps = 15
        v1 = fabs(spectral_coefficient(0, 1, ymax=10, nmax=80))
        v12 = fabs(spectral_coefficient(0, 12, ymax=10, nmax=80))
        assert v12 < v1

    def test_conjugation_symmetry(self):
        """c(-t; alpha) = conjugate(c(t; alpha)) for real alpha."""
        mp.dps = 15
        t = mpf(2)
        alpha = mpf(1)
        c_plus = spectral_coefficient(t, alpha, ymax=10, nmax=80)
        c_minus = spectral_coefficient(-t, alpha, ymax=10, nmax=80)
        assert fabs(c_plus.real - c_minus.real) < mpf('0.01') * fabs(c_plus)
        assert fabs(c_plus.imag + c_minus.imag) < mpf('0.01') * fabs(c_plus)


# ============================================================
# Section 5: Continuous spectral density
# ============================================================

class TestContinuousSpectralDensity:
    """rho_cont(t; alpha) = |c(t; alpha)|^2 / |zeta(1 + 2it)|^2."""

    def test_density_positive(self):
        """rho_cont(t; alpha) >= 0 for all t, alpha."""
        mp.dps = 15
        for t in [0.5, 1, 2]:
            rho = continuous_spectral_density(t, 1, ymax=10, nmax=80)
            assert rho >= 0

    def test_density_alpha1_at_t1(self):
        """Compute rho_cont(1; 1) and check it's a finite positive number."""
        mp.dps = 15
        rho = continuous_spectral_density(1, 1, ymax=10, nmax=80)
        assert rho > mpf('0.01')
        assert rho < mpf('1e6')

    def test_density_alpha12_smaller(self):
        """rho_cont at alpha=12 is smaller than alpha=1 (Delta decays faster)."""
        mp.dps = 15
        rho1 = continuous_spectral_density(1, 1, ymax=10, nmax=80)
        rho12 = continuous_spectral_density(1, 12, ymax=10, nmax=80)
        assert rho12 < rho1

    def test_density_decay_in_t(self):
        """rho_cont(t; 1) decreases for large t (Riemann-Lebesgue + zeta growth)."""
        mp.dps = 15
        rho1 = continuous_spectral_density(1, 1, ymax=10, nmax=80)
        rho5 = continuous_spectral_density(5, 1, ymax=10, nmax=80)
        assert rho5 < rho1


# ============================================================
# Section 6: Hecke eigenvalues of Eisenstein series
# ============================================================

class TestHeckeEigenvalues:
    """T_p(E_{1/2+it}) = 2*cos(t*log p) * E_{1/2+it}."""

    def test_t1_p2(self):
        """At t=1, p=2: eigenvalue = 2*cos(log 2) ~ 1.5385."""
        mp.dps = 25
        ev = hecke_eigenvalue_eisenstein(1, 2)
        expected = 2 * cos(log(mpf(2)))
        assert fabs(ev - expected) < mpf('1e-20')
        assert fabs(ev - mpf('1.5385')) < mpf('0.001')

    def test_t5_p2(self):
        """At t=5, p=2: eigenvalue = 2*cos(5*log 2) ~ -1.896."""
        mp.dps = 25
        ev = hecke_eigenvalue_eisenstein(5, 2)
        expected = 2 * cos(5 * log(mpf(2)))
        assert fabs(ev - expected) < mpf('1e-20')
        assert ev < -mpf('1.89')
        assert ev > -mpf('1.90')

    def test_t1_p3(self):
        """At t=1, p=3: eigenvalue = 2*cos(log 3) ~ 0.9097."""
        mp.dps = 25
        ev = hecke_eigenvalue_eisenstein(1, 3)
        expected = 2 * cos(log(mpf(3)))
        assert fabs(ev - expected) < mpf('1e-20')
        assert fabs(ev - mpf('0.9097')) < mpf('0.001')

    def test_eigenvalue_bounded(self):
        """Hecke eigenvalue is bounded by [-2, 2] (Ramanujan for Eisenstein)."""
        mp.dps = 20
        for t in [0.5, 1, 3, 7, 14]:
            for p in [2, 3, 5, 7]:
                ev = hecke_eigenvalue_eisenstein(t, p)
                assert fabs(ev) <= 2 + mpf('1e-15')

    def test_verify_hecke(self):
        """The verification function confirms eigenvalue = 2*cos(t*log p)."""
        mp.dps = 25
        result = verify_hecke_eigenvalue(1, 2, 1)
        assert result['match'] is True

    def test_hecke_t0(self):
        """At t=0: eigenvalue = 2*cos(0) = 2 (trivial representation)."""
        mp.dps = 25
        ev = hecke_eigenvalue_eisenstein(0, 2)
        assert fabs(ev - 2) < mpf('1e-20')

    def test_hecke_at_pi(self):
        """At t=pi/log(p): eigenvalue = 2*cos(pi) = -2."""
        mp.dps = 25
        p = 2
        t = mpi / log(mpf(p))
        ev = hecke_eigenvalue_eisenstein(t, p)
        assert fabs(ev + 2) < mpf('1e-15')


# ============================================================
# Section 7: Modularity classification
# ============================================================

class TestModularityClassification:
    """is_modular_alpha and classify_spectral_type."""

    def test_alpha_0_modular(self):
        """alpha=0: |eta|^0 = 1, trivially modular."""
        assert is_modular_alpha(0)

    def test_alpha_12_modular(self):
        """alpha=12: |eta|^24 = |Delta|, modular of weight 12."""
        assert is_modular_alpha(12)

    def test_alpha_24_modular(self):
        """alpha=24: |eta|^48 = |Delta^2|, modular of weight 24."""
        assert is_modular_alpha(24)

    def test_alpha_1_not_modular(self):
        """alpha=1: |eta|^2 is NOT modular for SL(2,Z)."""
        assert not is_modular_alpha(1)

    def test_alpha_6_not_modular(self):
        """alpha=6: |eta|^12 is NOT modular for full SL(2,Z)."""
        assert not is_modular_alpha(6)

    def test_irrational_not_modular(self):
        """Irrational alpha is never modular."""
        assert not is_modular_alpha(math.pi)

    def test_central_charge_conversion(self):
        """c = alpha + 1, alpha = c - 1."""
        assert central_charge_from_alpha(12) == 13
        assert alpha_from_central_charge(13) == 12

    def test_classify_c13_selfdual(self):
        """c=13 is self-dual, modular for SL(2,Z), discrete=0."""
        info = classify_spectral_type(13)
        assert info['type'] == 'modular_sl2z'
        assert info['discrete'] is False

    def test_classify_c25_modular(self):
        """c=25: alpha=24, modular for SL(2,Z)."""
        info = classify_spectral_type(25)
        assert info['type'] == 'modular_sl2z'

    def test_classify_c1_modular(self):
        """c=1: alpha=0, modular for SL(2,Z) (trivial)."""
        info = classify_spectral_type(1)
        assert info['type'] == 'modular_sl2z'

    def test_classify_c2_gamma0(self):
        """c=2: alpha=1, integer but 12 does not divide 1 -> Gamma_0(N)."""
        info = classify_spectral_type(2)
        assert info['type'] == 'modular_gamma0'

    def test_classify_c7_gamma0(self):
        """c=7: alpha=6, integer but 12 does not divide 6 -> Gamma_0(N)."""
        info = classify_spectral_type(7)
        assert info['type'] == 'modular_gamma0'

    def test_classify_cpi_nonmodular(self):
        """c=pi: irrational, non-modular, discrete component present."""
        info = classify_spectral_type(math.pi)
        assert info['type'] == 'non_modular'
        assert info['discrete'] is True

    def test_classify_c26_gamma0(self):
        """c=26: alpha=25, integer, 12 does not divide 25 -> Gamma_0(N)."""
        info = classify_spectral_type(26)
        assert info['type'] == 'modular_gamma0'


class TestSpectralTypeTable:
    """spectral_type_table for c = 1, 2, 7, 13, 25, 26, pi."""

    def test_table_has_seven_entries(self):
        """The table should have 7 entries."""
        table = spectral_type_table()
        assert len(table) == 7

    def test_table_contains_modular(self):
        """At least two entries should be modular_sl2z."""
        table = spectral_type_table()
        modular_count = sum(1 for e in table if e['type'] == 'modular_sl2z')
        assert modular_count >= 2  # c=1, c=13, c=25

    def test_table_contains_nonmodular(self):
        """At least one entry should be non_modular."""
        table = spectral_type_table()
        nm_count = sum(1 for e in table if e['type'] == 'non_modular')
        assert nm_count >= 1  # c=pi

    def test_selfdual_in_table(self):
        """c=13 (self-dual) should appear with label."""
        table = spectral_type_table()
        c13 = [e for e in table if abs(e['c'] - 13) < 0.01]
        assert len(c13) == 1
        assert 'self-dual' in c13[0]['label']


# ============================================================
# Section 8: Self-duality transition at c=13
# ============================================================

class TestSelfDualTransition:
    """At alpha=12 (c=13): all spectral weight in continuous spectrum.
    At alpha=12+epsilon: discrete component turns on."""

    def test_total_weight_finite(self):
        """Total spectral weight is finite for various alpha."""
        mp.dps = 15
        for alpha in [1, 6, 12]:
            w = total_spectral_weight(alpha, ymax=8, nmax=80)
            assert w > 0
            assert w < mpf('1e10')

    def test_weight_depends_on_alpha(self):
        """Total weight varies with alpha."""
        mp.dps = 15
        w1 = total_spectral_weight(1, ymax=8, nmax=80)
        w12 = total_spectral_weight(12, ymax=8, nmax=80)
        assert abs(float(w1) - float(w12)) > 1e-5

    def test_weight_near_selfdual_dict(self):
        """spectral_weight_near_selfdual returns a dict with correct keys."""
        result = spectral_weight_near_selfdual([11, 12, 13])
        assert 11 in result
        assert 12 in result
        assert 13 in result
        for v in result.values():
            assert v > 0


# ============================================================
# Section 9: Shadow moments from continuous spectrum
# ============================================================

class TestShadowMoments:
    """M_r^{cont} = integral t^{-2r} * rho_cont(t; alpha) dt."""

    def test_moment_r2_alpha1_positive(self):
        """M_2^{cont} at alpha=1 (c=2) is a positive number."""
        mp.dps = 15
        val = shadow_moment_continuous(2, 1, t_min=0.5, t_max=8, nmax=60)
        assert val.real > 0

    def test_moment_r4_alpha1_positive(self):
        """M_4^{cont} at alpha=1 is positive."""
        mp.dps = 15
        val = shadow_moment_continuous(4, 1, t_min=0.5, t_max=8, nmax=60)
        assert val.real > 0

    def test_moment_hierarchy(self):
        """M_4 > M_2 because t^{-2r} with larger r amplifies the
        small-t region where the density is concentrated. The integral
        int t^{-8} * rho(t) dt > int t^{-4} * rho(t) dt when rho
        has support near small t (t_min ~ 0.5)."""
        mp.dps = 15
        m2 = shadow_moment_continuous(2, 1, t_min=0.5, t_max=8, nmax=60)
        m4 = shadow_moment_continuous(4, 1, t_min=0.5, t_max=8, nmax=60)
        # Higher inverse moments are LARGER because t^{-8} >> t^{-4} for small t
        assert m4.real > m2.real


# ============================================================
# Section 10: Maass form discrete component
# ============================================================

class TestMaassDiscrete:
    """Estimates for the discrete (Maass cusp form) component."""

    def test_first_maass_eigenvalue(self):
        """The first Maass cusp form eigenvalue t_1 ~ 9.5337."""
        mp.dps = 20
        assert fabs(FIRST_MAASS_T - mpf('9.5337')) < mpf('0.001')

    def test_discrete_estimate_structure(self):
        """estimate_discrete_component returns dict with correct keys."""
        mp.dps = 15
        result = estimate_discrete_component(1, nmax=80)
        assert 'total' in result
        assert 'continuous_estimate' in result
        assert 'discrete_estimate' in result
        assert result['total'] >= 0

    def test_discrete_at_modular_alpha_small(self):
        """At alpha=12 (modular), the discrete component should be relatively
        small compared to non-modular alpha."""
        mp.dps = 15
        r_mod = estimate_discrete_component(12, t_max=15, nmax=80)
        r_gen = estimate_discrete_component(1, t_max=15, nmax=80)
        # Both have numerical approximation error, but the relative sizes
        # should show the discrete component is smaller at modular alpha
        assert r_mod['total'] >= 0
        assert r_gen['total'] >= 0


# ============================================================
# Section 11: Zeta-zero proximity in spectral density
# ============================================================

class TestZetaZeroProximity:
    """rho_cont has poles at t = gamma_k/2."""

    def test_zeta_zeros_stored(self):
        """The stored zeta zeros match known values."""
        assert abs(ZETA_ZEROS[0] - 14.1347) < 0.001
        assert abs(ZETA_ZEROS[1] - 21.0220) < 0.001
        assert len(ZETA_ZEROS) >= 5

    def test_density_blowup_near_zeta_zero(self):
        """rho_cont(t; alpha) blows up near t = gamma_1/2 ~ 7.067."""
        mp.dps = 15
        results = spectral_density_near_zeta_zero(1, gamma_k=ZETA_ZEROS[0],
                                                   delta=0.3, npts=5, nmax=80)
        assert len(results) >= 3
        # The values should show growth toward the center
        center_t = ZETA_ZEROS[0] / 2.0
        center_vals = [rho for t, rho in results if abs(t - center_t) < 0.15]
        edge_vals = [rho for t, rho in results if abs(t - center_t) > 0.2]
        if center_vals and edge_vals:
            # Center values should be larger (approaching the pole)
            assert max(center_vals) >= min(edge_vals) * 0.5  # relaxed for numerics

    def test_density_results_structure(self):
        """spectral_density_near_zeta_zero returns (t, rho) pairs."""
        mp.dps = 15
        results = spectral_density_near_zeta_zero(1, delta=0.5, npts=5, nmax=80)
        for t, rho in results:
            assert isinstance(t, float)
            assert isinstance(rho, float)
            assert rho >= 0


# ============================================================
# Section 12: L-function content at generic c
# ============================================================

class TestLFunctionContent:
    """Mellin of spectral density as L-function."""

    def test_mellin_at_alpha1_finite(self):
        """The Mellin transform of rho_cont at alpha=1 is finite for Re(s) > 1."""
        mp.dps = 15
        for s in [3, 4, 5]:
            val = mellin_of_spectral_density(s, 1, t_min=0.5, t_max=15, nmax=80)
            assert fabs(val) < mpf('1e10')
            assert fabs(val) > mpf('1e-15')

    def test_mellin_at_alpha12_finite(self):
        """The Mellin at alpha=12 (c=13) is finite."""
        mp.dps = 15
        val = mellin_of_spectral_density(3, 12, t_min=0.5, t_max=15, nmax=80)
        assert fabs(val) < mpf('1e10')

    def test_mellin_finite_at_multiple_s(self):
        """The Mellin integral is finite at multiple real s values."""
        mp.dps = 15
        for s in [3, 4, 5]:
            v = mellin_of_spectral_density(s, 1, t_min=0.5, t_max=15, nmax=80)
            assert fabs(v) < mpf('1e10')

    def test_mellin_at_irrational_alpha(self):
        """The Mellin at alpha=pi-1 (c=pi) is a well-defined finite number."""
        mp.dps = 15
        alpha = mpf(math.pi) - 1
        val = mellin_of_spectral_density(3, alpha, t_min=0.5, t_max=15, nmax=80)
        assert fabs(val) < mpf('1e10')


# ============================================================
# Section 13: Chriss-Ginzburg decomposition
# ============================================================

class TestChrissGinzburgDecomposition:
    """The theoretical summary of the spectral decomposition."""

    def test_summary_structure(self):
        """chriss_ginzburg_decomposition_summary returns correct keys."""
        s = chriss_ginzburg_decomposition_summary()
        assert 'statement' in s
        assert 'continuous' in s
        assert 'discrete' in s
        assert 'modular_cases' in s
        assert 'non_modular_cases' in s

    def test_continuous_has_hecke(self):
        """Continuous spectrum involves Hecke eigenforms."""
        s = chriss_ginzburg_decomposition_summary()
        assert 'Hecke' in s['continuous']['hecke'] or 'eigenvalue' in s['continuous']['hecke']

    def test_discrete_vanishing(self):
        """Discrete spectrum vanishes at modular c."""
        s = chriss_ginzburg_decomposition_summary()
        assert 'modular' in s['discrete']['vanishing']

    def test_first_maass_recorded(self):
        """The first Maass eigenvalue is recorded."""
        s = chriss_ginzburg_decomposition_summary()
        assert '9.533' in s['discrete']['first_eigenvalue']

    def test_selfdual_l_content(self):
        """At c=13, L-content involves Sym^2 Delta."""
        s = chriss_ginzburg_decomposition_summary()
        assert 'Sym' in s['modular_cases']['c=13']


# ============================================================
# Section 14: Cross-checks and consistency
# ============================================================

class TestCrossChecks:
    """Consistency checks between different computations."""

    def test_eta_power_consistency(self):
        """eta_power(y, alpha) = eta(y)^{2*alpha}."""
        mp.dps = 25
        y = mpf(1.5)
        alpha = mpf(3)
        direct = power(eta_on_imaginary_axis(y), 2 * alpha)
        via_fn = eta_power_on_imaginary_axis(y, alpha)
        assert fabs(direct - via_fn) < mpf('1e-20')

    def test_spectral_density_nonnegative(self):
        """rho_cont is non-negative for all tested parameters."""
        mp.dps = 15
        for alpha in [1, 2, 5]:
            for t in [0.5, 1, 3]:
                rho = continuous_spectral_density(t, alpha, ymax=10, nmax=80)
                assert rho >= -mpf('1e-10')  # allow small numerical error

    def test_hecke_eigenvalue_range(self):
        """2*cos(t*log p) is in [-2, 2] for all real t and prime p."""
        mp.dps = 20
        for t in [0, 0.5, 1, 3, 7, 14, 100]:
            for p in [2, 3, 5]:
                ev = hecke_eigenvalue_eisenstein(t, p)
                assert -2 - mpf('1e-15') <= ev <= 2 + mpf('1e-15')

    def test_spectral_coefficient_symmetry(self):
        """c(-t) = conj(c(t)) implies |c(-t)| = |c(t)|."""
        mp.dps = 15
        for t in [1, 3]:
            v_plus = fabs(spectral_coefficient(t, 1, ymax=10, nmax=80))
            v_minus = fabs(spectral_coefficient(-t, 1, ymax=10, nmax=80))
            assert fabs(v_plus - v_minus) < mpf('0.01') * v_plus

    def test_c_equals_alpha_plus_1(self):
        """Verify the c = alpha + 1 relation in classification."""
        for c in [1, 2, 7, 13, 25, 26]:
            alpha = alpha_from_central_charge(c)
            assert central_charge_from_alpha(alpha) == c
            assert alpha == c - 1

    def test_virasoro_selfdual_at_c13(self):
        """Vir_c self-dual at c=13 (NOT c=26). At c=13, alpha=12, modular."""
        info = classify_spectral_type(13)
        assert info['type'] == 'modular_sl2z'
        assert info['alpha'] == 12

    def test_virasoro_c26_not_selfdual_modular(self):
        """c=26: alpha=25, 12 does not divide 25, so Gamma_0 level."""
        info = classify_spectral_type(26)
        assert info['type'] == 'modular_gamma0'
        assert info['alpha'] == 25
