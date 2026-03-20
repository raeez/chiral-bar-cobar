"""RED TEAM tests for conj:mc3-arbitrary-type.

Stress-tests every gap in the path from type-A MC3 proof to arbitrary type.
Target: find real failure points, not strawmen.

Attack vectors tested:
  1. Root system enumeration consistency (all types)
  2. Multi-partition obstruction scaling (K_0 -> module gap)
  3. Minuscule representation scarcity
  4. Short root complications (non-simply-laced types)
  5. Spinor representation obstructions (B_n, D_n)
  6. Exceptional type hardness
  7. D_n spinor parity / outer automorphism
  8. Hernandez-Jimbo construction uniformity
  9. Escape route viability
  10. Cross-type CG obstruction comparison
  11. Type-by-type feasibility
  12. Comprehensive vulnerability assessment

References:
  - thm:mc3-type-a-resolution (yangians_computations.tex)
  - conj:mc3-arbitrary-type (yangians_computations.tex)
  - MC3-RED adversarial swarm results (2026-03-17)
"""

import math
import pytest

from compute.lib.mc3_red_team import (
    CARTAN_MATRICES,
    DYNKIN_DATA,
    FUNDAMENTAL_DIMS,
    FOLDING_DATA,
    enumerate_positive_roots,
    _multi_partition_dp,
    obstruction_dimension_by_type,
    minuscule_analysis,
    short_root_analysis,
    spinor_obstruction_analysis,
    exceptional_hardness_ranking,
    dn_spinor_parity_obstruction,
    hernandez_jimbo_uniformity_analysis,
    escape_route_analysis,
    comprehensive_vulnerability_report,
    cg_obstruction_comparison,
    type_by_type_feasibility,
)


# ============================================================================
# S1. Root system consistency
# ============================================================================

class TestRootSystemEnumeration:
    """Verify positive root counts match Dynkin classification."""

    @pytest.mark.parametrize("type_name,expected_count", [
        ("A1", 1),
        ("A2", 3),
        ("A3", 6),
        ("A4", 10),
        ("B2", 4),
        ("B3", 9),
        ("C2", 4),
        ("C3", 9),
        ("D4", 12),
        ("D5", 20),
        ("G2", 6),
        ("F4", 24),
        ("E6", 36),
    ])
    def test_positive_root_count(self, type_name, expected_count):
        """Number of positive roots matches classification data."""
        roots = enumerate_positive_roots(type_name)
        assert len(roots) == expected_count, (
            f"{type_name}: got {len(roots)} positive roots, expected {expected_count}"
        )

    def test_A2_positive_roots(self):
        """A_2 has roots alpha_1, alpha_2, alpha_1+alpha_2."""
        roots = enumerate_positive_roots("A2")
        assert (1, 0) in roots  # alpha_1
        assert (0, 1) in roots  # alpha_2
        assert (1, 1) in roots  # alpha_1 + alpha_2

    def test_B2_positive_roots(self):
        """B_2 has 4 positive roots: alpha_1, alpha_2, alpha_1+alpha_2, 2*alpha_1+alpha_2."""
        roots = enumerate_positive_roots("B2")
        assert (1, 0) in roots  # alpha_1 (short)
        assert (0, 1) in roots  # alpha_2 (long)
        assert (1, 1) in roots  # alpha_1 + alpha_2
        assert (2, 1) in roots  # 2*alpha_1 + alpha_2 (long)

    def test_G2_positive_roots(self):
        """G_2 has 6 positive roots."""
        roots = enumerate_positive_roots("G2")
        assert len(roots) == 6
        assert (1, 0) in roots  # alpha_1 (short)
        assert (0, 1) in roots  # alpha_2 (long)
        assert (3, 1) in roots  # 3*alpha_1 + alpha_2
        assert (3, 2) in roots  # 3*alpha_1 + 2*alpha_2 (highest root)

    def test_D4_positive_roots_triality(self):
        """D_4 has 12 positive roots. Triality permutes nodes 1,3,4."""
        roots = enumerate_positive_roots("D4")
        assert len(roots) == 12

    def test_F4_positive_roots(self):
        """F_4 has exactly 24 positive roots."""
        roots = enumerate_positive_roots("F4")
        assert len(roots) == 24


# ============================================================================
# S2. Multi-partition obstruction scaling
# ============================================================================

class TestMultiPartitionObstruction:
    """Test that K_0 -> module gap grows with rank."""

    def test_single_partition_base_cases(self):
        """p_1(k) = partition number p(k)."""
        from compute.lib.utils import partition_number
        for k in range(1, 15):
            assert _multi_partition_dp(1, k) == partition_number(k)

    def test_multi_partition_base(self):
        """p_N(0) = 1 for all N."""
        for N in range(1, 10):
            assert _multi_partition_dp(N, 0) == 1

    def test_multi_partition_k1(self):
        """p_N(1) = N for all N (one box, N colors)."""
        for N in range(1, 8):
            assert _multi_partition_dp(N, 1) == N

    def test_obstruction_grows_with_rank(self):
        """delta_N(k) = p_N(k) - 1 grows with N for fixed k >= 2."""
        k = 5
        prev = 0
        for N in range(1, 6):
            delta = _multi_partition_dp(N, k) - 1
            assert delta >= prev, (
                f"delta_{N}({k}) = {delta} < delta_{N-1}({k}) = {prev}"
            )
            prev = delta

    def test_obstruction_E8_node(self):
        """E_8 has up to 120 positive roots. The obstruction at the node
        with the most relevant roots is astronomically large."""
        # E_8 root system
        roots = enumerate_positive_roots("E8")
        assert len(roots) == 120

        # Count relevant roots per node
        rank = 8
        max_rel = 0
        for i in range(rank):
            count = sum(1 for root in roots if root[i] > 0)
            max_rel = max(max_rel, count)

        # The max relevant root count for E_8 should be substantial
        assert max_rel >= 30, (
            f"E_8 max relevant root count is {max_rel}, expected >= 30"
        )

    def test_obstruction_comparison_A2_vs_B2(self):
        """B_2 has more relevant roots per node than A_2, so larger obstruction."""
        a2_roots = enumerate_positive_roots("A2")
        b2_roots = enumerate_positive_roots("B2")

        # A_2: node 0 has 2 relevant roots (alpha_1, alpha_1+alpha_2)
        a2_rel_0 = sum(1 for r in a2_roots if r[0] > 0)
        # B_2: node 0 has relevant roots containing alpha_1
        b2_rel_0 = sum(1 for r in b2_roots if r[0] > 0)

        assert b2_rel_0 >= a2_rel_0, (
            f"B_2 node 0 has {b2_rel_0} relevant roots, "
            f"A_2 node 0 has {a2_rel_0}"
        )


# ============================================================================
# S3. Minuscule representation analysis
# ============================================================================

class TestMinusculeScarcity:
    """Test that minuscule scarcity correlates with MC3 difficulty."""

    def test_type_A_all_minuscule(self):
        """Type A_n: all fundamentals are minuscule."""
        for t in ["A1", "A2", "A3", "A4"]:
            result = minuscule_analysis(t)
            assert result["n_minuscule"] == result["rank"]
            assert result["generation_strategy"] == "EASY"

    def test_E8_no_minuscule(self):
        """E_8 has ZERO minuscule representations — hardest case."""
        result = minuscule_analysis("E8")
        assert result["n_minuscule"] == 0
        assert result["generation_strategy"] == "VERY_HARD"

    def test_F4_no_minuscule(self):
        """F_4 has ZERO minuscule representations."""
        result = minuscule_analysis("F4")
        assert result["n_minuscule"] == 0
        assert result["generation_strategy"] == "VERY_HARD"

    def test_G2_no_minuscule(self):
        """G_2 has ZERO minuscule representations."""
        result = minuscule_analysis("G2")
        assert result["n_minuscule"] == 0
        assert result["generation_strategy"] == "VERY_HARD"

    def test_D4_three_minuscule(self):
        """D_4 has 3 minuscule reps (vector + 2 half-spins)."""
        result = minuscule_analysis("D4")
        assert result["n_minuscule"] == 3

    def test_E6_two_minuscule(self):
        """E_6 has 2 minuscule reps (27-dim representations)."""
        result = minuscule_analysis("E6")
        assert result["n_minuscule"] == 2

    def test_E7_one_minuscule(self):
        """E_7 has only 1 minuscule rep (56-dim)."""
        result = minuscule_analysis("E7")
        assert result["n_minuscule"] == 1

    def test_B_n_one_minuscule(self):
        """B_n has only 1 minuscule (the vector rep)."""
        for t in ["B2", "B3"]:
            result = minuscule_analysis(t)
            assert result["n_minuscule"] == 1


# ============================================================================
# S4. Short root obstruction
# ============================================================================

class TestShortRootObstruction:
    """Test non-simply-laced complications."""

    def test_simply_laced_no_obstruction(self):
        """Simply-laced types have no short-root obstruction."""
        for t in ["A2", "A3", "D4", "E6"]:
            result = short_root_analysis(t)
            assert result["simply_laced"] is True

    def test_B2_asymmetric_cartan(self):
        """B_2 Cartan matrix has A_{12} = -1, A_{21} = -2 (asymmetric)."""
        result = short_root_analysis("B2")
        assert result["simply_laced"] is False
        assert len(result["asymmetric_cartan_entries"]) > 0

    def test_G2_extreme_asymmetry(self):
        """G_2 has Cartan entry -3 (most extreme asymmetry)."""
        result = short_root_analysis("G2")
        assert result["simply_laced"] is False
        # Check for the -3 entry
        entries = result["asymmetric_cartan_entries"]
        has_minus_3 = any(e["A_ij"] == -3 or e["A_ji"] == -3 for e in entries)
        assert has_minus_3, "G_2 should have Cartan entry -3"

    def test_F4_folding_from_E6(self):
        """F_4 is obtained by folding from E_6."""
        result = short_root_analysis("F4")
        assert result["folding_parent"] == "E6"

    def test_G2_folding_from_D4(self):
        """G_2 is obtained by folding from D_4 via triality (Z/3)."""
        result = short_root_analysis("G2")
        assert result["folding_parent"] == "D4"
        assert result["fold_automorphism"] == "Z/3"


# ============================================================================
# S5. Spinor obstruction
# ============================================================================

class TestSpinorObstruction:
    """Test spinor representation complications for B_n, D_n."""

    def test_B2_has_spinor(self):
        """B_2 has a spinor representation at node 2."""
        result = spinor_obstruction_analysis("B2")
        assert result["has_spinor"] is True

    def test_D4_has_two_half_spinors(self):
        """D_4 has two half-spinor reps at nodes 3,4."""
        result = spinor_obstruction_analysis("D4")
        assert result["has_spinor"] is True
        assert len(result["spinor_nodes"]) == 2

    def test_A_types_no_spinor(self):
        """Type A has no spinor representations."""
        for t in ["A1", "A2", "A3", "A4"]:
            result = spinor_obstruction_analysis(t)
            assert result["has_spinor"] is False

    def test_E_types_no_spinor(self):
        """E types have no spinor representations (they are simply-laced but not D)."""
        for t in ["E6", "E7", "E8"]:
            result = spinor_obstruction_analysis(t)
            assert result["has_spinor"] is False

    def test_spinor_dim_exponential(self):
        """Spinor dimension grows exponentially with rank."""
        for n in [4, 5]:
            result = dn_spinor_parity_obstruction(n)
            assert result["spin_dim"] == 2 ** (n - 1)


# ============================================================================
# S6. D_n spinor parity and outer automorphism
# ============================================================================

class TestDnSpinorParity:
    """Test the outer automorphism / spinor parity complications for D_n."""

    def test_d4_triality(self):
        """D_4 has S_3 triality (outer automorphism order 6)."""
        result = dn_spinor_parity_obstruction(4)
        assert result["outer_automorphism_order"] == 6

    def test_d5_z2_outer(self):
        """D_5 has Z/2 outer automorphism."""
        result = dn_spinor_parity_obstruction(5)
        assert result["outer_automorphism_order"] == 2

    def test_dn_spinor_minuscule(self):
        """D_n half-spinors are always minuscule — this is FAVORABLE."""
        for n in [4, 5, 6, 7]:
            result = dn_spinor_parity_obstruction(n)
            assert result["spin_is_minuscule"] is True
            assert result["obstruction_severity"] == "LOW"

    def test_dn_real_obstruction_is_adjoint(self):
        """The REAL obstruction for D_n is the adjoint rep (non-minuscule)."""
        for n in [4, 5, 6]:
            result = dn_spinor_parity_obstruction(n)
            expected_adj_dim = n * (2 * n - 1)
            assert result["adjoint_dim"] == expected_adj_dim


# ============================================================================
# S7. Exceptional type hardness ranking
# ============================================================================

class TestExceptionalHardness:
    """Test that the hardness ranking is correct."""

    def test_E8_is_hardest(self):
        """E_8 should be the hardest type overall."""
        ranking = exceptional_hardness_ranking()
        assert ranking["hardest_type"] == "E8"

    def test_A_types_easiest(self):
        """Type A should have the lowest hardness scores."""
        ranking = exceptional_hardness_ranking()
        ordered = [t for t, _ in ranking["ranking"]]
        # A1 should be first
        assert ordered[0] == "A1"

    def test_simply_laced_easier_than_non(self):
        """Within the same rank, simply-laced types are easier."""
        ranking = exceptional_hardness_ranking()
        details = ranking["details"]
        # A2 vs B2 vs G2 (all rank 2)
        assert details["A2"]["total_score"] < details["B2"]["total_score"]
        assert details["A2"]["total_score"] < details["G2"]["total_score"]

    def test_E8_score_much_larger_than_A4(self):
        """E_8 hardness score should be much larger than A_4."""
        ranking = exceptional_hardness_ranking()
        details = ranking["details"]
        assert details["E8"]["total_score"] > 3 * details["A4"]["total_score"]


# ============================================================================
# S8. Hernandez-Jimbo uniformity
# ============================================================================

class TestHJUniformity:
    """Test uniformity of the Hernandez-Jimbo construction."""

    def test_all_types_covered(self):
        """HJ analysis should cover all Dynkin types."""
        analysis = hernandez_jimbo_uniformity_analysis()
        for t in DYNKIN_DATA:
            assert t in analysis

    def test_type_A_good_uniformity(self):
        """Type A should have GOOD uniformity."""
        analysis = hernandez_jimbo_uniformity_analysis()
        for t in ["A1", "A2", "A3", "A4"]:
            assert analysis[t]["uniformity"] == "GOOD"

    def test_non_simply_laced_weak_uniformity(self):
        """Non-simply-laced types should have WEAK uniformity (folding)."""
        analysis = hernandez_jimbo_uniformity_analysis()
        for t in ["B2", "B3", "C2", "C3", "G2", "F4"]:
            assert analysis[t]["uniformity"] == "WEAK"

    def test_exceptional_moderate_uniformity(self):
        """Exceptional simply-laced types (E) should have MODERATE uniformity."""
        analysis = hernandez_jimbo_uniformity_analysis()
        for t in ["E6", "E7", "E8"]:
            assert analysis[t]["uniformity"] == "MODERATE"


# ============================================================================
# S9. Escape route viability
# ============================================================================

class TestEscapeRoutes:
    """Test alternative proof strategies."""

    def test_four_escape_routes_identified(self):
        """At least 4 escape routes should be identified."""
        routes = escape_route_analysis()
        assert len(routes["routes"]) >= 4

    def test_coulomb_branch_best(self):
        """Coulomb branch should be the most promising escape route."""
        routes = escape_route_analysis()
        assert routes["best_escape"] == "Coulomb_branch"

    def test_rtt_low_viability(self):
        """RTT approach has low viability for bypassing CG."""
        routes = escape_route_analysis()
        assert routes["routes"]["RTT_realization"]["viability"] == "LOW for bypassing CG"

    def test_maulik_okounkov_not_for_bcfg(self):
        """Maulik-Okounkov approach does NOT cover BCFG types."""
        routes = escape_route_analysis()
        mo = routes["routes"]["Maulik_Okounkov"]
        assert "NOT non-simply-laced" in mo["coverage"]


# ============================================================================
# S10. CG obstruction comparison across types
# ============================================================================

class TestCGObstructionComparison:
    """Cross-type quantitative CG obstruction comparison."""

    def test_comparison_includes_all_major_types(self):
        """Comparison should include A, B, C, D, G, F, E types."""
        result = cg_obstruction_comparison(max_k=10)
        types = result["types_compared"]
        assert "A2" in types
        assert "B2" in types
        assert "D4" in types
        assert "G2" in types
        assert "F4" in types
        assert "E6" in types

    def test_obstruction_nonneg(self):
        """Obstruction delta(k) = p_N(k) - 1 >= 0 for all k >= 1."""
        result = cg_obstruction_comparison(max_k=10)
        for t, data in result["results"].items():
            for k, delta in data["max_deltas"].items():
                assert delta >= 0, f"{t}: delta({k}) = {delta} < 0"

    def test_higher_rank_worse_obstruction(self):
        """E_6 should have worse obstruction than A_2 at k >= 3."""
        result = cg_obstruction_comparison(max_k=10)
        a2 = result["results"]["A2"]
        e6 = result["results"]["E6"]
        for k in range(3, 11):
            assert e6["max_deltas"][k] >= a2["max_deltas"][k], (
                f"E_6 delta({k}) = {e6['max_deltas'][k]} < "
                f"A_2 delta({k}) = {a2['max_deltas'][k]}"
            )


# ============================================================================
# S11. Comprehensive vulnerability report
# ============================================================================

class TestVulnerabilityReport:
    """Test the comprehensive vulnerability assessment."""

    def test_report_completeness(self):
        """Report should identify at least 6 vulnerabilities."""
        report = comprehensive_vulnerability_report()
        assert report["n_vulnerabilities"] >= 6

    def test_critical_vulnerabilities_identified(self):
        """At least 2 CRITICAL vulnerabilities should be identified."""
        report = comprehensive_vulnerability_report()
        assert report["n_critical"] >= 2

    def test_E8_identified_as_hardest(self):
        """E_8 should be identified as the hardest type."""
        report = comprehensive_vulnerability_report()
        assert report["hardest_type"] == "E8"

    def test_F4_identified_as_second_hardest(self):
        """F_4 should be identified as the second hardest type."""
        report = comprehensive_vulnerability_report()
        assert report["second_hardest_type"] == "F4"

    def test_proweyl_and_fg_low_severity(self):
        """Pro-Weyl and FG completion should be LOW severity (rank-independent)."""
        report = comprehensive_vulnerability_report()
        for v in report["vulnerabilities"]:
            if "Pro-Weyl" in v["description"] or "FG" in v["description"]:
                assert v["severity"] == "LOW"


# ============================================================================
# S12. Type-by-type feasibility
# ============================================================================

class TestFeasibility:
    """Test the type-by-type feasibility assessment."""

    def test_type_A_proved(self):
        """Type A should be graded A and marked PROVED."""
        result = type_by_type_feasibility()
        assert result["assessments"]["A_n"]["grade"] == "A"
        assert "PROVED" in result["assessments"]["A_n"]["status"]

    def test_E8_F4_hardest(self):
        """E_8 and F_4 should be the hardest (grade D)."""
        result = type_by_type_feasibility()
        assert result["assessments"]["E_8"]["grade"] == "D"
        assert result["assessments"]["F_4"]["grade"] == "D"

    def test_E8_F4_may_need_new_methods(self):
        """E_8 and F_4 should be in the 'may require new methods' list."""
        result = type_by_type_feasibility()
        assert "E_8" in result["may_require_new_methods"]
        assert "F_4" in result["may_require_new_methods"]

    def test_D_expected_straightforward(self):
        """D_n should be expected straightforward (simply-laced, minuscule spinors)."""
        result = type_by_type_feasibility()
        assert "D_n" in result["expected_straightforward"]


# ============================================================================
# S13. Specific quantitative attacks
# ============================================================================

class TestQuantitativeAttacks:
    """Specific quantitative computations exposing gaps."""

    def test_e8_relevant_roots_per_node(self):
        """E_8: compute relevant roots per node and verify high counts.

        E_8 has 120 positive roots. Even the node with the FEWEST relevant
        roots has far more than any type-A node, making the K_0-to-module
        obstruction much larger.

        RED TEAM FINDING: E_8 relevant root counts are surprisingly UNIFORM
        (range 57-106), meaning ALL nodes are hard simultaneously.
        There is no easy node to bootstrap from.
        """
        roots = enumerate_positive_roots("E8")
        rank = 8
        rel_counts = []
        for i in range(rank):
            count = sum(1 for r in roots if r[i] > 0)
            rel_counts.append(count)

        # E_8: even the MIN relevant root count is very high
        assert min(rel_counts) >= 50, (
            f"E_8 min relevant root count is {min(rel_counts)}, expected >= 50"
        )
        # E_8: max relevant root count >= 100
        assert max(rel_counts) >= 100, (
            f"E_8 max relevant root count is {max(rel_counts)}, expected >= 100"
        )
        # KEY FINDING: counts are surprisingly uniform — all nodes are hard
        ratio = max(rel_counts) / min(rel_counts)
        assert ratio < 2.0, (
            f"E_8 relevant root counts are unexpectedly non-uniform: "
            f"ratio = {ratio:.2f}, counts = {rel_counts}"
        )

    def test_f4_double_obstruction_quantified(self):
        """F_4: quantify the double obstruction (non-simply-laced + no minuscule)."""
        min_result = minuscule_analysis("F4")
        short_result = short_root_analysis("F4")

        assert min_result["n_minuscule"] == 0
        assert short_result["simply_laced"] is False
        assert len(short_result["short_nodes"]) >= 2

    def test_obstruction_at_k10_for_rank2_types(self):
        """Compare obstruction at k=10 for all rank-2 types."""
        types = ["A2", "B2", "C2", "G2"]
        deltas = {}
        for t in types:
            roots = enumerate_positive_roots(t)
            rank = DYNKIN_DATA[t]["rank"]
            max_rel = 0
            for i in range(rank):
                count = sum(1 for r in roots if r[i] > 0)
                max_rel = max(max_rel, count)
            delta = _multi_partition_dp(max_rel, 10) - 1
            deltas[t] = delta

        # G_2 should have the largest obstruction (most roots per node)
        assert deltas["G2"] >= deltas["A2"], (
            f"G_2 delta = {deltas['G2']}, A_2 delta = {deltas['A2']}"
        )

    def test_folding_data_consistency(self):
        """Verify folding relations are consistent with root system data.

        RED TEAM FINDING: The folding parents (A5, D3, D_{n+1}) for some
        types are NOT in our database. This highlights that the folding
        construction requires LARGER parent types that we have not
        computed explicitly. For the MC3 extension, this means the
        categorical CG for BCFG depends on results about the parent
        type that may be harder to verify.
        """
        # Known parents in database
        known_parents = set(CARTAN_MATRICES.keys()) | {"D3", "A5", "A7", "D6"}

        for child, data in FOLDING_DATA.items():
            parent = data["parent"]
            # Child must be non-simply-laced
            assert DYNKIN_DATA[child]["simply_laced"] is False, (
                f"Folded type {child} should be non-simply-laced"
            )
            # Parent must be simply-laced (folding goes simply-laced -> non)
            # We check that the parent type name starts with A/D/E
            assert parent[0] in "ADE", (
                f"{child} folding parent {parent} should be simply-laced (ADE)"
            )

    def test_minuscule_count_monotone_in_type_A(self):
        """In type A_r, n_minuscule = r (all fundamentals minuscule)."""
        for t in ["A1", "A2", "A3", "A4"]:
            rank = DYNKIN_DATA[t]["rank"]
            n_min = DYNKIN_DATA[t]["n_minuscule"]
            assert n_min == rank

    def test_e7_single_minuscule_insufficient(self):
        """E_7 has only 1 minuscule out of 7 fundamentals — generation is hard."""
        result = minuscule_analysis("E7")
        assert result["n_minuscule"] == 1
        assert result["rank"] == 7
        # More than 5/7 of fundamentals are non-minuscule
        assert result["rank"] - result["n_minuscule"] >= 6
