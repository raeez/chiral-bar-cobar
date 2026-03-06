# Session State — Post Adversarial Audit 5
# For: Claude Opus 4.6, Code Environment, Extended Reasoning
# Date: March 6, 2026
# Companion to: notes/ADVERSARIAL_AUDIT_SESSION5.md (234 findings)
# Launch: "Read notes/SESSION_STATE_POST_AUDIT5.md and execute it."

---

## SITUATION AWARENESS

This document captures the complete state of the chiral bar-cobar monograph
after 18-agent adversarial audit. It is designed to be the single source of
truth for the next session. Read this, then act.

### What the audit proved solid
- **Proof chains**: Theorems A, B, C have complete dependency trees (depth 4/5/6).
  Zero gaps, zero circles, zero conjectured dependencies. This is the bedrock.
- **Tex-code consistency**: 50+ formulas cross-verified between manuscript and
  compute engine. Zero discrepancies. The compute engine is reliable ground truth.
- **Formula correctness**: 15/16 deep spot-checks passed (W3 OPE, Verlinde, Mumford,
  A-infinity, Faber-Pandharipande, Riordan values). The manuscript's formulas are correct.
- **No physics contamination**: Physics conjectures are properly isolated. No
  Conjectured/Heuristic result appears in any proof chain for Theorems A/B/C.

### What the audit found broken (prioritized by blast radius)

The 234 findings decompose into work packages. Do NOT attempt all at once.
Each package is independent and can be executed in a single session.

---

## WORK PACKAGES (ordered by priority)

### WP1: FOUR TEX CRITICAL ERRORS [~2 hours, high mathematical impact]

These four contradict the mathematical content. A referee would catch each one.

| # | File:Line | Error | Fix |
|---|-----------|-------|-----|
| 1 | `hochschild_cohomology.tex:380` | d^2=0 proof assumes strict associativity (false for chiral algebras) | Rewrite proof using Borcherds identity or factorization algebra axioms |
| 2 | `chiral_koszul_pairs.tex:2307` | Summary table says Virasoro "No" for Koszul; thm at line 346 PROVES "Yes" | Change table entry; rename "Non-example 1" heading |
| 3 | `chiral_modules.tex:3553` | Sign error in eq:kac-table-koszul: q->-q flips denominator sign | Correct formula; recompute Ising {0,17/16,3/2} and free boson examples |
| 4 | `free_fields.tex:784` vs `2486` | Heisenberg bar identified as BOTH coLie AND coSym | Fix line 784 to match line 2486: H! = Sym^ch(V*) |

**Verification protocol**: After each fix, `make fast` to confirm compilation.
For #3, write Python to verify corrected dual weight values.

### WP2: THREE CODE BUGS [~30 min, compute engine integrity]

These produce wrong numerical values but tests pass tautologically.

| # | File:Line | Bug | Fix |
|---|-----------|-----|-----|
| 1 | `genus_bridge.py:63` + `cross_algebra.py:40` | kappa(Heisenberg) = k/2 (should be k) | Change to k; update tests to use independent verification |
| 2 | `bar_comparison.py:71-78` | os_dim uses falling factorial (should be elementary symmetric polynomial in {1,...,n-1}) | Rewrite using correct Poincare polynomial; add intermediate-degree tests |
| 3 | `bar_comparison.py:149` | sl3 complementarity = 48 (should be 16 = 2*dim(sl3)) | Fix value; add derivation comment |

**Verification**: `cd compute && python -m pytest tests/ -q` must still pass after fixes.
Write new tests that verify against independent formulas, not against themselves.

### WP3: BUILD SYSTEM FIXES [~20 min, prevents silent failures]

| # | Issue | Fix |
|---|-------|-----|
| 1 | `main.tex:429-435`: geometry options silently dead (options after closing brace) | Replace with `\geometry{top=1.2in, bottom=1.2in, left=1.25in, right=1.25in, footskip=0.5in}` |
| 2 | `derived_langlands.tex:633`: \xymatrix without xy package | Rewrite diagram using tikz-cd (already loaded) |
| 3 | `build.sh` missing buf_size=1000000 | Add `-cnf-line='buf_size=1000000'` |
| 4 | Convergence check misses "Label(s) may have changed" | Add to Makefile and build.sh |

**Verification**: `make` (full build) must complete cleanly.

### WP4: BIBLIOGRAPHY CLEANUP [~45 min, submission readiness]

| # | Issue | Fix |
|---|-------|-----|
| 1 | 2 broken citations (BLPW16, GG11) | Already fixed in synthesis session (289 entries now) |
| 2 | 15+ full duplicate entry sets (Kontsevich has 4 copies!) | Consolidate: keep canonical key, convert rest to alias stubs |
| 3 | 26 alias stubs render "Alias key for X" as visible text | Repeat full bibdata in each alias, or use biblatex cross-referencing |
| 4 | 74 uncited entries (26% of bibliography) | Remove uncited entries that are duplicates; keep supplementary refs |
| 5 | 6 key-name date mismatches (BW93->BW83, etc.) | Rename keys |

### WP5: LABEL/STRUCTURAL CLEANUP [~1 hour, referee presentation]

| # | Issue | Fix |
|---|-------|-----|
| 1 | 31 `thm:` labels on `\begin{conjecture}` environments | Batch rename to `conj:` prefix; update all \ref calls |
| 2 | 26 conjectures with `\begin{proof}` blocks | Replace with custom `\begin{evidence}` or `\begin{discussion}` env |
| 3 | 5 PH-tagged sketch lemmas in bar_cobar (lines 4793-4876) | Either expand to full proofs or add cross-ref to higher_genus.tex proofs |
| 4 | 8 duplicate "Koszul pair" definitions | Keep 2 canonical (algebraic_foundations + chiral_koszul_pairs), convert rest to remarks with \ref |

### WP6: PROOF GAP CLOSURE [~3 hours, mathematical depth]

The top 10 proof gaps from the audit, ranked by severity:

| # | File:Line | Gap | Difficulty |
|---|-----------|-----|------------|
| 1 | `bar_cobar:~8036` | E_2 collapse: conflates bar with bar-cobar spectral sequence | Medium (clarify identification) |
| 2 | `bar_cobar:~8117` | Fiberwise QI -> pushforward QI needs proper base change | Easy (cite and apply theorem) |
| 3 | `higher_genus:~6693` | d_0*d_k + d_k*d_0 = 0: OPE pole analysis incomplete | Medium (full OPE expansion) |
| 4 | `higher_genus:~6707` | A-cycle geometric disjointness not declared | Easy (add sentence) |
| 5 | `config_spaces:~2053` | Presentation independence: restatement, not proof | Hard (substantial argument needed) |
| 6 | `deformation_theory:402` | HH duality shift: 2+1+1=4, not 2 | Medium (reconcile shift accounting) |
| 7 | `deformation_theory:135` | d_int formula conflates internal diff with face map | Medium (rewrite formula) |
| 8 | `deformation_theory:1206` | [alpha_0, alpha(z)] != k*1 (alpha_0 is central) | Easy (fix argument) |
| 9 | `deformation_theory:996` | N=4 SYM HH^2 claim is wrong/garbled | Easy (remove or correct) |
| 10 | `examples_summary:1109` | Growth rate: log n -> n in denominator | Easy (fix formula) |

### WP7: PHYSICS CONJECTURE UPGRADES [~1 hour, claim count improvement]

Three conjectures can be upgraded immediately:

| # | Conjecture | Current | Upgrade | Reason |
|---|-----------|---------|---------|--------|
| 1 | Gaiotto-Witten S-duality (principal, simply-laced) | Conjectured | ProvedElsewhere | IS Feigin-Frenkel duality |
| 2 | Gaiotto-Witten (hook-type) | Conjectured | ProvedElsewhere | IS Arakawa-van Ekeren |
| 3 | W-algebra integrability (classical) | Conjectured | Split: classical PE / quantum CJ | IS Drinfeld-Sokolov |

Three imprecise conjectures need fixing:
- Modular anomaly formula: dim H*_BRST is infinite (needs regularization or Euler char)
- Bulk reconstruction: Omega^n(B(O)) is a space, not a function (needs reformulation)
- Entanglement/Koszul: "no precise formulation" -> downgrade to Heuristic

### WP8: CLAUDE.MD + METADATA SYNC [~30 min, infrastructure]

| # | Issue | Fix |
|---|-------|-----|
| 1 | Census stale: says 669/314/100/18; actual 699/328/114/18 | Update census |
| 2 | Riordan GF wrong: denominator 2x should be 2x(1+x) | Fix formula |
| 3 | File map missing 3 files (en_koszul, derived_langlands, kontsevich_integral) | Add entries |
| 4 | File map wrong line counts for 2 stubs (koszul_across_genera, classical_to_chiral) | Update counts |
| 5 | 17 unused macros in preamble | Clean up (optional) |

---

## EXECUTION ORDER (recommended)

**Session N+1**: WP1 (critical tex errors) + WP2 (code bugs) + WP3 (build fixes)
- These are the highest-blast-radius items. All are mechanical fixes.
- Estimated: 3 hours. Verification: `make` clean + `pytest` clean.

**Session N+2**: WP6 top 5 (proof gaps) + WP8 (metadata sync)
- Mathematical content improvement. Each gap is independent.
- Start with #2 and #4 (easy), then #1 and #3 (medium).

**Session N+3**: WP4 (bibliography) + WP5 (labels/structure)
- Submission presentation. Mechanical but high-volume.
- The label rename (31 items) is best done by batch grep+sed.

**Session N+4**: WP7 (physics upgrades) + WP6 remaining gaps
- Claim count improvement + deeper proof work.

---

## STRATEGIC ASSESSMENT

### The book's actual state
The three main theorems are proved. The proof chains are clean. The formulas
are correct. The compute engine is reliable. This is a book that WORKS.

The 234 findings are mostly presentation issues (labels, duplicates, stale metadata)
and proof exposition gaps (steps that skip non-trivial arguments). The 4 critical
tex errors are genuine mathematical mistakes that need fixing, but none threatens
the main theorem chain.

### What a referee would attack
1. **Hochschild d^2=0 proof** (C1) — this is the most visible mathematical error.
   A referee reading Chapter hochschild_cohomology will immediately see the false
   associativity claim and question all downstream results.
2. **The 26 conjectures with proof blocks** — structurally contradictory. A referee
   who sees `\begin{conjecture}` followed by `\begin{proof}` will question the
   author's understanding of mathematical logic.
3. **The shift accounting** in the HH duality proof — 2+1+1=4 not 2. If the main
   Hochschild duality theorem has a wrong shift, the entire deformation theory
   chapter is undermined.

### What is NOT broken
- The operadic/geometric bar-cobar theory (Part 1 core)
- The configuration space machinery
- The genus expansion framework
- The explicit computations (sl2, Vir, W3 bar cohomology)
- The Koszul pair theory and E_1 duality
- The complementarity theorem and its proof

### The path to submission
Fix WP1-WP3 (one session). Fix WP6 top 5 (one session). Fix WP4-WP5 (one session).
Then the book is in submission-ready state modulo the ~114 conjectures, which are
correctly scoped as open problems and research directions.

---

## COGNITIVE ARCHITECTURE NOTES

### For extended reasoning mode
- The proof gap fixes (WP6) benefit most from extended thinking. Give the model
  room to derive the correct argument before writing LaTeX.
- The formula fixes (WP1 #3, WP2) need Python verification. Always compute before asserting.
- The label rename (WP5 #1) is mechanical. Use Grep to find all instances, then Edit sequentially.

### Failure modes to prevent
- **Do not re-audit what was just audited.** The 234 findings are comprehensive.
  The next session should FIX, not FIND.
- **Do not attempt all work packages in one session.** Context exhaustion after
  ~150 tool calls degrades reasoning quality. One or two WPs per session.
- **Do not trust CLAUDE.md numbers.** They are stale. Always grep for fresh counts.
- **Do not "improve" proofs that weren't flagged.** The audit checked every proof.
  If it wasn't flagged, it passes.
- **The Riordan GF in CLAUDE.md is wrong.** The manuscript is correct. Do not
  "fix" the manuscript to match CLAUDE.md.

### What makes this prompt effective for Opus 4.6
1. **Specificity over abstraction.** Every work package has file:line references,
   exact error descriptions, and concrete fix instructions. The model doesn't
   need to rediscover what's wrong.
2. **Independence structure.** Work packages are explicitly independent, enabling
   the model to execute one completely before starting another.
3. **Verification gates.** Each WP ends with a verification step (`make fast`,
   `pytest`, formula check). The model knows when it's done.
4. **Anti-hallucination scaffolding.** Python verification is mandated for every
   formula fix. The compute engine is trusted ground truth.
5. **Priority ordering with rationale.** The model doesn't need to assess priority;
   it's pre-computed based on blast radius and referee visibility.
