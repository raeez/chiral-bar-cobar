"""Tests for cyclic CE cohomology computation (MC2 Step 1).

Marked slow — heavy symbolic matrix computations.  Run via ``make test-full``.

Verifies:
  - CE cohomology H*(sl_2, sl_2) = 0 (Whitehead lemmas)
  - Cyclic subcomplex dimensions C^n_cyc
  - Cyclic CE cohomology H^2_cyc(sl_2, sl_2) = C (Killing 3-cocycle)
  - d^2 = 0 for all differentials
  - Killing form ad-invariance
  - sl_3 extension: H^2_cyc(sl_3, sl_3) = C (universality)
  - Exterior algebra cross-check
"""

import pytest
import unittest
from fractions import Fraction

pytestmark = pytest.mark.slow

import numpy as np

from compute.lib.mc2_cyclic_ce import (
    _exact_rank,
    ce_cohomology,
    ce_differential_0,
    ce_differential_1,
    ce_differential_2,
    ce_exterior_differential,
    cyclic_ce_cohomology,
    cyclic_ce_via_exterior,
    g2_killing_form,
    g2_structure_constants,
    sl2_killing_form,
    sl2_structure_constants,
    sl3_killing_form,
    sl3_structure_constants,
    sp4_killing_form,
    sp4_structure_constants,
    verify_sl2_ce_cohomology,
    verify_sl2_cyclic_ce_cohomology,
    verify_sl2_exterior_cross_check,
    verify_sl3_ce_cohomology,
    verify_sl3_cyclic_ce_cohomology,
    verify_g2_cyclic_ce_cohomology,
    verify_sp4_ce_cohomology,
    verify_sp4_cyclic_ce_cohomology,
)


class TestSl2StructureData(unittest.TestCase):
    """Verify sl_2 Lie algebra data."""

    def test_antisymmetry(self):
        c = sl2_structure_constants()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.assertEqual(c[i, j, k], -c[j, i, k])

    def test_jacobi(self):
        c = sl2_structure_constants()
        for a in range(3):
            for b in range(3):
                for d in range(3):
                    for m in range(3):
                        val = sum(
                            c[a, b, k] * c[k, d, m]
                            + c[b, d, k] * c[k, a, m]
                            + c[d, a, k] * c[k, b, m]
                            for k in range(3)
                        )
                        self.assertEqual(val, 0)

    def test_killing_symmetry(self):
        kap = sl2_killing_form()
        for i in range(3):
            for j in range(3):
                self.assertEqual(kap[i, j], kap[j, i])

    def test_killing_nondegenerate(self):
        kap = sl2_killing_form()
        det = (
            kap[0, 0] * (kap[1, 1] * kap[2, 2] - kap[1, 2] * kap[2, 1])
            - kap[0, 1] * (kap[1, 0] * kap[2, 2] - kap[1, 2] * kap[2, 0])
            + kap[0, 2] * (kap[1, 0] * kap[2, 1] - kap[1, 1] * kap[2, 0])
        )
        self.assertNotEqual(det, 0)

    def test_killing_ad_invariant(self):
        c = sl2_structure_constants()
        kap = sl2_killing_form()
        for a in range(3):
            for b in range(3):
                for d in range(3):
                    lhs = sum(c[a, b, k] * kap[k, d] for k in range(3))
                    rhs = sum(c[a, d, k] * kap[b, k] for k in range(3))
                    self.assertEqual(lhs + rhs, 0)


class TestCEComplex(unittest.TestCase):
    """Verify the CE complex d^2 = 0 and cohomology."""

    def setUp(self):
        self.c = sl2_structure_constants()
        self.d0 = ce_differential_0(self.c, 3)
        self.d1 = ce_differential_1(self.c, 3)
        self.d2 = ce_differential_2(self.c, 3)

    def test_d0_rank(self):
        self.assertEqual(_exact_rank(self.d0), 3)

    def test_d1_d0_zero(self):
        prod = np.zeros((9, 3), dtype=object)
        for i in range(9):
            for j in range(3):
                prod[i, j] = sum(
                    self.d1[i, k] * self.d0[k, j] for k in range(9)
                )
        for i in range(9):
            for j in range(3):
                self.assertEqual(prod[i, j], 0)

    def test_d2_d1_zero(self):
        prod = np.zeros((3, 9), dtype=object)
        for i in range(3):
            for j in range(9):
                prod[i, j] = sum(
                    self.d2[i, k] * self.d1[k, j] for k in range(9)
                )
        for i in range(3):
            for j in range(9):
                self.assertEqual(prod[i, j], 0)

    def test_ce_cohomology_vanishes(self):
        result = ce_cohomology(self.c, 3)
        for n in range(4):
            self.assertEqual(result[n], 0, f"H^{n}(sl_2, sl_2) != 0")


class TestCyclicCECohomology(unittest.TestCase):
    """Verify cyclic CE cohomology of sl_2."""

    def setUp(self):
        self.c = sl2_structure_constants()
        self.kap = sl2_killing_form()
        self.result = cyclic_ce_cohomology(self.c, self.kap, 3)

    def test_subcomplex_dimensions(self):
        sub = self.result["subcomplex_dims"]
        self.assertEqual(sub[0], 3)
        self.assertEqual(sub[1], 3)
        self.assertEqual(sub[2], 1)
        self.assertEqual(sub[3], 0)

    def test_cyclic_cohomology(self):
        dims = self.result["dims"]
        self.assertEqual(dims[0], 0)
        self.assertEqual(dims[1], 0)
        self.assertEqual(dims[2], 1)
        self.assertEqual(dims[3], 0)

    def test_killing_3form_nonzero(self):
        self.assertNotEqual(self.result["killing_3form_value"], 0)

    def test_killing_3form_value(self):
        # phi(e, h, f) = kap([e,h], f) = kap(-2e, f) = -2*kap(e,f) = -2
        self.assertEqual(self.result["killing_3form_value"], Fraction(-2))

    def test_killing_3form_total_antisymmetry(self):
        c = self.c
        kap = self.kap
        for a in range(3):
            for b in range(3):
                for d in range(3):
                    v = sum(c[a, b, k] * kap[k, d] for k in range(3))
                    v_swap12 = sum(c[b, a, k] * kap[k, d] for k in range(3))
                    v_swap23 = sum(c[a, d, k] * kap[k, b] for k in range(3))
                    self.assertEqual(v, -v_swap12)
                    self.assertEqual(v, -v_swap23)


class TestVerificationBundles(unittest.TestCase):
    """Verify bundled self-check functions."""

    def test_ce_bundle(self):
        result = verify_sl2_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"CE check failed: {key}")

    def test_cyclic_ce_bundle(self):
        result = verify_sl2_cyclic_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"Cyclic CE check failed: {key}")


# ---------- sl_3 tests ----------


class TestSl3StructureData(unittest.TestCase):
    """Verify sl_3 Lie algebra data."""

    def setUp(self):
        self.c = sl3_structure_constants()
        self.kap = sl3_killing_form()
        self.dim = 8

    def test_antisymmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    self.assertEqual(
                        self.c[i, j, k], -self.c[j, i, k],
                        f"c[{i},{j},{k}] != -c[{j},{i},{k}]"
                    )

    def test_jacobi(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    for m in range(self.dim):
                        val = sum(
                            self.c[a, b, k] * self.c[k, d, m]
                            + self.c[b, d, k] * self.c[k, a, m]
                            + self.c[d, a, k] * self.c[k, b, m]
                            for k in range(self.dim)
                        )
                        self.assertEqual(
                            val, 0,
                            f"Jacobi fails at ({a},{b},{d},{m})"
                        )

    def test_killing_symmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.assertEqual(self.kap[i, j], self.kap[j, i])

    def test_killing_nondegenerate(self):
        """Check nondegeneracy via rank."""
        self.assertEqual(_exact_rank(self.kap), self.dim)

    def test_killing_ad_invariant(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    lhs = sum(
                        self.c[a, b, k] * self.kap[k, d]
                        for k in range(self.dim)
                    )
                    rhs = sum(
                        self.c[a, d, k] * self.kap[b, k]
                        for k in range(self.dim)
                    )
                    self.assertEqual(
                        lhs + rhs, 0,
                        f"Ad-invariance fails at ({a},{b},{d})"
                    )

    def test_specific_brackets(self):
        """Spot-check specific brackets against matrix computation."""
        c = self.c
        # [e1, e2] = e12
        self.assertEqual(c[0, 1, 2], Fraction(1))
        # [e12, f12] = h1 + h2
        self.assertEqual(c[2, 7, 3], Fraction(1))
        self.assertEqual(c[2, 7, 4], Fraction(1))
        # [h1, e1] = 2e1
        self.assertEqual(c[3, 0, 0], Fraction(2))
        # [e1, f12] = -f2
        self.assertEqual(c[0, 7, 6], Fraction(-1))
        # [f1, f2] = -f12
        self.assertEqual(c[5, 6, 7], Fraction(-1))

    def test_killing_specific_values(self):
        """Spot-check Killing form values."""
        kap = self.kap
        self.assertEqual(kap[0, 5], Fraction(1))  # (e1, f1) = 1
        self.assertEqual(kap[3, 3], Fraction(2))   # (h1, h1) = 2
        self.assertEqual(kap[3, 4], Fraction(-1))  # (h1, h2) = -1
        self.assertEqual(kap[0, 0], Fraction(0))   # (e1, e1) = 0


class TestSl3CECohomology(unittest.TestCase):
    """Verify CE cohomology H*(sl_3, sl_3) = 0 (Whitehead)."""

    def setUp(self):
        self.c = sl3_structure_constants()

    def test_d0_rank(self):
        """d0 is injective: rank = dim(sl_3) = 8."""
        d0 = ce_differential_0(self.c, 8)
        self.assertEqual(_exact_rank(d0), 8)

    def test_ce_h0_h1_h2_vanish(self):
        """H^0 = H^1 = H^2 = 0 by Whitehead."""
        result = ce_cohomology(self.c, 8)
        self.assertEqual(result[0], 0, "H^0(sl_3, sl_3) != 0")
        self.assertEqual(result[1], 0, "H^1(sl_3, sl_3) != 0")
        self.assertEqual(result[2], 0, "H^2(sl_3, sl_3) != 0")

    def test_ce_h3_vanishes(self):
        """H^3 also vanishes for the adjoint module of semisimple sl_3."""
        result = ce_cohomology(self.c, 8)
        self.assertEqual(result[3], 0, "H^3(sl_3, sl_3) != 0")

    def test_d1_rank(self):
        """rank(d1) = 56 (from Whitehead: dim C^1 - rank d0 - H^1 = 64 - 8 - 0)."""
        d1 = ce_differential_1(self.c, 8)
        self.assertEqual(_exact_rank(d1), 56)


class TestSl3CyclicCECohomology(unittest.TestCase):
    """Verify cyclic CE cohomology of sl_3 via exterior algebra.

    Key result: H^2_cyc(sl_3, sl_3) = C, confirming universality
    of the Killing 3-cocycle as unique cyclic deformation for all
    simple Lie algebras.
    """

    def setUp(self):
        self.c = sl3_structure_constants()
        self.kap = sl3_killing_form()
        self.result = cyclic_ce_via_exterior(self.c, 8)
        self.public_result = cyclic_ce_cohomology(self.c, self.kap, 8)

    def test_subcomplex_dimensions(self):
        """C^n_cyc = Lambda^{n+1}: dims C(8,1), C(8,2), C(8,3), C(8,4)."""
        sub = self.result["subcomplex_dims"]
        self.assertEqual(sub[0], 8)
        self.assertEqual(sub[1], 28)
        self.assertEqual(sub[2], 56)
        self.assertEqual(sub[3], 70)

    def test_h2_cyc_is_one(self):
        """H^2_cyc(sl_3, sl_3) = C (Killing 3-cocycle)."""
        self.assertEqual(self.result["dims"][2], 1)

    def test_other_cohomology_vanishes(self):
        """H^n_cyc = 0 for n != 2."""
        dims = self.result["dims"]
        self.assertEqual(dims[0], 0, "H^0_cyc != 0")
        self.assertEqual(dims[1], 0, "H^1_cyc != 0")
        self.assertEqual(dims[3], 0, "H^3_cyc != 0")

    def test_public_cyclic_routine_matches_exterior(self):
        """The public cyclic routine must agree with the exterior model."""
        self.assertEqual(self.public_result["dims"], self.result["dims"])
        self.assertEqual(
            self.public_result["subcomplex_dims"],
            self.result["subcomplex_dims"],
        )

    def test_exterior_ranks(self):
        """Verify CE exterior differential ranks.

        From Poincare polynomial (1+t^3)(1+t^5) of sl_3:
        rank d^1 = 8, rank d^2 = 20, rank d^3 = 35.
        """
        ranks = self.result["exterior_ranks"]
        self.assertEqual(ranks[1], 8)
        self.assertEqual(ranks[2], 20)
        self.assertEqual(ranks[3], 35)

    def test_killing_3form_nonzero_sl3(self):
        """The Killing 3-form phi(a,b,c) = kap([a,b],c) is nonzero on sl_3."""
        c = self.c
        kap = sl3_killing_form()
        # phi(e1, e2, f12) = kap([e1,e2], f12) = kap(e12, f12) = 1
        val = sum(c[0, 1, k] * kap[k, 7] for k in range(8))
        self.assertEqual(val, Fraction(1))

    def test_killing_3form_total_antisymmetry_sl3(self):
        """The lowered structure constants c_{ijk} = c^m_{ij} kap_{mk}
        are totally antisymmetric for sl_3."""
        c = self.c
        kap = sl3_killing_form()
        for a in range(8):
            for b in range(8):
                for d in range(8):
                    v = sum(c[a, b, k] * kap[k, d] for k in range(8))
                    v_swap12 = sum(c[b, a, k] * kap[k, d] for k in range(8))
                    v_swap23 = sum(c[a, d, k] * kap[k, b] for k in range(8))
                    self.assertEqual(v, -v_swap12)
                    self.assertEqual(v, -v_swap23)


class TestExteriorCEDifferential(unittest.TestCase):
    """Verify exterior algebra CE differential properties."""

    def test_d_squared_zero_sl2(self):
        """d^2 o d^1 = 0 on Lambda*(sl_2*)."""
        c = sl2_structure_constants()
        d1 = ce_exterior_differential(c, 3, 1)
        d2 = ce_exterior_differential(c, 3, 2)
        prod = np.zeros((1, 3), dtype=object)
        for i in range(1):
            for j in range(3):
                prod[i, j] = sum(
                    d2[i, k] * d1[k, j] for k in range(3)
                )
                self.assertEqual(prod[i, j], 0)

    def test_d_squared_zero_sl3_d2d1(self):
        """d^2 o d^1 = 0 on Lambda*(sl_3*)."""
        c = sl3_structure_constants()
        d1 = ce_exterior_differential(c, 8, 1)  # 28 x 8
        d2 = ce_exterior_differential(c, 8, 2)  # 56 x 28
        for i in range(56):
            for j in range(8):
                val = sum(
                    d2[i, k] * d1[k, j] for k in range(28)
                    if d2[i, k] != 0 and d1[k, j] != 0
                )
                self.assertEqual(val, 0, f"d2 o d1 nonzero at ({i},{j})")

    def test_d_squared_zero_sl3_d3d2(self):
        """d^3 o d^2 = 0 on Lambda*(sl_3*)."""
        c = sl3_structure_constants()
        d2 = ce_exterior_differential(c, 8, 2)  # 56 x 28
        d3 = ce_exterior_differential(c, 8, 3)  # 70 x 56
        for i in range(70):
            for j in range(28):
                val = sum(
                    d3[i, k] * d2[k, j] for k in range(56)
                    if d3[i, k] != 0 and d2[k, j] != 0
                )
                self.assertEqual(val, 0, f"d3 o d2 nonzero at ({i},{j})")

    def test_exterior_cross_check_sl2(self):
        """Exterior and Hom approaches agree for sl_2."""
        result = verify_sl2_exterior_cross_check()
        for key, val in result.items():
            self.assertTrue(val, f"Cross-check failed: {key}")


class TestSl3VerificationBundles(unittest.TestCase):
    """Verify sl_3 bundled self-check functions."""

    def test_sl3_ce_bundle(self):
        result = verify_sl3_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"sl_3 CE check failed: {key}")

    def test_sl3_cyclic_ce_bundle(self):
        result = verify_sl3_cyclic_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"sl_3 cyclic CE check failed: {key}")


# ---------- sp_4 tests (non-simply-laced) ----------


class TestSp4StructureData(unittest.TestCase):
    """Verify sp_4 Lie algebra data."""

    def setUp(self):
        self.c = sp4_structure_constants()
        self.kap = sp4_killing_form()
        self.dim = 10

    def test_antisymmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    self.assertEqual(
                        self.c[i, j, k], -self.c[j, i, k],
                        f"c[{i},{j},{k}] != -c[{j},{i},{k}]"
                    )

    def test_jacobi(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    for m in range(self.dim):
                        val = sum(
                            self.c[a, b, k] * self.c[k, d, m]
                            + self.c[b, d, k] * self.c[k, a, m]
                            + self.c[d, a, k] * self.c[k, b, m]
                            for k in range(self.dim)
                        )
                        self.assertEqual(
                            val, 0,
                            f"Jacobi fails at ({a},{b},{d},{m})"
                        )

    def test_killing_symmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.assertEqual(self.kap[i, j], self.kap[j, i])

    def test_killing_nondegenerate(self):
        self.assertEqual(_exact_rank(self.kap), self.dim)

    def test_killing_ad_invariant(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    lhs = sum(
                        self.c[a, b, k] * self.kap[k, d]
                        for k in range(self.dim)
                    )
                    rhs = sum(
                        self.c[a, d, k] * self.kap[b, k]
                        for k in range(self.dim)
                    )
                    self.assertEqual(
                        lhs + rhs, 0,
                        f"Ad-invariance fails at ({a},{b},{d})"
                    )

    def test_specific_brackets(self):
        """Spot-check specific brackets against matrix computation."""
        c = self.c
        # [e1, e2] = e12
        self.assertEqual(c[0, 1, 2], Fraction(1))
        # [e1, e12] = 2*e22
        self.assertEqual(c[0, 2, 3], Fraction(2))
        # [e12, f12] = h1 + 2*h2
        self.assertEqual(c[2, 8, 4], Fraction(1))
        self.assertEqual(c[2, 8, 5], Fraction(2))
        # [h1, e1] = 2e1
        self.assertEqual(c[4, 0, 0], Fraction(2))
        # [h1, e2] = -2e2 (non-simply-laced: NOT -e2)
        self.assertEqual(c[4, 1, 1], Fraction(-2))
        # [f1, f2] = -f12
        self.assertEqual(c[6, 7, 8], Fraction(-1))
        # [f1, f12] = -2*f22
        self.assertEqual(c[6, 8, 9], Fraction(-2))

    def test_killing_specific_values(self):
        """Spot-check Killing form: short roots pair to 2, long to 1."""
        kap = self.kap
        # Short roots: (e1,f1) = (e12,f12) = 2
        self.assertEqual(kap[0, 6], Fraction(2))
        self.assertEqual(kap[2, 8], Fraction(2))
        # Long roots: (e2,f2) = (e22,f22) = 1
        self.assertEqual(kap[1, 7], Fraction(1))
        self.assertEqual(kap[3, 9], Fraction(1))
        # Cartan
        self.assertEqual(kap[4, 4], Fraction(4))
        self.assertEqual(kap[4, 5], Fraction(-2))
        self.assertEqual(kap[5, 5], Fraction(2))

    def test_killing_3form_total_antisymmetry(self):
        """The lowered structure constants are totally antisymmetric for sp_4."""
        c = self.c
        kap = self.kap
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    v = sum(c[a, b, k] * kap[k, d] for k in range(self.dim))
                    v_swap12 = sum(c[b, a, k] * kap[k, d] for k in range(self.dim))
                    v_swap23 = sum(c[a, d, k] * kap[k, b] for k in range(self.dim))
                    self.assertEqual(v, -v_swap12)
                    self.assertEqual(v, -v_swap23)


class TestSp4CECohomology(unittest.TestCase):
    """Verify CE cohomology H*(sp_4, sp_4) = 0 (Whitehead)."""

    def setUp(self):
        self.c = sp4_structure_constants()

    def test_d0_rank(self):
        d0 = ce_differential_0(self.c, 10)
        self.assertEqual(_exact_rank(d0), 10)

    def test_ce_h0_h1_h2_vanish(self):
        result = ce_cohomology(self.c, 10)
        self.assertEqual(result[0], 0, "H^0(sp_4, sp_4) != 0")
        self.assertEqual(result[1], 0, "H^1(sp_4, sp_4) != 0")
        self.assertEqual(result[2], 0, "H^2(sp_4, sp_4) != 0")


class TestSp4CyclicCECohomology(unittest.TestCase):
    """Verify cyclic CE cohomology of sp_4 via exterior algebra.

    Key result: H^2_cyc(sp_4, sp_4) = C, confirming universality
    of the Killing 3-cocycle for the first non-simply-laced algebra.
    """

    def setUp(self):
        self.c = sp4_structure_constants()
        self.kap = sp4_killing_form()
        self.result = cyclic_ce_via_exterior(self.c, 10)
        self.public_result = cyclic_ce_cohomology(self.c, self.kap, 10)

    def test_h2_cyc_is_one(self):
        """H^2_cyc(sp_4, sp_4) = C (Killing 3-cocycle)."""
        self.assertEqual(self.result["dims"][2], 1)

    def test_other_cohomology_vanishes(self):
        dims = self.result["dims"]
        self.assertEqual(dims[0], 0, "H^0_cyc != 0")
        self.assertEqual(dims[1], 0, "H^1_cyc != 0")
        self.assertEqual(dims[3], 0, "H^3_cyc != 0")

    def test_public_cyclic_routine_matches_exterior(self):
        self.assertEqual(self.public_result["dims"], self.result["dims"])

    def test_killing_3form_nonzero_sp4(self):
        """phi(e1, e2, f12) = kap([e1,e2], f12) = kap(e12, f12) = 2."""
        c = self.c
        kap = self.kap
        val = sum(c[0, 1, k] * kap[k, 8] for k in range(10))
        self.assertEqual(val, Fraction(2))


class TestSp4VerificationBundles(unittest.TestCase):
    """Verify sp_4 bundled self-check functions."""

    def test_sp4_ce_bundle(self):
        result = verify_sp4_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"sp_4 CE check failed: {key}")

    def test_sp4_cyclic_ce_bundle(self):
        result = verify_sp4_cyclic_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"sp_4 cyclic CE check failed: {key}")


class TestG2StructureData(unittest.TestCase):
    """Verify G_2 Lie algebra data."""

    @classmethod
    def setUpClass(cls):
        cls.c = g2_structure_constants()
        cls.kap = g2_killing_form()
        cls.dim = 14

    def test_antisymmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    self.assertEqual(self.c[i, j, k], -self.c[j, i, k])

    def test_jacobi(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    for m in range(self.dim):
                        val = sum(
                            self.c[a, b, k] * self.c[k, d, m]
                            + self.c[b, d, k] * self.c[k, a, m]
                            + self.c[d, a, k] * self.c[k, b, m]
                            for k in range(self.dim)
                        )
                        self.assertEqual(val, 0, f"Jacobi fails at ({a},{b},{d},{m})")

    def test_killing_symmetry(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.assertEqual(self.kap[i, j], self.kap[j, i])

    def test_killing_nondegenerate(self):
        self.assertEqual(_exact_rank(self.kap), self.dim)

    def test_killing_ad_invariant(self):
        for a in range(self.dim):
            for b in range(self.dim):
                for d in range(self.dim):
                    lhs = sum(self.c[a, b, k] * self.kap[k, d] for k in range(self.dim))
                    rhs = sum(self.c[a, d, k] * self.kap[b, k] for k in range(self.dim))
                    self.assertEqual(lhs + rhs, 0, f"Ad-invariance fails at ({a},{b},{d})")

    def test_specific_brackets(self):
        c = self.c
        self.assertEqual(c[0, 1, 2], Fraction(1))
        self.assertEqual(c[0, 2, 3], Fraction(2))
        self.assertEqual(c[0, 3, 4], Fraction(3))
        self.assertEqual(c[1, 4, 5], Fraction(1))
        self.assertEqual(c[2, 11, 8], Fraction(2))
        self.assertEqual(c[2, 3, 5], Fraction(-3))

    def test_killing_specific_values(self):
        kap = self.kap
        self.assertEqual(kap[0, 8], Fraction(3))
        self.assertEqual(kap[1, 9], Fraction(1))
        self.assertEqual(kap[2, 10], Fraction(3))
        self.assertEqual(kap[3, 11], Fraction(3))
        self.assertEqual(kap[4, 12], Fraction(1))
        self.assertEqual(kap[5, 13], Fraction(1))
        self.assertEqual(kap[6, 6], Fraction(6))
        self.assertEqual(kap[6, 7], Fraction(-3))
        self.assertEqual(kap[7, 7], Fraction(2))


class TestG2CyclicCECohomology(unittest.TestCase):
    """Verify cyclic CE cohomology of G_2 via the exterior algebra."""

    @classmethod
    def setUpClass(cls):
        cls.c = g2_structure_constants()
        cls.kap = g2_killing_form()
        cls.result = cyclic_ce_via_exterior(cls.c, 14)
        cls.public_result = cyclic_ce_cohomology(cls.c, cls.kap, 14)

    def test_h2_cyc_is_one(self):
        self.assertEqual(self.result["dims"][2], 1)

    def test_other_cohomology_vanishes(self):
        dims = self.result["dims"]
        self.assertEqual(dims[0], 0, "H^0_cyc != 0")
        self.assertEqual(dims[1], 0, "H^1_cyc != 0")
        self.assertEqual(dims[3], 0, "H^3_cyc != 0")

    def test_public_cyclic_routine_matches_exterior(self):
        self.assertEqual(self.public_result["dims"], self.result["dims"])
        self.assertEqual(self.public_result["exterior_ranks"], self.result["exterior_ranks"])

    def test_killing_3form_nonzero_g2(self):
        val = sum(self.c[0, 1, k] * self.kap[k, 10] for k in range(14))
        self.assertEqual(val, Fraction(3))


class TestG2VerificationBundles(unittest.TestCase):
    """Verify G_2 bundled self-check functions."""

    def test_g2_cyclic_ce_bundle(self):
        result = verify_g2_cyclic_ce_cohomology()
        for key, val in result.items():
            self.assertTrue(val, f"G_2 cyclic CE check failed: {key}")


if __name__ == "__main__":
    unittest.main()
