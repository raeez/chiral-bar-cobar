r"""Exact tests for the finite bar and Swiss-cheese scope engine."""

from pathlib import Path

import pytest
from sympy import Matrix, Rational, Symbol, zeros

from compute.lib.sc_bar_cobar_inversion_engine import (
    DUAL_NUMBERS,
    TRUNCATED_CUBIC,
    TruncatedPolynomialAlgebra,
    affine_sl2_current_certificate,
    bar_basis,
    bar_d_squared_matrix,
    bar_differential,
    bar_differential_terms,
    bar_homology_dimension,
    bar_homology_table,
    first_quadratic_obstruction,
    level_pairing,
    quadratic_coalgebra_homology_dimension,
    quadratic_comparison_defects,
    sector_ledger,
    sl2_bracket,
    verify_bar_d_squared,
    verify_engine,
    worked_case_report,
)


ENGINE = Path("compute/lib/sc_bar_cobar_inversion_engine.py")


class TestAugmentedAlgebras:
    def test_dual_numbers_signature(self):
        assert DUAL_NUMBERS.name == "Q[x]/(x^2)"
        assert DUAL_NUMBERS.augmentation_basis == (1,)
        assert DUAL_NUMBERS.quadratic is True
        assert DUAL_NUMBERS.multiply_exponents(1, 1) is None

    def test_truncated_cubic_signature(self):
        assert TRUNCATED_CUBIC.name == "Q[x]/(x^3)"
        assert TRUNCATED_CUBIC.augmentation_basis == (1, 2)
        assert TRUNCATED_CUBIC.quadratic is False
        assert TRUNCATED_CUBIC.multiply_exponents(1, 1) == 2
        assert TRUNCATED_CUBIC.multiply_exponents(1, 2) is None

    @pytest.mark.parametrize("m", (0, 1, -3))
    def test_truncation_exponent_has_valid_range(self, m):
        with pytest.raises(ValueError):
            TruncatedPolynomialAlgebra(m)

    def test_bar_basis_is_weight_exact(self):
        basis = bar_basis(TRUNCATED_CUBIC, weight=5, length=3)
        assert basis == ((1, 2, 2), (2, 1, 2), (2, 2, 1))
        assert all(sum(word) == 5 and len(word) == 3 for word in basis)

    def test_weight_zero_coaugmentation_is_outside_reduced_complex(self):
        assert bar_basis(TRUNCATED_CUBIC, 0, 0) == ((),)
        assert bar_basis(TRUNCATED_CUBIC, 0, 1) == ()


class TestReducedBarDifferential:
    def test_dual_numbers_differential_vanishes(self):
        for length in range(1, 8):
            word = (1,) * length
            assert bar_differential_terms(DUAL_NUMBERS, word) == {}

    def test_cubic_binary_product(self):
        assert bar_differential_terms(TRUNCATED_CUBIC, (1, 1)) == {(2,): 1}

    def test_cubic_ternary_signs(self):
        assert bar_differential_terms(TRUNCATED_CUBIC, (1, 1, 1)) == {
            (2, 1): 1,
            (1, 2): -1,
        }

    def test_cubic_weight_two_matrix(self):
        differential = bar_differential(TRUNCATED_CUBIC, 2, 2)
        assert differential.source_basis == ((1, 1),)
        assert differential.target_basis == ((2,),)
        assert differential.matrix == Matrix([[1]])
        assert differential.rank == 1

    def test_cubic_weight_three_matrix(self):
        differential = bar_differential(TRUNCATED_CUBIC, 3, 3)
        assert differential.source_basis == ((1, 1, 1),)
        assert differential.target_basis == ((1, 2), (2, 1))
        assert differential.matrix == Matrix([[-1], [1]])

    @pytest.mark.parametrize("m", range(2, 8))
    def test_d_squared_in_large_finite_window(self, m):
        algebra = TruncatedPolynomialAlgebra(m)
        assert verify_bar_d_squared(algebra, max_weight=16, max_length=12)

    @pytest.mark.parametrize("m", range(2, 6))
    @pytest.mark.parametrize("weight", range(1, 11))
    @pytest.mark.parametrize("length", range(2, 8))
    def test_each_d_squared_block(self, m, weight, length):
        algebra = TruncatedPolynomialAlgebra(m)
        square = bar_d_squared_matrix(algebra, weight, length)
        assert square == zeros(*square.shape)

    def test_invalid_bar_letter_is_rejected(self):
        with pytest.raises(ValueError):
            bar_differential_terms(TRUNCATED_CUBIC, (1, 3))


class TestExactBarHomology:
    @pytest.mark.parametrize("weight", range(1, 11))
    def test_dual_numbers_diagonal_class(self, weight):
        assert bar_homology_dimension(DUAL_NUMBERS, weight, weight) == 1
        if weight > 1:
            assert bar_homology_dimension(DUAL_NUMBERS, weight, weight - 1) == 0

    def test_dual_numbers_table(self):
        expected = {(weight, weight): 1 for weight in range(1, 9)}
        assert bar_homology_table(
            DUAL_NUMBERS, max_weight=8, max_length=8
        ) == expected

    def test_cubic_first_period(self):
        table = bar_homology_table(
            TRUNCATED_CUBIC, max_weight=7, max_length=7
        )
        assert table == {
            (1, 1): 1,
            (3, 2): 1,
            (4, 3): 1,
            (6, 4): 1,
            (7, 5): 1,
        }

    @pytest.mark.parametrize(
        ("weight", "length"),
        ((1, 1), (3, 2), (4, 3), (6, 4), (7, 5), (9, 6), (10, 7)),
    )
    def test_cubic_periodic_classes(self, weight, length):
        assert bar_homology_dimension(TRUNCATED_CUBIC, weight, length) == 1

    def test_weight_two_pair_is_boundary(self):
        assert bar_homology_dimension(TRUNCATED_CUBIC, 2, 1) == 0
        assert bar_homology_dimension(TRUNCATED_CUBIC, 2, 2) == 0


class TestQuadraticComparison:
    @pytest.mark.parametrize("weight", range(1, 10))
    def test_dual_numbers_quadratic_coalgebra_equals_bar_homology(self, weight):
        source = quadratic_coalgebra_homology_dimension(
            DUAL_NUMBERS, weight, weight
        )
        target = bar_homology_dimension(DUAL_NUMBERS, weight, weight)
        assert source == target == 1

    def test_dual_numbers_have_no_q_defect(self):
        assert quadratic_comparison_defects(
            DUAL_NUMBERS, max_weight=12, max_length=12
        ) == ()
        assert first_quadratic_obstruction(DUAL_NUMBERS) is None

    def test_cubic_first_q_defect_is_relation_class(self):
        obstruction = first_quadratic_obstruction(TRUNCATED_CUBIC)
        assert obstruction is not None
        assert (obstruction.weight, obstruction.bar_length) == (3, 2)
        assert obstruction.source_homology_dimension == 0
        assert obstruction.target_homology_dimension == 1
        assert obstruction.cone_homology_dimension == 1

    def test_cubic_q_source_contains_indecomposable(self):
        assert quadratic_coalgebra_homology_dimension(
            TRUNCATED_CUBIC, 1, 1
        ) == 1
        assert quadratic_coalgebra_homology_dimension(
            TRUNCATED_CUBIC, 3, 2
        ) == 0

    def test_theorem_a_survives_cubic_obstruction(self):
        report = worked_case_report(TRUNCATED_CUBIC)
        assert report["theorem_a"].status == "proved-by-FG"
        assert report["theorem_b_status"] == "computed-obstruction"
        assert report["theorem_b_map"] == "q_A: A^i -> Bar(A)"

    def test_dual_numbers_q_is_global_identity(self):
        report = worked_case_report(DUAL_NUMBERS)
        assert report["theorem_b_status"] == (
            "proved-all-weights: A^i equals Bar(A)"
        )


class TestSwissCheeseTyping:
    def test_open_and_closed_outputs(self):
        ledger = sector_ledger()
        assert ledger.open_chart == "A"
        assert ledger.closed_actor == "Z_ch^der(A)=RHom_{A^e}(A,A)"
        assert ledger.open_closed_action == "Z_ch^der(A) acts on the open chart A"

    def test_reconstruction_and_quadratic_maps_are_distinct(self):
        ledger = sector_ledger()
        assert ledger.universal_reconstruction == (
            "epsilon_A: Omega_X Bar_X(A) -> A"
        )
        assert ledger.quadratic_comparison == "q_A: A^i -> Bar_X(A)"
        assert ledger.full_bar_object == "Bar_X(A)"

    def test_verdier_lane_has_named_hypothesis(self):
        ledger = sector_ledger()
        assert ledger.verdier_object == "D_Ran Bar_X(A)"
        assert "H_VD" in ledger.status["verdier_object"]

    def test_physical_bulk_identification_is_conditional(self):
        ledger = sector_ledger()
        assert "conditional" in ledger.status["closed_actor"]
        assert "H_OC" in ledger.status["open_closed_action"]


class TestAffineCurrentInput:
    @pytest.mark.parametrize("level", (Rational(0), Rational(1), Rational(-3), Symbol("k")))
    def test_jacobi_and_pairing_invariance(self, level):
        certificate = affine_sl2_current_certificate(level)
        assert certificate["jacobi_verified"] is True
        assert certificate["pairing_invariance_verified"] is True
        assert certificate["jacobi_failures"] == ()
        assert certificate["pairing_invariance_failures"] == ()
        assert certificate["bar_claim_status"] == "uncomputed from OPE data alone"

    def test_sl2_structure_constants(self):
        assert sl2_bracket("e", "f") == (0, 0, 1)
        assert sl2_bracket("h", "e") == (2, 0, 0)
        assert sl2_bracket("h", "f") == (0, -2, 0)

    def test_level_pairing(self):
        k = Symbol("k")
        assert level_pairing("e", "f", k) == k
        assert level_pairing("f", "e", k) == k
        assert level_pairing("h", "h", k) == 2 * k
        assert level_pairing("e", "e", k) == 0


class TestEngineLedger:
    def test_master_verification(self):
        report = verify_engine()
        assert report["status"] == "verified"
        assert report["dual_numbers"]["first_cone_obstruction"] is None
        obstruction = report["truncated_cubic"]["first_cone_obstruction"]
        assert (obstruction.weight, obstruction.bar_length) == (3, 2)

    def test_fabricated_claim_patterns_are_absent(self):
        source = ENGINE.read_text()
        assert "Theorem B (thm:bar-cobar-inversion-qi)" not in source
        assert "ALL_CLAIMS_VERIFIED" not in source
        assert "bar_cohomology = {0: 1, 1: 0, 2: 1}" not in source
        assert "recovers_closed_colour" not in source
        assert "Contracting homotopy" not in source
