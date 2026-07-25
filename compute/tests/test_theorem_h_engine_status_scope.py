"""Status guards for the family-indexed Theorem-H engine."""

from __future__ import annotations

from compute.lib.chiral_hochschild_engine import (
    THEOREM_H_REQUIRED_COMPONENTS,
    affine_slN_data,
    compute_all_standard_families,
    derivation_analysis,
    verify_km_h1_equals_dim_g,
    verify_theorem_h_complete,
    verify_universal_polynomial,
    whitehead_lemma_check,
)
from compute.lib.chirhoch_dimension_engine import theorem_h_scope_record


class TestTheoremHEngineStatusScope:
    def test_default_family_rows_request_explicit_support_data(self):
        rows = compute_all_standard_families()
        assert rows
        for result in rows.values():
            assert result.support is None
            assert result.dimensions is None
            assert result.dim_H0 is None
            assert result.dim_H1 is None
            assert result.dim_H2 is None
            assert result.status == "open-family-support-datum"
            assert result.hypothesis_package == THEOREM_H_REQUIRED_COMPONENTS

    def test_affine_zero_modes_are_exact_inner_metadata(self):
        for n in (2, 3, 4, 5, 6, 10):
            data = affine_slN_data(n)
            analysis = derivation_analysis(data)
            expected = n * n - 1
            assert data.lie_dim == expected
            assert analysis.known_inner_zero_mode_dimension == expected
            assert analysis.exact_ope_constraints[
                "adjoint_zero_mode_dimension"
            ] == expected
            assert analysis.total_derivations is None
            assert analysis.inner_derivations is None
            assert analysis.outer_derivations is None
            assert analysis.dim_chirhoch1 is None
            assert analysis.status == "open-complete-chiral-derivation-quotient"

    def test_legacy_affine_report_withholds_chart_h1(self):
        report = verify_km_h1_equals_dim_g()
        assert report["all_passed"] is None
        for label, row in report["families"].items():
            assert row["dim_H1"] is None, label
            assert row["dim_g"] == row["known_inner_zero_mode_dimension"], label
            assert row["status"] == "open-complete-chiral-derivation-quotient"
        assert "known inner zero-mode subspace" in report["claim"]

    def test_whitehead_calculation_and_chiral_transport_are_typed_separately(self):
        report = whitehead_lemma_check("A", 1)
        assert report["dim_g"] == 3
        assert report["H1_g_g"] == 0
        assert report["H2_g_g"] == 0
        assert report["chiral_H1"] is None
        assert "chiral transport open" in report["status"]

    def test_theorem_h_report_is_an_open_obligation(self):
        report = verify_theorem_h_complete(affine_slN_data(2))
        assert report["passed"] is None
        assert report["support"] is None
        assert report["dimensions"] is None
        assert report["bounded_benchmark"] is None
        assert report["status"] == "open-family-support-datum"
        assert report["hypothesis_package"] == THEOREM_H_REQUIRED_COMPONENTS

    def test_universal_polynomial_is_replaced_by_family_models(self):
        report = verify_universal_polynomial()
        assert report["all_passed"] is None
        assert "family support models" in report["status"]
        for row in report["families"].values():
            assert row["polynomial"] is None
            assert row["status"] == "open-family-support-datum"

    def test_scope_record_names_the_complete_family_package(self):
        record = theorem_h_scope_record("virasoro", applies=True)
        assert record["claim"] == "H_H(A;S) implies Supp ChirHoch(A) subset S"
        assert record["applies"] is None
        assert record["status"] == "open-explicit-family-support-datum"
        assert record["legacy_applies_argument"] is True
        assert set(record["hypotheses"]) == {
            "complete_chart_complex_Q_A",
            "chart_quasi_isomorphism_gamma_A",
            "support_model_K_A_S",
            "strong_deformation_retract_i_p_h",
            "incidence_and_bar_face_compatibility",
            "averaging_and_Mittag_Leffler_comparison",
        }
