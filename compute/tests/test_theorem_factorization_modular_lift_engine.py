r"""Tests for factorization envelope modular completion (class L).

55+ assertions verifying:
  1. Bernoulli / lambda_fp independent recomputation
  2. Kappa formulas for SU(N) (AP1 cross-verification)
  3. S_3 cubic shadow coefficient
  4. Genus-0 factorization algebra construction
  5. Genus-1 twisted factorization algebra (F_1 = kappa/24)
  6. Genus-2 total free energy with planted-forest correction
  7. Genus-3 and genus-4 class L closed forms
  8. Heisenberg limit (S_3 -> 0)
  9. Complementarity (AP24: kappa + kappa' = 0 for KM)
 10. Shadow tower termination (class L: r_max = 3, Delta = 0)
 11. HS-sewing verification
 12. Planted-forest degree analysis
 13. Full pipeline
 14. Cross-engine consistency with theorem_class_l_closed_form_engine
 15. Cross-engine consistency with theorem_vicedo_envelope_engine
 16. Genus growth rate analysis
 17. Constructiveness of the modular lift

Multi-path verification (3+ paths per claim):
  Path 1: Direct formula evaluation from this engine.
  Path 2: Independent recomputation in the test itself.
  Path 3: Cross-check with theorem_class_l_closed_form_engine.
  Path 4: Heisenberg limit (S_3 = 0 => delta_pf = 0).
  Path 5: Complementarity (kappa + kappa' = 0).

AP warnings:
  AP1: kappa = dim(g) * (k + h^v) / (2 * h^v).  NEVER c/2 for dim > 1.
  AP9: kappa != c/2 for affine KM with rank >= 2.
  AP10: tests use cross-family consistency, not just hardcoded values.
  AP24: kappa + kappa' = 0 for KM (NOT for Virasoro).
  AP38: consistent normalization for Bernoulli / lambda_fp.
"""

from fractions import Fraction
from math import comb, factorial

import pytest

from compute.lib.theorem_factorization_modular_lift_engine import (
    # Primitives
    bernoulli_exact,
    lambda_fp,
    # Kappa / shadow
    kappa_slN,
    central_charge_slN,
    S3_slN,
    ff_dual_level,
    # Genus-0
    Genus0FactorizationAlgebra,
    build_genus0,
    # Genus-1
    Genus1FactorizationAlgebra,
    build_genus1,
    # Planted-forest
    delta_pf_genus2,
    delta_pf_genus3_class_L,
    delta_pf_genus4_class_L,
    GENUS3_PF_CLASS_L,
    GENUS4_PF_CLASS_L,
    # Free energy
    F_g_class_L,
    # Genus-g
    GenusGFactorizationAlgebra,
    build_genus_g,
    # Modular lift
    ModularLift,
    build_modular_lift,
    # Sewing
    SewingEnvelopeData,
    verify_hs_sewing,
    # Analysis
    heisenberg_limit,
    complementarity_check,
    shadow_tower_analysis,
    pf_degree_analysis,
    # Pipeline
    full_modular_lift_pipeline,
    # Cross-checks
    cross_check_with_class_l_engine,
    cross_check_with_vicedo_engine,
    # Growth
    genus_growth_analysis,
)


# ============================================================================
# Ground truth (independently computed, NOT copied from engine)
# ============================================================================
# kappa(sl_2, k=0) = (4-1)*(0+2)/(2*2) = 3*2/4 = 3/2.
# kappa(sl_3, k=0) = (9-1)*(0+3)/(2*3) = 8*3/6 = 4.
# kappa(sl_4, k=0) = (16-1)*(0+4)/(2*4) = 15*4/8 = 15/2.
# kappa(sl_5, k=0) = (25-1)*(0+5)/(2*5) = 24*5/10 = 12.
# S_3(sl_2, k=0)  = 2*2/(3*(3/2)) = 4/(9/2) = 8/9.
# S_3(sl_3, k=0)  = 2*3/(3*4) = 6/12 = 1/2.
# lambda_1^FP = 1/24.  lambda_2^FP = 7/5760.
# c(sl_2, k=0) = 0.  c(sl_2, k=1) = 1.
# c(sl_3, k=0) = 0.  c(sl_3, k=1) = 2.

# Independent Bernoulli:
# B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42.


# ============================================================================
# 1. Bernoulli numbers
# ============================================================================

class TestBernoulliPrimitives:
    """Verify Bernoulli numbers from independent recomputation."""

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

    def test_lambda_fp_g1(self):
        """lambda_1^FP = (2^1 - 1)|B_2|/(2^1 * 2!) = 1*(1/6)/(2*2) = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = (2^3 - 1)|B_4|/(2^3 * 4!) = 7*(1/30)/(8*24) = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = (2^5 - 1)|B_6|/(2^5 * 6!) = 31*(1/42)/(32*720) = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)


# ============================================================================
# 2. Kappa formulas (AP1: independent verification per family)
# ============================================================================

class TestKappaFormulas:
    """AP1: every kappa formula verified from first principles."""

    def test_kappa_sl2_k0(self):
        """kappa(sl_2, k=0) = 3*2/4 = 3/2."""
        assert kappa_slN(2, Fraction(0)) == Fraction(3, 2)

    def test_kappa_sl3_k0(self):
        """kappa(sl_3, k=0) = 8*3/6 = 4."""
        assert kappa_slN(3, Fraction(0)) == Fraction(4)

    def test_kappa_sl4_k0(self):
        """kappa(sl_4, k=0) = 15*4/8 = 15/2."""
        assert kappa_slN(4, Fraction(0)) == Fraction(15, 2)

    def test_kappa_sl5_k0(self):
        """kappa(sl_5, k=0) = 24*5/10 = 12."""
        assert kappa_slN(5, Fraction(0)) == Fraction(12)

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        assert kappa_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_ap9_sl3_ne_c_over_2(self):
        """AP9: kappa(sl_3, k=1) != c(sl_3, k=1)/2."""
        kap = kappa_slN(3, Fraction(1))
        cc = central_charge_slN(3, Fraction(1))
        assert kap != cc / 2


# ============================================================================
# 3. Central charge and S_3
# ============================================================================

class TestCentralChargeAndS3:
    """Verify c and S_3 from first principles."""

    def test_c_sl2_k0(self):
        """c(sl_2, k=0) = 0*(4-1)/(0+2) = 0."""
        assert central_charge_slN(2, Fraction(0)) == Fraction(0)

    def test_c_sl2_k1(self):
        """c(sl_2, k=1) = 1*3/3 = 1."""
        assert central_charge_slN(2, Fraction(1)) == Fraction(1)

    def test_c_sl3_k1(self):
        """c(sl_3, k=1) = 1*8/4 = 2."""
        assert central_charge_slN(3, Fraction(1)) == Fraction(2)

    def test_S3_sl2_k0(self):
        """S_3(sl_2, k=0) = 2*2/(3*(3/2)) = 4/(9/2) = 8/9."""
        assert S3_slN(2, Fraction(0)) == Fraction(8, 9)

    def test_S3_sl3_k0(self):
        """S_3(sl_3, k=0) = 2*3/(3*4) = 1/2."""
        assert S3_slN(3, Fraction(0)) == Fraction(1, 2)

    def test_S3_sl4_k0(self):
        """S_3(sl_4, k=0) = 2*4/(3*(15/2)) = 8/(45/2) = 16/45."""
        assert S3_slN(4, Fraction(0)) == Fraction(16, 45)


# ============================================================================
# 4. Genus-0 factorization algebra
# ============================================================================

class TestGenus0:
    """Verify genus-0 factorization algebra construction."""

    def test_genus0_sl2_k0_kappa(self):
        g0 = build_genus0(2, Fraction(0))
        assert g0.kappa == Fraction(3, 2)

    def test_genus0_sl2_k0_S3(self):
        g0 = build_genus0(2, Fraction(0))
        assert g0.S_3 == Fraction(8, 9)

    def test_genus0_sl2_depth_class(self):
        g0 = build_genus0(2, Fraction(0))
        assert g0.shadow_depth_class == 'L'

    def test_genus0_sl3_dim(self):
        g0 = build_genus0(3, Fraction(0))
        assert g0.dim_g == 8

    def test_genus0_max_pole_order(self):
        """Weight-1 generators => max OPE pole order = 2."""
        g0 = build_genus0(2, Fraction(0))
        assert g0.max_ope_pole_order == 2

    def test_genus0_r_matrix_pole(self):
        """AP19: r-matrix max pole = OPE max pole - 1 = 1."""
        g0 = build_genus0(2, Fraction(0))
        assert g0.r_matrix_max_pole == 1


# ============================================================================
# 5. Genus-1 factorization algebra
# ============================================================================

class TestGenus1:
    """Verify genus-1 twisted factorization algebra."""

    def test_genus1_F1_sl2(self):
        """F_1(sl_2, k=0) = kappa/24 = (3/2)/24 = 1/16."""
        g0 = build_genus0(2, Fraction(0))
        g1 = build_genus1(g0)
        assert g1.F_1 == Fraction(3, 2) * Fraction(1, 24)
        assert g1.F_1 == Fraction(1, 16)

    def test_genus1_F1_sl3(self):
        """F_1(sl_3, k=0) = 4/24 = 1/6."""
        g0 = build_genus0(3, Fraction(0))
        g1 = build_genus1(g0)
        assert g1.F_1 == Fraction(1, 6)

    def test_genus1_sewing_converges(self):
        g0 = build_genus0(2, Fraction(0))
        g1 = build_genus1(g0)
        assert g1.sewing_converges is True

    def test_genus1_curvature(self):
        """Curvature = kappa."""
        g0 = build_genus0(2, Fraction(0))
        g1 = build_genus1(g0)
        assert g1.curvature_kappa == Fraction(3, 2)

    def test_genus1_universal(self):
        """obs_1 = kappa * lambda_1 is proved for ALL families.
        For sl_2 at k=0: F_1 = (3/2)/24 = 1/16.
        For sl_3 at k=0: F_1 = 4/24 = 1/6.
        Ratio: F_1(sl_3)/F_1(sl_2) = (1/6)/(1/16) = 16/6 = 8/3
               = kappa(sl_3)/kappa(sl_2) = 4/(3/2) = 8/3. Check."""
        g0_2 = build_genus0(2, Fraction(0))
        g0_3 = build_genus0(3, Fraction(0))
        g1_2 = build_genus1(g0_2)
        g1_3 = build_genus1(g0_3)
        ratio_F1 = g1_3.F_1 / g1_2.F_1
        ratio_kappa = g0_3.kappa / g0_2.kappa
        assert ratio_F1 == ratio_kappa


# ============================================================================
# 6. Genus-2 free energy
# ============================================================================

class TestGenus2:
    """Verify genus-2 free energy with planted-forest correction."""

    def test_delta_pf_genus2_sl2_k0(self):
        """delta_pf^{(2,0)} for SU(2) at k=0.
        kappa = 3/2, S_3 = 8/9.
        delta_pf = (8/9)*(10*(8/9) - 3/2)/48 = (8/9)*(80/9 - 3/2)/48
                 = (8/9)*(160/18 - 27/18)/48 = (8/9)*(133/18)/48
                 = (8*133)/(9*18*48) = 1064/7776 = 133/972.
        """
        kap = Fraction(3, 2)
        s3 = Fraction(8, 9)
        dpf = delta_pf_genus2(kap, s3)
        # Independent: S3*(10*S3 - kappa)/48
        expected = Fraction(8, 9) * (10 * Fraction(8, 9) - Fraction(3, 2)) / 48
        assert dpf == expected
        assert dpf == Fraction(133, 972)

    def test_F2_sl2_k0(self):
        """F_2(SU(2), k=0) = kappa*7/5760 + delta_pf."""
        kap = Fraction(3, 2)
        s3 = Fraction(8, 9)
        F2 = F_g_class_L(2, kap, s3)
        scalar = kap * Fraction(7, 5760)
        pf = delta_pf_genus2(kap, s3)
        assert F2 == scalar + pf

    def test_delta_pf_genus2_heisenberg_limit(self):
        """S_3 = 0 => delta_pf = 0 (class G recovery)."""
        dpf = delta_pf_genus2(Fraction(3, 2), Fraction(0))
        assert dpf == Fraction(0)


# ============================================================================
# 7. Genus-3 and genus-4 free energy
# ============================================================================

class TestHigherGenus:
    """Verify genus-3 and genus-4 class L closed forms."""

    def test_genus3_heisenberg_limit(self):
        """S_3 = 0 => delta_pf_3 = 0."""
        dpf3 = delta_pf_genus3_class_L(Fraction(3, 2), Fraction(0))
        assert dpf3 == Fraction(0)

    def test_genus3_decomposition(self):
        """F_3 = scalar + pf, where scalar = kappa * lambda_3^FP."""
        kap = Fraction(3, 2)
        s3 = Fraction(8, 9)
        F3 = F_g_class_L(3, kap, s3)
        scalar = kap * lambda_fp(3)
        pf = delta_pf_genus3_class_L(kap, s3)
        assert F3 == scalar + pf

    def test_genus4_heisenberg_limit(self):
        """S_3 = 0 => delta_pf_4 = 0."""
        dpf4 = delta_pf_genus4_class_L(Fraction(3, 2), Fraction(0))
        assert dpf4 == Fraction(0)

    def test_genus4_decomposition(self):
        """F_4 = scalar + pf, where scalar = kappa * lambda_4^FP."""
        kap = Fraction(3, 2)
        s3 = Fraction(8, 9)
        F4 = F_g_class_L(4, kap, s3)
        scalar = kap * lambda_fp(4)
        pf = delta_pf_genus4_class_L(kap, s3)
        assert F4 == scalar + pf

    def test_genus5_raises(self):
        """Genus 5 not available as closed-form polynomial."""
        with pytest.raises(ValueError, match="not available"):
            F_g_class_L(5, Fraction(3, 2), Fraction(8, 9))


# ============================================================================
# 8. Heisenberg limit
# ============================================================================

class TestHeisenbergLimit:
    """Verify S_3 -> 0 gives class G (Heisenberg) at each genus."""

    def test_heisenberg_limit_g1(self):
        result = heisenberg_limit(1, Fraction(3, 2))
        assert result['match'] is True

    def test_heisenberg_limit_g2(self):
        result = heisenberg_limit(2, Fraction(3, 2))
        assert result['match'] is True

    def test_heisenberg_limit_g3(self):
        result = heisenberg_limit(3, Fraction(4))
        assert result['match'] is True

    def test_heisenberg_limit_g4(self):
        result = heisenberg_limit(4, Fraction(15, 2))
        assert result['match'] is True


# ============================================================================
# 9. Complementarity (AP24)
# ============================================================================

class TestComplementarity:
    """AP24: kappa + kappa' = 0 for affine KM."""

    def test_complementarity_sl2_k0(self):
        result = complementarity_check(2, Fraction(0))
        assert result['anti_symmetric'] is True
        assert result['sum'] == Fraction(0)

    def test_complementarity_sl3_k0(self):
        result = complementarity_check(3, Fraction(0))
        assert result['anti_symmetric'] is True

    def test_complementarity_sl2_k1(self):
        result = complementarity_check(2, Fraction(1))
        assert result['anti_symmetric'] is True

    def test_ff_dual_level(self):
        """k' = -k - 2N for sl_N."""
        assert ff_dual_level(2, Fraction(0)) == Fraction(-4)
        assert ff_dual_level(3, Fraction(1)) == Fraction(-7)


# ============================================================================
# 10. Shadow tower termination
# ============================================================================

class TestShadowTower:
    """Verify shadow tower terminates for class L."""

    def test_shadow_tower_sl2_terminates(self):
        result = shadow_tower_analysis(2, Fraction(0))
        assert result['tower_terminates'] is True

    def test_shadow_tower_sl2_r_max(self):
        result = shadow_tower_analysis(2, Fraction(0))
        assert result['r_max'] == 3

    def test_shadow_tower_sl2_discriminant_zero(self):
        """Delta = 8 * kappa * S_4 = 0 for class L (S_4 = 0)."""
        result = shadow_tower_analysis(2, Fraction(0))
        assert result['discriminant_zero'] is True
        assert result['critical_discriminant'] == Fraction(0)

    def test_shadow_tower_depth_class(self):
        result = shadow_tower_analysis(3, Fraction(0))
        assert result['shadow_depth_class'] == 'L'

    def test_depth_decomposition(self):
        """d = 1 + d_arith + d_alg = 1 + 0 + 1 = 2 for class L."""
        result = shadow_tower_analysis(2, Fraction(0))
        assert result['d_total'] == 2
        assert result['d_alg'] == 1
        assert result['d_arith'] == 0


# ============================================================================
# 11. HS-sewing
# ============================================================================

class TestHSSewing:
    """Verify HS-sewing for affine KM."""

    def test_hs_sewing_sl2(self):
        result = verify_hs_sewing(2, Fraction(0))
        assert result.hs_sewing_converges is True

    def test_ope_growth_polynomial(self):
        result = verify_hs_sewing(3, Fraction(1))
        assert result.ope_growth_polynomial is True

    def test_sector_growth_subexponential(self):
        result = verify_hs_sewing(4, Fraction(0))
        assert result.sector_growth_subexponential is True


# ============================================================================
# 12. Planted-forest degree analysis
# ============================================================================

class TestDegreeAnalysis:
    """Verify degree structure of delta_pf for class L."""

    def test_genus2_degree(self):
        """Max total degree at g=2 should be 2 = 2*(2-1)."""
        result = pf_degree_analysis()
        assert result[2]['max_total_degree'] == 2
        assert result[2]['satisfies_bound'] is True

    def test_genus3_degree(self):
        """Max total degree at g=3 should be <= 4 = 2*(3-1)."""
        result = pf_degree_analysis()
        assert result[3]['satisfies_bound'] is True

    def test_genus4_degree(self):
        """Max total degree at g=4 should be <= 6 = 2*(4-1)."""
        result = pf_degree_analysis()
        assert result[4]['satisfies_bound'] is True


# ============================================================================
# 13. Full pipeline
# ============================================================================

class TestFullPipeline:
    """Verify the full modular lift pipeline."""

    def test_pipeline_sl2_constructive(self):
        result = full_modular_lift_pipeline(2, Fraction(0))
        assert result.is_constructive is True

    def test_pipeline_sl3_constructive(self):
        result = full_modular_lift_pipeline(3, Fraction(0))
        assert result.is_constructive is True

    def test_pipeline_sewing_converges(self):
        result = full_modular_lift_pipeline(2, Fraction(1))
        assert result.sewing.hs_sewing_converges is True

    def test_pipeline_shadow_terminates(self):
        result = full_modular_lift_pipeline(2, Fraction(0))
        assert result.shadow_analysis['tower_terminates'] is True

    def test_pipeline_complementarity(self):
        result = full_modular_lift_pipeline(2, Fraction(0))
        assert result.complementarity['anti_symmetric'] is True


# ============================================================================
# 14. Cross-engine consistency with class L engine
# ============================================================================

class TestCrossCheckClassL:
    """Cross-check with theorem_class_l_closed_form_engine (AP10)."""

    def test_cross_check_F1_sl2(self):
        """F_1 from this engine should match class L engine."""
        from compute.lib.theorem_class_l_closed_form_engine import (
            F_g_class_L as F_g_ref,
            kappa_slN as kappa_ref,
            S3_slN as S3_ref,
        )
        kap = kappa_slN(2, Fraction(0))
        s3 = S3_slN(2, Fraction(0))
        our = F_g_class_L(1, kap, s3)
        ref = F_g_ref(1, kappa_ref(2, Fraction(0)), S3_ref(2, Fraction(0)))
        assert our == ref

    def test_cross_check_F2_sl2(self):
        from compute.lib.theorem_class_l_closed_form_engine import (
            F_g_class_L as F_g_ref,
            kappa_slN as kappa_ref,
            S3_slN as S3_ref,
        )
        kap = kappa_slN(2, Fraction(0))
        s3 = S3_slN(2, Fraction(0))
        our = F_g_class_L(2, kap, s3)
        ref = F_g_ref(2, kappa_ref(2, Fraction(0)), S3_ref(2, Fraction(0)))
        assert our == ref

    def test_cross_check_F3_sl3(self):
        from compute.lib.theorem_class_l_closed_form_engine import (
            F_g_class_L as F_g_ref,
            kappa_slN as kappa_ref,
            S3_slN as S3_ref,
        )
        kap = kappa_slN(3, Fraction(0))
        s3 = S3_slN(3, Fraction(0))
        our = F_g_class_L(3, kap, s3)
        ref = F_g_ref(3, kappa_ref(3, Fraction(0)), S3_ref(3, Fraction(0)))
        assert our == ref

    def test_cross_check_kappa_sl4(self):
        from compute.lib.theorem_class_l_closed_form_engine import (
            kappa_slN as kappa_ref,
        )
        assert kappa_slN(4, Fraction(0)) == kappa_ref(4, Fraction(0))


# ============================================================================
# 15. Cross-engine consistency with Vicedo engine
# ============================================================================

class TestCrossCheckVicedo:
    """Cross-check with theorem_vicedo_envelope_engine."""

    def test_cross_check_kappa_sl2(self):
        from compute.lib.theorem_vicedo_envelope_engine import (
            affine_sl2_lca,
            compute_kappa,
        )
        from sympy import Rational
        L = affine_sl2_lca(Rational(0))
        vicedo_kappa = compute_kappa(L)
        our_kappa = kappa_slN(2, Fraction(0))
        # Sympy Rational vs fractions.Fraction: compare numerically
        assert float(vicedo_kappa) == float(our_kappa)

    def test_cross_check_depth_class_sl2(self):
        """Use sl_2 (which has full OPE table in Vicedo engine) for depth class.
        The affine_slN_lca constructor for N >= 3 omits the OPE table,
        so compute_shadow_depth_class sees no bracket and returns 'G'.
        The sl_2 constructor has the full OPE and correctly returns 'L'."""
        from compute.lib.theorem_vicedo_envelope_engine import (
            affine_sl2_lca,
            compute_shadow_depth_class,
        )
        from sympy import Rational
        L = affine_sl2_lca(Rational(0))
        vicedo_class = compute_shadow_depth_class(L)
        g0 = build_genus0(2, Fraction(0))
        assert vicedo_class == g0.shadow_depth_class
        assert vicedo_class == 'L'

    def test_cross_check_genus1_F1(self):
        from compute.lib.theorem_vicedo_envelope_engine import (
            affine_sl2_lca,
            build_vicedo_prefactorization,
            extend_to_genus1,
        )
        from sympy import Rational
        L = affine_sl2_lca(Rational(0))
        pfa = build_vicedo_prefactorization(L)
        g1_vicedo = extend_to_genus1(pfa)
        g0 = build_genus0(2, Fraction(0))
        g1_ours = build_genus1(g0)
        assert float(g1_vicedo.f1) == float(g1_ours.F_1)


# ============================================================================
# 16. Genus growth rate analysis
# ============================================================================

class TestGrowthAnalysis:
    """Verify genus growth rate properties."""

    def test_pf_ratio_nonzero_for_nonabelian(self):
        """Planted-forest / scalar ratio should be nonzero for g >= 2."""
        data = genus_growth_analysis(2, Fraction(0))
        assert data[1]['F_g_pf'] == Fraction(0)  # no pf at g=1
        assert data[2]['F_g_pf'] != Fraction(0)  # nonzero at g=2

    def test_pf_ratio_zero_at_g1(self):
        """No planted-forest correction at genus 1."""
        data = genus_growth_analysis(3, Fraction(0))
        assert data[1]['pf_to_scalar_ratio'] == Fraction(0)


# ============================================================================
# 17. Constructiveness of the modular lift
# ============================================================================

class TestConstructiveness:
    """Verify the modular lift is constructive for class L."""

    def test_modular_lift_constructive(self):
        ml = build_modular_lift(2, Fraction(0))
        assert ml.is_constructive is True

    def test_shadow_tower_terminates(self):
        ml = build_modular_lift(2, Fraction(0))
        assert ml.shadow_tower_terminates is True

    def test_termination_arity(self):
        ml = build_modular_lift(2, Fraction(0))
        assert ml.termination_arity == 3

    def test_hs_sewing_proved(self):
        ml = build_modular_lift(2, Fraction(0))
        assert ml.hs_sewing_proved is True

    def test_mc_equation_proved(self):
        ml = build_modular_lift(2, Fraction(0))
        assert ml.mc_equation_proved is True

    def test_genus_data_present(self):
        ml = build_modular_lift(3, Fraction(0), max_genus=3)
        assert 1 in ml.genus_data
        assert 2 in ml.genus_data
        assert 3 in ml.genus_data

    def test_cumulative_curvature_g2(self):
        """Cumulative curvature at g=2 = F_1 + F_2."""
        gd = build_genus_g(2, Fraction(0), 2)
        F1 = F_g_class_L(1, kappa_slN(2), S3_slN(2))
        F2 = F_g_class_L(2, kappa_slN(2), S3_slN(2))
        assert gd.cumulative_curvature == F1 + F2

    def test_cumulative_curvature_g3(self):
        """Cumulative curvature at g=3 = F_1 + F_2 + F_3."""
        gd = build_genus_g(3, Fraction(0), 3)
        kap = kappa_slN(3)
        s3 = S3_slN(3)
        expected = sum(F_g_class_L(g, kap, s3) for g in range(1, 4))
        assert gd.cumulative_curvature == expected
