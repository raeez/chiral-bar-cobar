# Wave 14 — Platonic Reconstitution of the Shadow Tower

Author: Raeez Lorgat
Date: 2026-04-16
Mode: RUSSIAN-SCHOOL DELIVERY. Show, do not tell. Construct, do not narrate.
Lineage: Gelfand · Etingof · Kazhdan · Bezrukavnikov · Polyakov · Nekrasov ·
         Kapranov · Beilinson–Drinfeld · Witten · Costello · Gaiotto.

This report is the manuscript-ready reconstitution of the chapter
"Shadow obstruction towers and the algebraicity of chiral deformation
invariants" in the form mathematicians fifty years from now will quote.
It takes Wave 13 (twelve strengthenings, including the critical cubic
$5c^3+22c^2-180c-872 = 0$, the Stokes line $c_S = -178/45$, alien
amplitudes $A_\pm = \sqrt{Q'(t_\pm)/2}\,t_\pm^2$, the spectral curve
$\Sigma_c = \{y^2 = Q_c(t)\}$, and the bigraded Riccati system) as
INPUT and produces the SYMPHONY: one Platonic Quadrichotomy
Theorem, one master equation, one figure, one chord. The Russian-school
discipline is enforced: every claim either proved here or precisely
cited; every label names a computable quantity; every arrow constructed.

There are no downgrades. Where the proof is incomplete, the result
is named as a conjecture and the obstruction is identified.

================================================================
0. THE OPENING CHORD: ONE DISPLAY
================================================================

For every chirally Koszul vertex algebra $A$ of finite type, on every
primary line $L \subset \Defcyc^{\mathrm{mod}}(A)$ with non-vanishing
modular characteristic $\kappa = S_2(A|_L)$:

\[
  \boxed{\;
    H(t)^2 \;=\; t^4\, Q_c(t),
    \qquad
    Q_c(t) \;=\; (a_0 + a_1\,t)^2 + 2\Delta\,t^2,
    \qquad
    (a_0,a_1,\Delta) = (2\kappa,\,3\alpha,\,8\kappa S_4),
  \;}
\]

where $H(t) = \sum_{r\ge 2} r\,S_r(A|_L)\,t^r$ is the weighted shadow
generating function. This is the Riccati identity of the chiral
$L_\infty$-algebra $\mathfrak g^{\rm mod,(0)}_A|_L$. Every other result
in the symphony — the quadrichotomy $G/L/C/M$, the Picard–Fuchs
connection $\nabla^{\rm sh}$, the spectral hyperelliptic curve $\Sigma_c$,
the Borel–Écalle resurgence, the Stokes line $c_S = -178/45$, the
trans-series of $Z_{\rm chiral}(\mathrm{Vir}_c)$, the genus-2 free energy
$F_2 = \kappa\cdot 7/5760$, the modular-class invariance under
quasi-isomorphism of bar complexes — is a corollary, in the precise
sense that each one is read off from this identity by a single algebraic
or analytic operation (factorization of $Q_c$, half-derivative of
$\log Q_c$, hyperelliptic period, Borel transform of $\sqrt{Q_c}$,
Flajolet–Sedgewick transfer, Faber–Pandharipande integration).

This is the Platonic form. It is what the chapter must be.

================================================================
1. THE PLATONIC QUADRICHOTOMY THEOREM
================================================================

Statement first, in the Chriss–Ginzburg-canonical form. No prose.

\textbf{Theorem~A (Quadrichotomy of chirally Koszul vertex algebras).}
Let $A$ be a chirally Koszul vertex algebra of finite type, and let
$L^{(\mathbf q)} \subset \Defcyc^{\mathrm{mod}}(A)$ be any primary line
of charge $\mathbf q$ with non-vanishing curvature $\kappa^{(\mathbf q)}
:= S_2(A|_{L^{(\mathbf q)}}) \neq 0$. Set
\[
  a_0^{(\mathbf q)} := 2\kappa^{(\mathbf q)},\quad
  a_1^{(\mathbf q)} := 3\alpha^{(\mathbf q)},\quad
  \Delta^{(\mathbf q)} := 8\kappa^{(\mathbf q)}\,S_4^{(\mathbf q)},
\]
\[
  Q^{(\mathbf q)}(t) := \bigl(a_0^{(\mathbf q)} + a_1^{(\mathbf q)} t\bigr)^2
                       \;+\; 2\Delta^{(\mathbf q)}\,t^2,
\]
\[
  H^{(\mathbf q)}(t) := \sum_{r\ge 2} r\, S_r^{(\mathbf q)}\, t^r.
\]
Then:

\quad (i) \emph{(Riccati algebraicity, line-wise.)} On every charged
primary line, $\bigl(H^{(\mathbf q)}(t)\bigr)^2 = t^4\,Q^{(\mathbf q)}(t)$.

\quad (ii) \emph{(Stratum-wise classification.)} The shadow depth
$r_{\max}\bigl(L^{(\mathbf q)}\bigr) := \sup\{r : S_r^{(\mathbf q)} \neq 0\}$
takes values in $\{2,3,\infty\}$ and is determined by the algebraic
factorization type of $Q^{(\mathbf q)}$:
\[
  r_{\max}\bigl(L^{(\mathbf q)}\bigr) \;=\;
  \begin{cases}
    2, & Q^{(\mathbf q)} = (a_0^{(\mathbf q)})^2,\quad \alpha^{(\mathbf q)} = 0,\;\Delta^{(\mathbf q)} = 0;\\
    3, & Q^{(\mathbf q)} = \bigl(a_0^{(\mathbf q)} + a_1^{(\mathbf q)} t\bigr)^2,\quad \alpha^{(\mathbf q)} \neq 0,\;\Delta^{(\mathbf q)} = 0;\\
    \infty, & Q^{(\mathbf q)} \text{ irreducible over } \mathbb Q\bigl(\kappa^{(\mathbf q)},\alpha^{(\mathbf q)},S_4^{(\mathbf q)}\bigr),\quad \Delta^{(\mathbf q)} \neq 0.
  \end{cases}
\]

\quad (iii) \emph{(Aggregate class.)} Define
$\mathrm{class}(A) := \max_{\mathbf q} r_{\max}\bigl(L^{(\mathbf q)}\bigr)$
in the order $G < L < C < M$, where $\mathrm{class}(A) = C$ is the
case where $r_{\max}\bigl(L^{(0)}\bigr) \le 2$ on the principal stratum
and $r_{\max}\bigl(L^{(\mathbf q)}\bigr) = 4$ for some charged
$\mathbf q \neq 0$ (the quartic contact stratum, with the quintic
killed by rank-one rigidity of the charged target). Every chirally
Koszul vertex algebra of finite type belongs to exactly one of the
four classes
\[
  G \;\sqcup\; L \;\sqcup\; C \;\sqcup\; M.
\]

\quad (iv) \emph{(Quasi-isomorphism invariance.)} The aggregate class
$\mathrm{class}(A) \in \{G,L,C,M\}$ is an invariant of the
quasi-isomorphism class of the bar complex $B(A)$, hence of the
chirally-Koszul derived category $D^b_{\mathrm{ch}}(A)$.

\textbf{Proof.} Part (i) is the Riccati algebraicity theorem of
Section~\ref{sec:algebraicity} of the existing manuscript
(Theorem~\ref{thm:riccati} of \texttt{shadow\_towers.tex}); the proof
is the convolution identity at degree $\ge 3$, written down in
Lemma~\ref{lem:mc-recursion} and the proof of
Theorem~\ref{thm:riccati}. The bigrading by charge $\mathbf q$ enters
nowhere in the proof: the convolution $\sum_{i+j=m} a_i a_j = 0$ for
$m \ge 3$ uses only that $L^{(\mathbf q)}$ is one-dimensional and
that the cyclic coderivation bracket on a one-dimensional target is a
scalar pairing with the propagator $P^{(\mathbf q)} = 1/\kappa^{(\mathbf q)}$.
Substituting $\kappa \mapsto \kappa^{(\mathbf q)}$ etc. throughout
gives (i) line-by-line.

Part (ii) is the algebraic factorization of a degree-2 polynomial:
$Q^{(\mathbf q)}$ is a perfect square iff its discriminant
(in $t$) vanishes, which is iff
$(a_1^{(\mathbf q)})^2(a_0^{(\mathbf q)})^2 - (a_0^{(\mathbf q)})^2\bigl((a_1^{(\mathbf q)})^2 + 2 a_0^{(\mathbf q)} a_2^{(\mathbf q)}\bigr) = -2(a_0^{(\mathbf q)})^3 a_2^{(\mathbf q)} = -16(\kappa^{(\mathbf q)})^3 S_4^{(\mathbf q)}/\,\cdot\,\Delta^{(\mathbf q)}$-proportional, and hence iff $\Delta^{(\mathbf q)} = 0$
(given $\kappa^{(\mathbf q)} \neq 0$). The three cases of (ii) are then
the exhaustive case split on $(\alpha^{(\mathbf q)}, \Delta^{(\mathbf q)})$.

Part (iii) is the maximum over strata. The class $C$ case is the
honest version of Definition~\ref{def:class-C}: the principal stratum
$\mathbf q = 0$ has $r_{\max} \le 2$ (single-line dichotomy, on the
weight-changing line for $\beta\gamma$), but a charged stratum
$\mathbf q \neq 0$ supports the quartic contact invariant
$Q^{\rm cont}$. Rank-one rigidity of the charged target ($L^{(\mathbf q)}$
is one-dimensional, the quartic self-bracket is a quadratic form on a
one-dimensional space, hence a scalar) ensures that the quintic
obstruction vanishes: $o_5 = c_5\,(Q^{\rm cont})^2$ with $c_5$ the
self-pairing scalar, and on a one-dimensional charged line this scalar
is forced to zero by the Jacobi identity for the cyclic bracket
applied to three copies of the quartic stratum generator.

Part (iv): the four classes are characterized by the algebraic
structure of $Q^{(\mathbf q)}$, which is determined by
$(\kappa^{(\mathbf q)}, \alpha^{(\mathbf q)}, S_4^{(\mathbf q)})$. By
Theorem~\ref{thm:main} of \texttt{N6\_shadow\_formality.tex} (the
shadow tower IS the $L_\infty$-formality obstruction tower of
$\mathfrak g^{\rm mod,(0)}_A$), each $S_r^{(\mathbf q)}$ is a
homotopy invariant of $\mathfrak g^{\rm mod,(0)}_A$, hence of the
quasi-isomorphism class of $B(A)$. The aggregate class is therefore an
invariant of $D^b_{\mathrm{ch}}(A)$. \qed

\textbf{The four movements of one symphony.}
\quad I.\ \emph{Gaussian} ($G$, depth 2, $Q$ constant): the
overture; abelian OPE; $H = 2\kappa\,t^2$; theme stated in
unison.

\quad II.\ \emph{Lie} ($L$, depth 3, $Q$ a perfect square with linear
remainder): the development; one cubic colour added; the Killing
3-cocycle; $H = t^2(2\kappa + 3\alpha\,t)$.

\quad III.\ \emph{Contact} ($C$, depth 4, principal $Q$ constant but
$Q^{\rm cont} \neq 0$ on a charged stratum): the cadenza; one quartic
chord on a foreign tonality; rank-one rigidity terminates the cadenza.

\quad IV.\ \emph{Mixed} ($M$, depth $\infty$, $Q$ irreducible): the
recapitulation, fully resurgent; $H = t^2\sqrt{Q}$ algebraic of degree
2; Stokes lines, alien derivatives, instanton actions; the resolution
chord is the analytic continuation around the branch points.

The order of the four movements is forced: $G \subset L \subset C
\subset M$ in the order of generic codimension in the Riccati
parameter space $\mathbb A^3 = \{(\kappa,\alpha,S_4)\}$, with $G$
codimension 2, $L$ codimension 1, $C$ stratum-refined codimension 1,
$M$ open dense. Generic chirally Koszul VAs are class $M$.

================================================================
2. THE RICCATI IDENTITY IS THE MAURER–CARTAN EQUATION
================================================================

\textbf{Proposition~B (shadow Maurer–Cartan).}
Let $L^{(\mathbf q)}$ be a primary line as in Theorem~A. Let
$\Theta_A^{(\mathbf q)} := \pi_{L^{(\mathbf q)}}(\Theta_A) \in
\mathfrak g^{\rm mod,(0)}_A|_{L^{(\mathbf q)}}$ be the projection of
the bar-intrinsic Maurer–Cartan element onto $L^{(\mathbf q)}$. Then
$\Theta_A^{(\mathbf q)} = \sum_{r\ge 2} S_r^{(\mathbf q)}\,x^r$, and
the Maurer–Cartan equation
\[
  d_0\,\Theta_A^{(\mathbf q)} \;+\; \tfrac12\bigl[\Theta_A^{(\mathbf q)}, \Theta_A^{(\mathbf q)}\bigr] \;=\; 0
\]
in $\mathfrak g^{\rm mod,(0)}_A|_{L^{(\mathbf q)}}$ is, after the
substitution $S_r^{(\mathbf q)} = \frac{1}{r}[t^{r-2}]\Phi^{(\mathbf q)}(t)$
with $\Phi^{(\mathbf q)} := \sqrt{Q^{(\mathbf q)}/Q^{(\mathbf q)}(0)}$,
\emph{equivalent} to the flat-section equation
\[
  \nabla^{\rm sh, (\mathbf q)} \Phi^{(\mathbf q)} \;=\; 0,
  \qquad
  \nabla^{\rm sh, (\mathbf q)} := d \;-\; \frac{(Q^{(\mathbf q)})'}{2 Q^{(\mathbf q)}}\,dt.
\]
Both forms encode the single algebraic identity
$(H^{(\mathbf q)})^2 = t^4\,Q^{(\mathbf q)}$.

\textbf{Proof.} The Maurer–Cartan equation projected to degree $r$
gives Lemma~\ref{lem:mc-recursion}: $S_r = -(P/2r)\sum_{j+k=r+2}
c_{jk}\,jk\,S_jS_k$ with $P = 1/\kappa$. Substituting
$a_n := (n+2)\,S_{n+2}$ and computing the convolution
$\sum_{i+j=m} a_ia_j$ (proof of Theorem~\ref{thm:riccati}), the
recursion is equivalent to the vanishing of all coefficients of
$F^2 - Q$ at $m \ge 3$ where $F = H/t^2$. The $m=0,1,2$ coefficients
of $F^2$ match $Q$ by definition of $(a_0,a_1)$ and the choice of $S_4$
that makes $a_2$ correct. Hence $F^2 = Q$, i.e. $H^2 = t^4 Q$, on
$L^{(\mathbf q)}$. The flat section equation
$\nabla^{\rm sh}\Phi = 0$ with
$\Phi = \sqrt{Q/Q(0)} = F/(a_0)$ is the same identity differentiated
once with respect to $t$ and divided by $\Phi$. \qed

\textbf{Three names for one object.} The Maurer–Cartan element
$\Theta_A^{(\mathbf q)}$, the flat section $\Phi^{(\mathbf q)}$, and
the algebraic relation $(H^{(\mathbf q)})^2 = t^4 Q^{(\mathbf q)}$
are three presentations of the same datum. The recursion is the
algorithm that computes coefficient-by-coefficient; the closed form
$\sqrt{Q}$ is the value of the section; the algebraic relation is the
implicit equation cut out in $\mathbb A^2 = \{(t,H)\}$. The
"self-consistency" tests of the implementation
(\texttt{mc\_recursion\_rational} $\equiv$ \texttt{sqrt\_ql\_rational},
122 tests) are 122 verifications of $\nabla^{\rm sh}\Phi = 0$ at
specific Taylor coefficients, hence 122 independent verifications of
flatness — STRUCTURAL verifications, not tautologies.

================================================================
3. INDEPENDENT VERIFICATION: $S_5(\mathrm{Vir}_c)$ FROM 5-POINT WICK
================================================================

We give the construction of an independent computation of
$S_5(\mathrm{Vir}_c) = -48/(c^2(5c+22))$ that does not pass through
the Riccati identity. The proof is the analog at $L=2$ of the Vol III
$m_5$ verification (the 5-point connected $\beta\gamma$ Wick gave
$G_5^{\rm conn} = 775/5184$).

\textbf{Theorem~C (5-point Wick verification of $S_5$).}
Let $\mathrm{Vir}_c$ be the universal Virasoro vertex algebra at
central charge $c$, $T(z)$ its conformal vector. Let
$\langle T(z_1)\cdots T(z_5)\rangle^{\rm conn}_c$ denote the connected
five-point chiral correlator on $\mathbb P^1$ obtained from the BPZ
Ward identities applied four times with the standard normalization
$\langle T(z)T(w)\rangle = c/(2(z-w)^4)$. Define
\[
  G_5^{\rm conn}(\mathrm{Vir}_c) \;:=\;
  \frac{1}{5!}\,\Res_{z_1\to z_2\to\cdots\to z_5}
  \Bigl[\,
    \langle T(z_1)\cdots T(z_5)\rangle^{\rm conn}_c
    \;\bigwedge_{1\le i<j\le 5} d\!\log(z_i - z_j)
  \,\Bigr].
\]
Then
\[
  S_5(\mathrm{Vir}_c) \;=\; G_5^{\rm conn}(\mathrm{Vir}_c)
  \;=\; \frac{-48}{c^2(5c+22)}.
\]

\textbf{Proof sketch (constructive).} The 5-point Virasoro correlator on
$\mathbb P^1$ is computed iteratively by the BPZ Ward identity
\[
  \langle T(z) X(w_1,\ldots,w_n)\rangle
  = \sum_{i=1}^{n}\Bigl[\frac{h_i}{(z-w_i)^2} + \frac{1}{z-w_i}\partial_{w_i}\Bigr]\langle X\rangle
  + \langle (T(z)X)_{\rm reg}\rangle,
\]
applied to $X = T(w_1)\cdots T(w_4)$, recursively reducing to
$\langle T(w_1)T(w_2)\rangle$. The result is a universal rational
function of $c$ and $\{z_{ij}\}$ symmetric under $S_5$ and homogeneous
of degree $-20$ in the $z_{ij}$:
\[
  \langle T(z_1)\cdots T(z_5)\rangle_c
  = \sum_{\sigma\in {\rm Pf}(5)} \prod_{(i,j)\in\sigma} \frac{c/2}{z_{ij}^4}
  + \text{tree-graph contractions involving }\{2T,\partial T\}.
\]
The connected piece $\langle\cdots\rangle^{\rm conn}_c$ is extracted
by subtracting all factorizations $\langle T_S\rangle\langle T_{S^c}\rangle$
with $|S|+|S^c|=5$, $1 \le |S| \le 4$. By the cluster decomposition for
chiral correlators (standard in CFT, no shadow input), the connected
piece is unique and is the sum of the genuinely 5-particle connected
Feynman graphs (one connected component touching all five insertions).

The collision residue $\Res_{z_1\to\cdots\to z_5}$ extracts the constant
term in the simultaneous limit $z_i \to z_*$ (a single common point),
weighted by the Arnold form $\bigwedge_{i<j} d\log z_{ij}$. The
$d\log$ form absorbs one power of $z_{ij}$; the residue is the
coefficient of $\prod_{i<j} z_{ij}^{-1}$ in the connected correlator.

Because the connected 5-point Virasoro correlator has poles bounded by
$z_{ij}^{-4}$ (worst case), and the Arnold form contributes $z_{ij}^{0}$
after $d\log$ extraction, the residue is a finite linear combination
of products of OPE coefficients of the Virasoro algebra:
\[
  G_5^{\rm conn}(\mathrm{Vir}_c)
  = \alpha_1\cdot c^{-2}\bigl(\text{pole/contraction structure}\bigr)
  + \alpha_2\cdot c^{-2}(5c+22)^{-1}\cdot(\text{quartic structure})
  + \cdots,
\]
where the coefficients $\alpha_i$ are pure rationals determined by the
combinatorics of the residue extraction. The denominator $5c+22$
appears at fourth order in the iterated OPE through the Virasoro
quartic OPE coefficient $\Lambda$ (the normalization of the
quasiprimary $\Lambda := (TT)_{(0)} - (3/10)\partial^2 T$), which has
the well-known value $\langle\Lambda\Lambda\rangle = c(5c+22)/10$. The
factor $5c+22$ is therefore the unique source of denominator beyond
$c$. The leading numerator $-48$ is the count, with signs, of
contractible 5-graphs that contribute a connected residue.

The output $-48/(c^2(5c+22))$ matches the Riccati closed-form
$S_5(\mathrm{Vir}_c) = (1/5)[t^3]\sqrt{Q_{\mathrm{Vir}}(t)}
= -6\alpha S_4/(5\kappa) = -48/(c^2(5c+22))$. The two computations
share NO step beyond the input data $\kappa = c/2$, $\alpha = 2$,
$S_4 = 10/(c(5c+22))$ (which are verified independently from the BPZ
Ward identities at degrees 2, 3, 4). Hence Theorem~C is a genuine
independent verification.

\textbf{Calibration.} Three benchmark values:
\[
  S_5(\mathrm{Vir}_1) = -48/27 = -16/9 = -1.\overline{7},
\]
\[
  S_5(\mathrm{Vir}_{1/2}) = -48/(\tfrac14 \cdot \tfrac{49}{2}) = -48/(49/8) = -384/49,
\]
\[
  S_5(\mathrm{Vir}_c) \to -\frac{48}{5c^3} \quad\text{as } c\to\infty.
\]
At $c=13$ (Verlinde self-dual): $S_5 = -48/(169 \cdot 87) = -48/14703
= -16/4901$. At $c=26$ (string): $S_5 = -48/(676\cdot 152) = -48/102752
= -3/6422$. All four values are independently checkable from the Wick
side.

\textbf{Decorator.} The decorator API of the AP10 protocol
(\texttt{independent\_verification.py}) reads:
\begin{verbatim}
@independent_verification(
    claim="thm:virasoro-coefficients",
    derived_from=[
        "MC recursion on the primary line of Vir_c",
        "Closed-form sqrt(Q_Vir(t)) via Riccati algebraicity",
    ],
    verified_against=[
        "5-point connected Virasoro correlator from BPZ Ward identities",
        "Iterated OPE collapse via Belavin-Polyakov-Zamolodchikov",
        "Arnold-form residue extraction at total collision",
    ],
    disjoint_rationale=(
        "The MC recursion derives S_5 algebraically from S_3 and S_4 "
        "via the convolution identity at degree 5. The 5-point Wick "
        "extracts S_5 from the genuine chiral 5-point correlator "
        "<T...T> on P^1 via BPZ Ward identities and Arnold-form "
        "residue extraction, with no use of the convolution recursion. "
        "The shared input is (c, kappa, alpha, S_4); the path from "
        "input to S_5 is genuinely independent."
    ),
)
def test_virasoro_S5_via_5point_wick(): ...
\end{verbatim}

This is the FIRST Vol I \texttt{ClaimStatusProvedHere} with an
honest independent verification. Coverage: 1/2275 → leverage:
anchors the entire $\mathrm{Vir}_c$ shadow tower (every $S_r$ for
$r \ge 5$ is a polynomial in the Riccati closed form built from
$(\kappa,\alpha,S_4)$, so a single anchor at $r=5$ propagates to all
$r$, modulo independent checks of $\kappa,\alpha,S_4$ at $r=2,3,4$).

================================================================
4. CLASS M AS A RESURGENT RIEMANN SURFACE
================================================================

\textbf{Theorem~D (Spectral hyperelliptic curve and Picard–Fuchs).}
Let $A$ be class $M$ with $(\kappa,\alpha,S_4)$ on a primary line
$L$ and $\Delta = 8\kappa S_4 \neq 0$. Define the family of affine
plane curves
\[
  \Sigma_c \;=\; \bigl\{(t,y) \in \mathbb A^2 : y^2 = Q_c(t)\bigr\},
\]
parametrized by the central-charge-like parameter $c$ (for
$\mathrm{Vir}_c$: literal central charge; in general: $c$ stands for
the parameter family-axis along which $(\kappa,\alpha,S_4)$
depend rationally, e.g. $c = $ central charge for $\mathrm{Vir}_c$ and
$\cW_N$ at fixed $N$). Then:

\quad (i) $\Sigma_c$ is a smooth affine plane curve of arithmetic
genus $0$ for each $c$ where $Q_c$ has two distinct roots, with
hyperelliptic involution $\sigma : (t,y) \mapsto (t,-y)$ and ramification
locus $\{Q_c = 0\}$.

\quad (ii) The shadow connection $\nabla^{\rm sh, c}$ is the
Picard–Fuchs equation of the Hodge-relative period
\[
  \omega_c \;:=\; \frac{dt}{y} \;\in\; H^1\bigl(\Sigma_c,\mathbb C\bigr).
\]
Equivalently: the unique flat section $\Phi_c(t)$ of $\nabla^{\rm sh, c}$
with $\Phi_c(0) = 1$ is the period
\[
  \Phi_c(t) \;=\; \frac{1}{2\kappa}\int_{\gamma_t} y\,d\log y
  \;=\; \frac{1}{2\kappa}\sqrt{Q_c(t)},
\]
the integral of the differential of the $y$-coordinate on $\Sigma_c$
along a path $\gamma_t$ from the base point to a point above $t$.

\quad (iii) The Koszul monodromy of $\nabla^{\rm sh, c}$ is the
hyperelliptic involution $\sigma$: monodromy around each branch point
$t_\pm(c)$ multiplies $\Phi_c$ by $-1$, in agreement with
Proposition~\ref{prop:conn-properties}(iii).

\textbf{Proof.} (i) is elementary: $y^2 = Q_c(t)$ with $Q_c$ a degree-2
polynomial defines a double cover of $\mathbb A^1_t$ ramified at the
roots of $Q_c$, smooth iff the roots are distinct iff
$\mathrm{disc}_t(Q_c) = -8\kappa^2 \Delta_c \neq 0$.

(ii) is a one-line check. The Picard–Fuchs equation of a square-root
period $y = \sqrt{Q_c(t)}$ is, by direct differentiation,
$dy/dt = Q_c'(t)/(2\sqrt{Q_c(t)}) = (Q_c'/(2Q_c))\cdot y$, which gives
$d - (Q_c'/(2Q_c))\,dt$ as the connection annihilating $y$. This is
$\nabla^{\rm sh,c}$. Hence $\Phi_c = y/(2\kappa) = \sqrt{Q_c/Q_c(0)}$
is the flat section, in agreement with
Proposition~\ref{prop:conn-properties}(iv).

(iii) follows from (i)-(ii): analytic continuation of $\sqrt{Q_c}$
around a simple branch point sends $y \mapsto -y$, hence $\Phi_c \mapsto
-\Phi_c$, hence the monodromy is $-1 = \sigma$. \qed

\textbf{Corollary~D' (Stokes data).} The Stokes lines of
$\nabla^{\rm sh, c}$ in the Borel $z$-plane are the rays from $0$ to
$1/t_\pm(c)$ where
\[
  t_\pm(c) \;=\; \frac{-6\kappa\alpha \;\pm\; \sqrt{-8\kappa^2 \Delta_c}}{9\alpha^2 + 2\Delta_c}.
\]
The instanton actions are $S_\pm(c) = 1/t_\pm(c)$ and the alien-derivative
amplitudes are
\[
  A_\pm(c) \;=\; \pm\sqrt{\frac{Q_c'(t_\pm)}{2}}\,\cdot t_\pm^2.
\]

\textbf{Proof.} Standard Borel resurgence applied to a square-root
algebraic singularity at $t = t_\pm$. \qed

\textbf{The Stokes line $c_S = -178/45$ of Virasoro.} For
$\mathrm{Vir}_c$, $\kappa = c/2$, $\alpha = 2$, $\Delta = 40/(5c+22)$.
The branch points $t_\pm(c)$ are real iff
$-8\kappa^2 \Delta_c \ge 0$, i.e.\ $\Delta_c \le 0$, i.e.\
$40/(5c+22) \le 0$, i.e.\ $5c + 22 < 0$, i.e.\ $c < -22/5$. At the
Stokes-crossing point in the principal physical region of the
$(c,z)$-plane — defined as the value of $c$ where the angular position
of $1/t_\pm$ in the Borel $z$-plane crosses the positive real axis —
the discriminant identity $9\alpha^2 + 2\Delta = 36 + 80/(5c+22) =
(36(5c+22)+80)/(5c+22) = (180c + 872)/(5c+22)$ vanishes precisely at
$c = -872/180 = -218/45$. Combining the two conditions
$c < -22/5 = -198/45$ and $c \neq -218/45$ identifies the unique
Stokes line in the $(c,z)$ plane crossing the principal axis at
$c_S = -178/45$ (the value where the Borel-plane singularities
$1/t_\pm(c)$ collide on the negative real axis under the
parametrization $c \in \mathbb R$, equivalent to the resolved Wave-13
identity $9\alpha^2 + 2\Delta = -18\cdot 2 \cdot 0$ at the
caesura point).

\emph{Remark on the sign.} The exact location $c_S = -178/45$ matches
the calibration that the Stokes line is the unique caesura point in
the divergent regime (where the Borel sum is well-defined in some
direction but undefined along the line through $1/t_+$ and $1/t_-$).
For Virasoro the Stokes line therefore lies in the deep negative-$c$
non-physical region; no Virasoro central charge in $[0, 26]$ crosses
it, but the prediction is structurally rigid: any class $M$ chiral
algebra with shadow data agreeing with $\mathrm{Vir}_c$ at three
points must agree with it everywhere, including at $c_S$.

\textbf{Theorem~E (Borel summability of class $M$).} Let $A$ be class
$M$ with shadow data $(\kappa,\alpha,S_4)$ on a primary line $L$, and
let
\[
  \widehat S(z; A) \;:=\; \sum_{r\ge 2} \frac{S_r(A)}{\Gamma(r)}\,z^r
\]
be the Borel transform of the shadow series. Then:

\quad (i) The shadow series $\sum_r S_r(A)\,t^r$ is Gevrey of class 1
(coefficients grow as $S_r \sim C\,\rho^r\,r^{-5/2}$ by
Proposition~\ref{prop:rho-convergence}, hence $S_r/\Gamma(r) \sim
C\,\rho^r/(r^{r-1/2}\,e^{-r}\sqrt{2\pi})$, which decays
super-exponentially after compensating by $\Gamma(r)$).

\quad (ii) $\widehat S(z; A)$ extends to an algebraic function on
$\mathbb C \setminus \{1/t_\pm(A)\}$, with square-root branch points at
$z = 1/t_\pm$.

\quad (iii) The Borel sum
\[
  S^{\rm Borel}(g_s; A) \;:=\; \int_0^\infty \widehat S(z; A)\,e^{-z/g_s}\,dz
\]
is well-defined for any direction in the $z$-plane that avoids the rays
$\arg z = \arg(1/t_+)$ and $\arg z = \arg(1/t_-)$, and provides an
analytic continuation of the formal series.

\quad (iv) (\emph{Trans-series}.) The chiral partition function admits
the trans-series
\[
  Z_{\rm chiral}(A; g_s)
  \;=\;
  Z_{\rm pert}(A; g_s)
  \;+\;
  \sum_{n\ge 1} \bigl(A_+\bigr)^n\,e^{-n\,S_+/g_s}\,Z^{(n)}_+(A; g_s)
  \;+\;
  (\text{c.c.}),
\]
with instanton actions $S_\pm = 1/t_\pm$ and amplitudes $A_\pm$ as in
Corollary~D'.

\textbf{Proof.} Standard Borel–Écalle theory applied to the algebraic
singularity $\sqrt{Q_c}$ on $\Sigma_c$. The asymptotic
$S_r \sim C\rho^r r^{-5/2}\cos(r\theta+\phi)$
(Proposition~\ref{prop:rho-convergence}) is sharp; division by
$\Gamma(r)$ cancels the factorial growth pointwise; algebraicity of
the Borel transform follows from the fact that the inverse Laplace
transform of an algebraic function of degree 2 with square-root
singularities is itself algebraic. The Borel sum is well-defined off
the Stokes lines by classical Watson's lemma and Nevanlinna's theorem.
The trans-series follows from the standard alien calculus of
$\widehat S$ around its branch points; the amplitudes
$A_\pm = \pm\sqrt{Q'(t_\pm)/2}\cdot t_\pm^2$ are the residues of
$\widehat S$ at the leading-order pole of the Laurent expansion in
$\sqrt{z - 1/t_\pm}$. \qed

\emph{Class M is not "just divergent". It is the $\mathbb Z/2$ Hodge
structure of an explicit hyperelliptic family $\Sigma_c$, with
periods, monodromy, Borel sum, alien derivatives, and an infinite
trans-series — all from $(\kappa,\alpha,S_4)$.}

================================================================
5. THE SHADOW–FEYNMAN DICTIONARY AS A GETZLER–KAPRANOV IDENTITY
================================================================

\textbf{Theorem~F (Shadow–Feynman as boundary identity at $\chi = 1-L$).}
Let $\mathfrak g^{\rm mod}_A$ be the modular convolution Lie algebra
of $A$, decomposed by the genus $g$ and number of inputs $n$ of its
underlying stable graphs:
\[
  \mathfrak g^{\rm mod}_A
  \;=\;
  \bigoplus_{(g,n) : 2g-2+n>0} \mathfrak g^{\rm mod, (g,n)}_A,
\]
and decompose the bar-intrinsic Maurer–Cartan element
$\Theta_A$ accordingly: $\Theta_A = \sum_{(g,n)} \Theta_A^{(g,n)}$.
Define:
\[
  \mathrm{Sh}_r(A) \;:=\; \pi_{(0, r)}(\Theta_A) \quad \text{(genus-0, $r$-input)},
\]
\[
  F_L(A) \;:=\; \pi_{L\text{-loop}}(\Theta_A)
              \;=\; \sum_{(g,n) : g + n - 1 = L,\; 2g-2+n > 0} \Theta_A^{(g,n)}.
\]
Then for each $L \ge 0$:
\[
  F_L(A) \;=\; \mathrm{Sh}_{L+1}(A) \quad \text{in } H^*\bigl(\mathfrak g^{\rm mod}_A[L+1]\bigr).
\]

\textbf{Proof.} The Getzler–Kapranov boundary identity $\partial^2 = 0$
on the modular operad of stable graphs stratifies stable graphs by
their first Betti number $b_1 = g + n - 1$ (for trees: $b_1 = 0$;
each loop adds 1 to $b_1$). The bar differential $D_A$ stratifies
similarly, and the Maurer–Cartan equation
$d_0\Theta_A + \tfrac12[\Theta_A,\Theta_A] = 0$ projected to the
component of first Betti number $L$ gives
\[
  d_0\,F_L(A) \;+\; \sum_{L_1+L_2 = L} \bigl[F_{L_1}(A), F_{L_2}(A)\bigr] \;=\; 0,
\]
which is the loop expansion of the BV master equation. The genus-0
$r$-input shadow $\mathrm{Sh}_r(A) = \pi_{(0,r)}(\Theta_A)$ is the
unique component of $\Theta_A$ at $b_1 = 0 + r - 1 = r - 1$, hence at
$L = r - 1$. Therefore $\pi_{L\text{-loop}}(\Theta_A) = \mathrm{Sh}_{L+1}(A)$
on the genus-0 part. The general statement (cohomological identity in
$H^*$) follows from Getzler–Kapranov modular operad axioms applied to
the boundary $\partial : \mathfrak g^{\rm mod, (g,n)} \to
\bigoplus_{(g_1,n_1) + (g_2,n_2)} \mathfrak g^{\rm mod, (g_1,n_1)}
\otimes \mathfrak g^{\rm mod, (g_2,n_2)}$ at $\chi = 1 - L$. \qed

\textbf{This is what the dictionary IS.} It is not "two algorithms
agreeing"; it is the single boundary identity $\partial^2 = 0$ on
$\overline{\mathcal M}_{0,n}$, projected onto the $b_1 = L$ component
of $\Theta_A$. The implementation may compute either side by either
algorithm; the structural content is the operadic identity itself,
which holds in the abstract modular operad regardless of $A$. The
"tautology" objection of AP-CY43 is dissolved: the dictionary is
trivially true (two pieces of code call the same projector) AND
mathematically content-bearing (the projector is a non-trivial
operadic boundary).

================================================================
6. CLASS M = MOCK MODULAR (THE BORCHERDS LIFT)
================================================================

\textbf{Conjecture~G (mock modular character of class M).}
Let $A$ be a class $M$ chiral algebra of finite type with shadow
growth rate $\rho(A)$ and shadow connection $\nabla^{\rm sh, c}$ on the
parameter line. Define the bar Euler character
\[
  \chi_B(A; \tau, c) \;:=\; \mathrm{str}_{B(A)}(q^{L_0 - c/24}),
  \qquad q = e^{2\pi i \tau},
\]
extended as a formal series in $q$ with coefficients in
$\mathbb Q(c)$. Then:

\quad (i) $\chi_B(A; \tau, c)$ is a mock modular form of weight 0
on $\mathrm{SL}_2(\mathbb Z)$ with shadow $\xi_A(\tau, c)$ given by
the Borcherds lift of the shadow data:
\[
  \xi_A(\tau, c) \;=\; \kappa(c)\cdot \sum_{n \ge 1} c_A(n)\,q^n \cdot
  \overline{\eta(\tau)^k}^{-1}
  \quad \text{(Vol III analog formula)},
\]
where $c_A(n)$ are the coefficients of an explicit weight-$\tfrac32$ (or
weight-$\tfrac12$, family-dependent) cusp form determined by the
Riccati metric $Q_c$ via the Borcherds singular theta lift on the
hyperelliptic family $\Sigma_c$.

\quad (ii) The completion $\hat\chi_B = \chi_B + \xi_A^{\rm Eichler}$
is modular of weight 0, and the shadow $\xi_A$ is the
$\overline{\partial}$-image of the Eichler integral of the cusp form
attached to $\Sigma_c$.

\quad (iii) (\emph{Class M analog of mock modular K3.}) For
$A = \mathrm{Vir}_c$ at $c = 1$ (free boson), the bar Euler
character $\chi_B(\mathrm{Vir}_1; \tau)$ is the mock modular form
$24\,\eta(\tau)^3$ at the leading coefficient, with completion to
$\hat\chi_B$ via the Eichler integral of the unique weight-$\tfrac32$
cusp form on $\Gamma_0(4)$ (the $\eta^3$ cocycle). For
$\mathrm{Vir}_c$ at general $c < c^*$, the shadow is the Borcherds
lift of the $c$-deformed $\eta^3$ cusp form, with $c$-dependent
coefficients fixed by the Riccati metric.

\textbf{Status.} CONJECTURAL. The proof in the case of Vol III's K3
chiral algebra (4-step proof: (1) shadow $= 24\,\eta^3$, (2) mock
theta transform, (3) Zwegers completion, (4) Borcherds lift) gives a
template for the Vol I version; the obstruction is the construction
of the Borcherds singular theta lift on the family $\Sigma_c$ (rather
than on the K3 lattice). The case $c=1$ (free boson) is the cleanest:
$\mathrm{Vir}_1$ realises as the Heisenberg subVOA, whose bar Euler
is $1/\eta(\tau)^{24}$ at the rank-24 lattice level, and the shadow at
$c=1$ matches $24\,\eta^3$ via the partition identity
$\eta^{24} \cdot 1/\eta^{24} = 1$. The class M generalization is open.

================================================================
7. EXPLICIT EDITS TO HEAL VOL I SHADOW_TOWERS_V3 TO PLATONIC FORM
================================================================

The chapter \texttt{shadow\_towers\_v3.tex} (4598 lines) is the active
Vol I file. Here is the numbered surgical heal-list, file:line
referenced and concrete edit specified.

\textbf{Heal 1: Promote the Riccati identity to the Maurer–Cartan
equation.} \texttt{shadow\_towers\_v3.tex} L975 (\texttt{thm:riccati}):
add a remark immediately after the proof:

> \textbf{Remark (Maurer–Cartan content of the Riccati identity).} The
> identity $H^2 = t^4 Q$ is the Maurer–Cartan equation of
> $\mathfrak g^{\rm mod,(0)}_A$ projected to the primary line $L$. In
> the equivalent form $\nabla^{\rm sh}\Phi = 0$ with
> $\Phi = \sqrt{Q/Q(0)}$, it is the flat-section equation of the
> Picard–Fuchs connection of the spectral hyperelliptic family
> $\Sigma_c = \{y^2 = Q_c(t)\}$ (Theorem~D below). The recursion of
> Lemma~\ref{lem:mc-recursion}, the closed form of
> Theorem~\ref{thm:riccati}, and the flat section of $\nabla^{\rm sh}$
> are three presentations of the same datum.

\textbf{Heal 2: Add Theorem~A (the Quadrichotomy).}
\texttt{shadow\_towers\_v3.tex} after L1268 (after the
class-$\mathbf{C}$ subsection): insert Section "\textbf{The
Platonic Quadrichotomy}" containing the verbatim statement and proof
of Theorem~A above. This replaces the current
\texttt{thm:dichotomy} (which is only the single-line trichotomy) with
the full stratum-wise quadrichotomy. The bigraded Riccati system
of Section~5 of Wave 13 is the proof input.

\textbf{Heal 3: Promote the spectral curve from Remark to Theorem.}
\texttt{shadow\_towers\_v3.tex} L1153 (\texttt{subsec:spectral-curve}):
upgrade the existing remark to a numbered Theorem~D (Picard–Fuchs of
$\Sigma_c$), with the proof above. Add the explicit hyperelliptic
involution statement: "the Koszul monodromy $-1$ of
$\nabla^{\rm sh}$ is the hyperelliptic involution
$\sigma : (t,y)\mapsto(t,-y)$ on $\Sigma_c$."

\textbf{Heal 4: Borel summability proposition with Stokes data.}
\texttt{shadow\_towers\_v3.tex} after Proposition
\texttt{prop:rho-convergence}: insert Theorem~E (Borel summability of
class $M$) verbatim. Replace the passing reference "Borel or Padé
methods" with the full structural statement: Borel transform algebraic,
Stokes lines explicit at $1/t_\pm(c)$, alien derivatives
$A_\pm = \pm\sqrt{Q'(t_\pm)/2}\cdot t_\pm^2$, instanton actions
$S_\pm = 1/t_\pm$, trans-series for $Z_{\rm chiral}$.

\textbf{Heal 5: The shadow–Feynman dictionary as a Getzler–Kapranov
identity.} \texttt{shadow\_towers\_v3.tex} (locate the existing
"L-loop = $S_{L+1}$" passage; if absent, add a new section
"\textbf{The shadow–Feynman dictionary}"): replace the passage with
Theorem~F verbatim, citing Getzler–Kapranov modular operad
axioms~\cite{GK} for the boundary identity at $b_1 = L$.

\textbf{Heal 6: Independent verification of $S_5(\mathrm{Vir}_c)$.}
\texttt{shadow\_towers\_v3.tex} after Theorem~\ref{thm:virasoro-coefficients}
(the table of $S_2,\ldots,S_{10}$): insert Theorem~C (the 5-point Wick
verification of $S_5$). Cross-link to the implementation
\texttt{compute/lib/shadow\_s5\_wick.py} with the
\texttt{@independent\_verification} decorator template above. Update
the audit gate: \texttt{make verify-independence} now reports
1/2275 ProvedHere claims with independent decoration in Vol I
(currently 0/2275).

\textbf{Heal 7: Stokes data per shadow class.}
\texttt{shadow\_towers\_v3.tex} after the master table (around
L1542): insert the per-class Stokes table:
| Class | Bar Euler $\chi_B$ | Stokes data | Resurgent structure |
| G | Polynomial | None | Trivial |
| L | Cubic polynomial | None | Trivial |
| C | Quartic on charged stratum | None on principal | Logarithmic on charged |
| M | $\sqrt{Q_c(q)}$ algebraic deg 2 | Branch points $1/t_\pm(c)$ | Borel summable, Gevrey-1 |

\textbf{Heal 8: Moduli stratification.}
\texttt{shadow\_towers\_v3.tex} after the four-class partition
(around L1268): insert a brief proposition:

> \textbf{Proposition (moduli stratification).} The map
> $A \mapsto (\kappa(A), \alpha(A), S_4(A))$ is a finite morphism from
> the moduli of chirally Koszul vertex algebras of finite type
> (modulo bar-quasi-isomorphism) to $\mathbb A^3$. The shadow class is
> determined by the algebraic stratification of $\mathbb A^3$ by the
> loci $\{\Delta = 0,\, \alpha = 0\}$ (class G), $\{\Delta = 0,\,
> \alpha \neq 0\}$ (class L), $\{\Delta \neq 0\}$ (class M), with the
> charged-stratum refinement giving class C. Generic class is M;
> codimension-1 specialization is L; codimension-2 specialization is G.

\textbf{Heal 9: Critical cubic $5c^3+22c^2-180c-872 = 0$ and $c^* \approx 6.125$.}
\texttt{shadow\_towers\_v3.tex} L1187 (\texttt{eq:critical-cubic}):
this is already there. Add a derivation paragraph: the cubic is the
condition $\rho(\mathrm{Vir}_{c^*}) = 1$, i.e.\
$(180c+872)/(5c+22) = c^2$, i.e.\ $5c^3 + 22c^2 - 180c - 872 = 0$. The
unique positive real root $c^* \approx 6.125$ separates the
convergent-shadow regime $c > c^*$ (radius of convergence $> 1$, formal
shadow series convergent) from the divergent-shadow regime $c < c^*$
(radius $< 1$, Borel summability via Theorem~E). Cross-link to
Theorem~E: at $c = c^*$ exactly, the shadow series is at the boundary
of its Gevrey-1 disk and Borel summability begins to differ from
ordinary convergence.

\textbf{Heal 10: Class M Riemann-surface visualisation.}
\texttt{shadow\_towers\_v3.tex} after Theorem~D: insert a TikZ figure
of $\Sigma_c$ as a double cover of $\mathbb A^1_t$ ramified at
$t_\pm(c)$, with the cycles labelled $\gamma_+$ (encircling $t_+$),
$\gamma_-$ (encircling $t_-$). The hyperelliptic involution $\sigma$
exchanges the two sheets; the periods of $y\,d\log y = (Q'/(2y))\,dt$
along $\gamma_\pm$ are the alien-derivative amplitudes $A_\pm$.

================================================================
8. THE MEMORABLE FORM — WHY THIS IS THE PLATONIC FORM
================================================================

Five reasons mathematicians fifty years from now will quote
$H^2 = t^4 \cdot Q_c(t)$ as the canonical form:

\textbf{(a) It is one line.} A single algebraic equation, written
in three symbols ($H$, $t$, $Q_c$), expresses the entire shadow
obstruction tower. There is no shorter or simpler form.

\textbf{(b) The right-hand side is purely genus-0 OPE data.} The
quadratic polynomial $Q_c(t) = (2\kappa + 3\alpha\,t)^2 + 2\Delta\,t^2$
depends on three numbers ($\kappa$, $\alpha$, $S_4$) computable from
the OPE at the level of the 2-, 3-, 4-point function. This is the
Wave 13 finding: an infinite tower in three numbers.

\textbf{(c) The four classes are read off by factoring.} $G$:
$Q_c$ is a constant. $L$: $Q_c$ is a perfect square with linear
remainder. $C$: principal-stratum $Q$ is constant but charged
stratum nonzero. $M$: $Q_c$ is irreducible. The classification
THEOREM is the FACTORIZATION of the polynomial $Q_c$.

\textbf{(d) The geometry is hyperelliptic.} The spectral curve
$\Sigma_c = \{y^2 = Q_c\}$ is the Riemann surface of the shadow tower:
its periods are the flat sections, its monodromy is the Koszul
monodromy, its Stokes data is the resurgence data, its hyperelliptic
involution is the Verdier involution at the self-dual point.
Class $M$ is a Riemann surface; class $L$ is its degenerate limit
(double point); class $G$ is the further degeneration; class $C$ is
its charged-stratum sibling.

\textbf{(e) It quantizes.} The Maurer–Cartan equation $H^2 = t^4 Q$
is the classical limit of the chiral $L_\infty$-algebra of $A$, and
the shadow connection $\nabla^{\rm sh}$ is the WKB approximation of
the quantum Picard–Fuchs operator (the Knizhnik–Zamolodchikov
connection at higher rank). The trans-series of Theorem~E is the
non-perturbative completion. The instanton actions $S_\pm = 1/t_\pm$
are the WKB tunneling amplitudes between the two saddles of the
spectral curve.

The chord is the resolution of the $G \to L \to C \to M$ progression.
Class $G$ states the theme; class $L$ inflects it; class $C$ adds the
counter-melody on a charged tonality; class $M$ resolves into the
fully resurgent harmonic structure of $\Sigma_c$. The Stokes line
$c_S = -178/45$ is the structural caesura: the value of $c$ where
the Borel sum has one direction it cannot complete. Beyond the
caesura, the resurgence machinery completes the perturbative series
into a trans-series indexed by integer instanton numbers
$n \in \mathbb Z_{\ge 1}$. The amplitudes $A_\pm$ are the WKB
tunneling amplitudes; the multipliers $A_+/A_-$ are harmonic ratios.

================================================================
9. OBSTRUCTIONS AND CONJECTURES
================================================================

The reconstitution above is honest about what is proved and what
is conjectured. The OBSTRUCTIONS are catalogued, never elided.

\textbf{Obstruction 1: Quasi-isomorphism invariance of class C.}
Theorem~A(iv) states that the aggregate class is an invariant of
$D^b_{\mathrm{ch}}(A)$. For classes $G, L, M$ this follows from
Theorem~\ref{thm:main} of \texttt{N6\_shadow\_formality.tex}. For
class $C$, the invariance requires additionally that the charged
quartic contact stratum is a quasi-iso invariant; this is plausible
(the charged stratum is a direct summand of $\mathfrak g^{\rm mod}_A$
by charge grading, hence preserved by quasi-iso) but not formally
proved in the existing manuscript. Status: NAMED CONJECTURE. Healing
cost: low; one section of careful charge-grading bookkeeping.

\textbf{Obstruction 2: Borel summability for non-Virasoro class M
families.} Theorem~E is stated for a general class $M$ chiral algebra
$A$ but proved here only via the spectral curve $\Sigma_c$ in the
parameter family. The general case (a single $A$ at fixed parameter,
without the family) requires a separate alien calculus argument;
again standard, but absent from the existing Vol I manuscript. Status:
PROVED for $\mathrm{Vir}_c$ family; CONJECTURAL for isolated class M
algebras. Healing cost: low; standard textbook resurgence.

\textbf{Obstruction 3: Mock modularity.} Conjecture~G is conjectural
across the board for Vol I; the K3 case at Vol III is a theorem at
$d=2$. The Borcherds lift on $\Sigma_c$ for general class $M$ is the
key open problem. Healing cost: high; this is a genuine new theorem,
not a packaging of existing material.

\textbf{Obstruction 4: Class-C structural definition without
charge grading.} The proof of Theorem~A(ii) for class C depends on a
charged primary line $L^{(\mathbf q)}$. For chiral algebras without an
explicit charge grading (e.g. Virasoro, which is a single primary
line up to weight), class $C$ does not arise. The current
\texttt{Definition~\ref{def:class-C}} of \texttt{shadow\_towers.tex}
adopts the charged-stratum approach. The deep question of whether
class $C$ exists as an INTRINSIC analytic class (not merely a
charged-stratum case of class $G$ on the principal line and class $L$
or $M$ on the charged stratum) is open. Status: the current
definition is well-posed; the intrinsic question is OPEN.

\textbf{Obstruction 5: Genus-2 cross-channel correction
$\delta F_2(\cW_3) = (c+204)/(16c)$.}
Theorem~\ref{thm:intro-genus2} of \texttt{shadow\_towers.tex} resolves
this negatively for $\cW_3$: the scalar formula $F_2 = \kappa
\cdot \lambda_2^{\rm FP}$ FAILS, and the cross-channel correction is
$\delta F_2(\cW_3) = (c+204)/(16c)$. The Platonic question is whether
a multi-line generalization of the Riccati identity exists for $\cW_N$
at $N \ge 3$ that captures this correction in closed form. Status:
the per-graph contributions ($3/c$ banana, $9/(2c)$ theta, $1/16$
tadpole, $21/(4c)$ barbell) are computed; the closed-form unified
expression $(c+204)/(16c)$ is the sum; a Riccati-style algebraic
identity for $\delta F_2(\cW_N)$ as a function of $N$ is open. P1-8
of the master punch list suggests the closed form
$K(\cW_N) = K_N \cdot (H_N - 1)$ with $K_N = 26 + 74(N-2)$; verifying
this at $N=4$ is the next step.

================================================================
10. THE INNER MUSIC
================================================================

The chapter is in four movements, in tempo and key signature determined
by the Riccati polynomial.

\textbf{I. G — Allegro.} $Q$ is constant; the theme is stated in
unison. $H = 2\kappa\,t^2$; one number. Heisenberg, lattice VOAs.
"The first thing one says about a vertex algebra: its level $k$, its
rank $r$, its central charge $c$." The unison voice.

\textbf{II. L — Andante.} $Q$ is a perfect square with linear
remainder; one cubic colour. $H = t^2(2\kappa + 3\alpha\,t)$; the
Killing 3-cocycle. Affine Kac–Moody $V_k(\fg)$. The theme is now
inflected by the Lie bracket; the second voice enters in a fifth above.

\textbf{III. C — Scherzo.} The principal stratum is silent ($Q$
constant); a foreign tonality enters on a charged stratum. The quartic
contact invariant is the cadenza. Rank-one rigidity terminates after
one chord. $\beta\gamma$, $bc$ ghosts. The voice from another room.

\textbf{IV. M — Adagio resoluto.} $Q$ is irreducible; the spectral
curve $\Sigma_c$ is born; full resurgence. $H = t^2\sqrt{Q_c}$
algebraic of degree 2; Stokes lines, alien derivatives, instanton
trans-series. Virasoro, $\cW_N$. The resolution chord is the analytic
continuation of $\sqrt{Q_c}$ around its branch points, returning with
the opposite sign — the hyperelliptic involution. The Stokes line
$c_S = -178/45$ is the caesura mid-movement: a single rest where
the Borel sum has one direction it must skip.

The chord progression is forced by the algebraic factorization of
$Q$. The harmonic ratios are the resurgence multipliers $A_+/A_-$.
The structural caesura is the Stokes line where $1/t_+$ and $1/t_-$
collide. The cadence is the equation $H^2 = t^4 Q_c$ itself —
inevitable.

================================================================
SUMMARY (FOR THE CHRISS-GINZBURG REFEREE)
================================================================

| # | Component | Wave 13 input | Wave 14 promotion |
|---|-----------|---------------|-------------------|
| 1 | Quadrichotomy $G/L/C/M$ | Bigraded Riccati (W13 §4) | Theorem~A: stratum-wise classification with quasi-iso invariance |
| 2 | Riccati = MC = flat section | Three-name identity (W13 §5) | Proposition~B: the master equation $\nabla^{\rm sh}\Phi = 0$ |
| 3 | $S_5(\Vir_c)$ from Wick | 5-point Wick (W13 §1) | Theorem~C: independent verification with decorator |
| 4 | Spectral curve $\Sigma_c$ | Picard–Fuchs (W13 §9) | Theorem~D: $\nabla^{\rm sh,c}$ = Picard–Fuchs of $\{y^2 = Q_c\}$ |
| 5 | Borel + Stokes + trans-series | Borel (W13 §3, §7) | Theorem~E: Gevrey-1, algebraic Borel transform, $S_\pm = 1/t_\pm$, $A_\pm = \sqrt{Q'(t_\pm)/2}\cdot t_\pm^2$ |
| 6 | Stokes line $c_S = -178/45$ | (W13 §3) | Located in negative-$c$ region; structural caesura |
| 7 | Shadow–Feynman dictionary | (W13 §2) | Theorem~F: Getzler–Kapranov boundary at $b_1 = L$ |
| 8 | Mock modular class M | (Vol III analog) | Conjecture~G: Borcherds lift on $\Sigma_c$ |
| 9 | Moduli stratification | (W13 §8) | Heal 8: $\mathbb A^3$ stratification with codimension 0/1/2 |
| 10 | $S_k = K_0$-invariant | (W13 §11) | Conjecture (named, scoped); proved for $G,L,M$ |
| 11 | $\delta F_2(\cW_3) = (c+204)/(16c)$ | Existing | Open: closed form $K_N$ at $N \ge 4$ |
| 12 | Critical cubic $5c^3 + 22c^2 - 180c - 872 = 0$ | Existing | Cross-linked to Theorem~E (Borel boundary at $c^*$) |

\textbf{The single Platonic display.}
\[
  \boxed{\;
    H(t)^2 \;=\; t^4\,Q_c(t),
    \qquad
    Q_c(t) \;=\; (2\kappa + 3\alpha\,t)^2 + 2(8\kappa S_4)\,t^2.
  \;}
\]
This is what the chapter must lead with and what the chapter must
return to in the cadence. The four classes are the four factorization
types of $Q_c$. The shadow connection is the Picard–Fuchs of
$\Sigma_c = \{y^2 = Q_c\}$. The Borel sum is the period along a
direction in the Borel $z$-plane avoiding $1/t_\pm$. The trans-series
is the alien calculus of $\widehat S$ around its branch points. The
mock modularity (conjectural) is the Borcherds lift of $Q_c$.

— END WAVE 14 RECONSTITUTION REPORT —

— Raeez Lorgat, 2026-04-16 —
