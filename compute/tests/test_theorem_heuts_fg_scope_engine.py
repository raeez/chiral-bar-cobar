r"""Semantic tests for the Heuts/Francis--Gaitsgory scope engine.

The oracle is the map signature.  Universal reconstruction
``Omega Bar(A) -> A`` belongs to Theorem A; quadratic recognition
``A^i -> Bar(A)`` belongs to Theorem B.  Heuts' completion theorem and
the Verdier comparison occupy two further, explicitly typed lanes.
"""

from itertools import combinations
from pathlib import Path

import pytest

from compute.lib.theorem_heuts_fg_scope_engine import (
    BL_SOURCE,
    DUAL_NUMBERS_PRESENTATION,
    FG_SOURCE,
    FREE_TENSOR_PRESENTATION,
    HEUTS_SOURCE,
    LV_QUADRATIC_SOURCE,
    ORDINARY_CHAIN_AMBIENT,
    RAN_CHIRAL_AMBIENT,
    TRUNCATED_CUBIC_PRESENTATION,
    bar_word_dimension,
    booth_lazarev_transfer_certificate,
    coalgebra_resolution_certificate,
    comparison_table,
    completed_support_certificate,
    conilpotence_index,
    heuts_completion_certificate,
    quadratic_comparison_certificate,
    reduced_deconcatenation_summands,
    universal_resolution_certificate,
    verdier_comparison_certificate,
    verify_scope_engine,
    worked_case_packet,
)


ENGINE = Path("compute/lib/theorem_heuts_fg_scope_engine.py")


class TestSourceAnchors:
    def test_fg_anchor_is_exact(self):
        assert "Proposition 4.1.2" in FG_SOURCE
        assert "Theorem 5.1.1" in FG_SOURCE
        assert "1103.5803" in FG_SOURCE

    def test_heuts_anchor_is_exact(self):
        assert "Theorem 2.1" in HEUTS_SOURCE
        assert "2408.06173" in HEUTS_SOURCE

    def test_quadratic_anchor_is_exact(self):
        assert "Theorems 2.3.2 and 3.4.6" in LV_QUADRATIC_SOURCE

    def test_booth_lazarev_anchor_names_global_result(self):
        assert "Global Koszul duality" in BL_SOURCE
        assert "2304.08409" in BL_SOURCE

    def test_fabricated_fg_theorem_number_is_absent(self):
        source = ENGINE.read_text()
        assert "Theorem 7.2.1" not in source
        assert "Thm 7.2.1" not in source


class TestAmbientHypotheses:
    def test_ran_chiral_ambient_carries_fg_package(self):
        assert RAN_CHIRAL_AMBIENT.heuts_ready is True
        assert RAN_CHIRAL_AMBIENT.fg_ready is True

    def test_ordinary_chains_carry_heuts_package(self):
        assert ORDINARY_CHAIN_AMBIENT.heuts_ready is True
        assert ORDINARY_CHAIN_AMBIENT.fg_ready is False

    def test_fg_application_records_open_pronilpotence(self):
        certificate = universal_resolution_certificate(ORDINARY_CHAIN_AMBIENT)
        assert certificate.status == "hypothesis-open"
        assert "pro-nilpotence" in certificate.conclusion


class TestUniversalResolution:
    def test_algebra_map_has_theorem_a_signature(self):
        certificate = universal_resolution_certificate()
        assert certificate.theorem.startswith("Theorem A")
        assert certificate.typed_map == "epsilon_A: Omega_X Bar_X(A) -> A"
        assert certificate.status == "proved-by-FG"
        assert "every augmented associative algebra" in certificate.conclusion

    def test_coalgebra_map_has_companion_signature(self):
        certificate = coalgebra_resolution_certificate()
        assert certificate.theorem.startswith("Theorem A")
        assert certificate.typed_map == "eta_C: C -> Bar_X Omega_X(C)"
        assert certificate.status == "proved-by-FG"

    def test_universal_map_has_no_quadratic_hypothesis(self):
        certificate = universal_resolution_certificate()
        hypotheses = " ".join(certificate.hypotheses).lower()
        assert "quadratic" not in hypotheses
        assert "koszul" not in hypotheses

    def test_cubic_worked_case_retains_universal_reconstruction(self):
        packet = worked_case_packet()["truncated_cubic"]
        assert packet["theorem_a"].status == "proved-by-FG"
        assert packet["theorem_b"].status == "outside-quadratic-signature"


class TestQuadraticRecognition:
    @pytest.mark.parametrize(
        "presentation",
        (FREE_TENSOR_PRESENTATION, DUAL_NUMBERS_PRESENTATION),
    )
    def test_verified_quadratic_cases(self, presentation):
        certificate = quadratic_comparison_certificate(presentation)
        assert certificate.theorem.startswith("Theorem B")
        assert certificate.typed_map == "q_A: A^i -> Bar_X(A)"
        assert certificate.status == "proved-koszul"
        assert "Omega(A^i)->A" in certificate.conclusion

    def test_cubic_relation_has_distinct_type_signature(self):
        assert TRUNCATED_CUBIC_PRESENTATION.quadratic is False
        certificate = quadratic_comparison_certificate(
            TRUNCATED_CUBIC_PRESENTATION
        )
        assert certificate.status == "outside-quadratic-signature"

    def test_unknown_q_stays_open(self):
        presentation = type(FREE_TENSOR_PRESENTATION)(
            name="quadratic test presentation",
            connected=True,
            positive_weight=True,
            relation_degrees=(2,),
            filtered_realization_converges=True,
            q_quasi_isomorphism_verified=None,
        )
        certificate = quadratic_comparison_certificate(presentation)
        assert certificate.status == "criterion-open"
        assert "cone of q_A" in certificate.conclusion

    def test_computed_failure_stays_on_q_lane(self):
        presentation = type(FREE_TENSOR_PRESENTATION)(
            name="quadratic counterexample certificate",
            connected=True,
            positive_weight=True,
            relation_degrees=(2,),
            filtered_realization_converges=True,
            q_quasi_isomorphism_verified=False,
        )
        certificate = quadratic_comparison_certificate(presentation)
        assert certificate.status == "computed-off-koszul-locus"
        assert "cone of q_A" in certificate.conclusion
        assert universal_resolution_certificate().status == "proved-by-FG"


class TestHeutsCompletionBoundary:
    def test_unknown_object_completion_is_preserved(self):
        result = heuts_completion_certificate(
            ORDINARY_CHAIN_AMBIENT,
            algebra_nilcomplete=None,
            coalgebra_conilcomplete=None,
        )
        assert result["categorical_scope"] == "proved-by-Heuts"
        assert result["pair_in_equivalence"] is False
        assert result["algebra_nilcomplete"] is None
        assert "nilcompletion" in result["algebra_unit"]
        assert "conilcompletion" in result["coalgebra_counit"]

    def test_complete_pair_enters_equivalence(self):
        result = heuts_completion_certificate(
            ORDINARY_CHAIN_AMBIENT,
            algebra_nilcomplete=True,
            coalgebra_conilcomplete=True,
        )
        assert result["pair_in_equivalence"] is True

    @pytest.mark.parametrize(
        ("algebra_complete", "coalgebra_complete"),
        ((False, True), (True, False), (False, False)),
    )
    def test_each_completion_hypothesis_is_load_bearing(
        self, algebra_complete, coalgebra_complete
    ):
        result = heuts_completion_certificate(
            ORDINARY_CHAIN_AMBIENT,
            algebra_nilcomplete=algebra_complete,
            coalgebra_conilcomplete=coalgebra_complete,
        )
        assert result["pair_in_equivalence"] is False


class TestVerdierAndCurvedLanes:
    def test_verdier_map_has_its_own_hypothesis_package(self):
        certificate = verdier_comparison_certificate()
        assert certificate.typed_map == "v_A: D_Ran Bar_X(A) -> A^!"
        assert certificate.status == "conditional-H_VD"
        assert any("H_VD" in hypothesis for hypothesis in certificate.hypotheses)

    def test_booth_lazarev_ran_transfer_remains_typed(self):
        certificate = booth_lazarev_transfer_certificate()
        assert certificate["abstract_chain_complex_result"] == "proved"
        assert certificate["ran_factorization_transfer"] == (
            "open-hypothesis-package"
        )
        assert len(certificate["required_transfer_data"]) == 3


class TestTensorCoalgebraOracle:
    @pytest.mark.parametrize("dimension", (0, 1, 2, 3, 5))
    @pytest.mark.parametrize("length", range(7))
    def test_word_dimension(self, dimension, length):
        assert bar_word_dimension(dimension, length) == dimension**length

    def test_square_zero_d2_growth(self):
        packet = worked_case_packet()
        assert packet["square_zero_bar_dimensions_d2"] == (1, 2, 4, 8, 16, 32)

    @pytest.mark.parametrize("word_length", range(1, 9))
    @pytest.mark.parametrize("iterations", range(0, 10))
    def test_deconcatenation_against_cut_enumeration(
        self, word_length, iterations
    ):
        cuts = tuple(
            combinations(range(1, word_length), iterations)
        ) if iterations <= word_length - 1 else ()
        assert reduced_deconcatenation_summands(
            word_length, iterations
        ) == len(cuts)

    @pytest.mark.parametrize("word_length", range(0, 12))
    def test_elementwise_conilpotence_index(self, word_length):
        index = conilpotence_index(word_length)
        assert index == word_length
        assert reduced_deconcatenation_summands(word_length, index) == 0

    def test_completion_keeps_separate_support_obligation(self):
        bounded = completed_support_certificate(bounded_support=True)
        unbounded = completed_support_certificate(bounded_support=False)
        assert bounded["elementwise_conilpotent"] is True
        assert unbounded["elementwise_conilpotent"] is False
        assert unbounded["completion_requires_separate_argument"] is True

    @pytest.mark.parametrize("args", ((-1, 0), (1, -1)))
    def test_deconcatenation_rejects_invalid_degrees(self, args):
        with pytest.raises(ValueError):
            reduced_deconcatenation_summands(*args)


class TestMasterLedger:
    def test_maps_are_pairwise_distinct(self):
        maps = comparison_table()
        signatures = {certificate.typed_map for certificate in maps.values()}
        assert len(signatures) == 4

    def test_master_verification(self):
        report = verify_scope_engine()
        assert report["status"] == "verified"
        assert "full bar object universally" in report["scope_statement"]
        assert "quadratic subcoalgebra" in report["scope_statement"]

    def test_engine_contains_no_family_verdict_api(self):
        source = ENGINE.read_text()
        assert "STANDARD_FAMILIES" not in source
        assert "monograph_safe" not in source
        assert "is_koszul=True" not in source
