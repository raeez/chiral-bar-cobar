# HT CFG^nc Mixed Swiss-Cheese Attack-Heal Synthesis

Date: 2026-04-24.

Scope: second 21-lens attack-heal swarm, run after the CFG 2026 boundary
swarm, on the geometry needed to realize Costello--Francis--Gwilliam-style
methods in a mixed modular holomorphic-topological Swiss-cheese setting. The
active concurrency cap was six.

Primary boundary:
[Costello--Francis--Gwilliam, *Chern--Simons factorization algebras and knot
polynomials*, arXiv:2602.12412, 2026](https://arxiv.org/abs/2602.12412).

Preceding synthesis:
`notes/cfg2026_mixed_modular_swiss_cheese_attack_heal_20260424.md`.

## Verdict

The stable structure is not "CFG generalized to every vertex algebra." It is
a three-lane theory.

1. **Non-conformal HT lane.** A vertex/chiral/factorization algebra without a
   conformal vector can still carry global CFG-analogous constructions:
   framed or coordinate-descended chiral factorization observables, the
   derived chiral center, ordered bar resolutions, line categories, and
   annular Hochschild trace complexes. The output is a mixed
   `SC^{ch,top}` or `E_1^{top} \widehat\otimes E_2^{hol}` object, not a
   locally constant `E_3` algebra.
2. **Conformal or quasi-conformal enhancement lane.** Coordinate descent,
   moduli descent, projective flatness, KZ/KZB, and anomaly formulas require
   extra data. A conformal vector is a strong source of such data, but not the
   only source of curve descent. Topologization requires still more: a
   chain-level or transferred primitive for holomorphic translation.
3. **CFG/RT shadow lane.** CFG 2026 enters only after formal-disk restriction,
   de Rham-horizontal fiber, topologization to a single-colored locally
   constant `E_3` object, a fixed parameter dictionary, all-order deformation
   class comparison, perfect module transport, and framed trace/coend data.

The user's correction is decisive: global HT analogues for non-conformal
vertex algebras are real. The false move is to identify those analogues with
CFG's topological `E_3` Chern--Simons algebra or with Reshetikhin--Turaev
framed-link scalars.

## Swarm Topology

The second swarm used 21 lenses:

1. HT Ran/log geometry.
2. Mixed colored operad.
3. HT BV observables.
4. Relative log geometry.
5. Defects, perfect labels, annular trace.
6. Examples and falsifiers.
7. `CFG^nc` non-conformal architecture.
8. Global HT trace.
9. HT deformation complex and topologization tower.
10. Homotopy and infinity-categorical localization.
11. Bare chiral-to-HT construction.
12. Coordinate descent.
13. HT braid and trace groupoids.
14. Descent obstruction tower.
15. Narrowed `CFG^nc` stability referee.
16. Square-zero non-conformal model theorem.
17. Formal-disk topological-shadow functor.
18. Theorem-stack integrator.
19. Compute/test design.
20. Primary-source boundary.
21. Final convergence referee.

No theorem files were edited in this pass. No builds or tests were run.

## The Geometry To Invent

The carrier is a relative mixed Ran/log object, not a product of unrelated
configuration spaces:

```tex
\operatorname{Ran}^{HT,oc}_{X/S,I}
```

It records:

1. holomorphic closed collisions on the curve `X/S`;
2. ordered locally constant collisions in a topological interval or circle
   `I`;
3. mixed bulk-boundary incidence;
4. line and junction strata when CFG-style Wilson lines are in scope;
5. log-Fulton--MacPherson boundary data;
6. nodal and clutching strata over modular bases;
7. tangential or formal-coordinate sectors when the input is a formal-disk
   vertex algebra rather than a native chiral algebra on `X`.

The local disk model has four visible strata:

```tex
(D_z \times I_t;\; D_z \times \{0\};\; \{0\}\times I_t;\; \{(0,0)\})
```

The corresponding operadic object is a framed stratified extension

```tex
C_*\operatorname{Disk}^{fr,HT}_{3 \supset 2 \supset 1 \supset 0}.
```

Its two-color truncation is the current `SC^{ch,top}` skeleton. The full
CFG-style trace problem needs the line and junction colors as separate
structure, not as a consequence of the two-color operad.

## The Non-Conformal Object

Define the proposed non-conformal package by

```tex
\operatorname{CFG}^{nc}_{X/S}(A)
  =
  (U^{HT}_{X/S}(A), F^\bullet, \operatorname{Perf}^{\omega}(A),
   \operatorname{Tr}^{ann}_{X/S}(A)).
```

This notation is new. It must be introduced as a definition, not cited as an
existing theorem.

The input is not a conformal vertex algebra. The input is an augmented
relative chiral or factorization algebra `A` on `X/S`, or a formal-coordinate
vertex algebra equipped with framed/quasi-conformal descent data. Required
admissibility:

1. complete separated bounded-below filtration `F`;
2. perfect finite graded pieces over `S`;
3. continuous bounded operations;
4. strict Mittag--Leffler finite-window towers;
5. holonomicity per weight when D-modules are used;
6. augmentation `A -> \omega_{X/S}` for reduced bar constructions;
7. Koszul/PBW or coderived control when a dual line algebra is claimed;
8. compact dualizable open sector for line labels;
9. cyclic or Calabi--Yau trace data only when annular, ribbon, or wheeled
   sewing is claimed.

The core object is the relative derived-center pair

```tex
U^{HT}_{X/S}(A)
  =
  (C^\bullet_{ch,X/S}(A,A), A, \mu^{brace}).
```

Here `B(A)` is the resolution engine. It is not the bulk, not `A^!`, and not a
CFG Wilson-line label. The bulk is

```tex
Z^{der}_{ch}(A)=C^\bullet_{ch}(A,A).
```

## Square-Zero Witness

The clean non-conformal witness is a global square-zero chiral algebra.

Let `pi: X -> S` be a smooth relative curve in characteristic zero. Let `M` be
an `S`-perfect holonomic right `D_{X/S}`-module, flat under base change. Put

```tex
A=\omega_{X/S}\oplus M,\qquad \bar A=M,
```

with augmentation `epsilon: A -> \omega_{X/S}` and square-zero multiplication

```tex
\omega\cdot\omega=\omega,\qquad
\omega\cdot m=m\cdot\omega=m,\qquad
m\cdot m'=0.
```

Then `A` is a global augmented chiral algebra on `X/S`, hence a factorization
algebra on `\operatorname{Ran}(X/S)`. Its ordered bar is

```tex
B^{ord}(A)=T^c(s^{-1}M),\qquad d_{\bar B}=0,
```

with deconcatenation coproduct. If `M` is finite perfect, the open-line
Koszul dual is

```tex
A^!_{line}\simeq \widehat T(sM^\vee),
```

and the compact line labels are objects of `\operatorname{Perf}(A^!_{line})`.
The HT bulk is still

```tex
C^\bullet_{ch}(A,A),
```

not the bar coalgebra and not the line dual.

A concrete non-conformal local model is obtained on an elliptic curve with
invariant relative form `alpha`. Take a rank-two flat bundle with basis
`e_0,e_1` and connection

```tex
\nabla e_0=e_1\otimes\alpha,\qquad \nabla e_1=0.
```

Set `M=E\otimes\omega`. Locally the vertex algebra has basis
`1,e_0,e_1`, square-zero ideal, and translation

```tex
T(e_0)=e_1,\qquad T(e_1)=0.
```

Every square-zero candidate stress tensor has trivial zero-mode action, but a
conformal vector would have to realize `L_{-1}=T`. Since `T` is nonzero, this
model carries the global chiral/HT package while having no conformal vector,
no `L_0`, and no stress tensor.

This should be the first theorem to inscribe: fixed-curve and relative-family
`SC^{ch,top}` package proved for the square-zero model; universal moduli
descent, cyclic scalar trace, and CFG trace are add-ons.

## Coordinate And Moduli Descent

A bare formal-disk vertex algebra globalizes first over the coordinate torsor

```tex
\operatorname{Coord}_{\operatorname{Ran}(X)}.
```

Descent to `\operatorname{Ran}(X)` is equivalent to compatible
`Aut(\mathcal O)` or quasi-conformal descent data. A conformal vector gives a
canonical source of such data, but curve descent can also come from a native
BD chiral algebra on `X`, current-algebra covariance, or framed/tangential
structure.

The obstruction tower is:

```tex
o_{\mathbb G_m},\quad
o_+,\quad
o_{Ward},\quad
o_{Cech},\quad
o_{mod}.
```

These record, respectively:

1. failure of an integral semisimple scaling operator;
2. failure of positive coordinate-change operators;
3. failure of Ward identities;
4. failure of local descent data to glue;
5. projective or Hodge anomaly over moduli.

Moduli descent is stronger than curve descent. It asks for compatibility with
families, mapping-class transport, nodal clutching, and anomaly control. The
anomaly may be expressed as `\kappa(A)\lambda_g` in the bar-modular lane or
as a Schwarzian central-charge term in the Virasoro lane; these are not
interchangeable without a comparison theorem.

## HT Trace Groupoid

The global trace is not a scalar invariant.

For a log-smooth modular base `S`, semistable curve `C -> S`, and ordered
log-FM configuration `FM_m^{ord}(C/S)^{log}`, define the HT braid groupoid

```tex
\operatorname{Br}^{HT}_{S,m}(\vec V)
  =
  \Pi_1^{log}(FM_m^{ord}(C/S)^{log}; \partial^{tan})\rtimes\Gamma_S.
```

The HT trace groupoid is its cyclic inertia groupoid:

```tex
\operatorname{Tr}^{HT}_{S,m}(\vec V)
  =
  I(\operatorname{Br}^{HT}_{S,m}(\vec V)).
```

The trace object is a monodromic local system, logarithmic D-module, or
perfect complex:

```tex
\mathcal T^{HT}_{A,\vec V}
  =
  HH^{cyc}_0(H_{\vec V},\nabla^{HT}).
```

It becomes a scalar only after imposing horizontal-section, anomaly-cancelled,
or ribbon/topological quotient data. Markov stabilization is not part of the
HT trace groupoid; it belongs to the later ribbon/CFG specialization.

Collision residues satisfy the infinitesimal braid identities:

```tex
[\Omega_{ij},\Omega_{kl}]=0,\qquad
[\Omega_{ij},\Omega_{ik}+\Omega_{jk}]=0.
```

Nodal residues must be coend sewing laws:

```tex
\operatorname{Res}_e\mathcal T^{HT}_{g,\vec V}
  \simeq
  \int^{L}
  \mathcal T^{HT}_{g_1,\vec V_1,L}
  \otimes
  \mathcal T^{HT}_{g_2,\vec V_2,L^\vee}
```

for separating nodes, and

```tex
\operatorname{Res}_e\mathcal T^{HT}_{g,\vec V}
  \simeq
  \int^{L}
  \mathcal T^{HT}_{g-1,\vec V,L,L^\vee}
```

for nonseparating nodes.

## Topologization Tower

The base HT deformation complex is

```tex
\operatorname{Def}_{HT}(\mathcal F)
  =
  \operatorname{Conv}_{cont}
  ((E_1^{top}\widehat\otimes E_2^{hol})^\ash,
   \operatorname{End}_{\mathcal F}).
```

Topologization is the obstruction problem for solving

```tex
[m_{HT},G]=\partial_z.
```

Modulo `F^{N+1}`, the defect

```tex
D_{N+1}
 =
 \pi_{N+1}([m_{HT},G^{\le N}]-\partial_z)
```

defines an obstruction class

```tex
o_{N+1}
  \in
  H^0(\operatorname{gr}^{N+1}\operatorname{Def}_{HT}(\mathcal F),d_m).
```

All-order topologization means every `o_{N+1}` vanishes and the chosen
primitive converges in the complete filtration. A conformal vector alone is
not enough. One needs a primitive on the original complex or an explicitly
transferred cohomological model.

Only after topologization does one pass from

```tex
E_1^{top}\widehat\otimes E_2^{hol}
```

to a single-colored locally constant

```tex
E_1^{top}\widehat\otimes E_2^{top}\simeq E_3^{top}
```

object. Dunn additivity is not applied to the bicolored `SC^{ch,top}` operad.

## Formal-Disk CFG Shadow

The required shadow functor is not ordinary global sections on the disk. It
has the form

```tex
\mathsf{Sh}^{CFG}_{x,G}
  =
  \operatorname{Loc}_G\circ x^*_{dR}\circ \widehat i_x^!,
```

where `\widehat i_x^!` restricts to the formal disk at `x`,

```tex
x^*_{dR}(-)
  =
  \mathbb C_x\otimes^{\mathbb L}_{\mathcal D_{\widehat D_x}}(-)
```

is the derived de Rham-horizontal fiber, and `\operatorname{Loc}_G` is defined
only when the holomorphic translation primitive has been supplied.

This functor is not faithful on global HT data. It kills or forgets the curve,
genus, marked positions, cross-ratios, FM/log-FM boundary strata, KZ/KZB
connection and monodromy, Stokes sectors, modular anomaly, and coordinate
descent unless equivariance is retained.

The all-order CFG comparison is equality of complete filtered MC classes:

```tex
[\Theta^{E_3}_{HT}]
  =
[\Theta_{CFG}]
\in
\operatorname{MC}(\hbar F^1\operatorname{Def}_{E_3}(C^*(\mathfrak g)))
/ \exp(\hbar F^1\operatorname{Def}^0).
```

It requires:

1. associated graded `C^*(\mathfrak g)`;
2. first-order `P_3` bracket from the invariant pairing;
3. parameter dictionary;
4. chosen formality, associator, and regularization data;
5. equality of every higher `\hbar^n` coefficient.

The shortcut "`\dim H^3(\mathfrak g)=1`, hence equality" is false. It gives
one scalar per order, not equality of scalar series.

## Parameter Dictionary

The comparison must keep the following quantities separate:

```tex
B_{KM}=kB_0,\qquad
h_{KZ}=\frac{1}{k+h^\vee},\qquad
q_{DJ}=\exp(\pi i h_{KZ}),\qquad
q_{Jones}=q_{DJ}^2.
```

Collision and KZ matrices are different:

```tex
r_{coll}=\frac{k\Omega_0}{z},\qquad
r_{KZ}=\frac{\Omega_0}{(k+h^\vee)z}.
```

Do not set the CFG invariant pairing equal to `k+h^\vee` without a
renormalization theorem.

## What Survives

The following claims survive attack:

1. Non-conformal global HT analogues exist for native chiral algebras on
   `X/S`, and for formal-disk vertex algebras after framed or coordinate
   descent data is supplied.
2. The base non-conformal output is an `SC^{ch,top}` derived-center package:
   `(C^\bullet_{ch}(A,A),A)`.
3. The ordered bar `B^{ord}(A)` is the correct resolution/Koszul engine.
4. The line category may be modeled by conilpotent `B(A)`-comodules, or by
   modules over a completed dual `A^!_{line}` under finite-perfect duality.
5. Annular HT traces are Hochschild/coend traces of the open/line category.
6. Global HT traces are monodromic D-modules or perfect complexes over trace
   groupoids, not automatic scalar invariants.
7. Topological `E_3` and CFG/RT appear only after topologization and
   separate CFG comparison gates.
8. The square-zero `A=\omega\oplus M` model is the right first non-conformal
   theorem candidate.

## Claims To Forbid

The swarm rejected the following statements:

1. "Global HT analogues require a conformal vector."
2. "`SC^{ch,top}=E_3` by Dunn additivity."
3. "`B(A)` is the HT bulk."
4. "`A^!` or `A^!_{line}` is a CFG Wilson-line label."
5. "Annular Hochschild trace is the CFG framed-link trace."
6. "A non-conformal chiral algebra has no global construction."
7. "A formal-disk vertex algebra automatically descends to every curve."
8. "`\kappa=0` removes critical-level topologization obstruction."
9. "`\dim H^3(\mathfrak g)=1` proves all-order `E_3` equality."
10. "CFG proves 6d hCS, CY3/Hall/BKM, K3/M5, WRT surgery, or Sugawara
    topologization."

## Theorem Stack

The honest architecture is:

1. **Definition: HT Ran/log geometry.** Construct
   `\operatorname{Ran}^{HT,oc}_{X/S,I}` with holomorphic, topological,
   mixed, line, junction, log-boundary, and nodal sectors.
2. **Definition: framed descent category.** A bare vertex algebra first gives
   a framed/formal-coordinate HT object; descent to `X` is extra
   `Aut(\mathcal O)` or quasi-conformal data unless `A` is already a BD
   chiral algebra on `X`.
3. **Definition: non-conformal HT package.** For augmented filtered
   admissible `A`, define `CFG^{nc}_{X/S}(A)` as the derived-center
   Swiss-cheese pair plus filtration, compact open sector, and annular trace.
4. **Proposition: square-zero theorem.** For finite-perfect holonomic
   `M`, the chiral algebra `\omega\oplus M` has ordered bar
   `T^c(s^{-1}M)`, line dual `\widehat T(sM^\vee)` under finite duality,
   and derived-center `SC^{ch,top}` package, without any conformal vector.
5. **Theorem: derived-center universality.** Prove the completed brace
   operations and terminal open/closed property for
   `(C^\bullet_{ch}(A,A),A)`. Strict `SC^{ch,top}` universality requires the
   two-colored cobar contracting homotopy.
6. **Definition/gate: line defects.** Build the framed `3/1` stratified
   defect operad and restrict labels to compact dualizable/perfect objects.
7. **Theorem/gate: annular trace.** Identify annular factorization homology
   with Hochschild/coend trace under smooth/proper/cyclic hypotheses.
8. **Theorem/gate: modular sewing.** Prove log-FM base change, collision and
   nodal residues, stable-graph clutching, cyclic BV orientation, and
   boundary-of-boundary cancellation.
9. **Theorem/gate: topologization.** Solve the obstruction tower
   `[m,G]=\partial_z`; only then obtain a single-colored `E_3`.
10. **Theorem/gate: CFG comparison.** Apply `\mathsf{Sh}^{CFG}_{x,G}` and
    prove associated-graded, first-order, and all-order MC equality with CFG.
11. **Theorem/gate: RT trace.** Transport perfect labels and trace/coend data
    to the CFG side; then framed-link RT equality is CFG's theorem.

## Test Surface

Future compute work should split the verdict into separate booleans:

```text
local_shadow_pass
annulus_hh_pass
relative_log_fm_pass
cfg_trace_pass
```

The first three may pass for non-conformal or toy finite-rank examples.
`cfg_trace_pass` must remain false unless the CFG-specific fixtures are
present:

1. complete filtered BV Chern--Simons `E_3` algebra;
2. semisimple finite-dimensional `\mathfrak g`;
3. parameter dictionary;
4. de Rham-horizontal formal-disk shadow;
5. all-order MC-class comparison if isomorphism is claimed;
6. perfect Drinfeld--Jimbo module label;
7. evaluation and coevaluation maps;
8. framed link;
9. trace/coend and ribbon normalization.

Minimal fixtures:

1. `NoConformalVectorFixture`.
2. `FiniteRankSquareZeroChiralAlgebraFixture`.
3. `InfiniteRankFalsifier`.
4. `FormalDiskTopologicalShadowGate`.
5. `AnnulusHHTraceFixture`.
6. `RelativeBaseChangeFixture`.
7. `LogFMResidueIdentityFixture`.
8. `TopologizationObstructionTowerFixture`.
9. `CFGComparisonGateSuite`.

## Source Boundary

Grounded elsewhere:

1. BD supports chiral algebras on curves, Ran/factorization, and chiral
   homology.
2. FBZ/Cliff-style formal-coordinate and quasi-conformal descent supports the
   coordinate torsor lane.
3. Costello--Gwilliam supports perturbative BV observables and factorization
   algebras.
4. Ayala--Francis--Rozenblyum supports stratified factorization-homology
   language for defect scaffolding.
5. Lurie/Dunn supports `E_m \otimes E_n \simeq E_{m+n}` only after
   one-colored local constancy.
6. KZ/KZB/TUY/Hitchin support conformal-block flat or projectively flat
   connections in their standard regimes.
7. CFG 2026 supports exactly ordinary real 3d Chern--Simons filtered `E_3`,
   perfect Drinfeld--Jimbo modules, and framed-link RT traces.

New or conditional here:

1. `CFG^{nc}_{X/S}(A)` as a named package.
2. `\operatorname{Ran}^{HT,oc}_{X/S,I}` with the full mixed modular
   Swiss-cheese/log/defect boundary.
3. The square-zero non-conformal HT theorem in the form above.
4. The global HT trace groupoid and D-module/perfect-complex trace theorem.
5. The topologization obstruction tower as the gate from HT to `E_3`.
6. The all-order comparison between topologized derived chiral centers and
   CFG deformation classes.

## Immediate Inscription Targets

1. Inscribe the square-zero theorem in a theorem file, because it gives the
   first clean non-conformal global witness.
2. Split any existing CFG comparison surface into:
   associated-graded/first-order comparison, conditional all-order comparison,
   and separate RT trace theorem.
3. Replace naive `\Gamma(\widehat D,-)` claims with the de
   Rham-horizontal fiber functor.
4. Add test fixtures with separate `local_shadow_pass`,
   `annulus_hh_pass`, `relative_log_fm_pass`, and `cfg_trace_pass` flags.
5. Keep every theorem lane ambient-qualified: non-conformal HT,
   coordinate/conformal enhancement, topologized `E_3`, and CFG/RT shadow.

