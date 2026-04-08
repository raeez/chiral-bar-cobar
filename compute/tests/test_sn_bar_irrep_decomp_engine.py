r"""Tests for the S_n irrep decomposition engine on the bar complex.

Multi-path verification (AP10 / multi-path mandate):
  Path 1: Direct character inner product against hardcoded character tables.
  Path 2: Schur-Weyl duality (Weyl/SSYT formula) for ungraded ('sl2', 'sl3') cases.
  Path 3: Total dimension sum (sum_lam mult(lam) * dim V_lam = d^n).
  Path 4: Cyclic subgroup Burnside identity (sum of traces / n = trivial rep mult).
  Path 5: Trivial/sign isotypic closed-form (C(d+n-1,n) and C(d,n)).
  Path 6: Cross-check with ordered-vs-unordered engine at common test points.
  Path 7: Character orthogonality (checks implicit via integer multiplicities).
  Path 8: Koszul sign flip test (degree-0 Sym <-> degree-1 sign).

References:
  Fulton-Harris, Representation Theory, Appendix A.1-A.2.
  Macdonald, Symmetric Functions, Ch I Section 7 (Schur expansion).
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

import pytest

from compute.lib.sn_bar_irrep_decomp_engine import (
    SnBarIrrepEngine,
    CHARACTER_TABLES,
    partitions,
    partition_class_size,
    cycle_type,
    irrep_dimension,
    schur_functor_dim,
    schur_weyl_sl2,
    virasoro_arity_4_decomposition,
    cyclic_decomposition_sl2,
)


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture(scope="module")
def sl2():
    return SnBarIrrepEngine('sl2')


@pytest.fixture(scope="module")
def sl3():
    return SnBarIrrepEngine('sl3')


@pytest.fixture(scope="module")
def vir_single():
    return SnBarIrrepEngine('virasoro_single')


@pytest.fixture(scope="module")
def vir_modes():
    return SnBarIrrepEngine('virasoro_modes', max_weight=10)


# ============================================================
# Partition / combinatorics tests
# ============================================================

class TestPartitionCombinatorics:

    def test_partitions_count_n_1_to_6(self):
        # p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11
        assert len(partitions(1)) == 1
        assert len(partitions(2)) == 2
        assert len(partitions(3)) == 3
        assert len(partitions(4)) == 5
        assert len(partitions(5)) == 7
        assert len(partitions(6)) == 11

    def test_partition_class_sizes_sum_to_n_factorial(self):
        for n in range(1, 6):
            total = sum(partition_class_size(lam, n) for lam in partitions(n))
            assert total == factorial(n)

    def test_partition_class_size_known(self):
        # S_3: e has size 1, transposition size 3, 3-cycle size 2
        assert partition_class_size((1, 1, 1), 3) == 1
        assert partition_class_size((2, 1), 3) == 3
        assert partition_class_size((3,), 3) == 2
        # S_4: e=1, (2,1,1)=6, (2,2)=3, (3,1)=8, (4,)=6
        assert partition_class_size((1, 1, 1, 1), 4) == 1
        assert partition_class_size((2, 1, 1), 4) == 6
        assert partition_class_size((2, 2), 4) == 3
        assert partition_class_size((3, 1), 4) == 8
        assert partition_class_size((4,), 4) == 6

    def test_cycle_type_identity(self):
        assert cycle_type((0, 1, 2, 3)) == (1, 1, 1, 1)

    def test_cycle_type_transposition(self):
        assert cycle_type((1, 0, 2)) == (2, 1)

    def test_cycle_type_3_cycle(self):
        assert cycle_type((1, 2, 0)) == (3,)


# ============================================================
# Character table sanity
# ============================================================

class TestCharacterTables:

    def test_s3_trivial_character(self):
        table = CHARACTER_TABLES[3]
        # Trivial = all 1's
        for cls in partitions(3):
            assert table[((3,), cls)] == 1

    def test_s3_sign_character(self):
        table = CHARACTER_TABLES[3]
        assert table[((1, 1, 1), (1, 1, 1))] == 1     # identity
        assert table[((1, 1, 1), (2, 1))] == -1       # transposition
        assert table[((1, 1, 1), (3,))] == 1          # 3-cycle

    def test_s3_standard_dimension(self):
        # Standard rep has dim 2
        table = CHARACTER_TABLES[3]
        assert table[((2, 1), (1, 1, 1))] == 2

    def test_s4_irrep_dimensions(self):
        # Dims: 1, 3, 2, 3, 1
        expected = {(4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1}
        for lam, dim in expected.items():
            assert irrep_dimension(lam) == dim, f"bad dim for {lam}"

    def test_s5_irrep_dimensions(self):
        # Dims for S_5: 1, 4, 5, 6, 5, 4, 1
        expected = {(5,): 1, (4, 1): 4, (3, 2): 5, (3, 1, 1): 6,
                    (2, 2, 1): 5, (2, 1, 1, 1): 4, (1, 1, 1, 1, 1): 1}
        for lam, dim in expected.items():
            assert irrep_dimension(lam) == dim

    def test_s4_column_orthogonality(self):
        # Sum_lam chi_lam(C) * chi_lam(C) * |C| = |G| if C is identity class,
        # and for general column: sum_lam chi_lam(C)^2 = |C_G(C)| = |G|/|C|.
        table = CHARACTER_TABLES[4]
        order = factorial(4)
        for cls in partitions(4):
            s = sum(table[(lam, cls)] ** 2 for lam in partitions(4))
            cls_size = partition_class_size(cls, 4)
            expected = order // cls_size
            assert s == expected, f"column orthogonality fails at {cls}: {s} != {expected}"

    def test_s3_row_orthogonality(self):
        # Sum_C |C| * chi_lam(C) * chi_mu(C) = |G| delta_{lam,mu}
        table = CHARACTER_TABLES[3]
        order = factorial(3)
        parts = partitions(3)
        for lam in parts:
            for mu in parts:
                s = sum(partition_class_size(cls, 3)
                        * table[(lam, cls)] * table[(mu, cls)]
                        for cls in parts)
                expected = order if lam == mu else 0
                assert s == expected


# ============================================================
# Schur functor dimension (Weyl formula) tests
# ============================================================

class TestSchurFunctorDimension:

    def test_sym_n_dimension(self):
        # S^{(n)}(C^d) = Sym^n C^d has dimension C(d+n-1, n)
        for d in range(1, 5):
            for n in range(1, 6):
                expected = comb(d + n - 1, n)
                assert schur_functor_dim((n,), d) == expected

    def test_lambda_n_dimension(self):
        # S^{(1,...,1)}(C^d) = Lambda^n C^d has dim C(d, n)
        for d in range(1, 6):
            for n in range(1, d + 2):
                expected = comb(d, n)
                lam = tuple([1] * n)
                assert schur_functor_dim(lam, d) == expected

    def test_adjoint_of_sl2(self):
        # S^{(2,1)}(C^3) has dimension 8 (the adjoint of sl_3 uses (2,1))
        assert schur_functor_dim((2, 1), 3) == 8

    def test_trivial_schur(self):
        # S^{()}(C^d) = trivial, dim 1
        for d in range(1, 5):
            assert schur_functor_dim((), d) == 1

    def test_vanishing_when_too_many_rows(self):
        # S^lam(C^d) = 0 if len(lam) > d
        assert schur_functor_dim((1, 1, 1, 1), 3) == 0
        assert schur_functor_dim((2, 1, 1), 2) == 0


# ============================================================
# sl_2 Schur-Weyl decomposition tests
# ============================================================

class TestSL2SchurWeyl:

    def test_sl2_tensor_dim_3_to_n(self, sl2):
        # dim V^{tensor n} = 3^n
        for n in range(1, 6):
            assert sl2.tensor_dim(n) == 3 ** n

    def test_sl2_n2_decomposition(self, sl2):
        # V^2 = Sym^2 V + Lambda^2 V, dims 6 + 3 = 9
        decomp = sl2.irrep_decomposition(2)
        assert decomp == {(2,): 6, (1, 1): 3}

    def test_sl2_n3_decomposition(self, sl2):
        # V^3 = Sym^3 + Lambda^3 + 2*(standard x S_{(2,1)})
        # mult((3,)) = dim Sym^3 V = C(5,3) = 10
        # mult((1^3)) = dim Lambda^3 V = C(3,3) = 1
        # mult((2,1)) = dim S^{(2,1)}(V) = 8
        # Total dim: 10*1 + 8*2 + 1*1 = 10+16+1 = 27 = 3^3
        decomp = sl2.irrep_decomposition(3)
        assert decomp == {(3,): 10, (2, 1): 8, (1, 1, 1): 1}

    def test_sl2_n4_decomposition(self, sl2):
        decomp = sl2.irrep_decomposition(4)
        # Sym^4 V: C(6,4) = 15
        # Lambda^4 V: 0 (dim V = 3 < 4)
        assert (1, 1, 1, 1) not in decomp
        assert decomp[(4,)] == 15

    def test_sl2_n5_no_lambda(self, sl2):
        # Lambda^5 C^3 = 0
        decomp = sl2.irrep_decomposition(5)
        assert (1, 1, 1, 1, 1) not in decomp

    def test_sl2_schur_weyl_consistency(self, sl2):
        for n in range(2, 6):
            assert sl2.schur_weyl_consistency(n)

    def test_sl2_total_dim_identity(self, sl2):
        for n in range(2, 5):
            assert sl2.verify_decomposition_dimension(n)

    def test_sl2_shortcut_function(self):
        assert schur_weyl_sl2(3) == {(3,): 10, (2, 1): 8, (1, 1, 1): 1}

    def test_sl2_trivial_part_is_sym(self, sl2):
        for n in range(1, 5):
            expected = comb(3 + n - 1, n)
            assert sl2.trivial_part_dim(n) == expected

    def test_sl2_sign_part_is_exterior(self, sl2):
        # dim Lambda^n V = C(3, n) for n <= 3
        for n in range(1, 4):
            expected = comb(3, n)
            assert sl2.sign_part_dim(n) == expected
        # For n >= 4 the sign part vanishes
        assert sl2.sign_part_dim(4) == 0


# ============================================================
# sl_3 (higher rank) Schur-Weyl tests
# ============================================================

class TestSL3SchurWeyl:

    def test_sl3_n2_decomposition(self, sl3):
        decomp = sl3.irrep_decomposition(2)
        # Sym^2 C^8 = 36, Lambda^2 C^8 = 28
        assert decomp == {(2,): 36, (1, 1): 28}
        # Total = 64 = 8^2
        assert sum(m * irrep_dimension(lam) for lam, m in decomp.items()) == 64

    def test_sl3_n3_schur_weyl(self, sl3):
        for n in range(2, 4):
            assert sl3.schur_weyl_consistency(n)


# ============================================================
# Virasoro single-generator (dim V = 1, desusp deg = 1)
# ============================================================

class TestVirasoroSingle:

    def test_vir_single_tensor_dim(self, vir_single):
        # dim V^{tensor n} = 1 for all n (one-dimensional generator)
        for n in range(1, 5):
            assert vir_single.tensor_dim(n) == 1

    def test_vir_single_n2_is_sign(self, vir_single):
        # For desusp-deg-1, T tensor T has Koszul sign -1 under swap.
        # Therefore it sits in the sign irrep.
        decomp = vir_single.irrep_decomposition(2)
        assert decomp == {(1, 1): 1}

    def test_vir_single_n3_is_sign(self, vir_single):
        decomp = vir_single.irrep_decomposition(3)
        assert decomp == {(1, 1, 1): 1}

    def test_vir_single_n4_is_sign(self, vir_single):
        decomp = vir_single.irrep_decomposition(4)
        assert decomp == {(1, 1, 1, 1): 1}

    def test_vir_single_trivial_vanishes(self, vir_single):
        # The "trivial" isotypic for degree-1 generators corresponds to
        # Sym^n of an ungraded action, but with Koszul signs the role
        # is swapped. For a SINGLE degree-1 generator, there is no trivial.
        for n in range(2, 5):
            assert vir_single.trivial_part_dim(n) == 0


# ============================================================
# Virasoro multi-mode (arity 4 focus)
# ============================================================

class TestVirasoroArity4:

    def test_vir_modes_arity_4_h_8(self, vir_modes):
        # At weight 8: only (L_-2)^{tensor 4}, which sits in sign irrep.
        decomp = vir_modes.irrep_decomposition(4, weight=8)
        assert decomp == {(1, 1, 1, 1): 1}

    def test_vir_modes_arity_4_h_9(self, vir_modes):
        # At weight 9: need sum 9 = 2+2+2+3, permutations of (L_-2, L_-2, L_-2, L_-3)
        # Full tensor dim = C(4,1) = 4 (4 positions for the L_-3)
        decomp = vir_modes.irrep_decomposition(4, weight=9)
        total = sum(m * irrep_dimension(lam) for lam, m in decomp.items())
        assert total == 4

    def test_vir_modes_arity_4_h_14_has_trivial(self, vir_modes):
        # At weight 14: the smallest fully-distinct tuple (L_-2,L_-3,L_-4,L_-5)
        # sums to 14. The trivial irrep (4,) first appears here.
        decomp = vir_modes.irrep_decomposition(4, weight=14)
        assert (4,) in decomp

    def test_vir_modes_arity_3_total_dim(self, vir_modes):
        # Sum over all partitions should equal dim V_weight tensor^3
        for h in [6, 7, 8, 9, 10]:
            total = sum(m * irrep_dimension(lam)
                        for lam, m in vir_modes.irrep_decomposition(3, weight=h).items())
            assert total == vir_modes.tensor_dim(3, weight=h)

    def test_vir_modes_arity_4_total_dim(self, vir_modes):
        for h in range(8, 15):
            decomp = vir_modes.irrep_decomposition(4, weight=h)
            total = sum(m * irrep_dimension(lam) for lam, m in decomp.items())
            assert total == vir_modes.tensor_dim(4, weight=h)

    def test_virasoro_arity_4_shortcut(self):
        out = virasoro_arity_4_decomposition(max_weight=10)
        assert 8 in out
        assert out[8] == {(1, 1, 1, 1): 1}


# ============================================================
# Cyclic subgroup decomposition tests
# ============================================================

class TestCyclicDecomposition:

    def test_cyclic_sum_equals_tensor_dim(self, sl2):
        for n in range(2, 5):
            eigendims = sl2.cyclic_eigenspace_dims(n)
            total = sum(eigendims.values())
            assert total == sl2.tensor_dim(n)

    def test_cyclic_burnside_invariant(self, sl2):
        # C_n-invariant subspace = (1/n) sum_k tr(c_n^k)
        for n in range(2, 5):
            inv = sl2.cyclic_invariant_dim(n)
            # The invariant dim is also the 0-eigenspace
            eigendims = sl2.cyclic_eigenspace_dims(n)
            assert inv == eigendims[0]

    def test_cyclic_invariant_formula_sl2(self, sl2):
        # For ungraded S_n action on C^3 tensor^n, the cyclic invariant
        # count = (1/n) sum_{d|n} phi(n/d) * 3^d
        from math import gcd

        def euler_phi(m: int) -> int:
            if m == 1:
                return 1
            result = m
            p = 2
            mm = m
            while p * p <= mm:
                if mm % p == 0:
                    while mm % p == 0:
                        mm //= p
                    result -= result // p
                p += 1
            if mm > 1:
                result -= result // mm
            return result

        for n in range(2, 5):
            total = 0
            for d in range(1, n + 1):
                if n % d == 0:
                    total += euler_phi(n // d) * (3 ** d)
            expected = Fraction(total, n)
            assert sl2.cyclic_invariant_dim(n) == expected

    def test_cyclic_all_eigenspaces_nonnegative(self, sl2):
        for n in range(2, 5):
            eigs = sl2.cyclic_eigenspace_dims(n)
            for v in eigs.values():
                assert v >= 0

    def test_cyclic_virasoro_single(self, vir_single):
        # dim V = 1, so every tensor power is 1-dim.
        # Under c_n, the line is fixed (single element). Koszul sign of the
        # n-cycle on n degree-1 elements: n-cycle is (n-1) transpositions,
        # each giving Koszul sign -1 (since deg*deg=1). So c_n acts by (-1)^{n-1}.
        for n in range(2, 5):
            traces = vir_single.cyclic_character(n)
            # tr(c_n^k) on a 1-dim space = the scalar by which it acts.
            # c_n acts by (-1)^{n-1}
            expected_c1 = (-1) ** (n - 1)
            assert traces[0] == 1  # identity
            assert traces[1] == expected_c1

    def test_cyclic_shortcut_function(self):
        eigs = cyclic_decomposition_sl2(3)
        # Must sum to 27
        assert sum(eigs.values()) == 27


# ============================================================
# Frobenius characteristic tests
# ============================================================

class TestFrobeniusCharacteristic:

    def test_frobenius_equals_irrep_decomposition(self, sl2):
        for n in range(1, 5):
            assert (sl2.frobenius_characteristic(n)
                    == sl2.irrep_decomposition(n))

    def test_schur_coefficients_monotone(self, sl2):
        coeffs = sl2.schur_coefficients(4)
        assert coeffs[0] == {(): 1}
        assert coeffs[1] == {(1,): 3}  # 3 copies of trivial S_1
        assert (2,) in coeffs[2]


# ============================================================
# Character inner product / orthogonality tests
# ============================================================

class TestCharacterInnerProduct:

    def test_sl2_character_is_integer(self, sl2):
        for n in range(2, 5):
            char = sl2.character(n)
            for cls, val in char.items():
                assert val.denominator == 1

    def test_character_identity_equals_dim(self, sl2):
        for n in range(2, 5):
            char = sl2.character(n)
            id_cls = tuple([1] * n)
            assert char[id_cls] == sl2.tensor_dim(n)

    def test_multiplicities_are_nonnegative_integers(self, sl2):
        for n in range(2, 5):
            decomp = sl2.irrep_decomposition(n)
            for m in decomp.values():
                assert isinstance(m, int)
                assert m >= 0


# ============================================================
# Weight-filtered decomposition tests
# ============================================================

class TestWeightFilteredDecomp:

    def test_sl2_weight_filter_matches(self, sl2):
        # All sl2 generators are weight 1, so weight filter = n iff weight == n
        decomp_w3 = sl2.irrep_decomposition(3, weight=3)
        decomp_all = sl2.irrep_decomposition(3)
        assert decomp_w3 == decomp_all

    def test_sl2_weight_too_small(self, sl2):
        # n > weight: empty
        decomp = sl2.irrep_decomposition(3, weight=2)
        assert decomp == {}

    def test_vir_modes_weight_minimum(self, vir_modes):
        # arity 3 minimum weight = 2+2+2 = 6
        decomp = vir_modes.irrep_decomposition(3, weight=5)
        assert decomp == {}


# ============================================================
# Ordered vs unordered identity
# ============================================================

class TestOrderedUnorderedIdentity:

    def test_sl2_identity(self, sl2):
        for n in range(2, 5):
            d = sl2.ordered_unordered_identity(n)
            assert d['tensor_dim'] == 3 ** n
            assert d['schur_weyl_sum'] == 3 ** n
            assert d['sym_dim'] == comb(3 + n - 1, n)
            assert d['ext_dim'] == comb(3, n)

    def test_sl3_identity(self, sl3):
        d = sl3.ordered_unordered_identity(2)
        assert d['tensor_dim'] == 64
        assert d['sym_dim'] == 36
        assert d['ext_dim'] == 28

    def test_virasoro_single_identity_empty(self, vir_single):
        # desusp_deg != 0 returns empty dict
        assert vir_single.ordered_unordered_identity(2) == {}


# ============================================================
# Cross-engine consistency with ordered/unordered engine
# ============================================================

class TestOrderedUnorderedEngineConsistency:

    def test_sl2_unordered_equals_sign_isotypic(self):
        # For weight-1 (degree-0) generators, the unordered bar = Lambda^n V.
        # Cross-check: sign_part_dim of new engine should match dim Lambda^n(V)
        # of the existing engine at that weight (subsets).
        from compute.lib.bar_complex_ordered_unordered_engine import (
            OrderedUnorderedBarEngine,
        )
        old = OrderedUnorderedBarEngine('sl2', max_weight=4)
        new = SnBarIrrepEngine('sl2')
        # At n=2, weight=2: old engine gives unordered dim for subsets with
        # total weight 2 (i.e. pairs of distinct mode-1 generators).
        # The new engine's Lambda^2(V_gens at mode 1) = C(3,2) = 3.
        # Old unordered at (2, weight=2) = pairs (i,j), i<j with mode 1 each.
        # There are C(3,2) = 3.
        assert old.unordered_dim(2, 2) == 3
        assert new.sign_part_dim(2) == 3


# ============================================================
# S_n equivariance defect reporting
# ============================================================

class TestEquivarianceDefect:

    def test_sl2_defect_report(self, sl2):
        r = sl2.sn_equivariance_defect(3, 3)
        assert r['n_contractions'] == 2
        assert r['skew_sign'] == -1
        assert r['desuspension_degree'] == 0

    def test_vir_single_defect_report(self, vir_single):
        r = vir_single.sn_equivariance_defect(3, 6)
        assert r['desuspension_degree'] == 1


# ============================================================
# Koszul sign consistency (degree-0 vs degree-1)
# ============================================================

class TestKoszulSignConsistency:

    def test_single_generator_degree_0_is_trivial(self):
        # A single degree-0 generator: V = C, V^n = C for all n,
        # S_n acts trivially. Decomposition = (n,) with mult 1.
        class Stub(SnBarIrrepEngine):
            def __init__(self):
                self.algebra_type = 'stub'
                self.generators = [('x', 1, 0)]
                self.dim_v = 1
                self.desuspended_degree = 0
                self.generator_weight = 1
                self._weight_of_basis_vector = [1]
                self._basis_cache = {}
                self._action_cache = {}

        eng = Stub()
        for n in range(1, 5):
            decomp = eng.irrep_decomposition(n)
            assert decomp == {(n,): 1}

    def test_single_generator_degree_1_is_sign(self, vir_single):
        # A single degree-1 generator: V = C[1], V^n = C,
        # S_n acts by sign representation.
        for n in range(2, 5):
            decomp = vir_single.irrep_decomposition(n)
            assert decomp == {tuple([1] * n): 1}


# ============================================================
# Sanity smoke tests
# ============================================================

class TestSmoke:

    def test_engine_instantiation(self):
        SnBarIrrepEngine('sl2')
        SnBarIrrepEngine('sl3')
        SnBarIrrepEngine('virasoro_single')
        SnBarIrrepEngine('virasoro_modes', max_weight=6)

    def test_invalid_algebra(self):
        with pytest.raises(ValueError):
            SnBarIrrepEngine('foo')

    def test_character_raises_above_n_5(self, sl2):
        with pytest.raises(ValueError):
            sl2.character(6)


# ============================================================
# Multi-path verification: cross-checks between independent methods.
# Each test computes the SAME invariant by two or more routes and
# insists they agree. This is the multi-path verification mandate.
# ============================================================

class TestMultiPathVerification:

    def _euler_phi(self, m: int) -> int:
        if m == 1:
            return 1
        result = m
        p = 2
        mm = m
        while p * p <= mm:
            if mm % p == 0:
                while mm % p == 0:
                    mm //= p
                result -= result // p
            p += 1
        if mm > 1:
            result -= result // mm
        return result

    def test_sl2_sym_via_three_paths(self, sl2):
        # Path 1: engine's trivial_part_dim (character inner product)
        # Path 2: Weyl/SSYT formula schur_functor_dim((n,), 3)
        # Path 3: closed form C(d+n-1, n)
        for n in range(1, 6):
            p1 = sl2.trivial_part_dim(n)
            p2 = schur_functor_dim((n,), 3)
            p3 = comb(3 + n - 1, n)
            assert p1 == p2 == p3, f"n={n}: {p1}, {p2}, {p3}"

    def test_sl2_exterior_via_three_paths(self, sl2):
        # Path 1: engine's sign_part_dim
        # Path 2: Weyl formula for (1,...,1)
        # Path 3: closed form C(d, n)
        for n in range(1, 4):
            p1 = sl2.sign_part_dim(n)
            p2 = schur_functor_dim(tuple([1] * n), 3)
            p3 = comb(3, n)
            assert p1 == p2 == p3

    def test_sl2_standard_multiplicity_via_two_paths(self, sl2):
        # mult((2,1)) in V^{tensor 3} should equal dim S^{(2,1)}(C^3) = 8
        # Path 1: character inner product
        # Path 2: Weyl formula (SSYT count)
        p1 = sl2.irrep_decomposition(3).get((2, 1), 0)
        p2 = schur_functor_dim((2, 1), 3)
        assert p1 == p2 == 8

    def test_sl3_full_tensor_dim_via_two_paths(self, sl3):
        # Path 1: sum m(lam)*dim V_lam = 8^n
        # Path 2: direct enumeration d^n
        for n in range(2, 4):
            p1 = sum(m * irrep_dimension(lam)
                     for lam, m in sl3.irrep_decomposition(n).items())
            p2 = 8 ** n
            p3 = sl3.tensor_dim(n)
            assert p1 == p2 == p3

    def test_cyclic_invariant_three_ways(self, sl2):
        # Path 1: Burnside average over C_n traces
        # Path 2: Closed-form number-theoretic formula: (1/n) sum_{d|n} phi(n/d) d^gcd_count... wait
        # Path 3: 0-eigenspace dim from Fourier decomposition
        # Correct formula for number of C_n-invariants in V^{tensor n} with dim V=d:
        #   N(n) = (1/n) sum_{k=0}^{n-1} tr(c_n^k) = (1/n) sum_{d|n} phi(n/d) * d^{...}
        # Actually tr(c_n^k) = d^{gcd(n,k)}, so:
        #   N(n) = (1/n) sum_{k=0}^{n-1} d^{gcd(n,k)} = (1/n) sum_{d|n} phi(n/d) d^d_part
        # Let's use the direct formula: (1/n) sum_{k=0}^{n-1} d^{gcd(n,k)}
        for n in range(2, 5):
            d = 3
            p1 = sl2.cyclic_invariant_dim(n)
            p2_float = sum(d ** gcd_val for gcd_val in
                            [gcd_val_of(n, k) for k in range(n)]) / n
            p2 = Fraction(sum(d ** gcd_val_of(n, k) for k in range(n)), n)
            p3 = sl2.cyclic_eigenspace_dims(n)[0]
            assert p1 == p2 == p3

    def test_character_identity_three_ways(self, sl2):
        # Character of identity element = dim of representation.
        # Path 1: from character dict
        # Path 2: from tensor_dim
        # Path 3: sum of isotypic dimensions
        for n in range(2, 5):
            p1 = sl2.character(n)[tuple([1] * n)]
            p2 = Fraction(sl2.tensor_dim(n))
            p3 = Fraction(sum(sl2.isotypic_dim(n, lam) for lam in partitions(n)))
            assert p1 == p2 == p3

    def test_virasoro_single_sign_action_two_ways(self, vir_single):
        # Path 1: irrep_decomposition says sign irrep
        # Path 2: trace of identity = 1, trace of transposition = -1 (Koszul)
        for n in range(2, 5):
            p1 = vir_single.irrep_decomposition(n)
            assert p1 == {tuple([1] * n): 1}
            # Check the character: tr(transposition) should equal -1
            # since the single 1-dim basis vector picks up a Koszul minus sign.
            char = vir_single.character(n)
            id_cls = tuple([1] * n)
            # The transposition class is (2, 1^{n-2})
            if n >= 2:
                trans_cls = tuple([2] + [1] * (n - 2))
                assert char[id_cls] == 1
                assert char[trans_cls] == -1

    def test_sl2_decomposition_via_character_orthogonality(self, sl2):
        # For each irrep lam, multiplicity = <chi_V, chi_lam>.
        # Cross-check: manually compute the inner product and compare with
        # the engine's irrep_decomposition.
        n = 3
        char = sl2.character(n)
        table = CHARACTER_TABLES[3]
        for lam in partitions(n):
            ip = Fraction(0)
            for cls in partitions(n):
                ip += (Fraction(partition_class_size(cls, n))
                       * Fraction(table[(lam, cls)])
                       * char[cls])
            ip /= factorial(n)
            engine_mult = sl2.irrep_decomposition(n).get(lam, 0)
            assert int(ip) == engine_mult

    def test_virasoro_modes_arity_3_dim_match(self, vir_modes):
        # Path 1: sum m(lam) * dim V_lam over partitions
        # Path 2: direct tensor_basis enumeration
        # Path 3: number of weight-h n-multisets of Vir modes (weighted comp)
        for h in range(6, 11):
            p1 = sum(m * irrep_dimension(lam)
                     for lam, m in vir_modes.irrep_decomposition(3, weight=h).items())
            p2 = vir_modes.tensor_dim(3, weight=h)
            # Path 3: count ordered weight-h triples from {2,3,...,max}
            p3 = sum(1 for a in range(2, 11)
                     for b in range(2, 11)
                     for c in range(2, 11)
                     if a + b + c == h)
            assert p1 == p2 == p3

    def test_virasoro_modes_arity_4_dim_match(self, vir_modes):
        for h in range(8, 13):
            p1 = sum(m * irrep_dimension(lam)
                     for lam, m in vir_modes.irrep_decomposition(4, weight=h).items())
            p2 = vir_modes.tensor_dim(4, weight=h)
            # Path 3: count ordered weight-h 4-tuples
            p3 = sum(1 for a in range(2, 11)
                     for b in range(2, 11)
                     for c in range(2, 11)
                     for d in range(2, 11)
                     if a + b + c + d == h)
            assert p1 == p2 == p3

    def test_sl3_sym_two_ways(self, sl3):
        # Sym^n(C^8) via engine and closed form
        for n in range(1, 4):
            p1 = sl3.trivial_part_dim(n)
            p2 = comb(8 + n - 1, n)
            assert p1 == p2

    def test_sl3_exterior_two_ways(self, sl3):
        # Lambda^n(C^8)
        for n in range(1, 4):
            p1 = sl3.sign_part_dim(n)
            p2 = comb(8, n)
            assert p1 == p2

    def test_irrep_dimension_two_ways(self):
        # Path 1: character table (identity class)
        # Path 2: hook-length formula
        from compute.lib.sn_bar_irrep_decomp_engine import _hook_length_dimension
        for n in range(1, 6):
            for lam in partitions(n):
                p1 = irrep_dimension(lam)
                p2 = _hook_length_dimension(lam)
                assert p1 == p2, f"{lam}: table={p1}, hook={p2}"

    def test_sl2_n4_sum_of_squares(self, sl2):
        # Row-orthogonality consequence: sum_lam mult(lam)^2 <= (1/|G|) sum_C |C| chi_V(C)^2
        # But a cleaner identity: sum_lam mult(lam) * dim(V_lam) = dim V^{tensor n}
        decomp = sl2.irrep_decomposition(4)
        # Path 1: total dim via isotypic sum
        p1 = sum(m * irrep_dimension(lam) for lam, m in decomp.items())
        # Path 2: direct d^n
        p2 = 81
        # Path 3: tensor_dim
        p3 = sl2.tensor_dim(4)
        assert p1 == p2 == p3


def gcd_val_of(n: int, k: int) -> int:
    """gcd(n, k) with gcd(n, 0) := n."""
    from math import gcd
    if k == 0:
        return n
    return gcd(n, k)
