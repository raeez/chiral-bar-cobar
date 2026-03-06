# VISION — Modular Koszul Duality for Factorization Algebras
# The architectural reference for the monograph's unifying programme.
# Source: raeeznotes.md analysis, integrated Mar 2026.
# Read time: 3 minutes. Replaces no existing file.

## The thesis in one sentence

Classical Koszul duality (bar-cobar adjunction) lifts to a modular
homotopy theory for factorization algebras on curves, where genus is
a deformation variable internal to the duality itself, controlled by a
single universal Maurer-Cartan class Theta_A.

## Four irreducible pieces (the minimal kernel)

| Piece | Mathematical content | Manuscript reference |
|-------|---------------------|---------------------|
| 1. Three-point collision | Arnold relation = factorization coherence | configuration_spaces.tex, thm:arnold-os-algebra |
| 2. Verdier on Ran(X) | D_Ran B_X(A) ~ B_X(A!) | thm:bar-cobar-isomorphism-main (Theorem A) |
| 3. Genus-1 curvature | d^2 = kappa(A) * omega_1 * id | thm:higher-genus-inversion (Theorem B), thm:genus-universality |
| 4. Clutching | Modular operad compatibility | thm:prism-higher-genus, thm:master-tower |

Everything else is a completion of these four.

## The correct object

NOT kappa(A), NOT Q_g(A), NOT the genus-g bar complex separately.
The correct object is the **modular characteristic package** (Theta_A, H_A, Delta_A):

- **Theta_A** in MC(Def_cyc(A) hat-tensor RGamma(M-bar_{g,.}, Q))
  Universal MC class controlling full genus tower as single deformation.
  Manuscript: eq:universal-MC (introduction.tex:147), conj:universal-MC (concordance.tex:930)

- **H_A** := RGamma(M-bar_g, Z_A) with Verdier duality
  Ambient modular deformation complex; home of complementarity.
  Manuscript: thm:quantum-complementarity-main (Theorem C)

- **Delta_A(x)** = det(1-xT) spectral discriminant
  First non-scalar characteristic class. Branch geometry invariant.
  Manuscript: thm:ds-bar-gf-discriminant (examples_summary.tex)

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

Arnold (genus 0, additive) -> clutching + Theta_A (modular, on curves) -> Fay (elliptic, multiplicative)

The Fay trisecant identity replaces Arnold when base geometry becomes
two-dimensional. Eisenstein-series corrections enter. This is the
toroidal/elliptic extension (toroidal_elliptic.tex).

## Programmes as facets of modular Koszul duality

| Programme | Role in modular Koszul programme |
|-----------|--------------------------------|
| I (Langlands) | Critical-level bar = derived opers (Theta_A trivializes) |
| II (KL) | Admissible-level bar = quantum group (N-complex periodicity of Theta_A) |
| III (Fusion) | Monoidality of bar-cobar = modular package functoriality |
| IV (E_n) | Higher-dimensional generalization (Arnold -> Totaro -> Fay) |
| V (Vassiliev) | Feynman transform = topological shadow of modular package |
| VI (Physics) | bar = BRST, curvature = anomaly, Theta_A = quantum background |
| VII (NC Hodge) | Genus variable = twistor parameter of modular package |
| VIII (Open math) | Structural conjectures about the package itself |
| IX (Computation) | Explicit data confirming/refuting the package predictions |

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
