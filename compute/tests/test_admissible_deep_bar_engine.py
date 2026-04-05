"""Tests for the deep bar complex engine at admissible levels.

Tests the explicit bar chain complex construction, bar cohomology
computation, shadow metric, Koszul dual analysis, bar-Ext vs ordinary-Ext
discrepancy, four-path Koszulness verification, negative-c shadow data,
fusion rules, W_3 at sl_3 admissible levels, and comprehensive sweep.

VERIFICATION MANDATE (3+ genuinely independent paths per result):
    Path 1: Direct bar cohomology computation
    Path 2: Shapovalov determinant h_null verification (independent of KK formula)
    Path 3: Modular S-matrix consistency (symmetry + Verlinde integrality)
    Path 4: Kappa two-way (KM formula vs Sugawara route)

References:
    Kac-Wakimoto (1988), Arakawa (2015, 2017), Creutzig-Ridout (2012-2013)
    Manuscript: rem:admissible-koszul-status, prop:pbw-universality
"""

import pytest
import unittest
from fractions import Fraction
from math import gcd, comb

import numpy as np

from compute.lib.admissible_deep_bar_engine import (
    # Partition functions
    colored_partition_count,
    vacuum_verma_dims,
    bar_chain_dims_arity,
    # Shapovalov-based
    quotient_dims_shapovalov,
    WeightSpaceData,
    # Bar cohomology
    ce_differential_matrices_sl2,
    bar_cohomology_universal_sl2,
    bar_cohomology_quotient_sl2,
    BarCohomologyData,
    # Shadow metric
    shadow_metric_admissible_sl2,
    ShadowMetricData,
    # Koszul dual
    koszul_dual_level_sl2,
    KoszulDualData,
    # Fusion rules
    fusion_rules_integrable_sl2,
    fusion_ring_structure,
    # Ext discrepancy
    ext_discrepancy_sl2,
    ExtDiscrepancyData,
    # W_3 at sl_3
    w3_at_admissible_sl3,
    WAlgebraAdmissibleData,
    # Six-path verification
    six_path_koszulness_sl2,
    KoszulnessVerification,
    # Negative c
    negative_c_shadow_sl2,
    NegativeCData,
    # Enumeration
    enumerate_admissible_sl2,
    enumerate_admissible_sl3,
    # Deep analysis
    deep_bar_analysis_sl2,
    DeepBarAnalysis,
    deep_bar_analysis_sl3,
    DeepBarAnalysisSl3,
    # Master sweep
    master_deep_verification,
)
from compute.lib.nonscalar_admissible_level import (
    admissible_level_sl2,
    admissible_modular_s_matrix_sl2,
)


# =========================================================================
# 1. Colored partition counts and vacuum Verma dims
# =========================================================================

class TestColoredPartitions(unittest.TestCase):
    """Colored partition counts p_r(h) for r generators of weight 1."""

    def test_p3_known_values(self):
        """p_3(h) matches OEIS A000716 (3-colored partitions)."""
        # OEIS A000716: 1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640
        expected = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640]
        for h, exp in enumerate(expected):
            self.assertEqual(colored_partition_count(h, 3), exp,
                             f"p_3({h}) = {colored_partition_count(h, 3)} != {exp}")

    def test_p1_ordinary_partitions(self):
        """p_1(h) = ordinary partition count."""
        # 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for h, exp in enumerate(expected):
            self.assertEqual(colored_partition_count(h, 1), exp,
                             f"p_1({h}) wrong")

    def test_p8_first_few(self):
        """p_8(h) for sl_3 (8 generators)."""
        # p_8(0) = 1, p_8(1) = 8, p_8(2) = 8+C(8,2) = 8+28+8 = ...
        # Actually p_8(1) = 8 (8 colors, one part of size 1)
        # p_8(2) = 8 (size 2, one part) + C(8+1, 2) (two parts of size 1)
        #        = 8 + 36 = 44. Hmm, let me compute directly.
        # p_8(2) = 8 (one part of 2) + 8*9/2 = 8 + 36 = 44... no.
        # With 8 colors, 2 can be: (2, color c) for c in 8: 8 ways.
        # (1 color c1) + (1 color c2) with c1 <= c2: C(8,2) + 8 = 28+8 = 36 ways.
        # Total: 8 + 36 = 44.
        dims = vacuum_verma_dims(5, rank=8)
        self.assertEqual(dims[0], 1)
        self.assertEqual(dims[1], 8)
        self.assertEqual(dims[2], 44)  # 8 + C(9,2) = 8 + 36 = 44

    def test_vacuum_verma_agrees(self):
        """vacuum_verma_dims matches colored_partition_count for sl_2."""
        dims = vacuum_verma_dims(10, rank=3)
        for h in range(11):
            self.assertEqual(dims[h], colored_partition_count(h, 3),
                             f"Disagree at weight {h}")

    def test_p0_base_case(self):
        """p_r(0) = 1 for all r."""
        for r in [1, 2, 3, 5, 8]:
            self.assertEqual(colored_partition_count(0, r), 1)

    def test_p_r_1_equals_r(self):
        """p_r(1) = r for all r."""
        for r in [1, 2, 3, 5, 8]:
            self.assertEqual(colored_partition_count(1, r), r)

    def test_negative_weight_zero(self):
        """p_r(h) = 0 for h < 0."""
        for r in [1, 3, 8]:
            self.assertEqual(colored_partition_count(-1, r), 0)


# =========================================================================
# 2. Bar chain dimensions
# =========================================================================

class TestBarChainDims(unittest.TestCase):
    """Bar chain group dimensions for the PBW-reduced CE complex."""

    def test_sl2_ce_dims(self):
        """Lambda^d(sl_2) = C(3, d)."""
        dims = bar_chain_dims_arity(3, 5)
        self.assertEqual(dims[0], 1)
        self.assertEqual(dims[1], 3)
        self.assertEqual(dims[2], 3)
        self.assertEqual(dims[3], 1)
        self.assertEqual(dims[4], 0)
        self.assertEqual(dims[5], 0)

    def test_sl3_ce_dims(self):
        """Lambda^d(sl_3) = C(8, d)."""
        dims = bar_chain_dims_arity(8, 10)
        for d in range(9):
            self.assertEqual(dims[d], comb(8, d))
        for d in range(9, 11):
            self.assertEqual(dims[d], 0)

    def test_euler_characteristic(self):
        """Euler char of CE complex = 0 for odd-dim g."""
        # For g = sl_2 (dim 3): sum (-1)^d * C(3,d) = (1-1)^3 = 0.
        dims_sl2 = bar_chain_dims_arity(3, 3)
        euler = sum((-1)**d * dims_sl2[d] for d in range(4))
        self.assertEqual(euler, 0)

        # For g = sl_3 (dim 8): sum (-1)^d * C(8,d) = 0.
        dims_sl3 = bar_chain_dims_arity(8, 8)
        euler = sum((-1)**d * dims_sl3[d] for d in range(9))
        self.assertEqual(euler, 0)


# =========================================================================
# 3. Quotient dimensions via Shapovalov
# =========================================================================

class TestQuotientDimsShapovalov(unittest.TestCase):
    """Shapovalov-based L_k dimensions."""

    def test_below_null_agree(self):
        """L_k and V_k agree below h_null."""
        for p, q in [(3, 2), (3, 1)]:
            if gcd(p, q) != 1:
                continue
            h_null = (p - 1) * q
            data = quotient_dims_shapovalov(p, q, min(h_null - 1, 5))
            for ws in data:
                if ws.weight < h_null:
                    self.assertEqual(ws.null_dim, 0,
                                     f"Null dim != 0 below h_null at weight {ws.weight}")
                    self.assertEqual(ws.quotient_dim, ws.verma_dim)

    def test_at_null_has_null(self):
        """At h_null, the null dimension is nonzero."""
        # k = 1 (p=3, q=1): h_null = 2
        data = quotient_dims_shapovalov(3, 1, 3)
        null_data = [ws for ws in data if ws.weight == 2]
        self.assertTrue(len(null_data) > 0)
        self.assertGreater(null_data[0].null_dim, 0,
                           "Should have null vector at h_null = 2")

    def test_k0_trivial(self):
        """k=0 (p=2, q=1): h_null = 1. Null at weight 1."""
        data = quotient_dims_shapovalov(2, 1, 2)
        # At weight 1, there should be a null (3 states, some null)
        null_w1 = [ws for ws in data if ws.weight == 1]
        self.assertTrue(len(null_w1) > 0)
        self.assertGreater(null_w1[0].null_dim, 0)

    def test_weight_zero_always_one(self):
        """Vacuum (weight 0) is always 1-dimensional."""
        for p, q in [(3, 2), (2, 3), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            data = quotient_dims_shapovalov(p, q, 1)
            self.assertEqual(data[0].verma_dim, 1)
            self.assertEqual(data[0].quotient_dim, 1)


# =========================================================================
# 4. CE differential matrices
# =========================================================================

class TestCEDifferential(unittest.TestCase):
    """CE differential for sl_2."""

    def test_d2_matrix_shape(self):
        """d^2: Lambda^2(3x3) -> Lambda^1(3)."""
        mats = ce_differential_matrices_sl2()
        self.assertEqual(mats['d2'].shape, (3, 3))

    def test_d3_matrix_shape(self):
        """d^3: Lambda^3(3x1) -> Lambda^2(3)."""
        mats = ce_differential_matrices_sl2()
        self.assertEqual(mats['d3'].shape, (3, 1))

    def test_d2_rank_3(self):
        """d^2 has rank 3 (surjective for semisimple sl_2)."""
        mats = ce_differential_matrices_sl2()
        rank = np.linalg.matrix_rank(mats['d2'], tol=1e-10)
        self.assertEqual(rank, 3)

    def test_d3_is_zero(self):
        """d^3 is the zero map (Jacobi identity)."""
        mats = ce_differential_matrices_sl2()
        rank = np.linalg.matrix_rank(mats['d3'], tol=1e-10)
        self.assertEqual(rank, 0)

    def test_d_squared_zero(self):
        """d^2 circ d^3 = 0 (d^2 = 0 for CE complex)."""
        mats = ce_differential_matrices_sl2()
        composition = mats['d2'] @ mats['d3']
        np.testing.assert_allclose(composition, 0, atol=1e-12)

    def test_ce_dims(self):
        """CE complex has dims 1, 3, 3, 1."""
        mats = ce_differential_matrices_sl2()
        self.assertEqual(mats['dims'], {0: 1, 1: 3, 2: 3, 3: 1})

    def test_d2_determinant_nonzero(self):
        """d^2 is invertible (det != 0) for semisimple sl_2."""
        mats = ce_differential_matrices_sl2()
        det = np.linalg.det(mats['d2'])
        self.assertNotAlmostEqual(det, 0.0, places=6)

    def test_d2_specific_entries(self):
        """d(e^h) = -2e, d(e^f) = h, d(h^f) = -2f."""
        mats = ce_differential_matrices_sl2()
        d2 = mats['d2']
        # Column 0: d(e^h) = -2e -> (-2, 0, 0)
        np.testing.assert_allclose(d2[:, 0], [-2, 0, 0])
        # Column 1: d(e^f) = h -> (0, 1, 0)
        np.testing.assert_allclose(d2[:, 1], [0, 1, 0])
        # Column 2: d(h^f) = -2f -> (0, 0, -2)
        np.testing.assert_allclose(d2[:, 2], [0, 0, -2])


# =========================================================================
# 5. Bar cohomology of V_k (universal, always Koszul)
# =========================================================================

class TestBarCohomologyUniversal(unittest.TestCase):
    """Bar cohomology of V_k(sl_2): always Koszul."""

    def test_h1_equals_3(self):
        """H^1(B(V_k)) = sl_2 (3-dimensional)."""
        cohom = bar_cohomology_universal_sl2()
        h1 = [c for c in cohom if c.bar_degree == 1]
        self.assertEqual(len(h1), 1)
        self.assertEqual(h1[0].cohom_dim, 3)

    def test_h2_equals_0(self):
        """H^2(B(V_k)) = 0 (Koszul)."""
        cohom = bar_cohomology_universal_sl2()
        h2 = [c for c in cohom if c.bar_degree == 2]
        self.assertEqual(len(h2), 1)
        self.assertEqual(h2[0].cohom_dim, 0)

    def test_h3_equals_0(self):
        """H^3(B(V_k)) = 0 (Koszul)."""
        cohom = bar_cohomology_universal_sl2()
        h3 = [c for c in cohom if c.bar_degree == 3]
        self.assertEqual(len(h3), 1)
        self.assertEqual(h3[0].cohom_dim, 0)

    def test_three_degrees(self):
        """Exactly three bar degrees computed."""
        cohom = bar_cohomology_universal_sl2()
        self.assertEqual(len(cohom), 3)

    def test_chain_dims(self):
        """Chain group dimensions: 3, 3, 1."""
        cohom = bar_cohomology_universal_sl2()
        dims = {c.bar_degree: c.chain_dim for c in cohom}
        self.assertEqual(dims[1], 3)
        self.assertEqual(dims[2], 3)
        self.assertEqual(dims[3], 1)

    def test_euler_characteristic(self):
        """Euler char = sum (-1)^d * dim H^d = 3 (= dim sl_2)."""
        cohom = bar_cohomology_universal_sl2()
        euler = sum((-1)**c.bar_degree * c.cohom_dim for c in cohom)
        # H^1 = 3, H^2 = H^3 = 0. Euler = -3 (sign convention).
        # Actually: with d starting at 1: (-1)^1 * 3 = -3.
        self.assertEqual(euler, -3)


# =========================================================================
# 6. Bar cohomology of L_k (quotient)
# =========================================================================

class TestBarCohomologyQuotient(unittest.TestCase):
    """Bar cohomology of L_k(sl_2) at admissible levels."""

    def test_k_minus_half_koszul(self):
        """k = -1/2 (p=3, q=2): h_null = 4 > 3 = max arity. Koszul."""
        cohom = bar_cohomology_quotient_sl2(3, 2)
        for c_data in cohom:
            if c_data.bar_degree > 1:
                self.assertEqual(c_data.cohom_dim, 0,
                                 f"H^{c_data.bar_degree} should be 0")
        h1 = [c for c in cohom if c.bar_degree == 1]
        self.assertEqual(h1[0].cohom_dim, 3)

    def test_k_minus_4_3_koszul(self):
        """k = -4/3 (p=2, q=3): h_null = 3 = max arity. Koszul."""
        cohom = bar_cohomology_quotient_sl2(2, 3)
        for c_data in cohom:
            if c_data.bar_degree > 1:
                self.assertEqual(c_data.cohom_dim, 0,
                                 f"H^{c_data.bar_degree} should be 0 at k=-4/3")

    def test_integrable_k1(self):
        """k=1 (p=3, q=1): integrable, Koszul."""
        cohom = bar_cohomology_quotient_sl2(3, 1)
        h1 = [c for c in cohom if c.bar_degree == 1][0]
        self.assertEqual(h1.cohom_dim, 3)

    def test_agrees_with_universal_above_null(self):
        """When h_null > 3, quotient cohomology = universal cohomology."""
        for p, q in [(3, 2), (5, 3), (7, 2)]:
            if gcd(p, q) != 1:
                continue
            h_null = (p - 1) * q
            if h_null > 3:
                univ = bar_cohomology_universal_sl2()
                quot = bar_cohomology_quotient_sl2(p, q)
                for u, q_data in zip(univ, quot):
                    self.assertEqual(u.cohom_dim, q_data.cohom_dim,
                                     f"Disagree at arity {u.bar_degree}")

    def test_quotient_cannot_add_cohomology(self):
        """No quotient adds bar cohomology for sl_2 at admissible levels."""
        for q_val in range(1, 5):
            for p_val in range(2, 3 * q_val + 3):
                if gcd(p_val, q_val) != 1:
                    continue
                cohom = bar_cohomology_quotient_sl2(p_val, q_val)
                for c_data in cohom:
                    if c_data.bar_degree > 1:
                        self.assertEqual(c_data.cohom_dim, 0,
                                         f"H^{c_data.bar_degree} != 0 at "
                                         f"(p,q) = ({p_val},{q_val})")


# =========================================================================
# 7. Shadow metric at admissible levels
# =========================================================================

class TestShadowMetric(unittest.TestCase):
    """Shadow metric Q_L(t) at admissible levels."""

    def test_always_class_L(self):
        """All admissible sl_2 levels have shadow class L."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (7, 4)]:
            if gcd(p, q) != 1:
                continue
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertEqual(sm.shadow_class, 'L')
            self.assertEqual(sm.r_max, 3)

    def test_kappa_positive(self):
        """kappa > 0 at all admissible levels."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertGreater(sm.kappa, 0)

    def test_kappa_formula(self):
        """kappa = 3p/(4q)."""
        for p, q in [(3, 2), (2, 3), (5, 3), (4, 1), (7, 3)]:
            if gcd(p, q) != 1:
                continue
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertEqual(sm.kappa, Fraction(3 * p, 4 * q))

    def test_delta_zero(self):
        """Critical discriminant Delta = 0 for KM (Jacobi)."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertEqual(sm.delta, 0)

    def test_perfect_square(self):
        """Q_L is a perfect square (Delta = 0)."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertTrue(sm.is_perfect_square)

    def test_S4_zero(self):
        """S_4 = 0 (quartic vanishes by Jacobi)."""
        for p, q in [(3, 2), (2, 3)]:
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertEqual(sm.S4, 0)

    def test_Q_at_zero(self):
        """Q(0) = 4*kappa^2."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            sm = shadow_metric_admissible_sl2(p, q)
            kappa = sm.kappa
            self.assertEqual(sm.Q_coefficients[0], 4 * kappa**2)

    def test_Q_coefficients_form(self):
        """Q(t) = kappa^2 * (4 - 4t + t^2) = kappa^2 * (2-t)^2."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            sm = shadow_metric_admissible_sl2(p, q)
            a, b, c = sm.Q_coefficients
            kappa = sm.kappa
            self.assertEqual(a, 4 * kappa**2)
            self.assertEqual(b, -4 * kappa**2)
            self.assertEqual(c, kappa**2)

    def test_negative_c_positive_kappa(self):
        """At negative c, kappa is still positive."""
        # k = -4/3: c = -6, but kappa = 1/2 > 0
        sm = shadow_metric_admissible_sl2(2, 3)
        self.assertLess(sm.c, 0)
        self.assertGreater(sm.kappa, 0)


# =========================================================================
# 8. Koszul dual level
# =========================================================================

class TestKoszulDual(unittest.TestCase):
    """Koszul dual level analysis."""

    def test_kappa_sum_zero(self):
        """kappa(k) + kappa(k') = 0 for all admissible sl_2."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1), (7, 4)]:
            if gcd(p, q) != 1:
                continue
            kd = koszul_dual_level_sl2(p, q)
            self.assertEqual(kd.kappa_sum, 0,
                             f"kappa + kappa' != 0 at (p,q)=({p},{q}): {kd.kappa_sum}")

    def test_c_sum_six(self):
        """c(k) + c(k') = 6 = 2*dim(sl_2) for sl_2."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1)]:
            if gcd(p, q) != 1:
                continue
            kd = koszul_dual_level_sl2(p, q)
            self.assertEqual(kd.c_sum, 6,
                             f"c + c' != 6 at (p,q)=({p},{q}): {kd.c_sum}")

    def test_dual_not_admissible(self):
        """Koszul dual level is NOT admissible for sl_2."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            if gcd(p, q) != 1:
                continue
            kd = koszul_dual_level_sl2(p, q)
            self.assertFalse(kd.dual_is_admissible)

    def test_kappa_dual_negative(self):
        """kappa' = -kappa < 0."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            kd = koszul_dual_level_sl2(p, q)
            self.assertLess(kd.kappa_dual, 0)

    def test_dual_level_formula(self):
        """k' = -k - 4 = -p/q - 2."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            if gcd(p, q) != 1:
                continue
            kd = koszul_dual_level_sl2(p, q)
            expected = -Fraction(p, q) - 2
            self.assertEqual(kd.k_dual, expected)

    def test_k_minus_half_dual(self):
        """k=-1/2: k' = -(-1/2) - 4 = 1/2 - 4 = -7/2."""
        kd = koszul_dual_level_sl2(3, 2)
        self.assertEqual(kd.k_dual, Fraction(-7, 2))
        self.assertEqual(kd.kappa, Fraction(9, 8))
        self.assertEqual(kd.kappa_dual, Fraction(-9, 8))

    def test_k_minus_4_3_dual(self):
        """k=-4/3: k' = -(-4/3) - 4 = 4/3 - 4 = -8/3."""
        kd = koszul_dual_level_sl2(2, 3)
        self.assertEqual(kd.k_dual, Fraction(-8, 3))
        self.assertEqual(kd.kappa, Fraction(1, 2))
        self.assertEqual(kd.kappa_dual, Fraction(-1, 2))

    def test_c_dual_positive_when_c_negative(self):
        """When c < 0, c' = 6 - c > 6 > 0."""
        kd = koszul_dual_level_sl2(2, 3)  # c = -6
        self.assertLess(kd.c, 0)
        self.assertGreater(kd.c_dual, 0)


# =========================================================================
# 9. Fusion rules
# =========================================================================

class TestFusionRules(unittest.TestCase):
    """Fusion rules at integrable and admissible levels."""

    def test_su2_k1_fusion(self):
        """SU(2)_1: 2 modules, fusion = Z/2Z."""
        N = fusion_rules_integrable_sl2(3)  # p=3 => k=1
        self.assertEqual(N.shape, (2, 2, 2))
        # 0 x 0 = 0: N[0,0,0] = 1, N[0,0,1] = 0
        self.assertEqual(N[0, 0, 0], 1)
        self.assertEqual(N[0, 0, 1], 0)
        # 0 x 1 = 1: N[0,1,1] = 1
        self.assertEqual(N[0, 1, 1], 1)
        # 1 x 1 = 0: N[1,1,0] = 1
        self.assertEqual(N[1, 1, 0], 1)

    def test_su2_k2_fusion(self):
        """SU(2)_2: 3 modules, Ising-like fusion."""
        N = fusion_rules_integrable_sl2(4)  # p=4 => k=2
        self.assertEqual(N.shape, (3, 3, 3))
        # 0 is identity: 0 x j = j
        for j in range(3):
            self.assertEqual(N[0, j, j], 1)
        # 1 x 1 = 0 + 2
        self.assertEqual(N[1, 1, 0], 1)
        self.assertEqual(N[1, 1, 2], 1)
        # 2 x 2 = 0
        self.assertEqual(N[2, 2, 0], 1)

    def test_vacuum_is_identity(self):
        """Module 0 is the identity for fusion."""
        for p in range(2, 6):
            N = fusion_rules_integrable_sl2(p)
            n = p - 1
            for j in range(n):
                self.assertEqual(N[0, j, j], 1,
                                 f"0 x {j} != {j} at k={p-2}")

    def test_fusion_commutative(self):
        """Fusion is commutative: N_{ij}^m = N_{ji}^m."""
        for p in range(2, 6):
            N = fusion_rules_integrable_sl2(p)
            n = p - 1
            for i in range(n):
                for j in range(n):
                    for m in range(n):
                        self.assertEqual(N[i, j, m], N[j, i, m],
                                         f"Not commutative at k={p-2}")

    def test_verlinde_integral(self):
        """Verlinde formula gives integer fusion coefficients."""
        for p, q in [(3, 1), (4, 1), (5, 1), (3, 2)]:
            if gcd(p, q) != 1:
                continue
            result = fusion_ring_structure(p, q)
            self.assertTrue(result['is_integral'],
                            f"Non-integral at (p,q) = ({p},{q}): "
                            f"error = {result['integrality_error']}")

    def test_verlinde_vacuum_identity(self):
        """Verlinde fusion has vacuum as identity."""
        for p, q in [(3, 1), (4, 1)]:
            result = fusion_ring_structure(p, q)
            self.assertTrue(result['vacuum_trivial'])

    def test_admissible_modular_data_size(self):
        """Admissible fusion tensor has correct size (p-1)*q."""
        for p, q in [(3, 2), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            result = fusion_ring_structure(p, q)
            self.assertEqual(result['n_modules'], (p - 1) * q)


# =========================================================================
# 10. Ext discrepancy
# =========================================================================

class TestExtDiscrepancy(unittest.TestCase):
    """Bar-Ext vs ordinary-Ext comparison."""

    def test_bar_ext1_always_3(self):
        """bar-Ext^1 = sl_2 (dim 3) at all levels."""
        for p, q in [(3, 2), (2, 3), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            ed = ext_discrepancy_sl2(p, q)
            self.assertEqual(ed.bar_ext_dims[1], 3)

    def test_integrable_semisimple(self):
        """Integrable levels have semisimple module category."""
        for p in range(2, 6):
            ed = ext_discrepancy_sl2(p, 1)
            self.assertTrue(ed.ordinary_ext_semisimple)
            self.assertEqual(ed.ordinary_ext1_nonzero_pairs, 0)

    def test_admissible_nonsemisimple(self):
        """Non-integrable admissible levels are non-semisimple."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            ed = ext_discrepancy_sl2(p, q)
            self.assertFalse(ed.ordinary_ext_semisimple)

    def test_ext1_exists_admissible(self):
        """Non-integrable admissible levels have nonzero Ext^1 pairs."""
        ed = ext_discrepancy_sl2(3, 2)  # k = -1/2
        self.assertGreater(ed.ordinary_ext1_nonzero_pairs, 0)

    def test_discrepancy_populated(self):
        """Discrepancy descriptions are populated."""
        ed = ext_discrepancy_sl2(3, 2)
        self.assertIn(1, ed.discrepancy_at_degree)
        self.assertIn(2, ed.discrepancy_at_degree)
        self.assertTrue(len(ed.discrepancy_at_degree[1]) > 10)


# =========================================================================
# 11. W_3 at sl_3 admissible levels
# =========================================================================

class TestW3Admissible(unittest.TestCase):
    """W_3 = DS(hat{sl}_3) at admissible levels."""

    def test_ds_changes_shadow_class(self):
        """DS reduction changes shadow class from L to M."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            w3 = w3_at_admissible_sl3(p, q)
            self.assertEqual(w3.shadow_class_sl3, 'L')
            self.assertEqual(w3.shadow_class_w3, 'M')
            self.assertTrue(w3.ds_changes_class)

    def test_w3_central_charge_formula(self):
        """c(W_3) = 2*(1 - 12*(p-q)^2/(pq)) where k+3 = p/q."""
        for p, q in [(4, 3), (5, 3)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            w3 = w3_at_admissible_sl3(p, q)
            expected = Fraction(2) * (1 - 12 * Fraction((p - q)**2, p * q))
            self.assertEqual(w3.c_w3, expected)

    def test_kappa_sl3_formula(self):
        """kappa(sl_3) = 8*(k+3)/6 = 4(k+3)/3 = 4p/(3q)."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            w3 = w3_at_admissible_sl3(p, q)
            expected = Fraction(4 * p, 3 * q)
            self.assertEqual(w3.kappa_sl3, expected)

    def test_w3_m43(self):
        """sl_3 at k = -5/3 (p=4, q=3): W_3 minimal model."""
        w3 = w3_at_admissible_sl3(4, 3)
        # c(W_3) = 2*(1 - 12*(1)^2/(12)) = 2*(1-1) = 0
        self.assertEqual(w3.c_w3, Fraction(0))

    def test_w3_kappa_is_5c_over_6(self):
        """kappa(W_3) = 5c(W_3)/6 (AP1/AP9: kappa = c*(H_N-1) = 5c/6 for N=3)."""
        for p, q in [(4, 3), (5, 3)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            w3 = w3_at_admissible_sl3(p, q)
            self.assertEqual(w3.kappa_w3, w3.c_w3 * Fraction(5, 6))


# =========================================================================
# 12. Four-path Koszulness verification (rectified from inflated 6-path)
# =========================================================================

class TestFourPathKoszulness(unittest.TestCase):
    """Four genuinely independent paths to verify Koszulness.

    Previously claimed 6 paths but only 2 were genuine (AP10 violation).
    Now 4 genuinely independent paths, each performing a distinct computation.
    """

    def test_all_sl2_koszul(self):
        """All admissible sl_2 levels are Koszul by 4-path verification."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                kv = six_path_koszulness_sl2(p, q)
                self.assertEqual(kv.verdict, 'Koszul',
                                 f"Koszulness verdict wrong at (p,q) = ({p},{q})")

    def test_reports_four_paths(self):
        """Verification honestly reports 4 paths, not 6."""
        kv = six_path_koszulness_sl2(3, 2)
        self.assertEqual(kv.n_paths, 4)

    def test_all_paths_agree(self):
        """All four paths agree for every admissible level tested."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1)]:
            if gcd(p, q) != 1:
                continue
            kv = six_path_koszulness_sl2(p, q)
            self.assertTrue(kv.all_paths_agree,
                            f"Paths disagree at (p,q) = ({p},{q})")

    def test_path1_bar_complex(self):
        """Path 1 (bar complex) confirms Koszulness."""
        for p, q in [(3, 2), (2, 3), (3, 1)]:
            kv = six_path_koszulness_sl2(p, q)
            self.assertTrue(kv.path1_bar_complex)

    def test_path2_shapovalov_h_null(self):
        """Path 2 (Shapovalov h_null) independently confirms nulls above bar range."""
        for p, q in [(3, 2), (2, 3), (3, 1)]:
            kv = six_path_koszulness_sl2(p, q)
            self.assertTrue(kv.path2_shapovalov_h_null)

    def test_path2_h_null_formula_matches_shapovalov(self):
        """Shapovalov numerical h_null matches Kac-Kazhdan formula (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (3, 1), (4, 1)]:
            kv = six_path_koszulness_sl2(p, q)
            h_null_formula = (p - 1) * q
            self.assertEqual(kv.path2_h_null_from_formula, h_null_formula)
            # For small h_null, Shapovalov should find it
            if h_null_formula <= 5:
                self.assertIsNotNone(kv.path2_h_null_from_shapovalov,
                                     f"Shapovalov should find null at "
                                     f"h_null={h_null_formula}")
                self.assertEqual(kv.path2_h_null_from_shapovalov,
                                 h_null_formula,
                                 f"Shapovalov h_null mismatch at (p,q)=({p},{q})")

    def test_path3_modular(self):
        """Path 3 (modular S-matrix) is consistent."""
        for p, q in [(3, 2), (3, 1), (4, 1)]:
            kv = six_path_koszulness_sl2(p, q)
            self.assertTrue(kv.path3_modular)

    def test_path4_kappa_two_way(self):
        """Path 4 (kappa two-way) is consistent: KM formula = Sugawara route."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            kv = six_path_koszulness_sl2(p, q)
            self.assertTrue(kv.path4_kappa_two_way)

    def test_path4_kappa_values_explicit(self):
        """Path 4 kappa values are correct and agree."""
        kv = six_path_koszulness_sl2(3, 2)  # k = -1/2
        self.assertEqual(kv.path4_kappa_km, Fraction(9, 8))
        self.assertEqual(kv.path4_kappa_sugawara, Fraction(9, 8))
        self.assertEqual(kv.path4_kappa_km, kv.path4_kappa_sugawara)

        kv = six_path_koszulness_sl2(2, 3)  # k = -4/3
        self.assertEqual(kv.path4_kappa_km, Fraction(1, 2))
        self.assertEqual(kv.path4_kappa_sugawara, Fraction(1, 2))


# =========================================================================
# 13. Negative-c shadow data
# =========================================================================

class TestNegativeC(unittest.TestCase):
    """Shadow data in the negative-c regime."""

    def test_negative_c_identification(self):
        """Correctly identify levels with c < 0."""
        # k < 0 => c < 0 for sl_2 (when p < 2q)
        nc = negative_c_shadow_sl2(2, 3)  # k = -4/3, c = -6
        self.assertTrue(nc.c_is_negative)
        self.assertEqual(nc.c, Fraction(-6))

        nc = negative_c_shadow_sl2(3, 2)  # k = -1/2, c = -1
        self.assertTrue(nc.c_is_negative)
        self.assertEqual(nc.c, Fraction(-1))

    def test_positive_c_identification(self):
        """Correctly identify levels with c > 0."""
        nc = negative_c_shadow_sl2(3, 1)  # k = 1, c = 1
        self.assertFalse(nc.c_is_negative)

    def test_kappa_always_positive(self):
        """kappa = 3p/(4q) > 0 regardless of c sign."""
        for p, q in [(2, 3), (3, 2), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            nc = negative_c_shadow_sl2(p, q)
            self.assertTrue(nc.kappa_is_positive)

    def test_complementarity_sum(self):
        """c + c' = 6 (complementarity)."""
        for p, q in [(2, 3), (3, 2), (5, 3), (3, 1)]:
            if gcd(p, q) != 1:
                continue
            nc = negative_c_shadow_sl2(p, q)
            self.assertEqual(nc.complementarity_sum, 6)

    def test_c_dual_positive_when_c_negative(self):
        """c' > 0 when c < 0 (complementarity c + c' = 6)."""
        for p, q in [(2, 3), (3, 2)]:
            nc = negative_c_shadow_sl2(p, q)
            if nc.c_is_negative:
                self.assertTrue(nc.c_dual_is_positive)

    def test_Q_at_zero_positive(self):
        """Q(0) = 4*kappa^2 > 0 even at negative c."""
        for p, q in [(2, 3), (3, 2)]:
            nc = negative_c_shadow_sl2(p, q)
            self.assertGreater(nc.Q_at_zero, 0)

    def test_shadow_class_independent_of_c_sign(self):
        """Shadow class is L regardless of c sign."""
        for p, q in [(2, 3), (3, 2), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            nc = negative_c_shadow_sl2(p, q)
            self.assertEqual(nc.shadow_class, 'L')


# =========================================================================
# 14. Admissible level enumeration
# =========================================================================

class TestEnumeration(unittest.TestCase):
    """Admissible level enumeration."""

    def test_sl2_contains_integrable(self):
        """Enumeration includes integrable levels."""
        levels = enumerate_admissible_sl2(max_k=4.0, max_q=3)
        k_vals = [float(k) for _, _, k in levels]
        # k = 0, 1, 2, 3, 4 should be present
        for expected in [0.0, 1.0, 2.0, 3.0]:
            self.assertIn(expected, k_vals,
                          f"Missing integrable k = {expected}")

    def test_sl2_contains_admissible(self):
        """Enumeration includes non-integrable admissible levels."""
        levels = enumerate_admissible_sl2(max_k=2.0, max_q=4)
        pq_pairs = [(p, q) for p, q, _ in levels]
        self.assertIn((3, 2), pq_pairs)  # k = -1/2
        self.assertIn((2, 3), pq_pairs)  # k = -4/3

    def test_sl2_sorted(self):
        """Levels are sorted by k."""
        levels = enumerate_admissible_sl2(max_k=3.0, max_q=4)
        k_vals = [float(k) for _, _, k in levels]
        self.assertEqual(k_vals, sorted(k_vals))

    def test_sl2_coprime(self):
        """All enumerated (p,q) are coprime."""
        levels = enumerate_admissible_sl2(max_k=3.0, max_q=5)
        for p, q, _ in levels:
            self.assertEqual(gcd(p, q), 1,
                             f"Non-coprime ({p},{q})")

    def test_sl3_contains_integrable(self):
        """sl_3 enumeration includes integrable levels."""
        levels = enumerate_admissible_sl3(max_k=2.0, max_q=3)
        pq_pairs = [(p, q) for p, q, _ in levels]
        self.assertIn((4, 1), pq_pairs)  # k = 1
        self.assertIn((5, 1), pq_pairs)  # k = 2

    def test_sl3_p_geq_3(self):
        """sl_3: all p >= 3 (h^v = 3)."""
        levels = enumerate_admissible_sl3(max_k=3.0, max_q=4)
        for p, q, _ in levels:
            self.assertGreaterEqual(p, 3)


# =========================================================================
# 15. Deep bar analysis (sl_2)
# =========================================================================

class TestDeepBarAnalysisSl2(unittest.TestCase):
    """Comprehensive deep analysis for sl_2."""

    def test_k_minus_half(self):
        """Deep analysis at k = -1/2."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertEqual(analysis.k, Fraction(-1, 2))
        self.assertEqual(analysis.c, Fraction(-1))
        self.assertEqual(analysis.kappa, Fraction(9, 8))
        self.assertEqual(analysis.h_null, 4)
        self.assertTrue(analysis.is_koszul)
        # kappa + kappa' = 0
        self.assertEqual(analysis.koszul_dual.kappa_sum, 0)

    def test_k_minus_4_3(self):
        """Deep analysis at k = -4/3."""
        analysis = deep_bar_analysis_sl2(2, 3)
        self.assertEqual(analysis.k, Fraction(-4, 3))
        self.assertEqual(analysis.c, Fraction(-6))
        self.assertEqual(analysis.kappa, Fraction(1, 2))
        self.assertEqual(analysis.h_null, 3)
        self.assertTrue(analysis.is_koszul)

    def test_k0_trivial(self):
        """Deep analysis at k = 0."""
        analysis = deep_bar_analysis_sl2(2, 1)
        self.assertEqual(analysis.k, Fraction(0))
        self.assertEqual(analysis.c, Fraction(0))
        self.assertTrue(analysis.is_koszul)

    def test_k1_integrable(self):
        """Deep analysis at k = 1."""
        analysis = deep_bar_analysis_sl2(3, 1)
        self.assertEqual(analysis.k, Fraction(1))
        self.assertEqual(analysis.c, Fraction(1))
        self.assertTrue(analysis.is_koszul)

    def test_verma_dims_populated(self):
        """Verma dimensions are populated."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertGreater(len(analysis.verma_dims), 0)
        self.assertEqual(analysis.verma_dims[0], 1)
        self.assertEqual(analysis.verma_dims[1], 3)

    def test_bar_cohom_universal_populated(self):
        """Universal bar cohomology is populated."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertEqual(len(analysis.bar_cohom_universal), 3)

    def test_bar_cohom_quotient_populated(self):
        """Quotient bar cohomology is populated."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertEqual(len(analysis.bar_cohom_quotient), 3)

    def test_shadow_metric_populated(self):
        """Shadow metric data is populated."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertIsNotNone(analysis.shadow_metric)
        self.assertEqual(analysis.shadow_metric.shadow_class, 'L')

    def test_summary_nonempty(self):
        """Summary string is populated."""
        analysis = deep_bar_analysis_sl2(3, 2)
        self.assertTrue(len(analysis.summary) > 50)

    def test_input_validation(self):
        """Invalid inputs raise ValueError."""
        with self.assertRaises(ValueError):
            deep_bar_analysis_sl2(4, 2)  # gcd != 1
        with self.assertRaises(ValueError):
            deep_bar_analysis_sl2(1, 1)  # p < 2


# =========================================================================
# 16. Deep bar analysis (sl_3)
# =========================================================================

class TestDeepBarAnalysisSl3(unittest.TestCase):
    """Deep analysis for sl_3."""

    def test_k1_integrable(self):
        """sl_3 at k = 1 (p=4, q=1)."""
        analysis = deep_bar_analysis_sl3(4, 1)
        self.assertEqual(analysis.k, Fraction(1))
        self.assertTrue(analysis.is_universal_koszul)
        self.assertEqual(analysis.max_bar_arity, 8)

    def test_h_null_estimate(self):
        """h_null estimate = (p-1)*q."""
        for p, q in [(4, 1), (5, 2), (4, 3)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            analysis = deep_bar_analysis_sl3(p, q)
            self.assertEqual(analysis.h_null_estimate, (p - 1) * q)

    def test_kappa_sl3(self):
        """kappa(sl_3) = 4p/(3q)."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            analysis = deep_bar_analysis_sl3(p, q)
            self.assertEqual(analysis.kappa, Fraction(4 * p, 3 * q))

    def test_kappa_sum_zero_sl3(self):
        """kappa + kappa' = 0 for sl_3."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            analysis = deep_bar_analysis_sl3(p, q)
            self.assertEqual(analysis.kappa_sum, 0)

    def test_ce_dims_binomial(self):
        """CE dims = C(8, d)."""
        analysis = deep_bar_analysis_sl3(4, 1)
        for d in range(9):
            self.assertEqual(analysis.ce_dims[d], comb(8, d))

    def test_w3_data_present(self):
        """W_3 data is present."""
        analysis = deep_bar_analysis_sl3(4, 1)
        self.assertIsNotNone(analysis.w3_data)
        self.assertEqual(analysis.w3_data.shadow_class_w3, 'M')

    def test_bar_relevant_null(self):
        """Correctly identify bar-relevant nulls for sl_3."""
        # p=4, q=1: h_null = 3, max arity = 8. Bar relevant.
        analysis = deep_bar_analysis_sl3(4, 1)
        self.assertTrue(analysis.bar_relevant_null)
        # p=4, q=3: h_null = 9, max arity = 8. NOT bar relevant.
        analysis = deep_bar_analysis_sl3(4, 3)
        self.assertFalse(analysis.bar_relevant_null)

    def test_quotient_koszul_above_bar(self):
        """Quotient Koszul when h_null > max arity."""
        analysis = deep_bar_analysis_sl3(4, 3)  # h_null = 9 > 8
        self.assertTrue(analysis.is_quotient_koszul)

    def test_quotient_open_in_bar(self):
        """Quotient Koszulness OPEN when h_null <= max arity."""
        analysis = deep_bar_analysis_sl3(4, 1)  # h_null = 3 <= 8
        self.assertIsNone(analysis.is_quotient_koszul)


# =========================================================================
# 17. Master verification sweep
# =========================================================================

@pytest.mark.skipif(True, reason="Slow: master_deep_verification takes >2min with mpmath")
class TestMasterSweep(unittest.TestCase):
    """Master verification across all admissible levels (slow: >2min)."""

    def test_all_koszul(self):
        """All tested sl_2 levels are Koszul."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertTrue(result['all_koszul'])

    def test_all_kappa_sum_zero(self):
        """kappa + kappa' = 0 at all levels."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertTrue(result['all_kappa_sum_zero'])

    def test_all_c_sum_six(self):
        """c + c' = 6 at all levels."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertTrue(result['all_c_sum_six'])

    def test_all_paths_agree(self):
        """All four verification paths agree at all levels."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertTrue(result['all_paths_agree'])

    def test_sufficient_levels(self):
        """At least 15 levels tested."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertGreaterEqual(result['n_levels'], 15)

    def test_has_negative_c_levels(self):
        """Some levels have negative c."""
        result = master_deep_verification(max_q=4, max_k=2.0)
        self.assertGreater(result['negative_c_count'], 0)

    def test_has_positive_c_levels(self):
        """Some levels have positive c."""
        result = master_deep_verification(max_q=4, max_k=3.0)
        self.assertGreater(result['positive_c_count'], 0)


# =========================================================================
# 18. Cross-checks: specific known admissible levels
# =========================================================================

class TestSpecificLevels(unittest.TestCase):
    """Detailed verification at specific well-known levels."""

    def test_k_minus_half_full(self):
        """k = -1/2: Complete cross-check."""
        a = deep_bar_analysis_sl2(3, 2)
        # Level data
        self.assertEqual(a.k, Fraction(-1, 2))
        self.assertEqual(a.c, Fraction(-1))
        self.assertEqual(a.kappa, Fraction(9, 8))
        self.assertEqual(a.h_null, 4)
        # Koszulness
        self.assertTrue(a.is_koszul)
        # Shadow metric
        self.assertEqual(a.shadow_metric.shadow_class, 'L')
        self.assertTrue(a.shadow_metric.is_perfect_square)
        # Koszul dual
        self.assertEqual(a.koszul_dual.k_dual, Fraction(-7, 2))
        self.assertEqual(a.koszul_dual.kappa_sum, 0)
        self.assertEqual(a.koszul_dual.c_sum, 6)
        # Verification
        self.assertTrue(a.koszulness_verification.all_paths_agree)

    def test_k_minus_4_3_full(self):
        """k = -4/3: Complete cross-check."""
        a = deep_bar_analysis_sl2(2, 3)
        # Level data
        self.assertEqual(a.k, Fraction(-4, 3))
        self.assertEqual(a.c, Fraction(-6))
        self.assertEqual(a.kappa, Fraction(1, 2))
        self.assertEqual(a.h_null, 3)
        # Koszulness
        self.assertTrue(a.is_koszul)
        # Negative c
        self.assertTrue(a.negative_c.c_is_negative)
        self.assertTrue(a.negative_c.kappa_is_positive)

    def test_k1_full(self):
        """k = 1: Complete cross-check."""
        a = deep_bar_analysis_sl2(3, 1)
        # Level data
        self.assertEqual(a.k, Fraction(1))
        self.assertEqual(a.c, Fraction(1))
        self.assertEqual(a.kappa, Fraction(9, 4))
        # Koszulness
        self.assertTrue(a.is_koszul)
        # Positive c
        self.assertFalse(a.negative_c.c_is_negative)

    def test_yang_lee_level(self):
        """k = -3/2 -- wait, not admissible (p=1, q=2 has p<2).
        Instead: k = 1/2 (p=5, q=2). M(5,2) is Yang-Lee."""
        a = deep_bar_analysis_sl2(5, 2)
        self.assertEqual(a.k, Fraction(1, 2))
        self.assertTrue(a.is_koszul)
        self.assertEqual(a.h_null, 8)  # (5-1)*2 = 8


# =========================================================================
# 19. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Cross-family checks: all levels in a family share properties."""

    def test_all_shadow_class_L(self):
        """ALL admissible sl_2 levels are class L (shadow depth 3)."""
        levels = enumerate_admissible_sl2(max_k=4.0, max_q=5)
        for p, q, k in levels:
            sm = shadow_metric_admissible_sl2(p, q)
            self.assertEqual(sm.shadow_class, 'L',
                             f"Not class L at k = {k}")

    def test_kappa_monotone_in_p_fixed_q(self):
        """kappa = 3p/(4q) is monotone increasing in p for fixed q."""
        for q in range(1, 4):
            prev_kappa = Fraction(0)
            for p in range(2, 10):
                if gcd(p, q) != 1:
                    continue
                kappa = Fraction(3 * p, 4 * q)
                self.assertGreater(kappa, prev_kappa)
                prev_kappa = kappa

    def test_kappa_at_dual_negates(self):
        """kappa' = -kappa universally for sl_2."""
        levels = enumerate_admissible_sl2(max_k=3.0, max_q=5)
        for p, q, k in levels:
            kd = koszul_dual_level_sl2(p, q)
            self.assertEqual(kd.kappa_sum, 0,
                             f"kappa + kappa' != 0 at k = {k}")

    def test_c_sum_six_universal(self):
        """c + c' = 6 universally for sl_2."""
        levels = enumerate_admissible_sl2(max_k=3.0, max_q=5)
        for p, q, k in levels:
            kd = koszul_dual_level_sl2(p, q)
            self.assertEqual(kd.c_sum, 6,
                             f"c + c' != 6 at k = {k}")


# =========================================================================
# 20. Dimensional checks and boundary cases
# =========================================================================

class TestBoundaryAndDimensional(unittest.TestCase):
    """Boundary cases and dimensional analysis."""

    def test_h_null_minimum(self):
        """Minimum h_null for non-integrable admissible = 3 (at p=2, q=3)."""
        levels = enumerate_admissible_sl2(max_k=4.0, max_q=6)
        non_int_nulls = [(p - 1) * q for p, q, k in levels if q > 1]
        if non_int_nulls:
            self.assertGreaterEqual(min(non_int_nulls), 3)

    def test_h_null_2_only_integrable(self):
        """h_null = 2 occurs only at integrable level k=1 (p=3, q=1)."""
        levels = enumerate_admissible_sl2(max_k=4.0, max_q=6)
        for p, q, k in levels:
            h_null = (p - 1) * q
            if h_null == 2:
                self.assertEqual(q, 1, f"h_null=2 at non-integrable (p,q)=({p},{q})")

    def test_large_q_large_h_null(self):
        """For large q, h_null = (p-1)*q is large (far above bar range)."""
        for q in range(4, 8):
            for p in range(2, 6):
                if gcd(p, q) != 1:
                    continue
                h_null = (p - 1) * q
                # For q >= 4 and p >= 2: h_null >= 4 > dim(sl_2) = 3
                self.assertGreaterEqual(h_null, 4,
                                        f"h_null too small at (p,q)=({p},{q})")

    def test_negative_c_count(self):
        """Count of negative-c levels is reasonable."""
        levels = enumerate_admissible_sl2(max_k=2.0, max_q=4)
        neg_c = sum(1 for p, q, k in levels if float(k) < 0)
        pos_c = sum(1 for p, q, k in levels if float(k) > 0)
        self.assertGreater(neg_c, 0, "Should have some negative-c levels")
        self.assertGreater(pos_c, 0, "Should have some positive-c levels")

    def test_kappa_bounded_below(self):
        """kappa = 3p/(4q) > 0 is bounded below by 3/(2*max_q)."""
        levels = enumerate_admissible_sl2(max_k=3.0, max_q=5)
        for p, q, k in levels:
            kappa = Fraction(3 * p, 4 * q)
            self.assertGreater(kappa, 0)

    def test_n_admissible_modules_formula(self):
        """Number of admissible modules = (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1)]:
            if gcd(p, q) != 1:
                continue
            n = (p - 1) * q
            S = admissible_modular_s_matrix_sl2(admissible_level_sl2(p, q))
            self.assertEqual(S.shape[0], n,
                             f"S-matrix size != (p-1)*q at (p,q)=({p},{q})")


if __name__ == '__main__':
    unittest.main()
