# Execution Plan — Chiral Bar-Cobar Monograph

## For Claude Opus 4.6 — Code Environment — Maximum Reasoning

This document is the operational plan for completing the monograph. It encodes the three breakthrough results, the structural reorganization, and the systematic examples/connections work. Supersedes the previous "Five Moves" framework (session 19); see notes/ENDGAME_PROMPT_v2.md for the analysis that produced this revision.

---

## Current State (verified 2026-03-01)

### Theory Graph
- 287 indexed claims: 231 ProvedHere, 49 ProvedElsewhere, 7 Conjectured, 0 Open
- 7 theory conjectures: thm:backreaction, thm:curved-mc-cobar, thm:partition-cyclic, thm:yangian-self-dual, cor:genus-expansion-converges, cor:physical-complementarity, cor:string-theory-complementarity-explicit

### Examples + Connections
- ~97 conjectures across 15 files (see CONJECTURE_REGISTRY.md)
- Densest: kac_moody_framework (8), free_fields (11), genus_complete (8), holomorphic_topological (7)
- Thinnest chapters: yangians (207 lines, 0 ProvedHere), toroidal_elliptic (144 lines, 0 ProvedHere)

### Infrastructure Established (Sessions 16-18)
- E₁-chiral: def:chiral-ass-operad, prop:chirAss-self-dual (proved)
- E₁ Koszul duality: thm:e1-chiral-koszul-duality (proved, 3-step proof)
- Module theory: def:factorization-module through def:module-categories (all defined)
- Module Koszul duality: thm:e1-module-koszul-duality (proved)
- Geometric = operadic bar: thm:geometric-equals-operadic-bar (proved)
- Modular operad + Feynman transform: def:modular-operad, def:feynman-transform (defined)
- Prism Principle: cor:prism-principle (proved at all genera)
- d² = 0 at all genera: thm:genus-induction-strict (proved)

### Critical Discovery (Session 20)
**The KS map gap in Main Theorem C can be closed for all Koszul pairs.** The proof as written (Step 7 of thm:quantum-complementarity-main) has three weaknesses, all fixable with existing machinery:
1. lem:fiber-cohomology-center uses informal "dimensional analysis" → replace with bar-complex kernel argument
2. "[D, ρ(z)] = 0 because z acts by a scalar" is Heisenberg-specific → generalize via Koszul pairing intertwining
3. "Z(A) ≅ Z(A!) via Koszul pairing" is asserted → prove via thm:e1-module-koszul-duality (equivalence preserves endomorphism algebras of unit)

### Hidden Theorem Identified (Session 20)
**Heisenberg Module Koszul Duality:** D^b(Mod^E₁_{H_κ}) ≃ D^b(Mod^E₁_{Sym^ch(V*)}) — a 3-line corollary of thm:e1-module-koszul-duality + thm:heisenberg-koszul-dual-early. Not yet stated in manuscript.

---

## Phase 7: Three Breakthroughs

### Breakthrough 1: Complete Main Theorem C — General KS Map (higher_genus.tex)

**Goal:** Close the Kodaira-Spencer map gap for ALL Koszul chiral pairs. This is the book's deepest theorem.

**What needs to change in the manuscript:**

The 10-step proof of thm:quantum-complementarity-main (lines 3742-4571) is structurally sound. Steps 1-6 and 8-10 are fully general. Only Step 7 (thm:kodaira-spencer-chiral-complete, lines 4228-4350) needs strengthening at three points:

**Fix A — lem:fiber-cohomology-center (lines 3965-4019):**
Replace the informal "dimensional analysis and conformal symmetry" argument (line 4002-4004) with:
1. The degree-0 fiber bar complex is B₀|_{Σ_g} = A
2. The bar differential d: B₁ → B₀ extracts OPE residues (collision maps)
3. H⁰(B|_{Σ_g}) = ker(d*) = {a ∈ A : Res_{z=w}[a(z) · (-)(w)] = 0 for all insertions}
4. This kernel is exactly Z(A) (center = elements with no singular OPE)
5. Z(A) is intrinsic to the algebra (independent of Σ_g) → fiber cohomology sheaf is constant

**Fix B — Center isomorphism Z(A) ≅ Z(A!) (line 4393):**
Replace the parenthetical assertion with a lemma proved via module Koszul duality:
1. thm:e1-module-koszul-duality gives D(Mod_A) ≃ D(Comod_{A!})
2. Under this equivalence, the unit module A maps to B(A) = A! (as comodule)
3. Z(A) = End_{D(Mod_A)}(A) ≅ End_{D(Comod_{A!})}(A!) = Z(A!)
4. Equivalences of categories preserve endomorphism algebras → canonical isomorphism

**Fix C — Anti-commutativity for general center (lines 4328-4339):**
Replace "z acts by a scalar on the Koszul pairing" with the general argument:
1. The Koszul pairing gives a map κ: Z(A) → Z(A!) (from Fix B)
2. Verdier intertwining: D ∘ ρ(z) = ρ(κ(z)) ∘ D (Koszul pairing is D-module morphism)
3. Anti-commutativity of Lie derivative: D ∘ L_v = -L_v ∘ D (standard, already stated)
4. Combined: D ∘ (ρ(z) ∘ L_v) = ρ(κ(z)) ∘ (-L_v) ∘ D = -(ρ(κ(z)) ∘ L_v) ∘ D
5. The involution σ = D ∘ ((-)!)⁻¹ absorbs κ(z) ↦ z, giving σ ∘ ∇ᶻ = -∇ᶻ ∘ σ

**Feasibility:** All three fixes use existing proved results (thm:e1-module-koszul-duality, cor:duality-bar-complexes-complete, lem:verdier-extension-exchange). No new mathematical ideas needed — this is assembly of existing machinery.

**Payoff:** Completes Main Theorem C for ALL Koszul pairs. Resolves the gap that has been identified since session 13. Upgrades the monograph's deepest theorem from "proved for Heisenberg at genus 1" to "proved in full generality."

**Downstream:** Resolves ~10 conjectures in higher_genus.tex and genus_complete.tex that depend on the general complementarity theorem.

---

### Breakthrough 2: Lattice Self-Duality (lattice_foundations.tex)

**Goal:** Prove V_Λ^! ≅ V_Λ for even unimodular Λ. Build the examples catalog.

**Theorem:** For even unimodular Λ: V_Λ^! ≅ V_Λ. For general even Λ: V_Λ^! ≅ V_{Λ*}.

**Proof strategy:**
1. Decompose B(V_Λ) along Λ-grading: B(V_Λ) = ⊕_{λ∈Λ} B(V_Λ)_λ
2. Zero-weight: B(V_Λ)₀ = B(Heisenberg) → dual is Sym^ch(V*) (proved)
3. λ-weight: B(V_Λ)_λ is rank 1 over B₀, generated by [e^λ]. Coproduct: Δ([e^λ]) = Σ_{μ+ν=λ} ε(μ,ν) [e^μ] ⊗ [e^ν]
4. For unimodular Λ = Λ*: the coproduct dualizes to the V_Λ product via ε
5. Cocycle consistency: ε(α,β) = (-1)^{⟨α,β⟩} ε(β,α) ensures compatibility

**Feasibility:** Computation + one insight (unimodularity makes coproduct self-dual).

**Payoff:** Opens entire lattice engine. From V_{E₈}: sublattice restriction gives duals for V_{A_n}, V_{D_n}. Enables catalog of 15-20 explicit pairs. Resolves ~7 conjectures in lattice_foundations.tex.

---

### Breakthrough 3: PBW Filtration Derives FG (concordance.tex + chiral_koszul_pairs.tex)

**Goal:** Prove Com^ch-Lie^ch duality is associated graded of Ass^ch self-duality.

**Theorem:** The arity filtration on Ass^ch-algebras induces a PBW filtration whose associated graded recovers FG duality: gr^PBW(Ass^ch-Koszul) = Com^ch-Lie^ch-Koszul.

**Proof strategy:**
1. Classical: arity filtration on Ass has gr = Com ∘ Lie (PBW, LV §9.3)
2. Chiral: j*j*(A ⊠ A) = Sym²_ch(A) ⊕ ∧²_ch(A)
3. PBW filtration: F_p B_{Ass^ch} with F₀/F₁ = B_{Com^ch}, F₁/F₂ = B_{Lie^ch}
4. Degeneration: for Koszul algebras, E₁ concentrated on diagonal → collapse

**Risk:** j* may not commute with Σ-quotients. Fallback: prove for E∞-chiral algebras (where commutativity trivializes the filtration), which still derives FG.

**Feasibility:** Insight required (the j* commutation). E∞ fallback is computation-level.

**Payoff:** Transforms concordance.tex into a theorem chapter. Positions FG as special case.

---

## Structural Reorganization

### Absorb koszul_across_genera.tex into higher_genus.tex
- Move genus tower diagram (lines 134-143) and degeneration compatibility into new section of higher_genus.tex
- State genus-graded Koszul duality as conjecture with modular Koszulity hypothesis
- Delete standalone file, update main.tex

### Compress classical_to_chiral.tex into introduction.tex
- Add "Three-Level Dictionary" subsection (~15 lines) to introduction
- Downgrade 3 conjectured theorems to "expected consequences"
- Delete standalone file, update main.tex, remove 3 conjectures from census

### Write Hidden Theorem A
- Add corollary in free_fields.tex after thm:heisenberg-koszul-dual-early
- 3-line proof: apply thm:e1-module-koszul-duality to H_κ with dual = Sym^ch(V*)
- State representation-theoretic consequences (simple ↔ projective, Ext exchange)

---

## Phase 8: Examples Engine

### 8A: Lattice Catalog (after Breakthrough 2, ~3700 new lines)
Prioritized pairs:
1. H_κ ↔ Sym^ch(V*) — existing, add module corollary
2. bc ↔ βγ — ~200 lines, computation
3. V_{A₁} ↔ V_{A₁} — ~250 lines, self-dual
4. V_{D₄} ↔ V_{D₄} — ~300 lines, triality
5. V_{E₈} ↔ V_{E₈} — ~400 lines, Breakthrough 2
6. ĝ_κ(sl₂) generic ↔ Wakimoto — ~300 lines
7. ĝ_κ(sl₂) critical ↔ curved — ~200 lines
8. Vir_c ↔ curved dual — ~200 lines
9. W₃^k ↔ W₃^{k'} — ~400 lines (formerly Move 1, now Phase 8C)
10. V_{A₁⊕A₁} — ~100 lines, direct sum functoriality
11. V_{A₂} — ~250 lines, rank 2 root
12. V_{Leech} ↔ V_{Leech} — ~300 lines, moonshine
13-15. Genus-1 corrections for H_κ, ĝ(sl₂), V_{E₈} — ~800 lines total

### 8B: Kac-Moody Conjectures (independent of breakthroughs)
- Wakimoto Koszul dual, screening = bar differential, A∞ operations
- sl₃ computation through degree 5

### 8C: W-algebra Computations (formerly Move 1)
- W₃ Koszul duality: computation, not a breakthrough
- Bar complex through degree 4, genus-1 obstruction

### 8D: Representation Theory Applications
- State module category equivalence for each computed pair
- Ext groups via Koszul resolution for Heisenberg, KM, lattice VOAs

### 8E: Advanced Examples (appendix sections, not full chapters)
- Yangians: ~500 lines, state E₁ framework + RTT + conjectured dual
- Toroidal/elliptic: ~300 lines, Fay identity + conjectured bar complex
- Deformation quantization: state formality conjectures precisely

---

## Phase 9: Connections

### 9A: PBW and Literature Concordance (after Breakthrough 3)
- If proved: expand to ~800 lines with full PBW theorem
- If obstructed: ~350 lines with precise obstruction + E∞ partial result
- GLZ comparison, Costello-Gwilliam comparison

### 9B: Physics Triage
- 4 conjectures → provable with mathematical content
- 5 conjectures → label as "physical motivation" (new \ClaimStatusPhysics tag)
- 4 conjectures → state with precise hypotheses as open problems

### 9C: Holomorphic-Topological Trim
- Trim from 900 to ~500 lines
- Keep: CL → chiral (provable), HCS operad (provable)
- Remove or appendix: speculative AGT/4d material

---

## Execution Order

**Session 20 (current):**
1. ✅ Write EXECUTION_PLAN v2
2. Write Hidden Theorem A (free_fields.tex)
3. **Breakthrough 1: General KS map** (higher_genus.tex) — the centerpiece
4. Verify compilation

**Session 21:** Breakthrough 2 (lattice self-duality) + begin catalog
**Session 22:** Breakthrough 3 (PBW/FG) + structural reorganization
**Sessions 23-25:** Phase 8 systematic computation
**Session 26:** Phase 9 connections + final cleanup

### Completion Criteria
1. Main Theorems A, B, C have complete, gap-free proofs (C for ALL Koszul pairs)
2. Lattice engine produces ≥10 explicit Koszul dual pairs
3. Module category equivalence stated for each computed pair
4. FG derived as special case (or precise obstruction stated)
5. Every Conjectured item: proved, precisely bounded, or labeled as open/physics
6. Zero compilation errors, zero undefined references
