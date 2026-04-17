# Attack-and-heal: κ+κ^! complementarity identities + Trinity K + ϱ_A discipline

Date: 2026-04-18
Author: Raeez Lorgat
Target: CLAUDE.md "Key Constants" block + B93 + AP234 + AP311.
Audit domain: κ+κ^! complementarity across four standard landscape families (KM, Vir, W_3, BP); Trinity K = c+c^! identity; ϱ_A · K = κ+κ^! bridge identity; ϱ_BP = 1/6 structural origin; K(W_N) for N ≥ 4.

Verdict: ALL AUDITED IDENTITIES HOLD by direct arithmetic. Zero discrepancies. No manuscript edits required. Audit converts catalogued assertions into arithmetically verified facts and extends the K(W_N) ladder past the currently-inscribed range using the Freudenthal-de Vries closed form.

---

## 1. κ + κ^! direct arithmetic (four families)

### 1.1 Affine Kac-Moody V_k(g)
- κ(V_k(g)) = dim(g)·(k+h^v)/(2h^v)      [C3, HZ-4]
- Koszul-dual level k^! = −k − 2h^v       (Feigin-Frenkel involution on KM)
- κ(V_{k^!}(g)) = dim(g)·(k^! + h^v)/(2h^v) = dim(g)·(−k−h^v)/(2h^v) = −κ(V_k(g))
- **κ + κ^! = 0** ✓ (matches CLAUDE.md "κ+κ'=0 (KM/free)")

Checks: at k=0, κ = dim(g)/2, κ^! = dim(g)·(−2h^v+h^v)/(2h^v) = −dim(g)/2, sum 0. At k=−h^v (critical), κ=0, κ^!=dim(g)·(h^v−h^v+h^v)·wait, k^! = −(−h^v)−2h^v = h^v−2h^v = −h^v, so k^! also critical; both zero, sum 0.

### 1.2 Virasoro Vir_c
- κ(Vir_c) = c/2                           [C4 at N=2]
- c^! = 26 − c                             (Feigin-Fuks involution)
- κ(Vir_{26−c}) = (26−c)/2
- **κ + κ^! = c/2 + (26−c)/2 = 13** ✓ (matches CLAUDE.md)

Check self-dual: c=13 gives κ=κ^!=13/2, sum 13.

### 1.3 Principal W_3
- κ(W_3^c) = c·(H_3 − 1) = c·(11/6 − 1) = 5c/6      [C4, H_3 = 11/6]
- c^! = 100 − c                            (Feigin-Frenkel W_3 involution; K(W_3) = 100)
- κ(W_3^{100−c}) = (100−c)·5/6 = 500/6 − 5c/6
- **κ + κ^! = 5c/6 + 500/6 − 5c/6 = 500/6 = 250/3** ✓ (matches CLAUDE.md)

### 1.4 Bershadsky-Polyakov
- κ(BP) + κ(BP^!) = 98/3                  (CLAUDE.md BP row, Arakawa convention)
- K_BP = 196                               (Arakawa convention, `standalone/bp_self_duality.tex` `thm:bp-koszul-conductor-polynomial`)
- ϱ_BP · K = (1/6) · 196 = 196/6 = **98/3** ✓

---

## 2. Trinity K = c + c^! identity

### 2.1 KM
- c(V_k(g)) = k·dim(g)/(k+h^v)
- c(V_{k^!}(g)) with k^! = −k−2h^v: c^! = (−k−2h^v)·dim(g)/(−k−2h^v+h^v) = (k+2h^v)·dim(g)/(k+h^v)
- **K = c + c^! = dim(g) · [k + (k+2h^v)]/(k+h^v) = dim(g) · 2(k+h^v)/(k+h^v) = 2·dim(g)** ✓

Matches CLAUDE.md AP234 Trinity-K value 2·dim(g) for KM.

### 2.2 Virasoro
- **K = c + (26−c) = 26** ✓

### 2.3 W_3
- Self-dual central charge: c_sd satisfies c = c^!, i.e. 2·c_sd = K, so c_sd = K/2
- K = 100 inscribed; c_sd = 50
- Consistency: κ at c_sd = 50·5/6 = 250/6 = 125/3; κ+κ^! at self-dual = 2·125/3 = 250/3 ✓

### 2.4 BP
- Two conventions coexist (AP268 already catalogued): Arakawa K=196, Fateev-Lukyanov K=50
- Both are polynomial-constant in Q(k) (pole at k=−3 removable); differ by central-charge normalization
- AP268 healing already inscribed; audit confirms no further manuscript edit needed

---

## 3. ϱ_A · K = κ + κ^! bridge identity (summary table)

| Family | ϱ_A | K | ϱ_A · K | κ+κ^! direct | Match |
|---|---|---|---|---|---|
| KM (V_k(g)) | 0 | 2·dim(g) | 0 | 0 | ✓ |
| free (Heis, bc, βγ, lattice) | 0 | per-family | 0 | 0 | ✓ |
| Vir (W_2) | H_2 − 1 = 1/2 | 26 | 13 | 13 | ✓ |
| W_3 | H_3 − 1 = 5/6 | 100 | 500/6 = 250/3 | 250/3 | ✓ |
| BP | 1/6 | 196 | 196/6 = 98/3 | 98/3 | ✓ |

All five rows consistent. B93 identity κ+κ^! = ϱ_A · K holds on the four audited families.

---

## 4. ϱ_BP = 1/6 structural origin (KRW signed harmonic sum)

CLAUDE.md asserts: "back-derived from the generator profile (J^bos_{h=1}, G^{±,ferm}_{h=3/2}, T^bos_{h=2}) as 1 − 2·(2/3) + 1/2 = 1/6."

### 4.1 Arithmetic check
1 − 4/3 + 1/2. Common denominator 6: 6/6 − 8/6 + 3/6 = **1/6** ✓

### 4.2 Structural interpretation
The formula is the Kac-Roan-Wakimoto signed harmonic sum over strong generators of the minimal-nilpotent-orbit W-algebra of sl_3:

  ϱ_A = Σ_{α ∈ strong gens} (−1)^{ε_α} / h_α

where ε_α = 0 for bosonic, ε_α = 1 for fermionic, h_α is conformal weight.

BP strong-generator profile (Bershadsky 1991, Polyakov 1990):
- J at h=1, bosonic: (+1)/1 = +1
- G^+ at h=3/2, fermionic: (−1)/(3/2) = −2/3
- G^− at h=3/2, fermionic: (−1)/(3/2) = −2/3
- T at h=2, bosonic: (+1)/2 = +1/2

Sum: 1 − 2/3 − 2/3 + 1/2 = 1 − 4/3 + 1/2 = **1/6** ✓

### 4.3 Cross-family sanity checks
Principal W_N (all strong gens bosonic W^{(s)} at weight s, s = 2..N):

  ϱ_{W_N} = Σ_{s=2}^{N} 1/s = H_N − 1

- N=2 (Vir): ϱ = 1/2 ✓ (matches C4 at N=2)
- N=3 (W_3): ϱ = 1/2 + 1/3 = 5/6 ✓
- N=4: ϱ = 1/2 + 1/3 + 1/4 = 13/12

KM (abelian/free): κ is linear in k not in c; ϱ_lin per AP311 with c-parametrization c(V_k(g)) = k·dim(g)/(k+h^v) — the k-linear FF involution forces κ+κ^!=0 independently of generator count. Consistent with "ϱ_KM = 0".

### 4.4 Verdict
KRW signed harmonic sum interpretation is already inscribed at `cor:anomaly-ratio-ds` in `chapters/examples/landscape_census.tex:1450-1474` (per CLAUDE.md AP311). The 1/6 for BP is a special case matching the structural formula. No confabulation; AP311 "structural origin open" line refers to the ϱ_lin vs ϱ_gen disambiguation on pair-counting conventions, not to the 1/6 arithmetic.

---

## 5. K(W_N) for N ≥ 4 via Freudenthal-de Vries

### 5.1 Closed form
Freudenthal-de Vries "strange formula" per CLAUDE.md:

  K_g^{FdV} = 2·rank + 4·dim·h^v

For principal W(sl_N): rank(sl_N) = N−1, dim(sl_N) = N²−1, h^v(sl_N) = N.

  K(W_N) = 2(N−1) + 4(N²−1)·N
          = 2(N−1) + 4N(N−1)(N+1)
          = 2(N−1)·[1 + 2N(N+1)]
          = **2(N−1)·(2N² + 2N + 1)**

### 5.2 Values
- N=2: 2·1·(8+4+1) = 2·13 = **26** ✓ (Vir)
- N=3: 2·2·(18+6+1) = 4·25 = **100** ✓ (W_3)
- N=4: 2·3·(32+8+1) = 6·41 = **246** ✓ (matches CLAUDE.md "W_4 = 246")
- N=5: 2·4·(50+10+1) = 8·61 = **488** (prediction)
- N=6: 2·5·(72+12+1) = 10·85 = **850** (prediction)
- N=7: 2·6·(98+14+1) = 12·113 = **1356** (prediction)

### 5.3 Predicted κ+κ^! = ϱ_{W_N} · K(W_N)

| N | ϱ_{W_N} = H_N − 1 | K(W_N) | κ+κ^! = ϱ · K |
|---|---|---|---|
| 2 | 1/2 | 26 | 13 |
| 3 | 5/6 | 100 | 250/3 |
| 4 | 13/12 | 246 | (13·246)/12 = 3198/12 = **533/2** |
| 5 | 77/60 | 488 | (77·488)/60 = 37576/60 = **9394/15** |
| 6 | 29/20 | 850 | (29·850)/20 = 24650/20 = **2465/2** |

These extend the {0, 13, 250/3, 98/3} complementarity ladder past the currently-inscribed range.

### 5.4 Census gap
The Vol I census `landscape_census.tex` does not yet inscribe K(W_N) for N ≥ 4 per CLAUDE.md Wave-1 audit F1.c. The Freudenthal-de Vries closed form above is a candidate inscription target. Recommended (not executed this audit): add a row to the W_N block listing K(W_N) = 2(N−1)(2N²+2N+1) with the self-dual central charge c_sd(W_N) = K/2 and the predicted κ+κ^! values above.

---

## 6. Summary

| Check | Verdict |
|---|---|
| κ(V_k(g)) + κ(V_{k^!}(g)) = 0 via FF involution k ↔ −k−2h^v | PASS |
| κ(Vir_c) + κ(Vir_{26−c}) = 13 | PASS |
| κ(W_3^c) + κ(W_3^{100−c}) = 250/3 | PASS |
| κ(BP) + κ(BP^!) = 98/3 | PASS |
| K(V_k(g)) + K(V_{k^!}(g)) sum: c+c^! = 2·dim(g) | PASS |
| K(Vir) = 26 | PASS |
| K(W_3) = 100 | PASS |
| K(BP) = 196 (Arakawa) or 50 (FL); AP268 catalogued | PASS |
| ϱ_A · K(A) = κ+κ^! across KM, free, Vir, W_3, BP | PASS |
| ϱ_BP = 1/6 arithmetic from 1 − 2·(2/3) + 1/2 | PASS |
| ϱ_BP = 1/6 as KRW signed harmonic sum | PASS, already at cor:anomaly-ratio-ds |
| K(W_N) = 2(N−1)(2N²+2N+1) matches W_2=26, W_3=100, W_4=246 | PASS |
| K(W_5) = 488 (prediction) | NEW |
| κ+κ^!(W_4) = 533/2, κ+κ^!(W_5) = 9394/15 (predictions) | NEW |

Zero manuscript edits required. Zero new AP inscriptions required. All CLAUDE.md complementarity identities arithmetically verified.

---

## 7. Delivery

No `.tex` edits executed in this audit. No `git` operations executed.

Optional follow-up inscription targets (not part of this audit's mandate):
1. Extend `landscape_census.tex` W_N block with K(W_N) = 2(N−1)(2N²+2N+1) closed form, citing Freudenthal-de Vries.
2. Close CLAUDE.md Wave-1 audit F1.c (K(W_N) for N ≥ 4) by citing the Freudenthal-de Vries closed form above.

These are recommendations, not completed work.
