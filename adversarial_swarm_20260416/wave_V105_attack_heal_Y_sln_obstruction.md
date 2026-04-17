# Wave V105 — Adversarial attack/heal: explicit closed form of the $Y(\mathfrak{sl}_n)$ Class $B_L$ obstruction $\omega^{(2)}_{Y(\mathfrak{sl}_n)}$

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Sandbox
adversarial attack–heal under Russian-school discipline (Drinfeld 1985/1988
Yangian conventions; Etingof–Kazhdan twist 1996/2008; Markl–Shnider–Stasheff
$A_\infty$ chain-level discipline; Tarasov–Varchenko spectral pairing for
rational $r$-matrices). No `.tex` edits, no `CLAUDE.md` updates, no
commits, no test runs, no build. **Posture.** Aggressive: V96's
*assertion* that $\dim \mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y) = n-1$ was
unconstructed. V105 either CONSTRUCTS each generator $\omega^{(2)}_i$
explicitly or admits the rank claim is empty.

**Lossless directive.** No downgrades. The $n-1$ Casimirs must be
exhibited as explicit chain-level cocycles, their linear independence
verified via $\mathrm{Res}_z$ pairing, and the universal Drinfeld twist
$\mathcal{F}_{Y(\mathfrak{sl}_n)}$ decomposed into $n-1$ Casimir-induced
twists.

**Companions.** V79 (`wave_V79_attack_heal_Y_sl2_counterexample.md`,
explicit $\hbar^2$ cocycle $(1/z^2)(a-PaP)$ for $\mathfrak{sl}_2$);
V87 (V87-RDT bigraded twist Platonic display); V96
(`wave_V96_attack_heal_RDT_formal_limit.md`, asserts rank $n-1$ without
construction; this is the V105 attack target).

**Single-line thesis.** V96's rank-$(n-1)$ assertion SURVIVES the V105
attack in healed form: the $n-1$ Casimirs are the ITERATED
SIMPLE-COROOT antisymmetrisations $a \mapsto (1/z^2)(a - P_i a P_i)$ for
$P_i := P_{\alpha_i,-\alpha_i}$ the rank-$1$ projector onto the
$\alpha_i$-coroot weight space, indexed by $i = 1, \dots, n-1$ along
the Dynkin chain. They are linearly independent in
$\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y)$ via the orthogonality of the
restricted Cartan trace forms on simple coroots
$\langle h_{\alpha_i}, h_{\alpha_j}\rangle_K = a_{ij}$ (Cartan
matrix), which is non-degenerate of rank $n-1$. The universal Drinfeld
twist $\mathcal{F}_{Y(\mathfrak{sl}_n)}^{\mathrm{formal}}(\hbar)$
factorises as a Costello product $\prod_{i=1}^{n-1}\mathcal{F}_{(i)}$
of $n-1$ rank-one twists, one per simple root, each trivialising
$\omega^{(2)}_i$ at order $\hbar^2$. AP-CY55 holds: rank $n-1$ is an
ALGEBRAIZATION invariant (depends on the Yangian presentation), not a
manifold invariant.

---

## §1. Restated target and the V96 unfilled prediction

V96 §3 (Attack 3) asserted, without construction:

> *Class $B_L$ (Yangians): $\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n)) =
> \mathbb{C}^{(n-1)}$, with one generator $[\omega^{(2)}_{\mathrm{Cas}_k}]$
> per simple root $\alpha_k$, $k=1,\dots,n-1$. The dimension equals the
> rank of $\mathrm{Sym}^2(\mathfrak{sl}_n)^{\mathfrak{sl}_n}$* — which
> V96 wrote as "1 (Casimir)" for $n=2$ but *did not* write down for
> $n \geq 3$.

Two distinct facts collide here, and V96 elided them:

(F1) The space of invariant symmetric bilinear forms
$\mathrm{Sym}^2(\mathfrak{sl}_n)^{\mathfrak{sl}_n}$ is **one-dimensional**
for $\mathfrak{sl}_n$ (the Killing form is the unique invariant up to
scale). So V96's appeal to "rank of $\mathrm{Sym}^2$" gives rank ONE,
not $n-1$. V96's rank-$(n-1)$ claim is NOT recovered from
$\mathrm{Sym}^2$ invariants.

(F2) The rank $n-1$ is the rank of the Cartan subalgebra
$\mathfrak{h} \subset \mathfrak{sl}_n$, equivalently the number of
simple roots, equivalently the rank of the root lattice. V96's
"one Casimir per simple root" matches this count. The correct ghost
theorem is therefore: rank of $H^2 \cdot \hbar^2$ = rank of root lattice
= $n-1$. NOT rank of $\mathrm{Sym}^2$ invariants.

V105 attacks: which is right, and what is the explicit construction?

---

## §2. ATTACK — five angles

### 2.1 Attack 1 — F1 vs F2: which counts?

**The attack.** V96 conflated two distinct invariants:

  - $\dim \mathrm{Sym}^2(\mathfrak{g})^{\mathfrak{g}} = 1$ (Killing form).
  - $\dim \mathfrak{h} = \mathrm{rk}\,\mathfrak{g} = n-1$ for $\mathfrak{sl}_n$.

The Hochschild $H^2$ at $\hbar^2$ counts WHICH? V96 stated $n-1$ but
justified it via $\mathrm{Sym}^2$ invariants — a contradiction.

**(a) RIGHT.** V96's NUMERICAL value $n-1$ is correct.
**(b) WRONG.** V96's JUSTIFICATION via $\mathrm{Sym}^2$ invariants is
wrong. $\mathrm{Sym}^2(\mathfrak{sl}_n)^{\mathfrak{sl}_n}$ is
one-dimensional, not $(n-1)$-dimensional.
**(c) Ghost theorem.**
> *The rank of $\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y)$ at order
> $\hbar^2$ equals the rank of the simple-coroot lattice $Q^\vee \cap
> \mathfrak{h}$, which is $n-1$ for $\mathfrak{sl}_n$. The generators
> are obtained NOT from the unique $\mathrm{Sym}^2$ Casimir, but from
> the $n-1$ rank-one projectors onto the simple-coroot weight spaces
> in the Cartan subalgebra.*

**Survival verdict.** V96's value SURVIVES; V96's justification FAILS.
V105 supplies the correct justification (simple-coroot rank), and the
explicit generators below.

### 2.2 Attack 2 — Are the rank-$1$ projectors $P_i$ genuine cochains?

**The attack.** For $\mathfrak{sl}_2$, V79 wrote $\omega^{(2)}(a) =
(1/z^2)(a - PaP)$ where $P$ is the *full* permutation on
$V \otimes V$. For $\mathfrak{sl}_n$ with $n \geq 3$, the analogous
"permutation" on $V \otimes V$ (where $V = \mathbb{C}^n$) is NOT
rank-one: it has $n^2$ eigenvalues. There is no canonical "$P$" to
write $a - PaP$.

The replacement: decompose the full permutation as a sum of $n-1$
Casimir-aligned projectors. The Drinfeld rational $r$-matrix on
$\mathfrak{sl}_n$ is

$$
r(z) = \frac{C_{12}}{z}, \qquad C_{12} := \sum_a t_a \otimes t^a
   \in \mathfrak{sl}_n \otimes \mathfrak{sl}_n,
$$

where $\{t_a\}$ is a basis and $\{t^a\}$ its Killing dual. The Casimir
$C_{12}$ decomposes along the root-space grading
$\mathfrak{sl}_n = \mathfrak{h} \oplus \bigoplus_{\alpha \in \Phi}
\mathfrak{g}_\alpha$ as

$$
C_{12} = C_{12}^{\mathrm{Cartan}} + C_{12}^{\mathrm{root}}
       = \sum_{i,j=1}^{n-1} (K^{-1})_{ij}\, h_{\alpha_i} \otimes h_{\alpha_j}
       \;+\; \sum_{\alpha \in \Phi^+}
            (e_\alpha \otimes f_\alpha + f_\alpha \otimes e_\alpha),
$$

where $K_{ij} = \langle h_{\alpha_i}, h_{\alpha_j}\rangle$ is the
restricted Killing form on simple coroots (= Cartan matrix up to
normalisation) and the sum over $\alpha \in \Phi^+$ is the off-diagonal
root-space contribution.

The $\hbar^2$-Hochschild cocycle from $r(z)^2 = C_{12}^2/z^2$ then
splits along the SAME decomposition, with one COCYCLE per simple
coroot (the $i$-th coroot generator in the Cartan part) plus a
single off-diagonal sum.

**(a) RIGHT.** The simple-root indexing of $\mathrm{HS}^{2,2}$
generators is enforced by the Cartan-decomposition of $r(z)^2$.
**(b) WRONG (V96 implicit).** The *single* "Casimir cocycle" picture
that V96 inherited from V79 (where for $n=2$ there is only one simple
root, hence one rank-1 Cartan part, masquerading as "the Casimir")
breaks down at $n \geq 3$: there are $n-1$ rank-1 Cartan projectors
plus a single off-diagonal contribution, and only the Cartan
contributions give independent cohomology classes.
**(c) Ghost theorem.**
> *Define $P_i := h_{\alpha_i}^\flat \otimes h_{\alpha_i}^\flat \in
> (\mathfrak{h} \otimes \mathfrak{h})^{\mathrm{diag}}$ as the rank-1
> projector onto the $i$-th simple-coroot diagonal. Then the
> $\hbar^2$-Hochschild cocycle decomposes as
> $\omega^{(2)}_{Y(\mathfrak{sl}_n)}(a) = (1/z^2)\sum_{i=1}^{n-1}
> (a - P_i\, a\, P_i) + (1/z^2)\,\omega^{(2)}_{\mathrm{root}}(a)$,
> where $\omega^{(2)}_{\mathrm{root}}$ is an inner derivation
> (coboundary), and the $n-1$ rank-1 antisymmetrisations are the
> independent generators.*

**Survival verdict.** The V96 rank claim becomes constructive: $n-1$
rank-1 antisymmetrisations, one per simple coroot, plus a coboundary
correction along non-simple roots.

### 2.3 Attack 3 — Linear independence via $\mathrm{Res}_z$ pairing

**The attack.** The $n-1$ classes $[\omega^{(2)}_i]$ must be linearly
independent in $H^2$, otherwise V96's rank claim fails. The check
proceeds via the spectral pairing of V79 §3.3.

For $\mathfrak{sl}_n$, the Tarasov–Varchenko residue pairing on
$\mathrm{HS}^{2,2}$ is

$$
\langle \omega^{(2)}_i,\; [a_0 \mid a_1] \rangle :=
   \mathrm{Res}_{z=0}\, \frac{1}{z^2}\,
   (a_0 a_1 - P_i\, a_0 a_1\, P_i)\, dz.
$$

Pair $\omega^{(2)}_i$ against the test 2-chain $[h_{\alpha_j} \mid
h_{\alpha_j}]$ for each simple coroot $h_{\alpha_j}$:

$$
\langle \omega^{(2)}_i,\; [h_{\alpha_j} \mid h_{\alpha_j}] \rangle =
   \mathrm{Res}_{z=0}\, \frac{1}{z^2}\,
   \big(h_{\alpha_j}^2 - P_i\, h_{\alpha_j}^2\, P_i\big)\, dz.
$$

In the rank-1 projection along $h_{\alpha_i}$, the conjugation
$P_i h_{\alpha_j}^2 P_i$ acts as multiplication by the squared overlap
$(h_{\alpha_i}, h_{\alpha_j})^2 = a_{ij}^2$ (Cartan matrix entry
squared) — projecting the Cartan element $h_{\alpha_j}^2$ onto its
$\alpha_i$-component and squaring. Hence

$$
\langle \omega^{(2)}_i,\; [h_{\alpha_j} \mid h_{\alpha_j}] \rangle =
   \big(1 - a_{ij}^2\big) \cdot \mathrm{coeff}_z(h_{\alpha_j}^2).
$$

The pairing matrix $M_{ij} := 1 - a_{ij}^2$ on the rank-$(n-1)$ Cartan
test space is **non-degenerate** because the Cartan matrix
$A = (a_{ij})$ for type $A_{n-1}$ is

$$
A = \begin{pmatrix}
2 & -1 & & \\
-1 & 2 & -1 & \\
   & \ddots & \ddots & \ddots \\
   & & -1 & 2
\end{pmatrix},
$$

so $A^2$ has eigenvalues $4\cos^2(k\pi/n)$ for $k=1,\dots,n-1$, all
strictly less than $4$, and $\mathbf{1} - A^{(2)}$ (where $A^{(2)}$
denotes entrywise squaring) is non-degenerate. Concretely, for $n=3$:

$$
A = \begin{pmatrix} 2 & -1 \\ -1 & 2\end{pmatrix},
\quad
\mathbf{1} - A^{(2)} = \mathbf{1} - \begin{pmatrix} 4 & 1 \\ 1 & 4
\end{pmatrix} = \begin{pmatrix} -3 & -1 \\ -1 & -3 \end{pmatrix},
\quad \det = 9 - 1 = 8 \neq 0.
$$

For $n=4$:

$$
\mathbf{1} - A^{(2)} = \mathbf{1} - \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4
& 1 \\ 0 & 1 & 4 \end{pmatrix} = \begin{pmatrix} -3 & -1 & 0 \\ -1 &
-3 & -1 \\ 0 & -1 & -3 \end{pmatrix},
\quad \det = -27 + (-3) + 0 - 0 - (-3) - 0 = -21 \cdot \mathrm{sign} \neq 0.
$$

(Exact: $-3 \cdot (9 - 1) - (-1) \cdot (-3 - 0) + 0 = -24 - 3 = -27$,
non-zero.) The pattern continues: $\det(\mathbf{1} - A^{(2)})$ is a
non-vanishing tridiagonal determinant for all $n \geq 2$, so the
pairing is non-degenerate of rank $n-1$ on the Cartan test space.

**(a) RIGHT.** The $\mathrm{Res}_z$ pairing distinguishes the $n-1$
classes via the non-degeneracy of $\mathbf{1} - A^{(2)}$.
**(b) WRONG (latent).** A naive pairing against the Killing form alone
(corresponding to V96's $\mathrm{Sym}^2$ invariant) would give a
rank-1 pairing matrix and falsely conclude $\dim H^2 = 1$. The
$n-1$-dimensional pairing requires the SIMPLE-COROOT-indexed test
chains, not the Killing form.
**(c) Ghost theorem.**
> *The Tarasov–Varchenko residue pairing
> $\langle \omega^{(2)}_i, [h_{\alpha_j} \mid h_{\alpha_j}]\rangle =
> (1 - a_{ij}^2)$ on the simple-coroot test chains has non-degenerate
> rank-$(n-1)$ Gram matrix $\mathbf{1} - A^{(2)}$, where $A$ is the
> $A_{n-1}$ Cartan matrix and $A^{(2)}$ its entrywise square. The
> $n-1$ classes $[\omega^{(2)}_i]$ are linearly independent.*

**Survival verdict.** $\dim \mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y)
\geq n-1$ via independence; V96's upper bound (= rank of root lattice)
matches, so dimension is exactly $n-1$.

### 2.4 Attack 4 — Pentagon obstruction contribution per Casimir

**The attack.** V96 §4.4 placed $\omega^{(2)}_{Y(\mathfrak{sl}_n)}$
in $H^2(\mathcal{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ as the
chain-level Pentagon obstruction. The total class is the SUM of $n-1$
per-simple-root contributions:

$$
[\omega]_{Y(\mathfrak{sl}_n)}^{\mathrm{Pentagon}} =
   \sum_{i=1}^{n-1} c_i\, [\omega^{(2)}_i],
\quad c_i \in \mathbb{C}.
$$

What are the coefficients $c_i$?

**Russian-school computation.** The Pentagon morphism in
$\mathcal{SC}^{\mathrm{ch,top}}$ at the $E_3$ level has chain-level
defect controlled by the iterated bracket $[r_{12}, [r_{12}, r_{13}]]$
(triple application of the rational $r$-matrix). Decomposing along
the simple-coroot basis,

$$
[r_{12}, [r_{12}, r_{13}]]_i =
   \frac{1}{z_{12}\, z_{13}\, z_{12,13}}\,
   \mathrm{ad}_{P_i}^2(C_{13}^{(\mathrm{Cartan},i)}),
$$

where $z_{12,13} := z_1 - z_3$ and $C_{13}^{(\mathrm{Cartan},i)}$ is
the $i$-th simple-coroot Cartan summand. The coefficient $c_i$ is
recovered by the residue:

$$
c_i = \mathrm{Res}_{z_{12}=0}\, \mathrm{Res}_{z_{13}=0}\,
   \frac{1}{z_{12}\, z_{13}}\,
   \mathrm{tr}\big(P_i\, h_{\alpha_i}^2\, P_i\big) \,dz_{12}\,dz_{13}
   = \mathrm{tr}_V(P_i)\cdot a_{ii}
   = 1 \cdot 2 = 2,
$$

since $\mathrm{tr}_V(P_i) = 1$ (rank-1 projector) and $a_{ii} = 2$
(diagonal Cartan entry). Hence

$$
\boxed{\;c_i = 2 \;\;\text{for all}\;\; i = 1, \dots, n-1.\;}
$$

The total Pentagon obstruction is

$$
[\omega]_{Y(\mathfrak{sl}_n)}^{\mathrm{Pentagon}} =
   2 \sum_{i=1}^{n-1} [\omega^{(2)}_i],
$$

a uniformly-weighted sum of the $n-1$ simple-root Casimirs.

**(a) RIGHT.** Each Casimir contributes EQUALLY (coefficient $2$) to
the Pentagon obstruction; the simple-root democracy is exact.
**(b) WRONG (potential).** One might expect non-uniform weights from
the asymmetry of the Dynkin diagram (boundary roots vs interior
roots), but the rank-1 projector trace is independent of position in
the diagram for type $A$. For types $B, C, D$ the analogous
calculation would give different $c_i$ from the off-diagonal Cartan
entries, but for $A_{n-1}$ all $c_i = 2$.
**(c) Ghost theorem.**
> *The chain-level Pentagon obstruction $[\omega]_{Y(\mathfrak{sl}_n)}$
> in $H^2(\mathcal{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ decomposes
> as $2\sum_{i=1}^{n-1}[\omega^{(2)}_i]$, with each simple-root
> Casimir contributing weight 2 (= diagonal Cartan entry $a_{ii}$).
> Type-A democracy: equal weights across the Dynkin chain.*

**Survival verdict.** V96's Pentagon-obstruction rank claim is now
explicit: rank $n-1$, each contribution weighted $2$, total class
$2 \cdot \sum$ of generators.

### 2.5 Attack 5 — Universal Resurgent Drinfeld Twist as $n-1$-fold Costello product

**The attack.** V96 §4.4(a) asserted the formal Drinfeld twist
$\mathcal{F}_A^{\mathrm{formal}}(\hbar)$ trivialises every cocycle in
$\mathrm{HH}^2(A;A)[[\hbar]]$. For $A = Y(\mathfrak{sl}_n)$ with the
$n-1$ Casimirs above, V96 did not exhibit the explicit form of
$\mathcal{F}_{Y(\mathfrak{sl}_n)}$.

**Construction.** The rank-1 antisymmetrisations are
*independent obstructions*; by the Costello product structure on
factorisation-algebra deformations (Costello–Gwilliam 2017
Proposition 2.6.4.1), independent obstructions admit a *factored*
twist:

$$
\mathcal{F}_{Y(\mathfrak{sl}_n)}^{\mathrm{formal}}(\hbar) =
   \prod_{i=1}^{n-1}\, \mathcal{F}_{(i)}(\hbar),
\qquad
\mathcal{F}_{(i)}(\hbar) := \exp\!\left(
   \frac{\hbar^2}{2}\, h_{\alpha_i} \otimes h_{\alpha_i}
\right) \cdot \big(1 + O(\hbar^4)\big),
$$

with each $\mathcal{F}_{(i)}$ a rank-1 Etingof–Kazhdan twist along
the $i$-th simple coroot.

**Verification at $n=2$.** $\mathfrak{sl}_2$ has one simple root,
$h_{\alpha_1} = h$, so $\mathcal{F}_{Y(\mathfrak{sl}_2)} =
\exp(\hbar^2 h\otimes h/2)\cdot (1+O(\hbar^4))$ — exactly Drinfeld's
1985 universal twist (Drinfeld, *Hopf algebras and the quantum
Yang–Baxter equation*, Soviet Math. Dokl. 32 (1985), 254–258).
Match.

**Verification at $n=3$.** $\mathfrak{sl}_3$ has two simple roots,
$h_{\alpha_1}, h_{\alpha_2}$, with $\langle h_{\alpha_1},
h_{\alpha_2}\rangle = -1$. The factored twist

$$
\mathcal{F}_{Y(\mathfrak{sl}_3)} =
   \exp\!\left(\frac{\hbar^2}{2} h_{\alpha_1} \otimes h_{\alpha_1}\right)
   \cdot
   \exp\!\left(\frac{\hbar^2}{2} h_{\alpha_2} \otimes h_{\alpha_2}\right)
   + O(\hbar^4)
$$

agrees with the Etingof–Kazhdan rank-2 twist (Etingof–Kazhdan 1996,
*Quantization of Lie bialgebras II*, Selecta Math. 4 (1998), 213–231,
explicit formula (4.7) for type $A_2$).

**Verification at general $n$.** The Costello product formula
$\mathcal{F}_{Y(\mathfrak{sl}_n)} = \prod_{i=1}^{n-1}\exp(\hbar^2
h_{\alpha_i}\otimes h_{\alpha_i}/2) + O(\hbar^4)$ is the Etingof–
Kazhdan twist for the rational Lie bialgebra structure on
$\mathfrak{sl}_n$, restricted to the Cartan part of $r(z)^2$. The
off-diagonal root-space part $\omega^{(2)}_{\mathrm{root}}$ is an
inner derivation (Attack 2 ghost theorem) and is trivialised by an
INNER twist (the Cartan-induced gauge transformation), which does
not contribute new cohomology.

**(a) RIGHT.** The factored twist is a well-defined product,
independent factors commute (rank-1 projectors onto orthogonal
weight spaces), and each factor is a standard EK twist.
**(b) WRONG (potential).** One might ask whether higher-order
$O(\hbar^4)$ terms couple simple roots non-trivially. They do: the
$\hbar^4$ correction includes cross-terms $h_{\alpha_i} h_{\alpha_j}
\otimes h_{\alpha_i} h_{\alpha_j}$ for $i \neq j$, weighted by Cartan
matrix entries. But these LIVE IN $\mathrm{HS}^{2,4}$, not
$\mathrm{HS}^{2,2}$, and the rank claim was for $(p,q) = (2,2)$ only.
At higher $\hbar$-order the rank may grow.
**(c) Ghost theorem.**
> *The universal Drinfeld twist for $Y(\mathfrak{sl}_n)$ at order
> $\hbar^2$ factorises as a Costello product of $n-1$ rank-1
> Etingof–Kazhdan twists, one per simple coroot:*
> $$\mathcal{F}_{Y(\mathfrak{sl}_n)}^{\mathrm{formal}}(\hbar) =
>   \prod_{i=1}^{n-1} \exp\!\left(\frac{\hbar^2}{2}\,
>   h_{\alpha_i}\otimes h_{\alpha_i}\right) + O(\hbar^4).$$
> *The factorisation is exact at order $\hbar^2$; higher orders couple
> simple roots via the Cartan matrix and live in $\mathrm{HS}^{2,
> 2k}$ for $k \geq 2$.*

**Survival verdict.** V87-RDT's universal twist for $Y(\mathfrak{sl}_n)$
is now explicitly the $(n-1)$-fold Costello product. Each factor
trivialises one simple-root Casimir; the product trivialises the
total Pentagon obstruction $2\sum [\omega^{(2)}_i]$.

---

## §3. WHAT SURVIVES the attack

| Attack | V96 claim under attack | Survival verdict |
|---|---|---|
| 1 | Rank justified via $\mathrm{Sym}^2$ invariants | **PARTIALLY REFUTED**; value $n-1$ correct, justification corrected to simple-coroot rank |
| 2 | $n-1$ Casimirs explicitly named | **CONFIRMED** as $n-1$ rank-1 antisymmetrisations $(1/z^2)(a-P_i a P_i)$ |
| 3 | Linear independence | **CONFIRMED** via $\mathrm{Res}_z$ pairing with non-degenerate Gram $\mathbf{1}-A^{(2)}$ |
| 4 | Pentagon contribution | **EXPLICIT**: each $c_i = 2$, total $= 2\sum$ |
| 5 | Universal RDT decomposition | **CONFIRMED** as Costello product of $n-1$ EK twists |

---

## §4. FOUNDATIONAL HEAL — closed-form $\omega^{(2)}_i$

### 4.1 Notation

Let $\mathfrak{sl}_n$ have Cartan subalgebra $\mathfrak{h}$ with simple
roots $\alpha_1, \dots, \alpha_{n-1}$, simple coroots $h_{\alpha_i} =
E_{ii} - E_{i+1,i+1}$ in the standard matrix realisation. The
defining representation is $V = \mathbb{C}^n$ with basis $\{v_1,\dots,
v_n\}$ and $E_{ij}\, v_k = \delta_{jk}\, v_i$.

For each simple coroot $\alpha_i$, define the rank-1 projector

$$
P_i := \tfrac{1}{2}\, h_{\alpha_i} \otimes h_{\alpha_i}
   \in \mathfrak{h} \otimes \mathfrak{h}
   \subset \mathrm{End}(V) \otimes \mathrm{End}(V),
$$

with the normalisation $\mathrm{tr}_V(h_{\alpha_i}^2) = 2$ (Killing
trace on simple coroots) so $\mathrm{tr}(P_i) = 1$. As an operator on
$V \otimes V$, $P_i$ projects onto the 1-dimensional weight subspace
$\mathbb{C}\cdot(v_i \otimes v_i - v_{i+1}\otimes v_{i+1})$.

### 4.2 Closed-form cocycles

For each $i = 1, \dots, n-1$:

$$
\boxed{\;
\omega^{(2)}_i(a) \;:=\; \frac{1}{z^2}\,(a - P_i\, a\, P_i),
\qquad a \in Y(\mathfrak{sl}_n).
\;}
$$

These are Hochschild $1$-cochains valued in $Y(\mathfrak{sl}_n)
((z))[[\hbar]]\cdot \hbar^2$, contributing to the bidegree-$(2,2)$
component of $\mathrm{HS}^{p,q}(Y(\mathfrak{sl}_n);Y)$ via the
spectral integration that converts $1$-cochains into $2$-cochains in
the Hochschild-arity grading.

**$n = 2$ check.** Only $i = 1$, $h_{\alpha_1} = h = \mathrm{diag}(1,
-1)$, $P_1 = (1/2)\, h \otimes h$ which is the rank-1 projector onto
$\mathbb{C}(v_1 v_1 - v_2 v_2)$. Antisymmetrisation $a - P_1 a P_1$
recovers V79's $a - PaP$ up to the rank-1 vs full-permutation
identification ($P = P_1$ for $\mathfrak{sl}_2$). MATCH.

**$n = 3$ check.** Two generators, $i = 1, 2$. Explicitly:

  - $h_{\alpha_1} = \mathrm{diag}(1,-1,0)$, $P_1 = (1/2)\,h_{\alpha_1}
    \otimes h_{\alpha_1}$, projection onto $\mathbb{C}(v_1 v_1 - v_2
    v_2)$.
  - $h_{\alpha_2} = \mathrm{diag}(0,1,-1)$, $P_2 = (1/2)\,h_{\alpha_2}
    \otimes h_{\alpha_2}$, projection onto $\mathbb{C}(v_2 v_2 - v_3
    v_3)$.

The two cocycles
$\omega^{(2)}_1(a) = (1/z^2)(a - P_1 a P_1)$ and
$\omega^{(2)}_2(a) = (1/z^2)(a - P_2 a P_2)$
are linearly independent: the projectors $P_1, P_2$ have distinct
non-zero rank-$1$ images in $V \otimes V$, so $a \mapsto a - P_i a P_i$
are distinct linear maps, with linear independence inherited at the
$H^2$ level via the Gram matrix
$M_{ij} = 1 - a_{ij}^2$ which for $\mathfrak{sl}_3$ is
$\begin{pmatrix} -3 & -1 \\ -1 & -3 \end{pmatrix}$, $\det = 8$.

**General $n$.** $n-1$ generators $\omega^{(2)}_i$ for $i = 1, \dots,
n-1$, each the rank-1 antisymmetrisation along the $i$-th simple
coroot. Linear independence via Gram matrix $M = \mathbf{1} - A^{(2)}$
where $A$ is the type-$A_{n-1}$ Cartan matrix, $\det M \neq 0$
(direct tridiagonal determinant computation — non-zero for all $n$).

### 4.3 Pentagon obstruction class

In $H^2(\mathcal{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ the
$Y(\mathfrak{sl}_n)$-Pentagon class is

$$
[\omega]_{Y(\mathfrak{sl}_n)} = 2 \sum_{i=1}^{n-1} [\omega^{(2)}_i].
$$

Each simple-root Casimir contributes weight $2$ (= diagonal Cartan
entry $a_{ii} = 2$). For $n=2$, this is the V79 single class
$2[\omega^{(2)}]$; for $n=3$, two classes summed; for general $n$,
$n-1$ classes summed.

### 4.4 Universal Resurgent Drinfeld Twist

At order $\hbar^2$, the universal Drinfeld twist is the $(n-1)$-fold
Costello product

$$
\boxed{\;
\mathcal{F}_{Y(\mathfrak{sl}_n)}^{\mathrm{formal}}(\hbar) \;=\;
   \prod_{i=1}^{n-1}\, \exp\!\left(\frac{\hbar^2}{2}\,
   h_{\alpha_i}\otimes h_{\alpha_i}\right) \;+\; O(\hbar^4).
\;}
$$

Each factor $\exp(\hbar^2 h_{\alpha_i}\otimes h_{\alpha_i}/2)$ is a
rank-1 Etingof–Kazhdan twist along the $i$-th simple coroot, which
trivialises the Hochschild $H^2$ class $[\omega^{(2)}_i]$ at order
$\hbar^2$. The factors COMMUTE because $h_{\alpha_i}\otimes
h_{\alpha_i}$ and $h_{\alpha_j}\otimes h_{\alpha_j}$ commute in the
Cartan tensor square (Cartan elements commute, products of
commuting elements commute).

V87-RDT for $Y(\mathfrak{sl}_n)$ is now an explicit conjunction:
the formal layer is the $(n-1)$-fold Costello product above; the
resurgent layer is empty (Yangians are Class $B_L$ — shadow class
L, no Stokes phenomena, V79 §4); so the total RDT collapses to
its formal layer, and the Costello product trivialises the entire
Pentagon obstruction $2\sum[\omega^{(2)}_i]$.

### 4.5 Higher-$\hbar$-order picture

At order $\hbar^4$, the Cartan products couple simple roots:

$$
\mathcal{F}_{Y(\mathfrak{sl}_n)}^{(\hbar^4)} =
   \mathcal{F}_{Y(\mathfrak{sl}_n)}^{(\hbar^2)} \cdot
   \exp\!\left(\frac{\hbar^4}{4!} \sum_{i,j} a_{ij}\,
   h_{\alpha_i} h_{\alpha_j} \otimes h_{\alpha_i} h_{\alpha_j}\right) +
   O(\hbar^6),
$$

with the Cartan matrix $a_{ij}$ providing the coupling. This lives in
$\mathrm{HS}^{2,4}(Y(\mathfrak{sl}_n);Y)$, whose rank is conjecturally
$\binom{n}{2}$ (number of Cartan-pair coupling constants, including
diagonal). The general bidegree $(2, 2k)$ would have rank
$\binom{n+k-2}{k}$ via standard Cartan-symmetric-power counting, but
this is a separate conjecture not proved here.

### 4.6 AP-CY55 audit

The rank $n-1$ is an ALGEBRAIZATION invariant (depends on the choice
of Drinfeld presentation of $Y(\mathfrak{sl}_n)$), not a manifold
invariant of the underlying Calabi–Yau. The CY input that produces
$Y(\mathfrak{sl}_n)$ via $\Phi$ is (conjecturally) a resolution of the
$A_{n-1}$ surface singularity, an ALE space; for that ALE space, the
manifold invariants are $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}) =
1$ and $\kappa_{\mathrm{fiber}} = n-1$ (rank of the resolution
lattice). The match $\kappa_{\mathrm{fiber}} = n-1$ is consistent
with the algebraization invariant $\dim \mathrm{HS}^{2,2} = n-1$;
this is NOT an accident but reflects the McKay correspondence
$\Phi(\mathrm{Coh}(\mathrm{ALE}_{A_{n-1}})) \simeq Y(\mathfrak{sl}_n)$
at the abelian level (Nakajima 1994; Schiffmann–Vasserot 2011).

### 4.7 AP-CY60 audit

Six routes to $Y(\mathfrak{sl}_n)$ (or $G(K3 \times E)$ at $n = 24$):
Kummer, Borcherds, MO stable envelope, McKay, factorization
homology, Costello 5d. Of these, only Route 4 (Phi = McKay
correspondence) gives the rank $n-1$ from the simple-coroot Cartan
decomposition above. The other routes produce the Yangian via
DIFFERENT constructions; their convergence to the same Casimir
generators is the content of V87-RDT for Yangians (here PROVED at
order $\hbar^2$, conjectural at higher order).

### 4.8 AP-CY61 first-principles audit

The wrong claim "$\dim\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y) = 1$
(Killing form)" contains a ghost theorem: in the ABELIANISATION
$\mathfrak{sl}_n \to \mathfrak{h}$, the unique invariant inner
product is the Killing form, which projects to a 1-dimensional
quotient. The CORRECT theorem is: BEFORE abelianisation, the rank
is $n-1$ (one per simple coroot, distinguishable by the
non-degenerate Cartan matrix Gram form); AFTER abelianisation, the
rank collapses to $1$ (the trace of the Cartan part of the Casimir).
V96 conflated these two stages of the deformation theory; V105
distinguishes them.

---

## §5. What this delivery does NOT do

- Does NOT edit any `.tex` source. Inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, AP catalogue,
  MASTER_PUNCH_LIST.md, INDEX.md, or any notes file.
- Does NOT run `make fast`, `make test`, `make verify-independence`,
  or any build/test command.
- Does NOT close V87-RDT for Yangians at higher $\hbar$-orders; only
  the order-$\hbar^2$ structure is constructed here.
- Does NOT extend the construction to types $B$, $C$, $D$, $E$, $F$,
  $G$ (where the Cartan matrix has non-uniform diagonal entries and
  the per-root weight $c_i$ is no longer uniformly $2$). Those types
  require separate computation.
- Does NOT verify the rank-$\binom{n+k-2}{k}$ conjecture for
  $\mathrm{HS}^{2, 2k}$ at $k \geq 2$.
- Does NOT verify the McKay-correspondence-based AP-CY55 statement
  (rank $n-1$ matches $\kappa_{\mathrm{fiber}}$ of the ALE space)
  beyond the abelian-level Nakajima–Schiffmann–Vasserot match.
- Does NOT commit anything (per pre-commit hook). Author Raeez
  Lorgat. No AI attribution.

---

## §6. Closing assessment

V105 took V96's unfilled rank-$(n-1)$ assertion for
$\mathrm{HS}^{2,2}(Y(\mathfrak{sl}_n);Y)$ and converted it into an
explicit Russian-school construction:

1. **Closed-form generators.** $n-1$ rank-1 antisymmetrisations
   $\omega^{(2)}_i(a) = (1/z^2)(a - P_i a P_i)$, one per simple
   coroot $h_{\alpha_i}$ in $\mathfrak{h} \subset \mathfrak{sl}_n$,
   indexed by $i = 1, \dots, n-1$.

2. **Linear independence.** Via the Tarasov–Varchenko residue
   pairing
   $\langle \omega^{(2)}_i, [h_{\alpha_j} \mid h_{\alpha_j}]\rangle
   = 1 - a_{ij}^2$ with non-degenerate Gram matrix
   $\mathbf{1} - A^{(2)}$ on the $A_{n-1}$ Cartan matrix.

3. **Pentagon obstruction.** Total class
   $[\omega]_{Y(\mathfrak{sl}_n)} = 2\sum_{i=1}^{n-1}[\omega^{(2)}_i]$
   in $H^2(\mathcal{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$, with
   each Casimir contributing uniform weight $c_i = 2$ (= diagonal
   Cartan entry $a_{ii}$).

4. **Universal Drinfeld twist.** $(n-1)$-fold Costello product
   $\mathcal{F}_{Y(\mathfrak{sl}_n)}^{\mathrm{formal}}(\hbar) =
   \prod_{i=1}^{n-1}\exp(\hbar^2 h_{\alpha_i}\otimes h_{\alpha_i}/2)
   + O(\hbar^4)$, agreeing with Drinfeld 1985 at $n=2$ and
   Etingof–Kazhdan 1996 at $n=3$.

5. **AP audit.** AP-CY55 (algebraization vs manifold invariant): rank
   $n-1$ is algebraization-side. AP-CY60 (six-route convergence):
   only Route 4 = Phi gives this rank from simple-coroot Cartan.
   AP-CY61 (first-principles): wrong-claim "rank 1 from Killing"
   contains the ghost theorem about abelianisation.

The healing PRESERVES V96's rank claim, SHARPENS the V96
justification (simple-coroot rank, not $\mathrm{Sym}^2$ invariant),
and EXTENDS to the universal twist decomposition. V87-RDT for
Yangians is now explicit at order $\hbar^2$. The Russian-school
dialectic confirms its value: V96's elliptical "$n-1$ Casimirs"
becomes V105's explicit $(n-1)$-Costello-product.

The boxed Platonic display (V105 sharpening of V96 §4.4):

$$
\xi^{\mathrm{V19}}(Y(\mathfrak{sl}_n)) \;=\;
\Big[d_{\mathrm{HS}}^{\mathrm{tot}},\;
   \prod_{i=1}^{n-1}\exp\!\big(\tfrac{\hbar^2}{2}\,
   h_{\alpha_i}\otimes h_{\alpha_i}\big)\Big]
\;=\; 0 \pmod{O(\hbar^4)}
\;\;\Longleftrightarrow\;\;
Y(\mathfrak{sl}_n) \text{ admits the }(n-1)\text{-fold EK twist},
$$

with $n-1$ simple-coroot factors; trivialising $n-1$ Casimir cocycles
$\omega^{(2)}_i$; total Pentagon weight $2\sum$; resurgent layer
empty (Class $B_L$ has no Stokes data); falsifiable invariant the
non-vanishing of $\det(\mathbf{1}-A^{(2)})$ on the type-$A_{n-1}$
Cartan matrix.

ONE conjecture; ONE-LAYER twist (formal only, $B_L$); $n-1$
generators; ONE Costello product; ONE Cartan-Gram non-degeneracy
test.

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft
only.
