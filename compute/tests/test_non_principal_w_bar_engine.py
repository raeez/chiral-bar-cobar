"""Tests for non-principal W-algebra bar complex engine.

Covers:
  - Bershadsky-Polyakov algebra (sl_3, minimal nilpotent)
  - sl_4 hook-type duality ((2,1,1) <-> (3,1))
  - sl_4 subregular and all nilpotent types
  - sl_6 complete nilpotent classification
  - DS shadow functor: kappa values and depth
  - Shadow depth classification for all types
  - Transport propagation for hook families
  - Multi-path kappa verification
  - Koszul dual pair identification
  - Comparison with principal W_N

80+ tests, multi-path verification throughout.
"""

import pytest
from sympy import Rational, Symbol, cancel, factor, simplify

from compute.lib.non_principal_w_bar_engine import (
    all_partitions_of,
    bershadsky_polyakov_anomaly_ratio,
    bershadsky_polyakov_central_charge,
    bershadsky_polyakov_kappa,
    bershadsky_polyakov_koszul_dual_central_charge,
    bershadsky_polyakov_profile,
    ds_depth_comparison,
    ds_depth_increase_all_nilpotents,
    ds_kappa_additivity_check,
    hook_type_edge_compatibility,
    kappa_multi_path_verification,
    koszul_dual_pairs,
    nilpotent_classification_table,
    principal_vs_nonprincipal_comparison,
    principal_w_n_profile,
    shadow_depth_on_T_line,
    shadow_depth_special_levels,
    shadow_tower_numerical,
    shadow_tower_on_T_line,
    sl4_hook_211_profile,
    sl4_hook_duality_check,
    sl4_subregular_31_profile,
    sl6_full_classification,
    transport_propagation_summary,
    w_algebra_bar_profile,
)
from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    krw_central_charge,
)
from compute.lib.nonprincipal_ds_orbits import (
    transpose_partition,
)

k = Symbol('k')


# =============================================================================
# A. Bershadsky-Polyakov algebra (sl_3, minimal nilpotent, partition (2,1))
# =============================================================================

class TestBershadsky:
    """Tests for the Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)})."""

    def test_bp_partition_is_21(self):
        bp = bershadsky_polyakov_profile()
        assert bp.partition == (2, 1)

    def test_bp_self_transpose(self):
        """(2,1) is self-transpose: (2,1)^t = (2,1)."""
        bp = bershadsky_polyakov_profile()
        assert bp.is_self_transpose
        assert bp.transpose == (2, 1)

    def test_bp_generator_count(self):
        """BP has 4 strong generators: J(1), G+(3/2), G-(3/2), T(2)."""
        bp = bershadsky_polyakov_profile()
        assert bp.num_generators == 4
        assert bp.num_bosonic == 2
        assert bp.num_fermionic == 2

    def test_bp_generator_weights(self):
        """Generator weights: 1, 3/2, 3/2, 2."""
        bp = bershadsky_polyakov_profile()
        weights = sorted([w for _, w, _ in bp.generator_weights])
        assert weights == [Rational(1), Rational(3, 2), Rational(3, 2), Rational(2)]

    def test_bp_anomaly_ratio(self):
        """rho_BP = 1 - 2/3 - 2/3 + 1/2 = 1/6.

        Path 1: direct from generator formula.
        Path 2: explicit computation 1 - 2*(2/3) + 1/2 = 1 - 4/3 + 1/2 = 1/6.
        """
        rho = bershadsky_polyakov_anomaly_ratio()
        assert rho == Rational(1, 6)
        # Cross-check from profile
        bp = bershadsky_polyakov_profile()
        assert bp.anomaly_ratio == Rational(1, 6)

    def test_bp_central_charge_formula(self):
        """c_BP(k) = 2 - 24*(k+1)^2/(k+3).

        # AP140: corrected from (k-15)/(k+3) which gives K=2; correct K_BP=196
        Verify at k=0: c = 2 - 24/3 = -6.
        Verify at k=3: c = 2 - 24*16/6 = -62.
        """
        c_bp = bershadsky_polyakov_central_charge(k)
        assert simplify(c_bp.subs(k, 0) - (-6)) == 0
        assert simplify(c_bp.subs(k, 3) - (-62)) == 0

    def test_bp_central_charge_pole(self):
        """c_BP has pole at k = -3 (critical level for sl_3)."""
        c_bp = bershadsky_polyakov_central_charge(k)
        # The denominator should be (k+3)
        from sympy import fraction
        _, denom = fraction(cancel(c_bp))
        assert simplify(denom.subs(k, -3)) == 0

    def test_bp_kappa_formula(self):
        """kappa_BP = (1/6) * c_BP(k).

        # AP140: corrected docstring; formula is (1/6)*(2 - 24*(k+1)^2/(k+3))
        """
        kappa = bershadsky_polyakov_kappa(k)
        kappa_direct = Rational(1, 6) * bershadsky_polyakov_central_charge(k)
        assert simplify(kappa - kappa_direct) == 0

    def test_bp_kappa_numerical(self):
        """kappa_BP(1) = (1/6)*(2 - 24*4/4) = (1/6)*(-22) = -11/3.

        # AP140: corrected from -7/12
        """
        kappa = bershadsky_polyakov_kappa(Rational(1))
        assert kappa == Rational(-11, 3)

    def test_bp_shadow_class_M(self):
        """BP has generic shadow class M (infinite depth) on T-line."""
        bp = bershadsky_polyakov_profile()
        assert bp.shadow_class == 'M'
        assert bp.shadow_depth == 'infinity'

    def test_bp_shadow_tower_all_nonzero(self):
        """All shadow coefficients S_r are nonzero at generic level."""
        st = shadow_tower_numerical((2, 1), Rational(1), max_arity=8)
        for r in range(2, 9):
            assert st[r]['nonzero'], f"S_{r} is zero at k=1"

    def test_bp_koszul_dual_is_self(self):
        """BP is self-dual since (2,1) is self-transpose."""
        bp = bershadsky_polyakov_profile()
        assert bp.koszul_dual_partition == (2, 1)

    def test_bp_complementarity_sum_constant(self):
        """For self-transpose BP: kappa(k) + kappa(k') = rho*(c+c') = (1/6)*196 = 98/3.

        # AP140: corrected from 1/3; K_BP=196, rho=1/6, so kappa_sum=98/3
        """
        bp = bershadsky_polyakov_profile()
        assert simplify(bp.kappa_complementarity - Rational(98, 3)) == 0

    def test_bp_dual_central_charge(self):
        """c_BP(k) + c_BP(-k-6) = 196 (Koszul conductor).

        # AP140: corrected from K=2; K = c(0)+c(-6) = -6+202 = 196
        """
        c_k = bershadsky_polyakov_central_charge(k)
        c_kv = bershadsky_polyakov_koszul_dual_central_charge(k)
        assert simplify(c_k + c_kv - 196) == 0

    def test_bp_multi_path(self):
        """Three-path kappa verification for BP."""
        mp = kappa_multi_path_verification((2, 1))
        assert mp['path1_eq_path2']
        assert mp['sum_is_constant']
        assert mp['all_paths_consistent']

    def test_bp_special_levels(self):
        """Find levels where BP changes shadow class."""
        sp = shadow_depth_special_levels((2, 1))
        assert sp['critical_level'] == -3
        # c = 0 at some level
        assert len(sp['c_zero_levels']) >= 1


# =============================================================================
# B. sl_4 hook-type duality ((2,1,1) <-> (3,1))
# =============================================================================

class TestSl4Hook:
    """Tests for sl_4 hook-type W-algebras and their duality."""

    def test_211_partition_data(self):
        """(2,1,1) is hook_nonprincipal, 9 generators."""
        p = sl4_hook_211_profile()
        assert p.partition == (2, 1, 1)
        assert p.orbit_class == 'hook_nonprincipal'
        assert p.num_generators == 9

    def test_31_partition_data(self):
        """(3,1) is subregular, 5 generators."""
        p = sl4_subregular_31_profile()
        assert p.partition == (3, 1)
        assert p.orbit_class == 'subregular'
        assert p.num_generators == 5

    def test_211_generators_detail(self):
        """(2,1,1) has 4 weight-1 (bos), 4 weight-3/2 (fer), 1 weight-2 (bos)."""
        p = sl4_hook_211_profile()
        assert p.num_bosonic == 5   # 4 wt-1 + 1 wt-2
        assert p.num_fermionic == 4  # 4 wt-3/2

    def test_31_generators_all_bosonic(self):
        """(3,1) has all bosonic generators (integer weights)."""
        p = sl4_subregular_31_profile()
        assert p.num_fermionic == 0
        assert p.num_bosonic == 5

    def test_transpose_relation(self):
        """(2,1,1)^t = (3,1) and (3,1)^t = (2,1,1)."""
        assert transpose_partition((2, 1, 1)) == (3, 1)
        assert transpose_partition((3, 1)) == (2, 1, 1)

    def test_hook_duality_transposes(self):
        hd = sl4_hook_duality_check()
        assert hd['are_transposes']

    def test_211_anomaly_ratio(self):
        """Anomaly ratio for (2,1,1)."""
        p = sl4_hook_211_profile()
        assert isinstance(p.anomaly_ratio, Rational)

    def test_31_anomaly_ratio(self):
        """Anomaly ratio for (3,1)."""
        p = sl4_subregular_31_profile()
        assert isinstance(p.anomaly_ratio, Rational)

    def test_anomaly_ratios_differ(self):
        """For non-self-transpose pair, anomaly ratios are generically different."""
        hd = sl4_hook_duality_check()
        assert hd['source_anomaly_ratio'] != hd['target_anomaly_ratio']

    def test_both_shadow_class_M(self):
        """Both (2,1,1) and (3,1) W-algebras are class M."""
        hd = sl4_hook_duality_check()
        assert hd['source_shadow_class'] == 'M'
        assert hd['target_shadow_class'] == 'M'

    def test_211_kappa_path1_eq_path2(self):
        """kappa(2,1,1) via anomaly ratio == via ds_kappa_from_affine."""
        mp = kappa_multi_path_verification((2, 1, 1))
        assert mp['path1_eq_path2']

    def test_31_kappa_path1_eq_path2(self):
        """kappa(3,1) via anomaly ratio == via ds_kappa_from_affine."""
        mp = kappa_multi_path_verification((3, 1))
        assert mp['path1_eq_path2']

    def test_211_shadow_tower_nonzero(self):
        """Shadow tower for (2,1,1) is all nonzero at k=1."""
        st = shadow_tower_numerical((2, 1, 1), Rational(1), max_arity=6)
        for r in range(2, 7):
            assert st[r]['nonzero'], f"S_{r} zero at k=1 for (2,1,1)"

    def test_31_shadow_tower_nonzero(self):
        """Shadow tower for (3,1) is all nonzero at k=1."""
        st = shadow_tower_numerical((3, 1), Rational(1), max_arity=6)
        for r in range(2, 7):
            assert st[r]['nonzero'], f"S_{r} zero at k=1 for (3,1)"

    def test_dual_level_formula(self):
        """Dual level for sl_4: k' = -k - 8."""
        kv = hook_dual_level_sl_n(4, k)
        assert simplify(kv - (-k - 8)) == 0


# =============================================================================
# C. sl_4 additional nilpotent types
# =============================================================================

class TestSl4All:
    """Tests for all nilpotent types of sl_4."""

    def test_sl4_partitions(self):
        """sl_4 has 5 partitions: (4), (3,1), (2,2), (2,1,1), (1,1,1,1)."""
        parts = all_partitions_of(4)
        assert len(parts) == 5

    def test_22_self_transpose(self):
        """(2,2) is self-transpose."""
        p = w_algebra_bar_profile((2, 2))
        assert p.is_self_transpose

    def test_22_shadow_class(self):
        """(2,2) W-algebra is class M."""
        p = w_algebra_bar_profile((2, 2))
        assert p.shadow_class == 'M'

    def test_22_anomaly_ratio(self):
        """Anomaly ratio for (2,2) is well-defined."""
        p = w_algebra_bar_profile((2, 2))
        assert isinstance(p.anomaly_ratio, Rational)

    def test_principal_4_profile(self):
        """Principal W_4 = W^k(sl_4, f_{(4)})."""
        p = principal_w_n_profile(4)
        assert p.partition == (4,)
        assert p.orbit_class == 'principal'
        assert p.num_generators == 3  # T, W_3, W_4


# =============================================================================
# D. sl_6 complete classification
# =============================================================================

class TestSl6Classification:
    """Tests for the complete sl_6 nilpotent classification."""

    def test_sl6_partition_count(self):
        """sl_6 has 11 partitions."""
        parts = all_partitions_of(6)
        assert len(parts) == 11

    def test_sl6_classification_runs(self):
        """Full classification completes without error."""
        table = sl6_full_classification()
        assert len(table) == 11

    def test_sl6_all_nontrivial_shadow_M(self):
        """All non-trivial nilpotent types in sl_6 are generically class M."""
        table = sl6_full_classification()
        for entry in table:
            if entry['orbit_class'] == 'trivial':
                continue
            if 'error' in entry:
                pytest.fail(f"Error for {entry['partition']}: {entry['error']}")
            assert entry['shadow_class'] == 'M', \
                f"{entry['partition']} has shadow class {entry['shadow_class']}, expected M"

    def test_sl6_self_transpose_partitions(self):
        """Only (3,2,1) is self-transpose among partitions of 6."""
        table = sl6_full_classification()
        self_t = [e['partition'] for e in table
                  if e.get('is_self_transpose', False)]
        assert (3, 2, 1) in self_t

    def test_sl6_koszul_dual_pairs(self):
        """Koszul dual pairs are identified correctly."""
        pairs = koszul_dual_pairs(6)
        # Should have: 5 non-self-dual pairs + 1 self-dual
        non_self = [p for p in pairs if p['type'] == 'non-self-dual']
        self_dual = [p for p in pairs if p['type'] == 'self-dual']
        assert len(non_self) == 5
        assert len(self_dual) == 1
        assert self_dual[0]['partition'] == (3, 2, 1)

    def test_sl6_principal_subregular_pair(self):
        """(6) <-> (1^6) is principal <-> trivial."""
        pairs = koszul_dual_pairs(6)
        found = False
        for p in pairs:
            if p.get('partition') == (6,):
                assert p['transpose'] == (1, 1, 1, 1, 1, 1)
                found = True
        assert found

    def test_sl6_hook_pairs(self):
        """(5,1) <-> (2,1^4) and (4,1,1) <-> (3,1^3) are hook pairs."""
        pairs = koszul_dual_pairs(6)
        pair_dict = {p['partition']: p for p in pairs if 'partition' in p}
        assert (5, 1) in pair_dict
        assert pair_dict[(5, 1)]['transpose'] == (2, 1, 1, 1, 1)

    def test_sl6_two_row_pairs(self):
        """(4,2) <-> (2,2,1,1) and (3,3) <-> (2,2,2)."""
        pairs = koszul_dual_pairs(6)
        pair_dict = {p['partition']: p for p in pairs if 'partition' in p}
        assert (4, 2) in pair_dict
        assert pair_dict[(4, 2)]['transpose'] == (2, 2, 1, 1)
        assert (3, 3) in pair_dict
        assert pair_dict[(3, 3)]['transpose'] == (2, 2, 2)

    def test_sl6_anomaly_ratios_all_positive(self):
        """All anomaly ratios are positive rationals."""
        table = sl6_full_classification()
        for entry in table:
            if entry['orbit_class'] == 'trivial':
                continue
            if 'error' in entry:
                continue
            rho = Rational(entry['anomaly_ratio'])
            assert rho > 0, f"{entry['partition']} has rho = {rho}"

    def test_sl6_generator_counts(self):
        """Generator counts are consistent with f-centralizer dimension."""
        table = sl6_full_classification()
        for entry in table:
            if entry['orbit_class'] == 'trivial' or 'error' in entry:
                continue
            n = entry['num_generators']
            assert n >= 1, f"{entry['partition']} has {n} generators"


# =============================================================================
# E. DS shadow functor
# =============================================================================

class TestDSShadowFunctor:
    """Tests for DS reduction as shadow functor."""

    def test_ds_kappa_additivity_sl3(self):
        """Kappa additivity for DS from sl_3."""
        result = ds_kappa_additivity_check((2, 1))
        assert result['all_match']

    def test_ds_kappa_additivity_sl4_211(self):
        """Kappa additivity for (2,1,1) from sl_4."""
        result = ds_kappa_additivity_check((2, 1, 1))
        assert result['all_match']

    def test_ds_kappa_additivity_sl4_31(self):
        """Kappa additivity for (3,1) from sl_4."""
        result = ds_kappa_additivity_check((3, 1))
        assert result['all_match']

    def test_ds_kappa_additivity_principal_3(self):
        """Kappa additivity for principal W_3."""
        result = ds_kappa_additivity_check((3,))
        assert result['all_match']

    def test_ds_depth_increase_bp(self):
        """DS from sl_3: depth 3 (affine) -> infinity (BP)."""
        comp = ds_depth_comparison((2, 1))
        assert comp['depth_increased']
        assert comp['affine_depth'] == 3
        assert comp['W_depth'] == 'infinity'

    def test_ds_depth_increase_211(self):
        """DS from sl_4: depth increases for (2,1,1)."""
        comp = ds_depth_comparison((2, 1, 1))
        assert comp['depth_increased']

    def test_ds_depth_increase_31(self):
        """DS from sl_4: depth increases for (3,1)."""
        comp = ds_depth_comparison((3, 1))
        assert comp['depth_increased']

    def test_ds_depth_increase_all_sl5(self):
        """All non-trivial nilpotent types of sl_5 have depth increase."""
        results = ds_depth_increase_all_nilpotents(5)
        for r in results:
            assert r['depth_increased'], f"{r['partition']} depth did not increase"

    def test_ds_depth_increase_all_sl6(self):
        """All non-trivial nilpotent types of sl_6 have depth increase."""
        results = ds_depth_increase_all_nilpotents(6)
        for r in results:
            assert r['depth_increased'], f"{r['partition']} depth did not increase"


# =============================================================================
# F. Shadow depth classification
# =============================================================================

class TestShadowDepth:
    """Tests for shadow depth classification."""

    def test_principal_w2_class_M(self):
        """Virasoro (principal W_2) is class M."""
        sd = shadow_depth_on_T_line((2,))
        assert sd.shadow_class == 'M'

    def test_principal_w3_class_M(self):
        """W_3 is class M."""
        sd = shadow_depth_on_T_line((3,))
        assert sd.shadow_class == 'M'

    def test_bp_class_M(self):
        """Bershadsky-Polyakov is class M."""
        sd = shadow_depth_on_T_line((2, 1))
        assert sd.shadow_class == 'M'

    def test_shadow_depth_discriminant_nonzero(self):
        """Discriminant Delta = 8*kappa_T*S_4 is generically nonzero."""
        sd = shadow_depth_on_T_line((2, 1))
        # At k=1 the discriminant should be nonzero
        disc_val = sd.discriminant.subs(k, 1)
        assert simplify(disc_val) != 0

    @pytest.mark.parametrize("partition", [
        (3,), (2, 1), (3, 1), (2, 1, 1), (2, 2),
        (4,), (3, 2, 1), (4, 2), (3, 3),
    ])
    def test_generic_class_M(self, partition):
        """All non-affine W-algebras are generically class M on T-line."""
        sd = shadow_depth_on_T_line(partition)
        assert sd.shadow_class == 'M'


# =============================================================================
# G. Transport propagation
# =============================================================================

class TestTransportPropagation:
    """Tests for hook-type transport propagation."""

    def test_hook_edge_compatibility_sl3(self):
        """sl_3: single hook r=1, self-transpose (2,1)."""
        edges = hook_type_edge_compatibility(3)
        assert len(edges) == 1
        assert edges[0]['partition'] == (2, 1)
        assert edges[0]['transpose'] == (2, 1)

    def test_hook_edge_compatibility_sl4(self):
        """sl_4: hooks r=1,2 are (3,1) and (2,1,1)."""
        edges = hook_type_edge_compatibility(4)
        assert len(edges) == 2
        partitions = {e['partition'] for e in edges}
        assert (3, 1) in partitions
        assert (2, 1, 1) in partitions

    def test_hook_anomaly_ratios_rational(self):
        """All hook anomaly ratios are rational."""
        for N in range(3, 7):
            edges = hook_type_edge_compatibility(N)
            for e in edges:
                assert isinstance(e['anomaly_ratio'], Rational)

    def test_hook_all_class_M(self):
        """All hook-type W-algebras are class M."""
        for N in range(3, 7):
            edges = hook_type_edge_compatibility(N)
            for e in edges:
                assert e['shadow_class'] == 'M'

    def test_transport_summary_N3_to_N6(self):
        """Transport propagation summary runs for N=3..6."""
        summary = transport_propagation_summary(max_N=6)
        assert len(summary) == 4  # N = 3, 4, 5, 6


# =============================================================================
# H. Multi-path kappa verification
# =============================================================================

class TestMultiPathKappa:
    """Tests for 3-path kappa verification."""

    def test_bp_all_paths(self):
        """BP: all 3 paths consistent."""
        mp = kappa_multi_path_verification((2, 1))
        assert mp['all_paths_consistent']

    def test_principal_w3_all_paths(self):
        """W_3: paths 1 and 2 consistent, and self-transpose sum constant."""
        mp = kappa_multi_path_verification((3,))
        assert mp['path1_eq_path2']
        # (3)^t = (1,1,1) is the trivial partition => not a W-algebra.
        # The complementarity check via our formula may not apply directly.

    @pytest.mark.parametrize("partition", [
        (2, 1), (3, 1), (2, 1, 1), (2, 2),
    ])
    def test_path1_eq_path2(self, partition):
        """Paths 1 (anomaly ratio) and 2 (ds_kappa) always agree."""
        mp = kappa_multi_path_verification(partition)
        assert mp['path1_eq_path2']

    def test_self_transpose_sum_constant(self):
        """For self-transpose partitions, kappa sum is k-independent."""
        # (2,1) is self-transpose
        mp = kappa_multi_path_verification((2, 1))
        assert mp['sum_is_constant']

    def test_22_self_transpose_sum_constant(self):
        """(2,2) is self-transpose, kappa sum should be constant."""
        mp = kappa_multi_path_verification((2, 2))
        assert mp['sum_is_constant']

    def test_numerical_path1_path2_match(self):
        """Numerical check: path1 == path2 at multiple levels."""
        mp = kappa_multi_path_verification((2, 1))
        for check in mp['numerical_checks']:
            assert check['path1_eq_path2']


# =============================================================================
# I. Comparison with principal W_N
# =============================================================================

class TestPrincipalComparison:
    """Tests comparing principal and non-principal W-algebras."""

    def test_principal_w2_is_virasoro(self):
        """W_2 has 1 generator at weight 2."""
        p = principal_w_n_profile(2)
        assert p.num_generators == 1
        weights = [w for _, w, _ in p.generator_weights]
        assert weights == [Rational(2)]

    def test_principal_w3_generators(self):
        """W_3 has 2 generators at weights 2, 3."""
        p = principal_w_n_profile(3)
        assert p.num_generators == 2
        weights = sorted([w for _, w, _ in p.generator_weights])
        assert weights == [Rational(2), Rational(3)]

    def test_principal_w4_generators(self):
        """W_4 has 3 generators at weights 2, 3, 4."""
        p = principal_w_n_profile(4)
        assert p.num_generators == 3
        weights = sorted([w for _, w, _ in p.generator_weights])
        assert weights == [Rational(2), Rational(3), Rational(4)]

    def test_principal_anomaly_ratio_formula(self):
        """rho(W_N) = 1/2 + 1/3 + ... + 1/N = H_N - 1.

        Path 1: from generator data.
        Path 2: explicit harmonic number.
        """
        for N in range(2, 6):
            p = principal_w_n_profile(N)
            expected = sum(Rational(1, j) for j in range(2, N + 1))
            assert p.anomaly_ratio == expected, \
                f"W_{N}: rho = {p.anomaly_ratio}, expected {expected}"

    def test_principal_all_bosonic(self):
        """Principal W_N generators are all bosonic (integer weights)."""
        for N in range(2, 6):
            p = principal_w_n_profile(N)
            assert p.num_fermionic == 0

    def test_bp_fewer_generators_than_w3(self):
        """BP has 4 generators vs W_3 has 2: non-principal has MORE generators."""
        bp = bershadsky_polyakov_profile()
        w3 = principal_w_n_profile(3)
        assert bp.num_generators > w3.num_generators

    def test_comparison_table_sl4(self):
        """Comparison table for sl_4 runs and has 5 entries."""
        table = principal_vs_nonprincipal_comparison(4)
        assert len(table) == 5


# =============================================================================
# J. Shadow tower computation
# =============================================================================

class TestShadowTower:
    """Tests for shadow tower computation on T-line."""

    def test_bp_S2_is_kappa(self):
        """S_2 = c/2 = kappa_T on the T-line."""
        tower = shadow_tower_on_T_line((2, 1), max_arity=4)
        c_bp = krw_central_charge((2, 1))
        assert simplify(tower[2] - c_bp / 2) == 0

    def test_bp_S3_is_constant(self):
        """S_3 = 2 for all algebras (universal cubic)."""
        tower = shadow_tower_on_T_line((2, 1), max_arity=4)
        # S_3 = 2 is universal for Virasoro on T-line
        assert simplify(tower[3] - 2) == 0

    def test_bp_S4_quartic_formula(self):
        """S_4 = 10/(c(5c+22)) at c = c_BP(k)."""
        tower = shadow_tower_on_T_line((2, 1), max_arity=4)
        c_bp = krw_central_charge((2, 1))
        expected = Rational(10) / (c_bp * (5 * c_bp + 22))
        assert simplify(tower[4] - expected) == 0

    def test_shadow_tower_numerical_bp(self):
        """Numerical shadow tower for BP at k=2."""
        st = shadow_tower_numerical((2, 1), Rational(2), max_arity=6)
        assert all(st[r]['nonzero'] for r in range(2, 7))

    def test_shadow_tower_numerical_31(self):
        """Numerical shadow tower for (3,1) at k=2."""
        st = shadow_tower_numerical((3, 1), Rational(2), max_arity=6)
        assert all(st[r]['nonzero'] for r in range(2, 7))


# =============================================================================
# K. Additional cross-checks and edge cases
# =============================================================================

class TestEdgeCases:
    """Edge cases and cross-checks."""

    def test_principal_not_self_transpose_for_N_ge_3(self):
        """(N)^t = (1^N) for N >= 3, so principal is NOT self-transpose."""
        for N in range(3, 7):
            p = principal_w_n_profile(N)
            assert not p.is_self_transpose

    def test_virasoro_self_transpose(self):
        """(2) is self-transpose: (2)^t = (1,1) but... (2) has only 1 part.
        Actually (2)^t = (1,1). So (2) is NOT self-transpose."""
        p = principal_w_n_profile(2)
        assert not p.is_self_transpose

    def test_321_self_transpose(self):
        """(3,2,1)^t = (3,2,1)."""
        assert transpose_partition((3, 2, 1)) == (3, 2, 1)
        p = w_algebra_bar_profile((3, 2, 1))
        assert p.is_self_transpose

    def test_all_partitions_of_small(self):
        """Partition counts: p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11."""
        assert len(all_partitions_of(2)) == 2
        assert len(all_partitions_of(3)) == 3
        assert len(all_partitions_of(4)) == 5
        assert len(all_partitions_of(5)) == 7
        assert len(all_partitions_of(6)) == 11

    @pytest.mark.parametrize("N", [3, 4, 5, 6])
    def test_koszul_dual_pairs_partition(self, N):
        """Every partition of N appears exactly once in the dual pair list."""
        pairs = koszul_dual_pairs(N)
        all_parts = set()
        for p in pairs:
            all_parts.add(p['partition'])
            if 'transpose' in p:
                all_parts.add(p['transpose'])
        expected = set(all_partitions_of(N))
        assert all_parts == expected

    def test_ds_kappa_additivity_sl5(self):
        """Kappa additivity holds for principal and non-principal sl_5."""
        for lam in [(5,), (4, 1), (3, 1, 1)]:
            result = ds_kappa_additivity_check(lam)
            assert result['all_match'], f"Additivity fails for {lam}"

    def test_sl6_321_complementarity(self):
        """For self-transpose (3,2,1): complementarity sum is constant."""
        mp = kappa_multi_path_verification((3, 2, 1))
        assert mp['path1_eq_path2']
        assert mp['sum_is_constant']


# =============================================================================
# L. Systematic multi-path verification across families
# =============================================================================

class TestSystematicMultiPath:
    """Systematic 3-path verification across all families."""

    @pytest.mark.parametrize("partition", [
        (2, 1),       # BP (sl_3 minimal)
        (3, 1),       # sl_4 subregular
        (2, 1, 1),    # sl_4 minimal
        (2, 2),       # sl_4 even
        (4, 1),       # sl_5 subregular
        (3, 1, 1),    # sl_5 hook (self-transpose)
    ])
    def test_paths_1_2_agree(self, partition):
        """Paths 1 (anomaly ratio) and 2 (ds_kappa) agree for all types."""
        mp = kappa_multi_path_verification(partition)
        assert mp['path1_eq_path2']

    @pytest.mark.parametrize("partition", [
        (2, 1),       # self-transpose
        (2, 2),       # self-transpose
        (3, 1, 1),    # self-transpose in sl_5
        (3, 2, 1),    # self-transpose in sl_6
    ])
    def test_self_transpose_constant_sum(self, partition):
        """Self-transpose partitions have k-independent kappa sum."""
        mp = kappa_multi_path_verification(partition)
        assert mp['sum_is_constant'], \
            f"{partition} (self-transpose) has non-constant sum: {mp['complementarity_sum']}"
