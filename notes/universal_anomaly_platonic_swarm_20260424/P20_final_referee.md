# P20 final adversarial referee report

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P20_final_referee.md`

Read-only surfaces:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
- `standalones/universal_anomaly_voa_explicit_supplement.tex`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex`
- available reports `P01` through `P16` in this directory
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`

No target TeX files were edited.

## Referee recommendation

Major revision. The paper is worth developing. It is not yet a proved
paper in its current TeX surface.

The platonic paper is real:

```tex
\title[Atiyah--Connes obstruction]
{The Atiyah--Connes obstruction to chiral bar--cobar specialisation}
```

Its first theorem should not be a universal pentagon, a four-climax
identity, or a K3/Igusa conclusion. Its first theorem should be the
construction, in a fixed cyclic-HKR datum, of a class

```tex
\alpha_X \in H^2(X,\Omega_X^1)=H^{1,2}(X)
```

and the first new theorem should be the comparison

```tex
\operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C)
\in H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
```

That theorem would be new and deep. The manuscript currently contains
the architecture of that theorem, but it has not yet proved it.

## Findings

### CRITICAL 1. The core class is still conditional, not fully constructed

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:223`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:248`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:461`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:480`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:513`
- `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md:89`

The manuscript writes a cochain operator `B^{(2)}`, a negative-cyclic
home, a commutator, and an HKR target. These are not yet one defined
mathematical object. Connes' primary operator is a chain operator. The
cochain BV/rotation operator requires a cyclic Calabi--Yau trace,
suspension convention, total grading, and sign rule. The current text
uses `B^{(2)}` as chain Connes operator, cochain rotation, cyclic-skew
projection, framed `E_2` circle action, and motivic class.

The target also needs a missing route:

```tex
\HH^4(X) \to H^2(X,\wedge^2 T_X)
\xrightarrow{\iota_{(-)}\Omega_X} H^2(X,\Omega_X^1).
```

The raw Dolbeault tensor

```tex
\bar\partial\nabla\wedge\bar\partial\nabla
```

does not by itself land in `\Omega_X^1`; it must pass through an
explicit trace/cyclic projection and Calabi--Yau contraction.

Required fix: insert a definition of a cyclic-HKR datum

```tex
\mathfrak C_X=(\Perf_{\mathrm{dg}}(X),\Tr_{\mathrm{cyc}},
\Delta_2,\HKR_{\mathrm{cyc}},\pi^{\HKR}_{2,2},\iota_{\Omega_X})
```

where `\Delta_2` is the transported cochain Connes operator. Define the
negative-cyclic or BV mixed complex, total degree, signs, corrected HKR
normalisation, projection to `H^2(\wedge^2T_X)`, and contraction to
`H^2(\Omega^1_X)`. Only after that may the paper call `\alpha_X`
constructed.

### CRITICAL 2. The main theorem has no native derived-loci machine

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:744`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:767`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:781`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:784`
- `notes/universal_anomaly_platonic_swarm_20260424/P05_derived_loci_category.md:9`

The manuscript now correctly says the pentagon is conditional, but it
still has no base stack, obstruction complex, zero locus, or witness
sheaves. "Derived loci" is not yet a theorem.

The native base should be a derived analytic stack of anomaly data

```tex
\mathcal B=
\mathcal M^{\Omega,\mathrm{cyc},\Sigma,C,L,\mathrm{tr}}_{\mathrm{CY}_3}(M),
```

with universal family `\pi:\mathcal X\to\mathcal B`, obstruction
complex

```tex
\mathbb E_{\mathrm{AC}}=R\pi_*\Omega^1_{\mathcal X/\mathcal B}[2],
```

section `\alpha_{\mathrm{AC}}`, and derived zero locus
`\mathbf Z_\alpha=\mathbf Z(\alpha_{\mathrm{AC}})`.

The comparison vertices should be derived loci or witness sheaves

```tex
\mathbf Z_{\mathrm{BC}},\quad
\mathbf Z_{\mathrm{FA}},\quad
\mathbf Z_{\Delta_5},\quad
\mathbf Z_{\mathrm{tr}},
```

with comparison maps from `\mathbb E_{\mathrm{AC}}` to their obstruction
complexes. `Pr^L_k` appears only after applying `QCoh` or `IndCoh` to
proved-equivalent loci.

Required fix: add the P05 derived-loci definitions before the bridge
theorem, or remove derived-loci language entirely.

### CRITICAL 3. The Positselski bridge target is undefined and too large

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:767`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:772`
- `notes/universal_anomaly_platonic_swarm_20260424/P02_positselski_bridge.md:14`
- `notes/universal_anomaly_platonic_swarm_20260424/P13_vol1_theoremAB_consistency.md:257`

The theorem maps to

```tex
\mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C),
```

but no such object is defined. The Vol I native target is the
genus-zero arity-three part of the completed modular cyclic deformation
complex:

```tex
H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
```

Here

```tex
A_C=\Sp^{\mathrm{ch}}_{\Sigma,C}(\Phi^{\mathrm{FA}}_3(\Perf_{\mathrm{dg}}(X))).
```

Vanishing of `\alpha_X` can kill at most the first obstruction
`o^{(0)}_3(A_C)`, once the comparison is proved. It does not imply
full Koszulness, strict Theorem B, or the vanishing of all higher
`o^{(0)}_{r+1}`. Full Theorem B still needs a Koszul/PBW hypothesis, a
completed Positselski hypothesis, or a new all-higher closure theorem.

Required fix: replace B1 by the exact comparison

```tex
\operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C)
\in H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
```

Then state the bar--cobar consequence only after independent
higher-obstruction closure.

### CRITICAL 4. `K3 x E` is not a zero witness; it is probably the first falsifier

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:908`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:947`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1313`
- `notes/universal_anomaly_platonic_swarm_20260424/P08_k3e_cyclic_projection.md:18`

The corrected product computation is:

```tex
H^2(S\times E,\Omega^1)
= H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E)
\oplus H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1),
```

of dimensions `20+1`. Product naturality kills the `20`-dimensional
mixed summand, but leaves the scalar line

```tex
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
```

Under standard Atiyah/Chern-Weil/Rozansky-Witten normalisation this
scalar should be proportional to

```tex
\int_S c_2(T_S)=24,
```

hence non-zero unless the final cyclic-HKR convention imposes a
trace-free projection.

Required fix: replace every use of raw `K3 x E` as an admissible
vanishing witness by the product-reduction theorem

```tex
\alpha_{S\times E}
=\lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)\,
[\bar\sigma_S]\otimes\eta_E,
\qquad
\alpha_{S\times E}=0 \Longleftrightarrow \lambda_{\mathrm{Cyc}}=0.
```

Then compute `\lambda_{\mathrm{Cyc}}`. Until that scalar is zero, the raw
product is not in the zero locus.

### CRITICAL 5. The Vol III K3 theorem is mis-stated in the standalone

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:352`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:355`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:359`
- `notes/universal_anomaly_platonic_swarm_20260424/P15_vol3_k3_chiral_bialgebra.md:76`

The theorem-grade Vol III input is not

```tex
\Phi_3(K3)=\mathbf H_{\Delta_5}.
```

`K3` is CY2, not CY3. The Vol III surface is the principal-locus
specialisation

```tex
\SpCh_{K3,E}(\PhiFA_3(\Perf(K3\times E)))
\simeq \mathbf H_{\Delta_5}
```

as an `E_1`-chiral bialgebra on `E`, with Vol III comparison witnesses
installed. This does not prove `\alpha_{K3\times E}=0`.

Required fix: replace the K3 theorem with the precise principal
`K3 x E` statement. Split constants:

```tex
\kappa_{\mathrm{BKM}}(\Delta_5)=5,\qquad
\Phi_{10}=\Delta_5^2,\qquad
K_{\mathrm{Muk}}=2c_+(\widetilde H(K3,\mathbb Z))=8.
```

The value `8` is the Mukai conductor, not the BKM weight and not a
vanishing theorem.

### CRITICAL 6. The Malcev face is false in the main CY3 lane

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:685`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:689`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:703`
- `notes/universal_anomaly_platonic_swarm_20260424/P11_malcev_configuration.md:15`

For a simply connected smooth complex threefold `X`, the diagonals in
`X^3` have complex codimension `3`, hence real codimension `6`.
Loops and null-homotopies avoid them. Therefore

```tex
\pi_1(\mathrm{Conf}_3(X))=0.
```

The Malcev completion of `pi_1` is trivial. There is no nontrivial
weight-three Malcev `pi_1` central extension to compare with
`\alpha_X`.

The Arnold one-forms `dlog(z_i-z_j)` are curve/formal-disk objects. For
a complex threefold the Kriz-Totaro diagonal generators have degree
`2 dim_C X - 1 = 5`, not degree `1`.

Required fix: delete `thm:malcev-quillen` and `cor:pi1-motivic`, or
replace them with a conjectural Kriz--Quillen rational-homotopy
comparison:

```tex
\Xi_X:\Def^{E_3,\mathrm{cyc}}(\Perf_{\mathrm{dg}}(X))\to\Der(K_X(3)).
```

No `H^3_{\mathrm{Malcev}}\cong H^3_{\mathcal M}(X,\mathbb Q(2))`
statement should remain.

### CRITICAL 7. The motivic lift is in the wrong direct cohomology group

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:536`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:540`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:624`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:637`
- `notes/universal_anomaly_platonic_swarm_20260424/P10_motivic_regulator.md:15`

The direct motivic home for an `H^{1,2}` obstruction is not

```tex
H^3_{\mathcal M}(X,\mathbb Q(2))=\mathrm{CH}^2(X,1)_{\mathbb Q}.
```

That regulator lands in `H^3_D(X,Q(2))`, governed by
`F^2H^3=H^{3,0}\oplus H^{2,1}`. The natural Abel--Jacobi surface for an
`H^{1,2}` tangent component is codimension-two motivic cohomology in
degree four:

```tex
Z_\alpha(X)\in H^4_{\mathcal M}(X,\mathbb Q(2))_{\mathrm{hom}}
=\mathrm{CH}^2(X)_{\mathrm{hom},\mathbb Q},
```

with normal function infinitesimal invariant equal to `\alpha_X`.

The "torsion graph of the Chern connection" is not an algebraic higher
Chow cycle, and the claim that `B^{(2)}` lifts to `Pic(X)_Q` is
unsupported.

Required fix: replace the motivic subsection by the conjecture

```tex
\delta AJ(Z_\alpha)=\alpha_X
```

for a homologically trivial codimension-two cycle. Move any
`CH^2(X,1)` material to a secondary transgression remark.

### SERIOUS 8. The graph, Duflo, and strict-formality claims still overstate constants

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:568`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:590`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:603`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:663`
- `notes/universal_anomaly_platonic_swarm_20260424/P09_graph_duflo_formality.md:23`

The constants `1/(2*pi^2)`, `1/(4*pi^2)`, and `1/12` are not justified
in one convention. A Tate twist does not convert a graph period into a
Duflo/Todd Bernoulli coefficient. Vanishing of one Taylor coefficient
`U_2` also does not imply strict `E_3` formality; strictification is a
full obstruction-tower problem.

Required fix: replace constants by convention-dependent scalars
`c_{\mathrm{tri}}(F)`, `c_{\mathrm{wheel}}(F)`, and
`c_{\mathrm{Duf}}`. Move graph/Duflo/formality to frontier unless the
graph complex, orientation convention, stable formality datum, cyclic
operator transport, HKR/Todd normalisation, and higher obstruction tower
are all supplied.

### SERIOUS 9. The factorisation/hCS bridge remains theorem-shaped before its proof

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:283`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:810`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:823`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:841`
- `notes/universal_anomaly_platonic_swarm_20260424/P03_factorization_hcs_bridge.md:42`

The manuscript still writes stage one as a global `Pr^L` functor and a
left adjoint more strongly than Vol III permits. The hCS theorem begins
conditionally but then says the BRST descent "produces" the
Atiyah--Connes class. That equality is the B2 bridge, not a proof step.

Required fix: make the factorisation object relative to fixed formality
and parametrix data `(F,P)`. State Weiss descent, BV/HKR comparison,
local BRST generation, and non-renormalisation as explicit hypotheses.
Move Adler--Bardeen/hCS into frontier unless those hypotheses are proved.

### SERIOUS 10. The quintic proves a target and detector, not nonzero `\alpha`

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:868`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1207`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1343`
- `notes/universal_anomaly_platonic_swarm_20260424/P07_hodge_quintic_falsifier.md:15`

For a quintic threefold,

```tex
H^{2,1}(Q_f)\cong R_f^5,\qquad
H^2(Q_f,\Omega^1_{Q_f})=H^{1,2}(Q_f)\cong R_f^{10}.
```

Both have dimension `101`. The Yukawa tensor proves nontrivial cubic
variation of Hodge structure and a nonzero detector pairing
`R_f^{10}\otimes R_f^5\to R_f^{15}`. It does not prove

```tex
\alpha_{Q_f}\ne0.
```

Required fix: in the summary table change `Q_5` from "no
(`101`-dim)" to "unknown/conditional; target `101`-dim". State a new
open problem: compute the Griffiths residue image

```tex
\Psi_f(\alpha_{Q_f})\in R_f^{10}.
```

### SERIOUS 11. The arithmetic lane has a true constant core but the nine-list is open

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1097`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:54`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:587`
- `notes/universal_anomaly_platonic_swarm_20260424/P16_heegner_bruinier_chenevier.md:9`

The true constant core is:

```tex
\operatorname{sig}\widetilde H(K3,\mathbb Z)=(4,20),\quad
c_+=4,\quad K_{\mathrm{Muk}}=2c_+=8,\quad
\Phi_{10}=\Delta_5^2.
```

The classical fundamental class-number-one discriminants are

```tex
\{3,4,7,8,11,19,43,67,163\}.
```

The proposed list

```tex
\{3,4,7,8,11,15,19,20,24\}
```

is, as currently justified, only the finite set of fundamental negative
discriminants with `d<=24` and class number at most `2`. It is not a
Bruinier--Chenevier theorem in the manuscript. Bruinier supplies
Heegner-divisor Chern-class and Borcherds-product technology; it does
not force `K=8`, `hbar^2=-1/8`, or the nine-list. Chenevier determinant
theory does not select the nine discriminants without a residual
pseudodeformation datum and comparison map.

Required fix: either revert to the classical list, or define an explicit
rank-8 admissibility predicate `\mathcal C_8(d)` and prove its solution
set. Downgrade all arithmetic VOA statements to conjectural candidates.

### SERIOUS 12. The architecture still hides the theorem

Local anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:78`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:86`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:286`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:423`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1138`
- `notes/universal_anomaly_platonic_swarm_20260424/P06_architecture_voice.md:20`

The comparison vertices still appear before the obstruction is built.
The motivic/graph/Duflo/Malcev faces appear inside the construction
section. The supplements are inserted before open questions. This makes
evidence and frontier material read as proof.

Required fix: reorder the paper:

1. Setup.
2. Cyclic-HKR datum.
3. Atiyah--Connes class.
4. Hodge target and curve falsifier.
5. Derived zero locus.
6. Comparison targets.
7. Conditional bridge.
8. Geometric tests: quintic, `K3 x E`, Clemens.
9. Elementary curve-side models.
10. Frontier realisations: motivic, graph/Duflo, hCS, configuration.
11. Open problems.
12. Appendices: VOA and arithmetic supplements.

Use "comparison target", "obstruction", "derived zero locus",
"conditional bridge", and "frontier realisation". Remove manuscript
titles such as "four climaxes", "ten minutes", and "load-bearing
computations".

## What must be fixed before development

Development is safe only if the next version makes these cuts:

1. Define the cyclic-HKR datum and make `\alpha_X` a class in a precise
   complex. If that cannot be done immediately, every occurrence of
   "proved class" becomes conditional.
2. Replace B1's undefined obstruction target by
   `H^2(\pi_{3,0}\Defcyc^{mod}(A_C))`.
3. Prove or explicitly assume
   `\operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C)`.
4. Separate first-obstruction vanishing from full Theorem B.
5. Insert the P05 derived-loci base/zero-locus architecture, or stop
   saying "derived loci".
6. Replace raw `K3 x E` vanishing by the scalar computation
   `\lambda_{\mathrm{Cyc}}`.
7. Move motivic, graph, Duflo, Malcev/configuration, hCS, arithmetic VOA,
   and all-loop material to frontier sections unless their exact
   hypotheses are imported.
8. Correct stale references to `thm:main(i)`, `(iii)`, `(iv)`, and any
   "equivalence of (i) and (iv)" language.

## What is genuinely new

Not new:

- `H^2(X,\Omega_X^1)=H^{1,2}(X)` on Kahler `X`.
- `H^2(C,\Omega_C^1)=0` for a smooth curve.
- The quintic Jacobian-ring dimension `101`.
- Mukai signature `(4,20)` and `c_+=4`.
- `\Phi_{10}=\Delta_5^2` in the Igusa/Gritsenko--Nikulin lane.

New if proved:

```tex
\operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C).
```

This would identify a global CY3 cyclic-HKR/Atiyah obstruction with the
first genus-zero curve-side chiral bar--cobar obstruction after
two-stage specialisation. I do not know a standard theorem that says
this. It is the paper's real mathematical claim.

New and deeper, but still conjectural:

- the equivalence of the Atiyah--Connes zero locus with the Positselski,
  factorisation, K3/Igusa, and trace loci;
- the motivic normal-function lift with infinitesimal invariant
  `\alpha_X`;
- the graph/Duflo realisation with computed constants;
- the K3/Mukai trace return edge;
- the all-higher closure theorem making first obstruction vanishing
  imply full chiral Koszulness.

## Is it deep?

Yes, if narrowed. The depth is not the pentagon. The depth is the
possibility that one cyclic-HKR class on a CY3 controls the first
curve-side chiral bar obstruction after factorisation homology. That
would connect Atiyah/Kapranov geometry, Connes cyclic rotation,
Calabi--Yau factorisation, and Vol I chiral Koszul duality through a
single obstruction calculation.

The K3/Igusa, motivic, graph, hCS, and arithmetic faces are deep
frontier satellites. They should orbit the obstruction theorem; they
should not be used to prove it.

## The theorem to prove first

Prove this theorem before developing any other face.

```tex
\begin{theorem}[First bar--cobar obstruction comparison]
Let \(X\) be a smooth projective Calabi--Yau threefold with cyclic-HKR
datum \(\mathfrak C_X\), let
\[
  \alpha_X\in H^2(X,\Omega_X^1)
\]
be the Atiyah--Connes class, and let
\[
  A_C=
  \Sp^{\mathrm{ch}}_{\Sigma,C}
  \Phi^{\mathrm{FA}}_3(\Perf_{\mathrm{dg}}(X))
\]
be the curve-side chiral algebra. Assume stage-two specialisation
induces a filtered morphism of cyclic deformation complexes
\[
  d\Sp^{\mathrm{ch}}_{\Sigma,C}:
  \Def^{E_3,\mathrm{cyc}}(\Phi^{\mathrm{FA}}_3(X))
  \to
  \Defcyc^{\mathrm{mod}}(A_C)
\]
preserving the bar-length and genus filtrations. Let \(\pi_{3,0}\)
denote projection to arity three and genus zero. Then
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)
  :=
  \pi_{3,0}d\Sp^{\mathrm{ch}}_{\Sigma,C}(\alpha_X)
  =
  o^{(0)}_3(A_C)
  \in H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
\]
Consequently \(\alpha_X=0\) kills the first genus-zero chiral
bar--cobar obstruction of \(A_C\).
\end{theorem}
```

This theorem is hard enough. It is also the narrowest theorem that makes
the paper unquestionably new.

Proof path:

1. Construct `\alpha_X` through `\beta_X\in H^2(\wedge^2T_X)` and the
   CY contraction.
2. Define the cyclic `E_3` deformation complex of the stage-one
   factorisation object.
3. Define the completed modular cyclic deformation complex of `A_C`.
4. Prove that stage-two specialisation differentiates to a filtered map
   between these complexes.
5. Compute the arity-three genus-zero component locally on a collision
   screen and identify the transported Connes rotation with cyclic
   symmetry of the bar coderivation.
6. Check signs against the fixed cyclic-HKR datum.
7. Conclude only `o^{(0)}_3=0`; do not claim higher obstructions vanish.

## Exact edits that would make the paper elite

1. Rename the title to "The Atiyah--Connes obstruction to chiral
   bar--cobar specialisation".
2. Replace the abstract with four claims: cyclic-HKR datum; Hodge target;
   curve falsifier; conditional comparison bridge.
3. Insert `\begin{definition}[Cyclic-HKR datum]` before the current
   Connes/m3 construction.
4. Replace `B^{(2)}` by `\Delta_2` until the cochain Connes convention is
   fixed; then define `B^{(2)}:=\Delta_2`.
5. Replace Construction `constr:cocycle` by the route
   `\gamma_X=[m_3,\Delta_2]`, `\beta_X=\pi^{HKR}_{2,2}([\gamma_X])`,
   `\alpha_X=\iota_{\beta_X}\Omega_X`.
6. Replace the connection-independence proof by the Ext-class argument:
   the Atiyah class is the jet-extension class; connections are
   representatives.
7. Split `thm:main` into `thm:atiyah-connes-obstruction` and
   `thm:atiyah-connes-bridge`.
8. Replace B1 by the exact `Defcyc^{mod}` target and `o^{(0)}_3`.
9. Add the P05 base stack, obstruction complex, section, and derived zero
   locus before the bridge.
10. Rewrite the four "climax" statements as "comparison targets".
11. Replace `\Phi_3(K3)` by the principal `K3 x E` Vol III
    specialisation theorem.
12. Replace the DVV theorem by a protected-index scalar theorem:
    `Z^{K3\times E}_{BPS}=\Phi_{10}^{-1}=\Delta_5^{-2}`.
13. Replace raw `K3 x E` vanishing with the scalar
    `\lambda_{\mathrm{Cyc}}`.
14. Split the quintic section into a proved Jacobian/Yukawa detector and
    an open Atiyah--Connes residue computation.
15. Delete the Malcev `pi_1` theorem; replace by a conjectural
    Kriz--Quillen rational-homotopy comparison.
16. Replace the motivic lift by an Abel--Jacobi normal-function
    conjecture in `CH^2(X)_{hom,Q}`.
17. Replace graph/Duflo numerical constants by convention-dependent
    scalars until the integrals are computed.
18. Replace strict-formality proof by a higher-obstruction tower.
19. Move hCS/Adler--Bardeen to frontier with hypotheses `(F1)--(F5)`.
20. Move both supplements after open questions under an appendix, or
    demote their top-level sections.
21. Replace "canonical arithmetic VOA" by "candidate arithmetic VOA" until
    the Bruinier/Chenevier coefficient-sign computation and class-group
    action are built.
22. Add the standalone to metadata extraction or maintain a separate
    claim map; otherwise status drift will recur.

## Final split

Proved or elementary in the current surface:

- corrected Hodge target once the class exists:
  `H^2(X,\Omega_X^1)=H^{1,2}(X)`;
- curve coherent target vanishing: `H^2(C,\Omega_C^1)=0`;
- quintic target and Yukawa detector;
- raw `K3 x E` target decomposition `20+1`;
- Mukai signature and `K_{\mathrm{Muk}}=8` after the paper's conductor
  convention;
- `\Phi_{10}=\Delta_5^2`.

Conditional and worth proving:

- construction of `\alpha_X` in a precise cyclic-HKR datum;
- first bar--cobar obstruction comparison;
- factorisation/hCS anomaly comparison;
- derived-loci equivalence of bridge vertices;
- `K3 x E` scalar `\lambda_{\mathrm{Cyc}}`;
- quintic residue `\Psi_f(\alpha_{Q_f})`.

Conjectural or frontier:

- five-vertex pentagon;
- motivic normal function;
- graph/Duflo constants;
- Malcev/configuration rational-homotopy realisation;
- all-higher closure;
- rank-8 nine-discriminant arithmetic and arithmetic VOAs.

Development verdict: yes, develop it. But develop the first-obstruction
comparison theorem. Everything else should be evidence, frontier, or
appendix until that theorem closes.
