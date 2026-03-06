# CG Restructuring Plan — Phase 0

## The Diagnosis

The manuscript's Heisenberg content is scattered across **17 files**:
- `algebraic_foundations.tex` (§2.7: Koszul duality from first principles, 130 lines)
- `bar_cobar_construction.tex` (6 examples: degrees 0-1, level shift, conilpotent, strict, quadratic, explicit bar)
- `configuration_spaces.tex` (1 example: factorization)
- `higher_genus.tex` (§: genus 2, obstruction at genus g, pairing, complementarity — 4 major blocks)
- `deformation_theory.tex` (§: Hochschild, Gerstenhaber bracket)
- `hochschild_cohomology.tex` (1 example: E₂ page)
- `filtered_curved.tex` (1 example: explicit bar)
- `chiral_modules.tex` (§: fusion verification)
- `free_fields.tex` (§§7.4-7.15: the bulk — bar complex, Koszul dual, modules, higher genus, complementarity, level inversion, ~1400 lines)
- `heisenberg_eisenstein.tex` (878 lines: genus expansion with Eisenstein series, all genera)
- `genus_expansions.tex` (§: all-genera free energy + A-hat genus)
- `detailed_computations.tex` (§: degrees 3-4, torus, verification — 200+ lines)
- `toroidal_elliptic.tex` (§: elliptic bar complex)
- `deformation_quantization.tex` (§: star product)
- `deformation_examples.tex` (§: Moyal verification)
- `lattice_foundations.tex` (1 example)
- `poincare_computations.tex` (§: NAP computation)
- `feynman_connection.tex` (§: Feynman bridge)

A reader wanting to understand what Heisenberg bar-cobar duality *is* must read fragments from 17 files across 3 Parts. This is the opposite of CG's method.

## The New Architecture

### Part 0: The Heisenberg Algebra (1 chapter, ~80 pages)

**File**: `chapters/frame/heisenberg_frame.tex`
**Role**: The CG frame chapter. Self-contained. Previews the entire theory through one example.

### Part I: The General Theory (chapters 2-10, ~500 pages)

The current theory chapters, with shortened introductions that back-reference the frame chapter. Content unchanged; framing updated.

| New Ch. | File | New Role |
|---------|------|----------|
| 2 | `algebraic_foundations.tex` | Classical bar-cobar (the algebraic template generalized from Heisenberg) |
| 3 | `configuration_spaces.tex` | FM compactification (the geometry behind η₁₂) |
| 4 | `bar_cobar_construction.tex` | General bar-cobar (the construction generalized) |
| 5 | `poincare_duality.tex` | Verdier duality (the mechanism behind Theorem A) |
| 6 | `higher_genus.tex` | Genus tower (the curvature generalized) |
| 7 | `chiral_koszul_pairs.tex` + `koszul_pair_structure.tex` | Koszul pairs (the framework) |
| 8 | `deformation_theory.tex` | Deformation-obstruction (Theorem C generalized) |
| 9 | `chiral_modules.tex` | Module theory |
| 10 | `poincare_duality_quantum.tex` + `quantum_corrections.tex` | Quantum corrections |

**Changes to Part I**: Each chapter gets a new 1-2 paragraph opening that says "In the Heisenberg frame chapter, we saw X in concrete form. We now establish X in full generality." The Heisenberg examples currently embedded in theory chapters (algebraic_foundations §2.7, bar_cobar examples, higher_genus examples) remain in place as "cf. Chapter 1" cross-references — they are **not removed**, only recontextualized. The frame chapter previews; the theory chapters prove generally and re-verify.

### Part II: Complete Portraits (chapters 11-19, ~450 pages)

Each chapter computes one family completely, CG-style portrait.

| New Ch. | File(s) | Title | What's New vs Heisenberg |
|---------|---------|-------|--------------------------|
| 11 | `free_fields.tex` §§fermion | Free fermions and the collapse regime | Antisymmetric collapse (trivial bar) |
| 12 | `free_fields.tex` §§bc + `beta_gamma.tex` | The βγ/bc systems | Shared discriminant (1-3x)(1+x) |
| 13 | `kac_moody_framework.tex` | Affine Kac-Moody algebras | Non-abelian bracket, spectral sequence, Feigin-Frenkel |
| 14 | `w_algebras_framework.tex` + `w3_composite_fields.tex` + `w_algebras_deep.tex` | W-algebras | DS reduction preserves discriminant |
| 15 | `minimal_model_fusion.tex` + `minimal_model_examples.tex` | Minimal models and fusion | Modular tensor categories |
| 16 | `deformation_quantization.tex` + `deformation_examples.tex` | Deformation quantization | P∞→E₁ passage |
| 17 | `yangians.tex` + `toroidal_elliptic.tex` | Yangians and the E₁-chiral world | Braided monodromy, R→R⁻¹ |
| 18 | `genus_expansions.tex` | Genus expansions: three theorems in action | The full interlock demonstrated |
| 19 | `detailed_computations.tex` + `examples_summary.tex` | Computational atlas and Master Table | Data |

**Changes to Part II**: The free_fields.tex chapter loses its "Examples I" and "Examples II" framing. The Heisenberg sections (~1400 lines) become back-references to Chapter 1. The lattice_foundations chapter is absorbed as a section of Ch. 13 (KM) or Ch. 18 (genus expansions), since lattice VOAs are extensions of Heisenberg by lattice vertex operators and their genus expansion is already proved via Heisenberg (thm:lattice-all-genera).

### Part III: The Frontier (chapters 20-24, ~200 pages)

Unchanged in substance. The concordance chapter becomes the epilogue.

| New Ch. | File(s) | Title |
|---------|---------|-------|
| 20 | `poincare_computations.tex` | NAP explicit computations |
| 21 | `feynman_diagrams.tex` + `feynman_connection.tex` | Feynman diagrams |
| 22 | `bv_brst.tex` | BV-BRST |
| 23 | `holomorphic_topological.tex` + `physical_origins.tex` + `genus_complete.tex` | Holomorphic-topological and physics |
| 24 | `concordance.tex` | Concordance and the modular Koszul programme |

### Appendices: Unchanged

All 14 appendix files stay exactly where they are.

---

## The Heisenberg Frame Chapter: Detailed Outline

### Section 1.1: The OPE (1 page)

Open cold:
```
Let X be a smooth algebraic curve. The Heisenberg chiral algebra H_k
at level k has a single current α(z) of conformal weight 1, with
operator product expansion

    α(z)α(w) = k/(z-w)² + regular.

The double pole is the entire structure.
```

**Source**: `free_fields.tex:607-613` (Definition), `algebraic_foundations.tex:228-238` (Lie* setup).

No motivation, no history. The OPE is the starting point.

### Section 1.2: The bar complex at degree 1 (3 pages)

Build B̄¹ by hand. The element α(z₁)⊗α(z₂)⊗η₁₂ where η₁₂ = d log(z₁-z₂). Apply the bar differential via the Borcherds identity. The double-pole OPE produces d_res = k·1 (extracting the second-order pole coefficient). Explain that this is NOT the literal residue of k/(z₁-z₂)² · dz/(z₁-z₂) (which would be a triple pole with zero residue) but the operadic extraction of OPE data.

**Source**: `algebraic_foundations.tex:266-302` (geometric perspective), `free_fields.tex:638-655` (degree 1 proof), `free_fields.tex:2462-2479` (step 2 computation).

### Section 1.3: The bar complex at degree 2 — Arnold enters (5 pages)

Build B̄². Three currents, two log forms. The element α(z₁)⊗α(z₂)⊗α(z₃)⊗η₁₂∧η₂₃. Now apply d twice. The Arnold relation η₁₂∧η₂₃ + η₂₃∧η₃₁ + η₃₁∧η₁₂ = 0 appears not as a theorem to state but as a computation that forces d²=0.

State the Arnold relation as a recognition: "The identity we have just used to verify d²=0 has a name."

**Source**: `free_fields.tex:680-698` (degree 2), `detailed_computations.tex:12-80` (full degree 3-4), `algebraic_foundations.tex:285-302`.

### Section 1.4: The bar complex at all degrees — d²=0 (3 pages)

Induction on degree. The Heisenberg bracket is purely central (no simple poles), so d_bracket = 0 and only d_curvature contributes. The full bar complex has cohomology H⁰=C, H¹=0 (on P¹), H²=C·c_k, Hⁿ=0 for n>2.

State: "For the Heisenberg algebra, the bar complex is formal: its cohomology is concentrated in degrees 0 and 2."

**Source**: `free_fields.tex:624-698` (thm:heisenberg-bar, full proof).

### Section 1.5: Reading off the Koszul dual (4 pages)

The bar cohomology is a commutative coalgebra (coLie^ch on one cogenerator). Apply cobar. Get Sym^ch(V*) — the commutative chiral algebra. The curvature m₀ = -k·ω encodes the level.

State the recognition: "The bar complex has produced a Koszul dual algebra without our having defined what 'Koszul dual' means. The construction we have just performed is an instance of a general pattern (Definition ref in Chapter 2)."

Key theorem: H_k is NOT self-dual. Table comparing H_k vs Sym^ch(V*).

**Source**: `free_fields.tex:784-795` (thm:heisenberg-koszul-dual-early), `free_fields.tex:2460-2528` (full derivation), `free_fields.tex:2508-2528` (not self-dual).

### Section 1.6: Bar-cobar inversion — Theorem A in action (3 pages)

Verify Ω(B̄(H_k)) → H_k is a quasi-isomorphism. The cobar of the coalgebra recovers the original algebra. This is Theorem A for the simplest case.

**Source**: `free_fields.tex:2500-2503`, `algebraic_foundations.tex:323-340`.

### Section 1.7: The passage to genus 1 — curvature appears (8 pages)

This is the dramatic turn. Replace P¹ by an elliptic curve E_τ. The propagator acquires periods:

G_τ(z) = ζ_τ(z) + (π²E₂(τ)/3)·z

The Weierstrass ζ-function, its quasi-periodicity, and the E₂ correction — all derived from first principles (Liouville's theorem forces the regularization).

Compute d² on E_τ. It is no longer zero: d² = κ(H_k)·ω₁·id where κ = k (the level). Curvature has appeared.

State the recognition: "The differential ceases to be strictly square-zero. This is the first appearance of a quantum correction."

**Source**: `heisenberg_eisenstein.tex:61-140` (genus-1 complete derivation), `higher_genus.tex:3464-3538` (obstruction theorem).

### Section 1.8: The holomorphic anomaly and E₂ (3 pages)

The E₂ quasi-modular form is the holomorphic anomaly. Under modular transformations, the two-point function transforms with an anomaly term proportional to κ. This is the genus-1 obstruction class.

**Source**: `heisenberg_eisenstein.tex:142-156` (rem:E2-holomorphic-anomaly).

### Section 1.9: Why the derived category fails (3 pages)

The curvature d²≠0 means the bar complex is NOT a chain complex in the ordinary sense. The ordinary derived category kills the distinction between "acyclic because exact" and "acyclic because curved." Positselski's coderived category is the natural home.

State: "The Heisenberg algebra at level k≠0 is the simplest object that forces us out of the ordinary derived category."

**Source**: `free_fields.tex:788` (Positselski reference), `concordance.tex:855-888` (coderived formalism).

### Section 1.10: Genus 2 — Siegel modular forms (5 pages)

The genus-2 Green function involves the prime form and Siegel modular forms E₄(Ω), E₆(Ω). Compute explicitly. The partition function at genus 2 is verified.

**Source**: `heisenberg_eisenstein.tex:180-370` (genus-2 complete + general genus).

### Section 1.11: The genus tower — recognizing the A-hat genus (6 pages)

The genus-g free energy is F_g = κ · (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)!. Compute F₁ = 1/24, F₂ = 7/5760, F₃ = 31/967680 by hand.

The generating function is Σ F_g x^{2g} = κ(x/2/sin(x/2) - 1) = κ(Â(ix) - 1).

State the recognition: "The generating function is the Wick-rotated A-hat genus. This is not coincidental — it is the shadow of a family index theorem (Conjecture ref)."

Derive this from the Faber-Pandharipande λ_g formula and the Bernoulli number identity.

**Source**: `genus_expansions.tex:7-80` (thm + A-hat remark), `heisenberg_eisenstein.tex:476-518` (DMVV agreement).

### Section 1.12: Complementarity — Theorem C in action (5 pages)

For the Koszul pair (H_k, Sym^ch(V*)):
- Q_g(H_k) + Q_g(H_k!) = H*(M̄_g, Z(H_k))
- The deformation space of H_k and the obstruction space of its dual are complementary.

Explicit genus-1 computation. Genus-2 complementarity.

**Source**: `free_fields.tex:2727-2860` (thm:heisenberg-genus-g, explicit genus-1), `higher_genus.tex:6207-6450` (complementarity examples).

### Section 1.13: The modular characteristic package (4 pages)

Collect the invariants computed so far into a single object:
- Θ_A ∈ MC(Def_cyc(A) ⊗̂ RΓ(M̄_{g,•}, Q)) — the universal MC class
- H_A := RΓ(M̄_g, Z_A) — the ambient deformation complex
- Δ_A(x) — the spectral discriminant (for Heisenberg: trivial, since rank 1)
- κ(H_k) = k — the first characteristic number

State: "For the Heisenberg algebra, the modular characteristic package is fully determined by the single number κ = k. In Chapter 13, we will see that for affine Kac-Moody algebras, the package acquires non-trivial spectral discriminant."

**Source**: `introduction.tex:129-227` (modular Koszul package), `concordance.tex:923-957` (universal MC conjecture).

### Section 1.14: What breaks for sl₂-hat — preview of the non-abelian theory (5 pages)

The Heisenberg has d_bracket = 0 (no simple poles). For ĝ_k, the simple poles contribute d_bracket ≠ 0, and d_bracket² ≠ 0 alone — the full Borcherds identity (not just Jacobi) is needed for the combined differential.

The bar spectral sequence: E₁ page involves d_bracket, E₂ page has the Chevalley-Eilenberg cohomology. For Koszul algebras, E₂ collapses.

The Feigin-Frenkel involution k ↦ -k-2h∨ is Koszul duality (not just a representation-theoretic accident).

Preview the level shift, the non-abelian discriminant Δ(x) = (1-3x)(1+x) shared by sl₂/Vir/βγ, and the critical level k = -h∨ where curvature vanishes.

**Source**: `kac_moody_framework.tex:1-54` (opening), `introduction.tex:896-917` (strict nilpotence).

### Section 1.15: What breaks for Yangians — preview of the E₁ world (4 pages)

The Heisenberg is E∞-chiral (commutative, full locality). The Yangian Y(g) is E₁-chiral (associative, no locality). The bar complex uses ordered configurations. Verdier duality inverts the R-matrix: Y(g)! ≅ Y_{R⁻¹}(g).

Preview the derived Drinfeld-Kohno conjecture: Fact_{E₁}(Y(g)) ≃ Fact_{E₁}(U_q(g))^op.

**Source**: `yangians.tex:1-60` (opening), `introduction.tex:428-556` (E₁ dictionary).

### Section 1.16: The view from here — what the theory wants to become (4 pages)

State the three main theorems as observations about Heisenberg, then as general theorems:
- Theorem A: What we saw as "bar produces Koszul dual" generalizes to...
- Theorem B: What we saw as "cobar inverts bar" generalizes to...
- Theorem C: What we saw as "complementarity of deformation and obstruction" generalizes to...

State the modular Koszul programme: A_mod, B_mod, C_mod, Index Theorem, Derived Drinfeld-Kohno.

Close: "The Heisenberg algebra is the atom from which this theory is built. Every theorem in this monograph is an elaboration of what we have seen in this chapter."

**Source**: `introduction.tex:162-227` (three theorems unified), `concordance.tex:844-960` (programme).

---

## The Transition Map

### Theorems that MOVE to the Frame Chapter

No theorems move. The frame chapter **previews** theorems by computing them for Heisenberg, but the formal statements and proofs remain in their current locations. The frame chapter creates new `\label`s for its own versions (e.g., `thm:heisenberg-bar-frame`, `thm:heisenberg-genus-tower-frame`) and cross-references the general theorems with forward pointers.

### Theorems that stay in place

ALL 695 ProvedHere, 333 ProvedElsewhere, 113 Conjectured claims remain exactly where they are. Their statement texts and proofs are untouched.

### What changes

1. **New file**: `chapters/frame/heisenberg_frame.tex` (~80 pages, ~2500 lines of new/reorganized content)
2. **main.tex**: New `\part{The Heisenberg Algebra}` before current Part I. Add `\include{chapters/frame/heisenberg_frame}`.
3. **introduction.tex**: Shortened from 1569 lines to ~400 lines. Remove the extended Dictionary section (§1.4), the Main Results with proof locations (§1.6), and the corollaries/applications (§1.7) — these are now previewed in the frame chapter. Keep: problem statement (§1.1), three theorems (§1.2), central thesis (§1.3), relationship to foundational work (§1.5).
4. **Part preambles**: Rewrite the 4 \part{} introductory paragraphs (currently at main.tex:628-640, 741-765, 891-913) to reference the frame chapter.
5. **Chapter openings**: Each of the 12 theory chapters gets a new 1-2 paragraph opening referencing the frame chapter. The current multi-paragraph preambles are shortened but not eliminated.
6. **free_fields.tex**: The chapter opening (lines 1-57) and the "Examples II: Heisenberg" section header are rewritten to say "Having studied the Heisenberg algebra in Chapter 1, we now..." The ~1400 lines of Heisenberg content remain but are reframed as "the complete proof of what Chapter 1 previewed."
7. **algebraic_foundations.tex**: §2.7 (Heisenberg Koszul duality from first principles, lines 211-342) is reframed: "The computation we performed for Heisenberg in Chapter 1 generalizes..."

### What does NOT change

- All theorem/proposition/lemma/corollary/definition statements
- All proofs
- All \label{} identifiers
- All cross-references (\ref{}, \eqref{})
- All appendices
- All bibliography entries
- All compute/ code
- The document class, preamble, fonts, macros

---

## Execution Strategy

### Phase 1: Write the Frame Chapter (~2500 lines)

**Approach**: The frame chapter is primarily a *resequencing* of existing content. Roughly:
- §1.1-1.6: Adapted from `algebraic_foundations.tex:211-342` and `free_fields.tex:599-798`
- §1.7-1.8: Adapted from `heisenberg_eisenstein.tex:61-177`
- §1.9: New expository text (~50 lines), citing Positselski
- §1.10-1.11: Adapted from `heisenberg_eisenstein.tex:180-518` and `genus_expansions.tex:7-80`
- §1.12: Adapted from `free_fields.tex:2727-2860`
- §1.13: Adapted from `introduction.tex:129-227`
- §1.14-1.15: New expository text (~200 lines), previewing KM and Yangian
- §1.16: Adapted from `concordance.tex:844-960`

**Key principle**: The frame chapter *recomputes* rather than *references*. It presents complete, self-contained calculations that happen to also appear (in more general form) in later chapters. The frame chapter and the later chapters are both correct and complete — the frame chapter is concrete, the later chapters are general.

### Phase 2: Update main.tex

- Add `\part{The Heisenberg Algebra}` with preamble
- Add `\include{chapters/frame/heisenberg_frame}`
- Update Part I/II/III preambles (3 paragraphs each)

### Phase 3: Shorten introduction.tex

- Remove ~1000 lines of content that is now previewed in the frame chapter
- Keep the structural overview, the three-theorem statements, the central thesis
- Add forward reference to Chapter 1

### Phase 4: Update chapter openings

- 12 theory chapter openings: each gets 1-2 new paragraphs (replace current preambles)
- 8 example chapter openings: each gets 1 new paragraph
- 4 connection chapter openings: minimal changes

### Phase 5: Verify

- `make fast` to check compilation
- `grep -c` census to verify no claims were altered
- Cross-reference audit: all \ref{} still resolve

---

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| Frame chapter duplicates content | Intentional. CG duplicates sl₂ content. The frame chapter is concrete, later chapters are general. Both are needed. |
| Cross-references break | No labels are moved or renamed. Frame chapter creates new labels. |
| Page count increases | Expected +80 pages (frame chapter) - 50 pages (shortened intro) = net +30 pages. Acceptable for a 1276-page book. |
| Heisenberg examples in theory chapters become redundant | They are not redundant — they verify the general theory for a specific example. The frame chapter previews; the theory chapters prove. |
| Chapter numbering changes | All internal cross-references use \ref{}, not hardcoded numbers. Chapter numbers will shift +1 but refs are symbolic. |

---

## Success Criteria

1. A mathematician reading ONLY Chapter 1 understands what modular Koszul duality is.
2. A mathematician reading Chapter 2's opening paragraph says "Yes, I need this generalization because Heisenberg was abelian and the bracket was trivial."
3. A mathematician reading Chapter 6's opening paragraph says "Yes, I need this because the curvature I saw at genus 1 for Heisenberg needs to be controlled at all genera."
4. The Master Table (examples_summary.tex) reads as a *summary* of computations the reader has already seen, not as a *preview* of computations to come.
5. The book compiles with zero errors and the claim census is unchanged.
