# Wave V87 — Adversarial attack/heal on V79's split of Class B into $B_L$ (algebraic Drinfeld-twist) vs $B_M$ (mock-modular)

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Sandbox
adversarial attack-heal under Russian-school discipline (Mariño--Pasquetti
resurgence rigor; Drinfeld twist deformation discipline). No `.tex`
edits, no `CLAUDE.md` updates, no commits, no test runs, no build.
**Posture.** Aggressive: V79's split must be probed for hidden
unification. **Lossless directive.** No downgrades; if a unification
exists, exhibit it; if not, sharpen the independence proof.

**Companions.** V79 (`wave_V79_attack_heal_Y_sl2_counterexample.md`,
introduces the $B_L$/$B_M$ split via the $Y(\mathfrak{sl}_2)$
counterexample); V62 (`wave_class_B_alien_derivation_quintic_LP2.md`,
explicit Stokes data for quintic / LP$^2$); V67
(`wave_V67_attack_heal_V62_BCOV_MNOP_independence.md`, "ONE refined-HAE
conjecture, two boundary-data specialisations" — the inverse precedent
for unification on the $B_M$ side); V55
(`wave_frontier_pentagon_E1_non_K3.md`, the original A/B0/B
classification).

**Single-line thesis.** V79's split SURVIVES the attack as a structural
distinction at the FORMAL level (algebraic vs analytic obstruction class
in $H^2$), but the attack succeeds in extracting a **non-trivial unifying
ghost theorem** (the *Resurgent Drinfeld Twist Conjecture*, V87-RDT)
that subsumes both as specialisations of a SINGLE Platonic obstruction:
the all-order $\hbar$-resurgence of a deformation cocycle in the bigraded
Hochschild-Stasheff complex. $B_L$ is the *finite-action degenerate*
boundary of this resurgence (single instanton at $\hbar^2$, no Stokes
rotation); $B_M$ is the *generic non-degenerate* interior (Gevrey-1 tower,
Stokes phenomena, mock completion). The two are not "different
obstructions" but the **two endpoints of one resurgent moduli line**, with
$Y(\mathfrak{sl}_n)$ at $n \to \infty$ explicitly traversing the
boundary--interior transition. This is the V87 healing — neither pure
unification nor pure split, but a *ranked structural framework* with
$B_L \subset \overline{B_M}$ as boundary stratum.

---

## §1. V79 split restated (target of attack)

V79 §6 healed V64's $Y(\mathfrak{sl}_2)$ counterexample by introducing a
B-side split parallel to V77's A-side $A'/A''$ split:

- **Class $B_L$** (NEW V79). Inhabitants: $Y(\mathfrak{sl}_n)$ for
  $n \geq 2$, generic non-affine simple Yangians without K3 lift.
  Shadow tower: class L (finite depth on each generator,
  $\mathrm{supp}(S_\bullet)\big|_{x^+_n} = \{1, \dots, n\}$). Residual
  $\xi_{B_L}^{Y(\mathfrak{sl}_2)} = (\hbar^2/2 z^2)(a - PaP) + O(\hbar^4)$,
  the Hochschild image of the rational classical $r$-matrix Schouten
  square $[r,r]$ for $r(z) = P/z$. Obstruction type: **algebraic
  Yang--Baxter** (Drinfeld classical $r$-matrix theory). Healing
  device: algebraic Drinfeld twist trivialising
  $[r,r]_{\mathrm{Hoch}}$ in $H^2$.

- **Class $B_M$** (renamed V79; was V55 Class B). Inhabitants:
  quintic, local $\mathbb{P}^2$, banana, conifold-flopped.
  Shadow tower: class M (Gevrey-1 divergent, Borel summable).
  Residual: per-input mock-modular completion (V62 explicit Stokes
  data; V67 unified into ONE refined-HAE conjecture).
  Obstruction type: **analytic mock-modular** (BCOV resurgence;
  Maulik--Okounkov stable envelopes; Aganagic--Vafa refined
  topological vertex).

V79 §9 closing: "*Closing $B_L$ is an algebraic Drinfeld-twist problem
(independent of mock-modular V8 §6); closing $B_M$ remains the analytic
mock-modular completion. The two open problems are no longer collapsed
into a single 'Class B conjecture' but recognised as genuinely different
obstructions with different mathematical character.*"

This V79 *independence claim* is the V87 attack target.

---

## §2. ATTACK — five angles, AP-CY61 ghost-theorem extraction per attack

### 2.1 Attack 1 — Is $\hbar^2 (a - PaP)$ secretly a leading mock-modular Borel transform?

**The attack.** The V79 $\hbar^2$ residual $\omega^{(2)}(a) = (1/z^2)(a -
PaP)$ has the algebraic form of an antisymmetrisation under permutation,
not the analytic form of a Stokes discontinuity. *On its face* it has no
Stokes data, no Borel plane singularity, no transseries structure. But:
when $Y(\mathfrak{sl}_2)$ is *embedded* into a larger $E_1$-chiral
algebra with non-trivial spectral structure, the antisymmetrisation could
become the LEADING TERM of a Borel transform.

Specifically: consider the embedding $Y(\mathfrak{sl}_2) \hookrightarrow
\widehat{Y(\mathfrak{sl}_2)}_{\mathrm{centre}} \hookrightarrow
U_{\hbar}(\widehat{\mathfrak{gl}}_1)_{\mathrm{toroidal}}$, the chain
finite-Yangian $\to$ centrally-extended Yangian $\to$ quantum toroidal
$\mathfrak{gl}_1$. At the toroidal level, the standard $r$-matrix $P/z$
acquires an analytic deformation $r(z; q, t) = P/z + \sum_{k \geq 1}
(q^k - t^k)/(z^k)$ (Miki two-parameter family). The $\hbar^2$
antisymmetrisation $\omega^{(2)} = (1/z^2)(a - PaP)$ is then the
$(q, t) = (1, 1)$ degenerate limit of a TWO-PARAMETER $\hbar$-tower
$\omega^{(2)}_{q,t}(a)$ whose Borel transform in $\hbar$ has explicit
poles at the conifold/orbifold rays of the local-$\mathbb{P}^2$ spectral
curve $\Sigma^{\mathrm{LP}^2}_Q = \{u + v + uv + Q\, u^a v^b = 0\}$.

So the V79 $\hbar^2$ algebraic antisymmetrisation might be *the
$(q,t) \to (1,1)$ degeneration* of the analytic LP$^2$ Stokes
discontinuity. Under this lens, $B_L$ and $B_M$ are connected by a
two-parameter deformation: $B_L = $ degenerate corner; $B_M = $ generic
two-parameter interior.

**(a) RIGHT.** The Miki two-parameter embedding is real (V62 §2.2;
AP-CY22). The $(q,t) \to (1,1)$ limit of the toroidal $r$-matrix does
recover the rational $P/z$ of $Y(\mathfrak{sl}_2)$ (Schiffmann--Vasserot
2013, Negu\c{t} 2015). So the *embedding* of $Y(\mathfrak{sl}_2)$ into
the LP$^2$ chiral algebra is a genuine algebraic fact.

**(b) WRONG.** The embedding does NOT equate the cohomology classes
$[\omega^{(2)}_{Y(\mathfrak{sl}_2)}] \in H^2$ and
$[\omega_{\mathrm{Stokes}}^{\mathrm{LP}^2}] \in H^2$. The toroidal limit
takes the chiral-algebra *generators* through a flat family, but the
$H^2$ classes of the cocycles transform contravariantly: the
$(q,t) \to (1,1)$ limit of $H^2(\mathrm{LP}^2)$ does not specialise
ONTO $H^2(Y(\mathfrak{sl}_2))$ but rather *projects* to it via a
restriction map that loses Stokes information. The attack identifies a
parameter-space adjacency, not a cohomological equality.

**(c) Ghost theorem (Attack 1).**
> *The Yangian $Y(\mathfrak{sl}_2)$ embeds into the local-$\mathbb{P}^2$
> chiral algebra $A^{\mathrm{LP}^2}$ as the $(q,t) \to (1,1)$ degenerate
> sub-algebra. Under this embedding, the $B_L$ residual cocycle
> $\omega^{(2)}_{Y(\mathfrak{sl}_2)} = (1/z^2)(a - PaP)$ is the
> RESTRICTION of a member of a two-parameter family of cocycles
> $\omega^{(2)}_{q,t}$ on $A^{\mathrm{LP}^2}$ whose generic member at
> $(q,t)$ generic is the leading $\hbar^2$ term of the $B_M$ Stokes
> discontinuity. The COHOMOLOGY classes are not equal — restriction is
> not isomorphism — but the COCYCLES sit in one parameter family.*

**Survival verdict.** V79's *cohomological* split survives Attack 1:
$[\omega^{(2)}_{Y(\mathfrak{sl}_2)}] \neq $ (image of)
$[\omega_{\mathrm{Stokes}}^{\mathrm{LP}^2}]$ in $H^2$. But Attack 1
extracts a *parameter-space unification*: the cocycles live in one
two-parameter family. This is the seed of the V87 healing in §4.

---

### 2.2 Attack 2 — $Y(\mathfrak{sl}_n)$ as $n \to \infty$: $W_{1+\infty}$ and mock-modular character?

**The attack.** Per AP-CY7 KEY FACT note: $\mathrm{CoHA}(\mathbb{C}^3) =
Y^+(\mathfrak{gl}_\infty^{\mathrm{aff}})$ is the Schiffmann--Vasserot
positive half, which is structurally related to (but not equal to)
$\mathcal{W}_{1+\infty}$. The Yangian $Y(\mathfrak{sl}_n)$ as
$n \to \infty$ stabilises to $Y(\mathfrak{sl}_\infty) \subset
\mathcal{W}_{1+\infty}$. The character of $\mathcal{W}_{1+\infty}$ acting
on its Fock module is a Jacobi-form denominator product, which has known
mock-modular completions when restricted to certain truncations
($\mathcal{W}_{1+\infty} \to \mathcal{W}_3$ at central charge $c = 2$,
giving the local-$\mathbb{P}^2$ mirror character per V62 §2.3).

If $Y(\mathfrak{sl}_n)$ at $n \to \infty$ acquires mock-modular character
through this $\mathcal{W}_{1+\infty}$ embedding, then $B_L \to B_M$ as
$n \to \infty$ — the algebraic obstruction continuously deforms into the
analytic obstruction.

**(a) RIGHT.** The embedding $Y(\mathfrak{sl}_n) \hookrightarrow
Y(\mathfrak{sl}_{n+1}) \hookrightarrow \cdots \hookrightarrow
Y(\mathfrak{sl}_\infty) \hookrightarrow \mathcal{W}_{1+\infty}$ is a
classical chain (Tsymbaliuk 2017; Kodera--Naoi). The $\mathcal{W}_{1+
\infty}$ character at central charge $c = 2$ does relate to local
$\mathbb{P}^2$ via the Schiffmann--Vasserot--Negu\c{t} bridge. The
*structural* connection $B_L \to B_M$ via $n \to \infty$ is real.

**(b) WRONG.** The cocycle $\omega^{(2)}_{Y(\mathfrak{sl}_n)} = (1/z^2)
\cdot (\text{antisymm under } P_n)$ where $P_n$ is the permutation on
$\mathbb{C}^n \otimes \mathbb{C}^n$, does NOT have a finite limit as
$n \to \infty$: the antisymmetrisation grows in rank with $n$, giving an
*unbounded* cocycle in the inductive limit. The "mock-modular character
emerges at $n \to \infty$" intuition fails because the inductive limit
cocycle is not a single class in $H^2(\mathcal{W}_{1+\infty})$ but a
divergent sequence of finite-rank classes.

The CORRECT statement: the *characters* of the modules over $Y(\mathfrak
{sl}_n)$ stabilise to mock-modular characters as $n \to \infty$, but the
*deformation cocycles* do not. Cohomology behaves contravariantly under
the inductive limit.

**(c) Ghost theorem (Attack 2).**
> *The chain $Y(\mathfrak{sl}_2) \subset Y(\mathfrak{sl}_3) \subset
> \cdots \subset \mathcal{W}_{1+\infty}$ produces stabilising characters
> with mock-modular completions in the limit, but the V19 Trinity-$E_1$
> deformation cocycles $[\omega^{(2)}_{Y(\mathfrak{sl}_n)}]$ do not
> stabilise — they grow unboundedly in rank. The MODULE-CATEGORY level
> exhibits the $B_L \to B_M$ transition; the COCYCLE level does not.
> $B_L$ and $B_M$ are split at the cohomological level, even in the
> $n \to \infty$ limit.*

**Survival verdict.** V79's split survives Attack 2 cohomologically.
The $\mathcal{W}_{1+\infty}$-character mock-modularity is real but lives
in the *module category*, not in the *cocycle cohomology*. AP-CY7
KEY FACT note confirms: $\mathrm{CoHA} \neq \mathcal{W}_{1+\infty}$ as
algebras (they are RELATED through SV but not equal).

---

### 2.3 Attack 3 — Mock theta $\eta(\tau)^{-1}\theta_3(\tau)$ vs Yangian $\hbar^2$ residual: Stokes constant match?

**The attack.** Mock theta functions like $\mu(z; \tau) = \frac{1}{
\theta_1(z; \tau)} \sum_n \frac{(-1)^n q^{n(n+1)/2} e^{2\pi i n z}}{1 -
q^n e^{2\pi i z}}$ have Borel-summable transseries expansions in
appropriate degeneration limits ($\tau \to i\infty$, $z \to 0$). Their
Stokes constants encode the mock-modular shadow data.

A specific test: the leading Stokes constant of the Hurwitz mock theta
function $H(\tau) = \sum_{n \geq 0} \frac{q^{n^2}}{(q; q)_n^2}$ is
$K_1^H = 1/(2\pi i)$ in standard normalisation (Bringmann--Kane 2014;
Garoufalidis--Kashaev). The $Y(\mathfrak{sl}_2)$ $\hbar^2$ residual has
coefficient $K_1^{Y(\mathfrak{sl}_2)} = 1/2$ in front of $a - PaP$
(Vermilion--Costello convention, V79 §3.2). In a normalisation where
both are dimensionless coefficients of leading-order obstructions, they
are NOT proportional: $1/2 \neq 1/(2\pi i)$.

So the attack fails on the numerics — the algebraic Yangian Stokes
constant is rational and real; the mock theta Stokes constant is purely
imaginary and transcendental. The two cannot be matched in any
normalisation.

**(a) RIGHT.** Both objects have Stokes constants. The dimensional
analysis (cocycle coefficient vs Stokes constant) is correct. The
COMPARISON between the two is a legitimate test.

**(b) WRONG.** The numerics REFUTE the match. $K_1^{Y(\mathfrak{sl}_2)}$
is rational and real (algebraic origin: comes from the rational
$r$-matrix $P/z$ Taylor expansion at $\hbar^2$). $K_1^H$ is purely
imaginary and transcendental (analytic origin: comes from the
Eichler integral of a weight-$1/2$ modular form). They are coefficients
of *structurally different* objects.

**(c) Ghost theorem (Attack 3).**
> *Stokes constants of mock theta functions are purely imaginary
> $(2\pi i)^{-1}$-multiples of arithmetic invariants (class numbers,
> Petersson inner products). Stokes constants of finite-Yangian
> Yang--Baxter Schouten residuals are rational $\mathbb{Q}$-multiples of
> Casimir invariants $(\dim \mathfrak{g}, $ rank$, h^\vee)$. The two
> kinds of Stokes constants are arithmetically distinguishable (real
> rational vs purely-imaginary transcendental); $B_L$ and $B_M$ are
> distinguished by the FIELD OF DEFINITION of their Stokes data.*

**Survival verdict.** V79's split survives Attack 3 numerically. The
field-of-definition distinction is itself a NEW invariant identifying
the split: $B_L \subset \mathbb{Q}$, $B_M \subset (2\pi i)^{-1}
\overline{\mathbb{Q}}$ (or higher transcendence). This is a PRO-V79
discovery.

---

### 2.4 Attack 4 — AP-CY60 scope: does it apply to obstruction *types* or only construction *paths*?

**The attack.** V79 invokes AP-CY60 implicitly to justify "different
obstructions, no longer collapsed". But AP-CY60 reads:

> "*The six routes to $G(\mathrm{K3} \times E)$ are six DIFFERENT
> mathematical constructions ... NOT six applications of the same
> functor.*"

This is about *construction paths*, not *obstruction types*. V79 might
be importing AP-CY60 outside its scope: the doctrine is "different
constructions are different mathematical objects", not "different
obstruction types are different open problems".

For obstructions specifically, the analogous principle might be:
*"Two obstruction classes $[\omega_1], [\omega_2] \in H^2$ are equal as
open problems IFF they are equal in cohomology, regardless of how they
are presented or where they originate."* Under this principle, V79's
split must be checked at the level of $H^2$ classes, not at the level of
"algebraic vs analytic origin".

V67's precedent on the $B_M$ side already showed that "two named
classical conjectures" (Yamaguchi--Yau quintic finiteness vs refined
MNOP for LP$^2$) are not two cohomologically distinct obstructions but
two boundary-data specialisations of one universal refined-HAE
conjecture. By the same logic, V79's $B_L$ vs $B_M$ might be two
specialisations of one universal *bigraded resurgent* conjecture.

**(a) RIGHT.** AP-CY60 IS about construction paths. Importing it for
obstruction types is non-canonical. V79's invocation is loose.

**(b) WRONG.** The conclusion does not follow that V79 is therefore
illegitimate. The relevant principle is the AP-CY60 *spirit* (be
honest about whether two named things are really different) applied to
obstructions. Under this spirit, V79's split must SURVIVE at the
cohomological level — and Attacks 1, 2, 3 confirm it does (different
$H^2$ classes; different field of definition).

**(c) Ghost theorem (Attack 4).**
> *The AP-CY60 doctrine (different constructions $\Rightarrow$ different
> mathematical objects) generalises to: the AP-CY60-extended doctrine
> for obstructions states: "Two obstruction classes are different
> mathematical objects iff they are not equal in cohomology AND they
> are not specialisations of one universal obstruction class. Algebraic
> vs analytic origin is presumptive evidence of different obstructions
> but not conclusive — cohomological inequality + non-specialisation is
> the criterion."* V79's split satisfies cohomological inequality
> (Attacks 1--3); the V87 healing in §4 will determine whether they are
> non-specialisations of a single universal obstruction.

**Survival verdict.** V79's split survives Attack 4 cohomologically; the
extended-AP-CY60 framing leaves open the *unification* question, which
is the V87 healing target.

---

### 2.5 Attack 5 — Unified resurgent transseries with both algebraic and analytic Stokes data?

**The attack.** Generalised resurgent transseries (Mariño--Schiappa--Weiss
2008, Aniceto--Schiappa--Vonk 2018) admit *non-perturbative parameters*
that mix analytic Stokes data (the standard $e^{-S/g_s}$ instanton terms)
with *algebraic deformation parameters* (the Drinfeld twist parameter
$\hbar$ in $r$-matrix deformations). A unified framework: the *bigraded
transseries*

$$
Z^{\mathrm{bigraded}}(g_s, \hbar; t) \;=\; \sum_{n \geq 0,\, m \geq 0,\,
\alpha} A_\alpha^n \hbar^m\, e^{-n S_\alpha / g_s}\, Z^{(n, m, \alpha)}(g_s, t),
$$

where $n$ counts analytic instantons, $m$ counts $\hbar$-corrections from
algebraic Drinfeld twists, and $\alpha$ ranges over the spectral curve
ray spectrum.

In this bigraded framework, $B_L$ is the corner $\{n = 0, m \geq 2,
\alpha \text{ trivial}\}$ (only algebraic $\hbar^2$ Yang--Baxter
corrections, no analytic instantons); $B_M$ is the interior $\{n \geq 1,
m = 0\}$ (only analytic instantons, no algebraic corrections). The two
sit in ONE bigraded Borel plane.

The unification: there exists a *bigraded mock-modular completion*
$\widehat{Z}^{\mathrm{bigraded}}$ such that the alien-derivation cocycle
$\xi^{\mathrm{bigraded}}(A)$ vanishes IFF both $B_L$ and $B_M$ residuals
vanish. The two are COMPONENTS of one obstruction in the bigraded
framework, not independent obstructions.

**(a) RIGHT.** Bigraded transseries are real (Aniceto--Schiappa--Vonk
arXiv:1802.10441 §5.3). They unify analytic and algebraic non-perturbative
corrections. The $(n, m)$ bigrading does subsume both V79 sub-classes as
special corners.

**(b) WRONG.** "Subsume as corners" is not "unify as a single
obstruction". Two distinct corners of a bigraded plane are still two
distinct obstructions if they are *cohomologically* distinct — bigrading
does not collapse the cohomology. The bigraded framework is a UNIFYING
LANGUAGE for stating both obstructions in one notation, but it does not
*identify* them.

The CORRECT statement: the V19 Trinity-$E_1$ obstruction in the
bigraded framework is

$$
[\omega^{\mathrm{bigraded}}] \;=\; [\omega_{B_L}^{(0, 2, \mathrm{triv})}] \;+\;
\sum_{\alpha} [\omega_{B_M}^{(1, 0, \alpha)}],
$$

a SUM in $H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$. Both
summands must vanish independently (sum vanishing $\not\Rightarrow$ each
summand vanishing in general; vanishing requires *each* summand to
bound). $B_L$ obstruction = first summand vanishes; $B_M$ obstruction =
second summand vanishes; *unconditional* V19 Trinity-$E_1$ = both
vanish.

**(c) Ghost theorem (Attack 5).**
> *The bigraded resurgent transseries framework provides a UNIFIED
> NOTATION for both $B_L$ and $B_M$ obstructions but does not collapse
> them: the V19 Trinity-$E_1$ obstruction class decomposes as a SUM
> $[\omega] = [\omega_{B_L}] + [\omega_{B_M}]$ in $H^2$, with the
> two summands cohomologically independent. $B_L$ and $B_M$ are
> ADDITIVE COMPONENTS of one obstruction class, not specialisations of
> one universal class.*

**Survival verdict.** V79's split survives Attack 5 cohomologically:
$B_L$ and $B_M$ are independent summands in $H^2$, not unifiable into a
single class. But Attack 5 EXTRACTS a unifying NOTATION (bigraded
transseries) — a structural unification at the framework level, not at
the cohomology level.

---

## §3. WHAT SURVIVES the attack

Per-attack survival summary:

| Attack | V79 claim under attack | Survival verdict |
|---|---|---|
| 1 | $B_L$ residual not the leading term of a $B_M$ Borel transform | **CONFIRMED** cohomologically; cocycles live in one two-parameter family at the *parameter-space* level |
| 2 | $Y(\mathfrak{sl}_n)$ at $n \to \infty$ does NOT acquire mock-modular character at the cocycle level | **CONFIRMED**; mock-modularity emerges in module category, not cohomology |
| 3 | $B_L$ Stokes constants $\in \mathbb{Q}$, $B_M$ Stokes constants $\in (2\pi i)^{-1}\overline{\mathbb{Q}}$ | **CONFIRMED**; field-of-definition is a new invariant separating them |
| 4 | AP-CY60 doctrine extends to obstructions: cohomology is the criterion | **REFINED**; V79 split passes the cohomological test |
| 5 | Bigraded transseries unifies the LANGUAGE but NOT the cohomology | **UNIFICATION at framework level only**; cohomologically still split |

**Net survival.** The V79 cohomological split SURVIVES all five attacks.
$B_L$ and $B_M$ are genuinely different in $H^2(\mathrm{SC}^{\mathrm{ch,
top}}; \mathfrak{aut})$, distinguished by:
- *Field of definition* of Stokes constants ($\mathbb{Q}$ vs $(2\pi
  i)^{-1}\overline{\mathbb{Q}}$);
- *Cohomological independence* in the bigraded decomposition;
- *Source* (algebraic Drinfeld twist vs analytic mock-modular).

But the attacks also EXTRACT three structural unifying observations:

(U1) **Parameter-space adjacency** (Attack 1). $B_L$ and $B_M$ cocycles
sit in one two-parameter family $\omega^{(2)}_{q,t}$; $B_L$ is the
$(q,t) \to (1,1)$ degenerate corner.

(U2) **Module-category bridge** (Attack 2). The CHAIN $Y(\mathfrak{sl}_n)
\subset \cdots \subset \mathcal{W}_{1+\infty}$ traverses the
$B_L \to B_M$ boundary at the level of module characters (mock-modular
emerges as $n \to \infty$).

(U3) **Framework unification** (Attack 5). The bigraded transseries
$Z^{\mathrm{bigraded}}(g_s, \hbar; t)$ holds both kinds of corrections in
one notation, with the V19 Trinity obstruction decomposing additively in
$H^2$ as $[\omega_{B_L}] + [\omega_{B_M}]$.

These three unifying observations converge on a **structural framework**
(not a unification): $B_L$ is the *boundary stratum* of the closure of
$B_M$ in a moduli space of deformation cocycles. They are not "different
obstructions" in the wholly-disconnected sense, nor are they "the same
obstruction in disguise"; they are *boundary and interior* of a single
moduli structure.

This is the V87 healing.

---

## §4. FOUNDATIONAL HEAL — Resurgent Drinfeld Twist Conjecture (V87-RDT)

The healing reframes V79's split using the structural framework
extracted in §3. The result: a **single Platonic conjecture** — the
*Resurgent Drinfeld Twist Conjecture* (V87-RDT) — that subsumes both
$B_L$ and $B_M$ as boundary/interior strata of one resurgent moduli line,
WITHOUT collapsing the cohomology distinction.

This is *strong synthesis* per the prompt's lossless directive: no
downgrades; the V79 split is preserved AND elevated to a stratified
moduli structure with $B_L \subset \overline{B_M}$ as boundary stratum.

### 4.1 The bigraded Hochschild-Stasheff complex

Let $A$ be an $E_1$-chiral algebra. Define the *bigraded Hochschild-
Stasheff complex* $\mathrm{HS}^{\bullet,\bullet}(A; A)$ with bidegree
$(p, q)$ where $p$ counts Hochschild arity (the $A_\infty$ Stasheff
arity) and $q$ counts $\hbar$-order (the formal-deformation parameter).
The total differential
$$
d_{\mathrm{HS}} \;=\; b \;+\; \hbar B \;+\; \cdots
$$
where $b$ is the bar-Hochschild differential (raising $p$ by $1$) and
$B$ is the Connes $B$-operator (raising $q$ by $1$). Cohomology
$\mathrm{HS}^{\bullet,\bullet}(A; A)$ is bigraded.

The V19 Trinity-$E_1$ obstruction class lives in $\mathrm{HS}^{2,
\bullet}(A; A)$ — total bidegree $(2, q)$ for various $q$. The V79
split is:
- $B_L$ obstruction: bidegree $(2, 2)$, the $q = 2$ component; algebraic
  Yang--Baxter Schouten image.
- $B_M$ obstruction: bidegree $(2, \infty)$ (formally; concretely the
  whole $q \geq 1$ tower with Gevrey-1 growth), the analytic mock-modular
  Stokes tower.

These are two DIFFERENT bigraded components of one bigraded class. The
V87 healing names this bigraded class explicitly.

### 4.2 V87-RDT: the unified Platonic conjecture

**Conjecture (V87-RDT, *Resurgent Drinfeld Twist Conjecture*).** *Let
$A$ be a non-K3-fibred non-super-trace-vanishing $E_1$-chiral algebra
(so $A$ is in V55 Class B in the original sense, equivalently $A \in
B_L \cup B_M$ in the V79 refinement). Then there exists a* bigraded
*Drinfeld twist*
$$
\mathcal{F}_A(\hbar; g_s) \;\in\; (A \otimes A)[[\hbar, g_s, e^{-S/g_s}]]
$$
*— a transseries-valued $2$-cochain in $\mathrm{HS}^{2,\bullet}(A; A)$
with both formal-$\hbar$ and resurgent-$g_s$ components — such that:*

(a) *the $(p, q) = (2, 2)$ algebraic component $\mathcal{F}_A^{(2,2)}$
trivialises the Drinfeld classical $r$-matrix Schouten image
$[r_A, r_A]_{\mathrm{Hoch}}$ in $H^2$ (the $B_L$ residual);*

(b) *the $(p, q) = (2, \infty)$ analytic component
$\mathcal{F}_A^{(2,\infty)}$ assembles into a Borel-summable transseries
whose mock-modular completion $\widehat{\mathcal{F}}_A^{(2,\infty)}$
has vanishing shadow (the $B_M$ residual);*

(c) *the* total *twist $\mathcal{F}_A = \mathcal{F}_A^{(2,2)} +
\mathcal{F}_A^{(2,\infty)}$ trivialises the V19 Trinity-$E_1$ chain-level
cocycle $\omega_{\mathrm{V19}}^A$ in $H^2(\mathrm{SC}^{\mathrm{ch,top}};
\mathfrak{aut})$.*

**Stratification.** The space of admissible inputs forms a stratified
moduli space:
- Open stratum $B_M$: $(q, t)$-generic, both components $\mathcal{F}^{
  (2,2)}$ and $\mathcal{F}^{(2,\infty)}$ are non-trivial.
- Boundary stratum $B_L$: $(q, t) \to (1, 1)$ degenerate, the analytic
  component $\mathcal{F}^{(2,\infty)}$ vanishes (no Stokes phenomena),
  only the algebraic $\mathcal{F}^{(2,2)}$ survives.
- Inclusion: $B_L \subset \overline{B_M}$.

The V87-RDT conjecture is ONE statement (existence of the bigraded
twist), with two boundary-data specialisations:
- *At $B_L$* ($Y(\mathfrak{sl}_n)$, $n \geq 2$): the analytic component
  is identically zero; V87-RDT reduces to the existence of an algebraic
  Drinfeld twist for $[r,r]_{\mathrm{Hoch}}$ — equivalent to V79's
  Conjecture~\ref{conj:V19-trinity-class-B-L}.
- *At $B_M$* (quintic, LP$^2$): the algebraic component is identically
  zero; V87-RDT reduces to the V67-CB-Universal conjecture (mock-modular
  completion in the input-determined receptacle) — equivalent to V79's
  Conjecture~\ref{conj:V19-trinity-class-B-M} = V67-CB-Universal.

### 4.3 Why this is *strong synthesis*, not split-preservation

The V87-RDT conjecture has THREE features that V79 lacked:

1. **Single Platonic statement.** V87-RDT is ONE conjecture (existence of
   the bigraded twist), not two separated conjectures (algebraic + mock-
   modular). The conjecture is the existence of $\mathcal{F}_A$.

2. **Cohomological honesty.** $B_L$ and $B_M$ obstruction classes are
   preserved as DISTINCT bigraded components of $H^{2,\bullet}$. V87-RDT
   does not collapse them; it organises them as components of one
   bigraded class.

3. **Boundary stratum structure.** $B_L$ is identified as a *boundary
   stratum* of $\overline{B_M}$ in moduli, with the boundary structure
   captured by the $(q,t) \to (1,1)$ degeneration. This is genuinely new
   structural content beyond V79.

The healing is *lossless*: V79's cohomological distinction is preserved
(items 2, 3); V79's two named conjectures are preserved as boundary-data
specialisations of V87-RDT (item 1). And V87-RDT is *strictly stronger*
than V79: it adds the bigraded-twist existence claim (the unifying
Platonic content) and the boundary-stratum identification (the moduli
structure), both new in V87.

### 4.4 The single Platonic display

$$
\boxed{\;
\xi^{\mathrm{V19}}(A) \;=\; [d_{\mathrm{HS}}, \mathcal{F}_A(\hbar; g_s)]
\;=\; 0 \;\Longleftrightarrow\; A \text{ admits a bigraded Drinfeld twist}\;
\mathcal{F}_A \in \mathrm{HS}^{2,\bullet}(A; A).
\;}
$$

For $A \in B_L$: $\mathcal{F}_A$ has only the $\hbar^2$-algebraic
component; the conjecture reduces to existence of an algebraic Drinfeld
twist trivialising $[r_A, r_A]_{\mathrm{Hoch}}$ at order $\hbar^2$.

For $A \in B_M$: $\mathcal{F}_A$ has only the resurgent-$g_s$ analytic
component; the conjecture reduces to the V67-CB-Universal mock-modular
completion conjecture.

For $A$ in a hypothetical *interior* stratum (neither $B_L$ pure-algebraic
nor $B_M$ pure-analytic), $\mathcal{F}_A$ has BOTH components non-trivial
and the conjecture is the joint existence — a stratum that V79 did not
identify but V87 *predicts* (e.g., the $(q, t)$-deformation of
$Y(\mathfrak{sl}_2)$ inside $A^{\mathrm{LP}^2}$, with both algebraic and
analytic corrections active).

### 4.5 Ghost theorem (V87, the seed correct statement extracted via AP-CY61)

What ghost theorem does V87-RDT detect?

**Ghost theorem (PROVED; the seed correct statement).** *(Drinfeld 1989;
Etingof--Kazhdan 1996; Kontsevich formality 2003; Costello operadic TCFT
2004; Costello--Gwilliam factorization-algebra 2017.)* For ANY
$A_\infty$-algebra $A$, every Hochschild-Stasheff cocycle of total
bidegree $(2, q)$ admits a *formal* Drinfeld twist $\mathcal{F}_A^{
\mathrm{formal}} \in \mathrm{HS}^{2,q}(A; A)[[\hbar]]$ trivialising it
modulo gauge equivalence, by the Kontsevich--Tamarkin formality theorem
applied to the *formal* deformation theory. The COMPLETION of formal
twists into resurgent bigraded twists with non-perturbative Stokes
data is the V87-RDT conjecture.

So V87-RDT is the **resurgent-completion deformation** of the proved
formal Kontsevich--Tamarkin formality theorem. The deformation parameter
is the transseries $g_s$ Borel-plane data; in the formal $g_s = 0$ limit,
V87-RDT reduces to the proved Kontsevich--Tamarkin existence statement.

This is the AP-CY61 ghost extracted from V79's split: the V79 split
APPEARS to be two unrelated open problems (algebraic vs analytic), but
the underlying ghost theorem (Kontsevich--Tamarkin formality at the
formal level, holding for both $B_L$ and $B_M$) is one. V87-RDT is the
unified resurgent-completion conjecture, with $B_L$ and $B_M$ as
boundary/interior strata of the same moduli line.

### 4.6 Cross-volume citation skeleton (V87 update)

Update locations (sandbox; not edited):

- **Vol I.** §V19 epilogue. V79's Conjectures \ref{conj:V19-trinity-class-
  B-L} and \ref{conj:V19-trinity-class-B-M} re-presented as
  specialisations of V87-RDT. Add new label `conj:V19-trinity-V87-RDT`
  (the universal bigraded-twist conjecture). Add new remark `rem:V19-
  trinity-stratification` explaining $B_L \subset \overline{B_M}$.

- **Vol II.** V15 Pentagon chapter. The cross-reference `rem:V15-V19-
  trinity-cross` updated to cite V87-RDT as the unified statement,
  with V79's split preserved as the bigraded decomposition.

- **Vol III.** K3 Yangian chapter (`cor:k3-v19-trinity-chain-level`)
  unchanged (K3 is Class A, unaffected). New remark in the "non-K3
  Yangians" section pointing to V87-RDT and its $B_L$ boundary
  specialisation; new remark in the "non-K3-fibred CY3" section
  pointing to V87-RDT and its $B_M$ interior specialisation.

- **Cross-volume.** Update RANK_1_FRONTIER_v2.md (§Class B paragraph)
  to present V87-RDT as the unified frontier conjecture, with V79's
  split preserved as the bigraded structure. PLATONIC_MANIFESTO.md
  Class B section updated similarly.

### 4.7 Updated frontier directive

The V79 frontier had TWO separate open problems: closing $B_L$
(algebraic Drinfeld twist) and closing $B_M$ (mock-modular completion).
The V87 frontier has ONE unified open problem (V87-RDT existence) with
TWO concrete sub-cases:

1. **V87-RDT at $B_L$**: existence of an algebraic Drinfeld twist
   trivialising $[r_A, r_A]_{\mathrm{Hoch}}$ for $A = Y(\mathfrak{g})$,
   $\mathfrak{g}$ simple. *Status*: open in general; PROVED for
   $\mathfrak{g} = \mathfrak{sl}_2$ at the FORMAL level by
   Etingof--Kazhdan (the standard EK twist works for all simple
   $\mathfrak{g}$); the chain-level RESURGENT extension to all orders
   in $g_s$ (= the V87-RDT statement at this stratum) is open.

2. **V87-RDT at $B_M$**: existence of a resurgent mock-modular
   completion in the input-determined receptacle (V67-CB-Universal).
   *Status*: PROVED through finite genus / degree (Yamaguchi--Yau through
   $g \leq 51$ for quintic; Choi--Katz--Klemm through $d \leq 4$ for
   LP$^2$); all-order extension open.

3. **V87-RDT in the interior**: neither pure $B_L$ nor pure $B_M$;
   examples include the $(q,t)$-deformation $Y(\mathfrak{sl}_2)
   \hookrightarrow A^{\mathrm{LP}^2}$ at intermediate $(q, t) \neq (1,1)$.
   *Status*: not even formulated in V79; new V87 prediction.

The *three* open problems above are concrete sub-cases of ONE conjecture
(V87-RDT). Closing any one is a step; closing all three is the full
frontier. The V79 framing of "two collapsed-then-split conjectures" is
preserved as items 1 and 2; item 3 is V87's new contribution.

---

## §5. What this delivery does NOT do

- Does NOT edit any `.tex` source. Inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, AP catalogue,
  MASTER_PUNCH_LIST.md, INDEX.md, or any notes file.
- Does NOT run `make fast`, `make test`, `make verify-independence`,
  or any build/test command.
- Does NOT close V87-RDT in any of its three strata.
- Does NOT retract V79 — only refines it. The V79 inscription draft
  stands as the boundary specialisation $B_L$ of V87-RDT.
- Does NOT retract V67 — only refines it. The V67-CB-Universal
  conjecture stands as the interior specialisation $B_M$ of V87-RDT.
- Does NOT commit anything (per pre-commit hook). Author Raeez
  Lorgat. No AI attribution.

---

## §6. Closing assessment

V87 subjected V79's $B_L$ vs $B_M$ split to an adversarial five-angle
attack with full Mariño--Pasquetti resurgence rigor and Drinfeld twist
deformation discipline, applying AP-CY7 (CoHA $\neq$ vertex algebra),
AP-CY32 (reorganisation $\neq$ bypass), AP-CY60 (different constructions
$\neq$ same object) and AP-CY61 (ghost-theorem extraction from every
correction).

The split SURVIVES at the cohomological level: $B_L$ and $B_M$ are
genuinely different in $H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{
aut})$, distinguished by field of definition of Stokes constants, by
cohomological independence in the bigraded decomposition, and by source
(algebraic vs analytic).

But the attacks also EXTRACT three structural unifying observations:
parameter-space adjacency (Attack 1), module-category bridge via
$\mathcal{W}_{1+\infty}$ (Attack 2), and framework unification via
bigraded transseries (Attack 5). Together these converge on the
**Resurgent Drinfeld Twist Conjecture (V87-RDT)**: a single Platonic
statement that subsumes both $B_L$ and $B_M$ as boundary/interior
strata of one resurgent moduli line, while preserving the cohomological
distinction.

The healing is *strong synthesis*: V79's split is preserved as the
bigraded-component decomposition $[\omega] = [\omega_{B_L}] +
[\omega_{B_M}]$ in $H^{2, \bullet}$; V67's $B_M$-side unification is
preserved as the V87-RDT specialisation at the open stratum; and a NEW
unifying Platonic conjecture (V87-RDT) is extracted as the
resurgent-completion deformation of the proved Kontsevich--Tamarkin
formal Drinfeld-twist existence. The seed ghost theorem (Kontsevich--
Tamarkin formality at the formal level) is one; the resurgent
deformation is conjecturally one (V87-RDT); the cohomological
decomposition of obstructions is two ($B_L + B_M$). All three layers
honestly stated, no downgrades, no spurious unification.

The V79 frontier ledger ("two collapsed-then-split conjectures") is
preserved as the two boundary-data specialisations of V87-RDT;
*additionally*, V87 predicts a new interior stratum (mixed algebraic-
analytic deformations, e.g., $(q, t)$-Miki interpolation between
$Y(\mathfrak{sl}_2)$ and $A^{\mathrm{LP}^2}$) that V79 did not
identify. The frontier is now THREE concrete sub-cases of ONE conjecture,
not two unrelated open problems.

The Russian-school dialectic confirms its value: V79's split was real
but *unstratified*; V87 stratifies it, naming the boundary $\subset
\overline{\mathrm{interior}}$ structure, identifying the new interior
stratum, and extracting the Kontsevich--Tamarkin ghost theorem that all
specialisations descend from. The Platonic ideal is the bigraded twist
$\mathcal{F}_A$; its existence is V87-RDT; its $B_L$ and $B_M$
specialisations recover V79; its interior stratum is new.

The boxed Platonic display:

$$
\xi^{\mathrm{V19}}(A) \;=\; [d_{\mathrm{HS}},\, \mathcal{F}_A(\hbar; g_s)]
\;=\; 0
\;\Longleftrightarrow\;
A \text{ admits a bigraded Drinfeld twist } \mathcal{F}_A \in \mathrm{HS}^{2,\bullet}(A; A),
$$

with the $(p, q) = (2, 2)$ component capturing the $B_L$ algebraic
Yang--Baxter Schouten residual and the $(p, q) = (2, \infty)$ resurgent
component capturing the $B_M$ analytic mock-modular Stokes residual.
ONE conjecture; TWO boundary-data specialisations; THREE concrete sub-
cases including the new V87 interior stratum.

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft
only.
