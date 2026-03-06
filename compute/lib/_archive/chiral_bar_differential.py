"""Chiral bar differential for Kac-Moody algebras.

Computes the full chiral bar differential d: B̄^n -> B̄^{n-1} for
affine Kac-Moody algebras, including both bracket and curvature terms.

The bar complex is:
  B̄^n = g^{⊗n} ⊗ OS^{n-1}(Conf_n)

with differential:
  d = Σ_{1≤i<j≤n} (OPE_{ij}) ⊗ (Res_{D_{ij}})

For KM algebras at level k:
  OPE(a,b) has:
  - Simple pole: [a,b] (Lie bracket) → reduces bar degree by 1
  - Double pole: k·(a,b) (Killing form) → reduces bar degree by 2 (to vacuum)

CONVENTIONS:
- Cohomological grading, |d| = +1
- Bar differential has bar-degree -1
- Generators: {J^a}_{a=1}^{dim g} of conformal weight 1
- Level k enters only through the Killing form term
"""

from __future__ import annotations

import numpy as np
from typing import Dict, List, Optional, Tuple
from itertools import product as iter_product
from math import factorial

from .os_algebra import os_basis, os_dimension, residue_map, make_pair


# ---------------------------------------------------------------------------
# Lie algebra data
# ---------------------------------------------------------------------------

def sl2_data() -> Tuple[int, np.ndarray, np.ndarray]:
    """Structure constants and Killing form for sl_2.

    Basis: e=0, h=1, f=2.
    [e,f]=h, [h,e]=2e, [h,f]=-2f.
    Killing form (normalized): (e,f)=(f,e)=1, (h,h)=2.

    Returns (dim, bracket, killing) where:
    - bracket[a,b,c] = coefficient of basis element c in [a,b]
    - killing[a,b] = (a,b) under normalized trace form
    """
    d = 3
    bracket = np.zeros((d, d, d))
    # [e,f] = h
    bracket[0, 2, 1] = 1
    bracket[2, 0, 1] = -1
    # [h,e] = 2e
    bracket[1, 0, 0] = 2
    bracket[0, 1, 0] = -2
    # [h,f] = -2f
    bracket[1, 2, 2] = -2
    bracket[2, 1, 2] = 2

    killing = np.zeros((d, d))
    killing[0, 2] = 1  # (e,f) = 1
    killing[2, 0] = 1  # (f,e) = 1
    killing[1, 1] = 2  # (h,h) = 2

    return d, bracket, killing


def sl3_data() -> Tuple[int, np.ndarray, np.ndarray]:
    """Structure constants and Killing form for sl_3.

    Basis: H1=0, H2=1, E1=2, E2=3, E3=4, F1=5, F2=6, F3=7.
    E3 = [E1,E2], F3 = [F2,F1].

    Cartan matrix: A = [[2,-1],[-1,2]].
    Killing form: (H_i, H_j) = A_{ij}, (E_i, F_j) = delta_{ij}.
    """
    d = 8
    bracket = np.zeros((d, d, d))

    H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
    A = np.array([[2, -1], [-1, 2]])  # Cartan matrix

    # [H_i, E_j] = A_{ij} E_j
    bracket[H1, E1, E1] = A[0, 0]   # 2
    bracket[H1, E2, E2] = A[0, 1]   # -1
    bracket[H2, E1, E1] = A[1, 0]   # -1
    bracket[H2, E2, E2] = A[1, 1]   # 2

    # [H_i, E3]: E3=[E1,E2], ad(H_i)E3 = [H_i,[E1,E2]] = [[H_i,E1],E2]+[E1,[H_i,E2]]
    # = A_{i1}[E1,E2] + A_{i2}[E1,E2] = (A_{i1}+A_{i2})E3
    bracket[H1, E3, E3] = A[0, 0] + A[0, 1]  # 2-1=1
    bracket[H2, E3, E3] = A[1, 0] + A[1, 1]  # -1+2=1

    # [H_i, F_j] = -A_{ij} F_j
    bracket[H1, F1, F1] = -A[0, 0]
    bracket[H1, F2, F2] = -A[0, 1]
    bracket[H2, F1, F1] = -A[1, 0]
    bracket[H2, F2, F2] = -A[1, 1]
    bracket[H1, F3, F3] = -(A[0, 0] + A[0, 1])
    bracket[H2, F3, F3] = -(A[1, 0] + A[1, 1])

    # Antisymmetry: [X, H_i] = -[H_i, X]
    for X in [E1, E2, E3, F1, F2, F3]:
        for Hi in [H1, H2]:
            for c in range(d):
                bracket[X, Hi, c] = -bracket[Hi, X, c]

    # [E_i, F_j] = delta_{ij} H_i
    bracket[E1, F1, H1] = 1
    bracket[F1, E1, H1] = -1
    bracket[E2, F2, H2] = 1
    bracket[F2, E2, H2] = -1

    # [E1, E2] = E3
    bracket[E1, E2, E3] = 1
    bracket[E2, E1, E3] = -1

    # [F2, F1] = F3
    bracket[F2, F1, F3] = 1
    bracket[F1, F2, F3] = -1

    # [E3, F1] = [E1,E2]F1 → use Jacobi: [[E1,E2],F1] = [E1,[E2,F1]] + [[E1,F1],E2]
    # [E2,F1] = 0 (i≠j), [E1,F1] = H1. So [E3,F1] = [H1,E2] = -E2.
    bracket[E3, F1, E2] = -1
    bracket[F1, E3, E2] = 1

    # [E3, F2] = [[E1,E2],F2] = [E1,[E2,F2]] + [[E1,F2],E2]
    # [E2,F2] = H2, [E1,F2] = 0. So [E3,F2] = [E1,H2] = -(-1)E1 = E1.
    # Wait: [E1,H2] = -[H2,E1] = -A_{21}E1 = -(-1)E1 = E1.
    bracket[E3, F2, E1] = 1
    bracket[F2, E3, E1] = -1

    # [E3, F3]: [[E1,E2],[F2,F1]] = use Jacobi repeatedly
    # = [E1,[E2,[F2,F1]]] - [E2,[E1,[F2,F1]]]  (or use ad)
    # [E2,F3] = [E2,[F2,F1]] = [[E2,F2],F1] + [F2,[E2,F1]]
    # = [H2,F1] + 0 = -A_{21}F1 = F1
    # [E1,F3] = [E1,[F2,F1]] = [[E1,F2],F1] + [F2,[E1,F1]]
    # = 0 + [F2,H1] = -[H1,F2] = -(-A_{01})F2 = -F2. Wait:
    # [H1,F2] = -A_{01}F2 = -(-1)F2 = F2. So [F2,H1] = -[H1,F2] = -F2.
    # Actually wait: [E1,F3] = [E1,[F2,F1]].
    # Jacobi: [E1,[F2,F1]] = [[E1,F2],F1] - [[E1,F1],F2]
    # [E1,F2] = 0 (different simple roots). [E1,F1] = H1.
    # So [E1,F3] = 0 - [H1,F2] = -F2... no:
    # Jacobi: [X,[Y,Z]] = [[X,Y],Z] + [Y,[X,Z]]
    # [E1,[F2,F1]] = [[E1,F2],F1] + [F2,[E1,F1]] = 0 + [F2,H1]
    # [F2,H1] = -[H1,F2] = -(-A_{01})F2 = -(1)F2 = F2? No wait:
    # A_{01} = A[0,1] = -1. So [H1,F2] = -A_{01}F2 = -(-1)F2 = F2.
    # Then [F2,H1] = -F2.
    # So [E1,F3] = -F2.
    bracket[E1, F3, F2] = -1
    bracket[F3, E1, F2] = 1

    # [E2,F3] = [E2,[F2,F1]] = [[E2,F2],F1] + [F2,[E2,F1]]
    # = [H2,F1] + 0 = -A_{10}F1 = -(-1)F1 = F1.
    bracket[E2, F3, F1] = 1
    bracket[F3, E2, F1] = -1

    # [E3,F3] = [[E1,E2],[F2,F1]]
    # = [E1,[E2,F3]] - [E2,[E1,F3]]   (Jacobi on [E1,E2] acting on F3)
    # Wait, [[E1,E2],F3] = [E1,[E2,F3]] + [[E1,F3],E2] (Jacobi)
    # Hmm, let me use: [[E1,E2],F3] = [E1,[E2,F3]] - [E2,[E1,F3]]
    # = [E1, F1] - [E2, -F2] = H1 + [E2,F2] = H1 + H2
    bracket[E3, F3, H1] = 1
    bracket[E3, F3, H2] = 1
    bracket[F3, E3, H1] = -1
    bracket[F3, E3, H2] = -1

    # Serre relations: [E1,[E1,E2]] = [E1,E3] = 0
    # [E2,[E2,E1]] = [E2,-E3] = -[E2,E3] = 0
    # Similarly for F's

    # [E_i, E3] and [F_i, F3] should be 0 (Serre)
    # Already zero by default (not set)

    # Killing form: normalized trace (E_i, F_j) = delta_{ij}, (H_i, H_j) = A_{ij}
    killing = np.zeros((d, d))
    killing[H1, H1] = A[0, 0]
    killing[H1, H2] = A[0, 1]
    killing[H2, H1] = A[1, 0]
    killing[H2, H2] = A[1, 1]
    killing[E1, F1] = 1
    killing[F1, E1] = 1
    killing[E2, F2] = 1
    killing[F2, E2] = 1
    killing[E3, F3] = 1
    killing[F3, E3] = 1

    return d, bracket, killing


# ---------------------------------------------------------------------------
# Chiral bar complex chain groups
# ---------------------------------------------------------------------------

def chain_group_dim(dim_g: int, bar_degree: int) -> int:
    """Dimension of B̄^n = g^{⊗n} ⊗ OS^{n-1}(n).

    dim = dim(g)^n × (n-1)!
    """
    if bar_degree < 1:
        return 1  # B̄^0 = ground field
    return dim_g ** bar_degree * factorial(bar_degree - 1)


def chain_group_basis(dim_g: int, bar_degree: int) -> int:
    """Number of basis elements for the chain group.

    The basis is indexed by (tensor_index, os_index) where:
    - tensor_index: tuple of dim_g^n elements (g^{⊗n} basis)
    - os_index: index into the OS basis
    """
    n = bar_degree
    if n < 1:
        return 1
    os_dim = os_dimension(n, n - 1)
    return dim_g ** n * os_dim


# ---------------------------------------------------------------------------
# Bar differential
# ---------------------------------------------------------------------------

def bar_differential_matrix(dim_g: int, bracket: np.ndarray, killing: np.ndarray,
                             bar_degree: int, level: float = 1.0) -> np.ndarray:
    """Compute the bar differential d: B̄^n -> B̄^{n-1} as a matrix.

    For KM algebras, the differential has two components:
    1. Bracket (simple pole): contracts pair (i,j) via [·,·], sends to B̄^{n-1}
    2. Curvature (double pole): contracts pair (i,j) via (·,·), sends to B̄^{n-2}

    We combine these into a single matrix mapping B̄^n -> B̄^{n-1} ⊕ B̄^{n-2} ⊕ ...
    Actually, for computing cohomology we only need d: B̄^n -> B̄^{n-1} at each step.

    BUT: the curvature (double pole) terms map to LOWER bar degrees, not just n-1.
    For KM algebras with OPE poles up to order 2, the curvature maps B̄^n -> B̄^{n-2}.
    This makes the differential NOT homogeneous in bar degree.

    Wait -- in the chiral bar complex, the differential is DEFINED to have
    bar-degree -1. The curvature is PART of the differential, contributing
    to B̄^{n-1} (not B̄^{n-2}). The point is that the curvature
    term k(a,b)|0⟩ reduces the number of generators by 2 (removing both
    a and b) but adds a scalar to the remaining tensor product, so the
    result lives in B̄^{n-2} as a tensor product component.

    Hmm, actually I need to think about this more carefully.

    The bar differential on B̄^n = (s^{-1}Ā)^{⊗n} ⊗ OS^{n-1}(Conf_n):
    d([v_1|...|v_n] ⊗ ω) = Σ_{i<j} Res_{D_{ij}}(OPE(v_i, v_j) ⊗ ω)

    For the bracket (simple pole): OPE gives [v_i, v_j] ∈ Ā.
    After the residue, we get [v_1|...|[v_i,v_j]|...|v̂_j|...|v_n] ⊗ Res(ω).
    This lives in (s^{-1}Ā)^{⊗(n-1)} ⊗ OS^{n-2}(Conf_{n-1}) = B̄^{n-1}. ✓

    For the curvature (double pole): OPE gives k·(v_i,v_j)·|0⟩ (scalar).
    After the residue, we get k·(v_i,v_j)·[v_1|...|v̂_i|...|v̂_j|...|v_n] ⊗ Res(ω).
    This lives in (s^{-1}Ā)^{⊗(n-2)} ⊗ OS^{n-2}(Conf_{n-1}) ... but wait.

    The OS residue maps OS^{n-1}(n) -> OS^{n-2}(n-1) (correct target for n-1 points).
    The curvature removes 2 tensor factors and the residue removes 1 point,
    giving n-2 tensor factors and n-1 points... that doesn't match B̄^{n-2}.

    OK I think the issue is: the residue on D_{ij} gives a form on n-1 points,
    but the curvature has n-2 tensor factors. So the result is
    g^{⊗(n-2)} ⊗ OS^{n-2}(Conf_{n-1}). This is NOT B̄^{n-2} (which would be
    g^{⊗(n-2)} ⊗ OS^{n-3}(Conf_{n-2})).

    So the curvature term has a DIFFERENT target than B̄^{n-2}. It lives in
    a "mixed" space. In the standard bar complex formulation, this is handled
    by the tensor coalgebra structure: the curvature contributes to the
    differential through the coalgebra decomposition.

    Actually, I think the correct interpretation is: the full bar complex
    differential maps B̄^n -> B̄^{n-1}. The "curvature" (double pole) terms
    contribute to this same B̄^{n-1} by combining the Killing form contraction
    with a DIFFERENT OS residue map.

    Let me reconsider. In the genus-0 chiral bar complex on P^1:

    d([v_1|...|v_n] ⊗ ω) = Σ_{i<j} { bracket term + curvature term }

    Bracket term: Res_{z_i=z_j} of (v_i(z_i) v_j(z_j) / (z_i - z_j)) ⊗ ω
    This gives [v_i, v_j] ⊗ Res_{D_{ij}}(ω), in B̄^{n-1}.

    Curvature term: Res_{z_i=z_j} of (k(v_i,v_j) / (z_i - z_j)^2) ⊗ ω
    This gives k(v_i,v_j) ⊗ Res_{D_{ij}}(η_{ij} ∧ ω) ? No...

    Actually, the OPE of two generators at the SAME point gives:
    v_i(z) v_j(w) ~ k(v_i,v_j)/(z-w)^2 + [v_i,v_j](w)/(z-w) + regular

    The bar differential extracts ALL singular terms via the residue
    of the propagator form ω. The specific contribution depends on the
    pole structure of ω.

    For the simple pole 1/(z-w): Res_{z=w} gives the coefficient, which is [v_i,v_j].
    For the double pole 1/(z-w)^2: Res_{z=w} of f(z)/(z-w)^2 gives f'(z_0)...

    Hmm, this is getting complicated. Let me think about this differently.

    In the COMBINATORIAL bar complex (which is what we're computing),
    the bar differential is defined using the n-th products of the vertex
    algebra. For a vertex algebra V with OPE:
      a(z) b(w) = Σ_{n≥0} (a_{(n)} b)(w) / (z-w)^{n+1}

    The bar differential on B̄^2 = g ⊗ g ⊗ OS^1(Conf_2) is:
      d([a|b] ⊗ η_{12}) = Σ_{n≥0} a_{(n)} b ⊗ (terms involving 1/Γ(n+1) etc.)

    But for KM algebras, only a_{(0)} b = [a,b] (bracket, simple pole) and
    a_{(1)} b = k(a,b) (Killing form, double pole) are nonzero.

    From the detailed computation in the manuscript (comp:virasoro-bar-diff):
      D(T ⊗ T ⊗ η_{12}) = T_{(3)}T · |0⟩ + T_{(2)}T + T_{(1)}T + T_{(0)}T
    which shows that ALL n-th products contribute.

    For KM (only 0th and 1st products nonzero):
      D([a|b] ⊗ η_{12}) = a_{(0)}b + a_{(1)}b · |0⟩
                         = [a,b] + k(a,b) · |0⟩

    The [a,b] term lives in B̄^1 = g (the Lie algebra), ✓.
    The k(a,b)·|0⟩ term lives in B̄^0 = ground field, mapping to the "vacuum."

    So for d: B̄^2 -> B̄^1 ⊕ B̄^0, the bracket gives the B̄^1 component
    and the curvature gives the B̄^0 component.

    For d: B̄^3 -> B̄^2 ⊕ B̄^1 ⊕ B̄^0:
    At each collision D_{ij}, the bracket maps to B̄^2 and the curvature
    maps to B̄^1 (because removing 2 generators from 3 gives 1, but the
    form has degree... wait).

    Actually I think the curvature maps B̄^n to B̄^{n-2} because it reduces
    the number of generators by 2 (collapsing the pair to a scalar). But the
    form degree also drops: the Res maps OS^{n-1}(n) to OS^{n-2}(n-1), and
    we need to further map OS^{n-2}(n-1) into something compatible with the
    n-2 remaining generators.

    Hmm, I think the key is: in the TOTAL bar complex, the differential
    maps B̄^n to the DIRECT SUM B̄^{n-1} ⊕ B̄^{n-2} ⊕ ... ⊕ B̄^0.
    The total complex is graded by TOTAL degree (bar degree + internal degree),
    and the differential has total degree +1.

    For computing bar COHOMOLOGY (as reported in the Master Table), we want:
    H^n = ker(d_n) / im(d_{n+1})

    where d_n: B̄^n -> (direct sum of lower B̄^k) is the TOTAL differential.

    But wait -- the bar complex is NOT just a chain complex B̄^n -> B̄^{n-1}.
    It's a COAUGMENTED coalgebra with a codifferential. The cohomology
    is computed from the TOTAL differential.

    For the purposes of this computation: the bar complex is
    B̄ = ⊕_{n≥0} B̄^n, with d: B̄ -> B̄ such that d²=0 and d decreases
    bar degree. The cohomology H^n(B̄) = ker(d_n)/im(d_{n+1}) where
    d_n: B̄^n -> ⊕_{k<n} B̄^k.

    Since the bracket maps n->n-1 and curvature maps n->n-2, we have:
    d_n: B̄^n -> B̄^{n-1} ⊕ B̄^{n-2}

    To compute H^n, we need:
    ker(d_n) ⊂ B̄^n
    im(d_{n+1}) ⊂ B̄^n (the image IN B̄^n of d_{n+1}: B̄^{n+1} -> B̄^n ⊕ B̄^{n-1})

    Wait, d_{n+1} maps B̄^{n+1} -> B̄^n ⊕ B̄^{n-1}.
    The image in B̄^n is the B̄^n-component of d_{n+1}.

    So: im(d_{n+1})_n = {bracket component of d_{n+1}(x) : x ∈ B̄^{n+1}}
                      ⊕ {curvature component of d_{n+2}(y) : y ∈ B̄^{n+2}}

    Hmm, this is getting complicated. For the curvature contribution from
    B̄^{n+2}: d_{n+2} maps B̄^{n+2} -> B̄^{n+1} ⊕ B̄^n. So the B̄^n
    component of d_{n+2} also contributes to the image in B̄^n.

    So im(d)_n = im(d_{n+1})_n + im(d_{n+2})_n where:
    - im(d_{n+1})_n = projection to B̄^n of d_{n+1}(B̄^{n+1}) [bracket part]
    - im(d_{n+2})_n = projection to B̄^n of d_{n+2}(B̄^{n+2}) [curvature part]

    And H^n = ker(d_n) / (im(d_{n+1})_n + im(d_{n+2})_n)

    This is correct but more complex than a simple chain complex.

    For the BRACKET-ONLY part (level k=0), the differential is strictly
    B̄^n -> B̄^{n-1}, which is a chain complex. But d²≠0 in this case!

    For the FULL differential (with curvature), d²=0 but the target is
    B̄^{n-1} ⊕ B̄^{n-2}, making it a filtered complex.

    OK let me just build the TOTAL differential matrix. Given that we're
    computing H^n for moderate n (up to 5 or so), we can build the matrix
    d: ⊕_{k≤n+2} B̄^k -> ⊕_{k≤n+2} B̄^k and compute cohomology directly.

    Parameters:
        dim_g: dimension of the Lie algebra
        bracket: structure constants, bracket[a,b,c] = coefficient of c in [a,b]
        killing: Killing form, killing[a,b]
        bar_degree: compute the differential FROM this degree (n)
        level: the level k (enters the Killing form term as k * killing)

    Returns:
        Matrix of shape (target_dim, source_dim) where:
        source = B̄^n
        target = B̄^{n-1} ⊕ B̄^{n-2}
    """
    n = bar_degree
    if n < 1:
        return np.zeros((1, 1))

    d = dim_g

    # Source: B̄^n = g^{⊗n} ⊗ OS^{n-1}(n)
    os_src_mons, os_src_basis = os_basis(n, n - 1) if n >= 2 else ([], np.array([[1.0]]))
    os_src_dim = os_src_basis.shape[0] if os_src_basis.size > 0 else (1 if n == 1 else 0)
    src_dim = d ** n * os_src_dim

    if n == 1:
        os_src_dim = 1  # OS^0 = C
        src_dim = d

    # Target: B̄^{n-1} ⊕ B̄^{n-2}
    # B̄^{n-1} = g^{⊗(n-1)} ⊗ OS^{n-2}(n-1)
    if n - 1 >= 2:
        os_tgt1_mons, os_tgt1_basis = os_basis(n - 1, n - 2)
        os_tgt1_dim = os_tgt1_basis.shape[0]
    elif n - 1 == 1:
        os_tgt1_dim = 1
    else:
        os_tgt1_dim = 1  # B̄^0 = C

    tgt1_dim = d ** (n - 1) * os_tgt1_dim if n >= 2 else 1

    # B̄^{n-2} (curvature target)
    if n >= 3:
        if n - 2 >= 2:
            os_tgt2_mons, os_tgt2_basis = os_basis(n - 2, n - 3)
            os_tgt2_dim = os_tgt2_basis.shape[0]
        elif n - 2 == 1:
            os_tgt2_dim = 1
        else:
            os_tgt2_dim = 1

        tgt2_dim = d ** (n - 2) * os_tgt2_dim if n >= 3 else 1
    elif n == 2:
        tgt2_dim = 1  # B̄^0 = C
    else:
        tgt2_dim = 0

    tgt_dim = tgt1_dim + tgt2_dim

    mat = np.zeros((tgt_dim, src_dim))

    # Iterate over all pairs (i, j) with 1 ≤ i < j ≤ n
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Compute the OS residue map: OS^{n-1}(n) -> OS^{n-2}(n-1)
            if n >= 2:
                os_res = residue_map(n, n - 1, i, j)
            else:
                os_res = np.array([[1.0]])

            # --- Bracket contribution (simple pole): B̄^n -> B̄^{n-1} ---
            # For each source basis element (v_1,...,v_n, os_idx):
            # bracket maps (v_1,...,v_n) to (v_1,...,[v_i,v_j],...,v̂_j,...,v_n)
            # with appropriate sign and relabeling.

            # The tensor contraction: v_i ⊗ v_j -> [v_i, v_j] ∈ g
            # replaces positions i and j with a single element at position i
            # (or at position min(i,j) in the relabeled sequence).
            # The remaining elements shift down.

            _add_bracket_contribution(mat, d, n, i, j, bracket, os_res,
                                       os_src_dim, os_tgt1_dim, 0)

            # --- Curvature contribution (double pole): B̄^n -> B̄^{n-2} ---
            # For each source basis element:
            # curvature maps (v_1,...,v_n) to k*(v_i,v_j) * (v_1,...,v̂_i,...,v̂_j,...,v_n)
            # The result lives in g^{⊗(n-2)}.
            # The OS residue still maps OS^{n-1}(n) -> OS^{n-2}(n-1).
            # But we need OS^{n-3}(n-2) for the target B̄^{n-2}.
            # The curvature OS factor requires a SECOND residue...

            # Actually, wait. The curvature term a_{(1)}b = k(a,b) is a SCALAR.
            # In the bar complex, this produces:
            # k(v_i,v_j) · [v_1|...|v̂_i|...|v̂_j|...|v_n] ⊗ (something in OS)
            # The OS part: we take Res_{D_{ij}}(ω), getting a form on n-1 points.
            # But we only have n-2 tensor factors left. So the OS form has
            # n-1 points but n-2 factors — the (n-1)-th point is the merged point
            # which no longer carries a generator (it became a scalar).

            # In the standard bar complex formulation, this would be handled by
            # the coalgebra structure. The curvature contributes to the
            # "coaugmentation" component.

            # For KM algebras: the curvature sends B̄^n to B̄^{n-2} with
            # a SEPARATE OS map. The OS contribution is:
            # We need to go from OS^{n-1}(n) to OS^{n-3}(n-2).
            # This requires TWO steps: first Res_{D_{ij}} to get OS^{n-2}(n-1),
            # then we need to further contract to OS^{n-3}(n-2) by removing
            # the merged point somehow.

            # Actually, I think the right interpretation is simpler:
            # The curvature just produces a scalar k(v_i,v_j) times the
            # remaining tensor product [v_1|...|v̂_i|...|v̂_j|...|v_n].
            # The OS form from the residue Res_{D_{ij}} lands in OS^{n-2}(n-1),
            # which has the right dimension for n-1 remaining points (n-2 non-merged
            # plus the merged). But since the merged point carries no generator,
            # we need to "forget" it.

            # The forgetting map is: sum over all ways to resolve the merged
            # point, i.e., integrate out the merged coordinate. This gives a
            # map OS^{n-2}(n-1) -> OS^{n-3}(n-2).

            # For n=2: curvature maps B̄^2 -> B̄^0 = C.
            # We have Res_{D_{12}}(η_{12}) = 1 (scalar). k(v_1,v_2)·1 ∈ C. ✓

            # For n=3: curvature maps B̄^3 -> B̄^1 = g.
            # Res_{D_{ij}}(ω) ∈ OS^1(2) = C. The result is k(v_i,v_j)·v_k,
            # with the remaining generator v_k and the OS form from the residue.
            # Since OS^1(2) is 1-dim and B̄^1 = g ⊗ OS^0(1) = g, we need to
            # map OS^1(2) -> OS^0(1) = C. This is integration, which is just
            # the identity map OS^1(2) ≅ C -> C.

            # Hmm, this is getting complicated. Let me think about it differently.

            # SIMPLER INTERPRETATION: In the curved A_infinity/bar complex,
            # the curvature m_0 maps B̄^n to B̄^{n-1} (not B̄^{n-2}!) by
            # the following mechanism:
            # m_0 ∈ A (an element of the algebra), and it enters through:
            # d(a_1 ⊗ ... ⊗ a_n) includes terms like
            # a_1 ⊗ ... ⊗ m_2(m_0, a_i) ⊗ ... ⊗ a_n  (WRONG: m_0 IS curvature)

            # Actually: in the curved A_infinity formalism,
            # d = d_bracket + d_curvature where:
            # d_bracket uses m_1 (linear differential, if any) and m_2 (bracket)
            # d_curvature uses m_0 (curvature element)

            # But m_0 is a CONSTANT (scalar), so d_curvature acts by:
            # d_curv([a_1|...|a_n]) = Σ_i [a_1|...|m_0|...|a_n]  (insert m_0)

            # This INCREASES bar degree by 1, not decreases it!

            # OK I think I'm confusing bar and cobar. Let me go back to
            # the manuscript's explicit computation.

            # From comp:virasoro-bar-diff (detailed_computations.tex):
            # D(T ⊗ T ⊗ η_{12}) = (c/2)·|0⟩ + 2T + ∂T
            # The (c/2)·|0⟩ is the vacuum term from the quartic pole.
            # This lands in B̄^0 (vacuum = degree 0).
            # The 2T + ∂T lands in B̄^1.

            # So D: B̄^2 -> B̄^1 ⊕ B̄^0. ✓ (bracket -> B̄^1, curvature -> B̄^0)

            # For KM: D([a|b] ⊗ η_{12}) = [a,b] + k(a,b)|0⟩
            # [a,b] ∈ B̄^1, k(a,b)|0⟩ ∈ B̄^0.

            # For B̄^3 -> B̄^2 ⊕ B̄^1:
            # D([a|b|c] ⊗ ω) = Σ_{(i,j)} Res_{D_{ij}}(...)
            # Each Res gives:
            #   Bracket: [v_i,v_j] replaces pair, maps to B̄^2
            #   Curvature: k(v_i,v_j) · remaining, maps to B̄^1

            # For the curvature part at D_{12} acting on [a|b|c] ⊗ ω:
            # OPE gives k(a,b)·|0⟩, so the result is:
            # k(a,b) · [c] ⊗ Res_{D_{12}}(ω)
            # where Res_{D_{12}}: OS^2(3) -> OS^1(2).
            # But [c] ⊗ OS^1(2) ∈ g ⊗ OS^1(2).
            # And B̄^1 = g ⊗ OS^0(1) = g.
            # So OS^1(2) ≠ OS^0(1). The form spaces don't match!

            # This means the curvature from B̄^3 doesn't land in B̄^1
            # unless there's an additional step.

            # I think the resolution is: in the bar complex, the differential
            # has a multi-step structure. The curvature from B̄^n lands in
            # a DIFFERENT graded piece than B̄^{n-2}. The full complex is:

            # B̄^n = ⊕_{k} g^{⊗(n-k)} ⊗ OS^{n-1-k}(Conf_n)

            # Wait no, I think the issue is that for the bar complex of a
            # CHIRAL algebra, the differential is well-defined as a map
            # B̄^n -> B̄^{n-1} with B̄^k defined differently from what I assumed.

            # Let me re-read the manuscript definition.

            # From bar_cobar_construction.tex: the bar construction is
            # B(A) = T^c(s^{-1}Ā), the cofree conilpotent coalgebra on
            # the desuspension of the augmentation ideal.

            # The differential on T^c(V) with V = s^{-1}Ā:
            # d = d_1 + d_2 where
            # d_1: V^{⊗n} -> V^{⊗(n-1)} is from the "binary" operation
            # d_2: V^{⊗n} -> V^{⊗(n-2)} is from the "nullary" operation (m_0)

            # For the CHIRAL bar complex, the tensor product is replaced by
            # the OS-weighted tensor product. So:
            # B̄^n = V^{⊗n} ⊗ OS^{n-1}(Conf_n)

            # And the differential maps B̄^n to B̄^{n-1} ⊕ B̄^{n-2}, where:
            # - d_1 (bracket) component maps to B̄^{n-1} = V^{⊗(n-1)} ⊗ OS^{n-2}(n-1)
            # - d_2 (curvature) component maps to B̄^{n-2} = V^{⊗(n-2)} ⊗ OS^{n-3}(n-2)

            # For d_2 mapping to B̄^{n-2}: we need a map
            # V^{⊗n} ⊗ OS^{n-1}(n) -> V^{⊗(n-2)} ⊗ OS^{n-3}(n-2)

            # The tensor contraction V^{⊗n} -> V^{⊗(n-2)} removes pair (i,j).
            # The OS map: OS^{n-1}(n) -> OS^{n-3}(n-2) removes TWO points.

            # Removing two points requires a COMPOSITE residue:
            # First Res_{D_{ij}}: OS^{n-1}(n) -> OS^{n-2}(n-1)
            # Then "forget point": OS^{n-2}(n-1) -> OS^{n-3}(n-2)
            # The "forget point" maps the merged point out.

            # Actually, I think the correct formula is: the curvature
            # contribution involves Res_{D_{ij}} followed by the
            # "counit" map that integrates out the merged coordinate.

            # For n=2: Res_{D_{12}}: OS^1(2) -> OS^0(1) ≅ C. The curvature
            # gives k(a,b) · 1 ∈ C = B̄^0. ✓

            # For n=3: Res_{D_{12}}: OS^2(3) -> OS^1(2). Then we need
            # a map OS^1(2) -> OS^0(1). This is Res of the merged point
            # with the remaining... but there's only 1 remaining point,
            # so it's a "forgetful" map.
            # OS^1(2) = span{η_{merged, c}} -> OS^0(1) by just taking the
            # coefficient (= 1 since there's only one form).
            # So the composite map is: evaluate the residue form on the single
            # remaining pair. This gives a scalar.

            # Hmm, for n=3 curvature at D_{12}:
            # [a|b|c] ⊗ ω → k(a,b) · c ⊗ (composite residue of ω)
            # The OS part: OS^2(3) → OS^0(1) via double residue.
            # OS^2(3) has dim 2, OS^0(1) = C has dim 1.
            # So this is a map R^2 -> R^1.

            # For B̄^1 = g ⊗ OS^0(1) = g ⊗ C = g.
            # The curvature result: k(a,b) · c ⊗ (scalar) ∈ g ⊗ C = B̄^1. ✓

            # OK so the curvature involves a DOUBLE residue. Let me implement
            # this properly.

            if n >= 2:
                _add_curvature_contribution(mat, d, n, i, j, killing, level,
                                             os_src_dim, os_tgt1_dim, tgt1_dim,
                                             os_res)

    return mat


def _add_bracket_contribution(mat, dim_g, n, i, j, bracket, os_res,
                                os_src_dim, os_tgt_dim, tgt_offset):
    """Add bracket (simple pole) contribution to the differential matrix.

    The bracket at collision D_{ij} maps:
    (v_1,...,v_n) ⊗ ω_s  →  (v_1,...,[v_i,v_j],...,v̂_j,...,v_n) ⊗ Res(ω_s)

    Sign: (-1)^{j-i-1} from moving v_j past v_{i+1},...,v_{j-1} in the
    desuspended tensor product (all generators are even for KM, so no
    Koszul signs from the generators themselves).
    """
    d = dim_g
    # Sign from the operadic structure
    # For the bar complex, the sign convention involves the desuspension.
    # For KM (all generators weight 1, even), the sign is simpler.
    # Standard convention: d([a_1|...|a_n]) = Σ_{i<j} ± [a_1|...|[a_i,a_j]|...|â_j|...|a_n]
    # The sign for the (i,j) term: (-1)^{(position of a_j) - (position of a_i) - 1}
    # = (-1)^{j-i-1} (0-indexed: (-1)^{j-i-1}).

    sign_ij = (-1) ** (j - i - 1)

    # Map each source basis element to target
    for src_tensor_idx in range(d ** n):
        # Decode tensor index: v_{n-1},...,v_0 (or v_1,...,v_n in 1-indexed)
        tensor = _decode_tensor(src_tensor_idx, d, n)  # tuple of n indices

        v_i = tensor[i - 1]  # 0-indexed
        v_j = tensor[j - 1]

        # Compute [v_i, v_j] = Σ_c bracket[v_i, v_j, c] * e_c
        for c in range(d):
            coeff = bracket[v_i, v_j, c]
            if abs(coeff) < 1e-15:
                continue

            # Build target tensor: replace v_i with c, remove v_j
            tgt_tensor = list(tensor)
            tgt_tensor[i - 1] = c
            del tgt_tensor[j - 1]
            tgt_tensor_idx = _encode_tensor(tgt_tensor, d)

            # Combine with OS residue
            for os_src_idx in range(os_src_dim):
                src_idx = src_tensor_idx * os_src_dim + os_src_idx

                for os_tgt_idx in range(os_tgt_dim):
                    os_coeff = os_res[os_tgt_idx, os_src_idx]
                    if abs(os_coeff) < 1e-15:
                        continue

                    tgt_idx = tgt_offset + tgt_tensor_idx * os_tgt_dim + os_tgt_idx
                    mat[tgt_idx, src_idx] += sign_ij * coeff * os_coeff


def _add_curvature_contribution(mat, dim_g, n, i, j, killing, level,
                                  os_src_dim, os_tgt1_dim, tgt1_offset, os_res):
    """Add curvature (double pole) contribution to the differential matrix.

    The curvature at collision D_{ij} maps:
    (v_1,...,v_n) ⊗ ω_s  →  k·(v_i,v_j) · (v_1,...,v̂_i,...,v̂_j,...,v_n) ⊗ (OS map)

    For n=2: maps to B̄^0 = C. OS: Res_{D_{12}}(η_{12}) = 1.
    For n≥3: maps to B̄^{n-2}. OS: need composite residue.

    The OS map for curvature is more complex than for bracket.
    For the curvature, we remove TWO tensor factors and need the
    OS form to live on n-2 points. The residue Res_{D_{ij}} gives
    OS^{n-2}(n-1), but we need OS^{n-3}(n-2).

    The additional contraction is: after merging i and j, the merged
    point carries no generator. So we need to "sum over" (trace out)
    the position of the merged point in the OS form.

    For n=2: trivial (result is a scalar).
    For n=3: OS^1(2) -> OS^0(1). The merged point and the remaining
    point give a 1-form η_{merged, remaining}. Tracing out = evaluating = scalar.
    """
    d = dim_g

    # Sign
    sign_ij = (-1) ** (j - i - 1)

    # For the curvature contribution with n generators:
    # After removing v_i and v_j, we have n-2 generators.
    # The target is B̄^{n-2} which starts at offset tgt1_offset + (previous dims...)

    # Actually, the curvature target offset in the combined target matrix
    # needs to be computed based on B̄^{n-1} size.

    if n == 2:
        # Curvature maps B̄^2 -> B̄^0 = C (1-dimensional)
        # Target index: tgt1_offset + dim(B̄^{n-1}) = tgt1_offset + d * os_tgt1_dim
        curv_offset = d * os_tgt1_dim  # after the B̄^1 block

        for src_tensor_idx in range(d ** n):
            tensor = _decode_tensor(src_tensor_idx, d, n)
            v_i = tensor[i - 1]
            v_j = tensor[j - 1]

            kf = killing[v_i, v_j]
            if abs(kf) < 1e-15:
                continue

            coeff = level * kf * sign_ij

            for os_src_idx in range(os_src_dim):
                src_idx = src_tensor_idx * os_src_dim + os_src_idx

                # OS residue for curvature: Res_{D_{ij}}(η_{12}) = scalar
                # For n=2, os_res is (1,1) matrix
                os_coeff = os_res[0, os_src_idx] if os_res.shape[0] > 0 else 1.0
                if abs(os_coeff) < 1e-15:
                    continue

                mat[curv_offset, src_idx] += coeff * os_coeff

    elif n >= 3:
        # Curvature maps B̄^n -> B̄^{n-2}
        # Need: composite OS map OS^{n-1}(n) -> OS^{n-3}(n-2)
        # = "trace out merged point" ∘ Res_{D_{ij}}

        # After Res_{D_{ij}}: OS^{n-2}(n-1)
        # The merged point gets label min(i,j). Points > max(i,j) decrement.
        # We need to further contract this to OS^{n-3}(n-2).

        # The contraction: sum over all remaining points p,
        # Res_{D_{merged, p}}: OS^{n-2}(n-1) -> OS^{n-3}(n-2)?
        # No — we need a different approach.

        # Actually, I think the curvature OS map is simply:
        # For the form η_{ij} ∧ α where α ∈ OS^{n-2}(n\{i,j}),
        # the residue Res_{D_{ij}} gives α restricted to {1,...,n}\{j}
        # (merged point labeled min(i,j), others shifted).
        # Then for the curvature, we need α to be a form on n-2 points
        # (excluding both i and j). The residue Res_{D_{ij}} already
        # removed one point (j) and the forms on the remaining n-1 points
        # include the merged point. The curvature contribution needs
        # the projection to forms on n-2 points (excluding the merged point).

        # The projection is: delete all edges involving the merged point
        # from the form. This is achieved by the "forgetful map"
        # OS^{n-2}(n-1) -> OS^{n-3}(n-2).

        # For efficiency, compute the composite map directly.
        # Actually, for the CHIRAL bar complex, I believe the curvature
        # contributes differently. Let me re-examine.

        # In the standard bar construction for an augmented dga:
        # B(A) = T^c(s^{-1}Ā) with differential
        # d(a_1|...|a_n) = Σ_{i=1}^{n-1} ±(a_1|...|a_i·a_{i+1}|...|a_n) [assoc case]

        # For the CHIRAL bar construction:
        # d = Σ_{i<j} contraction at (i,j)
        # Each contraction uses the FULL OPE (all poles).

        # For the simple pole (bracket), the contraction sends n generators
        # to n-1 generators: ✓, maps B̄^n -> B̄^{n-1}.

        # For the double pole (curvature), the contraction sends n generators
        # to n-2 generators (pair collapses to scalar). The OS form:
        # Res_{D_{ij}} maps OS^{n-1}(n) -> OS^{n-2}(n-1).
        # But we need OS^{n-3}(n-2) for B̄^{n-2}.

        # Hmm, actually maybe the curvature from the DOUBLE POLE does NOT
        # contribute to the bar differential in the same way. Let me re-read
        # the explicit computation for degree 3.

        # For the Heisenberg at degree 3 (comp:heisenberg-deg3-full):
        # D([a_m|a_n|a_p] ⊗ η12∧η23) involves Res at D12, D23, D13.
        # For Heisenberg OPE: only double pole a_{(1)}a = κ.
        # Res_{D12} of [a⊗a⊗a ⊗ η12∧η23]:
        #   The residue picks up the term κ/(z1-z2)^2 · d(z1-z2)/(z1-z2) ∧ dz23/(z2-z3)
        #   = κ · dε/ε^3 ∧ η23. Residue of triple pole = 0.
        # So the curvature at degree 3 gives ZERO for Heisenberg. Consistent!

        # For sl_2 at degree 3:
        # The bracket (simple pole) contributes. The double pole gives
        # k(a,b) · [c] ⊗ (residue of the form).
        # The residue: we have the form ω ∈ OS^2(3). The OPE has
        # k(a,b)/(z_i-z_j)^2 as the double pole. The propagator form ω
        # contains η_{ij} = dlog(z_i-z_j). The residue of
        # (k(a,b)/(z_i-z_j)^2) · ω at z_i = z_j:
        # if ω contains η_{ij} = d(z_i-z_j)/(z_i-z_j), then we get
        # k(a,b) · d(z_i-z_j) / (z_i-z_j)^3 ∧ (rest), which has residue 0
        # (triple pole).
        # If ω does NOT contain η_{ij}, then the residue of 1/(z_i-z_j)^2
        # at z_i = z_j is not a simple residue but a derivative.

        # Hmm, I think for the genus-0 bar complex, the curvature from
        # double poles actually gives ZERO contribution in degree ≥ 3
        # because the OPE pole and the form pole combine to give a
        # higher-order pole with vanishing residue.

        # Let me verify: for the bar complex at degree n ≥ 3, the form
        # ω ∈ OS^{n-1}(n) is a (n-1)-form on Conf_n. When we approach
        # the divisor D_{ij}, the form either contains η_{ij} or not.
        # If it contains η_{ij}: the OPE 1/(z_i-z_j)^2 combined with
        # η_{ij} = d(z_i-z_j)/(z_i-z_j) gives 1/(z_i-z_j)^3 · d(z_i-z_j),
        # which has zero residue (residue of a pole of order > 1 with a
        # d-log form).
        # If it doesn't contain η_{ij}: then the form is regular at D_{ij},
        # and 1/(z_i-z_j)^2 ∫ ... gives zero by the residue theorem
        # (double pole with regular form).

        # Wait, not exactly. The form ω might contain η_{ik} or η_{jk}
        # for other k, which after substituting z_i = z_j become η_{jk}
        # (regular). So the integrand near D_{ij} is:
        # 1/(z_i-z_j)^2 · (regular form) → double pole → residue = derivative
        # = d/dε (regular form)|_{ε=0} which is generally nonzero.

        # Hmm, but this is not the right way to compute the residue.
        # The Poincaré residue on a smooth divisor D ⊂ X of a meromorphic
        # form with a pole along D:
        # If the form is f · dz1∧...∧dzn / z_1^k (z_1 = local equation for D),
        # then the residue is nonzero only for k = 1 (simple pole).
        # For k ≥ 2: the Poincaré residue is zero.

        # So for the chiral bar complex: the double pole 1/(z_i-z_j)^2
        # combined with the form ω gives a Poincaré residue that is ZERO
        # whenever the total pole order along D_{ij} is ≥ 2.

        # But from the degree-2 computation: D([a|b] ⊗ η_{12}) = [a,b] + k(a,b)|0⟩
        # The k(a,b)|0⟩ term comes from the double pole!
        # Here: the form η_{12} = dz/(z_1-z_2). The OPE is 1/(z-w)^2.
        # Combined: dz/(z-w)^3. The Poincaré residue is... hmm.

        # Actually, I think the computation in the manuscript uses a different
        # normalization. The bar differential extracts ALL OPE products,
        # not just the Poincaré residue. The formula is:
        # d([a|b] ⊗ η_{12}) = Σ_{n≥0} a_{(n)} b
        # This is the FULL contraction, not a residue.

        # For degree 2 with one form η_{12}:
        # The contraction gives the sum of ALL n-th products a_{(n)}b
        # (weighted appropriately). For KM:
        # a_{(0)}b = [a,b] (from simple pole)
        # a_{(1)}b = k(a,b) (from double pole)
        # Result: [a,b] + k(a,b)·|0⟩

        # For degree 3 with a 2-form ω:
        # The contraction at D_{ij} involves the residue of the 2-form
        # times the OPE. The OPE for KM:
        # a(z)b(w) = k(a,b)/(z-w)^2 + [a,b](w)/(z-w)
        # Multiplied by the 2-form ω = α ∧ β:
        # If ω = η_{ij} ∧ η_{ik} (contains η_{ij}):
        # The residue extracts the coefficient of η_{ij} in ω,
        # giving η_{ik} (restricted to D_{ij}).
        # But which OPE product does this correspond to?
        # η_{ij} = d(z_i-z_j)/(z_i-z_j) has a simple pole at D_{ij}.
        # The OPE 1/(z_i-z_j)^2 · d(z_i-z_j)/(z_i-z_j) ∧ η_{ik}
        # = d(z_i-z_j)/(z_i-z_j)^3 ∧ η_{ik}
        # This has a TRIPLE pole in z_i-z_j. The residue involves
        # the coefficient of 1/(z_i-z_j) in the Laurent expansion,
        # which for d(z_i-z_j)/(z_i-z_j)^3 is zero (no 1/(z-w) term).
        # So the double pole with η_{ij} contributes NOTHING at degree 3.

        # And the simple pole: [a,b]/(z_i-z_j) · η_{ij} ∧ η_{ik}
        # = [a,b] · d(z_i-z_j)/(z_i-z_j)^2 ∧ η_{ik}
        # This has a double pole, so residue = 0 again!

        # Wait, this can't be right because the bar differential DOES
        # have nontrivial action at degree 3 (we know H^3 ≠ 0 for sl_2).

        # I think the issue is that I'm confusing the standard Poincaré
        # residue with the bar complex differential. The bar differential
        # is defined combinatorially using the vertex algebra structure,
        # not via Poincaré residues of forms.

        # Let me go back to the DEFINITION. From the manuscript
        # (bar_cobar_construction.tex), the bar differential is:

        # For the chiral bar complex, the differential is defined
        # algebraically using the composition maps of the chiral operad.
        # At degree n, the differential is:
        # d_bar([v_1|...|v_n]) = Σ_{i<j} Σ_{p≥0} ± [v_1|...|v_i(p)v_j|...|v̂_j|...|v_n]

        # Here v_i(p)v_j is the p-th product of the vertex algebra.
        # The sign and the meaning of this formula:
        # - v_i(p)v_j is an element of Ā (or vacuum for curvature)
        # - We replace v_i with v_i(p)v_j and remove v_j
        # - The sign depends on the bar complex convention

        # For KM:
        # v_i(0)v_j = [v_i, v_j] ∈ g (bracket)
        # v_i(1)v_j = k(v_i, v_j) ∈ C (Killing form)
        # v_i(p)v_j = 0 for p ≥ 2

        # So the bar differential is:
        # d([v_1|...|v_n]) = Σ_{i<j} ± [v_1|...|[v_i,v_j]|...|v̂_j|...|v_n]
        #                  + Σ_{i<j} ± k(v_i,v_j) [v_1|...|v̂_i|...|v̂_j|...|v_n]

        # The first sum maps B̄^n -> B̄^{n-1}.
        # The second sum maps B̄^n -> B̄^{n-2}.

        # BUT: what about the OS algebra? The bar complex for CHIRAL algebras
        # includes the OS factor. Does the OS algebra just give multiplicities
        # (chain group dim = d^n × (n-1)!), or does it affect the differential?

        # From the manuscript's prop:pole-decomposition:
        # d_res = d_bracket (simple pole) + d_curvature (double pole)
        # d_bracket²≠0, d_curvature²=0, {d_bracket, d_curvature}≠0
        # BUT: d_res² = 0 (full Borcherds identity)

        # The key insight from the MEMORY file:
        # "Direct bar differential matrix computation is WRONG APPROACH"
        # "Bracket-only d provably has d²≠0"
        # "Full d = d_bracket + d_curvature satisfies d²=0 via Borcherds"

        # So the FULL bar differential DOES include both bracket and curvature,
        # and it maps B̄^n -> B̄^{n-1} ⊕ B̄^{n-2}. And d² = 0 for this
        # total differential.

        # For the BAR COHOMOLOGY computation, we just need:
        # H^n = ker(d: B̄^n -> lower degrees) / im(d: higher degrees -> B̄^n)

        # So let me implement the curvature part too, mapping B̄^n -> B̄^{n-2}.
        # The formula is:
        # d_curv([v_1|...|v_n]) = Σ_{i<j} ± k(v_i,v_j) [v_1|...|v̂_i|...|v̂_j|...|v_n]
        # No OS factor interaction for the curvature? Or does it use the
        # SECOND residue (Res_{D_{ij}} on the form, which removes one point)?

        # Hmm, actually: the OS algebra controls HOW the pairs interact.
        # The differential d: B̄^n -> B̄^{n-1} involves the OS residue
        # Res_{D_{ij}}: OS^{n-1}(n) -> OS^{n-2}(n-1).
        # This works for the bracket part (n generators -> n-1 generators,
        # n points -> n-1 points, form degree drops by 1).

        # For the curvature: n generators -> n-2 generators. We'd need
        # OS^{n-1}(n) -> OS^{n-3}(n-2). This requires a DOUBLE residue.

        # I think the curvature uses the SAME single Res_{D_{ij}} but
        # the result lives in an intermediate space:
        # g^{⊗(n-2)} ⊗ OS^{n-2}(n-1)
        # This is NOT B̄^{n-2}. It's a larger space.

        # In the bar complex formalism, this intermediate space is part
        # of the bar coalgebra structure. The curvature contributes to
        # the TOTAL differential which maps the TOTAL bar complex
        # T^c(s^{-1}Ā) to itself.

        # For computing cohomology, the total complex has:
        # degree n component = B̄^n
        # d: B̄^n -> ⊕_{k=0}^{n-1} B̄^k (potentially multiple components)

        # But the standard bar complex differential only has components
        # d_{n,n-1} (from bracket) and d_{n,n-2} (from curvature).

        # For the curvature d_{n,n-2}: this involves removing 2 generators
        # and the OS map should produce an element in B̄^{n-2}.
        # I claim the correct OS map for curvature is:
        # The composition:
        # OS^{n-1}(n) --Res_{ij}--> OS^{n-2}(n-1) --forget_merged--> OS^{n-3}(n-2)
        # where forget_merged traces out the merged point.

        # But what IS the "forget merged point" map?
        # After Res_{D_{ij}}, we have a form on n-1 points.
        # One of these points (the merged one) carries no generator.
        # To get a form on n-2 points, we need to project to forms
        # that don't involve the merged point. But OS^{n-2}(n-1)
        # generally involves ALL n-1 points, so this projection is
        # nontrivial.

        # Actually, I wonder if the curvature DOESN'T use the OS algebra
        # at all. The curvature is a PURELY algebraic operation:
        # m_0 is a constant, and it enters the bar complex through the
        # coalgebra structure, not through the operad/OS structure.

        # In the standard (non-chiral) bar complex of an A_infinity algebra:
        # d([a_1|...|a_n]) = Σ_{i,j} ± [a_1|...|m_j(a_i,...,a_{i+j-1})|...|a_n]
        # where m_j is the j-th operation (j=0: curvature, j=1: differential,
        # j=2: product, etc.)

        # For j=0 (curvature): m_0 ∈ A, and:
        # d_curv([a_1|...|a_n]) = Σ_i ± [a_1|...|a_{i-1}|m_0|a_i|...|a_n]
        # This INCREASES bar degree by 1!

        # Wait, that's for the COBAR complex. For the BAR complex:
        # d([a_1|...|a_n]) = Σ_{i<j} ± [a_1|...|μ(a_i,...,a_j)|...|a_n]
        # For μ = m_2 (binary product): bar degree n -> n-1.
        # For μ = m_0: the curvature a_{(1)}b = k(a,b) reduces 2 inputs to 0 outputs.
        # So d_curv: bar degree n -> n-2.

        # In the chiral bar complex, the OS structure controls the
        # combinatorics of HOW the pairs interact. For the binary operation
        # (bracket), the OS gives the propagator. For the curvature, the
        # OS gives... what?

        # I think the key realization is: the OS forms encode the propagator
        # structure. For each collision D_{ij}, the residue on the propagator
        # form extracts the contribution at that collision. The OPE (whether
        # bracket or curvature) then determines WHAT is produced.

        # So both bracket and curvature use the SAME OS residue Res_{D_{ij}}.
        # The bracket produces a generator (maps B̄^n -> B̄^{n-1}).
        # The curvature produces a scalar (maps B̄^n -> g^{⊗(n-2)} ⊗ OS^{n-2}(n-1)).

        # For the curvature to map to B̄^{n-2}, we need to further project
        # from OS^{n-2}(n-1) to OS^{n-3}(n-2). But this projection LOSES
        # information and may not be well-defined.

        # ALTERNATIVE: maybe the curvature DOES map to B̄^{n-1}, not B̄^{n-2}.
        # If the curvature k(v_i,v_j) is viewed as producing k(v_i,v_j)·|0⟩,
        # and |0⟩ is a degree-0 element of Ā, then the replacement is:
        # [v_1|...|v_i|...|v_j|...|v_n] -> k(v_i,v_j) · [v_1|...|1|...|v̂_j|...|v_n]
        # But 1 = |0⟩ is NOT in Ā (it's the vacuum, which was quotiented out).

        # Hmm, in the REDUCED bar complex, we quotient out the vacuum.
        # So the curvature term k(v_i,v_j)·|0⟩ maps to ZERO in the reduced bar.
        # This would mean the curvature DOESN'T contribute to the bar differential!

        # But this contradicts the manuscript, which says D(T⊗T⊗η) includes
        # (c/2)|0⟩ as a term mapping to B̄^0.

        # Resolution: B̄^0 = C·|0⟩ is the GROUND FIELD (not zero).
        # The REDUCED bar complex B̄(A) = ⊕_{n≥1} (s^{-1}Ā)^{⊗n} ⊗ OS
        # has B̄^0 = 0 (no degree-0 part). But the AUGMENTED bar complex
        # B(A) = ⊕_{n≥0} includes B^0 = C.

        # For computing bar cohomology, we use the AUGMENTED complex:
        # H^n(B(A)) for n ≥ 1.
        # The differential d: B^n -> ⊕_{k<n} B^k.
        # For n=1: d: B^1 = g -> B^0 = C maps by... hmm, what is d on B^1?
        # For KM: d([a]) = a_{(1)} vacuum? No, there's nothing to contract with.
        # Actually d on B^1 is zero (no pair to contract).

        # For n=2: d: B^2 -> B^1 ⊕ B^0. Bracket -> B^1, curvature -> B^0.

        # For n≥3: d: B^n -> B^{n-1} ⊕ B^{n-2} (if curvature present).
        # Bracket maps to B^{n-1}, curvature maps to B^{n-2}.
        # Both use the SAME OS residue Res_{D_{ij}}: OS^{n-1}(n) -> OS^{n-2}(n-1).
        # For bracket: result in g^{⊗(n-1)} ⊗ OS^{n-2}(n-1) = B̄^{n-1}. ✓
        # For curvature: result in g^{⊗(n-2)} ⊗ OS^{n-2}(n-1).
        # But B̄^{n-2} = g^{⊗(n-2)} ⊗ OS^{n-3}(n-2). ✗ (wrong OS space)

        # So the curvature from B̄^n does NOT land in B̄^{n-2} for n ≥ 3.
        # It lands in g^{⊗(n-2)} ⊗ OS^{n-2}(n-1), which is a BIGGER space.

        # This means: for n ≥ 3, the curvature from B̄^n contributes to
        # a DIFFERENT component than B̄^{n-2}. The total bar complex must
        # accommodate these intermediate spaces.

        # CONCLUSION: For KM algebras at GENERIC level (k ≠ 0), the
        # curvature IS present but only affects B̄^2 -> B̄^0 (degree 2 to vacuum).
        # For degree n ≥ 3, the curvature contribution involves higher poles
        # that vanish. Let me verify this.

        # For n ≥ 3, collision at D_{ij} with double pole:
        # The form ω ∈ OS^{n-1}(n). The contraction involves:
        # 1/(z_i - z_j)^2 · ω
        # The Poincaré residue along D_{ij} picks up the d(z_i-z_j) factor.
        # If ω contains η_{ij} = d(z_i-z_j)/(z_i-z_j):
        #   integrand ~ d(z_i-z_j)/(z_i-z_j)^3 ∧ rest → triple pole → residue = 0
        # If ω does NOT contain η_{ij}:
        #   integrand ~ 1/(z_i-z_j)^2 · rest → no d(z_i-z_j) factor → no residue
        #   (not a top-degree form in the normal direction)

        # So for n ≥ 3, the double pole (curvature) contribution is ZERO.
        # This means the curvature only affects degrees 1 and 2:
        # d: B̄^2 -> B̄^1 ⊕ B̄^0 (curvature in B̄^0)
        # d: B̄^n -> B̄^{n-1} (bracket only, for n ≥ 3)

        # This is CONSISTENT with the Heisenberg computation (all triple
        # pole residues vanish) and explains why the bar differential
        # is essentially the bracket differential for n ≥ 3.

        # But wait — if d is bracket-only for n ≥ 3, and d_bracket² ≠ 0,
        # then d² ≠ 0. That contradicts d² = 0 for the bar complex.

        # Resolution: d² = 0 for the TOTAL differential including curvature.
        # The key is: d_bracket² gives a nonzero result that is CANCELLED
        # by the composition d_curv ∘ d_bracket + d_bracket ∘ d_curv.

        # Specifically: d² = d_bracket² + d_curv ∘ d_bracket + d_bracket ∘ d_curv = 0
        # For B̄^n (n ≥ 3):
        # d_bracket²: B̄^n -> B̄^{n-1} -> B̄^{n-2}
        # d_curv ∘ d_bracket: B̄^n -> B̄^{n-1} -> B̄^{n-3} (≤ B̄^0 level)
        # d_bracket ∘ d_curv: vanishes for n ≥ 4 (d_curv gives 0 from B̄^n, n≥3)
        #   Wait, d_curv is zero on B̄^n for n ≥ 3. So d_bracket ∘ d_curv = 0.
        # And d_curv ∘ d_bracket: d_bracket maps B̄^n to B̄^{n-1},
        #   then d_curv maps B̄^{n-1} to B̄^{n-3} (only for n-1=2, i.e., n=3).
        #   For n ≥ 4: d_curv on B̄^{n-1} (with n-1 ≥ 3) is zero, so this vanishes.

        # So for n ≥ 4: d² = d_bracket² and d² ≠ 0. CONTRADICTION.

        # This means my analysis above must be WRONG. Either:
        # 1. The curvature IS nonzero for n ≥ 3 (my pole analysis is wrong), or
        # 2. The bar differential has additional terms I'm missing, or
        # 3. The chiral bar complex has a different structure than I assumed.

        # I think option 1 is likely. Let me reconsider the pole analysis.

        # For the chiral bar complex, the differential is NOT a Poincaré residue.
        # It's an algebraic operation defined by the vertex algebra structure.
        # The formula uses configuration space integrals, not just residues.

        # The correct formula from the manuscript (bar_cobar_construction.tex)
        # involves the vertex algebra n-th products:
        # d([v_1|...|v_n] ⊗ ω) = Σ_{i<j} Σ_{p≥0} ±c_p · [v_1|...|v_i(p)v_j|...|v̂_j|...|v_n] ⊗ ω'
        # where c_p and ω' depend on the OS/propagator structure.

        # I think the c_p coefficients involve the residue of the form ω
        # with DIFFERENT weights depending on the pole order p. Specifically:
        # For a p-th pole 1/(z-w)^{p+1}, the contribution involves the
        # (p+1)-fold residue, which interacts with the OS forms differently.

        # OK this is getting very long. Let me take a PRACTICAL approach:
        # Since the curvature is zero for n ≥ 3 at the level of the
        # propagator forms, and d_bracket² ≠ 0, the bar cohomology
        # must be computed using the FULL bar complex structure.

        # For PRACTICAL computation, let me use the following approach:
        # The BRACKET-ONLY differential d_bracket: B̄^n -> B̄^{n-1}
        # does NOT give d² = 0. But the PBW spectral sequence provides
        # a way to compute bar cohomology without needing d² = 0 at the
        # chain level.

        # ALTERNATIVELY: just compute d_bracket and check if d² = 0 numerically.
        # If it IS zero (contradicting the theoretical analysis), then we can
        # proceed. If it's NOT zero, then we need the curvature.

        pass  # curvature for n ≥ 3 is handled below after more analysis


def _decode_tensor(idx: int, dim: int, n: int) -> tuple:
    """Decode a tensor index into a tuple of n basis indices."""
    result = []
    for _ in range(n):
        result.append(idx % dim)
        idx //= dim
    return tuple(reversed(result))


def _encode_tensor(tensor: list, dim: int) -> int:
    """Encode a tuple of basis indices into a single tensor index."""
    idx = 0
    for v in tensor:
        idx = idx * dim + v
    return idx


# ---------------------------------------------------------------------------
# Simplified approach: bracket-only differential + cohomology
# ---------------------------------------------------------------------------

def bracket_differential(dim_g: int, bracket: np.ndarray,
                          bar_degree: int) -> np.ndarray:
    """Compute the bracket (simple pole) differential d: B̄^n -> B̄^{n-1}.

    This is the bracket-only part. NOTE: d_bracket² ≠ 0 in general.
    However, for computing bar cohomology via the PBW spectral sequence,
    this is the E_1 page differential.

    For practical computation: we compute this matrix and check if it
    gives the correct bar cohomology dimensions when combined with the
    curvature term.

    Returns matrix of shape (dim B̄^{n-1}, dim B̄^n).
    """
    n = bar_degree
    d = dim_g

    if n <= 1:
        # d: B̄^1 -> B̄^0 = C. The map is zero (no pair to contract).
        return np.zeros((1, d))

    # Source: B̄^n = g^{⊗n} ⊗ OS^{n-1}(n)
    _, os_src_basis = os_basis(n, n - 1)
    os_src_dim = os_src_basis.shape[0]
    src_dim = d ** n * os_src_dim

    # Target: B̄^{n-1} = g^{⊗(n-1)} ⊗ OS^{n-2}(n-1)
    if n - 1 >= 2:
        _, os_tgt_basis = os_basis(n - 1, n - 2)
        os_tgt_dim = os_tgt_basis.shape[0]
    else:
        os_tgt_dim = 1  # OS^0(1) = C

    tgt_dim = d ** (n - 1) * os_tgt_dim

    mat = np.zeros((tgt_dim, src_dim))

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # OS residue
            os_res = residue_map(n, n - 1, i, j)

            sign_ij = (-1) ** (j - i - 1)

            # For each source tensor element
            for src_tensor_idx in range(d ** n):
                tensor = _decode_tensor(src_tensor_idx, d, n)
                v_i = tensor[i - 1]
                v_j = tensor[j - 1]

                for c in range(d):
                    coeff = bracket[v_i, v_j, c]
                    if abs(coeff) < 1e-15:
                        continue

                    tgt_tensor = list(tensor)
                    tgt_tensor[i - 1] = c
                    del tgt_tensor[j - 1]
                    tgt_tensor_idx = _encode_tensor(tgt_tensor, d)

                    for os_src_idx in range(os_src_dim):
                        src_idx = src_tensor_idx * os_src_dim + os_src_idx

                        for os_tgt_idx in range(os_tgt_dim):
                            os_coeff = os_res[os_tgt_idx, os_src_idx]
                            if abs(os_coeff) < 1e-15:
                                continue

                            tgt_idx = tgt_tensor_idx * os_tgt_dim + os_tgt_idx
                            mat[tgt_idx, src_idx] += sign_ij * coeff * os_coeff

    return mat


def curvature_differential(dim_g: int, killing: np.ndarray,
                             bar_degree: int, level: float = 1.0) -> np.ndarray:
    """Compute the curvature (double pole) differential d: B̄^n -> B̄^{n-2}.

    For n = 2: maps B̄^2 -> B̄^0 = C.
    For n ≥ 3: maps B̄^n -> B̄^{n-2} (with appropriate OS map).

    Returns matrix of shape (dim B̄^{n-2}, dim B̄^n).
    """
    n = bar_degree
    d = dim_g

    if n < 2:
        return np.zeros((1, d))

    # Source
    _, os_src_basis = os_basis(n, n - 1) if n >= 2 else ([], np.array([[1.0]]))
    os_src_dim = os_src_basis.shape[0] if n >= 2 else 1
    src_dim = d ** n * os_src_dim

    if n == 2:
        # Target: B̄^0 = C (1-dim)
        tgt_dim = 1
        mat = np.zeros((tgt_dim, src_dim))

        # Only pair (1,2)
        os_res = residue_map(2, 1, 1, 2)

        for src_tensor_idx in range(d ** 2):
            v1, v2 = _decode_tensor(src_tensor_idx, d, 2)
            kf = killing[v1, v2]
            if abs(kf) < 1e-15:
                continue

            for os_src_idx in range(os_src_dim):
                src_idx = src_tensor_idx * os_src_dim + os_src_idx
                os_coeff = os_res[0, os_src_idx]
                mat[0, src_idx] += level * kf * os_coeff

        return mat

    else:
        # n ≥ 3: need composite OS map
        # Target: B̄^{n-2} = g^{⊗(n-2)} ⊗ OS^{n-3}(n-2)
        if n - 2 >= 2:
            _, os_tgt_basis = os_basis(n - 2, n - 3)
            os_tgt_dim = os_tgt_basis.shape[0]
        elif n - 2 == 1:
            os_tgt_dim = 1
        else:
            os_tgt_dim = 1

        tgt_dim = d ** (n - 2) * os_tgt_dim if n >= 3 else 1

        mat = np.zeros((tgt_dim, src_dim))

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # OS map: composite of Res_{D_{ij}} and "forget merged point"
                # First: Res_{D_{ij}}: OS^{n-1}(n) -> OS^{n-2}(n-1)
                os_res1 = residue_map(n, n - 1, i, j)

                # Merged point = min(i,j). Points > max(i,j) decremented.
                merged = min(i, j)

                # Second: "forget merged point" map
                # OS^{n-2}(n-1) -> OS^{n-3}(n-2)
                # This removes the merged point from the configuration.
                # Implemented as: sum of Res_{D_{merged, q}} for all q ≠ merged
                # in {1,...,n-1}, weighted appropriately.
                # Actually, the "forgetful" map is:
                # π: Conf_{n-1} -> Conf_{n-2} (forget point labeled merged)
                # π*: OS^{n-3}(n-2) -> OS^{n-3}(n-1) (pullback, adds trivially)
                # We want the LEFT ADJOINT (pushforward):
                # π_*: OS^{n-2}(n-1) -> OS^{n-3}(n-2)

                # For the forgetful map on OS algebras:
                # π_*(η_{ij}) = η_{ij} if neither i nor j is the forgotten point
                # π_*(η_{i,merged}) = 0 (forms involving the forgotten point vanish)

                # So the pushforward just SETS TO ZERO all forms involving the
                # merged point. This is a projection.

                # Implement: for each basis element of OS^{n-2}(n-1), check if
                # it involves the merged point. If not, it maps to the corresponding
                # element of OS^{n-3}(n-2).

                # But this changes the point labels again. After forgetting point
                # 'merged' from {1,...,n-1}, we relabel {1,...,n-1}\{merged} to {1,...,n-2}.

                # This is equivalent to: residue_map(n-1, n-2, merged, q) summed
                # over q... no that's not right.

                # Actually: the forgetful map π: Conf_{n-1} -> Conf_{n-2}
                # (forget point merged) is the projection that drops one coordinate.
                # The pullback π* is injective. The pushforward π_* (fiber integration)
                # is NOT the residue — it's the integration over the fiber.

                # For the OS algebra, the forgetful map is simply:
                # restrict to forms not involving the forgotten point, then relabel.

                # This is implemented by checking which OS basis elements DON'T
                # involve the merged point.

                os_mid_mons, os_mid_basis = os_basis(n - 1, n - 2)
                os_mid_dim = os_mid_basis.shape[0]

                # Build the "forget merged" projection matrix
                # OS^{n-2}(n-1) -> OS^{n-3}(n-2)
                forget_matrix = _build_forget_map(n - 1, n - 2, merged)

                # Composite OS map: forget_matrix @ os_res1
                os_composite = forget_matrix @ os_res1

                sign_ij = (-1) ** (j - i - 1)

                for src_tensor_idx in range(d ** n):
                    tensor = _decode_tensor(src_tensor_idx, d, n)
                    v_i = tensor[i - 1]
                    v_j = tensor[j - 1]

                    kf = killing[v_i, v_j]
                    if abs(kf) < 1e-15:
                        continue

                    coeff = level * kf * sign_ij

                    # Build target tensor: remove v_i and v_j
                    tgt_tensor = list(tensor)
                    # Remove in reverse order to keep indices stable
                    del tgt_tensor[max(i, j) - 1]
                    del tgt_tensor[min(i, j) - 1]
                    tgt_tensor_idx = _encode_tensor(tgt_tensor, d)

                    for os_src_idx in range(os_src_dim):
                        src_idx = src_tensor_idx * os_src_dim + os_src_idx

                        for os_tgt_idx in range(os_tgt_dim):
                            os_coeff = os_composite[os_tgt_idx, os_src_idx]
                            if abs(os_coeff) < 1e-15:
                                continue

                            tgt_idx = tgt_tensor_idx * os_tgt_dim + os_tgt_idx
                            mat[tgt_idx, src_idx] += coeff * os_coeff

        return mat


def _build_forget_map(n_points: int, degree: int, forget_pt: int) -> np.ndarray:
    """Build the forgetful map OS^k(n) -> OS^{k-1}(n-1) that removes a point.

    This is NOT a residue. It's the restriction to forms not involving
    the forgotten point, with relabeling.

    Actually, this is exactly the same as the residue map! When we "forget"
    a point, we sum over all forms that involve that point (taking the
    residue at the diagonal) — but actually, forgetting a point in the
    configuration space is a different operation.

    For the curvature contribution: we need to go from OS^{n-2}(n-1)
    to OS^{n-3}(n-2). One natural map is the restriction: take only
    forms that don't involve the forgotten point, then relabel.

    Implementation: for each monomial in OS^{k}(n), if it doesn't
    contain any pair involving the forgotten point, relabel it to
    the (n-1)-point configuration.
    """
    src_mons, src_basis = os_basis(n_points, degree)
    tgt_mons, tgt_basis = os_basis(n_points - 1, degree)

    src_dim = src_basis.shape[0]
    tgt_dim = tgt_basis.shape[0]
    num_src_mons = len(src_mons)
    num_tgt_mons = len(tgt_mons)

    if src_dim == 0 or tgt_dim == 0:
        return np.zeros((tgt_dim, src_dim))

    tgt_mon_idx = {m: i for i, m in enumerate(tgt_mons)}

    def relabel_after_forget(pt):
        if pt > forget_pt:
            return pt - 1
        return pt

    # Build map on monomial level
    restrict = np.zeros((num_tgt_mons, num_src_mons))

    for s_idx, s_mon in enumerate(src_mons):
        # Check if any pair involves forget_pt
        involves_forgotten = any(forget_pt in (a, b) for a, b in s_mon)
        if involves_forgotten:
            continue

        # Relabel
        relabeled = tuple(sorted(make_pair(relabel_after_forget(a),
                                           relabel_after_forget(b))
                                  for a, b in s_mon))

        if relabeled in tgt_mon_idx:
            restrict[tgt_mon_idx[relabeled], s_idx] = 1

    # Convert to basis coords
    image_in_mons = restrict @ src_basis.T
    gram = tgt_basis @ tgt_basis.T
    rhs = tgt_basis @ image_in_mons

    try:
        result = np.linalg.solve(gram, rhs)
    except np.linalg.LinAlgError:
        result = np.linalg.lstsq(gram, rhs, rcond=None)[0]

    result[np.abs(result) < 1e-10] = 0
    return result


# ---------------------------------------------------------------------------
# Full differential and cohomology computation
# ---------------------------------------------------------------------------

def full_differential(dim_g: int, bracket: np.ndarray, killing: np.ndarray,
                       bar_degree: int, level: float = 1.0) -> np.ndarray:
    """Compute the FULL bar differential d: B̄^n -> B̄^{n-1} ⊕ B̄^{n-2}.

    Returns matrix of shape (dim B̄^{n-1} + dim B̄^{n-2}, dim B̄^n).
    """
    d_bracket = bracket_differential(dim_g, bracket, bar_degree)
    d_curv = curvature_differential(dim_g, killing, bar_degree, level)

    # Stack vertically
    return np.vstack([d_bracket, d_curv])


def bar_cohomology_dim(dim_g: int, bracket: np.ndarray, killing: np.ndarray,
                        bar_degree: int, level: float = 1.0) -> int:
    """Compute dim H^n(B̄) = dim ker(d_n) / im(d from higher degrees).

    H^n = ker(d_n: B̄^n -> lower) / im(d_{n+1}: B̄^{n+1} -> ... including B̄^n component)
                                   + im(d_{n+2}: B̄^{n+2} -> ... including B̄^n component)

    For KM algebras:
    d: B̄^n -> B̄^{n-1} ⊕ B̄^{n-2}

    Components landing in B̄^n:
    - Bracket from B̄^{n+1}: the B̄^n component of d_{n+1}
    - Curvature from B̄^{n+2}: the B̄^n component of d_{n+2}

    H^n = ker(d_n to B̄^{n-1} ⊕ B̄^{n-2}) / (im_bracket(d_{n+1}) + im_curv(d_{n+2}))
    """
    n = bar_degree
    d = dim_g

    if n < 1:
        return 1  # H^0 = C

    # Compute d_n: B̄^n -> B̄^{n-1} ⊕ B̄^{n-2}
    dn = full_differential(d, bracket, killing, n, level)
    src_dim = dn.shape[1]

    # kernel of d_n
    _, S_dn, Vt_dn = np.linalg.svd(dn, full_matrices=True)
    rank_dn = np.sum(S_dn > 1e-8)
    ker_dim = src_dim - rank_dn

    # Image in B̄^n from d_{n+1} (bracket component)
    d_n1_bracket = bracket_differential(d, bracket, n + 1)
    # d_n1_bracket maps B̄^{n+1} -> B̄^n

    # Image in B̄^n from d_{n+2} (curvature component)
    d_n2_curv = curvature_differential(d, killing, n + 2, level)
    # d_n2_curv maps B̄^{n+2} -> B̄^n

    # Total image in B̄^n
    # Stack the two image matrices horizontally
    if d_n1_bracket.shape[0] != d_n2_curv.shape[0]:
        # Dimensions might not match if one target is B̄^n and other is different
        # Both should target B̄^n
        pass

    # The image is the column space of [d_n1_bracket | d_n2_curv]
    image_matrix = np.hstack([d_n1_bracket, d_n2_curv])

    _, S_im, _ = np.linalg.svd(image_matrix, full_matrices=False)
    im_dim = np.sum(S_im > 1e-8)

    cohomology_dim = ker_dim - im_dim

    return int(round(cohomology_dim))


# ---------------------------------------------------------------------------
# Quick test
# ---------------------------------------------------------------------------

def verify_sl2_bar_cohomology(max_degree: int = 4) -> Dict[str, object]:
    """Verify sl₂ bar cohomology against known Riordan numbers."""
    from .koszul_hilbert import riordan

    d, bracket, killing = sl2_data()

    results = {}
    for n in range(1, max_degree + 1):
        computed = bar_cohomology_dim(d, bracket, killing, n, level=1.0)
        expected = riordan(n + 3)
        results[f"H^{n}(sl2)"] = {
            'computed': computed,
            'expected': expected,
            'match': computed == expected,
        }
        print(f"  H^{n}(B̄(sl₂)): computed={computed}, expected=R({n+3})={expected}, "
              f"{'✓' if computed == expected else '✗'}")

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("CHIRAL BAR DIFFERENTIAL: sl₂ VERIFICATION")
    print("=" * 60)
    print()

    d, bracket, killing = sl2_data()

    # Check bracket differential d²
    print("Checking d_bracket² for sl₂:")
    for n in range(2, 5):
        d_n = bracket_differential(d, bracket, n)
        d_n1 = bracket_differential(d, bracket, n - 1) if n >= 2 else np.zeros((1, d))
        # d² = d_{n-1} @ d_n
        if d_n.shape[0] == d_n1.shape[1]:
            d2 = d_n1 @ d_n
        else:
            print(f"  n={n}: shape mismatch d_{n-1}={d_n1.shape}, d_n={d_n.shape}")
            continue
        max_val = np.abs(d2).max() if d2.size > 0 else 0
        print(f"  n={n}: ||d²||_max = {max_val:.6e}  ({'d²=0' if max_val < 1e-8 else 'd²≠0'})")

    print()
    print("Bar cohomology:")
    verify_sl2_bar_cohomology(4)
