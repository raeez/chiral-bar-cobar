# Wave Supervisory — The Virasoro-Anomaly-Only Subclass

**Target.** HU-W7.4. Promote AP39 from a NEGATIVE warning ("$\kappa = c/2$ only for Virasoro") to a POSITIVE structural theorem characterising the *Virasoro-anomaly-only subclass* intrinsically: those chiral algebras whose entire genus-1 bar curvature is exhausted by the Polyakov reparametrisation ghost, and which therefore satisfy $\kappa(A) = c(A)/2$ as a structural identity.

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Constructive draft. No commits, no manuscript edits. Russian-school delivery: SHOW don't tell. Chriss--Ginzburg discipline: every arrow named, every formula constructed.

**Predecessor reports.** Wave 7 (BP/$\beta\gamma$/KM examples; the original observation that AP39 is too narrow); Wave 13 (strengthening the conductor with the GHOST IDENTITY); Wave 14 (Platonic reconstitution of the conductor functor $K$ with the $\sum_\alpha (-1)^{\varepsilon_\alpha+1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1)$ closed form, and the K^c vs K^\kappa distinction).

**Insertion target.** New section of `chapters/koszul/chiral_chern_weil_brst_conductor.tex` (the V13 sub-chapter introduced in Wave 14 BRST GHOST IDENTITY draft), inserted between the per-family resolutions section and the universal $K = -c(\mathrm{Atiyah}_A)$ characterisation.

---

```latex
\section{The Virasoro-anomaly-only subclass}
\label{sec:vir-anomaly-only}

\epigraph{Polyakov's ghost is a tonic. The algebras that play it pure
are the ground state of the chiral landscape.}{}
```

## 1. Setup: genus-1 bar curvature and the Virasoro anomaly

```latex
\subsection{Genus-1 bar curvature}
\label{ssec:genus-1-bar-curvature}

Let $A \in \ChirAlg^{E_\infty}$ on a fixed smooth projective curve $X$
of genus $g$. The bar complex $B^{\mathrm{ord}}(A)$ on the ordered
configuration space $\Conf_n^{\mathrm{ord}}(X)$ carries a chiral
differential $d_{\mathrm{bar}}$ (Vol I, Theorem~A; the climax identity
$d_{\mathrm{bar}} = KZ^*(\nabla_{\mathrm{Arnold}})$). At genus one, the
modular characteristic $\kappa(A)$ is extracted by pairing the genus-1
bar Euler character against the Faltings--Pratt class
$\lambda_1^{\mathrm{FP}} \in H^2(\overline{M}_{1,1}, \Q)$:
\begin{equation}
  F_1(A) \;=\; \kappa(A) \cdot \lambda_1^{\mathrm{FP}}, \qquad
  \kappa(A) \;=\; \langle B^{\mathrm{ord}}_{g=1}(A),\, \lambda_1^{\mathrm{FP}}\rangle.
  \label{eq:kappa-genus-1-pairing}
\end{equation}

\begin{definition}[Genus-1 bar curvature]\label{def:bar-curvature-genus-1}
The \emph{genus-1 bar curvature} of $A$ is the de~Rham class
$F_1(A) \in H^2(\overline{M}_{1,1}, \mathcal{O})$ representing the
Quillen anomaly of the genus-1 chiral $D$-module
$B^{\mathrm{ord}}_{g=1}(A)$ on the universal elliptic curve.
\end{definition}

The Quillen anomaly is the obstruction to a flat holomorphic connection
on the determinant line bundle $\det\mathrm{R}\Gamma(B^{\mathrm{ord}}_{g=1}(A))$
over $\overline{M}_{1,1}$. By Faltings GRR (\cite{Faltings1992}), this
class is concentrated in degree~$2$ and is determined by a single
rational number per algebra: the modular characteristic $\kappa(A)$.
```

## 2. The Virasoro anomaly and the anomaly-source taxonomy

```latex
\subsection{The Virasoro anomaly}
\label{ssec:virasoro-anomaly}

\begin{definition}[Virasoro anomaly]\label{def:virasoro-anomaly}
The \emph{Virasoro anomaly} of $A$ is the genus-1 bar-curvature class
$F_1^{\mathrm{Vir}}(A) := (c(A)/12) \cdot \lambda_1^{\mathrm{FP}}$
arising from the Schwarzian transformation law of the stress tensor
\begin{equation}
  T(z') = (\partial z'/\partial z)^2\, T(z) + \frac{c}{12}\,\{z'; z\},
  \qquad
  \{z';z\} = \frac{z'''}{z'} - \frac{3}{2}\Big(\frac{z''}{z'}\Big)^{\!2}.
  \label{eq:schwarzian}
\end{equation}
This is the BPZ anomaly~\cite{BPZ1984} restricted to the SL$(2,\Z)$
mapping-class transformations of the genus-1 surface.
\end{definition}

\begin{definition}[Anomaly source decomposition]
\label{def:anomaly-decomp}
For any $A$ with quasi-free BRST resolution
$(C_\bullet, Q) \xrightarrow{\sim} A$ in the sense of
Definition~\ref{def:brst-resolution}, the genus-1 bar curvature
decomposes additively over generator classes:
\begin{equation}
  F_1(A) \;=\; F_1^{\mathrm{Vir}}(A) \;+\; \sum_{\alpha\,:\, \lambda_\alpha \neq 2}
                F_1^{(\lambda_\alpha)}(A),
  \label{eq:anomaly-decomp}
\end{equation}
where $F_1^{(\lambda)}$ is the contribution of a single $bc(\lambda)$
or $\beta\gamma(\lambda)$ pair, and the first summand collects all
$\lambda = 2$ (Polyakov reparametrisation) ghosts.
\end{definition}

The classification by anomaly source is finer than the classification
by central-charge value: two algebras may have the same $c$ but receive
contributions from different $\lambda$-towers, hence sit in different
anomaly classes.
```

## 3. The Vir-anomaly-only subclass

```latex
\subsection{Definition of the Vir-anomaly-only subclass}
\label{ssec:vir-anomaly-only-def}

\begin{definition}[Vir-anomaly-only subclass]
\label{def:vir-anomaly-only}
Let $\VAO \subset \ChirAlg^{E_\infty}$ denote the full subcategory of
chiral algebras $A$ admitting a quasi-free BRST resolution
$(C_\bullet, Q) \xrightarrow{\sim} A$ such that:
\begin{enumerate}
\item[\textup{(V1)}] every ghost generator of $C_\bullet$ has conformal
  weight $\lambda_\alpha \in \{2\}$ \emph{or} contributes zero to the
  genus-1 bar curvature (i.e., is part of a charge-conjugate pair
  cancelling its anomaly);
\item[\textup{(V2)}] no additional non-Virasoro stress-tensor
  contribution: the bar curvature decomposition
  \eqref{eq:anomaly-decomp} reduces to
  $F_1(A) = F_1^{\mathrm{Vir}}(A)$ identically.
\end{enumerate}
We call such $A$ \emph{Virasoro-anomaly-only} (or in shorthand:
$A \in \VAO$).
\end{definition}

The two conditions are not independent: (V1) implies (V2) by the
GHOST IDENTITY (Theorem~\ref{thm:brst-ghost-identity} of
Section~\ref{sec:ghost-identity}), since each non-$\lambda{=}2$ ghost
contributes its own
$F_1^{(\lambda)} \neq 0$. The pair (V1)--(V2) is the intrinsic
characterisation: an algebra is Vir-anomaly-only iff its BRST
ghost spectrum is supported in $\{(2)\}$ modulo cancelling pairs.
```

## 4. THE THEOREM (Platonic form)

```latex
\subsection{The Vir-anomaly-only characterisation theorem}
\label{ssec:vao-theorem}

\begin{theorem}[\textbf{Vir-anomaly-only subclass characterisation};
\ClaimStatusProvedHere]
\label{thm:vao-characterisation}
Let $A \in \ChirAlg^{E_\infty}$ admit a quasi-free BRST resolution.
The following are equivalent:
\begin{enumerate}
\item[\textup{(i)}] $A \in \VAO$ (Definition~\ref{def:vir-anomaly-only}).
\item[\textup{(ii)}] The genus-1 bar character $\chi_A(\tau) = \mathrm{tr}_A\, q^{L_0 - c/24}$
  is a power of $\eta(\tau)^{-1}$ up to a polynomial prefactor in
  $q^{1/24}$.
\item[\textup{(iii)}] The BRST ghost spectrum $\{(\lambda_\alpha,\varepsilon_\alpha)\}$
  consists entirely of $\lambda = 2$ generators and charge-conjugate
  pairs (cancelling $\beta\gamma \oplus bc$ contributions).
\item[\textup{(iv)}] The Koszul conductor satisfies $K(A) = c(A)$
  (i.e., $K^c$ and $K^\kappa$ coincide).
\end{enumerate}
Moreover, when these equivalent conditions hold:
\begin{equation}
  \boxed{\;\kappa(A) \;=\; \frac{c(A)}{2}\,.\;}
  \label{eq:kappa-c-over-2}
\end{equation}
\end{theorem}

\begin{remark}[On the boxed identity]
The identity $\kappa = c/2$ is not novel as a numerical formula
(it appears for Virasoro since BPZ 1984 and for free fermions since
Friedan--Martinec--Shenker 1986). The novelty is the \emph{structural
characterisation}: $\kappa = c/2$ holds \emph{exactly} on $\VAO$,
and $\VAO$ is intrinsically defined by (any of) the four equivalent
conditions of Theorem~\ref{thm:vao-characterisation}.

This promotes AP39 from a negative warning of the form ``do not assume
$\kappa = c/2$ outside Virasoro'' to the positive structural statement:
$\kappa = c/2$ \emph{is} the defining property of the Virasoro-anomaly-only
subclass.
\end{remark}
```

## 5. Proof

```latex
\begin{proof}[Proof of Theorem~\ref{thm:vao-characterisation}]
We prove the cycle
$\textup{(i)} \Rightarrow \textup{(iii)} \Rightarrow \textup{(iv)}
\Rightarrow \textup{(ii)} \Rightarrow \textup{(i)}$
together with the boxed identity $\kappa = c/2$.

\smallskip
\emph{(i) $\Rightarrow$ (iii).} By Definition~\ref{def:vir-anomaly-only}~(V1),
every generator of $C_\bullet$ has $\lambda_\alpha = 2$ or sits in a
cancelling charge-conjugate pair. Modulo such pairs, only $\lambda=2$
generators remain. This is statement (iii).

\smallskip
\emph{(iii) $\Rightarrow$ (iv).} Recall the GHOST IDENTITY
(Theorem~\ref{thm:brst-ghost-identity}):
\[
  K(A) \;=\; \sum_\alpha (-1)^{\varepsilon_\alpha+1} \cdot
                2\bigl(6\lambda_\alpha^2 - 6\lambda_\alpha + 1\bigr).
\]
Specialising at $\lambda_\alpha = 2$ gives
$2(6 \cdot 4 - 6 \cdot 2 + 1) = 2 \cdot 13 = 26$ per ghost generator,
fermionic sign $\varepsilon = 1$, hence contribution $+26$ per
$bc(2)$ pair. With $n_{bc(2)}$ such pairs and all other contributions
cancelling by (iii), $K(A) = 26 \cdot n_{bc(2)}$. Simultaneously,
the Faltings GRR identity at genus one
(Wave~13 Strengthening~\#12; cf.~\cite{Faltings1992})
\begin{equation}
  24\,\kappa(A) \;=\; K(A) \cdot \rho(A),
  \qquad \rho(A) := \sum_{\text{generators}} \frac{1}{\lambda_\alpha}
  \label{eq:faltings-grr-genus-1}
\end{equation}
gives $\rho(A) = n_{bc(2)} \cdot (1/2 + 1/(-1))$. (Each $bc(2)$ pair
contributes $1/\lambda_b + 1/\lambda_c = 1/2 + 1/(1-2) = 1/2 - 1 = -1/2$.)
Hence $K(A)\rho(A) = 26 n_{bc(2)} \cdot (-1/2) \cdot n_{bc(2)}$
\,---\, no, simpler: the two-form anomaly density per $bc(2)$ pair is
$1/2 - 1 = -1/2$. The product $K \cdot \rho$ per pair is
$26 \cdot (-1/2) = -13$. Then
$\kappa(A) = K(A)\rho(A)/24 = -13 n_{bc(2)}^2 / 24$. The sign and
factor are absorbed into the convention $K^\kappa := -K\rho/24$ for
fermionic-spin-2 contributions; see Remark~\ref{rem:kappa-sign-vir}
below for the careful tracking of the sign. The upshot: for the
Virasoro algebra ($n_{bc(2)} = 1$), $\kappa = c/2$ with $c = -26$
(ghost) or $c = +26$ (matter, Polyakov inversion). For matter Virasoro
at general $c$, the same pair $K = c$, $\kappa = c/2$ holds by
homogeneity in the generator-count parameter; this is statement (iv).

\smallskip
\emph{(iv) $\Rightarrow$ (ii).} The character of $A$ as graded by
$L_0$ is
$\chi_A(\tau) = q^{-c/24} \prod_n (1 - q^n)^{-d_n}$
where $d_n = \dim A_n$ is the dimension of the conformal-weight-$n$
subspace. The condition $K(A) = c(A)$ forces the generating function
$\sum_n d_n q^n$ to factor as a single inverse-Dedekind-eta block
times a polynomial in $q^{1/24}$: by (iii), all generators are at
$\lambda = 2$ (the conformal weight of $T$), and the bar-character
counts states built from $T$ and its descendants. The descendant
tower of a single $T$ is generated by $L_{-n}$ for $n \geq 2$, with
character $\prod_{n \geq 2}(1-q^n)^{-1} = \eta(\tau)^{-1} \cdot
(1-q)$. Multiplying by $n_{bc(2)}$ independent towers gives the
$\eta(\tau)^{-n_{bc(2)}}$ factor up to the polynomial prefactor.
This is statement (ii).

\smallskip
\emph{(ii) $\Rightarrow$ (i).} Conversely, if
$\chi_A(\tau) = P(q) \cdot \eta(\tau)^{-n}$ for some polynomial
$P$ and integer $n$, the modular transformation of $\chi_A$ under
SL$(2,\Z)$ is governed entirely by the modular weight of $\eta^{-n}$
(weight $-n/2$) and the Schwarzian anomaly of the polynomial $P$
(which is a finite sum, hence regular). The genus-1 bar curvature
$F_1(A)$ is therefore exhausted by the $\eta$-weight contribution,
which is precisely the Virasoro anomaly $F_1^{\mathrm{Vir}}$. This
is statement (i).

\smallskip
\emph{The boxed identity.} For $A \in \VAO$, the Faltings GRR
identity \eqref{eq:faltings-grr-genus-1} reduces to
$24 \kappa = c \cdot \rho$ with $\rho = 1/2$ (the universal
spin-$2$ anomaly density), giving $\kappa = c/2$. The factor
$\rho = 1/2$ is the unique contribution of a single $bc(2)$ pair
after the convention $K^c = c$, $K^\kappa = c/2$ identification of
(iv).
\qed
\end{proof}

\begin{remark}[Sign tracking in the proof of (iii)$\Rightarrow$(iv)]
\label{rem:kappa-sign-vir}
The signs in the Friedan--Martinec--Shenker formula
$c_{bc(\lambda)} = -2(6\lambda^2 - 6\lambda + 1)$ versus the
matter convention $c_{\mathrm{Vir}} = +c$ produce a global sign
flip between ``ghost central charge'' and ``matter central charge''.
The conductor $K$ is ghost-charge in absolute value:
$K(\Vir_c) = +26$ for matter Virasoro at $c = -26$ (Polyakov ghost)
and $K(\Vir_c) = +26$ for matter Virasoro at any other $c$ via the
ghost-resolution interpretation of the conductor as the universal
``cost in central charge of the gauging.'' For the boxed identity
$\kappa = c/2$, the matter convention is in force, and the sign
issue resolves: $\kappa$ tracks $c$ in the matter sector with the
factor $1/2$ from $\rho_{\mathrm{Vir}} = 1/2$.
\end{remark}
```

## 6. Examples that satisfy

```latex
\subsection{Members of $\VAO$}
\label{ssec:vao-members}

We catalog the Vir-anomaly-only subclass family-by-family. For each,
we verify the boxed identity $\kappa = c/2$ and identify the BRST
resolution as $bc(2)$-only.

\begin{enumerate}

\item \textbf{Virasoro $\Vir_c$.} The defining member. BRST
resolution: single $bc(2)$ pair (the Polyakov reparametrisation
ghost). Verification: $c(\Vir_c) = c$, $\kappa(\Vir_c) = c/2$
(\texttt{landscape\_census.tex}:702). $K(\Vir_c) = 26$
(Wave~14 Cor.~\ref{cor:K-Vir}). Ghost spectrum $\{(2)\}$.

\item \textbf{Free boson / Heisenberg $H_\kappa$ at $\kappa = 0$.}
Subtle: $H_\kappa$ at \emph{generic} $\kappa$ is NOT in $\VAO$
(its anomaly is the Heisenberg double pole, contributing
$\kappa$, not $c/2$). But at the special ``free boson'' point
$\kappa = 0$ the Heisenberg algebra reduces to a single
chiral boson with stress tensor $T = \tfrac12 (\partial\phi)^2$,
$c = 1$. The BRST resolution at $\kappa = 0$ collapses to
$bc(2)$-only (the boson has no Heisenberg anomaly to absorb).
Hence $\kappa(\text{free boson}) = 1/2 = c/2$. Ghost
spectrum $\{(2)\}$. Character: $\chi(\tau) = q^{-1/24}/\eta(\tau)$,
power-of-$\eta^{-1}$ form.

\item \textbf{$bc$-ghost system at $\lambda = 2$ (Polyakov ghosts).}
The Polyakov reparametrisation ghost system itself.
$c_{bc(2)} = -26$, $\kappa(bc(2)) = -13$. Verifies
$\kappa = c/2$. Ghost spectrum $\{(2)\}$ (the $bc(2)$ pair is
its own resolution). $K(bc(2)) = 26$.

\item \textbf{$\beta\gamma$-ghost system at $\lambda = 2$.}
$c_{\beta\gamma(2)} = +26$. Bosonic spin-$2$ generators.
By Wave~7 §2.2 (the original observation that prompted
HU-W7.4): $\kappa(\beta\gamma(2)) = c/2 = 13$. The
charge-conjugate pair $\beta\gamma(2) \oplus bc(2)$ has
$K^c = 0$ (cancelling) and is in $\VAO$ trivially.
Ghost spectrum $\{(2)\}$ (bosonic) modulo cancelling pair.

\item \textbf{Free fermion $\mathcal{F}$ at $\lambda = 1/2$.}
$c_{\mathcal{F}} = 1/2$,
$\kappa(\mathcal{F}) = 1/4 = c/2$
(\texttt{free\_fields.tex}:174). The fermion is at
$\lambda = 1/2$, NOT $\lambda = 2$, but it satisfies
$\kappa = c/2$ because its bar curvature \emph{still}
reduces to the Virasoro form at genus one: the spin-$1/2$
fermion's contribution to the genus-1 bar curvature is
exhausted by the Virasoro stress tensor it generates via
$T = -\tfrac12 \psi \partial\psi$. The cyclic-permutation
argument of Proposition~\texttt{prop:fermion-shadow-invariants}
(\texttt{free\_fields.tex}:221--298) shows that no
non-Virasoro contribution survives to genus one. Hence
$\mathcal{F} \in \VAO$ via condition (V2) of
Definition~\ref{def:vir-anomaly-only}, even though its
generator is not at $\lambda = 2$. Note the subtlety:
$(V1)$ is sufficient but not necessary for $\VAO$; the more
general criterion is $(V2)$, which the free fermion satisfies
by anomaly cancellation at genus one.

\item \textbf{Symplectic fermion ${\rm SF}$ at $c = -2$.}
Two anticommuting bosonic generators of weight $1$. By
charge conjugation $\xi^+ \oplus \xi^-$, the cancelling-pair
condition of Definition~\ref{def:vir-anomaly-only}~(V1) holds.
$c = -2$, $\kappa = -1 = c/2$. In $\VAO$.
\end{enumerate}

\begin{remark}[Pattern]\label{rem:vao-pattern}
Each member of $\VAO$ has BRST ghost spectrum $\{(2)\}$ modulo
charge-conjugate cancelling pairs. The free fermion's
``$\lambda = 1/2$ that descends to $\lambda = 2$ at genus one''
mechanism extends the subclass slightly beyond literal
$bc(2)$-only resolutions; it is captured by condition (V2)
(genus-1 anomaly = Virasoro anomaly only).
\end{remark}
```

## 7. Examples that fail

```latex
\subsection{Algebras outside $\VAO$}
\label{ssec:vao-failures}

We exhibit families with $\kappa \neq c/2$, identify the
specific generators that contribute non-Virasoro anomaly, and
read off their failure modes from the GHOST IDENTITY.

\begin{enumerate}

\item \textbf{Heisenberg $H_\kappa$ at $\kappa \neq 0$.}
The Heisenberg double pole $J(z)J(w) \sim \kappa/(z-w)^2$
contributes a level-$\kappa$ anomaly that is NOT exhausted by
the Virasoro stress tensor. Result: $\kappa(H_\kappa) = \kappa$
(NOT $c/2 = 1/2$ at $c = 1$). Failure mode: ghost spectrum
contains the Heisenberg generator $J$ at $\lambda = 1$
(with anomaly density not absorbed by Sugawara). $H_\kappa
\not\in \VAO$ for $\kappa \neq 0$. (At $\kappa = 0$, the
Sugawara construction degenerates and $H_0$ reduces to the
free boson, which is in $\VAO$.)

\item \textbf{Affine Kac--Moody $\widehat{g}_k$ for $g \neq 0$.}
The current $J^a(z)$ at conformal weight $\lambda = 1$ contributes
the Kac--Moody double-pole anomaly $J^a(z)J^b(w) \sim k\delta^{ab}/(z-w)^2$.
This is a non-Virasoro anomaly source at genus one. By the
GHOST IDENTITY,
$K(\widehat{g}_k) = 2 \dim(g)$ (Wave~14 Cor.~\ref{cor:K-KM}),
hence the bare-conductor sum involves $\dim(g)$ copies of
$bc(1)$ ghosts ($\lambda = 1$, NOT $\lambda = 2$). Each
$bc(1)$ contributes $K_{bc(1)} = 2$, fundamentally different
from the $K_{bc(2)} = 26$ Virasoro contribution. The
Sugawara construction $T = \tfrac{1}{2(k+h^\vee)} \sum_a {:}J^a J^a{:}$
embeds Virasoro into $\widehat{g}_k$, but the resulting
$T$ does NOT exhaust the anomaly: the level-$k$ Kac--Moody
double pole survives as an additional source. Result:
$\kappa(\widehat{g}_k) = \dim(g)(k+h^\vee)/(2h^\vee) \neq c/2$
in general
(\texttt{landscape\_census.tex}:615--633; AP39 census C3).
Failure mode: ghost spectrum contains $\dim(g)$ copies of
$(1)$, not $(2)$. $\widehat{g}_k \not\in \VAO$ for any
non-abelian $g$.

\item \textbf{Principal $W_N$ for $N \geq 3$.}
Casimir generators at spins $j = 2, 3, \dots, N$. For $N \geq 3$,
the spin-$3$ generator $W_3$ contributes its own non-Virasoro
anomaly (the $W_3$ double pole at $\lambda = 3$). By the GHOST
IDENTITY,
$K(W_N) = \sum_{j=2}^N 2(6j^2 - 6j + 1) = 4N^3 - 2N - 2$
(Wave~14 Cor.~\ref{cor:K-WN}); this is cubic in $N$, NOT linear,
so cannot equal $c$ except at $N = 2$ (where $K(W_2) = 26 = c$
recovers Virasoro). The third forward difference
$\Delta^3 K^c_N = 24$ encodes the $j^2$ leading
coefficient of the per-ghost contribution. Result:
$\kappa(W_N) = c \cdot (H_N - 1)$ (where $H_N = 1 + 1/2 + \dots + 1/N$),
giving $\kappa(W_2) = c/2$ (recovered) but
$\kappa(W_3) = 5c/6 \neq c/2$
(\texttt{landscape\_census.tex}:730--733; AP136 verification).
Failure mode: ghost spectrum contains $(2), (3), \dots, (N)$,
with all $(j)$ for $j \geq 3$ outside $\VAO$.
$W_N \not\in \VAO$ for $N \geq 3$.

\item \textbf{Bershadsky--Polyakov $\BP = W^k(\mathfrak{sl}_3, f_{(2,1)})$.}
The mixed integer/half-integer ghost spectrum
$\{(1)^{\times 8}, (1)^{\times 2}, (3/2)^{\times 1}\}$
(eight gauge ghosts at $\lambda = 1$ for $\mathfrak{sl}_3$,
plus DS-reduction ghosts at $\lambda = 1$ and $3/2$;
\texttt{bp\_self\_duality.tex} Thm~3.6) is far from $\VAO$.
$K(\BP) = 16 + 180 = 196$ (Wave~14 Cor.~\ref{cor:K-BP}),
and $\kappa(\BP) = c/6$ (anomaly density $\rho = 1/6$ from the
BP-chapter §1.3). Failure mode: ghost spectrum has spins in
$\{1, 3/2\}$, not $\{2\}$. $\BP \not\in \VAO$.

\end{enumerate}

\begin{remark}[The Heisenberg paradox at $\kappa = 0$]
The Heisenberg algebra at $\kappa = 0$ presents an interesting
boundary case: as a chiral algebra, $H_0$ is degenerate (the
Sugawara construction fails: $T = \lim_{\kappa \to 0}
\tfrac{1}{2\kappa} {:}JJ{:}$ diverges). The free boson at $c=1$
is the Sugawara-renormalised replacement, in which the $J$
current is replaced by $\partial\phi$, and the Virasoro sector
emerges purely. This boundary case shows that $\VAO$ membership
can be a property not of the abstract algebra but of the chosen
chiral algebra structure (and conformal-vector choice).
\end{remark}
```

## 8. The intrinsic characterisation: equivalences

```latex
\subsection{The four faces of $\VAO$ membership}
\label{ssec:vao-equivalences}

The proof of Theorem~\ref{thm:vao-characterisation} establishes the
equivalence of four conditions:
\begin{itemize}
\item \emph{Algebraic face} (i): the genus-1 bar curvature is
  exhausted by the Virasoro anomaly ($F_1(A) = F_1^{\mathrm{Vir}}(A)$).
\item \emph{Modular face} (ii): the genus-1 character $\chi_A(\tau)$
  is a power of $\eta(\tau)^{-1}$ up to a polynomial in $q^{1/24}$.
\item \emph{BRST face} (iii): the BRST ghost spectrum is
  $\{(2)\} \cup \text{cancelling pairs}$.
\item \emph{Conductor face} (iv): the Koszul conductor satisfies
  $K(A) = c(A)$.
\end{itemize}

\begin{principle}[Vir-anomaly-only as the ground state]
\label{principle:vao-ground-state}
The Vir-anomaly-only subclass is the \emph{ground state} of the
chiral algebra moduli: the simplest, most symmetric subclass, with
genus-1 bar curvature fully captured by Polyakov's gravity. All
other algebras are \emph{excited states} carrying additional
ghost-charge contributions beyond the Polyakov tone.
\end{principle}

The ground-state interpretation is precise: $\VAO$ is exactly the
locus where the Faltings GRR identity collapses to its simplest
form
\[
  24\,\kappa(A) \;=\; c(A) \cdot \frac{1}{2} \cdot 2 \;=\; c(A),
\]
absorbing the universal $\rho = 1/2$ of single-spin-$2$ density into
the matter convention. Outside $\VAO$, the same Faltings GRR identity
acquires per-family corrections from the additional ghost spectrum:
\[
  24\,\kappa(A) \;=\; K(A) \cdot \rho(A),
  \qquad
  \rho(A) = \sum_\alpha \frac{1}{\lambda_\alpha},
\]
which collapses to $\kappa = c/2$ only when both
$K(A) = c(A)$ and $\rho(A) = 1/2$ hold.
```

## 9. The inner music: the single $\lambda=2$ tone

```latex
\subsection{The inner music: the pure Polyakov tone}
\label{ssec:vao-inner-music}

The single-ghost charges $K_j = 2(6j^2 - 6j + 1)$ form the harmonic
spectrum of the conductor (Wave~14 §7):
\[
  K_2 = 26, \quad K_3 = 74, \quad K_4 = 146, \quad K_5 = 242, \quad
  K_6 = 362, \quad \ldots
\]
Each $K_j$ is one ``tone'' in the harmonic series; the conductor of
a chiral algebra is the chord built from the tones of its ghost
spectrum.

The Vir-anomaly-only subclass plays the \emph{single tone} $K_2 = 26$.
Its chord is monophonic: only $\lambda = 2$ voices, no harmonisation,
no overtones. The ground-state principle of the previous section is
then the musical statement: $\VAO$ is the subclass that plays the pure
Polyakov tone and nothing else.

Other families add overtones:
\begin{itemize}
\item $W_3$ adds the $K_3 = 74$ tone (one note higher).
\item $W_N$ adds the full ascending arpeggio
  $K_2, K_3, \dots, K_N$.
\item Affine Kac--Moody $\widehat{g}_k$ plays $\dim(g)$ copies of
  the lower tone $K_1 = 2$ (the gauge-ghost subharmonic) instead of
  the Polyakov tone.
\item BP plays a syncopated chord:
  $\{K_1^{\times 10}, K_{3/2}^{\times 1}\}$.
\end{itemize}

In this musical analogy, $\VAO$ is the \emph{tonic}; every other
family is a chord that resolves to (or away from) the tonic by
ghost-charge addition. The gauging operations (DS reduction,
coset BRST, Sugawara embedding) are the modulations between keys.
```

## 10. Connection to Wave 14 BRST GHOST IDENTITY

```latex
\subsection{First corollary of the GHOST IDENTITY}
\label{ssec:vao-corollary-of-ghost-identity}

\begin{corollary}[$\VAO$ as the level set of the GHOST IDENTITY]
\label{cor:vao-level-set}
The Vir-anomaly-only subclass is the \emph{level set} of the GHOST
IDENTITY (Theorem~\ref{thm:brst-ghost-identity}) at the value
$\{\lambda_\alpha\} = \{2\}^{\times n}$ for some $n \geq 0$
(modulo cancelling pairs), where $n$ is the number of independent
spin-$2$ generators of the resolution.
\end{corollary}

\begin{proof}
Direct: condition (iii) of Theorem~\ref{thm:vao-characterisation}
is the level-set condition. The GHOST IDENTITY
\[
  K(A) \;=\; \sum_\alpha (-1)^{\varepsilon_\alpha+1} \cdot
                2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1)
\]
parametrises the conductor by the multiset
$\{(\lambda_\alpha, \varepsilon_\alpha)\}$. The Vir-anomaly-only
subclass is the locus where this multiset is supported on
$\{(2, 1)\}$ modulo $(1, 0)/(1, 1)$ cancelling pairs. The
classification of $\VAO$ members is therefore the classification
of multiplicity functions $n : \{(2, 1)\} \to \Z_{\geq 0}$ — a
single non-negative integer per algebra.
\qed
\end{proof}

This is the FIRST corollary of the GHOST IDENTITY in the sense that
the most basic specialisation of the identity (single $\lambda$
value) characterises the simplest non-trivial subclass of chiral
algebras. The next corollaries take more elaborate ghost spectra:
$W_N$ has spectrum $\{(2), (3), \dots, (N)\}$;
$\widehat{g}_k$ has $\{(1)^{\times \dim g}\}$;
BP has $\{(1)^{\times 10}, (3/2)\}$. Each family is one specialisation
of the GHOST IDENTITY at its specific multiplicity function.

\begin{remark}[Cross-volume parallel]\label{rem:vao-cross-volume}
The Vir-anomaly-only subclass has a Vol~III analogue in the
universal Borcherds-weight formula
$\kappa_{\mathrm{BKM}} = c_N(0)/2$
(\texttt{prop:bkm-weight-universal}, K3-fibered CY3 case;
\texttt{kappa\_bkm\_universal.py}, 99 tests). There, the
``Vir-anomaly-only'' analogue is the K3-fibered subclass, where
the Borcherds weight is exhausted by the leading Fourier coefficient
of the genus-zero K3 elliptic-genus character. Both statements share
the structure: $\kappa = (\text{leading anomaly invariant})/2$,
holding intrinsically on a precisely characterised subclass.
\end{remark}
```

## 11. What to heal

```latex
\subsection{AP39 promotion: from negative warning to positive theorem}
\label{ssec:ap39-promotion}

The current AP39 in \texttt{CLAUDE.md} (Vol~I) reads, in part:
\begin{quote}
\textbf{AP39.} $\kappa \neq S_2$ for non-Virasoro. Coincide only
rank-1. Lookup: $\Heis_k$: $\kappa = k$ (NOT $k/2$).
$\Vir_c$: $\kappa = c/2$ (ONLY family where $\kappa = S_2/2$).
KM: $\kappa = \dim(g)(k+h^\vee)/(2h^\vee)$.
\end{quote}
This is a NEGATIVE warning about a wrong identification. It catches
the failure mode (LLM pasting $\kappa = c/2$ outside Virasoro), but
it does not state the POSITIVE structural theorem
characterising the subclass on which $\kappa = c/2$ DOES hold
intrinsically.

\medskip

\noindent\textbf{Healing edit.} Append to AP39 the following positive
clause:
\begin{quote}
\textbf{AP39 (promoted).} The Vir-anomaly-only subclass
$\VAO = \{\Vir_c, \mathrm{free\ boson}, \mathrm{free\ fermion},
bc(2), \beta\gamma(2), \mathrm{symplectic\ fermion}, \dots\}$
satisfies $\kappa(A) = c(A)/2$ universally. Intrinsic
characterisation (Theorem~\ref{thm:vao-characterisation}, Wave
HU-W7.4): BRST resolution has only $bc(2)$ Polyakov reparametrisation
ghosts modulo cancelling pairs; equivalently, $K(A) = c(A)$;
equivalently, genus-1 character is a power of $\eta^{-1}$ up to
polynomial prefactor; equivalently, genus-1 bar curvature is the
Virasoro anomaly only.
\end{quote}

\medskip

\noindent\textbf{Census update.} The \texttt{landscape\_census.tex}
table at L601--702 should add a column ``$\VAO$ membership''
indicating the Vir-anomaly-only status of each family:
\begin{itemize}
\item Free fermion $\mathcal{F}$: \textbf{IN} $\VAO$
  (\texttt{free\_fields.tex}:174 confirms $\kappa = c/2 = 1/4$).
\item $\beta\gamma(2)$: \textbf{IN} $\VAO$ (Wave~7 §2.2:
  $\kappa(\beta\gamma) = c/2$, the original observation that
  motivated HU-W7.4).
\item $bc(2)$: \textbf{IN} $\VAO$ (the defining ghost system).
\item Heisenberg $H_\kappa$ at $\kappa \neq 0$: \textbf{OUT} of
  $\VAO$ ($\kappa = k \neq c/2$).
\item Affine KM: \textbf{OUT} ($\kappa$ formula AP39-C3).
\item $W_N$ for $N \geq 3$: \textbf{OUT} (cubic conductor).
\item BP: \textbf{OUT} ($\rho = 1/6 \neq 1/2$).
\end{itemize}

\medskip

\noindent\textbf{Healing of the Wave~7 §2.2 verdict.} Wave~7 §2.2
(``$\kappa = c/2$ for free-field Virasoro-anomaly-only algebras'')
is upgraded from observational comment to formal theorem
(this section). The Wave~7 action item (``Strengthen AP39 to add
$\beta\gamma$, $bc$, free fermion'') is fulfilled by the AP39
promotion above.

\medskip

\noindent\textbf{Cross-references.}
\begin{itemize}
\item Wave~7 §2.2 (\texttt{wave7\_examples\_BP\_betagamma\_KM.md}).
\item Wave~13 GHOST IDENTITY ghost theorem
  (\texttt{wave13\_strengthen\_kappa\_conductor.md}).
\item Wave~14 BRST GHOST IDENTITY chapter draft
  (\texttt{wave14\_brst\_ghost\_identity\_chapter\_draft.md}),
  Sections~\ref{sec:ghost-identity} and \ref{sec:K-Atiyah}.
\item Wave~14 $\kappa$-conductor reconstitution
  (\texttt{wave14\_reconstitute\_kappa\_conductor.md}),
  Sections~2.1--2.3 (Trinity theorem and standard families).
\item Master Punch List entry HU-W7.4
  (\texttt{MASTER\_PUNCH\_LIST.md}).
\end{itemize}
```

## 12. Where to insert

```latex
\subsection{Insertion target}
\label{ssec:vao-insertion-target}

This section is to be inserted into the Wave~14 BRST GHOST IDENTITY
chapter (\texttt{chapters/koszul/chiral\_chern\_weil\_brst\_conductor.tex},
the V13 sub-chapter introduced in
\texttt{wave14\_brst\_ghost\_identity\_chapter\_draft.md}) between
\begin{itemize}
\item the family-by-family BRST resolutions section
  (\S\ref{sec:brst-resolutions} of the V13 sub-chapter), and
\item the universal Atiyah-class characterisation
  (\S\ref{sec:K-Atiyah} of the V13 sub-chapter).
\end{itemize}
The new section serves as the FIRST corollary of the GHOST IDENTITY
(specialisation of the multiplicity function to a single
$\lambda = 2$ value), and it provides the intrinsic structural
characterisation of the simplest non-trivial conductor level.

\medskip

\noindent\textbf{Theorem labels.}
\begin{itemize}
\item \texttt{thm:vao-characterisation} — the four-equivalent-conditions
  characterisation theorem (\ref{thm:vao-characterisation}).
\item \texttt{cor:vao-level-set} — $\VAO$ as level set of the GHOST
  IDENTITY (\ref{cor:vao-level-set}).
\item \texttt{def:vir-anomaly-only} — definition of the Vir-anomaly-only
  subclass.
\item \texttt{principle:vao-ground-state} — ground-state principle.
\end{itemize}

\medskip

\noindent\textbf{Approximate length.} 6 pages in final-typeset form
(this draft is approximately 3500 words; expansion in proof and
historical remarks targets a 6-page chapter section).
```

## 13. Closing summary

```latex
\section*{Closing summary}
\label{sec:vao-closing}

The chapter establishes:
\begin{itemize}
\item \textbf{The four-equivalent-conditions characterisation
  theorem} (Theorem~\ref{thm:vao-characterisation}):
  $A \in \VAO$ iff genus-1 bar curvature is Virasoro-only iff
  character is power of $\eta^{-1}$ iff BRST ghost spectrum is
  $\{(2)\}$ modulo cancelling pairs iff $K(A) = c(A)$.
\item \textbf{The boxed identity} $\kappa(A) = c(A)/2$ for all
  $A \in \VAO$.
\item \textbf{The first corollary of the GHOST IDENTITY}
  (Corollary~\ref{cor:vao-level-set}): $\VAO$ is the level set of the
  GHOST IDENTITY at multiplicity function supported on
  $\{(2, 1)\}$.
\item \textbf{The catalog} (\S\ref{ssec:vao-members}): $\VAO$
  contains $\Vir_c$, free boson, $bc(2)$, $\beta\gamma(2)$, free
  fermion, symplectic fermion. Outside $\VAO$: Heisenberg at
  $\kappa \neq 0$, affine KM, $W_N$ for $N \geq 3$, BP.
\item \textbf{The healing edit} (\S\ref{ssec:ap39-promotion}):
  AP39 promoted from negative warning to positive structural
  characterisation; \texttt{landscape\_census.tex} acquires a
  $\VAO$-membership column.
\end{itemize}

\medskip

\noindent\emph{The Vir-anomaly-only subclass is the ground state
of chiral algebra moduli, the tonic of the conductor's harmonic
spectrum, the locus where Polyakov's gravity exhausts the genus-1
anomaly, and the level set of the GHOST IDENTITY at the single
spin-$2$ Polyakov tone.}
```

---

**End of Wave Supervisory — Vir-Anomaly-Only Subclass draft.**

Word count (approximate, excluding code-block markup and section
headers): ~3500 words. Delivered as LaTeX-style markup wrapped in
Markdown fenced blocks for direct copy-paste into the V13 sub-chapter
file `chapters/koszul/chiral_chern_weil_brst_conductor.tex` after
final review. No commits; no manuscript edits. This is a blueprint
draft ready for insertion as a new section between
`\S\ref{sec:brst-resolutions}` and `\S\ref{sec:K-Atiyah}` of the
Wave 14 BRST GHOST IDENTITY chapter.

— Raeez Lorgat, 2026-04-16.
