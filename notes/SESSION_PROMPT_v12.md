# SESSION PROMPT v12 — The Chriss-Ginzburg Restructuring

## What you are doing

You are restructuring a 1276-page mathematics monograph on chiral Koszul duality. The manuscript has 695 proved theorems, 113 conjectures, and a complete technical core. The *mathematics* is done. What remains is the *delivery*: the manuscript currently presents Theory → Examples → Connections, but its natural form — the form that makes the content inevitable rather than impressive — is the Chriss-Ginzburg inversion: **Example → Theory → Synthesis**.

Read `raeeznotes.md` for the author's vision of what the book yearns to become. Read `notes/VISION.md` for the four irreducible pieces and the theorematic silhouette. These are your north stars.

## The Chriss-Ginzburg method, precisely stated

In *Representation Theory and Complex Geometry*, Chriss and Ginzburg open with Chapter 1: the sl₂ Springer resolution. In 50 pages, every theme of the 500-page book appears in a single example — the moment map, the Weyl group action on cohomology, the Springer fiber, the convolution algebra, Kazhdan-Lusztig polynomials. Chapters 2-8 then develop the general theory. But the reader already *knows* what they're generalizing. The effect is not pedagogy — it is **inevitability**. You never ask "why are we doing this?" because you saw the answer before the question was posed.

The method has five structural principles:

1. **The Frame Example**: One example, chosen because it is the *simplest object carrying the full structure*, opens the book and previews every major theorem in concrete form. In CG, this is sl₂. In your manuscript, this is the **Heisenberg algebra** — the simplest chiral algebra where all four irreducible pieces (Arnold d²=0, Verdier duality, genus-1 curvature, clutching tower with A-hat genus) are simultaneously visible.

2. **Show, Don't Tell**: Definitions emerge from computations, not the reverse. CG defines the moment map *after* computing it for T*P¹. Your manuscript should define the bar complex *after* building it explicitly for Heisenberg — the reader sees η₁₂ = d log(z₁-z₂), watches the residue extract the OPE, watches Arnold force d²=0, and *then* receives the abstract definition.

3. **Inevitability Over Generality**: Each generalization step is motivated by a concrete failure of the previous level. CG doesn't say "now we generalize to reductive groups" — they show what breaks for sl₃ that worked for sl₂, and the general theory is the repair. Your manuscript should show what breaks when you pass from Heisenberg (abelian, rank 1) to sl₂-hat (non-abelian), from genus 0 to genus 1, from E∞ to E₁.

4. **Synthesis as Narrative Cadence**: Disparate mathematical domains (algebra, geometry, representation theory) are not presented in parallel tracks — they converge on the same object from different directions, and the reader experiences the convergence. In your manuscript: the bar differential is simultaneously an algebraic boundary map, a geometric residue on FM compactifications, and a physical OPE fusion. These three descriptions should *collide* in the text, not be presented in separate chapters.

5. **Sophistication in Selection, Not in Apparatus**: CG's sophistication lies in *what they choose to compute*, not in the machinery they deploy. The right example, computed completely, teaches more than a general theorem stated abstractly. Your manuscript's Master Table of invariants, the shared discriminant (1-3x)(1+x), the A-hat genus appearance — these are the CG moments. They should be *encountered* through computation, not announced in an introduction.

## The Restructuring Plan

### Phase 0: Architectural Design (THINK BEFORE ACTING)

Before editing any .tex file, produce a complete restructuring plan as a document `notes/CG_RESTRUCTURING_PLAN.md`. This plan must contain:

(a) **The new chapter order** — every .tex file assigned to its new position, with a one-sentence description of its new role. The current 55 files will not all survive as independent chapters; some will merge, some will be absorbed, a few may split.

(b) **The Heisenberg Frame Chapter** — a detailed outline (section by section, 15-20 sections) of the opening chapter. This chapter must preview:
   - The bar complex via explicit computation (η₁₂, residues, Arnold)
   - Koszul duality (H^! = Sym^ch(V*)) via the computation, not by fiat
   - The genus-0 bar-cobar adjunction in action
   - The genus-1 curvature d² = κ·ω₁ emerging from the elliptic propagator
   - The coderived category necessity (why ordinary derived fails)
   - The genus tower and the A-hat genus formula
   - The complementarity theorem Q_g(H) + Q_g(H!) = H*(M_g, Z(H))
   - The modular characteristic package (Θ_A, H_A, Δ_A) in concrete form
   - A preview of what happens for sl₂-hat (non-abelian generalization)
   - A preview of what happens for Yangian (E₁ generalization)

(c) **The transition map** — for each theorem currently in the manuscript, its new location and any changes to its proof or statement required by the restructuring.

(d) **Part structure** — the new Part divisions with their narrative roles. Consider:
   - Part 0: The Heisenberg algebra (the frame chapter, ~80 pages)
   - Part I: The general theory (developed as *inevitable generalization* of Part 0)
   - Part II: The full menagerie (each example computed completely, CG-style)
   - Part III: The frontier (physics connections, open programmes, modular silhouette)

(e) **What does NOT change** — identify all content that stays exactly where it is. Theorem statements, proofs, and computations are *mathematical facts* — they don't change. What changes is their *order*, their *framing*, and the *connective tissue* between them.

### Phase 1: The Heisenberg Frame Chapter

This is the centerpiece of the restructuring. Write it as a new chapter file `chapters/frame/heisenberg_frame.tex`. It is ~80 pages of self-contained mathematics that:

- Opens with the Heisenberg OPE J(z)J(w) = k/(z-w)² — no preamble, no motivation, just the algebra
- Builds the bar complex by hand: n=2, n=3, n=4, showing every sign, every residue
- Derives d²=0 from Arnold (not as a theorem to prove, but as a computation that *happens*)
- Identifies the Koszul dual Sym^ch(V*) by reading it off the bar cohomology
- Constructs the cobar and verifies Ω(B(H)) → H
- Passes to genus 1: writes the elliptic propagator, computes d², watches curvature appear
- Shows why the ordinary derived category cannot see the curvature (Positselski's insight)
- Computes the genus generating function term by term (g=1,2,3) and recognizes A-hat
- States the three main theorems as *observations about this example*
- Identifies what is special about Heisenberg (abelian, rank 1, d_bracket²=0 by commutativity) and what will break for sl₂-hat (non-abelian, bracket contributes, spectral sequence needed)
- Closes with the modular characteristic package as the *natural envelope* of everything computed

**Source material**: Draw from `chapters/examples/free_fields.tex` (Heisenberg sections), `chapters/examples/heisenberg_eisenstein.tex`, `chapters/theory/bar_cobar_construction.tex` (Heisenberg examples), `chapters/theory/higher_genus.tex` (genus tower). The mathematics is already written — you are *resequencing and reframing*, not inventing.

**Style constraints**:
- No sentence of the form "We now prove..." or "The following theorem shows..." — CG never announces what it's about to do. It does it.
- Definitions appear *after* the object has been constructed in the example. The general definition is a recognition: "The construction we have just performed for the Heisenberg algebra is an instance of a general pattern."
- Proofs for this example should be *complete computations*, not appeals to general theory. The reader should be able to verify every step with pencil and paper.
- Cross-references to later chapters should be forward-looking: "We will see in Chapter N that this phenomenon persists for all Kac-Moody algebras, with the Chevalley-Eilenberg complex replacing the symmetric coalgebra."

### Phase 2: Reframe Part I (Theory)

The theory chapters (algebraic_foundations through quantum_corrections) remain largely intact in content, but their *introductions* and *motivations* change. Each chapter now opens by saying "In the Heisenberg frame chapter, we saw X. We now establish X in full generality."

Specifically:
- `algebraic_foundations.tex`: Opens with "The bar-cobar adjunction we computed for Heisenberg extends to all augmented chiral algebras..."
- `configuration_spaces.tex`: Opens with "The logarithmic forms η₁₂ that served as propagators for Heisenberg live naturally on Fulton-MacPherson compactifications..."
- `bar_cobar_construction.tex`: Opens with "The three-step differential d = d_internal + d_residue + d_deRham that we built by hand now receives its general formulation..."
- `higher_genus.tex`: Opens with "The genus-1 curvature κ·ω₁ and the A-hat genus tower that we computed for Heisenberg are universal..."

Each chapter introduction should be 1-2 paragraphs, not the current multi-page preambles. The preamble work is done by the frame chapter. The theory chapters are now *clean, efficient, inevitable generalizations*.

### Phase 3: Reframe Part II (Examples)

The examples chapters become **complete portraits** in the CG style. Each chapter computes ONE family completely: Koszul dual, bar cohomology, spectral sequence, genus tower, discriminant, complementarity. The chapter titles should name the algebra, not the technique:

- "The Heisenberg algebra" (already done in frame chapter — this becomes a reference back)
- "Free fermions and the collapse regime"
- "The βγ/bc systems and the shared discriminant"
- "Affine Kac-Moody algebras: Feigin-Frenkel as Koszul duality"
- "The Virasoro algebra and the bosonic string"
- "W-algebras and the Drinfeld-Sokolov hierarchy"
- "Yangians and the E₁-chiral world"
- "Genus expansions: the three theorems in action"

Each portrait follows the same cadence: OPE → bar → dual → curvature → genus tower → discriminant → what's new here that wasn't in the previous example. The reader accumulates invariants through *computation*, building toward the Master Table as a *summary* of what they've seen, not a declaration of what they'll see.

### Phase 4: Reframe Part III (Connections)

Part III becomes the book's *horizon*: where the machinery, having been built and tested, reaches toward physics and open mathematics. The current Connections chapters (Feynman diagrams, BV-BRST, holomorphic-topological, concordance) are already well-suited for this role. The main change: the concordance chapter becomes the book's *epilogue*, stating the modular Koszul programme (from raeeznotes.md §XI) as the natural continuation, with the five-theorem silhouette (A_mod, B_mod, C_mod, Index, DK) as the formal target.

### Phase 5: Rewrite the Introduction

The current `introduction.tex` (1569 lines) is a comprehensive overview written before the restructuring. After Phases 1-4, it becomes much shorter — perhaps 10-15 pages — because the frame chapter does the heavy lifting. The introduction now:
- States the problem in one paragraph (Koszul duality on curves)
- States the three theorems in one paragraph each
- States the central thesis (quantum corrections = modular completion) in one paragraph
- Gives the Leitfaden (reading guide) with the new chapter order
- That's it. No definitions, no examples, no extended motivation. The frame chapter provides all of that.

## Execution Constraints

1. **Never delete proved mathematics.** Every theorem, lemma, proposition, and computation in the current manuscript is a verified mathematical fact. You may move it, reframe it, change its introduction, but you may not alter its statement or proof.

2. **Compile after every phase.** Run `make fast` after each phase to verify zero LaTeX errors. The manuscript must compile at every intermediate stage.

3. **Track all moves.** Maintain a running log in `notes/CG_RESTRUCTURING_LOG.md` recording every file moved, every section relocated, every introduction rewritten. This is your audit trail.

4. **Parallel decomposition.** Phases 1-4 are largely independent after the plan (Phase 0) is complete. Use subagents for independent chapter rewrites within each phase.

5. **The 80% rule.** The restructuring is successful if a mathematician reading the Heisenberg frame chapter says "I understand what this book is about" and a mathematician reading the introduction of any later chapter says "I see why we need this generalization." If those two conditions are met, the details will follow.

6. **Preserve the triple intersection.** The manuscript operates at math × math-physics × physics. The CG restructuring elevates the *mathematical* delivery but must not suppress the physical interpretations. In the Heisenberg frame chapter, the bar complex is simultaneously the algebraic bar construction, the geometric residue calculus, and the physical OPE fusion. All three are present in CG style: shown, not told.

## What Success Looks Like

A referee opens the manuscript. Chapter 1 is "The Heisenberg Algebra." In 80 pages, they see the bar complex built by hand, watch d²=0 emerge from Arnold, see the Koszul dual appear from the computation, watch curvature appear at genus 1, recognize the A-hat genus in the generating function, and understand — concretely, through one example — what modular Koszul duality is. They turn to Chapter 2 (Algebraic Foundations) and think: "Yes, of course — the bar-cobar adjunction I just saw needs to be formalized." They turn to Chapter 5 (Higher Genus) and think: "Yes, of course — the curvature I computed for Heisenberg needs to be controlled in general." They turn to Part II and think: "Now show me sl₂-hat." They reach the Master Table and think: "I already knew most of this from the examples."

The book reads as a single sustained argument, not as a collection of results. The mathematics speaks. The structure is invisible. The content is inevitable.

That is the Chriss-Ginzburg method applied to chiral bar-cobar duality.

## Begin

Start with Phase 0. Read `raeeznotes.md`, `notes/VISION.md`, and the current chapter files. Produce `notes/CG_RESTRUCTURING_PLAN.md`. Do not edit any .tex file until the plan is complete and reviewed.
