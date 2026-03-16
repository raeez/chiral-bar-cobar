"""Tests for the affine sl_2 shadow tower computation.

Verifies:
  - Hessian = Killing form on Cartan line
  - Cubic shadow vanishes on Cartan (abelian subalgebra)
  - Cubic shadow nonzero on full sl_2 (Lie bracket)
  - Quartic contact = 0 (Jacobi identity)
  - Boundary quartic from cubic sewing
  - Genus loop cancellation on Cartan
  - Shadow tower termination at arity 3
  - Comparison with Virasoro (infinite tower)

Ground truth:
  - nonlinear_modular_shadows.tex: Thm thm:nms-finite-termination,
    Thm thm:nms-affine-cubic-normal-form, Cor cor:nms-affine-boundary-tree
"""

import pytest
from sympy import Rational, Symbol, simplify, factor

import importlib.util
import os

# Load modules
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec_aff = importlib.util.spec_from_file_location(
    'affine_sl2_shadow_tower',
    os.path.join(_lib_dir, 'affine_sl2_shadow_tower.py')
)
_aff = importlib.util.module_from_spec(_spec_aff)
_spec_aff.loader.exec_module(_aff)

_spec_tower = importlib.util.spec_from_file_location(
    'modular_shadow_tower',
    os.path.join(_lib_dir, 'modular_shadow_tower.py')
)
_tower = importlib.util.module_from_spec(_spec_tower)
_spec_tower.loader.exec_module(_tower)


k = Symbol('k')
c = Symbol('c')


# ============================================================
# Hessian tests
# ============================================================

class TestAffineHessian:
    def test_hessian_cartan(self):
        """Hessian on Cartan line = k (from <h|h> = 2k, so H = k*x^2)."""
        assert _aff.affine_hessian_cartan() == k

    def test_propagator_cartan(self):
        """Propagator = 1/k on Cartan line."""
        assert _aff.affine_propagator_cartan() == 1/k

    def test_hessian_positive_at_positive_level(self):
        """H > 0 for k > 0 (unitarity)."""
        for k_val in [1, 2, 3, 5, 10]:
            assert _aff.affine_hessian_cartan().subs(k, k_val) > 0

    def test_hessian_vanishes_at_zero_level(self):
        """H = 0 at k = 0 (trivial level)."""
        assert _aff.affine_hessian_cartan().subs(k, 0) == 0


# ============================================================
# Central charge tests
# ============================================================

class TestAffineCentralCharge:
    def test_sugawara_formula(self):
        """c = 3k/(k+2) for sl_2 with h^v = 2."""
        cc = _aff.affine_central_charge()
        assert simplify(cc - 3*k/(k+2)) == 0

    def test_c_at_k1(self):
        """c(k=1) = 1 (the SU(2)_1 WZW model)."""
        assert _aff.affine_central_charge().subs(k, 1) == 1

    def test_c_at_k2(self):
        """c(k=2) = 3/2 (the SU(2)_2 WZW model)."""
        assert _aff.affine_central_charge().subs(k, 2) == Rational(3, 2)

    def test_c_large_k_limit(self):
        """c -> 3 as k -> infinity (free field limit)."""
        from sympy import limit, oo
        cc = _aff.affine_central_charge()
        assert limit(cc, k, oo) == 3

    def test_dual_coxeter(self):
        """h^v = 2 for sl_2."""
        assert _aff.affine_dual_coxeter() == 2

    def test_dim_sl2(self):
        """dim(sl_2) = 3."""
        assert _aff.affine_dim() == 3


# ============================================================
# Cubic shadow tests
# ============================================================

class TestAffineCubic:
    def test_cubic_vanishes_on_cartan(self):
        """C(h,h,h) = 0 because [h,h] = 0."""
        assert _aff.affine_cubic_structure_constant() == 0

    def test_cubic_full_nonzero(self):
        """C(h,e,f) = 2k != 0 for the Lie bracket."""
        full = _aff.affine_cubic_full()
        assert full[('h', 'e', 'f')] == 2*k

    def test_cubic_antisymmetric(self):
        """C(x,y,z) is antisymmetric in y,z (from Lie bracket)."""
        full = _aff.affine_cubic_full()
        assert full[('h', 'e', 'f')] == -full[('h', 'f', 'e')]

    def test_cubic_cyclic_with_killing(self):
        """C(x,y,z) = kappa(x,[y,z]) is cyclic: C(x,y,z) = C(z,x,y)."""
        full = _aff.affine_cubic_full()
        # C(h,e,f) should equal C(f,h,e) (cyclic rotation)
        assert full[('h', 'e', 'f')] == full[('f', 'h', 'e')]

    def test_cubic_6_nonzero_components(self):
        """The cubic has exactly 6 nonzero components (permutations of h,e,f)."""
        full = _aff.affine_cubic_full()
        assert len(full) == 6


# ============================================================
# Quartic vanishing tests
# ============================================================

class TestAffineQuartic:
    def test_quartic_contact_vanishes(self):
        """Q^contact = 0 for Lie algebra (Jacobi identity)."""
        assert _aff.affine_quartic_contact() == 0

    def test_quartic_obstruction_vanishes(self):
        """o^(4) = 0 (no quartic obstruction for Lie algebras)."""
        assert _aff.affine_quartic_obstruction() == 0

    def test_quintic_obstruction_vanishes(self):
        """o^(5) = {C, Q}_H = 0 since Q = 0."""
        assert _aff.affine_quintic_obstruction() == 0


# ============================================================
# Boundary quartic tests
# ============================================================

class TestAffineBoundaryQuartic:
    def test_boundary_vanishes_on_cartan(self):
        """Boundary quartic = 0 on Cartan line (abelian)."""
        bq = _aff.affine_boundary_quartic_full()
        assert bq['cartan_line'] == 0

    def test_boundary_nonzero_off_diagonal(self):
        """Boundary quartic nonzero in h-e-f channels."""
        bq = _aff.affine_boundary_quartic_full()
        val = bq['h_e_e_f']
        assert val != 0
        assert val == 4*k

    def test_boundary_positive_at_positive_level(self):
        """Boundary quartic coefficient > 0 for k > 0."""
        bq = _aff.affine_boundary_quartic_full()
        for k_val in [1, 2, 5]:
            assert bq['h_e_e_f'].subs(k, k_val) > 0

    def test_boundary_linear_in_level(self):
        """Boundary quartic coefficient is linear in k."""
        bq = _aff.affine_boundary_quartic_full()
        val = bq['h_e_e_f']
        assert val.coeff(k, 1) == 4  # coefficient of k^1
        assert val.coeff(k, 0) == 0  # no k^0 term
        assert val.coeff(k, 2) == 0  # no k^2 term


# ============================================================
# Genus loop tests
# ============================================================

class TestAffineGenusLoop:
    def test_genus_loop_cubic_vanishes(self):
        """Lambda_P(C) = 0 on h-direction (e-f cancellation)."""
        assert _aff.affine_genus_loop_cubic() == 0

    def test_genus1_correction_vanishes(self):
        """delta H^(1) = 0 on Cartan line."""
        assert _aff.affine_genus1_hessian_correction() == 0

    def test_loop_ratio_vanishes(self):
        """rho^(1) = 0 (no genus-1 loop correction on Cartan)."""
        assert _aff.affine_loop_ratio() == 0


# ============================================================
# Shadow tower termination
# ============================================================

class TestAffineShadowTower:
    def test_terminates_at_arity_3(self):
        """Shadow tower terminates at arity 3 (Lie/tree level)."""
        assert _aff.shadow_termination_arity_affine() == 3

    def test_tower_structure(self):
        """Complete tower: H nonzero, C=0 on Cartan, Q=0, terminates."""
        tower = _aff.affine_shadow_tower()
        assert tower['arity_2_cartan'] == k
        assert tower['arity_3_cartan'] == 0
        assert tower['arity_4_cartan'] == 0
        assert tower['termination'] == 3
        assert tower['genus_1_correction_cartan'] == 0
        assert tower['loop_ratio_cartan'] == 0


# ============================================================
# Comparison with Virasoro
# ============================================================

class TestComparisonWithVirasoro:
    def test_virasoro_has_nonzero_quartic(self):
        """Virasoro Q^contact = 10/[c(5c+22)] != 0."""
        Q_vir = _tower.virasoro_quartic_contact()
        assert Q_vir != 0

    def test_affine_has_zero_quartic(self):
        """Affine Q^contact = 0 (contrast with Virasoro)."""
        assert _aff.affine_quartic_contact() == 0

    def test_virasoro_tower_infinite(self):
        """Virasoro shadow tower does NOT terminate."""
        terms = _tower.shadow_termination_arity()
        assert terms['virasoro'] is None

    def test_affine_tower_finite(self):
        """Affine shadow tower terminates at arity 3."""
        terms = _tower.shadow_termination_arity()
        assert terms['affine_sl2'] == 3

    def test_virasoro_loop_ratio_nonzero(self):
        """Virasoro rho^(1) = 240/[c^3(5c+22)] != 0."""
        rho = _tower.virasoro_loop_ratio()
        assert rho != 0

    def test_affine_loop_ratio_zero(self):
        """Affine rho^(1) = 0 (tower terminates before genus correction)."""
        assert _aff.affine_loop_ratio() == 0

    def test_structure_dichotomy(self):
        """The fundamental dichotomy: Lie algebras have finite towers,
        W-algebras (which are NOT Lie) have infinite towers.

        Affine sl_2 is a Lie algebra -> terminates.
        Virasoro has [T,T] = 2T (non-Lie: T_(1)T has conformal pole) -> infinite.
        """
        assert _aff.shadow_termination_arity_affine() == 3
        terms = _tower.shadow_termination_arity()
        assert terms['virasoro'] is None
