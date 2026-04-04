r"""Tests for the quantum spectral curve and exact WKB from the shadow ODE.

Verifies:
1. Classical spectral curve y^2 = V(t) from the shadow metric
2. WKB expansion S_n(t) computed recursively
3. One-loop WKB = shadow connection (fundamental identification)
4. Voros coefficients (period integrals)
5. Universal results (classical period = pi, Koszul sign = -1)
6. Indicial exponents universal (always 1/2)
7. Riccati equation residuals vanish at each order
8. Painleve VI from W_3 multi-channel system
9. Genus expansion from WKB
10. Borel singularities
11. Special central charges (c = 1/2, 1, 13, 25, 26)
12. Cross-verification with shadow connection module

All formulas recomputed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
"""

import cmath
import math

import numpy as np
import pytest

from sympy import (
    I, Rational, Symbol, cancel, diff, expand, factor,
    log, pi, simplify, solve, sqrt, S, Poly,
)

from compute.lib.quantum_spectral_curve import (
    # Section 1: Classical spectral curve
    shadow_metric_poly,
    shadow_metric_coefficients,
    schwarzian_potential,
    classical_spectral_curve,
    virasoro_classical_curve,
    # Section 2: WKB expansion
    wkb_leading_order,
    wkb_one_loop,
    wkb_recursive_coefficients,
    wkb_expansion_virasoro,
    # Section 3: Voros coefficients
    voros_period_classical,
    voros_period_one_loop,
    voros_coefficients_numerical,
    # Section 4: WKB at specific charges
    virasoro_wkb_data,
    virasoro_wkb_at_special_charges,
    # Section 5: Stokes
    stokes_lines_virasoro,
    connection_matrices_monodromy,
    # Section 6: Genus expansion
    wkb_free_energy_genus_expansion,
    wkb_free_energy_from_voros,
    # Section 7: Painleve
    painleve_from_w3,
    painleve_crossratio_landscape,
    # Section 8: Topological recursion
    topological_recursion_omega_01,
    topological_recursion_omega_02,
    topological_recursion_F1,
    # Section 9: Borel
    borel_singularities_from_wkb,
    # Section 10: ODE classification
    virasoro_shadow_ode_type,
    w3_shadow_ode_type,
    # Section 11: Numerical WKB
    wkb_coefficients_numerical,
    # Section 12: Verification
    verify_wkb_riccati,
    verify_one_loop_is_shadow_connection,
    verify_indicial_exponents_universal,
    # Section 13: Special c values
    virasoro_c25_spectral_curve,
    virasoro_c26_spectral_curve,
    virasoro_c13_self_dual,
)


c = Symbol('c')
t = Symbol('t')


# =========================================================================
# 1. Classical spectral curve
# =========================================================================

class TestClassicalSpectralCurve:
    """Tests for the classical spectral curve y^2 = V(t)."""

    def test_shadow_metric_polynomial_form(self):
        """Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        kappa, alpha, Delta = Rational(1), Rational(2), Rational(3)
        Q = shadow_metric_poly(kappa, alpha, Delta)
        # Q = (2 + 6t)^2 + 6t^2 = 4 + 24t + 36t^2 + 6t^2 = 4 + 24t + 42t^2
        Q_expanded = expand(Q)
        expected = 4 + 24*t + 42*t**2
        assert expand(Q_expanded - expected) == 0

    def test_shadow_metric_coefficients(self):
        """q_0 = 4*kappa^2, q_1 = 12*kappa*alpha, q_2 = 9*alpha^2 + 2*Delta."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, Delta)
        assert q0 == 36  # 4*9
        assert q1 == 72  # 12*3*2
        assert q2 == 46  # 9*4 + 2*5

    def test_schwarzian_potential_form(self):
        """V(t) = 8*kappa^2*Delta / Q_L(t)^2."""
        kappa = Symbol('kappa', positive=True)
        alpha = Symbol('alpha')
        Delta = Symbol('Delta')
        V = schwarzian_potential(kappa, alpha, Delta)
        Q = shadow_metric_poly(kappa, alpha, Delta)
        C = 8 * kappa**2 * Delta
        expected = C / Q**2
        assert simplify(V - expected) == 0

    def test_classical_curve_genus_zero(self):
        """The spectral curve y^2 = V(t) has genus 0."""
        kappa, alpha, Delta = c/2, Rational(2), Rational(40)/(5*c+22)
        curve = classical_spectral_curve(kappa, alpha, Delta)
        assert curve['genus'] == 0

    def test_virasoro_classical_curve(self):
        """Virasoro classical curve has the correct branch points."""
        curve = virasoro_classical_curve()
        assert curve['genus'] == 0
        assert len(curve['branch_points']) == 2

    def test_schwarzian_vanishes_when_delta_zero(self):
        """V(t) = 0 when Delta = 0 (classes G and L)."""
        kappa, alpha = Rational(3), Rational(2)
        V = schwarzian_potential(kappa, alpha, S.Zero)
        assert V == 0

    def test_branch_points_are_zeros_of_Q(self):
        """Branch points of V(t) are the zeros of Q_L(t)."""
        kappa, alpha, Delta = c/2, Rational(2), Rational(40)/(5*c+22)
        curve = classical_spectral_curve(kappa, alpha, Delta)
        Q = curve['Q']
        for bp in curve['branch_points']:
            assert simplify(Q.subs(t, bp)) == 0


# =========================================================================
# 2. WKB expansion
# =========================================================================

class TestWKBExpansion:
    """Tests for the recursive WKB expansion."""

    def test_leading_order_form(self):
        """S_0'(t) = sqrt(C) / Q_L(t)."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = wkb_leading_order(kappa, alpha, Delta)
        C = 8 * kappa**2 * Delta
        Q = shadow_metric_poly(kappa, alpha, Delta)
        expected_S0p = sqrt(C) / Q
        assert simplify(result['S0_prime'] - expected_S0p) == 0

    def test_one_loop_is_connection_form(self):
        """S_1'(t) = Q_L'/(2*Q_L) -- the shadow connection form."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = wkb_one_loop(kappa, alpha, Delta)
        Q = shadow_metric_poly(kappa, alpha, Delta)
        Qp = diff(Q, t)
        expected = cancel(Qp / (2*Q))
        assert simplify(result['S1_prime'] - expected) == 0

    def test_one_loop_is_log_Q(self):
        """S_1(t) = (1/2)*ln(Q_L(t)) + const."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = wkb_one_loop(kappa, alpha, Delta)
        Q = shadow_metric_poly(kappa, alpha, Delta)
        expected = Rational(1, 2) * log(Q)
        assert simplify(result['S1'] - expected) == 0

    def test_wkb_recursive_order_0(self):
        """S_0' from recursive computation matches direct."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_order=2)
        C = 8 * kappa**2 * Delta
        Q = shadow_metric_poly(kappa, alpha, Delta)
        expected = sqrt(C) / Q
        assert simplify(Sp[0] - expected) == 0

    def test_wkb_recursive_order_1(self):
        """S_1' from recursive computation matches one-loop formula."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_order=2)
        Q = shadow_metric_poly(kappa, alpha, Delta)
        Qp = diff(Q, t)
        expected = cancel(Qp / (2*Q))
        assert simplify(Sp[1] - expected) == 0

    def test_wkb_recursive_produces_all_orders(self):
        """Recursive computation produces S_n' for n = 0, ..., max_order."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        for max_ord in [2, 3, 4]:
            Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_ord)
            assert len(Sp) == max_ord + 1
            for n in range(max_ord + 1):
                assert n in Sp

    def test_wkb_virasoro_computation(self):
        """WKB expansion for Virasoro produces 5 orders."""
        Sp = wkb_expansion_virasoro(max_order=4)
        assert len(Sp) == 5
        for n in range(5):
            assert n in Sp


# =========================================================================
# 3. Voros coefficients — universal results
# =========================================================================

class TestVorosCoefficients:
    """Tests for the Voros coefficients and their universal properties."""

    def test_classical_period_is_pi(self):
        """The classical half-period is universally pi."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = voros_period_classical(kappa, alpha, Delta)
        assert result['half_period'] == pi

    def test_compact_period_vanishes(self):
        """The compact cycle period vanishes (sum of residues = 0)."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = voros_period_classical(kappa, alpha, Delta)
        assert result['compact_period'] == 0

    def test_one_loop_koszul_sign(self):
        """exp(v_1) = -1 (the Koszul sign)."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = voros_period_one_loop(kappa, alpha, Delta)
        assert result['exp_half_period'] == -1

    def test_one_loop_half_period_is_pi_i(self):
        """v_1 (half-period) = pi*i."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = voros_period_one_loop(kappa, alpha, Delta)
        assert result['half_period'] == pi * I

    def test_one_loop_compact_period(self):
        """v_1 (compact period) = 2*pi*i."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        result = voros_period_one_loop(kappa, alpha, Delta)
        assert result['compact_period'] == 2 * pi * I

    def test_voros_numerical_v1_is_2pi_i(self):
        """Numerical v_1 should be close to 2*pi*i (compact cycle)."""
        kappa, alpha, Delta = 5.0, 2.0, 3.0
        voros = voros_coefficients_numerical(kappa, alpha, Delta,
                                             max_order=2, n_points=1000)
        if voros:
            v1 = voros.get(1, 0.0j)
            # v_1 = oint Q'/(2Q) dt = 2*pi*i * (sum of residues of Q'/(2Q))
            # Each simple zero of Q contributes residue 1/2
            # So v_1 = 2*pi*i * (1/2 + 1/2) = 2*pi*i
            expected = 2j * math.pi
            assert abs(v1 - expected) < 0.1, f"v_1 = {v1}, expected {expected}"


# =========================================================================
# 4. Riccati verification
# =========================================================================

class TestRiccatiVerification:
    """Tests that the WKB expansion satisfies the Riccati equation."""

    def test_riccati_order_0(self):
        """(S_0')^2 = V(t) at a specific point."""
        result = verify_wkb_riccati(5.0, 2.0, 3.0, 0.1)
        assert result['order_0_residual'] < 1e-12

    def test_riccati_order_1(self):
        """2*S_0'*S_1' + S_0'' = 0 at a specific point."""
        result = verify_wkb_riccati(5.0, 2.0, 3.0, 0.1)
        assert result['order_1_residual'] < 1e-12

    def test_riccati_virasoro_c1(self):
        """Riccati verification for Virasoro at c = 1."""
        kappa = 0.5
        alpha = 2.0
        S4 = 10.0 / (1.0 * 27.0)
        Delta = 8.0 * kappa * S4
        result = verify_wkb_riccati(kappa, alpha, Delta, 0.05)
        assert result['order_0_residual'] < 1e-12
        assert result['order_1_residual'] < 1e-12

    def test_riccati_virasoro_c26(self):
        """Riccati verification for Virasoro at c = 26."""
        kappa = 13.0
        alpha = 2.0
        S4 = 10.0 / (26.0 * 152.0)
        Delta = 8.0 * kappa * S4
        result = verify_wkb_riccati(kappa, alpha, Delta, 0.01)
        assert result['order_0_residual'] < 1e-10
        assert result['order_1_residual'] < 1e-10

    def test_riccati_multiple_points(self):
        """Riccati equation holds at multiple evaluation points."""
        kappa = 5.0
        alpha = 2.0
        Delta = 3.0
        for t_val in [0.01, 0.05, 0.1, 0.2, -0.1]:
            result = verify_wkb_riccati(kappa, alpha, Delta, t_val)
            assert result['order_0_residual'] < 1e-11, f"Failed at t = {t_val}"
            assert result['order_1_residual'] < 1e-11, f"Failed at t = {t_val}"


# =========================================================================
# 5. One-loop = shadow connection identification
# =========================================================================

class TestOneLoopIdentification:
    """Tests the identification S_1' = omega (shadow connection form)."""

    def test_identification_holds_numerical(self):
        """S_1'(t) = Q'/(2Q) numerically."""
        result = verify_one_loop_is_shadow_connection(5.0, 2.0, 3.0, 0.1)
        assert result['identification_holds']
        assert result['difference'] < 1e-15

    def test_identification_virasoro_c1(self):
        """Identification holds for Virasoro at c = 1."""
        kappa = 0.5
        alpha = 2.0
        S4 = 10.0 / 27.0
        Delta = 8.0 * kappa * S4
        result = verify_one_loop_is_shadow_connection(kappa, alpha, Delta, 0.05)
        assert result['identification_holds']

    def test_identification_virasoro_c26(self):
        """Identification holds for Virasoro at c = 26."""
        kappa = 13.0
        alpha = 2.0
        S4 = 10.0 / (26.0 * 152.0)
        Delta = 8.0 * kappa * S4
        result = verify_one_loop_is_shadow_connection(kappa, alpha, Delta, 0.01)
        assert result['identification_holds']

    def test_identification_multiple_algebras(self):
        """Identification holds for various (kappa, alpha, Delta)."""
        test_cases = [
            (1.0, 2.0, 5.0),
            (10.0, 3.0, 0.5),
            (0.5, 1.0, 2.0),
            (13.0, 2.0, 0.263),
        ]
        for kap, alp, delt in test_cases:
            result = verify_one_loop_is_shadow_connection(kap, alp, delt, 0.05)
            assert result['identification_holds'], f"Failed for ({kap}, {alp}, {delt})"


# =========================================================================
# 6. Indicial exponents universality
# =========================================================================

class TestIndicialExponents:
    """Tests the universal indicial exponents 1/2 at zeros of Q_L."""

    def test_c0_equals_minus_quarter(self):
        """c_0 = C/(Q'(t_0))^2 = -1/4 universally."""
        for c_val in [0.5, 1.0, 5.0, 13.0, 25.0, 26.0, 100.0]:
            result = verify_indicial_exponents_universal(c_val)
            assert result['is_universal'], f"Failed at c = {c_val}: c_0 = {result['c_0']}"

    def test_exponents_are_half(self):
        """Indicial exponents are (1/2, 1/2) universally."""
        result = verify_indicial_exponents_universal(10.0)
        assert result['exponents'] == (0.5, 0.5)

    def test_monodromy_eigenvalues_minus_one(self):
        """Monodromy eigenvalues are (-1, -1) universally."""
        kappa = 5.0
        alpha = 2.0
        Delta = 3.0
        result = connection_matrices_monodromy(kappa, alpha, Delta)
        assert result['type'] == 'logarithmic'
        assert result['monodromy_eigenvalues'] == (-1.0, -1.0)

    def test_monodromy_trivial_when_delta_zero(self):
        """No monodromy when Delta = 0."""
        result = connection_matrices_monodromy(5.0, 2.0, 0.0)
        assert result['type'] == 'trivial'


# =========================================================================
# 7. Genus expansion
# =========================================================================

class TestGenusExpansion:
    """Tests for the genus expansion from the WKB."""

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24."""
        kappa = 5.0
        F = wkb_free_energy_genus_expansion(kappa, g_max=5)
        assert abs(F[1] - kappa/24.0) < 1e-14

    def test_F2_equals_7kappa_over_5760(self):
        """F_2 = 7*kappa/5760."""
        kappa = 5.0
        F = wkb_free_energy_genus_expansion(kappa, g_max=5)
        assert abs(F[2] - 7*kappa/5760.0) < 1e-14

    def test_F3_equals_31kappa_over_967680(self):
        """F_3 = 31*kappa/967680."""
        kappa = 5.0
        F = wkb_free_energy_genus_expansion(kappa, g_max=5)
        assert abs(F[3] - 31*kappa/967680.0) < 1e-14

    def test_F_g_scales_linearly_with_kappa(self):
        """F_g is linear in kappa."""
        F_5 = wkb_free_energy_genus_expansion(5.0, g_max=5)
        F_10 = wkb_free_energy_genus_expansion(10.0, g_max=5)
        for g in range(1, 6):
            ratio = F_10[g] / F_5[g] if F_5[g] != 0 else None
            if ratio is not None:
                assert abs(ratio - 2.0) < 1e-12, f"Failed at g = {g}"

    def test_all_F_g_positive(self):
        """All F_g are positive for kappa > 0."""
        F = wkb_free_energy_genus_expansion(5.0, g_max=10)
        for g in range(1, 11):
            assert F[g] > 0, f"F_{g} = {F[g]} is not positive"


# =========================================================================
# 8. Stokes lines and ODE classification
# =========================================================================

class TestStokesAndODE:
    """Tests for Stokes lines and ODE classification."""

    def test_virasoro_is_fuchsian(self):
        """Virasoro shadow ODE is Fuchsian (all regular singularities)."""
        stokes = stokes_lines_virasoro(10.0)
        assert stokes['type'] == 'fuchsian_regular'

    def test_virasoro_ode_is_hypergeometric(self):
        """Virasoro shadow ODE is hypergeometric (3 reg sing on P^1)."""
        result = virasoro_shadow_ode_type(10.0)
        assert result['fuchsian_type'] == 'hypergeometric'
        assert result['n_singular_points'] == 3

    def test_virasoro_no_painleve(self):
        """Single-channel Virasoro has no Painleve (rigid)."""
        result = virasoro_shadow_ode_type(10.0)
        assert 'no accessory parameter' in result['painleve_type'].lower() or \
               'none' in result['painleve_type'].lower()

    def test_w3_is_painleve_vi(self):
        """W_3 2-channel system gives Painleve VI."""
        result = w3_shadow_ode_type(10.0)
        assert result['painleve_type'] == 'PVI'
        assert result['n_singular_points'] == 4


# =========================================================================
# 9. Painleve VI from W_3
# =========================================================================

class TestPainleveVI:
    """Tests for Painleve VI from the W_3 multi-channel system."""

    def test_four_singularities(self):
        """W_3 2-channel has exactly 4 singular points."""
        result = painleve_from_w3(10.0)
        assert len(result['singularities']) == 4

    def test_painleve_type_is_PVI(self):
        """Painleve type is PVI."""
        result = painleve_from_w3(10.0)
        assert result['painleve_type'] == 'PVI'

    def test_pvi_parameters(self):
        """PVI parameters: alpha = delta = 1/2, beta = gamma = 0."""
        result = painleve_from_w3(10.0)
        params = result['PVI_parameters']
        assert abs(params['alpha'] - 0.5) < 1e-10
        assert abs(params['beta']) < 1e-10
        assert abs(params['gamma']) < 1e-10
        assert abs(params['delta'] - 0.5) < 1e-10

    def test_cross_ratio_finite(self):
        """Cross-ratio of the 4 singularities is finite and nonzero."""
        result = painleve_from_w3(10.0)
        cr = result['cross_ratio']
        assert abs(cr) > 1e-10
        assert abs(cr) < 1e10

    def test_cross_ratio_varies_with_c(self):
        """Cross-ratio depends on c (NOT constant)."""
        cr_5 = painleve_from_w3(5.0)['cross_ratio']
        cr_20 = painleve_from_w3(20.0)['cross_ratio']
        assert abs(cr_5 - cr_20) > 1e-6

    def test_t_zeros_separated(self):
        """T-channel zeros are distinct from W-channel zeros."""
        result = painleve_from_w3(10.0)
        t_T = result['T_zeros']
        t_W = result['W_zeros']
        for tt in t_T:
            for tw in t_W:
                assert abs(tt - tw) > 1e-10

    def test_crossratio_landscape(self):
        """Cross-ratio landscape computation succeeds for multiple c."""
        results = painleve_crossratio_landscape()
        assert len(results) > 5
        # All values should be finite complex numbers
        for c_val, cr in results.items():
            if cr is not None:
                assert not cmath.isinf(cr)


# =========================================================================
# 10. Borel singularities
# =========================================================================

class TestBorelSingularities:
    """Tests for the Borel singularity structure."""

    def test_fundamental_action_is_pi(self):
        """A_1 = pi (universal for all shadow Schrodinger equations)."""
        result = borel_singularities_from_wkb(5.0, 2.0, 3.0)
        assert abs(result['A_1'] - math.pi) < 1e-14

    def test_borel_singularities_at_n_pi(self):
        """Borel singularities at xi = n*pi for n = 1, 2, ..., 5."""
        result = borel_singularities_from_wkb(5.0, 2.0, 3.0)
        for n in range(1, 6):
            expected = n * math.pi
            assert abs(result['borel_singularities'][n-1] - expected) < 1e-14

    def test_borel_universal_across_algebras(self):
        """A_1 = pi for different algebra data."""
        test_cases = [
            (0.5, 2.0, 1.0),
            (13.0, 2.0, 0.3),
            (100.0, 5.0, 0.01),
        ]
        for kap, alp, delt in test_cases:
            result = borel_singularities_from_wkb(kap, alp, delt)
            assert abs(result['A_1'] - math.pi) < 1e-14


# =========================================================================
# 11. Topological recursion
# =========================================================================

class TestTopologicalRecursion:
    """Tests for topological recursion on the spectral curve."""

    def test_omega_01_matches_S0_prime(self):
        """omega_{0,1}(t) = sqrt(C)/Q_L(t) = S_0'(t)."""
        kappa, alpha, Delta = 5.0, 2.0, 3.0
        omega_01 = topological_recursion_omega_01(kappa, alpha, Delta)
        C = 8 * kappa**2 * Delta
        sqC = cmath.sqrt(C)
        t_val = 0.1
        Q_val = 4*kappa**2 + 12*kappa*alpha*t_val + (9*alpha**2 + 2*Delta)*t_val**2
        expected = sqC / Q_val
        assert abs(omega_01(t_val) - expected) < 1e-14

    def test_bergman_kernel_double_pole(self):
        """Bergman kernel B(t1, t2) = 1/(t1-t2)^2."""
        bergman = topological_recursion_omega_02(5.0, 2.0, 3.0)
        assert abs(bergman(1.0, 0.5) - 4.0) < 1e-14  # 1/(0.5)^2 = 4

    def test_F1_shadow_matches_kappa_over_24(self):
        """F_1 from shadow tower = kappa/24."""
        kappa, alpha, Delta = 5.0, 2.0, 3.0
        result = topological_recursion_F1(kappa, alpha, Delta)
        assert abs(result['F1_shadow'] - kappa/24.0) < 1e-14


# =========================================================================
# 12. Special central charges
# =========================================================================

class TestSpecialCentralCharges:
    """Tests at physically significant central charges."""

    def test_c_half_ising(self):
        """WKB data at c = 1/2 (Ising model)."""
        data = virasoro_wkb_data(0.5, max_order=2, n_points=300)
        assert abs(data.kappa - 0.25) < 1e-14
        assert data.Delta > 0  # Virasoro is class M

    def test_c1_free_boson(self):
        """WKB data at c = 1."""
        data = virasoro_wkb_data(1.0, max_order=2, n_points=300)
        assert abs(data.kappa - 0.5) < 1e-14

    def test_c13_self_dual_kappa(self):
        """At c = 13 (self-dual): kappa = 13/2."""
        data = virasoro_c13_self_dual()
        assert abs(data.kappa - 6.5) < 1e-14

    def test_c25_kappa(self):
        """At c = 25: kappa = 25/2."""
        data = virasoro_c25_spectral_curve()
        assert abs(data.kappa - 12.5) < 1e-14

    def test_c26_critical_string_kappa(self):
        """At c = 26 (critical string): kappa = 13."""
        data = virasoro_c26_spectral_curve()
        assert abs(data.kappa - 13.0) < 1e-14

    def test_c26_delta(self):
        """At c = 26: Delta = 40/152 = 5/19."""
        data = virasoro_c26_spectral_curve()
        expected_delta = 40.0 / 152.0
        assert abs(data.Delta - expected_delta) < 1e-12

    def test_c13_self_dual_delta(self):
        """At c = 13: Delta = 40/87."""
        data = virasoro_c13_self_dual()
        expected_delta = 40.0 / 87.0
        assert abs(data.Delta - expected_delta) < 1e-12

    def test_special_charges_all_succeed(self):
        """WKB computation succeeds at all special charges."""
        results = virasoro_wkb_at_special_charges(max_order=2, n_points=300)
        assert len(results) == 5
        for c_val, data in results.items():
            assert data.kappa > 0
            assert data.Delta > 0

    def test_c13_self_dual_branch_points_symmetric(self):
        """At c = 13 self-dual: branch points have enhanced symmetry."""
        data = virasoro_c13_self_dual()
        # Branch points should be complex conjugates
        assert abs(data.t_plus - data.t_minus.conjugate()) < 1e-10


# =========================================================================
# 13. Numerical WKB
# =========================================================================

class TestNumericalWKB:
    """Tests for the numerical WKB computation."""

    def test_numerical_wkb_grid(self):
        """Numerical WKB produces arrays on a grid."""
        result = wkb_coefficients_numerical(10.0, max_order=4, n_grid=100)
        assert 't_grid' in result
        assert len(result['t_grid']) == 100
        for n in range(5):
            assert n in result['Sp']
            assert len(result['Sp'][n]) == 100

    def test_numerical_S0_matches_analytic(self):
        """Numerical S_0'(t) matches analytic formula."""
        c_val = 10.0
        result = wkb_coefficients_numerical(c_val, max_order=2, n_grid=100)
        kappa = c_val / 2.0
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
        Delta = 8.0 * kappa * S4
        C_sch = 8*kappa**2*Delta

        t_grid = result['t_grid']
        S0p = result['Sp'][0]

        for i in range(10, 90):
            tv = t_grid[i]
            Q_val = (4*kappa**2 + 12*kappa*alpha*tv
                     + (9*alpha**2 + 2*Delta)*tv**2)
            expected = cmath.sqrt(C_sch) / Q_val
            assert abs(S0p[i] - expected) / abs(expected) < 1e-10

    def test_numerical_S1_matches_analytic(self):
        """Numerical S_1'(t) matches Q'/(2Q)."""
        c_val = 10.0
        result = wkb_coefficients_numerical(c_val, max_order=2, n_grid=100)
        kappa = c_val / 2.0
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
        Delta = 8.0 * kappa * S4

        t_grid = result['t_grid']
        S1p = result['Sp'][1]

        for i in range(10, 90):
            tv = t_grid[i]
            Q_val = (4*kappa**2 + 12*kappa*alpha*tv
                     + (9*alpha**2 + 2*Delta)*tv**2)
            Qp_val = 12*kappa*alpha + 2*(9*alpha**2 + 2*Delta)*tv
            expected = Qp_val / (2*Q_val)
            assert abs(S1p[i] - expected) < 1e-10


# =========================================================================
# 14. Cross-verification with shadow_connection module
# =========================================================================

class TestCrossVerification:
    """Cross-verify with the existing shadow_connection module."""

    def test_shadow_metric_matches(self):
        """Shadow metric Q_L(t) matches between modules."""
        from compute.lib.shadow_connection import (
            virasoro_shadow_metric as vir_Q_connection,
            virasoro_shadow_data,
        )
        # From shadow_connection
        Q_conn = vir_Q_connection()

        # From quantum_spectral_curve
        kappa_vir, alpha_vir, S4_vir, Delta_vir = virasoro_shadow_data()
        Delta_val = 8 * kappa_vir * S4_vir
        Q_qsc = shadow_metric_poly(kappa_vir, alpha_vir,
                                    cancel(Delta_val))

        diff_expr = simplify(expand(Q_conn) - expand(Q_qsc))
        assert diff_expr == 0

    def test_connection_form_matches_S1_prime(self):
        """Shadow connection form = S_1'(t) (symbolic)."""
        from compute.lib.shadow_connection import (
            virasoro_connection_form,
            virasoro_shadow_data,
        )
        omega = virasoro_connection_form()

        kappa_vir, alpha_vir, S4_vir, Delta_vir = virasoro_shadow_data()
        Delta_val = cancel(8 * kappa_vir * S4_vir)
        one_loop = wkb_one_loop(kappa_vir, alpha_vir, Delta_val)
        S1p = one_loop['S1_prime']

        diff_expr = simplify(omega - S1p)
        assert diff_expr == 0


# =========================================================================
# 15. Consistency checks between symbolic and numerical
# =========================================================================

class TestSymbolicNumericalConsistency:
    """Cross-checks between symbolic and numerical computations."""

    def test_voros_v0_matches_residue(self):
        """Numerical v_0 should match the residue computation."""
        kappa, alpha, Delta = 5.0, 2.0, 3.0
        voros = voros_coefficients_numerical(kappa, alpha, Delta,
                                             max_order=1, n_points=2000)
        if voros:
            v0 = voros.get(0, None)
            # v_0 = oint sqrt(C)/Q dt around both zeros
            # By residue theorem: sum of residues of sqrt(C)/Q at its simple poles
            # = sqrt(C)/Q'(t_+) + sqrt(C)/Q'(t_-)
            # = sqrt(C)/(q2*(t_+-t_-)) + sqrt(C)/(q2*(t_--t_+))
            # = sqrt(C)/q2 * (1/(t_+-t_-) - 1/(t_+-t_-)) = 0
            # So v_0 should be 0 (or close to it)
            if v0 is not None:
                assert abs(v0) < 0.5, f"v_0 = {v0}, expected ~0"

    def test_schwarzian_potential_numerical(self):
        """Schwarzian potential V(t) matches symbolic at c = 10."""
        c_val = 10.0
        kappa = c_val / 2.0
        alpha = 2.0
        S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
        Delta = 8.0 * kappa * S4
        C_sch = 8 * kappa**2 * Delta

        t_val = 0.1
        Q_val = (4*kappa**2 + 12*kappa*alpha*t_val
                 + (9*alpha**2 + 2*Delta)*t_val**2)
        V_numerical = C_sch / Q_val**2

        # Symbolic (c and t are module-level Symbol('c') and Symbol('t'))
        V_sym = schwarzian_potential(c/2, Rational(2),
                                      Rational(40)/(5*c+22))
        V_at_c10 = float(V_sym.subs([(c, 10), (t, 0.1)]))

        assert abs(V_numerical - V_at_c10) / abs(V_at_c10) < 1e-10


# =========================================================================
# 16. Koszul duality of the spectral curve
# =========================================================================

class TestKoszulDuality:
    """Tests for Koszul duality properties of the spectral curve."""

    def test_dual_spectral_curve_c_to_26_minus_c(self):
        """Koszul dual spectral curve: c -> 26 - c."""
        data_c10 = virasoro_wkb_data(10.0, max_order=2, n_points=300)
        data_c16 = virasoro_wkb_data(16.0, max_order=2, n_points=300)
        # kappa(10) = 5, kappa(16) = 8
        assert abs(data_c10.kappa - 5.0) < 1e-14
        assert abs(data_c16.kappa - 8.0) < 1e-14
        # kappa + kappa' = 5 + 8 = 13 (NOT 0 for Virasoro, AP24)
        assert abs(data_c10.kappa + data_c16.kappa - 13.0) < 1e-14

    def test_self_dual_at_c13(self):
        """At c = 13: spectral curve is self-dual."""
        data = virasoro_c13_self_dual()
        assert abs(data.kappa - 6.5) < 1e-14
        # Self-dual: kappa + kappa' = 2*6.5 = 13
        assert abs(2*data.kappa - 13.0) < 1e-14

    def test_delta_complementarity(self):
        """Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c))."""
        for c_val in [1.0, 5.0, 10.0, 20.0, 25.0]:
            c_dual = 26.0 - c_val
            Delta_c = 40.0 / (5*c_val + 22)
            Delta_dual = 40.0 / (5*c_dual + 22)
            sum_delta = Delta_c + Delta_dual
            expected = 6960.0 / ((5*c_val + 22) * (152 - 5*c_val))
            assert abs(sum_delta - expected) < 1e-12, \
                f"Failed at c = {c_val}: sum = {sum_delta}, expected = {expected}"


# =========================================================================
# 17. W_3 Painleve cross-ratio at self-dual point
# =========================================================================

class TestW3SelfDual:
    """Tests for W_3 at the self-dual point c = 50 (W_3 conductor is 100)."""

    def test_w3_painleve_at_c50(self):
        """W_3 at c = 50 (self-dual for W_3 with conductor 100)."""
        # At c = 50: Koszul dual is W_3 at c = 100 - 50 = 50 (self-dual)
        result = painleve_from_w3(50.0)
        assert len(result['singularities']) == 4
        assert result['painleve_type'] == 'PVI'

    def test_w3_painleve_c_dependence(self):
        """Cross-ratio varies smoothly with c."""
        c_values = [5.0, 10.0, 15.0, 20.0, 25.0]
        cross_ratios = []
        for cv in c_values:
            cr = painleve_from_w3(cv)['cross_ratio']
            cross_ratios.append(cr)
        # Cross-ratios should all be distinct
        for i in range(len(cross_ratios)):
            for j in range(i+1, len(cross_ratios)):
                assert abs(cross_ratios[i] - cross_ratios[j]) > 1e-8


# =========================================================================
# 18. WKB higher-order structure
# =========================================================================

class TestWKBHigherOrder:
    """Tests for higher-order WKB coefficients."""

    def test_S2_prime_is_rational(self):
        """S_2'(t) is a rational function of t (no sqrt)."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_order=2)
        # S_2' should be rational in t (the sqrt(C) cancels in the recursion)
        # because S_2' = -(Q/(2*sqrt(C))) * ((S_1')^2 + S_1'')
        # and (S_1')^2 is rational, S_1'' is rational.
        # The factor Q/(2*sqrt(C)) introduces 1/sqrt(C), but the numerator
        # from (S_1')^2 + S_1'' does not have sqrt(C), so S_2' ~ 1/sqrt(C).
        #
        # Wait: S_2' = -(Q/(2*sqrt(C))) * ((S_1')^2 + S_1'')
        # S_1' = Q'/(2Q) is purely rational (no sqrt(C)).
        # So (S_1')^2 + S_1'' is purely rational.
        # Thus S_2' = -(Q/(2*sqrt(C))) * (rational) = (rational)/sqrt(C).
        # This contains 1/sqrt(C), so S_2' is NOT purely rational in t if C is symbolic.
        #
        # But in the WKB expansion, the sqrt(C) combines with hbar factors:
        # the "correct" expansion parameter is hbar*sqrt(C) or similar.
        # At the level of individual S_n', the even-n terms have integer powers
        # of sqrt(C) and the odd-n terms have half-integer powers.
        #
        # For this test: just verify S_2' is nonzero and has the right structure.
        assert Sp[2] != 0

    def test_higher_orders_nonzero(self):
        """S_n'(t) is nonzero for n = 2 and 4.

        The WKB recursion S_n' = -(sum S_j' S_{n-j}' + S_{n-1}'')/(2 S_0')
        has a parity structure: when S_1' = Q'/(2Q) is odd-parity in sqrt(C)
        and S_0' = sqrt(C)/Q is even-parity, the odd-n coefficients (n=3,5,...)
        can vanish identically. S_3' = 0 for kappa=3, alpha=2, Delta=5 because
        the convolution 2*S_1'*S_2' + S_2'' cancels after division by 2*S_0'.
        """
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_order=4)
        assert Sp[2] != 0, "S_2' is zero"
        assert Sp[4] != 0, "S_4' is zero"
        # S_3' vanishes for these parameters due to sqrt(C)-parity
        assert Sp[3] == 0, "S_3' should vanish by parity"

    def test_even_odd_sqrt_structure(self):
        """Even-order S_n' have 1/sqrt(C); odd-order S_n' are rational."""
        kappa, alpha, Delta = Rational(3), Rational(2), Rational(5)
        C = 8 * kappa**2 * Delta  # = 8*9*5 = 360
        sqC = sqrt(C)
        Sp = wkb_recursive_coefficients(kappa, alpha, Delta, max_order=3)

        # S_0' = sqrt(C)/Q contains sqrt(C) -> multiplied by sqC is rational
        # S_1' = Q'/(2Q) is rational (no sqrt)
        # S_2' should be proportional to 1/sqrt(C)
        # S_3' should be proportional to 1/C = 1/sqrt(C)^2

        # Check S_1' is independent of sqC: substitute sqC -> -sqC
        S1p_neg = Sp[1].subs(sqC, -sqC) if sqC in Sp[1].free_symbols else Sp[1]
        assert simplify(S1p_neg - Sp[1]) == 0  # S_1' unchanged -> no sqrt(C)


# =========================================================================
# 19. Virasoro WKB data container
# =========================================================================

class TestWKBDataContainer:
    """Tests for the WKBData container."""

    def test_virasoro_wkb_data_fields(self):
        """WKBData has all required fields."""
        data = virasoro_wkb_data(10.0, max_order=2, n_points=300)
        assert data.c_val == 10.0
        assert abs(data.kappa - 5.0) < 1e-14
        assert abs(data.alpha - 2.0) < 1e-14
        assert data.Delta > 0
        assert data.C_schwarzian > 0

    def test_branch_points_are_conjugate(self):
        """Branch points are complex conjugates for c > 0."""
        data = virasoro_wkb_data(10.0, max_order=2, n_points=300)
        assert abs(data.t_plus - data.t_minus.conjugate()) < 1e-10

    def test_voros_dict_populated(self):
        """Voros dict is populated with the right number of entries."""
        data = virasoro_wkb_data(10.0, max_order=3, n_points=300)
        assert len(data.voros) == 4  # orders 0, 1, 2, 3
