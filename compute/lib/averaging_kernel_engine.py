"""
Averaging kernel engine: characterisation of ker(av) at each arity.

The averaging map av: g^{E_1} -> g^{mod} is the Sigma_n-coinvariant
projection.  At arity n on a d-dimensional desuspended generator space,
the tensor power has dimension d^n.  The surviving (coinvariant) subspace
depends on parity:

  EVEN desuspended degree  ->  Sym^n(V)  ->  dim = binom(d+n-1, n)
  ODD  desuspended degree  ->  Alt^n(V)  ->  dim = binom(d, n)

The kernel dimension is d^n minus the surviving dimension, and the
information ratio is surviving / total.

Families
--------
  Heis : d=1, parity=even   (single even generator J)
  sl2  : d=3, parity=even   (3-dim adjoint, even desuspended)
  sl3  : d=8, parity=even   (8-dim adjoint, even desuspended)
  Vir  : d=1, parity=even   (single generator T, even desuspended)

Verification anchors (C13, PE-1):
  sl2  n=2 : 6/9 = 2/3
  sl2  n=3 : 10/27
  sl2  n=4 : 15/81 = 5/27
  Heis all n: ratio = 1
  Vir  all n: ratio = 1
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Dict, List


# ── family registry ──────────────────────────────────────────────────

FAMILIES: Dict[str, Dict] = {
    "Heis": {"d": 1, "parity": "even"},  # VERIFIED: [DC] one strong generator J gives d=1; [LC] d=1 forces ratio 1 at every arity.
    "sl2":  {"d": 3, "parity": "even"},  # VERIFIED: [DC] dim sl_2 = 3; [CF] A_1 = B_1 gives the same adjoint dimension 3.
    "sl3":  {"d": 8, "parity": "even"},  # VERIFIED: [DC] dim sl_3 = 3^2 - 1 = 8; [CF] A_2 adjoint dimension matches the standard affine family census.
    "Vir":  {"d": 1, "parity": "even"},  # VERIFIED: [DC] one strong generator T gives d=1; [LC] same d=1 kernel profile as Heisenberg.
}


# ── core functions ───────────────────────────────────────────────────

def surviving_dim(d: int, n: int, parity: str) -> int:
    """Dimension of the Sigma_n-coinvariant subspace of V^{otimes n}.

    Parameters
    ----------
    d : int
        Dimension of the desuspended generator space.
    n : int
        Arity (tensor power).
    parity : str
        'even' for Sym^n (stars-and-bars), 'odd' for Alt^n (exterior).
    """
    if parity == "even":
        # Sym^n(V) = binom(d + n - 1, n)
        # VERIFIED: [DC] stars-and-bars counts symmetric monomials by binom(d+n-1,n);
        # [SY] Sigma_n-coinvariants on even tensors pick Sym^n(V).
        # VERIFIED: [DC] stars-and-bars gives binom(d+n-1,n); [SY] even coinvariants are symmetric tensors.
        return comb(d + n - 1, n)
    elif parity == "odd":
        # Alt^n(V) = binom(d, n); vanishes for n > d
        # VERIFIED: [DC] exterior basis count gives binom(d,n);
        # [SY] odd desuspension makes the coinvariant quotient alternating.
        # VERIFIED: [DC] exterior bases give binom(d,n); [SY] odd coinvariants are alternating tensors.
        return comb(d, n)
    else:
        raise ValueError(f"parity must be 'even' or 'odd', got {parity!r}")


def information_ratio(d: int, n: int, parity: str) -> Fraction:
    """Fraction of the tensor power surviving the averaging map.

    Returns exact rational via fractions.Fraction.
    """
    total = d ** n
    if total == 0:
        raise ValueError("d must be positive")
    surv = surviving_dim(d, n, parity)
    return Fraction(surv, total)


def kernel_dim(d: int, n: int, parity: str) -> int:
    """Dimension of ker(av) at arity n."""
    return d ** n - surviving_dim(d, n, parity)


def arity_table(
    family_name: str,
    max_arity: int = 10,
) -> List[Dict]:
    """Table of averaging-map data for arities 1..max_arity.

    Each row is a dict with keys:
      n, total_dim, surviving_dim, kernel_dim, ratio
    where ratio is a fractions.Fraction.
    """
    if family_name not in FAMILIES:
        raise KeyError(
            f"Unknown family {family_name!r}; "
            f"known: {sorted(FAMILIES)}"
        )
    cfg = FAMILIES[family_name]
    d = cfg["d"]
    par = cfg["parity"]
    rows: List[Dict] = []
    for n in range(1, max_arity + 1):
        tot = d ** n
        surv = surviving_dim(d, n, par)
        rows.append({
            "n": n,
            "total_dim": tot,
            "surviving_dim": surv,
            "kernel_dim": tot - surv,
            "ratio": Fraction(surv, tot),
        })
    return rows


def print_arity_table(family_name: str, max_arity: int = 10) -> None:
    """Pretty-print the arity table for a given family."""
    cfg = FAMILIES[family_name]
    d = cfg["d"]
    par = cfg["parity"]
    rows = arity_table(family_name, max_arity)

    header = f"{'family':>8}  d={d}  parity={par}"
    print(header)
    print(f"{'n':>4}  {'total':>12}  {'surviving':>12}  {'kernel':>12}  {'ratio':>16}")
    print("-" * 64)
    for r in rows:
        ratio_str = str(r["ratio"])
        print(
            f"{r['n']:>4}  {r['total_dim']:>12}  "
            f"{r['surviving_dim']:>12}  {r['kernel_dim']:>12}  "
            f"{ratio_str:>16}"
        )
    print()


# ── main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    for fam in ("Heis", "sl2", "sl3", "Vir"):
        print_arity_table(fam, max_arity=10)
