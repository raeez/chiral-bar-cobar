"""
Bernoulli numbers and Faber-Pandharipande lambda_g: exact Fraction arithmetic.

Computes B_0 through B_20 via the standard recursion and cross-checks against
the Faber-Pandharipande formula lambda_g = (-1)^{g-1} * B_{2g} / (2 * (2g)!).

All arithmetic uses fractions.Fraction -- no floating point anywhere.
"""

from fractions import Fraction
from math import factorial


def bernoulli_exact(n_max: int = 20) -> dict[int, Fraction]:
    """
    Compute Bernoulli numbers B_0, B_1, ..., B_{n_max} using the recursion

        sum_{k=0}^{m} C(m+1, k) B_k = 0   for m >= 1

    which gives B_m = -1/(m+1) * sum_{k=0}^{m-1} C(m+1,k) B_k.

    Returns a dict mapping n -> B_n as exact Fractions.
    """
    B: dict[int, Fraction] = {}
    B[0] = Fraction(1)

    for m in range(1, n_max + 1):
        s = Fraction(0)
        for k in range(m):
            # C(m+1, k) as exact integer
            binom = Fraction(factorial(m + 1), factorial(k) * factorial(m + 1 - k))
            s += binom * B[k]
        B[m] = -s / Fraction(m + 1)

    return B


def lambda_g_exact(g: int, bernoulli_table: dict[int, Fraction] | None = None) -> Fraction:
    """
    Faber-Pandharipande formula:

        lambda_g = (-1)^{g-1} * B_{2g} / (2 * (2g)!)

    Returns exact Fraction for g >= 1.
    """
    if bernoulli_table is None:
        bernoulli_table = bernoulli_exact(2 * g)
    b2g = bernoulli_table[2 * g]
    sign = Fraction((-1) ** (g - 1))
    return sign * b2g / Fraction(2 * factorial(2 * g))


# ---------------------------------------------------------------------------
# Precomputed tables (exact)
# ---------------------------------------------------------------------------

BERNOULLI_TABLE = bernoulli_exact(20)

LAMBDA_G_TABLE = {g: lambda_g_exact(g, BERNOULLI_TABLE) for g in range(1, 11)}


# ---------------------------------------------------------------------------
# Canonical Bernoulli values for external cross-check
# ---------------------------------------------------------------------------

CANONICAL_BERNOULLI = {
    0: Fraction(1),
    1: Fraction(-1, 2),
    2: Fraction(1, 6),
    3: Fraction(0),
    4: Fraction(-1, 30),
    5: Fraction(0),
    6: Fraction(1, 42),
    7: Fraction(0),
    8: Fraction(-1, 30),
    9: Fraction(0),
    10: Fraction(5, 66),
    11: Fraction(0),
    12: Fraction(-691, 2730),
    13: Fraction(0),
    14: Fraction(7, 6),
    15: Fraction(0),
    16: Fraction(-3617, 510),
    17: Fraction(0),
    18: Fraction(43867, 798),
    19: Fraction(0),
    20: Fraction(-174611, 330),
}
