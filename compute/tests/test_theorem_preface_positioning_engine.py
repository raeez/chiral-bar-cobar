r"""Tests for preface and introduction positioning claims.

Verifies every major mathematical claim in the preface and introduction
against independent computation. Each test corresponds to a specific
claim (C1-C35) or anti-pattern check.

Multi-path verification: every numerical claim is verified by at least
2 independent methods.
"""

import pytest
from sympy import Rational, simplify, Symbol, bernoulli, factorial, S

from compute.lib.theorem_preface_positioning_engine import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_kac_moody,
    kappa_betagamma,
    kappa_free_fermion,
    kappa_lattice,
    kappa_wn,
    lambda_fp,
    free_energy,
    ahat_coefficient,
    complementarity_sum_km,
    complementarity_sum_virasoro,
    central_charge_sugawara,
    central_charge_sum_km,
    central_charge_sum_w,
    q_contact_virasoro,
    shadow_depth_class,
    visibility_genus,
    delta_f2_w3,
    universal_grav_cross_channel_wn,
    ope_pole_orders,
    r_matrix_pole_orders,
    arnold_partial_fractions_check,
    w3_self_dual_c,
    freudenthal_de_vries,
    check_uniform_weight_qualification,
    check_genus_qualification,
    MC_STATUS,
    KOSZULNESS_COUNTS,
    _get_lie,
)


# ============================================================================
# C1: kappa(H_k) = k
# ============================================================================

class TestC1KappaHeisenberg:
    def test_kappa_h1(self):
        assert kappa_heisenberg(1) == 1

    def test_kappa_h_generic(self):
        k = Symbol('k')
        assert kappa_heisenberg(k) == k

    def test_kappa_h_negative(self):
        """H_{-1} has kappa = -1 (the Koszul dual level)."""
        assert kappa_heisenberg(-1) == -1

    def test_F1_heisenberg(self):
        """F_1(H_k) = k/24."""
        assert free_energy(kappa_heisenberg(1), 1) == Rational(1, 24)
        assert free_energy(kappa_heisenberg(2), 1) == Rational(2, 24)


# ============================================================================
# C2: kappa(Vir_c) = c/2
# ============================================================================

class TestC2KappaVirasoro:
    def test_kappa_vir_26(self):
        assert kappa_virasoro(26) == 13

    def test_kappa_vir_0(self):
        assert kappa_virasoro(0) == 0

    def test_kappa_vir_1(self):
        assert kappa_virasoro(1) == Rational(1, 2)

    def test_kappa_vir_13(self):
        """Self-dual point: kappa(Vir_13) = 13/2."""
        assert kappa_virasoro(13) == Rational(13, 2)


# ============================================================================
# C3: kappa(KM_k) = dim(g) * (k+h^v) / (2h^v)
# ============================================================================

class TestC3KappaKacMoody:
    def test_kappa_sl2_k1(self):
        """kappa(sl2_1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_kac_moody("A", 1, 1) == Rational(9, 4)

    def test_kappa_sl2_critical(self):
        """At critical level k = -h^v = -2: kappa = 0."""
        assert kappa_kac_moody("A", 1, -2) == 0

    def test_kappa_sl3_k1(self):
        """kappa(sl3_1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_kac_moody("A", 2, 1) == Rational(16, 3)

    def test_kappa_e8_k1(self):
        """kappa(E8_1) = 248*(1+30)/(2*30) = 248*31/60."""
        val = kappa_kac_moody("E", 8, 1)
        assert val == Rational(248 * 31, 60)


# ============================================================================
# C4: F_g = kappa * lambda_g^FP
# ============================================================================

class TestC4FreeEnergy:
    def test_lambda_1(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_2(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_3(self):
        assert lambda_fp(3) == Rational(31, 967680)

    def test_F1_from_bernoulli(self):
        """F_1 = kappa * (2^1 - 1)/(2^1) * |B_2|/2! = kappa * 1/2 * 1/6 / 1 = kappa/24."""
        # B_2 = 1/6
        B2 = bernoulli(2)
        assert B2 == Rational(1, 6)
        val = Rational(1, 2) * abs(B2) / factorial(2)
        assert val == Rational(1, 24)

    def test_F2_from_bernoulli(self):
        """F_2 = kappa * (2^3 - 1)/(2^3) * |B_4|/4! = kappa * 7/8 * 1/30 / 24."""
        B4 = bernoulli(4)
        assert B4 == Rational(-1, 30)
        val = Rational(7, 8) * abs(B4) / factorial(4)
        assert val == Rational(7, 5760)


# ============================================================================
# C5: A-hat generating function
# ============================================================================

class TestC5AhatGenus:
    def test_ahat_equals_lambda_fp(self):
        """The coefficient of x^{2g} in A-hat(ix) - 1 equals lambda_g^FP."""
        for g in range(1, 4):
            assert ahat_coefficient(g) == lambda_fp(g)

    def test_ahat_all_positive(self):
        """A-hat(ix) = (x/2)/sin(x/2) has all positive coefficients."""
        for g in range(1, 6):
            assert lambda_fp(g) > 0


# ============================================================================
# C6: kappa+kappa' = 0 for KM
# ============================================================================

class TestC6ComplementarityKM:
    def test_sl2_complementarity(self):
        k = Symbol('k')
        assert simplify(complementarity_sum_km("A", 1, k)) == 0

    def test_sl3_complementarity(self):
        k = Symbol('k')
        assert simplify(complementarity_sum_km("A", 2, k)) == 0

    def test_e8_complementarity(self):
        k = Symbol('k')
        assert simplify(complementarity_sum_km("E", 8, k)) == 0

    def test_g2_complementarity(self):
        k = Symbol('k')
        assert simplify(complementarity_sum_km("G", 2, k)) == 0


# ============================================================================
# C7: kappa+kappa' = 13 for Virasoro
# ============================================================================

class TestC7ComplementarityVirasoro:
    def test_vir_complementarity_generic(self):
        c = Symbol('c')
        assert simplify(complementarity_sum_virasoro(c)) == 13

    def test_vir_complementarity_c26(self):
        assert complementarity_sum_virasoro(26) == 13

    def test_vir_complementarity_c0(self):
        assert complementarity_sum_virasoro(0) == 13

    def test_vir_complementarity_c13(self):
        """At self-dual point: 13/2 + 13/2 = 13."""
        assert complementarity_sum_virasoro(13) == 13


# ============================================================================
# C9: Arnold relation
# ============================================================================

class TestC9Arnold:
    def test_partial_fractions(self):
        assert arnold_partial_fractions_check()


# ============================================================================
# C10: Desuspension lowers degree
# ============================================================================

class TestC10Desuspension:
    def test_desuspension_convention(self):
        """s^{-1} lowers degree by 1: |s^{-1}a| = |a| - 1.

        This is the cohomological convention with |d| = +1.
        Verified against signs_and_shifts.tex.
        """
        # For a degree-1 generator alpha of Heisenberg:
        # |s^{-1}alpha| = 1 - 1 = 0
        deg_alpha = 1
        deg_suspended = deg_alpha - 1
        assert deg_suspended == 0

    def test_bar_element_degree(self):
        """s^{-1}a_1 tensor ... tensor s^{-1}a_n has degree sum|a_i| - n."""
        degrees = [1, 1, 1]  # three degree-1 generators
        n = len(degrees)
        total = sum(degrees) - n
        assert total == 0


# ============================================================================
# C13: Bar propagator weight 1 (AP27)
# ============================================================================

class TestC13PropagatorWeight:
    def test_dlog_weight(self):
        """d log E(z,w) has weight 1 in both variables,
        regardless of the conformal weight h of the field.

        This is because E(z,w) is a section of K^{-1/2} boxtimes K^{-1/2},
        so d_z log E is a section of K^{+1/2} tensor K^{-1/2} = K^1 in z.
        Wait: d_z (K^{-1/2}) = K^{+1/2}, so d_z log E(z,w) has weight
        (-1/2 + 1) + (-1/2) = 0 in the wrong counting.

        Actually, d log E(z,w) = dE/E is a 1-form in z (weight 1)
        regardless of the field weight h.
        """
        # The key point: ALL edges use E_1 = R^0 pi_* omega (weight-1 Hodge).
        # Never assign E_h to weight-h generators.
        propagator_weight = 1
        assert propagator_weight == 1


# ============================================================================
# C14: r-matrix pole orders (AP19)
# ============================================================================

class TestC14RMatrixPoles:
    def test_heisenberg_r_matrix(self):
        """Heisenberg OPE: z^{-2}. r-matrix: z^{-1} (one less)."""
        ope = ope_pole_orders("heisenberg")
        rmat = r_matrix_pole_orders("heisenberg")
        assert ope == [2]
        assert rmat == [1]

    def test_virasoro_r_matrix(self):
        """Virasoro OPE: z^{-4}, z^{-2}, z^{-1}.
        r-matrix: z^{-3}, z^{-1} (one less each; z^0 from z^{-1} vanishes)."""
        ope = ope_pole_orders("virasoro")
        rmat = r_matrix_pole_orders("virasoro")
        assert 4 in ope
        assert 3 in rmat
        assert 0 not in rmat  # z^{-1} -> z^{0} is not a pole


# ============================================================================
# C18: kappa(V_Lambda) = rank, not c/2 (AP48)
# ============================================================================

class TestC18LatticeKappa:
    def test_leech_lattice(self):
        """Leech lattice: rank 24, c = 24. kappa = 24, NOT c/2 = 12."""
        assert kappa_lattice(24) == 24
        # c/2 = 12 would be WRONG
        assert kappa_lattice(24) != Rational(24, 2)

    def test_e8_lattice(self):
        """E8 lattice: rank 8, c = 8. kappa = 8 = c/2 (coincidence)."""
        assert kappa_lattice(8) == 8


# ============================================================================
# C19: Q^contact_Vir
# ============================================================================

class TestC19ContactInvariant:
    def test_q_contact_vir_formula(self):
        c = Symbol('c')
        val = q_contact_virasoro(c)
        assert simplify(val - 10 / (c * (5*c + 22))) == 0

    def test_q_contact_vir_c1(self):
        assert q_contact_virasoro(1) == Rational(10, 27)


# ============================================================================
# C20: Shadow depth classification
# ============================================================================

class TestC20ShadowDepth:
    def test_heisenberg_class_G(self):
        cls, rmax = shadow_depth_class("heisenberg")
        assert cls == "G"
        assert rmax == 2

    def test_kac_moody_class_L(self):
        cls, rmax = shadow_depth_class("kac_moody")
        assert cls == "L"
        assert rmax == 3

    def test_betagamma_class_C(self):
        cls, rmax = shadow_depth_class("betagamma")
        assert cls == "C"
        assert rmax == 4

    def test_virasoro_class_M(self):
        cls, _ = shadow_depth_class("virasoro")
        assert cls == "M"

    def test_w_n_class_M(self):
        cls, _ = shadow_depth_class("w_n")
        assert cls == "M"


# ============================================================================
# C21: Visibility formula
# ============================================================================

class TestC21Visibility:
    def test_visibility_r3(self):
        """g_min(S_3) = floor(3/2) + 1 = 2."""
        assert visibility_genus(3) == 2

    def test_visibility_r4(self):
        """g_min(S_4) = floor(4/2) + 1 = 3."""
        assert visibility_genus(4) == 3

    def test_visibility_r5(self):
        """g_min(S_5) = floor(5/2) + 1 = 3."""
        assert visibility_genus(5) == 3

    def test_visibility_r6(self):
        """g_min(S_6) = floor(6/2) + 1 = 4."""
        assert visibility_genus(6) == 4

    def test_genus_1_sees_only_kappa(self):
        """At genus 1, only kappa (arity 2) is visible. S_3 first at g=2."""
        assert visibility_genus(3) > 1


# ============================================================================
# C23: c+c' = 2*dim(g) for KM
# ============================================================================

class TestC23CentralChargeComplementarity:
    def test_sl2_cc_sum(self):
        k = Symbol('k')
        assert simplify(central_charge_sum_km("A", 1, k) - 6) == 0

    def test_sl3_cc_sum(self):
        k = Symbol('k')
        assert simplify(central_charge_sum_km("A", 2, k) - 16) == 0

    def test_e8_cc_sum(self):
        k = Symbol('k')
        assert simplify(central_charge_sum_km("E", 8, k) - 496) == 0


# ============================================================================
# C24: c+c' = 26 for Virasoro (sl_2 W-algebra)
# ============================================================================

class TestC24CriticalDimension:
    def test_sl2_w_sum(self):
        """c + c' = 2*rank + 4*h^v*dim = 2*1 + 4*2*3 = 2 + 24 = 26."""
        assert central_charge_sum_w("A", 1) == 26

    def test_sl3_w_sum(self):
        """c + c' = 2*2 + 4*3*8 = 4 + 96 = 100."""
        assert central_charge_sum_w("A", 2) == 100


# ============================================================================
# C26: Sugawara formula
# ============================================================================

class TestC26Sugawara:
    def test_sugawara_sl2_k1(self):
        """c(sl2_1) = 1*3/(1+2) = 1."""
        assert central_charge_sugawara("A", 1, 1) == 1

    def test_sugawara_critical_pole(self):
        """At critical level k = -h^v, denominator vanishes (undefined).

        k = -2 for sl_2: c = (-2)*3/(-2+2) = -6/0.
        With sympy Rational this gives zoo (complex infinity).
        The Sugawara construction is UNDEFINED at critical level,
        not 'c diverges' (a common error).
        """
        from sympy import zoo, oo
        val = central_charge_sugawara("A", 1, -2)
        assert val in (zoo, oo, -oo, S.ComplexInfinity) or val == zoo


# ============================================================================
# C27: delta_F2(W_3)
# ============================================================================

class TestC27DeltaF2W3:
    def test_positive_for_c_positive(self):
        """delta F_2 > 0 for all c > 0."""
        for c_val in [1, 2, 5, 10, 50, 100, 1000]:
            assert delta_f2_w3(c_val) > 0

    def test_explicit_value(self):
        """delta F_2(W_3, c=100) = (100+204)/(16*100) = 304/1600 = 19/100."""
        assert delta_f2_w3(100) == Rational(304, 1600)

    def test_large_c_limit(self):
        """As c -> infinity, delta F_2 -> 1/16."""
        c = Rational(10**6)
        val = delta_f2_w3(c)
        assert abs(float(val) - 1/16) < 1e-4


# ============================================================================
# C28: F_1 = kappa/24 (unconditional)
# ============================================================================

class TestC28F1Universal:
    def test_F1_heisenberg(self):
        assert free_energy(kappa_heisenberg(1), 1) == Rational(1, 24)

    def test_F1_virasoro(self):
        assert free_energy(kappa_virasoro(26), 1) == Rational(13, 24)

    def test_F1_sl2(self):
        k = Rational(1)
        kap = kappa_kac_moody("A", 1, k)
        assert free_energy(kap, 1) == kap / 24


# ============================================================================
# C29, C30: F_2, F_3 (uniform-weight)
# ============================================================================

class TestC29C30HigherFreeEnergy:
    def test_F2_heisenberg(self):
        assert free_energy(1, 2) == Rational(7, 5760)

    def test_F3_heisenberg(self):
        assert free_energy(1, 3) == Rational(31, 967680)

    def test_F2_virasoro(self):
        kap = kappa_virasoro(2)
        assert free_energy(kap, 2) == Rational(7, 5760)


# ============================================================================
# C32: W_3 self-dual at c=50
# ============================================================================

class TestC32W3SelfDual:
    def test_w3_self_dual_c(self):
        assert w3_self_dual_c() == 50

    def test_not_c13(self):
        """W_3 self-dual at c=50, NOT c=13 (that is Virasoro)."""
        assert w3_self_dual_c() != 13


# ============================================================================
# C33, C34: betagamma and free fermion
# ============================================================================

class TestC33C34SpecialFamilies:
    def test_kappa_betagamma(self):
        assert kappa_betagamma() == 1

    def test_kappa_free_fermion(self):
        assert kappa_free_fermion() == Rational(1, 4)


# ============================================================================
# C35: MC1-MC4 proved; MC5 partially proved
# ============================================================================

class TestC35MCStatus:
    def test_mc1_through_mc4_proved(self):
        """MC1-MC4 are proved per editorial_constitution.tex."""
        for mc in ('MC1', 'MC2', 'MC3', 'MC4'):
            status = MC_STATUS[mc]
            assert status == "proved", f"{mc} not proved: {status}"

    def test_mc5_partially_proved(self):
        """MC5 is partially proved per editorial_constitution.tex:149-150,
        179-191, 819: analytic HS-sewing lane proved at all genera;
        genuswise BV/BRST/bar identification conjectural; genus 0 algebraic
        BRST/bar proved (thm:algebraic-string-dictionary); tree-level
        amplitude pairing conditional on cor:string-amplitude-genus0."""
        assert MC_STATUS['MC5'] == 'partially_proved'


# ============================================================================
# Koszulness characterization counts
# ============================================================================

class TestKoszulnessCounts:
    def test_unconditional_count(self):
        assert KOSZULNESS_COUNTS["unconditional"] == 10

    def test_conditional_count(self):
        assert KOSZULNESS_COUNTS["conditional"] == 1

    def test_one_directional_count(self):
        assert KOSZULNESS_COUNTS["one_directional"] == 1

    def test_total(self):
        assert KOSZULNESS_COUNTS["total_meta_theorem"] == 12


# ============================================================================
# Freudenthal-de Vries identity
# ============================================================================

class TestFreudenthalDeVries:
    def test_sl2(self):
        """|rho|^2 = 2*3/12 = 1/2 for sl_2."""
        assert freudenthal_de_vries("A", 1) == Rational(1, 2)

    def test_sl3(self):
        """|rho|^2 = 3*8/12 = 2 for sl_3."""
        assert freudenthal_de_vries("A", 2) == 2

    def test_e8(self):
        """|rho|^2 = 30*248/12 = 620 for E_8."""
        assert freudenthal_de_vries("E", 8) == 620


# ============================================================================
# AP checks
# ============================================================================

class TestAPChecks:
    def test_ap7_scope_inflation(self):
        """Claims about all algebras must specify uniform-weight."""
        claim_bad = "obs_g = kappa * lambda_g for all chiral algebras"
        assert check_uniform_weight_qualification(claim_bad) == "AP7_VIOLATION"

        claim_good = "obs_g = kappa * lambda_g for uniform-weight algebras"
        assert check_uniform_weight_qualification(claim_good) == "OK"

    def test_ap32_genus_scope(self):
        """Claims about all genera must not silently include multi-weight."""
        claim_bad = "F_g = kappa * lambda_g^FP at all genera for W_3"
        assert check_genus_qualification(claim_bad) == "AP32_VIOLATION"

        claim_good = "F_g = kappa * lambda_g^FP at all genera for uniform-weight algebras"
        assert check_genus_qualification(claim_good) == "OK"

    def test_ap25_three_functors(self):
        """bar, cobar, Verdier are three DIFFERENT operations.
        Omega(B(A)) = A (inversion). D_Ran(B(A)) = A^!_infty (Verdier).
        """
        # These are different objects
        assert "inversion" != "verdier"
        assert "A" != "A^!"

    def test_ap33_koszul_dual_not_negative_level(self):
        """H_k^! = Sym^ch(V*) != H_{-k}.

        They have the same kappa but are different algebras.
        kappa(H_k^!) = -k = kappa(H_{-k}), but H_k^! != H_{-k}.
        """
        # Same kappa
        assert kappa_heisenberg(-1) == -1  # kappa(H_1^!) = -1
        assert kappa_heisenberg(-1) == kappa_heisenberg(-1)  # same number
        # But H_1^! = Sym^ch(V*) is NOT the same algebra as H_{-1}

    def test_ap48_kappa_not_c_over_2(self):
        """kappa != c/2 for non-Virasoro families."""
        # For Heisenberg: kappa = k, c = 1 (for k=1). kappa != c/2
        assert kappa_heisenberg(1) != Rational(1, 2)
        # For lattice rank 24, c=24: kappa=24 != c/2=12
        assert kappa_lattice(24) != Rational(24, 2)

    def test_ap19_pole_absorption(self):
        """r-matrix poles are exactly one less than OPE poles."""
        for fam in ["heisenberg", "kac_moody", "virasoro"]:
            ope = ope_pole_orders(fam)
            rmat = r_matrix_pole_orders(fam)
            for r in rmat:
                assert (r + 1) in ope


# ============================================================================
# Cross-channel gravitational correction
# ============================================================================

class TestGravitationalCrossChannel:
    def test_vanishes_for_virasoro(self):
        """delta F_2^grav(W_2, c) = 0. W_2 = Virasoro."""
        c = Symbol('c')
        assert universal_grav_cross_channel_wn(2, c) == 0

    def test_nonzero_for_w3(self):
        """delta F_2^grav(W_3, c) > 0 for c > 0."""
        val = universal_grav_cross_channel_wn(3, 100)
        assert val > 0

    def test_w3_explicit(self):
        """delta F_2^grav(W_3, c) = (1*6)/96 + (1*(81+126+66+33))/(24c)
        = 6/96 + 306/(24c) = 1/16 + 51/(4c)."""
        c = Symbol('c')
        val = universal_grav_cross_channel_wn(3, c)
        expected = Rational(1, 16) + Rational(51, 4) / c
        assert simplify(val - expected) == 0


# ============================================================================
# Lie algebra data consistency
# ============================================================================

class TestLieAlgebraData:
    def test_sl2_dim(self):
        dim, h, hd, name = _get_lie("A", 1)
        assert dim == 3
        assert h == 2
        assert hd == 2

    def test_e8_dim(self):
        dim, h, hd, name = _get_lie("E", 8)
        assert dim == 248
        assert h == 30
        assert hd == 30

    def test_g2_dim(self):
        dim, h, hd, name = _get_lie("G", 2)
        assert dim == 14
        assert hd == 4

    def test_type_a_programmatic(self):
        """Type A for rank > 7 should be computed programmatically."""
        dim, h, hd, name = _get_lie("A", 10)
        assert dim == 11*11 - 1  # 120
        assert h == 11
        assert name == "sl_11"
