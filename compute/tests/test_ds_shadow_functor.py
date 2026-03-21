"""Tests for the DS shadow functor: sl_N -> W_N.

Verifies:
  - Central charge maps (Sugawara, DS, ghost)
  - Kappa compatibility under DS reduction for N=2,...,8
  - Cubic shadow compatibility
  - Quartic mechanism (zero -> nonzero)
  - Koszul conductor formula
  - Feigin-Frenkel duality
  - Numerical verification at specific levels
"""

import pytest
from sympy import Rational, Symbol, simplify, factor

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'ds_shadow_functor',
    os.path.join(_lib_dir, 'ds_shadow_functor.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

k = Symbol('k')
c = Symbol('c')


# ============================================================
# Central charge tests
# ============================================================

class TestCentralCharge:
    def test_sugawara_sl2(self):
        """c_{sl_2}(k) = 3k/(k+2)."""
        cc = _mod.sugawara_central_charge('A', 1)
        assert simplify(cc - 3*k/(k+2)) == 0

    def test_sugawara_sl3(self):
        """c_{sl_3}(k) = 8k/(k+3)."""
        cc = _mod.sugawara_central_charge('A', 2)
        assert simplify(cc - 8*k/(k+3)) == 0

    def test_ds_w2_is_virasoro(self):
        """W_2 = Virasoro: c = 1 - 6/(k+2)... no: c = 1(1-6/(k+2))."""
        cc = _mod.ds_central_charge('A', 1)
        # c_{Vir}(k) = (2-1)(1-2*3/(k+2)) = 1 - 6/(k+2)
        expected = 1 - 6 / (k + 2)
        assert simplify(cc - expected) == 0

    def test_ds_w3(self):
        """c_{W_3}(k) = 2(1-12/(k+3))."""
        cc = _mod.ds_central_charge('A', 2)
        expected = 2 * (1 - 12 / (k + 3))
        assert simplify(cc - expected) == 0

    def test_ds_w3_at_k1(self):
        """c_{W_3}(1) = 2 - 24/4 = -4."""
        cc = _mod.ds_central_charge('A', 2, 1)
        assert cc == -4

    def test_ds_w3_large_k(self):
        """c_{W_3}(k) -> 2 as k -> infinity."""
        cc = _mod.ds_central_charge('A', 2)
        # Take limit k -> large number
        assert abs(float(cc.subs(k, 10000)) - 2) < 0.01

    def test_ghost_central_charge_sl3(self):
        """Ghost central charge for sl_3 = 6 (level-independent)."""
        c_ghost = _mod.ghost_central_charge('A', 2)
        assert simplify(c_ghost - 6) == 0, \
            f"Ghost central charge = {factor(c_ghost)}, expected 6"

    def test_ghost_central_charge_sl2(self):
        """Ghost central charge for sl_2."""
        c_ghost = _mod.ghost_central_charge('A', 1)
        # c_{sl_2} - c_{Vir} = 3k/(k+2) - (1 - 6/(k+2))
        # = (3k - k - 2 + 6)/(k+2) = (2k+4)/(k+2) = 2
        assert simplify(c_ghost - 2) == 0


# ============================================================
# Kappa compatibility tests
# ============================================================

class TestKappaCompatibility:
    @pytest.mark.parametrize('n', [2, 3, 4, 5, 6, 7, 8])
    def test_kappa_ds_compatible(self, n):
        """kappa(W_N) + kappa(ghosts) = kappa(sl_N) for N=2,...,8."""
        result = _mod.verify_kappa_ds_compatibility(n)
        assert result['compatible'], \
            f"N={n}: difference = {result['difference']}"

    def test_kappa_sl2(self):
        """kappa(sl_2) = 3(k+2)/4."""
        kap = _mod.kappa_affine_slN(2)
        assert simplify(kap - 3*(k+2)/4) == 0

    def test_kappa_sl3(self):
        """kappa(sl_3) = 4(k+3)/3."""
        kap = _mod.kappa_affine_slN(3)
        assert simplify(kap - Rational(4)*(k+3)/3) == 0

    def test_kappa_w3(self):
        """kappa(W_3) = 5c/6 at c = c_{W_3}(k)."""
        c_w3 = _mod.ds_central_charge('A', 2)
        kap = _mod.kappa_wN(3, c_w3)
        expected = Rational(5) * c_w3 / 6
        assert simplify(kap - expected) == 0


# ============================================================
# Quartic shadow tests
# ============================================================

class TestQuarticDS:
    def test_sl_n_quartic_vanishes(self):
        """Affine sl_N quartic shadow = 0 (Jacobi identity)."""
        for n in [2, 3, 4, 5]:
            Q = _mod.quartic_shadow_slN(n)
            assert Q == 0, f"sl_{n} quartic should vanish"

    def test_virasoro_quartic_nonzero(self):
        """Virasoro quartic Q = 10/(c(5c+22)) is nonzero."""
        Q = _mod.quartic_shadow_virasoro()
        assert Q != 0

    def test_virasoro_quartic_at_c1(self):
        """Q_{Vir}(c=1) = 10/(1*27) = 10/27."""
        Q = _mod.quartic_shadow_virasoro(1)
        assert Q == Rational(10, 27)

    def test_quartic_mechanism_ghost(self):
        """DS quartic creation mechanism: ghost contribution."""
        mech = _mod.ds_quartic_mechanism()
        assert mech['Q_slN'] == 0
        assert 'ghost' in mech['mechanism'].lower()


# ============================================================
# Koszul conductor tests
# ============================================================

class TestKoszulConductor:
    @pytest.mark.parametrize('n, K', [(2, 26), (3, 100), (4, 246), (5, 488), (6, 850)])
    def test_known_conductors(self, n, K):
        """Verify known Koszul conductors K_N."""
        K_computed = _mod.koszul_conductor_wN(n)
        assert K_computed == K, f"K_{n} = {K_computed}, expected {K}"

    @pytest.mark.parametrize('n', [2, 3, 4, 5, 6])
    def test_ff_duality(self, n):
        """Feigin-Frenkel: c(k) + c(k') = K_N."""
        ff = _mod.ff_duality_ds_check(n)
        assert ff['complementary'], \
            f"N={n}: c_sum = {ff['c_sum']}, K_N = {ff['K_N']}"


# ============================================================
# Numerical verification tests
# ============================================================

class TestNumerical:
    def test_kappa_numerical_sl3(self):
        """Numerical kappa verification for sl_3 at k=1,...,100."""
        results = _mod.numerical_kappa_verification(3, [1, 2, 3, 5, 10, 100])
        for r in results:
            kap_sum = r['kappa_WN'] + r['kappa_ghosts']
            assert abs(kap_sum - r['kappa_slN']) < 1e-10, \
                f"k={r['k']}: kappa_WN + kappa_ghosts = {kap_sum}, " \
                f"kappa_sl3 = {r['kappa_slN']}"

    def test_quartic_ds_numerical(self):
        """Q_{Vir}(c_{W_3}(k)) is finite at non-critical levels."""
        results = _mod.quartic_ds_numerical([1, 2, 3, 5, 10])
        for r in results:
            assert abs(r['Q_Vir_T']) < 1e6, \
                f"k={r['k']}: Q diverges? Q = {r['Q_Vir_T']}"

    def test_central_charge_inverse(self):
        """c -> k -> c roundtrip."""
        for c_val in [Rational(-4), Rational(-14, 5), Rational(4, 5), Rational(1)]:
            k_val = _mod.central_charge_to_level(3, c_val)
            c_back = _mod.ds_level_to_central_charge(3, Rational(k_val))
            assert simplify(Rational(c_back) - c_val) == 0, \
                f"Roundtrip failed: c={c_val} -> k={k_val} -> c={c_back}"


# ============================================================
# Full shadow functor tests
# ============================================================

class TestFullFunctor:
    def test_sl3_functor_complete(self):
        """Complete sl_3 -> W_3 shadow functor."""
        data = _mod.ds_shadow_functor_sl3()
        assert data['kappa_compatible']
        assert data['cubic_compatible']

    def test_general_functor(self):
        """General sl_N -> W_N functor for N=2,...,8."""
        results = _mod.ds_shadow_functor_general(8)
        for n, data in results.items():
            assert data['compatible'], f"N={n} kappa not compatible"

    def test_ghost_kappa_positive_for_large_k(self):
        """Ghost kappa is positive for large k (unitarity region)."""
        for n in [2, 3, 4, 5]:
            kap_ghost = _mod.kappa_ghosts_principal(n)
            val = float(kap_ghost.subs(k, 100))
            assert val > 0, f"N={n}: ghost kappa = {val} < 0 at k=100"
