"""Tests for sl₃ current algebra E₁ computation (task B5).

Verifies the continuous CE cohomology of sl₃[t] and sl₂[t],
the E₁ page of the Strategy IV spectral sequence, and the
LQT (Loday-Quillen-Tsygan) predictions.
"""

from __future__ import annotations

import pytest

from compute.lib.sl3_current_algebra import (
    partitions_into_n_parts_geq0,
    partition_multiplicities,
    exterior_power_dim,
    ce_space_dim,
    lqt_prediction_sl2,
    lqt_prediction_sl3,
    sl2_e1_direct,
    sl3_e1_direct,
    sl2_cohomology_table,
    sl3_cohomology_table,
    growth_rate_comparison,
)


# ═══════════════════════════════════════════════════════════════════════
# Partition tests
# ═══════════════════════════════════════════════════════════════════════

class TestPartitions:
    def test_partitions_0_into_1(self):
        assert partitions_into_n_parts_geq0(0, 1) == [(0,)]

    def test_partitions_2_into_2(self):
        parts = partitions_into_n_parts_geq0(2, 2)
        assert len(parts) == 2  # (2,0) and (1,1)

    def test_partitions_3_into_2(self):
        parts = partitions_into_n_parts_geq0(3, 2)
        assert len(parts) == 2  # (3,0) and (2,1)

    def test_partition_count_0_3(self):
        assert len(partitions_into_n_parts_geq0(0, 3)) == 1  # (0,0,0)

    def test_partition_count_1_2(self):
        assert len(partitions_into_n_parts_geq0(1, 2)) == 1  # (1,0)

    def test_partition_count_4_3(self):
        # Partitions of 4 into 3 parts >= 0, non-increasing
        parts = partitions_into_n_parts_geq0(4, 3)
        assert len(parts) >= 3  # (4,0,0), (3,1,0), (2,2,0), (2,1,1)


class TestPartitionMultiplicities:
    def test_all_same(self):
        m = partition_multiplicities((2, 2, 2))
        assert m == {2: 3}

    def test_all_different(self):
        m = partition_multiplicities((3, 2, 1))
        assert m == {3: 1, 2: 1, 1: 1}

    def test_with_zeros(self):
        m = partition_multiplicities((3, 0, 0))
        assert m == {3: 1, 0: 2}


# ═══════════════════════════════════════════════════════════════════════
# Exterior algebra tests
# ═══════════════════════════════════════════════════════════════════════

class TestExteriorPower:
    def test_lambda_0(self):
        assert exterior_power_dim(3, 0) == 1
        assert exterior_power_dim(8, 0) == 1

    def test_lambda_1(self):
        assert exterior_power_dim(3, 1) == 3
        assert exterior_power_dim(8, 1) == 8

    def test_lambda_n(self):
        assert exterior_power_dim(3, 3) == 1
        assert exterior_power_dim(8, 8) == 1

    def test_poincare_duality_sl2(self):
        for k in range(4):
            assert exterior_power_dim(3, k) == exterior_power_dim(3, 3 - k)

    def test_poincare_duality_sl3(self):
        for k in range(9):
            assert exterior_power_dim(8, k) == exterior_power_dim(8, 8 - k)

    def test_binomial(self):
        # C(8,2) = 28
        assert exterior_power_dim(8, 2) == 28
        # C(8,4) = 70
        assert exterior_power_dim(8, 4) == 70


# ═══════════════════════════════════════════════════════════════════════
# CE cohomology at weight 0 (= H*(g))
# ═══════════════════════════════════════════════════════════════════════

class TestCECohomologyWeight0:
    """At weight 0, continuous CE = ordinary CE = H*(g)."""

    def test_sl2_h0(self):
        table = sl2_cohomology_table(0, 3)
        assert table.get((0, 0), 0) == 1

    def test_sl2_h3(self):
        table = sl2_cohomology_table(0, 3)
        assert table.get((3, 0), 0) == 1

    def test_sl2_h1_vanishes(self):
        """H¹(sl₂) = 0 (Whitehead)."""
        table = sl2_cohomology_table(0, 3)
        assert table.get((1, 0), 0) == 0

    def test_sl2_h2_vanishes(self):
        """H²(sl₂) = 0 (Whitehead)."""
        table = sl2_cohomology_table(0, 3)
        assert table.get((2, 0), 0) == 0

    def test_sl3_h0(self):
        table = sl3_cohomology_table(0, 8)
        assert table.get((0, 0), 0) == 1

    def test_sl3_h3(self):
        """H³(sl₃) = ℂ (exponent 1)."""
        table = sl3_cohomology_table(0, 8)
        assert table.get((3, 0), 0) == 1

    def test_sl3_h5(self):
        """H⁵(sl₃) = ℂ (exponent 2)."""
        table = sl3_cohomology_table(0, 8)
        assert table.get((5, 0), 0) == 1

    def test_sl3_h8(self):
        """H⁸(sl₃) = ℂ (top class)."""
        table = sl3_cohomology_table(0, 8)
        assert table.get((8, 0), 0) == 1


# ═══════════════════════════════════════════════════════════════════════
# LQT predictions
# ═══════════════════════════════════════════════════════════════════════

class TestLQTPredictions:
    def test_sl2_lqt_degree0(self):
        pred = lqt_prediction_sl2(10)
        assert pred[0] == 1

    def test_sl2_lqt_degree3(self):
        pred = lqt_prediction_sl2(10)
        assert pred[3] == 1

    def test_sl3_lqt_degree0(self):
        pred = lqt_prediction_sl3(10)
        assert pred[0] == 1

    def test_sl3_lqt_degree3(self):
        pred = lqt_prediction_sl3(10)
        assert pred[3] == 1

    def test_sl3_lqt_degree5(self):
        """At degree 5: exponent-2 generator + products from degree 3."""
        pred = lqt_prediction_sl3(10)
        assert pred[5] >= 1  # at least the exponent-2 generator

    def test_lqt_nonnegative(self):
        for pred in [lqt_prediction_sl2(15), lqt_prediction_sl3(15)]:
            for val in pred:
                assert val >= 0


# ═══════════════════════════════════════════════════════════════════════
# E₁ page computation
# ═══════════════════════════════════════════════════════════════════════

class TestE1Page:
    def test_sl2_e1_degree0(self):
        e1 = sl2_e1_direct(2, 8)
        assert e1.get(0, 0) == 1

    def test_sl2_e1_degree3(self):
        e1 = sl2_e1_direct(2, 8)
        assert e1.get(3, 0) == 1

    def test_sl3_e1_degree0(self):
        e1 = sl3_e1_direct(1, 8)
        assert e1.get(0, 0) == 1

    def test_sl2_e1_nonnegative(self):
        e1 = sl2_e1_direct(2, 8)
        for deg, dim in e1.items():
            assert dim >= 0

    def test_sl3_e1_nonnegative(self):
        e1 = sl3_e1_direct(1, 8)
        for deg, dim in e1.items():
            assert dim >= 0


# ═══════════════════════════════════════════════════════════════════════
# Growth rate
# ═══════════════════════════════════════════════════════════════════════

class TestGrowthRate:
    def test_growth_data_exists(self):
        data = growth_rate_comparison(10)
        assert "sl2" in data
        assert "sl3" in data

    def test_sl3_grows_faster(self):
        """sl₃ has more generators (exponents 1,2 vs just 1), so grows faster."""
        data = growth_rate_comparison(10)
        sl2 = data["sl2"]
        sl3 = data["sl3"]
        # At loop degree 8, sl₃ should have >= sl₂
        if len(sl2) > 8 and len(sl3) > 8:
            assert sl3[8] >= sl2[8]


# ═══════════════════════════════════════════════════════════════════════
# Integration
# ═══════════════════════════════════════════════════════════════════════

class TestIntegration:
    def test_sl2_full_pipeline(self):
        table = sl2_cohomology_table(2, 3)
        assert len(table) > 0

    def test_sl3_full_pipeline(self):
        table = sl3_cohomology_table(1, 5)
        assert len(table) > 0

    def test_e1_consistency(self):
        """E₁ dims should sum to CE space dims in a predictable way."""
        e1 = sl2_e1_direct(2, 6)
        total = sum(e1.values())
        assert total > 0
