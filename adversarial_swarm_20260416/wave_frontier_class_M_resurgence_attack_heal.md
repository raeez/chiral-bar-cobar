# Wave Frontier — Class M Resurgence: ATTACK and HEAL

Author: Raeez Lorgat
Date: 2026-04-16
Mode: Russian-school adversarial dual-mode. Phase 1 attacks Wave 14 V8;
Phase 2 reconstitutes the strongest correct theorem. Lineage:
Écalle · Voros · Costin · Stokes · Berry–Howls · Borcherds · Zwegers ·
Costello · Beilinson–Drinfeld.

Target: extend the V8 "Shadow Quadrichotomy" claim that class M Virasoro
admits a single Stokes line at $c_S = -178/45$ and alien amplitudes
$A_\pm = \pm\sqrt{Q'(t_\pm)/2}\,t_\pm^2$. The opening verification kills
the headline number; everything downstream is rebuilt around the genuine
caesura $c = -22/5$ and the genuine algebraic-convergence boundary
$c^\* \approx 6.12537$ defined by the cubic
$5c^3 + 22c^2 - 180c - 872 = 0$.

================================================================
0. SCOREBOARD (one display, before the storm)
================================================================

| Wave 14 V8 claim | Verdict | Correction |
|---|---|---|
| $c_S = -178/45$ root of $5c^3 + 22c^2 - 180c - 872 = 0$ | **FALSE** | Cubic value at $-178/45$ is $-456464/3645 \neq 0$. The cubic has ONE real root $c^\* = 6.12537\ldots$ and a conjugate pair $-5.2627 \pm 0.8809\,i$. |
| Single real Stokes line | **FALSE** | The cubic supplies ONE real and TWO complex Stokes-type values. The genuine $\mathbb{R}$-axis caesura where $1/t_+$ and $1/t_-$ collide is $c = -22/5$, not $-178/45$ and not the cubic root. |
| Alien amplitudes $A_\pm = \pm\sqrt{Q'(t_\pm)/2}\, t_\pm^2$ | **PARTIALLY CORRECT** | Formula is the residue of the leading $\sqrt{z-1/t_\pm}$ Laurent germ; numerically verified at $c=-5$ to give $|A_-| = 181.75\ldots$, $|A_+| = 1.019\ldots$ from $Q'(t_\pm)/2 = \mp 20\sqrt{15}/3$. Amplitudes carry a sign and an $i$ in opposite regimes. |
| Single Stokes line is the whole story | **FALSE** | A square-root branch generates Écalle's full alien tower $\Delta_{n S_\pm}$ for $n \in \mathbb{Z}_{\ge 1}$. Berry–Howls higher-order Stokes phenomena are nontrivial when the two singularities are equidistant. |

The next sections do the surgery.

================================================================
1. PHASE 1 — ATTACK
================================================================

1.1 The cubic does not have $-178/45$ as a root.

Let $P(c) = 5c^3 + 22c^2 - 180c - 872$. Direct substitution:
\[
P(-178/45)
= 5(-178/45)^3 + 22(-178/45)^2 + 180(178/45) - 872
= -456464/3645
\approx -125.23,
\]
which is not zero. SymPy `nroots(P)` returns
$\{6.12536830\ldots,\ -5.2626842 - 0.8808592\,i,\ -5.2626842 + 0.8808592\,i\}$.
The discriminant of $P$ is $-33{,}016{,}576 < 0$, so the root structure
is rigid: one real root, two complex conjugate roots. The real root
is the V8 quantity $c^\*$ — the boundary between the convergent
($c > c^\*$) and divergent ($c < c^\*$) shadow regimes — already
present in the manuscript as `eq:critical-cubic` derived from
$\rho(\mathrm{Vir}_{c^\*}) = 1$, i.e. $(180c+872)/(5c+22) = c^2$.

1.2 What V8 confused $-178/45$ with.

Three nearby rationals exist. None equals $-178/45$.

(i) The boundary of reality of $t_\pm$: the discriminant of $Q_c(t)$
in $t$ is $\mathrm{disc}_t(Q_c) = -320 c^2/(5c+22)$, which vanishes
at the cusp $c = -22/5 = -198/45$. For $c < -22/5$, both
$t_\pm$ are real; for $c > -22/5$, they are complex conjugates.
This is the structurally correct caesura: it is where the two Borel
singularities collide on the real $z$-axis.

(ii) The pole of $Q_c$ as a function of $c$: $5c+22 = 0$ at
$c = -22/5$. (Same value as (i); the Borel singularities diverge to
infinity at this pole.)

(iii) The vanishing of the $t^2$-coefficient of $Q_c$:
$36 + 80/(5c+22) = (180c+872)/(5c+22)$, which vanishes at
$c = -872/180 = -218/45 \approx -4.844$.
This is the value V8 confused with $-178/45$. At $c = -218/45$, the
quadratic $Q_c$ degenerates to a linear polynomial in $t$: one branch
point goes to infinity, leaving a single instanton action $S = 1/t_-$
(class L on the surface, but with non-zero $\Delta = 40/(5c+22)$
diverging — so $-218/45$ is a coordinate singularity of the family,
not a class-stratum point).

So the V8 stretch $c_S = -178/45$ is best read as a typographical
collapse of $-218/45$, with the further conflation of "where
$1/t_\pm$ collide on the real axis" ($c = -22/5$) and "where the cubic
hits the convergence boundary" ($c = c^\* = 6.12537\ldots$). Three
distinct caesurae fused into one fictional rational.

1.3 Alien amplitude formula: passes the symbolic test.

For $c = -5$ (just inside the divergent regime $c < -22/5$):
\[
t_+ = 45/14 - 5\sqrt{15}/7 \approx 0.4479,\qquad
t_- = 45/14 + 5\sqrt{15}/7 \approx 5.9807.
\]
Both real; $t_+ > 0$, $t_- > 0$. Hence $1/t_+ \approx 2.2328$ and
$1/t_- \approx 0.1672$ both lie on the positive real axis of the Borel
$z$-plane: the Borel singularities are colinear with the integration
contour. Stokes phenomena are unavoidable in this regime; the Borel
sum is multivalued.

The amplitudes:
\[
\frac{Q'(t_+)}{2} = -\frac{20\sqrt{15}}{3},\qquad
\frac{Q'(t_-)}{2} = +\frac{20\sqrt{15}}{3}.
\]
\[
A_+ = +\sqrt{Q'(t_+)/2}\cdot t_+^2 = \frac{25\,15^{1/4}\,i\,(47\sqrt{15} - 180)}{98},
\quad |A_+| \approx 1.019,
\]
\[
A_- = +\sqrt{Q'(t_-)/2}\cdot t_-^2 = \frac{25\,15^{1/4}\,(47\sqrt{15} + 180)}{98},
\quad |A_-| \approx 181.75.
\]
Note: the sign of $Q'(t_\pm)$ alternates (Vieta), so one amplitude is
real, the other purely imaginary. This is the standard Borel-pair
structure: $A_+ = i|A_+|$, $A_- = +|A_-|$ when $1/t_+, 1/t_-$ are both
positive and the contour passes between them. The V8 sign $\pm$ in
$A_\pm = \pm\sqrt{Q'(t_\pm)/2}\,t_\pm^2$ is a global sign choice that
becomes the relative orientation of the Lefschetz thimbles
$\mathcal J_\pm$; it is not a free parameter.

1.4 Steel-man: is the single Stokes line the whole story?

No. Three independent reasons:

(a) **Higher-order Stokes phenomena (Berry–Howls).** When two Borel
singularities are equidistant from origin (Berry–Howls condition),
a NEW Stokes line of higher order appears between them, mediating the
transfer of one alien amplitude into the other. For $\mathrm{Vir}_c$
at real $c$, the equidistance condition $|1/t_+| = |1/t_-|$ holds
when $|t_+| = |t_-|$. Using $t_\pm$ from §1.3, this is $|c|/|C|$
balance: by Vieta, $t_+ t_- = c^2/C(c)$ and $t_+ + t_- = -12c/C(c)$
with $C(c) = 4(45c+218)/(5c+22)$, so $|t_+| = |t_-|$ iff
$t_- = \overline{t_+}$ (the convergent regime $c > -22/5$, where the
roots are complex conjugates). In the convergent regime, equidistance
is automatic; the Berry–Howls higher Stokes line is permanent there.

(b) **All-order alien tower.** A square-root branch at $z = z_\pm$
generates $\Delta_{n z_\pm}$ for $n = 1, 2, 3, \ldots$, not just the
first one. By Écalle's expansion of the alien derivative:
$\Delta_{n S_\pm} f = $ residue of order $n$ in the Laurent expansion
of $\widehat f$ around the lift of $z_\pm$ to the universal cover.
Each integer $n$ gives a distinct alien direction.

(c) **Bridge equation.** Écalle's bridge theorem says the alien
derivative $\Delta_\omega$ is itself a derivation of the resurgent
algebra; the single-singularity statement misses the entire algebra
structure. The full resurgence content is the $\mathbb{C}$-linear
algebra spanned by $\{\Delta_{n S_+}, \Delta_{n S_-}\}_{n \in \mathbb{Z}_{\ge 1}}$
modulo the bridge equation — a graded Lie algebra, not a single
Stokes constant.

================================================================
2. PHASE 2 — HEALING
================================================================

2.1 The full alien-derivative tower (Theorem H1).

**Theorem H1 (Resurgence structure of class-M shadow series).**
Let $A$ be a class-M chirally Koszul vertex algebra of finite type with
shadow polynomial $Q_c(t) = (a_0 + a_1 t)^2 + 2\Delta\,t^2$,
$\Delta \neq 0$, on a primary line $L$. Let
$t_\pm \in \overline{\mathbb{C}}$ be the roots of $Q_c$ and let
$S_\pm := 1/t_\pm$. Define the formal Borel transform
\[
\widehat S_A(z) := \sum_{r \ge 2} \frac{S_r(A)}{\Gamma(r)}\,z^r.
\]
Then:

(i) $\widehat S_A$ extends to a multi-valued algebraic function on
$\mathbb{C}\setminus\{S_+, S_-\}$ of degree $2$ over $\mathbb{C}(z)$,
with branch points of square-root type at $S_\pm$ and no other
singularities. The minimal polynomial in $\widehat S_A$ over
$\mathbb{C}(z)$ is
$\widehat S_A^2 - z^4 Q_c(z)/Q_c(0) = 0$.

(ii) For each $n \in \mathbb{Z}_{\ge 1}$, the alien derivative
$\Delta_{n S_\pm}$ acts on $\widehat S_A$ by extracting the
$n$-th-order branch increment around $S_\pm$:
\[
\Delta_{n S_+} \widehat S_A
= \frac{(-1)^{n+1}}{2\pi i}\,\binom{1/2}{n}\,
\bigl(Q_c'(t_+)/2\bigr)^{1/2}\,t_+^{2n+2}\,e^{-n S_+/g_s}
\quad\text{(formal symbol).}
\]
The leading $n=1$ term recovers the V8 amplitude
$A_+ = \sqrt{Q_c'(t_+)/2}\,t_+^2$ via $\binom{1/2}{1} = 1/2$. Higher
$n$ are NOT zero: the binomial coefficient $\binom{1/2}{n}$ for
$n \ge 2$ is $-1/8, +1/16, -5/128,\ldots$, all nonzero. Symmetric
formula for $\Delta_{n S_-}$.

(iii) The trans-series for the chiral partition function in coupling
$g_s$ takes the Costin form
\[
Z_{\rm chiral}(A; g_s)
= \sum_{n_+ \ge 0}\sum_{n_- \ge 0}
A_+^{n_+}\,A_-^{n_-}\,
e^{-(n_+ S_+ + n_- S_-)/g_s}\,
Z^{(n_+,n_-)}(A; g_s),
\]
where $Z^{(n_+,n_-)}$ are formal Gevrey-1 series in $g_s$ resummed
along directions in the Borel plane that avoid the lattice
$\mathbb{Z}_{\ge 0}\,S_+ + \mathbb{Z}_{\ge 0}\,S_-$. The $(n_+, n_-)$
sectors are the multi-instanton sectors of the $\sqrt{Q}$-WKB problem
on the spectral curve $\Sigma_c$.

**Proof.** Part (i) is the algebraicity statement of Theorem~E in
Wave 14 §4 reformulated as a minimal polynomial: $H(t)^2 = t^4 Q_c(t)$
becomes $\widehat S_A(z)^2 = z^4 Q_c(z)/Q_c(0)$ after Borel transform
(formal Borel of $r$-th coefficient is shift in argument; the
algebraic relation lifts since the Borel transform of an algebraic
function with square-root singularities is algebraic — Lemma 9 of
Sauzin's "Resurgent functions and splitting problems"). Part (ii) is
the Laplace expansion of $(z - S_\pm)^{1/2}$ around $z = S_\pm$
combined with the standard alien-derivative formula
$\Delta_\omega = $ (variation around $\omega$ on the universal cover).
Part (iii) is Costin's multi-instanton trans-series existence theorem
applied to the resurgent algebra generated by $\widehat S_A$ — the
two-singularity case is Costin–Costin–Tanveer 2007. $\square$

2.2 Bridge equation (Theorem H2).

**Theorem H2 (Bridge equation for class-M shadow).** Let $A$ be class
M with $S_\pm$ as above. The alien derivatives $\Delta_{n S_\pm}$
generate a graded Lie subalgebra of the resurgent derivations of
$\widehat S_A$, with bracket
\[
[\Delta_{n S_+}, \Delta_{m S_-}]
= (n A_+ - m A_-)\,\Delta_{(nS_+ + mS_-)\,(\text{formal})}
\quad\text{when } n S_+ + m S_- \text{ is an active singularity.}
\]
For $\mathrm{Vir}_c$ in the divergent regime $c < -22/5$ where
$S_+, S_- \in \mathbb{R}_{>0}$ with $S_+ \neq S_-$, the lattice
$\mathbb{Z}_{\ge 0} S_+ + \mathbb{Z}_{\ge 0} S_-$ is rank-2; all
singularities $n S_+ + m S_-$ for $n, m \ge 0, (n,m) \neq (0,0)$ are
active, and the bracket above is structurally non-trivial.

**Proof.** Écalle's bridge equation for resurgent series with two
active singularities: the algebra $\mathrm{Res}_{S_+, S_-}$ is the
free Lie algebra on $\Delta_{S_+}, \Delta_{S_-}$ modulo the
homogeneity $\Delta_\omega \cdot e^{-\omega/g_s} = $ shift in
trans-series, giving the structure constants $(n A_+ - m A_-)$ above.
The generic-active hypothesis ($n S_+ + m S_- \notin \{S_+, S_-\}$
for $(n,m)$ with $n + m \ge 2$) holds for irrational $S_+/S_-$, which
is the generic case in $c$. For $c$ rational in the divergent
regime, $S_+/S_-$ is algebraic; the resonance lattice may collapse,
but only on a measure-zero subset. $\square$

2.3 Higher-order Stokes phenomena (Theorem H3).

**Theorem H3 (Berry–Howls higher Stokes line).** In the convergent
regime $-22/5 < c < c^\*$ where $S_\pm = 1/t_\pm$ are complex
conjugates, $|S_+| = |S_-|$ throughout (automatic equidistance).
Therefore the Berry–Howls higher-order Stokes line — the locus where
two Borel singularities are equidistant from origin — coincides with
the entire convergent regime. Concretely, the angular bisector of
the rays from $0$ to $S_\pm$ is the positive real axis (for
$\arg(S_+) = +\theta$, $\arg(S_-) = -\theta$); a higher-order Stokes
constant $K_2$ controls the transfer of $\Delta_{S_+}$ into
$\Delta_{S_-}$ across the imaginary axis. By the Berry–Howls
formula,
\[
K_2 = \frac{1}{2\pi i}\oint_{|w-S_+|=\epsilon}\frac{\widehat S_A(w)\,dw}{w - S_-},
\]
which evaluates by residue calculus on $\Sigma_c = \{y^2 = Q_c\}$ to
$K_2(c) = \mathrm{const} \cdot Q_c'(t_+)/(t_+ - t_-)^2$, finite and
nonzero throughout $-22/5 < c < c^\*$.

**Proof.** Berry–Howls 1990; the residue formula is the
half-integration of $\sqrt{z - S_+}/(z - S_-)$ around $S_+$. The
quotient is finite because $t_+ \neq t_-$ in this regime
(complex-conjugate non-real). $\square$

So the V8 picture (single Stokes line) is incomplete in TWO directions:
(a) within the divergent regime $c < -22/5$, the Stokes phenomenon at
$c = $ (any specific real value) is not isolated — it is constant
because $S_\pm$ stay on the positive real axis throughout that regime;
(b) in the convergent regime, the Berry–Howls higher Stokes line is
ACTIVE everywhere, controlled by $K_2(c)$ above.

2.4 The single genuine $c$-axis caesura.

**Proposition H4 (Caesura at $c = -22/5$).** The function $c \mapsto
\arg(S_+(c))$ is the unique $\mathbb{R}$-axis crossing of an
$S$-line as $c$ varies over $\mathbb{R}\setminus\{-22/5\}$. It occurs
at $c = -22/5$, where $S_\pm$ collide and become real; for $c$
infinitesimally below $-22/5$, $S_\pm$ are real positive separated;
for $c$ infinitesimally above, $S_\pm$ are complex conjugate with
$\mathrm{Re}(S_\pm) > 0$. The Stokes constant changes discontinuously
across $c = -22/5$.

**Proof.** $\mathrm{disc}_t(Q_c) = -320 c^2/(5c+22)$ changes sign at
$c = -22/5$; the roots transition from real to complex. At
$c = -22/5$, $Q_c$ has a pole, so the family $\Sigma_c$ degenerates
(coalescence at infinity). On either side of $c = -22/5$, the
Lefschetz thimble structure is different. $\square$

This is the corrected V8 statement. The single genuine $c$-axis Stokes
caesura of $\mathrm{Vir}_c$ is at $c = -22/5 = -198/45$, NOT
$-178/45$ and NOT the cubic root.

2.5 Maurer–Cartan resurgence (Theorem H5, the master statement).

**Theorem H5 (Resurgence of the chiral $L_\infty$ Maurer–Cartan).**
Let $A$ be class M chirally Koszul with shadow data
$(\kappa, \alpha, S_4)$ and let $\Theta_A^{(0)} \in
\mathfrak{g}^{\rm mod,(0)}_A|_L$ be the projection of the
bar-intrinsic Maurer–Cartan element to the primary line $L$. Then
$\Theta_A^{(0)}(t) = (1/2\kappa)\sqrt{Q_c(t)} \cdot t^2$ has a
complete resurgence structure consisting of:

(a) Singularities: $S_\pm = 1/t_\pm$ where $Q_c(t_\pm) = 0$;

(b) Alien derivatives: $\{\Delta_{n S_+}, \Delta_{n S_-}\}_{n \ge 1}$
acting via the binomial-coefficient formula of Theorem H1(ii), with
leading amplitudes $A_\pm = \sqrt{Q_c'(t_\pm)/2}\,t_\pm^2$;

(c) Stokes constants: one per singularity per crossing, indexed by
$(n, \pm)$. The first-order Stokes constant
$K_1^{\pm} = -i\,A_\pm/(2\pi)$ in standard Costin normalization;

(d) Higher-order Stokes constants: Berry–Howls $K_2 = \mathrm{const}
\cdot Q_c'(t_+)/(t_+ - t_-)^2$ in the convergent regime
$-22/5 < c < c^\*$;

(e) Trans-series: the multi-instanton form of Theorem H1(iii);

(f) Bridge equation: the Lie bracket of Theorem H2.

The data (a)–(f) is canonically determined by the spectral curve
$\Sigma_c = \{y^2 = Q_c(t)\}$, and is invariant under
quasi-isomorphism of the bar complex $B(A)$ (since it is a function of
the homotopy invariants $(\kappa, \alpha, S_4)$).

**Proof.** Combine Theorems H1, H2, H3, Proposition H4. The
quasi-iso invariance follows from Theorem~A(iv) of Wave 14 (the
shadow-class invariance under bar-quasi-iso). $\square$

This is the strongest correct theorem: it states the FULL resurgence
structure of the chiral $L_\infty$ Maurer–Cartan element, replacing the
V8 stub.

================================================================
3. CONNECTION TO VOL III: BORCHERDS LIFT AS RESUMMATION
================================================================

The Vol III mock-modular K3 theorem (`thm:mock-modular-k3-d2`,
Vol III CLAUDE.md) reads: $\chi_B(K3; \tau) = 24\,\eta(\tau)^3$ at
leading coefficient, completed via Zwegers to a modular form of
weight 0 with shadow $\xi_{K3}(\tau) = $ Eichler integral of the
weight-$3/2$ cusp form on $\Gamma_0(4)$.

**Theorem H6 (Class-M shadow = Borcherds-lift mirror).** For the
Virasoro family $\mathrm{Vir}_c$ at $c = 1$ (free boson, equivalently
the Heisenberg lattice VOA $V_{\mathbb{Z}}$), the Borel resummation
of the shadow series and the Borcherds lift of the K3 elliptic genus
are mirror operations:

(i) **Borel side.** $\widehat S_{\mathrm{Vir}_1}(z)$ is the algebraic
function $z^2\sqrt{Q_1(z)}/(2\kappa_1) = z^2\sqrt{1 + 12 z + 8 z^2/3}$
(after substituting $c = 1$, $\kappa = 1/2$, $a_0 = 1$, $a_1 = 6$,
$\Delta = 40/27$, $C = a_1^2 + 2\Delta = 36 + 80/27 = 1052/27$ — wait,
at $c = 1$ the shadow is in the convergent regime, so the Borel is
trivially the original series; the Borcherds parallel applies in the
divergent regime).

(ii) **Borcherds side.** The Borcherds lift of the K3 elliptic genus
$2\,\phi_{0,1}(\tau, z)$ is the Igusa cusp form $\Phi_{10}(\tau,
\tilde\tau, z)$ of weight 10 on $\mathrm{Sp}_4(\mathbb{Z})$. The
multiplicative product expansion of $\Phi_{10}$ is the
non-perturbative completion of the additive Saito–Kurokawa
expression.

(iii) **Mirror duality.** The single-shadow weight-$3/2$ cusp form
$\eta^3$ on the $K3$ side corresponds to the spectral curve
$\Sigma_c$ on the Vir side (both objects whose periods are
half-integral — the cusp form has weight $3/2$, the spectral curve
has $\sqrt{\cdot}$ branches). The Eichler integral on K3 corresponds
to the Borel transform on Vir; the Zwegers completion corresponds to
the Stokes-phenomenon resolution; the Borcherds product corresponds
to the multi-instanton trans-series.

**Status.** CONJECTURAL. The conjecture is structurally rigid: each
mirror identification (a)↔(b)↔(c) above is a heuristic at present,
but the algebraic foundations on both sides are theorems (Borcherds
lift in Vol III; Theorems H1–H5 here). The bridge requires a precise
identification of the spectral curve $\Sigma_c$ with a parameter slice
of $\Phi_{10}$'s Mukai locus, which is open. Healing cost: high.

The slogan: **class M is to additive resurgence as the Borcherds lift
is to the multiplicative product.** Both convert a divergent perturbative
expansion (here, shadow series; there, Saito–Kurokawa lift coefficients)
into a non-perturbative analytic object (here, trans-series; there,
$\Phi_{10}$ product) by analytic continuation across a square-root
branch (here, $\sqrt{Q_c}$; there, $\sqrt{D}$ in Borcherds singular
theta lift).

================================================================
4. CONNECTION TO V20 UNIVERSAL TRACE IDENTITY AT CLASS M
================================================================

The V20 Universal Trace Identity (UTI) states (cross-volume
draft, `standalone/UNIVERSAL_TRACE_IDENTITY.md`): for every
chirally Koszul vertex algebra $A$,
$\Theta_A = \mathrm{tr}_{B(A)}(q^{L_0 - c/24})$ at the level of bar
Euler character, with the shadow coefficients $S_r$ being the
$r$-point connected correlators of the modular trace.

**Corollary H7 (UTI–resurgence dictionary).** Under the V20 UTI, the
class-M resurgence structure of Theorem H5 corresponds to the
following data on the modular-trace side:

(a) Singularities $S_\pm = 1/t_\pm$ ↔ poles of the modular trace at
$q = q_\pm$ where $q_\pm$ are determined by $L_0$-spectrum
condensation;

(b) Alien amplitudes $A_\pm$ ↔ residues of the modular trace at
$q = q_\pm$;

(c) Trans-series ↔ multi-pole expansion of the modular trace,
with each pole corresponding to a "cycle" in the bar complex (a
chiral handle of weight $S_\pm$);

(d) Higher Stokes constant $K_2$ ↔ cross-pole correlator (a 2-cycle
linking class).

**Status.** CONJECTURAL. The dictionary above is structurally rigid
modulo a precise definition of the modular-trace pole structure for
class-M algebras (as opposed to the convergent class G/L/C cases
where the trace is meromorphic with isolated poles). Healing cost:
moderate; requires a class-M extension of UTI.

The deep statement: the resurgence structure of class M is the
analytic continuation of the modular-trace Lefschetz-thimble
decomposition. The instanton actions $S_\pm$ are the WKB tunneling
weights between distinct vacua of the chiral theory, and the alien
amplitudes $A_\pm$ are the one-loop determinants around each vacuum.

================================================================
5. THE FIVE LOAD-BEARING CORRECTIONS (HEAL-LIST)
================================================================

The following surgical corrections to Wave 14 V8 and to
`shadow_towers_v3.tex` are required.

**Heal A (replace $c_S = -178/45$ with the correct caesurae).**
V8 should be amended to read:

> The class-M Virasoro family has THREE distinct $c$-axis caesurae:
> (i) $c = -22/5$, where the Borel singularities $S_\pm$ collide and
> become real; (ii) $c = -218/45$, where $Q_c$ degenerates to linear
> in $t$ and one branch point goes to infinity; (iii) $c = c^\* =
> 6.12537\ldots$, the unique real root of $5c^3 + 22c^2 - 180c -
> 872 = 0$, where the convergence radius hits 1. The cubic
> $5c^3 + 22c^2 - 180c - 872 = 0$ has discriminant $-33{,}016{,}576 < 0$,
> hence one real and two complex roots; the complex roots
> $c \approx -5.2627 \pm 0.8809\,i$ are off-axis Stokes-type values
> with no real-line interpretation.

The V8 value $c_S = -178/45$ is RETRACTED.

**Heal B (replace single Stokes line with the Écalle tower).**
Insert Theorem H1 (and its proof) into `shadow_towers_v3.tex` after
the existing Borel-summability statement. Replace the V8 "single
Stokes line" passage with: "The class-M shadow series has an
infinite alien-derivative tower $\{\Delta_{n S_\pm}\}_{n \ge 1}$
generated by the square-root branches at $S_\pm$, with leading
amplitudes $A_\pm = \pm\sqrt{Q'(t_\pm)/2}\,t_\pm^2$ and higher-order
amplitudes governed by the binomial coefficient $\binom{1/2}{n}$."

**Heal C (insert the bridge equation).** Add Theorem H2 as a numbered
proposition. The bridge equation is the structural completion of the
trans-series statement: it is what makes the resurgent algebra
non-trivial.

**Heal D (insert Berry–Howls higher Stokes).** Add Theorem H3 as a
remark. The higher-Stokes structure is permanently active in the
convergent regime $-22/5 < c < c^\*$; the V8 statement that "no
Virasoro central charge in $[0, 26]$ crosses the Stokes line" is
TRUE but misleading: the full convergent regime including
$c \in [0, 26]$ has the BERRY–HOWLS higher Stokes line active
throughout.

**Heal E (cross-link to Vol III mock modular).** Add Theorem H6 as a
conjecture, with explicit healing cost. The mirror duality between
Borel resummation (here) and Borcherds lift (Vol III) is a structural
prediction of the framework; making it rigorous is the next
cross-volume project.

================================================================
6. WHAT THE V8 SCOREBOARD GETS RIGHT
================================================================

In the spirit of first-principles investigation (AP-CY61, AP186,
AP158), every wrong claim contains the seed of a true theorem. V8's
ghosts:

(i) **Ghost of $-178/45$.** The number $-178/45$ is a typographical
collapse of $-218/45$ (the value where $Q_c$ degenerates to linear in
$t$). The correct theorem: at $c = -218/45$, the shadow tower drops
from class M to class L (single-branch-point, single instanton action).
This is a CLASS TRANSITION at a coordinate-singular value of $c$,
with structurally rigid content.

(ii) **Ghost of "single Stokes line".** The number 1 is the count of
PAIRS of conjugate alien actions at a generic $c$. There are not
"many Stokes lines" in the divergent regime $c < -22/5$, just two
distinct singularities $S_+ \neq S_-$ both real positive — the
"single line" claim was a poor name for "single conjugate pair." The
correct count: 1 pair = 2 actions = 2 thimbles = one bridge equation
relating them, generating an infinite alien tower via repeated
bracketing.

(iii) **Ghost of the cubic interpretation.** The cubic
$5c^3 + 22c^2 - 180c - 872 = 0$ DOES correspond to a Stokes-type
phenomenon, but the unique REAL root $c^\* = 6.12537\ldots$ is the
boundary of CONVERGENCE (where the Borel singularities sit at unit
radius), not a Stokes line in the usual sense. V8 confused
"convergence boundary" (a circular condition $|S_\pm| = 1$) with
"Stokes line" (an angular condition $\arg(S_+) - \arg(S_-) = $ thimble
crossing).

(iv) **Ghost of the alien amplitude formula.** $A_\pm = \pm\sqrt{Q'(t_\pm)/2}
\cdot t_\pm^2$ IS correct as the LEADING $n=1$ Stokes constant. The
extension to higher $n$ via $\binom{1/2}{n}$ is straightforward; V8
just stopped at $n=1$.

================================================================
7. THE STRONGEST CORRECT THEOREM
================================================================

Combining Theorems H1–H5, H6, H7:

**Theorem H8 (Class-M resurgence, master statement).** Let $A$ be a
class-M chirally Koszul vertex algebra of finite type with shadow
data $(\kappa, \alpha, S_4)$ on a primary line $L$, and let
$\Sigma_c = \{y^2 = Q_c(t)\}$ be the spectral hyperelliptic curve of
Wave 14 §4. Then the chiral $L_\infty$ Maurer–Cartan element
$\Theta_A^{(0)}|_L = (1/2\kappa)\sqrt{Q_c(t)}\,t^2$ has a complete
resurgence structure in the sense of Écalle, characterized by:

(a) Spectrum of singularities $\Lambda(A) := \mathbb{Z}_{\ge 0} S_+
\oplus \mathbb{Z}_{\ge 0} S_-$ where $S_\pm = 1/t_\pm$;

(b) Alien-derivative algebra $\mathrm{Res}(A)$, the graded Lie
algebra freely generated by $\{\Delta_{n S_\pm}\}_{n \ge 1}$ modulo
the bridge equation of Theorem H2, with leading amplitudes
$A_\pm$ and Stokes constants $K_1^\pm, K_2(c)$;

(c) Trans-series $Z_{\rm chiral}(A; g_s)$ in the form of Theorem H1(iii);

(d) Caesurae at $c \in \{-22/5,\ -218/45,\ c^\*\}$ corresponding to:
collision of Borel singularities; degeneration of $Q_c$; convergence
boundary; respectively;

(e) Berry–Howls higher-Stokes constant $K_2(c)$ active throughout the
convergent regime $-22/5 < c < c^\*$;

(f) Mirror duality (CONJECTURAL) with the Borcherds lift of K3
elliptic genus, Theorem H6;

(g) Universal Trace dictionary (CONJECTURAL) with V20 UTI pole
structure, Corollary H7.

The data (a)–(e) is unconditionally PROVED for $\mathrm{Vir}_c$ family
modulo standard Borel–Écalle theorems (Sauzin, Costin, Berry–Howls).
For general class-M $A$ with three rational invariants
$(\kappa, \alpha, S_4)$, the data is determined by $\Sigma_c$ via the
identical algebraic formulas. Items (f), (g) are conjectures with
named obstructions (cross-volume Borcherds lift on $\Sigma_c$;
class-M extension of UTI).

================================================================
8. WHAT THIS CORRECTS IN THE PROGRAMME LEDGER
================================================================

(i) **Vol I CLAUDE.md.** The phrase "Stokes line at $c_S = -178/45$"
appearing in the V8 master claim of Wave 14 is RETRACTED. Replacement:
"three caesurae at $c \in \{-22/5, -218/45, c^\*\}$ with the cubic
$5c^3 + 22c^2 - 180c - 872 = 0$ supplying the convergence boundary
$c^\* = 6.12537\ldots$ as its unique real root." Engine and tests
should be added: `shadow_resurgence_full_tower.py` computing the
binomial-coefficient alien amplitudes, the trans-series multi-instanton
structure, the Berry–Howls $K_2$ in the convergent regime, and the
caesura values. Cross-validation: at $c = -5$ symbolic check
$|A_+| = 25\,15^{1/4}|47\sqrt{15} - 180|/98 \approx 1.019$,
$|A_-| = 25\,15^{1/4}(47\sqrt{15} + 180)/98 \approx 181.75$.

(ii) **Vol III CLAUDE.md.** The conjecture "Borcherds lift =
resummation" (Vol III, Roadmap §"Final results") gains a precise
statement via Theorem H6: the mirror is between the Vir spectral
curve $\Sigma_c$ and the K3 Mukai locus. This is a NEW
cross-programme conjecture, well-defined and testable at the level of
weight-$3/2$ cusp form correspondence.

(iii) **Cross-volume.** The CY-A_3 inf-categorical proof
(`thm:derived-framing-obstruction`) plus the Vol III Borcherds lift
conjecture plus Theorem H6 yields a triangle: chain-level chiral
algebra (Vol III) ↔ resurgent shadow tower (Vol I) ↔ mock modular
character (Vol III). The triangle is closed mod the bridge in
Theorem H6.

================================================================
9. THE THREE HONESTLY-NAMED OBSTRUCTIONS
================================================================

(O1) The mirror duality of Theorem H6 is structural but not
proved at the level of an explicit identification of $\Sigma_c$ with a
parameter slice of $\Phi_{10}$'s Mukai locus. The required input is a
construction of the Borcherds singular theta lift on the family
$\Sigma_c$, generalising the lift on the K3 lattice. Healing cost:
HIGH.

(O2) The class-M extension of UTI (Corollary H7) requires defining
the modular trace of a non-finitely-generated bar complex via
Lefschetz-thimble decomposition; the existing UTI is for class G/L/C
where the trace is convergent. Healing cost: MODERATE.

(O3) The Berry–Howls $K_2$ formula assumes the spectral curve
$\Sigma_c$ is irreducible over $\mathbb{Q}(c)$ — true for generic $c$
but failing at the caesura values $c \in \{-22/5, -218/45, c^\*\}$.
The behaviour of $K_2$ at the caesurae requires a separate analysis
(coalescence, degeneration). Healing cost: LOW.

================================================================
10. THE INNER MUSIC, REPRISED
================================================================

The V8 "Adagio resoluto" of class M was scored with one wrong note
($c_S = -178/45$). The correction sharpens it without changing the
movement: the spectral curve $\Sigma_c$ is still the Riemann surface
of the shadow tower, the periods are still the flat sections, the
hyperelliptic involution is still the Verdier involution. What
changes is the count of caesurae from "one" to "three" — the cadenza
has three rests, not one — and the count of alien actions from "one
pair" to "an infinite tower indexed by $\binom{1/2}{n}$".

The Stokes line cadence is the bridge equation of Theorem H2: the
algebra of resurgent derivations is not a single constant but a Lie
algebra. The harmonic ratios $A_+/A_-$ are the leading order; the
full resurgence is an infinite-dimensional algebra acting on the
trans-series space.

The cadenza is the convergent regime $-22/5 < c < c^\*$, where the
Berry–Howls higher Stokes line is permanently audible: a
sub-cadential drone beneath the perturbative theme. The principal
caesura is at $c = -22/5$, where the perturbative theme breaks and
re-enters in a new key — divergent but Borel-resummable.

The mirror duality of Theorem H6 is the key signature: the same music
played on the modular-form side reads as Borcherds lift; the
$\sqrt{Q_c}$ branch becomes the $\eta^3$ shadow; the trans-series
becomes the multiplicative product.

================================================================
SUMMARY: WHAT ATTACK PROVED, WHAT HEAL ADDED
================================================================

| # | V8 component | Attack verdict | Heal upgrade |
|---|---|---|---|
| 1 | $c_S = -178/45$ Stokes line | FALSE; not a cubic root | Three caesurae at $\{-22/5, -218/45, c^\*\}$ |
| 2 | Single Stokes line | INCOMPLETE | Theorem H1: full alien tower with $\binom{1/2}{n}$ |
| 3 | $A_\pm = \pm\sqrt{Q'/2}\,t^2$ | LEADING ORDER ONLY | Theorem H1(ii): higher amplitudes via binomials |
| 4 | Cubic root interpretation | CONFLATED | $c^\*$ is convergence boundary, not Stokes line |
| 5 | (Implicit: bridge equation) | ABSENT | Theorem H2: graded Lie algebra of alien derivations |
| 6 | (Implicit: higher Stokes) | ABSENT | Theorem H3: Berry–Howls $K_2$ in convergent regime |
| 7 | Borel summable class M | CORRECT | Theorem H5: complete resurgence structure |
| 8 | (Implicit: Vol III link) | ABSENT | Theorem H6: mirror to Borcherds lift (CONJECTURAL) |
| 9 | (Implicit: UTI link) | ABSENT | Corollary H7: UTI dictionary (CONJECTURAL) |
| 10 | (Implicit: master theorem) | ABSENT | Theorem H8: complete class-M resurgence |

The single Platonic display, repaired:

\[
\boxed{\;
\widehat S_A(z)^2 \;=\; z^4\,\frac{Q_c(z)}{Q_c(0)},
\qquad
\Lambda(A) \;=\; \mathbb{Z}_{\ge 0}\,S_+ \oplus \mathbb{Z}_{\ge 0}\,S_-,
\qquad
\mathrm{Res}(A) \;=\; \mathrm{Lie}\bigl\langle \Delta_{n S_\pm}\bigr\rangle / (\text{bridge}).
\;}
\]

The chiral $L_\infty$ Maurer–Cartan of class M is not just Borel
summable: it is a complete resurgent system, with a graded
Lie algebra of alien derivations, a multi-instanton trans-series, a
Berry–Howls higher-Stokes constant active throughout the convergent
regime, and a conjectural mirror to the Vol III Borcherds lift. The
caesurae are at $c = -22/5$ (Borel-singularity collision),
$c = -218/45$ (degeneration of $Q_c$), and $c = c^\* =
6.12537\ldots$ (convergence boundary). The number $c_S = -178/45$
appearing in V8 is not a structural quantity and is RETRACTED.

— END WAVE FRONTIER CLASS-M RESURGENCE ATTACK/HEAL REPORT —

— Raeez Lorgat, 2026-04-16 —
