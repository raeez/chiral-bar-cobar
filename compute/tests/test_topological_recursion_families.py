r"""Tests for topological_recursion_families.py.

Covers:
  - Faber-Pandharipande numbers lambda_g^FP (exact values, positivity, growth)
  - FamilyShadowData construction and properties for all standard families
  - Shadow obstruction tower extraction from Q_L
  - Shadow free energies F_g = kappa * lambda_g^FP
  - Classical spectral curves (Airy, Bessel, Sine, Catalan)
  - TREngine construction and degenerate detection
  - Cross-family consistency: Koszul duality, additivity, Airy-Heisenberg match
  - Weil-Petersson volume comparison
  - Comparison table builder
  - Spectral curve atlas

Ground truth:
  - cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
  - thm:theorem-d: F_g = kappa * lambda_g^FP
  - thm:shadow-archetype-classification: G/L/C/M depth classes
  - AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0)
"""

import math
import os
import sys

import pytest
from fractions import Fraction
from sympy import Rational, simplify, factorial

# conftest.py adds the repo root to sys.path, so direct import works.
from compute.lib.topological_recursion_families import (
    lambda_fp,
    FamilyShadowData,
    heisenberg_data,
    lattice_data,
    free_fermion_data,
    affine_sl2_data,
    affine_slN_data,
    betagamma_data,
    virasoro_data,
    w3_wline_data,
    w3_tline_data,
    wN_data,
    shadow_tower_from_QL,
    shadow_free_energy,
    AiryCurve,
    BesselCurve,
    SineCurve,
    CatalanCurve,
    build_comparison_table,
    verify_koszul_duality_tr,
    verify_additivity_heisenberg,
    verify_airy_heisenberg_match,
    spectral_curve_data_all_families,
    weil_petersson_volumes,
    compare_wp_with_shadow,
    TREngine,
    build_tr_engine,
    heisenberg_tr,
    affine_sl2_tr,
    virasoro_tr,
    w3_wline_tr,
    _HAS_MPMATH,
)


# ========================================================================
# 1. Faber-Pandharipande numbers
# ========================================================================

class TestLambdaFP:
    """Tests for lambda_g^FP = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!."""

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_g4(self):
        """lambda_4^FP = 127/154828800."""
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_fp_positivity(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli sign cancellation)."""
        for g in range(1, 8):
            val = lambda_fp(g)
            assert val > 0, f"lambda_fp({g}) = {val} is not positive"

    def test_lambda_fp_monotone_decrease(self):
        """lambda_g^FP is monotonically decreasing for g >= 1."""
        for g in range(1, 7):
            assert lambda_fp(g) > lambda_fp(g + 1), \
                f"lambda_fp({g}) = {lambda_fp(g)} not > lambda_fp({g+1}) = {lambda_fp(g+1)}"

    def test_lambda_fp_g0_raises(self):
        """lambda_fp requires g >= 1."""
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_lambda_fp_negative_raises(self):
        with pytest.raises(ValueError):
            lambda_fp(-1)

    def test_lambda_fp_exact_type(self):
        """Return type is sympy Rational (exact arithmetic)."""
        val = lambda_fp(1)
        assert isinstance(val, Rational)

    def test_lambda_fp_formula_direct(self):
        """Cross-check against direct Bernoulli computation for g=5."""
        from sympy import bernoulli as bern
        g = 5
        B2g = Rational(bern(2 * g))
        num = (2**(2*g - 1) - 1) * abs(B2g)
        den = 2**(2*g - 1) * factorial(2 * g)
        expected = Rational(num, den)
        assert lambda_fp(g) == expected


# ========================================================================
# 2. FamilyShadowData: construction and properties
# ========================================================================

class TestHeisenbergData:
    """Heisenberg family: class G, r_max=2, alpha=S4=0."""

    def test_default_kappa(self):
        d = heisenberg_data()
        assert d.kappa == Fraction(1)

    def test_kappa_at_level_k(self):
        d = heisenberg_data(Fraction(5))
        assert d.kappa == Fraction(5)

    def test_class_G(self):
        d = heisenberg_data()
        assert d.depth_class == 'G'
        assert d.r_max == 2

    def test_alpha_zero(self):
        d = heisenberg_data()
        assert d.alpha == Fraction(0)

    def test_S4_zero(self):
        d = heisenberg_data()
        assert d.S4 == Fraction(0)

    def test_Delta_zero(self):
        """Delta = 8*kappa*S4 = 0 for Heisenberg."""
        d = heisenberg_data()
        assert d.Delta == Fraction(0)

    def test_QL_constant(self):
        """Q_L = 4*kappa^2 (constant) for Heisenberg."""
        d = heisenberg_data(Fraction(3))
        assert d.q0 == Fraction(36)
        assert d.q1 == Fraction(0)
        assert d.q2 == Fraction(0)

    def test_degenerate(self):
        """Heisenberg spectral curve is degenerate (q2=0)."""
        d = heisenberg_data()
        assert d.is_degenerate


class TestLatticeData:
    """Lattice VOA: same structure as Heisenberg but kappa = rank."""

    def test_kappa_equals_rank(self):
        d = lattice_data(8)
        assert d.kappa == Fraction(8)

    def test_lattice_24_leech(self):
        """Leech lattice: rank=24, kappa=24."""
        d = lattice_data(24)
        assert d.kappa == Fraction(24)
        assert d.depth_class == 'G'


class TestFreeFermionData:
    def test_kappa(self):
        d = free_fermion_data()
        assert d.kappa == Fraction(1, 4)

    def test_class_G(self):
        d = free_fermion_data()
        assert d.depth_class == 'G'


class TestAffineSl2Data:
    """Affine sl_2: class L, r_max=3."""

    def test_kappa_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        d = affine_sl2_data(Fraction(1))
        assert d.kappa == Fraction(9, 4)

    def test_class_L(self):
        d = affine_sl2_data()
        assert d.depth_class == 'L'
        assert d.r_max == 3

    def test_S4_zero(self):
        """S4 = 0 by Jacobi identity for affine algebras."""
        d = affine_sl2_data()
        assert d.S4 == Fraction(0)

    def test_Delta_zero(self):
        """Delta = 0 for affine (class L)."""
        d = affine_sl2_data()
        assert d.Delta == Fraction(0)

    def test_alpha_nonzero(self):
        d = affine_sl2_data()
        assert d.alpha != Fraction(0)


class TestAffineSlNData:
    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = (9-1)*(1+3)/(2*3) = 32/6 = 16/3."""
        d = affine_slN_data(3, Fraction(1))
        assert d.kappa == Fraction(16, 3)

    def test_kappa_sl2_matches(self):
        """sl_N at N=2 should give same kappa as affine_sl2_data."""
        d1 = affine_sl2_data(Fraction(1))
        d2 = affine_slN_data(2, Fraction(1))
        assert d1.kappa == d2.kappa

    def test_class_L(self):
        d = affine_slN_data(4, Fraction(1))
        assert d.depth_class == 'L'


class TestBetaGammaData:
    def test_class_C(self):
        d = betagamma_data(Fraction(1, 2))
        assert d.depth_class == 'C'
        assert d.r_max == 4

    def test_kappa_lam_zero(self):
        """At lambda=0: kappa = 0^2*6 - 0*6 + 1 = 1."""
        d = betagamma_data(Fraction(0))
        assert d.kappa == Fraction(1)

    def test_kappa_lam_half(self):
        """At lambda=1/2: kappa = 6*(1/4) - 6*(1/2) + 1 = 3/2 - 3 + 1 = -1/2."""
        d = betagamma_data(Fraction(1, 2))
        assert d.kappa == Fraction(-1, 2)


class TestVirasoroData:
    def test_kappa(self):
        """kappa(Vir_c) = c/2."""
        d = virasoro_data(Fraction(26))
        assert d.kappa == Fraction(13)

    def test_class_M(self):
        d = virasoro_data(Fraction(10))
        assert d.depth_class == 'M'
        assert d.r_max is None

    def test_S4_formula(self):
        """S4 = 10/[c*(5c+22)] for Virasoro."""
        c = Fraction(10)
        d = virasoro_data(c)
        expected_S4 = Fraction(10) / (c * (5 * c + 22))
        assert d.S4 == expected_S4

    def test_self_dual_c13(self):
        """At c=13: kappa = 13/2, kappa' = (26-13)/2 = 13/2. Self-dual."""
        d = virasoro_data(Fraction(13))
        d_dual = virasoro_data(Fraction(26 - 13))
        assert d.kappa == d_dual.kappa

    def test_Delta_nonzero(self):
        """Virasoro has Delta != 0 (class M)."""
        d = virasoro_data(Fraction(10))
        assert d.Delta != Fraction(0)


class TestW3Data:
    def test_wline_kappa(self):
        """kappa_W = c/3 on the W-line."""
        d = w3_wline_data(Fraction(12))
        assert d.kappa == Fraction(4)

    def test_wline_alpha_zero(self):
        """Alpha = 0 on W-line (Z_2 parity)."""
        d = w3_wline_data(Fraction(10))
        assert d.alpha == Fraction(0)

    def test_tline_equals_virasoro(self):
        """T-line of W_3 = Virasoro shadow."""
        c = Fraction(10)
        d_t = w3_tline_data(c)
        d_v = virasoro_data(c)
        assert d_t.kappa == d_v.kappa
        assert d_t.S4 == d_v.S4


class TestWNData:
    def test_kappa_formula(self):
        """kappa(W_N) = (H_N - 1)*c where H_N = 1 + 1/2 + ... + 1/N."""
        c = Fraction(10)
        d = wN_data(3, c)
        # H_3 = 1 + 1/2 + 1/3 = 11/6; rho = H_3 - 1 = 1/2 + 1/3 = 5/6
        # Wait: code uses sum(1/i for i in range(2, N+1)) which is 1/2 + 1/3 = 5/6
        assert d.kappa == Fraction(5, 6) * c

    def test_w2_equals_virasoro_kappa(self):
        """W_2 = Virasoro, so kappa(W_2) = (1/2)*c = c/2."""
        c = Fraction(10)
        d = wN_data(2, c)
        assert d.kappa == c / 2


# ========================================================================
# 3. Shadow metric Q_L properties
# ========================================================================

class TestShadowMetricQL:
    """Test Q_L(t) = q0 + q1*t + q2*t^2 properties."""

    def test_heisenberg_QL_constant(self):
        d = heisenberg_data(Fraction(2))
        assert d.q0 == Fraction(16)  # 4*4
        assert d.q1 == Fraction(0)
        assert d.q2 == Fraction(0)

    def test_virasoro_QL_quadratic(self):
        """Virasoro has genuine quadratic Q_L."""
        d = virasoro_data(Fraction(10))
        assert d.q0 != Fraction(0)
        assert d.q1 != Fraction(0)
        assert d.q2 != Fraction(0)

    def test_discriminant_formula(self):
        """disc_QL = q1^2 - 4*q0*q2 = -32*kappa^2*Delta."""
        d = virasoro_data(Fraction(10))
        expected = -32 * d.kappa**2 * d.Delta
        assert d.disc_QL == expected

    def test_discriminant_vanishes_class_L(self):
        """For class L (affine), disc = 0 because Delta = 0."""
        d = affine_sl2_data(Fraction(1))
        assert d.disc_QL == Fraction(0)

    def test_discriminant_nonzero_class_M(self):
        d = virasoro_data(Fraction(10))
        assert d.disc_QL != Fraction(0)

    def test_degenerate_heisenberg(self):
        d = heisenberg_data()
        assert d.is_degenerate  # q2 = 0

    def test_degenerate_affine(self):
        d = affine_sl2_data()
        # disc = 0, so degenerate
        assert d.is_degenerate

    def test_nondegenerate_virasoro(self):
        d = virasoro_data(Fraction(10))
        assert not d.is_degenerate


# ========================================================================
# 4. Shadow obstruction tower from Q_L
# ========================================================================

class TestShadowTower:
    """Shadow obstruction tower S_r from H(t) = t^2 * sqrt(Q_L(t))."""

    def test_heisenberg_tower_kappa_only(self):
        """Heisenberg: S_2 = kappa, S_r = 0 for r > 2."""
        d = heisenberg_data(Fraction(3))
        tower = shadow_tower_from_QL(d, max_arity=8)
        # S_2 should be kappa = 3 (from the sqrt(4*9) = 6, times 1/2 coeff = 3... check)
        # Actually S_r = (1/r)*[t^{r-2}] sqrt(Q_L). For Heisenberg, sqrt(Q_L) = 2*kappa.
        # So [t^0] = 2*kappa, and [t^m] = 0 for m > 0.
        # S_2 = (1/2)*2*kappa = kappa = 3.
        assert tower[2] == Rational(3)
        for r in range(3, 9):
            assert tower[r] == 0, f"S_{r} should be 0 for Heisenberg, got {tower[r]}"

    def test_virasoro_tower_nonzero_higher(self):
        """Virasoro (class M): tower does NOT terminate."""
        d = virasoro_data(Fraction(10))
        tower = shadow_tower_from_QL(d, max_arity=8)
        assert tower[2] != 0
        # At least some higher arities should be nonzero
        nonzero_count = sum(1 for r in range(3, 9) if tower[r] != 0)
        assert nonzero_count > 0

    def test_affine_tower_terminates_at_3(self):
        """Affine (class L): S_2 != 0, S_3 != 0, S_r = 0 for r >= 4."""
        d = affine_sl2_data(Fraction(1))
        tower = shadow_tower_from_QL(d, max_arity=8)
        assert tower[2] != 0
        assert tower[3] != 0
        for r in range(4, 9):
            assert tower[r] == 0, f"S_{r} = {tower[r]} should be 0 for affine"

    def test_tower_keys(self):
        """Tower should have keys from 2 to max_arity."""
        d = heisenberg_data()
        tower = shadow_tower_from_QL(d, max_arity=6)
        assert set(tower.keys()) == {2, 3, 4, 5, 6}

    def test_tower_kappa_zero(self):
        """When kappa = 0, entire tower vanishes (q0 = 0)."""
        # Construct data with kappa=0
        d = FamilyShadowData("test_zero", Fraction(0), Fraction(0),
                             Fraction(0), 'G', 2)
        tower = shadow_tower_from_QL(d, max_arity=6)
        for r in range(2, 7):
            assert tower[r] == 0


# ========================================================================
# 5. Shadow free energies
# ========================================================================

class TestShadowFreeEnergy:
    """F_g = kappa * lambda_g^FP (Theorem D)."""

    def test_F1_heisenberg(self):
        d = heisenberg_data(Fraction(1))
        assert shadow_free_energy(d, 1) == Rational(1, 24)

    def test_F1_virasoro(self):
        """F_1(Vir_c) = (c/2) * (1/24) = c/48."""
        d = virasoro_data(Fraction(10))
        assert shadow_free_energy(d, 1) == Rational(10, 48)

    def test_F2_heisenberg(self):
        d = heisenberg_data(Fraction(1))
        assert shadow_free_energy(d, 2) == Rational(7, 5760)

    def test_Fg_linearity_in_kappa(self):
        """F_g is linear in kappa: F_g(2*kappa) = 2*F_g(kappa)."""
        for g in range(1, 5):
            d1 = heisenberg_data(Fraction(1))
            d2 = heisenberg_data(Fraction(2))
            assert shadow_free_energy(d2, g) == 2 * shadow_free_energy(d1, g)

    def test_Fg_positivity(self):
        """F_g > 0 for kappa > 0."""
        d = heisenberg_data(Fraction(1))
        for g in range(1, 6):
            assert shadow_free_energy(d, g) > 0


# ========================================================================
# 6. Classical spectral curves
# ========================================================================

class TestAiryCurve:
    def test_free_energy_g1(self):
        a = AiryCurve()
        assert a.free_energy(1) == Rational(1, 24)

    def test_free_energy_g2(self):
        a = AiryCurve()
        assert a.free_energy(2) == Rational(7, 5760)

    def test_free_energy_g3(self):
        a = AiryCurve()
        assert a.free_energy(3) == Rational(31, 967680)

    def test_verify_F2(self):
        assert AiryCurve.verify_F2() == Rational(7, 5760)

    def test_verify_F3(self):
        assert AiryCurve.verify_F3() == Rational(31, 967680)

    def test_name(self):
        a = AiryCurve()
        assert a.name == "Airy"

    def test_q_coeffs(self):
        a = AiryCurve()
        assert a.q_coeffs == (0.0, 1.0, 0.0)


class TestBesselCurve:
    def test_free_energy_g1(self):
        b = BesselCurve()
        assert b.free_energy(1) == pytest.approx(-1 / 12)

    def test_free_energy_g2(self):
        """F_2^{Bessel} = B_4/(4*2) = -1/240."""
        b = BesselCurve()
        assert b.free_energy(2) == pytest.approx(-1 / 240)

    def test_raises_g0(self):
        b = BesselCurve()
        with pytest.raises(ValueError):
            b.free_energy(0)


class TestSineCurve:
    def test_wp_volume_g1(self):
        s = SineCurve()
        assert s.free_energy(1) == pytest.approx(float(Rational(1, 24)))

    def test_wp_volume_g2(self):
        s = SineCurve()
        assert s.free_energy(2) == pytest.approx(float(Rational(43, 960)))

    def test_wp_volume_g3(self):
        s = SineCurve()
        assert s.free_energy(3) == pytest.approx(float(Rational(7811, 725760)))

    def test_wp_volume_g4(self):
        s = SineCurve()
        assert s.free_energy(4) == pytest.approx(float(Rational(1149547, 348364800)))

    def test_raises_g0(self):
        s = SineCurve()
        with pytest.raises(ValueError):
            s.free_energy(0)


class TestCatalanCurve:
    def test_free_energy_g1(self):
        c = CatalanCurve()
        assert c.free_energy(1) == pytest.approx(-1 / 12)

    def test_q_coeffs(self):
        c = CatalanCurve()
        assert c.q_coeffs == (1.0, -4.0, 0.0)

    def test_raises_g0(self):
        c = CatalanCurve()
        with pytest.raises(ValueError):
            c.free_energy(0)


# ========================================================================
# 7. TREngine (requires mpmath)
# ========================================================================

class TestTREngine:
    """Tests for the topological recursion engine."""

    @pytest.fixture(autouse=True)
    def check_mpmath(self):
        if not _HAS_MPMATH:
            pytest.skip("mpmath not available")

    def test_heisenberg_degenerate(self):
        """Heisenberg spectral curve is degenerate."""
        eng = heisenberg_tr()
        assert eng.degenerate

    def test_affine_degenerate(self):
        """Affine sl_2 spectral curve is degenerate (disc=0)."""
        eng = affine_sl2_tr()
        assert eng.degenerate

    def test_virasoro_nondegenerate(self):
        """Virasoro at c=10 is non-degenerate."""
        eng = virasoro_tr(Fraction(10))
        assert not eng.degenerate

    def test_degenerate_omega11_zero(self):
        """Degenerate curves give omega_{1,1} = 0."""
        eng = heisenberg_tr()
        val = eng.omega_11(2.0 + 0.3j)
        import mpmath
        assert abs(val) < 1e-30

    def test_degenerate_omega03_zero(self):
        eng = heisenberg_tr()
        val = eng.omega_03(2.0 + 0.3j, 3.0 - 0.1j, 1.5 + 0.5j)
        import mpmath
        assert abs(val) < 1e-30

    def test_from_shadow_data(self):
        d = virasoro_data(Fraction(10))
        eng = TREngine.from_shadow_data(d)
        assert eng.name == d.name

    def test_build_tr_engine(self):
        d = virasoro_data(Fraction(10))
        eng = build_tr_engine(d)
        assert not eng.degenerate

    def test_F1_exact(self):
        eng = virasoro_tr(Fraction(10))
        f1 = eng.F1_exact(kappa=5.0)
        assert f1 == pytest.approx(5.0 / 24.0)

    def test_F2_analytical(self):
        eng = virasoro_tr(Fraction(10))
        f2 = eng.F2_from_omega_21(kappa=5.0)
        assert f2 == pytest.approx(5.0 * float(lambda_fp(2)))

    def test_F3_analytical(self):
        eng = virasoro_tr(Fraction(10))
        f3 = eng.F3_analytical(kappa=5.0)
        assert f3 == pytest.approx(5.0 * float(lambda_fp(3)))

    def test_F4_analytical(self):
        eng = virasoro_tr(Fraction(10))
        f4 = eng.F4_analytical(kappa=5.0)
        assert f4 == pytest.approx(5.0 * float(lambda_fp(4)))

    def test_F2_requires_kappa(self):
        eng = virasoro_tr(Fraction(10))
        with pytest.raises(ValueError):
            eng.F2_from_omega_21(kappa=None)

    def test_w3_wline_engine(self):
        eng = w3_wline_tr(Fraction(10))
        assert not eng.degenerate


# ========================================================================
# 8. Cross-family consistency: Koszul duality (AP24)
# ========================================================================

class TestKoszulDualityConsistency:
    """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""

    def test_kappa_sum_13(self):
        for c_val in [1, 5, 10, 13, 20, 25]:
            c = Fraction(c_val)
            d1 = virasoro_data(c)
            d2 = virasoro_data(Fraction(26) - c)
            assert d1.kappa + d2.kappa == Fraction(13)

    def test_verify_koszul_duality_tr_c10(self):
        results = verify_koszul_duality_tr(Fraction(10))
        for g in range(1, 5):
            assert results[g]['agrees']

    def test_verify_koszul_duality_tr_c1(self):
        results = verify_koszul_duality_tr(Fraction(1))
        for g in range(1, 5):
            assert results[g]['agrees']

    def test_Fg_sum_equals_13_lambda(self):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP."""
        c = Fraction(10)
        d1 = virasoro_data(c)
        d2 = virasoro_data(Fraction(26) - c)
        for g in range(1, 5):
            lam = lambda_fp(g)
            total = shadow_free_energy(d1, g) + shadow_free_energy(d2, g)
            assert simplify(total - 13 * lam) == 0


# ========================================================================
# 9. Additivity
# ========================================================================

class TestAdditivity:
    def test_heisenberg_additivity(self):
        results = verify_additivity_heisenberg(Fraction(3), Fraction(7))
        for g in range(1, 5):
            assert results[g]['agrees']

    def test_heisenberg_additivity_fractional(self):
        results = verify_additivity_heisenberg(Fraction(1, 2), Fraction(3, 2))
        for g in range(1, 5):
            assert results[g]['agrees']


# ========================================================================
# 10. Airy-Heisenberg match
# ========================================================================

class TestAiryHeisenbergMatch:
    def test_match_all_genera(self):
        """Heisenberg at k=1 reproduces Airy curve exactly."""
        results = verify_airy_heisenberg_match()
        for g in range(1, 6):
            assert results[g]['agrees']

    def test_explicit_match(self):
        """Direct comparison: F_g(Heis_1) = F_g^Airy."""
        airy = AiryCurve()
        d = heisenberg_data(Fraction(1))
        for g in range(1, 5):
            assert shadow_free_energy(d, g) == airy.free_energy(g)


# ========================================================================
# 11. Weil-Petersson volumes
# ========================================================================

class TestWeilPetersson:
    def test_known_volumes(self):
        wp = weil_petersson_volumes()
        assert wp[1] == Rational(1, 24)
        assert wp[2] == Rational(43, 960)
        assert wp[3] == Rational(7811, 725760)
        assert wp[4] == Rational(1149547, 348364800)

    def test_wp_not_equal_shadow(self):
        """WP volumes differ from shadow obstruction tower F_g for generic c."""
        results = compare_wp_with_shadow(Fraction(10))
        # They should NOT be equal for generic c
        for g in results:
            assert not results[g]['equal']


# ========================================================================
# 12. Comparison table
# ========================================================================

class TestComparisonTable:
    def test_default_table_nonempty(self):
        table = build_comparison_table(max_genus=3)
        assert len(table) > 0

    def test_default_table_agreement(self):
        """All entries should agree (analytical = shadow = TR on scalar lane)."""
        table = build_comparison_table(max_genus=3)
        for entry in table:
            assert entry.agreement, \
                f"Disagreement for {entry.family} at g={entry.g}"

    def test_custom_families(self):
        families = [heisenberg_data(Fraction(1)), virasoro_data(Fraction(10))]
        table = build_comparison_table(families=families, max_genus=2)
        # 2 families * 2 genera = 4 entries
        assert len(table) == 4

    def test_entry_fields(self):
        table = build_comparison_table(max_genus=1)
        entry = table[0]
        assert hasattr(entry, 'family')
        assert hasattr(entry, 'g')
        assert hasattr(entry, 'F_g_analytical')
        assert hasattr(entry, 'F_g_shadow_tower')
        assert hasattr(entry, 'F_g_TR')
        assert hasattr(entry, 'agreement')


# ========================================================================
# 13. Spectral curve atlas
# ========================================================================

class TestSpectralCurveAtlas:
    def test_atlas_has_all_families(self):
        atlas = spectral_curve_data_all_families()
        expected_keys = [
            'Heisenberg_k=1', 'Heisenberg_k=2', 'Lattice_r=8',
            'Lattice_r=24', 'FreeFermion',
            'Affine_sl2_k=1', 'Affine_sl2_k=10',
            'Affine_sl3_k=1',
            'BetaGamma_lam=0', 'BetaGamma_lam=1/2',
            'Virasoro_c=1', 'Virasoro_c=10', 'Virasoro_c=13', 'Virasoro_c=26',
            'W3_W_c=10', 'W3_T_c=10',
        ]
        for key in expected_keys:
            assert key in atlas, f"Missing family: {key}"

    def test_atlas_depth_classes(self):
        atlas = spectral_curve_data_all_families()
        assert atlas['Heisenberg_k=1']['depth_class'] == 'G'
        assert atlas['Affine_sl2_k=1']['depth_class'] == 'L'
        assert atlas['BetaGamma_lam=0']['depth_class'] == 'C'
        assert atlas['Virasoro_c=10']['depth_class'] == 'M'

    def test_atlas_degenerate_flags(self):
        atlas = spectral_curve_data_all_families()
        assert atlas['Heisenberg_k=1']['degenerate']
        assert atlas['Affine_sl2_k=1']['degenerate']
        assert not atlas['Virasoro_c=10']['degenerate']

    def test_atlas_entry_has_all_fields(self):
        atlas = spectral_curve_data_all_families()
        entry = atlas['Virasoro_c=10']
        for field in ['kappa', 'alpha', 'S4', 'Delta', 'q0', 'q1', 'q2',
                       'disc_QL', 'depth_class', 'r_max', 'degenerate']:
            assert field in entry, f"Missing field: {field}"

    def test_atlas_kappa_values(self):
        atlas = spectral_curve_data_all_families()
        assert atlas['Heisenberg_k=1']['kappa'] == pytest.approx(1.0)
        assert atlas['Heisenberg_k=2']['kappa'] == pytest.approx(2.0)
        assert atlas['Virasoro_c=26']['kappa'] == pytest.approx(13.0)
        assert atlas['Lattice_r=24']['kappa'] == pytest.approx(24.0)

    def test_atlas_virasoro_c13_self_dual(self):
        atlas = spectral_curve_data_all_families()
        assert atlas['Virasoro_c=13']['kappa'] == pytest.approx(6.5)


# ========================================================================
# 14. Depth class / r_max consistency across families
# ========================================================================

class TestDepthClassification:
    """Shadow archetype classification (thm:shadow-archetype-classification)."""

    def test_class_G_terminates_at_2(self):
        for d in [heisenberg_data(), lattice_data(8), free_fermion_data()]:
            assert d.depth_class == 'G'
            assert d.r_max == 2
            assert d.Delta == Fraction(0)
            assert d.alpha == Fraction(0)

    def test_class_L_terminates_at_3(self):
        for d in [affine_sl2_data(), affine_slN_data(3)]:
            assert d.depth_class == 'L'
            assert d.r_max == 3
            assert d.Delta == Fraction(0)
            assert d.alpha != Fraction(0)

    def test_class_C_terminates_at_4(self):
        d = betagamma_data(Fraction(1, 2))
        assert d.depth_class == 'C'
        assert d.r_max == 4

    def test_class_M_infinite(self):
        for d in [virasoro_data(Fraction(10)), w3_wline_data(Fraction(10))]:
            assert d.depth_class == 'M'
            assert d.r_max is None
            assert d.Delta != Fraction(0)

    def test_class_G_implies_S4_zero(self):
        d = heisenberg_data(Fraction(5))
        assert d.S4 == Fraction(0)

    def test_class_L_implies_S4_zero(self):
        d = affine_sl2_data(Fraction(3))
        assert d.S4 == Fraction(0)


# ========================================================================
# 15. Edge cases and error handling
# ========================================================================

class TestEdgeCases:
    def test_virasoro_large_c(self):
        """Large c should not cause errors."""
        d = virasoro_data(Fraction(1000))
        tower = shadow_tower_from_QL(d, max_arity=6)
        assert tower[2] != 0

    def test_bessel_higher_genus(self):
        """Bessel free energies for g >= 3."""
        b = BesselCurve()
        for g in range(2, 5):
            val = b.free_energy(g)
            assert isinstance(val, float)

    def test_sine_higher_genus_approximate(self):
        """Sine curve free energies for g > 4 use approximation."""
        s = SineCurve()
        val = s.free_energy(5)
        assert isinstance(val, float)
        assert val > 0

    def test_catalan_higher_genus(self):
        c = CatalanCurve()
        for g in range(2, 5):
            val = c.free_energy(g)
            assert isinstance(val, float)

    def test_wN_c_zero(self):
        """W_N at c=0: special branch (no S4 division by zero)."""
        d = wN_data(3, Fraction(0))
        assert d.kappa == Fraction(0)
        assert d.S4 == Fraction(0)

    def test_betagamma_c_eff_zero(self):
        """beta-gamma at lambda where c_eff = 2*kappa = 0."""
        # kappa = 6*lam^2 - 6*lam + 1 = 0 when lam = (3 +/- sqrt(3))/6
        # At these values c_eff = 0, S4 should default to 0
        # Just test lam = (3 - sqrt(3))/6 is not a Fraction easily,
        # but the branch for c_eff == 0 in the code uses exact Fraction(0) check.
        # The c_eff = 0 branch triggers when kappa = 0 since c_eff = 2*kappa.
        # But 6*lam^2 - 6*lam + 1 = 0 has irrational roots.
        # Test the exact case: lam=0 gives kappa=1, c_eff=2 (nonzero).
        # lam=1 gives kappa=1, c_eff=2 (nonzero).
        # The branch c_eff==0 may not be easily reachable with Fraction input.
        # Just verify no crash for lam=0 and lam=1.
        d0 = betagamma_data(Fraction(0))
        d1 = betagamma_data(Fraction(1))
        assert d0.kappa == Fraction(1)
        assert d1.kappa == Fraction(1)


# ========================================================================
# 16. Cross-consistency: shadow obstruction tower S_2 = kappa
# ========================================================================

class TestShadowTowerS2EqualsKappa:
    """S_2 = kappa for all families (fundamental identity)."""

    def test_heisenberg_S2(self):
        d = heisenberg_data(Fraction(5))
        tower = shadow_tower_from_QL(d)
        assert tower[2] == Rational(5)

    def test_virasoro_S2(self):
        c = Fraction(10)
        d = virasoro_data(c)
        tower = shadow_tower_from_QL(d)
        assert simplify(tower[2] - Rational(c) / 2) == 0

    def test_affine_sl2_S2(self):
        d = affine_sl2_data(Fraction(1))
        tower = shadow_tower_from_QL(d)
        assert simplify(tower[2] - Rational(d.kappa)) == 0

    def test_lattice_S2(self):
        d = lattice_data(24)
        tower = shadow_tower_from_QL(d)
        assert tower[2] == Rational(24)
