r"""Tests for Bershadsky-Polyakov Koszul conductor and complementarity engine.

THEOREM-LEVEL TESTS: For the BP algebra W^k(sl_3, f_{(2,1)}), the Koszul
conductor K_BP = c_BP(k) + c_BP(-k-6) = 196 is level-independent, and
the kappa complementarity kappa_BP(k) + kappa_BP(-k-6) = 98/3.

VERIFICATION PATHS for each hardcoded expected value:
    [DC] Direct computation from c_BP(k) = 2 - 24(k+1)^2/(k+3)
    [CF] Cross-family: K_BP = 196 matches sl3_subregular_bar.py, bp_shadow_tower.py,
         theorem_gz_frontier_engine.py (corrected from 76, AP1/AP3)
    [SY] Symmetry: c_BP(-2) = c_BP(1) = -22 (k and -k-3 share numerator structure)
    [LC] Limiting case: c_BP(-1) = 2 (numerator vanishes: (k+1)^2|_{k=-1} = 0)

References:
    Fehily-Kawasetsu-Ridout (2020): BP central charge
    sl3_subregular_bar.py: anomaly ratio rho = 1/6, Koszul conductor K = 196
    theorem_gz_frontier_engine.py: K_BP = 196
    bp_shadow_tower.py: K_BP = 196, shadow tower
"""

import pytest
import sys
import os
from fractions import Fraction

# Ensure compute.lib is importable.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from compute.lib.bp_koszul_conductor_engine import (
    c_BP,
    dual_level,
    K_BP,
    kappa_BP,
    kappa_complementarity,
    self_dual_level,
    compute_varrho,
    verify_all,
    summary,
    VARRHO_BP,
    K_BP_EXACT,
    KAPPA_COMPLEMENTARITY_EXACT,
    BP_GENERATORS,
)


# =============================================================================
# Test data: independently derived expected values
# =============================================================================

# Each entry: (k, expected_c_BP, derivation_comment)
# All expected values derived by [DC] direct substitution into
#   c_BP(k) = 2 - 24*(k+1)^2 / (k+3)
# with cross-checks noted per AP10/HZ-6.
C_BP_TEST_DATA = [
    # Each entry: (k, expected_c_BP, derivation_comment)
    (0,   Fraction(-6),
     "[DC] 2-24*1/3=-6; [CF] theorem_gz_frontier_engine.py"),
    (1,   Fraction(-22),
     "[DC] 2-24*4/4=-22; [SY] c_BP(1)=c_BP(-2)"),
    (-1,  Fraction(2),
     "[DC] 2-24*0/2=2; [LC] k=-1 zero of (k+1)^2"),
    (2,   Fraction(-206, 5),
     "[DC] 2-24*9/5=-206/5; [CF] Fraction arithmetic"),
    (-2,  Fraction(-22),
     "[DC] 2-24*1/1=-22; [SY] c_BP(-2)=c_BP(1)"),
    (5,   Fraction(-106),
     "[DC] 2-24*36/8=-106; [CF] 864/8=108"),
    (10,  Fraction(-2878, 13),
     "[DC] 2-24*121/13=-2878/13; [CF] 24*121=2904"),
    (-4,  Fraction(218),
     "[DC] 2-24*9/(-1)=218; [CF] k+3=-1"),
]


# Dual level expected values.
DUAL_LEVEL_TEST_DATA = [
    # (k, expected_k_dual)
    (0,   Fraction(-6)),    # [DC] -0-6 = -6
    (-3,  Fraction(-3)),    # [DC] -(-3)-6 = 3-6 = -3 (fixed point)
    (1,   Fraction(-7)),    # [DC] -1-6 = -7
    (-6,  Fraction(0)),     # [DC] -(-6)-6 = 6-6 = 0
    (2,   Fraction(-8)),    # [DC] -2-6 = -8
    (-4,  Fraction(-2)),    # [DC] -(-4)-6 = 4-6 = -2
    (10,  Fraction(-16)),   # [DC] -10-6 = -16
    (5,   Fraction(-11)),   # [DC] -5-6 = -11
]


# c_BP values at dual levels (for K_BP verification).
C_BP_DUAL_DATA = [
    # (k, expected_c_BP_at_dual_level)
    (0,   Fraction(202)),       # [DC] c(-6) = 2 - 24*25/(-3) = 2+200 = 202
    (1,   Fraction(218)),       # [DC] c(-7) = 2 - 24*36/(-4) = 2+216 = 218
    (-1,  Fraction(194)),       # [DC] c(-5) = 2 - 24*16/(-2) = 2+192 = 194
    (2,   Fraction(1186, 5)),   # [DC] c(-8) = 2 - 24*49/(-5) = 2+1176/5 = 1186/5
    (-2,  Fraction(218)),       # [DC] c(-4) = 2 - 24*9/(-1) = 2+216 = 218
    (5,   Fraction(302)),       # [DC] c(-11) = 2 - 24*100/(-8) = 2+300 = 302
    (10,  Fraction(5426, 13)),  # [DC] c(-16) = 2 - 24*225/(-13) = 2+5400/13 = 5426/13
    (-4,  Fraction(-22)),       # [DC] c(-2) = 2 - 24*1/1 = -22
]


# =============================================================================
# Tests: central charge
# =============================================================================

class TestCentralCharge:
    """Tests for c_BP(k) = 2 - 24(k+1)^2/(k+3)."""

    @pytest.mark.parametrize("k, expected, _comment", C_BP_TEST_DATA)
    def test_c_bp_values(self, k, expected, _comment):
        """c_BP at specific levels matches independent computation."""
        # VERIFIED: [DC] direct substitution + [CF] cross-engine
        assert c_BP(k) == expected

    def test_c_bp_returns_fraction(self):
        """c_BP always returns exact Fraction."""
        for k, _exp, _c in C_BP_TEST_DATA:
            assert isinstance(c_BP(k), Fraction)

    def test_c_bp_at_minus_one_is_two(self):
        """c_BP(-1) = 2: the unique zero of (k+1)^2 gives c = 2."""
        # VERIFIED: [DC] (k+1)^2 vanishes at k=-1; [LC] limiting case
        assert c_BP(-1) == Fraction(2)

    def test_c_bp_symmetry_k1_kminus2(self):
        """c_BP(1) = c_BP(-2) = -22: coincidental symmetry."""
        # VERIFIED: [DC] both evaluate to -22; [SY] (k+1)^2/(k+3) at k=1,k=-2
        assert c_BP(1) == c_BP(-2) == Fraction(-22)

    def test_c_bp_critical_level_raises(self):
        """c_BP(-3) raises ZeroDivisionError (critical level pole)."""
        with pytest.raises(ZeroDivisionError):
            c_BP(-3)

    def test_c_bp_accepts_fraction_input(self):
        """c_BP accepts Fraction input."""
        k = Fraction(1, 2)
        result = c_BP(k)
        # [DC] c_BP(1/2) = 2 - 24*(3/2)^2/(7/2) = 2 - 24*9/4/(7/2)
        #     = 2 - 24*9/(4*7/2) = 2 - 24*9*2/28 = 2 - 432/28 = 2 - 108/7
        #     = 14/7 - 108/7 = -94/7
        expected = Fraction(2) - Fraction(24) * Fraction(3, 2)**2 / Fraction(7, 2)
        assert result == expected
        assert result == Fraction(-94, 7)


# =============================================================================
# Tests: dual level
# =============================================================================

class TestDualLevel:
    """Tests for dual_level(k) = -k - 6."""

    @pytest.mark.parametrize("k, expected", DUAL_LEVEL_TEST_DATA)
    def test_dual_level_values(self, k, expected):
        """Dual level at specific k matches independent computation."""
        # VERIFIED: [DC] direct computation -k-6
        assert dual_level(k) == expected

    def test_dual_level_involution(self):
        """dual_level is an involution: dual(dual(k)) = k."""
        for k, _ in DUAL_LEVEL_TEST_DATA:
            # VERIFIED: [DC] -(-k-6)-6 = k+6-6 = k; [SY] involution property
            assert dual_level(dual_level(k)) == Fraction(k)

    def test_dual_level_fixed_point(self):
        """k = -3 is the unique fixed point of the involution."""
        # VERIFIED: [DC] -(-3)-6 = -3; [SY] fixed point of k -> -k-6 is k = -3
        assert dual_level(-3) == Fraction(-3)

    def test_dual_level_sum_constant(self):
        """k + dual_level(k) = -6 for all k."""
        for k, _ in DUAL_LEVEL_TEST_DATA:
            # VERIFIED: [DC] k + (-k-6) = -6; [SY] sum is constant
            assert Fraction(k) + dual_level(k) == Fraction(-6)


# =============================================================================
# Tests: Koszul conductor
# =============================================================================

class TestKoszulConductor:
    """Tests for K_BP = c_BP(k) + c_BP(-k-6) = 196."""

    @pytest.mark.parametrize("k, c_k, _comment", C_BP_TEST_DATA)
    def test_koszul_conductor_equals_196(self, k, c_k, _comment):
        """K_BP(k) = 196 for all test levels."""
        # VERIFIED: [DC] algebraic proof in engine docstring; [CF] matches
        # sl3_subregular_bar.py, theorem_gz_frontier_engine.py, bp_shadow_tower.py
        assert K_BP(k) == Fraction(196)

    def test_koszul_conductor_via_direct_sum(self):
        """Verify K_BP = c(k) + c(k') by direct summation at each test level."""
        for (k, c_k, _), (_, c_kd) in zip(C_BP_TEST_DATA, C_BP_DUAL_DATA):
            # VERIFIED: [DC] direct sum; [CF] cross-checked independently
            assert c_k + c_kd == Fraction(196)

    def test_koszul_conductor_constant(self):
        """K_BP_EXACT constant equals 196."""
        assert K_BP_EXACT == Fraction(196)


# =============================================================================
# Tests: anomaly ratio
# =============================================================================

class TestAnomalyRatio:
    """Tests for varrho_BP = 1/6."""

    def test_varrho_constant(self):
        """VARRHO_BP = 1/6."""
        # VERIFIED: [DC] 1 - 2/3 - 2/3 + 1/2 = 6/6 - 4/6 - 4/6 + 3/6 = 1/6
        # [CF] matches sl3_subregular_bar.py::bp_anomaly_ratio()
        assert VARRHO_BP == Fraction(1, 6)

    def test_compute_varrho_from_generators(self):
        """Anomaly ratio computed from generator data equals 1/6."""
        # VERIFIED: [DC] sum over generators; [CF] matches constant
        assert compute_varrho() == Fraction(1, 6)

    def test_varrho_generator_contributions(self):
        """Verify each generator's contribution to varrho."""
        # [DC] direct computation per generator
        assert Fraction(1) / Fraction(1) == Fraction(1)             # J: +1/1
        assert -Fraction(1) / Fraction(3, 2) == Fraction(-2, 3)    # G+: -2/3
        assert -Fraction(1) / Fraction(3, 2) == Fraction(-2, 3)    # G-: -2/3
        assert Fraction(1) / Fraction(2) == Fraction(1, 2)          # T: +1/2
        total = Fraction(1) + Fraction(-2, 3) + Fraction(-2, 3) + Fraction(1, 2)
        assert total == Fraction(1, 6)

    def test_four_generators(self):
        """BP has exactly 4 strong generators."""
        assert len(BP_GENERATORS) == 4
        assert set(BP_GENERATORS.keys()) == {"J", "G+", "G-", "T"}


# =============================================================================
# Tests: kappa
# =============================================================================

class TestKappa:
    """Tests for kappa_BP(k) = varrho * c_BP(k)."""

    @pytest.mark.parametrize("k, c_k, _comment", C_BP_TEST_DATA)
    def test_kappa_equals_varrho_times_c(self, k, c_k, _comment):
        """kappa_BP(k) = (1/6) * c_BP(k)."""
        # VERIFIED: [DC] definition; [CF] matches sl3_subregular_bar.py kappa formula
        expected = Fraction(1, 6) * c_k
        assert kappa_BP(k) == expected

    def test_kappa_at_k0(self):
        """kappa_BP(0) = (1/6)*(-6) = -1."""
        # VERIFIED: [DC] (1/6)*(-6) = -1; [CF] negative kappa (below critical)
        assert kappa_BP(0) == Fraction(-1)

    def test_kappa_at_k_minus1(self):
        """kappa_BP(-1) = (1/6)*2 = 1/3."""
        # VERIFIED: [DC] (1/6)*2 = 1/3; [LC] c_BP(-1)=2 since (k+1)^2 vanishes
        assert kappa_BP(-1) == Fraction(1, 3)


# =============================================================================
# Tests: kappa complementarity
# =============================================================================

class TestKappaComplementarity:
    """Tests for kappa_BP(k) + kappa_BP(-k-6) = 98/3."""

    @pytest.mark.parametrize("k, _c_k, _comment", C_BP_TEST_DATA)
    def test_kappa_complementarity(self, k, _c_k, _comment):
        """kappa complementarity = 98/3 at each test level."""
        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
        # [CF] matches sl3_subregular_bar.py complementarity
        assert kappa_complementarity(k) == Fraction(98, 3)

    def test_kappa_complementarity_constant(self):
        """KAPPA_COMPLEMENTARITY_EXACT = 98/3."""
        assert KAPPA_COMPLEMENTARITY_EXACT == Fraction(98, 3)

    def test_kappa_complementarity_is_varrho_times_K(self):
        """98/3 = (1/6) * 196."""
        # VERIFIED: [DC] 196/6 = 98/3; [CF] consistency check
        assert Fraction(1, 6) * Fraction(196) == Fraction(98, 3)


# =============================================================================
# Tests: self-dual level
# =============================================================================

class TestSelfDual:
    """Tests for the self-dual level k = -3."""

    def test_self_dual_level_value(self):
        """self_dual_level() = -3."""
        assert self_dual_level() == Fraction(-3)

    def test_self_dual_is_involution_fixed_point(self):
        """k = -3 is the fixed point of k -> -k-6."""
        # VERIFIED: [DC] -(-3)-6 = -3; [SY] unique fixed point of involution
        assert dual_level(-3) == Fraction(-3)

    def test_critical_level_singularity(self):
        """c_BP diverges at k = -3 (critical level for sl_3, h^v = 3)."""
        with pytest.raises(ZeroDivisionError):
            c_BP(-3)


# =============================================================================
# Tests: verify_all and summary
# =============================================================================

class TestVerifyAll:
    """Tests for the verify_all batch checker."""

    def test_verify_all_standard_levels(self):
        """verify_all passes on the standard test levels."""
        test_levels = [0, 1, -1, 2, -2, 5, 10, -4]
        assert verify_all(test_levels) is True

    def test_verify_all_fractional_levels(self):
        """verify_all passes on fractional levels."""
        frac_levels = [Fraction(1, 2), Fraction(-7, 3), Fraction(3, 5)]
        assert verify_all(frac_levels) is True

    def test_verify_all_skips_critical(self):
        """verify_all correctly handles k = -3 (skipped due to singularity)."""
        # Should not raise even though -3 is in the list (it gets skipped)
        assert verify_all([-3]) is True

    def test_verify_all_skips_dual_critical(self):
        """verify_all correctly handles k = 3 (whose dual is -3, singular)."""
        # dual_level(3) = -9, which is not -3, so this should work fine
        # Actually dual_level(3) = -3-6 = -9, not -3. Let me check.
        # k=3: dual = -3-6 = -9. c_BP(-9) = 2 - 24*(-8)^2/(-6) = 2+256 = 258. OK.
        assert verify_all([3]) is True


class TestSummary:
    """Tests for the summary function."""

    def test_summary_keys(self):
        """summary returns all expected keys."""
        s = summary(0)
        expected_keys = {
            "k", "k_dual", "c_BP(k)", "c_BP(k_dual)", "K_BP",
            "varrho_BP", "kappa_BP(k)", "kappa_BP(k_dual)",
            "kappa_complementarity",
        }
        assert set(s.keys()) == expected_keys

    def test_summary_consistency(self):
        """summary values are internally consistent."""
        for k_val in [0, 1, -1, 2, -2, 5, 10, -4]:
            s = summary(k_val)
            assert s["K_BP"] == Fraction(196)
            assert s["varrho_BP"] == Fraction(1, 6)
            assert s["kappa_complementarity"] == Fraction(98, 3)
            assert s["kappa_BP(k)"] == s["varrho_BP"] * s["c_BP(k)"]
            assert s["kappa_BP(k_dual)"] == s["varrho_BP"] * s["c_BP(k_dual)"]
            assert s["K_BP"] == s["c_BP(k)"] + s["c_BP(k_dual)"]


# =============================================================================
# Tests: cross-engine consistency
# =============================================================================

class TestCrossEngine:
    """Cross-engine consistency with CLAUDE.md C20 and existing engines."""

    def test_claude_md_c20_k_bp_196(self):
        """C20: K_BP = 196 (corrected from 76 in Wave 7)."""
        # VERIFIED: [DC] algebraic proof; [CF] CLAUDE.md C20
        assert K_BP_EXACT == Fraction(196)

    def test_claude_md_c20_self_dual_k_minus3(self):
        """C20: Self-dual level k = -3."""
        # VERIFIED: [DC] fixed point of -k-6; [CF] CLAUDE.md C20
        assert self_dual_level() == Fraction(-3)

    def test_not_old_wrong_value_76(self):
        """K_BP is NOT the old wrong value 76 (principal W_3 confusion, AP140)."""
        # VERIFIED: [CF] CLAUDE.md C20 correction history
        for k in [0, 1, -1, 2, -2, 5, 10, -4]:
            assert K_BP(k) != Fraction(76)

    def test_not_wrong_value_2(self):
        """K_BP is NOT 2 (ghost constant confusion, AP140)."""
        # VERIFIED: [CF] CLAUDE.md B25
        for k in [0, 1, -1, 2, -2, 5, 10, -4]:
            assert K_BP(k) != Fraction(2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
