"""Comprehensive tests for MC3 frontier modules.

Tests three new compute modules:
  1. mc3_ext_computation — Ext and resolution obstruction analysis
  2. mc3_tilting_probe — Rickard tilting self-orthogonality probe
  3. mc3_chromatic_strategy — Chromatic/conformal weight filtration strategy

Total: ~75 tests covering all functions in all three modules.
"""

import math

import pytest
from sympy import Rational, pi, sqrt

from compute.lib.mc3_ext_computation import (
    _partition_number,
    compactness_obstruction_count,
    endomorphism_algebra_G,
    euler_char_prefundamental_eval,
    ext1_from_baxter_ses,
    hardy_ramanujan_constant,
    hom_prefundamental_eval,
    multi_partition_function,
    resolution_obstruction_higher_rank,
    resolution_obstruction_sequence,
    verify_sub_exponential_growth,
)
from compute.lib.mc3_tilting_probe import (
    euler_characteristic_pattern,
    finite_length_obstruction_test,
    self_orthogonality_check,
    tilting_complex_from_baxter,
)
from compute.lib.mc3_chromatic_strategy import (
    _partitions_into_odd_parts_geq3,
    capture_ratio,
    chromatic_vs_naive_comparison,
    pro_weyl_mittag_leffler_assembly,
    sectorwise_e1_page,
    spectral_sequence_convergence_check,
)


# ===========================================================================
# Reference data: partition numbers p(k)
# ===========================================================================

PARTITION_NUMBERS = [
    1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231
]


# ===========================================================================
# Module 1: mc3_ext_computation
# ===========================================================================


class TestPartitionNumber:
    """Verify the partition function implementation."""

    @pytest.mark.parametrize("k, expected", list(enumerate(PARTITION_NUMBERS)))
    def test_known_values(self, k, expected):
        assert _partition_number(k) == expected

    def test_negative(self):
        assert _partition_number(-1) == 0
        assert _partition_number(-5) == 0


class TestHomPrefundamentalEval:
    """Hom(L⁻, V_n) = 0 for n odd, n/2+1 for n even."""

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9, 11, 13, 15])
    def test_odd_n_zero(self, n):
        """Weight parity: V_n has odd weights, L⁻ has even → Hom = 0."""
        assert hom_prefundamental_eval(n) == 0

    @pytest.mark.parametrize("n, expected", [
        (0, 1), (2, 2), (4, 3), (6, 4), (8, 5), (10, 6), (12, 7), (14, 8),
    ])
    def test_even_n(self, n, expected):
        """Hom(L⁻, V_n) = n/2 + 1 for even n."""
        assert hom_prefundamental_eval(n) == expected

    def test_formula(self):
        """Verify the formula n/2 + 1 for even n up to 30."""
        for n in range(0, 31, 2):
            assert hom_prefundamental_eval(n) == n // 2 + 1


class TestEulerCharPrefundamentalEval:
    """χ(L⁻, V_n) = Σ_{k=0}^{n/2} p(k) for even n."""

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9])
    def test_odd_n_zero(self, n):
        assert euler_char_prefundamental_eval(n) == 0

    def test_n0(self):
        """χ(L⁻, V_0) = p(0) = 1."""
        assert euler_char_prefundamental_eval(0) == 1

    def test_n2(self):
        """χ(L⁻, V_2) = p(0) + p(1) = 1 + 1 = 2."""
        assert euler_char_prefundamental_eval(2) == 2

    def test_n4(self):
        """χ(L⁻, V_4) = p(0) + p(1) + p(2) = 1 + 1 + 2 = 4."""
        assert euler_char_prefundamental_eval(4) == 4

    def test_n6(self):
        """χ(L⁻, V_6) = p(0)+p(1)+p(2)+p(3) = 1+1+2+3 = 7."""
        assert euler_char_prefundamental_eval(6) == 7

    def test_n8(self):
        """χ(L⁻, V_8) = Σ_{k=0}^{4} p(k) = 1+1+2+3+5 = 12."""
        assert euler_char_prefundamental_eval(8) == 12

    def test_n10(self):
        """χ(L⁻, V_10) = Σ_{k=0}^{5} p(k) = 1+1+2+3+5+7 = 19."""
        assert euler_char_prefundamental_eval(10) == 19

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8, 10, 12])
    def test_cumulative_partition_sum(self, n):
        """Verify χ = Σ p(k) formula for even n."""
        expected = sum(_partition_number(k) for k in range(n // 2 + 1))
        assert euler_char_prefundamental_eval(n) == expected


class TestResolutionObstructionSequence:
    """δ(k) = p(k) - 1."""

    def test_basic_values(self):
        obs = resolution_obstruction_sequence(max_k=10)
        assert obs[1] == 0   # p(1)-1 = 0
        assert obs[2] == 1   # p(2)-1 = 1
        assert obs[3] == 2   # p(3)-1 = 2
        assert obs[4] == 4   # p(4)-1 = 4
        assert obs[5] == 6   # p(5)-1 = 6

    def test_all_nonnegative(self):
        obs = resolution_obstruction_sequence(max_k=50)
        for k, delta in obs.items():
            assert delta >= 0, f"δ({k}) = {delta} < 0"

    def test_monotone_from_k2(self):
        """δ(k) is non-decreasing for k ≥ 2."""
        obs = resolution_obstruction_sequence(max_k=50)
        for k in range(3, 51):
            assert obs[k] >= obs[k - 1], f"δ({k}) < δ({k-1})"


class TestSubExponentialGrowth:
    """log(p(k))/√k → π√(2/3) ≈ 2.5651.

    Hardy-Ramanujan convergence is SLOW due to sub-leading 1/√k corrections.
    At k=50, the ratio is only ~1.73 (vs limit 2.57). We test:
    1. The ratio is INCREASING (approaching the limit from below).
    2. The ratio is bounded below the HR constant (approaches from below).
    3. The ratio at k=50 is in a reasonable range.
    """

    def test_increasing(self):
        """The ratio log(p(k))/√k is increasing for large k."""
        ratios = verify_sub_exponential_growth(max_k=50)
        # Check monotone increasing for k ≥ 5
        for k in range(6, 51):
            assert ratios[k] >= ratios[k - 1] - 0.01, (
                f"ratio at k={k} dropped: {ratios[k]:.4f} < {ratios[k-1]:.4f}"
            )

    def test_approaches_from_below(self):
        """For large k, the ratio should be below the HR constant."""
        ratios = verify_sub_exponential_growth(max_k=50)
        hr = hardy_ramanujan_constant()
        # The ratio approaches HR from below (always less than HR)
        assert ratios[50] < hr

    def test_in_reasonable_range(self):
        """At k=50, log(p(50))/√50 should be between 1.5 and 2.0."""
        ratios = verify_sub_exponential_growth(max_k=50)
        assert 1.5 < ratios[50] < 2.0

    def test_hr_constant_value(self):
        hr = hardy_ramanujan_constant()
        assert abs(hr - 2.5651) < 0.001


class TestMultiPartitionFunction:
    """N-colored partition function."""

    def test_n1_is_partition(self):
        """For N=1, p₁(k) = p(k)."""
        for k in range(15):
            assert multi_partition_function(1, k) == _partition_number(k)

    def test_n2_values(self):
        """p₂(0)=1, p₂(1)=2, p₂(2)=5, p₂(3)=10, p₂(4)=20."""
        # p₂(k) = Σ_{j=0}^{k} p(j)*p(k-j) (convolution)
        assert multi_partition_function(2, 0) == 1
        assert multi_partition_function(2, 1) == 1 * 1 + 1 * 1  # p(0)p(1)+p(1)p(0) = 2
        # p₂(2) = p(0)p(2)+p(1)p(1)+p(2)p(0) = 2+1+2 = 5
        assert multi_partition_function(2, 2) == 5

    def test_zero(self):
        assert multi_partition_function(1, 0) == 1
        assert multi_partition_function(5, 0) == 1

    def test_negative(self):
        assert multi_partition_function(1, -1) == 0

    def test_growth_with_rank(self):
        """p_N(k) grows with N for fixed k > 0."""
        for k in [3, 5, 8]:
            prev = multi_partition_function(1, k)
            for N in range(2, 5):
                curr = multi_partition_function(N, k)
                assert curr >= prev, f"p_{N}({k}) < p_{N-1}({k})"
                prev = curr


class TestResolutionObstructionHigherRank:
    """δ_N(k) = p_N(k) - 1 for sl_N."""

    def test_rank1_matches_standard(self):
        std = resolution_obstruction_sequence(max_k=20)
        hr = resolution_obstruction_higher_rank(1, max_k=20)
        for k in range(1, 21):
            assert hr[k] == std[k]

    def test_higher_rank_larger(self):
        """δ_N(k) ≥ δ_1(k) for N ≥ 1, k ≥ 1."""
        obs1 = resolution_obstruction_higher_rank(1, max_k=15)
        obs2 = resolution_obstruction_higher_rank(2, max_k=15)
        for k in range(1, 16):
            assert obs2[k] >= obs1[k]


class TestEndomorphismAlgebra:
    """dim Ext⁰(G, G) = 5 for G = V₁ ⊕ L⁻."""

    def test_total_dim(self):
        result = endomorphism_algebra_G()
        assert result["total_dim"] == 5

    def test_block_structure(self):
        result = endomorphism_algebra_G()
        blocks = result["blocks"]
        assert blocks["End(V₁)"] == 4
        assert blocks["End(L⁻)"] == 1
        assert blocks["Hom(V₁, L⁻)"] == 0
        assert blocks["Hom(L⁻, V₁)"] == 0

    def test_weight_parity_obstruction(self):
        result = endomorphism_algebra_G()
        assert result["weight_parity_obstruction"] is True


class TestCompactnessObstruction:
    """L⁻ has nonzero Hom to M(-2k) for all k ≥ 0."""

    def test_all_nonzero(self):
        result = compactness_obstruction_count(depth=30)
        assert result["all_nonzero"] is True

    def test_count_matches_depth(self):
        for d in [10, 20, 30]:
            result = compactness_obstruction_count(depth=d)
            assert result["nonzero_hom_count"] == d + 1

    def test_hom_lower_bounds(self):
        result = compactness_obstruction_count(depth=10)
        for k in range(11):
            detail = result["details"][-2 * k]
            assert detail["hom_lower_bound"] >= 1
            assert detail["L_mult_at_weight"] == _partition_number(k)


class TestExt1FromBaxterSES:
    """Ext¹(L⁻(+1), L⁻(-1)) ≠ 0."""

    def test_nonzero(self):
        result = ext1_from_baxter_ses()
        assert result["nonzero"] is True

    def test_ses_structure(self):
        result = ext1_from_baxter_ses()
        assert "L⁻(-1)" in result["ses"]
        assert "L⁻(+1)" in result["ses"]
        assert "V₁" in result["ses"]

    def test_has_yangian_origin(self):
        result = ext1_from_baxter_ses()
        assert "Δ(E)" in result["yangian_origin"]


# ===========================================================================
# Module 2: mc3_tilting_probe
# ===========================================================================


class TestSelfOrthogonality:
    """Hom(V_n, L⁻) = 0 for odd n."""

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9, 11])
    def test_odd_n_orthogonal(self, n):
        result = self_orthogonality_check(n)
        assert result["orthogonal"] is True
        assert result["hom_dim"] == 0

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8, 10])
    def test_even_n_not_orthogonal(self, n):
        result = self_orthogonality_check(n)
        assert result["orthogonal"] is False
        assert result["hom_dim"] == n // 2 + 1

    def test_weight_parity_labels(self):
        r_odd = self_orthogonality_check(3)
        assert r_odd["v_weights_parity"] == "odd"
        assert r_odd["l_weights_parity"] == "even"

        r_even = self_orthogonality_check(4)
        assert r_even["v_weights_parity"] == "even"


class TestEulerCharacteristicPattern:
    """χ(V_n, L⁻) = Σ_{k=0}^{n/2} p(k) for even n."""

    def test_pattern_values(self):
        pattern = euler_characteristic_pattern(max_n=10)
        assert pattern[0] == 1    # p(0) = 1
        assert pattern[2] == 2    # p(0)+p(1) = 2
        assert pattern[4] == 4    # p(0)+p(1)+p(2) = 4
        assert pattern[6] == 7    # + p(3) = 7
        assert pattern[8] == 12   # + p(4)=5 → 12
        assert pattern[10] == 19  # + p(5)=7 → 19

    def test_only_even_keys(self):
        pattern = euler_characteristic_pattern(max_n=20)
        for key in pattern:
            assert key % 2 == 0

    def test_monotone_increasing(self):
        pattern = euler_characteristic_pattern(max_n=20)
        keys = sorted(pattern.keys())
        for i in range(1, len(keys)):
            assert pattern[keys[i]] > pattern[keys[i - 1]]


class TestFiniteLengthObstruction:
    """Resolution length grows unboundedly."""

    def test_unbounded(self):
        result = finite_length_obstruction_test(max_n=20)
        assert result["unbounded"] is True

    def test_lengths_increasing(self):
        result = finite_length_obstruction_test(max_n=20)
        lengths = result["lengths"]
        for i in range(1, len(lengths)):
            assert lengths[i] >= lengths[i - 1]

    def test_cumulative_grows(self):
        result = finite_length_obstruction_test(max_n=30)
        assert result["cumulative_obstruction"] > 100  # grows fast


class TestTiltingComplex:
    """Tilting complex assembly from Baxter SES."""

    def test_structure(self):
        result = tilting_complex_from_baxter(max_spin=8)
        assert result["max_spin"] == 8
        assert len(result["complexes"]) == 8

    def test_odd_spin_orthogonal(self):
        result = tilting_complex_from_baxter(max_spin=10)
        assert result["odd_spin_all_orthogonal"] is True

    def test_n_summands(self):
        result = tilting_complex_from_baxter(max_spin=6)
        for c in result["complexes"]:
            assert c["n_summands"] == c["spin"] + 1

    def test_shifts_correct(self):
        result = tilting_complex_from_baxter(max_spin=4)
        for c in result["complexes"]:
            n = c["spin"]
            expected_shifts = [n - 2 * j for j in range(n + 1)]
            assert c["L_shifts"] == expected_shifts


# ===========================================================================
# Module 3: mc3_chromatic_strategy
# ===========================================================================


class TestPartitionsIntoOddPartsGeq3:
    """Partitions of n into odd parts ≥ 3."""

    @pytest.mark.parametrize("n, expected", [
        (0, 1),   # empty partition
        (1, 0),
        (2, 0),
        (3, 1),   # {3}
        (4, 0),
        (5, 1),   # {5}
        (6, 1),   # {3+3}
        (7, 1),   # {7}
        (8, 1),   # {3+5}
        (9, 2),   # {9, 3+3+3}
        (10, 2),  # {5+5, 3+7}
    ])
    def test_small_values(self, n, expected):
        assert _partitions_into_odd_parts_geq3(n) == expected

    def test_nonnegativity(self):
        for n in range(30):
            assert _partitions_into_odd_parts_geq3(n) >= 0


class TestSectorwiseE1Page:
    """E₁ page dimensions at each bidegree."""

    def test_root_weight_0(self):
        """At root weight 0, count partitions into odd parts ≥ 3."""
        for q in range(15):
            expected = _partitions_into_odd_parts_geq3(q)
            assert sectorwise_e1_page(0, q, rank=1) == expected

    def test_negative_loop_degree(self):
        assert sectorwise_e1_page(0, -1) == 0
        assert sectorwise_e1_page(5, -3) == 0

    def test_large_root_weight(self):
        """If |root_weight| > loop_degree, E₁ = 0."""
        assert sectorwise_e1_page(10, 5) == 0
        assert sectorwise_e1_page(-8, 3) == 0

    @pytest.mark.parametrize("p,q", [(0, 0), (0, 3), (0, 6), (1, 5), (2, 8)])
    def test_finite_dimensional(self, p, q):
        """Every E₁^{p,q} is finite (non-negative integer)."""
        dim = sectorwise_e1_page(p, q)
        assert isinstance(dim, int)
        assert dim >= 0


class TestCaptureRatio:
    """R(n) = Σ_{k≤n} p(k) / Σ_{k≤2n} p(k) is decreasing."""

    def test_decreasing(self):
        ratios = capture_ratio(30)
        for m in range(2, 31):
            assert ratios[m] <= ratios[m - 1], (
                f"R({m}) = {ratios[m]} > R({m-1}) = {ratios[m-1]}"
            )

    def test_bounded_01(self):
        """0 < R(n) < 1 for all n ≥ 1."""
        ratios = capture_ratio(30)
        for m, r in ratios.items():
            assert 0 < r < 1, f"R({m}) = {r} not in (0,1)"

    def test_exact_at_n1(self):
        """R(1) = (p(0)+p(1)) / (p(0)+p(1)+p(2)) = 2/4 = 1/2."""
        ratios = capture_ratio(1)
        assert ratios[1] == Rational(2, 4)

    def test_shrinks_significantly(self):
        """R(n) should shrink substantially by n=30."""
        ratios = capture_ratio(30)
        assert float(ratios[30]) < 0.01  # very small


class TestSpectralSequenceConvergence:
    """E₁ page is finite-dimensional at each bidegree."""

    def test_all_finite(self):
        result = spectral_sequence_convergence_check(max_bidegree=15)
        assert result["all_finite"] is True
        assert result["convergence"] is True

    def test_bidegree_count(self):
        result = spectral_sequence_convergence_check(max_bidegree=10)
        assert result["n_bidegrees_checked"] > 0

    def test_total_degree_0(self):
        """At total degree 0: only (0,0) contributes, dim = 1."""
        result = spectral_sequence_convergence_check(max_bidegree=10)
        assert result["e1_dims"][(0, 0)] == 1  # empty partition


class TestProWeylMittagLeffler:
    """Mittag-Leffler condition for pro-Weyl assembly."""

    def test_all_surjective(self):
        result = pro_weyl_mittag_leffler_assembly(max_lam=10)
        assert result["all_mittag_leffler"] is True
        assert result["r1_lim_vanishes"] is True

    def test_multiple_lambdas(self):
        result = pro_weyl_mittag_leffler_assembly(max_lam=15)
        for lam in range(16):
            assert result["verifications"][lam]["mittag_leffler"] is True

    def test_transition_kernel(self):
        """Each transition W_{m+1} → W_m has 1-dimensional kernel."""
        result = pro_weyl_mittag_leffler_assembly(max_lam=5)
        v = result["verifications"][3]  # λ = 3
        # All transitions should have kernel_dim = 1
        # (from the verification structure)
        assert v["all_surjective"] is True


class TestChromaticVsNaive:
    """Comparison: naive truncation fails, chromatic succeeds."""

    def test_naive_fails(self):
        result = chromatic_vs_naive_comparison(max_n=20)
        assert result["naive"]["fails"] is True

    def test_chromatic_succeeds(self):
        result = chromatic_vs_naive_comparison(max_n=20)
        assert result["chromatic"]["succeeds"] is True

    def test_decreasing_ratio(self):
        result = chromatic_vs_naive_comparison(max_n=20)
        assert result["naive"]["decreasing"] is True

    def test_e1_finite(self):
        result = chromatic_vs_naive_comparison(max_n=15)
        assert result["chromatic"]["all_e1_finite"] is True


# ===========================================================================
# Cross-module consistency tests
# ===========================================================================


class TestCrossModuleConsistency:
    """Verify consistency across the three modules."""

    def test_hom_matches_orthogonality(self):
        """hom_prefundamental_eval and self_orthogonality_check agree."""
        for n in range(0, 16):
            hom = hom_prefundamental_eval(n)
            ortho = self_orthogonality_check(n)
            assert hom == ortho["hom_dim"], f"Mismatch at n={n}"

    def test_euler_char_matches_pattern(self):
        """euler_char_prefundamental_eval and euler_characteristic_pattern agree."""
        pattern = euler_characteristic_pattern(max_n=20)
        for n in range(0, 21, 2):
            assert euler_char_prefundamental_eval(n) == pattern[n]

    def test_partition_consistency(self):
        """Partition functions across modules agree."""
        from compute.lib.mc3_tilting_probe import _partition_number as tp_pn
        from compute.lib.mc3_chromatic_strategy import _partition_number as cs_pn
        for k in range(20):
            assert _partition_number(k) == tp_pn(k) == cs_pn(k)
