r"""Affine type-A zero-mode audit for the first chiral-Hochschild group.

For ``sl_N`` the adjoint zero modes span an ``N^2-1`` dimensional subspace.
Their action

    (J^a)_(0) J^b = f^{ab}_c J^c

is inner.  This finite-dimensional calculation identifies a known inner
subspace of the completed chiral derivation complex.  The dimension of the
full quotient ``Der_ch/Inn_ch`` requires the complete chart complex and its
bounded-to-chart comparison, so the numerical value of
``ChirHoch^1(V_k(sl_N))`` remains open.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


CHART_H1_OBLIGATION = (
    "construct the completed affine chiral derivation complex, compute every "
    "cocycle and inner coderivation, and prove the bounded-to-chart "
    "quasi-isomorphism"
)


@dataclass(frozen=True)
class AffineSLNOuterDerivationAudit:
    N: int
    level: object
    lie_dimension: int
    adjoint_zero_mode_dimension: int
    known_inner_zero_mode_dimension: int
    chart_chirhoch1_dimension: Optional[int]
    status: str
    resolution_obligation: str


def affine_sl_n_outer_derivation_audit(
    N: int, k: object = "generic"
) -> AffineSLNOuterDerivationAudit:
    if not isinstance(N, int) or N < 2:
        raise ValueError("N must be an integer at least 2")
    if isinstance(k, str):
        if k != "generic":
            raise ValueError("a string level must equal 'generic'")
    elif k == -N:
        raise ValueError(f"the critical level k={-N} has a separate centre theory")

    dimension = N * N - 1
    return AffineSLNOuterDerivationAudit(
        N=N,
        level=k,
        lie_dimension=dimension,
        adjoint_zero_mode_dimension=dimension,
        known_inner_zero_mode_dimension=dimension,
        chart_chirhoch1_dimension=None,
        status="open-complete-chiral-derivation-quotient",
        resolution_obligation=CHART_H1_OBLIGATION,
    )


def compute_chirhoch1_affine_sl_n(
    N: int, k: object = "generic"
) -> Optional[int]:
    """Return the chart dimension when available; the current audit gives ``None``."""

    return affine_sl_n_outer_derivation_audit(N, k).chart_chirhoch1_dimension


def verify_fr4_conjecture() -> Dict[int, AffineSLNOuterDerivationAudit]:
    """Return exact type-A zero-mode arithmetic for ``N=2,...,8``."""

    return {N: affine_sl_n_outer_derivation_audit(N) for N in range(2, 9)}
