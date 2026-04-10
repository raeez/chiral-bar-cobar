# AP5 Cross-Volume Propagation Audit — Wave 6

Date: 2026-04-09
Scope: Vol I (`~/chiral-bar-cobar`), Vol II (`~/chiral-bar-cobar-vol2`), Vol III (`~/calabi-yau-quantum-groups`)
Mode: READ-ONLY. No .tex modifications performed.
Checks executed: 8 categories from the AP5 audit template.

---

## Section 1: Summary

| Check | Category | Vol I hits | Vol II hits | Vol III hits | Status |
|-------|----------|------------|-------------|--------------|--------|
| 1a | kappa(Heis_k) = k | 4 (correct) | 1 (correct) | 0 | CLEAN |
| 1b | kappa(Vir_c) = c/2 | ~60 (correct) | ~40 (correct) | 3 (correct) | CLEAN |
| 1c | kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v) | ~15 (correct) | ~15 (correct) | 0 | CLEAN |
| 1d | kappa(W_N) = c(H_N - 1) | 3 (correct) | 1 (correct) | 2 (correct) | CLEAN |
| 1e | kappa(W_N) = c*H_{N-1} (AP136 violation) | 0 | 0 | 0 | CLEAN |
| 2 | Bare Omega/z (AP126) in affine KM context | ~40 | ~25 | 5 | CRITICAL |
| 3 | T^c(s^{-1} A) without bar (AP132) | 2 (meta-commentary only) | 0 | 0 | CLEAN |
| 4 | Complementarity kappa+kappa'=0/=13 scoping | all scoped | all scoped | all scoped | CLEAN |
| 5 | Shadow CohFT flat identity qualifier | all scoped | all scoped | N/A | CLEAN |
| 6 | obs_g / F_g (UNIFORM-WEIGHT tag, AP32) | ~15 tagged, ~6 untagged | ~20 untagged | ~15 untagged | WARNING |
| 7a | Vol I OPE modes vs Vol II lambda-brackets (AP44) | OPE modes (correct) | lambda-brackets, c/12 (correct) | N/A | CLEAN |
| 7b | Virasoro lambda-bracket c/12 vs c/2 (V2-AP34) | N/A | all c/12 (correct) | N/A | CLEAN |
| 7c | W_3 lambda-bracket c/360 (V2-AP34) | N/A | all c/360 (correct) | N/A | CLEAN |
| 8 | Label prefix environment mismatch (AP125) | 0 | 4 | 0 | WARNING |

Headline numbers: one CRITICAL category (AP126 propagation, ~70 raw hits, a majority of which are genuine violations in affine KM context), two WARNING categories (AP32 uniform-weight tag discipline in Vols II/III prose, AP125 label-environment mismatches in Vol II `ht_physical_origins.tex`), rest CLEAN.

---

## Section 2: Critical

### C1. AP126 level-stripped r-matrix — MAIN PREFACE

**File:** `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex`
**Lines:** 515-528

Equation `\label{eq:pf1-km-kappa}` reads:
```
av(Omega/z) = dim(g)(k+h^vee)/(2h^vee) = kappa(g_hat_k)
```
The LHS must be `av(k*Omega/z)`. At `k=0` the RHS is `dim(g)/2 != 0` while the r-matrix vanishes, so the equality is false without the level. Line 526 then writes "the passage from $r(z) = \Omega/z$ to $\kappa(\widehat{\mathfrak g}_k)$" — the r-matrix in this affine KM context must be `k*Omega/z`. **This is a primary AP126 violation in the main preface, the most visible page of Vol I.**

### C2. AP126 propagation — preface variants

Same error copied to draft / v2 forms of the preface:
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:643, 652`
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:491, 501`
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542, 581, 582, 608, 683`
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2321, 2360, 2361, 2387, 2462, 3145`
- `/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex:524`
- `/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:132`

The chain `standalone/programme_summary_sections5_8.tex:132` explicitly asserts
```
av(Omega/z) = dim(fg)(k + h^vee)/(2h^vee)
```
— the same equation-level error as preface.tex, in a standalone paper.

### C3. AP126 propagation — Vol I chapters and appendices

- `/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2746` "r^{KM}(z) = \Omega/z"
- `/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2789` "The simple-pole KM r-matrix \Omega/z"
- `/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:227` "r(z) = \Omega/z = (P - 1/N)/z"
- `/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:2513` "r(z) = \Omega/z (Casimir, 24-dim)"
- `/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4654, 4686` "r(z) = \Omega/z (classical Yang-Baxter)", "The R-matrix r(z) = \Omega/z is the collision residue"
- `/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:489, 1279` "r(z) = \Omega/z" in Kac-Moody contexts
- `/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2681, 2718` "the r-matrix r(z) = \Omega/z with Casimir ..."
- `/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_preface_supplement.tex:1180` "r(z)=\Omega/z, the full Casimir element. For Virasoro: ..."
- `/Users/raeez/chiral-bar-cobar/compute/audit/standalone_paper/computations.tex:715, 739` "affine Casimir \Omega/z", table row
- `/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:3049` "and \Omega/z in the affine case"

### C4. AP126 propagation — Vol II

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2409, 2414, 4029, 4046, 4349, 4358, 4367` bare `\Omega/z` forms (multiple table rows and text); rosetta_stone is a central exposition chapter
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4029` "rational r-matrix $r_0(z) = \Omega/z + k\kappa/z^2$" — the `k` belongs on `\Omega/z`, not on the second term
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2221` "The holographic R-matrix is $r(z) = \Omega/z$"
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:261, 476, 525` "$r(z) = \Omega/z$" used in a worked CYBE verification
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:222, 269, 1899`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186, 229, 276`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:774` "residue $\Omega/(k+2)$ ... $r(z) = \Omega/z + O(1)$" — prose derives from level-stripped claim
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:521` "$r(z) = \Omega_k/z = k\,\Omega/z$" — this one is CORRECT (explicit `k`); retained for contrast
- `/Users/raeez/chiral-bar-cobar-vol2/compute/audit/non_simply_laced_rmatrix_report.tex:107` "$r_{12}(z) = \Omega/z$" (audit report)

### C5. AP126 propagation — Vol III

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:127, 142, 265, 550, 557` all bare `r(z) = \Omega/z`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2675, 5700` bare
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:148, 175` bare
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:292` "$\mathcal{R}(z) = 1 + \Omega/z + O(z^{-2})$"
- `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:35` — this one is CORRECT: "the classical r-matrix of V_k(g) is r(z) = k\,\Omega/z, so at k = -h^vee the surviving structure ..."

### C6. AP24 complementarity — no violations flagged

All 90+ occurrences of `kappa + kappa' = 0` and `kappa + kappa' = 13` that I reviewed carried explicit family qualifiers (affine KM, Virasoro, free fields, Heisenberg). No unqualified usage. Concordance and CLAUDE.md compliant.

---

## Section 3: Warnings

### W1. AP32 uniform-weight tag discipline

Many prose occurrences of `F_g = kappa * lambda_g^{FP}` or `obs_g = kappa * lambda_g` lack the explicit `(UNIFORM-WEIGHT)` parenthetical tag even though CLAUDE.md mandates it "in a theorem." The surrounding prose usually makes scope clear, but the following lack even implicit context in the same sentence:

- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:35` (opening paragraph summary of Thm D) — bare
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:3578, 3583` — table caption, bare
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:3724` — bare
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex:820` — "$F_g = \kappa \cdot \lambda_g^{FP}$" with no uniform-weight tag
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations.tex:426, 835` — bare
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5361, 5433, 5469, 5568` — rosetta-stone table and prose, bare
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:747, 1184, 1342` — bare
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3484, 7516` — bare
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:1537` — "scalar lane, $F_g(\cH_N) = \kappa \cdot \lambda_g^{FP}$" — scalar lane is implicitly uniform-weight but should carry the tag
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2712, 3506, 3923, 3982, 4002, 4593, 5132` — many bare (kappa_ch compliant but no UNIFORM-WEIGHT tag)
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:526` — bare
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1152` — "on the uniform-weight lane (Vol I, Thm D)" — scoped, OK

None are in theorem environments; all are in prose or tables. CLAUDE.md AP32 says "every occurrence in a theorem MUST carry explicit tag" so these are below the strict threshold but still represent AP32 drift. Recommendation: add a `(UNIFORM-WEIGHT)` parenthetical to table captions and to each table row/column header describing `F_g`.

### W2. AP125 label-environment mismatches (Vol II)

**File:** `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex`

Four environments carrying mismatched `rem:` labels:

1. **Line 1031:** `\begin{conjecture}[W-algebra bar-cobar duality; \ClaimStatusConjectured]\label{rem:w-algebra-bar-cobar}`
   — conjecture with `rem:` prefix; should be `conj:w-algebra-bar-cobar`

2. **Line 1276-1277:** `\begin{theorem}[HT theory from 4d N=4 SYM; \ClaimStatusProvedElsewhere]` / `\label{rem:ht-from-n4-sym}`
   — theorem with `rem:` prefix; should be `thm:ht-from-n4-sym`

3. **Line 1326-1327:** `\begin{theorem}[Boundary chiral algebra; \ClaimStatusProvedElsewhere ...]` / `\label{rem:boundary-chiral-algebra-bv}`
   — theorem with `rem:` prefix; should be `thm:boundary-chiral-algebra-bv`

4. **Line 1363-1364:** `\begin{conjecture}[Bar-cobar from HT boundary; \ClaimStatusHeuristic]` / `\label{rem:bar-cobar-ht-boundary}`
   — conjecture with `rem:` prefix; should be `conj:bar-cobar-ht-boundary`

These are AP125 violations ("Label prefix MUST match environment"). They likely arose from downgrading-then-upgrading in rectification waves. Any grep for `conj:` to count conjectures or `thm:` to count theorems will under-count these four.

### W3. Rosetta-stone table convention mixing (Vol II)

**File:** `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4029`

```
rational r-matrix $r_0(z) = \Omega/z + k\kappa/z^2$
```

The `k` is attached to the wrong term (the double-pole `k\kappa/z^2` is fine) but the first term `\Omega/z` is level-stripped. The correct affine KM r-matrix is `k*Omega/z + k*kappa/z^2` or with overall factor `k(Omega/z + kappa/z^2)`. Needs verification against the intended expression.

---

## Section 4: Benign

### B1. Yang's classical CYBE solution

Occurrences of `r(z) = \Omega/z` labelled as "Yang's solution" or "classical Yang-Baxter" refer to the universal Yang solution for the Yangian, which is independent of level. In this context the bare form is correct (the underlying algebra is the fixed Lie algebra, not the affine level-k extension):

- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex:354` "Yang's solution of the CYBE"
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3145` "Yang's solution"
- `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex:344` "(spectral form with r(z) = \Omega/z)" — definition of spectral CYBE, not affine KM

### B2. AP132 meta-commentary

Both `T^c(s^{-1} A)` without bar hits in Vol I are explicit meta-commentary citing AP132:
- `standalone/N1_koszul_meta.tex:323` "writing T^c(s^{-1} cA) instead of T^c(s^{-1} \bar\cA) would include the vacuum ... (Anti-Pattern~132 of~LorgatMKD1)"
- `standalone/N4_mc4_completion.tex:271` "writing T^c(s^{-1} cA) in place of T^c(s^{-1} \bar\cA) includes the unit and breaks the Koszul sign computation"

These are correct usage (contrasting the wrong form with the right form).

### B3. H_{N-1} in Dirichlet-sewing / Li-coefficient formulas

Hits for `H_{N-1}` in `chapters/examples/w_algebras_deep.tex:4768-4769` and `chapters/connections/genus_complete.tex:1936-2195` are inside a distinct formula (a sewing-determinant series and a Li-coefficient closed form), not in the `kappa(W_N) = c*(H_N - 1)` formula. Independent verification via surrounding context confirms the usage is correct (`(N-1)*zeta(u) - N*H_{N-1}(u) + H_{N-1}(u-1)`, etc.).

### B4. Casimir-only r-matrix in Fukaya / braided factorization contexts (Vol III)

Some Vol III hits for bare `\Omega/z` are in CY settings where the "level" is a categorical invariant (`kappa_cat`, `kappa_fiber`) that does not enter the r-matrix in the same way as affine KM level. Borderline: `braided_factorization.tex:292` and `fukaya_categories.tex:148,175` should still carry a prefix or a clarifying sentence ("level absorbed into normalization").

---

## Section 5: Recommended follow-up agents

### Tier 1 (CRITICAL, serialize)

**Agent T1.preface-ap126:** Fix `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex` AP126 violations. Must:
1. Rewrite `eq:pf1-km-kappa` (line 515-521) to `\mathrm{av}(k\,\Omega/z) = ...`.
2. Rewrite line 526 `r(z) = \Omega/z` to `r(z) = k\,\Omega/z`.
3. Fix analogous occurrences at lines 2321, 2360, 2361, 2387, 2462, 3145.
4. Propagate identical fixes to draft/v2 variants: `preface_section1_draft.tex:643,652`, `preface_section1_v2.tex:491,501`, `preface_sections5_9_draft.tex:542,581,582,608,683`, `preface_sections10_13_draft.tex:354`.
5. Also fix `standalone/programme_summary_section1.tex:524` and `standalone/programme_summary_sections5_8.tex:132`.

**Agent T1.vol1-chapters-ap126:** Fix Vol I chapter-level AP126 hits in `w_algebras_deep.tex`, `yangians_foundations.tex`, `toroidal_elliptic.tex`, `frontier_modular_holography_platonic.tex`, `thqg_introduction_supplement_body.tex`, `arithmetic_shadows.tex`, `thqg_preface_supplement.tex`, `standalone_paper/computations.tex`, `appendices/nonlinear_modular_shadows.tex`.

**Agent T1.vol2-rosetta-ap126:** Fix `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex`. At least 14 AP126 violations in tables and prose. Verify that line 4029 expression `$r_0(z) = \Omega/z + k\kappa/z^2$` is corrected to carry level on both terms (or as an overall factor).

**Agent T1.vol2-physics-ap126:** Fix `thqg_holographic_reconstruction.tex:2221`, `thqg_spectral_braiding_extensions.tex:261,476,525`, `log_ht_monodromy_core.tex:222,269,1899`, `log_ht_monodromy.tex:186,229,276`, `log_ht_monodromy_frontier.tex:774`, `compute/audit/non_simply_laced_rmatrix_report.tex:107`.

**Agent T1.vol3-ap126:** Fix Vol III hits in `chapters/examples/quantum_group_reps.tex` (5 hits), `toroidal_elliptic.tex` (2), `fukaya_categories.tex` (2), `theory/braided_factorization.tex` (1). Note: `chapters/connections/geometric_langlands.tex:35` is already correct (explicit `k\,\Omega/z`) — leave alone.

### Tier 2 (WARNING, parallelizable)

**Agent T2.ap125-vol2-hpo:** Fix the four label-prefix mismatches in `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex`. Atomic rename: update label + all `\ref{}` pointing to it in all three volumes. Lines 1031, 1276-1277, 1326-1327, 1363-1364.

**Agent T2.ap32-vol2:** Add `(UNIFORM-WEIGHT)` tags to `F_g = kappa * lambda_g^{FP}` occurrences in Vol II table captions and theorem-adjacent prose: `factorization_swiss_cheese.tex`, `foundations.tex`, `rosetta_stone.tex`, `holomorphic_topological.tex`, `3d_gravity.tex`, `thqg_bv_ht_extensions.tex`.

**Agent T2.ap32-vol3:** Same for Vol III: `toroidal_elliptic.tex` (7 hits), `k3_times_e.tex` (1 hit), and verify that each uses `kappa_ch` consistently (AP113).

**Agent T2.ap32-vol1-census:** Add `(UNIFORM-WEIGHT)` to `landscape_census.tex:35, 3578, 3583, 3724` and verify the opening summary paragraph scope.

### Tier 3 (verification)

**Agent T3.ap126-verification:** Across all three volumes, for every remaining `\Omega/z` (after Tier 1 fixes) grep for (a) the pattern `k\,\Omega/z`, (b) `\hbar\,\Omega/z`, (c) "k=0" vanishing check within 20 lines, or (d) "Yang" / "classical CYBE" context. Any hit not satisfying (a)-(d) is a residual AP126 violation.

---

## Closing note

The AP126 propagation count (a majority of ~70 hits across all three volumes after filtering out legitimate Yang/hbar/av forms) is large enough to justify a dedicated mini-sweep. The main-preface hit (C1) is the highest-priority single fix because it is on the most-read page of Vol I and contains an equation that is FALSE at k=0.

Label-prefix (AP125) hits are concentrated in one Vol II file (`ht_physical_origins.tex`). Fixable in a single atomic commit.

All other checks (kappa formulas, complementarity scoping, bar augmentation, shadow CohFT flat identity, convention consistency) are substantively CLEAN across the three volumes. Waves 1-5 have successfully stabilized these.
