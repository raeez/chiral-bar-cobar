"""Rank-one Heisenberg curved second-kind finite-window contraction.

This module checks the finite-window normal form used by
``lem:curved-dual-centre-heisenberg``.  In weight window N, the curved
second-kind Koszul column is a vacuum line plus oscillator pairs

    0 -> Q*e_n --(-k*n)--> Q*f_n -> 0,  1 <= n <= N.

For k != 0 every positive-weight pair is contractible and the
degreewise inverse system is strict Mittag-Leffler.  This proves the
curved dual-vacuum endpoint only; it does not prove ordered
residue-twisted acyclicity, ordered-to-symmetric descent, or Theorem H.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CurvedSecondKindWindowReport:
    """Exact finite-window report for the curved Heisenberg dual."""

    level: Fraction
    max_weight: int
    coefficients: tuple[Fraction, ...]
    vacuum_cohomology_dim: int
    positive_weight_cohomology: tuple[tuple[int, int], ...]
    strict_mittag_leffler: bool
    logical_scope: str = (
        "rank-one Heisenberg curved second-kind endpoint only; not "
        "ordered residue-twisted acyclicity, not ordered-to-symmetric "
        "descent, and not a proof of Theorem H"
    )
    proves_curved_second_kind_endpoint: bool = True
    proves_theorem_h: bool = False


def curved_second_kind_heisenberg_report(
    level: int | Fraction, max_weight: int
) -> CurvedSecondKindWindowReport:
    """Return exact coefficients and cohomology for the finite window."""

    k = level if isinstance(level, Fraction) else Fraction(level)
    if max_weight < 0:
        raise ValueError("max_weight must be nonnegative")
    coefficients = tuple(-k * n for n in range(1, max_weight + 1))
    positive = tuple(
        (n, 1 if coefficient == 0 else 0)
        for n, coefficient in enumerate(coefficients, start=1)
    )
    return CurvedSecondKindWindowReport(
        level=k,
        max_weight=max_weight,
        coefficients=coefficients,
        vacuum_cohomology_dim=1,
        positive_weight_cohomology=positive,
        strict_mittag_leffler=(k != 0),
        proves_curved_second_kind_endpoint=(k != 0),
    )
