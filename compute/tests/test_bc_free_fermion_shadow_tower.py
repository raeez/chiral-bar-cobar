"""Tests for the free fermion bc(lambda=1/2) shadow obstruction tower.

Verifies:
  - Central charge c = 1/2 and kappa = 1/4
  - Shadow tower S_2 = 1/4, S_3 = ... = S_8 = 0
  - Class G (Gaussian) with shadow depth 2
  - Critical discriminant Delta = 0
  - Shadow metric Q(t) = 1/4 (constant)
  - Contrast with Virasoro at c=1/2 (class M, S_4 = 40/49)

Ground truth:
  - free_fields.tex: Prop prop:fermion-shadow-invariants,
    Prop prop:fermion-shadow-metric
  - computational_methods.tex: Example ex:comp-virasoro-half (Virasoro contrast)
  - n2_free_field_shadow.py: kappa_fermion_pair() = 1/2 = 2 * 1/4
  - landscape_census_verification.py: kappa_free_fermion() = 1/4
"""

import importlib.util
import os

import pytest
from sympy import Rational

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'bc_free_fermion_shadow_tower',
    os.path.join(_lib_dir, 'bc_free_fermion_shadow_tower.py'),
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)


# ============================================================
# Central charge and kappa
# ============================================================

class TestParameters:
    def test_central_charge(self):
        """c = 1/2 for a single real fermion at lambda=1/2.

        # VERIFIED:
        #   [DC] c_bc(1/2) = 1 for complex pair; single real = 1/2
        #   [LT] Di Francesco et al, Ising model c = 1/2
        """
        assert _mod.central_charge() == Rational(1, 2)

    def test_conformal_weight(self):
        """h = 1/2 for the fermion generator.

        # VERIFIED:
        #   [DC] bc at lambda=1/2: h = lambda = 1/2
        #   [LT] free_fields.tex: weight-1/2 generator
        """
        assert _mod.conformal_weight() == Rational(1, 2)

    def test_kappa(self):
        """kappa = 1/4 = c/2.

        # VERIFIED:
        #   [DC] kappa = c/2 = (1/2)/2 = 1/4
        #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants
        #   [CF] landscape_census_verification.py: kappa_free_fermion() = 1/4
        """
        assert _mod.kappa() == Rational(1, 4)

    def test_kappa_equals_c_over_2(self):
        """kappa = c/2 (universal for single-generator algebras).

        # VERIFIED:
        #   [DC] 1/4 = (1/2)/2
        #   [LT] Thm thm:modular-characteristic: rho=1/2 for single-generator
        """
        assert _mod.kappa() == _mod.central_charge() / 2

    def test_ope_pole_order(self):
        """OPE pole order p = 1 (simple pole).

        # VERIFIED:
        #   [DC] psi(z)psi(w) ~ 1/(z-w), order 1
        #   [LT] free_fields.tex: OPE definition
        """
        assert _mod.ope_pole_order() == 1

    def test_r_matrix_pole_order(self):
        """r-matrix pole order = p - 1 = 0 (AP19: d-log absorption).

        # VERIFIED:
        #   [DC] 1 - 1 = 0
        #   [LT] AP19: pole_r = pole_OPE - 1
        """
        assert _mod.r_matrix_pole_order() == 0


# ============================================================
# Shadow tower S_2 through S_8
# ============================================================

class TestShadowTower:
    def test_S_2(self):
        """S_2 = kappa = 1/4.

        # VERIFIED:
        #   [DC] S_2 = kappa by definition
        #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants
        """
        assert _mod.S_2() == Rational(1, 4)

    def test_S_2_equals_kappa(self):
        """S_2 = kappa (identity at arity 2).

        # VERIFIED:
        #   [DC] S_2 = kappa by the shadow tower definition
        #   [LT] nonlinear_modular_shadows.tex
        """
        assert _mod.S_2() == _mod.kappa()

    def test_S_3(self):
        """S_3 = 0 (fermionic antisymmetry).

        # VERIFIED:
        #   [DC] Cyclic eigenvalue argument on 3-pt config space
        #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-S3
        """
        assert _mod.S_3() == Rational(0)

    def test_S_4(self):
        """S_4 = 0 (consequence of S_3 = 0).

        # VERIFIED:
        #   [DC] S_3=0 implies o_4=0 by cubic gauge triviality
        #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants item:fermion-S4
        """
        assert _mod.S_4() == Rational(0)

    def test_S_5(self):
        """S_5 = 0 (quintic obstruction vanishes).

        # VERIFIED:
        #   [DC] o^(5) = {S_3, S_4}_H = 0
        #   [SY] Class G: all S_r = 0 for r >= 3
        """
        assert _mod.S_5() == Rational(0)

    def test_S_6(self):
        """S_6 = 0 (induction on sewing products of zeros).

        # VERIFIED:
        #   [DC] All lower S_j = 0 for j >= 3 -> o^(6) = 0
        #   [SY] Class G: tower terminates at depth 2
        """
        assert _mod.S_6() == Rational(0)

    def test_S_7(self):
        """S_7 = 0.

        # VERIFIED:
        #   [DC] Induction from lower arities
        #   [SY] Class G termination
        """
        assert _mod.S_7() == Rational(0)

    def test_S_8(self):
        """S_8 = 0.

        # VERIFIED:
        #   [DC] Induction from lower arities
        #   [SY] Class G termination
        """
        assert _mod.S_8() == Rational(0)

    def test_tower_dict_completeness(self):
        """shadow_tower(8) returns S_2 through S_8 (7 entries)."""
        tower = _mod.shadow_tower(8)
        assert len(tower) == 7
        assert set(tower.keys()) == {2, 3, 4, 5, 6, 7, 8}

    def test_tower_only_S_2_nonzero(self):
        """In the tower, only S_2 is nonzero.

        # VERIFIED:
        #   [DC] Class G definition: S_r = 0 for r >= 3
        #   [LT] free_fields.tex: tower termination at r_max = 2
        """
        tower = _mod.shadow_tower(8)
        assert tower[2] == Rational(1, 4)
        for r in range(3, 9):
            assert tower[r] == Rational(0), f"S_{r} should be 0, got {tower[r]}"

    def test_tower_extensible(self):
        """shadow_tower with larger max_arity still gives zeros.

        # VERIFIED:
        #   [DC] Class G: all S_r = 0 for r >= 3 regardless of cutoff
        #   [SY] Tower termination is exact, not numerical
        """
        tower = _mod.shadow_tower(20)
        assert len(tower) == 19  # S_2 through S_20
        for r in range(3, 21):
            assert tower[r] == Rational(0)


# ============================================================
# Derived quantities
# ============================================================

class TestDerivedQuantities:
    def test_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 0.

        # VERIFIED:
        #   [DC] 8 * (1/4) * 0 = 0
        #   [LT] free_fields.tex Prop prop:fermion-shadow-invariants
        """
        assert _mod.critical_discriminant() == Rational(0)

    def test_shadow_metric(self):
        """Q(t) = (2*kappa)^2 = 1/4 (constant).

        # VERIFIED:
        #   [DC] (2 * 1/4)^2 = (1/2)^2 = 1/4
        #   [LT] free_fields.tex Prop prop:fermion-shadow-metric
        """
        assert _mod.shadow_metric() == Rational(1, 4)

    def test_shadow_generating_function(self):
        """H(t) = (1/2)*t^2, coefficient 1/2.

        # VERIFIED:
        #   [DC] sqrt(Q) = sqrt(1/4) = 1/2
        #   [LT] free_fields.tex: "H(t) = (1/2)*t^2"
        """
        assert _mod.shadow_generating_function_coefficient() == Rational(1, 2)


# ============================================================
# Classification
# ============================================================

class TestClassification:
    def test_shadow_class_G(self):
        """Shadow class is G (Gaussian).

        # VERIFIED:
        #   [DC] S_3=S_4=0 and Delta=0 -> G by definition
        #   [LT] free_fields.tex item:fermion-class
        #   [CF] Heisenberg is also class G (different mechanism)
        """
        assert _mod.shadow_class() == 'G'

    def test_shadow_depth_2(self):
        """Shadow depth r_max = 2 (tower terminates at arity 2).

        # VERIFIED:
        #   [DC] max r with S_r != 0 is r=2
        #   [LT] free_fields.tex: r_max = 2
        #   [CF] Heisenberg also depth 2
        """
        assert _mod.shadow_depth() == 2

    def test_theta_mc_element(self):
        """MC element is determined by kappa alone (no higher corrections).

        # VERIFIED:
        #   [DC] Theta = kappa * eta tensor Lambda, no higher terms
        #   [LT] free_fields.tex item:fermion-tower
        """
        theta = _mod.theta_mc_element()
        assert theta['kappa_coefficient'] == Rational(1, 4)
        assert theta['higher_corrections'] is False


# ============================================================
# Virasoro contrast
# ============================================================

class TestVirasoroContrast:
    """The free fermion and Virasoro at c=1/2 share kappa but differ in class.

    This is a critical distinction: same central charge, same kappa,
    but radically different shadow towers.
    """

    def test_same_central_charge(self):
        """Both have c = 1/2.

        # VERIFIED:
        #   [DC] Free fermion c=1/2; Vir minimal model c=1/2 (Ising)
        #   [LT] computational_methods.tex Example ex:comp-virasoro-half
        """
        contrast = _mod.virasoro_contrast()
        assert contrast['free_fermion']['c'] == Rational(1, 2)
        assert contrast['virasoro_c_half']['c'] == Rational(1, 2)

    def test_same_kappa(self):
        """Both have kappa = 1/4.

        # VERIFIED:
        #   [DC] kappa = c/2 = 1/4 for both
        #   [LT] computational_methods.tex: kappa = 1/4 at c=1/2
        """
        contrast = _mod.virasoro_contrast()
        assert contrast['free_fermion']['kappa'] == Rational(1, 4)
        assert contrast['virasoro_c_half']['kappa'] == Rational(1, 4)

    def test_different_S_3(self):
        """Free fermion S_3=0 vs Virasoro S_3=alpha=2.

        # VERIFIED:
        #   [DC] Vir alpha=2 from T_(1)T = 2T; fermion S_3=0 by antisymmetry
        #   [LT] computational_methods.tex: alpha=2; free_fields.tex: S_3=0
        """
        contrast = _mod.virasoro_contrast()
        assert contrast['free_fermion']['S_3'] == Rational(0)
        assert contrast['virasoro_c_half']['S_3'] == Rational(2)

    def test_different_S_4(self):
        """Free fermion S_4=0 vs Virasoro S_4=40/49.

        # VERIFIED:
        #   [DC] Vir: S_4 = 10/(c*(5c+22)) = 10/((1/2)*(49/2)) = 40/49
        #   [LT] computational_methods.tex: S_4=40/49 at c=1/2
        """
        contrast = _mod.virasoro_contrast()
        assert contrast['free_fermion']['S_4'] == Rational(0)
        assert contrast['virasoro_c_half']['S_4'] == Rational(40, 49)

    def test_different_class(self):
        """Free fermion class G vs Virasoro class M.

        # VERIFIED:
        #   [DC] Fermion: Delta=0, depth 2 -> G; Vir: Delta!=0, depth inf -> M
        #   [LT] free_fields.tex vs computational_methods.tex
        """
        contrast = _mod.virasoro_contrast()
        assert contrast['free_fermion']['class'] == 'G'
        assert contrast['virasoro_c_half']['class'] == 'M'

    def test_virasoro_S4_formula(self):
        """Cross-check Virasoro S_4 = 10/(c*(5c+22)) at c=1/2.

        # VERIFIED:
        #   [DC] 10/((1/2)*(5/2+22)) = 10/((1/2)*(49/2)) = 10/(49/4) = 40/49
        #   [LT] virasoro_quartic_contact.py: Q = 10/(c*(5c+22))
        """
        c = Rational(1, 2)
        S4_vir = Rational(10) / (c * (5 * c + 22))
        assert S4_vir == Rational(40, 49)

    def test_virasoro_discriminant_nonzero(self):
        """Virasoro Delta = 80/49 != 0 (class M, infinite tower).

        # VERIFIED:
        #   [DC] 8 * (1/4) * (40/49) = 80/49
        #   [LT] Delta != 0 -> class M
        """
        contrast = _mod.virasoro_contrast()
        delta_vir = contrast['virasoro_c_half']['Delta']
        assert delta_vir == 8 * Rational(1, 4) * Rational(40, 49)
        assert delta_vir == Rational(80, 49)
        assert delta_vir != 0


# ============================================================
# Internal verification suite
# ============================================================

class TestInternalVerification:
    def test_verify_all_passes(self):
        """All internal consistency checks pass."""
        results = _mod.verify_all()
        for name, ok in results.items():
            assert ok, f"Internal check failed: {name}"
