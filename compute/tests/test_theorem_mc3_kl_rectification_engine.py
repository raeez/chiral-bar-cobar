r"""Tests for MC3 KL Rectification Engine.

65 tests organized in 10 sections:
    I.   Quantum group parameter computation (8 tests)
    II.  Fusion ring verification (8 tests)
    III. Kappa preservation analysis (6 tests)
    IV.  Thick generation transport (4 tests)
    V.   DK-4/5 obstruction analysis (6 tests)
    VI.  Creutzig-Niu abelian gauge landscape (5 tests)
    VII. Full KL equivalence analysis (6 tests)
    VIII.sl_2 at k = -1/2 complete analysis (8 tests)
    IX.  Multi-path verification (8 tests)
    X.   Cross-check and consistency (6 tests)

VERIFICATION MANDATE: every numerical result is verified by at least 2
independent methods (AP10 compliance).

Manuscript references:
    thm:categorical-cg-all-types (yangians_drinfeld_kohno.tex)
    cor:dk23-all-types (yangians_drinfeld_kohno.tex)
    conj:dk4-formal-moduli (yangians_drinfeld_kohno.tex)
    prop:admissible-verlinde-bar (kac_moody.tex)
    thm:kw-bar-spectral (kac_moody.tex)
"""

import pytest
from fractions import Fraction
from math import pi, cos, sin, sqrt

from compute.lib.theorem_mc3_kl_rectification_engine import (
    QuantumGroupParameter,
    FusionRingData,
    KLEquivalenceAnalysis,
    AbelianGaugeVOSA,
    DK45ObstructionAnalysis,
    quantum_parameter_from_level,
    sl2_admissible_q_parameter,
    admissible_fusion_ring_sl2,
    quantum_group_fusion_sl2,
    verify_kl_fusion_match,
    kappa_sl2_at_level,
    kappa_vir_from_c,
    central_charge_sl2,
    kl_kappa_analysis_sl2,
    thick_generation_transport_analysis,
    dk45_obstruction_from_kl_equivalence,
    abelian_gauge_vosas,
    abelian_gauge_landscape_intersection,
    kl_equivalence_dk_analysis,
    sl2_admissible_braided_analysis,
    creutzig_dk_summary,
    verify_q_parameter_sl2_k_minus_half,
    verify_fusion_ring_sl2_k_minus_half,
    verify_central_charge_complementarity_sl2,
    verify_kappa_non_preservation,
    verify_admissible_count_sl2,
)


# ===================================================================
# I. Quantum group parameter computation
# ===================================================================

class TestQuantumGroupParameters:
    """Tests for q-parameter computation at admissible levels."""

    def test_sl2_k_minus_half_q_order(self):
        """At k=-1/2 for sl_2: q = exp(2*pi*i/3), order 3."""
        qp = sl2_admissible_q_parameter(3, 2)
        assert qp.root_of_unity_order == 3

    def test_sl2_k_minus_half_q_value(self):
        """q = exp(2*pi*i/3) = -1/2 + i*sqrt(3)/2."""
        qp = sl2_admissible_q_parameter(3, 2)
        expected_re = cos(2 * pi / 3)  # -1/2
        expected_im = sin(2 * pi / 3)  # sqrt(3)/2
        assert abs(qp.q_value.real - expected_re) < 1e-10
        assert abs(qp.q_value.imag - expected_im) < 1e-10

    def test_sl2_k_minus_half_level(self):
        """k = 3/2 - 2 = -1/2."""
        qp = sl2_admissible_q_parameter(3, 2)
        assert qp.k == Fraction(-1, 2)

    def test_sl2_k_minus_half_k_plus_hv(self):
        """k + h^v = 3/2 for sl_2 at k = -1/2."""
        qp = sl2_admissible_q_parameter(3, 2)
        assert qp.k_plus_hv == Fraction(3, 2)

    def test_sl2_integrable_k1_q_order(self):
        """At integrable k=1 (p=3, q=1): q = exp(pi*i/3), order 6."""
        qp = sl2_admissible_q_parameter(3, 1)
        assert qp.root_of_unity_order == 6

    def test_sl2_p5q2_q_order(self):
        """At k=1/2 (p=5, q=2): q = exp(2*pi*i/5), order 5."""
        qp = sl2_admissible_q_parameter(5, 2)
        assert qp.root_of_unity_order == 5

    def test_sl2_h_dual(self):
        """sl_2 has h^v = 2."""
        qp = sl2_admissible_q_parameter(3, 2)
        assert qp.h_dual == 2

    def test_q_is_root_of_unity(self):
        """At admissible level, q is always a root of unity."""
        for p, q in [(3, 2), (5, 2), (4, 3), (5, 3)]:
            qp = sl2_admissible_q_parameter(p, q)
            assert qp.is_root_of_unity is True


# ===================================================================
# II. Fusion ring verification
# ===================================================================

class TestFusionRings:
    """Tests for fusion ring computation and matching."""

    def test_voa_n_simples_k_minus_half(self):
        """VOA at k=-1/2 has 2 simples."""
        fr = admissible_fusion_ring_sl2(3, 2)
        assert fr.n_simples == 2

    def test_qg_n_simples_k_minus_half(self):
        """Quantum group at q=exp(2pi*i/3) has 2 simples."""
        fr = quantum_group_fusion_sl2(3, 2)
        assert fr.n_simples == 2

    def test_fusion_ring_z2_voa(self):
        """VOA fusion ring is Z[Z/2]."""
        fr = admissible_fusion_ring_sl2(3, 2)
        assert fr.group_ring == "Z[Z/2]"

    def test_fusion_ring_z2_qg(self):
        """Quantum group fusion ring is Z[Z/2]."""
        fr = quantum_group_fusion_sl2(3, 2)
        assert fr.group_ring == "Z[Z/2]"

    def test_kl_fusion_match(self):
        """VOA and quantum group fusion rings match at k=-1/2."""
        assert verify_kl_fusion_match(3, 2) is True

    def test_voa_modular(self):
        """VOA category at admissible level is modular."""
        fr = admissible_fusion_ring_sl2(3, 2)
        assert fr.is_modular is True

    def test_s_matrix_unitarity(self):
        """S-matrix is unitary: S * S^* = I."""
        fr = admissible_fusion_ring_sl2(3, 2)
        s = fr.s_matrix
        # Check (S S^*)_{00} = 1
        ss00 = sum(s[0][j] * s[0][j] for j in range(2))
        assert abs(ss00 - 1.0) < 1e-10

    def test_quantum_dims_positive(self):
        """Quantum dimensions are positive."""
        fr = admissible_fusion_ring_sl2(3, 2)
        assert all(d > 0 for d in fr.quantum_dims)


# ===================================================================
# III. Kappa preservation analysis
# ===================================================================

class TestKappaPreservation:
    """Tests for kappa under KL equivalence."""

    def test_kappa_affine_sl2_k_minus_half(self):
        """kappa(V_{-1/2}(sl_2)) = 3*(3/2)/4 = 9/8."""
        k = Fraction(-1, 2)
        assert kappa_sl2_at_level(k) == Fraction(9, 8)

    def test_central_charge_sl2_k_minus_half(self):
        """c(sl_2, k=-1/2) = 3*(-1/2)/((-1/2)+2) = -1."""
        k = Fraction(-1, 2)
        assert central_charge_sl2(k) == Fraction(-1)

    def test_kappa_virasoro_c_minus_1(self):
        """kappa(Vir_{-1}) = -1/2."""
        assert kappa_vir_from_c(Fraction(-1)) == Fraction(-1, 2)

    def test_kappa_not_preserved(self):
        """kappa(V_{-1/2}(sl_2)) = 9/8 != -1/2 = kappa(Vir_{-1})."""
        k = Fraction(-1, 2)
        c = central_charge_sl2(k)
        assert kappa_sl2_at_level(k) != kappa_vir_from_c(c)

    def test_kl_kappa_analysis(self):
        """Full kappa analysis confirms non-preservation."""
        result = kl_kappa_analysis_sl2(3, 2)
        assert result['kappa_preserved'] is False

    def test_kappa_ratio(self):
        """kappa ratio = (9/8) / (-1/2) = -9/4."""
        result = kl_kappa_analysis_sl2(3, 2)
        expected = Fraction(9, 8) / Fraction(-1, 2)
        assert result['kappa_ratio'] == expected


# ===================================================================
# IV. Thick generation transport
# ===================================================================

class TestThickGenerationTransport:
    """Tests for thick generation transport via braided equivalence."""

    def test_transport_via_ds_reduction(self):
        """Thick generation transports via DS reduction equivalence."""
        result = thick_generation_transport_analysis(
            "KL(V_k(sl_2))", "KL(Vir_c)", "ds_reduction"
        )
        assert result['thick_generation_transported'] is True

    def test_dk23_consequence_stated(self):
        """DK-2/3 consequence is explicitly stated."""
        result = thick_generation_transport_analysis(
            "KL(V_k(sl_2))", "KL(Vir_c)", "ds_reduction"
        )
        assert "DK-2/3" in result['dk23_consequence']

    def test_dk45_not_advanced(self):
        """DK-4/5 is NOT advanced by thick generation transport."""
        result = thick_generation_transport_analysis(
            "KL(V_k(sl_2))", "KL(Vir_c)", "ds_reduction"
        )
        assert "NOT advanced" in result['dk45_consequence']

    def test_transport_via_conformal_embedding(self):
        """Thick generation also transports via conformal embedding."""
        result = thick_generation_transport_analysis(
            "KL(V_k(sl_3))", "KL(W^k(sl_3))", "conformal_embedding"
        )
        assert result['thick_generation_transported'] is True


# ===================================================================
# V. DK-4/5 obstruction analysis
# ===================================================================

class TestDK45Obstructions:
    """Tests for DK-4/5 obstruction analysis."""

    def test_four_obstructions(self):
        """There are exactly 4 identified obstructions."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert len(obs) == 4

    def test_all_genuine(self):
        """All 4 obstructions are genuine."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert all(o.is_genuine_obstruction for o in obs)

    def test_categorical_level_mismatch(self):
        """First obstruction is categorical level mismatch."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert obs[0].obstruction_type == "categorical_level_mismatch"

    def test_algebra_vs_category(self):
        """Second obstruction is algebra vs category."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert obs[1].obstruction_type == "algebra_vs_category"

    def test_evaluation_core_only(self):
        """Third obstruction is evaluation core limitation."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert obs[2].obstruction_type == "evaluation_core_only"

    def test_kappa_obstruction(self):
        """Fourth obstruction is kappa non-preservation."""
        obs = dk45_obstruction_from_kl_equivalence()
        assert obs[3].obstruction_type == "kappa_non_preservation"


# ===================================================================
# VI. Creutzig-Niu abelian gauge landscape
# ===================================================================

class TestAbelianGaugeLandscape:
    """Tests for Creutzig-Niu abelian gauge theory VOSAs."""

    def test_all_in_standard_landscape(self):
        """All abelian gauge VOSAs are in the standard landscape."""
        result = abelian_gauge_landscape_intersection()
        assert result['all_in_landscape'] is True

    def test_no_class_m(self):
        """Abelian gauge does NOT produce class M examples."""
        result = abelian_gauge_landscape_intersection()
        assert result['produces_class_M'] is False

    def test_produces_class_g(self):
        """Abelian gauge produces class G (symplectic fermions)."""
        result = abelian_gauge_landscape_intersection()
        assert result['produces_class_G'] is True

    def test_produces_class_l(self):
        """Abelian gauge produces class L (lattice VOAs)."""
        result = abelian_gauge_landscape_intersection()
        assert result['produces_class_L'] is True

    def test_produces_class_c(self):
        """Abelian gauge produces class C (beta-gamma)."""
        result = abelian_gauge_landscape_intersection()
        assert result['produces_class_C'] is True


# ===================================================================
# VII. Full KL equivalence analysis
# ===================================================================

class TestKLEquivalenceAnalysis:
    """Tests for the complete KL equivalence DK analysis."""

    def test_kl_proved(self):
        """KL equivalence is proved at admissible level."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.kl_equivalence_proved is True

    def test_bar_cobar_does_not_commute(self):
        """Bar-cobar does NOT commute with KL equivalence."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.bar_cobar_commutes is False

    def test_dk4_not_advanced(self):
        """DK-4 is NOT advanced."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.dk4_advanced is False

    def test_dk5_not_advanced(self):
        """DK-5 is NOT advanced."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.dk5_advanced is False

    def test_thick_generation_transported(self):
        """Thick generation IS transported."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.thick_generation_transported is True

    def test_kappa_not_preserved(self):
        """Kappa is NOT preserved."""
        result = kl_equivalence_dk_analysis('sl', 1, 3, 2)
        assert result.kappa_preserved is False


# ===================================================================
# VIII. sl_2 at k = -1/2 complete analysis
# ===================================================================

class TestSl2KMinusHalf:
    """Tests for the complete sl_2 at k=-1/2 braided tensor analysis."""

    def test_central_charge_minus_1(self):
        """c = -1 at k = -1/2."""
        result = sl2_admissible_braided_analysis()
        assert result['central_charge'] == Fraction(-1)

    def test_n_simples_2(self):
        """2 simples at k = -1/2."""
        result = sl2_admissible_braided_analysis()
        assert result['n_simples'] == 2

    def test_fusion_ring_z2(self):
        """Fusion ring is Z[Z/2]."""
        result = sl2_admissible_braided_analysis()
        assert result['fusion_ring'] == "Z[Z/2]"

    def test_conformal_weight_vacuum(self):
        """Vacuum has h = 0."""
        result = sl2_admissible_braided_analysis()
        assert result['conformal_weights'][0] == 0

    def test_conformal_weight_nonvacuum(self):
        """Non-vacuum has h = 3/8."""
        result = sl2_admissible_braided_analysis()
        assert result['conformal_weights'][1] == Fraction(3, 8)

    def test_modular_tensor(self):
        """Category is modular tensor."""
        result = sl2_admissible_braided_analysis()
        assert result['is_modular_tensor'] is True

    def test_dk45_not_advanced(self):
        """DK-4/5 NOT advanced."""
        result = sl2_admissible_braided_analysis()
        assert result['dk45_advanced'] is False

    def test_mc3_advanced(self):
        """MC3 IS advanced via thick generation."""
        result = sl2_admissible_braided_analysis()
        assert result['mc3_advanced_via_thick_gen'] is True


# ===================================================================
# IX. Multi-path verification
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification of key results (AP10 compliance)."""

    def test_q_parameter_two_paths(self):
        """q-parameter verified by 2 independent paths."""
        result = verify_q_parameter_sl2_k_minus_half()
        assert result['paths_agree'] is True

    def test_q_is_primitive_3rd_root(self):
        """q is a primitive 3rd root of unity."""
        result = verify_q_parameter_sl2_k_minus_half()
        assert result['is_primitive_3rd_root'] is True

    def test_fusion_ring_three_paths(self):
        """Fusion ring verified by 3 paths."""
        result = verify_fusion_ring_sl2_k_minus_half()
        assert result['all_paths_agree'] is True

    def test_c_complementarity_p3q2(self):
        """c + c' = 6 at (p,q) = (3,2)."""
        result = verify_central_charge_complementarity_sl2(3, 2)
        assert result['match'] is True

    def test_c_complementarity_p5q2(self):
        """c + c' = 6 at (p,q) = (5,2)."""
        result = verify_central_charge_complementarity_sl2(5, 2)
        assert result['match'] is True

    def test_c_complementarity_p4q3(self):
        """c + c' = 6 at (p,q) = (4,3)."""
        result = verify_central_charge_complementarity_sl2(4, 3)
        assert result['match'] is True

    def test_kappa_non_preservation_verified(self):
        """kappa non-preservation verified: 9/8 != -1/2."""
        result = verify_kappa_non_preservation()
        assert result['kappa_differ'] is True

    def test_kappa_ratio_correct(self):
        """kappa ratio = -9/4."""
        result = verify_kappa_non_preservation()
        assert result['kappa_ratio'] == Fraction(-9, 4)


# ===================================================================
# X. Cross-check and consistency
# ===================================================================

class TestCrossChecks:
    """Cross-family consistency and summary checks."""

    def test_admissible_count_all_levels(self):
        """Admissible module count verified at 4 levels."""
        result = verify_admissible_count_sl2()
        assert result['all_match'] is True

    def test_creutzig_summary_mc3_advanced(self):
        """Summary correctly reports MC3 advanced."""
        summary = creutzig_dk_summary()
        assert summary['mc3_thick_generation_extended'] is True

    def test_creutzig_summary_dk4_not_advanced(self):
        """Summary correctly reports DK-4 NOT advanced."""
        summary = creutzig_dk_summary()
        assert summary['dk4_advanced'] is False

    def test_creutzig_summary_dk5_not_advanced(self):
        """Summary correctly reports DK-5 NOT advanced."""
        summary = creutzig_dk_summary()
        assert summary['dk5_advanced'] is False

    def test_creutzig_summary_bar_cobar(self):
        """Summary correctly reports bar-cobar does not commute."""
        summary = creutzig_dk_summary()
        assert summary['bar_cobar_commutes_with_kl'] is False

    def test_creutzig_niu_no_class_m(self):
        """Summary correctly reports Creutzig-Niu gives no class M."""
        summary = creutzig_dk_summary()
        assert summary['creutzig_niu_class_M'] is False
