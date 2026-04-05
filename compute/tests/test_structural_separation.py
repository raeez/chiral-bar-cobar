r"""
Tests for structural_separation.py — thm:structural-separation analysis.

Verifies:
1. Unfolding erasure mechanism (poles of Mellin transform disjoint from scattering)
2. Pluriharmonic obstruction (arithmetic component invisible to WP)
3. Bootstrap system dimension analysis
4. Three-step programme status
5. Genus-2 escape route analysis
6. Algebra-representation gap classification
7. Moment-determines-poles falsification
8. Full structural separation assessment
"""

import pytest
from compute.lib.structural_separation import (
    mellin_transform_poles,
    real_axis_constraint_analysis,
    kahler_arithmetic_blindness,
    bootstrap_constraint_system,
    three_step_programme_analysis,
    genus2_sewing_nondiagonality,
    genus2_escape_analysis,
    genus2_rs_integral_poles,
    algebra_representation_gap,
    heisenberg_scattering_coupling,
    moment_determines_poles_test,
    structural_separation_full_analysis,
)


# ============================================================
# T1-T8: Unfolding Erasure Mechanism
# ============================================================

class TestUnfoldingErasure:
    """Tests for thm:structural-separation part (ii): unfolding erases scattering."""

    def test_T1_scattering_poles_erased(self):
        """T1: All scattering poles are erased by RS unfolding."""
        result = mellin_transform_poles(c=26.0)
        assert result['scattering_poles_erased'] is True

    def test_T2_pole_locations_disjoint(self):
        """T2: Mellin poles and scattering poles are disjoint sets."""
        result = mellin_transform_poles(c=26.0)
        assert result['pole_locations_disjoint'] is True

    def test_T3_mellin_poles_from_maass(self):
        """T3: Mellin poles come from Maass spectrum, not zeta zeros."""
        result = mellin_transform_poles(c=26.0)
        for pole in result['poles_from_a0']:
            # Real parts of Mellin poles: 1.0 (constant term),
            # 0.0 (functional equation), 0.5 (Maass eigenvalues)
            rp = pole['real_part']
            assert rp in [0.0, 0.5, 1.0], f"Unexpected pole real part: {rp}"

    def test_T4_scattering_poles_at_rho_half(self):
        """T4: Scattering poles are at s = (1+ρ)/2 for zeta zeros ρ."""
        result = mellin_transform_poles(c=26.0)
        for sp in result['scattering_poles']:
            rho = sp['zeta_zero']
            expected_pole = (1 + rho) / 2
            assert abs(sp['scattering_pole'] - expected_pole) < 1e-10

    def test_T5_scattering_poles_real_part(self):
        """T5: Assuming RH, scattering poles have Re(s) = 3/4."""
        result = mellin_transform_poles(c=26.0)
        for sp in result['scattering_poles']:
            # Under RH: ρ = 1/2 + iγ → s = (1+ρ)/2 = 3/4 + iγ/2
            assert abs(sp['real_part'] - 0.75) < 1e-10

    def test_T6_mellin_poles_not_at_three_quarters(self):
        """T6: Mellin poles have Re(s) ≠ 3/4 (disjoint from scattering)."""
        result = mellin_transform_poles(c=26.0)
        for pole in result['poles_from_a0']:
            rp = pole['real_part']
            assert abs(rp - 0.75) > 0.1, f"Mellin pole at Re(s) = {rp} ≈ 3/4"

    def test_T7_different_central_charges(self):
        """T7: Erasure holds for multiple central charges."""
        for c in [1.0, 2.0, 12.0, 13.0, 26.0]:
            result = mellin_transform_poles(c=c)
            assert result['scattering_poles_erased'] is True

    def test_T8_mechanism_explanation(self):
        """T8: The mechanism is Mellin replacement (not cancellation)."""
        result = mellin_transform_poles(c=26.0)
        assert 'Mellin' in result['mechanism']
        assert 'a_0' in result['mechanism']


# ============================================================
# T9-T12: Real Axis Constraint Analysis
# ============================================================

class TestRealAxisConstraints:
    """Tests for the real/complex dichotomy."""

    def test_T9_mc_constraints_real(self):
        """T9: MC constraints are real-valued for real c."""
        result = real_axis_constraint_analysis(c=26.0)
        assert result['mc_constraints_real'] is True

    def test_T10_scattering_poles_complex(self):
        """T10: Scattering poles are complex."""
        result = real_axis_constraint_analysis(c=26.0)
        assert result['scattering_poles_complex'] is True

    def test_T11_finite_vs_infinite(self):
        """T11: Finite real constraints vs infinite complex parameters."""
        result = real_axis_constraint_analysis(c=26.0)
        analysis = result['finite_real_vs_infinite_complex']
        assert 'finite' in analysis['conclusion'].lower() or \
               'Finitely' in analysis['conclusion']

    def test_T12_virasoro_shadow_coefficients(self):
        """T12: Virasoro shadow coefficients are determined by c alone."""
        result = real_axis_constraint_analysis(c=26.0)
        assert result['kappa'] == 13.0  # κ = c/2 = 26/2 = 13
        S = result['shadow_coeffs']
        assert S[0] == 13.0  # S_2 = κ
        assert S[1] == 0.0   # S_3 = 0 for Virasoro


# ============================================================
# T13-T16: Pluriharmonic Obstruction
# ============================================================

class TestPluriharmonicObstruction:
    """Tests for thm:structural-separation part (iii)."""

    def test_T13_arithmetic_component_pluriharmonic(self):
        """T13: 2 log|η(τ)|² is pluriharmonic."""
        result = kahler_arithmetic_blindness()
        assert result['arithmetic_component']['ddbar'] == '0 (pluriharmonic)'

    def test_T14_geometric_component_generates_wp(self):
        """T14: log(4π² y) generates the WP Kahler form."""
        result = kahler_arithmetic_blindness()
        assert result['geometric_component']['generates_wp'] is True

    def test_T15_arithmetic_wp_invisible(self):
        """T15: Arithmetic content invisible to WP metric."""
        result = kahler_arithmetic_blindness()
        assert result['arithmetic_component']['wp_invisible'] is True

    def test_T16_reason_is_holomorphicity(self):
        """T16: The reason is holomorphicity of log η."""
        result = kahler_arithmetic_blindness()
        assert 'holomorphic' in result['arithmetic_component']['reason']


# ============================================================
# T17-T22: Bootstrap System Analysis
# ============================================================

class TestBootstrapSystem:
    """Tests for the bootstrap across central charges."""

    def test_T17_constraint_count(self):
        """T17: Constraint count = n_charges * (max_arity - 1)."""
        charges = [1.0, 2.0, 13.0, 26.0]
        result = bootstrap_constraint_system(charges, max_arity=6)
        assert result['total_constraints'] == 4 * 5  # 4 charges * 5 arities

    def test_T18_kappa_values(self):
        """T18: κ = c/2 for each central charge."""
        charges = [2.0, 12.0, 26.0]
        result = bootstrap_constraint_system(charges)
        for datum in result['bootstrap_data']:
            assert abs(datum['kappa'] - datum['c'] / 2) < 1e-10

    def test_T19_status_open(self):
        """T19: Bootstrap programme status is OPEN."""
        charges = [1.0, 2.0, 13.0, 26.0]
        result = bootstrap_constraint_system(charges)
        assert 'OPEN' in result['status']

    def test_T20_fundamental_obstruction_identified(self):
        """T20: The fundamental obstruction is identified."""
        charges = [1.0, 2.0]
        result = bootstrap_constraint_system(charges)
        assert 'obstruction' in result['fundamental_obstruction'].lower() or \
               'NOT overcome' in result['fundamental_obstruction']

    def test_T21_virasoro_q_contact(self):
        """T21: Q^contact(Vir) = 10/[c(5c+22)] for c in bootstrap."""
        charges = [2.0, 12.0, 26.0]
        result = bootstrap_constraint_system(charges, max_arity=6)
        for datum in result['bootstrap_data']:
            c = datum['c']
            expected_q = 10.0 / (c * (5 * c + 22))
            assert abs(datum['Q_contact'] - expected_q) < 1e-12

    def test_T22_single_charge_no_bootstrap(self):
        """T22: Single central charge gives no bootstrap advantage."""
        result = bootstrap_constraint_system([26.0], max_arity=6)
        assert result['n_charges'] == 1
        # No cross-charge information
        assert result['total_constraints'] == 5


# ============================================================
# T23-T28: Three-Step Programme
# ============================================================

class TestThreeStepProgramme:
    """Tests for the three open steps."""

    def test_T23_all_steps_open(self):
        """T23: All three steps are OPEN."""
        result = three_step_programme_analysis()
        assert result['step_1']['status'] == 'OPEN'
        assert result['step_2']['status'] == 'OPEN'
        assert result['step_3']['status'] == 'OPEN'

    def test_T24_step1_has_falsification_test(self):
        """T24: Step 1 has a falsification test."""
        result = three_step_programme_analysis()
        assert 'falsification_test' in result['step_1']
        assert len(result['step_1']['falsification_test']) > 0

    def test_T25_step2_has_falsification_test(self):
        """T25: Step 2 has a falsification test."""
        result = three_step_programme_analysis()
        assert 'falsification_test' in result['step_2']
        assert len(result['step_2']['falsification_test']) > 0

    def test_T26_step3_has_falsification_test(self):
        """T26: Step 3 has a falsification test."""
        result = three_step_programme_analysis()
        assert 'falsification_test' in result['step_3']
        assert len(result['step_3']['falsification_test']) > 0

    def test_T27_overall_assessment_identifies_gap(self):
        """T27: Overall assessment identifies the algebra-representation gap."""
        result = three_step_programme_analysis()
        assert 'algebra' in result['overall_assessment'].lower()
        assert 'representation' in result['overall_assessment'].lower()

    def test_T28_step2_heisenberg_falsification(self):
        """T28: Heisenberg falsification shows MC carries no ρ-info."""
        result = three_step_programme_analysis()
        assert 'Heisenberg' in result['step_2']['falsification_test']
        assert 'MC constraint' in result['step_2']['falsification_test']


# ============================================================
# T29-T38: Genus-2 Escape Route
# ============================================================

class TestGenus2Escape:
    """Tests for the genus-2 escape mechanism."""

    def test_T29_genus1_sewing_diagonal(self):
        """T29: Genus-1 sewing is Fock-diagonal."""
        result = genus2_sewing_nondiagonality()
        assert result['genus_1']['sewing_diagonal'] is True

    def test_T30_genus2_sewing_not_diagonal(self):
        """T30: Genus-2 sewing is NOT Fock-diagonal."""
        result = genus2_sewing_nondiagonality()
        assert result['genus_2']['sewing_diagonal'] is False

    def test_T31_genus1_hecke_collapse(self):
        """T31: Genus-1 has sewing-Hecke collapse."""
        result = genus2_sewing_nondiagonality()
        assert result['genus_1']['hecke_collapse'] is True

    def test_T32_genus2_no_hecke_collapse(self):
        """T32: Genus-2 does NOT have sewing-Hecke collapse."""
        result = genus2_sewing_nondiagonality()
        assert result['genus_2']['hecke_collapse'] is False

    def test_T33_three_consequences(self):
        """T33: Three consequences of genus-2 non-diagonality."""
        result = genus2_sewing_nondiagonality()
        assert len(result['three_consequences']) == 3

    def test_T34_bocherer_bridge_provides_escape(self):
        """T34: Bocherer bridge provides critical-line access."""
        result = genus2_escape_analysis()
        assert result['bocherer_bridge']['critical_line_access'] is True

    def test_T35_bocherer_bridge_proved(self):
        """T35: Bocherer bridge is proved (DPSS20)."""
        result = genus2_escape_analysis()
        assert result['bocherer_bridge']['proved'] is True
        assert 'DPSS20' in result['bocherer_bridge']['references']

    def test_T36_access_not_control(self):
        """T36: Access ≠ control (remaining gap)."""
        result = genus2_escape_analysis()
        gap = result['remaining_gap']
        # The remaining gap: MC determines L-values but not positivity/non-vanishing
        assert 'does not' in gap or 'Gap A' in gap

    def test_T37_leech_test_passed(self):
        """T37: Leech lattice test: chi12 projection nonzero."""
        result = genus2_escape_analysis()
        assert result['leech_lattice_test']['chi12_projection_nonzero'] is True
        assert abs(result['leech_lattice_test']['c2_approx'] - (-1.918e-6)) < 1e-7

    def test_T38_escalation_principle(self):
        """T38: Escalation to all genera via symmetric powers."""
        result = genus2_escape_analysis()
        assert 'Sym' in result['escalation_principle']
        assert 'Newton-Thorne' in result['escalation_principle']


# ============================================================
# T39-T44: Genus-2 RS Integral Poles
# ============================================================

class TestGenus2RSPoles:
    """Tests for genus-2 Rankin-Selberg integral pole analysis."""

    def test_T39_genus1_erased(self):
        """T39: Genus-1 RS poles are erased by unfolding."""
        result = genus2_rs_integral_poles()
        assert result['genus_1_poles']['erased_by_unfolding'] is True

    def test_T40_genus2_erasure_unknown(self):
        """T40: Genus-2 RS pole erasure is UNKNOWN."""
        result = genus2_rs_integral_poles()
        assert result['genus_2_poles']['erased_by_unfolding'] == 'UNKNOWN'

    def test_T41_genus2_more_scattering_factors(self):
        """T41: Genus-2 has more zeta factors in scattering matrix."""
        result = genus2_rs_integral_poles()
        assert len(result['genus_2_poles']['scattering_factors']) == 4
        assert len(result['genus_2_poles']['poles_from_zeta']) == 4

    def test_T42_bocherer_bypasses_unfolding(self):
        """T42: Bocherer bridge bypasses the unfolding question."""
        result = genus2_rs_integral_poles()
        assert result['bocherer_bypass']['avoids_unfolding_question'] is True

    def test_T43_obstruction_not_absolute(self):
        """T43: The obstruction is NOT absolute (genus 2 provides escape)."""
        result = genus2_rs_integral_poles()
        assert result['is_obstruction_absolute'] is False

    def test_T44_escape_via_bocherer(self):
        """T44: Escape is via Bocherer bridge, not RS unfolding."""
        result = genus2_rs_integral_poles()
        assert result['genus_2_provides_escape'] is True
        assert result['escape_mechanism'] == 'Bocherer bridge, not RS unfolding'


# ============================================================
# T45-T50: Algebra-Representation Gap
# ============================================================

class TestAlgebraRepGap:
    """Tests for the algebra-representation gap classification."""

    def test_T45_minimal_model_gap_closed(self):
        """T45: Minimal model (c < 1) gap is closed."""
        result = algebra_representation_gap(c=0.5)
        assert result['gap_status'] == 'CLOSED'

    def test_T46_generic_virasoro_gap_open(self):
        """T46: Generic Virasoro (c > 1) gap is OPEN."""
        result = algebra_representation_gap(c=26.0)
        assert result['gap_status'] == 'OPEN'

    def test_T47_c_equals_1_conditional(self):
        """T47: c = 1 gap is CONDITIONAL (depends on radius)."""
        result = algebra_representation_gap(c=1.0)
        assert result['gap_status'] == 'CONDITIONAL'

    def test_T48_gap_is_representation_functor(self):
        """T48: The gap is the representation functor A ↦ A-mod."""
        result = algebra_representation_gap(c=26.0)
        assert result['gap_is_representation_functor'] is True

    def test_T49_algebraic_data_listed(self):
        """T49: Algebraic data includes OPE, c, weights, shadow tower, MC."""
        result = algebra_representation_gap(c=26.0)
        data = result['algebraic_data']
        assert any('OPE' in d for d in data)
        assert any('shadow' in d.lower() for d in data)
        assert any('MC' in d or 'Θ' in d for d in data)

    def test_T50_representation_data_listed(self):
        """T50: Representation data includes primary spectrum, fusion, S-matrix."""
        result = algebra_representation_gap(c=26.0)
        data = result['representation_data']
        assert any('primary' in d.lower() for d in data)
        assert any('fusion' in d.lower() for d in data)


# ============================================================
# T51-T55: Heisenberg Falsification
# ============================================================

class TestHeisenbergFalsification:
    """Tests for the Heisenberg scattering coupling falsification."""

    def test_T51_mc_constraint_satisfied(self):
        """T51: MC constraint trivially satisfied for Heisenberg."""
        rho = complex(0.5, 14.1347)
        result = heisenberg_scattering_coupling(k=1.0, rho=rho)
        assert result['mc_constraint_satisfied'] is True

    def test_T52_no_rho_location_info(self):
        """T52: Coupling carries NO ρ-location information."""
        rho = complex(0.5, 14.1347)
        result = heisenberg_scattering_coupling(k=1.0, rho=rho)
        assert result['carries_rho_location_info'] is False

    def test_T53_works_for_off_line_rho(self):
        """T53: Coupling well-defined for off-line ρ (σ ≠ 1/2)."""
        rho_off = complex(0.6, 14.1347)  # Off the critical line
        result = heisenberg_scattering_coupling(k=1.0, rho=rho_off)
        assert result['mc_constraint_satisfied'] is True
        # The MC constraint is satisfied for ANY ρ, confirming it
        # carries no information about ρ's real part.

    def test_T54_different_levels(self):
        """T54: Same result for different Heisenberg levels."""
        rho = complex(0.5, 14.1347)
        for k in [1.0, 2.0, 12.0, 24.0]:
            result = heisenberg_scattering_coupling(k=k, rho=rho)
            assert result['mc_constraint_satisfied'] is True
            assert result['carries_rho_location_info'] is False

    def test_T55_explanation_mentions_class_g(self):
        """T55: Explanation mentions class G (shadow depth 2)."""
        rho = complex(0.5, 14.1347)
        result = heisenberg_scattering_coupling(k=1.0, rho=rho)
        assert 'class G' in result['explanation']


# ============================================================
# T56-T60: Moment-Determines-Poles Falsification
# ============================================================

class TestMomentDeterminesPoles:
    """Tests for the moment → poles analysis."""

    def test_T56_finite_moments_insufficient(self):
        """T56: Finite moments do NOT determine poles."""
        result = moment_determines_poles_test(max_moment=20)
        assert result['finite_moments_determine_poles'] is False

    def test_T57_all_moments_determine_right_half(self):
        """T57: All moments determine continuation on Re(s) > 1."""
        result = moment_determines_poles_test()
        assert result['all_moments_determine_continuation_right_half'] is True

    def test_T58_right_half_not_critical_strip(self):
        """T58: Right half-plane does NOT determine critical strip poles."""
        result = moment_determines_poles_test()
        assert result['continuation_right_half_determines_critical_strip_poles'] is False

    def test_T59_functional_equation_would_help(self):
        """T59: A functional equation WOULD help bridge the gap."""
        result = moment_determines_poles_test()
        assert result['functional_equation_would_help'] is True

    def test_T60_mc_no_functional_equation(self):
        """T60: MC equation does NOT supply a functional equation."""
        result = moment_determines_poles_test()
        assert result['mc_supplies_functional_equation'] is False


# ============================================================
# T61-T70: Full Structural Separation Assessment
# ============================================================

class TestFullAssessment:
    """Comprehensive tests for the structural separation analysis."""

    def test_T61_theorem_has_three_parts(self):
        """T61: Theorem has parts (i), (ii), (iii)."""
        result = structural_separation_full_analysis()
        parts = result['theorem_statement']['parts']
        assert 'i' in parts and 'ii' in parts and 'iii' in parts

    def test_T62_obstruction_is_unfolding(self):
        """T62: Main mechanism is Rankin-Selberg unfolding."""
        result = structural_separation_full_analysis()
        assert 'unfolding' in result['precise_obstruction']['mechanism'].lower()

    def test_T63_genus2_escape_exists(self):
        """T63: Genus-2 escape route exists."""
        result = structural_separation_full_analysis()
        assert result['genus_2_escape']['exists'] is True

    def test_T64_genus2_mechanism_is_bocherer(self):
        """T64: Genus-2 escape mechanism is Bocherer bridge."""
        result = structural_separation_full_analysis()
        assert 'Bocherer' in result['genus_2_escape']['mechanism']

    def test_T65_obstruction_absolute_at_genus1(self):
        """T65: Obstruction IS absolute at genus 1."""
        result = structural_separation_full_analysis()
        assert result['is_obstruction_absolute']['at_genus_1'] is True

    def test_T66_obstruction_not_absolute_at_genus2(self):
        """T66: Obstruction is NOT absolute at genus 2."""
        result = structural_separation_full_analysis()
        assert result['is_obstruction_absolute']['at_genus_2'] is False

    def test_T67_all_genera_unknown(self):
        """T67: Whether obstruction is absolute at all genera is UNKNOWN."""
        result = structural_separation_full_analysis()
        assert result['is_obstruction_absolute']['at_all_genera'] == 'UNKNOWN'

    def test_T68_three_steps_all_open(self):
        """T68: All three programme steps are OPEN."""
        result = structural_separation_full_analysis()
        for key in ['step_1', 'step_2', 'step_3']:
            assert 'OPEN' in result['three_step_programme'][key]

    def test_T69_leech_example_proved(self):
        """T69: Leech lattice is the proved example."""
        result = structural_separation_full_analysis()
        assert 'Leech' in result['genus_2_escape']['proved_example']

    def test_T70_access_not_control(self):
        """T70: Access ≠ control at genus 2."""
        result = structural_separation_full_analysis()
        gap = result['genus_2_escape']['remaining_gap']
        assert 'Access' in gap or 'access' in gap


# ============================================================
# T71-T75: Cross-Validation with Existing Modules
# ============================================================

class TestCrossValidation:
    """Cross-validation with existing arithmetic modules."""

    def test_T71_kappa_virasoro_consistency(self):
        """T71: κ(Vir_c) = c/2 consistent across analyses."""
        for c in [2.0, 13.0, 26.0]:
            result = real_axis_constraint_analysis(c)
            assert abs(result['kappa'] - c / 2) < 1e-10

    def test_T72_q_contact_virasoro(self):
        """T72: Q^contact(Vir) = 10/[c(5c+22)] for standard c values."""
        charges = [2.0, 6.0, 12.0, 26.0]
        result = bootstrap_constraint_system(charges, max_arity=6)
        for datum in result['bootstrap_data']:
            c = datum['c']
            expected = 10.0 / (c * (5 * c + 22))
            assert abs(datum['Q_contact'] - expected) < 1e-12

    def test_T73_self_dual_c13(self):
        """T73: Virasoro at c=13 is self-dual (κ = 13/2)."""
        result = real_axis_constraint_analysis(c=13.0)
        assert abs(result['kappa'] - 6.5) < 1e-10

    def test_T74_critical_string_c26(self):
        """T74: Critical string at c=26 has κ = 13."""
        result = real_axis_constraint_analysis(c=26.0)
        assert abs(result['kappa'] - 13.0) < 1e-10

    def test_T75_shadow_s3_vanishes_virasoro(self):
        """T75: S_3 = 0 for Virasoro (cubic shadow vanishes by parity)."""
        result = real_axis_constraint_analysis(c=26.0)
        assert result['shadow_coeffs'][1] == 0.0
