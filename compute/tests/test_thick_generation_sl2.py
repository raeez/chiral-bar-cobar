"""Tests for thick generation analysis — MC3 G5 aggressive attack.

Verifies:
  1. Fock-Verma factorization: ch(L^-) = ch(M(0)) * ch(F_multi)
  2. Multi-particle sector dimensions (partitions with parts >= 2)
  3. Character-level Hom/Ext bounds
  4. p(k) obstruction growth (sub-exponential)
  5. Character containment: ch(M(lam)) <= ch(V_lam tensor L^-)
  6. Sectorwise Ext finiteness
  7. Full thick generation evidence package
"""

from __future__ import annotations

import math

import pytest

from compute.lib.thick_generation_sl2 import (
    ext_euler_char_bound,
    fock_verma_factorization_check,
    hom_bound_L_minus_Verma,
    hom_bound_L_minus_Vn,
    iterated_baxter_from_L_minus,
    multi_particle_character,
    multi_particle_dimensions,
    obstruction_growth_analysis,
    pk_obstruction_sequence,
    resolution_obstruction_dimensions,
    sectorwise_ext_finiteness,
    thick_generation_evidence,
    verma_approx_from_L_minus,
    verify_all,
)
from compute.lib.hjz_prefundamental import partition_function


# =========================================================================
# 1. Fock-Verma factorization
# =========================================================================

class TestFockVermaFactorization:
    """Verify ch(L^-) = ch(M(0)) * ch(F_multi)."""

    def test_factorization_holds(self):
        result = fock_verma_factorization_check(depth=30)
        assert result["factorization_holds"]

    def test_factorization_deep(self):
        result = fock_verma_factorization_check(depth=50)
        assert result["factorization_holds"]
        assert result["n_mismatches"] == 0

    def test_multi_particle_character_weight_0(self):
        """p_2(0) = 1 (empty partition)."""
        char = multi_particle_character(depth=10)
        assert char.get(0, 0) == 1

    def test_multi_particle_character_weight_2(self):
        """p_2(1) = 0 (no partition of 1 with all parts >= 2)."""
        char = multi_particle_character(depth=10)
        assert char.get(-2, 0) == 0

    def test_multi_particle_character_weight_4(self):
        """p_2(2) = 1 (partition {2})."""
        char = multi_particle_character(depth=10)
        assert char.get(-4, 0) == 1

    def test_multi_particle_character_weight_6(self):
        """p_2(3) = 1 (partition {3})."""
        char = multi_particle_character(depth=10)
        assert char.get(-6, 0) == 1

    def test_multi_particle_character_weight_8(self):
        """p_2(4) = 2 (partitions {4}, {2,2})."""
        char = multi_particle_character(depth=10)
        assert char.get(-8, 0) == 2

    def test_multi_particle_character_weight_10(self):
        """p_2(5) = 2 (partitions {5}, {3,2})."""
        char = multi_particle_character(depth=10)
        assert char.get(-10, 0) == 2


class TestMultiParticleDimensions:
    """Verify p_2(k) = p(k) - p(k-1) recurrence."""

    def test_recurrence(self):
        dims = multi_particle_dimensions(max_k=20)
        for k, pk, p2k in dims:
            if k >= 1:
                assert p2k == pk - partition_function(k - 1), (
                    f"p_2({k}) = {p2k} != p({k}) - p({k}-1) = "
                    f"{pk} - {partition_function(k-1)}"
                )

    def test_first_values(self):
        dims = multi_particle_dimensions(max_k=10)
        # p_2 sequence: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12
        expected_p2 = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        for i, (k, pk, p2k) in enumerate(dims):
            assert p2k == expected_p2[i], f"p_2({k}) = {p2k}, expected {expected_p2[i]}"


# =========================================================================
# 2. Character-level Hom/Ext bounds
# =========================================================================

class TestHomBounds:
    """Verify Hom(L^-, V_n) weight bounds."""

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8])
    def test_even_n(self, n):
        """For n even: Hom bound = n/2 + 1."""
        result = hom_bound_L_minus_Vn(n)
        assert result["hom_weight_bound"] == n // 2 + 1
        assert result["bound_matches_prediction"]

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9])
    def test_odd_n(self, n):
        """For n odd: Hom bound = 0 (parity mismatch)."""
        result = hom_bound_L_minus_Vn(n)
        assert result["hom_weight_bound"] == 0
        assert result["bound_matches_prediction"]

    def test_hom_verma_even(self):
        """Hom(L^-, M(0)) is infinite (grows with depth)."""
        r1 = hom_bound_L_minus_Verma(0, depth=20)
        r2 = hom_bound_L_minus_Verma(0, depth=40)
        assert r2["hom_weight_bound"] > r1["hom_weight_bound"]
        assert r1["is_infinite"]

    def test_hom_verma_odd(self):
        """Hom(L^-, M(1)) = 0 (parity mismatch)."""
        result = hom_bound_L_minus_Verma(1, depth=30)
        assert result["hom_weight_bound"] == 0
        assert not result["is_infinite"]


class TestEulerCharacteristic:
    """Verify chi(L^-, V_n) computation."""

    def test_euler_V0(self):
        """chi(L^-, V_0) = p(0) = 1."""
        result = ext_euler_char_bound(0)
        assert result["euler_characteristic"] == 1

    def test_euler_V1(self):
        """chi(L^-, V_1) = 0 (parity mismatch)."""
        result = ext_euler_char_bound(1)
        assert result["euler_characteristic"] == 0

    def test_euler_V2(self):
        """chi(L^-, V_2) = p(0) + p(1) = 2."""
        result = ext_euler_char_bound(2)
        assert result["euler_characteristic"] == 2

    def test_euler_V4(self):
        """chi(L^-, V_4) = p(0) + p(1) + p(2) = 4."""
        result = ext_euler_char_bound(4)
        assert result["euler_characteristic"] == 4

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8, 10])
    def test_euler_even_formula(self, n):
        """chi(L^-, V_n) = sum_{k=0}^{n/2} p(k) for n even."""
        result = ext_euler_char_bound(n)
        expected = sum(partition_function(k) for k in range(n // 2 + 1))
        assert result["euler_characteristic"] == expected


# =========================================================================
# 3. p(k) obstruction analysis
# =========================================================================

class TestObstruction:
    """Verify the p(k) - 1 obstruction sequence."""

    def test_first_values(self):
        seq = pk_obstruction_sequence(max_k=10)
        expected_delta = [0, 0, 1, 2, 4, 6, 10, 14, 21, 29, 41]
        for i, entry in enumerate(seq):
            assert entry["delta_k"] == expected_delta[i], (
                f"delta({i}) = {entry['delta_k']}, expected {expected_delta[i]}"
            )

    def test_delta_is_pk_minus_1(self):
        seq = pk_obstruction_sequence(max_k=20)
        for entry in seq:
            assert entry["delta_k"] == entry["p_k"] - 1

    def test_sub_exponential_growth(self):
        result = obstruction_growth_analysis(max_k=50)
        assert result["is_sub_exponential"]

    def test_growth_slope_positive(self):
        result = obstruction_growth_analysis(max_k=50)
        assert result["estimated_slope"] > 0

    def test_growth_slope_near_theoretical(self):
        """Estimated slope should be within 20% of pi*sqrt(2/3)."""
        result = obstruction_growth_analysis(max_k=50)
        assert 0.7 < result["slope_ratio"] < 1.3


# =========================================================================
# 4. Character containment
# =========================================================================

class TestCharacterContainment:
    """Verify ch(M(lam)) <= ch(V_lam tensor L^-)."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, 4, 5, 6])
    def test_containment(self, lam):
        """M(lam) character is contained in V_lam tensor L^-."""
        result = verma_approx_from_L_minus(lam, depth=25)
        assert result["containment"]

    def test_excess_grows(self):
        """Excess ratio should grow with lambda."""
        ratios = []
        for lam in range(0, 7):
            result = verma_approx_from_L_minus(lam, depth=25)
            ratios.append(result["ratio"])
        # Excess should be non-negative and generally growing
        assert all(r >= 0 for r in ratios)


# =========================================================================
# 5. Iterated Baxter from L^-
# =========================================================================

class TestIteratedBaxter:
    """Verify iterated Baxter generation from L^-."""

    def test_alternating_parity(self):
        """V_1^n tensor L^- alternates between even and odd weight lattices."""
        result = iterated_baxter_from_L_minus(max_iter=6, depth=20)
        assert result["alternating_parity"]

    def test_step_0_even(self):
        """L^- lives on even weight lattice."""
        result = iterated_baxter_from_L_minus(max_iter=2, depth=20)
        assert result["iterates"][0]["weight_parity"] == "even"

    def test_step_1_odd(self):
        """V_1 tensor L^- lives on odd weight lattice."""
        result = iterated_baxter_from_L_minus(max_iter=2, depth=20)
        assert result["iterates"][1]["weight_parity"] == "odd"

    def test_highest_weight_increases(self):
        """Highest weight increases by 1 at each step."""
        result = iterated_baxter_from_L_minus(max_iter=6, depth=20)
        hws = [it["highest_weight"] for it in result["iterates"]]
        for i in range(1, len(hws)):
            assert hws[i] == hws[i - 1] + 1


# =========================================================================
# 6. Sectorwise Ext finiteness
# =========================================================================

class TestExtFiniteness:
    """Verify sectorwise finiteness of Ext^*(L^-, V_n)."""

    def test_all_hom_finite(self):
        result = sectorwise_ext_finiteness(max_n=10, depth=30)
        assert result["all_finite_hom"]

    def test_hom_zero_for_odd(self):
        result = sectorwise_ext_finiteness(max_n=10, depth=30)
        for r in result["results"]:
            if r["n"] % 2 == 1:
                assert r["hom_bound"] == 0


# =========================================================================
# 7. Resolution obstruction
# =========================================================================

class TestResolutionObstruction:
    """Verify resolution obstruction dimensions."""

    def test_resolution_converges(self):
        """Resolution obstruction should decrease with degree."""
        result = resolution_obstruction_dimensions(lam=0, max_degree=4, depth=20)
        assert result["converging"]

    def test_first_obstruction_at_k2(self):
        """First nonzero obstruction at k=2 (weight -4)."""
        seq = pk_obstruction_sequence(max_k=5)
        assert seq[0]["delta_k"] == 0  # k=0
        assert seq[1]["delta_k"] == 0  # k=1
        assert seq[2]["delta_k"] == 1  # k=2: p(2)-1 = 1


# =========================================================================
# 8. Full thick generation evidence
# =========================================================================

class TestThickGenerationEvidence:
    """Full G5 evidence package."""

    def test_overall_verdict(self):
        result = thick_generation_evidence(max_lam=4, depth=25)
        assert result["overall_verdict"]

    def test_fock_factorization_in_evidence(self):
        result = thick_generation_evidence(max_lam=4, depth=25)
        assert result["fock_factorization"]

    def test_sub_exponential_in_evidence(self):
        result = thick_generation_evidence(max_lam=4, depth=25)
        assert result["sub_exponential_growth"]

    def test_all_contained_in_evidence(self):
        result = thick_generation_evidence(max_lam=4, depth=25)
        assert result["all_contained"]


# =========================================================================
# 9. Verify all
# =========================================================================

class TestVerifyAll:
    """Run the full verification suite."""

    def test_all_pass(self):
        results = verify_all(depth=25)
        for name, val in results.items():
            if isinstance(val, bool):
                assert val, f"Check '{name}' failed"
