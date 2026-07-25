"""Tests for exact N=2 OPE weight bookkeeping and open H2 status."""

import pytest
import sympy as sp

from compute.lib.n2_sca_chiral_bar_weight_graded_engine import (
    ChiralBarN2SCA,
    OpenWeightGradedBarError,
    analyze_mode1_correction,
    mode_1_product,
    mode_1_product_weight_shift,
    n2_sca_chiral_bar_h2_at_weight3,
    n2_sca_h2_analysis,
    nth_product_output_weight,
)


class TestNthProductWeights:
    @pytest.mark.parametrize(
        ("a", "b", "n", "weight"),
        [
            ("T", "T", 3, 0),
            ("T", "T", 1, 2),
            ("T", "J", 1, 1),
            ("T", "G+", 1, sp.Rational(3, 2)),
            ("J", "J", 1, 0),
            ("G+", "G-", 2, 0),
            ("G+", "G-", 1, 1),
            ("G+", "G-", 0, 2),
        ],
    )
    def test_weight_formula(self, a, b, n, weight):
        assert nth_product_output_weight(a, b, n) == weight

    def test_mode_one_products(self):
        assert mode_1_product("T", "T") == {"T": 2}
        assert mode_1_product("T", "J") == {"J": 1}
        assert mode_1_product("G+", "G-") == {"J": 2}
        assert mode_1_product("G-", "G+") == {"J": -2}
        assert mode_1_product("J", "G+") == {}

    def test_all_recorded_mode_one_weights(self):
        packet = mode_1_product_weight_shift()
        assert packet[("G+", "G-")]["expected_output_weight"] == 1
        assert packet[("T", "G+")]["expected_output_weight"] == sp.Rational(3, 2)
        assert packet[("J", "J")]["expected_output_weight"] == 0


class TestOpenFilteredCohomology:
    def test_handle_status(self):
        handle = ChiralBarN2SCA(central_charge=1, max_weight_half=10)
        packet = handle.status()
        assert packet["status"] == "open"
        assert packet["H2"] is None
        assert packet["quadratic_koszul"] is None

    def test_h2_call_fails_loudly(self):
        with pytest.raises(OpenWeightGradedBarError):
            ChiralBarN2SCA().h2_at_weight(6)

    def test_mode_one_correction_is_unconstructed(self):
        packet = analyze_mode1_correction({"CE_H2": 5})
        assert packet["status"] == "open filtered comparison"
        assert packet["induced_spectral_sequence_map"] is None
        assert packet["input_ce_data"] == {"CE_H2": 5}

    def test_analysis_packet(self):
        packet = n2_sca_h2_analysis(max_weight_half=8, c_val=1)
        assert packet["status"] == "open"
        assert packet["H2"] is None
        assert packet["mode_1_weight_checks"]

    def test_weight_three_packet(self):
        packet = n2_sca_chiral_bar_h2_at_weight3()
        assert packet["conformal_weight"] == 3
        assert packet["half_weight"] == 6
        assert packet["H2"] is None
