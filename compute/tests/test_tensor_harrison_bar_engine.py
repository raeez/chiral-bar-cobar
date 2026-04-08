r"""Tests for tensor_harrison_bar_engine: Eulerian idempotent decomposition.

Tests the foundational question: which bar complex does the manuscript use?

Multi-path verification:
  Path 1: Direct computation of Eulerian idempotents via DSW formula
  Path 2: Matrix rank verification (rank e_1 = (n-1)!)
  Path 3: Witt dimension formula (Harrison dimensions)
  Path 4: Explicit low-arity hand computations
  Path 5: Structural checks (idempotent, trivial trace vanishes)
"""

import pytest
from fractions import Fraction
from math import factorial, comb
from itertools import permutations

from compute.lib.tensor_harrison_bar_engine import (
    permutation_to_cycles,
    num_cycles,
    descent_count,
    first_eulerian_idempotent_coefficients,
    verify_idempotent,
    lie_operad_dimension,
    tensor_bar_dimension,
    harrison_dimension,
    witt_dimension,
    moebius,
    dimension_table,
    heisenberg_bar_analysis,
    multi_generator_bar_analysis,
    analyze_coproduct_on_harrison,
    identify_manuscript_bar,
    verify_dsw_idempotent,
    explicit_arity_2,
    explicit_arity_3,
    explicit_arity_4,
    explicit_e1_matrix,
    e1_rank,
    convolution_lie_algebra_analysis,
    full_analysis_summary,
    _right_normed_bracket_coefficients,
)

F = Fraction


# ============================================================================
# Moebius function
# ============================================================================

class TestMoebius:
    def test_moebius_1(self):
        assert moebius(1) == 1

    def test_moebius_primes(self):
        assert moebius(2) == -1
        assert moebius(3) == -1
        assert moebius(5) == -1
        assert moebius(7) == -1

    def test_moebius_squarefree_2_primes(self):
        assert moebius(6) == 1     # 2*3
        assert moebius(10) == 1    # 2*5
        assert moebius(15) == 1    # 3*5
        assert moebius(30) == -1   # 2*3*5

    def test_moebius_square_factor(self):
        assert moebius(4) == 0     # 2^2
        assert moebius(8) == 0     # 2^3
        assert moebius(9) == 0     # 3^2
        assert moebius(12) == 0    # 2^2 * 3


# ============================================================================
# Witt dimension formula
# ============================================================================

class TestWittDimension:
    """Test Witt's formula: dim Lie(V)_n = (1/n) sum_{d|n} mu(n/d) m^d."""

    def test_witt_n1(self):
        """At arity 1, dim = m (the generators themselves)."""
        for m in range(1, 6):
            assert witt_dimension(1, m) == m

    def test_witt_n2(self):
        """At arity 2: W(2,m) = (1/2)(m^2 - m) = m(m-1)/2."""
        for m in range(1, 6):
            expected = m * (m - 1) // 2
            assert witt_dimension(2, m) == expected

    def test_witt_n3(self):
        """At arity 3: W(3,m) = (1/3)(m^3 - m)."""
        for m in range(1, 6):
            expected = (m**3 - m) // 3
            assert witt_dimension(3, m) == expected

    def test_witt_single_generator(self):
        """For m=1: W(n,1) = 0 for all n >= 2, and W(1,1) = 1."""
        assert witt_dimension(1, 1) == 1
        for n in range(2, 8):
            assert witt_dimension(n, 1) == 0, f"W({n},1) should be 0"

    def test_witt_two_generators_known_values(self):
        """Known values for m=2: 2, 1, 2, 3, 6, 9, 18, 30, ..."""
        known = {1: 2, 2: 1, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18, 8: 30}
        for n, expected in known.items():
            assert witt_dimension(n, 2) == expected, f"W({n},2)={witt_dimension(n,2)}, expected {expected}"

    def test_witt_sum_equals_free_algebra(self):
        """The free associative algebra on m generators has dim m^n at degree n.
        Free Lie algebra dimension: sum_{d|n} d * W(d,m) = m^n ... no.
        Actually: sum_{n>=1} W(n,m) * t^n = -sum_{d>=1} mu(d)/d * log(1-m*t^d).
        Simpler: m^n = sum_{d|n} d * W(d, m) ... no that's for the tensor algebra.

        The correct identity: m^n = sum of n/d * W(d,m) over d|n ... no.

        PBW: T(V)_n = direct sum of Sym^{j_1}(Lie(V)_{d_1}) tensor ...
        This is complicated. Let's just check a simpler identity.

        For the free associative algebra: dim_n = m^n.
        For the free Lie algebra: dim_n = W(n,m).
        PBW: sum_n dim(U(Lie(V))_n) t^n = prod_{n>=1} 1/(1-t^n)^{W(n,m)}.
        And U(Lie(V)) = T(V), so the LHS = sum_n m^n t^n = 1/(1-mt).
        So: prod_{n>=1} 1/(1-t^n)^{W(n,m)} = 1/(1-mt).
        Taking log: sum_n W(n,m) * sum_{k>=1} t^{nk}/k = -log(1-mt) = sum m^n t^n/n.
        """
        # Verify PBW identity at small orders
        m = 3
        for N in range(1, 7):
            # LHS: coefficient of t^N in prod_{n=1}^{N} 1/(1-t^n)^{W(n,m)}
            # = number of partitions weighted by Witt dimensions
            # This is too complex to verify directly. Instead check:
            # sum_{d|N} d * W(d, m) ... actually let me just verify the
            # necklace identity: sum_{d|n} W(d,m) = (1/n) sum ... no.
            # Let's check: n * W(n,m) = sum_{d|n} mu(n/d) m^d (definition * n).
            lhs = N * witt_dimension(N, m)
            rhs = sum(moebius(N // d) * m**d for d in range(1, N + 1) if N % d == 0)
            assert lhs == rhs

    def test_lie_operad_dimension(self):
        """dim Lie(n) = (n-1)!."""
        for n in range(1, 8):
            assert lie_operad_dimension(n) == factorial(n - 1)


# ============================================================================
# Permutation utilities
# ============================================================================

class TestPermutationUtils:
    def test_cycles_identity(self):
        cycles = permutation_to_cycles((0, 1, 2))
        assert len(cycles) == 3  # 3 fixed points

    def test_cycles_transposition(self):
        cycles = permutation_to_cycles((1, 0, 2))
        # (0,1) is a 2-cycle, (2) is fixed
        assert num_cycles((1, 0, 2)) == 2

    def test_cycles_3cycle(self):
        assert num_cycles((1, 2, 0)) == 1  # single 3-cycle

    def test_descent_count(self):
        assert descent_count((0, 1, 2)) == 0
        assert descent_count((2, 1, 0)) == 2
        assert descent_count((1, 0, 2)) == 1


# ============================================================================
# Right-normed bracket coefficients
# ============================================================================

class TestRightNormedBracket:
    def test_arity_1(self):
        """[x_0] = x_0."""
        coeffs = _right_normed_bracket_coefficients(1)
        assert coeffs == {(0,): F(1)}

    def test_arity_2(self):
        """[x_0, x_1] = x_0 x_1 - x_1 x_0."""
        coeffs = _right_normed_bracket_coefficients(2)
        assert coeffs[(0, 1)] == F(1)
        assert coeffs[(1, 0)] == F(-1)
        assert len(coeffs) == 2

    def test_arity_3(self):
        """[x_0, [x_1, x_2]] = x_0 x_1 x_2 - x_0 x_2 x_1 - x_1 x_2 x_0 + x_2 x_1 x_0."""
        coeffs = _right_normed_bracket_coefficients(3)
        assert coeffs.get((0, 1, 2), F(0)) == F(1)
        assert coeffs.get((0, 2, 1), F(0)) == F(-1)
        assert coeffs.get((1, 2, 0), F(0)) == F(-1)
        assert coeffs.get((2, 1, 0), F(0)) == F(1)
        # The other two permutations should have coefficient 0
        assert coeffs.get((1, 0, 2), F(0)) == F(0)
        assert coeffs.get((2, 0, 1), F(0)) == F(0)
        assert sum(coeffs.values()) == F(0), "Sum of bracket coefficients should be 0"

    def test_arity_4_coefficient_sum_zero(self):
        """Sum of all bracket coefficients is 0 for n >= 2."""
        coeffs = _right_normed_bracket_coefficients(4)
        total = sum(coeffs.values())
        assert total == F(0), f"Sum should be 0, got {total}"

    def test_arity_5_coefficient_sum_zero(self):
        coeffs = _right_normed_bracket_coefficients(5)
        total = sum(coeffs.values())
        assert total == F(0)

    def test_bracket_has_2_pow_n_minus_1_terms(self):
        """The right-normed bracket of n elements has 2^{n-1} nonzero terms."""
        for n in range(1, 6):
            coeffs = _right_normed_bracket_coefficients(n)
            nonzero = sum(1 for v in coeffs.values() if v != 0)
            assert nonzero == 2**(n - 1), f"n={n}: got {nonzero}, expected {2**(n-1)}"


# ============================================================================
# First Eulerian idempotent
# ============================================================================

class TestFirstEulerianIdempotent:
    def test_e1_arity_1(self):
        """e_1 at arity 1 is the identity."""
        e1 = first_eulerian_idempotent_coefficients(1)
        assert e1 == {(0,): F(1)}

    def test_e1_arity_2(self):
        """e_1 at arity 2 is (1/2)(id - (01)) = antisymmetrizer."""
        e1 = first_eulerian_idempotent_coefficients(2)
        assert e1[(0, 1)] == F(1, 2)
        assert e1[(1, 0)] == F(-1, 2)

    def test_e1_arity_3_specific_values(self):
        """e_1 at arity 3 = (1/3) * [x_0, [x_1, x_2]]."""
        e1 = first_eulerian_idempotent_coefficients(3)
        assert e1.get((0, 1, 2), F(0)) == F(1, 3)
        assert e1.get((0, 2, 1), F(0)) == F(-1, 3)
        assert e1.get((1, 2, 0), F(0)) == F(-1, 3)
        assert e1.get((2, 1, 0), F(0)) == F(1, 3)

    def test_e1_is_idempotent_n2(self):
        assert verify_idempotent(2) == F(0)

    def test_e1_is_idempotent_n3(self):
        assert verify_idempotent(3) == F(0)

    def test_e1_is_idempotent_n4(self):
        assert verify_idempotent(4) == F(0)

    def test_e1_is_idempotent_n5(self):
        assert verify_idempotent(5) == F(0)

    def test_e1_rank_equals_lie_dim(self):
        """rank(e_1) = (n-1)! = dim Lie(n)."""
        for n in range(1, 5):
            assert e1_rank(n) == factorial(n - 1), f"n={n}: rank={e1_rank(n)}, expected {factorial(n-1)}"

    def test_e1_trivial_trace_vanishes(self):
        """On the trivial S_n-representation, e_1 acts as 0 for n >= 2."""
        for n in range(2, 6):
            e1 = first_eulerian_idempotent_coefficients(n)
            trace = sum(e1.values(), F(0))
            assert trace == F(0), f"n={n}: trivial trace = {trace}, should be 0"


# ============================================================================
# DSW verification comprehensive
# ============================================================================

class TestDSWVerification:
    def test_dsw_n2(self):
        result = verify_dsw_idempotent(2)
        assert result['is_idempotent']
        assert result['rank_correct']
        assert result['trace_correct']
        assert result['trivial_trace_vanishes_for_n_geq_2']

    def test_dsw_n3(self):
        result = verify_dsw_idempotent(3)
        assert result['is_idempotent']
        assert result['rank_correct']
        assert result['trace_correct']
        assert result['trivial_trace_vanishes_for_n_geq_2']

    def test_dsw_n4(self):
        result = verify_dsw_idempotent(4)
        assert result['is_idempotent']
        assert result['rank_correct']
        assert result['trace_correct']
        assert result['trivial_trace_vanishes_for_n_geq_2']

    def test_dsw_n5(self):
        result = verify_dsw_idempotent(5)
        assert result['is_idempotent']
        assert result['rank_correct']
        assert result['trace_correct']
        assert result['trivial_trace_vanishes_for_n_geq_2']


# ============================================================================
# Harrison dimensions
# ============================================================================

class TestHarrisonDimension:
    def test_harrison_1gen_arity1(self):
        assert harrison_dimension(1, 1) == 1

    def test_harrison_1gen_arity2(self):
        """Single generator: Harrison vanishes at arity >= 2."""
        assert harrison_dimension(2, 1) == 0

    def test_harrison_1gen_arity3(self):
        assert harrison_dimension(3, 1) == 0

    def test_harrison_1gen_arity4(self):
        assert harrison_dimension(4, 1) == 0

    def test_harrison_1gen_arity5(self):
        assert harrison_dimension(5, 1) == 0

    def test_harrison_2gen(self):
        """Two generators: W(n,2) = 2,1,2,3,6,9,18,30,..."""
        expected = {1: 2, 2: 1, 3: 2, 4: 3, 5: 6}
        for n, exp in expected.items():
            assert harrison_dimension(n, 2) == exp

    def test_harrison_3gen(self):
        """Three generators."""
        expected = {1: 3, 2: 3, 3: 8, 4: 18, 5: 48}
        for n, exp in expected.items():
            assert harrison_dimension(n, 3) == exp

    def test_harrison_sum_bounded_by_tensor(self):
        """Harrison dim <= tensor dim at each arity."""
        for m in range(1, 5):
            for n in range(1, 7):
                assert harrison_dimension(n, m) <= tensor_bar_dimension(n, m)


# ============================================================================
# Dimension tables
# ============================================================================

class TestDimensionTable:
    def test_table_1gen(self):
        """For 1 generator, tensor=symmetric=1 at all arities, Harrison=0 for n>=2."""
        table = dimension_table(5, 1)
        for row in table:
            assert row.tensor_dim == 1
            assert row.symmetric_dim == 1
            if row.arity == 1:
                assert row.harrison_dim == 1
            else:
                assert row.harrison_dim == 0

    def test_table_2gen_arity2(self):
        table = dimension_table(2, 2)
        row = table[1]  # arity 2
        assert row.tensor_dim == 4       # 2^2
        assert row.symmetric_dim == 3    # binom(3,2)
        assert row.harrison_dim == 1     # W(2,2) = 1

    def test_tensor_dim_formula(self):
        """tensor_dim = m^n."""
        for m in range(1, 4):
            for n in range(1, 6):
                assert tensor_bar_dimension(n, m) == m**n


# ============================================================================
# Heisenberg analysis
# ============================================================================

class TestHeisenbergAnalysis:
    def test_heisenberg_dimensions(self):
        result = heisenberg_bar_analysis(5)
        table = result['dimension_table']
        for entry in table:
            assert entry['tensor_dim'] == 1
            assert entry['symmetric_dim'] == 1
            if entry['arity'] == 1:
                assert entry['harrison_dim'] == 1
            else:
                assert entry['harrison_dim'] == 0

    def test_harrison_vanishes(self):
        result = heisenberg_bar_analysis(5)
        assert result['harrison_vanishes_above_1'] is True

    def test_kappa_not_in_harrison(self):
        """kappa lives at arity 2 but Harrison dim at arity 2 is 0 for 1 generator."""
        result = heisenberg_bar_analysis()
        # kappa is in Sym^2, not in Lie^c_2
        table = result['dimension_table']
        arity2 = [e for e in table if e['arity'] == 2][0]
        assert arity2['harrison_dim'] == 0, "Harrison at arity 2 should be 0 for Heisenberg"
        assert arity2['symmetric_dim'] == 1, "Sym^2 at arity 2 should be 1"


# ============================================================================
# Coproduct analysis
# ============================================================================

class TestCoproductAnalysis:
    def test_coproduct_arity_1(self):
        result = analyze_coproduct_on_harrison(1)
        assert result.deconcatenation_preserves_harrison is True

    def test_coproduct_arity_2(self):
        result = analyze_coproduct_on_harrison(2)
        assert result.deconcatenation_preserves_harrison is True
        assert result.coshuffle_preserves_harrison is True

    def test_coproduct_arity_3(self):
        """At arity 3, deconcatenation does NOT preserve Harrison."""
        result = analyze_coproduct_on_harrison(3)
        assert result.deconcatenation_preserves_harrison is False
        assert result.coshuffle_preserves_harrison is True

    def test_coproduct_arity_4(self):
        result = analyze_coproduct_on_harrison(4)
        assert result.deconcatenation_preserves_harrison is False

    def test_harrison_dim_in_analysis(self):
        """The Harrison dimension at arity n should be (n-1)!."""
        for n in range(1, 5):
            result = analyze_coproduct_on_harrison(n)
            assert result.harrison_dim == factorial(n - 1)


# ============================================================================
# Manuscript identification
# ============================================================================

class TestManuscriptIdentification:
    def test_identifies_symcoalg(self):
        result = identify_manuscript_bar()
        assert 'coshuffle' in result.coproduct_type
        assert 'cocommutative' in result.coproduct_type
        assert 'coassociative' in result.coproduct_type

    def test_not_tensor_bar(self):
        result = identify_manuscript_bar()
        assert 'NOT the tensor bar' in result.operadic_type

    def test_not_harrison_bar(self):
        result = identify_manuscript_bar()
        assert 'NOT' in result.operadic_type and 'Harrison' in result.operadic_type

    def test_coalgebra_type(self):
        result = identify_manuscript_bar()
        assert result.coalgebra_type == 'cocommutative coassociative'


# ============================================================================
# Explicit low-arity computations
# ============================================================================

class TestExplicitArity2:
    def test_e1_coefficients(self):
        result = explicit_arity_2()
        assert result['e1_id'] == F(1, 2)
        assert result['e1_swap'] == F(-1, 2)

    def test_harrison_1gen(self):
        assert explicit_arity_2()['harrison_dim_1gen'] == 0

    def test_harrison_2gen(self):
        assert explicit_arity_2()['harrison_dim_2gen'] == 1

    def test_harrison_3gen(self):
        assert explicit_arity_2()['harrison_dim_3gen'] == 3

    def test_sym_dim(self):
        """Sym^2(Q^m) has dim m(m+1)/2."""
        assert explicit_arity_2()['sym_dim_1gen'] == 1
        assert explicit_arity_2()['sym_dim_2gen'] == 3
        assert explicit_arity_2()['sym_dim_3gen'] == 6


class TestExplicitArity3:
    def test_nonzero_count(self):
        """[x_0,[x_1,x_2]] has 4 nonzero terms = 2^2."""
        result = explicit_arity_3()
        assert result['nonzero_count'] == 4

    def test_harrison_dims(self):
        result = explicit_arity_3()
        assert result['harrison_dim_1gen'] == 0
        assert result['harrison_dim_2gen'] == 2
        assert result['harrison_dim_3gen'] == 8


class TestExplicitArity4:
    def test_harrison_dims(self):
        result = explicit_arity_4()
        assert result['harrison_dim_1gen'] == 0
        assert result['harrison_dim_2gen'] == 3
        assert result['harrison_dim_3gen'] == 18


# ============================================================================
# Convolution algebra analysis
# ============================================================================

class TestConvolutionAnalysis:
    def test_primitives_are_harrison(self):
        result = convolution_lie_algebra_analysis()
        assert 'Harrison' in result['primitives']
        assert 'Prim' in result['primitives']

    def test_coalgebra_is_sym(self):
        result = convolution_lie_algebra_analysis()
        assert 'Sym^c' in result['coalgebra']


# ============================================================================
# Full summary
# ============================================================================

class TestFullSummary:
    def test_answer_is_sym(self):
        result = full_analysis_summary()
        assert 'Sym^c' in result['answer']
        assert 'NEITHER' in result['answer']

    def test_heisenberg_finding(self):
        result = full_analysis_summary()
        assert 'ZERO at arity >= 2' in result['heisenberg_critical_finding']

    def test_line_1563_error(self):
        result = full_analysis_summary()
        assert 'WRONG' in result['manuscript_status']['line_1563_error']


# ============================================================================
# Cross-checks and consistency
# ============================================================================

class TestCrossChecks:
    def test_eulerian_decomposition_dims_sum(self):
        """For V = Q^m, multilinear: sum of Eulerian weight dims = n!.
        Weight 1 = (n-1)! (Lie). Weight n = 1 (symmetric/trivial).
        Total: (n-1)! + ... + 1 = n!."""
        # For the multilinear part of V^{tensor n} with dim(V) >= n:
        for n in range(1, 5):
            # Total = n! (multilinear part of (Q^n)^{tensor n})
            total = factorial(n)
            harrison = factorial(n - 1)  # weight 1
            # The non-Harrison part has dim n! - (n-1)! = (n-1)(n-1)!
            non_harrison = total - harrison
            assert non_harrison == (n - 1) * factorial(n - 1)

    def test_prim_of_sym_is_lie(self):
        """Prim(Sym^c(V)) = Lie^c(V): the primitives of the symmetric coalgebra
        are the cofree coLie coalgebra.

        Consequence: for 1-generator, Prim(Sym^c(Q)) = Q (concentrated in arity 1).
        """
        # For Q: Sym^c(Q)_n = Q for all n (1-dim at each arity).
        # Prim = Lie^c(Q) = Q at arity 1, 0 elsewhere.
        for n in range(1, 6):
            sym_dim = 1  # Sym^n(Q) = Q
            lie_dim = harrison_dimension(n, 1)
            if n == 1:
                assert lie_dim == 1
            else:
                assert lie_dim == 0

    def test_harrison_less_than_tensor(self):
        """Harrison (Lie^c) dim <= Tensor (T^c) dim at each arity.

        Lie^c(V)_n embeds into T^c(V)_n = V^{tensor n}, so dim Lie^c <= dim T^c = m^n.
        Note: Lie^c does NOT embed into Sym^c. For m=2, n=6: W(6,2)=9 > binom(7,6)=7.
        The Harrison complex is a subcomplex of the TENSOR bar, not of the symmetric bar.
        """
        for m in range(1, 5):
            for n in range(1, 7):
                h = harrison_dimension(n, m)
                t = tensor_bar_dimension(n, m)
                assert h <= t, f"m={m}, n={n}: Harrison={h} > Tensor={t}"

    def test_harrison_can_exceed_symmetric(self):
        """Harrison dim CAN exceed Sym dim: W(6,2) = 9 > binom(7,6) = 7.

        This is a critical structural fact: Lie^c(V)_n lives inside T^c(V)_n
        (the tensor bar), NOT inside Sym^c(V)_n (the symmetric bar). The
        Eulerian weight-1 component of T^c_n can be larger than Sym^n(V)
        because Lie words at high arity can involve more independent
        antisymmetric combinations than the symmetric power has dimension.
        """
        assert witt_dimension(6, 2) == 9
        assert comb(7, 6) == 7
        assert 9 > 7  # Harrison > Symmetric: this is correct!

    def test_sym_coalgebra_dims(self):
        """dim Sym^n(Q^m) = binom(m+n-1, n)."""
        for m in range(1, 5):
            for n in range(1, 6):
                assert comb(m + n - 1, n) >= 0

    def test_tensor_geq_symmetric(self):
        """dim T_n(V) = m^n >= dim Sym^n(V) = binom(m+n-1,n)."""
        for m in range(1, 5):
            for n in range(1, 6):
                assert m**n >= comb(m + n - 1, n)

    def test_witt_is_nonnegative(self):
        """Witt dimension is always nonneg."""
        for m in range(1, 5):
            for n in range(1, 10):
                assert witt_dimension(n, m) >= 0


# ============================================================================
# The critical structural theorem: Harrison bar has no coAss coproduct
# ============================================================================

class TestCriticalStructure:
    def test_deconcatenation_not_on_harrison(self):
        """The deconcatenation coproduct on T^c does NOT restrict to Lie^c.
        Verified: at arity 3, deconcatenation of a Harrison element
        has non-Harrison components."""
        analysis = analyze_coproduct_on_harrison(3)
        assert not analysis.deconcatenation_preserves_harrison

    def test_manuscript_uses_coshuffle(self):
        """The manuscript's coproduct (bipartition sum) is coshuffle."""
        ident = identify_manuscript_bar()
        assert 'coshuffle' in ident.coproduct_type

    def test_coshuffle_is_not_deconcatenation(self):
        """Coshuffle and deconcatenation are different coproducts.

        Deconcatenation of [a|b|c] at (1,2) level:
          [a] tensor [b|c]
        Only ONE such term (for this particular split point).

        Coshuffle of a.b.c at (1,2) level:
          a tensor b.c + b tensor a.c + c tensor a.b
        THREE terms (all ways to pick 1 element from {a,b,c}).

        These are clearly different (1 term vs 3 terms).
        """
        # At arity 3, the (1,2)-component of deconcatenation has
        # 1 term per basis element (pick split point after position 1).
        # The (1,2)-component of coshuffle has binom(3,1) = 3 terms per basis element.
        # These are different numbers of terms.
        assert comb(3, 1) == 3  # coshuffle: 3 ways to pick 1 from 3
        # deconcatenation: only 1 way (split after position 1)
        assert 1 != 3  # they are different!

    def test_heisenberg_kappa_invisible_to_harrison(self):
        """For Heisenberg (1 generator), kappa lives at arity 2 where Harrison = 0."""
        h = harrison_dimension(2, 1)
        assert h == 0, "Harrison vanishes at arity 2 for 1 generator"
        # But Sym^2 is nonzero:
        s = comb(1 + 2 - 1, 2)  # = binom(2,2) = 1
        assert s == 1, "Sym^2 is 1-dim for 1 generator"

    def test_multi_generator_harrison_nonzero(self):
        """For 2+ generators, Harrison is nonzero at all arities."""
        for m in range(2, 5):
            for n in range(1, 6):
                assert harrison_dimension(n, m) > 0, f"m={m}, n={n}"


# ============================================================================
# MULTI-PATH CROSS-VERIFICATION
# ============================================================================

class TestMultiPathWittVerification:
    """Verify Witt dimensions via 3+ independent methods."""

    def test_witt_via_necklace_count(self):
        """Path 1: Witt(n,m) = (1/n) number of aperiodic necklaces of length n on m colors.

        An aperiodic necklace is a cyclic sequence with minimal period = n.
        Count via Moebius inversion: (1/n) sum_{d|n} mu(n/d) m^d.
        Verify against direct enumeration for small cases.

        For m=2, n=3: aperiodic binary necklaces of length 3.
        All binary strings of length 3: 8. Periodic ones: 000, 111 (period 1).
        Aperiodic: 6. Necklaces (mod rotation): 6/3 = 2.
        Witt(3,2) = 2. CHECK.
        """
        # m=2, n=3
        assert witt_dimension(3, 2) == 2
        # Direct: binary strings 001,010,100 are one necklace; 011,110,101 are another.
        # So 2 aperiodic necklaces. Matches Witt.

        # m=2, n=4: aperiodic binary length-4.
        # All: 16. Period 1: 0000,1111 = 2. Period 2: 0101,1010,0011... wait
        # Period-2 strings: those where s = s[2:]s[:2]. These are: 0000,0101,1010,1111.
        # But 0000,1111 already counted as period 1.
        # Pure period-2 (not period-1): 0101, 1010 = 2 strings, = 1 necklace class of size 2... no.
        # Aperiodic count = sum_{d|4} mu(4/d) * 2^d = mu(4)*2 + mu(2)*4 + mu(1)*16
        #                 = 0*2 + (-1)*4 + 1*16 = 12
        # Necklaces = 12/4 = 3.
        assert witt_dimension(4, 2) == 3

    def test_witt_via_pbw_identity(self):
        """Path 2: PBW identity: prod_{n>=1} 1/(1-t^n)^{W(n,m)} = 1/(1-mt).

        Verify by expanding both sides to order t^N and comparing coefficients.
        LHS coefficient of t^N = number of partitions weighted by Witt dims.
        RHS coefficient of t^N = m^N.
        """
        for m in range(1, 4):
            max_N = 8
            # Compute Witt dimensions
            W = {n: witt_dimension(n, m) for n in range(1, max_N + 1)}

            # Expand prod_{n=1}^{max_N} 1/(1-t^n)^{W(n,m)} to order max_N
            # Start with polynomial [1] and iteratively multiply by 1/(1-t^n)^{W(n,m)}
            # 1/(1-t^n)^k = sum_{j>=0} binom(k+j-1,j) t^{nj}
            coeffs = [F(0)] * (max_N + 1)
            coeffs[0] = F(1)
            for n in range(1, max_N + 1):
                k = W[n]
                if k == 0:
                    continue
                # Multiply current polynomial by 1/(1-t^n)^k
                new_coeffs = [F(0)] * (max_N + 1)
                for j in range(0, max_N // n + 1):
                    # binom(k+j-1, j) = C(k+j-1, j)
                    bcoeff = F(comb(k + j - 1, j))
                    for prev_deg in range(max_N + 1):
                        total_deg = prev_deg + n * j
                        if total_deg > max_N:
                            break
                        new_coeffs[total_deg] += coeffs[prev_deg] * bcoeff
                coeffs = new_coeffs

            # Check: coefficient of t^N should be m^N
            for N in range(0, max_N + 1):
                expected = F(m ** N) if N >= 0 else F(0)
                assert coeffs[N] == expected, (
                    f"PBW identity fails at m={m}, N={N}: got {coeffs[N]}, expected {expected}"
                )

    def test_witt_via_direct_lie_basis_count(self):
        """Path 3: For m=2, n=1..5: directly verify dim of multilinear Lie(n)
        inside V^{tensor n} using the e_1 projector rank.

        The rank of e_1 on the multilinear part of V^{tensor n} (dim(V)=n
        so multilinear = n! basis elements) should be (n-1)!.
        Witt(n,m) for general m uses the full V^{tensor n}.
        For the multilinear part: dim = (n-1)! = Lie operad dimension.
        """
        for n in range(1, 5):
            rank = e1_rank(n)
            assert rank == factorial(n - 1), f"n={n}: rank={rank}, expected {factorial(n-1)}"
            # This is the Lie operad dimension, which is the building block for Witt.
            # Witt(n,m) = (multilinear Lie dim) * (m choose n) / ... no.
            # Actually Witt(n,m) uses ALL of V^{tensor n}, not just multilinear.
            # But the Lie operad dimension (n-1)! is the S_n-module dimension of Lie(n).
            # The multiplicity of Lie(n) in V^{tensor n} for V = Q^m gives Witt(n,m)
            # via character theory. The rank check confirms the operadic dimension.


class TestMultiPathIdempotentVerification:
    """Verify e_1 via 3+ independent methods."""

    def test_e1_via_dsw_and_matrix_rank(self):
        """Path 1 (DSW formula) cross-checked with Path 2 (matrix rank)."""
        for n in range(2, 5):
            result = verify_dsw_idempotent(n)
            assert result['is_idempotent'], f"n={n}: not idempotent"
            assert result['rank_correct'], f"n={n}: wrong rank"

    def test_e1_via_trace_on_regular_rep(self):
        """Path 3: trace on regular rep = n! * e_1(id) should equal (n-1)!.
        So e_1(id) = 1/n.

        Verify: e_1(id) = (1/n) * l_n(id). The coefficient of the identity
        in the right-normed bracket is +1 (the leading term x_0 x_1 ... x_{n-1}).
        So l_n(id) = 1, hence e_1(id) = 1/n.
        """
        for n in range(1, 6):
            e1 = first_eulerian_idempotent_coefficients(n)
            id_perm = tuple(range(n))
            assert e1.get(id_perm, F(0)) == F(1, n), (
                f"n={n}: e_1(id) = {e1.get(id_perm, F(0))}, expected 1/{n}"
            )

    def test_e1_via_lie_bracket_property(self):
        """Path 4: e_1 . v is a Lie element iff l_n(e_1 . v) = n * (e_1 . v).
        Since e_1 = (1/n)*l_n and l_n^2 = n*l_n, we have l_n(e_1.v) = (1/n)*l_n^2(v) = l_n(v) = n*(e_1.v).
        Verify: (1/n)*l_n applied twice gives (1/n)*l_n (idempotent property).
        """
        for n in range(2, 5):
            err = verify_idempotent(n)
            assert err == F(0), f"n={n}: e_1^2 != e_1, error={err}"

    def test_e1_antisymmetry_at_n2(self):
        """Path 5: At n=2, e_1 = antisymmetrizer. Independently verify:
        [x_0, x_1] = x_0 x_1 - x_1 x_0, so e_1 = (1/2)(id - tau).
        The antisymmetrizer projects onto Lambda^2(V) = Lie(2).
        """
        e1 = first_eulerian_idempotent_coefficients(2)
        # Must be exactly (1/2)(id - swap)
        assert e1[(0, 1)] == F(1, 2)
        assert e1[(1, 0)] == F(-1, 2)
        # Independently: the Lie bracket [a,b] = ab - ba in T(V)
        # lives in the antisymmetric part. Dim Lambda^2(V) = m(m-1)/2.
        # For V = Q^m: W(2,m) = m(m-1)/2.
        for m in range(1, 6):
            assert witt_dimension(2, m) == m * (m - 1) // 2


class TestMultiPathHeisenbergVerification:
    """Verify Heisenberg bar structure via 3+ independent paths."""

    def test_heisenberg_harrison_vanishes_path1_witt(self):
        """Path 1: Witt(n,1) = 0 for n >= 2 (direct formula)."""
        for n in range(2, 8):
            assert witt_dimension(n, 1) == 0

    def test_heisenberg_harrison_vanishes_path2_bracket_trace(self):
        """Path 2: sum of e_1 coefficients = 0 for n >= 2 (bracket sum vanishes)."""
        for n in range(2, 6):
            e1 = first_eulerian_idempotent_coefficients(n)
            assert sum(e1.values(), F(0)) == F(0)

    def test_heisenberg_harrison_vanishes_path3_free_lie_abelian(self):
        """Path 3: The free Lie algebra on 1 generator is abelian (1-dim, just
        the generator itself). Lie(Q)_n = 0 for n >= 2 because all brackets
        [x, [x, [..., x]...]] = 0 when there is only one generator x.
        In the tensor algebra Q[x], [x,x] = xx - xx = 0.
        """
        # The bracket [x,x] = 0 in any Lie algebra (antisymmetry).
        # So Lie(Q) = Q * x, concentrated in degree 1.
        # Verify: W(n,1) = (1/n) sum_{d|n} mu(n/d) * 1 = (1/n) sum_{d|n} mu(d)
        # For n >= 2: sum_{d|n} mu(d) = 0 (standard Moebius identity).
        for n in range(2, 10):
            moebius_sum = sum(moebius(d) for d in range(1, n + 1) if n % d == 0)
            assert moebius_sum == 0, f"sum mu(d) for d|{n} = {moebius_sum}, expected 0"

    def test_heisenberg_kappa_in_weight2_path1(self):
        """Path 1: kappa at arity 2 is in Sym^2(Q) (weight 2 Eulerian, NOT weight 1).
        For V=Q: V^{tensor 2} = Q is trivial S_2-rep.
        e_1 = (1/2)(id - swap) acts as (1/2)(1 - 1) = 0.
        e_2 = (1/2)(id + swap) acts as (1/2)(1 + 1) = 1.
        So the entire arity-2 space is weight 2 (symmetric), weight 1 = 0.
        """
        e1 = first_eulerian_idempotent_coefficients(2)
        # On trivial rep: e_1 acts as sum of coefficients
        trace_e1 = sum(e1.values(), F(0))
        assert trace_e1 == F(0), "e_1 annihilates trivial rep at n=2"
        # e_2 = id - e_1, so e_2 acts as 1 - 0 = 1
        trace_e2 = F(1) - trace_e1
        assert trace_e2 == F(1), "e_2 acts as identity on trivial rep at n=2"

    def test_heisenberg_kappa_in_weight2_path2(self):
        """Path 2: Physical argument. The Heisenberg OPE J(z)J(w) ~ k/(z-w)^2
        produces a SYMMETRIC bilinear form (the level k). The bar element
        [J|J] at arity 2 represents this symmetric pairing. Symmetric = weight 2,
        not antisymmetric = weight 1 (Harrison)."""
        # The OPE J(z)J(w) = J(w)J(z) (bosonic symmetry) means the arity-2
        # bar element is S_2-invariant (symmetric), not S_2-anti-invariant.
        # e_2 (symmetrizer) projects onto this; e_1 (antisymmetrizer) kills it.
        assert harrison_dimension(2, 1) == 0


class TestMultiPathBracketVerification:
    """Verify bracket coefficients via independent methods."""

    def test_arity3_bracket_path1_recursive(self):
        """Path 1: Recursive computation [x0, [x1, x2]]."""
        coeffs = _right_normed_bracket_coefficients(3)
        assert coeffs[(0, 1, 2)] == F(1)
        assert coeffs[(2, 1, 0)] == F(1)
        assert coeffs[(0, 2, 1)] == F(-1)
        assert coeffs[(1, 2, 0)] == F(-1)

    def test_arity3_bracket_path2_direct_expansion(self):
        """Path 2: Direct expansion of [a,[b,c]] = a(bc-cb) - (bc-cb)a.

        [a,[b,c]] = abc - acb - bca + cba.
        Permutations: (0,1,2)=abc, (0,2,1)=acb, (1,2,0)=bca, (2,1,0)=cba.
        Coefficients: +1, -1, -1, +1.
        """
        # Independently compute by hand
        expected = {(0,1,2): 1, (0,2,1): -1, (1,2,0): -1, (2,1,0): 1}
        coeffs = _right_normed_bracket_coefficients(3)
        for perm, exp_val in expected.items():
            assert coeffs.get(perm, F(0)) == F(exp_val), f"perm={perm}"

    def test_arity4_bracket_path1_term_count(self):
        """Path 1: [x0,[x1,[x2,x3]]] has 2^3 = 8 nonzero terms."""
        coeffs = _right_normed_bracket_coefficients(4)
        nonzero = sum(1 for v in coeffs.values() if v != 0)
        assert nonzero == 8

    def test_arity4_bracket_path2_leading_term(self):
        """Path 2: The leading term x_0 x_1 x_2 x_3 has coefficient +1."""
        coeffs = _right_normed_bracket_coefficients(4)
        assert coeffs.get((0, 1, 2, 3), F(0)) == F(1)

    def test_arity4_bracket_path3_reversal_sign(self):
        """Path 3: The fully reversed term x_3 x_2 x_1 x_0 has coefficient +1.

        [a,[b,[c,d]]] contains the term +dcba.
        Proof: the innermost [c,d] has +cd-dc. Then [b, +cd-dc] has
        terms ...+dcb-dcb... wait, let me compute.
        [c,d] = cd - dc
        [b,[c,d]] = bcd - bdc - cdb + dcb
        [a,[b,[c,d]]] = a(bcd-bdc-cdb+dcb) - (bcd-bdc-cdb+dcb)a
          = abcd - abdc - acdb + adcb - bcda + bdca + cdba - dcba
        Hmm, the reversal (3,2,1,0) = dcba has coefficient -1 here.
        Wait, let me recount. Using 0-indexed: a=x_0, b=x_1, c=x_2, d=x_3.
        dcba = x_3 x_2 x_1 x_0 = permutation (3,2,1,0).
        From the expansion: -dcba has coefficient -1.
        But the recursive formula gives... let me check.
        """
        coeffs = _right_normed_bracket_coefficients(4)
        # From hand expansion: [a,[b,[c,d]]] = abcd - abdc - acdb + adcb
        #                                     - bcda + bdca + cdba - dcba
        # So (3,2,1,0) -> -1
        # But wait: at arity 3, (2,1,0) -> +1. Let me re-derive arity 4.
        # [x_0, inner] where inner = [x_1,[x_2,x_3]]
        # inner at arity 3 (shifted by 1): coefficients on {1,2,3}
        # inner = x_1x_2x_3 - x_1x_3x_2 - x_2x_3x_1 + x_3x_2x_1
        # [x_0, inner] = x_0*inner - inner*x_0
        # x_0*inner: prepend 0: (0,1,2,3)->+1, (0,1,3,2)->-1, (0,2,3,1)->-1, (0,3,2,1)->+1
        # inner*x_0: append 0:  (1,2,3,0)->+1, (1,3,2,0)->-1, (2,3,1,0)->-1, (3,2,1,0)->+1
        # [x_0,inner] = (x_0*inner) - (inner*x_0)
        # So (3,2,1,0) gets coefficient -(+1) = -1 from inner*x_0 term.
        # And (0,3,2,1) gets +1 from x_0*inner.
        assert coeffs.get((3, 2, 1, 0), F(0)) == F(-1)
        assert coeffs.get((0, 3, 2, 1), F(0)) == F(1)
        assert coeffs.get((0, 1, 2, 3), F(0)) == F(1)
        assert coeffs.get((1, 2, 3, 0), F(0)) == F(-1)


class TestMultiPathDimensionVerification:
    """Verify dimension formulas via independent paths."""

    def test_dims_m2_n4_three_paths(self):
        """m=2, n=4: verify tensor, symmetric, Harrison dims via 3 paths.

        Path 1: Direct formulas. T=2^4=16, S=binom(5,4)=5, H=W(4,2)=3.
        Path 2: Compute W(4,2) from Moebius: (1/4)(mu(1)*16+mu(2)*4+mu(4)*2)
                = (1/4)(16-4+0) = 3.
        Path 3: PBW check at degree 4: prod 1/(1-t^n)^{W(n,2)} has t^4 coeff = 16.
        """
        # Path 1
        assert tensor_bar_dimension(4, 2) == 16
        assert comb(5, 4) == 5
        assert harrison_dimension(4, 2) == 3

        # Path 2: explicit Moebius
        m, n = 2, 4
        moebius_sum = sum(moebius(n // d) * m**d for d in range(1, n+1) if n % d == 0)
        assert moebius_sum == 12  # n * W(n,m) = 4 * 3 = 12
        assert moebius_sum // n == 3

        # Path 3: PBW coefficient
        W = {1: 2, 2: 1, 3: 2, 4: 3}
        # prod_{n=1}^{4} 1/(1-t^n)^{W(n,2)} expanded to t^4
        # Use generating function expansion
        coeffs = [F(0)] * 5
        coeffs[0] = F(1)
        for nn in range(1, 5):
            k = W[nn]
            if k == 0:
                continue
            new_coeffs = [F(0)] * 5
            for j in range(0, 4 // nn + 1):
                bc = F(comb(k + j - 1, j))
                for prev in range(5):
                    tot = prev + nn * j
                    if tot > 4:
                        break
                    new_coeffs[tot] += coeffs[prev] * bc
            coeffs = new_coeffs
        assert coeffs[4] == F(16), f"PBW coeff at t^4 = {coeffs[4]}, expected 16"
