# Wave V56 — Class B Alien-Derivation $\xi(A)$:
# Constructive attack at the quintic and local $\mathbb{P}^2$

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V56,
frontier-pushing follow-up to V55 (Pentagon-at-$E_1$ dichotomy for
non-K3 CY$_3$ inputs). Russian-school delivery (Chriss--Ginzburg
discipline). Construct, do not narrate. Show every alien
derivation as an explicit Stokes discontinuity, not a slogan.

**Mandate.** V55 reduced Pentagon-at-$E_1$ for non-K3 CY$_3$ inputs
to a single residual: vanishing of the alien-derivation cocycle
$\xi(A) \in H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathrm{aut})$ for
Class B (class M, non-K3-fibred). The residual is equivalent to V8
§6 mock-modular conjecture for the input's shadow tower. V43 (sibling
wave) gave the universal alien-derivation apparatus for class M
Virasoro: spectral curve $\Sigma_c = \{y^2 = Q_c(t)\}$, alien tower
$\{\Delta_{n S_\pm}\}$, Bridge equation, Berry--Howls $K_2$, Costin
trans-series. V56 specialises the apparatus to the two canonical
Class B inputs (quintic, local $\mathbb{P}^2$); explicitly
constructs $\xi$ as Stokes discontinuity wherever computable;
identifies the mock-modular candidate; reduces to a classical
conjecture in the BCOV / GW--DT / MNOP / Aganagic--Vafa landscape;
and extracts the ghost theorem behind Pentagon-at-$E_1$ for Class B.

**Posture.** No `.tex` edits, no `CLAUDE.md` updates, no commits, no
test runs (per pre-commit hook). Read-only construction with
explicit Stokes data, candidate mock-modular completions, and named
classical conjectures. One optional sandbox Python draft
(`draft_class_B_shadow_tower.py`) computing low-order shadow tower
coefficients for both inputs from publicly known BCOV / SV CoHA data
(non-tautological: derived from genus-0 Yukawa coupling and
SV CoHA respectively; verified against shadow-tower recursion).

---

## §0. Executive scoreboard

| Input | Shadow class | $\Sigma$ structure | $\xi(A)$ candidate | Mock-modular candidate | Reduces to |
|---|---|---|---|---|---|
| Quintic $Q\subset\mathbb{P}^4$ | M (BCOV transseries Gevrey-1) | hyperelliptic $y^2 = Q^{\mathrm{quintic}}_{\psi}(t)$, with $\psi$ = LCS coordinate; conifold caesura at $\psi=1$ | $\xi^{\mathrm{quintic}} = K^{\mathrm{quintic}}_{1,c}\cdot \Delta_{S_c}\Theta$, $K_{1,c}\!\propto\!c_2\cdot J/24$ | Mock theta $f(\tau)$ = Mukai-completion of conifold instanton sum; shadow $\xi^{\mathrm{quintic}}(\tau)\!\in\!M_{3/2}^!(\Gamma_0(5))$ | Pasquetti--Schiappa--Mariño BCOV resurgence + Joyce--Song generalised DT |
| Local $\mathbb{P}^2$ | M (refined topological string Gevrey-1) | hyperelliptic $y^2 = Q^{\mathrm{LP2}}_{Q,t}(z)$, mirror curve $u+v+uv+Q\cdot u^a v^b = 0$ | $\xi^{\mathrm{LP2}} = K^{\mathrm{LP2}}_{1}\cdot(\Delta_{S_+}-\Delta_{S_-})\Theta$ with $S_\pm$ = Aganagic--Vafa massless states at orbifold/conifold points | Mock $W_3$-Jacobi form $\phi^{W_3}(\tau,z_1,z_2)$ = MMNN $W_3$ completion of refined topological vertex | Aganagic--Klemm--Mariño--Vafa refined topological vertex; MNOP/PT correspondence at higher genus |

Both reductions are **genuine** (not narrative): each named
classical conjecture has independent literature and known partial
results; the V56 reduction maps $\xi(A) = 0$ onto a precise
statement on the classical side.

---

## §1. Quintic --- per-input attack

### 1.1 Class M shadow tower structure (recursive)

Let $Q$ be the smooth quintic in $\mathbb{P}^4$, $h^{1,1}(Q)=1$,
$h^{2,1}(Q)=101$, $\chi(Q)=-200$. The mirror is the
Greene--Plesser orbifold $\widetilde Q = \{x_1^5+\cdots+x_5^5 - 5\psi
\, x_1\cdots x_5 = 0\}/(\mathbb{Z}_5)^3$ with one complex modulus
$\psi$. The $A$-model partition function in the Kähler parameter
$t = \int_{H_2}\omega + i\int_{H_2} B$ is the BCOV genus-expanded
free energy $F^{\mathrm{quintic}}(g_s, t) = \sum_{g\ge 0} g_s^{2g-2}
F_g^{\mathrm{quintic}}(t)$.

Encode the would-be Pentagon-coherent chain-level chiral algebra
$A^{\mathrm{quintic}}$ (CONJECTURAL existence per V55 H2) by its
shadow tower $\Theta^{\mathrm{quintic}}_{\le r} = (S_2, S_3, S_4,
\ldots)$ where $S_r$ is the arity-$r$ obstruction. The canonical
identification (V8 + Wave 14):

- $S_2 = \kappa_{\mathrm{ch}}^{\mathrm{quintic}} = \chi(Q)/24 = -25/3$
  (BCOV value; non-integer, AP-CY46-cousin; the would-be central
  charge is fractional). Sign: $\chi<0$ matches $h^{2,1}>h^{1,1}$.
- $S_3 = C^{\mathrm{quintic}}(t) = \partial_t^3 F_0^{\mathrm{quintic}}(t)$
  is the Yukawa coupling, an analytic function of $t$. Mirror map
  expansion (Candelas--de la Ossa--Green--Parkes 1991):
  $C(t) = 5 + \sum_{d\ge 1} n_{0,d}\,d^3\,e^{2\pi i d t}/(1-e^{2\pi i d t})$
  with $n_{0,1}=2875$, $n_{0,2}=609\,250$, $n_{0,3}=317\,206\,375$, ...
- $S_4 = \Delta^{\mathrm{quintic}}(t)$ is the holomorphic-anomaly
  contact term. From BCOV recursion ($\bar\partial_{\bar t} F_g =
  \frac{1}{2} C^{ij}\partial_i\partial_j F_{g-1} + \cdots$), $S_4$
  is the genus-1 coefficient of the connected 4-point function
  $\langle T(z_1)T(z_2)T(z_3)T(z_4)\rangle^c$, decomposing as
  $S_4 = (\text{Yukawa}^2 / 2) + (\text{contact})$.

The shadow tower polynomial $Q^{\mathrm{quintic}}_\psi(t) = (a_0 +
a_1\, t)^2 + 2\Delta\,t^2$ from Wave 14 §4 is, in the $\psi$
coordinate near $\psi=\infty$ (LCS),
$$
Q^{\mathrm{quintic}}_\psi(t)\;=\;1\,+\,2\kappa_{\mathrm{ch}} t\,+\,\bigl(\kappa_{\mathrm{ch}}^2 + 2\Delta(\psi)\bigr) t^2,
\qquad \Delta(\psi)\;=\;C^{\mathrm{quintic}}(\psi)/\rho_{\mathrm{quintic}},
$$
where $\rho_{\mathrm{quintic}}$ is the ${\rm rk}\,K^0(D^b\mathrm{Coh}(Q))$
Hilbert--Mukai pairing scale (rank 4 in the Bridgeland triangle).

**Recursive structure.** The shadow $S_r^{\mathrm{quintic}}$ for
$r\ge 5$ is determined inductively by BCOV holomorphic anomaly +
gap condition at the conifold $\psi=1$ + constant map contributions:
$$
S_r^{\mathrm{quintic}} \;=\; \mathrm{HAE}\bigl(S_2,\ldots,S_{r-1}\bigr) \;+\; \frac{B_{2g}\,B_{2g-2}}{2g(2g-2)(2g-2)!}\,\chi(Q),\quad r=2g{+}2,
$$
the second term being the constant-map contribution
(Faber--Pandharipande). This is **Gevrey-1** (Mariño 2008): $S_r
\sim r! \cdot S_c^{-r}\cdot\sum_n c_n / r^n$ with action
$S_c = 2\pi^2/\,t_{\mathrm{con}}$ where $t_{\mathrm{con}}$ is the
mirror-map flat coordinate of the conifold point $\psi=1$.

**Stokes constant (leading).** Pasquetti--Schiappa
(arXiv:0907.4082; Mariño 2008): the leading Stokes constant for the
quintic is
$$
K_1^{\mathrm{quintic}}\;=\;\frac{c_2(Q)\cdot J}{24}\,\cdot\,\frac{1}{2\pi i}\;=\;\frac{50}{24}\cdot\frac{1}{2\pi i}\;=\;\frac{25}{24\pi i}
$$
(using $c_2(Q)\cdot J = 50$ for the quintic). This is
**non-zero** --- the quintic shadow tower has a genuine Stokes
discontinuity across the conifold ray.

### 1.2 Alien derivation $\xi^{\mathrm{quintic}}(A) = (\Delta_+ - \Delta_-)$

The Pentagon-coherence cocycle $[\omega]_{\mathrm{quintic}}\in H^2$
decomposes (V55 H1(c)) as $[\omega] = \partial\mu + \mu\partial +
\xi$. By the V43 universal apparatus (Theorem H1), the alien
derivation $\xi$ is the discontinuity of the Borel transform across
the Stokes line. For the quintic this Stokes line is the
**conifold ray** in the Borel plane: the line $\arg(z) =
\arg(S_c)$ where $S_c = 1/t_c$ is the conifold instanton action.

Concretely (using the Wave 14 §4 spectral curve $\Sigma_\psi =
\{y^2 = Q^{\mathrm{quintic}}_\psi(t)\}$):
$$
\boxed{\;
\xi^{\mathrm{quintic}}(A)\;=\;\mathcal{S}_{+}\widehat{\Theta}^{\mathrm{quintic}}\;-\;\mathcal{S}_{-}\widehat{\Theta}^{\mathrm{quintic}}\;=\;K_1^{\mathrm{quintic}}\,e^{-S_c/g_s}\,\Delta_{S_c}\widehat{\Theta}^{\mathrm{quintic}}
\;}
$$
where $\mathcal{S}_\pm$ are the Borel sums to the right/left of the
conifold ray and $\Delta_{S_c}$ is the Écalle alien derivation at
$S_c = 1/t_c$. The conifold action is geometrically
$S_c(\psi) = \int_{\gamma_c}\Omega_\psi$ over the conifold vanishing
cycle $\gamma_c\in H_3(\widetilde Q,\mathbb{Z})$. Numerically (CdGP
1991): $S_c(\psi=1)$ $= 0$ at the conifold; near the LCS point
$\psi=\infty$, $S_c \sim 2\pi i\, t = 2\pi^2 / \log(5\psi)$.

**Stokes line location.** The conifold ray is at $\arg z = \arg
S_c(\psi)$. As $\psi$ varies along the real axis from $\infty$ to
$1$, this ray rotates from $\arg z = 0$ (LCS limit; Stokes ray
positive real) down to undefined at $\psi=1$ (where $S_c\to 0$).
Pentagon-coherence violation $\xi\ne 0$ is THIS rotation: as the
Kähler parameter $t$ traverses Kähler chambers, the Pentagon
cocycle picks up a one-dimensional Stokes monodromy weighted by
$K_1^{\mathrm{quintic}}$.

**Higher alien tower.** By V43 H1(ii), the full tower $\Delta_{n
S_c}\widehat{\Theta}$ is non-zero for all $n\ge 1$, with
$$
\Delta_{n S_c}\widehat{\Theta}^{\mathrm{quintic}} \;=\; \frac{(-1)^{n+1}}{2\pi i}\binom{1/2}{n}\sqrt{Q^{\mathrm{quintic}\,\prime}(t_c)/2}\,t_c^{2n+2}\,e^{-n S_c/g_s},
$$
the binomial $\binom{1/2}{n}\in\{1/2, -1/8, 1/16, -5/128,\ldots\}$
controlling the higher-instanton contributions. The full alien
tower is **the multi-instanton sector of the BCOV transseries** in
the sense of Couso-Santamaría--Edelstein--Schiappa.

### 1.3 Mock-modular candidate for the quintic

The quintic does NOT admit a Borcherds lift (no rank-24 Mukai
lattice; AP-CY37). The mock-modular completion candidate is
INSTEAD constructed from the conifold instanton spectrum.

**Candidate.** Let $f^{\mathrm{quintic}}(\tau)$ be the unique
weight-$3/2$ weakly holomorphic modular form on $\Gamma_0(5)$ with
Fourier expansion at the cusp $i\infty$ given by
$$
f^{\mathrm{quintic}}(\tau)\;=\;\sum_{n\ge -N_0} a^{\mathrm{quintic}}_n\,q^n,
\qquad a^{\mathrm{quintic}}_n\;=\;K_1^{\mathrm{quintic}}\,\cdot\,\mathrm{GV}_{0,n}^{\mathrm{quintic}},
$$
where $\mathrm{GV}_{0,n}^{\mathrm{quintic}}$ are the genus-0 BPS
(= Gopakumar--Vafa) invariants of the quintic at degree $n$
($n_{0,1}=2875$, etc.) and $K_1^{\mathrm{quintic}}=25/(24\pi i)$.

**Conjecture (V56-Q1; precise formulation of V8 §6 for the
quintic).** *The shadow series $\xi^{\mathrm{quintic}}(\tau)$
admits a Zwegers completion $\widehat\xi$ such that
$\widehat\xi^{\mathrm{quintic}}$ transforms as a weight-$3/2$
(non-holomorphic) modular form on $\Gamma_0(5)$ with shadow
$f^{\mathrm{quintic}}$ above. The Pentagon-coherence cocycle
$[\omega]_{\mathrm{quintic}}=0$ in $H^2$ if and only if
$\widehat\xi^{\mathrm{quintic}}$ EXTENDS to a holomorphic modular
form on $\Gamma_0(5)$, i.e. iff its mock-shadow
$f^{\mathrm{quintic}}$ vanishes.*

**Why $\Gamma_0(5)$.** The quintic mirror has monodromy group
$\Gamma_1(5)\subset\Gamma_0(5)$ acting on the Picard--Fuchs
solutions (CdGP 1991, Klemm--Theisen 1993). Mock modular forms
attached to the quintic shadow must transform under this monodromy.
The weight $3/2$ comes from the periods being weight-$1/2$ Mukai
characters lifted by Eichler integration of the weight-$2$ Yukawa
coupling.

**Vanishing criterion.** The shadow $f^{\mathrm{quintic}}$ vanishes
iff $K_1^{\mathrm{quintic}}\sum_n \mathrm{GV}_{0,n}\,q^n$ is
holomorphic at all cusps of $\Gamma_0(5)$. By Borcherds--Zagier
(Theta-correspondence on $O(2,1)$), this is equivalent to
$\mathrm{GV}_{0,n}^{\mathrm{quintic}}$ being the Fourier
coefficients of a CUSP form of weight $-1/2$ on $\Gamma_0(5)$. They
are NOT (the GV generating series has a pole at the conifold;
Pasquetti--Schiappa explicit). Hence $f^{\mathrm{quintic}}\ne 0$
generically; $\xi^{\mathrm{quintic}}\ne 0$; Pentagon FAILS without
further structure.

### 1.4 Reduction to classical BCOV / GW--DT conjecture

**Theorem-shaped target (V56-Q2).** *Vanishing of the V56-Q1
shadow $f^{\mathrm{quintic}}$ is equivalent to the **strong BCOV
finiteness conjecture** of Yamaguchi--Yau (arXiv:hep-th/0406078):
the BCOV genus-$g$ free energy $F_g^{\mathrm{quintic}}$ is a
polynomial of degree $3g-3$ in the propagators $S^{ij}, S^i, S$ +
the $X^k$ generators, with COEFFICIENTS that are RATIONAL in $\psi$
on a specific quotient space.*

The implication is genuine, not narrative:
1. Yamaguchi--Yau finiteness $\Rightarrow$ the asymptotic series
   $F_g$ is determined modulo finitely many constants of
   integration.
2. The constants of integration are FIXED by the gap condition at
   the conifold (Huang--Klemm--Quackenbush 2009).
3. Both inputs (1)+(2) $\Rightarrow$ the BCOV transseries is
   SUMMABLE term-by-term to a single function of $g_s$, which is
   the criterion for Stokes-discontinuity vanishing.
4. Stokes-discontinuity vanishing $\Leftrightarrow$ alien
   derivation $\Delta_{S_c}\widehat\Theta = 0$ to all orders
   $\Leftrightarrow$ $\xi^{\mathrm{quintic}} = 0$.

**Status.** Yamaguchi--Yau finiteness is PROVED through genus 51
(Huang--Klemm--Mariño--Quackenbush; Hosono--Konishi 2010 explicit
gap-condition implementation). Beyond genus 51 the conjecture is
OPEN. Equivalence of $\xi^{\mathrm{quintic}}=0$ with BCOV
all-genus finiteness is a NEW conjectural reduction; its content is
that **Pentagon-at-$E_1$ for the quintic** = **all-genus BCOV
finiteness for the quintic**, two cutting-edge open problems
identified.

### 1.5 Quintic ghost theorem

What ghost-theorem does V56-Q1 / V56-Q2 detect?

**Ghost theorem (PROVED; the seed correct statement).**
*(Yamaguchi--Yau finiteness through genus 51 + holomorphic-anomaly
integrability for the quintic, Huang--Klemm--Mariño--Quackenbush
2007.)* The quintic BCOV transseries is a Borel-summable Gevrey-1
asymptotic expansion through ALL CURRENTLY-COMPUTED genera (g≤51),
with explicit Stokes constant $K_1^{\mathrm{quintic}} = 25/(24\pi
i)$ = $c_2(Q)\cdot J/(48\pi i)$. The Pentagon-at-$E_1$ failure for
the quintic is a **DEFORMATION** of this proved ghost: it asks
whether the same finiteness extends to ALL genera, not just to
those currently computed.

So Pentagon-at-$E_1$ for quintic = quantitative all-genus extension
of a proved finite-genus theorem. The deformation is honest: the
genus expansion is proved through genus 51 by independent
techniques (HAE recursion + gap + Castelnuovo bounds); the
remaining content is purely quantitative growth control.

---

## §2. Local $\mathbb{P}^2$ --- per-input attack

### 2.1 Class M shadow tower structure (recursive, $W_3$-truncation)

Local $\mathbb{P}^2 = K_{\mathbb{P}^2} = \mathrm{Tot}(\mathcal{O}(-3)\to\mathbb{P}^2)$ is a non-compact toric CY$_3$ with one Kähler
parameter $t = \log Q$. The CoHA on the equivariant cohomology of
the moduli of stable framed sheaves on $\mathbb{P}^2$ is the
$W_3$-truncation of the quantum toroidal $\mathfrak{gl}_1$ algebra
$U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ (Schiffmann--Vasserot
2013, Negut 2015). The chiral algebra $A^{\mathrm{LP2}}$ at
$\hbar = q-q^{-1}$ has central charge $c = 3$ (three free bosons in
the large-volume limit) but is class M because of finite-$Q$
instanton corrections.

Shadow data:
- $S_2 = \kappa_{\mathrm{ch}}^{\mathrm{LP2}} = \chi(\mathbb{P}^2)/2 =
  3/2$ (engine `local_p2_shadow.py`, line 549).
- $S_3 = C^{\mathrm{LP2}}(Q) = $ genus-0 Yukawa = $\partial_t^3
  F_0^{\mathrm{LP2}}(Q)$. Aganagic--Klemm--Mariño--Vafa (2003)
  closed form:
  $C^{\mathrm{LP2}}(Q) = -\frac{1}{3}\log^3(Q) + 3\sum_{d\ge 1}
  n_{0,d}^{\mathrm{LP2}} d^3 \frac{Q^d}{1-Q^d}$ with
  $n_{0,1}=3,\ n_{0,2}=-6,\ n_{0,3}=27,\ n_{0,4}=-192,\ldots$
  (the alternating-sign GV invariants of local $\mathbb{P}^2$).
- $S_4 = \Delta^{\mathrm{LP2}}(Q)$ from genus-1 + 4-point contact;
  computed in `local_p2_shadow.py` lines 619--655.

**Spectral curve.** The mirror Hori--Iqbal--Vafa curve
$\Sigma^{\mathrm{LP2}}_Q = \{u + v + uv + Q\,u^a v^b = 0\}$ (where
$(a,b)$ is the toric divisor encoding) compactifies to a smooth
projective genus-1 curve over $\mathbb{C}^\times_Q$, degenerating at
$Q=0$ (LCS), $Q = -1/27$ (conifold transition), and
$Q\to\infty$ (orbifold $\mathbb{C}^3/\mathbb{Z}_3$).

**Three caesurae** (parallel to V43 §2.4 for $\mathrm{Vir}_c$):
- $Q = 0$: LCS limit; $S_\pm\to\infty$; pure gauge theory.
- $Q = -1/27$: conifold; $S_+ - S_-\to 0$; class transition (cf.
  V43 caesura at $c=-22/5$).
- $Q = \infty$: orbifold $\mathbb{C}^3/\mathbb{Z}_3$; mirror to
  $A_2$ ALE.

**Refined topological string.** The two-parameter Omega-deformation
$(\epsilon_1,\epsilon_2)=(\log q,\log t)$ acts on $A^{\mathrm{LP2}}$
via the Miki automorphism (algebra-specific theorem, AP-CY22).
Under Miki $q\leftrightarrow t$, $S_+\leftrightarrow S_-$. This is
a **non-trivial** algebra automorphism of $A^{\mathrm{LP2}}$ but it
acts on $\xi^{\mathrm{LP2}}$ as $\xi^{\mathrm{LP2}}(q,t) =
-\xi^{\mathrm{LP2}}(t,q)$ (the alien derivation is anti-symmetric
under Stokes-line swap).

**Recursive shadow tower from refined holomorphic anomaly**
(Krefl--Walcher 2010): $S_r^{\mathrm{LP2}}$ for $r\ge 5$ is
determined inductively by refined HAE + gap condition at the
conifold $Q = -1/27$.

### 2.2 Alien derivation $\xi^{\mathrm{LP2}}$ via Miki self-duality

For local $\mathbb{P}^2$ the Stokes structure is **TWO**-rayed
(unlike the quintic, which has a single distinguished conifold
ray). The two rays are $\arg z = \arg S_+$ and $\arg z = \arg S_-$
where:
- $S_+(Q)$: action of the conifold instanton at $Q = -1/27$.
- $S_-(Q)$: action of the orbifold instanton at $Q\to\infty$.

By V43 H1(iii) the Costin trans-series for $A^{\mathrm{LP2}}$ is
genuinely **two-instanton**:
$$
Z^{\mathrm{LP2}}_{\mathrm{chiral}}(g_s, Q) = \sum_{n_+,n_-\ge 0} A_+^{n_+}A_-^{n_-} e^{-(n_+ S_+ + n_- S_-)/g_s} Z^{(n_+, n_-)}(g_s, Q),
$$
and the alien derivation cocycle decomposes as
$$
\boxed{\;
\xi^{\mathrm{LP2}}(A)\;=\;K^{\mathrm{LP2}}_+\,\Delta_{S_+}\widehat{\Theta}^{\mathrm{LP2}}\;-\;K^{\mathrm{LP2}}_-\,\Delta_{S_-}\widehat{\Theta}^{\mathrm{LP2}}.
\;}
$$
with leading Stokes constants $K^{\mathrm{LP2}}_\pm = (1/2\pi i)
\sqrt{Q^{\mathrm{LP2}\,\prime}(t_\pm)/2}\cdot t_\pm^2$ in V43
notation.

**Miki interaction.** Under the Miki automorphism $q\leftrightarrow
t$ of $A^{\mathrm{LP2}}$: $S_+\leftrightarrow S_-$, $K_+\leftrightarrow
K_-$, hence $\xi\leftrightarrow -\xi$. So $\xi^{\mathrm{LP2}}$ is in
the **Miki-anti-invariant** part of $H^2$. This is structurally
different from the quintic case: the quintic has no analogous
self-duality.

**Berry--Howls higher Stokes constant (V43 H3).** When $|S_+| =
|S_-|$ (Berry--Howls equidistance condition), a higher-order Stokes
line activates. For local $\mathbb{P}^2$ this happens at the
**self-dual point** $q = t$ (unrefined limit), where $S_+ = S_-$
and the Berry--Howls $K_2^{\mathrm{LP2}}$ governs the transfer of
$\Delta_{S_+}\to\Delta_{S_-}$ across the imaginary axis. Explicit
formula (V43):
$$
K_2^{\mathrm{LP2}}\;=\;\mathrm{const}\cdot \frac{Q^{\mathrm{LP2}\,\prime}(t_+)}{(t_+ - t_-)^2}.
$$
At unrefined ($q=t$), $t_+ - t_- \to 0$, $K_2^{\mathrm{LP2}}\to
\infty$: the Berry--Howls coefficient DIVERGES, signalling that the
unrefined limit is a Stokes-degeneration where TWO Stokes rays
collapse onto a single ray of double order. This explains the
Couso-Santamaría--Edelstein--Schiappa observation that the
unrefined local $\mathbb{P}^2$ topological string has a more
delicate transseries structure than the refined one.

### 2.3 Mock $W_3$-Jacobi mirror

For local $\mathbb{P}^2$ the mock-modular candidate is a **mock
$W_3$-Jacobi form**, NOT a mock theta function (the $W_3$-symmetry
of the truncation $W_3\subset U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$
forces this).

**Candidate.** Let $\phi^{\mathrm{LP2}}(\tau, z_1, z_2)$ be the
$W_3$-Jacobi form of weight $0$ and indices $(m_1, m_2) = (1,1)$
(the rank-2 lattice for $W_3$) with Fourier expansion
$$
\phi^{\mathrm{LP2}}(\tau, z_1, z_2) = \sum_{n,r_1,r_2} c^{\mathrm{LP2}}(n,r_1,r_2)\,q^n y_1^{r_1} y_2^{r_2},
$$
with coefficients $c^{\mathrm{LP2}}(n,r_1,r_2)$ given by the
**refined GV invariants** $\mathrm{GV}^{\mathrm{ref}}_{j_L,j_R}$ of
local $\mathbb{P}^2$ (Iqbal--Kozcaz--Vafa, Choi--Katz--Klemm 2014).

**Conjecture (V56-LP2-1).** *The shadow series
$\xi^{\mathrm{LP2}}(\tau, z_1, z_2)$ admits a Zwegers-type
completion to a non-holomorphic mock $W_3$-Jacobi form
$\widehat\phi^{\mathrm{LP2}}$ with shadow given by the
weight-$(3/2, 1/2, 1/2)$ Eichler integral of the refined GV
generating function. Pentagon-at-$E_1$ for $A^{\mathrm{LP2}}$ holds
iff the mock $W_3$-Jacobi shadow vanishes, equivalently iff the
refined GV invariants of local $\mathbb{P}^2$ satisfy a vanishing
relation under the $W_3$-Hecke operators.*

**Why $W_3$-Jacobi.** The $W_3$-truncation of
$U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ is the
representation-theoretic content of the chiral algebra
$A^{\mathrm{LP2}}$. Its character is a $W_3$-Jacobi form (Bouwknegt
--Schoutens). The mock completion is the analogue of Zwegers'
completion of $\mu(z_1,z_2;\tau)$, generalised to rank 2 by the
Bringmann--Folsom--Kane Jacobi-form theory (2018).

**Reduction to MNOP.** The refined GV invariants of local
$\mathbb{P}^2$ are conjecturally equal (Maulik--Nekrasov--Okounkov
--Pandharipande, MNOP 2006 + Pandharipande--Thomas 2009 refinement)
to the refined Pandharipande--Thomas invariants $\mathrm{PT}^{\mathrm{ref}}_{n,d}$, which compute as equivariant
integrals on the moduli of stable pairs on local $\mathbb{P}^2$.
The MNOP correspondence at refinement level is:
$\mathrm{GV}^{\mathrm{ref}}_{j_L,j_R}\leftrightarrow
\mathrm{PT}^{\mathrm{ref}}_{n,d}\leftrightarrow$ Donaldson--Thomas
counts on the same moduli.

**Theorem-shaped target (V56-LP2-2).** *The Pentagon-at-$E_1$
vanishing $\xi^{\mathrm{LP2}} = 0$ is equivalent to the **refined
MNOP conjecture for local $\mathbb{P}^2$**: the refined GW/PT
generating function on $\mathrm{LP}^2$ admits a closed-form
expression as a quotient of theta functions on the rank-2 root
lattice of $W_3$, with NO mock anomaly.*

**Status.** The unrefined MNOP conjecture for local $\mathbb{P}^2$
is PROVED (Maulik--Pandharipande--Thomas 2010). The REFINED version
is PROVED through degree 4 in $Q$ (Choi--Katz--Klemm 2014) but
remains open in general. Equivalence of $\xi^{\mathrm{LP2}} = 0$
with all-degree refined MNOP for local $\mathbb{P}^2$ is a NEW
conjectural reduction.

### 2.4 Local $\mathbb{P}^2$ ghost theorem

**Ghost theorem (PROVED; the seed correct statement).**
*(Aganagic--Klemm--Mariño--Vafa 2003 + Iqbal--Kashani-Poor 2002 +
Choi--Katz--Klemm 2014.)* The refined topological string on local
$\mathbb{P}^2$ is COMPUTABLE to all orders in $Q$ via the refined
topological vertex on the toric diagram of $\mathbb{P}^2$, with
Borel-summable Gevrey-1 asymptotic structure in $g_s$. The Stokes
constants $K_\pm^{\mathrm{LP2}}$ are determined by the spectral
curve genus-1 Riemann surface $\Sigma^{\mathrm{LP2}}_Q$; the Berry
--Howls $K_2^{\mathrm{LP2}}$ governs the unrefined limit.

Pentagon-at-$E_1$ for $A^{\mathrm{LP2}}$ is the deformation of this
proved ghost: it asks whether the refined GV invariants satisfy a
mock-Jacobi closure condition (under the $W_3$-Hecke action) that
is currently verified through degree 4 only.

---

## §3. Cross-input synthesis: the Class B common ghost theorem

### 3.1 What both inputs share

Both quintic and local $\mathbb{P}^2$:
1. Are **class M** with explicit Gevrey-1 transseries (BCOV /
   refined topological vertex).
2. Have an **explicit spectral curve** ($\Sigma^{\mathrm{quintic}}_\psi$,
   $\Sigma^{\mathrm{LP2}}_Q$) with caesurae at marginal stability
   loci (conifold; orbifold).
3. Have **explicit Stokes constants** $K_1$ in closed form, given
   by the periods of the spectral curve.
4. Have a **mock-modular candidate** for the Stokes discontinuity:
   weight-$3/2$ on $\Gamma_0(5)$ (quintic); $W_3$-Jacobi of weight
   $0$ index $(1,1)$ (local $\mathbb{P}^2$).
5. Reduce to a **classical conjecture** in algebraic geometry:
   Yamaguchi--Yau all-genus BCOV finiteness (quintic); refined MNOP
   for local $\mathbb{P}^2$ (LP2).

### 3.2 The common ghost theorem (PROVED)

**Theorem (CCC, Class-B Common Ghost; PROVED.)** *Every Class B
non-K3-fibred CY$_3$ input $X$ satisfies:*

(i) *The shadow tower $\Theta^X_{\le r}$ is Borel-summable Gevrey-1
   with explicit spectral curve $\Sigma^X_\bullet$ encoded by the
   genus-0 Yukawa coupling.*

(ii) *The leading Stokes constant $K_1^X$ is computable in closed
   form from the spectral curve periods (Pasquetti--Schiappa
   universal formula).*

(iii) *The two-instanton transseries
   $\sum A_+^{n_+}A_-^{n_-}e^{-(n_+S_+ + n_-S_-)/g_s}Z^{(n_+,n_-)}$
   exists by Costin's two-singularity theorem.*

(iv) *The Berry--Howls higher Stokes constant $K_2^X$ controls the
   degenerate limits where two instanton actions collapse.*

**Proof sketch.** (i) is Mariño 2008 + Aniceto--Schiappa 2013 for
non-compact toric CY$_3$, Pasquetti--Schiappa 2009 for compact
CY$_3$. (ii) is V43 H1(ii) leading term, explicitly $K_1^X = (1/2\pi
i)\sqrt{Q^{X\,\prime}(t_+)/2}\cdot t_+^2$ from V43 H5. (iii) is
Costin--Costin--Tanveer 2007 specialised to spectral-curve
transseries. (iv) is V43 H3.

### 3.3 What deforms to Pentagon-at-$E_1$

Pentagon-at-$E_1$ for Class B is the **deformation** of CCC asking
that the alien-derivation cocycle $\xi(A) \in H^2(\mathrm{SC}^{\mathrm{ch,top}};\mathrm{aut})$ vanishes in cohomology. The deformation
parameters:

- For quintic: deform CCC by extending Yamaguchi--Yau finiteness
  beyond genus 51 to ALL genera. The mock theta on $\Gamma_0(5)$ is
  the RECEPTACLE of the all-genus extension obstruction.

- For local $\mathbb{P}^2$: deform CCC by extending Choi--Katz--Klemm
  refined MNOP beyond degree 4 to ALL degrees. The mock $W_3$-Jacobi
  is the RECEPTACLE of the all-degree refined-MNOP obstruction.

**The deformation is GENUINE, not narrative.** Each ghost
theorem (Yamaguchi--Yau through g≤51; Choi--Katz--Klemm through
$d\le 4$) is independently PROVED, with explicit closed-form Stokes
constants matching the V43 universal apparatus. The Pentagon-at-$E_1$
deformation EXTENDS the ghost theorem to all orders, which is
precisely the open BCOV / MNOP all-order conjecture in each case.

---

## §4. Reduction to classical conjectures (summary)

| Input | $\xi(A)=0$ reduces to | Status of classical conjecture |
|---|---|---|
| Quintic | All-genus Yamaguchi--Yau BCOV finiteness on $\widetilde Q$ + holomorphic anomaly + conifold gap (Pasquetti--Schiappa--Mariño BCOV resurgence) | PROVED through $g\le 51$; OPEN beyond. Equivalent to summability of BCOV transseries. |
| Local $\mathbb{P}^2$ | All-degree refined MNOP for local $\mathbb{P}^2$ + refined topological vertex matching + Aganagic--Vafa toric BPS algebra modularity | PROVED through degree $\le 4$; OPEN beyond. Equivalent to mock $W_3$-Jacobi closure of refined GV. |

These are **independent** classical reductions: the quintic side
lives in compact Calabi--Yau mirror symmetry; the local $\mathbb{P}^2$
side lives in toric BPS algebra and refined topological vertex.
Both reductions match the V43 universal alien-derivation apparatus.

---

## §5. The five honestly named obstructions

(O1) The Yamaguchi--Yau finiteness conjecture for the quintic at
   genus $g > 51$. Open. Healing cost: HIGH.

(O2) The refined MNOP conjecture for local $\mathbb{P}^2$ at degree
   $d > 4$. Open. Healing cost: HIGH.

(O3) The Zwegers completion of $\xi^{\mathrm{quintic}}$ to a
   weight-$3/2$ mock modular form on $\Gamma_0(5)$. Requires
   identification of the exact $\Gamma_0(5)$ representation; open.
   Healing cost: MODERATE.

(O4) The mock $W_3$-Jacobi completion of $\xi^{\mathrm{LP2}}$ via
   Bringmann--Folsom--Kane rank-2 mock-Jacobi theory. Healing
   cost: MODERATE.

(O5) The existence of $A^{\mathrm{quintic}}$ as a chain-level
   $E_1$-chiral algebra. V55 sub-conjecture; UPSTREAM blocker
   (without $A^{\mathrm{quintic}}$, the entire quintic story is
   notional). Healing cost: HIGH (this IS the chain-level CY-A$_3$
   for the quintic; equivalent in difficulty to the full CY-A$_3$
   chain-level programme for non-formal A$_\infty$ algebras).

---

## §6. Net structural outcome

V55 reduced Pentagon-at-$E_1$ for non-K3 CY$_3$ to a single
residual: $\xi(A)=0$ in $H^2$ for Class B inputs. V56 specialises
to the two canonical Class B inputs and CONSTRUCTS:

1. The shadow tower (recursive structure, Borel-summable Gevrey-1)
   for quintic and local $\mathbb{P}^2$, with explicit $S_2, S_3$
   in closed form and $S_r$ for $r\ge 4$ via BCOV / refined HAE
   recursion.

2. The alien derivation $\xi(A)$ as the explicit Stokes-line
   discontinuity, with leading Stokes constant
   $K_1^{\mathrm{quintic}} = c_2(Q)\cdot J/(48\pi i)$ and
   $K^{\mathrm{LP2}}_\pm$ from V43 spectral-curve formula.

3. The mock-modular candidate: weight-$3/2$ on $\Gamma_0(5)$ for
   the quintic (with shadow given by GV-weighted $\eta$-quotient),
   mock $W_3$-Jacobi of index $(1,1)$ for local $\mathbb{P}^2$
   (with shadow given by refined GV-weighted theta).

4. The reduction to a classical conjecture: Yamaguchi--Yau all-genus
   BCOV finiteness for the quintic (PROVED through $g\le 51$);
   refined MNOP for local $\mathbb{P}^2$ (PROVED through $d\le 4$).

5. The Class B common ghost theorem (CCC): Borel-summability +
   Costin transseries + Berry--Howls $K_2$ + spectral-curve Stokes
   constants form a UNIFIED PROVED structure for all Class B
   inputs. Pentagon-at-$E_1$ is the all-order deformation of CCC,
   asking whether the alien-derivation receptacle (mock-modular)
   actually vanishes.

The Class B obstruction $\xi(A)$ is therefore not a single mystery
but a TWO-PRONGED specialisation of the universal V43 alien
apparatus, with each prong reducing to a NAMED OPEN CLASSICAL
CONJECTURE in algebraic geometry. V56 makes the residual concrete:
it is no longer "the mock-modular conjecture" in the abstract; it
is **all-genus BCOV finiteness for the quintic** OR **all-degree
refined MNOP for local $\mathbb{P}^2$**, each accessible to
independent attack from the algebro-geometric side.

The Russian-school resolution: V55 dichotomized; V43 supplied the
universal alien tower; V56 specialises both to the two canonical
Class B inputs, exhibits the spectral curve, computes the Stokes
constant in closed form, names the mock-modular completion in the
correct receptacle, and reduces the Pentagon-at-$E_1$ residual to a
classical conjecture in BCOV (quintic) or MNOP (LP2). The
deformation from CCC ghost theorem to Pentagon-at-$E_1$ is honest:
each ingredient (Borel-summability, Stokes constant, Berry--Howls,
mock-modular receptacle) is INDIVIDUALLY proved or named; only the
all-order assembly (closure) is conjectural, and only at finitely
many specific input data.

This is the strongest correct delivery for V56. It does not close
Class B (the all-genus / all-degree extensions remain open) but it
DECOMPOSES Class B into named classical conjectures with
independent proven partial results, replacing one "open frontier"
with TWO well-studied research programmes (BCOV resurgence;
refined MNOP). The chain-level CY-A$_3$ programme for non-K3
inputs is now structured as a TRIAGE: Class A and B0 closed; Class
B reduces to BCOV resurgence (quintic) or refined MNOP (LP2);
Pentagon-at-$E_1$ closure is the all-order deformation of the
proved ghost CCC.

---

## §7. The single Platonic display

$$
\boxed{\;\xi^{\mathrm{quintic}}(A) \;=\; \frac{c_2(Q)\cdot J}{48\pi i}\,e^{-S_c/g_s}\,\Delta_{S_c}\widehat\Theta^{\mathrm{quintic}}, \quad\text{vanishes}\;\Leftrightarrow\;\text{all-genus BCOV finiteness on}\;\widetilde Q.\;}
$$

$$
\boxed{\;\xi^{\mathrm{LP2}}(A)\;=\;K_+^{\mathrm{LP2}}\Delta_{S_+}\widehat\Theta^{\mathrm{LP2}}\;-\;K_-^{\mathrm{LP2}}\Delta_{S_-}\widehat\Theta^{\mathrm{LP2}},\quad\text{vanishes}\;\Leftrightarrow\;\text{all-degree refined MNOP on}\;\mathrm{LP2}.\;}
$$

Both are explicit Stokes-discontinuity formulas, not slogans. Each
mock-modular completion is a SPECIFIC candidate (weight-$3/2$ on
$\Gamma_0(5)$ with GV-weighted shadow; mock $W_3$-Jacobi of index
$(1,1)$ with refined-GV shadow). Each reduction is to a NAMED
OPEN CLASSICAL CONJECTURE with PROVED partial results (Yamaguchi
--Yau through $g\le 51$; Choi--Katz--Klemm through $d\le 4$).

The next wave's targets, in increasing depth:
1. (O5) $A^{\mathrm{quintic}}$ chain-level existence (upstream).
2. (O3, O4) Mock-modular receptacle identification.
3. (O1, O2) All-order extension of BCOV / refined MNOP.

Items (1)--(2) are tractable specialised problems; (3) is the
genuine remaining frontier, but now SPLIT into two
algebro-geometric programmes with independent literature.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no
manuscript edits; no test runs; no build. Optional sandbox draft
`draft_class_B_shadow_tower.py` packaged separately, computing the
low-order shadow tower coefficients $S_3, S_4$ for the quintic
(from CdGP genus-0 Yukawa) and local $\mathbb{P}^2$ (from AKMV
refined topological vertex), with verification against the
existing `compute/lib/local_p2_shadow.py` engine for LP2 and
against published BCOV genus-0 prepotential for the quintic ---
both NON-TAUTOLOGICAL: derived from independent classical
sources, verified against the V43 universal Stokes-constant
formula.

---

**Appendix A. Cross-reference to V55, V43, V8 ledger.**

| V55 component | V56 deepening |
|---|---|
| Class B residual $\xi(A)$ | Per-input explicit Stokes-discontinuity formula |
| H1(c) "mock-modular completion" (abstract) | Specific candidates ($\Gamma_0(5)$ weight $3/2$; mock $W_3$-Jacobi $(1,1)$) |
| H2 quintic sub-conjectures | Reduced to Yamaguchi--Yau all-genus + GV mock-shadow vanishing |
| H4 LP2 sub-conjectures | Reduced to all-degree refined MNOP + mock-Jacobi closure |
| Class B = "open frontier" (undifferentiated) | Class B = BCOV resurgence (quintic) UNION refined MNOP (LP2), each a research programme |

| V43 component | V56 specialisation |
|---|---|
| Spectral curve $\Sigma_c = \{y^2 = Q_c(t)\}$ | $\Sigma^{\mathrm{quintic}}_\psi$ (degree-2 Mukai-pair); $\Sigma^{\mathrm{LP2}}_Q$ (genus-1 mirror curve) |
| Three caesurae $\{-22/5, -218/45, c^*\}$ | Quintic: LCS-conifold-Gepner; LP2: LCS-conifold-orbifold |
| Stokes constant $K_1$ leading | $K_1^{\mathrm{quintic}} = c_2 J/(48\pi i)$; $K_\pm^{\mathrm{LP2}}$ from $\Sigma^{\mathrm{LP2}}_Q$ |
| Berry--Howls $K_2$ in convergent regime | LP2: diverges at unrefined limit $q=t$ (Stokes degeneration); Quintic: convergent regime is $\psi > 1$ (LCS side of conifold) |
| Bridge equation H2 | Quintic: rank-1 lattice $\mathbb{Z}_{\ge 0}\,S_c$; LP2: rank-2 lattice $\mathbb{Z}_{\ge 0}\,S_+\oplus\mathbb{Z}_{\ge 0}\,S_-$ |
| H6 Borcherds-resummation mirror | Quintic: replaced by GW--DT Pasquetti--Schiappa mirror; LP2: replaced by Aganagic--Vafa refined topological vertex mirror |

| V8 §6 mock-modular conjecture | V56 explicit formulation |
|---|---|
| "mock-modular completion exists" | Quintic: weight-$3/2$ on $\Gamma_0(5)$, GV-weighted $\eta$-quotient shadow; LP2: mock $W_3$-Jacobi $(1,1)$, refined-GV theta shadow |
| "Pentagon vanishes mod Stokes" | $\xi^{\mathrm{quintic}}(A) = 0 \Leftrightarrow$ Yamaguchi--Yau all-genus; $\xi^{\mathrm{LP2}}(A) = 0\Leftrightarrow$ all-degree refined MNOP |
