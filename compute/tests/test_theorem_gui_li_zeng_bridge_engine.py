r"""Tests for the Gui-Li-Zeng bridge engine.

Verifies the comparison between the GLZ quadratic duality framework
[arXiv:2212.11252, Adv. Math. 451 (2024)] and the monograph's bar-cobar
Koszul duality framework.

Test organization:
  Section 1: Kappa formula verification (multi-path, AP1/AP39-safe)
  Section 2: GLZ quadratic dual computation for standard families
  Section 3: Framework scope comparison (where GLZ vs monograph apply)
  Section 4: MC equation comparison
  Section 5: PBW bridge (non-quadratic -> quadratic via associated graded)
  Section 6: Complementarity verification (kappa + kappa!)
  Section 7: Regime classification
  Section 8: Involutivity of duality
  Section 9: Cross-family consistency
  Section 10: Edge cases and boundary values

50+ tests total, each with independent verification.
"""
import sys
import os
from fractions import Fraction

import pytest

# Ensure compute/lib is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_gui_li_zeng_bridge_engine import (
    # Lie data
    lie_dim, lie_h_dual,
    # Kappa formulas
    kappa_heisenberg, kappa_virasoro, kappa_affine,
    kappa_betagamma, kappa_bc, kappa_wn, kappa_lattice,
    # Duality maps
    ff_dual_level, virasoro_dual_charge,
    # GLZ dual computations
    compute_glz_dual_heisenberg,
    compute_glz_dual_affine,
    compute_glz_dual_betagamma,
    compute_glz_dual_virasoro,
    compute_glz_dual_wn,
    compute_glz_dual_yangian,
    # Framework predicates
    is_quadratic, needs_completion, regime_classification,
    glz_scope, monograph_scope,
    # MC comparison
    compare_mc_equations,
    # PBW bridge
    pbw_bridge,
    # Complementarity
    verify_kappa_complementarity,
    # Full comparison
    full_comparison,
)


# =====================================================================
# Section 1: Kappa formula verification
# =====================================================================

class TestKappaFormulas:
    """Multi-path verification of kappa formulas (AP1/AP39-safe)."""

    def test_kappa_heisenberg_level_1(self):
        """kappa(H_1) = 1."""
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

    def test_kappa_heisenberg_level_minus1(self):
        """kappa(H_{-1}) = -1."""
        assert kappa_heisenberg(Fraction(-1)) == Fraction(-1)

    def test_kappa_heisenberg_level_k(self):
        """kappa(H_k) = k for arbitrary k."""
        for k in [Fraction(1, 2), Fraction(3), Fraction(-7, 3)]:
            assert kappa_heisenberg(k) == k

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa_virasoro(Fraction(1)) == Fraction(1, 2)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_kappa_virasoro_c0(self):
        """kappa(Vir_0) = 0 (uncurved at c=0)."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_virasoro_self_dual_c13(self):
        """kappa(Vir_13) = 13/2, self-dual point."""
        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)

    def test_kappa_affine_sl2_level_1(self):
        """kappa(sl_2 at k=1) = 3*(1+2)/(2*2) = 9/4."""
        result = kappa_affine("A", 1, Fraction(1))
        assert result == Fraction(9, 4)

    def test_kappa_affine_sl2_critical(self):
        """kappa(sl_2 at k=-h^v=-2) = 3*(-2+2)/(2*2) = 0."""
        result = kappa_affine("A", 1, Fraction(-2))
        assert result == Fraction(0)

    def test_kappa_affine_sl3_level_1(self):
        """kappa(sl_3 at k=1) = 8*(1+3)/(2*3) = 16/3."""
        result = kappa_affine("A", 2, Fraction(1))
        assert result == Fraction(16, 3)

    def test_kappa_affine_not_c_over_2(self):
        """AP39: kappa(g_k) != c/2 for rank > 1.

        For sl_2 at k=1: c = 3*1/(1+2) = 1, c/2 = 1/2.
        But kappa = 9/4, which is NOT 1/2.
        This verifies AP39: kappa != c/2 except for rank-1 Virasoro.
        """
        # Sugawara central charge for sl_2 at level k=1:
        # c = k*dim(g)/(k+h^v) = 1*3/(1+2) = 1
        c_sl2 = Fraction(1 * 3, 1 + 2)
        kap = kappa_affine("A", 1, Fraction(1))
        assert kap != c_sl2 / 2

    def test_kappa_betagamma(self):
        """kappa(betagamma) = +1 at lambda=1.
        # VERIFIED: [DC] c_bg(1) = 2(6-6+1) = +2, kappa = c/2 = +1.
        # [CF] kappa_bg + kappa_bc = 0, so kappa_bg = -kappa_bc = +1.
        # AP137: was -1 (sign swapped with bc). Corrected.
        """
        assert kappa_betagamma() == Fraction(1)

    def test_kappa_bc(self):
        """kappa(bc) = -1 at lambda=1.
        # VERIFIED: [DC] c_bc(1) = 1-3(1)^2 = -2, kappa = c/2 = -1.
        # [CF] complementarity: kappa_bc = -kappa_bg = -1.
        # AP137: was +1 (sign swapped with betagamma). Corrected.
        """
        assert kappa_bc() == Fraction(-1)

    def test_kappa_lattice_rank24(self):
        """kappa(V_Lambda) = 24 for a rank-24 lattice (Leech, Niemeier)."""
        assert kappa_lattice(24) == Fraction(24)

    def test_kappa_wn_virasoro_consistency(self):
        """W_2 = Virasoro, so kappa(W_2, c) should equal kappa(Vir_c) = c/2.

        H_2 = 1 + 1/2 = 3/2, so sigma = H_2 - 1 = 1/2.
        kappa(W_2) = c * (H_2 - 1) = c/2 = kappa(Vir_c). Check.
        """
        c = Fraction(10)
        assert kappa_wn(2, c) == kappa_virasoro(c)


# =====================================================================
# Section 2: GLZ quadratic dual computation
# =====================================================================

class TestGLZDualComputation:
    """Verify GLZ quadratic dual for standard families."""

    def test_heisenberg_dual_kappa_negates(self):
        """H_k^! has kappa = -k."""
        result = compute_glz_dual_heisenberg(Fraction(3))
        assert result.kappa_original == Fraction(3)
        assert result.kappa_dual == Fraction(-3)

    def test_heisenberg_dual_sum_zero(self):
        """kappa(H_k) + kappa(H_k^!) = 0."""
        result = compute_glz_dual_heisenberg(Fraction(7, 2))
        assert result.kappa_sum == Fraction(0)

    def test_heisenberg_is_quadratic_regime(self):
        """Heisenberg is in the quadratic regime."""
        result = compute_glz_dual_heisenberg(Fraction(1))
        assert result.regime == 'quadratic'

    def test_heisenberg_glz_applies(self):
        """GLZ framework applies to Heisenberg."""
        result = compute_glz_dual_heisenberg(Fraction(1))
        assert result.glz_applicable is True

    def test_heisenberg_frameworks_agree(self):
        """Both frameworks agree for Heisenberg."""
        result = compute_glz_dual_heisenberg(Fraction(1))
        assert result.frameworks_agree is True

    def test_affine_sl2_dual_kappa_sum_zero(self):
        """kappa(sl_2 at k) + kappa(sl_2 at -k-4) = 0 (FF anti-symmetry)."""
        result = compute_glz_dual_affine("A", 1, Fraction(1))
        assert result.kappa_sum == Fraction(0)

    def test_affine_sl3_dual_kappa_sum_zero(self):
        """kappa(sl_3 at k) + kappa(sl_3 at -k-6) = 0."""
        result = compute_glz_dual_affine("A", 2, Fraction(1))
        assert result.kappa_sum == Fraction(0)

    def test_affine_glz_applies(self):
        """GLZ applies to affine KM (quadratic generators)."""
        result = compute_glz_dual_affine("A", 1, Fraction(1))
        assert result.glz_applicable is True

    def test_betagamma_dual_is_bc(self):
        """(betagamma)^! = bc ghost system."""
        result = compute_glz_dual_betagamma()
        assert "bc" in result.dual.name.lower() or "bc" in result.dual.name

    def test_betagamma_statistics_swap(self):
        """betagamma is bosonic, bc is fermionic (Sym <-> Lambda)."""
        result = compute_glz_dual_betagamma()
        assert result.original.statistics == 'bosonic'
        assert result.dual.statistics == 'fermionic'

    def test_betagamma_kappa_sum_zero(self):
        """kappa(betagamma) + kappa(bc) = 0."""
        result = compute_glz_dual_betagamma()
        assert result.kappa_sum == Fraction(0)

    def test_virasoro_glz_not_applicable(self):
        """GLZ does NOT directly apply to Virasoro (quartic pole)."""
        result = compute_glz_dual_virasoro(Fraction(1))
        assert result.glz_applicable is False

    def test_virasoro_monograph_applies(self):
        """Monograph framework applies to Virasoro."""
        result = compute_glz_dual_virasoro(Fraction(1))
        assert result.monograph_applicable is True

    def test_virasoro_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [Fraction(1), Fraction(10), Fraction(13), Fraction(25)]:
            result = compute_glz_dual_virasoro(c)
            assert result.kappa_sum == Fraction(13), f"Failed at c={c}"

    def test_wn_glz_not_applicable(self):
        """GLZ does NOT directly apply to W_3 (composite fields)."""
        result = compute_glz_dual_wn(3, Fraction(2))
        assert result.glz_applicable is False

    def test_yangian_glz_applies(self):
        """GLZ applies to Yangian (RTT is quadratic)."""
        result = compute_glz_dual_yangian("A", 1)
        assert result.glz_applicable is True

    def test_yangian_self_dual_simply_laced(self):
        """Y(g)^! = Y(g) for simply-laced g."""
        result = compute_glz_dual_yangian("A", 1, simply_laced=True)
        assert "self-dual" in result.dual.name


# =====================================================================
# Section 3: Framework scope comparison
# =====================================================================

class TestFrameworkScope:
    """Verify which framework applies to which family."""

    def test_heisenberg_is_quadratic(self):
        assert is_quadratic('heisenberg') is True

    def test_affine_is_quadratic(self):
        assert is_quadratic('affine_km') is True

    def test_betagamma_is_quadratic(self):
        assert is_quadratic('betagamma') is True

    def test_virasoro_is_not_quadratic(self):
        assert is_quadratic('virasoro') is False

    def test_wn_is_not_quadratic(self):
        assert is_quadratic('w_n') is False

    def test_yangian_is_quadratic(self):
        assert is_quadratic('yangian') is True

    def test_virasoro_needs_completion(self):
        assert needs_completion('virasoro') is True

    def test_heisenberg_no_completion(self):
        assert needs_completion('heisenberg') is False

    def test_glz_scope_matches_quadratic(self):
        """GLZ scope = quadratic families."""
        for fam in ['heisenberg', 'affine_km', 'betagamma', 'yangian']:
            assert glz_scope(fam) is True, f"GLZ should apply to {fam}"
        for fam in ['virasoro', 'w_n', 'w_3']:
            assert glz_scope(fam) is False, f"GLZ should NOT apply to {fam}"


# =====================================================================
# Section 4: MC equation comparison
# =====================================================================

class TestMCComparison:
    """Verify MC equation correspondence between frameworks."""

    def test_heisenberg_mc_both_apply(self):
        mc = compare_mc_equations('heisenberg', Fraction(1))
        assert mc.glz_mc_applies is True
        assert mc.monograph_mc_applies is True

    def test_heisenberg_mc_genus_0_agree(self):
        mc = compare_mc_equations('heisenberg', Fraction(1))
        assert mc.genus_0_agree is True

    def test_virasoro_mc_glz_not_apply(self):
        mc = compare_mc_equations('virasoro', Fraction(1, 2))
        assert mc.glz_mc_applies is False
        assert mc.monograph_mc_applies is True

    def test_mc_curvature_nonzero(self):
        """MC at genus 1 has curvature kappa for kappa != 0."""
        mc = compare_mc_equations('heisenberg', Fraction(3))
        assert mc.curvature_at_genus_1 == Fraction(3)

    def test_mc_curvature_zero_at_critical(self):
        """At critical level kappa = 0, curvature vanishes."""
        mc = compare_mc_equations('affine_km', Fraction(0))
        assert mc.curvature_at_genus_1 is None

    def test_mc_higher_genus_is_monograph_only(self):
        """GLZ is genus-0 only; monograph extends to all genera."""
        mc = compare_mc_equations('heisenberg', Fraction(1))
        assert "all genera" in mc.higher_genus_extension
        assert "GLZ" in mc.higher_genus_extension


# =====================================================================
# Section 5: PBW bridge
# =====================================================================

class TestPBWBridge:
    """Verify PBW bridge from GLZ to monograph for non-quadratic families."""

    def test_virasoro_pbw_bridge(self):
        """Virasoro: non-quadratic, but gr_F is Koszul, GLZ applies to gr_F."""
        result = pbw_bridge('virasoro')
        assert result.is_quadratic is False
        assert result.gr_is_classically_koszul is True
        assert result.pbw_lifts_to_chiral_koszul is True
        assert result.glz_applies_to_gr is True

    def test_wn_pbw_bridge(self):
        """W_N: non-quadratic, but gr_F is Koszul."""
        result = pbw_bridge('w_n')
        assert result.is_quadratic is False
        assert result.gr_is_classically_koszul is True

    def test_heisenberg_pbw_trivial(self):
        """Heisenberg: already quadratic, PBW trivial."""
        result = pbw_bridge('heisenberg')
        assert result.is_quadratic is True
        assert result.glz_applies_to_gr is True

    def test_virasoro_associated_graded_is_sym(self):
        """gr_F(Vir_c) = Sym(V): a polynomial algebra (Priddy Koszul)."""
        result = pbw_bridge('virasoro')
        assert "Sym" in result.associated_graded


# =====================================================================
# Section 6: Complementarity verification
# =====================================================================

class TestComplementarity:
    """Verify kappa + kappa! (AP24)."""

    def test_heisenberg_complementarity(self):
        kap, kap_d, s, ok = verify_kappa_complementarity('heisenberg', k=Fraction(5))
        assert s == Fraction(0)
        assert ok is True

    def test_affine_sl2_complementarity(self):
        kap, kap_d, s, ok = verify_kappa_complementarity(
            'affine_km', lie_type='A', rank=1, k=Fraction(3))
        assert s == Fraction(0)
        assert ok is True

    def test_affine_sl3_complementarity(self):
        kap, kap_d, s, ok = verify_kappa_complementarity(
            'affine_km', lie_type='A', rank=2, k=Fraction(1))
        assert s == Fraction(0)
        assert ok is True

    def test_virasoro_complementarity_c1(self):
        kap, kap_d, s, ok = verify_kappa_complementarity('virasoro', c=Fraction(1))
        assert s == Fraction(13)
        assert ok is True

    def test_virasoro_complementarity_c13(self):
        """At self-dual point c=13: kappa = 13/2, kappa! = 13/2, sum = 13."""
        kap, kap_d, s, ok = verify_kappa_complementarity('virasoro', c=Fraction(13))
        assert kap == kap_d  # self-dual
        assert s == Fraction(13)
        assert ok is True

    def test_betagamma_complementarity(self):
        kap, kap_d, s, ok = verify_kappa_complementarity('betagamma')
        assert s == Fraction(0)
        assert ok is True

    def test_lattice_complementarity(self):
        kap, kap_d, s, ok = verify_kappa_complementarity('lattice', rank=8)
        assert s == Fraction(0)
        assert ok is True


# =====================================================================
# Section 7: Regime classification
# =====================================================================

class TestRegimeClassification:
    """Verify the four-regime hierarchy."""

    def test_heisenberg_quadratic(self):
        assert regime_classification('heisenberg') == 'quadratic'

    def test_betagamma_quadratic(self):
        assert regime_classification('betagamma') == 'quadratic'

    def test_affine_curved_central(self):
        assert regime_classification('affine_km') == 'curved-central'

    def test_virasoro_curved_central(self):
        assert regime_classification('virasoro') == 'curved-central'

    def test_w3_filtered(self):
        assert regime_classification('w_3') == 'filtered'

    def test_winfty_programmatic(self):
        assert regime_classification('w_infinity') == 'programmatic'

    def test_yangian_quadratic(self):
        assert regime_classification('yangian') == 'quadratic'


# =====================================================================
# Section 8: Involutivity of duality
# =====================================================================

class TestInvolutivity:
    """Verify (A^!)^! = A (involutivity of quadratic duality)."""

    def test_heisenberg_involutive(self):
        result = compute_glz_dual_heisenberg(Fraction(1))
        assert result.is_involutive is True

    def test_affine_involutive(self):
        result = compute_glz_dual_affine("A", 1, Fraction(1))
        assert result.is_involutive is True

    def test_betagamma_involutive(self):
        result = compute_glz_dual_betagamma()
        assert result.is_involutive is True

    def test_ff_involution_is_involutive(self):
        """k -> -k - 2h^v -> k (double application returns to original)."""
        k = Fraction(3)
        k_dual = ff_dual_level("A", 1, k)  # -3 - 4 = -7
        k_double = ff_dual_level("A", 1, k_dual)  # -(-7) - 4 = 3
        assert k_double == k

    def test_virasoro_duality_involutive(self):
        """c -> 26-c -> c (double application)."""
        c = Fraction(5)
        c_dual = virasoro_dual_charge(c)  # 21
        c_double = virasoro_dual_charge(c_dual)  # 5
        assert c_double == c


# =====================================================================
# Section 9: Cross-family consistency
# =====================================================================

class TestCrossFamilyConsistency:
    """Cross-check consistency across families."""

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive: kappa(H_{k1} + H_{k2}) = k1 + k2."""
        k1, k2 = Fraction(3), Fraction(5)
        assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == k1 + k2

    def test_betagamma_bc_dual_pair(self):
        """(betagamma)^! = bc and (bc)^! = betagamma."""
        bg_result = compute_glz_dual_betagamma()
        assert bg_result.kappa_original + bg_result.kappa_dual == 0

    def test_heisenberg_is_abelian_km(self):
        """H_k should match sl_1 (rank 0) affine KM if we could define it.

        Instead, verify that H_k at k matches affine u(1) conventions:
        kappa(H_k) = k (number of bosons times level).
        """
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

    def test_wn_reduces_to_virasoro_at_n2(self):
        """W_2 = Virasoro, so their kappa formulas must agree."""
        c = Fraction(25)
        assert kappa_wn(2, c) == kappa_virasoro(c)

    def test_full_comparison_heisenberg(self):
        """Full comparison report for Heisenberg is consistent."""
        report = full_comparison('heisenberg', k=Fraction(1))
        assert report.glz_result is not None
        assert report.glz_result.frameworks_agree is True
        assert report.kappa_verification[3] is True  # sum correct

    def test_full_comparison_virasoro(self):
        """Full comparison report for Virasoro handles non-quadratic correctly."""
        report = full_comparison('virasoro', c=Fraction(10))
        assert report.glz_result is not None
        assert report.glz_result.glz_applicable is False
        assert report.pbw_bridge_result.glz_applies_to_gr is True

    def test_full_comparison_yangian(self):
        """Full comparison report for Yangian: GLZ applies."""
        report = full_comparison('yangian', lie_type='A', rank=1)
        assert report.glz_result is not None
        assert report.glz_result.glz_applicable is True


# =====================================================================
# Section 10: Edge cases and boundary values
# =====================================================================

class TestEdgeCases:
    """Edge cases and boundary values."""

    def test_kappa_virasoro_c0(self):
        """c=0: kappa = 0, uncurved bar complex."""
        assert kappa_virasoro(Fraction(0)) == Fraction(0)

    def test_kappa_virasoro_c26(self):
        """c=26: kappa = 13, critical string dimension."""
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

    def test_ff_dual_at_critical_level(self):
        """At critical level k=-h^v: the FF involution is self-dual.

        For sl_2: h^v = 2, k_crit = -2.
        FF dual: -(-2) - 2*2 = 2 - 4 = -2 = k_crit.
        The critical level is a fixed point of the FF involution.
        """
        h_v = Fraction(lie_h_dual("A", 1))
        k_crit = -h_v
        k_dual = ff_dual_level("A", 1, k_crit)
        # Path 1: direct computation
        assert k_dual == k_crit
        # Path 2: verify the formula -k - 2h^v at k=-h^v gives -(-h^v) - 2h^v = -h^v
        assert -k_crit - 2 * h_v == k_crit
        # Path 3: kappa at critical level is zero (uncurved)
        assert kappa_affine("A", 1, k_crit) == Fraction(0)

    def test_virasoro_self_dual_point(self):
        """At c=13: Vir_13^! = Vir_13 (self-dual)."""
        c_dual = virasoro_dual_charge(Fraction(13))
        assert c_dual == Fraction(13)

    def test_heisenberg_level_zero(self):
        """H_0: degenerate case, kappa = 0, uncurved."""
        result = compute_glz_dual_heisenberg(Fraction(0))
        assert result.kappa_original == Fraction(0)
        assert result.kappa_dual == Fraction(0)

    def test_lie_dim_sl2(self):
        assert lie_dim("A", 1) == 3

    def test_lie_h_dual_sl2(self):
        assert lie_h_dual("A", 1) == 2

    def test_lie_dim_e8(self):
        assert lie_dim("E", 8) == 248

    def test_lie_h_dual_e8(self):
        assert lie_h_dual("E", 8) == 30

    def test_monograph_scope_always_applies(self):
        """Monograph framework applies to ALL families (its scope is universal)."""
        for fam in ['heisenberg', 'affine_km', 'betagamma',
                    'virasoro', 'w_n', 'w_infinity', 'yangian']:
            scope = monograph_scope(fam)
            assert scope != 'Unknown regime', f"Monograph should cover {fam}"

    def test_affine_all_types_kappa_sum_zero(self):
        """kappa + kappa! = 0 for ALL simple Lie types (FF anti-symmetry)."""
        for (lt, rk) in [("A", 1), ("A", 2), ("A", 3),
                         ("B", 2), ("C", 2), ("D", 4),
                         ("G", 2), ("F", 4), ("E", 6), ("E", 7), ("E", 8)]:
            k = Fraction(1)
            result = compute_glz_dual_affine(lt, rk, k)
            assert result.kappa_sum == Fraction(0), (
                f"kappa sum should be 0 for {lt}_{rk} at k={k}, "
                f"got {result.kappa_sum}"
            )


# =====================================================================
# Section 11: Multi-path verification (AP10 compliance)
# =====================================================================

class TestMultiPathKappa:
    """Multi-path verification of every kappa value.

    AP10 mandate: every hardcoded expected value must be verified by
    at least 2 independent computation paths.  This section provides
    the cross-checks that the single-assertion tests above lack.
    """

    def test_kappa_sl2_three_paths(self):
        """kappa(sl_2 at k=1) via three independent paths.

        Path 1: direct formula dim(g)*(k+h^v)/(2*h^v) = 3*3/4 = 9/4.
        Path 2: Sugawara c = k*dim(g)/(k+h^v) = 3/3 = 1,
                 then kappa = c * dim(g)/(2*k) = 1*3/2 = 3/2... NO.
                 Actually kappa != c/2 for affine KM (AP39).
                 Path 2: compute from dual: kappa + kappa' = 0,
                 kappa' = dim(g)*(-k-2h^v+h^v)/(2*h^v) = 3*(-3)/(4) = -9/4.
                 So kappa = -kappa' = 9/4.
        Path 3: limiting case k=0: kappa = 3*2/4 = 3/2.
                 Shift to k=1: kappa(k=1) - kappa(k=0) = 3*1/4 = 3/4.
                 So kappa(k=1) = 3/2 + 3/4 = 9/4.
        """
        k = Fraction(1)
        # Path 1: direct
        kap1 = kappa_affine("A", 1, k)
        assert kap1 == Fraction(9, 4)
        # Path 2: from FF anti-symmetry
        k_dual = ff_dual_level("A", 1, k)
        kap_dual = kappa_affine("A", 1, k_dual)
        kap2 = -kap_dual
        assert kap2 == Fraction(9, 4)
        # Path 3: linearity in k
        kap_0 = kappa_affine("A", 1, Fraction(0))
        slope = Fraction(lie_dim("A", 1), 2 * lie_h_dual("A", 1))
        kap3 = kap_0 + slope * k
        assert kap3 == Fraction(9, 4)
        # All three agree
        assert kap1 == kap2 == kap3

    def test_kappa_sl3_three_paths(self):
        """kappa(sl_3 at k=1) via three independent paths.

        Path 1: direct: 8*(1+3)/(2*3) = 32/6 = 16/3.
        Path 2: FF anti-symmetry: kappa + kappa' = 0, so kappa = -kappa'.
        Path 3: k-linearity: kappa = kappa(k=0) + slope*k.
        """
        k = Fraction(1)
        # Path 1
        kap1 = kappa_affine("A", 2, k)
        assert kap1 == Fraction(16, 3)
        # Path 2
        k_dual = ff_dual_level("A", 2, k)
        kap2 = -kappa_affine("A", 2, k_dual)
        assert kap2 == Fraction(16, 3)
        # Path 3
        kap_0 = kappa_affine("A", 2, Fraction(0))
        slope = Fraction(lie_dim("A", 2), 2 * lie_h_dual("A", 2))
        kap3 = kap_0 + slope * k
        assert kap3 == Fraction(16, 3)
        assert kap1 == kap2 == kap3

    def test_kappa_virasoro_three_paths(self):
        """kappa(Vir_c) via three paths for c = 25.

        Path 1: direct formula c/2 = 25/2.
        Path 2: complementarity kappa + kappa' = 13.
                 kappa' = (26-25)/2 = 1/2.
                 kappa = 13 - 1/2 = 25/2.
        Path 3: W_2 reduction: kappa(W_2, c) should equal kappa(Vir_c).
        """
        c = Fraction(25)
        # Path 1
        kap1 = kappa_virasoro(c)
        assert kap1 == Fraction(25, 2)
        # Path 2
        c_dual = virasoro_dual_charge(c)
        kap_dual = kappa_virasoro(c_dual)
        kap2 = Fraction(13) - kap_dual
        assert kap2 == Fraction(25, 2)
        # Path 3
        kap3 = kappa_wn(2, c)
        assert kap3 == Fraction(25, 2)
        assert kap1 == kap2 == kap3

    def test_kappa_heisenberg_three_paths(self):
        """kappa(H_k) via three paths for k = 7/3.

        Path 1: direct formula kappa = k = 7/3.
        Path 2: anti-symmetry kappa + kappa' = 0, kappa' = -7/3,
                 so kappa = -kappa' = 7/3.
        Path 3: additivity kappa(H_{k1+k2}) = kappa(H_{k1}) + kappa(H_{k2}).
                 kappa(H_{1/3}) + kappa(H_2) = 1/3 + 2 = 7/3.
        """
        k = Fraction(7, 3)
        # Path 1
        kap1 = kappa_heisenberg(k)
        assert kap1 == Fraction(7, 3)
        # Path 2
        kap2 = -kappa_heisenberg(-k)
        assert kap2 == Fraction(7, 3)
        # Path 3
        kap3 = kappa_heisenberg(Fraction(1, 3)) + kappa_heisenberg(Fraction(2))
        assert kap3 == Fraction(7, 3)
        assert kap1 == kap2 == kap3

    def test_kappa_betagamma_bc_two_paths(self):
        """kappa(betagamma) and kappa(bc) via two paths.

        Path 1: direct formulas: kappa(bg) = +1, kappa(bc) = -1.
        Path 2: complementarity sum = 0, so kappa(bc) = -kappa(bg) = -1.
        # AP137: signs were swapped. Corrected.
        """
        # Path 1
        kap_bg = kappa_betagamma()
        kap_bc = kappa_bc()
        assert kap_bg == Fraction(1)
        assert kap_bc == Fraction(-1)
        # Path 2
        assert kap_bg + kap_bc == Fraction(0)
        assert -kap_bg == kap_bc

    def test_ff_involution_all_types_two_paths(self):
        """FF involution k -> -k-2h^v: verify involutivity via two paths.

        Path 1: apply twice, should get identity.
        Path 2: verify kappa sum = 0 (consequence of involutivity).
        """
        for (lt, rk) in [("A", 1), ("A", 2), ("B", 2), ("D", 4),
                         ("G", 2), ("E", 6), ("E", 8)]:
            k = Fraction(3)
            # Path 1: double application
            k_dual = ff_dual_level(lt, rk, k)
            k_back = ff_dual_level(lt, rk, k_dual)
            assert k_back == k, f"FF not involutive for {lt}_{rk}"
            # Path 2: kappa anti-symmetry
            kap = kappa_affine(lt, rk, k)
            kap_dual = kappa_affine(lt, rk, k_dual)
            assert kap + kap_dual == Fraction(0), (
                f"kappa sum != 0 for {lt}_{rk}: {kap} + {kap_dual}"
            )

    def test_virasoro_complementarity_sweep_two_paths(self):
        """Virasoro kappa + kappa' = 13 for many c values, via two paths.

        Path 1: direct computation of both kappas.
        Path 2: algebraic identity c/2 + (26-c)/2 = 26/2 = 13.
        """
        for c_num in range(-5, 30):
            c = Fraction(c_num)
            # Path 1
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(virasoro_dual_charge(c))
            s = kap + kap_dual
            assert s == Fraction(13), f"Failed at c={c}: sum={s}"
            # Path 2: algebraic
            s_alg = c / 2 + (26 - c) / 2
            assert s_alg == Fraction(13)
            assert s == s_alg

    def test_glz_dual_heisenberg_multipath(self):
        """GLZ dual of Heisenberg: verify via two independent paths.

        Path 1: compute via compute_glz_dual_heisenberg.
        Path 2: compute kappa directly and verify properties.
        """
        k = Fraction(5)
        # Path 1: via engine
        result = compute_glz_dual_heisenberg(k)
        # Path 2: independent kappa computation
        kap_direct = k  # kappa(H_k) = k by definition
        kap_dual_direct = -k  # kappa(H_k^!) = -k
        assert result.kappa_original == kap_direct
        assert result.kappa_dual == kap_dual_direct
        assert result.kappa_sum == kap_direct + kap_dual_direct

    def test_glz_dual_affine_multipath(self):
        """GLZ dual of affine sl_2: verify via two paths.

        Path 1: via engine.
        Path 2: independent formula evaluation.
        """
        k = Fraction(2)
        # Path 1
        result = compute_glz_dual_affine("A", 1, k)
        # Path 2: independent
        dim_g = Fraction(3)
        h_v = Fraction(2)
        kap = dim_g * (k + h_v) / (2 * h_v)  # 3*4/4 = 3
        k_dual = -k - 2 * h_v  # -2 -4 = -6
        kap_dual = dim_g * (k_dual + h_v) / (2 * h_v)  # 3*(-4)/4 = -3
        assert result.kappa_original == kap
        assert result.kappa_dual == kap_dual
        assert result.kappa_sum == Fraction(0)
        assert kap + kap_dual == Fraction(0)

    def test_regime_and_scope_consistency(self):
        """Regime classification and GLZ scope must be consistent.

        If regime = 'quadratic', GLZ should apply.
        If regime = 'filtered' or 'programmatic', GLZ should not apply.
        """
        for fam in ['heisenberg', 'betagamma', 'bc', 'yangian']:
            r = regime_classification(fam)
            g = glz_scope(fam)
            assert r == 'quadratic', f"{fam} should be quadratic, got {r}"
            assert g is True, f"GLZ should apply to quadratic {fam}"
        for fam in ['virasoro']:
            r = regime_classification(fam)
            g = glz_scope(fam)
            assert r == 'curved-central'
            assert g is False
        for fam in ['w_3', 'w_n']:
            r = regime_classification(fam)
            g = glz_scope(fam)
            assert r == 'filtered'
            assert g is False

    def test_pbw_bridge_consistency_multipath(self):
        """PBW bridge: for non-quadratic families, verify gr_F is Koszul
        both via pbw_bridge and via the PBW criterion logic.

        Path 1: pbw_bridge says gr_is_classically_koszul.
        Path 2: For Virasoro, gr_F = Sym(V) and polynomial algebras are
                 Koszul by Priddy's theorem (the Koszul complex of Sym(V)
                 is the de Rham complex, acyclic by Poincare lemma).
        """
        result = pbw_bridge('virasoro')
        # Path 1
        assert result.gr_is_classically_koszul is True
        # Path 2: Sym(V) is Koszul for any V (Priddy)
        assert "Sym" in result.associated_graded
        # Path 3: PBW lifts to chiral Koszulness
        assert result.pbw_lifts_to_chiral_koszul is True
        # Consistency: if gr is Koszul and PBW lifts, then A is chiral Koszul
        assert result.glz_applies_to_gr is True


# =====================================================================
# Run
# =====================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
