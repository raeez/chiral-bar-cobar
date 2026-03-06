#!/usr/bin/env python3
"""Trace d^2 for the failing element h⊗h⊗e ⊗ ω₁."""

import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chiral_bar_cohomology import (
    nbc_basis, residue_matrix, sl2_structure_tensor
)

f = sl2_structure_tensor()
d = 3
names = ['e', 'h', 'f']

os2_3 = nbc_basis(3, 2)
os1_2 = nbc_basis(2, 1)
os0_1 = nbc_basis(1, 0)
res3 = residue_matrix(3)
res2 = residue_matrix(2)

print(f"OS^2(C_3) basis: {os2_3}")
print(f"  ω_0 = {os2_3[0]} = η₁₂∧η₂₃")
print(f"  ω_1 = {os2_3[1]} = η₁₃∧η₂₃")

print(f"\nResidue maps (n=3):")
for (p,q), M in sorted(res3.items()):
    print(f"  Res_D{p}{q}: {M.tolist()}")

a = [1, 1, 0]  # h, h, e
os_s = 1  # ω_1 = η₁₃∧η₂₃
print(f"\n=== d_3({names[a[0]]}⊗{names[a[1]]}⊗{names[a[2]]} ⊗ ω_{os_s}) ===")
print(f"Element: {[names[x] for x in a]} ⊗ {os2_3[os_s]}")

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
                coeff = sign * fc * rc
                d3_result[key] = d3_result.get(key, 0) + coeff
                print(f"  ({p},{q}): [{names[ap]},{names[aq]}]={fc:.0f}*{names[c]}, "
                      f"Res={rc:.1f}, sign={sign}, "
                      f"tgt={[names[x] for x in tgt]}⊗os_{os_t}, "
                      f"coeff={coeff:.1f}")

print(f"\nd_3 result:")
for (tgt, os_t), coeff in sorted(d3_result.items()):
    if abs(coeff) > 1e-15:
        print(f"  {[names[x] for x in tgt]} ⊗ η₁₂: {coeff:.1f}")

# Now d_2
print(f"\n=== d_2 applied to result ===")
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
            contrib = coeff * sign * fc * rc
            d2_result[c] = d2_result.get(c, 0) + contrib
            print(f"  [{names[ap]},{names[aq]}]={fc:.0f}*{names[c]}, "
                  f"Res={rc:.1f}, coeff_in={coeff:.1f}, contrib={contrib:.1f}")

print(f"\nd^2 result:")
for c in range(d):
    v = d2_result.get(c, 0)
    print(f"  {names[c]}: {v:.1f}")

# Now let's check: what SHOULD the Arnold relation give?
print(f"\n=== Arnold relation check ===")
print(f"The element is h⊗h⊗e ⊗ η₁₃∧η₂₃")
print(f"Collisions contributing to d_3:")
print(f"  (1,3): Res_{os2_3[os_s]}(D_13) involves η₁₃ being removed")
print(f"  (2,3): Res_{os2_3[os_s]}(D_23) involves η₂₃ being removed")
print(f"  (1,2): Res_{os2_3[os_s]}(D_12) -- but η₁₂ not in ω₁!")
print(f"")
print(f"For ω₁ = η₁₃∧η₂₃:")
print(f"  Res_D13: removes eta_13, leaving eta_merged in C_2")
print(f"    After merging 3 into 1: relabel 1=merged, 2=original 2")
print(f"    η₂₃ becomes η_{2,merged} = η₂₁ (new labels)")
print(f"    Sign from position of η₁₃: position 0 in ω₁, sign=(-1)^0=1")
print(f"  Res_D23: removes η₂₃, leaving η_{1,merged} in C_2")
print(f"    After merging 3 into 2: relabel 1=original 1, 2=merged")
print(f"    η₁₃ becomes η_{1,merged} = η₁₂ (new labels)")
print(f"    Sign from position of η₂₃: position 1 in ω₁, sign=(-1)^1=-1")
print(f"  Res_D12: η₁₂ not in ω₁, so residue = 0")
print(f"")
print(f"Manual residue values:")
print(f"  Res_D13(ω₁) should be: -(η₂₁) = -η₁₂ (with sign from orientation)")
print(f"  Res_D23(ω₁) should be: -(η₁₂)")
print(f"  Res_D12(ω₁) should be: 0")
print(f"My code gives: Res_D13={res3[(1,3)][0,1]}, Res_D23={res3[(2,3)][0,1]}, Res_D12={res3[(1,2)][0,1]}")
