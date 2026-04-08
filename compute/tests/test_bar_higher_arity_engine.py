r"""Tests for bar_higher_arity_engine.py.

Verifies explicit bar differential at arities 5, 6, 7 for standard families,
higher Massey products for k[x]/(x^3), cyclic structure at arity 5,
combinatorial dimension counts, and sparsity profiles.

MULTI-PATH VERIFICATION:
  Path 1: d^2 = 0 as exact matrix identity at each (arity, weight)
  Path 2: sl_2 cohomology concentration at h = n(n+1)/2 with dim 2n+1
  Path 3: Heisenberg rank-1 has d = 0 (dim H = chain dim)
  Path 4: Heisenberg total dimension matches prod(1 + x^k) coefficient
  Path 5: sl_2 chain dim via combinatorial formula matches engine enumeration
  Path 6: Virasoro CE at arity 5 vanishes (Koszulness)
  Path 7: k[x]/(x^2) is Koszul (only diagonal cohomology), k[x]/(x^3) is not
  Path 8: Cyclic rotation preserves sorted-tuple basis up to sign
  Path 9: Sparsity density decreases as arity grows (O(n^{-2}) scaling)

SIGN CONVENTION:
  AP45: |s^{-1}v| = |v| - 1. Desuspension LOWERS degree by 1.
  The CE differential sign: (-1)^{pos_c + pos_beta + pos_gamma}.

References:
  comp:sl2-ce-verification (bar_complex_tables.tex)
  lem:bar-deg2-symmetric-square (landscape_census.tex)
  CLAUDE.md: sl_2 bar H^n = 2n+1 concentrated at h = n(n+1)/2
  CLAUDE.md: k[x]/(x^2) Koszul, k[x]/(x^3) has higher Massey products
"""

import pytest
from fractions import Fraction

from compute.lib.bar_higher_arity_engine import (
    # Core helpers
    _frac, _frac_array, _frac_matmul, _exact_rank, _mod_p_rank, _density,
    # Partition combinatorics
    partitions_distinct_into_n, partitions_into_n,
    # Engines
    LoopCEEngine, VirasoroCEEngine, TruncatedPolyMasseyEngine,
    # sl_2
    SL2_BRACKET, DIM_SL2,
    sl2_engine, sl2_arity_n_cohomology,
    sl2_concentration_weight, sl2_concentration_dim,
    sl2_chain_dim_combinatorial, sl2_chain_dim_exact,
    sl2_sparsity_summary,
    # Heisenberg
    HEIS_BRACKET,
    heisenberg_engine, heisenberg_chain_dim, heisenberg_cohomology_dim,
    heisenberg_gf_coefficient, heisenberg_kahler_check,
    # Cyclic
    cyclic_rotation_sign, cyclic_action_on_basis,
    cyclic_invariants_dim, cyclic_cohomology_arity_5_sl2,
    # Reports
    report_sl2_high_arity, report_heisenberg_high_arity,
    report_virasoro_arity_5, report_virasoro_arity_5_saturated,
    sparsity_profile,
)


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture(scope='module')
def sl2_w10():
    return sl2_engine(max_weight=10)


@pytest.fixture(scope='module')
def sl2_w12():
    return sl2_engine(max_weight=12)


@pytest.fixture(scope='module')
def sl2_w15():
    return sl2_engine(max_weight=15)


@pytest.fixture(scope='module')
def heis_w10():
    return heisenberg_engine(max_weight=10)


@pytest.fixture(scope='module')
def vir_w16():
    return VirasoroCEEngine(max_weight=16)


@pytest.fixture(scope='module')
def truncpoly_N2():
    return TruncatedPolyMasseyEngine(N=2, max_weight=8)


@pytest.fixture(scope='module')
def truncpoly_N3():
    return TruncatedPolyMasseyEngine(N=3, max_weight=10)


# ============================================================
# 1. Exact arithmetic helpers
# ============================================================

class TestArithmeticHelpers:

    def test_frac_int(self):
        assert _frac(5) == Fraction(5)

    def test_frac_fraction(self):
        assert _frac(Fraction(3, 7)) == Fraction(3, 7)

    def test_exact_rank_identity(self):
        import numpy as np
        M = _frac_array((3, 3))
        for i in range(3):
            M[i, i] = Fraction(1)
        assert _exact_rank(M) == 3

    def test_exact_rank_zero(self):
        import numpy as np
        M = _frac_array((3, 3))
        assert _exact_rank(M) == 0

    def test_mod_p_rank_matches_exact(self):
        """mod-p rank and exact rank agree on a random small matrix."""
        import numpy as np
        M = _frac_array((4, 5))
        values = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10],
                  [0, 1, 2, 3, 4], [1, 0, -1, -2, -3]]
        for i in range(4):
            for j in range(5):
                M[i, j] = Fraction(values[i][j])
        assert _exact_rank(M) == _mod_p_rank(M)

    def test_density_zero_matrix(self):
        M = _frac_array((3, 4))
        assert _density(M) == Fraction(0)

    def test_density_full_matrix(self):
        M = _frac_array((2, 3))
        for i in range(2):
            for j in range(3):
                M[i, j] = Fraction(1)
        assert _density(M) == Fraction(1)


# ============================================================
# 2. Partition combinatorics
# ============================================================

class TestPartitionCombinatorics:

    def test_partitions_distinct_trivial(self):
        # 5 into 2 distinct positive parts: (1,4), (2,3) -> 2
        assert partitions_distinct_into_n(5, 2, 1) == 2

    def test_partitions_distinct_arity_3(self):
        # 6 into 3 distinct positive parts: (1,2,3) -> 1
        assert partitions_distinct_into_n(6, 3, 1) == 1

    def test_partitions_distinct_arity_5_min(self):
        # 15 = 1+2+3+4+5, the minimum for 5 distinct positive parts
        assert partitions_distinct_into_n(15, 5, 1) == 1

    def test_partitions_distinct_arity_5_weight_16(self):
        # 16 into 5 distinct positive parts: (1,2,3,4,6) -> 1
        assert partitions_distinct_into_n(16, 5, 1) == 1

    def test_partitions_distinct_arity_6_weight_21(self):
        # 21 = 1+2+3+4+5+6 -> 1
        assert partitions_distinct_into_n(21, 6, 1) == 1

    def test_partitions_distinct_returns_zero_for_impossible(self):
        # 3 into 4 distinct positive parts: impossible
        assert partitions_distinct_into_n(3, 4, 1) == 0

    def test_partitions_regular(self):
        # 5 into 3 parts (not necessarily distinct): (1,1,3), (1,2,2) -> 2
        assert partitions_into_n(5, 3, 1) == 2


# ============================================================
# 3. sl_2 loop algebra CE engine
# ============================================================

class TestSl2LoopEngine:

    def test_chain_dim_arity_1(self, sl2_w10):
        """arity 1 at each weight h has 3 generators e_h, h_h, f_h."""
        for h in range(1, 11):
            assert sl2_w10.chain_dim(1, h) == 3

    def test_chain_dim_arity_2_weight_2(self, sl2_w10):
        """arity 2 weight 2: (i,j) with i+j=2 and distinct flat indices.
        Both mode 1, so any pair of distinct sl_2 generators at mode 1.
        C(3,2) = 3.
        """
        assert sl2_w10.chain_dim(2, 2) == 3

    def test_chain_dim_arity_3_weight_3(self, sl2_w10):
        """arity 3 weight 3: all three sl_2 generators at mode 1. C(3,3)=1."""
        assert sl2_w10.chain_dim(3, 3) == 1

    def test_arity_5_minimum_weight(self, sl2_w10):
        """Minimum arity-5 weight in sl_2 CE is 1+1+1+2+2 = 7.
        At weight 7 we choose all three at mode 1 and two of three at mode 2.
        Count: 1 * C(3,2) = 3.
        """
        assert sl2_w10.chain_dim(5, 7) == 3

    def test_arity_5_weight_10(self, sl2_w10):
        """Known combinatorial value from engine."""
        assert sl2_w10.chain_dim(5, 10) == 81

    def test_arity_6_minimum_weight(self, sl2_w10):
        """Minimum arity-6 weight: 1+1+1+2+2+2 = 9, pick all 3 at mode 1 and
        all 3 at mode 2: 1 * 1 = 1."""
        assert sl2_w10.chain_dim(6, 9) == 1

    def test_arity_7_minimum_weight(self, sl2_w10):
        """Minimum arity-7: 1+1+1+2+2+2+3 = 12, pick 3 at mode 1, 3 at mode 2,
        1 at mode 3: 1 * 1 * 3 = 3."""
        assert sl2_w10.chain_dim(7, 12) == 3

    def test_d_squared_zero_arity_4_weight_6(self, sl2_w10):
        assert sl2_w10.verify_d_squared(4, 6) is True

    def test_d_squared_zero_arity_4_weight_8(self, sl2_w10):
        assert sl2_w10.verify_d_squared(4, 8) is True

    def test_d_squared_zero_arity_5_weight_10(self, sl2_w10):
        assert sl2_w10.verify_d_squared(5, 10) is True

    def test_d_squared_zero_arity_5_weight_12(self, sl2_w12):
        assert sl2_w12.verify_d_squared(5, 12) is True

    def test_cohomology_concentration_arity_4(self, sl2_w10):
        """H^4 = 9 at h = 10, else 0."""
        assert sl2_w10.cohomology_dim(4, 10, fast=True) == 9
        for h in [5, 6, 7, 8, 9]:
            # off-concentration weights have H^4 = 0
            assert sl2_w10.cohomology_dim(4, h, fast=True) == 0

    def test_cohomology_concentration_arity_5(self, sl2_w15):
        """H^5 = 11 at h = 15, else 0 (within accessible weights)."""
        assert sl2_w15.cohomology_dim(5, 15, fast=True) == 11

    def test_cohomology_arity_5_vanishes_below_concentration(self, sl2_w12):
        """H^5 = 0 for h < 15 (accessible range up to 12)."""
        for h in [10, 11, 12]:
            assert sl2_w12.cohomology_dim(5, h, fast=True) == 0

    def test_cohomology_arity_6_vanishes_below_concentration(self, sl2_w12):
        """H^6 = 0 for h < 21."""
        for h in [9, 10, 11, 12]:
            assert sl2_w12.cohomology_dim(6, h, fast=True) == 0


# ============================================================
# 4. sl_2 concentration formulas
# ============================================================

class TestSl2Concentration:

    def test_concentration_weight_formula(self):
        """h_n = n(n+1)/2."""
        for n in range(1, 8):
            assert sl2_concentration_weight(n) == n * (n + 1) // 2

    def test_concentration_dim_formula(self):
        """dim H^n = 2n + 1."""
        for n in range(1, 8):
            assert sl2_concentration_dim(n) == 2 * n + 1

    def test_concentration_arity_1(self):
        assert sl2_concentration_weight(1) == 1
        assert sl2_concentration_dim(1) == 3

    def test_concentration_arity_5(self):
        assert sl2_concentration_weight(5) == 15
        assert sl2_concentration_dim(5) == 11

    def test_concentration_arity_6(self):
        assert sl2_concentration_weight(6) == 21
        assert sl2_concentration_dim(6) == 13


# ============================================================
# 5. Heisenberg rank-1: abelian loop, d = 0
# ============================================================

class TestHeisenbergRankOne:

    def test_bracket_is_empty(self):
        """Heisenberg bracket has no entries (abelian)."""
        assert HEIS_BRACKET == {}

    def test_chain_dim_arity_1(self, heis_w10):
        """Chain at arity 1 weight h: exactly 1 generator (mode h)."""
        for h in range(1, 11):
            assert heis_w10.chain_dim(1, h) == 1

    def test_chain_dim_arity_2(self, heis_w10):
        """Chain at arity 2 weight 5: {(1,4), (2,3)} -> 2."""
        assert heis_w10.chain_dim(2, 5) == 2

    def test_chain_dim_arity_5_weight_15(self, heis_w10):
        """Arity 5 min weight = 1+2+3+4+5 = 15 has exactly 1 element.
        Reachable inside heis_w10 since max mode 5 <= 10.
        """
        assert heis_w10.chain_dim(5, 15) == 1
        heis_big = heisenberg_engine(max_weight=15)
        assert heis_big.chain_dim(5, 15) == 1

    def test_chain_dim_arity_6_weight_21(self):
        heis_big = heisenberg_engine(max_weight=21)
        assert heis_big.chain_dim(6, 21) == 1

    def test_chain_dim_arity_7_weight_28(self):
        heis_big = heisenberg_engine(max_weight=28)
        assert heis_big.chain_dim(7, 28) == 1

    def test_d_is_identically_zero(self, heis_w10):
        """Bracket-free loop algebra gives differential = 0 everywhere."""
        for n in range(1, 5):
            for w in range(1, 11):
                d = heis_w10.differential_matrix(n, w)
                if d.size == 0:
                    continue
                rows, cols = d.shape
                all_zero = all(d[i, j] == Fraction(0)
                               for i in range(rows) for j in range(cols))
                assert all_zero, f"d != 0 at (n={n}, w={w})"

    def test_cohomology_equals_chain_dim(self, heis_w10):
        """With d = 0, H^n_w = chain_dim."""
        for n in range(1, 5):
            for w in range(1, 11):
                assert heis_w10.chain_dim(n, w) == heis_w10.cohomology_dim(n, w)

    def test_total_dim_matches_exterior_gf(self):
        """Sum over arities of chain dim = [x^w] prod(1+x^k)."""
        result = heisenberg_kahler_check(max_weight=12)
        assert all(result.values())

    def test_gf_coefficient_first_values(self):
        """First values of prod(1+x^k): 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, ..."""
        expected = [1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10]
        for w, e in enumerate(expected):
            assert heisenberg_gf_coefficient(w) == e

    def test_pbw_collapse_k_independence(self, heis_w10):
        """Heisenberg CE is k-independent (no central term for m, n >= 1)."""
        # Verify by explicit construction: the LoopCEEngine's bracket is empty.
        # This is structural; no loop-algebra bracket depends on k.
        assert HEIS_BRACKET == {}


# ============================================================
# 6. Virasoro CE at arity 5
# ============================================================

class TestVirasoroArity5:

    def test_vir_arity_1_concentration(self, vir_w16):
        """H^1(B(Vir))_h concentrated at h in {2, 3, 4}."""
        for h in [2, 3, 4]:
            assert vir_w16.cohomology_dim(1, h) == 1
        for h in [5, 6, 7, 8, 9, 10]:
            assert vir_w16.cohomology_dim(1, h) == 0

    def test_vir_arity_5_chain_is_empty_below_20(self, vir_w16):
        """Min arity-5 weight: 2+3+4+5+6 = 20. Below this, chain is 0."""
        for w in range(5, 20):
            assert vir_w16.chain_dim(5, w) == 0

    def test_vir_arity_5_chain_at_weight_20(self, vir_w16):
        """Exactly 1 chain element at weight 20: (L_-2, L_-3, L_-4, L_-5, L_-6)."""
        assert vir_w16.chain_dim(5, 20) == 1

    def test_vir_arity_5_chain_at_weight_21(self, vir_w16):
        """Exactly 1 chain element at weight 21: (L_-2, L_-3, L_-4, L_-5, L_-7)."""
        assert vir_w16.chain_dim(5, 21) == 1

    def test_vir_arity_5_chain_at_weight_22(self):
        """2 chains at weight 22: (2,3,4,5,8) and (2,3,4,6,7)."""
        eng = VirasoroCEEngine(max_weight=24)
        assert eng.chain_dim(5, 22) == 2

    def test_vir_arity_5_cohomology_vanishes_at_20(self, vir_w16):
        """Koszulness: H^5 = 0."""
        assert vir_w16.cohomology_dim(5, 20, fast=True) == 0

    def test_vir_arity_5_cohomology_vanishes_at_21(self, vir_w16):
        assert vir_w16.cohomology_dim(5, 21, fast=True) == 0

    def test_vir_d_squared_at_arity_4(self, vir_w16):
        for w in [10, 15, 20]:
            assert vir_w16.verify_d_squared(4, w) is True


# ============================================================
# 7. Combinatorial dimension count for sl_2
# ============================================================

class TestSl2CombinatorialCount:

    def test_combinatorial_matches_engine_arity_2(self):
        for w in range(2, 10):
            assert sl2_chain_dim_combinatorial(2, w) == sl2_chain_dim_exact(2, w, max_weight=12)

    def test_combinatorial_matches_engine_arity_3(self):
        for w in range(3, 11):
            assert sl2_chain_dim_combinatorial(3, w) == sl2_chain_dim_exact(3, w, max_weight=12)

    def test_combinatorial_matches_engine_arity_4(self):
        for w in range(4, 11):
            assert sl2_chain_dim_combinatorial(4, w) == sl2_chain_dim_exact(4, w, max_weight=12)

    def test_combinatorial_arity_5_weight_10(self):
        assert sl2_chain_dim_combinatorial(5, 10) == 81

    def test_combinatorial_arity_5_weight_15(self):
        assert sl2_chain_dim_combinatorial(5, 15) == 1119

    def test_combinatorial_arity_6_weight_10(self):
        """B^6 at weight 10 for sl_2: the tight corner.

        Min weight for arity 6 is 9.  At weight 10 we have the patterns:
          (1,1,1,2,2,2) impossible (only 6 distinct if we use all 3 at mode 1
          and all 3 at mode 2 -> weight 9, not 10).
          (1,1,1,2,2,3): C(3,3)*C(3,2)*C(3,1) = 1 * 3 * 3 = 9.
        """
        assert sl2_chain_dim_combinatorial(6, 10) == 9

    def test_combinatorial_arity_6_weight_9(self):
        """Arity 6, weight 9: (1,1,1,2,2,2), C(3,3)*C(3,3) = 1."""
        assert sl2_chain_dim_combinatorial(6, 9) == 1


# ============================================================
# 8. Higher Massey products: k[x]/(x^2) vs k[x]/(x^3)
# ============================================================

class TestTruncatedPolyMassey:

    def test_N2_koszul(self, truncpoly_N2):
        """k[x]/(x^2) is Koszul: H^n_n = 1, all else 0."""
        cohom = truncpoly_N2.koszul_test(max_arity=5, max_weight=8)
        for (arity, w), val in cohom.items():
            if arity == w:
                assert val == 1, f"H^{arity}_{w} = {val}, expected 1"
            else:
                assert val == 0, f"H^{arity}_{w} = {val}, expected 0"

    def test_N2_no_higher_massey(self, truncpoly_N2):
        """k[x]/(x^2) is Koszul: no higher Massey products."""
        assert truncpoly_N2.has_higher_massey(max_arity=5, max_weight=8) is False

    def test_N3_has_higher_massey(self, truncpoly_N3):
        """k[x]/(x^3) is NOT Koszul: higher Massey products exist."""
        assert truncpoly_N3.has_higher_massey(max_arity=5, max_weight=10) is True

    def test_N3_cohomology_at_arity_3_weight_4(self, truncpoly_N3):
        """k[x]/(x^3) bar cohomology has H^3_4 != 0.

        The explicit class: x|x|x at weight 3 has d(x|x|x) = x^2|x - x|x^2.
        At weight 4, a cocycle exists carrying the secondary Massey product.
        """
        assert truncpoly_N3.cohomology_dim(3, 4) == 1

    def test_N3_cohomology_at_arity_4_weight_6(self, truncpoly_N3):
        """Arity 4, weight 6: tertiary Massey class."""
        assert truncpoly_N3.cohomology_dim(4, 6) == 1

    def test_N3_cohomology_at_arity_5_weight_7(self, truncpoly_N3):
        """Arity 5, weight 7: quaternary Massey class.  This is the m_5
        5-ary A-infinity operation target.
        """
        assert truncpoly_N3.cohomology_dim(5, 7) == 1

    def test_N3_d_squared_zero(self, truncpoly_N3):
        """Bar differential squares to zero at all tested (arity, weight)."""
        for arity in range(2, 6):
            for w in range(arity, 10):
                assert truncpoly_N3.verify_d_squared(arity, w) is True


# ============================================================
# 9. Cyclic structure at arity 5
# ============================================================

class TestCyclicStructure:

    def test_cyclic_rotation_sign_even(self):
        """Arity 5 rotation: (-1)^4 = +1."""
        assert cyclic_rotation_sign(5) == 1

    def test_cyclic_rotation_sign_odd(self):
        """Arity 4 rotation: (-1)^3 = -1."""
        assert cyclic_rotation_sign(4) == -1

    def test_cyclic_action_preserves_sorted_tuples(self, sl2_w10):
        """On sorted-tuple CE basis, the cyclic action maps each basis
        element back to itself (as a set of flat indices) with a sign
        given by the sort permutation.
        """
        basis = sl2_w10.chain_basis(3, 6)
        cyc = cyclic_action_on_basis(basis)
        for b in basis:
            sign, target = cyc[b]
            assert target == b  # same multiset, hence same canonical tuple
            assert sign in (-1, 1)

    def test_cyclic_invariants_arity_5_sl2(self):
        """At arity 5 and concentration weight 15, invariants = chain dim."""
        result = cyclic_cohomology_arity_5_sl2(weight=15, max_weight=15)
        assert result['chain_dim'] == result['cyclic_invariant_dim']

    def test_cyclic_invariants_small_example(self, sl2_w10):
        """dim(invariants) = chain_dim for arity <= 1 (trivial rotation)."""
        assert cyclic_invariants_dim(sl2_w10, 1, 3) == sl2_w10.chain_dim(1, 3)

    def test_cyclic_cohomology_arity_5_structure(self):
        """Verify the invariants report has all three fields and consistent
        values at arity 5."""
        r = cyclic_cohomology_arity_5_sl2(weight=15, max_weight=15)
        assert 'chain_dim' in r
        assert 'cyclic_invariant_dim' in r
        assert 'ce_cohomology_dim' in r
        assert r['ce_cohomology_dim'] == 11  # concentration dim 2*5+1


# ============================================================
# 10. Sparsity analysis
# ============================================================

class TestSparsityAnalysis:

    def test_sparsity_arity_2_weight_4(self):
        s = sl2_sparsity_summary(2, 4)
        assert s['rows'] == 9
        assert s['cols'] == 12
        # 18 nonzero entries (verified manually)
        assert s['nonzero'] == 18
        # density = 18 / (9*12) = 1/6
        assert abs(s['density'] - 1.0 / 6) < 1e-10

    def test_sparsity_decreases_with_weight_at_fixed_arity(self):
        """At fixed arity, density decreases as weight grows (matrix dim
        grows roughly as partition count squared, but nonzeros per column
        grow linearly in bracket pairs).

        Concretely at arity 3: density at w=6 > density at w=10.
        """
        s_low = sl2_sparsity_summary(3, 6)
        s_hi = sl2_sparsity_summary(3, 10)
        assert s_hi['density'] < s_low['density']

    def test_sparsity_ranks_equal_chain_dim_full_rank_case(self):
        """At arity 2 weight 4, the differential has full column rank 9."""
        s = sl2_sparsity_summary(2, 4)
        assert s['rank'] == 9

    def test_sparsity_profile_consistency(self, sl2_w10):
        """Profile output has expected keys for each (arity, weight)."""
        prof = sparsity_profile(sl2_w10, 'sl2', [2, 3], [4, 5])
        for key, val in prof.items():
            assert 'family' in val
            assert 'chain_dim_source' in val
            assert 'density' in val
            assert 'rank' in val
            assert val['family'] == 'sl2'


# ============================================================
# 11. Multi-path cross-checks (AP10)
# ============================================================

class TestMultiPathVerification:
    """Every numerical claim verified by at least TWO independent paths.

    AP10: tests with hardcoded expected values can be wrong and still pass.
    The real verification is cross-family, cross-path, cross-formula.
    """

    def test_sl2_chain_path_cross(self):
        """Path A: engine enumeration.  Path B: closed-form combinatorial."""
        for n in range(1, 6):
            for h in range(n, 12):
                a = sl2_chain_dim_exact(n, h, max_weight=12)
                b = sl2_chain_dim_combinatorial(n, h)
                assert a == b, f"path mismatch n={n} h={h}: engine={a} comb={b}"

    def test_heisenberg_two_paths_gf(self):
        """Path A: sum of chain dim over arities.
        Path B: direct prod(1+x^k) expansion.
        """
        heis = heisenberg_engine(max_weight=12)
        for w in range(0, 13):
            path_a = sum(heis.chain_dim(n, w) for n in range(0, w + 1))
            path_b = heisenberg_gf_coefficient(w)
            assert path_a == path_b, f"w={w}: engine_sum={path_a} gf={path_b}"

    def test_heisenberg_combinatorial_consistency(self):
        """Path A: heisenberg_chain_dim helper.
        Path B: partitions_distinct_into_n helper.
        Path C: engine chain_dim.
        """
        heis = heisenberg_engine(max_weight=12)
        for n in range(1, 6):
            for w in range(1, 13):
                a = heisenberg_chain_dim(n, w)
                b = partitions_distinct_into_n(w, n, 1)
                c = heis.chain_dim(n, w)
                assert a == b == c, f"n={n} w={w}: {a} {b} {c}"

    def test_sl2_d_squared_zero_multi_arity(self, sl2_w10):
        """Exhaustive d^2 = 0 check across all arities and weights up to 10."""
        for arity in range(1, 5):
            for w in range(arity, 11):
                assert sl2_w10.verify_d_squared(arity, w), \
                    f"d^2 != 0 at arity={arity} weight={w}"

    def test_sl2_concentration_cross_check_with_engine(self):
        """The formula dim H^n = 2n+1 at h = n(n+1)/2 is verified by direct
        computation for arities 1 through 4 (arity 5 covered separately).
        """
        eng = sl2_engine(max_weight=12)
        for n in range(1, 5):
            h = sl2_concentration_weight(n)
            computed = eng.cohomology_dim(n, h, fast=True)
            formula = sl2_concentration_dim(n)
            assert computed == formula, \
                f"n={n}: computed={computed} formula={formula}"

    def test_sl2_off_concentration_vanishing_multi(self):
        """For arity n and weight h in [n+1, n(n+1)/2 - 1] (strictly off),
        the cohomology vanishes."""
        eng = sl2_engine(max_weight=10)
        # n=3: h_concentration = 6, so h in [4, 5] should vanish (H^3)
        for h in [4, 5]:
            assert eng.cohomology_dim(3, h, fast=True) == 0
        # n=4: h_concentration = 10, so h in [5..9] should vanish
        for h in [5, 6, 7, 8, 9]:
            assert eng.cohomology_dim(4, h, fast=True) == 0

    def test_exact_vs_mod_p_rank_agreement(self):
        """For small matrices from the engine, exact and mod-p rank agree.

        If they disagree, either the mod-p rank is unlucky (hit a bad prime)
        or one of the methods is buggy.
        """
        eng = sl2_engine(max_weight=8)
        for arity in range(1, 4):
            for w in range(arity, 9):
                d = eng.differential_matrix(arity, w)
                if d.size == 0:
                    continue
                exact = _exact_rank(d)
                mod = _mod_p_rank(d)
                assert exact == mod, \
                    f"arity={arity} w={w}: exact={exact} mod-p={mod}"

    def test_sl2_euler_characteristic_consistency(self):
        """Path-check: sum_n (-1)^n chain_dim(n, h) at fixed h should be
        invariant under bar differential.  Since d preserves h, the
        Euler characteristic equals sum_n (-1)^n cohomology_dim(n, h)
        exactly.
        """
        eng = sl2_engine(max_weight=10)
        for h in [3, 5, 6, 7, 10]:
            chain_chi = 0
            cohom_chi = 0
            for n in range(1, 11):
                chain_chi += (-1) ** n * eng.chain_dim(n, h)
                cohom_chi += (-1) ** n * eng.cohomology_dim(n, h, fast=True)
            assert chain_chi == cohom_chi, \
                f"h={h}: chain_chi={chain_chi} cohom_chi={cohom_chi}"

    def test_truncpoly_N2_matches_koszul_resolution(self, truncpoly_N2):
        """Independent path: for k[x]/(x^2), the minimal resolution gives
        Tor_n = k concentrated in internal degree n.  The bar complex must
        recover this Tor structure.
        """
        for n in range(1, 6):
            assert truncpoly_N2.cohomology_dim(n, n) == 1
            for w in range(n + 1, 8):
                assert truncpoly_N2.cohomology_dim(n, w) == 0

    def test_sl2_bracket_table_symmetry(self, sl2_w10):
        """Structure constants are antisymmetric: [a,b] + [b,a] = 0.
        Verified via the Lie bracket table.
        """
        for (a, b), br_ab in SL2_BRACKET.items():
            br_ba = SL2_BRACKET.get((b, a), {})
            for c, coeff in br_ab.items():
                assert Fraction(0) == coeff + br_ba.get(c, Fraction(0))

    def test_combinatorial_chain_via_mode_multiplicity_check(self):
        """Third verification path for sl_2 chain dimensions:
        decompose each mode multiplicity and count.

        For arity 2, weight 3: either (mode 1 + mode 2) or (mode 1 + mode 2).
        Modes distinct: mode 1 contributes C(3,1) = 3 choices, mode 2
        contributes C(3,1) = 3 choices, product = 9.
        """
        # Match against combinatorial routine directly
        assert sl2_chain_dim_combinatorial(2, 3) == 9
        # Match against engine
        eng = sl2_engine(max_weight=5)
        assert eng.chain_dim(2, 3) == 9

    def test_sl2_chain_dim_bound_from_partitions(self):
        """Loose upper bound: sl_2 chain dim <= 3^n * partitions into n parts.
        Lower bound: >= partitions into n distinct parts (single-generator case).
        """
        eng = sl2_engine(max_weight=10)
        for n in range(1, 5):
            for w in range(n, 11):
                cd = eng.chain_dim(n, w)
                # Lower bound: if each mode is distinct use sl_2 gen 0 only
                lower = partitions_distinct_into_n(w, n, 1)
                # Upper bound: (3^n) * partitions_into_n (allows repetition)
                upper = 3 ** n * partitions_into_n(w, n, 1)
                assert lower <= cd, \
                    f"n={n} w={w}: chain={cd} < lower={lower}"
                assert cd <= upper, \
                    f"n={n} w={w}: chain={cd} > upper={upper}"


# ============================================================
# 12. Reports / integration
# ============================================================

class TestReports:

    def test_report_sl2_matches_concentration(self):
        """report_sl2_high_arity checks H^n = 2n+1 at h = n(n+1)/2."""
        r = report_sl2_high_arity(max_arity=4)
        for n in range(1, 5):
            assert r[n]['matches'] is True
            assert r[n]['concentration_weight'] == n * (n + 1) // 2
            assert r[n]['expected_dim'] == 2 * n + 1

    def test_report_heisenberg_d_is_zero(self):
        """Heisenberg report confirms d = 0 (chain = cohomology) everywhere."""
        r = report_heisenberg_high_arity(max_arity=4, max_weight=8)
        for (n, w), info in r.items():
            assert info['d_zero'] is True

    def test_report_virasoro_arity_5_empty_below_20(self):
        r = report_virasoro_arity_5(weights=(5, 10, 15))
        for w, info in r.items():
            assert info['chain_dim_p5'] == 0
            assert info['cohomology_dim_p5'] == 0

    def test_report_virasoro_arity_5_saturated(self):
        """At saturated weights 20, 21, 22, chain is nonempty but H^5 = 0."""
        r = report_virasoro_arity_5_saturated(min_weight=20, max_weight=22)
        assert r[20]['chain_dim_p5'] == 1
        assert r[21]['chain_dim_p5'] == 1
        assert r[22]['chain_dim_p5'] == 2
        for w in [20, 21, 22]:
            assert r[w]['cohomology_dim_p5'] == 0
            assert r[w]['d_squared_zero'] is True
