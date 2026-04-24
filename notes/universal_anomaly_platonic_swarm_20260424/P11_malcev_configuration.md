# P11: Malcev and Configuration-Space Face

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P11_malcev_configuration.md`

Read-only target surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`

No target TeX file was edited.

## Verdict

The Malcev/configuration-space face should be removed from the theorem
lane in its present form.

The paper currently asserts a conditional equality
\[
  \mu_3 \equiv [m_3,B^{(2)}]_X
  \quad\text{in}\quad
  H^3_{\mathrm{Malcev}}(B^{\mathrm{ord}}(A),\mathbb Q)
  \cong H^3_{\mathcal M}(X,\mathbb Q(2)).
\]
This statement does not survive source-level attack.  There are three
independent fatal failures.

1. For the main simply connected Calabi-Yau threefolds, the ordered
   configuration space `Conf_3(X)` is simply connected.  Its Malcev
   completion of `pi_1` is therefore trivial.
2. The Arnold degree-one logarithmic generators `eta_ij=dlog(z_i-z_j)`
   are the curve/formal-disk model.  For a complex threefold, the
   Kriz-Totaro-Bezrukavnikov generator attached to the diagonal has
   degree `2 dim_C X - 1 = 5`, with differential the diagonal class.
3. Deligne-Goncharov's motivic fundamental group is a mixed Tate
   unipotent `pi_1` construction for unirational/mixed Tate situations,
   especially punctured projective lines.  It does not give a canonical
   isomorphism from Malcev cohomology of `Conf_n(X)` for a general CY3
   to `H^3_M(X,Q(2))`.

There is still a real frontier face, but it is not a Malcev `pi_1`
theorem.  It is a conditional Quillen/Kriz configuration-space
rational-homotopy comparison:
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1)
  \quad\leadsto\quad
  \text{a weight-three derivation class of the Kriz model of }
  \mathrm{Conf}_3(X).
\]
That comparison may be deep.  It has not been proved in the standalone.

## Local anchors

- Malcev subsection:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:685`.
- Current theorem:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:689`.
- Current equality with motivic cohomology:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:691`.
- Current proof invoking Bezrukavnikov, Kriz, Quillen, and
  Deligne-Goncharov:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:698`.
- Motivic `pi_1` corollary:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:703`.
- Five-face table:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:725`.
- Local configuration-space chapter, Arnold relation and genus split:
  `chapters/theory/configuration_spaces.tex:803`.
- Local configuration-space chapter, Totaro/Kriz/Bezrukavnikov model:
  `chapters/theory/configuration_spaces.tex:1170`.
- P01 cyclic-HKR report:
  `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md:1`.
- P02 Positselski bridge report:
  `notes/universal_anomaly_platonic_swarm_20260424/P02_positselski_bridge.md:1`.
- P10 motivic/regulator report:
  `notes/universal_anomaly_platonic_swarm_20260424/P10_motivic_regulator.md:1`.

## Primary-source anchors checked

- Quillen, *Rational homotopy theory*, Ann. Math. 90 (1969), 205-295:
  algebraic models for rational homotopy via differential graded Lie
  algebras.  The Annals page records the article and DOI
  `10.2307/1970725`.
- Kriz, *On the rational homotopy type of configuration spaces*, Ann.
  Math. 139 (1994), 227-237: the Annals page records the paper and DOI
  `10.2307/2946581`.
- Totaro, *Configuration spaces of algebraic varieties*, Topology 35
  (1996), accessible from Totaro's UCLA page.  This gives the
  diagonal-generator model and degeneration statement used locally.
- Bezrukavnikov, *Koszul DG-algebras arising from configuration
  spaces*, GAFA 4 (1994), 119-135.  EUDML records the keywords
  "configuration space, rational model, Poincare-Birkhoff-Witt,
  Mal'tsev nilpotent completion".
- Hain, *The de Rham homotopy theory of complex algebraic varieties I*,
  K-Theory 1 (1987), 271-324: mixed Hodge/de Rham rational homotopy
  and unipotent completion technology, not the specific equality in
  the target theorem.
- Deligne-Goncharov, *Groupes fondamentaux motiviques de Tate mixte*,
  Ann. Sci. ENS 38 (2005), 1-56: mixed Tate motivic unipotent
  fundamental groups.  The text is explicitly about mixed Tate motives
  and motivic fundamental groups "rendus unipotents"; it does not
  supply the CY3 comparison asserted in the standalone.

## Attacks

### Critical 1: `pi_1 Conf_3(X)` is trivial in the main CY3 case

Let \(X\) be a simply connected smooth complex threefold.  Then
\[
  \mathrm{Conf}_3(X)
  =
  X^3\setminus(\Delta_{12}\cup\Delta_{13}\cup\Delta_{23}).
\]
The ambient \(X^3\) is simply connected.  Each pairwise diagonal has
complex codimension \(3\), hence real codimension \(6\).  By
transversality, any loop in \(X^3\) and any null-homotopy disk can be
homotoped rel boundary to avoid the union of these diagonals, since the
domain dimensions are \(1\) and \(2\), strictly below real codimension
\(\ge 3\).  Therefore
\[
  \pi_1(\mathrm{Conf}_3(X))\cong \pi_1(X^3)=0.
\]
The Malcev completion of \(\pi_1(\mathrm{Conf}_3(X))\) is trivial.
There is no nontrivial weight-three central extension of this Malcev
`pi_1` to obstruct.

This kills the current statement as a theorem about generic quintics
and other simply connected CY3s.  If \(X=K3\times E\), then \(X\) is
not simply connected and also fails the paper's strict Hodge
hypotheses.  That product cannot be used to rescue the main CY3
Malcev theorem without first changing the base object.

### Critical 2: the Arnold one-forms are the wrong generators on a CY3

The forms
\[
  \eta_{ij}=d\log(z_i-z_j)
\]
are global on the affine line/formal disk and locally on a curve
collision screen.  They are not global forms on
\(\mathrm{Conf}_3(X)\) for a general projective CY3.

The Kriz-Totaro model for a compact smooth complex variety of complex
dimension \(d\) has diagonal-linking generators \(g_{ij}\) of degree
\[
  |g_{ij}|=2d-1
\]
and differential
\[
  d g_{ij}=p_{ij}^*[\Delta_X].
\]
For a CY3 this gives \(|g_{ij}|=5\), not \(1\).  The generalized
Arnold relation remains present as a relation among the \(g_{ij}\), but
it lives in the diagonal CDGA model, not in the pure-braid degree-one
Orlik-Solomon algebra.

Thus the displayed secondary Arnold expression
\[
  \langle\eta_{12},\eta_{23},\eta_{31}\rangle
\]
is not a CY3 configuration-space class.  It is at best a curve-side or
formal-screen class.  To compare it with \(\alpha_X\), the paper needs
the stage-two specialization morphism of P02, not a direct
Kriz-Bezrukavnikov citation.

### Critical 3: Quillen rational homotopy is not a Malcev `pi_1`
classification in this case

Quillen's theorem supplies a differential graded Lie model for rational
homotopy, especially for simply connected spaces.  In the simply
connected CY3 configuration-space case, the relevant object is the
Quillen dg Lie algebra of \(\mathrm{Conf}_3(X)\), whose homology
records higher rational homotopy groups and Whitehead products.

That is different from a central extension of the Malcev completion of
\(\pi_1\).  The present theorem conflates:

- the Quillen dg Lie model of a simply connected configuration space;
- the Malcev Lie algebra of a nontrivial fundamental group;
- the ordered chiral bar complex \(B^{\mathrm{ord}}(A)\);
- motivic cohomology of \(X\).

Those objects can be compared only after writing explicit filtered
maps between their complexes.  No such maps are present.

### Critical 4: Deligne-Goncharov does not give the displayed motivic isomorphism

The theorem states
\[
  H^3_{\mathrm{Malcev}}(B^{\mathrm{ord}}(A),\mathbb Q)
  \cong
  H^3_{\mathcal M}(X,\mathbb Q(2)).
\]
This is not a consequence of Deligne-Goncharov 2005 Proposition 5.27.
Deligne-Goncharov is a mixed Tate motivic unipotent fundamental-group
construction.  Its natural examples are rational or mixed Tate
varieties such as punctured projective lines.  A general Calabi-Yau
threefold is not mixed Tate, and \(\mathrm{Conf}_3(X)\) is not in the
scope of the displayed mixed Tate `pi_1` construction.

P10 also shows that \(H^3_{\mathcal M}(X,\mathbb Q(2))\) is not the
right direct regulator home for an \(H^{1,2}\)-valued obstruction.
Even if a motivic comparison existed, this is not the target as written.

### Serious 1: the Bezrukavnikov/Kriz citation is over-read

Kriz, Totaro, and Bezrukavnikov give configuration-space rational
models.  They do not identify those models with the ordered chiral bar
complex of an arbitrary augmented chiral algebra supported on the
diagonal.  The bridge from the Kriz CDGA to \(B^{\mathrm{ord}}(A)\)
requires at least:

1. a map from the cyclic \(E_3\) deformation complex of
   \(\Perf_{\mathrm{dg}}(X)\) to derivations of the Kriz model;
2. compatibility with the bar-length/diagonal-linking filtration;
3. a convention matching between \(B^{(2)}\) and the cyclic symmetry of
   the configuration-space model;
4. a degree shift explaining how a class in \(H^2(X,\Omega^1_X)\)
   becomes a weight-three derivation cocycle.

No local theorem supplies these data.

### Serious 2: the corollary overuses nonvanishing on the quintic

The corollary says that on generic \(Q_5\) the weight-three extension
fails and the Malcev completion stabilizes at weight \(2\).  For a
generic quintic threefold, \(\pi_1(Q_5)=0\), hence
\(\pi_1(\mathrm{Conf}_3(Q_5))=0\) by the codimension argument above.
There is no nontrivial Malcev lower-central series to stabilize at
weight \(2\).

The correct possible statement is about a nonzero class in the Quillen
minimal model or in a derivation complex of the Kriz model.  That
nonvanishing is not proved by the present quintic Yukawa calculation.

## What survives as theorem

### Theorem-grade local Arnold surface

For the affine line/formal disk, or for local genus-zero collision
screens on a curve, the Arnold relation
\[
  \eta_{ij}\wedge\eta_{jk}
  +\eta_{jk}\wedge\eta_{ki}
  +\eta_{ki}\wedge\eta_{ij}=0
\]
is theorem-grade.  Locally it is the flatness of the Arnold/KZ
connection and the mechanism behind \(d_{\mathrm{bar}}^2=0\) in the
ordered chiral bar complex.

This theorem belongs to the curve-side bar construction.  It does not
by itself identify \(\alpha_X\) with a configuration-space Malcev
class.

### Theorem-grade CY3 configuration model

For a smooth projective complex variety \(X\), the
Totaro-Kriz-Bezrukavnikov CDGA gives the rational configuration-space
model:
\[
  K_X(n)=H^*(X^n;\mathbb Q)[g_{ij}]/(\text{diagonal and Arnold-type
  relations}),
  \qquad
  d g_{ij}=p_{ij}^*[\Delta_X].
\]
For \(\dim_{\mathbb C}X=3\), \(|g_{ij}|=5\).  If \(X\) is simply
connected, this model is a Quillen/Sullivan rational-homotopy input
for \(\mathrm{Conf}_n(X)\), not a nontrivial Malcev \(\pi_1\) input.

### Theorem-grade triviality of the Malcev `pi_1` in the simply connected CY3 lane

For simply connected smooth projective CY3 \(X\),
\[
  \pi_1(\mathrm{Conf}_n(X))=0
\]
for every finite \(n\).  Hence the unipotent/Malcev completion of this
fundamental group is trivial.  This should be stated explicitly if the
paper keeps a configuration-space section.

## Corrected frontier statement

The following is the strongest true-shaped replacement.

```tex
\begin{conjecture}[Kriz--Quillen realisation of the Atiyah--Connes class]
\label{conj:kriz-quillen-atiyah-connes}
Let \(X\) be a simply connected smooth projective Calabi--Yau
threefold and let \(K_X(3)\) be the
Totaro--Kriz--Bezrukavnikov CDGA model of
\(\mathrm{Conf}_3(X)\), with diagonal generators
\(|g_{ij}|=5\) and \(d g_{ij}=p_{ij}^{*}[\Delta_X]\).
Fix a cyclic-HKR datum defining
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1).
\]
Assume there is a filtered \(L_\infty\)-morphism
\[
  \Xi_X:
  \Def^{E_3,\mathrm{cyc}}(\Perf_{\mathrm{dg}}(X))
  \longrightarrow
  \Der(K_X(3))
\]
compatible with the diagonal-linking filtration, the cyclic
rotation, and the Calabi--Yau HKR contraction.  Then the image
\[
  q_3(X):=\operatorname{gr}^W_3\Xi_X(\alpha_X)
\]
is a well-defined weight-three Quillen derivation class of the
configuration-space rational homotopy type.  Vanishing of
\(\alpha_X\) implies vanishing of this weight-three
configuration-space class.
\end{conjecture}
```

This is conjectural until \(\Xi_X\) is constructed and its arity-three
component is computed.  It is not a theorem about the Malcev completion
of `pi_1`.

## Replacement text for the current theorem lane

The current theorem and corollary should be replaced by a short
frontier paragraph:

```tex
\begin{remark}[Configuration-space rational homotopy; \ClaimStatusConjectured]
For a simply connected Calabi--Yau threefold \(X\), the spaces
\(\mathrm{Conf}_n(X)\) are simply connected: the diagonals in \(X^n\)
have real codimension \(6\), so loops and null-homotopies avoid them
after transversality.  Thus the Malcev completion of
\(\pi_1(\mathrm{Conf}_n(X))\) is trivial.  The relevant
configuration-space object is instead the Quillen rational-homotopy
Lie algebra of \(\mathrm{Conf}_n(X)\), or equivalently the
Totaro--Kriz--Bezrukavnikov CDGA model with degree-\(5\) diagonal
generators when \(\dim_{\mathbb C}X=3\).

The expected frontier comparison is a filtered \(L_\infty\)-morphism
from the cyclic \(E_3\)-deformation complex carrying
\(\alpha_X=[m_3,B^{(2)}]_X\) to the derivation complex of this
configuration-space model.  The construction of this morphism and the
calculation of its weight-three component are open.
\end{remark}
```

The five-face table should change its Malcev row to:

```tex
5 & Configuration rational homotopy, conjectural &
weight-three derivation of the Kriz model \(K_X(3)\), not Malcev
\(\pi_1\)
```

## Status recommendations

- `thm:malcev-quillen`: replace by a conjectural
  Kriz-Quillen realisation, or delete from theorem lane.
- `cor:pi1-motivic`: delete.  It is false for simply connected CY3s as
  a statement about Malcev `pi_1`.
- Five-face table Malcev row: rewrite as "configuration rational
  homotopy, conjectural".
- Any use of
  `H^3_Malcev(B^{ord}(A),Q) \cong H^3_M(X,Q(2))`: remove.
- Any phrase "generic quintic Malcev completion stabilises at weight
  2": remove.
- Keep Arnold relations only on curve/formal-disk collision screens
  unless a global CY3 Kriz model is explicitly being discussed.

## Proof obligations for resurrection

1. Build the cyclic-HKR class \(\alpha_X\) as a class in a fixed
   filtered deformation complex, per P01.
2. Define \(K_X(3)\) with its diagonal-linking filtration and exact
   degree shifts for \(\dim_{\mathbb C}X=3\).
3. Construct a filtered \(L_\infty\)-morphism
   \[
     \Xi_X:\Def^{E_3,\mathrm{cyc}}(\Perf_{\mathrm{dg}}(X))
     \to \Der(K_X(3)).
   \]
4. Compute the arity-three component of \(\Xi_X(\alpha_X)\).
5. Prove that this component is independent of the cyclic-HKR model,
   volume-form scaling, and Kriz-model quasi-isomorphism.
6. Only after P10's motivic target is repaired, ask whether the
   resulting Quillen derivation is the infinitesimal invariant of a
   normal function or motivic rational-homotopy class.

## Files changed

- Created this report only:
  `notes/universal_anomaly_platonic_swarm_20260424/P11_malcev_configuration.md`.

No target TeX files were edited.

## Commands run

- `sed -n '1,220p' CLAUDE.md`
- `sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md`
- `sed -n '1,220p' .agents/skills/frontier-research/SKILL.md`
- `sed -n '1,220p' chapters/connections/concordance.tex`
- `sed -n '1,240p' metadata/theorem_registry.md`
- `sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md`
- `rg -n "Malcev|Quillen|Hain|Kriz|Bezrukavnikov|Arnold|configuration|Conf_|Conf|motivic|pi_1|fundamental|Chen|Orlik|Sullivan|weight" ...`
- `sed -n '660,735p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
- `sed -n '803,920p' chapters/theory/configuration_spaces.tex`
- `sed -n '1170,1210p' chapters/theory/configuration_spaces.tex`
- `sed -n '1,260p' notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md`
- `sed -n '1,470p' notes/universal_anomaly_platonic_swarm_20260424/P02_positselski_bridge.md`
- `sed -n '1,260p' notes/universal_anomaly_platonic_swarm_20260424/P05_derived_loci_category.md`
- `sed -n '1,260p' notes/universal_anomaly_platonic_swarm_20260424/P06_architecture_voice.md`
- `sed -n '1,260p' notes/universal_anomaly_platonic_swarm_20260424/P10_motivic_regulator.md`
- Primary-source web checks for Quillen 1969, Kriz 1994, Bezrukavnikov
  1994, Hain 1987, Deligne-Goncharov 2005.

No build was run.
