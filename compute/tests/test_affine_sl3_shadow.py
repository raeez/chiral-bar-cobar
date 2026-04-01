r"""Tests for the affine sl_3 shadow tower and r-matrix.

Verifies:
  - kappa(sl_3_k) = 4(k+3)/3 (modular characteristic)
  - S_3 = 1 (cubic shadow, universal for KM)
  - S_4 = 0 (quartic killed by Jacobi identity)
  - Delta = 0 (critical discriminant)
  - Class L assignment (depth 3, tower terminates at arity 3)
  - Shadow metric is a perfect square (class L property)
  - S_r = 0 for all r >= 4 (termination)
  - Koszul duality: k' = -k-6, kappa + kappa' = 0, c + c' = 16
  - F_1 = (k+3)/18, F_1 complementarity
  - r-matrix r(z) = Omega/z where Omega = P - I/3
  - Classical Yang-Baxter equation (CYBE)
  - Quantum Yang-Baxter equation (YBE) for Yang R-matrix
  - Cubic shadow nonzero from structure constants
  - Jacobi identity kills quartic obstruction

Ground truth:
  - kac_moody.tex: thm:sl3-genus1-curvature, rem:sl3-universality,
    thm:affine-cubic-normal-form, cor:affine-postnikov-termination
  - landscape_census.tex: kappa formula
  - discriminant_atlas_complete.py: alpha = 1 universal
  - yangian_rmatrix_sl3.py: Casimir, YBE
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify

import importlib.util
import os

# Load the module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'affine_sl3_shadow',
    os.path.join(_lib_dir, 'affine_sl3_shadow.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

k = Symbol('k')


# ============================================================
# kappa tests
# ============================================================

class TestKappa:
    def test_kappa_formula(self):
        """kappa = 4(k+3)/3 = dim(sl_3)(k+h^vee)/(2*h^vee)."""
        kp = _mod.sl3_kappa()
        expected = Rational(4, 3) * (k + 3)
        assert simplify(kp - expected) == 0

    def test_kappa_at_k1(self):
        """kappa(k=1) = 4*4/3 = 16/3."""
        kp = _mod.sl3_kappa(1)
        assert kp == Rational(16, 3)

    def test_kappa_at_k2(self):
        """kappa(k=2) = 4*5/3 = 20/3."""
        kp = _mod.sl3_kappa(2)
        assert kp == Rational(20, 3)

    def test_kappa_at_critical_level(self):
        """kappa(k=-3) = 0 (critical level, uncurved)."""
        kp = _mod.sl3_kappa(-3)
        assert kp == 0

    def test_kappa_from_dim_and_hvee(self):
        """kappa = dim(g)*(k+h^vee)/(2*h^vee) = 8*(k+3)/6."""
        kp = _mod.sl3_kappa()
        from_formula = Rational(8) * (k + 3) / 6
        assert simplify(kp - from_formula) == 0

    def test_kappa_positive_at_positive_level(self):
        """kappa > 0 for k > -3."""
        for k_val in [1, 2, 5, 10, 100]:
            assert _mod.sl3_kappa(k_val) > 0


# ============================================================
# Central charge tests
# ============================================================

class TestCentralCharge:
    def test_sugawara(self):
        """c = 8k/(k+3) for sl_3-hat_k."""
        cc = _mod.sl3_central_charge()
        expected = 8 * k / (k + 3)
        assert simplify(cc - expected) == 0

    def test_c_at_k1(self):
        """c(k=1) = 8/4 = 2."""
        assert _mod.sl3_central_charge(1) == 2

    def test_c_at_k3(self):
        """c(k=3) = 24/6 = 4."""
        assert _mod.sl3_central_charge(3) == 4

    def test_c_large_k(self):
        """c -> 8 as k -> infinity (free-field limit, 8 free currents)."""
        from sympy import limit, oo
        cc = _mod.sl3_central_charge()
        assert limit(cc, k, oo) == 8


# ============================================================
# Koszul duality tests
# ============================================================

class TestKoszulDuality:
    def test_dual_level(self):
        """k' = -k - 6 for sl_3 (h^vee = 3)."""
        kd = _mod.sl3_dual_level()
        assert simplify(kd - (-k - 6)) == 0

    def test_kappa_anti_symmetry_symbolic(self):
        """kappa(k) + kappa(-k-6) = 0 symbolically."""
        assert _mod.verify_kappa_anti_symmetry() is True

    def test_kappa_anti_symmetry_numeric(self):
        """kappa(k) + kappa(-k-6) = 0 at k=1, 2, 5."""
        for k_val in [1, 2, 5]:
            assert _mod.verify_kappa_anti_symmetry(k_val) is True

    def test_central_charge_sum(self):
        """c(k) + c(-k-6) = 2*dim(sl_3) = 16."""
        assert _mod.verify_central_charge_sum() is True

    def test_central_charge_sum_numeric(self):
        """c + c' = 16 at k=1, 2, 5."""
        for k_val in [1, 2, 5]:
            assert _mod.verify_central_charge_sum(k_val) is True

    def test_involutivity(self):
        """(k')' = k: the dual of the dual is the original."""
        kd = _mod.sl3_dual_level()
        kdd = _mod.sl3_dual_level(kd)
        assert simplify(kdd - k) == 0


# ============================================================
# Shadow tower coefficient tests
# ============================================================

class TestShadowCoefficients:
    def test_S3_equals_1(self):
        """S_3 = 1 (universal for all affine KM)."""
        assert _mod.sl3_cubic_shadow() == 1

    def test_S4_equals_0(self):
        """S_4 = 0 (Jacobi identity kills quartic)."""
        assert _mod.sl3_quartic_shadow() == 0

    def test_discriminant_zero(self):
        """Delta = 8*kappa*S_4 = 0."""
        assert _mod.sl3_discriminant() == 0


# ============================================================
# Depth classification tests
# ============================================================

class TestDepthClassification:
    def test_class_L(self):
        """sl_3-hat is class L (depth 3)."""
        dc, depth = _mod.verify_class_L()
        assert dc == 'L'
        assert depth == 3

    def test_termination_k1(self):
        """S_r = 0 for r >= 4 at k = 1."""
        assert _mod.verify_termination(k_val=1, check_arity=15) is True

    def test_termination_k5(self):
        """S_r = 0 for r >= 4 at k = 5."""
        assert _mod.verify_termination(k_val=5, check_arity=15) is True

    def test_termination_k10(self):
        """S_r = 0 for r >= 4 at k = 10."""
        assert _mod.verify_termination(k_val=10, check_arity=15) is True

    def test_S2_equals_kappa(self):
        """S_2 in the tower equals kappa at k = 1."""
        tower = _mod.sl3_shadow_tower_numeric(1.0, max_arity=5)
        kappa_expected = 4.0 * (1.0 + 3.0) / 3.0
        sc2 = tower.coefficients[2]
        assert abs(sc2.numerical - kappa_expected) < 1e-10

    def test_S3_in_tower(self):
        """S_3 in the recursive tower equals 1 at k = 1."""
        tower = _mod.sl3_shadow_tower_numeric(1.0, max_arity=5)
        sc3 = tower.coefficients[3]
        assert abs(sc3.numerical - 1.0) < 1e-10

    def test_S4_through_S10_zero(self):
        """S_4 through S_10 are all zero (class L termination)."""
        tower = _mod.sl3_shadow_tower_numeric(1.0, max_arity=10)
        for r in range(4, 11):
            sc = tower.coefficients.get(r)
            assert sc is not None
            assert abs(sc.numerical) < 1e-12, f"S_{r} = {sc.numerical} != 0"


# ============================================================
# Shadow metric tests
# ============================================================

class TestShadowMetric:
    def test_perfect_square(self):
        """Q_L(t) is a perfect square for class L."""
        assert _mod.verify_perfect_square() is True

    def test_perfect_square_numeric(self):
        """Q_L(t) perfect square at k = 1, 5, 10."""
        for k_val in [1, 5, 10]:
            assert _mod.verify_perfect_square(k_val) is True

    def test_q0(self):
        """q_0 = 4*kappa^2."""
        q0, q1, q2, Delta = _mod.sl3_shadow_metric()
        kappa_val = _mod.sl3_kappa()
        assert simplify(q0 - 4 * kappa_val**2) == 0

    def test_q1(self):
        """q_1 = 12*kappa*alpha = 12*kappa*1 = 12*kappa."""
        q0, q1, q2, Delta = _mod.sl3_shadow_metric()
        kappa_val = _mod.sl3_kappa()
        assert simplify(q1 - 12 * kappa_val) == 0

    def test_q2(self):
        """q_2 = 9*alpha^2 + 16*kappa*S_4 = 9*1 + 0 = 9."""
        q0, q1, q2, Delta = _mod.sl3_shadow_metric()
        assert simplify(q2 - 9) == 0


# ============================================================
# F_1 tests
# ============================================================

class TestF1:
    def test_F1_formula(self):
        """F_1 = kappa/24 = (k+3)/18."""
        f1 = _mod.sl3_F1()
        expected = (k + 3) / 18
        assert simplify(f1 - expected) == 0

    def test_F1_at_k1(self):
        """F_1(k=1) = 4/18 = 2/9."""
        f1 = _mod.sl3_F1(1)
        assert f1 == Rational(2, 9)

    def test_F1_at_critical(self):
        """F_1(k=-3) = 0 (critical level)."""
        f1 = _mod.sl3_F1(-3)
        assert f1 == 0

    def test_F1_complementarity(self):
        """F_1(k) + F_1(-k-6) = 0."""
        assert _mod.verify_F1_complementarity() is True

    def test_F1_complementarity_numeric(self):
        """F_1 complementarity at k = 1, 2, 5."""
        for k_val in [1, 2, 5]:
            assert _mod.verify_F1_complementarity(k_val) is True


# ============================================================
# Casimir and r-matrix tests
# ============================================================

class TestCasimir:
    def test_casimir_identity(self):
        """Omega = P - I/3 on V tensor V."""
        err = _mod.verify_casimir_is_P_minus_I_over_N()
        assert err < 1e-10

    def test_r_matrix_pole_order(self):
        """r(z) = Omega/z has a single pole at z = 0 (AP19)."""
        import numpy as np
        r1 = _mod.sl3_r_matrix(1.0)
        r2 = _mod.sl3_r_matrix(2.0)
        # r(z) = Omega/z, so z*r(z) = Omega (constant)
        Omega_from_r1 = 1.0 * r1
        Omega_from_r2 = 2.0 * r2
        assert np.linalg.norm(Omega_from_r1 - Omega_from_r2) < 1e-10


# ============================================================
# Classical Yang-Baxter equation tests
# ============================================================

class TestCYBE:
    def test_cybe_generic(self):
        """CYBE at u=1.0, v=2.0."""
        err = _mod.verify_cybe(1.0, 2.0)
        assert err < 1e-10, f"CYBE residual = {err}"

    def test_cybe_varied_params(self):
        """CYBE at several spectral parameter values."""
        test_cases = [
            (0.5, 1.5),
            (1.0, 3.0),
            (2.0, 0.7),
            (0.3, 0.9),
            (5.0, 7.0),
        ]
        for u, v in test_cases:
            err = _mod.verify_cybe(u, v)
            assert err < 1e-9, f"CYBE failed at u={u}, v={v}: residual = {err}"

    def test_cybe_complex_params(self):
        """CYBE with complex spectral parameters."""
        err = _mod.verify_cybe(1.0 + 0.5j, 2.0 - 0.3j)
        assert err < 1e-9


# ============================================================
# Quantum Yang-Baxter equation tests
# ============================================================

class TestQuantumYBE:
    def test_ybe_generic(self):
        """Quantum YBE at z1=1, z2=2, z3=3."""
        err = _mod.verify_quantum_ybe(1.0, 2.0, 3.0)
        assert err < 1e-9, f"YBE residual = {err}"

    def test_ybe_varied(self):
        """Quantum YBE at several values."""
        test_cases = [
            (0.5, 1.5, 2.5),
            (1.0, 3.0, 5.0),
            (2.0, 0.7, 4.0),
        ]
        for z1, z2, z3 in test_cases:
            err = _mod.verify_quantum_ybe(z1, z2, z3)
            assert err < 1e-8, f"YBE failed at z={z1},{z2},{z3}: residual = {err}"

    def test_ybe_complex(self):
        """Quantum YBE with complex parameters."""
        err = _mod.verify_quantum_ybe(1.0 + 0.3j, 2.0 - 0.1j, 3.0 + 0.5j)
        assert err < 1e-8


# ============================================================
# Structure constant verification
# ============================================================

class TestStructureConstants:
    def test_cubic_nonzero(self):
        """Cubic shadow C(H_1, E_1, F_1) = 2 (nonzero)."""
        result = _mod.verify_cubic_from_structure_constants()
        assert result['cubic_nonzero'] is True
        assert abs(result['C(H1,E1,F1)'] - 2.0) < 1e-12

    def test_jacobi_kills_quartic(self):
        """Jacobiator vanishes over all basis elements."""
        max_jac = _mod.verify_jacobi_kills_quartic()
        assert max_jac < 1e-10, f"Max Jacobiator = {max_jac}"


# ============================================================
# Comparison with sl_2
# ============================================================

class TestComparison:
    def test_both_class_L(self):
        """Both sl_2 and sl_3 are class L."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['depth_class'] == 'L'
        assert comp['sl_3']['depth_class'] == 'L'

    def test_same_S3(self):
        """Both have S_3 = 1 (universal for KM)."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['S_3'] == 1
        assert comp['sl_3']['S_3'] == 1

    def test_same_S4(self):
        """Both have S_4 = 0 (Jacobi identity)."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['S_4'] == 0
        assert comp['sl_3']['S_4'] == 0

    def test_same_depth(self):
        """Both have depth 3."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['depth'] == 3
        assert comp['sl_3']['depth'] == 3

    def test_different_dim(self):
        """sl_2 has dim 3, sl_3 has dim 8."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['dim'] == 3
        assert comp['sl_3']['dim'] == 8

    def test_different_hvee(self):
        """sl_2 has h^vee = 2, sl_3 has h^vee = 3."""
        comp = _mod.comparison_sl2_sl3()
        assert comp['sl_2']['h_vee'] == 2
        assert comp['sl_3']['h_vee'] == 3


# ============================================================
# Cross-family consistency (AP10: cross-family checks)
# ============================================================

class TestCrossFamilyConsistency:
    def test_kappa_formula_two_routes(self):
        """kappa via dim*shifted_level/(2*h^vee) == kappa via F_1*24.

        Two independent routes to kappa must agree (AP10).
        """
        kp = _mod.sl3_kappa(1)
        f1 = _mod.sl3_F1(1)
        assert kp == 24 * f1

    def test_tower_summary(self):
        """Tower summary does not crash and reports class L."""
        tower = _mod.sl3_shadow_tower_numeric(1.0, max_arity=10)
        summary = tower.summary()
        assert 'L' in summary or 'Depth class: L' in summary

    def test_growth_rate_zero_for_class_L(self):
        """Growth rate rho = 0 for class L (finite tower)."""
        tower = _mod.sl3_shadow_tower_numeric(1.0, max_arity=10)
        assert tower.growth_rate is not None
        if hasattr(tower.growth_rate, '__float__'):
            assert float(tower.growth_rate) == 0.0
        else:
            assert tower.growth_rate == 0

    def test_kappa_additivity(self):
        """kappa is additive: kappa(g1 x g2) = kappa(g1) + kappa(g2).

        For sl_2 x sl_3 at levels k1, k2:
            kappa = 3(k1+2)/4 + 4(k2+3)/3.
        """
        k1, k2 = 1, 2
        kappa_sl2 = Rational(3, 4) * (k1 + 2)
        kappa_sl3 = _mod.sl3_kappa(k2)
        kappa_product = kappa_sl2 + kappa_sl3
        expected = Rational(3, 4) * 3 + Rational(4, 3) * 5
        assert kappa_product == expected
