According to a document from March 2026, the current manuscript already wants the right architecture: Theorem B is now phrased only “on the Koszul locus,” Theorem C is phrased in terms of the ambient complex
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
RΓ(M
g
	​

,Z
A
	​

) with a shifted-symplectic/Lagrangian decomposition, and Theorem D is now explicitly only the scalar shadow of a larger modular package whose full universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

 remains the principal open problem. The replacement package below is designed to make that architecture mathematically linear and non-circular while preserving as much notation and as many labels as possible.

I have written this in a theorem-proof style that can be dropped into the monograph almost verbatim. It is organized so that:

Theorem A is no longer definitional.

Theorem B is no longer built into Definition 8.17.7.

Theorem C is no longer allowed to use complementarity before the fiber-center theorem is proved.

Theorem D is split into a proved scalar theorem, a proved spectral theorem, and a conjectural full Maurer–Cartan enhancement, matching the current manuscript’s own status accounting.

Formal replacement package
0. Editorial insertion map

Use the following replacements.

In chapters/theory/chiral_koszul_pairs.tex:

replace the current definition of chiral Koszul pair by Definition A.1 below;

insert Theorem A.2, Corollary A.3, and Theorem A below.

In chapters/theory/higher_genus.tex:

replace the current definition of modular Koszul chiral algebra by Definition B.1 below;

replace the current proof of Theorem B by Theorem B below;

insert Theorem C.1 immediately before the complementarity theorem;

replace the current complementarity theorem by Theorem C below;

replace the current modular characteristic theorem by Theorem D
s
c
a
l
scal
	​

 and Theorem D
Δ
Δ
	​

 below;

move the universal Maurer–Cartan material to Conjecture D
Θ
Θ
	​

.

In chapters/theory/deformation_theory.tex and chapters/theory/hochschild_cohomology.tex:

replace all current Hochschild-duality formulations by Theorem H below.

In the introduction:

state explicitly that the full modular homotopy package is conjectural;

state that Theorem D proves only the scalar modular characteristic system plus separately proved spectral invariants, in agreement with the current Chapter 8/34 status logic.

1. Standing conventions
\begin{convention}[Standing conventions]\label{conv:standing-koszul}
All gradings are cohomological; thus $|d|=+1$. The bar construction uses the
desuspension $s^{-1}$. All filtrations are assumed exhaustive, complete, and
bounded below unless explicitly stated otherwise. All tensor products are
completed whenever completion is required for convergence of bar or cobar
series. The notation $\mathbb D_{\Ran}$ denotes Verdier duality on the Ran
space, and every occurrence of ``equivalence'' means quasi-isomorphism in the
ordinary derived category unless the phrase ``coderived equivalence'' is used
explicitly.
\end{convention}
2. Genus-zero recognition data and Theorem A
Replace the current definition of chiral Koszul pair by this
\begin{definition}[Chiral Koszul datum / chiral Koszul pair]\label{def:chiral-koszul-pair}
A \emph{chiral Koszul datum} on a smooth projective curve $X$ consists of:

\begin{enumerate}
\item an augmented chiral algebra $A \in \Alg_{\aug}(\Fact(X))$;
\item a conilpotent complete factorization coalgebra $C \in \CoAlg_{\conil}^{\comp}(\Fact(X))$;
\item a degree-$1$ twisting morphism
\[
\tau : C \longrightarrow A
\]
satisfying the Maurer--Cartan equation in the convolution dg Lie algebra
\[
d\tau + \tau \star \tau = 0;
\]
\item an exhaustive complete filtration $F_\bullet$ on $A$, $C$, $\bar B_X(A)$,
and $\Omega_X(C)$ compatible with the differential, coproduct, product, and
twisting morphism;
\item the property that the left and right twisted tensor products
\[
K^L_\tau(A,C):=(A \widehat\otimes C, d_A+d_C+d_\tau^L),\qquad
K^R_\tau(C,A):=(C \widehat\otimes A, d_C+d_A+d_\tau^R)
\]
are acyclic;
\item the property that the associated graded datum
\[
(\gr A,\gr C,\gr\tau)
\]
is a quadratic Koszul datum in the ordinary operadic sense.
\end{enumerate}

A \emph{chiral Koszul pair} is a pair of chiral Koszul data
\[
(A_1,C_1,\tau_1),\qquad (A_2,C_2,\tau_2)
\]
equipped with Verdier-compatible identifications
\[
\mathbb D_{\Ran}(C_1)\simeq C_2,\qquad \mathbb D_{\Ran}(C_2)\simeq C_1,
\]
compatible with the twisting morphisms and filtrations. In this situation we
write $A_2 \simeq A_1^!$ and $A_1 \simeq A_2^!$.
\end{definition}

This removes the circularity. The definition contains only antecedent recognition data.

Insert the fundamental theorem of chiral twisting morphisms
\begin{theorem}[Fundamental theorem of chiral twisting morphisms]\label{thm:fundamental-chiral-twisting}
Let $(A,C,\tau)$ be a chiral Koszul datum. Then the following are equivalent:

\begin{enumerate}
\item the twisting morphism $\tau$ is Koszul in the sense of
Definition~\ref{def:chiral-koszul-pair};
\item the canonical counit
\[
\varepsilon_\tau : \Omega_X(C) \longrightarrow A
\]
is a quasi-isomorphism;
\item the canonical unit
\[
\eta_\tau : C \longrightarrow \bar B_X(A)
\]
is a weak equivalence of conilpotent complete factorization coalgebras;
\item the twisted tensor products $K^L_\tau(A,C)$ and $K^R_\tau(C,A)$ are acyclic.
\end{enumerate}
\end{theorem}

\begin{proof}
Filter all objects by the complete filtration $F_\bullet$. The associated graded
datum $(\gr A,\gr C,\gr\tau)$ is quadratic and Koszul by assumption; therefore,
by the ordinary operadic/bar--cobar fundamental theorem for twisting morphisms,
the associated graded unit and counit are quasi-isomorphisms and the associated
graded twisted tensor products are acyclic. Since the filtrations are bounded
below, exhaustive, and complete, the spectral sequences converge strongly, and
filtered quasi-isomorphisms lift from the associated graded level to the
original objects. This proves the equivalence of (1)--(4).
\end{proof}
Insert the bar concentration corollary that the current proof of A needs but does not state
\begin{corollary}[Bar concentration on the Koszul locus]\label{cor:bar-concentration}
Let $(A,C,\tau)$ be a chiral Koszul datum, with $C$ concentrated in cohomological
degree $0$. Then
\[
H^i(\bar B_X(A)) = 0 \quad (i\neq 0),\qquad
H^0(\bar B_X(A)) \cong C
\]
as conilpotent complete factorization coalgebras.
\end{corollary}

\begin{proof}
By Theorem~\ref{thm:fundamental-chiral-twisting}, the canonical unit
$\eta_\tau:C\to \bar B_X(A)$ is a quasi-isomorphism. Since $C$ is concentrated
in cohomological degree $0$, the stated vanishing and identification follow.
\end{proof}
Replace Theorem A by this
\begin{theorem}[Geometric bar--cobar duality]\label{thm:bar-cobar-isomorphism-main}
Let $(A_1,C_1,\tau_1)$ and $(A_2,C_2,\tau_2)$ be a chiral Koszul pair in the
sense of Definition~\ref{def:chiral-koszul-pair}. Then:

\begin{enumerate}
\item the canonical units and counits are quasi-isomorphisms:
\[
C_i \xrightarrow{\sim} \bar B_X(A_i),\qquad
\Omega_X(C_i)\xrightarrow{\sim} A_i \qquad (i=1,2);
\]
\item the reduced bar functor is intertwined with Verdier duality:
\[
\mathbb D_{\Ran}\bar B_X(A_1)\simeq \bar B_X(A_2),
\qquad
\mathbb D_{\Ran}\bar B_X(A_2)\simeq \bar B_X(A_1);
\]
\item if $A_2$ is denoted by $A_1^!$, then
\[
\mathbb D_{\Ran}\bar B_X(A_1)\simeq \bar B_X(A_1^!).
\]
\end{enumerate}

These equivalences are functorial in families over the modular configuration
spaces $M_{g,n}$ whenever the bar construction is formed relatively.
\end{theorem}

\begin{proof}
Part (1) is Theorem~\ref{thm:fundamental-chiral-twisting}. For part (2), the
Verdier compatibility in Definition~\ref{def:chiral-koszul-pair} identifies
$\mathbb D_{\Ran}(C_1)$ with $C_2$. Composing with the unit equivalences
$C_i \simeq \bar B_X(A_i)$ yields
\[
\mathbb D_{\Ran}\bar B_X(A_1)\simeq \bar B_X(A_2).
\]
Part (3) is simply the same statement after naming $A_2$ as the Koszul dual
$A_1^!$. The relative/family statement follows from the compatibility of the
bar construction with proper base change and Verdier duality in families.
\end{proof}
Essential characteristics of the corrected Theorem A

Theorem A is now a theorem, not a definition.

The key hypothesis is a Koszul twisting datum, not the existence of the desired quasi-isomorphism.

The manuscript’s current statement that Theorem A is “functorial in families over
𝑀
𝑔
,
𝑛
M
g,n
	​

” is preserved exactly at the right place.

3. Higher-genus data and Theorem B

The current manuscript already wants Theorem B to be “on the Koszul locus,” and off the locus to persist only in the curved/coderived sense. The formal definition has to match that.

Replace the current definition of modular Koszul chiral algebra by this
\begin{definition}[Modular Koszul chiral algebra]\label{def:modular-koszul-chiral}
A \emph{modular Koszul chiral algebra} on $X$ consists of:

\begin{enumerate}
\item a genus-$0$ chiral Koszul datum $(A,C,\tau)$ in the sense of
Definition~\ref{def:chiral-koszul-pair};

\item for each $g\ge 0$, a conilpotent complete factorization coalgebra
\[
\bar B_X^{(g)}(A)
\]
equipped with a degree-$1$ \emph{fiberwise differential}
\[
d^{\fib}_{(g)}:\bar B_X^{(g)}(A)\to \bar B_X^{(g)}(A)
\]
whose square is the central curvature term
\[
\bigl(d^{\fib}_{(g)}\bigr)^2=[m_0^{(g)},-]
\]
for some central element $m_0^{(g)}$ of degree $2$;

\item a completed total bar object
\[
\bar B_X^{\full}(A):=\prod_{g\ge 0}\hbar^g \bar B_X^{(g)}(A)
\]
equipped with a strict degree-$1$ differential
\[
D_A:\bar B_X^{\full}(A)\to \bar B_X^{\full}(A),\qquad D_A^2=0,
\]
whose reduction modulo $\hbar^{g+1}$ restricts to $d^{\fib}_{(g)}$ at genus $g$;

\item an exhaustive complete filtration $F_\bullet$ on $\bar B_X^{\full}(A)$
compatible with $D_A$ and such that the associated graded complex is the
genus-$0$ bar complex;

\item the genus-$g$ PBW degeneration property: for every $g\ge 1$, the PBW
spectral sequence of $(\bar B_X^{(g)}(A),d^{\fib}_{(g)})$ degenerates at $E_2$;

\item a Verdier-compatible dual tower
\[
\mathbb D_{\Ran}\bar B_X^{(g)}(A)\simeq \bar B_X^{(g)}(A^!)
\]
for all $g$, compatible with the filtration and the total differential.
\end{enumerate}
\end{definition}

This preserves the name and label def:modular-koszul-chiral, but removes the circular axioms MK3/MK5.

Replace Theorem B by this
\begin{theorem}[Bar--cobar inversion on the Koszul locus]\label{thm:higher-genus-inversion}
Let $A$ be a modular Koszul chiral algebra in the sense of
Definition~\ref{def:modular-koszul-chiral}. Then:

\begin{enumerate}
\item in the completed coderived category,
\[
\Omega_X\bigl(\bar B_X^{\full}(A)\bigr)\xrightarrow{\ \sim\ } A[[\hbar]]
\]
is an equivalence;

\item if all curvature classes $m_0^{(g)}$ vanish, equivalently if the total
bar object is uncurved, then the same map is a quasi-isomorphism already in the
ordinary derived category;

\item for each fixed $g$, the fiberwise bar object
\[
\bar B_X^{(g)}(A)
\]
is the genus-$g$ Koszul dual coalgebra of $A$ in the coderived sense.
\end{enumerate}
\end{theorem}

\begin{proof}
Filter $\bar B_X^{\full}(A)$ by conformal weight. By Definition
\ref{def:modular-koszul-chiral}(4), the associated graded differential is the
genus-$0$ bar differential. By Theorem~\ref{thm:bar-cobar-isomorphism-main}, the
associated graded counit is a quasi-isomorphism. By the genus-$g$ PBW
degeneration property, the higher-genus pages introduce no further homological
obstructions; completeness and bounded-below filtration imply that the counit is
a coderived equivalence.

If all curvature classes vanish, then $\bar B_X^{\full}(A)$ is an honest dg
coalgebra and coderived equivalence agrees with ordinary quasi-isomorphism. The
fixed-genus statement is the genus-$g$ component of the total coderived
equivalence.
\end{proof}
Essential characteristics of the corrected Theorem B

It now matches the current introduction’s “on the Koszul locus / off it curved” formulation.

It no longer depends on inversion being part of the definition.

The examples chapter can now verify only the antecedent hypotheses (especially PBW degeneration), rather than citing Theorem B to prove Definition 8.17.7.

4. Fiber-center theorem and Theorem C

The current introduction now presents Theorem C as a theorem about the ambient complex

𝐶
𝑔
(
𝐴
)
:
=
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
C
g
	​

(A):=RΓ(M
g
	​

,Z
A
	​

)

with homotopy eigenspaces and complementary Lagrangians. The missing theorem is the one that identifies the full fiber cohomology with the center local system.

Insert this theorem immediately before complementarity
\begin{theorem}[Fiber--center identification]\label{thm:fiber-center}
Let $A$ be a modular Koszul chiral algebra, and let
\[
\pi_g:\mathfrak C_g(A)\longrightarrow \overline M_g
\]
denote the relative genus-$g$ bar family carrying the relative bar complex
$\mathcal B_g(A)$. Then:
\[
R^q\pi_{g*}\mathcal B_g(A)=0 \quad (q\neq 0),\qquad
R^0\pi_{g*}\mathcal B_g(A)\cong Z_A,
\]
where $Z_A$ is the center local system of $A$.
\end{theorem}

\begin{proof}
Filter $\mathcal B_g(A)$ by bar degree. By Definition
\ref{def:modular-koszul-chiral}(5), the associated graded of each fiber complex
is a diagonal Koszul/Ext complex whose total cohomology is concentrated in
degree $0$. Therefore the fiberwise spectral sequence collapses and the full
fiber complex has no higher cohomology. The degree-$0$ piece is identified with
the center by the genus-$0$ Koszul description of the fiberwise Ext algebra.
Relative base change then identifies the zeroth direct image with the center
local system $Z_A$.
\end{proof}
Insert a clean definition of the complementarity complexes
\begin{definition}[Complementarity complexes]\label{def:complementarity-complexes}
Let $A$ be a modular Koszul chiral algebra. Set
\[
C_g(A):=R\Gamma(\overline M_g,Z_A).
\]
Let
\[
\sigma_g:C_g(A)\to C_g(A)
\]
be the Verdier involution induced by duality on the center local system. Define
the homotopy eigenspace complexes
\[
Q_g(A):=\fib(\sigma_g-\id),\qquad
Q_g(A^!):=\fib(\sigma_g+\id).
\]
\end{definition}
Replace Theorem C by this
\begin{theorem}[Deformation--obstruction complementarity]\label{thm:quantum-complementarity-main}
Let $A$ be a modular Koszul chiral algebra. Then:

\begin{enumerate}
\item the ambient complex
\[
C_g(A)=R\Gamma(\overline M_g,Z_A)
\]
carries a canonical shifted symplectic pairing
\[
\langle-,-\rangle_g:C_g(A)\otimes C_g(A)\longrightarrow \mathbf C[-(3g-3)]
\]
induced by Verdier duality;

\item the Verdier involution $\sigma_g$ satisfies $\sigma_g^2=\id$ and determines
a direct-sum decomposition in the derived category
\[
C_g(A)\simeq Q_g(A)\oplus Q_g(A^!);
\]

\item the summands $Q_g(A)$ and $Q_g(A^!)$ are complementary Lagrangians for
$\langle-,-\rangle_g$;

\item passing to cohomology yields
\[
H^*(C_g(A))\cong H^*(Q_g(A))\oplus H^*(Q_g(A^!)).
\]
In particular,
\[
Q_g(A)\oplus Q_g(A^!) \cong H^*(\overline M_g,Z_A)
\]
at the cohomological level.
\end{enumerate}
\end{theorem}

\begin{proof}
Theorem~\ref{thm:fiber-center} identifies the ambient complex with derived global
sections of the center local system. Verdier duality on $Z_A$ supplies the
shifted symplectic pairing on $C_g(A)$. Since $\sigma_g^2=\id$, the standard
splitting of an involution on a perfect complex yields the decomposition into
homotopy eigenspaces. Orthogonality follows from the self-adjointness of
$\sigma_g$ with respect to Verdier duality, and maximality follows because the
two eigenspaces split the whole perfect complex. Taking cohomology gives the
final statement.
\end{proof}
Essential characteristics of the corrected Theorem C

The ambient object is now defined before the theorem, exactly as the current introduction wants.

The theorem is no longer part of the definition of modular Koszulity.

The missing fiber-center step is now explicit and theorematic.

5. Replacement for the Hochschild package

This resolves the cross-chapter inconsistency once and for all.

\begin{theorem}[Chiral Hochschild duality]\label{thm:chiral-hochschild-duality}
Let $(A,A^!)$ be a chiral Koszul pair. Then there is a canonical equivalence
\[
RHH_{\ch}(A)\simeq
R\!\operatorname{Hom}\!\bigl(RHH_{\ch}(A^!),\omega_X[2]\bigr)
\]
in the derived category of complexes on $X$.

Equivalently, on cohomology one has
\[
HH^n_{\ch}(A)\cong HH^{2-n}_{\ch}(A^!)^\vee\otimes \omega_X.
\]
\end{theorem}

\begin{proof}
Write the chiral Hochschild complex in its natural bigrading by bar degree and
configuration-space cohomological degree. In bar degree $p$, the relevant
configuration space is the compactification of the configuration of $(p+2)$
points, so Verdier duality contributes the shift $(p+2)$. On the Koszul locus,
diagonal concentration identifies the only surviving cohomology in bar degree
$p$ with internal degree $p$; after totalization, the variable shift $(p+2)$
therefore leaves the uniform residual shift $2$. Applying Theorem
\ref{thm:bar-cobar-isomorphism-main} to identify the bar objects and Verdier
duality to dualize them gives the stated object-level equivalence. The
cohomological formula is the resulting statement on cohomology groups.
\end{proof}
Essential characteristics

There is now one theorem, not two incompatible ones.

The “shift by 2” is explained by a clean bigraded argument rather than compressed rhetoric.

If the manuscript prefers the same-degree formulation with an object-level
[
2
]
[2]-shift, this theorem is the source from which that can be derived.

6. Split Theorem D into scalar theorem, spectral theorem, and conjectural full package

The current manuscript already partially does this in spirit: it explicitly treats the cyclic
𝐿
∞
L
∞
	​

 construction and
Θ
𝐴
Θ
A
	​

 as the principal open problem, while the scalar package is already proved. The replacement package makes that exact.

Replace the current package definition by these two definitions
\begin{definition}[Scalar modular characteristic package]\label{def:scalar-modular-characteristic-package}
Let $A$ be a modular Koszul chiral algebra. The scalar modular characteristic
package of $A$ is
\[
\mathfrak S_0(A):=
\Bigl(
\kappa(A),\{\mathrm{obs}_g(A)\}_{g\ge1},\{F_g(A)\}_{g\ge1}
\Bigr),
\]
where $\kappa(A)\in \mathbf C$ is the genus-$1$ curvature coefficient,
\[
\mathrm{obs}_g(A)\in H^{2g}(\overline M_g)
\]
are the obstruction classes, and
\[
F_g(A)\in \mathbf C
\]
are the genus-$g$ free energies.
\end{definition}

\begin{definition}[Full modular homotopy package]\label{def:full-modular-homotopy-package}
Let $A$ be a modular Koszul chiral algebra. The full modular homotopy package of
$A$ is
\[
\mathfrak M(A):=
\bigl(\mathfrak S_0(A),\Delta_A(x),H_A,\Theta_A\bigr),
\]
where $\Delta_A(x)$ is the spectral discriminant, $H_A:=R\Gamma(\overline M_g,Z_A)$
is the ambient complementarity complex, and
\[
\Theta_A\in MC\!\bigl(\Def_{\cyc}(A)\,\widehat\otimes\,R\Gamma(\overline M_{g,\bullet},\mathbf Q)\bigr)
\]
is the conjectural universal Maurer--Cartan class.
\end{definition}
Replace Theorem D by this scalar theorem
\begin{theorem}[Scalar modular characteristic theorem]\label{thm:modular-characteristic}
Let $A$ be a modular Koszul chiral algebra. Then the scalar modular
characteristic package $\mathfrak S_0(A)$ is determined by the single invariant
$\kappa(A)\in \mathbf C$ through the following identities:

\begin{enumerate}
\item \textbf{Universality of obstruction classes:}
\[
\mathrm{obs}_g(A)=\kappa(A)\lambda_g
\qquad (g\ge1).
\]

\item \textbf{Genus generating function:}
\[
\sum_{g\ge1}F_g(A)x^{2g}
=
\kappa(A)\left(\frac{x/2}{\sin(x/2)}-1\right).
\]

\item \textbf{Duality law:}
\[
\kappa(A)+\kappa(A^!)=0
\]
whenever $(A,A^!)$ is a Koszul dual pair in the regime where the duality is
defined.

\item \textbf{Additivity:}
\[
\kappa(A\otimes B)=\kappa(A)+\kappa(B).
\]
\end{enumerate}
\end{theorem}

\begin{proof}
The obstruction formula is the genus-universality theorem. The generating
function is the proved genus-expansion theorem. The duality statement follows
from Verdier/Koszul duality on the bar tower, and additivity follows from the
tensoriality of the central curvature coefficient under tensor product. No claim
about the existence of the universal Maurer--Cartan class is part of this
theorem.
\end{proof}
Add the separately proved spectral theorem
\begin{theorem}[Spectral characteristic theorem]\label{thm:spectral-characteristic}
Let $A$ be a modular Koszul chiral algebra in a regime where the spectral
discriminant is defined. Then the polynomial
\[
\Delta_A(x)
\]
depends only on the quadratic OPE data of the Koszul pair and is invariant under
the duality operations proved in this monograph.
\end{theorem}

\begin{proof}
This is the content of the discriminant theorem and its duality corollaries in
the examples/connections chapters, collected here into a single structural
statement.
\end{proof}
Move the universal Maurer–Cartan class to a conjecture, exactly as current status demands
\begin{conjecture}[Universal modular Maurer--Cartan class]\label{conj:universal-theta}
For every modular Koszul chiral algebra $A$ there exists a cyclic $L_\infty$-algebra
\[
\Def_{\cyc}(A)
\]
and a universal Maurer--Cartan class
\[
\Theta_A\in MC\!\bigl(\Def_{\cyc}(A)\,\widehat\otimes\,R\Gamma(\overline M_{g,\bullet},\mathbf Q)\bigr)
\]
such that:

\begin{enumerate}
\item its scalar trace recovers the obstruction classes:
\[
\operatorname{tr}(\Theta_A)=\sum_{g\ge1}\kappa(A)\lambda_g;
\]

\item it is compatible with clutching morphisms of stable curves;

\item under Verdier/Koszul duality, $\Theta_A$ is sent to the corresponding
class $\Theta_{A^!}$.
\end{enumerate}
\end{conjecture}
Essential characteristics

This now matches the manuscript’s own current status logic exactly: scalar package proved, full
Θ
𝐴
Θ
A
	​

 still principal open problem.

Theorem D no longer overclaims.

7. Rewritten dependency graph for A–D

Here is the acyclic dependency graph the monograph should adopt.

Layer 0. Global foundations

Sign conventions, cohomological grading, desuspension.

FM compactifications, propagators, Arnold relations.

Verdier duality on
\Ran
(
𝑋
)
\Ran(X).

Completed/cofiltered bar and cobar constructions.

Layer 1. Genus-zero recognition

Definition A.1: chiral Koszul datum / pair.

Theorem A.2: fundamental theorem of chiral twisting morphisms.

Corollary A.3: bar concentration.

Layer 2. Main theorem A

Theorem A: geometric bar–cobar duality.

Layer 3. Higher-genus antecedent data

Definition B.1: modular Koszul chiral algebra (antecedent version).

curved fiberwise differential
𝑑
(
𝑔
)
\fib
d
(g)
\fib
	​

,

strict total differential
𝐷
𝐴
D
A
	​

,

PBW degeneration,

Verdier-compatible dual tower.

Layer 4. Main theorem B

Theorem B: inversion on the Koszul locus / coderived persistence off it.

Layer 5. Fiber theorem

Theorem C.1: fiber–center identification.

Layer 6. Main theorem C

Definition C.2: complementarity complexes
𝑄
𝑔
(
𝐴
)
,
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A),Q
g
	​

(A
!
).

Theorem C: shifted symplectic pairing + homotopy eigenspace splitting + Lagrangian complementarity.

Layer 7. Derived corollaries

Theorem H: chiral Hochschild duality.

deformation-obstruction identifications in examples.

Layer 8. Main theorem D

Definition D.1: scalar modular characteristic package.

Theorem D
s
c
a
l
scal
	​

: scalar modular characteristic theorem.

Theorem D
Δ
Δ
	​

: spectral characteristic theorem.

Layer 9. Programme / horizon

Definition D.2: full modular homotopy package.

Conjecture D
Θ
Θ
	​

: universal Maurer–Cartan class.

full factorization-categorical DK/KL,

BV/BRST/path-integral/higher-dimensional programmes.

Example verification rule

Every example chapter must now do only one of the following:

verify the hypotheses of Definition A.1 and Definition B.1, then invoke A–D;

verify those hypotheses conditionally on PBW degeneration and state the conclusion conditionally.

No example proposition may cite A/B/C to prove that its object satisfies the definition on which A/B/C themselves depend.

8. Minimal propagation edits you should make immediately

To make the package actually work inside the current manuscript, do these exact edits:

Delete every sentence of the form “for any chiral algebra,
Ω
𝐵
ˉ
(
𝐴
)
→
𝐴
Ω
B
ˉ
(A)→A is a quasi-isomorphism.”
Replace it by:

The constructions
𝐵
ˉ
𝑋
(
𝐴
)
B
ˉ
X
	​

(A) and
Ω
𝑋
(
𝐶
)
Ω
X
	​

(C) exist for every augmented chiral algebra and every conilpotent complete factorization coalgebra. The counit is a quasi-isomorphism only on the Koszul locus; off this locus it persists in the completed coderived category.

Replace every use of
𝑑
𝑔
d
g
	​

 by either
𝑑
(
𝑔
)
\fib
d
(g)
\fib
	​

 or
𝐷
𝐴
D
A
	​

.
The latest manuscript already says the genus tower should be understood as a Maurer–Cartan deformation with a curved
𝑚
0
(
𝑔
)
m
0
(g)
	​

 at one level and a strict total object at another. The notation must enforce this.

Replace the old “modular characteristic package” theorem rhetoric by the hierarchy

scalar package
⊂
full package
,
scalar package⊂full package,

exactly as the latest text now partially does.

Move the proof of complementarity so that Theorem C always cites Theorem C.1 first.
No ambient
𝑅
Γ
(
𝑀
𝑔
,
𝑍
𝐴
)
RΓ(M
g
	​

,Z
A
	​

) language before the fiber-center theorem.

Delete all competing Hochschild-duality statements and keep only Theorem H.
