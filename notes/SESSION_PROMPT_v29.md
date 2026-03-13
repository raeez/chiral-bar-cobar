> **Historical prompt note (March 13, 2026).**
> This file is retained for provenance and should not be treated as a live control document.
> Active doctrine is `notes/SESSION_PROMPT_v23.md` together with `notes/autonomous_state.md`, `notes/VISION.md`, `notes/PROGRAMMES.md`, and `chapters/connections/concordance.tex`.
> Current constitutional status: MC1/MC2 resolved on the printed loci; live frontier MC3/MC4; MC5 downstream; periodicity orthogonal.

# SESSION PROMPT v29 — The Chriss-Ginzburg Rewrite Forge
# Launch: "Read notes/SESSION_PROMPT_v29.md and execute it."
# Date: March 2026

---

## COGNITIVE CONTRACT

You are rewriting a 1742-page mathematics monograph and its 160-page companion volume into their Platonic ideal form. The monograph sits at the triple intersection of pure mathematics (Serre/Grothendieck/Beilinson-Drinfeld), mathematical physics (Witten/Costello), and physics (Polyakov/Dirac). Your target: Annals/Astérisque grade prose of the kind found in Chriss-Ginzburg's *Representation Theory and Complex Geometry* — where every sentence carries structural weight, every definition serves a theorem that serves a geometric picture, and the reader feels a single unified mechanism unfolding rather than a sequence of independent results.

**Volumes:**
- **Volume I** (~1742pp, ~/chiral-bar-cobar): *Modular Homotopy Theory for Factorization Algebras on Curves. Volume 1: Modular Koszul Duality*
- **Volume II** (~160pp, ~/ainfinity-chiral-hochschild-cohomology-3d-qft): *A∞ Chiral Algebras and Chiral Hochschild Cohomology in 3D HT QFT*

### The Rewrite Imperative

The manuscript is structurally complete. The theorems are stated, the proofs are written, the examples are computed. But prose that was written incrementally across many sessions — built up layer by layer, conjecture promoted to theorem, scope qualifiers inserted post-hoc, computations appended as they were verified — reads like geological strata rather than a designed cathedral. Your task is to rewrite each section so it reads as if it were written in one sitting by a mathematician who already knew the final theorem and designed the exposition to make the reader feel the inevitability of the result before seeing its proof.

**Do not assume the mathematics is correct.** Every `\ClaimStatusProvedHere` is an aspiration until you have read the proof and verified each step follows from its premises. The labels express the dream of what the theorem is meant to be. Your rewrite is the act of earning each label: you read, you verify, you rewrite so the proof is airtight and the exposition makes the mechanism transparent. When you find a gap, you close it or flag it with a precise `% REWRITE-GAP:` comment. When you find a soft spot, you harden it. When you find loose prose, you forge it into Chriss-Ginzburg steel.

### The Cardinal Rule of This Session

**You are REWRITING, not adding.** Every edit replaces existing material with a better version. You do not add new sections, new theorems, new conjectures, or new definitions. You do not change the theorem architecture. You rewrite what exists so it reads as if it were always this good. The page count should stay roughly constant or decrease. The information density should increase. The mathematical precision should increase. The aesthetic quality should increase. All three simultaneously.

---

## THE CHRISS-GINZBURG STANDARD

What makes Chriss-Ginzburg the target:

1. **Mechanism before formalism.** Every chapter opens by naming the geometric mechanism at work, in one sentence. The formalism then unpacks the mechanism. The reader always knows *why* before they see *what*.

2. **Definitions that serve theorems.** No definition stands alone. Each is introduced because a specific theorem needs it, and the definition is stated in the form that makes the theorem most transparent. Definitions are sharp, minimal, and immediately followed by the first result that needs them.

3. **Proofs that reveal structure.** A proof is not a verification ritual — it is the exposition of the mechanism by which the theorem becomes true. Each step of a proof should feel like the only possible next step. When a proof has multiple cases or ingredients, the architecture of the proof (why these cases, why this order) is transparent.

4. **Remarks that illuminate connections.** A remark connects the current theorem to something the reader already knows, or names a structural principle that will recur. Remarks are never padding. A remark that says "this is related to X" without explaining how is worse than no remark.

5. **Examples that are portraits.** An example is not a drill — it is a portrait of the theory in a specific setting, showing features that are invisible in generality. The reader should learn something from the example that they could not learn from the theorem statement alone.

6. **Cross-references that teach.** A reference to another part of the text is not a bureaucratic pointer — it names what the reader will find there and why it matters here.

7. **No wasted sentences.** Every sentence advances understanding. Sentences that restate what was just said, that hedge without precision, that defer to future sections without naming what will be found there, that use three words where one would do — all are cut.

8. **The feeling of unity.** The reader finishes a chapter and feels that they have seen one mechanism from multiple angles, not a collection of loosely related results. This feeling is achieved not by asserting unity but by making the structural connections visible at every turn.

---

## EXECUTION PROTOCOL

### Phase 0: Orientation (do this ONCE, ≤30 minutes)

Build your map. Do NOT attempt to hold the entire manuscript in context. Instead:

1. Read `CLAUDE.md` — this is your invariant reference. The Mathematical Invariants section is sacred; these are verified facts. Getting any of them wrong corrupts the manuscript.
2. Read `chapters/connections/concordance.tex` — this is the constitution. When earlier chapters disagree with concordance, concordance is right.
3. Run `make fast` to verify the build compiles.
4. Run `cd compute && .venv/bin/python -m pytest tests/ -q` to verify tests pass.
5. Read the git diff (`git diff` for unstaged) to understand what work is in-flight.

You now have the map. Begin Phase 1.

### Phase 1: The Strike List (≤2 hours)

Produce a comprehensive, file-by-file audit of rewrite targets. Work through chapters systematically. For EACH .tex file:

1. Read the file (or the first 300 lines if very large, then sample interior and end).
2. Identify rewrite sites using the taxonomy below.
3. Record each site as a one-line entry: `FILE:LINE — CATEGORY — brief description`.

**Rewrite Site Taxonomy** (ordered by severity):

| Category | Code | Description | Rewrite Action |
|----------|------|-------------|---------------|
| Mathematical gap | G | Proof step that doesn't follow from premises; missing hypothesis; incorrect formula | Close the gap or insert `% REWRITE-GAP:` |
| Loose amalgamation | L | Multiple paragraphs/remarks that discuss related ideas without synthesis | Fuse into one coherent passage with a single governing thread |
| Dead prose | D | Sentences that restate, hedge, defer, or pad | Cut or compress to essential content |
| Mechanism-blind | M | Formalism presented without naming the geometric mechanism behind it | Prepend the mechanism sentence; restructure to serve it |
| Orphan definition | O | Definition not immediately connected to the theorem it serves | Move or reframe to serve its theorem |
| Proof architecture | P | Proof whose structure (case order, ingredient sequence) is opaque | Restructure so the proof architecture is transparent |
| Remark vacuum | R | Remark that names a connection without explaining it | Either explain the connection or delete the remark |
| Example as drill | E | Example presented as calculation without portrait quality | Rewrite to show what the theory looks like in this case |
| Cross-reference as bureaucracy | X | Reference that doesn't say what the reader will find | Add the illuminating clause |
| Stale qualifier | S | Scope qualifier or status remark that's out of date | Update to match concordance.tex |

Aim for **200+ sites** across the manuscript. When you see a tight, well-forged section (the nilpotence-periodicity correspondence, the Heisenberg frame chapter, the best parts of the bar-cobar core), note it as `EXEMPLARY` and move on — those are the standard the rest must match.

Save the strike list as `notes/REWRITE_STRIKE_LIST_v29.md`.

### Phase 2: Execution (the main phase — iterate until done)

Work through the strike list in chapters, one chapter at a time, front to back through the book. For each chapter:

1. **Read the full chapter** (or read it in 400-line blocks for very large chapters).
2. **Execute all rewrite sites in that chapter**, making edits with the Edit tool.
3. **After each chapter**: run `make fast` to verify compilation. Fix any errors immediately.
4. **Commit nothing.** Leave all changes unstaged. The author will review the full diff.

**Execution tempo**: Do NOT attempt to rewrite an entire large chapter in one pass. Work in blocks of 5-10 sites, verify compilation, then continue. This prevents accumulation of cascading errors.

**Execution depth**: Each rewrite should be **substantive**, not cosmetic. A rewrite of a loose amalgamation means restructuring 10-30 lines into a new paragraph with a governing sentence and a clear logical arc. A rewrite of a mechanism-blind passage means reading the proof, understanding the geometric picture, and prepending the mechanism sentence. A rewrite of a dead prose passage means cutting it to 30-50% of its current length while preserving all mathematical content.

### Phase 3: Verification (after each batch of chapters)

1. Run `make fast` — must compile with 0 errors, 0 undefined refs.
2. Run `cd compute && .venv/bin/python -m pytest tests/ -q` — must pass.
3. Spot-check 3-5 rewrites by re-reading the result and verifying it's an improvement.

---

## ANTI-PATTERNS (failure modes to avoid)

1. **The cosmetic trap.** Changing "we note that" to "note that" is not a rewrite. Swapping synonyms, reordering unchanged sentences, adding adverbs — these are cosmetic. A real rewrite changes the logical structure of the passage.

2. **The commentary trap.** Adding a sentence that says "this is important because..." without changing the underlying passage. If you need to explain why something matters, rewrite the passage so the importance is self-evident.

3. **The expansion trap.** Making a passage longer. Almost every rewrite should make the passage shorter or the same length with higher information density. The only exception is closing a mathematical gap, which may require adding proof steps.

4. **The hallucination trap.** Inventing mathematical content. Every formula you write must be derivable from the existing content, the CLAUDE.md invariants, or standard references. If you're unsure whether a formula is correct, DO NOT WRITE IT. Insert `% REWRITE-GAP: [precise description of what's needed]` instead.

5. **The uniformity trap.** Rewriting every passage to the same length and rhythm. Good mathematical prose has texture — a crisp definition, a discursive remark, a terse proof, a rich example. Match the style to the content.

6. **The scope-creep trap.** Adding new theorems, new definitions, new conjectures, new sections. You are rewriting, not extending. The theorem architecture is fixed. If you discover that a new theorem is needed to close a gap, flag it with `% REWRITE-GAP:` and move on.

7. **The context-window trap.** Trying to hold too much in memory at once. Work chapter by chapter, block by block. Re-read the relevant section of CLAUDE.md invariants before editing any section that involves formulas from the Critical Pitfalls list.

8. **The deference trap.** Leaving a passage unchanged because it was written by the author. Every passage is a candidate for rewrite. The author wants to see a heatmap that tiles the book.

---

## CHAPTER PRIORITY ORDER

Work front-to-back through the book, but weight your time toward Part II (Examples), which is half the book and where the most loose amalgamations live:

**Part I — Theory** (chapters/theory/):
1. `introduction.tex` — governing question, double-frame narrative
2. `algebraic_foundations.tex` — operadic prerequisites
3. `bar_cobar_construction.tex` — THE core chapter
4. `chiral_koszul_pairs.tex` — Koszul pair structure
5. `koszul_pair_structure.tex` — detailed pair theory
6. `configuration_spaces.tex` — FM compactifications
7. `higher_genus.tex` — modular face of the theory
8. `chiral_modules.tex` — module bar-cobar
9. `deformation_theory.tex` — deformation-obstruction
10. `poincare_duality.tex`, `poincare_duality_quantum.tex` — NAP duality
11. `hochschild_cohomology.tex` — Theorem H
12. `en_koszul_duality.tex` — E_n generalization
13. `derived_langlands.tex` — Langlands connections

**Part II — Examples** (chapters/examples/) [**HEAVIEST REWRITE TERRITORY**]:
14. `lattice_foundations.tex` — lattice VOAs
15. `free_fields.tex` — free field families
16. `beta_gamma.tex` — beta-gamma system
17. `heisenberg_eisenstein.tex` — Heisenberg-Eisenstein
18. `kac_moody_framework.tex` — KM framework
19. `w_algebras_framework.tex` — W-algebra overview
20. `w3_composite_fields.tex` — W₃ composites
21. `w_algebras_deep.tex` — deep W-algebra theory
22. `yangians.tex` — Yangian DK square
23. `toroidal_elliptic.tex` — toroidal/elliptic extensions
24. `deformation_quantization.tex` — deformation quantization examples
25. `deformation_examples.tex` — further deformation examples
26. `genus_expansions.tex` — explicit genus computations
27. `detailed_computations.tex` — extended computations
28. `examples_summary.tex` — master summary table
29. `minimal_model_fusion.tex`, `minimal_model_examples.tex` — fusion rules

**Part III — Connections** (chapters/connections/):
30. `concordance.tex` — constitution (REWRITE WITH EXTREME CARE)
31. `feynman_diagrams.tex` — Feynman graph complex
32. `holomorphic_topological.tex` — HT QFT bridge
33. `bv_brst.tex` — BV/BRST identification
34. `physical_origins.tex` — physics connections
35. `kontsevich_integral.tex` — Kontsevich integral

**Frame** (chapters/frame/):
36. `heisenberg_frame.tex` — entry atom

**Volume II** (~/ainfinity-chiral-hochschild-cohomology-3d-qft):
37-46. All chapters, with special attention to the five cross-volume bridges (bar-cobar, Hochschild, DK/YBE, BRST=bar, (H1)-(H4))

---

## THE QUALITY TEST

After each chapter rewrite, ask yourself: if a reader opened this chapter with no prior context (but the book's own definitions), would they feel the inevitability of the main result? Would they understand the geometric mechanism before seeing the formal proof? Would they finish the chapter feeling they had seen one coherent picture rather than a sequence of lemmas?

If the answer is no, keep rewriting.

---

## MATHEMATICAL INVARIANTS — GROUND TRUTH

Before rewriting ANY section involving formulas, re-read the relevant subsection of the Critical Pitfalls in CLAUDE.md. These are the verified facts of the theory. Violating any of them corrupts the manuscript. The most commonly needed:

- **Grading**: COHOMOLOGICAL, |d| = +1. Bar uses DESUSPENSION.
- **Koszul duals**: Com^! = Lie (NOT coLie). Heisenberg NOT self-dual.
- **Sugawara**: T = (1/2(k+h^∨))∑:J^a J^a:, c = k·dim(g)/(k+h^∨)
- **Feigin-Frenkel**: k ↔ −k−2h^∨ (NOT −k−h^∨)
- **Curved A-infinity**: m₁²(a) = m₂(m₀,a) − m₂(a,m₀) = [m₀,a] (MINUS sign)
- **FM**: C̄_n(X) = blowup, NOT X^n \ Δ
- **Prime form**: E(z,w) ∈ K^{−1/2} ⊠ K^{−1/2}
- **QME**: ℏΔS + (1/2){S,S} = 0 (factor 1/2)
- **HCS**: coefficient 2/3, not 1/3
- **W₃ composite**: Λ = :TT: − (3/10)∂²T (MINUS sign)

---

## WHAT SUCCESS LOOKS LIKE

When you are done, the git diff should show:
- **200+ edit sites** distributed across 35+ files
- **Every chapter touched** — no chapter left unexamined
- **Net line count roughly constant** — rewrites compress as much as they expand
- **Zero compilation errors, zero test failures**
- **A heatmap that tiles the book**: not sparse edits at obvious soft spots, but a dense distribution of improvements that together raise the entire manuscript to Chriss-Ginzburg standard

The manuscript should read, on every page, as if written by a mathematician who has already seen the complete theory and is presenting it with the calm certainty of someone who knows exactly where every piece fits.

---

## BEGIN

Read `CLAUDE.md`. Read `concordance.tex`. Build. Test. Then produce the strike list.
