#!/usr/bin/env python3
"""Debug d^2 for the chiral bar complex. Trace specific elements."""

import numpy as np
from math import factorial
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_bar_cohomology import (
    nbc_basis, residue_matrix, sl2_structure_tensor
)


def trace_d2_degree3():
    """Trace d^2 at degree 3 for sl_2 (bracket only, k=0).

    B^3 = g^3 * OS^2(C_3),  dim = 27 * 2 = 54
    B^2 = g^2 * OS^1(C_2),  dim = 9 * 1 = 9
    B^1 = g * OS^0(C_1),    dim = 3

    d_3: B^3 -> B^2 (bracket + OS residue)
    d_2: B^2 -> B^1 (bracket, trivial OS)
    d^2 = d_2 . d_3 should be zero.
    """
    f = sl2_structure_tensor()  # f[a,b,c] = [a,b]_c
    d = 3  # dim sl_2

    # OS bases
    os2_3 = nbc_basis(3, 2)  # OS^2(C_3), should have dim 2
    os1_2 = nbc_basis(2, 1)  # OS^1(C_2), should have dim 1
    os0_1 = nbc_basis(1, 0)  # OS^0(C_1), dim 1

    print(f"OS^2(C_3) basis ({len(os2_3)} elements): {os2_3}")
    print(f"OS^1(C_2) basis ({len(os1_2)} elements): {os1_2}")

    # Residue maps for n=3 (C_3 -> C_2)
    res3 = residue_matrix(3)
    for (p,q), M in sorted(res3.items()):
        print(f"  Res_D{p}{q}: {M.tolist()}")

    # Residue maps for n=2 (C_2 -> C_1)
    res2 = residue_matrix(2)
    for (p,q), M in sorted(res2.items()):
        print(f"  Res_D{p}{q} (n=2): {M.tolist()}")

    # Manual trace: element e⊗f⊗e ⊗ η₁₂∧η₂₃
    # (This is a_1=e=0, a_2=f=2, a_3=e=0, os_idx=0 for first OS basis element)
    print("\n--- Tracing d_3(e⊗f⊗e ⊗ ω_0) ---")
    a = [0, 2, 0]  # e, f, e
    os_idx = 0
    omega = os2_3[os_idx]
    print(f"  Element: a={a}, ω={omega}")

    names = ['e', 'h', 'f']

    # Sum over all pairs (p,q) with p < q
    result_terms = {}  # (target_tensor, target_os) -> coefficient

    for p in range(1, 4):
        for q in range(p+1, 4):
            # OS residue: Res_{D_pq}(omega) -> coefficient in target OS basis
            res = res3[(p, q)]
            for os_t in range(len(os1_2)):
                rc = res[os_t, os_idx]
                if abs(rc) < 1e-15:
                    continue

                # Bracket [a_p, a_q]
                ap, aq = a[p-1], a[q-1]
                for c in range(d):
                    fc = f[ap, aq, c]
                    if abs(fc) < 1e-15:
                        continue

                    # Build target tensor: replace a_p with c, remove a_q
                    tgt = list(a)
                    tgt[p-1] = c
                    del tgt[q-1]

                    # Sign
                    sign = (-1) ** (q - p - 1)

                    key = (tuple(tgt), os_t)
                    coeff = sign * fc * rc
                    result_terms[key] = result_terms.get(key, 0) + coeff
                    print(f"  (p,q)=({p},{q}): [{names[ap]},{names[aq]}]="
                          f"{fc}*{names[c]}, os_res={rc:.1f}, "
                          f"sign={sign}, tgt={[names[x] for x in tgt]}, "
                          f"coeff={coeff:.1f}")

    print("\n  d_3 result (in B^2 = g^2 * OS^1(C_2)):")
    for (tgt, os_t), coeff in sorted(result_terms.items()):
        if abs(coeff) > 1e-15:
            print(f"    {[names[x] for x in tgt]} ⊗ os_{os_t}: {coeff:.1f}")

    # Now apply d_2 to the result
    print("\n--- Applying d_2 to result ---")
    d2_result = {}  # gen -> coefficient

    for (tgt, os_t), coeff in result_terms.items():
        if abs(coeff) < 1e-15:
            continue

        # d_2: g^2 * OS^1(C_2) -> g * OS^0(C_1)
        # Only pair (1,2)
        res = res2[(1, 2)]
        for os_t2 in range(len(os0_1)):
            rc = res[os_t2, os_t]
            if abs(rc) < 1e-15:
                continue

            ap, aq = tgt[0], tgt[1]
            for c in range(d):
                fc = f[ap, aq, c]
                if abs(fc) < 1e-15:
                    continue

                sign = 1  # (-1)^{2-1-1} = 1
                contrib = coeff * sign * fc * rc
                d2_result[c] = d2_result.get(c, 0) + contrib
                print(f"    [{names[ap]},{names[aq]}]={fc}*{names[c]}, "
                      f"os_res={rc:.1f}, coeff={coeff:.1f}, contrib={contrib:.1f}")

    print("\n  d^2 result (in B^1 = g):")
    for c, v in sorted(d2_result.items()):
        print(f"    {names[c]}: {v:.1f}")

    total_err = sum(abs(v) for v in d2_result.values())
    print(f"  d^2 = {'0 ✓' if total_err < 1e-10 else 'NONZERO ✗'}")


def trace_d2_all_elements():
    """Check d^2 for ALL degree-3 elements."""
    f = sl2_structure_tensor()
    d = 3

    os2_3 = nbc_basis(3, 2)
    os1_2 = nbc_basis(2, 1)
    os0_1 = nbc_basis(1, 0)
    res3 = residue_matrix(3)
    res2 = residue_matrix(2)

    names = ['e', 'h', 'f']

    max_err = 0
    worst = None

    for a1 in range(d):
        for a2 in range(d):
            for a3 in range(d):
                for os_s in range(len(os2_3)):
                    a = [a1, a2, a3]

                    # d_3: B^3 -> B^2
                    d3_result = {}
                    for p in range(1, 4):
                        for q in range(p+1, 4):
                            res = res3[(p, q)]
                            for os_t in range(len(os1_2)):
                                rc = res[os_t, os_s]
                                if abs(rc) < 1e-15:
                                    continue
                                ap, aq = a[p-1], a[q-1]
                                for c in range(d):
                                    fc = f[ap, aq, c]
                                    if abs(fc) < 1e-15:
                                        continue
                                    tgt = list(a)
                                    tgt[p-1] = c
                                    del tgt[q-1]
                                    sign = (-1) ** (q - p - 1)
                                    key = (tuple(tgt), os_t)
                                    d3_result[key] = d3_result.get(key, 0) + sign * fc * rc

                    # d_2: B^2 -> B^1
                    d2_result = {}
                    for (tgt, os_t), coeff in d3_result.items():
                        if abs(coeff) < 1e-15:
                            continue
                        res = res2[(1, 2)]
                        for os_t2 in range(len(os0_1)):
                            rc = res[os_t2, os_t]
                            if abs(rc) < 1e-15:
                                continue
                            ap, aq = tgt[0], tgt[1]
                            for c in range(d):
                                fc = f[ap, aq, c]
                                if abs(fc) < 1e-15:
                                    continue
                                sign = 1
                                d2_result[c] = d2_result.get(c, 0) + coeff * sign * fc * rc

                    for c, v in d2_result.items():
                        if abs(v) > max_err:
                            max_err = abs(v)
                            worst = (a, os_s, c, v)

    print(f"\nMax |d^2| over all degree-3 elements: {max_err:.2e}")
    if worst:
        a, os_s, c, v = worst
        print(f"  Worst: a={[names[x] for x in a]}, os={os_s} -> "
              f"{names[c]}: {v:.1f}")


if __name__ == "__main__":
    trace_d2_degree3()
    print("\n" + "="*60)
    trace_d2_all_elements()
