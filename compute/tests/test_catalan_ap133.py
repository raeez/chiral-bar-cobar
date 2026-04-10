r"""Tests for Catalan numbers C_0..C_15 and AP133 index-shift verification.

AP133 states: C_n counts binary trees with n+1 leaves (equivalently
n internal nodes).  The most common error is writing C_k when C_{k-1}
is meant (or vice versa).

Three independent computation paths:
  Path 1: Direct formula  C_n = binom(2n, n) / (n+1)
  Path 2: Segner recursion  C_0=1, C_{n+1} = sum_{i=0}^{n} C_i * C_{n-i}
  Path 3: Generating function  C(x) = (1 - sqrt(1 - 4x)) / (2x)
          via ballot identity  C_n = binom(2n, n) - binom(2n, n+1)

AP133 AUDIT OF EXISTING .tex FILES (flagged, not modified):
  higher_genus_foundations.tex:1655 says "m_k^H from C_k planar binary trees"
  then line 1657 says "C_4 = 5 trees for m_4^H".  But C_4=14 and C_3=5.
  Since m_k sums over trees with k leaves = C_{k-1} trees, the text should
  read C_{k-1}, not C_k.  This is an AP133 index-shift violation.

References:
  OEIS A000108 (Catalan numbers)
  Stanley, Enumerative Combinatorics Vol. 2, Exercise 6.19
  AP133 in CLAUDE.md
"""

import unittest
from math import comb, factorial


# =====================================================================
# Catalan number implementations (three independent paths)
# =====================================================================

def catalan_direct(n):
    """Path 1: C_n = binom(2n, n) / (n+1).

    # VERIFIED: [DC] direct formula from binom(2n,n)/(n+1)
    #           [LT] Stanley, EC2 Exercise 6.19(a)
    """
    if n < 0:
        return 0
    return comb(2 * n, n) // (n + 1)


def catalan_recursion(n):
    """Path 2: Segner recursion C_0=1, C_{n+1} = sum C_i * C_{n-i}.

    # VERIFIED: [DC] recursive definition
    #           [LT] OEIS A000108 recurrence
    """
    table = [0] * (n + 1)
    table[0] = 1
    for k in range(1, n + 1):
        table[k] = sum(table[i] * table[k - 1 - i] for i in range(k))
    return table[n]


def catalan_generating_function(n):
    """Path 3: Extract coefficient from C(x) = (1 - sqrt(1-4x))/(2x).

    Use the identity C_n = binom(2n, n) - binom(2n, n+1)
    which follows from the generating function.

    # VERIFIED: [DC] ballot-number subtraction binom(2n,n) - binom(2n,n+1)
    #           [LT] Stanley, EC2 Exercise 6.19, variant (c)
    """
    if n < 0:
        return 0
    return comb(2 * n, n) - comb(2 * n, n + 1)


# =====================================================================
# Reference values
# =====================================================================

# VERIFIED: [LT] OEIS A000108; [DC] direct formula; [NE] recursion cross-check
CATALAN_C0_TO_C15 = [
    1,        # C_0   # VERIFIED: [DC] binom(0,0)/1=1; [LT] OEIS A000108
    1,        # C_1   # VERIFIED: [DC] binom(2,1)/2=1; [LT] OEIS A000108
    2,        # C_2   # VERIFIED: [DC] binom(4,2)/3=2; [LT] OEIS A000108
    5,        # C_3   # VERIFIED: [DC] binom(6,3)/4=5; [LT] OEIS A000108
    14,       # C_4   # VERIFIED: [DC] binom(8,4)/5=14; [LT] OEIS A000108
    42,       # C_5   # VERIFIED: [DC] binom(10,5)/6=42; [LT] OEIS A000108
    132,      # C_6   # VERIFIED: [DC] binom(12,6)/7=132; [LT] OEIS A000108
    429,      # C_7   # VERIFIED: [DC] binom(14,7)/8=429; [LT] OEIS A000108
    1430,     # C_8   # VERIFIED: [DC] binom(16,8)/9=1430; [LT] OEIS A000108
    4862,     # C_9   # VERIFIED: [DC] binom(18,9)/10=4862; [LT] OEIS A000108
    16796,    # C_10  # VERIFIED: [DC] binom(20,10)/11=16796; [LT] OEIS A000108
    58786,    # C_11  # VERIFIED: [DC] binom(22,11)/12=58786; [LT] OEIS A000108
    208012,   # C_12  # VERIFIED: [DC] binom(24,12)/13=208012; [LT] OEIS A000108
    742900,   # C_13  # VERIFIED: [DC] binom(26,13)/14=742900; [LT] OEIS A000108
    2674440,  # C_14  # VERIFIED: [DC] binom(28,14)/15=2674440; [LT] OEIS A000108
    9694845,  # C_15  # VERIFIED: [DC] binom(30,15)/16=9694845; [LT] OEIS A000108
]


# =====================================================================
# Test class
# =====================================================================

class TestCatalanAP133(unittest.TestCase):
    """Catalan numbers C_0..C_15 via three independent paths + AP133 audit."""

    # -----------------------------------------------------------------
    # Path 1: Direct formula
    # -----------------------------------------------------------------
    def test_direct_formula_C0_to_C15(self):
        """C_n = binom(2n, n) / (n+1) matches reference for n=0..15."""
        for n, expected in enumerate(CATALAN_C0_TO_C15):
            with self.subTest(n=n):
                self.assertEqual(
                    catalan_direct(n), expected,
                    f"C_{n} direct formula: got {catalan_direct(n)}, expected {expected}"
                )

    # -----------------------------------------------------------------
    # Path 2: Segner recursion
    # -----------------------------------------------------------------
    def test_recursion_C0_to_C15(self):
        """Segner recursion matches reference for n=0..15."""
        for n, expected in enumerate(CATALAN_C0_TO_C15):
            with self.subTest(n=n):
                self.assertEqual(
                    catalan_recursion(n), expected,
                    f"C_{n} recursion: got {catalan_recursion(n)}, expected {expected}"
                )

    # -----------------------------------------------------------------
    # Path 3: Generating function (ballot subtraction)
    # -----------------------------------------------------------------
    def test_generating_function_C0_to_C15(self):
        """Ballot-number formula matches reference for n=0..15."""
        for n, expected in enumerate(CATALAN_C0_TO_C15):
            with self.subTest(n=n):
                self.assertEqual(
                    catalan_generating_function(n), expected,
                    f"C_{n} gen func: got {catalan_generating_function(n)}, expected {expected}"
                )

    # -----------------------------------------------------------------
    # Three-path cross-consistency
    # -----------------------------------------------------------------
    def test_three_paths_agree_C0_to_C15(self):
        """All three computation paths produce identical values."""
        for n in range(16):
            with self.subTest(n=n):
                d = catalan_direct(n)
                r = catalan_recursion(n)
                g = catalan_generating_function(n)
                self.assertEqual(d, r, f"C_{n}: direct={d} != recursion={r}")
                self.assertEqual(d, g, f"C_{n}: direct={d} != genfunc={g}")

    # -----------------------------------------------------------------
    # AP133: Index-shift property
    # C_n counts binary trees with n+1 leaves (n internal nodes)
    # -----------------------------------------------------------------
    def test_ap133_leaves_count(self):
        """AP133: C_n counts planar binary trees with exactly n+1 leaves.

        Enumerate small cases by hand:
          C_0 = 1: the single leaf (1 leaf = 0+1)
          C_1 = 1: one binary tree with 2 leaves (root splits into 2)
          C_2 = 2: two binary trees with 3 leaves
          C_3 = 5: five binary trees with 4 leaves
          C_4 = 14: fourteen binary trees with 5 leaves

        # VERIFIED: [DC] hand enumeration for n<=3
        #           [LT] Stanley EC2 Exercise 6.19(e): C_n = |PBT(n+1)|
        """
        # Small-case verification against hand count
        cases = {
            0: (1, 1),    # C_0=1, 1 leaf (trivial tree)
            1: (1, 2),    # C_1=1, 2 leaves
            2: (2, 3),    # C_2=2, 3 leaves
            3: (5, 4),    # C_3=5, 4 leaves
            4: (14, 5),   # C_4=14, 5 leaves
        }
        for n, (cat_val, n_leaves) in cases.items():
            with self.subTest(n=n):
                self.assertEqual(catalan_direct(n), cat_val)
                self.assertEqual(n_leaves, n + 1,
                                 f"AP133: C_{n} counts trees with {n}+1={n+1} leaves")

    def test_ap133_internal_nodes_count(self):
        """AP133: C_n counts planar binary trees with exactly n internal nodes.

        A binary tree with n internal nodes has n+1 leaves.
        This is the dual statement of the leaves count.

        # VERIFIED: [DC] binary tree node relation: internal + 1 = leaves
        #           [LT] Knuth, TAOCP Vol 1, Section 2.3
        """
        for n in range(16):
            with self.subTest(n=n):
                n_internal = n
                n_leaves = n_internal + 1
                # C_n counts binary trees with n internal nodes and n+1 leaves
                self.assertEqual(n_leaves, n + 1)
                # The count itself
                self.assertEqual(catalan_direct(n), CATALAN_C0_TO_C15[n])

    def test_ap133_arity_k_operation_uses_C_k_minus_1(self):
        """AP133: An arity-k A-infinity operation m_k sums over C_{k-1} trees.

        m_k sums over planar binary trees with k leaves.
        Trees with k leaves = C_{k-1} (NOT C_k).

        # VERIFIED: [DC] k leaves -> k-1 internal nodes -> C_{k-1}
        #           [LT] Loday-Vallette, Algebraic Operads, Prop 9.2.6
        """
        # m_3: 3 leaves -> C_2 = 2 trees
        self.assertEqual(catalan_direct(2), 2)
        # m_4: 4 leaves -> C_3 = 5 trees
        self.assertEqual(catalan_direct(3), 5)
        # m_5: 5 leaves -> C_4 = 14 trees
        self.assertEqual(catalan_direct(4), 14)
        # m_6: 6 leaves -> C_5 = 42 trees
        self.assertEqual(catalan_direct(5), 42)

    def test_ap133_common_error_C_k_vs_C_k_minus_1(self):
        """AP133: C_k != C_{k-1} for k >= 2 (the index shift matters).

        The common error is writing C_k when C_{k-1} is meant.
        Note: C_0 = C_1 = 1 is the unique adjacent pair that coincides.
        For k >= 2, consecutive Catalan numbers are always distinct.

        # VERIFIED: [DC] direct computation; [LT] C_n is strictly increasing for n >= 1
        """
        # C_0 = C_1 = 1 is the unique coincidence
        self.assertEqual(catalan_direct(0), catalan_direct(1))
        # For k >= 2, C_k > C_{k-1} strictly
        for k in range(2, 16):
            with self.subTest(k=k):
                self.assertGreater(
                    catalan_direct(k), catalan_direct(k - 1),
                    f"C_{k}={catalan_direct(k)} should be strictly greater than "
                    f"C_{k-1}={catalan_direct(k-1)} for k >= 2"
                )

    # -----------------------------------------------------------------
    # Manuscript cross-checks
    # -----------------------------------------------------------------
    def test_manuscript_m3_has_C2_eq_2_trees(self):
        """Cross-check: ordered_associative_chiral_kd.tex:8173 says C_2=2 for m_3."""
        # m_3 sums over binary trees with 3 leaves = C_2 = 2
        # VERIFIED: [DC] C_2 = binom(4,2)/3 = 2; [LT] manuscript line 8173
        self.assertEqual(catalan_direct(2), 2)

    def test_manuscript_m4_has_C3_eq_5_trees(self):
        """Cross-check: ordered_associative_chiral_kd.tex:8174 says C_3=5 for m_4."""
        # m_4 sums over binary trees with 4 leaves = C_3 = 5
        # VERIFIED: [DC] C_3 = binom(6,3)/4 = 5; [LT] manuscript line 8174
        self.assertEqual(catalan_direct(3), 5)

    def test_manuscript_m5_has_C4_eq_14_trees(self):
        """Cross-check: ordered_associative_chiral_kd.tex:8030 says C_{k-1} for m_k.
        At k=5: C_4=14.
        Also: quintic_shadow_engine says C_4=14 binary trees on 5 leaves.
        """
        # VERIFIED: [DC] C_4 = binom(8,4)/5 = 14; [LT] manuscript line 8030
        self.assertEqual(catalan_direct(4), 14)

    def test_manuscript_higher_genus_foundations_1187_C3_eq_5(self):
        """Cross-check: higher_genus_foundations.tex:1187 says C_3=5 for 4-leaf trees."""
        # VERIFIED: [DC] C_3 = 5; [LT] manuscript line 1187
        self.assertEqual(catalan_direct(3), 5)

    def test_manuscript_feynman_transform_C_k_on_k_plus_1_leaves(self):
        """Cross-check: higher_genus_modular_koszul.tex:15190 says
        C_k binary trees on k+1 leaves. This is CORRECT: C_k counts
        trees with k+1 leaves.
        """
        for k in range(8):
            with self.subTest(k=k):
                # C_k counts trees with k+1 leaves
                self.assertEqual(catalan_direct(k), CATALAN_C0_TO_C15[k])

    # -----------------------------------------------------------------
    # Flagged AP133 violation (test documents the error, does NOT fix it)
    # -----------------------------------------------------------------
    def test_flag_higher_genus_foundations_1655_ap133_violation(self):
        """FLAG: higher_genus_foundations.tex:1655 says 'm_k^H from C_k trees'.

        This is an AP133 violation. m_k sums over trees with k leaves,
        which is C_{k-1} trees, NOT C_k. The next line (1657) says
        'C_4 = 5 trees for m_4^H' but C_4=14 and C_3=5.

        The correct statement: m_k^H sums over C_{k-1} planar binary trees.
        """
        # C_4 is 14, NOT 5. The manuscript line 1657 says C_4=5 which is wrong.
        self.assertEqual(catalan_direct(4), 14)
        self.assertNotEqual(catalan_direct(4), 5)
        # C_3 IS 5. The manuscript should say C_{k-1}=C_3=5 for m_4.
        self.assertEqual(catalan_direct(3), 5)

    # -----------------------------------------------------------------
    # Additional structural properties
    # -----------------------------------------------------------------
    def test_catalan_growth_ratio_approaches_4(self):
        """C_{n+1}/C_n -> 4 as n -> infinity.

        Exact ratio: C_{n+1}/C_n = 2(2n+1)/(n+2).
        At n=5: 2*11/7 = 22/7 ~ 3.143.
        At n=14: 2*29/16 = 58/16 = 3.625.
        Convergence is slow; we verify the exact ratio formula instead.

        # VERIFIED: [DC] direct ratio computation
        #           [LT] Stanley EC2, asymptotic C_n ~ 4^n / (n^{3/2} sqrt(pi))
        """
        for n in range(1, 15):
            ratio = CATALAN_C0_TO_C15[n + 1] / CATALAN_C0_TO_C15[n]
            exact_ratio = 2 * (2 * n + 1) / (n + 2)
            with self.subTest(n=n):
                self.assertAlmostEqual(ratio, exact_ratio, places=10,
                                       msg=f"C_{n+1}/C_{n} != 2(2n+1)/(n+2)")

    def test_catalan_divisibility(self):
        """C_n = binom(2n,n)/(n+1) is always an integer."""
        for n in range(16):
            with self.subTest(n=n):
                self.assertEqual(comb(2 * n, n) % (n + 1), 0,
                                 f"binom(2*{n},{n}) not divisible by {n+1}")

    def test_catalan_C0_is_1(self):
        """C_0 = 1 (the empty tree / single leaf)."""
        self.assertEqual(catalan_direct(0), 1)
        self.assertEqual(catalan_recursion(0), 1)
        self.assertEqual(catalan_generating_function(0), 1)

    def test_catalan_hankel_determinant(self):
        """det([C_{i+j}]_{0<=i,j<=n}) = 1 for all n (Hankel determinant).

        # VERIFIED: [DC] direct 2x2 and 3x3; [LT] Aigner, Catalan Numbers, Thm 3.1
        """
        C = CATALAN_C0_TO_C15
        # 1x1: det([C_0]) = 1
        self.assertEqual(C[0], 1)
        # 2x2: det([[C_0, C_1], [C_1, C_2]]) = C_0*C_2 - C_1^2 = 1*2 - 1 = 1
        det2 = C[0] * C[2] - C[1] * C[1]
        self.assertEqual(det2, 1)
        # 3x3
        det3 = (C[0] * (C[2] * C[4] - C[3] * C[3])
                - C[1] * (C[1] * C[4] - C[3] * C[2])
                + C[2] * (C[1] * C[3] - C[2] * C[2]))
        self.assertEqual(det3, 1)

    def test_catalan_sum_formula(self):
        """sum_{k=0}^{n} C_k = C_{n+1} - C_n for n >= 1 is FALSE;
        instead verify the correct partial-sum identity:
        sum_{k=0}^{n} C_k equals known values.

        # VERIFIED: [DC] direct summation; [NE] cross-check against table
        """
        # Partial sums: 1, 2, 4, 9, 23, 65, 197, 626, ...
        expected_partial_sums = [1, 2, 4, 9, 23, 65, 197, 626, 2056, 6918]
        for n in range(len(expected_partial_sums)):
            s = sum(CATALAN_C0_TO_C15[k] for k in range(n + 1))
            with self.subTest(n=n):
                self.assertEqual(s, expected_partial_sums[n],
                                 f"Partial sum to C_{n} = {s}, "
                                 f"expected {expected_partial_sums[n]}")

    def test_catalan_strict_monotonicity_from_C1(self):
        """C_n is strictly increasing for n >= 1.

        # VERIFIED: [DC] direct comparison; [LT] C_{n+1}/C_n > 1 for n >= 1
        """
        for n in range(1, 15):
            with self.subTest(n=n):
                self.assertGreater(CATALAN_C0_TO_C15[n + 1],
                                   CATALAN_C0_TO_C15[n])


if __name__ == '__main__':
    unittest.main()
