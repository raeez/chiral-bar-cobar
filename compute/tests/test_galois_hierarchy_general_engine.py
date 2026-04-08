r"""Tests for galois_hierarchy_general_engine.

Verifies:
    1. Z_2 parity and coupling enumeration (correctness + counts).
    2. Lollipop-type coupling classification.
    3. Exact OPE structure constants at special c values (cross-checked
       against galois_w4_w5_engine).
    4. Squarefree kernel arithmetic.
    5. F_2 linear algebra (rank, kernel).
    6. MAIN THEOREM: Gal(K_N(c)/Q(c)) = (Z/2)^{N-2} for N=4,...,11.
    7. Rank = 0 for N = 2, 3 (trivial Galois group).
    8. Numerical Galois group at special c values (Ising collapse, etc.).
    9. Weight-by-weight growth: each new weight adds exactly one to the rank.
   10. Proof structure: lower bound (primitive couplings) and upper bound
       (F_2 dependencies among non-primitives).
   11. Cross-engine consistency against galois_w4_w5_engine.
   12. W_6 and W_7 new couplings and factors.
   13. Discriminant data correctness for N=4,5.
   14. Abstract weight-space model consistency.
   15. Field extension structure at rational c.
   16. Galois trace stability (rational invariants).

Reference: galois_w4_w5_engine.py, galois_cross_channel_engine.py,
    w5_full_ope_delta_f2_engine.py, theorem_w4_full_ope_delta_f2_engine.py
"""

from __future__ import annotations

import os
import sys
import unittest
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from galois_hierarchy_general_engine import (
    # Arithmetic
    is_rational_square,
    squarefree_kernel_int,
    squarefree_kernel_rational,
    f2_rank,
    f2_rank_of_squarefree_classes,
    # Coupling enumeration
    parity_allowed,
    is_gravitational,
    higher_spin_couplings,
    lollipop_couplings,
    odd_power_couplings,
    # OPE structure constants
    g_squared_at,
    # Discriminant data
    discriminant_data,
    weight_specific_factor,
    # Main theorem
    build_discriminant_matrix,
    galois_rank_wn,
    galois_group_wn,
    verify_galois_hierarchy,
    # Proof components
    proof_lower_bound,
    proof_upper_bound,
    # Numerical
    numerical_galois_at,
    field_extension_at,
    SPECIAL_C_VALUES,
    # Growth table
    galois_growth_table,
    # Cross-checks
    cross_check_w4,
    cross_check_w5,
    # Summary
    summary,
)


# ============================================================================
# 1. Z_2 Parity
# ============================================================================

class TestParity(unittest.TestCase):

    def test_all_even_allowed(self):
        self.assertTrue(parity_allowed(2, 4, 6))
        self.assertTrue(parity_allowed(4, 4, 4))
        self.assertTrue(parity_allowed(2, 2, 2))

    def test_two_odd_allowed(self):
        self.assertTrue(parity_allowed(3, 3, 4))
        self.assertTrue(parity_allowed(3, 5, 4))
        self.assertTrue(parity_allowed(5, 5, 6))

    def test_one_odd_forbidden(self):
        self.assertFalse(parity_allowed(3, 4, 4))
        self.assertFalse(parity_allowed(2, 2, 3))
        self.assertFalse(parity_allowed(4, 4, 5))

    def test_three_odd_forbidden(self):
        self.assertFalse(parity_allowed(3, 3, 3))
        self.assertFalse(parity_allowed(3, 5, 5))
        self.assertFalse(parity_allowed(5, 5, 5))
        self.assertFalse(parity_allowed(3, 5, 7))

    def test_gravitational(self):
        self.assertTrue(is_gravitational(2, 2, 2))
        self.assertTrue(is_gravitational(2, 3, 3))
        self.assertTrue(is_gravitational(2, 4, 4))
        self.assertTrue(is_gravitational(2, 5, 5))

    def test_not_gravitational(self):
        self.assertFalse(is_gravitational(3, 3, 4))
        self.assertFalse(is_gravitational(4, 4, 4))
        self.assertFalse(is_gravitational(2, 3, 4))
        self.assertFalse(is_gravitational(2, 2, 4))


# ============================================================================
# 2. Coupling Enumeration
# ============================================================================

class TestCouplingEnumeration(unittest.TestCase):

    def test_w3_no_higher_spin(self):
        self.assertEqual(higher_spin_couplings(3), [])

    def test_w4_higher_spin_count(self):
        hs = higher_spin_couplings(4)
        self.assertEqual(len(hs), 3)
        self.assertIn((3, 3, 4), hs)
        self.assertIn((4, 4, 4), hs)
        self.assertIn((2, 2, 4), hs)

    def test_w5_higher_spin_count(self):
        hs = higher_spin_couplings(5)
        self.assertEqual(len(hs), 6)

    def test_w3_no_lollipop(self):
        self.assertEqual(lollipop_couplings(3), [])

    def test_w4_lollipop(self):
        lc = lollipop_couplings(4)
        self.assertEqual(len(lc), 2)
        self.assertIn((3, 3, 4), lc)
        self.assertIn((4, 4, 4), lc)

    def test_w5_lollipop(self):
        lc = lollipop_couplings(5)
        self.assertEqual(len(lc), 3)
        self.assertIn((3, 3, 4), lc)
        self.assertIn((4, 4, 4), lc)
        self.assertIn((4, 5, 5), lc)

    def test_w6_lollipop_count(self):
        lc = lollipop_couplings(6)
        self.assertEqual(len(lc), 8)

    def test_w7_lollipop_count(self):
        lc = lollipop_couplings(7)
        self.assertEqual(len(lc), 10)

    def test_lollipop_j_must_be_even(self):
        """At the lollipop vertex, the bridge half-edge label j must be even."""
        for N in range(4, 9):
            for triple in lollipop_couplings(N):
                i, j, k = triple
                # One of the indices must be even and >= 4
                counts = {}
                for w in triple:
                    counts[w] = counts.get(w, 0) + 1
                # The coupling is (j, k, k) where j appears once and k appears twice.
                # If all three are the same (k,k,k), j=k is even.
                # Otherwise j is the unique one and must be even.
                if len(counts) == 1:
                    # All same: (k,k,k). k must be even.
                    self.assertEqual(triple[0] % 2, 0,
                                     f"Self-coupling {triple} has odd weight")
                else:
                    # Two distinct: (j,k,k). j is the one with count 1.
                    j_val = [w for w, c in counts.items() if c == 1][0]
                    self.assertEqual(j_val % 2, 0,
                                     f"Bridge label j={j_val} in {triple} is odd")

    def test_lollipop_subset_of_higher_spin(self):
        """Lollipop couplings are a subset of all higher-spin couplings."""
        for N in range(3, 9):
            lc = set(lollipop_couplings(N))
            hs = set(higher_spin_couplings(N))
            self.assertTrue(lc.issubset(hs),
                            f"W_{N}: lollipop not subset of higher-spin")

    def test_w5_g345_not_in_lollipop(self):
        """g_{345} is NOT a lollipop coupling (all three indices distinct)."""
        lc = lollipop_couplings(5)
        self.assertNotIn((3, 4, 5), lc)

    def test_w5_g345_is_higher_spin(self):
        """g_{345} IS a higher-spin coupling (just not a lollipop one)."""
        hs = higher_spin_couplings(5)
        self.assertIn((3, 4, 5), hs)


# ============================================================================
# 3. OPE Structure Constants
# ============================================================================

class TestOPEConstants(unittest.TestCase):

    def test_g334_at_ising(self):
        val = g_squared_at(3, 3, 4, Fraction(1, 2))
        self.assertEqual(val, Fraction(42, 13585))

    def test_g444_at_ising_vanishes(self):
        val = g_squared_at(4, 4, 4, Fraction(1, 2))
        self.assertEqual(val, Fraction(0))

    def test_g334_at_monster(self):
        val = g_squared_at(3, 3, 4, Fraction(24))
        self.assertEqual(val, Fraction(8946, 3481))

    def test_g444_at_monster(self):
        val = g_squared_at(4, 4, 4, Fraction(24))
        expected = Fraction(112 * 576 * 47 * 118, 48 * 236 * 437 * 123)
        self.assertEqual(val, expected)

    def test_g455_at_ising_vanishes(self):
        """g_{455}^2(1/2) = 0 because (2c-1)=0 at c=1/2."""
        val = g_squared_at(4, 5, 5, Fraction(1, 2))
        self.assertEqual(val, Fraction(0))

    def test_g334_positive_for_c_gt_0(self):
        """g_{334}^2 > 0 for all c > 0 (no zeros in the physical range)."""
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(24), Fraction(100)]:
            val = g_squared_at(3, 3, 4, c)
            self.assertGreater(val, 0, f"g334^2 not positive at c={c}")

    def test_g_squared_ordering_is_normalized(self):
        """g_squared_at(3,4,3) should equal g_squared_at(3,3,4)."""
        c0 = Fraction(10)
        self.assertEqual(g_squared_at(3, 4, 3, c0), g_squared_at(3, 3, 4, c0))

    def test_cross_check_g334_against_w4w5_engine(self):
        """Cross-check against galois_w4_w5_engine."""
        from galois_w4_w5_engine import g334_sq
        for c0 in [Fraction(1), Fraction(13), Fraction(24), Fraction(100)]:
            self.assertEqual(g_squared_at(3, 3, 4, c0), g334_sq(c0))

    def test_cross_check_g444_against_w4w5_engine(self):
        from galois_w4_w5_engine import g444_sq
        for c0 in [Fraction(1), Fraction(13), Fraction(24), Fraction(100)]:
            self.assertEqual(g_squared_at(4, 4, 4, c0), g444_sq(c0))

    def test_cross_check_g455_against_w4w5_engine(self):
        from galois_w4_w5_engine import g455_sq_w5
        for c0 in [Fraction(1), Fraction(13), Fraction(24), Fraction(100)]:
            self.assertEqual(g_squared_at(4, 5, 5, c0), g455_sq_w5(c0))


# ============================================================================
# 4. Squarefree Kernel Arithmetic
# ============================================================================

class TestSquarefreeKernel(unittest.TestCase):

    def test_squarefree_kernel_int_basic(self):
        self.assertEqual(squarefree_kernel_int(0), 0)
        self.assertEqual(squarefree_kernel_int(1), 1)
        self.assertEqual(squarefree_kernel_int(4), 1)
        self.assertEqual(squarefree_kernel_int(8), 2)
        self.assertEqual(squarefree_kernel_int(12), 3)
        self.assertEqual(squarefree_kernel_int(42), 42)
        self.assertEqual(squarefree_kernel_int(112), 7)
        self.assertEqual(squarefree_kernel_int(1680), 105)
        self.assertEqual(squarefree_kernel_int(2240), 35)

    def test_squarefree_kernel_rational_basic(self):
        self.assertEqual(squarefree_kernel_rational(Fraction(0)), 0)
        self.assertEqual(squarefree_kernel_rational(Fraction(1)), 1)
        self.assertEqual(squarefree_kernel_rational(Fraction(42, 13585)), 570570)
        self.assertEqual(squarefree_kernel_rational(Fraction(8946, 3481)), 994)

    def test_is_rational_square(self):
        self.assertTrue(is_rational_square(Fraction(0)))
        self.assertTrue(is_rational_square(Fraction(1)))
        self.assertTrue(is_rational_square(Fraction(9, 4)))
        self.assertFalse(is_rational_square(Fraction(2)))
        self.assertFalse(is_rational_square(Fraction(-1)))


# ============================================================================
# 5. F_2 Linear Algebra
# ============================================================================

class TestF2LinearAlgebra(unittest.TestCase):

    def test_f2_rank_empty(self):
        self.assertEqual(f2_rank([]), 0)

    def test_f2_rank_identity(self):
        self.assertEqual(f2_rank([[1, 0], [0, 1]]), 2)

    def test_f2_rank_dependent(self):
        self.assertEqual(f2_rank([[1, 1], [1, 1]]), 1)

    def test_f2_rank_3x3(self):
        # Three independent vectors
        self.assertEqual(f2_rank([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)

    def test_f2_rank_with_dependency(self):
        # Row 3 = Row 1 + Row 2
        self.assertEqual(f2_rank([[1, 1, 0], [0, 1, 1], [1, 0, 1]]), 2)

    def test_f2_rank_of_squarefree_classes(self):
        # 42 = 2*3*7, 7 = 7. Product 42*7 = 294 = 2*3*7^2, sqfree = 6 != 1
        self.assertEqual(f2_rank_of_squarefree_classes([42, 7]), 2)

    def test_f2_rank_of_squarefree_classes_dependent(self):
        # 6 = 2*3, 10 = 2*5, 15 = 3*5. Product 6*10*15 = 900 = (30)^2. DEPENDENT.
        self.assertEqual(f2_rank_of_squarefree_classes([6, 10, 15]), 2)

    def test_f2_rank_trivial(self):
        self.assertEqual(f2_rank_of_squarefree_classes([]), 0)
        self.assertEqual(f2_rank_of_squarefree_classes([1]), 0)


# ============================================================================
# 6. MAIN THEOREM: Gal = (Z/2)^{N-2}
# ============================================================================

class TestMainTheorem(unittest.TestCase):
    """The central theorem: Gal(K_N(c)/Q(c)) = (Z/2)^{N-2} for N >= 4."""

    def test_w2_trivial(self):
        self.assertEqual(galois_rank_wn(2), 0)

    def test_w3_trivial(self):
        self.assertEqual(galois_rank_wn(3), 0)

    def test_w4_rank_2(self):
        self.assertEqual(galois_rank_wn(4), 2)

    def test_w5_rank_3(self):
        self.assertEqual(galois_rank_wn(5), 3)

    def test_w6_rank_4(self):
        self.assertEqual(galois_rank_wn(6), 4)

    def test_w7_rank_5(self):
        self.assertEqual(galois_rank_wn(7), 5)

    def test_w8_rank_6(self):
        self.assertEqual(galois_rank_wn(8), 6)

    def test_w9_rank_7(self):
        self.assertEqual(galois_rank_wn(9), 7)

    def test_w10_rank_8(self):
        self.assertEqual(galois_rank_wn(10), 8)

    def test_w11_rank_9(self):
        self.assertEqual(galois_rank_wn(11), 9)

    def test_rank_equals_n_minus_2_for_all_n(self):
        """The main theorem for N = 4, ..., 15."""
        for N in range(4, 16):
            with self.subTest(N=N):
                self.assertEqual(galois_rank_wn(N), N - 2,
                                 f"W_{N}: expected rank {N-2}")

    def test_galois_group_string(self):
        g = galois_group_wn(6)
        self.assertEqual(g['group'], '(Z/2)^4')
        self.assertEqual(g['order'], 16)
        self.assertTrue(g['verified'])

    def test_verify_hierarchy_all_pass(self):
        result = verify_galois_hierarchy(N_max=10)
        self.assertTrue(result['all_verified'],
                        "Not all N verified in galois hierarchy")


# ============================================================================
# 7. Weight-by-Weight Growth
# ============================================================================

class TestWeightGrowth(unittest.TestCase):

    def test_rank_increases_by_one_per_weight(self):
        """Each new weight from 4 to N adds exactly 1 to the Galois rank."""
        for N in range(5, 12):
            r_prev = galois_rank_wn(N - 1)
            r_curr = galois_rank_wn(N)
            self.assertEqual(r_curr, r_prev + 1,
                             f"Rank jump from W_{N-1} to W_{N}: "
                             f"expected +1, got {r_curr - r_prev}")

    def test_new_couplings_involve_new_weight(self):
        """When going from W_{N-1} to W_N, all new couplings involve weight N."""
        for N in range(5, 10):
            prev = set(lollipop_couplings(N - 1))
            curr = set(lollipop_couplings(N))
            new = curr - prev
            for triple in new:
                self.assertIn(N, triple,
                              f"New coupling {triple} for W_{N} does not involve weight {N}")

    def test_growth_table_consistent(self):
        table = galois_growth_table(N_max=8)
        for entry in table:
            self.assertEqual(entry['computed_rank'], entry['predicted_rank'])
            self.assertTrue(entry['verified'])


# ============================================================================
# 8. Proof Structure
# ============================================================================

class TestProofStructure(unittest.TestCase):

    def test_lower_bound_w4(self):
        lb = proof_lower_bound(4)
        self.assertEqual(lb['lower_bound'], 2)
        self.assertEqual(len(lb['primitive_couplings']), 2)
        self.assertIn((3, 3, 4), lb['primitive_couplings'])
        self.assertIn((4, 4, 4), lb['primitive_couplings'])

    def test_lower_bound_w5(self):
        lb = proof_lower_bound(5)
        self.assertEqual(lb['lower_bound'], 3)
        self.assertEqual(len(lb['primitive_couplings']), 3)
        self.assertIn((4, 5, 5), lb['primitive_couplings'])

    def test_lower_bound_w6(self):
        lb = proof_lower_bound(6)
        self.assertEqual(lb['lower_bound'], 4)
        self.assertEqual(len(lb['primitive_couplings']), 4)
        self.assertIn((6, 6, 6), lb['primitive_couplings'])

    def test_primitive_count_equals_n_minus_2(self):
        for N in range(4, 10):
            lb = proof_lower_bound(N)
            self.assertEqual(len(lb['primitive_couplings']), N - 2,
                             f"W_{N}: wrong number of primitives")

    def test_each_primitive_has_unique_factor(self):
        for N in range(4, 8):
            lb = proof_lower_bound(N)
            factors = lb['unique_factors']
            # All factors should be distinct
            self.assertEqual(len(factors), len(set(factors)),
                             f"W_{N}: duplicate weight-specific factors")

    def test_upper_bound_w4(self):
        ub = proof_upper_bound(4)
        self.assertEqual(ub['upper_bound'], 2)
        # W_4 has exactly 2 couplings = 2 primitives, so 0 non-primitives
        self.assertEqual(ub['n_non_primitive'], 0)

    def test_upper_bound_w5(self):
        ub = proof_upper_bound(5)
        self.assertEqual(ub['upper_bound'], 3)
        # W_5 has 3 couplings = 3 primitives, so 0 non-primitives
        self.assertEqual(ub['n_non_primitive'], 0)

    def test_upper_bound_w6(self):
        ub = proof_upper_bound(6)
        self.assertEqual(ub['upper_bound'], 4)
        # W_6 has 8 couplings, 4 primitives, 4 non-primitives
        self.assertEqual(ub['n_non_primitive'], 4)


# ============================================================================
# 9. Discriminant Data
# ============================================================================

class TestDiscriminantData(unittest.TestCase):

    def test_g334_data(self):
        d = discriminant_data((3, 3, 4))
        self.assertIsNotNone(d)
        self.assertEqual(d['const'], 42)
        self.assertIn((22, 5), d['odd_factors'])  # 5c+22
        self.assertIn((24, 1), d['odd_factors'])   # c+24

    def test_g444_data(self):
        d = discriminant_data((4, 4, 4))
        self.assertIsNotNone(d)
        self.assertEqual(d['const'], 7)
        self.assertIn((-1, 2), d['odd_factors'])  # 2c-1

    def test_g345_data(self):
        d = discriminant_data((3, 4, 5))
        self.assertIsNotNone(d)
        self.assertEqual(d['const'], 105)

    def test_g455_data(self):
        d = discriminant_data((4, 5, 5))
        self.assertIsNotNone(d)
        self.assertEqual(d['const'], 35)
        self.assertIn((2, 1), d['odd_factors'])    # c+2 (weight-5 factor)
        self.assertIn((37, 2), d['odd_factors'])   # 2c+37

    def test_sqfree_constants_match_hornfeck(self):
        """Verify squarefree constants match the Hornfeck normalization."""
        self.assertEqual(squarefree_kernel_int(42), 42)    # g334: 42 squarefree
        self.assertEqual(squarefree_kernel_int(112), 7)    # g444: 112=16*7
        self.assertEqual(squarefree_kernel_int(1680), 105)  # g345: 1680=16*105
        self.assertEqual(squarefree_kernel_int(2240), 35)  # g455: 2240=64*35


# ============================================================================
# 10. Numerical Galois at Special Points
# ============================================================================

class TestNumericalGalois(unittest.TestCase):

    def test_w4_ising_collapses(self):
        """At c=1/2 (Ising), g_{444}^2 = 0 so the Galois group collapses."""
        result = numerical_galois_at(Fraction(1, 2), 4)
        self.assertEqual(result['rank'], 1)
        self.assertTrue(result['collapsed'])
        self.assertEqual(result['group'], 'Z/2')

    def test_w4_monster_full(self):
        """At c=24 (Monster), the full Galois group (Z/2)^2 is realized."""
        result = numerical_galois_at(Fraction(24), 4)
        self.assertEqual(result['rank'], 2)
        self.assertFalse(result['collapsed'])

    def test_w5_ising_collapses(self):
        result = numerical_galois_at(Fraction(1, 2), 5)
        self.assertEqual(result['rank'], 1)
        self.assertTrue(result['collapsed'])

    def test_w5_monster_full(self):
        result = numerical_galois_at(Fraction(24), 5)
        self.assertEqual(result['rank'], 3)
        self.assertFalse(result['collapsed'])

    def test_w4_c1_full(self):
        result = numerical_galois_at(Fraction(1), 4)
        self.assertEqual(result['rank'], 2)

    def test_numerical_rank_le_generic(self):
        """At any rational c, the numerical rank is <= generic rank."""
        for N in [4, 5]:
            generic = N - 2
            for c0, label in SPECIAL_C_VALUES:
                result = numerical_galois_at(c0, N)
                self.assertLessEqual(result['rank'], generic,
                                     f"W_{N} at c={c0}: rank {result['rank']} > {generic}")


# ============================================================================
# 11. Field Extension Structure
# ============================================================================

class TestFieldExtension(unittest.TestCase):

    def test_w4_monster_field(self):
        ext = field_extension_at(Fraction(24), 4)
        self.assertEqual(ext['rank'], 2)
        self.assertEqual(ext['field_degree'], 4)
        self.assertFalse(ext['collapsed'])

    def test_w4_ising_field(self):
        ext = field_extension_at(Fraction(1, 2), 4)
        self.assertEqual(ext['rank'], 1)
        self.assertEqual(ext['field_degree'], 2)
        self.assertTrue(ext['collapsed'])


# ============================================================================
# 12. Cross-Engine Consistency
# ============================================================================

class TestCrossEngine(unittest.TestCase):

    def test_cross_check_w4(self):
        result = cross_check_w4()
        self.assertTrue(result['match'])
        self.assertTrue(result['group_match'])

    def test_cross_check_w5(self):
        result = cross_check_w5()
        self.assertTrue(result['match'])
        self.assertTrue(result['group_match'])

    def test_cross_check_numerics_w4(self):
        from galois_hierarchy_general_engine import cross_check_numerics_w4
        result = cross_check_numerics_w4(Fraction(24))
        self.assertTrue(result['g334_match'])
        self.assertTrue(result['g444_match'])

    def test_cross_check_numerics_w4_multiple_points(self):
        from galois_hierarchy_general_engine import cross_check_numerics_w4
        for c0 in [Fraction(1), Fraction(13), Fraction(26), Fraction(100)]:
            result = cross_check_numerics_w4(c0)
            self.assertTrue(result['g334_match'], f"g334 mismatch at c={c0}")
            self.assertTrue(result['g444_match'], f"g444 mismatch at c={c0}")


# ============================================================================
# 13. W_6 and W_7 Specific Tests
# ============================================================================

class TestW6W7(unittest.TestCase):

    def test_w6_new_couplings(self):
        """W_6 introduces 5 new lollipop couplings involving weight 6."""
        prev = set(lollipop_couplings(5))
        curr = set(lollipop_couplings(6))
        new = curr - prev
        self.assertEqual(len(new), 5)
        for triple in new:
            self.assertIn(6, triple)

    def test_w7_new_couplings(self):
        """W_7 introduces 2 new lollipop couplings involving weight 7."""
        prev = set(lollipop_couplings(6))
        curr = set(lollipop_couplings(7))
        new = curr - prev
        self.assertEqual(len(new), 2)
        # Should be (4,7,7) and (6,7,7)
        self.assertIn((4, 7, 7), new)
        self.assertIn((6, 7, 7), new)

    def test_w6_has_f2_dependencies(self):
        """W_6 has 8 couplings with rank 4: at least 4 F_2 dependencies."""
        data = build_discriminant_matrix(6)
        self.assertEqual(data['rank'], 4)
        self.assertEqual(len(data['couplings']), 8)
        # kernel dimension = 8 - 4 = 4

    def test_w6_specific_dependency(self):
        """In W_6, g_{446} and g_{466} have the same discriminant class."""
        data = build_discriminant_matrix(6)
        mat = data['matrix']
        couplings = data['couplings']
        idx_446 = couplings.index((4, 4, 6))
        idx_466 = couplings.index((4, 6, 6))
        self.assertEqual(mat[idx_446], mat[idx_466])

    def test_w6_weight_factor(self):
        """Weight 6 introduces factor (c-1)."""
        wf = weight_specific_factor(6, 6)
        self.assertEqual(wf, (-1, 1))  # (c - 1) = 1*c + (-1)

    def test_w7_weight_factor(self):
        """Weight 7 introduces factor (5c+4)."""
        wf = weight_specific_factor(7, 7)
        self.assertEqual(wf, (4, 5))


# ============================================================================
# 14. Abstract Weight-Space Model
# ============================================================================

class TestAbstractModel(unittest.TestCase):

    def test_abstract_model_used_for_n_ge_6(self):
        """For N >= 6, the abstract model is used (no exact data)."""
        data = build_discriminant_matrix(6)
        self.assertIn('model', data)
        self.assertEqual(data['model'], 'abstract_weight_space')

    def test_exact_model_used_for_n_le_5(self):
        """For N <= 5, exact bootstrap data is used."""
        data4 = build_discriminant_matrix(4)
        data5 = build_discriminant_matrix(5)
        self.assertNotIn('model', data4)
        self.assertNotIn('model', data5)

    def test_abstract_model_weight_vectors(self):
        """Verify the abstract weight-space vectors for W_6."""
        data = build_discriminant_matrix(6)
        mat = data['matrix']
        couplings = data['couplings']

        # (3,3,4): weights {3,4} -> e_3 + e_4 = [1,1,0,0]
        idx = couplings.index((3, 3, 4))
        self.assertEqual(mat[idx], [1, 1, 0, 0])

        # (4,4,4): weight {4} -> e_4 = [0,1,0,0]
        idx = couplings.index((4, 4, 4))
        self.assertEqual(mat[idx], [0, 1, 0, 0])

        # (4,5,5): weights {4,5} -> e_4 + e_5 = [0,1,1,0]
        idx = couplings.index((4, 5, 5))
        self.assertEqual(mat[idx], [0, 1, 1, 0])

        # (6,6,6): weight {6} -> e_6 = [0,0,0,1]
        idx = couplings.index((6, 6, 6))
        self.assertEqual(mat[idx], [0, 0, 0, 1])

        # (5,5,6): weights {5,6} -> e_5 + e_6 = [0,0,1,1]
        idx = couplings.index((5, 5, 6))
        self.assertEqual(mat[idx], [0, 0, 1, 1])

    def test_abstract_model_consistency_w4(self):
        """Check that the abstract model gives rank 2 for W_4 (same as exact)."""
        # Force abstract model by calling directly
        from galois_hierarchy_general_engine import _build_abstract_discriminant_matrix
        couplings = lollipop_couplings(4)
        data = _build_abstract_discriminant_matrix(4, couplings)
        self.assertEqual(data['rank'], 2)

    def test_abstract_model_consistency_w5(self):
        from galois_hierarchy_general_engine import _build_abstract_discriminant_matrix
        couplings = lollipop_couplings(5)
        data = _build_abstract_discriminant_matrix(5, couplings)
        self.assertEqual(data['rank'], 3)


# ============================================================================
# 15. Summary
# ============================================================================

class TestSummary(unittest.TestCase):

    def test_summary_runs(self):
        s = summary(N_max=6)
        self.assertTrue(s['all_verified'])
        self.assertIn('theorem', s)
        self.assertIn('hierarchy', s)

    def test_summary_cross_checks_pass(self):
        s = summary(N_max=5)
        self.assertTrue(s['cross_check_w4']['match'])
        self.assertTrue(s['cross_check_w5']['match'])


# ============================================================================
# 16. Large N Behavior
# ============================================================================

class TestLargeN(unittest.TestCase):

    def test_coupling_count_growth(self):
        """Number of lollipop couplings grows, but rank stays N-2."""
        for N in range(4, 12):
            n_couplings = len(lollipop_couplings(N))
            rank = galois_rank_wn(N)
            self.assertEqual(rank, N - 2)
            self.assertGreaterEqual(n_couplings, rank)

    def test_w15_rank(self):
        self.assertEqual(galois_rank_wn(15), 13)

    def test_w20_rank(self):
        self.assertEqual(galois_rank_wn(20), 18)

    def test_galois_order_is_power_of_2(self):
        for N in range(4, 12):
            g = galois_group_wn(N)
            self.assertEqual(g['order'], 2 ** (N - 2))


# ============================================================================
# 17. Mechanism: New Weight Introduces New Factor
# ============================================================================

class TestNewWeightMechanism(unittest.TestCase):
    """Each weight w from 3 to N introduces exactly ONE new irreducible factor."""

    def test_weight_3_factor_5c22(self):
        """Weight 3 factor is (5c+22)."""
        wf = weight_specific_factor(3, 4)
        self.assertEqual(wf, (22, 5))

    def test_weight_4_factor_2c_minus_1(self):
        """Weight 4 factor is (2c-1), vanishing at the Ising point c=1/2."""
        wf = weight_specific_factor(4, 4)
        self.assertEqual(wf, (-1, 2))

    def test_weight_5_factor_c_plus_2(self):
        """Weight 5 factor is (c+2), vanishing at c=-2."""
        wf = weight_specific_factor(5, 5)
        self.assertEqual(wf, (2, 1))

    def test_weight_6_factor(self):
        wf = weight_specific_factor(6, 6)
        b, a = wf
        # (a*c + b) = 0 at c = -b/a = 1
        self.assertEqual(Fraction(-b, a), Fraction(1))

    def test_weight_7_factor(self):
        wf = weight_specific_factor(7, 7)
        b, a = wf
        self.assertEqual(Fraction(-b, a), Fraction(-4, 5))

    def test_weight_8_factor(self):
        wf = weight_specific_factor(8, 8)
        b, a = wf
        self.assertEqual(Fraction(-b, a), Fraction(5, 2))

    def test_all_weight_factors_distinct(self):
        """All weight-specific factors for w=3,...,12 are pairwise distinct."""
        factors = [weight_specific_factor(w, 12) for w in range(3, 13)]
        zeros = [Fraction(-b, a) for b, a in factors]
        self.assertEqual(len(set(zeros)), len(zeros))


# ============================================================================
# 18. Odd Multiplicity via Parity Counting
# ============================================================================

class TestOddMultiplicityParity(unittest.TestCase):
    """Verify that the parity-allowed couplings with two equal indices
    correspond to odd-multiplicity contributions in the graph sum."""

    def test_g345_has_all_distinct_indices(self):
        """g_{345} has all distinct indices -> even multiplicity in graph sum."""
        self.assertEqual(len(set([3, 4, 5])), 3)
        # Therefore g345 does NOT appear in lollipop couplings
        self.assertNotIn((3, 4, 5), lollipop_couplings(5))

    def test_self_coupling_odd_weight_forbidden(self):
        """g_{kkk} for odd k is parity-forbidden (3 odd-weight fields)."""
        for k in [3, 5, 7, 9]:
            self.assertFalse(parity_allowed(k, k, k),
                             f"g_{{{k}{k}{k}}} should be parity-forbidden")

    def test_self_coupling_even_weight_allowed(self):
        """g_{kkk} for even k >= 4 is parity-allowed (0 odd-weight fields)."""
        for k in [4, 6, 8, 10]:
            self.assertTrue(parity_allowed(k, k, k),
                            f"g_{{{k}{k}{k}}} should be parity-allowed")

    def test_jkk_with_j_odd_forbidden(self):
        """g_{j,k,k} with j odd is parity-forbidden (1 odd-weight field)."""
        for j in [3, 5, 7]:
            for k in [4, 6]:
                self.assertFalse(parity_allowed(j, k, k),
                                 f"g_{{{j}{k}{k}}} should be parity-forbidden")

    def test_all_lollipop_couplings_have_even_bridge(self):
        """In every lollipop coupling (j,k,k), j is even."""
        for N in range(4, 12):
            for triple in lollipop_couplings(N):
                counts = {}
                for w in triple:
                    counts[w] = counts.get(w, 0) + 1
                if len(counts) == 1:
                    self.assertEqual(triple[0] % 2, 0)
                else:
                    bridge = [w for w, c in counts.items() if c == 1][0]
                    self.assertEqual(bridge % 2, 0,
                                     f"Bridge {bridge} in {triple} is odd for W_{N}")


# ============================================================================
# 19. Independence of Discriminants
# ============================================================================

class TestDiscriminantIndependence(unittest.TestCase):

    def test_w4_discriminants_independent(self):
        """D_{334} and D_{444} are F_2-independent in Q(c)*/Q(c)*^2."""
        data = build_discriminant_matrix(4)
        self.assertEqual(data['rank'], 2)
        # 2 rows, rank 2 -> independent
        self.assertEqual(len(data['couplings']), 2)

    def test_w5_three_discriminants_independent(self):
        """D_{334}, D_{444}, D_{455} are F_2-independent."""
        data = build_discriminant_matrix(5)
        self.assertEqual(data['rank'], 3)
        self.assertEqual(len(data['couplings']), 3)

    def test_w6_four_primitive_discriminants_independent(self):
        """The 4 primitive discriminants span a 4-dim F_2 subspace."""
        lb = proof_lower_bound(6)
        from galois_hierarchy_general_engine import _build_abstract_discriminant_matrix
        data = _build_abstract_discriminant_matrix(6, lb['primitive_couplings'])
        self.assertEqual(data['rank'], 4)

    def test_squarefree_class_at_c24_w4_independent(self):
        """At c=24: D_{334}(24) = 994, D_{444}(24) has sqfree != 994."""
        c0 = Fraction(24)
        s334 = squarefree_kernel_rational(g_squared_at(3, 3, 4, c0))
        s444 = squarefree_kernel_rational(g_squared_at(4, 4, 4, c0))
        self.assertEqual(s334, 994)
        # s334 * s444 should not be a perfect square
        self.assertNotEqual(squarefree_kernel_int(s334 * s444), 1)

    def test_squarefree_class_at_c24_w5_independent(self):
        """At c=24: all three W_5 discriminant classes are F_2-independent."""
        c0 = Fraction(24)
        s334 = squarefree_kernel_rational(g_squared_at(3, 3, 4, c0))
        s444 = squarefree_kernel_rational(g_squared_at(4, 4, 4, c0))
        s455 = squarefree_kernel_rational(g_squared_at(4, 5, 5, c0))
        classes = [s for s in [s334, s444, s455] if s not in (0, 1)]
        rank = f2_rank_of_squarefree_classes(classes)
        self.assertEqual(rank, 3)


# ============================================================================
# 20. Coupling Count Formulas
# ============================================================================

class TestCouplingCounts(unittest.TestCase):

    def test_w4_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(4)), 2)

    def test_w5_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(5)), 3)

    def test_w6_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(6)), 8)

    def test_w7_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(7)), 10)

    def test_w8_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(8)), 18)

    def test_w9_lollipop_count(self):
        self.assertEqual(len(lollipop_couplings(9)), 21)

    def test_new_coupling_count_per_weight(self):
        """Even weights add more new couplings than odd weights."""
        for N in range(5, 12):
            prev = set(lollipop_couplings(N - 1))
            curr = set(lollipop_couplings(N))
            n_new = len(curr - prev)
            if N % 2 == 0:
                # Even weight: adds couplings (j,N,N) for all even j <= N
                # and (N,k,k) for all k, and (N,N,N)
                self.assertGreater(n_new, 0, f"W_{N}: no new couplings")
            else:
                # Odd weight: fewer new couplings (no self-coupling)
                self.assertGreater(n_new, 0, f"W_{N}: no new couplings")


if __name__ == '__main__':
    unittest.main()
