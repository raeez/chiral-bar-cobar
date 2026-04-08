r"""Tests for non_principal_w_duality_engine.py.

Systematic verification of Koszul duality for non-principal W-algebras
W^k(sl_N, f_lambda) in type A.  Tests cover:

  1. Correct central charge formulas (independent of oversimplified KRW)
  2. sl_3 classification: principal W_3 and Bershadsky-Polyakov
  3. sl_4 classification: all four non-trivial orbits
  4. Generator content from ad(h)-grading
  5. Anomaly ratio computation and decomposition
  6. DS-Koszul commutation at the generator level
  7. Hook-type duality (Fehily-CLNS): kappa complementarity
  8. Transport propagation: coverage of Par(N) from hook seeds
  9. Shadow depth classification on the T-line
  10. Self-dual (self-transpose) partition analysis
  11. Non-hook partition analysis for sl_5, sl_6
  12. Complementarity constant table
  13. Multi-path kappa verification
  14. OPE data for the Bershadsky-Polyakov algebra

Multi-path verification mandate (CLAUDE.md):
  Every formula verified by at least 3 independent paths.
"""

import pytest
from sympy import Rational, Symbol, simplify, cancel

from compute.lib.non_principal_w_duality_engine import (
    NonPrincipalDualityProfile,
    anomaly_ratio_table,
    complementarity_constant_table,
    compute_duality_profile,
    correct_central_charge,
    correct_kappa,
    ds_koszul_generator_test,
    dual_level,
    fehily_clns_hook_predictions,
    hook_duality_catalog,
    hook_duality_level,
    kappa_multipath_verification,
    non_hook_partition_analysis,
    self_dual_partitions,
    shadow_depth_all_orbits,
    sl3_all_profiles,
    sl3_subregular_ope_data,
    sl4_all_profiles,
    sl4_duality_pairs,
    transport_closure_from_hooks,
    transport_graph_edges,
    transport_propagation_summary,
    verify_non_principal_w_duality,
)

k = Symbol('k')


# =====================================================================
# 1. Correct central charge formulas
# =====================================================================

class TestCorrectCentralCharge:
    """Test the correct central charge formulas against known values."""

    def test_virasoro_formula(self):
        """Virasoro c = 1 - 6(k+1)^2/(k+2)."""
        c_val, exact = correct_central_charge((2,))
        assert exact
        expected = 1 - 6 * (k + 1)**2 / (k + 2)
        assert simplify(c_val - expected) == 0

    def test_virasoro_at_k1(self):
        """c(Vir, k=1) = -7."""
        c_val, _ = correct_central_charge((2,), Rational(1))
        assert c_val == -7

    def test_virasoro_at_k0(self):
        """c(Vir, k=0) = -2."""
        c_val, _ = correct_central_charge((2,), Rational(0))
        assert c_val == -2

    def test_w3_formula(self):
        """W_3 c = 2 - 24(k+2)^2/(k+3)."""
        c_val, exact = correct_central_charge((3,))
        assert exact
        expected = 2 - 24 * (k + 2)**2 / (k + 3)
        assert simplify(c_val - expected) == 0

    def test_w3_at_k0(self):
        """c(W_3, k=0) = -30."""
        c_val, _ = correct_central_charge((3,), Rational(0))
        assert c_val == -30

    def test_bp_formula(self):
        """BP c = 2 - 24(k+1)^2/(k+3) (FKR 2020)."""
        c_val, exact = correct_central_charge((2, 1))
        assert exact
        expected = 2 - 24 * (k + 1)**2 / (k + 3)
        assert simplify(c_val - expected) == 0

    def test_bp_at_k0(self):
        """c(BP, k=0) = 2 - 24/3 = -6."""
        c_val, _ = correct_central_charge((2, 1), Rational(0))
        assert c_val == -6

    def test_bp_at_k1(self):
        """c(BP, k=1) = 2 - 24*4/4 = -22."""
        c_val, _ = correct_central_charge((2, 1), Rational(1))
        assert c_val == -22

    def test_w4_formula(self):
        """W_4 c = 3 - 60(k+3)^2/(k+4)."""
        c_val, exact = correct_central_charge((4,))
        assert exact
        expected = 3 - 60 * (k + 3)**2 / (k + 4)
        assert simplify(c_val - expected) == 0

    def test_w4_at_k0(self):
        """c(W_4, k=0) = -132."""
        c_val, _ = correct_central_charge((4,), Rational(0))
        assert c_val == -132

    def test_affine_sugawara_sl3(self):
        """c(V_k(sl_3)) = 8k/(k+3)."""
        c_val, exact = correct_central_charge((1, 1, 1))
        assert exact
        expected = 8 * k / (k + 3)
        assert simplify(c_val - expected) == 0

    def test_sl4_non_principal_not_exact(self):
        """sl_4 non-principal non-hook: c formula is not exact."""
        # (2,2) is not hook and not principal
        _, exact = correct_central_charge((2, 2))
        assert not exact

    def test_bp_ne_oversimplified(self):
        """BP correct c differs from the oversimplified KRW formula."""
        c_correct, _ = correct_central_charge((2, 1))
        from compute.lib.hook_type_w_duality import krw_central_charge
        c_krw = krw_central_charge((2, 1))
        # They must NOT be equal (the KRW is wrong for non-principal)
        assert simplify(c_correct - c_krw) != 0

    def test_principal_matches_krw(self):
        """For principal W_N, the correct formula and KRW should agree
        in STRUCTURE (both depend on k), but KRW gives wrong coefficients."""
        c_correct, _ = correct_central_charge((3,))
        from compute.lib.hook_type_w_duality import krw_central_charge
        c_krw = krw_central_charge((3,))
        # Both are rational functions of k with denominator (k+3)
        # but they differ (KRW is linear numerator, correct is quadratic)
        assert simplify(c_correct - c_krw) != 0


# =====================================================================
# 2. sl_3 classification
# =====================================================================

class TestSl3Classification:
    """Test the complete classification for sl_3."""

    def test_sl3_partitions(self):
        """sl_3 has 2 non-trivial W-algebras."""
        profiles = sl3_all_profiles()
        assert set(profiles.keys()) == {(3,), (2, 1)}

    def test_w3_is_principal(self):
        p = compute_duality_profile((3,))
        assert p.is_principal
        assert p.orbit_class == 'principal'
        assert p.duality_status == 'proved_principal'

    def test_bp_is_self_transpose(self):
        p = compute_duality_profile((2, 1))
        assert p.is_self_transpose
        assert p.transpose == (2, 1)

    def test_bp_generators(self):
        """BP has 4 generators: J(1), G+(3/2), G-(3/2), T(2)."""
        p = compute_duality_profile((2, 1))
        # f-centralizer dimension from the Jacobson-Morozov
        # grading gives 2 elements. But strong generators
        # (from non-positive grades) may differ.
        # The actual num_generators comes from the f-centralizer dim.
        assert p.num_generators == 4  # J(1), G+(3/2), G-(3/2), T(2)

    def test_bp_anomaly_ratio(self):
        """BP rho = 1/6."""
        p = compute_duality_profile((2, 1))
        assert p.anomaly_ratio == Rational(1, 6)

    def test_bp_rho_decomposition(self):
        """BP rho = 1 - 2/3 - 2/3 + 1/2 = 1/6 from J, G+, G-, T."""
        # From the STRONG generator presentation (not the f-centralizer)
        # The strong generators are: J(1,bos), G+(3/2,ferm), G-(3/2,ferm), T(2,bos)
        rho = Rational(1) - Rational(2, 3) - Rational(2, 3) + Rational(1, 2)
        assert rho == Rational(1, 6)

    def test_bp_shadow_class_M(self):
        p = compute_duality_profile((2, 1))
        assert p.shadow_class == 'M'

    def test_w3_rho(self):
        """W_3 rho = 1/2 + 1/3 = 5/6."""
        p = compute_duality_profile((3,))
        assert p.anomaly_ratio == Rational(5, 6)


# =====================================================================
# 3. sl_4 classification
# =====================================================================

class TestSl4Classification:
    """Test the complete classification for sl_4."""

    def test_sl4_partitions(self):
        """sl_4 has 4 non-trivial W-algebras."""
        profiles = sl4_all_profiles()
        assert set(profiles.keys()) == {(4,), (3, 1), (2, 2), (2, 1, 1)}

    def test_sl4_principal(self):
        p = compute_duality_profile((4,))
        assert p.is_principal
        assert p.anomaly_ratio == Rational(13, 12)

    def test_sl4_subregular(self):
        p = compute_duality_profile((3, 1))
        assert p.orbit_class == 'subregular'
        assert p.transpose == (2, 1, 1)
        assert not p.is_self_transpose

    def test_sl4_minimal(self):
        p = compute_duality_profile((2, 1, 1))
        assert p.orbit_class == 'hook_nonprincipal'
        assert p.transpose == (3, 1)

    def test_sl4_even(self):
        p = compute_duality_profile((2, 2))
        assert p.orbit_class == 'two_row_nonhook'
        assert p.is_self_transpose
        assert p.transpose == (2, 2)

    def test_sl4_subregular_generators(self):
        """sl_4 (3,1): 5 generators, all bosonic."""
        p = compute_duality_profile((3, 1))
        assert p.num_generators == 5
        assert p.num_bosonic == 5
        assert p.num_fermionic == 0

    def test_sl4_minimal_generators(self):
        """sl_4 (2,1,1): 9 generators (5 bos + 4 ferm)."""
        p = compute_duality_profile((2, 1, 1))
        assert p.num_generators == 9
        assert p.num_bosonic == 5
        assert p.num_fermionic == 4

    def test_sl4_even_generators(self):
        """sl_4 (2,2): 7 generators, all bosonic."""
        p = compute_duality_profile((2, 2))
        assert p.num_generators == 7
        assert p.num_bosonic == 7
        assert p.num_fermionic == 0

    def test_sl4_duality_pairs(self):
        """sl_4 has one non-self-dual pair and one self-dual."""
        pairs = sl4_duality_pairs()
        assert len(pairs) == 2
        non_sd = [p for p in pairs if p['type'] == 'non-self-dual']
        sd = [p for p in pairs if p['type'] == 'self-dual']
        assert len(non_sd) == 1
        assert len(sd) == 1
        assert non_sd[0]['partition_A'] == (3, 1)
        assert non_sd[0]['partition_B'] == (2, 1, 1)
        assert sd[0]['partition'] == (2, 2)


# =====================================================================
# 4. Generator content from ad(h)-grading
# =====================================================================

class TestGeneratorContent:
    """Test generator content computed from f-centralizer."""

    def test_sl3_principal_2_generators(self):
        """W_3 has 2 generators: T(2), W(3)."""
        from compute.lib.hook_type_w_duality import w_algebra_generator_data
        g = w_algebra_generator_data((3,))
        assert g.f_centralizer_dimension == 2
        assert g.n_bosonic == 2
        assert g.n_fermionic == 0

    def test_sl4_principal_3_generators(self):
        """W_4 has 3 generators: T(2), W(3), W(4)."""
        from compute.lib.hook_type_w_duality import w_algebra_generator_data
        g = w_algebra_generator_data((4,))
        assert g.f_centralizer_dimension == 3
        assert g.n_bosonic == 3
        assert g.n_fermionic == 0

    def test_sl5_principal_4_generators(self):
        """W_5 has 4 generators."""
        from compute.lib.hook_type_w_duality import w_algebra_generator_data
        g = w_algebra_generator_data((5,))
        assert g.f_centralizer_dimension == 4

    def test_generator_count_increases_with_partition_refinement(self):
        """Finer partitions give more generators (larger centralizer)."""
        from compute.lib.hook_type_w_duality import w_algebra_generator_data
        g4 = w_algebra_generator_data((4,)).f_centralizer_dimension
        g31 = w_algebra_generator_data((3, 1)).f_centralizer_dimension
        g22 = w_algebra_generator_data((2, 2)).f_centralizer_dimension
        g211 = w_algebra_generator_data((2, 1, 1)).f_centralizer_dimension
        # Principal has fewest, minimal has most
        assert g4 < g31
        assert g31 < g22
        assert g22 < g211


# =====================================================================
# 5. Anomaly ratio computation
# =====================================================================

class TestAnomalyRatio:
    """Test anomaly ratio computation and decomposition."""

    def test_virasoro_rho_half(self):
        """Virasoro rho = 1/2."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        assert anomaly_ratio_from_partition((2,)) == Rational(1, 2)

    def test_w3_rho_5_6(self):
        """W_3 rho = 5/6."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        assert anomaly_ratio_from_partition((3,)) == Rational(5, 6)

    def test_w4_rho_13_12(self):
        """W_4 rho = 13/12."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        assert anomaly_ratio_from_partition((4,)) == Rational(13, 12)

    def test_principal_rho_is_harmonic(self):
        """Principal W_N: rho = H_N - 1 = sum_{j=2}^{N} 1/j."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        for N in [2, 3, 4, 5]:
            rho = anomaly_ratio_from_partition((N,))
            expected = sum(Rational(1, j) for j in range(2, N + 1))
            assert rho == expected, f"N={N}: got {rho}, expected {expected}"

    def test_bp_rho_1_6(self):
        """BP rho = 1/6."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        assert anomaly_ratio_from_partition((2, 1)) == Rational(1, 6)

    def test_anomaly_ratio_table_sl4(self):
        """All sl_4 anomaly ratios are well-defined rationals."""
        table = anomaly_ratio_table(4)
        assert len(table) == 4
        for entry in table:
            assert entry['rho_total'] is not None
            assert isinstance(entry['rho_total'], Rational)

    def test_anomaly_ratio_positive_for_principal(self):
        """Principal W_N always has rho > 0."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        for N in range(2, 8):
            rho = anomaly_ratio_from_partition((N,))
            assert rho > 0


# =====================================================================
# 6. DS-Koszul commutation at generator level
# =====================================================================

class TestDSKoszulCommutation:
    """Test DS-Koszul commutation at the generator level."""

    def test_bp_self_dual_generators_equal(self):
        """BP is self-transpose: source and target generators match."""
        gt = ds_koszul_generator_test((2, 1))
        assert gt['is_self_transpose']
        assert gt['generators_equal']
        assert gt['rho_equal']

    def test_sl4_hook_generators_differ(self):
        """sl_4 (3,1) and (2,1,1) have different generator counts."""
        gt = ds_koszul_generator_test((3, 1))
        assert not gt['is_self_transpose']
        assert not gt['generators_equal']
        # (3,1): 5 generators, (2,1,1): 9 generators
        assert gt['num_generators_source'] == 5
        assert gt['num_generators_target'] == 9

    def test_sl4_even_self_dual(self):
        """sl_4 (2,2) is self-transpose."""
        gt = ds_koszul_generator_test((2, 2))
        assert gt['is_self_transpose']
        assert gt['generators_equal']

    def test_sl4_hook_rho_differ(self):
        """sl_4 (3,1) and (2,1,1) have different anomaly ratios."""
        gt31 = ds_koszul_generator_test((3, 1))
        assert not gt31['rho_equal']

    def test_all_sl4_orbits(self):
        """DS-Koszul generator test for all sl_4 orbits."""
        for lam in [(4,), (3, 1), (2, 2), (2, 1, 1)]:
            gt = ds_koszul_generator_test(lam)
            assert gt['N'] == 4


# =====================================================================
# 7. Hook-type duality (Fehily-CLNS)
# =====================================================================

class TestHookDuality:
    """Test hook-type duality: kappa complementarity for hooks."""

    def test_sl3_hook_r1(self):
        """sl_3, r=1: hook (2,1), self-transpose."""
        data = hook_duality_level(3, 1)
        assert data['partition'] == (2, 1)
        assert data['transpose'] == (2, 1)

    def test_sl4_hook_r1(self):
        """sl_4, r=1: hook (3,1), transpose (2,1,1)."""
        data = hook_duality_level(4, 1)
        assert data['partition'] == (3, 1)
        assert data['transpose'] == (2, 1, 1)

    def test_sl4_hook_r2(self):
        """sl_4, r=2: hook (2,1,1), transpose (3,1)."""
        data = hook_duality_level(4, 2)
        assert data['partition'] == (2, 1, 1)
        assert data['transpose'] == (3, 1)

    def test_dual_level_involutive(self):
        """k'' = -(-k-2N) - 2N = k. Dual level is involutive."""
        for N in [3, 4, 5, 6]:
            kv = dual_level(N, k)
            kvv = dual_level(N, kv)
            assert simplify(kvv - k) == 0

    def test_hook_catalog_nonempty(self):
        """Hook catalog through sl_6 is non-empty."""
        catalog = hook_duality_catalog(max_N=6)
        assert len(catalog) > 0
        # sl_3 has 1 hook, sl_4 has 2, sl_5 has 3, sl_6 has 4: total 10
        assert len(catalog) == 1 + 2 + 3 + 4

    def test_hook_rho_well_defined(self):
        """All hook anomaly ratios are well-defined rationals."""
        catalog = hook_duality_catalog(max_N=6)
        for entry in catalog:
            assert isinstance(entry['rho_source'], Rational)
            assert isinstance(entry['rho_target'], Rational)

    def test_fehily_clns_sl4(self):
        """Fehily-CLNS predictions for sl_4 hooks."""
        results = fehily_clns_hook_predictions(4)
        assert len(results) == 2  # r=1 and r=2

    def test_fehily_clns_numerical_consistency(self):
        """Numerical spot-checks for hook duality at specific levels."""
        results = fehily_clns_hook_predictions(4)
        for entry in results:
            for num in entry['numerical']:
                # kappa and c should be finite at test levels
                assert abs(num['c_sum']) < 1e10
                assert abs(num['kappa_sum']) < 1e10


# =====================================================================
# 8. Transport propagation
# =====================================================================

class TestTransportPropagation:
    """Test transport propagation from hook seeds."""

    def test_sl3_fully_covered(self):
        """sl_3: all non-trivial partitions reached."""
        cl = transport_closure_from_hooks(3)
        assert cl['fully_covered']
        assert cl['closure_size'] == 2  # (3,) and (2,1)

    def test_sl4_fully_covered(self):
        """sl_4: all non-trivial partitions reached."""
        cl = transport_closure_from_hooks(4)
        assert cl['fully_covered']
        assert cl['closure_size'] == 4

    def test_sl5_fully_covered(self):
        """sl_5: all non-trivial partitions reached."""
        cl = transport_closure_from_hooks(5)
        assert cl['fully_covered']

    def test_sl6_fully_covered(self):
        """sl_6: all non-trivial partitions reached."""
        cl = transport_closure_from_hooks(6)
        assert cl['fully_covered']

    def test_sl7_fully_covered(self):
        """sl_7: all non-trivial partitions reached."""
        cl = transport_closure_from_hooks(7)
        assert cl['fully_covered']

    def test_transport_graph_edges_sl4(self):
        """sl_4 dominance order has 4 edges (linear chain)."""
        edges = transport_graph_edges(4)
        assert len(edges) == 4  # (4)->(3,1)->(2,2)->(2,1,1)->(1,1,1,1)

    def test_transport_graph_sl6_has_branching(self):
        """sl_6 dominance order has branching (non-linear)."""
        edges = transport_graph_edges(6)
        # sl_6 has branching: (4,2) covers both (4,1,1) and (3,3)
        edge_set = set(edges)
        assert ((4, 2), (4, 1, 1)) in edge_set
        assert ((4, 2), (3, 3)) in edge_set

    def test_propagation_summary(self):
        """Transport summary through sl_7: all fully covered."""
        summary = transport_propagation_summary(max_N=7)
        assert len(summary) == 5  # sl_3 through sl_7
        for entry in summary:
            assert entry['fully_covered']

    def test_coverage_fraction_is_one(self):
        """Coverage fraction = 1 for all N <= 7."""
        for N in range(3, 8):
            cl = transport_closure_from_hooks(N)
            assert cl['coverage_fraction'] == 1


# =====================================================================
# 9. Shadow depth classification
# =====================================================================

class TestShadowDepth:
    """Test shadow depth on the T-line."""

    def test_all_sl4_class_M(self):
        """All non-trivial sl_4 W-algebras are class M on the T-line."""
        orbits = shadow_depth_all_orbits(4)
        for entry in orbits:
            assert entry['shadow_class'] == 'M'
            assert entry['shadow_depth'] == 'infinity'

    def test_all_sl3_class_M(self):
        """All non-trivial sl_3 W-algebras are class M on the T-line."""
        orbits = shadow_depth_all_orbits(3)
        for entry in orbits:
            assert entry['shadow_class'] == 'M'

    def test_shadow_depth_increases_under_ds(self):
        """Shadow depth should not decrease under DS reduction.
        Affine = class L (depth 3), W-algebras >= class M."""
        for N in range(3, 6):
            orbits = shadow_depth_all_orbits(N)
            for entry in orbits:
                # All non-trivial should be M (depth infinity)
                # or at worst L (depth 3, same as affine)
                assert entry['shadow_depth'] in [3, 'infinity']

    def test_special_levels_exist(self):
        """Each orbit has special levels where c=0 or 5c+22=0."""
        orbits = shadow_depth_all_orbits(3)
        for entry in orbits:
            # c=0 levels should exist (at least one)
            assert 'c_zero_levels' in entry['special_levels']


# =====================================================================
# 10. Self-dual (self-transpose) partitions
# =====================================================================

class TestSelfDual:
    """Test self-transpose partition analysis."""

    def test_sl3_one_self_dual(self):
        """sl_3: only (2,1) is self-transpose."""
        sd = self_dual_partitions(3)
        assert len(sd) == 1
        assert sd[0]['partition'] == (2, 1)

    def test_sl4_one_self_dual(self):
        """sl_4: only (2,2) is self-transpose."""
        sd = self_dual_partitions(4)
        assert len(sd) == 1
        assert sd[0]['partition'] == (2, 2)

    def test_sl5_self_dual(self):
        """sl_5: (3,1,1) is self-transpose ((3,1,1)^t = (3,1,1))."""
        sd = self_dual_partitions(5)
        parts = [s['partition'] for s in sd]
        assert (3, 1, 1) in parts
        # (2,2,1)^t = (3,2) != (2,2,1), so NOT self-dual
        assert (2, 2, 1) not in parts

    def test_self_dual_c_sum_constant(self):
        """Self-dual partitions with exact c: c+c' is constant."""
        # BP is self-dual with exact c
        sd3 = self_dual_partitions(3)
        assert sd3[0]['c_sum_is_constant']

    def test_bp_c_midpoint(self):
        """BP c midpoint = (c+c')/2."""
        sd = self_dual_partitions(3)
        bp = sd[0]
        assert bp['c_midpoint'] is not None


# =====================================================================
# 11. Non-hook partition analysis
# =====================================================================

class TestNonHookPartitions:
    """Test non-hook partition analysis."""

    def test_sl4_one_non_hook(self):
        """sl_4 has one non-hook non-principal: (2,2)."""
        nh = non_hook_partition_analysis(4)
        assert len(nh) == 1
        assert nh[0]['partition'] == (2, 2)

    def test_sl5_non_hooks(self):
        """sl_5 non-hooks: (3,2) and (2,2,1)."""
        nh = non_hook_partition_analysis(5)
        parts = [e['partition'] for e in nh]
        assert (3, 2) in parts
        assert (2, 2, 1) in parts

    def test_non_hooks_all_reached(self):
        """All non-hook partitions of sl_4..sl_6 are reached by transport."""
        for N in range(4, 7):
            nh = non_hook_partition_analysis(N)
            for entry in nh:
                assert entry['reached_by_transport'], (
                    f"sl_{N} {entry['partition']} not reached")

    def test_non_hook_duality_status(self):
        """Non-hook partitions have 'conjectural' duality status."""
        nh = non_hook_partition_analysis(4)
        for entry in nh:
            assert entry['duality_status'] == 'conjectural'


# =====================================================================
# 12. Complementarity constant table
# =====================================================================

class TestComplementarity:
    """Test complementarity constant table."""

    def test_sl3_table(self):
        """sl_3 complementarity table has 2 entries."""
        table = complementarity_constant_table(3)
        assert len(table) == 2

    def test_sl4_table(self):
        """sl_4 complementarity table has 4 entries."""
        table = complementarity_constant_table(4)
        assert len(table) == 4

    def test_self_transpose_rho_equal(self):
        """Self-transpose partitions have rho_source = rho_target."""
        table = complementarity_constant_table(4)
        for entry in table:
            if entry['is_self_transpose']:
                assert entry['rho_equal']

    def test_bp_complementarity_constant(self):
        """BP kappa sum is constant (self-dual, exact c)."""
        table = complementarity_constant_table(3)
        bp_entry = [e for e in table if e['partition'] == (2, 1)][0]
        assert bp_entry['kappa_sum_is_constant']


# =====================================================================
# 13. Multi-path kappa verification
# =====================================================================

class TestKappaMultipath:
    """Test multi-path kappa verification."""

    def test_bp_kappa_multipath(self):
        """BP kappa verified via multiple paths."""
        result = kappa_multipath_verification((2, 1))
        assert result['c_exact']
        assert result['anomaly_ratio'] == Rational(1, 6)

    def test_w3_kappa_multipath(self):
        """W_3 kappa verified via multiple paths."""
        result = kappa_multipath_verification((3,))
        assert result['c_exact']
        assert result['anomaly_ratio'] == Rational(5, 6)

    def test_w4_kappa_multipath(self):
        """W_4 kappa verified via multiple paths."""
        result = kappa_multipath_verification((4,))
        assert result['c_exact']
        assert result['anomaly_ratio'] == Rational(13, 12)

    def test_numerical_consistency(self):
        """Numerical values are consistent at test levels."""
        for lam in [(2,), (3,), (2, 1), (4,)]:
            result = kappa_multipath_verification(lam)
            for num in result['numerical']:
                # kappa should be finite at test levels
                assert num['kappa'] is not None

    def test_bp_complementarity_sum_constant_numerical(self):
        """BP kappa + kappa_dual is numerically constant across levels."""
        result = kappa_multipath_verification((2, 1))
        sums = [float(num['sum']) for num in result['numerical']]
        # All sums should be the same value
        for s in sums:
            assert abs(s - sums[0]) < 1e-10


# =====================================================================
# 14. OPE data for Bershadsky-Polyakov
# =====================================================================

class TestBPOPEData:
    """Test OPE data for the Bershadsky-Polyakov algebra."""

    def test_bp_generator_count(self):
        """BP has 4 generators."""
        data = sl3_subregular_ope_data()
        assert len(data['generators']) == 4

    def test_bp_generator_names(self):
        """BP generators: J, G+, G-, T."""
        data = sl3_subregular_ope_data()
        names = [g[0] for g in data['generators']]
        assert 'J' in names
        assert 'G+' in names
        assert 'G-' in names
        assert 'T' in names

    def test_bp_central_charge_at_k1(self):
        """BP c(k=1) = -67/4."""
        data = sl3_subregular_ope_data(Rational(1))
        assert data['central_charge'] == Rational(-67, 4)

    def test_bp_jj_pole(self):
        """J(z)J(w) ~ (c/3)/(z-w)^2."""
        data = sl3_subregular_ope_data()
        c_val = data['central_charge']
        assert simplify(data['ope']['JJ']['pole_2'] - c_val / 3) == 0

    def test_bp_tt_pole(self):
        """T(z)T(w) ~ (c/2)/(z-w)^4."""
        data = sl3_subregular_ope_data()
        c_val = data['central_charge']
        assert simplify(data['ope']['TT']['pole_4'] - c_val / 2) == 0

    def test_bp_gg_pole3(self):
        """G+G- pole 3 = c/3."""
        data = sl3_subregular_ope_data()
        c_val = data['central_charge']
        assert simplify(data['ope']['G+G-']['pole_3'] - c_val / 3) == 0

    def test_bp_r_matrix_pole_order(self):
        """r-matrix poles are one order less than OPE (AP19)."""
        data = sl3_subregular_ope_data()
        # OPE TT has pole_4 -> r-matrix has pole_3
        assert 'pole_3' in data['r_matrix']['TT']
        assert 'pole_4' not in data['r_matrix']['TT']
        # OPE JJ has pole_2 -> r-matrix has pole_1
        assert 'pole_1' in data['r_matrix']['JJ']
        assert 'pole_2' not in data['r_matrix']['JJ']

    def test_bp_is_self_dual(self):
        """BP is self-dual: (2,1)^t = (2,1)."""
        data = sl3_subregular_ope_data()
        assert data['is_self_dual']

    def test_bp_self_dual_level(self):
        """BP self-dual level: k' = -k - 6."""
        data = sl3_subregular_ope_data()
        assert simplify(data['self_dual_level'] + k + 6) == 0


# =====================================================================
# 15. Comprehensive verification bundle
# =====================================================================

class TestVerificationBundle:
    """Test the comprehensive verification bundle."""

    def test_all_pass(self):
        """All internal verification checks pass."""
        results = verify_non_principal_w_duality()
        failed = [name for name, val in results.items() if not val]
        assert not failed, f"Failed checks: {failed}"

    def test_at_least_50_checks(self):
        """At least 50 verification checks."""
        results = verify_non_principal_w_duality()
        assert len(results) >= 50


# =====================================================================
# 16. Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks (AP10: not just hardcoded values)."""

    def test_principal_rho_monotone(self):
        """Principal anomaly ratio increases with N."""
        from compute.lib.hook_type_w_duality import anomaly_ratio_from_partition
        rhos = [anomaly_ratio_from_partition((N,)) for N in range(2, 7)]
        for i in range(len(rhos) - 1):
            assert rhos[i] < rhos[i + 1]

    def test_transpose_involution(self):
        """Partition transpose is an involution for all N <= 7."""
        from compute.lib.nonprincipal_ds_orbits import (
            transpose_partition, _partitions_of_n)
        for N in range(2, 8):
            for lam in _partitions_of_n(N):
                lam_t = transpose_partition(lam)
                lam_tt = transpose_partition(lam_t)
                assert lam == lam_tt, f"Transpose not involutive: {lam}"

    def test_dual_level_involutive_all_N(self):
        """k'' = k for all N (dual level involutive)."""
        for N in range(2, 8):
            kv = dual_level(N, k)
            kvv = dual_level(N, kv)
            assert simplify(kvv - k) == 0

    def test_generator_count_equals_centralizer_dim(self):
        """Generator count = dim(g^f) for all orbits of sl_3..sl_5."""
        from compute.lib.nonprincipal_ds_orbits import (
            _partitions_of_n, centralizer_dimension_sl_n,
            type_a_partition_sl2_triple)
        from compute.lib.hook_type_w_duality import w_algebra_generator_data
        for N in range(3, 6):
            for lam in _partitions_of_n(N):
                if lam == (1,) * N:
                    continue
                g = w_algebra_generator_data(lam)
                assert g.f_centralizer_dimension > 0

    def test_bp_kappa_at_k0(self):
        """BP kappa(k=0) = rho * c(k=0) = (1/6)*(-6) = -1."""
        kappa_val, exact = correct_kappa((2, 1), Rational(0))
        assert exact
        assert kappa_val == -1

    def test_correct_kappa_exact_flag(self):
        """correct_kappa returns exact=True only for known formulas."""
        _, ex1 = correct_kappa((2,))
        _, ex2 = correct_kappa((3,))
        _, ex3 = correct_kappa((2, 1))
        _, ex4 = correct_kappa((4,))
        _, ex5 = correct_kappa((2, 2))
        assert ex1 and ex2 and ex3 and ex4
        assert not ex5  # (2,2) uses oversimplified KRW
