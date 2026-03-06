# DEEP CRITIQUE v2 — Mathematical Referee Report
# Date: March 6, 2026 | Session 125
# Census: PH 676 / PE 310 / CJ 100 / H 18 = 1104
# Pages: 1217 | Build: clean

---

## Executive Summary

The monograph proves three substantial theorems about chiral Koszul duality via configuration space integrals, establishes a computational framework that produces verifiable invariants (the shared discriminant, the genus universality formula, the complementarity sums), and carries out explicit computations for ~10 families of chiral algebras. The theoretical apparatus is sound and complete at the algebra level.

The central deficiency is **representation-theoretic thinness**: the book defines module Koszul duality functors, BGG resolutions, module categories, and genus-graded modules in full generality, but applies them to only one algebra (sl₂) producing only one non-trivial result (the BGG pipeline, which recovers a classical resolution by a new method). The ratio of abstract module machinery to concrete module computation is approximately 28:15, and most of the 15 "concrete" results are either tautological (free modules map to free modules) or recover classical results (Verlinde formula, Weyl-Kac character).

The second deficiency is **narrative inconsistency**: the voice varies between chapters (pedagogical in higher_genus, computational in free_fields, manifesto-like in bv_brst), and dead prose accumulates in the form of redundant remarks that restate what proofs have just shown.

The third deficiency is **incomplete proof sketches**: F4a and F4b in bar_cobar_construction.tex retain circular reasoning in their sketch bodies despite having been annotated with forward pointers.

---

## Findings

### C1: The Module Theory Deficit
Severity: CRITICAL
Location: chiral_modules.tex (entire), kac_moody_framework.tex, yangians.tex
The gap: 28 abstract module theorems vs 15 concrete computations. Of the 15, most are shallow:
- prop:vacuum-verma-koszul says "free modules map to free modules" (Φ(M(0)_k) ≃ M(0)_{-k-4})
- ex:fusion-bar-sl2 computes fusion at level 2, where the category is semisimple (Ext = 0 trivially)
- thm:yangian-bgg reduces to the classical CE complex
The book never computes:
- Ext¹ between modules in a non-semisimple category via bar complex
- The bar resolution of a non-vacuum Verma module (e.g., M(λ) for sl₂ at generic λ)
- A character of an admissible module via the bar spectral sequence
- Any module computation for sl₃ or beyond (BGG pipeline stops at sl₂)
What depth demands: Explicit computation of Φ applied to M(λ) for sl₂ at generic k, with the output identified as a named module of sl₂_{-k-4}. Explicit Ext¹ between admissible modules at fractional level. sl₃ BGG pipeline.
Remedy: Target M2 from the prompt — compute Φ on non-vacuum modules. Scale: 5-8 pages.
Priority: 1

### C2: The Springer Candidate Is Underexploited
Severity: MAJOR
Location: examples_summary.tex:509 (thm:ds-bar-gf-discriminant), genus_expansions.tex
The gap: The shared discriminant Δ = (1−3x)(1+x) is the book's strongest "Springer moment" — a concrete, falsifiable discovery that retroactively justifies the entire apparatus. It is proved and explained (via DS and Wakimoto). But it is not developed to its full potential:
- The monodromy interpretation (Δ(x) = det(1 − x·T) for Kodaira-Spencer operator T) is a remark, not a theorem
- The sl₃/W₃ discriminant prediction (1−3x−x²) is stated but not proved
- The Q(x)-linear dependence (thm:discriminant-linear-dependence) is proved but not interpreted representation-theoretically
What depth demands: Prove the spectral interpretation of Δ, or formulate it as a precise conjecture with evidence. Prove the sl₃ discriminant prediction, or at least verify it numerically through one more degree.
Remedy: Target M3. Scale: 3-5 pages.
Priority: 2

### C3: Proof Sketch Residues in bar_cobar_construction.tex
Severity: MAJOR
Location: bar_cobar_construction.tex lines ~4600 (F4a), ~4625 (F4b)
The gap: Two proof sketches retain circular reasoning in their bodies:
- F4a (lem:obstruction-class): "d_g² must land in the center by the Jacobi identity" — but centrality is what needs proving. Annotation says "see Theorem X for full proof" but the sketch itself is wrong.
- F4b (lem:period-integral): "By relative Stokes' theorem" without verifying hypotheses of Stokes.
Both are annotated with forward pointers to the full proofs elsewhere, but a referee reading linearly will encounter the circular/incomplete sketches first.
What depth demands: Either complete the sketches or replace them with clean forward references without the misleading argument bodies.
Remedy: Rewrite both lemma proofs as 2-3 sentence arguments that cite the full proof without reproducing the circular reasoning. Scale: 0.5 pages.
Priority: 1 (small effort, prevents referee damage)

### C4: Voice Inconsistency and Dead Prose
Severity: AESTHETIC
Location: scattered (higher_genus.tex, bv_brst.tex, free_fields.tex)
The gap: Three specific issues:
(a) bv_brst.tex line 5: "on the nose" — violates the style convention in CLAUDE.md ("strict" not "on-nose")
(b) higher_genus.tex lines 243-264: Two consecutive remarks (Physical interpretation, Connection to Feynman diagrams) restate the same heuristic A∞/Feynman correspondence in different words. Delete one.
(c) bv_brst.tex lines 146-153: Scope remark containing "The synthesis — identifying the QME as the functorial expression of bar-cobar Verdier compatibility — is new to this work." This is self-advertisement. The theorem proves it; the remark should not claim novelty.
(d) Introduction: "The deepest insight is this:" announces rather than reveals. Pattern "this is not an analogy" repeated 3+ times.
What depth demands: Uniform voice (free_fields.tex is the model). Dead prose eliminated. Mathematics speaks for itself.
Remedy: Targeted edits. Scale: 1 hour.
Priority: 2

### C5: Motzkin Combinatorics Are Numerical, Not Structural
Severity: STRUCTURAL
Location: examples_summary.tex (bar dimension table), free_fields.tex (Virasoro bar)
The gap: The Virasoro bar cohomology dimensions are Motzkin differences M(n+1)−M(n). This is stated as a numerical observation. There is no bijection between Motzkin paths and a natural basis of the bar cohomology. No combinatorial model is constructed.
What depth demands: Even a conjectural combinatorial model (e.g., cells of a CW decomposition of the bar complex indexed by non-crossing chord diagrams) would transform this from a numerical curiosity into structural mathematics.
Remedy: Target M4. Scale: 4-6 pages. May be partially achievable as a precise conjecture with evidence.
Priority: 3

### C6: Genus-Graded Module Theory Is Empty
Severity: MAJOR
Location: chiral_modules.tex:4205-4341
The gap: The genus-graded modules section (def:genus-graded-module, thm:module-genus-tower, prop:genus-module-koszul) contains one decorative example (ex:verma-genus-graded) that "describes" the genus-graded Verma tower in words but computes nothing: no dimensions, no chain complexes, no character corrections.
What depth demands: At minimum, compute dim of the genus-1 layer of the genus-graded Verma module for sl₂. This involves the elliptic bar complex at the module level.
Remedy: One explicit computation filling the genus-graded example. Scale: 2-3 pages.
Priority: 2

### C7: Chapter Ordering Serves the Mathematics
Severity: STRUCTURAL
Location: Table of contents
Finding: The Theory/Examples/Connections partition is effective. The chapter ordering within Part 1 is logical (foundations → bar-cobar → Poincaré → higher genus → Koszul pairs → modules → deformation). The METAMORPHOSIS transforms have improved all chapter openings to GOOD or EXCELLENT.
The one weakness: chiral_koszul_pairs.tex opens with 40 lines of historical survey before reaching chiral content. This delays momentum.
Remedy: Compress the historical survey to 5-10 lines. Scale: 15 minutes.
Priority: 3

### C8: Introduction Dead Prose
Severity: AESTHETIC
Location: introduction.tex
Finding: Six passages of dead prose identified:
(a) "This structural viewpoint explains why the explicit computations of Part 2 cohere." — meta-commentary
(b) "The remaining sections of this introduction develop the tools..." — navigation that duplicates ToC
(c) "The identification of algebraic structure constants with geometric residues underlies the entire construction." — restates what the formula shows
(d) "providing both conceptual clarity and computational power." — advertising
(e,f) "These are not three analogies but three projections" appears twice in near-identical form on consecutive pages
Plus: "The deepest insight is this:" announces depth instead of revealing it. Replace with neutral transition.
Remedy: Delete or rewrite each passage. Scale: 30 minutes.
Priority: 2

---

## Priority Ranking (IMPACT × FEASIBILITY)

| Rank | Finding | Impact | Feasibility | Target |
|------|---------|--------|-------------|--------|
| 1 | C1: Module theory deficit | 10 | 7 | M2: Explicit Φ on non-vacuum modules |
| 2 | C3: Proof sketch residues | 8 | 10 | Fix F4a, F4b |
| 3 | C4: Voice/dead prose | 6 | 9 | Targeted edits |
| 4 | C8: Introduction dead prose | 5 | 10 | Delete/rewrite 6 passages |
| 5 | C2: Discriminant underexploited | 8 | 5 | M3: Spectral interpretation |
| 6 | C6: Genus-graded modules empty | 7 | 5 | Fill one example |
| 7 | C5: Motzkin combinatorics | 6 | 4 | M4: Combinatorial model |
| 8 | C7: Koszul pairs historical drift | 3 | 10 | Compress opening |

**Phase 2 execution order**: C3 → C4+C8 (voice cleanup) → C1 (module computation) → C6 → C2
