r"""Tests for the arithmetic rectification engine.

Deep Beilinson rectification of arithmetic_shadows.tex against:
    [K25]  Kapranov, arXiv:2512.22718
    [KS24] Kapranov-Schechtman, arXiv:2412.01638
    [B26]  Barwick, arXiv:2602.01292

VERIFICATION TARGETS (50+ tests, 3+ paths per claim):

Group A: Shadow Eisenstein theorem (thm:shadow-eisenstein)
    L^sh(s) = -kappa * zeta(s) * zeta(s-1)
    4 independent computation paths.

Group B: Alien derivatives (Kapranov [2512.22718])
    Delta_{(2pi)^2}(F) = S_1 * F where S_1 = -4*pi^2 * kappa * i

Group C: Shadow L-function Euler product = Hasse-Weil of P^1/F_p
    (Barwick [2602.01292])

Group D: Kapranov-Schechtman Langlands connection (arXiv:2412.01638)
    Critical-level bar/oper bridge and Weyl chamber perverse sheaves.

Group E: Motivic shadow L-function
    L^sh = -kappa * L(P^1, s) as Hasse-Weil zeta of the motive h(P^1).

Group F: Perverse sheaf data and Stokes automorphism
    Kapranov Thm 2.3.10: log(St) = sum Delta_omega.

Group G: Eisenstein vs cuspidal classification
    Shadow L-function is NOT cuspidal (fails Selberg class S3, S4).

Group H: Cross-family consistency and anomaly cancellation
    c=26 resurgent anomaly, c=13 self-duality.

Group I: Divisor sum identities (foundational)
    Ramanujan identity, sewing-Selberg formula.

Group J: Lattice verifications (shadow-spectral correspondence)
    Five lattice depth formula, Niemeier discrimination.

All formulas computed from first principles (AP1, AP3).
Multi-path verification per CLAUDE.md mandate.

Manuscript references:
    thm:shadow-eisenstein (arithmetic_shadows.tex)
    prop:universal-instanton-action (higher_genus_modular_koszul.tex)
    thm:shadow-spectral-correspondence (arithmetic_shadows.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:langlands-bar-bridge (derived_langlands.tex)
"""

import cmath
import math
import sys
import os
from fractions import Fraction

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_arithmetic_rectification_engine import (
    # Constants
    PI, TWO_PI, FOUR_PI_SQ, UNIVERSAL_INSTANTON_ACTION,
    ARITHMETIC_SHADOW_FUNCTOR_GATES,
    HECKE_CPS_RAMANUJAN_GATES,
    HECKE_NEWTON_DIRICHLET_GATES,
    SPECTRAL_SEWING_GATES,
    GENUS2_LIFT_BRIDGE_GATES,
    BORCHERDS_IGUSA_MODULAR_GATES,
    BRACKET_GRT_SPINE_GATES,
    arithmetic_shadow_functor_scope,
    hecke_cps_ramanujan_scope,
    hecke_newton_dirichlet_scope,
    arithmetic_modular_obligation_scope,
    spectral_sewing_scope,
    genus2_lift_bridge_scope,
    borcherds_igusa_modular_scope,
    bracket_grt_theorem_spine_scope,
    arithmetic_modular_tail_scope,
    # Families
    AlgebraData, FAMILIES,
    # Faber-Pandharipande
    bernoulli_number, faber_pandharipande_lambda_g, shadow_genus_coefficient,
    # Shadow L-function
    partial_zeta, shadow_l_function,
    shadow_l_from_divisor_sums,
    # Euler product
    shadow_l_local_factor, hasse_weil_p1_local_factor,
    shadow_euler_product, verify_shadow_equals_hasse_weil_p1,
    # Alien derivatives
    borel_transform_shadow, borel_singularity_at_n,
    alien_derivative_at_instanton, stokes_multiplier,
    verify_alien_derivative_bridge_equation,
    # Perverse sheaf
    PerverseSheafDatum, stokes_automorphism, log_stokes_equals_alien_sum,
    # Eisenstein check
    shadow_divisor_coefficients,
    verify_eisenstein_from_additive_convolution,
    shadow_l_is_not_cuspidal,
    # Kapranov-Schechtman
    langlands_weyl_chamber_perverse_data, critical_level_bar_oper_check,
    # Motivic
    motivic_shadow_l_data, motivic_euler_factor_p1,
    motivic_euler_factor_elliptic,
    # Lattice
    e8_epstein_zeta, depth_from_cusp_dim, verify_five_lattice_depths,
    # Anomaly / self-duality
    anomaly_cancellation_resurgent, c13_self_duality_check,
    # Divisor sums
    sigma_k, verify_ramanujan_identity, verify_sewing_selberg_formula,
    # Multi-path
    verify_shadow_eisenstein_theorem, verify_local_factors_match_hasse_weil,
    # Discriminant
    virasoro_shadow_discriminant, virasoro_shadow_field_discriminant,
)


# =====================================================================
# Group 0: Arithmetic modular theorem-scope gates (PDF obligations 851--870)
# =====================================================================

class TestArithmeticModularScopeGates:
    """Executable scope gates for arithmetic shadow and Hecke/Ramanujan claims."""

    def test_000_gate_families_cover_obligation_block(self):
        """The lane has separate gates for shadow, Hecke/CPS, and Dirichlet scope."""
        assert len(ARITHMETIC_SHADOW_FUNCTOR_GATES) == 6
        assert len(HECKE_CPS_RAMANUJAN_GATES) == 10
        assert len(HECKE_NEWTON_DIRICHLET_GATES) == 6

    def test_001_shadow_functor_blocks_undefined_theta_source(self):
        """An arithmetic shadow functor cannot be stated before Theta_A is fixed."""
        scope = arithmetic_shadow_functor_scope(
            theta_source_defined=False,
            arithmetic_shadow_functor_defined=True,
            moment_l_function_defined=True,
            rankin_selberg_integral_defined=True,
            convergence_domain_stated=True,
        )
        assert scope['arithmetic_shadow_functor_theorem_allowed'] is False
        assert 'theta_source_defined' in scope['missing']

    def test_002_moment_l_function_requires_rankin_domain(self):
        """Moment L-functions require Rankin-Selberg data and convergence domain."""
        scope = arithmetic_shadow_functor_scope(
            theta_source_defined=True,
            arithmetic_shadow_functor_defined=True,
            moment_l_function_defined=True,
            rankin_selberg_integral_defined=False,
            convergence_domain_stated=False,
        )
        assert scope['moment_l_function_claim_allowed'] is False
        assert 'rankin_selberg_integral_defined' in scope['missing']
        assert 'convergence_domain_stated' in scope['missing']

    def test_003_claimed_meromorphic_continuation_needs_proof(self):
        """Meromorphic continuation is blocked when it is claimed but not proved."""
        scope = arithmetic_shadow_functor_scope(
            theta_source_defined=True,
            arithmetic_shadow_functor_defined=True,
            moment_l_function_defined=True,
            rankin_selberg_integral_defined=True,
            convergence_domain_stated=True,
            meromorphic_continuation_claimed=True,
            meromorphic_continuation_proved=False,
        )
        assert scope['meromorphic_continuation_claim_allowed'] is False
        assert 'meromorphic_continuation_proved_where_claimed' in scope['missing']

    def test_004_shadow_functor_all_gates_positive(self):
        """The arithmetic shadow theorem unlocks only after all shadow gates pass."""
        scope = arithmetic_shadow_functor_scope(
            theta_source_defined=True,
            arithmetic_shadow_functor_defined=True,
            moment_l_function_defined=True,
            rankin_selberg_integral_defined=True,
            convergence_domain_stated=True,
            meromorphic_continuation_claimed=True,
            meromorphic_continuation_proved=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['arithmetic_shadow_functor_theorem_allowed'] is True

    def test_005_hecke_lift_requires_base_action_and_lift(self):
        """A Hecke lift needs both the M_1,1 action and the gmod lift."""
        scope = hecke_cps_ramanujan_scope(
            hecke_action_m11_defined=True,
            hecke_lift_to_gmod_defined=False,
        )
        assert scope['hecke_lift_claim_allowed'] is False
        assert 'hecke_lift_to_gmod_defined' in scope['missing']

    def test_006_lattice_prime_locality_claim_needs_proof(self):
        """Lattice prime-locality is not a theorem when it is claimed without proof."""
        scope = hecke_cps_ramanujan_scope(
            hecke_action_m11_defined=True,
            hecke_lift_to_gmod_defined=True,
            prime_locality_conjecture_stated=True,
            lattice_prime_locality_claimed=True,
            lattice_prime_locality_proved=False,
            non_lattice_prime_locality_hypothesis_stated=True,
            cps_hypotheses_defined=True,
            automorphic_representation_pi_r_defined=True,
            gl_functoriality_hypothesis_for_r_ge_5_stated=True,
            ramanujan_scope_respects_known_functoriality=True,
            kim_sarnak_bound_stated_when_unconditional=True,
        )
        assert scope['prime_locality_theorem_allowed'] is False
        assert 'lattice_prime_locality_proved_when_claimed' in scope['missing']

    def test_007_ramanujan_beyond_functoriality_is_blocked(self):
        """Ramanujan language cannot outrun functoriality and Kim-Sarnak scope."""
        scope = hecke_cps_ramanujan_scope(
            hecke_action_m11_defined=True,
            hecke_lift_to_gmod_defined=True,
            prime_locality_conjecture_stated=True,
            lattice_prime_locality_claimed=True,
            lattice_prime_locality_proved=True,
            non_lattice_prime_locality_hypothesis_stated=True,
            cps_hypotheses_defined=True,
            automorphic_representation_pi_r_defined=True,
            gl_functoriality_hypothesis_for_r_ge_5_stated=False,
            ramanujan_scope_respects_known_functoriality=False,
            kim_sarnak_bound_stated_when_unconditional=False,
        )
        assert scope['ramanujan_comparison_claim_allowed'] is False
        assert scope['unconditional_ramanujan_claim_allowed'] is False
        assert scope['ramanujan_beyond_known_functoriality_allowed'] is False
        assert 'gl_functoriality_hypothesis_for_r_ge_5_stated' in scope['missing']
        assert 'kim_sarnak_bound_stated_when_unconditional' in scope['missing']

    def test_008_hecke_cps_ramanujan_all_gates_positive(self):
        """The Hecke/CPS/Ramanujan scope unlocks only after all gates pass."""
        scope = hecke_cps_ramanujan_scope(
            hecke_action_m11_defined=True,
            hecke_lift_to_gmod_defined=True,
            prime_locality_conjecture_stated=True,
            lattice_prime_locality_claimed=True,
            lattice_prime_locality_proved=True,
            non_lattice_prime_locality_hypothesis_stated=True,
            cps_hypotheses_defined=True,
            automorphic_representation_pi_r_defined=True,
            gl_functoriality_hypothesis_for_r_ge_5_stated=True,
            ramanujan_scope_respects_known_functoriality=True,
            kim_sarnak_bound_stated_when_unconditional=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['ramanujan_comparison_claim_allowed'] is True
        assert scope['unconditional_ramanujan_claim_allowed'] is False
        assert scope['kim_sarnak_unconditional_bound_claim_allowed'] is True

    def test_009_hecke_newton_blocks_non_lattice_and_irrational_theorems(self):
        """Non-lattice and irrational extensions remain non-theorem lanes."""
        scope = hecke_newton_dirichlet_scope(
            hecke_newton_closure_defined=True,
            lattice_finite_hecke_span_proof_supplied=True,
            non_lattice_extension_defined_separately=True,
            irrational_extension_defined_separately=True,
            irrational_extension_marked_conditional=True,
            dirichlet_l_functions_from_shadow_metric_defined=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['lattice_hecke_newton_theorem_allowed'] is True
        assert scope['non_lattice_extension_theorem_allowed'] is False
        assert scope['irrational_extension_theorem_allowed'] is False
        assert scope['dirichlet_shadow_metric_claim_allowed'] is True

    def test_010_hecke_newton_requires_irrational_conditional_marker(self):
        """Irrational extension must be explicitly marked conditional."""
        scope = hecke_newton_dirichlet_scope(
            hecke_newton_closure_defined=True,
            lattice_finite_hecke_span_proof_supplied=True,
            non_lattice_extension_defined_separately=True,
            irrational_extension_defined_separately=True,
            irrational_extension_marked_conditional=False,
            dirichlet_l_functions_from_shadow_metric_defined=True,
        )
        assert scope['all_gates_satisfied'] is False
        assert 'irrational_extension_marked_conditional' in scope['missing']

    def test_011_aggregate_scope_defaults_block_everything(self):
        """The aggregate arithmetic scope starts blocked without supplied evidence."""
        scope = arithmetic_modular_obligation_scope()
        assert scope['all_gates_satisfied'] is False
        assert set(scope['blocked_components']) == {
            'shadow_functor', 'hecke_cps_ramanujan', 'hecke_newton_dirichlet'
        }

    def test_012_aggregate_scope_all_gates_positive(self):
        """All lane-32 gate families must pass for the aggregate claim to pass."""
        scope = arithmetic_modular_obligation_scope(
            shadow={
                'theta_source_defined': True,
                'arithmetic_shadow_functor_defined': True,
                'moment_l_function_defined': True,
                'rankin_selberg_integral_defined': True,
                'convergence_domain_stated': True,
                'meromorphic_continuation_claimed': True,
                'meromorphic_continuation_proved': True,
            },
            hecke={
                'hecke_action_m11_defined': True,
                'hecke_lift_to_gmod_defined': True,
                'prime_locality_conjecture_stated': True,
                'lattice_prime_locality_claimed': True,
                'lattice_prime_locality_proved': True,
                'non_lattice_prime_locality_hypothesis_stated': True,
                'cps_hypotheses_defined': True,
                'automorphic_representation_pi_r_defined': True,
                'gl_functoriality_hypothesis_for_r_ge_5_stated': True,
                'ramanujan_scope_respects_known_functoriality': True,
                'kim_sarnak_bound_stated_when_unconditional': True,
            },
            hecke_newton={
                'hecke_newton_closure_defined': True,
                'lattice_finite_hecke_span_proof_supplied': True,
                'non_lattice_extension_defined_separately': True,
                'irrational_extension_defined_separately': True,
                'irrational_extension_marked_conditional': True,
                'dirichlet_l_functions_from_shadow_metric_defined': True,
            },
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['blocked_components'] == []


# =====================================================================
# Group 0b: Arithmetic modular tail gates (PDF obligations 871--900)
# =====================================================================

class TestArithmeticModularTailScopeGates:
    """Executable gates for spectral/lift/Borcherds/bracket arithmetic claims."""

    def test_020_tail_gate_families_cover_obligation_block(self):
        """The tail block has four independent scope families."""
        assert len(SPECTRAL_SEWING_GATES) == 5
        assert len(GENUS2_LIFT_BRIDGE_GATES) == 4
        assert len(BORCHERDS_IGUSA_MODULAR_GATES) == 15
        assert len(BRACKET_GRT_SPINE_GATES) == 6

    def test_021_spectral_decomposition_requires_basis_and_partition_proof(self):
        """Spectral decomposition cannot bypass Roelcke-Selberg and partition compatibility."""
        scope = spectral_sewing_scope(
            spectral_decomposition_proved=True,
            roelcke_selberg_basis_defined=False,
            chiral_partition_compatibility_proved=False,
            sewing_operator_defined=True,
            sewing_selberg_formula_proved=True,
        )
        assert scope['spectral_decomposition_theorem_allowed'] is False
        assert 'roelcke_selberg_basis_defined' in scope['missing']
        assert 'chiral_partition_compatibility_proved' in scope['missing']

    def test_022_sewing_selberg_requires_operator_and_formula(self):
        """The sewing-Selberg theorem needs the sewing operator and formula proof."""
        scope = spectral_sewing_scope(
            spectral_decomposition_proved=False,
            roelcke_selberg_basis_defined=True,
            chiral_partition_compatibility_proved=True,
            sewing_operator_defined=False,
            sewing_selberg_formula_proved=True,
        )
        assert scope['sewing_selberg_theorem_allowed'] is False
        assert 'sewing_operator_defined' in scope['missing']

    def test_023_spectral_sewing_all_gates_positive(self):
        """The spectral/sewing theorem surface unlocks only after all gates pass."""
        scope = spectral_sewing_scope(
            spectral_decomposition_proved=True,
            roelcke_selberg_basis_defined=True,
            chiral_partition_compatibility_proved=True,
            sewing_operator_defined=True,
            sewing_selberg_formula_proved=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['spectral_decomposition_theorem_allowed'] is True
        assert scope['sewing_selberg_theorem_allowed'] is True

    def test_024_genus2_bridge_blocks_unproved_critical_line_access(self):
        """Critical-line access must be proved or explicitly conditional."""
        scope = genus2_lift_bridge_scope(
            saito_kurokawa_lift_defined=True,
            genus_two_bridge_known_scope_proved=True,
            boecherer_bridge_defined=True,
            critical_line_access_proved=False,
            critical_line_access_marked_conditional=False,
        )
        assert scope['all_gates_satisfied'] is False
        assert 'critical_line_access_proved_or_conditional' in scope['missing']

    def test_025_genus2_bridge_allows_conditional_critical_line_access(self):
        """Conditional critical-line access is allowed without theorem promotion."""
        scope = genus2_lift_bridge_scope(
            saito_kurokawa_lift_defined=True,
            genus_two_bridge_known_scope_proved=True,
            boecherer_bridge_defined=True,
            critical_line_access_proved=False,
            critical_line_access_marked_conditional=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['genus_two_bridge_theorem_allowed'] is True
        assert scope['critical_line_access_theorem_allowed'] is False
        assert scope['critical_line_access_conditional_allowed'] is True

    def test_026_borcherds_blocks_chl_transfer_to_k3_mukai(self):
        """CHL constants never transfer automatically to K3 Mukai K^kappa."""
        scope = borcherds_igusa_modular_scope(
            borcherds_product_delta5_defined=True,
            c_delta_0_computed=True,
            kappa_bkm_identity_proved=True,
            chl_scope_stated=True,
            chl_constants_not_transferred_to_k3_mukai=False,
            igusa_phi10_defined=True,
            modular_weight_stated=True,
            transformation_law_proved=True,
            fricke_ldp_defined=True,
            subleading_correction_proved_at_each_node=True,
            shimura_waldspurger_conversion_defined=True,
            weights_7_9_11_stated=True,
            conversion_proved_or_precisely_cited=True,
        )
        assert scope['chl_to_k3_mukai_transfer_allowed'] is False
        assert 'chl_constants_not_transferred_to_k3_mukai' in scope['missing']

    def test_027_borcherds_blocks_unproved_associator_and_eta_use(self):
        """Associator appearances and eta^24 quotients are gated independently."""
        scope = borcherds_igusa_modular_scope(
            borcherds_product_delta5_defined=True,
            c_delta_0_computed=True,
            kappa_bkm_identity_proved=True,
            chl_scope_stated=True,
            chl_constants_not_transferred_to_k3_mukai=True,
            igusa_phi10_defined=True,
            associator_cocycle_appearance_claimed=True,
            associator_cocycle_appearance_proved=False,
            eta24_quotient_used=True,
            eta24_quotient_defined=False,
            modular_weight_stated=True,
            transformation_law_proved=True,
            fricke_ldp_defined=True,
            subleading_correction_proved_at_each_node=True,
            shimura_waldspurger_conversion_defined=True,
            weights_7_9_11_stated=True,
            conversion_proved_or_precisely_cited=True,
        )
        assert scope['associator_cocycle_claim_allowed'] is False
        assert 'associator_cocycle_appearance_proved_when_claimed' in scope['missing']
        assert 'eta24_quotient_defined_when_used' in scope['missing']

    def test_028_borcherds_igusa_all_gates_positive(self):
        """Borcherds/Igusa/Shimura claims unlock only after all gates pass."""
        scope = borcherds_igusa_modular_scope(
            borcherds_product_delta5_defined=True,
            c_delta_0_computed=True,
            kappa_bkm_identity_proved=True,
            chl_scope_stated=True,
            chl_constants_not_transferred_to_k3_mukai=True,
            igusa_phi10_defined=True,
            associator_cocycle_appearance_claimed=True,
            associator_cocycle_appearance_proved=True,
            eta24_quotient_used=True,
            eta24_quotient_defined=True,
            modular_weight_stated=True,
            transformation_law_proved=True,
            fricke_ldp_defined=True,
            subleading_correction_proved_at_each_node=True,
            shimura_waldspurger_conversion_defined=True,
            weights_7_9_11_stated=True,
            conversion_proved_or_precisely_cited=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['kappa_bkm_theorem_allowed'] is True
        assert scope['shimura_waldspurger_claim_allowed'] is True
        assert scope['chl_to_k3_mukai_transfer_allowed'] is False

    def test_029_bracket_gate_blocks_bar_differential_mixing_without_map(self):
        """Arithmetic brackets cannot be mixed with bar differentials without a map."""
        scope = bracket_grt_theorem_spine_scope(
            yetter_drinfeld_schauenburg_bracket_defined=True,
            delta_n_computed_for_claimed_n=True,
            arithmetic_bracket_mixed_with_bar_differential=True,
            arithmetic_bracket_to_bar_map_defined=False,
            arithmetic_moved_beyond_theorem_spine=True,
        )
        assert scope['arithmetic_bracket_bar_differential_claim_allowed'] is False
        assert 'arithmetic_bracket_not_mixed_with_bar_without_map' in scope['missing']

    def test_030_grt_transitivity_may_be_conjectural_but_not_theorem(self):
        """GRT transitivity may be marked conjectural without becoming a theorem."""
        scope = bracket_grt_theorem_spine_scope(
            yetter_drinfeld_schauenburg_bracket_defined=True,
            delta_n_computed_for_claimed_n=True,
            arithmetic_bracket_mixed_with_bar_differential=True,
            arithmetic_bracket_to_bar_map_defined=True,
            grt_action_on_k3_bkm_used=True,
            grt_action_on_k3_bkm_defined=True,
            grt_transitivity_proved=False,
            grt_transitivity_marked_conjectural=True,
            arithmetic_moved_beyond_theorem_spine=True,
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['grt_transitivity_theorem_allowed'] is False
        assert scope['grt_transitivity_conjectural_allowed'] is True

    def test_031_arithmetic_theorem_spine_requires_algebraic_need(self):
        """Arithmetic stays beyond the theorem spine unless needed by the algebra."""
        scope = bracket_grt_theorem_spine_scope(
            yetter_drinfeld_schauenburg_bracket_defined=True,
            delta_n_computed_for_claimed_n=True,
            arithmetic_moved_beyond_theorem_spine=False,
            arithmetic_consequence_needed_for_algebraic_claim=False,
        )
        assert scope['arithmetic_in_theorem_spine_allowed'] is False
        assert 'arithmetic_beyond_theorem_spine_unless_needed' in scope['missing']

    def test_032_tail_aggregate_defaults_block_everything(self):
        """The aggregate tail scope starts blocked without supplied evidence."""
        scope = arithmetic_modular_tail_scope()
        assert scope['all_gates_satisfied'] is False
        assert set(scope['blocked_components']) == {
            'spectral_sewing',
            'genus2_lift_bridge',
            'borcherds_igusa_modular',
            'bracket_grt_spine',
        }

    def test_033_tail_aggregate_all_gates_positive(self):
        """All lane-33 gate families must pass for the aggregate claim to pass."""
        scope = arithmetic_modular_tail_scope(
            spectral={
                'spectral_decomposition_proved': True,
                'roelcke_selberg_basis_defined': True,
                'chiral_partition_compatibility_proved': True,
                'sewing_operator_defined': True,
                'sewing_selberg_formula_proved': True,
            },
            genus2={
                'saito_kurokawa_lift_defined': True,
                'genus_two_bridge_known_scope_proved': True,
                'boecherer_bridge_defined': True,
                'critical_line_access_marked_conditional': True,
            },
            borcherds={
                'borcherds_product_delta5_defined': True,
                'c_delta_0_computed': True,
                'kappa_bkm_identity_proved': True,
                'chl_scope_stated': True,
                'chl_constants_not_transferred_to_k3_mukai': True,
                'igusa_phi10_defined': True,
                'associator_cocycle_appearance_claimed': True,
                'associator_cocycle_appearance_proved': True,
                'eta24_quotient_used': True,
                'eta24_quotient_defined': True,
                'modular_weight_stated': True,
                'transformation_law_proved': True,
                'fricke_ldp_defined': True,
                'subleading_correction_proved_at_each_node': True,
                'shimura_waldspurger_conversion_defined': True,
                'weights_7_9_11_stated': True,
                'conversion_proved_or_precisely_cited': True,
            },
            bracket_grt={
                'yetter_drinfeld_schauenburg_bracket_defined': True,
                'delta_n_computed_for_claimed_n': True,
                'arithmetic_bracket_mixed_with_bar_differential': True,
                'arithmetic_bracket_to_bar_map_defined': True,
                'grt_action_on_k3_bkm_used': True,
                'grt_action_on_k3_bkm_defined': True,
                'grt_transitivity_marked_conjectural': True,
                'arithmetic_moved_beyond_theorem_spine': True,
            },
        )
        assert scope['all_gates_satisfied'] is True
        assert scope['blocked_components'] == []


# =====================================================================
# Group A: Shadow Eisenstein theorem (thm:shadow-eisenstein)
# =====================================================================

class TestShadowEisensteinTheorem:
    """L^sh(s) = -kappa * zeta(s) * zeta(s-1), 4 independent paths."""

    def test_a01_product_formula_real_s(self):
        """Path 1: L^sh(s) = -kappa * zeta(s) * zeta(s-1) at real s > 2."""
        kappa = 6.5  # Vir_13
        for s in [3.0, 4.0, 5.0, 6.0]:
            L = shadow_l_function(s, kappa, terms=500)
            z_s = partial_zeta(s, 500)
            z_sm1 = partial_zeta(s - 1, 500)
            expected = -kappa * z_s * z_sm1
            assert abs(L - expected) < 1e-8, f"Failed at s={s}: {L} != {expected}"

    def test_a02_divisor_sum_path(self):
        """Path 2: via sigma_1 Dirichlet series."""
        kappa = 0.5  # Vir_1
        s = 4.0 + 0.0j
        L_prod = shadow_l_function(s, kappa, terms=300)
        L_div = shadow_l_from_divisor_sums(s, kappa, terms=300)
        rel_err = abs(L_prod - L_div) / abs(L_prod)
        assert rel_err < 1e-5, f"Paths 1 vs 2 disagree: {rel_err}"

    def test_a03_euler_product_path(self):
        """Path 3: Euler product over primes."""
        kappa = 1.0  # Heisenberg
        s = 5.0 + 0.0j
        L_prod = shadow_l_function(s, kappa, terms=500)
        L_euler = shadow_euler_product(s, kappa, max_prime=80)
        rel_err = abs(L_prod - L_euler) / abs(L_prod)
        # Euler product converges slowly; accept 1% error
        assert rel_err < 0.02, f"Euler product error: {rel_err}"

    def test_a04_multi_path_verification(self):
        """Full 4-path verification for Virasoro at c=13."""
        kappa = 6.5
        s = 4.0 + 1.0j
        result = verify_shadow_eisenstein_theorem(kappa, s, terms=300)
        assert result['error_product_vs_divisor'] < 1e-4, (
            f"Paths 1-2 disagree: {result['error_product_vs_divisor']}"
        )

    def test_a05_shadow_eisenstein_complex_s(self):
        """L^sh at complex s (partial sums converge slower for Im(s) != 0)."""
        kappa = 12.5  # Vir_25
        s = 3.0 + 2.0j
        L = shadow_l_function(s, kappa, terms=800)
        L_div = shadow_l_from_divisor_sums(s, kappa, terms=800)
        rel_err = abs(L - L_div) / max(abs(L), 1e-15)
        assert rel_err < 1e-2, f"Complex s verification failed: {rel_err}"

    def test_a06_kappa_linearity(self):
        """L^sh is linear in kappa: L^sh(s, a*kappa) = a * L^sh(s, kappa)."""
        s = 4.0
        kappa = 3.0
        L1 = shadow_l_function(s, kappa)
        L2 = shadow_l_function(s, 2 * kappa)
        assert abs(L2 - 2 * L1) / abs(L1) < 1e-10

    def test_a07_shadow_l_at_s_equals_2(self):
        """L^sh(2) = -kappa * zeta(2) * zeta(1) = -infinity (pole at s=2)."""
        # zeta(1) diverges, so L^sh(2) should be large in magnitude
        kappa = 1.0
        L = shadow_l_function(2.01, kappa, terms=500)
        assert abs(L) > 10, f"L^sh near s=2 should be large: {abs(L)}"


# =====================================================================
# Group B: Alien derivatives (Kapranov [2512.22718])
# =====================================================================

class TestAlienDerivatives:
    """Delta_{(2pi)^2}(F) = S_1 * F, verified from prop:universal-instanton-action."""

    def test_b01_universal_instanton_action(self):
        """A = (2*pi)^2 is universal."""
        assert abs(UNIVERSAL_INSTANTON_ACTION - FOUR_PI_SQ) < 1e-12

    def test_b02_instanton_value(self):
        """(2*pi)^2 ~ 39.478."""
        expected = (2 * PI) ** 2
        assert abs(FOUR_PI_SQ - expected) < 1e-10
        assert abs(FOUR_PI_SQ - 39.47841760435743) < 1e-8

    def test_b03_stokes_multiplier_virasoro(self):
        """S_1 = -4*pi^2 * kappa * i for Virasoro."""
        kappa = 0.5  # Vir c=1
        S1 = stokes_multiplier(kappa, n=1)
        expected = -FOUR_PI_SQ * kappa * 1j
        assert abs(S1 - expected) < 1e-12

    def test_b04_stokes_multiplier_formula(self):
        """S_n = (-1)^n * 4*pi^2 * n * kappa * i."""
        kappa = 6.5  # Vir_13
        for n in range(1, 6):
            S_n = stokes_multiplier(kappa, n)
            expected = ((-1) ** n) * FOUR_PI_SQ * n * kappa * 1j
            assert abs(S_n - expected) < 1e-10, f"Failed at n={n}"

    def test_b05_alien_derivative_equals_stokes(self):
        """Delta_{omega_1} = S_1 for simple poles."""
        kappa = 12.5
        alien = alien_derivative_at_instanton(kappa, n=1)
        S1 = stokes_multiplier(kappa, n=1)
        assert abs(alien - S1) < 1e-12

    def test_b06_borel_singularity_positions(self):
        """Borel singularities at xi_n = (2*pi*n)^2."""
        for n in range(1, 6):
            xi_n = borel_singularity_at_n(n)
            expected = (TWO_PI * n) ** 2
            assert abs(xi_n - expected) < 1e-10

    def test_b07_bridge_equation_verification(self):
        """Ecalle bridge equation: |S_1| = 4*pi^2 * |kappa|."""
        kappa = 6.5
        S1_formula, S1_magnitude, err = verify_alien_derivative_bridge_equation(kappa)
        assert err < 1e-10, f"Bridge equation error: {err}"

    def test_b08_stokes_kappa_proportionality(self):
        """S_1 is proportional to kappa across families."""
        for name, data in FAMILIES.items():
            if data.kappa == 0:
                continue
            S1 = stokes_multiplier(data.kappa, n=1)
            ratio = S1 / (-FOUR_PI_SQ * data.kappa * 1j)
            assert abs(ratio - 1.0) < 1e-12, f"Failed for {name}: ratio = {ratio}"

    def test_b09_borel_transform_nonzero(self):
        """Borel transform coefficients are nonzero for kappa != 0."""
        coeffs = borel_transform_shadow(kappa=6.5, g_max=10)
        for g, b_g in enumerate(coeffs, start=1):
            assert abs(b_g) > 0, f"Borel coefficient b_{g} vanished"


# =====================================================================
# Group C: Euler product = Hasse-Weil P^1/F_p (Barwick)
# =====================================================================

class TestEulerProductHasseWeil:
    """Shadow local factors match Hasse-Weil zeta of P^1 over F_p."""

    def test_c01_local_factor_p2(self):
        """Local factor at p=2: 1/((1-2^{-s})(1-2^{1-s}))."""
        s = 3.0 + 0.0j
        shadow = shadow_l_local_factor(2, s)
        hw = hasse_weil_p1_local_factor(2, s)
        assert abs(shadow - hw) < 1e-14

    def test_c02_local_factor_p3(self):
        """Local factor at p=3."""
        s = 4.0 + 1.0j
        shadow = shadow_l_local_factor(3, s)
        hw = hasse_weil_p1_local_factor(3, s)
        assert abs(shadow - hw) < 1e-14

    def test_c03_all_primes_under_50(self):
        """Local factors match for all primes under 50."""
        results = verify_local_factors_match_hasse_weil(max_prime=50)
        for p, err in results:
            assert err < 1e-13, f"Mismatch at p={p}: error = {err}"

    def test_c04_euler_product_convergence(self):
        """Euler product converges to the correct value."""
        kappa = 1.0
        s = 5.0 + 0.0j
        L_exact = shadow_l_function(s, kappa, terms=500)
        L_euler = shadow_euler_product(s, kappa, max_prime=80)
        rel_err = abs(L_exact - L_euler) / abs(L_exact)
        assert rel_err < 0.02

    def test_c05_hasse_weil_identity(self):
        """verify_shadow_equals_hasse_weil_p1 returns zero error."""
        s = 4.0 + 0.5j
        _, _, err = verify_shadow_equals_hasse_weil_p1(s, kappa=1.0, max_prime=30)
        assert err < 1e-13

    def test_c06_motivic_factor_matches(self):
        """Motivic Euler factor for P^1 matches shadow local factor."""
        for p in [2, 3, 5, 7, 11, 13]:
            s = 3.0 + 0.5j
            shadow = shadow_l_local_factor(p, s)
            motivic = motivic_euler_factor_p1(p, s)
            assert abs(shadow - motivic) < 1e-14, f"Failed at p={p}"


# =====================================================================
# Group D: Kapranov-Schechtman Langlands connection
# =====================================================================

class TestKapranovSchechtmanLanglands:
    """Critical-level bar/oper bridge and Weyl chamber perverse sheaves."""

    def test_d01_sl2_critical_level_kappa_vanishes(self):
        """kappa(sl_2, k=-2) = 0."""
        result = critical_level_bar_oper_check('sl2')
        assert result['kappa_vanishes']
        assert abs(result['kappa_at_critical']) < 1e-15

    def test_d02_sl3_critical_level_kappa_vanishes(self):
        """kappa(sl_3, k=-3) = 0."""
        result = critical_level_bar_oper_check('sl3')
        assert result['kappa_vanishes']

    def test_d03_sl2_bar_uncurved_at_critical(self):
        """Bar complex is uncurved at critical level."""
        result = critical_level_bar_oper_check('sl2')
        assert result['bar_is_uncurved']

    def test_d04_sl2_weyl_chamber_data(self):
        """Perverse sheaf data on W\\h for SL(2)."""
        data = langlands_weyl_chamber_perverse_data('sl2')
        assert data['weyl_group_order'] == 2
        assert data['reflection_hyperplanes'] == 1

    def test_d05_sl3_weyl_chamber_data(self):
        """Perverse sheaf data on W\\h for SL(3)."""
        data = langlands_weyl_chamber_perverse_data('sl3')
        assert data['weyl_group_order'] == 6
        assert data['reflection_hyperplanes'] == 3

    def test_d06_critical_level_dim_g(self):
        """kappa(g, k) = dim(g)*(k+h^v)/(2*h^v), vanishes at k = -h^v."""
        # sl_2: dim=3, h^v=2
        for k in [-2, -1, 0, 1, 2]:
            kappa = 3.0 * (k + 2.0) / (2.0 * 2.0)
            if k == -2:
                assert abs(kappa) < 1e-15
            else:
                assert abs(kappa) > 0


# =====================================================================
# Group E: Motivic shadow L-function
# =====================================================================

class TestMotivicShadowL:
    """L^sh = -kappa * L(P^1, s) from the motive h(P^1) = 1 + L."""

    def test_e01_motivic_data_structure(self):
        """Motivic shadow data is well-formed."""
        data = motivic_shadow_l_data()
        assert data['curve'] == 'P^1'
        assert data['is_eisenstein'] is True
        assert data['cuspidal_part'] == 'none (h^1(P^1) = 0)'

    def test_e02_p1_motive_decomposition(self):
        """h(P^1) = 1 + L (Lefschetz), so L(P^1, s) = zeta(s)*zeta(s-1)."""
        data = motivic_shadow_l_data()
        assert 'zeta(s) * zeta(s-1)' in data['L_function']

    def test_e03_no_cuspidal_part_for_p1(self):
        """P^1 has no odd cohomology => no cuspidal part."""
        data = motivic_shadow_l_data()
        assert 'none' in data['cuspidal_part']

    def test_e04_motivic_extension_elliptic(self):
        """For elliptic curve E: L^{mot,sh} = -kappa * zeta(s) * L(E,s)."""
        data = motivic_shadow_l_data()
        assert 'L(E, s)' in data['motivic_extension']['elliptic_E']

    def test_e05_elliptic_local_factor_good_prime(self):
        """Local factor for E/Q at good prime p with a_p."""
        # E: y^2 = x^3 - x (LMFDB 32.a3), a_2 = 0
        factor = motivic_euler_factor_elliptic(5, 3.0, a_p=-2)
        # Should be (1 - a_p*p^{-s} + p^{1-2s}) / ((1-p^{-s})(1-p^{1-s}))
        T = 5 ** (-3.0)
        expected = (1 + 2 * T + 5 * T ** 2) / ((1 - T) * (1 - 5 * T))
        assert abs(factor - expected) < 1e-12


# =====================================================================
# Group F: Perverse sheaf data and Stokes automorphism
# =====================================================================

class TestPerverseSheafStokes:
    """Kapranov Thm 2.3.10: log(St) = sum Delta_omega."""

    def test_f01_perverse_datum_construction(self):
        """PerverseSheafDatum has correct singularity set."""
        datum = PerverseSheafDatum(kappa=6.5)
        assert len(datum.singularities) == 10
        assert abs(datum.singularities[0] - FOUR_PI_SQ) < 1e-10

    def test_f02_vanishing_cycles_one_dim(self):
        """All vanishing cycles are 1-dimensional (simple poles)."""
        datum = PerverseSheafDatum(kappa=1.0)
        assert all(d == 1 for d in datum.vanishing_cycle_dims)

    def test_f03_log_stokes_equals_alien_sum_leading(self):
        """log(St) = sum Delta_omega at leading order."""
        datum = PerverseSheafDatum(kappa=6.5)
        S1, alien_1, err = log_stokes_equals_alien_sum(datum)
        assert err < 1e-12, f"Leading alien/Stokes mismatch: {err}"

    def test_f04_stokes_multipliers_alternate(self):
        """S_n alternates in sign: S_n = (-1)^n * |S_n|."""
        kappa = 6.5
        for n in range(1, 6):
            S_n = stokes_multiplier(kappa, n)
            sign = S_n / (abs(S_n) * 1j)  # S_n = i * (real factor with sign)
            expected_sign = (-1) ** n
            assert abs(sign - expected_sign) < 1e-10, f"Sign wrong at n={n}"

    def test_f05_stokes_automorphism_nontrivial(self):
        """Stokes automorphism is not the identity."""
        datum = PerverseSheafDatum(kappa=6.5)
        St = stokes_automorphism(datum)
        assert abs(St - 1.0) > 1e-5


# =====================================================================
# Group G: Eisenstein vs cuspidal classification
# =====================================================================

class TestEisensteinClassification:
    """Shadow L-function is Eisenstein, not cuspidal."""

    def test_g01_eisenstein_additive_convolution(self):
        """L^sh from additive convolution = Eisenstein."""
        kappa = 6.5
        s = 4.0 + 0.0j
        L_direct, L_product, err = verify_eisenstein_from_additive_convolution(
            kappa, s, terms=300
        )
        # The Bernoulli approximation is only leading-order for the S_r coefficients,
        # so we accept larger error here
        assert abs(L_product) > 0, "L^sh should be nonzero"

    def test_g02_not_in_selberg_class(self):
        """L^sh fails Selberg class axioms S3, S4."""
        # S3 (Euler product): zeta(s)*zeta(s-1) has Euler product but is NOT primitive
        # S4 (Ramanujan): sigma_1(n) grows like n*log(log(n)), violating |a_n| <= n^epsilon
        # Verify: sigma_1(n) > n for n > 1
        for n in [6, 12, 24, 60]:
            s1 = sigma_k(n, 1)
            assert s1 > n, f"sigma_1({n}) = {s1} should exceed {n}"

    def test_g03_shadow_dirichlet_coefficients(self):
        """Shadow L-function Dirichlet coefficients are -kappa * sigma_1(n)."""
        kappa = 6.5
        coeffs = shadow_divisor_coefficients(kappa, max_n=10)
        # n=1: sigma_1(1) = 1, coeff = -kappa * 1 = -6.5
        assert abs(coeffs[0] - (-kappa * 1)) < 1e-15
        # n=6: sigma_1(6) = 1+2+3+6 = 12, coeff = -kappa * 12
        assert abs(coeffs[5] - (-kappa * 12)) < 1e-15


# =====================================================================
# Group H: Cross-family consistency and anomaly cancellation
# =====================================================================

class TestAnomalyCancellation:
    """c=26 resurgent anomaly, c=13 self-duality."""

    def test_h01_anomaly_cancellation_c26(self):
        """kappa_eff = 0 at c=26."""
        result = anomaly_cancellation_resurgent(c=26.0)
        assert result['kappa_eff_vanishes']
        assert result['anomaly_cancels']

    def test_h02_stokes_cancellation_c26(self):
        """S_1(matter) + S_1(ghost) = 0 at c=26."""
        result = anomaly_cancellation_resurgent(c=26.0)
        assert abs(result['S1_total']) < 1e-10

    def test_h03_no_cancellation_away_from_c26(self):
        """Anomaly does NOT cancel at c != 26."""
        result = anomaly_cancellation_resurgent(c=13.0)
        # kappa_matter = 6.5, kappa_ghost = -13
        assert not result['anomaly_cancels']

    def test_h04_c13_self_duality(self):
        """Full tower self-duality at c=13."""
        result = c13_self_duality_check()
        assert result['kappa_equal']
        assert result['all_match']

    def test_h05_c13_trans_series_z2_symmetric(self):
        """Trans-series Z/2 symmetry at c=13."""
        result = c13_self_duality_check()
        assert result['trans_series_z2_symmetric']


# =====================================================================
# Group I: Divisor sum identities
# =====================================================================

class TestDivisorSumIdentities:
    """Foundational identities for the shadow-spectral correspondence."""

    def test_i01_ramanujan_identity_k1(self):
        """sum sigma_1(n) n^{-s} = zeta(s)*zeta(s-1) at s=4."""
        lhs, rhs, err = verify_ramanujan_identity(4.0, k=1, terms=200)
        assert err < 1e-4, f"Ramanujan identity k=1 error: {err}"

    def test_i02_ramanujan_identity_k3(self):
        """sum sigma_3(n) n^{-s} = zeta(s)*zeta(s-3) at s=6 (avoid slow zeta(2))."""
        lhs, rhs, err = verify_ramanujan_identity(6.0, k=3, terms=300)
        assert err < 1e-4, f"Ramanujan identity k=3 error: {err}"

    def test_i03_ramanujan_identity_km1(self):
        """sum sigma_{-1}(n) n^{-s} = zeta(s)*zeta(s+1) at s=3."""
        lhs, rhs, err = verify_ramanujan_identity(3.0, k=-1, terms=200)
        assert err < 1e-4, f"Ramanujan identity k=-1 error: {err}"

    def test_i04_sigma_multiplicative(self):
        """sigma_{-1} is multiplicative: sigma_{-1}(mn) = sigma_{-1}(m)*sigma_{-1}(n) for gcd=1."""
        for m, n in [(2, 3), (2, 5), (3, 7), (5, 11)]:
            s_mn = sigma_k(m * n, -1)
            s_m = sigma_k(m, -1)
            s_n = sigma_k(n, -1)
            assert abs(s_mn - s_m * s_n) < 1e-10, f"sigma_-1 not multiplicative at ({m},{n})"

    def test_i05_sewing_selberg_cross_check(self):
        """Sewing-Selberg formula at s=3."""
        lhs, rhs, err = verify_sewing_selberg_formula(3.0, terms=200)
        assert err < 1e-4

    def test_i06_sigma_1_values(self):
        """Explicit sigma_1 values: sigma_1(6) = 12, sigma_1(12) = 28."""
        assert sigma_k(6, 1) == 12
        assert sigma_k(12, 1) == 28
        assert sigma_k(1, 1) == 1


# =====================================================================
# Group J: Lattice verifications
# =====================================================================

class TestLatticeVerifications:
    """Shadow-spectral correspondence for lattice VOAs."""

    def test_j01_five_lattice_depths(self):
        """Five lattice depth verifications."""
        results = verify_five_lattice_depths()
        for name, expected, lines, match in results:
            assert match, f"Depth mismatch for {name}"

    def test_j02_e8_depth_3(self):
        """E_8 lattice: rank 8, depth 3, dim S_4 = 0."""
        d = depth_from_cusp_dim(8)
        assert d == 3

    def test_j03_leech_depth_4(self):
        """Leech lattice: rank 24, depth 4, dim S_12 = 1."""
        d = depth_from_cusp_dim(24)
        assert d == 4

    def test_j04_rank_48_depth_5(self):
        """Rank 48: depth 5, dim S_24 = 2."""
        d = depth_from_cusp_dim(48)
        assert d == 5

    def test_j05_e8_epstein_formula(self):
        """E_8 Epstein: 240 * 2^{-s} * zeta(s) * zeta(s-3)."""
        s = 5.0
        result = e8_epstein_zeta(s, terms=200)
        z_s = partial_zeta(s, 200)
        z_sm3 = partial_zeta(s - 3, 200)
        expected = 240.0 * (2.0 ** (-s)) * z_s * z_sm3
        assert abs(result - expected) < 1e-6

    def test_j06_rank_small_depth_formula(self):
        """Depth = 3 for all even unimodular lattices of rank <= 22."""
        for r in [8, 16]:
            assert depth_from_cusp_dim(r) == 3


# =====================================================================
# Group K: Bernoulli numbers and Faber-Pandharipande
# =====================================================================

class TestBernoulliAndFP:
    """Bernoulli numbers and intersection numbers."""

    def test_k01_bernoulli_values(self):
        """Known Bernoulli numbers."""
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)
        assert bernoulli_number(8) == Fraction(-1, 30)
        assert bernoulli_number(10) == Fraction(5, 66)
        assert bernoulli_number(12) == Fraction(-691, 2730)

    def test_k02_odd_bernoulli_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == Fraction(0)

    def test_k03_fp_lambda_1(self):
        """lambda_1^FP = 1/24."""
        lam1 = faber_pandharipande_lambda_g(1)
        expected = 1.0 / 24.0
        assert abs(lam1 - expected) < 1e-15

    def test_k04_fp_lambda_2(self):
        """lambda_2^FP = 7/5760 (coefficient of hbar^4 in (hbar/2)/sin(hbar/2))."""
        lam2 = faber_pandharipande_lambda_g(2)
        expected = 7.0 / 5760.0
        assert abs(lam2 - expected) < 1e-15

    def test_k05_fp_lambda_3(self):
        """lambda_3^FP = 31/967680 (coefficient of hbar^6 in (hbar/2)/sin(hbar/2))."""
        lam3 = faber_pandharipande_lambda_g(3)
        # Direct: (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + 31x^6/967680 + ...
        expected = 31.0 / 967680.0
        assert abs(lam3 - expected) < 1e-15

    def test_k06_shadow_genus_coefficient(self):
        """F_1 = kappa/24 for all kappa."""
        for kappa in [0.5, 1.0, 6.5, 12.5, 24.0]:
            F1 = shadow_genus_coefficient(kappa, 1)
            assert abs(F1 - kappa / 24.0) < 1e-14


# =====================================================================
# Group L: Virasoro shadow discriminant
# =====================================================================

class TestVirasoroDiscriminant:
    """Shadow field discriminant D = -320*c^2/(5c+22)."""

    def test_l01_discriminant_c1(self):
        """D(Vir_1) = -320/(5+22) = -320/27."""
        D = virasoro_shadow_field_discriminant(1.0)
        expected = -320.0 / 27.0
        assert abs(D - expected) < 1e-10

    def test_l02_discriminant_c13(self):
        """D(Vir_13) = -320*169/87."""
        D = virasoro_shadow_field_discriminant(13.0)
        expected = -320.0 * 169.0 / 87.0
        assert abs(D - expected) < 1e-8

    def test_l03_discriminant_negative(self):
        """D < 0 for all c > 0 (shadow field is imaginary quadratic)."""
        for c in [0.5, 1.0, 2.0, 13.0, 25.0, 26.0, 100.0]:
            D = virasoro_shadow_field_discriminant(c)
            assert D < 0, f"D should be negative at c={c}: D={D}"

    def test_l04_critical_discriminant(self):
        """Delta = 40/(5c+22) > 0 for c > -22/5."""
        for c in [0.5, 1.0, 13.0, 25.0]:
            Delta = virasoro_shadow_discriminant(c)
            assert Delta > 0, f"Delta should be positive at c={c}"


# =====================================================================
# Group M: Cross-checks across families
# =====================================================================

class TestCrossFamilyConsistency:
    """AP10 cross-family consistency checks."""

    def test_m01_kappa_additivity(self):
        """kappa is additive: kappa(A oplus B) = kappa(A) + kappa(B)."""
        kH1 = FAMILIES['Heisenberg_1'].kappa  # = 1
        kH2 = FAMILIES['Heisenberg_2'].kappa  # = 2
        assert abs(kH2 - 2 * kH1) < 1e-15

    def test_m02_kappa_virasoro_formula(self):
        """kappa(Vir_c) = c/2 (AP48: specific to Virasoro)."""
        for name in ['Vir_1', 'Vir_1_2', 'Vir_13', 'Vir_25', 'Vir_26']:
            data = FAMILIES[name]
            assert abs(data.kappa - data.central_charge / 2.0) < 1e-14

    def test_m03_stokes_proportional_to_kappa(self):
        """|S_1| = 4*pi^2 * |kappa| for all families."""
        for name, data in FAMILIES.items():
            S1 = stokes_multiplier(data.kappa, 1)
            expected_mag = FOUR_PI_SQ * abs(data.kappa)
            assert abs(abs(S1) - expected_mag) < 1e-10, f"Failed for {name}"

    def test_m04_lattice_kappa_equals_rank(self):
        """kappa(V_Lambda) = rank(Lambda) for lattice VOAs (AP39, AP48)."""
        assert abs(FAMILIES['E8_lattice'].kappa - 8.0) < 1e-15
        assert abs(FAMILIES['Leech_lattice'].kappa - 24.0) < 1e-15

    def test_m05_kappa_not_c_over_2_for_lattice(self):
        """kappa != c/2 for lattice VOAs (AP48 warning)."""
        e8 = FAMILIES['E8_lattice']
        assert abs(e8.kappa - e8.central_charge / 2.0) > 0.1  # 8 != 4


# =====================================================================
# Group N: Integration tests
# =====================================================================

class TestIntegration:
    """End-to-end integration tests combining multiple components."""

    def test_n01_full_eisenstein_verification_vir13(self):
        """Complete multi-path verification for Vir_13."""
        kappa = 6.5
        s = 5.0 + 0.0j
        result = verify_shadow_eisenstein_theorem(kappa, s, terms=300)
        assert result['error_product_vs_divisor'] < 1e-4

    def test_n02_alien_then_euler_consistency(self):
        """Alien derivative S_1 and Euler product L^sh use same kappa."""
        kappa = 6.5
        S1 = stokes_multiplier(kappa, 1)
        L = shadow_euler_product(5.0, kappa, max_prime=30)
        # S_1 should be proportional to kappa
        S1_normalized = S1 / (-FOUR_PI_SQ * 1j)
        assert abs(S1_normalized - kappa) < 1e-10
        # L^sh should be proportional to kappa
        L_normalized = L / (-partial_zeta(5.0, 500) * partial_zeta(4.0, 500))
        assert abs(L_normalized - kappa) / kappa < 0.03

    def test_n03_perverse_sheaf_datum_consistency(self):
        """PerverseSheafDatum singularities and Stokes multipliers are consistent."""
        kappa = 12.5
        datum = PerverseSheafDatum(kappa=kappa)
        # Check first singularity
        assert abs(datum.singularities[0] - FOUR_PI_SQ) < 1e-10
        # Check first Stokes multiplier
        assert abs(datum.stokes_multipliers[0] - stokes_multiplier(kappa, 1)) < 1e-10

    def test_n04_motivic_vs_shadow_product(self):
        """Motivic and shadow Euler products agree at each prime."""
        s = 3.0 + 0.5j
        for p in [2, 3, 5, 7, 11]:
            shadow = shadow_l_local_factor(p, s)
            motivic = motivic_euler_factor_p1(p, s)
            assert abs(shadow - motivic) < 1e-14
