"""Finite invariants for bar-cobar bottleneck verification.

The functions in this module are deliberately small: each one computes a
finite algebraic witness for a manuscript claim whose statement is otherwise
infinite-categorical.  Tests use these witnesses as disjoint checks, not as
the source of the manuscript proofs.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

from sympy import Matrix, Poly, symbols


t = symbols("t")


def degree_cutoff_survives(stage: int, arity: int) -> bool:
    """Return whether epsilon^arity survives in k[epsilon]/epsilon^{stage+1}.

    This is the finite quotient model for the strong-filtration assertion:
    if every input lies in F^1, an arity-r operation lands in F^r and
    vanishes modulo F^{N+1} exactly when r >= N+1.
    """
    if stage < 0:
        raise ValueError("stage must be nonnegative")
    if arity < 1:
        raise ValueError("arity must be positive")
    return arity <= stage


def degree_cutoff_profile(stage: int, max_arity: int) -> dict[int, bool]:
    """Survival profile for arities 1..max_arity in the finite quotient."""
    return {
        arity: degree_cutoff_survives(stage, arity)
        for arity in range(1, max_arity + 1)
    }


@dataclass(frozen=True)
class WeightCohomologySlice:
    """Cohomology dimensions of a two-term weight slice."""

    weight: int
    h0: int
    h1: int


def toy_weight_slice_cohomology(weight: int) -> WeightCohomologySlice:
    """Cohomology of a finite two-term complex in a fixed weight.

    The slice is Q^2 -> Q.  For even weights the differential has rank 1;
    for odd weights it has rank 0.  This gives a nonconstant family of
    finite-dimensional slices while keeping the rank computation exact.
    """
    if weight < 0:
        raise ValueError("weight must be nonnegative")
    rank = 1 if weight % 2 == 0 else 0
    return WeightCohomologySlice(weight=weight, h0=2 - rank, h1=1 - rank)


def toy_weight_tower(stage: int) -> dict[int, WeightCohomologySlice]:
    """Weight-slice cohomology for the truncated tower C_{<= stage}."""
    if stage < 0:
        raise ValueError("stage must be nonnegative")
    return {
        weight: toy_weight_slice_cohomology(weight)
        for weight in range(stage + 1)
    }


def weight_slices_stabilize(max_stage: int) -> bool:
    """Check C_{N+1}->C_N is identity on weight slices w <= N."""
    if max_stage < 1:
        raise ValueError("max_stage must be at least 1")
    for stage in range(max_stage):
        lower = toy_weight_tower(stage)
        upper = toy_weight_tower(stage + 1)
        for weight, slice_lower in lower.items():
            if upper[weight] != slice_lower:
                return False
    return True


def _poly(expr) -> Poly:
    return Poly(expr, t, domain="QQ")


def _coeff_vector(poly: Poly, length: int) -> Matrix:
    coeffs = [Fraction(0) for _ in range(length)]
    for (degree,), coeff in poly.terms():
        if degree < length:
            coeffs[degree] = Fraction(coeff)
    return Matrix([coeffs])


def _remainder_vector(expr, modulus: Poly) -> Matrix:
    rem = _poly(expr).rem(modulus)
    return _coeff_vector(rem, modulus.degree())


def _rank(vectors: Iterable[Matrix]) -> int:
    cols = [v.T for v in vectors]
    if not cols:
        return 0
    return Matrix.hstack(*cols).rank()


def core_basis(modulus_expr, divisor_expr) -> list[Matrix]:
    """Basis vectors for C_g(p)=(p/g)M(p) inside k[t]/(p)."""
    p = _poly(modulus_expr)
    g = _poly(divisor_expr)
    quotient, remainder = p.div(g)
    if not remainder.is_zero:
        raise ValueError("divisor_expr must divide modulus_expr")
    return [
        _remainder_vector((t**j) * quotient.as_expr(), p)
        for j in range(g.degree())
    ]


def core_rank(modulus_expr, divisor_expr) -> int:
    return _rank(core_basis(modulus_expr, divisor_expr))


def divisor_core_summary(modulus_expr, g1_expr, g2_expr) -> dict[str, int | bool]:
    """Compute the finite divisor-core lattice data for two divisors."""
    p = _poly(modulus_expr)
    g1 = _poly(g1_expr)
    g2 = _poly(g2_expr)
    basis1 = core_basis(p.as_expr(), g1.as_expr())
    basis2 = core_basis(p.as_expr(), g2.as_expr())
    sum_rank = _rank([*basis1, *basis2])
    intersection_rank = _rank(basis1) + _rank(basis2) - sum_rank
    gcd = g1.gcd(g2).monic()
    lcm = ((g1 * g2).quo(gcd)).monic()
    quotient1 = p.quo(g1).monic()
    quotient2 = p.quo(g2).monic()
    return {
        "degree_p": p.degree(),
        "rank_g1": _rank(basis1),
        "rank_g2": _rank(basis2),
        "rank_gcd": core_rank(p.as_expr(), gcd.as_expr()),
        "rank_lcm": core_rank(p.as_expr(), lcm.as_expr()),
        "intersection_rank": intersection_rank,
        "sum_rank": sum_rank,
        "quotient_dim_g1": p.degree() - _rank(basis1),
        "quotient_degree_g1": quotient1.degree(),
        "quotient_dim_g2": p.degree() - _rank(basis2),
        "quotient_degree_g2": quotient2.degree(),
        "g1_splits": g1.gcd(quotient1).degree() == 0,
        "g2_splits": g2.gcd(quotient2).degree() == 0,
    }
