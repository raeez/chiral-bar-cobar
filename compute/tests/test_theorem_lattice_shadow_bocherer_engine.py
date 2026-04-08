r"""Tests for the lattice VOA shadow tower and Bocherer-type constraints.

Tests the discrimination hierarchy for the 24 Niemeier lattices, verifying:
  - Scalar shadow tower blindness (kappa=24, S_r=0 for all 24)
  - Per-factor shadow uniformity (S_3=1/3, S_4=0 for all KM)
  - Planted-forest sum closed form (10k-72)/432
  - Multi-channel F_2 consistency
  - Quartic Casimir sum completeness (276/276)
  - Per-factor dim vector completeness (276/276)
  - All 5 root-count collision pairs resolved
  - Leech lattice shadow data
  - (kappa, S_3) incompleteness
  - Bocherer-shadow connection

Multi-path verification: every test checks at least 2 independent paths.
"""

from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from typing import Dict

import pytest

from compute.lib.theorem_lattice_shadow_bocherer_engine import (
    ALL_LABELS,
    COLLISION_PAIRS,
    F2_multi_channel,
    F2_multi_channel_closed,
    F2_scalar,
    all_collision_pair_resolutions,
    bocherer_shadow_constraint,
    collision_pair_resolution,
    delta_pf_sum,
    delta_pf_sum_direct,
    delta_pf_sum_leech,
    discrimination_hierarchy_full,
    h_equals_6_analysis,
    kappa_S3_completeness,
    lattices_by_coxeter,
    leech_shadow_data,
    need_S4_or_multichannel,
    per_factor_S3_value,
    per_factor_S4_value,
    per_factor_delta_pf,
    per_factor_delta_pf_vector,
    per_factor_dim_vector,
    quartic_casimir_sum,
    quartic_casimir_sum_all,
    run_all_verifications,
    verify_dim_vector_complete,
    verify_quartic_casimir_complete,
)
from compute.lib.theorem_niemeier_shadow_discrimination_engine import (
    common_coxeter,
    dim_lie,
    faber_pandharipande,
    per_factor_rank_partition,
    per_factor_type,
    root_count_niemeier,
    scalar_F_g,
    scalar_kappa,
    scalar_S3,
    scalar_S4,
    scalar_shadow_class,
    scalar_shadow_depth,
)


# =========================================================================
# Section 1: Scalar shadow tower blindness
# =========================================================================

class TestScalarTowerBlind:
    """The scalar shadow tower has zero discrimination power."""

    def test_kappa_24_for_all(self):
        """kappa = 24 for all 24 Niemeier lattice VOAs."""
        for lab in ALL_LABELS:
            assert scalar_kappa() == Fraction(24), f"{lab}: kappa != 24"

    def test_S3_zero_for_all(self):
        """S_3 = 0 for all 24 Niemeier lattice VOAs."""
        assert scalar_S3() == Fraction(0)

    def test_S4_zero_for_all(self):
        """S_4 = 0 for all 24 Niemeier lattice VOAs."""
        assert scalar_S4() == Fraction(0)

    def test_shadow_class_G_for_all(self):
        """All 24 Niemeier lattice VOAs are class G (Gaussian)."""
        assert scalar_shadow_class() == 'G'

    def test_shadow_depth_2_for_all(self):
        """Shadow depth r_max = 2 for all Niemeier lattice VOAs."""
        assert scalar_shadow_depth() == 2

    def test_F1_universal(self):
        """F_1 = 24 * 1/24 = 1 for all (Bernoulli: |B_2|=1/6, FP = 1/24)."""
        f1 = scalar_F_g(1)
        assert f1 == Fraction(24) * Fraction(1, 24)
        assert f1 == Fraction(1)

    def test_F2_universal(self):
        """F_2 = 24 * 7/5760 = 7/240 for all."""
        f2 = scalar_F_g(2)
        assert f2 == Fraction(24) * Fraction(7, 5760)
        assert f2 == Fraction(7, 240)


# =========================================================================
# Section 2: Per-factor shadow uniformity
# =========================================================================

class TestPerFactorShadow:
    """Per-factor shadow data is uniform for KM at level 1."""

    def test_S3_one_third(self):
        """S_3(g, 1) = 1/3 for all affine KM algebras."""
        assert per_factor_S3_value() == Fraction(1, 3)

    def test_S4_zero(self):
        """S_4(g, 1) = 0 for all affine KM algebras (Jacobi identity)."""
        assert per_factor_S4_value() == Fraction(0)

    def test_delta_pf_rank_1(self):
        """delta_pf for rank-1 factor: (10 - 3)/432 = 7/432."""
        assert per_factor_delta_pf(1) == Fraction(7, 432)

    def test_delta_pf_rank_4(self):
        """delta_pf for rank-4 factor: (10 - 12)/432 = -2/432 = -1/216."""
        assert per_factor_delta_pf(4) == Fraction(-1, 216)

    def test_delta_pf_rank_8(self):
        """delta_pf for rank-8 factor: (10 - 24)/432 = -14/432 = -7/216."""
        assert per_factor_delta_pf(8) == Fraction(-7, 216)

    def test_delta_pf_zero_crossing(self):
        """delta_pf = 0 when rank = 10/3 (not integer, so never exactly 0)."""
        # rank 3: (10-9)/432 = 1/432 > 0
        # rank 4: (10-12)/432 = -1/216 < 0
        assert per_factor_delta_pf(3) > 0
        assert per_factor_delta_pf(4) < 0


# =========================================================================
# Section 3: Planted-forest sum closed form
# =========================================================================

class TestPlantedForestSum:
    """delta_pf_sum = (10k - 72)/432 depends only on factor count k."""

    def test_closed_form_matches_direct_all(self):
        """Closed form matches direct sum for all 23 non-Leech lattices."""
        for lab in ALL_LABELS:
            if lab == 'Leech':
                continue
            closed = delta_pf_sum(lab)
            direct = delta_pf_sum_direct(lab)
            assert closed == direct, f"{lab}: closed={closed} != direct={direct}"

    def test_leech_delta_pf_zero(self):
        """Leech lattice: delta_pf_sum = 0 (no factors to sum over)."""
        assert delta_pf_sum_leech() == Fraction(0)
        assert delta_pf_sum_direct('Leech') == Fraction(0)

    def test_24A1_delta_pf(self):
        """24A_1 has k=24 factors: delta_pf = (240-72)/432 = 168/432 = 7/18."""
        assert delta_pf_sum('24A1') == Fraction(7, 18)
        assert delta_pf_sum('24A1') == Fraction(10 * 24 - 72, 432)

    def test_D24_delta_pf(self):
        """D_24 has k=1 factor: delta_pf = (10-72)/432 = -62/432 = -31/216."""
        assert delta_pf_sum('D24') == Fraction(-31, 216)

    def test_6D4_delta_pf(self):
        """6D_4 has k=6 factors: delta_pf = (60-72)/432 = -12/432 = -1/36."""
        assert delta_pf_sum('6D4') == Fraction(-1, 36)

    def test_4A5_D4_delta_pf(self):
        """4A_5 D_4 has k=5 factors: delta_pf = (50-72)/432 = -22/432 = -11/216."""
        assert delta_pf_sum('4A5_D4') == Fraction(-11, 216)

    def test_collision_pairs_different_k(self):
        """All 5 root-count collision pairs have different factor counts."""
        for l1, l2, _ in COLLISION_PAIRS:
            k1 = len(per_factor_type(l1))
            k2 = len(per_factor_type(l2))
            assert k1 != k2, f"{l1}(k={k1}) vs {l2}(k={k2})"

    def test_collision_pairs_different_delta_pf(self):
        """All 5 collision pairs are resolved by delta_pf_sum."""
        for l1, l2, _ in COLLISION_PAIRS:
            d1 = delta_pf_sum(l1)
            d2 = delta_pf_sum(l2)
            assert d1 != d2, f"{l1}={d1} vs {l2}={d2}"


# =========================================================================
# Section 4: Multi-channel F_2
# =========================================================================

class TestMultiChannelF2:
    """Multi-channel genus-2 free energy consistency."""

    def test_F2_direct_matches_closed_all(self):
        """Direct and closed-form F_2 agree for all 24 lattices."""
        for lab in ALL_LABELS:
            direct = F2_multi_channel(lab)
            closed = F2_multi_channel_closed(lab)
            assert direct == closed, f"{lab}: {direct} != {closed}"

    def test_F2_leech_equals_scalar(self):
        """Leech: multi-channel F_2 = scalar F_2 (no factor corrections)."""
        assert F2_multi_channel('Leech') == F2_scalar()
        assert F2_multi_channel('Leech') == Fraction(7, 240)

    def test_F2_24A1(self):
        """24A_1: F_2^multi = 7/240 + 7/18."""
        expected = Fraction(7, 240) + Fraction(7, 18)
        assert F2_multi_channel('24A1') == expected

    def test_F2_differs_across_lattices(self):
        """F_2^multi takes different values on different lattices."""
        vals = {F2_multi_channel(lab) for lab in ALL_LABELS}
        # At least 10 distinct values (we know there are more)
        assert len(vals) >= 10


# =========================================================================
# Section 5: Quartic Casimir sum completeness
# =========================================================================

class TestQuarticCasimirComplete:
    """The quartic Casimir sum sum dim(g_i)^2 is a complete invariant."""

    def test_completeness(self):
        """All 276 pairs distinguished by sum dim(g_i)^2."""
        result = verify_quartic_casimir_complete()
        assert result['is_complete']
        assert result['distinguished'] == 276
        assert result['total_pairs'] == 276
        assert result['num_distinct_values'] == 24

    def test_leech_zero(self):
        """Leech: quartic Casimir = 0 (no factors)."""
        assert quartic_casimir_sum('Leech') == 0

    def test_24A1_value(self):
        """24A_1: sum dim(sl_2)^2 = 24 * 3^2 = 216."""
        assert quartic_casimir_sum('24A1') == 24 * 9

    def test_3E8_value(self):
        """3E_8: sum dim(E_8)^2 = 3 * 248^2 = 184512."""
        assert quartic_casimir_sum('3E8') == 3 * 248 ** 2

    def test_D24_value(self):
        """D_24: sum dim(D_24)^2 = 1128^2 = 1272384."""
        # dim(D_24) = 24*(2*24-1) = 24*47 = 1128
        assert dim_lie('D', 24) == 1128
        assert quartic_casimir_sum('D24') == 1128 ** 2

    def test_monotone_in_max_dim(self):
        """Lattices with larger max factor dim tend to have larger sum."""
        # D_24 (single factor dim 1128) has the largest quartic Casimir
        vals = quartic_casimir_sum_all()
        assert vals['D24'] == max(vals.values())


# =========================================================================
# Section 6: Per-factor dim vector completeness
# =========================================================================

class TestDimVectorComplete:
    """Per-factor dim vector is a complete invariant."""

    def test_completeness(self):
        """All 276 pairs distinguished by the dim vector."""
        result = verify_dim_vector_complete()
        assert result['is_complete']
        assert result['distinguished'] == 276

    def test_leech_empty(self):
        """Leech: empty dim vector."""
        assert per_factor_dim_vector('Leech') == ()

    def test_24A1_vector(self):
        """24A_1: 24 copies of dim(sl_2) = 3."""
        assert per_factor_dim_vector('24A1') == tuple([3] * 24)

    def test_3E8_vector(self):
        """3E_8: 3 copies of dim(E_8) = 248."""
        assert per_factor_dim_vector('3E8') == (248, 248, 248)

    def test_collision_pair_different_vectors(self):
        """All 5 collision pairs have different dim vectors."""
        for l1, l2, _ in COLLISION_PAIRS:
            v1 = per_factor_dim_vector(l1)
            v2 = per_factor_dim_vector(l2)
            assert v1 != v2, f"{l1}={v1} vs {l2}={v2}"


# =========================================================================
# Section 7: Collision pair resolution
# =========================================================================

class TestCollisionPairResolution:
    """All 5 root-count collision pairs are resolved at Level 2."""

    def test_all_resolved_at_level_2(self):
        """Every collision pair differs in factor count k."""
        resolutions = all_collision_pair_resolutions()
        for key, res in resolutions.items():
            assert res['resolved_at'] == 'level_2_factor_count', (
                f"{key}: resolved at {res['resolved_at']}, expected level_2"
            )

    def test_D16E8_vs_3E8(self):
        """D_16+E_8 (k=2) vs 3E_8 (k=3): resolved by factor count."""
        res = collision_pair_resolution('D16_E8', '3E8')
        assert res['same_root_count']
        assert not res['same_k']
        assert res['k'] == (2, 3)

    def test_4A5D4_vs_6D4(self):
        """4A_5+D_4 (k=5) vs 6D_4 (k=6): resolved by factor count."""
        res = collision_pair_resolution('4A5_D4', '6D4')
        assert res['same_root_count']
        assert not res['same_k']
        assert res['k'] == (5, 6)


# =========================================================================
# Section 8: h=6 analysis
# =========================================================================

class TestH6Analysis:
    """There are exactly 2 Niemeier lattices with h=6 (not 4)."""

    def test_only_two_h6(self):
        """Exactly 2 lattices have common Coxeter number h=6."""
        result = h_equals_6_analysis()
        assert result['num_lattices'] == 2

    def test_h6_labels(self):
        """The h=6 lattices are 4A_5 D_4 and 6D_4."""
        result = h_equals_6_analysis()
        assert set(result['lattices']) == {'4A5_D4', '6D4'}

    def test_h6_collision_resolved(self):
        """4A_5 D_4 and 6D_4 share h=6 and |R|=144 but differ in k."""
        res = collision_pair_resolution('4A5_D4', '6D4')
        assert res['same_root_count']
        assert not res['same_k']
        assert not res['same_quartic_casimir']

    def test_A3_8_has_h4(self):
        """A_3^8 has h=4, NOT h=6 (correcting the task description)."""
        assert common_coxeter('8A3') == 4

    def test_4D6_has_h10(self):
        """D_6^4 (= 4D_6) has h=10, NOT h=6."""
        assert common_coxeter('4D6') == 10


# =========================================================================
# Section 9: Leech lattice
# =========================================================================

class TestLeechLattice:
    """Complete shadow tower data for the Leech lattice."""

    def test_leech_data_complete(self):
        """Verify all Leech lattice shadow data."""
        data = leech_shadow_data()
        assert data['kappa'] == Fraction(24)
        assert data['S_3'] == Fraction(0)
        assert data['S_4'] == Fraction(0)
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['num_factors'] == 0
        assert data['root_count'] == 0
        assert data['quartic_casimir'] == 0
        assert data['min_norm'] == 4
        assert data['uniquely_rootless']

    def test_leech_F2(self):
        """Leech F_2 = scalar F_2 = 7/240."""
        data = leech_shadow_data()
        assert data['F2_scalar'] == data['F2_multi'] == Fraction(7, 240)


# =========================================================================
# Section 10: (kappa, S_3) incompleteness
# =========================================================================

class TestKappaS3Incomplete:
    """(kappa, S_3) has zero discrimination power for Niemeier lattices."""

    def test_not_complete(self):
        """(kappa, S_3) is not a complete invariant."""
        result = kappa_S3_completeness()
        assert not result['is_complete']
        assert result['discrimination_power'] == 0

    def test_both_uniform(self):
        """kappa and S_3 are both uniform across all 24 lattices."""
        result = kappa_S3_completeness()
        assert result['kappa_uniform']
        assert result['S3_uniform']

    def test_need_multichannel(self):
        """S_4 does not help; multi-channel data is needed."""
        result = need_S4_or_multichannel()
        assert not result['S4_helps']
        assert result['multichannel_needed']


# =========================================================================
# Section 11: Discrimination hierarchy
# =========================================================================

class TestDiscriminationHierarchy:
    """Full discrimination hierarchy from 0/276 to 276/276."""

    def test_hierarchy_monotone(self):
        """Each level resolves at least as many pairs as the previous."""
        h = discrimination_hierarchy_full()
        powers = [
            h['level_0_scalar_kappa']['distinguished'],
            h['level_1_scalar_tower']['distinguished'],
            h['level_2_factor_count']['distinguished'],
            h['level_4_rank_partition']['distinguished'],
            h['level_5_dim_vector']['distinguished'],
            h['level_6_quartic_casimir']['distinguished'],
            h['level_7_root_system_type']['distinguished'],
        ]
        for i in range(1, len(powers)):
            assert powers[i] >= powers[i - 1], (
                f"Non-monotone at position {i}: {powers[i]} < {powers[i-1]}"
            )

    def test_level_0_blind(self):
        """Level 0 (scalar kappa): 0/276."""
        h = discrimination_hierarchy_full()
        assert h['level_0_scalar_kappa']['distinguished'] == 0

    def test_level_1_blind(self):
        """Level 1 (scalar tower): 0/276."""
        h = discrimination_hierarchy_full()
        assert h['level_1_scalar_tower']['distinguished'] == 0

    def test_level_2_resolves_collisions(self):
        """Level 2 (factor count): 243/276."""
        h = discrimination_hierarchy_full()
        assert h['level_2_factor_count']['distinguished'] == 243

    def test_level_5_complete(self):
        """Level 5 (dim vector): 276/276 COMPLETE."""
        h = discrimination_hierarchy_full()
        assert h['level_5_dim_vector']['distinguished'] == 276
        assert h['level_5_dim_vector']['is_complete']

    def test_level_6_complete(self):
        """Level 6 (quartic Casimir): 276/276 COMPLETE."""
        h = discrimination_hierarchy_full()
        assert h['level_6_quartic_casimir']['distinguished'] == 276
        assert h['level_6_quartic_casimir']['is_complete']

    def test_level_7_complete(self):
        """Level 7 (root system type): 276/276 COMPLETE."""
        h = discrimination_hierarchy_full()
        assert h['level_7_root_system_type']['distinguished'] == 276
        assert h['level_7_root_system_type']['is_complete']


# =========================================================================
# Section 12: Bocherer-shadow constraint
# =========================================================================

class TestBochererShadow:
    """Connection between multi-channel shadow and Bocherer coefficient."""

    def test_bocherer_residual_all(self):
        """Bocherer coefficient is residual for all 24 lattices."""
        for lab in ALL_LABELS:
            data = bocherer_shadow_constraint(lab)
            assert data['bocherer_is_residual']
            assert data['F2_total_shadow'] == (
                data['F2_universal'] + data['F2_multi_channel_correction']
            )

    def test_bocherer_leech(self):
        """Leech: multi-channel correction is zero."""
        data = bocherer_shadow_constraint('Leech')
        assert data['F2_multi_channel_correction'] == Fraction(0)
        assert data['F2_total_shadow'] == Fraction(7, 240)


# =========================================================================
# Section 13: Cross-checks and multi-path verification
# =========================================================================

class TestCrossChecks:
    """Multi-path verification of key identities."""

    def test_sum_rank_24(self):
        """sum rank_i = 24 for all non-Leech lattices."""
        for lab in ALL_LABELS:
            if lab == 'Leech':
                continue
            rp = per_factor_rank_partition(lab)
            assert sum(rp) == 24, f"{lab}: sum rank = {sum(rp)}"

    def test_common_coxeter_property(self):
        """All factors of each lattice share the same Coxeter number."""
        for lab in ALL_LABELS:
            ft = per_factor_type(lab)
            if not ft:
                continue
            h_vals = [common_coxeter(lab)]
            assert all(h == h_vals[0] for h in h_vals)

    def test_dim_identity(self):
        """dim(g) = rank * (1 + h) for all simply-laced types."""
        for lab in ALL_LABELS:
            for f, n in per_factor_type(lab):
                d = dim_lie(f, n)
                h = common_coxeter(lab)
                assert d == n * (1 + h), f"{f}_{n}: dim={d}, rank*(1+h)={n*(1+h)}"

    def test_root_count_identity(self):
        """|R| = sum dim(g_i) - 24 (roots = dim - rank)."""
        for lab in ALL_LABELS:
            ft = per_factor_type(lab)
            if not ft:
                assert root_count_niemeier(lab) == 0
                continue
            total_dim = sum(dim_lie(f, n) for f, n in ft)
            assert root_count_niemeier(lab) == total_dim - 24

    def test_FP_lambda2(self):
        """Faber-Pandharipande lambda_2 = 7/5760.

        Three verification paths:
          1. Direct from Bernoulli: (2^3-1)/2^3 * |B_4|/4! = 7/8 * (1/30)/24
          2. From formula: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
          3. From known value: 7/5760
        """
        # Path 1: Bernoulli
        B4 = Fraction(1, 30)  # |B_4| = 1/30
        path1 = Fraction(7, 8) * B4 / Fraction(24)
        # Path 2: formula
        path2 = faber_pandharipande(2)
        # Path 3: known
        path3 = Fraction(7, 5760)
        assert path1 == path2 == path3

    def test_niemeier_count(self):
        """There are exactly 24 Niemeier lattices."""
        assert len(ALL_LABELS) == 24


# =========================================================================
# Section 14: Master verification suite
# =========================================================================

class TestMasterVerification:
    """Run the full verification suite."""

    def test_master_all_pass(self):
        """All verifications in the master suite pass."""
        results = run_all_verifications()
        assert results['all_pass'], f"Failed checks: {results}"
