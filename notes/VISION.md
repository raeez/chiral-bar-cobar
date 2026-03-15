# VISION — Modular Koszul Duality for Factorization Algebras
# The architectural reference for the monograph's unifying programme.
# Source: raeeznotes.md analysis, integrated Mar 2026.
# Read time: 3 minutes. Replaces no existing file.

## The thesis in one sentence

Classical Koszul duality (bar-cobar adjunction) lifts to a proved
modular Koszul core for factorization algebras on curves, and must be
completed into the definitive dimension-one modular homotopy theory in
which genus becomes a deformation variable internal to the duality
itself and is already organized at the resolved deformation-theoretic
level by the universal Maurer-Cartan class `Theta_A`; the live outer
programme is the categorical and infinite-tower comparison layer.

**Dual Imperative.** The work is governed by maximalist ambition
(always push for the most powerful, general theorems — the shape of
what the book wants to become is a research signal) and maximal
truth-seeking (every claim processed with equal rigor, precise
knowledge of what is proved enabling credible frontier advancement).
These are synergistic: honest status discipline is what makes the
ambition credible.

## Definitive dimension-one mandate

This project is not meant to stop at a proved core plus horizon prose.
The book is being built as the definitive treatise of modular homotopy
theory for factorization algebras on curves in dimension one.

Accordingly, the modular-operadic and homotopy-theoretic foundations
are load-bearing components of the subject, not optional epilogue
material. Some already belong to the proved core; the rest remain
explicit frontier build targets:

- modular operads of stable curves as the organization of the genus tower
- curved factorization algebras on `Ran(X)` and the coderived/contraderived ambient
- H-level bar-cobar adjunction and Verdier compatibility over `\overline{M}_{g,n}`
- the cyclic deformation complex `Def_cyc(A)` and the universal class `Theta_A`
- shifted-symplectic / Lagrangian complementarity as constitutive structure

Status discipline is unchanged: the `Def_cyc(A)` / `Theta_A` and
shifted-symplectic layers now belong to the proved core, while the
coderived Ran and factorization-categorical extensions remain frontier
targets. Future sessions should treat both the proved foundation and
the fenced frontier as parts of one subject, not as optional
background machinery.

## Four irreducible pieces (the minimal kernel)

| Piece | Mathematical content | Manuscript reference |
|-------|---------------------|---------------------|
| 1. Three-point collision | Arnold relation = factorization coherence | configuration_spaces.tex, thm:arnold-os-algebra |
| 2. Verdier on Ran(X) | D_Ran B_X(A) ~ B_X(A!) | thm:bar-cobar-isomorphism-main (Theorem A) |
| 3. Genus-1 curvature | d^2 = kappa(A) * omega_1 * id | thm:higher-genus-inversion (Theorem B), thm:genus-universality |
| 4. Clutching | Modular operad compatibility | thm:prism-higher-genus, thm:master-tower |

Everything else is a completion of these four.

## The correct hierarchy

NOT `kappa(A)` alone, NOT `Q_g(A)` alone, and not the genus-`g` bar
complex separately. The manuscript now treats the characteristic story
as a hierarchy with distinct statuses:

- **Scalar package** `(\kappa(A), \{F_g(A)\}_{g \ge 1})`
  Proved S-level data: genus-`1` curvature and the full scalar genus
  tower.
  Manuscript: `thm:modular-characteristic`, `thm:genus-universality`

- **Spectral layer** `(\Delta_A, \Pi_A)`
  Separately proved non-scalar M/S-level invariants: discriminant,
  recurrence/growth shadow, and periodicity profile.
  Manuscript: `thm:spectral-characteristic`

- **Full package** `\mathcal{C}_A = (\Theta_A, \kappa(A), \Delta_A, \Pi_A, \mathcal{H}_A)`
  Existence is now proved on the current theorem surface, where
  `\Theta_A \in MC(Def_cyc(A) \hat{\otimes} R\Gamma(\overline{M}_{g,\bullet}, \mathbb{Q}))`
  carries the homotopy-level deformation data, `\mathcal{H}_A` is the
  induced genus-graded deformation family, and `\Pi_A` has a proved
  structural framework even where sharp periodicity claims remain
  conjectural.
  Manuscript: `def:full-modular-package`, `thm:mc2-full-resolution`

## Current frontier order

The active route is not flat:

1. the finite-type MC1 entry theorem is resolved;
2. MC2 is resolved: the intrinsic cyclic `\Defcyc(\cA)` model, the
   geometric completed tensor / clutching package, and the resulting
   `Theta_A` all belong to the proved foundation;
3. MC3 and MC4, not MC2, are now the live structural comparison layer
   after the standard
   M-level completions for `W_\infty` and Yangian towers; the active
   MC4 ledger is now exact:
   build the filtered H-level targets, prove
   `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)` and
   `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)`, and close the
   corresponding finite-detection packages `\Delta_{a,0}(N)` and
   `\mathcal{I}_N`;
4. MC5 is downstream physics completion;
5. the non-principal orbit frontier is separate from MC4 standard-tower
   comparison and splits into three packets: dual-orbit input,
   orbit-indexed level shift, and paired DS seed
   transport/globalization;
6. periodicity is a weak orthogonal flank, not the master-conjecture
   chain; its geometric part is currently a nilpotent
   depth/stabilization threshold, not a proved global period law.

## Theorematic silhouette (the current control surface)

| Label | Statement | Status | Manuscript |
|-------|-----------|--------|------------|
| A_mod | Bar-cobar intertwined with Verdier, functorial over M_{g,n} | PROVED | Theorems A, B |
| B_mod | Inversion on the Koszul locus; off-locus coderived persistence explicitly fenced | PROVED on locus; frontier off locus | Thm B + concordance |
| C_mod | (-1)-shifted symplectic complementarity (Lagrangian) | PROVED | thm:shifted-symplectic-complementarity / thm:lagrangian-complementarity |
| Index | GRR: genus series = kappa(A) * (A-hat(ix) - 1) | PROVED | thm:family-index |
| DK | Derived Drinfeld-Kohno ladder from evaluation locus to completed bridge | DK-0/1/1½/2/3 proved on natural loci; DK-4/5 conjectural | concordance DK ladder |

## Free fields as atoms

Not easy examples — the irreducible kernel displaying full generality:
- **Free fermion**: antisymmetric collapse (trivial bar cohomology)
- **Heisenberg**: universal genus series, A-hat genus appearance
- **betagamma/bc**: shared discriminant Delta = (1-3x)(1+x)
- **KM/Vir/W**: functorial shadows via DS reduction (discriminant preserved)
- **Yangian**: E1 door to braided/noncommutative world (R -> R^{-1})

## The ultimate generalization principle

Arnold (genus 0, additive) -> clutching + proved `Theta_A`
(modular, on curves) -> Fay (elliptic, multiplicative)

The Fay trisecant identity replaces Arnold when base geometry becomes
two-dimensional. Eisenstein-series corrections enter. This is the
toroidal/elliptic extension (toroidal_elliptic.tex).

## Programmes as facets of modular Koszul duality

| Programme | Role in modular Koszul programme |
|-----------|--------------------------------|
| I (Langlands) | Critical-level bar = derived opers; the proved MC2 hierarchy is expected to degenerate there |
| II (KL) | Admissible-level bar should recover the semisimplified KL target; the outer non-semisimple/completed lift remains MC3 frontier (periodic/CDG shadow feeding the modular characteristic hierarchy) |
| III (Fusion) | Monoidality of bar-cobar should act on the modular characteristic hierarchy |
| IV (E_n) | Higher-dimensional generalization (Arnold -> Totaro -> Fay) |
| V (Vassiliev) | Feynman transform = topological shadow of the characteristic hierarchy |
| VI (Physics) | bar = BRST, curvature = anomaly, `Theta_A` = quantum-background datum |
| VII (NC Hodge) | Genus variable = twistor parameter of the characteristic hierarchy |
| VIII (Open math) | Structural conjectures about the hierarchy itself |
| IX (Computation) | Explicit data testing scalar/spectral laws and the MC3/MC4 frontier |

## Definitive dimension-one skeleton

"Modular Homotopy Theory for Factorization Algebras on Curves":
1. Modular operads of stable curves in dimension one
2. Curved factorization algebras and coderived Ran categories
3. Cyclic deformation complexes and the universal modular MC equation
4. Shifted symplectic complementarity (PTVV theorem on M-bar_g)
5. Grothendieck-Riemann-Roch for modular Koszul duality
6. Derived Drinfeld-Kohno and elliptic extension (Arnold -> Fay)

## Gaps between raeeznotes vision and current manuscript — ALL ADDRESSED

| Gap | Location | Status |
|-----|----------|--------|
| Four-kernel pedagogy | introduction.tex:229 | ✅ rem:four-pieces |
| Atoms framing | free_fields.tex:32 | ✅ rem:free-field-atoms |
| Discriminant as char. class | concordance.tex | ✅ conj:discriminant-characteristic |
| Arnold → Fay elevation | toroidal_elliptic.tex | ✅ rem:arnold-fay-generalization |
