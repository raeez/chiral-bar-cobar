"""Faber-Pandharipande intersection numbers lambda_g^FP.

Computes the tautological integral

    lambda_g^FP = int_{M-bar_{g,1}} psi^{2g-2} lambda_g
               = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

for g = 1, ..., 10 using exact rational (Fraction) arithmetic.

Generating function: sum_{g>=1} lambda_g^FP x^{2g} = (x/2)/sin(x/2) - 1.

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Faber-Pandharipande, "Hodge integrals and moduli" (2000)
  - Mumford, "Towards an enumerative geometry of the moduli space of curves"
"""

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
from typing import Dict


# ---------------------------------------------------------------------------
# Bernoulli numbers (exact, recursive)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=64)
def bernoulli_exact(n: int) -> Fraction:
    r"""Exact Bernoulli number B_n as a Fraction.

    Uses the recursive definition:
      sum_{k=0}^{n} C(n+1, k) B_k = 0  for n >= 1, with B_0 = 1.

    Convention: B_1 = -1/2 (the "old" convention).
    """
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    s = Fraction(0)
    for k in range(n):
        bk = bernoulli_exact(k)
        if bk != 0:
            s += Fraction(comb(n + 1, k)) * bk
    return -s / Fraction(n + 1)


# ---------------------------------------------------------------------------
# lambda_g^FP
# ---------------------------------------------------------------------------

@lru_cache(maxsize=32)
def get_lambda_g_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

    Verified values (g=1..3):
      g=1: (2^1 - 1)|B_2| / (2^1 * 2!) = 1 * (1/6) / 2 = 1/12 ... no.
      g=1: (2^1 - 1)|B_2| / (2^1 * 2!) = 1*(1/6)/(2*2) = 1/24. Check: F_1 = kappa/24.
      g=2: (2^3 - 1)|B_4| / (2^3 * 4!) = 7*(1/30)/(8*24) = 7/5760.
      g=3: (2^5 - 1)|B_6| / (2^5 * 6!) = 31*(1/42)/(32*720) = 31/967680.
    """
    if g < 1:
        raise ValueError(f"lambda_g^FP requires g >= 1, got {g}")
    B_2g = bernoulli_exact(2 * g)
    abs_B_2g = abs(B_2g)
    numerator = (2 ** (2 * g - 1) - 1) * abs_B_2g
    denominator = Fraction(2 ** (2 * g - 1) * factorial(2 * g))
    return numerator / denominator


# ---------------------------------------------------------------------------
# Precomputed table for g = 1 .. 10
# ---------------------------------------------------------------------------

LAMBDA_G_FP: Dict[int, Fraction] = {}
for _g in range(1, 11):
    LAMBDA_G_FP[_g] = get_lambda_g_fp(_g)

# Sanity: g=1 must be 1/24 (F_1 = kappa/24 is the genus-1 partition function).
assert LAMBDA_G_FP[1] == Fraction(1, 24), f"g=1 failed: {LAMBDA_G_FP[1]}"

# ---------------------------------------------------------------------------
# Cross-check against stable_graph_enumeration
# ---------------------------------------------------------------------------

def cross_check_stable_graph_enumeration() -> bool:
    """Verify agreement with the independent implementation in stable_graph_enumeration.py.

    Returns True if all g=1..10 values match, raises AssertionError otherwise.
    """
    from compute.lib.stable_graph_enumeration import _lambda_fp_exact
    for g in range(1, 11):
        ours = LAMBDA_G_FP[g]
        theirs = _lambda_fp_exact(g)
        assert ours == theirs, (
            f"Mismatch at g={g}: engine={ours}, stable_graph={theirs}"
        )
    return True


# ---------------------------------------------------------------------------
# Generating function cross-check
# ---------------------------------------------------------------------------

def generating_function_check(x: float = 1.0, max_g: int = 10,
                              rtol: float = 1e-12) -> bool:
    """Verify sum_{g=1}^{max_g} lambda_g x^{2g} against (x/2)/sin(x/2) - 1.

    The generating function identity is:
      (x/2)/sin(x/2) - 1 = sum_{g>=1} lambda_g^FP x^{2g}

    Returns True if relative error < rtol.
    """
    import math
    exact = (x / 2) / math.sin(x / 2) - 1.0
    series = sum(float(LAMBDA_G_FP[g]) * x ** (2 * g) for g in range(1, max_g + 1))
    if exact == 0.0:
        return abs(series) < rtol
    rel_err = abs(exact - series) / abs(exact)
    return rel_err < rtol
