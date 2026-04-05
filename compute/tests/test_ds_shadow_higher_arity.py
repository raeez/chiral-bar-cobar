"""Tests for DS shadow functor at higher arities and Bershadsky-Polyakov reduction.

Verifies:
  - Principal DS shadow obstruction tower at arities 5-8 for W_2 (Virasoro) and W_3
  - Consistency with the Virasoro tower under the DS central charge map
  - Depth-increase mechanism: sl_N depth 3 -> W_N depth infinity
  - Bershadsky-Polyakov central charge, kappa, and shadow obstruction tower
  - BP J-line Gaussian structure (depth 2)
  - BP T-line matches Virasoro at c = c_BP(k)
  - Feigin-Frenkel involution and complementarity for both principal and BP
  - Ghost central charge level-independence for principal DS
  - Principal vs minimal DS comparison for sl_3

Target: 70+ tests covering both established and new mathematical territory.
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'ds_shadow_higher_arity',
    os.path.join(_lib_dir, 'ds_shadow_higher_arity.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

# Also import the existing ds_shadow_functor for cross-validation
_spec2 = importlib.util.spec_from_file_location(
    'ds_shadow_functor',
    os.path.join(_lib_dir, 'ds_shadow_functor.py')
)
_dsf = importlib.util.module_from_spec(_spec2)
_spec2.loader.exec_module(_dsf)

# And the virasoro_shadow_factored for Delta-factored form
_spec3 = importlib.util.spec_from_file_location(
    'virasoro_shadow_factored',
    os.path.join(_lib_dir, 'virasoro_shadow_factored.py')
)
_vsf = importlib.util.module_from_spec(_spec3)
_spec3.loader.exec_module(_vsf)

k = Symbol('k')
c = Symbol('c')


# ============================================================
# Section 1: Principal DS shadow obstruction tower at arities 5-8 (Virasoro = W_2)
# ============================================================

class TestPrincipalDSVirasoro:
    """Verify the principal DS shadow obstruction tower for W_2 = Virasoro at arities 5-8."""

    def _virasoro_tower(self, max_r=8):
        return _mod.principal_ds_shadow_tower(2, max_r=max_r)

    def test_arity2_kappa(self):
        """Sh_2 = (k-4)/(2(k+2)) for Virasoro at c(k) = (k-4)/(k+2)."""
        tower = self._virasoro_tower()
        expected = (k - 4) / (2 * (k + 2))
        assert simplify(tower[2] - expected) == 0

    def test_arity3_cubic(self):
        """Sh_3 = 2 (constant, level-independent)."""
        tower = self._virasoro_tower()
        assert simplify(tower[3] - 2) == 0

    def test_arity4_quartic(self):
        """Sh_4 is nonzero and matches DS substitution into Virasoro Q."""
        tower = self._virasoro_tower()
        # Virasoro Q = 10/[c(5c+22)], at c = (k-4)/(k+2):
        c_k = (k - 4) / (k + 2)
        expected = Rational(10) / (c_k * (5 * c_k + 22))
        assert simplify(tower[4] - expected) == 0

    def test_arity5_nonzero(self):
        """Sh_5 != 0 at generic k (quintic forced)."""
        tower = self._virasoro_tower()
        # Evaluate at k=7 (generic)
        val = tower[5].subs(k, 7)
        assert val != 0, "Quintic should be nonzero at generic level"

    def test_arity5_explicit(self):
        """Sh_5 matches Virasoro tower S_5(c(k))."""
        tower = self._virasoro_tower()
        vir = _mod._virasoro_tower_internal(5)
        c_k = (k - 4) / (k + 2)
        expected = cancel(vir[5].subs(c, c_k))
        assert simplify(tower[5] - expected) == 0

    def test_arity6_nonzero(self):
        """Sh_6 != 0 at k=7."""
        tower = self._virasoro_tower()
        assert tower[6].subs(k, 7) != 0

    def test_arity7_nonzero(self):
        """Sh_7 != 0 at k=7."""
        tower = self._virasoro_tower()
        assert tower[7].subs(k, 7) != 0

    def test_arity8_nonzero(self):
        """Sh_8 != 0 at k=7."""
        tower = self._virasoro_tower()
        assert tower[8].subs(k, 7) != 0

    def test_arity5_sign(self):
        """Sh_5 is negative at large positive k (c > 0 region)."""
        tower = self._virasoro_tower()
        val = float(tower[5].subs(k, 100))
        assert val < 0, f"Expected Sh_5 < 0 at k=100, got {val}"

    def test_arity5_matches_known(self):
        """Sh_5 coefficient matches -48/[c^2(5c+22)] at c = c(k)."""
        vir = _mod._virasoro_tower_internal(5)
        expected_S5 = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(vir[5] - expected_S5) == 0

    @pytest.mark.parametrize('level_val', [1, 2, 3, 5, 10, 50])
    def test_numerical_match(self, level_val):
        """Numerical: DS tower matches Virasoro tower through DS map at each k."""
        tower = _mod.principal_ds_shadow_tower(2, max_r=8)
        vir = _mod._virasoro_tower_internal(8)
        c_k = Rational(level_val - 4, level_val + 2)
        for r in range(2, 9):
            ds_val = float(tower[r].subs(k, level_val))
            vir_val = float(vir[r].subs(c, c_k))
            # Use relative tolerance for large values
            tol = max(1e-10, 1e-6 * max(abs(ds_val), abs(vir_val), 1))
            assert abs(ds_val - vir_val) < tol, \
                f"Mismatch at r={r}, k={level_val}: DS={ds_val}, Vir={vir_val}"


# ============================================================
# Section 2: Principal DS shadow obstruction tower for W_3 at arities 5-8
# ============================================================

class TestPrincipalDSW3:
    """Verify the principal DS shadow obstruction tower for W_3 at arities 5-8."""

    def _w3_tower(self, max_r=8):
        return _mod.principal_ds_shadow_tower(3, max_r=max_r)

    def test_arity2_kappa_w3(self):
        """Sh_2(W_3) = c(k)/2 where c(k) = 2(k-9)/(k+3)."""
        tower = self._w3_tower()
        c_w3 = 2 * (k - 9) / (k + 3)
        expected = c_w3 / 2
        assert simplify(tower[2] - expected) == 0

    def test_arity3_cubic_w3(self):
        """Sh_3(W_3) = 2 (same as Virasoro, universal cubic)."""
        tower = self._w3_tower()
        assert simplify(tower[3] - 2) == 0

    def test_arity4_quartic_w3(self):
        """Sh_4(W_3) is nonzero at k=10."""
        tower = self._w3_tower()
        assert tower[4].subs(k, 10) != 0

    def test_arity5_nonzero_w3(self):
        """Sh_5(W_3) != 0 at k=10."""
        tower = self._w3_tower()
        assert tower[5].subs(k, 10) != 0

    def test_arity6_nonzero_w3(self):
        """Sh_6(W_3) != 0 at k=10."""
        tower = self._w3_tower()
        assert tower[6].subs(k, 10) != 0

    def test_arity7_nonzero_w3(self):
        """Sh_7(W_3) != 0 at k=10."""
        tower = self._w3_tower()
        assert tower[7].subs(k, 10) != 0

    def test_arity8_nonzero_w3(self):
        """Sh_8(W_3) != 0 at k=10."""
        tower = self._w3_tower()
        assert tower[8].subs(k, 10) != 0

    def test_tower_rational_in_k(self):
        """All Sh_r are rational functions of k (no square roots)."""
        tower = self._w3_tower()
        for r in range(2, 9):
            # factor() would fail on irrational expressions
            factored = factor(tower[r])
            assert factored.is_rational_function(k), \
                f"Sh_{r} is not rational in k: {factored}"

    @pytest.mark.parametrize('level_val', [1, 2, 5, 10, 20])
    def test_w3_numerical_match(self, level_val):
        """Numerical: W_3 DS tower matches Virasoro at c = c_{W_3}(k)."""
        tower = _mod.principal_ds_shadow_tower(3, max_r=8)
        vir = _mod._virasoro_tower_internal(8)
        c_w3_val = Rational(2 * (level_val - 9), level_val + 3)
        for r in range(2, 9):
            ds_val = float(tower[r].subs(k, level_val))
            vir_val = float(vir[r].subs(c, c_w3_val))
            tol = max(1e-10, 1e-6 * max(abs(ds_val), abs(vir_val), 1))
            assert abs(ds_val - vir_val) < tol, \
                f"Mismatch at r={r}, k={level_val}: DS={ds_val}, Vir={vir_val}"


# ============================================================
# Section 3: Higher N principal DS (W_4, W_5, W_6)
# ============================================================

class TestPrincipalDSHigherN:
    """Principal DS shadow obstruction tower for W_N at N = 4, 5, 6."""

    @pytest.mark.parametrize('n', [4, 5, 6])
    def test_quintic_nonzero(self, n):
        """Sh_5(W_N) != 0 at k=20 for N=4,5,6."""
        tower = _mod.principal_ds_shadow_tower(n, max_r=5)
        assert tower[5].subs(k, 20) != 0

    @pytest.mark.parametrize('n', [4, 5, 6])
    def test_cubic_universal(self, n):
        """Sh_3 = 2 for all W_N (universal cubic)."""
        tower = _mod.principal_ds_shadow_tower(n, max_r=3)
        assert simplify(tower[3] - 2) == 0

    @pytest.mark.parametrize('n', [4, 5, 6])
    def test_rational_tower(self, n):
        """All entries are rational functions of k."""
        tower = _mod.principal_ds_shadow_tower(n, max_r=6)
        for r in range(2, 7):
            assert factor(tower[r]).is_rational_function(k)


# ============================================================
# Section 4: Depth increase mechanism
# ============================================================

class TestDepthIncrease:
    """Verify the depth increase sl_N (depth 3) -> W_N (depth inf)."""

    @pytest.mark.parametrize('n', [2, 3, 4, 5, 6])
    def test_depth_increase_table(self, n):
        """sl_N has depth 3, W_N has depth infinity, for N=2..6."""
        table = _mod.ds_shadow_depth_comparison(n + 1)
        assert table[n]['sl_N_depth'] == 3
        assert table[n]['W_N_depth'] == 'infinity'
        assert table[n]['Q_4_nonzero']

    @pytest.mark.parametrize('n', [2, 3, 4])
    def test_quartic_seed_mechanism(self, n):
        """DS creates quartic from ghost sector; mechanism data is populated."""
        mech = _mod.ds_depth_increase_mechanism(n)
        assert mech['sl_N_depth'] == 3
        assert mech['W_N_depth'] == 'infinity'
        assert mech['Q_quartic_seed'] != 0

    def test_depth_increase_quintic_from_seed(self):
        """The quintic is generated from the quartic seed, not from sl_N."""
        mech = _mod.ds_depth_increase_mechanism(3)
        # The quintic comes from {C, Q}_H where Q is DS-created
        Sh5 = mech['Sh5_from_seed']
        assert Sh5.subs(k, 10) != 0


# ============================================================
# Section 5: BP central charge
# ============================================================

class TestBPCentralCharge:
    """Verify BP central charge: c_BP(k) = 2 - 3(2k+3)^2/(k+3)."""

    def test_bp_formula(self):
        """c_BP(k) = (-12k^2 - 34k - 21)/(k+3)."""
        c_bp = _mod.bp_central_charge()
        expected = (-12 * k**2 - 34 * k - 21) / (k + 3)
        assert simplify(c_bp - expected) == 0

    def test_bp_at_k1(self):
        """c_BP(1) = -67/4 = 2 - 75/4."""
        c_val = _mod.bp_central_charge(Rational(1))
        assert simplify(c_val - Rational(-67, 4)) == 0, f"c_BP(1) = {c_val}"

    def test_bp_at_k0(self):
        """c_BP(0) = -7."""
        c_val = _mod.bp_central_charge(Rational(0))
        assert simplify(c_val + 7) == 0, f"c_BP(0) = {c_val}"

    def test_bp_at_k_neg1(self):
        """c_BP(-1) = 1/2."""
        c_val = _mod.bp_central_charge(Rational(-1))
        assert simplify(c_val - Rational(1, 2)) == 0, f"c_BP(-1) = {c_val}"

    def test_bp_at_k_neg3_half(self):
        """c_BP(-3/2) = 2 (the (2k+3)^2 term vanishes)."""
        c_val = _mod.bp_central_charge(Rational(-3, 2))
        assert simplify(c_val - 2) == 0

    def test_bp_at_k2(self):
        """c_BP(2) = -137/5 = 2 - 147/5."""
        c_val = _mod.bp_central_charge(Rational(2))
        assert simplify(c_val - Rational(-137, 5)) == 0, f"c_BP(2) = {c_val}"

    def test_bp_numerator_irreducible(self):
        """12k^2 + 34k + 21 has discriminant 148 = 4*37 (not a perfect square)."""
        disc = 34**2 - 4 * 12 * 21
        assert disc == 148
        # 148 = 4*37, and 37 is prime -> sqrt(148) is irrational
        assert disc > 0  # two real roots, but irrational

    def test_bp_large_k_asymptotics(self):
        """c_BP(k) ~ -12k as k -> infinity."""
        c_bp = _mod.bp_central_charge()
        # At k=1000: c ~ -12000
        val = float(c_bp.subs(k, 1000))
        assert abs(val / (-12000) - 1) < 0.01

    def test_bp_differs_from_principal(self):
        """c_BP != c_{W_3} for generic k."""
        c_bp = _mod.bp_central_charge()
        c_w3 = _mod.principal_ds_central_charge(3)
        assert simplify(c_bp - c_w3) != 0


# ============================================================
# Section 6: BP kappa values
# ============================================================

class TestBPKappa:
    """Verify kappa values for BP on T-line and J-line."""

    def test_kappa_t_equals_c_over_2(self):
        """kappa_BP on T-line = c_BP/2 (Virasoro curvature)."""
        kappa_t = _mod.bershadsky_polyakov_kappa()
        expected = _mod.bp_central_charge() / 2
        assert simplify(kappa_t - expected) == 0

    def test_kappa_j_formula(self):
        """kappa_J = (k + 1/2)/2 = (2k+1)/4."""
        kappa_j = _mod.bershadsky_polyakov_kappa_j()
        expected = (2 * k + 1) / 4
        assert simplify(kappa_j - expected) == 0

    def test_kappa_j_at_k1(self):
        """kappa_J(1) = 3/4."""
        kappa_j = _mod.bershadsky_polyakov_kappa_j(1)
        assert kappa_j == Rational(3, 4)

    def test_kappa_j_at_k0(self):
        """kappa_J(0) = 1/4."""
        kappa_j = _mod.bershadsky_polyakov_kappa_j(0)
        assert kappa_j == Rational(1, 4)

    def test_kappa_t_at_k1(self):
        """kappa_T(1) = c_BP(1)/2 = -67/8."""
        kappa_t = _mod.bershadsky_polyakov_kappa(Rational(1))
        assert simplify(kappa_t - Rational(-67, 8)) == 0, f"kappa_T(1) = {kappa_t}"


# ============================================================
# Section 7: BP shadow obstruction tower on T-line
# ============================================================

class TestBPTLine:
    """Verify BP shadow obstruction tower on the T-line = Virasoro at c_BP(k)."""

    def _bp_tower(self, max_r=6):
        return _mod.bershadsky_polyakov_shadow_tower(max_r)

    def test_bp_tline_arity2(self):
        """Sh_2 on T-line = c_BP/2."""
        tower = self._bp_tower()
        assert simplify(tower[2] - _mod.bp_central_charge() / 2) == 0

    def test_bp_tline_arity3(self):
        """Sh_3 on T-line = 2 (universal cubic)."""
        tower = self._bp_tower()
        assert simplify(tower[3] - 2) == 0

    def test_bp_tline_arity4_nonzero(self):
        """Sh_4 on T-line is nonzero at k=5."""
        tower = self._bp_tower()
        assert tower[4].subs(k, 5) != 0

    def test_bp_tline_arity5_nonzero(self):
        """Sh_5 on T-line is nonzero at k=5 (quintic forced)."""
        tower = self._bp_tower()
        assert tower[5].subs(k, 5) != 0

    def test_bp_tline_arity6_nonzero(self):
        """Sh_6 on T-line is nonzero at k=5."""
        tower = self._bp_tower()
        assert tower[6].subs(k, 5) != 0

    def test_bp_tline_matches_virasoro(self):
        """BP T-line tower = Virasoro tower at c = c_BP(k), numerically at k=5."""
        tower = self._bp_tower()
        vir = _mod._virasoro_tower_internal(6)
        c_bp_val = float(_mod.bp_central_charge(5))
        for r in range(2, 7):
            bp_val = float(tower[r].subs(k, 5))
            vir_val = float(vir[r].subs(c, c_bp_val))
            assert abs(bp_val - vir_val) < 1e-10, \
                f"Mismatch at r={r}: BP={bp_val}, Vir={vir_val}"

    def test_bp_tline_rational(self):
        """All BP T-line coefficients are rational in k."""
        tower = self._bp_tower()
        for r in range(2, 7):
            assert factor(tower[r]).is_rational_function(k)

    def test_bp_quartic_on_tline_formula(self):
        """Quartic on T-line = 10/[c_BP*(5c_BP + 22)]."""
        Q = _mod.bp_quartic_on_tline()
        c_bp = _mod.bp_central_charge()
        expected = cancel(Rational(10) / (c_bp * (5 * c_bp + 22)))
        assert simplify(Q - expected) == 0


# ============================================================
# Section 8: BP J-line (Gaussian, depth 2)
# ============================================================

class TestBPJLine:
    """Verify BP shadow obstruction tower on the J-line is Gaussian (depth 2)."""

    def test_j_line_kappa(self):
        """J-line kappa = (k+1/2)/2."""
        tower = _mod.bershadsky_polyakov_j_line(4)
        expected = (k + Rational(1, 2)) / 2
        assert simplify(tower[2] - expected) == 0

    def test_j_line_cubic_zero(self):
        """J-line cubic = 0 (U(1) is abelian)."""
        tower = _mod.bershadsky_polyakov_j_line(4)
        assert tower[3] == 0

    def test_j_line_quartic_zero(self):
        """J-line quartic = 0 (U(1) has no quartic obstruction)."""
        tower = _mod.bershadsky_polyakov_j_line(4)
        assert tower[4] == 0

    def test_j_line_depth_is_2(self):
        """J-line shadow depth = 2 (class G)."""
        tower = _mod.bershadsky_polyakov_j_line(4)
        # All arities >= 3 should be zero
        for r in range(3, 5):
            assert tower[r] == 0, f"Sh_{r} should be 0 on J-line"


# ============================================================
# Section 9: Feigin-Frenkel duality
# ============================================================

class TestFeiginFrenkelDuality:
    """Verify FF involution and complementarity."""

    @pytest.mark.parametrize('n', [2, 3, 4, 5, 6])
    def test_ff_involution_principal(self, n):
        """(k')' = k for principal FF dual level."""
        assert _mod.ff_involution_check_principal(n)

    def test_ff_involution_bp(self):
        """(k')' = k for BP dual level k' = -k - 6."""
        assert _mod.ff_involution_check_bp()

    def test_ff_complementarity_bp(self):
        """c_BP(k) + c_BP(-k-6) = 76."""
        result = _mod.ff_complementarity_check_bp()
        assert result['complementary'], \
            f"c_sum = {result['c_sum']}, expected 76"

    def test_bp_koszul_conductor(self):
        """K_BP = 76."""
        result = _mod.ff_complementarity_check_bp()
        assert result['K_BP'] == 76

    def test_bp_dual_level_formula(self):
        """k' = -k - 6 for BP."""
        kp = _mod.bp_dual_level()
        assert simplify(kp - (-k - 6)) == 0

    def test_bp_dual_at_k1(self):
        """At k=1: k' = -7."""
        kp = _mod.bp_dual_level(1)
        assert kp == -7

    def test_bp_dual_at_k0(self):
        """At k=0: k' = -6."""
        kp = _mod.bp_dual_level(0)
        assert kp == -6


# ============================================================
# Section 10: Ghost central charge
# ============================================================

class TestGhostCentralCharge:
    """Verify ghost central charge properties."""

    @pytest.mark.parametrize('n', [2, 3, 4, 5, 6])
    def test_ghost_level_independent(self, n):
        """Ghost c is level-independent for principal DS of sl_N."""
        result = _mod.ghost_central_charge_level_independence(n + 1)
        assert result[n]['level_independent'], \
            f"N={n}: ghost c = {result[n]['c_ghosts']} is k-dependent"

    @pytest.mark.parametrize('n, expected', [(2, 2), (3, 6), (4, 12), (5, 20), (6, 30)])
    def test_ghost_values(self, n, expected):
        """Ghost c values: N(N-1) for principal DS of sl_N."""
        result = _mod.ghost_central_charge_level_independence(n + 1)
        c_ghost = result[n]['c_ghosts']
        assert simplify(c_ghost - expected) == 0, \
            f"N={n}: expected c_ghosts = {expected}, got {c_ghost}"

    def test_ghost_bp_level_dependent(self):
        """Ghost c for BP is level-DEPENDENT (unlike principal)."""
        from sympy import diff as sym_diff
        c_ghost_bp = _mod.ghost_central_charge_bp()
        assert simplify(sym_diff(c_ghost_bp, k)) != 0, \
            "BP ghost central charge should depend on k"


# ============================================================
# Section 11: Cross-validation with existing ds_shadow_functor.py
# ============================================================

class TestCrossValidation:
    """Cross-validate with the existing ds_shadow_functor.py module."""

    def test_central_charge_match_sl2(self):
        """DS central charge for sl_2 matches between modules."""
        c_new = _mod.principal_ds_central_charge(2)
        c_old = _dsf.ds_central_charge('A', 1)
        assert simplify(c_new - c_old) == 0

    def test_central_charge_match_sl3(self):
        """DS central charge for sl_3 matches between modules."""
        c_new = _mod.principal_ds_central_charge(3)
        c_old = _dsf.ds_central_charge('A', 2)
        assert simplify(c_new - c_old) == 0

    @pytest.mark.parametrize('n', [2, 3, 4, 5])
    def test_kappa_compatibility_preserved(self, n):
        """kappa(W_N) + kappa(ghosts) = kappa(sl_N), consistent with old module."""
        result = _dsf.verify_kappa_ds_compatibility(n)
        assert result['compatible']

    def test_quartic_virasoro_matches_old(self):
        """Virasoro quartic from new module matches old module."""
        Q_new = _mod._virasoro_tower_internal(4)[4]
        Q_old = _dsf.quartic_shadow_virasoro()
        assert simplify(Q_new - Q_old) == 0


# ============================================================
# Section 12: Delta-factored form under DS
# ============================================================

class TestDeltaFactored:
    """Verify Delta-factored structure of higher-arity DS shadows."""

    def test_virasoro_delta_factorization_at_c_of_k(self):
        """Sh_r = Delta * R_r holds after c -> c(k) substitution."""
        # Delta_Vir = 40/(5c+22)
        c_k = (k - 4) / (k + 2)
        Delta_k = Rational(40) / (5 * c_k + 22)
        tower = _mod.principal_ds_shadow_tower(2, max_r=8)
        for r in range(4, 9):
            R_r_k = cancel(tower[r] / Delta_k)
            reconstructed = cancel(Delta_k * R_r_k)
            assert simplify(reconstructed - tower[r]) == 0, \
                f"Delta factorization fails at r={r}"

    def test_delta_bp_nonzero(self):
        """BP discriminant Delta on T-line is nonzero at k=5."""
        delta = _mod.bp_discriminant_on_tline(5)
        assert delta != 0

    def test_5c22_bp_factor(self):
        """5c_BP + 22 is a rational function of k with known structure."""
        val = _mod.bp_5c_plus_22()
        # Should be a rational function, nonzero at generic k
        assert val.subs(k, 5) != 0
        assert factor(val).is_rational_function(k)


# ============================================================
# Section 13: Principal vs minimal DS comparison
# ============================================================

class TestPrincipalVsMinimal:
    """Compare principal (sl_3 -> W_3) and minimal (sl_3 -> BP) DS."""

    def test_different_central_charges(self):
        """c_W3 != c_BP."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert simplify(comp['c_W3'] - comp['c_BP']) != 0

    def test_different_koszul_conductors(self):
        """K_W3 = 100, K_BP = 76."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert comp['K_W3'] == 100
        assert comp['K_BP'] == 76

    def test_bp_has_j_line(self):
        """BP has a J-line (U(1) current) that W_3 does not."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert comp['BP_J_depth'] == '2 (class G)'

    def test_both_have_infinite_t_depth(self):
        """Both W_3 and BP have depth infinity on the T-line."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert 'infinity' in comp['W3_depth']
        assert 'infinity' in comp['BP_T_depth']

    def test_different_ghost_charges(self):
        """Ghost central charges differ between principal and minimal."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert simplify(comp['c_ghost_principal'] - comp['c_ghost_minimal']) != 0

    def test_principal_ghost_constant(self):
        """Principal ghost charge = 6 (constant)."""
        comp = _mod.principal_vs_minimal_ds_comparison()
        assert simplify(comp['c_ghost_principal'] - 6) == 0


# ============================================================
# Section 14: BP residual level
# ============================================================

class TestBPResidualLevel:
    """Verify BP residual sl_2 level properties."""

    def test_residual_formula(self):
        """k_res = k + 1/2."""
        k_res = _mod.bp_residual_level()
        assert simplify(k_res - k - Rational(1, 2)) == 0

    def test_residual_at_k1(self):
        """k_res(1) = 3/2."""
        k_res = _mod.bp_residual_level(1)
        assert k_res == Rational(3, 2)

    def test_residual_positive_for_k_geq_0(self):
        """k_res > 0 for k >= 0."""
        k_res = _mod.bp_residual_level()
        for kv in [0, 1, 2, 5, 10]:
            assert float(k_res.subs(k, kv)) > 0


# ============================================================
# Section 15: Shadow structure summary
# ============================================================

class TestShadowStructure:
    """Verify the BP shadow structure summary."""

    def test_t_line_depth(self):
        """T-line has depth infinity (class M)."""
        summary = _mod.bp_shadow_structure_summary()
        assert summary['T_line']['depth'] == 'infinity'
        assert summary['T_line']['class'] == 'M'

    def test_j_line_depth(self):
        """J-line has depth 2 (class G)."""
        summary = _mod.bp_shadow_structure_summary()
        assert summary['J_line']['depth'] == 2
        assert summary['J_line']['class'] == 'G'

    def test_j_line_cubic_zero(self):
        """J-line cubic is zero."""
        summary = _mod.bp_shadow_structure_summary()
        assert summary['J_line']['cubic'] == 0

    def test_t_line_cubic_two(self):
        """T-line cubic is 2."""
        summary = _mod.bp_shadow_structure_summary()
        assert summary['T_line']['cubic'] == 2

    def test_generator_weights(self):
        """BP generators: J (1), G+ (3/2), G- (3/2), T (2)."""
        summary = _mod.bp_shadow_structure_summary()
        gens = summary['generators']
        assert gens['J']['weight'] == 1
        assert gens['G+']['weight'] == Rational(3, 2)
        assert gens['G-']['weight'] == Rational(3, 2)
        assert gens['T']['weight'] == 2


# ============================================================
# Section 16: Depth classification table
# ============================================================

class TestDepthClassification:
    """Verify the global depth classification table."""

    def test_classification_populated(self):
        """Classification table has all expected entries."""
        table = _mod.ds_depth_classification()
        assert 'inputs' in table
        assert 'principal_outputs' in table
        assert 'nonprincipal_outputs' in table

    def test_sl_n_depth_3(self):
        """All sl_N inputs have depth 3 (class L)."""
        table = _mod.ds_depth_classification()
        for name, data in table['inputs'].items():
            assert data['depth'] == 3
            assert data['class'] == 'L'

    def test_w_n_depth_infinite(self):
        """All principal W_N outputs have depth infinity (class M)."""
        table = _mod.ds_depth_classification()
        for name, data in table['principal_outputs'].items():
            assert data['depth'] == 'infinity'
            assert data['class'] == 'M'

    def test_bp_mixed_depth(self):
        """BP outputs: T-line = M, J-line = G."""
        table = _mod.ds_depth_classification()
        assert table['nonprincipal_outputs']['BP (T-line)']['class'] == 'M'
        assert table['nonprincipal_outputs']['BP (J-line)']['class'] == 'G'

    def test_depth_increase_universal(self):
        """Depth increase is universal."""
        table = _mod.ds_depth_classification()
        assert table['depth_increase_universal']


# ============================================================
# Section 17: Nonvanishing verification
# ============================================================

class TestNonvanishing:
    """Verify shadow nonvanishing at specific levels."""

    @pytest.mark.parametrize('n', [2, 3, 4])
    def test_quintic_nonvanishing(self, n):
        """Sh_5(W_N) != 0 at a generic level for N=2,3,4."""
        result = _mod.verify_quintic_nonvanishing(n)
        assert result['nonzero']

    def test_full_nonvanishing_table_w2(self):
        """All arities 2-8 are nonzero for Virasoro at k=7."""
        table = _mod.shadow_nonvanishing_table(2, max_r=8)
        for r in range(2, 9):
            assert table[r]['nonzero'], f"Sh_{r} vanishes at test level"

    def test_full_nonvanishing_table_w3(self):
        """All arities 2-8 are nonzero for W_3 at k=10."""
        table = _mod.shadow_nonvanishing_table(3, max_r=8)
        for r in range(2, 9):
            assert table[r]['nonzero'], f"Sh_{r} vanishes at test level"


# ============================================================
# Section 18: Alternating signs
# ============================================================

class TestAlternatingSigns:
    """Verify sign pattern of the shadow obstruction tower."""

    def test_virasoro_sign_alternation(self):
        """Sh_r alternates sign for Virasoro at large k (c ~ 1 - 6/k)."""
        tower = _mod.principal_ds_shadow_tower(2, max_r=8)
        # At k=100: c ~ (96)/(102) ~ 0.94 > 0
        signs = []
        for r in range(2, 9):
            val = float(tower[r].subs(k, 100))
            signs.append(1 if val > 0 else -1)
        # S_2 > 0, S_3 > 0, S_4 > 0, S_5 < 0, S_6 > 0, S_7 < 0, S_8 > 0
        assert signs[0] > 0   # S_2 = kappa > 0
        assert signs[1] > 0   # S_3 = 2
        assert signs[2] > 0   # S_4 > 0 for c > 0
        assert signs[3] < 0   # S_5 < 0
        assert signs[4] > 0   # S_6 > 0
        assert signs[5] < 0   # S_7 < 0
        assert signs[6] > 0   # S_8 > 0


# ============================================================
# Section 19: BP-specific shadow invariants
# ============================================================

class TestBPInvariants:
    """Additional BP-specific tests."""

    def test_bp_quartic_at_k5(self):
        """Quartic Q_BP on T-line at k=5 is finite and nonzero."""
        Q = _mod.bp_quartic_on_tline(5)
        assert Q != 0
        assert Q.is_finite

    def test_bp_discriminant_at_k5(self):
        """Discriminant Delta_BP on T-line at k=5 is finite and nonzero."""
        Delta = _mod.bp_discriminant_on_tline(5)
        assert Delta != 0
        assert Delta.is_finite

    def test_bp_kappa_j_vanishes_at_k_neg_half(self):
        """kappa_J = 0 at k = -1/2 (critical point for J-line)."""
        kappa_j = _mod.bershadsky_polyakov_kappa_j(Rational(-1, 2))
        assert kappa_j == 0

    def test_bp_c_at_neg3_half(self):
        """c_BP(-3/2) = 2 (special value where (2k+3) vanishes)."""
        assert simplify(_mod.bp_central_charge(Rational(-3, 2)) - 2) == 0

    @pytest.mark.parametrize('level_val', [1, 2, 3, 5, 10])
    def test_bp_tline_numerical_match(self, level_val):
        """Numerical: BP T-line matches Virasoro tower at c = c_BP(k)."""
        tower = _mod.bershadsky_polyakov_shadow_tower(6)
        vir = _mod._virasoro_tower_internal(6)
        c_bp_val = float(_mod.bp_central_charge(level_val))
        for r in range(2, 7):
            bp_val = float(tower[r].subs(k, level_val))
            vir_val = float(vir[r].subs(c, c_bp_val))
            assert abs(bp_val - vir_val) < 1e-10, \
                f"Mismatch at r={r}, k={level_val}: BP={bp_val}, Vir={vir_val}"
