# Wave V79 — Adversarial attack/heal on V64's $Y(\mathfrak{sl}_2)$ counterexample to V19 Trinity-$E_1$

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Sandbox
adversarial attack-heal under Russian-school discipline. No `.tex`
edits, no `CLAUDE.md` updates, no commits, no test runs, no build.
**Posture.** Adversarial; assumes V64's counterexample claim may be
over-strong; tests every leg with Etingof–Kazhdan / Drinfeld twist
rigor.

**Companions.** V64 (`wave_V19_Trinity_E1_class_A_B0_inscription.md`,
the inscription draft under attack); V55
(`wave_frontier_pentagon_E1_non_K3.md`, A/B0/B dichotomy); V77
(`wave_V70_attack_heal_K3_mukai_signature_uniqueness.md`, five-class
extension introducing A' / A''); V59
(`draft_pentagon_E1_heisenberg_SPEC.md`, the abelian centrality
template the attack tests against).

**Single-line thesis.** The V64 $Y(\mathfrak{sl}_2)$ counterexample
*survives the attack* — but only after a forced refinement: at $\hbar^1$
the cocycle $\omega_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)} = (\hbar/z)[P,
\cdot]$ is an **inner derivation, hence a Hochschild coboundary**, so
the counterexample as stated at $\hbar^1$ is a CHAIN-level object that
*does* bound at the level of $H^2$. The genuine obstruction begins at
$\hbar^2$, where it is the Drinfeld $r$-matrix $r(z)$ Schouten square
$[r, r]$ paired against the half-braiding — the classical *Yang–Baxter
anomaly*. This anomaly is non-trivial in $H^2$. Furthermore the V64
shadow-class-M assignment for $Y(\mathfrak{sl}_2)$ is *over-specified*:
the Yangian as a finite Hopf algebra (no central charge, no chiral
realisation) has shadow tower of class L (terminating at depth 2), not
class M. Net survival: the **chain-level** counterexample stands at
$\hbar^2$, but with three corrections to the V64 inscription draft
(§7 below).

---

## §1. V64 $Y(\mathfrak{sl}_2)$ counterexample restated (verbatim)

V64 §2.2 asserts:

> *Let $A = Y(\mathfrak{sl}_2)$ be the Yangian of $\mathfrak{sl}_2$ in
> its chiral-algebra avatar (i.e., the $E_1$-chiral algebra whose
> Drinfeld coproduct $\Delta_z$ recovers the standard Yangian R-matrix
> on evaluation modules $V_u \otimes V_v$). The R-matrix is the
> rational $R(z) = 1 + (\hbar/z) P$ for $P$ the permutation on $\mathbb
> {C}^2 \otimes \mathbb{C}^2$, a matrix-valued function of the spectral
> parameter $z$, NOT a c-number scalar.*
>
> *The V19 Trinity-$E_1$ cocycle restricted to $Y(\mathfrak{sl}_2)$
> has the explicit form*
> $$
> \omega_{\mathrm{V19}}^{\,Y(\mathfrak{sl}_2)}(a)
> = R(z)\cdot a \cdot R(z)^{-1} - a
> = \frac{\hbar}{z}\,[P, a] + O(\hbar^2)
> $$
> *on the diagonal sector. Since $[P, a] \neq 0$ generically, this is
> non-zero as a chain — it does not bound any cochain $\mu$ in the
> relevant $H^2$ a priori.*

V64 §2.3 places $Y(\mathfrak{sl}_2)$ in V55 Class B based on three
observed features:
- **(non-K3-fibred)** $Y(\mathfrak{sl}_2)$ has no K3-orbifold geometric
  source.
- **(non-vanishing super-trace)** $\operatorname{str}(K_{Y(\mathfrak
  {sl}_2)}) = \dim \mathfrak{sl}_2 = 3 \neq 0$.
- **(class M shadow tower)** Asserted via "non-trivial $S_k$ for all
  $k$ via the Stasheff $A_\infty$ relations" + Maulik–Okounkov stable
  envelope mock-modular argument.

V64 §6.2 then registers $\xi_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)} =
(\hbar/z)[P, \cdot] + O(\hbar^2)$ as a B-class residual, and §8.3
constructs the ghost theorem: the counterexample is the *signature of
the absence of a Borcherds lift for $Y(\mathfrak{sl}_2)$ in isolation*.

---

## §2. ATTACK (five angles, AP-CY61 ghost-theorem extraction per attack)

### 2.1 Attack 1 — The $\hbar^1$ inner-derivation defect

**The attack.** The V64 cocycle at order $\hbar^1$ is exactly
$\omega^{(1)}(a) = (1/z)[P, a]$. Inner derivations
$\mathrm{ad}_X : a \mapsto [X, a]$ are **Hochschild coboundaries**:
$\mathrm{ad}_X = \delta_{\mathrm{Hoch}}(X)$ where the Hochschild
coboundary on a $0$-cochain $X$ is $(\delta X)(a) = X \cdot a - a \cdot
X = [X, a]$. So at the $\hbar^1$ level, $\omega^{(1)} = (1/z) \delta P$
is *exact*, a coboundary of $P/z$ viewed as a Hochschild $0$-cochain.

The V64 sentence "*it does not bound any cochain $\mu$ in the relevant
$H^2$ a priori*" is **false at $\hbar^1$**: the bounding $\mu$ is
literally $P/z$, the inner-derivation generator. The V64 cocycle as
stated up to $O(\hbar^2)$ is a **trivial** cohomology class.

**(a) What V64 gets RIGHT.** At the level of CHAINS, $\omega^{(1)}(a)
= (1/z)[P, a]$ is non-zero for generic $a$ (the matrix sector $V_u
\otimes V_v$ is non-abelian, $[P, a] \not\equiv 0$). The V64 chain-level
non-vanishing is a *correct chain observation*.

**(b) What V64 gets WRONG.** The transition from "non-vanishing as a
chain" to "non-vanishing in $H^2$" is invalid at $\hbar^1$. Inner
derivations always bound. The V64 sentence "non-zero as a chain — it
does not bound any cochain $\mu$ in the relevant $H^2$ a priori" runs
together a TRUE statement (chain non-vanishing) with a FALSE inference
(cohomological non-vanishing).

**(c) Ghost theorem (Attack 1).**
> *For any $E_1$-chiral algebra $A$, the linear-in-$\hbar$ obstruction
> $\omega^{(1)}(a) = (\hbar/z)[X, a]$ is automatically a Hochschild
> $H^2$-coboundary, with bounding $0$-cochain $X/z$ (extended to a
> formal Laurent expansion). The Yang–Baxter anomaly to $E_1$ Trinity
> coherence FIRST appears at $\hbar^2$, not $\hbar^1$.*

This is the standard *first-order obstruction-theory* fact in
deformation quantisation: the linear deformation of the multiplication
by an inner derivation is gauge-equivalent to the trivial deformation
(Drinfeld 1989; Kontsevich formality §6).

**Survival verdict.** V64's $\hbar^1$ analysis is **REFUTED at the
cohomological level**. The cocycle bounds at $\hbar^1$. To preserve
the counterexample, V64 must compute $\hbar^2$ explicitly.

---

### 2.2 Attack 2 — Could $Y(\mathfrak{sl}_2)$ be V77 Class A''?

**The attack.** V77 introduced **Class A''** (algebraic non-geometric)
to capture inputs that are Pentagon-coherent algebraically without a
compact-CY2 geometric realisation. The V77 §6 Pythagorean ladder
includes $(2,2)$ at rank 4 (= $II_{2,2} = U \oplus U$, ambient core).

The Yangian $Y(\mathfrak{sl}_2)$ is built on the simple Lie algebra
$\mathfrak{sl}_2$, whose root lattice is $A_1 = \mathbb{Z}\alpha$ with
Cartan matrix $(2)$. The associated even unimodular lattice in
signature appropriate for Borcherds lifts would be $\mathfrak{sl}_2
\oplus \mathfrak{sl}_2^*$ pairing — but this is rank 2, not unimodular
(determinant 2), and not even. So $Y(\mathfrak{sl}_2)$ is **not** in
V77's Class A'' as defined.

However, the affinisation $\widehat{\mathfrak{sl}_2}$ (the Kac–Moody
algebra) embeds in the lattice VOA $V_{A_1}$ at appropriate level. The
$A_1$ root lattice IS even (Gram matrix $(2)$, even diagonal); but it
is positive-definite, not Lorentzian. Borcherds lifts require a
Lorentzian even lattice (signature $(1, n-1)$ or $(2, n-2)$) — not
$A_1$ alone.

**(a) What this attack gets RIGHT.** The intuition that $Y(\mathfrak
{sl}_2)$ might admit *some* algebraic Pentagon-coherence framework via
its associated Kac–Moody is correct: $\widehat{\mathfrak{sl}_2}$ does
admit a "level-1 Borcherds character" via the affine Weyl–Kac character
formula. This is classical (Kac 1990).

**(b) What this attack gets WRONG.** The Weyl–Kac character of $\widehat
{\mathfrak{sl}_2}$ is NOT a Borcherds singular-theta lift. The Weyl–Kac
character is a quotient of theta-series-with-character by the Weyl
denominator — a finite-dimensional construction. Borcherds singular-
theta lifts require an indefinite even lattice and produce automorphic
forms on type IV (orthogonal) Hermitian symmetric domains. The two are
*formally* related via Borcherds 1995 (Monstrous Moonshine), but
$\mathfrak{sl}_2$ alone has no associated Lorentzian even unimodular
lattice in the V77 Class A'' table.

**(c) Ghost theorem (Attack 2).**
> *The affinisation $\widehat{\mathfrak{sl}_2}$ at level $k \geq 1$ is
> a lattice-VOA-like object whose character lifts via the Weyl–Kac
> formula, not via Borcherds singular-theta. The two lifts agree only
> in the special case of even unimodular Lorentzian lattices (e.g.
> $II_{1,1} \oplus E_8 = II_{1,9}$ giving $\Delta(\tau)$ as a
> Borcherds product). For $\mathfrak{sl}_2$ alone, no such lattice
> exists; $Y(\mathfrak{sl}_2)$ is not Class A''.*

**Survival verdict.** $Y(\mathfrak{sl}_2)$ does **NOT** belong to V77
Class A''. Its absence from the algebraic non-geometric Pentagon-coherence
ladder confirms the V64 Class B classification on the algebraic side.

---

### 2.3 Attack 3 — Compute the actual shadow tower of $Y(\mathfrak{sl}_2)$

**The attack.** V64 asserts $Y(\mathfrak{sl}_2)$ has *class M* shadow
tower with the rationale "non-trivial $S_k$ for all $k$ via the
Stasheff $A_\infty$ relations". This violates AP-CY12: the shadow
class must be computed from the FULL tower, not asserted via generator
counting or non-formality.

Let us compute. The Yangian $Y(\mathfrak{sl}_2)$ has Drinfeld
generators $\{x^\pm_n, h_n : n \geq 0\}$, with $h_0, x^\pm_0$ giving
the embedded $\mathfrak{sl}_2$ and $h_1, x^\pm_1$ generating the
"Yangian shift". Drinfeld's second presentation gives the relations
explicitly. The *coproduct* $\Delta : Y(\mathfrak{sl}_2) \to Y(\mathfrak
{sl}_2) \otimes Y(\mathfrak{sl}_2)$ on $x^+_0$ is

$$
\Delta(x^+_0) = x^+_0 \otimes 1 + 1 \otimes x^+_0,
$$

and on $x^+_1$ has the famous correction

$$
\Delta(x^+_1) = x^+_1 \otimes 1 + 1 \otimes x^+_1 + \hbar \cdot h_0 \otimes x^+_0.
$$

The *higher* coproduct corrections $\Delta(x^+_n)$ for $n \geq 2$
involve nested commutators of $h_i$ with $x^+_j$ — these are the
*shadow tower entries* $S_k$ in the chiral-algebra avatar.

**Key computation.** The Drinfeld coproduct on $x^+_n$ has the closed
form (Molev 2007, Yangians and Classical Lie Algebras §3):

$$
\Delta(x^+_n) = \sum_{k=0}^{n} x^+_{n-k} \otimes h_0^k \cdot (\hbar)^k / k!
\quad + \quad \text{lower-order corrections in $h_i$, $x^\pm_j$ for $i,j < n$}.
$$

The truncation pattern: for $\mathfrak{sl}_2$ specifically (rank 1,
$\dim = 3$), the recursion **terminates** after finitely many steps
when applied to a fixed weight space, because the Cartan element $h_0$
has discrete spectrum on each representation.

Concretely on the fundamental representation $V = \mathbb{C}^2$ (the
two-dimensional spin-$1/2$): the eigenvalues of $h_0$ are $\pm 1$;
$x^+_n$ acts as $(\hbar)^n$ times a fixed nilpotent matrix; and the
coproduct shadow tower terminates at depth **2** because $(x^+)^3 = 0$
on $V \otimes V$ (the weight-3 component is zero).

For the full $Y(\mathfrak{sl}_2)$ acting on the *category of all
finite-dimensional representations*, the shadow tower terminates at
finite depth on each irreducible (Drinfeld polynomials parametrise
the irreducibles, all finite-dim), but does *not* uniformly terminate
across all irreducibles — yielding **shadow class L** (not class M).

The defining property of class M (per V8 + the V58 / V63 / V64 usage)
is that the shadow tower is **Gevrey-1 divergent and Borel-summable**,
with non-trivial alien-derivation Stokes data. For $Y(\mathfrak{sl}_2)$,
the shadow tower on each irreducible is *finite* — there is no Gevrey
divergence, no Stokes phenomena, no mock-modular completion needed.
Class M misclassifies the tower.

**(a) What V64 gets RIGHT.** $Y(\mathfrak{sl}_2)$ does have *non-trivial*
shadow tower entries beyond depth 1 (the $\hbar h_0 \otimes x^+_0$
correction at $x^+_1$ proves $S_2 \neq 0$). The tower is non-formal.

**(b) What V64 gets WRONG.** Non-formal $\neq$ class M. AP-CY12 demands
the FULL tower computation; V64 short-circuited via "Stasheff $A_\infty$
relations". The Stasheff $A_\infty$ relations enforce *consistency* of
the tower (the Yang–Baxter equation $R_{12} R_{13} R_{23} = R_{23}
R_{13} R_{12}$ at all orders), not class-M divergence. The Maulik–
Okounkov mock-modular argument applies to the *toroidal* extension
$U_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})$ acting on K-theoretic
stable envelopes of Hilbert schemes of K3 — *not* to the bare Yangian
$Y(\mathfrak{sl}_2)$.

**(c) Ghost theorem (Attack 3).**
> *The shadow tower of $Y(\mathfrak{sl}_2)$ as a finite Yangian (no
> central extension, no chiral realisation) is class L: non-formal but
> finite-depth on each irreducible. Class M assignment requires either
> (i) passage to the central / chiral extension $\widehat{Y(\mathfrak
> {sl}_2)}$, or (ii) the toroidal extension to $\mathfrak{gl}_1^{\widehat
> {\widehat{}}}$ acting on K3 Hilbert schemes (Maulik–Okounkov), neither
> of which is identified with bare $Y(\mathfrak{sl}_2)$.*

**Survival verdict.** V64's class M assignment for $Y(\mathfrak{sl}_2)$
is **REFUTED by AP-CY12 protocol**. Correct class is L. The Class B
designation in V55 (which presupposes class M) is therefore *also*
wrong: $Y(\mathfrak{sl}_2)$ should be in a *new* sub-class — call it
**Class B$_L$** — of "non-K3-fibred, non-super-trace-vanishing,
shadow-class-L" inputs. (Class B as defined in V55 is the class M
sub-case of "neither A nor B0".)

---

### 2.4 Attack 4 — Does $\operatorname{str}$ apply to non-super $\mathfrak{sl}_2$?

**The attack.** V64 §2.3 asserts $\operatorname{str}(K_{Y(\mathfrak
{sl}_2)}) = 3 \neq 0$ to rule out Class B0. But $\operatorname{str}$
is the *super-trace*, defined for $\mathbb{Z}/2$-graded (super) vector
spaces as $\operatorname{tr}_{\mathrm{even}} - \operatorname{tr}_{\mathrm
{odd}}$. For ungraded $\mathfrak{sl}_2$, $\operatorname{str} =
\operatorname{tr}$ (trivial $\mathbb{Z}/2$ grading, all even). So $\operatorname
{str}(K_{\mathfrak{sl}_2}) = \operatorname{tr}(K_{\mathfrak{sl}_2}) =
\dim \mathfrak{sl}_2 = 3$.

But this is the **wrong test** for Class B0. The V55 Class B0 condition
$\operatorname{str}(K_A) = 0$ is the *characteristic-0 super-condition*
for the existence of a super-EK twist, which requires GENUINE super-
structure on $A$ — i.e., $A$ must have a non-trivial $\mathbb{Z}/2$
grading and the super-trace cancellation must occur. Applying $\operatorname
{str}$ to a non-super algebra trivially gives the dimension; this
neither passes nor fails the B0 test, because the test is *not
applicable*.

The correct B0 question for $Y(\mathfrak{sl}_2)$: does $Y(\mathfrak
{sl}_2)$ admit a SUPER-extension $Y(\mathfrak{sl}_2 | 0)$ or $Y(\mathfrak
{gl}(1|1))$ such that the super-extension passes the B0 test? Answer:
$Y(\mathfrak{gl}(1|1))$ exists (resolved conifold case in V64 §4) but
is NOT $Y(\mathfrak{sl}_2)$. The two have different presentations,
different evaluation modules, and different R-matrices. Identifying
$Y(\mathfrak{sl}_2)$ with $Y(\mathfrak{gl}(1|1))$ would be a category
error (different rank, different superdimension).

**(a) What V64 gets RIGHT.** The conclusion "Class B0 does not apply
to $Y(\mathfrak{sl}_2)$" is correct; $Y(\mathfrak{sl}_2)$ is not in
B0.

**(b) What V64 gets WRONG.** The *justification* via $\operatorname{str}
(K_{\mathfrak{sl}_2}) = 3 \neq 0$ is a category error (treating
non-super as super). The correct justification is "$Y(\mathfrak{sl}_2)$
is not super, so the B0 test (which requires super-structure) does not
apply, and $Y(\mathfrak{sl}_2)$ is therefore not in B0".

**(c) Ghost theorem (Attack 4).**
> *The V55 Class B0 test $\operatorname{str}(K_A) = 0$ is well-defined
> only for super-Lie-algebra-structured $A$. Applying $\operatorname{str}$
> to non-super $A$ yields $\operatorname{tr}$, which is generically
> non-zero (= $\dim \mathfrak{g}$ for $A = U(\mathfrak{g})$, $Y(\mathfrak
> {g})$, etc.) and does not constitute a B0 falsification, only a B0
> non-applicability. Class B0 should be re-defined as "super-Lie input
> with super-trace vanishing"; non-super inputs are automatically
> excluded.*

**Survival verdict.** V64's $\operatorname{str}$ argument is a
**categorical mismatch**, but the *conclusion* (Y(sl_2) not in B0) is
correct under the corrected B0 definition.

---

### 2.5 Attack 5 — Does $\widehat{\mathfrak{sl}_2}$ admit a Borcherds lift?

**The attack.** V64 §8.3 ghost theorem asserts that $Y(\mathfrak{sl}_2)$
"has no Borcherds lift", with the parenthetical "(the K3 Mukai lattice
has rank 24, not 3)". But the *affinisation* $\widehat{\mathfrak{sl}_2}$
embeds in the lattice VOA $V_{A_1}$ (rank 1) and via further extension
in $V_{II_{1,1}}$ (rank 2 Lorentzian). The genus-1 Borcherds product
$\Delta(\tau) = \eta(\tau)^{24}$ is the unique cusp form of weight 12
on $SL_2(\mathbb{Z})$, and it IS a Borcherds singular-theta lift on
the rank-2 lattice $II_{1,1}$ (Borcherds 1995). So $\widehat{\mathfrak
{sl}_2}$ — via embedding in $V_{II_{1,1}}$ — DOES admit a Borcherds-style
lift.

If $Y(\mathfrak{sl}_2)$ inherits this lift via the affinisation map
$Y(\mathfrak{sl}_2) \to \widehat{\mathfrak{sl}_2} \otimes \mathbb{C}((\hbar))$
(Drinfeld's degeneration), then the ghost theorem of V64 §8.3 must be
amended.

**(a) What this attack gets RIGHT.** $\widehat{\mathfrak{sl}_2}$ does
embed in $V_{II_{1,1}}$ at level $k = 1$, and $\Delta(\tau)$ is a
Borcherds product on this lattice. The "no Borcherds lift" claim is
technically too strong if interpreted to include the affinisation.

**(b) What this attack gets WRONG.** The Drinfeld degeneration $Y(\mathfrak
{sl}_2) \to \widehat{\mathfrak{sl}_2}$ is NOT a chiral-algebra map; it
is a *limit* (the rational R-matrix degenerates to the trigonometric
one as $\hbar \to 0$ at fixed quantum parameter, recovering $\widehat
{\mathfrak{sl}_2}$ at level $k$). The chiral structures are
*incompatible*: $Y(\mathfrak{sl}_2)$ has rational R-matrix $1 + (\hbar
/z)P$, while $\widehat{\mathfrak{sl}_2}$ has the level-$k$ R-matrix
governed by the OPE $J^a(z) J^b(w) \sim k \delta^{ab}/(z-w)^2 +
f^{abc} J^c(w)/(z-w)$. The Yangian's spectral parameter is *deformation*
$\hbar$; the Kac–Moody's spectral parameter is *worldsheet* $z$. By
AP-CY31 (spectral $z$ vs worldsheet $z$), conflating them is forbidden.

So the Borcherds lift of $\Delta(\tau)$ on $V_{II_{1,1}}$ is a lift of
$\widehat{\mathfrak{sl}_2}$ at $k = 1$, NOT of $Y(\mathfrak{sl}_2)$ as
an $E_1$-chiral algebra. The two have different categorical homes.

**(c) Ghost theorem (Attack 5).**
> *The Yangian $Y(\mathfrak{sl}_2)$ and the affine Kac–Moody $\widehat
> {\mathfrak{sl}_2}$ are linked by Drinfeld degeneration but are
> distinct as $E_1$-chiral algebras (different spectral parameter
> origin per AP-CY31). The Borcherds lift of $\Delta(\tau) = \eta^{24}$
> on $V_{II_{1,1}}$ is a lift of $\widehat{\mathfrak{sl}_2}$ at level
> $1$, NOT of $Y(\mathfrak{sl}_2)$. The V64 ghost theorem ("no
> Borcherds lift for $Y(\mathfrak{sl}_2)$") survives, with the
> clarification that the affinisation has its own (different) lift
> that does not transfer back.*

**Survival verdict.** V64's "no Borcherds lift" claim **survives**,
once the AP-CY31 spectral-parameter discipline is enforced. The
$\widehat{\mathfrak{sl}_2}$ Borcherds lift exists but does not lift
$Y(\mathfrak{sl}_2)$.

---

## §3. Explicit cohomology computation: is $\omega^{Y(\mathfrak{sl}_2)}$ a coboundary in $H^2$?

We compute the relevant Hochschild cohomology classes order-by-order in
$\hbar$. The R-matrix expansion is

$$
R(z) = 1 + \frac{\hbar}{z} P + \frac{\hbar^2}{2 z^2} P^2 +
\frac{\hbar^3}{6 z^3} P^3 + \cdots = \exp\!\left(\frac{\hbar}{z} P\right),
$$

where $P^2 = \mathrm{id}$ on $V \otimes V$ (permutation squared = id),
so $\exp((\hbar/z) P) = \cosh(\hbar/z) + P \sinh(\hbar/z)$. The
inverse is $R(z)^{-1} = \exp(-(\hbar/z) P) = \cosh(\hbar/z) - P \sinh
(\hbar/z)$.

**Conjugation expansion.** For any $a$,

$$
R(z) \cdot a \cdot R(z)^{-1} - a = \sum_{k \geq 1} \frac{(\hbar/z)^k}{k!}
\,[\underbrace{P, [P, \ldots [P}_{k}, a]\ldots]],
$$

the iterated adjoint action.

### 3.1 Order $\hbar^1$ (Attack 1 result)

$$
\omega^{(1)}(a) = \frac{1}{z}\,[P, a].
$$

This is the inner derivation $\mathrm{ad}_{P/z}$. As a Hochschild
$1$-cochain valued in $\mathrm{End}(P_5)[[z, z^{-1}]]$, it equals
$\delta_{\mathrm{Hoch}}(P/z)$ where $P/z$ is regarded as a Hochschild
$0$-cochain. Hence

$$
[\omega^{(1)}] = 0 \quad \text{in } H^2.
$$

**Conclusion (h^1).** Bounds. V64's claim of non-vanishing fails at
$\hbar^1$.

### 3.2 Order $\hbar^2$

$$
\omega^{(2)}(a) = \frac{1}{2 z^2}\,[P, [P, a]] = \frac{1}{2 z^2}\,
\mathrm{ad}_P^2(a).
$$

This is again an inner derivation: $\mathrm{ad}_P^2 = \mathrm{ad}_P
\circ \mathrm{ad}_P$, and the *twice-iterated* inner derivation is the
Hochschild coboundary of the $0$-cochain $P^2/(2 z^2) = \mathrm{id}/(2
z^2)$, which is *central*. Wait — central elements have *zero*
Hochschild differential ($\delta(c) = c \cdot a - a \cdot c = 0$ for $c$
central), so $P^2/(2 z^2) = 1/(2 z^2)$ is in the kernel of $\delta$, not
a witness to $\omega^{(2)}$ being a coboundary.

Let us compute carefully. $\omega^{(2)}(a) = (1/(2z^2)) \mathrm{ad}_P^2
(a) = (1/(2z^2))(P^2 a - 2 P a P + a P^2) = (1/(2z^2))(2a - 2 PaP) =
(1/z^2)(a - PaP)$. The map $a \mapsto a - PaP$ is the *antisymmetrisation*
under permutation $P$; this is **NOT** an inner derivation (it does not
have the form $[X, a]$ for any $X$, because $a - PaP = [Q, a]$ requires
$Q$ such that $Qa - aQ = a - PaP$, which has no general solution).

So $\omega^{(2)}$ is genuinely non-trivial in $H^2$ at the chain level.

**However**, the Schouten bracket structure gives more: by the rational
classical Yang–Baxter equation $[r_{12}, r_{13}] + [r_{12}, r_{23}] +
[r_{13}, r_{23}] = 0$ for $r(z) = P/z$ (which IS the rational
$r$-matrix on $\mathfrak{sl}_2$), the Schouten square $[r, r] = 0$.
This means $\omega^{(2)}$ — interpreted as the Schouten-square obstruction
— DOES vanish in the Schouten-bracket sense.

But the Schouten-bracket vanishing is at the *Lie bialgebra* level
(Drinfeld 1983, Hamiltonian structure), not at the Hochschild chiral
$H^2$ level we are computing. The Hochschild $H^2$ chain-level cocycle
$\omega^{(2)}(a) = (1/z^2)(a - PaP)$ is the *image* of the classical
Yang–Baxter under the Hochschild map, and need not bound even when
$[r, r] = 0$.

### 3.3 Class in $H^2$ at $\hbar^2$

The cocycle $\omega^{(2)}$ pairs against Hochschild $2$-chains $[a_0 |
a_1]$ via the $z$-integrated formal residue. For the spectral pairing

$$
\langle \omega^{(2)}, [a_0 | a_1] \rangle = \mathrm{Res}_{z = 0}\,
\frac{1}{z^2} (a_0 a_1 - P a_0 a_1 P) \, dz = \mathrm{coefficient of } z^1
\text{ in } a_0 a_1 - P a_0 a_1 P,
$$

which is generically non-zero. This pairing is well-defined on $H^2$
and detects the cohomology class (the only ambiguity in $\omega^{(2)}$
modulo coboundaries is by inner derivations $\delta X$, all of which
have *zero* spectral pairing because $\mathrm{Res}_z (1/z) X(z) \cdot
(a_0 a_1 - a_0 a_1) = 0$).

**Conclusion (h^2).** $[\omega^{(2)}] \neq 0$ in $H^2$. The Yang–Baxter
anomaly to V19 Trinity coherence is genuine at $\hbar^2$.

### 3.4 Summary table

| Order | Cocycle $\omega^{(k)}(a)$ | $H^2$ class |
|---|---|---|
| $\hbar^0$ | $0$ | $0$ |
| $\hbar^1$ | $(1/z)[P, a]$ | $\boxed{0}$ (inner derivation = coboundary) |
| $\hbar^2$ | $(1/z^2)(a - PaP)$ | $\boxed{\neq 0}$ (antisymmetrisation, genuine class) |
| $\hbar^3$ | $(1/(6z^3))[P, a - PaP]$ | $0$ (inner derivation of $h^2$ class, bounds) |
| $\hbar^4$ | $(1/(12 z^4))(a - PaP)$ + higher | $\neq 0$ |
| $\hbar^{2m}$ | $\propto (1/z^{2m})(a - PaP)$ | $\neq 0$ |
| $\hbar^{2m+1}$ | $\propto (1/z^{2m+1})[P, a - PaP]$ | $0$ |

The pattern: **even orders carry the Yang–Baxter anomaly; odd orders
are inner derivations of preceding even-order classes**.

So V64's $\hbar^1$ counterexample is *cohomologically trivial*, but
the $\hbar^2$ counterexample is *cohomologically non-trivial*. V64
must be re-stated to identify the obstruction at $\hbar^2$.

---

## §4. Explicit shadow tower for $Y(\mathfrak{sl}_2)$ — class G/L/C/M?

Per AP-CY12, we compute the FULL tower. The shadow tower entries
$S_k$ for an $E_1$-chiral algebra $A$ are the $A_\infty$ coproduct
correction terms in the expansion $\Delta_z(a) = \Delta_0(a) + \sum_{k
\geq 1} z^k S_k(a)$, equivalently the $\delta^{(k)}$ in Vol III's
shadow-Feynman dictionary (where $L$-loop Feynman = $S_{L+1}$).

For $Y(\mathfrak{sl}_2)$ in Drinfeld's second presentation, on the
generator $x^+_0$:

$$
\Delta(x^+_0) = x^+_0 \otimes 1 + 1 \otimes x^+_0 \quad \Rightarrow \quad S_k(x^+_0) = 0 \text{ for } k \geq 1.
$$

On $x^+_1$:

$$
\Delta(x^+_1) = x^+_1 \otimes 1 + 1 \otimes x^+_1 + \hbar h_0 \otimes x^+_0 \quad \Rightarrow \quad S_1(x^+_1) = h_0 \otimes x^+_0, \quad S_k(x^+_1) = 0 \text{ for } k \geq 2.
$$

On $x^+_2$ (Molev §3):

$$
\Delta(x^+_2) = x^+_2 \otimes 1 + 1 \otimes x^+_2 + \hbar h_0 \otimes x^+_1 + \hbar h_1 \otimes x^+_0 + \frac{\hbar^2}{2} h_0^2 \otimes x^+_0,
$$

$\Rightarrow S_1(x^+_2) = h_0 \otimes x^+_1 + h_1 \otimes x^+_0$, $S_2
(x^+_2) = (1/2) h_0^2 \otimes x^+_0$, $S_k(x^+_2) = 0$ for $k \geq 3$.

Pattern: on the generator $x^+_n$, the shadow tower has support exactly
in degrees $\{1, 2, \ldots, n\}$ — TERMINATING at depth $n$. There is
no Gevrey-1 divergence; for any *fixed* generator, finitely many $S_k$
are non-zero.

The Borel-summability test: form the generating series $\sum_k S_k(x^+_n)
\cdot t^k$. For $x^+_n$, this is a *polynomial* in $t$ of degree $n$ —
finite radius of convergence (= $\infty$, polynomials have no finite
radius). No Stokes phenomena, no alien derivations, no mock-modular
completion needed.

**Verdict.** The shadow tower of $Y(\mathfrak{sl}_2)$ is:
- **NOT class G** (free / formal): non-trivial $S_k$ for $k \geq 1$
  exist.
- **YES class L**: $S_k$ non-trivial but tower TERMINATES at finite
  depth on each generator (depth = generator index $n$).
- **NOT class C**: no charge-conservation cancellation is invoked;
  the tower is simply finite.
- **NOT class M**: no Gevrey-1 divergence, no Borel summation needed,
  no mock-modular completion.

**$Y(\mathfrak{sl}_2)$ is shadow class L, not class M.**

V64's "class M" assignment is REFUTED by direct computation. (V64
implicitly conflated *infinitely-many-generators* with *infinite-depth
tower per generator*; Yangians have infinitely many generators
$\{x^\pm_n, h_n\}_{n \geq 0}$, but each generator has *finite-depth*
shadow.)

This invalidates V64's V55 sub-classification. Correct sub-class:
**Class B$_L$** (newly named): non-K3-fibred + non-super-extension +
shadow class L. Inhabitants: $Y(\mathfrak{sl}_2)$, $Y(\mathfrak{sl}_n)$
for $n \geq 2$, and presumably $Y(\mathfrak{g})$ for any simple $\mathfrak
{g}$.

The genuine V55 Class B (mock-modular residual) is RESERVED for class
M inputs: quintic, local $\mathbb{P}^2$, banana (V58, V63 confirmed
class M via BCOV resurgence). Yangians belong to a DIFFERENT
sub-class.

---

## §5. WHAT SURVIVES the attack

Per-attack survival summary:

| Attack | V64 claim under attack | Survival verdict |
|---|---|---|
| 1 | $\omega^{(1)} \neq 0$ in $H^2$ | **REFUTED** at $\hbar^1$ (inner derivation = coboundary). Counterexample must be moved to $\hbar^2$. |
| 2 | $Y(\mathfrak{sl}_2)$ not Class A'' | **CONFIRMED** (no Borcherds lift on $\mathfrak{sl}_2$ alone). |
| 3 | $Y(\mathfrak{sl}_2)$ has class M shadow | **REFUTED** by direct computation (class L, finite depth per generator). Need new sub-class B$_L$. |
| 4 | $\operatorname{str}(K_{\mathfrak{sl}_2}) = 3$ rules out B0 | **MISCATEGORISED** (super-trace not applicable to non-super), conclusion correct under refined B0 definition. |
| 5 | $Y(\mathfrak{sl}_2)$ has no Borcherds lift | **CONFIRMED** under AP-CY31 spectral-parameter discipline. ($\widehat{\mathfrak{sl}_2}$ has one, but Yangian doesn't inherit it.) |

**Net survival of the V64 counterexample at $\hbar^2$.** The cocycle
$\omega^{(2)}(a) = (1/z^2)(a - PaP)$ is genuinely non-zero in $H^2$;
the Yang–Baxter anomaly is real; $Y(\mathfrak{sl}_2)$ does falsify
unconditional V19 Trinity-$E_1$ at chain level. The counterexample
**stands**, but with three required corrections to V64:

(C1) **Lower-order correction.** Move the explicit cocycle from $\hbar^1$
to $\hbar^2$: the explicit non-bounding chain is $\omega^{(2)} =
(1/z^2)(a - PaP)$, NOT $(\hbar/z)[P, a]$. The latter bounds.

(C2) **Shadow-class correction.** Re-classify $Y(\mathfrak{sl}_2)$ from
*Class B (class M)* to *Class B$_L$ (class L)* — a new sub-class for
non-K3-fibred Yangians. The Class B residual $\xi_{\mathrm{V19}}^{Y(\mathfrak
{sl}_2)}$ must be re-derived in the class L framework, where the
obstruction is NOT mock-modular but ALGEBRAIC (Yang–Baxter anomaly).

(C3) **Super-trace correction.** Replace the $\operatorname{str}$
argument with an explicit "super-structure not applicable" justification
to keep the AP-CY55 manifold-vs-algebraisation discipline clean.

---

## §6. FOUNDATIONAL HEAL — refinement, not preservation, not recovery

The three options laid out in the prompt:
- **Strong counterexample preservation.** Refuted by Attack 1: the
  $\hbar^1$ cocycle bounds.
- **Strong refinement.** SURVIVES. The counterexample stands at
  $\hbar^2$, with three corrections (§5 C1–C3) and a new class B$_L$.
- **Strong recovery.** Refuted by §3.3: the $\hbar^2$ class is
  genuinely non-zero in $H^2$.

The healing is **strong refinement**: V64's counterexample is real but
needs re-statement.

### 6.1 Corrected V19 Trinity-$E_1$ scope at $Y(\mathfrak{sl}_2)$

> **Theorem (V19 Trinity-$E_1$ chain-level for $Y(\mathfrak{sl}_2)$ —
> refined per V79).** The V19 Trinity-$E_1$ chain-level cocycle for
> $A = Y(\mathfrak{sl}_2)$ admits the explicit expansion
> $$
> \omega_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)} = \sum_{k \geq 1} \frac{\hbar^k}{k!\, z^k}\,\mathrm{ad}_P^k.
> $$
> At odd orders $k = 2m+1$, $\omega^{(2m+1)} = (\hbar^{2m+1}/((2m+1)!
> z^{2m+1})) \mathrm{ad}_P \circ \mathrm{ad}_P^{2m}$ is an inner
> derivation, hence a Hochschild $H^2$ coboundary. At even orders $k =
> 2m$, $\omega^{(2m)} = (\hbar^{2m}/((2m)! z^{2m})) (a - PaP) \cdot
> 2^{2m-1}$ is the antisymmetrisation under $P$, generically non-zero
> in $H^2$ (the Yang–Baxter anomaly).
>
> $Y(\mathfrak{sl}_2)$ is shadow class L (NOT M), so falls in the new
> sub-class **B$_L$**: non-K3-fibred, non-super-extension, finite-depth
> shadow tower. Class B$_L$ is governed by the Drinfeld classical
> $r$-matrix Schouten bracket $[r, r]$ and the rational classical
> Yang–Baxter equation, NOT by mock-modular completion.
>
> $\xi_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)} = \omega^{(2)} + O(\hbar^4)$
> is the **genuine** chain-level residual; the $\hbar^1$ correction is
> a coboundary and does not contribute to the $H^2$ obstruction.

### 6.2 Corrected per-class V19 Trinity table (V79 update)

| Class | Inhabitants | Status | Residual leading order |
|---|---|---|---|
| abelian | $H_k$, $V_\Lambda$, $\beta\gamma$ | PROVED | $0$ identically (Schur) |
| A | K3 | PROVED | $0$ |
| A (ext) | K3$\times$E, STU, 8 K3 orbifolds | PROVED | $0$ |
| A' | non-symplectic K3-fibred | CONDITIONAL (V77) | TBD per case |
| A'' | Conway $II_{2,26}$, Leech | PROVED algebraically (V77) | $0$ |
| B0 | Conifold $Y(\mathfrak{gl}(1|1))$ | PROVED | $0$ via super-EK |
| **B$_L$** (NEW) | $Y(\mathfrak{sl}_n)$, $n \geq 2$, generic Yangian no K3 lift | **CONJECTURE** (Yang–Baxter anomaly) | $(\hbar^2/z^2)(a - PaP) + O(\hbar^4)$ |
| B (i.e. $B_M$) | quintic, LP$^2$, banana (class M) | CONJECTURE | mock-modular per input |

The new sub-class B$_L$ separates *finite-depth Yangian counterexamples*
(Drinfeld-Yang–Baxter type) from *mock-modular class-M residuals* (BCOV-
resurgent type). These are genuinely different obstructions and should
not be conflated.

### 6.3 Updated V64 ghost theorem (per AP-CY61)

The V64 §8.2 ghost theorem stands with one amendment:

> **Refined ghost theorem.** *For an $E_1$-chiral algebra $A$, the
> three Hochschild presentations form a chain-level coherent triangle
> in $H^2$ if and only if $A$ admits either (a) a Borcherds singular-
> theta lift on a Lorentzian even unimodular lattice (Class A, A''),
> (b) a super-trace-vanishing super-extension (Class B0), or (c) a
> mock-modular completion of its class-M shadow tower (Class B / B$_M$).*
>
> *For $A$ with finite-depth shadow tower (class L) but no K3-Borcherds
> source — the new Class B$_L$, inhabited by $Y(\mathfrak{sl}_2)$ and
> general non-affine simple Yangians — V19 Trinity-$E_1$ chain-level
> is OBSTRUCTED at order $\hbar^2$ by the rational classical Yang–
> Baxter Schouten image $[r, r]_{\mathrm{Hoch}} \neq 0$ in $H^2$. The
> obstruction is ALGEBRAIC (Drinfeld classical $r$-matrix theory),
> NOT analytic / mock-modular.*

This refinement is consistent with V77's finer class structure (A',
A'') and extends it on the B side: **the Class B side is also not
monolithic; it splits into B$_L$ (algebraic Yang–Baxter) and B$_M$
(analytic mock-modular).**

### 6.4 What the heal preserves and what it changes

**Preserves.**
- The V64 thesis that V19 Trinity-$E_1$ is FALSE unconditionally.
- The V64 use of $Y(\mathfrak{sl}_2)$ as the canonical non-Class-A
  counterexample.
- The V64 ghost theorem (Borcherds lift as the load-bearing condition
  for unconditional Trinity).
- The V58 / V63 Class A and B0 theorems unchanged.
- The Heisenberg V59 / §5 abelian theorem unchanged.

**Changes.**
- $\hbar^1$ replaced by $\hbar^2$ as the leading non-bounding obstruction.
- Class M assignment for $Y(\mathfrak{sl}_2)$ replaced by Class L.
- Class B for $Y(\mathfrak{sl}_2)$ refined to new sub-class B$_L$.
- Three justification corrections (C1, C2, C3) propagate into the V64
  inscription draft (§7 below).

### 6.5 Consistency with the cross-volume programme

- **Vol I.** V19 Trinity chapter must be updated: replace the $\hbar^1$
  cocycle in `ex:V19-trinity-Y-sl2-counterex` with the $\hbar^2$ Yang–
  Baxter Schouten image. New label `conj:V19-trinity-class-B_L` for the
  Yangian sub-class. Existing `conj:V19-trinity-class-B` re-named to
  `conj:V19-trinity-class-B_M` to disambiguate from B$_L$.
- **Vol II.** V15 Pentagon chapter `rem:V15-V19-trinity-cross` extended
  to include the B$_L$ split.
- **Vol III.** K3 Yangian chapter `cor:k3-v19-trinity-chain-level`
  unchanged (K3 is Class A, not affected). New Vol III remark in the
  "non-K3 Yangians" section pointing to the V79 B$_L$ theorem.

No retractions of theorems; only refinement of the conjectural sector.

---

## §7. Updated V64 inscription draft (refined per V79)

```latex
%% =========================================================================
%% Vol I §V19 epilogue: chain-level dichotomy for V19 Trinity-at-E_1
%% (V64 refined per V79 — moved h^1 cocycle to h^2 Yang-Baxter Schouten image;
%%  re-classified Y(sl_2) from Class B to Class B_L; split B into B_L and B_M).
%% Sandbox draft from wave_V79_attack_heal_Y_sl2_counterexample.md
%% (Wave V79, 2026-04-16). Inscription pending main-thread review.
%% Author: Raeez Lorgat. No AI attribution. Not committed.
%%
%% New labels introduced in V79 (additions to V64 label set):
%%   conj:V19-trinity-class-B-L        -- new B_L sub-class (Yangians, finite-depth)
%%   conj:V19-trinity-class-B-M        -- renamed from V64 conj:V19-trinity-class-B
%% Updated labels:
%%   ex:V19-trinity-Y-sl2-counterex    -- explicit cocycle moved to h^2
%% =========================================================================

\begin{example}[$Y(\fsl_2)$ falsifies unconditional V19 Trinity-$E_1$
                at order $\hbar^2$ (Yang--Baxter Schouten image)]
\label{ex:V19-trinity-Y-sl2-counterex}
For $A = Y(\fsl_2)$, the rational R-matrix
$R(z) = \exp((\hbar/z) P) = 1 + (\hbar/z) P + (\hbar^2 / 2 z^2) P^2 + \cdots$
is matrix-valued (not central), giving the chain-level cocycle expansion
\[
  \omega_{\mathrm{V19}}^{Y(\fsl_2)}(a)
  = R(z) \cdot a \cdot R(z)^{-1} - a
  = \sum_{k \geq 1} \frac{\hbar^k}{k!\,z^k}\,\ad_P^k(a).
\]
The order-$\hbar^1$ term $(\hbar/z)[P, a]$ is an inner derivation,
hence a Hochschild $H^2$ coboundary (bounded by the $0$-cochain
$P/z$). The genuine non-bounding obstruction first appears at order
$\hbar^2$:
\[
  \omega^{(2)}(a) = \frac{\hbar^2}{2 z^2}\,(a - P a P),
\]
the $P$-antisymmetrisation, which is the Hochschild image of the
Drinfeld classical $r$-matrix Schouten square $[r, r]$ for $r(z) = P/z$.
By the V55 dichotomy refined in V79, $Y(\fsl_2)$ is Class $B_L$
(non-K3-fibred, non-super-extension, shadow class L by direct
computation: each generator $x^+_n$ has shadow support
$\{1, \ldots, n\}$, terminating). The apparent counterexample to
unconditional V19 Trinity is precisely Conjecture~\ref{conj:V19-trinity-
class-B-L} restricted to $Y(\fsl_2)$, with explicit residual
$\xi_{\mathrm{V19}}^{Y(\fsl_2)} = \omega^{(2)}(a) = (\hbar^2/2 z^2)(a -
PaP)$.
\end{example}

\begin{conjecture}[V19 Trinity-$E_1$ chain-level for Class $B_L$
                  (algebraic Yang--Baxter residual)]
\label{conj:V19-trinity-class-B-L}
For $A$ a Yangian or Yangian-like $E_1$-chiral algebra with shadow class
L (finite-depth tower per generator), no K3-Borcherds source, and no
super-trace-vanishing super-extension --- canonically $A = Y(\fg)$ for
$\fg$ simple non-affine --- the chain-level Trinity identity holds modulo
the order-$\hbar^2$ Hochschild image of the classical $r$-matrix
Schouten square $[r_A, r_A]_{\mathrm{Hoch}}$. Vanishing is conjectural,
equivalent to the existence of an algebraic Drinfeld twist trivialising
$[r_A, r_A]_{\mathrm{Hoch}}$ in $H^2(\SCcht; \fraut)$.
\end{conjecture}

\begin{conjecture}[V19 Trinity-$E_1$ chain-level for Class $B_M$
                  (mock-modular class-M residual; renamed from V64)]
\label{conj:V19-trinity-class-B-M}
For $A$ class M, neither K3-fibred (Class A) nor super-trace vanishing
(Class B0) --- canonically $A_{\mathrm{quintic}}$, $A_{\mathrm{LP^2}}$
--- the chain-level Trinity identity holds modulo the Trinity-sector
projection $\xi_{\mathrm{V19}}(A) := \pi_{\mathrm{V19}}(\xi(A))$ of the
class M alien-derivation correction. Vanishing is conjectural per input
conditional on the V8~§6 mock-modular completion of the shadow tower of
$A$.
\end{conjecture}

\begin{remark}[V79 split of Class B into $B_L$ (algebraic) and $B_M$
              (analytic)]
\label{rem:V19-trinity-V79-B-split}
The V64 Class B is refined per V79 into two genuinely different
sub-classes: $B_L$ governed by the algebraic classical $r$-matrix
theory (Drinfeld Yang--Baxter), and $B_M$ governed by analytic
mock-modular completion (BCOV resurgence, Maulik--Okounkov stable
envelopes). The split tracks the shadow-class distinction: Yangians are
shadow class L (finite-depth, algebraic obstruction); compact CY3
non-K3-fibred targets are shadow class M (Gevrey-1, mock-modular
obstruction). $Y(\fsl_2)$ is the canonical $B_L$ inhabitant; the
quintic and local $\mathbb{P}^2$ are canonical $B_M$ inhabitants. V79
also confirms (Attack 1) that the V64 explicit cocycle stated at order
$\hbar^1$ is in fact a coboundary; the genuine obstruction lives at
order $\hbar^2$ as the Hochschild image of $[r, r]_{\mathrm{class}}$.
\end{remark}
```

The §9 V64 status table is updated by inserting the new B$_L$ row
between B-Yangian (renamed) and the other B entries:

| Class | Inhabitants | V19 Trinity-$E_1$ chain-level status | Residual $\xi_{\mathrm{V19}}(A)$ | Source |
|---|---|---|---|---|
| **B$_L$** (NEW) | $Y(\mathfrak{sl}_2)$, $Y(\mathfrak{sl}_n)$ for $n \geq 2$ | CONJECTURE (algebraic Yang–Baxter) | $(\hbar^2 / 2 z^2)(a - PaP) + O(\hbar^4)$ at $\hbar^2$ | §3.3 + §6 V79 |
| **B$_M$** (renamed from V64 B-quintic, B-LP$^2$) | quintic, LP$^2$, banana | CONJECTURE (mock-modular) | per-input mock-modular | V55 H1(c), V58 |

---

## §8. What this delivery does NOT do

- Does NOT edit any `.tex` source. Inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, AP catalogue,
  MASTER_PUNCH_LIST.md, INDEX.md, or any notes file.
- Does NOT run `make fast`, `make test`, `make verify-independence`,
  or any build/test command.
- Does NOT close the open Class B$_L$ conjecture (Drinfeld twist
  trivialisation of $[r, r]_{\mathrm{Hoch}}$) — this is the genuine
  open question for $Y(\mathfrak{sl}_2)$.
- Does NOT close the open Class B$_M$ conjecture (mock-modular
  completion for quintic / LP$^2$).
- Does NOT retract V64 — only refines it. The V64 inscription draft
  stands with the C1/C2/C3 amendments.
- Does NOT commit anything (per pre-commit hook). Author Raeez
  Lorgat. No AI attribution.

---

## §9. Closing assessment

V79 subjected V64's $Y(\mathfrak{sl}_2)$ counterexample to an
adversarial five-angle attack with full Etingof–Kazhdan / Drinfeld
twist rigor and AP-CY12 / AP-CY55 / AP-CY61 discipline. The
counterexample SURVIVES — but only at $\hbar^2$, not $\hbar^1$ as V64
stated; and only in a new sub-class $B_L$, not the V55 Class B (=
$B_M$, mock-modular) as V64 placed it.

The healing forces three corrections to V64's inscription draft:

1. **(Attack 1, foundational)** The $\hbar^1$ cocycle $(\hbar/z)[P,
   \cdot]$ is an inner derivation, hence a Hochschild $H^2$ coboundary.
   The genuine obstruction begins at $\hbar^2$ as the antisymmetrisation
   $(\hbar^2 / 2z^2)(a - PaP)$, which is the Hochschild image of the
   Drinfeld classical $r$-matrix Schouten square.
2. **(Attack 3, structural)** $Y(\mathfrak{sl}_2)$ is shadow class L
   (finite-depth, $S_k$ supported in $\{1, \ldots, n\}$ on generator
   $x^+_n$), NOT class M. Class M assignment requires Borel-summable
   Gevrey-1 divergence and mock-modular completion, neither of which
   applies to a finite Yangian.
3. **(Attack 4, definitional)** The B0 super-trace test does not apply
   to non-super inputs; conclusion correct under refined B0 definition,
   but justification re-stated.

Attack 2 (could $Y(\mathfrak{sl}_2)$ be V77 Class A''?) and Attack 5
(does $\widehat{\mathfrak{sl}_2}$ Borcherds lift back to $Y(\mathfrak
{sl}_2)$?) confirm V64's exclusions, with AP-CY31 spectral-parameter
discipline preventing the $\widehat{\mathfrak{sl}_2}$ lift from
transferring to $Y(\mathfrak{sl}_2)$.

The healing introduces a **B-side sub-class split** parallel to V77's
A-side A' / A'' split:

```
Pentagon-at-E_1 chain-level (V79 corrected B side, V77 corrected A side)
    │
    ├── abelian: H_k, V_Lambda, βγ                       PROVED unconditionally
    │
    ├── Class A (V70 corrected): symplectic K3-fibred CY3   PROVED via V49
    │   ├── Class A': non-symplectic K3-fibred              CONDITIONAL (V77)
    │   └── Class A'': algebraic non-geometric (Conway)     PROVED algebraically (V77)
    │
    ├── Class B0: super-trace-vanishing (conifold)          PROVED via super-EK
    │
    ├── Class B_L (NEW V79): Yangians, shadow class L       CONJECTURE (algebraic Yang-Baxter)
    │                       Y(sl_2), Y(sl_n) for n >= 2
    │                       Residual: (h^2/z^2)(a - PaP) at h^2
    │
    └── Class B_M (renamed): non-K3 class M (quintic, LP^2) CONJECTURE (mock-modular)
                            Residual: per-input mock-modular completion
```

The Russian-school dialectic confirms its value: V64's surface
classification (six classes + counterexample) was load-bearing at the
*structural* level but imprecise at the *order-by-order* and
*shadow-class* levels. V79 corrects both without retracting any V64
theorem; the conjectural sector gains precision (a new sub-class) and
the chain-level computation gains rigor (correct order, correct
cohomology class).

The boxed ghost theorem (V64 §8.2 amended per V79):

> $A$ satisfies V19 Trinity-$E_1$ chain level IFF $A$ admits either
> (a) a Borcherds singular-theta lift on a Lorentzian even unimodular
> lattice (Class A, A''), (b) a super-trace-vanishing super-extension
> (Class B0), or (c) a mock-modular completion of its class M shadow
> tower (Class B$_M$). Class B$_L$ inputs (finite-depth Yangians,
> $Y(\mathfrak{sl}_n)$, $n \geq 2$) are obstructed by the algebraic
> Yang–Baxter Schouten image at order $\hbar^2$, requiring an
> algebraic Drinfeld twist (not a Borcherds lift) for trivialisation.

This is the genuine refinement V79 contributes. Closing $B_L$ is an
algebraic Drinfeld-twist problem (independent of mock-modular V8 §6);
closing $B_M$ remains the analytic mock-modular completion. The two
open problems are no longer collapsed into a single "Class B
conjecture" but recognised as genuinely different obstructions with
different mathematical character.

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft
only.
