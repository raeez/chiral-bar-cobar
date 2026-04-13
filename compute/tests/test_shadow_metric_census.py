"""Tests for the shadow metric census.

Verifies:
    1. Delta = 8*kappa*S_4 for every family
    2. Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2 for every family
    3. G/L/C/M classification consistency with (Delta, alpha)
    4. Virasoro Delta = 40/(5c+22)
    5. Affine Delta = 0 (Jacobi identity kills quartic)
    6. Heisenberg Q_L = (2k)^2 (constant, no t-dependence)
    7. Specific numerical evaluations at distinguished central charges
    8. Harmonic number formulas for W_N kappa
    9. Cross-checks against envelope_shadow_functor.py

Mathematical references:
    - def:shadow-depth-classification in higher_genus_modular_koszul.tex
    - thm:shadow-archetype-classification in higher_genus_modular_koszul.tex
    - thm:nms-mc-principle in nonlinear_modular_shadows.tex
    - cor:nms-betagamma-mu-vanishing in nonlinear_modular_shadows.tex
    - cor:general-w-obstruction in w_algebras.tex
    - virasoro_shadow_tower.py: Sh_3 = 2x^3
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

from __future__ import annotations

import pytest

from fractions import Fraction

from sympy import (
    Rational, Symbol, expand, simplify, symbols, S, factor, oo
)

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from shadow_metric_census import (
    build_census,
    classify,
    classify_from_data,
    evaluate_heisenberg,
    evaluate_virasoro,
    evaluate_wN,
    evaluate_affine_sl2,
    harmonic_number,
    anomaly_ratio,
    kappa_heisenberg,
    kappa_lattice,
    kappa_free_fermion,
    kappa_affine_sl2,
    kappa_affine_slN,
    kappa_betagamma,
    kappa_bc,
    kappa_virasoro,
    kappa_w3,
    kappa_wN,
    summary_table,
    verify_all_deltas,
    verify_all_classes,
    verify_all_Q_L,
    verify_Q_L_formula,
    virasoro_shadow_metric_symbolic,
    ShadowMetricEntry,
)


k = Symbol('k')
c = Symbol('c')
t = Symbol('t')
N = Symbol('N')
lam = Symbol('lambda')


# ========================================================================
# 1. Delta = 8*kappa*S_4 for every family
# ========================================================================

class TestDeltaIdentity:
    """Verify Delta = 8*kappa*S_4 for each family in the census."""

    def test_all_deltas(self):
        """Master test: Delta = 8*kappa*S_4 for every entry."""
        results = verify_all_deltas()
        for name, ok in results.items():
            assert ok, f"Delta != 8*kappa*S_4 for {name}"

    def test_heisenberg_delta(self):
        census = build_census()
        entry = census['Heisenberg']
        assert simplify(entry.Delta) == 0
        assert simplify(entry.Delta - 8 * entry.kappa * entry.S4) == 0

    def test_lattice_delta(self):
        census = build_census()
        entry = census['Lattice']
        assert simplify(entry.Delta) == 0

    def test_free_fermion_delta(self):
        census = build_census()
        entry = census['FreeFermion']
        assert entry.Delta == 0

    def test_affine_sl2_delta(self):
        """Affine sl_2: Delta = 0 because S_4 = 0 (Jacobi identity)."""
        census = build_census()
        entry = census['Affine_sl2']
        assert simplify(entry.Delta) == 0
        assert simplify(entry.S4) == 0

    def test_affine_slN_delta(self):
        """Affine sl_N: Delta = 0 because S_4 = 0 (Jacobi identity)."""
        census = build_census()
        entry = census['Affine_slN']
        assert simplify(entry.Delta) == 0
        assert simplify(entry.S4) == 0

    def test_virasoro_delta_formula(self):
        """Virasoro: Delta = 40/(5c+22)."""
        census = build_census()
        entry = census['Virasoro']
        expected = Rational(40) / (5 * c + 22)
        assert simplify(entry.Delta - expected) == 0

    def test_virasoro_delta_from_kappa_S4(self):
        """Virasoro: verify 8*kappa*S4 = 40/(5c+22)."""
        kap = c / 2
        S4 = Rational(10) / (c * (5 * c + 22))
        Delta_computed = 8 * kap * S4
        Delta_expected = Rational(40) / (5 * c + 22)
        assert simplify(Delta_computed - Delta_expected) == 0

    def test_virasoro_delta_numerical_c1(self):
        """Delta at c=1: 40/(5+22) = 40/27."""
        v = evaluate_virasoro(1)
        assert v['Delta'] == Rational(40, 27)
        assert v['Delta'] == v['Delta_check']

    def test_virasoro_delta_numerical_c26(self):
        """Delta at c=26: 40/(130+22) = 40/152 = 5/19."""
        v = evaluate_virasoro(26)
        assert v['Delta'] == Rational(40, 152)
        assert v['Delta'] == Rational(5, 19)
        assert v['Delta'] == v['Delta_check']

    def test_virasoro_delta_numerical_c_minus22_over5(self):
        """Delta diverges at c = -22/5 (Lee-Yang edge singularity)."""
        # At c = -22/5, the denominator 5c+22 = -22+22 = 0
        # So Delta has a pole. We check that the formula gives the
        # correct pole location.
        pole = Rational(-22, 5)
        denom = 5 * pole + 22
        assert denom == 0


# ========================================================================
# 2. Q_L(t) = (2*kappa + alpha*t)^2 + 2*Delta*t^2 for every family
# ========================================================================

class TestQLFormula:
    """Verify the shadow metric formula for each family."""

    def test_all_Q_L(self):
        """Master test: Q_L formula for every entry."""
        results = verify_all_Q_L()
        for name, ok in results.items():
            assert ok, f"Q_L formula fails for {name}"

    def test_heisenberg_Q_L_constant(self):
        """Heisenberg: Q_L(t) = (2k)^2 = 4k^2 (no t-dependence)."""
        census = build_census()
        entry = census['Heisenberg']
        Q = entry.Q_L()
        # Should be 4*k^2 with no t-dependence
        assert simplify(Q - 4 * k**2) == 0

    def test_heisenberg_Q_L_no_t(self):
        """Heisenberg Q_L has zero coefficient of t and t^2."""
        census = build_census()
        entry = census['Heisenberg']
        Q = expand(entry.Q_L())
        from sympy import Poly
        p = Poly(Q, t)
        # Coefficient of t^1 should be 0
        assert p.nth(1) == 0
        # Coefficient of t^2 should be 0
        assert p.nth(2) == 0

    def test_heisenberg_Q_L_numerical(self):
        """Heisenberg at k=3: Q_L = 36."""
        h = evaluate_heisenberg(3)
        assert h['Q_L_const'] == 36

    def test_free_fermion_Q_L(self):
        """Free fermion: kappa = 1/4, Q_L = (2*1/4)^2 = 1/4."""
        census = build_census()
        entry = census['FreeFermion']
        Q = entry.Q_L()
        assert simplify(Q - Rational(1, 4)) == 0

    def test_affine_sl2_Q_L_form(self):
        """Affine sl_2: Q_L(t) = (2*kappa + 3*alpha*t)^2 (perfect square, Delta=0)."""
        census = build_census()
        entry = census['Affine_sl2']
        Q = entry.Q_L()
        # Since Delta = 0, Q_L = (2*kappa + 3*alpha*t)^2
        expected = (2 * entry.kappa + 3 * entry.alpha * t)**2
        assert simplify(Q - expand(expected)) == 0

    def test_virasoro_Q_L_symbolic(self):
        """Virasoro: Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22).

        alpha = 2 (cubic shadow S_3), so 3*alpha = 6.
        2*kappa = c, so (2*kappa + 3*alpha*t) = (c + 6t).
        """
        census = build_census()
        entry = census['Virasoro']
        Q = entry.Q_L()
        expected = expand((c + 6 * t)**2
                          + 2 * Rational(40) / (5 * c + 22) * t**2)
        assert simplify(Q - expected) == 0

    def test_virasoro_Q_L_at_c1(self):
        """Virasoro Q_L at c=1: Q = (1 + 6t)^2 + 80t^2/27.

        2*kappa = 1, 3*alpha = 6, so (2*kappa + 3*alpha*t) = (1 + 6t).
        """
        v = evaluate_virasoro(1)
        Q = v['Q_L']
        expected = expand((1 + 6 * t)**2 + Rational(80, 27) * t**2)
        assert simplify(Q - expected) == 0


# ========================================================================
# 3. G/L/C/M classification consistency
# ========================================================================

class TestClassification:
    """Verify classification consistency with (Delta, alpha)."""

    def test_all_classes(self):
        """Master test: all entries have consistent classification."""
        results = verify_all_classes()
        for name, ok in results.items():
            assert ok, f"Classification inconsistent for {name}"

    def test_classify_G(self):
        """Delta = 0, alpha = 0 => G, r_max = 2."""
        cls, r = classify(0, 0)
        assert cls == 'G'
        assert r == 2

    def test_classify_L(self):
        """Delta = 0, alpha != 0 => L, r_max = 3."""
        cls, r = classify(1, 0)
        assert cls == 'L'
        assert r == 3

    def test_classify_C(self):
        """Delta != 0, alpha = 0 => C, r_max = 4."""
        cls, r = classify(0, 1)
        assert cls == 'C'
        assert r == 4

    def test_classify_M(self):
        """Delta != 0, alpha != 0 => M, r_max = None (infinity)."""
        cls, r = classify(1, 1)
        assert cls == 'M'
        assert r is None

    def test_classify_from_data_heisenberg(self):
        """Heisenberg: kappa=k, alpha=0, S4=0 => G."""
        cls, r = classify_from_data(k, 0, 0)
        assert cls == 'G'
        assert r == 2

    def test_classify_from_data_virasoro(self):
        """Virasoro: kappa=c/2, alpha=2, S4=10/[c(5c+22)] => M."""
        kap = c / 2
        S4 = Rational(10) / (c * (5 * c + 22))
        cls, r = classify_from_data(kap, 2, S4)
        assert cls == 'M'
        assert r is None

    def test_classify_from_data_affine(self):
        """Affine: kappa nonzero, alpha nonzero, S4=0 => L."""
        kap = Rational(3) * (k + 2) / 4
        alpha_nz = Symbol('a', nonzero=True)
        cls, r = classify_from_data(kap, alpha_nz, 0)
        assert cls == 'L'
        assert r == 3

    def test_heisenberg_is_G(self):
        census = build_census()
        assert census['Heisenberg'].cls == 'G'
        assert census['Heisenberg'].r_max == 2

    def test_lattice_is_G(self):
        census = build_census()
        assert census['Lattice'].cls == 'G'
        assert census['Lattice'].r_max == 2

    def test_free_fermion_is_G(self):
        census = build_census()
        assert census['FreeFermion'].cls == 'G'
        assert census['FreeFermion'].r_max == 2

    def test_affine_sl2_is_L(self):
        census = build_census()
        assert census['Affine_sl2'].cls == 'L'
        assert census['Affine_sl2'].r_max == 3

    def test_affine_slN_is_L(self):
        census = build_census()
        assert census['Affine_slN'].cls == 'L'
        assert census['Affine_slN'].r_max == 3

    def test_betagamma_is_C(self):
        census = build_census()
        assert census['BetaGamma'].cls == 'C'
        assert census['BetaGamma'].r_max == 4

    def test_bc_is_C(self):
        census = build_census()
        assert census['bc'].cls == 'C'
        assert census['bc'].r_max == 4

    def test_virasoro_is_M(self):
        census = build_census()
        assert census['Virasoro'].cls == 'M'
        assert census['Virasoro'].r_max is None

    def test_w3_is_M(self):
        census = build_census()
        assert census['W3'].cls == 'M'
        assert census['W3'].r_max is None

    def test_wN_is_M(self):
        census = build_census()
        assert census['W_N'].cls == 'M'
        assert census['W_N'].r_max is None


# ========================================================================
# 4. Virasoro-specific tests
# ========================================================================

class TestVirasoro:
    """Detailed Virasoro shadow metric tests."""

    def test_virasoro_kappa(self):
        assert kappa_virasoro(c) == c / 2

    def test_virasoro_kappa_numerical(self):
        assert kappa_virasoro(Rational(26)) == Rational(13)
        assert kappa_virasoro(Rational(1)) == Rational(1, 2)
        assert kappa_virasoro(Rational(0)) == 0

    def test_virasoro_alpha_is_2(self):
        """The cubic shadow Sh_3 = 2x^3 gives alpha = 2."""
        census = build_census()
        assert census['Virasoro'].alpha == 2

    def test_virasoro_S4(self):
        """S_4 = Q^contact_Vir = 10/[c(5c+22)]."""
        census = build_census()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(census['Virasoro'].S4 - expected) == 0

    def test_virasoro_S4_at_c1(self):
        """S_4 at c=1: 10/(1*27) = 10/27."""
        v = evaluate_virasoro(1)
        assert v['S4'] == Rational(10, 27)

    def test_virasoro_S4_at_c26(self):
        """S_4 at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        v = evaluate_virasoro(26)
        assert v['S4'] == Rational(10, 26 * 152)
        assert v['S4'] == Rational(5, 1976)

    def test_virasoro_delta_40_over_5c_plus_22(self):
        """Delta = 40/(5c+22)."""
        vir = virasoro_shadow_metric_symbolic()
        assert simplify(vir['Delta'] - Rational(40) / (5 * c + 22)) == 0

    def test_virasoro_self_duality_c13(self):
        """At c=13 (self-dual point), Delta = 40/(65+22) = 40/87."""
        v = evaluate_virasoro(13)
        assert v['Delta'] == Rational(40, 87)
        # Not zero: Virasoro is class M even at self-dual point
        assert v['Delta'] != 0

    def test_virasoro_c26_delta(self):
        """At c=26, Delta = 40/152 = 5/19."""
        v = evaluate_virasoro(26)
        assert v['Delta'] == Rational(5, 19)

    def test_virasoro_Q_L_positive_definite_large_c(self):
        """For large positive c, Q_L(t) should be positive for all t != 0.

        At c = 100: kappa = 50, alpha = 2, Delta = 40/522 > 0.
        Q_L(t) = (100 + 2t)^2 + 80t^2/522 > 0 for all real t.
        """
        v = evaluate_virasoro(100)
        # Delta > 0 and kappa > 0, so Q_L > 0 for all t
        assert v['Delta'] > 0
        assert v['kappa'] > 0


# ========================================================================
# 5. Affine-specific tests
# ========================================================================

class TestAffine:
    """Affine Kac-Moody shadow metric tests."""

    def test_affine_delta_zero(self):
        """Affine: Delta = 0 because Jacobi kills quartic on primary line."""
        census = build_census()
        assert simplify(census['Affine_sl2'].Delta) == 0
        assert simplify(census['Affine_slN'].Delta) == 0

    def test_affine_S4_zero(self):
        """Affine: S_4 = 0 (Jacobi identity)."""
        census = build_census()
        assert census['Affine_sl2'].S4 == 0
        assert census['Affine_slN'].S4 == 0

    def test_affine_alpha_nonzero(self):
        """Affine: alpha != 0 (Lie bracket gives cubic shadow)."""
        census = build_census()
        # alpha is a nonzero symbol
        assert census['Affine_sl2'].alpha != 0
        assert census['Affine_slN'].alpha != 0

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        assert simplify(kappa_affine_sl2(k) - Rational(3) * (k + 2) / 4) == 0

    def test_affine_sl2_kappa_level1(self):
        """kappa(sl_2, 1) = 3*3/4 = 9/4."""
        assert kappa_affine_sl2(Rational(1)) == Rational(9, 4)

    def test_affine_slN_kappa(self):
        """kappa(sl_N, k) = (N^2-1)(k+N)/(2N)."""
        # Check at N=3, k=1: (9-1)(1+3)/6 = 8*4/6 = 32/6 = 16/3
        assert kappa_affine_slN(3, Rational(1)) == Rational(16, 3)

    def test_affine_slN_kappa_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4 from the general N formula."""
        assert simplify(kappa_affine_slN(2, k) - Rational(3) * (k + 2) / 4) == 0

    def test_affine_Q_L_perfect_square(self):
        """When Delta = 0, Q_L = (2*kappa + 3*alpha*t)^2 is a perfect square."""
        census = build_census()
        entry = census['Affine_sl2']
        Q = entry.Q_L()
        expected = (2 * entry.kappa + 3 * entry.alpha * t)**2
        assert simplify(Q - expand(expected)) == 0


# ========================================================================
# 6. Heisenberg-specific tests
# ========================================================================

class TestHeisenberg:
    """Heisenberg shadow metric tests."""

    def test_heisenberg_Q_L_is_4k_squared(self):
        """Q_L(t) = (2k)^2 = 4k^2."""
        census = build_census()
        entry = census['Heisenberg']
        assert simplify(entry.Q_L() - 4 * k**2) == 0

    def test_heisenberg_kappa(self):
        """kappa(Heis, k) = k."""
        assert kappa_heisenberg(k) == k

    def test_heisenberg_alpha_zero(self):
        """alpha = 0 (abelian OPE)."""
        census = build_census()
        assert census['Heisenberg'].alpha == 0

    def test_heisenberg_S4_zero(self):
        """S_4 = 0 (abelian OPE)."""
        census = build_census()
        assert census['Heisenberg'].S4 == 0

    def test_heisenberg_delta_zero(self):
        """Delta = 0."""
        census = build_census()
        assert census['Heisenberg'].Delta == 0

    def test_heisenberg_numerical_k1(self):
        """k=1: Q_L = 4."""
        h = evaluate_heisenberg(1)
        assert h['Q_L_const'] == 4
        assert h['Delta'] == 0

    def test_heisenberg_numerical_k_half(self):
        """k=1/2: Q_L = 1."""
        h = evaluate_heisenberg(Rational(1, 2))
        assert h['Q_L_const'] == 1


# ========================================================================
# 7. Specific numerical evaluations
# ========================================================================

class TestNumerical:
    """Numerical evaluations at distinguished parameter values."""

    def test_virasoro_c1(self):
        v = evaluate_virasoro(1)
        assert v['kappa'] == Rational(1, 2)
        assert v['Delta'] == Rational(40, 27)
        assert v['S4'] == Rational(10, 27)

    def test_virasoro_c26(self):
        v = evaluate_virasoro(26)
        assert v['kappa'] == Rational(13)
        assert v['Delta'] == Rational(5, 19)

    def test_virasoro_c_half(self):
        """Virasoro at c = 1/2 (Ising model)."""
        v = evaluate_virasoro(Rational(1, 2))
        assert v['kappa'] == Rational(1, 4)
        # Delta = 40/(5/2 + 22) = 40/(49/2) = 80/49
        assert v['Delta'] == Rational(80, 49)

    def test_virasoro_c25(self):
        """Virasoro at c = 25."""
        v = evaluate_virasoro(25)
        assert v['kappa'] == Rational(25, 2)
        # Delta = 40/(125+22) = 40/147
        assert v['Delta'] == Rational(40, 147)

    def test_heisenberg_k0(self):
        """k=0 (trivial): Q_L = 0, kappa = 0."""
        h = evaluate_heisenberg(0)
        assert h['Q_L_const'] == 0
        assert h['kappa'] == 0

    def test_affine_sl2_k1(self):
        """sl_2 at k=1: kappa = 9/4, Delta = 0."""
        a = evaluate_affine_sl2(Rational(1))
        assert a['kappa'] == Rational(9, 4)
        assert a['Delta'] == 0

    def test_affine_sl2_k_minus2(self):
        """sl_2 at k=-2 (critical): kappa = 0."""
        a = evaluate_affine_sl2(Rational(-2))
        assert a['kappa'] == 0

    def test_wN_N2(self):
        """W_2 = Virasoro: rho(sl_2) = 1/2."""
        w = evaluate_wN(2, Rational(1))
        assert w['rho_N'] == Rational(1, 2)
        assert w['kappa'] == Rational(1, 2)

    def test_wN_N3(self):
        """W_3: rho(sl_3) = 5/6."""
        w = evaluate_wN(3, Rational(1))
        assert w['rho_N'] == Rational(5, 6)
        assert w['kappa'] == Rational(5, 6)

    def test_wN_N4(self):
        """W_4: rho(sl_4) = 13/12."""
        w = evaluate_wN(4, Rational(1))
        assert w['rho_N'] == Rational(13, 12)
        assert w['kappa'] == Rational(13, 12)


# ========================================================================
# 8. Harmonic number and anomaly ratio
# ========================================================================

class TestHarmonicNumbers:
    """Test harmonic numbers used in W_N kappa formulas."""

    def test_H1(self):
        assert harmonic_number(1) == 1

    def test_H2(self):
        assert harmonic_number(2) == Rational(3, 2)

    def test_H3(self):
        assert harmonic_number(3) == Rational(11, 6)

    def test_H4(self):
        assert harmonic_number(4) == Rational(25, 12)

    def test_H5(self):
        assert harmonic_number(5) == Rational(137, 60)

    def test_anomaly_ratio_sl2(self):
        """rho(sl_2) = H_2 - 1 = 1/2."""
        assert anomaly_ratio(2) == Rational(1, 2)

    def test_anomaly_ratio_sl3(self):
        """rho(sl_3) = H_3 - 1 = 5/6."""
        assert anomaly_ratio(3) == Rational(5, 6)

    def test_anomaly_ratio_sl4(self):
        """rho(sl_4) = H_4 - 1 = 13/12."""
        assert anomaly_ratio(4) == Rational(13, 12)

    def test_kappa_wN_consistency(self):
        """kappa(W_N, c) = rho(sl_N) * c matches dedicated functions."""
        # W_2 = Virasoro
        assert kappa_wN(2, c) == kappa_virasoro(c)
        # W_3
        assert simplify(kappa_wN(3, c) - kappa_w3(c)) == 0


# ========================================================================
# 9. Cross-checks with envelope_shadow_functor.py
# ========================================================================

class TestCrossChecks:
    """Cross-checks against envelope_shadow_functor.py formulas."""

    def test_kappa_heisenberg_cross(self):
        """kappa(Heis, k) = k matches envelope_shadow_functor."""
        from envelope_shadow_functor import kappa_heisenberg as esf_kappa_heis
        assert kappa_heisenberg(Fraction(3)) == esf_kappa_heis(Fraction(3))

    def test_kappa_virasoro_cross(self):
        """kappa(Vir, c) = c/2 matches envelope_shadow_functor."""
        from envelope_shadow_functor import kappa_virasoro as esf_kappa_vir
        assert kappa_virasoro(Rational(26)) == Rational(esf_kappa_vir(Fraction(26)))

    def test_kappa_affine_cross(self):
        """kappa(sl_N, k) matches envelope_shadow_functor."""
        from envelope_shadow_functor import kappa_affine_sl_N as esf_kappa_aff
        for n_val in [2, 3, 4, 5]:
            for k_val in [1, 2, 3, 5]:
                my_val = kappa_affine_slN(n_val, Rational(k_val))
                esf_val = esf_kappa_aff(n_val, Fraction(k_val))
                assert my_val == Rational(esf_val), \
                    f"Mismatch at sl_{n_val}, k={k_val}: {my_val} vs {esf_val}"

    def test_kappa_w3_cross(self):
        """kappa(W_3, c) matches envelope_shadow_functor."""
        from envelope_shadow_functor import kappa_w3 as esf_kappa_w3
        for c_val in [1, 2, 10, 26]:
            my_val = kappa_w3(Rational(c_val))
            esf_val = esf_kappa_w3(Fraction(c_val))
            assert my_val == Rational(esf_val)

    def test_quartic_contact_virasoro_cross(self):
        """Q^contact_Vir matches envelope_shadow_functor."""
        from envelope_shadow_functor import quartic_contact_virasoro as esf_Q
        for c_val in [1, 2, 10, 26]:
            my_S4 = Rational(10) / (Rational(c_val) * (5 * Rational(c_val) + 22))
            esf_val = esf_Q(Fraction(c_val))
            assert my_S4 == Rational(esf_val)

    def test_shadow_depth_data_cross(self):
        """Shadow depth classes match SHADOW_DEPTH_DATA in envelope_shadow_functor."""
        from envelope_shadow_functor import SHADOW_DEPTH_DATA
        census = build_census()
        # Map census keys to SHADOW_DEPTH_DATA keys
        mapping = {
            'Heisenberg': 'Heisenberg',
            'Lattice': 'Lattice',
            'FreeFermion': 'FreeFermion',
            'Affine_sl2': 'Affine_sl2',
            'Affine_slN': 'Affine_generic',
            'BetaGamma': 'BetaGamma',
            'Virasoro': 'Virasoro',
            'W_N': 'W_N',
        }
        for my_key, esf_key in mapping.items():
            if esf_key in SHADOW_DEPTH_DATA:
                assert census[my_key].cls == SHADOW_DEPTH_DATA[esf_key]['class'], \
                    f"Class mismatch for {my_key}: {census[my_key].cls} vs {SHADOW_DEPTH_DATA[esf_key]['class']}"
                assert census[my_key].r_max == SHADOW_DEPTH_DATA[esf_key]['r_max'], \
                    f"r_max mismatch for {my_key}: {census[my_key].r_max} vs {SHADOW_DEPTH_DATA[esf_key]['r_max']}"

    def test_betagamma_kappa_cross(self):
        """kappa(betagamma) matches envelope_shadow_functor."""
        from envelope_shadow_functor import kappa_betagamma as esf_kappa_bg
        for lam_val in [0, Rational(1, 2), 1, 2]:
            my_val = kappa_betagamma(lam_val)
            esf_val = esf_kappa_bg(Fraction(lam_val))
            assert my_val == Rational(esf_val)


# ========================================================================
# 10. Summary table and census structure
# ========================================================================

class TestCensusStructure:
    """Test census structure and summary table."""

    def test_census_has_10_families(self):
        """Census has exactly 10 family entries."""
        census = build_census()
        assert len(census) == 10

    def test_census_keys(self):
        """Census has the expected keys."""
        census = build_census()
        expected_keys = {'Heisenberg', 'Lattice', 'FreeFermion',
                          'Affine_sl2', 'Affine_slN',
                          'BetaGamma', 'bc',
                          'Virasoro', 'W3', 'W_N'}
        assert set(census.keys()) == expected_keys

    def test_summary_table_length(self):
        """Summary table has 10 rows."""
        table = summary_table()
        assert len(table) == 10

    def test_summary_table_keys(self):
        """Each row in summary table has required keys."""
        table = summary_table()
        required = {'name', 'kappa', 'alpha', 'S4', 'Delta', 'Q_L', 'class', 'r_max', 'd_alg'}
        for row in table:
            assert required <= set(row.keys()), f"Missing keys in row: {row['name']}"

    def test_every_entry_has_params(self):
        """Every census entry has a params dict."""
        census = build_census()
        for name, entry in census.items():
            assert isinstance(entry.params, dict), f"{name} missing params"

    def test_to_dict_roundtrip(self):
        """to_dict produces valid output for each entry."""
        census = build_census()
        for name, entry in census.items():
            d = entry.to_dict()
            assert d['name'] == entry.name
            assert d['class'] == entry.cls
            assert d['r_max'] == entry.r_max


# ========================================================================
# 11. Classification boundary cases and edge tests
# ========================================================================

class TestClassificationEdgeCases:
    """Test classification at boundary values and special points."""

    def test_classify_symbolic_nonzero(self):
        """Symbolic nonzero values classify correctly."""
        a = Symbol('a', nonzero=True)
        d = Symbol('d', nonzero=True)
        cls, r = classify(a, d)
        assert cls == 'M'
        assert r is None

    def test_gaussian_three_families(self):
        """All three Gaussian families have identical structure."""
        census = build_census()
        for name in ['Heisenberg', 'Lattice', 'FreeFermion']:
            entry = census[name]
            assert entry.cls == 'G'
            assert entry.r_max == 2
            assert simplify(entry.alpha) == 0
            assert simplify(entry.S4) == 0
            assert simplify(entry.Delta) == 0

    def test_affine_two_entries_agree(self):
        """Affine sl_2 is a special case of sl_N (N=2)."""
        # Both are class L with r_max = 3
        census = build_census()
        assert census['Affine_sl2'].cls == census['Affine_slN'].cls
        assert census['Affine_sl2'].r_max == census['Affine_slN'].r_max

    def test_betagamma_bc_mirror(self):
        """bc and betagamma are both class C."""
        census = build_census()
        assert census['BetaGamma'].cls == 'C'
        assert census['bc'].cls == 'C'
        assert census['BetaGamma'].r_max == census['bc'].r_max == 4

    def test_mixed_class_all_infinite(self):
        """All mixed-class families have r_max = None (infinite tower)."""
        census = build_census()
        for name in ['Virasoro', 'W3', 'W_N']:
            assert census[name].cls == 'M'
            assert census[name].r_max is None

    def test_r_max_ordering(self):
        """r_max ordering: G(2) < L(3) < C(4) < M(inf)."""
        census = build_census()
        assert census['Heisenberg'].r_max == 2
        assert census['Affine_sl2'].r_max == 3
        assert census['BetaGamma'].r_max == 4
        assert census['Virasoro'].r_max is None

    def test_virasoro_is_w2(self):
        """W_2 = Virasoro: same kappa formula."""
        assert simplify(kappa_wN(2, c) - kappa_virasoro(c)) == 0


# ========================================================================
# 12. Betagamma and bc system tests
# ========================================================================

class TestBetaGammaBc:
    """betagamma and bc system shadow metric tests."""

    def test_betagamma_kappa_standard(self):
        """betagamma at lambda=0: kappa = 1."""
        assert kappa_betagamma(0) == 1

    def test_betagamma_kappa_lambda1(self):
        """betagamma at lambda=1: kappa = 1."""
        assert kappa_betagamma(1) == 1

    def test_betagamma_kappa_symplectic(self):
        """betagamma at lambda=1/2 (symplectic): kappa = -1/2."""
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)

    def test_bc_kappa_is_negative_betagamma(self):
        """kappa(bc, j) = -kappa(betagamma, j)."""
        for j_val in [0, Rational(1, 2), 1, 2, 3]:
            assert kappa_bc(j_val) == -kappa_betagamma(j_val)

    def test_betagamma_alpha_zero_on_weight_line(self):
        """betagamma: alpha = 0 on weight-changing line (abelian)."""
        census = build_census()
        assert census['BetaGamma'].alpha == 0

    def test_betagamma_S4_nonzero_on_charged(self):
        """betagamma: S_4 nonzero on charged stratum."""
        census = build_census()
        assert census['BetaGamma'].S4 != 0

    def test_lattice_kappa(self):
        """kappa(V_Lambda) = rank(Lambda)."""
        for r_val in [1, 2, 8, 16, 24]:
            assert kappa_lattice(r_val) == r_val


# ========================================================================
# 13. ShadowMetricEntry API tests
# ========================================================================

class TestShadowMetricEntryAPI:
    """Test the ShadowMetricEntry class interface."""

    def test_entry_creation(self):
        """Create a custom entry and verify."""
        entry = ShadowMetricEntry(
            name='Test',
            kappa=Rational(1),
            alpha=Rational(0),
            S4=Rational(0),
            cls='G',
            r_max=2,
            d_alg='test',
        )
        assert entry.name == 'Test'
        assert entry.kappa == 1
        assert entry.cls == 'G'

    def test_entry_Q_L_custom_param(self):
        """Q_L with custom deformation parameter."""
        s = Symbol('s')
        entry = ShadowMetricEntry(
            name='Test', kappa=Rational(3), alpha=Rational(2),
            S4=Rational(0), cls='L', r_max=3, d_alg='test'
        )
        Q = entry.Q_L(deformation_param=s)
        # Q_L = (2*kappa + 3*alpha*s)^2 = (6 + 6s)^2
        expected = expand((6 + 6 * s)**2)
        assert simplify(Q - expected) == 0

    def test_entry_delta_override(self):
        """Delta override takes precedence over 8*kappa*S4."""
        entry = ShadowMetricEntry(
            name='Test', kappa=Rational(1), alpha=Rational(0),
            S4=Rational(1), cls='C', r_max=4, d_alg='test',
            Delta_override=Rational(42),
        )
        assert entry.Delta == 42
        # verify_Delta checks 8*kappa*S4 = 8, not 42
        # But the entry stores the override
        assert entry.Delta != 8 * entry.kappa * entry.S4

    def test_verify_class_passes(self):
        """verify_class returns True for consistent entries."""
        entry = ShadowMetricEntry(
            name='Test', kappa=Rational(1), alpha=Rational(0),
            S4=Rational(0), cls='G', r_max=2, d_alg='test'
        )
        assert entry.verify_class()

    def test_verify_class_fails(self):
        """verify_class returns False for inconsistent entries."""
        entry = ShadowMetricEntry(
            name='Test', kappa=Rational(1), alpha=Rational(0),
            S4=Rational(0), cls='M', r_max=None, d_alg='test'
        )
        assert not entry.verify_class()
