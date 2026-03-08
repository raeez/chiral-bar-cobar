# VISION — Modular Koszul Duality for Factorization Algebras
# The architectural reference for the monograph's unifying programme.
# Source: raeeznotes.md analysis, integrated Mar 2026.
# Read time: 3 minutes. Replaces no existing file.

## The thesis in one sentence

Classical Koszul duality (bar-cobar adjunction) lifts to a proved
modular Koszul core for factorization algebras on curves, and points
toward a modular homotopy theory programme in which genus becomes a
deformation variable internal to the duality itself and is expected to
be organized by a universal Maurer-Cartan class `Theta_A`.

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
  Conjectural H-level completion, where
  `\Theta_A \in MC(Def_cyc(A) \hat{\otimes} R\Gamma(\overline{M}_{g,\bullet}, \mathbb{Q}))`
  is the open homotopy object and `\mathcal{H}_A` is the ambient
  genus-graded deformation family.
  Manuscript: `def:full-modular-package`, `conj:master-theta`

## Current frontier order

The active route is not flat:

1. the finite-type MC1 entry theorem is resolved;
2. MC2 is the foundational next target, now reduced on the theorem
   surface to three exact packages: the intrinsic cyclic
   `\Defcyc(\cA)` model, the geometric completed tensor / clutching
   package, and the one-channel genus-by-genus normalization problem in
   the simple-Lie case;
3. MC3 and MC4 are the structural comparison layer after the standard
   M-level completions for `W_\infty` and Yangian towers;
4. MC5 is downstream physics completion;
5. periodicity is a weak orthogonal flank, not the master-conjecture
   chain.

## Theorematic silhouette (the target)

| Label | Statement | Status | Manuscript |
|-------|-----------|--------|------------|
| A_mod | Bar-cobar intertwined with Verdier, functorial over M_{g,n} | PROVED (genus 0+g) | Theorems A, B |
| B_mod | Inversion on Koszul locus; coderived persistence off it | PROVED + conjectured | Thm B + concordance |
| C_mod | (-1)-shifted symplectic complementarity (Lagrangian) | Conjectured | conj:lagrangian-complementarity |
| Index | GRR: genus series = kappa(A) * (A-hat(ix) - 1) | Conjectured | conj:family-index |
| DK | Derived Drinfeld-Kohno: Fact_E1(Y(g)) ~ Fact_E1(U_q(g))^op | Conjectured | conj:derived-drinfeld-kohno |

## Free fields as atoms

Not easy examples — the irreducible kernel displaying full generality:
- **Free fermion**: antisymmetric collapse (trivial bar cohomology)
- **Heisenberg**: universal genus series, A-hat genus appearance
- **betagamma/bc**: shared discriminant Delta = (1-3x)(1+x)
- **KM/Vir/W**: functorial shadows via DS reduction (discriminant preserved)
- **Yangian**: E1 door to braided/noncommutative world (R -> R^{-1})

## The ultimate generalization principle

Arnold (genus 0, additive) -> clutching + conjectural `Theta_A`
(modular, on curves) -> Fay (elliptic, multiplicative)

The Fay trisecant identity replaces Arnold when base geometry becomes
two-dimensional. Eisenstein-series corrections enter. This is the
toroidal/elliptic extension (toroidal_elliptic.tex).

## Programmes as facets of modular Koszul duality

| Programme | Role in modular Koszul programme |
|-----------|--------------------------------|
| I (Langlands) | Critical-level bar = derived opers; the MC2 hierarchy is expected to degenerate there |
| II (KL) | Admissible-level bar = quantum group (periodic/CDG shadow feeding the `Theta_A` programme) |
| III (Fusion) | Monoidality of bar-cobar should act on the modular characteristic hierarchy |
| IV (E_n) | Higher-dimensional generalization (Arnold -> Totaro -> Fay) |
| V (Vassiliev) | Feynman transform = topological shadow of the characteristic hierarchy |
| VI (Physics) | bar = BRST, curvature = anomaly, `Theta_A` = quantum-background target |
| VII (NC Hodge) | Genus variable = twistor parameter of the characteristic hierarchy |
| VIII (Open math) | Structural conjectures about the hierarchy itself |
| IX (Computation) | Explicit data testing scalar/spectral laws and the MC2 frontier |

## Next volume skeleton (from raeeznotes XII)

"Modular Homotopy Theory for Factorization Algebras on Curves":
1. Curved factorization algebras and coderived Ran categories
2. Cyclic deformation complexes and the universal modular MC equation
3. Shifted symplectic complementarity (PTVV theorem on M-bar_g)
4. Grothendieck-Riemann-Roch for modular Koszul duality
5. Derived Drinfeld-Kohno and elliptic extension (Arnold -> Fay)

## Gaps between raeeznotes vision and current manuscript — ALL ADDRESSED

| Gap | Location | Status |
|-----|----------|--------|
| Four-kernel pedagogy | introduction.tex:229 | ✅ rem:four-pieces |
| Atoms framing | free_fields.tex:32 | ✅ rem:free-field-atoms |
| Discriminant as char. class | concordance.tex | ✅ conj:discriminant-characteristic |
| Arnold → Fay elevation | toroidal_elliptic.tex | ✅ rem:arnold-fay-generalization |
