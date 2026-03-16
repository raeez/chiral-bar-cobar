# Upgrade memo: modular Koszul / holomorphic-topological programme

## 1. What is already genuinely strong

- The programme has a real core at the intersection of chiral Koszul duality, higher operations in holomorphic-topological QFT, and the bulk/boundary/line triangle.
- Recent source papers support a robust genus-zero/nonlinear apparatus:
  - bulk chiral algebra + boundary modules/A-infinity structure;
  - higher perturbative operations with quadratic consistency;
  - line operators as modules over a Koszul dual A-infinity algebra with dg-shifted Yangian structure;
  - PVA-to-3d gauge theory with Virasoro enhancement to full topological symmetry;
  - logarithmic Fulton–MacPherson compactifications with a genuine degeneration formula.

## 2. What must be corrected immediately

- Separate four distinct objects everywhere: A, B(A), A^i = H^*(B(A)), A^! = (A^i)^\vee.
- Do not present linear duality and bar-cobar inversion as the same operation.
- Correct standard identifications:
  - Com^! = Lie (not coLie).
  - Heisenberg is not self-dual.
  - Vir_c^! should pair with Vir_{26-c}; self-duality is at c=13, not c=26.
  - Sugawara is undefined at critical level k = -h^\vee.
- Relabel all theorem-level claims involving the full universal modular Maurer–Cartan class Theta_A, modular convolution dg Lie algebra, all-genera BV-BRST identifications, shifted Yangian E1-chiral lifts, and physics interpretations unless a complete proof is present.

## 3. Best re-centering of the programme

Replace the old centre of gravity

> “full modular package is already a theorem”

with the sharper two-level picture

1. **Rigorous core:** genus-zero and finite-order higher structures, with exact examples and explicit calculations.
2. **Frontier layer:** a filtered shadow/resonance tower approximating the hypothetical all-genera modular Maurer–Cartan element.

This turns the programme from “overstated universal theorem” into “precise finite-order engine with a credible modular envelope conjecture.”

## 4. Breakthrough mathematics that is actually worth introducing

### 4.1 Shadow Postnikov tower

Define finite truncations Theta_A^{<=r} of the modular deformation problem and obstruction classes

- o_3(A): cubic shadow obstruction,
- o_4(A): quartic shadow obstruction,
- etc.

Interpret kappa, Delta, C_A, Q_A as the first low-order shadows of this tower rather than as pieces of an already-globalized universal Theta_A.

### 4.2 Ambient complementarity as derived Lagrangian geometry under explicit hypotheses

Only claim the derived-Lagrangian complementarity package when the cyclic deformation complex is perfect and admits a nondegenerate pairing. Then the deformation/obstruction packages for A and A^! can be realized as complementary isotropic/Lagrangian sectors inside one formal moduli problem.

### 4.3 Modular resonance classes

Use logarithmic Fulton–MacPherson spaces as the geometric home for clutching-compatible nonlinear shadow classes. The first useful object is a quartic resonance class attached to the quartic shadow cocycle. Its exact modular realization should be stated as a conjectural construction unless the differential form and birational invariance arguments are written in full.

### 4.4 Bulk–boundary–line triangle as the noncommutative frame

Promote the Volume II triangle

- bulk local operators,
- boundary chiral algebra,
- line category = A^!-modules,

into a formal second frame dual to the Heisenberg frame. This should be a theorem only in the perturbative quasi-linear regime already covered by the source papers.

### 4.5 Virasoro locus / topological resonance reduction

Use the Khan–Zeng result as a structural principle: when the PVA has a Virasoro element, the 3d theory becomes fully topological. This is the natural locus where modular completion becomes much more plausible and where the shadow tower should simplify drastically.

## 5. Concrete near-term theorem package

### Theorem A (finite-order complementarity)
For a cyclic Koszul chiral algebra with perfect deformation pairing, the order-r shadow obstruction of A and that of A^! are dual and opposite under the ambient pairing. For r=2 this recovers the scalar characteristic; for r=3,4 it gives cubic and quartic complementarity.

### Theorem B (exact archetypes)
- Heisenberg: the shadow tower truncates at quadratic order (exact Gaussianity).
- affine Kac–Moody: cubic shadow is the first nontrivial correction.
- beta-gamma / boundary-linear LG examples: quartic shadow appears and is explicitly computable.

### Theorem C (holomorphic-topological transport)
In quasi-linear 3d HT theories, perturbative line operators are A^!-modules and their OPE is encoded by a dg-shifted Yangian Maurer–Cartan kernel r(z), with no loop corrections.

### Conjecture D (modular envelope)
The filtered shadow tower integrates to an all-genera modular Maurer–Cartan class whose clutching is governed by logarithmic Fulton–MacPherson degeneration.

## 6. Editorial surgery needed

- Cut theorem inflation. Present a short spine of main results and demote most of the rest to propositions, examples, or conjectural frontiers.
- Remove internal programme jargon from theorematic sections.
- Fence every heuristic physical interpretation.
- Keep the Heisenberg frame, but do not let it stand in for the full programme.
- Make the line/Yangian frame equally explicit, or else present it only as a secondary frame under development.

## 7. Outcome

If this surgery is done, the programme becomes:

- **mathematically sharper** (finite-order rigorous core),
- **more original** (shadow Postnikov tower + modular resonance classes),
- **more believable** (honest about the all-genera frontier),
- **better aligned with current literature** (Francis–Gaitsgory, Gui–Li–Zeng, Costello–Dimofte–Gaiotto, Gaiotto–Kulp–Wu, Khan–Zeng, Dimofte–Niu–Py, Mok).
