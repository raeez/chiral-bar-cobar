"""Exact W3 OPE and generic-vacuum checks with a loud bar boundary."""

import pytest
import sympy as sp

from compute.lib.w3_bar import (
    OpenW3BarError,
    verify_skew_symmetry,
    verify_w3_ope,
    w3_arnold_cancellation_deg3,
    w3_bar_diff_deg2,
    w3_central_charge,
    w3_complementarity_sum,
    w3_curvature,
    w3_deg3_cohomology,
    w3_leading_norm_ratio,
    w3_leading_ope_norms,
    w3_nth_product,
    w3_nth_products,
    w3_ope_status_packet,
    w3_reflected_central_sum,
    w3_vacuum_basis,
    w3_vacuum_dim,
)


def test_exact_tt_tw_wt_products():
    c = sp.Symbol("c")
    products = w3_nth_products()
    assert products[("T", "T")][3] == {"vac": c / 2}
    assert products[("T", "T")][1] == {"T": 2}
    assert products[("T", "W")][1] == {"W": 3}
    assert products[("T", "W")][0] == {"dW": 1}
    assert products[("W", "T")][0] == {"dW": 2}
    assert verify_skew_symmetry()


def test_exact_ww_32_16_normalization():
    c = sp.Symbol("c")
    ww = w3_nth_products()[("W", "W")]
    assert ww[5] == {"vac": c / 3}
    assert ww[3] == {"T": 2}
    assert ww[2] == {"dT": 1}
    assert ww[1]["d2T"] == sp.Rational(3, 10)
    assert sp.simplify(ww[1]["Lambda"] - 32 / (22 + 5 * c)) == 0
    assert ww[0]["d3T"] == sp.Rational(1, 15)
    assert sp.simplify(ww[0]["dLambda"] - 16 / (22 + 5 * c)) == 0
    assert w3_nth_product("W", "W", 4) == {}


def test_ope_verification_and_status_packet():
    assert all(verify_w3_ope().values())
    packet = w3_ope_status_packet()
    assert packet["ordered_bar"].status == "open"
    assert packet["scalar_shadow"].status == "open"


def test_leading_norms_are_ope_data():
    c = sp.Symbol("c")
    assert w3_leading_ope_norms() == {"T": c / 2, "W": c / 3}
    assert w3_leading_norm_ratio() == sp.Rational(2, 3)


def test_principal_central_charge_and_formal_reflection():
    k = sp.Symbol("k")
    expected = 2 - 24 * (k + 2) ** 2 / (k + 3)
    assert sp.factor(w3_central_charge(k) - expected) == 0
    assert w3_reflected_central_sum(k) == 100
    assert w3_complementarity_sum() == 100


def test_generic_vacuum_basis_matches_product_character():
    basis = w3_vacuum_basis(10)
    for weight in range(1, 11):
        assert len(basis.get(weight, [])) == w3_vacuum_dim(weight)
    assert w3_vacuum_dim(2) == 1
    assert w3_vacuum_dim(3) == 2
    assert w3_vacuum_dim(4) == 3


@pytest.mark.parametrize(
    "operation",
    [
        lambda: w3_bar_diff_deg2("T", "T"),
        lambda: w3_curvature(),
        lambda: w3_arnold_cancellation_deg3(),
        lambda: w3_deg3_cohomology(6),
    ],
)
def test_historical_bar_promotions_require_geometric_residue_model(operation):
    with pytest.raises(OpenW3BarError, match=r"H_W3\^bar"):
        operation()
