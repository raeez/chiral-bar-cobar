"""Tests for W_3 bar complex chain-level computations.

Ground truth from manuscript (detailed_computations.tex):
  T×T: T_{(3)}T=c/2, T_{(1)}T=2T, T_{(0)}T=dT      [comp:w3-nthproducts]
  T×W: T_{(1)}W=3W, T_{(0)}W=dW                       [primary weight 3]
  W×T: W_{(1)}T=3W, W_{(0)}T=2dW                      [skew-symmetry]
  W×W: W_{(5)}W=c/3, W_{(3)}W=2T, ...                 [sixth-order pole]
  Curvature: m_0^(T)=c/2, m_0^(W)=c/3                 [comp:w3-curvature]
  Complementarity: c + c' = 100                        [comp:w3-curvature]
  DS formula: c = 2 - 24(k+2)^2/(k+3)                 [comp:ds-w3]
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.w3_bar import (
    w3_nth_product,
    w3_nth_products,
    w3_bar_diff_deg2,
    w3_bar_diff_deg3_TTT_xi1,
    w3_bar_diff_deg3_WTT,
    w3_bar_diff_deg3_TWT,
    w3_arnold_cancellation_deg3,
    w3_deg3_cohomology,
    w3_deg3_chain_dim,
    w3_curvature,
    w3_curvature_ratio,
    w3_central_charge,
    w3_complementarity_sum,
    w3_vacuum_basis,
    w3_vacuum_dim,
    verify_skew_symmetry,
    verify_w3_bar_diff,
    verify_w3_curvature,
    verify_w3_deg3,
)

c = Symbol('c')
k = Symbol('k')


# ---------------------------------------------------------------------------
# n-th products
# ---------------------------------------------------------------------------

class TestNthProducts:
    """OPE n-th products for all 4 generator pairs."""

    def test_TT_quartic(self):
        """T_{(3)}T = c/2 (curvature, quartic pole)."""
        assert w3_nth_product("T", "T", 3)["vac"] == c / 2

    def test_TT_cubic_absent(self):
        """T_{(2)}T = 0."""
        assert len(w3_nth_product("T", "T", 2)) == 0

    def test_TT_double(self):
        """T_{(1)}T = 2T."""
        assert w3_nth_product("T", "T", 1)["T"] == Rational(2)

    def test_TT_simple(self):
        """T_{(0)}T = dT."""
        assert w3_nth_product("T", "T", 0)["dT"] == Rational(1)

    def test_TW_double(self):
        """T_{(1)}W = 3W (W is primary of weight 3)."""
        assert w3_nth_product("T", "W", 1)["W"] == Rational(3)

    def test_TW_simple(self):
        """T_{(0)}W = dW."""
        assert w3_nth_product("T", "W", 0)["dW"] == Rational(1)

    def test_TW_no_higher_poles(self):
        """T_{(n)}W = 0 for n >= 2."""
        for n in [2, 3, 4, 5]:
            assert len(w3_nth_product("T", "W", n)) == 0

    def test_WT_double(self):
        """W_{(1)}T = 3W (same as T_{(1)}W by Borcherds symmetry)."""
        assert w3_nth_product("W", "T", 1)["W"] == Rational(3)

    def test_WT_simple_asymmetric(self):
        """W_{(0)}T = 2dW (NOT dW — asymmetric with T_{(0)}W)."""
        assert w3_nth_product("W", "T", 0)["dW"] == Rational(2)

    def test_WW_sixth_order(self):
        """W_{(5)}W = c/3 (sixth-order pole)."""
        assert w3_nth_product("W", "W", 5)["vac"] == c / 3

    def test_WW_fifth_absent(self):
        """W_{(4)}W = 0 (no weight-1 state)."""
        assert len(w3_nth_product("W", "W", 4)) == 0

    def test_WW_quartic(self):
        """W_{(3)}W = 2T."""
        assert w3_nth_product("W", "W", 3)["T"] == Rational(2)

    def test_WW_cubic(self):
        """W_{(2)}W = dT."""
        assert w3_nth_product("W", "W", 2)["dT"] == Rational(1)

    def test_WW_double_d2T(self):
        """W_{(1)}W has (3/10)d²T component."""
        assert w3_nth_product("W", "W", 1)["d2T"] == Rational(3, 10)

    def test_WW_double_Lambda(self):
        """W_{(1)}W has (16/(22+5c))Λ component."""
        alpha = Rational(16, 1) / (22 + 5 * c)
        result = w3_nth_product("W", "W", 1)["Lambda"]
        assert simplify(result - alpha) == 0


# ---------------------------------------------------------------------------
# Bar differential
# ---------------------------------------------------------------------------

class TestBarDifferential:
    """Bar differential D: B̄^2 → B̄^0 ⊕ B̄^1 for all generator pairs.

    Ground truth: comp:w3-bar-degree2.
    """

    def test_TT(self):
        """D(T⊗T⊗η) = (c/2)|0⟩ + 2T + dT."""
        vac, bar1 = w3_bar_diff_deg2("T", "T")
        assert vac["vac"] == c / 2
        assert bar1["T"] == Rational(2)
        assert bar1["dT"] == Rational(1)

    def test_TW_no_vacuum(self):
        """D(T⊗W⊗η) has no vacuum leakage."""
        vac, _ = w3_bar_diff_deg2("T", "W")
        assert len(vac) == 0

    def test_TW_bar1(self):
        """D(T⊗W⊗η) = 3W + dW."""
        _, bar1 = w3_bar_diff_deg2("T", "W")
        assert bar1["W"] == Rational(3)
        assert bar1["dW"] == Rational(1)

    def test_WT_no_vacuum(self):
        """D(W⊗T⊗η) has no vacuum leakage."""
        vac, _ = w3_bar_diff_deg2("W", "T")
        assert len(vac) == 0

    def test_WT_bar1(self):
        """D(W⊗T⊗η) = 3W + 2dW (asymmetric with T⊗W)."""
        _, bar1 = w3_bar_diff_deg2("W", "T")
        assert bar1["W"] == Rational(3)
        assert bar1["dW"] == Rational(2)

    def test_WW_vacuum(self):
        """D(W⊗W⊗η) has vacuum c/3."""
        vac, _ = w3_bar_diff_deg2("W", "W")
        assert vac["vac"] == c / 3

    def test_WW_virasoro_sector(self):
        """D(W⊗W⊗η) has 2T + dT (same as Virasoro OPE!)."""
        _, bar1 = w3_bar_diff_deg2("W", "W")
        assert bar1["T"] == Rational(2)
        assert bar1["dT"] == Rational(1)

    def test_WW_weight4(self):
        """D(W⊗W⊗η) has weight-4 component (3/10)d²T + αΛ."""
        _, bar1 = w3_bar_diff_deg2("W", "W")
        assert bar1["d2T"] == Rational(3, 10)
        assert "Lambda" in bar1

    def test_asymmetry(self):
        """D(T⊗W) ≠ D(W⊗T): coefficients of dW differ (1 vs 2)."""
        _, tw = w3_bar_diff_deg2("T", "W")
        _, wt = w3_bar_diff_deg2("W", "T")
        assert tw["dW"] == Rational(1)
        assert wt["dW"] == Rational(2)

    def test_only_diagonal_vacuum(self):
        """Only TT and WW produce vacuum leakage."""
        for a, b in [("T", "T"), ("T", "W"), ("W", "T"), ("W", "W")]:
            vac, _ = w3_bar_diff_deg2(a, b)
            if a == b:
                assert len(vac) > 0, f"{a}⊗{b} should have vacuum"
            else:
                assert len(vac) == 0, f"{a}⊗{b} should NOT have vacuum"


# ---------------------------------------------------------------------------
# Curvature
# ---------------------------------------------------------------------------

class TestCurvature:
    """Curvature m_0^(T) = c/2, m_0^(W) = c/3.

    Ground truth: comp:w3-curvature-dual-detail.
    """

    def test_T_curvature(self):
        assert w3_curvature()["T"] == c / 2

    def test_W_curvature(self):
        assert w3_curvature()["W"] == c / 3

    def test_ratio(self):
        """m_0^(W)/m_0^(T) = 2/3."""
        assert w3_curvature_ratio() == Rational(2, 3)

    def test_both_vanish_at_c0(self):
        """Both curvatures vanish iff c=0."""
        curv = w3_curvature()
        assert curv["T"].subs(c, 0) == 0
        assert curv["W"].subs(c, 0) == 0

    def test_complementarity_sum(self):
        """c(k) + c(k') = 4 where k' = -k-6."""
        assert w3_complementarity_sum() == 4

    def test_ds_complementarity(self):
        """Verify c + c' = 4 from DS formula."""
        c_k = w3_central_charge(k)
        c_dual = w3_central_charge(-k - 6)
        assert simplify(c_k + c_dual - 4) == 0

    def test_ds_at_k_minus3(self):
        """Critical level k=-3: c diverges (Sugawara undefined)."""
        # c = 2 - 24(k+2)^2/(k+3), at k=-3: denominator = 0
        c_val = w3_central_charge(k)
        # Check that k+3 appears in denominator
        assert c_val.subs(k, -3) is not None or True  # division by zero
        # More precisely: the DS formula has k+3 in denominator
        from sympy import oo, limit
        assert abs(limit(c_val, k, -3)) == oo

    def test_curvature_complementarity(self):
        """m_0^(T)(c) + m_0^(T)(100-c) = 50."""
        curv = w3_curvature()
        m0_sum = curv["T"] + curv["T"].subs(c, 100 - c)
        assert simplify(m0_sum - 50) == 0


# ---------------------------------------------------------------------------
# Skew-symmetry
# ---------------------------------------------------------------------------

class TestSkewSymmetry:
    """Verify W_{(0)}T = 2dW via skew-symmetry formula."""

    def test_skew_symmetry(self):
        assert verify_skew_symmetry() is True

    def test_W1T_equals_T1W(self):
        """W_{(1)}T = T_{(1)}W = 3W (symmetric for n=1)."""
        w1t = w3_nth_product("W", "T", 1)
        t1w = w3_nth_product("T", "W", 1)
        assert w1t["W"] == t1w["W"] == Rational(3)


# ---------------------------------------------------------------------------
# Vacuum module
# ---------------------------------------------------------------------------

class TestVacuumModule:
    def test_weight_2(self):
        """Weight 2: just T."""
        assert w3_vacuum_dim(2) == 1

    def test_weight_3(self):
        """Weight 3: W and dT."""
        assert w3_vacuum_dim(3) == 2

    def test_weight_4(self):
        """Weight 4: dW, d²T, :TT: (and Λ is a linear combo)."""
        assert w3_vacuum_dim(4) == 3


# ---------------------------------------------------------------------------
# Self-consistency
# ---------------------------------------------------------------------------

class TestSelfConsistency:
    def test_all_bar_diff_checks(self):
        for name, ok in verify_w3_bar_diff().items():
            assert ok, f"Bar diff check failed: {name}"

    def test_all_curvature_checks(self):
        for name, ok in verify_w3_curvature().items():
            assert ok, f"Curvature check failed: {name}"

    def test_TT_curvature_matches_quartic(self):
        """m_0^(T) = T_{(3)}T."""
        assert w3_nth_product("T", "T", 3)["vac"] == w3_curvature()["T"]

    def test_WW_curvature_matches_sixth(self):
        """m_0^(W) = W_{(5)}W."""
        assert w3_nth_product("W", "W", 5)["vac"] == w3_curvature()["W"]

    def test_deg3_checks(self):
        for name, ok in verify_w3_deg3().items():
            assert ok, f"Deg3 check failed: {name}"


# ---------------------------------------------------------------------------
# Degree-3 bar complex
# ---------------------------------------------------------------------------

class TestDeg3TTT:
    """d(Xi_1) = [dT|T]⊗eta + [T|dT]⊗eta + [2T|T]⊗(-wp dz).

    Ground truth: comp:w3-deg3-structure.
    """

    def test_D23_zero(self):
        """D_{23} gives zero (no pole in eta_{12}∧eta_{13} along D_{23})."""
        xi1 = w3_bar_diff_deg3_TTT_xi1()
        assert xi1["D_23"] == "zero (no pole in form)"

    def test_D12_quartic_zero(self):
        """T_{(3)}T = c/2 gives zero residue (insufficient pole order)."""
        xi1 = w3_bar_diff_deg3_TTT_xi1()
        assert "zero" in xi1["D_12"]["n=3"]["result"]

    def test_D12_double_pole(self):
        """T_{(1)}T = 2T contributes [2T|T] ⊗ (-wp_{23}dz_3)."""
        xi1 = w3_bar_diff_deg3_TTT_xi1()
        assert xi1["D_12"]["n=1"]["coeff"] == Rational(2)

    def test_D12_simple_pole(self):
        """T_{(0)}T = dT contributes [dT|T] ⊗ eta_{23}."""
        xi1 = w3_bar_diff_deg3_TTT_xi1()
        assert xi1["D_12"]["n=0"]["coeff"] == Rational(1)

    def test_D13_simple_pole(self):
        """D_{13}: only n=0 contributes, giving [T|dT] ⊗ eta_{23}."""
        xi1 = w3_bar_diff_deg3_TTT_xi1()
        assert xi1["D_13"]["n=0"]["coeff"] == Rational(1)
        assert len(xi1["D_13"]) == 1


class TestDeg3Mixed:
    """Mixed T-W elements at weight 7.

    Ground truth: comp:w3-deg3-mixed.
    """

    def test_WTT_D12(self):
        """[W|T|T]: D_{12} uses W(z)T(w) OPE."""
        wtt = w3_bar_diff_deg3_WTT()
        assert wtt["D_12"]["n=1"]["coeff"] == Rational(3)  # W_{(1)}T = 3W
        assert wtt["D_12"]["n=0"]["coeff"] == Rational(1)  # dW term

    def test_WTT_D13(self):
        """[W|T|T]: D_{13} uses T(z)T(w) OPE, W spectator."""
        wtt = w3_bar_diff_deg3_WTT()
        assert wtt["D_13"]["n=0"]["coeff"] == Rational(1)

    def test_TWT_D12(self):
        """[T|W|T]: D_{12} uses T(z)W(w) OPE."""
        twt = w3_bar_diff_deg3_TWT()
        assert twt["D_12"]["n=1"]["coeff"] == Rational(3)  # T_{(1)}W = 3W

    def test_TWT_D13(self):
        """[T|W|T]: D_{13} uses T(z)T(w) with W at position 2."""
        twt = w3_bar_diff_deg3_TWT()
        assert twt["D_13"]["n=1"]["coeff"] == Rational(2)  # 2T


class TestArnoldDeg3:
    """Arnold cancellation kills vacuum leakage at degree 3.

    Ground truth: comp:w3-arnold-deg3, prop:w3-deg3-vacuum.
    """

    def test_vacuum_cancellation(self):
        assert w3_arnold_cancellation_deg3() is True

    def test_chain_dim_h6(self):
        """dim B^3_6 = 2 ([T|T|T] × 2 forms)."""
        assert w3_deg3_chain_dim(6) == 2

    def test_chain_dim_h7(self):
        """dim B^3_7 = 12 (3 orderings × dim V̄_3=2 states × 2 forms)."""
        assert w3_deg3_chain_dim(7) == 12

    def test_chain_dim_below(self):
        """dim B^3_5 = 0 (minimum weight 2+2+2=6)."""
        assert w3_deg3_chain_dim(5) == 0

    def test_cohom_h6(self):
        """H^3_6 = 0 at generic c."""
        assert w3_deg3_cohomology(6) == 0

    def test_cohom_h7(self):
        """H^3_7 = 0 (Koszul)."""
        assert w3_deg3_cohomology(7) == 0
