#!/usr/bin/env python3
r"""Compute chiral bar cohomology via the UNREDUCED bar complex.

Key insight: use V_aug = C|0> + g (vacuum + generators) with the FULL OPE
as a single linear map OPE: V_aug x V_aug -> V_aug:
  OPE(a, b) = [a,b] + k*kappa(a,b)*|0>  for a,b in g
  OPE(|0>, anything) = 0
  OPE(anything, |0>) = 0

The bar differential d: B_n -> B_{n-1} uses OPE + OS residue, same as
the bracket-only differential but with V_aug instead of g.

Chain groups: B_n = V_aug^{tensor n} * OS^{n-1}(C_n)
  dim B_n = (1 + dim g)^n * (n-1)!

The UNREDUCED bar cohomology gives the correct "bar cohomology" of the
chiral algebra (after quotienting by trivial factors).
"""

import numpy as np
from math import factorial
from typing import Dict, List, Tuple
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_bar_cohomology import nbc_basis, residue_matrix


def build_ope_tensor_sl2(k: float) -> np.ndarray:
    """Build OPE tensor for sl_2 at level k on V_aug = C|0> + sl_2.

    Basis: |0>=0, e=1, h=2, f=3. dim=4.
    OPE(a,b) = [a,b] + k*kappa(a,b)*|0>.
    """
    d = 4
    T = np.zeros((d, d, d))

    # Indices: 0=|0>, 1=e, 2=h, 3=f

    # Lie bracket part: [a,b] for a,b in {e,h,f}
    # [e,f] = h, [f,e] = -h
    T[1, 3, 2] = 1     # OPE(e,f) -> h
    T[3, 1, 2] = -1    # OPE(f,e) -> -h
    # [h,e] = 2e, [e,h] = -2e
    T[2, 1, 1] = 2     # OPE(h,e) -> 2e
    T[1, 2, 1] = -2    # OPE(e,h) -> -2e
    # [h,f] = -2f, [f,h] = 2f
    T[2, 3, 3] = -2    # OPE(h,f) -> -2f
    T[3, 2, 3] = 2     # OPE(f,h) -> 2f

    # Killing form part: k * kappa(a,b) * |0>
    # kappa(e,f) = kappa(f,e) = 1, kappa(h,h) = 2
    T[1, 3, 0] += k * 1    # OPE(e,f) -> k*|0>
    T[3, 1, 0] += k * 1    # OPE(f,e) -> k*|0>
    T[2, 2, 0] += k * 2    # OPE(h,h) -> 2k*|0>

    return T


def build_ope_tensor_sl3(k: float) -> np.ndarray:
    """Build OPE tensor for sl_3 at level k on V_aug = C|0> + sl_3.

    Basis: |0>=0, H1=1, H2=2, E1=3, E2=4, E3=5, F1=6, F2=7, F3=8. dim=9.
    """
    d = 9
    T = np.zeros((d, d, d))

    # Generator indices (shifted by 1 from the vacuum)
    H1, H2, E1, E2, E3, F1, F2, F3 = 1, 2, 3, 4, 5, 6, 7, 8
    CARTAN = np.array([[2, -1], [-1, 2]])

    def set_bracket(a, b, c, val):
        T[a, b, c] += val
        T[b, a, c] -= val

    # [H_i, E_j] = A_{ij} E_j
    for i, hi in enumerate([H1, H2]):
        for j, ej in enumerate([E1, E2]):
            if CARTAN[i, j] != 0:
                set_bracket(hi, ej, ej, CARTAN[i, j])

    # [H_i, F_j] = -A_{ij} F_j
    for i, hi in enumerate([H1, H2]):
        for j, fj in enumerate([F1, F2]):
            if CARTAN[i, j] != 0:
                set_bracket(hi, fj, fj, -CARTAN[i, j])

    # [E_i, F_j] = delta_{ij} H_i
    set_bracket(E1, F1, H1, 1)
    set_bracket(E2, F2, H2, 1)

    # [E_1, E_2] = E_3
    set_bracket(E1, E2, E3, 1)
    # [F_2, F_1] = F_3
    set_bracket(F2, F1, F3, 1)

    # [H_i, E_3]: root alpha_1+alpha_2
    set_bracket(H1, E3, E3, 1)
    set_bracket(H2, E3, E3, 1)

    # [H_i, F_3]
    set_bracket(H1, F3, F3, -1)
    set_bracket(H2, F3, F3, -1)

    # [E_3, F_1] = -E_2
    set_bracket(E3, F1, E2, -1)
    # [E_3, F_2] = E_1
    set_bracket(E3, F2, E1, 1)
    # [E_3, F_3] = H_1 + H_2
    set_bracket(E3, F3, H1, 1)
    set_bracket(E3, F3, H2, 1)

    # [E_1, F_3] = -F_2
    set_bracket(E1, F3, F2, -1)
    # [E_2, F_3] = F_1
    set_bracket(E2, F3, F1, 1)

    # Killing form: k * kappa(a,b) * |0>
    # kappa(H_i, H_j) = A_{ij}
    T[H1, H1, 0] += k * 2
    T[H1, H2, 0] += k * (-1)
    T[H2, H1, 0] += k * (-1)
    T[H2, H2, 0] += k * 2
    # kappa(E_i, F_i) = kappa(F_i, E_i) = 1
    T[E1, F1, 0] += k * 1; T[F1, E1, 0] += k * 1
    T[E2, F2, 0] += k * 1; T[F2, E2, 0] += k * 1
    T[E3, F3, 0] += k * 1; T[F3, E3, 0] += k * 1

    return T


def chiral_bar_diff(ope_tensor: np.ndarray, n: int) -> np.ndarray:
    """Build chiral bar differential d: B_n -> B_{n-1}.

    B_n = V^{tensor n} * OS^{n-1}(C_n)
    B_{n-1} = V^{tensor (n-1)} * OS^{n-2}(C_{n-1})

    d = sum_{p<q} sign * OPE(v_p, v_q) * remaining * Res_{D_pq}(omega)
    """
    dim_v = ope_tensor.shape[0]

    if n <= 1:
        return np.zeros((0, dim_v))

    source_os = nbc_basis(n, n - 1)
    target_os = nbc_basis(n - 1, n - 2) if n >= 2 else [()]
    dim_os_s = len(source_os)
    dim_os_t = len(target_os)

    source_dim = dim_v ** n * dim_os_s
    target_dim = dim_v ** (n - 1) * dim_os_t

    res_maps = residue_matrix(n)

    M = np.zeros((target_dim, source_dim))

    for src_t_idx in range(dim_v ** n):
        gens = []
        temp = src_t_idx
        for _ in range(n):
            gens.append(temp % dim_v)
            temp //= dim_v

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

                        a_p, a_q = gens[p - 1], gens[q - 1]
                        for c in range(dim_v):
                            fc = ope_tensor[a_p, a_q, c]
                            if abs(fc) < 1e-15:
                                continue

                            tgt = list(gens)
                            tgt[p - 1] = c
                            del tgt[q - 1]

                            sign = (-1) ** (q - p - 1)

                            tgt_idx = 0
                            for i in range(len(tgt) - 1, -1, -1):
                                tgt_idx = tgt_idx * dim_v + tgt[i]
                            row = tgt_idx * dim_os_t + os_t

                            M[row, col] += sign * fc * rc

    return M


def compute_cohomology(ope_tensor: np.ndarray, name: str, max_deg: int = 4,
                       expected: list = None):
    """Compute unreduced bar cohomology and report."""
    dim_v = ope_tensor.shape[0]

    print(f"\n{'='*60}")
    print(f"UNREDUCED BAR COHOMOLOGY: {name} (dim V_aug = {dim_v})")
    print(f"{'='*60}")

    # Chain dimensions
    dims = {}
    for n in range(1, max_deg + 2):
        os = factorial(n - 1) if n >= 1 else 1
        dims[n] = dim_v ** n * os
        print(f"  B_{n}: dim = {dim_v}^{n} * {os} = {dims[n]}")

    # Build differentials and check d^2
    diffs = {}
    ranks = {}
    for n in range(2, max_deg + 2):
        if dims[n] > 500000:
            print(f"  d_{n}: SKIPPED (dim {dims[n]} too large)")
            continue
        print(f"  Building d_{n}: B_{n}({dims[n]}) -> B_{n-1}({dims[n-1]})")
        D = chiral_bar_diff(ope_tensor, n)
        r = np.linalg.matrix_rank(D, tol=1e-8)
        ranks[n] = r
        diffs[n] = D
        print(f"    rank = {r}")

        # d^2 check
        if n - 1 in diffs:
            D_prev = diffs[n - 1]
            prod = D_prev @ D
            err = np.max(np.abs(prod)) if prod.size > 0 else 0
            status = "OK" if err < 1e-8 else f"FAIL (max={err:.2e})"
            print(f"    d^2 check: {status}")

    # Cohomology (homological: d goes down)
    print(f"\nBar homology (d going down):")
    for n in range(1, max_deg + 1):
        r_out = ranks.get(n, 0)      # rank of d_n (going out)
        r_in = ranks.get(n + 1, 0)   # rank of d_{n+1} (coming in)
        H_n = dims[n] - r_out - r_in
        exp_str = ""
        if expected and n <= len(expected):
            exp_str = f"  (expected: {expected[n-1]})"
        print(f"  H_{n} = {dims[n]} - {r_out} - {r_in} = {H_n}{exp_str}")


def verify_jacobi(T: np.ndarray, name: str):
    """Verify Jacobi identity for the OPE tensor (on g part only)."""
    d = T.shape[0]
    err = 0
    for a in range(1, d):  # skip vacuum
        for b in range(1, d):
            for c in range(1, d):
                total = np.zeros(d)
                for x in range(d):
                    total += T[a, b, x] * T[x, c, :]
                    total += T[b, c, x] * T[x, a, :]
                    total += T[c, a, x] * T[x, b, :]
                err = max(err, np.max(np.abs(total)))
    print(f"Jacobi error for {name}: {err:.2e}")


if __name__ == "__main__":
    print("="*60)
    print("TESTING UNREDUCED BAR COMPLEX")
    print("="*60)

    # sl_2 at various levels
    for k in [1, 0, -1, 2]:
        T = build_ope_tensor_sl2(k)
        verify_jacobi(T, f"sl_2(k={k})")
        compute_cohomology(T, f"sl_2 at k={k}", max_deg=4,
                           expected=[3, 6, 15, 36, 91])

    # sl_3 at k=1
    print("\n" + "="*60)
    T3 = build_ope_tensor_sl3(1)
    verify_jacobi(T3, "sl_3(k=1)")
    compute_cohomology(T3, "sl_3 at k=1", max_deg=3,
                       expected=[8, 36, 204])
