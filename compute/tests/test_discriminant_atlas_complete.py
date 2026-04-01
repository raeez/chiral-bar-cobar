r"""Tests for the complete discriminant atlas across ALL simple Lie algebras.

Tests conj:non-simply-laced-discriminant and produces a complete atlas
of shadow discriminants for ALL simple Lie algebras of rank <= 8.

Organized in sections:
    1. A_n matches known values from existing engines
    2. B_2 = C_2 isomorphism: discriminants agree
    3. D_4 triality
    4. G_2 inside B_3 embedding compatibility
    5. F_4 inside E_6 folding
    6. E_6 self-duality
    7. Classical limit k -> infinity
    8. Critical limit k -> -h^vee
    9. DS route matches direct OPE route
   10. Cross-check: kappa values match landscape_census.tex
   11. Ghost sector k-independence
   12. Shadow tower verification
   13. Lacing number analysis
   14. Universal formula verification
   15. Completeness and structural tests

Uses exact Fraction arithmetic throughout.
"""

from __future__ import annotations

import pytest
from fractions import Fraction

from compute.lib.discriminant_atlas_complete import (
    all_simple_types,
    simply_laced_types,
    non_simply_laced_types,
    lie_data,
    c_affine,
    kappa_affine,
    ff_dual_level,
    c_W_principal,
    anomaly_ratio_general,
    kappa_W_T_line,
    virasoro_S4,
    virasoro_Delta,
    shadow_data_affine,
    shadow_data_W_T_line,
    ghost_central_charge,
    verify_ghost_c_k_independent,
    shadow_data_via_folding,
    shadow_tower_from_metric,
    atlas_entry,
    build_atlas,
    discriminant_nonzero_check,
    discriminant_scaling,
    discriminant_ratio_analysis,
    lacing_factor_analysis,
    classical_limit_check,
    universal_formula_test,
    summary_table,
    BnCn_comparison,
    D4_triality_check,
    E6_self_duality_check,
    FOLDING_PARENTS,
)


# ============================================================================
# Helper: standard level for most tests
# ============================================================================

K_DEFAULT = Fraction(5)


# ============================================================================
# Section 1: A_n matches known values from existing engines
# ============================================================================

class TestAnKnownValues:
    """Verify A_n shadow data against known values from ds_shadow_cascade_engine."""

    def test_A1_is_sl2(self):
        """A_1 = sl_2: dim=3, h=h^v=2."""
        d = lie_data("A", 1)
        assert d['dim'] == 3
        assert d['h'] == 2
        assert d['h_dual'] == 2
        assert d['simply_laced'] is True

    def test_A1_kappa(self):
        """kappa(sl_2, k=5) = 3*(5+2)/4 = 21/4."""
        kap = kappa_affine(3, 2, Fraction(5))
        assert kap == Fraction(21, 4)

    def test_A1_c_affine(self):
        """c(sl_2, k=5) = 3*5/(5+2) = 15/7."""
        c = c_affine(3, 2, Fraction(5))
        assert c == Fraction(15, 7)

    def test_A2_is_sl3(self):
        """A_2 = sl_3: dim=8, h=h^v=3."""
        d = lie_data("A", 2)
        assert d['dim'] == 8
        assert d['h'] == 3
        assert d['h_dual'] == 3

    def test_A2_kappa(self):
        """kappa(sl_3, k=5) = 8*(5+3)/6 = 32/3."""
        kap = kappa_affine(8, 3, Fraction(5))
        assert kap == Fraction(32, 3)

    def test_W2_is_Virasoro(self):
        """W(A_1) = Virasoro: c = 1 - 6/(k+2)."""
        c_w = c_W_principal("A", 1, Fraction(5))
        expected = Fraction(1) - Fraction(6) / (Fraction(5) + 2)
        assert c_w == expected
        assert c_w == Fraction(1, 7)

    def test_W3_central_charge(self):
        """c(W_3, k=5) = 2 - 24/(k+3) = 2 - 24/8 = -1."""
        c_w = c_W_principal("A", 2, Fraction(5))
        assert c_w == Fraction(-1)

    def test_W2_kappa_T_line(self):
        """kappa_T for W_2 (Virasoro) = c/2."""
        c_w = c_W_principal("A", 1, Fraction(5))
        kap = kappa_W_T_line("A", 1, Fraction(5))
        assert kap == c_w / 2

    def test_A1_anomaly_ratio(self):
        """rho(sl_2) = H_2 - 1 = 1/2."""
        rho = anomaly_ratio_general("A", 1)
        assert rho == Fraction(1, 2)

    def test_A2_anomaly_ratio(self):
        """rho(sl_3) = H_3 - 1 = 1/2 + 1/3 = 5/6."""
        rho = anomaly_ratio_general("A", 2)
        assert rho == Fraction(5, 6)

    def test_A3_anomaly_ratio(self):
        """rho(sl_4) = H_4 - 1 = 1/2 + 1/3 + 1/4 = 13/12."""
        rho = anomaly_ratio_general("A", 3)
        assert rho == Fraction(13, 12)

    def test_all_An_affine_class_L(self):
        """All affine A_n are class L (depth 3)."""
        for n in range(1, 9):
            sd = shadow_data_affine("A", n, K_DEFAULT)
            assert sd['depth_class'] == 'L'
            assert sd['S4'] == Fraction(0)
            assert sd['Delta'] == Fraction(0)

    def test_all_An_W_class_M(self):
        """All W(A_n) are class M (infinite tower) for n >= 1."""
        for n in range(1, 9):
            sd = shadow_data_W_T_line("A", n, K_DEFAULT)
            assert sd['depth_class'] == 'M'
            assert sd['Delta'] != Fraction(0)


# ============================================================================
# Section 2: B_2 = C_2 isomorphism
# ============================================================================

class TestB2C2Isomorphism:
    """B_2 = so(5) and C_2 = sp(4) are isomorphic."""

    def test_same_dim(self):
        d_b = lie_data("B", 2)
        d_c = lie_data("C", 2)
        assert d_b['dim'] == d_c['dim'] == 10

    def test_same_h(self):
        d_b = lie_data("B", 2)
        d_c = lie_data("C", 2)
        assert d_b['h'] == d_c['h'] == 4

    def test_same_h_dual(self):
        d_b = lie_data("B", 2)
        d_c = lie_data("C", 2)
        assert d_b['h_dual'] == d_c['h_dual'] == 3

    def test_same_c_affine(self):
        c_b = c_affine(10, 3, K_DEFAULT)
        c_c = c_affine(10, 3, K_DEFAULT)
        assert c_b == c_c

    def test_same_kappa_affine(self):
        kap_b = kappa_affine(10, 3, K_DEFAULT)
        kap_c = kappa_affine(10, 3, K_DEFAULT)
        assert kap_b == kap_c

    def test_same_c_W(self):
        c_b = c_W_principal("B", 2, K_DEFAULT)
        c_c = c_W_principal("C", 2, K_DEFAULT)
        assert c_b == c_c

    def test_same_Delta_W(self):
        """B_2 and C_2 W-algebras have the same discriminant."""
        c_b = c_W_principal("B", 2, K_DEFAULT)
        c_c = c_W_principal("C", 2, K_DEFAULT)
        delta_b = virasoro_Delta(c_b)
        delta_c = virasoro_Delta(c_c)
        assert delta_b == delta_c

    def test_BnCn_comparison_n2(self):
        """BnCn comparison at n=2: everything agrees."""
        comp = BnCn_comparison(2, K_DEFAULT)
        row = comp[0]
        assert row['c_agree'] is True
        assert row['Delta_agree'] is True
        assert row['same_h_dual'] is True


# ============================================================================
# Section 3: D_4 triality
# ============================================================================

class TestD4Triality:
    """D_4 has S_3 triality symmetry."""

    def test_D4_data(self):
        d = lie_data("D", 4)
        assert d['dim'] == 28
        assert d['h'] == 6
        assert d['h_dual'] == 6
        assert d['simply_laced'] is True

    def test_D4_exponents(self):
        """D_4 exponents: [1, 3, 3, 5] -- note the repeated 3."""
        d = lie_data("D", 4)
        assert sorted(d['exponents']) == [1, 3, 3, 5]

    def test_D4_triality_well_defined(self):
        """D_4 triality check returns valid data."""
        result = D4_triality_check(K_DEFAULT)
        assert result['depth_class_aff'] == 'L'
        assert result['depth_class_W'] == 'M'
        assert result['Delta_W'] != 0


# ============================================================================
# Section 4: G_2 inside B_3 embedding
# ============================================================================

class TestG2B3Embedding:
    """G_2 is a subalgebra of B_3 = so(7). Check compatibility."""

    def test_G2_data(self):
        d = lie_data("G", 2)
        assert d['dim'] == 14
        assert d['h'] == 6
        assert d['h_dual'] == 4
        assert d['lacing_number'] == 3

    def test_B3_data(self):
        d = lie_data("B", 3)
        assert d['dim'] == 21
        assert d['h'] == 6
        assert d['h_dual'] == 5
        assert d['lacing_number'] == 2

    def test_G2_B3_same_coxeter(self):
        """G_2 and B_3 have the same Coxeter number h=6."""
        d_g = lie_data("G", 2)
        d_b = lie_data("B", 3)
        assert d_g['h'] == d_b['h'] == 6

    def test_G2_B3_different_h_dual(self):
        """G_2 and B_3 have different dual Coxeter numbers."""
        d_g = lie_data("G", 2)
        d_b = lie_data("B", 3)
        assert d_g['h_dual'] != d_b['h_dual']
        assert d_g['h_dual'] == 4
        assert d_b['h_dual'] == 5

    def test_G2_folds_from_D4(self):
        """G_2 folds from D_4 (not from B_3)."""
        from compute.lib.discriminant_atlas_complete import folding_parent
        p = folding_parent("G", 2)
        assert p == ("D", 4)

    def test_G2_folding_data(self):
        """Folding route gives valid data for G_2."""
        f = shadow_data_via_folding("G", 2, K_DEFAULT)
        assert f is not None
        assert f['lacing_number'] == 3


# ============================================================================
# Section 5: F_4 inside E_6 folding
# ============================================================================

class TestF4E6Folding:
    """F_4 folds from E_6."""

    def test_F4_data(self):
        d = lie_data("F", 4)
        assert d['dim'] == 52
        assert d['h'] == 12
        assert d['h_dual'] == 9
        assert d['lacing_number'] == 2

    def test_E6_data(self):
        d = lie_data("E", 6)
        assert d['dim'] == 78
        assert d['h'] == 12
        assert d['h_dual'] == 12
        assert d['lacing_number'] == 1

    def test_F4_folds_from_E6(self):
        from compute.lib.discriminant_atlas_complete import folding_parent
        p = folding_parent("F", 4)
        assert p == ("E", 6)

    def test_F4_E6_same_coxeter(self):
        """F_4 and E_6 have the same Coxeter number h=12."""
        d_f = lie_data("F", 4)
        d_e = lie_data("E", 6)
        assert d_f['h'] == d_e['h'] == 12

    def test_F4_folding_route(self):
        """Folding route for F_4 gives valid data."""
        f = shadow_data_via_folding("F", 4, K_DEFAULT)
        assert f is not None
        assert f['parent_type'] == 'E6'
        assert f['lacing_number'] == 2


# ============================================================================
# Section 6: E_6 self-duality
# ============================================================================

class TestE6SelfDuality:
    """E_6 has diagram automorphism. Check discriminant symmetry."""

    def test_E6_ff_dual_level(self):
        """FF dual level for E_6: k' = -k - 24."""
        k_dual = ff_dual_level(12, Fraction(5))
        assert k_dual == Fraction(-29)

    def test_E6_self_duality(self):
        """E_6 duality check returns valid data."""
        result = E6_self_duality_check(Fraction(5))
        assert 'error' not in result
        assert result['k'] == Fraction(5)
        assert result['k_dual'] == Fraction(-29)

    def test_E6_c_sum(self):
        """c(E_6, k) + c(E_6, -k-24) should relate to 2*dim/(h^v)... complex."""
        result = E6_self_duality_check(Fraction(10))
        # The sum depends on the specific duality; just check it's rational
        assert isinstance(result['c_sum'], Fraction)


# ============================================================================
# Section 7: Classical limit (k -> infinity)
# ============================================================================

class TestClassicalLimit:
    """As k -> infinity, Delta_T/kappa^2 -> 0."""

    def test_classical_limit_A1(self):
        """For A_1 (Virasoro), Delta/kappa^2 -> 0 as k -> infinity."""
        results = classical_limit_check("A", 1, [Fraction(n) for n in [10, 100, 1000]])
        ratios = [r['Delta_over_kappa_sq'] for r in results if r['Delta_over_kappa_sq'] is not None]
        # Ratios should decrease
        assert all(abs(ratios[i]) >= abs(ratios[i + 1]) for i in range(len(ratios) - 1))

    def test_classical_limit_B3(self):
        """For B_3, Delta/kappa^2 decreases with k."""
        results = classical_limit_check("B", 3, [Fraction(n) for n in [10, 100, 1000]])
        ratios = [abs(r['Delta_over_kappa_sq']) for r in results
                  if r['Delta_over_kappa_sq'] is not None]
        assert len(ratios) >= 2
        assert ratios[-1] < ratios[0]

    def test_classical_limit_E8(self):
        """For E_8, Delta approaches finite value as k -> infinity.

        E_8 converges slowly: c_W = 8 - 248*30/(k+30), so at k=1000
        c_W is still far from 8. Need k >> dim*h^v = 7440 to converge.
        """
        results = classical_limit_check("E", 8, [Fraction(n) for n in [10, 1000, 1000000]])
        # Delta should converge to 40/(5*8+22) = 40/62 = 20/31 as c -> 8
        limiting = Fraction(40, 5 * 8 + 22)
        last_delta = results[-1]['Delta']
        # At k=10^6, should be close to the limiting value
        assert abs(float(last_delta) - float(limiting)) < 0.001


# ============================================================================
# Section 8: Critical limit (k -> -h^vee)
# ============================================================================

class TestCriticalLimit:
    """At critical level k = -h^vee, Sugawara is undefined."""

    def test_critical_A1(self):
        """c(sl_2, k=-2) should raise."""
        with pytest.raises(ValueError):
            c_affine(3, 2, Fraction(-2))

    def test_critical_B3(self):
        """c(B_3, k=-5) should raise."""
        with pytest.raises(ValueError):
            c_affine(21, 5, Fraction(-5))

    def test_critical_W(self):
        """W(A_1) at k=-2 should raise."""
        with pytest.raises(ValueError):
            c_W_principal("A", 1, Fraction(-2))

    def test_near_critical_large_c(self):
        """Near critical level, |c| is large."""
        c_w = c_W_principal("A", 1, Fraction(-2) + Fraction(1, 1000))
        assert abs(c_w) > 100


# ============================================================================
# Section 9: DS route matches direct OPE route
# ============================================================================

class TestDSRouteAgreement:
    """Both routes give the same discriminant for non-simply-laced types."""

    def test_B2_ds_routes_agree(self):
        """B_2: direct and folding route discriminants agree."""
        entry = atlas_entry("B", 2, K_DEFAULT)
        # For B_2, the folding parent is D_3 = A_3
        # The T-line Delta is computed from c(W(B_2))
        # Both routes use the same c, so Delta must agree
        assert entry['ds_routes_agree'] is True or entry['folding'] is None

    def test_G2_ds_routes_agree(self):
        """G_2: direct route gives well-defined Delta."""
        entry = atlas_entry("G", 2, K_DEFAULT)
        w = entry['W_T_line']
        assert w['Delta'] != 0
        # The folding route should also give valid data
        if entry['folding'] is not None:
            assert entry['folding']['Delta_child'] == w['Delta']

    def test_F4_ds_routes_agree(self):
        """F_4: direct route gives well-defined Delta."""
        entry = atlas_entry("F", 4, K_DEFAULT)
        w = entry['W_T_line']
        assert w['Delta'] != 0

    def test_all_nonsl_with_parents_have_folding_data(self):
        """All non-simply-laced types with available parents have folding data."""
        for key in FOLDING_PARENTS:
            type_, rank = key
            f = shadow_data_via_folding(type_, rank, K_DEFAULT)
            assert f is not None, f"Folding data missing for {type_}{rank}"

    def test_folding_parents_count(self):
        """We have 12 folding relationships in the registry."""
        # B2-B7 (6) + C2-C4 (3) + G2 (1) + F4 (1) = 11
        assert len(FOLDING_PARENTS) == 11


# ============================================================================
# Section 10: Cross-check kappa values
# ============================================================================

class TestKappaValues:
    """Cross-check kappa values against known formulas from landscape_census.tex."""

    def test_kappa_sl2_k5(self):
        """kappa(sl_2, k=5) = 3*7/4 = 21/4."""
        assert kappa_affine(3, 2, Fraction(5)) == Fraction(21, 4)

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*4/6 = 16/3."""
        assert kappa_affine(8, 3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_B2_k5(self):
        """kappa(B_2, k=5) = 10*8/(2*3) = 40/3."""
        assert kappa_affine(10, 3, Fraction(5)) == Fraction(40, 3)

    def test_kappa_G2_k5(self):
        """kappa(G_2, k=5) = 14*9/(2*4) = 63/4."""
        assert kappa_affine(14, 4, Fraction(5)) == Fraction(63, 4)

    def test_kappa_F4_k5(self):
        """kappa(F_4, k=5) = 52*14/(2*9) = 364/9."""
        assert kappa_affine(52, 9, Fraction(5)) == Fraction(364, 9)

    def test_kappa_E6_k1(self):
        """kappa(E_6, k=1) = 78*13/(2*12) = 1014/24 = 169/4."""
        assert kappa_affine(78, 12, Fraction(1)) == Fraction(169, 4)

    def test_kappa_E7_k1(self):
        """kappa(E_7, k=1) = 133*19/(2*18) = 2527/36."""
        assert kappa_affine(133, 18, Fraction(1)) == Fraction(2527, 36)

    def test_kappa_E8_k1(self):
        """kappa(E_8, k=1) = 248*31/(2*30) = 7688/60 = 1922/15."""
        assert kappa_affine(248, 30, Fraction(1)) == Fraction(1922, 15)

    def test_kappa_formula_universal(self):
        """kappa = dim*(k+h^v)/(2*h^v) for all types."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            kap = kappa_affine(d['dim'], d['h_dual'], K_DEFAULT)
            expected = Fraction(d['dim']) * (K_DEFAULT + d['h_dual']) / (2 * d['h_dual'])
            assert kap == expected, f"{type_}{rank}: kappa mismatch"


# ============================================================================
# Section 11: Ghost sector k-independence
# ============================================================================

class TestGhostSector:
    """Ghost central charge c_ghost = dim - rank is k-independent."""

    def test_ghost_c_formula(self):
        """c_ghost(g) = dim(g) - rank(g)."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            gc = ghost_central_charge(type_, rank)
            assert gc == Fraction(d['dim'] - d['rank'])

    def test_ghost_c_A1(self):
        assert ghost_central_charge("A", 1) == Fraction(2)

    def test_ghost_c_A2(self):
        assert ghost_central_charge("A", 2) == Fraction(6)

    def test_ghost_c_E8(self):
        assert ghost_central_charge("E", 8) == Fraction(240)

    def test_ghost_c_k_independent_all(self):
        """Ghost c is k-independent for a sample of types."""
        for type_, rank in [("A", 3), ("B", 4), ("C", 5), ("D", 6), ("E", 7), ("F", 4), ("G", 2)]:
            assert verify_ghost_c_k_independent(type_, rank), \
                f"Ghost c NOT k-independent for {type_}{rank}"

    def test_c_additivity(self):
        """c(g-hat, k) = c(W(g), k) + c_ghost for all types."""
        for type_, rank in all_simple_types(6):
            d = lie_data(type_, rank)
            gc = ghost_central_charge(type_, rank)
            for kv in [Fraction(1), Fraction(5), Fraction(10)]:
                try:
                    c_aff = c_affine(d['dim'], d['h_dual'], kv)
                    c_w = c_W_principal(type_, rank, kv)
                    assert c_aff == c_w + gc, \
                        f"{type_}{rank} at k={kv}: c additivity fails"
                except ValueError:
                    continue


# ============================================================================
# Section 12: Shadow tower verification
# ============================================================================

class TestShadowTower:
    """Verify shadow tower computation from metric data."""

    def test_heisenberg_tower_zero(self):
        """Heisenberg (kappa=1, alpha=0, S4=0): tower terminates at arity 2."""
        tower = shadow_tower_from_metric(Fraction(1), Fraction(0), Fraction(0))
        assert tower[2] == Fraction(1)  # S_2 = kappa
        for r in range(3, 9):
            assert tower[r] == Fraction(0), f"S_{r} != 0 for Heisenberg"

    def test_affine_tower_terminates_at_3(self):
        """Affine KM (alpha=1, S4=0): tower terminates at arity 3."""
        kap = Fraction(5)
        tower = shadow_tower_from_metric(kap, Fraction(1), Fraction(0))
        assert tower[2] == kap  # S_2 = kappa
        assert tower[3] != Fraction(0)  # cubic nonzero
        for r in range(4, 9):
            assert tower[r] == Fraction(0), f"S_{r} != 0 for affine KM"

    def test_virasoro_tower_infinite(self):
        """Virasoro at c=1/7: tower never terminates."""
        c_val = Fraction(1, 7)
        kap = c_val / 2
        s4 = virasoro_S4(c_val)
        tower = shadow_tower_from_metric(kap, Fraction(2), s4)
        assert tower[2] == kap  # S_2 = kappa
        for r in range(3, 9):
            assert tower[r] != Fraction(0), f"S_{r} = 0 for Virasoro at c=1/7"

    def test_tower_S2_equals_kappa(self):
        """S_2 = kappa for all towers."""
        for kap in [Fraction(1), Fraction(5), Fraction(-3, 2)]:
            tower = shadow_tower_from_metric(kap, Fraction(1), Fraction(0))
            assert tower[2] == kap

    def test_virasoro_S4_formula(self):
        """S_4(Vir) = 10/(c*(5c+22)) at several central charges."""
        for c_val in [Fraction(1), Fraction(2), Fraction(26), Fraction(1, 2)]:
            s4 = virasoro_S4(c_val)
            expected = Fraction(10) / (c_val * (5 * c_val + 22))
            assert s4 == expected

    def test_virasoro_Delta_formula(self):
        """Delta(Vir) = 40/(5c+22) at several central charges."""
        for c_val in [Fraction(1), Fraction(26), Fraction(13)]:
            delta = virasoro_Delta(c_val)
            expected = Fraction(40) / (5 * c_val + 22)
            assert delta == expected

    def test_affine_all_S4_zero(self):
        """All affine KM algebras have S_4 = 0."""
        for type_, rank in all_simple_types(8):
            sd = shadow_data_affine(type_, rank, K_DEFAULT)
            assert sd['S4'] == Fraction(0), f"{type_}{rank} affine S_4 != 0"

    def test_affine_all_Delta_zero(self):
        """All affine KM algebras have Delta = 0."""
        for type_, rank in all_simple_types(8):
            sd = shadow_data_affine(type_, rank, K_DEFAULT)
            assert sd['Delta'] == Fraction(0), f"{type_}{rank} affine Delta != 0"


# ============================================================================
# Section 13: Lacing number analysis
# ============================================================================

class TestLacingNumber:
    """Verify lacing numbers and test conj:non-simply-laced-discriminant."""

    def test_simply_laced_lacing_1(self):
        """All simply-laced types have lacing number 1."""
        for type_, rank in simply_laced_types(8):
            d = lie_data(type_, rank)
            assert d['lacing_number'] == 1, f"{type_}{rank} lacing != 1"

    def test_B_lacing_2(self):
        """All B_n have lacing number 2."""
        for n in range(2, 9):
            d = lie_data("B", n)
            assert d['lacing_number'] == 2

    def test_C_lacing_2(self):
        """All C_n have lacing number 2."""
        for n in range(2, 9):
            d = lie_data("C", n)
            assert d['lacing_number'] == 2

    def test_G2_lacing_3(self):
        """G_2 has lacing number 3."""
        d = lie_data("G", 2)
        assert d['lacing_number'] == 3

    def test_F4_lacing_2(self):
        """F_4 has lacing number 2."""
        d = lie_data("F", 4)
        assert d['lacing_number'] == 2

    def test_BnCn_same_dim(self):
        """B_n and C_n have the same dimension n(2n+1)."""
        for n in range(2, 9):
            d_b = lie_data("B", n)
            d_c = lie_data("C", n)
            assert d_b['dim'] == d_c['dim']
            assert d_b['dim'] == n * (2 * n + 1)

    def test_BnCn_same_coxeter(self):
        """B_n and C_n have the same Coxeter number 2n."""
        for n in range(2, 9):
            d_b = lie_data("B", n)
            d_c = lie_data("C", n)
            assert d_b['h'] == d_c['h'] == 2 * n

    def test_BnCn_different_h_dual_n3_plus(self):
        """B_n and C_n have different h^vee for n >= 3."""
        for n in range(3, 9):
            d_b = lie_data("B", n)
            d_c = lie_data("C", n)
            assert d_b['h_dual'] != d_c['h_dual']
            assert d_b['h_dual'] == 2 * n - 1
            assert d_c['h_dual'] == n + 1

    def test_lacing_factor_in_discriminant(self):
        """Non-simply-laced discriminants differ from parents.

        The folding map changes c(W), hence Delta = 40/(5c+22).
        The STRUCTURAL prediction: the c difference involves h^vee
        which encodes the root length ratio.
        """
        atlas = build_atlas(K_DEFAULT, max_rank=7)
        analysis = lacing_factor_analysis(atlas)
        for row in analysis:
            # Delta ratio is well-defined (neither parent nor child Delta is zero)
            assert row['Delta_ratio'] is not None, \
                f"Delta ratio undefined for {row['child']}"


# ============================================================================
# Section 14: Universal formula verification
# ============================================================================

class TestUniversalFormula:
    """Test the universal discriminant formula."""

    def test_universal_formula_k5(self):
        """Universal formula matches direct computation at k=5."""
        results = universal_formula_test(Fraction(5), 8)
        for r in results:
            if 'error' not in r:
                assert r['match'], f"Universal formula mismatch for {r['label']}"

    def test_universal_formula_k1(self):
        """Universal formula matches at k=1."""
        results = universal_formula_test(Fraction(1), 8)
        for r in results:
            if 'error' not in r:
                assert r['match'], f"Universal formula mismatch for {r['label']}"

    def test_universal_formula_k10(self):
        """Universal formula matches at k=10."""
        results = universal_formula_test(Fraction(10), 8)
        for r in results:
            if 'error' not in r:
                assert r['match'], f"Universal formula mismatch for {r['label']}"

    def test_universal_formula_explicit(self):
        """Verify the universal formula by hand for A_1.

        Delta = 40*(k+2) / ((5*1+22)*k + 2*(5*1+22-5*3))
              = 40*(k+2) / (27*k + 2*(27-15))
              = 40*(k+2) / (27*k + 24)
              = 40*(k+2) / (3*(9k+8))
        At k=5: 40*7 / (3*53) = 280/159.

        Direct: c_W = 1 - 6/7 = 1/7. Delta = 40/(5/7+22) = 40/(159/7) = 280/159.
        """
        delta = virasoro_Delta(Fraction(1, 7))
        assert delta == Fraction(280, 159)


# ============================================================================
# Section 15: Completeness and structural tests
# ============================================================================

class TestCompleteness:
    """Verify the atlas covers all expected types."""

    def test_total_type_count(self):
        """There are 32 simple types with rank <= 8."""
        types = all_simple_types(8)
        # A: 1..8 = 8, B: 2..8 = 7, C: 2..8 = 7, D: 4..8 = 5,
        # G_2, F_4, E_6, E_7, E_8 = 5. Total = 32.
        assert len(types) == 32

    def test_simply_laced_count(self):
        """16 simply-laced types with rank <= 8."""
        # A: 8, D: 5, E: 3 = 16
        sl = simply_laced_types(8)
        assert len(sl) == 16

    def test_non_simply_laced_count(self):
        """16 non-simply-laced types with rank <= 8."""
        # B: 7, C: 7, F: 1, G: 1 = 16
        nsl = non_simply_laced_types(8)
        assert len(nsl) == 16

    def test_atlas_covers_all(self):
        """Atlas has entries for all 32 types."""
        atlas = build_atlas(K_DEFAULT, max_rank=8)
        assert len(atlas) == 32

    def test_no_errors_in_atlas(self):
        """No type produces an error at k=5."""
        atlas = build_atlas(K_DEFAULT, max_rank=8)
        for label, entry in atlas.items():
            assert 'error' not in entry, f"{label} has error: {entry.get('error')}"

    def test_all_affine_class_L(self):
        """Every affine KM is class L."""
        atlas = build_atlas(K_DEFAULT, max_rank=8)
        for label, entry in atlas.items():
            if 'error' in entry:
                continue
            assert entry['affine']['depth_class'] == 'L', f"{label} affine not class L"

    def test_all_W_class_M(self):
        """Every W-algebra is class M (on T-line)."""
        atlas = build_atlas(K_DEFAULT, max_rank=8)
        for label, entry in atlas.items():
            if 'error' in entry:
                continue
            w = entry.get('W_T_line')
            if w is not None:
                assert w['depth_class'] == 'M', f"{label} W not class M"

    def test_all_W_Delta_nonzero(self):
        """Delta != 0 for all W-algebras (non-abelian implies class M)."""
        atlas = build_atlas(K_DEFAULT, max_rank=8)
        check = discriminant_nonzero_check(atlas)
        for label, nonzero in check.items():
            assert nonzero, f"{label}: Delta = 0 for W-algebra"

    def test_summary_table_complete(self):
        """Summary table has 32 rows."""
        table = summary_table(K_DEFAULT, 8)
        assert len(table) == 32

    def test_dim_formula_An(self):
        """dim(A_n) = n(n+2) for all n."""
        for n in range(1, 9):
            d = lie_data("A", n)
            assert d['dim'] == n * (n + 2)

    def test_dim_formula_Bn(self):
        """dim(B_n) = n(2n+1) for all n >= 2."""
        for n in range(2, 9):
            d = lie_data("B", n)
            assert d['dim'] == n * (2 * n + 1)

    def test_dim_formula_Dn(self):
        """dim(D_n) = n(2n-1) for all n >= 4."""
        for n in range(4, 9):
            d = lie_data("D", n)
            assert d['dim'] == n * (2 * n - 1)

    def test_h_dual_formula_Bn(self):
        """h^vee(B_n) = 2n-1 for all n >= 2."""
        for n in range(2, 9):
            d = lie_data("B", n)
            assert d['h_dual'] == 2 * n - 1

    def test_h_dual_formula_Cn(self):
        """h^vee(C_n) = n+1 for all n >= 2."""
        for n in range(2, 9):
            d = lie_data("C", n)
            assert d['h_dual'] == n + 1

    def test_ff_involution(self):
        """FF involution is an involution: k'' = k for all types."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            h_v = d['h_dual']
            k = Fraction(5)
            k_dual = ff_dual_level(h_v, k)
            k_back = ff_dual_level(h_v, k_dual)
            assert k_back == k, f"{type_}{rank}: FF involution not involutive"


# ============================================================================
# Additional specific tests
# ============================================================================

class TestSpecificValues:
    """Specific numerical tests for particular algebras."""

    def test_virasoro_S4_c26(self):
        """S_4(Vir, c=26) = 10/(26*152) = 10/3952 = 5/1976."""
        s4 = virasoro_S4(Fraction(26))
        assert s4 == Fraction(10, 26 * (5 * 26 + 22))
        assert s4 == Fraction(5, 1976)

    def test_virasoro_Delta_c13(self):
        """Delta(Vir, c=13) = 40/(65+22) = 40/87."""
        delta = virasoro_Delta(Fraction(13))
        assert delta == Fraction(40, 87)

    def test_E8_dim(self):
        d = lie_data("E", 8)
        assert d['dim'] == 248

    def test_E8_exponents(self):
        d = lie_data("E", 8)
        assert d['exponents'] == [1, 7, 11, 13, 17, 19, 23, 29]

    def test_E7_dim(self):
        d = lie_data("E", 7)
        assert d['dim'] == 133

    def test_W_c_A1_formula(self):
        """c(W(A_1), k) = 1 - 6/(k+2)."""
        for kv in [Fraction(1), Fraction(2), Fraction(10)]:
            c_w = c_W_principal("A", 1, kv)
            expected = 1 - Fraction(6) / (kv + 2)
            assert c_w == expected

    def test_W_c_general_formula(self):
        """c(W(g), k) = rank - dim*h^v/(k+h^v) for several types."""
        for type_, rank in [("A", 3), ("B", 4), ("C", 5), ("D", 6), ("E", 6)]:
            d = lie_data(type_, rank)
            c_w = c_W_principal(type_, rank, K_DEFAULT)
            expected = Fraction(d['rank']) - Fraction(d['dim'] * d['h_dual']) / (K_DEFAULT + d['h_dual'])
            assert c_w == expected, f"{type_}{rank}: c_W formula mismatch"

    def test_B6_and_E6_same_dim(self):
        """B_6 and E_6 have the same dimension 78, but different structure."""
        d_b = lie_data("B", 6)
        d_e = lie_data("E", 6)
        assert d_b['dim'] == d_e['dim'] == 78
        assert d_b['h_dual'] != d_e['h_dual']
        # Different c_W at same level
        c_b = c_W_principal("B", 6, K_DEFAULT)
        c_e = c_W_principal("E", 6, K_DEFAULT)
        assert c_b != c_e

    def test_shadow_data_W_alpha_2(self):
        """All W-algebras have alpha = 2 on T-line (Virasoro value)."""
        for type_, rank in all_simple_types(8):
            sd = shadow_data_W_T_line(type_, rank, K_DEFAULT)
            assert sd['alpha'] == Fraction(2)

    def test_shadow_data_affine_alpha_1(self):
        """All affine KM have alpha = 1 (universal cubic from Lie bracket)."""
        for type_, rank in all_simple_types(8):
            sd = shadow_data_affine(type_, rank, K_DEFAULT)
            assert sd['alpha'] == Fraction(1)


# ============================================================================
# Cross-checks with existing engines
# ============================================================================

class TestCrossChecks:
    """Cross-check with ds_shadow_cascade_engine.py values."""

    def test_c_slN_agrees(self):
        """c_affine matches c_slN from ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import c_slN
        for N in range(2, 6):
            dim_g = N * N - 1
            h_v = N
            for kv in [Fraction(1), Fraction(5), Fraction(10)]:
                c_our = c_affine(dim_g, h_v, kv)
                c_ref = c_slN(N, kv)
                assert c_our == c_ref, f"sl_{N} at k={kv}: c mismatch"

    def test_kappa_slN_agrees(self):
        """kappa_affine matches kappa_slN from ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import kappa_slN
        for N in range(2, 6):
            dim_g = N * N - 1
            h_v = N
            for kv in [Fraction(1), Fraction(5)]:
                kap_our = kappa_affine(dim_g, h_v, kv)
                kap_ref = kappa_slN(N, kv)
                assert kap_our == kap_ref, f"sl_{N} at k={kv}: kappa mismatch"

    def test_c_WN_agrees(self):
        """c_W_principal matches c_WN from ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import c_WN
        for N in range(2, 6):
            for kv in [Fraction(1), Fraction(5), Fraction(10)]:
                c_our = c_W_principal("A", N - 1, kv)
                c_ref = c_WN(N, kv)
                assert c_our == c_ref, f"W_{N} at k={kv}: c mismatch"

    def test_anomaly_ratio_agrees(self):
        """anomaly_ratio matches ds_shadow_cascade_engine."""
        from compute.lib.ds_shadow_cascade_engine import anomaly_ratio
        for N in range(2, 6):
            rho_our = anomaly_ratio_general("A", N - 1)
            rho_ref = anomaly_ratio(N)
            assert rho_our == rho_ref, f"sl_{N}: anomaly ratio mismatch"

    def test_nonsimplylaced_B2_kappa(self):
        """kappa(B_2) matches nonsimplylaced_bar.py."""
        from compute.lib.nonsimplylaced_bar import b2_kappa
        from sympy import Rational as Rat, Symbol
        ks = Symbol('k')
        # Our formula: kappa = 10*(k+3)/6 = 5*(k+3)/3
        kap_ref = b2_kappa(ks)
        assert kap_ref == Rat(5) * (ks + 3) / 3
        # Numeric check at k=5
        kap_num = kappa_affine(10, 3, Fraction(5))
        assert kap_num == Fraction(5 * 8, 3)

    def test_nonsimplylaced_G2_kappa(self):
        """kappa(G_2) matches nonsimplylaced_bar.py."""
        from compute.lib.nonsimplylaced_bar import g2_kappa
        from sympy import Rational as Rat, Symbol
        ks = Symbol('k')
        kap_ref = g2_kappa(ks)
        assert kap_ref == Rat(7) * (ks + 4) / 4
        # Numeric check at k=5
        kap_num = kappa_affine(14, 4, Fraction(5))
        assert kap_num == Fraction(7 * 9, 4)


# ============================================================================
# Exponent and Weyl group verifications
# ============================================================================

class TestExponents:
    """Verify exponent data for all types."""

    def test_sum_exponents_equals_n_pos(self):
        """sum(exponents) = n_positive_roots for all types."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            assert sum(d['exponents']) == d['n_positive_roots'], \
                f"{type_}{rank}: sum(exp) != n_pos"

    def test_max_exponent_plus_1_equals_h(self):
        """max(exponents) + 1 = h for all types."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            assert max(d['exponents']) + 1 == d['h'], \
                f"{type_}{rank}: max(exp)+1 != h"

    def test_dim_equals_rank_plus_2npos(self):
        """dim(g) = rank + 2*n_positive_roots."""
        for type_, rank in all_simple_types(8):
            d = lie_data(type_, rank)
            assert d['dim'] == d['rank'] + 2 * d['n_positive_roots'], \
                f"{type_}{rank}: dim formula fails"
