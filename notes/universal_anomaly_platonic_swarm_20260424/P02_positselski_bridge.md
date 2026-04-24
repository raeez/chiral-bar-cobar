# P02: Positselski Bridge From the Atiyah-Connes Class

Assigned surface:
`standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`,
Theorem `thm:main`, item (iii), lines 744--786.

Mission: attack and heal the B1 bridge
\[
  \alpha_X \in H^2(X,\Omega^1_X)
  \longrightarrow
  \text{first chiral bar--cobar obstruction on } C .
\]

## Verdict

The rectified theorem is honest: it states B1 as a missing comparison
hypothesis. It is not yet theorem-grade because the target
\[
  \mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C)
\]
is not defined.

The strongest plausible new theorem is not
\[
  \alpha_X=0 \Longrightarrow
  \Omega_C^{\mathrm{ch}}\Bar_C^{\mathrm{ch}}(A_C)\simeq A_C
\]
by itself. The strongest plausible theorem is the first-obstruction
identity
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)
  =
  o^{(0)}_3(A_C)
  \in
  H^2\bigl(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr),
\]
where
\[
  A_C :=
  \Sp^{\mathrm{ch}}_{\Sigma,C}\bigl(\Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X))\bigr)
\]
is the stage-two chiral algebra on the reference curve. If the
standalone insists on the symbol `obs_2`, define
\[
  \mathrm{obs}^{\mathrm{bc}}_2(A_C):=o^{(0)}_3(A_C).
\]
In Volume I notation the first genus-zero obstruction is the cubic
shadow \(o^{(0)}_3\), not a total all-genus obstruction tower.

Vanishing of \(\alpha_X\) then gives only
\[
  o^{(0)}_3(A_C)=0
\]
under the comparison theorem. It does not kill \(o^{(0)}_4,o^{(0)}_5,\ldots\).
Full Theorem B needs either independent Koszul/PBW collapse or an
additional all-loop closure theorem.

## Anchors Read

- Rectified B1 surface:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:744--786`.
- The paper's two-stage definition:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:253--259`.
- Volume III stage-two definition:
  `~/calabi-yau-quantum-groups/main.tex:1038--1056`.
- Volume I Theorem B:
  `chapters/theory/bar_cobar_adjunction_inversion.tex:1995--2106`.
- Construction versus resolution warning:
  `chapters/theory/chiral_koszul_pairs.tex:289--300`.
- Cyclic deformation complex:
  `chapters/theory/chiral_hochschild_koszul.tex:3191--3209`,
  `3530--3577`.
- Modular cyclic MC ambient:
  `chapters/theory/chiral_hochschild_koszul.tex:3642--3728`.
- Koszulness as vanishing of all genus-zero obstruction classes:
  `chapters/theory/chiral_koszul_pairs.tex:4145--4182`.
- Independence of Koszulness and full shadow depth:
  `chapters/theory/chiral_koszul_pairs.tex:4191--4198`.
- Off-locus obstruction as first off-diagonal bar class / first higher
  multiplication:
  `chapters/theory/bar_cobar_adjunction_inversion.tex:2336--2398`.
- Counterexample pattern: \(k[x]/(x^n)\) has first higher operation
  \(m_{n-1}\), so absence of a lower higher product does not imply
  formality:
  `chapters/theory/chiral_koszul_pairs.tex:1631--1666`.
- Concordance statement of Theorem B:
  `chapters/connections/concordance.tex:41--72`.

## Attack

### A1. The current B1 target is not a mathematical object

Theorem `thm:main` writes
\[
  \operatorname{sp}_{\Sigma,C}\colon H^2(X,\Omega^1_X)
  \to
  \mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C).
\]
No such obstruction group is defined in the paper.

The curve target cannot be \(H^2(C,\Omega^1_C)\), since that group is
zero for every smooth curve. The target must be a deformation complex
of the curve-side chiral algebra, not coherent sheaf cohomology of
the curve.

### A2. Volume I does not identify one class with full bar--cobar inversion

Theorem B says:

1. On the strict Koszul lane, the counit
   \[
     \Omega_C^{\mathrm{ch}}\Bar_C^{\mathrm{ch}}(A_C)\to A_C
   \]
   is a quasi-isomorphism.
2. On the completed filtered pro-conilpotent finite-piece lane, the
   same counit is a coderived/coacyclic equivalence.
3. Promotion from coderived equivalence to ordinary quasi-isomorphism
   requires a collapse input such as \(\kappa(A_C)=0\) or a
   bar-degree spectral sequence degeneration.

It does not say that a single secondary cyclic class kills the whole
obstruction tower.

### A3. First obstruction and Koszulness are different logical levels

Volume I separates:
\[
  o^{(0)}_{r+1}(A_C)=0 \quad (r\ge 2)
\]
as the genus-zero Koszul/formality condition. The first obstruction is
only the first non-zero higher operation, equivalently the first
off-diagonal bar class.

Thus
\[
  o^{(0)}_3(A_C)=0
\]
does not imply
\[
  o^{(0)}_{r+1}(A_C)=0\quad\forall r\ge 2.
\]
The classical warning is already in Volume I: for \(A=k[x]/(x^n)\),
the transferred model has the first non-zero operation \(m_{n-1}\).
For \(n=5\), a cubic obstruction can vanish while a quartic obstruction
survives. The chiral statement needs a proof that the curve-side
family is not in this failure pattern.

### A4. Stage-two specialization is a functor, not an ordinary restriction

Volume III defines
\[
  \Sp^{\mathrm{ch}}_{\Sigma_{d-1},C}(\mathcal F)
  =
  \left(\int_{\Sigma_{d-1}}\mathcal F\right)\big|_C .
\]
This is factorisation homology followed by restriction to the reference
curve. It is stage-two specialization. It is not inversion and it is
not the sheaf map
\[
  H^2(X,\Omega^1_X)\to H^2(C,\Omega^1_C).
\]

The B1 bridge must be the derivative of this functor on formal
moduli/deformation complexes.

## Repaired Objects

Let
\[
  \mathcal F_X:=\Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X)),
  \qquad
  A_C:=\Sp^{\mathrm{ch}}_{\Sigma,C}(\mathcal F_X).
\]

Let the curve-side cyclic bar deformation complex be
\[
  \Defcyc(A_C)
  :=
  \operatorname{CoDer}^{\mathrm{cyc}}\!
  \bigl(\widehat{\Bar}^{\mathrm{ch}}_C(A_C)\bigr)[1],
\]
with modular refinement \(\Defcyc^{\mathrm{mod}}(A_C)\) when genus
corrections are retained. Let
\[
  \pi_{r,g}\Defcyc^{\mathrm{mod}}(A_C)
\]
denote the component of bar/shadow degree \(r\) and genus \(g\).

Define the first bar--cobar obstruction group by
\[
  \Ob^{(1)}_{\mathrm{bc}}(A_C)
  :=
  H^2\bigl(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr).
\]
This is the receptacle for the cubic genus-zero shadow \(o^{(0)}_3(A_C)\).
If the paper uses the index `2` because obstruction theory places it in
cohomological degree two, write
\[
  \Ob^{(2)}_{\mathrm{bc}}(A_C)
  :=
  H^2\bigl(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr),
  \qquad
  \mathrm{obs}^{\mathrm{bc}}_2(A_C):=o^{(0)}_3(A_C).
\]

The full strict Koszul obstruction is the tower
\[
  \Ob^{\mathrm{Kosz}}_{\mathrm{bc}}(A_C)
  :=
  \prod_{r\ge 2}
  H^2\bigl(\pi_{r+1,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr),
\]
with class
\[
  o^{(0)}_{\ge 3}(A_C)
  :=
  \bigl(o^{(0)}_3(A_C),o^{(0)}_4(A_C),\ldots\bigr).
\]

The completed Positselski obstruction to strict chain-level extension
across a wall lives instead in the CDG morphism complex:
\[
  H^1\!
  \left(
    \Hom_{\mathrm{CDG}}
    \bigl(B^w(A_C),\Omega^w B^w(A_C)\bigr)
  \right),
\]
as in the curved theorem's formula. This is a different target. It
should not be conflated with the first genus-zero cyclic obstruction.

## The Specialization Map

The specialization map should be the composite on obstruction
cohomology induced by stage-two factorisation:
\[
\begin{tikzcd}[column sep=large]
H^2(X,\Omega^1_X)
  \arrow[r,"\mathrm{HKR}^{-1}_{\mathrm{cyc}}"]
&
H^2\!\left(\Def^{E_3,\mathrm{cyc}}(\mathcal F_X)\right)
  \arrow[r,"d\Sp^{\mathrm{ch}}_{\Sigma,C}"]
&
H^2\!\left(\Defcyc^{\mathrm{mod}}(A_C)\right)
  \arrow[r,"\pi_{3,0}"]
&
H^2\!\left(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\right).
\end{tikzcd}
\]
Set
\[
  \operatorname{sp}_{\Sigma,C}
  :=
  \pi_{3,0}\circ d\Sp^{\mathrm{ch}}_{\Sigma,C}
  \circ \mathrm{HKR}^{-1}_{\mathrm{cyc}}.
\]

This is the only viable B1 map. It is not a map of coherent sheaf
cohomology on \(C\). It is a map between deformation complexes of
factorisation/chiral structures.

## Strongest Plausible Theorem

```tex
\begin{theorem}[Stage-two specialization of the Atiyah--Connes class]
\label{thm:sp-alpha-first-barcobar-obstruction}
Let \(X\) be a smooth projective Calabi--Yau threefold with a fixed
cyclic dg enhancement of \(D^b(\Coh X)\). Let
\[
  \mathcal F_X=\Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X)),\qquad
  A_C=\Sp^{\mathrm{ch}}_{\Sigma,C}(\mathcal F_X).
\]
Assume:
\begin{enumerate}[label=\textup{(S\arabic*)}]
\item \(\mathcal F_X\) is a cyclic holomorphic \(E_3\)-factorisation
algebra and \(\Sp^{\mathrm{ch}}_{\Sigma,C}\) is defined as
factorisation homology over \(\Sigma\), followed by restriction to
\(C\).
\item \(\Sp^{\mathrm{ch}}_{\Sigma,C}\) is differentiable as a functor
of formal moduli problems and induces a filtered morphism
\[
  d\Sp^{\mathrm{ch}}_{\Sigma,C}\colon
  \Def^{E_3,\mathrm{cyc}}(\mathcal F_X)
  \to
  \Defcyc^{\mathrm{mod}}(A_C).
\]
\item The cyclic HKR comparison sends the Atiyah--Connes class
\(\alpha_X=[m_3,B^{(2)}]_X\) to the \(E_3\)-cyclic deformation class
represented by the ternary Stasheff operation and the Connes rotation.
\item The bar-length filtration is preserved and the arity-three,
genus-zero projection of \(d\Sp^{\mathrm{ch}}_{\Sigma,C}(\alpha_X)\)
is computed by the same cyclic coderivation convention as
\(\Defcyc(A_C)=\operatorname{CoDer}^{\mathrm{cyc}}
(\widehat{\Bar}^{\mathrm{ch}}_C(A_C))[1]\).
\end{enumerate}
Then
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)
  =
  o^{(0)}_3(A_C)
  \in
  H^2\bigl(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr).
\]
Consequently \(\alpha_X=0\) implies the vanishing of the first
genus-zero bar--cobar obstruction of \(A_C\).
\end{theorem}
```

This theorem is narrow, new, and worth proving. It is the B1 bridge in
its true form.

## Positselski Consequence

The Positselski consequence requires one further input.

```tex
\begin{corollary}[Bar--cobar inversion after obstruction closure]
\label{cor:sp-alpha-positselski}
In the situation of Theorem~\ref{thm:sp-alpha-first-barcobar-obstruction},
assume in addition one of the following:
\begin{enumerate}[label=\textup{(K\arabic*)}]
\item \(A_C\in\operatorname{Kosz}(C)\), equivalently
\[
  o^{(0)}_{r+1}(A_C)=0\qquad(r\ge 2).
\]
\item \(A_C\) lies in the completed filtered pro-conilpotent
Positselski surface with finite graded bar pieces, so the cone of
\[
  \Omega_C^{\mathrm{ch}}\Bar_C^{\mathrm{ch}}(A_C)\to A_C
\]
is coacyclic.
\item The obstruction tower is generated by the first obstruction in
the precise sense that the ideal generated by \(o^{(0)}_3(A_C)\) in the
minimal \(L_\infty\)-model of
\(\Defcyc^{\mathrm{mod}}(A_C)|_{g=0}\) contains every
\(o^{(0)}_{r+1}(A_C)\) for \(r\ge 3\).
\end{enumerate}
Then Theorem B applies. In case \textup{(K1)} the counit is a strict
quasi-isomorphism. In case \textup{(K2)} it is an isomorphism in the
coderived category. In case \textup{(K3)}, \(\alpha_X=0\) implies
\textup{(K1)} and hence strict inversion.
\end{corollary}
```

Status:

- (K1) is an independent Koszul/PBW hypothesis.
- (K2) is the completed Positselski lane.
- (K3) is the new all-higher closure theorem. It is not in Volume I.

## Proof Architecture

### Step 1. Put \(\alpha_X\) in the correct formal moduli tangent complex

The paper already constructs
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega^1_X).
\]
To connect it to bar--cobar, one must lift this statement from
coherent cohomology to the cyclic deformation complex of the stage-one
factorisation algebra:
\[
  H^2(X,\Omega^1_X)
  \cong
  H^2\bigl(\Def^{E_3,\mathrm{cyc}}(\mathcal F_X)_{\mathrm{HKR}}\bigr).
\]
This is a cyclic HKR theorem with trace/contraction conventions fixed.
The proof must not use ordinary restriction to \(C\).

### Step 2. Differentiate stage-two factorisation

Construct a morphism of complete filtered \(L_\infty\)-algebras
\[
  d\Sp^{\mathrm{ch}}_{\Sigma,C}\colon
  \Def^{E_3,\mathrm{cyc}}(\mathcal F_X)
  \to
  \Defcyc^{\mathrm{mod}}(A_C).
\]
This is the load-bearing new functoriality statement. It follows only
if factorisation homology over \(\Sigma\) preserves the cyclic
structure, the bar-length filtration, and the relevant completions.
Ayala--Francis Fubini-type formalism can support the homology step, but
it does not by itself prove the cyclic bar-coderivation comparison.

### Step 3. Project to the arity-three genus-zero component

The first genus-zero obstruction is
\[
  o^{(0)}_3(A_C)\in
  H^2\bigl(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)\bigr).
\]
Show
\[
  \pi_{3,0}\bigl(d\Sp^{\mathrm{ch}}_{\Sigma,C}(\alpha_X)\bigr)
  =
  o^{(0)}_3(A_C).
\]
This is a chain calculation: the ternary Stasheff operation in the
stage-one cyclic Hochschild model must specialize to the arity-three
cyclic coderivation of \(\widehat{\Bar}^{\mathrm{ch}}_C(A_C)\), with
the Connes rotation becoming the cyclic symmetry of the bar complex.

### Step 4. Invoke Volume I only after the tower is closed

Volume I Theorem B applies once \(A_C\) is on the strict Koszul lane or
the completed Positselski lane. It does not prove that the first
obstruction controls higher ones. The all-higher implication must be
one of:
\[
  \text{PBW/Koszul hypothesis,}
  \qquad
  \text{spectral sequence collapse,}
  \qquad
  \text{new generated-by-}o_3\text{ theorem.}
\]

## Exact Blockers

1. **Definition blocker.** The paper must define
   \(\Def^{E_3,\mathrm{cyc}}(\mathcal F_X)\) and its relation to
   \(H^2(X,\Omega^1_X)\). Without this, \(\alpha_X\) has no functorial
   source for stage-two specialization.

2. **Functoriality blocker.** It must prove that
   \(\Sp^{\mathrm{ch}}_{\Sigma,C}\) induces a filtered morphism on
   cyclic deformation complexes. This is stronger than the existence of
   the stage-two functor on objects.

3. **Filtration blocker.** It must prove that the arity/bar-length
   projection \(\pi_{3,0}\) is preserved by stage-two specialization.
   Factorisation homology may mix weights unless the completion and
   filtration are controlled.

4. **Convention blocker.** It must fix the cyclic chain/cochain
   convention for \(B^{(2)}\) and the sign in the commutator before the
   equality with \(o^{(0)}_3(A_C)\) can be meaningful.

5. **Higher-obstruction blocker.** It must not claim that
   \(\alpha_X=0\) implies all \(o^{(0)}_{r+1}=0\). A separate PBW,
   formality, or tower-generation theorem is required.

6. **Strict/coderived blocker.** It must distinguish strict
   quasi-isomorphism from coderived equivalence. The completed
   Positselski surface gives coacyclic cone; ordinary chain-level
   inversion requires collapse.

## Recommended TeX Patch Surface

Replace the vague B1 item with:

```tex
\item \textup{(conditional Positselski bridge)}
Let
\[
  A_C :=
  \Sp^{\mathrm{ch}}_{\Sigma,C}
  \bigl(\Phi^{\mathrm{FA}}_3(D^b_{\mathrm{dg}}(X))\bigr).
\]
Assume the stage-two functor induces a filtered morphism of cyclic
deformation complexes
\[
  d\Sp^{\mathrm{ch}}_{\Sigma,C}\colon
  \Def^{E_3,\mathrm{cyc}}(\Phi^{\mathrm{FA}}_3(X))
  \to
  \Defcyc^{\mathrm{mod}}(A_C)
\]
and that the cyclic HKR representative of
\(\alpha_X=[m_3,B^{(2)}]_X\) maps, after projection to arity three and
genus zero, to the first bar--cobar obstruction:
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)
  :=
  \pi_{3,0}d\Sp^{\mathrm{ch}}_{\Sigma,C}(\alpha_X)
  =
  o^{(0)}_3(A_C)
  \in
  H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
\]
Then \(\alpha_X=0\) kills the first genus-zero obstruction. The
bar--cobar counit is a strict quasi-isomorphism only after the
independent Koszul/PBW condition
\[
  o^{(0)}_{r+1}(A_C)=0\qquad(r\ge2)
\]
or an all-higher closure theorem reducing these classes to
\(o^{(0)}_3(A_C)\). On the completed Positselski surface it is a
coderived equivalence under the finite-piece pro-conilpotent
hypotheses of Volume I.
```

## What Is Already Proved

- The paper proves, conditionally on its cyclic HKR model, the existence
  and target of \(\alpha_X\) in \(H^2(X,\Omega^1_X)=H^{1,2}(X)\).
- Volume I proves strict bar--cobar inversion on the Koszul locus.
- Volume I proves a completed/coderived Positselski surface under
  filtered pro-conilpotent finite-piece hypotheses.
- Volume III states the stage-two specialization functor as
  factorisation homology over \(\Sigma\) followed by restriction to \(C\).

## What Is Conditionally Reachable

The new theorem
\[
  \operatorname{sp}_{\Sigma,C}(\alpha_X)=o^{(0)}_3(A_C)
\]
is conditionally reachable and should be the next proof target. It is
deep enough to justify the paper: it makes a global Atiyah-Connes class
control the first curve-side chiral bar obstruction.

## What Remains Conjectural

- \(\alpha_X=0\Rightarrow A_C\in\operatorname{Kosz}(C)\).
- \(\alpha_X=0\Rightarrow o^{(0)}_{r+1}(A_C)=0\) for all \(r\ge2\).
- The all-loop/all-genus shadow closure.
- Any identification of the B1 bridge with the K3/Mukai trace or
  Bruinier conductor edge.

## Next Falsifier

Search for a curve-side specialization \(A_C\) with
\[
  o^{(0)}_3(A_C)=0,\qquad o^{(0)}_4(A_C)\ne0.
\]
If such an example appears inside the stage-two image of a CY3, then
\(\alpha_X\) is only the first obstruction and cannot be advertised as
the Theorem B control class. If no such example exists on the
stage-two image, the missing theorem is precisely:

\[
  \text{Stage-two CY3 image has obstruction tower generated by }
  o^{(0)}_3.
\]

That would be a genuinely new theorem.

## Files Changed

- `notes/universal_anomaly_platonic_swarm_20260424/P02_positselski_bridge.md`

No target TeX file was edited. No build was run.

## Commands Run

- Loaded repo and ecosystem instructions:
  `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`,
  `~/ecosystem/AGENTS-HARNESS.md`.
- Loaded skills:
  `.agents/skills/deep-beilinson-audit/SKILL.md`,
  `.agents/skills/frontier-research/SKILL.md`.
- Read the rectified theorem and its local setup with `nl -ba ... sed`.
- Grepped Volume I and metadata for Theorem B, Positselski, Koszul
  locus, cyclic deformation complexes, and obstruction tower notation.
- Read cross-volume stage-two definitions in
  `~/calabi-yau-quantum-groups/main.tex` and `FRONTIER.md`.
