r"""Tests for the E_8 affine shadow obstruction tower engine.

FIRST COMPLETE SHADOW TOWER COMPUTATION FOR E_8^(1)_k
======================================================

Verifies:
  - kappa(E_8^(1)_k) = 62(k+30)/15 (modular characteristic, 5-path)
  - c(k) = 248k/(k+30) (Sugawara central charge)
  - S_3 = 1 (cubic shadow, universal for KM)
  - S_4 = 0 (quartic killed by Jacobi identity)
  - Delta = 0 (critical discriminant)
  - Class L assignment (depth 3, tower terminates at arity 3)
  - Shadow metric is a perfect square (class L property)
  - S_r = 0 for all r >= 4 (termination)
  - Koszul duality: k' = -k-60, kappa + kappa' = 0, c + c' = 496
  - F_g values at k=1 against manuscript table
  - A-hat generating function consistency
  - E_8 root system: dim=248, rank=8, h^vee=30, Cartan det=1
  - Lattice vs affine kappa discrepancy (AP48 finding)
  - Anomaly ratio rho(e_8) = 121/126
  - Exceptional family comparison
  - Heterotic string central charge budget
  - E_8 theta function = E_4

Ground truth:
  - kac_moody.tex: thm:affine-cubic-normal-form, cor:affine-postnikov-termination
  - genus_expansions.tex: comp:e8-genus-expansion
  - lattice_foundations.tex: prop:lattice:bar-E8
  - landscape_census.tex: tab:master-invariants
  - kappa_cross_verification.py: five-method cross-check
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, Matrix

import importlib.util
import os

# Load the module
_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'e8_affine_shadow_engine',
    os.path.join(_lib_dir, 'e8_affine_shadow_engine.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

k = Symbol('k')


# ============================================================
# Lie algebra constants
# ============================================================

class TestE8Constants:
    """Verify E_8 Lie algebra data against Bourbaki tables."""

    def test_dimension(self):
        """dim(e_8) = 248."""
        assert _mod.DIM_E8 == 248

    def test_rank(self):
        """rank(e_8) = 8."""
        assert _mod.RANK_E8 == 8

    def test_dual_coxeter(self):
        """h^vee(e_8) = 30 (simply-laced: h = h^vee)."""
        assert _mod.H_VEE_E8 == 30

    def test_coxeter(self):
        """h(e_8) = 30."""
        assert _mod.H_COX_E8 == 30

    def test_num_positive_roots(self):
        """|Delta^+| = 120."""
        assert _mod.NUM_POSITIVE_ROOTS == 120

    def test_num_roots(self):
        """|Delta| = 240."""
        assert _mod.NUM_ROOTS == 240

    def test_weyl_order(self):
        """|W(E_8)| = 696729600."""
        assert _mod.WEYL_ORDER == 696729600

    def test_exponents(self):
        """Exponents = [1, 7, 11, 13, 17, 19, 23, 29]."""
        assert _mod.EXPONENTS_E8 == [1, 7, 11, 13, 17, 19, 23, 29]

    def test_exponents_count(self):
        """Number of exponents = rank = 8."""
        assert len(_mod.EXPONENTS_E8) == _mod.RANK_E8

    def test_exponents_sum(self):
        """sum(exponents) = |Delta^+| = 120."""
        assert _mod.e8_exponent_verification() == 120

    def test_max_exponent_gives_h(self):
        """h^vee = max(exponent) + 1 = 29 + 1 = 30."""
        assert _mod.e8_dual_coxeter_from_exponents() == 30

    def test_dimension_from_roots(self):
        """dim = rank + |Delta| = 8 + 240 = 248."""
        assert _mod.e8_dimension_verification() == 248


# ============================================================
# Cartan matrix
# ============================================================

class TestCartanMatrix:
    """Verify the E_8 Cartan matrix."""

    def test_cartan_determinant(self):
        """det(A_{E_8}) = 1 (unique simply-laced with det = 1)."""
        assert _mod.e8_cartan_determinant() == 1

    def test_self_dual_lattice(self):
        """E_8 root lattice = weight lattice (det = 1 => self-dual)."""
        assert _mod.e8_is_self_dual_lattice()

    def test_cartan_shape(self):
        """Cartan matrix is 8x8."""
        A = _mod.e8_cartan_matrix()
        assert A.shape == (8, 8)

    def test_cartan_symmetric_off_diagonal(self):
        """Cartan matrix has A_{ij} = A_{ji} for i != j
        (simply-laced, all bonds are single)."""
        A = _mod.e8_cartan_matrix()
        for i in range(8):
            for j in range(8):
                if i != j:
                    assert A[i, j] == A[j, i], f"A[{i},{j}]={A[i,j]} != A[{j},{i}]={A[j,i]}"

    def test_cartan_diagonal(self):
        """All diagonal entries are 2."""
        A = _mod.e8_cartan_matrix()
        for i in range(8):
            assert A[i, i] == 2

    def test_cartan_off_diagonal_nonnegative(self):
        """Off-diagonal entries are 0 or -1 (simply-laced)."""
        A = _mod.e8_cartan_matrix()
        for i in range(8):
            for j in range(8):
                if i != j:
                    assert A[i, j] in (0, -1)

    def test_inverse_integral(self):
        """Inverse Cartan matrix has integer entries (since det = 1)."""
        A = _mod.e8_cartan_matrix()
        Ainv = A.inv()
        for i in range(8):
            for j in range(8):
                assert Ainv[i, j].is_integer, f"A^-1[{i},{j}]={Ainv[i,j]} not integer"

    def test_inverse_positive_definite(self):
        """Inverse Cartan matrix is positive definite (E_8 is finite type)."""
        A = _mod.e8_cartan_matrix()
        Ainv = A.inv()
        # All eigenvalues should be positive
        eigenvals = Ainv.eigenvals()
        for ev, mult in eigenvals.items():
            assert float(ev) > 0, f"Eigenvalue {ev} is not positive"

    def test_trivalent_vertex(self):
        """Node 3 is trivalent (connected to nodes 2, 4, 8)."""
        A = _mod.e8_cartan_matrix()
        neighbors_of_3 = [j for j in range(8) if j != 2 and A[2, j] == -1]
        assert sorted(neighbors_of_3) == [1, 3, 7], \
            f"Node 3 neighbors: {neighbors_of_3}"

    def test_number_of_edges(self):
        """E_8 Dynkin diagram has 7 edges."""
        A = _mod.e8_cartan_matrix()
        edges = sum(1 for i in range(8) for j in range(i+1, 8) if A[i, j] == -1)
        assert edges == 7


# ============================================================
# kappa tests (modular characteristic)
# ============================================================

class TestKappa:
    """Verify kappa(E_8^(1)_k) = 62(k+30)/15 by multiple paths."""

    def test_kappa_formula_symbolic(self):
        """kappa = 62(k+30)/15 = 248(k+30)/60."""
        kp = _mod.e8_kappa()
        expected = Rational(62, 15) * (k + 30)
        assert simplify(kp - expected) == 0

    def test_kappa_formula_alt(self):
        """kappa = dim(g)(k+h^vee)/(2h^vee) = 248(k+30)/60."""
        kp = _mod.e8_kappa()
        expected = Rational(248) * (k + 30) / 60
        assert simplify(kp - expected) == 0

    def test_kappa_at_k1(self):
        """kappa(k=1) = 248*31/60 = 1922/15."""
        kp = _mod.e8_kappa(1)
        assert kp == Rational(1922, 15)

    def test_kappa_at_k1_direct(self):
        """kappa(k=1) = 62*31/15 = 1922/15 (simplified formula)."""
        assert Rational(62) * 31 / 15 == Rational(1922, 15)

    def test_kappa_at_k1_decimal(self):
        """kappa(k=1) approx 128.133."""
        kp = float(_mod.e8_kappa(1))
        assert abs(kp - 128.1333333) < 1e-5

    def test_kappa_at_k2(self):
        """kappa(k=2) = 62*32/15 = 1984/15."""
        kp = _mod.e8_kappa(2)
        assert kp == Rational(62) * 32 / 15

    def test_kappa_at_critical_level(self):
        """kappa(k=-30) = 0 (critical level, uncurved)."""
        kp = _mod.e8_kappa(-30)
        assert kp == 0

    def test_kappa_positive_above_critical(self):
        """kappa > 0 for k > -30."""
        for k_val in [1, 2, 5, 10, 100]:
            assert _mod.e8_kappa(k_val) > 0

    def test_kappa_negative_below_critical(self):
        """kappa < 0 for k < -30 (non-critical negative level)."""
        for k_val in [-31, -40, -50, -59]:
            assert _mod.e8_kappa(k_val) < 0

    def test_kappa_from_genus1_bar(self):
        """Path 1: kappa = 24 * F_1."""
        kappa_val = _mod.e8_kappa(1)
        F1 = _mod.e8_free_energy(1, 1)
        assert simplify(kappa_val - 24 * F1) == 0

    def test_kappa_from_complementarity(self):
        """Path 3: kappa(k) + kappa(k') = 0."""
        assert _mod.verify_kappa_anti_symmetry()
        assert _mod.verify_kappa_anti_symmetry(1)
        assert _mod.verify_kappa_anti_symmetry(2)


# ============================================================
# Central charge tests
# ============================================================

class TestCentralCharge:
    """Verify the Sugawara central charge c = 248k/(k+30)."""

    def test_sugawara_formula(self):
        """c = 248k/(k+30) for E_8^(1)_k."""
        cc = _mod.e8_central_charge()
        expected = 248 * k / (k + 30)
        assert simplify(cc - expected) == 0

    def test_c_at_k1(self):
        """c(k=1) = 248/31 = 8."""
        assert _mod.e8_central_charge(1) == 8

    def test_c_at_k1_exact(self):
        """c(k=1) = 248/31 (as a rational)."""
        assert _mod.e8_central_charge(1) == Rational(248, 31)

    def test_c_at_k2(self):
        """c(k=2) = 496/32 = 31/2."""
        assert _mod.e8_central_charge(2) == Rational(496, 32)

    def test_c_at_large_k(self):
        """c(k) -> 248 as k -> infinity."""
        for k_val in [100, 1000, 10000]:
            c_val = float(_mod.e8_central_charge(k_val))
            assert abs(c_val - 248) < 248.0 / k_val * 100

    def test_c_at_critical_level(self):
        """c(k=-30) is UNDEFINED (Sugawara degenerates)."""
        # At critical level k = -h^vee = -30, the denominator vanishes.
        # The formula is undefined, not zero.
        with pytest.raises((ZeroDivisionError, Exception)):
            float(_mod.e8_central_charge(-30))


# ============================================================
# Koszul duality tests
# ============================================================

class TestKoszulDuality:
    """Verify Koszul dual level and complementarity sums."""

    def test_dual_level_formula(self):
        """k' = -k - 60 for E_8."""
        kd = _mod.e8_dual_level()
        assert simplify(kd - (-k - 60)) == 0

    def test_dual_level_at_k1(self):
        """k'(k=1) = -61."""
        assert _mod.e8_dual_level(1) == -61

    def test_kappa_anti_symmetry_symbolic(self):
        """kappa(k) + kappa(k') = 0 (symbolically)."""
        assert _mod.verify_kappa_anti_symmetry()

    def test_kappa_anti_symmetry_numeric(self):
        """kappa(k) + kappa(k') = 0 at several levels."""
        for k_val in [1, 2, 5, 10]:
            assert _mod.verify_kappa_anti_symmetry(k_val)

    def test_central_charge_sum_symbolic(self):
        """c(k) + c(k') = 496 (symbolically)."""
        assert _mod.verify_central_charge_sum()

    def test_central_charge_sum_numeric(self):
        """c(k) + c(k') = 496 at several levels."""
        for k_val in [1, 2, 5, 10]:
            assert _mod.verify_central_charge_sum(k_val)

    def test_496_is_heterotic(self):
        """c + c' = 496 = 2 * dim(E_8) = 2 * 248."""
        assert 2 * _mod.DIM_E8 == 496

    def test_496_is_perfect_number(self):
        """496 is the third perfect number (sum of proper divisors = 496)."""
        n = 496
        divisor_sum = sum(d for d in range(1, n) if n % d == 0)
        assert divisor_sum == n

    def test_complementarity_data(self):
        """Full complementarity data at k=1."""
        data = _mod.e8_complementarity_data(1)
        assert data['kappa_anti_symmetric']
        assert data['c_sum_equals_496']
        assert data['k_dual'] == -61
        assert data['kappa'] == Rational(1922, 15)
        assert data['kappa_dual'] == Rational(-1922, 15)

    def test_dual_kappa_explicit(self):
        """kappa(k=-61) = 62*(-61+30)/15 = 62*(-31)/15 = -1922/15."""
        kp_dual = _mod.e8_kappa(-61)
        assert kp_dual == Rational(-1922, 15)


# ============================================================
# Shadow tower tests
# ============================================================

class TestShadowTower:
    """Verify the shadow obstruction tower for E_8^(1)."""

    def test_cubic_shadow(self):
        """S_3 = 1 (universal for all affine KM)."""
        assert _mod.e8_cubic_shadow() == 1

    def test_quartic_shadow(self):
        """S_4 = 0 (Jacobi identity kills quartic)."""
        assert _mod.e8_quartic_shadow() == 0

    def test_discriminant(self):
        """Delta = 8*kappa*S_4 = 0."""
        assert _mod.e8_discriminant() == 0

    def test_depth_class(self):
        """E_8^(1) is class L (Lie/tree archetype)."""
        assert _mod.e8_depth_class() == 'L'

    def test_shadow_depth(self):
        """r_max = 3 (tower terminates at arity 3)."""
        assert _mod.e8_shadow_depth() == 3

    def test_tower_class_L_at_k1(self):
        """Shadow tower at k=1 has class L."""
        tower = _mod.e8_shadow_tower(1, max_arity=10)
        assert tower.depth_class == 'L'

    def test_tower_S2_is_kappa(self):
        """S_2 = kappa at k=1."""
        tower = _mod.e8_shadow_tower(1, max_arity=10)
        assert tower.kappa == Rational(1922, 15)

    def test_tower_S3_is_one(self):
        """S_3 = 1 from the tower computation."""
        tower = _mod.e8_shadow_tower(1, max_arity=10)
        sc3 = tower.coefficients.get(3)
        assert sc3 is not None
        assert abs(sc3.numerical - 1.0) < 1e-12

    def test_tower_terminates_at_arity_3(self):
        """S_r = 0 for all r >= 4 (class L termination)."""
        tower = _mod.e8_shadow_tower(1, max_arity=20)
        for r in range(4, 21):
            sc = tower.coefficients.get(r)
            if sc is not None and sc.numerical is not None:
                assert abs(sc.numerical) < 1e-12, \
                    f"S_{r} = {sc.numerical} != 0 (tower should terminate)"

    def test_tower_terminates_at_k2(self):
        """Termination holds at k=2 as well."""
        tower = _mod.e8_shadow_tower(2, max_arity=15)
        for r in range(4, 16):
            sc = tower.coefficients.get(r)
            if sc is not None and sc.numerical is not None:
                assert abs(sc.numerical) < 1e-12

    def test_tower_terminates_at_k5(self):
        """Termination at k=5."""
        tower = _mod.e8_shadow_tower(5, max_arity=15)
        for r in range(4, 16):
            sc = tower.coefficients.get(r)
            if sc is not None and sc.numerical is not None:
                assert abs(sc.numerical) < 1e-12

    def test_tower_numeric(self):
        """Numeric tower at k=1."""
        tower = _mod.e8_shadow_tower_numeric(1.0, max_arity=10)
        assert tower.depth_class == 'L'
        sc2 = tower.coefficients.get(2)
        assert abs(sc2.numerical - 1922.0/15.0) < 1e-8

    def test_growth_rate_zero(self):
        """Growth rate is 0 for class L."""
        assert _mod.e8_shadow_growth_rate() == 0

    def test_tower_convergent(self):
        """Shadow tower is trivially convergent (terminates)."""
        assert _mod.e8_shadow_convergent()


# ============================================================
# Shadow metric tests
# ============================================================

class TestShadowMetric:
    """Verify the shadow metric Q_L(t) for E_8^(1)."""

    def test_shadow_metric_is_perfect_square(self):
        """Q_L(t) = (2*kappa + 3*t)^2 (perfect square for class L)."""
        q0, q1, q2, delta = _mod.e8_shadow_metric()
        # For perfect square: q1^2 = 4*q0*q2
        # q1^2 = (12*kappa)^2 = 144*kappa^2
        # 4*q0*q2 = 4*(4*kappa^2)*9 = 144*kappa^2
        assert simplify(q1**2 - 4 * q0 * q2) == 0

    def test_shadow_metric_delta_zero(self):
        """Delta = 0 (class L condition)."""
        _, _, _, delta = _mod.e8_shadow_metric()
        assert delta == 0

    def test_shadow_metric_q0(self):
        """q0 = 4*kappa^2."""
        q0, _, _, _ = _mod.e8_shadow_metric(1)
        expected = 4 * Rational(1922, 15)**2
        assert simplify(q0 - expected) == 0

    def test_shadow_metric_q1(self):
        """q1 = 12*kappa (since alpha = S_3 = 1)."""
        _, q1, _, _ = _mod.e8_shadow_metric(1)
        expected = 12 * Rational(1922, 15)
        assert simplify(q1 - expected) == 0

    def test_shadow_metric_q2(self):
        """q2 = 9 (since alpha = 1 and S_4 = 0)."""
        _, _, q2, _ = _mod.e8_shadow_metric(1)
        assert q2 == 9

    def test_shadow_metric_explicit(self):
        """Explicit Q_L(t) at k=1."""
        q0, q1, q2 = _mod.e8_shadow_metric_explicit(1)
        kappa = Rational(1922, 15)
        assert q0 == 4 * kappa**2
        assert q1 == 12 * kappa
        assert q2 == 9

    def test_shadow_connection_residue(self):
        """Shadow connection residue data."""
        data = _mod.e8_shadow_connection_residue()
        assert data['residue'] == 1
        assert data['perfect_square']
        assert data['branch_points'] == 0


# ============================================================
# Genus expansion tests (F_g)
# ============================================================

class TestGenusExpansion:
    """Verify F_g(E_8^(1)_1) against the manuscript table."""

    def test_F1_exact(self):
        """F_1(k=1) = 961/180 (from manuscript comp:e8-genus-expansion)."""
        assert _mod.e8_free_energy(1, 1) == Rational(961, 180)

    def test_F1_from_kappa(self):
        """F_1 = kappa/24 = (1922/15)/24 = 1922/360 = 961/180."""
        kappa = Rational(1922, 15)
        assert kappa / 24 == Rational(961, 180)

    def test_F2_exact(self):
        """F_2(k=1) = 6727/43200."""
        assert _mod.e8_free_energy(2, 1) == Rational(6727, 43200)

    def test_F3_exact(self):
        """F_3(k=1) = 29791/7257600."""
        assert _mod.e8_free_energy(3, 1) == Rational(29791, 7257600)

    def test_F4_exact(self):
        """F_4(k=1) = 122047/1161216000."""
        assert _mod.e8_free_energy(4, 1) == Rational(122047, 1161216000)

    def test_F5_exact(self):
        """F_5(k=1) = 70153/26276659200."""
        assert _mod.e8_free_energy(5, 1) == Rational(70153, 26276659200)

    def test_manuscript_verification_all(self):
        """All manuscript F_g values verified."""
        results = _mod.verify_manuscript_Fg_values()
        for g, (computed, manuscript, agree) in results.items():
            assert agree, f"F_{g}: computed={computed} != manuscript={manuscript}"

    def test_F1_decimal(self):
        """F_1 approx 5.34."""
        assert abs(float(_mod.e8_free_energy(1, 1)) - 5.3389) < 0.01

    def test_Fg_positive(self):
        """F_g > 0 for all g >= 1 at k=1 (kappa > 0)."""
        for g in range(1, 11):
            assert _mod.e8_free_energy(g, 1) > 0

    def test_Fg_decreasing(self):
        """F_g is monotonically decreasing in g (Bernoulli decay)."""
        for g in range(1, 10):
            assert _mod.e8_free_energy(g, 1) > _mod.e8_free_energy(g + 1, 1)

    def test_F_table(self):
        """Full table computation."""
        table = _mod.e8_free_energy_table(5, 1)
        assert len(table) == 5
        assert table[1] == Rational(961, 180)

    def test_F1_complementarity(self):
        """F_1(k) + F_1(k') = 0 (kappa anti-symmetric => F_1 anti-symmetric)."""
        F1 = _mod.e8_free_energy(1, 1)
        F1_dual = _mod.e8_free_energy(1, -61)
        assert simplify(F1 + F1_dual) == 0

    def test_F_at_critical_level(self):
        """F_g = 0 at the critical level k = -30 (kappa = 0)."""
        for g in range(1, 5):
            assert _mod.e8_free_energy(g, -30) == 0


# ============================================================
# A-hat generating function tests
# ============================================================

class TestAhatGF:
    """Verify the A-hat generating function relation (AP22)."""

    def test_ahat_consistency_g1(self):
        """F_1 matches A-hat coefficient at genus 1."""
        results = _mod.e8_ahat_generating_function_check(1)
        direct, ahat, agree = results[1]
        assert agree

    def test_ahat_consistency_all(self):
        """All F_g match A-hat coefficients through genus 5."""
        results = _mod.e8_ahat_generating_function_check(5)
        for g, (direct, ahat, agree) in results.items():
            assert agree, f"g={g}: F_g direct={direct} != from A-hat={ahat}"


# ============================================================
# Kappa discrepancy (AP48)
# ============================================================

class TestKappaDiscrepancy:
    """Verify the AP48 finding: kappa_affine != kappa_lattice for E_8."""

    def test_affine_kappa_at_k1(self):
        """Affine formula gives kappa = 1922/15."""
        assert _mod.affine_kappa_formula(1) == Rational(1922, 15)

    def test_lattice_kappa(self):
        """Lattice formula gives kappa = 8 (rank)."""
        assert _mod.lattice_kappa_rank() == 8

    def test_they_disagree(self):
        """The two formulas give DIFFERENT values (this is the finding)."""
        assert _mod.affine_kappa_formula(1) != _mod.lattice_kappa_rank()

    def test_ratio(self):
        """kappa_affine / kappa_lattice = 961/60 approx 16.017."""
        ratio = _mod.kappa_discrepancy_ratio()
        assert ratio == Rational(961, 60)

    def test_ratio_decimal(self):
        """Ratio is approximately 16.017."""
        ratio = float(_mod.kappa_discrepancy_ratio())
        assert abs(ratio - 16.0167) < 0.001

    def test_ratio_formula(self):
        """Ratio = dim(g)(1+h^vee) / (2*h^vee*rank) = 248*31/(60*8)."""
        expected = Rational(248) * 31 / (60 * 8)
        assert _mod.kappa_discrepancy_ratio() == expected

    def test_discrepancy_analysis(self):
        """Full discrepancy analysis."""
        disc = _mod.kappa_discrepancy_analysis()
        assert disc['kappa_affine'] == Rational(1922, 15)
        assert disc['kappa_lattice'] == Rational(8)
        assert disc['ratio'] == Rational(961, 60)
        assert disc['num_cartan_currents'] == 8
        assert disc['num_root_currents'] == 240
        assert disc['total_currents'] == 248

    def test_root_vector_contribution(self):
        """Root vectors contribute kappa_affine - kappa_lattice = 1922/15 - 8 = 1802/15."""
        disc = _mod.kappa_discrepancy_analysis()
        expected = Rational(1922, 15) - 8
        assert disc['root_vector_contribution'] == expected
        assert expected == Rational(1802, 15)

    def test_cartan_fraction(self):
        """Cartan subalgebra contributes only ~6.2% of total kappa."""
        disc = _mod.kappa_discrepancy_analysis()
        frac = disc['cartan_fraction_float']
        assert abs(frac - 8.0 / (1922.0 / 15.0)) < 1e-6
        assert frac < 0.07  # Less than 7%

    def test_root_fraction_dominant(self):
        """Root vectors contribute ~93.8% of total kappa."""
        disc = _mod.kappa_discrepancy_analysis()
        assert disc['root_fraction'] > 0.93


# ============================================================
# W-algebra and DS reduction tests
# ============================================================

class TestWAlgebra:
    """Verify the anomaly ratio and W-algebra connection."""

    def test_anomaly_ratio(self):
        """rho(e_8) = sum 1/(m_i+1) = 121/126."""
        assert _mod.e8_anomaly_ratio() == Rational(121, 126)

    def test_anomaly_ratio_decimal(self):
        """rho(e_8) approx 0.960."""
        assert abs(float(_mod.e8_anomaly_ratio()) - 0.96032) < 0.001

    def test_anomaly_ratio_less_than_1(self):
        """rho(e_8) < 1 (convergent shadow tower for W(e_8))."""
        assert _mod.e8_anomaly_ratio() < 1

    def test_anomaly_ratio_from_exponents(self):
        """Verify rho from explicit exponent calculation."""
        exps = [1, 7, 11, 13, 17, 19, 23, 29]
        rho = sum(Rational(1, m + 1) for m in exps)
        assert rho == Rational(121, 126)

    def test_ds_consistency(self):
        """DS reduction internal consistency check."""
        assert _mod.verify_ds_kappa_consistency(1)


# ============================================================
# r-matrix tests
# ============================================================

class TestRMatrix:
    """Verify the r-matrix data for E_8^(1)."""

    def test_r_matrix_type(self):
        """r(z) = k*Omega/z (rational, single pole)."""
        data = _mod.e8_r_matrix_type()
        assert data['type'] == 'rational'
        assert data['pole_order'] == 1
        assert data['cybe_satisfied']

    def test_casimir_adjoint(self):
        """C_2(adj) = 2*h^vee = 60."""
        assert _mod.e8_casimir_adjoint() == 60

    def test_casimir_trace_adjoint(self):
        """Tr_{adj}(C_2) = 60 * 248 = 14880."""
        assert _mod.e8_casimir_trace_adjoint() == 14880


# ============================================================
# Heterotic string tests
# ============================================================

class TestHeterotic:
    """Verify the heterotic string central charge budget."""

    def test_c_e8_at_k1_is_8(self):
        """c(E_8^(1)_1) = 8."""
        het = _mod.heterotic_central_charge_check()
        assert het['c_e8_level1'] == 8

    def test_double_e8_gives_16(self):
        """c(E_8 x E_8) = 16."""
        het = _mod.heterotic_central_charge_check()
        assert het['c_double_e8'] == 16

    def test_heterotic_is_26(self):
        """c(E_8 x E_8) + 10 = 26 (bosonic string)."""
        het = _mod.heterotic_central_charge_check()
        assert het['heterotic_check']

    def test_c_at_k1_is_248_over_31(self):
        """c = 248/31 = 8 (exact)."""
        c = _mod.e8_central_charge(1)
        assert c == Rational(248, 31)
        assert c == 8


# ============================================================
# E_8 theta function tests
# ============================================================

class TestThetaFunction:
    """Verify theta_{E_8} = E_4 data."""

    def test_theta_constant_term(self):
        """a(0) = 1 (one zero vector)."""
        coeffs = _mod.e8_theta_is_e4()
        assert coeffs[0] == 1

    def test_theta_norm2_count(self):
        """a(1) = 240 = |Delta(E_8)| (240 roots of norm 2)."""
        coeffs = _mod.e8_theta_is_e4()
        assert coeffs[1] == 240

    def test_theta_norm4_count(self):
        """a(2) = 2160 (vectors of norm 4)."""
        coeffs = _mod.e8_theta_is_e4()
        assert coeffs[2] == 2160

    def test_theta_sigma3_relation(self):
        """a(n) = 240 * sigma_3(n) for n >= 1.

        For E_4 = 1 + 240 * sum sigma_3(n) q^n.
        """
        coeffs = _mod.e8_theta_is_e4()
        # sigma_3(n) = sum of cubes of divisors
        def sigma3(n):
            return sum(d**3 for d in range(1, n+1) if n % d == 0)

        for n in range(1, 6):
            assert coeffs[n] == 240 * sigma3(n), \
                f"a({n}) = {coeffs[n]} != 240*sigma_3({n}) = {240*sigma3(n)}"


# ============================================================
# Exceptional family comparison tests
# ============================================================

class TestExceptionalComparison:
    """Compare kappa across exceptional Lie algebras."""

    def test_exceptional_kappas_all_correct(self):
        """All exceptional kappa formulas verified."""
        results = _mod.compare_exceptional_kappas()
        for name, data in results.items():
            assert data['formula_check'], f"{name}: kappa formula mismatch"

    def test_g2_kappa(self):
        """kappa(G_2, k=1) = 35/4."""
        results = _mod.compare_exceptional_kappas()
        assert results['G_2']['kappa_k1'] == Rational(35, 4)

    def test_f4_kappa(self):
        """kappa(F_4, k=1) = 260/9."""
        results = _mod.compare_exceptional_kappas()
        assert results['F_4']['kappa_k1'] == Rational(260, 9)

    def test_e6_kappa(self):
        """kappa(E_6, k=1) = 169/4."""
        results = _mod.compare_exceptional_kappas()
        assert results['E_6']['kappa_k1'] == Rational(169, 4)

    def test_e7_kappa(self):
        """kappa(E_7, k=1) = 2527/36."""
        results = _mod.compare_exceptional_kappas()
        assert results['E_7']['kappa_k1'] == Rational(2527, 36)

    def test_e8_kappa_matches(self):
        """kappa(E_8, k=1) = 1922/15 in comparison table."""
        results = _mod.compare_exceptional_kappas()
        assert results['E_8']['kappa_k1'] == Rational(1922, 15)

    def test_kappa_ordering(self):
        """Kappa values increase with dimension:
        G_2 < F_4 < E_6 < E_7 < E_8."""
        results = _mod.compare_exceptional_kappas()
        kappas = [float(results[name]['kappa_decimal'])
                  for name in ['G_2', 'F_4', 'E_6', 'E_7', 'E_8']]
        for i in range(len(kappas) - 1):
            assert kappas[i] < kappas[i + 1]


# ============================================================
# Cross-verification with kappa_cross_verification.py
# ============================================================

class TestCrossVerification:
    """Cross-check against the central kappa verification engine."""

    def test_matches_manuscript_value(self):
        """kappa(E_8, k=1) = 1922/15 matches manuscript table."""
        assert _mod.e8_kappa(1) == Rational(1922, 15)

    def test_matches_landscape_census(self):
        """Value matches the authoritative landscape census.

        From kappa_cross_verification.py:
            ("affine_E8", ("k", 1)): Rational(1922, 15)
        """
        assert _mod.e8_kappa(1) == Rational(1922, 15)

    def test_matches_lattice_e8_value(self):
        """Lattice E_8 value matches the lattice entry.

        From kappa_cross_verification.py:
            ("lattice_E8", ()): Rational(8)
        """
        assert _mod.lattice_kappa_rank() == Rational(8)

    def test_kappa_formula_matches_general(self):
        """Formula matches the general KM formula dim(g)(k+h^v)/(2h^v).

        At k=1: 248*(1+30)/(2*30) = 248*31/60 = 7688/60 = 1922/15.
        """
        general = Rational(248) * (1 + 30) / (2 * 30)
        assert general == Rational(1922, 15)
        assert _mod.e8_kappa(1) == general


# ============================================================
# Depth filtration tests
# ============================================================

class TestDepthFiltration:
    """Verify the depth filtration data."""

    def test_depth_filtration(self):
        """Depth filtration for E_8^(1)."""
        data = _mod.e8_depth_filtration()
        assert data['shadow_depth'] == 3
        assert data['d_arith'] == 0
        assert data['d_alg'] == 1
        assert data['nonzero_arities'] == [2, 3]


# ============================================================
# E_8 special properties
# ============================================================

class TestSpecialProperties:
    """Verify special properties of E_8."""

    def test_unique_integrable(self):
        """Level-1 E_8 has a unique integrable representation."""
        assert _mod.e8_unique_integrable_level()

    def test_self_dual_lattice(self):
        """E_8 lattice is self-dual (det Cartan = 1)."""
        assert _mod.e8_is_self_dual_lattice()


# ============================================================
# Parametric level tests
# ============================================================

class TestParametricLevel:
    """Verify formulas at various levels k."""

    @pytest.mark.parametrize("k_val,expected_kappa", [
        (1, Rational(1922, 15)),
        (2, Rational(62) * 32 / 15),
        (3, Rational(62) * 33 / 15),
        (10, Rational(62) * 40 / 15),
        (-29, Rational(62) * 1 / 15),
        (-30, 0),
    ])
    def test_kappa_at_various_levels(self, k_val, expected_kappa):
        """kappa at various levels."""
        assert _mod.e8_kappa(k_val) == expected_kappa

    @pytest.mark.parametrize("k_val,expected_c", [
        (1, 8),
        (2, Rational(496, 32)),
        (10, Rational(248) * 10 / 40),
    ])
    def test_c_at_various_levels(self, k_val, expected_c):
        """Central charge at various levels."""
        assert _mod.e8_central_charge(k_val) == expected_c

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 50, 100])
    def test_kappa_complementarity_parametric(self, k_val):
        """kappa anti-symmetry at various levels."""
        assert _mod.verify_kappa_anti_symmetry(k_val)

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, 50, 100])
    def test_c_sum_parametric(self, k_val):
        """c + c' = 496 at various levels."""
        assert _mod.verify_central_charge_sum(k_val)


# ============================================================
# Numerics and decimal checks
# ============================================================

class TestNumerics:
    """Numerical sanity checks."""

    def test_kappa_magnitude(self):
        """kappa(k=1) approx 128 (among largest in landscape table)."""
        kp = float(_mod.e8_kappa(1))
        assert 128 < kp < 129

    def test_F1_magnitude(self):
        """F_1(k=1) approx 5.34."""
        f1 = float(_mod.e8_free_energy(1, 1))
        assert 5.3 < f1 < 5.4

    def test_F2_magnitude(self):
        """F_2(k=1) approx 0.156."""
        f2 = float(_mod.e8_free_energy(2, 1))
        assert 0.15 < f2 < 0.16

    def test_c_at_k1_is_integer(self):
        """c(k=1) = 8 (an integer, which is rare and special)."""
        c = _mod.e8_central_charge(1)
        assert c == 8
        assert c.is_integer

    def test_kappa_over_24_is_F1(self):
        """kappa/24 = F_1 (basic identity check)."""
        kp = _mod.e8_kappa(1)
        F1 = _mod.e8_free_energy(1, 1)
        assert simplify(kp / 24 - F1) == 0


# ============================================================
# Additional structural tests
# ============================================================

class TestStructural:
    """Structural verification of the shadow tower."""

    def test_tower_has_summary(self):
        """Tower summary is non-empty."""
        tower = _mod.e8_shadow_tower(1, max_arity=5)
        summary = tower.summary()
        assert 'E_8' in summary
        assert 'Class' in summary or 'class' in summary.lower() or 'L' in summary

    def test_tower_coefficients_dict(self):
        """Tower has the right number of coefficients."""
        tower = _mod.e8_shadow_tower(1, max_arity=10)
        assert 2 in tower.coefficients
        assert 3 in tower.coefficients
        # Should have entries from 2 to 10
        for r in range(2, 11):
            assert r in tower.coefficients

    def test_generating_function_polynomial(self):
        """For class L, the generating function is a polynomial of degree 3."""
        tower = _mod.e8_shadow_tower(1, max_arity=10)
        gf = tower.generating_function('t', max_terms=10)
        # Should be kappa*t^2 + 1*t^3 (approximately, with S_3/3 etc.)
        # The tower has S_2 = kappa, S_3 = 1, S_r = 0 for r >= 4
        # GF = kappa*t^2 + 1*t^3
        from sympy import Symbol, Poly
        t = Symbol('t')
        poly = gf.as_poly(t)
        assert poly is not None
        assert poly.degree() == 3  # Highest nonzero term is t^3

    def test_ratio_test_class_L(self):
        """Ratio test gives 0 for class L (trailing ratios are 0/x = 0)."""
        tower = _mod.e8_shadow_tower_numeric(1.0, max_arity=10)
        ratios = tower.ratio_test()
        # After the termination point, ratios should be 0
        for r in range(3, len(ratios)):
            assert ratios[r] < 1e-10

    def test_partial_sums_constant(self):
        """Partial sums stabilize for class L."""
        tower = _mod.e8_shadow_tower_numeric(1.0, max_arity=10)
        psums = tower.partial_sums()
        # After arity 3, partial sums should be constant
        if len(psums) >= 3:
            for i in range(2, len(psums)):
                assert abs(psums[i] - psums[2]) < 1e-10


# ============================================================
# Anomaly ratio comparison across exceptional algebras
# ============================================================

class TestAnomalyRatioComparison:
    """Compare anomaly ratios across exceptional algebras."""

    def test_e8_rho_exact(self):
        """rho(E_8) = 121/126."""
        assert _mod.e8_anomaly_ratio() == Rational(121, 126)

    def test_e8_rho_parts(self):
        """Verify each term in the sum."""
        terms = [Rational(1, m + 1) for m in [1, 7, 11, 13, 17, 19, 23, 29]]
        expected = [Rational(1, 2), Rational(1, 8), Rational(1, 12),
                    Rational(1, 14), Rational(1, 18), Rational(1, 20),
                    Rational(1, 24), Rational(1, 30)]
        for t, e in zip(terms, expected):
            assert t == e
        assert sum(terms) == Rational(121, 126)

    def test_rho_ordering(self):
        """Anomaly ratios: rho(G_2) < rho(F_4) < rho(E_8) < rho(E_7) < rho(E_6).

        The ordering is NOT monotone in rank. E_6 has the LARGEST rho among
        exceptionals because its exponents [1,4,5,7,8,11] have many small
        values. E_8 has the smallest rho among the E series because its
        large exponents (23, 29) give tiny 1/(m+1) contributions.

        Exact values:
            rho(G_2) = 2/3 approx 0.667
            rho(F_4) = 7/8 = 0.875
            rho(E_8) = 121/126 approx 0.960
            rho(E_7) = 2777/2520 approx 1.102
            rho(E_6) = 427/360 approx 1.186
        """
        exps_data = {
            'G_2': [1, 5],
            'F_4': [1, 5, 7, 11],
            'E_6': [1, 4, 5, 7, 8, 11],
            'E_7': [1, 5, 7, 9, 11, 13, 17],
            'E_8': [1, 7, 11, 13, 17, 19, 23, 29],
        }
        rhos = {}
        for name, exps in exps_data.items():
            rhos[name] = sum(Rational(1, m + 1) for m in exps)

        # Verified ordering: G_2 < F_4 < E_8 < E_7 < E_6
        ordered = ['G_2', 'F_4', 'E_8', 'E_7', 'E_6']
        for i in range(len(ordered) - 1):
            assert rhos[ordered[i]] < rhos[ordered[i+1]], \
                f"rho({ordered[i]}) = {rhos[ordered[i]]} not < rho({ordered[i+1]}) = {rhos[ordered[i+1]]}"

    def test_e8_rho_less_than_1(self):
        """rho(E_8) < 1 (W(e_8) shadow tower converges)."""
        exps = [1, 7, 11, 13, 17, 19, 23, 29]
        rho = sum(Rational(1, m + 1) for m in exps)
        assert rho < 1

    def test_e6_rho_greater_than_1(self):
        """rho(E_6) > 1 (W(e_6) shadow tower diverges)."""
        exps = [1, 4, 5, 7, 8, 11]
        rho = sum(Rational(1, m + 1) for m in exps)
        assert rho > 1
