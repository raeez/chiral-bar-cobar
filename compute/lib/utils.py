"""Graded vector spaces, tensor products, cohomological sign conventions.

CONVENTION: This monograph uses COHOMOLOGICAL grading (|d| = +1).
Bar construction uses DESUSPENSION: B(A) = T^c(s^{-1}A-bar, d).
Suspension: sV = V[-1] under V[n]^k = V^{k+n}.
Koszul sign rule: swapping elements of degrees p and q gives (-1)^{pq}.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import sympy
from sympy import Matrix, Rational, binomial, factorial, bernoulli, zeros


# ---------------------------------------------------------------------------
# Graded vector space
# ---------------------------------------------------------------------------

@dataclass
class GradedVectorSpace:
    """A finite-dimensional graded vector space V = ⊕ V^k.

    dims[k] = dim V^k.  Missing keys are treated as 0.
    """
    dims: Dict[int, int] = field(default_factory=dict)
    name: str = ""

    def dim(self, degree: int) -> int:
        return self.dims.get(degree, 0)

    def total_dim(self) -> int:
        return sum(self.dims.values())

    def euler_char(self) -> int:
        """Euler characteristic: sum (-1)^k dim V^k."""
        return sum((-1)**k * d for k, d in self.dims.items())

    def poincare_series(self, var: str = "t") -> sympy.Expr:
        """Poincare series sum dim(V^k) t^k."""
        t = sympy.Symbol(var)
        return sum(d * t**k for k, d in sorted(self.dims.items()))

    def shift(self, n: int) -> "GradedVectorSpace":
        """V[n] with V[n]^k = V^{k+n}."""
        return GradedVectorSpace(
            dims={k - n: d for k, d in self.dims.items()},
            name=f"{self.name}[{n}]" if self.name else "",
        )

    def desuspend(self) -> "GradedVectorSpace":
        """s^{-1}V = V[1] (cohomological: desuspension shifts degree DOWN by 1)."""
        return self.shift(1)

    def suspend(self) -> "GradedVectorSpace":
        """sV = V[-1] (cohomological: suspension shifts degree UP by 1)."""
        return self.shift(-1)

    def __repr__(self) -> str:
        parts = [f"{k}:{d}" for k, d in sorted(self.dims.items()) if d != 0]
        label = f"{self.name} " if self.name else ""
        return f"GVS({label}{{{', '.join(parts)}}})"


# ---------------------------------------------------------------------------
# Chain complex
# ---------------------------------------------------------------------------

@dataclass
class ChainComplex:
    """A cochain complex (C*, d) with d of degree +1.

    differentials[k] is a matrix d: C^k -> C^{k+1}.
    """
    spaces: GradedVectorSpace
    differentials: Dict[int, Matrix] = field(default_factory=dict)
    name: str = ""

    def d(self, degree: int) -> Optional[Matrix]:
        """Return d: C^degree -> C^{degree+1}, or None if not defined."""
        return self.differentials.get(degree)

    def check_d_squared(self) -> List[Tuple[int, bool]]:
        """Check d^2 = 0 at every degree. Returns [(degree, passes)]."""
        results = []
        degrees = sorted(self.differentials.keys())
        for k in degrees:
            d_k = self.differentials.get(k)
            d_k1 = self.differentials.get(k + 1)
            if d_k is not None and d_k1 is not None:
                product = d_k1 * d_k
                passes = product.is_zero_matrix
                results.append((k, passes))
        return results

    def cohomology_dim(self, degree: int) -> Optional[int]:
        """Compute dim H^degree = dim ker(d^degree) - dim im(d^{degree-1})."""
        d_k = self.differentials.get(degree)
        d_km1 = self.differentials.get(degree - 1)

        dim_k = self.spaces.dim(degree)
        if dim_k == 0:
            return 0

        # kernel of d: C^k -> C^{k+1}
        if d_k is not None:
            ker_dim = dim_k - d_k.rank()
        else:
            ker_dim = dim_k  # d is zero -> everything is a cocycle

        # image of d: C^{k-1} -> C^k
        if d_km1 is not None:
            im_dim = d_km1.rank()
        else:
            im_dim = 0

        return ker_dim - im_dim


# ---------------------------------------------------------------------------
# Koszul sign
# ---------------------------------------------------------------------------

def koszul_sign(degrees: List[int], permutation: List[int]) -> int:
    """Compute the Koszul sign of a permutation of homogeneous elements.

    Args:
        degrees: degrees of elements in original order
        permutation: the permutation as a list of indices

    Returns:
        +1 or -1
    """
    sign = 1
    n = len(degrees)
    for i in range(n):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                sign *= (-1) ** (degrees[permutation[i]] * degrees[permutation[j]])
    return sign


# ---------------------------------------------------------------------------
# Bernoulli / Faber-Pandharipande numbers
# ---------------------------------------------------------------------------

def lambda_fp(g: int) -> Rational:
    """Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    This is the tautological integral int_{M-bar_{g,1}} psi^{2g-2} lambda_g.
    Generating function: sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    numerator = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    denominator = 2 ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


def F_g(kappa: sympy.Expr, g: int) -> sympy.Expr:
    """Genus-g free energy: F_g(A) = kappa(A) * lambda_g^FP."""
    return kappa * lambda_fp(g)


# ---------------------------------------------------------------------------
# Partition function (for Heisenberg bar complex verification)
# ---------------------------------------------------------------------------

def partition_number(n: int) -> int:
    """Number of integer partitions of n. p(0) = 1, p(1) = 1, p(2) = 2, ..."""
    if n < 0:
        return 0
    # Simple DP
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            dp[m] += dp[m - k]
    return dp[n]
