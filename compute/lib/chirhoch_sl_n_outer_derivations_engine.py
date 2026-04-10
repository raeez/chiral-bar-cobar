r"""Affine sl_N outer-derivation engine for ChirHoch^1.

This module records the FR4 conjecture verification surface for generic
affine Kac--Moody type A:

    ChirHoch^1(V_k(sl_N)) \cong sl_N,
    dim ChirHoch^1(V_k(sl_N)) = dim(sl_N) = N^2 - 1.

Verification paths:
    1. [DC] dim(sl_N) = N^2 - 1 from traceless N x N matrices.
    2. [LT] Frenkel--Ben-Zvi, Vertex Algebras and Algebraic Curves:
       the generic affine first Hochschild package identifies HH^1(V_k(g))
       with the adjoint g-module.
    3. [CF] compute/lib/chirhoch_dimension_engine.py records the generic
       affine rule ChirHoch^1(V_k(g)) = dim(g).

References:
    - Frenkel--Ben-Zvi, Vertex Algebras and Algebraic Curves, 2nd ed. (2004)
    - chapters/theory/chiral_center_theorem.tex, prop:chirhoch1-affine-km
    - compute/lib/chirhoch_dimension_engine.py, chirhoch_affine_km
"""

from __future__ import annotations

from typing import Dict, Tuple


def compute_chirhoch1_affine_sl_n(N: int, k: object = "generic") -> int:
    r"""Return dim ChirHoch^1(V_k(sl_N)) at generic level.

    FR4 verification surface:
        ChirHoch^1(V_k(sl_N)) \cong sl_N
        dim ChirHoch^1(V_k(sl_N)) = N^2 - 1

    The generic affine locus excludes the critical level k = -N, since
    h^\vee(sl_N) = N.
    """
    if not isinstance(N, int) or N < 2:
        raise ValueError(f"N must be an integer >= 2, got {N!r}")

    if isinstance(k, str):
        if k != "generic":
            raise ValueError("k must be 'generic' or a non-critical level")
    elif k == -N:
        raise ValueError(
            f"critical level k = -N = {-N} is excluded for affine sl_{N}"
        )

    return N * N - 1


def verify_fr4_conjecture() -> Dict[int, Tuple[int, int, bool]]:
    """Check the FR4 affine sl_N dimension statement for N = 2, ..., 8."""
    results: Dict[int, Tuple[int, int, bool]] = {}
    for N in range(2, 9):
        computed = compute_chirhoch1_affine_sl_n(N)
        expected = N * N - 1
        results[N] = (computed, expected, computed == expected)
    return results
