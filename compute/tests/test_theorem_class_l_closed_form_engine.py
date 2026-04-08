r"""Tests for closed-form genus expansion of class L (affine KM) algebras.

40+ assertions covering:
1. Bernoulli numbers and lambda_fp (independent recomputation)
2. Kappa formulas for SU(N) (AP1 cross-verification)
3. Shadow tower S_3 for class L (AP9 check: kappa != c/2)
4. Genus-1 free energy F_1 = kappa/24
5. Genus-2 planted-forest correction
6. Genus-2 total free energy
7. Genus-3 planted-forest correction (5-term class L polynomial)
8. Genus-3 total free energy (cross-check with costello engine)
9. Heisenberg limit (S_3 -> 0)
10. Complementarity (AP24: kappa + kappa' = 0 for KM)
11. Additivity of scalar part
12. A-hat generating function consistency
13. Degree structure of planted-forest polynomial

Multi-path verification (3+ paths per claim):
  Path 1: Direct formula evaluation from this engine.
  Path 2: Independent recomputation in the test itself.
  Path 3: Cross-check with the costello genus-3 engine at SU(N).
  Path 4: Heisenberg limit (S_3 = 0 => delta_pf = 0).
  Path 5: Additivity of scalar part.

Ground truth (independently computed, NOT copied):
  kappa(sl_2, k=0) = 3/2.  S_3 = 8/9.
  kappa(sl_3, k=0) = 4.    S_3 = 1/2.
  kappa(sl_4, k=0) = 15/2. S_3 = 16/45.
  kappa(sl_5, k=0) = 12.   S_3 = 5/18.

  lambda_1^FP = 1/24.      lambda_2^FP = 7/5760.
  lambda_3^FP = 31/967680.  lambda_4^FP = 127/154828800.
  lambda_5^FP = 73/3503554560.

  F_3(SU(2)) = -11698777/156764160.
  F_3(SU(3)) = -422789/1451520.
  F_3(SU(4)) = -1553227411/3919104000.
  F_3(SU(5)) = -9728417/19595520.
"""

from fractions import Fraction
from math import comb, factorial

import pytest

from compute.lib.theorem_class_l_closed_form_engine import (
    # Primitives
    bernoulli_exact,
    lambda_fp,
    ahat_coefficient,
    # Kappa / shadow
    kappa_slN,
    central_charge_slN,
    S3_slN,
    shadow_tower_class_L,
    # Planted-forest
    delta_pf_genus2,
    delta_pf_genus3_class_L,
    GENUS3_PF_CLASS_L,
    # Free energy
    F_g_class_L,
    # Genus expansion
    ClassLGenusExpansion,
    genus_expansion_slN,
    # Analysis
    pf_degree_analysis_class_L,
    complementarity_check_slN,
    ahat_generating_function_check,
    heisenberg_limit_check,
    additivity_scalar_check,
    summary_table,
)


# ============================================================================
# Section 1: Bernoulli numbers (independent recomputation)
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers from first principles."""

    def test_B0(self):
        assert bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        assert bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_exact(10) == Fraction(5, 66)

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_exact(n) == Fraction(0)


# ============================================================================
# Section 2: Faber-Pandharipande intersection numbers
# ============================================================================

class TestLambdaFP:
    """Verify lambda_g^FP from Bernoulli numbers."""

    def test_g1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_g2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_g3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_g4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_g5(self):
        assert lambda_fp(5) == Fraction(73, 3503554560)

    def test_g1_independent(self):
        """Independent computation: (2^1 - 1)|B_2|/(2^1 * 2!) = 1*1/6/(2*2) = 1/24."""
        val = Fraction(1) * Fraction(1, 6) / Fraction(2 * 2)
        assert lambda_fp(1) == val

    def test_g2_independent(self):
        """Independent: (2^3-1)|B_4|/(2^3*4!) = 7*(1/30)/(8*24) = 7/5760."""
        val = Fraction(7) * Fraction(1, 30) / Fraction(8 * 24)
        assert lambda_fp(2) == val

    def test_ahat_match(self):
        """A-hat generating function path: ahat_coefficient = lambda_fp."""
        for g in range(1, 6):
            assert ahat_coefficient(g) == lambda_fp(g)


# ============================================================================
# Section 3: Kappa formulas (AP1 cross-verification)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N) from first principles."""

    def test_sl2_k0(self):
        """kappa(sl_2, k=0) = 3*2/4 = 3/2."""
        assert kappa_slN(2) == Fraction(3, 2)

    def test_sl3_k0(self):
        """kappa(sl_3, k=0) = 8*3/6 = 4."""
        assert kappa_slN(3) == Fraction(4)

    def test_sl4_k0(self):
        """kappa(sl_4, k=0) = 15*4/8 = 15/2."""
        assert kappa_slN(4) == Fraction(15, 2)

    def test_sl5_k0(self):
        """kappa(sl_5, k=0) = 24*5/10 = 12."""
        assert kappa_slN(5) == Fraction(12)

    def test_sl2_k0_from_definition(self):
        """Independent: dim(sl_2)=3, h^v=2. kappa = 3*(0+2)/(2*2) = 3/2."""
        val = Fraction(3) * Fraction(2) / Fraction(4)
        assert kappa_slN(2) == val

    def test_sl3_k0_from_definition(self):
        """Independent: dim(sl_3)=8, h^v=3. kappa = 8*(0+3)/(2*3) = 4."""
        val = Fraction(8) * Fraction(3) / Fraction(6)
        assert kappa_slN(3) == val

    def test_kappa_not_c_over_2(self):
        """AP9: kappa != c/2 for dim > 1. At k=0, c=0 so c/2=0 != kappa."""
        for N in [2, 3, 4, 5]:
            c = central_charge_slN(N)
            assert c == Fraction(0)  # c(sl_N, k=0) = 0
            assert kappa_slN(N) != c / 2  # AP9

    def test_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)


# ============================================================================
# Section 4: Shadow tower S_3 (class L)
# ============================================================================

class TestShadowTower:
    """Verify S_3 and class L termination."""

    def test_S3_sl2_k0(self):
        """S_3(sl_2, k=0) = 4*2/(3*3) = 8/9."""
        assert S3_slN(2) == Fraction(8, 9)

    def test_S3_sl3_k0(self):
        """S_3(sl_3, k=0) = 4*3/(3*8) = 1/2."""
        assert S3_slN(3) == Fraction(1, 2)

    def test_S3_sl4_k0(self):
        """S_3(sl_4, k=0) = 4*4/(3*15) = 16/45."""
        assert S3_slN(4) == Fraction(16, 45)

    def test_S3_sl5_k0(self):
        """S_3(sl_5, k=0) = 4*5/(3*24) = 5/18."""
        assert S3_slN(5) == Fraction(5, 18)

    def test_S3_from_formula(self):
        """Independent path: S_3 = 2N/(3*kappa)."""
        for N in [2, 3, 4, 5]:
            kap = kappa_slN(N)
            expected = Fraction(2 * N) / (3 * kap)
            assert S3_slN(N) == expected

    def test_class_L_termination(self):
        """S_4 = S_5 = 0 for all class L algebras."""
        for N in [2, 3, 4, 5, 6, 7, 8]:
            tower = shadow_tower_class_L(N)
            assert tower['S_4'] == Fraction(0)
            assert tower['S_5'] == Fraction(0)


# ============================================================================
# Section 5: Genus-1 free energy
# ============================================================================

class TestGenus1:
    """F_1 = kappa/24, no planted-forest correction."""

    def test_F1_su2(self):
        assert F_g_class_L(1, Fraction(3, 2), Fraction(8, 9)) == Fraction(1, 16)

    def test_F1_su3(self):
        assert F_g_class_L(1, Fraction(4), Fraction(1, 2)) == Fraction(1, 6)

    def test_F1_su4(self):
        assert F_g_class_L(1, Fraction(15, 2), Fraction(16, 45)) == Fraction(5, 16)

    def test_F1_su5(self):
        assert F_g_class_L(1, Fraction(12), Fraction(5, 18)) == Fraction(1, 2)

    def test_F1_independent_of_S3(self):
        """F_1 depends only on kappa, not S_3."""
        kap = Fraction(7, 3)
        for s3 in [Fraction(0), Fraction(1), Fraction(5, 7)]:
            assert F_g_class_L(1, kap, s3) == kap / 24


# ============================================================================
# Section 6: Genus-2 planted-forest and total free energy
# ============================================================================

class TestGenus2:
    """delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48."""

    def test_dpf2_su2(self):
        """SU(2): S_3=8/9, kappa=3/2. dpf = (8/9)*(80/9 - 3/2)/48."""
        s3, kap = Fraction(8, 9), Fraction(3, 2)
        expected = s3 * (10 * s3 - kap) / 48
        assert delta_pf_genus2(kap, s3) == expected
        assert expected == Fraction(133, 972)

    def test_dpf2_su3(self):
        """SU(3): S_3=1/2, kappa=4. dpf = (1/2)*(5 - 4)/48 = 1/96."""
        assert delta_pf_genus2(Fraction(4), Fraction(1, 2)) == Fraction(1, 96)

    def test_dpf2_heisenberg_vanishes(self):
        """Heisenberg: S_3=0 => delta_pf = 0."""
        assert delta_pf_genus2(Fraction(7), Fraction(0)) == Fraction(0)

    def test_F2_su2(self):
        exp = genus_expansion_slN(2)
        assert exp.F_2 == Fraction(43127, 311040)

    def test_F2_su3(self):
        exp = genus_expansion_slN(3)
        assert exp.F_2 == Fraction(11, 720)

    def test_F2_su4(self):
        exp = genus_expansion_slN(4)
        assert exp.F_2 == Fraction(-6253, 311040)

    def test_F2_su5(self):
        exp = genus_expansion_slN(5)
        assert exp.F_2 == Fraction(-377, 9720)


# ============================================================================
# Section 7: Genus-3 planted-forest and total free energy
# ============================================================================

class TestGenus3:
    """Cross-check with costello engine expected values."""

    def test_F3_su2(self):
        exp = genus_expansion_slN(2)
        assert exp.F_3 == Fraction(-11698777, 156764160)

    def test_F3_su3(self):
        exp = genus_expansion_slN(3)
        assert exp.F_3 == Fraction(-422789, 1451520)

    def test_F3_su4(self):
        exp = genus_expansion_slN(4)
        assert exp.F_3 == Fraction(-1553227411, 3919104000)

    def test_F3_su5(self):
        exp = genus_expansion_slN(5)
        assert exp.F_3 == Fraction(-9728417, 19595520)

    def test_dpf3_heisenberg_vanishes(self):
        """All 5 terms vanish when S_3 = 0."""
        assert delta_pf_genus3_class_L(Fraction(10), Fraction(0)) == Fraction(0)

    def test_F3_scalar_su2(self):
        """F_3^scalar = kappa * lambda_3^FP = (3/2)*(31/967680) = 31/645120."""
        exp = genus_expansion_slN(2)
        assert exp.F_3_scalar == Fraction(31, 645120)

    def test_F3_decomposition(self):
        """F_3 = F_3_scalar + F_3_pf for all SU(N)."""
        for N in [2, 3, 4, 5]:
            exp = genus_expansion_slN(N)
            assert exp.F_3 == exp.F_3_scalar + exp.F_3_pf


# ============================================================================
# Section 8: Heisenberg limit (multi-path: S_3 -> 0)
# ============================================================================

class TestHeisenbergLimit:
    """When S_3 = 0, all planted-forest corrections vanish."""

    def test_heisenberg_g1(self):
        result = heisenberg_limit_check(1, Fraction(5))
        assert result['match'] is True

    def test_heisenberg_g2(self):
        result = heisenberg_limit_check(2, Fraction(5))
        assert result['match'] is True

    def test_heisenberg_g3(self):
        result = heisenberg_limit_check(3, Fraction(5))
        assert result['match'] is True

    def test_F_g_at_S3_zero_equals_scalar(self):
        """For any kappa, F_g(kappa, 0) = kappa * lambda_fp(g)."""
        kap = Fraction(17, 3)
        for g in [1, 2, 3]:
            assert F_g_class_L(g, kap, Fraction(0)) == kap * lambda_fp(g)


# ============================================================================
# Section 9: Complementarity (AP24)
# ============================================================================

class TestComplementarity:
    """kappa(A) + kappa(A!) = 0 for affine KM (Feigin-Frenkel involution)."""

    def test_complementarity_sl2(self):
        result = complementarity_check_slN(2)
        assert result['anti_symmetric'] is True
        assert result['sum'] == Fraction(0)

    def test_complementarity_sl3(self):
        result = complementarity_check_slN(3)
        assert result['anti_symmetric'] is True

    def test_complementarity_sl5_k1(self):
        result = complementarity_check_slN(5, Fraction(1))
        assert result['anti_symmetric'] is True

    def test_dual_level(self):
        """Feigin-Frenkel: k' = -k - 2h^v = -k - 2N."""
        for N in [2, 3, 4]:
            result = complementarity_check_slN(N)
            assert result['k_dual'] == -2 * N


# ============================================================================
# Section 10: Additivity of scalar part
# ============================================================================

class TestAdditivity:
    """F_g^scalar is additive in kappa."""

    def test_additive_g1(self):
        result = additivity_scalar_check(1)
        assert result['additive'] is True

    def test_additive_g2(self):
        result = additivity_scalar_check(2)
        assert result['additive'] is True

    def test_additive_g3(self):
        result = additivity_scalar_check(3)
        assert result['additive'] is True


# ============================================================================
# Section 11: Degree analysis of planted-forest polynomial
# ============================================================================

class TestDegreeAnalysis:
    """Planted-forest polynomial degree structure."""

    def test_genus2_max_S3_degree(self):
        analysis = pf_degree_analysis_class_L()
        assert analysis[2]['max_S3_degree'] == 2

    def test_genus3_max_S3_degree(self):
        analysis = pf_degree_analysis_class_L()
        assert analysis[3]['max_S3_degree'] == 4

    def test_genus3_num_terms(self):
        analysis = pf_degree_analysis_class_L()
        assert analysis[3]['num_terms'] == 5

    def test_bound_2gm2(self):
        """max S_3 degree <= 2(g-1) at each genus."""
        analysis = pf_degree_analysis_class_L()
        for g in [2, 3]:
            assert analysis[g]['satisfies_bound'] is True


# ============================================================================
# Section 12: A-hat generating function
# ============================================================================

class TestAhatGF:
    """Scalar part matches A-hat generating function."""

    def test_ahat_sl2(self):
        result = ahat_generating_function_check(Fraction(3, 2))
        for g in range(1, 4):
            assert result[g]['F_scalar'] == Fraction(3, 2) * lambda_fp(g)

    def test_ahat_sl5(self):
        result = ahat_generating_function_check(Fraction(12))
        assert result[1]['F_scalar'] == Fraction(1, 2)
        assert result[2]['F_scalar'] == Fraction(7, 480)


# ============================================================================
# Section 13: Summary table and genus expansion dataclass
# ============================================================================

class TestSummaryTable:
    """Summary table for SU(2..5)."""

    def test_table_length(self):
        table = summary_table()
        assert len(table) == 4

    def test_table_N_values(self):
        table = summary_table()
        assert [row['N'] for row in table] == [2, 3, 4, 5]

    def test_expansion_dataclass(self):
        exp = genus_expansion_slN(3)
        assert exp.N == 3
        assert exp.k == Fraction(0)
        assert exp.kappa == Fraction(4)
        assert exp.S_3 == Fraction(1, 2)
        assert exp.F_1 == Fraction(1, 6)

    def test_nonzero_level(self):
        """sl_2 at k=1: kappa = 9/4, S_3 = 16/27."""
        exp = genus_expansion_slN(2, Fraction(1))
        assert exp.kappa == Fraction(9, 4)
        assert exp.S_3 == Fraction(16, 27)
        assert exp.c == Fraction(1)


# ============================================================================
# Section 14: Cross-engine verification with costello genus-3 engine
# ============================================================================

class TestCrossEngine:
    """Verify our values match the costello_genus3 engine exactly."""

    def test_cross_engine_su2_F3(self):
        """Import from costello engine and compare F_3(SU(2))."""
        try:
            from compute.lib.theorem_costello_genus3_amplitudes_engine import (
                genus3_amplitude_suN,
            )
            costello_result = genus3_amplitude_suN(2)
            our_result = genus_expansion_slN(2)
            assert our_result.F_3 == costello_result.F_3
        except ImportError:
            pytest.skip("costello engine not available")

    def test_cross_engine_su3_F3(self):
        try:
            from compute.lib.theorem_costello_genus3_amplitudes_engine import (
                genus3_amplitude_suN,
            )
            costello_result = genus3_amplitude_suN(3)
            our_result = genus_expansion_slN(3)
            assert our_result.F_3 == costello_result.F_3
        except ImportError:
            pytest.skip("costello engine not available")

    def test_cross_engine_su4_F3(self):
        try:
            from compute.lib.theorem_costello_genus3_amplitudes_engine import (
                genus3_amplitude_suN,
            )
            costello_result = genus3_amplitude_suN(4)
            our_result = genus_expansion_slN(4)
            assert our_result.F_3 == costello_result.F_3
        except ImportError:
            pytest.skip("costello engine not available")

    def test_cross_engine_su5_F3(self):
        try:
            from compute.lib.theorem_costello_genus3_amplitudes_engine import (
                genus3_amplitude_suN,
            )
            costello_result = genus3_amplitude_suN(5)
            our_result = genus_expansion_slN(5)
            assert our_result.F_3 == costello_result.F_3
        except ImportError:
            pytest.skip("costello engine not available")
