# P01 cyclic/HKR core attack-heal report

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md`

Target read-only surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`

No target TeX file was edited.

## Verdict

The paper has a real core, but the core is not yet the displayed
chain-level formula
\[
  [m_3,B^{(2)}]_X\in
  \HC^{-,2}(\End(T_X),\End(T_X)\otimes\Omega^1_X)
  \to H^2(X,\Omega^1_X)
\]
as an unconditional construction. The theorem-grade survivor is
smaller and sharper:

1. a cyclic enhancement of the Hochschild cochains supplies an
   \(S^1\)-operator only after a precise chain/cochain convention;
2. the commutator has to be projected to the
   \(H^2(X,\wedge^2T_X)\) HKR summand;
3. the Calabi--Yau volume form then gives the honest target
   \[
     \wedge^2T_X \xrightarrow{\iota_{(-)}\Omega_X} \Omega^1_X,
     \qquad
     \alpha_X\in H^2(X,\Omega^1_X)=H^{1,2}(X).
   \]

This is deep enough to develop. It is not yet a proved new theorem
until the \(B^{(2)}\) convention, the negative-cyclic total complex, and
the trace/contraction map are fixed in the paper.

## Local anchors

- The abstract and introduction now state the nucleus as an
  Atiyah--Connes class:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:91`,
  `:94`, `:131`.
- The current \(B^{(2)}\) subsection mixes chain Connes \(B\), cyclic
  operads, framed \(E_2\), and a cochain degree-raising operator:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:211`,
  `:213`, `:219`, `:223`.
- The common-ambient paragraph asserts a degree-zero commutator and a
  direct landing in \(H^2(X,\Omega^1_X)\):
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:246`,
  `:248`.
- The construction records a negative-cyclic home and an HKR/trace
  target:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:461`,
  `:467`, `:473`, `:475`.
- The explicit representative still displays the raw tensor
  \(\bar\partial\nabla\wedge\bar\partial\nabla\) before the missing
  contraction:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:482`,
  `:486`, `:490`.
- The ten-step derivation is correctly demoted to conditional, but its
  Steps 6--9 are exactly the unproved core:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:513`,
  `:523`, `:524`, `:525`, `:526`.
- The main theorem already separates the bridge as conditional:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:744`,
  `:755`, `:769`.
- The local Hochschild chapter defines ordinary Connes \(B\) on chains,
  not the current cochain \(B^{(2)}\):
  `chapters/theory/hochschild_cohomology.tex:709`.
- The same chapter flags the chiral Connes lift as an additional
  obstruction, not automatic data:
  `chapters/theory/hochschild_cohomology.tex:2660`.
- Primary references already carried by the standalone include
  Connes 1985, Loday 1998, Getzler 1994, Getzler--Jones 1994,
  Getzler--Kapranov 1995, Kapranov 1999, Caldararu 2005,
  Caldararu--Willerton 2010, Calaque--Van den Bergh 2010, Markarian
  2009, Ramadoss 2008, Tamarkin 2007, and Shoikhet 2003:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1394`,
  `:1396`, `:1398`, `:1412`, `:1426`, `:1428`, `:1430`,
  `:1442`, `:1462`, `:1470`, `:1486`, `:1494`, `:1575`.

## Attacks

### Critical 1: \(B^{(2)}\) is not yet a defined operator

Connes' primary operator is a chain operator
\[
  B:C_n(A)\to C_{n+1}(A),\qquad B=(1-t)sN,
\]
with \(bB+Bb=0\). This is the convention in the local Hochschild
chapter and in Connes--Loday. The standalone also calls \(B^{(2)}\):

- a bidegree-two component of ordinary \(B\);
- an \(S^1\)-rotation in the framed \(E_2\) action;
- a cochain map \(\HH^2\to\HH^3\);
- a cyclic-skew projection;
- a motivic cyclic class.

Those are not the same object until a comparison is written. In a
cyclic Calabi--Yau algebra the chain operator can be transported to a
cochain BV operator only after choosing the trace degree, suspension,
and pairing convention. The sign and cohomological degree then change.
The present notation does not specify this transport, so the commutator
\([m_3,B^{(2)}]\) is not yet a theorem-grade cochain.

### Critical 2: the HKR target is shifted incorrectly unless the
\(H^2(\wedge^2T_X)\) summand is named

For a smooth variety,
\[
  \HH^n(X)\cong\bigoplus_{p+q=n}H^p(X,\wedge^qT_X).
\]
On a Calabi--Yau threefold, the volume form identifies
\(\wedge^qT_X\cong\Omega_X^{3-q}\). Therefore
\[
  H^2(X,\Omega^1_X)
  \quad\text{comes from}\quad
  H^2(X,\wedge^2T_X)\subset \HH^4(X),
\]
not from a bare Hochschild degree-two class. The current prose speaks
of a cyclic Hochschild \(2\)-cocycle and a cochain operator
\(\HH^2\to\HH^3\), then lands in \(H^2(\Omega^1)\). This can be made
consistent only after declaring the total grading in the negative
cyclic bicomplex and the projection
\[
  \pi_{2,2}^{\mathrm{HKR}}:\HH^4(X)\to H^2(X,\wedge^2T_X).
\]

### Critical 3: the trace/contraction to \(\Omega^1_X\) is missing

The Dolbeault representative has raw form
\[
  \bar\partial\nabla\wedge\bar\partial\nabla
  \in
  \Omega^{0,2}
  (X,\End(T_X)^{\otimes 2}\otimes(\Omega^1_X)^{\otimes 2}),
\]
up to the exact placement of the two endomorphism factors. Taking
\(\mathrm{tr}_{\End T_X}\) gives a class with two holomorphic one-form
factors, hence an \(\Omega^2_X\)-type object, not an \(\Omega^1_X\)
object. Cyclic skew-symmetrisation does not lower the holomorphic
degree.

The right repair is to route through the HKR polyvector summand:
\[
  \beta_X\in H^2(X,\wedge^2T_X),
  \qquad
  \alpha_X:=\iota_{\beta_X}\Omega_X\in H^2(X,\Omega^1_X).
\]
If the paper wants a direct Dolbeault formula, it must write the map
from the raw tensor to \(\wedge^2T_X\) or to \(\Omega^1_X\) explicitly.

### Serious 1: connection-independence is proved in the wrong lane

The text says independence follows because
\(\bar\partial(\nabla-\nabla')\) is exact. That does not by itself
handle a quadratic expression: changing \(\nabla\) changes
\((\bar\partial\nabla)^2\) by two cross terms and a square term before
trace/projection. The correct proof of independence should not be a
formal one-line Dolbeault calculation. It should be:

1. the Atiyah class is the Ext class of the jet sequence;
2. Kapranov's representative \(\bar\partial\nabla\) is one Dolbeault
   representative of that Ext class;
3. the construction uses the Yoneda/HKR/CY class, not the connection;
4. different connections change only the representative of the same
   class after the chosen projection.

This uses Atiyah/Kapranov/Markarian/Calaque--Van den Bergh, not a
bare exactness claim.

### Serious 2: bare HKR is not multiplicative without the Todd/Duflo
normalisation

The standalone already cites Caldararu--Willerton and later invokes a
Duflo coefficient. That is the correct warning sign. The HKR map
identifies vector spaces, but compatibility with products, pairings,
and trace needs the corrected HKR/Mukai normalisation, usually the
\(\sqrt{\mathrm{td}_X}\) or Duflo-twisted form. The construction should
state whether it uses:

- bare HKR only for target decomposition;
- corrected HKR for products and pairings;
- Calabi--Yau trivial Todd simplifications, if any are actually true
  in the chosen degree.

Without this, Steps 7--9 of the ten-step derivation overstate what the
sources give.

### Serious 3: negative cyclic cohomology is named but not built

The construction writes
\[
  \HC^{-,2}(\End(T_X),\End(T_X)\otimes\Omega^1_X)
\]
without defining the complex, its \(u\)-adic grading, its differential,
or its coefficient system. For a theorem, the paper needs a named
complex such as
\[
  (C^\bullet_{\mathrm{Hoch}}(\Perf_{\mathrm{dg}}(X)),
  \delta_{\mathrm{Hoch}},\Delta,u),
  \qquad
  d^-=\delta_{\mathrm{Hoch}}+u\Delta,
\]
or the chain version transported through a Calabi--Yau trace. The
operator \(B^{(2)}\) should then be a component of \(\Delta\) or of the
transported Connes operator, not a free symbol.

## Survivor theorem

The sharp true surface is the following. It is theorem-grade because it
states every required datum and makes the actual proved target explicit.

```tex
\begin{theorem}[Atiyah--Connes HKR obstruction class; \ClaimStatusConditional]
\label{thm:atiyah-connes-hkr-core}
Let \(X\) be a smooth projective Calabi--Yau threefold over
\(\mathbb C\), fix a holomorphic volume form
\(\Omega_X\in H^0(X,\Omega_X^3)\), and fix a cyclic dg enhancement
\(\Perf_{\mathrm{dg}}(X)\) of \(D^b(\Coh X)\).
Assume the following cyclic-HKR datum.
\begin{enumerate}[label=\textup{(AC\arabic*)}]
\item A Hochschild cochain model
\[
  C^\bullet_X=C^\bullet(\Perf_{\mathrm{dg}}(X),\Perf_{\mathrm{dg}}(X))
\]
with Hochschild differential \(\delta\).
\item A cohomological \(S^1\)-operator
\[
  \Delta_2:C^\bullet_X\to C^{\bullet+\epsilon}_X
\]
obtained from Connes' chain operator \(B=(1-t)sN\) by the stated
Calabi--Yau trace convention, with the sign and degree
\(\epsilon\) fixed, and satisfying
\(\delta\Delta_2+(-1)^\epsilon\Delta_2\delta=0\).
\item The ternary Stasheff operation \(m_3\) acts on the same complex,
with the displayed degree convention, and the graded commutator
\[
  \gamma_X=[m_3,\Delta_2]
\]
is \(\delta\)-closed of total Hochschild degree \(4\).
\item The corrected HKR/Mukai map is fixed, and
\[
  \beta_X:=\pi^{\mathrm{HKR}}_{2,2}([\gamma_X])
  \in H^2(X,\wedge^2T_X)
\]
is the \((p,q)=(2,2)\) HKR component of the commutator class.
\end{enumerate}
Then
\[
  \alpha_X:=\iota_{\beta_X}\Omega_X
  \in H^2(X,\Omega_X^1)
\]
is independent of the Dolbeault representative of the Atiyah class and
depends only on the cyclic dg enhancement and the chosen volume-form
normalisation. On compact Kahler \(X\),
\[
  H^2(X,\Omega_X^1)\cong H^{1,2}(X).
\]
The vanishing of \(\alpha_X\) is invariant under cyclic
\(A_\infty\)-quasi-equivalence preserving the trace convention.
\end{theorem}
```

This theorem should replace the current implicit claim that the raw
commutator itself already lands in \(H^2(X,\Omega^1_X)\).

## Proof outline for the survivor theorem

1. **Mixed/cyclic complex.** Use Connes 1985 and Loday 1998 for the
   chain mixed complex. If the proof is cohomological, transport the
   chain operator through the chosen Calabi--Yau cyclic trace and record
   the resulting degree. This is the only legitimate meaning of
   \(B^{(2)}\) or \(\Delta_2\).

2. **Closed commutator.** The framed \(E_2\)/BV structure gives the
   Cartan relation between the Hochschild differential and the
   \(S^1\)-operator. With the degree convention fixed,
   \(\delta[m_3,\Delta_2]=0\) follows from the \(A_\infty\)-relations
   for \(m_3\) and the mixed-complex relation for \(\Delta_2\).

3. **HKR projection.** Apply the HKR decomposition to the cohomology
   class of the commutator and project to
   \(H^2(X,\wedge^2T_X)\). Use bare HKR only for the decomposition. Use
   the corrected HKR/Mukai normalisation when products, traces, or
   pairings are invoked.

4. **Calabi--Yau contraction.** The volume form gives
   \[
     \wedge^2T_X \cong \Omega^1_X,
     \qquad
     v\wedge w\mapsto \iota_{v\wedge w}\Omega_X.
   \]
   Hence \(\beta_X\) yields
   \(\alpha_X\in H^2(X,\Omega^1_X)\).

5. **Connection independence.** The Dolbeault form
   \(\bar\partial\nabla\) is a representative of the Atiyah Ext class
   by Kapranov. The construction uses the Ext/HKR class, so changing
   the connection changes the representative, not the cohomology class.
   This avoids the invalid one-line quadratic exactness argument.

6. **Hodge location.** Dolbeault comparison on compact Kahler \(X\)
   gives \(H^q(X,\Omega_X^p)=H^{p,q}(X)\), hence
   \(H^2(X,\Omega_X^1)=H^{1,2}(X)\).

## TeX patch suggestions

### 1. Rename \(B^{(2)}\) at first definition

```tex
We write \(\Delta_2\) for the cohomological operator obtained from
Connes' chain operator \(B=(1-t)sN\) by the Calabi--Yau trace convention
fixed in Convention~\ref{conv:cyclic-cochain-B}.  The symbol
\(B^{(2)}\) is used only after this convention has been fixed:
\[
  B^{(2)}:=\Delta_2 .
\]
It is not a new Connes hierarchy operator.
```

### 2. Add a convention before the construction

```tex
\begin{convention}[Cochain Connes convention]
\label{conv:cyclic-cochain-B}
Connes' operator \(B\) acts on Hochschild chains by
\(B:C_n(A)\to C_{n+1}(A)\).  For the cyclic dg category
\(\Perf_{\mathrm{dg}}(X)\) with its Calabi--Yau trace, we transport
\(B\) to Hochschild cochains using the trace pairing.  The transported
operator is denoted \(\Delta_2\), has cohomological degree
\(\epsilon\), and satisfies
\[
  \delta\Delta_2+(-1)^\epsilon\Delta_2\delta=0.
\]
All graded commutators with \(m_3\) use this convention.
\end{convention}
```

The value of \(\epsilon\) must be filled only after the convention is
checked. Do not guess it.

### 3. Replace the construction target

```tex
\begin{construction}[Atiyah--Connes HKR class]
\label{constr:cocycle}
Let \(X\) be a smooth projective Calabi--Yau threefold, fix
\(\Omega_X\), and use Convention~\ref{conv:cyclic-cochain-B}.  The
graded commutator
\[
  \gamma_X:=[m_3,\Delta_2]
\]
is a Hochschild cohomology class in the total degree fixed by the
cyclic convention.  Its Atiyah--Connes component is
\[
  \beta_X:=\pi^{\mathrm{HKR}}_{2,2}([\gamma_X])
  \in H^2(X,\wedge^2T_X).
\]
Contracting with the Calabi--Yau volume form gives
\[
  \alpha_X:=\iota_{\beta_X}\Omega_X
  \in H^2(X,\Omega_X^1).
\]
This is the obstruction class used below.
\end{construction}
```

### 4. Replace the representative proposition

```tex
\begin{proposition}[Dolbeault representative; \ClaimStatusConditional]
\label{prop:cocycle-rep}
After Convention~\ref{conv:cyclic-cochain-B} and the HKR projection
\(\pi^{\mathrm{HKR}}_{2,2}\) are fixed, the class \(\alpha_X\) is
represented by the image of the Kapranov Atiyah representative
\(\bar\partial\nabla\) under the composite
\[
  \Omega^{0,2}\!\left(X,
  \End(T_X)^{\otimes2}\otimes(\Omega_X^1)^{\otimes2}\right)
  \longrightarrow
  \Omega^{0,2}(X,\wedge^2T_X)
  \xrightarrow{\iota_{(-)}\Omega_X}
  \Omega^{0,2}(X,\Omega_X^1).
\]
The first arrow is the trace/cyclic projection specified by the
cochain Connes convention.
\end{proposition}
```

### 5. Replace the independence sentence

```tex
Independence of \(\nabla\) is not proved by a direct quadratic
exactness calculation.  The class \(\bar\partial\nabla\) represents the
Atiyah Ext class of the jet sequence; the construction above is made
from the resulting Ext/HKR class.  Changing the connection changes the
Dolbeault representative, not the class in \(H^2(X,\Omega_X^1)\).
```

### 6. Replace Step 6--Step 9 of the ten-step derivation

```tex
&\textup{(Step 6, cyclic convention)} &&
\Delta_2 \text{ is the cochain operator of
Convention~\ref{conv:cyclic-cochain-B}.}\\
&\textup{(Step 7, closed commutator)} &&
\gamma_X=[m_3,\Delta_2],\qquad \delta\gamma_X=0.\\
&\textup{(Step 8, corrected HKR projection)} &&
\beta_X=\pi^{\mathrm{HKR}}_{2,2}([\gamma_X])
\in H^2(X,\wedge^2T_X).\\
&\textup{(Step 9, Calabi--Yau contraction)} &&
\alpha_X=\iota_{\beta_X}\Omega_X\in H^2(X,\Omega_X^1).
```

## Exact blockers

1. Fix the cochain degree and sign of the transported Connes operator.
   The local Hochschild chapter uses chain \(B:C_n\to C_{n+1}\); the
   standalone needs the cochain transport.
2. Define the negative-cyclic or cyclic-Hochschild total complex,
   including \(u\)-degree if negative cyclic is retained.
3. Prove or assume the Cartan/mixed-complex relation that makes
   \([m_3,\Delta_2]\) closed.
4. Insert the HKR projection
   \(\pi_{2,2}^{\mathrm{HKR}}:\HH^4(X)\to H^2(X,\wedge^2T_X)\).
5. State whether the construction uses bare HKR or corrected
   HKR/Mukai/Duflo normalisation for products and traces.
6. Specify the trace/cyclic projection from the raw Dolbeault tensor to
   \(\wedge^2T_X\), then contract with \(\Omega_X\).
7. Replace direct connection-independence claims by the Ext-class
   argument.

## Claim attacked

The attacked claim is that the current construction already gives a
well-defined chain-level negative-cyclic cocycle
\[
  [m_3,B^{(2)}]_X
  \in \HC^{-,2}(\End(T_X),\End(T_X)\otimes\Omega^1_X)
\]
whose HKR image is canonically
\[
  \at_X\cup B^{(2)}_{\mathrm{Connes}}
  \in H^2(X,\Omega^1_X).
\]

Status: conditional. The Hodge target is correct after repair; the
chain-level cyclic construction is not yet fully defined.

## Survivor theorem

The survivor is the conditional Atiyah--Connes HKR obstruction theorem
above: once a cyclic cochain Connes operator \(\Delta_2\), a closed
commutator class, the corrected HKR projection, and the CY contraction
are fixed, the paper obtains a canonical obstruction
\[
  \alpha_X\in H^2(X,\Omega^1_X)=H^{1,2}(X)
\]
whose vanishing is invariant under cyclic \(A_\infty\)-quasi-equivalence.

## Files changed

- `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md`

No target TeX files were edited.

## Commands run

```bash
sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md
sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md
sed -n '1,220p' CLAUDE.md
sed -n '1,240p' chapters/connections/concordance.tex
sed -n '1,240p' metadata/theorem_registry.md
sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md
rg -n -F -e 'alpha_X' -e 'B^{(2)}' -e 'HKR' -e 'negative cyclic' -e 'cyclic Hochschild' -e 'Connes' -e 'Atiyah' -e 'trace' -e 'connection' -e 'independence' -e 'H^2(X,\\Omega' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
ls -la notes/universal_anomaly_platonic_swarm_20260424 notes/universal_anomaly_attack_heal_20260424
rg -n -F -e 'HKR' -e 'Connes' -e 'negative cyclic' -e 'Atiyah--Connes' -e 'Atiyah-Connes' notes/universal_anomaly_attack_heal_20260424
rg -n -F -e 'HKR' -e 'Connes' -e 'negative cyclic' -e 'Atiyah' -e 'Cyclic' -e 'Keller' -e 'Loday' -e 'Markarian' -e 'Caldararu' -e 'Kontsevich' -e 'Shoikhet' -e 'Weibel' -e 'Goodwillie' bibliography chapters appendices standalones
sed -n '120,260p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '423,540p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '740,805p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
sed -n '700,725p' chapters/theory/hochschild_cohomology.tex
sed -n '2648,2676p' chapters/theory/hochschild_cohomology.tex
sed -n '260,380p' notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A6_rectification_blueprint.md
sed -n '1388,1505p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n -F -e 'Caldararu' -e 'Ramadoss' -e 'Atiyah' -e 'Getzler' -e 'Jones' -e 'Tamarkin' -e 'Shoikhet' -e 'Tsygan' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex bibliography/references.tex
git status --short notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md notes/universal_anomaly_platonic_swarm_20260424
sed -n '1,220p' notes/universal_anomaly_platonic_swarm_20260424/README.md
```
