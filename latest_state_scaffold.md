# Latest-state analysis and theorem scaffolding

**Dual Imperative**: This scaffold is governed by maximalist ambition
(the most powerful theorems the subject admits) and maximal truth-seeking
(every claim verified at its stated level). These are synergistic.

## 1. Current state

The project now has a stable constitutional spine:
- H/M/S levels are explicit.
- scalar / spectral / full package are distinguished.
- fiberwise curvature and total strict differential are separated.
- Chapter 34 governs status, and the dependency order is now
  `MC2 -> MC3/MC4 -> MC5`, with periodicity kept orthogonal.
- shifted-symplectic / Lagrangian complementarity is already in
  Stratum I.

The live danger is no longer broad theorem-graph instability inside the
TeX core. The remaining danger is residual prompt/state drift on
Markdown or synthesis surfaces, especially when:
- periodicity is described as the main bottleneck rather than an
  orthogonal weak flank;
- `conj:lagrangian-complementarity` is cited as if still conjectural;
- physics bridges are phrased as completed theorem-level
  identifications rather than genus-`0` theorems plus downstream
  comparison programmes.

For entry, the book should now be read through two atoms rather than a
single generic examples layer:
- Heisenberg = the primary commutative/modular atom.
- The Yangian evaluation-locus Drinfeld-Kohno square = the secondary
  braided/factorization atom.

The first atom shows why genus forces modular completion.  The second
shows why ordered configurations force factorization and braid
reversal.  The open category-`O` / dg-shifted Yangian comparison must
remain visibly downstream of that second atom.

## 2. Derived DK -> factorization DK

The factorization statement needs to be upgraded in three passes.

### Pass I: intrinsic ordered factorization category
Define `Factord(X; A)` as the stable infinity-category of A-modules on ordered configuration spaces with interval-factorization descent and braid-monodromy compatibility. Prove:
1. exit-path / ordered-FM model equivalence;
2. compact generation by evaluation objects on the rational Yangian side;
3. monoidal Verdier reversal acts by `op` on the tensor structure.

### Pass II: factorization Kazhdan functor
Construct a functor
`KZ_fact : Factord(X; Y_h(g)) -> Factord(X; U_q(g))`
whose shadow on evaluation modules is the classical Kazhdan/KZ functor, and prove:
1. compatibility with ordered interval fusion;
2. compatibility with braid monodromy / R-matrix transport;
3. compatibility with the bar-cobar duality involution `h -> -h`, hence `q -> q^{-1}`.

### Pass III: extension beyond evaluation locus
To extend from evaluation modules to full category O, the book needs four exact inputs:
1. Yangian Koszulness or a replacement monadic criterion strong enough to produce minimal bar resolutions for category O;
2. pro-nilpotent / RTT-complete control on the bar side;
3. a generator theorem saying evaluation modules generate the relevant factorization category after completion / ind-completion;
4. a monadicity or Barr-Beck style reconstruction identifying the target factorization category with modules for the reconstructed quantum-group factorization algebra.

### DK ladder
The derived Drinfeld-Kohno package should be linearized as a staged
ladder rather than stored as one monolithic conjecture:
1. `DK-0`: chain-level evaluation-locus `q \mapsto q^{-1}` /
   `R \mapsto R^{-1}` shadow on the standard evaluation objects;
2. `DK-1`: intrinsic ordered factorization category on the evaluation
   locus;
3. `DK-2`: factorization Kazhdan functor `KZ_fact` on that ordered
   category;
4. `DK-3`: extension beyond evaluation modules via Koszul,
   generation, and monadicity input;
5. `DK-4`: full ordered `E1`-factorization equivalence;
6. `DK-5`: dg-shifted Yangian / line-operator comparison at the
   intended H-level target.

## 3. New theorems the book wants

### T1. Higher-genus PBW concentration theorem
Move the resolved MC1 package into the theorem spine, not only concordance.

### T2. Scalar-to-spectral modular characteristic theorem
Package `kappa`, `Delta_A`, and `Pi_A` as the proved shadow hierarchy, separate from `Theta_A`.

### T3. Universal cyclic deformation theorem
Construct `Def_cyc(A)` as a cyclic `L_infty` algebra and solve the completed MC equation to define `Theta_A`.

### T4. Factorization DK theorem
Upgrade evaluation-locus factorization DK to a full equivalence of ordered `E1` factorization categories.

### T5. dg-shifted Yangian comparison theorem
Show the dg-shifted Yangian of line operators and the chiral Yangian of ordered configuration spaces present the same H-level object after RTT-complete filtration.

### T6. Infinite-tower H-level comparison theorem
For principal `W_infty` / Yangian towers, prove the filtered H-level comparison by coefficient identification and finite detection.

### T7. BV/BRST/bar theorem at all genera
This is downstream. It should not be used as foundational motivation until T3--T6 are in place.

## 4. Chriss-Ginzburgification

The book should continue to use the Heisenberg chapter as the atom, but add a second atom for the noncommutative face:
- Heisenberg = commutative/modular atom.
- Yangian evaluation-locus DK square = braided/factorization atom.

Then the narrative becomes inevitable:
1. one atom shows why genus forces modular completion;
2. the other shows why ordered configurations force factorization and braid reversal;
3. the general theorems then appear as the only possible synthesis.

## 5. Technical trilogy

Every new theorem should be written with three simultaneous readings:
- mathematics: exact categorical / homological statement;
- mathematical physics: line operators, KZ/KZB monodromy, factorization, deformation quantization;
- physics: defect OPE, braiding, anomaly, background dependence.

This should not be metaphorical. Each theorem should have a one-paragraph trilogy remark stating what it means on each side.

## 6. Immediate agenda

The fastest source-tree agenda is now:
1. prompt/control cleanup:
   keep Markdown state files and synthesis surfaces synchronized with
   the constitutional MC2 -> MC3/MC4 -> MC5 order;
2. DK linearization:
   keep the staged `DK-0` through `DK-5` ladder explicit, with the
   evaluation locus separated from the downstream category-`O` /
   dg-shifted comparison;
3. package hierarchy:
   keep `\kappa`, `(\Delta_A,\Pi_A)`, and `\Theta_A` separated, and keep
   shifted-symplectic complementarity on the proved side;
4. physics-scope discipline:
   state BRST/bar, Vassiliev, and gauge-theory bridges as genus-`0`
   theorems plus downstream conjectural comparison packages unless the
   all-genera comparison is actually proved.
