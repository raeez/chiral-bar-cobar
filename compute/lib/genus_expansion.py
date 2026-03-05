"""Genus expansion via the universal formula.

For any Koszul chiral algebra A with obstruction coefficient kappa(A):

  F_g(A) = kappa(A) * lambda_g^FP

where lambda_g^FP = |B_{2g}| / (2g * (2g-2)!) are Faber-Pandharipande numbers.

The universal generating function (thm:universal-generating-function):
  sum_{g>=1} F_g(A) x^{2g} = kappa * ((x/2)/sin(x/2) - 1)

Radius of convergence: |x| = 2*pi (independent of A).

Complementarity (thm:quantum-complementarity-main):
  kappa(A) + kappa(A!) = sigma * (c + c')
  (depends only on root datum, not on level)

All arithmetic is exact (sympy.Rational). Never floating point.
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi, sin,
    series, simplify, Abs,
)

from .utils import lambda_fp, F_g
from .lie_algebra import (
    cartan_data, sugawara_c, ff_dual_level, kappa_km,
    sigma_invariant, virasoro_ds_c, w3_ds_c,
)


# ---------------------------------------------------------------------------
# Known kappa values (ground truth from Master Table / genus_expansions.tex)
# ---------------------------------------------------------------------------

def kappa_heisenberg(kappa_param=None):
    """kappa(H_kappa) = kappa (the level IS the obstruction coefficient)."""
    if kappa_param is None:
        return Symbol("kappa")
    return Rational(kappa_param)


def kappa_virasoro(c=None):
    """kappa(Vir_c) = c/2."""
    if c is None:
        return Symbol("c") / 2
    return Rational(c) / 2


def kappa_w3(c=None):
    """kappa(W_3^k) = 5c/6.

    Derived from sigma(sl_3) = 1/2 + 1/3 = 5/6 and kappa = c * sigma.
    """
    if c is None:
        return 5 * Symbol("c") / 6
    return 5 * Rational(c) / 6


def kappa_sl2(k=None):
    """kappa(sl_2_k) = 3(k+2)/4.

    From: dim=3, h*=2, kappa = dim*(k+h*)/(2*h*) = 3*(k+2)/4.
    """
    if k is None:
        return 3 * (Symbol("k") + 2) / 4
    return Rational(3) * (Rational(k) + 2) / 4


def kappa_sl3(k=None):
    """kappa(sl_3_k) = 8*(k+3)/(2*3) = 4*(k+3)/3.

    From: dim=8, h*=3, kappa = 8*(k+3)/6 = 4*(k+3)/3.
    """
    if k is None:
        return 4 * (Symbol("k") + 3) / 3
    return Rational(4) * (Rational(k) + 3) / 3


def kappa_g2(k=None):
    """kappa(G_2_k) = 14*(k+4)/(2*4) = 7*(k+4)/4.

    From: dim=14, h*=4, kappa = dim*(k+h*)/(2*h*) = 14*(k+4)/8 = 7*(k+4)/4.
    """
    if k is None:
        return 7 * (Symbol("k") + 4) / 4
    return Rational(7) * (Rational(k) + 4) / 4


def kappa_b2(k=None):
    """kappa(B_2_k) = 10*(k+3)/(2*3) = 5*(k+3)/3.

    From: dim=10, h*=3, kappa = dim*(k+h*)/(2*h*) = 10*(k+3)/6 = 5*(k+3)/3.
    """
    if k is None:
        return 5 * (Symbol("k") + 3) / 3
    return Rational(5) * (Rational(k) + 3) / 3


# ---------------------------------------------------------------------------
# Genus expansion tables
# ---------------------------------------------------------------------------

def genus_table(kappa_val, max_genus: int = 10) -> Dict[int, Rational]:
    """Compute F_g for g = 1, ..., max_genus.

    Uses exact rational arithmetic throughout.
    """
    table = {}
    for g in range(1, max_genus + 1):
        table[g] = F_g(kappa_val, g)
    return table


def genus_table_numeric(kappa_val, max_genus: int = 10) -> Dict[int, str]:
    """Genus table with both exact and approximate values."""
    table = {}
    for g in range(1, max_genus + 1):
        exact = F_g(kappa_val, g)
        table[g] = str(exact)
    return table


# ---------------------------------------------------------------------------
# Complementarity
# ---------------------------------------------------------------------------

def complementarity_sum_km(type_: str, rank: int, k=None) -> Rational:
    """Compute kappa(ĝ_k) + kappa(ĝ_{k'}) where k' = -k - 2h*.

    This should be level-independent (depends only on root datum).
    """
    if k is None:
        k = Symbol("k")
    data = cartan_data(type_, rank)
    kappa_k = kappa_km(type_, rank, k)
    k_prime = ff_dual_level(type_, rank, k)
    kappa_k_prime = kappa_km(type_, rank, k_prime)
    total = simplify(kappa_k + kappa_k_prime)
    return total


def complementarity_sum_w(type_: str, rank: int, k=None):
    """Compute kappa(W^k(g)) + kappa(W^{k'}(g)).

    For W-algebras: kappa = c * sigma(g), so:
    kappa + kappa' = (c + c') * sigma(g)

    This is the content of thm:complementarity-root-datum.
    """
    sigma = sigma_invariant(type_, rank)
    if type_ == "A" and rank == 1:
        # Virasoro case: c + c' = 26
        c_sum = Rational(26)
    elif type_ == "A" and rank == 2:
        # W_3 case: c + c' = ? Need to compute
        if k is None:
            k = Symbol("k")
        c_k = w3_ds_c(k)
        k_prime = ff_dual_level(type_, rank, k)
        c_k_prime = w3_ds_c(k_prime)
        c_sum = simplify(c_k + c_k_prime)
    else:
        c_sum = Symbol("c_sum")  # general case needs DS formula

    return c_sum * sigma


# ---------------------------------------------------------------------------
# Convergence
# ---------------------------------------------------------------------------

def convergence_radius() -> Rational:
    """Radius of convergence of the genus expansion.

    |x| = 2*pi, so ratio |F_{g+1}/F_g| -> 1/(2*pi)^2 as g -> inf.

    This is the content of thm:bernoulli-universality.
    """
    return 2 * pi


def ratio_successive(kappa_val, g: int):
    """Compute |F_{g+1}/F_g| for checking convergence."""
    fg = F_g(kappa_val, g)
    fg1 = F_g(kappa_val, g + 1)
    if fg == 0:
        return None
    return simplify(fg1 / fg)


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

KNOWN_F1 = {
    "Heisenberg": ("kappa", lambda kappa: kappa * lambda_fp(1)),
    "sl2": ("k", lambda k: Rational(3) * (k + 2) / 4 * lambda_fp(1)),
    "sl3": ("k", lambda k: Rational(4) * (k + 3) / 3 * lambda_fp(1)),
    "G2": ("k", lambda k: Rational(7) * (k + 4) / 4 * lambda_fp(1)),
    "B2": ("k", lambda k: Rational(5) * (k + 3) / 3 * lambda_fp(1)),
    "Virasoro": ("c", lambda c: c / 2 * lambda_fp(1)),
    "W3": ("c", lambda c: 5 * c / 6 * lambda_fp(1)),
}


def verify_F1(algebra: str, param_val, computed) -> Tuple[bool, str]:
    """Verify a computed F_1 value against known formulas."""
    if algebra not in KNOWN_F1:
        return True, f"No ground truth for F_1({algebra})"

    param_name, formula = KNOWN_F1[algebra]
    expected = formula(Rational(param_val))
    computed_r = Rational(computed) if not hasattr(computed, 'is_Rational') else computed

    if simplify(computed_r - expected) == 0:
        return True, f"VERIFIED: F_1({algebra}) = {computed} matches formula"
    return False, f"MISMATCH: computed F_1({algebra}) = {computed}, expected {expected}"
