# Conjecture Registry — Chiral Bar-Cobar Monograph

## Summary
~97 Conjectured claims across 25 files. Organized by priority tier.

---

## Tier 1: Core Theory — Must Resolve for Submission

These block the main theorems or the Five Moves.

### Theory Core (7 claims from PHASE0_PROOF_STATUS)
| Label | File | Line | Description | Move |
|-------|------|------|-------------|------|
| thm:backreaction | poincare_duality_quantum.tex | 214 | Gravitational backreaction as deformation | — |
| thm:curved-mc-cobar | bar_cobar_construction.tex | 3721 | Curved Maurer-Cartan for cobar | — |
| cor:genus-expansion-converges | bar_cobar_construction.tex | 5815 | Genus expansion convergence | 5 |
| thm:yangian-self-dual | chiral_koszul_pairs.tex | 292 | Yangian self-duality | 4 |
| cor:physical-complementarity | higher_genus.tex | 4504 | Physical interpretation of complementarity | 5 |
| cor:string-theory-complementarity | higher_genus.tex | 4652 | String theory complementarity | 5 |
| thm:convergence-filtered | higher_genus.tex | 737 | Convergence for filtered algebras | 5 |

### Move 1 Dependencies (W₃ Koszul Duality)
| Label | File | Line | Description |
|-------|------|------|-------------|
| thm:w-algebra-koszul-main | w_algebras_framework.tex | 38 | Main W-algebra Koszul duality |
| thm:w-geometric-ope | w_algebras_framework.tex | 256 | Geometric OPE formula for W-algebras |
| thm:w-koszul-precise | w_algebras_framework.tex | 394 | Koszul duality precise statement |
| thm:w-bar-coalg | w_algebras_deep.tex | 81 | W-algebra bar coalgebra |

### Move 2 Dependencies (Lattice Engine)
| Label | File | Line | Description |
|-------|------|------|-------------|
| prop:lattice:bar-D4 | lattice_foundations.tex | 644 | D₄ bar complex and triality |
| prop:lattice:bar-E8 | lattice_foundations.tex | 654 | E₈ bar complex |

### Move 3 Dependencies (Derive FG from Ass^ch)
| Label | File | Line | Description |
|-------|------|------|-------------|
| GLZ-special-case | concordance.tex | 52 | GLZ as special case of our framework |

### Move 4 Dependencies (Yangian)
| Label | File | Line | Description |
|-------|------|------|-------------|
| prop:toroidal-ope | toroidal_elliptic.tex | 35 | Toroidal OPE |
| thm:toroidal-e1 | toroidal_elliptic.tex | 43 | Toroidal as E₁-chiral |
| thm:elliptic-vs-rational | toroidal_elliptic.tex | 136 | Elliptic vs rational homology |

---

## Tier 2: High-Value Examples — Upgrade with Existing Machinery

### Kac-Moody Framework (8 conjectures)
| Label | File | Line | Description | Feasibility |
|-------|------|------|-------------|-------------|
| thm:wakimoto-koszul | kac_moody_framework.tex | 256 | Wakimoto as Koszul dual | High — use screening charges |
| thm:screening-bar | kac_moody_framework.tex | 568 | Screening implements bar diff | High |
| thm:kac-moody-ainfty | kac_moody_framework.tex | 624 | A∞ operations on KM | Medium |
| thm:w-algebra-koszul (KM) | kac_moody_framework.tex | 588 | W-algebra via DS as Koszul dual | Medium — depends Move 1 |
| sl₃ Koszul dual | kac_moody_framework.tex | 450 | sl₃ bar complex computation | Medium — fix dim B¹=64 |
| Higher genus corrections | kac_moody_framework.tex | 654 | Genus corrections to KM duality | Low |
| thm:km-holography | kac_moody_framework.tex | 729 | KM in holography | Physics — label as such |
| Connection to quantum groups | kac_moody_framework.tex | 748 | KM ↔ quantum groups | Physics |

### W-Algebra Framework (remaining, after Move 1)
| Label | File | Line | Description | Feasibility |
|-------|------|------|-------------|-------------|
| thm:w-center-langlands | w_algebras_framework.tex | 769 | W-algebra centers and Langlands | Medium |
| thm:agt-w-algebra | w_algebras_framework.tex | 950 | AGT via W-algebras | Physics — label |

### Free Fields (11 conjectures)
| Label | File | Line | Description | Feasibility |
|-------|------|------|-------------|-------------|
| Table entries (5) | free_fields.tex | 922-926 | Koszul dual table conjectures | Medium — each is a separate computation |
| thm:string-amplitude | free_fields.tex | 2182 | String amplitude correspondence | Physics |
| thm:bulk-boundary | free_fields.tex | 2211 | Bulk-boundary correspondence | Physics |
| thm:bulk-reconstruct | free_fields.tex | 2261 | Bulk reconstruction | Physics |
| cor:holographic-dict | free_fields.tex | 2277 | Holographic dictionary | Physics |
| thm:loop-corrections | free_fields.tex | 2297 | Loop corrections as deformation | Physics |
| thm:modular-anomaly-brst | free_fields.tex | 2482 | Modular anomaly and BRST | Medium |

### Heisenberg-Eisenstein (2 conjectures)
| Label | File | Line | Description | Feasibility |
|-------|------|------|-------------|-------------|
| prop:modular-weight-formula | heisenberg_eisenstein.tex | 339 | Modular weight formula | High — direct computation |
| thm:eta-appearance | heisenberg_eisenstein.tex | 347 | Eta function in bar complex | High |

---

## Tier 3: Connections — Label or Prove

### Genus Complete (8 conjectures)
| Label | File | Line | Description | Action |
|-------|------|------|-------------|--------|
| thm:elliptic-bar | genus_complete.tex | 25 | Elliptic bar complex | Prove sketch |
| thm:extension-obstruction | genus_complete.tex | 97 | Extension obstruction classification | Prove |
| thm:higher-genus-diff | genus_complete.tex | 144 | Higher genus bar differential | Prove or precise conjecture |
| thm:master-tower | genus_complete.tex | 208 | Master tower of extensions | Prove sketch |
| thm:EO-recursion | genus_complete.tex | 256 | Eynard-Orantin for bar complex | Conjecture with evidence |
| thm:string-amplitude-debris | genus_complete.tex | 338 | String amplitude = bar cohomology | Physics label |
| holographic-duality-corollary | genus_complete.tex | 364 | Holographic duality via bar-cobar | Physics label |
| thm:poincare-extended | genus_complete.tex | 402 | Poincaré-Verdier extended | **Already proved** (session 17) |

### Holomorphic-Topological (7 conjectures)
| Label | File | Line | Description | Action |
|-------|------|------|-------------|--------|
| prop:CL-produces-chiral | holomorphic_topological.tex | 71 | Costello-Li → chiral algebras | Medium |
| HCS chiral operad | holomorphic_topological.tex | 333 | Chiral operad from HCS | Medium |
| Open-closed duality | holomorphic_topological.tex | 363 | Topological open-closed | Physics |
| Dimension tower | holomorphic_topological.tex | 405 | Factorization along dimension | Speculative |
| W from Hitchin | holomorphic_topological.tex | 451 | W-algebra from Hitchin system | Medium |
| W bar complex (HT) | holomorphic_topological.tex | 502 | W-algebra bar complex | Depends Move 1 |
| Bar-cobar quantum | holomorphic_topological.tex | 552 | Bar-cobar with quantum corrections | Depends Move 5 |
| thm:agt-bar-cobar | holomorphic_topological.tex | 844 | AGT through bar-cobar | Physics |

### Physical Origins (3 conjectures — all physics)
| Label | File | Line | Description | Action |
|-------|------|------|-------------|--------|
| thm:nc-cs | physical_origins.tex | 57 | Non-commutative Chern-Simons | Physics label |
| thm:dbrane-e1 | physical_origins.tex | 82 | D-brane algebras are E₁ | Physics label |
| thm:q-agt | physical_origins.tex | 117 | q-deformed AGT | Physics label |

### Other Connections
| Label | File | Line | Description | Action |
|-------|------|------|-------------|--------|
| thm:genus-complementarity | poincare_computations.tex | 334 | Genus complementarity | Prove (Move 5 consequence) |
| thm:costello-gaiotto-agt | bv_brst.tex | 369 | Costello-Gaiotto AGT | Physics label |

---

## Tier 4: Theory Periphery — Prove or Precisely Conjecture

### Deformation Theory (3)
| Label | File | Line | Description |
|-------|------|------|-------------|
| Reflected modular periodicity | deformation_theory.tex | 597 | Conjecture |
| Periodicity exchange | deformation_theory.tex | 732 | Under Koszul duality |
| Holographic Koszul | deformation_theory.tex | 810 | Conjecture |

### Chiral Koszul Pairs (5, excluding thm:yangian-self-dual)
| Label | File | Line | Description |
|-------|------|------|-------------|
| Affine Yangian from W | chiral_koszul_pairs.tex | 278 | Affine Yangian from W-algebras |
| Feynman-bar-cobar | chiral_koszul_pairs.tex | 1454 | Feynman-bar-cobar correspondence |
| Curved Koszul pairs | chiral_koszul_pairs.tex | 1930 | Curved pair theory |
| bc-βγ extended | chiral_koszul_pairs.tex | 1955 | Extended bc-βγ vs two fermions |

### Classical to Chiral (3)
| Label | File | Line | Description |
|-------|------|------|-------------|
| thm:hierarchy-functorial | classical_to_chiral.tex | 52 | Functoriality of hierarchy |
| thm:enhancement-preserves | classical_to_chiral.tex | 290 | Enhancement preserves Koszul |
| thm:three-level-main | classical_to_chiral.tex | 410 | Three-level hierarchy main theorem |

### Koszul Across Genera (4 — stub file)
| Label | File | Line | Description |
|-------|------|------|-------------|
| Extended Koszul duality | koszul_across_genera.tex | 5 | Conjecture |
| Genus-graded theorem | koszul_across_genera.tex | 26 | Theorem |
| Resolution | koszul_across_genera.tex | 61 | Lemma |
| MC elements | koszul_across_genera.tex | 80 | Theorem |

### Koszul Pair Structure (6)
| Label | File | Line | Description |
|-------|------|------|-------------|
| Periodicity Virasoro | koszul_pair_structure.tex | 467 | Conjectured |
| Periodicity affine critical | koszul_pair_structure.tex | 518 | Conjectured |
| Gaiotto-Witten S-duality | koszul_pair_structure.tex | 881 | Physics |
| WRT | koszul_pair_structure.tex | 1040 | Physics |
| AdS/CFT as CS/Koszul | koszul_pair_structure.tex | 1082 | Physics |
| BV structure | koszul_pair_structure.tex | 1105 | Conjectured |

### Other Theory
| Label | File | Line | Description |
|-------|------|------|-------------|
| Extended Koszul 4.3 | introduction.tex | 953 | Extended Koszul duality |
| W-algebra cohomology | hochschild_cohomology.tex | 66 | W-algebra Hochschild |
| Partition function cyclic | hochschild_cohomology.tex | 468 | Z as cyclic homology |
| KS complementarity higher genus | quantum_corrections.tex | 283 | Higher genus complementarity |
| W-algebra critical level | chiral_modules.tex | 653 | Calculation |
| Fermion-boson Koszul | bar_cobar_construction.tex | 2953 | Conjectured |
| Universal extension tower | bar_cobar_construction.tex | 4086 | Conjectured |
| conj:holographic-koszul | poincare_duality_quantum.tex | 992 | Holographic conjecture |

### Deformation Quantization (6)
| Label | File | Line | Description |
|-------|------|------|-------------|
| Chiral quantization | deformation_quantization.tex | 112 | Conjectured |
| Chiral Kontsevich | deformation_quantization.tex | 152 | Conjectured |
| Genus expansion DQ | deformation_quantization.tex | 462 | Conjectured |
| Chiral formality | deformation_quantization.tex | 502 | Conjectured |
| Holographic duality DQ | deformation_quantization.tex | 613 | Physics |
| P∞ formality | deformation_examples.tex | 66 | Conjectured |

---

## Action Summary

| Action | Count | Description |
|--------|-------|-------------|
| **Prove** | ~25 | Upgradable with existing machinery (Moves 1-5 + Phase 8) |
| **Prove sketch** | ~10 | Need more detail but strategy exists |
| **Physics label** | ~25 | Require physics input beyond scope; label precisely |
| **Precise conjecture** | ~15 | State with evidence, mark as open problems |
| **Already proved** | 1 | thm:poincare-extended — update status tag |
| **Depends on Moves** | ~20 | Blocked until Move 1-5 proofs exist |

---

## Priority Ordering for Sessions

1. **Move 5 conjectures** (complete Main Theorem C): cor:genus-expansion-converges, cor:physical-complementarity, cor:string-theory-complementarity, thm:convergence-filtered
2. **Move 1 conjectures** (W₃ engine): thm:w-algebra-koszul-main, thm:w-koszul-precise, thm:w-geometric-ope
3. **Move 2 conjectures** (lattice engine): prop:lattice:bar-D4, prop:lattice:bar-E8
4. **Move 4 conjectures** (Yangian): thm:yangian-self-dual, toroidal conjectures
5. **Move 3 conjectures** (FG derivation): GLZ special case
6. **Kac-Moody upgrades**: thm:wakimoto-koszul, thm:screening-bar, thm:kac-moody-ainfty
7. **Physics labeling pass**: all "Physics" entries → add precise mathematical content + label as beyond scope
8. **Heisenberg upgrades**: prop:modular-weight-formula, thm:eta-appearance
9. **Theory periphery**: prove or precisely conjecture remaining items
