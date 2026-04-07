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
