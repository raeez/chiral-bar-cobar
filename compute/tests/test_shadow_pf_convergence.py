r"""Tests for shadow partition function convergence analysis.

Verifies all seven analytic results:
1. Genus convergence radius = 2*pi
2. Arity convergence (shadow radius, critical c*)
3. Double convergence domain
4. Residues and analytic continuation
5. Borel transform entirety
6. Boundary behavior (critical exponent alpha = 1)
7. Modular properties

Plus: Bernoulli decay, string comparison, class comparison,
      high-precision verification, Virasoro family scan.

60+ tests covering the full convergence landscape.

Manuscript references:
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    rem:convergence-vs-string (genus_expansions.tex)
"""

import math
import cmath
import pytest

from sympy import Rational

from compute.lib.shadow_pf_convergence import (
    # Section 1: A-hat and genus convergence
    ahat_function,
    ahat_at_imaginary,
    genus_series_closed_form,
    genus_series_partial_sum,
    genus_convergence_radius,
    genus_convergence_verification,
    # Section 2: Bernoulli decay
    bernoulli_decay_coefficients,
    string_divergence_rate,
    # Section 3: Arity convergence
    virasoro_shadow_radius_squared,
    virasoro_shadow_radius,
    arity_convergence_radius,
    critical_central_charge,
    arity_convergence_landscape,
    # Section 4: Double convergence
    DoubleConvergenceDomain,
    double_convergence_domain,
    double_convergence_table,
    # Section 5: Residues
    ahat_residue_at_2pi_n,
    scalar_genus_series_residue,
    ahat_residue_verification,
    # Section 6: Borel transform
    borel_transform_genus_series,
    borel_transform_is_entire,
    string_borel_comparison,
    # Section 7: Boundary behavior
    boundary_behavior,
    boundary_exponent_extraction,
    # Section 8: Modular
    genus_1_shadow_modular,
    # Section 9: High-precision
    hp_ahat,
    hp_genus_series,
    hp_convergence_radius_verification,
    hp_residue_at_2pi,
    # Section 10: Virasoro
    virasoro_full_convergence,
    virasoro_convergence_scan,
    # Section 11: Class comparison
    class_comparison,
    # Section 12: Polylogarithm
    polylogarithm,
    arity_borel_transform,
    arity_borel_singularity_structure,
    # Section 13: Master
    master_convergence_summary,
    # Constants
    TWO_PI,
    TWO_PI_SQ,
)

from compute.lib.utils import lambda_fp

PI = math.pi


# =========================================================================
# Class 1: A-hat function properties
# =========================================================================

class TestAhatFunction:
    """Test the A-hat genus function A-hat(x) = (x/2)/sinh(x/2)."""

    def test_ahat_at_zero(self):
        """A-hat(0) = 1."""
        assert abs(ahat_function(0) - 1.0) < 1e-14

    def test_ahat_at_imaginary_zero(self):
        """A-hat(i*0) = 1."""
        assert abs(ahat_at_imaginary(0.0) - 1.0) < 1e-14

    def test_ahat_real_positive(self):
        """A-hat(x) > 0 for small real x."""
        for x in [0.1, 0.5, 1.0, 2.0]:
            val = ahat_function(complex(x, 0))
            assert val.real > 0

    def test_ahat_imaginary_positive(self):
        """A-hat(i*hbar) > 0 for 0 < hbar < 2*pi."""
        for hbar in [0.1, 1.0, 3.0, 5.0, 6.0]:
            assert ahat_at_imaginary(hbar) > 0

    def test_ahat_symmetry(self):
        """A-hat(x) = A-hat(-x) (even function)."""
        for x in [0.5, 1.0, 2.0]:
            assert abs(ahat_function(x) - ahat_function(-x)) < 1e-14

    def test_ahat_small_x_expansion(self):
        """A-hat(i*hbar) = 1 + hbar^2/24 + 7*hbar^4/5760 + ... for small hbar."""
        hbar = 0.01
        val = ahat_at_imaginary(hbar)
        # 1 + hbar^2/24 to leading order
        expected = 1.0 + hbar**2 / 24.0
        assert abs(val - expected) < 1e-8


# =========================================================================
# Class 2: Genus convergence radius = 2*pi
# =========================================================================

class TestGenusConvergenceRadius:
    """Test that the genus series has convergence radius 2*pi."""

    def test_convergence_radius_value(self):
        """R = 2*pi ~ 6.2832."""
        R = genus_convergence_radius()
        assert abs(R - 2 * PI) < 1e-10

    def test_partial_sum_converges_at_hbar_1(self):
        """Partial sum converges to closed form at hbar = 1."""
        kappa = 1.0
        closed = genus_series_closed_form(kappa, 1.0)
        partial = genus_series_partial_sum(kappa, 50, 1.0)
        assert abs(partial - closed) / abs(closed) < 1e-10

    def test_partial_sum_converges_at_hbar_5(self):
        """Partial sum converges at hbar = 5 (inside disc)."""
        kappa = 1.0
        closed = genus_series_closed_form(kappa, 5.0)
        partial = genus_series_partial_sum(kappa, 50, 5.0)
        assert abs(partial - closed) / abs(closed) < 1e-4

    def test_partial_sum_converges_at_hbar_6(self):
        """Partial sum converges at hbar = 6 (just inside disc).

        hbar = 6 gives ratio 36/(2*pi)^2 ~ 0.912, so convergence is slow.
        With 50 terms the error is ~1%; with 100 terms it improves.
        """
        kappa = 1.0
        closed = genus_series_closed_form(kappa, 6.0)
        partial = genus_series_partial_sum(kappa, 100, 6.0)
        # Convergence is slow near the boundary; 2% tolerance
        assert abs(partial - closed) / abs(closed) < 0.02

    def test_ratio_test_at_hbar_1(self):
        """Asymptotic ratio at hbar = 1: hbar^2/(2*pi)^2 ~ 0.025."""
        ratio = 1.0 / TWO_PI_SQ
        assert abs(ratio - 0.02533) < 0.001

    def test_ratio_test_at_hbar_2pi(self):
        """At hbar = 2*pi, the ratio is exactly 1 (boundary)."""
        ratio = (2 * PI)**2 / TWO_PI_SQ
        assert abs(ratio - 1.0) < 1e-14

    def test_verification_function(self):
        """Full verification function returns consistent results."""
        result = genus_convergence_verification(1.0, max_genus=30)
        assert result['convergence_radius'] == TWO_PI
        assert result['hbar_1']['relative_error'] < 1e-10


# =========================================================================
# Class 3: Bernoulli decay
# =========================================================================

class TestBernoulliDecay:
    """Test the Bernoulli decay |lambda_g^FP| ~ 2/(2*pi)^{2g}."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_decay_ratio_approaches_limit(self):
        """Ratio lambda_{g+1}/lambda_g -> 1/(2*pi)^2."""
        target = 1.0 / TWO_PI_SQ
        for g in range(10, 20):
            r = float(lambda_fp(g + 1)) / float(lambda_fp(g))
            assert abs(r - target) / target < 0.05

    def test_bernoulli_asymptotic(self):
        """lambda_g / (2/(2*pi)^{2g}) -> 1 as g -> infty."""
        result = bernoulli_decay_coefficients(25)
        # At g=20, the ratio should be close to 1
        ratio_g20 = result['data'][19]['ratio']  # index 19 = g=20
        assert abs(ratio_g20 - 1.0) < 0.01

    def test_all_positive(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 30):
            assert float(lambda_fp(g)) > 0


# =========================================================================
# Class 4: String divergence contrast
# =========================================================================

class TestStringDivergence:
    """Shadow converges, string diverges."""

    def test_shadow_string_ratio_decreases(self):
        """Ratio shadow/string -> 0 superexponentially."""
        result = string_divergence_rate(10)
        ratios = [d['ratio'] for d in result['data']]
        for i in range(1, len(ratios)):
            assert ratios[i] < ratios[i - 1]

    def test_shadow_string_ratio_tiny_at_g10(self):
        """At genus 10, shadow/string ratio is astronomically small.

        lambda_10^FP / (20!) ~ 2/(2*pi)^20 / (20!) ~ 1e-34.
        """
        result = string_divergence_rate(10)
        assert result['data'][9]['ratio'] < 1e-30

    def test_log_ratio_decreasing(self):
        """log10(ratio) is monotonically decreasing."""
        result = string_divergence_rate(10)
        logs = [d['log_ratio'] for d in result['data']]
        for i in range(1, len(logs)):
            assert logs[i] < logs[i - 1]


# =========================================================================
# Class 5: Arity convergence and critical c*
# =========================================================================

class TestArityConvergence:
    """Test arity convergence radius = 1/rho."""

    def test_critical_c_star(self):
        """c* ~ 6.125 (unique positive root of 5c^3+22c^2-180c-872)."""
        c_star = critical_central_charge()
        assert abs(c_star - 6.1254) < 0.001

    def test_rho_at_c_star_is_one(self):
        """rho(Vir_{c*}) = 1."""
        c_star = critical_central_charge()
        rho = virasoro_shadow_radius(c_star)
        assert abs(rho - 1.0) < 0.001

    def test_rho_decreases_with_c(self):
        """rho(Vir_c) decreases as c increases (for large c)."""
        rho_10 = virasoro_shadow_radius(10.0)
        rho_20 = virasoro_shadow_radius(20.0)
        rho_50 = virasoro_shadow_radius(50.0)
        assert rho_10 > rho_20 > rho_50

    def test_rho_c13_self_dual(self):
        """rho(Vir_13) ~ 0.467."""
        rho = virasoro_shadow_radius(13.0)
        assert abs(rho - 0.467) < 0.01

    def test_rho_c26_string(self):
        """rho(Vir_26) ~ 0.234 (strongly convergent)."""
        rho = virasoro_shadow_radius(26.0)
        assert abs(rho - 0.234) < 0.01

    def test_rho_c1_divergent(self):
        """rho(Vir_1) > 1 (divergent arity series)."""
        rho = virasoro_shadow_radius(1.0)
        assert rho > 1.0

    def test_rho_c_half_divergent(self):
        """rho(Vir_{1/2}) > 1 (Ising, divergent)."""
        rho = virasoro_shadow_radius(0.5)
        assert rho > 1.0

    def test_arity_radius_heisenberg_infinite(self):
        """Heisenberg: rho = 0, R_arity = infinity."""
        assert arity_convergence_radius(0.0) == float('inf')

    def test_arity_radius_inverse_of_rho(self):
        """R_arity = 1/rho for rho > 0."""
        rho = virasoro_shadow_radius(13.0)
        R = arity_convergence_radius(rho)
        assert abs(R - 1.0 / rho) < 1e-10

    def test_landscape_consistency(self):
        """Landscape function returns consistent data."""
        landscape = arity_convergence_landscape()
        assert landscape['Heisenberg']['convergent'] is True
        assert landscape['Affine_sl2']['convergent'] is True
        assert landscape['Vir_c=13']['convergent'] is True
        assert landscape['Vir_c=1']['convergent'] is False


# =========================================================================
# Class 6: Double convergence domain
# =========================================================================

class TestDoubleConvergence:
    """Test the double convergence domain D = {|hbar| < 2pi} x {|t| < 1/rho}."""

    def test_domain_construction(self):
        """Construct domain for Vir c=13."""
        rho = virasoro_shadow_radius(13.0)
        domain = double_convergence_domain(6.5, rho, 'Vir_13')
        assert abs(domain.R_genus - TWO_PI) < 1e-10
        assert abs(domain.R_arity - 1.0 / rho) < 1e-10
        assert domain.physical_point_in_domain is True

    def test_domain_heisenberg_infinite(self):
        """Heisenberg: arity radius is infinite."""
        domain = double_convergence_domain(0.5, 0.0, 'Heis')
        assert domain.R_arity == float('inf')
        assert domain.physical_point_in_domain is True

    def test_domain_divergent_case(self):
        """Vir c=1: physical point outside domain."""
        rho = virasoro_shadow_radius(1.0)
        domain = double_convergence_domain(0.5, rho, 'Vir_1')
        assert domain.physical_point_in_domain is False

    def test_area_estimate(self):
        """Area R_genus * R_arity for convergent case."""
        rho = virasoro_shadow_radius(13.0)
        domain = double_convergence_domain(6.5, rho)
        area = domain.area_estimate
        assert area > 0
        assert math.isfinite(area)

    def test_table_has_all_families(self):
        """Convergence table includes all standard families."""
        table = double_convergence_table()
        assert len(table) >= 9
        names = [row['name'] for row in table]
        assert any('Heisenberg' in n for n in names)
        assert any('Affine' in n for n in names)

    def test_table_genus_radius_universal(self):
        """All families have the same genus radius = 2*pi."""
        table = double_convergence_table()
        for row in table:
            assert abs(row['R_genus'] - TWO_PI) < 1e-10


# =========================================================================
# Class 7: Residues and analytic continuation
# =========================================================================

class TestResidues:
    """Test residues of A-hat(i*hbar) at hbar = 2*pi*n."""

    def test_residue_at_n1(self):
        """Res_{hbar=2*pi} = (-1)^1 * 2*pi = -2*pi."""
        res = ahat_residue_at_2pi_n(1)
        assert abs(res - (-2 * PI)) < 1e-10

    def test_residue_at_n_minus1(self):
        """Res_{hbar=-2*pi} = (-1)^{-1} * 2*pi*(-1) = 2*pi."""
        res = ahat_residue_at_2pi_n(-1)
        assert abs(res - 2 * PI) < 1e-10

    def test_residue_at_n2(self):
        """Res_{hbar=4*pi} = (-1)^2 * 2*pi*2 = 4*pi."""
        res = ahat_residue_at_2pi_n(2)
        assert abs(res - 4 * PI) < 1e-10

    def test_residue_at_n0(self):
        """No pole at hbar = 0."""
        assert ahat_residue_at_2pi_n(0) == 0.0

    def test_scalar_residue_scales_with_kappa(self):
        """Residue of F_g series = kappa * Res(A-hat)."""
        kappa = 3.0
        res = scalar_genus_series_residue(kappa, 1)
        assert abs(res - kappa * (-2 * PI)) < 1e-10

    def test_numerical_residue_verification_n1(self):
        """Numerical verification of residue at n=1."""
        result = ahat_residue_verification(1)
        assert result['relative_error'] < 1e-4

    def test_numerical_residue_verification_n2(self):
        """Numerical verification of residue at n=2."""
        result = ahat_residue_verification(2)
        assert result['relative_error'] < 1e-4

    def test_residue_alternating_signs(self):
        """Residues alternate in sign: n=1 negative, n=2 positive."""
        assert ahat_residue_at_2pi_n(1) < 0
        assert ahat_residue_at_2pi_n(2) > 0
        assert ahat_residue_at_2pi_n(3) < 0


# =========================================================================
# Class 8: Borel transform
# =========================================================================

class TestBorelTransform:
    """Test Borel transform properties."""

    def test_borel_genus_series_at_zero(self):
        """Borel transform vanishes at zeta = 0."""
        val = borel_transform_genus_series(1.0, 0.0)
        assert abs(val) < 1e-15

    def test_borel_genus_series_finite_at_large_zeta(self):
        """Borel transform is finite at large |zeta| (entire)."""
        for z in [10.0, 50.0, 100.0]:
            val = borel_transform_genus_series(1.0, z)
            assert math.isfinite(abs(val))

    def test_borel_genus_series_entire_verification(self):
        """Full entirety verification."""
        result = borel_transform_is_entire(1.0)
        assert result['is_entire'] is True

    def test_borel_at_imaginary(self):
        """Borel transform finite on imaginary axis."""
        for y in [1.0, 5.0, 10.0]:
            val = borel_transform_genus_series(1.0, complex(0, y))
            assert math.isfinite(abs(val))

    def test_string_borel_comparison(self):
        """Shadow Borel coefficients decay, string coefficients constant."""
        result = string_borel_comparison(1.0, 10)
        # Shadow coefficients decrease
        for i in range(1, len(result['shadow_borel_coefficients'])):
            assert result['shadow_borel_coefficients'][i] < result['shadow_borel_coefficients'][i-1]
        # String coefficients are constant = 1
        assert all(c == 1.0 for c in result['string_borel_coefficients'])

    def test_arity_borel_entire_for_rho_gt_1(self):
        """Arity Borel transform is entire even for rho > 1."""
        rho = 2.0  # divergent ordinary series
        for z in [1.0, 5.0, 10.0]:
            val = arity_borel_transform(rho, z)
            assert math.isfinite(abs(val))

    def test_arity_borel_structure(self):
        """Arity Borel singularity structure reports entire."""
        for rho in [0.5, 1.0, 2.0]:
            result = arity_borel_singularity_structure(rho)
            assert result['borel_entire'] is True


# =========================================================================
# Class 9: Boundary behavior
# =========================================================================

class TestBoundaryBehavior:
    """Test boundary behavior at |hbar| = 2*pi."""

    def test_critical_exponent_is_1(self):
        """Critical exponent alpha = 1 (simple pole)."""
        result = boundary_behavior(1.0)
        assert result['critical_exponent'] == 1

    def test_pole_type_is_simple(self):
        """The pole is simple, not higher-order."""
        result = boundary_behavior(1.0)
        assert result['pole_type'] == 'simple'

    def test_singular_part_dominates(self):
        """Near the boundary, singular part dominates."""
        result = boundary_behavior(1.0, n_points=10)
        # At small eps, ratio Z/singular -> 1
        last = result['data'][-1]
        assert abs(last['ratio_Z_to_singular'] - 1.0) < 0.01

    def test_exponent_extraction(self):
        """Numerical extraction of alpha ~ 1."""
        result = boundary_exponent_extraction(1.0)
        assert abs(result['alpha'] - 1.0) < 0.05

    def test_leading_coefficient(self):
        """Leading coefficient = -2*pi*kappa."""
        kappa = 2.0
        result = boundary_behavior(kappa)
        assert abs(result['leading_coefficient'] - (-TWO_PI * kappa)) < 1e-10


# =========================================================================
# Class 10: Modular properties
# =========================================================================

class TestModularProperties:
    """Test modular properties at genus 1."""

    def test_F1_heisenberg(self):
        """F_1(Heisenberg rank 1) = 1/48."""
        result = genus_1_shadow_modular(0.5)  # kappa = 1/2
        assert abs(result['F_1'] - 1.0/48.0) < 1e-14

    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/48."""
        for c in [1.0, 13.0, 26.0]:
            result = genus_1_shadow_modular(c / 2.0)
            assert abs(result['F_1'] - c / 48.0) < 1e-14

    def test_modular_anomaly_equals_kappa(self):
        """Modular anomaly coefficient = kappa."""
        kappa = 3.5
        result = genus_1_shadow_modular(kappa)
        assert abs(result['modular_anomaly'] - kappa) < 1e-14


# =========================================================================
# Class 11: High-precision verification
# =========================================================================

class TestHighPrecision:
    """Test high-precision (mpmath) computations."""

    def test_hp_ahat_at_zero(self):
        """High-precision A-hat(0) = 1."""
        import mpmath
        val = hp_ahat(mpmath.mpf(0))
        assert abs(float(val) - 1.0) < 1e-30

    def test_hp_convergence_radius(self):
        """High-precision verification of R = 2*pi.

        At 30-digit precision with 200 terms, convergence is only achievable
        well inside the disc (frac <= 0.9).  Near the boundary, the series
        ratio approaches 1 and convergence requires many more terms.
        """
        result = hp_convergence_radius_verification(1.0, precision=30)
        assert abs(result['convergence_radius'] - 2 * PI) < 1e-10
        # Verify at least the first two points (frac=0.5, 0.9) converge
        assert result['results'][0]['converged'] is True
        assert result['results'][1]['converged'] is True

    def test_hp_residue_at_2pi(self):
        """High-precision residue = -2*pi*kappa."""
        result = hp_residue_at_2pi(1.0, precision=30)
        assert abs(result['predicted_residue'] - (-2 * PI)) < 1e-10
        assert result['convergence'] is True

    def test_hp_genus_series_matches_closed(self):
        """High-precision partial sum matches closed form at hbar = 1."""
        import mpmath
        old_dps = mpmath.mp.dps
        mpmath.mp.dps = 30
        try:
            kappa = mpmath.mpf(1)
            hbar = mpmath.mpf(1)
            closed = kappa * (hp_ahat(hbar) - 1)
            partial = hp_genus_series(kappa, hbar, max_genus=100)
            error = float(abs(partial - closed))
            assert error < 1e-20
        finally:
            mpmath.mp.dps = old_dps


# =========================================================================
# Class 12: Virasoro family analysis
# =========================================================================

class TestVirasoroFamily:
    """Test Virasoro convergence analysis across central charges."""

    def test_virasoro_c13(self):
        """Vir c=13 (self-dual): convergent."""
        result = virasoro_full_convergence(13.0)
        assert result['arity_convergent'] is True
        assert result['kappa'] == 6.5

    def test_virasoro_c26(self):
        """Vir c=26 (string): convergent."""
        result = virasoro_full_convergence(26.0)
        assert result['arity_convergent'] is True

    def test_virasoro_c1(self):
        """Vir c=1: divergent."""
        result = virasoro_full_convergence(1.0)
        assert result['arity_convergent'] is False

    def test_virasoro_scan(self):
        """Scan returns results for all central charges."""
        scan = virasoro_convergence_scan([1.0, 13.0, 26.0])
        assert len(scan) == 3
        assert scan[0]['arity_convergent'] is False
        assert scan[1]['arity_convergent'] is True
        assert scan[2]['arity_convergent'] is True

    def test_virasoro_F1_F2(self):
        """F_1 and F_2 are correct for Vir c=13."""
        result = virasoro_full_convergence(13.0)
        assert abs(result['F_1'] - 13.0 / 48.0) < 1e-10
        # F_2 = kappa * lambda_2 = 6.5 * 7/5760
        expected_F2 = 6.5 * 7.0 / 5760.0
        assert abs(result['F_2'] - expected_F2) < 1e-10

    def test_residue_at_2pi_virasoro(self):
        """Residue = -2*pi*kappa = -2*pi*(c/2)."""
        result = virasoro_full_convergence(26.0)
        expected = -2 * PI * 13.0
        assert abs(result['residue_at_2pi'] - expected) < 1e-8


# =========================================================================
# Class 13: Class comparison (G/L/C/M)
# =========================================================================

class TestClassComparison:
    """Test comparison across the four depth classes."""

    def test_class_G_convergent(self):
        """Class G (Heisenberg): always convergent."""
        classes = class_comparison()
        assert classes['G']['double_convergent'] is True
        assert classes['G']['arity_R'] == float('inf')

    def test_class_L_convergent(self):
        """Class L (Affine): always convergent."""
        classes = class_comparison()
        assert classes['L']['double_convergent'] is True

    def test_class_C_undefined(self):
        """Class C (Beta-gamma): convergence undefined."""
        classes = class_comparison()
        assert classes['C']['double_convergent'] is None

    def test_class_M_convergent(self):
        """Class M convergent (c=13): double convergent."""
        classes = class_comparison()
        assert classes['M_convergent']['double_convergent'] is True
        assert classes['M_convergent']['rho'] < 1.0

    def test_class_M_divergent(self):
        """Class M divergent (c=1): not double convergent."""
        classes = class_comparison()
        assert classes['M_divergent']['double_convergent'] is False
        assert classes['M_divergent']['rho'] > 1.0

    def test_all_classes_same_genus_radius(self):
        """All classes have genus radius = 2*pi."""
        classes = class_comparison()
        for key in ['G', 'L', 'M_convergent', 'M_divergent']:
            assert abs(classes[key]['genus_R'] - TWO_PI) < 1e-10


# =========================================================================
# Class 14: Polylogarithm and arity Borel
# =========================================================================

class TestPolylogarithm:
    """Test polylogarithm Li_s(z)."""

    def test_li_1_minus1(self):
        """Li_1(-1) = -ln(2).

        The alternating harmonic series converges slowly; 500 terms
        gives ~3 digits of accuracy.
        """
        val = polylogarithm(1.0, -1.0, max_terms=5000)
        assert abs(val.real - (-math.log(2))) < 1e-3

    def test_li_2_1(self):
        """Li_2(1) = pi^2/6."""
        val = polylogarithm(2.0, 0.999)  # approach z=1
        assert abs(val.real - PI**2 / 6) < 0.01

    def test_li_5_2_at_half(self):
        """Li_{5/2}(0.5) is a small positive number."""
        val = polylogarithm(2.5, 0.5)
        assert val.real > 0
        assert val.real < 1.0  # Li_{5/2}(1/2) ~ 0.53


# =========================================================================
# Class 15: Master convergence summary
# =========================================================================

class TestMasterSummary:
    """Test the master convergence summary."""

    def test_master_c13(self):
        """Master summary for c=13: fully convergent."""
        result = master_convergence_summary(13.0)
        assert result['genus_convergent'] is True
        assert result['arity_convergent'] is True
        assert result['double_convergent'] is True
        assert result['genus_borel_entire'] is True
        assert result['boundary_exponent'] == 1

    def test_master_c1(self):
        """Master summary for c=1: genus converges, arity diverges."""
        result = master_convergence_summary(1.0)
        assert result['genus_convergent'] is True
        assert result['arity_convergent'] is False
        assert result['double_convergent'] is False

    def test_master_c26(self):
        """Master summary for c=26 (string)."""
        result = master_convergence_summary(26.0)
        assert result['kappa'] == 13.0
        assert result['double_convergent'] is True

    def test_master_modular_anomaly(self):
        """Modular anomaly = kappa = c/2."""
        result = master_convergence_summary(13.0)
        assert abs(result['modular_anomaly'] - 6.5) < 1e-14

    def test_master_F1(self):
        """F_1 = kappa/24 = c/48."""
        result = master_convergence_summary(26.0)
        assert abs(result['F_1'] - 26.0 / 48.0) < 1e-14


# =========================================================================
# Class 16: Virasoro c=1 (Ising-like) detailed
# =========================================================================

class TestVirasoroC1:
    """Detailed tests for Virasoro at c=1 (free boson compactified)."""

    def test_rho_c1(self):
        """rho(Vir_1) computed from formula."""
        rho_sq = virasoro_shadow_radius_squared(1.0)
        # (180 + 872) / ((5 + 22) * 1) = 1052 / 27 ~ 38.96
        assert abs(rho_sq - 1052.0 / 27.0) < 1e-10
        rho = math.sqrt(rho_sq)
        assert rho > 1.0  # divergent

    def test_R_arity_c1(self):
        """R_arity(c=1) = 1/rho < 1."""
        rho = virasoro_shadow_radius(1.0)
        R = arity_convergence_radius(rho)
        assert R < 1.0

    def test_below_c_star(self):
        """c=1 < c* ~ 6.12."""
        c_star = critical_central_charge()
        assert 1.0 < c_star


# =========================================================================
# Class 17: Koszul dual shadow radius
# =========================================================================

class TestKoszulDualRadius:
    """Test rho(Vir_c) vs rho(Vir_{26-c})."""

    def test_self_dual_c13(self):
        """At c=13: rho(13) = rho(26-13) = rho(13)."""
        rho_A = virasoro_shadow_radius(13.0)
        rho_A_dual = virasoro_shadow_radius(26.0 - 13.0)
        assert abs(rho_A - rho_A_dual) < 1e-10

    def test_duality_c1_c25(self):
        """rho(Vir_1) and rho(Vir_25) are both computable."""
        rho_1 = virasoro_shadow_radius(1.0)
        rho_25 = virasoro_shadow_radius(25.0)
        # Both should be positive
        assert rho_1 > 0
        assert rho_25 > 0
        # c=1 divergent, c=25 convergent
        assert rho_1 > 1.0
        assert rho_25 < 1.0

    def test_rho_squared_formula(self):
        """Verify rho^2 formula at c=26."""
        rho_sq = virasoro_shadow_radius_squared(26.0)
        # (180*26 + 872) / ((5*26 + 22) * 26^2)
        # = (4680 + 872) / (152 * 676)
        # = 5552 / 102752
        expected = 5552.0 / 102752.0
        assert abs(rho_sq - expected) < 1e-10
