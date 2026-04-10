# Adversarial Swarm 2026-04-09 — Batch 3: Theorem B circularity deep audit

**Scope.** 10 agents, 10 distinct angles on Theorem B genus-0 circularity. Read-only. The Wave-0 finding (Theorem B genus-0 clause is definition-unfolded against `def:koszul-chiral-algebra`) gets the highest-resolution adversarial pass. Vol I theorem statement is `thm:bar-cobar-inversion-qi` at `chapters/theory/bar_cobar_adjunction_inversion.tex:1604-1715`.

## Files of record

- Statement: `chapters/theory/bar_cobar_adjunction_inversion.tex:1604-1715`
- Current canonical def: `chapters/theory/algebraic_foundations.tex:223-234` (`def:koszul-chiral-algebra`)
- Equivalent formulations remark: `algebraic_foundations.tex:273-298` (`rem:equivalent-formulations-koszul`)
- Morphism-level def (alternative canonical): `chapters/theory/chiral_koszul_pairs.tex:234-246` (`def:chiral-koszul-morphism`)
- Fundamental twisting morphisms: `chiral_koszul_pairs.tex:342-414` (`thm:fundamental-twisting-morphisms`)
- 10+1+1 meta-theorem: `chiral_koszul_pairs.tex:1900-2202` (`thm:koszul-equivalences-meta`)
- Load-bearing cone lemma: `chiral_koszul_pairs.tex:267-312` (`lem:twisted-product-cone-counit`)
- PBW criterion: `chiral_koszul_pairs.tex:682-752` (`thm:pbw-koszulness-criterion`)
- Manuscript's own concession: `bar_cobar_adjunction_inversion.tex:1686-1695` (`rem:inversion-vs-fundamental`)
- Higher-genus inversion: `chapters/theory/higher_genus_complementarity.tex:4065-4136` (`thm:higher-genus-inversion`)

## 10-angle reports (compact)

### Angle 1 — Hostile-deep prosecutor

**Verdict: CIRCULAR-EQUIVALENCES (attack succeeds at meta-level).**

Critical finding: **the 10+1+1 equivalences form a cycle that passes through (v).** Specific quotations:

- `chiral_koszul_pairs.tex:1975-1978` — "(ii)⇒(v): E_2-collapse gives bar concentration (`thm:bar-concentration`), which is the input for bar-cobar inversion (`thm:bar-cobar-inversion-qi`)."
- `chiral_koszul_pairs.tex:1981-1986` — "(v)⇒(i): The bar-cobar counit being a qi means the twisted tensor product K_τ^L is acyclic (`lem:twisted-product-cone-counit`), which is condition (1) of `def:chiral-koszul-morphism`."

**The proof of (ii)⇒(v) cites Theorem B itself.** After substituting "Koszul := PBW collapse", the rewritten statement becomes "(ii)⇒(v)", whose only proof in the manuscript IS "(v) by Theorem `thm:bar-cobar-inversion-qi`" — pure tautology.

Further chain: (i)⇔(vi) at L2095 states "(vi)⇒(i): Conservativity... by bar-cobar inversion (v)". (viii)⇒(v) at L1997 uses "already established (iv)⇒(i)⇒(v)". (iv)⇒(i) at L2155 re-derives E_2-collapse.

**The ONE viable anchor: condition (ix) Kac-Shapovalov determinant**, whose (ix)⇒(i) proof at L2127-2142 is a PBW-strictness argument that does NOT invoke (v). This is the only arrow into (i) from outside the (v)-cycle.

**CRITICAL IMPLICATION**: No naive PBW pivot works. The rescue must either (A) use Kac-Shapovalov as canonical, or (B) use `def:chiral-koszul-morphism` (twisted-tensor acyclicity) where `lem:twisted-product-cone-counit` IS proved from primitives (cone identification, L280-292, genuine Loday-Vallette Thm 2.2.5 transport).

### Angle 2 — Steelman PBW canonical

**Verdict: RESCUABLE-WITH-REWRITE** (but see Angle 1 for the circularity caveat).

Argues PBW is most intrinsic: only uses F_• and gr_F A = vertex Poisson, no B(A)/Ω/A^!. Provides verbatim rewrite of definition + new Theorem B statement. 6 Vol I references, zero Vol II/III. All family-specific theorems already discharge the new hypotheses (KM, Vir, W_N all verified via Priddy + thm:pbw-koszulness-criterion).

**Problem** (exposed by Angle 1): PBW is inside the (v)-cycle. (ii)⇒(v) routes through `thm:bar-concentration` which cites `thm:bar-cobar-inversion-qi`. The rewrite relocates circularity rather than eliminating it.

### Angle 3 — Alt-def Ext-diagonal (iv)

**Verdict: BETTER-THAN-PBW.**

- Classical precedent: BGS96 takes Ext-diagonal as canonical for quadratic algebras
- Already the canonical higher-genus axiom: `bar_cobar_adjunction_inversion.tex:1706-1707` "axiom MK:modular: PBW degeneration at genus g, equivalently diagonal Ext vanishing"
- Module-theoretic, bridges to rep theory via BGG/parabolic O
- Family verification via `free_fields.tex:2388`, `kac_moody.tex:3708, 3945`, `w_algebras.tex:1656, 2038`
- **Caveat**: uses `cor:bar-computes-ext` (ProvedElsewhere, Beilinson-Drinfeld comparison) as load-bearing external dependency. Should be upgraded to first-class theorem with in-house proof.

Proof of "(iv) ⇒ counit qi": Ext-diagonal ⇒ (via `cor:bar-computes-ext`) H*(B(A)) concentrated on diagonal ⇒ Boardman convergence + split PBW ⇒ bar concentration ⇒ counit qi via Thm B clause D2. Substantive: the Boardman convergence + extension-splitting step is non-trivial chain-level work.

### Angle 4 — Alt-def twisted-tensor (def:chiral-koszul-morphism)

**Verdict: BETTER-THAN-PBW.**

- `thm:koszul-equivalences-meta` already cites `def:chiral-koszul-morphism` as condition (i) — it's already implicitly canonical
- `lem:twisted-product-cone-counit` IS proved at L267-340 (`\ClaimStatusProvedHere`) via LV12 Lemma 2.2.5 transport
- Handles non-quadratic families (Vir, W_N, Yangians) natively — PBW requires quadraticity
- `thm:fundamental-twisting-morphisms` equates four conditions directly, providing a self-contained proof structure

Proof under this choice: "(twisted-tensor acyclicity) ⇒ (counit qi)" via `ftm:koszul ⇒ ftm:counit`, using `lem:twisted-product-cone-counit` to identify K_τ^L ≃ Cone(ε_τ)[-1]. Complete at genus 0 from primitives.

**Caveat**: closure under tensor/dual/base change not proved; should add `prop:koszul-closure-properties`.

### Angle 5 — Alt-def bar A_∞-formality (iii)

**Verdict: BETTER AS STATEMENT, IMPRACTICAL AS WORKING DEF.**

- Conceptually canonical (aligns with LV12 §3.4)
- Makes AP14 (bar formality vs SC formality) impossible to re-introduce
- All standard families are bar-formal via Priddy on gr_F

**But**: verifying bar formality directly requires constructing the HPL retract and checking transferred m_n = 0 at infinitely many arities on every FM stratum. No family is ever verified this way in the manuscript.

Recommendation: promote (iii) to a **co-definition** ("Koszul means any of [twisted-tensor acyclicity / PBW E_2 collapse / bar formality]"), emphasizing bar formality as the intrinsic content and twisted-tensor as the working tool.

### Angle 6 — Surviving content cataloguer

**Verdict: 7/8 ≈ 88% of Theorem B is non-tautological.**

Clause-by-clause:
| # | Clause | Tautology class |
|---|---|---|
| 1 | ψ is morphism of chiral algebras (A_∞-level) | NON-TAUT |
| 2a | Genus-0 ψ_0 qi | TAUT/DEPENDS-ON-DEF |
| 2b | **Genus-g ψ_g qi for g ≥ 1** | NON-TAUT (MK3, normal-crossing MV) |
| 3 | ℏ-adic convergence | NON-TAUT |
| 4a | Spectral sequence existence | structural |
| 4b | E_1, E_2 page identification | NON-TAUT |
| 4c | E_2 collapse | NON-TAUT |
| 5 | qi as chiral-algebra map, not merely chain | NON-TAUT |
| 6 | L_∞-lift (rem:bar-cobar-inversion-linfty) | NON-TAUT |
| 7 | Off-Koszul persistence | scope |

**Recommended splitting**: Split monolith into B.0/B.1/B.2/B.3/B.4 to isolate the fragile piece. Theorem B.0 can be downgraded to `\begin{proposition}` (citing `thm:fundamental-twisting-morphisms`) without affecting ~85% of downstream citers (who reference B.1, B.3, or B.4).

### Angle 7 — Cross-volume definition propagation

**Verdict: SEMANTICALLY NULL across volumes.**

- Vol I: 6 `\ref{def:koszul-chiral-algebra}` sites, all within Vol I
- Vol II: **ZERO** `\ref{def:koszul-chiral-algebra}`. Uses the notion by prose name only. Has own `def:GLZ_Koszul` in `connections/bar-cobar-review.tex:80` (lambda-bracket adapted, convention-specific)
- Vol III: **ZERO** references. No `def:koszul-chiral-algebra`. Has only `def:koszul-dual-root-datum` (BKM motivic, unrelated)
- AP113 kappa discipline unaffected: PBW definition has no kappa subscripts
- **AP124 violation discovered (pre-existing)**: `def:koszul-dual-cooperad` is duplicated in Vol I `algebraic_foundations.tex:1675` AND Vol II `connections/relative_feynman_transform.tex:942`. Flag for separate rectification.

**Implication**: any canonical rewrite in Vol I is semantically safe for Vol II/III (no broken references). Label stays `def:koszul-chiral-algebra`; only body changes.

### Angle 8 — Missing-lemma writer: "PBW E_2 ⇒ counit qi"

**Produced complete 7-step proof.**

Steps:
1. Construct PBW spectral sequence on Ω(B̄(A)) via F_•-induced cobar filtration
2. E_1 = bar of gr_F A (uses flatness of F_•)
3. PBW hypothesis ⇒ E_1^{p,q} = 0 for p+q > 0 ⇒ E_2 = E_∞ concentrated on q=0
4. Boardman conditional convergence ⇒ E_∞ ≅ gr H*(Ω(B̄(A)))
5. Compute cobar of identified E_∞
6. Identify canonical map
7. Conclude qi via filtered five-lemma

**ONE new lemma required**: `lem:pbw-boardman-convergence` — "Under (F)+(B), the PBW filtration on Ω(B̄(A)) satisfies lim¹_r E_r = 0 and the spectral sequence converges strongly to H*Ω(B̄(A))." Proof: finite-dim (n,h)-pieces make each fixed weight a finite filtration; lim¹ = 0 termwise; take direct sum.

Insertion point: after `thm:pbw-koszulness-criterion` at `chiral_koszul_pairs.tex:752`, labelled `thm:pbw-implies-counit-qi`.

**Problem**: Angle 1 shows this lemma would still be circular because Step 4 (Boardman convergence) routes through `cor:bar-cobar-inverse` at `cobar_construction.tex:1495-1505`, which itself uses Theorem B. Need to verify Step 4 can be proved independently.

### Angle 9 — Counterexample searcher

**Verdict: BRITTLE WITHIN SCOPE, FALSE OUTSIDE SCOPE.**

- Within the 12 certified standard families: **no counterexample** to (ii) ⇔ (v)
- Critical level sl_2 (k=-h^v): landscape_census says Koszul; not a counterexample
- Minimal model L(c_{3,4},0): proved NOT Koszul via (ix) Kac-Shapovalov failure (null at h=6); consistent
- `thm:fundamental-twisting-morphisms` is tagged `[Regime: quadratic]` — non-quadratic chiral algebras are OUTSIDE scope
- (v)⇒(ii) is NOT self-contained: routes (v)⇒(i)⇒(ii), with the second arrow being "immediate converse" one-liner at L1972

**Key warning**: Non-quadratic families (curved deformations, cubic OPE families hinted in Vol II) would satisfy (v) vacuously (no E_2 to collapse). Any rewrite MUST explicitly scope to quadratic algebras.

### Angle 10 — Edit planner

**Verdict: 5 edits, 2 files, single atomic commit, LOW build risk.**

Edit 1 (primary): `algebraic_foundations.tex:223-234` — rewrite def body
Edit 2: `algebraic_foundations.tex:276-290` — update equivalent formulations remark
Edit 3: `bar_cobar_adjunction_inversion.tex:1611-1615` — adjust Theorem B wording
Edit 4: `bar_cobar_adjunction_inversion.tex:1686-1695` — rewrite rem:inversion-vs-fundamental
Edit 5: `bar_cobar_adjunction_inversion.tex:1697-1709` — update higher-genus conditionality phrasing

Verify-only (no change): `higher_genus_foundations.tex:5353`, `chiral_koszul_pairs.tex:614`
Cross-volume: Vol II zero, Vol III zero — no edits needed.
Metadata auto-regenerated via `scripts/generate_metadata.py`.

---

## Convergent verdict on Theorem B (Batch 3)

**Status: RESCUABLE, but NOT via the naive PBW-canonical approach.**

### Key discovery from Angle 1 (overrules Batch 1 convergence)

Batch 1 concluded "make PBW E_2-collapse the canonical Koszul definition". Angle 1 shows this **still circular**: the proof of (ii)⇒(v) cites Theorem B itself. The (v)-cycle in `thm:koszul-equivalences-meta` includes PBW (ii), Ext-diagonal (iv), bar formality (iii), and BBL (vi). All four routes back to (v) go through Theorem B.

**The only anchor from OUTSIDE the cycle is condition (ix) Kac-Shapovalov determinant** whose (ix)⇒(i) proof is an independent PBW-strictness argument.

### Three viable canonical candidates (ranked)

1. **`def:chiral-koszul-morphism` (twisted-tensor acyclicity)** — **PREFERRED**
   - Already condition (i) in meta-theorem, so no renumbering
   - `lem:twisted-product-cone-counit` is proved from primitives (cone identification, LV12 §2.2.5)
   - Handles non-quadratic cases
   - (i)⇒(v) via cone lemma is NOT circular (direct acyclicity computation)
   - Problem: requires closure under tensor/dual/base change proposition (currently unproved)

2. **(ix) Kac-Shapovalov determinant** — alternative anchor
   - The only arrow into (i) from outside the (v)-cycle
   - Intrinsic (determinant of a pairing on A itself)
   - Proof of (ix)⇒(i) at L2127-2142 is self-contained
   - Problem: less natural as a "definition"; feels like a verification criterion

3. **Ext-diagonal (iv)** — classically canonical but circular within the manuscript
   - Already the higher-genus axiom (MK:modular)
   - Matches BGS96 precedent
   - Problem: (iv)⇒(i) at L2155 re-derives E_2-collapse through (v)

### Required fixes (revised from Batch 1)

1. **Promote `def:chiral-koszul-morphism` to the canonical "Koszul chiral algebra" definition.** Keep `def:koszul-chiral-algebra` as a named alias for backward compatibility, but redirect its body to cite the morphism-level definition. Specifically: rewrite `algebraic_foundations.tex:223-234` to say "A chiral algebra A is Koszul if it admits a twisting datum (A, C, τ, F_•) such that the twisted tensor products K_τ^{L/R} are acyclic and the filtration gr gives a classical Koszul pair." Reference `def:chiral-koszul-morphism:234-246` for the full definition.

2. **State Theorem B explicitly as "twisted-tensor acyclicity ⇒ counit qi".** The genus-0 clause is then a direct application of `lem:twisted-product-cone-counit` via cone identification K_τ^L ≃ Cone(ε_τ)[-1].

3. **Add `prop:koszul-closure-properties`** — closure of Koszul-ness under chiral tensor product, dualization, base change. Not currently proved; needed to make the morphism-level definition as robust as the property-of-A-alone definition.

4. **Explicitly state quadratic-regime restriction** in the theorem hypothesis. Non-quadratic algebras lie outside scope.

5. **Split Theorem B into B.0/B.1/B.2/B.3/B.4** per Angle 6, isolating the fragile genus-0 clause to a small corollary (B.0) and making the substantive content (B.1 higher genus, B.3 spectral sequence, B.4 L_∞-lift) visible to downstream citers.

6. **Add `prop:kac-shapovalov-koszulness` as an alternative criterion** (backup canonical). If Angle 1's attack on the twisted-tensor route also succeeds in future audit, Kac-Shapovalov is the fallback.

### Mathematical upgrades discovered

- **Condition (ix) Kac-Shapovalov determinant is the unique independent anchor** in the 10+1+1 equivalence cycle. This is an important structural discovery about the programme's own meta-theorem.
- **The manuscript's meta-equivalence theorem is secretly DAG-constrained**: most implications route through (v). Making this DAG explicit (which implications are proved from primitives vs routed through Theorem B) is a prerequisite for any clean canonical choice.
- **AP124 violation discovered**: `def:koszul-dual-cooperad` duplicated in Vol I `algebraic_foundations.tex:1675` and Vol II `connections/relative_feynman_transform.tex:942`. Independent of Theorem B fix; flag for separate rectification.

### Open items for next batch

- **Audit the 10+1+1 equivalence DAG**: which implications are proved from primitives, which route through Theorem B? This is a prerequisite for knowing which canonical definition works.
- **Verify Kac-Shapovalov (ix)⇒(i) proof** at L2127-2142 is self-contained.
- **Check Angle 8's Step 4** (Boardman convergence) — does it use Theorem B, or is it independent?
- **Find or write `prop:koszul-closure-properties`**.

## Files affected by fixes

- `chapters/theory/algebraic_foundations.tex` (lines 223-298: def rewrite + equivalents remark)
- `chapters/theory/bar_cobar_adjunction_inversion.tex` (lines 1604-1715: theorem wording + remarks + split)
- `chapters/theory/chiral_koszul_pairs.tex` (lines 1900-2202: meta-theorem DAG audit, potential reordering)
- **NEW**: `prop:koszul-closure-properties` (insertion point: `chiral_koszul_pairs.tex` after the 10+1+1 meta-theorem)
