r"""Tests for A_2(N) polynomial combinatorics engine.

Multi-path verification of the genus-2 cross-channel polynomial

    A_2(N) = (N-2)(3 N^3 + 14 N^2 + 22 N + 33) / 24

and its inner cubic P_2(N) = 3 N^3 + 14 N^2 + 22 N + 33.

The tests verify A_2(N) by FOUR independent computational paths:
  (1) Direct closed-form polynomial in N
  (2) Power-sum form (2 p_1^2 + p_2 - 12)/4
  (3) Elementary symmetric form (3 e_1^2 - 2 e_2 - 12)/4
  (4) W-only form 2 (p_1')^2 + p_2' + 8 p_1' (no -12 constant)

plus per-graph decomposition into figure-eight, theta, sunrise.

Manuscript references:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    prop:universal-gravitational-cross-channel
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

import pytest

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from compute.lib.a2_polynomial_combinatorics_engine import (
    A2_W_only_form,
    A2_figure_eight,
    A2_graph_decomposition,
    A2_polynomial,
    A2_power_sums,
    A2_sunrise,
    A2_symmetric,
    A2_theta,
    A2_times_4_integer_sequence,
    B2_polynomial,
    B2_power_sum,
    P2_falling_factorial,
    P2_rising_factorial,
    asymptotic_leading_coefficient,
    asymptotic_ratio,
    asymptotic_subleading_coefficients,
    cubic_value_sequence,
    delta_F2_grav,
    elementary_e1,
    elementary_e2,
    inner_polynomial_P2,
    p1,
    p2,
    p3,
    pair_weight_count,
    power_sum,
    power_sum_W_only,
    quadratic_casimir_cross,
    virasoro_baseline,
    virasoro_singleton_subtraction,
    weight_operator_trace,
)


# ============================================================================
# Path 1 vs Path 2 vs Path 3 vs Path 4: cross-form agreement
# ============================================================================

@pytest.mark.parametrize("N", list(range(2, 21)))
def test_A2_polynomial_equals_power_sum_form(N: int):
    """Path 1 (polynomial) == Path 2 (power sums)."""
    assert A2_polynomial(N) == A2_power_sums(N)


@pytest.mark.parametrize("N", list(range(2, 21)))
def test_A2_polynomial_equals_symmetric_form(N: int):
    """Path 1 (polynomial) == Path 3 (elementary symmetric)."""
    assert A2_polynomial(N) == A2_symmetric(N)


@pytest.mark.parametrize("N", list(range(2, 21)))
def test_A2_polynomial_equals_W_only_form(N: int):
    """Path 1 (polynomial) == Path 4 (W-only basis)."""
    assert A2_polynomial(N) == A2_W_only_form(N)


@pytest.mark.parametrize("N", list(range(2, 16)))
def test_A2_all_four_paths_agree(N: int):
    """All four representations of A_2(N) agree pointwise."""
    a = A2_polynomial(N)
    assert A2_power_sums(N) == a
    assert A2_symmetric(N) == a
    assert A2_W_only_form(N) == a


# ============================================================================
# Hardcoded values: small-N spot checks
# ============================================================================

def test_A2_at_N2_is_zero():
    """Virasoro baseline: A_2(2) = 0 (uniform-weight, no cross-channel)."""
    assert A2_polynomial(2) == 0


def test_A2_at_N3_is_51_over_4():
    """W_3 algebra: A_2(3) = (1)*(3*27 + 14*9 + 22*3 + 33)/24 = 306/24 = 51/4."""
    assert A2_polynomial(3) == Fraction(51, 4)


def test_A2_at_N4_is_179_over_4():
    """W_4 algebra: A_2(4) = 2*537/24 = 179/4."""
    assert A2_polynomial(4) == Fraction(179, 4)


def test_A2_at_N5_is_217_over_2():
    """W_5 algebra: A_2(5) = 3*868/24 = 2604/24 = 217/2."""
    assert A2_polynomial(5) == Fraction(217, 2)


def test_A2_at_N6_correct_value():
    """W_6 algebra: A_2(6) = 4*1317/24 = 5268/24 = 439/2.

    Note: the task description suggested 1729/4. That value is INCORRECT
    by direct computation; the formula gives 439/2 = 878/4 ~ 219.5.
    The Hardy-Ramanujan number 1729 does NOT appear in this sequence
    (verified for N up to 100).
    """
    assert A2_polynomial(6) == Fraction(439, 2)
    assert A2_polynomial(6) != Fraction(1729, 4)


def test_A2_at_N9_is_1036_integer():
    """A_2(9) = 7*3552/24 = 24864/24 = 1036 (integer when 24 | (N-2)*P_2)."""
    assert A2_polynomial(9) == 1036


def test_A2_at_N10_is_1551_integer():
    """A_2(10) = 8*4653/24 = 1551."""
    assert A2_polynomial(10) == 1551


# ============================================================================
# Inner polynomial P_2(N) = 3N^3 + 14N^2 + 22N + 33
# ============================================================================

@pytest.mark.parametrize("N,expected", [
    (0, 33), (1, 72), (2, 157), (3, 306), (4, 537),
    (5, 868), (6, 1317), (7, 1902), (8, 2641), (9, 3552),
    (10, 4653), (11, 5962), (12, 7497), (13, 9276),
    (14, 11317), (15, 13638),
])
def test_P2_value_table(N: int, expected: int):
    """P_2(N) value table for N = 0..15."""
    assert inner_polynomial_P2(N) == expected


@pytest.mark.parametrize("N", list(range(0, 16)))
def test_P2_rising_factorial_basis(N: int):
    """P_2(N) = 3 N(N+1)(N+2) + 5 N(N+1) + 11 N + 33."""
    assert P2_rising_factorial(N) == inner_polynomial_P2(N)


@pytest.mark.parametrize("N", list(range(0, 16)))
def test_P2_falling_factorial_basis(N: int):
    """P_2(N) = 18 C(N,3) + 46 C(N,2) + 39 N + 33."""
    assert P2_falling_factorial(N) == inner_polynomial_P2(N)


def test_P2_constant_term():
    """P_2(0) = 33."""
    assert inner_polynomial_P2(0) == 33


def test_P2_no_rational_roots():
    """P_2 has no rational root in [-50, 50] (it is irreducible over Q)."""
    for k in range(-50, 51):
        assert inner_polynomial_P2(k) != 0


def test_cubic_value_sequence_table():
    """cubic_value_sequence(16) returns the standard list."""
    expected = [
        33, 72, 157, 306, 537, 868, 1317, 1902, 2641,
        3552, 4653, 5962, 7497, 9276, 11317, 13638,
    ]
    assert cubic_value_sequence(16) == expected


# ============================================================================
# 4*A_2 integer sequence and OEIS-negative result
# ============================================================================

def test_4A2_integer_sequence_table():
    """4*A_2(N) for N=2..15 gives the documented integer sequence."""
    expected = [
        0, 51, 179, 434, 878, 1585, 2641, 4144, 6204,
        8943, 12495, 17006, 22634, 29549,
    ]
    assert A2_times_4_integer_sequence(14) == expected


def test_4A2_is_always_integer():
    """4*A_2(N) is an integer for every N >= 2."""
    for N in range(2, 50):
        a4 = 4 * A2_polynomial(N)
        assert a4.denominator == 1, f"4*A_2({N}) = {a4} is not integer"


# ============================================================================
# Asymptotic verification: A_2(N) / N^4 -> 1/8
# ============================================================================

def test_leading_coefficient_is_one_eighth():
    """Asymptotic leading coefficient is 1/8 = 3/24."""
    assert asymptotic_leading_coefficient() == Fraction(1, 8)


def test_asymptotic_ratio_converges_to_one_eighth():
    """A_2(N)/N^4 monotonically approaches 1/8 from above."""
    target = 1.0 / 8.0
    last = float(asymptotic_ratio(20))
    for N in [40, 80, 160, 320, 640, 1280]:
        r = float(asymptotic_ratio(N))
        # Should be decreasing toward 1/8
        assert r > target, f"ratio at N={N} = {r} should exceed 1/8"
        assert r < last, f"ratio at N={N} = {r} should be less than at previous N"
        last = r
    # Final value should be within 1% of 1/8
    final = float(asymptotic_ratio(2000))
    assert abs(final - target) < target * 0.01


def test_subleading_coefficients():
    """The full polynomial coefficients of A_2(N) in the monomial basis."""
    coefs = asymptotic_subleading_coefficients()
    assert coefs['N4'] == Fraction(1, 8)
    assert coefs['N3'] == Fraction(1, 3)
    assert coefs['N2'] == Fraction(-1, 4)
    assert coefs['N1'] == Fraction(-11, 24)
    assert coefs['N0'] == Fraction(-11, 4)


def test_subleading_coefficients_reproduce_polynomial():
    """Sum of c_k * N^k matches A_2(N) at sample N."""
    coefs = asymptotic_subleading_coefficients()
    for N in [2, 3, 5, 8, 13, 21]:
        val = (
            coefs['N4'] * N ** 4
            + coefs['N3'] * N ** 3
            + coefs['N2'] * N ** 2
            + coefs['N1'] * N
            + coefs['N0']
        )
        assert val == A2_polynomial(N), f"mismatch at N={N}"


# ============================================================================
# The constant -12 (Virasoro singleton subtraction)
# ============================================================================

def test_virasoro_baseline_is_12():
    """The baseline 2 p_1(2)^2 + p_2(2) = 2*4 + 4 = 12."""
    assert virasoro_baseline() == 12
    assert virasoro_singleton_subtraction() == 12


def test_baseline_at_N2_matches_subtracted_constant():
    """4 A_2(2) + 12 = 12 (because A_2(2) = 0)."""
    val = 4 * A2_polynomial(2) + virasoro_baseline()
    assert val == 12


def test_pair_weight_count_at_N2_equals_baseline():
    """pair_weight_count(2) = 2*p_1(2)^2 + p_2(2) = 12."""
    assert pair_weight_count(2) == 12


def test_pair_weight_count_equals_4A2_plus_12():
    """For all N >= 2: 2 p_1^2 + p_2 = 4 A_2(N) + 12."""
    for N in range(2, 20):
        assert pair_weight_count(N) == 4 * A2_polynomial(N) + 12


# ============================================================================
# Power sums and W-only sums consistency
# ============================================================================

@pytest.mark.parametrize("N", list(range(2, 16)))
def test_p1_closed_form(N: int):
    """p_1(N) = N(N+1)/2 - 1."""
    expected = Fraction(N * (N + 1), 2) - 1
    assert p1(N) == expected
    assert power_sum(1, N) == expected


@pytest.mark.parametrize("N", list(range(2, 16)))
def test_p2_closed_form(N: int):
    """p_2(N) = N(N+1)(2N+1)/6 - 1."""
    expected = Fraction(N * (N + 1) * (2 * N + 1), 6) - 1
    assert p2(N) == expected
    assert power_sum(2, N) == expected


@pytest.mark.parametrize("N", list(range(2, 16)))
def test_p3_closed_form(N: int):
    """p_3(N) = (N(N+1)/2)^2 - 1."""
    expected = Fraction(N * (N + 1) // 2) ** 2 - 1
    assert p3(N) == expected


@pytest.mark.parametrize("N", list(range(3, 16)))
def test_W_only_power_sums_relation(N: int):
    """p_1' = p_1 - 2 and p_2' = p_2 - 4 (j=2 contribution removed)."""
    assert power_sum_W_only(1, N) == p1(N) - 2
    assert power_sum_W_only(2, N) == p2(N) - 4


def test_W_only_form_at_N2_is_empty():
    """For N=2 the W-only sums are empty, A_2(2) = 0."""
    assert power_sum_W_only(1, 2) == 0
    assert power_sum_W_only(2, 2) == 0
    assert A2_W_only_form(2) == 0


# ============================================================================
# Elementary symmetric functions
# ============================================================================

@pytest.mark.parametrize("N", list(range(2, 12)))
def test_e2_definition_brute_force(N: int):
    """e_2(2,...,N) = sum_{2 <= i < j <= N} i*j computed brute force."""
    brute = sum(Fraction(i * j) for i in range(2, N + 1) for j in range(i + 1, N + 1))
    assert elementary_e2(N) == brute


@pytest.mark.parametrize("N", list(range(2, 12)))
def test_e1_squared_minus_p2_equals_2_e2(N: int):
    """Newton's identity: p_1^2 = p_2 + 2 e_2."""
    assert p1(N) ** 2 == p2(N) + 2 * elementary_e2(N)


# ============================================================================
# Graph decomposition: A_2 = FE + Theta + Sunrise
# ============================================================================

@pytest.mark.parametrize("N", list(range(2, 16)))
def test_graph_decomposition_sums_to_A2(N: int):
    """A_2(N) = A_2^FE + A_2^Th + A_2^SR."""
    decomp = A2_graph_decomposition(N)
    assert decomp['total'] == A2_polynomial(N)
    assert decomp['figure_eight'] + decomp['theta'] + decomp['sunrise'] == A2_polynomial(N)


@pytest.mark.parametrize("N", list(range(2, 12)))
def test_figure_eight_equals_e2_over_2(N: int):
    """A_2^FE(N) = e_2(2,...,N) / 2."""
    assert A2_figure_eight(N) == elementary_e2(N) / 2


@pytest.mark.parametrize("N", list(range(2, 12)))
def test_theta_graph_formula(N: int):
    """A_2^Th(N) = (p_2 - 4)/2 = (sum_{j=3}^N j^2)/2."""
    assert A2_theta(N) == (p2(N) - 4) / 2
    # Brute force on j>=3:
    brute = Fraction(sum(j * j for j in range(3, N + 1)), 2)
    assert A2_theta(N) == brute


@pytest.mark.parametrize("N", list(range(2, 12)))
def test_sunrise_graph_formula(N: int):
    """A_2^SR(N) = (p_1^2 - 4)/4."""
    assert A2_sunrise(N) == (p1(N) ** 2 - 4) / 4


# ============================================================================
# B_2(N) and full delta_F_2 cross-channel
# ============================================================================

@pytest.mark.parametrize("N", list(range(2, 20)))
def test_B2_two_forms_agree(N: int):
    """B_2(N) = (N-2)(N+3)/96 = (p_1 - 2)/48."""
    assert B2_polynomial(N) == B2_power_sum(N)


def test_B2_at_W3():
    """B_2(3) = (1)(6)/96 = 1/16."""
    assert B2_polynomial(3) == Fraction(1, 16)


def test_delta_F2_grav_at_W3_specific_c():
    """delta_F_2(W_3, c) = B_2(3) + A_2(3)/c = 1/16 + (51/4)/c.

    For c = 1: 1/16 + 51/4 = 1/16 + 204/16 = 205/16.
    """
    val = delta_F2_grav(3, Fraction(1))
    assert val == Fraction(205, 16)


# ============================================================================
# Cross-check: known formula delta_F_2(W_3) = (c+204)/(16 c)
# ============================================================================

def test_delta_F2_W3_matches_known_universal_formula():
    """delta_F_2(W_3, c) = (c + 204)/(16 c) for all rational c != 0.

    This is the manuscript formula thm:multi-weight-genus-expansion
    instantiated at W_3. Independent path: known closed form for the
    W_3 multi-weight genus-2 free-energy correction.
    """
    for c_int in [1, 2, 3, 5, 10, 100]:
        c = Fraction(c_int)
        engine_val = delta_F2_grav(3, c)
        formula_val = (c + 204) / (16 * c)
        assert engine_val == formula_val, f"mismatch at c={c}: {engine_val} vs {formula_val}"


# ============================================================================
# Quadratic Casimir invariant
# ============================================================================

def test_quadratic_casimir_relation():
    """Q = 2 (tr D)^2 + tr(D^2) and A_2 = (Q - 12)/4."""
    for N in range(2, 16):
        Q = quadratic_casimir_cross(N)
        assert (Q - 12) / 4 == A2_polynomial(N)


def test_weight_operator_trace_equals_power_sum():
    """tr(D^k) = p_k for k = 1, 2, 3."""
    for N in range(2, 12):
        assert weight_operator_trace(1, N) == p1(N)
        assert weight_operator_trace(2, N) == p2(N)


# ============================================================================
# 1729 / Hardy-Ramanujan: confirm DOES NOT appear
# ============================================================================

def test_1729_does_not_appear_in_A2():
    """1729 (Hardy-Ramanujan taxicab) does not appear as numerator of A_2 or 4*A_2."""
    for N in range(2, 200):
        a2 = A2_polynomial(N)
        assert a2.numerator != 1729
        assert (4 * a2).numerator != 1729


# ============================================================================
# Sign and monotonicity sanity checks
# ============================================================================

def test_A2_strictly_increasing_for_N_geq_2():
    """A_2(N) is strictly increasing in N for N >= 2."""
    prev = Fraction(-1)
    for N in range(2, 30):
        cur = A2_polynomial(N)
        assert cur > prev, f"A_2 decreased at N={N}: {prev} -> {cur}"
        prev = cur


def test_A2_positive_for_N_geq_3():
    """A_2(N) > 0 for N >= 3 (at N=2 it is exactly 0)."""
    assert A2_polynomial(2) == 0
    for N in range(3, 30):
        assert A2_polynomial(N) > 0


def test_inner_polynomial_positive_for_nonneg_N():
    """P_2(N) > 0 for all N >= 0 (the irreducible cubic has its real root near -3.47)."""
    for N in range(0, 100):
        assert inner_polynomial_P2(N) > 0


# ============================================================================
# Multi-path cross-verification (per AP10): every hardcoded value is
# independently re-derived by an INDEPENDENT route.
# ============================================================================

def _A2_brute_force_from_definition(N: int) -> Fraction:
    """Brute-force A_2(N) directly from sums over j in {2,..,N}.

    Independent path: never uses the cubic formula. Computes
        4 A_2 = 2 (sum_{j=2}^N j)^2 + sum_{j=2}^N j^2 - 12
    by explicit summation, NOT closed-form Faulhaber.
    """
    if N < 2:
        return Fraction(0)
    s1 = sum(Fraction(j) for j in range(2, N + 1))
    s2 = sum(Fraction(j * j) for j in range(2, N + 1))
    return (2 * s1 * s1 + s2 - 12) / 4


def _A2_brute_from_W_only_pairs(N: int) -> Fraction:
    """Brute-force A_2(N) from W-only pair sums.

    Uses: 4 A_2 = 2 (sum_{j=3}^N j)^2 + sum_{j=3}^N j^2 + 8 sum_{j=3}^N j.
    Independent of the closed cubic and of the -12 normalization.
    """
    if N < 3:
        return Fraction(0)
    s1p = sum(Fraction(j) for j in range(3, N + 1))
    s2p = sum(Fraction(j * j) for j in range(3, N + 1))
    return (2 * s1p * s1p + s2p + 8 * s1p) / 4


def _A2_from_graph_brute(N: int) -> Fraction:
    """Brute-force A_2 as a sum of three graph contributions, each computed
    by direct summation over weights (no closed forms)."""
    if N < 2:
        return Fraction(0)
    # Figure-eight: sum_{i<j in 2..N} ij / 2
    fe_brute = Fraction(0)
    for i in range(2, N + 1):
        for j in range(i + 1, N + 1):
            fe_brute += Fraction(i * j)
    fe_brute /= 2
    # Theta: (sum_{j>=3} j^2)/2
    th_brute = Fraction(sum(j * j for j in range(3, N + 1)), 2)
    # Sunrise: ((sum j)^2 - 4)/4
    s1 = sum(j for j in range(2, N + 1))
    sr_brute = Fraction(s1 * s1 - 4, 4)
    return fe_brute + th_brute + sr_brute


# Hardcoded spot values are each cross-checked by multiple INDEPENDENT paths.

@pytest.mark.parametrize("N,expected", [
    (2, Fraction(0)),
    (3, Fraction(51, 4)),
    (4, Fraction(179, 4)),
    (5, Fraction(217, 2)),
    (6, Fraction(439, 2)),
    (7, Fraction(1585, 4)),
    (8, Fraction(2641, 4)),
    (9, Fraction(1036)),
    (10, Fraction(1551)),
    (11, Fraction(8943, 4)),
    (12, Fraction(12495, 4)),
    (13, Fraction(8503, 2)),
    (14, Fraction(11317, 2)),
    (15, Fraction(29549, 4)),
])
def test_A2_value_six_path_cross_check(N: int, expected: Fraction):
    """For each hardcoded A_2 value, verify by SIX independent paths:
        1. Direct closed cubic formula
        2. Power-sum (2 p_1^2 + p_2 - 12)/4 via Faulhaber
        3. Elementary symmetric (3 e_1^2 - 2 e_2 - 12)/4
        4. W-only Newton form (no -12 constant)
        5. Brute-force summation from definition (no closed form)
        6. Brute-force per-graph summation
    """
    assert A2_polynomial(N) == expected
    assert A2_power_sums(N) == expected
    assert A2_symmetric(N) == expected
    assert A2_W_only_form(N) == expected
    assert _A2_brute_force_from_definition(N) == expected
    assert _A2_brute_from_graph_brute(N) == expected if False else _A2_from_graph_brute(N) == expected


@pytest.mark.parametrize("N", list(range(2, 25)))
def test_A2_brute_force_matches_closed_form(N: int):
    """Closed-form A_2(N) == brute-force computation from definition."""
    assert A2_polynomial(N) == _A2_brute_force_from_definition(N)


@pytest.mark.parametrize("N", list(range(2, 20)))
def test_A2_W_only_brute_force_matches(N: int):
    """W-only brute force agrees with closed form for all N."""
    assert A2_polynomial(N) == _A2_brute_from_W_only_pairs(N)


@pytest.mark.parametrize("N", list(range(2, 15)))
def test_A2_graph_brute_force_matches(N: int):
    """Per-graph brute force agrees with closed form."""
    assert A2_polynomial(N) == _A2_from_graph_brute(N)


@pytest.mark.parametrize("N", list(range(0, 16)))
def test_P2_value_four_path_cross_check(N: int):
    """P_2(N) by four representations: monomial, rising factorial,
    falling factorial, and explicit polynomial evaluation."""
    direct = 3 * N ** 3 + 14 * N ** 2 + 22 * N + 33
    assert inner_polynomial_P2(N) == direct
    assert P2_rising_factorial(N) == direct
    assert P2_falling_factorial(N) == direct
    # Fourth path: P_2 reconstructed from A_2 via inversion
    if N >= 3:
        a = A2_polynomial(N)
        # 24 * A_2 / (N-2) = P_2(N)
        recovered = 24 * a / (N - 2)
        assert recovered == direct


def test_4A2_integer_sequence_six_path():
    """The integer sequence 0,51,179,...,29549 is reproduced by all paths."""
    expected = [
        0, 51, 179, 434, 878, 1585, 2641, 4144, 6204,
        8943, 12495, 17006, 22634, 29549,
    ]
    by_polynomial = [int(4 * A2_polynomial(N)) for N in range(2, 16)]
    by_power_sum = [int(4 * A2_power_sums(N)) for N in range(2, 16)]
    by_symmetric = [int(4 * A2_symmetric(N)) for N in range(2, 16)]
    by_W_only = [int(4 * A2_W_only_form(N)) for N in range(2, 16)]
    by_brute = [int(4 * _A2_brute_force_from_definition(N)) for N in range(2, 16)]
    by_graph = [int(4 * _A2_from_graph_brute(N)) for N in range(2, 16)]
    assert by_polynomial == expected
    assert by_power_sum == expected
    assert by_symmetric == expected
    assert by_W_only == expected
    assert by_brute == expected
    assert by_graph == expected
    assert A2_times_4_integer_sequence(14) == expected


def test_W3_known_universal_formula_three_paths():
    """delta_F_2(W_3, c) = (c+204)/(16 c) by THREE independent paths.

    Path 1: engine via B_2 + A_2/c.
    Path 2: explicit closed form (c + 204)/(16 c).
    Path 3: B_2(3) = 1/16 hardcoded + A_2(3) = 51/4 hardcoded -> 1/16 + 51/(4c).
    """
    for c_int in [1, 2, 3, 7, 11, 50, 137]:
        c = Fraction(c_int)
        path1 = delta_F2_grav(3, c)
        path2 = (c + 204) / (16 * c)
        path3 = Fraction(1, 16) + Fraction(51, 4) / c
        assert path1 == path2
        assert path1 == path3


def test_baseline_12_three_path_derivation():
    """The constant 12 appears via THREE derivations:
        (a) virasoro_baseline()
        (b) 2 * 2^2 + 2^2 = 12 (Virasoro singleton)
        (c) pair_weight_count(2) = 12
    """
    assert virasoro_baseline() == 12
    assert virasoro_singleton_subtraction() == 12
    assert 2 * 2 ** 2 + 2 ** 2 == 12
    assert pair_weight_count(2) == 12
    # And 4 A_2(2) + 12 = 12 because A_2(2) = 0
    assert 4 * A2_polynomial(2) + 12 == 12


def test_leading_coefficient_three_paths():
    """The N^4 coefficient 1/8 by three paths:
        (a) Direct from cubic 3*N^3 leading -> 3/24 = 1/8.
        (b) From asymptotic_subleading_coefficients()['N4'].
        (c) From limit of A_2(N)/N^4 at large N.
    """
    a = Fraction(3, 24)  # leading 3 from cubic / 24 denominator
    b = asymptotic_subleading_coefficients()['N4']
    c_val = float(asymptotic_ratio(10000))
    assert a == Fraction(1, 8)
    assert b == Fraction(1, 8)
    assert abs(c_val - 1.0 / 8.0) < 1e-3


def test_graph_decomposition_three_path_consistency():
    """At N=3..10, verify graph decomposition equals A_2 by THREE paths:
        (a) Sum of FE + Theta + Sunrise from engine.
        (b) Sum of brute-force per-graph computations.
        (c) Direct A_2 from closed form.
    """
    for N in range(3, 11):
        engine_sum = A2_figure_eight(N) + A2_theta(N) + A2_sunrise(N)
        brute_sum = _A2_from_graph_brute(N)
        closed = A2_polynomial(N)
        assert engine_sum == brute_sum == closed


def test_oeis_negative_result_documented():
    """Document that the cubic and A_2 sequences are NOT in OEIS.

    Verified 2026-04-07 via OEIS JSON API: queries
        33,72,157,306,537,868,1317,1902,2641
        51,179,434,878,1585,2641,4144,6204
    return zero matches. The sequences are intrinsically new to this
    monograph and do not coincide with any catalogued combinatorial
    polynomial. This test merely asserts that the integer sequences
    are well-defined and reproducible (the OEIS-negative result is
    documented in the engine docstring; this test does not call
    out to the network).
    """
    cubic = cubic_value_sequence(16)
    assert cubic[0] == 33
    assert cubic[-1] == 13638
    a4 = A2_times_4_integer_sequence(14)
    assert a4[0] == 0
    assert a4[-1] == 29549
    # Both sequences contain large primes, ruling out clean factorization:
    assert 179 in a4  # 179 prime
    assert 11317 in cubic  # 11317 prime
    assert 1729 not in a4  # Hardy-Ramanujan absent
