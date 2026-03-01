# Chiral Duality in the Presence of Quantum Corrections

**Geometric Realizations via Configuration Spaces**

---

A research monograph constructing the geometric bar-cobar duality for chiral algebras
on algebraic curves, extending Beilinson--Drinfeld's genus-zero framework through
all genera via configuration space integrals on Fulton--MacPherson compactifications.

> *Logarithmic differential forms on configuration spaces act as diffracting prisms,*
> *decomposing chiral algebras across their operadic spectrum.*

---

## The Central Construction

The manuscript builds a geometric realization of the bar construction

$$\bar{B}_{\text{geom}} \colon \mathsf{ChirAlg}_X \longrightarrow \mathsf{dgCoalg}_X$$

for chiral algebras on a smooth algebraic curve $X$.
The differential sums residues over boundary divisors
of the Fulton--MacPherson compactification:

$$d_{\text{geom}} = \sum_{D \,\in\, \partial\, \overline{C}_n(X)} (-1)^{|D|} \operatorname{Res}_D$$

Nilpotence $d^2 = 0$ at genus zero follows from the
Arnold--Orlik--Solomon relations. At genus $g \geq 1$,
curvature enters: $d_g^2 = \sum_k t_{g,k} \cdot \mathrm{obs}_k$,
controlled by modular parameters $t_{g,k} \in H^1(\mathcal{M}_g)$
and central obstructions $\mathrm{obs}_k \in Z(\mathcal{A})$.

---

## Repository Layout

```
.
├── main.tex                         Entry point (preamble, structure, includes)
├── Makefile                         Build system
├── README.md
├── .gitignore
│
├── chapters/
│   ├── theory/                      Part I: Theory (19 files)
│   │   ├── introduction.tex             Introduction and main results
│   │   ├── algebraic_foundations.tex     Classical Koszul duality
│   │   ├── configuration_spaces.tex     FM compactification, Arnold relations
│   │   ├── bar_cobar_construction.tex   The core construction
│   │   ├── bar_cobar_quasi_isomorphism.tex  Inversion theorem, spectral sequence
│   │   ├── poincare_duality.tex         Non-abelian Poincare duality
│   │   ├── higher_genus.tex             Extension to all genera
│   │   ├── higher_genus_full.tex        Full genus theory
│   │   ├── higher_genus_quasi_isomorphism.tex  Higher genus inversion
│   │   ├── koszul_across_genera.tex     Tower structure, modular invariance
│   │   ├── chiral_koszul_pairs.tex      Curved structures, non-quadratic
│   │   ├── koszul_pair_structure.tex    Pair classification
│   │   ├── deformation_theory.tex       Deformation-obstruction theory
│   │   ├── classical_to_chiral.tex      Three-level hierarchy
│   │   ├── chiral_modules.tex           Module categories
│   │   ├── poincare_duality_quantum.tex Quantum Poincare duality
│   │   ├── quantum_corrections.tex      Loop corrections
│   │   ├── filtered_curved.tex          Filtered vs. curved hierarchy
│   │   └── hochschild_cohomology.tex    Chiral Hochschild, cyclic structure
│   │
│   ├── examples/                    Part II: Examples (21 files)
│   │   ├── free_fields.tex              Heisenberg, free fermion
│   │   ├── beta_gamma.tex               Symplectic bosons
│   │   ├── heisenberg_higher_genus.tex  Higher genus Heisenberg
│   │   ├── obstruction_classes.tex      Obstruction class computations
│   │   ├── heisenberg_eisenstein.tex    Eisenstein series, modular forms
│   │   ├── kac_moody_framework.tex      Affine Kac-Moody: framework
│   │   ├── kac_moody_computations.tex   sl_2, sl_3, E_8 computations
│   │   ├── w_algebras_framework.tex     W-algebras: framework
│   │   ├── w_algebras_computations.tex  W_3, W_N, minimal models
│   │   ├── w3_composite_fields.tex      W_3 Lambda field derivation
│   │   ├── minimal_model_fusion.tex     Verlinde formula, fusion rules
│   │   ├── minimal_model_examples.tex   Fusion tables
│   │   ├── w_algebras_deep.tex          Flag varieties, jet geometry, Toda
│   │   ├── deformation_quantization.tex Chiral Kontsevich formality
│   │   ├── deformation_quantization_complete.tex  Complete proofs
│   │   ├── deformation_examples.tex     Star products, Maurer-Cartan
│   │   ├── yangians.tex                 Drinfeld Yangians, Coulomb branches
│   │   ├── toroidal_elliptic.tex        Double affine, elliptic R-matrix
│   │   ├── genus_expansions.tex         All-genera expansions
│   │   ├── detailed_computations.tex    Degree-by-degree tables
│   │   └── examples_summary.tex         Examples catalogue summary
│   │
│   └── connections/                 Part III: Connections (8 files)
│       ├── poincare_computations.tex    NAP duality computations
│       ├── feynman_diagrams.tex         Feynman diagram interpretation
│       ├── feynman_connection.tex       Feynman-configuration connection
│       ├── bv_brst.tex                  BV-BRST formalism
│       ├── holomorphic_topological.tex  Holomorphic-topological theories
│       ├── physical_origins.tex         4d/2d, D-branes, AGT
│       ├── genus_complete.tex           Universal genus tower
│       └── concordance.tex              Literature concordance
│
├── appendices/                      Appendices (14 files)
│   ├── general_relations.tex            A-infinity relations, sign formulas
│   ├── arnold_relations.tex             Arnold relations
│   ├── signs_and_shifts.tex             Koszul signs, suspensions, determinants
│   ├── sign_conventions.tex             LV vs. manuscript dictionary
│   ├── theta_functions.tex              Theta functions, modular forms
│   ├── spectral_sequences.tex           Filtered complexes, convergence
│   ├── spectral_higher_genus.tex        Hodge-to-de Rham at higher genus
│   ├── koszul_reference.tex             Koszul duality reference
│   ├── homotopy_transfer.tex            HTT: SDR, tree formulas, transfer
│   ├── dual_methodology.tex             Abstract-concrete methodology
│   ├── computational_tables.tex         Computational tables
│   ├── existence_criteria.tex           Existence criteria
│   ├── nilpotent_completion.tex         Nilpotent completion
│   └── notation_index.tex               Complete notation index
│
├── bibliography/
│   └── references.tex                   Bibliography
│
├── notes/                           Working documents
│   ├── INSIGHTS.md                      Mathematical audit log
│   └── ...
│
└── archive/                         Superseded material
```

---

## Building

**Requirements:** TeX Live (or equivalent) with `pdflatex`, the `memoir` class,
`ebgaramond`, `newtxmath`, `microtype`, `tikz-cd`, `thmtools`, `mathtools`,
and `tcolorbox`.

```
make            # Full build (3 passes — stable cross-references, ~1015 pages)
make fast       # Single pass for quick iteration
make watch      # Continuous rebuild on file changes (requires latexmk)
make check      # Halt-on-error validation
make draft      # Draft mode (faster, suppresses images)
make clean      # Remove build artifacts
make veryclean  # Remove artifacts and compiled PDF
make count      # Manuscript statistics (line count, page count)
make help       # Show all targets
```

The canonical entry point is `main.tex`. All chapter files are pulled in
via `\include` or `\input` from their semantic directories. The build produces `main.pdf`.

**Font options.** The default build uses EB Garamond (free) via `pdflatex`.
For Adobe Garamond Pro (commercial), uncomment the XeLaTeX/LuaLaTeX
font block in `main.tex` and compile with `xelatex` or `lualatex`.

---

## Structure

The manuscript is organized in three parts, followed by appendices.

### Part I — Theory

| Ch. | Source | Subject |
|-----|--------|---------|
| 1 | `theory/introduction` | Introduction and main results |
| 2 | `theory/algebraic_foundations` | Algebraic foundations: classical Koszul duality |
| 3 | `theory/configuration_spaces` | Configuration spaces and logarithmic forms |
| 4 | `theory/bar_cobar_construction`, `theory/bar_cobar_quasi_isomorphism` | The geometric bar-cobar construction |
| 5 | `theory/poincare_duality` | Non-abelian Poincare duality |
| 6 | `theory/higher_genus*`, `theory/koszul_across_genera` | Higher genus extension |
| 7 | `theory/chiral_koszul_pairs` -- `theory/hochschild_cohomology` | Chiral Koszul pairs, deformation theory, Hochschild cohomology |

### Part II — Examples

| Ch. | Source | Subject |
|-----|--------|---------|
| 8 | `examples/free_fields`, `examples/beta_gamma` | Free field theories: Heisenberg, fermions, $\beta\gamma$ |
| 9 | `examples/kac_moody_*` | Affine Kac--Moody algebras |
| 10 | `examples/w_algebras_*`, `examples/w3_*`, `examples/minimal_model_*` | $\mathcal{W}$-algebras |
| 11 | `examples/deformation_quantization*` | Chiral deformation quantization |
| 12 | `examples/yangians` | Yangians, shifted Yangians, Coulomb branches |
| 13 | `examples/toroidal_elliptic` | Toroidal and elliptic algebras |
| 14 | `examples/genus_expansions` | Explicit genus expansions |

### Part III — Connections and Applications

| Source | Subject |
|--------|---------|
| `connections/poincare_computations` | Non-abelian Poincare duality: computations |
| `connections/feynman_diagrams` | Feynman diagram interpretation |
| `connections/bv_brst` | BV-BRST formalism |
| `connections/holomorphic_topological` | Holomorphic-topological theories |
| `connections/physical_origins` | Physical origins: 4d/2d, D-branes, AGT |
| `connections/concordance` | Literature concordance |

---

## Key Results

1. **Geometric bar construction** realizing chiral algebra homology
   through residue calculus on compactified configuration spaces.

2. **Bar-cobar quasi-isomorphism** $\Omega^{\text{ch}} \circ \bar{B}_{\text{geom}} \simeq \mathrm{id}$
   via spectral sequence collapse.

3. **Higher genus extension** incorporating quantum corrections
   as curvature in curved $A_\infty$ structures,
   with $m_0 \propto (k + h^\vee) \cdot \text{Casimir}$ at genus $g \geq 1$.

4. **Deformation-obstruction complementarity** for chiral Koszul pairs:
   $Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \simeq H^*(\mathcal{M}_g, Z(\mathcal{A}))$.

5. **Chiral Poincare duality**
   $HH^n_{\text{chiral}}(\mathcal{A}) \simeq HH^{2-n}_{\text{chiral}}(\mathcal{A}^!)^\vee$.

6. **Explicit computations** through degree 5 for Heisenberg,
   affine Kac--Moody ($\mathfrak{sl}_2$, $\mathfrak{sl}_3$, $E_8$),
   and $\mathcal{W}$-algebras with curved $A_\infty$ Koszul duals.

---

## Notation

| Symbol | Meaning |
|--------|---------|
| $\bar{B}_{\text{geom}}(\mathcal{A})$ | Geometric bar complex |
| $\Omega^{\text{ch}}(\mathcal{C})$ | Chiral cobar complex |
| $\overline{C}_n(X)$ | Fulton--MacPherson compactification |
| $\eta_{ij} = d\log(z_i - z_j)$ | Logarithmic 1-forms |
| $\mathsf{Com}$, $\mathsf{Lie}$, $\mathsf{Ass}$ | Operads (Loday--Vallette conventions) |
| $\mathsf{A}_\infty$, $\mathsf{L}_\infty$, $\mathsf{C}_\infty$ | Homotopy algebras |
| $k + h^\vee$ | Shifted level (Kac--Moody) |
| $\mathcal{W}_k(\mathfrak{g})$ | $\mathcal{W}$-algebra at level $k$ |
| $E_r^{p,q}$ | Spectral sequence page |

A complete notation index appears in `appendices/notation_index.tex`.

---

## Mathematical Prerequisites

The reader is assumed familiar with:

- Operad theory and Koszul duality (Loday--Vallette, *Algebraic Operads*)
- Vertex algebras and chiral algebras (Beilinson--Drinfeld, Frenkel--Ben-Zvi)
- Configuration spaces and the Fulton--MacPherson compactification
- Homological algebra: $A_\infty$, $L_\infty$, spectral sequences, derived categories
- Moduli of curves $\overline{\mathcal{M}}_{g,n}$ and their cohomology

---

*~120,000 lines of LaTeX across 64 source files, compiling to ~1015 pages.*
