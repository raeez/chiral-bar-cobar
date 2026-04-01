#!/usr/bin/env python3
r"""
test_shadow_epstein_zeta.py -- Tests for the Epstein zeta of the shadow metric.

Tests organized into:
1. Shadow metric data consistency
2. Binary form properties (positive definiteness, discriminant)
3. Lattice sum vs theta-splitting agreement (Re(s) > 1)
4. Functional equation Xi(s) = Xi(1-s) for all minimal models
5. Number-theoretic identification (quadratic field, class number)
6. Specific central charge tests (Ising, Potts, self-dual, free boson)
7. Dirichlet L-function tests
8. Cross-checks between Epstein and Dedekind zeta for h=1
9. Deeper L-function investigation (class number survey)
"""

import pytest
import math
from fractions import Fraction

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_epstein_zeta import (
    virasoro_shadow_data,
    minimal_model_c,
    binary_quadratic_form,
    quadratic_form_discriminant,
    virasoro_discriminant,
    virasoro_form,
    theta_binary_form,
    epstein_phi,
    epstein_zeta,
    epstein_zeta_lattice_sum,
    epstein_zeta_virasoro,
    completed_epstein,
    completed_epstein_virasoro,
    functional_equation_test,
    squarefree_part,
    _is_fundamental_discriminant,
    fundamental_discriminant,
    class_number_small,
    roots_of_unity,
    kronecker_symbol,
    dirichlet_l_function,
    dedekind_zeta,
    scaled_integer_form,
    quadratic_field_from_disc,
    minimal_model_epstein_data,
    verify_functional_equation_virasoro,
    deeper_l_function_investigation,
)


# ================================================================
# 1. Shadow metric data consistency
# ================================================================

class TestShadowMetricData:
    """Verify shadow data formulas (AP1 compliance: recompute from first principles)."""

    def test_virasoro_kappa(self):
        """kappa = c/2 for Virasoro."""
        for c in [Fraction(1, 2), Fraction(7, 10), Fraction(4, 5), 1, 13]:
            data = virasoro_shadow_data(c)
            if isinstance(c, Fraction):
                assert data['kappa'] == c / 2
            else:
                assert abs(data['kappa'] - c / 2) < 1e-15

    def test_virasoro_alpha(self):
        """alpha = 2 for Virasoro (c-independent)."""
        for c in [Fraction(1, 2), Fraction(7, 10), 1, 13]:
            data = virasoro_shadow_data(c)
            expected = Fraction(2) if isinstance(c, Fraction) else 2.0
            assert data['alpha'] == expected

    def test_virasoro_S4(self):
        """S4 = 10/(c*(5c+22)) for Virasoro."""
        c = Fraction(1, 2)
        data = virasoro_shadow_data(c)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert data['S4'] == expected
        # Numerical check: c=1/2 -> S4 = 10/(1/2*49/2) = 10*4/49 = 40/49
        assert data['S4'] == Fraction(40, 49)

    def test_virasoro_Delta(self):
        """Delta = 40/(5c+22) for Virasoro."""
        c = Fraction(14, 15)
        data = virasoro_shadow_data(c)
        expected = Fraction(40) / (5 * c + 22)
        assert data['Delta'] == expected
        # c=14/15: 5*14/15+22 = 70/15+22 = 70/15+330/15 = 400/15 = 80/3
        # Delta = 40/(80/3) = 40*3/80 = 3/2
        assert data['Delta'] == Fraction(3, 2)

    def test_minimal_model_c(self):
        """c = 1 - 6/(m(m+1)) for M(m, m+1)."""
        assert minimal_model_c(3) == Fraction(1, 2)
        assert minimal_model_c(4) == Fraction(7, 10)
        assert minimal_model_c(5) == Fraction(4, 5)


# ================================================================
# 2. Binary form properties
# ================================================================

class TestBinaryForm:
    """Verify properties of the binary quadratic form from the shadow metric."""

    def test_form_coefficients(self):
        """Q(m,n) = 4kappa^2*m^2 + 12*kappa*alpha*mn + (9*alpha^2+16*kappa*S4)*n^2."""
        c = Fraction(1, 2)
        data = virasoro_shadow_data(c)
        a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
        # kappa = 1/4, alpha = 2, S4 = 40/49
        assert a == Fraction(1, 4)  # 4*(1/4)^2 = 4/16 = 1/4
        assert b == Fraction(6)  # 12*(1/4)*2 = 6
        # 9*4 + 16*(1/4)*(40/49) = 36 + 160/49 = (36*49+160)/49 = (1764+160)/49 = 1924/49
        assert cc == Fraction(1924, 49)

    def test_positive_definite(self):
        """Q is positive definite for all c > -22/5."""
        for m in range(3, 15):
            c = minimal_model_c(m)
            data = virasoro_shadow_data(c)
            a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
            disc = quadratic_form_discriminant(a, b, cc)
            assert float(a) > 0, f"a = {a} not positive for m={m}"
            assert float(disc) < 0, f"disc = {disc} not negative for m={m}"

    def test_discriminant_formula(self):
        """disc(Q) = -320*c^2/(5c+22) for Virasoro."""
        for m in range(3, 10):
            c = minimal_model_c(m)
            data = virasoro_shadow_data(c)
            a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
            disc_computed = quadratic_form_discriminant(a, b, cc)
            disc_formula = virasoro_discriminant(c)
            assert disc_computed == disc_formula, (
                f"Discriminant mismatch at m={m}: {disc_computed} vs {disc_formula}")

    def test_discriminant_equals_minus_32_kappa_sq_Delta(self):
        """disc = -32*kappa^2*Delta (the theoretical formula)."""
        for m in range(3, 10):
            c = minimal_model_c(m)
            data = virasoro_shadow_data(c)
            disc = virasoro_discriminant(c)
            expected = -32 * data['kappa'] ** 2 * data['Delta']
            assert disc == expected


# ================================================================
# 3. Lattice sum vs theta-splitting agreement
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestLatticeVsTheta:
    """Verify lattice sum and theta splitting agree for Re(s) > 1."""

    def test_agreement_simple_form(self):
        """m^2+n^2: lattice sum vs theta splitting at s=2."""
        E_lattice = epstein_zeta_lattice_sum(2.0, 1, 0, 1, N=100)
        E_theta = complex(epstein_zeta(2.0, 1, 0, 1, N_theta=20))
        assert abs(E_lattice - E_theta) / abs(E_lattice) < 0.001

    def test_agreement_virasoro_ising(self):
        """Virasoro c=1/2: lattice sum vs theta splitting at s=2."""
        a, b, cc, D = virasoro_form(0.5)
        E_lattice = epstein_zeta_lattice_sum(2.0, a, b, cc, N=80)
        E_theta = complex(epstein_zeta(2.0, a, b, cc, N_theta=18))
        assert abs(E_lattice - E_theta) / abs(E_lattice) < 0.01

    def test_agreement_multiple_s(self):
        """m^2+n^2 at s=1.5, 2.0, 2.5, 3.0."""
        for s in [1.5, 2.0, 2.5, 3.0]:
            E_lat = epstein_zeta_lattice_sum(s, 1, 0, 1, N=80)
            E_th = complex(epstein_zeta(s, 1, 0, 1, N_theta=18))
            rel_err = abs(E_lat - E_th) / abs(E_lat)
            assert rel_err < 0.01, f"Agreement fails at s={s}: rel_err={rel_err}"

    def test_known_value_m2_n2(self):
        """m^2+n^2: E(s) = 4*zeta(s)*L(s, chi_{-4})."""
        s = 2.5
        E_theta = complex(epstein_zeta(s, 1, 0, 1, N_theta=20))
        # L(s, chi_{-4}) by direct sum
        L_val = sum(([0, 1, 0, -1][n % 4]) * n ** (-s) for n in range(1, 20001))
        E_known = 4 * float(mpmath.zeta(s)) * L_val
        assert abs(E_theta - E_known) / abs(E_known) < 0.001


# ================================================================
# 4. Functional equation Xi(s) = Xi(1-s)
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestFunctionalEquation:
    """Verify the functional equation for the completed Epstein zeta."""

    def test_fe_m2_n2(self):
        """Xi(s) = Xi(1-s) for Q = m^2+n^2."""
        for s in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
            result = functional_equation_test(s, 1, 0, 1, N_theta=20)
            assert result['passes'], f"FE fails at s={s}: rel_err={result['rel_err']}"

    def test_fe_ising(self):
        """Xi(s) = Xi(1-s) for Virasoro c=1/2 (Ising)."""
        a, b, cc, D = virasoro_form(0.5)
        for s in [0.3, 0.5, 0.7]:
            result = functional_equation_test(s, a, b, cc, N_theta=18)
            assert result['rel_err'] < 0.01, (
                f"FE fails at s={s}: rel_err={result['rel_err']}")

    def test_fe_tricritical_ising(self):
        """Xi(s) = Xi(1-s) for Virasoro c=7/10."""
        a, b, cc, D = virasoro_form(0.7)
        for s in [0.3, 0.5, 0.7]:
            result = functional_equation_test(s, a, b, cc, N_theta=18)
            assert result['rel_err'] < 0.01

    def test_fe_potts(self):
        """Xi(s) = Xi(1-s) for Virasoro c=4/5 (3-state Potts)."""
        a, b, cc, D = virasoro_form(0.8)
        for s in [0.3, 0.5, 0.7]:
            result = functional_equation_test(s, a, b, cc, N_theta=18)
            assert result['rel_err'] < 0.01

    def test_fe_m9_10(self):
        """Xi(s) = Xi(1-s) for M(9,10) c=14/15 (h=1)."""
        a, b, cc, D = virasoro_form(14.0 / 15)
        for s in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
            result = functional_equation_test(s, a, b, cc, N_theta=18)
            assert result['rel_err'] < 0.01

    def test_fe_free_boson(self):
        """Xi(s) = Xi(1-s) for Virasoro c=1."""
        a, b, cc, D = virasoro_form(1.0)
        for s in [0.3, 0.5, 0.7]:
            result = functional_equation_test(s, a, b, cc, N_theta=18)
            assert result['rel_err'] < 0.01

    def test_fe_symmetry_at_half(self):
        """Xi(1/2) is on the symmetry axis: Xi(s)=Xi(1-s) is trivial."""
        a, b, cc, D = virasoro_form(0.5)
        result = functional_equation_test(0.5, a, b, cc, N_theta=18)
        assert result['rel_err'] < 1e-10

    def test_fe_all_minimal_models(self):
        """FE holds for M(m,m+1) for m=3..8 at s=0.3 and s=0.7."""
        for m in range(3, 9):
            c = float(minimal_model_c(m))
            a, b, cc, D = virasoro_form(c)
            for s in [0.3, 0.7]:
                result = functional_equation_test(s, a, b, cc, N_theta=16)
                assert result['rel_err'] < 0.02, (
                    f"FE fails for M({m},{m+1}) at s={s}: "
                    f"rel_err={result['rel_err']}")


# ================================================================
# 5. Number-theoretic identification
# ================================================================

class TestNumberTheory:
    """Verify number-theoretic properties of the shadow discriminant."""

    def test_squarefree_part(self):
        assert squarefree_part(12) == 3
        assert squarefree_part(-12) == -3
        assert squarefree_part(1) == 1
        assert squarefree_part(7) == 7
        assert squarefree_part(18) == 2
        assert squarefree_part(-8640) == -15

    def test_fundamental_discriminant_check(self):
        assert _is_fundamental_discriminant(-3)
        assert _is_fundamental_discriminant(-4)
        assert _is_fundamental_discriminant(-7)
        assert _is_fundamental_discriminant(-8)
        assert _is_fundamental_discriminant(-40)
        assert not _is_fundamental_discriminant(-12)  # -12 = -3*4
        assert not _is_fundamental_discriminant(0)

    def test_fundamental_discriminant_decomposition(self):
        d, f = fundamental_discriminant(-12)
        assert d == -3 and f == 2

        d, f = fundamental_discriminant(-40)
        assert d == -40 and f == 1

        d, f = fundamental_discriminant(-529200)
        assert d == -3 and f == 420

    def test_class_number_small_known(self):
        assert class_number_small(-3) == 1
        assert class_number_small(-4) == 1
        assert class_number_small(-7) == 1
        assert class_number_small(-8) == 1
        assert class_number_small(-11) == 1
        assert class_number_small(-15) == 2
        assert class_number_small(-20) == 2
        assert class_number_small(-23) == 3
        assert class_number_small(-24) == 2
        assert class_number_small(-40) == 2

    def test_roots_of_unity(self):
        assert roots_of_unity(-3) == 6
        assert roots_of_unity(-4) == 4
        assert roots_of_unity(-7) == 2
        assert roots_of_unity(-40) == 2

    def test_ising_field(self):
        """Ising (c=1/2): Q(sqrt(-10)), fund disc = -40, h = 2."""
        fd = quadratic_field_from_disc(Fraction(1, 2))
        assert fd['squarefree'] == -10
        assert fd['fund_disc'] == -40
        assert fd['class_number'] == 2

    def test_m9_10_field(self):
        """M(9,10) (c=14/15): Q(sqrt(-3)), fund disc = -3, h = 1."""
        fd = quadratic_field_from_disc(Fraction(14, 15))
        assert fd['squarefree'] == -3
        assert fd['fund_disc'] == -3
        assert fd['class_number'] == 1
        assert fd['roots_of_unity'] == 6

    def test_free_boson_field(self):
        """c=1: Q(sqrt(-15)), fund disc = -15, h = 2."""
        fd = quadratic_field_from_disc(Fraction(1))
        assert fd['squarefree'] == -15
        assert fd['fund_disc'] == -15
        assert fd['class_number'] == 2

    def test_kronecker_symbol_basic(self):
        """Known values of Kronecker symbol."""
        # chi_{-4}: (n/4) for n odd
        assert kronecker_symbol(-4, 1) == 1
        assert kronecker_symbol(-4, 3) == -1
        assert kronecker_symbol(-4, 5) == 1
        assert kronecker_symbol(-4, 7) == -1
        assert kronecker_symbol(-4, 2) == 0

        # chi_{-3}: Legendre mod 3
        assert kronecker_symbol(-3, 1) == 1
        assert kronecker_symbol(-3, 2) == -1
        assert kronecker_symbol(-3, 3) == 0
        assert kronecker_symbol(-3, 4) == 1
        assert kronecker_symbol(-3, 5) == -1


# ================================================================
# 6. Specific central charge tests
# ================================================================

class TestSpecificCentralCharges:
    """Tests for specific physically important central charges."""

    def test_ising_discriminant(self):
        """c=1/2: disc = -160/49."""
        disc = virasoro_discriminant(Fraction(1, 2))
        assert disc == Fraction(-160, 49)

    def test_tricritical_ising_discriminant(self):
        """c=7/10: disc = -1568/255."""
        disc = virasoro_discriminant(Fraction(7, 10))
        assert disc == Fraction(-1568, 255)

    def test_potts_discriminant(self):
        """c=4/5: disc = -512/65."""
        disc = virasoro_discriminant(Fraction(4, 5))
        assert disc == Fraction(-512, 65)

    def test_m9_10_discriminant(self):
        """c=14/15: disc = -784/75."""
        disc = virasoro_discriminant(Fraction(14, 15))
        assert disc == Fraction(-784, 75)

    def test_self_dual_kappa(self):
        """c=13: kappa = 13/2."""
        data = virasoro_shadow_data(13.0)
        assert abs(data['kappa'] - 6.5) < 1e-10

    def test_self_dual_discriminant(self):
        """c=13: disc = -320*169/87 = -54080/87."""
        disc = virasoro_discriminant(Fraction(13))
        assert disc == Fraction(-320 * 169, 87)
        assert disc == Fraction(-54080, 87)

    def test_disc_negative_for_all_unitary(self):
        """disc < 0 for all c > 0 (positive definite form)."""
        for m in range(3, 30):
            c = minimal_model_c(m)
            disc = virasoro_discriminant(c)
            assert disc < 0, f"disc = {disc} not negative for m={m}"

    def test_disc_approaches_limit(self):
        """disc -> -320/27 as c -> 1 (m -> infinity)."""
        limit = Fraction(-320, 27)
        for m in [50, 100, 200]:
            c = minimal_model_c(m)
            disc = virasoro_discriminant(c)
            assert abs(float(disc) - float(limit)) < 0.1


# ================================================================
# 7. Dirichlet L-function tests
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestDirichletL:
    """Verify Dirichlet L-function implementation."""

    def test_L_chi_m4_at_2(self):
        """L(2, chi_{-4}) = Catalan's constant G = 0.9159..."""
        L2 = dirichlet_l_function(2.0, -4, n_terms=50000)
        # Catalan's constant
        G = float(mpmath.catalan)
        assert abs(L2 - G) / G < 0.001

    def test_L_chi_m3_at_1(self):
        """L(1, chi_{-3}) = pi/(3*sqrt(3)) via class number formula.

        h(-3)=1, w=6: L(1, chi_{-3}) = 2*pi*h/(w*sqrt(|d|)) = 2*pi/(6*sqrt(3))
        = pi/(3*sqrt(3)) = 0.6046..."""
        L1 = dirichlet_l_function(1.0, -3, n_terms=100000)
        expected = math.pi / (3 * math.sqrt(3))
        assert abs(L1 - expected) / expected < 0.01

    def test_L_chi_m4_at_1(self):
        """L(1, chi_{-4}) = pi/4 via class number formula.

        h(-4)=1, w=4: L(1, chi_{-4}) = 2*pi*h/(w*sqrt(|d|)) = 2*pi/(4*2)
        = pi/4 = 0.7854..."""
        L1 = dirichlet_l_function(1.0, -4, n_terms=100000)
        expected = math.pi / 4
        assert abs(L1 - expected) / expected < 0.01


# ================================================================
# 8. Cross-checks: Epstein vs Dedekind for known forms
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestEpsteinDedekind:
    """Cross-check Epstein zeta against Dedekind zeta for known forms."""

    def test_m2_n2_equals_4_zeta_K(self):
        """For m^2+n^2: E(s) = 4*zeta(s)*L(s, chi_{-4})."""
        for s in [2.0, 2.5, 3.0]:
            E = complex(epstein_zeta(s, 1, 0, 1, N_theta=20))
            zeta_K = dedekind_zeta(s, -4, n_terms=10000)
            ratio = abs(E / (4 * zeta_K))
            assert abs(ratio - 1) < 0.01, (
                f"E / (4*zeta_K) = {ratio} at s={s}")

    def test_m2_2n2_equals_w_zeta_K(self):
        """For m^2+2n^2 (disc=-8, h=1, w=2): E(s) = 2*zeta_K(s)."""
        for s in [2.0, 2.5, 3.0]:
            E = complex(epstein_zeta(s, 1, 0, 2, N_theta=20))
            zeta_K = dedekind_zeta(s, -8, n_terms=10000)
            ratio = abs(E / (2 * zeta_K))
            assert abs(ratio - 1) < 0.01, (
                f"E / (2*zeta_K) = {ratio} at s={s}")


# ================================================================
# 9. Theta function tests
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestThetaFunction:
    """Test theta function properties."""

    def test_theta_positive(self):
        """Theta function is positive for t > 0."""
        th = theta_binary_form(1.0, 1, 0, 1, N=10)
        assert float(th) > 0

    def test_theta_at_zero_limit(self):
        """Theta approaches (area)^{-1/2} * t^{-1} as t -> 0+."""
        # For Q=m^2+n^2: det(A) = 1, so theta(t) ~ 1/t for small t
        th_small = float(theta_binary_form(0.01, 1, 0, 1, N=30))
        assert th_small > 50  # Should be roughly 1/0.01 = 100

    def test_theta_exponential_decay(self):
        """Theta - 1 decays exponentially for large t."""
        th_large = float(theta_binary_form(10.0, 1, 0, 1, N=10))
        assert abs(th_large - 1) < 0.001  # very close to 1

    def test_theta_positive_definite_required(self):
        """Q must be positive definite for theta to be well-defined."""
        # This is automatic when disc < 0 and a > 0
        for m in range(3, 10):
            c = float(minimal_model_c(m))
            a, b, cc, D = virasoro_form(c)
            th = float(theta_binary_form(1.0, a, b, cc, N=10))
            assert th > 0


# ================================================================
# 10. Deeper L-function investigation
# ================================================================

class TestDeeperLFunction:
    """Test the ideal class analysis for minimal models."""

    def test_h1_exists(self):
        """At least one minimal model has h = 1."""
        investigation = deeper_l_function_investigation()
        assert investigation['h1_count'] >= 1

    def test_m9_10_is_h1(self):
        """M(9,10) has h = 1."""
        investigation = deeper_l_function_investigation()
        h1_ms = [m for m, d in investigation['h1_models']]
        assert 9 in h1_ms

    def test_ising_is_h2(self):
        """Ising (m=3) has h = 2."""
        investigation = deeper_l_function_investigation()
        h_gt_1 = {m: h for m, h, d in investigation['h_gt_1_models']}
        assert h_gt_1.get(3) == 2

    def test_class_numbers_positive(self):
        """All class numbers are positive integers."""
        investigation = deeper_l_function_investigation()
        for model in investigation['models']:
            h = model['class_number']
            if h is not None:
                assert isinstance(h, int) and h >= 1

    def test_h1_implies_dirichlet_l(self):
        """For h=1 models, the L-function is a Dirichlet L-function."""
        investigation = deeper_l_function_investigation()
        for m, d in investigation['h1_models']:
            assert _is_fundamental_discriminant(d), (
                f"Fund disc {d} for M({m},{m+1}) is not fundamental")
            assert class_number_small(d) == 1


# ================================================================
# 11. Scaled integer form tests
# ================================================================

class TestScaledForm:
    """Test the scaling to integer coefficients."""

    def test_ising_scaled_form(self):
        """Ising: scaled form has integer coefficients."""
        A, B, C, scale = scaled_integer_form(3)
        assert isinstance(A, int) and isinstance(B, int) and isinstance(C, int)
        # Verify discriminant
        D_int = B * B - 4 * A * C
        assert D_int < 0  # negative definite

    def test_scaled_disc_consistent(self):
        """Scaled discriminant = scale^2 * original discriminant."""
        for m in range(3, 10):
            c = minimal_model_c(m)
            disc_orig = virasoro_discriminant(c)
            A, B, C, scale = scaled_integer_form(m)
            D_int = B * B - 4 * A * C
            # D_int = scale^2 * disc(Q_orig)
            expected = int(scale ** 2 * disc_orig)
            assert D_int == expected, (
                f"Disc mismatch at m={m}: {D_int} vs {expected}")

    def test_m9_10_conductor(self):
        """M(9,10): conductor f = 420 for fund disc -3."""
        A, B, C, scale = scaled_integer_form(9)
        D_int = B * B - 4 * A * C
        d, f = fundamental_discriminant(D_int)
        assert d == -3
        assert f == 420


# ================================================================
# 12. Edge case and robustness tests
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestEdgeCases:
    """Test behavior at edge cases."""

    def test_fe_at_symmetry_point(self):
        """Xi(0.5) = Xi(0.5) trivially."""
        result = functional_equation_test(0.5, 1, 0, 1, N_theta=15)
        assert result['rel_err'] < 1e-10

    def test_epstein_pole_at_s1(self):
        """E(s) diverges as s -> 1."""
        # E(s) has a simple pole at s=1 with residue 2*pi/sqrt(|D|)
        # For m^2+n^2: residue = 2*pi/sqrt(4) = pi
        E_near = complex(epstein_zeta(1.01, 1, 0, 1, N_theta=15))
        assert abs(E_near) > 100  # Should be large near pole

    def test_large_c(self):
        """Shadow form at c=100."""
        a, b, cc, D = virasoro_form(100.0)
        assert D < 0  # Still negative definite
        disc = virasoro_discriminant(Fraction(100))
        assert disc < 0


# ================================================================
# 13. Comprehensive functional equation sweep
# ================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestFEComprehensive:
    """Comprehensive functional equation tests across many models."""

    @pytest.mark.parametrize("m", range(3, 9))
    def test_fe_minimal_model(self, m):
        """FE for M(m, m+1) at s = 0.3."""
        c = float(minimal_model_c(m))
        a, b, cc, D = virasoro_form(c)
        result = functional_equation_test(0.3, a, b, cc, N_theta=16)
        assert result['rel_err'] < 0.02, (
            f"FE fails for M({m},{m+1}): rel_err={result['rel_err']}")

    def test_fe_c_equals_2(self):
        """FE for Virasoro c=2 (betagamma)."""
        a, b, cc, D = virasoro_form(2.0)
        result = functional_equation_test(0.3, a, b, cc, N_theta=16)
        assert result['rel_err'] < 0.02

    def test_fe_c_equals_26(self):
        """FE for Virasoro c=26 (critical string)."""
        a, b, cc, D = virasoro_form(26.0)
        result = functional_equation_test(0.3, a, b, cc, N_theta=16)
        assert result['rel_err'] < 0.05  # Larger disc needs more theta terms
