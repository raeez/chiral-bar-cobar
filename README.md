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

## Five Main Theorems (Platonic form, 2026-04-17)

These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable. Each theorem has been adversarially audited through the 2026-04-16 sweep and now stands at its strongest honest form.

| Theorem | Statement | Status |
|:-------:|-----------|--------|
| **(A)** | Bar-cobar equivalence at properad level in the Francis-Gaitsgory factorization ambient on Ran(X); R-twisted Σ_n-descent relates ordered and symmetric bars | Proved here (upgraded to `thm:A-infinity-2`, ∞,2-categorical) |
| **(B)** | Strict bar-cobar inversion on the Koszul locus via explicit MacLane-splitting for class G/L; coderived/coacyclic refinement off the locus; class M direct-sum genuinely false, weight-completed proved | Proved here |
| **(C)** | Complementarity package: C0/C1 unconditional on Koszul locus; the shifted-symplectic/BV upgrade C2 conditional only on BV package; +3 shift contradiction at g = 0 resolved via `thm:theorem-C-g0` | C0/C1 proved here; C2 conditional on BV package |
| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g uniform-weight all g >= 1; multi-weight carries explicit cross-channel correction delta F_g^cross; clutching-uniqueness pins the scalar | Proved here |
| **(H)** | Chiral Hochschild on the Koszul locus at generic level: concentrated in {0,1,2}, duality shift [2], sharp Hilbert series; Feigin-Frenkel companion at k = -h^v (infinite-dim center, non-exclusion) | Proved here |

Programme status 2026-04-17: Four previously-irreducible frontiers CLOSED or REDUCED on the non-degenerate locus — curved-Dunn H² = 0 at g ≥ 2 (Vol II `curved_dunn_higher_genus.tex`); DS-Hochschild bridge for class M (Vol II `chiral_higher_deligne.tex`); `conj:periodic-cdg` admissible KL (Vol I `periodic_cdg_admissible.tex`); chain-level chiral Deligne-Tamarkin (reduced to associator-dependence). Single remaining open: original-complex chain-level E_3-topological for class M (weight-completed proof is unconditional).

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
| Pages (annals edition) | ~2,700 |
| Pages (total with Platonic reconstitutions) | ~2,900 |
| Tagged claims (Vol I registry) | ~3,550 |
| Compute tests | 125,000+ |
| Source tree | 106 chapter `.tex`; 16 appendices; 67+ standalone `.tex` |
| Standalone papers | 16 papers + 2 MC5 successors (theorem + analytic), all CG-rectified |
| Survey paper | 8,500+ lines / 122pp |
| Koszulness programme | 14 characterizations on GRT-equivariant moduli atlas `M_Kosz(A)` |
| Master conjectures MC1-MC5 | ALL PROVED (MC5 weight-completed class M; direct-sum class M genuinely false as scope) |
| Main proofs adversarially verified | 10/10 SOUND through April 2026 (>732-agent campaigns) |
| First-principles cache | 750+ lines, cross-programme enforcement verified clean |
| HZ-IV decorators installed | ~45 Wave-1 / Wave-2 installations across theorem labels |
| Shadow tower S_r | closed forms through r = 11 with three-tier arithmetic stratification |
| Reconstitution waves | 14 completed 2026-04-16 (105-agent sweep); Platonic ideal form inscribed |

## Build

All compiled output goes to `out/`.

```bash
make fast                    # quick converging build → out/main.pdf
make                         # full build: manuscript + working notes → out/
make release                 # manuscript + working notes + standalone → out/ + iCloud
make standalone              # standalone papers → out/
make test                    # non-slow test suite (124,511 currently selected)
make test-full               # full suite (125,444 currently collected)
make clean-builds            # remove /tmp/mkd-* isolated build directories
```

Each build runs in its own `/tmp/mkd-chiral-bar-cobar-<NS>/` directory,
so parallel agents never clobber each other's `.aux` files. Set
`MKD_BUILD_NS` to reuse a build directory across invocations (warm
`.aux` files converge in fewer passes):

```bash
export MKD_BUILD_NS="agent-$$"   # stable for the agent's session
make fast                         # cold first time
# ... edit ...
make fast                         # warm — reuses .aux, converges faster
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
