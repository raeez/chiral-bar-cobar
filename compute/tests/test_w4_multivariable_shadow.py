"""Tests for W_4 multi-variable shadow tower (3-generator).

Ground truth from manuscript:
  kappa = diag(c/2, c/3, c/4)                    [comp:w4-kappa]
  kappa_scalar = 13c/12                           [tr(kappa)]
  propagator = diag(2/c, 3/c, 4/c)               [kappa^{-1}]
  dim(QP_4) = 2: {Lambda, W_4}                   [w4-weight4-quasi-primaries]
  N_Lambda = c(5c+22)/10                          [BPZ norm]
  N_{W_4} = c/4                                   [kappa_{44}]
  Sh_3 = 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2      [gravitational cubic]
        + c334 x_4 x_3^2                          [non-gravitational cubic]
  Q_TTTT = 10/[c(5c+22)]                          [same as Virasoro/W_3]
  Q_T4T4 = 64/c                                   [W_4-only, NO (5c+22)]
  Q_3333 has both Lambda and W_4 terms            [two-channel exchange]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from sympy import (
    Symbol, Rational, simplify, factor, expand, S, diff,
    Poly, numer, denom, degree, Matrix
)

from lib.w4_multivariable_shadow import (
    w4_kappa,
    w4_propagator,
    w4_kappa_scalar,
    w4_weight4_quasi_primaries,
    w4_cubic,
    w4_quartic,
    w4_quartic_structure,
    w4_shadow_tower,
    w4_autonomy_checks,
    w4_denominator_analysis,
)

c = Symbol('c')
c334 = Symbol('c334')
c444 = Symbol('c444')
alpha_44 = Symbol('alpha_44')
x_T = Symbol('x_T')
x_3 = Symbol('x_3')
x_4 = Symbol('x_4')


# ===========================================================================
# TestKappa (K1-K5)
# ===========================================================================

class TestKappa:
    """Kappa matrix, scalar, and propagator for W_4."""

    def test_K1_kappa_diagonal_entries(self):
        """kappa = diag(c/2, c/3, c/4)."""
        K = w4_kappa()
        assert simplify(K[0, 0] - c/2) == 0
        assert simplify(K[1, 1] - c/3) == 0
        assert simplify(K[2, 2] - c/4) == 0

    def test_K2_kappa_off_diagonal_zero(self):
        """kappa is diagonal (generators orthogonal)."""
        K = w4_kappa()
        assert K[0, 1] == 0
        assert K[0, 2] == 0
        assert K[1, 2] == 0

    def test_K3_kappa_scalar(self):
        """tr(kappa) = c/2 + c/3 + c/4 = 13c/12."""
        expected = Rational(13) * c / 12
        assert simplify(w4_kappa_scalar() - expected) == 0

    def test_K4_propagator_diagonal(self):
        """Propagator = kappa^{-1} = diag(2/c, 3/c, 4/c)."""
        P = w4_propagator()
        assert simplify(P[0, 0] - 2/c) == 0
        assert simplify(P[1, 1] - 3/c) == 0
        assert simplify(P[2, 2] - 4/c) == 0

    def test_K5_propagator_inverts_kappa(self):
        """kappa * kappa^{-1} = I_3."""
        K = w4_kappa()
        P = w4_propagator()
        prod = K * P
        I3 = Matrix.eye(3)
        for i in range(3):
            for j in range(3):
                assert simplify(prod[i, j] - I3[i, j]) == 0


# ===========================================================================
# TestQuasiPrimaries (QP1-QP5)
# ===========================================================================

class TestQuasiPrimaries:
    """Weight-4 quasi-primary spectrum in W_4."""

    def test_QP1_dimension(self):
        """Two quasi-primaries at weight 4: Lambda and W_4."""
        qp = w4_weight4_quasi_primaries()
        assert qp['dim'] == 2

    def test_QP2_basis_labels(self):
        """Basis is {Lambda, W_4}."""
        qp = w4_weight4_quasi_primaries()
        assert 'Lambda' in qp['basis']
        assert 'W_4' in qp['basis']

    def test_QP3_lambda_norm(self):
        """N_Lambda = c(5c+22)/10."""
        qp = w4_weight4_quasi_primaries()
        expected = c * (5*c + 22) / 10
        assert simplify(qp['norms']['Lambda'] - expected) == 0

    def test_QP4_w4_norm(self):
        """N_{W_4} = c/4 (equals kappa_{44})."""
        qp = w4_weight4_quasi_primaries()
        expected = c / 4
        assert simplify(qp['norms']['W_4'] - expected) == 0

    def test_QP5_orthogonality(self):
        """Lambda and W_4 are orthogonal (different sectors)."""
        qp = w4_weight4_quasi_primaries()
        assert qp['orthogonal'] is True


# ===========================================================================
# TestCubic (C1-C6)
# ===========================================================================

class TestCubic:
    """Cubic shadow for W_4."""

    def test_C1_gravitational_cubic(self):
        """Gravitational part: 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2."""
        sh3 = w4_cubic()
        # Set c334=0 to isolate gravitational part
        grav = expand(sh3.subs(c334, 0))
        expected = expand(2*x_T**3 + 3*x_T*x_3**2 + 4*x_T*x_4**2)
        assert simplify(grav - expected) == 0

    def test_C2_nongravitational_c334_present(self):
        """Non-gravitational c334 term is present."""
        sh3 = w4_cubic()
        # The coefficient of x_4*x_3^2 should contain c334
        coeff = Poly(sh3, x_T, x_3, x_4).nth(0, 2, 1)
        assert coeff != 0
        assert c334 in coeff.free_symbols

    def test_C3_charge_conservation_even_x3(self):
        """W-charge conservation: all terms have even x_3 power."""
        sh3 = w4_cubic()
        p = Poly(sh3, x_T, x_3, x_4)
        for monom, coeff in p.as_dict().items():
            x3_power = monom[1]
            assert x3_power % 2 == 0, f"Monomial {monom} has odd x_3 power {x3_power}"

    def test_C4_no_x3_x4_squared(self):
        """No x_3 x_4^2 term (vanishes by weight mismatch)."""
        sh3 = w4_cubic()
        p = Poly(sh3, x_T, x_3, x_4)
        # x_3 x_4^2 has exponents (0, 1, 2)
        coeff_0_1_2 = p.nth(0, 1, 2)
        assert coeff_0_1_2 == 0

    def test_C5_gravitational_coefficients_match_weight(self):
        """Gravitational cubic: coefficient of x_T x_j^2 = h_j (conformal weight)."""
        sh3 = w4_cubic()
        grav = expand(sh3.subs(c334, 0))
        p = Poly(grav, x_T, x_3, x_4)
        # x_T^3 coefficient: h_T = 2
        assert p.nth(3, 0, 0) == 2
        # x_T x_3^2 coefficient: h_3 = 3
        assert p.nth(1, 2, 0) == 3
        # x_T x_4^2 coefficient: h_4 = 4
        assert p.nth(1, 0, 2) == 4

    def test_C6_full_cubic_form(self):
        """Full cubic: 2x_T^3 + 3x_T x_3^2 + 4x_T x_4^2 + c334*x_4*x_3^2."""
        sh3 = w4_cubic()
        expected = 2*x_T**3 + 3*x_T*x_3**2 + 4*x_T*x_4**2 + c334*x_4*x_3**2
        assert simplify(expand(sh3) - expand(expected)) == 0


# ===========================================================================
# TestQuartic (Q1-Q7)
# ===========================================================================

class TestQuartic:
    """Quartic shadow from two-channel exchange."""

    def test_Q1_TTTT_matches_virasoro(self):
        """Q_TTTT = 10/[c(5c+22)] — same as Virasoro and W_3."""
        q = w4_quartic()
        expected = Rational(10) / (c * (5*c + 22))
        assert simplify(q['Q_TTTT'] - expected) == 0

    def test_Q2_T4T4_no_5c22(self):
        """Q_T4T4 = 64/c — W_4-only channel, NO (5c+22)."""
        q = w4_quartic()
        expected = Rational(64) / c
        assert simplify(q['Q_T4T4'] - expected) == 0

    def test_Q3_T4T4_denominator_only_c(self):
        """Q_T4T4 denominator is c alone (no (5c+22) factor)."""
        q = w4_quartic()
        Q_T4T4 = q['Q_T4T4']
        d = denom(Q_T4T4)
        # denominator should be c, not c*(5c+22)
        assert simplify(d - c) == 0

    def test_Q4_3333_has_both_channels(self):
        """Q_3333 has both Lambda and W_4 terms."""
        q = w4_quartic()
        Q_3333 = q['Q_3333']
        # Should contain c334 (from W_4 channel)
        assert c334 in Q_3333.free_symbols
        # Should also have a c-only term from Lambda channel (alpha_33^2/N_Lambda)
        # Set c334=0: only Lambda channel survives
        Q_3333_lambda_only = simplify(Q_3333.subs(c334, 0))
        expected_lambda = Rational(16)**2 / ((5*c+22)**2 * c * (5*c+22) / 10)
        expected_lambda = simplify(Rational(10) * Rational(256) / (c * (5*c+22)**3))
        assert simplify(Q_3333_lambda_only - expected_lambda) == 0

    def test_Q5_uniform_filtration_broken(self):
        """Uniform denominator filtration from W_3 is broken."""
        s = w4_quartic_structure()
        assert s['uniform_filtration_broken'] is True

    def test_Q6_TTTT_pure_lambda(self):
        """Q_TTTT comes entirely from Lambda exchange (no W_4 contribution)."""
        q = w4_quartic()
        Q_TTTT = q['Q_TTTT']
        # Should have no c334, c444, alpha_44, C_34_W dependence
        assert c334 not in Q_TTTT.free_symbols
        assert c444 not in Q_TTTT.free_symbols

    def test_Q7_quartic_channel_count(self):
        """Seven distinct quartic channels computed."""
        q = w4_quartic()
        expected_keys = ['Q_TTTT', 'Q_TT33', 'Q_TT44', 'Q_T4T4',
                         'Q_3333', 'Q_3344', 'Q_4444']
        for key in expected_keys:
            assert key in q, f"Missing channel {key}"


# ===========================================================================
# TestAutonomy (A1-A4)
# ===========================================================================

class TestAutonomy:
    """Shadow subalgebra autonomy checks."""

    def test_A1_T_line_virasoro_cubic(self):
        """T-line (x_3=x_4=0) cubic gives 2x_T^3 (Virasoro cubic)."""
        checks = w4_autonomy_checks()
        sh3_T = checks['Sh_3_T_line']
        assert simplify(sh3_T - 2*x_T**3) == 0

    def test_A2_T_line_virasoro_quartic(self):
        """T-line quartic gives Virasoro Sh_4 = Q_TTTT * x_T^4."""
        checks = w4_autonomy_checks()
        sh4_T = checks['Sh_4_T_line']
        Q_TTTT = Rational(10) / (c * (5*c + 22))
        expected = expand(Q_TTTT * x_T**4)
        assert simplify(sh4_T - expected) == 0

    def test_A3_W3_plane_extra_c334_term(self):
        """W_3-plane (x_4=0) quartic does NOT match standalone W_3.

        The extra c334^2 term from the W_4-exchange channel
        persists even when x_4=0, because the Q_3333 channel
        has a c334^2/c term absent in standalone W_3.
        """
        checks = w4_autonomy_checks()
        sh4_W3 = checks['Sh_4_W3_plane']
        # On x_4=0: the quartic has x_T^4 and x_T^2 x_3^2 and x_3^4 terms.
        # The x_3^4 coefficient includes c334^2 * 4/c from the W_4 exchange.
        p = Poly(sh4_W3, x_T, x_3)
        coeff_x3_4 = p.nth(0, 4)
        # This should contain c334 (unlike standalone W_3 which has no c334)
        assert c334 in coeff_x3_4.free_symbols

    def test_A4_W4_plane_two_generator(self):
        """W_4-plane (x_3=0) gives a 2-generator system (T, W_4)."""
        checks = w4_autonomy_checks()
        sh3_W4 = checks['Sh_3_W4_plane']
        # Should be 2x_T^3 + 4x_T x_4^2 (no x_3 terms)
        expected = expand(2*x_T**3 + 4*x_T*x_4**2)
        assert simplify(sh3_W4 - expected) == 0


# ===========================================================================
# TestDenominator (D1-D4)
# ===========================================================================

class TestDenominator:
    """Denominator structure and Lee-Yang regularity."""

    def test_D1_lambda_channels_have_5c22(self):
        """Lambda-only channels have (5c+22) in denominator."""
        da = w4_denominator_analysis()
        Q_TTTT = da['Q_TTTT']
        d = denom(Q_TTTT)
        # denominator = c*(5c+22)
        p = Poly(d, c)
        # Should be degree 2 with factor (5c+22)
        assert simplify(d.subs(c, Rational(-22, 5))) == 0

    def test_D2_w4_channels_no_5c22(self):
        """W_4-only channel has only c in denominator."""
        da = w4_denominator_analysis()
        assert da['W4_channel_poles'] == [0]

    def test_D3_lee_yang_regularity_Q_T4T4(self):
        """Q_T4T4 is regular at c = -22/5 (Lee-Yang)."""
        q = w4_quartic()
        Q_T4T4 = q['Q_T4T4']
        val = Q_T4T4.subs(c, Rational(-22, 5))
        # Should be finite (= 64/(-22/5) = -320/22 = -160/11)
        expected = Rational(64) / Rational(-22, 5)
        assert simplify(val - expected) == 0

    def test_D4_lambda_poles(self):
        """Lambda channel poles are at c=0 and c=-22/5."""
        da = w4_denominator_analysis()
        assert 0 in da['Lambda_channel_poles']
        assert Rational(-22, 5) in da['Lambda_channel_poles']


# ===========================================================================
# TestStructure (S1-S3)
# ===========================================================================

class TestStructure:
    """Channel classification: Lambda-only, W_4-only, both."""

    def test_S1_lambda_only_channels(self):
        """Lambda-only channels: Q_TTTT, Q_TT33, Q_TT44."""
        s = w4_quartic_structure()
        assert s['Lambda_only'] == ['Q_TTTT', 'Q_TT33', 'Q_TT44']

    def test_S2_w4_only_channels(self):
        """W_4-only channels: Q_T4T4."""
        s = w4_quartic_structure()
        assert s['W4_only'] == ['Q_T4T4']

    def test_S3_both_channels(self):
        """Both-channel: Q_3333, Q_3344, Q_4444."""
        s = w4_quartic_structure()
        assert s['both'] == ['Q_3333', 'Q_3344', 'Q_4444']
