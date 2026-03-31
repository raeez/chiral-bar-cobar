# Beilinson Swarm Audit — Prompt Architecture

## The Prompt Template

Each agent receives this prompt with [CHAPTER_FILE] substituted:

---

```
You are a Beilinson auditor for [CHAPTER_FILE]. Your sole purpose is FALSIFICATION — not confirmation, not summary, not improvement. A claim is false until you independently verify it.

CONTEXT (your complete mathematical input — do not read CLAUDE.md):
- Grading: cohomological, |d|=+1. Bar uses desuspension s^{-1}. m_1^2(a) = [m_0, a].
- Status tags (\ClaimStatusProvedHere etc.) are CLAIMS, not proofs. ProvedHere means someone typed those characters.
- Four objects: A (algebra), B(A) (bar coalgebra), A^i = H*(B(A)) (dual coalgebra), A^! = (A^i)^v (dual algebra). Omega(B(A)) = A (inversion, NOT duality).
- Virasoro: self-dual at c=13, NOT c=26. Vir_c^! = Vir_{26-c}. Sugawara UNDEFINED at k=-h^v.
- kappa formulas are FAMILY-SPECIFIC: kappa(KM) = dim(g)(k+h^v)/(2h^v), kappa(Vir) = c/2, kappa(W_N) = c(H_N - 1). NEVER assume one formula applies to another family.

ACTIVE ANTI-PATTERNS (the specific errors this repository makes — check every claim against these):
- AP1: Formula copied between families without recomputation.
- AP3: Pattern completion — "correcting" a formula to match others without independent verification.
- AP4: Status tag as ground truth — ProvedHere tag on a claim whose proof cites conjectural inputs.
- AP7: Scope inflation — universal claim ("for all"), special-case proof (type A only, genus 0 only, generic level only).
- AP15: HOLOMORPHIC/QUASI-MODULAR CONFLATION. E_2*(tau) is quasi-modular (NOT holomorphic). Products of E_2* are polynomials in {E_2*, E_4, E_6}, NOT in {E_4, E_6}. The "dim S_k = 0 for k < 12" argument applies ONLY to holomorphic M_k(SL(2,Z)), NOT to quasi-modular forms. The genus-1 propagator IS E_2*.
- AP16: INTEGRATED IDENTITY ≠ CLASS IDENTITY. F_g = kappa * lambda_g^FP is a number. lambda_g^{(h)} = lambda_g would be a class equality. Hodge bundle E_h = R^0 pi_* omega^{otimes h} has rank (2h-1)(g-1) depending on h. Classes in different cohomological degrees CANNOT be equal.
- AP17: CASCADE ERROR. If you find a suspicious claim, do NOT build on it. Flag it and move on.
- AP18: "ENTIRE STANDARD LANDSCAPE" — before accepting any universal quantifier, mentally list: Heisenberg, free fermion, beta-gamma, affine KM (generic), affine KM (admissible), Virasoro (generic c), Virasoro (minimal model), W_N (principal), W_N (non-principal), lattice VOAs. Check EACH against the hypotheses.

PROTOCOL — execute exactly these 9 steps:
1. Read [CHAPTER_FILE] in full.
2. For every \ClaimStatusProvedHere: read the proof. Does it prove the stated claim? Check: (a) are cited results' hypotheses satisfied? (b) is the scope honest (AP7)? (c) are there unstated assumptions (AP4)?
3. For every formula: verify by dimensional analysis, limiting case, or known special value. Do NOT pattern-match against other occurrences (AP3).
4. For every "for all" / "every" / "the standard landscape": list the families and check each against hypotheses (AP18).
5. For every modular form or Eisenstein series: is the object holomorphic, quasi-modular, or almost-holomorphic? (AP15)
6. For every equality: are both sides the same TYPE (number vs class vs function vs functor)? (AP16)
7. Classify each finding: CRITICAL (logical gap or false claim), SERIOUS (formula error, scope inflation, status mislabel), MODERATE (unstated assumption, missing qualification), MINOR (editorial, notation).
8. Output a numbered list. Each finding: {number}. [{severity}] {file}:{line_range} — {claim_label} — {exact diagnosis}
9. If you find ZERO issues after honest examination, say "No issues found in [CHAPTER_FILE]." Do NOT manufacture findings.

IMPORTANT: Do NOT edit any file. Do NOT suggest fixes. ONLY REPORT findings. Your output is consumed by a human who will decide what to fix.
```

---

## Wave Dispatch Plan

### Wave 1: Vol I Theory Core (20 agents)
The proof backbone. Every other chapter depends on these.

| Agent | File | Lines | Contains |
|-------|------|-------|----------|
| 1 | chapters/theory/bar_construction.tex | 2,036 | Bar complex definition |
| 2 | chapters/theory/cobar_construction.tex | 3,241 | Cobar complex, Theorem A partial |
| 3 | chapters/theory/configuration_spaces.tex | 4,916 | FM compactification, Arnold |
| 4 | chapters/theory/algebraic_foundations.tex | 1,914 | Definitions, conventions |
| 5 | chapters/theory/chiral_koszul_pairs.tex | 4,454 | Koszul meta-theorem (12 equiv) |
| 6 | chapters/theory/bar_cobar_adjunction_curved.tex | 6,993 | Theorem A, curved bar-cobar |
| 7 | chapters/theory/bar_cobar_adjunction_inversion.tex | 6,010 | Theorem B, MK3 conditionality |
| 8 | chapters/theory/poincare_duality.tex | 774 | Poincaré duality foundations |
| 9 | chapters/theory/poincare_duality_quantum.tex | 1,235 | Quantum corrections to duality |
| 10 | chapters/theory/higher_genus_foundations.tex | 6,429 | Genus tower, multi-gen, MK axioms |
| 11 | chapters/theory/higher_genus_complementarity.tex | 5,743 | Theorem C |
| 12 | chapters/theory/higher_genus_modular_koszul.tex | 21,988 | Theorem D, shadow tower, MC2 |
| 13 | chapters/theory/chiral_hochschild_koszul.tex | 5,439 | Theorem H, deformation complex |
| 14 | chapters/theory/chiral_center_theorem.tex | 1,736 | Center theorem |
| 15 | chapters/theory/hochschild_cohomology.tex | 1,665 | Hochschild bridge |
| 16 | chapters/theory/en_koszul_duality.tex | 2,219 | E_n Koszul duality |
| 17 | chapters/theory/derived_langlands.tex | 1,273 | Langlands bridge |
| 18 | chapters/theory/chiral_modules.tex | 4,969 | Module categories |
| 19 | chapters/theory/quantum_corrections.tex | 1,442 | Quantum corrections |
| 20 | chapters/theory/introduction.tex | 4,483 | Introduction claims |

### Wave 2: Vol I Examples + Key Connections (20 agents)
Computational claims and cross-references.

| Agent | File | Lines | Contains |
|-------|------|-------|----------|
| 21 | chapters/examples/free_fields.tex | 4,120 | Heisenberg, fermion |
| 22 | chapters/examples/beta_gamma.tex | 2,728 | βγ system |
| 23 | chapters/examples/kac_moody.tex | 4,867 | Affine KM |
| 24 | chapters/examples/w_algebras.tex | 6,269 | W-algebras |
| 25 | chapters/examples/w_algebras_deep.tex | 3,710 | W deep structure |
| 26 | chapters/examples/yangians_foundations.tex | 3,367 | Yangian foundations |
| 27 | chapters/examples/yangians_computations.tex | 4,314 | Yangian computations |
| 28 | chapters/examples/yangians_drinfeld_kohno.tex | 7,112 | DK bridge |
| 29 | chapters/examples/lattice_foundations.tex | 4,520 | Lattice VOAs |
| 30 | chapters/examples/genus_expansions.tex | 3,299 | Genus expansions |
| 31 | chapters/examples/landscape_census.tex | 2,762 | Census (authoritative) |
| 32 | chapters/examples/deformation_quantization.tex | 2,133 | Deformation quant |
| 33 | chapters/examples/bar_complex_tables.tex | 4,361 | Bar tables |
| 34 | chapters/connections/concordance.tex | 6,915 | THE CONSTITUTION |
| 35 | chapters/connections/arithmetic_shadows.tex | 8,394 | Arithmetic programme |
| 36 | chapters/connections/bv_brst.tex | 1,104 | BV-BRST bridge |
| 37 | chapters/connections/feynman_diagrams.tex | 1,136 | Feynman bridge |
| 38 | chapters/frame/preface.tex | 7,315 | Preface claims |
| 39 | chapters/frame/heisenberg_frame.tex | 3,726 | Heisenberg overture |
| 40 | chapters/connections/frontier_modular_holography_platonic.tex | 3,928 | Platonic frontier |

### Wave 3: Vol II Theory Core (14 agents)

| Agent | File | Lines | Contains |
|-------|------|-------|----------|
| 41 | ~/vol2/chapters/theory/foundations.tex | 1,852 | Vol II foundations |
| 42 | ~/vol2/chapters/theory/factorization_swiss_cheese.tex | 3,464 | SC operad |
| 43 | ~/vol2/chapters/theory/modular_swiss_cheese_operad.tex | 2,978 | Modular SC |
| 44 | ~/vol2/chapters/theory/axioms.tex | 1,011 | Axiom system |
| 45 | ~/vol2/chapters/theory/fm-calculus.tex | 1,106 | FM calculus |
| 46 | ~/vol2/chapters/theory/pva-descent-repaired.tex | 1,529 | PVA descent |
| 47 | ~/vol2/chapters/theory/introduction.tex | 1,833 | Vol II intro |
| 48 | ~/vol2/chapters/connections/bar-cobar-review.tex | 3,425 | Bar-cobar review |
| 49 | ~/vol2/chapters/connections/hochschild.tex | 1,435 | Hochschild |
| 50 | ~/vol2/chapters/connections/relative_feynman_transform.tex | 3,189 | Relative FT |
| 51 | ~/vol2/chapters/connections/dg_shifted_factorization_bridge.tex | 1,915 | DG bridge |
| 52 | ~/vol2/chapters/connections/spectral-braiding-core.tex | 1,903 | Spectral braiding |
| 53 | ~/vol2/chapters/connections/ordered_associative_chiral_kd_core.tex | 2,165 | Ordered KD |
| 54 | ~/vol2/chapters/connections/modular_pva_quantization_core.tex | 1,971 | PVA quant |

### Wave 4: Vol II Connections + Examples (20 agents)
Remaining Vol II files with substantive content (>500 lines).

### Wave 5: Vol I Remaining Connections (20 agents)
The thqg_* files, YM chapters, editorial constitution.

### Wave 6: Cleanup
Files < 500 lines, stubs, appendices.

## Execution Protocol

1. **Spawn Wave 1** (20 agents in parallel, all subagent_type="Explore")
2. **Collect findings** — the main agent reads all 20 reports
3. **Triage**: CRITICAL findings get immediate RECTIFICATION-FLAG in source
4. **Cross-reference**: Check AP5 (does a finding in one file propagate to others?)
5. **Spawn Wave 2** (incorporating any cross-cutting findings from Wave 1)
6. Repeat for Waves 3-6

## Design Rationale

- **Inline anti-patterns** in prompt (not "read CLAUDE.md") → eliminates tool call, ensures AP15-18 in working memory
- **Read-only agents** (Explore type) → structurally prevents the cascade error (AP17)
- **"Do NOT suggest fixes"** → separates diagnosis from treatment
- **"If ZERO issues, say so"** → prevents manufactured findings
- **Upstream-first waves** → theory core audited before examples/connections that cite it
- **20 agents per wave** → conservative batch size to avoid rate limits
- **Human triage between waves** → findings from Wave 1 inform Wave 2 dispatch
