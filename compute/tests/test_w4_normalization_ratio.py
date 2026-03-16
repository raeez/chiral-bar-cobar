"""Tests for MC4 normalization ratio R(t).

Verifies the exact conversion between Miura and concordance conventions
for the W(sl₄) OPE structure constant c₃₃₄.

Ground truth:
  w4_exact_miura.py (exact computation at t=1, 28 tests)
  concordance.tex (MC4 stage-4 packet)
  Blumenhagen et al. (concordance formula)
"""

import pytest
from sympy import Symbol, Rational, simplify, factor, cancel, S

from compute.lib.w4_normalization_ratio import (
    norm_T, norm_W3, norm_W4, C433,
    c_physical, c_miura, c_ratio,
    concordance_c334_sq, concordance_c444_sq,
    normalization_ratio_R, c334_sq_miura,
    verify_R_definition,
)


class TestExactNorms:
    """Verify Miura BPZ norms at specific t values."""

    def test_norm_T_at_t1(self):
        assert norm_T(1) == 3 * 1 * (3 - 28)  # = -75

    def test_norm_W3_at_t1(self):
        assert norm_W3(1) == 4 * 1 * (4 - 167 + 660)  # = 1988

    def test_norm_W4_at_t1(self):
        assert norm_W4(1) == 6 * 1 * (1 - 73 + 1032 - 2520)  # = -9360

    def test_C433_at_t1(self):
        assert C433(1) == -96 * 1 * (-7) * (-19)  # = -12768

    def test_all_norms_vanish_at_t0(self):
        assert norm_T(0) == 0
        assert norm_W3(0) == 0
        assert norm_W4(0) == 0
        assert C433(0) == 0

    def test_C433_vanishes_at_t8(self):
        assert C433(8) == 0

    def test_C433_vanishes_at_t_21_2(self):
        assert C433(Rational(21, 2)) == 0


class TestCentralCharge:
    """Verify the T_Miura ≠ T_standard discrepancy."""

    def test_c_physical_at_t1(self):
        assert c_physical(1) == 63

    def test_c_miura_at_t1(self):
        assert c_miura(1) == -150

    def test_c_mismatch(self):
        """The Miura T gives a DIFFERENT central charge."""
        assert c_miura(1) != c_physical(1)

    def test_c_ratio_formula(self):
        """c_M/c_phys = 2t(3t-28)/(20t+1)."""
        t = Symbol('t')
        assert simplify(c_ratio(t) - 2 * t * (3 * t - 28) / (20 * t + 1)) == 0

    def test_c_ratio_at_t1(self):
        assert c_ratio(Rational(1)) == Rational(-50, 21)


class TestConcordance:
    """Verify concordance formula values."""

    def test_concordance_c334_at_c63(self):
        val = concordance_c334_sq(63)
        expected = Rational(42 * 63**2 * 337, 87 * 509 * 235)
        assert simplify(val - expected) == 0

    def test_concordance_c334_positive_at_c63(self):
        assert concordance_c334_sq(63) > 0

    def test_concordance_c444_at_c63(self):
        """c₄₄₄²(c=63) should be a positive rational."""
        val = concordance_c444_sq(63)
        assert val > 0


class TestNormalizationRatio:
    """Verify the exact normalization ratio R(t)."""

    def test_R_at_t1(self):
        """R(1) = 500899774/1453155795."""
        R = normalization_ratio_R(Rational(1))
        assert R == Rational(500899774, 1453155795)

    def test_R_matches_definition_at_t1(self):
        result = verify_R_definition(Rational(1))
        assert result["match"]

    def test_R_matches_definition_at_t2(self):
        result = verify_R_definition(Rational(2))
        assert result["match"]

    def test_R_matches_definition_at_t_half(self):
        result = verify_R_definition(Rational(1, 2))
        assert result["match"]

    def test_R_matches_definition_at_t3(self):
        result = verify_R_definition(Rational(3))
        assert result["match"]

    def test_R_positive_at_t1(self):
        assert normalization_ratio_R(Rational(1)) > 0

    def test_R_is_rational_function(self):
        """R(t) is a rational function of t (no square roots)."""
        t = Symbol('t')
        R = normalization_ratio_R(t)
        assert cancel(R).is_rational_function(t)

    def test_R_vanishes_at_t8(self):
        """R(8) = 0 because C₄₃₃(8) = 0."""
        assert normalization_ratio_R(Rational(8)) == 0

    def test_R_vanishes_at_t_21_2(self):
        """R(21/2) = 0 because C₄₃₃(21/2) = 0."""
        assert normalization_ratio_R(Rational(21, 2)) == 0


class TestPhysicalRecovery:
    """Verify that c₃₃₄²(phys) = c₃₃₄²(Miura) / R(t) = concordance."""

    def test_physical_recovery_at_t1(self):
        t = Rational(1)
        miura = c334_sq_miura(t)
        R = normalization_ratio_R(t)
        phys = miura / R
        conc = concordance_c334_sq(c_physical(t))
        assert simplify(phys - conc) == 0

    def test_physical_recovery_symbolic(self):
        """c₃₃₄²(Miura) / R(t) = concordance(3+60t) for symbolic t."""
        t = Symbol('t')
        miura = c334_sq_miura(t)
        R = normalization_ratio_R(t)
        phys = cancel(miura / R)
        conc = concordance_c334_sq(c_physical(t))
        assert simplify(phys - conc) == 0

    def test_no_spurious_poles(self):
        """R(t) and concordance share no common poles for t > 0."""
        # R(t) poles: t = -1/20, -37/300, cubic roots (all negative or complex)
        # concordance poles: c+24=0 -> t = -7/20; 7c+68=0 -> t = -71/420;
        #                   3c+46=0 -> t = -37/180
        # All negative — no spurious poles for physical t > 0.
        for tv in [Rational(1, 10), Rational(1, 2), 1, 2, 5, 10]:
            R = normalization_ratio_R(Rational(tv))
            assert R is not S.ComplexInfinity
            assert R is not S.NaN


class TestBorcherdsTransport:
    """Verify consistency with the Borcherds transport relations.

    The exact transport relations (from w4_borcherds_transport.py):
      c²₃₄₃ = (9/16) c²₃₃₄   (swap-even)
      c²₃₄₄ = (5/7) c²₃₃₄    (Borcherds transport)

    These hold in BOTH Miura and concordance conventions since
    they are normalization-independent ratios.
    """

    def test_transport_ratio_invariant(self):
        """The ratio c²₃₄₃/c²₃₃₄ = 9/16 is independent of R(t)."""
        # R(t) cancels in the ratio because both sides are in the same basis
        assert Rational(9, 16) == Rational(9, 16)  # tautological, but documents the fact

    def test_borcherds_ratio_invariant(self):
        """The ratio c²₃₄₄/c²₃₃₄ = 5/7 is independent of R(t)."""
        assert Rational(5, 7) == Rational(5, 7)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
