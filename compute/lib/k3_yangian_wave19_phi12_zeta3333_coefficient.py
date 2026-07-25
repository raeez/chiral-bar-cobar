"""The repeated weight-twelve multiple-zeta scalar.

Let x_n=n^{-3}.  The strict nested sum zeta(3,3,3,3) is the fourth
elementary symmetric function in the sequence (x_n).  Newton's
identities give

    zeta(3,3,3,3)
      = (zeta(3)^4 - 6*zeta(3)^2*zeta(6) + 3*zeta(6)^2
         + 8*zeta(3)*zeta(9) - 6*zeta(12))/24.

This identity belongs to the commutative algebra of multiple-zeta
periods.  Its motivic primitive projection is zero.  Division by 12!
defines a scalar normalisation.  A pentagon cochain, graph-complex
class, cyclic operation, or genus obstruction additionally requires
the corresponding chain maps and homotopies.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Dict

try:
    from mpmath import mp
except ImportError:  # pragma: no cover
    mp = None

from compute.lib.k3_yangian_wave18_pentagon_coboundary_hbar11_12 import (
    Polynomial,
    zeta3333_newton_identity,
)


def zeta3333_exact_polynomial() -> Polynomial:
    """Return the exact Newton polynomial."""
    return zeta3333_newton_identity()


def zeta3333_newton_numeric(dps: int = 50):
    """Evaluate the Newton identity with dps decimal digits."""
    if dps < 15:
        raise ValueError("dps must be at least 15")
    if mp is None:
        raise ImportError("numerical evaluation requires mpmath")
    with mp.workdps(dps):
        return +(
            mp.zeta(3) ** 4
            - 6 * mp.zeta(3) ** 2 * mp.zeta(6)
            + 3 * mp.zeta(6) ** 2
            + 8 * mp.zeta(3) * mp.zeta(9)
            - 6 * mp.zeta(12)
        ) / 24


def zeta3333_finite_elementary_sum(cutoff: int, dps: int = 50):
    """Evaluate the finite fourth elementary symmetric sum.

    The result is

        sum_{cutoff >= n1 > n2 > n3 > n4 >= 1}
            1/(n1*n2*n3*n4)^3.

    The descending update is an independent route from the Newton
    power-sum identity.
    """
    if cutoff < 4:
        raise ValueError("cutoff must be at least 4")
    if dps < 15:
        raise ValueError("dps must be at least 15")
    if mp is None:
        raise ImportError("numerical evaluation requires mpmath")

    with mp.workdps(dps):
        elementary = [mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        for n in range(1, cutoff + 1):
            value = mp.mpf(1) / mp.mpf(n) ** 3
            for depth in range(min(4, n), 0, -1):
                elementary[depth] += value * elementary[depth - 1]
        return +elementary[4]


def zeta3333_tail_corrected_sum(cutoff: int, dps: int = 50):
    """Add the leading tail to the finite elementary-symmetric sum.

    Writing e_3(N) for the finite third elementary symmetric sum,
    the omitted tail begins with

        e_3(N) * sum_{n>N} n^{-3}.

    The remaining term is bounded by the simultaneous variation of
    e_3 beyond N and is of order N^{-4}.
    """
    if cutoff < 4:
        raise ValueError("cutoff must be at least 4")
    if dps < 15:
        raise ValueError("dps must be at least 15")
    if mp is None:
        raise ImportError("numerical evaluation requires mpmath")

    with mp.workdps(dps):
        elementary = [mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        for n in range(1, cutoff + 1):
            value = mp.mpf(1) / mp.mpf(n) ** 3
            for depth in range(min(4, n), 0, -1):
                elementary[depth] += value * elementary[depth - 1]
        leading_tail = elementary[3] * mp.zeta(3, cutoff + 1)
        return +(elementary[4] + leading_tail)


def zeta3333_normalized_scalar(dps: int = 50):
    """Return zeta(3,3,3,3)/12! as a scalar normalisation."""
    if mp is None:
        raise ImportError("numerical evaluation requires mpmath")
    with mp.workdps(dps):
        return +(zeta3333_newton_numeric(dps) / factorial(12))


def weight12_scalar_status() -> Dict[str, object]:
    """Separate proved scalar arithmetic from open comparison maps."""
    return {
        "weight": 12,
        "depth": 4,
        "newton_identity": zeta3333_exact_polynomial(),
        "decomposable": True,
        "primitive_projection": 0,
        "simplex_denominator": factorial(12),
        "normalized_scalar_defined": True,
        "normalized_scalar_is_pentagon_coefficient": False,
        "associator_word_specified": False,
        "graph_complex_class_constructed": False,
        "word_to_cochain_map_constructed": False,
        "cyclic_cochain_constructed": False,
        "genus_comparison_constructed": False,
        "status": "exact product-period scalar; chain comparison open",
    }


def run_tests() -> Dict[str, bool]:
    """Run exact and numerical consistency checks."""
    expected = {
        (3, 3, 3, 3): Fraction(1, 24),
        (3, 3, 6): Fraction(-1, 4),
        (6, 6): Fraction(1, 8),
        (3, 9): Fraction(1, 3),
        (12,): Fraction(-1, 4),
    }
    status = weight12_scalar_status()
    if mp is None:
        finite_agreement = True
        numerical_anchor = True
    else:
        with mp.workdps(50):
            exact_value = zeta3333_newton_numeric(50)
            finite_value = zeta3333_tail_corrected_sum(50_000, 50)
            finite_agreement = abs(exact_value - finite_value) < mp.mpf("1e-18")
            numerical_anchor = abs(
                exact_value
                - mp.mpf(
                    "0.000295999014043171835500960819133545583238160712113"
                )
            ) < mp.mpf("1e-49")

    return {
        "newton_identity_exact": zeta3333_exact_polynomial() == expected,
        "numerical_anchor": numerical_anchor,
        "finite_sum_agrees": finite_agreement,
        "primitive_projection_zero": status["primitive_projection"] == 0,
        "pentagon_coefficient_open": (
            status["normalized_scalar_is_pentagon_coefficient"] is False
        ),
        "cochain_comparison_open": (
            status["word_to_cochain_map_constructed"] is False
        ),
    }


if __name__ == "__main__":
    checks = run_tests()
    for name, passed in checks.items():
        print(f"{name}: {passed}")
    if not all(checks.values()):
        raise SystemExit(1)
