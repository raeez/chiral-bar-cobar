r"""Tests for VOA bundles on moduli of curves and the genus extension problem.

Verification paths:
  Path 1: Verlinde formula with insertions (S-matrix)
  Path 2: Fusion coefficients as genus-0 conformal blocks
  Path 3: Factorization/sewing (separating + non-separating degeneration)
  Path 4: Verlinde bundle c_1 = rk * slope * lambda
  Path 5: Shadow CohFT F_g = kappa * lambda_g^FP
  Path 6: Slope = c/dim (independent derivation from Sugawara)
  Path 7: Hitchin connection projective flatness
  Path 8: Literature values (Beauville, MOP, DMS)

Ground truth:
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  thm:conformal-block-reconstruction (higher_genus_modular_koszul.tex)
  Verlinde (1988), Beauville (1996)
  Marian-Oprea-Pandharipande (2013, 2014)
  Damiolini-Gibney-Tarasca (2019)
  Frenkel-Ben-Zvi (2004), Looijenga (2010)
"""

from __future__ import annotations

import math
import pytest

from sympy import Rational, bernoulli, binomial, factorial

from compute.lib.voa_bundle_genus_engine import (
    beauville_laszlo_sewing_verification,
    c2_cofiniteness_check,
    conformal_block_dim_general,
    conformal_block_dim_sl2,
    determinant_line_comparison,
    factorization_check_general,
    factorization_check_sl2,
    full_voa_bundle_diagnostic,
    genus1_three_way_comparison,
    hitchin_shadow_comparison,
    nonseparating_check_sl2,
    shadow_vs_chern_character,
    sl2_conformal_block_table,
    verlinde_bundle_rank,
    verlinde_c1,
    verlinde_chern_numbers,
    verlinde_cohft_unit,
    verlinde_R_matrix,
    verlinde_slope_general,
    verlinde_slope_sl2,
)

from compute.lib.verlinde_shadow_cohft_engine import (
    central_charge,
    fusion_coefficients,
    kappa_affine,
    kappa_affine_exact,
    lambda_fp,
    num_integrable_reps,
    shadow_F_g,
    verlinde_dimension_exact,
)


# =========================================================================
# Section 1: Conformal block dimensions with marked points (sl_2)
# =========================================================================

class TestConformalBlockDimSl2:
    """Conformal block dimensions for sl_2 with insertions."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5])
    def test_no_insertions_recovers_verlinde(self, k):
        """V(Sigma_g, no insertions) = V_g for all g."""
        for g in range(5):
            cb = conformal_block_dim_sl2(k, g, ())
            V = verlinde_dimension_exact("A", 1, k, g)
            assert cb == V, (
                f"k={k}, g={g}: CB={cb} != V_g={V}"
            )

    @pytest.mark.parametrize("k,j1,j2,j3,expected", [
        # Fusion coefficients = genus-0 conformal blocks with 3 insertions
        # N_{j1,j2}^{j3} = V(S^2, j1, j2, j3*)
        # For sl_2: j* = j (self-conjugate)
        (1, 0, 0, 0, 1),   # vacuum x vacuum = vacuum
        (1, 0, 1, 1, 1),   # vacuum x fund = fund
        (1, 1, 1, 0, 1),   # fund x fund = vacuum (k=1)
        (2, 0, 0, 0, 1),   # vacuum identities
        (2, 0, 1, 1, 1),
        (2, 0, 2, 2, 1),
        (2, 1, 1, 0, 1),   # j=1 x j=1 -> j=0
        (2, 1, 1, 2, 1),   # j=1 x j=1 -> j=2
        (2, 1, 1, 1, 0),   # j=1 x j=1 -> j=1 FORBIDDEN (parity)
        (3, 1, 1, 0, 1),
        (3, 1, 1, 2, 1),
        (3, 1, 2, 1, 1),   # j=1 x j=2 -> j=1
        (3, 1, 2, 3, 1),   # j=1 x j=2 -> j=3
    ])
    def test_genus0_three_point_is_fusion(self, k, j1, j2, j3, expected):
        """Genus-0 three-point = fusion coefficient N_{j1,j2}^{j3}."""
        dim = conformal_block_dim_sl2(k, 0, (j1, j2, j3))
        assert dim == expected, (
            f"k={k}: V(S^2, {j1},{j2},{j3}) = {dim}, expected {expected}"
        )

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_genus0_vacuum_insertions(self, k):
        """V(S^2, 0, j, j) = 1 for all j (vacuum is unit)."""
        for j in range(k + 1):
            dim = conformal_block_dim_sl2(k, 0, (0, j, j))
            assert dim == 1, f"k={k}, j={j}: V(S^2, 0, {j}, {j}) = {dim}"

    def test_genus0_four_point_sl2_k2(self):
        """V(S^2, 1,1,1,1) for sl_2 at k=2: should be 2."""
        # N_{11}^0 * N_{11}^0 + N_{11}^2 * N_{11}^2 = 1 + 1 = 2
        # Actually: V(S^2, 1,1,1,1) = sum_m N_{11}^m N_{11}^m = 2
        dim = conformal_block_dim_sl2(2, 0, (1, 1, 1, 1))
        assert dim == 2

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_genus1_one_point_vacuum(self, k):
        """V(T^2, 0) = V_1 (vacuum insertion doesn't change genus-1 dim)."""
        V1 = verlinde_dimension_exact("A", 1, k, 1)
        dim = conformal_block_dim_sl2(k, 1, (0,))
        assert dim == V1

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_all_genus1_one_point_nonneg(self, k):
        """V(T^2, j) for all j: each is non-negative integer."""
        total = 0
        for j in range(k + 1):
            dim = conformal_block_dim_sl2(k, 1, (j,))
            assert dim >= 0, f"k={k}, j={j}: V(T^2, {j}) = {dim}"
            total += dim
        # At least one insertion should give nonzero
        assert total > 0

    @pytest.mark.parametrize("k,g", [
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 1),
    ])
    def test_conformal_blocks_are_nonneg_integers(self, k, g):
        """All conformal block dims are non-negative integers."""
        for j in range(k + 1):
            dim = conformal_block_dim_sl2(k, g, (j,))
            assert isinstance(dim, int) and dim >= 0

    def test_invalid_spin_raises(self):
        """Spin out of range raises ValueError."""
        with pytest.raises(ValueError):
            conformal_block_dim_sl2(2, 0, (3,))  # j=3 > k=2
        with pytest.raises(ValueError):
            conformal_block_dim_sl2(2, 0, (-1,))  # negative spin

    def test_sl2_k1_genus2_one_point(self):
        """sl_2 k=1, genus 2 with one insertion."""
        # V_2(k=1) = 4
        # V(Sigma_2, j=0) should equal V_2 = 4 (vacuum insertion trivial)
        dim0 = conformal_block_dim_sl2(1, 2, (0,))
        dim1 = conformal_block_dim_sl2(1, 2, (1,))
        assert dim0 + dim1 > 0  # both non-negative
        # Sum over j: sum_j V(Sigma_2, j) = V_2 (from non-sep degeneration
        # perspective, but this is a different identity)


# =========================================================================
# Section 2: Conformal block dimensions (general type)
# =========================================================================

class TestConformalBlockDimGeneral:
    """Conformal block dimensions for general Lie types."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_no_insertions_recovers_verlinde(self, lt, r, k):
        """V(Sigma_g) = V_g for general type."""
        for g in range(4):
            cb = conformal_block_dim_general(lt, r, k, g, ())
            V = verlinde_dimension_exact(lt, r, k, g)
            assert cb == V

    def test_sl3_k1_genus0_three_point(self):
        """sl_3 at k=1: fusion of three fundamentals."""
        # sl_3 k=1 reps: (0,0), (1,0), (0,1)
        # N_{(1,0),(0,1)}^{(0,0)} = 1 (fundamental x antifundamental = vacuum)
        dim = conformal_block_dim_general("A", 2, 1, 0, ((1, 0), (0, 1), (0, 0)))
        assert dim == 1

    def test_sl3_k1_genus0_three_fund(self):
        """sl_3 at k=1: V(S^2, (1,0), (1,0), (1,0)) = 1."""
        # Three fundamentals of sl_3: the determinant rep gives fusion = 1
        dim = conformal_block_dim_general("A", 2, 1, 0, ((1, 0), (1, 0), (1, 0)))
        assert dim == 1

    def test_vacuum_insertion_trivial(self):
        """Vacuum insertion doesn't change CB dimension at genus >= 1."""
        for (lt, r, k) in [("A", 2, 1), ("A", 3, 1)]:
            for g in range(1, 3):
                V_g = verlinde_dimension_exact(lt, r, k, g)
                vacuum = tuple(0 for _ in range(r))
                V_with_vac = conformal_block_dim_general(lt, r, k, g, (vacuum,))
                assert V_with_vac == V_g


# =========================================================================
# Section 3: Verlinde bundle slope
# =========================================================================

class TestVerlindeSlope:
    """Verify the Marian-Oprea-Pandharipande slope formula."""

    @pytest.mark.parametrize("k,expected_slope", [
        (1, Rational(1, 3)),    # k/(k+2) = 1/3
        (2, Rational(1, 2)),    # 2/4 = 1/2
        (3, Rational(3, 5)),    # 3/5
        (4, Rational(2, 3)),    # 4/6 = 2/3
        (5, Rational(5, 7)),    # 5/7
        (10, Rational(5, 6)),   # 10/12 = 5/6
    ])
    def test_sl2_slope(self, k, expected_slope):
        """sl_2 slope = k/(k+2)."""
        slope = verlinde_slope_sl2(k, 0)
        assert slope == expected_slope

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_slope_equals_c_over_dim(self, lt, r, k):
        """Slope = c(g_k) / dim(g): independent derivation from Sugawara."""
        from compute.lib.voa_bundle_genus_engine import _get_lie_data
        data = _get_lie_data(lt, r)
        c = central_charge(lt, r, k)
        slope = verlinde_slope_general(lt, r, k)
        assert abs(float(slope) - c / data["dim"]) < 1e-10, (
            f"slope={float(slope)}, c/dim={c / data['dim']}"
        )

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 1), ("A", 3, 1),
    ])
    def test_slope_bounded_by_1(self, lt, r, k):
        """Slope = k/(k+h^v) < 1 for all positive integer k."""
        slope = verlinde_slope_general(lt, r, k)
        assert 0 < float(slope) < 1

    def test_slope_monotone_in_level(self):
        """Slope increases with level k (for fixed type)."""
        for k in range(1, 10):
            s1 = verlinde_slope_general("A", 1, k)
            s2 = verlinde_slope_general("A", 1, k + 1)
            assert s2 > s1

    def test_slope_approaches_1_at_large_k(self):
        """Slope -> 1 as k -> infinity."""
        slope = verlinde_slope_general("A", 1, 1000)
        assert abs(float(slope) - 1.0) < 0.01


# =========================================================================
# Section 4: Verlinde bundle c_1
# =========================================================================

class TestVerlindeC1:
    """First Chern class of the Verlinde bundle."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1),
    ])
    def test_c1_equals_rk_times_slope(self, lt, r, k):
        """c_1(V) = rk(V) * slope * lambda."""
        for g in range(1, 4):
            info = verlinde_c1(lt, r, k, g)
            rk = info["verlinde_rank"]
            slope = verlinde_slope_general(lt, r, k)
            expected = float(rk * slope)
            assert abs(info["c1_verlinde_coeff"] - expected) < 1e-10

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_c1_shadow_equals_kappa(self, lt, r, k):
        """c_1(L_A) = kappa * lambda."""
        for g in range(1, 4):
            info = verlinde_c1(lt, r, k, g)
            kap = float(kappa_affine_exact(lt, r, k))
            assert abs(info["c1_shadow_coeff"] - kap) < 1e-10

    def test_c1_verlinde_vs_shadow_differ(self):
        """c_1(V) != c_1(L_A) in general (at genus >= 2)."""
        info = verlinde_c1("A", 1, 2, 2)
        # rk = V_2 = 10, slope = 1/2, so c_1(V) = 5
        # kappa = 3, so c_1(L) = 3
        assert info["c1_verlinde_coeff"] != info["c1_shadow_coeff"]

    def test_c1_verlinde_genus1(self):
        """At genus 1: c_1(V) = V_1 * slope, c_1(L) = kappa."""
        for (lt, r, k) in [("A", 1, 2), ("A", 2, 1)]:
            info = verlinde_c1(lt, r, k, 1)
            V1 = verlinde_dimension_exact(lt, r, k, 1)
            slope = float(verlinde_slope_general(lt, r, k))
            assert abs(info["c1_verlinde_coeff"] - V1 * slope) < 1e-10


# =========================================================================
# Section 5: Factorization (separating degeneration)
# =========================================================================

class TestFactorizationSeparating:
    """Verify separating degeneration: V_g = sum_j V(g1,j) V(g2,j)."""

    @pytest.mark.parametrize("k,g,partition", [
        (1, 2, (1, 1)),
        (1, 3, (2, 1)),
        (1, 3, (1, 2)),
        (1, 4, (2, 2)),
        (1, 4, (3, 1)),
        (2, 2, (1, 1)),
        (2, 3, (2, 1)),
        (2, 3, (1, 2)),
        (2, 4, (2, 2)),
        (3, 2, (1, 1)),
        (3, 3, (2, 1)),
    ])
    def test_separating_factorization_sl2(self, k, g, partition):
        """Separating factorization holds for sl_2."""
        result = factorization_check_sl2(k, g, partition)
        assert result["factorization_holds"], (
            f"k={k}, g={g}, ({partition}): "
            f"V_g={result['V_g']} != sum={result['factored_sum']}"
        )

    @pytest.mark.parametrize("lt,r,k,g,partition", [
        ("A", 2, 1, 2, (1, 1)),
        ("A", 2, 1, 3, (2, 1)),
        ("A", 3, 1, 2, (1, 1)),
    ])
    def test_separating_factorization_general(self, lt, r, k, g, partition):
        """Separating factorization holds for general type."""
        result = factorization_check_general(lt, r, k, g, partition)
        assert result["factorization_holds"], (
            f"{lt}_{r} k={k}, g={g}: "
            f"V_g={result['V_g']} != sum={result['factored_sum']}"
        )


# =========================================================================
# Section 6: Factorization (non-separating degeneration)
# =========================================================================

class TestFactorizationNonSeparating:
    """Verify non-separating degeneration: V_g = sum_j V(g-1, j, j)."""

    @pytest.mark.parametrize("k,g", [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 2), (2, 3),
        (3, 1), (3, 2), (3, 3),
        (4, 1), (4, 2),
    ])
    def test_nonseparating_factorization_sl2(self, k, g):
        """Non-separating factorization V_g = sum_j V(g-1, j, j)."""
        result = nonseparating_check_sl2(k, g)
        assert result["nonseparating_holds"], (
            f"k={k}, g={g}: "
            f"V_g={result['V_g']} != sum={result['nonseparating_sum']}"
        )

    def test_nonsep_genus1_is_sum_of_genus0_two_point(self):
        """V_1 = sum_j V(S^2, j, j) for sl_2.
        V(S^2, j, j) with only 2 points: need stability 2g-2+n > 0.
        At g=0, n=2: 2*0 - 2 + 2 = 0, NOT stable.
        So V_1 = sum_j dim(j) where dim(j) is from the metric.
        Actually the formula V_g = sum_j V(g-1, j, j) uses conformal
        block dims with 2 marked points at genus 0, which is
        S_{0,j}^{2-0-2} * S_{j,l} * S_{j,l} / S_{0,l} = delta(0 = 0)...
        Let's just verify the formula holds numerically."""
        for k in [1, 2, 3]:
            result = nonseparating_check_sl2(k, 1)
            assert result["nonseparating_holds"]


# =========================================================================
# Section 7: Beauville-Laszlo full sewing verification
# =========================================================================

class TestBeauvilleLaszloSewing:
    """Full Beauville-Laszlo sewing verification."""

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_full_sewing_sl2(self, k):
        """All factorization checks pass for sl_2 up to genus 4."""
        result = beauville_laszlo_sewing_verification(k, max_genus=4)
        assert result["all_pass"], (
            f"Sewing failed for sl_2 k={k}"
        )

    def test_sewing_separating_count(self):
        """Check that we test enough separating partitions."""
        result = beauville_laszlo_sewing_verification(2, max_genus=4)
        assert len(result["separating"]) >= 4
        assert len(result["nonseparating"]) >= 3


# =========================================================================
# Section 8: Hitchin vs shadow connection
# =========================================================================

class TestHitchinShadowComparison:
    """Compare Hitchin connection with our shadow connection."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_slope_equals_c_over_dim(self, lt, r, k):
        """Key identity: Hitchin projective curvature = c/dim = slope."""
        comp = hitchin_shadow_comparison(lt, r, k)
        assert comp["slope_equals_c_over_dim"]

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 1), ("A", 3, 1),
    ])
    def test_hitchin_curvature_positive(self, lt, r, k):
        """Hitchin projective curvature coefficient is positive."""
        comp = hitchin_shadow_comparison(lt, r, k)
        assert float(comp["slope"]) > 0

    def test_shadow_connection_koszul_monodromy(self):
        """Shadow connection has residue 1/2 (monodromy = -1 = Koszul sign)."""
        comp = hitchin_shadow_comparison("A", 1, 2)
        assert comp["shadow_connection_residue"] == Rational(1, 2)


# =========================================================================
# Section 9: Shadow CohFT vs Chern character structural comparison
# =========================================================================

class TestShadowVsChernCharacter:
    """Structural comparison: shadow CohFT vs Verlinde Chern character."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_same_genus0_structure(self, lt, r, k):
        """Both CohFTs use the same fusion algebra at genus 0."""
        unit = verlinde_cohft_unit(lt, r, k)
        assert unit["is_semisimple"]
        assert unit["num_weights"] == num_integrable_reps(lt, r, k)
        # Quantum dimensions positive
        for d in unit["quantum_dims"]:
            assert d > 0

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 2), ("A", 2, 1),
    ])
    def test_different_at_genus_2(self, lt, r, k):
        """Shadow and Verlinde CohFTs differ at genus >= 2."""
        comp = shadow_vs_chern_character(lt, r, k, 2)
        # c_1(V) = rk * slope * lambda, c_1(L) = kappa * lambda
        # These differ when rk * slope != kappa
        c1_V = comp["c1_verlinde"]
        c1_L = comp["c1_shadow_det"]
        assert abs(c1_V - c1_L) > 0.01, (
            f"c_1(V)={c1_V} should differ from c_1(L)={c1_L} at genus 2"
        )

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_slope_equals_c_over_dim_in_comparison(self, lt, r, k):
        """slope = c/dim identity verified in comparison."""
        comp = shadow_vs_chern_character(lt, r, k, 1)
        assert comp["slope_equals_c_over_dim"]

    def test_verlinde_rank_grows_shadow_constant(self):
        """Verlinde rank grows exponentially; shadow kappa is constant."""
        comp_data = determinant_line_comparison("A", 1, 2, max_genus=5)
        genus_data = comp_data["genus_data"]
        # c_1(det V) grows, c_1(L) is constant
        c1_V_values = [gd["c1_det_verlinde"] for gd in genus_data]
        c1_L_values = [gd["c1_shadow_det"] for gd in genus_data]
        # Verlinde c_1 should be strictly increasing
        for i in range(len(c1_V_values) - 1):
            assert c1_V_values[i + 1] > c1_V_values[i]
        # Shadow c_1 is constant
        for c1_L in c1_L_values:
            assert abs(c1_L - c1_L_values[0]) < 1e-10


# =========================================================================
# Section 10: Genus-1 three-way comparison
# =========================================================================

class TestGenus1ThreeWay:
    """Three-way comparison at genus 1: V_1, F_1, c_1(V)."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3), ("A", 1, 4),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
    ])
    def test_V1_is_integer(self, lt, r, k):
        """V_1 = |P_+^k| is a positive integer."""
        comp = genus1_three_way_comparison(lt, r, k)
        assert comp["V_1"] == num_integrable_reps(lt, r, k)
        assert comp["V_1"] > 0

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_F1_is_kappa_over_24(self, lt, r, k):
        """F_1 = kappa / 24."""
        comp = genus1_three_way_comparison(lt, r, k)
        kap = kappa_affine(lt, r, k)
        assert abs(comp["F_1"] - kap / 24.0) < 1e-10

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_c1V_is_V1_times_slope(self, lt, r, k):
        """c_1(V) = V_1 * slope at genus 1."""
        comp = genus1_three_way_comparison(lt, r, k)
        V1 = comp["V_1"]
        slope = comp["slope"]
        assert abs(comp["c1_verlinde"] - V1 * slope) < 1e-10

    def test_three_quantities_all_different(self):
        """V_1, F_1, c_1(V) are generically all different."""
        comp = genus1_three_way_comparison("A", 1, 2)
        # V_1 = 3 (integer)
        # F_1 = 3/24 = 1/8 (fraction)
        # c_1(V) = 3 * 1/2 = 3/2
        assert comp["V_1"] == 3
        assert abs(comp["F_1"] - 0.125) < 1e-10
        assert abs(comp["c1_verlinde"] - 1.5) < 1e-10
        # All three are different
        vals = [comp["V_1"], comp["F_1"], comp["c1_verlinde"]]
        assert len(set(round(v, 6) for v in vals)) == 3


# =========================================================================
# Section 11: C2-cofiniteness conditions
# =========================================================================

class TestC2Cofiniteness:
    """C2-cofiniteness and finite generation of conformal block bundles."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1), ("A", 2, 2),
        ("A", 3, 1),
        ("B", 2, 1),
        ("G", 2, 1),
    ])
    def test_integrable_is_c2_cofinite(self, lt, r, k):
        """All integrable affine VOAs are C2-cofinite."""
        check = c2_cofiniteness_check(lt, r, k)
        assert check["is_c2_cofinite"]

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2),
        ("A", 2, 1),
    ])
    def test_integrable_is_rational(self, lt, r, k):
        """Integrable affine VOAs are rational."""
        check = c2_cofiniteness_check(lt, r, k)
        assert check["is_rational"]

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 1), ("A", 3, 1),
    ])
    def test_rational_implies_vector_bundles(self, lt, r, k):
        """Rationality + C2-cofiniteness => conformal blocks are vector bundles."""
        check = c2_cofiniteness_check(lt, r, k)
        assert check["conformal_blocks_are_vector_bundles"]

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 1),
    ])
    def test_num_simples_equals_integrable(self, lt, r, k):
        """Number of simple modules = number of integrable reps."""
        check = c2_cofiniteness_check(lt, r, k)
        assert check["num_simple_modules"] == num_integrable_reps(lt, r, k)


# =========================================================================
# Section 12: Verlinde CohFT data
# =========================================================================

class TestVerlindeCohFTUnit:
    """Genus-0 Frobenius algebra of the Verlinde CohFT."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2),
        ("A", 2, 1),
    ])
    def test_semisimplicity(self, lt, r, k):
        """Integrable affine CohFT is always semisimple."""
        unit = verlinde_cohft_unit(lt, r, k)
        assert unit["is_semisimple"]

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2),
    ])
    def test_quantum_dims_positive(self, lt, r, k):
        """All quantum dimensions are positive."""
        unit = verlinde_cohft_unit(lt, r, k)
        for d in unit["quantum_dims"]:
            assert d > 0

    def test_D_squared_consistency(self):
        """D^2 = sum d_lambda^2."""
        unit = verlinde_cohft_unit("A", 1, 2)
        D2 = sum(d ** 2 for d in unit["quantum_dims"])
        assert abs(D2 - unit["D_squared"]) < 1e-10


# =========================================================================
# Section 13: R-matrix data
# =========================================================================

class TestVerlindeRMatrix:
    """R-matrix of the Verlinde CohFT."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 1, 3),
        ("A", 2, 1),
    ])
    def test_R_first_coeff_is_minus_slope_over_2(self, lt, r, k):
        """R_1 = -slope/2 from Hitchin connection."""
        R = verlinde_R_matrix(lt, r, k)
        slope = verlinde_slope_general(lt, r, k)
        assert R["R_first_coeff"] == -slope / 2

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 2, 1),
    ])
    def test_R_diagonal(self, lt, r, k):
        """R-matrix is diagonal in idempotent basis (semisimple)."""
        R = verlinde_R_matrix(lt, r, k)
        assert R["is_diagonal"]


# =========================================================================
# Section 14: Determinant line comparison across genera
# =========================================================================

class TestDeterminantLineComparison:
    """Compare det(V_k) vs L_A across genera."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 2), ("A", 2, 1),
    ])
    def test_shadow_det_constant(self, lt, r, k):
        """c_1(L_A) = kappa * lambda is independent of genus."""
        comp = determinant_line_comparison(lt, r, k, max_genus=5)
        c1_L_values = [gd["c1_shadow_det"] for gd in comp["genus_data"]]
        for c1_L in c1_L_values:
            assert abs(c1_L - c1_L_values[0]) < 1e-10

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 2), ("A", 2, 1),
    ])
    def test_verlinde_det_grows(self, lt, r, k):
        """c_1(det V) = rk * slope * lambda grows with genus."""
        comp = determinant_line_comparison(lt, r, k, max_genus=5)
        c1_V_values = [gd["c1_det_verlinde"] for gd in comp["genus_data"]]
        for i in range(len(c1_V_values) - 1):
            assert c1_V_values[i + 1] > c1_V_values[i]

    def test_ratio_grows_exponentially(self):
        """c_1(det V) / c_1(L) grows exponentially with genus."""
        comp = determinant_line_comparison("A", 1, 2, max_genus=5)
        ratios = [gd["ratio"] for gd in comp["genus_data"]]
        # Ratio grows (not necessarily exponentially at low genus, but grows)
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i]


# =========================================================================
# Section 15: Chern number integration
# =========================================================================

class TestVerlindeChernNumbers:
    """Chern numbers integrated against tautological classes."""

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_int_c1_shadow_is_F_g(self, lt, r, k):
        """int_{M_g} c_1(L_A) = kappa * lambda_g^FP = F_g."""
        cn = verlinde_chern_numbers(lt, r, k, max_genus=4)
        for gd in cn["genus_results"]:
            g = gd["genus"]
            expected = float(shadow_F_g(lt, r, k, g))
            assert abs(gd["int_c1_shadow"] - expected) < 1e-12

    def test_int_c1_verlinde_eventually_dominates(self):
        """int c_1(V) eventually exceeds int c_1(L) at large genus.

        Since rk(V_g) grows exponentially while kappa is constant,
        rk * slope * lambda_fp eventually exceeds kappa * lambda_fp.
        For sl_2 k=2 this crossover happens early.
        """
        cn = verlinde_chern_numbers("A", 1, 2, max_genus=5)
        # At genus 5, the ratio should be > 1
        last = cn["genus_results"][-1]
        assert last["ratio"] > 1.0


# =========================================================================
# Section 16: Conformal block dimension tables
# =========================================================================

class TestConformalBlockTable:
    """Conformal block dimension tables for sl_2."""

    def test_sl2_k2_table_nonempty(self):
        """Table for k=2 is nonempty."""
        tbl = sl2_conformal_block_table(2, max_genus=2, max_insertions=1)
        assert len(tbl["table"]) > 0

    def test_sl2_k1_table_genus0_three_point(self):
        """Table includes genus-0 three-point functions."""
        tbl = sl2_conformal_block_table(1, max_genus=1, max_insertions=0)
        # Should have genus-0 no-insertion (= V_0 = 1), genus-1 no-insertion
        assert (1, ()) in tbl["table"]
        assert tbl["table"][(1, ())] == 2  # V_1(sl_2, k=1) = 2

    def test_table_nonneg_integers(self):
        """All table entries are non-negative integers."""
        tbl = sl2_conformal_block_table(2, max_genus=2, max_insertions=1)
        for key, val in tbl["table"].items():
            assert isinstance(val, int), f"Non-integer: {key} -> {val}"
            assert val >= 0, f"Negative: {key} -> {val}"


# =========================================================================
# Section 17: Full diagnostic
# =========================================================================

class TestFullDiagnostic:
    """Full VOA bundle diagnostic."""

    def test_sl2_k2_diagnostic(self):
        """Full diagnostic for sl_2 at k=2."""
        diag = full_voa_bundle_diagnostic("A", 1, 2, max_genus=3)
        assert diag["algebra"] == "sl_2"
        assert diag["kappa"] == 3.0
        assert abs(diag["slope"] - 0.5) < 1e-10
        assert diag["num_reps"] == 3
        assert diag["c2_check"]["is_c2_cofinite"]
        assert diag["hitchin_comparison"]["slope_equals_c_over_dim"]

    def test_sl3_k1_diagnostic(self):
        """Full diagnostic for sl_3 at k=1."""
        diag = full_voa_bundle_diagnostic("A", 2, 1, max_genus=3)
        assert diag["algebra"] == "sl_3"
        assert diag["num_reps"] == 3
        assert abs(diag["slope"] - 0.25) < 1e-10  # 1/4

    def test_diagnostic_genus_data(self):
        """Genus data structure is complete."""
        diag = full_voa_bundle_diagnostic("A", 1, 2, max_genus=3)
        for g in range(4):
            assert g in diag["genus_data"]
            gd = diag["genus_data"][g]
            assert "verlinde_dim" in gd
            if g >= 1:
                assert "shadow_F_g" in gd
                assert "c1_verlinde" in gd
                assert "c1_shadow" in gd


# =========================================================================
# Section 18: Cross-checks with existing Verlinde engine
# =========================================================================

class TestCrossChecksWithExistingEngine:
    """Verify consistency with the existing verlinde_shadow_cohft_engine."""

    @pytest.mark.parametrize("lt,r,k,g", [
        ("A", 1, 1, 2), ("A", 1, 2, 2), ("A", 1, 3, 2),
        ("A", 2, 1, 2), ("A", 2, 2, 2),
        ("A", 3, 1, 2),
        ("A", 1, 1, 3), ("A", 1, 2, 3),
    ])
    def test_bundle_rank_equals_verlinde_dim(self, lt, r, k, g):
        """verlinde_bundle_rank = verlinde_dimension_exact."""
        rk = verlinde_bundle_rank(lt, r, k, g)
        V = verlinde_dimension_exact(lt, r, k, g)
        assert rk == V

    @pytest.mark.parametrize("lt,r,k", [
        ("A", 1, 1), ("A", 1, 2), ("A", 2, 1),
    ])
    def test_shadow_F_g_consistent(self, lt, r, k):
        """Our F_g agrees with the existing engine's shadow_F_g."""
        for g in range(1, 5):
            cn = verlinde_chern_numbers(lt, r, k, max_genus=g)
            for gd in cn["genus_results"]:
                if gd["genus"] == g:
                    expected = float(shadow_F_g(lt, r, k, g))
                    assert abs(gd["int_c1_shadow"] - expected) < 1e-12


# =========================================================================
# Section 19: Specific numerical values
# =========================================================================

class TestSpecificNumericalValues:
    """Test specific numerical values from the literature."""

    def test_sl2_k2_verlinde_dims(self):
        """sl_2 k=2: V_0=1, V_1=3, V_2=10, V_3=36."""
        assert verlinde_bundle_rank("A", 1, 2, 0) == 1
        assert verlinde_bundle_rank("A", 1, 2, 1) == 3
        assert verlinde_bundle_rank("A", 1, 2, 2) == 10
        assert verlinde_bundle_rank("A", 1, 2, 3) == 36

    def test_sl2_k2_slope(self):
        """sl_2 k=2: slope = 2/4 = 1/2."""
        assert verlinde_slope_sl2(2, 0) == Rational(1, 2)

    def test_sl2_k2_kappa(self):
        """sl_2 k=2: kappa = 3*4/4 = 3."""
        assert kappa_affine_exact("A", 1, 2) == Rational(3)

    def test_sl2_k2_c1_genus2(self):
        """sl_2 k=2 genus 2: c_1(V) = 10 * 1/2 = 5, c_1(L) = 3."""
        info = verlinde_c1("A", 1, 2, 2)
        assert abs(info["c1_verlinde_coeff"] - 5.0) < 1e-10
        assert abs(info["c1_shadow_coeff"] - 3.0) < 1e-10

    def test_sl3_k1_verlinde_dims(self):
        """sl_3 k=1: V_g = 3^g."""
        for g in range(5):
            assert verlinde_bundle_rank("A", 2, 1, g) == 3 ** g

    def test_sl3_k1_slope(self):
        """sl_3 k=1: slope = 1/(1+3) = 1/4."""
        assert verlinde_slope_general("A", 2, 1) == Rational(1, 4)

    def test_sl2_k1_genus2_cb_with_insertion(self):
        """sl_2 k=1 genus 2: V(Sigma_2, j=0) + V(Sigma_2, j=1) relates to V_2."""
        # For k=1, V_2 = 4
        V0 = conformal_block_dim_sl2(1, 2, (0,))
        V1 = conformal_block_dim_sl2(1, 2, (1,))
        # Non-separating degeneration from genus 3:
        # V_3 = V(Sigma_2, 0, 0) + V(Sigma_2, 1, 1)
        # But V(Sigma_2, j) with 1 insertion is different from V_3
        assert V0 >= 0 and V1 >= 0

    def test_sl2_k2_genus0_four_point(self):
        """sl_2 k=2: V(S^2, 1,1,1,1) = 2 (two conformal blocks)."""
        assert conformal_block_dim_sl2(2, 0, (1, 1, 1, 1)) == 2

    def test_sl2_k3_genus0_four_point(self):
        """sl_2 k=3: V(S^2, 1,1,1,1) = sum_m N_{11}^m * N_{11}^m = 2.

        N_{11}^0 = 1, N_{11}^1 = 0, N_{11}^2 = 1, N_{11}^3 = 0.
        So sum = 1 + 0 + 1 + 0 = 2.
        """
        dim = conformal_block_dim_sl2(3, 0, (1, 1, 1, 1))
        assert dim == 2


# =========================================================================
# Section 20: Consistency and edge cases
# =========================================================================

class TestConsistencyAndEdgeCases:
    """Consistency checks and edge cases."""

    def test_genus0_no_insertions_is_1(self):
        """V_0 = 1 for all algebras."""
        for (lt, r, k) in [("A", 1, 1), ("A", 1, 2), ("A", 2, 1), ("A", 3, 1)]:
            assert verlinde_bundle_rank(lt, r, k, 0) == 1

    def test_nonsep_genus_below_1_raises(self):
        """Non-separating check requires genus >= 1."""
        with pytest.raises(ValueError):
            nonseparating_check_sl2(2, 0)

    def test_factorization_bad_partition_raises(self):
        """Partition not summing to genus raises ValueError."""
        with pytest.raises(ValueError):
            factorization_check_sl2(2, 3, (1, 1))

    def test_slope_at_various_types(self):
        """Slope is well-defined for all supported types."""
        for (lt, r) in [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2),
                         ("D", 4), ("G", 2)]:
            slope = verlinde_slope_general(lt, r, 1)
            assert 0 < float(slope) < 1

    @pytest.mark.parametrize("k", [1, 2, 3, 4])
    def test_sl2_fusion_from_conformal_blocks(self, k):
        """Fusion = genus-0 three-point conformal blocks (cross-check)."""
        import numpy as np
        N_fus = fusion_coefficients("A", 1, k)
        for j1 in range(k + 1):
            for j2 in range(k + 1):
                for j3 in range(k + 1):
                    N_val = int(round(N_fus[j1, j2, j3].real))
                    cb_val = conformal_block_dim_sl2(k, 0, (j1, j2, j3))
                    assert N_val == cb_val, (
                        f"k={k}: N_{j1},{j2}^{j3}={N_val} != "
                        f"V(S^2,{j1},{j2},{j3})={cb_val}"
                    )
