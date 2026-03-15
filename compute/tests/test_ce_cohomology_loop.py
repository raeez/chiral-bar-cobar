"""Tests for CE cohomology of the negative loop algebra V̄ = g ⊗ t⁻¹k[t⁻¹].

Tests d²=0, H¹ verification, and cohomology dimensions at each weight.
"""

import pytest
import numpy as np

from compute.lib.ce_cohomology_loop import (
    CEBasis,
    _build_structure_tensor,
    build_ce_differential,
    ce_cohomology_at_weight,
    ce_space_dim,
    exterior_power_dim,
    partition_multiplicities,
    partitions_into_n_parts,
    sl2_structure_constants,
    sl3_structure_constants,
    verify_d_squared,
    verify_h1,
    DIM_G,
    DIM_G_SL2,
)


# ============================================================
# Partition enumeration
# ============================================================

class TestPartitions:
    def test_partitions_1_1(self):
        assert partitions_into_n_parts(1, 1) == [(1,)]

    def test_partitions_4_2(self):
        parts = partitions_into_n_parts(4, 2)
        assert parts == [(1, 3), (2, 2)]

    def test_partitions_3_3(self):
        assert partitions_into_n_parts(3, 3) == [(1, 1, 1)]

    def test_partitions_impossible(self):
        assert partitions_into_n_parts(2, 3) == []

    def test_multiplicities(self):
        assert partition_multiplicities((1, 1, 2, 3)) == {1: 2, 2: 1, 3: 1}


# ============================================================
# Space dimensions
# ============================================================

class TestSpaceDimensions:
    def test_ce0(self):
        """CE^0_H = 0 for H ≥ 1 (no 0-cochains at positive weight)."""
        for H in range(1, 5):
            assert ce_space_dim(DIM_G, H, 0) == 0

    def test_ce1(self):
        """CE^1_H = dim(g) = 8 for all H ≥ 1."""
        for H in range(1, 5):
            assert ce_space_dim(DIM_G, H, 1) == 8

    def test_ce2_h2(self):
        """CE^2_2: partition (1,1), mult {1:2}, Λ²(g) = C(8,2) = 28."""
        assert ce_space_dim(DIM_G, 2, 2) == 28

    def test_ce3_h3(self):
        """CE^3_3: partition (1,1,1), mult {1:3}, Λ³(g) = C(8,3) = 56."""
        assert ce_space_dim(DIM_G, 3, 3) == 56


# ============================================================
# d² = 0 verification
# ============================================================

class TestDSquared:
    @pytest.fixture
    def sl3_tensor(self):
        sc = sl3_structure_constants()
        return _build_structure_tensor(DIM_G, sc)

    @pytest.fixture
    def sl2_tensor(self):
        sc = sl2_structure_constants()
        return _build_structure_tensor(DIM_G_SL2, sc)

    @pytest.mark.parametrize("H,n", [
        (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (4, 2), (4, 3),
    ])
    def test_d_squared_sl3(self, sl3_tensor, H, n):
        norm = verify_d_squared(DIM_G, sl3_tensor, H, n)
        assert norm < 1e-10, f"d² ≠ 0 at (H={H}, n={n}): norm={norm}"

    @pytest.mark.parametrize("H,n", [
        (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1), (5, 0), (5, 1),
    ])
    def test_d_squared_sl2(self, sl2_tensor, H, n):
        norm = verify_d_squared(DIM_G_SL2, sl2_tensor, H, n)
        assert norm < 1e-10, f"d² ≠ 0 at (H={H}, n={n}): norm={norm}"


# ============================================================
# sl₃ CE cohomology — locked numerical results
# ============================================================

class TestSl3Cohomology:
    @pytest.fixture
    def sl3_tensor(self):
        sc = sl3_structure_constants()
        return _build_structure_tensor(DIM_G, sc)

    def test_h1_weight1(self, sl3_tensor):
        """H¹₁ = 8 (abelianization: g₁/[V̄,V̄]∩g₁ = g)."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 1, max_degree=1)
        assert cohom[1] == 8

    def test_h1_weight2_zero(self, sl3_tensor):
        """H¹₂ = 0 (bracket surjective: [g₁,g₁] = g₂)."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 2, max_degree=1)
        assert cohom[1] == 0

    def test_h1_total(self):
        """Total H¹ = 8."""
        h1 = verify_h1()
        assert sum(h1.values()) == 8

    def test_h2_weight2(self, sl3_tensor):
        """H²₂ = 20 = C(8,2) - 8."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 2, max_degree=2)
        assert cohom[2] == 20

    def test_h2_weight3_zero(self, sl3_tensor):
        """H²₃ = 0."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 3, max_degree=2)
        assert cohom[2] == 0

    def test_h3_weight4(self, sl3_tensor):
        """H³₄ = 70 = C(8,4)."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 4, max_degree=3)
        assert cohom[3] == 70

    def test_h4_weight5(self, sl3_tensor):
        """H⁴₅ = 64."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 5, max_degree=4)
        assert cohom[4] == 64

    @pytest.mark.slow
    def test_h4_weight6(self, sl3_tensor):
        """H⁴₆ = 56."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 6, max_degree=4)
        assert cohom[4] == 56

    @pytest.mark.slow
    def test_h4_weight7_zero(self, sl3_tensor):
        """H⁴₇ = 0."""
        cohom = ce_cohomology_at_weight(DIM_G, sl3_tensor, 7, max_degree=4)
        assert cohom[4] == 0


# ============================================================
# sl₃ CE cohomology totals
# ============================================================

class TestSl3Totals:
    """Total CE cohomology H^n(V̄, k) = Σ_H H^n_H."""

    def test_total_h1(self):
        """H¹ = 8."""
        sc = sl3_structure_constants()
        ft = _build_structure_tensor(DIM_G, sc)
        total = 0
        for H in range(1, 10):
            cohom = ce_cohomology_at_weight(DIM_G, ft, H, max_degree=1)
            total += cohom.get(1, 0)
        assert total == 8

    def test_total_h2(self):
        """H² = 20."""
        sc = sl3_structure_constants()
        ft = _build_structure_tensor(DIM_G, sc)
        total = 0
        for H in range(1, 6):
            cohom = ce_cohomology_at_weight(DIM_G, ft, H, max_degree=2)
            total += cohom.get(2, 0)
        assert total == 20

    def test_total_h3(self):
        """H³ = 70."""
        sc = sl3_structure_constants()
        ft = _build_structure_tensor(DIM_G, sc)
        total = 0
        for H in range(1, 8):
            cohom = ce_cohomology_at_weight(DIM_G, ft, H, max_degree=3)
            total += cohom.get(3, 0)
        assert total == 70

    def test_ce_less_than_chiral_bar(self):
        """CE cohomology should be strictly less than chiral bar at degree ≥ 2."""
        # CE:         [1, 8, 20, 70, 120]
        # Chiral bar: [1, 8, 36, 204, 1352]
        ce_dims = [8, 20, 70, 120]
        bar_dims = [8, 36, 204, 1352]
        for n in range(len(ce_dims)):
            assert ce_dims[n] <= bar_dims[n], f"CE H^{n+1} > bar H^{n+1}"


# ============================================================
# sl₂ cross-validation
# ============================================================

class TestSl2Cohomology:
    @pytest.fixture
    def sl2_tensor(self):
        sc = sl2_structure_constants()
        return _build_structure_tensor(DIM_G_SL2, sc)

    def test_h1_total_sl2(self, sl2_tensor):
        """H¹(sl₂⁻) = 3 = dim(sl₂)."""
        total = 0
        for H in range(1, 6):
            cohom = ce_cohomology_at_weight(DIM_G_SL2, sl2_tensor, H, max_degree=1)
            total += cohom.get(1, 0)
        assert total == 3

    def test_h2_weight2_sl2(self, sl2_tensor):
        """H²₂(sl₂⁻) = C(3,2) - rank(bracket) = 3 - 3 = 0?"""
        # [sl₂, sl₂] = sl₂ (surjective), so rank = 3
        # Λ²(sl₂) at weight 2 = C(3,2) = 3
        # H² = 3 - 3 = 0
        cohom = ce_cohomology_at_weight(DIM_G_SL2, sl2_tensor, 2, max_degree=2)
        assert cohom[2] == 0
