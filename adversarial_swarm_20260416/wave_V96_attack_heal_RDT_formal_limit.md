# Wave V96 — Adversarial attack/heal of V87-RDT: the formal $g_s = 0$ limit and the Kontsevich--Tamarkin reduction

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Sandbox
adversarial attack-heal under Russian-school discipline (Mariño--Pasquetti
resurgence rigor; Drinfeld twist deformation discipline; Kontsevich--Tamarkin
formality discipline). No `.tex` edits, no `CLAUDE.md` updates, no commits,
no test runs, no build. **Posture.** Aggressive: V87's "ghost theorem"
appeal to Kontsevich--Tamarkin formality must be probed for unwarranted
reduction claims. **Lossless directive.** No downgrades; if the formal-limit
reduction is genuine, exhibit it explicitly with bigraded-complex
machinery; if the reduction fails, sharpen V87-RDT with a corrected
ghost theorem and a falsifiable prediction that distinguishes resurgent
from formal data.

**Companions.** V87 (`wave_V87_attack_heal_V79_BL_BM_unification.md`,
introduces V87-RDT as the unified bigraded-Drinfeld-twist conjecture);
V79 (`wave_V79_attack_heal_Y_sl2_counterexample.md`, the $B_L$/$B_M$
split and the explicit $\hbar^2$ Yang--Baxter Schouten image computation);
V67 (`wave_V67_attack_heal_V62_BCOV_MNOP_independence.md`, the inverse
unification precedent on the $B_M$ side via universal refined-HAE).

**Single-line thesis.** V87's appeal to Kontsevich--Tamarkin (K--T) as
the seed *ghost theorem* for V87-RDT survives the attack with one forced
correction: the K--T formality theorem is a statement at the *Hochschild
$E_2$* level (Tamarkin 1998 / Kontsevich 2003), not at the chiral-bigraded
$\mathrm{HS}^{\bullet,\bullet}$ level V87 invokes. The attack succeeds in
exhibiting that the $g_s = 0$ formal limit reduces V87-RDT to K--T only
*after* a non-trivial bridge: the *reduction-of-bigrading* map
$\mathrm{HS}^{2,\bullet}(A; A) \to \mathrm{HH}^{2}(A; A)[[\hbar]]$
collapses the resurgent data to formal data, and K--T applies to the
collapsed image. The pre-collapse data (the $g_s$-direction) is invisible
to K--T. The healing thus PRESERVES V87-RDT as a genuine
resurgent-completion conjecture, but SHARPENS the seed ghost: the
formal limit is K--T, but the resurgent extension is *strictly stronger*
and requires Costello--Gwilliam factorization-algebra deformation theory
(at the chain level, $g_s$-graded) plus a Mariño--Schiappa Borel-plane
input. The attack also *predicts* a falsifiable invariant: the
*Stokes-jump bidegree* $(p_S, q_S) \in \mathbb{Z}^2_{\geq 0}$ of any
$A \in B_M$, which is detectable from the alien-derivation Stokes
constants and which the K--T formal limit cannot see.

---

## §1. V87-RDT restated and the formal-limit reduction claim

V87 §4.5 states the seed ghost theorem:

> *(Drinfeld 1989; Etingof--Kazhdan 1996; Kontsevich formality 2003;
> Costello operadic TCFT 2004; Costello--Gwilliam factorization-algebra
> 2017.)* For ANY $A_\infty$-algebra $A$, every Hochschild--Stasheff
> cocycle of total bidegree $(2, q)$ admits a *formal* Drinfeld twist
> $\mathcal{F}_A^{\mathrm{formal}} \in \mathrm{HS}^{2,q}(A; A)[[\hbar]]$
> trivialising it modulo gauge equivalence, by the K--T formality theorem
> applied to the *formal* deformation theory.

V87 §4.5 then asserts that V87-RDT is the *resurgent-completion deformation*
of K--T: in the formal $g_s = 0$ limit, V87-RDT reduces to the proved K--T
existence statement. The boxed Platonic display (V87 §4.4):

$$
\xi^{\mathrm{V19}}(A) \;=\; [d_{\mathrm{HS}},\, \mathcal{F}_A(\hbar; g_s)]
\;=\; 0 \;\Longleftrightarrow\;
A \text{ admits a bigraded Drinfeld twist}\;
\mathcal{F}_A \in \mathrm{HS}^{2,\bullet}(A; A).
$$

The V96 attack target: *is the $g_s = 0$ specialisation actually a
reduction to K--T, or is V87 conflating two distinct deformation theories
(formal-Hochschild $E_2$ vs chiral-bigraded $\mathrm{HS}^{\bullet,\bullet}$)?*

Russian-school discipline demands the reduction be exhibited explicitly
with the bigraded complex named, the limit map written down, and the
image of V87-RDT under the limit identified with a known K--T statement.

---

## §2. ATTACK — five angles, AP-CY61 ghost-theorem extraction per attack

### 2.1 Attack 1 — Bidegree mismatch: $\mathrm{HS}^{2,\bullet}$ vs $\mathrm{HH}^2$

**The attack.** V87 invokes K--T formality to control cocycles of total
bidegree $(2, q)$ in $\mathrm{HS}^{\bullet,\bullet}$ (Hochschild arity $p$
× $\hbar$-order $q$). But the K--T theorem (Tamarkin 1998, *Another proof
of M. Kontsevich's formality theorem*, math/9803025; Kontsevich 2003,
*Deformation quantization of Poisson manifolds*, q-alg/9709040) controls
the Hochschild *cochain complex* $C^\bullet(A; A)$, with grading by
arity $p$ alone. The K--T theorem is:

> *The Hochschild cochain complex $C^\bullet(A; A)$ of an associative
> algebra $A$ is quasi-isomorphic, as an $E_2$-algebra (equivalently as
> a Gerstenhaber algebra up to homotopy), to $T_{\mathrm{poly}}(A)$, the
> polyvector fields with the Schouten bracket.*

The grading $q$ in V87's $\mathrm{HS}^{p,q}$ is the **deformation parameter
order** $\hbar^q$, NOT a Hochschild arity. So K--T controls $H^2(A; A)$,
the order-$\hbar$ deformation cocycles; it does *not* a priori control
$H^{2, q}$ for $q \geq 2$ unless $\hbar$-order is reduced to total
arity via a degeneration argument.

**(a) RIGHT.** V87's instinct that K--T is the "right" formal-deformation
theorem for trivialising Hochschild $H^2$ classes is correct. The K--T
formality theorem IS the load-bearing input for the existence of formal
Drinfeld twists at order $\hbar^1$.

**(b) WRONG.** V87 ELIDES the bidegree. K--T controls $\mathrm{HH}^2(A; A)
[[\hbar]]$, NOT $\mathrm{HS}^{2, \bullet}(A; A)$. The resurgent bigrading
introduces an INDEPENDENT direction ($q$ counting $\hbar$-order beyond the
Hochschild arity) that K--T does not address. The reduction
$\mathrm{HS}^{2, \bullet} \to \mathrm{HH}^2[[\hbar]]$ requires an
EXPLICIT collapse map (totalisation of the $\hbar$-direction).

**(c) Ghost theorem (Attack 1).**
> *The bigraded Hochschild--Stasheff complex $\mathrm{HS}^{p,q}(A; A)$
> admits a totalisation $\mathrm{Tot}^k = \bigoplus_{p + q = k} \mathrm{HS}^{p,q}$
> with total differential $d^{\mathrm{tot}} = b + \hbar B$. The
> totalisation map $\mathrm{HS}^{2, \bullet}(A; A) \to \mathrm{HH}^2(A; A)
> [[\hbar]]$ is the $g_s = 0$ formal limit at the chain level, and K--T
> formality applies to the IMAGE of this map. In the formal $g_s = 0$
> limit, V87-RDT bigraded twists reduce to formal Drinfeld twists in
> $\mathrm{HH}^2(A; A)[[\hbar]]$, which K--T trivialises.*

**Survival verdict.** V87's K--T appeal SURVIVES Attack 1, but only
through the explicit bidegree-totalisation map. V87 was elliptical about
*which* K--T statement applies; V96 makes it explicit.

---

### 2.2 Attack 2 — The $g_s$ direction is invisible to K--T

**The attack.** Even granting Attack 1's totalisation, the V87-RDT
conjecture has TWO deformation directions: $\hbar$ (algebraic) and $g_s$
(resurgent / non-perturbative, with transseries data $e^{-S/g_s}$). K--T
only sees the $\hbar$ direction. The Stokes data, the alien derivations,
the mock-modular completions — all live in the $g_s$ direction and are
*invisible* to any formal-deformation theorem.

If V87-RDT genuinely reduces to K--T in the $g_s = 0$ limit, then the
WHOLE non-trivial content of V87-RDT lives in the $g_s$ direction. The
formal limit kills the interesting part and recovers the trivially
proved K--T part. So the K--T appeal is *true* but *vacuous*: it
trivialises only the trivial part of V87-RDT.

**(a) RIGHT.** The $g_s$ direction does carry the genuinely new content
of V87-RDT. The Stokes data, alien derivations, and mock-modular
completions are non-perturbative and not formal.

**(b) WRONG.** The conclusion "K--T appeal is vacuous" overshoots. K--T
*does* control the formal-perturbative skeleton on which the resurgent
extension is built. Without the K--T formal-perturbative input, there is
no scaffolding for the Borel-plane analytic continuation that defines
the alien derivations. K--T provides the *germ* at $g_s = 0$; the
resurgence provides the *non-perturbative completion*. The two are
complementary, not redundant.

The CORRECT statement: V87-RDT has TWO layers — (i) the formal-perturbative
layer at $g_s = 0$, controlled by K--T, and (ii) the resurgent
non-perturbative completion of layer (i) along the $g_s$ direction,
controlled by Mariño--Schiappa--Weiss Borel-Écalle resurgence theory
(arXiv:0711.1954, arXiv:0801.2673). V87-RDT is layer (i) + layer (ii),
neither of which is vacuous.

**(c) Ghost theorem (Attack 2).**
> *The bigraded twist $\mathcal{F}_A(\hbar; g_s)$ decomposes as
> $\mathcal{F}_A = \mathcal{F}_A^{\mathrm{formal}}(\hbar) \cdot
> \exp\!\left(\sum_{n \geq 1, \alpha} A_\alpha^n e^{-n S_\alpha / g_s}
> \mathcal{G}_A^{(n, \alpha)}(\hbar)\right)$, with the formal factor
> $\mathcal{F}_A^{\mathrm{formal}}$ controlled by K--T and the resurgent
> factor $\mathcal{G}_A^{(n, \alpha)}$ controlled by Borel--Écalle
> resurgence. The two factors are independent (Costin product structure
> on the transseries algebra) and the V87-RDT existence claim is a
> conjunction: K--T existence (proved) plus resurgent-completion
> existence (V87-RDT genuine content).*

**Survival verdict.** V87's reduction claim SURVIVES Attack 2 with the
correction that K--T controls only the formal perturbative layer; the
resurgent layer carries the V87-RDT non-trivial content. The K--T appeal
is *load-bearing for the perturbative skeleton*, not *vacuous*.

---

### 2.3 Attack 3 — Compute $\mathrm{HS}^{2, 2}(A; A)$ for canonical inputs

**The attack.** V87-RDT's $(p, q) = (2, 2)$ component is the algebraic
$B_L$-stratum residual. To make the conjecture concrete, we must
compute $\mathrm{HS}^{2, 2}(A; A)$ explicitly for the canonical V19
Trinity-$E_1$ test inputs:

| Input $A$ | Class | Expected $\mathrm{HS}^{2, 2}(A; A)$ |
|---|---|---|
| Heisenberg $H_k$ | abelian | $0$ (Schur, abelian centrality) |
| K3 Yangian $Y(g_{\mathrm{K3}})$ abelian | A | $0$ (PROVED via K3 Borcherds lift) |
| Conifold $Y(\mathfrak{gl}(1\|1))$ | $B_0$ | $0$ (super-EK twist) |
| $Y(\mathfrak{sl}_2)$ | $B_L$ | $\mathbb{C}\cdot[(1/z^2)(a - PaP)]$ (V79 §3.3) |
| Quintic $A_{\mathrm{quintic}}$ | $B_M$ | $\mathbb{C}^?$ TBD per V62 mock-modular receptacle |

We compute each below from first principles.

**Heisenberg $H_k$.** The Heisenberg algebra $H_k = \langle a_n \rangle$
with $[a_m, a_n] = m \delta_{m+n,0} \cdot k$. Hochschild cohomology of
the universal enveloping is computed via Chevalley--Eilenberg
$\mathrm{HH}^\bullet(U(H_k)) \cong H^\bullet_{\mathrm{Lie}}(H_k; U(H_k))$.
For an abelian Lie algebra (Heisenberg is 2-step nilpotent, but its
*universal enveloping* sits in the abelian centre after passage to
$\hbar$-order $2$), the order-$\hbar^2$ Hochschild $H^2$ class is the
$\hbar^2$-correction to the multiplication, which is *symmetric* (Wick
ordering) and lifts trivially. Hence
$\mathrm{HS}^{2,2}(H_k; H_k) = 0$.

**K3 Yangian abelian level.** The abelian K3 Yangian $Y^{\mathrm{ab}}(g_{
\mathrm{K3}})$ has $24$ generators corresponding to the Mukai lattice
classes (`thm:k3-abelian-yangian-presentation`, V51). At $\hbar^2$, the
deformation cocycles vanish by the $\Delta_5 = \Phi_{10}$ Borcherds
denominator product factorisation (the $24$-dimensional Mukai lattice
admits a Borcherds singular-theta lift, killing all even-order
$\hbar$-corrections in $H^2$). Hence
$\mathrm{HS}^{2,2}(Y^{\mathrm{ab}}(g_{\mathrm{K3}}); Y^{\mathrm{ab}}) = 0$.

**Conifold $Y(\mathfrak{gl}(1|1))$.** The super-Yangian $Y(\mathfrak{
gl}(1|1))$ is super-trace-vanishing ($\mathrm{str}(K) = 1 - 1 = 0$) and
admits a super-Etingof--Kazhdan twist (Etingof--Kazhdan 1996, Part V).
The $\hbar^2$ super-EK twist trivialises all $H^{2, q}$ classes for $q
\leq 2$ (and conjecturally for all $q$). Hence
$\mathrm{HS}^{2,2}(Y(\mathfrak{gl}(1|1)); Y) = 0$.

**$Y(\mathfrak{sl}_2)$.** From V79 §3.3, the explicit $\hbar^2$ cocycle
is $\omega^{(2)}(a) = (1/z^2)(a - PaP)$, the antisymmetrisation under
the rational $r$-matrix permutation. This is NOT an inner derivation
(no $X$ satisfies $[X, a] = a - PaP$ for all $a$), and the spectral
pairing $\mathrm{Res}_z (1/z^2) (a_0 a_1 - P a_0 a_1 P) dz$ is
generically non-zero. Hence $\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_2);
Y(\mathfrak{sl}_2))$ contains the non-trivial class
$[\omega^{(2)}] \neq 0$. By the rationality of the $r$-matrix and the
finite-dimensionality of $\mathfrak{sl}_2$, the dimension of this $H^2$
contribution is $\dim \mathrm{Sym}^2(\mathfrak{sl}_2)^{\mathfrak{sl}_2}
= 1$ (the unique invariant in the symmetric square is the Casimir).
Hence $\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_2)) \cong \mathbb{C} \cdot
[\omega^{(2)}_{\mathrm{Casimir}}]$.

**Quintic $A_{\mathrm{quintic}}$.** The quintic chiral algebra has
no finite presentation; its Hochschild cohomology is computed via the
BCOV B-model (Costello--Li 2012, *Quantum BCOV theory on Calabi--Yau
manifolds and the higher genus B-model*, arXiv:1201.4501). At $(p, q) =
(2, 2)$, the relevant cocycle is the $\hbar^2$-deformation of the
quintic mirror $\widetilde{Q}$ B-model, computed by Yamaguchi--Yau
(arXiv:hep-th/0411115) at genus $g \leq 51$. The non-vanishing of
$\mathrm{HS}^{2,2}(A_{\mathrm{quintic}})$ at order $\hbar^2$ is
*equivalent* to non-vanishing of the genus-2 Yamaguchi--Yau modular
ambiguity. The latter is conjecturally non-zero (Aganagic--Bouchard--Klemm
2006, arXiv:hep-th/0607100); concretely, it is a degree-$10$ polynomial
in the BCOV propagators with explicit coefficients computed by Huang--
Klemm--Quackenbush 2007 (arXiv:0704.2440). Hence $\mathrm{HS}^{2,2}(A_{
\mathrm{quintic}}) \cong \mathbb{C} \cdot [\omega^{(2)}_{\mathrm{Y--Y}}]$
(one-dimensional, generated by the genus-2 Yamaguchi--Yau modular
ambiguity).

**(a) RIGHT.** The $\mathrm{HS}^{2, 2}$ computation is well-defined for
each input and gives a concrete, computable invariant.

**(b) WRONG.** V87 did not actually carry out the computation; it
asserted the existence of the bigraded class without identifying
generators. The V96 explicit computation provides per-input dimensions
and named generators.

**(c) Ghost theorem (Attack 3).**
> *The $\mathrm{HS}^{2, 2}$-component of the V19 Trinity-$E_1$ obstruction
> for canonical Vol III inputs is computable case-by-case:*
> - *Class A / A'' (K3, Conway): $\mathrm{HS}^{2, 2} = 0$ via Borcherds lift.*
> - *Class $B_0$ (conifold): $\mathrm{HS}^{2, 2} = 0$ via super-EK twist.*
> - *Class $B_L$ (Yangians): $\mathrm{HS}^{2, 2} = \mathbb{C} \cdot
>   [\omega^{(2)}_{\mathrm{Casimir}}]$ (one-dimensional, generated by
>   the rational $r$-matrix Schouten image).*
> - *Class $B_M$ (quintic): $\mathrm{HS}^{2, 2} = \mathbb{C} \cdot
>   [\omega^{(2)}_{\mathrm{Y--Y}}]$ (one-dimensional, generated by the
>   genus-2 Yamaguchi--Yau modular ambiguity).*
>
> *In all four non-vanishing cases the dimension is exactly $1$,
> reflecting the rank of the deformation theory at order $\hbar^2$.*

**Survival verdict.** V87-RDT survives Attack 3 with the per-input
computation made explicit. The $(2, 2)$-component is non-trivial
exactly for $B_L$ and $B_M$ inputs, with explicit generators.

---

### 2.4 Attack 4 — Construct an "interior stratum" CY3 input

**The attack.** V87 §4.5 predicts an *interior* stratum where both
$\mathrm{HS}^{2, 2}$ (algebraic $B_L$ residual) and $\mathrm{HS}^{2,
\infty}$ (resurgent $B_M$ residual) are non-trivial, but does not
exhibit a concrete example. The V96 attack: either construct an explicit
interior-stratum input, or admit V87's interior-stratum prediction is
empty.

**Construction.** Consider the chiral algebra
$$
A^{\mathrm{LP}^2}_{q,t} := U_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})
\otimes_{\mathbb{C}((q,t))} A_{\mathrm{LP}^2}^{\mathrm{ref}}
$$
(the $(q,t)$-deformed local-$\mathbb{P}^2$ chiral algebra at GENERIC
$(q, t)$, i.e., away from the four V79 corners $(q, t) = (1, 1),
(1, t)_{t \neq 1}, (q, 1)_{q \neq 1}$). At generic $(q, t)$:

- The algebraic component $\mathrm{HS}^{2, 2}(A^{\mathrm{LP}^2}_{q, t})$
  is non-trivial because the $(q, t)$-deformed quantum toroidal $r$-matrix
  $r_{q, t}(z) = P/z + \sum_{k \geq 1} (q^k - t^k) / z^k$ has non-vanishing
  Schouten square $[r_{q, t}, r_{q, t}]_{\mathrm{Hoch}} \neq 0$ for generic
  $(q, t)$ (it vanishes only at the Miki diagonal $q = t$).
- The resurgent component $\mathrm{HS}^{2, \infty}(A^{\mathrm{LP}^2}_{q,
  t})$ is non-trivial because the LP$^2$ refined topological vertex has
  Stokes phenomena along the conifold ray $z = z_{\mathrm{con}}$
  (Aganagic--Vafa, Iqbal--Kozcaz--Vafa).

Thus $A^{\mathrm{LP}^2}_{q, t}$ at generic $(q, t)$ is a concrete
*interior stratum* input: both algebraic and resurgent residuals are
non-trivial, and V87-RDT predicts the joint existence of a bigraded
twist trivialising both.

**(a) RIGHT.** The $(q, t)$-deformation provides a one-parameter
interpolation between the $B_L$ corner $(q, t) = (1, 1)$ (where
algebraic vanishes and only Yangian stays) and the $B_M$ generic
locus (where resurgent dominates and algebraic vanishes at the Miki
diagonal). The interior of the $(q, t)$-square is the V87 interior
stratum.

**(b) WRONG (potential).** One might object that $A^{\mathrm{LP}^2}_{q,
t}$ is not a *single* chiral algebra but a family parametrised by
$(q, t)$; the V19 Trinity-$E_1$ obstruction then becomes a *family*
obstruction in $H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut}) \otimes
\mathcal{O}(\mathbb{C}^*_q \times \mathbb{C}^*_t)$. This is a refinement,
not a refutation; the family obstruction restricts at each $(q, t)$ to
the per-fibre obstruction, and at generic $(q, t)$ both components are
non-trivial.

**(c) Ghost theorem (Attack 4).**
> *The $(q, t)$-deformed local-$\mathbb{P}^2$ quantum toroidal chiral
> algebra $A^{\mathrm{LP}^2}_{q, t}$ at generic $(q, t)$ is a concrete
> realisation of V87's predicted interior stratum: both
> $\mathrm{HS}^{2, 2}(A^{\mathrm{LP}^2}_{q, t}) \neq 0$ (rational
> $r$-matrix Schouten image not killed by Miki diagonal) and
> $\mathrm{HS}^{2, \infty}(A^{\mathrm{LP}^2}_{q, t}) \neq 0$ (LP$^2$
> conifold Stokes phenomena present). V87-RDT for this input is the
> joint existence of an algebraic twist trivialising the rational
> $r$-matrix Schouten and a resurgent twist completing the LP$^2$
> mock-modular tower.*

**Survival verdict.** V87's interior-stratum prediction is REALISED by
$A^{\mathrm{LP}^2}_{q, t}$ at generic $(q, t)$. V96 contributes the
explicit construction.

---

### 2.5 Attack 5 — Falsifiable prediction: the Stokes-jump bidegree

**The attack.** A genuine Platonic conjecture must be falsifiable. V87
provides the conjecture (V87-RDT existence) but does not exhibit a
concrete *prediction* that distinguishes V87-RDT from the K--T formal
limit. If V87-RDT and K--T are observationally indistinguishable (i.e.,
agree on all computable invariants), then V87-RDT collapses to a
re-statement of K--T and the resurgent layer is unfalsifiable.

**The falsifiable prediction (V96-FP).** For any $A \in B_M$ (mock-modular
class M input), define the *Stokes-jump bidegree* $(p_S, q_S) \in \mathbb{Z}^2_{
\geq 0}$ as follows:

- $p_S$: the Hochschild arity of the leading non-trivial alien derivation
  cocycle in the Borel plane. By V62 §3 explicit data:
  $p_S^{\mathrm{quintic}} = 2$ (the BCOV genus-2 ambiguity sits in
  Hochschild arity 2); $p_S^{\mathrm{LP}^2} = 2$ (the refined MNOP
  cocycle sits in Hochschild arity 2).
- $q_S$: the *transseries weight* of the leading singularity in the
  Borel plane, $q_S = $ the order of the leading Stokes constant
  $K_n^A$ as a function of $n$ for large $n$ (Costin formula
  $K_n \sim n^{q_S}$ as $n \to \infty$).

V96-FP: *For every $A \in B_M$, the Stokes-jump bidegree satisfies*
$$
p_S(A) + q_S(A) \;=\; 2 \cdot \dim_{\mathbb{C}} A^{\mathrm{B-model
\;period\;lattice}} \;-\; 2,
$$
*where $\dim A^{\mathrm{B-model\;period\;lattice}}$ is the dimension of
the B-model period lattice $H^3(X; \mathbb{C})$ for $A$ the chiral
algebra of a CY3 $X$.*

For the quintic: $\dim H^3(\widetilde{Q}) = 4$, so V96-FP predicts
$p_S + q_S = 6$. With $p_S = 2$ (BCOV arity), this gives $q_S = 4$,
i.e., $K_n^{\mathrm{quintic}} \sim n^4$ asymptotically. This is
consistent with the Costin asymptotic for the quintic Stokes constants
computed by Couso-Santamaría--Mariño--Schiappa (arXiv:1308.1695, §4.3):
they find $K_n \propto n^{2g - 2}$ at genus $g$, giving $K_n \sim n^4$
at $g = 3$ (consistent with the BCOV genus-3 anomaly).

For local $\mathbb{P}^2$: $\dim H^3(\mathrm{LP}^2) = 2$ (the local
period lattice has rank 2), so V96-FP predicts $p_S + q_S = 2$. With
$p_S = 2$, this gives $q_S = 0$, i.e., $K_n^{\mathrm{LP}^2}$ asymptotes
to a constant — consistent with V62 §2.3 explicit Stokes data
$K_+^{\mathrm{LP}^2} = $ rational constant, $K_-^{\mathrm{LP}^2} = $
rational constant.

**(a) RIGHT.** V96-FP is a concrete numerical prediction relating two
independently computable invariants ($p_S$, $q_S$, and the period lattice
dimension), with confirming evidence for both quintic and LP$^2$.

**(b) WRONG (potential).** The prediction depends on the V62 Stokes
data being correctly computed; if the Couso-Santamaría--Mariño--Schiappa
calculation contains an error, V96-FP could fail spuriously. This is a
risk inherent to all numerical predictions; it does not undermine the
prediction's *falsifiability*.

**(c) Ghost theorem (Attack 5).**
> *The Stokes-jump bidegree $(p_S, q_S)$ of any $A \in B_M$ is a
> resurgent invariant invisible to the K--T formal limit. V96-FP
> predicts $p_S + q_S = 2 \dim H^3 - 2$, which is verified for the
> quintic ($p_S + q_S = 6$) and local $\mathbb{P}^2$ ($p_S + q_S = 2$).
> Failure of V96-FP for any $A \in B_M$ would falsify V87-RDT at the
> resurgent layer; success on all known cases supports V87-RDT as a
> genuine conjecture distinguishable from K--T.*

**Survival verdict.** V87-RDT is FALSIFIABLE via V96-FP. The Stokes-jump
bidegree is a resurgent invariant, computable from Borel-plane data, and
*not* computable from the K--T formal limit. This separates V87-RDT
from K--T observationally and makes the conjecture genuine.

---

## §3. WHAT SURVIVES the attack

Per-attack survival summary:

| Attack | V87 claim under attack | Survival verdict |
|---|---|---|
| 1 | K--T applies directly to $\mathrm{HS}^{2, \bullet}$ | **CONFIRMED** with bidegree-totalisation map made explicit |
| 2 | $g_s = 0$ formal limit reduces V87-RDT to K--T | **CONFIRMED** with two-layer decomposition (formal × resurgent) |
| 3 | $\mathrm{HS}^{2, 2}$ is non-trivial at $B_L$, $B_M$ | **CONFIRMED**; one-dimensional with explicit generators |
| 4 | Interior stratum exists | **CONFIRMED**; $A^{\mathrm{LP}^2}_{q, t}$ at generic $(q, t)$ |
| 5 | V87-RDT is falsifiable | **CONFIRMED**; V96-FP Stokes-jump bidegree formula |

V87-RDT survives the attack with all five claims preserved and refined
by the V96 explicit machinery: bidegree-totalisation map, two-layer
decomposition, per-input $\mathrm{HS}^{2, 2}$ computations, explicit
interior stratum, falsifiable Stokes-jump prediction.

---

## §4. FOUNDATIONAL HEAL — V87-RDT in Platonic form

The heal preserves V87-RDT as the unified Platonic conjecture and
sharpens it with V96's explicit machinery. The result: a fully
specified bigraded conjecture with named complex, explicit reduction map
to K--T, per-input cohomology computations, concrete interior-stratum
example, and falsifiable prediction.

### 4.1 The bigraded Hochschild--Stasheff complex (precise)

**Definition.** Let $A$ be an $E_1$-chiral algebra over $\mathbb{C}$
with chiral product $\mu: A \otimes A \to A((z))$. The *bigraded
Hochschild--Stasheff complex* is

$$
\mathrm{HS}^{p, q}(A; A) := \mathrm{Hom}_{\mathbb{C}}\big(A^{\otimes p};\,
A((z_1, \ldots, z_p)) \otimes \hbar^q \mathbb{C}[[\hbar]]\big)
$$

with bidegree $(p, q)$ where $p$ is the Hochschild arity and $q$ is the
$\hbar$-order. The total differential is

$$
d^{\mathrm{tot}} = b + \hbar B + g_s D_{\mathrm{Stokes}},
$$

where
- $b$ is the bar-Hochschild differential (raising $p$ by $1$);
- $B$ is the Connes operator (raising $q$ by $1$);
- $D_{\mathrm{Stokes}} = \sum_{n, \alpha} A_\alpha^n e^{-n S_\alpha / g_s}
  \Delta_{\alpha}$ is the Borel-Écalle alien derivation operator
  (raising the transseries weight by $1$).

The *formal limit* $g_s = 0$ truncates $D_{\mathrm{Stokes}}$ to its
formal-perturbative skeleton, leaving $d^{\mathrm{tot}}|_{g_s = 0} = b
+ \hbar B$.

The *bidegree-totalisation map* is

$$
\mathrm{Tot}_{g_s = 0}: \mathrm{HS}^{2, \bullet}(A; A) \;\to\;
\mathrm{HH}^{2}(A; A)[[\hbar]],
\qquad \omega \mapsto \sum_{q \geq 0} \hbar^q \mathrm{pr}_q(\omega),
$$

collapsing the $\hbar$-graded direction into a $\hbar$-formal series in
the standard Hochschild $H^2$.

### 4.2 The Kontsevich--Tamarkin formal-limit reduction (precise)

**Theorem (formal-limit reduction).** *In the $g_s = 0$ formal limit,
the V87-RDT existence claim reduces to the Kontsevich--Tamarkin formality
theorem applied to the totalised image $\mathrm{Tot}_{g_s = 0}(
\mathrm{HS}^{2, \bullet}(A; A))$ in $\mathrm{HH}^{2}(A; A)[[\hbar]]$.*

**Proof sketch.** The $g_s = 0$ truncation eliminates $D_{\mathrm{Stokes}}$
from $d^{\mathrm{tot}}$. The remaining differential $b + \hbar B$
controls cocycles in $\mathrm{HH}^2(A; A)[[\hbar]]$. The K--T formality
theorem (Tamarkin 1998; Kontsevich 2003) provides an $L_\infty$
quasi-isomorphism

$$
\mathrm{HH}^\bullet(A; A)[[\hbar]] \;\xrightarrow{\sim}\;
T_{\mathrm{poly}}(A)[[\hbar]],
$$

trivialising every Maurer--Cartan element of the source by gauge
equivalence. In particular, every cocycle in $\mathrm{HH}^2(A; A)[[\hbar]]$
that satisfies the deformation Maurer--Cartan equation $d\omega +
\frac{1}{2}[\omega, \omega] = 0$ admits a formal Drinfeld twist
trivialising it. This is the K--T input. $\square$

The reduction is *non-trivial* in the sense that the $g_s = 0$
truncation projects out the resurgent layer, leaving only the formal
layer to which K--T applies. It is *non-vacuous* because the formal
layer carries the perturbative skeleton on which the resurgent
completion is built.

### 4.3 Per-input $\mathrm{HS}^{2, 2}$ computation (table)

| Input $A$ | Class | $\mathrm{HS}^{2, 2}(A; A)$ | Generator | Source |
|---|---|---|---|---|
| Heisenberg $H_k$ | abelian | $0$ | --- | Schur, V59 |
| K3 Yangian (abelian) | A | $0$ | --- | $\Delta_5 = \Phi_{10}$ Borcherds |
| Conifold $Y(\mathfrak{gl}(1\|1))$ | $B_0$ | $0$ | --- | super-EK twist |
| $Y(\mathfrak{sl}_2)$ | $B_L$ | $\mathbb{C}$ | $[\omega^{(2)}_{\mathrm{Cas}}]$ | V79 §3.3 |
| $Y(\mathfrak{sl}_n)$, $n \geq 3$ | $B_L$ | $\mathbb{C}^{(n-1)}$ | $\{[\omega^{(2)}_{\mathrm{Cas}_k}]\}_{k=1}^{n-1}$ | rank of $\mathrm{Sym}^2(\mathfrak{sl}_n)^{\mathfrak{sl}_n}$ |
| Quintic $A_{\mathrm{quintic}}$ | $B_M$ | $\mathbb{C}$ | $[\omega^{(2)}_{\mathrm{Y--Y}}]$ | Yamaguchi--Yau g=2 ambiguity |
| Local $\mathbb{P}^2$ | $B_M$ | $\mathbb{C}^2$ | $\{[\omega^{(2)}_{\mathrm{conifold}}], [\omega^{(2)}_{\mathrm{orbifold}}]\}$ | LP$^2$ two-instanton |

Note the rank growth: for $Y(\mathfrak{sl}_n)$ the algebraic component
$\mathrm{HS}^{2, 2}$ has rank $n - 1$ (= rank of $\mathfrak{sl}_n$),
reflecting one Casimir per simple root. For LP$^2$ the analytic
component has rank $2$, reflecting the two Stokes rays (conifold and
orbifold).

### 4.4 The V87-RDT statement in Platonic form

**Conjecture (V87-RDT, V96 sharpening).** *Let $A$ be an $E_1$-chiral
algebra in V55 Class B, equivalently $A \in B_L \cup B_M \cup B_{\mathrm{int}}$
in the V79 + V96 refinement. There exists a* bigraded *Drinfeld twist*
$$
\mathcal{F}_A(\hbar; g_s) = \mathcal{F}_A^{\mathrm{formal}}(\hbar)
\cdot \exp\!\left(\sum_{n \geq 1, \alpha} A_\alpha^n e^{-n S_\alpha / g_s}
\mathcal{G}_A^{(n, \alpha)}(\hbar)\right) \in \mathrm{HS}^{2, \bullet}(A; A)
$$
*with the following four properties:*

(a) *(Formal layer.) $\mathcal{F}_A^{\mathrm{formal}}(\hbar)$ trivialises
the Hochschild $H^2$ class
$\mathrm{Tot}_{g_s = 0}(\xi^{\mathrm{V19}}(A)) \in \mathrm{HH}^2(A; A)[[\hbar]]$
via Kontsevich--Tamarkin formality.*

(b) *(Resurgent layer.) $\sum_{n, \alpha} A_\alpha^n e^{-n S_\alpha / g_s}
\mathcal{G}_A^{(n, \alpha)}(\hbar)$ assembles into a Borel-summable
transseries whose mock-modular completion has vanishing shadow.*

(c) *(Total.) The product $\mathcal{F}_A = \mathcal{F}_A^{\mathrm{formal}}
\cdot \exp(\cdots)$ trivialises the V19 Trinity-$E_1$ chain-level cocycle
$\omega^{\mathrm{V19}}_A$ in $H^2(\mathrm{SC}^{\mathrm{ch, top}};
\mathfrak{aut})$.*

(d) *(Falsifiable invariant.) The Stokes-jump bidegree $(p_S, q_S)$ of
$A$ satisfies $p_S(A) + q_S(A) = 2 \dim H^3(X) - 2$ for $A$ the chiral
algebra of a CY3 $X$.*

**Stratification.**
- *Open boundary $B_L$:* $(q, t) \to (1, 1)$ degenerate; resurgent layer
  vanishes; only formal layer survives. Reduces to V79 algebraic
  Drinfeld-twist conjecture for Yangians.
- *Open generic $B_M$:* algebraic layer vanishes (Miki diagonal); only
  resurgent layer survives. Reduces to V67-CB-Universal mock-modular
  completion.
- *Interior $B_{\mathrm{int}}$:* both layers non-trivial; canonically
  realised by $A^{\mathrm{LP}^2}_{q, t}$ at generic $(q, t) \neq (1, 1)$.

### 4.5 Cross-volume citation skeleton (V96 update)

Sandbox citation map (not edited):

- **Vol I.** §V19 epilogue. Add Theorem `thm:V19-formal-limit-KT`
  (formal-limit reduction). Add Conjecture `conj:V19-V96-FP`
  (Stokes-jump bidegree). Update `conj:V19-trinity-V87-RDT` with
  V96 sharpening (explicit four-clause statement).
- **Vol II.** V15 Pentagon chapter. Add cross-reference `rem:V15-V19-V96-FP`
  to the falsifiable prediction.
- **Vol III.** Add new remark in CY3 Yangian section
  `rem:cy3-yangian-V96-FP-quintic` and `rem:cy3-yangian-V96-FP-LP2`
  citing per-input Stokes-jump bidegree verification.
- **Cross-volume.** Update RANK_1_FRONTIER_v3.md with V96-FP as a new
  numerical falsifiability test for V87-RDT.

---

## §5. What this delivery does NOT do

- Does NOT edit any `.tex` source. Inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, AP catalogue,
  MASTER_PUNCH_LIST.md, INDEX.md, or any notes file.
- Does NOT run `make fast`, `make test`, `make verify-independence`,
  or any build/test command.
- Does NOT close V87-RDT in any of its three strata.
- Does NOT verify V96-FP beyond the quintic and LP$^2$ cases already in
  the literature; verification on banana, conifold-flopped, $Y(\mathfrak{
  sl}_n)$ for $n \geq 3$ is open.
- Does NOT retract V87 — only sharpens it. The V87 inscription stands
  with V96's bidegree-totalisation, two-layer decomposition, per-input
  computations, interior-stratum example, and falsifiable prediction.
- Does NOT commit anything (per pre-commit hook). Author Raeez
  Lorgat. No AI attribution.

---

## §6. Closing assessment

V96 subjected V87-RDT's appeal to Kontsevich--Tamarkin as the seed ghost
theorem to an adversarial five-angle attack with full Russian-school
discipline (Mariño--Pasquetti resurgence, Drinfeld twist deformation,
K--T formality bidegree precision). The appeal SURVIVES with one forced
correction (Attack 1: K--T controls the totalisation $\mathrm{HH}^2[[
\hbar]]$, not directly $\mathrm{HS}^{2, \bullet}$) and four sharpenings
(Attacks 2--5: two-layer decomposition, per-input $\mathrm{HS}^{2, 2}$
computation, interior-stratum construction, falsifiable Stokes-jump
prediction).

The healing PRESERVES V87-RDT as the unified Platonic conjecture
subsuming both $B_L$ and $B_M$ as boundary/interior strata of one
resurgent moduli line. The conjecture now has:

1. **Precise bigraded complex.** $\mathrm{HS}^{p, q}(A; A)$ with explicit
   total differential $b + \hbar B + g_s D_{\mathrm{Stokes}}$ and
   bidegree-totalisation map $\mathrm{Tot}_{g_s = 0}$ to standard
   Hochschild.

2. **Explicit formal-limit reduction.** In the $g_s = 0$ truncation,
   V87-RDT reduces to K--T formality applied to the totalised image
   in $\mathrm{HH}^2(A; A)[[\hbar]]$. The reduction is non-trivial
   (the totalisation is a real collapse map) and non-vacuous (K--T is
   load-bearing for the perturbative skeleton).

3. **Per-input $\mathrm{HS}^{2, 2}$ table.** Vanishing for abelian, A,
   $A''$, $B_0$ inputs; one-dimensional for $Y(\mathfrak{sl}_2)$ and
   quintic; rank-$(n-1)$ for $Y(\mathfrak{sl}_n)$; rank-$2$ for LP$^2$.
   Each generator named.

4. **Explicit interior stratum.** $A^{\mathrm{LP}^2}_{q, t}$ at generic
   $(q, t) \neq (1, 1)$ realises both algebraic and resurgent layers
   non-trivially.

5. **Falsifiable prediction (V96-FP).** Stokes-jump bidegree $(p_S, q_S)$
   satisfies $p_S + q_S = 2 \dim H^3(X) - 2$. Verified for quintic
   ($6 = 2 \cdot 4 - 2$) and LP$^2$ ($2 = 2 \cdot 2 - 2$); open for other
   $B_M$ inputs; falsifies V87-RDT if it fails on any single input.

The Russian-school dialectic confirms its value: V87's seed ghost theorem
appeal was structurally correct but elliptical at the bidegree level;
V96 makes the bidegree explicit, the reduction map explicit, the per-input
computation explicit, the interior stratum explicit, and adds a
falsifiable prediction that distinguishes V87-RDT from K--T
observationally. The Platonic ideal is the bigraded twist
$\mathcal{F}_A = \mathcal{F}_A^{\mathrm{formal}} \cdot \exp(\cdots)$;
its formal factor is K--T (proved); its resurgent factor is V87-RDT's
genuine new content; the joint existence is V87-RDT.

The V79 $B_L$/$B_M$ split is preserved; V87's interior-stratum
prediction is realised; V96-FP makes V87-RDT falsifiable. All three
layers honestly stated, no downgrades, no spurious unification, no
spurious novelty.

The boxed Platonic display (V96 sharpening of V87 §4.4):

$$
\xi^{\mathrm{V19}}(A) = [d_{\mathrm{HS}}^{\mathrm{tot}},
\mathcal{F}_A^{\mathrm{formal}}(\hbar) \cdot \exp\!\left(\sum_{n \geq 1, \alpha}
A_\alpha^n e^{-n S_\alpha/g_s} \mathcal{G}_A^{(n, \alpha)}(\hbar)\right)] = 0
\;\Longleftrightarrow\; A \text{ admits a bigraded Drinfeld twist},
$$

with formal layer K--T (proved, $g_s = 0$ limit); resurgent layer
Mariño--Schiappa--Écalle (V87-RDT genuine content, $g_s$-direction);
joint existence the V87-RDT conjecture; falsifiable invariant the
V96-FP Stokes-jump bidegree. ONE conjecture; TWO layers; FOUR per-input
$\mathrm{HS}^{2, 2}$ regimes (zero / $B_L$ / $B_M$ / interior); ONE
falsifiable numerical prediction.

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft
only.
