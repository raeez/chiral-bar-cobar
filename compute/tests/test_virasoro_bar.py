"""Tests for Virasoro bar complex chain-level computations.

Ground truth from manuscript (detailed_computations.tex):
  OPE: T_{(3)}T=c/2, T_{(1)}T=2T, T_{(0)}T=dT     [comp:virasoro-ope]
  Bar diff: D(TT)=(c/2)|0>+2T+dT                    [comp:virasoro-bar-diff]
  Curvature: m_0=c/2, complementarity c+c'=26        [comp:virasoro-curvature]
  Vacuum: dim=p_{>=2}(h)                             [comp:virasoro-vacuum]
  Arnold: vacuum cancels at deg>=3                    [prop:arnold-virasoro-deg3]
  Dim table: through degree 5                         [comp:virasoro-dim-table]
  Mixed: D(T,dT)=3dT+d^2T, D(dT,T)=3dT+2d^2T       [comp:virasoro-bar-diff]
  DS formula: c=1-6(k+1)^2/(k+2)                     [CLAUDE.md]
"""

import pytest
from sympy import Rational, Symbol, simplify, oo, limit

from compute.lib.virasoro_bar import (
    virasoro_nth_products,
    virasoro_nth_product,
    virasoro_descendant_products,
    virasoro_bar_diff_deg2,
    virasoro_bar_diff_deg2_mixed,
    virasoro_curvature,
    virasoro_complementarity_sum,
    virasoro_ds_central_charge,
    partitions_geq2,
    vacuum_module_dims,
    os_top_dim,
    os_poincare,
    bar_chain_dim,
    bar_dim_table,
    arnold_cancellation_deg3,
    arnold_cancellation_deg4,
    arnold_cancellation_deg5,
    verify_virasoro_bar_diff,
    verify_virasoro_curvature,
    verify_vacuum_dims,
    verify_bar_dims,
    verify_arnold_cancellation,
    verify_mixed_weight_bar,
)

c = Symbol('c')
k = Symbol('k')


# ---------------------------------------------------------------------------
# OPE n-th products
# ---------------------------------------------------------------------------

class TestNthProducts:
    """OPE n-th products T_{(n)}T."""

    def test_quartic_pole(self):
        """T_{(3)}T = c/2 (curvature)."""
        assert virasoro_nth_product(3)["vac"] == c / 2

    def test_cubic_absent(self):
        """T_{(2)}T = 0."""
        assert len(virasoro_nth_product(2)) == 0

    def test_double_pole(self):
        """T_{(1)}T = 2T (conformal weight)."""
        assert virasoro_nth_product(1)["T"] == Rational(2)

    def test_simple_pole(self):
        """T_{(0)}T = dT (translation)."""
        assert virasoro_nth_product(0)["dT"] == Rational(1)

    def test_no_higher_poles(self):
        """T_{(n)}T = 0 for n >= 4."""
        for n in [4, 5, 6]:
            assert len(virasoro_nth_product(n)) == 0


# ---------------------------------------------------------------------------
# Descendant products
# ---------------------------------------------------------------------------

class TestDescendantProducts:
    """OPE products for T and dT."""

    def test_T_dT_no_quartic(self):
        """T_{(3)}(dT) = 0."""
        desc = virasoro_descendant_products()
        assert 3 not in desc[("T", "dT")]

    def test_T_dT_double(self):
        """T_{(1)}(dT) = 3dT."""
        desc = virasoro_descendant_products()
        assert desc[("T", "dT")][1]["dT"] == Rational(3)

    def test_T_dT_simple(self):
        """T_{(0)}(dT) = d^2T."""
        desc = virasoro_descendant_products()
        assert desc[("T", "dT")][0]["d2T"] == Rational(1)

    def test_dT_T_simple(self):
        """(dT)_{(0)}T = 2d^2T (asymmetric via skew-symmetry)."""
        desc = virasoro_descendant_products()
        assert desc[("dT", "T")][0]["d2T"] == Rational(2)

    def test_dT_T_double(self):
        """(dT)_{(1)}T = 3dT."""
        desc = virasoro_descendant_products()
        assert desc[("dT", "T")][1]["dT"] == Rational(3)

    def test_asymmetry(self):
        """(dT)_{(0)}T != T_{(0)}(dT): 2d^2T vs d^2T."""
        desc = virasoro_descendant_products()
        assert desc[("dT", "T")][0]["d2T"] != desc[("T", "dT")][0]["d2T"]


# ---------------------------------------------------------------------------
# Bar differential degree 2
# ---------------------------------------------------------------------------

class TestBarDifferential:
    """Bar differential D: B-bar^2 -> B-bar^0 + B-bar^1."""

    def test_vacuum(self):
        """D(T otimes T otimes eta) has vacuum c/2."""
        vac, _ = virasoro_bar_diff_deg2()
        assert vac["vac"] == c / 2

    def test_2T(self):
        """D(T otimes T otimes eta) has 2T."""
        _, bar1 = virasoro_bar_diff_deg2()
        assert bar1["T"] == Rational(2)

    def test_dT(self):
        """D(T otimes T otimes eta) has dT."""
        _, bar1 = virasoro_bar_diff_deg2()
        assert bar1["dT"] == Rational(1)

    def test_mixed_TdT_no_vacuum(self):
        """D(T otimes dT otimes eta) has no vacuum."""
        vac, _ = virasoro_bar_diff_deg2_mixed("T", "dT")
        assert len(vac) == 0

    def test_mixed_TdT(self):
        """D(T otimes dT otimes eta) = 3dT + d^2T."""
        _, bar1 = virasoro_bar_diff_deg2_mixed("T", "dT")
        assert bar1["dT"] == Rational(3)
        assert bar1["d2T"] == Rational(1)

    def test_mixed_dTT_no_vacuum(self):
        """D(dT otimes T otimes eta) has no vacuum."""
        vac, _ = virasoro_bar_diff_deg2_mixed("dT", "T")
        assert len(vac) == 0

    def test_mixed_dTT(self):
        """D(dT otimes T otimes eta) = 3dT + 2d^2T."""
        _, bar1 = virasoro_bar_diff_deg2_mixed("dT", "T")
        assert bar1["dT"] == Rational(3)
        assert bar1["d2T"] == Rational(2)

    def test_mixed_asymmetry(self):
        """D(T,dT) and D(dT,T) differ in d^2T coefficient."""
        _, tw = virasoro_bar_diff_deg2_mixed("T", "dT")
        _, wt = virasoro_bar_diff_deg2_mixed("dT", "T")
        assert tw["d2T"] == Rational(1)
        assert wt["d2T"] == Rational(2)


# ---------------------------------------------------------------------------
# Curvature
# ---------------------------------------------------------------------------

class TestCurvature:
    """Curvature m_0 = c/2."""

    def test_curvature_value(self):
        assert virasoro_curvature() == c / 2

    def test_complementarity(self):
        """c + c' = 26."""
        assert virasoro_complementarity_sum() == 26

    def test_curvature_complementarity(self):
        """m0(c) + m0(26-c) = 13."""
        m0 = virasoro_curvature()
        m0_dual = m0.subs(c, 26 - c)
        assert simplify(m0 + m0_dual - 13) == 0

    def test_vanishes_at_c0(self):
        """m_0 = 0 iff c = 0."""
        assert virasoro_curvature().subs(c, 0) == 0

    def test_curvature_matches_quartic(self):
        """m_0 = T_{(3)}T."""
        assert virasoro_nth_product(3)["vac"] == virasoro_curvature()

    def test_ds_formula(self):
        """c = 1 - 6(k+1)^2/(k+2)."""
        c_val = virasoro_ds_central_charge(k)
        # At k = 0: c = 1 - 6/2 = -2
        assert c_val.subs(k, 0) == -2

    def test_ds_complementarity(self):
        """c(k) + c(-k-4) = 26."""
        c_k = virasoro_ds_central_charge(k)
        c_dual = virasoro_ds_central_charge(-k - 4)
        assert simplify(c_k + c_dual - 26) == 0

    def test_ds_critical_level(self):
        """At k = -2 (critical level), c diverges."""
        c_val = virasoro_ds_central_charge(k)
        assert abs(limit(c_val, k, -2)) == oo


# ---------------------------------------------------------------------------
# Vacuum module
# ---------------------------------------------------------------------------

class TestVacuumModule:
    """Vacuum module dimensions p_{>=2}(h)."""

    @pytest.mark.parametrize("h,expected", [
        (2, 1), (3, 1), (4, 2), (5, 2), (6, 4), (7, 4),
        (8, 7), (9, 8), (10, 12), (11, 14), (12, 21),
    ])
    def test_dims(self, h, expected):
        assert partitions_geq2(h) == expected

    def test_h0(self):
        assert partitions_geq2(0) == 1

    def test_h1(self):
        assert partitions_geq2(1) == 0


# ---------------------------------------------------------------------------
# OS algebra
# ---------------------------------------------------------------------------

class TestOSAlgebra:
    """Orlik-Solomon algebra dimensions."""

    @pytest.mark.parametrize("n,expected", [(2, 1), (3, 2), (4, 6), (5, 24)])
    def test_top_dim(self, n, expected):
        assert os_top_dim(n) == expected

    def test_poincare_2(self):
        assert os_poincare(2) == [1, 1]

    def test_poincare_3(self):
        assert os_poincare(3) == [1, 3, 2]

    def test_poincare_4(self):
        assert os_poincare(4) == [1, 6, 11, 6]

    def test_poincare_5(self):
        assert os_poincare(5) == [1, 10, 35, 50, 24]


# ---------------------------------------------------------------------------
# Bar complex dimensions
# ---------------------------------------------------------------------------

class TestBarDims:
    """Bar complex dimension table through degree 5."""

    @pytest.mark.parametrize("n,h,expected", [
        # Row n=1: vacuum module dims
        (1, 2, 1), (1, 3, 1), (1, 4, 2), (1, 5, 2), (1, 6, 4),
        # Row n=2
        (2, 4, 1), (2, 5, 2), (2, 6, 5), (2, 7, 8), (2, 8, 16),
        # Row n=3
        (3, 6, 2), (3, 7, 6), (3, 8, 18), (3, 9, 38), (3, 10, 84),
        # Row n=4
        (4, 8, 6), (4, 9, 24), (4, 10, 84), (4, 11, 216),
        # Row n=5
        (5, 10, 24), (5, 11, 120), (5, 12, 480),
        # Row n=6
        (6, 12, 120),
    ])
    def test_dim(self, n, h, expected):
        assert bar_chain_dim(n, h) == expected

    def test_below_diagonal(self):
        """B^n_h = 0 for h < 2n."""
        assert bar_chain_dim(3, 5) == 0
        assert bar_chain_dim(4, 7) == 0
        assert bar_chain_dim(5, 9) == 0


# ---------------------------------------------------------------------------
# Arnold cancellation
# ---------------------------------------------------------------------------

class TestArnoldCancellation:
    """Arnold relation kills vacuum leakage at degrees >= 3."""

    def test_deg3_vacuum_cancels(self):
        result = arnold_cancellation_deg3()
        assert result["arnold_kills_vacuum"]

    def test_deg3_form_coefficients(self):
        result = arnold_cancellation_deg3()
        assert result["form_coefficients_equal"]

    def test_deg3_symmetric_killed(self):
        result = arnold_cancellation_deg3()
        assert result["symmetric_term_killed"]

    def test_deg4_vacuum_cancels(self):
        result = arnold_cancellation_deg4()
        assert result["vacuum_cancels"]

    def test_deg4_form_dim(self):
        assert arnold_cancellation_deg4()["form_space_dim"] == 6

    def test_deg5_vacuum_cancels(self):
        result = arnold_cancellation_deg5()
        assert result["vacuum_cancels"]

    def test_deg5_form_dim(self):
        assert arnold_cancellation_deg5()["form_space_dim"] == 24


# ---------------------------------------------------------------------------
# Self-consistency
# ---------------------------------------------------------------------------

class TestSelfConsistency:
    def test_all_bar_diff_checks(self):
        for name, ok in verify_virasoro_bar_diff().items():
            assert ok, f"Bar diff check failed: {name}"

    def test_all_curvature_checks(self):
        for name, ok in verify_virasoro_curvature().items():
            assert ok, f"Curvature check failed: {name}"

    def test_all_vacuum_dim_checks(self):
        for name, ok in verify_vacuum_dims().items():
            assert ok, f"Vacuum dim check failed: {name}"

    def test_all_bar_dim_checks(self):
        for name, ok in verify_bar_dims().items():
            assert ok, f"Bar dim check failed: {name}"

    def test_all_arnold_checks(self):
        for name, ok in verify_arnold_cancellation().items():
            assert ok, f"Arnold check failed: {name}"

    def test_all_mixed_weight_checks(self):
        for name, ok in verify_mixed_weight_bar().items():
            assert ok, f"Mixed weight check failed: {name}"
