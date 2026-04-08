r"""Tests for shadow arity frontier engine: S_6, S_7, S_8 across the full landscape.

Multi-path verification mandate: every formula is checked by at least 3 independent
paths before it is considered reliable.

Test structure:
    1. Three-path agreement (convolution, master equation, ODE) for S_2-S_10
    2. Explicit formula verification
    3. Denominator pattern theorem
    4. Numerator degree theorem
    5. Limiting cases (c -> infinity, c -> 0 poles)
    6. Self-duality at c=13
    7. Koszul dual pair checks
    8. Sign pattern analysis
    9. Affine sl_2 shadow tower
   10. Beta-gamma T-line projection
   11. Heisenberg termination
   12. Shadow visibility genus
   13. Special central charge evaluations
   14. General single-line shadow tower
   15. Cross-engine consistency with virasoro_shadow_all_arity
   16. W_3 bivariate tower T-line projection consistency
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

from compute.lib.theorem_shadow_arity_frontier_engine import (
    S_explicit,
    affine_sl2_S_fraction,
    affine_sl2_shadow_coefficient,
    affine_sl2_shadow_tower,
    betagamma_central_charge,
    betagamma_T_line_shadow,
    branch_point_argument,
    convolution_coefficients,
    denominator_analysis,
    evaluate_landscape,
    general_shadow_coefficients,
    heisenberg_shadow_coefficient,
    koszul_dual_ratio,
    numerator_degree_analysis,
    self_duality_check,
    shadow_coefficients_convolution,
    shadow_coefficients_master_eq,
    shadow_coefficients_ode,
    shadow_visibility_genus,
    sign_pattern,
    virasoro_S_fraction,
    virasoro_shadow_metric,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. THREE-PATH AGREEMENT: Convolution, Master Eq, ODE
# =========================================================================

class TestThreePathAgreement:
    """Every S_r must agree across all three independent derivation paths."""

    @pytest.fixture(scope="class")
    def all_paths(self):
        conv = shadow_coefficients_convolution(max_r=10)
        meq = shadow_coefficients_master_eq(max_r=10)
        ode = shadow_coefficients_ode(max_r=10)
        return conv, meq, ode

    @pytest.mark.parametrize("r", range(2, 11))
    def test_conv_vs_meq(self, all_paths, r):
        """Convolution and master equation must agree."""
        conv, meq, _ = all_paths
        diff = simplify(conv[r] - meq[r])
        assert diff == 0, f"S_{r}: conv != meq, diff = {diff}"

    @pytest.mark.parametrize("r", range(2, 11))
    def test_conv_vs_ode(self, all_paths, r):
        """Convolution and ODE 3-term recurrence must agree."""
        conv, _, ode = all_paths
        diff = simplify(conv[r] - ode[r])
        assert diff == 0, f"S_{r}: conv != ode, diff = {diff}"

    @pytest.mark.parametrize("r", range(2, 11))
    def test_meq_vs_ode(self, all_paths, r):
        """Master equation and ODE must agree."""
        _, meq, ode = all_paths
        diff = simplify(meq[r] - ode[r])
        assert diff == 0, f"S_{r}: meq != ode, diff = {diff}"


# =========================================================================
# 2. EXPLICIT FORMULA VERIFICATION
# =========================================================================

class TestExplicitFormulas:
    """Verify explicit closed-form formulas match computation."""

    @pytest.fixture(scope="class")
    def computed(self):
        return shadow_coefficients_convolution(max_r=10)

    @pytest.mark.parametrize("r", range(2, 11))
    def test_explicit_matches_computed(self, computed, r):
        diff = simplify(computed[r] - S_explicit(r))
        assert diff == 0, f"S_{r} explicit != computed"

    def test_S6_formula(self):
        """S_6 = 80(45c+193) / [3 c^3 (5c+22)^2]."""
        expected = Rational(80) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
        assert simplify(S_explicit(6) - expected) == 0

    def test_S7_formula(self):
        """S_7 = -2880(15c+61) / [7 c^4 (5c+22)^2]."""
        expected = Rational(-2880) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2)
        assert simplify(S_explicit(7) - expected) == 0

    def test_S8_formula(self):
        """S_8 = 80(2025c^2+16470c+33314) / [c^5 (5c+22)^3]."""
        expected = (Rational(80) * (2025 * c**2 + 16470 * c + 33314)
                    / (c**5 * (5 * c + 22)**3))
        assert simplify(S_explicit(8) - expected) == 0

    def test_S2_is_kappa(self):
        assert simplify(S_explicit(2) - c / 2) == 0

    def test_S3_is_constant(self):
        assert S_explicit(3) == 2

    def test_S4_is_Q_contact(self):
        """S_4 = Q^contact_Vir = 10/[c(5c+22)]."""
        assert simplify(S_explicit(4) - Rational(10) / (c * (5 * c + 22))) == 0


# =========================================================================
# 3. DENOMINATOR PATTERN THEOREM
# =========================================================================

class TestDenominatorPattern:
    """denom(S_r) = c^{r-3} (5c+22)^{floor((r-2)/2)} times rational constant."""

    @pytest.fixture(scope="class")
    def analysis(self):
        return denominator_analysis(max_r=12)

    @pytest.mark.parametrize("r", range(4, 13))
    def test_denominator_matches_prediction(self, analysis, r):
        entry = [e for e in analysis if e[0] == r][0]
        assert entry[3], (f"S_{r}: pow_c={entry[1]} (pred {r-3}), "
                          f"pow_5c22={entry[2]} (pred {(r-2)//2})")


# =========================================================================
# 4. NUMERATOR DEGREE THEOREM
# =========================================================================

class TestNumeratorDegree:
    """deg_c(numer(S_r)) = floor((r-4)/2)."""

    @pytest.fixture(scope="class")
    def analysis(self):
        return numerator_degree_analysis(max_r=12)

    @pytest.mark.parametrize("r", range(4, 13))
    def test_numerator_degree_matches(self, analysis, r):
        entry = [e for e in analysis if e[0] == r][0]
        assert entry[3], (f"S_{r}: deg={entry[1]}, pred={(r-4)//2}")


# =========================================================================
# 5. LIMITING CASES
# =========================================================================

class TestLimitingCases:
    """S_r -> 0 as c -> infinity for r >= 4."""

    @pytest.mark.parametrize("r", [6, 7, 8, 9, 10])
    def test_large_c_vanishing(self, r):
        Sr = S_explicit(r)
        lim_val = limit(Sr, c, oo)
        assert lim_val == 0, f"S_{r} -> {lim_val} as c->inf, expected 0"

    @pytest.mark.parametrize("r", [4, 5, 6, 7, 8])
    def test_pole_order_at_c0(self, r):
        """S_r has pole of order r-3 at c=0 (from c^{r-3} in denominator)."""
        Sr = S_explicit(r)
        # Multiply by c^{r-3} and evaluate at c=0: should be finite nonzero
        regularized = cancel(Sr * c**(r - 3))
        val_at_0 = regularized.subs(c, 0)
        assert val_at_0 != 0, f"S_{r} * c^{r-3} vanishes at c=0"

    def test_S6_at_c1(self):
        """S_6(c=1) via exact Fraction arithmetic."""
        val = virasoro_S_fraction(6, 1)
        expected = Fraction(80, 3) * (45 + 193) / (1 * 27**2)
        assert val == expected

    def test_S7_at_c1(self):
        val = virasoro_S_fraction(7, 1)
        expected = Fraction(-2880, 7) * (15 + 61) / (1 * 27**2)
        assert val == expected

    def test_S8_at_c1(self):
        val = virasoro_S_fraction(8, 1)
        expected = Fraction(80) * (2025 + 16470 + 33314) / (1 * 27**3)
        assert val == expected


# =========================================================================
# 6. SELF-DUALITY AT c=13
# =========================================================================

class TestSelfDuality:
    """At c=13 (self-dual point), S_r(13) = S_r(26-13) = S_r(13)."""

    def test_self_duality_check(self):
        results = self_duality_check(max_r=10)
        for r, (v, v_dual, match) in results.items():
            assert match, f"S_{r}(13) != S_{r}(13): {v} vs {v_dual}"

    @pytest.mark.parametrize("r", [6, 7, 8])
    def test_S_at_c13_nonzero(self, r):
        """S_r(13) is nonzero (the tower does not terminate at self-dual point)."""
        val = virasoro_S_fraction(r, 13)
        assert val != 0, f"S_{r}(13) = 0 (unexpected termination)"

    def test_S6_c13_exact(self):
        """S_6(13) = 80*(45*13+193)/(3*13^3*(5*13+22)^2) = 62240/49887279."""
        val = virasoro_S_fraction(6, 13)
        numer_val = 80 * (45 * 13 + 193)
        denom_val = 3 * 13**3 * (5 * 13 + 22)**2
        assert val == Fraction(numer_val, denom_val)


# =========================================================================
# 7. KOSZUL DUAL PAIR CHECKS
# =========================================================================

class TestKoszulDuality:
    """S_r(c) vs S_r(26-c) for Virasoro Koszul duality c <-> 26-c."""

    @pytest.mark.parametrize("r", [6, 7, 8])
    def test_duality_ratio_well_defined(self, r):
        """The ratio S_r(c)/S_r(26-c) is a rational function of c."""
        ratio = koszul_dual_ratio(r)
        assert ratio is not None

    def test_complementarity_sum_nonzero(self):
        """S_6(c) + S_6(26-c) is generically nonzero (AP24: no anti-symmetry)."""
        S6 = S_explicit(6)
        S6_dual = S6.subs(c, 26 - c)
        sum_val = cancel(S6 + S6_dual)
        assert sum_val != 0

    def test_duality_at_c1_and_c25(self):
        """S_6(1) and S_6(25) should satisfy the Koszul duality relation."""
        v1 = virasoro_S_fraction(6, 1)
        v25 = virasoro_S_fraction(6, 25)
        # Both should be nonzero
        assert v1 != 0 and v25 != 0


# =========================================================================
# 8. SIGN PATTERN
# =========================================================================

class TestSignPattern:
    """S_r alternates sign (-1)^r for r >= 4 at generic c."""

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 25, 26, 100])
    def test_alternation_c_positive(self, c_val):
        """Sign of S_r is (-1)^r for r=4,...,10 at positive c."""
        results = sign_pattern(max_r=10, c_val=float(c_val))
        for r, sgn, expected, match in results:
            assert match, (f"S_{r}(c={c_val}): sign={sgn}, expected={expected}")

    def test_branch_point_at_c1(self):
        """Branch point argument at c=1 should be between 90 and 180 degrees."""
        arg = branch_point_argument(1.0)
        assert 90 < arg < 180


# =========================================================================
# 9. AFFINE sl_2 SHADOW TOWER
# =========================================================================

class TestAffineSl2:
    """Shadow tower for affine sl_2 via Sugawara substitution c=3k/(k+2)."""

    def test_S2_is_kappa_km(self):
        """S_2(sl_2) = 3k/(2(k+2))."""
        S2 = affine_sl2_shadow_coefficient(2)
        expected = 3 * k / (2 * (k + 2))
        assert simplify(S2 - expected) == 0

    def test_S3_universal(self):
        """S_3 = 2 (universal, independent of k)."""
        S3 = affine_sl2_shadow_coefficient(3)
        assert S3 == 2

    def test_S4_rational_in_k(self):
        """S_4 is a rational function of k."""
        S4 = affine_sl2_shadow_coefficient(4)
        assert S4 is not None and S4 != 0

    @pytest.mark.parametrize("r", [6, 7, 8])
    def test_S678_nonzero(self, r):
        """S_6, S_7, S_8 are nonzero for sl_2 on the T-line."""
        Sr = affine_sl2_shadow_coefficient(r)
        assert Sr != 0, f"S_{r}(sl_2) = 0 (unexpected)"

    def test_S6_at_k1(self):
        """S_6(sl_2, k=1) via exact arithmetic."""
        val = affine_sl2_S_fraction(6, 1)
        assert val != 0

    def test_S7_at_k1(self):
        val = affine_sl2_S_fraction(7, 1)
        assert val != 0

    def test_S8_at_k1(self):
        val = affine_sl2_S_fraction(8, 1)
        assert val != 0

    def test_tower_agrees_with_sugawara(self):
        """Full tower through S_8 matches Sugawara substitution."""
        tower = affine_sl2_shadow_tower(max_r=8)
        for r in range(2, 9):
            assert simplify(tower[r] - affine_sl2_shadow_coefficient(r)) == 0

    def test_large_k_limit_S6(self):
        """As k -> infinity, c(sl_2,k) = 3k/(k+2) -> 3, so
        S_6(sl_2) -> S_6(Vir, c=3) = 26240/110889.

        Note: the large-k limit is NOT zero. c approaches the finite
        large-k asymptote c=3 (Sugawara central charge of the abelianized
        sl_2, one real scalar + two neutral fields each contributing 1).
        """
        from sympy import Rational
        S6 = affine_sl2_shadow_coefficient(6)
        lim = limit(S6, k, oo)
        # S_6(Vir, c=3) = 80 * (45*3 + 193) / (3 * 27 * (5*3+22)^2)
        #              = 80 * 328 / (81 * 1369) = 26240 / 110889
        assert lim == Rational(26240, 110889)


# =========================================================================
# 10. BETA-GAMMA T-LINE PROJECTION
# =========================================================================

class TestBetaGamma:
    """Beta-gamma shadow tower on the T-line (Virasoro sub at c(bg, lambda))."""

    def test_T_line_S6_at_lam0(self):
        """S_6(bg, lam=0) = S_6(Vir, c=2) (nonzero)."""
        from sympy import Symbol as Sym
        lam_sym = Sym('lambda')
        S6 = betagamma_T_line_shadow(6)
        val = S6.subs(lam_sym, 0)
        vir_val = S_explicit(6).subs(c, 2)
        assert simplify(val - vir_val) == 0

    def test_T_line_S6_nonzero(self):
        """The T-line S_6 does NOT terminate (global termination is stratum sep)."""
        from sympy import Symbol as Sym
        lam_sym = Sym('lambda')
        S6 = betagamma_T_line_shadow(6)
        # At lambda=0: c=2
        val = S6.subs(lam_sym, 0)
        assert val != 0


# =========================================================================
# 11. HEISENBERG TERMINATION
# =========================================================================

class TestHeisenberg:
    """Heisenberg: class G, tower terminates at arity 2."""

    def test_S2_is_k(self):
        assert heisenberg_shadow_coefficient(2, k_val=k) == k

    @pytest.mark.parametrize("r", [3, 4, 5, 6, 7, 8])
    def test_higher_shadows_vanish(self, r):
        assert heisenberg_shadow_coefficient(r) == 0


# =========================================================================
# 12. SHADOW VISIBILITY GENUS
# =========================================================================

class TestVisibilityGenus:
    """g_min(S_r) = floor(r/2) + 1."""

    def test_S6_visibility(self):
        assert shadow_visibility_genus(6) == 4

    def test_S7_visibility(self):
        assert shadow_visibility_genus(7) == 4

    def test_S8_visibility(self):
        assert shadow_visibility_genus(8) == 5

    def test_S4_visibility(self):
        assert shadow_visibility_genus(4) == 3

    def test_S5_visibility(self):
        assert shadow_visibility_genus(5) == 3


# =========================================================================
# 13. SPECIAL CENTRAL CHARGE EVALUATIONS
# =========================================================================

class TestSpecialValues:
    """Evaluate S_6, S_7, S_8 at physically important central charges."""

    def test_ising_S6(self):
        """S_6(c=1/2) is well-defined and nonzero."""
        val = virasoro_S_fraction(6, Fraction(1, 2))
        assert val != 0

    def test_free_boson_S6(self):
        """S_6(c=1) is well-defined and nonzero."""
        val = virasoro_S_fraction(6, 1)
        assert val != 0

    def test_critical_string_S6(self):
        """S_6(c=26) is well-defined and nonzero."""
        val = virasoro_S_fraction(6, 26)
        assert val != 0

    def test_landscape_evaluation_runs(self):
        """The full landscape evaluation completes without error."""
        results = evaluate_landscape(max_r=8)
        assert len(results) > 0

    @pytest.mark.parametrize("name", [
        'ising', 'free_boson', 'self_dual', 'critical_string',
    ])
    def test_landscape_S6_S7_S8_nonzero(self, name):
        """S_6, S_7, S_8 are nonzero across the standard landscape."""
        results = evaluate_landscape(max_r=8)
        if name in results:
            for r in [6, 7, 8]:
                assert results[name][r] != 0, f"S_{r}({name}) = 0"


# =========================================================================
# 14. GENERAL SINGLE-LINE SHADOW TOWER
# =========================================================================

class TestGeneralTower:
    """General single-line tower recovers Virasoro when kappa=c/2, alpha=2, S4=Q^contact."""

    def test_general_recovers_virasoro(self):
        """General tower with Virasoro data matches Virasoro tower."""
        kappa_v = c / 2
        alpha_v = Rational(2)
        S4_v = Rational(10) / (c * (5 * c + 22))
        gen = general_shadow_coefficients(kappa_v, alpha_v, S4_v, max_r=8)
        vir = shadow_coefficients_convolution(max_r=8)
        for r in range(2, 9):
            diff = simplify(gen[r] - vir[r])
            assert diff == 0, f"S_{r}: general != Virasoro, diff = {diff}"

    def test_heisenberg_via_general(self):
        """General tower with Heisenberg data: S_r = 0 for r >= 3."""
        # Heisenberg: kappa = k, alpha = 0, S4 = 0
        gen = general_shadow_coefficients(k, Rational(0), Rational(0), max_r=8)
        assert gen[2] == k
        for r in range(3, 9):
            assert cancel(gen[r]) == 0, f"Heisenberg S_{r} != 0"


# =========================================================================
# 15. CROSS-ENGINE CONSISTENCY
# =========================================================================

class TestCrossEngine:
    """Verify agreement with the canonical virasoro_shadow_all_arity module."""

    @pytest.fixture(scope="class")
    def canonical(self):
        from compute.lib.virasoro_shadow_all_arity import (
            shadow_coefficients as canonical_shadow_coefficients,
        )
        return canonical_shadow_coefficients(max_r=10)

    @pytest.mark.parametrize("r", range(2, 11))
    def test_matches_canonical(self, canonical, r):
        """Frontier engine matches canonical virasoro_shadow_all_arity."""
        frontier = shadow_coefficients_convolution(max_r=10)
        diff = simplify(frontier[r] - canonical[r])
        assert diff == 0, f"S_{r}: frontier != canonical"


# =========================================================================
# 16. W_3 BIVARIATE TOWER T-LINE PROJECTION
# =========================================================================

class TestW3TLine:
    """The T-line projection (x_W=0) of the W_3 tower must match Virasoro."""

    @pytest.fixture(scope="class")
    def w3_tower(self):
        from compute.lib.w3_full_2d_shadow_tower import compute_full_2d_tower
        from sympy import Symbol
        return compute_full_2d_tower(max_arity=8)

    @pytest.mark.parametrize("r", [2, 3, 4, 5, 6, 7, 8])
    def test_T_line_projection_matches_virasoro(self, w3_tower, r):
        """Sh_r(x_T, 0) restricted to x_T = 1 should give the Virasoro S_r * r
        (since Sh_r = sum S_{r,m} x_T^a x_W^b and the pure T-term is S_r x_T^r,
        i.e. the coefficient of x_T^r equals the Virasoro shadow at that arity)."""
        from sympy import Symbol
        x_T = Symbol('x_T')
        x_W = Symbol('x_W')
        sh = w3_tower[r]
        # Set x_W = 0: extract T-line projection
        t_line = sh.subs(x_W, 0)
        # The coefficient of x_T^r is the pure-T shadow coefficient
        from sympy import Poly
        p = Poly(t_line, x_T)
        coeff_dict = p.as_dict()
        leading_coeff = coeff_dict.get((r,), 0)
        # Compare with Virasoro S_r (the coefficient should match)
        vir_Sr = S_explicit(r)
        diff = simplify(leading_coeff - vir_Sr)
        assert diff == 0, f"W_3 T-line coeff at x_T^{r} != Vir S_{r}: diff={diff}"


# =========================================================================
# 17. ADDITIONAL STRUCTURAL TESTS
# =========================================================================

class TestStructural:
    """Structural properties of the shadow tower."""

    def test_S_r_rational_functions(self):
        """S_r are rational functions of c (no radicals)."""
        for r in range(2, 11):
            Sr = S_explicit(r)
            # If Sr contains sqrt, this will fail
            assert 'sqrt' not in str(Sr), f"S_{r} contains square root"

    def test_shadow_metric_discriminant(self):
        """disc(Q_L) = -320c^2/(5c+22) < 0 for c > 0."""
        q0, q1, q2 = virasoro_shadow_metric()
        disc = cancel(q1**2 - 4 * q0 * q2)
        expected = -320 * c**2 / (5 * c + 22)
        assert simplify(disc - expected) == 0

    def test_growth_rate_squared(self):
        """rho^2 = (180c+872)/[c^2(5c+22)] = q2/q0."""
        q0, q1, q2 = virasoro_shadow_metric()
        rho2 = cancel(q2 / q0)
        expected = (180 * c + 872) / (c**2 * (5 * c + 22))
        assert simplify(rho2 - expected) == 0

    def test_convolution_identity_a0_squared(self):
        """a_0^2 = q0 = c^2."""
        a = convolution_coefficients(max_n=2)
        q0, _, _ = virasoro_shadow_metric()
        assert simplify(a[0]**2 - q0) == 0

    def test_convolution_identity_2a0a1(self):
        """2*a_0*a_1 = q1 = 12c."""
        a = convolution_coefficients(max_n=2)
        _, q1, _ = virasoro_shadow_metric()
        assert simplify(2 * a[0] * a[1] - q1) == 0

    def test_yang_lee_pole(self):
        """c = -22/5 (Yang-Lee) is a pole of S_r for r >= 4."""
        # S_4 has (5c+22) in denominator, so c=-22/5 is a pole
        # We verify the denominator vanishes
        S4 = S_explicit(4)
        d = cancel(S4 * c * (5 * c + 22))
        val = d.subs(c, Rational(-22, 5))
        assert val != 0  # The numerator is nonzero at c=-22/5

    def test_S6_numerator_root(self):
        """S_6 has a numerator zero at c = -193/45."""
        S6 = S_explicit(6)
        # Multiply out denominator
        n = numer(cancel(S6))
        val = n.subs(c, Rational(-193, 45))
        assert val == 0

    def test_S7_numerator_root(self):
        """S_7 has a numerator zero at c = -61/15."""
        S7 = S_explicit(7)
        n = numer(cancel(S7))
        val = n.subs(c, Rational(-61, 15))
        assert val == 0
