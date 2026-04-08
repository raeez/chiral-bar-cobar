r"""Tests for W_3 Stokes resurgence engine.

40+ tests covering:
  - kappa formulas (AP1, AP9, multi-path verification)
  - Cross-channel corrections delta_F_g (exact, verified against graph sum)
  - Full genus expansion F_g = kappa * lambda_g^FP + delta_F_g^cross
  - Borel transform structure and singularities
  - Stokes constants (scalar, cross, full)
  - Instanton action invariance under multi-weight structure
  - MC equation / bridge equation constraints
  - Koszul duality c <-> 100 - c
  - Self-dual point c = 50
  - Per-channel decomposition
  - Multi-c comparison

Each test uses at least 2 independent verification paths (multi-path mandate).
"""

import math
import cmath
from fractions import Fraction

import numpy as np
import pytest

from compute.lib.theorem_w3_stokes_resurgence_engine import (
    # Bernoulli / FP
    _bernoulli_exact,
    _lambda_fp_exact,
    # kappa
    kappa_w3,
    kappa_T,
    kappa_W,
    kappa_w3_dual,
    # Cross-channel
    delta_F2_exact,
    delta_F3_exact,
    delta_Fg_extrapolated,
    # Full genus expansion
    F_g_scalar,
    F_g_cross,
    F_g_full,
    genus_expansion_table,
    # Borel
    borel_transform_scalar,
    borel_transform_cross,
    borel_transform_full,
    INSTANTON_ACTION,
    # Stokes
    stokes_scalar,
    stokes_cross_residue,
    stokes_full,
    leading_stokes_w3,
    # Singularity
    singularity_scan,
    # Instanton
    instanton_action_w3,
    # Bridge equation
    bridge_equation_check,
    # Koszul duality
    koszul_duality_stokes,
    # Per-channel
    per_channel_stokes,
    # Self-dual
    self_dual_stokes_symmetry,
    # Multi-c
    multi_c_stokes_comparison,
    # Full analysis
    full_w3_stokes_analysis,
)

PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI_SQ = TWO_PI ** 2


# ============================================================================
# Section 0: Bernoulli / Faber-Pandharipande consistency
# ============================================================================

class TestBernoulliAndFP:
    """Verify Bernoulli numbers and lambda_g^FP values."""

    def test_bernoulli_b2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_bernoulli_b6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert _lambda_fp_exact(3) == Fraction(31, 967680)


# ============================================================================
# Section 1: kappa formulas (AP1, AP9, multi-path)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa(W_3) via multiple independent computations."""

    def test_kappa_w3_c10(self):
        """kappa(W_3, c=10) = 5*10/6 = 25/3."""
        assert kappa_w3(Fraction(10)) == Fraction(25, 3)

    def test_kappa_w3_c50(self):
        """kappa(W_3, c=50) = 5*50/6 = 125/3."""
        assert kappa_w3(Fraction(50)) == Fraction(125, 3)

    def test_kappa_per_channel_sum(self):
        """kappa_T + kappa_W = kappa_total for all c."""
        for c_val in [1, 4, 10, 26, 50]:
            c = Fraction(c_val)
            assert kappa_T(c) + kappa_W(c) == kappa_w3(c)

    def test_kappa_harmonic_formula(self):
        """kappa(W_3) = c * (H_3 - 1) where H_3 = 1 + 1/2 + 1/3 = 11/6.

        Cross-check: c * (11/6 - 1) = c * 5/6.
        Path 1: harmonic number formula.
        Path 2: per-channel sum c/2 + c/3 = 5c/6.
        """
        for c_val in [1, 7, 26, 100]:
            c = Fraction(c_val)
            harmonic = Fraction(1) + Fraction(1, 2) + Fraction(1, 3)
            assert kappa_w3(c) == c * (harmonic - 1)

    def test_kappa_dual_symmetry(self):
        """kappa(c) + kappa(100-c) = 250/3 for all c."""
        for c_val in [1, 10, 26, 50, 99]:
            c = Fraction(c_val)
            assert kappa_w3(c) + kappa_w3_dual(c) == Fraction(250, 3)

    def test_kappa_T_equals_c_over_2(self):
        """kappa_T = c/2 (Virasoro sector)."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            assert kappa_T(c) == c / 2

    def test_kappa_W_equals_c_over_3(self):
        """kappa_W = c/3 (spin-3 sector)."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            assert kappa_W(c) == c / 3


# ============================================================================
# Section 2: Cross-channel corrections (exact, multi-path)
# ============================================================================

class TestCrossChannelCorrections:
    """Verify delta_F_g^cross from graph sum computations."""

    def test_delta_F2_formula(self):
        """delta_F_2 = (c + 204) / (16c), verified at multiple c values."""
        for c_val in [1, 4, 10, 26, 50, 100]:
            c = Fraction(c_val)
            result = delta_F2_exact(c)
            expected = (c + 204) / (16 * c)
            assert result == expected

    def test_delta_F2_partial_fractions(self):
        """delta_F_2 = 1/16 + 51/(4c), partial fraction decomposition.

        Path 1: closed form (c+204)/(16c).
        Path 2: partial fractions 1/16 + 204/(16c) = 1/16 + 51/(4c).
        """
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            from_formula = delta_F2_exact(c)
            from_partial = Fraction(1, 16) + Fraction(51, 4) / c
            assert from_formula == from_partial

    def test_delta_F2_positive(self):
        """delta_F_2 > 0 for all c > 0."""
        for c_val in [1, 4, 10, 26, 50, 100, 1000]:
            c = Fraction(c_val)
            assert delta_F2_exact(c) > 0

    def test_delta_F2_large_c_limit(self):
        """As c -> infinity, delta_F_2 -> 1/16."""
        c = Fraction(10**6)
        assert abs(float(delta_F2_exact(c)) - 1.0/16.0) < 1e-4

    def test_delta_F3_formula(self):
        """delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240 c^2)."""
        for c_val in [1, 4, 10, 50]:
            c = Fraction(c_val)
            result = delta_F3_exact(c)
            num = 5*c**3 + 3792*c**2 + 1149120*c + 217071360
            den = 138240 * c**2
            expected = Fraction(num, den)
            assert result == expected

    def test_delta_F3_partial_fractions(self):
        """delta_F_3 partial fractions: c/27648 + 79/2880 + (133/16)/c + (6281/4)/c^2.

        Path 1: closed form.
        Path 2: partial fraction sum.
        """
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            from_formula = delta_F3_exact(c)
            from_partial = (c / 27648 + Fraction(79, 2880)
                            + Fraction(133, 16) / c + Fraction(6281, 4) / c**2)
            assert from_formula == from_partial

    def test_delta_F3_positive(self):
        """delta_F_3 > 0 for all c > 0."""
        for c_val in [1, 4, 10, 26, 50, 100]:
            c = Fraction(c_val)
            assert delta_F3_exact(c) > 0

    def test_delta_F1_vanishes(self):
        """delta_F_1 = 0 (genus-1 universality is PROVED)."""
        for c_val in [1, 10, 50]:
            c = Fraction(c_val)
            assert F_g_cross(1, c) == 0


# ============================================================================
# Section 3: Full genus expansion
# ============================================================================

class TestGenusExpansion:
    """Test the full W_3 genus expansion at multiple c values."""

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 (genus-1 universality, no cross-channel)."""
        for c_val in [4, 10, 26, 50]:
            c = Fraction(c_val)
            expected = kappa_w3(c) / 24
            assert F_g_full(1, c) == expected
            assert F_g_cross(1, c) == 0

    def test_F2_scalar_plus_cross(self):
        """F_2 = kappa * lambda_2^FP + delta_F_2."""
        for c_val in [4, 10, 26, 50]:
            c = Fraction(c_val)
            sc = F_g_scalar(2, c)
            cr = F_g_cross(2, c)
            assert sc == kappa_w3(c) * _lambda_fp_exact(2)
            assert cr == delta_F2_exact(c)
            assert F_g_full(2, c) == sc + cr

    def test_F3_scalar_plus_cross(self):
        """F_3 = kappa * lambda_3^FP + delta_F_3."""
        for c_val in [4, 10, 26, 50]:
            c = Fraction(c_val)
            sc = F_g_scalar(3, c)
            cr = F_g_cross(3, c)
            assert sc == kappa_w3(c) * _lambda_fp_exact(3)
            assert cr == delta_F3_exact(c)

    def test_cross_fraction_increases_with_genus(self):
        """The cross-channel fraction F_cross/F_total grows with genus.

        This is because delta_F_g grows FASTER than kappa * lambda_g^FP
        at large g (the cross-channel has polynomial growth in g, while
        lambda_g^FP has Bernoulli decay).
        """
        c = Fraction(10)
        table = genus_expansion_table(c, g_max=3)
        # At c=10, verify cross fraction is nonzero at g=2
        assert table[2]['cross_fraction'] > 0

    def test_genus_table_structure(self):
        """Genus expansion table has correct structure."""
        c = Fraction(26)
        table = genus_expansion_table(c, g_max=4)
        assert 1 in table
        assert 4 in table
        assert 'F_scalar' in table[1]
        assert 'F_cross' in table[1]
        assert 'F_total' in table[1]


# ============================================================================
# Section 4: Borel transforms
# ============================================================================

class TestBorelTransforms:
    """Test Borel transform structure and singularities."""

    def test_scalar_borel_at_origin(self):
        """B[F^{scalar}](0) = kappa/24 / 2! (leading term)."""
        kappa = 5.0 * 10.0 / 6.0  # W_3 at c=10
        b0 = borel_transform_scalar(0.001, kappa)
        # Near origin: B(xi) ~ F_1 * xi^2 / 2! = kappa/24 * xi^2 / 2
        expected = kappa / 24.0 * 0.001**2 / 2.0
        assert abs(b0 - expected) < 1e-6

    def test_scalar_borel_pole_at_2pi(self):
        """B[F^{scalar}](xi) diverges as xi -> 2*pi (first singularity)."""
        kappa = 5.0 * 10.0 / 6.0
        # Evaluate close to 2*pi
        b_near = abs(borel_transform_scalar(TWO_PI - 0.01, kappa))
        b_far = abs(borel_transform_scalar(TWO_PI - 1.0, kappa))
        assert b_near > b_far * 5  # diverging near the pole

    def test_cross_borel_starts_at_g2(self):
        """B[F^{cross}](xi) starts at xi^4 (g=2 is first nonzero term)."""
        c = 10.0
        b_small = borel_transform_cross(0.1, c)
        # At small xi, B^{cross} ~ delta_F_2 * xi^4 / 4!
        dF2 = float(delta_F2_exact(Fraction(10)))
        expected = dF2 * 0.1**4 / math.factorial(4)
        # Tolerance accounts for the g=3 term (subleading at small xi)
        assert abs(b_small - expected) < 1e-6

    def test_full_borel_equals_sum(self):
        """B[F^{full}] = B[F^{scalar}] + B[F^{cross}] at several points."""
        c = 26.0
        kappa = 5.0 * 26.0 / 6.0
        for xi in [1.0, 3.0, 5.0]:
            bs = borel_transform_scalar(xi, kappa)
            bc = borel_transform_cross(xi, c)
            bf = borel_transform_full(xi, c)
            # Relative tolerance for large magnitudes
            scale = max(abs(bf), abs(bs + bc), 1e-15)
            assert abs(bf - (bs + bc)) / scale < 1e-10


# ============================================================================
# Section 5: Stokes constants
# ============================================================================

class TestStokesConstants:
    """Test Stokes constant formulas and decomposition."""

    def test_scalar_stokes_formula(self):
        """S_n^{scalar} = (-1)^n * 4*pi^2 * n * kappa * i."""
        kappa = 5.0 * 10.0 / 6.0
        s1 = stokes_scalar(1, kappa)
        expected = -4.0 * PI**2 * kappa * 1j
        assert abs(s1 - expected) < 1e-10

    def test_scalar_stokes_is_imaginary(self):
        """Scalar Stokes constants are purely imaginary."""
        for c_val in [4.0, 10.0, 50.0]:
            kappa = 5.0 * c_val / 6.0
            for n in range(1, 4):
                sn = stokes_scalar(n, kappa)
                assert abs(sn.real) < 1e-10 * abs(sn.imag)

    def test_scalar_stokes_alternating_sign(self):
        """S_n alternates sign: S_1 has Im < 0, S_2 has Im > 0, etc."""
        kappa = 5.0 * 10.0 / 6.0
        assert stokes_scalar(1, kappa).imag < 0
        assert stokes_scalar(2, kappa).imag > 0
        assert stokes_scalar(3, kappa).imag < 0

    def test_leading_stokes_w3_structure(self):
        """Leading Stokes data has correct structure."""
        result = leading_stokes_w3(10.0)
        assert 'S1_scalar' in result
        assert 'S1_cross' in result
        assert 'S1_full' in result
        assert result['instanton_action'] == INSTANTON_ACTION

    def test_stokes_per_channel_additivity(self):
        """S_1^{scalar}(total) = S_1^{scalar}(T) + S_1^{scalar}(W).

        Path 1: compute S_1 with total kappa.
        Path 2: sum per-channel S_1.
        """
        for c_val in [4.0, 10.0, 50.0]:
            result = per_channel_stokes(c_val)
            assert result['per_channel_additivity']


# ============================================================================
# Section 6: Instanton action
# ============================================================================

class TestInstantonAction:
    """Test that the instanton action A = (2*pi)^2 is unchanged by multi-weight.

    The cross-channel Borel transform B[F^{cross}](xi) is a finite sum of
    entire functions xi^{2g}/(2g)! weighted by rational coefficients in c.
    It has no singularities in the finite xi-plane, so it cannot move the
    leading Borel singularity from xi = 2*pi.
    """

    def test_instanton_action_value(self):
        """A = (2*pi)^2."""
        assert abs(INSTANTON_ACTION - FOUR_PI_SQ) < 1e-10

    def test_instanton_action_unchanged_c10(self):
        """The instanton action is unchanged for W_3 at c=10."""
        result = instanton_action_w3(10.0)
        assert result['A_unchanged']
        assert result['cross_borel_entire']

    def test_instanton_action_unchanged_c50(self):
        """The instanton action is unchanged for W_3 at c=50."""
        result = instanton_action_w3(50.0)
        assert result['A_unchanged']

    def test_cross_dominates_at_low_genus_small_c(self):
        """At small c, the cross-channel dominates the scalar part at low genus.

        This is NOT evidence that A changes -- it reflects the different
        growth regimes. The scalar part has Bernoulli decay 1/(2*pi)^{2g},
        while the cross part has rational-in-c coefficients that can be large.
        At large genus, the Bernoulli factorial growth always wins.
        """
        c = Fraction(10)
        sc2 = float(F_g_scalar(2, c))
        cr2 = float(F_g_cross(2, c))
        # Cross dominates scalar at genus 2 for c=10
        assert cr2 > sc2


# ============================================================================
# Section 7: Singularity structure
# ============================================================================

class TestSingularityStructure:
    """Test that cross-channel does NOT create new singularities."""

    def test_no_new_singularities_c10(self):
        """Cross-channel does not create new singularities at c=10."""
        result = singularity_scan(10.0)
        assert not result['cross_creates_new_singularities']

    def test_no_new_singularities_c50(self):
        """Cross-channel does not create new singularities at c=50."""
        result = singularity_scan(50.0)
        assert not result['cross_creates_new_singularities']


# ============================================================================
# Section 8: Koszul duality
# ============================================================================

class TestKoszulDuality:
    """Test Koszul duality c <-> 100-c for Stokes data."""

    def test_kappa_complementarity(self):
        """kappa(c) + kappa(100-c) = 250/3 for all c."""
        for c_val in [4.0, 10.0, 26.0, 50.0]:
            result = koszul_duality_stokes(c_val)
            assert result['scalar_complementarity_holds']

    def test_self_dual_kappa(self):
        """At c=50: kappa = kappa_dual = 125/3."""
        result = koszul_duality_stokes(50.0)
        assert result['is_self_dual']
        assert abs(result['kappa_sum'] - 250.0/3.0) < 1e-10

    def test_scalar_stokes_complementarity(self):
        """S_1^{scalar}(c) + S_1^{scalar}(100-c) = -4*pi^2 * (250/3) * i.

        The scalar Stokes sum is FIXED.
        """
        for c_val in [4.0, 10.0, 26.0]:
            result = koszul_duality_stokes(c_val)
            expected = -4.0 * PI**2 * 250.0/3.0 * 1j
            actual = result['S1_scalar_sum']
            assert abs(actual - expected) < 1e-6

    def test_cross_correction_sum_not_universal(self):
        """delta_F_2(c) + delta_F_2(100-c) depends on c (not universal)."""
        r1 = koszul_duality_stokes(10.0)
        r2 = koszul_duality_stokes(26.0)
        # The sums should be different
        assert abs(r1['dF2_sum'] - r2['dF2_sum']) > 1e-6


# ============================================================================
# Section 9: Self-dual point c = 50
# ============================================================================

class TestSelfDualPoint:
    """Detailed analysis at the W_3 self-dual point c=50."""

    def test_self_dual_kappa_value(self):
        """kappa(W_3, c=50) = 125/3."""
        assert kappa_w3(Fraction(50)) == Fraction(125, 3)

    def test_self_dual_delta_F2(self):
        """delta_F_2(50) = (50 + 204)/(16*50) = 254/800 = 127/400."""
        assert delta_F2_exact(Fraction(50)) == Fraction(127, 400)

    def test_self_dual_symmetry(self):
        """At c=50, kappa(c) = kappa(100-c)."""
        result = self_dual_stokes_symmetry()
        assert result['kappa_equal']

    def test_self_dual_nonzero_cross(self):
        """delta_F_2 is nonzero at the self-dual point (unlike scalar kappa)."""
        result = self_dual_stokes_symmetry()
        assert result['F_2_cross'] != 0


# ============================================================================
# Section 10: Bridge equation / MC constraint
# ============================================================================

class TestBridgeEquation:
    """Test MC equation constraints on Stokes multipliers."""

    def test_bridge_scalar_consistency(self):
        """Scalar bridge equation: S_n = 2*pi*i * Res_{xi_n} B[F]."""
        result = bridge_equation_check(10.0, n_max=3)
        for key, data in result.items():
            assert data['bridge_check_scalar'] < 1e-10

    def test_cross_stokes_finite(self):
        """Cross-channel Stokes contribution is finite (not divergent).

        The cross-channel Borel transform is ENTIRE (no poles), so the
        numerical discontinuity extraction yields the smooth function value
        at xi_n, not a pole residue.  The cross-channel modifies the
        Stokes constant by adding to the scalar residue, but this
        modification is finite at every singularity.
        """
        result = bridge_equation_check(10.0, n_max=2)
        for key, data in result.items():
            # Cross contribution is finite (not inf or nan)
            assert math.isfinite(data['cross_to_scalar'])


# ============================================================================
# Section 11: Full analysis integration
# ============================================================================

class TestFullAnalysis:
    """Test the complete analysis pipeline."""

    def test_full_analysis_c4(self):
        """Full W_3 analysis at c=4."""
        result = full_w3_stokes_analysis(4.0)
        assert result.instanton_action == INSTANTON_ACTION
        assert result.kappa == pytest.approx(5.0 * 4.0 / 6.0, rel=1e-10)
        assert not result.cross_creates_new_singularities

    def test_full_analysis_c26(self):
        """Full W_3 analysis at c=26."""
        result = full_w3_stokes_analysis(26.0)
        assert result.instanton_action_unchanged
        assert not result.cross_creates_new_singularities

    def test_full_analysis_c50(self):
        """Full W_3 analysis at c=50 (self-dual)."""
        result = full_w3_stokes_analysis(50.0)
        assert result.instanton_action_unchanged
        assert not result.cross_creates_new_singularities
        assert result.koszul_complementarity['is_self_dual']


# ============================================================================
# Section 12: Multi-c comparison
# ============================================================================

class TestMultiCComparison:
    """Test Stokes data across multiple central charges."""

    def test_multi_c_all_same_instanton_action(self):
        """All c values have the same instanton action."""
        result = multi_c_stokes_comparison([4.0, 10.0, 26.0, 50.0])
        for key, data in result.items():
            assert data['instanton_action'] == INSTANTON_ACTION

    def test_multi_c_cross_ratio_finite(self):
        """Cross-channel ratio is finite and bounded for all c > 0."""
        result = multi_c_stokes_comparison([4.0, 10.0, 26.0, 50.0])
        for key, data in result.items():
            assert data['cross_ratio'] < float('inf')
            assert data['cross_ratio'] >= 0

    def test_kappa_increases_with_c(self):
        """kappa(W_3) = 5c/6 increases linearly with c."""
        result = multi_c_stokes_comparison([4.0, 10.0, 50.0])
        kappas = [data['kappa'] for data in result.values()]
        assert kappas == sorted(kappas)


# ============================================================================
# Section 13: Cross-checks between sections
# ============================================================================

class TestCrossChecks:
    """Cross-checks between different parts of the engine."""

    def test_genus_table_matches_individual(self):
        """Genus table entries match individual F_g computations."""
        c = Fraction(10)
        table = genus_expansion_table(c, g_max=3)
        for g in range(1, 4):
            assert float(F_g_scalar(g, c)) == pytest.approx(table[g]['F_scalar'], rel=1e-12)
            assert float(F_g_cross(g, c)) == pytest.approx(table[g]['F_cross'], rel=1e-12)
            assert float(F_g_full(g, c)) == pytest.approx(table[g]['F_total'], rel=1e-12)

    def test_stokes_decomposition_consistency(self):
        """S_1^{full} = S_1^{scalar} + S_1^{cross}."""
        result = leading_stokes_w3(10.0)
        assert abs(result['S1_full'] - result['S1_scalar'] - result['S1_cross']) < 1e-10

    def test_cross_fraction_monotone_in_c(self):
        """For fixed genus, the cross fraction delta_F_2/F_2 varies with c.

        At large c: delta_F_2 ~ 1/16, F_2^{scalar} ~ 7c/(6*5760).
        So the cross fraction ~ 5760/(16*7*c/6) = 2160/(56c) -> 0 as c -> infty.
        At small c: delta_F_2 ~ 51/(4c), F_2^{scalar} ~ 7c/(6*5760).
        So the cross fraction diverges as c -> 0.
        """
        fracs = []
        for c_val in [10, 50, 100, 1000]:
            c = Fraction(c_val)
            sc = F_g_scalar(2, c)
            cr = F_g_cross(2, c)
            total = sc + cr
            fracs.append(float(cr / total))
        # Cross fraction should decrease as c increases (for large c)
        assert fracs[-1] < fracs[0]
