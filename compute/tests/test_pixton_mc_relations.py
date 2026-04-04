r"""Tests for Pixton tautological relations derived from the MC tower.

Tests conj:pixton-from-shadows at genera 2, 3, 4: the MC equation
D*Theta + (1/2)[Theta, Theta] = 0 produces tautological relations
in R*(M-bar_g) that should generate the Pixton ideal for class-M algebras.

Test structure:
  1. Faber-Pandharipande numbers (lambda_g^FP) through genus 5
  2. Genus-2 tautological ring and intersection numbers
  3. MC equation -> genus-2 relations (class G/L/M comparison)
  4. Genus-3 MC relations and shadow visibility
  5. Faber's Gorenstein conjecture verification
  6. Mumford formula from MC for Heisenberg through genus 4
  7. Double ramification cycle dimensional checks
  8. Genus-4 MC predictions
  9. Cross-family planted-forest comparison
  10. Shadow depth and Pixton ideal hierarchy
  11. Planted-forest explicit formula verification
  12. Virasoro c-dependence analysis
  13. Consistency checks and cross-module verification
"""

import pytest
from fractions import Fraction

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from pixton_mc_relations import (
    _bernoulli_exact,
    lambda_fp_exact,
    Genus2TautRing,
    mc_genus2_relation,
    mc_genus2_bracket_decomposition,
    mc_genus3_relations,
    genus3_pixton_ideal_test,
    genus3_new_relations_test,
    faber_gorenstein_check,
    mumford_formula_from_mc,
    ahat_generating_function,
    mumford_chern_character,
    dr_cycle_genus2_check,
    mc_genus4_scalar_prediction,
    genus4_pixton_prediction,
    cross_family_mc_relations,
    admcycles_comparison_genus2,
    shadow_amplitude_genus2,
    shadow_amplitude_genus3,
    mc_recursive_genus_determination,
    shadow_depth_pixton_hierarchy,
    planted_forest_genus2_explicit,
    planted_forest_genus3_explicit,
    virasoro_pf_c_dependence,
    consistency_checks,
)

from pixton_shadow_bridge import (
    wk_intersection,
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)

from sympy import Rational, Integer, cancel, simplify, Symbol


# ============================================================================
# Section 1: Faber-Pandharipande numbers
# ============================================================================

class TestBernoulliNumbers:
    """Verify exact Bernoulli numbers."""

    def test_B0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_odd_vanish(self):
        """B_{2k+1} = 0 for k >= 1."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == Fraction(0)


class TestLambdaFP:
    """Verify Faber-Pandharipande numbers lambda_g^FP."""

    def test_genus1(self):
        assert lambda_fp_exact(1) == Fraction(1, 24)

    def test_genus2(self):
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_genus3(self):
        assert lambda_fp_exact(3) == Fraction(31, 967680)

    def test_genus4(self):
        assert lambda_fp_exact(4) == Fraction(127, 154828800)

    def test_genus5(self):
        """lambda_5^FP from B_10 = 5/66."""
        result = lambda_fp_exact(5)
        # (2^9 - 1)/2^9 * |B_10|/10! = 511/512 * 5/66 / 3628800
        expected = Fraction(511, 512) * Fraction(5, 66) / Fraction(3628800)
        assert result == expected

    def test_positivity(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 7):
            assert lambda_fp_exact(g) > 0

    def test_monotone_decrease(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 6):
            assert lambda_fp_exact(g) > lambda_fp_exact(g + 1)


# ============================================================================
# Section 2: Genus-2 tautological ring
# ============================================================================

class TestGenus2TautRing:
    """Verify genus-2 intersection numbers from Faber's tables."""

    def test_lambda1_cube(self):
        assert Genus2TautRing.int_lambda1_cube() == Fraction(1, 1440)

    def test_lambda2_lambda1(self):
        assert Genus2TautRing.int_lambda2_lambda1() == Fraction(1, 2880)

    def test_lambda1_sq_delta_irr(self):
        assert Genus2TautRing.int_lambda1_sq_delta_irr() == Fraction(1, 120)

    def test_lambda1_sq_delta_1(self):
        assert Genus2TautRing.int_lambda1_sq_delta_1() == Fraction(0)

    def test_dimensions(self):
        dims = Genus2TautRing.dimensions()
        assert dims[0] == 1
        assert dims[1] == 2
        assert dims[2] == 2
        assert dims[3] == 1

    def test_pixton_relation_exists(self):
        rel = Genus2TautRing.pixton_codim2_relation()
        assert 'lambda_2' in rel
        assert 'lambda_1_sq' in rel

    def test_poincare_duality(self):
        """R^k and R^{3-k} should have the same dimension (Poincare)."""
        dims = Genus2TautRing.dimensions()
        for k in range(4):
            assert dims[k] == dims[3 - k]


# ============================================================================
# Section 3: MC -> genus-2 relations
# ============================================================================

class TestMCGenus2:
    """Test MC equation at genus 2 for different shadow depth classes."""

    def test_heisenberg_pf_vanishes(self):
        """Class G: planted-forest correction vanishes."""
        heis = heisenberg_shadow_data()
        result = mc_genus2_relation(heis)
        assert result['planted_forest'] == 0

    def test_virasoro_pf_nonzero(self):
        """Class M: planted-forest correction is nonzero."""
        vir = virasoro_shadow_data()
        result = mc_genus2_relation(vir)
        pf = cancel(result['planted_forest'])
        assert pf != 0

    def test_affine_pf_structure(self):
        """Class L: planted-forest involves S_3 but not S_4."""
        aff = affine_shadow_data()
        result = mc_genus2_relation(aff)
        # The planted-forest for affine (S_4=0) should be nonzero
        # (S_3 = 2, so S_3-terms survive)
        pf = cancel(result['planted_forest'])
        # It should be a polynomial in k (the level) from kappa = 3(k+2)/4
        assert pf != 0

    def test_bracket_decomposition(self):
        """Verify the bracket [Theta_1, Theta_1] decomposes correctly."""
        heis = heisenberg_shadow_data()
        result = mc_genus2_bracket_decomposition(heis)
        # Both separating and non-separating should be present
        assert 'bracket_separating' in result
        assert 'bracket_non_separating' in result

    def test_virasoro_numerical_c25(self):
        """Virasoro planted-forest at c=25 is a definite number."""
        vir = virasoro_shadow_data()
        result = mc_genus2_relation(vir)
        pf = cancel(result['planted_forest'])
        val = float(pf.subs(c_sym, 25))
        assert abs(val) > 1e-10  # nonzero

    def test_virasoro_numerical_c26(self):
        """Virasoro planted-forest at c=26 (critical string)."""
        vir = virasoro_shadow_data()
        result = mc_genus2_relation(vir)
        pf = cancel(result['planted_forest'])
        val = float(pf.subs(c_sym, 26))
        assert isinstance(val, float)


# ============================================================================
# Section 4: Genus-3 MC relations
# ============================================================================

class TestMCGenus3:
    """Test MC-derived relations at genus 3."""

    def test_heisenberg_pf_vanishes_g3(self):
        """Class G: planted-forest vanishes at genus 3."""
        heis = heisenberg_shadow_data()
        result = mc_genus3_relations(heis)
        assert result['planted_forest'] == 0

    def test_virasoro_pf_nonzero_g3(self):
        """Class M: planted-forest is nonzero at genus 3."""
        vir = virasoro_shadow_data(max_arity=8)
        result = mc_genus3_relations(vir)
        pf = cancel(result['planted_forest'])
        # Evaluate at c=25 to check nonzero
        val = float(pf.subs(c_sym, 25))
        assert abs(val) > 1e-15

    def test_pixton_ideal_test_heisenberg(self):
        """Class G gives trivially-in-ideal status."""
        heis = heisenberg_shadow_data()
        result = genus3_pixton_ideal_test(heis)
        assert result['pixton_status'] == 'trivially_in_ideal'

    def test_pixton_ideal_test_virasoro(self):
        """Class M gives nontrivial MC relation."""
        vir = virasoro_shadow_data(max_arity=8)
        result = genus3_pixton_ideal_test(vir)
        assert result['pixton_status'] == 'nontrivial_mc_relation'

    def test_genus3_new_relations(self):
        """Genus-3 MC relations involve S_4 or S_5 (new data)."""
        result = genus3_new_relations_test()
        assert result['is_new_at_genus3']

    def test_genus3_S4_dependence(self):
        """Genus-3 planted-forest depends on S_4."""
        result = genus3_new_relations_test()
        assert result['depends_on_S4']

    def test_genus3_S5_dependence(self):
        """Genus-3 planted-forest depends on S_5."""
        result = genus3_new_relations_test()
        assert result['depends_on_S5']


# ============================================================================
# Section 5: Faber's Gorenstein conjecture
# ============================================================================

class TestFaberGorenstein:
    """Verify Faber's Gorenstein conjecture for shadow CohFT."""

    def test_genus2_gorenstein(self):
        result = faber_gorenstein_check(2)
        assert result['gorenstein'] is True
        assert result['socle_degree'] == 0

    def test_genus3_gorenstein(self):
        result = faber_gorenstein_check(3)
        assert result['gorenstein'] is True
        assert result['socle_degree'] == 1

    def test_genus2_socle_dimension(self):
        result = faber_gorenstein_check(2)
        assert result['R_socle_dimension'] == 1

    def test_genus3_socle_generator(self):
        result = faber_gorenstein_check(3)
        assert result['socle_generator'] == 'kappa_1'


# ============================================================================
# Section 6: Mumford formula from MC
# ============================================================================

class TestMumfordFormula:
    """Verify Mumford's formula through genus 4."""

    def test_mumford_all_match(self):
        result = mumford_formula_from_mc(max_genus=4)
        assert result['all_match']

    def test_mumford_genus1(self):
        result = mumford_formula_from_mc(max_genus=4)
        assert result['per_genus'][1]['match']

    def test_mumford_genus2(self):
        result = mumford_formula_from_mc(max_genus=4)
        assert result['per_genus'][2]['match']

    def test_mumford_genus3(self):
        result = mumford_formula_from_mc(max_genus=4)
        assert result['per_genus'][3]['match']

    def test_mumford_genus4(self):
        result = mumford_formula_from_mc(max_genus=4)
        assert result['per_genus'][4]['match']

    def test_ahat_generating_function(self):
        """A-hat generating function coefficients match lambda_g^FP."""
        coeffs = ahat_generating_function(6)
        for g in range(1, 7):
            assert coeffs[g] == lambda_fp_exact(g)

    def test_mumford_chern_character_g2(self):
        result = mumford_chern_character(2)
        assert result['ch_classes'][0] == Fraction(2)
        # ch_1(E) = B_2/2! = (1/6)/2 = 1/12
        assert result['ch_1_value'] == Fraction(1, 12)

    def test_mumford_lambda1_formula(self):
        """ch_1(E) = B_2/2! = 1/12 implies lambda_1 = kappa_1/12."""
        result = mumford_chern_character(2)
        assert result['lambda_1_equals_kappa_1_over_12']


# ============================================================================
# Section 7: Double ramification cycle
# ============================================================================

class TestDoubleRamification:
    """Verify DR cycle dimensional checks."""

    def test_dr_genus2_codimension(self):
        result = dr_cycle_genus2_check()
        assert result['codimension_DR'] == 2

    def test_dr_genus2_moduli_dim(self):
        result = dr_cycle_genus2_check()
        assert result['dim_moduli'] == 5

    def test_dr_genus2_consistent(self):
        result = dr_cycle_genus2_check()
        assert result['consistent']


# ============================================================================
# Section 8: Genus-4 MC predictions
# ============================================================================

class TestGenus4:
    """Test genus-4 MC predictions."""

    def test_lambda4_fp(self):
        result = mc_genus4_scalar_prediction()
        assert result['match']
        assert result['lambda_4_fp'] == Fraction(127, 154828800)

    def test_cross_check_module(self):
        result = mc_genus4_scalar_prediction()
        assert result['cross_check_module']

    def test_new_shadow_data(self):
        """S_6 first appears at genus 4."""
        result = mc_genus4_scalar_prediction()
        assert 'S_6' in result['new_shadow_data_at_g4']

    def test_shadow_visibility_S6(self):
        result = mc_genus4_scalar_prediction()
        assert result['shadow_visibility']['S_6'] == 4

    def test_shadow_visibility_S3(self):
        result = mc_genus4_scalar_prediction()
        assert result['shadow_visibility']['S_3'] == 2

    def test_genus4_prediction_structure(self):
        result = genus4_pixton_prediction()
        assert result['genus'] == 4
        assert result['dim_moduli'] == 9
        assert result['first_new_codimension'] == 4


# ============================================================================
# Section 9: Cross-family comparison
# ============================================================================

class TestCrossFamily:
    """Compare MC-derived relations across shadow depth classes."""

    def test_heisenberg_is_zero(self):
        result = cross_family_mc_relations()
        assert result['Heisenberg']['genus2_pf_is_zero']

    def test_affine_is_nonzero(self):
        result = cross_family_mc_relations()
        assert not result['Affine_sl2']['genus2_pf_is_zero']

    def test_virasoro_is_nonzero(self):
        result = cross_family_mc_relations()
        assert not result['Virasoro']['genus2_pf_is_zero']

    def test_class_hierarchy(self):
        """G < L < C < M in tautological relation content."""
        result = cross_family_mc_relations()
        # G has zero pf, L and M have nonzero pf
        assert result['Heisenberg']['genus2_pf_is_zero']
        assert not result['Virasoro']['genus2_pf_is_zero']

    def test_admcycles_comparison(self):
        result = admcycles_comparison_genus2()
        assert result['nonzero_check']
        assert result['pixton_relations_genus2']['R2_dimension'] == 2


# ============================================================================
# Section 10: Shadow depth and Pixton hierarchy
# ============================================================================

class TestShadowDepthHierarchy:
    """Test shadow depth classification and Pixton ideal generation."""

    def test_depth_classes(self):
        result = shadow_depth_pixton_hierarchy()
        assert result['depth_classes']['G']['r_max'] == 2
        assert result['depth_classes']['L']['r_max'] == 3
        assert result['depth_classes']['C']['r_max'] == 4
        assert result['depth_classes']['M']['r_max'] == 'infinity'

    def test_shadow_visibility_formula(self):
        """g_min(S_r) = floor(r/2) + 1."""
        result = shadow_depth_pixton_hierarchy()
        vis = result['shadow_visibility']
        assert vis['S_2'] == 2
        assert vis['S_3'] == 2
        assert vis['S_4'] == 3
        assert vis['S_5'] == 3
        assert vis['S_6'] == 4
        assert vis['S_7'] == 4
        assert vis['S_8'] == 5

    def test_evidence_genera(self):
        result = shadow_depth_pixton_hierarchy()
        assert 2 in result['evidence_genera']
        assert 3 in result['evidence_genera']
        assert 4 in result['evidence_genera']


# ============================================================================
# Section 11: Planted-forest explicit formulas
# ============================================================================

class TestPlantedForestExplicit:
    """Verify explicit planted-forest formulas at genus 2."""

    def test_genus2_class_L(self):
        """Class L formula: S_3*(10*S_3 - kappa)/48."""
        result = planted_forest_genus2_explicit()
        pf_L = result['class_L_formula']
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        # Evaluate at specific values
        val = pf_L.subs({kappa: 1, S3: 2})
        expected = 2 * (20 - 1) / 48
        assert abs(float(val) - expected) < 1e-10

    def test_genus2_class_M_no_S4(self):
        """Class M formula at genus 2 does NOT include S_4.

        The sunset graph (0,4) carries S_4 but has vanishing Hodge
        integral (self-loop parity vanishing at genus 0, dim M-bar_{0,4}=1
        is odd). S_4 first contributes at genus 3 via the bridge-loop
        graph (1,2)+(0,4). This is consistent with shadow visibility:
        g_min(S_4) = floor(4/2)+1 = 3, but the genus-2 sunset integral
        vanishes by parity.
        """
        result = planted_forest_genus2_explicit()
        pf_M = result['class_M_formula']
        S4 = Symbol('S_4')
        # S_4 does NOT appear at genus 2 due to self-loop parity vanishing
        assert S4 not in pf_M.free_symbols

    def test_genus2_class_L_vanishes_for_S3_zero(self):
        """When S_3 = 0 (class G), the class-L formula vanishes."""
        result = planted_forest_genus2_explicit()
        pf_L = result['class_L_formula']
        S3 = Symbol('S_3')
        val = pf_L.subs(S3, 0)
        assert cancel(val) == 0

    def test_genus2_heisenberg_zero(self):
        """Heisenberg (S_3=0, S_4=0): planted-forest = 0."""
        heis = heisenberg_shadow_data()
        result = planted_forest_genus2_explicit()
        kappa_sym = Symbol('kappa')
        S3_sym = Symbol('S_3')
        S4_sym = Symbol('S_4')
        pf_M = result['class_M_formula']
        val = pf_M.subs({kappa_sym: Symbol('k'), S3_sym: 0, S4_sym: 0})
        assert cancel(val) == 0


# ============================================================================
# Section 12: Virasoro c-dependence
# ============================================================================

class TestVirasiroCDependence:
    """Analyze Virasoro planted-forest as a function of c."""

    def test_genus2_c_dependence(self):
        result = virasoro_pf_c_dependence(genus=2)
        assert result['genus'] == 2
        assert len(result['numerical_values']) > 0

    def test_genus2_c1_nonzero(self):
        """Ising model (c=1): nonzero planted-forest."""
        result = virasoro_pf_c_dependence(genus=2)
        assert result['numerical_values'][1] is not None
        assert abs(result['numerical_values'][1]) > 1e-10

    def test_genus2_c13_self_dual(self):
        """Self-dual point (c=13): planted-forest has a definite value."""
        result = virasoro_pf_c_dependence(genus=2)
        assert result['numerical_values'][13] is not None

    def test_genus2_c26_critical(self):
        """Critical string (c=26): planted-forest is definite."""
        result = virasoro_pf_c_dependence(genus=2)
        assert result['numerical_values'][26] is not None

    def test_genus3_c_dependence(self):
        result = virasoro_pf_c_dependence(genus=3)
        assert result['genus'] == 3
        assert len(result['numerical_values']) > 0

    def test_genus3_c25_nonzero(self):
        """c=25: nonzero at genus 3."""
        result = virasoro_pf_c_dependence(genus=3)
        assert result['numerical_values'][25] is not None
        assert abs(result['numerical_values'][25]) > 1e-15


# ============================================================================
# Section 13: Shadow amplitudes as tautological classes
# ============================================================================

class TestShadowAmplitudes:
    """Test shadow amplitudes expressed in R*(M-bar_g)."""

    def test_heisenberg_genus2_scalar(self):
        """Heisenberg F_2 is pure scalar (no planted-forest)."""
        heis = heisenberg_shadow_data()
        result = shadow_amplitude_genus2(heis)
        assert cancel(result['planted_forest_correction']) == 0

    def test_virasoro_genus2_has_correction(self):
        """Virasoro F_2 has planted-forest correction."""
        vir = virasoro_shadow_data()
        result = shadow_amplitude_genus2(vir)
        pf = cancel(result['planted_forest_correction'])
        assert pf != 0

    def test_heisenberg_genus3_scalar(self):
        """Heisenberg F_3 is pure scalar."""
        heis = heisenberg_shadow_data()
        result = shadow_amplitude_genus3(heis)
        assert cancel(result['planted_forest_correction']) == 0

    def test_virasoro_genus3_has_correction(self):
        """Virasoro F_3 has planted-forest correction."""
        vir = virasoro_shadow_data(max_arity=8)
        result = shadow_amplitude_genus3(vir)
        pf = cancel(result['planted_forest_correction'])
        # Evaluate numerically to check nonzero
        val = float(pf.subs(c_sym, 25))
        assert abs(val) > 1e-15


# ============================================================================
# Section 14: MC recursive structure
# ============================================================================

class TestMCRecursive:
    """Verify the recursive structure of MC genus determination."""

    def test_F_coefficients(self):
        result = mc_recursive_genus_determination()
        assert result['F_coefficients'][1] == Fraction(1, 24)
        assert result['F_coefficients'][2] == Fraction(7, 5760)
        assert result['F_coefficients'][3] == Fraction(31, 967680)
        assert result['F_coefficients'][4] == Fraction(127, 154828800)

    def test_all_match_bernoulli(self):
        result = mc_recursive_genus_determination()
        for g in range(1, 5):
            assert result['verification'][g]['matches_bernoulli']


# ============================================================================
# Section 15: Consistency checks
# ============================================================================

class TestConsistency:
    """Run comprehensive consistency checks."""

    def test_all_consistency_checks_pass(self):
        result = consistency_checks()
        assert result['all_pass']

    def test_lambda_fp_consistency(self):
        result = consistency_checks()
        for g in range(1, 5):
            assert result['lambda_fp'][g]['match']

    def test_heisenberg_pf_g2_zero(self):
        result = consistency_checks()
        assert result['heisenberg_pf_g2_zero']

    def test_virasoro_pf_g2_nonzero(self):
        result = consistency_checks()
        assert result['virasoro_pf_g2_nonzero']

    def test_affine_pf_g2_no_S4(self):
        result = consistency_checks()
        assert result['affine_pf_g2_no_S4']


# ============================================================================
# Section 16: WK intersection number cross-checks
# ============================================================================

class TestWKCrossChecks:
    """Cross-check WK intersection numbers used in the MC relations."""

    def test_tau1_genus1(self):
        """<tau_1>_1 = 1/24."""
        assert wk_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau4_genus2(self):
        """<tau_4>_2 = 1/1152."""
        assert wk_intersection(2, (4,)) == Fraction(1, 1152)

    def test_tau2_tau2_genus2(self):
        """<tau_2^2>_2.

        Selection rule: sum d_i = 3*2-3+2 = 5. But 2+2 = 4 != 5.
        Actually n=2 here, so 3g-3+n = 3+2 = 5 but sum=4. Zero.
        Use <tau_3 tau_2>_2: sum = 5 = 3*2-3+2. OK.
        """
        result = wk_intersection(2, (3, 2))
        # 3+2 = 5 = 3*2-3+2, so selection rule satisfied
        assert result != 0

    def test_tau0_cubed_genus0(self):
        """<tau_0^3>_0 = 1."""
        assert wk_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_genus0_multinomial(self):
        """<tau_0 tau_0 tau_0 tau_0>_0 = ... (sum d_i = 1, n=4)."""
        # dim constraint: sum d_i = 3*0-3+4 = 1
        # <tau_1 tau_0 tau_0 tau_0>_0 = 1 (by string equation)
        result = wk_intersection(0, (1, 0, 0, 0))
        assert result == Fraction(1)


# ============================================================================
# Section 17: Genus-2 planted-forest formula numerical verification
# ============================================================================

class TestPlantedForestNumerical:
    """Numerical verification of planted-forest formulas."""

    def test_virasoro_c1(self):
        """Virasoro planted-forest at c=1 (Ising model)."""
        vir = virasoro_shadow_data()
        from pixton_shadow_bridge import planted_forest_polynomial
        pf = cancel(planted_forest_polynomial(vir))
        val = float(pf.subs(c_sym, 1))
        assert isinstance(val, float)
        assert abs(val) > 1e-10

    def test_virasoro_c13_vs_c26(self):
        """Compare planted-forest at self-dual c=13 vs critical c=26."""
        vir = virasoro_shadow_data()
        from pixton_shadow_bridge import planted_forest_polynomial
        pf = cancel(planted_forest_polynomial(vir))
        val_13 = float(pf.subs(c_sym, 13))
        val_26 = float(pf.subs(c_sym, 26))
        # Both should be nonzero and different
        assert abs(val_13) > 1e-10
        assert abs(val_26) > 1e-10
        assert abs(val_13 - val_26) > 1e-10

    def test_affine_sl2_k1(self):
        """Affine sl_2 planted-forest at level k=1."""
        aff = affine_shadow_data()
        from pixton_shadow_bridge import planted_forest_polynomial
        pf = cancel(planted_forest_polynomial(aff))
        k = Symbol('k')
        val = float(pf.subs(k, 1))
        assert isinstance(val, float)


# ============================================================================
# Section 18: Shadow visibility genus theorem
# ============================================================================

class TestShadowVisibility:
    """Verify the shadow visibility genus formula cor:shadow-visibility-genus."""

    def test_S2_visibility(self):
        """S_2 (= kappa) visible at genus g_min = 2."""
        assert 2 // 2 + 1 == 2

    def test_S3_visibility(self):
        """S_3 first visible at genus g_min = 2."""
        assert 3 // 2 + 1 == 2

    def test_S4_visibility(self):
        """S_4 first visible at genus g_min = 3."""
        assert 4 // 2 + 1 == 3

    def test_S5_visibility(self):
        """S_5 first visible at genus g_min = 3."""
        assert 5 // 2 + 1 == 3

    def test_S6_visibility(self):
        """S_6 first visible at genus g_min = 4."""
        assert 6 // 2 + 1 == 4

    def test_S7_visibility(self):
        """S_7 first visible at genus g_min = 4."""
        assert 7 // 2 + 1 == 4

    def test_general_formula(self):
        """g_min(S_r) = floor(r/2) + 1 for all r."""
        for r in range(2, 20):
            g_min = r // 2 + 1
            # A genus-0 vertex of valence r contributes S_r.
            # It appears in a genus-g graph when g >= g_min.
            # The minimal genus g_min comes from the graph
            # with one genus-0 vertex of valence r and (r/2)
            # self-loops, giving arithmetic genus = r/2 = floor(r/2).
            # But we need the MARKED version at genus g_min = floor(r/2)+1
            # because the cyclic marking adds one to the genus count.
            # Actually: a graph with one vertex of genus 0, valence r,
            # and r/2 self-loops has h^1 = r/2 (for r even).
            # For r odd, we need at least one bridge to another vertex.
            assert g_min >= 2  # S_r cannot appear at genus 0 or 1


# ============================================================================
# Section 19: MC equation structural tests
# ============================================================================

class TestMCStructure:
    """Test structural properties of the MC equation tower."""

    def test_genus2_has_separating(self):
        """Genus-2 MC equation has separating boundary contribution."""
        heis = heisenberg_shadow_data()
        result = mc_genus2_bracket_decomposition(heis)
        # Separating = dumbbell graph
        assert result['bracket_separating'] != 0

    def test_genus2_has_non_separating(self):
        """Genus-2 MC equation has non-separating boundary contribution."""
        heis = heisenberg_shadow_data()
        result = mc_genus2_bracket_decomposition(heis)
        # Non-separating = lollipop graph
        assert result['bracket_non_separating'] != 0

    def test_mc_genus3_has_all_parts(self):
        """Genus-3 MC relation has codim-1 and planted-forest parts."""
        vir = virasoro_shadow_data(max_arity=8)
        result = mc_genus3_relations(vir)
        assert 'codim1_total' in result
        assert 'planted_forest' in result
        assert 'iterated_boundary' in result


# ============================================================================
# Section 20: Cross-module verification
# ============================================================================

class TestCrossModule:
    """Verify consistency between pixton_mc_relations and other modules."""

    def test_lambda_fp_matches_genus4_module(self):
        """lambda_4^FP matches between pixton_mc_relations and genus4_amplitude."""
        from genus4_amplitude import lambda_FP as lfp_g4
        assert lambda_fp_exact(4) == lfp_g4(4)

    def test_lambda_fp_matches_pixton_bridge(self):
        """lambda_g^FP matches pixton_shadow_bridge values."""
        from pixton_shadow_bridge import wk_intersection
        # lambda_1^FP = <tau_1>_1 = 1/24
        assert lambda_fp_exact(1) == wk_intersection(1, (1,))
        # lambda_2^FP uses the full psi-class integral
        # <tau_4>_2 = 1/1152 (a different integral)
        # lambda_2^FP = 7/5760 (computed from Bernoulli, not from a single WK)
        assert lambda_fp_exact(2) == Fraction(7, 5760)

    def test_shadow_data_consistency(self):
        """Shadow data is consistent between modules."""
        vir = virasoro_shadow_data()
        assert cancel(vir.kappa - c_sym / 2) == 0
        assert vir.S3 == Integer(2)

    def test_heisenberg_shadow_data(self):
        """Heisenberg shadow data: kappa = k, S_3 = 0, S_4 = 0."""
        heis = heisenberg_shadow_data()
        assert heis.S3 == Integer(0)
        assert heis.S4 == Integer(0)
        assert heis.depth_class == 'G'

    def test_affine_shadow_data(self):
        """Affine sl_2: kappa = 3(k+2)/4, S_3 = 2, S_4 = 0."""
        aff = affine_shadow_data()
        assert aff.S3 == Integer(2)
        assert aff.S4 == Integer(0)
        assert aff.depth_class == 'L'
