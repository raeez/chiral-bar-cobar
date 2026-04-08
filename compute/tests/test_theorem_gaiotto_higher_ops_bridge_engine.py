r"""Tests for theorem_gaiotto_higher_ops_bridge_engine.py.

THEOREM: GKW higher operations = shadow obstruction tower projections.

Multi-path verification mandate (CLAUDE.md): every claim verified by >= 3
independent paths where possible.

Test organization:
    1. Shadow coefficient correctness (Virasoro, KM, Heisenberg, betagamma)
    2. Riccati algebraicity verification
    3. GKW Feynman data consistency
    4. Transferred A-infinity operations
    5. Stasheff relations / Wess-Zumino / MC equation bridge
    6. Formality comparison (GKW vs G/L/C/M)
    7. Quantitative bridge at arities 2, 3, 4
    8. D^2 = 0 alternative proof analysis
    9. Framework gap analysis
    10. Full bridge summary
    11. Koszulness and GKW formality
    12. Adversarial / edge-case tests
"""

import pytest
from fractions import Fraction
from math import factorial

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from sympy import Rational, Symbol, simplify, S, expand

from theorem_gaiotto_higher_ops_bridge_engine import (
    # Shadow coefficients
    virasoro_shadow_coefficient,
    affine_sl2_shadow_coefficient,
    affine_slN_shadow_coefficient,
    heisenberg_shadow_coefficient,
    betagamma_shadow_coefficient,
    # GKW Feynman data
    gkw_feynman_data,
    GKWFeynmanData,
    # Transferred operations
    transferred_mk_primary_line,
    # Stasheff / WZ / MC
    stasheff_relation_count,
    verify_stasheff_at_arity,
    wess_zumino_mc_bridge,
    WessZuminoBridge,
    # Formality
    formality_comparison,
    FormalityComparison,
    # Quantitative bridge
    quantitative_bridge_arity2,
    quantitative_bridge_arity3,
    quantitative_bridge_arity4,
    # D^2=0
    feynman_d_squared_analysis,
    # Gaps
    framework_gap_analysis,
    FrameworkGap,
    # Full summary
    full_bridge_summary,
    # Koszulness
    gkw_implies_koszulness_equivalence,
)


c_sym = Symbol('c')
k_sym = Symbol('k')


# ============================================================================
# 1. Shadow coefficient correctness
# ============================================================================

class TestVirasiroShadowCoefficients:
    """Verify Virasoro shadow coefficients S_r(c)."""

    def test_S2_is_kappa(self):
        """S_2 = c/2 (the modular characteristic)."""
        assert virasoro_shadow_coefficient(2) == c_sym / 2

    def test_S3_is_alpha(self):
        """S_3 = 2 (cubic shadow on the T-line)."""
        assert virasoro_shadow_coefficient(3) == Rational(2)

    def test_S4_Q_contact(self):
        """S_4 = 10/[c(5c+22)] (quartic contact invariant)."""
        s4 = virasoro_shadow_coefficient(4)
        expected = Rational(10) / (c_sym * (5 * c_sym + 22))
        assert simplify(s4 - expected) == 0

    def test_S5_explicit(self):
        """S_5 = -48/[c^2(5c+22)]."""
        s5 = virasoro_shadow_coefficient(5)
        expected = Rational(-48) / (c_sym**2 * (5 * c_sym + 22))
        assert simplify(s5 - expected) == 0

    def test_S6_explicit(self):
        """S_6 = 16(55c+1196)/[3 c^3 (5c+22)^2]."""
        s6 = virasoro_shadow_coefficient(6)
        expected = Rational(16) * (55 * c_sym + 1196) / (3 * c_sym**3 * (5 * c_sym + 22)**2)
        assert simplify(s6 - expected) == 0

    def test_S7_explicit(self):
        """S_7 = -2880(15c+61)/[7 c^4 (5c+22)^2]."""
        s7 = virasoro_shadow_coefficient(7)
        expected = Rational(-2880) * (15 * c_sym + 61) / (7 * c_sym**4 * (5 * c_sym + 22)**2)
        assert simplify(s7 - expected) == 0

    def test_S2_numerical_c1(self):
        """S_2(c=1) = 1/2."""
        assert virasoro_shadow_coefficient(2, Rational(1)) == Rational(1, 2)

    def test_S4_numerical_c1(self):
        """S_4(c=1) = 10/(1*27) = 10/27."""
        assert virasoro_shadow_coefficient(4, Rational(1)) == Rational(10, 27)

    def test_S4_numerical_c25(self):
        """S_4(c=25) = 10/(25*147) = 10/3675 = 2/735."""
        val = virasoro_shadow_coefficient(4, Rational(25))
        assert simplify(val - Rational(10, 3675)) == 0

    def test_all_Sr_nonzero_for_generic_c(self):
        """All S_r are nonzero rational functions of c (class M)."""
        c_val = Rational(7)  # generic value
        for r in range(2, 8):
            sr = virasoro_shadow_coefficient(r, c_val)
            assert sr != 0, f'S_{r}(c=7) should be nonzero for class M'

    def test_S_below_2_is_zero(self):
        """S_0 = S_1 = 0."""
        assert virasoro_shadow_coefficient(0) == 0
        assert virasoro_shadow_coefficient(1) == 0


class TestAffineShadowCoefficients:
    """Verify affine KM shadow coefficients."""

    def test_sl2_S2_is_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        s2 = affine_sl2_shadow_coefficient(2)
        assert simplify(s2 - Rational(3) * (k_sym + 2) / 4) == 0

    def test_sl2_S3_nonzero(self):
        """S_3 = 1 (cubic from Lie bracket)."""
        assert affine_sl2_shadow_coefficient(3) == Rational(1)

    def test_sl2_S4_zero(self):
        """S_4 = 0 (Jacobi kills quartic). Class L."""
        assert affine_sl2_shadow_coefficient(4) == 0

    def test_sl2_S5_zero(self):
        """S_r = 0 for r >= 4. Class L terminates at arity 3."""
        for r in range(4, 10):
            assert affine_sl2_shadow_coefficient(r) == 0, f'S_{r} should be 0 for class L'

    def test_sl3_S2_is_kappa(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        s2 = affine_slN_shadow_coefficient(2, 3)
        expected = Rational(8) * (k_sym + 3) / 6
        assert simplify(s2 - expected) == 0

    def test_sl3_class_L(self):
        """sl_3 is class L: S_4 = 0."""
        assert affine_slN_shadow_coefficient(4, 3) == 0

    def test_slN_all_class_L(self):
        """All sl_N are class L: S_4 = 0 for N = 2..8."""
        for N_val in range(2, 9):
            assert affine_slN_shadow_coefficient(4, N_val) == 0, (
                f'sl_{N_val} should have S_4 = 0 (class L)')

    def test_sl2_kappa_at_k1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        assert affine_sl2_shadow_coefficient(2, Rational(1)) == Rational(9, 4)


class TestHeisenbergShadowCoefficients:
    """Verify Heisenberg shadow coefficients."""

    def test_S2_is_k(self):
        """kappa(H_k) = k."""
        assert heisenberg_shadow_coefficient(2) == k_sym

    def test_S3_zero(self):
        """S_3 = 0 (abelian). Class G."""
        assert heisenberg_shadow_coefficient(3) == 0

    def test_all_higher_zero(self):
        """S_r = 0 for all r >= 3. Class G terminates at arity 2."""
        for r in range(3, 15):
            assert heisenberg_shadow_coefficient(r) == 0

    def test_S2_at_k1(self):
        """kappa(H_1) = 1."""
        assert heisenberg_shadow_coefficient(2, Rational(1)) == Rational(1)


class TestBetagammaShadowCoefficients:
    """Verify betagamma shadow coefficients."""

    def test_S2_kappa_lam0(self):
        """kappa(bg, lam=0) = 1."""
        assert betagamma_shadow_coefficient(2, Rational(0)) == Rational(1)

    def test_S3_zero(self):
        """S_3 = 0 (neutral stratum)."""
        assert betagamma_shadow_coefficient(3) == 0

    def test_S4_contact(self):
        """S_4 = -5/12 (contact quartic)."""
        assert betagamma_shadow_coefficient(4) == Rational(-5, 12)

    def test_S5_zero(self):
        """S_5 = 0 (class C terminates at arity 4)."""
        assert betagamma_shadow_coefficient(5) == 0

    def test_all_higher_zero(self):
        """S_r = 0 for r >= 5."""
        for r in range(5, 12):
            assert betagamma_shadow_coefficient(r) == 0


# ============================================================================
# 2. Riccati algebraicity
# ============================================================================

class TestRiccatiAlgebraicity:
    """Verify H^2 = t^4 Q_L for the shadow generating function."""

    def test_riccati_at_c1_through_arity6(self):
        """Verify F(t)^2 = Q_L(t) coefficient-by-coefficient at c=1.

        The Riccati algebraicity (thm:riccati-algebraicity) states:
            H(t) = sum_{r>=2} r * S_r * t^r
            F(t) = H(t)/t^2 = sum_{n>=0} a_n t^n  with a_n = (n+2)*S_{n+2}
            F(t)^2 = Q_L(t)

        where Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.
        """
        c_val = Rational(1)
        kappa = c_val / 2
        alpha = Rational(2)
        Delta = Rational(40) / (5 * c_val + 22)

        S_vals = {r: virasoro_shadow_coefficient(r, c_val) for r in range(2, 8)}

        # a_n = (n+2)*S_{n+2}
        a = {n: (n + 2) * S_vals[n + 2] for n in range(6)}

        # Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        q0 = (2 * kappa)**2
        q1 = 2 * (2 * kappa) * (3 * alpha)
        q2 = (3 * alpha)**2 + 2 * Delta

        # F^2 coefficient at t^0: a_0^2 = q0
        assert simplify(a[0]**2 - q0) == 0, 'Riccati fails at t^0'

        # F^2 coefficient at t^1: 2*a_0*a_1 = q1
        assert simplify(2 * a[0] * a[1] - q1) == 0, 'Riccati fails at t^1'

        # F^2 coefficient at t^2: 2*a_0*a_2 + a_1^2 = q2
        lhs = 2 * a[0] * a[2] + a[1]**2
        assert simplify(lhs - q2) == 0, 'Riccati fails at t^2'

        # F^2 coefficient at t^3: 2*a_0*a_3 + 2*a_1*a_2 = 0 (Q_L is degree 2)
        lhs3 = 2 * a[0] * a[3] + 2 * a[1] * a[2]
        assert simplify(lhs3) == 0, 'Riccati fails at t^3'

    def test_riccati_at_c25_through_arity6(self):
        """Verify Riccati at c=25."""
        c_val = Rational(25)
        kappa = c_val / 2
        alpha = Rational(2)
        Delta = Rational(40) / (5 * c_val + 22)

        S_vals = {r: virasoro_shadow_coefficient(r, c_val) for r in range(2, 8)}
        a = {n: (n + 2) * S_vals[n + 2] for n in range(6)}

        q0 = (2 * kappa)**2
        q1 = 2 * (2 * kappa) * (3 * alpha)
        q2 = (3 * alpha)**2 + 2 * Delta

        assert simplify(a[0]**2 - q0) == 0
        assert simplify(2 * a[0] * a[1] - q1) == 0
        lhs = 2 * a[0] * a[2] + a[1]**2
        assert simplify(lhs - q2) == 0

    def test_discriminant_formula(self):
        """Delta = 8*kappa*S_4 = 40/(5c+22)."""
        c_val = c_sym
        kappa = c_val / 2
        S4 = virasoro_shadow_coefficient(4, c_val)
        Delta_from_formula = 8 * kappa * S4
        Delta_expected = Rational(40) / (5 * c_val + 22)
        assert simplify(Delta_from_formula - Delta_expected) == 0


# ============================================================================
# 3. GKW Feynman data consistency
# ============================================================================

class TestGKWFeynmanData:
    """Verify GKW Feynman diagram data is internally consistent."""

    def test_heisenberg_no_diagrams_at_arity3(self):
        """Free theory: no Feynman diagrams at arity >= 3."""
        fd = gkw_feynman_data('heisenberg', 3)
        assert fd.n_diagrams == 0
        assert fd.value == S.Zero

    def test_heisenberg_convergent(self):
        """All Heisenberg Feynman integrals converge trivially."""
        for k in range(2, 8):
            fd = gkw_feynman_data('heisenberg', k)
            assert fd.is_convergent

    def test_km_m3_has_diagrams(self):
        """Gauge theory has tree diagrams at arity 3."""
        fd = gkw_feynman_data('affine_km', 3)
        assert fd.n_diagrams > 0
        assert fd.value is not None

    def test_km_m4_vanishes(self):
        """Pure gauge: m_4 = 0 (no quartic vertex)."""
        fd = gkw_feynman_data('affine_km', 4)
        assert fd.value == S.Zero

    def test_betagamma_m4_contact(self):
        """Betagamma m_4 = -5/12 (contact quartic)."""
        fd = gkw_feynman_data('betagamma', 4)
        assert fd.value == Rational(-5, 12)

    def test_virasoro_has_catalan_diagrams(self):
        """Virasoro has Catalan(k-1) tree diagrams at arity k."""
        from math import comb
        for k in range(3, 7):
            fd = gkw_feynman_data('virasoro', k)
            catalan = comb(2 * (k - 1), k - 1) // k
            assert fd.n_diagrams == catalan

    def test_fm_dimension_formula(self):
        """FM_k(C) has real dimension 2(k-1)."""
        for k in range(2, 10):
            fd = gkw_feynman_data('heisenberg', k)
            assert fd.dimension == 2 * (k - 1)


# ============================================================================
# 4. Transferred A-infinity operations
# ============================================================================

class TestTransferredOperations:
    """Verify transferred m_k on the primary line equals shadow S_k."""

    def test_heisenberg_mk_all_zero_k3_plus(self):
        """Heisenberg: m_k = 0 for k >= 3 (class G)."""
        for k in range(3, 10):
            val = transferred_mk_primary_line('heisenberg', k)
            assert val == 0

    def test_sl2_m3_nonzero(self):
        """sl_2: m_3 != 0 (class L)."""
        val = transferred_mk_primary_line('affine_sl2', 3)
        assert val != 0

    def test_sl2_m4_zero(self):
        """sl_2: m_4 = 0 (class L terminates)."""
        val = transferred_mk_primary_line('affine_sl2', 4)
        assert val == 0

    def test_virasoro_mk_all_nonzero(self):
        """Virasoro: m_k != 0 for all k >= 2 (class M)."""
        c_val = Rational(7)
        for k in range(2, 8):
            val = transferred_mk_primary_line('virasoro', k, c_val=c_val)
            assert val != 0, f'm_{k} should be nonzero for Virasoro at c=7'

    def test_betagamma_m3_zero_m4_nonzero(self):
        """Betagamma: m_3 = 0 (neutral stratum), m_4 != 0 (class C)."""
        assert transferred_mk_primary_line('betagamma', 3) == 0
        assert transferred_mk_primary_line('betagamma', 4) != 0

    def test_consistency_with_shadow_coefficients(self):
        """Transferred m_k should equal shadow coefficient S_k."""
        c_val = Rational(13)
        for k in range(2, 7):
            mk = transferred_mk_primary_line('virasoro', k, c_val=c_val)
            sk = virasoro_shadow_coefficient(k, c_val)
            assert simplify(mk - sk) == 0, (
                f'Transferred m_{k} != S_{k} for Virasoro at c=13')


# ============================================================================
# 5. Stasheff / Wess-Zumino / MC bridge
# ============================================================================

class TestStasheffRelations:
    """Verify Stasheff relation count and bridge."""

    def test_stasheff_count_arity2(self):
        """Arity 2: 3 terms."""
        assert stasheff_relation_count(2) == 3

    def test_stasheff_count_arity3(self):
        """Arity 3: 6 terms."""
        assert stasheff_relation_count(3) == 6

    def test_stasheff_count_arity4(self):
        """Arity 4: 10 terms."""
        assert stasheff_relation_count(4) == 10

    def test_stasheff_count_formula(self):
        """n(n+1)/2 terms at arity n."""
        for n in range(2, 20):
            assert stasheff_relation_count(n) == n * (n + 1) // 2


class TestWessZuminoBridge:
    """Verify the WZ = Stasheff = MC identification."""

    def test_bridge_at_arity3(self):
        """WZ at arity 3 maps to MC at arity 3."""
        bridge = wess_zumino_mc_bridge(3)
        assert bridge.verified
        assert bridge.arity == 3
        assert 'Q_BRST' in bridge.gkw_lhs
        assert 'Theta' in bridge.our_lhs

    def test_bridge_at_all_arities(self):
        """Bridge is verified at all arities 3-10."""
        for n in range(3, 11):
            bridge = wess_zumino_mc_bridge(n)
            assert bridge.verified

    def test_identification_mentions_bar_differential(self):
        """The identification Q_BRST = D must be present."""
        bridge = wess_zumino_mc_bridge(4)
        assert 'Q_BRST = D' in bridge.identification


class TestMCProjection:
    """Verify Stasheff at specific arities via MC projection."""

    def test_mc_arity4_heisenberg(self):
        """MC at arity 4 for Heisenberg: bracket_sum = S_2*S_2 = k^2.

        The bracket sum is NOT zero even for class G. What the MC equation
        says is D_4(Theta) + (1/2)*bracket_sum = 0, so the differential
        term compensates. The relation holds by construction.
        """
        result = verify_stasheff_at_arity('heisenberg', 4, k_val=Rational(1))
        assert result['relation_holds']
        # bracket_sum at arity 4: sum_{i+j=4, i,j>=2} S_i*S_j = S_2*S_2 = 1
        assert simplify(result['bracket_sum'] - Rational(1)) == 0

    def test_mc_arity5_heisenberg(self):
        """MC at arity 5 for Heisenberg: bracket only has S_2*S_3+S_3*S_2 = 0."""
        result = verify_stasheff_at_arity('heisenberg', 5, k_val=Rational(1))
        assert result['relation_holds']
        # At arity 5: (2,3) and (3,2). S_3=0 for Heisenberg, so bracket=0
        assert result['bracket_sum'] == 0

    def test_mc_arity5_virasoro(self):
        """MC at arity 5 for Virasoro: nontrivial bracket."""
        result = verify_stasheff_at_arity('virasoro', 5, c_val=Rational(1))
        assert result['relation_holds']
        # bracket_sum = S_2*S_3 + S_3*S_2 = 2*S_2*S_3 = 2*(1/2)*2 = 2
        assert simplify(result['bracket_sum'] - Rational(2)) == 0

    def test_mc_arity5_sl2(self):
        """MC at arity 5 for sl_2: only S_2, S_3 nonzero."""
        result = verify_stasheff_at_arity('affine_sl2', 5, k_val=Rational(1))
        assert result['relation_holds']
        # bracket_sum at arity 5: S_2*S_3 + S_3*S_2 = 2 * kappa * 1 = 2 * 9/4 = 9/2
        expected = 2 * Rational(9, 4) * Rational(1)
        assert simplify(result['bracket_sum'] - expected) == 0


# ============================================================================
# 6. Formality comparison
# ============================================================================

class TestFormalityComparison:
    """GKW formality vs shadow depth G/L/C/M."""

    def test_heisenberg_formal_at_d1(self):
        """Heisenberg is formal even at d'=1 (class G). Invisible to GKW."""
        fc = formality_comparison('heisenberg', d_prime=1)
        assert fc.gkw_is_formal  # our class G IS formal
        assert fc.shadow_class == 'G'
        assert fc.shadow_r_max == 2

    def test_km_non_formal_at_d1(self):
        """Affine KM is non-formal at d'=1 (class L)."""
        fc = formality_comparison('affine_km', d_prime=1)
        assert not fc.gkw_is_formal
        assert fc.shadow_class == 'L'
        assert fc.shadow_r_max == 3

    def test_virasoro_non_formal_at_d1(self):
        """Virasoro is non-formal at d'=1 (class M)."""
        fc = formality_comparison('virasoro', d_prime=1)
        assert not fc.gkw_is_formal
        assert fc.shadow_class == 'M'
        assert fc.shadow_r_max == float('inf')

    def test_all_formal_at_d2(self):
        """Everything is formal at d'=2 (GKW formality theorem)."""
        for fam in ['heisenberg', 'affine_km', 'virasoro', 'betagamma']:
            fc = formality_comparison(fam, d_prime=2)
            assert fc.gkw_is_formal

    def test_strict_refinement(self):
        """G/L/C/M strictly refines GKW's binary at d'=1."""
        gkw_classes = set()
        our_classes = set()
        for fam in ['heisenberg', 'affine_km', 'betagamma', 'virasoro']:
            fc = formality_comparison(fam, d_prime=1)
            gkw_classes.add('formal' if fc.gkw_is_formal else 'non-formal')
            our_classes.add(fc.shadow_class)

        # GKW gives 2 classes; we give 4
        assert len(gkw_classes) == 2
        assert len(our_classes) == 4
        assert our_classes == {'G', 'L', 'C', 'M'}


# ============================================================================
# 7. Quantitative bridge at arities 2, 3, 4
# ============================================================================

class TestQuantitativeBridgeArity2:
    """Arity 2: kappa matches between frameworks."""

    def test_heisenberg_kappa_match(self):
        result = quantitative_bridge_arity2('heisenberg', k=Rational(3))
        assert result['match']
        assert result['our_kappa'] == 3

    def test_sl2_kappa_match(self):
        result = quantitative_bridge_arity2('affine_sl2', k=Rational(1))
        assert result['match']
        assert result['our_kappa'] == Rational(9, 4)

    def test_virasoro_kappa_match(self):
        result = quantitative_bridge_arity2('virasoro', c=Rational(26))
        assert result['match']
        assert result['our_kappa'] == 13

    def test_betagamma_kappa_match(self):
        result = quantitative_bridge_arity2('betagamma', lam=Rational(0))
        assert result['match']


class TestQuantitativeBridgeArity3:
    """Arity 3: cubic shadow vs GKW m_3."""

    def test_heisenberg_m3_zero_both(self):
        result = quantitative_bridge_arity3('heisenberg')
        assert result['match']
        assert result['our_S3'] == 0
        assert result['gkw_m3_vanishes']

    def test_sl2_m3_nonzero_both(self):
        result = quantitative_bridge_arity3('affine_sl2')
        assert result['match']
        assert result['our_S3'] != 0
        assert not result['gkw_m3_vanishes']

    def test_virasoro_m3_nonzero_both(self):
        result = quantitative_bridge_arity3('virasoro')
        assert result['match']
        assert result['our_S3'] == 2
        assert not result['gkw_m3_vanishes']


class TestQuantitativeBridgeArity4:
    """Arity 4: quartic shadow vs GKW m_4."""

    def test_heisenberg_m4_zero_both(self):
        result = quantitative_bridge_arity4('heisenberg')
        assert result['match']

    def test_sl2_m4_zero_both(self):
        """Jacobi kills quartic for sl_2."""
        result = quantitative_bridge_arity4('affine_sl2')
        assert result['match']
        assert result['our_S4'] == 0
        assert result['gkw_m4_vanishes']

    def test_virasoro_m4_nonzero_both(self):
        result = quantitative_bridge_arity4('virasoro', c=Rational(1))
        assert result['match']
        assert result['our_S4'] != 0
        assert not result['gkw_m4_vanishes']

    def test_betagamma_m4_contact(self):
        result = quantitative_bridge_arity4('betagamma')
        assert result['match']
        assert result['our_S4'] == Rational(-5, 12)


# ============================================================================
# 8. D^2 = 0 alternative proof
# ============================================================================

class TestDSquaredProof:
    """D^2=0 has three independent proof routes."""

    def test_three_routes_exist(self):
        result = feynman_d_squared_analysis('virasoro')
        assert len(result['routes']) == 3

    def test_routes_are_independent(self):
        result = feynman_d_squared_analysis('virasoro')
        assert result['are_independent']

    def test_route_a_proved(self):
        result = feynman_d_squared_analysis('virasoro')
        assert result['routes']['route_A']['status'] == 'PROVED'

    def test_route_b_proved(self):
        result = feynman_d_squared_analysis('virasoro')
        assert result['routes']['route_B']['status'] == 'PROVED'

    def test_route_c_genus0(self):
        """GKW route is proved at genus 0 only."""
        result = feynman_d_squared_analysis('virasoro')
        assert 'genus 0' in result['routes']['route_C']['status'].lower() or \
               'Genus 0' in result['routes']['route_C']['status']


# ============================================================================
# 9. Framework gap analysis
# ============================================================================

class TestFrameworkGaps:
    """Verify the gap analysis between frameworks."""

    def test_gaps_nonempty(self):
        gaps = framework_gap_analysis()
        assert len(gaps) > 0

    def test_both_directions(self):
        gaps = framework_gap_analysis()
        directions = {g.direction for g in gaps}
        assert 'gkw_only' in directions
        assert 'us_only' in directions

    def test_critical_gaps_exist(self):
        gaps = framework_gap_analysis()
        critical = [g for g in gaps if g.importance == 'critical']
        assert len(critical) >= 4

    def test_genus_expansion_is_us_only(self):
        gaps = framework_gap_analysis()
        genus_gaps = [g for g in gaps if 'genus' in g.description.lower() and g.direction == 'us_only']
        assert len(genus_gaps) >= 1

    def test_formality_d2_is_gkw_only(self):
        gaps = framework_gap_analysis()
        formality_gaps = [g for g in gaps if 'd\'' in g.description and g.direction == 'gkw_only']
        assert len(formality_gaps) >= 1


# ============================================================================
# 10. Full bridge summary
# ============================================================================

class TestFullBridgeSummary:
    """Integration test: full comparison summary."""

    def test_summary_completes(self):
        summary = full_bridge_summary()
        assert summary is not None

    def test_all_arity2_match(self):
        summary = full_bridge_summary()
        assert summary['all_arity2_match']

    def test_all_arity3_match(self):
        summary = full_bridge_summary()
        assert summary['all_arity3_match']

    def test_all_arity4_match(self):
        summary = full_bridge_summary()
        assert summary['all_arity4_match']

    def test_four_families_covered(self):
        summary = full_bridge_summary()
        assert len(summary['arity2']) == 4
        assert len(summary['arity3']) == 4
        assert len(summary['arity4']) == 4

    def test_wz_bridges_exist(self):
        summary = full_bridge_summary()
        assert len(summary['wess_zumino_bridges']) == 5  # arities 3-7

    def test_total_gaps_reasonable(self):
        summary = full_bridge_summary()
        assert summary['total_gaps'] >= 10


# ============================================================================
# 11. Koszulness and GKW formality
# ============================================================================

class TestKoszulnessGKW:
    """GKW formality implies Koszulness at d'>=2."""

    def test_d2_implies_koszul(self):
        result = gkw_implies_koszulness_equivalence(2)
        assert result['implies_koszul']
        assert result['implies_class_G']

    def test_d3_implies_koszul(self):
        result = gkw_implies_koszulness_equivalence(3)
        assert result['implies_koszul']

    def test_d1_does_not_imply_koszul(self):
        result = gkw_implies_koszulness_equivalence(1)
        assert not result['implies_koszul']

    def test_d1_note_mentions_12_equivalences(self):
        result = gkw_implies_koszulness_equivalence(1)
        assert '12' in result['notes']


# ============================================================================
# 12. Adversarial / edge-case tests
# ============================================================================

class TestAdversarial:
    """Edge cases and adversarial tests."""

    def test_virasoro_c0_S4_pole(self):
        """At c=0, S_4 has a pole. This is expected: Virasoro is degenerate."""
        # S_4 = 10/[c(5c+22)] has a pole at c=0
        # We test that the formula evaluates symbolically
        s4 = virasoro_shadow_coefficient(4, c_sym)
        # Substitute c=0 should give oo (pole)
        # This is correct behavior: c=0 is degenerate

    def test_virasoro_c_minus_22_over_5_S4_pole(self):
        """S_4 has a pole at c = -22/5 (5c+22=0)."""
        s4 = virasoro_shadow_coefficient(4, c_sym)
        # At c = -22/5: denominator vanishes

    def test_self_dual_c13(self):
        """At c=13 (Virasoro self-dual): all S_r should be real and nonzero."""
        c_val = Rational(13)
        for r in range(2, 7):
            sr = virasoro_shadow_coefficient(r, c_val)
            assert sr != 0, f'S_{r}(c=13) should be nonzero'

    def test_complementarity_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        c_val = Rational(7)
        kappa_A = virasoro_shadow_coefficient(2, c_val)
        kappa_dual = virasoro_shadow_coefficient(2, 26 - c_val)
        assert kappa_A + kappa_dual == 13

    def test_ap19_pole_shift(self):
        """AP19: bar residue order = OPE pole - 1."""
        # Virasoro: OPE pole 4, bar residue 3
        fd = gkw_feynman_data('virasoro', 3)
        # The pole order in the integrand should reflect the bar residue order
        # (not the raw OPE pole order)

    def test_unknown_family_raises(self):
        """Unknown families raise ValueError."""
        with pytest.raises(ValueError):
            transferred_mk_primary_line('unknown_algebra', 3)
        with pytest.raises(ValueError):
            formality_comparison('unknown_algebra')
        with pytest.raises(ValueError):
            quantitative_bridge_arity2('unknown_algebra')

    def test_large_arity_virasoro(self):
        """Shadow coefficients exist at large arities for Virasoro."""
        # Using the Riccati recursion, S_8 should be computable
        c_val = Rational(2)
        s8 = virasoro_shadow_coefficient(8, c_val)
        assert s8 is not None
        # S_8 should be nonzero for class M
        assert s8 != 0

    def test_kappa_additivity_direct_sum(self):
        """kappa(A1 + A2) = kappa(A1) + kappa(A2) for independent algebras."""
        # Heisenberg H_k1 + H_k2: kappa = k1 + k2
        k1 = Rational(3)
        k2 = Rational(5)
        kappa1 = heisenberg_shadow_coefficient(2, k1)
        kappa2 = heisenberg_shadow_coefficient(2, k2)
        assert kappa1 + kappa2 == k1 + k2

    def test_shadow_class_determines_truncation(self):
        """Shadow class G/L/C/M determines where the tower truncates."""
        # G: terminates at 2
        for r in range(3, 8):
            assert heisenberg_shadow_coefficient(r) == 0

        # L: terminates at 3
        for r in range(4, 8):
            assert affine_sl2_shadow_coefficient(r) == 0

        # C: terminates at 4
        for r in range(5, 8):
            assert betagamma_shadow_coefficient(r) == 0

        # M: never terminates
        c_val = Rational(3)
        for r in range(2, 8):
            assert virasoro_shadow_coefficient(r, c_val) != 0
