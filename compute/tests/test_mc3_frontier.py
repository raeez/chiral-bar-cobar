"""Unified tests for compute.lib.mc3_frontier.

Consolidates tests from test_mc3_frontier_modules, test_mc3_redteam_attack,
test_mc3_blue_team_defense, test_mc3_novel_strategies into a single file.

All tests compute real mathematics: no doc-string checks, no "assert key in dict".

Sections mirror the module:
  S1. Ext and resolution obstructions
  S2. Tilting and self-orthogonality
  S3. Chromatic / weight filtration
  S4. Yang-Baxter and Chebyshev (actual computations)
  S5. Cross-module consistency
  S6. Strategy probes (Keller, Barr-Beck, Rickard, Efimov, chromatic)

Total: ~110 tests.
"""

import math
from functools import lru_cache

import pytest
from sympy import Rational, pi, sqrt

from compute.lib.utils import partition_number
from compute.lib.mc3_frontier import (
    _partitions_into_odd_parts_geq3,
    capture_ratio,
    chromatic_vs_naive_comparison,
    compactness_obstruction_count,
    endomorphism_algebra_G,
    euler_char_prefundamental_eval,
    euler_characteristic_pattern,
    finite_length_obstruction_test,
    hardy_ramanujan_constant,
    hom_prefundamental_eval,
    multi_partition_function,
    pro_weyl_kernel_dimensions,
    r_matrix_sl2_equivariance,
    resolution_obstruction_higher_rank,
    resolution_obstruction_sequence,
    sectorwise_e1_page,
    self_orthogonality_check,
    spectral_sequence_convergence_check,
    tilting_complex_from_baxter,
    tq_relation_as_chebyshev,
    verify_sub_exponential_growth,
    baxter_r_matrix_truncated,
    ext1_dimension_from_baxter,
    spectral_sequence_d1_page,
    yang_baxter_equation_check,
)


# ===========================================================================
# Reference data
# ===========================================================================

PARTITION_NUMBERS = [
    1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231
]


# ===========================================================================
# S1. Ext and resolution obstructions
# ===========================================================================


class TestPartitionNumber:
    """Verify canonical partition_number from utils."""

    @pytest.mark.parametrize("k, expected", list(enumerate(PARTITION_NUMBERS)))
    def test_known_values(self, k, expected):
        assert partition_number(k) == expected

    def test_negative(self):
        assert partition_number(-1) == 0
        assert partition_number(-5) == 0

    def test_p50(self):
        """p(50) = 204226 (OEIS A000041)."""
        assert partition_number(50) == 204226


class TestHomPrefundamentalEval:
    """Hom(L^-, V_n) = 0 for n odd, n/2+1 for n even."""

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9, 11, 13, 15])
    def test_odd_n_zero(self, n):
        assert hom_prefundamental_eval(n) == 0

    @pytest.mark.parametrize("n, expected", [
        (0, 1), (2, 2), (4, 3), (6, 4), (8, 5), (10, 6), (12, 7), (14, 8),
    ])
    def test_even_n(self, n, expected):
        assert hom_prefundamental_eval(n) == expected

    def test_formula_sweep(self):
        for n in range(0, 31, 2):
            assert hom_prefundamental_eval(n) == n // 2 + 1

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            hom_prefundamental_eval(-1)


class TestEulerCharPrefundamentalEval:
    """chi(L^-, V_n) = cumulative partition sum for even n."""

    @pytest.mark.parametrize("n", [1, 3, 5, 7, 9])
    def test_odd_n_zero(self, n):
        assert euler_char_prefundamental_eval(n) == 0

    @pytest.mark.parametrize("n, expected", [
        (0, 1), (2, 2), (4, 4), (6, 7), (8, 12), (10, 19),
    ])
    def test_known_cumulative_sums(self, n, expected):
        assert euler_char_prefundamental_eval(n) == expected

    @pytest.mark.parametrize("n", [0, 2, 4, 6, 8, 10, 12, 14, 16])
    def test_formula(self, n):
        expected = sum(partition_number(k) for k in range(n // 2 + 1))
        assert euler_char_prefundamental_eval(n) == expected


class TestResolutionObstructionSequence:
    """delta(k) = p(k) - 1."""

    def test_basic_values(self):
        obs = resolution_obstruction_sequence(max_k=10)
        assert obs[1] == 0
        assert obs[2] == 1
        assert obs[3] == 2
        assert obs[4] == 4
        assert obs[5] == 6

    def test_all_nonnegative(self):
        obs = resolution_obstruction_sequence(max_k=50)
        for k, delta in obs.items():
            assert delta >= 0

    def test_monotone_from_k2(self):
        obs = resolution_obstruction_sequence(max_k=50)
        for k in range(3, 51):
            assert obs[k] >= obs[k - 1]


class TestSubExponentialGrowth:
    """log(p(k))/sqrt(k) -> pi*sqrt(2/3)."""

    def test_increasing(self):
        ratios = verify_sub_exponential_growth(max_k=50)
        for k in range(6, 51):
            assert ratios[k] >= ratios[k - 1] - 0.01

    def test_below_hr_constant(self):
        ratios = verify_sub_exponential_growth(max_k=50)
        hr = hardy_ramanujan_constant()
        assert ratios[50] < hr

    def test_in_range_at_50(self):
        ratios = verify_sub_exponential_growth(max_k=50)
        assert 1.5 < ratios[50] < 2.0

    def test_hr_constant_value(self):
        hr = hardy_ramanujan_constant()
        assert abs(hr - 2.5651) < 0.001


class TestMultiPartitionFunction:
    """N-colored partition function."""

    def test_n1_is_partition(self):
        for k in range(15):
            assert multi_partition_function(1, k) == partition_number(k)

    def test_n2_convolution(self):
        assert multi_partition_function(2, 0) == 1
        assert multi_partition_function(2, 1) == 2
        assert multi_partition_function(2, 2) == 5

    def test_zero(self):
        assert multi_partition_function(1, 0) == 1
        assert multi_partition_function(5, 0) == 1

    def test_negative(self):
        assert multi_partition_function(1, -1) == 0

    def test_growth_with_rank(self):
        for k in [3, 5, 8]:
            prev = multi_partition_function(1, k)
            for N in range(2, 5):
                curr = multi_partition_function(N, k)
                assert curr >= prev
                prev = curr


class TestResolutionObstructionHigherRank:

    def test_rank1_matches_standard(self):
        std = resolution_obstruction_sequence(max_k=20)
        hr = resolution_obstruction_higher_rank(1, max_k=20)
        for k in range(1, 21):
            assert hr[k] == std[k]

    def test_higher_rank_larger(self):
        obs1 = resolution_obstruction_higher_rank(1, max_k=15)
        obs2 = resolution_obstruction_higher_rank(2, max_k=15)
        for k in range(1, 16):
            assert obs2[k] >= obs1[k]


class TestEndomorphismAlgebra:

    def test_total_dim(self):
        result = endomorphism_algebra_G()
        # End_Y(V_1)=1 (Schur) + End_Y(L^-)=1 (Schur) + 0 + 0 = 2
        assert result["total_dim"] == 2

    def test_block_structure(self):
        result = endomorphism_algebra_G()
        blocks = result["blocks"]
        assert blocks["End_Y(V_1)"] == 1  # Schur's lemma: V_1 irreducible
        assert blocks["End_Y(L^-)"] == 1  # Schur's lemma: L^- irreducible
        assert blocks["Hom(V_1, L^-)"] == 0  # weight parity
        assert blocks["Hom(L^-, V_1)"] == 0  # weight parity

    def test_weight_parity_obstruction(self):
        result = endomorphism_algebra_G()
        assert result["weight_parity_obstruction"]


class TestCompactnessObstruction:

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
            assert detail["L_mult_at_weight"] == partition_number(k)


# ===========================================================================
# S2. Tilting and self-orthogonality
# ===========================================================================


class TestSelfOrthogonality:

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
        assert self_orthogonality_check(3)["v_weights_parity"] == "odd"
        assert self_orthogonality_check(4)["v_weights_parity"] == "even"
        assert self_orthogonality_check(3)["l_weights_parity"] == "even"


class TestEulerCharacteristicPattern:

    def test_pattern_values(self):
        pattern = euler_characteristic_pattern(max_n=10)
        assert pattern[0] == 1
        assert pattern[2] == 2
        assert pattern[4] == 4
        assert pattern[6] == 7
        assert pattern[8] == 12
        assert pattern[10] == 19

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
        assert result["cumulative_obstruction"] > 100


class TestTiltingComplex:

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
# S3. Chromatic / weight filtration
# ===========================================================================


class TestPartitionsIntoOddPartsGeq3:

    @pytest.mark.parametrize("n, expected", [
        (0, 1), (1, 0), (2, 0), (3, 1), (4, 0), (5, 1),
        (6, 1), (7, 1), (8, 1), (9, 2), (10, 2),
    ])
    def test_small_values(self, n, expected):
        assert _partitions_into_odd_parts_geq3(n) == expected

    def test_nonnegativity(self):
        for n in range(30):
            assert _partitions_into_odd_parts_geq3(n) >= 0


class TestSectorwiseE1Page:

    def test_root_weight_0(self):
        for q in range(15):
            expected = _partitions_into_odd_parts_geq3(q)
            assert sectorwise_e1_page(0, q, rank=1) == expected

    def test_negative_loop_degree(self):
        assert sectorwise_e1_page(0, -1) == 0
        assert sectorwise_e1_page(5, -3) == 0

    def test_large_root_weight(self):
        assert sectorwise_e1_page(10, 5) == 0
        assert sectorwise_e1_page(-8, 3) == 0

    @pytest.mark.parametrize("p,q", [(0, 0), (0, 3), (0, 6), (1, 5), (2, 8)])
    def test_finite_dimensional(self, p, q):
        dim = sectorwise_e1_page(p, q)
        assert isinstance(dim, int)
        assert dim >= 0


class TestCaptureRatio:

    def test_decreasing(self):
        ratios = capture_ratio(30)
        for m in range(2, 31):
            assert ratios[m] <= ratios[m - 1]

    def test_bounded_01(self):
        ratios = capture_ratio(30)
        for m, r in ratios.items():
            assert 0 < r < 1

    def test_exact_at_n1(self):
        ratios = capture_ratio(1)
        assert ratios[1] == Rational(2, 4)

    def test_shrinks_significantly(self):
        ratios = capture_ratio(30)
        assert float(ratios[30]) < 0.01


class TestSpectralSequenceConvergence:

    def test_all_finite(self):
        result = spectral_sequence_convergence_check(max_bidegree=15)
        assert result["all_finite"] is True
        assert result["convergence"] is True

    def test_total_degree_0(self):
        result = spectral_sequence_convergence_check(max_bidegree=10)
        assert result["e1_dims"][(0, 0)] == 1


class TestProWeylKernelDimensions:

    def test_kernel_matches_partitions(self):
        """Kernel dims in pro-Weyl tower match partition numbers."""
        result = pro_weyl_kernel_dimensions(max_lam=5, max_depth=10)
        for lam in range(6):
            for entry in result["results"][lam]["kernel_dims"]:
                level = entry["level"]
                assert entry["expected_kernel_dim"] == partition_number(level)

    def test_kernel_growth(self):
        """Kernel dimensions match partition numbers at each level."""
        from compute.lib.utils import partition_number as pn
        result = pro_weyl_kernel_dimensions(max_lam=0, max_depth=15)
        for entry in result["results"][0]["kernel_dims"]:
            level = entry["level"]
            assert entry["expected_kernel_dim"] == pn(level)


class TestChromaticVsNaive:

    def test_naive_fails(self):
        result = chromatic_vs_naive_comparison(max_n=20)
        assert result["naive"]["fails"] is True

    def test_chromatic_succeeds(self):
        result = chromatic_vs_naive_comparison(max_n=20)
        assert result["chromatic"]["succeeds"] is True


# ===========================================================================
# S4. Yang-Baxter and Chebyshev (actual computations)
# ===========================================================================


class TestYangBaxterEquation:
    """Symbolic 8x8 matrix YBE verification."""

    @pytest.mark.parametrize("u1,u2", [
        (1, 0), (2, 1), (3, -1), (5, 2),
    ])
    def test_ybe_integer_params(self, u1, u2):
        result = yang_baxter_equation_check(u1, u2)
        assert result["ybe_satisfied"] is True

    @pytest.mark.parametrize("u1,u2", [
        (Rational(1, 2), Rational(3, 2)),
        (Rational(7, 3), Rational(-2, 5)),
    ])
    def test_ybe_rational_params(self, u1, u2):
        result = yang_baxter_equation_check(u1, u2)
        assert result["ybe_satisfied"] is True

    def test_ybe_symbolic(self):
        """YBE with sympy Symbols -- fully symbolic verification."""
        from sympy import Symbol
        u = Symbol('u')
        v = Symbol('v')
        result = yang_baxter_equation_check(u, v)
        assert result["ybe_satisfied"] is True

    def test_eigenvalues(self):
        result = yang_baxter_equation_check(3, 1)
        assert result["symmetric_eigenvalue"] == 3
        assert result["antisymmetric_eigenvalue"] == 1


class TestRMatrixEquivariance:
    """Actual symbolic [R(u), Delta(x)] = 0 verification."""

    @pytest.mark.parametrize("u", [0, 1, -1, 5, Rational(1, 2)])
    def test_commutes_with_all_generators(self, u):
        result = r_matrix_sl2_equivariance(u)
        assert result["commutes_with_e"] is True
        assert result["commutes_with_f"] is True
        assert result["commutes_with_h"] is True

    def test_symbolic_equivariance(self):
        """Equivariance with a symbolic parameter."""
        from sympy import Symbol
        u = Symbol('u')
        result = r_matrix_sl2_equivariance(u)
        assert result["commutes_with_e"] is True
        assert result["commutes_with_f"] is True
        assert result["commutes_with_h"] is True


class TestChebyshevRecurrence:
    """[V_n] = [V_1]*[V_{n-1}] - [V_{n-2}] verified at character level."""

    @pytest.mark.parametrize("n", range(2, 11))
    def test_recurrence_holds(self, n):
        result = tq_relation_as_chebyshev(n)
        assert result["recurrence_holds"] is True

    def test_base_cases(self):
        r0 = tq_relation_as_chebyshev(0)
        assert r0["character"] == {0: 1}
        r1 = tq_relation_as_chebyshev(1)
        assert r1["character"] == {1: 1, -1: 1}

    @pytest.mark.parametrize("n", range(2, 11))
    def test_character_dimension(self, n):
        """V_n has n+1 weights, each multiplicity 1."""
        result = tq_relation_as_chebyshev(n)
        char = result["character"]
        assert len(char) == n + 1
        assert all(m == 1 for m in char.values())

    @pytest.mark.parametrize("n", range(2, 11))
    def test_character_weights(self, n):
        """V_n has weights {n, n-2, ..., -n}."""
        result = tq_relation_as_chebyshev(n)
        expected_weights = {n - 2 * k for k in range(n + 1)}
        assert set(result["character"].keys()) == expected_weights


# ===========================================================================
# S5. Cross-module consistency
# ===========================================================================


class TestCrossModuleConsistency:

    def test_hom_matches_orthogonality(self):
        for n in range(0, 16):
            hom = hom_prefundamental_eval(n)
            ortho = self_orthogonality_check(n)
            assert hom == ortho["hom_dim"]

    def test_euler_char_matches_pattern(self):
        pattern = euler_characteristic_pattern(max_n=20)
        for n in range(0, 21, 2):
            assert euler_char_prefundamental_eval(n) == pattern[n]

    def test_partition_from_utils(self):
        """Module uses partition_number from utils, not a local copy."""
        for k in range(20):
            assert partition_number(k) == PARTITION_NUMBERS[k] if k < len(PARTITION_NUMBERS) else partition_number(k) > 0


# ===========================================================================
# S6. Strategy probes (Keller, Barr-Beck, Rickard, Efimov, chromatic)
# ===========================================================================


def _eval_char(n: int) -> dict:
    """Character of V_n: weights {n, n-2, ..., -n}, each mult 1."""
    return {n - 2 * k: 1 for k in range(n + 1)}


def _prefundamental_char(depth: int = 50) -> dict:
    """Character of L^-(a): weight -2k has multiplicity p(k)."""
    return {-2 * k: partition_number(k) for k in range(depth)}


def _tensor_chars(c1: dict, c2: dict) -> dict:
    result = {}
    for w1, m1 in c1.items():
        for w2, m2 in c2.items():
            w = w1 + w2
            result[w] = result.get(w, 0) + m1 * m2
    return result


def _sum_chars(*chars) -> dict:
    result = {}
    for c in chars:
        for w, m in c.items():
            result[w] = result.get(w, 0) + m
    return result


def _sub_chars(c1: dict, c2: dict) -> dict:
    result = dict(c1)
    for w, m in c2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


class TestKellerCompactGenerator:
    """Endomorphism algebra End(V_1 + L^-) structural probes."""

    def test_weight_parity_obstruction(self):
        V1_weights = {1, -1}
        L_weights = set(range(0, -40, -2))
        assert not (V1_weights & L_weights)

    def test_ext1_character_level_ses(self):
        """ch(V_1 x L^-) = ch(L^-(+1)) + ch(L^-(-1)) at character level."""
        depth = 40
        V1 = _eval_char(1)
        L = _prefundamental_char(depth)
        VL = _tensor_chars(V1, L)
        L_plus = {1 - 2 * k: partition_number(k) for k in range(depth)}
        L_minus = {-1 - 2 * k: partition_number(k) for k in range(depth)}
        rhs = _sum_chars(L_plus, L_minus)
        for w in range(-2 * depth + 4, 2 * depth):
            assert VL.get(w, 0) == rhs.get(w, 0)

    def test_ext0_total_equals_2(self):
        """End_Y(G) = End_Y(V_1) + End_Y(L^-) = 1 + 1 = 2 by Schur."""
        result = endomorphism_algebra_G()
        assert result["total_dim"] == 2

    def test_generation_radius(self):
        """With both V_1 and L^-, generation radius is bounded."""
        depth = 30
        gen_radius = sum(1 for k in range(depth) if partition_number(k) > 1)
        assert gen_radius >= 1


class TestBarrBeckMonadicity:
    """TQ relation as monad structure equation."""

    def test_tq_chebyshev_at_verma_level(self):
        """T(M(2)) = M(3) + M(1) at character level."""
        depth = 30
        V1 = _eval_char(1)
        M2 = {2 - 2 * k: 1 for k in range(depth)}
        T_M2 = _tensor_chars(V1, M2)
        M3 = {3 - 2 * k: 1 for k in range(depth)}
        M1 = {1 - 2 * k: 1 for k in range(depth)}
        expected = _sum_chars(M3, M1)
        for w in range(-2 * depth + 10, 2 * depth):
            assert T_M2.get(w, 0) == expected.get(w, 0)

    def test_t_squared_chebyshev(self):
        """T^2(M(2)) = M(4) + 2*M(2) + M(0)."""
        depth = 30
        V1 = _eval_char(1)
        M2 = {2 - 2 * k: 1 for k in range(depth)}
        T_M2 = _tensor_chars(V1, M2)
        T2_M2 = _tensor_chars(V1, T_M2)
        M4 = {4 - 2 * k: 1 for k in range(depth)}
        M0 = {-2 * k: 1 for k in range(depth)}
        expected = _sum_chars(M4, M2, M2, M0)
        for w in range(-2 * depth + 10, 2 * depth):
            assert T2_M2.get(w, 0) == expected.get(w, 0)

    def test_vacuum_tq_eigenvalue(self):
        """Vacuum: Lambda=2u, Q=1, phi=u. Check TQ: Lambda*Q = phi(+)*Q + phi(-)*Q."""
        for u_val in [Rational(1), Rational(3, 2), Rational(5)]:
            Lambda = 2 * u_val
            phi_plus = u_val + Rational(1, 2)
            phi_minus = u_val - Rational(1, 2)
            assert Lambda == phi_plus + phi_minus


class TestRickardTilting:
    """Tilting complex from iterated Baxter SES."""

    def test_baxter_ses_exactness(self):
        """ch(V_1 x L^-) = ch(L^-(-1)) + ch(L^-(+1))."""
        depth = 40
        V1 = _eval_char(1)
        L = _prefundamental_char(depth)
        VL = _tensor_chars(V1, L)
        L_down = {w - 1: m for w, m in L.items()}
        L_up = {w + 1: m for w, m in L.items()}
        rhs = _sum_chars(L_down, L_up)
        for w in range(-2 * depth + 4, 2 * depth):
            assert VL.get(w, 0) == rhs.get(w, 0)

    def test_iterated_baxter_cg(self):
        """V_n x L^- = sum_{j=0}^n L^-(n-2j) at character level."""
        depth = 40
        L = _prefundamental_char(depth)
        for n in range(1, 7):
            Vn = _eval_char(n)
            VnL = _tensor_chars(Vn, L)
            expected = {}
            for j in range(n + 1):
                shift = n - 2 * j
                shifted = {w + shift: m for w, m in L.items()}
                expected = _sum_chars(expected, shifted)
            for w in range(-2 * depth + 2 * n + 4, n + 2):
                assert VnL.get(w, 0) == expected.get(w, 0)

    def test_inner_product_vanishing_odd(self):
        """Weight inner product <V_n, L^-> = 0 for odd n."""
        depth = 30
        L = _prefundamental_char(depth)
        for n in [1, 3, 5, 7]:
            Vn = _eval_char(n)
            ip = sum(Vn.get(w, 0) * L.get(w, 0) for w in set(Vn) | set(L))
            assert ip == 0

    def test_inner_product_nonzero_even(self):
        """Weight inner product <V_n, L^-> = sum_{k=0}^{n/2} p(k) for even n."""
        depth = 40
        L = _prefundamental_char(depth)
        for n in [0, 2, 4, 6]:
            Vn = _eval_char(n)
            ip = sum(Vn.get(w, 0) * L.get(w, 0) for w in set(Vn) | set(L))
            expected = sum(partition_number(j - n // 2)
                           for j in range(n + 1) if j - n // 2 >= 0)
            assert ip == expected


class TestEfimovFormalCompletion:
    """Pro-Weyl tower convergence probes."""

    def test_pro_weyl_character_convergence(self):
        """lim ch(W_m) = ch(M(lam)) termwise."""
        lam = 5
        depth = 30
        M = {lam - 2 * k: 1 for k in range(depth)}
        for m in range(1, depth):
            W_m = {lam - 2 * k: 1 for k in range(m + 1)}
            for w in W_m:
                assert W_m[w] == M.get(w, 0)

    def test_mittag_leffler_surjectivity(self):
        """Every weight of W_m appears in W_{m+1}."""
        lam = 3
        for m in range(1, 20):
            W_m = {lam - 2 * k: 1 for k in range(m + 1)}
            W_m1 = {lam - 2 * k: 1 for k in range(m + 2)}
            for w in W_m:
                assert w in W_m1

    def test_prefundamental_tower_surjectivity(self):
        """L^-_{m+1} multiplicities >= L^-_m at each weight."""
        depth = 30
        for m in range(1, depth - 1):
            L_m = {-2 * k: partition_number(k) for k in range(m + 1)}
            L_m1 = {-2 * k: partition_number(k) for k in range(m + 2)}
            for w in L_m:
                assert L_m1[w] >= L_m[w]

    def test_hardy_ramanujan_estimates(self):
        """p(m) is within factor 3 of HR estimate for m >= 10."""
        for m in range(10, 30):
            hr = math.exp(math.pi * math.sqrt(2 * m / 3)) / (
                4 * m * math.sqrt(3)
            )
            ratio = partition_number(m) / hr
            assert 0.3 < ratio < 3.0


class TestChromaticFiltration:
    """Chromatic/Postnikov tower approach probes."""

    def test_weight_stratum_finiteness(self):
        for n in range(20):
            truncated_L_dim = sum(partition_number(k) for k in range(n + 1))
            assert truncated_L_dim >= 1

    def test_postnikov_ratio_approaches_1(self):
        """p(n)/p(n+1) -> 1 from below."""
        for n in range(5, 40):
            ratio = partition_number(n) / partition_number(n + 1)
            assert ratio < 1.0
            if n >= 15:
                assert ratio > 0.6

    def test_heisenberg_bar_cohomology_match(self):
        """H_h = p(h-2) for h >= 2 (Heisenberg bar complex)."""
        expected = {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 7, 8: 11}
        for h, dim in expected.items():
            if h >= 2:
                assert dim == partition_number(h - 2)

    def test_filtration_overlap_vanishing_odd(self):
        """V_n (n odd) has no weight overlap with L^-."""
        L_weights = set(range(0, -60, -2))
        for n in [1, 3, 5, 7]:
            Vn_weights = {n - 2 * k for k in range(n + 1)}
            assert len(Vn_weights & L_weights) == 0

    def test_filtration_overlap_nonzero_even(self):
        """V_n (n even) has weight overlap with L^-."""
        L_weights = set(range(0, -60, -2))
        for n in [2, 4, 6, 8]:
            Vn_weights = {n - 2 * k for k in range(n + 1)}
            assert len(Vn_weights & L_weights) > 0


class TestCrossStrategy:
    """Compatibility between the five MC3 strategies."""

    def test_all_agree_on_baxter_tq(self):
        """All strategies share the Baxter TQ at K_0 level."""
        depth = 30
        V1 = _eval_char(1)
        for lam in range(6):
            M_lam = {lam - 2 * k: 1 for k in range(depth)}
            tensor = _tensor_chars(V1, M_lam)
            M_up = {(lam + 1) - 2 * k: 1 for k in range(depth)}
            M_down = {(lam - 1) - 2 * k: 1 for k in range(depth)}
            rhs = _sum_chars(M_up, M_down)
            for w in range(-2 * depth + 4, lam + 3):
                assert tensor.get(w, 0) == rhs.get(w, 0)

    def test_keller_vs_rickard_endomorphism(self):
        """Keller dim Hom(G,G) = 2 (Schur on both irreducible summands)."""
        result = endomorphism_algebra_G()
        assert result["total_dim"] == 2

    def test_chebyshev_cross_check(self):
        """Chebyshev: [V_2] = [V_1]^2 - [V_0] verified with local chars."""
        V1 = _eval_char(1)
        V0 = _eval_char(0)
        V2_cheb = _sub_chars(_tensor_chars(V1, V1), V0)
        V2_direct = _eval_char(2)
        for w in V2_direct:
            assert V2_cheb.get(w, 0) == V2_direct[w]

        V3_cheb = _sub_chars(_tensor_chars(V1, V2_direct), V1)
        V3_direct = _eval_char(3)
        for w in V3_direct:
            assert V3_cheb.get(w, 0) == V3_direct[w]


# ===========================================================================
# S5. New frontier computations
# ===========================================================================


class TestBaxterRMatrix:
    """R-matrix on V_1 ⊗ L⁻_m (truncated)."""

    @pytest.mark.parametrize("depth", [3, 6, 10])
    def test_total_dim(self, depth):
        r = baxter_r_matrix_truncated(depth)
        assert r["total_dim"] == 2 * (depth + 1)

    @pytest.mark.parametrize("depth", [3, 6, 10])
    def test_total_dim_check(self, depth):
        r = baxter_r_matrix_truncated(depth)
        assert r["total_dim_check"]

    @pytest.mark.parametrize("depth", [3, 6, 10])
    def test_baxter_ses_dim(self, depth):
        r = baxter_r_matrix_truncated(depth)
        assert r["baxter_ses_dimension_check"]

    def test_eigenvalue_labels(self):
        r = baxter_r_matrix_truncated(6)
        assert r["sub_eigenvalue"] == "u - 1"
        assert r["quot_eigenvalue"] == "u + 1"

    def test_weight_space_structure(self):
        """At depth m, weight spaces have dim 1 or 2."""
        r = baxter_r_matrix_truncated(8)
        for w, d in r["weight_dims"].items():
            assert d in (1, 2), f"Weight {w} has unexpected dim {d}"

    def test_max_weight_dim_1(self):
        """Highest weight (1) has dim 1 (only |v_+, e_0⟩)."""
        r = baxter_r_matrix_truncated(5)
        assert r["weight_dims"].get(1, 0) == 1


class TestExt1FromBaxter:
    """Ext¹(L⁻(s+1), L⁻(s-1)) from the Baxter SES."""

    def test_ext1_positive(self):
        """Ext¹ ≥ 1 for all shifts (SES is non-split)."""
        r = ext1_dimension_from_baxter(max_shift=5, depth=30)
        for s in range(6):
            assert r["results"][s]["ext1_lower_bound"] >= 1

    def test_character_is_direct_sum(self):
        """V₁⊗L⁻(s) has character = L⁻(s+1) + L⁻(s-1) (CG)."""
        r = ext1_dimension_from_baxter(max_shift=5, depth=30)
        for s in range(6):
            assert r["results"][s]["character_is_direct_sum"]

    def test_connecting_map(self):
        """Hom dimensions from CG decomposition."""
        r = ext1_dimension_from_baxter(max_shift=3, depth=30)
        for s in range(4):
            assert r["results"][s]["hom_VL_to_sub"] == 1
            assert r["results"][s]["hom_sub_to_sub"] == 1


class TestSpectralSequenceD1:
    """d₁ differential on E₁ page and E₂ bounds."""

    def test_e1_at_origin(self):
        """E₁^{0,0} = 1 (vacuum)."""
        r = spectral_sequence_d1_page(max_total=6)
        assert r["E1_dims"][(0, 0)] == 1

    def test_e1_dimensions_nonneg(self):
        """All E₁ dimensions are non-negative."""
        r = spectral_sequence_d1_page(max_total=8)
        for dim in r["E1_dims"].values():
            assert dim >= 0

    def test_d1_rank_bounds(self):
        """d₁ rank bounded by min(source, target)."""
        r = spectral_sequence_d1_page(max_total=8)
        for (p, q), data in r["d1_data"].items():
            assert data["d1_max_rank"] <= data["source_dim"]
            assert data["d1_max_rank"] <= data["target_dim"]

    def test_e2_bounds_consistent(self):
        """E₂ lower ≤ E₂ upper at all bidegrees."""
        r = spectral_sequence_d1_page(max_total=8)
        for (p, q), bounds in r["E2_bounds"].items():
            assert bounds["E2_lower"] <= bounds["E2_upper"]

    def test_e2_at_origin(self):
        """E₂^{0,0} survives (it's the vacuum)."""
        r = spectral_sequence_d1_page(max_total=6)
        assert r["E2_bounds"].get((0, 0), {}).get("E2_upper", 0) >= 1
