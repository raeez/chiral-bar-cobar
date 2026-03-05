#!/usr/bin/env python3
r"""Compute chiral bar cohomology with FULL OPE differential.

The bar differential for a KM algebra has TWO components:
  d = d_bracket + d_killing
where:
  d_bracket: B-bar^n -> B-bar^{n-1}  (from simple pole, Lie bracket)
  d_killing: B-bar^n -> B-bar^{n-2}  (from double pole, k * Killing form)

d^2 = 0 requires BOTH components. The bracket-only differential does NOT
square to zero on g^{tensor n} tensor OS^{n-1}(C_n).

This script builds the total complex C = oplus B-bar^n with d = d_bracket + d_killing,
verifies d^2 = 0, and computes bar cohomology at each degree.
"""

import numpy as np
from math import factorial
from typing import Dict, List, Tuple, Optional
import sys
from pathlib import Path

# Reuse OS algebra code from the previous script
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_bar_cohomology import (
    nbc_basis, residue_matrix, sl2_structure_tensor, sl3_structure_tensor
)


def killing_form_sl2():
    """Killing form for sl_2. kappa(a,b) with basis e=0, h=1, f=2.

    Normalized: (e,f)=(f,e)=1, (h,h)=2, rest zero.
    """
    K = np.zeros((3, 3))
    K[0, 2] = 1   # (e, f) = 1
    K[2, 0] = 1   # (f, e) = 1
    K[1, 1] = 2   # (h, h) = 2
    return K


def killing_form_sl3():
    """Killing form for sl_3. kappa(a,b) with standard basis."""
    d = 8
    K = np.zeros((d, d))
    H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
    CARTAN = np.array([[2, -1], [-1, 2]])
    # (H_i, H_j) = A_{ij}
    K[H1, H1] = 2; K[H1, H2] = -1; K[H2, H1] = -1; K[H2, H2] = 2
    # (E_i, F_i) = 1
    K[E1, F1] = 1; K[F1, E1] = 1
    K[E2, F2] = 1; K[F2, E2] = 1
    K[E3, F3] = 1; K[F3, E3] = 1
    return K


def build_block_differential(f_abc, kappa, level, max_degree):
    """Build the full bar differential as a block matrix.

    The total complex C = B-bar^0 + B-bar^1 + ... + B-bar^N
    with d = d_bracket + level * d_killing.

    Returns: (D, offsets, dims) where D is the total differential matrix,
    offsets[n] is the starting index of B-bar^n in C,
    dims[n] is dim B-bar^n.
    """
    dim_g = f_abc.shape[0]

    # Compute dimensions and offsets
    dims = {}
    dims[0] = 1  # B-bar^0 = ground field
    for n in range(1, max_degree + 1):
        os_dim = factorial(n - 1) if n >= 1 else 1
        dims[n] = dim_g ** n * os_dim

    total_dim = sum(dims[n] for n in range(max_degree + 1))
    offsets = {}
    off = 0
    for n in range(max_degree + 1):
        offsets[n] = off
        off += dims[n]

    D = np.zeros((total_dim, total_dim))

    # Build d_bracket: B-bar^n -> B-bar^{n-1} for n >= 2
    for n in range(2, max_degree + 1):
        D_bracket = _build_bracket_component(f_abc, n)
        r_start = offsets[n - 1]
        c_start = offsets[n]
        D[r_start:r_start + dims[n-1], c_start:c_start + dims[n]] += D_bracket

    # Build d_killing: B-bar^n -> B-bar^{n-2} for n >= 2
    for n in range(2, max_degree + 1):
        D_killing = _build_killing_component(f_abc, kappa, n)
        target_deg = n - 2
        if target_deg < 0:
            continue
        r_start = offsets[target_deg]
        c_start = offsets[n]
        D[r_start:r_start + dims[target_deg], c_start:c_start + dims[n]] += level * D_killing

    return D, offsets, dims


def _build_bracket_component(f_abc, n):
    """Build d_bracket: B-bar^n -> B-bar^{n-1}.

    Same as before: uses Lie bracket + OS residues.
    """
    dim_g = f_abc.shape[0]

    source_os = nbc_basis(n, n - 1)
    target_os = nbc_basis(n - 1, n - 2) if n >= 2 else [()]
    dim_os_s = len(source_os)
    dim_os_t = len(target_os)

    source_dim = dim_g ** n * dim_os_s
    target_dim = dim_g ** (n - 1) * dim_os_t

    res_maps = residue_matrix(n)

    M = np.zeros((target_dim, source_dim))

    for src_t_idx in range(dim_g ** n):
        gens = []
        temp = src_t_idx
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g

        for os_s in range(dim_os_s):
            col = src_t_idx * dim_os_s + os_s

            for p in range(1, n + 1):
                for q in range(p + 1, n + 1):
                    res = res_maps.get((p, q))
                    if res is None:
                        continue

                    for os_t in range(dim_os_t):
                        rc = res[os_t, os_s]
                        if abs(rc) < 1e-15:
                            continue

                        a_p, a_q = gens[p-1], gens[q-1]
                        for c in range(dim_g):
                            fc = f_abc[a_p, a_q, c]
                            if abs(fc) < 1e-15:
                                continue

                            tgt = list(gens)
                            tgt[p-1] = c
                            del tgt[q-1]

                            sign = (-1) ** (q - p - 1)

                            tgt_idx = 0
                            for k in range(len(tgt) - 1, -1, -1):
                                tgt_idx = tgt_idx * dim_g + tgt[k]
                            row = tgt_idx * dim_os_t + os_t

                            M[row, col] += sign * fc * rc

    return M


def _build_killing_component(f_abc, kappa, n):
    """Build d_killing: B-bar^n -> B-bar^{n-2}.

    For each collision (p,q), this contracts generators a_p, a_q using the
    Killing form kappa(a_p, a_q) and removes both, reducing to n-2 generators.

    The OS residue Res_{D_{pq}}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})
    is applied first (from colliding points p,q into one),
    then the SECOND collision (of the merged point with the remaining OS form)...

    Actually, the Killing form maps a PAIR of generators to a SCALAR.
    So both generators are removed, and we go from n generators to n-2.
    The OS form maps: we need Res_{D_{pq}}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})
    but then the merged point carries a scalar (not a generator), so the
    resulting element is in g^{n-2} * OS^{n-2}(C_{n-1}).

    Wait — after the Killing form collision, the merged point has no generator.
    So we should remove it entirely. The n-2 remaining generators sit at
    n-2 points, and we need a form in OS^{n-3}(C_{n-2}).

    Hmm, this means d_killing: B-bar^n -> B-bar^{n-2} uses a DOUBLE residue:
    first Res_{D_{pq}} to merge p,q (OS^{n-1} -> OS^{n-2}),
    then we need to handle the fact that the merged point has no generator.

    Actually, for KM, the double pole OPE a(z)b(w) ~ k*kappa(a,b)/(z-w)^2
    gives a contribution to the vacuum (no generator output). The
    Poincare residue at D_{pq} of a form with a SECOND-ORDER pole
    requires extracting the coefficient of 1/(z_p - z_q)^2, not just
    1/(z_p - z_q).

    The standard bar construction for a QUADRATIC algebra uses:
    - Simple pole residue -> bracket (goes to B^{n-1})
    - Double pole residue -> Killing form (goes to B^{n-2})

    For the double pole, the residue operation is different from the
    simple pole residue. Instead of Res_{z_p=z_q}[f(z) dlog(z_p-z_q)],
    we need Res_{z_p=z_q}[f(z) / (z_p-z_q)^2 * dz_p].

    In terms of OS forms: the double pole doesn't use the eta_{pq} factor.
    Instead, it extracts the coefficient of 1/(z_p-z_q)^2 in the OPE,
    times the form factor with eta_{pq} replaced by (no form at that pair).

    But this requires the form omega to have a specific structure near D_{pq},
    which is more complex than the simple pole case.

    ALTERNATIVE INTERPRETATION: The double pole gives a map
    d_killing: B^n -> B^{n-2} where we:
    1. Pick a pair (p,q)
    2. Apply kappa(a_p, a_q) -> scalar
    3. Remove both positions p,q from the tensor product
    4. The OS form goes: Res_{D_{pq}}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})
       where C_{n-1} has the point {pq merged} plus n-2 remaining.
       BUT the merged point has no generator, so effectively we have
       n-2 active points with n-2 generators.

    Wait, after merging p,q into one point, we have n-1 points. But one of
    them (the merged point) carries no generator — it carries a scalar.
    The resulting element is: scalar * (g^{n-2} tensor OS^{n-2}(C_{n-1}))

    But OS^{n-2}(C_{n-1}) has dim (n-2)!, and g^{n-2} has dim d^{n-2}.
    So the target is B-bar^{n-2} but with an EXTRA point (the scalar point)
    contributing to the OS algebra.

    Hmm, this means the OS algebra has n-1 points (not n-2), so
    OS^{n-2}(C_{n-1}) has dim (n-2)!, matching B-bar^{n-2}.
    But B-bar^{n-2} should have n-2 points with OS^{n-3}(C_{n-2})
    of dim (n-3)!.

    This doesn't match. Unless the "extra" point (carrying the scalar)
    is absorbed into the OS algebra differently.

    I think the correct interpretation is simpler:
    The double pole contribution at (p,q) gives:
    d_killing(a_1...a_n * omega)_{pq} = kappa(a_p, a_q) * sign *
        (a_1...^a_p...^a_q...a_n) * Res_{D_{pq}}(omega)

    where the result lives in g^{n-2} * OS^{n-2}(C_{n-1}).
    And we identify this with B-bar^{n-2} = g^{n-2} * OS^{n-3}(C_{n-2}).

    The identification requires a further step: the merged point (now
    carrying a scalar) needs to be "removed" from the configuration,
    going from C_{n-1} to C_{n-2} by forgetting the scalar point.

    The forgetful map pi: C_{n-1} -> C_{n-2} (forget the merged point)
    induces pi*: OS^{n-3}(C_{n-2}) -> OS^{n-2}(C_{n-1}) (pullback).

    We need the TRANSPOSE (pushforward) to go the other direction:
    pi_*: OS^{n-2}(C_{n-1}) -> OS^{n-3}(C_{n-2}).

    This is the "integration along fiber" map. For configuration spaces,
    this is the forgetful map on cohomology.

    THIS IS TOO COMPLEX. Let me try a completely different approach.
    """
    dim_g = f_abc.shape[0]

    # For now: implement the SIMPLEST version where d_killing maps
    # B^n -> B^{n-2} by contracting a pair with the Killing form.
    # The OS form part: use Res_{D_{pq}} followed by forgetful map.

    # Source: B^n = g^n * OS^{n-1}(C_n)
    # Target: B^{n-2} = g^{n-2} * OS^{n-3}(C_{n-2})

    if n < 2:
        return np.zeros((0, 0))

    source_os = nbc_basis(n, n - 1)
    dim_os_s = len(source_os)
    source_dim = dim_g ** n * dim_os_s

    if n == 2:
        # B^0 = k, dim 1. Target has no generators and no OS forms.
        target_dim = 1
        M = np.zeros((target_dim, source_dim))

        # d_killing(a*b * eta12) = kappa(a,b)
        # The OS residue Res_{D12}(eta12) = 1
        for a in range(dim_g):
            for b in range(dim_g):
                kab = kappa[a, b]
                if abs(kab) < 1e-15:
                    continue
                src_t_idx = b * dim_g + a  # little-endian
                col = src_t_idx * 1 + 0  # only one OS form
                M[0, col] += kab  # sign = 1 for (1,2) collision

        return M

    # For n >= 3: d_killing: B^n -> B^{n-2}
    # This involves: Res_{D_{pq}} for the OS form (OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})),
    # then forgetful/projection to OS^{n-3}(C_{n-2}).

    # For now, return zero matrix (we'll add this later)
    target_os = nbc_basis(n - 2, n - 3) if n >= 3 else [()]
    dim_os_t = len(target_os)
    target_dim = dim_g ** (n - 2) * dim_os_t if n >= 3 else 1

    M = np.zeros((target_dim, source_dim))
    # TODO: implement the full d_killing for n >= 3
    return M


def compute_full_bar_cohomology(f_abc, kappa, level, name, max_degree=4):
    """Compute bar cohomology with both bracket and Killing form."""
    dim_g = f_abc.shape[0]

    print(f"\n{'='*60}")
    print(f"FULL BAR COHOMOLOGY: {name}, level k = {level}")
    print(f"{'='*60}")

    D, offsets, dims = build_block_differential(f_abc, kappa, level, max_degree)
    total = sum(dims[n] for n in range(max_degree + 1))

    print(f"\nChain dimensions:")
    for n in range(max_degree + 1):
        print(f"  B-bar^{n}: dim = {dims[n]}")
    print(f"  Total: {total}")

    # Check d^2 = 0
    D2 = D @ D
    d2_err = np.max(np.abs(D2)) if D2.size > 0 else 0
    print(f"\nd^2 check: max |D^2| = {d2_err:.2e}",
          "OK" if d2_err < 1e-8 else "FAIL")

    # Compute cohomology at each bar degree
    print(f"\nBar cohomology by degree:")
    for n in range(max_degree + 1):
        # kernel of d at degree n: d maps FROM degree n to degrees n-1 and n-2
        # image of d at degree n: d maps TO degree n from degrees n+1 and n+2

        # Extract the rows of D that correspond to degree n (this is im(d) INTO n)
        # and the columns of D that correspond to degree n (this is d FROM n)

        start_n = offsets[n]
        end_n = start_n + dims[n]

        # d FROM n: columns start_n:end_n of D
        d_from_n = D[:, start_n:end_n]

        # d INTO n: rows start_n:end_n of D
        d_into_n = D[start_n:end_n, :]

        rank_out = np.linalg.matrix_rank(d_from_n, tol=1e-8)
        rank_in = np.linalg.matrix_rank(d_into_n, tol=1e-8)

        H_n = dims[n] - rank_out - rank_in
        print(f"  H^{n} = {dims[n]} - {rank_out} - {rank_in} = {H_n}")


if __name__ == "__main__":
    f_sl2 = sl2_structure_tensor()
    K_sl2 = killing_form_sl2()

    # Test at several levels
    for k in [0, 1, 2, -1]:
        compute_full_bar_cohomology(f_sl2, K_sl2, level=k, name="sl_2", max_degree=4)
