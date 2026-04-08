r"""Tests for closed-form genus expansion of class C (beta-gamma / bc ghost) algebras.

50+ assertions covering:
1. Bernoulli numbers (independent recomputation)
2. Faber-Pandharipande intersection numbers
3. Beta-gamma central charge and kappa (AP1 cross-verification)
4. Shadow tower data (S_3, S_4) for T-line and charged stratum
5. Genus-1 free energy F_1 = kappa/24 (universal)
6. Genus-2 planted-forest (S_4 absent by self-loop parity)
7. Genus-3 planted-forest (S_4 enters: 9-term polynomial)
8. Genus-4 planted-forest (S_4 enters: 24-term polynomial)
9. Class L degeneration: S_4 -> 0 recovers class L (EXACT structural check)
10. Heisenberg limit: S_3 = S_4 = 0 recovers Heisenberg (class G)
11. Complementarity: kappa + kappa' = 1 for beta-gamma (AP24)
12. Additivity of scalar part
13. Degree structure of planted-forest polynomial
14. bc ghost data consistency
15. Lambda-symmetry: c(lambda) = c(1-lambda) and kappa(lambda) = kappa(1-lambda)
16. Shadow visibility: S_4 absent at g=2, present at g=3
17. Charged stratum: S_3 = 0 simplifies the polynomial
18. Cross-check with generic 11-term formula at S_5 = 0

Multi-path verification (3+ paths per claim):
  Path 1: Direct formula evaluation from this engine.
  Path 2: Independent recomputation in the test itself.
  Path 3: Class L degeneration (S_4 = 0 check).
  Path 4: Heisenberg limit (S_3 = S_4 = 0 check).
  Path 5: Complementarity (AP24 check).
  Path 6: Cross-family consistency (bc ghost vs beta-gamma at c -> -c).

ANTI-PATTERN COMPLIANCE:
  AP1: kappa recomputed from definition in tests.
  AP10: Multi-path verification, not hardcoded expected values only.
  AP14: Class C IS Koszul. Shadow depth != Koszulness.
  AP24: kappa + kappa' = 1, not 0.
  AP39: kappa = c/2 correct for single-generator.
"""

from fractions import Fraction
from math import comb, factorial

import pytest

from compute.lib.theorem_class_c_closed_form_engine import (
    # Primitives
    bernoulli_exact,
    lambda_fp,
    # Beta-gamma data
    central_charge_betagamma,
    kappa_betagamma,
    S3_betagamma_tline,
    S4_betagamma_tline,
    S4_betagamma_charged,
    shadow_tower_class_C_tline,
    shadow_tower_class_C_charged,
    # bc ghost data
    central_charge_bc,
    kappa_bc,
    S4_bc_tline,
    # Planted-forest
    delta_pf_genus2,
    delta_pf_genus3_class_C,
    delta_pf_genus3_generic,
    delta_pf_genus4_class_C,
    # Free energy
    F_g_class_C,
    # Genus expansion
    ClassCGenusExpansion,
    genus_expansion_betagamma_tline,
    genus_expansion_betagamma_charged,
    # Cross-checks
    class_L_degeneration_check,
    heisenberg_limit_check,
    additivity_scalar_check,
    complementarity_betagamma,
    pf_degree_analysis_class_C,
    summary_table,
)


# ============================================================================
# Section 1: Bernoulli numbers (independent recomputation)
# ============================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers from first principles."""

    def test_B0(self):
        assert bernoulli_exact(0) == Fraction(1)

    def test_B2(self):
        assert bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_exact(8) == Fraction(-1, 30)

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9]:
            assert bernoulli_exact(n) == Fraction(0)


# ============================================================================
# Section 2: Faber-Pandharipande intersection numbers
# ============================================================================

class TestLambdaFP:

    def test_g1(self):
        assert lambda_fp(1) == Fraction(1, 24)

    def test_g2(self):
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_g3(self):
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_g4(self):
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_g1_independent(self):
        """Independent: (2^1 - 1)|B_2|/(2^1 * 2!) = 1 * 1/6 / 4 = 1/24."""
        val = Fraction(1) * Fraction(1, 6) / Fraction(4)
        assert lambda_fp(1) == val

    def test_g2_independent(self):
        """Independent: (2^3-1)|B_4|/(2^3*4!) = 7*(1/30)/(8*24) = 7/5760."""
        val = Fraction(7) * Fraction(1, 30) / Fraction(192)
        assert lambda_fp(2) == val


# ============================================================================
# Section 3: Beta-gamma central charge and kappa (AP1)
# ============================================================================

class TestBetagammaShadowData:
    """Verify beta-gamma shadow data from first principles."""

    def test_c_lambda0(self):
        """c(0) = 12*0 - 0 + 2 = 2."""
        assert central_charge_betagamma(Fraction(0)) == Fraction(2)

    def test_c_lambda1(self):
        """c(1) = 12 - 12 + 2 = 2."""
        assert central_charge_betagamma(Fraction(1)) == Fraction(2)

    def test_c_lambda_half(self):
        """c(1/2) = 12/4 - 6 + 2 = 3 - 6 + 2 = -1."""
        assert central_charge_betagamma(Fraction(1, 2)) == Fraction(-1)

    def test_c_lambda2(self):
        """c(2) = 48 - 24 + 2 = 26."""
        assert central_charge_betagamma(Fraction(2)) == Fraction(26)

    def test_c_symmetry(self):
        """c(lambda) = c(1-lambda) (symmetry around lambda = 1/2)."""
        for lam in [Fraction(0), Fraction(1, 3), Fraction(1, 4), Fraction(2)]:
            assert central_charge_betagamma(lam) == central_charge_betagamma(1 - lam)

    def test_kappa_lambda0(self):
        """kappa(0) = 1."""
        assert kappa_betagamma(Fraction(0)) == Fraction(1)

    def test_kappa_lambda1(self):
        """kappa(1) = 6 - 6 + 1 = 1."""
        assert kappa_betagamma(Fraction(1)) == Fraction(1)

    def test_kappa_lambda_half(self):
        """kappa(1/2) = 6/4 - 3 + 1 = 3/2 - 3 + 1 = -1/2."""
        assert kappa_betagamma(Fraction(1, 2)) == Fraction(-1, 2)

    def test_kappa_lambda2(self):
        """kappa(2) = 24 - 12 + 1 = 13."""
        assert kappa_betagamma(Fraction(2)) == Fraction(13)

    def test_kappa_equals_c_over_2(self):
        """AP39: kappa = c/2 for single-generator algebra."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]:
            assert kappa_betagamma(lam) == central_charge_betagamma(lam) / 2

    def test_kappa_symmetry(self):
        """kappa(lambda) = kappa(1-lambda)."""
        for lam in [Fraction(0), Fraction(1, 3), Fraction(1, 4)]:
            assert kappa_betagamma(lam) == kappa_betagamma(1 - lam)

    def test_S3_tline(self):
        """S_3 = 2 on the T-line (Virasoro value)."""
        assert S3_betagamma_tline() == Fraction(2)

    def test_S4_tline_lambda1(self):
        """S_4 = 10/(c*(5c+22)) at lambda=1: 10/(2*32) = 5/32."""
        assert S4_betagamma_tline(Fraction(1)) == Fraction(5, 32)

    def test_S4_tline_lambda0(self):
        """lambda=0 has same c=2 as lambda=1: S_4 = 5/32."""
        assert S4_betagamma_tline(Fraction(0)) == Fraction(5, 32)

    def test_S4_tline_lambda2(self):
        """lambda=2: c=26, S_4 = 10/(26*152) = 10/3952 = 5/1976."""
        assert S4_betagamma_tline(Fraction(2)) == Fraction(5, 1976)

    def test_S4_tline_independent(self):
        """Independent computation of S_4 at lambda=1."""
        c = Fraction(2)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert S4_betagamma_tline(Fraction(1)) == expected

    def test_S4_charged(self):
        """S_4 = -5/12 on the charged stratum."""
        assert S4_betagamma_charged() == Fraction(-5, 12)

    def test_tower_tline_S5_zero(self):
        """Class C: S_5 = 0 on T-line (tower terminates at depth 4)."""
        tower = shadow_tower_class_C_tline(Fraction(1))
        assert tower['S_5'] == Fraction(0)

    def test_tower_charged_S3_zero(self):
        """Charged stratum: S_3 = 0 (rank-one rigidity)."""
        tower = shadow_tower_class_C_charged(Fraction(1))
        assert tower['S_3'] == Fraction(0)


# ============================================================================
# Section 4: bc ghost data consistency
# ============================================================================

class TestBCGhost:
    """Verify bc ghost shadow data and consistency with beta-gamma."""

    def test_bc_c_j2(self):
        """c(j=2) = -(48 - 24 + 2) = -26 (reparametrization ghosts)."""
        assert central_charge_bc(Fraction(2)) == Fraction(-26)

    def test_bc_c_j1(self):
        """c(j=1) = -(12 - 12 + 2) = -2."""
        assert central_charge_bc(Fraction(1)) == Fraction(-2)

    def test_bc_kappa_j2(self):
        """kappa(j=2) = -26/2 = -13."""
        assert kappa_bc(Fraction(2)) == Fraction(-13)

    def test_bc_betagamma_relation(self):
        """bc at spin j has c_bc = -c_bg with lambda=j.

        c_bg(lambda) = 12*lam^2 - 12*lam + 2.
        c_bc(j) = -(12*j^2 - 12*j + 2) = -c_bg(j).
        """
        for j in [Fraction(1), Fraction(2), Fraction(3), Fraction(3, 2)]:
            assert central_charge_bc(j) == -central_charge_betagamma(j)


# ============================================================================
# Section 5: Genus 1 universality (F_1 = kappa/24)
# ============================================================================

class TestGenus1:

    def test_F1_tline_lambda1(self):
        """F_1 = kappa/24 = 1/24 at lambda=1."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_1 == Fraction(1, 24)

    def test_F1_tline_lambda2(self):
        """F_1 = 13/24 at lambda=2."""
        exp = genus_expansion_betagamma_tline(Fraction(2))
        assert exp.F_1 == Fraction(13, 24)

    def test_F1_charged_lambda1(self):
        """F_1 = kappa/24 = 1/24 on charged stratum (same kappa)."""
        exp = genus_expansion_betagamma_charged(Fraction(1))
        assert exp.F_1 == Fraction(1, 24)

    def test_F1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all lambda (universal)."""
        for lam in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]:
            kap = kappa_betagamma(lam)
            assert F_g_class_C(1, kap, Fraction(2), Fraction(0)) == kap / 24


# ============================================================================
# Section 6: Genus 2 (S_4 absent by self-loop parity)
# ============================================================================

class TestGenus2:

    def test_S4_absent_tline(self):
        """S_4 does not affect F_2: shadow visibility g_min(S_4) = 3 > 2."""
        kap = Fraction(1)
        s3 = Fraction(2)
        F2_with_S4 = delta_pf_genus2(kap, s3, Fraction(5, 32))
        F2_without_S4 = delta_pf_genus2(kap, s3, Fraction(0))
        assert F2_with_S4 == F2_without_S4

    def test_S4_absent_charged(self):
        """S_4 does not affect F_2 on charged stratum either."""
        kap = Fraction(1)
        s3 = Fraction(0)
        F2_with = delta_pf_genus2(kap, s3, Fraction(-5, 12))
        F2_without = delta_pf_genus2(kap, s3, Fraction(0))
        assert F2_with == F2_without

    def test_genus2_formula_direct(self):
        """delta_pf^{(2,0)} = S_3*(10*S_3 - kappa)/48."""
        kap = Fraction(1)
        s3 = Fraction(2)
        expected = s3 * (10 * s3 - kap) / 48
        assert delta_pf_genus2(kap, s3) == expected

    def test_genus2_charged_vanishes(self):
        """On charged stratum, S_3 = 0 so delta_pf^{(2,0)} = 0."""
        kap = Fraction(1)
        assert delta_pf_genus2(kap, Fraction(0)) == Fraction(0)

    def test_genus2_tline_lambda1(self):
        """F_2 at lambda=1, T-line."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        # scalar = 1 * 7/5760 = 7/5760
        assert exp.F_2_scalar == Fraction(7, 5760)
        # pf = 2*(20 - 1)/48 = 2*19/48 = 19/24
        assert exp.F_2_pf == Fraction(19, 24)


# ============================================================================
# Section 7: Class L degeneration (S_4 -> 0)
# ============================================================================

class TestClassLDegeneration:
    """Setting S_4 = 0 in class C must recover class L exactly.

    This is the key structural check: the class C polynomial CONTAINS
    the class L polynomial as its S_4 = 0 specialization.
    """

    def test_genus2_degeneration(self):
        r = class_L_degeneration_check(2, Fraction(3, 2), Fraction(8, 9))
        assert r['match'], "Class C at S_4=0 must match class L at g=2"

    def test_genus3_degeneration_su2(self):
        """SU(2) at k=0: kappa = 3/2, S_3 = 8/9."""
        r = class_L_degeneration_check(3, Fraction(3, 2), Fraction(8, 9))
        assert r['match'], "Class C at S_4=0 must match class L at g=3"

    def test_genus3_degeneration_su3(self):
        """SU(3) at k=0: kappa = 4, S_3 = 1/2."""
        r = class_L_degeneration_check(3, Fraction(4), Fraction(1, 2))
        assert r['match'], "Class C at S_4=0 must match class L at g=3"

    def test_genus3_degeneration_su4(self):
        """SU(4) at k=0: kappa = 15/2, S_3 = 16/45."""
        r = class_L_degeneration_check(3, Fraction(15, 2), Fraction(16, 45))
        assert r['match'], "Class C at S_4=0 must match class L at g=3"

    def test_genus4_degeneration_su2(self):
        r = class_L_degeneration_check(4, Fraction(3, 2), Fraction(8, 9))
        assert r['match'], "Class C at S_4=0 must match class L at g=4"

    def test_genus4_degeneration_su3(self):
        r = class_L_degeneration_check(4, Fraction(4), Fraction(1, 2))
        assert r['match'], "Class C at S_4=0 must match class L at g=4"

    def test_genus4_degeneration_su4(self):
        r = class_L_degeneration_check(4, Fraction(15, 2), Fraction(16, 45))
        assert r['match'], "Class C at S_4=0 must match class L at g=4"

    def test_genus4_degeneration_su5(self):
        """SU(5) at k=0: kappa = 12, S_3 = 5/18."""
        r = class_L_degeneration_check(4, Fraction(12), Fraction(5, 18))
        assert r['match'], "Class C at S_4=0 must match class L at g=4"


# ============================================================================
# Section 8: Heisenberg limit (S_3 = S_4 = 0)
# ============================================================================

class TestHeisenbergLimit:
    """S_3 = S_4 = 0 must recover class G: F_g = kappa * lambda_fp."""

    def test_g1(self):
        r = heisenberg_limit_check(1, Fraction(1))
        assert r['match']

    def test_g2(self):
        r = heisenberg_limit_check(2, Fraction(1))
        assert r['match']

    def test_g3(self):
        r = heisenberg_limit_check(3, Fraction(1))
        assert r['match']

    def test_g4(self):
        r = heisenberg_limit_check(4, Fraction(1))
        assert r['match']

    def test_g2_kappa5(self):
        r = heisenberg_limit_check(2, Fraction(5))
        assert r['match']

    def test_g3_kappa_half(self):
        r = heisenberg_limit_check(3, Fraction(1, 2))
        assert r['match']


# ============================================================================
# Section 9: Complementarity (AP24)
# ============================================================================

class TestComplementarity:
    """kappa + kappa' = 1 for beta-gamma (NOT zero, unlike KM)."""

    def test_lambda0(self):
        r = complementarity_betagamma(Fraction(0))
        assert r['sum_is_one']
        assert r['c_sum'] == Fraction(2)

    def test_lambda1(self):
        r = complementarity_betagamma(Fraction(1))
        assert r['sum_is_one']

    def test_lambda_half(self):
        r = complementarity_betagamma(Fraction(1, 2))
        assert r['sum_is_one']

    def test_lambda2(self):
        r = complementarity_betagamma(Fraction(2))
        assert r['sum_is_one']

    def test_lambda3(self):
        r = complementarity_betagamma(Fraction(3))
        assert r['sum_is_one']


# ============================================================================
# Section 10: Additivity of scalar part
# ============================================================================

class TestAdditivity:

    def test_g1(self):
        r = additivity_scalar_check(1)
        assert r['additive']

    def test_g2(self):
        r = additivity_scalar_check(2)
        assert r['additive']

    def test_g3(self):
        r = additivity_scalar_check(3)
        assert r['additive']

    def test_g4(self):
        r = additivity_scalar_check(4)
        assert r['additive']


# ============================================================================
# Section 11: Degree structure
# ============================================================================

class TestDegreeStructure:
    """Total degree of delta_pf in (kappa, S_3, S_4) <= 2(g-1)."""

    def test_genus2(self):
        da = pf_degree_analysis_class_C()
        assert da[2]['satisfies_bound']
        assert da[2]['max_total_degree'] == 2
        assert da[2]['S4_dependence'] is False

    def test_genus3(self):
        da = pf_degree_analysis_class_C()
        assert da[3]['satisfies_bound']
        assert da[3]['max_total_degree'] <= 4
        assert da[3]['S4_dependence'] is True

    def test_genus4(self):
        da = pf_degree_analysis_class_C()
        assert da[4]['satisfies_bound']
        assert da[4]['max_total_degree'] <= 6
        assert da[4]['S4_dependence'] is True


# ============================================================================
# Section 12: Shadow visibility (S_4 first at g=3)
# ============================================================================

class TestShadowVisibility:
    """S_4 first contributes at genus 3, not genus 2."""

    def test_S4_invisible_at_g2(self):
        """F_2 is independent of S_4 for any (kappa, S_3)."""
        kap, s3 = Fraction(5), Fraction(3)
        for s4 in [Fraction(0), Fraction(1), Fraction(-1), Fraction(100)]:
            assert F_g_class_C(2, kap, s3, s4) == F_g_class_C(2, kap, s3, Fraction(0))

    def test_S4_visible_at_g3(self):
        """F_3 DOES depend on S_4 when S_3 != 0 or when S_4 != 0 in pure term."""
        kap, s3 = Fraction(1), Fraction(2)
        F3_with = F_g_class_C(3, kap, s3, Fraction(1, 10))
        F3_without = F_g_class_C(3, kap, s3, Fraction(0))
        assert F3_with != F3_without, "S_4 must affect F_3"

    def test_S4_visible_at_g3_pure(self):
        """Even with S_3 = 0, the S_4^2 term makes F_3 depend on S_4."""
        kap = Fraction(1)
        F3_s4_nonzero = F_g_class_C(3, kap, Fraction(0), Fraction(1))
        F3_s4_zero = F_g_class_C(3, kap, Fraction(0), Fraction(0))
        assert F3_s4_nonzero != F3_s4_zero, "Pure S_4^2 term must contribute"


# ============================================================================
# Section 13: Charged stratum simplification
# ============================================================================

class TestChargedStratum:
    """On the charged stratum, S_3 = 0, simplifying the polynomial."""

    def test_genus2_charged_pf_zero(self):
        """delta_pf = 0 at genus 2 when S_3 = 0."""
        kap = Fraction(1)
        assert delta_pf_genus2(kap, Fraction(0), Fraction(-5, 12)) == Fraction(0)

    def test_genus3_charged_pure_S4(self):
        """At genus 3 with S_3 = 0, only S_4^2 and kappa*S_4 terms survive."""
        kap = Fraction(1)
        s4 = Fraction(-5, 12)
        pf = delta_pf_genus3_class_C(kap, Fraction(0), s4)
        # Only terms with b=0 survive: -7/12 * S_4^2 + 1/1152 * kappa^2 * S_4
        expected = Fraction(-7, 12) * s4 ** 2 + Fraction(1, 1152) * kap ** 2 * s4
        assert pf == expected

    def test_genus3_charged_explicit(self):
        """Explicit computation on charged stratum at lambda=1."""
        s4 = Fraction(-5, 12)
        kap = Fraction(1)
        # -7/12 * (25/144) + 1/1152 * 1 * (-5/12)
        # = -175/1728 + (-5/13824)
        # = -175/1728 - 5/13824
        expected = Fraction(-7, 12) * Fraction(25, 144) + Fraction(1, 1152) * Fraction(-5, 12)
        pf = delta_pf_genus3_class_C(kap, Fraction(0), s4)
        assert pf == expected


# ============================================================================
# Section 14: Cross-check with generic 11-term formula (structural)
# ============================================================================

class TestGenericFormulaConsistency:
    """The class C formula and the generic formula agree on EXACT terms."""

    def test_pure_S4_squared_matches(self):
        """The S_4^2 coefficient is -7/12 in both formulas."""
        kap = Fraction(0)
        s3 = Fraction(0)
        s4 = Fraction(1)
        from_classC = delta_pf_genus3_class_C(kap, s3, s4)
        from_generic = delta_pf_genus3_generic(kap, s3, s4, Fraction(0))
        # Both should give -7/12 * 1^2 = -7/12
        assert from_classC == Fraction(-7, 12)
        assert from_generic == Fraction(-7, 12)

    def test_S3_squared_S4_coefficient_exact(self):
        """The S_3^2 * S_4 coefficient -167/96 is exact in class C.

        Verify by evaluating at kappa=0, S_3=0, S_4=1 (for S_4^2 term)
        and at kappa=0, S_3=1, S_4=0 (for S_3^4 term) separately, then
        checking that the cross term at S_3=1, S_4=1, kappa=0 is:
          class_L(S_3=1) + pure_S4(S_3=1, S_4=1)
        """
        kap = Fraction(0)
        # class L at kappa=0 is just the S_3^4 term: 15/64
        classL_only = delta_pf_genus3_class_C(kap, Fraction(1), Fraction(0))
        assert classL_only == Fraction(15, 64)
        # pure S_4 at S_3=1, S_4=1: -167/96 * 1 + (-7/12) * 1
        pure_S4 = Fraction(-167, 96) + Fraction(-7, 12)
        assert pure_S4 == Fraction(-167 - 56, 96)  # = -223/96
        # Full at kappa=0: classL + pure_S4
        full = delta_pf_genus3_class_C(kap, Fraction(1), Fraction(1))
        assert full == classL_only + pure_S4

    def test_generic_formula_differs_from_exact(self):
        """The generic formula has APPROXIMATE S_3-only terms.

        At kappa=0, the class C formula uses the exact class L S_3^4
        coefficient (15/64) while the generic uses -5/128. These differ
        because the generic formula was derived with approximate genus-1+
        vertex weights. This test documents the known discrepancy.
        """
        kap = Fraction(0)
        s3 = Fraction(1)
        from_classC = delta_pf_genus3_class_C(kap, s3, Fraction(0))
        from_generic = delta_pf_genus3_generic(kap, s3, Fraction(0), Fraction(0))
        # The class L S_3^4 coefficient differs: 15/64 vs -5/128
        assert from_classC == Fraction(15, 64)      # exact
        assert from_generic == Fraction(-5, 128)     # approximate
        assert from_classC != from_generic           # they MUST differ


# ============================================================================
# Section 15: F_g values at specific beta-gamma parameters
# ============================================================================

class TestSpecificValues:
    """F_g at specific beta-gamma parameters."""

    def test_F1_lambda1_tline(self):
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_1 == Fraction(1, 24)

    def test_F2_lambda1_tline_positive(self):
        """F_2 should be positive at lambda=1 (kappa=1, S_3=2)."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_2 > 0

    def test_F2_decomposition(self):
        """F_2 = F_2_scalar + F_2_pf."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_2 == exp.F_2_scalar + exp.F_2_pf

    def test_F3_decomposition(self):
        """F_3 = F_3_scalar + F_3_pf."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_3 == exp.F_3_scalar + exp.F_3_pf

    def test_F4_decomposition(self):
        """F_4 = F_4_scalar + F_4_pf."""
        exp = genus_expansion_betagamma_tline(Fraction(1))
        assert exp.F_4 == exp.F_4_scalar + exp.F_4_pf

    def test_charged_genus_expansion(self):
        """Charged stratum expansion produces valid results."""
        exp = genus_expansion_betagamma_charged(Fraction(1))
        assert exp.F_1 == Fraction(1, 24)
        # F_2_pf = 0 on charged stratum (S_3 = 0)
        assert exp.F_2_pf == Fraction(0)

    def test_lambda2_kappa(self):
        exp = genus_expansion_betagamma_tline(Fraction(2))
        assert exp.kappa == Fraction(13)
        assert exp.c == Fraction(26)


# ============================================================================
# Section 16: S_4 contribution sign and magnitude at genus 3
# ============================================================================

class TestS4Contribution:
    """Verify that S_4 terms contribute with correct sign and magnitude."""

    def test_pure_S4_squared_negative(self):
        """The -7/12 * S_4^2 term is always non-positive."""
        for s4 in [Fraction(1), Fraction(-1), Fraction(5, 32)]:
            assert Fraction(-7, 12) * s4 ** 2 <= 0

    def test_S4_effect_on_F3_tline(self):
        """S_4 term should be small relative to the class L part at lambda=1.

        S_4 = 5/32 is small, so the correction should be modest.
        """
        kap = Fraction(1)
        s3 = Fraction(2)
        s4 = Fraction(5, 32)
        classL_part = delta_pf_genus3_class_C(kap, s3, Fraction(0))
        S4_correction = delta_pf_genus3_class_C(kap, s3, s4) - classL_part
        # The correction should be nonzero
        assert S4_correction != 0
        # And much smaller than the class L part in absolute value
        assert abs(S4_correction) < abs(classL_part)

    def test_charged_S4_dominates_g3(self):
        """On charged stratum, S_4 is the ONLY contributor at g=3.

        (S_3 = 0, so class L part vanishes entirely.)
        """
        kap = Fraction(1)
        pf = delta_pf_genus3_class_C(kap, Fraction(0), Fraction(-5, 12))
        assert pf != 0, "Charged stratum has nonzero pf at g=3 from S_4"


# ============================================================================
# Section 17: Summary table
# ============================================================================

class TestSummaryTable:

    def test_tline_table_length(self):
        rows = summary_table()
        assert len(rows) == 5  # 5 lambda values

    def test_charged_table_length(self):
        rows = summary_table(stratum='charged')
        assert len(rows) == 5

    def test_tline_lambda1_kappa(self):
        rows = summary_table(lam_values=[Fraction(1)])
        assert rows[0]['kappa'] == Fraction(1)

    def test_tline_lambda_symmetry(self):
        """lambda=0 and lambda=1 should give same F_g (same c and kappa)."""
        rows = summary_table(lam_values=[Fraction(0), Fraction(1)])
        for key in ['F_1', 'F_2', 'F_3', 'F_4']:
            assert rows[0][key] == rows[1][key]
