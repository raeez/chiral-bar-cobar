# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex of a chiral algebra is computed by integration over Fulton-MacPherson compactifications; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

| Theorem | Statement |
|:-------:|-----------|
| **(A)** | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
| **(B)** | Bar-cobar inversion: quasi-isomorphism on the Koszul locus |
| **(C)** | Complementarity: deformations of A and obstructions of A^! are Lagrangian complements |
| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g at all genera (uniform-weight lane) |
| **(H)** | Hochschild duality: ChirHoch*(A) polynomial, Koszul-functorial |

All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.

## The Six-Object Web

Six objects built from the bar complex B(A), connected by three functors:

- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).

## Shadow Depth Classification

| Class | Shadow depth | Archetype | Defining property |
|:-----:|:-----------:|-----------|-------------------|
| **G** | 2 | Heisenberg | Gaussian: tower terminates at kappa |
| **L** | 3 | Affine Kac-Moody | Lie/tree: cubic shadow, then terminates |
| **C** | 4 | beta-gamma | Contact/quartic: quartic shadow, then terminates |
| **M** | infinity | Virasoro, W_N | Mixed: infinite tower, all higher shadows nonzero |

## Status

| Metric | Value |
|--------|------:|
| Pages | ~2,650 |
| Tagged claims | ~6,023 |
| Compute tests | ~120,000+ |
| Source files | 113 .tex chapters + 15 appendices + 35 standalones |
| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
| Shadow census families | 25 (14 original + 11 added: BP_k, W_3, Ising, N=2 SCA, W(p), Y-algebras, symplectic boson/fermion, quantum lattice) |
| Compute modules | 1,312 lib + 1,378 test |
| Anti-patterns | AP1-AP149 (123 foundational + 26 deep empirical) + AAP1-18 + RS-1..20 |
| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
| Standalone papers | 13 (all building successfully) |

## Build

```bash
# Kill any competing pdflatex, then build
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast

# Run tests
make test          # fast suite (~8K)
make test-full     # all tests (~120K definitions)
```

Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).

## Structure

The monograph has six parts plus appendices:

- **Part I** (The Bar Complex): Theorems A-D+H, bar-cobar adjunction, inversion, complementarity
- **Part II** (The Characteristic Datum): nonlinear shadow obstruction tower, depth classification
- **Part III** (The Standard Landscape): 21 example families including Y-algebras and logarithmic W(p), combinatorial frontier
- **Part IV** (Physics Bridges): Feynman, BV/BRST, E_n, Langlands (YM/HT content migrated to Vol II)
- **Part V** (The Seven Faces of r(z)): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin
- **Part VI** (The Frontier): conditional extensions, conjectural outlook

```
chiral-bar-cobar/
  main.tex                  entry point
  Makefile                  build system
  chapters/
    frame/                  overture + preface + introduction
    theory/                 Parts I-II (~30 files)
    examples/               Part III (~20 files)
    connections/            Parts IV-VI (~30 files)
  appendices/               signs, FM proofs, tables
  compute/
    lib/                    1,312 verification engines
    tests/                  1,378 test files (~120K tests)
  standalone/               13 extracted standalone papers
```
