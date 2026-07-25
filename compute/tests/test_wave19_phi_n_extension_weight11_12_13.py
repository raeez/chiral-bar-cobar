"""Tests for the motivic arithmetic at weights 11, 12, and 13."""

from math import factorial

import pytest

from compute.lib.wave19_phi_n_extension_weight11_12_13 import (
    motivic_dimension_table,
    run_tests,
    weight_extension_status,
    weight_order_status,
)


def _independent_count(weight):
    if weight < 0:
        return 0
    if weight == 0:
        return 1
    return _independent_count(weight - 2) + _independent_count(weight - 3)


@pytest.mark.parametrize(
    "weight,expected",
    [(3, 1), (4, 1), (5, 2), (6, 2), (7, 3), (8, 4),
     (9, 5), (10, 7), (11, 9), (12, 12), (13, 16)],
)
def test_dimensions(weight, expected):
    assert motivic_dimension_table(weight, weight)[weight] == expected
    assert expected == _independent_count(weight)


def test_weight_words_have_exact_weight():
    statuses = weight_extension_status()
    for weight, status in statuses.items():
        assert len(status["hoffman_words"]) == status["motivic_dimension"]
        assert all(sum(word) == weight for word in status["hoffman_words"])
        assert all(set(word) <= {2, 3} for word in status["hoffman_words"])


@pytest.mark.parametrize("weight", [11, 12, 13])
def test_simplex_volume_is_only_the_constant_integrand_normalisation(weight):
    status = weight_order_status(weight)
    assert status["simplex_denominator"] == factorial(weight)
    kz = status["kz_normalization"]
    assert kz["constant_integrand_simplex_denominator"] == factorial(weight)
    assert kz["word_specified"] is False
    assert kz["regularised_word_integral_computed"] is False


def test_weight_twelve_repeated_period_is_decomposable():
    status = weight_order_status(12)["zeta3333"]
    assert status["decomposable"]
    assert status["primitive_projection"] == 0
    assert status["first_depth_four_primitive"] is False
    assert status["graph_complex_class_constructed"] is False
    assert status["grt_action_computed"] is False


@pytest.mark.parametrize("weight", [11, 12, 13])
def test_cyclic_operations_remain_open(weight):
    status = weight_order_status(weight)
    assert status["associator_chosen"] is False
    assert status["represented_kz_word_constructed"] is False
    assert status["word_to_cochain_map_constructed"] is False
    assert status["cyclic_cochain_constructed"] is False
    assert status["rotation_equation_verified"] is False
    assert status["maurer_cartan_equation_verified"] is False
    assert status["phi_n_constructed"] is False


def test_validation_and_internal_checks():
    with pytest.raises(ValueError):
        motivic_dimension_table(-1, 3)
    with pytest.raises(ValueError):
        motivic_dimension_table(4, 3)
    checks = run_tests()
    assert checks
    assert all(checks.values())
