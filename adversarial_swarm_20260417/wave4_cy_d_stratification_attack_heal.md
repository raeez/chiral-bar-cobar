# Wave 4 — CY-D Dimension Stratification Attack / Heal

Target: `~/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex`
(1373 lines), plus engine `compute/lib/kappa_bkm_universal.py` and sibling
`compute/lib/diagonal_siegel_cy_orbifolds.py`.

Date: 2026-04-17. Beilinson-adversarial audit against primary source (AP2).

## Scope

- `thm:kappa-hodge-supertrace-identification` (κ_ch = Hodge supertrace Ξ).
- `thm:kappa-stratification-by-d` (dimension-by-dimension table).
- `thm:cy-d-tri-stratum` (odd-d / strict-CY / HK tri-stratification).
- `cor:conifold-non-local-surface`.
- `thm:borcherds-weight-kappa-BKM-universal` (κ_BKM = c_N(0)/2).

## Phase 1. First-principles attack

### A. Supertrace numerical consistency (independent Künneth check)

Python convolution of h^{0,•} columns verified:

| manifold | column h^{0,•} | Ξ | claim | verdict |
|---|---|---|---|---|
| E | (1,1) | 0 | 0 | OK |
| K3 | (1,0,1) | 2 | 2 | OK |
| E×E | (1,2,1) | 0 | 0 | OK |
| bielliptic | (1,1,0) | 0 | 0 | OK |
| quintic X_5 | (1,0,0,1) | 0 | 0 | OK |
| K3×E | (1,1,1,1) | 0 | 0 | OK |
| E^3 | (1,3,3,1) | 0 | 0 | OK |
| sextic X_6 | (1,0,0,0,1) | 2 | 2 | OK |
| K3^[2] | (1,0,1,0,1) | 3 | 3 | OK |
| septic X_7 | (1,0,0,0,0,1) | 0 | 0 | OK |
| K3×X_5 | (1,0,1,1,0,1) | 0 | 0 | OK |

All in-body numerical Ξ values survive first-principles verification.

### B. CRITICAL: preamble contradicts body (Finding 9)

Lines 30–32:

> κ_ch is demonstrably nonzero on standard examples such as K3×E
> (where κ_ch = 3 by Vol I additivity)

**Both claims wrong.** Body + direct supertrace give κ_ch(K3×E) = Ξ = 0
(column (1,1,1,1)). The value 3 is not produced by any correct rule; it
appears to be a lingering relic of conflation between:

- VolI Heisenberg κ = k = 1 for H_1, and
- VolII additivity myth κ(X × Y) = κ(X) + κ(Y),

yielding the pseudo-computation 2 + 1 = 3. Both conventions are rejected by
the chapter itself (line 394–406 inscribes κ_ch(Φ_1(E)) = 0; line 417 gives
κ_ch(E × E) = 0 by direct supertrace). Preamble edit required.

### C. CRITICAL: "Vol I additivity" is a category error (Finding 10, 11)

Lines 153–155 and 463–466 assert
  κ_ch(X × Y) = κ_ch(X) + κ_ch(Y)
for product CY manifolds. The Hodge supertrace Ξ is **Künneth-multiplicative**,
not additive: the Poincaré polynomial of the structure-sheaf column
satisfies P_{X×Y}(t) = P_X(t) · P_Y(t), hence Ξ(X×Y) = Ξ(X) · Ξ(Y).

Evidence:
- Ξ(K3) · Ξ(E) = 2 · 0 = 0 = Ξ(K3 × E) ✓
- Ξ(K3) · Ξ(K3) = 4 = Ξ(K3 × K3) ✓ (Künneth column (1,0,2,0,1))
- Additive rule would give 2 + 2 = 4 — coincidence at this point.
  Distinguishing test Ξ(K3 × K3^[2]) would give Ξ_mult = 2 · 3 = 6 vs
  Ξ_add = 2 + 3 = 5. No such example inscribed; additive = multiplicative
  coincidentally on the existing table because at least one factor is
  always 0 or equal.

The tautology masking this error is that every product in the stratification
table has Ξ = 0 (forced by odd-d Serre on at least one factor). Healing edit:
state Künneth multiplicativity explicitly; retract "additivity".

### D. Stratum III vs K3 double-placement (Finding 2, 3)

Lines 359–366 assert K3 sits "simultaneously in stratum (II) (strict CY with
h^{2,0}=1 giving Ξ = 1 + 1 + 1 = 3, discrepancy reconciled by the
holomorphic-symplectic compatibility on h^{1,1})". Mathematically wrong.

K3 has h^{0,•} = (1, 0, 1), giving Ξ = 1 − 0 + 1 = 2. There is no
"1 + 1 + 1 = 3" computation: the middle term is h^{0,1} = 0, not 1.
Stratum-II formula Ξ = 1 + (−1)^{d/2} h^{0,d/2} + 1 at d=2, h^{0,1}=0 gives
1 + 0 + 1 = 2, consistent with stratum-III's n+1 = 2 at n=1.

The remark seems to confuse h^{1,1} = 20 (middle COLUMN of K3's Hodge
diamond) with h^{0,1} = 0 (middle of the structure-sheaf supertrace column).
The remark needs rewriting: K3 is in both strata because stratum-II and
stratum-III coincide at d=2 with h^{0,1} = 0; no "reconciliation via h^{1,1}"
is needed or possible.

### E. Proof of supertrace identification (Finding 17)

Theorem `thm:kappa-hodge-supertrace-identification` step 2 says:

> the averaging map av picks out the diagonal p = 0 component of Hodge
> cohomology: only the H^q(X, Ω^0_X) = H^q(X, O_X) part pairs with the CY
> trace. Higher p components are killed by the diagonal supertrace...

This is underjustified. The Mukai pairing on HH_* is nondegenerate on
⊕_{p+q=0} H^q(X, Ω^{-p}); the CY trace on HC^-_d evaluates on HH_0 =
⊕_{p=q} H^q(Ω^p), not on the p = 0 column alone. The **numerical** outcome
Ξ = χ(O_X) for compact CY is correct (Hodge symmetry h^{0,q} = h^{q,0}
connects the two), but the argument "only p=0 survives" does not hold as
written. The healing minimally rephrases step 2: the Hodge-filtered
supertrace Ξ(X) = χ_0(X) is the restriction of the HKR graded-trace to the
first Hodge-filtration piece F^d/F^{d−1} of de Rham cohomology, whose
representative is the (0, •) column. No "killing" of higher p is claimed;
the chiral κ is by construction the p=0 component of the full HKR trace.

### F. BKM weights (Finding 8, RESOLVED)

Engine `diagonal_siegel_cy_orbifolds.py` FRAME_SHAPE_DATA:

  N=1: c_1(0)=10, weight 5 (Gritsenko Δ_5, level-1 paramodular)
  N=2: c_2(0)=8,  weight 4
  N=3: c_3(0)=6,  weight 3
  N=4: c_4(0)=4,  weight 2
  N=5: c_5(0)=4,  weight 2
  N=6: c_6(0)=2,  weight 1
  N=7: c_7(0)=2,  weight 1
  N=8: c_8(0)=2,  weight 1

Chapter's five-frame claim {5,4,3,2,1} at N ∈ {1,2,3,4,6} matches the engine
exactly. Gritsenko Δ_5 weight-5 for N=1 is authoritative (Gritsenko 1999
"Arithmetical lifting"; not Igusa's weight-10 χ_{10}, which lives in a
different automorphic context). **Statement, proof, and engine all agree
on 5.** The prior CLAUDE.md note on disagreement is stale post-healing.

### G. Stratum-III mutual exclusivity restriction (Finding 5, latent)

The mutual-exclusivity proof (lines 337–344) uses the h^{1,0} = 0 hypothesis
to eliminate the torus factor. But the main stratification-by-d theorem
(lines 382–457) DOES include abelian surface (h^{1,0} = 2) as a d=2 entry
with Ξ = 0, placing it outside the stratum-II/III partition. This is
consistent when read carefully — abelian surface lies in the "torus factor"
excluded from stratum-II/III. No healing needed, but scope tag helps.

### H. Dead refs to thm:cy-d-d2/d3-stratification (Finding 20)

Line 1019–1020:

> Theorems~\ref{thm:cy-d-d2-stratification},
> \ref{thm:cy-d-d3-stratification}, ...

Neither label is defined in the chapter (only d4, d5 exist). Repoint to
`thm:kappa-stratification-by-d`.

### I. Section header incomplete (Finding 18)

Line 1063: `\section{Conifold, non-compact, and the}` — missing completion.
Heal to `\section{Conifold, non-compact toric, and the open frontier}`.

### J. Metadata-leak empty parentheticals (Finding 19)

Lines 1104, 1206, 1242–1244: empty `(…)` with AP-scrubbed labels. Pattern
#221 (AP236). Delete the empty parentheticals; retain mathematical content.

### K. Label prefix vs environment mismatch (Finding 21)

Proposition at line 1130 carries label `thm:borcherds-weight-kappa-BKM-universal`
(plus alias `prop:kappa-BKM-universal-cy-strat`). Environment is `\begin{proposition}`.
Per HZ-2, prefix should match. Options:

- (a) rename label to `prop:…` — O(N) debt across chapters, standalones,
  tests, notes, FRONTIER.md, CLAUDE.md theorem-status table.
- (b) upgrade environment to `\begin{theorem}` — preserves cross-refs.

Option (b) is cleaner because the label `thm:…` is canonical in the theorem
status table. Heal: replace `\begin{proposition}…\end{proposition}` with
`\begin{theorem}…\end{theorem}`, keep both labels (the alias `prop:…` stays
for intra-chapter redundant reference, but the `thm:…` label is now prefix-
matched to the theorem environment). Test file AP40 discipline preserved.

### L. Conifold McKay κ_ch = 1 (Finding 15)

The proof sketch is thin (single compact cycle ⇒ "one Heisenberg mode of
level 1 ⇒ κ = 1") but not contradicted. The conifold's Klebanov-Witten
quiver has path algebra whose HH_0 dimension is consistent with a
one-dimensional abelian shadow. Leave as ProvedHere with the stated
direct-McKay computation; record that the deeper verification is open.

## Phase 2. Heal plan

Surgical edits to `cy_d_kappa_stratification.tex`:

1. **Preamble (lines 26–47):** Rewrite to remove the false "κ_ch = 3 by Vol I
   additivity" claim for K3×E. Use Künneth multiplicativity instead; the
   motivating tension is not "supertrace nonzero at odd d" (it isn't) but
   the replacement of the naive χ(O_X) claim by the supertrace identity
   at even d with h^{1,0} ≠ 0.

2. **Lines 153–155, 463–466:** Replace "Vol I additivity κ(X×Y) = κ(X) + κ(Y)"
   with Künneth multiplicativity Ξ(X×Y) = Ξ(X) · Ξ(Y). Note additivity
   holds coincidentally on the table because at least one factor has Ξ = 0.

3. **Remark `rem:kappa-ch-landscape-even-d` (lines 359–366):** Rewrite the
   "K3 simultaneously in stratum II and III" to delete the nonsense
   "Ξ = 1 + 1 + 1 = 3" and "reconciled by h^{1,1}" sentences. State
   cleanly that at d=2 with h^{1,0}=0, stratum-II formula and stratum-III
   formula give the SAME value Ξ=2 (no reconciliation needed).

4. **Proof step 2 of `thm:kappa-hodge-supertrace-identification` (lines 196–208):**
   Rephrase to "the HKR trace restricted to the first Hodge-filtration
   piece F^d/F^{d−1} is the (0,•) supertrace Ξ(X) = χ_0(X); higher Hodge
   columns contribute to the full categorical trace but not to the chiral
   κ_ch by construction." Avoid the wrong "killing by diagonal supertrace"
   formulation.

5. **Section header line 1063:** Complete to "Conifold, non-compact toric,
   and the open frontier".

6. **Lines 1019–1020 dead refs:** Repoint to `thm:kappa-stratification-by-d`.

7. **Metadata-leak empty parentheticals (lines 1104, 1206, 1242–1244):**
   Delete the empty "()" tokens; retain the mathematical content.

8. **Proposition → theorem at line 1130:** Upgrade environment to match
   the `thm:` label prefix. The inner proof is already consistent.

9. **Remove the word "retracted" and related metacognitive commentary
   inside the manuscript (HEAL 2026-04-17 block line 1156–1160)** — move
   to comment-only form per Manuscript Metadata Hygiene.

Engine: no numerical change required (all Ξ values and BKM weights already
match first-principles verification).

## Phase 3. Residual open

- The proof of `thm:kappa-hodge-supertrace-identification` step 2 remains
  schematic (HKR-filtration p=0 projection is asserted, not derived from
  the Vol I averaging map). This is a structural weakness of the
  CY-to-chiral functor's trace construction, not a numerical error. Flag
  as a minor proof-depth gap for a later refinement pass.

- The conifold Klebanov-Witten McKay computation (Corollary) is stated
  without engine verification. Recommend adding a small conifold-HH
  compute as a future wave.

- The mutual-exclusivity restriction of `thm:cy-d-tri-stratum` to
  h^{1,0} = 0 is correct but could be stated explicitly in the theorem
  statement (not only in the proof).
