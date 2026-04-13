# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.

| Theorem | Statement | Status |
|:-------:|-----------|--------|
| **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
| **(B)** | Strict bar-cobar inversion on the Koszul locus; coderived/coacyclic refinement off the locus | Proved here |
| **(C)** | Complementarity package: C0/C1 are proved; the shifted-symplectic/BV upgrade C2 is conditional | C0/C1 proved here; C2 conditional |
| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g on the proved uniform-weight lane; genus 1 is universal, multi-weight g >= 2 has delta F_g^cross | Proved here |
| **(H)** | Chiral Hochschild on the Koszul locus at generic level: concentrated in {0,1,2}, duality shift [2], degree <= 2 Hilbert polynomial | Proved here |

The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.

## The Five Objects

The programme keeps the five canonical objects distinct:

- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
- A^! is recovered from A^i by linear or Verdier duality.
- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.

## Shadow Depth Classification

| Class | Shadow depth | Archetype | Defining property |
|:-----:|:-----------:|-----------|-------------------|
| **G** | 2 | Heisenberg | Gaussian: tower terminates at kappa |
| **L** | 3 | Affine Kac-Moody | Lie/tree: cubic shadow, then terminates |
| **C** | 4 | beta-gamma | Contact/quartic: quartic shadow, then terminates |
| **M** | infinity | Virasoro, W_N | Mixed: infinite tower, all higher shadows nonzero |

## Standalone Papers Programme

16 standalone papers extracting the three-volume programme into publishable units, all CG-rectified:

| Paper | Title | Pages |
|:-----:|-------|------:|
| A | Five Theorems of Modular Koszul Duality | 27 |
| B | The Shadow Obstruction Tower | 43 |
| C | The Ordered Bar Complex and E_1 Primacy | 27 |
| D | Chiral Koszulness: 14 Characterizations | 22 |
| E | E_n-Chiral Algebras and the Operadic Circle | 37 |
| F | Chiral Quantum Groups and the gl_N Tower | 81 |
| G | The Drinfeld-Kohno Bridge | 19 |
| H | Seven Faces of the Collision Residue | 25 |
| I | Arithmetic Shadows | 14 |
| J | Multi-Weight Cross-Channel Corrections | 18 |
| K | SC^{ch,top} and PVA Descent | 18 |
| L | The Holographic Modular Koszul Datum | 15 |
| M | Three-Dimensional Quantum Gravity | 30 |
| N | Analytic Sewing for Chiral Algebras | 40 |
| O | The CY-to-Chiral Functor | 11 |
| P | CY Quantum Groups and 6d hCS | 11 |

Survey paper: 122pp (standalone/survey_modular_koszul_duality_v2.tex).

## Status

| Metric | Value |
|--------|------:|
| Pages (annals edition) | ~2,745 |
| Pages (total with guarded chapters) | ~2,786 |
| Tagged claims (Vol I registry) | ~3,463 |
| Compute tests | 121,000+ |
| Source tree | 89 chapter `.tex`; 15 appendices; 65+ standalone `.tex` |
| Standalone papers | 16 papers, ~438pp total, all CG-rectified |
| Survey paper | 8,507 lines / 122pp |
| Koszulness programme | 10 unconditional + 1 proved consequence + 1 conditional + 1 one-directional + bifunctor + Sklyanin = 14 total |
| Master conjectures MC1-MC5 | ALL PROVED |
| Main proofs adversarially verified | 10/10 SOUND (732-agent campaign) |

## Build

```bash
# Kill any competing pdflatex, then build
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast

# Run tests
make test          # non-slow suite (124,511 currently selected)
make test-full     # full suite (125,444 currently collected)
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
    lib/                    1,352 Python files
    tests/                  1,421 test files (125,444 collected tests)
  standalone/               51 .tex sources
```
