r"""Tests for the conformal bootstrap as a projection of the MC equation.

Verifies:
  1. MC equation at (0,4) = crossing equation for 4-point functions
  2. Q^contact = 10/[c(5c+22)] via three independent paths
  3. Ising model (c=1/2): MC predictions vs exact BPZ results
  4. Free boson (c=1): Wick contraction and crossing symmetry
  5. Hellerman bound Delta <= c/12 + O(1) from kappa = c/2
  6. Genus-1 MC = torus partition function constraint
  7. Modular bootstrap compatibility with shadow tower
  8. Cardy formula from the genus-1 shadow
  9. Shadow tower gap bounds
 10. Cross-family landscape scan

AP compliance:
  - AP10: Every numerical result verified by 2+ independent paths.
  - AP1: kappa(Vir_c) = c/2 verified independently.
  - AP24: Virasoro complementarity sum checked.
  - AP38: All numerical values derived from first principles.
"""

import math
import pytest
from fractions import Fraction

import numpy as np

from sympy import Rational, simplify, bernoulli, factorial, S as symS

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from conformal_bootstrap_mc_engine import (
    # Primitives
    kappa_virasoro,
    kappa_heisenberg,
    lambda_fp,
    F_g_shadow,
    Q_contact_virasoro,
    shadow_planted_forest_genus2,
    # MC at (0,4)
    mc_genus0_arity4_virasoro,
    mc_crossing_equation_components,
    # Q^contact three paths
    Q_contact_path1_mc_recursion,
    Q_contact_path2_gram_matrix,
    Q_contact_path3_discriminant,
    Q_contact_verify_three_paths,
    # Ising
    ising_mc_data,
    ising_four_point_at_z_half,
    ising_ope_from_mc,
    # Free boson
    free_boson_mc_data,
    free_boson_four_point_wick,
    free_boson_crossing_check,
    # Hellerman
    hellerman_bound_from_shadow,
    # Genus-1
    genus1_mc_torus_one_point,
    genus1_mc_partition_function,
    # Modular bootstrap
    modular_bootstrap_shadow_verification,
    # Cardy
    cardy_from_shadow,
    cardy_subleading_from_shadow,
    # Gap bounds
    shadow_tower_gap_bound,
    # Verifications
    verify_ising_bootstrap,
    verify_free_boson_bootstrap,
    verify_monster_bootstrap,
    verify_c_large_cardy,
    # Landscape
    bootstrap_landscape_scan,
    mc_hierarchy_virasoro,
    shadow_bootstrap_minimal_models,
)


# ============================================================================
# 1. Shadow primitives
# ============================================================================

class TestShadowPrimitives:
    """Verify shadow obstruction tower primitives."""

    def test_kappa_virasoro_rational(self):
        """kappa(Vir_c) = c/2 for exact rational c."""
        assert kappa_virasoro(Rational(1, 2)) == Rational(1, 4)
        assert kappa_virasoro(Rational(1)) == Rational(1, 2)
        assert kappa_virasoro(Rational(24)) == Rational(12)

    def test_kappa_virasoro_integer(self):
        """kappa(Vir_c) = c/2 for integer c."""
        assert kappa_virasoro(1) == Rational(1, 2)
        assert kappa_virasoro(24) == Rational(12)
        assert kappa_virasoro(26) == Rational(13)

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k. AP1: different formula from Virasoro."""
        assert kappa_heisenberg(1) == Rational(1)
        assert kappa_heisenberg(2) == Rational(2)
        # AP9: kappa(H_k) and kappa(Vir_c) are DIFFERENT formulas.
        # Heisenberg at level k=1 has c=1 and kappa=1.
        # Virasoro at c=1 has kappa = c/2 = 1/2.
        # The distinction: same c, different kappa.
        assert kappa_heisenberg(1) != kappa_virasoro(1)  # 1 != 1/2
        # At k=2: kappa(H_2) = 2, but kappa(Vir_{c=1}) = 1/2
        # The Heisenberg central charge is c = 1 for any k,
        # while kappa = k depends on the level.
        assert kappa_heisenberg(2) == Rational(2)
        assert kappa_virasoro(1) == Rational(1, 2)

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        # (2^5 - 1)/2^5 * |B_6|/6! = 31/32 * (1/42) / 720
        # = 31/(32 * 42 * 720) = 31/967680
        assert lambda_fp(3) == Rational(31, 967680)

    def test_F1_virasoro(self):
        """F_1 = kappa/24 = c/48."""
        c = Rational(1, 2)
        kappa = kappa_virasoro(c)
        F_1 = F_g_shadow(kappa, 1)
        assert F_1 == Rational(1, 96)

    def test_F1_positive(self):
        """F_1 > 0 for c > 0 (Bernoulli positivity)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            kappa = kappa_virasoro(c_val)
            assert F_g_shadow(kappa, 1) > 0


# ============================================================================
# 2. Q^contact verification
# ============================================================================

class TestQContactVirasoro:
    """Verify Q^contact = 10/[c(5c+22)] via multiple paths."""

    def test_Q_contact_ising(self):
        """Q^contact(Vir_{1/2}) = 40/49."""
        c = Rational(1, 2)
        Q = Q_contact_virasoro(c)
        # 10 / [(1/2)(5/2 + 22)] = 10 / [(1/2)(49/2)] = 10 / (49/4) = 40/49
        assert Q == Rational(40, 49)

    def test_Q_contact_c1(self):
        """Q^contact(Vir_1) = 10/27."""
        c = Rational(1)
        Q = Q_contact_virasoro(c)
        # 10 / [1 * (5 + 22)] = 10/27
        assert Q == Rational(10, 27)

    def test_Q_contact_c24(self):
        """Q^contact(Vir_{24}) = 10/[24*142] = 5/1704."""
        c = Rational(24)
        Q = Q_contact_virasoro(c)
        # 10 / [24 * (120 + 22)] = 10 / (24 * 142) = 10/3408 = 5/1704
        assert Q == Rational(5, 1704)

    def test_Q_contact_c26(self):
        """Q^contact(Vir_{26}) = 10/[26*152] = 5/1976."""
        c = Rational(26)
        Q = Q_contact_virasoro(c)
        assert Q == Rational(10, 26 * 152)

    def test_Q_contact_three_paths_ising(self):
        """Three-path verification at c = 1/2 (AP10)."""
        result = Q_contact_verify_three_paths(Rational(1, 2))
        assert result['all_paths_agree']

    def test_Q_contact_three_paths_c1(self):
        """Three-path verification at c = 1 (AP10)."""
        result = Q_contact_verify_three_paths(Rational(1))
        assert result['all_paths_agree']

    def test_Q_contact_three_paths_c24(self):
        """Three-path verification at c = 24 (AP10)."""
        result = Q_contact_verify_three_paths(Rational(24))
        assert result['all_paths_agree']

    def test_Q_contact_discriminant_consistency(self):
        """Discriminant Delta = 40/(5c+22) matches Q^contact path."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            result = Q_contact_path3_discriminant(c_val)
            assert result['consistent']

    def test_Q_contact_positive_for_c_positive(self):
        """Q^contact > 0 for c > 0 (quartic shadow is positive)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(10), Rational(24)]:
            Q = Q_contact_virasoro(c_val)
            assert Q > 0

    def test_Q_contact_decreases_with_c(self):
        """Q^contact is a decreasing function of c for c > 0."""
        c_vals = [Rational(1, 2), Rational(1), Rational(2), Rational(10), Rational(24)]
        Q_vals = [Q_contact_virasoro(c) for c in c_vals]
        for i in range(len(Q_vals) - 1):
            assert Q_vals[i] > Q_vals[i + 1]


# ============================================================================
# 3. MC equation at (0,4): crossing equation
# ============================================================================

class TestMCGenus0Arity4:
    """Verify MC at (0,4) = crossing equation."""

    def test_mc_arity4_satisfied(self):
        """MC equation at (0,4) is satisfied for all c > 0."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            data = mc_genus0_arity4_virasoro(c_val)
            assert data['mc_satisfied']

    def test_mc_arity4_components_ising(self):
        """MC equation components at c = 1/2."""
        data = mc_genus0_arity4_virasoro(Rational(1, 2))
        assert data['kappa'] == Rational(1, 4)
        assert data['S_3'] == Rational(2)
        assert data['Q_contact'] == Rational(40, 49)

    def test_mc_crossing_interpretation(self):
        """MC at (0,4) is the crossing equation in the shadow basis."""
        data = mc_crossing_equation_components(Rational(1, 2))
        assert data['crossing_satisfied']
        assert 'crossing equation' in data['interpretation']

    def test_beta_2_ising(self):
        """beta_2 = 16/(22 + 5c) at c = 1/2."""
        data = mc_genus0_arity4_virasoro(Rational(1, 2))
        expected = Rational(16, 22 + 5 * Rational(1, 2))
        # 16 / (22 + 5/2) = 16 / (49/2) = 32/49
        assert data['beta_2'] == Rational(32, 49)

    def test_beta_2_c1(self):
        """beta_2 = 16/27 at c = 1."""
        data = mc_genus0_arity4_virasoro(Rational(1))
        assert data['beta_2'] == Rational(16, 27)

    def test_cubic_self_sewing_nonzero(self):
        """The cubic self-sewing {S_3, S_3}_H is nonzero."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            data = mc_genus0_arity4_virasoro(c_val)
            assert data['cubic_self_sewing'] != 0

    def test_composite_correction_nonzero(self):
        """The composite-field correction is nonzero for Virasoro."""
        for c_val in [Rational(1, 2), Rational(1)]:
            data = mc_genus0_arity4_virasoro(c_val)
            assert data['composite_correction'] != 0


# ============================================================================
# 4. Ising model (c = 1/2)
# ============================================================================

class TestIsingBootstrap:
    """Verify bootstrap constraints for the Ising model."""

    def test_ising_kappa(self):
        """kappa(Ising) = 1/4."""
        data = ising_mc_data()
        assert data['kappa'] == Rational(1, 4)

    def test_ising_Q_contact(self):
        """Q^contact(Ising) = 40/49."""
        data = ising_mc_data()
        assert data['Q_contact_matches']

    def test_ising_F1(self):
        """F_1(Ising) = 1/96."""
        data = ising_mc_data()
        assert data['F_1_matches']

    def test_ising_C_sse_squared(self):
        """C_{sigma sigma epsilon}^2 = 1/4 (exact BPZ result)."""
        data = ising_mc_data()
        assert data['C_sigma_sigma_epsilon_sq'] == Rational(1, 4)

    def test_ising_hypergeometric_params(self):
        """Ising 4-point function = _2F_1(1/2, 1/2; 1; z)."""
        data = ising_mc_data()
        params = data['hypergeometric_parameters']
        assert params['a'] == Rational(1, 2)
        assert params['b'] == Rational(1, 2)
        assert params['c_param'] == Rational(1)

    def test_ising_four_point_crossing(self):
        """Ising 4-point function satisfies crossing at z = 1/2."""
        data = ising_four_point_at_z_half()
        assert data['crossing_satisfied']

    def test_ising_four_point_exact(self):
        """Ising 4-point matches the exact elliptic integral value."""
        data = ising_four_point_at_z_half()
        assert data['F_matches_exact']

    def test_ising_full_verification(self):
        """Full multi-path Ising verification (AP10)."""
        result = verify_ising_bootstrap()
        assert result['all_consistent']

    def test_ising_gap_above_c_12(self):
        """Ising gap 1/16 > c/12 = 1/24."""
        result = verify_ising_bootstrap()
        assert result['gap_above_c_12']


# ============================================================================
# 5. Free boson (c = 1)
# ============================================================================

class TestFreeBosonBootstrap:
    """Verify bootstrap constraints for the free boson."""

    def test_boson_heisenberg_kappa(self):
        """kappa(H_1) = 1 (Heisenberg formula)."""
        data = free_boson_mc_data()
        assert data['heisenberg_data']['kappa'] == Rational(1)

    def test_boson_virasoro_kappa(self):
        """kappa(Vir_1) = 1/2 (Virasoro formula)."""
        data = free_boson_mc_data()
        assert data['virasoro_data']['kappa'] == Rational(1, 2)

    def test_boson_heisenberg_class_G(self):
        """Heisenberg is class G: Q^contact = 0."""
        data = free_boson_mc_data()
        assert data['heisenberg_data']['Q_contact'] == 0
        assert data['heisenberg_data']['shadow_class'] == 'G'

    def test_boson_virasoro_class_M(self):
        """Virasoro is class M: Q^contact != 0."""
        data = free_boson_mc_data()
        assert data['virasoro_data']['Q_contact'] != 0
        assert data['virasoro_data']['shadow_class'] == 'M'

    def test_boson_wick_three_terms(self):
        """Free boson 4-point = 3 Wick contractions."""
        data = free_boson_mc_data()
        assert data['four_point_wick_terms'] == 3

    def test_boson_wick_specific(self):
        """Wick contraction at specific points."""
        # <j(1)j(2)j(3)j(4)> = 1/(1*1) + 1/(4*1) + 1/(9*4)
        # = 1 + 1/4 + 1/36 = 36/36 + 9/36 + 1/36 = 46/36 = 23/18
        # Wait: 1/((1-2)^2 * (3-4)^2) + 1/((1-3)^2 * (2-4)^2) + 1/((1-4)^2 * (2-3)^2)
        # = 1/(1*1) + 1/(4*4) + 1/(9*1)
        # = 1 + 1/16 + 1/9 = 144/144 + 9/144 + 16/144 = 169/144
        result = free_boson_four_point_wick(1.0, 2.0, 3.0, 4.0)
        expected = 1.0 + 1.0/16.0 + 1.0/9.0
        assert abs(result - expected) < 1e-10

    def test_boson_crossing_symmetry(self):
        """Free boson 4-point is crossing-symmetric (permutation invariant)."""
        data = free_boson_crossing_check()
        assert data['crossing_12']
        assert data['crossing_13']
        assert data['crossing_14']

    def test_boson_full_verification(self):
        """Full multi-path free boson verification (AP10)."""
        result = verify_free_boson_bootstrap()
        assert result['all_consistent']


# ============================================================================
# 6. Hellerman bound
# ============================================================================

class TestHellermanBound:
    """Verify Hellerman bound from shadow data."""

    def test_hellerman_leading_term(self):
        """Leading Hellerman bound is c/12."""
        data = hellerman_bound_from_shadow(24)
        assert float(data['leading_bound']) == pytest.approx(2.0)

    def test_hellerman_c24(self):
        """Hellerman bound at c = 24: Delta <= 2 + O(1)."""
        data = hellerman_bound_from_shadow(24)
        assert data['full_bound'] > 2.0  # bound > actual gap
        assert data['full_bound'] < 3.0  # bound not too loose

    def test_hellerman_not_applicable_c_le_1(self):
        """Hellerman bound is not applicable for c <= 1."""
        data = hellerman_bound_from_shadow(Rational(1, 2))
        assert data['hellerman_constant'] == float('inf')

    def test_hellerman_kappa_identification(self):
        """Leading bound c/12 = kappa/6 is determined by kappa."""
        for c_val in [2, 10, 24, 100]:
            data = hellerman_bound_from_shadow(c_val)
            kappa = float(data['kappa'])
            leading = float(data['leading_bound'])
            assert abs(leading - kappa / 6.0) < 1e-10

    def test_monster_near_saturation(self):
        """Monster module (c=24) nearly saturates the Hellerman bound."""
        result = verify_monster_bootstrap()
        assert result['gap_below_hellerman']
        assert result['near_saturation']

    def test_hellerman_increases_with_c(self):
        """Hellerman bound increases with c."""
        bounds = []
        for c_val in [2, 5, 10, 24, 50]:
            data = hellerman_bound_from_shadow(c_val)
            bounds.append(data['full_bound'])
        for i in range(len(bounds) - 1):
            assert bounds[i] < bounds[i + 1]


# ============================================================================
# 7. Genus-1 MC equation
# ============================================================================

class TestGenus1MC:
    """Verify genus-1 MC equation = torus constraint."""

    def test_genus1_partition_function(self):
        """F_1 = kappa/24 = c/48 for Virasoro."""
        data = genus1_mc_partition_function(Rational(1))
        assert data['F_1'] == Rational(1, 48)
        assert data['lambda_1'] == Rational(1, 24)

    def test_genus1_ising(self):
        """F_1(Ising) = 1/96."""
        data = genus1_mc_partition_function(Rational(1, 2))
        assert data['F_1'] == Rational(1, 96)

    def test_genus1_monster(self):
        """F_1(Monster) = 1/2."""
        data = genus1_mc_partition_function(Rational(24))
        assert data['F_1'] == Rational(1, 2)

    def test_genus1_torus_one_point(self):
        """Torus one-point function of T is proportional to E_2*."""
        data = genus1_mc_torus_one_point(Rational(1))
        assert data['mc_genus1_arity1']
        assert 'E_2*' in data['eisenstein_connection']

    def test_genus1_F1_matches_kappa_over_24(self):
        """F_1 = kappa/24 verified independently from lambda_1."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24), Rational(26)]:
            kappa = kappa_virasoro(c_val)
            F_1_from_formula = kappa / 24
            F_1_from_lambda = kappa * lambda_fp(1)
            assert simplify(F_1_from_formula - F_1_from_lambda) == 0


# ============================================================================
# 8. Modular bootstrap + shadow
# ============================================================================

class TestModularBootstrap:
    """Verify modular bootstrap compatibility with shadow tower."""

    def test_modular_shadow_c1(self):
        """Shadow F_g values are consistent with modular invariance at c=1."""
        data = modular_bootstrap_shadow_verification(Rational(1))
        assert data['modular_consistent']
        assert data['F_values_positive']
        assert data['bernoulli_decay_holds']

    def test_modular_shadow_c24(self):
        """Shadow F_g values consistent at c=24 (Monster)."""
        data = modular_bootstrap_shadow_verification(Rational(24))
        assert data['modular_consistent']

    def test_bernoulli_decay(self):
        """F_g / (2pi)^{2g} decreases with g (Bernoulli decay)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            data = modular_bootstrap_shadow_verification(c_val)
            assert data['bernoulli_decay_holds']

    def test_F_g_positive_all_genera(self):
        """F_g > 0 for all g >= 1 and c > 0."""
        for c_val in [Rational(1, 2), Rational(1), Rational(24)]:
            data = modular_bootstrap_shadow_verification(c_val)
            assert data['F_values_positive']


# ============================================================================
# 9. Cardy formula
# ============================================================================

class TestCardyFormula:
    """Verify Cardy formula from the genus-1 shadow."""

    def test_cardy_exponent_from_kappa(self):
        """log rho ~ 2 pi sqrt(c Delta / 3) = 2 pi sqrt(2 kappa Delta / 3)."""
        c_val = 24.0
        Delta = 10.0
        data = cardy_from_shadow(c_val, [Delta])
        result = data['cardy_densities'][Delta]
        assert result['consistent']

    def test_cardy_high_temperature(self):
        """log Z ~ pi^2 c / (3 beta) = 4 pi^2 kappa / (3 beta)."""
        c_val = 24.0
        data = cardy_from_shadow(c_val)
        for beta, result in data['high_temp'].items():
            assert result['consistent']

    def test_cardy_c_from_kappa_equivalence(self):
        """The Cardy exponent expressed via c and via kappa must agree."""
        for c_val in [1.0, 10.0, 24.0, 100.0]:
            kappa = c_val / 2.0
            Delta = 5.0
            exp_c = 2 * math.pi * math.sqrt(c_val * Delta / 3.0)
            exp_k = 2 * math.pi * math.sqrt(2 * kappa * Delta / 3.0)
            assert abs(exp_c - exp_k) < 1e-10

    def test_cardy_subleading_c1_at_large_delta(self):
        """Subleading Cardy correction is small at large Delta."""
        result = cardy_subleading_from_shadow(24.0, 100.0)
        ratio = abs(result['c_1'] / math.sqrt(100.0)) / result['S_0']
        assert ratio < 0.1

    def test_cardy_large_c_accuracy(self):
        """Cardy formula becomes accurate at large c."""
        result = verify_c_large_cardy(100.0)
        assert result['cardy_accurate']

    def test_cardy_ising_exponent(self):
        """Cardy exponent at c=1/2, Delta=1 matches direct computation."""
        c_val = 0.5
        Delta = 1.0
        S_0_expected = 2 * math.pi * math.sqrt(c_val * Delta / 3.0)
        result = cardy_subleading_from_shadow(c_val, Delta)
        assert abs(result['S_0'] - S_0_expected) < 1e-10


# ============================================================================
# 10. Gap bounds from shadow tower
# ============================================================================

class TestGapBounds:
    """Verify spectral gap bounds from the shadow tower."""

    def test_gap_bound_c24(self):
        """Shadow gap bound at c=24 is finite and near Hellerman."""
        data = shadow_tower_gap_bound(24.0, max_genus=3)
        assert 'genus_1' in data['bounds']
        assert data['bounds']['genus_1'] > 2.0  # above actual gap
        assert data['bounds']['genus_1'] < 3.0

    def test_gap_bounds_tighten(self):
        """Higher-genus bounds are tighter than lower-genus bounds."""
        data = shadow_tower_gap_bound(24.0, max_genus=3)
        assert data['bounds_tighten']

    def test_gap_bound_not_applicable_small_c(self):
        """For c <= 0, no meaningful bound."""
        data = shadow_tower_gap_bound(0.0)
        assert data['bounds'] == {}

    def test_gap_bound_increases_with_c(self):
        """The genus-1 bound (c/12 + O(1)) increases with c for c > 1."""
        b5 = shadow_tower_gap_bound(5.0)['bounds']['genus_1']
        b10 = shadow_tower_gap_bound(10.0)['bounds']['genus_1']
        b24 = shadow_tower_gap_bound(24.0)['bounds']['genus_1']
        assert b5 < b10 < b24


# ============================================================================
# 11. Monster module
# ============================================================================

class TestMonsterBootstrap:
    """Verify bootstrap for the Monster module (c=24)."""

    def test_monster_F1(self):
        """F_1(Monster) = 1/2."""
        result = verify_monster_bootstrap()
        assert result['F_1_is_half']

    def test_monster_gap(self):
        """Monster gap h=2 is below Hellerman bound."""
        result = verify_monster_bootstrap()
        assert result['gap_below_hellerman']

    def test_monster_kappa(self):
        """kappa(V-natural) = 12.

        AP48: this is kappa = c/2 for the VIRASORO subalgebra.
        For the Monster MODULE, the Virasoro formula applies
        because V-natural has no weight-1 currents (dim V_1 = 0).
        """
        result = verify_monster_bootstrap()
        assert result['kappa'] == Rational(12)


# ============================================================================
# 12. MC hierarchy
# ============================================================================

class TestMCHierarchy:
    """Verify the MC equation hierarchy across genera and arities."""

    def test_hierarchy_genus0_arity2(self):
        """(0,2) projection = kappa."""
        h = mc_hierarchy_virasoro(Rational(1, 2))
        assert h[(0, 2)]['value'] == Rational(1, 4)

    def test_hierarchy_genus0_arity3(self):
        """(0,3) projection = cubic shadow S_3 = 2."""
        h = mc_hierarchy_virasoro(Rational(1, 2))
        assert h[(0, 3)]['value'] == Rational(2)

    def test_hierarchy_genus0_arity4(self):
        """(0,4) projection = quartic contact Q^contact."""
        h = mc_hierarchy_virasoro(Rational(1, 2))
        assert h[(0, 4)]['value'] == Rational(40, 49)

    def test_hierarchy_genus1_arity0(self):
        """(1,0) projection = F_1 = kappa/24."""
        h = mc_hierarchy_virasoro(Rational(1, 2))
        assert h[(1, 0)]['value'] == Rational(1, 96)

    def test_hierarchy_genus2_with_planted_forest(self):
        """(2,0) projection includes planted-forest correction."""
        h = mc_hierarchy_virasoro(Rational(1, 2))
        F_2_scalar = h[(2, 0)]['value']
        delta_pf = h[(2, 0)]['delta_pf']
        F_2_total = h[(2, 0)]['F_2_total']
        assert simplify(F_2_total - F_2_scalar - delta_pf) == 0

    def test_hierarchy_all_positive_c24(self):
        """All scalar F_g are positive at c = 24."""
        h = mc_hierarchy_virasoro(Rational(24), max_genus=3)
        for g in range(1, 4):
            assert h[(g, 0)]['value'] > 0


# ============================================================================
# 13. Minimal model landscape
# ============================================================================

class TestMinimalModelLandscape:
    """Verify shadow bootstrap data for the minimal model series."""

    def test_minimal_model_series(self):
        """Shadow data computed for m = 3 to 20."""
        results = shadow_bootstrap_minimal_models()
        assert len(results) == 18  # m = 3, 4, ..., 20

    def test_ising_in_series(self):
        """Ising model (m=3) appears with correct data."""
        results = shadow_bootstrap_minimal_models()
        ising = results[0]  # m=3
        assert ising['m'] == 3
        assert ising['c'] == Rational(1, 2)
        assert ising['kappa'] == Rational(1, 4)

    def test_minimal_model_c_increases(self):
        """Central charges increase toward c=1 as m -> infinity."""
        results = shadow_bootstrap_minimal_models()
        c_vals = [float(r['c']) for r in results]
        for i in range(len(c_vals) - 1):
            assert c_vals[i] < c_vals[i + 1]
        assert c_vals[-1] < 1.0  # never reaches 1

    def test_minimal_model_gap_formula(self):
        """Gap h_{2,1} = (m+3)/(4m) for M(m+1, m)."""
        results = shadow_bootstrap_minimal_models()
        for r in results:
            m = r['m']
            expected_gap = Rational(m + 3, 4 * m)
            assert r['gap'] == expected_gap

    def test_minimal_model_Q_contact_positive(self):
        """Q^contact > 0 for all minimal models."""
        results = shadow_bootstrap_minimal_models()
        for r in results:
            if r['Q_contact'] is not None:
                assert r['Q_contact'] > 0


# ============================================================================
# 14. Landscape scan
# ============================================================================

class TestBootstrapLandscape:
    """Verify the landscape scan across central charges."""

    def test_landscape_scan_runs(self):
        """Landscape scan produces results for all central charges."""
        results = bootstrap_landscape_scan()
        assert len(results) == 9

    def test_landscape_kappa_correct(self):
        """kappa = c/2 throughout the landscape."""
        results = bootstrap_landscape_scan()
        for r in results:
            c_f = float(r['c'])
            k_f = float(r['kappa'])
            assert abs(k_f - c_f / 2.0) < 1e-10

    def test_landscape_known_gaps(self):
        """Known gaps are below Hellerman bounds where applicable."""
        results = bootstrap_landscape_scan()
        for r in results:
            if 'known_gap' in r and 'gap_below_hellerman' in r:
                assert r['gap_below_hellerman']


# ============================================================================
# 15. Cross-checks and consistency
# ============================================================================

class TestCrossChecks:
    """Cross-checks between different computations."""

    def test_F1_from_two_formulas(self):
        """F_1 = kappa/24 vs F_1 = kappa * lambda_1^FP."""
        for c_val in [Rational(1, 2), Rational(1), Rational(7, 10), Rational(24)]:
            kappa = kappa_virasoro(c_val)
            f1_direct = kappa / 24
            f1_lambda = kappa * lambda_fp(1)
            assert simplify(f1_direct - f1_lambda) == 0

    def test_F2_scalar_from_bernoulli(self):
        """F_2 = kappa * 7/5760 verified from Bernoulli number."""
        # B_4 = -1/30, lambda_2 = (2^3-1)/2^3 * (1/30) / 24 = 7/8 * 1/720 = 7/5760
        kappa = kappa_virasoro(Rational(24))  # = 12
        F_2 = F_g_shadow(kappa, 2)
        expected = kappa * Rational(7, 5760)
        assert simplify(F_2 - expected) == 0

    def test_complementarity_kappa_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (not 0)."""
        for c_val in [Rational(1, 2), Rational(1), Rational(13), Rational(24)]:
            k = kappa_virasoro(c_val)
            k_dual = kappa_virasoro(26 - c_val)
            assert simplify(k + k_dual - 13) == 0

    def test_self_dual_point_c13(self):
        """At c = 13: kappa = kappa_dual = 13/2."""
        kappa_13 = kappa_virasoro(Rational(13))
        kappa_13_dual = kappa_virasoro(Rational(13))
        assert kappa_13 == kappa_13_dual
        assert kappa_13 == Rational(13, 2)

    def test_cardy_matches_modular(self):
        """Cardy exponent 2pi sqrt(c Delta/3) uses the SAME c as kappa = c/2."""
        c_val = 10.0
        kappa = c_val / 2.0
        Delta = 5.0

        # From c directly
        exp_c = 2 * math.pi * math.sqrt(c_val * Delta / 3.0)
        # From kappa
        exp_k = 2 * math.pi * math.sqrt(2 * kappa * Delta / 3.0)

        assert abs(exp_c - exp_k) < 1e-10

    def test_planted_forest_vanishes_heisenberg(self):
        """delta_pf^{(2,0)} = 0 for Heisenberg (S_3 = 0)."""
        # Heisenberg has S_3 = 0 (class G)
        kappa = kappa_heisenberg(1)  # = 1
        S_3 = Rational(0)  # class G: no cubic
        delta_pf = shadow_planted_forest_genus2(kappa, S_3)
        assert delta_pf == 0

    def test_planted_forest_nonzero_virasoro(self):
        """delta_pf^{(2,0)} != 0 for Virasoro (S_3 = 2)."""
        kappa = kappa_virasoro(Rational(24))
        S_3 = Rational(2)
        delta_pf = shadow_planted_forest_genus2(kappa, S_3)
        assert delta_pf != 0

    def test_Q_contact_pole_at_c0(self):
        """Q^contact has a pole at c = 0."""
        with pytest.raises((ValueError, ZeroDivisionError)):
            Q_contact_virasoro(Rational(0))

    def test_Q_contact_pole_at_c_neg22_5(self):
        """Q^contact has a pole at c = -22/5."""
        with pytest.raises((ValueError, ZeroDivisionError)):
            Q_contact_virasoro(Rational(-22, 5))

    def test_shadow_hierarchy_single_mc_element(self):
        """All hierarchy components are projections of a single MC element.

        Consistency check: the genus-0 data (kappa, S_3, S_4)
        constrains the genus-1 data (F_1) and genus-2 data (F_2 + delta_pf)
        through the MC equation.
        """
        h = mc_hierarchy_virasoro(Rational(24), max_genus=3)

        # kappa determines F_1
        kappa = h[(0, 2)]['value']
        F_1 = h[(1, 0)]['value']
        assert simplify(F_1 - kappa / 24) == 0

        # S_3 and kappa determine delta_pf at genus 2
        S_3 = h[(0, 3)]['value']
        delta_pf = h[(2, 0)]['delta_pf']
        expected_delta_pf = S_3 * (10 * S_3 - kappa) / 48
        assert simplify(delta_pf - expected_delta_pf) == 0
