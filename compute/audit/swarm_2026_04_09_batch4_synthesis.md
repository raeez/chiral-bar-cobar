# Adversarial Swarm 2026-04-09 — Batch 4: Writers + Verifiers

**Scope.** 10 agents, mix of WRITERS (actionable LaTeX ready to apply) and VERIFIERS (correct Batch 3 open items + other-swarm handoffs). Coordination via `reconciliation_learnings.md`. Respects other-swarm "do not touch" list.

## 10-angle deliverables

### Angle 1 — Theorem H proof-gap fix writer

**Deliverable: COMPLETE ready-to-apply LaTeX.**

Produced:
1. New `lem:bar-cobar-DX-Ext-reduction` — ~35 lines of LaTeX with 4-step proof (bar concentration → bar-cobar resolution → E_1-module Koszul duality descent → D_X gl.dim 1 on smooth curve). **Verified non-circular** (does not cite `thm:hochschild-polynomial-growth`).
2. Updated proof of Theorem H Part (a) replacing the one-line "inheritance" at `chiral_hochschild_koszul.tex:700-725` with a clean invocation of the new lemma.
3. New `cor:theorem-h-concentration-unconditional` — the [0,2] concentration clause is UNCONDITIONAL on the Koszul locus (no generic-level needed); only dim ≤ 4 requires H4 (finite-dim center).
4. Footnote citation replaced: the incorrect "Brylinski HH*(D_X)" citation is swapped for `\cite[Proposition 1.4.6, Theorem 2.6.1]{HTT08}` (Hotta-Takeuchi-Tanisaki, **already in bibliography** at `references.tex:669`). No new bibitem needed.

**Key insight**: The descent lemma uses `thm:bar-concentration`, `thm:bar-cobar-isomorphism-main`, `thm:e1-module-koszul-duality`, `lem:bar-holonomicity`, and HTT08. **Zero circular references.**

Files affected: `chiral_hochschild_koszul.tex` (insert at L697, replace L700-725, insert at L736+).

### Angle 2 — Theorem B twisted-tensor pivot writer

**Deliverable: COMPLETE ready-to-apply LaTeX.**

Produced:
1. New `def:koszul-chiral-algebra` at `algebraic_foundations.tex:223-234` — body rewritten to reference `def:chiral-koszul-morphism` (three conditions: K_τ^{L/R} acyclic + quadratic gr + strong convergence). Label **stays the same** — zero broken cross-references.
2. Updated Theorem B statement at `bar_cobar_adjunction_inversion.tex:1611-1615` with explicit twisting-datum hypothesis.
3. Updated proof clause D2 at L1661-1672: routes through `ftm:koszul ⇒ ftm:counit` of `thm:fundamental-twisting-morphisms` via `lem:twisted-product-cone-counit` (cone identification).
4. Rewritten `rem:inversion-vs-fundamental` at L1686-1695 explaining the non-circularity: the cone lemma is proved from primitives (LV12 §2.2.5 transport), not through the (v)-cycle.
5. Cross-reference audit: 6 Vol I refs, zero Vol II/III refs. Semantically null across volumes.

**Key observation**: the rewrite is a single atomic commit across 2 files. No label renames, no \ref rewrites, no build risk.

### Angle 3 — MC3 status downgrade writer

**Deliverable: 33-item diff plan + NEW LEMMA L with full proof.**

Produced:
1. **33 diffs** across all three volumes (D1 through D33):
   - Vol I: CLAUDE.md:399, FRONTIER.md:27/246, outlook.tex:203, introduction.tex:1799/1809, standalone/introduction_full_survey.tex:4719/4729, preface:3135/3354, working_notes_frontier_2026_04.tex:324, appendices/combinatorial_frontier.tex:155, and more
   - Vol II: CLAUDE.md:81, FRONTIER.md:118, thqg_gravitational_yangian.tex:2162, twisted_holography_quantum_gravity.tex:2624, holomorphic_topological.tex:1041
   - Vol III: quantum_group_reps.tex:232, e1_chiral_algebras.tex:152, introduction.tex, FRONTIER.md
2. **New `lem:rank-independence-step2`** (Lemma L from Batch 1 Defense) with complete proof — insertion point `yangians_computations.tex` between L3140 and L3142. Proof promotes Step 2 of `thm:shifted-prefundamental-generation` from type A to all simple types via Hernandez block separation + `thm:categorical-cg-all-types`.
3. **3-layer MC3 split**: MC3a (all types CG closure), MC3b (all types DK-2/3 on eval core), MC3c (now all types via Lemma L), MC3 residual (`conj:dk-compacts-completion`).
4. **Downstream upgrades**: with Lemma L installed, `thm:shifted-prefundamental-generation`, `thm:mc3-type-a-resolution`, `prop:mc3-automatic-generalization` (Conditional → ProvedHere), and Vol II `thm:thqg-V-mc3-thick-generation` all drop the type-A hypothesis.

**Canonical replacement wording**: "MC3 proved for all simple Lie types on the evaluation-generated core; compact-to-completed DK extension remains `conj:dk-compacts-completion`; type A reduction promoted to all types via Lemma L."

### Angle 4 — MC4 status verify + upgrade

**Deliverable: DIRECT-READ VERDICT: UPGRADE, not downgrade.**

**Critical finding**: the MC4-0 upgrade has been PARTIALLY executed on disk. `thm:platonic-completion` at `nilpotent_completion.tex:944-1171` is already `\begin{theorem}[...; \ClaimStatusProvedHere]`. The legacy `conj:platonic-completion` at `main.tex:1649` is a phantomsection alias with the comment "upgraded from conj to thm".

Verified directly from source:
1. Step 1: weight-compatible SDR using L_0-semisimplicity + finite-dim eigenspaces ✓
2. Step 2: weight-graded HTT showing m_k (k≥2) strictly lowers conformal weight ✓
3. Step 3: R_A ⊆ V_0, dim V_0 < ∞ from positive-energy axiom ✓
4. Step 4: verifies H1/H2/H3 of `thm:resonance-filtered-bar-cobar` ✓
5. Universal bound: ρ(A) ≤ dim V_0 < ∞ for every positive-energy chiral algebra ✓

**Residual cleanup** (6 small diffs):
- D1: `metadata/claims.jsonl:3038` — rewrite key from `conj:platonic-completion` to `thm:platonic-completion`
- D2: `nilpotent_completion.tex:847-858` — tighten Vir-proof of `prop:resonance-ranks-standard` with one-line citation to Step 3 of `thm:platonic-completion`
- D3-D6: status table updates across CLAUDE.md/FRONTIER.md (most are already honest; minor cosmetic)

**Batch 1 Attack was WRONG**: the verdict "GAP, not FATAL" overstated. MC4 is PROVED. Batch 1 Defense was correct.

### Angle 5 — Huang 2005 bibliography writer

**Deliverable: bibliography corrections + comparison remark + Mok25 normalization.**

**CRITICAL FINDING #1**: The existing `Huang05` entry in `bibliography/references.tex:675-676` has the **WRONG TITLE**. Current says "Differential equations and intertwining operators, CCM 7 (2005), 375-400". The actual arXiv:math/0502533 paper is "Differential equations, duality and modular invariance, CCM 7 (2005), 649-706" — different paper, wrong pagination, wrong title.

Produced:
1. Corrected `Huang05a` entry (arXiv:math/0502533 with correct title and pagination)
2. New `Huang05b` (PNAS announcement, arXiv:math/0412261)
3. New `Huang08` (CCM 10 (2008), arXiv:math/0406291)
4. Backward-compat alias: keep `Huang05` key pointing at same entry as `Huang05a` to avoid churning 3 standalone/N5 citations
5. New `BorelDmodules` bibitem (for potential Theorem H backup citation; HTT08 is already primary)
6. New `rem:hs-sewing-vs-huang` comparison remark (~25 lines of LaTeX with incomparability table) ready to insert at `genus_complete.tex:1419` between end of `thm:general-hs-sewing` and `cor:hs-sewing-standard-landscape`

**CRITICAL FINDING #2**: Mok25 author name is WRONG in main bibliography. Canonical form is **"C.-P. Mok" (Chung-Pang Mok)** — verified via `standalone/references.bib:569`. Current main bib uses "S. C. Mok" (wrong — different person). Also wrong in:
- Vol II `main.tex:1745-1750` (duplicate entry!)
- `standalone/programme_summary*.tex` uses "L. Mok" (also wrong)
- `compute/lib/theorem_concordance_rectification_engine.py:91`

### Angle 6 — Theorem C UNIFORM-WEIGHT tag writer

**Deliverable: 5 ready-to-apply inline tag insertions.**

**Primary HZ-3 violation**: `e1_modular_koszul.tex:1133-1138` — scalar identity `κ+κ^!=0` / `κ+κ^!=ρ·K` stated without the uniform-weight tag. Edit 1 is the primary fix.

Also produced:
- Edit 2: `higher_genus_complementarity.tex:407-410` (remark preceding Theorem C)
- Edit 3: `genus_expansions.tex:3097-3115` (`thm:complementarity-root-datum`, multi-generator W_N clause)
- Edit 4: `genus_expansions.tex:2164-2174` (optional cosmetic on `prop:vir-complementarity`)
- Edit 5: `landscape_census.tex:3695-3715` (`rem:genus-complementarity`)

**Correction to task prompt**: the upstream target `thm:multi-weight-genus-expansion` is at `higher_genus_modular_koszul.tex:20518`, NOT 20256 as originally stated. Label verified by direct read.

**Cross-volume**: Vol II `thm:e1-theorem-C` is the coHochschild bicomodule isomorphism form, NOT the scalar identity — NO tag required. Vol III has no Theorem C analog. All other cross-refs inherit from Vol I.

### Angle 7 — 10+1+1 meta-theorem DAG auditor

**CRITICAL CORRECTION TO BATCH 3 ANGLE 1**: Angle 1 was **WRONG** about the cycle.

Direct source read of `chiral_koszul_pairs.tex:1039-1107` shows `thm:bar-concentration` is proved from `thm:pbw-koszulness-criterion` + `thm:fundamental-twisting-morphisms` + `lem:bar-holonomicity`. It does **NOT** cite `thm:bar-cobar-inversion-qi`. Angle 1's claim "(ii)⇒(v) cites Theorem B itself" is **false**.

**Actual DAG structure**: there are **FOUR** independent anchors from outside any cycle:
1. `lem:twisted-product-cone-counit` (L267-292) — cone identification K_τ^L ≃ Cone(ε_τ)[-1], LV12 §2.2.5 transport
2. `thm:pbw-koszulness-criterion` (L682-752) — filtered SS + classical Priddy
3. (iv)⇒(i) at L2155-2169 — Boardman conditional convergence + diagonal collapse
4. (ix)⇒(i) at L2127-2142 — Kac-Shapovalov determinantal argument

**Minimum anchor set**: `{lem:twisted-product-cone-counit}` alone suffices. Every condition (i)-(x) has a primitive path to (i) that doesn't cite Theorem B.

**Implication for Batch 4 Angle 2**: the twisted-tensor pivot is clean. The rescue does NOT require rewriting `def:koszul-chiral-algebra` — it's sufficient to route Theorem B's genus-0 clause through `lem:twisted-product-cone-counit` (which is already what the manuscript does). The circularity is only apparent when one misreads the definition.

### Angle 8 — prop:koszul-closure-properties writer

**Deliverable: ~40-line proposition + proof, ready to apply.**

**Important discovery**: closure properties are already **PARTIALLY proved** in scattered form:
- `prop:koszul-dual-tensor-product` at `chiral_koszul_pairs.tex:5310` (quadratic tensor closure)
- Involutivity `(A^!)^! ≃ A` asserted inline at L5002 and proved in Vol II `thm:two-colour-double-kd` at `ordered_associative_chiral_kd.tex:2853`
- Base change via `lem:pushforward-preserves-qi` + `thm:bar-cobar-inversion-functorial` at L3313-3319

The new prop **consolidates** these three fragments into a first-class statement with:
- (a) Chiral tensor product: verifies twisted-tensor, gr-quadratic, strong convergence under `\boxtimes`
- (b) Koszul dualization (involutivity): `(A^!)^! ≃ A` via `thm:fundamental-twisting-morphisms` + Verdier involution on holonomic D-modules
- (c) Smooth base change: pulls back the witnessing datum

Insertion point: `chiral_koszul_pairs.tex` after `thm:koszul-equivalences-meta` closes at L2202, before `:2937`. Label `prop:koszul-closure-properties` is unique (grep verified across all 3 volumes).

### Angle 9 — Wave 15 interweavings re-reader

**Deliverable: 8 edit sites with exact before→after text.**

**Vol I preface (Wave 15-1)**: CLEAN. L3349 + L3398-3411 correctly hedge "MC1-4 proved; MC5 partially proved", matches editorial_constitution.tex:179.

**Vol II preface (Wave 15-2) — 4 overclaim sites**:
- L29-45: Main thesis "$\cA$ determines the bulk via $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$" stated UNHEDGED. Vol II CLAUDE.md says "boundary-linear proved; global triangle conjectural" — contradicts the preface.
- L295-299: "the double is the universal boundary-bulk algebra" unhedged
- L302-307: Theorem H bulk identification without critical-level qualifier
- L630-637: "execute the boundary-bulk reconstruction programme" (mild)

**Introduction (Wave 15-4) — 4 sites**:
- L246-254: boundary-bulk thesis block unhedged (identical wording to Vol II preface)
- L645-659: `\begin{principle}[boundary-bulk reconstruction thesis]` is an **AP40 violation** (should be `\begin{conjecture}` since content is conjectural)
- L261-264 + L685-687: TWO explicit references to `def:koszul-chiral-algebra` genus-0 tautology. These BREAK under Batch 4 Angle 2's rewrite (the sentences become false once the definition is no longer the counit form)

**κ-proposition (Wave 15-9)**: CLEAN. `prop:kappa-holographic-central-charge` at `higher_genus_modular_koszul.tex:2709` is correctly `\ClaimStatusHeuristic` with explicit scope tag.

**No new MC5 propagation errors found.** The problem is the boundary-bulk thesis is stated identically unhedged in Vol I introduction (as `\begin{principle}`) and Vol II preface, while Vol I preface is correctly hedged. Recommend atomic propagation of hedged wording.

### Angle 10 — Kac-Shapovalov independence verifier

**Verdict: CONFIRMED** — both anchors are verified independent.

Direct read of `chiral_koszul_pairs.tex:2127-2142`:
1. `(ix)⇒(i)` proof: Shapovalov non-degeneracy `det G_h ≠ 0` ⇒ PBW-to-bar map `ι: Sym^ch(V)_h → barB_h(A)` injective ⇒ E_2-collapse ⇒ (ii) ⇒ (i). Only dependencies: `thm:pbw-koszulness-criterion` + classical Priddy Koszul of Sym(V). **Does NOT cite Theorem B, bar-concentration, or Theorem H.**
2. Kac-Shapovalov form is a **classical VOA-theoretic object** from the anti-involution structure; non-degeneracy is classical (Kac-Kazhdan, Feigin-Fuchs), not derived from bar cohomology.
3. `(i)⇒(ix)` also non-circular: routes through PBW strictness.

Direct read of `chiral_koszul_pairs.tex:267-312`:
- `lem:twisted-product-cone-counit` is a direct chain-level decomposition of $d_A + d_C + d_\tau^L$, identifying the double complex as `Cone(ε_τ)[-1]`. Single external citation: LV12 Lemma 2.2.5.
- **No internal circular citations.**

**Two independent anchors verified** → rescue is robust. Preferred: `def:chiral-koszul-morphism` via `lem:twisted-product-cone-counit`. Fallback: Kac-Shapovalov determinant.

---

## Key corrections to Batch 3 convergence

1. **Batch 3 Angle 1 was wrong about circularity.** The (ii)⇒(v) implication does NOT route through Theorem B. The DAG has 4 anchors, not 1.
2. **Batch 3's PBW-canonical proposal** is neither necessary nor sufficient. Use twisted-tensor canonical (def:chiral-koszul-morphism) instead.

## Key corrections to Batch 1 convergence

1. **MC4 is ALREADY PROVED**, not in need of downgrade. Batch 1 Attack overstated. The upgrade is partially executed on disk; 6 small cleanup diffs remain.

## New critical findings (not from Batch 3)

1. **Huang 2005 bibliography entry has WRONG TITLE**. The arXiv:math/0502533 paper is "Differential equations, duality and modular invariance" (CCM 7 (2005), 649-706), NOT "Differential equations and intertwining operators" (CCM 7 (2005), 375-400) as in `references.tex:675-676`. Separate paper, wrong pagination.
2. **Mok25 author is MISATTRIBUTED**. Canonical form is "C.-P. Mok" (Chung-Pang Mok, Purdue), verified via `standalone/references.bib:569`. Current main bib "S. C. Mok" is a different mathematician. Also wrong in Vol II `main.tex`, standalone programme summaries, and compute engines.
3. **`\begin{principle}` for boundary-bulk thesis at `introduction.tex:645-659` is an AP40 violation.** Content is conjectural; environment should be `\begin{conjecture}` or prose should be hedged.
4. **Two explicit `def:koszul-chiral-algebra` genus-0 tautology references in introduction.tex** (L261-264, L685-687) — these become false sentences after Batch 4 Angle 2's rewrite and must be updated atomically.
5. **AP124 violation discovered**: `def:koszul-dual-cooperad` duplicated in Vol I `algebraic_foundations.tex:1675` and Vol II `relative_feynman_transform.tex:942`.

## Batch 4 convergent action list (all actionable LaTeX available)

Ready to apply, each deliverable listed above:

1. **Theorem H descent lemma + updated proof + new corollary** (Angle 1) → apply to `chiral_hochschild_koszul.tex`
2. **Theorem B twisted-tensor pivot** (Angle 2) → apply to `algebraic_foundations.tex` + `bar_cobar_adjunction_inversion.tex`
3. **MC3 33-item status downgrade + Lemma L** (Angle 3) → apply across all 3 volumes + new lemma in `yangians_computations.tex`
4. **MC4 finalization** (Angle 4) → 6 small diffs in `nilpotent_completion.tex`, `metadata/claims.jsonl`, main bib
5. **Huang 2005 bibliography correction** (Angle 5) → fix `references.tex:675-676`, add Huang05a/b/08, add `rem:hs-sewing-vs-huang` to `genus_complete.tex`
6. **Mok25 author normalization** (Angle 5) → fix `references.tex:927-928`, Vol II `main.tex:1745-1750`, standalone programme summaries
7. **Theorem C UNIFORM-WEIGHT tags** (Angle 6) → 5 inline insertions
8. **prop:koszul-closure-properties** (Angle 8) → insert after `thm:koszul-equivalences-meta` at `chiral_koszul_pairs.tex:2202`
9. **Wave 15 boundary-bulk thesis hedging** (Angle 9) → 8 edits across Vol I intro + Vol II preface
10. **`\begin{principle}` → `\begin{conjecture}` atomic rename** (Angle 9) → introduction.tex:645-659 with label update

**Total batch 4 deliverables**: 10 independent fix packages, all with ready-to-apply LaTeX. No further adversarial work needed to close these items; they're awaiting application.

## Open items for Batch 5+

- **Vol II/III backbone theorem audits** (not yet touched by any swarm)
- **Seven Faces of r(z)** for both Vol I and Vol II (R-matrix, Yangian, Sklyanin, DK, celestial, holographic, Drinfeld double)
- **Physics identifications**: Costello-Gaiotto-Dimofte slab structure, BV-BRST = bar status, entanglement S_EE derivation
- **Compute engine deep audit** for remaining AP94/AP128 infections (partially handled by other swarm)
- **Wave 15 interweavings beyond the 4 targets** (other Wave 15 subwaves not yet read)
- **AP124 `def:koszul-dual-cooperad` cross-volume duplication** (pre-existing, separate rectification)
- **Full bibliography audit** for other misattributed / wrong-title entries (Huang was one; how many others?)
