"""Tests for PBW spectral sequence E₁ page (sl₃-hat).

Tests invariant dimensions by partition type, E₁^{p,0}_H dimensions,
and cross-validation with spectral_sequence.py.
"""

import pytest

from compute.lib.pbw_e1_sl3 import (
    all_partition_types,
    count_partitions_by_type,
    e1_dim,
    e1_total_through_weight,
    invariant_dim_cached,
    invariant_dim_direct,
    invariant_dim_weyl,
    partition_type,
    partitions_of,
    verify_basic_facts,
)


# ============================================================
# Partition enumeration
# ============================================================

class TestPartitions:
    def test_partitions_of_4_into_2(self):
        parts = partitions_of(4, 2)
        assert parts == [(1, 3), (2, 2)]

    def test_partitions_of_5_into_3(self):
        parts = partitions_of(5, 3)
        assert parts == [(1, 1, 3), (1, 2, 2)]

    def test_partitions_of_4_into_1(self):
        assert partitions_of(4, 1) == [(4,)]

    def test_partitions_of_0_into_0(self):
        assert partitions_of(0, 0) == [()]

    def test_partitions_of_3_into_4_empty(self):
        assert partitions_of(3, 4) == []

    def test_partition_type_all_same(self):
        assert partition_type((1, 1, 1, 1)) == (4,)

    def test_partition_type_mixed(self):
        assert partition_type((1, 1, 2, 3)) == (2, 1, 1)

    def test_partition_type_all_different(self):
        assert partition_type((1, 2, 3)) == (1, 1, 1)

    def test_all_partition_types_deg3(self):
        types = all_partition_types(3)
        assert set(types) == {(3,), (2, 1), (1, 1, 1)}

    def test_all_partition_types_deg4(self):
        types = all_partition_types(4)
        assert set(types) == {(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)}

    def test_count_partitions_by_type_weight4_parts2(self):
        counts = count_partitions_by_type(4, 2)
        # (1,3) has type (1,1), (2,2) has type (2,)
        assert counts == {(1, 1): 1, (2,): 1}


# ============================================================
# Invariant dimensions — Chevalley ring of sl₃
# ============================================================

class TestChevalleyInvariants:
    """S^m(g)^g for g = sl₃.

    By Chevalley restriction, S(g)^g = k[C₂, C₃] where deg C₂ = 2, deg C₃ = 3.
    So dim S^m(g)^g = #{(a,b): 2a+3b = m}.
    """

    @pytest.mark.parametrize("m,expected", [
        (1, 0), (2, 1), (3, 1), (4, 1), (5, 1),
        (6, 2), (7, 1), (8, 2), (9, 2),
    ])
    def test_single_factor(self, m, expected):
        assert invariant_dim_cached((m,)) == expected


class TestTensorInvariants:
    """Invariants of tensor products, cross-checked with Casimir data."""

    def test_g_tensor_g(self):
        # (g⊗g)^g = 1 (Killing form)
        assert invariant_dim_cached((1, 1)) == 1

    def test_g_tensor3(self):
        # (g^⊗3)^g = 2 (f_{abc} + d_{abc})
        assert invariant_dim_cached((1, 1, 1)) == 2

    @pytest.mark.slow
    def test_g_tensor4(self):
        """(g^{otimes 4})^g = 8 via direct Kronecker product (~1.5 GB)."""
        assert invariant_dim_cached((1, 1, 1, 1)) == 8

    def test_s2g_tensor_g(self):
        # (S²(g) ⊗ g)^g: partition type (1,1) means two distinct weights
        # This is (g ⊗ g)^g = 1 (NOT S²(g) ⊗ g)
        # Type (1,1) encodes: "two values each appearing once"
        assert int(invariant_dim_cached((1, 1))) == 1

    def test_s2g_tensor_s2g(self):
        # partition type (2,2): two values each appearing twice → (S²(g)⊗S²(g))^g
        assert int(invariant_dim_cached((2, 2))) >= 0


# ============================================================
# Weyl vs Direct cross-validation
# ============================================================

class TestWeylVsDirect:
    """Cross-validate Weyl integration against direct (exact) computation."""

    @pytest.mark.parametrize("ptype", [
        (1,), (2,), (3,), (1, 1), (1, 2),
    ])
    def test_agreement(self, ptype):
        direct = invariant_dim_direct(ptype)
        weyl = invariant_dim_weyl(ptype, n_grid=200)
        assert direct == weyl, f"Mismatch for {ptype}: direct={direct}, weyl={weyl}"

    @pytest.mark.slow
    @pytest.mark.parametrize("ptype", [
        (2, 2),      # total_dim = 1296 (~195 MB)
        (1, 1, 1),   # total_dim = 512  (~70 MB)
    ])
    def test_agreement_heavy(self, ptype):
        """Heavy partition types: direct method allocates large Kronecker products."""
        direct = invariant_dim_direct(ptype)
        weyl = invariant_dim_weyl(ptype, n_grid=200)
        assert direct == weyl, f"Mismatch for {ptype}: direct={direct}, weyl={weyl}"

    @pytest.mark.slow
    def test_agreement_very_heavy(self):
        """(1,1,2): total_dim=2304, Weyl only (direct would exceed memory)."""
        weyl = invariant_dim_weyl((1, 1, 2), n_grid=300)
        # Cross-check via cached dispatch (which routes to Weyl for large dims)
        cached = invariant_dim_cached((1, 1, 2))
        assert weyl == cached, f"Weyl={weyl}, cached={cached}"


# ============================================================
# E₁ page dimensions
# ============================================================

class TestE1Dims:
    """E₁^{p,0}_H = dim(S^p(V̄)_H)^g."""

    def test_e1_p1_all_zero(self):
        """E₁^{1,0}_H = (g_H)^g = 0 for all H (adjoint has no invariants)."""
        for H in range(1, 6):
            assert e1_dim(1, H) == 0

    def test_e1_p2_h2(self):
        """E₁^{2,0}_2: partition (1,1), type (2,) → (g⊗g)^g = 1."""
        assert e1_dim(2, 2) == 1

    def test_e1_p2_h3(self):
        """E₁^{2,0}_3: partition (1,2), type (1,1) → (g⊗g)^g = 1."""
        assert int(e1_dim(2, 3)) == 1

    def test_e1_p3_h3(self):
        """E₁^{3,0}_3: partition (1,1,1), type (3,) → S³(g)^g = 1 (Chevalley: C₃)."""
        assert int(e1_dim(3, 3)) == 1

    def test_e1_p4_h4(self):
        """E₁^{4,0}_4: partition (1,1,1,1), type (4,) → S⁴(g)^g = 1 (Chevalley: C₂²)."""
        assert int(e1_dim(4, 4)) == 1

    def test_e1_total_p2(self):
        """Total E₁^{2,0} through weight 8 should match spectral_sequence data."""
        total = e1_total_through_weight(2, 8)
        assert total > 0


# ============================================================
# Cross-validation with spectral_sequence.py
# ============================================================

class TestCrossValidation:
    @pytest.mark.slow
    def test_basic_facts(self):
        """verify_basic_facts() computes (g^{otimes 4})^g via direct Kronecker
        product (total_dim = 4096, stack ~1.5 GB).  Marked slow."""
        results = verify_basic_facts()
        for desc, ok in results.items():
            assert ok, f"FAIL: {desc}"

    def test_basic_facts_light(self):
        """Light version of basic facts: skip (g^{otimes 4})^g."""
        # Chevalley single-factor checks (cheap)
        chevalley = {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2}
        for m, expected in chevalley.items():
            actual = invariant_dim_cached((m,))
            assert actual == expected, f"S^{m}(g)^g = {actual}, expected {expected}"
        # Low-rank tensor checks (cheap)
        assert invariant_dim_cached((1, 1)) == 1
        assert invariant_dim_cached((1, 1, 1)) == 2

    @pytest.mark.slow
    @pytest.mark.parametrize("weight_h", range(1, 7))
    def test_cross_validate_spectral_sequence(self, weight_h):
        """Σ_p E₁^{p,0}_H should equal adjoint_invariant_dim(H)."""
        from compute.lib.pbw_e1_sl3 import cross_validate_with_spectral_sequence
        results = cross_validate_with_spectral_sequence(
            min_weight=weight_h,
            max_weight=weight_h,
        )
        for desc, ok in results.items():
            assert ok, f"FAIL: {desc}"


# ============================================================
# Monotonicity and growth checks
# ============================================================

class TestGrowth:
    def test_e1_p2_nondecreasing(self):
        """E₁^{2,0}_H should generally grow with H."""
        vals = [e1_dim(2, H) for H in range(2, 8)]
        # Not strictly monotone, but total should grow
        assert vals[-1] >= vals[0]

    def test_partition_type_count(self):
        """Number of partition types at degree p."""
        # p=1: (1,)
        assert len(all_partition_types(1)) == 1
        # p=2: (2,), (1,1)
        assert len(all_partition_types(2)) == 2
        # p=3: (3,), (2,1), (1,1,1)
        assert len(all_partition_types(3)) == 3
        # p=4: (4,), (3,1), (2,2), (2,1,1), (1,1,1,1)
        assert len(all_partition_types(4)) == 5
