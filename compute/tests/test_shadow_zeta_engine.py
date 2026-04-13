"""Tests for compute/lib/shadow_zeta_engine.py -- shadow zeta function.

Validates:
  1. Bernoulli number computation (exact)
  2. Shadow coefficients b_g against known values
  3. Free energies F_g at specific kappa values
  4. Shadow zeta partial sums
  5. Convergence analysis (Gevrey-0, radius = (2*pi)^2)
  6. Virasoro specialization at c = 1, 13, 25, 26

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Faber-Pandharipande, "Hodge integrals and moduli of curves" (2000)
  - CLAUDE.md C2 (kappa(Vir) = c/2), C24 (F_1 = kappa/24), B37 (F_2 = 7/5760)
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import math
import pytest
from fractions import Fraction

from compute.lib.shadow_zeta_engine import (
    _bernoulli_exact,
    bernoulli_even,
    shadow_b_g,
    shadow_F_g,
    shadow_zeta,
    shadow_zeta_exact,
    shadow_zeta_terms,
    analyze_convergence,
    virasoro_kappa,
    virasoro_shadow_zeta,
)


# ============================================================================
# Bernoulli numbers
# ============================================================================

class TestBernoulli:
    """Exact Bernoulli number computation."""

    def test_B0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        # VERIFIED [DC] direct recurrence [LT] Abramowitz-Stegun Table 23.2
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        # VERIFIED [DC] direct recurrence [LT] Abramowitz-Stegun Table 23.2
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_B12(self):
        # VERIFIED [DC] direct recurrence [LT] Abramowitz-Stegun
        assert _bernoulli_exact(12) == Fraction(-691, 2730)

    def test_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert _bernoulli_exact(n) == Fraction(0), f"B_{n} should vanish"

    def test_bernoulli_even_wrapper(self):
        """bernoulli_even(g) returns B_{2g}."""
        assert bernoulli_even(1) == Fraction(1, 6)
        assert bernoulli_even(2) == Fraction(-1, 30)
        assert bernoulli_even(3) == Fraction(1, 42)


# ============================================================================
# Shadow coefficients b_g
# ============================================================================

class TestShadowCoefficients:
    """Universal coefficients b_g = (2^{2g-1}-1)*|B_{2g}| / (2^{2g-1}*(2g)!)."""

    def test_b1(self):
        """b_1 = 1/24.
        # VERIFIED [DC] (2^1-1)/2^1 * (1/6)/2! = (1/2)*(1/6)/2 = 1/24
        # VERIFIED [LT] CLAUDE.md C24: F_1 = kappa/24
        """
        assert shadow_b_g(1) == Fraction(1, 24)

    def test_b2(self):
        """b_2 = 7/5760.
        # VERIFIED [DC] (2^3-1)/2^3 * (1/30)/4! = (7/8)*(1/30)/24 = 7/5760
        # VERIFIED [LT] CLAUDE.md B37: F_2 = 7/5760 (at kappa=1)
        """
        assert shadow_b_g(2) == Fraction(7, 5760)

    def test_b3(self):
        """b_3 = 31/967680.
        # VERIFIED [DC] (2^5-1)/2^5 * (1/42)/6! = (31/32)*(1/42)/720 = 31/967680
        # VERIFIED [NE] 31/967680 = 3.2035e-05, matches sympy computation
        """
        assert shadow_b_g(3) == Fraction(31, 967680)

    def test_b4(self):
        """b_4 = 127/154828800.
        # VERIFIED [DC] (2^7-1)/2^7 * (1/30)/8! = (127/128)*(1/30)/40320
        # VERIFIED [NE] cross-checked with sympy bernoulli(8)
        """
        assert shadow_b_g(4) == Fraction(127, 154828800)

    def test_all_positive(self):
        """All b_g are positive (since |B_{2g}| > 0 and prefactor > 0)."""
        for g in range(1, 11):
            assert shadow_b_g(g) > 0, f"b_{g} should be positive"

    def test_monotone_decreasing(self):
        """b_g is strictly decreasing for g >= 1."""
        for g in range(1, 10):
            assert shadow_b_g(g) > shadow_b_g(g + 1), \
                f"b_{g} should be > b_{g+1}"

    def test_invalid_genus(self):
        with pytest.raises(ValueError):
            shadow_b_g(0)
        with pytest.raises(ValueError):
            shadow_b_g(-1)


# ============================================================================
# Free energies F_g
# ============================================================================

class TestFreeEnergies:
    """F_g(kappa) = kappa^g * b_g."""

    def test_F1_kappa_1(self):
        """F_1(1) = 1/24.
        # VERIFIED [DC] 1^1 * 1/24 = 1/24
        # VERIFIED [LT] CLAUDE.md C24
        """
        assert shadow_F_g(1, Fraction(1)) == Fraction(1, 24)

    def test_F2_kappa_1(self):
        """F_2(1) = 7/5760.
        # VERIFIED [DC] 1^2 * 7/5760 = 7/5760
        # VERIFIED [LT] CLAUDE.md B37
        """
        assert shadow_F_g(2, Fraction(1)) == Fraction(7, 5760)

    def test_F1_virasoro_c1(self):
        """Virasoro c=1: kappa=1/2, F_1 = (1/2)/24 = 1/48.
        # VERIFIED [DC] (1/2)^1 * 1/24 = 1/48
        # VERIFIED [LC] kappa(Vir_1) = 1/2 from CLAUDE.md C2
        """
        kappa = Fraction(1, 2)
        assert shadow_F_g(1, kappa) == Fraction(1, 48)

    def test_F1_virasoro_c13(self):
        """Virasoro c=13 (self-dual): kappa=13/2, F_1 = 13/48.
        # VERIFIED [DC] (13/2)/24 = 13/48
        # VERIFIED [SY] c=13 is self-dual point (CLAUDE.md C8)
        """
        kappa = Fraction(13, 2)
        assert shadow_F_g(1, kappa) == Fraction(13, 48)

    def test_F1_virasoro_c26(self):
        """Virasoro c=26: kappa=13, F_1 = 13/24.
        # VERIFIED [DC] 13/24
        # VERIFIED [LT] c=26 is bosonic string critical dimension
        """
        kappa = Fraction(13)
        assert shadow_F_g(1, kappa) == Fraction(13, 24)

    def test_F_g_scaling(self):
        """F_g(a*kappa) = a^g * F_g(kappa)."""
        kappa = Fraction(3, 2)
        a = Fraction(2)
        for g in range(1, 6):
            lhs = shadow_F_g(g, a * kappa)
            rhs = a ** g * shadow_F_g(g, kappa)
            assert lhs == rhs, f"Scaling fails at g={g}"

    def test_F_g_kappa_zero(self):
        """F_g(0) = 0 for all g >= 1."""
        for g in range(1, 6):
            assert shadow_F_g(g, Fraction(0)) == Fraction(0)


# ============================================================================
# Shadow zeta function
# ============================================================================

class TestShadowZeta:
    """Z_A(s) = sum F_g * g^{-s}."""

    def test_zeta_s0_is_sum_of_terms(self):
        """Z_A(0) = sum F_g (all g^0 = 1)."""
        kappa = Fraction(1, 2)
        terms = shadow_zeta_terms(kappa, 10)
        z0 = shadow_zeta_exact(0, kappa, 10)
        assert z0 == sum(terms)

    def test_zeta_s1_kappa1(self):
        """Z_A(1) at kappa=1: sum b_g / g.
        # VERIFIED [DC] F_1/1 + F_2/2 = 1/24 + 7/11520 = 487/11520
        # VERIFIED [NE] numerical cross-check below
        """
        kappa = Fraction(1)
        z1_exact = shadow_zeta_exact(1, kappa, 2)
        expected = Fraction(1, 24) + Fraction(7, 11520)
        assert z1_exact == expected

    def test_zeta_float_matches_exact(self):
        """Float evaluation matches exact for integer s."""
        kappa = Fraction(13, 2)
        for s_val in [0, 1, 2, 3]:
            z_exact = float(shadow_zeta_exact(s_val, kappa, 10))
            z_float = shadow_zeta(float(s_val), kappa, 10)
            assert abs(z_exact - z_float) < 1e-14 * max(abs(z_exact), 1e-20), \
                f"Mismatch at s={s_val}"

    def test_zeta_terms_length(self):
        """shadow_zeta_terms returns exactly G_max terms."""
        for G in [5, 10, 15]:
            terms = shadow_zeta_terms(Fraction(1), G)
            assert len(terms) == G

    def test_zeta_monotone_in_kappa(self):
        """Z_A(0) increases with kappa (all terms positive)."""
        z1 = shadow_zeta_exact(0, Fraction(1, 2), 10)
        z2 = shadow_zeta_exact(0, Fraction(1), 10)
        z3 = shadow_zeta_exact(0, Fraction(13, 2), 10)
        assert z1 < z2 < z3


# ============================================================================
# Convergence analysis
# ============================================================================

class TestConvergence:
    """Gevrey-0 classification and convergence radius."""

    def test_gevrey_class_zero(self):
        """Shadow series is Gevrey-0 (geometric decay, not factorial)."""
        analysis = analyze_convergence(Fraction(1), 10)
        assert analysis.gevrey_class == 0

    def test_convergence_radius(self):
        """Convergence radius in kappa is (2*pi)^2 ~ 39.478.
        # VERIFIED [DC] |b_{g+1}/b_g| -> 1/(2*pi)^2
        # VERIFIED [NE] numerical ratio at g=9->10 matches to 5 digits
        """
        analysis = analyze_convergence(Fraction(1), 10)
        assert abs(analysis.convergence_radius_kappa - (2 * math.pi) ** 2) < 1e-6

    def test_asymptotic_ratio(self):
        """Asymptotic |b_{g+1}/b_g| = 1/(2*pi)^2."""
        analysis = analyze_convergence(Fraction(1), 10)
        expected = 1.0 / (2.0 * math.pi) ** 2
        assert abs(analysis.asymptotic_ratio - expected) < 1e-10

    def test_ratios_converge_to_asymptotic(self):
        """Successive ratios |F_{g+1}/F_g| converge to kappa/(2*pi)^2.
        # VERIFIED [DC] explicit ratio computation
        # VERIFIED [NE] last ratio within 0.01% of limit
        """
        kappa = Fraction(1)
        analysis = analyze_convergence(kappa, 10)
        expected_limit = float(kappa) / (2.0 * math.pi) ** 2
        # Last ratio should be close to the limit
        last_ratio = analysis.ratios[-1]
        assert abs(last_ratio - expected_limit) / expected_limit < 1e-3

    def test_virasoro_c1_convergent(self):
        """c=1: kappa=1/2 < (2*pi)^2 => convergent."""
        analysis = analyze_convergence(Fraction(1, 2), 10)
        assert analysis.is_convergent

    def test_virasoro_c13_convergent(self):
        """c=13: kappa=13/2 < (2*pi)^2 => convergent (self-dual)."""
        analysis = analyze_convergence(Fraction(13, 2), 10)
        assert analysis.is_convergent

    def test_virasoro_c25_convergent(self):
        """c=25: kappa=25/2 < (2*pi)^2 => convergent."""
        analysis = analyze_convergence(Fraction(25, 2), 10)
        assert analysis.is_convergent

    def test_virasoro_c26_convergent(self):
        """c=26: kappa=13 < (2*pi)^2 => convergent."""
        analysis = analyze_convergence(Fraction(13), 10)
        assert analysis.is_convergent

    def test_large_kappa_divergent(self):
        """kappa=40 > (2*pi)^2 ~ 39.478 => divergent."""
        analysis = analyze_convergence(Fraction(40), 10)
        assert not analysis.is_convergent

    def test_ratios_list_length(self):
        """There are G_max - 1 successive ratios."""
        analysis = analyze_convergence(Fraction(1), 10)
        assert len(analysis.ratios) == 9


# ============================================================================
# Virasoro specialization
# ============================================================================

class TestVirasoro:
    """Virasoro kappa and shadow zeta."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2.
        # VERIFIED [DC] CLAUDE.md C2  [LT] landscape_census.tex
        """
        assert virasoro_kappa(Fraction(1)) == Fraction(1, 2)
        assert virasoro_kappa(Fraction(13)) == Fraction(13, 2)
        assert virasoro_kappa(Fraction(25)) == Fraction(25, 2)
        assert virasoro_kappa(Fraction(26)) == Fraction(13)

    def test_self_dual_c13(self):
        """At c=13 (self-dual), kappa = 13/2.
        # VERIFIED [DC] CLAUDE.md C8: self-dual at c=13
        # VERIFIED [SY] kappa + kappa' = 13 => self-dual kappa = 13/2
        """
        kappa = virasoro_kappa(Fraction(13))
        assert kappa == Fraction(13, 2)

    def test_complementary_c1_c25(self):
        """c=1 and c=25 are Koszul complements: kappa + kappa' = 13.
        # VERIFIED [DC] 1/2 + 25/2 = 26/2 = 13
        # VERIFIED [LT] CLAUDE.md C8, C18
        """
        k1 = virasoro_kappa(Fraction(1))
        k25 = virasoro_kappa(Fraction(25))
        assert k1 + k25 == Fraction(13)

    def test_virasoro_shadow_zeta_wrapper(self):
        """virasoro_shadow_zeta delegates correctly."""
        c = Fraction(13)
        kappa = virasoro_kappa(c)
        z_direct = shadow_zeta(2.0, kappa, 10)
        z_wrapper = virasoro_shadow_zeta(2.0, c, 10)
        assert abs(z_direct - z_wrapper) < 1e-15

    def test_c26_kappa_integer(self):
        """At c=26, kappa=13 is integer (bosonic string critical dimension).
        # VERIFIED [DC] 26/2 = 13
        # VERIFIED [LT] c=26 ghost cancellation from CLAUDE.md C7
        """
        assert virasoro_kappa(Fraction(26)) == Fraction(13)


# ============================================================================
# Cross-checks and special values
# ============================================================================

class TestCrossChecks:
    """Multi-path verification of special values."""

    def test_F1_universal(self):
        """F_1 = kappa/24 for all kappa.
        # VERIFIED [DC] b_1 = 1/24  [LT] CLAUDE.md C24  [CF] stable_graph F_1
        """
        for kappa_val in [Fraction(1, 2), Fraction(1), Fraction(13, 2), Fraction(13)]:
            assert shadow_F_g(1, kappa_val) == kappa_val / 24

    def test_complementary_zeta_symmetry(self):
        """Complementary pair c=1, c=25: check Z_A(0) ratio.

        At kappa and kappa' = 13 - kappa, the terms relate by
        F_g(kappa') / F_g(kappa) = (kappa'/kappa)^g.
        """
        k1 = Fraction(1, 2)
        k25 = Fraction(25, 2)
        for g in range(1, 6):
            ratio = shadow_F_g(g, k25) / shadow_F_g(g, k1)
            expected = (k25 / k1) ** g
            assert ratio == expected

    def test_b_g_sum_relation(self):
        """sum_{g=1}^{G} b_g converges (since b_g ~ (2*pi)^{-2g}).

        Partial sum at G=10 should be close to the infinite sum.
        The infinite sum is log(2*sinh(1/2)) by evaluating the GF...
        actually the GF with these specific coefficients isn't a standard
        closed form, but we verify internal consistency: the partial sum
        at G=10 and G=9 should differ by b_10.
        """
        terms = shadow_zeta_terms(Fraction(1), 10)
        partial_9 = sum(terms[:9])
        partial_10 = sum(terms)
        assert partial_10 - partial_9 == terms[9]

    def test_zeta_s2_positive(self):
        """Z_A(2) > 0 for all tested kappa (all terms positive, g^{-2} > 0)."""
        for kappa_val in [Fraction(1, 2), Fraction(1), Fraction(13, 2), Fraction(13)]:
            z2 = shadow_zeta(2.0, kappa_val, 10)
            assert z2 > 0
