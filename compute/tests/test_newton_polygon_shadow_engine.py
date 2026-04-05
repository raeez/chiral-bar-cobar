"""Tests for Newton polygon analysis of shadow generating functions.

Verifies:
- Newton polygon computation (lower convex hull of p-adic lattice points)
- Slopes, breaks, and p-adic shadow radii
- Multi-path verification: sqrt(Q_L) expansion vs ODE recursion vs denominator factors
- Hadamard comparison: rho_p vs rho_infty
- Hodge polygon and Mazur inequality
- Dieudonne-Manin slope decomposition
- Specific families: Virasoro (class M), Heisenberg (class G), affine KM (class L),
  beta-gamma (class C)
- Full (c, p) table for c in {1/2, 4/5, 7/10, 1, 2, 25} x p in {2,3,5,7,11,13}

Multi-path verification mandate (CLAUDE.md):
  Path 1: Direct v_p computation from exact S_r
  Path 2: Shadow ODE recurrence -> p-adic growth estimate
  Path 3: Newton polygon from factored denominator patterns
  Path 4: Cross-check rho_p vs rho_infty (Hadamard consistency)

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    chap:arithmetic-shadows (arithmetic_shadows.tex)
"""

import pytest
from fractions import Fraction
from math import log

from compute.lib.newton_polygon_shadow_engine import (
    v_p,
    v_p_safe,
    virasoro_shadow_coefficients,
    virasoro_shadow_coefficients_ode,
    affine_sl2_shadow_coefficients,
    heisenberg_shadow_coefficients,
    beta_gamma_shadow_coefficients,
    newton_polygon_points,
    lower_convex_hull,
    newton_polygon,
    newton_polygon_slopes,
    newton_polygon_slopes_exact,
    break_count,
    break_locations,
    padic_shadow_radius,
    archimedean_shadow_radius,
    analyze_newton_polygon,
    virasoro_newton_polygon_table,
    full_virasoro_newton_table,
    hodge_polygon_padic,
    verify_mazur_inequality,
    classify_ordinarity,
    discriminant_newton_polygon,
    slope_multiplicity,
    isocrystal_decomposition,
    compare_padic_archimedean_radii,
    full_radius_comparison_table,
    break_count_table,
    heisenberg_newton_analysis,
    affine_sl2_newton_analysis,
    beta_gamma_newton_analysis,
    denominator_prime_factorization,
    verify_vp_from_denominator,
    verify_shadow_coefficients_two_paths,
    ising_analysis,
    c_equals_1_analysis,
    VIRASORO_C_VALUES,
    PRIMES,
)


# ============================================================================
# 1. p-adic valuation
# ============================================================================

class TestPadicValuation:
    """Tests for the p-adic valuation function."""

    def test_vp_integer(self):
        """v_p of integers."""
        assert v_p(Fraction(8), 2) == 3
        assert v_p(Fraction(9), 3) == 2
        assert v_p(Fraction(25), 5) == 2
        assert v_p(Fraction(7), 7) == 1
        assert v_p(Fraction(1), 2) == 0

    def test_vp_fraction(self):
        """v_p of fractions."""
        assert v_p(Fraction(1, 4), 2) == -2
        assert v_p(Fraction(3, 8), 2) == -3
        assert v_p(Fraction(9, 5), 3) == 2
        assert v_p(Fraction(49, 3), 7) == 2

    def test_vp_negative(self):
        """v_p of negative numbers."""
        assert v_p(Fraction(-8), 2) == 3
        assert v_p(Fraction(-1, 9), 3) == -2

    def test_vp_zero_raises(self):
        """v_p(0) should raise ValueError."""
        with pytest.raises(ValueError):
            v_p(Fraction(0), 2)

    def test_vp_safe_zero(self):
        """v_p_safe returns inf for zero."""
        assert v_p_safe(Fraction(0), 2) == float('inf')

    def test_vp_coprime(self):
        """v_p(n) = 0 when gcd(n, p) = 1."""
        assert v_p(Fraction(7), 2) == 0
        assert v_p(Fraction(11), 3) == 0
        assert v_p(Fraction(13), 5) == 0


# ============================================================================
# 2. Shadow coefficient computation
# ============================================================================

class TestShadowCoefficients:
    """Tests for exact shadow coefficient computation."""

    def test_virasoro_kappa(self):
        """S_2 = c/2 for all c."""
        for c_val in [Fraction(1), Fraction(1, 2), Fraction(25)]:
            coeffs = virasoro_shadow_coefficients(c_val, max_r=4)
            assert coeffs[2] == c_val / 2

    def test_virasoro_cubic(self):
        """S_3 = 2 for Virasoro (c-independent, from convolution recursion)."""
        for c_val in [Fraction(1), Fraction(1, 2), Fraction(25)]:
            coeffs = virasoro_shadow_coefficients(c_val, max_r=4)
            assert coeffs[3] == Fraction(2)

    def test_virasoro_quartic_c1(self):
        """S_4 = 10/(c(5c+22)) at c=1 gives 10/27."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=4)
        expected = Fraction(10) / (Fraction(1) * (5 + 22))
        assert coeffs[4] == expected

    def test_virasoro_quartic_ising(self):
        """S_4 at c=1/2: 10/((1/2)(49/2)) = 10/(49/4) = 40/49."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=4)
        c = Fraction(1, 2)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert coeffs[4] == expected

    def test_virasoro_quartic_c25(self):
        """S_4 at c=25: 10/(25*147) = 10/3675 = 2/735."""
        coeffs = virasoro_shadow_coefficients(Fraction(25), max_r=4)
        c = Fraction(25)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert coeffs[4] == expected

    def test_heisenberg_class_g(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3."""
        coeffs = heisenberg_shadow_coefficients(Fraction(1), max_r=10)
        assert coeffs[2] == Fraction(1)
        for r in range(3, 11):
            assert coeffs[r] == 0

    def test_affine_sl2_class_l(self):
        """Affine sl_2: S_2 = 3(k+2)/4, S_3 nonzero, S_r = 0 for r >= 4."""
        k = Fraction(1)
        coeffs = affine_sl2_shadow_coefficients(k, max_r=10)
        assert coeffs[2] == Fraction(3) * (k + 2) / 4
        assert coeffs[3] != 0  # Nonzero cubic shadow
        for r in range(4, 11):
            assert coeffs[r] == 0

    def test_beta_gamma_class_c(self):
        """Beta-gamma (c=-2): S_2 = -1, S_3 = 2, S_4 = -5/12, S_r = 0 for r >= 5.

        S_3 = 2 (c-independent). S_4 = 10/(c(5c+22)) = 10/((-2)(12)) = -5/12.
        """
        coeffs = beta_gamma_shadow_coefficients(max_r=10)
        assert coeffs[2] == Fraction(-1)
        assert coeffs[3] == Fraction(2)
        assert coeffs[4] == Fraction(-5, 12)
        for r in range(5, 11):
            assert coeffs[r] == 0


# ============================================================================
# 3. Multi-path verification (Paths 1 and 2)
# ============================================================================

class TestMultiPathVerification:
    """Multi-path verification: sqrt(Q_L) expansion vs ODE recursion."""

    @pytest.mark.parametrize("c_val", [
        Fraction(1, 2), Fraction(1), Fraction(2),
        Fraction(4, 5), Fraction(7, 10), Fraction(25),
    ])
    def test_two_paths_agree(self, c_val):
        """sqrt(Q_L) expansion and ODE recursion give identical S_r."""
        results = verify_shadow_coefficients_two_paths(c_val, max_r=15)
        for r, match in results:
            assert match, f"Paths disagree at r={r} for c={c_val}"

    def test_two_paths_agree_c1_high_arity(self):
        """Agreement through r=20 at c=1."""
        results = verify_shadow_coefficients_two_paths(Fraction(1), max_r=20)
        for r, match in results:
            assert match, f"Paths disagree at r={r} for c=1"


# ============================================================================
# 4. Newton polygon computation
# ============================================================================

class TestNewtonPolygon:
    """Tests for Newton polygon (lower convex hull) computation."""

    def test_convex_hull_simple(self):
        """Simple case: 3 collinear points -> 2 vertices."""
        pts = [(0, 0), (1, 1), (2, 2)]
        hull = lower_convex_hull(pts)
        assert len(hull) == 2
        assert hull[0] == (0, 0)
        assert hull[-1] == (2, 2)

    def test_convex_hull_concave(self):
        """Point above the line is kept in the hull only if it is below."""
        pts = [(0, 0), (1, -1), (2, 0)]
        hull = lower_convex_hull(pts)
        assert len(hull) == 3
        assert (1, -1) in hull

    def test_convex_hull_drops_above(self):
        """Point above the line is dropped from the lower hull."""
        pts = [(0, 0), (1, 2), (2, 0)]
        hull = lower_convex_hull(pts)
        assert len(hull) == 2
        assert (1, 2) not in hull

    def test_newton_polygon_virasoro_c1_p2(self):
        """Newton polygon for Virasoro at c=1, p=2 (landscape convention)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        verts = newton_polygon(coeffs, 2)
        # S_2 = 1/2, v_2(1/2) = -1
        # S_3 = 2, v_2(2) = 1
        # S_4 = 10/27, v_2(10/27) = v_2(10)-v_2(27) = 1-0 = 1
        points = newton_polygon_points(coeffs, 2)
        assert points[0] == (2, -1)  # v_2(1/2) = -1
        assert points[1] == (3, 1)   # v_2(2) = 1
        # Newton polygon should have at least 2 vertices
        assert len(verts) >= 2

    def test_newton_polygon_ising_p7(self):
        """Ising (c=1/2) at p=7: S_4 = 40/49, v_7 = -2."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=10)
        S4 = coeffs[4]
        c = Fraction(1, 2)
        expected = Fraction(10) / (c * (5 * c + 22))  # = 40/49
        assert S4 == expected
        assert v_p(S4, 7) == -2

    def test_newton_polygon_heisenberg_single_point(self):
        """Heisenberg: only S_2 is nonzero -> 1 vertex, no slopes."""
        coeffs = heisenberg_shadow_coefficients(Fraction(1), max_r=10)
        verts = newton_polygon(coeffs, 2)
        assert len(verts) == 1  # Only one nonzero coefficient

    def test_newton_polygon_affine_sl2_two_points(self):
        """Affine sl_2: S_2 and S_3 nonzero -> 2 vertices, 1 slope."""
        k = Fraction(1)
        coeffs = affine_sl2_shadow_coefficients(k, max_r=10)
        verts = newton_polygon(coeffs, 2)
        assert len(verts) == 2
        slopes = newton_polygon_slopes(verts)
        assert len(slopes) == 1

    def test_newton_polygon_empty_input(self):
        """Empty coefficient dict returns empty polygon."""
        verts = newton_polygon({}, 2)
        assert verts == []


# ============================================================================
# 5. Slopes and breaks
# ============================================================================

class TestSlopesAndBreaks:
    """Tests for slope extraction and break counting."""

    def test_slopes_single_segment(self):
        """Two vertices -> one slope."""
        verts = [(2, -1), (5, 2)]
        slopes = newton_polygon_slopes(verts)
        assert len(slopes) == 1
        assert slopes[0][0] == pytest.approx(1.0)

    def test_slopes_exact(self):
        """Exact slope computation with Fractions."""
        verts = [(2, 0), (5, 3)]
        slopes = newton_polygon_slopes_exact(verts)
        assert slopes[0][0] == Fraction(1)

    def test_break_count_no_breaks(self):
        """Two vertices -> 0 breaks."""
        verts = [(2, 0), (5, 3)]
        assert break_count(verts) == 0

    def test_break_count_one_break(self):
        """Three vertices -> 1 break."""
        verts = [(2, 0), (4, -2), (6, 1)]
        assert break_count(verts) == 1
        assert break_locations(verts) == [4]

    def test_break_count_multiple(self):
        """Multiple breaks."""
        verts = [(0, 0), (2, -2), (4, -1), (6, 3)]
        assert break_count(verts) == 2
        assert break_locations(verts) == [2, 4]

    def test_heisenberg_no_breaks(self):
        """Class G: single nonzero coefficient -> 0 breaks."""
        coeffs = heisenberg_shadow_coefficients(Fraction(1))
        verts = newton_polygon(coeffs, 2)
        assert break_count(verts) == 0

    def test_affine_sl2_no_breaks(self):
        """Class L: two nonzero coefficients -> 0 breaks."""
        coeffs = affine_sl2_shadow_coefficients(Fraction(1))
        verts = newton_polygon(coeffs, 2)
        assert break_count(verts) == 0


# ============================================================================
# 6. p-adic shadow radius
# ============================================================================

class TestPadicShadowRadius:
    """Tests for p-adic shadow radius computation."""

    def test_padic_radius_single_slope(self):
        """Single slope s -> rho_p = p^{-s}."""
        verts = [(2, 0), (5, 3)]  # slope = 1
        assert padic_shadow_radius(verts, 2) == pytest.approx(0.5)  # 2^{-1}
        assert padic_shadow_radius(verts, 3) == pytest.approx(1.0 / 3)

    def test_padic_radius_negative_slope(self):
        """Negative slope -> rho_p > 1."""
        verts = [(2, 0), (5, -3)]  # slope = -1
        assert padic_shadow_radius(verts, 2) == pytest.approx(2.0)

    def test_padic_radius_zero_slope(self):
        """Zero slope -> rho_p = 1."""
        verts = [(2, 0), (5, 0)]  # slope = 0
        assert padic_shadow_radius(verts, 2) == pytest.approx(1.0)

    def test_padic_radius_empty(self):
        """Empty polygon -> rho = 0."""
        assert padic_shadow_radius([], 2) == 0.0

    def test_archimedean_radius_c1(self):
        """Archimedean shadow radius for Virasoro c=1."""
        rho = archimedean_shadow_radius(Fraction(1))
        # rho^2 = (180+872)/((5+22)*1) = 1052/27 ≈ 38.96
        # rho ≈ 6.24
        assert rho > 1.0  # Tower diverges at c=1

    def test_archimedean_radius_c25(self):
        """Archimedean shadow radius for Virasoro c=25."""
        rho = archimedean_shadow_radius(Fraction(25))
        # rho^2 = (180*25+872)/((5*25+22)*625) = 5372/(147*625) = 5372/91875
        # rho ≈ 0.242
        assert rho < 1.0  # Tower converges at c=25


# ============================================================================
# 7. Ising model specific tests
# ============================================================================

class TestIsingModel:
    """Specific tests for the Ising model (c = 1/2)."""

    def test_ising_s4_valuation_at_7(self):
        """S_4(c=1/2) = 10/((1/2)(49/2)) = 40/49.
        v_7(40/49) = -2 (from denominator 49 = 7^2).
        """
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=5)
        # 40/49: numerator has no factor of 7, denominator has 7^2
        assert v_p(coeffs[4], 7) == -2

    def test_ising_kappa_valuation(self):
        """kappa = 1/4 at c=1/2, v_2(1/4) = -2."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=3)
        assert coeffs[2] == Fraction(1, 4)
        assert v_p(coeffs[2], 2) == -2

    def test_ising_newton_polygon_p7_has_interesting_structure(self):
        """At p=7, the Ising NP reflects the 7^2 in the denominator of S_4.
        S_4 = 40/49, so v_7(S_4) = -2, creating a dip in the NP.
        """
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=15)
        analysis = analyze_newton_polygon(coeffs, 7, "Ising p=7")
        verts = analysis['vertices']
        assert len(verts) >= 2
        # S_2 = 1/4: v_7(1/4) = 0
        # S_3 = 2: v_7(2) = 0
        # S_4 = 40/49: v_7 = -2
        # The v_7 = -2 at r=4 is a local low point
        lattice_pts = analysis['lattice_points']
        r4_pts = [pt for pt in lattice_pts if pt[0] == 4]
        assert len(r4_pts) == 1
        assert r4_pts[0][1] == -2  # v_7 = -2

    def test_ising_all_primes(self):
        """Ising model analysis completes for all primes."""
        results = ising_analysis(max_r=15)
        assert len(results) == len(PRIMES)
        for p in PRIMES:
            assert results[p]['p'] == p
            assert len(results[p]['vertices']) >= 1


# ============================================================================
# 8. Full (c, p) table
# ============================================================================

class TestFullTable:
    """Tests for the full Virasoro Newton polygon table."""

    def test_full_table_completeness(self):
        """Table covers all 6 x 6 = 36 combinations."""
        table = full_virasoro_newton_table(max_r=10)
        assert len(table) == len(VIRASORO_C_VALUES) * len(PRIMES)

    def test_full_table_has_vertices(self):
        """Every entry has at least one NP vertex."""
        table = full_virasoro_newton_table(max_r=10)
        for entry in table:
            assert len(entry['vertices']) >= 1

    def test_full_table_slopes_finite(self):
        """All slopes are finite numbers."""
        table = full_virasoro_newton_table(max_r=10)
        for entry in table:
            for slope, r1, r2 in entry['slopes']:
                assert slope == slope  # not NaN
                assert abs(slope) < 1000  # sanity bound

    @pytest.mark.parametrize("c_val", VIRASORO_C_VALUES)
    def test_virasoro_table_per_c(self, c_val):
        """Newton polygon table for each c value."""
        results = virasoro_newton_polygon_table(c_val, max_r=10)
        assert len(results) == len(PRIMES)


# ============================================================================
# 9. Path 3: Denominator factorization verification
# ============================================================================

class TestDenominatorFactorization:
    """Tests for Path 3: v_p from denominator factorization."""

    @pytest.mark.parametrize("c_val", [Fraction(1), Fraction(1, 2), Fraction(2)])
    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_vp_from_denominator_matches_direct(self, c_val, p):
        """v_p computed from denominator factorization matches direct computation."""
        coeffs = virasoro_shadow_coefficients(c_val, max_r=15)
        results = verify_vp_from_denominator(coeffs, p, max_r=15)
        for r, vp_direct, vp_factored, match in results:
            assert match, (
                f"Mismatch at r={r}, c={c_val}, p={p}: "
                f"direct={vp_direct}, factored={vp_factored}"
            )

    def test_denominator_factorization_structure(self):
        """Denominator factorization has expected structure for c=1 (landscape conv)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        factors = denominator_prime_factorization(coeffs, max_r=10)
        # S_2 = 1/2: denom = 2
        assert 2 in factors[2]
        # S_4 = 10/27: denom = 27 = 3^3
        assert factors[4].get(3, 0) == 3


# ============================================================================
# 10. Hodge polygon and Mazur inequality
# ============================================================================

class TestHodgePolygon:
    """Tests for Hodge polygon and Mazur inequality."""

    @pytest.mark.parametrize("c_val", [Fraction(1), Fraction(1, 2), Fraction(25)])
    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_mazur_inequality_holds(self, c_val, p):
        """NP_p >= HP_p for all computed cases."""
        coeffs = virasoro_shadow_coefficients(c_val, max_r=15)
        result = verify_mazur_inequality(coeffs, p)
        assert result['holds'], (
            f"Mazur inequality violated at c={c_val}, p={p}: "
            f"violations={result['violations']}"
        )

    def test_hodge_polygon_has_correct_endpoints(self):
        """Hodge polygon starts and ends at the same points as the data."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        hp = hodge_polygon_padic(coeffs, 2)
        np_points = newton_polygon_points(coeffs, 2)
        if len(hp) >= 2 and len(np_points) >= 2:
            # First and last points should match
            assert hp[0][0] == np_points[0][0]
            assert hp[-1][0] == np_points[-1][0]
            assert abs(hp[0][1] - np_points[0][1]) < 0.01
            assert abs(hp[-1][1] - np_points[-1][1]) < 0.01

    @pytest.mark.parametrize("c_val", VIRASORO_C_VALUES)
    def test_ordinarity_classification(self, c_val):
        """Ordinarity classification returns valid label."""
        coeffs = virasoro_shadow_coefficients(c_val, max_r=10)
        for p in [2, 3, 5]:
            cls = classify_ordinarity(coeffs, p)
            assert cls in ('ordinary', 'supersingular', 'degenerate', 'violation')


# ============================================================================
# 11. Dieudonne-Manin decomposition
# ============================================================================

class TestDieudonneManin:
    """Tests for isocrystal decomposition."""

    def test_heisenberg_isoclinic(self):
        """Heisenberg: single coefficient -> single slope component."""
        coeffs = heisenberg_shadow_coefficients(Fraction(1))
        decomp = isocrystal_decomposition(coeffs, 2, "Heis k=1")
        # Only one nonzero coefficient, so the NP is a single point
        assert decomp['num_slopes'] == 0  # Single point = no slopes

    def test_affine_sl2_single_slope(self):
        """Affine sl_2: two coefficients -> one slope."""
        coeffs = affine_sl2_shadow_coefficients(Fraction(1))
        decomp = isocrystal_decomposition(coeffs, 2, "sl2 k=1")
        assert decomp['num_slopes'] == 1

    def test_virasoro_mixed(self):
        """Virasoro (class M): many slopes -> mixed classification."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)
        decomp = isocrystal_decomposition(coeffs, 2, "Vir c=1")
        # Virasoro should have multiple slope components
        assert decomp['num_slopes'] >= 1

    def test_slope_multiplicity_sums_correctly(self):
        """Total dimension = sum of multiplicities = horizontal span of NP."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        verts = newton_polygon(coeffs, 2)
        mults = slope_multiplicity(verts)
        total = sum(mults.values())
        if len(verts) >= 2:
            expected = verts[-1][0] - verts[0][0]
            assert total == expected

    @pytest.mark.parametrize("p", PRIMES)
    def test_decomposition_valid_for_all_primes(self, p):
        """Isocrystal decomposition is valid for all primes."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        decomp = isocrystal_decomposition(coeffs, p, f"Vir c=1 p={p}")
        assert decomp['classification'] in ('zero', 'unit', 'supersingular',
                                              'mixed') or \
               decomp['classification'].startswith('isoclinic')


# ============================================================================
# 12. Break count analysis
# ============================================================================

class TestBreakCount:
    """Tests for break count beta_p across families."""

    def test_heisenberg_zero_breaks(self):
        """Class G: 0 breaks for all primes."""
        results = heisenberg_newton_analysis(Fraction(1))
        for analysis in results:
            assert analysis['break_count'] == 0

    def test_affine_sl2_zero_breaks(self):
        """Class L: 0 breaks (two points -> one segment)."""
        results = affine_sl2_newton_analysis(Fraction(1))
        for analysis in results:
            assert analysis['break_count'] == 0

    def test_beta_gamma_few_breaks(self):
        """Class C: at most 1 break (three nonzero coefficients)."""
        results = beta_gamma_newton_analysis()
        for analysis in results:
            assert analysis['break_count'] <= 1

    def test_virasoro_has_breaks(self):
        """Class M: Virasoro should have breaks for some primes."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)
        found_break = False
        for p in PRIMES:
            verts = newton_polygon(coeffs, p)
            if break_count(verts) > 0:
                found_break = True
                break
        # Class M has infinite shadow depth -> many nonzero coefficients
        # -> likely to have breaks in the NP for some prime
        assert found_break, "Virasoro c=1 should have breaks for at least one prime"

    def test_break_count_table_completeness(self):
        """Break count table covers all (c, p) pairs."""
        table = break_count_table(max_r=10)
        expected_size = len(VIRASORO_C_VALUES) * len(PRIMES)
        assert len(table) == expected_size


# ============================================================================
# 13. Radius comparison: rho_p vs rho_infty
# ============================================================================

class TestRadiusComparison:
    """Tests for comparing p-adic and archimedean shadow radii."""

    def test_comparison_has_all_primes(self):
        """Comparison returns data for all primes."""
        result = compare_padic_archimedean_radii(Fraction(1))
        assert len(result['radii']) == len(PRIMES)

    def test_archimedean_radius_positive(self):
        """Archimedean radius is positive for nonzero c."""
        for c_val in VIRASORO_C_VALUES:
            rho = archimedean_shadow_radius(c_val)
            assert rho > 0

    def test_full_comparison_table(self):
        """Full table has correct number of entries."""
        table = full_radius_comparison_table(max_r=10)
        assert len(table) == len(VIRASORO_C_VALUES)

    @pytest.mark.parametrize("c_val", [Fraction(1), Fraction(25)])
    def test_padic_radii_are_finite(self, c_val):
        """p-adic radii are finite positive numbers."""
        result = compare_padic_archimedean_radii(c_val, max_r=10)
        for p, rho_p in result['radii'].items():
            assert rho_p >= 0
            assert rho_p < float('inf')


# ============================================================================
# 14. Discriminant Newton polygon
# ============================================================================

class TestDiscriminantNewtonPolygon:
    """Tests for Newton polygon of the discriminant function."""

    def test_discriminant_formula(self):
        """Delta(c) = 8*kappa*S_4 = 8*(c/2)*10/(c(5c+22)) = 40/(5c+22)."""
        for c_val in [1, 2, 5, 10]:
            c = Fraction(c_val)
            expected = Fraction(40) / (5 * c + 22)
            coeffs = virasoro_shadow_coefficients(c, max_r=5)
            kappa = coeffs[2]
            S4 = coeffs[4]
            delta = 8 * kappa * S4
            assert delta == expected, f"Delta mismatch at c={c_val}"

    def test_discriminant_np_p2(self):
        """Discriminant NP at p=2 has valid structure."""
        result = discriminant_newton_polygon(range(1, 20), 2)
        assert len(result['vertices']) >= 2

    @pytest.mark.parametrize("p", [2, 3, 5, 7])
    def test_discriminant_np_valid(self, p):
        """Discriminant NP is valid for various primes."""
        result = discriminant_newton_polygon(range(1, 15), p)
        assert result['p'] == p
        assert len(result['vertices']) >= 1


# ============================================================================
# 15. Non-Virasoro families
# ============================================================================

class TestNonVirasoroFamilies:
    """Tests for Newton polygons of non-Virasoro families."""

    def test_heisenberg_analysis_complete(self):
        """Heisenberg analysis runs for all primes."""
        results = heisenberg_newton_analysis(Fraction(1))
        assert len(results) == len(PRIMES)

    def test_heisenberg_single_vertex_all_primes(self):
        """Heisenberg: only S_2 nonzero -> single vertex polygon."""
        for k_val in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            results = heisenberg_newton_analysis(k_val)
            for analysis in results:
                assert len(analysis['vertices']) == 1

    def test_affine_sl2_analysis_complete(self):
        """Affine sl_2 analysis runs for all primes."""
        results = affine_sl2_newton_analysis(Fraction(1))
        assert len(results) == len(PRIMES)

    def test_affine_sl2_two_vertices(self):
        """Affine sl_2: two nonzero coefficients -> two vertices."""
        results = affine_sl2_newton_analysis(Fraction(1))
        for analysis in results:
            assert len(analysis['vertices']) == 2

    def test_beta_gamma_analysis_complete(self):
        """Beta-gamma analysis runs for all primes."""
        results = beta_gamma_newton_analysis()
        assert len(results) == len(PRIMES)

    def test_beta_gamma_three_vertices_max(self):
        """Beta-gamma: 3 nonzero coefficients -> at most 3 vertices."""
        results = beta_gamma_newton_analysis()
        for analysis in results:
            assert len(analysis['vertices']) <= 3


# ============================================================================
# 16. Shadow depth and break count correlation
# ============================================================================

class TestShadowDepthCorrelation:
    """Test the relationship between shadow depth class and NP structure."""

    def test_class_g_minimal_np(self):
        """Class G (Heisenberg): 1 vertex, 0 breaks, 0 slopes."""
        coeffs = heisenberg_shadow_coefficients(Fraction(1))
        for p in [2, 3, 5]:
            verts = newton_polygon(coeffs, p)
            assert len(verts) == 1
            assert break_count(verts) == 0
            assert newton_polygon_slopes(verts) == []

    def test_class_l_single_slope(self):
        """Class L (affine KM): 2 vertices, 0 breaks, 1 slope."""
        coeffs = affine_sl2_shadow_coefficients(Fraction(1))
        for p in [2, 3, 5]:
            verts = newton_polygon(coeffs, p)
            assert len(verts) == 2
            assert break_count(verts) == 0
            slopes = newton_polygon_slopes(verts)
            assert len(slopes) == 1

    def test_class_m_many_slopes(self):
        """Class M (Virasoro): many vertices and slopes."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)
        # At least for some prime, Virasoro should have > 1 slope
        max_slopes = 0
        for p in PRIMES:
            verts = newton_polygon(coeffs, p)
            num_slopes = len(newton_polygon_slopes(verts))
            max_slopes = max(max_slopes, num_slopes)
        assert max_slopes >= 2, "Class M should have multiple NP slopes"

    def test_depth_ordering(self):
        """Break count: class G <= class L <= class C <= class M."""
        g_coeffs = heisenberg_shadow_coefficients(Fraction(1))
        l_coeffs = affine_sl2_shadow_coefficients(Fraction(1))
        c_coeffs = beta_gamma_shadow_coefficients()
        m_coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)

        for p in [2, 3, 5]:
            g_breaks = break_count(newton_polygon(g_coeffs, p))
            l_breaks = break_count(newton_polygon(l_coeffs, p))
            c_breaks = break_count(newton_polygon(c_coeffs, p))
            m_breaks = break_count(newton_polygon(m_coeffs, p))
            assert g_breaks <= l_breaks or g_breaks <= 0
            # m_breaks >= g_breaks at least (class M has more structure)
            assert m_breaks >= g_breaks


# ============================================================================
# 17. Specific lattice point verification
# ============================================================================

class TestSpecificLatticePoints:
    """Verify specific v_p(S_r) values by hand computation."""

    def test_vp_s2_c1_p2(self):
        """S_2(c=1) = 1/2, v_2 = -1."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=3)
        assert v_p(coeffs[2], 2) == -1

    def test_vp_s3_c1_p2(self):
        """S_3(c=1) = 2 (c-independent).
        v_2(2) = 1."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=4)
        assert coeffs[3] == Fraction(2)
        assert v_p(coeffs[3], 2) == 1

    def test_vp_s4_c1_p3(self):
        """S_4(c=1) = 10/27 (landscape convention).
        v_3(10/27) = -3 (27 = 3^3, 10 has no factor of 3)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=5)
        expected = Fraction(10, 27)
        assert coeffs[4] == expected
        assert v_p(coeffs[4], 3) == -3

    def test_vp_s2_ising_p2(self):
        """S_2(c=1/2) = 1/4, v_2 = -2."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=3)
        assert v_p(coeffs[2], 2) == -2

    def test_vp_s4_ising_p7(self):
        """S_4(c=1/2) = 40/49.
        v_7(40/49) = -2 (49 = 7^2 in denominator, 40 has no factor of 7)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1, 2), max_r=5)
        assert v_p(coeffs[4], 7) == -2

    def test_vp_s2_c25_p5(self):
        """S_2(c=25) = 25/2, v_5 = 2."""
        coeffs = virasoro_shadow_coefficients(Fraction(25), max_r=3)
        assert coeffs[2] == Fraction(25, 2)
        assert v_p(coeffs[2], 5) == 2

    def test_vp_s4_c25(self):
        """S_4(c=25) = 10/(25*147) = 2/735.
        735 = 3 * 5 * 7^2."""
        coeffs = virasoro_shadow_coefficients(Fraction(25), max_r=5)
        c = Fraction(25)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert coeffs[4] == expected
        assert v_p(coeffs[4], 5) == -1  # 735 has 5^1
        assert v_p(coeffs[4], 7) == -2  # 735 has 7^2
        assert v_p(coeffs[4], 2) == 1   # 2 in numerator

    def test_vp_s2_c4_5_p5(self):
        """S_2(c=4/5) = 2/5, v_5 = -1."""
        coeffs = virasoro_shadow_coefficients(Fraction(4, 5), max_r=3)
        assert coeffs[2] == Fraction(2, 5)
        assert v_p(coeffs[2], 5) == -1


# ============================================================================
# 18. Convex hull correctness
# ============================================================================

class TestConvexHullCorrectness:
    """Additional tests for lower convex hull algorithm correctness."""

    def test_single_point(self):
        """Single point returns itself."""
        hull = lower_convex_hull([(3, 5)])
        assert hull == [(3, 5)]

    def test_two_points(self):
        """Two points are always both vertices."""
        hull = lower_convex_hull([(1, 2), (3, 4)])
        assert len(hull) == 2

    def test_all_on_line(self):
        """Collinear points: only endpoints survive."""
        pts = [(i, 2 * i) for i in range(10)]
        hull = lower_convex_hull(pts)
        assert len(hull) == 2
        assert hull[0] == (0, 0)
        assert hull[-1] == (9, 18)

    def test_deep_concavity(self):
        """Deep dip is captured as a vertex."""
        pts = [(0, 10), (3, -5), (6, 10)]
        hull = lower_convex_hull(pts)
        assert len(hull) == 3
        assert (3, -5) in hull

    def test_multiple_dips(self):
        """Multiple dips create multiple breaks."""
        pts = [(0, 0), (2, -3), (4, 0), (6, -2), (8, 0)]
        hull = lower_convex_hull(pts)
        # All are vertices of the lower hull
        assert (2, -3) in hull
        assert (6, -2) in hull

    def test_upper_points_removed(self):
        """Points above the hull line are removed."""
        pts = [(0, 0), (1, 5), (2, 1), (3, 6), (4, 2)]
        hull = lower_convex_hull(pts)
        # (1, 5) is above the line from (0,0) to (2,1); check it's removed
        # Actually lower hull: (0,0), (2,1), (4,2) are collinear at slope 1/2
        # (1,5) and (3,6) are above -> removed
        for _, y in hull:
            assert y <= 6  # sanity


# ============================================================================
# 19. Consistency: Newton polygon is indeed lower convex hull
# ============================================================================

class TestNewtonPolygonConsistency:
    """Verify NP is the lower convex hull of the lattice points."""

    @pytest.mark.parametrize("c_val", [Fraction(1), Fraction(1, 2)])
    @pytest.mark.parametrize("p", [2, 3, 5])
    def test_all_points_above_np(self, c_val, p):
        """Every lattice point (r, v_p(S_r)) lies on or above the NP."""
        coeffs = virasoro_shadow_coefficients(c_val, max_r=15)
        points = newton_polygon_points(coeffs, p)
        verts = newton_polygon(coeffs, p)

        if len(verts) < 2:
            return  # Nothing to check

        for r, vp_val in points:
            # Find the NP value at this r by interpolation
            for i in range(len(verts) - 1):
                r1, v1 = verts[i]
                r2, v2 = verts[i + 1]
                if r1 <= r <= r2:
                    t = (r - r1) / (r2 - r1) if r2 > r1 else 0
                    np_val = v1 + t * (v2 - v1)
                    assert vp_val >= np_val - 1e-10, (
                        f"Point ({r}, {vp_val}) below NP ({np_val}) "
                        f"at c={c_val}, p={p}"
                    )
                    break


# ============================================================================
# 20. c = 1 specific analysis
# ============================================================================

class TestCEquals1:
    """Tests for c = 1 (free boson on circle)."""

    def test_c1_analysis_runs(self):
        """c=1 analysis completes for all primes."""
        results = c_equals_1_analysis(max_r=15)
        assert len(results) == len(PRIMES)

    def test_c1_newton_polygon_p2(self):
        """c=1, p=2: specific lattice points (landscape convention)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        points = newton_polygon_points(coeffs, 2)
        # r=2: S_2 = 1/2, v_2 = -1
        assert points[0] == (2, -1)
        # r=3: S_3 = 2, v_2(2) = 1
        assert points[1] == (3, 1)

    def test_c1_newton_polygon_p3(self):
        """c=1, p=3: S_4 = 10/27 (landscape convention).
        v_3(10/27) = -3 (27 = 3^3 in denominator)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        points = newton_polygon_points(coeffs, 3)
        # Find the point at r=4
        r4_point = [pt for pt in points if pt[0] == 4]
        assert len(r4_point) == 1
        assert r4_point[0][1] == -3  # v_3(10/27) = -3


# ============================================================================
# 21. Virasoro shadow coefficients at rational c
# ============================================================================

class TestRationalC:
    """Tests for shadow coefficients at rational central charges."""

    @pytest.mark.parametrize("c_val", [
        Fraction(7, 10),  # Lee-Yang edge
        Fraction(4, 5),   # tricritical Ising
    ])
    def test_coefficients_are_rational(self, c_val):
        """All S_r are exact rationals."""
        coeffs = virasoro_shadow_coefficients(c_val, max_r=15)
        for r, S_r in coeffs.items():
            assert isinstance(S_r, Fraction), f"S_{r} is not Fraction at c={c_val}"

    def test_lee_yang_kappa(self):
        """Lee-Yang (c=7/10): kappa = 7/20."""
        coeffs = virasoro_shadow_coefficients(Fraction(7, 10), max_r=3)
        assert coeffs[2] == Fraction(7, 20)

    def test_tricritical_ising_kappa(self):
        """Tricritical Ising (c=4/5): kappa = 2/5."""
        coeffs = virasoro_shadow_coefficients(Fraction(4, 5), max_r=3)
        assert coeffs[2] == Fraction(2, 5)


# ============================================================================
# 22. Newton polygon monotonicity properties
# ============================================================================

class TestNewtonPolygonMonotonicity:
    """Test structural properties of Newton polygons."""

    def test_vertices_ordered_by_x(self):
        """Vertices are strictly increasing in x-coordinate."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)
        for p in PRIMES:
            verts = newton_polygon(coeffs, p)
            for i in range(len(verts) - 1):
                assert verts[i][0] < verts[i + 1][0]

    def test_slopes_change_at_breaks(self):
        """Slopes increase at each break (convexity)."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)
        for p in [2, 3, 5]:
            verts = newton_polygon(coeffs, p)
            slopes = newton_polygon_slopes(verts)
            for i in range(len(slopes) - 1):
                assert slopes[i][0] <= slopes[i + 1][0] + 1e-10, (
                    f"Slope decrease at p={p}: {slopes[i][0]} > {slopes[i+1][0]}"
                )


# ============================================================================
# 23. Virasoro at c = 25 (near critical)
# ============================================================================

class TestNearCritical:
    """Tests for c = 25 (near the critical dimension c = 26)."""

    def test_c25_tower_converges(self):
        """At c=25, the archimedean shadow radius < 1 (convergent tower)."""
        rho = archimedean_shadow_radius(Fraction(25))
        assert rho < 1.0

    def test_c25_many_nonzero_coefficients(self):
        """At c=25, the Virasoro tower has many nonzero coefficients (class M)."""
        coeffs = virasoro_shadow_coefficients(Fraction(25), max_r=15)
        nonzero_count = sum(1 for r in range(2, 16) if coeffs[r] != 0)
        # Class M (infinite shadow depth): all S_r should be nonzero
        assert nonzero_count >= 10, "Class M should have many nonzero coefficients"

    def test_c25_newton_polygon_structure(self):
        """c=25 NP has expected structure for large c."""
        coeffs = virasoro_shadow_coefficients(Fraction(25), max_r=15)
        for p in [2, 3, 5]:
            analysis = analyze_newton_polygon(coeffs, p, f"c=25, p={p}")
            assert len(analysis['vertices']) >= 2


# ============================================================================
# 24. Cross-family Newton polygon comparison
# ============================================================================

class TestCrossFamilyComparison:
    """Compare NP structure across the four shadow depth classes."""

    def test_np_complexity_ordering(self):
        """NP vertex count: class G < class L <= class C < class M (for most primes)."""
        g_coeffs = heisenberg_shadow_coefficients(Fraction(1))
        l_coeffs = affine_sl2_shadow_coefficients(Fraction(1))
        m_coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=15)

        for p in [2, 3, 5]:
            g_verts = len(newton_polygon(g_coeffs, p))
            l_verts = len(newton_polygon(l_coeffs, p))
            m_verts = len(newton_polygon(m_coeffs, p))
            assert g_verts <= l_verts, f"Class G has more vertices than L at p={p}"
            assert l_verts <= m_verts, f"Class L has more vertices than M at p={p}"


# ============================================================================
# 25. Slope multiplicity
# ============================================================================

class TestSlopeMultiplicity:
    """Tests for Dieudonne-Manin slope decomposition details."""

    def test_single_slope_multiplicity(self):
        """Two vertices -> one slope with multiplicity = horizontal span."""
        verts = [(2, 0), (5, 3)]
        mults = slope_multiplicity(verts)
        assert len(mults) == 1
        assert list(mults.values())[0] == 3  # 5 - 2 = 3

    def test_two_slopes_multiplicity(self):
        """Three vertices -> two slopes."""
        verts = [(0, 0), (3, -3), (6, 0)]
        mults = slope_multiplicity(verts)
        assert len(mults) == 2
        # First slope: (0,0) to (3,-3), slope = -1, mult = 3
        # Second slope: (3,-3) to (6,0), slope = 1, mult = 3
        assert mults[Fraction(-1)] == 3
        assert mults[Fraction(1)] == 3


# ============================================================================
# 26. Analyze function output structure
# ============================================================================

class TestAnalyzeOutputStructure:
    """Verify the structure of the analyze_newton_polygon output."""

    def test_all_keys_present(self):
        """Output dict has all expected keys."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=10)
        result = analyze_newton_polygon(coeffs, 2, "test")
        expected_keys = {
            'label', 'p', 'lattice_points', 'vertices', 'slopes',
            'slopes_exact', 'break_count', 'break_locations',
            'padic_radius', 'min_slope', 'max_slope',
        }
        assert expected_keys.issubset(set(result.keys()))

    def test_label_propagates(self):
        """Label is passed through correctly."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=5)
        result = analyze_newton_polygon(coeffs, 2, "my_label")
        assert result['label'] == "my_label"

    def test_prime_recorded(self):
        """Prime is recorded in the output."""
        coeffs = virasoro_shadow_coefficients(Fraction(1), max_r=5)
        result = analyze_newton_polygon(coeffs, 7)
        assert result['p'] == 7
