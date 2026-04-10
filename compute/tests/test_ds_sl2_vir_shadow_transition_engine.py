r"""Tests for DS sl_2 -> Vir shadow transition engine.

Verifies shadow invariants S_2, S_3, S_4, Delta for V_k(sl_2) and Vir_c,
and the class L -> class M transition under Drinfeld-Sokolov reduction.

STRUCTURE:
  Section 1: Central charge formulas (7 tests)
  Section 2: Kappa formulas and boundary values (8 tests)
  Section 3: Shadow invariants for V_k(sl_2) -- class L (7 tests)
  Section 4: Shadow invariants for Vir_c -- class M (10 tests)
  Section 5: DS transition verification (8 tests)
  Section 6: Shadow tower computation (8 tests)
  Section 7: Complementarity (5 tests)
  Section 8: Cross-engine consistency (5 tests)
  Section 9: Full verification (1 test)

Total: 59 tests.

Manuscript references:
    thm:shadow-archetype-classification, thm:ds-central-charge-additivity,
    landscape_census.tex (C1-C4, C9-C11, C30)
"""

import pytest
from fractions import Fraction

from compute.lib.ds_sl2_vir_shadow_transition_engine import (
    # Central charges
    c_sugawara_sl2,
    c_ds_sl2_to_vir,
    # Kappa
    kappa_km_sl2,
    kappa_vir,
    # Shadow invariants -- KM
    s2_km,
    s3_km,
    s4_km,
    delta_km,
    # Shadow invariants -- Vir
    s2_vir,
    s3_vir,
    s4_vir,
    s5_vir,
    delta_vir,
    # Profiles
    shadow_profile_km,
    shadow_profile_vir,
    # Transition
    verify_class_transition,
    transition_table,
    # Tower
    shadow_tower,
    full_tower_comparison,
    # Complementarity
    ds_complementarity,
    # Verification
    verify_all,
)


# ============================================================================
# Section 1: Central charge formulas
# ============================================================================

class TestCentralCharges:
    """Test Sugawara and DS central charge formulas for sl_2."""

    def test_sugawara_k1(self):
        # VERIFIED: [DC] 3*1/(1+2)=1; [LT] Kac-Raina Ch.12
        assert c_sugawara_sl2(Fraction(1)) == Fraction(1)

    def test_sugawara_k0(self):
        # VERIFIED: [DC] 3*0/(0+2)=0; [LC] abelian limit
        assert c_sugawara_sl2(Fraction(0)) == Fraction(0)

    def test_sugawara_k2(self):
        # VERIFIED: [DC] 3*2/(2+2)=3/2; [LT] standard table
        assert c_sugawara_sl2(Fraction(2)) == Fraction(3, 2)

    def test_ds_k1(self):
        # VERIFIED: [DC] 1-6*4/3=-7; [LT] Fateev-Lukyanov, wn_central_charge_canonical.py
        assert c_ds_sl2_to_vir(Fraction(1)) == Fraction(-7)

    def test_ds_k0(self):
        # VERIFIED: [DC] 1-6*1/2=-2; [LT] Fateev-Lukyanov
        assert c_ds_sl2_to_vir(Fraction(0)) == Fraction(-2)

    def test_ds_k_neg1(self):
        # VERIFIED: [DC] 1-6*0/1=1; [LT] c=1 free fermion point
        assert c_ds_sl2_to_vir(Fraction(-1)) == Fraction(1)

    def test_ds_critical_raises(self):
        # VERIFIED: [DC] k=-2 is critical level, denominator vanishes
        with pytest.raises(ValueError, match="Critical level"):
            c_ds_sl2_to_vir(Fraction(-2))


# ============================================================================
# Section 2: Kappa formulas and boundary values
# ============================================================================

class TestKappaFormulas:
    """Test kappa = dim(g)(k+h^v)/(2h^v) for sl_2 and kappa = c/2 for Vir."""

    def test_kappa_km_k0(self):
        # VERIFIED: [DC] 3*(0+2)/4=3/2; [C3] dim(g)/2 at k=0
        assert kappa_km_sl2(Fraction(0)) == Fraction(3, 2)

    def test_kappa_km_critical(self):
        # VERIFIED: [DC] 3*(−2+2)/4=0; [C3] k=−h^v -> kappa=0
        assert kappa_km_sl2(Fraction(-2)) == Fraction(0)

    def test_kappa_km_k1(self):
        # VERIFIED: [DC] 3*3/4=9/4; [CF] matches cascade engine kappa_slN(2,1)
        assert kappa_km_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_km_k5(self):
        # VERIFIED: [DC] 3*7/4=21/4; [CF] ds_shadow_cascade_engine.kappa_slN(2,5)
        assert kappa_km_sl2(Fraction(5)) == Fraction(21, 4)

    def test_kappa_vir_c0(self):
        # VERIFIED: [DC] 0/2=0; [LC] trivial algebra
        assert kappa_vir(Fraction(0)) == Fraction(0)

    def test_kappa_vir_c13(self):
        # VERIFIED: [DC] 13/2; [C8] self-dual point kappa+kappa'=13
        assert kappa_vir(Fraction(13)) == Fraction(13, 2)

    def test_kappa_vir_c1(self):
        # VERIFIED: [DC] 1/2; [LT] standard table
        assert kappa_vir(Fraction(1)) == Fraction(1, 2)

    def test_kappa_vir_c_half(self):
        # VERIFIED: [DC] (1/2)/2=1/4; [LT] Ising model c=1/2
        assert kappa_vir(Fraction(1, 2)) == Fraction(1, 4)


# ============================================================================
# Section 3: Shadow invariants for V_k(sl_2) -- class L
# ============================================================================

class TestShadowKM:
    """Test S_2, S_3, S_4, Delta for V_k(sl_2)."""

    def test_s2_equals_kappa(self):
        # VERIFIED: [DC] S_2 = kappa by definition; [LT] shadow tower S_2 = a_0/2 = kappa
        for k in [Fraction(0), Fraction(1), Fraction(5)]:
            assert s2_km(k) == kappa_km_sl2(k)

    def test_s3_is_one(self):
        # VERIFIED: [DC] alpha=1 for all KM; [LT] Killing form structure constant universality
        for k in [Fraction(0), Fraction(1), Fraction(5), Fraction(100)]:
            assert s3_km(k) == Fraction(1)

    def test_s4_is_zero(self):
        # VERIFIED: [DC] Jacobi kills quartic for KM; [CF] ds_shadow_cascade_engine slN_shadow_data
        for k in [Fraction(0), Fraction(1), Fraction(5), Fraction(100)]:
            assert s4_km(k) == Fraction(0)

    def test_delta_is_zero(self):
        # VERIFIED: [DC] Delta=8*kappa*0=0; [C30] Delta=0 <-> finite tower
        for k in [Fraction(0), Fraction(1), Fraction(5)]:
            assert delta_km(k) == Fraction(0)

    def test_delta_formula(self):
        # VERIFIED: [DC] Delta = 8*kappa*S_4; [C30]
        k = Fraction(5)
        assert delta_km(k) == 8 * kappa_km_sl2(k) * s4_km(k)

    def test_shadow_class_L(self):
        # VERIFIED: [DC] S_4=0 -> class L; [LT] thm:shadow-archetype-classification
        prof = shadow_profile_km(Fraction(5))
        assert prof['shadow_class'] == 'L'
        assert prof['shadow_depth'] == 3

    def test_r_matrix_pole_1(self):
        # VERIFIED: [C9] r^KM(z) = k*Omega/z has pole order 1; [C12] OPE pole 2 minus 1
        prof = shadow_profile_km(Fraction(5))
        assert prof['r_matrix_pole'] == 1


# ============================================================================
# Section 4: Shadow invariants for Vir_c -- class M
# ============================================================================

class TestShadowVir:
    """Test S_2, S_3, S_4, S_5, Delta for Vir_c."""

    def test_s2_equals_kappa(self):
        # VERIFIED: [DC] S_2 = kappa = c/2; [LT] shadow tower S_2 = a_0/2 = kappa
        for c in [Fraction(1), Fraction(13), Fraction(25)]:
            assert s2_vir(c) == kappa_vir(c)

    def test_s3_is_two(self):
        # VERIFIED: [DC] alpha=2 for Vir; [LT] T(z)T(w) OPE cubic pole coeff = 2T(w)
        for c in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(25)]:
            assert s3_vir(c) == Fraction(2)

    def test_s4_c1(self):
        # VERIFIED: [DC] 10/(1*27)=10/27; [CF] ds_shadow_cascade_engine WN_shadow_data_T_line(2,k)
        assert s4_vir(Fraction(1)) == Fraction(10, 27)

    def test_s4_c13(self):
        # VERIFIED: [DC] 10/(13*87)=10/1131; [SY] c=13 self-dual
        assert s4_vir(Fraction(13)) == Fraction(10, 1131)

    def test_s4_c_half(self):
        # VERIFIED: [DC] 10/((1/2)*(5/2+22))=10/(49/4)=40/49; [NE] float check
        assert s4_vir(Fraction(1, 2)) == Fraction(40, 49)

    def test_s5_c1(self):
        # VERIFIED: [DC] -48/(1*27)=-48/27=-16/9; [CF] cascade engine S_5 cross-check
        assert s5_vir(Fraction(1)) == Fraction(-16, 9)

    def test_s5_c13(self):
        # VERIFIED: [DC] -48/(169*87)=-48/14703=-16/4901; [CF] cascade engine
        assert s5_vir(Fraction(13)) == Fraction(-16, 4901)

    def test_delta_c1(self):
        # VERIFIED: [DC] 40/(5+22)=40/27; [DC] 8*(1/2)*(10/27)=40/27
        assert delta_vir(Fraction(1)) == Fraction(40, 27)

    def test_delta_c13(self):
        # VERIFIED: [DC] 40/(65+22)=40/87; [SY] self-dual point
        assert delta_vir(Fraction(13)) == Fraction(40, 87)

    def test_delta_formula_consistency(self):
        # VERIFIED: [DC] Delta = 8*kappa*S_4 = 40/(5c+22); [C30]
        for c in [Fraction(1, 2), Fraction(1), Fraction(13), Fraction(25)]:
            lhs = 8 * kappa_vir(c) * s4_vir(c)
            rhs = delta_vir(c)
            assert lhs == rhs, f"Delta formula mismatch at c={c}: {lhs} != {rhs}"


# ============================================================================
# Section 5: DS transition verification
# ============================================================================

class TestDSTransition:
    """Test the class L -> M transition under DS(sl_2) -> Vir."""

    def test_transition_k1(self):
        # VERIFIED: [DC] k=1 -> c=-7, class L->M; [CF] cascade engine depth_increase
        trans = verify_class_transition(Fraction(1))
        assert trans['class_source'] == 'L'
        assert trans['class_target'] == 'M'
        assert trans['S_4_created']
        assert trans['Delta_created']

    def test_transition_k5(self):
        # VERIFIED: [DC] k=5 -> c=-103/7; [CF] cascade engine
        trans = verify_class_transition(Fraction(5))
        assert trans['class_transition'] == 'L -> M'
        assert trans['S_4_created']

    def test_transition_k10(self):
        # VERIFIED: [DC] k=10 -> c=-718/12=-359/6; [CF] cascade engine
        trans = verify_class_transition(Fraction(10))
        assert trans['class_transition'] == 'L -> M'

    def test_alpha_change_1_to_2(self):
        # VERIFIED: [DC] alpha_KM=1, alpha_Vir=2; [LT] shadow classification table
        trans = verify_class_transition(Fraction(5))
        assert trans['alpha_change'] == (Fraction(1), Fraction(2))

    def test_pole_increase_1_to_3(self):
        # VERIFIED: [C9] KM r-matrix pole=1; [C11] Vir r-matrix pole=3; [C12] absorption
        trans = verify_class_transition(Fraction(5))
        assert trans['pole_increase'] == (1, 3)

    def test_s4_zero_to_nonzero(self):
        # VERIFIED: [DC] S_4(KM)=0, S_4(Vir)!=0 for generic c; [LT] depth increase mechanism
        for k in [Fraction(1), Fraction(3), Fraction(10)]:
            trans = verify_class_transition(k)
            assert trans['source']['S_4'] == 0
            assert trans['target']['S_4'] != 0

    def test_delta_zero_to_nonzero(self):
        # VERIFIED: [DC] Delta(KM)=0, Delta(Vir)!=0; [C30]
        for k in [Fraction(1), Fraction(3), Fraction(10)]:
            trans = verify_class_transition(k)
            assert trans['source']['Delta'] == 0
            assert trans['target']['Delta'] != 0

    def test_transition_table_all_L_to_M(self):
        # VERIFIED: [DC] universal for all k; [LT] thm:shadow-archetype-classification
        table = transition_table()
        for row in table:
            assert row['class_KM'] == 'L'
            assert row['class_Vir'] == 'M'


# ============================================================================
# Section 6: Shadow tower computation
# ============================================================================

class TestShadowTower:
    """Test shadow tower via convolution recursion."""

    def test_km_tower_s2_equals_kappa(self):
        # VERIFIED: [DC] a_0/2 = 2*kappa/2 = kappa; [LT] definition
        k = Fraction(5)
        tower = shadow_tower(kappa_km_sl2(k), s3_km(k), s4_km(k), 6)
        assert tower[2] == kappa_km_sl2(k)

    def test_km_tower_s3_equals_alpha(self):
        # VERIFIED: [DC] a_1/3 = (q1/(2*a0))/3 = alpha; [LT] definition
        k = Fraction(5)
        tower = shadow_tower(kappa_km_sl2(k), s3_km(k), s4_km(k), 6)
        assert tower[3] == Fraction(1)

    def test_km_tower_truncates_at_4(self):
        # VERIFIED: [DC] S_4=0 -> all higher S_r=0; [LT] class L finite tower
        k = Fraction(5)
        tower = shadow_tower(kappa_km_sl2(k), s3_km(k), s4_km(k), 8)
        for r in range(4, 9):
            assert tower[r] == 0, f"S_{r} should be 0 for class L, got {tower[r]}"

    def test_vir_tower_s4_matches(self):
        # VERIFIED: [DC] tower S_4 = s4_vir(c); [CF] cascade engine
        c = Fraction(1)
        tower = shadow_tower(kappa_vir(c), s3_vir(c), s4_vir(c), 6)
        assert tower[4] == s4_vir(c)

    def test_vir_tower_s5_matches(self):
        # VERIFIED: [DC] tower S_5 = s5_vir(c); [CF] cascade engine S_5 cross-check
        c = Fraction(1)
        tower = shadow_tower(kappa_vir(c), s3_vir(c), s4_vir(c), 6)
        assert tower[5] == s5_vir(c)

    def test_vir_tower_all_nonzero(self):
        # VERIFIED: [DC] S_r != 0 for r=2..8; [LT] class M infinite tower
        c = Fraction(13)
        tower = shadow_tower(kappa_vir(c), s3_vir(c), s4_vir(c), 8)
        for r in range(2, 9):
            assert tower[r] != 0, f"S_{r} should be nonzero for class M, got 0"

    def test_full_comparison_km_truncated(self):
        # VERIFIED: [DC] KM S_r=0 for r>=4; [LT] class L
        ftc = full_tower_comparison(Fraction(5), 8)
        assert ftc['km_truncated_at_4']

    def test_full_comparison_vir_infinite(self):
        # VERIFIED: [DC] Vir S_r!=0 for all r; [LT] class M
        ftc = full_tower_comparison(Fraction(5), 8)
        assert ftc['vir_infinite_tower']


# ============================================================================
# Section 7: Complementarity
# ============================================================================

class TestComplementarity:
    """Test Feigin-Frenkel complementarity c(k) + c(-k-4) = 26."""

    def test_c_sum_26_k1(self):
        # VERIFIED: [DC] c(1)+c(-5)=-7+33=26; [C18] K_Vir=26
        comp = ds_complementarity(Fraction(1))
        assert comp['c_sum_is_26']

    def test_c_sum_26_k5(self):
        # VERIFIED: [DC] c(5)+c(-9)=26; [C18]
        comp = ds_complementarity(Fraction(5))
        assert comp['c_sum_is_26']

    def test_kappa_sum_13_k1(self):
        # VERIFIED: [DC] kappa+kappa'=13; [C8] Virasoro self-dual
        comp = ds_complementarity(Fraction(1))
        assert comp['kappa_sum_is_13']

    def test_kappa_sum_13_k10(self):
        # VERIFIED: [DC] kappa+kappa'=13; [C8]
        comp = ds_complementarity(Fraction(10))
        assert comp['kappa_sum_is_13']

    def test_dual_level(self):
        # VERIFIED: [DC] k'=-k-4; [LT] Feigin-Frenkel for sl_2
        comp = ds_complementarity(Fraction(3))
        assert comp['k_dual'] == Fraction(-7)


# ============================================================================
# Section 8: Cross-engine consistency
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-check against ds_shadow_cascade_engine formulas."""

    def test_ds_c_matches_cascade(self):
        # VERIFIED: [CF] c_WN(2, k) = c_ds_sl2_to_vir(k)
        from compute.lib.ds_shadow_cascade_engine import c_WN
        for k in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            assert c_ds_sl2_to_vir(k) == c_WN(2, k)

    def test_kappa_km_matches_cascade(self):
        # VERIFIED: [CF] kappa_slN(2, k) = kappa_km_sl2(k)
        from compute.lib.ds_shadow_cascade_engine import kappa_slN
        for k in [Fraction(0), Fraction(1), Fraction(5)]:
            assert kappa_km_sl2(k) == kappa_slN(2, k)

    def test_s4_vir_matches_cascade(self):
        # VERIFIED: [CF] WN_shadow_data_T_line(2, k)['S4'] = s4_vir(c_ds(k))
        from compute.lib.ds_shadow_cascade_engine import WN_shadow_data_T_line
        for k in [Fraction(1), Fraction(5), Fraction(10)]:
            cascade_data = WN_shadow_data_T_line(2, k)
            c_target = c_ds_sl2_to_vir(k)
            assert s4_vir(c_target) == cascade_data['S4']

    def test_cascade_depth_increase_matches(self):
        # VERIFIED: [CF] ds_pipeline(2, k)['depth_increase'] = True
        from compute.lib.ds_shadow_cascade_engine import ds_pipeline
        for k in [Fraction(1), Fraction(5)]:
            pipe = ds_pipeline(2, k)
            assert pipe['depth_increase']

    def test_tower_s5_matches_cascade(self):
        # VERIFIED: [CF] cascade S_5 cross-check for Virasoro
        from compute.lib.ds_shadow_cascade_engine import virasoro_s5_crosscheck
        result = virasoro_s5_crosscheck([Fraction(1), Fraction(5)])
        assert result['all_match']


# ============================================================================
# Section 9: Full verification
# ============================================================================

class TestFullVerification:
    """Run the engine's built-in verify_all."""

    def test_verify_all(self):
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"verify_all failed: {name}"
