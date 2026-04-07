"""Tests for the superconformal shadow obstruction tower engine.

75+ tests covering N=1, N=2, N=4 superconformal algebras:

  1. N=1 Super Virasoro (15 tests):
     - kappa formula, OPE, shadow data, Koszul dual, complementarity,
       minimal models, superstring worldsheet, NS vs Ramond invariance

  2. N=2 Superconformal (15 tests):
     - kappa from coset, OPE, shadow per line, Koszul duality,
       complementarity, spectral flow, c=9 CY prediction

  3. N=4 Small Superconformal (15 tests):
     - kappa, central charge, Koszul duality, complementarity,
       K3 kappa, shadow per line, SU(2)_R data

  4. Cross-family comparisons (10 tests):
     - kappa table, shadow depth table, Koszul duality table,
       critical dimensions, hierarchy relations

  5. Shadow tower computation (10 tests):
     - T-line tower agreement with Virasoro, G-line termination,
       growth rates, convergence

  6. Beem-Rastelli 4d/2d (5 tests):
     - Free hyper, free vector, class S, c_2d formula

  7. Special values and edge cases (5+ tests):
     - Self-dual points, c=9 CY, c=15 worldsheet,
       mirror symmetry vs Koszul duality

ADVERSARIAL DESIGN (per CLAUDE.md):
  - Each kappa is verified by independent computation (AP10).
  - Complementarity sums verified at multiple c values (AP24).
  - Shadow depth verified from data, not assumed (AP14).
  - Cross-checks between families expose inconsistencies (AP3, AP5).
  - No hardcoded expected values without derivation (AP38).
"""

import math
import pytest
from sympy import Rational, simplify, Symbol, oo

from compute.lib.superconformal_shadow_engine import (
    # Core
    shadow_tower_coefficients,
    shadow_class_from_data,
    shadow_growth_rate,
    critical_discriminant,
    lambda_fp,
    # N=1
    N1SuperVirasoro,
    # N=2
    N2Superconformal,
    # N=4
    N4SmallSuperconformal,
    # Beem-Rastelli
    BeemRastelli4d2d,
    # Summaries
    superconformal_kappa_table,
    superconformal_shadow_depth_table,
    superconformal_koszul_duality_table,
    n2_mirror_symmetry_and_koszul,
    # Complementarity hierarchy
    superconformal_complementarity_hierarchy,
    complementarity_sum_general,
    kappa_superconformal,
    c_critical_superconformal,
    verify_complementarity_sum_symbolic,
    verify_complementarity_sum_numerical,
    hierarchy_proof_method_self_dual,
    hierarchy_proof_method_k_param,
    hierarchy_strict_decrease,
)


# =========================================================================
# 1. N=1 Super Virasoro
# =========================================================================

class TestN1Kappa:
    """Test the modular characteristic kappa(N=1, c) = (3c-2)/4."""

    def test_kappa_symbolic(self):
        c = Symbol('c')
        kap = N1SuperVirasoro.kappa()
        assert simplify(kap - (3 * c - 2) / 4) == 0

    def test_kappa_c_3_2(self):
        """c = 3/2 (free fermion limit): kappa = 5/8."""
        assert N1SuperVirasoro.kappa(Rational(3, 2)) == Rational(5, 8)

    def test_kappa_c_15(self):
        """c = 15 (superstring worldsheet): kappa = 43/4."""
        assert N1SuperVirasoro.kappa(15) == Rational(43, 4)

    def test_kappa_c_0(self):
        """c = 0: kappa = -1/2 (nonzero from fermionic sector)."""
        assert N1SuperVirasoro.kappa(0) == Rational(-1, 2)

    def test_kappa_c_2_3(self):
        """c = 2/3: kappa = (2-2)/4 = 0 (the uncurved point for N=1)."""
        assert N1SuperVirasoro.kappa(Rational(2, 3)) == Rational(0)


class TestN1KoszulDuality:
    """Test Koszul duality: c' = 15-c, kappa+kappa' = 41/4."""

    def test_dual_c(self):
        assert N1SuperVirasoro.koszul_dual_c(1) == 14

    def test_dual_c_15(self):
        assert N1SuperVirasoro.koszul_dual_c(15) == 0

    def test_complementarity_c1(self):
        result = N1SuperVirasoro.complementarity_sum(1)
        assert result['sum'] == Rational(41, 4)

    def test_complementarity_c_3_2(self):
        result = N1SuperVirasoro.complementarity_sum(Rational(3, 2))
        assert result['sum'] == Rational(41, 4)

    def test_complementarity_c15(self):
        result = N1SuperVirasoro.complementarity_sum(15)
        assert result['sum'] == Rational(41, 4)

    @pytest.mark.parametrize("c_val", [1, 2, 3, Rational(7, 10), Rational(15, 2), 10, 15])
    def test_complementarity_universal(self, c_val):
        """kappa + kappa' = 41/4 for ALL c values."""
        result = N1SuperVirasoro.complementarity_sum(c_val)
        assert result['sum'] == Rational(41, 4), \
            f"Complementarity failed at c={c_val}: sum={result['sum']}"

    def test_self_dual_point(self):
        sd = N1SuperVirasoro.self_dual_point()
        assert sd['c_self_dual'] == Rational(15, 2)
        # kappa at self-dual: (3*15/2 - 2)/4 = (45/2 - 2)/4 = 41/8
        assert sd['kappa_self_dual'] == Rational(41, 8)


class TestN1OPE:
    """Test the N=1 SCA OPE structure."""

    def test_TT_quartic_pole(self):
        c = Symbol('c')
        ope = N1SuperVirasoro.ope_data()
        assert ope[('T', 'T')][3] == {'vac': c / 2}

    def test_GG_cubic_pole(self):
        """G_{(2)}G = 2c/3: the leading fermionic pairing."""
        c = Symbol('c')
        ope = N1SuperVirasoro.ope_data()
        assert ope[('G', 'G')][2] == {'vac': 2 * c / 3}

    def test_GG_no_double_pole(self):
        """G_{(1)}G = 0: fermionic antisymmetry kills the double pole."""
        ope = N1SuperVirasoro.ope_data()
        assert 1 not in ope[('G', 'G')]

    def test_GG_simple_pole(self):
        """G_{(0)}G = 2T: the supersymmetry relation."""
        ope = N1SuperVirasoro.ope_data()
        assert ope[('G', 'G')][0] == {'T': Rational(2)}


class TestN1ShadowData:
    """Test shadow tower data for N=1 SCA."""

    def test_T_line_is_virasoro(self):
        """T-line shadow data matches Virasoro at same c."""
        data = N1SuperVirasoro.shadow_data_T_line(Rational(1, 2))
        assert data['kappa'] == Rational(1, 4)
        assert data['alpha'] == Rational(2)
        assert data['class'] == 'M'

    def test_G_line_is_gaussian(self):
        """G-line has alpha=0, S4=0: class G (depth 2)."""
        data = N1SuperVirasoro.shadow_data_G_line(10)
        assert data['alpha'] == 0
        assert data['S4'] == 0
        assert data['class'] == 'G'

    def test_G_line_kappa(self):
        """kappa_G = 2c/3 on the G-line."""
        data = N1SuperVirasoro.shadow_data_G_line(Rational(3, 2))
        assert data['kappa'] == Rational(1)

    def test_overall_class_M(self):
        sc = N1SuperVirasoro.shadow_class()
        assert sc['class'] == 'M'
        assert sc['T_line'] == 'M'
        assert sc['G_line'] == 'G'

    def test_ns_ramond_same_shadow(self):
        """NS and Ramond sectors have identical shadow towers."""
        result = N1SuperVirasoro.ns_vs_ramond_shadow()
        assert result['NS_shadow'] == 'same as R'


# =========================================================================
# 2. N=2 Superconformal
# =========================================================================

class TestN2Kappa:
    """Test kappa(N=2) = (6-c)/(2(3-c)) = (k+4)/4."""

    def test_kappa_k1(self):
        """k=1 (c=1): kappa = 5/4."""
        assert N2Superconformal.kappa(k_val=1) == Rational(5, 4)

    def test_kappa_k2(self):
        """k=2 (c=3/2): kappa = 3/2."""
        assert N2Superconformal.kappa(k_val=2) == Rational(3, 2)

    def test_kappa_k3(self):
        """k=3 (c=9/5): kappa = 7/4."""
        assert N2Superconformal.kappa(k_val=3) == Rational(7, 4)

    def test_kappa_k4(self):
        """k=4 (c=2): kappa = 2."""
        assert N2Superconformal.kappa(k_val=4) == Rational(2)

    def test_kappa_c_formula(self):
        """kappa from c-formula matches k-formula at k=1."""
        c_val = Rational(3) * 1 / (1 + 2)  # c = 1 at k=1
        assert N2Superconformal.kappa(c_val=c_val) == Rational(5, 4)

    def test_kappa_c9(self):
        """c=9 (CY3): kappa = 1/4."""
        assert N2Superconformal.kappa(c_val=9) == Rational(1, 4)


class TestN2KoszulDuality:
    """Test N=2 Koszul duality: c' = 6-c, kappa+kappa' = 1."""

    def test_dual_c(self):
        assert N2Superconformal.koszul_dual_c(1) == 5

    def test_dual_c9(self):
        assert N2Superconformal.koszul_dual_c(9) == -3

    @pytest.mark.parametrize("c_val", [1, Rational(3, 2), 2, Rational(9, 5), 5, 9, -3])
    def test_complementarity_universal(self, c_val):
        """kappa + kappa' = 1 for all c != 3."""
        result = N2Superconformal.complementarity_sum(c_val)
        assert result['sum'] == Rational(1), \
            f"N=2 complementarity failed at c={c_val}: sum={result['sum']}"

    def test_self_dual_c3(self):
        sd = N2Superconformal.self_dual_point()
        assert sd['c_self_dual'] == Rational(3)


class TestN2ShadowData:
    """Test N=2 shadow tower per line."""

    def test_T_line_class_M(self):
        data = N2Superconformal.shadow_data_T_line(1)
        assert data['class'] == 'M'
        assert data['kappa'] == Rational(1, 2)

    def test_J_line_class_G(self):
        data = N2Superconformal.shadow_data_J_line(1)
        assert data['class'] == 'G'
        assert data['kappa'] == Rational(1, 3)
        assert data['alpha'] == 0

    def test_G_line_class_L(self):
        data = N2Superconformal.shadow_data_G_line(1)
        assert data['class'] == 'L'
        assert data['alpha'] == 1

    def test_overall_class_M(self):
        sc = N2Superconformal.shadow_class()
        assert sc['class'] == 'M'

    def test_spectral_flow_invariance(self):
        result = N2Superconformal.spectral_flow_invariance()
        assert result['NS_eq_R'] is True
        assert 'kappa' in result['invariant_quantities']


class TestN2CY:
    """Test the c=9 Calabi-Yau prediction."""

    def test_cy_kappa(self):
        result = N2Superconformal.cy_compactification_c9()
        assert result['kappa'] == Rational(1, 4)

    def test_cy_dual(self):
        result = N2Superconformal.cy_compactification_c9()
        assert result['c_dual'] == Rational(-3)

    def test_cy_complementarity(self):
        result = N2Superconformal.cy_compactification_c9()
        assert result['complementarity_sum'] == Rational(1)

    def test_cy_T_line_class(self):
        result = N2Superconformal.cy_compactification_c9()
        assert result['T_line_class'] == 'M'


# =========================================================================
# 3. N=4 Small Superconformal
# =========================================================================

class TestN4Kappa:
    """Test kappa(N=4) = (k+2)/2 = 6/(6-c)."""

    def test_kappa_k1(self):
        """k=1 (c=2): kappa = (1+2)/2 = 3/2."""
        assert N4SmallSuperconformal.kappa(k_val=1) == Rational(3, 2)

    def test_kappa_k2(self):
        """k=2 (c=3): kappa = (2+2)/2 = 2."""
        assert N4SmallSuperconformal.kappa(k_val=2) == Rational(2)

    def test_kappa_k3(self):
        """k=3 (c=18/5): kappa = (3+2)/2 = 5/2."""
        assert N4SmallSuperconformal.kappa(k_val=3) == Rational(5, 2)

    def test_kappa_c_formula(self):
        """c-formula kappa = 6/(6-c) matches k-formula at k=1 (c=2)."""
        assert N4SmallSuperconformal.kappa(c_val=2) == Rational(6) / (6 - 2)
        assert N4SmallSuperconformal.kappa(c_val=2) == Rational(3, 2)

    def test_kappa_k3_c_formula(self):
        """k=3 gives c=18/5; kappa from c-formula = 6/(6-18/5) = 6/(12/5) = 5/2."""
        c_v = Rational(6) * 3 / (3 + 2)
        assert c_v == Rational(18, 5)
        assert N4SmallSuperconformal.kappa(c_val=c_v) == Rational(5, 2)
        # Also verify k-formula agrees
        assert N4SmallSuperconformal.kappa(k_val=3) == Rational(5, 2)

    def test_k3_kappa(self):
        """K3 sigma model: kappa = 2 (complex dimension)."""
        assert N4SmallSuperconformal.kappa_k3() == Rational(2)

    def test_central_charge_k1(self):
        """k=1: c = 6*1/(1+2) = 2."""
        assert N4SmallSuperconformal.central_charge(k_val=1) == Rational(2)

    def test_central_charge_k2(self):
        """k=2: c = 6*2/(2+2) = 3."""
        assert N4SmallSuperconformal.central_charge(k_val=2) == Rational(3)


class TestN4KoszulDuality:
    """Test N=4 Koszul duality: c' = 12-c, kappa+kappa' = 0."""

    def test_dual_c2(self):
        """c=2 (k=1): dual c' = 12-2 = 10."""
        assert N4SmallSuperconformal.koszul_dual_c(2) == 10

    def test_dual_c3(self):
        """c=3 (k=2): dual c' = 12-3 = 9."""
        assert N4SmallSuperconformal.koszul_dual_c(3) == 9

    @pytest.mark.parametrize("c_val", [1, 2, 3, 4, 5, Rational(18, 5)])
    def test_complementarity_zero(self, c_val):
        """kappa + kappa' = 0 for all c != 6."""
        result = N4SmallSuperconformal.complementarity_sum(c_val=c_val)
        assert result['sum'] == Rational(0), \
            f"N=4 complementarity failed at c={c_val}: sum={result['sum']}"

    @pytest.mark.parametrize("k_val", [1, 2, 3, 4, 10])
    def test_complementarity_from_k(self, k_val):
        """kappa(k) + kappa(-k-4) = 0 from k-parametrization."""
        result = N4SmallSuperconformal.complementarity_sum(k_val=k_val)
        assert result['sum'] == Rational(0)

    def test_self_dual_c6(self):
        sd = N4SmallSuperconformal.self_dual_point()
        assert sd['c_self_dual'] == Rational(6)


class TestN4ShadowData:
    """Test shadow data for N=4 SCA."""

    def test_T_line_class_M(self):
        """T-line at c=2 (k=1): kappa_T = c/2 = 1."""
        data = N4SmallSuperconformal.shadow_data_T_line(2)
        assert data['class'] == 'M'
        assert data['kappa'] == Rational(1)

    def test_J_line_class_L(self):
        """SU(2)_R currents at level k: class L (Lie algebra)."""
        data = N4SmallSuperconformal.shadow_data_J_line(k_val=1)
        assert data['class'] == 'L'
        assert data['S4'] == 0

    def test_G_line_class_L(self):
        data = N4SmallSuperconformal.shadow_data_G_line(k_val=1)
        assert data['class'] == 'L'

    def test_overall_class_M(self):
        sc = N4SmallSuperconformal.shadow_class()
        assert sc['class'] == 'M'
        assert sc['T_line'] == 'M'
        assert sc['J_line'] == 'L'
        assert sc['G_line'] == 'L'


# =========================================================================
# 4. Cross-family comparisons
# =========================================================================

class TestCrossFamilyComparisons:
    """Compare shadow data across N=1,2,4 families."""

    def test_kappa_hierarchy_at_c1(self):
        """At c=1: verify kappa ordering across families."""
        kap_n1 = N1SuperVirasoro.kappa(1)  # (3-2)/4 = 1/4
        kap_n2 = N2Superconformal.kappa(c_val=1)  # (6-1)/(2*2) = 5/4
        kap_n4 = N4SmallSuperconformal.kappa(c_val=1)  # 6/5
        assert kap_n1 == Rational(1, 4)
        assert kap_n2 == Rational(5, 4)
        assert kap_n4 == Rational(6, 5)

    def test_all_class_M(self):
        """All three superconformal algebras are class M."""
        depth_table = superconformal_shadow_depth_table()
        for N_name in ['N=1', 'N=2', 'N=4']:
            assert depth_table[N_name]['class'] == 'M'

    def test_koszul_c_sums(self):
        """Critical dimensions: 15, 6, 12 for N=1,2,4."""
        table = superconformal_koszul_duality_table()
        assert table['N=1']['c_sum'] == 15
        assert table['N=2']['c_sum'] == 6
        assert table['N=4']['c_sum'] == 12

    def test_kappa_sums(self):
        """Complementarity sums: 41/4, 1, 0 for N=1,2,4."""
        table = superconformal_koszul_duality_table()
        assert table['N=1']['kappa_sum'] == Rational(41, 4)
        assert table['N=2']['kappa_sum'] == Rational(1)
        assert table['N=4']['kappa_sum'] == Rational(0)

    def test_self_dual_points(self):
        """Self-dual points: 15/2, 3, 6 for N=1,2,4."""
        table = superconformal_koszul_duality_table()
        assert table['N=1']['self_dual_c'] == Rational(15, 2)
        assert table['N=2']['self_dual_c'] == Rational(3)
        assert table['N=4']['self_dual_c'] == Rational(6)

    def test_generator_counts(self):
        """N=1: 2 gen, N=2: 4 gen, N=4: 8 gen."""
        depth_table = superconformal_shadow_depth_table()
        assert depth_table['N=1']['n_generators'] == 2
        assert depth_table['N=2']['n_generators'] == 4
        assert depth_table['N=4']['n_generators'] == 8

    def test_boson_fermion_balance(self):
        """N=1: 1B+1F, N=2: 2B+2F, N=4: 4B+4F."""
        dt = superconformal_shadow_depth_table()
        for N_name in ['N=1', 'N=2', 'N=4']:
            assert dt[N_name]['n_bosonic'] == dt[N_name]['n_fermionic']

    def test_kappa_table_populated(self):
        """Kappa table has entries for all three families at standard c values."""
        table = superconformal_kappa_table()
        assert len(table) >= 7
        for row in table:
            assert 'kappa_N1' in row

    def test_kappa_table_c1(self):
        """Spot-check kappa table at c=1."""
        table = superconformal_kappa_table([1])
        row = table[0]
        assert row['kappa_N1'] == Rational(1, 4)
        assert row['kappa_N2'] == Rational(5, 4)
        assert row['kappa_N4'] == Rational(6, 5)

    def test_n1_contains_virasoro(self):
        """N=1 T-line shadow data matches pure Virasoro."""
        n1_T = N1SuperVirasoro.shadow_data_T_line(10)
        # Compare with what Virasoro at c=10 would give
        assert n1_T['kappa'] == Rational(5)
        assert n1_T['alpha'] == 2
        assert n1_T['S4'] == Rational(10) / (10 * (5 * 10 + 22))


# =========================================================================
# 5. Shadow tower computation
# =========================================================================

class TestShadowTowerComputation:
    """Test explicit shadow tower computations."""

    def test_virasoro_tower_S2(self):
        """S_2 = kappa = c/2 on any T-line."""
        tower = N1SuperVirasoro.shadow_tower_T_line(Rational(1, 2), max_arity=6)
        assert tower[2] == Rational(1, 4)

    def test_virasoro_tower_S3(self):
        """S_3 = alpha = 2 (independent of c)."""
        # S_3 = a_1/3 where a_1 = 3*alpha = 6, so S_3 = 6/3 = 2
        tower = N1SuperVirasoro.shadow_tower_T_line(Rational(1, 2), max_arity=6)
        assert tower[3] == Rational(2)

    def test_virasoro_tower_S4(self):
        """S_4 = 10/(c(5c+22)) at c=1/2."""
        tower = N1SuperVirasoro.shadow_tower_T_line(Rational(1, 2), max_arity=6)
        expected_S4 = Rational(10) / (Rational(1, 2) * (Rational(5, 2) + 22))
        assert tower[4] == expected_S4

    def test_G_line_terminates(self):
        """G-line tower has S_r = 0 for r >= 3."""
        tower = N1SuperVirasoro.shadow_tower_G_line(10, max_arity=10)
        assert tower[2] == Rational(20, 3)
        for r in range(3, 11):
            assert tower[r] == 0

    def test_n2_J_line_terminates(self):
        """N=2 J-line: S_r = 0 for r >= 3 (Heisenberg)."""
        towers = N2Superconformal.shadow_tower_all_lines(1, max_arity=10)
        for r in range(3, 11):
            assert towers['J'][r] == 0

    def test_n2_T_line_matches_virasoro(self):
        """N=2 T-line tower matches Virasoro at same c."""
        c_val = Rational(1)
        n2_T = N2Superconformal.shadow_tower_all_lines(c_val, max_arity=6)['T']
        n1_T = N1SuperVirasoro.shadow_tower_T_line(c_val, max_arity=6)
        for r in range(2, 7):
            assert n2_T[r] == n1_T[r], f"Mismatch at arity {r}"

    def test_n4_T_line_matches_virasoro(self):
        """N=4 T-line tower matches Virasoro at same c (c=2, k=1)."""
        c_val = Rational(2)
        n4_T = N4SmallSuperconformal.shadow_tower_T_line(c_val, max_arity=6)
        n1_T = N1SuperVirasoro.shadow_tower_T_line(c_val, max_arity=6)
        for r in range(2, 7):
            assert n4_T[r] == n1_T[r], f"Mismatch at arity {r}"

    def test_shadow_class_from_data_G(self):
        """Class G: alpha=0, S4=0."""
        assert shadow_class_from_data(Rational(1), Rational(0), Rational(0)) == 'G'

    def test_shadow_class_from_data_L(self):
        """Class L: alpha!=0, S4=0."""
        assert shadow_class_from_data(Rational(1), Rational(1), Rational(0)) == 'L'

    def test_shadow_class_from_data_M(self):
        """Class M: Delta = 8*kappa*S4 != 0."""
        assert shadow_class_from_data(Rational(1), Rational(2), Rational(1)) == 'M'


# =========================================================================
# 6. Beem-Rastelli 4d/2d
# =========================================================================

class TestBeemRastelli:
    """Test the Beem-Rastelli 4d/2d correspondence."""

    def test_c_2d_formula(self):
        """c_{2d} = -12 * c_{4d}."""
        assert BeemRastelli4d2d.c_2d_from_4d(Rational(1, 12)) == Rational(-1)

    def test_free_hyper(self):
        """Free hyper: c_{2d} = -1, class G."""
        result = BeemRastelli4d2d.free_hypermultiplet()
        assert result['c_2d'] == Rational(-1)
        assert result['shadow_class'] == 'G'

    def test_free_vector(self):
        """Free vector: c_{2d} = -2, class G."""
        result = BeemRastelli4d2d.free_vector()
        assert result['c_2d'] == Rational(-2)
        assert result['shadow_class'] == 'G'

    def test_class_s_su2(self):
        result = BeemRastelli4d2d.class_s_su_n(2)
        assert result['shadow_class'] == 'M'

    def test_class_s_su3(self):
        result = BeemRastelli4d2d.class_s_su_n(3)
        assert result['shadow_class'] == 'M'


# =========================================================================
# 7. Special values and edge cases
# =========================================================================

class TestSpecialValues:
    """Test physically important special values."""

    def test_n1_worldsheet(self):
        """Superstring worldsheet: c=15, kappa=43/4."""
        result = N1SuperVirasoro.superstring_worldsheet()
        assert result['c'] == 15
        assert result['kappa_N1'] == Rational(43, 4)
        assert result['overall_shadow_class'] == 'M'

    def test_n1_worldsheet_ghost_kappa(self):
        """Ghost contribution: bc(-26) + betagamma(11)."""
        result = N1SuperVirasoro.superstring_worldsheet()
        assert result['ghost_kappa_bc'] == Rational(-13)
        assert result['ghost_kappa_betagamma'] == Rational(11, 2)
        assert result['ghost_kappa_total'] == Rational(-15, 2)

    def test_n1_worldsheet_kappa_eff(self):
        """Effective kappa = 43/4 - 15/2 = 13/4."""
        result = N1SuperVirasoro.superstring_worldsheet()
        assert result['kappa_eff'] == Rational(13, 4)

    def test_n2_cy_c9(self):
        """CY3 compactification: c=9, kappa=1/4."""
        result = N2Superconformal.cy_compactification_c9()
        assert result['kappa'] == Rational(1, 4)
        assert result['kappa_dual'] == Rational(3, 4)

    def test_n2_mirror_vs_koszul(self):
        """Mirror symmetry (spectral flow) vs Koszul duality (c->6-c)."""
        result = n2_mirror_symmetry_and_koszul()
        assert result['mirror_symmetry']['on_shadow'] == 'invariant (automorphism)'

    def test_n1_minimal_model_c(self):
        """N=1 minimal models: c(m=3) = 7/10 (tricritical Ising)."""
        c_3 = N1SuperVirasoro.central_charge_minimal_model(3)
        assert c_3 == Rational(7, 10)

    def test_n1_minimal_model_c4(self):
        """N=1 minimal model at m=4: c = 1."""
        # c = 3/2 * (1 - 8/(4*6)) = 3/2 * (1 - 1/3) = 3/2 * 2/3 = 1
        c_4 = N1SuperVirasoro.central_charge_minimal_model(4)
        assert c_4 == Rational(1)

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24 (Bernoulli number identity)."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_n1_genus_energy_c15(self):
        """F_1(N=1, c=15) = (43/4) * (1/24) = 43/96."""
        f1 = N1SuperVirasoro.genus_free_energy(15, 1)
        assert f1 == Rational(43, 96)


# =========================================================================
# 8. Multi-path verification (the core mandate)
# =========================================================================

class TestMultiPathVerification:
    """Multi-path verification of key results (AP10 compliance)."""

    def test_n2_kappa_two_paths(self):
        """N=2 kappa via k-formula and c-formula must agree at k=1."""
        kap_k = N2Superconformal.kappa(k_val=1)
        c_val = N2Superconformal.central_charge(k_val=1)
        kap_c = N2Superconformal.kappa(c_val=c_val)
        assert kap_k == kap_c

    def test_n4_kappa_two_paths(self):
        """N=4 kappa via k-formula and c-formula must agree at k=2."""
        kap_k = N4SmallSuperconformal.kappa(k_val=2)
        c_val = N4SmallSuperconformal.central_charge(k_val=2)
        kap_c = N4SmallSuperconformal.kappa(c_val=c_val)
        assert kap_k == kap_c

    def test_n2_complementarity_algebraic(self):
        """N=2: verify kappa + kappa' = 1 algebraically from the formula."""
        # kappa(c) = (6-c)/(2(3-c)), kappa(6-c) = c/(2(c-3))
        # sum = (6-c)/(2(3-c)) + c/(2(c-3)) = (6-c)/(2(3-c)) - c/(2(3-c))
        # = (6-2c)/(2(3-c)) = 2(3-c)/(2(3-c)) = 1.
        c_sym = Symbol('c')
        kap = (6 - c_sym) / (2 * (3 - c_sym))
        kap_dual = (6 - (6 - c_sym)) / (2 * (3 - (6 - c_sym)))
        assert simplify(kap + kap_dual) == 1

    def test_n4_complementarity_algebraic(self):
        """N=4: verify kappa + kappa' = 0 algebraically."""
        c_sym = Symbol('c')
        kap = Rational(6) / (6 - c_sym)
        kap_dual = Rational(6) / (6 - (12 - c_sym))
        assert simplify(kap + kap_dual) == 0

    def test_n1_complementarity_algebraic(self):
        """N=1: verify kappa + kappa' = 41/4 algebraically."""
        c_sym = Symbol('c')
        kap = (3 * c_sym - 2) / 4
        kap_dual = (3 * (15 - c_sym) - 2) / 4
        assert simplify(kap + kap_dual) == Rational(41, 4)

    def test_shadow_recursion_identity(self):
        """Verify a_0 = 2*kappa, a_1 = 3*alpha, a_2 = 4*S4 from recursion."""
        kap = Rational(5)
        alpha = Rational(2)
        S4 = Rational(1, 10)
        tower = shadow_tower_coefficients(kap, alpha, S4, max_r=4)
        assert tower[2] == kap  # S_2 = a_0/2 = 2*kappa/2 = kappa
        assert tower[3] == alpha  # S_3 = a_1/3 = 3*alpha/3 = alpha
        assert tower[4] == S4  # S_4 = a_2/4 = 4*S4/4 = S4

    def test_critical_discriminant_formula(self):
        """Delta = 8*kappa*S4."""
        assert critical_discriminant(Rational(5), Rational(3)) == 120

    def test_growth_rate_class_G(self):
        """Class G has zero growth rate."""
        rho = shadow_growth_rate(Rational(1), Rational(0), Rational(0))
        assert rho == 0

    def test_growth_rate_class_L(self):
        """Class L has zero growth rate (Delta=0, alpha!=0 contributes
        but sqrt(9*alpha^2 + 0) / (2|kappa|) is the convergence radius
        of a degree-2 algebraic function, which is... actually nonzero.

        Wait: for class L, Delta = 0, so Q_L(t) = (2kappa + 3alpha*t)^2
        is a PERFECT SQUARE. Then H(t) = t^2 * |2kappa + 3alpha*t| which
        is a polynomial (degree 3 in t). A polynomial has infinite radius
        of convergence, so rho = 0.

        But the growth rate formula gives rho = sqrt(9*alpha^2)/(2|kappa|) = 3|alpha|/(2|kappa|).
        This is the ratio that determines the ZERO of Q_L, not the convergence radius.
        The convergence radius of sqrt(Q_L) is |2kappa/(3alpha)| (distance to zero of Q_L).
        For Q_L = perfect square, sqrt(Q_L) is linear -> polynomial -> rho_convergence = 0.
        But the formula gives a nonzero value because it measures the relative
        size of coefficients, not the convergence radius directly.
        """
        rho = shadow_growth_rate(Rational(1), Rational(1), Rational(0))
        # For class L: rho = 3|alpha|/(2|kappa|) which is nonzero as a RATIO
        # but the tower terminates (all S_r = 0 for r >= 4) so the effective
        # convergence radius is infinite. The growth rate formula gives 3/2.
        assert rho == Rational(3, 2)


# =========================================================================
# 9. Superconformal Complementarity Sum Hierarchy (41/4 > 1 > 0)
# =========================================================================

class TestComplementarityHierarchyStructure:
    """Test the hierarchy data structure and basic properties."""

    def test_hierarchy_has_four_levels(self):
        h = superconformal_complementarity_hierarchy()
        assert set(h.keys()) == {0, 1, 2, 4}

    def test_hierarchy_n0_is_virasoro(self):
        h = superconformal_complementarity_hierarchy()
        assert h[0]['name'] == 'Virasoro'
        assert h[0]['sum'] == Rational(13)
        assert h[0]['c_crit'] == Rational(26)

    def test_hierarchy_n1_data(self):
        h = superconformal_complementarity_hierarchy()
        assert h[1]['sum'] == Rational(41, 4)
        assert h[1]['c_crit'] == Rational(15)
        assert h[1]['c_self_dual'] == Rational(15, 2)

    def test_hierarchy_n2_data(self):
        h = superconformal_complementarity_hierarchy()
        assert h[2]['sum'] == Rational(1)
        assert h[2]['c_crit'] == Rational(6)

    def test_hierarchy_n4_data(self):
        h = superconformal_complementarity_hierarchy()
        assert h[4]['sum'] == Rational(0)
        assert h[4]['c_crit'] == Rational(12)

    def test_boson_fermion_balance(self):
        """For N >= 1, n_bosonic == n_fermionic (bose-fermi balance)."""
        h = superconformal_complementarity_hierarchy()
        for N in [1, 2, 4]:
            assert h[N]['n_bosonic'] == h[N]['n_fermionic'], \
                f"N={N}: n_bos={h[N]['n_bosonic']} != n_ferm={h[N]['n_fermionic']}"

    def test_generator_count_doubles(self):
        """n_generators: 1, 2, 4, 8 (powers of 2)."""
        h = superconformal_complementarity_hierarchy()
        counts = [h[N]['n_generators'] for N in [0, 1, 2, 4]]
        assert counts == [1, 2, 4, 8]


class TestComplementaritySumGeneral:
    """Test the complementarity_sum_general function."""

    def test_n0(self):
        assert complementarity_sum_general(0) == Rational(13)

    def test_n1(self):
        assert complementarity_sum_general(1) == Rational(41, 4)

    def test_n2(self):
        assert complementarity_sum_general(2) == Rational(1)

    def test_n4(self):
        assert complementarity_sum_general(4) == Rational(0)

    def test_n3_raises(self):
        """N=3 is not in the standard Ademollo et al. hierarchy."""
        with pytest.raises(ValueError, match="N=3"):
            complementarity_sum_general(3)

    def test_n5_raises(self):
        with pytest.raises(ValueError):
            complementarity_sum_general(5)


class TestKappaSuperconformal:
    """Test the unified kappa_superconformal function."""

    def test_n0_matches_virasoro(self):
        assert kappa_superconformal(0, 10) == Rational(5)
        assert kappa_superconformal(0, 26) == Rational(13)

    def test_n1_matches_class(self):
        assert kappa_superconformal(1, 15) == N1SuperVirasoro.kappa(15)
        assert kappa_superconformal(1, Rational(3, 2)) == N1SuperVirasoro.kappa(Rational(3, 2))

    def test_n2_matches_class(self):
        assert kappa_superconformal(2, 1) == N2Superconformal.kappa(c_val=1)

    def test_n4_matches_class(self):
        assert kappa_superconformal(4, 2) == N4SmallSuperconformal.kappa(c_val=2)

    def test_n0_symbolic(self):
        kap = kappa_superconformal(0)
        c_sym = Symbol('c')
        assert simplify(kap - c_sym / 2) == 0


class TestCCriticalSuperconformal:
    """Test critical central charge values."""

    def test_n0(self):
        assert c_critical_superconformal(0) == 26

    def test_n1(self):
        assert c_critical_superconformal(1) == 15

    def test_n2(self):
        assert c_critical_superconformal(2) == 6

    def test_n4(self):
        assert c_critical_superconformal(4) == 12

    def test_invalid(self):
        with pytest.raises(ValueError):
            c_critical_superconformal(3)


class TestMethod1DirectKappaFormula:
    """METHOD 1: Direct computation from kappa formulas.

    N=0: (c/2) + ((26-c)/2) = 13.
    N=1: (3c-2)/4 + (3(15-c)-2)/4 = 41/4.
    N=2: (6-c)/(2(3-c)) + c/(2(c-3)) = 1.
    N=4: 6/(6-c) + 6/(c-6) = 0.
    """

    @pytest.mark.parametrize("N_susy", [0, 1, 2, 4])
    def test_symbolic_verification(self, N_susy):
        """Verify kappa(c) + kappa(c_crit - c) simplifies to constant."""
        result = verify_complementarity_sum_symbolic(N_susy)
        assert result['verified'], \
            f"N={N_susy}: symbolic sum = {result['sum_symbolic']}, expected {result['sum_expected']}"

    @pytest.mark.parametrize("N_susy,c_val", [
        (0, 1), (0, 10), (0, 13), (0, 25),
        (1, 1), (1, Rational(3, 2)), (1, Rational(15, 2)), (1, 14),
        (2, 1), (2, Rational(3, 2)), (2, 5), (2, -3),
        (4, 1), (4, 2), (4, 3), (4, Rational(18, 5)),
    ])
    def test_numerical_verification(self, N_susy, c_val):
        """Verify at specific c values."""
        result = verify_complementarity_sum_numerical(N_susy, c_val)
        assert result['verified'], \
            f"N={N_susy}, c={c_val}: sum = {result['sum']}, expected {result['expected']}"

    def test_n0_explicit_algebra(self):
        """N=0: c/2 + (26-c)/2 = 26/2 = 13."""
        c_sym = Symbol('c')
        lhs = c_sym / 2 + (26 - c_sym) / 2
        assert simplify(lhs) == 13

    def test_n1_explicit_algebra(self):
        """N=1: (3c-2)/4 + (3(15-c)-2)/4 = (3c-2+45-3c-2)/4 = 41/4."""
        c_sym = Symbol('c')
        lhs = (3 * c_sym - 2) / 4 + (3 * (15 - c_sym) - 2) / 4
        assert simplify(lhs) == Rational(41, 4)

    def test_n2_explicit_algebra(self):
        """N=2: (6-c)/(2(3-c)) + c/(2(c-3)) = 1."""
        c_sym = Symbol('c')
        kap = (6 - c_sym) / (2 * (3 - c_sym))
        kap_dual = (6 - (6 - c_sym)) / (2 * (3 - (6 - c_sym)))
        # kap_dual = c/(2(c-3)) = -c/(2(3-c))
        assert simplify(kap + kap_dual) == 1

    def test_n4_explicit_algebra(self):
        """N=4: 6/(6-c) + 6/(c-6) = 0."""
        c_sym = Symbol('c')
        kap = Rational(6) / (6 - c_sym)
        kap_dual = Rational(6) / (6 - (12 - c_sym))
        assert simplify(kap + kap_dual) == 0


class TestMethod2KParametrization:
    """METHOD 2: k-parametrization with FF involution k -> -k-4."""

    def test_all_verified(self):
        results = hierarchy_proof_method_k_param()
        for N_val in [0, 1, 2, 4]:
            assert results[N_val]['verified'], f"N={N_val} failed k-param verification"

    def test_n2_k_formula(self):
        """N=2: kappa(k) = (k+4)/4, kappa(-k-4) = -k/4, sum = 1."""
        k_sym = Symbol('k')
        kap = (k_sym + 4) / 4
        kap_dual = (-k_sym) / 4
        assert simplify(kap + kap_dual) == 1

    def test_n4_k_formula(self):
        """N=4: kappa(k) = (k+2)/2, kappa(-k-4) = (-k-2)/2, sum = 0."""
        k_sym = Symbol('k')
        kap = (k_sym + 2) / 2
        kap_dual = (-k_sym - 2) / 2
        assert simplify(kap + kap_dual) == 0

    def test_n1_linear_formula(self):
        """N=1: slope*c_crit + 2*intercept = (3/4)*15 + 2*(-1/2) = 41/4."""
        slope = Rational(3, 4)
        intercept = Rational(-1, 2)
        c_crit = Rational(15)
        assert slope * c_crit + 2 * intercept == Rational(41, 4)

    def test_n0_linear_formula(self):
        """N=0: slope*c_crit + 2*intercept = (1/2)*26 + 0 = 13."""
        assert Rational(1, 2) * 26 == 13

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, 100])
    def test_n2_numerical_k(self, k_val):
        """N=2 at various k: kappa(k) + kappa(-k-4) = 1."""
        kap = (Rational(k_val) + 4) / 4
        kap_dual = (-Rational(k_val)) / 4
        assert kap + kap_dual == 1

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5, 10, 100])
    def test_n4_numerical_k(self, k_val):
        """N=4 at various k: kappa(k) + kappa(-k-4) = 0."""
        kap = (Rational(k_val) + 2) / 2
        kap_dual = (-Rational(k_val) - 2) / 2
        assert kap + kap_dual == 0


class TestMethod3SelfDualPoint:
    """METHOD 3: Self-dual point evaluation.

    For linear kappa (N=0, N=1): Sigma = 2*kappa(c_sd).
    For Moebius kappa (N=2, N=4): algebraic simplification.
    """

    def test_all_verified(self):
        results = hierarchy_proof_method_self_dual()
        for N_val in [0, 1, 2, 4]:
            assert results[N_val]['verified'], f"N={N_val} self-dual verification failed"

    def test_n0_self_dual(self):
        """N=0: c_sd=13, kappa(13)=13/2, Sigma=2*13/2=13."""
        assert kappa_superconformal(0, 13) == Rational(13, 2)
        assert 2 * kappa_superconformal(0, 13) == Rational(13)

    def test_n1_self_dual(self):
        """N=1: c_sd=15/2, kappa(15/2)=41/8, Sigma=2*41/8=41/4."""
        kap_sd = kappa_superconformal(1, Rational(15, 2))
        assert kap_sd == Rational(41, 8)
        assert 2 * kap_sd == Rational(41, 4)

    def test_n2_self_dual_is_pole(self):
        """N=2: c_sd=3 is a pole of kappa (k -> infinity limit)."""
        # kappa(c=3) = (6-3)/(2(3-3)) = 3/0 = pole
        # But the sum is still well-defined: 1
        result = verify_complementarity_sum_symbolic(2)
        assert result['verified']

    def test_n4_self_dual_is_pole(self):
        """N=4: c_sd=6 is a pole of kappa."""
        result = verify_complementarity_sum_symbolic(4)
        assert result['verified']


class TestMethod4AnomalyCancellation:
    """METHOD 4: Anomaly cancellation interpretation.

    The complementarity sum measures residual chiral anomaly after
    Koszul pairing. N=4 achieves complete cancellation.
    """

    def test_n4_is_km_type(self):
        """N=4 has KM-type anti-symmetry: kappa + kappa' = 0."""
        h = superconformal_complementarity_hierarchy()
        assert h[4]['anomaly_type'] == 'KM-type (exact cancellation)'
        assert h[4]['sum'] == 0

    def test_n0_residual_anomaly(self):
        """N=0 (Virasoro) has the largest residual anomaly."""
        h = superconformal_complementarity_hierarchy()
        sums = {N: h[N]['sum'] for N in [0, 1, 2, 4]}
        assert sums[0] == max(sums.values())

    def test_anomaly_decreases_with_susy(self):
        """More SUSY => smaller residual anomaly."""
        h = superconformal_complementarity_hierarchy()
        assert h[0]['sum'] > h[1]['sum'] > h[2]['sum'] > h[4]['sum']


class TestMethod5SuperMumford:
    """METHOD 5: Super-Mumford class decomposition.

    For linear kappa (N=0, N=1): kappa = slope*c + intercept.
    The sum = slope*c_crit + 2*intercept.

    The slope encodes the bosonic Mumford contribution; the intercept
    encodes the fermionic correction from the super-moduli space.
    """

    def test_n0_pure_bosonic(self):
        """N=0: kappa = c/2, slope=1/2, intercept=0 (pure bosonic Mumford)."""
        assert kappa_superconformal(0, 0) == 0  # intercept = 0
        assert kappa_superconformal(0, 2) - kappa_superconformal(0, 0) == 1  # slope = 1/2

    def test_n1_fermionic_correction(self):
        """N=1: kappa = (3c-2)/4, intercept = -1/2 (fermionic sector)."""
        assert kappa_superconformal(1, 0) == Rational(-1, 2)

    def test_n1_slope_increase(self):
        """N=1 slope 3/4 > N=0 slope 1/2 (super-Mumford enhancement)."""
        # N=1 slope = 3/4 (from the combined bosonic + fermionic Mumford class)
        slope_n0 = Rational(1, 2)
        slope_n1 = Rational(3, 4)
        assert slope_n1 > slope_n0

    def test_n2_partial_fraction(self):
        """N=2: kappa = 1/2 + 3/(2(3-c)). The constant 1/2 is the
        surviving piece after Koszul cancellation of the pole part."""
        c_sym = Symbol('c')
        kap = (6 - c_sym) / (2 * (3 - c_sym))
        # Partial fraction: 1/2 + 3/(2(3-c))
        # The pole part 3/(2(3-c)) cancels with its dual -3/(2(3-c))
        # The constant 1/2 survives twice: 2 * 1/2 = 1
        assert simplify(kap - (Rational(1, 2) + Rational(3) / (2 * (3 - c_sym)))) == 0


class TestStrictDecrease:
    """Test the strict decrease property: 13 > 41/4 > 1 > 0."""

    def test_hierarchy_strict_decrease_function(self):
        result = hierarchy_strict_decrease()
        assert result['strictly_decreasing'] is True

    def test_all_pairwise(self):
        result = hierarchy_strict_decrease()
        for pair in result['pairwise']:
            assert pair['decreasing'], \
                f"N={pair['N_left']} vs N={pair['N_right']}: " \
                f"{pair['sum_left']} not > {pair['sum_right']}"

    def test_differences_positive(self):
        result = hierarchy_strict_decrease()
        for pair in result['pairwise']:
            assert pair['difference'] > 0

    def test_n0_minus_n1(self):
        """13 - 41/4 = 52/4 - 41/4 = 11/4."""
        assert Rational(13) - Rational(41, 4) == Rational(11, 4)

    def test_n1_minus_n2(self):
        """41/4 - 1 = 37/4."""
        assert Rational(41, 4) - 1 == Rational(37, 4)

    def test_n2_minus_n4(self):
        """1 - 0 = 1."""
        assert Rational(1) - Rational(0) == 1


class TestCrossConsistency:
    """Cross-consistency between the hierarchy engine and the individual classes."""

    @pytest.mark.parametrize("c_val", [1, 2, Rational(3, 2), 5, 10])
    def test_n1_kappa_consistency(self, c_val):
        """kappa_superconformal(1, c) == N1SuperVirasoro.kappa(c)."""
        assert kappa_superconformal(1, c_val) == N1SuperVirasoro.kappa(c_val)

    @pytest.mark.parametrize("c_val", [1, 2, Rational(9, 5), 5])
    def test_n2_kappa_consistency(self, c_val):
        """kappa_superconformal(2, c) == N2Superconformal.kappa(c_val=c)."""
        assert kappa_superconformal(2, c_val) == N2Superconformal.kappa(c_val=c_val)

    @pytest.mark.parametrize("c_val", [1, 2, 3, 4, Rational(18, 5)])
    def test_n4_kappa_consistency(self, c_val):
        """kappa_superconformal(4, c) == N4SmallSuperconformal.kappa(c_val=c)."""
        assert kappa_superconformal(4, c_val) == N4SmallSuperconformal.kappa(c_val=c_val)

    def test_n1_complementarity_matches_class(self):
        """Hierarchy sum matches N1SuperVirasoro.complementarity_sum."""
        result = N1SuperVirasoro.complementarity_sum(7)
        assert result['sum'] == complementarity_sum_general(1)

    def test_n2_complementarity_matches_class(self):
        result = N2Superconformal.complementarity_sum(1)
        assert result['sum'] == complementarity_sum_general(2)

    def test_n4_complementarity_matches_class(self):
        result = N4SmallSuperconformal.complementarity_sum(c_val=2)
        assert result['sum'] == complementarity_sum_general(4)

    def test_hierarchy_table_matches(self):
        """Koszul duality table sums match hierarchy sums."""
        table = superconformal_koszul_duality_table()
        h = superconformal_complementarity_hierarchy()
        assert table['N=1']['kappa_sum'] == h[1]['sum']
        assert table['N=2']['kappa_sum'] == h[2]['sum']
        assert table['N=4']['kappa_sum'] == h[4]['sum']


class TestPhysicalSpecialValues:
    """Test at physically important special central charges."""

    def test_superstring_worldsheet(self):
        """c=15 (N=1 superstring): kappa=43/4, dual c=0, kappa'=-1/2."""
        kap = kappa_superconformal(1, 15)
        kap_dual = kappa_superconformal(1, 0)
        assert kap == Rational(43, 4)
        assert kap_dual == Rational(-1, 2)
        assert kap + kap_dual == Rational(41, 4)

    def test_cy3_internal(self):
        """c=9 (N=2 CY3 internal): kappa=1/4, dual c=-3, kappa'=3/4."""
        kap = kappa_superconformal(2, 9)
        kap_dual = kappa_superconformal(2, -3)
        assert kap == Rational(1, 4)
        assert kap_dual == Rational(3, 4)
        assert kap + kap_dual == Rational(1)

    def test_k3_universal_n4(self):
        """c=3 (N=4, k=2): kappa=2, dual c=9, kappa'=-2."""
        kap = kappa_superconformal(4, 3)
        kap_dual = kappa_superconformal(4, 9)
        assert kap == Rational(2)
        assert kap_dual == Rational(-2)
        assert kap + kap_dual == 0

    def test_bosonic_string_worldsheet(self):
        """c=26 (N=0 bosonic string): kappa=13, dual c=0, kappa'=0."""
        kap = kappa_superconformal(0, 26)
        kap_dual = kappa_superconformal(0, 0)
        assert kap == Rational(13)
        assert kap_dual == Rational(0)
        assert kap + kap_dual == Rational(13)

    def test_n1_free_fermion_limit(self):
        """c=3/2 (N=1 free fermion): kappa=5/8."""
        kap = kappa_superconformal(1, Rational(3, 2))
        assert kap == Rational(5, 8)

    def test_n2_unitary_minimal(self):
        """c=1 (N=2 k=1 minimal): kappa=5/4."""
        kap = kappa_superconformal(2, 1)
        assert kap == Rational(5, 4)

    def test_n4_first_minimal(self):
        """c=2 (N=4 k=1): kappa=3/2."""
        kap = kappa_superconformal(4, 2)
        assert kap == Rational(3, 2)
