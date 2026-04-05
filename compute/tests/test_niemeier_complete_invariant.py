r"""Tests for the complete Niemeier invariant from the MC framework.

Comprehensive test suite verifying:
  1. Each invariant level (0-6) computes correctly for all 24 lattices
  2. Discrimination power at each level (including exact collision counts)
  3. The minimal complete invariant (Level 3) is proved complete
  4. Level 3 resolves all Level 2 collisions
  5. Genus-1 theta series indistinguishability (5 collision pairs)
  6. Per-factor bar complex data is consistent
  7. Niemeier's constraint (uniform Coxeter number) holds
  8. The ADE type recovery from (rank, h) is injective
  9. Genus-2 data partially discriminates
  10. Arithmetic packet data structure
  11. Full discrimination cascade end-to-end
  12. MC framework added value (conj:arithmetic-comparison status)

Mathematical ground truth:
  - Niemeier (1968): classification by root systems, uniform Coxeter
  - Conway-Sloane, Ch. 16: the 24 lattices and their root systems
  - arithmetic_shadows.tex: depth decomposition, packet connection
  - conj:arithmetic-comparison status for lattice VOAs
"""

import pytest
from fractions import Fraction

from compute.lib.niemeier_complete_invariant import (
    ALL_NIEMEIER_LABELS,
    KAPPA_NIEMEIER,
    NIEMEIER_REGISTRY,
    bar_complex_factor_data,
    discrimination_matrix,
    discrimination_power,
    full_discrimination_cascade,
    genus1_collision_pairs,
    level0_kappa,
    level1_shadow_tower,
    level2_per_factor_kappa,
    level3_coxeter_rank_partition,
    level3_rank_coxeter,
    level4_root_system,
    level5_theta_invariants,
    level5b_genus2_data,
    level6_arithmetic_packet,
    mc_framework_added_value,
    minimal_complete_invariant,
    prove_genus1_incomplete,
    verify_completeness,
    verify_level3_resolves_all_level2_collisions,
)
from compute.lib.niemeier_shadow_atlas import (
    coxeter_number,
    root_count,
    root_lattice_det,
    theta_coefficient,
)


# =========================================================================
# Section 1: Level 0 — Scalar kappa
# =========================================================================

class TestLevel0Kappa:
    """Level 0: kappa = 24 for all 24 Niemeier lattices."""

    def test_kappa_24_for_all(self):
        for label in ALL_NIEMEIER_LABELS:
            assert level0_kappa(label) == 24, f"{label}: kappa != 24"

    def test_kappa_undiscriminating(self):
        """kappa cannot distinguish ANY pair."""
        dp = discrimination_power(level0_kappa)
        assert dp['distinguished_pairs'] == 0
        assert dp['is_complete'] is False
        assert dp['num_distinct_values'] == 1


# =========================================================================
# Section 2: Level 1 — Full scalar shadow tower
# =========================================================================

class TestLevel1ShadowTower:
    """Level 1: shadow tower (all class G, S_r = 0 for r >= 3)."""

    def test_identical_for_all(self):
        ref = level1_shadow_tower('Leech')
        for label in ALL_NIEMEIER_LABELS:
            assert level1_shadow_tower(label) == ref, f"{label} differs"

    def test_shadow_starts_with_kappa(self):
        for label in ALL_NIEMEIER_LABELS:
            tower = level1_shadow_tower(label)
            assert tower[0] == 24

    def test_higher_shadows_zero(self):
        for label in ALL_NIEMEIER_LABELS:
            tower = level1_shadow_tower(label, max_r=20)
            for r in range(1, len(tower)):
                assert tower[r] == 0, f"{label}: S_{r+2} != 0"

    def test_undiscriminating(self):
        dp = discrimination_power(level1_shadow_tower)
        assert dp['is_complete'] is False
        assert dp['num_distinct_values'] == 1


# =========================================================================
# Section 3: Level 2 — Per-factor kappa vector
# =========================================================================

class TestLevel2PerFactorKappa:
    """Level 2: sorted per-factor kappa vector."""

    def test_leech_empty(self):
        assert level2_per_factor_kappa('Leech') == ()

    def test_sum_is_24(self):
        """Per-factor kappa sums to 24 for non-Leech."""
        for label in ALL_NIEMEIER_LABELS:
            kv = level2_per_factor_kappa(label)
            if label != 'Leech':
                assert sum(kv) == 24, f"{label}: sum != 24"

    def test_sorted_descending(self):
        for label in ALL_NIEMEIER_LABELS:
            kv = level2_per_factor_kappa(label)
            for i in range(len(kv) - 1):
                assert kv[i] >= kv[i + 1], f"{label}: not sorted"

    def test_known_examples(self):
        assert level2_per_factor_kappa('D24') == (24,)
        assert level2_per_factor_kappa('3E8') == (8, 8, 8)
        assert level2_per_factor_kappa('24A1') == tuple([1] * 24)
        assert level2_per_factor_kappa('D16_E8') == (16, 8)

    def test_has_5_collision_groups(self):
        """Level 2 has exactly 5 collision groups."""
        dp = discrimination_power(level2_per_factor_kappa)
        assert dp['num_collision_groups'] == 5

    def test_incomplete(self):
        dp = discrimination_power(level2_per_factor_kappa)
        assert dp['is_complete'] is False

    def test_specific_collisions(self):
        """Verify the 5 known collision groups at Level 2."""
        # (24,): A24 and D24 both have single rank-24 factor
        assert level2_per_factor_kappa('A24') == level2_per_factor_kappa('D24')
        # (12,12): 2A12 and 2D12
        assert level2_per_factor_kappa('2A12') == level2_per_factor_kappa('2D12')
        # (8,8,8): 3A8, 3D8, 3E8
        assert level2_per_factor_kappa('3A8') == level2_per_factor_kappa('3D8')
        assert level2_per_factor_kappa('3D8') == level2_per_factor_kappa('3E8')
        # (6,6,6,6): 4A6, 4D6, 4E6
        assert level2_per_factor_kappa('4A6') == level2_per_factor_kappa('4D6')
        assert level2_per_factor_kappa('4D6') == level2_per_factor_kappa('4E6')
        # (4,4,4,4,4,4): 6A4, 6D4
        assert level2_per_factor_kappa('6A4') == level2_per_factor_kappa('6D4')


# =========================================================================
# Section 4: Level 3 — Minimal complete invariant
# =========================================================================

class TestLevel3MinimalComplete:
    """Level 3: sorted per-factor (rank, Coxeter) — COMPLETE."""

    def test_complete(self):
        """THE MAIN THEOREM: Level 3 distinguishes all 24 lattices."""
        dp = discrimination_power(level3_rank_coxeter)
        assert dp['is_complete'] is True
        assert dp['num_distinct_values'] == 24
        assert dp['distinguished_pairs'] == 24 * 23 // 2

    def test_verify_completeness(self):
        result = verify_completeness()
        assert result['is_complete'] is True
        assert result['num_distinct'] == 24
        assert len(result['collisions']) == 0

    def test_resolves_all_level2_collisions(self):
        result = verify_level3_resolves_all_level2_collisions()
        assert result['all_resolved'] is True
        assert result['num_level2_collisions'] == 5

    def test_leech_unique(self):
        assert level3_rank_coxeter('Leech') == ()

    def test_known_values(self):
        # D24: single factor with rank 24, h = 2*(24-1) = 46
        assert level3_rank_coxeter('D24') == ((24, 46),)
        # A24: single factor with rank 24, h = 24+1 = 25
        assert level3_rank_coxeter('A24') == ((24, 25),)
        # These DIFFER (resolved collision)
        assert level3_rank_coxeter('D24') != level3_rank_coxeter('A24')

    def test_3e8_vs_3d8_vs_3a8(self):
        """The triple collision (8,8,8) is resolved by Coxeter numbers."""
        l3_3e8 = level3_rank_coxeter('3E8')
        l3_3d8 = level3_rank_coxeter('3D8')
        l3_3a8 = level3_rank_coxeter('3A8')
        # E8: h=30, D8: h=14, A8: h=9
        assert l3_3e8 == ((8, 30), (8, 30), (8, 30))
        assert l3_3d8 == ((8, 14), (8, 14), (8, 14))
        assert l3_3a8 == ((8, 9), (8, 9), (8, 9))
        assert l3_3e8 != l3_3d8
        assert l3_3d8 != l3_3a8
        assert l3_3e8 != l3_3a8

    def test_4x6_triple_collision(self):
        """4A6 vs 4D6 vs 4E6: resolved by Coxeter."""
        l3_4a6 = level3_rank_coxeter('4A6')
        l3_4d6 = level3_rank_coxeter('4D6')
        l3_4e6 = level3_rank_coxeter('4E6')
        # A6: h=7, D6: h=10, E6: h=12
        assert l3_4a6 == ((6, 7),) * 4
        assert l3_4d6 == ((6, 10),) * 4
        assert l3_4e6 == ((6, 12),) * 4
        assert len({l3_4a6, l3_4d6, l3_4e6}) == 3

    def test_6a4_vs_6d4(self):
        """6A4 vs 6D4: resolved by Coxeter."""
        # A4: h=5, D4: h=6
        assert level3_rank_coxeter('6A4') == ((4, 5),) * 6
        assert level3_rank_coxeter('6D4') == ((4, 6),) * 6
        assert level3_rank_coxeter('6A4') != level3_rank_coxeter('6D4')

    def test_2a12_vs_2d12(self):
        """2A12 vs 2D12: resolved by Coxeter."""
        # A12: h=13, D12: h=22
        assert level3_rank_coxeter('2A12') == ((12, 13), (12, 13))
        assert level3_rank_coxeter('2D12') == ((12, 22), (12, 22))
        assert level3_rank_coxeter('2A12') != level3_rank_coxeter('2D12')


class TestLevel3CoxeterRankPartition:
    """Alternative Level 3 encoding: (h, rank_partition)."""

    def test_complete(self):
        vals = set()
        for label in ALL_NIEMEIER_LABELS:
            vals.add(level3_coxeter_rank_partition(label))
        assert len(vals) == 24

    def test_uniform_coxeter(self):
        """Niemeier's constraint: all factors have the same h."""
        for label in ALL_NIEMEIER_LABELS:
            h, part = level3_coxeter_rank_partition(label)
            if label == 'Leech':
                assert h is None
                assert part == ()
            else:
                assert h is not None
                assert h > 0

    def test_partition_sums_to_24(self):
        for label in ALL_NIEMEIER_LABELS:
            h, part = level3_coxeter_rank_partition(label)
            if label != 'Leech':
                assert sum(part) == 24

    def test_equals_minimal_complete(self):
        """The two Level 3 encodings agree."""
        for label in ALL_NIEMEIER_LABELS:
            assert level3_coxeter_rank_partition(label) == minimal_complete_invariant(label)


# =========================================================================
# Section 5: Level 4 — Root system type
# =========================================================================

class TestLevel4RootSystem:
    """Level 4: root system type (trivially complete)."""

    def test_complete(self):
        dp = discrimination_power(level4_root_system)
        assert dp['is_complete'] is True
        assert dp['num_distinct_values'] == 24

    def test_leech_empty(self):
        assert level4_root_system('Leech') == ()

    def test_known_root_systems(self):
        assert level4_root_system('3E8') == (('E', 8), ('E', 8), ('E', 8))
        assert level4_root_system('D16_E8') == (('D', 16), ('E', 8))
        assert level4_root_system('A11_D7_E6') == (('A', 11), ('D', 7), ('E', 6))


# =========================================================================
# Section 6: Genus-1 theta series indistinguishability
# =========================================================================

class TestGenus1Incomplete:
    """Prove genus-1 theta series cannot distinguish all 24."""

    def test_exactly_5_collision_pairs(self):
        pairs = genus1_collision_pairs()
        assert len(pairs) == 5

    def test_collision_pair_identities(self):
        """Each collision pair has IDENTICAL theta series (exact)."""
        result = prove_genus1_incomplete(max_n=20)
        assert result['num_collision_pairs'] == 5
        assert result['all_exactly_identical'] is True
        for pair_data in result['pairs']:
            assert pair_data['is_exactly_identical'] is True

    def test_known_collision_pairs(self):
        """Verify the 5 specific collision pairs."""
        pairs = genus1_collision_pairs()
        pair_sets = {frozenset(p[:2]) for p in pairs}
        expected = {
            frozenset({'D16_E8', '3E8'}),
            frozenset({'A17_E7', 'D10_2E7'}),
            frozenset({'A11_D7_E6', '4E6'}),
            frozenset({'2A9_D6', '4D6'}),
            frozenset({'4A5_D4', '6D4'}),
        }
        assert pair_sets == expected

    def test_collision_root_counts(self):
        """Verify collision pairs share the correct root counts."""
        pairs = genus1_collision_pairs()
        root_counts = {frozenset(p[:2]): p[2] for p in pairs}
        assert root_counts[frozenset({'D16_E8', '3E8'})] == 720
        assert root_counts[frozenset({'A17_E7', 'D10_2E7'})] == 432
        assert root_counts[frozenset({'A11_D7_E6', '4E6'})] == 288
        assert root_counts[frozenset({'2A9_D6', '4D6'})] == 240
        assert root_counts[frozenset({'4A5_D4', '6D4'})] == 144

    def test_theta_coefficients_identical_highorder(self):
        """Verify theta identity to n=30 for D16+E8 vs 3E8."""
        for n in range(31):
            assert theta_coefficient('D16_E8', n) == theta_coefficient('3E8', n), (
                f"Differ at n={n}"
            )

    def test_genus1_discrimination_power(self):
        """Genus-1 theta distinguishes 19 lattices, not 24."""
        def _root_key(label):
            return NIEMEIER_REGISTRY[label]['num_roots']
        dp = discrimination_power(_root_key)
        assert dp['num_distinct_values'] == 19
        assert dp['is_complete'] is False


# =========================================================================
# Section 7: Genus-2 data
# =========================================================================

class TestGenus2Data:
    """Level 5b: genus-2 representation numbers."""

    def test_leech_zero(self):
        data = level5b_genus2_data('Leech')
        assert data['genus2_diag11'] == 0

    def test_distinguishes_a17e7_from_d10_2e7(self):
        """Genus-2 diag(1,1) resolves the |R|=432 collision."""
        d1 = level5b_genus2_data('A17_E7')
        d2 = level5b_genus2_data('D10_2E7')
        assert d1['genus2_diag11'] != d2['genus2_diag11']

    def test_does_not_resolve_all(self):
        """Genus-2 diag(1,1) alone does NOT resolve all collisions."""
        dp = discrimination_power(
            lambda lab: level5b_genus2_data(lab)['genus2_diag11']
        )
        # It's better than genus-1 but still incomplete
        assert dp['is_complete'] is False


# =========================================================================
# Section 8: Arithmetic packet data
# =========================================================================

class TestLevel6ArithmeticPacket:
    """Level 6: arithmetic packet connection data."""

    def test_module_rank_2(self):
        """S_{12}(SL(2,Z)) = C*Delta, so module rank = 2."""
        for label in ALL_NIEMEIER_LABELS:
            data = level6_arithmetic_packet(label)
            assert data['module_rank'] == 2
            assert data['cusp_dim'] == 1

    def test_nilpotent_zero(self):
        """Lattice VOA packets are diagonal (all N_chi = 0)."""
        for label in ALL_NIEMEIER_LABELS:
            data = level6_arithmetic_packet(label)
            assert data['nilpotent_parts_zero'] is True

    def test_d_alg_zero(self):
        """Lattice VOAs have d_alg = 0."""
        for label in ALL_NIEMEIER_LABELS:
            data = level6_arithmetic_packet(label)
            assert data['d_alg'] == 0

    def test_c_delta_depends_only_on_roots(self):
        """c_Delta is the same for lattices with the same |R|."""
        pairs = genus1_collision_pairs()
        for lab1, lab2, _ in pairs:
            d1 = level6_arithmetic_packet(lab1)
            d2 = level6_arithmetic_packet(lab2)
            assert d1['c_delta'] == d2['c_delta']


# =========================================================================
# Section 9: Bar complex factor data
# =========================================================================

class TestBarComplexFactorData:
    """Per-factor bar complex decomposition."""

    def test_total_kappa_24(self):
        for label in ALL_NIEMEIER_LABELS:
            data = bar_complex_factor_data(label)
            assert data['total_kappa'] == 24

    def test_leech_no_factors(self):
        data = bar_complex_factor_data('Leech')
        assert data['is_leech'] is True
        assert data['num_factors'] == 0

    def test_uniform_coxeter(self):
        """Niemeier constraint: all factors share the same h."""
        for label in ALL_NIEMEIER_LABELS:
            data = bar_complex_factor_data(label)
            if not data['is_leech']:
                assert data['uniform_coxeter'] is True

    def test_known_factor_counts(self):
        assert bar_complex_factor_data('3E8')['num_factors'] == 3
        assert bar_complex_factor_data('D24')['num_factors'] == 1
        assert bar_complex_factor_data('24A1')['num_factors'] == 24
        assert bar_complex_factor_data('A11_D7_E6')['num_factors'] == 3

    def test_3e8_factor_details(self):
        data = bar_complex_factor_data('3E8')
        for factor in data['factors']:
            assert factor['family'] == 'E'
            assert factor['rank'] == 8
            assert factor['roots'] == 240
            assert factor['coxeter'] == 30
            assert factor['det_cartan'] == 1

    def test_d16_e8_factor_details(self):
        data = bar_complex_factor_data('D16_E8')
        families = sorted([f['family'] for f in data['factors']])
        assert families == ['D', 'E']
        for f in data['factors']:
            if f['family'] == 'D':
                assert f['rank'] == 16
                assert f['coxeter'] == 30
            elif f['family'] == 'E':
                assert f['rank'] == 8
                assert f['coxeter'] == 30


# =========================================================================
# Section 10: ADE type recovery
# =========================================================================

class TestADETypeRecovery:
    """Verify that (rank, Coxeter) determines ADE type uniquely."""

    def test_a_type_recovery(self):
        """A_n: rank=n, h=n+1."""
        for n in range(1, 25):
            h = n + 1
            assert coxeter_number('A', n) == h

    def test_d_type_recovery(self):
        """D_n: rank=n, h=2(n-1)."""
        for n in range(3, 25):
            h = 2 * (n - 1)
            assert coxeter_number('D', n) == h

    def test_e_type_recovery(self):
        """E_6: (6,12), E_7: (7,18), E_8: (8,30)."""
        assert coxeter_number('E', 6) == 12
        assert coxeter_number('E', 7) == 18
        assert coxeter_number('E', 8) == 30

    def test_no_ade_collisions_rank_le_24(self):
        """No two DISTINCT ADE types with rank <= 24 share (rank, h).

        The only exception is (A_3, D_3) at (rank=3, h=4), which is a
        genuine isomorphism: D_3 = A_3 as Lie algebras (sl_4 = so_6).
        Niemeier lattices use D_n only for n >= 4, so this does not
        affect the classification.
        """
        pairs = set()
        for n in range(1, 25):
            pairs.add(('A', n, n + 1))
        for n in range(4, 25):  # D_n for n >= 4 only (D_3 = A_3)
            pairs.add(('D', n, 2 * (n - 1)))
        for n in [6, 7, 8]:
            pairs.add(('E', n, coxeter_number('E', n)))

        # Extract (rank, h) and check no collisions
        rh_to_types = {}
        for family, rank, h in pairs:
            key = (rank, h)
            if key not in rh_to_types:
                rh_to_types[key] = []
            rh_to_types[key].append(f'{family}_{rank}')
        for key, types in rh_to_types.items():
            assert len(types) == 1, f"Collision at {key}: {types}"


# =========================================================================
# Section 11: Discrimination matrix
# =========================================================================

class TestDiscriminationMatrix:
    """Verify discrimination matrices are correct."""

    def test_level3_full_discrimination(self):
        labels, matrix = discrimination_matrix(level3_rank_coxeter)
        n = len(labels)
        assert n == 24
        for i in range(n):
            for j in range(n):
                if i == j:
                    assert matrix[i][j] is True
                else:
                    assert matrix[i][j] is True, (
                        f"Level 3 fails to distinguish {labels[i]} and {labels[j]}"
                    )

    def test_level0_no_discrimination(self):
        labels, matrix = discrimination_matrix(level0_kappa)
        n = len(labels)
        for i in range(n):
            for j in range(n):
                if i == j:
                    assert matrix[i][j] is True
                else:
                    assert matrix[i][j] is False

    def test_level2_partial_discrimination(self):
        labels, matrix = discrimination_matrix(level2_per_factor_kappa)
        n = len(labels)
        # Count undistinguished off-diagonal pairs
        undist = sum(1 for i in range(n) for j in range(i + 1, n)
                     if not matrix[i][j])
        # 5 collision groups: sizes 2,2,2,3,3 => C(2,2)*3 + C(3,2)*2 = 3+6 = 9
        # Actually: (24,) x2, (12,12) x2, (8,8,8) x3, (6,6,6,6) x3, (4,4,4,4,4,4) x2
        # => C(2,2)*3 + C(3,2)*2 = 3 + 6 = 9
        # Wait: sizes are 2, 2, 3, 3, 2 => 1+1+3+3+1 = 9
        assert undist == 9


# =========================================================================
# Section 12: Full discrimination cascade
# =========================================================================

class TestFullCascade:
    """End-to-end test of the full discrimination cascade."""

    def test_cascade_structure(self):
        result = full_discrimination_cascade()
        assert 'levels' in result
        assert 'summary' in result
        levels = result['levels']
        assert 'level0_kappa' in levels
        assert 'level1_shadow_tower' in levels
        assert 'level2_per_factor_kappa' in levels
        assert 'level3_rank_coxeter' in levels
        assert 'level4_root_system' in levels
        assert 'level5_genus1_theta' in levels
        assert 'level5b_genus2_diag11' in levels

    def test_monotone_discrimination(self):
        """Higher levels distinguish at least as many pairs as lower levels."""
        result = full_discrimination_cascade()
        levels = result['levels']
        # Level 0 <= Level 1 (both 0)
        assert levels['level0_kappa']['distinguished_pairs'] <= \
               levels['level2_per_factor_kappa']['distinguished_pairs']
        # Level 2 < Level 3 (strictly)
        assert levels['level2_per_factor_kappa']['distinguished_pairs'] < \
               levels['level3_rank_coxeter']['distinguished_pairs']
        # Level 3 == Level 4 (both complete)
        assert levels['level3_rank_coxeter']['distinguished_pairs'] == \
               levels['level4_root_system']['distinguished_pairs']

    def test_level3_is_first_complete(self):
        result = full_discrimination_cascade()
        levels = result['levels']
        assert levels['level0_kappa']['is_complete'] is False
        assert levels['level1_shadow_tower']['is_complete'] is False
        assert levels['level2_per_factor_kappa']['is_complete'] is False
        assert levels['level3_rank_coxeter']['is_complete'] is True

    def test_genus1_weaker_than_level2(self):
        """Genus-1 theta (19 values) vs per-factor kappa (19 values)."""
        result = full_discrimination_cascade()
        levels = result['levels']
        # Both have 19 distinct values but genus-1 collisions != level-2 collisions
        assert levels['level5_genus1_theta']['is_complete'] is False

    def test_total_pairs_276(self):
        """C(24,2) = 276 total pairs."""
        result = full_discrimination_cascade()
        for level_data in result['levels'].values():
            assert level_data['total_pairs'] == 276


# =========================================================================
# Section 13: MC framework added value
# =========================================================================

class TestMCFrameworkAddedValue:
    """Verify the synthesis of what MC adds beyond Conway-Sloane."""

    def test_added_value_structure(self):
        av = mc_framework_added_value()
        assert 'functorial_packaging' in av
        assert 'arithmetic_extension' in av
        assert 'genus_tower' in av
        assert 'universality' in av
        assert 'conj_arithmetic_comparison_status' in av

    def test_conj_status_for_niemeier(self):
        """conj:arithmetic-comparison parts (i)-(iii) status."""
        av = mc_framework_added_value()
        status = av['conj_arithmetic_comparison_status']
        # Part (i) holds classically
        assert 'holds' in status.lower() or 'classical' in status.lower()
        # Part (iii) requires genus-2
        assert 'genus-2' in status.lower() or 'genus 2' in status.lower()


# =========================================================================
# Section 14: Cross-checks and mathematical consistency
# =========================================================================

class TestMathematicalConsistency:
    """Mathematical cross-checks."""

    def test_coxeter_numbers_correct_A(self):
        """h(A_n) = n + 1."""
        for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 17, 24]:
            assert coxeter_number('A', n) == n + 1

    def test_coxeter_numbers_correct_D(self):
        """h(D_n) = 2(n-1)."""
        for n in [4, 5, 6, 7, 8, 9, 10, 12, 16, 24]:
            assert coxeter_number('D', n) == 2 * (n - 1)

    def test_root_counts_correct(self):
        """Verify root counts: A_n: n(n+1), D_n: 2n(n-1)."""
        assert root_count('A', 1) == 2
        assert root_count('A', 2) == 6
        assert root_count('A', 24) == 600
        assert root_count('D', 4) == 24
        assert root_count('D', 8) == 112
        assert root_count('E', 8) == 240

    def test_root_lattice_det_correct(self):
        """det(Cartan): A_n: n+1, D_n: 4, E_6: 3, E_7: 2, E_8: 1."""
        assert root_lattice_det('A', 1) == 2
        assert root_lattice_det('A', 24) == 25
        assert root_lattice_det('D', 4) == 4
        assert root_lattice_det('D', 24) == 4
        assert root_lattice_det('E', 6) == 3
        assert root_lattice_det('E', 7) == 2
        assert root_lattice_det('E', 8) == 1

    def test_24_lattices_present(self):
        assert len(ALL_NIEMEIER_LABELS) == 24

    def test_niemeier_constraint_h_uniform(self):
        """All factors of each Niemeier root system have the same h."""
        for label in ALL_NIEMEIER_LABELS:
            h_vals = NIEMEIER_REGISTRY[label]['coxeter_numbers']
            if h_vals:
                assert all(h == h_vals[0] for h in h_vals), (
                    f"{label}: non-uniform h = {h_vals}"
                )


# =========================================================================
# Section 15: Edge cases and error handling
# =========================================================================

class TestEdgeCases:
    """Edge cases and error handling."""

    def test_unknown_label_raises(self):
        with pytest.raises(ValueError):
            level2_per_factor_kappa('NonexistentLattice')
        with pytest.raises(ValueError):
            level3_rank_coxeter('NonexistentLattice')
        with pytest.raises(ValueError):
            bar_complex_factor_data('NonexistentLattice')

    def test_leech_special_in_all_levels(self):
        """Leech lattice is unique at every level."""
        assert level0_kappa('Leech') == 24
        assert level1_shadow_tower('Leech') == (24,) + (0,) * 8
        assert level2_per_factor_kappa('Leech') == ()
        assert level3_rank_coxeter('Leech') == ()
        assert level4_root_system('Leech') == ()

    def test_d24_largest_root_count(self):
        """D24 has the most roots: 2*24*23 = 1104."""
        max_roots = max(NIEMEIER_REGISTRY[lab]['num_roots']
                        for lab in ALL_NIEMEIER_LABELS)
        assert max_roots == 1104
        assert NIEMEIER_REGISTRY['D24']['num_roots'] == 1104

    def test_leech_fewest_roots(self):
        """Leech has 0 roots."""
        min_roots = min(NIEMEIER_REGISTRY[lab]['num_roots']
                        for lab in ALL_NIEMEIER_LABELS)
        assert min_roots == 0
        assert NIEMEIER_REGISTRY['Leech']['num_roots'] == 0


# =========================================================================
# Section 16: Summary statistics
# =========================================================================

class TestSummaryStatistics:
    """Summary statistics for the discrimination hierarchy."""

    def test_distinct_root_counts(self):
        """There are exactly 19 distinct root counts among the 24."""
        root_counts = set(NIEMEIER_REGISTRY[lab]['num_roots']
                          for lab in ALL_NIEMEIER_LABELS)
        assert len(root_counts) == 19

    def test_distinct_coxeter_numbers(self):
        """Count distinct Coxeter numbers across the 24 lattices."""
        h_values = set()
        for label in ALL_NIEMEIER_LABELS:
            h_vals = NIEMEIER_REGISTRY[label]['coxeter_numbers']
            if h_vals:
                h_values.add(h_vals[0])
        # h ranges from 2 (A1) to 46 (D24), plus Leech (no h)
        assert 2 in h_values
        assert 46 in h_values
        assert 30 in h_values  # E8 and D16 both have h=30

    def test_level2_collision_sizes(self):
        """Level 2 collision groups have sizes 2, 2, 2, 3, 3."""
        dp = discrimination_power(level2_per_factor_kappa)
        sizes = sorted([len(v) for v in dp['collision_groups'].values()])
        assert sizes == [2, 2, 2, 3, 3]

    def test_undistinguished_pairs_level2(self):
        """Level 2: C(2,2)*3 + C(3,2)*2 = 3 + 6 = 9 undistinguished pairs."""
        dp = discrimination_power(level2_per_factor_kappa)
        total = dp['total_pairs']
        dist = dp['distinguished_pairs']
        assert total - dist == 9
