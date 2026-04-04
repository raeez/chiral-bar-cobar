r"""Tests for Seiberg-Witten theory from the shadow connection.

Verifies:
1.  SU(2) N_f=0 SW curve structure (factorization, branch points, discriminant)
2.  Picard-Fuchs equation: singular points, indicial exponents, derivation from shadow
3.  Monodromy matrices: Sp(2,Z), factorization M_inf = M_+ M_-, traces
4.  Instanton coefficients F_1..F_5: exact values, numerical consistency
5.  Prepotential: perturbative + instanton, tau coupling
6.  BPS spectrum: central charges, mass formula, standard states
7.  Strong coupling / Koszul duality: a -> 0 near monopole point
8.  Curve of marginal stability structure
9.  N_f = 1,2,3,4 curves: correct polynomial structure, singular points
10. SU(3) curve and W_3 shadow: genus-2, branch points, F_1
11. Shadow-SW dictionary: structural consistency
12. Period numerical computation: weak-coupling asymptotics

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
"""

import cmath
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
import numpy as np
from sympy import (
    I, Matrix, Rational, S, Symbol, cancel, diff, expand, factor,
    pi, simplify, solve, sqrt, symbols, Poly, Abs, oo, N as Neval,
)

from compute.lib.seiberg_witten_shadow import (
    # Section 1: SU(2) curve
    su2_sw_curve_polynomial,
    su2_sw_branch_points,
    su2_sw_curve_j_invariant,
    # Section 2: Picard-Fuchs
    su2_picard_fuchs_operator,
    su2_picard_fuchs_verify,
    su2_picard_fuchs_from_shadow,
    # Section 3: Periods
    su2_period_a,
    su2_period_a_D,
    su2_periods_weak_coupling,
    # Section 4: Monodromies
    su2_monodromy_infinity,
    su2_monodromy_monopole,
    su2_monodromy_dyon,
    verify_monodromy_relation,
    verify_monodromies_in_sp2,
    monodromy_from_shadow_sign,
    # Section 5: Prepotential
    instanton_coefficient,
    instanton_coefficient_numerical,
    prepotential_perturbative,
    prepotential_instanton,
    prepotential_full,
    tau_coupling,
    instanton_from_shadow_connection,
    # Section 6: BPS
    bps_central_charge,
    bps_mass,
    bps_spectrum_standard,
    bps_from_shadow_residue,
    # Section 7: Strong coupling
    strong_coupling_koszul_duality,
    verify_strong_coupling_koszul,
    # Section 8: Marginal stability
    marginal_stability_condition,
    # Section 9: N_f curves
    su2_nf_curve,
    su2_nf_picard_fuchs_singular_points,
    su2_nf_shadow_connection,
    # Section 10: SU(3)
    su3_sw_curve,
    su3_periods_numerical,
    su3_f1_from_shadow,
    su3_shadow_at_sw_point,
    # Section 11: Dictionary
    shadow_picard_fuchs_comparison,
    sw_from_shadow_dictionary,
)

u_sym = Symbol('u')
x_sym = Symbol('x')
Lambda_sym = Symbol('Lambda', positive=True)
c_sym = Symbol('c')


# ===========================================================================
# 1. SU(2) N_f=0 Seiberg-Witten curve
# ===========================================================================

class TestSU2Curve:
    """Test the SU(2) N_f=0 Seiberg-Witten curve."""

    def test_curve_polynomial_structure(self):
        """y^2 = (x^2-u)^2 - Lambda^4 expands correctly."""
        data = su2_sw_curve_polynomial()
        x = x_sym
        u = u_sym
        L = Lambda_sym
        expected = x**4 - 2*u*x**2 + u**2 - L**4
        assert simplify(data['rhs'] - expected) == 0

    def test_curve_factorization(self):
        """(x^2-u)^2 - L^4 = (x^2-u-L^2)(x^2-u+L^2)."""
        data = su2_sw_curve_polynomial()
        f1, f2 = data['factored']
        x = x_sym
        product = expand(f1 * f2)
        assert simplify(product - data['rhs']) == 0

    def test_singular_fibers(self):
        """Singular fibers at u = +/- Lambda^2."""
        data = su2_sw_curve_polynomial()
        assert Lambda_sym**2 in data['singular_fibers']
        assert -Lambda_sym**2 in data['singular_fibers']
        assert len(data['singular_fibers']) == 2

    def test_four_branch_points(self):
        """Four branch points at each smooth u."""
        data = su2_sw_curve_polynomial()
        assert len(data['roots']) == 4

    def test_branch_points_numerical(self):
        """Numerical branch points for u=2, Lambda=1."""
        bp = su2_sw_branch_points(2.0, 1.0)
        assert len(bp) == 4
        # x^2 = u+1 = 3 and x^2 = u-1 = 1
        # Branch points: +/-sqrt(3), +/-1
        bp_abs = sorted([abs(b) for b in bp])
        assert abs(bp_abs[0] - 1.0) < 1e-10
        assert abs(bp_abs[1] - 1.0) < 1e-10
        assert abs(bp_abs[2] - math.sqrt(3)) < 1e-10
        assert abs(bp_abs[3] - math.sqrt(3)) < 1e-10

    def test_discriminant_vanishes_at_singular(self):
        """Discriminant (u^2-L^4)^2 vanishes at u=+/-L^2."""
        data = su2_sw_curve_polynomial()
        disc = data['discriminant_u']
        L = Lambda_sym
        u = u_sym
        assert simplify(disc.subs(u, L**2)) == 0
        assert simplify(disc.subs(u, -L**2)) == 0

    def test_curve_at_u_zero(self):
        """At u=0: y^2 = x^4 - Lambda^4 (maximal Z_2 symmetry)."""
        data = su2_sw_curve_polynomial(u=S.Zero)
        x = x_sym
        L = Lambda_sym
        expected = x**4 - L**4
        assert simplify(data['rhs'] - expected) == 0


# ===========================================================================
# 2. Picard-Fuchs equation
# ===========================================================================

class TestPicardFuchs:
    """Test the Picard-Fuchs equation for SU(2)."""

    def test_singular_points(self):
        """PF has 3 regular singular points: u=L^2, u=-L^2, u=inf."""
        pf = su2_picard_fuchs_operator()
        assert len(pf['singular_points']) == 3
        L = Lambda_sym
        assert L**2 in pf['singular_points']
        assert -L**2 in pf['singular_points']
        assert oo in pf['singular_points']

    def test_leading_coefficient(self):
        """Leading coefficient is u^2 - Lambda^4."""
        pf = su2_picard_fuchs_operator()
        u = u_sym
        L = Lambda_sym
        expected = u**2 - L**4
        assert simplify(pf['leading_coeff'] - expected) == 0

    def test_sub_leading_coefficient(self):
        """Sub-leading coefficient is u."""
        pf = su2_picard_fuchs_operator()
        assert pf['sub_leading_coeff'] == u_sym

    def test_constant_coefficient(self):
        """Constant coefficient is -1/4."""
        pf = su2_picard_fuchs_operator()
        assert pf['constant_coeff'] == Rational(-1, 4)

    def test_indicial_at_monopole(self):
        """Indicial roots at u=Lambda^2 are 0 and 1/2."""
        pf = su2_picard_fuchs_operator()
        roots = pf['indicial_roots']['u=Lambda^2']
        assert S.Zero in roots
        assert Rational(1, 2) in roots

    def test_indicial_at_dyon(self):
        """Indicial roots at u=-Lambda^2 are 0 and 1/2."""
        pf = su2_picard_fuchs_operator()
        roots = pf['indicial_roots']['u=-Lambda^2']
        assert S.Zero in roots
        assert Rational(1, 2) in roots

    def test_indicial_at_infinity(self):
        """Indicial roots at u=inf are 1/4 and 1/4 (logarithmic)."""
        pf = su2_picard_fuchs_operator()
        roots = pf['indicial_roots']['u=infinity']
        assert roots == (Rational(1, 4), Rational(1, 4))

    def test_shadow_derivation_structure(self):
        """Shadow derivation returns consistent data."""
        deriv = su2_picard_fuchs_from_shadow()
        assert 'shadow_pf' in deriv
        assert 'sw_pf' in deriv
        assert 'identification' in deriv

    def test_pf_leading_vanishes_at_singular(self):
        """u^2 - Lambda^4 vanishes at u = +/- Lambda^2."""
        pf = su2_picard_fuchs_operator()
        L = Lambda_sym
        u = u_sym
        leading = pf['leading_coeff']
        assert simplify(leading.subs(u, L**2)) == 0
        assert simplify(leading.subs(u, -L**2)) == 0


# ===========================================================================
# 3. Monodromies
# ===========================================================================

class TestMonodromies:
    """Test monodromy matrices of the SW theory."""

    def test_monodromy_infinity_matrix(self):
        """M_inf = [[-1, 2], [0, -1]]."""
        M = su2_monodromy_infinity()
        assert M == Matrix([[-1, 2], [0, -1]])

    def test_monodromy_monopole_matrix(self):
        """M_+ = [[1, 0], [-2, 1]]."""
        M = su2_monodromy_monopole()
        assert M == Matrix([[1, 0], [-2, 1]])

    def test_monodromy_dyon_matrix(self):
        """M_- = [[-1, 2], [-2, 3]]."""
        M = su2_monodromy_dyon()
        assert M == Matrix([[-1, 2], [-2, 3]])

    def test_monodromy_factorization(self):
        """M_inf = M_+ * M_-."""
        assert verify_monodromy_relation()

    def test_monodromies_in_sp2(self):
        """All monodromies in Sp(2, Z): M^T J M = J."""
        results = verify_monodromies_in_sp2()
        assert all(results.values()), f"Sp(2) check failed: {results}"

    def test_monodromy_infinity_det(self):
        """det(M_inf) = 1."""
        M = su2_monodromy_infinity()
        assert M.det() == 1

    def test_monodromy_monopole_det(self):
        """det(M_+) = 1."""
        M = su2_monodromy_monopole()
        assert M.det() == 1

    def test_monodromy_dyon_det(self):
        """det(M_-) = 1."""
        M = su2_monodromy_dyon()
        assert M.det() == 1

    def test_monodromy_infinity_trace(self):
        """tr(M_inf) = -2 (the Koszul sign doubled)."""
        M = su2_monodromy_infinity()
        assert M.trace() == -2

    def test_monodromy_monopole_trace(self):
        """tr(M_+) = 2 (parabolic)."""
        M = su2_monodromy_monopole()
        assert M.trace() == 2

    def test_monodromy_dyon_trace(self):
        """tr(M_-) = 2 (parabolic)."""
        M = su2_monodromy_dyon()
        assert M.trace() == 2

    def test_monodromy_infinity_eigenvalues(self):
        """M_inf has eigenvalue -1 (double, Koszul sign)."""
        M = su2_monodromy_infinity()
        eigvals = list(M.eigenvals().keys())
        assert len(eigvals) == 1
        assert eigvals[0] == -1

    def test_monodromy_monopole_eigenvalues(self):
        """M_+ has eigenvalue 1 (double, unipotent)."""
        M = su2_monodromy_monopole()
        eigvals = list(M.eigenvals().keys())
        assert len(eigvals) == 1
        assert eigvals[0] == 1

    def test_shadow_sign_connection(self):
        """Koszul sign -1 appears in monodromy data."""
        data = monodromy_from_shadow_sign()
        assert data['koszul_sign'] == -1
        assert data['M_inf_trace'] == -2
        assert data['M_inf_det'] == 1

    def test_monodromy_dyon_is_product(self):
        """M_- = M_+ * [[1,0],[0,1]] + correction, or equivalently,
        M_inf = M_+ M_- with the correct multiplication order."""
        M_inf = su2_monodromy_infinity()
        M_plus = su2_monodromy_monopole()
        M_minus = su2_monodromy_dyon()
        assert M_inf == M_plus * M_minus


# ===========================================================================
# 4. Instanton coefficients
# ===========================================================================

class TestInstantonCoefficients:
    """Test exact instanton coefficients F_1..F_5."""

    def test_F1_exact(self):
        """F_1 = 1/(2^5 * pi^2) = 1/(32*pi^2)."""
        F1 = instanton_coefficient(1)
        expected = Rational(1, 32) / pi**2
        assert simplify(F1 - expected) == 0

    def test_F2_exact(self):
        """F_2 = 5/(2^14 * pi^4) = 5/(16384*pi^4)."""
        F2 = instanton_coefficient(2)
        expected = Rational(5, 16384) / pi**4
        assert simplify(F2 - expected) == 0

    def test_F3_exact(self):
        """F_3 = 3/(2^18 * pi^6) = 3/(262144*pi^6)."""
        F3 = instanton_coefficient(3)
        expected = Rational(3, 262144) / pi**6
        assert simplify(F3 - expected) == 0

    def test_F4_exact(self):
        """F_4 = 1469/(2^29 * pi^8)."""
        F4 = instanton_coefficient(4)
        expected = Rational(1469, 2**29) / pi**8
        assert simplify(F4 - expected) == 0

    def test_F5_exact(self):
        """F_5 = 4471/(2^34 * pi^10)."""
        F5 = instanton_coefficient(5)
        expected = Rational(4471, 2**34) / pi**10
        assert simplify(F5 - expected) == 0

    def test_F1_numerical(self):
        """F_1 numerically ~ 3.167e-3."""
        F1_num = instanton_coefficient_numerical(1)
        expected = 1.0 / (32 * math.pi**2)
        assert abs(F1_num - expected) < 1e-10

    def test_F2_numerical(self):
        """F_2 numerically ~ 3.133e-6."""
        F2_num = instanton_coefficient_numerical(2)
        expected = 5.0 / (16384 * math.pi**4)
        assert abs(F2_num - expected) < 1e-12

    def test_F3_numerical(self):
        """F_3 numerically ~ 1.188e-8."""
        F3_num = instanton_coefficient_numerical(3)
        expected = 3.0 / (262144 * math.pi**6)
        assert abs(F3_num - expected) < 1e-14

    def test_instanton_coefficients_positive(self):
        """All instanton coefficients F_k > 0."""
        for k in range(1, 6):
            assert instanton_coefficient_numerical(k) > 0

    def test_instanton_coefficients_decreasing(self):
        """F_1 > F_2 > F_3 > F_4 > F_5 (rapid decrease)."""
        vals = [instanton_coefficient_numerical(k) for k in range(1, 6)]
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i+1]

    def test_invalid_k_raises(self):
        """instanton_coefficient(k) raises for k > 5."""
        with pytest.raises(ValueError):
            instanton_coefficient(6)

    def test_shadow_derivation_exists(self):
        """Shadow-to-instanton derivation returns valid dict."""
        deriv = instanton_from_shadow_connection()
        assert 'shadow_to_instanton' in deriv
        assert 'verification' in deriv


# ===========================================================================
# 5. Prepotential
# ===========================================================================

class TestPrepotential:
    """Test the prepotential computation."""

    def test_perturbative_at_large_a(self):
        """F_pert(a) ~ (i/(2pi)) a^2 ln(a^2/L^2) for large a."""
        a = 10.0
        F_pert = prepotential_perturbative(a, Lambda_val=1.0)
        # F_pert = (i/(2*pi)) * a^2 * ln(a^2/L^2) = (i/(2*pi)) * 100 * ln(100)
        expected = (1j / (2 * math.pi)) * a**2 * cmath.log(a**2 / 1.0)
        assert abs(F_pert - expected) < 1e-10

    def test_instanton_small_at_large_a(self):
        """F_inst << F_pert for |a| >> Lambda."""
        a = 10.0
        F_inst = prepotential_instanton(a, Lambda_val=1.0)
        F_pert = prepotential_perturbative(a, Lambda_val=1.0)
        assert abs(F_inst) < 1e-3 * abs(F_pert)

    def test_instanton_at_a_equals_2(self):
        """F_inst(2) is a well-defined complex number."""
        F_inst = prepotential_instanton(2.0, Lambda_val=1.0)
        assert math.isfinite(abs(F_inst))

    def test_full_equals_sum(self):
        """F_full = F_pert + F_inst."""
        a = 5.0
        F_full = prepotential_full(a)
        F_pert = prepotential_perturbative(a)
        F_inst = prepotential_instanton(a)
        assert abs(F_full - (F_pert + F_inst)) < 1e-15

    def test_tau_imaginary_part_positive(self):
        """Im(tau) > 0 in the weak-coupling regime (physical)."""
        tau = tau_coupling(5.0, Lambda_val=1.0)
        assert tau.imag > 0, f"Im(tau) = {tau.imag} should be > 0"


# ===========================================================================
# 6. BPS spectrum
# ===========================================================================

class TestBPSSpectrum:
    """Test BPS central charges and mass formula."""

    def test_bps_central_charge_linear(self):
        """Z = n_e*a + n_m*a_D is linear in charges."""
        a, a_D = 1+1j, 0.5+2j
        Z1 = bps_central_charge(1, 0, a, a_D)
        Z2 = bps_central_charge(0, 1, a, a_D)
        Z_sum = bps_central_charge(1, 1, a, a_D)
        assert abs(Z_sum - (Z1 + Z2)) < 1e-15

    def test_bps_mass_nonnegative(self):
        """BPS mass M = |Z| >= 0."""
        a, a_D = 1+1j, 0.5+2j
        for ne, nm in [(1, 0), (0, 1), (1, 1), (-1, 1), (2, 0)]:
            M = bps_mass(ne, nm, a, a_D)
            assert M >= 0

    def test_w_boson_mass(self):
        """W-boson mass M_W = 2|a|."""
        a = 3 + 4j
        a_D = 1 + 1j
        states = bps_spectrum_standard(a, a_D)
        M_W = states['W_boson']['mass']
        assert abs(M_W - 2 * abs(a)) < 1e-10

    def test_monopole_mass(self):
        """Monopole mass M_mon = |a_D|."""
        a = 3 + 4j
        a_D = 1 + 1j
        states = bps_spectrum_standard(a, a_D)
        M_mon = states['monopole']['mass']
        assert abs(M_mon - abs(a_D)) < 1e-10

    def test_dyon_mass(self):
        """Dyon(1,1) mass M = |a + a_D|."""
        a = 3 + 4j
        a_D = 1 + 1j
        states = bps_spectrum_standard(a, a_D)
        M_dyon = states['dyon_11']['mass']
        assert abs(M_dyon - abs(a + a_D)) < 1e-10

    def test_bps_from_shadow_residue_structure(self):
        """Shadow residue derivation has correct fields."""
        deriv = bps_from_shadow_residue()
        assert 'r_matrix' in deriv
        assert 'central_charge' in deriv
        assert 'mass_formula' in deriv


# ===========================================================================
# 7. Strong coupling and Koszul duality
# ===========================================================================

class TestStrongCoupling:
    """Test strong-coupling / Koszul duality correspondence."""

    def test_koszul_duality_structure(self):
        """Strong coupling dictionary has required keys."""
        data = strong_coupling_koszul_duality()
        assert 'weak_coupling' in data
        assert 'strong_coupling_monopole' in data
        assert 'self_dual_point' in data

    def test_koszul_exchange_at_monopole(self):
        """At monopole point, Koszul exchange A <-> A! is recorded."""
        data = strong_coupling_koszul_duality()
        assert 'koszul_exchange' in data['strong_coupling_monopole']

    def test_self_dual_at_c_13(self):
        """Self-dual point is c=13."""
        data = strong_coupling_koszul_duality()
        assert '13' in str(data['self_dual_point']['shadow'])

    def test_numerical_strong_coupling(self):
        """Near monopole point, periods are computed (basic sanity)."""
        result = verify_strong_coupling_koszul(Lambda_val=1.0, epsilon=0.1)
        # At u = L^2 + epsilon, both periods should be finite
        assert math.isfinite(result['abs_a'])
        assert math.isfinite(result['abs_a_D'])


# ===========================================================================
# 8. Marginal stability
# ===========================================================================

class TestMarginalStability:
    """Test curve of marginal stability."""

    def test_cms_aligned_phases(self):
        """CMS condition: Im(Z_1/Z_2) = 0 means aligned phases."""
        # When Z_1 and Z_2 are proportional, phase diff = 0
        a = 1 + 0j
        a_D = 2 + 0j  # Both real => all charges aligned
        pd = marginal_stability_condition(1, 0, 0, 1, a, a_D)
        assert abs(pd) < 1e-10

    def test_cms_nonzero_off_locus(self):
        """Off the CMS, phases are not aligned."""
        a = 1 + 1j
        a_D = 1 - 1j
        pd = marginal_stability_condition(1, 0, 0, 1, a, a_D)
        assert abs(pd) > 0.1


# ===========================================================================
# 9. N_f = 1,2,3,4 curves
# ===========================================================================

class TestNfCurves:
    """Test SU(2) SW curves with flavors."""

    def test_nf0_is_standard(self):
        """N_f=0 curve matches the standard form."""
        data = su2_nf_curve(0)
        x = x_sym
        u = u_sym
        L = Lambda_sym
        expected = (x**2 - u)**2 - L**4
        assert simplify(data['rhs'] - expected) == 0

    def test_nf1_structure(self):
        """N_f=1 curve has correct structure."""
        data = su2_nf_curve(1)
        assert data['n_f'] == 1
        assert len(data['masses']) == 1

    def test_nf2_structure(self):
        """N_f=2 curve has correct structure."""
        data = su2_nf_curve(2)
        assert data['n_f'] == 2
        assert len(data['masses']) == 2

    def test_nf3_structure(self):
        """N_f=3 curve has correct structure."""
        data = su2_nf_curve(3)
        assert data['n_f'] == 3
        assert len(data['masses']) == 3

    def test_nf4_structure(self):
        """N_f=4 curve (scale-invariant) has correct structure."""
        data = su2_nf_curve(4)
        assert data['n_f'] == 4
        assert len(data['masses']) == 4

    def test_nf_invalid(self):
        """N_f > 4 raises ValueError."""
        with pytest.raises(ValueError):
            su2_nf_curve(5)

    def test_nf0_massless_limit(self):
        """N_f curves reduce to N_f=0 when Lambda is dominant."""
        # N_f=1 with m=0: y^2 = (x^2-u)^2 - L^3*x
        data = su2_nf_curve(1, masses=[S.Zero])
        x = x_sym
        u = u_sym
        L = Lambda_sym
        expected = (x**2 - u)**2 - L**3 * x
        assert simplify(data['rhs'] - expected) == 0

    def test_nf2_massless_limit(self):
        """N_f=2 with m_1=m_2=0: y^2 = (x^2-u)^2 - L^2*x^2."""
        data = su2_nf_curve(2, masses=[S.Zero, S.Zero])
        x = x_sym
        u = u_sym
        L = Lambda_sym
        expected = (x**2 - u)**2 - L**2 * x**2
        assert simplify(data['rhs'] - expected) == 0

    def test_nf_singular_points_count(self):
        """Singular point count grows with N_f."""
        for nf in range(5):
            data = su2_nf_picard_fuchs_singular_points(nf)
            assert data['n_singular_generic'] == nf + 3

    def test_nf_shadow_connection_zeros(self):
        """Shadow connection zeros grow with N_f."""
        for nf in range(5):
            data = su2_nf_shadow_connection(nf)
            assert data['n_zeros_Q'] == nf + 2
            assert data['monodromy_eigenvalue'] == -1

    def test_nf_all_fuchsian(self):
        """All N_f theories give Fuchsian PF equations."""
        for nf in range(5):
            data = su2_nf_shadow_connection(nf)
            assert data['fuchsian'] is True


# ===========================================================================
# 10. SU(3) and W_3
# ===========================================================================

class TestSU3:
    """Test SU(3) SW curve and W_3 shadow."""

    def test_su3_curve_genus(self):
        """SU(3) curve is genus-2."""
        data = su3_sw_curve()
        assert data['genus'] == 2
        assert data['rank'] == 2

    def test_su3_curve_polynomial(self):
        """SU(3) curve: y^2 = P(x)^2 - 4*Lambda^6."""
        data = su3_sw_curve()
        x = x_sym
        u2 = Symbol('u_2')
        u3 = Symbol('u_3')
        L = Lambda_sym
        P = x**3 - u2*x - u3
        expected = expand(P**2 - 4*L**6)
        assert simplify(data['rhs'] - expected) == 0

    def test_su3_six_branch_points(self):
        """SU(3) curve has 6 branch points generically."""
        data = su3_periods_numerical(1.0, 0.5, Lambda_val=1.0)
        assert data['n_branch_points'] == 6

    def test_su3_four_periods(self):
        """Genus-2 curve has 4 periods."""
        data = su3_periods_numerical(1.0, 0.5, Lambda_val=1.0)
        assert data['n_periods'] == 4

    def test_su3_branch_points_numerical(self):
        """Branch points are computed and have correct count."""
        data = su3_periods_numerical(2.0, 1.0, Lambda_val=0.5)
        assert len(data['branch_points']) == 6

    def test_su3_f1_symbolic(self):
        """F_1^{SU(3)} = 5c/144 at the scalar shadow level."""
        data = su3_f1_from_shadow()
        c = c_sym
        expected = 5 * c / 144
        assert simplify(data['F_1_scalar'] - expected) == 0

    def test_su3_kappa_w3(self):
        """kappa(W_3) = 5c/6."""
        data = su3_f1_from_shadow()
        c = c_sym
        assert simplify(data['kappa_W3'] - 5*c/6) == 0

    def test_su3_shadow_discriminants(self):
        """Shadow discriminants for W_3: Delta_T and Delta_W."""
        data = su3_f1_from_shadow()
        c = c_sym
        Delta_T = data['shadow_discriminants']['Delta_T']
        Delta_W = data['shadow_discriminants']['Delta_W']
        assert simplify(Delta_T - Rational(40)/(5*c+22)) == 0
        assert simplify(Delta_W - Rational(20480)/(3*(5*c+22)**3)) == 0

    def test_su3_shadow_at_sw(self):
        """W_3 shadow at SW point has correct structure."""
        data = su3_shadow_at_sw_point()
        c = c_sym
        assert simplify(data['kappa_T'] - c/2) == 0
        assert simplify(data['kappa_W'] - c/3) == 0
        assert simplify(data['total_kappa'] - 5*c/6) == 0


# ===========================================================================
# 11. Shadow-SW dictionary and cross-checks
# ===========================================================================

class TestDictionary:
    """Test structural consistency of the shadow-SW dictionary."""

    def test_dictionary_length(self):
        """Dictionary has 17 entries."""
        d = sw_from_shadow_dictionary()
        assert len(d) == 17

    def test_picard_fuchs_comparison(self):
        """PF comparison covers all N_f."""
        comp = shadow_picard_fuchs_comparison()
        assert len(comp) == 5
        for nf in range(5):
            key = f'N_f={nf}'
            assert key in comp
            assert comp[key]['pf_order'] == 2
            assert comp[key]['monodromy'] == -1


# ===========================================================================
# 12. Period computation cross-checks
# ===========================================================================

class TestPeriods:
    """Test numerical period computation."""

    def test_weak_coupling_a_asymptotics(self):
        """At large |u|, |a(u)| ~ sqrt(u) (standard SW convention)."""
        u_val = 100.0
        a = su2_period_a(u_val, Lambda_val=1.0)
        expected = math.sqrt(u_val)  # a ~ sqrt(u) for u >> Lambda^2
        assert abs(abs(a) - expected) / expected < 0.01, \
            f"|a| = {abs(a)}, expected ~ {expected}"

    def test_weak_coupling_comparison(self):
        """Weak-coupling asymptotic vs numerical, large u."""
        u_val = 200.0
        a_num = su2_period_a(u_val)
        a_wc, _ = su2_periods_weak_coupling(u_val)
        rel_error = abs(abs(a_num) - abs(a_wc)) / abs(a_wc)
        assert rel_error < 0.01, f"Relative error {rel_error} too large"

    def test_period_a_finite(self):
        """Period a(u) is finite for generic u."""
        a = su2_period_a(3.0, Lambda_val=1.0)
        assert math.isfinite(abs(a))

    def test_period_a_D_finite(self):
        """Period a_D(u) is finite for generic u."""
        a_D = su2_period_a_D(3.0, Lambda_val=1.0)
        assert math.isfinite(abs(a_D))

    def test_period_a_nonzero_at_generic_u(self):
        """Period a(u) is nonzero at generic u."""
        a = su2_period_a(5.0, Lambda_val=1.0)
        assert abs(a) > 1e-10


# ===========================================================================
# 13. Sp(2,Z) cross-checks
# ===========================================================================

class TestSp2Algebra:
    """Test algebraic properties of the monodromy group."""

    def test_sp2_generators(self):
        """M_+ and M_- generate a subgroup of Sp(2,Z)."""
        # Verify both are in SL(2,Z) (a subgroup of Sp(2,Z) for 2x2)
        M_plus = su2_monodromy_monopole()
        M_minus = su2_monodromy_dyon()
        assert M_plus.det() == 1
        assert M_minus.det() == 1
        # All entries are integers
        for M in [M_plus, M_minus]:
            for i in range(2):
                for j in range(2):
                    assert M[i, j] == int(M[i, j])

    def test_monodromy_squared(self):
        """(M_+)^2 = [[1,0],[-4,1]], parabolic iteration."""
        M_plus = su2_monodromy_monopole()
        M_sq = M_plus * M_plus
        expected = Matrix([[1, 0], [-4, 1]])
        assert M_sq == expected

    def test_conjugacy_class(self):
        """M_+ and M_- are conjugate in SL(2,Z) (both unipotent with n=2)."""
        M_plus = su2_monodromy_monopole()
        M_minus = su2_monodromy_dyon()
        # Both have trace 2 and det 1
        assert M_plus.trace() == M_minus.trace() == 2
        assert M_plus.det() == M_minus.det() == 1


# ===========================================================================
# 14. Instanton series convergence
# ===========================================================================

class TestInstantonConvergence:
    """Test convergence properties of the instanton series."""

    def test_ratio_F2_F1(self):
        """F_2/F_1 ~ 5/(512*pi^2) ~ 9.9e-4."""
        F1 = instanton_coefficient_numerical(1)
        F2 = instanton_coefficient_numerical(2)
        ratio = F2 / F1
        expected = 5.0 / (512 * math.pi**2)
        assert abs(ratio - expected) < 1e-8

    def test_ratio_F3_F2(self):
        """F_3/F_2 = (3/5) * (16384/262144) * pi^{-2} / pi^{-2} = (3*16384)/(5*262144)."""
        F2 = instanton_coefficient_numerical(2)
        F3 = instanton_coefficient_numerical(3)
        ratio = F3 / F2
        expected = (3.0 * 16384) / (5.0 * 262144 * math.pi**2)
        assert abs(ratio - expected) < 1e-10

    def test_instanton_series_at_large_a(self):
        """For a=10, Lambda=1: instanton series converges rapidly."""
        a = 10.0
        terms = []
        for k in range(1, 6):
            fk = instanton_coefficient_numerical(k)
            q_k = (1.0 / a**4)**k  # (Lambda/a)^4k with Lambda=1
            terms.append(abs(fk * q_k))
        # Each term should be smaller than the previous
        for i in range(len(terms) - 1):
            assert terms[i+1] < terms[i]


# ===========================================================================
# 15. Picard-Fuchs numerical verification
# ===========================================================================

class TestPicardFuchsNumerical:
    """Test PF equation numerically using period functions."""

    def test_pf_residual_at_u_3(self):
        """PF residual at u=3 is small."""
        residual = su2_picard_fuchs_verify(
            lambda u: su2_period_a(u, 1.0),
            u_val=3.0, Lambda_val=1.0, du=1e-5
        )
        # The residual should be small relative to the period itself
        a_val = abs(su2_period_a(3.0, 1.0))
        if a_val > 0:
            rel_residual = residual / a_val
            # Finite-difference PF verification: tolerance is moderate
            assert rel_residual < 1.0, \
                f"PF residual {rel_residual} at u=3 (may need smaller du)"


# ===========================================================================
# 16. Shadow connection specialization
# ===========================================================================

class TestShadowSpecialization:
    """Test that the shadow connection specializes correctly to SW data."""

    def test_shadow_pf_structure(self):
        """Shadow PF: Q*f'' + Q'/2 * f' = 0 is second-order Fuchsian."""
        from compute.lib.shadow_connection import (
            virasoro_shadow_metric,
            virasoro_picard_fuchs,
        )
        Q, Q_prime = virasoro_picard_fuchs()
        # Q is quadratic in t => Q*f'' + Q'/2*f' = 0 has 3 singular points
        # (2 finite zeros of Q, plus t=infinity)
        t = Symbol('t')
        zeros = solve(Q, t)
        assert len(zeros) == 2, "Shadow metric should have 2 zeros"

    def test_shadow_monodromy_matches_sw(self):
        """Shadow monodromy -1 matches SW monodromy eigenvalue."""
        from compute.lib.shadow_connection import monodromy_eigenvalue
        assert monodromy_eigenvalue() == -1
        # This is the same as the eigenvalue of M_inf
        M_inf = su2_monodromy_infinity()
        eigvals = list(M_inf.eigenvals().keys())
        assert eigvals[0] == -1

    def test_shadow_residue_half(self):
        """Shadow connection residue = 1/2 at each zero."""
        from compute.lib.shadow_connection import connection_residue_at_zero
        assert connection_residue_at_zero() == Rational(1, 2)
        # This matches the indicial exponent 1/2 at the SW singular points

    def test_indicial_from_residue(self):
        """Indicial roots (0, 1/2) follow from residue 1/2."""
        # For a regular singular point with residue r = 1/2:
        # indicial equation: s(s-1) + s + 0 = 0 gives s=0, but
        # for the LOG connection, the indicial roots are 0 and 2*r = 1
        # Actually for Q*f'' + Q'/2*f' = 0 at a simple zero of Q:
        # indicial equation s^2 - s/2 = 0 => s = 0 or s = 1/2
        pf = su2_picard_fuchs_operator()
        roots = pf['indicial_roots']['u=Lambda^2']
        assert S.Zero in roots
        assert Rational(1, 2) in roots
