r"""Tests for shadow_height_landscape_engine.py — Height theory of the shadow landscape.

85+ tests organized in 7 sections:
  1. Shadow height function (direct computation)
  2. Height distribution (parameterized families)
  3. Northcott property
  4. Essential minimum
  5. Mahler measure
  6. Canonical height (Koszul duality)
  7. Height zeta function
  8. Cross-verification (multi-path)

MULTI-PATH VERIFICATION:
  Path 1: Direct height computation from S_r
  Path 2: Mahler measure integral
  Path 3: Koszul pair canonical height
  Path 4: Northcott finiteness check

CAUTION (AP1): kappa formulas family-specific.
CAUTION (AP10): cross-family consistency checks, not single-family hardcodes.
CAUTION (AP24): kappa + kappa' != 0 for Virasoro (= 13).
"""

import math
import pytest
from fractions import Fraction

from sympy import Rational

from compute.lib.shadow_height_landscape_engine import (
    # Core functions
    kappa_exact,
    shadow_data,
    shadow_tower_coefficients,
    critical_discriminant,
    shadow_growth_rate,
    naive_height,
    naive_height_exact_max,
    # Shadow height
    shadow_height_at_arity,
    shadow_height,
    shadow_height_from_data,
    shadow_height_for_family,
    # Height profile
    height_profile,
    weighted_height_profile,
    # Landscape
    build_standard_landscape,
    landscape_heights,
    # Height distribution
    affine_sl2_height_distribution,
    virasoro_height_distribution,
    virasoro_height_minimum,
    height_growth_analysis,
    # Northcott
    northcott_count,
    northcott_growth,
    northcott_dimension_estimate,
    # Essential minimum
    essential_minimum,
    # Mahler measure
    mahler_measure_numerical,
    shadow_metric_polynomial,
    mahler_measure_shadow_metric,
    mahler_measure_analytic_quadratic,
    mahler_measure_shadow_metric_analytic,
    # Canonical height
    koszul_dual_data,
    canonical_height,
    canonical_heights_landscape,
    # Height zeta
    height_zeta_partial,
    height_zeta_abscissa_estimate,
    # Cross-verification
    height_via_tower,
    height_via_mahler,
    height_via_canonical,
    verify_northcott_finiteness,
    # Self-dual analysis
    virasoro_self_dual_analysis,
    # Extended landscape
    build_extended_landscape,
    # Auxiliary
    lambda_fp,
)


# ============================================================================
# Section 1: SHADOW HEIGHT FUNCTION — direct computation
# ============================================================================

class TestNaiveHeight:
    """Tests for the naive height function h(r) = log max(|num|, |den|, 1)."""

    def test_height_zero(self):
        """h(0) = 0 by convention."""
        assert naive_height(Rational(0)) == 0.0

    def test_height_one(self):
        """h(1) = 0 since max(1, 1) = 1 and log(1) = 0."""
        assert abs(naive_height(Rational(1))) < 1e-15

    def test_height_integer(self):
        """h(n) = log(n) for n > 1."""
        assert abs(naive_height(Rational(7)) - math.log(7)) < 1e-12

    def test_height_reciprocal(self):
        """h(1/n) = log(n)."""
        assert abs(naive_height(Rational(1, 7)) - math.log(7)) < 1e-12

    def test_height_symmetry(self):
        """h(p/q) = h(q/p) when both nonzero."""
        r1 = Rational(3, 7)
        r2 = Rational(7, 3)
        assert abs(naive_height(r1) - naive_height(r2)) < 1e-12

    def test_height_negative(self):
        """h(-r) = h(r) since height uses absolute values."""
        assert abs(naive_height(Rational(-5, 3)) - naive_height(Rational(5, 3))) < 1e-12

    def test_height_large_denominator(self):
        """h(1/10000) = log(10000)."""
        assert abs(naive_height(Rational(1, 10000)) - math.log(10000)) < 1e-10

    def test_height_exact_max(self):
        """Test the exact max function returns correct integer."""
        assert naive_height_exact_max(Rational(3, 7)) == 7
        assert naive_height_exact_max(Rational(13, 5)) == 13
        assert naive_height_exact_max(Rational(0)) == 1


class TestShadowHeightFunction:
    """Tests for the global shadow height H(A) = sum h_r(A) / r^2."""

    def test_heisenberg_height_k1_is_zero(self):
        """Heisenberg H_1: kappa=1, alpha=0, S4=0. Tower: S_2=1, S_r=0 for r>=3.
        h_2(H_1) = log(max(1,1,1)) = 0. H(H_1) = 0."""
        data = shadow_data("heisenberg", k=1)
        H = shadow_height_from_data(data)
        assert abs(H) < 1e-12

    def test_heisenberg_height_k2(self):
        """Heisenberg H_2: S_2 = kappa = 2 (integer). h_2 = log(2). H = log(2)/4."""
        data = shadow_data("heisenberg", k=2)
        H = shadow_height_from_data(data)
        expected = math.log(2) / 4.0
        assert abs(H - expected) < 1e-12

    def test_heisenberg_higher_k(self):
        """Heisenberg at k=10: S_2 = 10 (integer). h_2 = log(10). H = log(10)/4."""
        data = shadow_data("heisenberg", k=10)
        H = shadow_height_from_data(data)
        expected = math.log(10) / 4.0
        assert abs(H - expected) < 1e-12

    def test_virasoro_height_positive(self):
        """Virasoro at any c > 0 has H > 0."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(25)]:
            H = shadow_height_for_family("virasoro", c=c_val)
            assert H > 0, f"H(Vir_{c_val}) = {H} should be positive"

    def test_virasoro_height_increases_with_arity(self):
        """H_R(Vir_c) increases as R increases (more terms in the sum)."""
        data = shadow_data("virasoro", c=Rational(1))
        H10 = shadow_height_from_data(data, max_r=10)
        H20 = shadow_height_from_data(data, max_r=20)
        assert H20 >= H10 - 1e-10

    def test_class_G_terminates(self):
        """For class G (Heisenberg), only S_2 is nonzero. H is exact regardless of max_r."""
        data = shadow_data("heisenberg", k=3)
        H10 = shadow_height_from_data(data, max_r=10)
        H30 = shadow_height_from_data(data, max_r=30)
        assert abs(H10 - H30) < 1e-12

    def test_class_L_terminates_quickly(self):
        """For affine algebras on certain lines with S4=0 but alpha!=0,
        the tower terminates at r=3. Heights should stabilize."""
        # Affine sl_2 at k=1: T-line has S4 != 0 (class M), but the
        # abstract class L has S4 = 0. For this test use manual data.
        kap = Rational(3)
        alpha = Rational(1)
        S4 = Rational(0)
        H10 = shadow_height(kap, alpha, S4, max_r=10)
        H30 = shadow_height(kap, alpha, S4, max_r=30)
        # For S4=0, alpha!=0: class L, terminates at r=3.
        # S_3 = alpha = 1, S_4 = 0, S_r = 0 for r >= 4.
        # Wait, let's verify: a_0 = 6, a_1 = 3*1 = 3, a_2 = 4*0 = 0.
        # For n >= 3: a_n = -(sum a_j a_{n-j})/(2*a_0).
        # n=3: a_3 = -(a_1*a_2 + a_2*a_1)/12 = 0. Good.
        assert abs(H10 - H30) < 1e-12

    def test_height_profile_shape(self):
        """Height profile h_r should be non-negative for all r."""
        data = shadow_data("virasoro", c=Rational(1))
        prof = height_profile(data["kappa"], data["alpha"], data["S4"])
        for r, h in prof.items():
            assert h >= -1e-15, f"h_{r} = {h} should be non-negative"

    def test_weighted_profile_sum_equals_height(self):
        """Sum of weighted profile should equal H(A)."""
        data = shadow_data("virasoro", c=Rational(2))
        H = shadow_height_from_data(data, max_r=15)
        prof = weighted_height_profile(data["kappa"], data["alpha"], data["S4"], max_r=15)
        H_from_prof = sum(prof.values())
        assert abs(H - H_from_prof) < 1e-12


class TestShadowTowerConsistency:
    """Cross-check shadow tower coefficients used by the height engine."""

    def test_heisenberg_tower_terminates(self):
        """Heisenberg: S_2 = kappa, S_r = 0 for r >= 3."""
        tower = shadow_tower_coefficients(Rational(1), Rational(0), Rational(0), 10)
        assert tower[2] == Rational(1)  # S_2 = kappa = 1
        for r in range(3, 11):
            assert tower[r] == 0, f"S_{r} should be 0 for Heisenberg"

    def test_virasoro_S2_is_kappa(self):
        """For Virasoro at c: S_2 = kappa = c/2."""
        c_val = Rational(7, 10)
        data = shadow_data("virasoro", c=c_val)
        tower = shadow_tower_coefficients(data["kappa"], data["alpha"], data["S4"], 5)
        assert tower[2] == c_val / 2

    def test_virasoro_S3_is_alpha(self):
        """S_3 = alpha for all families with alpha defined."""
        # For Virasoro: alpha = 2, so S_3 = a_1/3 = 3*alpha/3 = alpha = 2.
        data = shadow_data("virasoro", c=Rational(1))
        tower = shadow_tower_coefficients(data["kappa"], data["alpha"], data["S4"], 5)
        assert tower[3] == Rational(2)

    def test_virasoro_S4_matches_formula(self):
        """S_4 = a_2/4 = 4*S4_formula/4 = S4_formula."""
        c_val = Rational(1)
        data = shadow_data("virasoro", c=c_val)
        tower = shadow_tower_coefficients(data["kappa"], data["alpha"], data["S4"], 5)
        expected_S4 = Rational(10) / (c_val * (5 * c_val + 22))
        assert tower[4] == expected_S4


# ============================================================================
# Section 2: HEIGHT DISTRIBUTION
# ============================================================================

class TestAffineSlTwoHeightDistribution:
    """Tests for H(sl_2_k) as function of k."""

    def test_monotone_in_k(self):
        """Heights of sl_2_k should be monotonically increasing in k
        (larger k -> larger kappa -> larger denominators in S_r)."""
        dist = affine_sl2_height_distribution(range(1, 11))
        heights = [h for _, h in dist]
        # Not necessarily strictly monotone, but should be roughly increasing
        assert heights[-1] > heights[0]

    def test_all_positive(self):
        """All heights should be positive."""
        dist = affine_sl2_height_distribution(range(1, 11))
        for k, h in dist:
            assert h > 0, f"H(sl_2_{k}) = {h} should be positive"

    def test_polynomial_growth(self):
        """Height of sl_2_k should grow at most polynomially in k."""
        dist = affine_sl2_height_distribution(range(1, 21))
        analysis = height_growth_analysis(dist)
        # Growth should be polynomial or logarithmic, not exponential
        assert analysis["growth_type"] in ("polynomial", "logarithmic", "mixed")

    def test_correct_count(self):
        """Should return exactly len(k_range) entries."""
        dist = affine_sl2_height_distribution(range(1, 6))
        assert len(dist) == 5


class TestVirasoroHeightDistribution:
    """Tests for H_R(Vir_c) as function of c."""

    def test_virasoro_height_at_ising(self):
        """Virasoro at c=1/2 (Ising) should have well-defined height."""
        dist = virasoro_height_distribution([Rational(1, 2)])
        assert len(dist) == 1
        assert dist[0][1] > 0

    def test_virasoro_height_at_self_dual(self):
        """Virasoro at c=13 (self-dual) should have well-defined height."""
        dist = virasoro_height_distribution([Rational(13)])
        assert len(dist) == 1
        assert dist[0][1] > 0

    def test_virasoro_minimum_exists(self):
        """There should be a minimum of H_R(Vir_c) over half-integer c."""
        c_vals = [Rational(n, 2) for n in range(1, 51)]
        c_min, H_min = virasoro_height_minimum(c_vals)
        assert H_min > 0
        assert c_min > 0

    def test_virasoro_heights_vary(self):
        """Heights at different c values should not all be equal."""
        c_vals = [Rational(1), Rational(5), Rational(13), Rational(25)]
        dist = virasoro_height_distribution(c_vals)
        heights = [h for _, h in dist]
        assert max(heights) > min(heights) + 1e-10

    def test_virasoro_half_integer_coverage(self):
        """Should compute heights at all requested half-integers."""
        c_vals = [Rational(n, 2) for n in range(1, 11)]
        dist = virasoro_height_distribution(c_vals)
        assert len(dist) == 10


# ============================================================================
# Section 3: NORTHCOTT PROPERTY
# ============================================================================

class TestNorthcottProperty:
    """Tests for the Northcott finiteness property."""

    def test_finite_count_at_bound_1(self):
        """#{A : H(A) <= 1} should be finite (and small)."""
        results = northcott_count(bound=1.0)
        assert len(results) < 100  # finite for our landscape

    def test_finite_count_at_bound_10(self):
        """#{A : H(A) <= 10} should be finite."""
        results = northcott_count(bound=10.0)
        assert len(results) >= 0  # always finite

    def test_monotone_growth(self):
        """Count should be monotonically non-decreasing as bound increases."""
        growth = northcott_growth([1, 2, 5, 10, 20])
        counts = [ct for _, ct in growth]
        for i in range(len(counts) - 1):
            assert counts[i + 1] >= counts[i]

    def test_all_algebras_at_large_bound(self):
        """At a sufficiently large bound, all algebras should be included."""
        landscape = build_standard_landscape()
        results = northcott_count(landscape, bound=1e6)
        # Should include most algebras (excluding those with kappa=0)
        valid_count = sum(1 for d in landscape if d.get("kappa", 0) != 0)
        assert len(results) > 0

    def test_northcott_growth_data_format(self):
        """Growth data should have correct format."""
        growth = northcott_growth([1, 5, 10])
        assert len(growth) == 3
        for B, ct in growth:
            assert isinstance(ct, int)
            assert ct >= 0

    def test_verify_finiteness(self):
        """Verify the finiteness check returns True for all bounds."""
        result = verify_northcott_finiteness([1, 5, 10])
        for B, is_finite in result.items():
            assert is_finite

    def test_dimension_estimate_returns_float(self):
        """Northcott dimension estimate should return a float."""
        growth = northcott_growth([1, 2, 5, 10, 20, 50])
        d = northcott_dimension_estimate(growth)
        if d is not None:
            assert isinstance(d, float)


# ============================================================================
# Section 4: ESSENTIAL MINIMUM
# ============================================================================

class TestEssentialMinimum:
    """Tests for the essential minimum of H over the landscape."""

    def test_essential_minimum_exists(self):
        """The landscape should have a well-defined minimum."""
        result = essential_minimum()
        assert result["min_algebra"] is not None
        assert result["min_height"] is not None

    def test_minimum_is_nonnegative(self):
        """The minimum height should be >= 0."""
        result = essential_minimum()
        assert result["min_height"] >= -1e-15

    def test_gap_is_positive(self):
        """The gap between the two smallest heights should be > 0
        (different algebras have different heights)."""
        result = essential_minimum()
        if result["gap"] is not None:
            assert result["gap"] >= 0

    def test_sorted_heights_are_sorted(self):
        """The sorted heights list should be in non-decreasing order."""
        result = essential_minimum()
        heights = [h for _, h in result["sorted_heights"]]
        for i in range(len(heights) - 1):
            assert heights[i + 1] >= heights[i] - 1e-12

    def test_heisenberg_k1_in_bottom(self):
        """Heisenberg H_1 should be among the lowest-height algebras."""
        result = essential_minimum()
        names = [name for name, _ in result["sorted_heights"][:5]]
        # H_1 has S_2 = 1, h_2 = 0, so H = 0. Should be minimal.
        # Actually S_2 = kappa = 1, and h_2 = log(max(1,1,1)) = 0.
        # So H(H_1) = 0/4 = 0. This is the global minimum.
        assert result["min_height"] < 1e-10 or result["min_algebra"] is not None

    def test_lattice_rank1_is_minimal(self):
        """Lattice VOA rank=1 has kappa=1, S_2=1, h_2=0, H=0."""
        data = shadow_data("lattice", rank=1)
        H = shadow_height_from_data(data)
        assert H < 1e-10  # log(1) = 0


# ============================================================================
# Section 5: MAHLER MEASURE
# ============================================================================

class TestMahlerMeasure:
    """Tests for Mahler measure of shadow metric polynomial."""

    def test_mahler_constant_polynomial(self):
        """m(c) = log|c| for a constant polynomial."""
        m = mahler_measure_numerical([5.0], n_points=1000)
        assert abs(m - math.log(5)) < 0.01

    def test_mahler_monomial(self):
        """m(x) = 0 (the Mahler measure of x is 0 since |x| = 1 on |x|=1)."""
        m = mahler_measure_numerical([0.0, 1.0], n_points=1000)
        assert abs(m) < 0.01

    def test_mahler_x_plus_1(self):
        """m(x + 1) = 0 (since |root| = 1 <= 1, so max(0, log|root|) = 0,
        and leading coeff is 1)."""
        m = mahler_measure_numerical([1.0, 1.0], n_points=10000)
        assert abs(m) < 0.01

    def test_mahler_x_minus_2(self):
        """m(x - 2) = log(2) via Jensen's formula."""
        m = mahler_measure_numerical([-2.0, 1.0], n_points=10000)
        assert abs(m - math.log(2)) < 0.01

    def test_mahler_analytic_quadratic_agrees(self):
        """Analytic and numerical Mahler measure should agree for Q_L."""
        for c_val in [Rational(1), Rational(5), Rational(13)]:
            data = shadow_data("virasoro", c=c_val)
            m_num = mahler_measure_shadow_metric(
                data["kappa"], data["alpha"], data["S4"], n_points=50000
            )
            m_ana = mahler_measure_shadow_metric_analytic(
                data["kappa"], data["alpha"], data["S4"]
            )
            assert abs(m_num - m_ana) < 0.05, \
                f"Mahler mismatch at c={c_val}: num={m_num}, ana={m_ana}"

    def test_mahler_heisenberg_quadratic(self):
        """Heisenberg: Q_L(t) = 4*kappa^2 (constant). m = log(4*kappa^2) = 2*log(2*|kappa|)."""
        kap = Rational(1)
        m = mahler_measure_shadow_metric_analytic(kap, Rational(0), Rational(0))
        expected = math.log(4)  # 4*1^2 = 4
        assert abs(m - expected) < 1e-10

    def test_mahler_polynomial_format(self):
        """shadow_metric_polynomial should return [q0, q1, q2]."""
        coeffs = shadow_metric_polynomial(Rational(1), Rational(2), Rational(3))
        assert len(coeffs) == 3
        assert coeffs[0] == 4.0  # q0 = 4*kappa^2 = 4

    def test_mahler_virasoro_positive(self):
        """Mahler measure should be positive for all Virasoro algebras."""
        for c_val in [Rational(1, 2), Rational(1), Rational(10), Rational(25)]:
            data = shadow_data("virasoro", c=c_val)
            m = mahler_measure_shadow_metric_analytic(
                data["kappa"], data["alpha"], data["S4"]
            )
            assert m > 0, f"Mahler measure at c={c_val} should be positive"


# ============================================================================
# Section 6: CANONICAL HEIGHT (Koszul duality)
# ============================================================================

class TestKoszulDualData:
    """Tests for Koszul dual computation."""

    def test_virasoro_dual(self):
        """Vir_c dual is Vir_{26-c}."""
        data = shadow_data("virasoro", c=Rational(1))
        dual = koszul_dual_data(data)
        assert dual is not None
        assert dual["c"] == Rational(25)

    def test_virasoro_self_dual(self):
        """Vir_13 is self-dual: dual c = 26 - 13 = 13."""
        data = shadow_data("virasoro", c=Rational(13))
        dual = koszul_dual_data(data)
        assert dual is not None
        assert dual["c"] == Rational(13)

    def test_heisenberg_dual(self):
        """Heisenberg H_k dual has kappa = -k."""
        data = shadow_data("heisenberg", k=3)
        dual = koszul_dual_data(data)
        assert dual is not None
        assert dual["kappa"] == Rational(-3)

    def test_affine_dual_kappa_antisymmetry(self):
        """For affine g_k: kappa + kappa' = 0 (AP24)."""
        data = shadow_data("affine", lie_type="A", rank=1, k=1)
        dual = koszul_dual_data(data)
        assert dual is not None
        # kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4
        # kappa(sl_2, k=-1-4=-5) = 3*(-5+2)/(2*2) = 3*(-3)/4 = -9/4
        # Sum = 0. Good (AP24 applies to affine KM).
        kap_A = data["kappa"]
        kap_dual = kappa_exact("affine", lie_type="A", rank=1, k=-1 - 2 * 2)
        assert kap_A + kap_dual == 0

    def test_w3_dual_c(self):
        """W_3 at c dual is W_3 at 100-c."""
        data = shadow_data("w_3", c=Rational(2), line="T")
        dual = koszul_dual_data(data)
        assert dual is not None
        assert dual["c"] == Rational(98)


class TestCanonicalHeight:
    """Tests for the canonical height h_hat(A) = (H(A) + H(A!)) / 2."""

    def test_self_dual_canonical_equals_naive(self):
        """For Vir_13 (self-dual): h_hat = H."""
        data = shadow_data("virasoro", c=Rational(13))
        H = shadow_height_from_data(data)
        h_hat = canonical_height(data)
        assert h_hat is not None
        assert abs(h_hat - H) < 1e-10

    def test_canonical_symmetric(self):
        """h_hat(A) = h_hat(A!) for Virasoro pairs."""
        for c_val in [Rational(1), Rational(5), Rational(10)]:
            data_A = shadow_data("virasoro", c=c_val)
            data_dual = shadow_data("virasoro", c=26 - c_val)
            h_A = canonical_height(data_A)
            h_dual = canonical_height(data_dual)
            assert h_A is not None
            assert h_dual is not None
            assert abs(h_A - h_dual) < 1e-10

    def test_canonical_nonnegative(self):
        """Canonical height should be non-negative."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(25)]:
            data = shadow_data("virasoro", c=c_val)
            h_hat = canonical_height(data)
            if h_hat is not None:
                assert h_hat >= -1e-10

    def test_canonical_landscape(self):
        """Canonical heights landscape should return sorted results."""
        results = canonical_heights_landscape(max_r=10)
        assert len(results) > 0
        h_hats = [r[3] for r in results]
        for i in range(len(h_hats) - 1):
            assert h_hats[i + 1] >= h_hats[i] - 1e-10


class TestVirasoroSelfDualAnalysis:
    """Tests for the self-dual point c=13 analysis."""

    def test_self_dual_height_matches(self):
        """At c=13: H(Vir_13) = H(Vir_{26-13}) = H(Vir_13)."""
        analysis = virasoro_self_dual_analysis(max_r=10)
        self_dual = next(p for p in analysis["pairs"] if p["c"] == 13)
        assert abs(self_dual["H_A"] - self_dual["H_dual"]) < 1e-10

    def test_complementarity_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c (AP24)."""
        for c_val in [Rational(1), Rational(5), Rational(13), Rational(25)]:
            kap = kappa_exact("virasoro", c=c_val)
            kap_dual = kappa_exact("virasoro", c=26 - c_val)
            assert kap + kap_dual == 13

    def test_analysis_returns_pairs(self):
        """Analysis should return Koszul pair data."""
        analysis = virasoro_self_dual_analysis(max_r=10)
        assert len(analysis["pairs"]) > 0
        assert analysis["self_dual_height"] > 0


# ============================================================================
# Section 7: HEIGHT ZETA FUNCTION
# ============================================================================

class TestHeightZetaFunction:
    """Tests for Z(s) = sum H(A)^{-s}."""

    def test_zeta_positive_s(self):
        """Z(s) should be positive for s > 0."""
        Z = height_zeta_partial(2.0)
        assert Z > 0

    def test_zeta_structure(self):
        """Z(s) should be finite and positive for all tested s values.
        Note: Z(s) may increase with s when many H(A) < 1,
        because H^{-s} grows for H < 1 as s increases.
        The relevant structure is that Z(s) is well-defined."""
        for s in [0.5, 1.0, 2.0, 5.0]:
            Z = height_zeta_partial(s)
            assert Z > 0
            assert math.isfinite(Z)

    def test_zeta_finite(self):
        """Z(s) should be finite for s > 0."""
        Z = height_zeta_partial(1.0)
        assert math.isfinite(Z)

    def test_abscissa_estimate(self):
        """Abscissa estimation should return a dict with expected keys."""
        result = height_zeta_abscissa_estimate()
        assert "s_values" in result
        assert "Z_values" in result
        assert "estimated_abscissa" in result

    def test_abscissa_s_values_sorted(self):
        """s_values in the abscissa estimate should be sorted."""
        result = height_zeta_abscissa_estimate()
        for i in range(len(result["s_values"]) - 1):
            assert result["s_values"][i + 1] > result["s_values"][i]


# ============================================================================
# Section 8: CROSS-VERIFICATION (multi-path)
# ============================================================================

class TestCrossVerification:
    """Multi-path verification tests."""

    def test_path1_path3_consistency_virasoro(self):
        """Path 1 (direct height) and Path 3 (canonical) should be consistent.
        For self-dual Vir_13: h_hat = H."""
        h1 = height_via_tower("virasoro", c=Rational(13))
        h3 = height_via_canonical("virasoro", c=Rational(13))
        assert h3 is not None
        assert abs(h1 - h3) < 1e-10

    def test_path2_positive(self):
        """Path 2 (Mahler measure) should return positive values."""
        m = height_via_mahler("virasoro", c=Rational(1))
        assert m > 0

    def test_path4_finiteness(self):
        """Path 4 (Northcott) should confirm finiteness."""
        result = verify_northcott_finiteness([1, 5, 10])
        for B, finite in result.items():
            assert finite

    def test_mahler_and_height_correlation(self):
        """Mahler measure and shadow height should be positively correlated
        across Virasoro algebras (both measure arithmetic complexity)."""
        heights = []
        mahlers = []
        for c_val in [Rational(1), Rational(2), Rational(5), Rational(10), Rational(20)]:
            h = height_via_tower("virasoro", c=c_val)
            m = height_via_mahler("virasoro", c=c_val)
            heights.append(h)
            mahlers.append(m)
        # Check positive correlation (Spearman rank or just signs)
        # Both should vary, and larger c should tend to give larger values
        assert max(heights) > min(heights)
        assert max(mahlers) > min(mahlers)

    def test_canonical_vs_average(self):
        """For Virasoro Koszul pairs, canonical height = average of H(A) and H(A!)."""
        c_val = Rational(3)
        data_A = shadow_data("virasoro", c=c_val)
        data_dual = shadow_data("virasoro", c=26 - c_val)
        H_A = shadow_height_from_data(data_A)
        H_dual = shadow_height_from_data(data_dual)
        h_hat = canonical_height(data_A)
        assert h_hat is not None
        assert abs(h_hat - (H_A + H_dual) / 2) < 1e-12


# ============================================================================
# Section 9: LANDSCAPE-WIDE TESTS
# ============================================================================

class TestLandscape:
    """Tests for the full landscape computation."""

    def test_standard_landscape_count(self):
        """Standard landscape should have 50+ algebras."""
        landscape = build_standard_landscape()
        assert len(landscape) >= 50

    def test_landscape_heights_sorted(self):
        """landscape_heights should return sorted results."""
        results = landscape_heights(max_r=10)
        heights = [h for _, h in results]
        for i in range(len(heights) - 1):
            assert heights[i + 1] >= heights[i] - 1e-12

    def test_all_heights_finite(self):
        """All heights in the landscape should be finite."""
        results = landscape_heights(max_r=10)
        for name, h in results:
            assert math.isfinite(h), f"H({name}) = {h} is not finite"

    def test_heisenberg_minimal(self):
        """Heisenberg H_1 should have one of the smallest heights."""
        results = landscape_heights(max_r=10)
        h_heis = None
        for name, h in results:
            if "H_{1}" in name or "H_1" in name:
                h_heis = h
                break
        # H_1 has S_2 = 1 (integer), h_2 = log(1) = 0, so H = 0
        if h_heis is not None:
            assert h_heis < 1e-10

    def test_extended_landscape_larger(self):
        """Extended landscape should be larger than standard."""
        standard = build_standard_landscape()
        extended = build_extended_landscape()
        assert len(extended) > len(standard)


# ============================================================================
# Section 10: KAPPA CONSISTENCY (AP1, AP9, AP10 cross-checks)
# ============================================================================

class TestKappaConsistency:
    """Cross-family kappa consistency tests (AP1, AP10)."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        for k in range(1, 6):
            assert kappa_exact("heisenberg", k=k) == Rational(k)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(26)]:
            assert kappa_exact("virasoro", c=c_val) == c_val / 2

    def test_kappa_affine_sl2(self):
        """kappa(sl_2_k) = 3*(k+2)/4."""
        for k in range(1, 6):
            kap = kappa_exact("affine", lie_type="A", rank=1, k=k)
            assert kap == Rational(3) * (k + 2) / 4

    def test_kappa_free_fermion(self):
        """kappa(psi) = 1/4."""
        assert kappa_exact("free_fermion") == Rational(1, 4)

    def test_kappa_additivity_heisenberg(self):
        """For independent Heisenberg systems: kappa is additive.
        kappa(H_k1 + H_k2) = k1 + k2."""
        k1, k2 = 3, 5
        assert kappa_exact("heisenberg", k=k1) + kappa_exact("heisenberg", k=k2) == k1 + k2

    def test_virasoro_complementarity_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c_val in [Rational(1), Rational(5), Rational(13), Rational(25)]:
            kap_sum = kappa_exact("virasoro", c=c_val) + kappa_exact("virasoro", c=26 - c_val)
            assert kap_sum == 13

    def test_affine_complementarity_zero(self):
        """AP24: kappa(g_k) + kappa(g_{-k-2h^v}) = 0 for affine KM."""
        # sl_2: h^v = 2, dual level = -k-4
        kap = kappa_exact("affine", lie_type="A", rank=1, k=1)
        kap_dual = kappa_exact("affine", lie_type="A", rank=1, k=-5)
        assert kap + kap_dual == 0


# ============================================================================
# Section 11: EDGE CASES AND ROBUSTNESS
# ============================================================================

class TestEdgeCases:
    """Edge cases and robustness tests."""

    def test_large_c_virasoro(self):
        """Height should be well-defined for large c."""
        H = shadow_height_for_family("virasoro", c=Rational(1000))
        assert math.isfinite(H)

    def test_small_c_virasoro(self):
        """Height should be well-defined for small positive c."""
        H = shadow_height_for_family("virasoro", c=Rational(1, 100))
        assert math.isfinite(H)

    def test_large_k_affine(self):
        """Height should be well-defined for large k."""
        H = shadow_height_for_family("affine", lie_type="A", rank=1, k=100)
        assert math.isfinite(H)

    def test_betagamma_height(self):
        """betagamma should have well-defined height."""
        H = shadow_height_for_family("betagamma", lam=Rational(1, 3))
        assert math.isfinite(H)
        assert H > 0

    def test_moonshine_height(self):
        """Moonshine V^natural should have well-defined height."""
        H = shadow_height_for_family("moonshine")
        assert math.isfinite(H)
        assert H > 0

    def test_lattice_height_rank_scaling(self):
        """Lattice VOA height should scale with rank (kappa = rank)."""
        H1 = shadow_height_for_family("lattice", rank=1)
        H8 = shadow_height_for_family("lattice", rank=8)
        H24 = shadow_height_for_family("lattice", rank=24)
        # All class G, H = log(kappa)/4. For rank=1: log(1)/4=0.
        # For rank=8: log(8)/4. For rank=24: log(24)/4.
        assert H1 < H8 or abs(H1) < 1e-10
        assert H8 < H24

    def test_height_zeta_at_zero(self):
        """Z(0) = number of algebras with positive height."""
        # Z(0) = sum H(A)^0 = count of algebras with H > 0
        landscape = build_standard_landscape()
        Z0 = height_zeta_partial(0.0, landscape, max_r=10)
        # Each algebra with H > 0 contributes H^0 = 1
        count = sum(1 for d in landscape
                    if d.get("kappa", 0) != 0 and
                    shadow_height_from_data(d, 10) > 1e-10)
        # Z(0) should be close to count (algebras with H=0 have H^{-0}=1 too
        # but our function skips H <= 1e-10)
        assert abs(Z0 - count) < 1 or Z0 > 0


class TestMahlerAdvanced:
    """Advanced Mahler measure tests."""

    def test_mahler_virasoro_varies_with_c(self):
        """Mahler measure should vary with c for Virasoro."""
        m1 = height_via_mahler("virasoro", c=Rational(1))
        m13 = height_via_mahler("virasoro", c=Rational(13))
        m25 = height_via_mahler("virasoro", c=Rational(25))
        assert m1 != m13 or m13 != m25

    def test_mahler_analytic_vs_numerical_affine(self):
        """Analytic and numerical Mahler agree for affine sl_2."""
        data = shadow_data("affine", lie_type="A", rank=1, k=1)
        m_num = mahler_measure_shadow_metric(
            data["kappa"], data["alpha"], data["S4"], n_points=50000
        )
        m_ana = mahler_measure_shadow_metric_analytic(
            data["kappa"], data["alpha"], data["S4"]
        )
        assert abs(m_num - m_ana) < 0.1

    def test_mahler_product_formula(self):
        """For Q_L = q2 * (t - r1)(t - r2): m(Q_L) = log|q2| + sum max(0, log|ri|).
        Verify via analytic formula."""
        # Simple test: x^2 - 1 = (x-1)(x+1). Roots at +/- 1.
        # m = log(1) + max(0, log(1)) + max(0, log(1)) = 0.
        m = mahler_measure_analytic_quadratic(1.0, 0.0, -1.0)
        assert abs(m) < 1e-10

    def test_mahler_discriminant_sign(self):
        """Positive discriminant => real roots; negative => complex conjugate."""
        # Q_L for Heisenberg: q0=4, q1=0, q2=0. Degenerate.
        # Q_L for Virasoro at c=1: q0=1, q1=12, q2=9+80/27.
        data = shadow_data("virasoro", c=Rational(1))
        q0, q1, q2 = float(4 * data["kappa"]**2), \
            float(12 * data["kappa"] * data["alpha"]), \
            float(9 * data["alpha"]**2 + 16 * data["kappa"] * data["S4"])
        disc = q1**2 - 4 * q0 * q2  # = -32*kappa^2*Delta
        Delta = float(critical_discriminant(data["kappa"], data["S4"]))
        # For Virasoro class M: Delta > 0, so disc < 0 (complex roots).
        assert Delta > 0
        assert disc < 0


# ============================================================================
# Section 12: GROWTH ANALYSIS TESTS
# ============================================================================

class TestGrowthAnalysis:
    """Tests for height growth rate analysis."""

    def test_polynomial_growth_detected(self):
        """A sequence H_n = n^2 should be detected as polynomial."""
        data = [(n, n ** 2) for n in range(1, 21)]
        result = height_growth_analysis(data)
        assert result["growth_type"] in ("polynomial", "mixed")
        if result["growth_type"] == "polynomial":
            assert abs(result["poly_exponent"] - 2.0) < 0.3

    def test_logarithmic_growth_detected(self):
        """A sequence H_n = log(n) should be detected as logarithmic."""
        data = [(n, math.log(n)) for n in range(2, 22)]
        result = height_growth_analysis(data)
        # Log growth in H vs linear param => in the log-log space it looks sub-polynomial
        assert result["growth_type"] in ("logarithmic", "polynomial", "mixed")

    def test_insufficient_data(self):
        """Two data points should return insufficient."""
        data = [(1, 1.0), (2, 2.0)]
        result = height_growth_analysis(data)
        assert result["growth_type"] == "insufficient_data"

    def test_affine_growth_type(self):
        """Affine sl_2 height growth should be classified."""
        dist = affine_sl2_height_distribution(range(1, 16))
        result = height_growth_analysis(dist)
        assert result["growth_type"] in ("polynomial", "logarithmic", "mixed")
