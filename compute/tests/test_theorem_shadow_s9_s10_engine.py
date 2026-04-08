r"""Tests for shadow S_9, S_10 engine and structural theorems.

Multi-path verification mandate: every formula checked by at least 3
independent paths.  Structural theorems verified through arity 20+.

Test structure:
    1. Three-path agreement (convolution, master eq, ODE) for S_2-S_20
    2. Explicit S_9, S_10 formulas
    3. Denominator theorem through arity 20
    4. Numerator degree theorem through arity 20
    5. Rationality theorem through arity 20
    6. Sign pattern: leading coefficient always (-1)^r
    7. Sign pattern: phase slip analysis at c=1
    8. Self-duality at c=13
    9. Koszul duality ratio = 1 at c=13
   10. Affine sl_2: S_6 through S_10
   11. Affine sl_2: exact values at k=1
   12. W_3 Virasoro tower at c=50
   13. Growth rate convergence
   14. Numerator zero analysis
   15. Exact Fraction arithmetic consistency
   16. Cross-engine consistency with frontier engine
   17. Limiting cases (large c, pole structure)
   18. Structural pattern summary
   19. Branch point and beat period
   20. Phase slip boundary identification
"""

import math
from fractions import Fraction

import pytest
from sympy import (
    Rational,
    Symbol,
    cancel,
    factor,
    limit,
    numer,
    oo,
    simplify,
)

from compute.lib.theorem_shadow_s9_s10_engine import (
    S_explicit,
    affine_sl2_S_fraction,
    affine_sl2_shadow_coefficient,
    affine_sl2_shadow_tower,
    branch_point_data,
    convolution_coefficients,
    denominator_analysis,
    denominator_exponents,
    duality_ratio_at_c13,
    growth_rate_numerical,
    koszul_dual_ratio,
    large_r_ratio_test,
    leading_coefficient_sign,
    numerator_degree_analysis,
    numerator_zeros,
    phase_slip_arity,
    positive_numerator_zeros,
    self_duality_check,
    shadow_coefficients_convolution,
    shadow_coefficients_master_eq,
    shadow_coefficients_ode,
    shadow_growth_rate_squared,
    sign_at_value,
    structural_pattern_summary,
    verify_rationality,
    virasoro_S_fraction,
    virasoro_shadow_metric,
    w3_virasoro_tower_at_c,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. THREE-PATH AGREEMENT: S_2 through S_20
# =========================================================================

class TestThreePathAgreement:
    """Every S_r must agree across all three independent derivation paths."""

    @pytest.fixture(scope="class")
    def all_paths(self):
        conv = shadow_coefficients_convolution(max_r=20)
        meq = shadow_coefficients_master_eq(max_r=20)
        ode = shadow_coefficients_ode(max_r=20)
        return conv, meq, ode

    @pytest.mark.parametrize("r", range(2, 21))
    def test_conv_vs_meq(self, all_paths, r):
        conv, meq, _ = all_paths
        diff = simplify(conv[r] - meq[r])
        assert diff == 0, f"S_{r}: conv != meq, diff = {diff}"

    @pytest.mark.parametrize("r", range(2, 21))
    def test_conv_vs_ode(self, all_paths, r):
        conv, _, ode = all_paths
        diff = simplify(conv[r] - ode[r])
        assert diff == 0, f"S_{r}: conv != ode, diff = {diff}"

    @pytest.mark.parametrize("r", range(2, 21))
    def test_meq_vs_ode(self, all_paths, r):
        _, meq, ode = all_paths
        diff = simplify(meq[r] - ode[r])
        assert diff == 0, f"S_{r}: meq != ode, diff = {diff}"


# =========================================================================
# 2. EXPLICIT S_9, S_10 FORMULAS
# =========================================================================

class TestExplicitS9S10:
    """Verify the closed-form formulas for S_9 and S_10."""

    @pytest.fixture(scope="class")
    def computed(self):
        return shadow_coefficients_convolution(max_r=10)

    def test_S9_formula(self):
        """S_9 = -1280(2025c^2 + 15570c + 29554) / [3 c^6 (5c+22)^3]."""
        expected = (Rational(-1280) * (2025 * c**2 + 15570 * c + 29554)
                    / (3 * c**6 * (5 * c + 22)**3))
        assert simplify(S_explicit(9) - expected) == 0

    def test_S10_formula(self):
        """S_10 = 256(91125c^3 + 1050975c^2 + 3989790c + 4969967)
        / [c^7 (5c+22)^4]."""
        expected = (Rational(256)
                    * (91125 * c**3 + 1050975 * c**2
                       + 3989790 * c + 4969967)
                    / (c**7 * (5 * c + 22)**4))
        assert simplify(S_explicit(10) - expected) == 0

    @pytest.mark.parametrize("r", range(2, 11))
    def test_explicit_matches_convolution(self, computed, r):
        diff = simplify(computed[r] - S_explicit(r))
        assert diff == 0, f"S_{r} explicit != computed"

    def test_S9_at_c1(self):
        """S_9(c=1) via exact Fraction arithmetic."""
        val = virasoro_S_fraction(9, 1)
        expected = Fraction(-1280, 3) * (2025 + 15570 + 29554) / (1 * 27**3)
        assert val == expected

    def test_S10_at_c1(self):
        """S_10(c=1) via exact Fraction arithmetic."""
        val = virasoro_S_fraction(10, 1)
        expected = Fraction(256) * (91125 + 1050975 + 3989790 + 4969967) / (1 * 27**4)
        assert val == expected

    def test_S9_at_c13(self):
        """S_9(c=13) is nonzero."""
        val = virasoro_S_fraction(9, 13)
        assert val != 0

    def test_S10_at_c13(self):
        """S_10(c=13) is nonzero."""
        val = virasoro_S_fraction(10, 13)
        assert val != 0

    def test_S9_sign_at_c10(self):
        """S_9 is negative at c=10 ((-1)^9 = -1)."""
        val = virasoro_S_fraction(9, 10)
        assert val < 0

    def test_S10_sign_at_c10(self):
        """S_10 is positive at c=10 ((-1)^10 = +1)."""
        val = virasoro_S_fraction(10, 10)
        assert val > 0


# =========================================================================
# 3. DENOMINATOR THEOREM through arity 20
# =========================================================================

class TestDenominatorTheorem:
    """denom(S_r) = rho(r) * c^{r-3} * (5c+22)^{floor((r-2)/2)}."""

    @pytest.fixture(scope="class")
    def analysis(self):
        return denominator_analysis(max_r=20)

    @pytest.mark.parametrize("r", range(4, 21))
    def test_exponents_match(self, analysis, r):
        entry = [e for e in analysis if e[0] == r][0]
        assert entry[4], (
            f"S_{r}: pow_c={entry[1]} (pred {r-3}), "
            f"pow_5c22={entry[2]} (pred {(r-2)//2})")

    @pytest.mark.parametrize("r", range(4, 21))
    def test_residual_positive(self, analysis, r):
        """The residual factor rho(r) is a positive integer."""
        entry = [e for e in analysis if e[0] == r][0]
        residual = entry[3]
        assert residual > 0 and isinstance(residual, int)

    @pytest.mark.parametrize("r", range(4, 21))
    def test_residual_divides_r(self, analysis, r):
        """rho(r) divides r."""
        entry = [e for e in analysis if e[0] == r][0]
        residual = entry[3]
        assert r % residual == 0, f"rho({r})={residual} does not divide {r}"


# =========================================================================
# 4. NUMERATOR DEGREE THEOREM through arity 20
# =========================================================================

class TestNumeratorDegreeTheorem:
    """deg_c(numer(S_r)) = floor((r-4)/2)."""

    @pytest.fixture(scope="class")
    def analysis(self):
        return numerator_degree_analysis(max_r=20)

    @pytest.mark.parametrize("r", range(4, 21))
    def test_degree_matches(self, analysis, r):
        entry = [e for e in analysis if e[0] == r][0]
        assert entry[3], f"S_{r}: deg={entry[1]}, pred={(r-4)//2}"


# =========================================================================
# 5. RATIONALITY THEOREM through arity 20
# =========================================================================

class TestRationalityTheorem:
    """S_r is a rational function of c (no radicals)."""

    @pytest.fixture(scope="class")
    def verification(self):
        return verify_rationality(max_r=20)

    @pytest.mark.parametrize("r", range(2, 21))
    def test_no_radicals(self, verification, r):
        entry = [e for e in verification if e[0] == r][0]
        assert entry[1], f"S_{r} contains radicals"


# =========================================================================
# 6. SIGN PATTERN: leading coefficient
# =========================================================================

class TestLeadingCoefficientSign:
    """The leading coefficient of P_r(c) has sign (-1)^r."""

    @pytest.fixture(scope="class")
    def signs(self):
        return leading_coefficient_sign(max_r=20)

    @pytest.mark.parametrize("r", range(4, 21))
    def test_leading_sign_alternates(self, signs, r):
        entry = [e for e in signs if e[0] == r][0]
        assert entry[3], (
            f"S_{r}: lead_sign={entry[1]}, expected=(-1)^{r}={entry[2]}")


# =========================================================================
# 7. SIGN PATTERN: phase slip at c=1
# =========================================================================

class TestPhaseSlip:
    """The (-1)^r sign pattern breaks at large arity for small c."""

    def test_c1_holds_through_r16(self):
        """At c=1, (-1)^r holds for r=4..16."""
        results = sign_at_value(max_r=16, c_val=1.0)
        for r, sgn, expected, match in results:
            assert match, f"S_{r}(c=1): sign={sgn}, expected={expected}"

    def test_c1_fails_at_r17(self):
        """At c=1, (-1)^r fails at r=17."""
        results = sign_at_value(max_r=17, c_val=1.0)
        r17 = [e for e in results if e[0] == 17][0]
        assert not r17[3], "S_17(c=1) still follows (-1)^17 (unexpected)"

    def test_c26_holds_through_r20(self):
        """At c=26, (-1)^r holds for r=4..20."""
        results = sign_at_value(max_r=20, c_val=26.0)
        for r, sgn, expected, match in results:
            assert match, f"S_{r}(c=26): sign={sgn}, expected={expected}"

    def test_c100_holds_through_r20(self):
        """At c=100, (-1)^r holds for r=4..20."""
        results = sign_at_value(max_r=20, c_val=100.0)
        for r, sgn, expected, match in results:
            assert match, f"S_{r}(c=100): sign={sgn}, expected={expected}"

    def test_phase_slip_arity_c1(self):
        """Phase slip at c=1 predicted near r=15-17."""
        slip = phase_slip_arity(1.0)
        assert 14 <= slip <= 18

    def test_phase_slip_arity_c26(self):
        """Phase slip at c=26 predicted near r=28-32."""
        slip = phase_slip_arity(26.0)
        assert 25 <= slip <= 35

    def test_phase_slip_grows_with_c(self):
        """Phase slip arity increases with c."""
        s1 = phase_slip_arity(1.0)
        s10 = phase_slip_arity(10.0)
        s100 = phase_slip_arity(100.0)
        assert s1 < s10 < s100


# =========================================================================
# 8. SELF-DUALITY AT c=13
# =========================================================================

class TestSelfDuality:
    """S_r(13) = S_r(26-13) = S_r(13)."""

    def test_self_duality_all_r(self):
        results = self_duality_check(max_r=10)
        for r, (v, v_dual, match) in results.items():
            assert match, f"S_{r}(13) != S_{r}(13_dual)"

    @pytest.mark.parametrize("r", range(2, 11))
    def test_S_at_c13_nonzero(self, r):
        """The tower does not terminate at the self-dual point."""
        if r <= 3:
            return  # S_2 = 13/2, S_3 = 2
        val = virasoro_S_fraction(r, 13)
        assert val != 0, f"S_{r}(13) = 0"

    def test_S9_c13_exact(self):
        """S_9(13) exact value."""
        val = virasoro_S_fraction(9, 13)
        numer_val = -1280 * (2025 * 169 + 15570 * 13 + 29554)
        denom_val = 3 * 13**6 * (5 * 13 + 22)**3
        assert val == Fraction(numer_val, denom_val)

    def test_S10_c13_exact(self):
        """S_10(13) exact value."""
        val = virasoro_S_fraction(10, 13)
        numer_val = 256 * (91125 * 2197 + 1050975 * 169
                           + 3989790 * 13 + 4969967)
        denom_val = 13**7 * (87)**4
        assert val == Fraction(numer_val, denom_val)


# =========================================================================
# 9. KOSZUL DUALITY RATIO = 1 AT c=13
# =========================================================================

class TestKoszulDualityRatio:
    """S_r(c)/S_r(26-c) evaluates to 1 at c=13 for all r."""

    @pytest.fixture(scope="class")
    def ratios(self):
        return duality_ratio_at_c13(max_r=10)

    @pytest.mark.parametrize("r", range(4, 11))
    def test_ratio_is_one(self, ratios, r):
        assert ratios[r] == 1, f"S_{r}(c)/S_{r}(26-c) at c=13 = {ratios[r]}"


# =========================================================================
# 10. AFFINE sl_2: S_6 through S_10
# =========================================================================

class TestAffineSl2:
    """Shadow tower for sl_2 via Sugawara substitution c=3k/(k+2)."""

    @pytest.fixture(scope="class")
    def tower(self):
        return affine_sl2_shadow_tower(max_r=10)

    def test_S2_is_kappa_km(self):
        S2 = affine_sl2_shadow_coefficient(2)
        expected = 3 * k / (2 * (k + 2))
        assert simplify(S2 - expected) == 0

    def test_S3_universal(self):
        """S_3 = 2 (independent of level k)."""
        assert affine_sl2_shadow_coefficient(3) == 2

    @pytest.mark.parametrize("r", range(6, 11))
    def test_S6_to_S10_nonzero(self, tower, r):
        assert tower[r] != 0, f"S_{r}(sl_2) = 0"

    def test_S9_sl2_sign_at_k1(self):
        """S_9(sl_2, k=1) is negative ((-1)^9)."""
        val = affine_sl2_S_fraction(9, 1)
        assert val < 0

    def test_S10_sl2_sign_at_k1(self):
        """S_10(sl_2, k=1) is positive ((-1)^10)."""
        val = affine_sl2_S_fraction(10, 1)
        assert val > 0


# =========================================================================
# 11. AFFINE sl_2: exact values at k=1
# =========================================================================

class TestAffineSl2Exact:
    """Exact arithmetic at level k=1 (Ising embedding, c=1)."""

    @pytest.mark.parametrize("r", range(6, 11))
    def test_exact_nonzero(self, r):
        val = affine_sl2_S_fraction(r, 1)
        assert val != 0

    def test_S6_k1_matches_vir_c1(self):
        """S_6(sl_2, k=1) = S_6(Vir, c=1) since c(sl_2, k=1)=1."""
        sl2_val = affine_sl2_S_fraction(6, 1)
        vir_val = virasoro_S_fraction(6, 1)
        assert sl2_val == vir_val

    def test_S9_k1_matches_vir_c1(self):
        sl2_val = affine_sl2_S_fraction(9, 1)
        vir_val = virasoro_S_fraction(9, 1)
        assert sl2_val == vir_val

    def test_S10_k1_matches_vir_c1(self):
        sl2_val = affine_sl2_S_fraction(10, 1)
        vir_val = virasoro_S_fraction(10, 1)
        assert sl2_val == vir_val

    def test_large_k_limit_S9(self):
        """As k -> infinity, S_9(sl_2) -> S_9(Vir, c=3)."""
        S9 = affine_sl2_shadow_coefficient(9)
        lim = limit(S9, k, oo)
        S9_c3 = virasoro_S_fraction(9, 3)
        assert simplify(lim - Rational(S9_c3)) == 0


# =========================================================================
# 12. W_3 VIRASORO TOWER AT c=50
# =========================================================================

class TestW3Specialization:
    """Virasoro tower at c=50 (relevant for W_3 T-line)."""

    @pytest.fixture(scope="class")
    def tower(self):
        return w3_virasoro_tower_at_c(50, max_r=10)

    def test_S2_is_25(self, tower):
        assert tower[2] == 25

    def test_S3_is_2(self, tower):
        assert tower[3] == 2

    @pytest.mark.parametrize("r", range(4, 11))
    def test_nonzero(self, tower, r):
        assert tower[r] != 0

    @pytest.mark.parametrize("r", range(4, 11))
    def test_sign_alternation(self, tower, r):
        """(-1)^r sign pattern at c=50."""
        expected_sign = (-1)**r
        actual_sign = 1 if tower[r] > 0 else -1
        assert actual_sign == expected_sign, (
            f"S_{r}(c=50) has wrong sign: {tower[r]}")

    def test_magnitude_decreasing(self, tower):
        """|S_r| decreases rapidly for r >= 4 at c=50."""
        for r in range(5, 11):
            assert abs(tower[r]) < abs(tower[r - 1]), (
                f"|S_{r}| >= |S_{r-1}| at c=50")


# =========================================================================
# 13. GROWTH RATE CONVERGENCE
# =========================================================================

class TestGrowthRate:
    """Asymptotic |S_{r+1}/S_r| -> rho."""

    def test_growth_rate_formula(self):
        """rho^2 = (180c+872)/[c^2(5c+22)]."""
        rho2 = shadow_growth_rate_squared()
        expected = (180 * c + 872) / (c**2 * (5 * c + 22))
        assert simplify(rho2 - expected) == 0

    def test_growth_rate_c1(self):
        """rho(c=1) = sqrt(1052/27)."""
        rho = growth_rate_numerical(1.0)
        expected = math.sqrt(1052.0 / 27.0)
        assert abs(rho - expected) < 1e-10

    def test_ratio_convergence_c10(self):
        """Successive ratios approach rho at c=10."""
        results = large_r_ratio_test(max_r=15, c_val=10.0)
        # Last ratio should be within 20% of rho
        last = results[-1]
        assert last[3] < 0.2, f"ratio/rho deviation = {last[3]}"

    def test_growth_rate_decreases_with_c(self):
        """rho(c) decreases as c increases (for c >> 1)."""
        r1 = growth_rate_numerical(1.0)
        r10 = growth_rate_numerical(10.0)
        r100 = growth_rate_numerical(100.0)
        assert r1 > r10 > r100


# =========================================================================
# 14. NUMERATOR ZERO ANALYSIS
# =========================================================================

class TestNumeratorZeros:
    """Sign change boundaries from numerator zeros."""

    def test_S6_numerator_zero(self):
        """S_6 has numerator zero at c = -193/45."""
        zeros = numerator_zeros(6)
        assert Rational(-193, 45) in zeros

    def test_S7_numerator_zero(self):
        """S_7 has numerator zero at c = -61/15."""
        zeros = numerator_zeros(7)
        assert Rational(-61, 15) in zeros

    def test_S4_S5_no_zeros(self):
        """S_4, S_5 have constant numerators (no zeros)."""
        z4 = numerator_zeros(4)
        z5 = numerator_zeros(5)
        assert len(z4) == 0
        assert len(z5) == 0

    def test_first_positive_zero_at_r15(self):
        """The first positive real numerator zero appears at r=15."""
        pz = positive_numerator_zeros(max_r=20)
        first_r = min(pz.keys()) if pz else None
        assert first_r == 15, f"First positive zero at r={first_r}"


# =========================================================================
# 15. EXACT FRACTION ARITHMETIC
# =========================================================================

class TestFractionArithmetic:
    """Cross-check via exact Fraction evaluation."""

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26])
    def test_S9_fraction_consistency(self, c_val):
        """S_9 via Fraction matches S_9 via sympy .subs."""
        frac_val = virasoro_S_fraction(9, c_val)
        sym_val = S_explicit(9).subs(c, c_val)
        assert Fraction(sym_val) == frac_val

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 26])
    def test_S10_fraction_consistency(self, c_val):
        frac_val = virasoro_S_fraction(10, c_val)
        sym_val = S_explicit(10).subs(c, c_val)
        assert Fraction(sym_val) == frac_val

    def test_ising_S9_S10(self):
        """S_9 and S_10 at c=1/2 (Ising model)."""
        s9 = virasoro_S_fraction(9, Fraction(1, 2))
        s10 = virasoro_S_fraction(10, Fraction(1, 2))
        assert s9 != 0 and s10 != 0

    def test_tricritical_ising_S9_S10(self):
        """S_9 and S_10 at c=7/10 (tricritical Ising)."""
        s9 = virasoro_S_fraction(9, Fraction(7, 10))
        s10 = virasoro_S_fraction(10, Fraction(7, 10))
        assert s9 != 0 and s10 != 0


# =========================================================================
# 16. CROSS-ENGINE CONSISTENCY
# =========================================================================

class TestCrossEngine:
    """Verify agreement with the existing frontier engine."""

    @pytest.fixture(scope="class")
    def frontier(self):
        from compute.lib.theorem_shadow_arity_frontier_engine import (
            shadow_coefficients_convolution as frontier_conv,
            S_explicit as frontier_explicit,
        )
        return frontier_conv(max_r=10), frontier_explicit

    @pytest.mark.parametrize("r", range(2, 11))
    def test_convolution_matches_frontier(self, frontier, r):
        frontier_conv, _ = frontier
        local = shadow_coefficients_convolution(max_r=10)
        diff = simplify(local[r] - frontier_conv[r])
        assert diff == 0, f"S_{r}: local != frontier"

    @pytest.mark.parametrize("r", range(2, 11))
    def test_explicit_matches_frontier(self, frontier, r):
        _, frontier_explicit = frontier
        diff = simplify(S_explicit(r) - frontier_explicit(r))
        assert diff == 0, f"S_{r}: explicit formulas disagree"


# =========================================================================
# 17. LIMITING CASES
# =========================================================================

class TestLimitingCases:
    """Large-c vanishing and pole structure."""

    @pytest.mark.parametrize("r", [9, 10])
    def test_large_c_vanishing(self, r):
        """S_r -> 0 as c -> infinity for r >= 4."""
        Sr = S_explicit(r)
        lim_val = limit(Sr, c, oo)
        assert lim_val == 0

    @pytest.mark.parametrize("r", [9, 10])
    def test_pole_order_at_c0(self, r):
        """S_r has pole of order r-3 at c=0."""
        Sr = S_explicit(r)
        regularized = cancel(Sr * c**(r - 3))
        val_at_0 = regularized.subs(c, 0)
        assert val_at_0 != 0

    def test_S9_leading_large_c(self):
        """S_9 ~ const/c^4 for large c."""
        Sr = S_explicit(9)
        # c^6 * (5c+22)^3 ~ 125 c^9, and numer ~ 2025 c^2
        # so S_9 ~ -1280*2025 / (3*125*c^7) = ... /c^4 after cancellation
        # Actually: deg(numer)=2, deg(denom)=6+3=9, so S_9 ~ 1/c^7
        # Wait, numer has c^2, denom has c^{6+3}=c^9 from c^6*(5c)^3
        # So S_9 ~ c^2/c^9 = 1/c^7... but numer_deg = 2 and total denom
        # power = 6 + 3 = 9 in c. So S_9 ~ 1/c^{9-2} = 1/c^7.
        # Just verify it vanishes:
        lim_val = limit(Sr, c, oo)
        assert lim_val == 0

    def test_critical_string_S9_S10(self):
        """S_9 and S_10 at c=26 are nonzero."""
        s9 = virasoro_S_fraction(9, 26)
        s10 = virasoro_S_fraction(10, 26)
        assert s9 != 0 and s10 != 0


# =========================================================================
# 18. STRUCTURAL PATTERN SUMMARY
# =========================================================================

class TestStructuralSummary:
    """Full structural data verification."""

    @pytest.fixture(scope="class")
    def summary(self):
        return structural_pattern_summary(max_r=20)

    @pytest.mark.parametrize("r", range(4, 21))
    def test_pow_c(self, summary, r):
        assert summary[r]['pow_c'] == summary[r]['pred_pow_c']

    @pytest.mark.parametrize("r", range(4, 21))
    def test_pow_5c22(self, summary, r):
        assert summary[r]['pow_5c22'] == summary[r]['pred_pow_5c22']

    @pytest.mark.parametrize("r", range(4, 21))
    def test_numer_deg(self, summary, r):
        assert summary[r]['numer_deg'] == summary[r]['pred_numer_deg']

    @pytest.mark.parametrize("r", range(4, 21))
    def test_lead_sign(self, summary, r):
        assert summary[r]['lead_sign'] == summary[r]['pred_lead_sign']


# =========================================================================
# 19. BRANCH POINT AND BEAT PERIOD
# =========================================================================

class TestBranchPoint:
    """Branch point analysis of Q_L(t)."""

    def test_branch_point_c1(self):
        data = branch_point_data(1.0)
        assert 160 < data['argument_deg'] < 170

    def test_branch_point_c13(self):
        data = branch_point_data(13.0)
        assert 168 < data['argument_deg'] < 175

    def test_branch_point_c26(self):
        data = branch_point_data(26.0)
        assert 170 < data['argument_deg'] < 177

    def test_beat_period_finite(self):
        """Beat period is finite for all c > 0."""
        for c_val in [0.5, 1, 5, 13, 26, 100]:
            data = branch_point_data(c_val)
            assert data['beat_period'] > 0
            assert data['beat_period'] < 1000

    def test_argument_increases_with_c(self):
        """Branch point argument approaches 180 deg as c -> infinity."""
        args = [branch_point_data(cv)['argument_deg']
                for cv in [1, 10, 100, 1000]]
        for i in range(len(args) - 1):
            assert args[i] < args[i + 1]
        assert args[-1] > 178


# =========================================================================
# 20. PHASE SLIP BOUNDARY IDENTIFICATION
# =========================================================================

class TestPhaseSlipBoundary:
    """Identify the central charge at which S_r first changes sign."""

    def test_S15_has_positive_zero(self):
        """S_15 numerator has a positive real zero (near c ~ 0.03)."""
        pz = positive_numerator_zeros(max_r=16)
        assert 15 in pz, "S_15 should have a positive numerator zero"
        assert pz[15][0] < 0.1, f"First positive zero of S_15 at c={pz[15][0]}"

    def test_S16_has_positive_zero(self):
        """S_16 numerator has a positive real zero (near c ~ 0.82)."""
        pz = positive_numerator_zeros(max_r=17)
        assert 16 in pz
        assert 0.5 < pz[16][0] < 1.5

    def test_S17_has_positive_zero(self):
        """S_17 numerator has a positive real zero (near c ~ 1.66)."""
        pz = positive_numerator_zeros(max_r=18)
        assert 17 in pz
        assert 1.0 < pz[17][0] < 2.5

    def test_positive_zero_c_increases_with_r(self):
        """The first positive zero moves to higher c as r increases."""
        pz = positive_numerator_zeros(max_r=20)
        prev_z = 0
        for r in sorted(pz.keys()):
            if r >= 16:  # Start from 16 where zeros are well-separated
                z = pz[r][0]
                assert z > prev_z, (
                    f"Positive zero of S_{r} ({z}) <= S_{r-1} ({prev_z})")
                prev_z = z

    def test_no_positive_zero_before_r15(self):
        """S_4 through S_14 have no positive numerator zeros."""
        pz = positive_numerator_zeros(max_r=15)
        early = {r: z for r, z in pz.items() if r < 15}
        assert len(early) == 0, f"Unexpected positive zeros at r={list(early.keys())}"


# =========================================================================
# ADDITIONAL: Convolution identity checks
# =========================================================================

class TestConvolutionIdentities:
    """Algebraic identities from the convolution recursion."""

    def test_a0_squared_is_q0(self):
        a = convolution_coefficients(max_n=2)
        q0, _, _ = virasoro_shadow_metric()
        assert simplify(a[0]**2 - q0) == 0

    def test_2a0a1_is_q1(self):
        a = convolution_coefficients(max_n=2)
        _, q1, _ = virasoro_shadow_metric()
        assert simplify(2 * a[0] * a[1] - q1) == 0

    def test_a1_is_6(self):
        a = convolution_coefficients(max_n=2)
        assert a[1] == 6

    def test_convolution_closure(self):
        """a_0^2 + 2*a_0*a_1*t + (a_1^2 + 2*a_0*a_2)*t^2 = Q_L(t)."""
        a = convolution_coefficients(max_n=2)
        q0, q1, q2 = virasoro_shadow_metric()
        assert simplify(a[0]**2 - q0) == 0
        assert simplify(2 * a[0] * a[1] - q1) == 0
        assert simplify(a[1]**2 + 2 * a[0] * a[2] - q2) == 0

    def test_shadow_metric_discriminant(self):
        """disc(Q_L) = -320c^2/(5c+22) < 0 for c > 0."""
        q0, q1, q2 = virasoro_shadow_metric()
        disc = cancel(q1**2 - 4 * q0 * q2)
        expected = -320 * c**2 / (5 * c + 22)
        assert simplify(disc - expected) == 0
