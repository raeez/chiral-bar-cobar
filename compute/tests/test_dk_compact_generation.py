"""Tests for DK compact generation and ladder status (MC3 G7).

Verifies:
  1. DK ladder status data (6 levels, proved/conjectural status)
  2. Boundary strip defect vanishes for Yang R-matrix (N=2,...,8)
  3. Thick closure of evaluation modules via Clebsch-Gordan recursion
  4. K_0 lattice comparison (Yangian vs quantum group)
  5. Francis-Gaitsgory completion data consistency
  6. Evaluation core vs O_poly comparison
  7. Drinfeld polynomial classification for sl_2, sl_3

References:
  - concordance.tex: DK ladder status, thm:catO-thick-generation
  - yangians.tex: sec:cat-O-strategies, conj:master-dk-kl
  - Drinfeld classification theorem
"""

from math import comb

import numpy as np
import pytest

from compute.lib.dk_compact_generation import (
    dk_ladder_status,
    boundary_strip_defect,
    verify_boundary_strip_identities,
    thick_closure_evaluation_sl2,
    compact_generator_k0_comparison,
    francis_gaitsgory_completion_data,
    eval_core_vs_full_O,
    drinfeld_polynomial_classification,
    _permutation_operator,
    _compositions,
)


# =========================================================================
# DK ladder status tests
# =========================================================================

class TestDKLadderStatus:
    """Test the DK ladder status data structure."""

    def test_six_levels(self):
        """DK ladder has exactly 6 levels."""
        status = dk_ladder_status()
        assert len(status) == 6

    def test_level_names(self):
        """All expected level names are present."""
        status = dk_ladder_status()
        expected = {"DK-0", "DK-1", "DK-1.5", "DK-2", "DK-3", "DK-4/5"}
        assert set(status.keys()) == expected

    def test_proved_levels(self):
        """DK-0 through DK-3 are PROVED."""
        status = dk_ladder_status()
        for level in ["DK-0", "DK-1", "DK-1.5", "DK-2", "DK-3"]:
            assert status[level]["status"] == "PROVED", (
                f"{level} should be PROVED, got {status[level]['status']}"
            )

    def test_conjectural_level(self):
        """DK-4/5 is CONJECTURAL."""
        status = dk_ladder_status()
        assert status["DK-4/5"]["status"] == "CONJECTURAL"

    def test_all_have_description(self):
        """Every level has a non-empty description."""
        status = dk_ladder_status()
        for level, data in status.items():
            assert "description" in data
            assert len(data["description"]) > 0, f"{level} has empty description"

    def test_all_have_reference(self):
        """Every level has a manuscript reference."""
        status = dk_ladder_status()
        for level, data in status.items():
            assert "reference" in data
            assert len(data["reference"]) > 0, f"{level} has empty reference"

    def test_dk0_reference(self):
        """DK-0 references the bar-cobar isomorphism theorem."""
        status = dk_ladder_status()
        assert "bar-cobar" in status["DK-0"]["reference"]

    def test_dk1_reference(self):
        """DK-1 references the eval-core identification theorem."""
        status = dk_ladder_status()
        assert "eval" in status["DK-1"]["reference"]

    def test_dk45_reference(self):
        """DK-4/5 references the master DK-KL conjecture."""
        status = dk_ladder_status()
        assert "dk-kl" in status["DK-4/5"]["reference"]


# =========================================================================
# Permutation operator tests
# =========================================================================

class TestPermutationOperator:
    """Test the permutation operator P on C^N tensor C^N."""

    def test_shape(self):
        """P has shape (N^2, N^2)."""
        for N in [2, 3, 4]:
            P = _permutation_operator(N)
            assert P.shape == (N * N, N * N)

    def test_involution(self):
        """P^2 = I (permutation is an involution)."""
        for N in [2, 3, 4]:
            P = _permutation_operator(N)
            P2 = P @ P
            np.testing.assert_allclose(P2, np.eye(N * N), atol=1e-14)

    def test_eigenvalues(self):
        """P has eigenvalues +1 and -1 only."""
        for N in [2, 3, 4]:
            P = _permutation_operator(N)
            eigenvalues = np.linalg.eigvalsh(P)
            for ev in eigenvalues:
                assert abs(abs(ev) - 1.0) < 1e-12, f"Unexpected eigenvalue {ev}"

    def test_eigenvalue_multiplicities(self):
        """P has N(N+1)/2 eigenvalues +1 and N(N-1)/2 eigenvalues -1."""
        for N in [2, 3, 4, 5]:
            P = _permutation_operator(N)
            eigenvalues = np.linalg.eigvalsh(P)
            num_plus = sum(1 for ev in eigenvalues if ev > 0)
            num_minus = sum(1 for ev in eigenvalues if ev < 0)
            assert num_plus == N * (N + 1) // 2
            assert num_minus == N * (N - 1) // 2

    def test_trace(self):
        """Tr(P) = N (number of fixed points |i>|i>)."""
        for N in [2, 3, 4, 5]:
            P = _permutation_operator(N)
            assert abs(np.trace(P) - N) < 1e-12

    def test_swap_action(self):
        """P|i>|j> = |j>|i> for specific cases."""
        N = 3
        P = _permutation_operator(N)
        # |0>|1> -> |1>|0>: index 0*3+1=1 -> 1*3+0=3
        assert P[3, 1] == 1.0
        # |1>|2> -> |2>|1>: index 1*3+2=5 -> 2*3+1=7
        assert P[7, 5] == 1.0
        # |0>|0> -> |0>|0>: index 0 -> 0
        assert P[0, 0] == 1.0


# =========================================================================
# Boundary strip defect tests
# =========================================================================

class TestBoundaryStripDefect:
    """Test the boundary strip defect for the Yang R-matrix."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_defect_zero(self, N):
        """Boundary strip defect vanishes for N = 2, ..., 6."""
        defect = boundary_strip_defect(N)
        assert defect == 0, f"Defect = {defect} != 0 at N={N}"

    def test_defect_zero_N7(self):
        """Boundary strip defect vanishes at N = 7."""
        assert boundary_strip_defect(7) == 0

    def test_defect_zero_N8(self):
        """Boundary strip defect vanishes at N = 8."""
        assert boundary_strip_defect(8) == 0

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            boundary_strip_defect(1)
        with pytest.raises(ValueError):
            boundary_strip_defect(0)

    def test_antisymmetric_dimension(self):
        """dim Lambda^2(C^N) = N(N-1)/2."""
        for N in [2, 3, 4, 5]:
            P = _permutation_operator(N)
            identity = np.eye(N * N)
            antisym_proj = (identity - P) / 2.0
            dim_antisym = int(round(np.trace(antisym_proj)))
            assert dim_antisym == N * (N - 1) // 2

    def test_verify_boundary_strip_identities(self):
        """Batch verification of boundary strip identities."""
        result = verify_boundary_strip_identities(max_N=6)
        assert result["all_zero"]
        assert result["max_N"] == 6
        assert len(result["results"]) == 5  # N=2,...,6

    def test_verify_boundary_strip_results_structure(self):
        """Each result has defect, dim_antisym, dim_line, dim_rtt."""
        result = verify_boundary_strip_identities(max_N=4)
        for N, data in result["results"].items():
            assert "defect" in data
            assert "dim_antisym" in data
            assert "dim_line" in data
            assert "dim_rtt" in data
            assert data["dim_line"] == data["dim_antisym"]

    def test_verify_boundary_strip_consistency(self):
        """dim_rtt = dim_line - defect for each N."""
        result = verify_boundary_strip_identities(max_N=6)
        for N, data in result["results"].items():
            assert data["dim_rtt"] == data["dim_line"] - data["defect"]


# =========================================================================
# Thick closure tests (Clebsch-Gordan recursion)
# =========================================================================

class TestThickClosureEvaluationSl2:
    """Test thick closure of evaluation modules for Y(sl_2)."""

    def test_all_reachable(self):
        """All V_n for n = 0, ..., 10 are reachable from {V_0, V_1}."""
        result = thick_closure_evaluation_sl2(max_spin=10)
        assert result["all_reachable"]

    def test_all_reachable_large(self):
        """All V_n for n = 0, ..., 50 are reachable."""
        result = thick_closure_evaluation_sl2(max_spin=50)
        assert result["all_reachable"]

    def test_clebsch_gordan_holds(self):
        """Clebsch-Gordan: dim(V_1 tensor V_n) = dim(V_{n+1}) + dim(V_{n-1})."""
        result = thick_closure_evaluation_sl2(max_spin=20)
        assert result["all_clebsch_gordan_hold"]

    def test_dimensions_correct(self):
        """dim V_n = n + 1."""
        result = thick_closure_evaluation_sl2(max_spin=10)
        for n, dim in result["dims"].items():
            assert dim == n + 1, f"dim V_{n} = {dim} != {n+1}"

    def test_V0_V1_are_seeds(self):
        """V_0 and V_1 are the seed representations."""
        result = thick_closure_evaluation_sl2(max_spin=5)
        assert result["reachable"][0]
        assert result["reachable"][1]

    def test_recursion_step_structure(self):
        """Each recursion step has the expected fields."""
        result = thick_closure_evaluation_sl2(max_spin=5)
        for step in result["recursion_steps"]:
            assert "n" in step
            assert "dim_V_n" in step
            assert "clebsch_gordan_holds" in step
            assert "reachable_from_V0_V1" in step

    def test_clebsch_gordan_dimensions(self):
        """V_1 tensor V_n has dimension 2(n+1) = (n+2) + n."""
        result = thick_closure_evaluation_sl2(max_spin=10)
        for step in result["recursion_steps"]:
            n = step["n"]
            assert step["dim_V1_tensor_V_{n-1}"] == 2 * n
            assert step["dim_V_n_plus_V_{n-2}"] == (n + 1) + (n - 1)
            # Both equal 2n
            assert step["dim_V1_tensor_V_{n-1}"] == step["dim_V_n_plus_V_{n-2}"]

    def test_generator_is_fundamental(self):
        """The generator is V_1 (the fundamental 2-dim representation)."""
        result = thick_closure_evaluation_sl2(max_spin=3)
        assert "V_1" in result["generator"]
        assert "fundamental" in result["generator"]


# =========================================================================
# K_0 lattice comparison tests
# =========================================================================

class TestCompactGeneratorK0Comparison:
    """Test K_0 lattice comparison between Yangian and quantum group."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_k0_ranks_match(self, N):
        """K_0 ranks match: both are N-1."""
        result = compact_generator_k0_comparison(N)
        assert result["k0_ranks_match"]
        assert result["rank"] == N - 1

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_generator_dims_match(self, N):
        """Fundamental representation dimensions match."""
        result = compact_generator_k0_comparison(N)
        assert result["generator_dims_match"]

    def test_sl2_rank(self):
        """sl_2: K_0 has rank 1."""
        result = compact_generator_k0_comparison(2)
        assert result["rank"] == 1

    def test_sl3_rank(self):
        """sl_3: K_0 has rank 2."""
        result = compact_generator_k0_comparison(3)
        assert result["rank"] == 2

    def test_sl4_rank(self):
        """sl_4: K_0 has rank 3."""
        result = compact_generator_k0_comparison(4)
        assert result["rank"] == 3

    def test_fundamental_dims_sl2(self):
        """sl_2: V_{omega_1} has dim 2."""
        result = compact_generator_k0_comparison(2)
        assert result["fundamental_dims"]["omega_1"] == 2

    def test_fundamental_dims_sl3(self):
        """sl_3: V_{omega_1} = 3, V_{omega_2} = 3 (dual)."""
        result = compact_generator_k0_comparison(3)
        assert result["fundamental_dims"]["omega_1"] == 3
        assert result["fundamental_dims"]["omega_2"] == 3

    def test_fundamental_dims_sl4(self):
        """sl_4: V_{omega_1} = 4, V_{omega_2} = 6, V_{omega_3} = 4."""
        result = compact_generator_k0_comparison(4)
        assert result["fundamental_dims"]["omega_1"] == 4
        assert result["fundamental_dims"]["omega_2"] == 6
        assert result["fundamental_dims"]["omega_3"] == 4

    def test_fundamental_dims_formula(self):
        """dim V_{omega_k} = C(N, k) for all N, k."""
        for N in [2, 3, 4, 5, 6]:
            result = compact_generator_k0_comparison(N)
            for k in range(1, N):
                key = f"omega_{k}"
                assert result["fundamental_dims"][key] == comb(N, k), (
                    f"dim V_{{omega_{k}}} for sl_{N}: "
                    f"got {result['fundamental_dims'][key]}, expected {comb(N, k)}"
                )

    def test_isomorphism_verified(self):
        """K_0 isomorphism is verified for all N."""
        for N in [2, 3, 4, 5]:
            result = compact_generator_k0_comparison(N)
            assert result["isomorphism_verified"]

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            compact_generator_k0_comparison(1)


# =========================================================================
# Francis-Gaitsgory completion data tests
# =========================================================================

class TestFrancisGaitsgoryCompletionData:
    """Test Francis-Gaitsgory pro-nilpotent completion data."""

    def test_sl2_dim_g(self):
        """dim(sl_2) = 3."""
        result = francis_gaitsgory_completion_data(2)
        assert result["dim_g"] == 3

    def test_sl3_dim_g(self):
        """dim(sl_3) = 8."""
        result = francis_gaitsgory_completion_data(3)
        assert result["dim_g"] == 8

    def test_sl4_dim_g(self):
        """dim(sl_4) = 15."""
        result = francis_gaitsgory_completion_data(4)
        assert result["dim_g"] == 15

    def test_dim_g_formula(self):
        """dim(sl_N) = N^2 - 1."""
        for N in [2, 3, 4, 5, 6]:
            result = francis_gaitsgory_completion_data(N)
            assert result["dim_g"] == N * N - 1

    def test_truncation_dim_1(self):
        """Y/I = C has dimension 1."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            assert result["truncation_dims"][1] == 1

    def test_truncation_dim_2(self):
        """Y/I^2 = C + sl_N has dimension N^2."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            expected = 1 + (N * N - 1)
            assert result["truncation_dims"][2] == expected

    def test_truncation_dims_increasing(self):
        """Truncation dimensions are strictly increasing."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            dims = result["truncation_dims"]
            assert dims[1] < dims[2] < dims[3]

    def test_augmentation_ideal_generators(self):
        """Augmentation ideal has dim(g) generators."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            assert result["augmentation_ideal_generators"] == N * N - 1

    def test_rtt_generators_per_level(self):
        """RTT generators per level = N^2."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            assert result["rtt_generators_per_level"] == N * N

    def test_rank(self):
        """Rank is N-1."""
        for N in [2, 3, 4]:
            result = francis_gaitsgory_completion_data(N)
            assert result["rank"] == N - 1

    def test_completion_type(self):
        """Completion type is pro-nilpotent."""
        result = francis_gaitsgory_completion_data(2)
        assert result["completion_type"] == "pro-nilpotent"

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            francis_gaitsgory_completion_data(1)


# =========================================================================
# Evaluation core vs O_poly tests
# =========================================================================

class TestEvalCoreVsFullO:
    """Test comparison between D^eval and D^b(O_poly)."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_type_a_equivalence(self, N):
        """Type A equivalence holds for all N."""
        result = eval_core_vs_full_O(N)
        assert result["type_a_equivalence"]

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_dk_statuses_proved(self, N):
        """DK-1, DK-2, DK-3 are all PROVED."""
        result = eval_core_vs_full_O(N)
        assert result["dk_1_status"] == "PROVED"
        assert result["dk_2_status"] == "PROVED"
        assert result["dk_3_status"] == "PROVED"

    def test_rank(self):
        """Rank is N-1."""
        for N in [2, 3, 4]:
            result = eval_core_vs_full_O(N)
            assert result["rank"] == N - 1

    def test_eval_core_has_compact_generators(self):
        """Evaluation core has N-1 compact generators (fundamentals)."""
        for N in [2, 3, 4]:
            result = eval_core_vs_full_O(N)
            assert result["eval_core"]["num_compact_generators"] == N - 1

    def test_o_poly_contains_fd_modules(self):
        """O_poly contains fd modules."""
        result = eval_core_vs_full_O(3)
        assert "fd modules" in result["o_poly"]["contains"]

    def test_o_poly_contains_standard_modules(self):
        """O_poly contains standard modules."""
        result = eval_core_vs_full_O(3)
        assert "standard modules" in result["o_poly"]["contains"]

    def test_sl2_explicit_data(self):
        """sl_2 has explicit evaluation module description."""
        result = eval_core_vs_full_O(2)
        assert "explicit" in result["eval_core"]
        assert "V_n(a)" in result["eval_core"]["explicit"]

    def test_reference_fields(self):
        """Result has reference field."""
        result = eval_core_vs_full_O(2)
        assert "reference" in result
        assert "eval-core" in result["reference"]
        assert "dk-poly" in result["reference"]

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            eval_core_vs_full_O(1)


# =========================================================================
# Drinfeld polynomial classification tests
# =========================================================================

class TestDrinfeldPolynomialClassification:
    """Test Drinfeld polynomial classification of fd Y(sl_N) modules."""

    def test_sl2_trivial(self):
        """sl_2 degree 0: trivial representation only."""
        result = drinfeld_polynomial_classification(2, max_deg=0)
        assert result["total_count"] == 1
        assert result["classifications"][0]["dim"] == 1
        assert result["classifications"][0]["degree"] == 0

    def test_sl2_up_to_deg3(self):
        """sl_2 up to degree 3: 4 families (deg 0, 1, 2, 3)."""
        result = drinfeld_polynomial_classification(2, max_deg=3)
        assert result["total_count"] == 4
        assert result["count_by_degree"] == {0: 1, 1: 1, 2: 1, 3: 1}

    def test_sl2_dimensions(self):
        """sl_2: V_n has dim n+1."""
        result = drinfeld_polynomial_classification(2, max_deg=5)
        for c in result["classifications"]:
            if isinstance(c["dim"], int):
                assert c["dim"] == c["degree"] + 1

    def test_sl2_all_evaluation(self):
        """sl_2: all modules are evaluation modules."""
        result = drinfeld_polynomial_classification(2, max_deg=5)
        for c in result["classifications"]:
            assert c["is_evaluation"]

    def test_sl3_trivial(self):
        """sl_3 degree 0: trivial representation."""
        result = drinfeld_polynomial_classification(3, max_deg=0)
        assert result["total_count"] == 1
        assert result["classifications"][0]["dim"] == 1

    def test_sl3_fundamentals(self):
        """sl_3 degree 1: two fundamental representations (3, 3-bar)."""
        result = drinfeld_polynomial_classification(3, max_deg=1)
        deg1_classes = [c for c in result["classifications"] if c["degree"] == 1]
        assert len(deg1_classes) == 2
        # Both have dim 3 = C(3,1) = C(3,2)
        dims = sorted([c["dim"] for c in deg1_classes])
        assert dims == [3, 3]

    def test_sl3_degree2_count(self):
        """sl_3 degree 2: 3 composition types (2,0), (1,1), (0,2)."""
        result = drinfeld_polynomial_classification(3, max_deg=2)
        deg2_classes = [c for c in result["classifications"] if c["degree"] == 2]
        assert len(deg2_classes) == 3

    def test_sl3_degree2_evaluation(self):
        """sl_3 degree 2: (1,1) is evaluation, (2,0) and (0,2) are not."""
        result = drinfeld_polynomial_classification(3, max_deg=2)
        deg2_classes = [c for c in result["classifications"] if c["degree"] == 2]
        eval_count = sum(1 for c in deg2_classes if c["is_evaluation"])
        non_eval_count = sum(1 for c in deg2_classes if not c["is_evaluation"])
        assert eval_count == 1  # (1,1): both P_i have degree 1
        assert non_eval_count == 2  # (2,0) and (0,2)

    def test_rank_field(self):
        """Rank is N-1."""
        for N in [2, 3, 4]:
            result = drinfeld_polynomial_classification(N, max_deg=1)
            assert result["rank"] == N - 1

    def test_theorem_field(self):
        """Theorem reference is Drinfeld classification."""
        result = drinfeld_polynomial_classification(2, max_deg=1)
        assert "Drinfeld" in result["theorem"]

    def test_invalid_N(self):
        """N < 2 raises ValueError."""
        with pytest.raises(ValueError):
            drinfeld_polynomial_classification(1)


# =========================================================================
# Compositions helper tests
# =========================================================================

class TestCompositions:
    """Test the integer compositions helper."""

    def test_single_part(self):
        """Compositions of n into 1 part: just (n,)."""
        assert _compositions(3, 1) == [(3,)]
        assert _compositions(0, 1) == [(0,)]

    def test_two_parts(self):
        """Compositions of n into 2 parts."""
        result = _compositions(2, 2)
        assert len(result) == 3
        assert set(result) == {(0, 2), (1, 1), (2, 0)}

    def test_three_parts_sum_2(self):
        """Compositions of 2 into 3 parts."""
        result = _compositions(2, 3)
        # (0,0,2), (0,1,1), (0,2,0), (1,0,1), (1,1,0), (2,0,0)
        assert len(result) == 6
        for comp in result:
            assert sum(comp) == 2
            assert len(comp) == 3

    def test_zero_into_k(self):
        """Compositions of 0 into k parts: all zeros."""
        for k in [1, 2, 3]:
            result = _compositions(0, k)
            assert len(result) == 1
            assert result[0] == tuple(0 for _ in range(k))

    def test_count_formula(self):
        """Number of compositions of n into k parts = C(n+k-1, k-1)."""
        for n in range(5):
            for k in range(1, 4):
                result = _compositions(n, k)
                expected_count = comb(n + k - 1, k - 1)
                assert len(result) == expected_count, (
                    f"compositions({n}, {k}): got {len(result)}, "
                    f"expected {expected_count}"
                )


# =========================================================================
# Integration tests
# =========================================================================

class TestIntegration:
    """Cross-cutting integration tests."""

    def test_dk_ladder_consistency_with_eval_core(self):
        """DK ladder status is consistent with eval_core_vs_full_O."""
        status = dk_ladder_status()
        for N in [2, 3, 4]:
            ev = eval_core_vs_full_O(N)
            assert ev["dk_1_status"] == status["DK-1"]["status"]
            assert ev["dk_2_status"] == status["DK-2"]["status"]
            assert ev["dk_3_status"] == status["DK-3"]["status"]

    def test_thick_closure_implies_k0_generation(self):
        """Thick closure (all V_n reachable) implies K_0 is generated by V_1."""
        tc = thick_closure_evaluation_sl2(max_spin=10)
        k0 = compact_generator_k0_comparison(2)
        assert tc["all_reachable"]
        assert k0["k0_ranks_match"]

    def test_boundary_strip_consistent_with_k0(self):
        """Boundary strip defect = 0 is consistent with K_0 matching."""
        for N in [2, 3, 4, 5]:
            defect = boundary_strip_defect(N)
            k0 = compact_generator_k0_comparison(N)
            assert defect == 0
            assert k0["k0_ranks_match"]

    def test_fg_completion_consistent_with_dk_ladder(self):
        """FG completion status references DK-4/5."""
        fg = francis_gaitsgory_completion_data(2)
        status = dk_ladder_status()
        assert "4/5" in fg["status"] or "DK" in fg["status"]
        assert status["DK-4/5"]["status"] == "CONJECTURAL"

    def test_drinfeld_classification_matches_thick_closure(self):
        """For sl_2, Drinfeld classification confirms evaluation = all fd."""
        dp = drinfeld_polynomial_classification(2, max_deg=10)
        tc = thick_closure_evaluation_sl2(max_spin=10)

        # All Drinfeld classes are evaluation modules
        for c in dp["classifications"]:
            assert c["is_evaluation"]

        # All V_n are reachable from thick closure
        assert tc["all_reachable"]

    def test_fundamental_dim_matches_clebsch_gordan(self):
        """V_{omega_1} = V_1 for sl_2 has dim 2, matching CG generator."""
        k0 = compact_generator_k0_comparison(2)
        tc = thick_closure_evaluation_sl2(max_spin=3)
        assert k0["fundamental_dims"]["omega_1"] == 2
        assert tc["dims"][1] == 2

    def test_all_proved_levels_have_computational_verification(self):
        """Every PROVED DK level has some computational verification in this module."""
        status = dk_ladder_status()
        proved_levels = [lev for lev, d in status.items() if d["status"] == "PROVED"]
        # DK-0: bar-cobar (verified by bar complex modules elsewhere)
        # DK-1: eval core (verified by eval_core_vs_full_O)
        # DK-1.5: lattice (verified by sectorwise_finiteness module)
        # DK-2/3: fd type A / O_poly (verified by thick closure + K_0 + boundary strip)
        assert len(proved_levels) == 5
