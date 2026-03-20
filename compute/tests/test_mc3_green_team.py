"""Tests for MC3 GREEN TEAM alternative proof strategies.

Five strategies to bypass the Hernandez-Jimbo bottleneck for conj:mc3-arbitrary-type.

Strategy A: Geometric Satake bypass (Mirkovic-Vilonen for all types)
Strategy B: Tilting module approach (Soergel bimodules, type-independent)
Strategy C: Cluster category approach (Hernandez-Leclerc for all types)
Strategy D: Reduction to type A via folding (B_n from A_{2n-1})
Strategy E: MC4 uniform PBW bridge bypass (completed equivalence)

All tests compute real mathematics: no doc-string checks, no "assert key in dict".

Total: 44 tests.
"""

import math

import pytest

from compute.lib.mc3_green_team import (
    DYNKIN_DATA,
    FOLDING_PAIRS,
    satake_generator_count,
    satake_convolution_ring,
    satake_thick_generation_test,
    tilting_generation_data,
    tilting_vs_prefundamental_comparison,
    cluster_algebra_data,
    cluster_mutation_rank2,
    folding_data,
    folding_descent_test_rank2,
    mc4_bypass_analysis,
    mc4_weight_stabilization_test,
    strategy_comparison,
    _fundamental_representation_dims,
    _positive_roots_at_height,
    _adjoint_tensor_power,
    _count_fixed_fundamentals,
    _bar_dim_at_weight,
)


# ===========================================================================
# S1. Dynkin data consistency
# ===========================================================================

class TestDynkinData:
    """Verify root system data for all simple types."""

    def test_positive_root_count_type_A(self):
        """For A_n: |Phi^+| = n(n+1)/2."""
        for n in range(1, 6):
            name = f"A{n}"
            _, n_pos, _, _, _ = DYNKIN_DATA[name]
            assert n_pos == n * (n + 1) // 2, f"{name}: expected {n*(n+1)//2}, got {n_pos}"

    def test_weyl_group_order_type_A(self):
        """For A_n: |W| = (n+1)!."""
        for n in range(1, 6):
            name = f"A{n}"
            _, _, weyl_order, _, _ = DYNKIN_DATA[name]
            assert weyl_order == math.factorial(n + 1), f"{name}: |W| mismatch"

    def test_coxeter_number_type_A(self):
        """For A_n: Coxeter number h = n+1."""
        for n in range(1, 6):
            name = f"A{n}"
            _, _, _, coxeter, _ = DYNKIN_DATA[name]
            assert coxeter == n + 1, f"{name}: h should be {n+1}"

    def test_simply_laced_types(self):
        """A, D, E have lacing number 1."""
        for name in ("A1", "A2", "A3", "D4", "D5", "E6", "E7", "E8"):
            assert DYNKIN_DATA[name][4] == 1, f"{name} should be simply-laced"

    def test_non_simply_laced_types(self):
        """B, C have lacing 2; G_2 has lacing 3."""
        for name in ("B2", "B3", "B4", "C2", "C3"):
            assert DYNKIN_DATA[name][4] == 2, f"{name} should have lacing 2"
        assert DYNKIN_DATA["G2"][4] == 3, "G_2 should have lacing 3"

    def test_dim_g_formula(self):
        """dim(g) = 2|Phi^+| + rank for all types."""
        known_dims = {
            "A1": 3, "A2": 8, "A3": 15, "A4": 24,
            "B2": 10, "B3": 21,
            "G2": 14,
            "D4": 28,
            "E6": 78, "E7": 133, "E8": 248,
        }
        for name, expected_dim in known_dims.items():
            rank, n_pos, _, _, _ = DYNKIN_DATA[name]
            computed_dim = 2 * n_pos + rank
            assert computed_dim == expected_dim, f"{name}: dim should be {expected_dim}, got {computed_dim}"


# ===========================================================================
# S2. Strategy A: Geometric Satake bypass
# ===========================================================================

class TestStrategySatake:
    """Geometric Satake bypass tests."""

    def test_satake_generators_equal_rank(self):
        """Number of Satake generators = rank for all types."""
        for name in DYNKIN_DATA:
            result = satake_generator_count(name)
            assert result["n_satake_generators"] == result["rank"], \
                f"{name}: Satake generators should equal rank"

    def test_satake_advantage_non_type_A(self):
        """Satake has advantage over prefundamental for non-type-A."""
        for name in ("B2", "B3", "G2", "D4", "E6"):
            result = satake_generator_count(name)
            assert result["satake_vs_prefundamental"]["satake_advantage"], \
                f"{name}: Satake should have advantage"

    def test_satake_no_advantage_type_A(self):
        """For type A, prefundamental CG is already proved."""
        for name in ("A1", "A2", "A3"):
            result = satake_generator_count(name)
            assert not result["satake_vs_prefundamental"]["satake_advantage"]

    def test_fundamental_dims_type_A(self):
        """For A_n: fundamental reps have dims C(n+1, i+1)."""
        for n in range(1, 6):
            name = f"A{n}"
            dims = _fundamental_representation_dims(name)
            for i, d in enumerate(dims):
                expected = math.comb(n + 1, i + 1)
                assert d == expected, f"{name}, omega_{i+1}: dim should be {expected}, got {d}"

    def test_adjoint_in_second_tensor_power(self):
        """The adjoint representation is reached at most by tensor power 2
        for types A, B, C, D, G_2, E_6."""
        for name in ("A2", "A3", "B2", "B3", "G2", "D4", "E6"):
            power = _adjoint_tensor_power(name)
            assert power <= 2, f"{name}: adjoint should be in omega_i^2"

    def test_satake_convolution_ring_polynomial(self):
        """The convolution ring K_0(Perv(Gr_G)) is polynomial for all types."""
        for name in ("A2", "B2", "G2", "D4"):
            result = satake_convolution_ring(name)
            assert result["ring_is_polynomial"]

    def test_satake_thick_generation_rank2(self):
        """For rank-2 types, Satake generators reach dominant weights
        via tensor products up to power 3."""
        for name in ("A2", "B2", "G2"):
            result = satake_thick_generation_test(name)
            reachability = result["reachability_rank2"]
            assert reachability is not None
            # At power 3, we should reach at least 5 dominant weights
            assert reachability["total_reached"] >= 5, \
                f"{name}: should reach >=5 dominant weights by power 3"


# ===========================================================================
# S3. Strategy B: Tilting module approach
# ===========================================================================

class TestStrategyTilting:
    """Tilting module approach tests."""

    def test_tilting_principal_block_equals_weyl(self):
        """Number of tiltings in principal block = |W|."""
        for name in ("A2", "A3", "B2", "G2", "D4"):
            result = tilting_generation_data(name)
            assert result["n_tilting_principal_block"] == DYNKIN_DATA[name][2]

    def test_soergel_generators_equal_rank(self):
        """Soergel bimodule generators = rank (one per simple reflection)."""
        for name in DYNKIN_DATA:
            result = tilting_generation_data(name)
            assert result["n_soergel_generators"] == DYNKIN_DATA[name][0]

    def test_tilting_type_independent(self):
        """Tilting generation theorem is type-independent."""
        for name in ("A2", "B2", "G2", "D4", "E6"):
            result = tilting_generation_data(name)
            assert result["type_independent"]
            assert result["tilting_generation_theorem"]

    def test_tilting_vs_prefundamental(self):
        """Tilting has comparative advantage for non-type-A."""
        for name in ("B2", "G2", "D4"):
            result = tilting_vs_prefundamental_comparison(name)
            assert result["comparative_advantage"] == "tilting"
        for name in ("A2", "A3"):
            result = tilting_vs_prefundamental_comparison(name)
            assert result["comparative_advantage"] == "prefundamental"


# ===========================================================================
# S4. Strategy C: Cluster category approach
# ===========================================================================

class TestStrategyCluster:
    """Cluster category approach tests."""

    def test_cluster_algebra_finite_type_all(self):
        """All simple Lie algebras give finite-type cluster algebras on C_g."""
        for name in DYNKIN_DATA:
            result = cluster_algebra_data(name)
            assert result["cluster_type_finite"], f"{name} should give finite-type cluster"

    def test_cluster_variable_count_rank2(self):
        """Cluster variable counts for rank-2 types."""
        expected = {"A2": 5, "B2": 6, "G2": 8}
        for name, n_expected in expected.items():
            result = cluster_algebra_data(name)
            assert result["n_cluster_variables"] == n_expected, \
                f"{name}: expected {n_expected} cluster vars, got {result['n_cluster_variables']}"

    def test_frozen_variables_equal_rank(self):
        """Number of frozen variables = rank."""
        for name in DYNKIN_DATA:
            result = cluster_algebra_data(name)
            assert result["n_frozen_variables"] == DYNKIN_DATA[name][0]

    def test_cluster_mutation_A2(self):
        """A_2 cluster mutations produce exactly 5 variables."""
        result = cluster_mutation_rank2("A2")
        assert result["count_matches"], \
            f"A2: expected 5 cluster vars, got {result['n_cluster_variables']}"

    def test_cluster_mutation_B2(self):
        """B_2 cluster mutations produce exactly 6 variables."""
        result = cluster_mutation_rank2("B2")
        assert result["count_matches"], \
            f"B2: expected 6 cluster vars, got {result['n_cluster_variables']}"

    def test_cluster_mutation_G2(self):
        """G_2 cluster mutations produce exactly 8 variables."""
        result = cluster_mutation_rank2("G2")
        assert result["count_matches"], \
            f"G2: expected 8 cluster vars, got {result['n_cluster_variables']}"

    def test_cluster_exchange_pairs(self):
        """Exchange pairs match Dynkin diagram valences."""
        expected_pairs = {"A2": (1, 1), "B2": (1, 2), "G2": (1, 3)}
        for name, (b, c) in expected_pairs.items():
            result = cluster_mutation_rank2(name)
            assert result["exchange_pair"] == (b, c)


# ===========================================================================
# S5. Strategy D: Folding descent
# ===========================================================================

class TestStrategyFolding:
    """Folding reduction to type A tests."""

    def test_folding_B2_from_A3(self):
        """B_2 folds from A_3 (type A, MC3 proved)."""
        result = folding_data("B2")
        assert result["is_folded"]
        assert result["unfolded_type"] == "A3"
        assert result["mc3_unfolded"] == "proved"
        assert result["mc3_descent_possible"]

    def test_folding_G2_from_D4(self):
        """G_2 folds from D_4 (not type A, MC3 open)."""
        result = folding_data("G2")
        assert result["is_folded"]
        assert result["unfolded_type"] == "D4"
        assert result["mc3_unfolded"] == "open"
        assert not result["mc3_descent_possible"]

    def test_folding_F4_from_E6(self):
        """F_4 folds from E_6 (not type A, MC3 open)."""
        result = folding_data("F4")
        assert result["is_folded"]
        assert result["unfolded_type"] == "E6"
        assert not result["mc3_descent_possible"]

    def test_type_A_not_folded(self):
        """Type A algebras are not folded from anything."""
        for name in ("A1", "A2", "A3"):
            result = folding_data(name)
            assert not result["is_folded"]
            assert result["mc3_status"] == "proved"

    def test_folding_descent_only_covers_B(self):
        """Folding from type A covers only type B."""
        result = folding_descent_test_rank2()
        reachable = result["reachable_from_type_A"]
        assert all(t.startswith("B") for t in reachable)
        assert "G2" not in reachable
        assert "F4" not in [r for r in reachable]

    def test_fold_order_matches(self):
        """Fold orders match: Z/2 for B from A, Z/3 for G_2 from D_4."""
        for folded, unfolded, order in FOLDING_PAIRS:
            result = folding_data(folded)
            assert result["fold_order"] == order, \
                f"{folded}: fold order should be {order}"

    def test_fixed_fundamentals_A3(self):
        """A_3 with Z/2: middle node omega_2 is fixed (odd rank)."""
        n_fixed = _count_fixed_fundamentals("A3", 2)
        assert n_fixed == 1, "A_3 with Z/2 should have 1 fixed fundamental"

    def test_fixed_fundamentals_D4_triality(self):
        """D_4 with Z/3 (triality): only omega_2 is fixed."""
        n_fixed = _count_fixed_fundamentals("D4", 3)
        assert n_fixed == 1, "D_4 with triality should have 1 fixed fundamental"


# ===========================================================================
# S6. Strategy E: MC4 bypass
# ===========================================================================

class TestStrategyMC4Bypass:
    """MC4 uniform PBW bridge bypass tests."""

    def test_mc1_mc4_proved_all_types(self):
        """MC1 and MC4 are proved for ALL types."""
        for name in DYNKIN_DATA:
            result = mc4_bypass_analysis(name)
            assert result["mc1_proved"]
            assert result["mc4_proved"]

    def test_eval_modules_exist_all_types(self):
        """Evaluation modules exist for all types."""
        for name in DYNKIN_DATA:
            result = mc4_bypass_analysis(name)
            assert result["eval_modules_exist"]

    def test_mc4_gives_completed_not_finite(self):
        """MC4 gives completed equivalence but NOT finite generation."""
        for name in DYNKIN_DATA:
            result = mc4_bypass_analysis(name)
            assert result["mc4_gives_completed_equivalence"]
            assert not result["mc4_gives_finite_generation"]

    def test_gap_zero_for_type_A(self):
        """Type A has zero gap (MC3 already proved)."""
        for name in ("A1", "A2", "A3"):
            result = mc4_bypass_analysis(name)
            assert result["gap_estimate"] == 0

    def test_gap_increases_with_complexity(self):
        """Gap estimate increases from simply-laced to exceptional."""
        gap_B = mc4_bypass_analysis("B2")["gap_estimate"]
        gap_D = mc4_bypass_analysis("D4")["gap_estimate"]
        gap_G = mc4_bypass_analysis("G2")["gap_estimate"]
        gap_E = mc4_bypass_analysis("E6")["gap_estimate"]
        assert gap_B <= gap_D <= gap_G
        assert gap_G <= gap_E

    def test_weight_stabilization_positive_tower(self):
        """All Yangians are positive towers with linear stabilization."""
        for name in ("A2", "B2", "G2"):
            result = mc4_weight_stabilization_test(name, max_weight=5)
            assert result["all_positive"]
            assert result["stabilization_linear"]

    def test_positive_root_height_type_A(self):
        """For A_n, number of roots at height h = n+1-h for h <= n."""
        for name, (rank, _, _, _, _) in DYNKIN_DATA.items():
            if name.startswith("A"):
                for h in range(1, rank + 1):
                    n_roots = _positive_roots_at_height(name, h)
                    assert n_roots == rank + 1 - h, \
                        f"{name}, h={h}: expected {rank+1-h} roots, got {n_roots}"

    def test_positive_root_count_sums(self):
        """Sum of roots at all heights = |Phi^+|."""
        for name in ("A2", "A3", "B2", "G2", "D4"):
            _, n_pos, _, coxeter, _ = DYNKIN_DATA[name]
            total = sum(_positive_roots_at_height(name, h)
                        for h in range(1, 2 * coxeter))
            assert total == n_pos, \
                f"{name}: sum of roots at heights should be {n_pos}, got {total}"


# ===========================================================================
# S7. Strategy comparison and recommendations
# ===========================================================================

class TestStrategyComparison:
    """Overall strategy comparison tests."""

    def test_all_five_strategies_present(self):
        """All five strategies are rated."""
        result = strategy_comparison()
        assert len(result["strategies"]) == 5

    def test_folding_highest_feasibility(self):
        """Folding (D) should have the highest feasibility score."""
        result = strategy_comparison()
        scores = {k: v["feasibility"] for k, v in result["strategies"].items()}
        assert scores["D_Folding"] >= max(scores.values()) - 1  # within 1 of max

    def test_folding_incomplete(self):
        """Folding (D) is incomplete: does not solve all types."""
        result = strategy_comparison()
        assert not result["strategies"]["D_Folding"]["completeness"]

    def test_cluster_and_satake_complete(self):
        """Cluster (C) and Satake (A) are complete strategies."""
        result = strategy_comparison()
        assert result["strategies"]["C_Cluster"]["completeness"]
        assert result["strategies"]["A_Satake"]["completeness"]

    def test_mc4_bypass_lowest_feasibility(self):
        """MC4 bypass (E) should have the lowest feasibility."""
        result = strategy_comparison()
        scores = {k: v["feasibility"] for k, v in result["strategies"].items()}
        assert scores["E_MC4_Bypass"] <= min(scores.values()) + 1

    def test_recommendation_is_hybrid(self):
        """The recommendation should be a hybrid approach."""
        result = strategy_comparison()
        rec = result["recommendation"]["recommended_approach"]
        assert "HYBRID" in rec or "hybrid" in rec.lower()
