# Adversarial Swarm 2026-04-09 — Batch 1 Synthesis

**Scope.** 5 segments (Wave-0 critical findings) × 2 angles each (Attack vs Defense). 10 agents. Read-only audit. All findings reference the canonical CLAUDE.md hot zones (HZ-1..HZ-10) and AP catalogue (1..141).

## Segment A — Theorem B circularity (genus-0 clause)

**Files of record.**
- Statement: `chapters/theory/bar_cobar_adjunction_inversion.tex:1604-1715`
- Definition: `chapters/theory/algebraic_foundations.tex:223-298`
- Alternative definition: `chapters/theory/chiral_koszul_pairs.tex:234-246` (`def:chiral-koszul-morphism`)
- 10+1+1 meta: `chiral_koszul_pairs.tex:1900-2008` (`thm:koszul-equivalences-meta`)
- PBW criterion: `chiral_koszul_pairs.tex:682-752` (`thm:pbw-koszulness-criterion`)
- Manuscript's own concession: `bar_cobar_adjunction_inversion.tex:1686-1695` (`rem:inversion-vs-fundamental`)

**Attack verdict (DEPENDS-ON-REWRITE).** Two definitions of "Koszul" coexist: (i) `def:koszul-chiral-algebra` (counit-qi at genus 0, which IS what Theorem B asserts) and (ii) `def:chiral-koszul-morphism` (twisted-tensor acyclicity + quadratic gr + filtration convergence). Theorem B's hypothesis cites (i); its proof step D2 routes through `ftm:koszul ⇒ ftm:counit` of `thm:fundamental-twisting-morphisms`, which uses (ii). Under (i), genus-0 is definition-unfolded. Under (ii), genus-0 is the substantive implication "twisted-tensor acyclicity ⇒ counit qi" (Lemma `lem:twisted-product-cone-counit`). The remark at L1686 is the manuscript's own admission.

**Defense verdict (RESCUABLE-WITH-REWRITE).** Pick PBW E₂-collapse as canonical Koszul definition. Surviving non-tautological content of Theorem B even at g=0:
1. A∞-qi (not just chain map)
2. Genus-g components ψ_g for g ≥ 1 via `thm:higher-genus-inversion` + MK3
3. ℏ-adic convergence of Σ ℏ^(2g-2) ψ_g
4. Explicit E₁-page spectral sequence computing H*(A)
5. Base change over M̄_{g,n}, functoriality, L∞-lift

**Convergence.** Both agents agree the fix is a single edit at `algebraic_foundations.tex:227-233`: replace "counit-qi at genus 0" with "PBW spectral sequence E₂ collapse" (which is condition (ii) of `thm:koszul-equivalences-meta` and is the criterion `thm:pbw-koszulness-criterion` actually verifies). Theorem B then says **PBW ⇒ counit qi**, which is substantive and matches the actual proof route.

**Status: RESCUABLE-CLEAN. Single-line definition rewrite suffices.**

---

## Segment B — Theorem H proof gap + critical level

**Files of record.**
- Statement + proof: `chapters/theory/chiral_hochschild_koszul.tex:649-736`
- ChirHoch definition: `chiral_hochschild_koszul.tex:145-157`
- Spectral sequence: `chiral_hochschild_koszul.tex:362-372`
- "Inheritance" step: `chiral_hochschild_koszul.tex:713-725`
- Critical-level counterexample: `hochschild_cohomology.tex:166-179`
- Bar concentration: `chiral_koszul_pairs.tex:1039-1107`
- Live AP94 violation: `compute/lib/derived_center_explicit.py:298`

**Attack verdict (FATAL at critical level + GAP at generic).** (1) Spectral sequence `E_1^{n,q}` on `C̄_{n+2}(X)` has q ranging up to 2(n+2), unbounded; "diagonal collapse" to n+q ≤ 2 unjustified. (2) "Inheritance" step at L713-725 is one-line assertion. (3) `V_crit(g)` is admitted counterexample (`rem:critical-level-lie-vs-chirhoch:176` says dim ChirHoch⁰ = ∞).

**Defense verdict (RESCUABLE-WITH-EXTRA-HYPOTHESIS).** The proof actually goes through bar-cobar replacement → Hom complex of D_X-modules on X → Brylinski [0,2] amplitude (configuration spaces are integrated out by bar-cobar, NOT bounded pointwise). Real log de Rham amplitude of (C̄_{n+2}(X), D) via Deligne logarithmic Poincaré + Kriz-Totaro collapse is more nuanced than the strawman SS suggests. Add "generic level" + Mok25 snc hypothesis. Already invoked piecewise in family-specific theorems but not hoisted to Theorem H.

**Convergence.** Both agree: (a) the spectral-sequence route is a strawman, (b) the real route is bar-cobar reduction, (c) "generic level" hypothesis must be added explicitly. Detailed deep dive in **Batch 2** (10 angles on Theorem H specifically).

**Status: RESCUABLE-WITH-FIXES. See Batch 2 synthesis for the complete reformulation.**

---

## Segment C — MC5 vs Huang 2005

**Files of record.**
- thm:general-hs-sewing: `chapters/connections/genus_complete.tex:1389-1419`
- Internal hedge: `chapters/connections/editorial_constitution.tex:149-150, 179-185, 459-473, 819`
- Status table contradiction: `concordance.tex:1863, 3195`, `FRONTIER.md:29`, `CLAUDE.md:399`
- 14+ "PROVED" locations propagating the unqualified headline
- Bibliography missing Huang 2005: `bibliography/references.tex:672-673` (only HLZ)

**Attack verdict (STRICTLY WEAKER as substitute, INDEPENDENT as different result).** thm:general-hs-sewing is a four-line power-mean Hilbert-Schmidt norm bound. Huang 2005 (math/0502533) is a regular-singular ODE analytic continuation theorem. Different objects, different hypotheses, different conclusions. The "HS is stronger" claim in standalone N5 is unsupported. Bibliography contains HLZ (Huang-Lepowsky-Zhang logarithmic tensor category, arXiv:1012.4193) but NOT Huang 2005.

**Defense verdict (INCOMPARABLE-VALID).** C₂-cofiniteness and polynomial OPE growth have ESSENTIALLY DISJOINT family coverage:
- MC5 covers: Heisenberg, V_k(g) generic, universal Vir_c, W_N, lattice — none C₂-cofinite
- Huang covers: minimal models, integrable L_k(g), W(p) triplet — most not Koszul
- Intersection narrow: rational lattice VOAs, integrable L_k(g)

MC5 carries operator-theoretic content (HS → trace-class → Fredholm determinant for Heisenberg) that Huang's analytic continuation does not. They are complementary. Fix is editorial:
1. Add comparison Remark `rem:hs-sewing-vs-huang` to `genus_complete.tex:1419+`
2. Add bibitems for Huang 2005 + Huang 2008 to `bibliography/references.tex`
3. Reconcile 14+ status locations to "MC5 analytic lane proved; BV/BRST=bar conjectural"

**Convergence.** Both agents agree the families are essentially disjoint (verified via `compute/lib/c2_cofiniteness_koszul_bridge_engine.py`). The "PROVED" headline is defensible IF the comparison remark is added AND the BV/BRST=bar identification is stated as a separate downstream conjecture (which it already is in editorial_constitution).

**Status: RESCUABLE-EDITORIAL. No mathematical work required. Fix is 1 Remark + 2 bibitems + 14 status-line edits.**

---

## Segment D — MC3 status drift

**Files of record.**
- MC3 statement of record: `chapters/examples/yangians_computations.tex:3940-3953` (`cor:mc3-all-types`)
- DK-4/5 conjecture: `yangians_computations.tex:3497-3506` (`conj:dk-compacts-completion`)
- Type-A only: `yangians_computations.tex:3034-3140` (`thm:shifted-prefundamental-generation`)
- RNW19 obstruction: `chapters/connections/concordance.tex:1727-1750` (`rem:no-bifunctor`)
- Headline contradictions: `CLAUDE.md:399`, `FRONTIER.md:27`, `concordance.tex:1770, 3176`
- Honest qualification: `concordance.tex:10699-10703`

**Attack verdict (SCOPE-DRIFT-MAJOR).** Headline "MC1-5 ALL PROVED" drops the qualifier. Cor:mc3-all-types is "a corollary about where the residual work lives", not thick generation of full Cat O. DK-4/5 explicitly Conjectured. Type-A only for shifted-prefundamental + pro-Weyl + Baxter exact triangles. 14+ "PROVED" locations vs ~10 qualified locations.

**Defense verdict (RESCUABLE-CLEAN).** Reformulate MC3 as 3-layer theorem:
- **MC3a (all types, PROVED):** Categorical CG closure for prefundamental modules (`thm:categorical-cg-all-types`)
- **MC3b (all types, PROVED):** DK-2/3 bar-cobar equivalence on evaluation-generated core via one-slot RNW19 Thm 5.1 (`cor:dk23-all-types`)
- **MC3c (type A, PROVED; arbitrary type, CONDITIONAL on Lemma L):** E_1-chiral thick generation by {V_ω_i(a)} ∪ {L⁻_i,a} in widehat-D(O^sh)

**Lemma L supplied (proof sketch):** "L⁻_i(b') ∈ thick⟨V_ω_i(a), L⁻_i(b)⟩ in widehat-D(O^sh_{≤0}(Y(g)))". Step 2 of `thm:shifted-prefundamental-generation` is rank-independent (uses only Chevalley-Serre, not sl_2-specific data). Type-A restriction enters only via HJZ25 generic irreducibility. Can be promoted via `thm:categorical-cg-all-types` + Hernandez block separation. Closes MC3c uniformly. Push DK-4/5 (compact-to-completed Francis-Gaitsgory transport) DOWNSTREAM of MC3 reformulation.

**Convergence.** Both agents converge on the 3-layer split. Defense supplies the missing Lemma L for type-A → all-types extension. RNW19 obstruction is asymmetric (blocks two-sided bifunctoriality but not the one-slot strategy actually used) — the "one slot" formulation is structural, not a weakening.

**Status: RESCUABLE-CLEAN + NEW LEMMA. The Lemma L proof sketch is the upgrade.**

---

## Segment E — MC4-0 Virasoro splitting

**Files of record.**
- Hypothesis: `chapters/theory/nilpotent_completion.tex:671-723` (`thm:resonance-filtered-bar-cobar`)
- Vir entry: `nilpotent_completion.tex:820-822` (`prop:resonance-ranks-standard`)
- Construction: `nilpotent_completion.tex:944-1171` (`thm:platonic-completion`)
- Mode-vs-state remark: `nilpotent_completion.tex:1173-1188` (`rem:mode-vs-state-completion`)
- conj:platonic-completion alias: `main.tex:1649`
- Independence of shadow depth: `compute/lib/resonance_rank_classification.py:1065`

**Attack verdict (GAP, not FATAL).** Vir splitting constructed only on positive-energy state space (vacuum module), not on the mode algebra (which is explicitly disavowed). Hypothesis (2) verification in `prop:resonance-ranks-standard` is "loose wording" ("higher-order terms vanish by dimension"). Class M / shadow depth / resonance rank: NO contradiction (independent invariants).

**Defense verdict (CONSTRUCTED).** `thm:platonic-completion` Steps 3-4 explicitly construct the splitting:
- R_Vir := V_0 (weight-zero slice) = k·|0⟩, dim 1
- Vir_c^{>0} := ⊕_{h≥1} V_h
- Strong-tower axioms verified line-by-line:
  - (H1): `prop:standard-strong-filtration`, OPE L_{(n)}L for n=0,...,3 satisfies weight additivity
  - (H2): m_k|_{V_0^⊗k} = 0 for k≥2 (output weight -n-1 < 0, forbidden by positive-energy); m_1|_{V_0} = 0 (weight-preserving)
  - (H3): Vacuum property v_{(n)}a = 0 for v ∈ V_0, a ∈ Vir_c^{>0}, n ≥ 0

ρ(Vir_c) = 1 derivation: m_1^R(m_0) = 0 because transferred m_1 is weight-preserving and vanishes on 1-dim V_0. Generalization: ρ ≤ dim V_0 < ∞ for every positive-energy chiral algebra. **conj:platonic-completion is actually a theorem in this volume.**

**Convergence.** Defense wins decisively. The construction exists at `thm:platonic-completion`; the table entry at `prop:resonance-ranks-standard:820-828` is sketchy and should be tightened to cite Step 4 explicitly. Class M (algebraic depth) and ρ (resonance rank) are orthogonal invariants. `conj:platonic-completion` should be promoted to a theorem (its content is already proved in volume).

**Status: RESCUABLE-PROSE. Tighten `prop:resonance-ranks-standard` proof to cite `thm:platonic-completion` Step 4. Promote `conj:platonic-completion` → `thm:platonic-completion-universal`.**

---

## Cross-segment patterns

1. **Hot Zone HZ-2 (env match tag) + HZ-5 (label/uniqueness):** All 5 segments have status-tag drift between top-level tables and chapter bodies. Pattern: chapter is honest, status table is over-claim. Fix: regenerate status tables from concordance body, not from CLAUDE.md.

2. **Definition vs Theorem chain coupling:** Segment A (Thm B) and Segment B (Thm H) both reduce to "the theorem statement and the proof use different equivalent characterizations of the same property; the official definition needs rewriting". Fix: the canonical definition should always be the one the proof actually consumes.

3. **Multi-document propagation lag:** Segment C (MC5) shows 14 status documents disagreeing because the wave-14 audit `compute/audit/codex_survey_v2_math_review_wave14.md:124-128` already flagged this as CRITICAL but propagation never happened. Lesson: status edits must touch all 14 mirrors in the same commit.

4. **Defense contributes new mathematics:** Segment D (Lemma L for MC3) and Segment E (`thm:platonic-completion-universal` upgrade) both produced new results from the defense side. The adversarial pair is generative, not just diagnostic.

5. **AP94 live in compute/lib:** `compute/lib/derived_center_explicit.py:298` still contains the verbatim forbidden string `ChirHoch*(Vir_c) = C[Theta] with |Theta|=2 (Gelfand-Fuchs)`. Strip in next pass.

## Action items (from Batch 1)

1. Edit `algebraic_foundations.tex:227-233`: replace counit definition of Koszul with PBW E₂-collapse
2. Strip AP94 from `compute/lib/derived_center_explicit.py:298`
3. Add `rem:hs-sewing-vs-huang` + 2 bibitems for Huang 2005/2008
4. Reconcile 14 MC5 status locations to "analytic lane proved; BV/BRST=bar conjectural"
5. Reformulate MC3 as MC3a/b/c (3-layer); insert Lemma L
6. Upgrade `conj:platonic-completion` to theorem (content already proved in vol)
7. Tighten `prop:resonance-ranks-standard` proof
8. **Theorem H** — see Batch 2 synthesis for full reformulation

## Next batches

- **Batch 2:** Theorem H (10 angles) — see `swarm_2026_04_09_batch2_thm_h.md`
- **Batch 3 (planned):** Theorem B circularity (10 angles)
- **Batch 4 (planned):** MC5 vs Huang (10 angles)
- **Batch 5 (planned):** MC3 reformulation (10 angles)
- **Batch 6 (planned):** MC4-0 universal upgrade (10 angles)
- **Batches 7+:** Vol II theorems, Vol III, compute engines, cross-volume consistency
