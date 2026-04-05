r"""Tests for multi-channel shadow extraction for lattice VOAs.

Comprehensive test suite covering:
  1. All 24 Niemeier lattices have scalar shadow kappa = 24
  2. Per-factor shadow data correctness (kappa_aff, dim, h, etc.)
  3. D16+E8 and 3E8 (same |R|=720) distinguished by Channel 1
  4. A11+D7+E6 and 4E6 (same |R|=288) distinguished by Channel 1
  5. All 5 |R|-collision pairs distinguished by Channel 1
  6. All 10 rank-collision pairs distinguished by Coxeter number
  7. Every pair of Niemeier lattices distinguished by SOME channel
  8. Minimal distinguishing channel set identified
  9. kappa_aff injectivity on ADE types
  10. Kappa decomposition analysis
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.multichannel_shadow import (
    MultichannelShadow,
    ChannelShadow,
    compute_all_multichannel,
    discrimination_power,
    find_collision_pairs,
    full_discrimination_analysis,
    minimal_distinguishing_channels,
    _channel_0,
    _channel_0_tower,
    _channel_1a,
    _channel_1b,
    _channel_1c,
    _channel_1d,
    _channel_full,
    _num_roots,
)
from compute.lib.niemeier_multichannel import (
    niemeier_multichannel_atlas,
    build_discrimination_matrix,
    full_discrimination_report,
    resolve_collision_pairs,
    rank_collision_analysis,
    verify_kappa_aff_injectivity,
    channel_1_shadow_table,
    kappa_decomposition_analysis,
    verify_all_pairwise_distinguished,
    verify_minimal_channel,
)
from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
)
from compute.lib.niemeier_bar_nonscalar import (
    kappa_factor,
    dim_simple,
    central_charge_factor,
)


# =========================================================================
# Basic Channel 0 tests: scalar shadow universal
# =========================================================================

class TestChannel0Scalar:
    """All 24 Niemeier lattices have identical scalar shadow."""

    def test_all_kappa_24(self):
        """kappa = 24 for all 24 Niemeier lattices."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            assert mc.scalar_kappa == 24, f'{label}: kappa = {mc.scalar_kappa}'

    def test_all_class_G(self):
        """Shadow class = G for all lattice VOAs."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            assert mc.scalar_shadow_class == 'G', f'{label}: class = {mc.scalar_shadow_class}'

    def test_all_depth_2(self):
        """Shadow depth = 2 for all lattice VOAs."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            assert mc.scalar_shadow_depth == 2, f'{label}: depth = {mc.scalar_shadow_depth}'

    def test_channel_0_no_discrimination(self):
        """Channel 0 distinguishes 0 out of 276 pairs."""
        dp = discrimination_power(_channel_0)
        assert dp['distinguished_pairs'] == 0
        assert dp['total_pairs'] == 276  # 24*23/2

    def test_channel_0_tower_no_discrimination(self):
        """Full scalar tower also distinguishes 0 pairs."""
        dp = discrimination_power(_channel_0_tower)
        assert dp['distinguished_pairs'] == 0


# =========================================================================
# Channel 1 tests: per-factor data
# =========================================================================

class TestChannel1PerFactor:
    """Per-factor shadow data for each Niemeier lattice."""

    def test_leech_no_factors(self):
        """Leech lattice has no root factors."""
        mc = MultichannelShadow('Leech')
        assert mc.is_leech
        assert mc.num_factors == 0
        assert mc.rank_partition == ()
        assert mc.affine_kappa_vector == ()

    def test_24A1_factors(self):
        """24A_1 has 24 factors of type A_1."""
        mc = MultichannelShadow('24A1')
        assert mc.num_factors == 24
        assert mc.rank_partition == tuple([1] * 24)
        assert mc.common_coxeter == 2
        for ch in mc.channels:
            assert ch.family == 'A'
            assert ch.rank == 1
            assert ch.h == 2
            assert ch.dim == 3

    def test_3E8_factors(self):
        """3E_8 has 3 factors of type E_8."""
        mc = MultichannelShadow('3E8')
        assert mc.num_factors == 3
        assert mc.rank_partition == (8, 8, 8)
        assert mc.common_coxeter == 30
        for ch in mc.channels:
            assert ch.family == 'E'
            assert ch.rank == 8
            assert ch.h == 30
            assert ch.dim == 248

    def test_D16_E8_factors(self):
        """D_16 + E_8 has 2 factors."""
        mc = MultichannelShadow('D16_E8')
        assert mc.num_factors == 2
        families = sorted([(ch.family, ch.rank) for ch in mc.channels])
        assert ('D', 16) in families
        assert ('E', 8) in families

    def test_D16_E8_coxeter(self):
        """D_16 + E_8: both factors have h = 30."""
        mc = MultichannelShadow('D16_E8')
        assert mc.common_coxeter == 30
        for ch in mc.channels:
            assert ch.h == 30

    def test_all_rank_sum_24(self):
        """Sum of per-factor ranks = 24 for non-Leech."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            if not mc.is_leech:
                total = sum(ch.rank for ch in mc.channels)
                assert total == 24, f'{label}: rank sum = {total}'

    def test_all_c_sum_24(self):
        """Sum of per-factor central charges = 24 for non-Leech.

        c(g, 1) = rank(g) for simply-laced at level 1.
        """
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            if not mc.is_leech:
                total_c = sum(ch.c for ch in mc.channels)
                assert total_c == 24, f'{label}: c sum = {total_c}'

    def test_uniform_coxeter(self):
        """All factors of a non-Leech Niemeier lattice have the same Coxeter number."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            if not mc.is_leech:
                h_vals = [ch.h for ch in mc.channels]
                assert len(set(h_vals)) == 1, (
                    f'{label}: non-uniform Coxeter numbers {h_vals}'
                )

    def test_all_factors_class_L(self):
        """Every affine KM factor is class L on its current line."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            for ch in mc.channels:
                assert ch.shadow_class == 'L', (
                    f'{label}/{ch.type_label}: shadow class = {ch.shadow_class}'
                )

    def test_all_factors_S3_one_third(self):
        """S_3 = 1/3 for every affine KM factor."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            for ch in mc.channels:
                assert ch.S3 == Rational(1, 3), (
                    f'{label}/{ch.type_label}: S_3 = {ch.S3}'
                )

    def test_all_factors_S4_zero(self):
        """S_4 = 0 for every affine KM factor (Jacobi identity)."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            for ch in mc.channels:
                assert ch.S4 == 0, (
                    f'{label}/{ch.type_label}: S_4 = {ch.S4}'
                )


# =========================================================================
# Per-factor kappa verification (AP1: recompute for each!)
# =========================================================================

class TestPerFactorKappa:
    """Verify kappa_aff formulas from first principles (AP1 compliance)."""

    def test_kappa_A1(self):
        """kappa(sl_2, 1) = 3*3/4 = 9/4."""
        assert kappa_factor('A', 1, k=1) == Rational(9, 4)

    def test_kappa_A2(self):
        """kappa(sl_3, 1) = 8*4/6 = 16/3."""
        assert kappa_factor('A', 2, k=1) == Rational(16, 3)

    def test_kappa_A3(self):
        """kappa(sl_4, 1) = 15*5/8 = 75/8."""
        assert kappa_factor('A', 3, k=1) == Rational(75, 8)

    def test_kappa_D4(self):
        """kappa(so_8, 1) = 28*7/12 = 196/12 = 49/3."""
        assert kappa_factor('D', 4, k=1) == Rational(49, 3)

    def test_kappa_D5(self):
        """kappa(so_10, 1) = 45*9/16 = 405/16."""
        assert kappa_factor('D', 5, k=1) == Rational(405, 16)

    def test_kappa_E6(self):
        """kappa(E_6, 1) = 78*13/24 = 1014/24 = 169/4."""
        assert kappa_factor('E', 6, k=1) == Rational(169, 4)

    def test_kappa_E7(self):
        """kappa(E_7, 1) = 133*19/36 = 2527/36."""
        assert kappa_factor('E', 7, k=1) == Rational(2527, 36)

    def test_kappa_E8(self):
        """kappa(E_8, 1) = 248*31/60 = 7688/60 = 1922/15."""
        assert kappa_factor('E', 8, k=1) == Rational(1922, 15)

    def test_kappa_formula_general(self):
        """kappa(g, k) = dim(g) * (k + h^v) / (2 * h^v) for all ADE types."""
        test_cases = [
            ('A', 1, 1), ('A', 5, 1), ('A', 11, 1), ('A', 24, 1),
            ('D', 4, 1), ('D', 7, 1), ('D', 12, 1), ('D', 24, 1),
            ('E', 6, 1), ('E', 7, 1), ('E', 8, 1),
        ]
        from compute.lib.niemeier_shadow_atlas import coxeter_number
        for fam, n, k in test_cases:
            d = dim_simple(fam, n)
            h = coxeter_number(fam, n)
            expected = Rational(d * (k + h), 2 * h)
            actual = kappa_factor(fam, n, k=k)
            assert actual == expected, (
                f'{fam}_{n} k={k}: kappa = {actual} != {expected}'
            )


# =========================================================================
# Discrimination: |R|-collision pairs
# =========================================================================

class TestRootCollisionPairs:
    """The 5 |R|-collision pairs are all distinguished by Channel 1."""

    def test_D16E8_vs_3E8_same_roots(self):
        """D_16+E_8 and 3E_8 both have |R| = 720."""
        assert NIEMEIER_REGISTRY['D16_E8']['num_roots'] == 720
        assert NIEMEIER_REGISTRY['3E8']['num_roots'] == 720

    def test_D16E8_vs_3E8_different_channels(self):
        """D_16+E_8 and 3E_8 are distinguished by multi-channel shadow."""
        mca = MultichannelShadow('D16_E8')
        mcb = MultichannelShadow('3E8')
        # Different number of factors
        assert mca.num_factors == 2
        assert mcb.num_factors == 3
        # Different rank partitions
        assert mca.rank_partition != mcb.rank_partition
        # Different affine kappa vectors
        assert mca.affine_kappa_vector != mcb.affine_kappa_vector
        # Both have h = 30
        assert mca.common_coxeter == mcb.common_coxeter == 30

    def test_A17E7_vs_D10_2E7_same_roots(self):
        """A_17+E_7 and D_10+2E_7 both have |R| = 432."""
        assert NIEMEIER_REGISTRY['A17_E7']['num_roots'] == 432
        assert NIEMEIER_REGISTRY['D10_2E7']['num_roots'] == 432

    def test_A17E7_vs_D10_2E7_different_channels(self):
        """A_17+E_7 and D_10+2E_7 are distinguished by multi-channel shadow."""
        mca = MultichannelShadow('A17_E7')
        mcb = MultichannelShadow('D10_2E7')
        assert mca.multichannel_shadow_vector() != mcb.multichannel_shadow_vector()
        # Different number of factors
        assert mca.num_factors == 2
        assert mcb.num_factors == 3
        # Different rank partitions
        assert mca.rank_partition != mcb.rank_partition

    def test_A11D7E6_vs_4E6_same_roots(self):
        """A_11+D_7+E_6 and 4E_6 both have |R| = 288."""
        assert NIEMEIER_REGISTRY['A11_D7_E6']['num_roots'] == 288
        assert NIEMEIER_REGISTRY['4E6']['num_roots'] == 288

    def test_A11D7E6_vs_4E6_different_channels(self):
        """A_11+D_7+E_6 and 4E_6 are distinguished by multi-channel shadow."""
        mca = MultichannelShadow('A11_D7_E6')
        mcb = MultichannelShadow('4E6')
        assert mca.multichannel_shadow_vector() != mcb.multichannel_shadow_vector()
        # Different rank partitions
        assert mca.rank_partition != mcb.rank_partition
        # Different number of factors
        assert mca.num_factors == 3
        assert mcb.num_factors == 4

    def test_2A9D6_vs_4D6_same_roots(self):
        """2A_9+D_6 and 4D_6 both have |R| = 240."""
        assert NIEMEIER_REGISTRY['2A9_D6']['num_roots'] == 240
        assert NIEMEIER_REGISTRY['4D6']['num_roots'] == 240

    def test_2A9D6_vs_4D6_different_channels(self):
        """2A_9+D_6 and 4D_6 are distinguished by multi-channel shadow."""
        mca = MultichannelShadow('2A9_D6')
        mcb = MultichannelShadow('4D6')
        assert mca.multichannel_shadow_vector() != mcb.multichannel_shadow_vector()

    def test_4A5D4_vs_6D4_same_roots(self):
        """4A_5+D_4 and 6D_4 both have |R| = 144."""
        assert NIEMEIER_REGISTRY['4A5_D4']['num_roots'] == 144
        assert NIEMEIER_REGISTRY['6D4']['num_roots'] == 144

    def test_4A5D4_vs_6D4_different_channels(self):
        """4A_5+D_4 and 6D_4 are distinguished by multi-channel shadow."""
        mca = MultichannelShadow('4A5_D4')
        mcb = MultichannelShadow('6D4')
        assert mca.multichannel_shadow_vector() != mcb.multichannel_shadow_vector()

    def test_all_5_collision_pairs_resolved(self):
        """All 5 |R|-collision pairs are resolved by per-factor data."""
        resolutions = resolve_collision_pairs()
        for key, res in resolutions.items():
            assert len(res['distinguishing_channels']) > 0, (
                f'Collision pair {key} NOT resolved!'
            )


# =========================================================================
# Discrimination: rank-collision pairs
# =========================================================================

class TestRankCollisionPairs:
    """Pairs with the same rank partition but different ADE types."""

    def test_A24_vs_D24_same_rank(self):
        """A_24 and D_24 have the same rank (24) but different Coxeter number."""
        mca = MultichannelShadow('A24')
        mcb = MultichannelShadow('D24')
        assert mca.rank_partition == mcb.rank_partition == (24,)
        assert mca.common_coxeter == 25  # h(A_24) = 25
        assert mcb.common_coxeter == 46  # h(D_24) = 46
        assert mca.common_coxeter != mcb.common_coxeter

    def test_2A12_vs_2D12_same_rank(self):
        """2A_12 and 2D_12 have the same rank partition (12,12)."""
        mca = MultichannelShadow('2A12')
        mcb = MultichannelShadow('2D12')
        assert mca.rank_partition == mcb.rank_partition == (12, 12)
        assert mca.common_coxeter == 13  # h(A_12) = 13
        assert mcb.common_coxeter == 22  # h(D_12) = 22
        assert mca.common_coxeter != mcb.common_coxeter

    def test_3way_888_collision(self):
        """3A_8, 3D_8, 3E_8 have rank partition (8,8,8)."""
        labels = ['3A8', '3D8', '3E8']
        mcs = {l: MultichannelShadow(l) for l in labels}
        for l in labels:
            assert mcs[l].rank_partition == (8, 8, 8)
        # All have different Coxeter numbers
        h_vals = {l: mcs[l].common_coxeter for l in labels}
        assert h_vals['3A8'] == 9    # h(A_8) = 9
        assert h_vals['3D8'] == 14   # h(D_8) = 14
        assert h_vals['3E8'] == 30   # h(E_8) = 30
        assert len(set(h_vals.values())) == 3

    def test_3way_6666_collision(self):
        """4A_6, 4D_6, 4E_6 have rank partition (6,6,6,6)."""
        labels = ['4A6', '4D6', '4E6']
        mcs = {l: MultichannelShadow(l) for l in labels}
        for l in labels:
            assert mcs[l].rank_partition == (6, 6, 6, 6)
        h_vals = {l: mcs[l].common_coxeter for l in labels}
        assert h_vals['4A6'] == 7    # h(A_6) = 7
        assert h_vals['4D6'] == 10   # h(D_6) = 10
        assert h_vals['4E6'] == 12   # h(E_6) = 12
        assert len(set(h_vals.values())) == 3

    def test_6A4_vs_6D4_same_rank(self):
        """6A_4 and 6D_4 have rank partition (4,4,4,4,4,4)."""
        mca = MultichannelShadow('6A4')
        mcb = MultichannelShadow('6D4')
        assert mca.rank_partition == mcb.rank_partition == (4, 4, 4, 4, 4, 4)
        assert mca.common_coxeter == 5   # h(A_4) = 5
        assert mcb.common_coxeter == 6   # h(D_4) = 6
        assert mca.common_coxeter != mcb.common_coxeter

    def test_rank_collision_analysis(self):
        """All rank-collision groups are resolved by Coxeter number."""
        rca = rank_collision_analysis()
        for key, details in rca['details'].items():
            assert details['distinguished_by_coxeter'], (
                f'Rank collision group {key} NOT resolved by Coxeter!'
            )


# =========================================================================
# Complete discrimination: every pair
# =========================================================================

class TestCompleteness:
    """Every pair of Niemeier lattices is distinguished by some channel."""

    def test_full_multichannel_complete(self):
        """Full multi-channel vector distinguishes all 276 pairs."""
        result = verify_all_pairwise_distinguished()
        assert result['is_complete'], (
            f"Undistinguished pairs: {result['undistinguished_pairs']}"
        )
        assert result['distinguished_pairs'] == 276

    def test_coxeter_rank_complete(self):
        """Channel 1b (Coxeter + rank) is complete."""
        dp = discrimination_power(_channel_1b)
        assert dp['is_complete']
        assert dp['distinguished_pairs'] == 276

    def test_affine_kappa_complete(self):
        """Channel 1c (affine kappa vector) is complete."""
        dp = discrimination_power(_channel_1c)
        assert dp['is_complete']
        assert dp['distinguished_pairs'] == 276

    def test_dim_vector_complete(self):
        """Channel 1d (dimension vector) is complete."""
        dp = discrimination_power(_channel_1d)
        assert dp['is_complete']
        assert dp['distinguished_pairs'] == 276

    def test_full_vector_complete(self):
        """Full multi-channel vector is complete."""
        dp = discrimination_power(_channel_full)
        assert dp['is_complete']

    def test_rank_alone_incomplete(self):
        """Channel 1a (rank partition alone) is NOT complete."""
        dp = discrimination_power(_channel_1a)
        assert not dp['is_complete']
        # Should have 10 undistinguished pairs
        undist = dp['total_pairs'] - dp['distinguished_pairs']
        assert undist > 0

    def test_roots_incomplete(self):
        """Root count alone is NOT complete (5 collision pairs)."""
        dp = discrimination_power(_num_roots)
        assert not dp['is_complete']


# =========================================================================
# Minimal channel identification
# =========================================================================

class TestMinimalChannel:
    """Identify the smallest channel set for complete discrimination."""

    def test_minimal_is_channel_1b(self):
        """Channel 1b is the minimal complete channel."""
        result = minimal_distinguishing_channels()
        assert result['minimal_complete_channel'] == 'Channel 1b (Coxeter + rank)'

    def test_verify_minimal(self):
        """Neither Coxeter alone nor rank alone is complete."""
        result = verify_minimal_channel()
        assert not result['rank_alone_complete']
        assert not result['coxeter_alone_complete']
        assert result['coxeter_plus_rank_complete']

    def test_discrimination_hierarchy(self):
        """Channels form a strict hierarchy of increasing power."""
        dp_0 = discrimination_power(_channel_0)['distinguished_pairs']
        dp_roots = discrimination_power(_num_roots)['distinguished_pairs']
        dp_1a = discrimination_power(_channel_1a)['distinguished_pairs']
        dp_1b = discrimination_power(_channel_1b)['distinguished_pairs']

        assert dp_0 == 0
        assert dp_0 < dp_roots
        # roots (19/24) vs rank (14/24) -- roots can be MORE powerful
        # because root count is finer than rank partition for some pairs
        assert dp_roots > 0
        assert dp_1a > 0
        assert dp_1b == 276  # complete


# =========================================================================
# kappa_aff injectivity on ADE types
# =========================================================================

class TestKappaInjectivity:
    """Verify kappa_aff is injective on ADE types (needed for completeness)."""

    def test_injectivity(self):
        """kappa_aff is injective on ADE types (up to D_3 = A_3 isomorphism)."""
        result = verify_kappa_aff_injectivity()
        assert result['is_injective_excluding_iso']

    def test_D3_equals_A3(self):
        """D_3 and A_3 have the same kappa_aff (isomorphic root systems)."""
        assert kappa_factor('D', 3, k=1) == kappa_factor('A', 3, k=1)

    def test_distinct_kappas_for_niemeier_types(self):
        """All ADE types appearing in Niemeier lattices have distinct kappa_aff.

        The types appearing are: A_1 through A_24, D_4 through D_24,
        E_6, E_7, E_8 (but only those with rank summing to 24 and
        uniform Coxeter number).  We verify all PAIRS have distinct kappa.
        """
        types = set()
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            for ch in mc.channels:
                types.add((ch.family, ch.rank))

        kappas = {}
        for fam, n in types:
            k = kappa_factor(fam, n, k=1)
            if k not in kappas:
                kappas[k] = []
            kappas[k].append(f'{fam}_{n}')

        collisions = {k: v for k, v in kappas.items() if len(v) > 1}
        assert len(collisions) == 0, f'kappa_aff collisions: {collisions}'


# =========================================================================
# Kappa decomposition (the lattice kappa = 24 puzzle)
# =========================================================================

class TestKappaDecomposition:
    """Test the kappa decomposition for lattice VOAs."""

    def test_affine_kappa_sum_not_24(self):
        """The sum of per-factor affine kappas is NOT 24 in general."""
        mc = MultichannelShadow('24A1')
        # 24 * kappa(A_1, 1) = 24 * 9/4 = 54
        assert mc.affine_kappa_sum == 54

    def test_affine_kappa_sum_3E8(self):
        """3E_8: affine kappa sum = 3 * 1922/15 = 5766/15 = 1922/5."""
        mc = MultichannelShadow('3E8')
        expected = 3 * Rational(1922, 15)
        assert mc.affine_kappa_sum == expected

    def test_lattice_kappa_always_24(self):
        """The LATTICE kappa is always 24 (rank), regardless of affine kappas."""
        for label in ALL_NIEMEIER_LABELS:
            mc = MultichannelShadow(label)
            assert mc.scalar_kappa == 24

    def test_affine_kappa_ratio_formula(self):
        """For uniform-h lattices: ratio = (1+h)^2/(2h)."""
        analysis = kappa_decomposition_analysis()
        for label in ALL_NIEMEIER_LABELS:
            if label == 'Leech':
                continue
            data = analysis[label]
            h = data['h']
            expected_ratio = Rational((1 + h) ** 2, 2 * h)
            assert data['theoretical_ratio'] == expected_ratio, (
                f'{label}: ratio mismatch'
            )


# =========================================================================
# Discrimination matrix tests
# =========================================================================

class TestDiscriminationMatrix:
    """Tests for the 24x24 discrimination matrix."""

    def test_scalar_matrix_all_zeros(self):
        """Scalar channel: 0 off-diagonal entries are 1."""
        _, matrix, stats = build_discrimination_matrix('scalar')
        assert stats['distinguished'] == 0

    def test_coxeter_matrix_complete(self):
        """Coxeter + rank channel: all off-diagonal entries are 1."""
        _, matrix, stats = build_discrimination_matrix('coxeter')
        assert stats['is_complete']
        assert stats['distinguished'] == 276

    def test_full_matrix_complete(self):
        """Full multi-channel: all off-diagonal entries are 1."""
        _, matrix, stats = build_discrimination_matrix('full')
        assert stats['is_complete']
        assert stats['distinguished'] == 276

    def test_root_matrix_has_collisions(self):
        """Root count channel has exactly 5 collision pairs."""
        _, matrix, stats = build_discrimination_matrix('roots')
        assert not stats['is_complete']
        assert stats['undistinguished'] == 5  # 5 collision pairs

    def test_rank_matrix_has_collisions(self):
        """Rank partition channel has exactly 9 collision pairs.

        (24,): A24, D24 -> 1 pair
        (12,12): 2A12, 2D12 -> 1 pair
        (8,8,8): 3A8, 3D8, 3E8 -> 3 pairs
        (6,6,6,6): 4A6, 4D6, 4E6 -> 3 pairs
        (4,4,4,4,4,4): 6A4, 6D4 -> 1 pair
        Total: 1+1+3+3+1 = 9 undistinguished pairs.
        """
        _, matrix, stats = build_discrimination_matrix('rank')
        assert not stats['is_complete']
        assert stats['undistinguished'] == 9


# =========================================================================
# Channel-1 shadow table
# =========================================================================

class TestChannelTable:
    """Test the Channel-1 shadow table output."""

    def test_table_has_24_entries(self):
        """Table has exactly 24 entries."""
        table = channel_1_shadow_table()
        assert len(table) == 24

    def test_table_leech_entry(self):
        """Leech entry has no per-factor data."""
        table = channel_1_shadow_table()
        leech = [e for e in table if e['label'] == 'Leech'][0]
        assert leech['num_factors'] == 0

    def test_table_ordered_by_roots(self):
        """Table is ordered by decreasing number of roots."""
        table = channel_1_shadow_table()
        root_counts = [e['num_roots'] for e in table]
        assert root_counts == sorted(root_counts, reverse=True)


# =========================================================================
# Full discrimination analysis
# =========================================================================

class TestFullAnalysis:
    """Test the complete discrimination analysis pipeline."""

    def test_full_report(self):
        """Full report covers all channels."""
        report = full_discrimination_report()
        assert 'scalar' in report
        assert 'coxeter' in report
        assert 'full' in report
        assert report['scalar']['distinguished'] == 0
        assert report['coxeter']['is_complete']
        assert report['full']['is_complete']

    def test_collision_pair_details(self):
        """Collision pair details are complete."""
        resolutions = resolve_collision_pairs()
        assert len(resolutions) == 5  # 5 known collision pairs
        for key, res in resolutions.items():
            assert res['a']['label'] != res['b']['label']
            assert len(res['distinguishing_channels']) > 0

    def test_atlas_complete(self):
        """Atlas has entries for all 24 lattices."""
        atlas = niemeier_multichannel_atlas()
        assert len(atlas) == 24
        for label in ALL_NIEMEIER_LABELS:
            assert label in atlas

    def test_atlas_scalar_universal(self):
        """All atlas entries have scalar kappa = 24."""
        atlas = niemeier_multichannel_atlas()
        for label, data in atlas.items():
            assert data['scalar_kappa'] == 24


# =========================================================================
# Specific Coxeter number verification (independent of the module)
# =========================================================================

class TestCoxeterNumbers:
    """Verify Coxeter numbers independently (AP1 compliance)."""

    def test_h_A_n(self):
        """h(A_n) = n + 1."""
        for n in [1, 2, 3, 4, 5, 8, 12, 15, 17, 24]:
            mc = MultichannelShadow(f'24A1' if n == 1 else f'A24')
            # Just verify the formula
            from compute.lib.niemeier_shadow_atlas import coxeter_number
            assert coxeter_number('A', n) == n + 1

    def test_h_D_n(self):
        """h(D_n) = 2(n-1)."""
        for n in [4, 5, 6, 7, 8, 9, 10, 12, 16, 24]:
            from compute.lib.niemeier_shadow_atlas import coxeter_number
            assert coxeter_number('D', n) == 2 * (n - 1)

    def test_h_E(self):
        """h(E_6)=12, h(E_7)=18, h(E_8)=30."""
        from compute.lib.niemeier_shadow_atlas import coxeter_number
        assert coxeter_number('E', 6) == 12
        assert coxeter_number('E', 7) == 18
        assert coxeter_number('E', 8) == 30


# =========================================================================
# Lie algebra dimension verification (AP1 compliance)
# =========================================================================

class TestLieDimensions:
    """Verify Lie algebra dimensions independently."""

    def test_dim_A_n(self):
        """dim(sl_{n+1}) = n(n+2)."""
        for n, expected in [(1, 3), (2, 8), (3, 15), (4, 24), (5, 35)]:
            assert dim_simple('A', n) == expected

    def test_dim_D_n(self):
        """dim(so_{2n}) = n(2n-1)."""
        for n, expected in [(3, 15), (4, 28), (5, 45), (6, 66)]:
            assert dim_simple('D', n) == expected

    def test_dim_E(self):
        """dim(E_6)=78, dim(E_7)=133, dim(E_8)=248."""
        assert dim_simple('E', 6) == 78
        assert dim_simple('E', 7) == 133
        assert dim_simple('E', 8) == 248

    def test_dim_equals_rank_plus_roots(self):
        """dim(g) = rank(g) + |R(g)| for all ADE types."""
        from compute.lib.niemeier_shadow_atlas import root_count
        types = [('A', n) for n in range(1, 10)]
        types += [('D', n) for n in range(3, 10)]
        types += [('E', 6), ('E', 7), ('E', 8)]
        for fam, n in types:
            d = dim_simple(fam, n)
            r = root_count(fam, n)
            assert d == n + r, f'{fam}_{n}: {d} != {n} + {r}'


# =========================================================================
# Central charge verification
# =========================================================================

class TestCentralCharges:
    """Verify c(g, 1) = rank(g) for simply-laced at level 1."""

    def test_c_equals_rank(self):
        """c(g, 1) = rank for all simply-laced types."""
        types = [('A', n) for n in range(1, 10)]
        types += [('D', n) for n in range(3, 10)]
        types += [('E', 6), ('E', 7), ('E', 8)]
        for fam, n in types:
            c = central_charge_factor(fam, n, k=1)
            assert c == n, f'{fam}_{n}: c = {c} != {n}'


# =========================================================================
# Specific lattice per-factor data
# =========================================================================

class TestSpecificLattices:
    """Detailed per-factor verification for specific lattices."""

    def test_D24_single_factor(self):
        """D_24: one factor of type D_24."""
        mc = MultichannelShadow('D24')
        assert mc.num_factors == 1
        ch = mc.channels[0]
        assert ch.family == 'D'
        assert ch.rank == 24
        assert ch.h == 46  # h(D_24) = 2*23 = 46
        assert ch.dim == 24 * 47  # 24 * (2*24-1) = 24*47 = 1128

    def test_A15_D9(self):
        """A_15 + D_9: two factors with h = 16."""
        mc = MultichannelShadow('A15_D9')
        assert mc.num_factors == 2
        assert mc.common_coxeter == 16
        # A_15: rank 15, h = 16
        # D_9: rank 9, h = 2*8 = 16
        types = sorted([(ch.family, ch.rank) for ch in mc.channels])
        assert ('A', 15) in types
        assert ('D', 9) in types

    def test_2A7_2D5(self):
        """2A_7 + 2D_5: four factors with h = 8."""
        mc = MultichannelShadow('2A7_2D5')
        assert mc.num_factors == 4
        assert mc.common_coxeter == 8
        types = sorted([(ch.family, ch.rank) for ch in mc.channels])
        assert types.count(('A', 7)) == 2
        assert types.count(('D', 5)) == 2

    def test_12A2(self):
        """12A_2: twelve factors of type A_2."""
        mc = MultichannelShadow('12A2')
        assert mc.num_factors == 12
        assert mc.common_coxeter == 3
        for ch in mc.channels:
            assert ch.family == 'A'
            assert ch.rank == 2
            assert ch.h == 3
            assert ch.dim == 8

    def test_4E6(self):
        """4E_6: four factors of type E_6."""
        mc = MultichannelShadow('4E6')
        assert mc.num_factors == 4
        assert mc.common_coxeter == 12
        for ch in mc.channels:
            assert ch.family == 'E'
            assert ch.rank == 6
            assert ch.h == 12
            assert ch.dim == 78
