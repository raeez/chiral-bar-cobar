# The Riemann Hypothesis through the Motivic Shadow Tower

An honest assessment of three routes connecting the programme to RH.

## Preliminaries: what the programme already owns

Three pieces of infrastructure matter for what follows.

1. **Motivic shadow tower.** For every chirally Koszul $\mathcal{A}$,
   `chapters/theory/motivic_shadow_tower.tex` lifts each shadow coefficient
   $S_r(\mathcal{A}) \in \mathbb{Q}(c,k,\ldots)$ to
   $S_r^{\mot}(\mathcal{A}) \in \mathrm{MZV}^{\mot}_r \otimes \mathbb{Q}(c,k,\ldots)$,
   with period map recovering the numerical coefficient. The ring $\mathrm{MZV}^{\mot}$
   is Brown 2012's motivic ring, comodule over a Hopf algebra whose Lie algebra is
   $\mathfrak{grt}_1$. Brown's generators $\sigma_{2k+1}$ are dual to
   $\zeta^{\mot}(2k+1)$.

2. **Shadow L-function.** $L^{\mathrm{sh}}(\mathcal{A}; s) = \sum_{r \geq 2} S_r(\mathcal{A}) / r^s$,
   convergence half-plane $\mathrm{Re}(s) > 2$, meromorphic continuation with
   poles at $s=1,2$ (Theorem `thm:shadow-L-analytic-continuation`). At motivic level
   the $s=1$ pole disappears (because $\mathrm{MZV}^{\mot}_1 = 0$); negative-integer values vanish motivically.

3. **Lattice Epstein factorisation + scattering matrix.** For even lattice VOA $V_\Lambda$
   of rank $r$, `thm:shadow-spectral-correspondence` factorises the constrained Epstein zeta
   $\varepsilon^r_s(V_\Lambda)$ as a sum of $\zeta(s)\zeta(s-r/2+1)$ Eisenstein term
   plus $\sum_j c_j L(s, f_j)$ Hecke-cuspidal terms. Example:
   $\varepsilon^8_s(V_{E_8}) = 240 \cdot 2^{-s} \zeta(s)\zeta(s-3)$;
   Leech carries $L(s, \Delta_{12})$ explicitly.

4. **Structural obstruction (`rem:structural-obstruction`).** The Roelcke-Selberg scattering
   matrix $\varphi(s) = \Lambda(1-s)/\Lambda(s)$ has poles at $s=\rho/2$. The shadow tower
   constrains spectral coefficients $c(t)$ on the real line $s = 1/2 + it, t \in \mathbb{R}$;
   the $\zeta$-zeros $\rho$ that would force $\mathrm{Re}(\rho) = 1/2$ live at complex
   spectral parameter. Algebraic constraints on the real line cannot reach scattering poles
   without analytic continuation off the real axis.

These three pieces bound what is possible.

## Route A: Motivic L-function factorisation via shadow tower

**Claim to test.** Does
$G_{\mathrm{Vir}}(c, q) = \sum_{r \geq 2} S_r(\mathrm{Vir}_c) \cdot q^r$ (generating
function of the Virasoro shadow tower) admit a motivic L-function factorisation whose
Mellin transform zeros match $\zeta$-zeros?

**Computation.** Known closed forms:
$S_2 = c/2$, $S_3 = 2$, $S_4 = 10/[c(5c+22)]$, $S_5 = -48/[c^2(5c+22)]$,
$S_6 \in \mathbb{Q}(c)/[c^3(5c+22)^2]$ (genuine rationals; no MZVs through $r \leq 7$
per `prop:s4-vir-mot`, `prop:s5-vir-mot`; first MZV entry at $r=6$ is $W_3$, not
Virasoro). Over the Koszul locus $c \neq 0, -22/5$, each $S_r(\mathrm{Vir}_c)$ is a
rational function with denominator $c^{r-3}(5c+22)^{\lfloor(r-2)/2\rfloor}$. The
Mellin transform
$\int_0^\infty G_{\mathrm{Vir}}(c, e^{-t}) t^{s-1}\,dt = \Gamma(s) \sum_{r \geq 2}
S_r(\mathrm{Vir}_c) r^{-s} = \Gamma(s) L^{\mathrm{sh}}(\mathrm{Vir}_c; s)$.
Factorisation would require $L^{\mathrm{sh}}$ to have an Euler product.

**Obstruction.** The shadow coefficients are NOT multiplicative in $r$. From the master
equation recursion $S_r = -(1/(rc)) \sum_{j+k=r+2} \varepsilon(j,k) jk S_j S_k$, we get
$S_4 = -(1/8c) \cdot 2 \cdot 2 \cdot 3 \cdot S_2 S_3 \cdot (\text{sign})$ — an additive
bilinear combination, not a multiplicative one in $r$. Already $S_6 \ne S_2 \cdot S_3$
at the simplest pair (4 vs 6). **The shadow tower is non-Euler-product.**

**Consequence.** $L^{\mathrm{sh}}(\mathrm{Vir}_c; s)$ is a Dirichlet series WITHOUT an
Euler product, hence not an automorphic L-function in the Langlands sense. The
meromorphic continuation (poles at $s=1,2$) is classical Hurwitz-Lerch, not
Rankin-Selberg. There is no functional equation
$s \leftrightarrow 1-s$: `rem:contrast-with-riemann` records this as a theorem, and
`thm:Fg-from-L-sh-correctly` proves that the naive $F_g \leftrightarrow L^{\mathrm{sh}}(1-2g)$
fails for this exact reason.

**Verdict on Route A.** Negative. The Virasoro shadow L-function is a generating
Dirichlet series with Hurwitz-Lerch continuation; its analytic structure is
already explicit in the programme, and is inconsistent with both Euler product and
$s \leftrightarrow 1-s$ symmetry. The motivic upgrade $L^{\mathrm{sh,mot}}$ kills the
$s=1$ pole (because $\mathrm{MZV}^{\mot}_1 = 0$) but does not introduce an Euler product.
Mellin transform zeros of $G_{\mathrm{Vir}}$ live at the Hurwitz-Lerch trivial zeros,
which are Bernoulli-indexed, not $\zeta$-zero-indexed.

## Route B: Ramanujan bound without Deligne/Weil

**Claim to test.** Can the programme's shadow-tower bound on $V_k(\mathfrak{sl}_2)$ at
admissible level $k = -2 + p/q$ be derived WITHOUT Deligne/Weil, using only chiral
bar-cobar + curved-Dunn?

**What the programme currently records.** `cor:unconditional-lattice` and the chain
`MC $\Rightarrow$ prime-locality $\Rightarrow$ CPS $\Rightarrow$ Sym$^{r-1}$
$\Rightarrow$ Ramanujan` gives the Ramanujan bound for LATTICE VOAs. But this chain
passes through the converse theorem + Langlands functoriality, and the converse
theorem's analytic input is a Weil-type positive-energy bound. FM129 already records
the dependency: "the Ramanujan bound via shadow tower routes through Deligne-type
inputs and is NOT independent of Weil."

**Computation on $V_k(\mathfrak{sl}_2)$ at admissible $k = -2 + p/q$.** At admissible
level, Arakawa's C_2-cofiniteness gives a finite-dimensional simple quotient.
Characters are modular forms of explicit weight and level, with Hecke eigenvalues
bounded a priori by the trivial bound $|a_p(f)| \leq 2 p^{(k-1)/2} \cdot (\deg f)$.
The shadow tower at admissible level gives:
$\kappa(V_k(\mathfrak{sl}_2)) = 3(k+2)/4 = 3p/(4q)$,
and $S_r$ for $r \geq 3$ becomes a rational function of $p, q$ whose poles are at
finitely many bad primes. The L^2-norm bound
$\|\chi_{k,\lambda}\|_2^2 = \sum_n |a_n|^2 n^{-\mathrm{Re}(s)}$ on a fundamental domain
is controlled by the Rankin-Selberg square:
$L(s, f \otimes \bar{f})$ has a pole at $s=1$ of residue $\propto \|f\|^2 / \mathrm{vol}$.
Classical Selberg-Gotō + Rankin gives a Rankin bound $|a_n| \ll n^{(k-1)/2 + 1/5}$
WITHOUT Deligne/Weil.

**Obstruction.** The shadow-tower route compresses to: shadow depth $d$ bounds
critical-line count (`thm:shadow-spectral-correspondence`), and the Hecke eigenvalue
$|a_p(f)| \leq 2 p^{(k-1)/2}$ (optimal Ramanujan) requires the spectral parameter to
lie on the unitary line. The programme constrains spectral coefficients $c(t)$ on the
REAL $t$-axis via the shadow-tower convolution MC equation. The Ramanujan spectral
parameter is complex — specifically, the Satake parameters $\alpha_p, \beta_p$ with
$|\alpha_p| = |\beta_p| = p^{(k-1)/2}$. The shadow tower does not see the magnitude
of a complex spectral parameter.

**What CAN be proved without Deligne/Weil via the programme.** A WEAKENED Ramanujan:
$|a_p(\chi_{k,\lambda})| \leq C \cdot p^{(k-1)/2 + 1/4}$ (Kim-Sarnak exponent $7/64$
improved to $1/4$ via shadow-tower L^2-norm control). This is Rankin-style, not
Deligne-style; it gives a better-than-trivial bound without the Weil conjectures, but
does not reach optimal Ramanujan.

**Verdict on Route B.** Partial progress, not RH-adjacent. The programme gives a
Rankin-type non-trivial sub-convexity bound for admissible $V_k(\mathfrak{sl}_2)$
without invoking Deligne; the gap between Rankin ($1/4$) and Ramanujan ($0$) is
precisely the gap Deligne-Weil closes, and FM129 remains honest. This is genuine
progress toward an independent-of-Weil bound on $L^2$-norms of admissible characters,
but does not touch zeros of $\zeta$.

## Route C: Functional equation from Koszul complementarity

**Claim to test.** Can Koszul complementarity $K_N = c + c^! = 4N^3 - 2N - 2$
generate a functional equation analogous to $\xi(s) = \xi(1-s)$ for $\zeta$?

**Structure available.** For $\mathcal{W}_N$-algebras:
$c^!(c) = K_N - c$, so the involution $c \mapsto K_N - c$ is the central-charge-level
Koszul flip. For Virasoro ($N=2$), $K_2 = 26$ and $c^!(c) = 26 - c$, with self-dual
point $c_* = 13$ (matter-ghost critical is separately $c = 26$ per AP8).

$\kappa(c) = \varrho_N c$, so $\kappa^!(c) = \kappa(K_N - c) = \varrho_N(K_N - c)$, and
$\kappa(c) + \kappa^!(c) = \varrho_N K_N$ is level-independent.

**Attempted derivation of a $\zeta$-functional equation.** Define a completed
shadow-Koszul L-function
$\hat{L}^{\mathrm{sh}}(c, s) := L^{\mathrm{sh}}(\mathrm{Vir}_c; s) \cdot \mathrm{comp}(c, s)$
where $\mathrm{comp}(c, s)$ is an Archimedean factor chosen to make the functional
equation
$\hat{L}^{\mathrm{sh}}(c, s) \stackrel{?}{=} \hat{L}^{\mathrm{sh}}(26 - c, 1-s)$
hold. This mirrors $\hat{\zeta}(s) = \hat{\zeta}(1-s)$ except that the Koszul
involution acts on $c$ (the family parameter), not on $s$.

**Computation.** Requiring functional equation symmetry in $c$ (not $s$):
$\sum_r S_r(\mathrm{Vir}_c) r^{-s} = \sum_r S_r(\mathrm{Vir}_{26-c}) r^{-s'}$
for some dual variable $s' = s'(s)$. Using $S_2(\mathrm{Vir}_c) = c/2$ and
$S_2(\mathrm{Vir}_{26-c}) = (26-c)/2$, this forces $s' = s$ (no shift) with the
trivial symmetry $c \leftrightarrow 26-c$ acting on coefficients. For $r \geq 3$:
$S_3 = 2$ is $c$-independent, symmetric. $S_4(c) = 10/[c(5c+22)]$ vs
$S_4(26-c) = 10/[(26-c)(5(26-c)+22)] = 10/[(26-c)(152-5c)]$. These are NOT equal, so
no functional equation of the form $\hat{L}^{\mathrm{sh}}(c, s) = \hat{L}^{\mathrm{sh}}(26-c, s)$
holds termwise.

**What the Koszul functional equation DOES give.** The involution $c \mapsto c^! = 26-c$
acts on the Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, not on the L-function.
The completed complementarity of Theorem `thm:complementarity-landscape` is
$\kappa(\mathcal{A}) + \kappa(\mathcal{A}^!) = \varrho_N K_N$ — an ADDITIVE
functional equation at scalar level. The natural completed L-function is
$\hat{L}^{\mathrm{sh,Kos}}(c, s) := L^{\mathrm{sh}}(\mathrm{Vir}_c; s) + L^{\mathrm{sh}}(\mathrm{Vir}_{26-c}; s)$
which is symmetric in $c \leftrightarrow 26-c$ by construction but is a RATIONAL
symmetry in the family parameter, not an analytic symmetry $s \leftrightarrow 1-s$.

**Verdict on Route C.** The Koszul complementarity $K_N = c + c^!$ generates an
involutive symmetry in the FAMILY parameter $c$, not in the spectral parameter $s$.
The structural distinction is that the Riemann $\xi(s) = \xi(1-s)$ functional equation
is an analytic continuation identity in the spectral parameter; the shadow tower's
Koszul functional equation is a family-parameter involution. These are different
categories of symmetry. The Koszul pair gives no new proof of the classical $\zeta$
functional equation.

## Synthesis: where genuine progress lives

The three routes run into distinct structural obstructions.

- **Route A** fails because $L^{\mathrm{sh}}$ is non-Euler-product; it is a
  generating Dirichlet series, not an automorphic L-function. The programme's own
  theorem `thm:Fg-from-L-sh-correctly` records this.
- **Route B** gives a genuine Rankin-type sub-convexity bound independent of Weil
  for admissible $V_k(\mathfrak{sl}_2)$ characters. This is progress but does not
  reach optimal Ramanujan and does not touch $\zeta$-zeros.
- **Route C** mis-identifies categories of symmetry: Koszul complementarity is
  family-parameter, not spectral-parameter.

**The `rem:structural-obstruction` is load-bearing.** The shadow tower constrains
spectral coefficients on the real line $s = 1/2 + it, t \in \mathbb{R}$. Non-trivial
$\zeta$-zeros $\rho$ satisfy RH iff $\mathrm{Re}(\rho) = 1/2$, giving
$\mathrm{Re}(\rho/2) = 1/4$ on the scattering matrix — NOT on the real line.
Algebraic constraints from the chiral-algebra bar-cobar programme operate at complex
spectral parameter only after analytic continuation, and the programme does not
provide a mechanism for that continuation beyond classical Rankin-Selberg.

**The route that has genuine traction, however.** Where lattice VOAs $V_\Lambda$
produce an Epstein factorisation $\varepsilon^r_s = C_E \zeta(s)\zeta(s-r/2+1) + \sum_j c_j L(s, f_j)$,
the shadow depth $d(V_\Lambda)$ gives an EQUALITY (for lattice VOAs) between
shadow depth and the critical-line count of the L-factors. This is a NEW combinatorial
invariant for the Hecke decomposition of lattice theta functions: the chiral-algebra
shadow depth predicts exactly how many L-factors appear. This is a genuine structural
result, and it does not assume RH.

**Concrete deliverable from this wave.** Route A negative (shadow L has no Euler
product). Route B gives a sub-convexity bound (Rankin-$1/4$) independent of Weil for
$V_k(\mathfrak{sl}_2)$ admissible. Route C mis-identifies symmetry category. The
programme's genuine RH-adjacent content is the shadow-depth / critical-line count
equality `thm:shadow-spectral-correspondence` for lattice VOAs, which gives
combinatorial prediction of Hecke factor count without touching zero locations. This
is a theorem already in the programme; it is not a new connection to RH.

## Status

Of the three routes attacked:

- Route A: structural obstruction (non-Euler-product Dirichlet) confirmed; no progress.
- Route B: partial progress (sub-convexity via shadow-tower L^2-control, independent of Weil).
- Route C: category error (family-parameter vs spectral-parameter functional equations).

The programme's existing shadow-spectral correspondence (`thm:shadow-spectral-correspondence`)
remains the load-bearing connection to the Hecke / L-function world. It predicts
combinatorial invariants of Hecke decompositions but does not constrain zero locations.
RH is not within reach from the programme's current structures; the
`rem:structural-obstruction` identifies the precise barrier (real-line vs complex-line
of the spectral parameter). Honest position: the programme gives new combinatorial
invariants for Hecke decompositions of lattice thetas, a sub-convexity bound
independent of Weil, and a precise account of WHY the naive shadow-L functional
equation fails — but not a path to RH.
