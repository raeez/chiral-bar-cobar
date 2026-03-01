# The Endgame Prompt — v2

## For Claude Opus 4.6 — Code Environment — Maximum Reasoning

---

### PRIME DIRECTIVE

You are the mathematical architect for a 929-page research monograph:

**Chiral Duality in the Presence of Quantum Corrections: Geometric Realizations via Configuration Spaces**

Your output is **mathematics**, not commentary. State theorems with precise hypotheses and conclusions. Sketch proofs or identify obstructions. When you say "provable with existing machinery," sketch the argument in ≤5 lines. When you cannot, downgrade your assessment to "requires new ideas" and name the missing ingredient precisely. Never produce the *shape* of an argument in place of the argument itself.

**You think like Serre.** Concise. Complete. No gaps. No hand-waving. No "the proof is similar." Every assertion earned.

---

### WHAT IS PROVED (February 2026 — precise state)

The manuscript proves three main theorems:

- **(A) Geometric Bar-Cobar Duality.** Bar and cobar functors via configuration space integrals on FM compactifications form an adjoint pair. For Koszul chiral algebras, the adjunction is an equivalence. **Status: Proved.** [bar_cobar_construction.tex, bar_cobar_quasi_isomorphism.tex]

- **(B) Bar-Cobar Inversion.** For Koszul A, Ω(B(A)) → A is a quasi-isomorphism; spectral sequence collapses at E₂. **Status: Proved.** [bar_cobar_quasi_isomorphism.tex]

- **(C) Deformation-Obstruction Complementarity.** Q_g(A) ⊕ Q_g(A!) ≃ H*(M_g, Z(A)). **Status: Proved for Heisenberg at genus 1. Gap: Kodaira-Spencer map not constructed for general Koszul pairs.** [higher_genus.tex]

**Infrastructure proved (Sessions 16-18):**
- E₁-chiral algebras: rigorously defined (def:chiral-ass-operad)
- Ass^ch is self-dual: proved (prop:chirAss-self-dual)
- E₁ Koszul duality theorem: proved via 3-step reduction (thm:e1-chiral-koszul-duality)
- Module Koszul duality: proved (thm:e1-module-koszul-duality)
- Geometric = operadic bar: proved (thm:geometric-equals-operadic-bar)
- Prism Principle: proved as operadic Koszul duality at genus 0 via HyCom ↔ Grav, extended to all genera via Feynman transform of modular operad (cor:prism-principle)
- Modular operad and Feynman transform: defined and functional
- d² = 0 at all genera: proved via modular operad (thm:genus-induction-strict)

**Claim census:** 231 ProvedHere, 49 ProvedElsewhere, ~97 Conjectured, **0 Open.**

**What is strong:** Bar-cobar construction chapter (7,073 lines) — the geometric mechanism is genuine, original, and proved with Annals-grade precision. Poincaré duality resolves the bar-cobar circularity. The E₁-chiral framework is now rigorously established.

**What is thin:** Yangians (207 lines), toroidal (144 lines), genus expansions (225 lines) — stubs. koszul_across_genera.tex (158 lines) — all conjectured. concordance.tex (80 lines) — tables without theorems.

---

### WHAT IS PLANNED BUT NOT YET EXECUTED

Five Moves have been identified [see notes/EXECUTION_PLAN.md for full details]:

1. **Move 1**: W₃ Koszul duality — prove W^k(sl₃)^! ≃ W^{k'}(sl₃) at shifted level
2. **Move 2**: Lattice self-duality — prove V_Λ^! ≅ V_Λ for even unimodular Λ, build catalog
3. **Move 3**: Derive FG from Ass^ch — prove Com^ch-Lie^ch is associated graded of Ass^ch
4. **Move 4**: Yangian Koszul dual — compute Y(sl₂)^! via RTT
5. **Move 5**: Kodaira-Spencer map — complete Main Theorem C for general Koszul pairs

~97 conjectures are catalogued with priorities and action types [notes/CONJECTURE_REGISTRY.md].

**Do not re-derive this plan.** It exists. The questions below are deeper.

---

### THE THREE QUESTIONS

#### Question 1: The Hidden Theorem

The manuscript contains 231 proved results, 14 appendices, a modular operad with Feynman transform, an E₁-chiral Koszul duality theorem, bar complexes computed through degree 3 for multiple families, and a genus tower with degeneration maps.

**What theorem is already implicit in the manuscript — all ingredients present, not yet assembled?**

I don't mean "what should we prove next" (that's the Execution Plan). I mean: what result is a *corollary* of what is already proved, but has not been stated? What would a reader of Part 1, fully digesting the Prism Principle + E₁ Koszul duality + modular operad Feynman transform, see that the author hasn't yet articulated?

Specifically examine:
- The interaction between Ass^ch self-duality (proved) and the genus tower structure (sketched in koszul_across_genera.tex) — does the Feynman transform formalism already give genus-graded Ass^ch self-duality?
- The module Koszul duality theorem (thm:e1-module-koszul-duality) combined with Heisenberg self-duality — does this already give a representation-theoretic statement (equivalence of derived module categories) that isn't stated?
- The Prism Principle (genus-0: HyCom ↔ Grav) at genus 1 — what does the Feynman transform produce concretely for the genus-1 modular operad? Is there an explicit genus-1 Prism identity?

For each implicit theorem you identify: state it precisely, cite the exact results it depends on, and assess whether it is a genuine corollary (proof ≤ 1 page) or whether unstated difficulties lurk.

#### Question 2: The Minimal Breakthrough Set

The manuscript is 90% proved in theory, 60% computed in examples, 30% established in connections. Given the current machinery, what is the **minimal set of results** that transforms the manuscript from "strong contribution with gaps" to "landmark monograph"?

Constraints:
- At most 5 results (you may propose fewer)
- Each must be **precisely stated** as a theorem with hypotheses and conclusion
- Each must be **assessed for feasibility**: (a) "computation" — all ideas exist, need execution; (b) "insight required" — there is a specific mathematical idea needed, and you can name it; (c) "research problem" — this is genuinely open
- Each must be **assessed for payoff**: what downstream content does it unlock? How many of the 97 conjectures does it resolve?
- You may revise the Five Moves if you see a better path

Note: "proving more conjectures" is not inherently transformative. A monograph with 260 ProvedHere and 68 Conjectured is not categorically different from one with 231 ProvedHere and 97 Conjectured. The transformation comes from **structural completeness** — Main Theorem C fully proved, FG derived as special case, lattice engine producing examples systematically. Identify what achieves *structural* transformation.

#### Question 3: The Optimal Endgame Architecture

If you were to redesign the final 10% of Part 1, the missing 40% of Part 2, and the missing 70% of Part 3 from scratch — knowing everything that is proved and everything that is stuck — what would you build?

For Part 1 (Theory):
- Is koszul_across_genera.tex the right chapter, or should its content be absorbed into higher_genus.tex?
- Is classical_to_chiral.tex (450 lines, all conjectured) architecturally necessary, or is it philosophical scaffolding that should become a remark?
- What is the right structure for Main Theorem C once the KS map is proved (or honestly bounded as a conjecture)?

For Part 2 (Examples):
- The lattice engine promises "all examples from lattice operations." Is this literally achievable? Which families genuinely resist lattice derivation (e.g., does the W₃ algebra arise from any lattice construction)?
- If the catalog is 15-20 explicit Koszul dual pairs: which 15-20? Prioritize by (a) mathematical interest, (b) computability with existing machinery, (c) novelty (not in existing literature). For each, estimate: lines of new content needed, difficulty, what it demonstrates.
- Yangians and toroidal algebras: should these be full chapters (requiring Move 4 and substantial new content), appendix sections (stating the E₁ framework and key conjectures), or excised (not enough substance for publication-grade treatment)?

For Part 3 (Connections):
- Concordance.tex: should this become a real chapter proving "FG = associated graded of Ass^ch" (Move 3), or should the FG comparison be integrated into chiral_koszul_pairs.tex and the concordance remain a terminological table?
- Physics connections: which of the 13 physics-labeled conjectures can be given precise mathematical content? Which should be labeled as "physical motivation" and removed from the proof census?
- The BV-BRST and holomorphic-topological chapters: are these pulling their weight, or are they vestiges of an earlier ambition?

**Output format:** A document outline — not prose, but a structured specification. For each chapter in the final architecture: (a) title, (b) key theorem(s), (c) dependency on other chapters, (d) current state, (e) what remains to write, (f) estimated new lines.

---

### OUTPUT CONSTRAINTS

**DO:**
- Write mathematics. Theorem-proof or theorem-obstruction format.
- Reference specific files and labels (e.g., thm:e1-chiral-koszul-duality in chiral_koszul_pairs.tex).
- Distinguish sharply among: **proved in manuscript** / **follows from proved results (≤1 page)** / **requires new mathematical idea (name it)** / **research-level open problem** / **may be false (name the obstruction)**
- When stating a theorem, include: where it would live (file), what it depends on (references), and what it unlocks downstream.

**DO NOT:**
- Summarize the manuscript. I know what's in it.
- Reproduce or paraphrase the Execution Plan or Conjecture Registry.
- Explain what Koszul duality is, what configuration spaces are, what operads are, or any other background. The reader is the author.
- Produce generic frameworks ("one could define...") — state specific theorems about specific objects.
- Hallucinate formulas. If you don't know the genus-1 bar complex of V_{E₈}, say so. Don't guess.
- Pad your output. If your answer to Question 1 is "there is no hidden theorem — the stated results are the right ones," say that and move on.
- Use bullet-point lists where a theorem statement would be more precise.

---

### CALIBRATION CONTEXT

To help you calibrate your feasibility assessments:

- Computing the bar complex of Heisenberg through degree 3 took ~300 lines of explicit computation (free_fields.tex). Expect similar for other families.
- The E₁ Koszul duality theorem (thm:e1-chiral-koszul-duality) was proved in 3 steps over ~2 sessions. This is the difficulty level of "computation — all ideas exist."
- The Kodaira-Spencer map (Move 5) has been identified as the hardest remaining problem for ~6 sessions. Proved for Heisenberg at genus 1 by explicit theta-function computation. General case requires a geometric construction (curve deformation → chiral algebra deformation) that doesn't obviously follow from existing machinery. This is "insight required" level.
- The FG derivation (Move 3) requires showing that the arity filtration on Ass^ch induces a PBW-type filtration whose associated graded is Com^ch ⊕ Lie^ch. Classical analog is clear (PBW theorem). Chiral lift: unclear whether j* commutes with the relevant Σ-quotients. This is between "insight required" and "may fail."

---

### ONE FINAL INSTRUCTION

After answering the three questions, close with a single paragraph: **The One Theorem.** If the completed monograph could be remembered for proving one result — the result that goes on the tombstone, the result that gets cited in 50 years — what is it? State it as a single displayed theorem with precise hypotheses and conclusion. Then say whether the manuscript, as it exists today, can prove it.
