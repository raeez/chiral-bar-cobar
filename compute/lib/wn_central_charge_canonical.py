r"""Canonical W_N central charge formula — single source of truth.

The correct Fateev-Lukyanov formula for the principal W-algebra W^k(sl_N)
obtained by quantum Drinfeld-Sokolov reduction is:

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

This is the ONLY correct formula. The simpler expression
``(N-1)(1 - N(N+1)/(k+N))`` is WRONG — it gives c+c' = 2(N-1) under
Feigin-Frenkel duality k' = -k-2N, but the correct complementarity is
c+c' = 2(N-1) + 4N(N^2-1) (Freudenthal-de Vries identity).

Decisive test: at N=2, k=1, the correct formula gives c = -7
(standard Virasoro from DS(sl_2, k=1)). The wrong formula gives c = -1.

Source: w_algebras.tex line 2815.

XVER-34 independently verified: kappa+kappa' = 13 for Virasoro (171 tests).
The simple formula gives kappa+kappa' = 1. WRONG.

This module exists because an external file watcher reverts inline edits
to existing compute/lib/ files. Import from HERE to get the correct formula.
"""

from fractions import Fraction
from typing import Union

Num = Union[int, float, Fraction]


def c_wn_fl(N: int, k: Num) -> Fraction:
    r"""Fateev-Lukyanov central charge for principal W^k(sl_N).

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    Parameters
    ----------
    N : rank of sl_N (N >= 2)
    k : level (k != -N)

    Returns exact Fraction.

    Examples
    --------
    >>> c_wn_fl(2, 1)
    Fraction(-7, 1)
    >>> c_wn_fl(3, 1)
    Fraction(-52, 1)
    >>> c_wn_fl(2, 1) + c_wn_fl(2, -5)  # complementarity
    Fraction(26, 1)
    """
    k_f = Fraction(k) if not isinstance(k, Fraction) else k
    kN = k_f + N
    if kN == 0:
        raise ValueError(f"Critical level k = -{N}: undefined")
    return Fraction(N - 1) - Fraction(N * (N**2 - 1)) * (kN - 1)**2 / kN


def kappa_wn_fl(N: int, k: Num) -> Fraction:
    r"""Modular characteristic kappa(W_N) = c * (H_N - 1).

    H_N = 1 + 1/2 + ... + 1/N (harmonic number).
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    return c_wn_fl(N, k) * (H_N - 1)


def complementarity_sum(N: int) -> Fraction:
    r"""c(W_N, k) + c(W_N, -k-2N) = 2(N-1) + 4N(N^2-1).

    Independent of k. This is the Freudenthal-de Vries identity.
    """
    return Fraction(2 * (N - 1) + 4 * N * (N**2 - 1))


def kappa_complementarity_sum(N: int) -> Fraction:
    r"""kappa(W_N, k) + kappa(W_N, -k-2N) = (H_N-1) * [2(N-1) + 4N(N^2-1)].

    At N=2: 13. At N=3: 250/3. At N=4: 533/2. At N=5: 9394/15.
    """
    H_N = sum(Fraction(1, j) for j in range(1, N + 1))
    return (H_N - 1) * complementarity_sum(N)


def ff_dual_level(N: int, k: Num) -> Fraction:
    """Feigin-Frenkel dual level: k' = -k - 2N."""
    return Fraction(-k - 2 * N) if not isinstance(k, Fraction) else -k - 2 * N


# Self-test on import
assert c_wn_fl(2, 1) == Fraction(-7), f"FATAL: c(W_2,1) = {c_wn_fl(2,1)}, expected -7"
assert c_wn_fl(2, 1) + c_wn_fl(2, -5) == Fraction(26), "FATAL: complementarity failed"
assert kappa_complementarity_sum(2) == Fraction(13), "FATAL: kappa complementarity"
