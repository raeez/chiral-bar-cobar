"""Exact W3 input checks and loud bar-cohomology boundary."""

import pytest
import sympy as sp

from compute.lib.bar_cohomology_w3_explicit_engine import (
    OpenW3BarCohomologyError,
    W3BarCohomologyEngine,
    _motzkin_numbers,
    bar_chain_dim,
    verify_curvature_complementarity,
    verify_ope_data,
    virasoro_bar_dims,
    w3_bar_dims,
    w3_gf_from_formula,
    w3_vacuum_dims,
)


def test_generic_vacuum_character_is_exact():
    dimensions = w3_vacuum_dims(10)
    assert {weight: dimensions[weight] for weight in range(9)} == {
        0: 0,
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 8,
        7: 10,
        8: 17,
    }


def test_raw_chain_count_keeps_arnold_top_form_factor_explicit():
    assert bar_chain_dim(1, 2) == 1
    assert bar_chain_dim(2, 4) == 1
    assert bar_chain_dim(3, 6) == 2


def test_ope_checks_use_repaired_normalization():
    assert all(verify_ope_data(7).values())


def test_formal_reflection_and_leading_norm_ratio_are_typed():
    packet = verify_curvature_complementarity()
    assert packet["formal_reflected_central_sum"] == 100
    assert packet["leading_norm_ratio"] == sp.Rational(2, 3)
    assert packet["bar_curvature"].status == "open"
    assert packet["modular_conductor"].status == "open"


@pytest.mark.parametrize("operation", [lambda: w3_bar_dims(8), lambda: virasoro_bar_dims(8), lambda: w3_gf_from_formula(8)])
def test_legacy_dimension_sequences_require_a_constructed_differential(operation):
    with pytest.raises(OpenW3BarCohomologyError):
        operation()


def test_motzkin_sequence_remains_pure_combinatorics():
    assert _motzkin_numbers(9) == [1, 1, 2, 4, 9, 21, 51, 127, 323]


def test_engine_summary_separates_exact_inputs_from_open_outputs():
    engine = W3BarCohomologyEngine(max_n=4, max_h=10, c_val=7)
    summary = engine.summary()
    assert all(summary["ope_checks"].values())
    assert summary["vacuum_dimensions"][8] == 17
    assert summary["bar_differential"].status == "open"
    assert summary["cohomology"].status == "open"
    assert summary["koszulness"].status == "open"
