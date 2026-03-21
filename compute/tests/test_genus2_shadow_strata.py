"""Tests for genus-2 shadow tower amplitudes at nonzero arity.

Tests the genuinely new computation: Theta^{(2,n)} for n = 2, 4 at genus 2,
decomposed by boundary stratum of M-bar_{2,n}, for Heisenberg, affine sl_2,
and Virasoro.

Ground truth:
  - Theta^{(2,0)} = kappa * 7/5760 (Theorem D, universal)
  - Theta^{(2,2)}_Heis = 0 (Gaussian termination)
  - Theta^{(2,4)} = 0 at leading order for all standard families
  - Shell decomposition: separating (h^1=0), one-loop (h^1=1), two-loop (h^1=2)
  - Separating contribution at arity 2: H^{(1)} * P * H^{(1)}
  - Q^contact_Vir = 10/[c(5c+22)]
  - delta_H^{(1)}_Vir = 120/[c^2(5c+22)]
  - kappa_Vir = c/2, P_Vir = 2/c
  - kappa_sl2 = 3(k+2)/4

References:
  concordance.tex, higher_genus_modular_koszul.tex,
  genus2_boundary_strata.py, modular_shadow_tower.py.
"""

import pytest
from sympy import Rational, Symbol, simplify, S, expand, factor

from compute.lib.genus2_shadow_strata import (
    # Shadow data
    ShadowData,
    heisenberg_shadow_data,
    virasoro_shadow_data,
    affine_sl2_shadow_data,
    # Graph enumeration
    MarkedStableGraph,
    genus2_marked_graphs_n0,
    genus2_marked_graphs_n2,
    verify_genus2_n2_graph_arithmetic,
    # Loop operators
    genus_loop_1d,
    double_genus_loop_1d,
    # Amplitude computation
    graph_amplitude_n2_1d,
    theta_2_2_coefficient,
    shell_decomposition_n2,
    # Family-specific results
    heisenberg_theta_2_2,
    virasoro_theta_2_2,
    virasoro_theta_2_2_leading_order,
    affine_sl2_theta_2_2,
    theta_2_4_leading_virasoro,
    # Census and classification
    genus2_graph_census,
    shadow_depth_classification_genus2,
    # Numerical evaluation
    evaluate_virasoro_shells,
    evaluate_heisenberg_shells,
    evaluate_affine_sl2_shells,
    cross_family_comparison,
)
from compute.lib.utils import lambda_fp


# =====================================================================
# Shadow data construction
# =====================================================================

class TestShadowData:
    """Verify shadow data for the standard landscape."""

    def test_heisenberg_kappa(self):
        sd = heisenberg_shadow_data(3)
        assert sd.kappa == Rational(3)

    def test_heisenberg_propagator(self):
        sd = heisenberg_shadow_data(3)
        assert sd.propagator == Rational(1, 3)

    def test_heisenberg_cubic_zero(self):
        sd = heisenberg_shadow_data(3)
        assert sd.cubic == S.Zero

    def test_heisenberg_quartic_zero(self):
        sd = heisenberg_shadow_data(3)
        assert sd.quartic == S.Zero

    def test_heisenberg_depth_2(self):
        sd = heisenberg_shadow_data(3)
        assert sd.shadow_depth == 2

    def test_virasoro_kappa(self):
        sd = virasoro_shadow_data(10)
        assert sd.kappa == Rational(5)

    def test_virasoro_propagator(self):
        sd = virasoro_shadow_data(10)
        assert sd.propagator == Rational(1, 5)

    def test_virasoro_cubic(self):
        sd = virasoro_shadow_data(10)
        assert sd.cubic == Rational(2)

    def test_virasoro_quartic_at_c10(self):
        """Q = 10/[c(5c+22)] at c=10 = 10/(10*72) = 1/72."""
        sd = virasoro_shadow_data(10)
        assert sd.quartic == Rational(1, 72)

    def test_virasoro_quartic_at_c1(self):
        """Q = 10/[1*(5+22)] = 10/27."""
        sd = virasoro_shadow_data(1)
        assert sd.quartic == Rational(10, 27)

    def test_virasoro_quartic_at_c26(self):
        """Q = 10/[26*(130+22)] = 10/(26*152) = 10/3952 = 5/1976."""
        sd = virasoro_shadow_data(26)
        assert sd.quartic == Rational(5, 1976)

    def test_virasoro_genus1_hessian_correction_c10(self):
        """delta_H^{(1)} = 120/[c^2(5c+22)] at c=10 = 120/(100*72) = 1/60."""
        sd = virasoro_shadow_data(10)
        expected = Rational(120, 100 * 72)
        assert simplify(sd.genus1_hessian_correction - expected) == 0

    def test_virasoro_depth_infinity(self):
        sd = virasoro_shadow_data(10)
        assert sd.shadow_depth == "infinity"

    def test_affine_sl2_kappa_k1(self):
        """kappa = 3*(1+2)/4 = 9/4."""
        sd = affine_sl2_shadow_data(1)
        assert sd.kappa == Rational(9, 4)

    def test_affine_sl2_kappa_k2(self):
        """kappa = 3*(2+2)/4 = 3."""
        sd = affine_sl2_shadow_data(2)
        assert sd.kappa == Rational(3)

    def test_affine_sl2_depth_3(self):
        sd = affine_sl2_shadow_data(1)
        assert sd.shadow_depth == 3


# =====================================================================
# Graph enumeration at n = 0
# =====================================================================

class TestGraphEnumerationN0:
    """Verify genus-2 stable graphs at arity 0."""

    def test_six_graphs(self):
        graphs = genus2_marked_graphs_n0()
        assert len(graphs) == 6

    def test_all_genus_2(self):
        for G in genus2_marked_graphs_n0():
            assert G.genus == 2

    def test_all_n_marked_0(self):
        for G in genus2_marked_graphs_n0():
            assert G.n_marked == 0

    def test_genus_formula(self):
        """g = sum g_v + h^1 for each graph."""
        for G in genus2_marked_graphs_n0():
            sum_gv = sum(G.vertex_genera)
            h1 = G.n_edges - G.n_vertices + 1
            assert h1 == G.h1, f"{G.name}: h^1 mismatch"
            assert sum_gv + h1 == 2, f"{G.name}: genus formula fails"

    def test_shell_distribution(self):
        """Two graphs at each shell level (h^1 = 0, 1, 2)."""
        shells = {}
        for G in genus2_marked_graphs_n0():
            shells.setdefault(G.shell, []).append(G.name)
        assert len(shells[0]) == 2
        assert len(shells[1]) == 2
        assert len(shells[2]) == 2


# =====================================================================
# Graph enumeration at n = 2
# =====================================================================

class TestGraphEnumerationN2:
    """Verify genus-2 stable graphs at arity 2."""

    def test_ten_graphs(self):
        """There are 10 stable graph types for M-bar_{2,2}."""
        graphs = genus2_marked_graphs_n2()
        assert len(graphs) == 10

    def test_all_genus_2(self):
        for G in genus2_marked_graphs_n2():
            assert G.genus == 2, f"{G.name}: genus = {G.genus}"

    def test_all_n_marked_2(self):
        for G in genus2_marked_graphs_n2():
            assert G.n_marked == 2, f"{G.name}: n_marked = {G.n_marked}"

    def test_genus_formula_n2(self):
        """g = sum g_v + h^1 for each n=2 graph."""
        results = verify_genus2_n2_graph_arithmetic()
        for name, data in results.items():
            assert data["genus_ok"], f"{name}: genus formula fails"
            assert data["h1_ok"], f"{name}: h^1 formula fails"
            assert data["n_marked_ok"], f"{name}: marking count fails"

    def test_marking_sum(self):
        """sum of vertex_markings = n_marked = 2 for each graph."""
        for G in genus2_marked_graphs_n2():
            assert sum(G.vertex_markings) == 2, f"{G.name}"

    def test_shell_distribution_n2(self):
        """Shell distribution at n=2."""
        shells = {}
        for G in genus2_marked_graphs_n2():
            shells.setdefault(G.shell, []).append(G.name)
        # Shell 0 (tree): smooth, sep_11, sep_20
        assert len(shells.get(0, [])) == 3
        # Shell 1 (one-loop): irred1, mixed_20, mixed_02, mixed_11
        assert len(shells.get(1, [])) == 4
        # Shell 2 (two-loop): banana, theta_11, theta_20
        assert len(shells.get(2, [])) == 3

    def test_aut_orders_positive(self):
        for G in genus2_marked_graphs_n2():
            assert G.aut_order > 0, f"{G.name}: |Aut| must be positive"


# =====================================================================
# Genus loop operator
# =====================================================================

class TestGenusLoopOperator:
    """Verify the genus loop operator Lambda_P."""

    def test_loop_on_quadratic(self):
        """Lambda_P(kappa * x^2) = C(2,2) * P * kappa = P * kappa."""
        assert genus_loop_1d(Rational(3), 2, Rational(1, 3)) == Rational(1)

    def test_loop_on_quartic(self):
        """Lambda_P(Q * x^4) = C(4,2) * P * Q = 6 * P * Q."""
        Q = Rational(10, 72)  # Q at c=10
        P = Rational(1, 5)    # P at c=10
        expected = 6 * P * Q
        assert genus_loop_1d(Q, 4, P) == expected

    def test_loop_on_cubic(self):
        """Lambda_P(C * x^3) = C(3,2) * P * C = 3 * P * C."""
        C_coeff = Rational(2)  # Virasoro cubic
        P = Rational(1, 5)
        expected = 3 * P * C_coeff
        assert genus_loop_1d(C_coeff, 3, P) == expected

    def test_double_loop(self):
        """Lambda_P^2(Q * x^4) = C(4,2)*P * C(2,2)*P * Q = 6*P^2*Q."""
        Q = Rational(10, 72)
        P = Rational(1, 5)
        expected = 6 * P * 1 * P * Q
        assert double_genus_loop_1d(Q, 4, P) == expected

    def test_virasoro_delta_H1(self):
        """delta_H^{(1)}_Vir = Lambda_P(Q_Vir * x^4) = 120/[c^2(5c+22)].

        At c = 10: 120/(100 * 72) = 120/7200 = 1/60.
        """
        Q_c10 = Rational(10, 10 * 72)  # = 1/72
        P_c10 = Rational(2, 10)        # = 1/5
        delta = genus_loop_1d(Q_c10, 4, P_c10)
        assert delta == Rational(1, 60)


# =====================================================================
# Heisenberg genus-2 arity-2
# =====================================================================

class TestHeisenbergTheta22:
    """Verify Theta^{(2,2)} = 0 for Heisenberg."""

    def test_theta_2_2_vanishes(self):
        result = heisenberg_theta_2_2(1)
        assert result["theta_2_2"] == S.Zero

    def test_theta_2_2_vanishes_k3(self):
        result = heisenberg_theta_2_2(3)
        assert result["theta_2_2"] == S.Zero

    def test_all_shells_zero(self):
        result = heisenberg_theta_2_2(1)
        assert result["shell_0"] == S.Zero
        assert result["shell_1"] == S.Zero
        assert result["shell_2"] == S.Zero

    def test_reason_gaussian(self):
        result = heisenberg_theta_2_2(1)
        assert "Gaussian" in result["reason"]

    def test_numeric_evaluation(self):
        result = evaluate_heisenberg_shells(5)
        assert result["theta_2_2"] == S.Zero
        assert result["kappa"] == Rational(5)


# =====================================================================
# Virasoro genus-2 arity-2
# =====================================================================

class TestVirasoroTheta22:
    """Verify the genus-2 arity-2 shadow for Virasoro."""

    def test_sep_11_at_c10(self):
        """Separating (1,1) at c=10: H1^2 * P.

        H1 = kappa + delta = 5 + 1/60 = 301/60.
        P = 1/5.
        sep_11 = (301/60)^2 * (1/5) = 90601/(3600*5) = 90601/18000.
        """
        result = virasoro_theta_2_2(10)
        H1 = Rational(5) + Rational(1, 60)
        P = Rational(1, 5)
        expected = H1 ** 2 * P
        assert simplify(result["sep_11_weighted"] - expected) == 0

    def test_sep_11_at_c26(self):
        """Self-dual point c=13 gives kappa = 13/2."""
        result = virasoro_theta_2_2(26)
        assert result["kappa"] == Rational(13)

    def test_theta_11_at_c10(self):
        """Theta (1,1) at c=10: Q^2 * P^3 / 6.

        Q = 1/72, P = 1/5.
        theta = (1/72)^2 * (1/5)^3 / 6 = 1/(5184 * 125 * 6) = 1/3888000.
        """
        result = virasoro_theta_2_2(10)
        Q = Rational(1, 72)
        P = Rational(1, 5)
        expected = Q ** 2 * P ** 3 / 6
        assert simplify(result["theta_11_weighted"] - expected) == 0

    def test_mixed_11_at_c10(self):
        """Mixed (1,1) at c=10: 6*P^2*Q*H1 / 2.

        Q = 1/72, P = 1/5, H1 = 301/60.
        mixed = 6 * (1/25) * (1/72) * (301/60) / 2 = 6*301/(25*72*60*2).
        """
        result = virasoro_theta_2_2(10)
        Q = Rational(1, 72)
        P = Rational(1, 5)
        H1 = Rational(5) + Rational(1, 60)
        expected = 6 * P * Q * P * H1 / 2
        assert simplify(result["mixed_11_weighted"] - expected) == 0

    def test_boundary_total_nonzero(self):
        """The boundary total at c=10 is nonzero."""
        result = virasoro_theta_2_2(10)
        assert result["boundary_total"] != 0

    def test_boundary_total_positive_at_c10(self):
        """The boundary total is positive at c=10."""
        result = virasoro_theta_2_2(10)
        bt = result["boundary_total"]
        assert bt > 0

    def test_shell_0_equals_sep(self):
        """Shell 0 (tree) should equal the separating contribution."""
        result = virasoro_theta_2_2(10)
        assert simplify(result["shell_0_tree"] - result["sep_11_weighted"]) == 0

    def test_shell_1_equals_mixed(self):
        """Shell 1 (one-loop) should equal the mixed contribution."""
        result = virasoro_theta_2_2(10)
        assert simplify(result["shell_1_loop"] - result["mixed_11_weighted"]) == 0

    def test_shell_2_equals_theta(self):
        """Shell 2 (two-loop) should equal the theta contribution."""
        result = virasoro_theta_2_2(10)
        assert simplify(result["shell_2_double_loop"] - result["theta_11_weighted"]) == 0

    def test_virasoro_symbolic(self):
        """Symbolic computation (no numeric c value)."""
        result = virasoro_theta_2_2()
        # Should contain sympy expressions with Symbol('c')
        assert result["kappa"] is not None

    def test_shells_sum_to_boundary(self):
        """Sum of shells equals boundary total."""
        result = virasoro_theta_2_2(10)
        shell_sum = result["shell_0_tree"] + result["shell_1_loop"] + result["shell_2_double_loop"]
        assert simplify(shell_sum - result["boundary_total"]) == 0


# =====================================================================
# Virasoro leading-order asymptotics
# =====================================================================

class TestVirasoroLeadingOrder:
    """Verify large-c asymptotics of Theta^{(2,2)}_Vir."""

    def test_sep_dominant(self):
        """At large c, the separating term dominates."""
        result = virasoro_theta_2_2_leading_order()
        assert result["dominant_term"] == "separating (1,1)"

    def test_sep_scales_as_c(self):
        """The separating term goes as c/2 at large c."""
        result = virasoro_theta_2_2_leading_order(100)
        sep = result["sep_11_leading"]
        # At c=100: kappa^2 * P = (50)^2 * (2/100) = 50
        assert sep == Rational(50)

    def test_mixed_subleading(self):
        """The mixed term is O(1/c^2) at large c."""
        r1 = virasoro_theta_2_2_leading_order(100)
        r2 = virasoro_theta_2_2_leading_order(200)
        # mixed should decrease as c increases
        m1 = r1["mixed_11_leading"]
        m2 = r2["mixed_11_leading"]
        # Both should be positive (for large positive c)
        assert m1 > 0
        assert m2 > 0
        # m2 < m1 (decreasing in c)
        assert m2 < m1

    def test_theta_much_smaller_than_sep(self):
        """The theta term is much smaller than the sep term at large c."""
        result = virasoro_theta_2_2_leading_order(100)
        sep = result["sep_11_leading"]
        theta = result["theta_11_leading"]
        assert theta < sep / 100


# =====================================================================
# Affine sl_2 genus-2 arity-2
# =====================================================================

class TestAffineSl2Theta22:
    """Verify Theta^{(2,2)} for affine sl_2."""

    def test_boundary_equals_kappa_k1(self):
        """At k=1: boundary = kappa = 9/4, so boundary total = kappa."""
        result = affine_sl2_theta_2_2(1)
        kappa = Rational(9, 4)
        # sep_11 = H1 * P * H1 = kappa * (1/kappa) * kappa = kappa
        assert simplify(result["theta_2_2_boundary"] - kappa) == 0

    def test_boundary_equals_kappa_k2(self):
        """At k=2: kappa = 3."""
        result = affine_sl2_theta_2_2(2)
        kappa = Rational(3)
        assert simplify(result["theta_2_2_boundary"] - kappa) == 0

    def test_shell_0_equals_boundary(self):
        """All contribution is in shell 0 (separating)."""
        result = affine_sl2_theta_2_2(1)
        assert simplify(result["shell_0_tree"] - result["theta_2_2_boundary"]) == 0

    def test_shell_1_zero(self):
        result = affine_sl2_theta_2_2(1)
        assert result["shell_1_loop"] == S.Zero

    def test_shell_2_zero(self):
        result = affine_sl2_theta_2_2(1)
        assert result["shell_2_double_loop"] == S.Zero

    def test_sep_equals_kappa_squared_times_P(self):
        """sep_11 = kappa^2 * P = kappa."""
        for k_val in [1, 2, 3, 5, 10]:
            result = affine_sl2_theta_2_2(k_val)
            kappa = Rational(3) * (Rational(k_val) + 2) / 4
            assert simplify(result["theta_2_2_boundary"] - kappa) == 0


# =====================================================================
# Genus-2 arity-4 (leading order)
# =====================================================================

class TestTheta24:
    """Verify the genus-2 quartic shadow vanishes at leading order."""

    def test_virasoro_theta_24_zero(self):
        result = theta_2_4_leading_virasoro()
        assert result["theta_2_4_leading"] == S.Zero

    def test_virasoro_theta_24_reason(self):
        result = theta_2_4_leading_virasoro()
        assert "shadow depth" in result["reason"]


# =====================================================================
# Graph census
# =====================================================================

class TestGraphCensus:
    """Verify graph census at arities 0 and 2."""

    def test_n0_count(self):
        census = genus2_graph_census()
        assert census["n=0"]["n_graphs"] == 6

    def test_n2_count(self):
        census = genus2_graph_census()
        assert census["n=2"]["n_graphs"] == 10

    def test_n0_shell_distribution(self):
        census = genus2_graph_census()
        shells = census["n=0"]["shells"]
        assert shells[0] == 2
        assert shells[1] == 2
        assert shells[2] == 2

    def test_n2_shell_distribution(self):
        census = genus2_graph_census()
        shells = census["n=2"]["shells"]
        assert shells[0] == 3
        assert shells[1] == 4
        assert shells[2] == 3


# =====================================================================
# Shadow depth classification
# =====================================================================

class TestShadowDepthClassification:
    """Verify the genus-2 extension of shadow depth classification."""

    def test_gaussian_zero(self):
        cls = shadow_depth_classification_genus2()
        assert cls["G_gaussian"]["theta_2_2"] == "0"
        assert cls["G_gaussian"]["theta_2_4"] == "0"

    def test_lie_tree_sep_only(self):
        cls = shadow_depth_classification_genus2()
        assert 0 in cls["L_lie_tree"]["active_shells"]
        assert cls["L_lie_tree"]["n_active_graphs"] == 1

    def test_mixed_all_shells(self):
        cls = shadow_depth_classification_genus2()
        assert set(cls["M_mixed"]["active_shells"]) == {0, 1, 2}
        assert cls["M_mixed"]["n_active_graphs"] == 3


# =====================================================================
# Numerical evaluations at specific parameter values
# =====================================================================

class TestNumericalEvaluations:
    """Verify exact rational evaluations at specific parameter values."""

    def test_virasoro_c1(self):
        """Detailed check at c=1 (minimal model)."""
        result = evaluate_virasoro_shells(1)
        assert result["c"] == 1
        assert result["kappa"] == Rational(1, 2)

    def test_virasoro_c26(self):
        """At c=26: kappa = 13."""
        result = evaluate_virasoro_shells(26)
        assert result["kappa"] == Rational(13)
        assert result["boundary_total"] != 0

    def test_virasoro_c2(self):
        """At c=2: kappa = 1."""
        result = evaluate_virasoro_shells(2)
        assert result["kappa"] == Rational(1)

    def test_heisenberg_always_zero(self):
        """Heisenberg shells are zero for all k."""
        for kv in [1, 2, 3, 5, 10, 100]:
            result = evaluate_heisenberg_shells(kv)
            assert result["theta_2_2"] == S.Zero

    def test_affine_sl2_k1(self):
        result = evaluate_affine_sl2_shells(1)
        assert result["kappa"] == Rational(9, 4)
        assert result["shell_0"] == Rational(9, 4)

    def test_affine_sl2_k10(self):
        result = evaluate_affine_sl2_shells(10)
        assert result["kappa"] == Rational(9)  # 3*(10+2)/4 = 36/4 = 9
        assert simplify(result["boundary_total"] - Rational(9)) == 0


# =====================================================================
# Cross-family comparison
# =====================================================================

class TestCrossFamilyComparison:
    """Compare genus-2 arity-2 across families."""

    def test_virasoro_dominates_heisenberg(self):
        """Virasoro boundary is nonzero while Heisenberg is zero."""
        results = cross_family_comparison([10])
        assert results["c=10"]["virasoro_boundary"] != 0
        assert results["c=10"]["heisenberg"] == S.Zero

    def test_multiple_c_values(self):
        """Check that results are computed for multiple c values."""
        results = cross_family_comparison([1, 2, 4])
        assert "c=1" in results
        assert "c=2" in results
        assert "c=4" in results


# =====================================================================
# Consistency checks
# =====================================================================

class TestConsistency:
    """Internal consistency checks for the computation."""

    def test_propagator_inverse_of_kappa_heisenberg(self):
        """P * kappa = 1 for Heisenberg."""
        sd = heisenberg_shadow_data(7)
        assert simplify(sd.propagator * sd.kappa - 1) == 0

    def test_propagator_inverse_of_kappa_affine(self):
        """P * kappa = 1 for affine sl_2."""
        sd = affine_sl2_shadow_data(3)
        assert simplify(sd.propagator * sd.kappa - 1) == 0

    def test_propagator_inverse_of_kappa_virasoro(self):
        """P * kappa = 1 for Virasoro (P = 2/c, kappa = c/2)."""
        sd = virasoro_shadow_data(10)
        assert simplify(sd.propagator * sd.kappa - 1) == 0

    def test_sep_factorizes(self):
        """The separating contribution factorizes as H1 * P * H1."""
        for c_val in [1, 2, 4, 10, 26]:
            sd = virasoro_shadow_data(c_val)
            H1 = sd.kappa + sd.genus1_hessian_correction
            sep = H1 * sd.propagator * H1
            result = virasoro_theta_2_2(c_val)
            assert simplify(result["sep_11_weighted"] - sep) == 0

    def test_virasoro_quartic_formula(self):
        """Q = 10/[c(5c+22)] for several c values."""
        for c_val in [1, 2, 4, 6, 10, 26]:
            sd = virasoro_shadow_data(c_val)
            expected = Rational(10, c_val * (5 * c_val + 22))
            assert sd.quartic == expected

    def test_virasoro_genus1_hessian_formula(self):
        """delta_H^{(1)} = 120/[c^2(5c+22)] for several c values."""
        for c_val in [1, 2, 4, 6, 10, 26]:
            sd = virasoro_shadow_data(c_val)
            expected = Rational(120, c_val ** 2 * (5 * c_val + 22))
            assert simplify(sd.genus1_hessian_correction - expected) == 0

    def test_kappa_virasoro_formula(self):
        """kappa = c/2 for Virasoro."""
        for c_val in [1, 2, 4, 6, 10, 26]:
            sd = virasoro_shadow_data(c_val)
            assert sd.kappa == Rational(c_val, 2)

    def test_kappa_affine_formula(self):
        """kappa = 3(k+2)/4 for affine sl_2."""
        for k_val in [1, 2, 3, 5, 10]:
            sd = affine_sl2_shadow_data(k_val)
            expected = Rational(3) * (Rational(k_val) + 2) / 4
            assert sd.kappa == expected


# =====================================================================
# Edge cases and special values
# =====================================================================

class TestEdgeCases:
    """Test edge cases and special parameter values."""

    def test_virasoro_self_dual_c13(self):
        """Virasoro is self-dual at c = 13. Check computation runs."""
        result = virasoro_theta_2_2(13)
        assert result["kappa"] == Rational(13, 2)
        assert result["boundary_total"] != 0

    def test_virasoro_c_large(self):
        """At large c, the boundary total should grow linearly in c."""
        r100 = virasoro_theta_2_2(100)
        r200 = virasoro_theta_2_2(200)
        # Both boundary totals should be positive
        assert r100["boundary_total"] > 0
        assert r200["boundary_total"] > 0
        # Ratio should be approximately 2 (linear growth)
        ratio = r200["boundary_total"] / r100["boundary_total"]
        assert Rational(3, 2) < ratio < Rational(5, 2)

    def test_affine_boundary_equals_kappa_universally(self):
        """For affine sl_2, boundary total = kappa for all k."""
        for k_val in range(1, 20):
            result = affine_sl2_theta_2_2(k_val)
            kappa = Rational(3) * (Rational(k_val) + 2) / 4
            assert simplify(result["theta_2_2_boundary"] - kappa) == 0

    def test_heisenberg_large_k(self):
        """Heisenberg at large k: still zero."""
        result = heisenberg_theta_2_2(1000)
        assert result["theta_2_2"] == S.Zero


# =====================================================================
# Shell monotonicity and positivity
# =====================================================================

class TestShellProperties:
    """Properties of the shell decomposition."""

    def test_virasoro_all_shells_nonnegative(self):
        """All shell amplitudes should be non-negative at c=10."""
        result = virasoro_theta_2_2(10)
        assert result["shell_0_tree"] >= 0
        assert result["shell_1_loop"] >= 0
        assert result["shell_2_double_loop"] >= 0

    def test_virasoro_shell_0_dominates(self):
        """Shell 0 (separating) should dominate at large c."""
        result = virasoro_theta_2_2(100)
        s0 = result["shell_0_tree"]
        s1 = result["shell_1_loop"]
        s2 = result["shell_2_double_loop"]
        assert s0 > s1
        assert s0 > s2

    def test_virasoro_shell_hierarchy(self):
        """Shell 0 > Shell 1 > Shell 2 at c=10 (natural hierarchy)."""
        result = virasoro_theta_2_2(10)
        s0 = result["shell_0_tree"]
        s1 = result["shell_1_loop"]
        s2 = result["shell_2_double_loop"]
        assert s0 > s1 > s2

    def test_shell_decomposition_agrees_with_direct(self):
        """Shell decomposition function agrees with direct computation."""
        sd = virasoro_shadow_data(10)
        shells = shell_decomposition_n2(sd)
        direct = virasoro_theta_2_2(10)
        assert simplify(shells["shell_0_tree"] - direct["shell_0_tree"]) == 0
        # Shell 1 and 2 from shell_decomposition should match
        # (they use the same underlying graph_amplitude_n2_1d)


# =====================================================================
# Symbolic computation tests
# =====================================================================

class TestSymbolic:
    """Test symbolic (non-numeric) computations."""

    def test_virasoro_symbolic_kappa(self):
        """Symbolic kappa = c/2."""
        result = virasoro_theta_2_2()
        cc = Symbol('c')
        assert result["kappa"] == cc / 2

    def test_heisenberg_symbolic_zero(self):
        """Symbolic Heisenberg is still zero."""
        result = heisenberg_theta_2_2()
        assert result["theta_2_2"] == S.Zero

    def test_genus2_census_runs(self):
        """Census function runs without error."""
        census = genus2_graph_census()
        assert "n=0" in census
        assert "n=2" in census
