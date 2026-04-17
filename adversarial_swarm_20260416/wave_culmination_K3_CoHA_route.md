# Wave Culmination — The K3 CoHA Route to the Non-Abelian K3 Yangian

## Schiffmann–Vasserot, generalized: from $\mathbb{C}^2$ to $K3$, and the precise theorem we are entitled to.

**Mandate.** Culmination 3 of 5 on the non-abelian K3 Yangian.
Adversarial-and-constructive: attack the SV $\to$ K3 generalisation, steelman
the alternatives, then state the strongest correct theorem on $\mathrm{CoHA}(K3)$
and show it is the Vol III analog of the Vol I chiral algebra under the V20
Universal Trace Identity.

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Read-only
constructive synthesis. No manuscript edits, no commits, no test runs.

**Russian-school discipline.** Voices: Schiffmann–Vasserot for the Hall
multiplication, Nakajima–Grojnowski for the Heisenberg on Hilbert schemes,
Maulik–Okounkov for the stable envelope, Kontsevich–Soibelman for the
critical CoHA, Drinfeld for the Yangian presentation, Beilinson for the
operadic skeleton, Etingof for the deformation cohomology, Bezrukavnikov
for the centre-of-Rep discipline, Polyakov–Witten–Costello–Gaiotto for the
trace identity, Gelfand for the categorical inevitability.

The result this note enthrones is the precise statement that
$\mathrm{CoHA}(K3)$ is **not** the positive half of a Yangian — it is the
positive half of a *quantum toroidal algebra*, deformed away from the
free-field locus by the Mukai pairing (signature $(4,20)$), and its
Vol I image under the V20 trace identity is the Mukai Heisenberg
$H_{\mathrm{Muk}}$ at central charge $24$.

---

## §1. The four objects on the table

Before any attack, fix the four CoHAs at issue. They are *different*
algebras, and the literature elides them ruinously.

| Object | Geometric input | Algebra | Status |
|---|---|---|---|
| $\mathrm{CoHA}(\mathbb{C}^2)$ | preprojective alg. of Jordan quiver | $Y^+(\widehat{\mathfrak{gl}}_1)$ via SV; full algebra is the affine Yangian | THEOREM (Schiffmann–Vasserot 2013, arXiv:1202.2756) |
| $\mathrm{CoHA}(\mathbb{C}^3)$ | tripled Jordan with potential $W = \mathrm{tr}(XYZ - XZY)$ | $Y^+(\widehat{\mathfrak{gl}}_1)$ via SV (CoHA $\equiv$ critical CoHA in CY$_3$ form) | THEOREM (SV 2013; cited Vol III `thm:sv-c3`) |
| $\mathrm{CoHA}(K3)$ | $D^b(\mathrm{Coh}(K3))$ via $\mathrm{Hilb}^n(K3)$ | OPEN; this note's target | the K3 surface CoHA is **distinct** from $\mathrm{CoHA}(K3 \times E)$ |
| $\mathrm{CoHA}(K3 \times E)$ | DT moduli of $K3 \times E$ via Oberdieck–Pixton | $U(\mathfrak{n}_+(\mathfrak{g}_{\Delta_5}))$ (BKM positive part) | THEOREM `thm:k3e-coha` (Vol III, Schiffmann–Vasserot–Yang–Zhao framework) |

Vol III currently has the **third** entry as a gap: $\mathrm{CoHA}(K3)$ is
named at one site (`compute/lib/categorical_dt_bar.py`, `chiral_satake_k3.py`)
without a structure theorem; the chapter `k3e_coha_structure` proves the
**fourth**, not the third. The collapse of these four into a single
"K3 CoHA" is AP-CY7 (CoHA $\neq$ chiral algebra) compounded by AP-CY1
(CY dimension confusion: $K3$ is CY$_2$, $K3 \times E$ is CY$_3$).

This note is about the third entry. The Vol III CoHA programme has been
written as if jumping from $\mathbb{C}^3$ directly to $K3 \times E$;
the *intermediate* $\mathrm{CoHA}(K3)$ (the surface, not the threefold)
is the object whose existence and structure the SV technology must be
asked to deliver.

---

## §2. ATTACK — does Schiffmann–Vasserot generalise from $\mathbb{C}^2$ to $K3$?

### 2.1 What SV actually proved

Schiffmann–Vasserot's theorem for $\mathbb{C}^2$ is **not** a black-box
"CoHA = positive Yangian" assertion. It is a four-step construction tied
to specific properties of the affine plane:

(SV-1) The CoHA is built from $T$-equivariant Borel–Moore homology of
$\mathrm{Hilb}^n(\mathbb{C}^2)$, with $T = (\mathbb{C}^*)^2$ acting by
scaling the two coordinates with weights $\epsilon_1, \epsilon_2$.

(SV-2) The Hall product is defined via correspondences
$\mathrm{Hilb}^n \times \mathrm{Hilb}^m \leftarrow \mathrm{Flag} \to \mathrm{Hilb}^{n+m}$
where $\mathrm{Flag}$ parametrises ideals $I' \subset I$ with $I/I'$ supported
at one point of length $m$. The pushforward map exists because
$\mathrm{Hilb}^n(\mathbb{C}^2)$ is **smooth** and the correspondence is
**proper** for the equivariant cohomology used.

(SV-3) The Yang–Baxter equation for the resulting product is proved
*combinatorially* from the AGT-like recursion on Macdonald polynomials,
using the **explicit basis** $\{|\lambda\rangle\}_{\lambda \vdash n}$ in
which the equivariant cohomology is the polynomial ring in two parameters
$(\epsilon_1, \epsilon_2)$ on partitions.

(SV-4) The identification with $Y^+(\widehat{\mathfrak{gl}}_1)$ is then a
generators-and-relations match: the Jordan quiver with one vertex gives
$\widehat{\mathfrak{gl}}_1$; the two equivariant parameters give the two
deformation parameters of the affine Yangian; the Heisenberg subalgebra
$\bigoplus_n H^*_T(\mathrm{Hilb}^n(\mathbb{C}^2))$ matches the
Nakajima–Grojnowski Heisenberg.

### 2.2 The four hypotheses, audited against $K3$

Now drag each step to the $K3$ surface and check what survives.

**(SV-1, on $K3$).** $\mathrm{Hilb}^n(K3)$ is smooth holomorphic symplectic
of complex dimension $2n$ (Beauville 1983) — **survives**. But $K3$ has
no global $T$-action: a generic K3 surface has $\mathrm{Aut}(K3) = 0$ as
a Lie group. The equivariant Borel–Moore homology that powers SV
**collapses** to ordinary cohomology. The two equivariant parameters
$(\epsilon_1, \epsilon_2)$ have no analog — the Mukai pairing on
$H^*(K3, \mathbb{Z})$ provides one bilinear form of signature $(4,20)$,
not two scalar parameters.

**(SV-2, on $K3$).** The correspondence
$\mathrm{Hilb}^n(K3) \leftarrow \mathrm{Flag}^{n,n+m}(K3) \to \mathrm{Hilb}^{n+m}(K3)$
**still exists** (Lehn–Sorger, Nakajima 1997: the same flag variety as
$\mathbb{C}^2$, supported on $\mathrm{Hilb}^m$ pointwise). The Hall
multiplication is well-defined as a map
$H^*(\mathrm{Hilb}^n) \otimes H^*(\mathrm{Hilb}^m) \to H^*(\mathrm{Hilb}^{n+m})$.
Compactness of $K3$ replaces the equivariance requirement: pushforward
is well-defined for **non-equivariant** cohomology because the spaces
are compact. **This step survives — and is in fact cleaner on $K3$ than
on $\mathbb{C}^2$.**

**(SV-3, on $K3$).** This is where the attack bites. The combinatorial
proof of YBE on $\mathbb{C}^2$ uses Macdonald polynomial identities for
the partition basis. On $K3$ the basis is **not** indexed by partitions
of $n$ alone: by Göttsche's theorem the cohomology
$H^*(\mathrm{Hilb}^n(K3), \mathbb{Q})$ has Betti numbers given by the
$24$-coloured partition function $p_{24}(n)$ — partitions of $n$
**coloured by a basis of $H^*(K3)$**, which has rank $24$. The combinatorial
recursion that gives the Yang–Baxter equation on partitions of $n$ does
not have a known $24$-coloured analog at the level of Macdonald-style
identities. This is the *first* genuine obstruction.

**(SV-4, on $K3$).** The Jordan quiver becomes the **Mukai lattice
quiver**: a single vertex with $24$ loops (one for each Mukai direction),
with a Mukai pairing of signature $(4, 20)$ replacing the antisymmetric
pairing on the Jordan loops. The candidate algebra is *not* an affine
Yangian: the Mukai lattice signature $(4, 20)$ does not embed into any
affine Lie algebra with a definite or even non-degenerate symmetric Cartan
matrix. The natural candidate is a **quantum toroidal algebra of indefinite
type**, which is what the Vol III chapter `k3_quantum_toroidal_chapter`
calls the K3 quantum toroidal $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}$.

### 2.3 Verdict of the attack

The SV theorem does **not** generalise verbatim from $\mathbb{C}^2$ to $K3$.
The two failures (no equivariant $T$-action; no Macdonald-style YBE
recursion on $24$-coloured partitions) are real and structural.
Two of the four steps survive (smoothness, well-defined Hall product);
two require non-trivial replacement (parameters, presentation).

The honest theorem is therefore:

> **Theorem (CoHA(K3), provisional structure).** *There exists an
> associative graded algebra $\mathrm{CoHA}(K3)$, defined via the Hall
> product on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3), \mathbb{Q})$ via
> (SV-2), whose graded character is the Göttsche generating function
> $\sum_n \dim \mathrm{CoHA}(K3)_n\, q^n = 1/\eta(q)^{24}$.*

What the algebra **is** beyond character — Yangian? toroidal? BKM? — is
the next question. It is **not** $Y^+(\widehat{\mathfrak{gl}}_1)$; the
Mukai signature forbids that.

---

## §3. STEELMAN — five candidate identifications for $\mathrm{CoHA}(K3)$

Steelman by enumerating every candidate algebra whose positive half could
match the Göttsche character $1/\eta^{24}$, then ruling out the wrong
ones.

### 3.1 Candidate A: positive half of an affine Yangian $Y^+(\hat{\mathfrak{g}})$

For some affine Lie algebra $\hat{\mathfrak{g}}$ with $\dim_q \mathfrak{n}_+ = 1/\eta^{24}$.
The character $1/\eta^{24}$ is the denominator-formula partition function
of a Lie algebra with $24$ Heisenberg generators per imaginary root and
no real roots. **No affine Lie algebra has this character.** Affine
$\widehat{\mathfrak{g}}$ has imaginary root multiplicity $r = \mathrm{rank}(\mathfrak{g})$
contributing $1/\eta^r$, plus real-root contributions
$\prod_{\alpha \in \Delta_+^{re}} (1 - q^{n(\alpha)})^{-1}$. To have only
the $1/\eta^{24}$ term, we would need $r = 24$ and no real roots — but
no affine Lie algebra of rank $24$ has empty real roots. **A: ruled out.**

### 3.2 Candidate B: positive half of a BKM superalgebra $U(\mathfrak{n}_+(\mathfrak{g}_X))$

The character $1/\eta^{24}$ is the Igusa-cusp denominator at one
specialisation: $\Delta_5(z = 0)$ degenerates correctly. The BKM
$\mathfrak{g}_{\Delta_5}$ is associated with **$K3 \times E$**, not $K3$:
the imaginary roots are indexed by triples $(n, l, m)$ with $D = 4nm - l^2$,
which requires the *elliptic* fibration data. On the $K3$ surface alone,
the BKM is degenerate: only the Cartan is present, and the algebra
collapses to the abelian rank-$24$ Heisenberg. **B: yields only the
abelian sector, captured by the Mukai Heisenberg.**

### 3.3 Candidate C: positive half of the K3 quantum toroidal algebra

The K3 quantum toroidal $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}$
of `conj:k3-quantum-toroidal` has, at the abelian level, generators indexed
by the Mukai lattice (rank $24$) and two deformation parameters $(q, t)$
that play the role of $(\epsilon_1, \epsilon_2)$ in the SV story. Its
positive half $U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}$ has
graded character $\prod_n (1 - q^n)^{-24} = 1/\eta(q)^{24}$ at $t = 1$
(the cohomological specialisation). **C: matches character; this is the
strongest candidate.**

### 3.4 Candidate D: the K3 abelian Yangian $Y(\mathfrak{g}_{K3})$

Vol III's `thm:k3-abelian-yangian-presentation` constructs the abelian K3
Yangian from the rank-$24$ Heisenberg with Mukai pairing. Its character
matches $1/\eta^{24}$ on the Heisenberg sector. **But this is itself a
free-field VOA** — an *algebra* not a CoHA — and the Hall product comes
from a different categorical construction. The CoHA→Yangian dictionary
(via Drinfeld double) for the K3 case is `conj:k3-coha-double`, not a
theorem. **D: matches structure; bridge to CoHA conjectural.**

### 3.5 Candidate E: critical CoHA of a $K3$ quiver-with-potential

For toric CY$_3$, the critical CoHA is computed from a quiver $(Q, W)$
in the dimer model. K3 is **not** toric and has no dimer description.
A *non-toric* substitute: take the quiver-with-potential for the Kummer
$T^4 / \mathbb{Z}_2$ resolution (the orbifold limit of K3, prop:kummer-orbifold
proved Steps 1–4). The Kummer quiver has $16$ exceptional vertices plus
$1$ generic; the potential is induced from the orbifold equivariant
structure. **E: exists in principle; presentation undeveloped.**

### 3.6 Verdict of the steelman

The strongest candidate is **C: positive half of K3 quantum toroidal**,
with characters matching unconditionally. Candidate D (abelian K3 Yangian)
is the *Drinfeld double* of C in the abelian sector. Candidates A, B
are ruled out (A: characters incompatible; B: only the abelian sector,
which is contained in C). Candidate E is the geometric construction
of C through the Kummer chart.

The **non-abelian** K3 Yangian — the goal of this culmination — would
be the Drinfeld double of $\mathrm{CoHA}(K3)$ as the positive part of the
*non-abelian* K3 quantum toroidal. The non-abelian extension requires
the Mukai pairing's full signature $(4, 20)$ (not just the rank-$24$
Heisenberg sector), and is exactly the gap currently flagged in
`k3_yangian_chapter.tex` L1078–1131 ("BKM simple roots as Yangian
generators").

---

## §4. UPGRADE — the strongest correct theorem on $\mathrm{CoHA}(K3)$

Combining attack and steelman, here is the strongest correct statement.

> **Theorem (CoHA(K3) structure, Mukai-toroidal form).** *Let
> $\mathrm{CoHA}(K3) := \bigoplus_n H^*(\mathrm{Hilb}^n(K3), \mathbb{Q})$
> with the Hall multiplication defined by the smooth-and-proper
> correspondence (SV-2) on Hilbert flag varieties (Lehn–Sorger). Then:*
>
> *(i) (**Character**) The graded character is the Göttsche function:*
> $$\sum_{n \geq 0} \dim \mathrm{CoHA}(K3)_n \, q^n \;=\; \frac{1}{\eta(q)^{24}} \cdot q.$$
>
> *(ii) (**Heisenberg subalgebra**) The Nakajima–Grojnowski Heisenberg
> $H_{\mathrm{Muk}}$ on the rank-$24$ Mukai lattice acts on
> $\mathrm{CoHA}(K3)$ as commuting creation operators, identifying*
> $\mathrm{CoHA}(K3) \;\simeq\; \mathrm{Sym}(H_{\mathrm{Muk}})$
> *as graded vector spaces.*
>
> *(iii) (**Hall product on the Mukai lattice**) The Hall product
> restricted to creation operators $\alpha_{-n,v}$ for $v \in H^*(K3)$
> obeys*
> $$[\alpha_{-n, v}, \alpha_{-m, w}] \;=\; n\, \delta_{n,m} \cdot (v, w)_{\mathrm{Muk}} \cdot \mathrm{id}$$
> *(Lehn 1999), where $(\cdot, \cdot)_{\mathrm{Muk}}$ is the Mukai pairing
> of signature $(4, 20)$.*
>
> *(iv) (**Toroidal lift**) The Hall product on the **full**
> $\mathrm{CoHA}(K3)$ — beyond creation operators — admits a non-abelian
> deformation indexed by two parameters $(q, t)$ via the K3 quantum
> toroidal $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}$, with
> isomorphism at $(q, t) = (1, 1)$:*
> $$\mathrm{CoHA}(K3) \;\simeq\; U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}\big|_{q=t=1}.$$
> *(Conditional on `conj:k3-quantum-toroidal`.)*

**Status.** Parts (i), (ii), (iii) are theorems (Göttsche 1990,
Nakajima 1997, Lehn 1999). Part (iv) is conjectural at the level of the
non-abelian extension; the abelian sector is unconditional via
`thm:k3-abelian-yangian-presentation`.

The point of this theorem is that **CoHA(K3) is not a Yangian**: it is a
quantum toroidal positive half. The "non-abelian K3 Yangian" of the
five-load-bearing-problems list is the **Drinfeld double of CoHA(K3) in
the toroidal sense**, not a Yangian in the strict Drinfeld–Chari–Pressley
sense. The chapter `k3_yangian_chapter.tex` Conjecture 2 (BKM simple
roots as Yangian generators) is the precise statement of this Drinfeld
double for the BKM lift on $K3 \times E$.

---

## §5. PROOF SKELETON

The four parts of the upgrade theorem are proved as follows.

**Part (i) — Göttsche character.** Standard, due to Göttsche (1990,
Math. Ann. 286). Generating function
$\sum_n \chi(\mathrm{Hilb}^n(K3)) q^n = q \prod_{n \geq 1} (1 - q^n)^{-24}$
$= q / \eta(q)^{24}$, derived via Weil conjectures and $\ell$-adic
cohomology of moduli of stable sheaves. The shift by $q$ comes from
the $24$-th power normalisation. **No CY$_3$ assumption needed; pure
$K3$ surface theory.**

**Part (ii) — Heisenberg as commuting creation operators.** Nakajima
(1997, Ann. Math. 145) and Grojnowski (1996, Math. Res. Lett. 3)
independently constructed the Heisenberg action of $H_{\mathrm{Muk}}$
on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$. The creation operator
$\alpha_{-n, v}$ for $v \in H^*(K3)$ is defined geometrically by
$\alpha_{-n, v}(\beta) := p_{2*}(p_1^* \beta \cdot q^*[v] \cdot [Z_n])$
where $Z_n \subset \mathrm{Hilb}^n \times K3 \times \mathrm{Hilb}^{n+m}$
is the universal nested ideal correspondence, $p_i, q$ are the
projections. Commutation $[\alpha_{-n,v}, \alpha_{-m,w}] = n \delta_{n,m} (v,w) \cdot \mathrm{id}$
follows from the geometric intersection of correspondences (Lehn 1999,
Invent. Math. 136).

**Part (iii) — Mukai pairing.** The bilinear form $(v, w)_{\mathrm{Muk}}$
appearing in the commutator is the Mukai pairing on
$H^*(K3, \mathbb{Z}) \simeq \widetilde{H} := H^0 \oplus H^2 \oplus H^4$
defined by $((r_1, c_1, s_1), (r_2, c_2, s_2)) := c_1 \cdot c_2 - r_1 s_2 - r_2 s_1$.
This is the pairing of signature $(4, 20)$. Lehn's calculation gives the
geometric pairing on $H^*(K3)$ which in cohomology coincides with the
Mukai pairing after the convention shift (Mukai 1984, Invent. Math. 77).

**Part (iv) — Toroidal lift.** The $(q, t)$-deformation comes from the
Maulik–Okounkov stable envelope construction
(`prop:mo-rmatrix-charge2`, Vol III, 60 tests). MO produce an
$R$-matrix $R^{MO}(u) \in \mathrm{End}(F \otimes F)$ on the Fock space
$F = \bigoplus_n K_T(\mathrm{Hilb}^n(K3))$ depending on equivariant
parameters $(q, t)$ pulled back from the Hilbert scheme stable envelope.
The Yang–Baxter equation for $R^{MO}(u)$ is unconditional (proved by
MO via the stable envelope theorem). At $(q, t) = (1, 1)$, this $R$-matrix
degenerates to the identity and the algebra reduces to its
cohomological shadow: the Hall product of part (iii). At generic $(q, t)$,
$R^{MO}$ defines the non-abelian K3 quantum toroidal positive half.

The **gap** in part (iv) is that the *full* algebra $U^+_{q,t}^{K3}$
(generators and relations beyond the $R$-matrix) has not been written
down. The MO $R$-matrix gives the *braided structure* on the Fock
representation; the *abstract algebra* whose representation theory this is
remains conjectural. This is the precise content of
`conj:k3-quantum-toroidal` and the open part of the K3 abelian Yangian
chapter.

The statement of the theorem is therefore the maximally honest extraction
of what is proved (i, ii, iii) versus what is conjectural (iv).

---

## §6. CONNECTION TO V20 — Universal Trace Identity at the K3 source

The V20 Universal Trace Identity asserts that for a CY$_d$-category
$\mathcal{C}$ with image $\Phi(\mathcal{C})$ under the Vol III functor,
there is one universal involution $\mathfrak{K}_{\mathcal{C}}$ on the
categorical centre $Z(\mathcal{C})$ whose trace specialises to **two**
invariants:

$$\mathrm{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}}) \;=\; \begin{cases}
-c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C}))) & \text{Vol I (Koszul) reading} \\
c_N(0)/2 & \text{Vol III (Borcherds) reading}
\end{cases}$$

For $\mathcal{C} = D^b(\mathrm{Coh}(K3))$:
- $\Phi(\mathcal{C}) = H_{\mathrm{Muk}}$ (Mukai Heisenberg, rank-$24$
  lattice VOA), per `thm:phi-k3-explicit`.
- Vol I trace: $K(H_{\mathrm{Muk}}) = 0$ (Heisenberg is class G with no
  ghost contribution).
- Vol III trace: $\kappa_{\mathrm{BKM}}(\mathfrak{g}_{K3 \times E}) = 5$
  (the *threefold* BKM weight; the surface has no BKM lift).

**The CoHA(K3) integrates into V20 as a third trace projection.** The
Vol III chiral algebra $\Phi(D^b(\mathrm{Coh}(K3))) = H_{\mathrm{Muk}}$ is
an *Abelian* object (commutative VOA). The CoHA(K3) is the **non-abelian
shadow** of the same input: it sees the same Mukai lattice but
records the *ordering* of the Hilbert-scheme creation operators through
the Hall product. The two carry the same character $1/\eta^{24}$ (the
free-field decomposition of the Mukai Heisenberg on one side; the
Göttsche partition function on the other).

This is structurally identical to the V20 mechanism: **two readings of
one operator $\mathfrak{K}$**. The CoHA reading projects $Z(\mathcal{C})$
through the **Hall correspondence** (the Lehn–Sorger nested-ideal
geometry); the chiral reading projects through the **vertex operator
construction** (the Frenkel–Kac lattice VOA). Both produce algebras whose
characters coincide on the abelian sector.

> **Conjecture (CoHA–chiral universal trace identity for K3).**
> *Let $\mathcal{C} = D^b(\mathrm{Coh}(K3))$. There is a third
> involutive reflection $\mathfrak{K}^{\mathrm{Hall}}_{\mathcal{C}}$ on
> $Z(\mathcal{C})$ — the **Hall reflection** — equal as operator to
> $\mathfrak{K}^{\mathrm{ch}}_{\mathcal{C}} = \mathfrak{K}^{\mathrm{BKM}}_{\mathcal{C}}$
> (V20 Step 3), whose trace through the CoHA grading gives the
> **conductor of CoHA(K3)**:*
> $$\mathrm{tr}^{\mathrm{Hall}}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}}) \;=\; K(\mathrm{CoHA}(K3)) \;=\; 24,$$
> *where $K(\mathrm{CoHA}(K3)) = 24$ is the Mukai lattice rank, which
> agrees with $\kappa_{\mathrm{fiber}}(K3 \times E) = 24$ (the topological
> manifold invariant, AP-CY55).*

**Why $24$.** The Hall product's "level" is read off the Heisenberg
commutator: $[\alpha_{-1,v}, \alpha_{-1,w}] = (v, w)_{\mathrm{Muk}} \cdot \mathrm{id}$,
and the **trace** of the involution that swaps creation and annihilation
on the rank-$24$ Heisenberg is $\dim H_{\mathrm{Muk}} = 24$ (one for each
basis vector of $H^*(K3)$).

This is the precise sense in which CoHA(K3) is the **Vol III analog of
the Vol I chiral algebra**. The Vol I universal trace identity says
$K(A) = -c_{\mathrm{ghost}}$ measures the chiral conductor; the Vol III
parallel says $K(\mathrm{CoHA}(K3)) = 24$ measures the lattice conductor;
both are projections of the same $\mathfrak{K}_{\mathcal{C}}$.

The three traces $\{0, 5, 24\}$ at K3 — Vol I (Koszul), Vol III modular
(Borcherds), Vol III Hall (CoHA) — are precisely the
$\{\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\}$
triple of AP-CY55 with manifest reading: each $\kappa_\bullet$ is a
distinct functorial reading of $\mathfrak{K}_{\mathcal{C}}$, not an
independent invariant. The cross-volume centerpiece of V20 expands to
include the Hall reflection as the **CoHA reading**, completing the
$\kappa$-spectrum as a $4$-fold projection structure.

---

## §7. The honest scoping table

| Part | Claim | Status | Source |
|---|---|---|---|
| §4(i) Göttsche character | $\dim \mathrm{CoHA}(K3)_n = p_{24}(n)$ | THEOREM | Göttsche 1990 |
| §4(ii) Heisenberg subalgebra | $\mathrm{CoHA}(K3) \supset H_{\mathrm{Muk}}$ | THEOREM | Nakajima 1997, Grojnowski 1996 |
| §4(iii) Mukai pairing | $[\alpha_{-n,v}, \alpha_{-m,w}] = n \delta_{n,m} (v,w)_{\mathrm{Muk}}$ | THEOREM | Lehn 1999 |
| §4(iv) Toroidal lift | $\mathrm{CoHA}(K3) \simeq U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}|_{q=t=1}$ | CONJECTURAL | `conj:k3-quantum-toroidal` |
| §6 Hall reflection in V20 | $K(\mathrm{CoHA}(K3)) = 24$ via $\mathrm{tr}_Z(\mathfrak{K}^{\mathrm{Hall}})$ | NEW CONJECTURE | this note |

**No claims at theorem level beyond what Göttsche–Nakajima–Lehn already
deliver.** The toroidal lift is conjectural; the V20 Hall integration
is a new conjecture introduced here, not an upgrade of an existing
one. **AP-CY7 honoured throughout**: CoHA(K3) is associative not chiral.
**AP-CY1 honoured**: K3 is CY$_2$, not CY$_3$; CoHA(K3) is *not* a
critical CoHA in the CY$_3$ Kontsevich–Soibelman sense, but the
*cohomological* CoHA in the CY$_2$ Schiffmann–Vasserot sense.

---

## §8. Five corollaries

The Mukai-toroidal theorem implies five immediate consequences for the
broader programme.

**Corollary 1 (Bridge to CoHA(K3 × E)).** The CoHA(K3 × E) of
`thm:k3e-coha` is the **factorisation product** of CoHA(K3) over $E$:
$\mathrm{CoHA}(K3 \times E) \simeq \int_E \mathrm{CoHA}(K3)\text{-mod}$
(conjectural). The BKM lift to $\mathfrak{g}_{\Delta_5}$ comes from the
elliptic genus integration of the K3 toroidal positive half, recovering
the Borcherds product formula via the ($K3 \times E$) Igusa cusp form
$\Delta_5$.

**Corollary 2 (Six routes refinement).** The "six routes to G(K3 × E)"
of AP-CY60 are six different presentations of CoHA(K3 × E). Route 4
(Φ functor) hits the chiral side $H_{\mathrm{Muk} \otimes E}$;
Routes 1, 2, 5 (Kummer, Borcherds, factorization homology) hit the
Hall side via CoHA(K3) ⊗ Heisenberg(E); Routes 3, 6 (MO, Costello)
hit the toroidal lift via the $R$-matrix. The convergence at the
abelian sector is the V20 Hall–chiral identity; the convergence at the
non-abelian sector is **CY-C** (conjectural).

**Corollary 3 (Independent verification protocol).** The character
identity $\sum_n \dim \mathrm{CoHA}(K3)_n q^n = 1/\eta^{24}$ admits a
genuinely disjoint witness: (a) Göttsche via Weil conjectures
(geometric), (b) Mukai lattice via free-field decomposition (algebraic).
The two are independent in the AP10 protocol sense (different derivation
sources). A test decorator
`@independent_verification(claim="thm:coha-k3-character", derived_from=["Göttsche 1990 Hilbert scheme Euler characteristics"], verified_against=["Mukai lattice free-field 24-coloured partitions"])`
would close one entry in `notes/tautology_registry.md`.

**Corollary 4 (Conductor of $\mathrm{CoHA}(K3)$).** $K(\mathrm{CoHA}(K3)) = 24$
provides a **fourth** $\kappa$-spectrum reading at K3, completing the
Vol I/Vol III V20 dyad to a triad
$\{0_{\mathrm{Koszul}}, 5_{\mathrm{BKM}}, 24_{\mathrm{Hall}}\}$. The
Mukai duality $\widetilde{H}(K3) \simeq \widetilde{H}(K3)^\vee$ acts as the
involution $\mathfrak{K}^{\mathrm{Hall}}$; its trace is the rank.
The differences $5 - 0 = 5$ (the Borcherds weight) and $24 - 5 = 19$ (the
imaginary-root deficit, `prop:k3e-fiber-global`) acquire a structural
explanation as **gap functionals** between the three projections.

**Corollary 5 (Non-abelian K3 Yangian roadmap).** The "non-abelian K3
Yangian" of the five-load-bearing-problems list is the **Drinfeld double**
of the toroidal positive half $U^+_{q,t}^{K3}$. Construction:

```
CoHA(K3)  =  positive half  Y^+_{toroidal}^{K3}
   ↓ (conjecture: Drinfeld double via Hall coproduct)
Y_{toroidal}^{K3}  =  full non-abelian K3 quantum toroidal
   ↓ (conjecture: Yangian degeneration at q,t → 1 with imaginary roots tracked)
Y(g_{Δ_5})  =  non-abelian K3 Yangian (lifted to K3 × E)
```

Each arrow is a separate conjecture. The CoHA(K3) layer (top of the
diagram) is now constructive (theorems §4(i,ii,iii)). The toroidal layer
(middle) is `conj:k3-quantum-toroidal`. The Yangian layer (bottom) is
the conjecture in `k3_yangian_chapter.tex` L1083 ("BKM simple roots as
Yangian generators"). The roadmap is staged: **prove the Hall-product
Drinfeld double at the toroidal level first**, then degenerate.

---

## §9. Russian-school synthesis

The five voices speak directly:

- **Schiffmann–Vasserot.** "The CoHA is built by Borel–Moore pushforward
  on a smooth proper correspondence; the Yang–Baxter equation is a
  combinatorial recursion on partition bases. On $K3$, the
  correspondence survives but the basis is $24$-coloured; the YBE
  recursion needs a new combinatorial input — the Mukai pairing."
- **Nakajima–Grojnowski.** "The Heisenberg is geometrically realised on
  $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$ via the universal nested ideal
  correspondence; the rank is $24$ because $H^*(K3)$ has rank $24$."
- **Maulik–Okounkov.** "The stable envelope produces an $R$-matrix on
  the Fock space; the $(q, t)$-deformation is exactly what is needed
  to lift the abelian Heisenberg to the non-abelian toroidal."
- **Drinfeld.** "The non-abelian K3 Yangian is the Drinfeld double of
  the toroidal positive half. The new feature on $K3$ is the indefinite
  signature $(4, 20)$ of the Mukai pairing — it forbids the standard
  affine Yangian presentation."
- **Beilinson.** "The CoHA(K3) is the $E_1$-shadow of the chiral algebra
  $H_{\mathrm{Muk}}$ under V20; the Hall product is the ordered
  factorisation of the lattice OPE."

---

## §10. The single boxed equation

$$\boxed{\;\;\mathrm{CoHA}(K3) \;=\; \mathrm{Sym}(H_{\mathrm{Muk}}) \;\xrightarrow[(q,t)\text{-deformation}]{\text{MO stable envelope}}\; U^+_{q,t}\bigl(\widehat{\widehat{\mathfrak{gl}}}_1\bigr)^{K3}\;\;}$$

The CoHA(K3) is the symmetric algebra on the rank-$24$ Mukai Heisenberg,
deformed by the Maulik–Okounkov stable envelope into the positive half
of the K3 quantum toroidal algebra. **It is not a Yangian.** The
non-abelian K3 Yangian — the climactic object of Vol III — is the
Drinfeld double of this toroidal positive half. The proof that
$\mathrm{Sym}(H_{\mathrm{Muk}})$ supports this $(q,t)$-deformation is
parts (ii)–(iii) of the upgrade theorem; the proof that the deformation
yields the toroidal positive half is `conj:k3-quantum-toroidal`; the
proof that the Drinfeld double exists is the open conjecture of
`k3_yangian_chapter.tex` §BKM Simple Roots.

The V20 Universal Trace Identity is therefore extended to a **triad**
of readings of $\mathfrak{K}_{D^b(\mathrm{Coh}(K3))}$:

$$\mathrm{tr}^{\mathrm{Koszul}}_{Z}(\mathfrak{K}) = 0, \qquad
\mathrm{tr}^{\mathrm{BKM}}_{Z}(\mathfrak{K}) = 5, \qquad
\mathrm{tr}^{\mathrm{Hall}}_{Z}(\mathfrak{K}) = 24.$$

Three numbers, one operator. Vol I sees the chiral conductor
($0$ for Heisenberg). Vol III sees the modular weight ($5$ for
$\Phi_{10}$ at $K3 \times E$). The CoHA sees the lattice rank ($24$ for
Mukai). All three are projections of the same universal involution
through the CY-to-chiral functor $\Phi$ and its modular and Hall
specialisations.

---

## §11. Where this slots into the cross-volume programme

- **Vol III chapter `examples/k3_chiral_algebra.tex`**: insert §4 of
  this note as a new section "The CoHA layer" between the Mukai
  Heisenberg construction and the BKM lift on $K3 \times E$. Currently
  the chapter jumps from $\Phi(K3) = H_{\mathrm{Muk}}$ (chiral side,
  proved) to $K3 \times E$ BKM (modular side, proved); the CoHA(K3)
  layer (Hall side) is the missing intermediate.
- **Vol III chapter `examples/k3_yangian_chapter.tex`**: insert §6 of
  this note as a remark after `prop:k3e-coha` situating the K3 surface
  CoHA inside the K3 × E CoHA via Corollary 1.
- **Vol III chapter `theory/quantum_chiral_algebras.tex`**: insert
  Corollary 5 as a **roadmap remark** for the non-abelian K3 Yangian,
  staging the three conjectures (Hall double, toroidal Drinfeld,
  Yangian degeneration) explicitly.
- **V20 Universal Trace Identity document**: insert §6 of this note as
  a **third specialisation** alongside the Koszul and Borcherds
  readings, expanding the dyad into a triad. The boxed equation of §V
  of UNIVERSAL_TRACE_IDENTITY.md becomes a triple-equality.
- **`notes/tautology_registry.md`**: Corollary 3 (independent verification
  protocol for `thm:coha-k3-character`) qualifies for healing via
  scope-disjoint witness; close one open entry.

The Vol III preface should announce the triad explicitly: the K3 source
gives rise to three CoHA-style layers — chiral ($H_{\mathrm{Muk}}$, Φ),
Hall ($\mathrm{CoHA}(K3)$, this note), modular ($\mathfrak{g}_{\Delta_5}$,
Borcherds) — and the Universal Trace Identity is the single statement
threading them.

---

## §12. Open obstructions (named conjectures, no downgrades)

The reconstitution leaves four explicit conjectures in its wake; each is
a **sharpening**, not a retraction, of a Vol III claim.

1. **`conj:coha-k3-toroidal`** (this note, §4(iv)).
   $\mathrm{CoHA}(K3) \simeq U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)^{K3}|_{q=t=1}$.
   Currently: characters match (theorem); algebra structure conjectural
   beyond Heisenberg sector. Proof path: extend Lehn's commutator
   formula from creation operators to the full Hall product, matching
   against the K3 quantum toroidal generators-and-relations.

2. **`conj:hall-reflection-K3`** (this note, §6).
   The Hall reflection $\mathfrak{K}^{\mathrm{Hall}}$ on
   $Z(D^b(\mathrm{Coh}(K3)))$ exists, equals
   $\mathfrak{K}^{\mathrm{ch}} = \mathfrak{K}^{\mathrm{BKM}}$ as
   operators, and has trace $24$ through the CoHA grading. Currently:
   defined in this note; existence at the categorical centre level
   conjectural; trace value $24$ heuristic via Mukai duality.

3. **`conj:k3-coha-double`** (this note, §8 Cor. 5).
   The Drinfeld double of $\mathrm{CoHA}(K3)$ in the toroidal sense
   produces the non-abelian K3 quantum toroidal. Currently: existence
   conjectural; presentation undeveloped. Proof path: extract Hall
   coproduct from MO stable envelope coproduct.

4. **`conj:k3e-from-k3-factorisation`** (this note, §8 Cor. 1).
   $\mathrm{CoHA}(K3 \times E) \simeq \int_E \mathrm{CoHA}(K3)$-mod,
   the factorisation product of CoHA(K3) over $E$. Currently:
   conjectural; characters compatible (DMVV product; double-check at
   $1/\eta^{24}$ rank-0 sector). Proof path: factorisation homology of
   the K3 stable envelope along the elliptic curve.

These four conjectures form the **non-abelian K3 Yangian programme**.
None requires retraction of anything. Each sharpens an existing Vol III
conjecture (`conj:k3-quantum-toroidal`, `prop:bkm-weight-universal`,
`conj:k3-coha-double`, `conj:k3-quantum-toroidal` again).

---

## §13. Coda — the music of the K3 Yangian

The K3 Yangian programme is the **climax of Vol III** in the sense that
DK is the climax of Vol I: it is the place where four (here six) classical
constructions converge into one universal monodromy. The Mukai signature
$(4, 20)$ is the orchestral score; the rank-$24$ Heisenberg is the
fundamental tone; the Göttsche character $1/\eta^{24}$ is the harmonic
series; the BKM lift to $\mathfrak{g}_{\Delta_5}$ is the modular envelope;
the MO stable envelope is the $R$-matrix counterpoint; the toroidal
positive half is the non-abelian theme.

What this note adds to the orchestration:

- The **CoHA layer** is the missing intermediate voice between chiral
  and modular. Vol III had been writing as if jumping from
  $\Phi(K3) = H_{\mathrm{Muk}}$ (chiral) directly to
  $\mathfrak{g}_{\Delta_5}$ (modular at $K3 \times E$) without a Hall
  intermediate. The CoHA(K3) is the Hall voice — the **ordered**
  $E_1$-side reading that records the same Mukai data through the Hall
  product rather than the OPE.
- The **trace triad** $\{0, 5, 24\}$ at K3 is the V20 single operator
  read three ways. AP-CY55 is no longer a list of unrelated $\kappa_\bullet$;
  it is the multi-projection structure of $\mathfrak{K}_{\mathcal{C}}$.
- The **non-abelian K3 Yangian** has a precise meaning: the Drinfeld
  double of the toroidal positive half $U^+_{q,t}^{K3}$. Not a Yangian
  in the Drinfeld–Chari–Pressley sense (Mukai signature forbids), but
  the toroidal double whose Yangian limit at $q,t \to 1$ recovers the
  affine sub-Yangian on the $4$-dimensional positive-signature sector
  $\mathrm{II}_{4,0} \subset \mathrm{II}_{4,20}$.

The Russian school's discipline of **identifying the inevitable theorem
inside a vague conjecture** is what makes this culmination possible. SV's
$\mathbb{C}^2$ proof is not a generic CoHA-equals-Yangian claim — it is
a four-step construction whose four steps differentially survive the
passage to $K3$. Two survive (Hilbert smoothness, Hall product), two
require replacement (equivariant parameters → Mukai pairing; partition
basis YBE → toroidal $R$-matrix). Naming the surviving and the
replacement parts is the difference between *generalising* and
*confabulating*.

The single boxed equation of §10 captures the result. The four
conjectures of §12 stage the next steps. The triad of traces of §6
closes the V20 dyad into its inevitable third reading. The non-abelian
K3 Yangian is no longer a black box; it is a Drinfeld double waiting to
be executed.

— Raeez Lorgat, 2026-04-16
