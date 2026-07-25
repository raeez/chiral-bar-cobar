"""Independent guards for the BP chiral-cohomology audit surface."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.bp_koszul_conductor_engine import (
    BP_GENERATORS as CANONICAL_GENERATORS,
    BP_KAPPA_STATUS,
    K_BP_EXACT,
    c_BP as canonical_c_bp,
)
from compute.lib.chirhoch_bershadsky_polyakov_engine import (
    BP_CHIRHOCH_HYPOTHESES,
    BP_CHIRHOCH_RESOLUTION_OBLIGATION,
    BP_GENERATORS,
    BPHochschildPolynomial,
    BPChirHochResult,
    BPChiralData,
    BPDeformationObstruction,
    BPDerivationAnalysis,
    UnverifiedBPChirHochError,
    all_deformations_unobstructed_bp,
    bp_central_charge,
    bp_central_conductor,
    bp_data,
    bp_dual_level,
    bp_primary_ope_normal_form,
    bp_reciprocal_weight_diagnostic,
    center_dimension_bp,
    center_dimension_koszul_dual_bp,
    comparison_with_principal,
    compute_bp_hochschild_polynomial,
    compute_chirhoch_bp,
    deformation_obstruction_analysis_bp,
    derivation_analysis_bp,
    feigin_semikhatov_constraints_on_chirhoch,
    koszul_duality_check_bp,
    n2_sca_constraints_on_chirhoch,
    special_level_analysis,
    verify_chirhoch_bp,
    verify_theorem_h_for_bp,
)


k = Symbol("k")
ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute" / "lib" / "chirhoch_bershadsky_polyakov_engine.py"


class TestPrimarySourceData:
    def test_standard_central_charge_formula(self):
        expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
        assert simplify(bp_central_charge() - expected) == 0

    @pytest.mark.parametrize("level", [0, 1, -1, 2, -4, Fraction(1, 2)])
    def test_independent_central_conductor_samples(self, level):
        level_q = Rational(level.numerator, level.denominator) if isinstance(level, Fraction) else Rational(level)
        dual = -level_q - 6
        direct = -((2 * level_q + 3) * (3 * level_q + 1)) / (level_q + 3)
        direct_dual = -((2 * dual + 3) * (3 * dual + 1)) / (dual + 3)
        assert simplify(direct + direct_dual) == 50
        assert simplify(bp_central_conductor(level_q)) == 50
        assert canonical_c_bp(Fraction(level)) == Fraction(direct)

    def test_canonical_engine_agrees_on_conductor(self):
        assert K_BP_EXACT == Fraction(50)
        assert simplify(bp_central_conductor() - K_BP_EXACT) == 0

    def test_level_involution_and_pole(self):
        assert simplify(bp_dual_level(bp_dual_level()) - k) == 0
        assert bp_dual_level(-3) == -3
        with pytest.raises(ZeroDivisionError, match="pole"):
            bp_central_charge(-3)

    def test_all_four_generators_are_even(self):
        assert set(BP_GENERATORS) == {"J", "G+", "G-", "T"}
        assert all(datum["parity"] == 0 for datum in BP_GENERATORS.values())
        assert all(parity == 0 for _weight, parity in CANONICAL_GENERATORS.values())

    def test_reciprocal_weight_diagnostic_is_17_over_6(self):
        independent = 1 + Rational(2, 3) + Rational(2, 3) + Rational(1, 2)
        assert independent == Rational(17, 6)
        assert bp_reciprocal_weight_diagnostic() == independent

    def test_bp_data_is_status_typed(self):
        data = bp_data(0)
        assert isinstance(data, BPChiralData)
        assert data.central_charge == -1
        assert data.anomaly_ratio is None
        assert data.kappa_status == BP_KAPPA_STATUS.status
        assert data.bosonic_generators == ["J", "G+", "G-", "T"]
        assert data.fermionic_generators == []
        assert data.weight_one_bosonic == ["J"]


class TestExactOPECandidateChecks:
    def test_normal_form_coefficients(self):
        normal = bp_primary_ope_normal_form()
        assert simplify(normal["J_level"] - (2 * k + 3) / 3) == 0
        assert normal["J_G_plus_charge"] == 1
        assert normal["J_G_minus_charge"] == -1
        assert simplify(normal["G_pairing"] - (k + 1) * (2 * k + 3)) == 0
        assert simplify(normal["GJ_coefficient"] - 3 * (k + 1)) == 0
        assert normal["JJ_coefficient"] == 3
        assert simplify(normal["dJ_coefficient"] - 3 * (k + 1) / 2) == 0
        assert simplify(normal["T_coefficient"] + k + 3) == 0

    def test_charge_rotation_is_inner_and_scaling_is_generically_obstructed(self):
        analysis = derivation_analysis_bp(0)
        assert isinstance(analysis, BPDerivationAnalysis)
        assert analysis.exact_candidate_tests["J_charge_rotation_is_inner"]
        assert analysis.exact_candidate_tests[
            "J_scaling_fails_when_2k_plus_3_invertible"
        ]
        assert analysis.inner_derivations == ["J_{(0)} (charge rotation)"]

    def test_zero_j_level_is_recorded_as_exceptional(self):
        analysis = derivation_analysis_bp(Rational(-3, 2))
        assert analysis.exact_candidate_tests[
            "J_scaling_fails_when_2k_plus_3_invertible"
        ] is False
        assert "exceptional_J_level_zero" in analysis.unresolved_candidates

    def test_complete_outer_derivation_dimension_is_withheld(self):
        analysis = derivation_analysis_bp()
        assert analysis.total_outer is None
        assert analysis.dim_chirhoch1 is None
        assert analysis.j_current_contribution is None
        assert analysis.fermionic_contribution is None
        assert "complete_even_derivation_system" in analysis.unresolved_candidates

    def test_fs_constraint_packet_reaches_no_fake_dimension(self):
        packet = feigin_semikhatov_constraints_on_chirhoch()
        assert packet["is_feigin_semikhatov_bp"] is True
        assert packet["is_n2_sca"] is False
        assert packet["all_generators_even"] is True
        assert packet["charge_rotation_is_inner"] is True
        assert packet["actual_outer_derivations"] is None
        assert packet["status"] == "open-complete-linearized-Borcherds-system"
        assert n2_sca_constraints_on_chirhoch() == packet


class TestFailLoudCohomologyAPI:
    @pytest.mark.parametrize(
        "function",
        [center_dimension_bp, center_dimension_koszul_dual_bp],
    )
    def test_unproved_dimensions_raise(self, function):
        with pytest.raises(UnverifiedBPChirHochError, match="chiral cochain"):
            function()

    def test_polynomial_packet_contains_no_fabricated_coefficients(self):
        polynomial = compute_bp_hochschild_polynomial()
        assert isinstance(polynomial, BPHochschildPolynomial)
        assert polynomial.coefficients == [None, None, None]
        assert polynomial.total_dimension is None
        assert polynomial.euler_characteristic is None
        assert polynomial.is_palindromic is None
        assert polynomial.status == "open-chiral-cochain-computation"
        with pytest.raises(UnverifiedBPChirHochError, match="P_BP"):
            polynomial.evaluate(1)

    def test_product_family_and_h2_class_are_separated(self):
        lanes = deformation_obstruction_analysis_bp()
        assert all(isinstance(lane, BPDeformationObstruction) for lane in lanes)
        family = next(lane for lane in lanes if lane.lane_name == "level_motion")
        h2 = next(lane for lane in lanes if lane.lane_name == "chiral_H2_class")
        assert family.is_unobstructed is True
        assert family.cohomological_degree is None
        assert h2.is_unobstructed is None
        assert h2.cohomological_degree == 2
        assert all_deformations_unobstructed_bp() is None

    def test_same_family_duality_is_conditional(self):
        packet = koszul_duality_check_bp()
        assert packet["partition_self_transpose"] is True
        assert packet["involution_check"] is True
        assert packet["same_family_duality_status"] == "conditional-H_BP_DS_bar"
        assert packet["K_c"] == 50
        assert packet["K_kappa"] is None
        assert packet["betti_A"] is None
        assert packet["all_checks_pass"] is None

    def test_principal_and_bp_support_require_separate_maps(self):
        packet = comparison_with_principal()
        assert packet["virasoro_bounded_support"] == (0, 2, 3)
        assert packet["virasoro_bounded_dimensions"] == {0: 1, 2: 1, 3: 1}
        assert packet["principal_w3_support"] is None
        assert packet["principal_w3_dimensions"] is None
        assert packet["bp_polynomial"] is None
        assert packet["bp_total"] is None
        assert packet["transfer_available"] is False


class TestMasterStatusPacket:
    def test_special_levels_use_standard_fkr_values(self):
        packet = special_level_analysis()
        assert packet["critical_level"] == -3
        assert packet["level_0"]["c"] == -1
        assert packet["level_1"]["c"] == -5
        assert packet["level_0"]["kappa"] is None
        assert packet["generic_result"]["H0"] is None

    def test_master_result_withholds_every_betti_number(self):
        result = compute_chirhoch_bp()
        assert isinstance(result, BPChirHochResult)
        assert result.dim_H0 is None
        assert result.dim_H1 is None
        assert result.dim_H2 is None
        assert result.betti_numbers is None
        assert result.total_dimension is None
        assert result.concentrated_in_0_1_2 is None
        assert result.all_unobstructed is None
        assert result.hypothesis_package == BP_CHIRHOCH_HYPOTHESES
        assert result.resolution_obligation == BP_CHIRHOCH_RESOLUTION_OBLIGATION

    def test_theorem_h_report_is_open(self):
        report = verify_theorem_h_for_bp()
        assert report["is_chirally_koszul"] is None
        assert report["concentrated_in_0_1_2"] is None
        assert report["theorem_h_satisfied"] is None
        assert report["betti_numbers"] is None
        assert report["status"] == "open-family-specific-Theorem-H-comparison"
        assert "bounded-to-chart" in report["resolution_obligation"]

    def test_exact_verification_suite_passes(self):
        checks = verify_chirhoch_bp()
        assert checks
        assert all(checks.values()), checks


class TestRegressionFirewalls:
    def test_engine_contains_no_old_numeric_promotions(self):
        source = ENGINE.read_text(encoding="utf-8")
        for stale in (
            "Koszul conductor K_BP = c(k) + c(-k-6) = 196",
            "Anomaly ratio rho = 1/6",
            "dim ChirHoch^1(BP_k) " + "= 0",
            "theorem_h_satisfied\": True",
            "fermionic_contribution=0",
        ):
            assert stale not in source

    def test_status_packet_names_every_load_bearing_obligation(self):
        result = compute_chirhoch_bp()
        for hypothesis in (
            "complete_generator_compatible_derivation_complex_computed",
            "same_family_bar_duality_comparison_q_BP_proved",
            "bounded_vertex_to_chiral_chart_quasi_isomorphism",
            "strong_deformation_retract_with_Mittag_Leffler_control",
        ):
            assert hypothesis in result.hypothesis_package
