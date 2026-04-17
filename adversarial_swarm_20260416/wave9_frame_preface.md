# Wave 9 — Adversarial Audit: Vol I Frame Chapters

**Files audited (live)**:
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex` (4717 lines, 196KB — \include'd in main.tex L846)
- `/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex` (4913 lines, 215KB — \include'd L874)
- `/Users/raeez/chiral-bar-cobar/chapters/frame/guide_to_main_results.tex` (369 lines — \input'd L850)

**Files audited (status: DEAD)**:
- `preface_section1_v2.tex` (581 lines)
- `preface_section1_draft.tex` (682 lines)
- `preface_sections2_4_draft.tex` (1228 lines)
- `preface_sections5_9_draft.tex` (1009 lines)
- `preface_sections10_13_draft.tex` (629 lines)

Verified by `grep -rn` against `main.tex`, `Makefile`, `standalone/`: NONE of the five draft files are \input or \include'd anywhere in the live build. Total ~4,129 dead lines sitting beside the live preface.

**Posture**: I went looking for genuine errors and structural strengthening opportunities. The frame chapters are in materially better shape than typical for a 2700pp manuscript: the live preface opens with the operad (not a "this chapter constructs..." block), the Heisenberg chapter opens with the OPE (CG-style), AP136 is correctly applied (`c·(H_N − 1)` not `c·H_{N-1}`), the AP-CY54 trap is avoided (Drinfeld center described as "right adjoint to forgetful U: E_2-Cat → E_1-Cat", not "categorified averaging"), and the level-bearing r-matrix `k·Ω/z` (AP126/AP141) is used consistently. The audit nonetheless surfaces 14 actionable items, two of which are genuine status discrepancies and one of which is a structural hygiene issue (5 dead drafts).

---

## Section 1. Live preface audit

### 1.1 Status of named theorems vs source-of-truth

Method: name each theorem in the preface "Five Theorems" block (preface.tex L1411–1499) and the early framing paragraph (L46–73), then cross-check against the source label and against guide_to_main_results.tex.

| Preface claim (live) | Source label (resolved) | ClaimStatus tag at source | Preface scope language | Verdict |
|---|---|---|---|---|
| Theorem A: bar-cobar adjunction + Verdier intertwining | `thm:bar-cobar-isomorphism-main` (chiral_koszul_pairs.tex L4194; aux: 11.1.85) | `\ClaimStatusProvedHere` | Stated unconditionally | OK |
| Theorem B: bar-cobar inversion. "Genus 0 unconditional. For arbitrary A, g≥1 conditional on axiom MK:modular; on standard CFT-type surface unconditional except integer-spin βγ." | `thm:higher-genus-inversion` (higher_genus_complementarity.tex L4408) | `\ClaimStatusProvedHere` | Three-tier scoping in preface body (L51–55, L1425–1432) | OK — scoping matches the body |
| Theorem C: complementarity. "Verdier-side Lagrangian splitting proved; ambient shifted-symplectic upgrade conditional on perfectness/nondegeneracy." | `thm:quantum-complementarity-main` (higher_genus_complementarity.tex L527) | `\ClaimStatusProvedHere` | Two-tier scoping (proved part vs conditional upgrade) | OK |
| Theorem D: modular characteristic. "Genus-1 unconditional for every family. UNIFORM-WEIGHT all-genera via clutching/GRR; clutching-uniqueness step is principal conditional element." | `thm:modular-characteristic` (higher_genus_modular_koszul.tex L2830) | `\ClaimStatusProvedHere` | Tagged with UNIFORM-WEIGHT and ALL-WEIGHT+δF^{cross} (AP32 compliant) | OK |
| Theorem H: chiral Hochschild concentration in {0,1,2} on Koszul locus, generic affine level | `thm:hochschild-polynomial-growth` (chiral_hochschild_koszul.tex L1042; aux: 14.4.14) | `\ClaimStatusProvedHere` | Excludes critical level k=−h^v explicitly | OK |
| Family index theorem (`thm:guide-family-index`, guide L240) | guide L241 self-tag: `\ClaimStatusProvedElsewhere` | local | Marked as proved-elsewhere | OK |

**Verdict 1.1**: No fabricated theorems. All five named theorems resolve to actual `\label{...}` lines bearing `\ClaimStatusProvedHere`. Scope-tags (UNIFORM-WEIGHT / ALL-WEIGHT, conditionality on `axiom:MK:modular`, perfectness/nondegeneracy) match between preface and source. No AP4 violation.

### 1.2 AP106 audit ("This chapter constructs..." or "We construct...")

`grep -n "^\\\\section\\|^\\\\subsection\\|^\\\\chapter\\|This chapter constructs\\|This chapter proves\\|We construct"` over preface.tex shows ZERO instances of "This chapter constructs", "This chapter proves", "We construct" as section openings. The opening paragraph (L26–42) opens with the mathematical content ("This monograph studies holomorphic chiral factorisation (co)homology...") which is acceptable monograph-level framing, not a chapter-opening "we construct". Each `\section*` opens with mathematical exposition, not with a meta-statement of intent.

**Verdict 1.2**: AP106 clean.

### 1.3 AP109/AP111 audit (result preview blocks, "What this monograph proves")

`grep -n "What we prove\\|What this monograph proves\\|What this chapter"` over preface.tex returns ZERO matches. The "Five Theorems" block at L1411–1499 is positioned at the END of Section 2 (after the genus tower has been developed), not as a preview block at the top. This is the right architectural choice: the theorems appear when the reader has earned the vocabulary to parse them.

There IS a top-level "five theorems" paragraph at L46–73 (the second paragraph of the preface), but it is short, contentful (each theorem stated with its scope and conditional clauses) and qualifies as a roadmap, not as an AP109/AP111 "What we prove" preview. Borderline-acceptable; if the user wanted to be maximally CG-strict the L46–73 block could be deferred to L1411, but the current placement is defensible because it tells a brand-new reader where the destination is.

**Verdict 1.3**: AP109/AP111 essentially clean. Minor borderline at L46–73 (acceptable).

### 1.4 AP15 audit (verified/established/proved scope inflation)

The preface uses "proved" carefully throughout. Sample check: every "proved" in the Five Theorems block (L46–73, L1411–1499) is paired either with explicit conditional clauses ("conditional on axiom MK:modular", "principal conditional element", "ambient shifted-symplectic upgrade conditional on perfectness/nondegeneracy") or with scope tags (UNIFORM-WEIGHT, ALL-WEIGHT+δF_g^{cross}). The MC1–MC5 status block at L4419–4482 explicitly says "MC1 through MC4 are proved; MC5 is partially proved (analytic sewing at all genera, coderived BV=bar for all four classes including class~M; genuswise chain-level identification conjectural, class~M chain-level false)" — this is honest scope.

**One moderate inflation candidate**: L4480 "BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived})". Wave 5 (bv_feynman) found that the feynman_connection chapter is the "model of honest exposition", so the underlying chapter likely backs this. Not flagged as a violation, but flagged for re-confirmation against `thm:bv-bar-coderived`.

**Verdict 1.4**: AP15 clean within tolerance.

### 1.5 Inflated counts

L4582–4594 (preface): "Every formula in this preface has been verified by an independent symbolic computation layer: over 1,300 engine modules and over 119,000 tests..."

Comparison with CLAUDE.md L9 (canonical, 2026-04-16): "Vol I *Modular Koszul Duality* (this repo, ~2,700pp, 139,568 tests, 3,726 engines)".

```
Preface claim     | CLAUDE.md (live)  | Delta
1,300 engines     | 3,726 engines     | preface UNDERSTATES by 65% (≈1/2.87)
119,000 tests     | 139,568 tests     | preface UNDERSTATES by 17% (≈1/1.17)
```

The preface understates current scale. This is an FM46-class issue (stale leading-edge counts) but in the safe direction (understatement). If updating, recommended numerical phrasing is "over 3,700 engine modules and over 139,000 tests" (round down conservatively). This is safe to update; no strengthening required, just a refresh.

**Verdict 1.5**: FM46-style stale count. Low priority but trivially fixable. Lines 4583–4584.

### 1.6 Section ordering quirk: 1, 1', 1''

The live preface uses Section 1 (ordered bar construction), Section 1' (bar chain models on curve geometries, L827), Section 1'' (E_n-chiral algebras and derived centres, L928), then Section 2, 3, ..., 10. This is unusual. The 1' and 1'' sections were clearly inserted as supplementary subsections to Section 1 without renumbering downstream sections. Not a bug, but an aesthetic flag: a typical reader will wonder if 1' and 1'' are "less important" than the integers. Recommend either (a) renumber to Sections 1, 2, 3, ... 12 (a one-time pass) or (b) call them 1.5 / 1.75 (worse). Current state is suboptimal but does not introduce mathematical confusion.

**Verdict 1.6**: Cosmetic only. Logged as low-priority restructuring opportunity.

---

## Section 2. Draft files audit

`preface_section1_v2.tex`, `preface_section1_draft.tex`, `preface_sections2_4_draft.tex`, `preface_sections5_9_draft.tex`, `preface_sections10_13_draft.tex` — total 4,129 lines beside the 4,717-line live preface, in the same `chapters/frame/` directory.

**Live status**: NONE of these files are \input or \include in `main.tex`, the `Makefile`, the `standalone/` directory, or anywhere else under the build path. Verified via `grep -rn "preface_section..."` over the entire repo — only matches are inside the files themselves and inside the audit scaffolding (resume_*, fix_wave_*, audit_campaign_*, .md notes).

**Content drift**: spot-checked `preface_section1_v2.tex` L1–60 against live `preface.tex` L26–155 (same Section 1, propagator / bar complex content):

- Live preface opens "This monograph studies holomorphic chiral factorisation (co)homology via bar and cobar chain constructions at various geometric locations on algebraic curves. The geometry determines the operad..."
- Draft (v2) opens "A chiral algebra on a smooth algebraic curve X encodes operator product singularities..."

Different opening, different organising sentence. The drafts are *earlier prose* that was superseded. Confirming that nothing is broken if they are removed: zero downstream references. They are pure dead weight.

**Risk if left in place**: a future agent (V2-AP38 / V2-AP19 class) reading `chapters/frame/` may pick up a draft, edit it, and silently propagate stale prose because the draft "looks like" a live preface fragment. This has already happened in nearby manuscripts (Vol II / Vol III have analogous archive-vs-live confusion). Wave 6 introduction_survey already raised this question.

**Recommendation**: move all five drafts to `archive/preface_drafts_pre_20260413/` (or similar). Do NOT delete (audit trail), but get them out of `chapters/frame/`. This is the single highest-value hygiene move from this audit.

**Verdict 2**: 5 dead drafts. Move to archive. No edits to live build.

---

## Section 3. Heisenberg frame audit

### 3.1 AP106/AP108 — opening style

`heisenberg_frame.tex` L1–7 opens:
```
\chapter{The Gaussian Archetype}\label{ch:heisenberg-frame}

One generator. One relation.
\[
J(z)\,J(w) \;\sim\; \frac{k}{(z-w)^2}.
\]
If bar-cobar duality fails for this OPE, it fails everywhere.
```

This is a model CG opening: **the OPE is the very first mathematical content**, with a prose hook ("If bar-cobar duality fails for this OPE, it fails everywhere") that establishes WHY this algebra is the canonical frame. AP106 satisfied. AP108 satisfied (Heisenberg explicitly framed as "the simplest chiral algebra... the boundary algebra of abelian Chern--Simons theory" — opening, not the atom).

### 3.2 r(z) vs R(z) convention (AP126/AP141 + Wave 1 cross-vol clash)

Wave 1 found that "e1_primacy / N3 use linear r(z), chapter+5 standalones use curved R(z)". Heisenberg frame uses BOTH explicitly and cross-references them:

- L102 (in opening prose): `r^{Heis}(z) = k/z`. AP126 satisfied: at k=0, r vanishes.
- L104: `R(z) = e^{kℏ/z}` (the curved exponentiation).
- L1979–1982: `r(z) = k/z (after dlog absorption of the double pole, with the level k surviving)... exponential R(z) = exp(kℏ/z) (Theorem ~rosetta-cs-r-matrix...)`
- L3926–3949: `\label{thm:rosetta-cs-r-matrix}` provides a 3-clause statement linking the linear r(z) and curved R(z) explicitly. The Laplace transform / exponentiation is the bridge.

**Verdict 3.2**: Convention CLASH RESOLVED inside heisenberg_frame.tex via thm:rosetta-cs-r-matrix. The Wave 1 finding (clash between e1_primacy and chapter+5 standalones) does not apply to the frame chapter. The frame chapter is the rosetta stone — recommend other files cite `thm:rosetta-cs-r-matrix` when both conventions appear.

### 3.3 Genus-1 character formula

L1413–1418: `Z_{E_τ}^{H} = Tr_{F_k} q^{L_0 - c/24} = 1/η(τ) = q^{-1/24} ∏_{n≥1} 1/(1-q^n)`.

For the Heisenberg with central charge c=1 (one boson): the standard character is indeed `1/η(τ)`. Verified: Heisenberg c=1, q^{-c/24} = q^{-1/24} ✓; the partition counting ∏ 1/(1-q^n) ✓. Note: tagged `\ClaimStatusProvedElsewhere` (this is classical Frenkel-Kac).

**No k-dependence in the character**: this is correct — the level k determines the OPE normalization but NOT the Fock space structure (the Fock space at any level k≠0 is the same vector space). Adversarial check passes.

### 3.4 Class assignment

Heisenberg = class G (Gaussian). Verified: L41–45 ("κ(H_k) = k. The cubic shadow S_3 vanishes. The quartic contact invariant S_4 vanishes... the entire obstruction tower terminates at degree 2: H_k is class G"); L112 ("Heisenberg is class G: shadow depth 2, tower terminates, SC-formal"); L2041 ("Heisenberg is of class G (Gaussian): the shadow obstruction tower"); L2187 ("H_k is of class G").

**Verdict 3.4**: Class G assignment consistent. No drift.

### 3.5 AP107 (r^coll vs r(z) for odd generators)

`heisenberg_frame.tex` L3171–3233 contains the dedicated `\subsection{The braided example: the odd current algebra and the spectral R-matrix}` which **explicitly distinguishes the odd current algebra from the Heisenberg**. The remark `rem:abelian-cs-is-heisenberg` (L3199–3233) is one of the most surgical AP-defenses I've seen in this manuscript:

> "The boundary algebra of U(1) Chern-Simons theory on C × R_{≥0} is the **Heisenberg algebra** H_k itself: the boundary current J is even/bosonic..."
> "The odd current algebra (eq:rosetta-cs-ope) is **not** a Chern-Simons boundary algebra; it is included for the bar-complex contrast it provides. Its single fermionic generator has only a simple pole..."
> "Both algebras are E_∞-chiral with nontrivial derived R-matrices... neither is E_1-chiral. The genuine E_1 atom is the Yangian, where the R-matrix constitutes independent input not derivable from any local OPE."

This is the AP107/AP108 defense in textbook form. Future readers cannot confuse the two cases.

**Verdict 3.5**: AP107 explicitly defended. Best-in-class.

---

## Section 4. Guide to main results audit

Wave 6 (introduction_survey) already said "consistent with chapters; no overclaim." I verified key entries against source.

### 4.1 Theorem cross-references resolve to ProvedHere

| Guide entry | Source label | Source ClaimStatus |
|---|---|---|
| Theorem A → `thm:bar-cobar-isomorphism-main` | chiral_koszul_pairs.tex L4194 | `\ClaimStatusProvedHere` |
| Theorem B → `thm:higher-genus-inversion` | higher_genus_complementarity.tex L4408 | `\ClaimStatusProvedHere` |
| Theorem C → `thm:quantum-complementarity-main` | higher_genus_complementarity.tex L527 | `\ClaimStatusProvedHere` |
| Theorem D → `thm:modular-characteristic` | higher_genus_modular_koszul.tex L2830 | `\ClaimStatusProvedHere` |
| Theorem H → `thm:hochschild-polynomial-growth` | chiral_hochschild_koszul.tex L1042 | `\ClaimStatusProvedHere` |

All five resolve. No fabricated labels.

### 4.2 Standing assumptions reference

guide_to_main_results.tex L14 references `\ref{sec:standing-assumptions}`. Resolution: defined at `chapters/theory/introduction.tex` L2549 (and standalone/introduction_full_survey.tex L5266). aux file maps it to "1.10 / page 139". Reference resolves but the section number 1.10 is unusually deep — readers entering via the guide will hit a forward reference. Acceptable but could be flagged as a navigation friction point.

### 4.3 MC4/MC5 status

Guide L99–109: MC5 (genus tower): "(1) Analytic HS-sewing **proved**... (2) Genus-0 algebraic BRST/bar **proved**. (3) D^{co}-level BV=bar **proved** for all shadow classes. (4) Chain-level BV/BRST/bar **conjectural** (class M fails). (5) Tree-level amplitude pairing **conditional**."

This matches the live preface L4464–4482 verbatim in conditional structure. No drift between guide and preface.

### 4.4 Family index theorem

Guide L240–281, `thm:guide-family-index`, `\ClaimStatusProvedElsewhere`. The body of the guide gives three components: GRR formula, A-hat identification, Verdier compatibility. The Verdier compatibility states `kappa(A) + kappa(A^!)` for κ_3 = 250/3 (W_3) and kappa(Vir) + kappa(Vir^!) = 13. Cross-check: K_3 = 2(N-1)(2N²+2N+1) at N=3 = 2·2·25 = 100 (chapters/examples/w_algebras_deep.tex L626). κ(W_3) + κ(W_3^!) = (5/6)·c + (5/6)·c' = (5/6)·K_3 = 500/6 = 250/3 ✓.

**Verdict 4**: Guide is consistent and resolves. Wave 6's verdict stands.

---

## Section 5. Cross-frame consistency

### 5.1 Theorem A naming

- preface.tex L46–50 calls it "Theorem A (bar-cobar adjunction and Verdier intertwining)".
- guide_to_main_results.tex L26 calls it "**Theorem A** Bar–cobar adjunction... intertwined with Verdier duality..."
- heisenberg_frame.tex L4582–4590 calls it "**Theorem A** (Theorem~\ref{thm:bar-cobar-isomorphism-main})".

All three use "Theorem A" as the public name and resolve to the same source label. Consistent.

### 5.2 Theorem D and the UNIFORM-WEIGHT tag (AP32)

AP32 in CLAUDE.md: *"Every occurrence of obs_g, F_g, λ_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation."*

Preface obs_g/F_g occurrences:
- L46–67: theorem A summary block tags `\textup{(UNIFORM-WEIGHT)}` and `\textup{(ALL-WEIGHT $+\delta F_g^{cross}$)}` ✓
- L1448–1462 (Theorem D body): tags `\textup{(UNIFORM-WEIGHT)}` and `\textup{(ALL-WEIGHT $+\delta F_g^{cross}$)}` ✓
- L2422 (Section 5.1 scalar curvature): "for uniform-weight algebras at all genera via clutching/GRR" ✓ (informal but adequate at this exposition level)
- L4607–4613 (four-test interface principle): tags `\textup{(UNIFORM-WEIGHT)}` and `\textup{(ALL-WEIGHT $+\delta F_g^{cross}$)}` ✓

Guide:
- L307–311 (rem:guide-four-test-interface): "obs_g(A) = κ(A)·λ_g (UNIFORM-WEIGHT) for uniform-weight algebras at all genera, unconditionally at genus~$1$" ✓

**Verdict 5.2**: AP32 clean across all three frame files. No untagged obs_g.

### 5.3 W_N kappa formula (AP136)

Preface L2443–2446: `\mathcal W_N(\widehat{\mathfrak{sl}}_N): κ = c·(H_N − 1)`. Footnote L2453: "Here H_N = sum_{j=1}^N 1/j is the N-th harmonic number".

Preface L3096–3098: `κ(\cW_3) = 5c/6 (from κ(\cW_N) = c(H_N − 1) at N=3: H_3 = 1+1/2+1/3 = 11/6, so H_3 − 1 = 5/6)`.

This is the **correct AP136 formulation**. Cross-check with w_algebras_deep.tex L622–626: also uses `H_N − 1`. CLAUDE.md AP136 itself confessed that the bare CLAUDE.md formula was once H_{N−1} and had to be corrected; the .tex never had the bug.

**Verdict 5.3**: AP136 clean and the preface explicitly demonstrates the H_3 calculation, which is exactly the right pedagogy for catching the bug at the smallest non-trivial N.

### 5.4 Drinfeld center description (AP-CY54 / Vol III crossover)

Vol III AP-CY54 forbids "categorified averaging" for the Drinfeld center; the right formulation is "right adjoint to forgetful U: E_2-Cat → E_1-Cat, equivalently categorified commutant via half-braidings".

preface.tex L3817–3825 (Section 10.1, Five Arrows):

> "Arrow 3 is the Drinfeld center Z: E_1-Cat → E_2-Cat, **the right adjoint to the forgetful functor U: E_2-Cat → E_1-Cat**: it constructs an E_2-braided monoidal category from E_1-module data by adjoining half-braidings σ_M: M ⊗ (-) → (-) ⊗ M. **The averaging map av is the further (lossy) step E_2 → E_∞** that projects the braiding to its scalar shadow κ(A); the center constructs what averaging destroys."

This is the AP-CY54-compliant formulation in textbook form. The preface then explicitly contrasts construction (Z) with destruction (av) and notes that direct restriction E_3^top → E_2 gives only symmetric braiding (π_1(Conf_2(R^3)) trivial — AP-CY53 also satisfied).

**Verdict 5.4**: AP-CY54 satisfied; AP-CY53 satisfied. The preface's Section 10.1 is the canonical defense across all three volumes — Vol III could cite this paragraph rather than re-deriving.

### 5.5 r-matrix level prefactor (AP126/AP141)

Preface uses level-bearing r-matrices throughout: `r(z) = k/z` (Heisenberg L597, L3277), `r(z) = kΩ/z` (Kac-Moody L711–714, L3293, L4033, L4363), `r(z) = (c/2)/z^3 + 2T/z` (Virasoro L3301, L4401). All vanish at the appropriate vanishing point (k=0 or c=0). No bare Ω/z.

**Verdict 5.5**: AP126/AP141 clean throughout the frame chapters.

---

## Section 6. New-reader experience

Steelman: a brand-new reader (PhD student, knows VOAs at the Frenkel-BenZvi level, has never seen factorization homology) picks up Vol I and reads only the frame chapters in order: preface → guide → Heisenberg.

### 6.1 What the reader gets right

- **The five theorems**: stated three times (L46–73 abstract, L1411–1499 body, guide table). Status of each is clear: A unconditional, B genus-0 unconditional / g≥1 conditional, C Verdier proved / shifted-symplectic conditional, D genus-1 unconditional / UNIFORM-WEIGHT all-genera proved / multi-weight at g≥2 has cross-channel correction, H Koszul locus proved / critical level excluded.
- **The conventions**: r(z) = k·Ω/z (linear) is the bar-side / classical convention; R(z) = exp(kℏ/z) (curved) is the quantum/Yangian convention; the bridge is `thm:rosetta-cs-r-matrix` in heisenberg_frame.tex.
- **The kappa-spectrum**: κ(A) is a single scalar, the OPE-derived modular characteristic, computed family-by-family (Heisenberg = k, Kac-Moody = (k+h^v)dim(g)/(2h^v), Virasoro = c/2, W_N = c·(H_N − 1)). The complementarity sum κ(A) + κ(A^!) is family-specific (0 for KM/free fields, 13 for Virasoro, 250/3 for W_3, 98/3 for Bershadsky-Polyakov).
- **The shadow class hierarchy**: G (Heisenberg, depth 2), L (KM, depth 3), C (βγ, depth 4), M (Virasoro/W_N, depth ∞).
- **The conjecture**: `conj:v1-drinfeld-center-equals-bulk` (preface L3971–3985) is clearly marked as a CONJECTURE with three identified obstructions and partial closure for affine KM.

### 6.2 What the reader gets wrong (or might)

- **Section 1 / 1' / 1''**: the prime/double-prime sectioning is mathematically harmless but cosmetically jarring. A first-time reader will assume 1' is supplementary to 1 and may skim it; in fact 1' (curve geometries) and 1'' (E_n-chiral algebras) are both load-bearing for understanding Sections 2 onwards.
- **The L46–73 "five theorems" paragraph**: a brand-new reader sees "Theorem D: UNIFORM-WEIGHT" before learning what UNIFORM-WEIGHT means. The tag is defined in the body (Section 5 / 7), not on first appearance. This is acceptable for a research monograph but suboptimal pedagogy. Suggestion: add a one-sentence forward reference: "(scope tags defined in §7)".
- **Engine/test counts at L4583–4584**: reader sees "1,300 engines, 119,000 tests" and may compare to CLAUDE.md (3,726 engines, 139,568 tests) and conclude one source is wrong. The preface number is stale.
- **Drafts in chapters/frame/**: a reader navigating the source tree (especially via GitHub or a file browser) will see five files starting with `preface_section*` and naturally assume they are in the build. They are not.

### 6.3 Reader-blocking issues

None. No mathematical confusion, no fabricated theorems, no AP106/AP109 walls. The reader CAN parse the frame and reach the body of the manuscript with a correct picture.

---

## Section 7. Three upgrade paths (strengthening, not downgrading)

The user's explicit posture is HEAL by realizing the strongest possible mathematical statements. Three candidate stronger framings the preface could safely make:

### 7.1 Upgrade path A — Drinfeld-Kohno / Verlinde / Borcherds as ONE machine

The current preface L3754–4036 (Section 10, the "E_n operadic circle") implicitly says: "the bar-cobar machine, applied at different geometries, recovers DK/Verlinde/Borcherds." But it does not name the unification explicitly.

**Stronger framing (justifiable now)**: Add a one-paragraph principle near L1411 or L4609:

> "**The unification principle.** The bar-cobar machine, instantiated on three geometries, recovers three classical results: on Conf_n(C) at genus 0 with KM input, the Drinfeld-Kohno theorem (KZ monodromy = quantum group R-matrix); on M_g,n at integer level, the Verlinde formula (Z_g = sum_j S_{0j}^{2-2g}, prop:verlinde-from-ordered, already proved through genus 6); on K3xE with Borcherds-lift completion, the Phi_10 = bar-Euler-product identification (Vol III). One construction, three classical theorems."

This is a CG-style structural claim that the preface has earned by its own theorems. Currently scattered (Verlinde mentioned at L4022–4027; Borcherds mentioned only in Vol III); collecting them as a principle would be a strict strengthening, not a downgrade.

### 7.2 Upgrade path B — The conductor K as a UNIVERSAL invariant with explicit family formula

The guide L274–279 says `κ(A) + κ(A^!)` is "a root-datum invariant (0 for KM/free fields, ρ(g)·K_N for W_N-algebras; e.g. 13 for Virasoro, 250/3 for W_3)". The preface L4407–4435 footnote: K_N = 2(N-1)(2N²+2N+1).

**Stronger framing (justifiable now)**: Promote this to a named object. Currently the manuscript has 6+ named structural numbers (κ, c, Δ, S_r, K_N, ρ_K) that are introduced piecemeal. K_N has a closed-form formula and a Lie-theoretic interpretation (pole-order count from the Drinfeld-Sokolov stress tensor). A 2–3 line paragraph naming it "the Koszul conductor" with the closed form K_N = 2(N-1)(2N²+2N+1) and the table {K_2 = 13, K_3 = 100, K_4 = 270, K_5 = 580, K_6 = 1085, K_7 = 1806, K_8 = 2820} (already in w_algebras_deep.tex L3166) would strengthen the preface's structural framing without making any new claims.

The W_3 sum 250/3 = (5/6) · K_3 = (5/6) · 100 already appears, but the H_N − 1 prefactor is hidden in a parenthetical. Surfacing it as κ(A) + κ(A^!) = (H_N − 1) · K_N for principal W-algebras would be a single clean closed-form statement of three currently scattered facts.

### 7.3 Upgrade path C — G/L/C/M classification as a STRUCTURAL theorem

The preface uses G/L/C/M throughout (L3279 census, L2041 Heisenberg = G, etc.) but never names the classification as a theorem. It is in fact a theorem: every standard chiral algebra has a determinate shadow depth, and the four classes exhaust the standard landscape. The preface treats it as an organisational scheme rather than a result.

**Stronger framing (justifiable now)**: the classification is provably exhaustive on the standard landscape (Heisenberg & free fields = G; KM = L; βγ = C; Virasoro & W_N = M). Naming this as `Theorem (Shadow class quadrichotomy)` somewhere in Section 6 ("The shadow obstruction tower") would elevate it from organising scheme to structural fact. The ingredients are already present:

- depth 2 for Gaussian algebras (no first-order pole) — proved L644–646
- depth 3 for KM (Lie bracket, no quartic) — proved L644–646 + family table
- depth 4 for βγ (contact term) — preface L3322–3329, prop in chapters/examples/landscape_census.tex
- depth ∞ for Virasoro/W_N (composite primaries) — proved L3091–3098

This is the structural fact that makes the rest of the manuscript navigable; surfacing it as a theorem would be the highest-leverage strengthening.

**Note on caveats**: G/L/C/M classification is BY shadow depth on the STANDARD landscape (E_∞ vertex algebras with finite generation). The classification on the genuine E_1 side (Yangians, EK quantum vertex algebras) requires the corresponding ordered-bar shadow tower, which the preface treats only at the Yangian level. The strengthened theorem statement should scope to "the standard landscape".

---

## Section 8. First-principles protocol applied (AP-CY61 / AP186 / AP158)

Two confusion points appeared during this audit. For each, the protocol is to find the ghost theorem, the wrong claim, and the correct relationship.

### 8.1 "The drafts are deprecated" — ghost theorem investigation

**Wrong claim** (implicit, by the file system): "preface_section1_v2.tex and four other drafts are part of the live build."

**Ghost theorem**: There IS a true theorem nearby — the file `preface.tex` IS the result of a multi-pass redrafting process where Section 1 went through v1 → v1_draft → v2 → live, and Sections 2–4, 5–9, 10–13 each had a draft pass. The drafts are not zero-content; they are the ARCHAEOLOGICAL TRACE of how the live preface was built. Some prose in the live preface may have ORIGINATED in a draft, and the drafts may contain alternative formulations that did not make it into the live version.

**Correct relationship**: drafts are dead-and-historical, not dead-and-equivalent. They should be MOVED to an archive directory, not deleted. The ghost theorem is "the live preface was assembled from 5 draft fragments; the assembly is now complete". The action is: archive, not delete.

### 8.2 "Section 1' and 1'' are supplementary" — ghost theorem

**Wrong reading** (a brand-new reader): "Sections 1' and 1'' are footnotes to Section 1; the 'real' content starts at Section 2."

**Ghost theorem**: The true relationship is that Sections 1, 1', 1'' are THREE successive entry points at three different levels of abstraction:
- Section 1: the algebraic engine (bar complex, propagator, residue differential) on a FIXED curve.
- Section 1': the same engine instantiated on FIVE specific curve geometries (D, D*, annulus, nodal, pair of pants).
- Section 1'': the engine lifted to the E_n hierarchy (E_∞ → E_1 → E_2 → E_3 with topologisation).

These are not supplementary; they are the THREE LENSES (algebraic / geometric / operadic) on the same construction. The 1' / 1'' notation hides this. **Correct framing**: rename to "Section 1.A. The algebraic engine. / Section 1.B. Five curve geometries. / Section 1.C. The E_n hierarchy." — or, more conservatively, rename to consecutive integers 1, 2, 3 and renumber all downstream sections. Either route surfaces the structural truth that 1' and 1'' are co-equal with 1, not subordinate.

---

## Section 9. Cache write-back (patterns appearing 2+ times across this audit)

Per project_two_derived_centers.md / feedback_cache_write_back.md: enforcement findings MUST be written back to the cache. Two patterns from this audit qualify.

### 9.1 New entry candidate — "Multi-pass draft files left in chapters/"

**Pattern**: when a long-form preface or chapter is rewritten across multiple sessions, the draft files (preface_section1_draft.tex, etc.) get left beside the live version in the same directory rather than archived. Risk: future agents may edit the wrong file. Frequency: 5 dead drafts in Vol I `chapters/frame/` (this audit); analogous draft accumulation likely in Vol II/III.

**Defense**: add a hygiene check to `make audit` or a session-entry checklist: `find chapters/ -name "*_draft.tex" -o -name "*_v2.tex" -o -name "*_v3.tex"` and fail if any are not in `archive/`. Cross-volume FM appendix candidate: **FM47. Draft accumulation in chapters/.**

### 9.2 New entry candidate — "Stale leading-edge counts in preface assessment paragraphs"

**Pattern**: preface and introduction blocks contain "over N engines and over M tests" claims that go stale as the compute layer grows. Vol III FM46 caught this at the chapter-line-count level; this audit catches it at the engine/test-count level (preface L4583: 1,300 engines vs CLAUDE.md 3,726 engines = 65% understatement).

**Defense**: every "over N engines" or "over M tests" string in the preface should be paired with an inline source-of-truth comment pointing to CLAUDE.md, and `make verify-counts` should grep all such strings and compare against CLAUDE.md. Cross-volume FM appendix candidate: **FM48. Stale engine/test counts in preface/introduction.**

---

## Punch list (priority-ordered)

| # | Item | Severity | File / Line | Action |
|---|---|---|---|---|
| 1 | 5 dead draft files in chapters/frame/ | HIGH (hygiene) | `chapters/frame/preface_section1_v2.tex`, `_section1_draft.tex`, `_sections2_4_draft.tex`, `_sections5_9_draft.tex`, `_sections10_13_draft.tex` | Move to `archive/preface_drafts_pre_20260413/` |
| 2 | Stale engine/test counts | LOW (refresh) | `preface.tex` L4583–4584 | Update "1,300 → 3,726", "119,000 → 139,568" (or "over 3,700 engines and over 139,000 tests") |
| 3 | UPGRADE: name "the unification principle" (DK + Verlinde + Borcherds = one machine) | OPPORTUNITY (strengthening) | `preface.tex` near L4609 (four-test interface principle) | Add a one-paragraph principle declaration |
| 4 | UPGRADE: surface the Koszul conductor K_N closed form | OPPORTUNITY (strengthening) | `preface.tex` L2455 (already present in footnote, expand to inline display) | Promote to a one-paragraph "named structural number" passage |
| 5 | UPGRADE: state G/L/C/M as the "shadow class quadrichotomy" theorem | OPPORTUNITY (strengthening) | `preface.tex` Section 6 (L2665+) | Add `\begin{theorem}[Shadow class quadrichotomy on the standard landscape]\ClaimStatusProvedHere ... \end{theorem}` |
| 6 | Section 1 / 1' / 1'' renumbering (cosmetic) | LOW (cosmetic) | `preface.tex` L827, L928 | Either rename to 1.A/1.B/1.C or renumber 1, 2, 3 with downstream cascade |
| 7 | UNIFORM-WEIGHT tag forward-ref in opening summary | LOW (pedagogy) | `preface.tex` L65 | Add "(scope tags UNIFORM-WEIGHT and ALL-WEIGHT defined in §7)" |
| 8 | Standing assumptions forward ref from guide | LOW (pedagogy) | `guide_to_main_results.tex` L14 | Optional: inline the standing assumptions in a footnote |
| 9 | New AP/FM entries: FM47 (draft accumulation), FM48 (stale preface counts) | DOCUMENTATION | `CLAUDE.md` failure-modes section | Cache write-back |

Items 1, 2, 9 are pure hygiene and can be done immediately.
Items 3–5 are strengthenings consistent with the user's stated posture; they require an editorial decision but no new mathematics.
Items 6–8 are minor pedagogical/cosmetic refinements.

**No status downgrades.** Every theorem that is currently `\ClaimStatusProvedHere` should remain so. Every conditional clause is correctly conditioned. Every scope tag is correctly applied.

---

## Final assessment

The Vol I frame chapters are NOT the weak link of the manuscript. They display the highest concentration of AP-defenses I have audited so far in this swarm: AP106 clean, AP107 surgically defended (rem:abelian-cs-is-heisenberg), AP109/AP111 clean, AP126/AP141 clean throughout, AP136 correctly applied with explicit H_3 calculation, AP-CY53 and AP-CY54 satisfied (the Drinfeld center is "right adjoint to forgetful", not "categorified averaging"; π_1(Conf_2(R^3)) trivial is acknowledged), AP32 (UNIFORM-WEIGHT tagging) clean across all three frame files. The Heisenberg frame is a model CG opening (the OPE in line 5 of the chapter, prose hook in line 7).

The single highest-value action from this audit is **moving the 5 dead drafts out of `chapters/frame/`**. Everything else is hygiene refresh or strengthening opportunity.

Wave 6's verdict ("guide_to_main_results.tex is consistent with chapters; no overclaim") is confirmed by spot-check.
Wave 5's verdict ("feynman_connection.tex is a model of honest exposition") is matched here: heisenberg_frame.tex is a model of honest exposition.
Wave 1's clash finding (linear vs curved r-matrix) is RESOLVED inside heisenberg_frame.tex via thm:rosetta-cs-r-matrix; other chapters should cite this theorem when both conventions appear.

If the rest of Vol I matched the frame chapters in AP-defense density, this manuscript would be near publication-ready.
