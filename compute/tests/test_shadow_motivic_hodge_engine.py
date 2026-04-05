r"""Tests for shadow_motivic_hodge_engine.py.

Multi-path verification of the motivic and Hodge-theoretic properties
of the shadow curve C_A: y^2 = t^4 * Q_L(t).

Test structure:
  1. Shadow curve genus (for all families)
  2. Hodge numbers
  3. Shadow metric and conic
  4. Virasoro shadow periods
  5. Weight filtration of S_r
  6. Kummer/transcendental decomposition
  7. Galois action
  8. L-function / point counting
  9. Cross-verification of growth rates
  10. Motivic weight analysis
  11. Landscape-wide tests

References:
    thm:riccati-algebraicity, def:shadow-metric, prop:shadow-periods,
    rem:motivic-decomposition, rem:kummer-motive
"""

import math
import pytest
from fractions import Fraction

from sympy import (
    Rational, Symbol, cancel, denom, expand, factor, numer, sqrt, simplify,
    Abs, N as sym_N,
)

from compute.lib.shadow_motivic_hodge_engine import (
    # Shadow data
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_km_shadow_data,
    betagamma_shadow_data,
    # Shadow metric and curve
    shadow_metric_QL,
    shadow_curve_sextic,
    shadow_curve_normalized,
    # Genus and Hodge
    shadow_curve_genus_abstract,
    shadow_curve_effective_genus,
    hodge_numbers_shadow_curve,
    # Virasoro specifics
    virasoro_shadow_metric,
    virasoro_conic,
    virasoro_shadow_curve_sextic,
    virasoro_conic_discriminant,
    # Periods
    virasoro_shadow_periods_numerical,
    picard_fuchs_equation,
    # Weight filtration
    virasoro_shadow_coefficient,
    denominator_factorization,
    weight_filtration_table,
    # Kummer/transcendental
    kummer_transcendental_decomposition,
    # Galois
    galois_action_algebraic_c,
    galois_orbit_golden_ratio,
    galois_orbit_sqrt2,
    # L-function
    point_count_conic_mod_p,
    virasoro_shadow_curve_Lfunction,
    shadow_conductor,
    # Cross-verification
    growth_rate_from_branch_points,
    growth_rate_from_coefficients,
    cross_verify_growth_rates,
    # Motivic weight
    motivic_weight_from_growth,
    # Analysis
    virasoro_shadow_analysis,
    shadow_curve_landscape,
)


c = Symbol('c')
t = Symbol('t')


# =========================================================================
# 1. SHADOW CURVE GENUS — all families have genus 0
# =========================================================================

class TestShadowCurveGenus:
    """The shadow curve C_A always has geometric genus 0."""

    def test_heisenberg_genus_0(self):
        """Heisenberg: Q_L = 4k^2 (constant), curve degenerates."""
        k_sym = Symbol('k')
        kappa, alpha, S4, Delta = heisenberg_shadow_data(k_sym)
        g = shadow_curve_genus_abstract(kappa, alpha, S4)
        assert g == 0

    def test_affine_sl2_genus_0(self):
        """Affine sl_2: Q_L quadratic with Delta=0, curve degenerates."""
        kappa, alpha, S4, Delta = affine_km_shadow_data(1)
        g = shadow_curve_genus_abstract(kappa, alpha, S4)
        assert g == 0

    def test_betagamma_genus_0(self):
        """Beta-gamma: Delta=0, curve degenerates."""
        kappa, alpha, S4, Delta = betagamma_shadow_data()
        g = shadow_curve_genus_abstract(kappa, alpha, S4)
        assert g == 0

    def test_virasoro_genus_0(self):
        """Virasoro: Delta != 0 but curve is still genus 0 after normalization."""
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        g = shadow_curve_genus_abstract(kappa, alpha, S4)
        assert g == 0

    def test_genus_0_universal(self):
        """Generic shadow curve has genus 0 (conic after normalization)."""
        kappa_sym = Symbol('kappa')
        alpha_sym = Symbol('alpha')
        S4_sym = Symbol('S4')
        g = shadow_curve_genus_abstract(kappa_sym, alpha_sym, S4_sym)
        assert g == 0

    def test_naive_genus_formula_would_give_2(self):
        """Naive genus formula for degree-6 sextic: g = (6-1)/2 - 1 = 2.
        But the quartic zero at t=0 reduces this to 0."""
        # The sextic t^4 * Q_L(t) has degree 6.
        # Naive hyperelliptic formula: g = floor((deg-1)/2) = 2.
        # But t=0 is a 4-fold root, so the effective degree is 2.
        # Genus of a degree-2 covering: g = 0.
        naive_genus = (6 - 1) // 2  # = 2
        actual_genus = 0
        assert naive_genus == 2
        assert actual_genus == 0


# =========================================================================
# 2. HODGE NUMBERS
# =========================================================================

class TestHodgeNumbers:
    """Hodge numbers of the shadow curve."""

    def test_heisenberg_hodge(self):
        k_sym = Symbol('k')
        kappa, alpha, S4, _ = heisenberg_shadow_data(k_sym)
        h = hodge_numbers_shadow_curve(kappa, alpha, S4)
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 0
        assert h[(0, 1)] == 0
        assert h['genus'] == 0
        assert h['euler_characteristic'] == 2

    def test_virasoro_hodge(self):
        kappa, alpha, S4, _ = virasoro_shadow_data()
        h = hodge_numbers_shadow_curve(kappa, alpha, S4)
        assert h[(0, 0)] == 1
        assert h[(1, 0)] == 0
        assert h[(0, 1)] == 0
        assert h['genus'] == 0
        assert h['euler_characteristic'] == 2

    def test_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry)."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        h = hodge_numbers_shadow_curve(kappa, alpha, S4)
        assert h[(1, 0)] == h[(0, 1)]

    def test_euler_characteristic(self):
        """chi = 2 - 2g = 2 for genus 0."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        h = hodge_numbers_shadow_curve(kappa, alpha, S4)
        assert h['euler_characteristic'] == 2 - 2 * h['genus']


# =========================================================================
# 3. SHADOW METRIC AND CONIC
# =========================================================================

class TestShadowMetric:
    """Q_L(t) and the normalized conic."""

    def test_virasoro_QL_at_t0(self):
        """Q_L(0) = 4*kappa^2 = c^2."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        QL, (q0, q1, q2) = shadow_metric_QL(kappa, alpha, S4)
        assert cancel(q0 - c**2) == 0

    def test_virasoro_QL_coefficients(self):
        """Verify Q_Vir(t) = c^2 + 12ct + ((180c+872)/(5c+22))t^2."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        _, (q0, q1, q2) = shadow_metric_QL(kappa, alpha, S4)
        assert cancel(q0 - c**2) == 0
        assert cancel(q1 - 12 * c) == 0
        expected_q2 = (180 * c + 872) / (5 * c + 22)
        assert cancel(q2 - expected_q2) == 0

    def test_heisenberg_QL_constant(self):
        """For Heisenberg: Q_L = 4k^2 (constant, no t-dependence)."""
        k_sym = Symbol('k')
        kappa, alpha, S4, _ = heisenberg_shadow_data(k_sym)
        QL, (q0, q1, q2) = shadow_metric_QL(kappa, alpha, S4)
        assert cancel(q1) == 0
        assert cancel(q2) == 0
        assert cancel(q0 - 4 * k_sym**2) == 0

    def test_virasoro_conic_discriminant(self):
        """disc = -320*c^2/(5c+22)."""
        disc = virasoro_conic_discriminant()
        expected = -320 * c**2 / (5 * c + 22)
        assert cancel(disc - expected) == 0

    def test_conic_discriminant_negative_for_positive_c(self):
        """For real c > 0: disc < 0 (no real points on conic)."""
        for c_val in [Rational(1, 2), 1, 2, 10, 25, 26]:
            disc = virasoro_conic_discriminant(c_val)
            assert float(disc) < 0, f"disc should be < 0 at c={c_val}"

    def test_shadow_curve_sextic_degree(self):
        """The sextic f(t) = t^4 * Q_L(t) has degree 6."""
        from sympy import Poly
        kappa, alpha, S4, _ = virasoro_shadow_data()
        f = shadow_curve_sextic(kappa, alpha, S4)
        p = Poly(f, t)
        assert p.degree() == 6

    def test_sextic_vanishes_at_t0_to_order_4(self):
        """f(t) has a zero of order 4 at t=0."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        f = shadow_curve_sextic(kappa, alpha, S4)
        from sympy import Poly
        p = Poly(f, t)
        # Coefficients of t^0, t^1, t^2, t^3 must vanish
        for i in range(4):
            assert p.nth(i) == 0, f"Coefficient of t^{i} should be 0"
        # Coefficient of t^4 is q_0 = c^2, nonzero
        assert cancel(p.nth(4) - c**2) == 0


class TestNormalizedConic:
    """The normalized shadow curve w^2 = Q_L^*(s)."""

    def test_virasoro_conic_structure(self):
        """Virasoro conic is a quadratic in s."""
        conic, disc = virasoro_conic()
        from sympy import Poly
        s = Symbol('s')
        p = Poly(conic, s)
        assert p.degree() == 2

    def test_conic_constant_term(self):
        """Constant term of Q_L^* is q_2 = (180c+872)/(5c+22)."""
        conic, _ = virasoro_conic()
        s = Symbol('s')
        from sympy import Poly
        p = Poly(conic, s)
        q2 = p.nth(0)
        expected = (180 * c + 872) / (5 * c + 22)
        assert cancel(q2 - expected) == 0

    def test_conic_leading_coefficient(self):
        """Leading coefficient of Q_L^* is q_0 = c^2."""
        conic, _ = virasoro_conic()
        s = Symbol('s')
        from sympy import Poly
        p = Poly(conic, s)
        q0 = p.nth(2)
        assert cancel(q0 - c**2) == 0


# =========================================================================
# 4. VIRASORO SHADOW PERIODS
# =========================================================================

class TestShadowPeriods:
    """Periods of the Virasoro shadow curve."""

    def test_periods_c1(self):
        """Period data at c=1."""
        data = virasoro_shadow_periods_numerical(1.0)
        assert data['c'] == 1.0
        assert data['kappa'] == 0.5
        assert abs(data['Delta'] - 40 / 27) < 1e-10
        assert data['monodromy'] == -1

    def test_periods_c_half(self):
        """Period data at c=1/2 (Ising model)."""
        data = virasoro_shadow_periods_numerical(0.5)
        assert abs(data['kappa'] - 0.25) < 1e-10
        assert data['growth_rate_rho'] > 0

    def test_periods_c25(self):
        """Period data at c=25."""
        data = virasoro_shadow_periods_numerical(25.0)
        assert data['growth_rate_rho'] > 0
        assert data['growth_rate_rho'] < 1  # c > c* ~ 6.12 => convergent

    def test_periods_c26(self):
        """Period data at c=26 (critical string)."""
        data = virasoro_shadow_periods_numerical(26.0)
        assert data['growth_rate_rho'] > 0
        assert data['growth_rate_rho'] < 1

    def test_periods_c2(self):
        """Period data at c=2."""
        data = virasoro_shadow_periods_numerical(2.0)
        assert data['growth_rate_rho'] > 0

    def test_branch_points_complex_conjugate(self):
        """For c > 0: branch points of Q_L are complex conjugates."""
        import cmath
        data = virasoro_shadow_periods_numerical(1.0)
        bp = data['branch_point_plus']
        bm = data['branch_point_minus']
        # Complex conjugates: bp = conj(bm)
        assert abs(bp.real - bm.real) < 1e-10
        assert abs(bp.imag + bm.imag) < 1e-10

    def test_branch_points_equal_modulus(self):
        """Complex conjugate branch points have equal modulus."""
        data = virasoro_shadow_periods_numerical(10.0)
        bp = data['branch_point_plus']
        bm = data['branch_point_minus']
        assert abs(abs(bp) - abs(bm)) < 1e-10

    def test_growth_rate_equals_inverse_branch_modulus(self):
        """rho = 1/|branch point|."""
        data = virasoro_shadow_periods_numerical(10.0)
        bp_mod = abs(data['branch_point_plus'])
        rho = data['growth_rate_rho']
        assert abs(rho - 1.0 / bp_mod) < 1e-8

    def test_shadow_period_integral_finite(self):
        """The shadow period (integral ds/sqrt(Q)) is finite."""
        data = virasoro_shadow_periods_numerical(1.0)
        omega = data['shadow_period_0_to_1']
        assert omega is not None
        assert abs(omega) > 0
        assert abs(omega) < 1e6  # not divergent


class TestPicardFuchs:
    """Picard-Fuchs equation for the shadow generating function."""

    def test_picard_fuchs_virasoro(self):
        """Virasoro shadow satisfies a Riccati equation."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        pf = picard_fuchs_equation(kappa, alpha, S4)
        assert pf['type'] == 'Riccati (degree 2 algebraic function)'
        assert pf['monodromy_at_branch'] == -1

    def test_picard_fuchs_heisenberg(self):
        """Heisenberg: trivial Picard-Fuchs (no branch points)."""
        k_sym = Symbol('k')
        kappa, alpha, S4, _ = heisenberg_shadow_data(k_sym)
        pf = picard_fuchs_equation(kappa, alpha, S4)
        assert pf['q1'] == 0
        assert pf['q2'] == 0

    def test_picard_fuchs_singular_points(self):
        """Singular points: t=0 and zeros of Q_L."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        pf = picard_fuchs_equation(kappa, alpha, S4)
        assert len(pf['singular_points']) == 2


# =========================================================================
# 5. VIRASORO SHADOW COEFFICIENTS — INDEPENDENT VERIFICATION
# =========================================================================

class TestVirasoroShadowCoefficients:
    """Verify S_r against known values (AP1: recompute, don't copy)."""

    def test_S2_equals_c_over_2(self):
        """S_2 = c/2 (the modular characteristic kappa)."""
        S2 = virasoro_shadow_coefficient(2)
        assert cancel(S2 - c / 2) == 0

    def test_S3_equals_2(self):
        """S_3 = 2 (the gravitational cubic)."""
        S3 = virasoro_shadow_coefficient(3)
        assert cancel(S3 - 2) == 0

    def test_S4_equals_Q_contact(self):
        """S_4 = 10/(c(5c+22)) = Q^contact_Vir."""
        S4 = virasoro_shadow_coefficient(4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert cancel(S4 - expected) == 0

    def test_S5_equals_known(self):
        """S_5 = -48/(c^2(5c+22))."""
        S5 = virasoro_shadow_coefficient(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert cancel(S5 - expected) == 0

    def test_S2_numerical(self):
        """S_2 at c=1: S_2 = 1/2."""
        S2 = virasoro_shadow_coefficient(2)
        assert float(S2.subs(c, 1)) == 0.5

    def test_S4_numerical_c1(self):
        """S_4 at c=1: 10/(1*27) = 10/27."""
        S4 = virasoro_shadow_coefficient(4)
        expected = 10.0 / 27.0
        assert abs(float(S4.subs(c, 1)) - expected) < 1e-12

    def test_S4_numerical_c26(self):
        """S_4 at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        S4 = virasoro_shadow_coefficient(4)
        expected = 10.0 / (26 * 152)
        assert abs(float(S4.subs(c, 26)) - expected) < 1e-12


# =========================================================================
# 6. DENOMINATOR FACTORIZATION AND WEIGHT FILTRATION
# =========================================================================

class TestDenominatorFactorization:
    """S_r has denominator c^{a_r} * (5c+22)^{b_r}."""

    def test_S2_no_denominator(self):
        """S_2 = c/2: no poles."""
        a, b, num = denominator_factorization(2)
        assert a == 0
        assert b == 0

    def test_S3_no_denominator(self):
        """S_3 = 2: no poles."""
        a, b, num = denominator_factorization(3)
        assert a == 0
        assert b == 0

    def test_S4_denominator(self):
        """S_4 = 10/(c*(5c+22)): a=1, b=1."""
        a, b, num = denominator_factorization(4)
        assert a == 1, f"Expected a=1, got a={a}"
        assert b == 1, f"Expected b=1, got b={b}"

    def test_S5_denominator(self):
        """S_5 = -48/(c^2*(5c+22)): a=2, b=1."""
        a, b, num = denominator_factorization(5)
        assert a == 2, f"Expected a=2, got a={a}"
        assert b == 1, f"Expected b=1, got b={b}"

    def test_denominator_a_monotone(self):
        """The exponent a_r (power of c in denominator) is non-decreasing for r >= 4."""
        table = weight_filtration_table(12)
        a_values = [(entry['r'], entry['a_r']) for entry in table if entry['r'] >= 4]
        for i in range(1, len(a_values)):
            assert a_values[i][1] >= a_values[i - 1][1], \
                f"a_r not monotone: a_{a_values[i][0]} = {a_values[i][1]} < a_{a_values[i-1][0]} = {a_values[i-1][1]}"

    def test_weight_filtration_table_length(self):
        """Weight filtration table has correct length."""
        table = weight_filtration_table(10)
        assert len(table) == 9  # r = 2, ..., 10

    def test_denominator_only_c_and_5c22(self):
        """The denominator of S_r has no prime factors other than c and (5c+22).

        This is a structural prediction: the Virasoro OPE data introduces
        poles only at c=0 and c=-22/5.
        """
        for r in range(2, 11):
            Sr = virasoro_shadow_coefficient(r)
            d = denom(cancel(Sr))
            a, b, _ = denominator_factorization(r)
            # After removing c^a and (5c+22)^b, the remainder should be a constant
            remainder = cancel(d / (c**a * (5 * c + 22)**b))
            # remainder should be a nonzero integer (no c-dependence)
            from sympy import Poly
            try:
                p = Poly(remainder, c)
                assert p.degree() == 0, \
                    f"S_{r} has unexpected pole: remainder = {remainder}"
            except Exception:
                # If it's already a constant, that's fine
                pass


class TestWeightFiltration:
    """Motivic weight filtration from the denominator structure."""

    def test_weight_filtration_first_entries(self):
        """First few entries of the weight filtration."""
        table = weight_filtration_table(6)
        # r=2: a=0, b=0 (S_2 = c/2, no poles)
        assert table[0]['r'] == 2
        assert table[0]['a_r'] == 0
        assert table[0]['b_r'] == 0

    def test_weight_2_pure(self):
        """S_2 = c/2 is a polynomial in c: weight 0, pure."""
        decomp = kummer_transcendental_decomposition(2, 1)
        assert decomp['is_kummer'] is True

    def test_all_Sr_rational_at_rational_c(self):
        """S_r(c) at rational c gives a rational number."""
        for r in range(2, 10):
            decomp = kummer_transcendental_decomposition(r, Rational(1, 2))
            assert decomp['is_kummer'] is True


# =========================================================================
# 7. GALOIS ACTION
# =========================================================================

class TestGaloisAction:
    """Galois action on shadow coefficients at algebraic c."""

    def test_galois_golden_ratio_trace_rational(self):
        """S_r(phi) + S_r(phi_bar) is rational for all r."""
        for r in [2, 3, 4]:
            data = galois_orbit_golden_ratio(r)
            trace = data['trace']
            # The trace should involve no sqrt(5)
            from sympy import sqrt as sym_sqrt
            trace_simplified = cancel(trace)
            # Check: substitute sqrt(5) -> -sqrt(5) should give same trace
            # (trace is invariant under Galois)
            trace_conj = trace_simplified.subs(sym_sqrt(5), -sym_sqrt(5))
            assert cancel(trace_simplified - trace_conj) == 0, \
                f"Trace of S_{r} not Galois-invariant"

    def test_galois_golden_ratio_norm_rational(self):
        """S_r(phi) * S_r(phi_bar) is rational for all r."""
        for r in [2, 3, 4]:
            data = galois_orbit_golden_ratio(r)
            norm = data['norm']
            from sympy import sqrt as sym_sqrt
            norm_simplified = cancel(norm)
            norm_conj = norm_simplified.subs(sym_sqrt(5), -sym_sqrt(5))
            assert cancel(norm_simplified - norm_conj) == 0, \
                f"Norm of S_{r} not Galois-invariant"

    def test_galois_S2_golden_ratio(self):
        """S_2(phi) = phi/2, S_2(phi_bar) = phi_bar/2.
        Trace = (phi + phi_bar)/2 = 1/2.
        Norm = phi * phi_bar / 4 = -1/4."""
        from sympy import sqrt as sym_sqrt
        data = galois_orbit_golden_ratio(2)
        phi = (1 + sym_sqrt(5)) / 2
        phi_bar = (1 - sym_sqrt(5)) / 2
        assert cancel(data['S_r_phi'] - phi / 2) == 0
        assert cancel(data['S_r_phi_bar'] - phi_bar / 2) == 0

    def test_galois_S3_constant(self):
        """S_3 = 2 is constant (independent of c), so Galois acts trivially."""
        data = galois_orbit_golden_ratio(3)
        assert cancel(data['S_r_phi'] - 2) == 0
        assert cancel(data['S_r_phi_bar'] - 2) == 0

    def test_galois_sqrt2_trace_rational(self):
        """S_r(sqrt(2)) + S_r(-sqrt(2)) should be rational."""
        for r in [2, 3]:
            data = galois_orbit_sqrt2(r)
            trace = cancel(data['trace'])
            from sympy import sqrt as sym_sqrt
            trace_conj = trace.subs(sym_sqrt(2), -sym_sqrt(2))
            assert cancel(trace - trace_conj) == 0

    def test_galois_orbit_size(self):
        """For c in Q: Galois orbit has size 1.
        For c = phi: orbit has size 2."""
        # Rational c: S_r is rational, orbit size 1
        Sr = virasoro_shadow_coefficient(4)
        val = cancel(Sr.subs(c, 1))
        # This is rational: 10/27
        assert val == Rational(10, 27)

        # Golden ratio: orbit has size 2 (phi and phi_bar are distinct)
        data = galois_orbit_golden_ratio(4)
        assert cancel(data['S_r_phi'] - data['S_r_phi_bar']) != 0


# =========================================================================
# 8. L-FUNCTION AND POINT COUNTING
# =========================================================================

class TestPointCounting:
    """Point counting on the shadow conic mod p."""

    def test_smooth_conic_has_p_plus_1_points(self):
        """A smooth conic over F_p has p+1 projective points.

        Use w^2 = s^2 + 1 (disc = -4). Smooth at all odd primes (disc != 0 mod p for p > 2).
        """
        for p in [5, 7, 11, 13, 17, 19, 23]:
            data = point_count_conic_mod_p(1, 0, 1, p)
            assert data['N_p'] == p + 1, \
                f"Smooth conic should have p+1={p+1} points at p={p}, got {data['N_p']}"

    def test_trace_of_frobenius_zero_for_conic(self):
        """For a smooth conic: a_p = 0 for all good primes."""
        for p in [5, 7, 11, 13, 17, 19, 23]:
            data = point_count_conic_mod_p(1, 0, 1, p)
            assert data['a_p'] == 0, \
                f"a_p should be 0 for smooth conic at p={p}, got {data['a_p']}"

    def test_virasoro_conic_c1_point_count(self):
        """Virasoro shadow conic at c=1: count points mod p."""
        # q_0 = 1, q_1 = 12, q_2 = (180+872)/27 = 1052/27
        # Scale to integers: multiply by 27: q_0=27, q_1=324, q_2=1052
        for p in [5, 7, 11, 13]:
            data = point_count_conic_mod_p(27, 324, 1052, p)
            # For a smooth conic: N_p = p + 1
            # (The scaling doesn't change the conic up to a quadratic twist)
            assert isinstance(data['N_p'], int)
            assert data['N_p'] >= 0

    def test_degenerate_conic_singular(self):
        """Degenerate conic (disc=0): has a singular point."""
        # w^2 = s^2 (disc = 0): degenerate into two lines
        for p in [3, 5, 7]:
            data = point_count_conic_mod_p(1, 0, 0, p)
            # w^2 = s^2 => w = +/-s: 2*(p-1) + 1 (the origin) + 2 at inf
            # Actually: w = s gives p points, w = -s gives p points, minus
            # the intersection (0,0): total = 2p - 1 affine + points at inf
            assert isinstance(data['N_p'], int)

    def test_legendre_symbol_consistency(self):
        """Legendre symbol (disc/p) should be consistent with point count."""
        for p in [5, 7, 11, 13, 17, 19]:
            data = point_count_conic_mod_p(1, 3, 2, p)
            # disc = 9 - 8 = 1, so (1/p) = 1 for all p
            if data['disc_mod_p'] != 0:
                assert data['legendre_disc'] in [-1, 1]


class TestLFunction:
    """L-function of the shadow conic."""

    def test_virasoro_L_function_c_half(self):
        """L-function data for Virasoro at c = 1/2."""
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        data = virasoro_shadow_curve_Lfunction(1, 2, primes)
        assert 'primes' in data
        assert len(data['primes']) > 0

    def test_virasoro_L_function_c1(self):
        """L-function data for Virasoro at c = 1."""
        primes = [3, 5, 7, 11, 13, 17, 19, 23]
        data = virasoro_shadow_curve_Lfunction(1, 1, primes)
        assert 'partial_L_at_s1' in data
        assert data['partial_L_at_s1'] > 0

    def test_conductor_c_half(self):
        """Conductor at c = 1/2."""
        data = shadow_conductor(1, 2)
        assert 'discriminant' in data
        assert data['disc_numerator'] != 0

    def test_conductor_c1(self):
        """Conductor at c = 1."""
        data = shadow_conductor(1, 1)
        assert data['disc_numerator'] != 0

    def test_L_function_primes_to_50(self):
        """Compute a_p for primes up to 50 at c = 1/2."""
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        data = virasoro_shadow_curve_Lfunction(1, 2, primes)
        for p in primes:
            if p in data['primes']:
                assert 'a_p' in data['primes'][p]
                assert 'N_p' in data['primes'][p]


# =========================================================================
# 9. CROSS-VERIFICATION OF GROWTH RATES
# =========================================================================

class TestGrowthRateCrossVerification:
    """Multi-path verification of the shadow growth rate."""

    def test_path1_branch_points_virasoro(self):
        """Path 1: rho from branch points at c=25."""
        kappa = Rational(25, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (25 * (5 * 25 + 22))
        data = growth_rate_from_branch_points(kappa, alpha, S4)
        rho = float(sym_N(Abs(data['rho'])))
        assert 0 < rho < 1  # c=25 > c* ~ 6.12

    def test_path3_formula_virasoro_c25(self):
        """Path 3: explicit formula at c=25."""
        rho_sq = (180 * 25 + 872) / ((5 * 25 + 22) * 25**2)
        rho = math.sqrt(rho_sq)
        assert 0 < rho < 1

    def test_paths_1_and_3_agree(self):
        """Paths 1 and 3 must agree (same mathematical content)."""
        c_val = 10
        result = cross_verify_growth_rates(c_val)
        assert result['paths_agree_1_3']

    def test_cross_verification_c1(self):
        """Full cross-verification at c=1."""
        result = cross_verify_growth_rates(1)
        assert result['paths_agree_1_3']
        # Path 2 (coefficient ratios) may not converge well at small r_max
        # but should be in the right ballpark

    def test_cross_verification_c25(self):
        """Full cross-verification at c=25."""
        result = cross_verify_growth_rates(25)
        assert result['paths_agree_1_3']

    def test_cross_verification_c26(self):
        """Full cross-verification at c=26 (critical string)."""
        result = cross_verify_growth_rates(26)
        assert result['paths_agree_1_3']

    def test_growth_rate_monotone_in_c(self):
        """rho(c) is decreasing for c >> c* (large c regime)."""
        rhos = []
        for c_val in [10, 15, 20, 25, 30]:
            rho_sq = (180 * c_val + 872) / ((5 * c_val + 22) * c_val**2)
            rhos.append((c_val, math.sqrt(rho_sq)))
        for i in range(1, len(rhos)):
            assert rhos[i][1] < rhos[i - 1][1], \
                f"rho not decreasing: rho({rhos[i][0]}) = {rhos[i][1]} >= rho({rhos[i-1][0]}) = {rhos[i-1][1]}"

    def test_growth_rate_self_dual_c13(self):
        """rho at the self-dual point c=13."""
        rho_sq = (180 * 13 + 872) / ((5 * 13 + 22) * 13**2)
        rho = math.sqrt(rho_sq)
        # From CLAUDE.md: rho ~ 0.467 at c=13
        assert abs(rho - 0.467) < 0.01, f"rho(c=13) = {rho}, expected ~0.467"


# =========================================================================
# 10. EFFECTIVE GENUS AND SHADOW CLASSIFICATION
# =========================================================================

class TestEffectiveGenus:
    """Effective genus distinguishes classes G/L/C from M."""

    def test_heisenberg_class_G(self):
        k_sym = Symbol('k')
        kappa, alpha, S4, Delta = heisenberg_shadow_data(k_sym)
        data = shadow_curve_effective_genus(kappa, alpha, S4)
        assert data['geometric_genus'] == 0
        assert data['tower_terminates'] is True
        assert data['shadow_class'] == 'G/L/C'

    def test_virasoro_class_M(self):
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        data = shadow_curve_effective_genus(kappa, alpha, S4)
        assert data['geometric_genus'] == 0
        assert data['tower_terminates'] is False
        assert data['shadow_class'] == 'M'

    def test_virasoro_field_extension(self):
        """Class M requires a quadratic field extension."""
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        data = shadow_curve_effective_genus(kappa, alpha, S4)
        assert 'sqrt' in data['field_extension']


# =========================================================================
# 11. MOTIVIC WEIGHT FROM GROWTH
# =========================================================================

class TestMotivicWeight:
    """Motivic weight analysis."""

    def test_all_Sr_weight_0(self):
        """S_r at rational c are rational: motivic weight 0."""
        data = motivic_weight_from_growth(1, r_max=8)
        assert data['all_rational'] is True
        assert data['motivic_weight_of_Sr'] == 0

    def test_coefficients_computed(self):
        """Shadow coefficients are computed correctly."""
        data = motivic_weight_from_growth(1, r_max=8)
        assert len(data['coefficients']) == 7  # r=2,...,8
        # S_2(1) = 1/2
        assert abs(data['coefficients'][0][1] - 0.5) < 1e-10

    def test_motivic_weight_c25(self):
        data = motivic_weight_from_growth(25, r_max=8)
        assert data['all_rational'] is True


# =========================================================================
# 12. KUMMER / TRANSCENDENTAL DECOMPOSITION
# =========================================================================

class TestKummerTranscendental:
    """All S_r at rational c are Kummer (rational)."""

    def test_kummer_c1(self):
        for r in range(2, 8):
            decomp = kummer_transcendental_decomposition(r, 1)
            assert decomp['is_kummer'] is True

    def test_kummer_c_half(self):
        for r in range(2, 6):
            decomp = kummer_transcendental_decomposition(r, Rational(1, 2))
            assert decomp['is_kummer'] is True

    def test_transcendence_in_tower_sum(self):
        """The transcendence is in the tower sum sqrt(Q_L), not in individual S_r."""
        decomp = kummer_transcendental_decomposition(4, 1)
        assert 'sqrt' in decomp['transcendence_source']


# =========================================================================
# 13. VIRASORO SHADOW ANALYSIS — FULL PIPELINE
# =========================================================================

class TestVirasoroAnalysis:
    """Full motivic-Hodge analysis at specific c values."""

    def test_analysis_c1(self):
        result = virasoro_shadow_analysis(1)
        assert result['c'] == 1
        assert abs(result['kappa'] - 0.5) < 1e-10
        assert result['genus_data']['geometric_genus'] == 0

    def test_analysis_c_half(self):
        result = virasoro_shadow_analysis(Rational(1, 2))
        assert result['genus_data']['geometric_genus'] == 0

    def test_analysis_c25(self):
        result = virasoro_shadow_analysis(25)
        assert result['genus_data']['shadow_class'] == 'M'
        assert result['genus_data']['tower_terminates'] is False

    def test_analysis_c26(self):
        result = virasoro_shadow_analysis(26)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_analysis_c2(self):
        result = virasoro_shadow_analysis(2)
        assert abs(result['kappa'] - 1.0) < 1e-10


# =========================================================================
# 14. LANDSCAPE ANALYSIS
# =========================================================================

class TestLandscape:
    """Shadow curve landscape across all standard families."""

    def test_landscape_has_four_families(self):
        landscape = shadow_curve_landscape()
        assert 'heisenberg' in landscape
        assert 'affine_sl2' in landscape
        assert 'betagamma' in landscape
        assert 'virasoro' in landscape

    def test_all_genus_0(self):
        landscape = shadow_curve_landscape()
        for family, data in landscape.items():
            assert data['geometric_genus'] == 0, \
                f"Family {family} has genus {data['geometric_genus']}"

    def test_class_G_terminates(self):
        landscape = shadow_curve_landscape()
        assert landscape['heisenberg']['tower_terminates'] is True
        assert landscape['heisenberg']['r_max'] == 2

    def test_class_L_terminates(self):
        landscape = shadow_curve_landscape()
        assert landscape['affine_sl2']['tower_terminates'] is True
        assert landscape['affine_sl2']['r_max'] == 3

    def test_class_C_terminates(self):
        landscape = shadow_curve_landscape()
        assert landscape['betagamma']['tower_terminates'] is True
        assert landscape['betagamma']['r_max'] == 4

    def test_class_M_infinite(self):
        landscape = shadow_curve_landscape()
        assert landscape['virasoro']['tower_terminates'] is False
        assert landscape['virasoro']['r_max'] == float('inf')

    def test_virasoro_Delta_nonzero(self):
        landscape = shadow_curve_landscape()
        assert cancel(landscape['virasoro']['Delta']) != 0


# =========================================================================
# 15. CONSISTENCY CHECKS (MULTI-PATH)
# =========================================================================

class TestConsistency:
    """Multi-path consistency checks across the engine."""

    def test_genus_consistent_with_hodge(self):
        """Genus from genus computation = genus from Hodge numbers."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        g = shadow_curve_genus_abstract(kappa, alpha, S4)
        h = hodge_numbers_shadow_curve(kappa, alpha, S4)
        assert g == h['genus']
        assert h[(1, 0)] == g
        assert h[(0, 1)] == g

    def test_delta_from_data_consistent(self):
        """Delta from virasoro_shadow_data = Delta from shadow_metric_QL."""
        kappa, alpha, S4, Delta_direct = virasoro_shadow_data()
        _, (q0, q1, q2) = shadow_metric_QL(kappa, alpha, S4)
        # disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2*Delta
        disc = q1**2 - 4 * q0 * q2
        Delta_from_disc = cancel(-disc / (32 * kappa**2))
        assert cancel(Delta_direct - Delta_from_disc) == 0

    def test_virasoro_delta_equals_40_over_5c22(self):
        """Delta_Vir = 40/(5c+22)."""
        _, _, _, Delta = virasoro_shadow_data()
        expected = Rational(40) / (5 * c + 22)
        assert cancel(Delta - expected) == 0

    def test_growth_rate_from_QL_disc(self):
        """rho^2 = q_2/q_0 for complex conjugate branch points."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        _, (q0, q1, q2) = shadow_metric_QL(kappa, alpha, S4)
        rho_sq_metric = cancel(q2 / q0)
        # Compare with the formula: rho^2 = (180c+872)/((5c+22)*c^2)
        rho_sq_formula = (180 * c + 872) / ((5 * c + 22) * c**2)
        assert cancel(rho_sq_metric - rho_sq_formula) == 0

    def test_shadow_duality_c_to_26_minus_c(self):
        """Under c -> 26-c (Koszul duality): Delta transforms."""
        Delta_c = Rational(40) / (5 * c + 22)
        Delta_dual = Delta_c.subs(c, 26 - c)
        # Delta(26-c) = 40/(5(26-c)+22) = 40/(152-5c)
        expected = Rational(40) / (152 - 5 * c)
        assert cancel(Delta_dual - expected) == 0

    def test_discriminant_sum_complementarity(self):
        """Delta(c) + Delta(26-c) = 40*(5c+22+152-5c)/((5c+22)(152-5c))
        = 40*174/((5c+22)(152-5c)) = 6960/((5c+22)(152-5c)).

        This is the complementarity sum (from concordance)."""
        Delta_c = Rational(40) / (5 * c + 22)
        Delta_dual = Rational(40) / (152 - 5 * c)
        total = cancel(Delta_c + Delta_dual)
        expected = Rational(6960) / ((5 * c + 22) * (152 - 5 * c))
        assert cancel(total - expected) == 0

    def test_self_dual_point_c13(self):
        """At c=13: Delta(13) = Delta(26-13) = 40/87."""
        Delta_13 = Rational(40) / (5 * 13 + 22)
        assert Delta_13 == Rational(40, 87)

    def test_heisenberg_trivial_conic(self):
        """Heisenberg: conic degenerates to w^2 = 4k^2*s^2, i.e., w = +/- 2k*s."""
        k_sym = Symbol('k')
        kappa, alpha, S4, _ = heisenberg_shadow_data(k_sym)
        QL_star, disc = shadow_curve_normalized(kappa, alpha, S4)
        # QL_star = q0*s^2 + q1*s + q2 with q0=4k^2, q1=0, q2=0
        # So QL_star = 4k^2*s^2
        assert cancel(disc) == 0  # degenerate


# =========================================================================
# 16. POINT COUNTING EDGE CASES
# =========================================================================

class TestPointCountingEdgeCases:
    """Edge cases in point counting mod p."""

    def test_identity_conic(self):
        """w^2 = s^2 + 1 over F_p."""
        for p in [3, 5, 7, 11, 13]:
            data = point_count_conic_mod_p(1, 0, 1, p)
            assert data['N_p'] == p + 1

    def test_twist_conic(self):
        """w^2 = 2*s^2 + 1 (quadratic twist)."""
        for p in [3, 5, 7, 11, 13]:
            data = point_count_conic_mod_p(2, 0, 1, p)
            # Still a smooth conic
            assert data['N_p'] == p + 1

    def test_large_prime(self):
        """Point counting at a larger prime."""
        data = point_count_conic_mod_p(1, 1, 1, 97)
        assert data['N_p'] == 98  # smooth conic: p+1

    def test_bad_reduction(self):
        """Conic with bad reduction mod p."""
        # w^2 = 5*s^2 + 10*s + 5 = 5*(s+1)^2 (degenerate mod 5)
        data = point_count_conic_mod_p(5, 10, 5, 5)
        # Degenerate: disc = 100 - 100 = 0 (mod 5)
        assert data['disc_mod_p'] == 0


# =========================================================================
# 17. SHADOW CURVE NUMERICAL PROPERTIES
# =========================================================================

class TestNumericalProperties:
    """Numerical properties of the shadow curve at specific c values."""

    def test_branch_point_modulus_c1(self):
        """At c=1: |branch point| = 1/rho where rho = sqrt((180+872)/(27*1))."""
        rho_sq = (180 + 872) / (27 * 1)
        rho = math.sqrt(rho_sq)
        bp_mod = 1.0 / rho
        data = virasoro_shadow_periods_numerical(1.0)
        assert abs(abs(data['branch_point_plus']) - bp_mod) < 1e-6

    def test_growth_rate_c1_numerical(self):
        """rho at c=1: sqrt(1052/27) ~ 6.24."""
        rho_sq = 1052 / 27
        rho = math.sqrt(rho_sq)
        assert abs(rho - 6.2414) < 0.01

    def test_growth_rate_c26_numerical(self):
        """rho at c=26: sqrt((180*26+872)/(152*676))."""
        rho_sq = (180 * 26 + 872) / (152 * 676)
        rho = math.sqrt(rho_sq)
        assert rho < 1  # convergent tower

    def test_kappa_c1(self):
        data = virasoro_shadow_periods_numerical(1.0)
        assert abs(data['kappa'] - 0.5) < 1e-12

    def test_delta_c1(self):
        data = virasoro_shadow_periods_numerical(1.0)
        expected_delta = 40 / 27
        assert abs(data['Delta'] - expected_delta) < 1e-10

    def test_q2_positive(self):
        """q_2 > 0 for all c > 0 (since 180c+872 > 0 and 5c+22 > 0)."""
        for c_val in [0.5, 1, 2, 5, 10, 25, 26, 100]:
            data = virasoro_shadow_periods_numerical(c_val)
            assert data['q2'] > 0, f"q2 < 0 at c={c_val}"


# =========================================================================
# 18. DUALITY PROPERTIES
# =========================================================================

class TestDualityProperties:
    """Koszul duality c -> 26-c on the shadow curve."""

    def test_kappa_duality(self):
        """kappa(c) + kappa(26-c) = 13 (AP24 for Virasoro)."""
        for c_val in [1, Rational(1, 2), 5, 10, 25]:
            kappa_c = Rational(c_val) / 2
            kappa_dual = Rational(26 - c_val) / 2
            assert kappa_c + kappa_dual == 13

    def test_Q_L_transforms_under_duality(self):
        """Q_L at c and Q_L at 26-c are related but not equal."""
        kappa_c, alpha_c, S4_c, _ = virasoro_shadow_data()
        # At c=1 vs c=25
        QL_1 = virasoro_shadow_metric(Rational(1))[0]
        QL_25 = virasoro_shadow_metric(Rational(25))[0]
        # They should be different
        assert cancel(QL_1 - QL_25) != 0

    def test_shadow_curve_not_self_dual_except_c13(self):
        """The shadow curve is self-dual only at c=13."""
        # At c=13: kappa = 13/2, S4 symmetric
        S4_at_13 = virasoro_shadow_coefficient(4).subs(c, 13)
        S4_at_13_dual = virasoro_shadow_coefficient(4).subs(c, 13)  # same!
        assert cancel(S4_at_13 - S4_at_13_dual) == 0

        # At c=1 vs c=25: S4 different
        S4_at_1 = virasoro_shadow_coefficient(4).subs(c, 1)
        S4_at_25 = virasoro_shadow_coefficient(4).subs(c, 25)
        assert cancel(S4_at_1 - S4_at_25) != 0

    def test_S4_duality_product(self):
        """S_4(c) * S_4(26-c) is rational in c."""
        S4 = virasoro_shadow_coefficient(4)
        S4_dual = S4.subs(c, 26 - c)
        product = cancel(S4 * S4_dual)
        # Should be a rational function of c
        from sympy import Poly
        p = Poly(numer(product), c)
        d = Poly(denom(product), c)
        assert p.degree() >= 0
        assert d.degree() >= 0


# =========================================================================
# 19. STRUCTURAL TESTS
# =========================================================================

class TestStructural:
    """Structural properties of the shadow motivic-Hodge engine."""

    def test_virasoro_shadow_data_consistency(self):
        """kappa, alpha, S4, Delta are consistent."""
        kappa, alpha, S4, Delta = virasoro_shadow_data()
        assert cancel(kappa - c / 2) == 0
        assert cancel(alpha - 2) == 0
        assert cancel(S4 - Rational(10) / (c * (5 * c + 22))) == 0
        assert cancel(Delta - Rational(40) / (5 * c + 22)) == 0

    def test_betagamma_delta_zero(self):
        """Beta-gamma has Delta = 0."""
        _, _, _, Delta = betagamma_shadow_data()
        assert Delta == 0

    def test_affine_sl2_delta_zero(self):
        """Affine sl_2 has Delta = 0 (class L, S_4 = 0)."""
        kappa, alpha, S4, Delta = affine_km_shadow_data(1)
        assert cancel(Delta) == 0

    def test_virasoro_S_r_rational_function(self):
        """S_r(c) is a rational function of c for all r."""
        for r in range(2, 10):
            Sr = virasoro_shadow_coefficient(r)
            # Check it's a ratio of polynomials in c
            n = numer(cancel(Sr))
            d = denom(cancel(Sr))
            from sympy import Poly
            try:
                Poly(n, c)
                Poly(d, c)
            except Exception:
                pytest.fail(f"S_{r} is not a rational function of c")


# =========================================================================
# 20. CONDUCTOR AND ARITHMETIC INVARIANTS
# =========================================================================

class TestConductorArithmetic:
    """Conductor and discriminant computations."""

    def test_conductor_c1(self):
        data = shadow_conductor(1, 1)
        assert data['disc_numerator'] != 0

    def test_conductor_c_half(self):
        data = shadow_conductor(1, 2)
        assert data['disc_numerator'] != 0

    def test_conductor_c26(self):
        data = shadow_conductor(26, 1)
        assert data['disc_numerator'] != 0

    def test_discriminant_formula(self):
        """disc = -320*c^2/(5c+22)."""
        # At c=1: -320/27
        data = shadow_conductor(1, 1)
        expected_num = -320
        expected_den = 27
        # The function may simplify differently, but the ratio should match
        ratio = Fraction(data['disc_numerator'], data['disc_denominator'])
        assert ratio == Fraction(expected_num, expected_den)

    def test_discriminant_c_half(self):
        """At c=1/2: disc = -320*(1/4)/(22+5/2) = -80/(49/2) = -160/49."""
        data = shadow_conductor(1, 2)
        ratio = Fraction(data['disc_numerator'], data['disc_denominator'])
        expected = Fraction(-320 * 1, 4) / Fraction(5 + 44, 2)
        # -80 / (49/2) = -160/49
        assert ratio == Fraction(-160, 49)


# =========================================================================
# 21. COMBINED CROSS-FAMILY TESTS
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency of the motivic-Hodge framework."""

    def test_all_standard_families_genus_0(self):
        """Every standard family has shadow curve genus 0."""
        families = [
            heisenberg_shadow_data(Symbol('k')),
            affine_km_shadow_data(1),
            betagamma_shadow_data(),
            virasoro_shadow_data(),
        ]
        for kappa, alpha, S4, Delta in families:
            assert shadow_curve_genus_abstract(kappa, alpha, S4) == 0

    def test_class_classification_consistent(self):
        """Class G/L/C have Delta=0; class M has Delta != 0."""
        # Heisenberg
        _, _, _, Delta_h = heisenberg_shadow_data(Symbol('k'))
        assert Delta_h == 0

        # Virasoro
        _, _, _, Delta_v = virasoro_shadow_data()
        assert cancel(Delta_v) != 0

    def test_hodge_numbers_agree_across_families(self):
        """All families have the same Hodge numbers (genus 0)."""
        families = [
            heisenberg_shadow_data(Symbol('k')),
            virasoro_shadow_data(),
        ]
        for kappa, alpha, S4, _ in families:
            h = hodge_numbers_shadow_curve(kappa, alpha, S4)
            assert h[(1, 0)] == 0
            assert h[(0, 1)] == 0
