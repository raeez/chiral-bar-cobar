r"""Tests for the pentagonal-rigidity theorem and the Motzkin/Riordan falsification.

Two circulating formulas assert bar cohomology dimensions:

    C-004   dim H^n(Bar(Vir_c))  = M(n+1) - M(n) = 1, 2, 5, 12, 30, 76, ...
    C-014   dim H^n(Bar(sl2_k))  = R(n+3)        = 3, 6, 15, 36, 91, ...

with the coincidence of the discriminant sqrt(1 - 2z - 3z^2) in the two
generating functions attributed to Drinfeld-Sokolov reduction.

Five independent paths:

  P1  reproduce both sequences from their combinatorial definitions, and check
      the four-term recurrence quoted alongside C-004
  P2  M(n) = R(n) + R(n+1) and M(n+1) - M(n) = R(n+2) - R(n), so the two
      sequences are elementary transforms of ONE sequence and the shared
      discriminant is forced independently of Drinfeld-Sokolov
  P3  H^*(sl_2; k) has Betti numbers 1, 0, 0, 1 (Whitehead), recomputed by
      exact rational elimination with d^2 = 0 asserted
  P4  dim H^n(L_1) = 2 for n = 1, 2, 3, 4, in the pentagonal weights
      (3n^2 -+ n)/2 (Goncharova 1973)
  P5  the graded Euler character prod_{n>=1}(1 - q^n) is supported exactly on
      the pentagonal numbers with sign (-1)^n, saturating P4 degree by degree,
      and the bar chain-space counts are 3^r rather than 3, 6, 15, 36, 91

Conclusion: neither formula is the bar cohomology of the algebra it names, and
neither is a bar chain count.  The honest closed-form invariant is the Euler
supercharacter, which is a Weyl-Kac-Borcherds denominator product.
"""

from __future__ import annotations

import pytest

from compute.lib.witt_pentagonal_rigidity import (
    euler_function_coefficients,
    motzkin,
    pentagonal_numbers,
    riordan,
    sl2,
    witt_positive,
)

CLAIM_VIRASORO = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]   # C-004, n = 1..10
CLAIM_SL2 = [3, 6, 15, 36, 91, 232, 603, 1585]                  # C-014, n = 1..8

NMAX = 24


# ----------------------------------------------------------------- P1
def test_P1_motzkin_differences_reproduce_C004():
    M = motzkin(NMAX)
    assert [M[n + 1] - M[n] for n in range(1, 11)] == CLAIM_VIRASORO


def test_P1_riordan_shift_reproduces_C014():
    R = riordan(NMAX)
    assert [R[n + 3] for n in range(1, 9)] == CLAIM_SL2


def test_P1_C004_quoted_recurrence_holds():
    """(n+3)a(n) - (3n+4)a(n-1) - (n+1)a(n-2) + 3(n-2)a(n-3) = 0."""
    M = motzkin(NMAX)
    a = {n: M[n + 1] - M[n] for n in range(1, NMAX)}
    for n in range(4, NMAX - 1):
        assert (n + 3) * a[n] - (3 * n + 4) * a[n - 1] \
               - (n + 1) * a[n - 2] + 3 * (n - 2) * a[n - 3] == 0


# ----------------------------------------------------------------- P2
def test_P2_motzkin_is_sum_of_consecutive_riordan():
    M, R = motzkin(NMAX), riordan(NMAX)
    for n in range(NMAX):
        assert M[n] == R[n] + R[n + 1]


def test_P2_virasoro_sequence_is_a_riordan_difference():
    """The two 'independent' sequences are R(n+2)-R(n) and R(n+3)."""
    M, R = motzkin(NMAX), riordan(NMAX)
    for n in range(NMAX - 2):
        assert M[n + 1] - M[n] == R[n + 2] - R[n]


# ----------------------------------------------------------------- P3
def test_P3_sl2_betti_numbers_are_whitehead():
    g = sl2()
    betti = [g.cohomology(n, 0)[0] for n in range(4)]
    chains = [g.cohomology(n, 0)[1] for n in range(4)]
    assert chains == [1, 3, 3, 1]
    assert betti == [1, 0, 0, 1], "H^*(sl_2) = Lambda(c_3)"


def test_P3_C014_is_not_sl2_cohomology():
    g = sl2()
    betti = [g.cohomology(n, 0)[0] for n in range(1, 4)]
    assert betti != CLAIM_SL2[:3]
    assert betti == [0, 0, 1]


# ----------------------------------------------------------------- P4
@pytest.mark.parametrize("n", [1, 2, 3])
def test_P4_goncharova_two_dimensional_in_pentagonal_weights(n: int):
    lo, hi = (3 * n * n - n) // 2, (3 * n * n + n) // 2
    g = witt_positive(hi + 2)
    found = []
    for w in range(n * (n + 1) // 2, hi + 2):
        h, _ = g.cohomology(n, w)
        if h:
            found.append((w, h))
    assert found == [(lo, 1), (hi, 1)], f"Goncharova: 2 classes at {(lo, hi)}"


@pytest.mark.slow
def test_P4_goncharova_degree_four():
    n = 4
    lo, hi = (3 * n * n - n) // 2, (3 * n * n + n) // 2   # 22, 26
    g = witt_positive(hi + 1)
    found = []
    for w in range(n * (n + 1) // 2, hi + 2):
        h, _ = g.cohomology(n, w)
        if h:
            found.append((w, h))
    assert found == [(22, 1), (26, 1)]


def test_P4_C004_is_not_witt_cohomology():
    """dim H^n(L_1) = 2 for every n >= 1, not 1, 2, 5, 12, 30, ...

    C-004 records "verified_against: Master Table degrees 1-5".  The truth on
    degrees 1..5 is the constant 2, while C-004 asserts 1, 2, 5, 12, 30.  The
    two agree at n = 2 and nowhere else, which is how a formula checked at a
    single low degree can survive.
    """
    truth, claimed = [], []
    for n in (1, 2, 3):
        hi = (3 * n * n + n) // 2
        g = witt_positive(hi + 2)
        total = sum(g.cohomology(n, w)[0]
                    for w in range(n * (n + 1) // 2, hi + 2))
        truth.append(total)
        claimed.append(CLAIM_VIRASORO[n - 1])

    assert truth == [2, 2, 2], "Goncharova: constant 2 in every positive degree"
    assert claimed == [1, 2, 5]
    agree = [n for n, (t, c) in enumerate(zip(truth, claimed), start=1) if t == c]
    assert agree == [2], "C-004 coincides with the truth at n = 2 alone"


# ----------------------------------------------------------------- P5
def test_P5_euler_character_is_supported_on_pentagonal_numbers():
    N = 30
    coeffs = euler_function_coefficients(N)
    support = [k for k, c in enumerate(coeffs) if c != 0]
    assert support == pentagonal_numbers(N)


def test_P5_euler_character_signs_saturate_goncharova():
    """Coefficient at (3n^2 -+ n)/2 is (-1)^n, one class per weight."""
    N = 30
    coeffs = euler_function_coefficients(N)
    for n in range(1, 5):
        for w in ((3 * n * n - n) // 2, (3 * n * n + n) // 2):
            if w <= N:
                assert coeffs[w] == (-1) ** n


def test_P5_bar_chain_counts_are_powers_not_riordan():
    """For dim(A-bar) = d the length-r ordered bar term has dimension d^r."""
    d = 3
    assert [d ** r for r in range(1, 6)] == [3, 9, 27, 81, 243]
    assert [d ** r for r in range(1, 6)] != CLAIM_SL2[:5]


# ----------------------------------------------------------------- self-test
def test_differential_squares_to_zero_witt():
    g = witt_positive(14)
    for n in range(0, 4):
        for w in range(0, 15):
            g.check_d_squared(n, w)


def test_differential_squares_to_zero_sl2():
    g = sl2()
    for n in range(0, 4):
        g.check_d_squared(n, 0)
