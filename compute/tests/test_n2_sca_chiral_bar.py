"""Tests for the finite N=2 generator screen and open bar status."""

from math import factorial

import pytest
import sympy as sp

from compute.lib.n2_sca_chiral_bar_engine import (
    GENERATORS,
    GEN_PARITY,
    GEN_WEIGHT,
    OpenN2BarCohomologyError,
    _compute_h2_at_weight_simplified,
    bar_basis_at_weight,
    bar_dim_at_weight,
    ce_differential_matrix,
    ce_h2_at_weight,
    chiral_bar_differential_data,
    chiral_bar_h2_numerical,
    chiral_bar_status_packet,
    koszulness_evidence_summary,
    max_pole_order,
    n2_ope_data,
    n2_sca_koszulness_analysis,
    ordered_screen_with_os_dimension,
)
from compute.lib.n2_superconformal_shadow import (
    n2_central_charge,
    n2_nth_products,
)


c = sp.Symbol("c")


class TestGeneratorPacket:
    def test_names_weights_and_parities(self):
        assert GENERATORS == ("T", "J", "G+", "G-")
        assert GEN_WEIGHT == {
            "T": 2,
            "J": 1,
            "G+": sp.Rational(3, 2),
            "G-": sp.Rational(3, 2),
        }
        assert GEN_PARITY == {"T": 0, "J": 0, "G+": 1, "G-": 1}

    def test_total_generator_weight(self):
        assert sum(GEN_WEIGHT.values()) == 6


class TestOPEData:
    def test_cross_engine_central_parameter(self):
        for level in (1, 2, 3, 5, 10):
            assert n2_central_charge(level) == sp.Rational(3 * level, level + 2)

    def test_vacuum_key_conversion(self):
        assert n2_ope_data()[("T", "T")][3]["1"] == c / 2
        assert n2_nth_products()[("T", "T")][3]["vac"] == c / 2

    def test_standard_supercurrent_normalization(self):
        products = n2_ope_data()[("G+", "G-")]
        assert products[2] == {"1": 2 * c / 3}
        assert products[1] == {"J": 2}
        assert products[0] == {"T": 2, "dJ": 1}

    @pytest.mark.parametrize(
        ("pair", "order"),
        [
            (("T", "T"), 4),
            (("T", "J"), 2),
            (("J", "J"), 2),
            (("J", "G+"), 1),
            (("G+", "G-"), 3),
            (("G+", "G+"), 0),
        ],
    )
    def test_max_pole_order(self, pair, order):
        assert max_pole_order(*pair) == order


class TestOrderedGeneratorScreen:
    @pytest.mark.parametrize(
        ("degree", "weight", "expected"),
        [
            (1, 1, [("J",)]),
            (1, sp.Rational(3, 2), [("G+",), ("G-",)]),
            (1, 2, [("T",)]),
            (2, 2, [("J", "J")]),
            (2, sp.Rational(5, 2), [("J", "G+"), ("J", "G-"), ("G+", "J"), ("G-", "J")]),
        ],
    )
    def test_word_enumeration(self, degree, weight, expected):
        assert bar_basis_at_weight(degree, weight) == expected
        assert bar_dim_at_weight(degree, weight) == len(expected)

    def test_os_dimension_is_a_separate_factor(self):
        packet = ordered_screen_with_os_dimension(3, 3)
        assert packet["os_top_dimension"] == factorial(2)
        assert packet["tensor_product_upper_bound"] == 2 * packet["word_dimension"]
        assert packet["status"] == "finite generator/OS screen"


class TestOpenBarCohomology:
    @pytest.mark.parametrize(
        ("function", "args"),
        [
            (ce_differential_matrix, (3,)),
            (ce_h2_at_weight, (3,)),
            (chiral_bar_h2_numerical, (1.0,)),
            (_compute_h2_at_weight_simplified, (3, 1.0)),
        ],
    )
    def test_cohomology_calls_fail_loudly(self, function, args):
        with pytest.raises(OpenN2BarCohomologyError):
            function(*args)

    def test_differential_packet_stops_before_map(self):
        packet = chiral_bar_differential_data(3)
        assert packet["differential"] is None
        assert packet["ope"] == n2_ope_data()

    def test_status_packet(self):
        packet = chiral_bar_status_packet()
        assert packet["status"] == "open"
        assert packet["H2"] is None
        assert packet["quadratic_koszul"] is None

    def test_analysis_reports_finite_screens_only(self):
        packet = n2_sca_koszulness_analysis(1)
        assert packet["status"] == "open"
        assert packet["quadratic_koszul"] is None
        assert packet["finite_screens"]["3"][2] == bar_dim_at_weight(2, 3)

    def test_evidence_summary_names_obligations(self):
        packet = koszulness_evidence_summary()
        assert packet["status"] == "open"
        assert packet["quadratic_koszul"] is None
        assert "construct the signed residue differential" in packet["remaining_obligations"]
