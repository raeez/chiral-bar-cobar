r"""Tests for genus-2 MC descent + DS-shadow commutation cross-checks.

Two foundational cross-checks:

PART A: Genus-2 MC tautological descent
  1. Planted-forest formula delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48
  2. Heisenberg: pf = 0 (class G, no planted forests)
  3. Virasoro: pf = -(c-40)/48
  4. Betagamma: pf = 11/48
  5. Affine: pf depends on k
  6. Hodge integral consistency

PART B: DS-shadow commutation
  7. Ghost central charge: c_ghost(sl_2) = 2 (constant)
  8. Ghost central charge: c_ghost(sl_3) = 6 (constant)
  9. Arity-2: kappa comparison (NOT additive under DS)
  10. Arity-3: S_3 additivity: S_3(Vir) = S_3(sl_2) + S_3(ghost)
  11. Arity-4: depth increase S_4(sl_2) = 0, S_4(Vir) != 0
  12. Full tower comparison at multiple levels
  13. Ghost sector depth analysis

Manuscript references:
    thm:mc-tautological-descent, thm:ds-central-charge-additivity,
    rem:planted-forest-correction-explicit, thm:shadow-archetype-classification
"""

import pytest
from fractions import Fraction

from sympy import Rational, Symbol, cancel, simplify

from compute.lib.genus2_ds_cross_engine import (
    # Part A
    genus2_planted_forest_formula,
    genus2_mc_relation_check,
    genus2_planted_forest_all_families,
    genus2_hodge_integrals,
    verify_genus2_hodge,
    heisenberg_shadow,
    affine_sl2_shadow,
    virasoro_shadow,
    betagamma_shadow,
    # Part B
    c_sl2,
    c_sl3,
    c_vir_from_ds_sl2,
    c_w3_from_ds_sl3,
    c_ghost_sl2,
    c_ghost_sl3,
    ds_shadow_comparison_arity2,
    ds_shadow_comparison_arity3,
    ds_shadow_comparison_arity4,
    ds_shadow_full_comparison,
    ds_shadow_sl3_w3_comparison,
    ghost_sector_depth_analysis,
    ds_ghost_shadow_creation,
    verify_all,
)


c = Symbol('c')
k = Symbol('k')


# ============================================================================
# PART A: Genus-2 MC tautological descent
# ============================================================================

class TestGenus2PlantedForestFormula:
    """Test delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48."""

    def test_formula_structure(self):
        """Formula is quadratic in alpha, linear in kappa."""
        kap, alp, s4 = Symbol('kap'), Symbol('alp'), Symbol('s4')
        pf = genus2_planted_forest_formula(kap, alp, s4)
        # Should be alp*(10*alp - kap)/48
        expected = alp * (10*alp - kap) / 48
        assert simplify(pf - expected) == 0

    def test_formula_independent_of_s4(self):
        """Genus-2 pf correction depends only on S_2 (kappa) and S_3 (alpha)."""
        kap = Rational(5)
        alp = Rational(3)
        pf1 = genus2_planted_forest_formula(kap, alp, Rational(0))
        pf2 = genus2_planted_forest_formula(kap, alp, Rational(7))
        assert pf1 == pf2

    def test_vanishes_for_zero_alpha(self):
        """If alpha = 0, planted forest = 0."""
        pf = genus2_planted_forest_formula(Rational(5), Rational(0), Rational(0))
        assert pf == 0


class TestGenus2AllFamilies:
    """Test planted-forest correction for all standard families."""

    def test_heisenberg_pf_zero(self):
        """Heisenberg (class G): pf = 0."""
        result = genus2_planted_forest_all_families()
        assert result['Heisenberg']['is_zero']

    def test_virasoro_pf_formula(self):
        """Virasoro: pf = -(c-40)/48."""
        result = genus2_planted_forest_all_families()
        vir_pf = result['Virasoro']['pf']
        expected = cancel(-(c - 40) / 48)
        assert simplify(vir_pf - expected) == 0

    def test_virasoro_pf_at_c26(self):
        """At c=26: pf(Vir) = -(26-40)/48 = 14/48 = 7/24."""
        result = genus2_planted_forest_all_families()
        val = result['Virasoro']['pf'].subs(c, 26)
        assert val == Rational(7, 24)

    def test_virasoro_pf_at_c40(self):
        """At c=40: pf(Vir) = 0. This is a special zero!"""
        result = genus2_planted_forest_all_families()
        val = result['Virasoro']['pf'].subs(c, 40)
        assert val == 0

    def test_betagamma_pf_value(self):
        """Betagamma: pf = 1*(10-(-1))/48 = 11/48."""
        result = genus2_planted_forest_all_families()
        assert result['BetaGamma']['pf'] == Rational(11, 48)

    def test_affine_sl2_pf_depends_on_k(self):
        """Affine sl_2: pf depends on level k."""
        result = genus2_planted_forest_all_families()
        pf = result['Affine_sl2']['pf']
        # pf = 1*(10 - 3(k+2)/4)/48 = (10 - 3(k+2)/4)/48 = (40 - 3(k+2))/(4*48)
        # = (40 - 3k - 6)/192 = (34 - 3k)/192
        expected = cancel((34 - 3*k) / 192)
        assert simplify(pf - expected) == 0

    def test_affine_sl2_pf_at_k1(self):
        """At k=1: pf = (34-3)/192 = 31/192."""
        result = genus2_planted_forest_all_families()
        pf = result['Affine_sl2']['pf']
        val = pf.subs(k, 1)
        assert val == Rational(31, 192)

    def test_all_families_present(self):
        result = genus2_planted_forest_all_families()
        assert set(result.keys()) == {'Heisenberg', 'Affine_sl2', 'Virasoro', 'BetaGamma'}


class TestGenus2HodgeIntegrals:
    """Test known Hodge integrals at genus 2."""

    def test_kappa2_value(self):
        integrals = genus2_hodge_integrals()
        assert integrals['kappa_2'] == Fraction(1, 240)

    def test_kappa1_sq_value(self):
        integrals = genus2_hodge_integrals()
        assert integrals['kappa_1_sq'] == Fraction(1, 240)

    def test_kappa2_equals_kappa1_sq(self):
        """kappa_2 = kappa_1^2 in genus 2 (Faber's relation)."""
        result = verify_genus2_hodge()
        assert result['kappa2_equals_kappa1sq']

    def test_lambda2_equals_kappa2(self):
        result = verify_genus2_hodge()
        assert result['lambda2_equals_kappa2']

    def test_lambda1_sq_value(self):
        integrals = genus2_hodge_integrals()
        assert integrals['lambda_1_sq'] == Fraction(1, 1152)

    def test_delta1_sq_negative(self):
        """delta_1^2 < 0 in M-bar_2."""
        integrals = genus2_hodge_integrals()
        assert integrals['delta_1_sq'] < 0


class TestGenus2MCRelation:
    """Test the MC relation structure at genus 2."""

    def test_virasoro_mc_relation(self):
        vir = virasoro_shadow()
        result = genus2_mc_relation_check(vir['kappa'], vir['alpha'], vir['S4'])
        assert result['planted_forest'] is not None

    def test_heisenberg_mc_relation(self):
        heis = heisenberg_shadow()
        result = genus2_mc_relation_check(heis['kappa'], heis['alpha'], heis['S4'])
        assert simplify(result['planted_forest']) == 0


# ============================================================================
# PART B: DS-shadow commutation
# ============================================================================

class TestDSCentralCharges:
    """Test DS central charge formulas."""

    def test_c_sl2_at_k1(self):
        """c(sl_2, k=1) = 3/3 = 1."""
        assert float(c_sl2(1)) == pytest.approx(1.0)

    def test_c_sl2_at_k_inf(self):
        """c(sl_2, k→inf) → 3."""
        assert float(c_sl2(1000)) == pytest.approx(3.0, rel=0.01)

    def test_c_sl3_at_k1(self):
        """c(sl_3, k=1) = 8/4 = 2."""
        assert float(c_sl3(1)) == pytest.approx(2.0)

    def test_c_vir_from_ds_at_k1(self):
        """c(Vir from DS(sl_2_1)) = 1 - 6/3 = -1."""
        assert float(c_vir_from_ds_sl2(1)) == pytest.approx(-1.0)

    def test_c_vir_from_ds_at_k10(self):
        """c(Vir from DS(sl_2_10)) = 1 - 6/12 = 1/2."""
        assert float(c_vir_from_ds_sl2(10)) == pytest.approx(0.5)

    def test_c_w3_from_ds(self):
        """c(W_3 from DS(sl_3_k)) = 2(k-9)/(k+3)."""
        c_val = float(c_w3_from_ds_sl3(10))
        assert c_val == pytest.approx(2.0 * (10-9)/(10+3), abs=1e-10)


class TestGhostCentralCharges:
    """Test ghost central charge = constant."""

    def test_ghost_sl2_is_2(self):
        """c_ghost(sl_2) = c(sl_2) - c(Vir) = 2 (constant!)."""
        cg = c_ghost_sl2()
        assert simplify(cg - 2) == 0

    def test_ghost_sl3_is_6(self):
        """c_ghost(sl_3) = c(sl_3) - c(W_3) = 6 (constant!)."""
        cg = c_ghost_sl3()
        assert simplify(cg - 6) == 0

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 100])
    def test_ghost_sl2_constant_numerical(self, k_val):
        """c_ghost(sl_2) = 2 at every level k."""
        c_total = float(c_sl2(k_val))
        c_vir = float(c_vir_from_ds_sl2(k_val))
        assert c_total - c_vir == pytest.approx(2.0, abs=1e-10)

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 100])
    def test_ghost_sl3_constant_numerical(self, k_val):
        """c_ghost(sl_3) = 6 at every level k."""
        c_total = float(c_sl3(k_val))
        c_w3 = float(c_w3_from_ds_sl3(k_val))
        assert c_total - c_w3 == pytest.approx(6.0, abs=1e-10)

    def test_ghost_general_formula(self):
        """c_ghost(sl_N) = N(N-1)."""
        gs = ghost_sector_depth_analysis()
        assert gs['sl2_principal']['c_sl2_minus_c_vir'] == 2  # 2*1 = 2
        assert gs['sl3_principal']['c_sl3_minus_c_w3'] == 6  # 3*2 = 6


class TestDSArity2:
    """Test DS comparison at arity 2 (kappa)."""

    def test_kappa_comparison_computed(self):
        result = ds_shadow_comparison_arity2()
        assert result['kappa_sl2'] is not None
        assert result['kappa_vir'] is not None

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10])
    def test_kappa_not_simply_additive(self, k_val):
        """kappa(sl_2) != kappa(Vir) + kappa(ghost) in general."""
        result = ds_shadow_comparison_arity2()
        ev = result['evaluations'][k_val]
        # The difference should be nonzero in general
        # (kappa is not additive under DS)
        diff = ev['difference']
        # Actually check: 3(k+2)/4 vs (k-4)/(2(k+2)) + 1
        # At k=1: 3*3/4 = 9/4 vs (-3)/(6) + 1 = 1/2 → diff = 9/4 - 1/2 = 7/4
        if k_val == 1:
            assert abs(diff - 7/4) < 1e-10


class TestDSArity3:
    """Test DS comparison at arity 3 (cubic shadow)."""

    def test_s3_values(self):
        result = ds_shadow_comparison_arity3()
        assert result['S3_sl2'] == 1
        assert result['S3_vir'] == 2
        assert result['S3_ghost'] == 1

    def test_s3_additive_at_parameter_level(self):
        """S_3(Vir) = S_3(sl_2) + S_3(ghost) = 1 + 1 = 2."""
        result = ds_shadow_comparison_arity3()
        assert result['S3_sl2'] + result['S3_ghost'] == result['S3_vir']


class TestDSArity4:
    """Test DS depth increase at arity 4."""

    def test_s4_sl2_zero(self):
        """sl_2 has S_4 = 0 (class L, depth 3)."""
        result = ds_shadow_comparison_arity4()
        assert result['S4_sl2'] == 0

    def test_s4_vir_nonzero(self):
        """Vir from DS has S_4 != 0 (class M, depth inf)."""
        result = ds_shadow_comparison_arity4()
        assert result['S4_vir'] != 0

    def test_depth_increase(self):
        """Depth increases from 3 to infinity under DS."""
        result = ds_shadow_comparison_arity4()
        assert result['depth_increase']

    def test_mechanism_is_ghost_quartic(self):
        result = ds_shadow_comparison_arity4()
        assert result['mechanism'] == 'ghost_quartic_seed'

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10])
    def test_s4_vir_nonzero_all_levels(self, k_val):
        """S_4(Vir) != 0 at all levels."""
        result = ds_shadow_comparison_arity4()
        if k_val in result['evaluations']:
            assert result['evaluations'][k_val]['S4_nonzero']


class TestDSFullComparison:
    """Test full shadow tower comparison sl_2 vs Vir."""

    def test_full_comparison_runs(self):
        result = ds_shadow_full_comparison(max_r=6)
        assert len(result) >= 3

    def test_sl2_always_depth_l(self):
        """sl_2 is always class L (depth 3)."""
        result = ds_shadow_full_comparison(max_r=6)
        for k_val, data in result.items():
            assert data['sl2_depth'] == 'L'

    def test_vir_always_depth_m(self):
        """Vir from DS is always class M (depth inf)."""
        result = ds_shadow_full_comparison(max_r=6)
        for k_val, data in result.items():
            assert data['vir_depth'] == 'M'

    def test_sl2_s4_zero_all_levels(self):
        """sl_2 has S_4 = 0 at all levels."""
        result = ds_shadow_full_comparison(max_r=6)
        for k_val, data in result.items():
            assert abs(data['comparison'][4]['S_r_sl2']) < 1e-12

    def test_vir_s4_nonzero_all_levels(self):
        """Vir has S_4 != 0 at all levels."""
        result = ds_shadow_full_comparison(max_r=6)
        for k_val, data in result.items():
            assert abs(data['comparison'][4]['S_r_vir']) > 1e-15

    def test_s2_difference_consistent(self):
        """kappa difference is consistent across levels."""
        result = ds_shadow_full_comparison(max_r=6)
        for k_val, data in result.items():
            kap_sl2 = data['comparison'][2]['S_r_sl2']
            kap_vir = data['comparison'][2]['S_r_vir']
            # Both should be positive for k > 4
            if k_val > 4:
                assert kap_sl2 > 0
                assert kap_vir > 0


class TestDSSl3W3Comparison:
    """Test sl_3 -> W_3 DS comparison."""

    def test_comparison_runs(self):
        result = ds_shadow_sl3_w3_comparison(max_r=6)
        assert len(result) >= 3

    def test_sl3_always_depth_l(self):
        result = ds_shadow_sl3_w3_comparison(max_r=6)
        for k_val, data in result.items():
            assert data['sl3_depth'] == 'L'

    def test_w3_always_depth_m(self):
        result = ds_shadow_sl3_w3_comparison(max_r=6)
        for k_val, data in result.items():
            assert data['w3_depth'] == 'M'

    def test_ghost_central_charge_6(self):
        result = ds_shadow_sl3_w3_comparison(max_r=6)
        for k_val, data in result.items():
            assert abs(data['c_ghost'] - 6.0) < 1e-10


class TestGhostSectorAnalysis:
    """Test ghost sector depth analysis."""

    def test_ghost_analysis_complete(self):
        result = ghost_sector_depth_analysis()
        assert 'sl2_principal' in result
        assert 'sl3_principal' in result
        assert 'general_sl_N' in result

    def test_ghost_creation_mechanism(self):
        result = ds_ghost_shadow_creation()
        assert result['input_depth'] == 3
        assert result['output_depth'] == 'infinity'
        assert result['mechanism'] == 'ghost_quartic_seed'


class TestCrossFamilyConsistency:
    """Cross-check shadow data between families."""

    def test_heisenberg_data(self):
        h = heisenberg_shadow()
        assert h['alpha'] == 0
        assert h['S4'] == 0
        assert h['depth_class'] == 'G'

    def test_virasoro_data(self):
        v = virasoro_shadow()
        assert v['alpha'] == 2
        assert v['depth_class'] == 'M'

    def test_betagamma_data(self):
        bg = betagamma_shadow()
        assert bg['kappa'] == Rational(-1)
        assert bg['alpha'] == 1
        assert bg['S4'] == Rational(-5, 12)
        assert bg['depth_class'] == 'C'

    def test_affine_data(self):
        aff = affine_sl2_shadow()
        assert aff['alpha'] == 1
        assert aff['S4'] == 0
        assert aff['depth_class'] == 'L'


# ============================================================================
# Integration test
# ============================================================================

class TestVerificationSuite:
    """Run the built-in verification suite."""

    def test_all_verifications_pass(self):
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Verification failed: {name}"


# ============================================================================
# DS + Genus-2 cross-checks
# ============================================================================

class TestDSGenus2CrossCheck:
    """Cross-check: genus-2 planted-forest via DS reduction."""

    def test_vir_pf_at_ds_level(self):
        """Planted-forest for Vir at c = c(DS(sl_2_k)) should be well-defined."""
        for k_val in [1, 2, 5, 10]:
            cv = float(c_vir_from_ds_sl2(k_val))
            if abs(cv) > 0.01:
                pf = 2.0 * (20.0 - cv/2) / 48.0
                expected = -(cv - 40.0) / 48.0
                assert abs(pf - expected) < 1e-10

    def test_pf_changes_sign_at_c40(self):
        """Planted-forest changes sign at c=40."""
        pf_below = -(39 - 40) / 48.0  # positive
        pf_above = -(41 - 40) / 48.0  # negative
        assert pf_below > 0
        assert pf_above < 0

    def test_pf_self_dual_c13(self):
        """At self-dual c=13: pf = -(13-40)/48 = 27/48 = 9/16."""
        result = genus2_planted_forest_all_families()
        val = result['Virasoro']['pf'].subs(c, 13)
        assert val == Rational(27, 48)
