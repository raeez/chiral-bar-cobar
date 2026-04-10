# Theorem A / Theorem B Tautology Audit -- Ground Truth Verification

Read-only verification of two adversarial audit claims against Vol I source.

## 1. Theorem A: exact location and statement

**Label**: `thm:bar-cobar-isomorphism-main`
**File**: `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex`
**Lines**: 3253--3297 (statement); subsection "Geometric bar-cobar duality (Theorem A)" begins line 3244.

Note: There is a separate theorem `thm:bar-cobar-adjunction` at
`chapters/theory/cobar_construction.tex:1877--1890`, but that is the
**unit of adjunction** (a subsidiary result), NOT Theorem A itself.
`chiral_koszul_pairs.tex:3256` explicitly `\index{Theorem A|textbf}` on
`thm:bar-cobar-isomorphism-main`. This is the canonical Theorem A.

**Exact statement (verbatim, lines 3253--3297):**

```
\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
The equivalences below hold in the derived category
$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
factorization algebras on~$X$.

\smallskip\noindent
The Heisenberg instance was verified in~\S\ref{sec:frame-inversion}.
In general:

Let $(\cA_1, \cC_1, \tau_1, F_\bullet)$ and
$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
Then:
\begin{enumerate}
\item the canonical units and counits are quasi-isomorphisms:
\[
\cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad
\Omega_X(\cC_i) \xrightarrow{\;\sim\;} \cA_i
\qquad (i = 1, 2);
\]

\item the reduced bar functor is intertwined with Verdier duality:
\[
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
\simeq \bar{B}_X(\cA_2), \qquad
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_2)
\simeq \bar{B}_X(\cA_1);
\]

\item if $\cA_2$ is denoted by $\cA_1^!$, then
\[
\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
\simeq \bar{B}_X(\cA_1^!).
\]
\end{enumerate}
```

**Proof of part (2) (verbatim, lines 3305--3310):**

```
For part~(2), the Verdier compatibility in
Definition~\ref{def:chiral-koszul-pair} identifies
$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with $\cC_2$.
Composing with the unit equivalences $\cC_i \simeq \bar{B}_X(\cA_i)$
yields $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1) \simeq
(\cA_2)_\infty$ (factorization \emph{algebra}, not coalgebra).
```

## 2. Definition `def:chiral-koszul-pair` (the alleged source of circularity)

**File**: `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex`
**Lines**: 570--617.

**Exact statement (verbatim, lines 570--588):**

```
\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
\index{Koszul pair!chiral|textbf}
A \emph{chiral Koszul pair} on a smooth projective curve~$X$
is a pair of chiral Koszul data
\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
Definition~\textup{\ref{def:chiral-koszul-morphism})}
\[
(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
(\cA_2, \cC_2, \tau_2, F_\bullet)
\]
equipped with Verdier-compatible identifications
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \cC_2, \qquad
\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \cC_1,
\]
compatible with the twisting morphisms and filtrations.
In this situation we write $\cA_2 \simeq \cA_1^!$ and
$\cA_1 \simeq \cA_2^!$.
```

## 3. Theorem B: exact location and statement

**Label**: `thm:bar-cobar-inversion-qi`
**File**: `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex`
**Lines**: 1604--1650.

**Exact statement (verbatim, lines 1604--1650):**

```
\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
on the Koszul locus; filtered-complete off it
\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}

The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.

Let $\mathcal{A}$ be a \emph{Koszul} chiral algebra on a Riemann surface $X$
(Definition~\ref{def:koszul-chiral-algebra};
equivalently, $\cA \in \operatorname{Kosz}(X)$;
this excludes simple admissible-level quotients and minimal-model
central charges; see Scope below), with
$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ conilpotent or $\mathcal{A}$ complete
with respect to its augmentation ideal
(\S\ref{sec:i-adic-completion}).  Then the natural map:
\[\psi: \Omega(\bar{B}(\mathcal{A})) \longrightarrow \mathcal{A}\]
... is a quasi-isomorphism of \emph{chiral algebras}...

More precisely:
\begin{enumerate}
\item The map $\psi$ is a morphism of chiral algebras (respects all structure)
\item At each genus $g$, the genus-$g$ component:
      \[\psi_g: \Omega_g(\bar{B}_g(\mathcal{A})) \longrightarrow \mathcal{A}_g\]
      is a quasi-isomorphism
\item The full genus-graded map:
      \[\psi = \sum_{g=0}^\infty \hbar^{2g-2}\psi_g: \Omega(\bar{B}(\mathcal{A})) \longrightarrow \mathcal{A}\]
      converges and is a quasi-isomorphism in the $\hbar$-adic completion
\item There exists a spectral sequence converging to $H^\bullet(\mathcal{A})$
      with $E_1$-page given by the bar-cobar complex; it collapses at $E_2$
      by the Koszul property (Theorem~\ref{thm:spectral-sequence-collapse})
\end{enumerate}
```

The author's own self-remark (lines 1686--1695) explicitly states:

```
At genus~$0$, Theorem~\ref{thm:bar-cobar-inversion-qi} is a
consequence of the fundamental theorem of chiral twisting morphisms
(Theorem~\ref{thm:fundamental-twisting-morphisms}):
the counit $\Omega_X(\bar{B}_X(\cA)) \to \cA$ being a
quasi-isomorphism is one of the four equivalent characterizations
of Koszulity established there.  The present theorem extends this
to all genera via the genus induction of clause~(D2).
```

## 4. Definition `def:koszul-chiral-algebra` (the source of the Theorem B circularity)

**File**: `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex`
**Lines**: 223--234.

**Exact statement (verbatim):**

```
\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
\index{Koszul chiral algebra|textbf}
Let $X$ be a smooth projective curve over~$\CC$.
An augmented chiral algebra~$\cA$
(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
if the bar-cobar counit
\[
\varepsilon \colon
\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism at genus~$0$.
\end{definition}
```

---

## 5. Adversarial verdicts

### CLAIM 1 (Theorem A Part (2) = definitional tautology): **CONFIRMED**.

The auditor is right. `def:chiral-koszul-pair` at lines 580--584 explicitly
requires `Verdier-compatible identifications D_Ran(C_1) = C_2` as part of
the definition. The proof of part (2) on lines 3305--3307 reads:
"the Verdier compatibility in Definition~\ref{def:chiral-koszul-pair}
identifies D_Ran(C_1) with C_2". The proof then composes this
already-assumed identification with part (1)'s unit equivalences
C_i = B_X(A_i) to produce D_Ran(B_X(A_1)) = B_X(A_2).

In symbols: **the definition assumes D_Ran(C_1) = C_2, and the proof
re-states this after transporting across C_i = B_X(A_i).** That is a
post-composition of an identity, not a new theorem. Part (2) has no
content beyond part (1) + the definition.

The author partially acknowledges this on lines 590--597 in the
"antecedent hypotheses" paragraph ("Verdier compatibility can all be
verified without invoking bar-cobar duality itself. Theorem...then
proves the full bar-cobar identification as a consequence"), but the
wording obscures the fact that **the Verdier half of the "full bar-cobar
identification" is literally one of the antecedent hypotheses**. The
part that is genuinely proved is part (1) -- the unit/counit
quasi-isomorphisms. Part (3) is cosmetic renaming of (2).

### CLAIM 2 (Theorem B genus-0 = definitional tautology): **CONFIRMED**.

The auditor is right. `def:koszul-chiral-algebra` at lines 223--234 of
`algebraic_foundations.tex` defines "A is Koszul" by the condition
"the bar-cobar counit Omega_X(B_X(A)) -> A is a quasi-isomorphism at
genus 0". Theorem B then asserts: "Let A be a Koszul chiral algebra...
[then] psi: Omega(B(A)) -> A ... is a quasi-isomorphism" including at
each genus g (clause 2), of which g=0 is the base case.

At genus 0 this is verbatim the definition. The author admits this
directly in Remark `rem:inversion-vs-fundamental` (lines 1686--1695):
"the counit...being a quasi-isomorphism is one of the four equivalent
characterizations of Koszulity established there. The present theorem
extends this to all genera". The extension to genus g >= 1 is the
genuine content; the genus-0 clause is an identity on definitions.

The non-trivial content of Theorem B lives entirely in clauses (2)
for g >= 1, (3) (h-adic convergence of the genus series), and (4)
(spectral sequence collapse). Clause (2) at g=0 is tautological.

---

## 6. Proposed fixes

### Fix for CLAIM 1 (Theorem A part (2))

**Preferred fix**: rewrite `def:chiral-koszul-pair` so that it does NOT
presuppose Verdier compatibility, making part (2) genuinely provable.
Replace the "equipped with Verdier-compatible identifications..." clause
with a structural hypothesis that does not already resolve to the
theorem's conclusion. Candidates:

  (a) Require only that `A_1, A_2` are each individually Koszul
      chiral algebras in the sense of `def:koszul-chiral-algebra`,
      plus a quadratic-duality relation between the relation spaces
      (i.e., `A_2 = A_1^!` as classical quadratic algebras). Verdier
      compatibility becomes Theorem A part (2).

  (b) Replace the Verdier clause with a perfect-pairing condition at
      the classical (non-derived) level: a nondegenerate pairing
      `A_1 x A_2 -> k` compatible with the chiral structure. Then
      part (2) lifts this classical pairing to a derived Verdier
      intertwining.

**Alternative fix**: keep `def:chiral-koszul-pair` as-is, but demote
Theorem A part (2) to a Remark or Corollary, explicitly labeled
"immediate consequence of Definition~\ref{def:chiral-koszul-pair}",
and renumber the theorem. The theorem would then read: part (1)
(the unit/counit qi, which is substantive) and an Observation that
the Verdier clause of the definition transports to B_X(A_i).

### Fix for CLAIM 2 (Theorem B genus-0)

**Preferred fix**: rewrite `def:koszul-chiral-algebra` to use an
alternative characterization that does NOT bake in "counit is a qi".
The author's own Remark `rem:equivalent-formulations-koszul` (lines
273--298) lists three equivalent formulations:

  (i)  PBW degeneration (PBW spectral sequence collapses at E_2);
  (ii) Bar concentration: `H^*(B_X(A))` is concentrated in bar degree 1;
  (iii) Acyclicity of the twisted tensor product `B_X(A) otimes_pi A^!`.

**Adopt (i) or (ii) as the definition**, since both are checkable
without computing the cobar construction. Specifically:

```
\begin{definition}[Koszul chiral algebra]
An augmented chiral algebra A is Koszul if H^*(B_X(A)) is
concentrated in bar degree 1 (equivalently, the PBW spectral
sequence collapses at E_2).
\end{definition}
```

With this definition, Theorem B genus-0 becomes a genuine theorem:
from bar-degree concentration, **deduce** that the counit
`Omega(B(A)) -> A` is a quasi-isomorphism. This is the standard
Loday--Vallette bar-cobar inversion result in the chiral setting and
has real content.

**Alternative fix**: narrow Theorem B's scope. State it as:
"Let A be a chiral algebra satisfying the PBW criterion
(Theorem~\ref{thm:pbw-koszulness-criterion}). Then the counit is a
qi at all genera." Drop the genus-0 clause or reduce it to "holds by
definition of Koszul" with no \emph{more precisely} breakdown.

Both fixes require synchronizing approximately 20 call sites that
reference `def:koszul-chiral-algebra` (see grep results in
`koszul-chiral-algebra` and `thm:bar-cobar-inversion-qi` outputs).

---

## 7. Summary

Both adversarial claims are correct. The source of both circularities
is that two foundational definitions (`def:chiral-koszul-pair` and
`def:koszul-chiral-algebra`) both bake in exactly the conclusion that
the flagship theorems A and B then "prove". The fixes are mechanical
but touch many cross-references.

The genuine content of Theorem A is **part (1)**: the unit and counit
of bar-cobar are quasi-isomorphisms on the Koszul locus.

The genuine content of Theorem B is **genus g >= 1**: the higher-genus
inversion and the h-adic convergence of the genus series, plus the
spectral-sequence collapse statement (clause (4)).

Parts that are tautological under current definitions:
- Theorem A part (2) (Verdier intertwining), modulo transport of (1).
- Theorem A part (3) (rewriting in terms of A^!): cosmetic rename of (2).
- Theorem B clause (2) at genus 0: verbatim definition.
