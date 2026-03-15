#!/usr/bin/env python3
"""Find the correct sign convention for d^2 = 0 in the chiral bar complex.

The bar differential d: g^n * OS^{n-1}(C_n) -> g^{n-1} * OS^{n-2}(C_{n-1})
acts by:
  d(a_1 ... a_n * omega) = sum_{p<q} eps(p,q) * [a_p, a_q] * rest * Res_{pq}(omega)

We try various sign conventions eps(p,q) to find which gives d^2 = 0.
"""

import numpy as np
from math import factorial
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_bar_cohomology import (
    nbc_basis, residue_matrix, sl2_structure_tensor
)


def build_diff(f_abc, n, sign_fn):
    """Build bar differential with a custom sign function."""
    dim_g = f_abc.shape[0]
    if n <= 1:
        return np.zeros((0, dim_g))

    source_os = nbc_basis(n, n - 1)
    target_os = nbc_basis(n - 1, n - 2)
    dim_os_s = len(source_os)
    dim_os_t = len(target_os)
    source_dim = dim_g ** n * dim_os_s
    target_dim = dim_g ** (n - 1) * dim_os_t
    res_maps = residue_matrix(n)

    M = np.zeros((target_dim, source_dim))

    for src_t in range(dim_g ** n):
        gens = []
        temp = src_t
        for _ in range(n):
            gens.append(temp % dim_g)
            temp //= dim_g

        for os_s in range(dim_os_s):
            col = src_t * dim_os_s + os_s

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
                        for c in range(dim_g):
                            fc = f_abc[a_p, a_q, c]
                            if abs(fc) < 1e-15:
                                continue

                            tgt = list(gens)
                            tgt[p - 1] = c
                            del tgt[q - 1]

                            sign = sign_fn(p, q, n)

                            tgt_idx = 0
                            for i in range(len(tgt) - 1, -1, -1):
                                tgt_idx = tgt_idx * dim_g + tgt[i]
                            row = tgt_idx * dim_os_t + os_t

                            M[row, col] += sign * fc * rc

    return M


def test_sign_convention(f_abc, name, sign_fn, sign_name):
    """Test a sign convention for d^2 = 0."""
    D2 = build_diff(f_abc, 2, sign_fn)
    D3 = build_diff(f_abc, 3, sign_fn)
    D4 = build_diff(f_abc, 4, sign_fn)

    d2_23 = np.max(np.abs(D2 @ D3)) if D2.size > 0 and D3.size > 0 else 0
    d2_34 = np.max(np.abs(D3 @ D4)) if D3.size > 0 and D4.size > 0 else 0

    ok23 = "OK" if d2_23 < 1e-10 else f"FAIL({d2_23:.1f})"
    ok34 = "OK" if d2_34 < 1e-10 else f"FAIL({d2_34:.1f})"

    r2 = np.linalg.matrix_rank(D2, tol=1e-8)
    r3 = np.linalg.matrix_rank(D3, tol=1e-8)
    r4 = np.linalg.matrix_rank(D4, tol=1e-8)

    dim_g = f_abc.shape[0]
    dim_B1, dim_B2, dim_B3, dim_B4 = dim_g, dim_g**2, dim_g**3 * 2, dim_g**4 * 6

    H1 = dim_B1 - r2
    H2 = dim_B2 - r2 - r3
    H3 = dim_B3 - r3 - r4

    print(f"  {sign_name:30s}: d2_23={ok23:12s} d2_34={ok34:12s} "
          f"ranks={r2},{r3},{r4}  H1={H1} H2={H2} H3={H3}")
    return d2_23 < 1e-10 and d2_34 < 1e-10


if __name__ == "__main__":
    f = sl2_structure_tensor()
    print("Testing sign conventions for sl_2:")
    print(f"  Expected: H1=3, H2=6, H3=15")
    print()

    conventions = [
        ("(-1)^(q-p-1)", lambda p, q, n: (-1) ** (q - p - 1)),
        ("(-1)^(q-p)", lambda p, q, n: (-1) ** (q - p)),
        ("(-1)^(q-1)", lambda p, q, n: (-1) ** (q - 1)),
        ("(-1)^(p-1)", lambda p, q, n: (-1) ** (p - 1)),
        ("(-1)^(p+q)", lambda p, q, n: (-1) ** (p + q)),
        ("(-1)^(p+q+1)", lambda p, q, n: (-1) ** (p + q + 1)),
        ("+1 (no sign)", lambda p, q, n: 1),
        ("-1 (all neg)", lambda p, q, n: -1),
        ("(-1)^q", lambda p, q, n: (-1) ** q),
        ("(-1)^p", lambda p, q, n: (-1) ** p),
        ("(-1)^(n+q)", lambda p, q, n: (-1) ** (n + q)),
        ("(-1)^(n+p)", lambda p, q, n: (-1) ** (n + p)),
    ]

    for sign_name, sign_fn in conventions:
        test_sign_convention(f, "sl_2", sign_fn, sign_name)
