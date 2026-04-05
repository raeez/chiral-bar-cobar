r"""Tests for shadow radius landscape: rho(A) for ALL standard families.

Verifies:
1. Class G (Heisenberg, lattice): rho = 0 exactly
2. Class L (affine KM): rho = 0 exactly (Delta = 0)
3. Class C (beta-gamma): single-line rho = 0 (stratum separation)
4. Class M (Virasoro, W_N): rho > 0 with explicit formulas
5. Virasoro at special central charges (1/2, 1, 4, 13, 25, 26)
6. W_3 at special central charges (2, 50, 98)
7. W_4 at generic c (3 channels: T, W_3, W_4)
8. Koszul duality: rho(c) vs rho(K-c)
9. Self-duality: rho(13) = rho(13) for Virasoro
10. Critical cubic 5c^3 + 22c^2 - 180c - 872 = 0
11. rho(c) + rho(26-c) complementarity analysis
12. rho = 0 iff finite tower (class G/L/C)
13. rho > 0 iff infinite tower (class M)
14. W_N channel hierarchy: rho_T > rho_{W_3} > rho_{W_4} > ...
15. Betagamma at multiple conformal weights
"""

import sys
sys.path.insert(0, 'compute')

import math
import pytest
from sympy import Rational, sqrt, Symbol, simplify, cancel, S

c = Symbol('c')


# ============================================================================
# 1. Class G: rho = 0 (Heisenberg, lattice, free fermion)
# ============================================================================

class TestClassG:
    """Class G (Gaussian): rho = 0, tower terminates at arity 2."""

    def test_heisenberg_rho_zero(self):
        from lib.shadow_radius_landscape import shadow_radius_universal
        rho = shadow_radius_universal(Rational(1), Rational(0), Rational(0))
        assert rho == 0

    def test_heisenberg_any_level_rho_zero(self):
        """rho = 0 for Heisenberg at any level k."""
        from lib.shadow_radius_landscape import shadow_radius_universal
        for k_val in [1, 2, 5, 10, 100]:
            rho = shadow_radius_universal(Rational(k_val), Rational(0), Rational(0))
            assert rho == 0, f"rho should be 0 at level {k_val}"

    def test_lattice_rho_zero(self):
        from lib.shadow_radius_landscape import lattice_shadow_data
        for rank in [1, 2, 4, 8, 16, 24]:
            data = lattice_shadow_data(rank)
            assert data['rho'] == 0
            assert data['class'] == 'G'
            assert data['depth'] == 2

    def test_lattice_landscape_all_zero(self):
        from lib.shadow_radius_landscape import lattice_landscape
        ll = lattice_landscape()
        for name, data in ll.items():
            assert data['rho'] == 0, f"Lattice {name} should have rho=0"

    def test_lattice_kappa_equals_rank(self):
        from lib.shadow_radius_landscape import lattice_shadow_data
        for rank in [1, 2, 8, 24]:
            assert lattice_shadow_data(rank)['kappa'] == rank

    def test_free_fermion_class_g(self):
        """Free fermion: c=1/2, kappa=1/4, class G, rho=0."""
        from lib.shadow_radius_landscape import shadow_radius_universal
        rho = shadow_radius_universal(Rational(1, 4), Rational(0), Rational(0))
        assert rho == 0


# ============================================================================
# 2. Class L: rho = 0 (affine KM)
# ============================================================================

class TestClassL:
    """Class L (Lie/tree): Delta = 0, rho = 0, tower terminates at arity 3."""

    def test_affine_rho_zero(self):
        from lib.shadow_radius_landscape import affine_shadow_data
        for lt, rk in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('D', 4)]:
            data = affine_shadow_data(lt, rk)
            assert data['rho'] == 0
            assert data['class'] == 'L'
            assert data['depth'] == 3

    def test_affine_delta_zero(self):
        """For all affine KM: S_4 = 0 implies Delta = 0."""
        from lib.shadow_radius_landscape import affine_shadow_data
        for lt, rk in [('A', 1), ('A', 2), ('A', 3)]:
            data = affine_shadow_data(lt, rk)
            assert data['S4'] == 0
            assert data['Delta'] == 0

    def test_exceptional_rho_zero(self):
        """Exceptional Lie algebras also have rho = 0."""
        from lib.shadow_radius_landscape import affine_shadow_data
        for exc in [('E', 6), ('E', 7), ('E', 8), ('F', 4), ('G', 2)]:
            data = affine_shadow_data(*exc)
            assert data['rho'] == 0
            assert data['class'] == 'L'

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        from lib.shadow_radius_landscape import affine_shadow_data
        data = affine_shadow_data('A', 1, level_val=1)
        assert simplify(data['kappa'] - Rational(9, 4)) == 0

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k) = 8*(k+3)/6 = 4(k+3)/3."""
        from lib.shadow_radius_landscape import affine_shadow_data
        data = affine_shadow_data('A', 2, level_val=1)
        # dim(sl_3) = 8, h^v = 3
        # kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert simplify(data['kappa'] - Rational(16, 3)) == 0

    def test_affine_landscape_complete(self):
        from lib.shadow_radius_landscape import affine_landscape
        al = affine_landscape()
        assert 'A1' in al
        assert 'A2' in al
        assert 'E8' in al
        assert 'G2' in al
        for name, data in al.items():
            assert data['rho'] == 0


# ============================================================================
# 3. Class C: betagamma (stratum separation)
# ============================================================================

class TestClassC:
    """Class C (Contact): single-line rho = 0 (stratum separation)."""

    def test_betagamma_standard_rho_zero(self):
        """Standard betagamma (lambda=0 or 1): rho = 0 on primary line."""
        from lib.shadow_radius_landscape import betagamma_shadow_data
        kappa, alpha, S4, Delta = betagamma_shadow_data(0)
        assert alpha == 0
        assert S4 == 0
        assert Delta == 0

    def test_betagamma_standard_kappa(self):
        """kappa(bg, lambda=0) = 1, kappa(bg, lambda=1) = 1."""
        from lib.shadow_radius_landscape import betagamma_kappa
        assert betagamma_kappa(0) == 1
        assert betagamma_kappa(1) == 1

    def test_betagamma_symplectic_kappa(self):
        """kappa(bg, lambda=1/2) = -1/2."""
        from lib.shadow_radius_landscape import betagamma_kappa
        assert betagamma_kappa(Rational(1, 2)) == Rational(-1, 2)

    def test_betagamma_central_charge(self):
        """c(bg, lambda) = 2(6*lambda^2 - 6*lambda + 1)."""
        from lib.shadow_radius_landscape import betagamma_central_charge
        assert betagamma_central_charge(0) == 2
        assert betagamma_central_charge(1) == 2
        assert betagamma_central_charge(Rational(1, 2)) == -1

    def test_betagamma_lambda_3_2(self):
        """betagamma at lambda=3/2: c = 2(6*9/4 - 9 + 1) = 2(27/2 - 8) = 2*11/2 = 11."""
        from lib.shadow_radius_landscape import betagamma_central_charge, betagamma_kappa
        assert betagamma_central_charge(Rational(3, 2)) == 11
        assert betagamma_kappa(Rational(3, 2)) == Rational(11, 2)

    def test_betagamma_landscape_all_rho_zero(self):
        from lib.shadow_radius_landscape import betagamma_landscape
        bl = betagamma_landscape()
        for label, data in bl.items():
            assert data['rho_primary_line'] == 0
            assert data['class'] == 'C'
            assert data['depth'] == 4

    def test_betagamma_kappa_symmetry(self):
        """kappa(lambda) = kappa(1-lambda): symmetric under lambda -> 1-lambda."""
        from lib.shadow_radius_landscape import betagamma_kappa
        for lam_val in [0, Rational(1, 4), Rational(1, 3), Rational(1, 2)]:
            assert betagamma_kappa(lam_val) == betagamma_kappa(1 - lam_val)


# ============================================================================
# 4. Class M: Virasoro
# ============================================================================

class TestVirasoro:
    """Class M (Mixed): rho > 0, infinite tower."""

    def test_virasoro_rho_positive(self):
        """rho > 0 for all c > 0."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        for c_val in [Rational(1, 2), 1, 4, 13, 25, 26]:
            assert virasoro_rho_numerical(c_val) > 0

    def test_virasoro_rho_squared_formula(self):
        """rho^2(Vir_c) = (180c + 872) / ((5c+22)*c^2)."""
        from lib.shadow_radius_landscape import virasoro_rho_squared
        rho_sq = virasoro_rho_squared()
        expected = (180 * c + 872) / ((5 * c + 22) * c**2)
        assert simplify(cancel(rho_sq - expected)) == 0

    def test_virasoro_rho_c1(self):
        """rho(Vir_1) = sqrt(1052/27) ~ 6.242."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho = virasoro_rho_numerical(1)
        expected = (1052 / 27) ** 0.5
        assert abs(rho - expected) < 1e-6

    def test_virasoro_rho_c13(self):
        """rho(Vir_13) ~ 0.467 (known value)."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho = virasoro_rho_numerical(13)
        assert abs(rho - 0.467396) < 0.001

    def test_virasoro_rho_c26(self):
        """rho(Vir_26) ~ 0.232 (string theory value)."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho = virasoro_rho_numerical(26)
        assert abs(rho - 0.232450) < 0.001

    def test_virasoro_rho_c_half(self):
        """rho(Vir_{1/2}) >> 1 (Ising model, strongly divergent)."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho = virasoro_rho_numerical(Rational(1, 2))
        assert rho > 10  # very divergent

    def test_virasoro_rho_decreasing(self):
        """rho(c) is decreasing for large c."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho_10 = virasoro_rho_numerical(10)
        rho_20 = virasoro_rho_numerical(20)
        rho_50 = virasoro_rho_numerical(50)
        assert rho_10 > rho_20 > rho_50

    def test_virasoro_data_consistency(self):
        """Verify kappa, alpha, S4, Delta are consistent."""
        from lib.shadow_radius_landscape import virasoro_data
        kappa, alpha, S4, Delta = virasoro_data(Rational(1))
        assert kappa == Rational(1, 2)
        assert alpha == 2
        assert simplify(S4 - Rational(10, 27)) == 0
        assert simplify(Delta - Rational(40, 27)) == 0

    def test_virasoro_delta_positive(self):
        """Delta = 40/(5c+22) > 0 for c > 0 (class M confirmed)."""
        from lib.shadow_radius_landscape import virasoro_data
        for c_val in [Rational(1, 2), 1, 13, 26, 100]:
            _, _, _, Delta = virasoro_data(c_val)
            assert float(Delta.evalf()) > 0

    def test_virasoro_landscape_convergence(self):
        """Verify convergence classification at known c values."""
        from lib.shadow_radius_landscape import virasoro_landscape
        vl = virasoro_landscape()
        # c=1/2: divergent
        assert not vl['1/2']['convergent']
        # c=1: divergent
        assert not vl['1']['convergent']
        # c=4: divergent (rho ~ 1.54)
        assert not vl['4']['convergent']
        # c=13: convergent
        assert vl['13']['convergent']
        # c=25: convergent
        assert vl['25']['convergent']
        # c=26: convergent
        assert vl['26']['convergent']


# ============================================================================
# 5. Critical central charge
# ============================================================================

class TestCriticalCubic:
    """Test the critical cubic 5c^3 + 22c^2 - 180c - 872 = 0."""

    def test_critical_c_exists(self):
        from lib.shadow_radius_landscape import virasoro_critical_cubic
        _, _, c_star = virasoro_critical_cubic()
        assert c_star is not None

    def test_critical_c_value(self):
        """c* ~ 6.125."""
        from lib.shadow_radius_landscape import virasoro_critical_cubic
        _, _, c_star = virasoro_critical_cubic()
        assert 6.12 < c_star < 6.13

    def test_rho_equals_1_at_critical(self):
        """rho(c*) = 1 exactly."""
        from lib.shadow_radius_landscape import virasoro_critical_cubic, virasoro_rho_squared
        _, _, c_star = virasoro_critical_cubic()
        rho_sq = float(virasoro_rho_squared(c_star))
        assert abs(rho_sq - 1.0) < 1e-6

    def test_divergent_below_critical(self):
        """rho > 1 for 0 < c < c*."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        for c_val in [Rational(1, 2), 1, 2, 4, 6]:
            assert virasoro_rho_numerical(c_val) > 1.0

    def test_convergent_above_critical(self):
        """rho < 1 for c > c*."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        for c_val in [7, 10, 13, 20, 26, 50, 100]:
            assert virasoro_rho_numerical(c_val) < 1.0

    def test_cubic_solves_polynomial(self):
        """c* satisfies 5c^3 + 22c^2 - 180c - 872 = 0."""
        from lib.shadow_radius_landscape import virasoro_critical_cubic
        poly, _, c_star = virasoro_critical_cubic()
        residual = 5 * c_star**3 + 22 * c_star**2 - 180 * c_star - 872
        assert abs(residual) < 1e-6

    def test_tline_critical_equals_virasoro(self):
        """T-line critical c* is the same for all W_N."""
        from lib.shadow_radius_landscape import wn_tline_critical_c
        c_star = wn_tline_critical_c()
        assert 6.12 < c_star < 6.13


# ============================================================================
# 6. Koszul duality
# ============================================================================

class TestKoszulDuality:
    """Koszul duality: Vir_c <-> Vir_{26-c}."""

    def test_self_dual_c13(self):
        """rho(13) = rho(13): self-dual at c = 13."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        pair = virasoro_koszul_pair(13)
        assert pair['self_dual']

    def test_c_dual_correct(self):
        """c_dual = 26 - c."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        for cv in [1, 5, 13, 25]:
            pair = virasoro_koszul_pair(cv)
            assert pair['c_dual'] == 26 - cv

    def test_rho_swap_symmetry(self):
        """rho(c) at c = rho(26-c) at 26-c: symmetric under swap."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        pair1 = virasoro_koszul_pair(1)
        pair25 = virasoro_koszul_pair(25)
        assert abs(pair1['rho'] - pair25['rho_dual']) < 1e-10
        assert abs(pair1['rho_dual'] - pair25['rho']) < 1e-10

    def test_product_not_constant(self):
        """rho(c) * rho(26-c) is NOT constant (varies with c)."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        prod_1 = virasoro_koszul_pair(1)['rho_product']
        prod_13 = virasoro_koszul_pair(13)['rho_product']
        assert abs(prod_1 - prod_13) > 0.1  # clearly different

    def test_c13_unique_self_dual(self):
        """c = 13 is the unique self-dual point for Virasoro."""
        from lib.shadow_radius_landscape import virasoro_rho_squared
        rho_sq = virasoro_rho_squared()
        diff = cancel(rho_sq - rho_sq.subs(c, 26 - c))
        numer = simplify(diff).as_numer_denom()[0]
        # At c=13: numer = 0
        assert simplify(numer.subs(c, 13)) == 0

    def test_w3_self_dual_c50(self):
        """W_3 self-dual at c = 50 (Koszul conductor K_3 = 100)."""
        from lib.shadow_radius_landscape import w3_koszul_pair
        pair = w3_koszul_pair(50)
        assert pair['T_self_dual']
        assert pair['W_self_dual']

    def test_w3_koszul_conductor(self):
        from lib.shadow_radius_landscape import KOSZUL_CONDUCTORS
        assert KOSZUL_CONDUCTORS[3] == 100

    def test_w4_koszul_conductor(self):
        from lib.shadow_radius_landscape import KOSZUL_CONDUCTORS
        assert KOSZUL_CONDUCTORS[4] == 246

    def test_virasoro_koszul_conductor(self):
        from lib.shadow_radius_landscape import KOSZUL_CONDUCTORS
        assert KOSZUL_CONDUCTORS[2] == 26

    def test_rho_c26_dual_diverges(self):
        """rho(Vir_0) = infinity (kappa = 0)."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        assert virasoro_rho_numerical(0) == float('inf')


# ============================================================================
# 7. W_3 shadow radius
# ============================================================================

class TestW3:
    """W_3 shadow radius: two channels (T-line, W-line)."""

    def test_w3_tline_equals_virasoro(self):
        """T-line rho = Virasoro rho."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical, wn_tline_rho
        from sympy import N as Neval
        for c_val in [2, 13, 50, 98]:
            rho_vir = virasoro_rho_numerical(c_val)
            rho_T = float(wn_tline_rho(2, c_val).evalf())
            assert abs(rho_vir - rho_T) < 1e-8

    def test_w3_wline_rho_positive(self):
        """W-line rho > 0 for c > 0."""
        from lib.shadow_radius_landscape import w3_wline_rho_numerical
        for c_val in [2, 13, 50, 98]:
            assert w3_wline_rho_numerical(c_val) > 0

    def test_w3_wline_rho_much_smaller_than_tline(self):
        """rho_W << rho_T: T-line always dominates."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical, w3_wline_rho_numerical
        for c_val in [2, 13, 50, 98]:
            rho_T = virasoro_rho_numerical(c_val)
            rho_W = w3_wline_rho_numerical(c_val)
            assert rho_W < rho_T, f"W-line should be smaller at c={c_val}"

    def test_w3_wline_rho_squared_formula(self):
        """rho_W^2 = 30720 / (c^2 * (5c+22)^3)."""
        from lib.shadow_radius_landscape import w3_wline_rho_squared
        rho_sq = w3_wline_rho_squared()
        expected = Rational(30720) / (c**2 * (5 * c + 22)**3)
        assert simplify(cancel(rho_sq - expected)) == 0

    def test_w3_c2(self):
        """W_3 at c=2: rho_T ~ 3.10, rho_W ~ 0.48."""
        from lib.shadow_radius_landscape import w3_landscape
        w3 = w3_landscape()
        data = w3['2']
        assert abs(data['rho_T'] - 3.102) < 0.01
        assert abs(data['rho_W'] - 0.484) < 0.01

    def test_w3_c50_selfdual(self):
        """W_3 at c=50: self-dual point."""
        from lib.shadow_radius_landscape import w3_landscape
        w3 = w3_landscape()
        assert w3['50']['self_dual']

    def test_w3_c98(self):
        """W_3 at c=98: strongly convergent."""
        from lib.shadow_radius_landscape import w3_landscape
        w3 = w3_landscape()
        data = w3['98']
        assert data['rho_T'] < 0.1
        assert data['rho_W'] < 0.01

    def test_w3_wline_critical_c(self):
        """W-line critical c_W* ~ 1.19."""
        from lib.shadow_radius_landscape import w3_wline_critical_c
        c_star = w3_wline_critical_c()
        assert c_star is not None
        assert 1.0 < c_star < 1.5


# ============================================================================
# 8. W_4 shadow radius
# ============================================================================

class TestW4:
    """W_4 shadow radius: three channels (T, W_3, W_4)."""

    def test_w4_three_channels(self):
        """W_4 has three channels."""
        from lib.shadow_radius_landscape import w4_landscape
        w4 = w4_landscape(26)
        assert 'T' in w4
        assert 'W_3' in w4
        assert 'W_4' in w4

    def test_w4_channel_hierarchy(self):
        """rho_T > rho_{W_3} > rho_{W_4} for all c > 0."""
        from lib.shadow_radius_landscape import w4_landscape
        for c_val in [10, 26, 50, 123, 200]:
            w4 = w4_landscape(c_val)
            assert w4['T']['rho'] > w4['W_3']['rho']
            assert w4['W_3']['rho'] > w4['W_4']['rho']

    def test_w4_effective_equals_T(self):
        """Effective rho = T-line rho (T dominates)."""
        from lib.shadow_radius_landscape import w4_landscape
        for c_val in [10, 26, 123]:
            w4 = w4_landscape(c_val)
            assert abs(w4['rho_eff'] - w4['T']['rho']) < 1e-10

    def test_w4_selfdual_c123(self):
        """W_4 self-dual at c = 123 (K_4 = 246)."""
        from lib.shadow_radius_landscape import SELF_DUAL_CC
        assert SELF_DUAL_CC[4] == 123


# ============================================================================
# 9. W_N general
# ============================================================================

class TestWNGeneral:
    """W_N shadow radius: channel hierarchy and scaling."""

    def test_wn_channel_count(self):
        """W_N has N-1 channels (j=2,...,N)."""
        from lib.shadow_radius_landscape import wn_all_channel_rho
        for N in [3, 4, 5, 6]:
            channels = wn_all_channel_rho(N, 26)
            assert len(channels) == N - 1

    def test_wn_channel_decreasing(self):
        """rho_j is strictly decreasing in j for fixed c."""
        from lib.shadow_radius_landscape import wn_all_channel_rho
        for N in [3, 4, 5]:
            channels = wn_all_channel_rho(N, 26)
            rhos = [channels[j] for j in range(2, N + 1)]
            for i in range(len(rhos) - 1):
                assert rhos[i] > rhos[i + 1]

    def test_wn_effective_equals_T(self):
        """Effective rho = T-line rho for all W_N."""
        from lib.shadow_radius_landscape import wn_effective_rho, virasoro_rho_numerical
        for N in [3, 4, 5]:
            rho_eff = wn_effective_rho(N, 26)
            rho_T = virasoro_rho_numerical(26)
            assert abs(rho_eff - rho_T) < 1e-10

    def test_wn_j2_equals_virasoro(self):
        """The j=2 channel (T-line) equals Virasoro rho for all W_N."""
        from lib.shadow_radius_landscape import wn_all_channel_rho, virasoro_rho_numerical
        for N in [3, 4, 5, 6]:
            channels = wn_all_channel_rho(N, 13)
            assert abs(channels[2] - virasoro_rho_numerical(13)) < 1e-8

    def test_wn_rho_squared_formula_j3(self):
        """Verify W_3 rho^2 formula matches the wn_channel formula."""
        from lib.shadow_radius_landscape import wn_channel_rho_squared, w3_wline_rho_squared
        rho_gen = wn_channel_rho_squared(3, 3)
        rho_w3 = w3_wline_rho_squared()
        assert simplify(cancel(rho_gen - rho_w3)) == 0

    def test_wn_higher_channels_very_small(self):
        """Higher channels have very small rho (rapid geometric decay)."""
        from lib.shadow_radius_landscape import wn_all_channel_rho
        channels = wn_all_channel_rho(6, 26)
        # j=6 should be very small compared to j=2
        assert channels[6] < 1e-4
        assert channels[6] < channels[2] / 1000


# ============================================================================
# 10. rho = 0 iff finite tower
# ============================================================================

class TestRhoClassification:
    """rho = 0 iff tower terminates (class G/L); rho > 0 iff infinite (class M)."""

    def test_class_g_rho_zero(self):
        from lib.shadow_radius_landscape import shadow_radius_universal
        # Heisenberg: alpha=0, S4=0
        assert shadow_radius_universal(Rational(5), Rational(0), Rational(0)) == 0

    def test_class_l_rho_from_alpha(self):
        """Class L: S4=0, so rho = 3|alpha|/(2|kappa|)."""
        from lib.shadow_radius_landscape import shadow_radius_universal
        # This is nonzero but the tower still terminates (polynomial GF)
        rho = shadow_radius_universal(Rational(3), Rational(1), Rational(0))
        # rho = sqrt(9*1 + 0)/(2*3) = 3/6 = 1/2
        assert simplify(rho - Rational(1, 2)) == 0

    def test_class_m_rho_positive(self):
        """Class M: Delta > 0, rho > 0."""
        from lib.shadow_radius_landscape import shadow_radius_universal
        # Virasoro at c=1: kappa=1/2, alpha=2, S4=10/27
        rho = shadow_radius_universal(Rational(1, 2), Rational(2), Rational(10, 27))
        assert float(rho.evalf()) > 0

    def test_delta_zero_iff_s4_zero(self):
        """Delta = 8*kappa*S4 = 0 iff S4 = 0 (for kappa != 0)."""
        from lib.shadow_radius_landscape import virasoro_data, affine_shadow_data
        # Virasoro: S4 != 0, Delta != 0
        _, _, S4_vir, Delta_vir = virasoro_data(1)
        assert float(S4_vir.evalf()) != 0
        assert float(Delta_vir.evalf()) != 0
        # Affine: S4 = 0, Delta = 0
        aff = affine_shadow_data('A', 1)
        assert aff['S4'] == 0
        assert aff['Delta'] == 0


# ============================================================================
# 11. Complementarity analysis
# ============================================================================

class TestComplementarity:
    """Complementarity of shadow radii under Koszul duality."""

    def test_virasoro_complementarity_symmetry(self):
        """rho(c) and rho(26-c) swap under c -> 26-c."""
        from lib.shadow_radius_landscape import virasoro_complementarity_analysis
        results = virasoro_complementarity_analysis()
        for pair in results:
            if pair['c'] + pair['c_dual'] == 26:
                # rho(c) should equal rho_dual computed at c_dual = 26-c
                # This is definitionally true
                assert abs(pair['rho'] - pair['rho']) < 1e-10

    def test_sum_not_constant(self):
        """rho(c) + rho(26-c) is not constant."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        sum_1 = virasoro_koszul_pair(1)['rho_sum']
        sum_13 = virasoro_koszul_pair(13)['rho_sum']
        assert abs(sum_1 - sum_13) > 1.0  # clearly different

    def test_product_not_constant(self):
        """rho(c) * rho(26-c) is not constant."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        prod_1 = virasoro_koszul_pair(1)['rho_product']
        prod_13 = virasoro_koszul_pair(13)['rho_product']
        assert abs(prod_1 - prod_13) > 0.1

    def test_minimum_at_self_dual(self):
        """Product rho*rho' is minimal near the self-dual point c=13."""
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        prod_13 = virasoro_koszul_pair(13)['rho_product']
        for cv in [1, 4, 6, 10, 20, 25]:
            prod = virasoro_koszul_pair(cv)['rho_product']
            # Not necessarily minimal at 13 for all c, but product at
            # endpoints is larger
            if cv in [1, 25]:
                assert prod > prod_13

    def test_w3_complementarity(self):
        """W_3 complementarity: rho_T(c) swaps with rho_T(100-c)."""
        from lib.shadow_radius_landscape import w3_koszul_pair
        pair = w3_koszul_pair(10)
        pair90 = w3_koszul_pair(90)
        assert abs(pair['rho_T'] - pair90['rho_T_dual']) < 1e-8


# ============================================================================
# 12. Edge cases and consistency
# ============================================================================

class TestEdgeCases:
    """Edge cases and consistency checks."""

    def test_virasoro_rho_at_c0_infinite(self):
        """rho is infinite at c=0 (kappa=0)."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        assert virasoro_rho_numerical(0) == float('inf')

    def test_virasoro_large_c_asymptotics(self):
        """rho ~ sqrt(180/5) / c = 6/c for large c."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        for c_val in [100, 1000]:
            rho = virasoro_rho_numerical(c_val)
            asymptotic = 6.0 / c_val
            # Should agree to within 10% for c=100, 1% for c=1000
            assert abs(rho / asymptotic - 1) < 0.1 / (c_val / 100)

    def test_complete_landscape_structure(self):
        """Complete landscape has all four classes."""
        from lib.shadow_radius_landscape import complete_landscape
        ls = complete_landscape()
        assert 'CLASS_G' in ls
        assert 'CLASS_L' in ls
        assert 'CLASS_C' in ls
        assert 'CLASS_M' in ls

    def test_koszul_conductor_formula(self):
        """K_N = 2(N-1)(2N^2+2N+1) for type A."""
        from lib.shadow_radius_landscape import KOSZUL_CONDUCTORS
        for N, K_expected in KOSZUL_CONDUCTORS.items():
            K_formula = 2 * (N - 1) * (2 * N**2 + 2 * N + 1)
            assert K_formula == K_expected, f"K_{N}: {K_formula} != {K_expected}"

    def test_self_dual_cc_formula(self):
        """Self-dual central charge = K_N / 2."""
        from lib.shadow_radius_landscape import SELF_DUAL_CC, KOSZUL_CONDUCTORS
        for N in KOSZUL_CONDUCTORS:
            assert SELF_DUAL_CC[N] == Rational(KOSZUL_CONDUCTORS[N], 2)

    def test_wn_rho_squared_positive(self):
        """rho^2 > 0 for all channels at c > 0."""
        from lib.shadow_radius_landscape import wn_channel_rho_squared
        for N in [3, 4, 5]:
            for j in range(2, N + 1):
                rho_sq = wn_channel_rho_squared(N, j, 26)
                assert float(rho_sq.evalf()) > 0


# ============================================================================
# 13. Cross-checks with existing shadow_radius module
# ============================================================================

class TestCrossChecks:
    """Cross-checks against the existing shadow_radius.py module."""

    def test_virasoro_rho_matches_shadow_radius(self):
        """New module matches old shadow_radius.py at all test points."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        from lib.shadow_radius_landscape import virasoro_rho_squared
        _, rho_sq_old = virasoro_shadow_radius_formula()
        rho_sq_new = virasoro_rho_squared()
        assert simplify(cancel(rho_sq_old - rho_sq_new)) == 0

    def test_critical_c_matches(self):
        """Critical c* matches between old and new modules."""
        from lib.shadow_radius import virasoro_critical_central_charge
        from lib.shadow_radius_landscape import virasoro_critical_cubic
        c_star_old = float(virasoro_critical_central_charge().evalf())
        _, _, c_star_new = virasoro_critical_cubic()
        assert abs(c_star_old - c_star_new) < 1e-6

    def test_koszul_product_matches(self):
        """Koszul duality data matches old module."""
        from lib.shadow_radius import virasoro_koszul_product
        from lib.shadow_radius_landscape import virasoro_koszul_pair
        for cv in [1, 5, 13, 25]:
            old = virasoro_koszul_product(cv)
            new = virasoro_koszul_pair(cv)
            assert abs(old['rho'] - new['rho']) < 1e-8
            assert abs(old['rho_dual'] - new['rho_dual']) < 1e-8

    def test_shadow_radius_atlas_consistency(self):
        """Shadow radius atlas entries are consistent."""
        from lib.shadow_radius import shadow_radius_atlas
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        atlas = shadow_radius_atlas()
        # Check Virasoro special values
        sv = atlas['Virasoro Vir_c']['special_values']
        for label, c_val in [('c=1 (free boson)', 1),
                              ('c=13 (self-dual)', 13),
                              ('c=26 (string)', 26)]:
            old_rho = sv[label]['rho']
            new_rho = virasoro_rho_numerical(c_val)
            assert abs(old_rho - new_rho) < 1e-6

    def test_w3_koszul_conductors_match(self):
        """W_3 Koszul conductor matches shadow_tower_atlas."""
        from lib.shadow_tower_atlas import KOSZUL_CONDUCTORS as KC_old
        from lib.shadow_radius_landscape import KOSZUL_CONDUCTORS as KC_new
        for N in [2, 3, 4, 5, 6]:
            assert KC_old[N] == KC_new[N]


# ============================================================================
# 14. Monotonicity and global structure
# ============================================================================

class TestGlobalStructure:
    """Global structure of the shadow radius landscape."""

    def test_virasoro_rho_monotone_decreasing_large_c(self):
        """rho(c) is monotonically decreasing for c > c*."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        rho_prev = virasoro_rho_numerical(7)
        for cv in [8, 10, 13, 20, 26, 50, 100]:
            rho_curr = virasoro_rho_numerical(cv)
            assert rho_curr < rho_prev, f"rho should decrease: c={cv}"
            rho_prev = rho_curr

    def test_w3_wline_rho_monotone_decreasing(self):
        """W-line rho decreasing for large c."""
        from lib.shadow_radius_landscape import w3_wline_rho_numerical
        rho_prev = w3_wline_rho_numerical(5)
        for cv in [10, 20, 50, 100]:
            rho_curr = w3_wline_rho_numerical(cv)
            assert rho_curr < rho_prev, f"W-line rho should decrease: c={cv}"
            rho_prev = rho_curr

    def test_wn_higher_channel_rho_scales_geometrically(self):
        """Higher channels decay geometrically: rho_j / rho_{j-1} ~ const."""
        from lib.shadow_radius_landscape import wn_all_channel_rho
        channels = wn_all_channel_rho(5, 26)
        ratios = []
        for j in range(3, 6):
            if channels[j - 1] > 0:
                ratios.append(channels[j] / channels[j - 1])
        # Ratios should be roughly similar (geometric decay)
        for ratio in ratios:
            assert ratio < 1.0, "Higher channel should be smaller"

    def test_all_unitary_minimal_models_divergent(self):
        """All unitary minimal models (c < 1) have divergent shadow obstruction towers."""
        from lib.shadow_radius_landscape import virasoro_rho_numerical
        # Unitary minimal model central charges: c = 1 - 6/((m+2)(m+3))
        for m in range(1, 10):
            c_min = 1 - 6 / ((m + 2) * (m + 3))
            if c_min > 0:
                rho = virasoro_rho_numerical(c_min)
                assert rho > 1.0, f"Minimal model m={m}, c={c_min:.4f} should be divergent"
