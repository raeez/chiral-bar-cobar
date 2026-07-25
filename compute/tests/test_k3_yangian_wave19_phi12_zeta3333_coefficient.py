"""Independent tests for the repeated weight-twelve MZV scalar."""

from fractions import Fraction
from itertools import permutations
from math import factorial

import mpmath as mp
import pytest

from compute.lib.k3_yangian_wave19_phi12_zeta3333_coefficient import (
    run_tests,
    weight12_scalar_status,
    zeta3333_exact_polynomial,
    zeta3333_finite_elementary_sum,
    zeta3333_newton_numeric,
    zeta3333_normalized_scalar,
    zeta3333_tail_corrected_sum,
)


def _cycle_lengths(permutation):
    seen = set()
    lengths = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = permutation[current]
            length += 1
        lengths.append(length)
    return lengths


def _permutation_oracle():
    result = {}
    for permutation in permutations(range(4)):
        cycles = _cycle_lengths(permutation)
        sign = -1 if (4 - len(cycles)) % 2 else 1
        monomial = tuple(sorted(3 * length for length in cycles))
        result[monomial] = result.get(monomial, Fraction(0)) + Fraction(
            sign, factorial(4)
        )
    return {monomial: coefficient
            for monomial, coefficient in result.items() if coefficient}


def test_newton_identity_by_permutation_oracle():
    assert zeta3333_exact_polynomial() == _permutation_oracle()


def test_literal_newton_coefficients():
    assert zeta3333_exact_polynomial() == {
        (3, 3, 3, 3): Fraction(1, 24),
        (3, 3, 6): Fraction(-1, 4),
        (6, 6): Fraction(1, 8),
        (3, 9): Fraction(1, 3),
        (12,): Fraction(-1, 4),
    }


def test_numerical_value_from_depth_one_zeta_values():
    with mp.workdps(60):
        value = zeta3333_newton_numeric(60)
        expected = mp.mpf(
            "0.000295999014043171835500960819133545583238160712113039954782"
        )
        assert abs(value - expected) < mp.mpf("1e-59")


@pytest.mark.parametrize("cutoff,tolerance", [(10_000, "5e-17"), (50_000, "1e-19")])
def test_finite_elementary_sum_is_independent_numerical_route(cutoff, tolerance):
    with mp.workdps(50):
        finite = zeta3333_tail_corrected_sum(cutoff, 50)
        exact = zeta3333_newton_numeric(50)
        assert abs(finite - exact) < mp.mpf(tolerance)


def test_uncorrected_finite_sum_increases_toward_the_limit():
    with mp.workdps(40):
        short = zeta3333_finite_elementary_sum(2_000, 40)
        long = zeta3333_finite_elementary_sum(10_000, 40)
        exact = zeta3333_newton_numeric(40)
        assert short < long < exact


def test_factorial_normalisation_remains_a_scalar():
    with mp.workdps(50):
        assert zeta3333_normalized_scalar(50) == (
            zeta3333_newton_numeric(50) / factorial(12)
        )
    status = weight12_scalar_status()
    assert status["simplex_denominator"] == factorial(12)
    assert status["normalized_scalar_defined"]
    assert status["normalized_scalar_is_pentagon_coefficient"] is False


def test_primitive_and_chain_status():
    status = weight12_scalar_status()
    assert status["decomposable"]
    assert status["primitive_projection"] == 0
    assert status["graph_complex_class_constructed"] is False
    assert status["word_to_cochain_map_constructed"] is False
    assert status["cyclic_cochain_constructed"] is False
    assert status["genus_comparison_constructed"] is False


def test_validation_and_internal_checks():
    with pytest.raises(ValueError):
        zeta3333_finite_elementary_sum(3)
    checks = run_tests()
    assert checks
    assert all(checks.values())
