"""Tests for the typed CE/chiral-bar comparison boundary."""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.ce_vs_chiral_bar_reconciliation_engine import (
    OpenCEBarComparisonError,
    compare_resolutions_virasoro,
    minimal_resolution_dimensions_ce_witt,
    minimal_resolution_dimensions_virasoro,
    n2sca_h2_classes,
    n2sca_subleading_d2_kills_h2,
    n2sca_super_ce_chain_table,
    n2sca_super_ce_table,
    os_dimension,
    poincare_duality_check_sl2,
    poincare_duality_check_virasoro,
    reconcile_n2,
    reconcile_virasoro,
    reconcile_w3_at_weight_4,
    reconciliation_report,
    sl2_ce_vs_bar_with_os,
    virasoro_bar_dimensions_known,
    w3_bar_dimensions_known,
    w3_ce_leading_pole,
    w3_negative_mode_bracket,
    w3_pbw_ss_pages,
    witt_ce_chain_dimensions,
    witt_ce_dimensions,
    witt_negative_mode_bracket,
)


def test_witt_bracket_and_exterior_chain_dimensions():
    assert witt_negative_mode_bracket(2, 3) == {5: 1}
    assert witt_negative_mode_bracket(3, 2) == {5: -1}
    assert witt_negative_mode_bracket(2, 2) == {}
    dimensions = witt_ce_chain_dimensions(10)
    assert dimensions[(1, 2)] == 1
    assert dimensions[(1, 10)] == 1
    assert dimensions[(2, 5)] == 1
    assert dimensions[(2, 6)] == 1


def test_virasoro_packet_separates_chain_data_and_comparison():
    packet = reconcile_virasoro(10)
    assert packet.exact_inputs["ce_chain_dimensions"][(2, 5)] == 1
    assert packet.ce_cohomology.status == "open"
    assert packet.chiral_bar_cohomology.status == "open"
    assert packet.comparison.status == "open"


def test_w3_packet_keeps_nonlinear_ww_channel():
    packet = w3_negative_mode_bracket(8)
    assert packet["linear_brackets"][("L_-2", "W_-3")] == {"W_-5": -1}
    c = sp.Symbol("c")
    assert packet["WW_OPE"][1]["Lambda"] == 32 / (22 + 5 * c)
    assert packet["WW_OPE"][0]["dLambda"] == 16 / (22 + 5 * c)
    assert packet["linear_ce_model"].status == "open"


def test_w3_weight_four_comparison_is_open_with_exact_norm_input():
    packet = reconcile_w3_at_weight_4()
    c = sp.Symbol("c")
    assert packet.exact_inputs["N_Lambda"] == c * (5 * c + 22) / 10
    assert packet.comparison.status == "open"


def test_n2_chain_table_and_comparison_packet():
    table = n2sca_super_ce_chain_table(8)
    assert table[(1, Fraction(1, 1))] == 1
    assert table[(1, Fraction(3, 2))] == 2
    packet = reconcile_n2(8)
    assert packet.exact_inputs["sample_G+G-_bracket"] == {
        ("L", Fraction(-4)): 2,
        ("J", Fraction(-4)): 1,
    }
    assert packet.comparison.status == "open"


@pytest.mark.parametrize("n,expected", [(1, 1), (2, 1), (3, 2), (4, 6), (5, 24)])
def test_arnold_top_degree_dimension(n, expected):
    assert os_dimension(n) == expected


def test_os_dimension_is_input_rather_than_dimension_multiplier():
    packet = sl2_ce_vs_bar_with_os()
    assert packet.exact_inputs["OS_top_dimensions"][6] == 120
    assert packet.comparison.status == "open"
    assert any("chain map" in item for item in packet.comparison.hypotheses)


@pytest.mark.parametrize(
    "operation",
    [
        lambda: witt_ce_dimensions(8),
        lambda: virasoro_bar_dimensions_known(8),
        lambda: w3_ce_leading_pole(8),
        lambda: w3_bar_dimensions_known(8),
        lambda: n2sca_super_ce_table(8),
    ],
)
def test_historical_numeric_promotions_stop_at_comparison_boundary(operation):
    with pytest.raises(OpenCEBarComparisonError):
        operation()


def test_all_remaining_comparison_claims_are_explicitly_open():
    packets = [
        n2sca_h2_classes(),
        n2sca_subleading_d2_kills_h2(),
        poincare_duality_check_virasoro(),
        poincare_duality_check_sl2(),
        w3_pbw_ss_pages(),
        minimal_resolution_dimensions_virasoro(),
        minimal_resolution_dimensions_ce_witt(),
        compare_resolutions_virasoro(),
    ]
    assert {packet.status for packet in packets} == {"open"}


def test_reconciliation_report_has_no_promoted_equality():
    report = reconciliation_report(6)
    assert report["status"] == "finite presentations exact; comparison theorems open"
    for family in ("Virasoro", "W3", "N2", "sl2"):
        assert report[family].comparison.status == "open"
