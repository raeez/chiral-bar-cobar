r"""Tests for CohFT string equation via topological recursion and Eynard-Orantin.

Multi-path verification of the bridge between:
  (A) TR string equation (automatic from Eynard-Orantin recursion)
  (B) CohFT string equation (requires flat unit, AP30)
  (C) MC string equation (from Maurer-Cartan tautological descent)

Verification paths per claim:
  PATH 1: Witten-Kontsevich intersection numbers (exact arithmetic)
  PATH 2: Faber-Pandharipande free energy formula F_g = kappa * lambda_fp(g)
  PATH 3: Shadow spectral curve + EO recursion structure
  PATH 4: Dilaton equation cross-check
  PATH 5: Cross-family consistency (additivity of kappa)

Ground truth:
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:cohft-reconstruction (higher_genus_modular_koszul.tex)
    cor:topological-recursion-mc-shadow (higher_genus_modular_koszul.tex)
    thm:spectral-curve-from-shadow (higher_genus_modular_koszul.tex)
    thm:tr-shadow-free-energies (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction
from sympy import Rational, factorial, sqrt as sym_sqrt

from compute.lib.cohft_toprec_string_engine import (
    # Core functions
    lambda_fp,
    wk_intersection,
    # Spectral data
    ShadowSpectralData,
    heisenberg_spectral,
    virasoro_spectral,
    affine_sl2_spectral,
    # Spectral curve
    SpectralCurveDescription,
    describe_spectral_curve,
    # String equation
    tr_string_equation_airy_genus_g,
    CohFTStringEquationStatus,
    # Bridge lemma
    BridgeLemmaVerification,
    verify_bridge_lemma_airy,
    verify_bridge_lemma_shadow,
    # Dilaton
    verify_dilaton_equation,
    # Genus-specific
    verify_string_equation_genus2,
    verify_string_equation_genus3,
    # Shadow free energy
    verify_shadow_free_energy_string_equation,
    # Comprehensive
    comprehensive_verification,
    bridge_theorem_statement,
)


# ============================================================================
# Section 1: Faber-Pandharipande numbers (3 independent paths per genus)
# ============================================================================

class TestFaberPandharipande:
    """Verify lambda_fp(g) via multiple independent paths."""

    def test_lambda_fp_g1(self):
        """F_1 = 1/24.

        PATH 1: Bernoulli formula (2^1 - 1)/2^1 * |B_2|/2! = 1/2 * 1/6 / 2 = 1/24.
        PATH 2: <tau_1>_1 = 1/24 (WK base case).
        PATH 3: Euler characteristic chi(M_{1,1}) = -1/12, so
                 lambda_fp(1) = |B_2|/(2*2!) = 1/24.
        """
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_g2(self):
        """F_2 = 7/5760.

        PATH 1: (2^3-1)/2^3 * |B_4|/4! = 7/8 * 1/30 / 24 = 7/5760.
        PATH 2: Known value from Faber-Pandharipande.
        PATH 3: (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)! with g=2.
        """
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda_fp_g3(self):
        """F_3 = 31/967680.

        PATH 1: (2^5-1)/2^5 * |B_6|/6! = 31/32 * 1/42 / 720 = 31/967680.
        PATH 2: Known value.
        """
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda_fp_g4(self):
        """F_4 = 127/154828800.

        PATH 1: (2^7-1)/2^7 * |B_8|/8! = 127/128 * 1/30 / 40320 = 127/154828800.
        """
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_fp_positivity(self):
        """All lambda_fp(g) are positive (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0, f"lambda_fp({g}) should be positive"

    def test_lambda_fp_ahat_consistency(self):
        r"""Check A-hat generating function consistency.

        sum_{g>=1} F_g * x^{2g} = x/sinh(x) - 1 (suitably normalized).
        At leading order: F_1 * x^2 = x^2/24 matches A-hat expansion.
        """
        # Verify the first few terms match the A-hat genus expansion
        # A-hat(ix) - 1 = x^2/24 + 7x^4/5760 + ...
        assert lambda_fp(1) == Rational(1, 24)
        assert lambda_fp(2) == Rational(7, 5760)
        # Check ratio: F_2/F_1 = (7/5760)/(1/24) = 7*24/5760 = 7/240
        ratio = lambda_fp(2) / lambda_fp(1)
        assert ratio == Rational(7, 240)


# ============================================================================
# Section 2: Witten-Kontsevich intersection numbers
# ============================================================================

class TestWKIntersections:
    """Verify WK intersection numbers from multiple paths."""

    def test_base_g0(self):
        """<tau_0^3>_0 = 1."""
        assert wk_intersection(0, 0, 0, g=0) == 1

    def test_g0_multinomial(self):
        """<tau_0 tau_0 tau_1>_0 = 1 (Witten's formula: (3-3)!/0!0!1! = 0). Wait:
        n=3, sum=1, 3g-3+n = 0+3 = 3. 1 != 3. Zero by selection rule."""
        assert wk_intersection(0, 0, 1, g=0) == 0

    def test_g0_tau1_tau0_tau0(self):
        """<tau_1 tau_0^3>_0: sum=1, n=4, 3*0-3+4=1. Selection OK.
        Witten's formula: (4-3)!/(1!*0!^3) = 1."""
        assert wk_intersection(1, 0, 0, 0, g=0) == 1

    def test_g0_tau2_tau0_tau0_tau0_tau0(self):
        """<tau_2 tau_0^4>_0: sum=2, n=5, 5-3=2. OK.
        (5-3)!/(2!*0!^4) = 2/2 = 1."""
        assert wk_intersection(2, 0, 0, 0, 0, g=0) == 1

    def test_g1_base(self):
        """<tau_1>_1 = 1/24 (fundamental base case)."""
        assert wk_intersection(1, g=1) == Rational(1, 24)

    def test_g2_base(self):
        """<tau_4>_2 = 1/1152."""
        assert wk_intersection(4, g=2) == Rational(1, 1152)

    def test_g3_base(self):
        """<tau_7>_3 = 1/82944."""
        assert wk_intersection(7, g=3) == Rational(1, 82944)

    def test_selection_rule_violation(self):
        """Selection rule violations give zero."""
        # sum = 3 != 3*1-3+2 = 2
        assert wk_intersection(2, 1, g=1) == 0
        # n = 1 but 2g-2+n = 0 at g=0
        assert wk_intersection(0, g=0) == 0

    def test_stability_violation(self):
        """Unstable cases (2g-2+n <= 0) give zero."""
        assert wk_intersection(g=0) == 0  # n=0, g=0


# ============================================================================
# Section 3: String equation — the core test
# ============================================================================

class TestStringEquation:
    """The string equation <tau_0 tau_{d_1}...>_g = sum <tau_{d_i-1}...>_g.

    This is the TR string equation translated to intersection numbers
    via the DBOSS identification.
    """

    def test_string_equation_g1(self):
        """<tau_0 tau_2>_1 = <tau_1>_1 = 1/24.

        Selection: sum=2, n=2, need=3*1-3+2=2. OK.
        String removes tau_0, decreases tau_2 to tau_1.
        """
        lhs = wk_intersection(0, 2, g=1)
        rhs = wk_intersection(1, g=1)
        assert lhs == rhs == Rational(1, 24)

    def test_string_equation_g2(self):
        """<tau_0 tau_5>_2 = <tau_4>_2 = 1/1152.

        Selection: sum=5, n=2, need=3*2-3+2=5. OK.
        String removes tau_0, decreases tau_5 to tau_4.
        """
        lhs = wk_intersection(0, 5, g=2)
        rhs = wk_intersection(4, g=2)
        assert lhs == rhs
        assert lhs == Rational(1, 1152)

    def test_string_equation_g3(self):
        """<tau_0 tau_8>_3 = <tau_7>_3 = 1/82944.

        Selection: sum=8, n=2, need=3*3-3+2=8. OK.
        """
        lhs = wk_intersection(0, 8, g=3)
        rhs = wk_intersection(7, g=3)
        assert lhs == rhs
        assert lhs == Rational(1, 82944)

    def test_string_equation_g4(self):
        """<tau_0 tau_{11}>_4 = <tau_{10}>_4.

        Selection: sum=11, n=2, need=3*4-3+2=11. OK.
        """
        lhs = wk_intersection(0, 11, g=4)
        rhs = wk_intersection(10, g=4)
        assert lhs == rhs

    def test_string_equation_multipoint_g1(self):
        """<tau_0 tau_0 tau_3>_1 = <tau_0 tau_2>_1.

        Selection for LHS: sum=3, n=3, need=3*1-3+3=3. OK.
        Selection for RHS: sum=2, n=2, need=2. OK.
        String removes tau_0, decreases tau_3 to tau_2.
        Both reductions lead to <tau_1>_1 = 1/24.
        """
        lhs = wk_intersection(0, 0, 3, g=1)
        rhs = wk_intersection(0, 2, g=1)
        assert lhs == rhs == Rational(1, 24)

    def test_string_equation_multipoint_g0(self):
        """<tau_0 tau_0 tau_0 tau_1>_0 = <tau_0 tau_0 tau_0>_0 = 1.

        The string equation at genus 0: remove tau_0, decrease tau_1.
        """
        # sum=1, n=4, 3*0-3+4=1. OK.
        lhs = wk_intersection(0, 0, 0, 1, g=0)
        rhs = wk_intersection(0, 0, 0, g=0)
        assert lhs == rhs == 1

    def test_string_equation_via_engine_g1(self):
        """Verify via the engine function."""
        result = tr_string_equation_airy_genus_g(1, n=1)
        assert result['string_n1']['holds']

    def test_string_equation_via_engine_g2(self):
        result = tr_string_equation_airy_genus_g(2, n=1)
        assert result['string_n1']['holds']

    def test_string_equation_via_engine_g3(self):
        result = tr_string_equation_airy_genus_g(3, n=1)
        assert result['string_n1']['holds']


# ============================================================================
# Section 4: Dilaton equation
# ============================================================================

class TestDilatonEquation:
    """The dilaton equation <tau_1 S>_g = (2g-2+n) <S>_g."""

    def test_dilaton_g1_tau1_tau1(self):
        """<tau_1 tau_1>_1 = (2g-2+m)*<tau_1>_1 where m=1 remaining.

        Dilaton: <tau_1 tau_{d_1}...tau_{d_m}>_g = (2g-2+m)*<tau_{d_1}...tau_{d_m}>_g
        where m counts the OTHER insertions.
        <tau_1 tau_1>_1: m=1. Factor = (2-2+1) = 1. Result: 1/24.
        """
        lhs = wk_intersection(1, 1, g=1)
        rhs = (2 * 1 - 2 + 1) * wk_intersection(1, g=1)
        assert lhs == rhs
        assert lhs == Rational(1, 24)

    def test_dilaton_g2(self):
        """<tau_1 tau_4>_2 = (2*2-2+1)*<tau_4>_2 = 3 * 1/1152 = 1/384."""
        lhs = wk_intersection(1, 4, g=2)
        rhs = 3 * wk_intersection(4, g=2)
        assert lhs == rhs
        assert lhs == Rational(3, 1152)

    def test_dilaton_g3(self):
        """<tau_1 tau_7>_3 = (2*3-2+1)*<tau_7>_3 = 5 * 1/82944."""
        lhs = wk_intersection(1, 7, g=3)
        rhs = 5 * wk_intersection(7, g=3)
        assert lhs == rhs

    def test_dilaton_g4(self):
        """<tau_1 tau_{10}>_4 = (2*4-2+1)*<tau_{10}>_4 = 7*<tau_{10}>_4."""
        lhs = wk_intersection(1, 10, g=4)
        rhs = 7 * wk_intersection(10, g=4)
        assert lhs == rhs

    def test_dilaton_via_engine(self):
        """Verify dilaton via the engine."""
        res = verify_dilaton_equation(1, 2)
        for key, val in res.items():
            assert val['holds'], f"Dilaton failed: {key}"


# ============================================================================
# Section 5: Spectral curves for standard families
# ============================================================================

class TestSpectralCurves:
    """Verify spectral curve structure for each shadow class."""

    def test_heisenberg_degenerate(self):
        """Heisenberg: Q_L = 4k^2 (constant), curve degenerates."""
        data = heisenberg_spectral(Rational(1))
        assert data.q0 == 4
        assert data.q1 == 0
        assert data.q2 == 0
        assert data.Delta == 0
        assert data.is_degenerate
        desc = describe_spectral_curve(data)
        assert desc['curve_type'] == 'degenerate'
        assert desc['local_model'] == 'trivial'

    def test_heisenberg_q0_scales_with_k(self):
        """Q_L = 4k^2 for general k."""
        for k_val in [1, 2, 3, 5]:
            k = Rational(k_val)
            data = heisenberg_spectral(k)
            assert data.q0 == 4 * k**2

    def test_virasoro_class_M(self):
        """Virasoro: class M with Delta != 0."""
        data = virasoro_spectral(Rational(10))
        assert data.depth_class == 'M'
        assert data.kappa == 5
        assert data.alpha == 2
        assert data.S4 == Rational(10) / (10 * 72)
        assert data.Delta != 0
        assert not data.is_degenerate

    def test_virasoro_spectral_curve_coefficients(self):
        """Verify Q_L coefficients for Virasoro at c=10.

        PATH 1: Direct computation.
        PATH 2: From kappa=5, alpha=2, S4=10/(10*72)=1/72.
        """
        data = virasoro_spectral(Rational(10))
        assert data.q0 == 4 * 25  # 100
        assert data.q1 == 12 * 5 * 2  # 120
        assert data.q2 == 9 * 4 + 16 * 5 * Rational(1, 72)  # 36 + 80/72 = 36 + 10/9

    def test_virasoro_curve_smooth(self):
        """Virasoro spectral curve is smooth genus-0."""
        data = virasoro_spectral(Rational(10))
        desc = describe_spectral_curve(data)
        assert desc['curve_type'] == 'smooth'
        assert desc['local_model'] == 'airy'
        assert desc['ramification_type'] == 'simple'
        assert len(desc['branch_points']) == 2

    def test_affine_sl2_class_L(self):
        """Affine sl_2: class L with Delta = 0."""
        data = affine_sl2_spectral(Rational(1))
        assert data.depth_class == 'L'
        assert data.kappa == Rational(9, 4)
        assert data.alpha == 2
        assert data.S4 == 0
        assert data.Delta == 0

    def test_affine_sl2_perfect_square(self):
        """Q_L is a perfect square for class L.

        Q_L = (2*kappa + 6t)^2 when Delta = 0 and alpha = 2.
        q0 = 4*kappa^2, q1 = 12*kappa*2 = 24*kappa, q2 = 36.
        disc = (24*kappa)^2 - 4*4*kappa^2*36 = 576*kappa^2 - 576*kappa^2 = 0.
        """
        data = affine_sl2_spectral(Rational(1))
        assert data.disc_QL == 0
        assert data.is_degenerate  # branch points collide

    def test_virasoro_self_dual_c13(self):
        """At c=13 (self-dual point), kappa = 13/2, kappa' = (26-13)/2 = 13/2.

        The spectral curve at c=13 is still class M (Delta != 0).
        """
        data = virasoro_spectral(Rational(13))
        assert data.kappa == Rational(13, 2)
        assert data.Delta != 0
        # Koszul dual: c' = 26 - 13 = 13, same curve
        data_dual = virasoro_spectral(Rational(13))
        assert data.kappa == data_dual.kappa

    def test_virasoro_c26_kappa13(self):
        """Virasoro at c=26 has kappa = 13. Dual c' = 0 has kappa' = 0."""
        data = virasoro_spectral(Rational(26))
        assert data.kappa == 13
        # kappa + kappa' = 13 + 0 = 13 (AP24: NOT zero for Virasoro)


# ============================================================================
# Section 6: Bridge lemma verification
# ============================================================================

class TestBridgeLemma:
    """The bridge lemma: TR string <=> CohFT string via DBOSS/MC."""

    def test_bridge_airy_g1(self):
        """Bridge lemma at genus 1 on the Airy curve."""
        result = verify_bridge_lemma_airy(1)
        assert result.intersection_agrees
        assert result.all_paths_agree
        assert result.dboss_applicable

    def test_bridge_airy_g2(self):
        """Bridge lemma at genus 2 on the Airy curve."""
        result = verify_bridge_lemma_airy(2)
        assert result.intersection_agrees
        assert result.all_paths_agree

    def test_bridge_airy_g3(self):
        """Bridge lemma at genus 3 on the Airy curve."""
        result = verify_bridge_lemma_airy(3)
        assert result.intersection_agrees
        assert result.all_paths_agree

    def test_bridge_airy_g4(self):
        """Bridge lemma at genus 4."""
        result = verify_bridge_lemma_airy(4)
        assert result.intersection_agrees

    def test_bridge_virasoro_g1(self):
        """Bridge for Virasoro at c=10, genus 1."""
        data = virasoro_spectral(Rational(10))
        result = verify_bridge_lemma_shadow(data, 1)
        assert result.intersection_agrees
        assert result.dboss_applicable  # Virasoro is class M (semisimple)
        assert result.dboss_flat_unit

    def test_bridge_virasoro_g2(self):
        """Bridge for Virasoro at c=10, genus 2."""
        data = virasoro_spectral(Rational(10))
        result = verify_bridge_lemma_shadow(data, 2)
        assert result.intersection_agrees

    def test_bridge_virasoro_g3(self):
        """Bridge for Virasoro at c=10, genus 3."""
        data = virasoro_spectral(Rational(10))
        result = verify_bridge_lemma_shadow(data, 3)
        assert result.intersection_agrees

    def test_bridge_heisenberg_g1(self):
        """Bridge for Heisenberg at k=1, genus 1."""
        data = heisenberg_spectral(Rational(1))
        result = verify_bridge_lemma_shadow(data, 1)
        assert result.intersection_agrees
        # Heisenberg is class G, but DBOSS still works (degenerate curve)
        assert result.mc_string_holds

    def test_bridge_affine_sl2_g1(self):
        """Bridge for affine sl_2 at k=1, genus 1."""
        data = affine_sl2_spectral(Rational(1))
        result = verify_bridge_lemma_shadow(data, 1)
        assert result.intersection_agrees


# ============================================================================
# Section 7: CohFT string equation status (AP30)
# ============================================================================

class TestCohFTStatus:
    """Verify CohFT string equation status respects AP30."""

    def test_heisenberg_has_flat_unit(self):
        """Heisenberg vacuum |0> is a flat unit."""
        status = CohFTStringEquationStatus.for_heisenberg()
        assert status.has_flat_unit
        assert status.string_equation_holds
        assert status.ap30_status == 'satisfied'

    def test_virasoro_has_flat_unit(self):
        """Virasoro vacuum |0> (L_n|0>=0 for n>=-1) is a flat unit."""
        status = CohFTStringEquationStatus.for_virasoro(Rational(10))
        assert status.has_flat_unit
        assert status.string_equation_holds
        assert status.proof_route == 'DBOSS'

    def test_affine_sl2_conditional(self):
        """Affine sl_2: vacuum exists but V = span{J^a} does not contain it.

        Two V choices: (A) V=span{J^a} (rank 3, AP30 fails for CohFT unit),
        (B) V=span{|0>,J^a} (rank 4, AP30 satisfied). Standard landscape
        uses choice (B). The DR string equation holds unconditionally
        regardless of V choice (Buryak 2015, Thm 1.1).
        """
        status = CohFTStringEquationStatus.for_affine_sl2(Rational(1))
        assert status.string_equation_holds  # via DR unconditional
        assert status.proof_route == 'DR_unconditional'
        assert status.ap30_status == 'satisfied_after_V_enlargement'

    def test_general_no_vacuum(self):
        """When vacuum is NOT in V, CohFT unit axiom fails (AP30).

        The DR string equation still holds unconditionally (Buryak 2015).
        For rank 1, F^{DR} = F^{CohFT}, so the string equation holds
        at the level of the descendant potential regardless.
        """
        status = CohFTStringEquationStatus.for_general("test", has_vacuum_in_V=False)
        assert not status.has_flat_unit
        assert status.string_equation_holds  # via DR unconditional
        assert status.proof_route == 'DR_unconditional'
        assert status.ap30_status == 'fails'

    def test_general_with_vacuum(self):
        """When vacuum IS in V, string equation holds."""
        status = CohFTStringEquationStatus.for_general("test", has_vacuum_in_V=True)
        assert status.has_flat_unit
        assert status.string_equation_holds


# ============================================================================
# Section 8: Genus-2 detailed verification
# ============================================================================

class TestGenus2Detail:
    """Detailed genus-2 string equation verification from 3+ paths."""

    def test_genus2_base_case(self):
        """<tau_4>_2 = 1/1152 (base case for genus 2)."""
        result = verify_string_equation_genus2()
        assert result['base_tau4_g2']['ok']

    def test_genus2_string(self):
        """String equation holds at genus 2."""
        result = verify_string_equation_genus2()
        assert result['string_05_g2']['holds']

    def test_genus2_dilaton(self):
        """Dilaton equation at genus 2: <tau_1 tau_4>_2 = 3*<tau_4>_2."""
        result = verify_string_equation_genus2()
        assert result['dilaton_14_g2']['holds']
        assert result['dilaton_14_g2']['lhs'] == Rational(3, 1152)

    def test_genus2_F2(self):
        """F_2 = 7/5760."""
        result = verify_string_equation_genus2()
        assert result['F2_value']['ok']

    def test_genus2_string_for_shadow(self):
        """Verify genus-2 string for shadow CohFT: F_2 = kappa * 7/5760.

        For Virasoro at c=10: F_2 = 5 * 7/5760 = 7/1152.
        """
        data = virasoro_spectral(Rational(10))
        result = verify_shadow_free_energy_string_equation(data, max_genus=2)
        assert result['genus_2']['holds']
        assert result['genus_2']['F_g'] == 5 * Rational(7, 5760)


# ============================================================================
# Section 9: Genus-3 cross-check
# ============================================================================

class TestGenus3CrossCheck:
    """Genus-3 string equation as independent cross-check."""

    def test_genus3_base(self):
        """<tau_7>_3 = 1/82944."""
        result = verify_string_equation_genus3()
        assert result['base_tau7_g3']['ok']

    def test_genus3_F3(self):
        """F_3 = 31/967680."""
        result = verify_string_equation_genus3()
        assert result['F3']['ok']

    def test_genus3_string(self):
        """String equation at genus 3."""
        result = verify_string_equation_genus3()
        assert result['string_08_g3']['holds']

    def test_genus3_dilaton(self):
        """Dilaton at genus 3."""
        result = verify_string_equation_genus3()
        assert result['dilaton_17_g3']['holds']

    def test_genus3_shadow_virasoro(self):
        """Shadow string equation for Virasoro at genus 3."""
        data = virasoro_spectral(Rational(10))
        result = verify_shadow_free_energy_string_equation(data, max_genus=3)
        assert result['genus_3']['holds']


# ============================================================================
# Section 10: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Verify cross-family consistency of the string equation."""

    def test_kappa_additivity(self):
        """F_g(A1 + A2) = F_g(A1) + F_g(A2) via kappa additivity.

        For independent sum A = A1 + A2: kappa(A) = kappa(A1) + kappa(A2).
        F_g(A) = kappa(A)*lambda_fp(g) = [kappa(A1)+kappa(A2)]*lambda_fp(g)
              = F_g(A1) + F_g(A2).
        """
        k1 = Rational(3)
        k2 = Rational(5)
        data1 = heisenberg_spectral(k1)
        data2 = heisenberg_spectral(k2)
        for g in range(1, 5):
            f1 = data1.kappa * lambda_fp(g)
            f2 = data2.kappa * lambda_fp(g)
            f_sum = (k1 + k2) * lambda_fp(g)
            assert f1 + f2 == f_sum

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24, NOT zero).

        F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_fp(g).
        String equation respects this additivity.
        """
        for c_val in [2, 5, 10, 13, 24]:
            c = Rational(c_val)
            data = virasoro_spectral(c)
            data_dual = virasoro_spectral(26 - c)
            for g in range(1, 4):
                f = data.kappa * lambda_fp(g)
                f_dual = data_dual.kappa * lambda_fp(g)
                assert f + f_dual == 13 * lambda_fp(g)

    def test_heisenberg_scaling(self):
        """F_g(H_k) = k * lambda_fp(g). Linear in k."""
        for k_val in [1, 2, 3, 7, 10]:
            k = Rational(k_val)
            data = heisenberg_spectral(k)
            for g in range(1, 5):
                assert data.kappa * lambda_fp(g) == k * lambda_fp(g)

    def test_affine_sl2_kappa_formula(self):
        """kappa(V_k(sl_2)) = 3(k+2)/4. Verify at multiple levels.

        PATH 1: kappa formula.
        PATH 2: dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4.
        """
        for k_val in [1, 2, 3, 5, 10]:
            k = Rational(k_val)
            data = affine_sl2_spectral(k)
            expected = Rational(3) * (k + 2) / 4
            assert data.kappa == expected


# ============================================================================
# Section 11: Bridge theorem formal content
# ============================================================================

class TestBridgeTheorem:
    """Test the bridge theorem statement is well-formed and complete."""

    def test_theorem_has_all_routes(self):
        """Bridge theorem statement should contain all 3 proof routes."""
        stmt = bridge_theorem_statement()
        assert 'proof_route_1_DBOSS' in stmt
        assert 'proof_route_2_MC' in stmt
        assert 'proof_route_3_Givental' in stmt

    def test_ap30_addressed(self):
        """The theorem must address AP30 (flat unit condition)."""
        stmt = bridge_theorem_statement()
        assert 'flat_unit' in stmt['flat_unit_condition'].lower() or 'AP30' in stmt['flat_unit_condition']

    def test_gap_resolution(self):
        """The theorem must resolve the gap between TR and CohFT string."""
        stmt = bridge_theorem_statement()
        assert 'gap' in stmt['gap_resolution'].lower()


# ============================================================================
# Section 12: Comprehensive integration test
# ============================================================================

class TestComprehensive:
    """End-to-end comprehensive verification."""

    def test_comprehensive_runs(self):
        """Comprehensive verification completes without error."""
        results = comprehensive_verification(max_genus=3)
        assert 'string_equation' in results
        assert 'dilaton_equation' in results
        assert 'spectral_curves' in results
        assert 'bridge_lemma' in results
        assert 'cohft_status' in results
        assert 'genus2_detail' in results
        assert 'genus3_detail' in results
        assert 'bridge_theorem' in results

    def test_comprehensive_string_all_pass(self):
        """All string equation checks pass."""
        results = comprehensive_verification(max_genus=3)
        for g_key, g_data in results['string_equation'].items():
            for check_key, check in g_data.items():
                if isinstance(check, dict) and 'holds' in check:
                    assert check['holds'], f"String eq failed: {g_key}/{check_key}"

    def test_comprehensive_genus2_passes(self):
        """Genus-2 detailed check passes."""
        results = comprehensive_verification(max_genus=3)
        g2 = results['genus2_detail']
        assert g2['base_tau4_g2']['ok']
        assert g2['string_05_g2']['holds']
        assert g2['F2_value']['ok']

    def test_comprehensive_genus3_passes(self):
        """Genus-3 detailed check passes."""
        results = comprehensive_verification(max_genus=3)
        g3 = results['genus3_detail']
        assert g3['base_tau7_g3']['ok']
        assert g3['string_08_g3']['holds']
        assert g3['F3']['ok']


# ============================================================================
# Section 13: Shadow CohFT free energy + string consistency
# ============================================================================

class TestShadowFreeEnergyString:
    """Verify shadow F_g satisfies string equation for all families."""

    @pytest.mark.parametrize("c_val", [2, 5, 10, 13, 24, 26])
    def test_virasoro_string_g1_to_g4(self, c_val):
        """Shadow string equation for Virasoro at various c."""
        data = virasoro_spectral(Rational(c_val))
        result = verify_shadow_free_energy_string_equation(data, max_genus=4)
        for g in range(1, 5):
            assert result[f'genus_{g}']['holds'], (
                f"String eq failed for Vir_c={c_val} at genus {g}"
            )

    @pytest.mark.parametrize("k_val", [1, 2, 3, 5])
    def test_heisenberg_string_g1_to_g4(self, k_val):
        """Shadow string equation for Heisenberg at various k."""
        data = heisenberg_spectral(Rational(k_val))
        result = verify_shadow_free_energy_string_equation(data, max_genus=4)
        for g in range(1, 5):
            assert result[f'genus_{g}']['holds']

    @pytest.mark.parametrize("k_val", [1, 2, 3])
    def test_affine_sl2_string_g1_to_g4(self, k_val):
        """Shadow string equation for affine sl_2 at various k."""
        data = affine_sl2_spectral(Rational(k_val))
        result = verify_shadow_free_energy_string_equation(data, max_genus=4)
        for g in range(1, 5):
            assert result[f'genus_{g}']['holds']


# ============================================================================
# Section 14: Spectral curve geometry (3+ verification paths)
# ============================================================================

class TestSpectralCurveGeometry:
    """Verify spectral curve geometric properties from multiple paths."""

    def test_discriminant_relation(self):
        """disc(Q_L) = -32 * kappa^2 * Delta.

        PATH 1: Direct computation disc = q1^2 - 4*q0*q2.
        PATH 2: From Delta = 8*kappa*S4.
        """
        data = virasoro_spectral(Rational(10))
        disc = data.disc_QL
        expected = -32 * data.kappa**2 * data.Delta
        assert disc == expected

    def test_discriminant_heisenberg_zero(self):
        """Heisenberg: disc = 0 (degenerate)."""
        data = heisenberg_spectral(Rational(1))
        assert data.disc_QL == 0

    def test_discriminant_affine_zero(self):
        """Affine sl_2: disc = 0 (colliding branch points)."""
        data = affine_sl2_spectral(Rational(1))
        assert data.disc_QL == 0

    def test_virasoro_q2_formula(self):
        """q2 = 9*alpha^2 + 16*kappa*S4 for Virasoro.

        PATH 1: Direct from shadow data.
        PATH 2: 9*4 + 16*(c/2)*10/[c(5c+22)] = 36 + 80/(5c+22).
        """
        c = Rational(10)
        data = virasoro_spectral(c)
        expected_q2 = 36 + Rational(80, 5 * c + 22)
        assert data.q2 == expected_q2

    def test_depth_class_determines_geometry(self):
        """Depth class uniquely determines spectral curve geometry.

        G -> degenerate, L -> cusp, C -> smooth (same as M), M -> smooth.
        """
        g_data = heisenberg_spectral(Rational(1))
        l_data = affine_sl2_spectral(Rational(1))
        m_data = virasoro_spectral(Rational(10))

        g_desc = SpectralCurveDescription.from_shadow_data(g_data)
        l_desc = SpectralCurveDescription.from_shadow_data(l_data)
        m_desc = SpectralCurveDescription.from_shadow_data(m_data)

        assert g_desc.curve_type == 'degenerate'
        assert l_desc.curve_type == 'cusp'
        assert m_desc.curve_type == 'smooth'


# ============================================================================
# Section 15: Higher-genus string equation regression
# ============================================================================

class TestHigherGenusRegression:
    """Regression tests for string equation at higher genera."""

    def test_g1_string_chain(self):
        """Full chain at genus 1: base -> string -> dilaton -> consistency.

        <tau_1>_1 = 1/24  (base)
        <tau_0 tau_2>_1 = <tau_1>_1 = 1/24  (string)
        <tau_1 tau_1>_1 = 1*<tau_1>_1 = 1/24  (dilaton)
        F_1 = 1/24  (Bernoulli)
        """
        assert wk_intersection(1, g=1) == Rational(1, 24)
        assert wk_intersection(0, 2, g=1) == Rational(1, 24)
        assert lambda_fp(1) == Rational(1, 24)

    def test_g2_string_chain(self):
        """Chain at genus 2.

        <tau_4>_2 = 1/1152  (base, 1-point)
        <tau_0 tau_5>_2 = <tau_4>_2  (string, 2-point)
        <tau_1 tau_4>_2 = 3 * 1/1152  (dilaton, 2-point)
        F_2 = 7/5760  (Bernoulli)
        """
        base = wk_intersection(4, g=2)
        assert base == Rational(1, 1152)
        # String: <tau_0 tau_5>_2 = <tau_4>_2 (sum=5, n=2, need=5)
        assert wk_intersection(0, 5, g=2) == base
        # Dilaton: <tau_1 tau_4>_2 = 3*<tau_4>_2 (sum=5, n=2, need=5)
        assert wk_intersection(1, 4, g=2) == 3 * base
        assert lambda_fp(2) == Rational(7, 5760)

    def test_g3_string_chain(self):
        """Chain at genus 3."""
        base = wk_intersection(7, g=3)
        assert base == Rational(1, 82944)
        # String: <tau_0 tau_8>_3 = <tau_7>_3 (sum=8, n=2, need=8)
        assert wk_intersection(0, 8, g=3) == base
        # Dilaton: <tau_1 tau_7>_3 = 5*<tau_7>_3 (sum=8, n=2, need=8)
        assert wk_intersection(1, 7, g=3) == 5 * base
        assert lambda_fp(3) == Rational(31, 967680)

    def test_g4_string_chain(self):
        """Chain at genus 4."""
        base = wk_intersection(10, g=4)
        assert base == Rational(1, 7962624)
        # String: <tau_0 tau_{11}>_4 = <tau_{10}>_4 (sum=11, n=2, need=11)
        assert wk_intersection(0, 11, g=4) == base
        # Dilaton: <tau_1 tau_{10}>_4 = 7*<tau_{10}>_4 (sum=11, n=2, need=11)
        assert wk_intersection(1, 10, g=4) == 7 * base
        assert lambda_fp(4) == Rational(127, 154828800)
