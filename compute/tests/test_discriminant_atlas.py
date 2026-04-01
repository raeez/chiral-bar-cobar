"""Tests for the critical discriminant atlas.

Verifies:
  1. Critical discriminant Delta = 8*kappa*S_4 for all standard families
  2. Discriminant complementarity: Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]
  3. Self-dual point c = 13
  4. c = 0 limit (kappa -> 0 but Delta remains finite)
  5. Shadow class determination from Delta
  6. W_3 T-line and W-line discriminants
  7. Cross-checks against shadow_radius.py and quartic_contact_class.py
  8. Numerical stability
  9. Exact arithmetic via Fraction

Ground truth:
  - eq:discriminant-complementarity (higher_genus_modular_koszul.tex, line 15193)
  - thm:shadow-connection items (v)-(vi) (higher_genus_modular_koszul.tex)
  - thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

import sys
sys.path.insert(0, 'compute')

import pytest
from fractions import Fraction


# ============================================================================
# 1. Core discriminant formula
# ============================================================================

class TestCriticalDiscriminant:
    """Delta = 8 * kappa * S_4."""

    def test_discriminant_basic(self):
        from lib.discriminant_atlas import critical_discriminant
        assert critical_discriminant(Fraction(1), Fraction(1)) == Fraction(8)
        assert critical_discriminant(Fraction(3, 2), Fraction(0)) == Fraction(0)
        assert critical_discriminant(Fraction(0), Fraction(5)) == Fraction(0)

    def test_discriminant_linearity_in_kappa(self):
        from lib.discriminant_atlas import critical_discriminant
        S4 = Fraction(10, 27)
        for n in range(1, 6):
            assert (critical_discriminant(Fraction(n), S4) ==
                    n * critical_discriminant(Fraction(1), S4))

    def test_discriminant_linearity_in_S4(self):
        from lib.discriminant_atlas import critical_discriminant
        kappa = Fraction(5, 3)
        for n in range(1, 6):
            assert (critical_discriminant(kappa, Fraction(n)) ==
                    n * critical_discriminant(kappa, Fraction(1)))


# ============================================================================
# 2. Virasoro discriminant
# ============================================================================

class TestVirasoroDiscriminant:
    """Delta(Vir_c) = 40/(5c+22)."""

    def test_virasoro_Delta_formula(self):
        """Delta = 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)."""
        from lib.discriminant_atlas import virasoro_Delta, virasoro_kappa, virasoro_S4
        from lib.discriminant_atlas import critical_discriminant
        for c_val in [1, 2, 5, 7, 13, 25, 26]:
            c = Fraction(c_val)
            kappa = virasoro_kappa(c)
            S4 = virasoro_S4(c)
            Delta_direct = critical_discriminant(kappa, S4)
            Delta_formula = virasoro_Delta(c)
            assert Delta_direct == Delta_formula, \
                f"Mismatch at c={c_val}: {Delta_direct} != {Delta_formula}"

    def test_virasoro_Delta_closed_form(self):
        """Delta(c) = 40/(5c+22) at specific values."""
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(0) == Fraction(40, 22)
        assert virasoro_Delta(0) == Fraction(20, 11)
        assert virasoro_Delta(1) == Fraction(40, 27)
        assert virasoro_Delta(2) == Fraction(40, 32)
        assert virasoro_Delta(2) == Fraction(5, 4)
        assert virasoro_Delta(13) == Fraction(40, 87)
        assert virasoro_Delta(26) == Fraction(40, 152)
        assert virasoro_Delta(26) == Fraction(5, 19)

    def test_virasoro_Delta_positive_for_c_gt_minus_22_over_5(self):
        """Delta > 0 for c > -22/5 (the Lee-Yang pole)."""
        from lib.discriminant_atlas import virasoro_Delta
        for c_val in [1, 2, 5, 10, 13, 25, 26, 100]:
            assert virasoro_Delta(c_val) > 0

    def test_virasoro_Delta_c_cancellation(self):
        """The c in kappa = c/2 cancels the 1/c in S_4 = 10/[c(5c+22)].

        This makes Delta regular at c = 0.
        """
        from lib.discriminant_atlas import virasoro_Delta
        # Delta(0) = 40/(5*0+22) = 40/22 = 20/11
        assert virasoro_Delta(0) == Fraction(20, 11)

    def test_virasoro_kappa(self):
        from lib.discriminant_atlas import virasoro_kappa
        assert virasoro_kappa(0) == 0
        assert virasoro_kappa(1) == Fraction(1, 2)
        assert virasoro_kappa(13) == Fraction(13, 2)
        assert virasoro_kappa(26) == Fraction(13)

    def test_virasoro_S4(self):
        """S_4(Vir_c) = Q^contact = 10/[c(5c+22)]."""
        from lib.discriminant_atlas import virasoro_S4
        assert virasoro_S4(1) == Fraction(10, 27)
        assert virasoro_S4(2) == Fraction(10, 64)
        assert virasoro_S4(2) == Fraction(5, 32)
        # c=13: 10/(13*87) = 10/1131
        assert virasoro_S4(13) == Fraction(10, 13 * 87)

    def test_virasoro_alpha(self):
        from lib.discriminant_atlas import virasoro_alpha
        assert virasoro_alpha() == Fraction(2)


# ============================================================================
# 3. Discriminant complementarity
# ============================================================================

class TestDiscriminantComplementarity:
    """Delta(c) + Delta(26-c) = 6960/[(5c+22)(152-5c)]."""

    def test_complementarity_integer_c(self):
        """Verify at all integer c from -10 to 30 (skipping poles)."""
        from lib.discriminant_atlas import virasoro_complementarity
        for c_val in range(-10, 31):
            if 5 * c_val + 22 == 0 or 152 - 5 * c_val == 0:
                continue
            comp = virasoro_complementarity(c_val)
            assert comp['match'], f"Complementarity fails at c = {c_val}"

    def test_complementarity_half_integer_c(self):
        """Verify at half-integer c values."""
        from lib.discriminant_atlas import virasoro_complementarity
        for num in [1, 3, 5, 7, 9, 11, 15, 19, 23, 33, 43, 51]:
            c_val = Fraction(num, 2)
            if 5 * c_val + 22 == 0 or 152 - 5 * c_val == 0:
                continue
            comp = virasoro_complementarity(c_val)
            assert comp['match'], f"Complementarity fails at c = {c_val}"

    def test_complementarity_minimal_model_c(self):
        """Verify at unitary minimal model central charges c = 1 - 6/[m(m+1)]."""
        from lib.discriminant_atlas import virasoro_complementarity
        for m in range(3, 15):
            c_val = Fraction(1) - Fraction(6, m * (m + 1))
            comp = virasoro_complementarity(c_val)
            assert comp['match'], f"Complementarity fails at m = {m}, c = {c_val}"

    def test_complementarity_numerator_is_6960(self):
        """The numerator 6960 = 2^4 * 3 * 5 * 29 = 40 * 174."""
        assert 6960 == 2 ** 4 * 3 * 5 * 29
        assert 6960 == 40 * 174

    def test_complementarity_algebraic_derivation(self):
        """Direct algebraic verification of the complementarity formula.

        40/(5c+22) + 40/(152-5c)
        = 40*(152-5c+5c+22) / [(5c+22)(152-5c)]
        = 40*174 / [(5c+22)(152-5c)]
        = 6960 / [(5c+22)(152-5c)].
        """
        # The key algebraic identity: (152-5c) + (5c+22) = 174
        assert 152 + 22 == 174

    def test_complementarity_denominator_product(self):
        """Verify (5c+22)(152-5c) at specific values."""
        from lib.discriminant_atlas import virasoro_complementarity
        # c = 13: (5*13+22)(152-5*13) = 87*87 = 7569
        comp = virasoro_complementarity(13)
        assert comp['denominator'] == 7569
        assert comp['denominator'] == 87 ** 2

        # c = 0: (22)(152) = 3344
        comp = virasoro_complementarity(0)
        assert comp['denominator'] == 3344

    def test_complementarity_numerical(self):
        """Floating-point consistency check."""
        from lib.discriminant_atlas import virasoro_complementarity_float
        for c_val in [0.5, 1.0, 2.0, 5.5, 13.0, 25.0]:
            result = virasoro_complementarity_float(c_val)
            assert result['relative_error'] < 1e-14, \
                f"Numerical error at c={c_val}: {result['relative_error']}"


# ============================================================================
# 4. Self-dual point c = 13
# ============================================================================

class TestSelfDual:
    """At c = 13: Vir_13^! = Vir_13, so Delta(A) = Delta(A!)."""

    def test_self_dual_Delta_equality(self):
        from lib.discriminant_atlas import complementarity_at_self_dual
        sd = complementarity_at_self_dual()
        assert sd['self_dual']
        assert sd['Delta'] == sd['Delta_dual']

    def test_self_dual_Delta_value(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(13) == Fraction(40, 87)

    def test_self_dual_sum(self):
        from lib.discriminant_atlas import complementarity_at_self_dual
        sd = complementarity_at_self_dual()
        assert sd['sum'] == Fraction(80, 87)
        assert sd['match']

    def test_self_dual_kappa_value(self):
        """kappa(Vir_13) = 13/2."""
        from lib.discriminant_atlas import virasoro_kappa
        assert virasoro_kappa(13) == Fraction(13, 2)

    def test_self_dual_S4_value(self):
        """S_4(Vir_13) = 10/(13*87) = 10/1131."""
        from lib.discriminant_atlas import virasoro_S4
        assert virasoro_S4(13) == Fraction(10, 1131)

    def test_self_dual_S4_dual_equals_S4(self):
        """At c = 13: S_4(c) = S_4(26-c)."""
        from lib.discriminant_atlas import virasoro_S4
        assert virasoro_S4(13) == virasoro_S4(26 - 13)


# ============================================================================
# 5. c = 0 limit
# ============================================================================

class TestCZeroLimit:
    """Delta is regular at c = 0 despite kappa = 0 and S_4 having a pole."""

    def test_Delta_c0_is_regular(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(0) == Fraction(20, 11)

    def test_c0_complementarity(self):
        from lib.discriminant_atlas import complementarity_c0_limit
        lim = complementarity_c0_limit()
        assert lim['match']
        assert lim['Delta_c0'] == Fraction(20, 11)
        assert lim['Delta_c26'] == Fraction(5, 19)
        assert lim['sum'] == Fraction(435, 209)

    def test_c0_sum_reduces(self):
        """435/209 = 6960/3344: verify reduction."""
        assert Fraction(6960, 3344) == Fraction(435, 209)

    def test_c0_kappa_vanishes(self):
        from lib.discriminant_atlas import virasoro_kappa
        assert virasoro_kappa(0) == 0

    def test_c0_cancellation_mechanism(self):
        """kappa*S_4 = (c/2)*10/[c(5c+22)] = 5/(5c+22), regular at c=0."""
        from lib.discriminant_atlas import virasoro_kappa, virasoro_S4
        # At c=1: kappa*S4 = (1/2)*(10/27) = 5/27 = 5/(5+22)
        c = Fraction(1)
        product = virasoro_kappa(c) * virasoro_S4(c)
        assert product == Fraction(5, 27)
        assert product == Fraction(5, 5 * c + 22)


# ============================================================================
# 6. Shadow class determination
# ============================================================================

class TestShadowClassification:
    """Shadow depth classification from single-line discriminant."""

    def test_class_G_heisenberg(self):
        from lib.discriminant_atlas import classify_shadow_depth
        assert classify_shadow_depth(Fraction(1, 2), Fraction(0), Fraction(0)) == 'G'

    def test_class_L_affine(self):
        from lib.discriminant_atlas import classify_shadow_depth
        assert classify_shadow_depth(Fraction(3, 2), Fraction(1), Fraction(0)) == 'L'

    def test_class_M_virasoro(self):
        from lib.discriminant_atlas import classify_shadow_depth, virasoro_S4
        kappa = Fraction(1, 2)
        S4 = virasoro_S4(1)
        assert classify_shadow_depth(kappa, Fraction(2), S4) == 'M'

    def test_even_cascade_W3_W_line(self):
        """W_3 W-line: alpha = 0, S_4 != 0 -> even-only cascade."""
        from lib.discriminant_atlas import classify_shadow_depth, w3_W_line_data
        data = w3_W_line_data(2)
        result = classify_shadow_depth(data['kappa'], data['alpha'], data['S4'])
        assert result == 'even_cascade'

    def test_heisenberg_data(self):
        from lib.discriminant_atlas import heisenberg_data
        data = heisenberg_data(1)
        assert data['kappa'] == Fraction(1, 2)
        assert data['alpha'] == 0
        assert data['S4'] == 0
        assert data['Delta'] == 0
        assert data['class'] == 'G'

    def test_affine_sl2_data(self):
        from lib.discriminant_atlas import affine_sl2_data
        # k=1: kappa = 3*3/4 = 9/4
        data = affine_sl2_data(1)
        assert data['kappa'] == Fraction(9, 4)
        assert data['S4'] == 0
        assert data['Delta'] == 0
        assert data['class'] == 'L'

    def test_betagamma_data(self):
        from lib.discriminant_atlas import betagamma_data
        # lambda=1: kappa = 6-6+1 = 1
        data = betagamma_data(1)
        assert data['kappa'] == Fraction(1)
        assert data['S4'] == 0  # on weight-changing line
        assert data['Delta'] == 0  # on weight-changing line
        assert data['class'] == 'C'


# ============================================================================
# 7. Affine Kac-Moody: Delta = 0
# ============================================================================

class TestAffineDelta:
    """All affine KM algebras have Delta = 0 (class L)."""

    def test_sl2_Delta_zero(self):
        from lib.discriminant_atlas import affine_sl2_data
        for k in range(1, 10):
            data = affine_sl2_data(k)
            assert data['Delta'] == 0

    def test_slN_Delta_zero(self):
        from lib.discriminant_atlas import affine_slN_data
        for N in range(2, 8):
            for k in range(1, 5):
                data = affine_slN_data(N, k)
                assert data['Delta'] == 0

    def test_sl2_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        from lib.discriminant_atlas import affine_sl2_data
        assert affine_sl2_data(1)['kappa'] == Fraction(9, 4)
        assert affine_sl2_data(2)['kappa'] == Fraction(3)
        assert affine_sl2_data(10)['kappa'] == Fraction(9)

    def test_slN_kappa_formula(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N)."""
        from lib.discriminant_atlas import affine_slN_data
        # sl_3 at k=1: (9-1)*(1+3)/(2*3) = 8*4/6 = 32/6 = 16/3
        assert affine_slN_data(3, 1)['kappa'] == Fraction(16, 3)


# ============================================================================
# 8. Heisenberg: Delta = 0
# ============================================================================

class TestHeisenbergDelta:
    """Heisenberg has Delta = 0 (class G)."""

    def test_heisenberg_Delta_zero(self):
        from lib.discriminant_atlas import heisenberg_data
        for n in range(1, 10):
            data = heisenberg_data(n)
            assert data['Delta'] == 0

    def test_heisenberg_kappa(self):
        """kappa(H_n) = n/2."""
        from lib.discriminant_atlas import heisenberg_data
        assert heisenberg_data(1)['kappa'] == Fraction(1, 2)
        assert heisenberg_data(2)['kappa'] == Fraction(1)
        assert heisenberg_data(24)['kappa'] == Fraction(12)


# ============================================================================
# 9. Beta-gamma / bc systems
# ============================================================================

class TestBetaGamma:
    """Beta-gamma and bc systems: class C."""

    def test_betagamma_kappa_standard(self):
        """Standard betagamma (lambda=0 or 1): kappa = 1."""
        from lib.discriminant_atlas import betagamma_kappa
        assert betagamma_kappa(0) == Fraction(1)
        assert betagamma_kappa(1) == Fraction(1)

    def test_betagamma_kappa_symplectic(self):
        """Symplectic fermion (lambda=1/2): kappa = -1/2."""
        from lib.discriminant_atlas import betagamma_kappa
        assert betagamma_kappa(Fraction(1, 2)) == Fraction(-1, 2)

    def test_bc_kappa_opposite(self):
        """kappa(bc, j) = -kappa(betagamma, j)."""
        from lib.discriminant_atlas import betagamma_kappa, bc_kappa
        for lam in [0, Fraction(1, 2), 1, Fraction(3, 2), 2]:
            assert bc_kappa(lam) == -betagamma_kappa(lam)

    def test_bc_betagamma_complementarity(self):
        """kappa(bc) + kappa(bg) = 0 for all lambda."""
        from lib.discriminant_atlas import betagamma_kappa, bc_kappa
        for lam in [0, Fraction(1, 2), 1, Fraction(3, 2), 2, 3]:
            assert betagamma_kappa(lam) + bc_kappa(lam) == 0

    def test_betagamma_neutral_line_Delta_zero(self):
        from lib.discriminant_atlas import betagamma_data
        for lam in [0, Fraction(1, 2), 1, 2]:
            data = betagamma_data(lam)
            assert data['Delta'] == 0


# ============================================================================
# 10. W_3 discriminants
# ============================================================================

class TestW3Discriminant:
    """W_3 has two primary lines with different discriminants."""

    def test_T_line_equals_virasoro(self):
        """T-line: kappa_T = c/2, S4_T = 10/[c(5c+22)], Delta_T = 40/(5c+22)."""
        from lib.discriminant_atlas import w3_T_line_data, virasoro_Delta
        for c_val in [1, 2, 5, 13, 25]:
            T_data = w3_T_line_data(c_val)
            assert T_data['Delta'] == virasoro_Delta(c_val), \
                f"T-line != Virasoro at c={c_val}"

    def test_W_line_S4_formula(self):
        """S4_W = 2560/[c(5c+22)^3]."""
        from lib.discriminant_atlas import w3_W_line_data
        data = w3_W_line_data(2)
        expected = Fraction(2560, 2 * 32 ** 3)  # 2*(5*2+22)^3 = 2*32^3 = 65536
        assert data['S4'] == expected

    def test_W_line_Delta_closed_form(self):
        """Delta_W = 20480/[3(5c+22)^3]."""
        from lib.discriminant_atlas import w3_W_line_data, w3_W_line_Delta_formula
        for c_val in [1, 2, 3, 5, 7, 10, 13, 25]:
            data = w3_W_line_data(c_val)
            formula = w3_W_line_Delta_formula(c_val)
            assert data['Delta'] == formula, \
                f"W-line closed form fails at c={c_val}"

    def test_W_line_Delta_derivation(self):
        """Step-by-step: Delta_W = 8*(c/3)*2560/[c(5c+22)^3] = 20480/[3(5c+22)^3]."""
        from lib.discriminant_atlas import critical_discriminant
        c = Fraction(2)
        kappa_W = c / 3
        S4_W = Fraction(2560) / (c * (5 * c + 22) ** 3)
        Delta = critical_discriminant(kappa_W, S4_W)
        # 8*(2/3)*2560/(2*32^3) = 8*2*2560/(3*2*32^3) = 8*2560/(3*32^3)
        # = 20480/(3*32768) = 20480/98304 = 5/24
        assert Delta == Fraction(5, 24)
        # Closed form: 20480/(3*(5*2+22)^3) = 20480/(3*32^3) = 20480/98304 = 5/24
        assert Delta == Fraction(20480, 3 * 32 ** 3)

    def test_W_line_ratio_to_T_line(self):
        """Delta_W / Delta_T = 512/[3(5c+22)^2]."""
        from lib.discriminant_atlas import w3_discriminant_comparison
        comp = w3_discriminant_comparison(2)
        # ratio = (20480/[3*32^3]) / (40/32) = 20480/(3*32^3) * 32/40
        # = 20480*32/(3*40*32^3) = 20480/(3*40*32^2) = 512/(3*1024) = 1/6
        assert comp['ratio'] == Fraction(1, 6)

    def test_W_line_ratio_c13(self):
        """At c=13: ratio = 512/(3*87^2) = 512/22707."""
        from lib.discriminant_atlas import w3_discriminant_comparison
        comp = w3_discriminant_comparison(13)
        expected = Fraction(512, 3 * 87 ** 2)
        assert comp['ratio'] == expected

    def test_W_line_alpha_zero(self):
        """W-line has alpha = 0 (Z_2 parity forces odd vanishing)."""
        from lib.discriminant_atlas import w3_W_line_data
        for c_val in [1, 2, 13]:
            data = w3_W_line_data(c_val)
            assert data['alpha'] == 0

    def test_W_line_kappa(self):
        """kappa_W = c/3."""
        from lib.discriminant_atlas import w3_W_line_data
        data = w3_W_line_data(6)
        assert data['kappa'] == Fraction(2)

    def test_total_kappa_w3(self):
        """kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        from lib.discriminant_atlas import w3_total_kappa
        assert w3_total_kappa(6) == Fraction(5)
        assert w3_total_kappa(12) == Fraction(10)
        assert w3_total_kappa(Fraction(3, 5)) == Fraction(1, 2)

    def test_W_line_much_smaller_than_T_line(self):
        """At large c, Delta_W << Delta_T (W-line suppressed by (5c+22)^2)."""
        from lib.discriminant_atlas import w3_discriminant_comparison
        comp = w3_discriminant_comparison(100)
        assert comp['Delta_W'] < comp['Delta_T'] / 100


# ============================================================================
# 11. Shadow metric Q_L(t)
# ============================================================================

class TestShadowMetric:
    """Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""

    def test_Q_at_t0(self):
        """Q_L(0) = 4*kappa^2."""
        from lib.discriminant_atlas import shadow_metric_Q
        kappa = Fraction(5, 2)
        assert shadow_metric_Q(kappa, Fraction(2), Fraction(1), Fraction(0)) == 4 * kappa ** 2

    def test_Q_gaussian_decomposition(self):
        """Q_L = (2kappa + 3alpha*t)^2 + 2*Delta*t^2.

        When Delta = 0: Q_L is a perfect square.
        """
        from lib.discriminant_atlas import shadow_metric_Q, critical_discriminant
        kappa = Fraction(3)
        alpha = Fraction(2)
        S4 = Fraction(0)  # Delta = 0
        for t_val in [-1, 0, 1, 2, 5]:
            t = Fraction(t_val)
            Q = shadow_metric_Q(kappa, alpha, S4, t)
            perfect_sq = (2 * kappa + 3 * alpha * t) ** 2
            assert Q == perfect_sq

    def test_Q_coefficients_virasoro(self):
        """Q_Vir(t) has coefficients: q0=c^2, q1=12c, q2=(180c+872)/(5c+22)."""
        from lib.discriminant_atlas import virasoro_shadow_metric_coefficients
        q0, q1, q2 = virasoro_shadow_metric_coefficients(1)
        assert q0 == Fraction(1)      # 1^2
        assert q1 == Fraction(12)     # 12*1
        # q2 = (180+872)/(5+22) = 1052/27
        assert q2 == Fraction(1052, 27)

    def test_Q_polynomial_discriminant(self):
        """disc(Q_L) = -32*kappa^2*Delta."""
        from lib.discriminant_atlas import shadow_metric_polynomial_discriminant
        from lib.discriminant_atlas import critical_discriminant
        kappa = Fraction(3, 2)
        S4 = Fraction(5, 7)
        Delta = critical_discriminant(kappa, S4)
        disc = shadow_metric_polynomial_discriminant(kappa, Fraction(1), S4)
        assert disc == -32 * kappa ** 2 * Delta


# ============================================================================
# 12. Complete atlas
# ============================================================================

class TestCompleteAtlas:
    """The full discriminant_atlas() function."""

    def test_atlas_has_all_families(self):
        from lib.discriminant_atlas import discriminant_atlas
        atlas = discriminant_atlas()
        assert 'Heisenberg_1' in atlas
        assert 'Affine_sl2_k1' in atlas
        assert 'BetaGamma_lam1' in atlas
        assert 'Vir_13' in atlas
        assert 'W3_T_c2' in atlas
        assert 'W3_W_c2' in atlas

    def test_atlas_class_G_entries(self):
        from lib.discriminant_atlas import discriminant_atlas
        atlas = discriminant_atlas()
        assert atlas['Heisenberg_1']['class'] == 'G'
        assert atlas['Heisenberg_1']['Delta'] == 0

    def test_atlas_class_L_entries(self):
        from lib.discriminant_atlas import discriminant_atlas
        atlas = discriminant_atlas()
        assert atlas['Affine_sl2_k1']['class'] == 'L'
        assert atlas['Affine_sl2_k1']['Delta'] == 0

    def test_atlas_class_C_entries(self):
        from lib.discriminant_atlas import discriminant_atlas
        atlas = discriminant_atlas()
        assert atlas['BetaGamma_lam1']['class'] == 'C'

    def test_atlas_class_M_entries(self):
        from lib.discriminant_atlas import discriminant_atlas
        atlas = discriminant_atlas()
        assert atlas['Vir_13']['class'] == 'M'
        assert atlas['Vir_13']['Delta'] > 0


# ============================================================================
# 13. Cross-checks with other modules
# ============================================================================

class TestCrossChecks:
    """Cross-check discriminant_atlas against shadow_radius and quartic_contact_class."""

    def test_delta_matches_shadow_radius(self):
        """Delta from discriminant_atlas matches shadow_radius.critical_discriminant."""
        from lib.discriminant_atlas import virasoro_Delta
        from lib.shadow_radius import critical_discriminant as sr_critical_discriminant
        from sympy import Rational as SR, Symbol, simplify
        c = Symbol('c')
        kappa = c / 2
        S4 = SR(10) / (c * (5 * c + 22))
        Delta_sr = sr_critical_discriminant(kappa, S4)
        # Evaluate at specific values and compare
        for c_val in [1, 2, 5, 13, 25]:
            val_sr = float(Delta_sr.subs(c, c_val))
            val_da = float(virasoro_Delta(c_val))
            assert abs(val_sr - val_da) < 1e-14, \
                f"shadow_radius vs discriminant_atlas mismatch at c={c_val}"

    def test_S4_matches_quartic_contact_class(self):
        """S_4 from discriminant_atlas matches quartic_contact_class.Q_contact_virasoro."""
        from lib.discriminant_atlas import virasoro_S4
        from lib.quartic_contact_class import Q_contact_virasoro
        for c_val in [1, 2, 5, 13, 25, 26]:
            da_val = virasoro_S4(c_val)
            qcc_val = Q_contact_virasoro(c_val)
            assert da_val == qcc_val, \
                f"S4 mismatch at c={c_val}: {da_val} != {qcc_val}"

    def test_kappa_matches_quartic_contact_class(self):
        """kappa from discriminant_atlas matches quartic_contact_class.kappa_virasoro."""
        from lib.discriminant_atlas import virasoro_kappa
        from lib.quartic_contact_class import kappa_virasoro
        for c_val in [1, 2, 13, 26]:
            assert virasoro_kappa(c_val) == kappa_virasoro(c_val)

    def test_betagamma_kappa_matches_census(self):
        """kappa(betagamma) matches shadow_metric_census."""
        from lib.discriminant_atlas import betagamma_kappa
        from lib.shadow_metric_census import kappa_betagamma
        from sympy import Rational as SR
        for lam in [0, 1, 2]:
            da_val = betagamma_kappa(Fraction(lam))
            census_val = kappa_betagamma(SR(lam))
            assert int(da_val) == int(census_val), \
                f"betagamma kappa mismatch at lam={lam}"

    def test_w3_S4_matches_w3_engine(self):
        """W_3 S_4 values match w3_shadow_tower_engine."""
        from lib.discriminant_atlas import w3_T_line_data, w3_W_line_data
        from lib.w3_shadow_tower_engine import ds_quartic_creation
        from sympy import Rational as SR, Symbol
        c = Symbol('c')
        ds = ds_quartic_creation()
        # T-line S4
        T_data = w3_T_line_data(2)
        T_S4_engine = ds['S4_W3_T'].subs(c, 2)
        assert float(T_data['S4']) == pytest.approx(float(T_S4_engine), rel=1e-14)
        # W-line S4
        W_data = w3_W_line_data(2)
        W_S4_engine = ds['S4_W3_W'].subs(c, 2)
        assert float(W_data['S4']) == pytest.approx(float(W_S4_engine), rel=1e-14)


# ============================================================================
# 14. Edge cases and poles
# ============================================================================

class TestEdgeCases:
    """Behavior near poles and special values."""

    def test_lee_yang_poles(self):
        """Delta has poles at c = -22/5 and c = 152/5 (dual Lee-Yang)."""
        from lib.discriminant_atlas import virasoro_Delta, virasoro_Delta_dual
        # c = -22/5: 5c+22 = 0 (Delta pole)
        with pytest.raises(ZeroDivisionError):
            virasoro_Delta(Fraction(-22, 5))

        # c = 152/5: 152-5c = 0 (dual Delta pole)
        with pytest.raises(ZeroDivisionError):
            virasoro_Delta_dual(Fraction(152, 5))

    def test_dual_lee_yang_sum_26(self):
        """The two Lee-Yang poles sum to 26: -22/5 + 152/5 = 130/5 = 26."""
        assert Fraction(-22, 5) + Fraction(152, 5) == Fraction(26)

    def test_virasoro_c_negative(self):
        """Delta is defined for c < 0 (away from c = -22/5)."""
        from lib.discriminant_atlas import virasoro_Delta
        # c = -1: Delta = 40/(5*(-1)+22) = 40/17
        assert virasoro_Delta(-1) == Fraction(40, 17)

    def test_virasoro_large_c(self):
        """For large c: Delta ~ 8/c, S_4 ~ 2/(5c^2), kappa ~ c/2."""
        from lib.discriminant_atlas import virasoro_Delta
        # Delta(1000) = 40/(5*1000+22) = 40/5022
        assert virasoro_Delta(1000) == Fraction(40, 5022)
        assert virasoro_Delta(1000) == Fraction(20, 2511)


# ============================================================================
# 15. Specific numerical values (regression)
# ============================================================================

class TestRegressionValues:
    """Exact values for regression testing."""

    def test_vir_c1_Delta(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(1) == Fraction(40, 27)

    def test_vir_c2_Delta(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(2) == Fraction(5, 4)

    def test_vir_c13_Delta(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(13) == Fraction(40, 87)

    def test_vir_c25_Delta(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(25) == Fraction(40, 147)

    def test_vir_c26_Delta(self):
        from lib.discriminant_atlas import virasoro_Delta
        assert virasoro_Delta(26) == Fraction(5, 19)

    def test_w3_w_line_c2_Delta(self):
        from lib.discriminant_atlas import w3_W_line_data
        data = w3_W_line_data(2)
        assert data['Delta'] == Fraction(5, 24)

    def test_w3_w_line_c13_Delta(self):
        from lib.discriminant_atlas import w3_W_line_data
        data = w3_W_line_data(13)
        # 20480/(3*87^3) = 20480/1975308 = ...
        expected = Fraction(20480, 3 * 87 ** 3)
        assert data['Delta'] == expected

    def test_complementarity_c1(self):
        from lib.discriminant_atlas import virasoro_complementarity
        comp = virasoro_complementarity(1)
        # 40/27 + 40/147 = 40*(147+27)/(27*147) = 40*174/3969 = 6960/3969
        assert comp['sum'] == Fraction(6960, 3969)
        assert comp['sum'] == Fraction(2320, 1323)

    def test_complementarity_c2(self):
        from lib.discriminant_atlas import virasoro_complementarity
        comp = virasoro_complementarity(2)
        # Delta(2) = 40/32 = 5/4
        # Delta(24) = 40/(120+22) = 40/142 = 20/71
        # sum = 5/4 + 20/71 = (355+80)/284 = 435/284
        assert comp['Delta_A'] == Fraction(5, 4)
        assert comp['Delta_dual'] == Fraction(20, 71)
        assert comp['sum'] == Fraction(435, 284)
        # 6960/(32*142) = 6960/4544 = 435/284
        assert comp['predicted'] == Fraction(435, 284)


# ============================================================================
# 16. Additivity / independence properties
# ============================================================================

class TestAdditivity:
    """Delta = 8*kappa*S_4 is bilinear in kappa and S_4."""

    def test_Delta_scales_with_kappa(self):
        """Scaling kappa by lambda scales Delta by lambda."""
        from lib.discriminant_atlas import critical_discriminant
        S4 = Fraction(3, 7)
        for lam in [2, 3, 5, Fraction(1, 2)]:
            assert (critical_discriminant(lam * Fraction(1), S4) ==
                    lam * critical_discriminant(Fraction(1), S4))

    def test_w3_total_kappa_is_additive(self):
        """kappa(W_3) = kappa_T + kappa_W (direct-sum decomposition)."""
        from lib.discriminant_atlas import w3_T_line_data, w3_W_line_data, w3_total_kappa
        for c_val in [1, 2, 5, 13]:
            T = w3_T_line_data(c_val)
            W = w3_W_line_data(c_val)
            total = w3_total_kappa(c_val)
            assert T['kappa'] + W['kappa'] == total
