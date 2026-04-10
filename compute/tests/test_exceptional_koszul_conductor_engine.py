"""Tests for exact principal W conductor data at exceptional Lie types.

The new engine keeps both conductor surfaces explicit:
  - central-charge complement: c(k) + c(k')
  - kappa complementarity: kappa(k) + kappa(k')

Type A is checked against the existing canonical engines.
Exceptional values are checked against independently derived exact constants.
"""

from fractions import Fraction

import pytest

from compute.lib.alpha_n_conductor_engine import K_WN, alpha_N
from compute.lib.exceptional_koszul_conductor_engine import (
    ALL_SUPPORTED_TYPES,
    EXCEPTIONAL_TYPES,
    KAPPA_COMPLEMENTARITIES,
    KOSZUL_CONDUCTORS,
    TYPE_A_TYPES,
    anomaly_ratio,
    dual_level,
    expected_kappa_complementarity,
    expected_koszul_conductor,
    export_kappa_complementarities,
    export_koszul_conductors,
    generator_weights,
    kappa_complementarity,
    koszul_conductor,
    lie_data,
    principal_w_central_charge,
    principal_w_kappa,
    verify_all,
    verify_k_independence,
    weyl_rho_squared,
)
from compute.lib.wn_central_charge_canonical import c_wn_fl


TYPE_A_TO_N = {
    "A1": 2,
    "A2": 3,
    "A3": 4,
    "A4": 5,
    "A5": 6,
}

TEST_K_VALUES = (
    Fraction(-1),
    Fraction(0),
    Fraction(1),
    Fraction(2),
    Fraction(5),
)


ANOMALY_RATIO_EXPECTED = {
    "G2": Fraction(2, 3),  # VERIFIED: [DC] 1/2 + 1/6 = 2/3 from exponents {1,5}; [LT] chapters/examples/w_algebras.tex `rem:general-w-kappa-values` lists 2/3.
    "F4": Fraction(7, 8),  # VERIFIED: [DC] 1/2 + 1/6 + 1/8 + 1/12 = 7/8 from exponents {1,5,7,11}; [LT] `rem:general-w-kappa-values` lists 7/8.
    "E6": Fraction(427, 360),  # VERIFIED: [DC] 1/2 + 1/5 + 1/6 + 1/8 + 1/9 + 1/12 = 427/360; [LT] `rem:general-w-kappa-values` lists 427/360.
    "E7": Fraction(2777, 2520),  # VERIFIED: [DC] summing 1/(m_i+1) for exponents {1,5,7,9,11,13,17} gives 2777/2520; [LT] `rem:general-w-kappa-values` lists 2777/2520.
    "E8": Fraction(121, 126),  # VERIFIED: [DC] summing 1/(m_i+1) for exponents {1,7,11,13,17,19,23,29} gives 121/126; [LT] `rem:general-w-kappa-values` lists 121/126.
}

EXCEPTIONAL_CONDUCTOR_EXPECTED = {
    "G2": Fraction(228),  # VERIFIED: [DC] 2r + 4*dim*h_dual = 4 + 4*14*4 = 228; [CF] c(0) = -124 and c(-8) = 352, so c(0)+c(-8) = 228.
    "F4": Fraction(1880),  # VERIFIED: [DC] 2r + 4*dim*h_dual = 8 + 4*52*9 = 1880; [CF] c(0) = -3324 and c(-18) = 5204, so c(0)+c(-18) = 1880.
    "E6": Fraction(3756),  # VERIFIED: [DC] 2r + 4*dim*h_dual = 12 + 4*78*12 = 3756; [CF] c(0) = -9432 and c(-24) = 13188, so c(0)+c(-24) = 3756.
    "E7": Fraction(9590),  # VERIFIED: [DC] 2r + 4*dim*h_dual = 14 + 4*133*18 = 9590; [CF] c(0) = -38430 and c(-36) = 48020, so c(0)+c(-36) = 9590.
    "E8": Fraction(29776),  # VERIFIED: [DC] 2r + 4*dim*h_dual = 16 + 4*248*30 = 29776; [CF] c(0) = -208560 and c(-60) = 238336, so c(0)+c(-60) = 29776.
}

EXCEPTIONAL_KAPPA_EXPECTED = {
    "G2": Fraction(152),  # VERIFIED: [DC] (2/3) * 228 = 152; [CF] kappa(0) = -248/3 and kappa(-8) = 704/3, so the sum is 152.
    "F4": Fraction(1645),  # VERIFIED: [DC] (7/8) * 1880 = 1645; [CF] kappa(0) = -29085/8 and kappa(-18) = 45535/8, so the sum is 1645.
    "E6": Fraction(133651, 30),  # VERIFIED: [DC] (427/360) * 3756 = 133651/30; [CF] kappa(0) = -447004/40 and kappa(-24) = 625008/40, so the sum is 133651/30.
    "E7": Fraction(380449, 36),  # VERIFIED: [DC] (2777/2520) * 9590 = 380449/36; [CF] kappa(0) = -10672861/72 and kappa(-36) = 11433759/72, so the sum is 380449/36.
    "E8": Fraction(1801448, 63),  # VERIFIED: [DC] (121/126) * 29776 = 1801448/63; [CF] kappa(0) = -25235760/126 and kappa(-60) = 28838656/126, so the sum is 1801448/63.
}

RHO_SQUARED_EXPECTED = {
    "A1": Fraction(1, 2),  # VERIFIED: [DC] dim*h_dual/12 = 3*2/12 = 1/2; [LT] this is the standard |rho|^2 value for sl_2.
    "A2": Fraction(2),  # VERIFIED: [DC] 8*3/12 = 2; [LT] standard Weyl-vector norm for sl_3.
    "A3": Fraction(5),  # VERIFIED: [DC] 15*4/12 = 5; [LT] standard Weyl-vector norm for sl_4.
    "A4": Fraction(10),  # VERIFIED: [DC] 24*5/12 = 10; [LT] standard Weyl-vector norm for sl_5.
    "A5": Fraction(35, 2),  # VERIFIED: [DC] 35*6/12 = 35/2; [LT] standard Weyl-vector norm for sl_6.
    "G2": Fraction(14, 3),  # VERIFIED: [DC] 14*4/12 = 14/3; [LT] standard G2 Weyl-vector norm with long-root normalization.
    "F4": Fraction(39),  # VERIFIED: [DC] 52*9/12 = 39; [LT] standard F4 Weyl-vector norm with long-root normalization.
    "E6": Fraction(78),  # VERIFIED: [DC] 78*12/12 = 78; [LT] standard E6 Weyl-vector norm.
    "E7": Fraction(399, 2),  # VERIFIED: [DC] 133*18/12 = 399/2; [LT] standard E7 Weyl-vector norm.
    "E8": Fraction(620),  # VERIFIED: [DC] 248*30/12 = 620; [LT] standard E8 Weyl-vector norm.
}


class TestTypeAReduction:
    """Type A must reduce to the canonical existing engines."""

    @pytest.mark.parametrize("type_name,N", TYPE_A_TO_N.items())
    def test_type_a_central_charge_matches_canonical_engine(self, type_name, N):
        for k_value in TEST_K_VALUES:
            assert principal_w_central_charge(type_name, k_value) == c_wn_fl(N, k_value)

    @pytest.mark.parametrize("type_name,N", TYPE_A_TO_N.items())
    def test_type_a_conductor_matches_alpha_n(self, type_name, N):
        expected = alpha_N(N)
        assert expected_koszul_conductor(type_name) == expected
        for k_value in TEST_K_VALUES:
            assert koszul_conductor(type_name, k_value) == expected

    @pytest.mark.parametrize("type_name,N", TYPE_A_TO_N.items())
    def test_type_a_kappa_sum_matches_existing_engine(self, type_name, N):
        expected = K_WN(N)
        assert expected_kappa_complementarity(type_name) == expected
        for k_value in TEST_K_VALUES:
            assert kappa_complementarity(type_name, k_value) == expected

    @pytest.mark.parametrize("type_name", TYPE_A_TYPES)
    def test_type_a_generator_weights_are_consecutive(self, type_name):
        data = lie_data(type_name)
        assert generator_weights(type_name) == tuple(range(2, data.rank + 2))


class TestExceptionalExactValues:
    """Exact conductor and anomaly data for the exceptional families."""

    @pytest.mark.parametrize("type_name,expected", EXCEPTIONAL_CONDUCTOR_EXPECTED.items())
    def test_exceptional_conductors(self, type_name, expected):
        assert expected_koszul_conductor(type_name) == expected
        for k_value in TEST_K_VALUES:
            assert koszul_conductor(type_name, k_value) == expected

    @pytest.mark.parametrize("type_name,expected", EXCEPTIONAL_KAPPA_EXPECTED.items())
    def test_exceptional_kappa_complementarity(self, type_name, expected):
        assert expected_kappa_complementarity(type_name) == expected
        for k_value in TEST_K_VALUES:
            assert kappa_complementarity(type_name, k_value) == expected

    @pytest.mark.parametrize("type_name,expected", ANOMALY_RATIO_EXPECTED.items())
    def test_exceptional_anomaly_ratios(self, type_name, expected):
        assert anomaly_ratio(type_name) == expected

    @pytest.mark.parametrize("type_name", EXCEPTIONAL_TYPES)
    def test_exceptional_kappa_matches_varrho_times_c(self, type_name):
        varrho = anomaly_ratio(type_name)
        for k_value in TEST_K_VALUES:
            assert principal_w_kappa(type_name, k_value) == (
                varrho * principal_w_central_charge(type_name, k_value)
            )


class TestKIndependence:
    """Both complementarity sums must be level-independent."""

    @pytest.mark.parametrize("type_name", ALL_SUPPORTED_TYPES)
    def test_verify_k_independence(self, type_name):
        checks = verify_k_independence(type_name, TEST_K_VALUES)
        assert all(checks.values()), checks

    @pytest.mark.parametrize("type_name", ALL_SUPPORTED_TYPES)
    def test_dual_level_is_involution(self, type_name):
        for k_value in TEST_K_VALUES:
            assert dual_level(type_name, dual_level(type_name, k_value)) == k_value


class TestFreudenthalDeVries:
    """|rho|^2 = dim(g) * h_dual / 12 for all supported types."""

    @pytest.mark.parametrize("type_name,expected", RHO_SQUARED_EXPECTED.items())
    def test_rho_squared_values(self, type_name, expected):
        assert weyl_rho_squared(type_name) == expected


class TestExports:
    """Exported dictionaries should contain exact Fraction values."""

    def test_exported_conductors(self):
        exported = export_koszul_conductors()
        assert exported == dict(KOSZUL_CONDUCTORS)
        assert set(exported) == set(ALL_SUPPORTED_TYPES)
        assert all(isinstance(value, Fraction) for value in exported.values())

    def test_exported_kappa_complementarities(self):
        exported = export_kappa_complementarities()
        assert exported == dict(KAPPA_COMPLEMENTARITIES)
        assert set(exported) == set(ALL_SUPPORTED_TYPES)
        assert all(isinstance(value, Fraction) for value in exported.values())

    def test_verify_all(self):
        results = verify_all(k_values=TEST_K_VALUES)
        assert set(results) == set(ALL_SUPPORTED_TYPES)
        assert all(all(checks.values()) for checks in results.values())

