"""Primitive modular master-kernel profiles and metaplectic shadows.

Encodes the primitive kernel compression of the modular Koszul theory:
corolla coefficients, rigid-cut terms, shell equations, and the reduced
branch half-density that squares to the spectral determinant.

References:
  - Vol I, Definition def:primitive-log-modular-kernel
  - Vol I, Theorem thm:primitive-to-global-reconstruction
  - Vol I, Proposition prop:primitive-shell-equations
  - Vol I, Corollary cor:metaplectic-square-root
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from sympy import Matrix, Rational, Symbol, expand, eye, exp, simplify


@dataclass(frozen=True)
class MasterKernelProfile:
    """Primitive master-kernel data for a standard family.

    Encodes which corolla and rigid-cut terms are active, the branch
    rank, and derives shell equations and regime classification.
    """

    name: str
    cubic: bool
    quartic: bool
    rigid2: bool
    rigid3: bool
    branch_rank: int

    def primitive_kernel(self) -> Tuple[str, ...]:
        """Components of the primitive kernel K_A."""
        out = ["K02", "K11"]
        if self.cubic:
            out.insert(1, "K03")
        if self.quartic:
            out.insert(2 if self.cubic else 1, "K04")
        if self.rigid2:
            out.append("Rpf2")
        if self.rigid3:
            out.append("Rpf3")
        return tuple(out)

    def master_action_terms(self) -> Tuple[str, ...]:
        """Terms in the branch master action S^br_A."""
        out = ["S2"]
        if self.cubic:
            out.append("S3")
        if self.quartic:
            out.append("S4")
        if self.rigid2:
            out.append("Sigma2")
        if self.rigid3:
            out.append("Sigma3")
        return tuple(out)

    def genus_two_forcing(self) -> Tuple[str, ...]:
        """Genus-2 shell equation terms (Prop. primitive-shell-equations)."""
        out = ["Delta(K11)"]
        if self.cubic:
            out.append("1/2[K11,K11]")
        if self.quartic or self.rigid2:
            out.append("Rpf2(K02)")
        return tuple(out)

    def genus_three_forcing(self) -> Tuple[str, ...]:
        """Genus-3 shell equation terms (Prop. primitive-shell-equations)."""
        out = ["Delta(K2.)"]
        if self.cubic:
            out.append("[K11,K2.]")
            out.append("1/6[K11,K11,K11]")
        if self.rigid2:
            out.append("Rpf2(K11)")
        if self.quartic or self.rigid3:
            out.append("Rpf3(K02)")
        return tuple(out)

    def qme_shells(self) -> Tuple[str, ...]:
        """Quantum master equation shell conditions."""
        out = []
        if self.cubic:
            out.append("dK03=0")
            out.append("dK11+Delta_ns(K03)=0")
        else:
            out.append("K03=0")
            out.append("dK11=0")
        if self.quartic:
            out.append("dK04+K03*K03=0")
        else:
            out.append("K04=0")
        out.append("R2=" + "+".join(self.genus_two_forcing()))
        out.append("R3=" + "+".join(self.genus_three_forcing()))
        return tuple(out)

    def regime(self) -> str:
        """Shadow depth classification: G, L, C, or M regime."""
        if not self.cubic and not self.quartic:
            return "pure quadratic"
        if self.cubic and not self.quartic:
            return "cubic-tree"
        return "quartic-rigid"


# Standard family profiles
HEISENBERG = MasterKernelProfile(
    name="Heisenberg",
    cubic=False,
    quartic=False,
    rigid2=False,
    rigid3=False,
    branch_rank=1,
)

AFFINE_SL2 = MasterKernelProfile(
    name="Affine sl2-hat",
    cubic=True,
    quartic=False,
    rigid2=False,
    rigid3=False,
    branch_rank=2,
)

VIRASORO = MasterKernelProfile(
    name="Virasoro",
    cubic=True,
    quartic=True,
    rigid2=True,
    rigid3=True,
    branch_rank=2,
)

W3 = MasterKernelProfile(
    name="W3",
    cubic=True,
    quartic=True,
    rigid2=True,
    rigid3=True,
    branch_rank=3,
)

PROFILES: Dict[str, MasterKernelProfile] = {
    "heisenberg": HEISENBERG,
    "affine_sl2": AFFINE_SL2,
    "virasoro": VIRASORO,
    "w3": W3,
}


def get_profile(name: str) -> MasterKernelProfile:
    """Return the named master-kernel profile."""
    return PROFILES[name]


def profile_table(
    names: Iterable[str] | None = None,
) -> Tuple[Tuple[str, str, str, str], ...]:
    """Compact summary table for the standard families."""
    if names is None:
        names = PROFILES.keys()
    rows = []
    for name in names:
        profile = PROFILES[name]
        rows.append(
            (
                profile.name,
                profile.regime(),
                ", ".join(profile.master_action_terms()),
                ", ".join(profile.genus_two_forcing()),
            )
        )
    return tuple(rows)


def w3_quartic_factor(c: Symbol | int | object):
    """Universal quartic coefficient for the W3 primitive master action.

    Returns 16/(22 + 5c), the coefficient of the quartic quasi-primary
    Lambda = :TT: - (3/10) d^2 T in the W3 branch master action.
    """
    return simplify(Rational(16, 1) / (22 + 5 * c))


def formal_metaplectic_half_density(
    operator: Matrix, x: Symbol, order: int
):
    """Truncated metaplectic half-density exp(1/2 Tr log(1 - xT)).

    Corollary cor:metaplectic-square-root: this is the canonical
    square root of the spectral determinant det(1 - xT).
    """
    if operator.rows != operator.cols:
        raise ValueError("operator must be square")
    series_exponent = 0
    for m in range(1, order + 1):
        series_exponent -= (
            simplify((operator**m).trace()) * x**m / (2 * m)
        )
    return simplify(
        exp(series_exponent).series(x, 0, order + 1).removeO()
    )


def determinant_series(operator: Matrix, x: Symbol, order: int):
    """Taylor polynomial of det(1 - xT)."""
    if operator.rows != operator.cols:
        raise ValueError("operator must be square")
    return simplify(
        (eye(operator.rows) - x * operator)
        .det()
        .series(x, 0, order + 1)
        .removeO()
    )
