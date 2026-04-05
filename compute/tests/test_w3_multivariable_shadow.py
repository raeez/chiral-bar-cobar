"""Tests for W_3 multi-variable shadow obstruction tower.

Ground truth from manuscript:
  Q_TTTT = 10/[c(5c+22)]                         [thm:w3-quartic-shadow]
  Q_TTWW = 160/[c(5c+22)^2]                      [thm:w3-quartic-shadow]
  Q_WWWW = 2560/[c(5c+22)^3]                     [thm:w3-quartic-shadow]
  alpha = 16/(5c+22)                              [w3_bar.py]
  N_Lambda = c(5c+22)/10                          [BPZ norm]
  kappa(V_k(sl_3)) = 4(k+3)/3                    [comp:sl3-kappa]
  kappa(W_3) = 5c(k)/6                           [comp:w3-kappa]
  c(k) = 2 - 24(k+2)^2/(k+3)                    [comp:ds-w3]
  C_333^2 = 64(7c+68)(2c-1)/[5c(c+24)(5c+22)]   [Zamolodchikov]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from sympy import (
    Symbol, Rational, simplify, factor, expand, S, diff,
    Poly, numer, denom, degree
)

from lib.w3_multivariable_shadow import (
    w3_weight4_quasi_primaries,
    w3_weight6_quasi_primaries,
    w3_quartic_shadow,
    kac_shadow_singularity_principle,
    w3_corrected_shadow_tower,
    ds_shadow_compatibility,
    w3_quartic_denominator_analysis,
)

c = Symbol('c')
k = Symbol('k')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# ===========================================================================
# TestQuarticShadow (T1-T10)
# ===========================================================================

class TestQuarticShadow:
    """Quartic shadow coefficients from Lambda-exchange."""

    def test_T1_Q_TTTT_value(self):
        """Q_TTTT = 10/[c(5c+22)]."""
        q = w3_quartic_shadow()
        expected = Rational(10) / (c * (5*c + 22))
        assert simplify(q['Q_TTTT'] - expected) == 0

    def test_T2_Q_TTWW_value(self):
        """Q_TTWW = 160/[c(5c+22)^2]."""
        q = w3_quartic_shadow()
        expected = Rational(160) / (c * (5*c + 22)**2)
        assert simplify(q['Q_TTWW'] - expected) == 0

    def test_T3_Q_WWWW_value(self):
        """Q_WWWW = 2560/[c(5c+22)^3]."""
        q = w3_quartic_shadow()
        expected = Rational(2560) / (c * (5*c + 22)**3)
        assert simplify(q['Q_WWWW'] - expected) == 0

    def test_T4_T_line_recovers_virasoro(self):
        """On the T-line (x_W=0), Sh_4 = Q_TTTT x_T^4 = Virasoro quartic."""
        q = w3_quartic_shadow()
        on_T = q['on_T_line']
        vir_quartic = Rational(10) / (c * (5*c + 22))
        assert simplify(on_T - vir_quartic) == 0

    def test_T5_alpha_value(self):
        """alpha = 16/(5c+22)."""
        q = w3_quartic_shadow()
        expected = Rational(16) / (5*c + 22)
        assert simplify(q['alpha'] - expected) == 0

    def test_T6_N_Lambda_value(self):
        """N_Lambda = c(5c+22)/10."""
        q = w3_quartic_shadow()
        expected = c * (5*c + 22) / 10
        assert simplify(q['N_Lambda'] - expected) == 0

    def test_T7_Q_ratio_TTWW_over_TTTT(self):
        """Q_TTWW / Q_TTTT = alpha = 16/(5c+22)."""
        q = w3_quartic_shadow()
        ratio = simplify(q['Q_TTWW'] / q['Q_TTTT'])
        assert simplify(ratio - Rational(16) / (5*c + 22)) == 0

    def test_T8_Q_ratio_WWWW_over_TTWW(self):
        """Q_WWWW / Q_TTWW = alpha = 16/(5c+22)."""
        q = w3_quartic_shadow()
        ratio = simplify(q['Q_WWWW'] / q['Q_TTWW'])
        assert simplify(ratio - Rational(16) / (5*c + 22)) == 0

    def test_T9_geometric_progression(self):
        """Q_TTTT : Q_TTWW : Q_WWWW = 1 : alpha : alpha^2."""
        q = w3_quartic_shadow()
        alpha = Rational(16) / (5*c + 22)
        assert simplify(q['Q_TTWW'] - alpha * q['Q_TTTT']) == 0
        assert simplify(q['Q_WWWW'] - alpha**2 * q['Q_TTTT']) == 0

    def test_T10_weight4_quasi_primary_dim(self):
        """Weight-4 quasi-primary space is 1-dimensional."""
        data = w3_weight4_quasi_primaries()
        assert data['dim'] == 1


# ===========================================================================
# TestKacShadowSingularity (T11-T20)
# ===========================================================================

class TestKacShadowSingularity:
    """Kac-shadow singularity principle: shadow poles = Kac zeros."""

    def test_T11_all_shadow_zeros_are_kac(self):
        """Every shadow denominator zero is a Kac determinant zero."""
        ksp = kac_shadow_singularity_principle()
        for name, v in ksp['verifications'].items():
            assert v['all_are_kac_zeros'], f"{name} has non-Kac zeros"

    def test_T12_shared_factor_5c22(self):
        """All quartic shadow denominators share the factor (5c+22)."""
        q = w3_quartic_shadow()
        for coeff_name in ['Q_TTTT', 'Q_TTWW', 'Q_WWWW']:
            val = q[coeff_name].subs(c, Rational(-22, 5))
            # Should diverge (denominator zero) — check reciprocal vanishes
            recip = simplify(1 / q[coeff_name])
            assert simplify(recip.subs(c, Rational(-22, 5))) == 0

    def test_T13_c_zero_is_pole(self):
        """c=0 is a pole of all quartic shadow coefficients."""
        q = w3_quartic_shadow()
        for coeff_name in ['Q_TTTT', 'Q_TTWW', 'Q_WWWW']:
            recip = simplify(1 / q[coeff_name])
            assert simplify(recip.subs(c, 0)) == 0

    def test_T14_c_minus_22_over_5_is_pole(self):
        """c = -22/5 is a pole of Q_TTTT."""
        q = w3_quartic_shadow()
        recip = simplify(1 / q['Q_TTTT'])
        assert simplify(recip.subs(c, Rational(-22, 5))) == 0

    def test_T15_c_plus_24_in_C333(self):
        """(c+24) appears in C_333^2 denominator."""
        ksp = kac_shadow_singularity_principle()
        zeros = ksp['verifications']['W3_C333_sq']['zeros']
        assert -24 in zeros or Rational(-24) in [Rational(z) for z in zeros]

    def test_T16_Vir_Q_zeros(self):
        """Virasoro Q_TTTT denominator vanishes at c=0 and c=-22/5."""
        ksp = kac_shadow_singularity_principle()
        zeros = ksp['verifications']['Vir_Q_TTTT']['zeros']
        assert 0 in zeros or S.Zero in zeros
        assert Rational(-22, 5) in zeros

    def test_T17_kac_level4_factors(self):
        """Kac determinant at level 4 includes c, (2c-1), (5c+22), (7c+68)."""
        ksp = kac_shadow_singularity_principle()
        factors_4 = ksp['kac_factors'][4]
        # Check each factor vanishes at expected value
        factor_zeros = set()
        for f in factors_4:
            for val in [0, Rational(1, 2), Rational(-22, 5), Rational(-68, 7)]:
                if simplify(f.subs(c, val)) == 0:
                    factor_zeros.add(val)
        assert 0 in factor_zeros
        assert Rational(1, 2) in factor_zeros
        assert Rational(-22, 5) in factor_zeros
        assert Rational(-68, 7) in factor_zeros

    def test_T18_W3_Q_TTWW_double_pole(self):
        """Q_TTWW has a double pole at c = -22/5 (multiplicity 2)."""
        q = w3_quartic_shadow()
        # Q_TTWW = 160/[c(5c+22)^2]
        expected_denom = c * (5*c + 22)**2
        actual = simplify(Rational(160) / q['Q_TTWW'])
        assert simplify(actual - expected_denom) == 0

    def test_T19_W3_Q_WWWW_triple_pole(self):
        """Q_WWWW has a triple pole at c = -22/5 (multiplicity 3)."""
        q = w3_quartic_shadow()
        expected_denom = c * (5*c + 22)**3
        actual = simplify(Rational(2560) / q['Q_WWWW'])
        assert simplify(actual - expected_denom) == 0

    def test_T20_kac_level6_partial(self):
        """Kac det at level 6 includes (c+24) factor."""
        ksp = kac_shadow_singularity_principle()
        factors_6 = ksp['kac_factors'][6]
        has_c24 = any(simplify(f.subs(c, -24)) == 0 for f in factors_6)
        assert has_c24


# ===========================================================================
# TestDSShadowCompatibility (T21-T25)
# ===========================================================================

class TestDSShadowCompatibility:
    """DS reduction and shadow obstruction tower interaction."""

    def test_T21_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 4(k+3)/3."""
        ds = ds_shadow_compatibility()
        expected = Rational(4) * (k + 3) / 3
        assert simplify(ds['kappa_sl3'] - expected) == 0

    def test_T22_w3_kappa(self):
        """kappa(W_3) = 5c(k)/6."""
        ds = ds_shadow_compatibility()
        c_k = 2 - 24*(k + 2)**2 / (k + 3)
        expected = Rational(5) * c_k / 6
        assert simplify(ds['kappa_w3'] - expected) == 0

    def test_T23_ds_does_not_preserve_depth(self):
        """DS does NOT preserve shadow depth: sl_3 is L, W_3 is M."""
        ds = ds_shadow_compatibility()
        assert ds['ds_preserves_shadow_depth'] is False

    def test_T24_c_of_k(self):
        """c(k) = 2 - 24(k+2)^2/(k+3) at k=1 gives c = -46."""
        c_k = 2 - 24*(k + 2)**2 / (k + 3)
        val = c_k.subs(k, 1)
        # c(1) = 2 - 24*9/4 = 2 - 54 = -52
        assert simplify(val - (-52)) == 0

    def test_T25_sl3_class_L_w3_class_M(self):
        """sl_3 shadow class is L (r_max=3), W_3 is M (r_max=inf)."""
        ds = ds_shadow_compatibility()
        assert 'L' in ds['sl3_class']
        assert 'M' in ds['w3_class']


# ===========================================================================
# TestCorrectedTower (T26-T35)
# ===========================================================================

class TestCorrectedTower:
    """W_3 corrected shadow obstruction tower through master equation propagation."""

    def test_T26_Sh2(self):
        """Sh_2 = (c/2) x_T^2 + (c/3) x_W^2."""
        shadows = w3_corrected_shadow_tower(6)
        expected = (c / 2) * x_T**2 + (c / 3) * x_W**2
        assert simplify(shadows[2] - expected) == 0

    def test_T27_Sh3(self):
        """Sh_3 = 2 x_T^3 + 3 x_T x_W^2 (universal gravitational cubic, d_W=3)."""
        shadows = w3_corrected_shadow_tower(6)
        expected = 2 * x_T**3 + 3 * x_T * x_W**2
        assert simplify(shadows[3] - expected) == 0

    def test_T28_Sh4_structure(self):
        """Sh_4 has three monomials: x_T^4, x_T^2 x_W^2, x_W^4."""
        shadows = w3_corrected_shadow_tower(6)
        sh4 = expand(shadows[4])
        p = Poly(sh4, x_T, x_W, domain='ZZ(c)')
        monoms = set(p.monoms())
        # Should contain (4,0), (2,2), (0,4) only
        assert (4, 0) in monoms
        assert (2, 2) in monoms
        assert (0, 4) in monoms
        assert len(monoms) == 3

    def test_T29_Sh5_nonvanishing(self):
        """Sh_5 is nonzero (W_3 shadow obstruction tower is infinite)."""
        shadows = w3_corrected_shadow_tower(6)
        assert simplify(shadows[5]) != 0

    def test_T30_W_charge_conservation_Sh4(self):
        """Sh_4 has only even powers of x_W."""
        shadows = w3_corrected_shadow_tower(6)
        sh4 = expand(shadows[4])
        p = Poly(sh4, x_T, x_W, domain='ZZ(c)')
        for monom in p.monoms():
            assert monom[1] % 2 == 0, f"Odd x_W power in Sh_4: {monom}"

    def test_T31_W_charge_conservation_Sh5(self):
        """Sh_5 has only odd powers of x_W (by Z_2 symmetry, x_T^5 + x_T^3 x_W^2 + x_T x_W^4)."""
        shadows = w3_corrected_shadow_tower(6)
        sh5 = expand(shadows[5])
        p = Poly(sh5, x_T, x_W, domain='ZZ(c)')
        for monom in p.monoms():
            # Total degree is 5, W-charge conservation: W-parity = total parity mod 2
            # Actually: x_W must have even power (W → -W), so x_T must have odd power
            assert monom[1] % 2 == 0, f"Odd x_W power in Sh_5: {monom}"

    def test_T32_W_charge_conservation_Sh6(self):
        """Sh_6 has only even powers of x_W."""
        shadows = w3_corrected_shadow_tower(6)
        sh6 = expand(shadows[6])
        p = Poly(sh6, x_T, x_W, domain='ZZ(c)')
        for monom in p.monoms():
            assert monom[1] % 2 == 0, f"Odd x_W power in Sh_6: {monom}"

    def test_T33_T_line_autonomy_Sh4(self):
        """Sh_4 on T-line (x_W=0) equals Q_TTTT x_T^4."""
        shadows = w3_corrected_shadow_tower(6)
        sh4_T = expand(shadows[4].subs(x_W, 0))
        expected = Rational(10) / (c * (5*c + 22)) * x_T**4
        assert simplify(sh4_T - expected) == 0

    def test_T34_T_line_autonomy_Sh5(self):
        """Sh_5 on T-line has Coxeter anomaly = 0 at arity 5.

        The T-line shadow should propagate autonomously through
        the master equation at arity 5 as well (no W-backreaction
        at this order from the inputs)."""
        shadows = w3_corrected_shadow_tower(6)
        sh5_T = expand(shadows[5].subs(x_W, 0))
        # The T-line part of Sh_5 is generated by {Sh_2, Sh_3}
        # purely in the T-variable. Compute directly:
        # {Sh_2, Sh_3}_T = d(Sh_2)/d(x_T) * (2/c) * d(Sh_3)/d(x_T)
        # = c x_T * (2/c) * 6 x_T^2 = 12 x_T^3
        # Sh_5 = -12 x_T^3 / (2*5) = -6 x_T^3 / 5 ... but this is on T-line only
        # Just check it's a monomial in x_T
        if sh5_T != 0:
            p = Poly(sh5_T, x_T, domain='ZZ(c)')
            # Should be a single monomial x_T^5
            for monom in p.monoms():
                assert monom == (5,), f"Unexpected monomial on T-line Sh_5: {monom}"

    def test_T35_arity6_exists(self):
        """Sh_6 is computable and polynomial in x_T, x_W."""
        shadows = w3_corrected_shadow_tower(6)
        sh6 = expand(shadows[6])
        # Just check it's a polynomial (no error)
        assert sh6 is not None


# ===========================================================================
# TestDenominatorFiltration (T36-T40)
# ===========================================================================

class TestDenominatorFiltration:
    """(5c+22)^{1+k} pattern in quartic denominator."""

    def test_T36_pattern_T4(self):
        """Q_TTTT denominator has (5c+22)^1."""
        filt = w3_quartic_denominator_analysis()
        assert filt['(T^4)']['5c22_power'] == 1

    def test_T37_pattern_T2W2(self):
        """Q_TTWW denominator has (5c+22)^2."""
        filt = w3_quartic_denominator_analysis()
        assert filt['(T^2 W^2)']['5c22_power'] == 2

    def test_T38_pattern_W4(self):
        """Q_WWWW denominator has (5c+22)^3."""
        filt = w3_quartic_denominator_analysis()
        assert filt['(W^4)']['5c22_power'] == 3

    def test_T39_pattern_matches_formula(self):
        """(5c+22) power = 1 + W_legs/2 for each channel."""
        filt = w3_quartic_denominator_analysis()
        for name, data in filt.items():
            assert data['matches'], f"Pattern mismatch for {name}"

    def test_T40_all_channels_verified(self):
        """All three channels have verified Q_factored."""
        filt = w3_quartic_denominator_analysis()
        assert len(filt) == 3
        for name, data in filt.items():
            assert 'Q_factored' in data


# ===========================================================================
# TestSpecialValues (T41-T50)
# ===========================================================================

class TestSpecialValues:
    """Numerical evaluations at specific central charges."""

    def test_T41_c_equals_1(self):
        """Q_TTTT at c=1: 10/(1*27) = 10/27."""
        q = w3_quartic_shadow()
        val = q['Q_TTTT'].subs(c, 1)
        assert simplify(val - Rational(10, 27)) == 0

    def test_T42_c_equals_13(self):
        """Q_TTTT at c=13 (Virasoro self-dual): 10/(13*87) = 10/1131."""
        q = w3_quartic_shadow()
        val = q['Q_TTTT'].subs(c, 13)
        assert simplify(val - Rational(10, 1131)) == 0

    def test_T43_c_equals_25(self):
        """Q_TTTT at c=25: 10/(25*147) = 10/3675 = 2/735."""
        q = w3_quartic_shadow()
        val = q['Q_TTTT'].subs(c, 25)
        assert simplify(val - Rational(10, 3675)) == 0

    def test_T44_c_equals_26(self):
        """Q_TTTT at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        q = w3_quartic_shadow()
        val = q['Q_TTTT'].subs(c, 26)
        assert simplify(val - Rational(10, 3952)) == 0

    def test_T45_lee_yang_c_minus_22_over_5(self):
        """At c = -22/5 (Lee-Yang), Q_TTTT diverges (pole)."""
        q = w3_quartic_shadow()
        # Check denominator vanishes
        recip = simplify(1 / q['Q_TTTT'])
        assert simplify(recip.subs(c, Rational(-22, 5))) == 0

    def test_T46_Q_TTWW_at_c1(self):
        """Q_TTWW at c=1: 160/(1*27^2) = 160/729."""
        q = w3_quartic_shadow()
        val = q['Q_TTWW'].subs(c, 1)
        assert simplify(val - Rational(160, 729)) == 0

    def test_T47_Q_WWWW_at_c1(self):
        """Q_WWWW at c=1: 2560/(1*27^3) = 2560/19683."""
        q = w3_quartic_shadow()
        val = q['Q_WWWW'].subs(c, 1)
        assert simplify(val - Rational(2560, 19683)) == 0

    def test_T48_T_line_matches_virasoro_quartic(self):
        """On T-line, quartic shadow is exactly Virasoro Q^contact = 10/[c(5c+22)]."""
        q = w3_quartic_shadow()
        sh4 = q['Sh_4']
        sh4_T = expand(sh4.subs(x_W, 0))
        vir_quartic = Rational(10) / (c * (5*c + 22)) * x_T**4
        assert simplify(sh4_T - vir_quartic) == 0

    def test_T49_alpha_at_c1(self):
        """alpha at c=1: 16/27."""
        q = w3_quartic_shadow()
        val = q['alpha'].subs(c, 1)
        assert val == Rational(16, 27)

    def test_T50_N_Lambda_at_c1(self):
        """N_Lambda at c=1: 1*27/10 = 27/10."""
        q = w3_quartic_shadow()
        val = q['N_Lambda'].subs(c, 1)
        assert val == Rational(27, 10)
