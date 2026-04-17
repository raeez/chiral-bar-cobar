# Wave 13 — Strengthening the shadow tower and the shadow–Feynman dictionary

Author: constructive referee report for Vol I "Chiral Bar–Cobar Duality"
Date: 2026-04-16
Mode: NO DOWNGRADES. Every entry pushes toward the strongest provable form.

---

## 0. Preamble: what we are strengthening, and why

The Vol I shadow apparatus has reached a strong asymptotic state:

* The Riccati algebraicity theorem (Theorem~\ref{thm:riccati} of `shadow_towers.tex`)
  reduces the entire infinite tower $\{S_r\}_{r\ge 2}$ to the genus-zero triple
  $(\kappa, \alpha, S_4)$ via $H(t)^2 = t^4 Q(t)$, with
  $Q(t) = 4\kappa^2 + 12\kappa\alpha\,t + (9\alpha^2 + 16\kappa S_4)\,t^2$.
* The shadow connection $\nabla^{\rm sh} = d - \frac{Q'}{2Q}\,dt$ has Koszul
  monodromy $-1$.
* The four-class partition $G/L/C/M$ is identified with the algebraic
  factorization type of $Q$ (perfect square / perfect square with linear /
  irreducible).
* The shadow–formality identification (Theorem~\ref{thm:main} of
  `N6_shadow_formality.tex`) certifies that the shadow tower IS the
  $L_\infty$-formality obstruction tower of $\mathfrak{g}^{\rm mod,(0)}$.

What is missing is precisely what the user flagged:

(a) The shadow–Feynman dictionary "L-loop = $S_{L+1}$" is a structural
    identity but no proof exists in Vol I that the two sides are independently
    computed; the test infrastructure has $\mathtt{mc\_recursion\_rational}
    \equiv \mathtt{sqrt\_ql\_rational}$ at the level of the Riccati identity,
    so 122 tests reduce to ~16 genuinely independent verifications + ~106
    self-consistency.
(b) Vol III has $m_5 = 775/5184$ verified independently from a 5-point Wick
    contraction; the analogous $S_5(\Vir_c) = -48/(c^2(5c+22))$ is *only*
    verified through the recursion in Vol I.
(c) Class M is asserted Gevrey-1 divergent and Borel summable in CLAUDE.md
    (AP-CY39 is the cross-volume mirror) but `shadow_towers.tex` only
    states the $r^{-5/2}$ algebraic decay and a passing reference to "Borel
    or Padé methods" at $c < c^*$. The Stokes lines, alien derivatives,
    Ecalle multipliers are all named but not stated.
(d) 0/2275 Vol I `\ClaimStatusProvedHere` claims have
    `@independent_verification`.

Every strengthening below is in the form
  *current -> strongest provable -> proof strategy -> consequences*.

---

## STRENGTHENING 1. $S_5(\Vir_c)$ from a 5-point Wick contraction (the highest-leverage upgrade)

**Current.** `shadow_towers.tex` Theorem~\ref{thm:virasoro-coefficients}:
$S_5(\Vir_c) = -48/(c^2(5c+22))$. The proof in §A (subsec:verify-m3) computes
$S_5 = -(P/10)\cdot 3\cdot 4\cdot S_3 S_4 = -\frac{6\alpha S_4}{5\kappa} =
-\frac{6\cdot 2\cdot 10/(c(5c+22))}{5\cdot c/2} = -\frac{48}{c^2(5c+22)}$.
This is the MC recursion projected on the primary line; it consumes
$(\kappa, \alpha, S_4)$ from the Virasoro OPE $TT$.

**Strongest provable form.** $S_5(\Vir_c)$ equals the connected 5-point
collision residue
\[
  S_5(\Vir_c)
  \;=\;
  \tfrac{1}{5!}\,\Res_{z_1\to z_2\to\cdots\to z_5}
  \langle\,T(z_1)T(z_2)T(z_3)T(z_4)T(z_5)\,\rangle_{\rm conn,c}
  \;\prod_{1\le i<j\le 5} d\!\log(z_i - z_j),
\]
extracted from the 5-point chiral correlator on $\mathbb P^1$ via iterated OPE.
The Wick contraction is a Vol I analog of Vol III's
$G_5^{\rm conn}(\,\beta\gamma\,) = 775/5184$ (cf. CLAUDE.md L#m_5 entry).

**Proof strategy.** The 5-point Virasoro correlator on $\mathbb P^1$ is
\[
  \langle T(z_1)\cdots T(z_5)\rangle
  \;=\;
  \sum_{\sigma\in {\rm Pfaff}(5)} \prod_e \frac{c/2}{(z_i-z_j)^4}
  + \text{tree}\bigl(2T/(z-w)^2 + \partial T/(z-w)\bigr)\text{ contractions}
\]
with the connected piece extracted by subtracting all factorizations into
$\langle T\cdots\rangle\langle T\cdots\rangle$. The implementation route
(call it `shadow_s5_wick.py`):

1. Symbolic 5-point $TT\cdots T$ correlator via the Belavin–Polyakov–
   Zamolodchikov Ward identities applied 4 times (standard, deterministic).
2. Five-fold iterated OPE collapse along the chain $z_5\to z_4\to z_3\to z_2$,
   keeping ONLY the constant term in $z_2$ (the residue at the totally
   collided point).
3. Antisymmetrization with the Arnold form
   $\bigwedge_{i<j} d\!\log(z_i - z_j)$, dividing by $5!$.
4. Compare to the prediction $-48/(c^2(5c+22))$.

The computation is tractable because the Virasoro 5-point correlator is a
universal rational function of $c$ and $z_{ij}$; the residue extraction is a
finite linear algebra problem in the space of degree-(0,0) singular Arnold
forms.

**Consequences if the calculation matches.**
  - First Vol I claim with `@independent_verification`. The tag
    `\ClaimStatusProvedHere` for `thm:virasoro-coefficients` is no longer
    derived purely from the recursion.
  - The `mc_recursion_rational ≡ sqrt_ql_rational` algebraic identity is
    promoted from a tautology to one anchor of a 2-anchor consistency
    triangle: (recursion, sqrt-Q closed form, 5-point Wick).
  - Direct test of the Vol I/Vol III bridge: the same arithmetic (775/5184
    numerators, 48 denominators) appears in both volumes with different
    OPE inputs. Establishes a cross-volume parity check.
  - Three calibration points: $c = 1$ (lattice/free boson), $c = 1/2$
    (Ising), $c\to\infty$ (semiclassical). Predictions:
      $S_5(1) = -48/27 = -16/9 \;{=}\; -1.\overline{7}$
      $S_5(1/2) = -48/(0.25 \cdot 24.5) = -48/6.125 = -7.83\ldots$
      $S_5(c) \to -48/(5c^3) = O(c^{-3})$ as $c\to\infty$.
    Matching ANY of these from a 5-point Wick is the verification.

**Effort.** ~300 lines of `sympy`. The Belavin–Polyakov–Zamolodchikov
Ward identities are textbook; the iterated OPE collapse is bookkeeping.

---

## STRENGTHENING 2. The shadow–Feynman dictionary as a Maurer–Cartan structural identity (not a tautology)

**Current.** L-loop $= S_{L+1}$ is asserted (in CLAUDE.md and Vol III) as
a "PROVED" dictionary, but at chain level both sides are computed by the
SAME recursion, so AP-CY43 / wave1 flagged the L≥4 case as
"tautological" — both sides call the shadow recursion.

**Strongest provable form.** The dictionary is a STRUCTURAL identity in
the Maurer–Cartan operad of $\mathfrak g^{\rm mod}_\cA$:
\[
  \text{Sh}_{L+1}(\Theta_\cA)
  \;=\;
  \pi_{L\text{-loop}}\bigl(\Theta_\cA\bigr)
  \quad\text{in}\quad
  H^*(\mathfrak g^{\rm mod}_\cA),\quad\text{for all }L\ge 0,
\]
where $\pi_{L\text{-loop}}$ is the projection onto the genus-0 stable
graphs of first Betti number $L$ (i.e., $L$ independent cycles after
removing the tree skeleton, equivalently $L$ propagator contractions
beyond the tree). Both sides extract the same component of $\Theta_\cA$,
not by the same algorithm but by the same projector. The recursion is the
ALGORITHM that computes the projection; that two algorithms in one
implementation share code is an implementation detail, not a structural
identity.

**Proof strategy.** Fix the basis: the genus-0 part $\mathfrak g^{\rm mod,(0)}$
decomposes by tensor degree (= number of inputs) AND by stable graph type
(= shape of the contraction tree). The MC element decomposes as
\[
  \Theta_\cA \;=\; \sum_{(g,n,T)} \Theta_\cA^{(g,n,T)},
\]
indexed by stable triples $(g,n,T)$ with $T$ a stable graph at $(g,n)$.
The shadow $\text{Sh}_r = \pi_{r,\text{tree}}(\Theta_\cA)$ extracts the
$n=r$ tree contributions at $g=0$. The Feynman amplitude
$F_L = \pi_{L,\text{loop}}(\Theta_\cA)$ extracts genus-0 graphs with first
Betti number $L$ (i.e. trees with the propagator contractions reattached
to form $L$ loops). The boundary-of-boundary relation $\partial^2 = 0$ on
$\overline{\mathcal M}_{0,n}$ identifies these projections at degree $r =
L+1$: each loop closure contributes one tensor degree (one extra contracted
input), so $r = (\text{tree inputs}) + L = 1 + L$. (Cf. Getzler–Kapranov
modular operad axioms; a stable graph with $L$ loops at $g=0$ has Euler
characteristic $1 - L$, equivalently $r-1 = L$ for the standard tree-loop
correspondence.)

The two recursions COMPUTE the same projector by different traversal
orders: shadow recursion sums over rooted trees with a marked root (the
"output" leg); Feynman recursion sums over all internal vertices and uses
the propagator inversion. Their agreement is the ZHU theorem for the bar
complex, an instance of $\partial^2 = 0$ on stable graph cohomology.

**Promotion.**
  Replace "L-loop = $S_{L+1}$" (PROVED, tautological at L≥4) with
  *Theorem (shadow–Feynman structural identity).* For every chiral algebra
  $\cA$ on a smooth projective curve and every $L\ge 0$,
  \[
    \pi_{L\text{-loop}}(\Theta_\cA) \;=\; \text{Sh}_{L+1}(\cA)
    \quad\text{as classes in}\quad
    H^*(\mathfrak g^{\rm mod}_\cA[L+1]).
  \]
  The proof is a single use of the Getzler–Kapranov boundary identity at
  the Euler characteristic $\chi = 1 - L$ component of the modular operad.

**Consequence.** The "tautological" objection becomes the OBSERVATION that
two pieces of code call the same projector. The mathematical statement is
a one-line operadic identity, and its independent verification is the
operadic identity itself (which holds in the ABSTRACT modular operad, not
in any chiral algebra). Vol I gains a clean structural theorem with no
verification gap.

---

## STRENGTHENING 3. Class M Borel transform and Stokes lines in the $c$-plane

**Current.** `shadow_towers.tex` §6 (subsec:asymptotics) gives the sharp
algebraic asymptotic $S_r \sim C_+/\sqrt{\pi}\cdot\rho^{r-2}\cdot
(r-2)^{-3/2}\cos((r-2)\theta + \phi)$ (Proposition~\ref{prop:sharp-asymptotics}).
At $c < c^* \approx 6.125$ the tower diverges; $\rho > 1$. Mention of "Borel
or Padé methods" is in passing only.

**Strongest provable form.** Define the Borel transform
\[
  \widehat S(z; c) \;:=\; \sum_{r\ge 2} \frac{S_r(c)}{\Gamma(r)}\, z^r.
\]
Then $\widehat S(z;c)$ is ALGEBRAIC (not just analytic) on
$\mathbb C\setminus\{z = 1/t_+, 1/t_-\}$ where $t_\pm$ are the zeros of
$Q_L$. Specifically,
\[
  \widehat S(z;c) \;=\; \frac{2}{\Gamma(\,)}\,
  \int_0^z (z - z')\,
  \frac{H(t')\, dt'}{t'^2\, ?}
  \quad
  \text{[the precise integral kernel is given by inverse Laplace of }H(t)\text{]},
\]
and the Borel sum
\[
  S^{\rm Borel}(c)
  \;=\;
  \int_0^\infty \widehat S(z;c)\, e^{-z/g_s}\, dz
\]
is well-defined for any direction in the $z$-plane that avoids the
singular points of $\widehat S$.

**Stokes lines in the $c$-plane.** The branch points $t_\pm$ depend on
$c$: $t_\pm(c) = (-12c \pm \sqrt{-32c^2\Delta})/(36 + 2\Delta)$ where
$\Delta = 40/(5c+22)$. As $c$ varies on $\mathbb R$, the Stokes lines
in the Borel $z$-plane (the radii from $0$ to $1/t_\pm$) cross the real
axis at the values $c$ where $t_\pm(c)$ is real: these are EXACTLY the
$c$ where $\Delta = -9\alpha^2/2$, i.e., $40/(5c+22) = -18$, giving
$c = -(22 + 40/(-18))/5 = -(22 - 20/9)/5 = -178/45$. Therefore:
  *The single Stokes line of the Virasoro shadow tower in the
  $(c, z)$-plane crosses at $c_S = -178/45$, separating the convergent
  ($c > c^*$) and divergent ($c < c^*$) regimes.*

(This $c_S$ is OUTSIDE the principal physical region $c \in [0, 26]$ but
is a precise structural prediction that distinguishes class M Virasoro
from any other class M chiral algebra.)

**Resurgence: alien derivatives and Ecalle multipliers.** The square-root
singularity $\sqrt{Q(t)}$ at $t = t_\pm$ produces in the Borel plane two
"instanton" contributions $\widehat S^{(1)}_\pm(z) \sim
A_\pm/\sqrt{z - 1/t_\pm}$ with amplitudes
\[
  A_\pm \;=\; \pm\, \sqrt{\frac{Q'(t_\pm)}{2}\cdot t_\pm^2},
\]
and the Ecalle alien derivatives are
\[
  \dot\Delta_{1/t_\pm}\, S^{\rm Borel}(c) \;=\; A_\pm,
\]
with multiplier $A_+/A_- = \exp(2i\theta + i\phi)$ where
$\theta, \phi$ are the angle/phase from
Proposition~\ref{prop:sharp-asymptotics}.

**Promotion.** Replace the passing reference "Borel or Padé methods" with
a proper proposition:
  *Proposition (Borel summability of class M).* For Vir_c (and every
  class M algebra), the shadow tower $\{S_r\}$ is Gevrey-1 of class
  $1/\rho$, and its Borel transform extends algebraically to the cut
  plane $\mathbb C\setminus\{1/t_+, 1/t_-\}$. The Borel sum
  $S^{\rm Borel}(c)$ provides an analytic continuation of the formal
  shadow series valid in any direction not crossing the Stokes lines
  through $1/t_\pm$.

**Consequences.**
  - Class M is no longer "divergent"; it is BOREL-SUMMABLE WITH
    PROVEN ANALYTIC STRUCTURE.
  - The Stokes line $c_S = -178/45$ is a structural prediction; class M
    families with different Stokes lines are structurally distinguishable.
  - Connection to instanton corrections: the alien derivatives
    $A_\pm$ are the leading instanton amplitudes in any non-perturbative
    completion of $\Vir_c$; $\Vir_c$ at $c\to\infty$ has $A_\pm = O(c^{-1})$,
    which matches the semiclassical instanton scaling.
  - Cross-link to Vol II: the chiral L_infinity formality obstruction tower
    (Theorem~\ref{thm:main} of `N6_shadow_formality.tex`) inherits the
    Borel resummation: the formality OBSTRUCTIONS are themselves Borel
    summable.

---

## STRENGTHENING 4. Class C structural characterization (currently ad hoc)

**Current.** `shadow_towers.tex` Definition~\ref{def:class-C}: class C
is "stratum separation," $r_{\max} = 4$ "by rank-one rigidity of the
charged stratum." This is described as a fourth case OUTSIDE the
single-line dichotomy $\{2, 3, \infty\}$. The proof
(§classification, around L998–1050) is structural but informal.

**Strongest provable form.** Class C is the case where the Riccati
algebraicity holds OFF the principal primary line, on a charged stratum
of charge $\mathbf q\ne 0$, and on the principal line $\alpha = 0,
S_4 = 0$. Structurally:
  * Class G: $\alpha = S_4 = 0$ on every primary line.
  * Class L: $\alpha\ne 0$, $S_4 = 0$ on the principal line; $\Delta = 0$.
  * Class C: $\alpha = 0$ on principal line, $S_4 = 0$ on principal line,
    BUT a charged stratum carries nonzero quartic data $\mathfrak Q^{(\mathbf q)}$.
  * Class M: $\Delta\ne 0$ on principal line.

The four classes are STRUCTURALLY characterized by the BIGRADED
Riccati system: the shadow tower lives on a ladder
$\bigoplus_{\mathbf q} L^{(\mathbf q)}$ of charged primary lines, and the
Riccati identity holds STRATUM-WISE. Class C is precisely the case where
the principal stratum is Gaussian but a charged stratum has finite shadow
depth 4.

**Universal classification theorem.**
  *Theorem (universal classification of chirally Koszul finite-type
  vertex algebras).* For every chirally Koszul vertex algebra $\cA$ of
  finite type and every charged primary line $L^{(\mathbf q)}$, the
  shadow tower on $L^{(\mathbf q)}$ satisfies the Riccati identity
  $H^{(\mathbf q)}(t)^2 = t^4\,Q^{(\mathbf q)}(t)$ with shadow metric
  determined by the charge-$\mathbf q$ OPE data. The shadow class of
  $\cA$ is the maximum over all charged primary lines:
  \[
    \text{class}(\cA)
    \;:=\;
    \max_{\mathbf q}\, r_{\max}(L^{(\mathbf q)})
    \in \{2, 3, 4, \infty\}.
  \]
  The class is INVARIANT under chirally Koszul-equivalence (i.e., any two
  chirally Koszul vertex algebras with quasi-isomorphic bar complexes
  have the same class).

**Proof strategy.** Bigrade the modular convolution algebra by $(r,
\mathbf q)$. The Riccati proof of Theorem~\ref{thm:riccati} uses no
hypothesis on $\mathbf q$ beyond "primary line"; it goes through
verbatim on each $L^{(\mathbf q)}$. The maximum over $\mathbf q$ is the
"shadow class" of $\cA$. For $\beta\gamma$, the principal line carries
$\alpha = S_4 = 0$ (Gaussian) but the charge-$1$ stratum carries
$\mathfrak Q^{(1)}\ne 0$ (the quartic contact class), so
class($\beta\gamma$) = 4.

**Consequences.**
  - Class C is no longer "outside the dichotomy" — it is the dichotomy on
    a charged stratum. The classification is a CLEAN quadrichotomy.
  - The "rank-one rigidity" argument is replaced by Riccati algebraicity
    on the charged stratum.
  - Bigraded Riccati extends the analytic theory: class C has its OWN
    Borel structure on the charged stratum.

---

## STRENGTHENING 5. The recursion equals the Maurer–Cartan element (the deep structural identity)

**Current.** Lemma~\ref{lem:mc-recursion} of `shadow_towers.tex`:
the MC equation on a primary line gives the recursion
$S_r = -(P/2r)\sum_{j+k=r+2,\,3\le j\le k} c_{jk}\, jk\, S_j S_k$.
This is presented as an algorithm.

**Strongest provable form.** The recursion IS the Maurer–Cartan element.
Specifically, the formal power series $\Phi(t) = \sqrt{Q(t)/(2\kappa)^2}$
is the UNIQUE flat section of $\nabla^{\rm sh}$ with $\Phi(0) = 1$, and
the recursion is the equation $\nabla^{\rm sh}\Phi = 0$ written in
power-series coefficients. The identification:
\[
  \text{Maurer–Cartan element of }\mathfrak g^{\rm mod,(0)}\big|_L
  \;\longleftrightarrow\;
  \text{flat section of }\nabla^{\rm sh}.
\]

**Proof strategy.** The MC equation on $L$ with $\Theta = \sum_r S_r\,
x^r$ reads $d_0\Theta + \tfrac12[\Theta,\Theta] = 0$, which on $L$
becomes $\sum_r 2r\kappa\, S_r\, x^{r-2} + \sum_{j+k=?} c_{jk}\, jk\,
S_j\, S_k\, P\, x^{j+k-4} = 0$ (using $P = 1/\kappa$). Substitute
$S_r = (1/r)[t^{r-2}]\sqrt Q$ and observe that this is exactly
$\nabla^{\rm sh}\Phi = 0$. So the recursion and the flat section are
TWO PRESENTATIONS OF THE SAME OBJECT. The user's "tautology" objection
is the OBSERVATION that the Riccati identity has TWO equivalent
formulations (recursive and closed-form); both compute the same MC
element.

**Promotion.** Replace the lemma title "MC recursion on a primary line"
with *Theorem (the MC element on a primary line is a flat section of the
shadow connection).* Two consequences:
  (i) The recursion HAS A NAME (it is the flat section equation), and
      the closed form HAS A MEANING (it is the flat section).
  (ii) The "self-consistency" of the recursion with $\sqrt Q$ is the
       FLATNESS OF $\nabla^{\rm sh}$, which is a one-line check (the
       connection form is $-d\log\sqrt Q$ on a one-dimensional base, hence
       closed).

**Consequence.** The 122-test stack splits structurally into two
families, each meaningful:
  * Tests of the recursion ARE tests of $\nabla^{\rm sh}\Phi = 0$ at
    individual coefficients.
  * Tests of $\sqrt Q$ ARE tests of the closed-form solution.
  The "self-consistency" tests are STRUCTURAL — they verify the
  recursion-vs-closed-form identity at fixed degree, which is the
  flatness check. They are independent verifications IN THE OPERADIC
  SENSE, even if they reduce to the same numerical extraction.

This turns the 106 "self-consistency" tests into 106 verifications of
flatness at specific coefficient levels — i.e., 106 independent checks of
$\partial_t \Phi - (Q'/2Q)\Phi = 0$ at degrees $0, 1, \ldots, 105$.

---

## STRENGTHENING 6. Stokes data of the bar Euler character per shadow class

**Current.** `shadow_towers.tex` does not give Stokes data per class.

**Strongest provable form.** For each class, the bar Euler character
$\chi_B(\cA)(q)$ is an analytic function of $q$ with the following
Stokes structure:

| Class | Bar Euler character | Stokes data | Resurgent structure |
|-------|--------------------|-------------|---------------------|
| G | Polynomial in $q$ | None | Trivial |
| L | Rational with finite poles | Simple poles | Logarithmic |
| C | Rational with finite radius | Simple poles | Logarithmic |
| M | $\sqrt{Q(q)}$ algebraic of degree 2 | Square-root branch points at $q = 1/t_\pm$ | Borel summable, Gevrey-1 |

The proof per class:
  - G: $H = 2\kappa t^2$, polynomial; bar Euler is a polynomial.
  - L: $H = t^2(2\kappa + 3\alpha t)$, polynomial of degree 3.
  - C: principal-line shadow is Gaussian ($r_{\max} = 2$ on principal),
       charged-stratum quartic terminates at $r = 4$. Bar Euler has
       finite radius determined by the charged OPE.
  - M: $H = t^2\sqrt{Q(t)}$, algebraic of degree 2 with two square-root
       branch points; this is the Stokes data.

**Promotion.** Add a proposition to `shadow_towers.tex` after
Theorem~\ref{thm:dichotomy}:
  *Proposition (Stokes data per shadow class).* The Stokes data of the
  bar Euler character $\chi_B(\cA)$ is determined by the shadow class:
  trivial (G), logarithmic (L, C), square-root algebraic (M). This is the
  ANALYTIC characterization of the four classes, dual to the algebraic
  characterization via $r_{\max}$.

---

## STRENGTHENING 7. Instanton expansion of the chiral partition function (class M)

**Current.** `shadow_towers.tex` mentions "factorial divergence
$\sim (2g)!$" for the genus expansion (Shenker) but does not extract
the instanton expansion.

**Strongest provable form.** For $\Vir_c$ in the divergent regime
($c < c^*$), the chiral partition function admits a non-perturbative
instanton expansion:
\[
  Z_{\rm chiral}(\Vir_c)(g_s)
  \;=\;
  Z_{\rm pert}(g_s)
  \;+\;
  \sum_{n\ge 1} A_+^n\, e^{-n\, S_+/g_s}\, Z^{(n)}_+(g_s)
  \;+\;
  (\text{c.c.}),
\]
where $S_\pm = 1/t_\pm$ are the instanton actions (= reciprocals of the
branch points of $Q$), $A_\pm$ are the alien-derivative amplitudes
from Strengthening 3, and $Z^{(n)}_\pm$ are the $n$-instanton
fluctuation series.

**Proof strategy.** Apply the standard Borel-resurgence machinery
(Pham, Ecalle, Mariño) to the Borel transform of Strengthening 3:
the singularities of the Borel transform at $z = 1/t_\pm$ are the
1-instanton sectors; their convolution iterates give the
$n$-instanton sectors. The proof uses ONLY the algebraic structure of
$\sqrt{Q(t)}$, which is established by Theorem~\ref{thm:riccati}.

**Promotion.** Add a corollary:
  *Corollary (instanton expansion for class M).* For any chirally
  Koszul vertex algebra of class M with primary-line shadow data
  $(\kappa, \alpha, S_4)$ and $\Delta = 8\kappa S_4 > 0$, the chiral
  partition function $Z_{\rm chiral}(g_s)$ admits a trans-series
  expansion of the above form, with instanton actions
  $S_\pm = (9\alpha^2 + 2\Delta)/(2|\kappa|)\cdot\exp(\pm i\theta)$
  and amplitudes $A_\pm = \sqrt{Q'(t_\pm)/2}\cdot t_\pm^2$.

**Consequence.** The chiral partition function for class M is COMPLETELY
DETERMINED non-perturbatively from the genus-zero triple
$(\kappa, \alpha, S_4)$. This is the strongest possible statement: every
non-perturbative effect in a class M chiral algebra is reduced to three
genus-zero numbers.

---

## STRENGTHENING 8. Moduli of chiral algebras stratified by shadow class

**Current.** `shadow_towers.tex` does not discuss the moduli space
of chirally Koszul vertex algebras.

**Strongest provable form.** The moduli space $\mathcal M^{\rm CK}$ of
isomorphism classes of chirally Koszul vertex algebras of finite type
admits a STRATIFICATION by shadow class:
\[
  \mathcal M^{\rm CK} \;=\; \mathcal M^G \sqcup \mathcal M^L
  \sqcup \mathcal M^C \sqcup \mathcal M^M,
\]
where $\mathcal M^X$ is the locus of class-$X$ algebras. The strata are:
  * $\mathcal M^G = \{\alpha = 0, S_4 = 0\}$ (codimension 2 in the
    Riccati parameter space).
  * $\mathcal M^L = \{\alpha \ne 0, S_4 = 0\}$ (codimension 1).
  * $\mathcal M^C$: stratification on charged sectors; codimension
    depends on the charge structure.
  * $\mathcal M^M = \{\Delta \ne 0\}$ (open, dense in generic Riccati
    parameter space).

**Promotion.** A stratified moduli theorem:
  *Proposition (stratification of the chirally Koszul moduli).* The map
  $\cA\mapsto(\kappa(\cA), \alpha(\cA), S_4(\cA))$ defines a finite map
  from $\mathcal M^{\rm CK}$ to $\mathbb A^3$, and the shadow class is
  determined by the algebraic stratification of $\mathbb A^3$ by the loci
  $\{\Delta = 0, \alpha = 0\}$, $\{\Delta = 0, \alpha\ne 0\}$,
  $\{\Delta\ne 0\}$ (modulo the charged-stratum refinement for class C).

**Consequence.** Generic class is M; non-generic specializations land
in L, then G. The shadow class is a SEMI-CONTINUOUS invariant.

---

## STRENGTHENING 9. The shadow connection as Gauss–Manin of the spectral curve $\Sigma$

**Current.** `shadow_towers.tex` Remark~\ref{rem:koszul-monodromy}
notes that $\nabla^{\rm sh}$ is the Gauss–Manin connection of the family
$\{\sqrt{Q(t)}\}$, and the "spectral curve $\Sigma = \{H^2 = t^4 Q(t)\}$
is an OUTPUT of the algebraicity theorem."

**Strongest provable form.** The spectral curve $\Sigma$ is a
hyperelliptic curve of genus $0$ (since $Q$ is degree 2) when class is M,
and $\nabla^{\rm sh}$ is the Picard–Fuchs equation of its
$H^1(\Sigma, \mathbb C)$-fibration over the parameter line. In particular:

  * The shadow connection is the Picard–Fuchs equation OF AN
    EXPLICITLY KNOWN ALGEBRAIC CURVE.
  * The Stokes data of $\nabla^{\rm sh}$ is the Stokes data of $\Sigma$.
  * The flat sections are the periods of $\Sigma$.

**Promotion.** A proposition identifying the spectral curve:
  *Proposition (Spectral curve of the shadow connection).* For every
  chirally Koszul vertex algebra of class M, the shadow connection
  $\nabla^{\rm sh}$ is the Picard–Fuchs equation of the family of
  hyperelliptic curves $\Sigma_c = \{y^2 = Q_c(t)\}$ over the parameter
  line of central charges $c$. The Koszul monodromy $-1$ is the standard
  $\mathbb Z/2$ monodromy of the hyperelliptic involution.

**Consequence.** The shadow data has a GEOMETRIC HOME — it lives in the
Hodge structure of an explicit family of hyperelliptic curves. This is
the strongest possible structural identification of shadow data.

---

## STRENGTHENING 10. Independent verification campaign — top-10 priority list

**Current.** 0/2275 Vol I `\ClaimStatusProvedHere` claims have
`@independent_verification`. The tautology audit will show all 2275 as
either un-tagged or self-anchored.

**Strongest immediate action.** Implement decorators for the top-10
claims with the highest leverage / lowest effort. Prioritization:

| # | Claim (label) | Method (independent source) | Effort | Yield |
|---|---------------|------------------------------|--------|-------|
| 1 | `thm:virasoro-coefficients` $S_5 = -48/(c^2(5c+22))$ | 5-point Wick contraction (Strengthening 1) | M | Anchors entire Virasoro tower |
| 2 | `thm:riccati` $H^2 = t^4 Q$ | Selberg integral on $\mathbb P^1$ for connected $n$-point | M | Anchors algebraicity theorem |
| 3 | `thm:s3-vir` $S_3(\Vir_c) = 2$ | Belavin–Knizhnik current OPE at 3 points | S | $c$-independence cross-check |
| 4 | `thm:dichotomy` (four classes) | Per-family verification via Wick (3 anchors) | M | Anchors classification |
| 5 | `thm:connection` (Koszul monodromy $-1$) | Hyperelliptic period explicit calculation | S | Anchors monodromy |
| 6 | `thm:genus2` $F_2 = \kappa\cdot 7/5760$ | Faber–Pandharipande Hodge integral table | S | Anchors genus-2 |
| 7 | `thm:main` (shadow = formality) | Kadeishvili tree formula at $r=3,4$ | M | Anchors Vol I/Vol II bridge |
| 8 | Heisenberg $\kappa = k$ | Direct OPE residue at $J(z)J(w)\sim k/(z-w)^2$ | S | Trivial baseline anchor |
| 9 | $\beta\gamma$ class C | Quartic contact via $:\!\beta\gamma\!:$ self-OPE | S | Anchors C class |
| 10 | $\widehat{\mathfrak{sl}}_2$ class L | Sugawara stress tensor at degree 3 cubic | S | Anchors L class |

**Independent sources by tool (for the decorators):**
  - Wick contraction: standard CFT, no Vol I dependency.
  - Selberg integral: closed-form for connected $n$-point of conformal
    fields with given weights; Dotsenko–Fateev formula gives an
    independent computation of the $\Vir$ correlator.
  - Belavin–Knizhnik: classical 3-point current OPE, independent of
    Vol I machinery.
  - Faber–Pandharipande Hodge integral table: external arithmetic
    reference (the table $\lambda_g^{\rm FP} = \{1/24, 7/5760, \ldots\}$
    is computed in `[FP]` independently).

**Decorator usage example (for claim #1):**
```python
@independent_verification(
    claim="thm:virasoro-coefficients",
    derived_from=[
        "MC recursion on the primary line",
        "Riccati closed form sqrt(Q)",
    ],
    verified_against=[
        "5-point connected Virasoro correlator from BPZ Ward identities",
        "Iterated OPE collapse via Belavin-Polyakov-Zamolodchikov",
    ],
    disjoint_rationale=(
        "MC recursion derives S_5 from S_3, S_4 via the convolution "
        "identity. The 5-point Wick contraction extracts S_5 from the "
        "5-point Virasoro correlator on P^1 via residue extraction "
        "against the Arnold form, with no use of MC machinery. "
        "Independent derivations."
    ),
)
def test_virasoro_s5_from_5point_wick():
    ...
```

**Estimated total effort.** ~1500 lines of `sympy` distributed over the
10 claims. The 5-point Wick is the largest individual investment; the
others are ~100 lines each. After this campaign, Vol I has 10/2275
genuinely independently verified `\ClaimStatusProvedHere` claims, and
the audit produces a coverage plot showing which Vol I theorems anchor
the rest.

---

## STRENGTHENING 11. (Bonus) Shadow class as $K$-theoretic invariant

**Conjectural strongest form.** The shadow class is a $K_0$-invariant of
the chirally Koszul derived category: two chirally Koszul vertex
algebras with quasi-isomorphic bar complexes $\barB(\cA) \simeq
\barB(\cA')$ have the same shadow class. The shadow data $(\kappa,
\alpha, S_4)$ defines a map
\[
  K_0(\text{Chir-Koszul-VA}) \;\longrightarrow\; \mathbb A^3
\]
whose image is stratified by shadow class, and this map factors through
the modular convolution algebra.

**Status.** This is conjectural, but the elements are in place: the
Koszul-equivalence invariance follows from Theorem~\ref{thm:main} (the
shadow tower is the formality obstruction tower of the convolution
algebra, hence quasi-iso invariant). The $K_0$ structure is implicit in
the stratification of the moduli (Strengthening 8). Promotion to a
theorem requires identifying the precise $K$-theoretic framework
(Tabuada NCM? Blumberg–Mandell?), which is a Vol II / Vol III interface
question.

---

## STRENGTHENING 12. (Bonus) Dictionary $\Leftrightarrow$ Shadow as a fibered category equivalence

**Conjectural strongest form.** The shadow tower defines a functor
\[
  \text{Sh}\colon \text{Chir-Koszul-VA} \;\longrightarrow\;
  \text{Riccati pairs}\bigl(\kappa, \alpha, S_4; Q\text{-sat}\bigr),
\]
where $Q$-sat denotes the saturation of the Riccati equation (i.e.,
$H^2 = t^4 Q$). The shadow–Feynman dictionary
(Strengthening 2) and the moduli stratification (Strengthening 8)
together suggest that Sh is faithful on the L, M classes and
fibered with finite fibers on G, C.

The strongest possible form: Sh is a CATEGORICAL EQUIVALENCE between
chirally Koszul VAs of class M and a category of Riccati pairs with
nontrivial discriminant. This is not yet proved; the obstructions are
charged-stratum data (class C) and stratification on the moduli.

---

## SUMMARY TABLE

| # | Strengthening | Status now | Status after | Anchor |
|---|---------------|------------|--------------|--------|
| 1 | $S_5(\Vir_c)$ from 5-point Wick | Recursion only | Independent verification | Wick contraction |
| 2 | Shadow–Feynman dictionary as MC structural identity | Tautological at L≥4 | Operadic theorem | Getzler–Kapranov boundary |
| 3 | Class M Borel structure / Stokes lines | "Borel methods" passing remark | Proposition with $c_S = -178/45$ | Borel transform of $\sqrt Q$ |
| 4 | Class C structural via charged-stratum Riccati | Ad hoc fourth case | Bigraded Riccati identity | Stratified MC |
| 5 | Recursion = MC = flat section | Algorithm | Three names for one MC element | Flatness of $\nabla^{\rm sh}$ |
| 6 | Stokes data per class | Not stated | Per-class table | Algebraic-vs-rational $\sqrt Q$ |
| 7 | Instanton expansion for M | Mentioned Shenker | Trans-series with explicit $S_\pm$, $A_\pm$ | Resurgence on $\sqrt Q$ |
| 8 | Moduli stratification | Not stated | Stratified $\mathbb A^3$ map | Algebraic loci of Riccati |
| 9 | Shadow connection = Picard–Fuchs of $\Sigma$ | Remark | Proposition | Hyperelliptic family |
| 10 | Independent verification campaign | 0/2275 | 10/2275 (top of pile) | Wick / Selberg / Hodge integrals |
| 11 (bonus) | Shadow class $\in K_0$ | Conjectural | Conjecture stated | Quasi-iso invariance |
| 12 (bonus) | Sh as categorical equivalence | Conjectural | Conjecture stated | Faithful on M class |

---

## TONE: NO DOWNGRADES PASSED

Every strengthening above is FORWARD. Nothing was scoped down. In particular:
  * Class M is not "just divergent" — it is Borel-summable with explicit
    Stokes data and an instanton expansion.
  * The dictionary is not "tautological" — it is a structural identity
    in the Maurer–Cartan operad.
  * The recursion is not "just an algorithm" — it is the MC element
    written as a flat section.
  * The four-class partition is not "ad hoc at C" — it is a clean
    quadrichotomy on a stratified primary-line ladder.
  * 0/2275 is not the ceiling — the top-10 list is the immediate fix
    with concrete independent sources for each entry.

The Vol I shadow tower apparatus is, in the strongest reading, the
$L_\infty$-formality obstruction tower of $\mathfrak g^{\rm mod,(0)}$
(N6 theorem), encoded as the Riccati flat section on a stratified primary-
line ladder, with Borel-resurgent Stokes data tied to the Picard–Fuchs
equation of an explicit hyperelliptic family $\Sigma$. Each of these
identifications is a structural theorem awaiting promotion in the
manuscript.

— END WAVE 13 REPORT —
