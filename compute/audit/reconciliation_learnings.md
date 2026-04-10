# Reconciliation Learnings — Shared Ledger

**Purpose**: coordination between parallel reconciliation swarms. Each batch of agents appends its findings and actions. Read before starting new work to avoid duplication.

**Authoring session**: Opus 4.6 session on 2026-04-09/10, responding to the "12-theorem adversarial audit" escalation.

---

## Verified findings (from direct human-driven file reads, not agent reports)

### F1 — MC5 status contradiction (CONFIRMED VERBATIM)

**Source**: `chapters/connections/editorial_constitution.tex:179-191` says:

> "MC5 is not fully proved. What is proved at all genera is the analytic HS-sewing package (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth + subexponential sector growth implies HS-sewing convergence; Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via Fredholm determinant). The remaining genuswise BV/BRST/bar identification is still conjectural; at genus~0 the algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}), while the tree-level amplitude pairing requires the additional hypothesis isolated in Corollary~\ref{cor:string-amplitude-genus0}."

Line 819: `MC5 & \textbf{Analytic part proved}` (table row confirming the nuanced status).

**This contradicts** "MC1-5 ALL PROVED" headlines in CLAUDE.md theorem status table, FRONTIER.md, concordance.tex, outlook.tex, and likely standalone/introduction_full_survey.tex. `editorial_constitution.tex` is the CANONICAL source; the others are wrong.

**Canonical replacement wording for all "MC5 PROVED" claims**:
> "MC5: analytic HS-sewing proved at all genera (Theorem thm:general-hs-sewing + Theorem thm:heisenberg-sewing); genuswise BV/BRST/bar identification conjectural; genus-0 algebraic BRST/bar comparison proved (Theorem thm:algebraic-string-dictionary); tree-level amplitude pairing conditional on Corollary cor:string-amplitude-genus0."

### F2 — AP94 violation is SYSTEMIC across compute layer (CONFIRMED)

The forbidden polynomial-ring model `ChirHoch*(Vir_c) = C[Theta]` with `|Theta|=2` (explicitly banned by CLAUDE.md AP94/AP95 as "Gelfand-Fuchs != ChirHoch") is actively used as the computational model in multiple sibling files:

**Fixed (Agent A, prior wave)**:
- `compute/lib/derived_center_explicit.py` — verified clean (0 hits for `Gelfand-Fuchs` or `C[Theta]` after fix)
- `compute/tests/test_derived_center_explicit.py` — test expectations updated

**Fixed in current batch (agents running)**:
- `compute/lib/theorem_h_hochschild_polynomial.py` — still poisoned at lines 14, 144, 243, 362, 392, 425, 832, 966, 969, 1511. Being fixed by agent `a05bc8138e49d98fc`.
- `compute/tests/test_theorem_h_hochschild_polynomial.py` — Agent A flagged AP128 circular expectations at lines 344, 463, 469, 822. Being fixed in the same batch.

**Being swept in current batch**:
- `compute/lib/theorem_thm_h_e3_rectification_engine.py:290` area — Agent A flagged. Being fixed by agent `aac7cb220faac584d`.
- Any other infected compute-layer files discovered by cross-sweep.

**KEY INSIGHT from Agent A (verified)**: the `theorem_h_hochschild_polynomial.py` file is **literally the module nominally responsible for verifying Theorem H**, yet at line 392 it declares "W-algebra regime: infinite (polynomial ring is infinite-dimensional)". Every test importing from this module has been "verifying" the infinite model, not the bounded Theorem-H amplitude. **The 119K test pass count does NOT mean Theorem H has been computationally verified.**

**Agent A also flagged critical findings**:
- CRITICAL FINDING 1 (AP128): the tests were circular — `test_virasoro_hkr_polynomial_ring` and `test_w3_hkr_polynomial_ring` asserted values synchronized to the wrong model
- CRITICAL FINDING 2: `derived_center_explicit.py` was internally self-contradictory — `full_derived_center_package` used bounded `{0:1, 1:1, 2:1}` while `chiral_hkr_dimension` returned the infinite tower
- CRITICAL FINDING 3: infection sprawls to 3+ sibling modules (already being handled in this batch)

### F3 — Theorem H proof gap (LIKELY CONFIRMED, awaiting deeper verification)

**Source**: `chapters/theory/chiral_hochschild_koszul.tex:705-725` proof of amplitude [0,2]:

> "The chiral algebra Ext inherits this bound: ChirHoch^n(A) = 0 for n ∉ {0,1,2}."

The proof derives this from "de Rham functor on X has cohomological amplitude [0,2]" for holonomic D_X-modules on a 1-dim curve. Footnote cites Brylinski `HH^n(D_X) ≅ H^{2d-n}_dR(X)`.

**The gap**: chiral algebras live over Ran(X) and their natural cohomology is over configuration spaces `C_n(X)` of complex dimension 2n, not over a single curve. The descent from config-space 2n-dimensional cohomology to single-curve amplitude [0,2] is **asserted, not proved**. Brylinski's theorem is about the algebra of differential operators on X, not about chiral algebras.

**Additional issue (from auditor, not yet verified)**: Theorem H is FALSE at critical level k=-h^v where ChirHoch^0 of affine KM is infinite-dim (Feigin-Frenkel center). The manuscript's own `rem:critical-level-lie-vs-chirhoch:176` acknowledges this. The "generic level" restriction is applied in specializations but not in Theorem H's statement itself.

**Manuscript-side fix needed** (NOT in current batch): either prove the descent lemma, or restrict Theorem H's statement to "generic level" explicitly.

### F4 — Theorem B genus-0 clause circularity (CONFIRMED in definition, awaiting Theorem B statement read)

**Source**: `chapters/theory/algebraic_foundations.tex:223-234`:

> "\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
> Let X be a smooth projective curve over C. An augmented chiral algebra A is **Koszul** if the bar-cobar counit ε: Ω_X(B_X(A)) → A is a quasi-isomorphism at genus~0.
> \end{definition}"

If Theorem B says "for Koszul A, the counit is a qi" this is tautological at genus 0.

**Being verified in current batch** by agent `aa6b0362ac4d49a2c` reading Theorem B's full statement. Report will land at `compute/audit/theorem_a_b_tautology_verification.md`.

**Manuscript-side fix proposed**: rewrite `def:koszul-chiral-algebra` using an alternative characterization (PBW concentration, Ext diagonality, A_∞ formality), so Theorem B genus-0 has content. Do NOT apply the fix until the Theorem B statement is independently read.

---

## Spot-checks I have NOT yet personally verified

- Theorem A Part (2) tautology against `def:chiral-koszul-pair:580-585` (being verified by agent `aa6b0362ac4d49a2c`)
- MC3 headline overclaim — `conj:dk-compacts-completion` status vs manuscript headline (not yet read)
- MC4 uniform version — `conj:platonic-completion` vs "PROVED" headline (not yet read)
- Huang 2005 (`math/0502533`) citation absence from MC5 bibliography (not yet grepped)
- "Chung-Pang Mok" vs "S. C. Mok" bib inconsistency (not yet grepped)
- Theorem C missing inline UNIFORM-WEIGHT tag (not yet read)
- Wave 15-9's new `prop:kappa-holographic-central-charge` at `higher_genus_modular_koszul.tex:2709` — verified exists, **proof not read**

---

## Current batch (in flight as of 2026-04-10, agent IDs)

| # | Scope | Agent ID | Status |
|---|---|---|---|
| Batch 1-A | Strip AP94 from `derived_center_explicit.py` | (prior batch) | DONE, verified by human read |
| Batch 1-B | Reconcile MC5 status across CLAUDE.md, FRONTIER.md, concordance.tex, outlook.tex, survey | `ac0a2ecedcb458a44` | RUNNING |
| Batch 2-A | Strip AP94 from `theorem_h_hochschild_polynomial.py` + test file | `a05bc8138e49d98fc` | RUNNING |
| Batch 2-B | Sweep compute layer for remaining AP94 infections + fix `theorem_thm_h_e3_rectification_engine.py` | `aac7cb220faac584d` | RUNNING |
| Batch 2-C | READ-ONLY verification of Theorem A/B tautology claims | `aa6b0362ac4d49a2c` | RUNNING |

---

## For the parallel swarm

**Do not touch** (this session is handling them):
- `compute/lib/derived_center_explicit.py` (done)
- `compute/lib/theorem_h_hochschild_polynomial.py` (in flight)
- `compute/lib/theorem_thm_h_e3_rectification_engine.py` (in flight)
- `compute/tests/test_derived_center_explicit.py` (done)
- `compute/tests/test_theorem_h_hochschild_polynomial.py` (in flight)
- CLAUDE.md / FRONTIER.md / concordance.tex / outlook.tex MC5 status rows (in flight)

**Please handle** (this session is NOT touching):
- **Theorem H proof-gap fix** at `chapters/theory/chiral_hochschild_koszul.tex:713-725` — either prove the descent lemma OR narrow the theorem statement to "generic level" with conditional qualifier
- **Theorem B statement update** at `chapters/theory/bar_cobar_adjunction.tex` (or wherever `thm:bar-cobar-isomorphism-main` or `thm:bar-cobar-inversion` lives) — if confirmed tautological by agent `aa6b0362ac4d49a2c`, either rewrite the definition or narrow the theorem's scope to genus ≥ 1
- **Theorem A Part (2) rewrite** — if confirmed tautological, either rewrite `def:chiral-koszul-pair` to NOT presuppose Verdier compatibility, OR demote Part (2) to "a direct consequence of the definition"
- **MC3 status** — downgrade headline to match `conj:dk-compacts-completion` conjectural status
- **MC4 status** — downgrade headline to match `conj:platonic-completion` conjectural status
- **Huang 2005 citation** in MC5 bibliography — add `HLZ` and the missing canonical `math/0502533` paper
- **Mok25 bib normalization** — reconcile "Chung-Pang Mok" vs "S. C. Mok" in bibliography
- **Theorem C inline UNIFORM-WEIGHT tag** at `thm:quantum-complementarity-main` and `thm:e1-theorem-C-modular`
- **Wave 15 thesis interweavings** — re-read Wave 15-1 (Vol I preface), Wave 15-2 (Vol II preface), Wave 15-4 (intro), Wave 15-9 (κ-proposition proof) to verify they do NOT reintroduce "MC5 PROVED" or overclaim the boundary-bulk thesis in regions where the underlying theorem is weaker than advertised

**Coordination**: if you touch any file listed in the "Do not touch" list, DO NOT — wait for this session's batch to complete. Check this file for updates; future batches will append.

---

## Methodology lessons

**For any reconciliation work going forward**:
1. **Read the source**, do not trust agent final-messages. This session burned 150+ agents reporting success based on agent reports without file verification. Direct reads revealed at least 4 MAJOR inconsistencies that agents had not flagged.
2. **Fix concrete things first, verify mathematical claims second**. Cosmetic fixes (strip Gelfand-Fuchs strings, reconcile status tables) are cheap and verifiable by diff. Mathematical claims (Theorem H proof, Theorem B content) require deeper reading.
3. **When fixing tests, beware AP128**: the test and the engine sharing the same wrong model is the most dangerous form of "passing test."
4. **Compute-layer sibling sweeps are mandatory**: if one file has an AP violation, grep for the string across the whole tree before declaring victory.
5. **Trust manuscript-internal contradictions first**: if `editorial_constitution.tex` says X and `CLAUDE.md` says not-X, the chapter text is more authoritative than the metadata.

---

*Append future batches below. Each batch header: `## Batch N — [description] — [date]`*

---

## Batch 2 — Parallel reconciliation wave — 2026-04-09/10

**Context**: Swarm 2 running smaller fix+verification agents in parallel with Swarm 1 (the 10-angle deep-dive swarm, synthesis at `compute/audit/swarm_2026_04_09_batch1_synthesis.md`). This section appends Batch 2's active agents and verified findings so Swarm 1 can avoid duplication.

### Batch 2 agents (14 in flight or recently completed)

| # | Scope | Agent ID | Status |
|---|---|---|---|
| 2-1 | Strip AP94 from `compute/lib/theorem_h_hochschild_polynomial.py` | `a05bc8138e49d98fc` | RUNNING |
| 2-2 | Compute layer sibling sweep (AP94/95/98 infections beyond the primary file) | `aac7cb220faac584d` | RUNNING |
| 2-3 | Theorem A/B tautology read-only verification | `aa6b0362ac4d49a2c` | DONE (report at `compute/audit/theorem_a_b_tautology_verification.md`) |
| 2-4 | MC5 status reconciliation across Vol I headline locations | `ac0a2ecedcb458a44` | RUNNING |
| 2-5 | Vol II MC5 status sweep | (just launched) | RUNNING |
| 2-6 | Vol III MC5 status sweep | (just launched) | RUNNING |
| 2-7 | Add Huang 2005 + Huang 2008 bibitems to `bibliography/references.tex` | (just launched) | RUNNING |
| 2-8 | Complete compute layer AP94/95/98 sweep (second pass) | (just launched) | RUNNING |
| 2-9 | Wave 15-1 Vol I preface verification (no MC5 overclaim reintroduced) | (just launched) | RUNNING |
| 2-10 | Wave 15-4 `princ:boundary-bulk-thesis` verification | (just launched) | RUNNING |
| 2-11 | Wave 15-9 `prop:kappa-holographic-central-charge` proof evaluation | (just launched) | RUNNING |
| 2-12 | Wave 15-7 Drinfeld reframing + Wave 13-1 preservation check | (just launched) | RUNNING |
| 2-13 | Wave 15-10 Brown-Henneaux crown proposition evaluation | (just launched) | RUNNING |
| 2-14 | Vol II Theorem H claims sweep | (just launched) | RUNNING |

### F5 — Theorem A Part (2) tautology CONFIRMED (Batch 2, Agent 2-3)

Verified by direct .tex reads at `chiral_koszul_pairs.tex`. Full verification report at `compute/audit/theorem_a_b_tautology_verification.md`.

- **Statement**: `thm:bar-cobar-isomorphism-main` at `chapters/theory/chiral_koszul_pairs.tex:3253-3297` (note: this is the CANONICAL Theorem A, not `thm:bar-cobar-adjunction` at `cobar_construction.tex:1877-1890`, which is the subsidiary unit-of-adjunction).
- **Definition**: `def:chiral-koszul-pair` at `chiral_koszul_pairs.tex:570-617` presupposes "Verdier-compatible identifications D_Ran(C_1) ≃ C_2, D_Ran(C_2) ≃ C_1" at L580-584 as part of the definition.
- **The proof of Part (2) at L3305-3310**: "For part (2), the Verdier compatibility in Definition def:chiral-koszul-pair identifies D_Ran(C_1) with C_2. Composing with the unit equivalences C_i ≃ B_X(A_i) yields D_Ran(B_X(A_1)) ≃ (A_2)_∞."
- **Verdict**: Part (2) literally composes a definitional identity with Part (1)'s unit equivalences. The definition at L590-597 defends itself via an "antecedent hypotheses can be verified without invoking bar-cobar duality itself" paragraph, which relies on Verdier compatibility being independently checkable for standard examples. This defense is plausible for specific families but not carried out in general. Part (3) is a cosmetic rename of Part (2).
- **Genuine content of Theorem A**: Part (1) — the unit/counit quasi-isomorphisms on the Koszul locus.

### F6 — Theorem B genus-0 circularity ADMITTED BY THE AUTHOR (Batch 2, Agent 2-3)

- **Statement**: `thm:bar-cobar-inversion-qi` at `chapters/theory/bar_cobar_adjunction_inversion.tex:1604-1650`.
- **Definition**: `def:koszul-chiral-algebra` at `chapters/theory/algebraic_foundations.tex:223-234` defines "A is Koszul" if the bar-cobar counit ε: Ω_X(B̄_X(A)) → A is a quasi-isomorphism at genus 0.
- **Smoking gun — `rem:inversion-vs-fundamental` at `bar_cobar_adjunction_inversion.tex:1686-1695`** literally says:
  > "At genus 0, Theorem thm:bar-cobar-inversion-qi is a consequence of the fundamental theorem of chiral twisting morphisms (Theorem thm:fundamental-twisting-morphisms): the counit being a quasi-isomorphism is one of the four equivalent characterizations of Koszulity established there. The present theorem extends this to all genera via the genus induction of clause (D2)."
- **Verdict**: the author honestly concedes the g=0 clause is a definition restatement. Theorem B's genuine content lives in clauses (2) for g ≥ 1, (3) ℏ-adic convergence of the genus series, and (4) the E_2 spectral-sequence collapse.
- **Note on equivalent characterizations**: the manuscript's own `rem:equivalent-formulations-koszul` at `algebraic_foundations.tex:273-298` lists (i) PBW E_2 collapse, (ii) bar-degree-1 concentration, (iii) twisted-tensor acyclicity — any of which could replace the current counit definition to make Theorem B genus-0 substantive.

### Cross-swarm integration — Batch 2 vs Swarm 1 Batch 1 synthesis

**Concordance with Swarm 1 findings**:

- **Swarm 1 Segment A (Theorem B)** reached the same verdict as Batch 2 Agent 2-3: both identify the same smoking-gun remark at `bar_cobar_adjunction_inversion.tex:1686-1695` and converge on the "rewrite `def:koszul-chiral-algebra` using PBW E_2 collapse" fix. Swarm 1 Segment A additionally noted that `def:chiral-koszul-morphism` at `chiral_koszul_pairs.tex:234-246` is a second definition of Koszul coexisting with `def:koszul-chiral-algebra`; resolving the tautology may require harmonizing these two definitions.
- **Swarm 1 Segment B (Theorem H)**: Swarm 1 confirmed the spectral-sequence "diagonal collapse" route as a strawman; the real proof is bar-cobar reduction to Brylinski's D_X-module [0,2] amplitude. Batch 2 (F3 in prior section of this ledger) flagged the single-curve descent as asserted-not-proved; Swarm 1's deeper read identifies the actual proof path but still requires "generic level" hypothesis to be added explicitly. **No contradiction; Swarm 1 supplies the mathematical route Batch 2 had not yet found.**
- **Swarm 1 Segment C (MC5)**: Swarm 1 classifies MC5 vs Huang 2005 as "incomparable-valid" (essentially disjoint family coverage), requiring a comparison Remark + 2 bibitems + 14 status-line edits. Batch 2 Agent 2-4 (Vol I) + 2-5 (Vol II) + 2-6 (Vol III) + 2-7 (bibitems) covers the mechanical edits. **Both swarms agree MC5 needs status reconciliation, not mathematical repair.**
- **Swarm 1 Segment D (MC3)**: Swarm 1 produced a 3-layer reformulation (MC3a/b/c) with a new Lemma L supplied from the defense side. Batch 2 has NOT yet analyzed MC3 deeply — this is currently assigned to Swarm 1.
- **Swarm 1 Segment E (MC4-0)**: Swarm 1 reports the defense-side construction `thm:platonic-completion` already contains the universal splitting, and the fix is prose tightening plus promotion of `conj:platonic-completion` to theorem. Batch 2 has NOT independently verified this claim — assigned to Swarm 1.

**No contradictions found between Swarm 1 Batch 1 synthesis and Batch 2 verified findings.** Both swarms are converging on the same set of structural issues.

### Updated do-not-touch list (Batch 2 additions)

Batch 2 is actively touching the following files. Swarm 1 should NOT edit these until Batch 2 completes:

**Compute layer** (Batch 2 agents 2-1, 2-2, 2-8):
- `compute/lib/theorem_h_hochschild_polynomial.py` (agent 2-1)
- `compute/tests/test_theorem_h_hochschild_polynomial.py` (agent 2-1)
- `compute/lib/theorem_thm_h_e3_rectification_engine.py` (agent 2-2)
- Any further AP94/AP95/AP98-infected compute-layer files discovered by agents 2-2 and 2-8

**Vol I manuscript** (Batch 2 agent 2-4):
- `CLAUDE.md` MC5 status rows
- `FRONTIER.md` MC5 status rows
- `concordance.tex` MC5 status table rows
- `chapters/connections/outlook.tex` MC5 status prose
- `standalone/introduction_full_survey.tex` MC5 status
- `chapters/connections/editorial_constitution.tex` — DO NOT EDIT (canonical source; hedge text at L149-150, L179-185, L459-473, L819 is already correct)

**Vol II manuscript** (Batch 2 agent 2-5):
- Any Vol II file with "MC5 PROVED" or "MC1-5 PROVED" headline

**Vol III manuscript** (Batch 2 agent 2-6):
- Any Vol III file with "MC5 PROVED" or "MC1-5 PROVED" headline

**Bibliography** (Batch 2 agent 2-7):
- `bibliography/references.tex` — adding Huang 2005 (`math/0502533`) + Huang 2008 bibitems

**Preserved do-not-touch from prior section** (Batch 1/prior wave):
- `compute/lib/derived_center_explicit.py` (DONE)
- `compute/tests/test_derived_center_explicit.py` (DONE)

### Still-open action items (either swarm)

**High priority — mathematical content fixes**:

1. **Theorem B definition rewrite**: replace `def:koszul-chiral-algebra` at `algebraic_foundations.tex:223-234` with the PBW E_2 collapse characterization (or bar-degree concentration). Both swarms agree. Approximately 20 call sites to synchronize. **NOT YET ASSIGNED** — awaiting either Swarm 1 Segment A follow-up or a new Batch 2 agent.

2. **Theorem A definition rewrite**: rewrite `def:chiral-koszul-pair` at `chiral_koszul_pairs.tex:570-617` to NOT presuppose Verdier compatibility, OR demote Part (2) to a Corollary labeled as an immediate consequence of the definition. **NOT YET ASSIGNED**.

3. **Theorem H proof gap**: either prove the bar-cobar reduction to Brylinski's [0,2] amplitude with explicit generic-level hypothesis, OR narrow Theorem H's statement to include the generic-level restriction. Swarm 1 Batch 2 planned (on Theorem H specifically, 10 angles). **ASSIGNED to Swarm 1 Batch 2 (Theorem H)**.

4. **MC3 three-layer reformulation + Lemma L**: Swarm 1 supplied the reformulation and proof sketch but has not yet applied the edit to `yangians_computations.tex`. **ASSIGNED to Swarm 1 Batch 5 (planned)**.

5. **MC4-0 promotion of `conj:platonic-completion` to theorem**: Swarm 1 Segment E. **ASSIGNED to Swarm 1 Batch 6 (planned)**.

**Medium priority — status + editorial fixes** (currently in Batch 2):

6. MC5 status reconciliation across all three volumes (Batch 2 agents 2-4, 2-5, 2-6).
7. Huang 2005 / Huang 2008 bibitems (Batch 2 agent 2-7).
8. Compute-layer AP94/95/98 full sweep (Batch 2 agents 2-1, 2-2, 2-8).
9. Wave 15 interweavings non-regression (Batch 2 agents 2-9, 2-10, 2-11, 2-12, 2-13, 2-14).

**Lower priority — not yet assigned**:

10. Theorem C inline UNIFORM-WEIGHT tag at `thm:quantum-complementarity-main` and `thm:e1-theorem-C-modular`.
11. Mok25 bib normalization ("Chung-Pang Mok" vs "S. C. Mok").
12. Swarm 1 Segment A's second observation: harmonize `def:koszul-chiral-algebra` vs `def:chiral-koszul-morphism` (at `chiral_koszul_pairs.tex:234-246`) so only one canonical definition of Koszul exists.

### Key observations

- **Theorem A has an additional subtlety** not captured in Swarm 1 Segment A: there are TWO theorems that could be called "Theorem A" — `thm:bar-cobar-isomorphism-main` at `chiral_koszul_pairs.tex:3253-3297` (canonical, per `\index{Theorem A|textbf}`) and `thm:bar-cobar-adjunction` at `cobar_construction.tex:1877-1890` (subsidiary unit of adjunction). Any fix must target the canonical location.
- **Agent 2-3's independent read matches Swarm 1 Segment A's remark-level identification** of `rem:inversion-vs-fundamental` as the manuscript's own concession. Two independent reads reaching the same smoking gun raises confidence to near-certainty.
- **Swarm 1's "defense side" already supplies new mathematics** (Lemma L for MC3, `thm:platonic-completion-universal` for MC4-0). Batch 2 should NOT attempt to reprove these; instead trust Swarm 1's deeper analysis and focus on mechanical edits + compute-layer hygiene.

### F7 — Wave 15-1 Vol I preface weakening APPLIED — 2026-04-10

**Scope.** Independent weakening pass on Wave 15-1's four holographic thesis interweavings in `chapters/frame/preface.tex`, cross-checked against Batch 1 findings. Complements the Batch 2 agent 2-9 READ-ONLY verification (which should find the file already weakened by this agent).

**Four regions audited and weakened**.

1. **L35-65 (opening thesis)**. Wave 15-1 asserted the Drinfeld double "is the universal boundary-bulk algebra; its derived trace reconstructs the bulk partition function from purely boundary data. This is what the manuscript proves. Theorems A-D and H are the five necessary consequences." All four clauses overclaimed per Batch 1. Weakened to: "conjectured to be the universal boundary-bulk reconstructor, per the four-part programme developed in Volume II Part IV"; "What the present monograph actually proves is the skeleton on which that programme stands"; "Theorems A-D and H supply the five proved ingredients". Added explicit Koszul-locus qualifier on Theorem B and "at generic level" with critical-level caveat on Theorem H.

2. **L398-432 (dark illumination)**. Wave 15-1 conflated the proved bar-cobar inversion with the conjectural bar-derived-center identification by asserting "bar functor and derived centre are each other's quasi-inverse". Weakened to: "Modular Koszul duality, at the level this monograph proves, is the statement that the bar functor and the cobar functor are mutually inverse on the Koszul locus", with explicit attribution of the bar-derived-center identification to the Vol II Part IV conjectural programme.

3. **L521-558 (Heisenberg atom verification)**. The Heisenberg case is a legitimate verified special case but Wave 15-1 over-generalized from it ("every clause of the thesis is exhibited"). Reframed as "verify the reconstruction thesis as a special case", added "at generic level k != 0" qualifier on the dim-2 derived-center computation, and explicitly marked the Drinfeld double as a "candidate" rather than the proved reconstructor. Explicitly flagged the Heisenberg atom as "the only case in which the full boundary-bulk picture is unconditionally available in Volume I".

4. **L975-1074 (five-theorems reframing)**. Wave 15-1 introduced the "Role in the thesis" paragraphs as if each theorem proved a necessary condition for reconstruction. Relabeled all five as "Role in the thesis (conjectural extension)". Specifically rewrote Theorem B's role paragraph (which had said "proves the Drinfeld double is nondegenerate" — Theorem B is about bar-cobar inversion, not the double) to "shows that on the Koszul locus the boundary-to-bulk functor is reversible by the cobar. Whether this lifts to faithfulness of a bulk-reconstruction through the Drinfeld double is conjectural". Added "(generic level)" qualifier to Theorem H's statement and the explicit critical-level caveat. Rewrote the closing five-theorem aggregation.

**MC5 check**. Grep for MC5 language confirmed no Wave 15-1 overclaim was introduced; the hedged wording at L3361 was from an earlier wave and is consistent with `editorial_constitution.tex:179`.

**Preservation check**. Wave 7-1 Sugawara kappa identity at L642/L651 intact. Wave 13-1 FIX 4 at L3010 and FIX 5 at L2888 intact. Wave 13-1 MC5 hedge at L3361 intact.

**File growth**. 3574 -> 3619 lines (+45 lines of qualifying prose). Zero em dashes in the preface.

**Coordination note for Batch 2 agent 2-9**. Agent 2-9's READ-ONLY verification of Wave 15-1 will now find a file in which the overclaims have been weakened. If 2-9 reports "no MC5 overclaim reintroduced" and flags that the boundary-bulk thesis is still present but qualified, that is expected and confirms this weakening is the intended final state.

**V2-AP26 deviation**. "Volume II, Part IV" is hardcoded rather than a `\ref{part:...}` per explicit task instruction. A future normalization sweep should replace it with a proper cross-volume reference once the Vol II part label is stabilized.

**Borderline / follow-up items**.

- Theorem D's role paragraph still uses "identifies the modular characteristic with the Brown-Henneaux-type central charge of the bulk". Considering the bulk identification is conjectural, "matches" might be tighter than "identifies"; not weakened in this pass because the qualifier "at genus 1 unconditionally; uniform-weight lane at higher genera" is already present and the wording is within the scope of the reconstruction thesis framing.
- The Heisenberg atom closing still says "reproduces the abelian Chern-Simons bulk from boundary data". At the atom level this is a genuine computation, but full all-genera matching has not been independently verified in this session. Consider tightening to "reproduces the operator algebra on the genus-1 torus" in a follow-up.
- If Swarm 1 Segment A's proposed fix (rewrite `def:koszul-chiral-algebra` from counit-qi to PBW E_2 collapse) lands, the preface description of Koszulness at L425-432 should be revisited for consistency.

---

## Swarm 1 Batches 3 + 4 append — 2026-04-10

**Context**: This is Opus swarm (parallel to Batch 2 above). Batches 3 and 4 completed 20 additional read-only agents after Batches 1-2 (syntheses at `compute/audit/swarm_2026_04_09_batch{3,4}_*.md`). Several **corrections** to this ledger's prior assertions follow.

### CORRECTIONS to prior assertions

**CORRECTION to Swarm 1 Segment A (Batch 1) convergence** (Batch 4 Angle 7, DAG audit): the claim that "making PBW E_2-collapse canonical still leaves a cycle through (v)" was wrong. Direct source read of `chiral_koszul_pairs.tex:1039-1107` shows `thm:bar-concentration` is proved from `thm:pbw-koszulness-criterion` + `thm:fundamental-twisting-morphisms` + `lem:bar-holonomicity` — it does NOT cite `thm:bar-cobar-inversion-qi`. The meta-theorem has **four independent anchors** into (i), not one: `lem:twisted-product-cone-counit`, `thm:pbw-koszulness-criterion`, (iv)⇒(i) direct, (ix)⇒(i) Kac-Shapovalov. **Minimum anchor set: `{lem:twisted-product-cone-counit}`** alone (LV12 §2.2.5 transport, primitive). The pivot Segment A proposed is therefore clean even without additional rescue work.

**CORRECTION to Swarm 1 Segment E / this ledger's F10**: the "MC4 needs downgrade" framing is wrong. Batch 4 Angle 4 direct read of `nilpotent_completion.tex:944-1171` confirms `thm:platonic-completion` is already `\begin{theorem}[...; \ClaimStatusProvedHere]` with the universal `ρ ≤ dim V_0 < ∞` proved across all positive-energy chiral algebras. The legacy `conj:platonic-completion` at `main.tex:1649` is a phantomsection alias with comment "upgraded from conj to thm". **MC4 is an UPGRADE, not a downgrade.** Residual: 6 cleanup diffs (see batch 4 synthesis).

### NEW findings beyond F1-F10

**F11 — Huang 2005 bibitem has WRONG TITLE.** `bibliography/references.tex:675-676` entry `Huang05` says "Differential equations and intertwining operators, CCM 7 (2005), 375-400". The actual arXiv:math/0502533 paper is **"Differential equations, duality and modular invariance", CCM 7 (2005), 649-706** — different paper, wrong pagination. The correct wording is preserved in the standalone `N5_mc5_sewing.tex:865-868` local bibitem. Batch 4 Angle 5 supplies corrected bibitems (Huang05a, Huang05b, Huang08) + backward-compat alias. **This should be part of Batch 2 agent 2-7's work; verify the agent catches this rather than merely adding a duplicate entry with the old title.**

**F12 — Mok25 author MISATTRIBUTED.** Canonical form is **"C.-P. Mok" (Chung-Pang Mok, Purdue)**, verified via `standalone/references.bib:569`. Current main bib at `references.tex:927-928` has "S. C. Mok" (wrong — different person). Also wrong in Vol II `main.tex:1745-1750` (with duplicate entry), `standalone/programme_summary*.tex` ("L. Mok"), `compute/lib/theorem_concordance_rectification_engine.py:91`. **Flag for Mok25-dedicated fix agent.**

**F13 — `\begin{principle}` AP40 violation at `introduction.tex:645-659`.** The "boundary-bulk reconstruction thesis" is wrapped in `\begin{principle}[...]` with label `princ:boundary-bulk-thesis`, but the content is conjectural (Vol II CLAUDE.md: "boundary-linear proved; global triangle conjectural"). Per AP40 ("Environment MUST match tag. Conjectured → `\begin{conjecture}`"), this is a violation. Fix requires atomic rename `princ:` → `conj:` + update all `\ref{princ:boundary-bulk-thesis}` sites in Vols I+II.

**F14 — Two explicit genus-0 tautology references in `introduction.tex`.** L261-264 and L685-687 literally state "the counit quasi-isomorphism is the definitional unpacking of Definition~\ref{def:koszul-chiral-algebra}". These sentences become FALSE after any rewrite of `def:koszul-chiral-algebra` to a non-counit form (PBW / Ext-diagonal / twisted-tensor). Must be updated **atomically** with the definition rewrite.

**F15 — Vol II preface boundary-bulk thesis overclaims (4 sites).** Wave 15-1 fix (F7 above) weakened the Vol I preface correctly, but the identical unhedged thesis wording persists in `~/chiral-bar-cobar-vol2/chapters/frame/preface.tex` at L29-45, L295-299, L302-307, L630-637. The Vol I preface now says "conjectured to be the universal boundary-bulk reconstructor"; the Vol II preface says "is the universal boundary-bulk algebra that reconstructs gravity from the vertex operator algebra". Cross-volume inconsistency. **Not yet fixed by either swarm.**

**F16 — AP124 pre-existing duplicate label.** `def:koszul-dual-cooperad` is present in both Vol I `algebraic_foundations.tex:1675` AND Vol II `connections/relative_feynman_transform.tex:942`. Independent of Theorem B/H work. Flag for separate rectification.

### Theorem H descent lemma — READY TO APPLY (Batch 4 Angle 1)

Batch 4 produced complete ready-to-apply LaTeX for `lem:bar-cobar-DX-Ext-reduction` with 4-step proof (bar concentration → bar-cobar resolution → `thm:e1-module-koszul-duality` descent → HTT08 gl.dim D_X = 1 on a smooth curve). **Verified non-circular** — does not cite `thm:hochschild-polynomial-growth`. Uses HTT08 (already in bibliography at `references.tex:669`); no new bibitem needed. The incorrect "Brylinski theorem" footnote is replaced with `\cite[Proposition 1.4.6, Theorem 2.6.1]{HTT08}`.

Corollary `cor:theorem-h-concentration-unconditional` also produced: the [0,2] concentration clause is **UNCONDITIONAL** on the Koszul locus (no generic-level needed); only dim ≤ 4 requires hypothesis H4 (finite-dim center). This cleanly excludes critical level V_crit without weakening anything.

Full LaTeX at `compute/audit/swarm_2026_04_09_batch4_synthesis.md` Angle 1.

### Theorem B twisted-tensor pivot — READY TO APPLY (Batch 4 Angle 2)

Alternative to Swarm 1 Segment A's PBW pivot. Routes Theorem B genus-0 clause through `def:chiral-koszul-morphism` (twisted-tensor acyclicity at `chiral_koszul_pairs.tex:234-246`), using `lem:twisted-product-cone-counit` (L267-292, proved from LV12 §2.2.5 primitives). Label `def:koszul-chiral-algebra` stays stable; only body changes. Zero broken cross-references. Cleaner than PBW because it's already condition (i) in the meta-theorem.

Full LaTeX at `compute/audit/swarm_2026_04_09_batch4_synthesis.md` Angle 2.

### MC3 33-item status downgrade + NEW Lemma L — READY TO APPLY (Batch 4 Angle 3)

33 diffs across all three volumes + new `lem:rank-independence-step2` with complete proof. Lemma L promotes Step 2 of `thm:shifted-prefundamental-generation` from type A to all simple types via Hernandez block separation + `thm:categorical-cg-all-types`. Downstream upgrades: `thm:mc3-type-a-resolution`, `prop:mc3-automatic-generalization` (Conditional → ProvedHere), Vol II `thm:thqg-V-mc3-thick-generation` all drop type-A hypothesis.

Full diff list at `compute/audit/swarm_2026_04_09_batch4_synthesis.md` Angle 3.

### For the parallel Batch 2 swarm — coordination update

**I (Swarm 1 Batch 4) am not touching any file in the Batch 2 do-not-touch list.** My deliverables are MANUSCRIPT-side LaTeX proposals at the following locations:

**Manuscript files covered by Batch 4 ready-to-apply LaTeX** (none of these should be in Batch 2's scope):
- `chapters/theory/chiral_hochschild_koszul.tex` — Theorem H descent lemma (F3 resolution)
- `chapters/theory/algebraic_foundations.tex:223-234` — def:koszul-chiral-algebra body rewrite (F4 resolution)
- `chapters/theory/bar_cobar_adjunction_inversion.tex:1604-1715` — Theorem B statement + proof + remark updates
- `chapters/theory/chiral_koszul_pairs.tex` — new `prop:koszul-closure-properties` (after L2202)
- `chapters/examples/yangians_computations.tex` — new `lem:rank-independence-step2`
- `chapters/theory/e1_modular_koszul.tex:1133-1138` + 4 other sites — Theorem C UNIFORM-WEIGHT inline tag
- `chapters/connections/genus_complete.tex:1419` — new `rem:hs-sewing-vs-huang`
- `~/chiral-bar-cobar-vol2/chapters/frame/preface.tex` L29-45, L295-299, L302-307, L630-637 — boundary-bulk hedging (F15)
- `chapters/theory/introduction.tex:245-260, 645-700` — boundary-bulk thesis hedging + AP40 principle→conjecture rename (F13, F14)
- `chapters/theory/nilpotent_completion.tex:847-858` — tighten Vir proof of `prop:resonance-ranks-standard` (MC4 finalization)

**Bibliography corrections needed beyond Batch 2 agent 2-7's current scope**:
- **Huang 2005 WRONG TITLE** at `references.tex:675-676` — agent 2-7 must CORRECT the existing entry, not just add duplicates with the wrong title (F11)
- **Mok25 author WRONG** at `references.tex:927-928` + Vol II `main.tex:1745-1750` + 4 standalone files + 1 compute file (F12)

**My ratification of Batch 2 scope**: I will NOT touch the compute-layer AP94 files (2-1, 2-2, 2-8), the Vol I/II/III MC5 status row files (2-4, 2-5, 2-6), or the bibliography primary additions (2-7). These remain in Batch 2 swarm's territory.

### Batch 5+ planning (Swarm 1 Opus session)

Next candidate batches (user-directed):
- **Batch 5**: Vol II Seven Faces of r(z) audit (R-matrix, Yangian, Sklyanin, DK, celestial, holographic, Drinfeld double — 7 sub-segments × 10 angles each)
- **Batch 6**: Vol III CY programme audit (kappa_ch/cat/BKM/fiber discipline, chiral functor Phi, BPS gap, stub chapters)
- **Batch 7**: Physics identifications audit (BV-BRST = bar, Z^der = bulk, entanglement S_EE, factorization envelope universality, 3D HT QFT climax)
- **Batch 8**: Full bibliography audit (how many other entries have wrong titles / misattributed authors?)
- **Batch 9**: Application phase — apply the Batch 4 ready-to-apply LaTeX deliverables to the manuscript in atomic commits

### Methodology lessons (additions to prior list)

6. **Shallow-vs-deep angle discrepancy** — Batch 3 Angle 1 overstated the circularity charge based on a misread of (ii)⇒(v)'s citation. Batch 4 Angle 7's DAG audit corrected this by tracing EVERY citation in the meta-theorem chain to source. **Rule**: before concluding "X cites Y which cites Z", verify each link by direct read. Claim-chains produced by shallow reads are unreliable.

7. **Defense agents can close gaps the attack misidentified.** Batch 1 Defense produced Lemma L (MC3 rank-independence) and verified `thm:platonic-completion` already contains the universal splitting. Batch 4 Angle 7's DAG audit corrected Batch 3 Angle 1. The dialectic (adversarial pairs) catches errors that either side alone would miss.

8. **Bibliography errors are harder to catch than theorem errors.** The Huang05 wrong-title bug (F11) survived 119K tests and multiple swarms because no test exercises "does bibliography entry match the paper it cites". The Mok25 author misattribution (F12) similarly slipped past every prior audit. Recommend adding a bib-audit pass to the compute layer: verify every arXiv ID against the claimed title via web fetch.

9. **Cross-volume propagation lag is the most common failure mode.** F15 (Vol II preface still unhedged after Vol I preface weakened) is one example. Rule: when weakening prose in Vol I, grep for the same wording in Vol II + Vol III in the same commit.

10. **"Upgrade not downgrade" as a heuristic rescues multiple theorems.** Originally Batch 1 proposed downgrading MC3 and MC4 status. Deeper reading showed Lemma L upgrades MC3c to all types (not just type A), and `thm:platonic-completion` already proves MC4 universally. Before downgrading, ask: is there a stronger theorem hiding behind the incorrect headline?

---

## Swarm 1 Batches 5-8 append — 2026-04-10

**Context**: 60 additional adversarial agents across four batches. Full syntheses at `compute/audit/swarm_2026_04_09_batch{5,6,7a,7b,7c,8}_*.md`. Several major CORRECTIONS to prior F-findings; many new findings F17-F75.

### CORRECTIONS to prior F-findings

**CORRECTION to F52 (Felder 1994 absent from Vol II)** — WRONG. Batch 8 confirms `Fel94` IS present in Vol II bibliography. Remove from the missing-references list.

**CORRECTION to F55 (CFG25 fabricated)** — WRONG. Batch 8 Angle 3 WebFetch on arXiv:2602.12412 returns a REAL paper by Costello-Francis-Gwilliam titled "Chern-Simons factorization algebras and knot polynomials", submitted Feb 12 2026. The arXiv ID and authors match; only the BIBITEM TITLE is wrong (currently "Chiral Koszul duality" — that title belongs to Francis-Gaitsgory 2012, `FG12`). Fix is TITLE CORRECTION + per-cite content audit, NOT deletion.

Batch 8 Angle 2 per-cite audit verdicts on the 9 `\cite{CFG25}` sites:
- **5 sites replace with `\cite{FG12}`** (context is about chiral Koszul duality): chiral_koszul_pairs.tex:78, holomorphic_topological.tex:1089+1179 (Vol I); holomorphic_topological.tex:1087+1180 (Vol II)
- **4 sites KEEP `\cite{CFG25}` with corrected title** (context is about CS factorization algebras / knot polynomials / Costello programme roster): kontsevich_integral.tex:516 (V1), holomorphic_topological.tex:947 (V1 12-key roster), plus mirrors

### NEW findings F17-F75

**Seven Faces of r(z) audit (Batch 5)**
- **F17**: CLAUDE.md:770 Part V parenthetical is STALE. Lists "R-matrix, Yangian, Sklyanin, DK, celestial, holographic" (6 names, not 7, none match the actual seven faces). The REAL seven faces are bar-cobar twisting, DNP25, KZ25, GZ26, Drinfeld, Sklyanin/STS83, FFR94-Gaudin. AP115 metadata gap.
- **F18**: AP126 violations at `holographic_datum_master.tex:448, 476, 496, 568, 633, 739, 2309` (bare Ω/z for Drinfeld face + KM collision residue variants)
- **F19**: AP125 violations at `celestial_holography_core.tex:961, 989` — `\label{thm:...}` on `\begin{evidence}` environments
- **F20**: Celestial chapter body does NOT cite Costello-Paquette line (CostelloP2201, CPS2208, CPS2306, Costello2302, FernandezCostelloP24) despite all being in bibliography; Pasterski-Shao mentioned in prose without `\cite`
- **F21**: Sklyanin 1982 eight-vertex R-matrix MISSING from bibliography (only Belavin81 + BD82 present)
- **F22**: F5/F7 redundancy — Face 7 is literally `(k+h^v)·F4` per `thm:hdm-face-7:625-626`
- **F23**: F3 Khan-Zeng higher-genus conjectural clause NOT propagated from Vol I `thm:kz-classical-quantum-bridge` to Seven Faces master theorem
- **F24**: F4 Gaiotto-Zeng W_N normalization-convention gap similarly not propagated
- **F25**: "DK face" does not exist — DK is a 6-step ladder in `thqg_line_operators_extensions.tex`, not a face. CLAUDE.md misnames it.
- **F26**: DK-4 overclaim at `thqg_line_operators_extensions.tex:1526-1530`: claims DK-4 proved via `thm:completed-bar-cobar-strong` (algebraic MC4) but DK-4 as defined is representation-theoretic pro-category equivalence, part of `conj:dk-compacts-completion`

**Vol III CY programme audit (Batch 6)**
- **F27**: Vol III κ-spectrum promise UNDELIVERED. `κ_fiber` is undefined anywhere (0 matches); `κ_BKM` has no formal definition, only example values; `def:kappa-spectrum` is in Part III `toroidal_elliptic.tex:3021` not Part II; 3 empty section headers at `modular_trace.tex:143-150`
- **F28**: Vol III stub status INVERTED. MEMORY.md "12 stubs" / CLAUDE.md "5 genuine stubs" are STALE. The 5 flagged "stubs" are actually 152-229-line developed chapters with theorems. They're commented out in `main.tex:451-493` with STUB-AUDIT 2026-04-08 banners citing stale line counts. **~705 lines of developed content silently excluded from build**. Broken `\ref{ch:derived-cy}` at `fukaya_categories.tex:500`.
- **F29**: Costello-Gaiotto 2018 (arXiv:1804.06460 "VOAs and 3d N=4") NOT cited anywhere in Vol III. Direct analog of Vol III's Φ functor applied to Higgs branches. Most serious Vol III citation gap.
- **F30**: Conjecture CY-C is literally Kapustin-Rozansky-Saulina 2009 with A_C in place of KRS's 3D TQFT. KRS 2009 NOT cited.
- **F31**: 2 AP-CY6 theorem-environment violations: `thm:mo-chiral-rmatrix` at `quantum_chiral_algebras.tex:161-174` and `thm:wall-crossing-mc` at `toric_cy3_coha.tex:257-267` both marked ProvedHere but reference unconstructed A_X for CY3
- **F32**: Vol III's own internal red-team `notes/audit_red3_cy_to_chiral.md:19-57` flags a hidden circularity in Step 1 of Φ construction (λ-bracket simultaneously defined by and verified from Jacobi). Fix proposed but not applied.
- **F33**: Shadow-Siegel gap theorem at `toroidal_elliptic.tex:4365-4456` is a genuinely NEW negative result (4 obstructions O1-O4) that deserves headline status but is buried in Part III
- **F34**: 23 `\kappa_{BPS}` violations in `toroidal_elliptic.tex` (should be `\kappa_{BKM}`). Plus 37 other AP113 violations across Vol III.

**Physics identifications audit (Batch 7a)**
- **F35**: Parallel overlapping theorem/conjecture pair for U^mod_X: `thm:platonic-adjunction` (ProvedHere, `higher_genus_modular_koszul.tex:26593`) vs `conj:universal-modular-factorization-envelope` (Conjectured, `frontier_modular_holography_platonic.tex:3523`). Nearly identical adjunctions, not reconciled.
- **F36**: Nishinaka 2026 single-point dependency. U^mod_X existence rests on arXiv:2512.xxxxx — unpublished preprint with placeholder arXiv ID. Second Mok25-class AP11 dependency.
- **F37**: Vol III preface L271-279 is the MOST EGREGIOUS boundary-bulk overclaim: "Volumes I and II prove ... reconstructs gravity" with 4 "proves" + "is incarnated" + "is the universal reconstruction functor", all referring to conjectural content. Direct contradiction with post-F7 Vol I preface.
- **F38**: Bibitem alias hygiene: CDG20 has 3 aliases, CG18 has 4 aliases in Vol II. Creates phantom distinct references in citation analytics.
- **F39**: 3D gravity "climax" has NO Cross-Volume Bridges row in Vol II CLAUDE.md. The climax has no bridge entry.
- **F40**: MEMORY.md "six workpackages" for Dimofte programme is STALE — downscoped to four-part programme.
- **F41**: Two "holographic datum" definitions coexist — 6-tuple H(T) (`frontier_modular_holography_platonic.tex:1146-1235`) vs 8-tuple Π^oc_X (`thqg_open_closed_realization.tex:1477-1525`). CLAUDE.md/MEMORY.md conflate them.
- **F42**: Manuscript `chapters/` is AP94-CLEAN. 0 hits for forbidden strings. The AP94 violation is confined to compute layer.

**Vol II Seven Faces chapter-level (Batch 7b)**
- **F43**: 13 AP126 violations in Vol II across 8 files. Three sites share the same level-stripped Sugawara template (`dnp_identification_master.tex:48`, `thqg_spectral_braiding_extensions.tex:1502`, and the Vol I `holographic_datum_master.tex:448` finding from Batch 5) — common parent template.
- **F44**: Three-site template: `Ω/((k+h^v)z)` level-stripped Sugawara form propagated across volumes.
- **F45**: Vol II Face 3 (Khan-Zeng) silently erases Vol I higher-genus conjectural clause. Master theorem `ProvedHere` propagates stronger claim than underlying Vol I supports.
- **F46**: Vol II Face 4 (Gaiotto-Zeng) silently erases Vol I W_N conjectural qualifier via same master-theorem propagation.
- **F47**: Finkelberg-Tsymbaliuk 2017 (arXiv:1708.01795, canonical shifted-Yangian reference) ABSENT from Vol II bibliography. Face 5 gap.
- **F48**: Vol II Face 6 missing Sklyanin 1982, Etingof-Varchenko 1998 (correction: Felder 1994 IS present as `Fel94`, per Batch 8).
- **F49**: Vol II Face 7 missing Talalaev 2006, Rybnikov 2006.
- **F50**: Vol II Face 4 missing Calogero 1975, Moser 1975, Etingof-Felder-Ma 2009, Olshanski 2002.
- **F51**: Vol II master theorem is a forwarding restatement — 464 lines, 30-line master, 4-line "proof" delegating to Vol I. The real Vol II math is in 3D gravity (~half of Vol II) + DNP line operators + BV half-space + celestial + Kontsevich chapters, NOT in the Seven Faces master.
- **F52**: Batch 7b `4 bbl-core chapters with ZERO conjectures` (celestial, half-space BV, planted forest, Kontsevich integral). Density of ProvedHere claims invites AP40 audit.
- **F53**: Vol II Face 2 has only ONE conjecture across 6 bbl-core chapters in 11,963 lines.

**Full bibliography audit (Batch 7c)**
- **F54**: Vol III has NO BIBLIOGRAPHY. `main.tex:508-509` has `% \bibliography{references}` commented out. Zero .bib files exist. Every Vol III `\cite{}` currently emits `[?]`. 18 of 26 Vol III cite keys dangling.
- **F55**: ~~CFG25 fabricated~~ SUPERSEDED by Batch 8 Angle 3: CFG25 is a REAL paper with wrong bibitem title. See correction above.
- **F56**: `Nish26` literal placeholder arXiv `2512.xxxxx`. 23 downstream cites across 9 Vol I files.
- **F57**: Vol II `DNP25` arXiv ID drift. `main.tex:1504` cites 2506.09728; `main.tex:1506` cites 2508.11749. Vol I uses 2508.11749. Vol II `DNP25` is factually wrong.
- **F58**: Vol II `CG18` hyphen-only collision. `CostelloGaiotto18` (no hyphen) → arXiv:1812.09257 Twisted Holography. `Costello-Gaiotto18` (with hyphen) → arXiv:1804.06460 VOAs and 3d N=4. Two distinct papers differing only by a hyphen. Silent-citation-corruption hazard.
- **F59**: 8 forward-dated Vol I bibitems (2026+). Batch 8 Angle 3 WebFetch verification: 6 are real (Moriwaki26a/b, Nafcha26, CDN26, LQ26, GZ26), 1 has placeholder ID (Nish26), 1 has wrong title (CFG25). Nafcha26 is an ORPHAN (0 cites).
- **F60**: Borcherds 1986 (original VOA definition) MISSING from Vol I. Only `Bor92` Monstrous Moonshine present.
- **F61**: Witten 2007 "3D gravity revisited" (arXiv:0706.3359) MISSING from Vol II. Foundational for 3D gravity climax.
- **F62**: Vol I has 30 undefined-but-cited keys + 57 dead bibitems across 2510 `\cite{}` calls. Top concentration in holography chapters.
- **F63**: Vol I `LuninMathur2001` wrong initial ("S. D. Lunin" → "O. Lunin"); `BPRS15` key/content mismatch; `HerNeg24` title likely fabricated.

**Batch 8 consolidated findings**
- **F64** (corrects F55): CFG25 real paper, title-fix only. See correction above.
- **F65**: Nafcha26 ORPHAN, safe delete.
- **F66**: Vol II FRONTIER.md:18 and Vol III FRONTIER.md:18 both contain a **DIFFERENT fabricated CFG25 identity**: "Cliff-Gannon-Frenkel: universal chiral algebras and genus extension". Two-layer fabrication, metadata version separate from bibitem version.
- **F67**: r-matrix AP128 sub-epidemic in 8+ compute engines. `theorem_seven_face_categorification_engine.py`, `theorem_three_way_r_matrix_engine.py` (4 circularly-agreeing sub-engines), `quantum_rmatrix_barcomplex.py`, `theorem_genus1_seven_faces_engine.py` (6 sites), `elliptic_rmatrix_shadow.py`, `homfly_shadow_yangian_engine.py`, `theorem_bethe_mc_engine.py`, `theorem_cs_knot_invariant_engine.py`. None caught by 119K tests because no test parametrises k=0. Fix: add `pytest -k "k_zero"` mandatory boundary test.
- **F68**: FM5 live violation at `compute/lib/bc_exceptional_categorical_zeta_engine.py:750` — `779247` in `_E8_SMALL_DIMS` (not an E_8 irreducible).
- **F69**: Bar cohomology "new computation" AP128 cluster — `test_bar_cohomology_sl2_explicit_engine.py:177, 188` explicitly "(new computation from this engine)". Likely propagates to sl_3, w_3, w_4, lattice engines.
- **F70**: Six shadow classes, not four: G/L/C/M + M* + W. CLAUDE.md incomplete.
- **F71**: 10 families lack shadow class row in `tab:shadow-tower-census`. Most serious: BP_k (in Master Table with data, absent from shadow tower table).
- **F72**: AP131 `d_gen` symbol ABSENT from all Vol I chapters. Only `d_alg` exists. Agents grepping "d_gen" find nothing.
- **F73**: Vol III introduction.tex:238-241 uses `\kappa_{BPS}` (FORBIDDEN per HZ-7). NEW HZ-7 violation beyond Batch 6's `toroidal_elliptic.tex` finds.
- **F74**: Vol III introduction.tex:122 uses `\kappa_{MacMahon}` — new subscript leak, not in approved set.
- **F75**: Standalone N5_mc5_sewing.tex:865-868 owns the CORRECT Huang05 bibitem ("Differential equations, duality and modular invariance", CCM 7 (2005), 649-706). **Source of truth for monograph fix** — reverse propagation standalone → monograph.

### For the parallel swarm — updated coordination

**I am NOT touching** (Batch 2 swarm's territory): compute-layer AP94 files, Vol I/II/III MC5 status rows, primary bibliography additions.

**I AM touching (Tier 1 application phase, this session)**:
- `/Users/raeez/chiral-bar-cobar/bibliography/references.tex` — Huang05 title reverse-prop from N5; Mok25 author fix; CFG25 title fix
- `/Users/raeez/chiral-bar-cobar-vol2/main.tex` — Mok25 author fix; CFG25 title fix
- 4 standalone .tex files — Mok25 author fix (programme_summary*, survey_v2)
- `/Users/raeez/chiral-bar-cobar/compute/lib/bc_exceptional_categorical_zeta_engine.py:750` — strip 779247
- `/Users/raeez/chiral-bar-cobar/compute/lib/theorem_concordance_rectification_engine.py:91` — Mok25 string fix
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:238-241` — fix κ_BPS → κ_BKM
- 9 `\cite{CFG25}` sites per Batch 8 Angle 2 verdict table (5 → FG12, 4 keep CFG25)
- Vol II FRONTIER.md:18 and Vol III FRONTIER.md:18 — remove "Cliff-Gannon-Frenkel" fabrication

**For Batch 2 swarm to verify**: once Batch 2 agent 2-7 completes Huang05/Huang08 additions, cross-check against the corrected title I propagate from N5.

### Methodology lessons added

11. **Web verification catches fabricated-entry accusations.** Batch 7c flagged CFG25 as fabricated based on the wrong bibitem title. Batch 8 WebFetch found the arXiv ID IS real. Rule: before declaring an entry "fabricated", verify the arXiv ID with an actual web fetch.

12. **The one-dimensional proof discipline (k=0, critical level, generic level) is the MISSING TEST that would catch compute-layer AP126 at scale.** 119K tests pass while 8 r-matrix engines share the wrong mental model, because no test parametrises k=0.

13. **"Stub status" can be INVERTED.** Vol III's CLAUDE.md lists 5 stubs, but those chapters are actually 152-229 lines with theorems, silently excluded from the build. The problem is DEFLATION, not inflation. Rule: verify stub status by current line count, not by metadata.
