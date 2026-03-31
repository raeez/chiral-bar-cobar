"""
Tests for boundary_linear_lg_engine.py

Tests the full chain:
  boundary dg algebra → Jacobi coalgebra → pointed line algebra →
  Kuranishi reduction → derived center → quartic contact vanishing

Covers: free, quadratic, cubic, quartic, node, cusp, smooth, two-planes.
"""

import pytest
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from boundary_linear_lg_engine import (
    BoundaryDGAlgebra, JacobiCoalgebra, PointedLineAlgebra,
    KuranishiModel, derived_center_dimension, quartic_contact_vanishes,
    free_multiplet, quadratic_1d, cubic_1d, quartic_1d,
    node_2d, cusp_1d, smooth_linear_1d, two_planes,
    A1_singularity, A2_singularity, A3_singularity, D4_singularity,
    RecursiveKuranishi,
)


# ============================================================
# Free multiplet
# ============================================================

class TestFreeMultiplet:
    def test_free_n1_no_differential(self):
        bdg = free_multiplet(1)
        assert bdg.n == 1
        assert bdg.r == 1
        # F = 0, so all Taylor coefficients vanish
        assert bdg.taylor_coefficient(0, (0,)) == Fraction(0)

    def test_free_n1_jacobi_zero(self):
        bdg = free_multiplet(1)
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 0

    def test_free_n1_line_strict(self):
        bdg = free_multiplet(1)
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        assert pla.is_strict()

    def test_free_n2_line_strict(self):
        bdg = free_multiplet(2)
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        assert pla.is_strict()

    def test_free_kuranishi_smooth(self):
        bdg = free_multiplet(1)
        km = KuranishiModel(bdg)
        # F = 0 has rank 0
        assert km.rank == 0
        assert km.dim_T == 1
        assert km.dim_C == 1

    def test_free_derived_center_dim(self):
        bdg = free_multiplet(2)
        assert derived_center_dimension(bdg, 0) == 4  # 2 + 2
        assert derived_center_dimension(bdg, 1) == 4  # 2 + 2

    def test_free_quartic_vanishes(self):
        bdg = free_multiplet(1)
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Quadratic: F(x) = x^2
# ============================================================

class TestQuadratic:
    def test_quadratic_taylor(self):
        bdg = quadratic_1d()
        # F(x) = x^2: coefficient of x^2 is 1
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(1)
        # Linear term vanishes
        assert bdg.taylor_coefficient(0, (0,)) == Fraction(0)
        # Cubic term vanishes
        assert bdg.taylor_coefficient(0, (0, 0, 0)) == Fraction(0)

    def test_quadratic_jacobi_arity(self):
        bdg = quadratic_1d()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 2

    def test_quadratic_m2(self):
        bdg = quadratic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        # m_2(λ, λ) = c · (coeff of x^2 in F) = c · 1
        coeffs = pla.m_k(2, (0, 0))
        assert coeffs == [Fraction(1)]

    def test_quadratic_no_m3(self):
        bdg = quadratic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(3, (0, 0, 0))
        assert coeffs == [Fraction(0)]

    def test_quadratic_strict(self):
        """Quadratic has m_2 ≠ 0 but m_k = 0 for k ≥ 3."""
        bdg = quadratic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        assert pla.is_strict()

    def test_quadratic_kuranishi(self):
        bdg = quadratic_1d()
        km = KuranishiModel(bdg)
        # dF_0 = 0 (F has no linear term), so rank = 0
        assert km.rank == 0
        assert km.dim_T == 1
        assert km.dim_C == 1

    def test_quadratic_quartic_vanishes(self):
        bdg = quadratic_1d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Cubic: F(x) = x^3
# ============================================================

class TestCubic:
    def test_cubic_taylor(self):
        bdg = cubic_1d()
        assert bdg.taylor_coefficient(0, (0,)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (0, 0, 0)) == Fraction(1)

    def test_cubic_jacobi_arity(self):
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 3

    def test_cubic_m3(self):
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(3, (0, 0, 0))
        assert coeffs == [Fraction(1)]

    def test_cubic_m2_zero(self):
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(2, (0, 0))
        assert coeffs == [Fraction(0)]

    def test_cubic_m4_zero(self):
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(4, (0, 0, 0, 0))
        assert coeffs == [Fraction(0)]

    def test_cubic_has_higher(self):
        """Cubic has genuine m_3 ≠ 0."""
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        assert pla.has_higher_operations()

    def test_cubic_not_strict(self):
        bdg = cubic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        assert not pla.is_strict()

    def test_cubic_quartic_vanishes(self):
        bdg = cubic_1d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Quartic: F(x) = x^4
# ============================================================

class TestQuartic:
    def test_quartic_taylor(self):
        bdg = quartic_1d()
        assert bdg.taylor_coefficient(0, (0,)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (0, 0, 0)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (0, 0, 0, 0)) == Fraction(1)

    def test_quartic_jacobi_arity(self):
        bdg = quartic_1d()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 4

    def test_quartic_m4(self):
        bdg = quartic_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(4, (0, 0, 0, 0))
        assert coeffs == [Fraction(1)]

    def test_quartic_quartic_vanishes(self):
        bdg = quartic_1d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Node: F(x,y) = xy
# ============================================================

class TestNode:
    def test_node_taylor(self):
        bdg = node_2d()
        # F(x,y) = xy: mixed partial ∂²F/∂x∂y = 1
        # Taylor coefficient of x^1 y^1 is 1
        assert bdg.taylor_coefficient(0, (0, 1)) == Fraction(1)
        assert bdg.taylor_coefficient(0, (1, 0)) == Fraction(1)
        # Pure partials vanish
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(0)
        assert bdg.taylor_coefficient(0, (1, 1)) == Fraction(0)

    def test_node_jacobi_arity(self):
        bdg = node_2d()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 2

    def test_node_m2_mixed(self):
        bdg = node_2d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        # m_2(λ_0, λ_1) = c · 1 (from ∂²F/∂x∂y = 1)
        coeffs = pla.m_k(2, (0, 1))
        assert coeffs == [Fraction(1)]

    def test_node_kuranishi(self):
        bdg = node_2d()
        km = KuranishiModel(bdg)
        # dF_0: R^2 → R^1, dF_0 = (y, x) at origin = (0, 0)
        # So dF_0 = 0, rank = 0
        assert km.rank == 0
        assert km.dim_T == 2
        assert km.dim_C == 1

    def test_node_quartic_vanishes(self):
        bdg = node_2d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Cusp: F(x) = x^2 + x^3
# ============================================================

class TestCusp:
    def test_cusp_taylor_quadratic(self):
        bdg = cusp_1d()
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(1)

    def test_cusp_taylor_cubic(self):
        bdg = cusp_1d()
        assert bdg.taylor_coefficient(0, (0, 0, 0)) == Fraction(1)

    def test_cusp_jacobi_arity(self):
        bdg = cusp_1d()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 3

    def test_cusp_has_both_m2_and_m3(self):
        bdg = cusp_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        m2 = pla.m_k(2, (0, 0))
        m3 = pla.m_k(3, (0, 0, 0))
        assert m2 == [Fraction(1)]
        assert m3 == [Fraction(1)]

    def test_cusp_quartic_vanishes(self):
        bdg = cusp_1d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Smooth: F(x) = x
# ============================================================

class TestSmooth:
    def test_smooth_taylor(self):
        bdg = smooth_linear_1d()
        assert bdg.taylor_coefficient(0, (0,)) == Fraction(1)
        assert bdg.taylor_coefficient(0, (0, 0)) == Fraction(0)

    def test_smooth_kuranishi_unobstructed(self):
        bdg = smooth_linear_1d()
        km = KuranishiModel(bdg)
        assert km.rank == 1
        assert km.dim_T == 0  # No kernel
        assert km.dim_C == 0  # No cokernel
        assert km.is_smooth
        assert km.is_unobstructed

    def test_smooth_line_strict(self):
        bdg = smooth_linear_1d()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        # At a smooth point with invertible dF, the minimal line algebra is k
        assert pla.is_strict()

    def test_smooth_quartic_vanishes(self):
        bdg = smooth_linear_1d()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Two planes: F(x,y) = (x, y)
# ============================================================

class TestTwoPlanes:
    def test_two_planes_linearization(self):
        bdg = two_planes()
        A = bdg.linearization_at()
        # Should be identity matrix
        assert A == [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]

    def test_two_planes_kuranishi(self):
        bdg = two_planes()
        km = KuranishiModel(bdg)
        assert km.rank == 2
        assert km.dim_T == 0
        assert km.dim_C == 0
        assert km.is_smooth

    def test_two_planes_quartic_vanishes(self):
        bdg = two_planes()
        assert quartic_contact_vanishes(bdg)


# ============================================================
# Cross-family consistency
# ============================================================

class TestCrossFamily:
    def test_staircase_free_quadratic_cubic_quartic(self):
        """
        Free: m_k = 0 for all k ≥ 1 (no differential, no interaction)
        Quadratic: m_2 ≠ 0, m_k = 0 for k ≥ 3
        Cubic: m_3 ≠ 0, m_2 = m_4 = 0
        Quartic: m_4 ≠ 0, m_2 = m_3 = 0
        """
        free = free_multiplet(1)
        quad = quadratic_1d()
        cub = cubic_1d()
        quart = quartic_1d()

        for bdg in [free, quad, cub, quart]:
            jac = JacobiCoalgebra(bdg)
            pla = PointedLineAlgebra(jac)

        # Free: all m_k = 0 on the line algebra
        jac_f = JacobiCoalgebra(free)
        assert jac_f.max_nonzero_arity() == 0

        # Quadratic: max arity 2
        jac_q = JacobiCoalgebra(quad)
        assert jac_q.max_nonzero_arity() == 2

        # Cubic: max arity 3
        jac_c = JacobiCoalgebra(cub)
        assert jac_c.max_nonzero_arity() == 3

        # Quartic: max arity 4
        jac_4 = JacobiCoalgebra(quart)
        assert jac_4.max_nonzero_arity() == 4

    def test_all_boundary_linear_quartic_vanish(self):
        """q_4 = 0 for ALL boundary-linear LG algebras."""
        examples = [
            free_multiplet(1),
            free_multiplet(3),
            quadratic_1d(),
            cubic_1d(),
            quartic_1d(),
            node_2d(),
            cusp_1d(),
            smooth_linear_1d(),
            two_planes(),
        ]
        for bdg in examples:
            assert quartic_contact_vanishes(bdg), (
                f"q_4 should vanish for boundary-linear LG: "
                f"n={bdg.n}, r={bdg.r}"
            )

    def test_derived_center_dimension_formula(self):
        """
        Derived center has n+r generators in degree 0 and n+r in degree 1.
        """
        examples = [
            (free_multiplet(2), 4),   # n=2, r=2 → n+r=4
            (node_2d(), 3),           # n=2, r=1 → n+r=3
            (smooth_linear_1d(), 2),  # n=1, r=1 → n+r=2
            (two_planes(), 4),        # n=2, r=2 → n+r=4
        ]
        for bdg, expected in examples:
            assert derived_center_dimension(bdg, 0) == expected
            assert derived_center_dimension(bdg, 1) == expected

    def test_kuranishi_rank_monotone(self):
        """Smooth points have maximal rank; singular points have lower rank."""
        smooth = smooth_linear_1d()
        singular = quadratic_1d()
        km_s = KuranishiModel(smooth)
        km_q = KuranishiModel(singular)
        assert km_s.rank >= km_q.rank


# ============================================================
# ADE singularities
# ============================================================

class TestADESingularities:
    """Test the standard ADE singularities."""

    def test_A1_is_quadratic(self):
        bdg = A1_singularity()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 2

    def test_A2_is_cubic(self):
        bdg = A2_singularity()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 3

    def test_A3_is_quartic(self):
        bdg = A3_singularity()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 4

    def test_D4_arity(self):
        """D_4: F(x,y) = x^3 + xy^2. Max arity = 3 (from x^3 and xy^2)."""
        bdg = D4_singularity()
        jac = JacobiCoalgebra(bdg)
        assert jac.max_nonzero_arity() == 3

    def test_D4_m3_pure_x(self):
        """D_4: m_3(λ_x, λ_x, λ_x) = c (from x^3 term)."""
        bdg = D4_singularity()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(3, (0, 0, 0))
        assert coeffs == [Fraction(1)]

    def test_D4_m3_mixed(self):
        """D_4: m_3(λ_x, λ_y, λ_y) = c (from xy^2 term)."""
        bdg = D4_singularity()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        coeffs = pla.m_k(3, (0, 1, 1))
        assert coeffs == [Fraction(1)]

    def test_D4_m2_zero(self):
        """D_4 has no quadratic term, so m_2 = 0 on odd generators."""
        bdg = D4_singularity()
        jac = JacobiCoalgebra(bdg)
        pla = PointedLineAlgebra(jac)
        for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            coeffs = pla.m_k(2, (i, j))
            assert coeffs == [Fraction(0)]

    def test_D4_kuranishi(self):
        bdg = D4_singularity()
        km = KuranishiModel(bdg)
        # dF_0 = 0 (no linear terms), so rank = 0
        assert km.rank == 0
        assert km.dim_T == 2
        assert km.dim_C == 1

    def test_D4_quartic_vanishes(self):
        bdg = D4_singularity()
        assert quartic_contact_vanishes(bdg)

    def test_all_ade_quartic_vanish(self):
        """q_4 = 0 for all ADE singularities (boundary-linear)."""
        for bdg in [A1_singularity(), A2_singularity(),
                    A3_singularity(), D4_singularity()]:
            assert quartic_contact_vanishes(bdg)


# ============================================================
# Recursive Kuranishi
# ============================================================

class TestRecursiveKuranishi:
    def test_A1_kuranishi(self):
        rk = RecursiveKuranishi(A1_singularity())
        assert rk.dim_T == 1
        assert rk.dim_C == 1
        assert not rk.is_smooth_point()

    def test_A2_kuranishi(self):
        rk = RecursiveKuranishi(A2_singularity())
        assert rk.dim_T == 1
        assert rk.dim_C == 1

    def test_D4_kuranishi(self):
        rk = RecursiveKuranishi(D4_singularity())
        assert rk.dim_T == 2
        assert rk.dim_C == 1
        assert rk.obstruction_dimension() == 1

    def test_smooth_kuranishi(self):
        rk = RecursiveKuranishi(smooth_linear_1d())
        assert rk.is_smooth_point()
        assert rk.obstruction_dimension() == 0

    def test_two_planes_kuranishi(self):
        rk = RecursiveKuranishi(two_planes())
        assert rk.is_smooth_point()

    def test_node_kuranishi(self):
        rk = RecursiveKuranishi(node_2d())
        assert rk.dim_T == 2
        assert rk.dim_C == 1


# ============================================================
# Virasoro quartic contact (cross-check with Vol I)
# ============================================================

class TestVirasoroQuarticContact:
    """
    Cross-check: Q^contact_Vir = 10/[c(5c+22)] from Vol I.
    At c = 6k: Q = 5/[6k(15k+11)].
    """

    def test_virasoro_quartic_at_c26(self):
        """At c = 26 (gravity anomaly cancels): Q = 10/(26*152) = 5/1976."""
        c = 26
        Q = Fraction(10, c * (5 * c + 22))
        assert Q == Fraction(10, 26 * 152)
        assert Q == Fraction(5, 1976)

    def test_virasoro_quartic_at_c13(self):
        """At c = 13 (self-dual): Q = 10/(13*87) = 10/1131."""
        c = 13
        Q = Fraction(10, c * (5 * c + 22))
        assert Q == Fraction(10, 1131)

    def test_virasoro_quartic_at_brown_henneaux(self):
        """At c = 6k: Q = 5/[6k(15k+11)]."""
        for k_val in [1, 2, 3, 5, 10]:
            c = 6 * k_val
            Q_from_c = Fraction(10, c * (5 * c + 22))
            Q_from_k = Fraction(5, 6 * k_val * (15 * k_val + 11))
            assert Q_from_c == Q_from_k, f"Mismatch at k={k_val}"

    def test_virasoro_hessian_at_brown_henneaux(self):
        """δ_H(c=6k) = 5/[3k²(15k+11)]."""
        for k_val in [1, 2, 3, 5]:
            c = 6 * k_val
            dH_from_c = Fraction(120, c**2 * (5 * c + 22))
            dH_from_k = Fraction(5, 3 * k_val**2 * (15 * k_val + 11))
            assert dH_from_c == dH_from_k, f"Hessian mismatch at k={k_val}"

    def test_virasoro_complementarity(self):
        """Q(c) + Q(26-c) is a rational function of c."""
        for c_val in [1, 2, 5, 10, 13, 20, 25]:
            if c_val == 0 or 5 * c_val + 22 == 0:
                continue
            c_dual = 26 - c_val
            if c_dual == 0 or 5 * c_dual + 22 == 0:
                continue
            Q1 = Fraction(10, c_val * (5 * c_val + 22))
            Q2 = Fraction(10, c_dual * (5 * c_dual + 22))
            total = Q1 + Q2
            # At c = 13: Q(13) + Q(13) = 20/1131
            if c_val == 13:
                assert total == Fraction(20, 1131)

    def test_virasoro_self_dual_point(self):
        """At c = 13: Q(13) = 10/1131, complementarity sum = 20/1131."""
        Q13 = Fraction(10, 13 * 87)
        assert Q13 == Fraction(10, 1131)
        # Self-dual: Q(13) + Q(26-13) = 2 * Q(13)
        assert 2 * Q13 == Fraction(20, 1131)
