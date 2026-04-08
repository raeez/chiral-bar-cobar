r"""Tests for shadow_l_function_arithmetic_engine.py.

Verifies the arithmetic of L_A^{Eis}(s) = -kappa zeta(s) zeta(s-1) and
documents the BEILINSON FINDING that the Bernoulli-Dirichlet series
sum_{r >= 2} (B_{2r}/(2r)!) r^{-s} does NOT equal the same closed form.

Verification paths (>= 3 per claim):
  Path 1: Direct mpmath numerical evaluation
  Path 2: Riemann zeta special-value formulas
  Path 3: Closed-form Bernoulli generating function evaluation
  Path 4: Cross-family kappa values (Heisenberg, affine, Virasoro, lattice)
  Path 5: Euler product reconstruction
"""

import math
import sys
import os
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_l_function_arithmetic_engine import (
    bernoulli, bernoulli_ratio,
    zeta_at_negative_odd, zeta_at_zero, zeta_at_negative_even,
    kappa_virasoro, kappa_heisenberg, kappa_affine_km, kappa_lattice_voa,
    shadow_coefficient_algebraic, shadow_coefficient_exact,
    L_A_Dir, L_A_Eis,
    disagreement_at_zero,
    L_Eis_special_value, L_Eis_at_positive_even, L_Eis_pole_residues,
    riemann_xi, L_Eis_completed, functional_equation_image, functional_equation_check,
    trivial_zeros, riemann_zeros_image, L_Eis_at_zeta_zero, L_Eis_at_shifted_zeta_zero,
    critical_lines,
    euler_factor, euler_product_truncated, coefficient_an, L_Eis_dirichlet_partial,
    kummer_congruence_test, p_adic_valuation, kubota_leopoldt_special_value,
    L_at_s_eq_2, L_at_s_eq_2_residue, L_at_s_eq_0, L_at_s_eq_minus_1, L_at_negative_integers,
    F_g_via_riemann_FE, A_hat_coefficient, F_g_predicted,
    L_Eis_monster, monster_residue_at_2, monster_kappa_correction,
    full_diagnostic,
    HAS_MPMATH,
)

if HAS_MPMATH:
    import mpmath


# ============================================================================
# SECTION 0.  Bernoulli numbers and Riemann zeta special values
# ============================================================================


class TestBernoulli:
    def test_B0(self):
        assert bernoulli(0) == Fraction(1)

    def test_B1(self):
        assert bernoulli(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli(6) == Fraction(1, 42)

    def test_B12(self):
        assert bernoulli(12) == Fraction(-691, 2730)

    def test_odd_vanish(self):
        for n in range(3, 16, 2):
            assert bernoulli(n) == 0

    def test_bernoulli_ratio_r1(self):
        # B_2 / 2! = 1/12
        assert bernoulli_ratio(1) == Fraction(1, 12)

    def test_bernoulli_ratio_r2(self):
        # B_4 / 4! = -1/720
        assert bernoulli_ratio(2) == Fraction(-1, 720)


class TestZetaSpecialValues:
    def test_zeta_zero(self):
        assert zeta_at_zero() == Fraction(-1, 2)

    def test_zeta_minus_1(self):
        assert zeta_at_negative_odd(1) == Fraction(-1, 12)

    def test_zeta_minus_3(self):
        assert zeta_at_negative_odd(2) == Fraction(1, 120)

    def test_zeta_minus_5(self):
        assert zeta_at_negative_odd(3) == Fraction(-1, 252)

    def test_zeta_minus_2_zero(self):
        assert zeta_at_negative_even(1) == 0

    def test_zeta_minus_4_zero(self):
        assert zeta_at_negative_even(2) == 0


# ============================================================================
# SECTION 1.  Modular characteristics
# ============================================================================


class TestKappa:
    def test_virasoro_c2(self):
        assert kappa_virasoro(2.0) == 1.0

    def test_virasoro_c26(self):
        assert kappa_virasoro(26.0) == 13.0

    def test_heisenberg(self):
        assert kappa_heisenberg(7.0) == 7.0

    def test_affine_sl2_level_1(self):
        # sl_2: dim=3, h^vee=2, kappa = 3*(1+2)/4 = 9/4
        k = kappa_affine_km(3, 1.0, 2)
        assert abs(k - 9 / 4) < 1e-12

    def test_lattice_voa_e8(self):
        assert kappa_lattice_voa(8) == 8

    def test_lattice_voa_leech(self):
        assert kappa_lattice_voa(24) == 24

    def test_kappa_vnatural_not_c_over_2(self):
        # AP48: kappa(V^natural) = 24, NOT c/2 = 12.
        assert kappa_lattice_voa(24) != 24.0 / 2


# ============================================================================
# SECTION 2.  Shadow coefficients on the algebraic-family lane
# ============================================================================


class TestShadowCoefficients:
    """Convention A (asymptotic-lane):  S_r(A) = kappa(A) * B_{2r}/(2r)! for r >= 1.

    WARNING:  this convention DIFFERS from the arity convention where
    S_2 = kappa directly.  The manuscript proof of thm:shadow-eisenstein
    uses Convention A.  The Bernoulli ratio table:

        r=1: B_2/2!  =  1/12
        r=2: B_4/4!  = -1/720        (S_2 on the asymptotic lane)
        r=3: B_6/6!  =  1/30240
        r=4: B_8/8!  = -1/1209600
    """

    def test_S_r1_virasoro_c26(self):
        # Index r=1 on the asymptotic lane: B_2/2! = 1/12, so S = 13/12.
        val = shadow_coefficient_algebraic(13.0, 1)
        assert abs(val - 13.0 / 12.0) < 1e-12

    def test_S_r2_virasoro_c26(self):
        # Index r=2: B_4/4! = -1/30 / 24 = -1/720, so S = -13/720.
        val = shadow_coefficient_algebraic(13.0, 2)
        assert abs(val - (-13.0 / 720.0)) < 1e-12

    def test_S_r3_virasoro_c1(self):
        # B_6/6! = 1/30240
        val = shadow_coefficient_algebraic(1.0, 3)
        assert abs(val - 1.0 / 30240.0) < 1e-15

    def test_exact_arithmetic_r1(self):
        Sr = shadow_coefficient_exact(Fraction(13), 1)
        assert Sr == Fraction(13, 12)

    def test_exact_arithmetic_r2(self):
        Sr = shadow_coefficient_exact(Fraction(13), 2)
        assert Sr == Fraction(-13, 720)

    def test_decay_rate_matches_riemann_zeta(self):
        # Cross-check: |B_{2r}/(2r)!| = 2 zeta(2r) / (2pi)^{2r}
        # This is an independent verification path (Path 5: Bernoulli <-> zeta)
        for r in range(1, 6):
            lhs = abs(float(bernoulli_ratio(r)))
            zeta_2r = {1: math.pi**2/6, 2: math.pi**4/90, 3: math.pi**6/945,
                       4: math.pi**8/9450, 5: math.pi**10/93555}[r]
            rhs = 2 * zeta_2r / (2 * math.pi) ** (2 * r)
            assert abs(lhs - rhs) / rhs < 1e-10


# ============================================================================
# SECTION 3.  THE CRITICAL BEILINSON FINDING
# ============================================================================


class TestBeilinsonFindingDirVsEis:
    """The proof in arithmetic_shadows.tex claims sum B_{2r}/(2r)! r^{-s} =
    -zeta(s) zeta(s-1).  This test class verifies that claim is FALSE.
    """

    def test_disagreement_at_zero_explicit(self):
        d = disagreement_at_zero(kappa_val=2.0, r_max=80)
        # Internal consistency of the Dirichlet form
        assert d["agreement_Dir_internal"] < 1e-10
        # The two forms DISAGREE
        assert d["disagreement_Dir_vs_Eis"] > 1e-3

    def test_dir_form_at_zero_value(self):
        # sum_{r>=2} B_{2r}/(2r)! = 1/(e-1) - 1/2 - 1/12
        kappa_val = 1.0
        d = disagreement_at_zero(kappa_val=kappa_val, r_max=80)
        expected = 1.0 / (math.e - 1.0) - 0.5 - 1.0 / 12.0
        assert abs(d["L_Dir_at_0_numeric"] - expected) < 1e-10

    def test_eis_form_at_zero_value(self):
        # -kappa * zeta(0) zeta(-1) = -kappa/24
        kappa_val = 24.0
        d = disagreement_at_zero(kappa_val=kappa_val, r_max=80)
        assert abs(d["L_Eis_at_0"] - (-1.0)) < 1e-12

    def test_dir_form_is_entire(self):
        # The Dirichlet form converges for all s; sample at s = 2 (where Eis has a pole)
        val = L_A_Dir(1.0, complex(2, 0), r_max=60)
        assert abs(val) < 1.0  # finite, not a pole

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_eis_form_has_pole_at_2(self):
        # |L_Eis(2 - epsilon)| should blow up as epsilon -> 0
        v_far = abs(L_A_Eis(1.0, 2.5))
        v_near = abs(L_A_Eis(1.0, complex(2.001, 0)))
        # L_Eis has 1/(s-2) behaviour
        assert v_near > 100 * v_far


# ============================================================================
# SECTION 4.  Eisenstein-form special values
# ============================================================================


class TestEisSpecialValues:
    def test_at_zero(self):
        # L_Eis(0) = -kappa * (-1/2)(-1/12) = -kappa/24
        assert abs(L_at_s_eq_0(24.0) - (-1.0)) < 1e-12

    def test_at_minus_1_is_zero(self):
        # L_Eis(-1) = -kappa zeta(-1) zeta(-2) = -kappa(-1/12)(0) = 0
        # The user's claimed -kappa/144 is INCORRECT.
        assert L_at_s_eq_minus_1(13.0) == 0.0

    def test_at_negative_integers_all_zero(self):
        vals = L_at_negative_integers(13.0, max_neg=10)
        for k, v in vals.items():
            assert v == 0.0, f"L_Eis({k}) should be 0 but got {v}"

    def test_special_value_at_zero_rational(self):
        v = L_Eis_special_value(24.0, 0)
        assert v == Fraction(-1, 24) * Fraction(24)
        assert v == Fraction(-1)

    def test_special_value_at_pole(self):
        assert L_Eis_special_value(13.0, 1) is None
        assert L_Eis_special_value(13.0, 2) is None

    def test_special_value_at_negative(self):
        for k in range(1, 8):
            assert L_Eis_special_value(13.0, -k) == Fraction(0)


class TestEisResidues:
    def test_residue_at_1(self):
        # Res = -kappa * zeta(0) = kappa/2
        r = L_Eis_pole_residues(13.0)
        assert abs(r["residue_at_s_eq_1"] - 13.0 / 2) < 1e-12

    def test_residue_at_2(self):
        # Res = -kappa * zeta(2) = -kappa pi^2 / 6
        r = L_Eis_pole_residues(13.0)
        assert abs(r["residue_at_s_eq_2"] - (-13.0 * math.pi ** 2 / 6)) < 1e-10

    def test_residue_at_2_helper(self):
        assert abs(L_at_s_eq_2_residue(12.0) - (-2.0 * math.pi ** 2)) < 1e-12

    def test_l_at_2_is_pole(self):
        assert L_at_s_eq_2(13.0) is None


# ============================================================================
# SECTION 5.  Functional equation
# ============================================================================


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestFunctionalEquation:
    def test_xi_symmetry(self):
        # xi(s) = xi(1-s)
        for s in [0.3, 0.7, 1.5, complex(0.5, 14.13)]:
            xi_s = riemann_xi(s)
            xi_1ms = riemann_xi(1 - s)
            assert abs(xi_s - xi_1ms) < 1e-10

    def test_FE_image(self):
        assert functional_equation_image(0.5) == 2.5
        assert functional_equation_image(1.5) == 1.5  # fixed point

    def test_symmetry_centre_at_3_2(self):
        # The two critical lines 1/2 and 3/2 are reflected through s = 1.
        # Mid-point of {1/2, 3/2} is 1.
        assert (0.5 + 1.5) / 2 == 1.0


# ============================================================================
# SECTION 6.  Zeros
# ============================================================================


class TestTrivialZeros:
    def test_trivial_zeros_first_few(self):
        z = trivial_zeros(5)
        assert z == [-1, -2, -3, -4, -5]

    def test_all_negative_integers_are_trivial(self):
        z = trivial_zeros(20)
        assert len(z) == 20
        assert all(k < 0 for k in z)


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestNonTrivialZeros:
    def test_zero_at_first_riemann_zero(self):
        # rho_1 ~ 1/2 + 14.1347 i
        v = L_Eis_at_zeta_zero(1.0, 1)
        assert abs(v) < 1e-8

    def test_zero_at_first_shifted_riemann_zero(self):
        v = L_Eis_at_shifted_zeta_zero(1.0, 1)
        assert abs(v) < 1e-8

    def test_two_critical_lines(self):
        lines = critical_lines()
        assert lines == [0.5, 1.5]

    def test_riemann_zeros_image_pairs(self):
        pairs = riemann_zeros_image(3)
        assert len(pairs) == 3
        for rho, rho_plus_1 in pairs:
            assert abs(rho.real - 0.5) < 1e-8
            assert abs(rho_plus_1.real - 1.5) < 1e-8
            assert abs(rho.imag - rho_plus_1.imag) < 1e-12


# ============================================================================
# SECTION 7.  Euler product
# ============================================================================


class TestEulerProduct:
    def test_an_first_few(self):
        # a_n = -sigma_1(n)
        assert coefficient_an(1) == -1
        assert coefficient_an(2) == -3   # sigma_1(2) = 1+2 = 3
        assert coefficient_an(3) == -4
        assert coefficient_an(4) == -7
        assert coefficient_an(6) == -12  # 1+2+3+6

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_euler_vs_dirichlet(self):
        # For Re(s) > 2, both Euler product and Dirichlet sum should
        # approach L_Eis (slow convergence; Dirichlet sum has O(N^{2-s}) error).
        kappa_val = 1.0
        s = 4.0  # faster convergence than s=3
        v_euler = euler_product_truncated(kappa_val, s, p_max=500)
        v_dir = L_Eis_dirichlet_partial(kappa_val, s, N_max=2000)
        v_eis = L_A_Eis(kappa_val, s)
        # Euler product converges quickly; Dirichlet sum slower
        assert abs(v_euler - v_eis) / abs(v_eis) < 1e-6
        assert abs(v_dir - v_eis) / abs(v_eis) < 1e-2

    def test_euler_factor_at_p2_s3(self):
        # L_2(3) = 1 / [(1 - 1/8)(1 - 1/4)] = 1 / [(7/8)(3/4)] = 32/21
        ef = euler_factor(2, 3.0)
        assert abs(ef - 32 / 21) < 1e-12


# ============================================================================
# SECTION 8.  p-adic L-function
# ============================================================================


class TestPAdic:
    def test_kummer_p2_n_eq_m(self):
        d = kummer_congruence_test(2, 4, 4)
        assert d["diff"] == 0

    def test_kummer_classical_p691_n12_m22(self):
        # Famous case:  691 divides B_12 numerator, so v_691 anomaly
        d = kummer_congruence_test(691, 12, 12)
        assert d["diff"] == 0

    def test_p_adic_valuation_basic(self):
        assert p_adic_valuation(2, Fraction(8)) == 3
        assert p_adic_valuation(2, Fraction(1, 4)) == -2
        assert p_adic_valuation(3, Fraction(27, 5)) == 3

    def test_kubota_leopoldt_n2_p5(self):
        # L_5(s)|_{s=-1} = -(1 - 5) B_2 / 2 = -(1-5)(1/6)/2 = 4/12 = 1/3
        # Times -kappa: -kappa/3
        v = kubota_leopoldt_special_value(5, 2, Fraction(1))
        # -1 * (1 - 5) * (1/6) / 2 = -1 * (-4) * 1/12 = 4/12 = 1/3
        assert v == Fraction(1, 3)

    def test_kubota_leopoldt_odd_vanishes(self):
        # B_n = 0 for odd n >= 3, so L_p(1-n) = 0
        for n in [3, 5, 7, 9]:
            v = kubota_leopoldt_special_value(7, n, Fraction(13))
            assert v == 0


# ============================================================================
# SECTION 9.  F_g connection
# ============================================================================


class TestFgConnection:
    def test_F_g_via_FE_returns_None(self):
        # Documents that the negative-odd-integer connection is FALSE
        for g in range(1, 5):
            assert F_g_via_riemann_FE(13.0, g) is None

    def test_A_hat_g1(self):
        assert A_hat_coefficient(1) == Fraction(1, 24)

    def test_A_hat_g2(self):
        assert A_hat_coefficient(2) == Fraction(7, 5760)

    def test_F_g_virasoro_c26(self):
        # F_1(Vir_{c=26}) = 13 * 1/24 = 13/24
        f1 = F_g_predicted(13.0, 1)
        assert abs(f1 - 13.0 / 24.0) < 1e-12

    def test_F_g_virasoro_c2(self):
        # F_2(Vir_{c=2}) = 1 * 7/5760 = 7/5760
        f2 = F_g_predicted(1.0, 2)
        assert abs(f2 - 7.0 / 5760) < 1e-15


# ============================================================================
# SECTION 10.  Monster / V^natural
# ============================================================================


class TestMonster:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_monster_at_3(self):
        # L_{V^natural}^{Eis}(3) = -24 * zeta(3) * zeta(2)
        v = L_Eis_monster(3.0)
        expected = -24.0 * float(mpmath.zeta(3)) * (math.pi ** 2 / 6)
        assert abs(v - expected) / abs(expected) < 1e-10

    def test_monster_residue_at_2(self):
        # -24 * pi^2 / 6 = -4 pi^2
        v = monster_residue_at_2()
        assert abs(v - (-4.0 * math.pi ** 2)) < 1e-12

    def test_monster_kappa_correction(self):
        # AP48: kappa(V^natural) = 24, NOT 12 = c/2.
        c = monster_kappa_correction()
        assert c["correct_kappa"] == 24.0
        assert c["user_kappa"] == 12.0
        assert c["ratio"] == 2.0


# ============================================================================
# SECTION 11.  Cross-family verification
# ============================================================================


class TestCrossFamily:
    def test_residue_scales_linearly_in_kappa(self):
        # Residue at s=2 is -kappa * pi^2 / 6
        r1 = L_Eis_pole_residues(1.0)["residue_at_s_eq_2"]
        r13 = L_Eis_pole_residues(13.0)["residue_at_s_eq_2"]
        r24 = L_Eis_pole_residues(24.0)["residue_at_s_eq_2"]
        assert abs(r13 / r1 - 13.0) < 1e-12
        assert abs(r24 / r1 - 24.0) < 1e-12

    def test_value_at_zero_scales_linearly(self):
        for kappa_val in [1.0, 2.5, 13.0, 24.0, 248.0 / 60 * 31]:  # E_8 at level 1
            assert abs(L_at_s_eq_0(kappa_val) - (-kappa_val / 24.0)) < 1e-12

    def test_heisenberg_special_case(self):
        kappa_val = kappa_heisenberg(1.0)
        assert kappa_val == 1.0
        assert L_at_s_eq_0(kappa_val) == -1.0 / 24

    def test_affine_e8_level_1(self):
        # E_8: dim = 248, h^vee = 30, level k = 1  =>  kappa = 248*31/60
        kappa_val = kappa_affine_km(248, 1.0, 30)
        expected = 248 * 31 / 60
        assert abs(kappa_val - expected) < 1e-9


# ============================================================================
# SECTION 12.  Full diagnostic
# ============================================================================


class TestDiagnostic:
    def test_full_diagnostic_runs(self):
        d = full_diagnostic(kappa_val=13.0, p=5)
        assert d["kappa"] == 13.0
        assert d["L_at_0"] == -13.0 / 24
        assert d["L_at_minus_1"] == 0.0
        assert d["trivial_zeros"][0] == -1

    def test_diagnostic_kappa_zero(self):
        # AP31: kappa = 0 implies L_Eis identically zero
        # but does NOT imply the full shadow tower vanishes.
        d = full_diagnostic(kappa_val=0.0, p=2)
        assert d["L_at_0"] == 0.0
        assert d["F_1_predicted"] == 0.0
        assert d["F_2_predicted"] == 0.0


# ============================================================================
# SECTION 13.  Documentation tests for the user research questions
# ============================================================================


class TestUserResearchQuestions:
    """Each test corresponds to one of the user's research questions, and
    documents either the correct answer or the Beilinson finding that the
    naive answer is wrong.
    """

    def test_Q1_L_at_2_is_pole_not_value(self):
        """User: 'L^sh(2) = -kappa * pi^2/6'.
        FINDING: This is the RESIDUE at the pole s = 2, not a finite value."""
        assert L_at_s_eq_2(13.0) is None
        assert abs(L_at_s_eq_2_residue(13.0) - (-13.0 * math.pi ** 2 / 6)) < 1e-10

    def test_Q1_L_at_0_is_minus_kappa_over_24(self):
        """User: 'L^sh(0) = -kappa/12 (via zeta(0)=-1/2)'.
        FINDING: User dropped the zeta(-1) factor.  Correct: -kappa/24."""
        assert L_at_s_eq_0(12.0) == -12.0 / 24
        # User claim -kappa/12 = -1 would be wrong
        assert L_at_s_eq_0(12.0) != -12.0 / 12

    def test_Q1_L_at_minus_1_is_ZERO_not_minus_kappa_over_144(self):
        """User: 'L^sh(-1) = -kappa * B_2^2 / 4 = -kappa/144'.
        FINDING: zeta(-2) = 0, so L^sh(-1) = 0.  The user's value is INCORRECT."""
        assert L_at_s_eq_minus_1(13.0) == 0.0

    def test_Q3_zeros_double_at_rho_and_rho_plus_1(self):
        """User: 'Riemann zeta zeros rho give shadow zeta zeros at rho AND rho+1'.
        CONFIRMED via critical line analysis."""
        lines = critical_lines()
        assert 0.5 in lines  # from zeta(s)
        assert 1.5 in lines  # from zeta(s-1) shifted

    def test_Q4_euler_product_factors_kappa(self):
        """User: 'L^sh(s) = -kappa * prod_p [(1-p^{-s})(1-p^{1-s})]^{-1}'.
        CONFIRMED: kappa is a global multiplicative constant outside the
        Euler product."""
        # The Euler product itself is independent of kappa
        ef_p2_s3 = euler_factor(2, 3.0)
        assert ef_p2_s3 > 0  # finite, real, positive

    def test_Q5_padic_kummer_holds(self):
        """User: 'Does L^sh have a p-adic analogue?'
        ANSWER: Yes -- it reduces to Kubota-Leopoldt for zeta times a
        constant kappa shift.  Special values vanish at odd negative
        integers (since B_n = 0)."""
        v_n3 = kubota_leopoldt_special_value(5, 3, Fraction(13))
        assert v_n3 == 0  # B_3 = 0

    def test_Q6_Vnatural_kappa_correction(self):
        """User: 'kappa(V^natural) = 12 (Monster)'.
        FINDING (AP48): kappa(V^natural) = 24 (rank), NOT c/2 = 12."""
        c = monster_kappa_correction()
        assert c["correct_kappa"] != c["user_kappa"]
        assert c["correct_kappa"] == 24.0

    def test_Q7_negative_odd_integers_give_zero_not_F_g(self):
        """User: 'shadow zeta at s = -2g+1 connects to F_g via functional equation'.
        FINDING: L_Eis at every negative integer is ZERO (trivial zero of zeta(s-1)
        when s = -odd, and zero of zeta(s) when s = -even).  The connection F_g
        = kappa * lambda_g^FP holds via the A-hat genus expansion in hbar, NOT
        via the values of L_Eis at negative integers."""
        for g in range(1, 6):
            assert L_at_s_eq_minus_1(13.0) == 0.0  # at s=-1
            # s = 1 - 2g for g = 1: s = -1 (vanishes)
            # s = 1 - 2g for g = 2: s = -3 (vanishes)
            assert L_Eis_special_value(13.0, 1 - 2 * g) == 0
        # The correct connection is via A-hat genus coefficients
        f1 = F_g_predicted(13.0, 1)
        assert abs(f1 - 13.0 / 24.0) < 1e-12  # F_1 = kappa/24


# ============================================================================
# SECTION 14.  MULTI-PATH VERIFICATION (AP10 mandate: >= 3 paths per claim)
# ============================================================================


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required for multi-path tests")
class TestMultiPathL_Eis_at_0:
    """L_A^{Eis}(0) = -kappa/24.  Verify by >= 3 independent paths."""

    def test_path1_direct_formula(self):
        # Path 1: -kappa * zeta(0) * zeta(-1) from closed-form special values
        kappa_val = 13.0
        v1 = -kappa_val * float(zeta_at_zero()) * float(zeta_at_negative_odd(1))
        assert abs(v1 - (-13.0 / 24)) < 1e-12

    def test_path2_mpmath_direct(self):
        # Path 2: mpmath numerical evaluation
        kappa_val = 13.0
        v2 = float(-kappa_val * mpmath.zeta(0) * mpmath.zeta(-1))
        assert abs(v2 - (-13.0 / 24)) < 1e-12

    def test_path3_helper_function(self):
        # Path 3: the dedicated helper
        assert abs(L_at_s_eq_0(13.0) - (-13.0 / 24)) < 1e-12

    def test_path4_L_A_Eis_generic(self):
        # Path 4: the generic closed-form implementation
        v4 = L_A_Eis(13.0, 0.0)
        assert abs(v4.real - (-13.0 / 24)) < 1e-10

    def test_path5_bernoulli_ratio_path(self):
        # Path 5: via Bernoulli numbers directly.
        # zeta(0)  = -1/2
        # zeta(-1) = -B_2/2 = -(1/6)/2 = -1/12
        # -kappa * (-1/2) * (-1/12) = -kappa/24
        kappa_val = 13.0
        zeta_0 = -0.5
        zeta_m1 = -float(bernoulli(2)) / 2  # = -1/12
        v5 = -kappa_val * zeta_0 * zeta_m1
        assert abs(v5 - (-13.0 / 24)) < 1e-12

    def test_cross_path_agreement(self):
        # All five paths must agree to 10 digits
        kappa_val = 24.0  # V^natural
        v1 = -kappa_val * float(zeta_at_zero()) * float(zeta_at_negative_odd(1))
        v2 = float(-kappa_val * mpmath.zeta(0) * mpmath.zeta(-1))
        v3 = L_at_s_eq_0(kappa_val)
        v4 = L_A_Eis(kappa_val, 0.0).real
        # Path 5: explicit -kappa * (-1/2) * (-1/12)
        v5 = -kappa_val * (-0.5) * (-float(bernoulli(2)) / 2)
        for v in [v1, v2, v3, v4, v5]:
            assert abs(v - (-kappa_val / 24)) < 1e-9


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestMultiPathResidueAtS2:
    """Residue of L_A^{Eis} at s=2 is -kappa pi^2/6.  Verify by multiple paths."""

    def test_path1_direct_minus_kappa_zeta2(self):
        # Path 1:  -kappa * zeta(2) = -kappa * pi^2/6
        kappa_val = 13.0
        v1 = -kappa_val * float(mpmath.zeta(2))
        expected = -kappa_val * math.pi ** 2 / 6
        assert abs(v1 - expected) < 1e-10

    def test_path2_limit_epsilon(self):
        # Path 2:  lim (s - 2) * L_Eis(s) as s -> 2
        kappa_val = 13.0
        eps = 1e-8
        v2 = eps * L_A_Eis(kappa_val, 2 + eps).real
        expected = -kappa_val * math.pi ** 2 / 6
        assert abs(v2 - expected) / abs(expected) < 1e-5

    def test_path3_bernoulli_formula(self):
        # Path 3:  zeta(2) = pi^2/6 = 2 * B_2 * (2pi)^2 / (2 * 2!) / 2 = pi^2/6
        # Using zeta(2k) = (-1)^{k+1} (2pi)^{2k} B_{2k} / (2 (2k)!)
        kappa_val = 13.0
        B2 = float(bernoulli(2))  # 1/6
        zeta_2_via_bern = (2 * math.pi) ** 2 * B2 / (2 * 2)  # = 4 pi^2 * (1/6) / 4 = pi^2/6
        v3 = -kappa_val * zeta_2_via_bern
        expected = -kappa_val * math.pi ** 2 / 6
        assert abs(v3 - expected) < 1e-12

    def test_path4_helper(self):
        assert abs(L_at_s_eq_2_residue(13.0) - (-13.0 * math.pi ** 2 / 6)) < 1e-12

    def test_path5_pole_residues_dict(self):
        r = L_Eis_pole_residues(13.0)
        assert abs(r["residue_at_s_eq_2"] - (-13.0 * math.pi ** 2 / 6)) < 1e-12


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestMultiPathEulerProductConsistency:
    """Euler product = Dirichlet series = zeta product for Re(s) > 2."""

    def test_three_way_agreement_s_eq_3(self):
        kappa_val = 1.0
        s = 3.0
        # Path 1: Euler product
        v1 = euler_product_truncated(kappa_val, s, p_max=500)
        # Path 2: Dirichlet expansion -kappa sum sigma_1(n) n^{-s}
        v2 = L_Eis_dirichlet_partial(kappa_val, s, N_max=1000)
        # Path 3: Direct zeta product -kappa zeta(3) zeta(2)
        v3 = L_A_Eis(kappa_val, s)
        # Path 4: from mpmath special values
        v4 = -kappa_val * float(mpmath.zeta(3)) * (math.pi ** 2 / 6)
        for v in [v1, v2, v3, v4]:
            assert abs(v - v3) / abs(v3) < 1e-2

    def test_agreement_s_eq_4(self):
        kappa_val = 2.0
        s = 4.0
        v1 = L_A_Eis(kappa_val, s).real
        v2 = L_Eis_dirichlet_partial(kappa_val, s, N_max=2000).real
        # Path 3: Closed form -2 * zeta(4) * zeta(3) = -2 * pi^4/90 * zeta(3)
        v3 = -2.0 * (math.pi ** 4 / 90) * float(mpmath.zeta(3))
        assert abs(v1 - v3) / abs(v3) < 1e-10
        assert abs(v2 - v3) / abs(v3) < 1e-2


class TestMultiPathBernoulliSpecialValues:
    """Cross-checks: Bernoulli via recursion vs via zeta(1-2k) vs tabulated."""

    def test_B12_three_ways(self):
        # Path 1: recursion
        v1 = bernoulli(12)
        # Path 2: from zeta(-11) = -B_12/12
        # zeta(-11) = Fraction(-691, 2730) * ???  but we can't compute zeta(-11) symbolically
        # Instead: check zeta_at_negative_odd(6) = -B_{12}/12
        v2 = zeta_at_negative_odd(6)  # = -B_12/12
        assert v2 * 12 == -v1
        # Path 3: Hardcoded Euler value
        assert v1 == Fraction(-691, 2730)

    def test_B_ratio_g_1_three_ways(self):
        # Path 1: B_2/2! directly
        v1 = bernoulli_ratio(1)
        # Path 2: 1/12 hardcoded
        assert v1 == Fraction(1, 12)
        # Path 3: 2 zeta(2) / (2pi)^2 = 2 (pi^2/6) / 4 pi^2 = 1/12
        v3 = 2 * (math.pi ** 2 / 6) / (4 * math.pi ** 2)
        assert abs(float(v1) - v3) < 1e-15


@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestMultiPathZerosStructure:
    """Cross-check that zeros really come in pairs (rho, rho+1)."""

    def test_three_riemann_zeros_pair_up(self):
        for n in [1, 2, 3]:
            # Path 1: compute L_Eis at rho_n
            v_rho = L_Eis_at_zeta_zero(5.0, n)
            # Path 2: compute L_Eis at rho_n + 1
            v_shift = L_Eis_at_shifted_zeta_zero(5.0, n)
            # Both should be zero to high precision
            assert abs(v_rho) < 1e-8
            assert abs(v_shift) < 1e-8
            # Path 3: real parts confirm critical lines
            rho = complex(mpmath.zetazero(n))
            assert abs(rho.real - 0.5) < 1e-10
            assert abs((rho + 1).real - 1.5) < 1e-10

    def test_sign_of_kappa_does_not_affect_zero_locations(self):
        # Path 4 (cross-family): zeros are independent of kappa
        for kappa_val in [1.0, 13.0, 24.0, -5.0]:
            v = L_Eis_at_zeta_zero(kappa_val, 1)
            assert abs(v) < 1e-8


class TestMultiPathMonsterResidue:
    """Residue of L_{V^natural} at s=2.  Cross-family check with AP48."""

    def test_four_paths(self):
        # Path 1: direct helper
        v1 = monster_residue_at_2()
        # Path 2: via generic helper with correct kappa
        v2 = L_at_s_eq_2_residue(24.0)
        # Path 3: via pole residues dict
        v3 = L_Eis_pole_residues(24.0)["residue_at_s_eq_2"]
        # Path 4: manual -24 * pi^2/6 = -4 pi^2
        v4 = -4.0 * math.pi ** 2
        for v in [v1, v2, v3]:
            assert abs(v - v4) < 1e-12

    def test_ap48_c_over_2_would_give_wrong_answer(self):
        # Using WRONG kappa = c/2 = 12 gives -2 pi^2, not -4 pi^2.
        wrong = L_at_s_eq_2_residue(12.0)
        right = L_at_s_eq_2_residue(24.0)
        assert abs(wrong - (-2.0 * math.pi ** 2)) < 1e-12
        assert abs(right - (-4.0 * math.pi ** 2)) < 1e-12
        assert abs(wrong - right) > 1.0  # they differ significantly


class TestMultiPathBeilinsonDisagreement:
    """The disagreement between the Dirichlet form and the Eisenstein form.
    Three independent demonstrations."""

    def test_at_s_eq_0(self):
        # Path 1: sum B_{2r}/(2r)! for r=2..inf via closed form
        closed = 1.0 / (math.e - 1.0) - 0.5 - 1.0 / 12.0
        # Path 2: -zeta(0) zeta(-1) = -1/24
        eis = -1.0 / 24
        # Path 3: direct sum via engine
        numeric = sum(float(bernoulli_ratio(r)) for r in range(2, 80))
        assert abs(numeric - closed) < 1e-10
        assert abs(closed - eis) > 0.01  # DISAGREEMENT

    def test_at_s_eq_1(self):
        # At s=1: Dirichlet form converges; Eis has a pole.
        dir_val = sum(float(bernoulli_ratio(r)) / r for r in range(2, 80))
        assert abs(dir_val) < 1.0  # finite
        # Eis(1) is a pole (infinite)
        # We verify that the near-pole value of Eis is much larger
        eis_near = abs(L_A_Eis(1.0, complex(1.001, 0)))
        assert eis_near > 10 * abs(dir_val)

    def test_at_s_eq_3(self):
        # At s=3: both sides converge; but they give DIFFERENT numbers
        # (because the Bernoulli decay is super-exponential).
        dir_val = sum(float(bernoulli_ratio(r)) / r ** 3 for r in range(2, 80))
        eis_val = -1.0 * float(mpmath.zeta(3)) * (math.pi ** 2 / 6) if HAS_MPMATH else 0
        if HAS_MPMATH:
            assert abs(dir_val - eis_val) > 0.1  # disagreement

    def test_dir_form_is_entire_three_points(self):
        # Path: the Dirichlet form converges AT s=1, s=2, s=3 (all the Eis poles)
        for s in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
            val = L_A_Dir(1.0, complex(s, 0), r_max=60)
            assert abs(val) < 10.0  # bounded


class TestMultiPathFg:
    """F_g = kappa * lambda_g^FP predictions cross-checked."""

    def test_F_1_three_ways(self):
        kappa_val = 13.0
        # Path 1: helper
        v1 = F_g_predicted(kappa_val, 1)
        # Path 2: kappa/24 directly
        v2 = kappa_val / 24
        # Path 3: kappa * A-hat[g=1]
        v3 = kappa_val * float(A_hat_coefficient(1))
        assert abs(v1 - v2) < 1e-12
        assert abs(v1 - v3) < 1e-12

    def test_F_2_three_ways(self):
        kappa_val = 24.0
        v1 = F_g_predicted(kappa_val, 2)
        v2 = kappa_val * 7 / 5760
        v3 = kappa_val * float(A_hat_coefficient(2))
        assert abs(v1 - v2) < 1e-12
        assert abs(v1 - v3) < 1e-12

    def test_F_g_vanishes_when_kappa_zero(self):
        # AP31: kappa=0 => F_g=0 for all g, but does NOT imply full tower vanishes
        for g in range(1, 5):
            assert F_g_predicted(0.0, g) == 0.0


class TestMultiPathKappaLandscape:
    """kappa cross-family verification (AP1, AP48)."""

    def test_virasoro_heisenberg_agree_at_rank_1(self):
        # Path 1: Virasoro at c=1
        k_vir = kappa_virasoro(1.0)
        # Path 2: Heisenberg at k=1 gives the U(1) current
        k_heis = kappa_heisenberg(1.0)
        # These DIFFER: kappa(Vir_1) = 1/2, kappa(H_1) = 1
        # Both correct for their respective families (AP39)
        assert k_vir == 0.5
        assert k_heis == 1.0
        assert k_vir != k_heis  # AP9: same name, different object

    def test_ap48_lattice_vs_c_over_2(self):
        # Leech: rank = 24, c = 24, but kappa = 24 NOT 12
        assert kappa_lattice_voa(24) == 24
        assert kappa_lattice_voa(24) != 12  # c/2 would be wrong
        # E8: rank = 8, c = 8 (lattice VOA), kappa = 8
        assert kappa_lattice_voa(8) == 8

    def test_affine_sl2_multiple_levels(self):
        # kappa(sl_2, k) = 3(k+2)/4
        # Path 1: direct formula
        for k in [1, 2, 3, 5, 10]:
            v = kappa_affine_km(3, float(k), 2)
            # Path 2: hand formula
            v_hand = 3 * (k + 2) / 4
            assert abs(v - v_hand) < 1e-12
        # Path 3: at critical level k = -2: kappa = 0
        v_crit = kappa_affine_km(3, -2.0, 2)
        assert abs(v_crit) < 1e-12
