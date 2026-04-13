r"""Verlinde polynomial family for sl_3: polynomiality in n = k + h^v.

This engine studies the Verlinde dimension Z_g(sl_3, k) as a POLYNOMIAL
in the shifted variable n = k + 3 (where h^v = 3 is the dual Coxeter
number of sl_3).  The polynomiality is a theorem of Zagier, proved for
all simple Lie algebras by Zagier and Beauville; this engine computes the
polynomials explicitly and verifies their structural properties.

THE MATHEMATICAL FRAMEWORK:

  For sl_3 at level k, the Verlinde dimension is

      Z_g(k) = sum_{lambda in P_+^k} S_{0,lambda}^{2-2g}

  where P_+^k is the set of integrable highest weights (a,b) with
  a >= 0, b >= 0, a + b <= k, and S_{0,lambda} is the first row of
  the modular S-matrix.

  The quantum dimensions are

      d_{(a,b)}(k) = S_{0,(a,b)} / S_{0,0}
        = sin(pi(a+1)/n) sin(pi(b+1)/n) sin(pi(a+b+2)/n)
          / (sin(pi/n)^2 sin(2pi/n))

  where n = k + 3 = k + h^v.

  By unitarity of the S-matrix row:

      Z_g(k) = D^{2(g-1)} * Q_g(k)

  where D^2 = sum d_lambda^2 = S_{0,0}^{-2} (the total quantum
  dimension squared) and Q_g = sum d_lambda^{2-2g}.

POLYNOMIALITY:

  Z_g(sl_3, k) is a polynomial of degree 8(g-1) = dim(SU(3)) * (g-1)
  in the variable n = k + 3.  The key structural properties:

  (P1) For g >= 2, P_g(n) is an EVEN function: P_g(-n) = P_g(n).
       (Equivalently, only even powers of n appear.)
       For g = 1, P_1(n) = (n-1)(n-2)/2 is NOT even.

  (P2) For g >= 2, P_g(n) vanishes at n = 0, 1, 2, and by evenness
       also at n = -1, -2.  This gives the divisibility
           P_g(n) = n^2 (n^2 - 1)(n^2 - 4) * Q_g(n^2)
       where Q_g is a polynomial of degree 4(g-1) - 3 in n^2.

  (P3) The leading coefficient of P_g(n) as a degree 8(g-1) polynomial
       is related to the Witten zeta value zeta_W(2g-2, SU(3)):
           LC(P_g) ~ 1/(2g-2)! * zeta_W(2g-2) * (product over positive
           roots of 1/alpha) in a precise sense.
       For g = 2: LC = 2/8! = 1/20160.

  (P4) P_g(3) = Z_g(k=0) = 1 for all g (only the vacuum representation
       survives at level 0).

NUMERICAL DATA (n = k + 3):

  g=0: P_0 = 1
  g=1: P_1(n) = (n-1)(n-2)/2 = n^2/2 - 3n/2 + 1
  g=2: P_2(n) = n^2(n^2-1)(n^2-4)(n^2+47) / 20160
  g=3: degree 16 even polynomial, LC = 19/41513472000
  g=4: degree 24 even polynomial, LC = 1031/189225711747072000

RELATION TO THE EXISTING sl3_verlinde_engine:

  This engine wraps sl3_verlinde_engine.py (which computes Z_g(k)
  directly via quantum dimensions and high-precision arithmetic) and
  provides the POLYNOMIAL FAMILY viewpoint:
    - Express Z_g as P_g(n) with n = k + h^v
    - Verify polynomiality, evenness, vanishing, divisibility
    - Extract structural coefficients
    - Compare the polynomial at integer n with direct computation
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial
from typing import Dict, List, Optional, Tuple

from sympy import Poly, Rational, Symbol, expand, symbols

from compute.lib.sl3_verlinde_engine import (
    SL3_DIM,
    SL3_DUAL_COXETER,
    sl3_num_integrable_reps,
    sl3_verlinde_dimension,
    sl3_verlinde_polynomial,
    _POLY_SYMBOL as _K_SYMBOL,
)


# The shifted variable n = k + h^v
_N_SYMBOL = symbols("n")


def shifted_level(k: int) -> int:
    """n = k + h^v = k + 3."""
    return k + SL3_DUAL_COXETER


def verlinde_dimension(genus: int, level: int) -> int:
    """Z_g(sl_3, k) via the canonical sl3_verlinde_engine."""
    return sl3_verlinde_dimension(genus, level)


def verlinde_table(
    genus_range: Tuple[int, int] = (0, 4),
    level_range: Tuple[int, int] = (1, 6),
) -> Dict[Tuple[int, int], int]:
    """Table {(g, k): Z_g(k)} over the specified ranges."""
    result = {}
    for g in range(genus_range[0], genus_range[1] + 1):
        for k in range(level_range[0], level_range[1] + 1):
            result[(g, k)] = sl3_verlinde_dimension(g, k)
    return result


@lru_cache(maxsize=None)
def verlinde_polynomial_in_n(genus: int) -> Poly:
    """Verlinde polynomial P_g(n) where n = k + 3.

    Returns a sympy Poly in the variable n over QQ such that
    P_g(n) = Z_g(sl_3, k) when n = k + 3.
    """
    if genus < 0:
        raise ValueError(f"Genus must be non-negative, got g={genus}")

    n = _N_SYMBOL
    # Get the polynomial in k from the canonical engine
    p_k = sl3_verlinde_polynomial(genus)
    # Substitute k = n - 3
    expr_in_n = expand(p_k.as_expr().subs(_K_SYMBOL, n - 3))
    return Poly(expr_in_n, n, domain="QQ")


def verlinde_polynomial_degree(genus: int) -> int:
    """Degree of P_g(n): equals dim(SU(3)) * (g-1) = 8*(g-1) for g >= 1.

    Convention: deg(P_0) = 0 (constant 1).
    """
    if genus == 0:
        return 0
    if genus == 1:
        return 2  # (n-1)(n-2)/2 is degree 2
    return SL3_DIM * (genus - 1)


def is_even_polynomial(genus: int) -> bool:
    """Check whether P_g(-n) = P_g(n) (only even powers of n appear).

    True for g = 0 and g >= 2.  False for g = 1.
    """
    n = _N_SYMBOL
    p = verlinde_polynomial_in_n(genus)
    p_neg = Poly(expand(p.as_expr().subs(n, -n)), n, domain="QQ")
    return p == p_neg


def vanishing_at_roots(genus: int) -> Dict[int, bool]:
    """Check P_g(n) vanishes at n = 0, 1, 2.

    For g >= 2 all three vanish; for g = 1 only n=1,2 vanish;
    for g = 0 none vanish.
    """
    p = verlinde_polynomial_in_n(genus)
    return {nval: (p.eval(nval) == 0) for nval in [0, 1, 2]}


@lru_cache(maxsize=None)
def reduced_polynomial(genus: int) -> Optional[Poly]:
    """For g >= 2, compute Q_g(n) where P_g(n) = n^2(n^2-1)(n^2-4) Q_g(n).

    Q_g is an even polynomial of degree 8(g-1) - 6.
    Returns None for g < 2.
    """
    if genus < 2:
        return None

    n = _N_SYMBOL
    p = verlinde_polynomial_in_n(genus)
    divisor = Poly(n ** 2 * (n ** 2 - 1) * (n ** 2 - 4), n, domain="QQ")
    quotient, remainder = p.div(divisor)

    if remainder.as_expr() != 0:
        raise ValueError(
            f"Divisibility failed at g={genus}: remainder = {remainder.as_expr()}"
        )

    return quotient


def leading_coefficient(genus: int) -> Rational:
    """Leading coefficient of P_g(n) as a polynomial in n.

    For g = 2: LC = 1/20160 = 2/8!.
    """
    p = verlinde_polynomial_in_n(genus)
    return Rational(p.LC())


def verify_polynomial_at_level(genus: int, level: int) -> bool:
    """Check P_g(k+3) = Z_g(k) for a specific (g, k)."""
    p = verlinde_polynomial_in_n(genus)
    n_val = shifted_level(level)
    poly_val = int(p.eval(n_val))
    direct_val = sl3_verlinde_dimension(genus, level)
    return poly_val == direct_val


def genus2_factored_form() -> str:
    """Return the explicit factored form of P_2(n).

    P_2(n) = n^2 (n^2 - 1)(n^2 - 4)(n^2 + 47) / 20160.
    """
    return "n^2 * (n^2 - 1) * (n^2 - 4) * (n^2 + 47) / 20160"


def genus2_polynomial_in_n() -> Poly:
    """Explicit genus-2 Verlinde polynomial in n = k + 3."""
    n = _N_SYMBOL
    expr = n ** 2 * (n ** 2 - 1) * (n ** 2 - 4) * (n ** 2 + 47) / 20160
    return Poly(expand(expr), n, domain="QQ")


def genus1_polynomial_in_n() -> Poly:
    """Explicit genus-1 Verlinde polynomial in n = k + 3.

    P_1(n) = (n-1)(n-2)/2.
    """
    n = _N_SYMBOL
    return Poly(expand((n - 1) * (n - 2) / 2), n, domain="QQ")


def witten_zeta_leading_coefficient(genus: int) -> Rational:
    """The leading coefficient of P_g(n), expected to relate to
    the Witten zeta value zeta_W(2g-2, SU(3)).

    For g = 2: LC = 2/8! = 1/20160, corresponding to
    zeta_W(2, SU(3)) = sum_{irreps} 1/dim(lambda)^2.
    """
    return leading_coefficient(genus)


def polynomial_coefficients_in_n(genus: int) -> List[Rational]:
    """Coefficients of P_g(n) from highest to lowest degree.

    Returns a list [a_d, a_{d-1}, ..., a_1, a_0] where
    P_g(n) = a_d n^d + ... + a_1 n + a_0.
    """
    p = verlinde_polynomial_in_n(genus)
    return [Rational(c) for c in p.all_coeffs()]


def level_rank_check_genus1(level: int) -> bool:
    """At genus 1, Z_1(sl_3, k) = C(k+2, 2) = C(n-1, 2).

    Level-rank duality for sl_3 at level k vs sl_k at level 3
    predicts Z_1(sl_3, k) = Z_1(sl_k, 3).  Since both give
    C(k+2, 2), this is a tautology at genus 1.
    """
    expected = (level + 1) * (level + 2) // 2
    return sl3_verlinde_dimension(1, level) == expected


__all__ = [
    "SL3_DIM",
    "SL3_DUAL_COXETER",
    "genus1_polynomial_in_n",
    "genus2_factored_form",
    "genus2_polynomial_in_n",
    "is_even_polynomial",
    "leading_coefficient",
    "level_rank_check_genus1",
    "polynomial_coefficients_in_n",
    "reduced_polynomial",
    "shifted_level",
    "vanishing_at_roots",
    "verlinde_dimension",
    "verlinde_polynomial_degree",
    "verlinde_polynomial_in_n",
    "verlinde_table",
    "verify_polynomial_at_level",
    "witten_zeta_leading_coefficient",
]
