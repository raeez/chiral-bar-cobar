"""Tests for the genus-1 spectral sequence of the bar complex.

Investigates whether the spectral sequence E_r^{p,q} of the bar complex
B^(1)(A) at genus 1 carries algebra-dependent information beyond the
scalar modular characteristic kappa(A).

The answer, confirmed by these tests: NO. The genus-1 spectral sequence
depends on the algebra parameters (e.g. central charge c) only through
kappa(A). The E_2 page at genus 1 has the same dimensions as at genus 0.

Three independent verification axes:
  I.   Structure: E_1 page dimensions at genus 1 equal genus-0 bar complex dims
  II.  c-independence: d_1 differential is proportional to kappa (scalar)
  III. Cross-channel: for W_3, the curvature ratio m_0^W/m_0^T = 2/3 is universal

Ground truth:
  spectral_sequence.py (genus-0 E_2 pages, VIRASORO_BAR_COH),
  mc5_genus1_bridge.py (curvature formula d^2 = kappa * omega_1),
  genus_expansion.py (kappa values for all families),
  virasoro_bar.py (OPE data),
  w3_bar.py (W_3 curvature components).
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.genus1_spectral_sequence import (
    virasoro_vacuum_basis,
    virasoro_vacuum_dims,
    virasoro_bar_dims_genus0,
    w3_vacuum_dims,
    w3_bar_dims_genus0,
    genus1_e1_correction_dims,
    virasoro_genus1_e2_dims,
    w3_genus1_e2_analysis,
    compare_e2_pages,
    genus1_spectral_sequence_analysis,
    virasoro_multi_c_comparison,
    w3_multi_c_comparison,
    test_virasoro_d1_scalar_at_bar2,
    test_w3_cross_channel_ratio,
    w3_genus0_e2_known_dims,
    Genus1SpectralSequence,
)
from compute.lib.genus_expansion import kappa_virasoro, kappa_w3
from compute.lib.spectral_sequence import VIRASORO_BAR_COH
from compute.lib.utils import lambda_fp, partition_number


# =========================================================================
# I. Vacuum module dimensions
# =========================================================================

class TestVirasoroVacuumBasis:
    """Virasoro vacuum module: dim V-bar_h = p_{>=2}(h)."""

    def test_weight0(self):
        """Weight 0: vacuum state only."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[0]) == 1

    def test_weight1_empty(self):
        """Weight 1: empty (L_{-1}|0> = 0)."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[1]) == 0

    def test_weight2(self):
        """Weight 2: T = L_{-2}|0>, one state."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[2]) == 1
        assert basis[2] == [(2,)]

    def test_weight3(self):
        """Weight 3: L_{-3}|0>, one state."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[3]) == 1
        assert basis[3] == [(3,)]

    def test_weight4(self):
        """Weight 4: L_{-4}|0>, L_{-2}^2|0>, two states."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[4]) == 2

    def test_weight6(self):
        """Weight 6: partitions of 6 into parts >= 2: (6), (4,2), (3,3), (2,2,2)."""
        basis = virasoro_vacuum_basis(6)
        assert len(basis[6]) == 4

    def test_dims_match_partition_formula(self):
        """dim V-bar_h = p_{>=2}(h) for h = 0, ..., 10."""
        dims = virasoro_vacuum_dims(10)
        # p_{>=2}(h) equals the number of partitions of h into parts >= 2
        # Known values: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12
        expected = {0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 7, 9: 8, 10: 12}
        for h, exp in expected.items():
            assert dims[h] == exp, f"dim V-bar_{h} = {dims[h]}, expected {exp}"


class TestW3VacuumDims:
    """W_3 vacuum module dimensions."""

    def test_weight0(self):
        dims = w3_vacuum_dims(6)
        assert dims[0] == 1

    def test_weight1_empty(self):
        dims = w3_vacuum_dims(6)
        assert dims[1] == 0

    def test_weight2(self):
        """Weight 2: T only."""
        dims = w3_vacuum_dims(6)
        assert dims[2] == 1

    def test_weight3(self):
        """Weight 3: dT (from T-tower) and W (from W-tower)."""
        dims = w3_vacuum_dims(6)
        assert dims[3] == 2

    def test_weight4(self):
        """Weight 4: TT, L_{-4}|0> (T-tower) + nothing new from W-tower at weight 4."""
        # T-tower: partitions of 4 into parts >= 2 = {(4), (2,2)} -> 2 states
        # W-tower: partitions of 4 into parts >= 3 = {(4)} -> 1 state
        # But we need to convolve: total = sum_{a+b=4} t_dims[a] * w_dims[b]
        # a=0,b=4: 1*1=1; a=1,b=3: 0; a=2,b=2: 1*0=0; a=3,b=1: 1*0=0; a=4,b=0: 2*1=2
        # Total = 1 + 2 = 3
        dims = w3_vacuum_dims(6)
        assert dims[4] == 3

    def test_w3_larger_than_virasoro(self):
        """W_3 has more states than Virasoro at each weight >= 3."""
        vir_dims = virasoro_vacuum_dims(10)
        w3_dims_val = w3_vacuum_dims(10)
        for h in range(3, 11):
            assert w3_dims_val[h] >= vir_dims[h], \
                f"W_3 dim at weight {h}: {w3_dims_val[h]} < Vir dim {vir_dims[h]}"


# =========================================================================
# II. Bar complex dimensions at genus 0
# =========================================================================

class TestVirasoroBarDimsGenus0:
    """Virasoro bar complex dimensions at genus 0."""

    def test_bar1_weight2(self):
        """Bar degree 1, weight 2: one state (T)."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 2)] == 1

    def test_bar1_weight3(self):
        """Bar degree 1, weight 3: one state (dT)."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 3)] == 1

    def test_bar1_weight4(self):
        """Bar degree 1, weight 4: two states."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 4)] == 2

    def test_bar2_weight4(self):
        """Bar degree 2, weight 4: T tensor T, Arnold factor = 1! = 1.
        dim = dim(V_2) * dim(V_2) * 1 = 1."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(2, 4)] == 1

    def test_bar2_weight5(self):
        """Bar degree 2, weight 5: compositions 2+3 and 3+2.
        dim(V_2)*dim(V_3) + dim(V_3)*dim(V_2) = 1*1 + 1*1 = 2, times 1! = 2."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(2, 5)] == 2

    def test_bar2_weight6(self):
        """Bar degree 2, weight 6: compositions 2+4, 3+3, 4+2.
        1*2 + 1*1 + 2*1 = 5, times 1! = 5."""
        dims = virasoro_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(2, 6)] == 5


class TestW3BarDimsGenus0:
    """W_3 bar complex dimensions at genus 0."""

    def test_bar1_weight2(self):
        """Bar degree 1, weight 2: T only."""
        dims = w3_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 2)] == 1

    def test_bar1_weight3(self):
        """Bar degree 1, weight 3: dT and W."""
        dims = w3_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 3)] == 2

    def test_bar1_weight4(self):
        """Bar degree 1, weight 4: three W_3 states."""
        dims = w3_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(1, 4)] == 3

    def test_bar2_weight4(self):
        """Bar degree 2, weight 4: only (T, T) pair, dim = 1."""
        dims = w3_bar_dims_genus0(max_degree=2, max_weight=8)
        assert dims[(2, 4)] == 1

    def test_w3_bar_larger_than_virasoro(self):
        """W_3 bar complex is at least as large as Virasoro at each bidegree."""
        vir_dims = virasoro_bar_dims_genus0(max_degree=3, max_weight=10)
        w3_dims_val = w3_bar_dims_genus0(max_degree=3, max_weight=10)
        for key in vir_dims:
            w3_val = w3_dims_val.get(key, 0)
            assert w3_val >= vir_dims[key], \
                f"W_3 bar dim at {key}: {w3_val} < Vir dim {vir_dims[key]}"


# =========================================================================
# III. E_1 page at genus 1 equals genus-0 bar complex
# =========================================================================

class TestGenus1E1Page:
    """The E_1 page at genus 1 has the same dimensions as the genus-0 bar complex."""

    def test_virasoro_e1_equals_genus0(self):
        """Virasoro: E_1 at genus 1 = bar complex dims at genus 0."""
        genus0 = virasoro_bar_dims_genus0(max_degree=3, max_weight=8)
        genus1_e1 = genus1_e1_correction_dims("Virasoro", max_bar_degree=3, max_weight=8)
        assert genus0 == genus1_e1

    def test_w3_e1_equals_genus0(self):
        """W_3: E_1 at genus 1 = bar complex dims at genus 0."""
        genus0 = w3_bar_dims_genus0(max_degree=3, max_weight=8)
        genus1_e1 = genus1_e1_correction_dims("W3", max_bar_degree=3, max_weight=8)
        assert genus0 == genus1_e1


# =========================================================================
# IV. Virasoro E_2 at genus 1: c-independence
# =========================================================================

class TestVirasoroGenus1E2:
    """E_2 page at genus 1 for Virasoro: c-independent, equals genus-0 bar coh."""

    def test_e2_at_c1(self):
        """E_2 dims at c=1 match genus-0 values."""
        e2 = virasoro_genus1_e2_dims(Rational(1), max_degree=4)
        for d in range(1, 5):
            if d in VIRASORO_BAR_COH:
                assert e2[d] == VIRASORO_BAR_COH[d]

    def test_e2_at_c25(self):
        """E_2 dims at c=25 match genus-0 values."""
        e2 = virasoro_genus1_e2_dims(Rational(25), max_degree=4)
        for d in range(1, 5):
            if d in VIRASORO_BAR_COH:
                assert e2[d] == VIRASORO_BAR_COH[d]

    def test_e2_at_c26(self):
        """E_2 dims at c=26 match genus-0 values.
        c=26 is where kappa(Vir!) = 0, but Vir itself still has kappa = 13."""
        e2 = virasoro_genus1_e2_dims(Rational(26), max_degree=4)
        for d in range(1, 5):
            if d in VIRASORO_BAR_COH:
                assert e2[d] == VIRASORO_BAR_COH[d]

    def test_e2_c_independent(self):
        """E_2 dims are the same at c=1, c=25, c=26."""
        e2_1 = virasoro_genus1_e2_dims(Rational(1), max_degree=4)
        e2_25 = virasoro_genus1_e2_dims(Rational(25), max_degree=4)
        e2_26 = virasoro_genus1_e2_dims(Rational(26), max_degree=4)
        for d in e2_1:
            assert e2_1[d] == e2_25[d] == e2_26[d]

    def test_self_dual_point_c13(self):
        """At the self-dual point c=13, kappa = kappa_dual = 13/2."""
        e2 = virasoro_genus1_e2_dims(Rational(13), max_degree=4)
        for d in range(1, 5):
            if d in VIRASORO_BAR_COH:
                assert e2[d] == VIRASORO_BAR_COH[d]


class TestVirasoroMultiCComparison:
    """Multi-c comparison: the decisive test for c-independence."""

    def test_all_c_give_same_e2(self):
        result = virasoro_multi_c_comparison(
            c_vals=[Rational(1), Rational(13), Rational(25), Rational(26)]
        )
        assert result["all_c_give_same_e2"]

    def test_each_c_matches_genus0(self):
        result = virasoro_multi_c_comparison()
        for key, val in result.items():
            if isinstance(val, dict) and "matches_genus0" in val:
                assert val["matches_genus0"], f"{key} does not match genus 0"


# =========================================================================
# V. W_3 analysis at genus 1
# =========================================================================

class TestW3Genus1Analysis:
    """W_3 genus-1 spectral sequence analysis."""

    def test_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        c = Symbol('c')
        assert kappa_w3() == 5 * c / 6

    def test_curvature_ratio_is_2_over_3(self):
        """m_0^W / m_0^T = (c/3) / (c/2) = 2/3, c-independent."""
        result = w3_genus1_e2_analysis(Rational(50))
        assert result["curvature_ratio"] == Rational(2, 3)
        assert result["curvature_ratio_c_independent"]

    def test_d1_proportional_to_kappa(self):
        """d_1 is proportional to kappa = 5c/6 for W_3."""
        result = w3_genus1_e2_analysis(Rational(50))
        assert result["d1_proportional_to_kappa"]

    def test_e2_c_independent(self):
        """E_2 at genus 1 is c-independent for W_3."""
        result = w3_genus1_e2_analysis(Rational(50))
        assert result["e2_c_independent"]

    def test_w3_known_e2_dims(self):
        """W_3 bar cohomology: H^1 = 2, H^2 = 5."""
        known = w3_genus0_e2_known_dims(2)
        assert known[1] == 2
        assert known[2] == 5


class TestW3CrossChannelRatio:
    """W_3 cross-channel curvature ratio test."""

    def test_ratio_at_c1(self):
        result = test_w3_cross_channel_ratio([Rational(1)])
        assert result["ratio at c=1"]["is_2_over_3"]

    def test_ratio_at_c50(self):
        result = test_w3_cross_channel_ratio([Rational(50)])
        assert result["ratio at c=50"]["is_2_over_3"]

    def test_ratio_at_c100(self):
        result = test_w3_cross_channel_ratio([Rational(100)])
        assert result["ratio at c=100"]["is_2_over_3"]

    def test_ratio_universal(self):
        result = test_w3_cross_channel_ratio()
        assert result["ratio_c_independent"]


class TestW3MultiCComparison:
    """W_3 multi-c comparison."""

    def test_all_c_give_same_e2(self):
        result = w3_multi_c_comparison(
            c_vals=[Rational(1), Rational(50), Rational(100)]
        )
        assert result["all_c_give_same_e2"]

    def test_curvature_ratio_universal(self):
        result = w3_multi_c_comparison()
        assert result["curvature_ratio_universal"]


# =========================================================================
# VI. d_1 scalar test (Virasoro)
# =========================================================================

class TestVirasoroD1Scalar:
    """Verify that d_1 at bar degree 2 is kappa times a universal operator."""

    def test_d1_is_scalar_times_kappa(self):
        result = test_virasoro_d1_scalar_at_bar2()
        assert result["d1_is_kappa_times_universal"]

    def test_ratios_match(self):
        """d_1(c1) / d_1(c2) = kappa(c1) / kappa(c2) = c1 / c2."""
        result = test_virasoro_d1_scalar_at_bar2(
            c_vals=[Rational(1), Rational(25), Rational(26)]
        )
        for key, val in result.items():
            if isinstance(val, dict) and "match" in val:
                assert val["match"], f"Ratio mismatch: {key}"


# =========================================================================
# VII. Complete spectral sequence analysis
# =========================================================================

class TestCompleteAnalysis:
    """Full genus-1 spectral sequence analysis."""

    def test_virasoro_c1_complete(self):
        result = genus1_spectral_sequence_analysis("Virasoro", Rational(1))
        assert result["kappa"] == Rational(1, 2)
        assert result["complementarity_holds"]
        assert result["d1_proportional_to_kappa"]
        assert result["e2_genus0_equals_genus1"]
        assert not result["extra_c_dependence_at_genus1"]

    def test_virasoro_c25_complete(self):
        result = genus1_spectral_sequence_analysis("Virasoro", Rational(25))
        assert result["kappa"] == Rational(25, 2)
        assert result["complementarity_holds"]
        assert result["e2_genus0_equals_genus1"]

    def test_virasoro_c26_complete(self):
        """c=26: kappa = 13, kappa_dual = 0 (dual is uncurved)."""
        result = genus1_spectral_sequence_analysis("Virasoro", Rational(26))
        assert result["kappa"] == Rational(13)
        assert result["kappa_dual"] == 0
        assert result["complementarity_holds"]
        assert result["e2_genus0_equals_genus1"]

    def test_virasoro_c13_selfdual(self):
        """c=13: self-dual point, kappa = kappa_dual = 13/2."""
        result = genus1_spectral_sequence_analysis("Virasoro", Rational(13))
        assert result["kappa"] == Rational(13, 2)
        assert result["kappa"] == result["kappa_dual"]
        assert result["complementarity_holds"]

    def test_w3_c50_complete(self):
        result = genus1_spectral_sequence_analysis("W3", Rational(50))
        assert result["kappa"] == 5 * Rational(50) / 6
        assert result["complementarity_holds"]
        assert result["d1_proportional_to_kappa"]
        assert result["e2_genus0_equals_genus1"]

    def test_w3_c100_complete(self):
        """c=100: the DS dual central charge for W_3.
        kappa = 5*100/6 = 500/6 = 250/3."""
        result = genus1_spectral_sequence_analysis("W3", Rational(100))
        assert result["kappa"] == Rational(250, 3)
        assert result["complementarity_holds"]
        assert result["e2_genus0_equals_genus1"]


# =========================================================================
# VIII. Complementarity at genus 1
# =========================================================================

class TestComplementarityGenus1:
    """kappa(A) + kappa(A!) = const at genus 1."""

    def test_virasoro_sum_is_13(self):
        """Virasoro: kappa + kappa_dual = c/2 + (26-c)/2 = 13."""
        for c_val in [Rational(1), Rational(13), Rational(25), Rational(26)]:
            result = genus1_spectral_sequence_analysis("Virasoro", c_val)
            assert simplify(result["complementarity_sum"] - Rational(13)) == 0

    def test_w3_sum_is_250_over_3(self):
        """W_3: kappa + kappa_dual = 5c/6 + 5(100-c)/6 = 250/3."""
        for c_val in [Rational(1), Rational(50), Rational(100)]:
            result = genus1_spectral_sequence_analysis("W3", c_val)
            assert simplify(result["complementarity_sum"] - Rational(250, 3)) == 0


# =========================================================================
# IX. Quantum correction t_1 = kappa / 24
# =========================================================================

class TestQuantumCorrectionT1:
    """The genus-1 quantum correction t_1 = kappa * lambda_1^FP = kappa / 24."""

    def test_lambda1_fp(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_virasoro_t1(self):
        """t_1(Vir_c) = (c/2) / 24 = c/48."""
        for c_val in [Rational(1), Rational(26)]:
            result = genus1_spectral_sequence_analysis("Virasoro", c_val)
            expected = c_val / 48
            assert simplify(result["t1_correction"] - expected) == 0

    def test_w3_t1(self):
        """t_1(W_3_c) = (5c/6) / 24 = 5c/144."""
        for c_val in [Rational(1), Rational(100)]:
            result = genus1_spectral_sequence_analysis("W3", c_val)
            expected = 5 * c_val / 144
            assert simplify(result["t1_correction"] - expected) == 0


# =========================================================================
# X. Curvature channels for W_3
# =========================================================================

class TestW3CurvatureChannels:
    """W_3 has two curvature channels: T and W."""

    def test_T_channel_curvature(self):
        """m_0^(T) = c/2 (quartic pole of T x T)."""
        result = genus1_spectral_sequence_analysis("W3", Rational(50))
        assert result["curvature_channels"]["T"] == Rational(25)

    def test_W_channel_curvature(self):
        """m_0^(W) = c/3 (sixth-order pole of W x W)."""
        result = genus1_spectral_sequence_analysis("W3", Rational(50))
        assert result["curvature_channels"]["W"] == Rational(50, 3)

    def test_curvature_ratio(self):
        """m_0^(W) / m_0^(T) = 2/3."""
        for c_val in [Rational(1), Rational(50), Rational(100)]:
            result = genus1_spectral_sequence_analysis("W3", c_val)
            ratio = result["curvature_channels"]["W"] / result["curvature_channels"]["T"]
            assert simplify(ratio - Rational(2, 3)) == 0


# =========================================================================
# XI. Genus1SpectralSequence class
# =========================================================================

class TestGenus1SpectralSequenceClass:
    """Basic tests for the Genus1SpectralSequence class."""

    def test_virasoro_init(self):
        ss = Genus1SpectralSequence("Virasoro")
        c = Symbol('c')
        assert ss.algebra == "Virasoro"
        assert simplify(ss.kappa - c / 2) == 0
        assert simplify(ss.t1 - c / 48) == 0
        assert len(ss.generators) == 1
        assert ss.generators[0] == ("T", 2)

    def test_w3_init(self):
        ss = Genus1SpectralSequence("W3")
        c = Symbol('c')
        assert ss.algebra == "W3"
        assert simplify(ss.kappa - 5 * c / 6) == 0
        assert len(ss.generators) == 2
        assert ss.generators[0] == ("T", 2)
        assert ss.generators[1] == ("W", 3)

    def test_virasoro_with_specific_c(self):
        c = Rational(26)
        ss = Genus1SpectralSequence("Virasoro", param=c)
        assert ss.kappa == 13
        assert ss.t1 == Rational(13, 24)

    def test_w3_with_specific_c(self):
        c = Rational(100)
        ss = Genus1SpectralSequence("W3", param=c)
        assert ss.kappa == Rational(250, 3)

    def test_unknown_algebra_raises(self):
        with pytest.raises(ValueError):
            Genus1SpectralSequence("Unknown")


# =========================================================================
# XII. Numerical spot checks
# =========================================================================

class TestNumericalSpotChecks:
    """Exact rational arithmetic checks at specific values."""

    def test_virasoro_kappa_c1(self):
        assert kappa_virasoro(1) == Rational(1, 2)

    def test_virasoro_kappa_c26(self):
        assert kappa_virasoro(26) == Rational(13)

    def test_virasoro_kappa_c13(self):
        assert kappa_virasoro(13) == Rational(13, 2)

    def test_w3_kappa_c1(self):
        assert kappa_w3(1) == Rational(5, 6)

    def test_w3_kappa_c100(self):
        assert kappa_w3(100) == Rational(250, 3)

    def test_virasoro_complementarity_c1(self):
        """kappa(Vir_1) + kappa(Vir_25) = 1/2 + 25/2 = 13."""
        assert kappa_virasoro(1) + kappa_virasoro(25) == 13

    def test_virasoro_complementarity_c13(self):
        """kappa(Vir_13) + kappa(Vir_13) = 13/2 + 13/2 = 13."""
        assert kappa_virasoro(13) + kappa_virasoro(13) == 13

    def test_w3_complementarity(self):
        """kappa(W_3_c) + kappa(W_3_{100-c}) = 250/3."""
        for c_val in [1, 50, 100]:
            assert kappa_w3(c_val) + kappa_w3(100 - c_val) == Rational(250, 3)


# =========================================================================
# XIII. Vacuum module generating function cross-checks
# =========================================================================

class TestVacuumModuleGF:
    """Cross-check vacuum module dims against partition-theoretic formulas."""

    def test_virasoro_gf_sum(self):
        """Total dim of Virasoro vacuum module up to weight 8.
        Sum should match the coefficient sum of prod_{n>=2} 1/(1-q^n)."""
        dims = virasoro_vacuum_dims(8)
        # prod_{n>=2} 1/(1-q^n) first coefficients (weight 0 through 8):
        # 1, 0, 1, 1, 2, 2, 4, 4, 7
        expected_total = 1 + 0 + 1 + 1 + 2 + 2 + 4 + 4 + 7
        actual_total = sum(dims[h] for h in range(9))
        assert actual_total == expected_total

    def test_w3_exceeds_virasoro_total(self):
        """W_3 vacuum module is strictly larger than Virasoro from weight 3 onward."""
        vir = virasoro_vacuum_dims(8)
        w3 = w3_vacuum_dims(8)
        for h in range(3, 9):
            assert w3[h] > vir[h]


# =========================================================================
# XIV. Edge cases and structural tests
# =========================================================================

class TestEdgeCases:
    """Edge cases and structural sanity checks."""

    def test_compare_e2_virasoro(self):
        result = compare_e2_pages("Virasoro", Rational(1))
        assert result["dims_match"]
        assert not result["c_dependence_at_genus1"]

    def test_compare_e2_w3(self):
        result = compare_e2_pages("W3", Rational(50))
        assert result["dims_match"]
        assert not result["c_dependence_at_genus1"]

    def test_unknown_algebra_in_compare(self):
        with pytest.raises(ValueError):
            compare_e2_pages("Unknown", Rational(1))

    def test_unknown_algebra_in_analysis(self):
        with pytest.raises(ValueError):
            genus1_spectral_sequence_analysis("Unknown", Rational(1))

    def test_e1_unknown_algebra_raises(self):
        with pytest.raises(ValueError):
            genus1_e1_correction_dims("Unknown")
