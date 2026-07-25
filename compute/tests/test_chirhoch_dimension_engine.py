"""Exact arithmetic and status tests for ``chirhoch_dimension_engine``."""

from __future__ import annotations

from math import comb
from pathlib import Path

import pytest

from compute.lib.chirhoch_dimension_engine import (
    DUAL_COXETER_NUMBERS,
    THEOREM_H_REQUIRED_COMPONENTS,
    affine_bounded_upper_bound,
    all_standard_families,
    chirhoch_affine_km,
    chirhoch_dimensions,
    chirhoch_free_betagamma,
    chirhoch_free_fermion_bc,
    chirhoch_heisenberg,
    chirhoch_lattice,
    chirhoch_virasoro,
    chirhoch_w_algebra,
    dim_simple_lie_algebra,
    generate_summary_table,
    heisenberg_bounded_hilbert_polynomial,
    heisenberg_level_rescaling_exactness_window_check,
    heisenberg_outer_derivation_window_check,
    koszul_duality_check,
    old_theorem_h_bound_holds,
    rank_simple_lie_algebra,
    theorem_h_concentration_holds,
    theorem_h_scope_record,
)


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute/lib/chirhoch_dimension_engine.py"


class TestLieArithmetic:
    @pytest.mark.parametrize("N", range(2, 13))
    def test_type_a_dimension(self, N):
        assert dim_simple_lie_algebra(f"sl_{N}") == N * N - 1
        assert rank_simple_lie_algebra(f"sl_{N}") == N - 1

    @pytest.mark.parametrize(
        ("name", "dimension", "rank"),
        [
            ("so_5", 10, 2),
            ("sp_4", 10, 2),
            ("so_8", 28, 4),
            ("G2", 14, 2),
            ("F4", 52, 4),
            ("E6", 78, 6),
            ("E7", 133, 7),
            ("E8", 248, 8),
        ],
    )
    def test_named_dimensions_and_ranks(self, name, dimension, rank):
        assert dim_simple_lie_algebra(name) == dimension
        assert rank_simple_lie_algebra(name) == rank

    def test_low_rank_isomorphism_dimensions(self):
        assert dim_simple_lie_algebra("so_3") == dim_simple_lie_algebra("sl_2")
        assert dim_simple_lie_algebra("so_5") == dim_simple_lie_algebra("sp_4")
        assert dim_simple_lie_algebra("so_6") == dim_simple_lie_algebra("sl_4")

    def test_exceptional_dimensions_from_root_counts(self):
        assert dim_simple_lie_algebra("G2") == 2 + 12
        assert dim_simple_lie_algebra("F4") == 4 + 48
        assert dim_simple_lie_algebra("E8") == 8 + 240

    def test_type_a_dual_coxeter_numbers(self):
        for N in range(2, 7):
            assert DUAL_COXETER_NUMBERS[f"sl_{N}"] == N

    def test_input_validation(self):
        with pytest.raises(ValueError):
            dim_simple_lie_algebra("sl_1")
        with pytest.raises(KeyError):
            dim_simple_lie_algebra("mystery")


class TestBoundedBenchmarks:
    def test_rank_one_even_superboson(self):
        row = chirhoch_heisenberg()
        assert row.bounded_support == (0, 1)
        assert row.bounded_dimensions == {0: 2, 1: 1}
        assert row.bounded_status == "proved-bounded-BDSK-Theorem-7.4"
        assert row.bounded_prefix(5) == (2, 1, 0, 0, 0, 0)

    def test_virasoro(self):
        row = chirhoch_virasoro()
        assert row.bounded_support == (0, 2, 3)
        assert row.bounded_dimensions == {0: 1, 2: 1, 3: 1}
        assert row.bounded_status == "proved-bounded-BDSK-Theorem-7.2"

    def test_w2_routes_to_virasoro_bounded_result(self):
        row = chirhoch_w_algebra(2)
        assert row.family == "W_2 = Virasoro"
        assert row.bounded_support == (0, 2, 3)
        assert row.bounded_dimensions == {0: 1, 2: 1, 3: 1}

    @pytest.mark.parametrize(
        "row",
        [
            chirhoch_affine_km("sl_2"),
            chirhoch_free_fermion_bc(),
            chirhoch_free_betagamma(),
            chirhoch_w_algebra(3),
            chirhoch_lattice(1),
        ],
    )
    def test_other_bounded_vectors_are_withheld(self, row):
        assert row.bounded_dimensions is None


class TestHeisenbergFirstPrinciplesWindow:
    """Finite-window, first-principles checks of the two mechanisms behind
    the bounded Heisenberg profile (2, 1, 0, ...) with support {0, 1}.

    Scope discipline: these are mode-level Lie-algebra computations on
    h = span{alpha_m} + CK.  They witness (i) an explicit outer derivation
    (the H^1 generator's mechanism) and (ii) exactness of the level
    cocycle under the rescaling 1-cochain (the H^2-killing mechanism).
    They do NOT recompute the full chiral cohomology; the bounded profile
    itself remains ProvedElsewhere (BDSK Theorem 7.4), carried by
    ``chirhoch_heisenberg()`` and asserted in TestBoundedBenchmarks.
    """

    @pytest.mark.parametrize("window", [3, 6, 10])
    def test_outer_derivation_witness(self, window):
        result = heisenberg_outer_derivation_window_check(window)
        assert result["derivation_identity_on_window"] is True
        assert result["inner_derivations_kill_alpha0"] is True
        assert result["D_is_outer"] is True

    @pytest.mark.parametrize("window", [3, 6, 10])
    def test_level_cocycle_exact(self, window):
        result = heisenberg_level_rescaling_exactness_window_check(window)
        assert result["level_cocycle_exact_on_window"] is True

    def test_hilbert_polynomial_is_2_plus_t(self):
        """Coefficients computed from the profile dict: 2 + t."""
        assert heisenberg_bounded_hilbert_polynomial() == (2, 1)


class TestAffineConjecturalBound:
    @pytest.mark.parametrize("lie_algebra", ["sl_2", "sl_3", "G2", "E8"])
    def test_exact_zero_mode_metadata(self, lie_algebra):
        row = chirhoch_affine_km(lie_algebra)
        expected = dim_simple_lie_algebra(lie_algebra)
        assert row.prequotient_dimension == expected
        assert row.known_inner_zero_mode_dimension == expected
        assert row.chart_dimensions is None
        assert row.dim1 is None
        assert row.bounded_status == "conjectural-BDSK-Conjecture-7.5-bound"

    @pytest.mark.parametrize("degree", range(0, 6))
    def test_sl2_bound_right_side(self, degree):
        expected = (
            (comb(3, degree) if degree <= 3 else 0)
            + (comb(3, degree + 1) if degree + 1 <= 3 else 0)
        )
        assert affine_bounded_upper_bound("sl_2", degree) == expected

    def test_negative_degree_bound_is_zero(self):
        assert affine_bounded_upper_bound("sl_3", -1) == 0


class TestChartFirewall:
    @pytest.mark.parametrize("row", all_standard_families())
    def test_default_chart_fields_are_open(self, row):
        assert row.chart_support is None
        assert row.chart_dimensions is None
        assert row.dim0 is None
        assert row.dim1 is None
        assert row.dim2 is None
        assert row.total is None
        assert row.hilbert_triple is None
        assert row.poincare_poly is None
        assert row.concentrated_in_012 is None
        assert row.chart_status == "open-family-support-datum"

    def test_legacy_predicates_withhold_verdicts(self):
        row = chirhoch_virasoro()
        assert old_theorem_h_bound_holds(row) is None
        assert theorem_h_concentration_holds(row) is None
        assert koszul_duality_check(row, row) is None

    def test_scope_record_names_family_support_datum(self):
        record = theorem_h_scope_record("virasoro", applies=True)
        assert record["claim"] == "H_H(A;S) implies Supp ChirHoch(A) subset S"
        assert record["applies"] is None
        assert record["status"] == "open-explicit-family-support-datum"
        assert record["hypotheses"] == THEOREM_H_REQUIRED_COMPONENTS
        assert record["legacy_applies_argument"] is True


class TestDispatcherAndValidation:
    def test_aliases(self):
        assert chirhoch_dimensions("heis") == chirhoch_heisenberg()
        assert chirhoch_dimensions("vir") == chirhoch_virasoro()
        assert chirhoch_dimensions("bc") == chirhoch_free_fermion_bc()
        assert chirhoch_dimensions("bg") == chirhoch_free_betagamma()

    def test_parameterized_families(self):
        assert chirhoch_dimensions("affine_km", lie_algebra="sl_4").prequotient_dimension == 15
        assert chirhoch_dimensions("w_algebra", N=4).family == "principal W_4"
        assert chirhoch_dimensions("lattice", rank=3).family.endswith("rank 3")

    def test_missing_parameters_raise(self):
        with pytest.raises(ValueError):
            chirhoch_dimensions("affine_km")
        with pytest.raises(ValueError):
            chirhoch_dimensions("w_algebra")
        with pytest.raises(ValueError):
            chirhoch_dimensions("lattice")

    def test_invalid_family_raises(self):
        with pytest.raises(KeyError):
            chirhoch_dimensions("mystery")


class TestSummary:
    def test_summary_displays_bounded_and_chart_statuses(self):
        summary = generate_summary_table()
        assert "rank-one even superboson" in summary
        assert "support=(0, 2, 3)" in summary
        assert "open-family-support-datum" in summary
        assert "{0: 2, 1: 1}" in summary

    def test_retired_bureaucratic_stem_is_absent(self):
        assert ("cert" + "if") not in ENGINE.read_text(encoding="utf-8").lower()
