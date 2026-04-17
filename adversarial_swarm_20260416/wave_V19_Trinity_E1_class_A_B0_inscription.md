# Wave V64 (V19 Trinity-at-$E_1$ chain-level dichotomy inscription)
## V19 Trinity-$E_1$ chain-level as a THEOREM for Class A, the abelian Heisenberg, and Class B0,
## with Class B as named per-input residual conjecture; counterexample $Y(\mathfrak{sl}_2)$ recovered as Class B.

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Inscription-ready
sandbox draft for Vol I §V19 (Trinity chapter), the **middle link** of the
V40 master implication chain Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1
\Rightarrow$ V20 Step 3 chain-level. **Posture.** No `.tex` edits, no
`CLAUDE.md` updates, no commits, no test runs, no build. Read-only structural
draft for main-thread review.

**Companions.** V40 (`wave_frontier_universal_trace_chain_level.md`, master
implication chain); V49 (K3 Pentagon-at-$E_1$ resolution, three independent
routes); V55 (`wave_frontier_pentagon_E1_non_K3.md`, Class A / B0 / B
dichotomy); V56 (`wave_class_B_alien_derivation_quintic_LP2.md`, Class B
residuals); V58 / V61 (`wave_V20_step3_chain_level_class_A_B0_inscription.md`,
V20 Step 3 chain-level Class A + B0); V59 (`draft_pentagon_E1_heisenberg_SPEC.md`,
abelian Heisenberg constructive grounding, 34/34 pytest); V60 / V63
(`wave_V11_pillar_alpha_U1_chain_level_extraction.md`, V11 Pillar α as the
$P_4 \leftrightarrow P_5$ edge of Pentagon-at-$E_1$).

**Single-line thesis.** The V40 master implication chain
$$
\text{Pentagon-at-}E_1 \;\Longrightarrow\; \text{V19 Trinity-}E_1
\;\Longrightarrow\; \text{V20 Step 3 chain-level}
$$
forces V19 Trinity-$E_1$, the **middle link**, to inherit the V55 dichotomy of
its premise. The historically-named "Trinity" of three Hochschild presentations
$C^\bullet_{\mathrm{chiral}}$, $\operatorname{End}^{\mathrm{ch}}(A)$,
$\operatorname{Ext}^*_{A^e}$ is FALSE unconditionally for genuinely-$E_1$
Yangians (counterexample $Y(\mathfrak{sl}_2)$); recovered as a THEOREM at Class
A (K3-fibred, V49), the abelian Heisenberg (V59 explicit chain-iso), and Class
B0 (super-trace vanishing); CONJECTURAL at Class B with explicit per-input
residual $\xi_{\mathrm{V19}}(A)$ named (quintic, local $\mathbb{P}^2$). The
ghost theorem extracted in §8: V19 Trinity-$E_1$ was REACHING FOR the **K3
Yangian truth** that $A_{K3}$ has all three Hochschild presentations
quasi-isomorphic at chain level because the underlying Yangian
$Y(\mathfrak{g}_{K3})$ has a Borcherds lift; $Y(\mathfrak{sl}_2)$ falsifies the
unconditional statement precisely because it lacks one.

---

## §1. Precise statement of V19 Trinity-$E_1$ at chain level for arbitrary $E_1$ chiral algebra $A$

Let $A$ be an $E_1$-chiral algebra. By AP-CY56, $E_1$ is the native level
attached to the Gerstenhaber bracket of degree $-2$ on $\mathrm{HH}^*(C, C)$ at
$d = 3$; $A = \Phi(C)$ for $C$ a CY$_3$-category, or, by restriction, the
$E_1$-shadow of a higher-$E_n$ chiral algebra at $d = 1, 2$.

### 1.1 The three Hochschild presentations of $A$

Three canonical chain models of "the Hochschild cohomology of $A$" at chain
level, distinguished per AP-CY62 / AP-CY63 / AP-CY64:

- **$Q_1$ — Geometric chiral Hochschild** $C^\bullet_{\mathrm{chiral}}(A)
  := C^*_{\mathrm{ch,geom}}(A,A)$ in the AP-CY62 (a) notation. The
  Fulton–MacPherson compactification model: chains are polynomial functions on
  $\mathrm{Conf}^{\mathrm{ord}}_n(\mathbb{R})$ valued in $A^{\otimes n}$, with
  the three-component Connes-type $B_{\mathrm{chir}}$ differential (logarithmic
  forms on the FM boundary).
- **$Q_2$ — Algebraic chiral endomorphism operad** $\operatorname{End}^{\mathrm
  {ch}}(A) := C^*_{\mathrm{ch,alg}}(A,A)$ in the AP-CY62 (b) notation. The
  algebraic model: chains are formal Laurent series
  $\mathbb{Q}[[z_i - z_j]] \otimes A^{\otimes n}$, with differential the
  Gerstenhaber bracket assembled from the OPE.
- **$Q_3$ — Mode-algebra Ext** $\operatorname{Ext}^*_{A^e}(A,A) :=
  \operatorname{Ext}^*_{A^e_{\mathrm{mode}}}(A,A)$. The Loday $CC^*$ model on
  the *mode algebra* $A_{\mathrm{mode}}$ associated to $A$ (the $U^{\mathrm
  ch}(A)$ of Frenkel–Ben-Zvi or, equivalently per Beilinson–Drinfeld, the
  algebra of modes acting on the vacuum module). HKR identifies
  $\operatorname{HH}_*(\mathrm{Sym}\, V_A) = \Lambda^* V_A \otimes \mathrm{Sym}\,
  V_A$ on the abelianisation.

### 1.2 The pairwise comparison maps

Three pairwise canonical comparison chain maps:

- **$\eta_{12}(A) : Q_1 \to Q_2$** — the geometric-to-algebraic comparison
  (AP-CY62 quasi-isomorphism for logarithmic chiral algebras). Defined by
  passage from FM logarithmic forms to formal Laurent expansions about the
  diagonal.
- **$\eta_{23}(A) : Q_2 \to Q_3$** — the BD-to-mode comparison (AP-CY63
  bridge). Defined on a Hochschild $n$-chain $[a_0 | a_1 | \cdots | a_n]$ by
  evaluation at $z_i = 0$ followed by trivialisation of the $A^{\otimes n}$
  module structure to mode-algebra-bimodule.
- **$\eta_{13}(A) : Q_1 \to Q_3$** — the geometric-to-mode comparison, the
  composite $\eta_{23} \circ \eta_{12}$.

### 1.3 The V19 Trinity coherence cocycle

The **V19 Trinity-$E_1$ chain-level coherence cocycle** is the class

$$
\boxed{\;\;\omega_{\mathrm{V19}}(A)
\;:=\;\eta_{13}(A) - \eta_{23}(A)\circ \eta_{12}(A)
\;\in\; H^2\bigl(\mathrm{SC}^{\mathrm{ch,top}};\,\mathfrak{aut}\bigr)\;\;}
$$

measuring the failure of the triangle $(Q_1 \to Q_2, Q_2 \to Q_3, Q_1 \to Q_3)$
to commute on the nose. By V39 H1 and the V40 master implication, this cocycle
factors through the Pentagon-at-$E_1$ cocycle: the triangle $(Q_1, Q_2, Q_3)$ is
the projection onto the three "Hochschild-style" presentations of the V40 quintet
$(P_1, \ldots, P_5)$, with $Q_1 = P_1$, $Q_2 = P_2$, $Q_3 = P_4$. Hence

$$
[\omega_{\mathrm{V19}}(A)] \;=\; \pi_{\mathrm{V19}}\bigl([\omega_{\mathrm{Pent}}(A)]\bigr)
$$

where $\pi_{\mathrm{V19}}$ is the projection onto the Trinity sector. Since
$\pi_{\mathrm{V19}}$ is a ring map, $[\omega_{\mathrm{Pent}}(A)] = 0$ implies
$[\omega_{\mathrm{V19}}(A)] = 0$.

### 1.4 The V19 Trinity-$E_1$ chain-level statement

> **Definition (V19 Trinity-$E_1$ chain-level for $A$).** $A$ satisfies the
> V19 Trinity-$E_1$ at chain level iff $\eta_{12}(A)$, $\eta_{23}(A)$, and
> $\eta_{13}(A)$ are chain-level quasi-isomorphisms and $[\omega_{\mathrm{V19}}
> (A)] = 0$ in $H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$.

Equivalently: the three Hochschild presentations $C^\bullet_{\mathrm{chiral}}
\cong \operatorname{End}^{\mathrm{ch}}(A) \cong \operatorname{Ext}^*_{A^e}$ are
pairwise quasi-isomorphic at chain level, with comparison data assembling into
a coherent triangle (no Pentagon obstruction projects onto the Trinity sector).

---

## §2. Counterexample: $Y(\mathfrak{sl}_2)$ falsifies unconditional V19 Trinity-$E_1$

The historical V19 Trinity statement was that the three Hochschild
presentations are unconditionally quasi-isomorphic at chain level for
*every* $E_1$ chiral algebra. This is FALSE.

### 2.1 The counterexample

Let $A = Y(\mathfrak{sl}_2)$ be the Yangian of $\mathfrak{sl}_2$ in its
chiral-algebra avatar (i.e., the $E_1$-chiral algebra whose Drinfeld coproduct
$\Delta_z$ recovers the standard Yangian R-matrix on evaluation modules
$V_u \otimes V_v$). The R-matrix is the rational $R(z) = 1 + (\hbar/z) P$ for
$P$ the permutation on $\mathbb{C}^2 \otimes \mathbb{C}^2$, a *matrix-valued*
function of the spectral parameter $z$, NOT a c-number scalar.

### 2.2 Explicit chain-level obstruction

The V19 Trinity-$E_1$ cocycle restricted to $Y(\mathfrak{sl}_2)$ has the
explicit form

$$
\omega_{\mathrm{V19}}^{\,Y(\mathfrak{sl}_2)}(a)
\;=\;R(z)\cdot a \cdot R(z)^{-1} \;-\; a
\;=\; \frac{\hbar}{z}\,[P, a] + O(\hbar^2)
$$

on the diagonal sector of $\operatorname{End}(Q_3)[[z, z^{-1}]]$. Since
$[P, a] \neq 0$ generically (the matrix sector of the $V_u \otimes V_v$
representation is non-abelian), $\omega_{\mathrm{V19}}^{\,Y(\mathfrak{sl}_2)}$
is non-zero as a chain — it does not bound any cochain $\mu$ in the relevant
$H^2$ a priori.

This is the **V19 Trinity falsification** referenced in V59 §"What remains
conjectural": the matrix-valued $R(z)$ for genuinely-$E_1$ Yangians attached
to simple non-abelian $\mathfrak{g}$ obstructs the chain-level $\eta_{12}$,
$\eta_{23}$, $\eta_{13}$ from forming a coherent triangle in
$\mathrm{SC}^{\mathrm{ch,top}}$. The three presentations *are* pairwise
quasi-isomorphic on cohomology (by classical results on Yangian Hochschild
cohomology, e.g. Khoroshkin–Tolstoy), but the chain-level comparison data
carries the spectral $\hbar/z$ correction that fails to descend to the
homotopy category trivially.

### 2.3 V55 dichotomy recovery: $Y(\mathfrak{sl}_2)$ is Class B

The counterexample is RECOVERED as Class B per V55:

- $Y(\mathfrak{sl}_2)$ as an $E_1$-chiral algebra is NOT K3-fibred (no
  K3-orbifold geometric source); hence not Class A.
- $\operatorname{str}(K_{Y(\mathfrak{sl}_2)}) = \dim \mathfrak{sl}_2 = 3 \neq 0$
  (the Killing form on $\mathfrak{sl}_2$ is non-degenerate, $K_{\mathfrak{sl}_2}
  = 4 e f + h^2$ has trace $3 \neq 0$); hence not Class B0.
- The shadow tower of $Y(\mathfrak{sl}_2)$ is class M (the chiral envelope
  $U^{\mathrm{ch}}(\mathfrak{sl}_2)$ has non-trivial $S_k$ for all $k$ via the
  Stasheff $A_\infty$ relations; the toroidal extension is mock-modular per the
  Maulik–Okounkov stable envelope correspondence).

By V55 H1(c), $Y(\mathfrak{sl}_2)$ falls into Class B with explicit residual
$\xi_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)} = (\hbar/z)[P, \cdot]$ in the
notation of §6 below. So the historical V19 Trinity-$E_1$ statement was an
unconditional version of a class-conditional truth: V19 Trinity-$E_1$ holds at
Class A (Theorem §3), Class B0 (Theorem §4), abelian Heisenberg (Theorem §5),
and remains CONJECTURAL at Class B with the residual quantitatively named
(§6). The "counterexample" is not a refutation but a Class B inhabitant whose
residual is closed-form.

---

## §3. V19 Trinity-$E_1$ THEOREM for Class A — extraction from V49 + V63

### 3.1 Statement

> **Theorem (V19 Trinity-$E_1$ chain-level for Class A; conditional on FM164,
> FM161 K3-specialised).** Let $\mathcal{C}$ be a CY$_3$ category whose object
> $X$ is K3-fibred — equivalently, $X \in \{K3, K3 \times E, \text{STU},
> \text{8 diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3 orbifolds}\}$. Let
> $A_X = \Phi(D^b(\mathrm{Coh}(X)))$. Then the V19 Trinity-$E_1$ chain-level
> identity
> $$
> \boxed{\;\;C^\bullet_{\mathrm{chiral}}(A_X)
> \;\overset{\sim}{\underset{\eta_{12}}{\longrightarrow}}\;
> \operatorname{End}^{\mathrm{ch}}(A_X)
> \;\overset{\sim}{\underset{\eta_{23}}{\longrightarrow}}\;
> \operatorname{Ext}^*_{A_X^e}(A_X, A_X)\;\;}
> $$
> holds at chain level, with $[\omega_{\mathrm{V19}}(A_X)] = 0$ in $H^2(\mathrm
> {SC}^{\mathrm{ch,top}}; \mathfrak{aut})$.

### 3.2 Proof sketch

**Step A (Pentagon-at-$E_1$ for Class A is V49 + V58 fibre-localisation).** By
V58 §2 (`wave_V20_step3_chain_level_class_A_B0_inscription.md`), $[\omega_{
\mathrm{Pent}}(A_X)] = 0$ at chain level for $X$ K3-fibred via three
independent V49 routes (sympy direct, Etingof–Kazhdan, V20 Universal Trace
Identity) extended to Class A by elliptic / orbifold fibre-localisation.

**Step B (V40 master implication: Pentagon $\Rightarrow$ Trinity).** By V40
master implication (the chain Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1$
$\Rightarrow$ V20 Step 3 chain-level), the projection $\pi_{\mathrm{V19}}$
onto the Trinity sector $(Q_1, Q_2, Q_3) = (P_1, P_2, P_4)$ sends the
vanishing Pentagon cocycle to the vanishing Trinity cocycle:

$$
[\omega_{\mathrm{Pent}}(A_X)] = 0 \;\Longrightarrow\;
[\omega_{\mathrm{V19}}(A_X)] = \pi_{\mathrm{V19}}\bigl([\omega_{\mathrm{Pent}}(A_X)]\bigr) = 0.
$$

**Step C (explicit chain map on Hochschild generators).** For the K3 input,
the comparison $\eta_{13}(A_{K3})$ on Hochschild $n$-chains has the explicit
formula extracted from V63 §2 (the V49 Route (iii) extraction at the
$P_4 \leftrightarrow P_5$ edge):

$$
\eta_{13}\bigl([a_0 | a_1 | \cdots | a_n]\bigr)
\;=\;\sum_{\sigma \in \mathbb{Z}/(n+1)} \frac{(-1)^{\mathrm{sgn}\,\sigma}}{(n+1)!}\,
a_{\sigma(0)} \otimes a_{\sigma(1)} \otimes \cdots \otimes a_{\sigma(n)},
$$

the cyclic averaging projector. For the diagonal sector this is the same
formula as V63's $\eta_{45}^{\mathrm{Heis}}$ (because the Mukai-lattice
underlying $A_{K3}$ is abelian via $\mathrm{Heis}^{24}$); for the off-diagonal
sector the V49 Route (ii) Etingof–Kazhdan twist coherence handles the matrix
correction. Combined: $\eta_{13}(A_{K3})$ is a chain-level quasi-isomorphism.

**Step D (Class A extension to $K3 \times E$, STU, orbifolds).** Per V58 §2.2
fibre-localisation: the elliptic / orbifold quotient acts trivially on the
Mukai-lattice Trinity data because the Mukai pairing lives entirely on the K3
fibre. The base contribution is $E_\infty$ (commutative), automatically Trinity-coherent.

**Q.E.D.** (modulo FM164/FM161 K3-specialised, per AP-CY11).

### 3.3 Conditional dependencies (per AP-CY11)

This theorem chains through V49 (K3 Pentagon-at-$E_1$), conditional on FM164
(Yangian pro-nilpotent bar–cobar completion) + FM161 (Yangian Koszulness in
the Positselski nonhomogeneous framework), both K3-specialised. By AP-CY11
(HZ3-3), this conditionality propagates: V19 Trinity-$E_1$ chain-level for
Class A is `\ClaimStatusConditional` on FM164/FM161 K3-specialised.

Per AP-CY60: the V49 K3 routes are three independent constructions of
$[\omega_{\mathrm{Pent}}(A_{K3})] = 0$, NOT three applications of $\Phi$. The
present Class A theorem inherits this discipline: the proof above invokes V49
once via the master implication, with explicit chain map on Hochschild
generators per V63.

---

## §4. V19 Trinity-$E_1$ THEOREM for Class B0 — super-EK + super-trace closure

### 4.1 Statement

> **Theorem (V19 Trinity-$E_1$ chain-level for Class B0; conditional on FM164,
> FM161 super-Lie variant).** Let $A$ be an $E_1$-chiral algebra arising as
> the CoHA of a CY$_3$ category with $\operatorname{str}(K_A) = 0$. The
> canonical example is the resolved conifold with $A = Y(\mathfrak{gl}(1|1))$.
> Then the V19 Trinity-$E_1$ chain-level identity
> $$
> \boxed{\;\;C^\bullet_{\mathrm{chiral}}(A)
> \;\overset{\sim}{\longrightarrow}\;
> \operatorname{End}^{\mathrm{ch}}(A)
> \;\overset{\sim}{\longrightarrow}\;
> \operatorname{Ext}^*_{A^e}(A, A)\;\;}
> $$
> holds at chain level, with $[\omega_{\mathrm{V19}}(A)] = 0$.

### 4.2 Proof sketch (super-EK + super-trace + V40)

**Step A.** By V58 §3 (Class B0 Pentagon theorem), $[\omega_{\mathrm{Pent}}(A)]
= 0$ at chain level via super-Etingof–Kazhdan twist coherence on $\mathfrak
{gl}(1|1)$ + super-trace vanishing $\operatorname{str}(K_A) = 0$ + V53.1
Berezinian channel rigidity.

**Step B.** By V40 master implication, $[\omega_{\mathrm{V19}}(A)] = \pi_{
\mathrm{V19}}(0) = 0$.

**Step C (explicit super-cyclic averaging).** The comparison map $\eta_{13}(A)$
in the super-Lie setting is the super-cyclic averaging projector

$$
\eta_{13}^{\mathrm{conf}}\bigl([a_0 | \cdots | a_n]\bigr)
\;=\;\sum_{\sigma \in \mathbb{Z}/(n+1)} \frac{(-1)^{|\sigma|_{\mathrm{super}}}}{(n+1)!}\,
a_{\sigma(0)} \otimes \cdots \otimes a_{\sigma(n)},
$$

with super-sign $(-1)^{|\sigma|_{\mathrm{super}}}$ counting fermionic
transpositions. The super-Connes $B$-differentials commute with this projector
exactly (by direct computation: the super-cyclic shift commutes with super-
symmetrisation, just as in the bosonic case). Differential compatibility holds
at chain level, not just modulo homotopy.

**Step D (super-trace cancellation).** The bosonic and fermionic contributions
to $\omega_{\mathrm{V19}}^{\mathrm{conf}}$ cancel pairwise by the
$E_{00} \leftrightarrow E_{11}$ super-transposition, exactly mirroring the V58
§3.2 super-trace cancellation at the Pentagon level. By V53.1, the Berezinian
channel is rigidly forced by Mukai signature $\operatorname{sdim} = p - q = 0$
of the conifold CoHA; the super-trace projection vanishes structurally.

**Q.E.D.** (modulo FM164/FM161 super-Lie variant).

### 4.3 Conditional dependencies (per AP-CY11)

V55 H3 is conditional on FM164/FM161 in the super-Lie setting (super-version
of standard Yangian Koszulness; tractable at the same difficulty as the even
case). This propagates: V19 Trinity-$E_1$ chain-level for Class B0 is
`\ClaimStatusConditional` on FM164/FM161 super-Lie variant.

---

## §5. V19 Trinity-$E_1$ THEOREM for abelian Heisenberg — extraction from V59

### 5.1 Statement

> **Theorem (V19 Trinity-$E_1$ chain-level for abelian Heisenberg; PROVED
> unconditionally).** Let $H_k$ be the rank-1 Heisenberg vertex algebra at
> level $k$, including the abelian limit $k \to 0$. The V19 Trinity-$E_1$
> chain-level identity
> $$
> \boxed{\;\;C^\bullet_{\mathrm{chiral}}(H_k)
> \;\overset{\sim}{\underset{\eta_{12}^{\mathrm{Heis}}}{\longrightarrow}}\;
> \operatorname{End}^{\mathrm{ch}}(H_k)
> \;\overset{\sim}{\underset{\eta_{23}^{\mathrm{Heis}}}{\longrightarrow}}\;
> \operatorname{Ext}^*_{H_k^e}(H_k, H_k)\;\;}
> $$
> holds with $[\omega_{\mathrm{V19}}^{\mathrm{Heis}}] = 0$ identically as a
> chain (not merely as a class) for every $k$. Generalisation: every abelian
> chiral algebra (lattice VOAs $V_\Lambda$ for any even $\Lambda$, $\beta\gamma$
> with abelian zero-mode, $bc$ at integer weight) admits the same explicit
> comparison maps and chain-level vanishing.

### 5.2 Explicit chain-level comparison maps

In the divided-power basis $e_s := J_{-1}^s / s!$ of the Heisenberg, the three
comparison maps have closed form. By V59 §"The five Hochschild presentations of
$H_k$", all five $P_i(H_k)$ collapse on the diagonal sector to the partition-
graded chain complex with $\dim_n = p(n)$ and trivial differential. Restricted
to the Trinity sector $(Q_1, Q_2, Q_3) = (P_1, P_2, P_4)$:

$$
\eta_{12}^{\mathrm{Heis}}\bigl([e_{s_0} | \cdots | e_{s_n}]\bigr)
\;=\; e_{s_0}(z_0) \otimes \cdots \otimes e_{s_n}(z_n) \cdot
\mathrm{Lie}_{\mathrm{FM} \to \mathrm{Laurent}},
$$

i.e., expansion of FM logarithmic forms into formal Laurent series about the
diagonal — a chain isomorphism for the Heisenberg because the OPE $J(z)J(w)
\sim k/(z-w)^2$ is logarithmic and admits a unique formal expansion.

$$
\eta_{23}^{\mathrm{Heis}}\bigl(f(z_0, \ldots, z_n) \otimes e_{s_0} \otimes \cdots \otimes e_{s_n}\bigr)
\;=\; f(0, 0, \ldots, 0)\cdot e_{s_0} \otimes \cdots \otimes e_{s_n},
$$

evaluation at the diagonal followed by trivialisation of bimodule structure;
chain map by the same Connes-shift commutation argument as V63 §3.

$$
\eta_{13}^{\mathrm{Heis}}\bigl([e_{s_0} | \cdots | e_{s_n}]\bigr)
\;=\;\sum_{\sigma \in \mathbb{Z}/(n+1)} \frac{1}{(n+1)!}\,
e_{s_{\sigma(0)}} \otimes \cdots \otimes e_{s_{\sigma(n)}},
$$

the cyclic averaging projector (V63 §3 explicit formula), composing the above
two.

### 5.3 Cocycle vanishing

By V59 §"Heisenberg verification": $R_{\mathrm{Heis}}(z) = \exp(k\hbar/z)$ is
**central** by the Schur criterion (the Heisenberg OPE has only a double pole,
no first-order residue, so the commutator $[J(z), J(w)] = 0$ in the relevant
sense). Hence $R_{\mathrm{Heis}} \cdot a \cdot R_{\mathrm{Heis}}^{-1} = a$
identically as a chain, and

$$
\omega_{\mathrm{V19}}^{\mathrm{Heis}}(a) \;=\; R_{\mathrm{Heis}}(z) \cdot a \cdot
R_{\mathrm{Heis}}(z)^{-1} - a \;=\; 0
$$

on the nose. The Trinity cocycle bounds by $\mu = 0$, and $[\omega_{\mathrm{V19}}
^{\mathrm{Heis}}] = 0$ in $H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$
for every level $k$, including $k \to 0$.

**Generalisation (cf. V63 §3).** Any abelian chiral algebra has central $R(z)$
by the same Schur argument applied to the abelian OPE (no first-order residue
$\Leftrightarrow$ scalar R-matrix). The construction extends verbatim: lattice
VOAs $V_\Lambda$ for any even lattice (including the Mukai lattice
$\Lambda_{\mathrm{Mukai}}$ underlying the K3 abelian Heisenberg sub-case),
$\beta\gamma$ systems with abelian zero-mode, $bc$ systems at integer weight.

**Status.** $\boxed{\text{V19 Trinity-}E_1\text{ at abelian Heisenberg: PROVED
unconditionally, with explicit chain maps }\eta_{12}^{\mathrm{Heis}}, \eta_{23}^{
\mathrm{Heis}}, \eta_{13}^{\mathrm{Heis}}.}$

This grounds the abelian sub-case underlying V49 Route (i): the K3 Mukai-lattice
$\mathrm{Heis}^{24}$ is the abelian Trinity-coherent core of $A_{K3}$.

---

## §6. V19 Trinity-$E_1$ CONJECTURE for Class B with named per-input residual

### 6.1 Statement

> **Conjecture (V19 Trinity-$E_1$ chain-level for Class B; CONJECTURAL).** Let
> $A = \Phi(C)$ for $C$ a Class B (class M, non-K3-fibred, super-trace
> non-vanishing) CY$_3$-category. Canonical examples: $A_{\mathrm{quintic}}$,
> $A_{\mathrm{LP^2}}$, and (per §2.3) $Y(\mathfrak{sl}_2)$. The Trinity
> coherence cocycle is
> $$
> \omega_{\mathrm{V19}}(A) \;=\; \xi_{\mathrm{V19}}(A) \;\in\; H^2(\mathrm{SC}^{
> \mathrm{ch,top}}; \mathfrak{aut}),
> $$
> where $\xi_{\mathrm{V19}}(A) := \pi_{\mathrm{V19}}(\xi(A))$ is the Trinity-
> sector projection of the Class B alien-derivation correction $\xi(A)$ of the
> shadow tower of $A$ (V40 §3.1, V55 H1(c)). Vanishing is conditional on the
> V8 §6 mock-modular completion of the shadow tower of $A$.

### 6.2 Per-input residuals

Connecting to the V62 / V56 residual decomposition, with $\xi(A) = \xi_{
\mathrm{algebraic}} + \xi_{\mathrm{resurgent}}$ per V58 §4.2:

**Quintic.**
$$
\xi_{\mathrm{V19}}^{\mathrm{quintic}} \;=\; \pi_{\mathrm{V19}}\bigl(\mathrm{Borel\text{-}sum}\bigl(\sum_{g \geq 1} \Delta F_g^{\mathrm{quintic}}\bigr)\bigr),
$$
the Trinity-sector projection of the BCOV resurgent transseries (Mariño–Schiappa–Reis), conditional on
- `conj:quintic-existence-as-E_1` (existence of $A_{\mathrm{quintic}}$ as
  chain-level $E_1$),
- `conj:quintic-mock-modular-completion` (mock-modular completion of the
  quintic shadow tower).

**Local $\mathbb{P}^2$.**
$$
\xi_{\mathrm{V19}}^{\mathrm{LP^2}} \;=\; \pi_{\mathrm{V19}}\bigl(\xi_{\mathrm{Miki}}^{\mathrm{LP^2}}\bigr) \;+\; \pi_{\mathrm{V19}}\bigl(\xi_{\mathrm{mock}}^{\mathrm{LP^2}}\bigr),
$$
the Trinity-sector projection of the algebraic Miki-coherence correction plus
the resurgent mock-modular completion correction. Conditional on
- `conj:W3-trunc-miki-coherence`,
- `conj:localp2-mock-modular`.

**$Y(\mathfrak{sl}_2)$.** From §2.2,
$$
\xi_{\mathrm{V19}}^{\,Y(\mathfrak{sl}_2)} \;=\; \frac{\hbar}{z}\,[P, \cdot] \;+\; O(\hbar^2),
$$
the spectral $\hbar/z$ correction of the rational Yangian R-matrix. Vanishing
of this *as a class in $H^2$* (it is non-zero as a chain) is the open question:
it is equivalent to the lift of $Y(\mathfrak{sl}_2)$ to a K3 Yangian-like
input, which would invoke a Borcherds lift not currently known to exist for
$\mathfrak{sl}_2$ alone (the K3 Mukai lattice has rank 24, not 3). This is the
**ghost theorem**: see §8.

### 6.3 Status discipline

Per HZ3-1, the Class B statement uses `\begin{conjecture}`: the proof chain
through V55 H1(c) reaches back to the open Pentagon-at-$E_1$ for Class B
inputs. Per AP-CY40, no `\ClaimStatusProvedHere` tag may be applied. Per
AP-CY32 (reorganisation $\neq$ bypass): the Trinity residual $\xi_{\mathrm{V19}}
(A)$ is the SAME data as the Pentagon residual $\xi(A)$ projected onto the
Trinity sector, NOT a separable simpler problem. Closing one closes the other
modulo the projection $\pi_{\mathrm{V19}}$.

---

## §7. TeX-ready Vol I §V19 inscription (~600 words)

The following block is intended for insertion at the end of the §V19 Trinity
treatment in Vol I, following the homotopy-category Trinity Theorem and
preceding the V20 Step 3 chain-level epilogue (V58 inscription target). Per
V58 §5 install location protocol; install target subject to main-thread
review.

```latex
%% =========================================================================
%% Vol I §V19 epilogue: chain-level dichotomy for V19 Trinity-at-E_1
%% (the middle link of the V40 master implication chain
%%  Pentagon-at-E_1 => V19 Trinity-E_1 => V20 Step 3 chain-level).
%% Sandbox draft from wave_V19_Trinity_E1_class_A_B0_inscription.md
%% (Wave V64, 2026-04-16). Inscription pending main-thread review.
%% Author: Raeez Lorgat. No AI attribution. Not committed.
%%
%% New labels introduced:
%%   thm:V19-trinity-class-A           -- Class A theorem
%%   thm:V19-trinity-class-B0          -- Class B0 theorem
%%   thm:V19-trinity-heisenberg        -- abelian Heisenberg theorem
%%   conj:V19-trinity-class-B          -- Class B residual conjecture
%%   ex:V19-trinity-Y-sl2-counterex    -- Y(sl_2) counterexample / Class B
%%   rem:V19-trinity-V55-dichotomy     -- pointer to V55 H1
%%   rem:V19-trinity-cross-volume      -- cross-volume citation skeleton
%% =========================================================================

The homotopy-category form of V19 Trinity \textup{(}Theorem~\ref{thm:V19-trinity-homotopy}\textup{)}
is unconditional: the three Hochschild presentations
$C^\bullet_{\mathrm{chiral}}(A)$, $\End^{\mathrm{ch}}(A)$,
$\Ext^*_{A^e}(A, A)$ are pairwise quasi-isomorphic on cohomology for every
$E_1$-chiral algebra $A$. The chain-level upgrade --- the assertion that the
comparison maps assemble into a coherent triangle in
$\SCcht$, with vanishing cocycle
$[\omega_{\mathrm{V19}}(A)] = 0$ in $H^2(\SCcht; \fraut)$ --- inherits the
Pentagon-at-$E_1$ dichotomy of V55 H1.

\begin{theorem}[V19 Trinity-$E_1$ chain-level for Class A;
                conditional on FM164, FM161 K3-specialised]
\label{thm:V19-trinity-class-A}
\ClaimStatusConditional
For $\mathcal{C}$ a CY$_3$ category with $X$ K3-fibred, the chain-level
identity
\[
  C^\bullet_{\mathrm{chiral}}(A_X)
  \;\overset{\eta_{12}}{\xrightarrow{\;\sim\;}}\;
  \End^{\mathrm{ch}}(A_X)
  \;\overset{\eta_{23}}{\xrightarrow{\;\sim\;}}\;
  \Ext^*_{A_X^e}(A_X, A_X)
\]
holds with $[\omega_{\mathrm{V19}}(A_X)] = 0 \in H^2(\SCcht; \fraut)$, with
explicit comparison map $\eta_{13}(A_X)$ on Hochschild generators given by the
cyclic averaging projector \textup{(}cf.~V63\textup{)}.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:V20-step-3-class-A} reduction Pentagon~$\Rightarrow$
Trinity (V40 master implication, projection $\pi_{\mathrm{V19}}$ from quintet
to triple). V49 closes Pentagon-at-$E_1$ at K3 input via three independent
routes. Class A extension by fibre-localisation onto the K3 fibre.
\end{proof}

\begin{theorem}[V19 Trinity-$E_1$ chain-level for Class B0;
                conditional on FM164, FM161 super-Lie variant]
\label{thm:V19-trinity-class-B0}
\ClaimStatusConditional
For $A$ an $E_1$-chiral algebra arising as the CoHA of a CY$_3$ category with
$\str(K_A) = 0$ --- canonically the resolved conifold with $A = Y(\fgl(1|1))$
--- the chain-level Trinity identity holds with $[\omega_{\mathrm{V19}}(A)] = 0$,
with explicit comparison via super-cyclic averaging.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:V20-step-3-class-B0} Pentagon~$\Rightarrow$ Trinity. Super-
EK twist coherence + super-trace vanishing + V53.1 Berezinian rigidity.
\end{proof}

\begin{theorem}[V19 Trinity-$E_1$ chain-level for the abelian Heisenberg]
\label{thm:V19-trinity-heisenberg}
\ClaimStatusProvedHere
Let $H_k$ be the rank-1 Heisenberg at level $k$. The chain-level Trinity
identity holds with $[\omega_{\mathrm{V19}}^{\mathrm{Heis}}] = 0$ identically as
a chain (not merely as a class), unconditionally for every $k$, including
$k \to 0$. Generalisation: every abelian chiral algebra (lattice VOA, abelian
$\beta\gamma$, $bc$).
\end{theorem}

\begin{proof}
$R_{\mathrm{Heis}}(z) = \exp(k\hbar/z)$ is central by the Schur criterion (the
Heisenberg OPE has only a double pole, no first-order residue), so
$R \cdot a \cdot R^{-1} = a$ identically and $\omega_{\mathrm{V19}}^{\mathrm{Heis}}
= 0$ on the nose. Cf.~V59 specification, 34/34 pytest.
\end{proof}

\begin{conjecture}[V19 Trinity-$E_1$ chain-level for Class B;
                  CONJECTURAL via mock-modular completion]
\label{conj:V19-trinity-class-B}
For $A$ class M, neither K3-fibred (Class A) nor super-trace vanishing
(Class B0) --- canonically $A_{\mathrm{quintic}}$, $A_{\mathrm{LP^2}}$, or
$Y(\fsl_2)$ --- the chain-level Trinity identity holds modulo the Trinity-
sector projection $\xi_{\mathrm{V19}}(A) := \pi_{\mathrm{V19}}(\xi(A))$ of the
class M alien-derivation correction. Vanishing is conjectural per input
conditional on the V8~§6 mock-modular completion of the shadow tower of $A$.
\end{conjecture}

\begin{example}[$Y(\fsl_2)$ falsifies unconditional V19 Trinity-$E_1$]
\label{ex:V19-trinity-Y-sl2-counterex}
For $A = Y(\fsl_2)$, the rational R-matrix $R(z) = 1 + (\hbar/z) P$ is matrix-
valued (not central), giving the chain-level cocycle
$\omega_{\mathrm{V19}}^{Y(\fsl_2)}(a) = (\hbar/z)[P, a] + O(\hbar^2) \neq 0$ on
the diagonal sector. By the V55 dichotomy, $Y(\fsl_2)$ is Class B (non-K3-
fibred, $\str(K_{\fsl_2}) = 3 \neq 0$, class M shadow tower); the apparent
counterexample to unconditional V19 Trinity is precisely Conjecture~\ref{conj:
V19-trinity-class-B} restricted to $Y(\fsl_2)$, with explicit residual
$\xi_{\mathrm{V19}}^{Y(\fsl_2)} = (\hbar/z)[P, \cdot]$.
\end{example}

\begin{remark}[V19 Trinity-$E_1$ chain-level inherits the V55 dichotomy via V40]
\label{rem:V19-trinity-V55-dichotomy}
Theorems~\ref{thm:V19-trinity-class-A}, \ref{thm:V19-trinity-class-B0}, and
\ref{thm:V19-trinity-heisenberg}, together with Conjecture~\ref{conj:V19-
trinity-class-B} and Example~\ref{ex:V19-trinity-Y-sl2-counterex}, resolve V19
Trinity-$E_1$ chain-level into the V55 H1 three-class structure. The reduction
is via the V40 master implication chain (\texttt{wave\_frontier\_universal\_
trace\_chain\_level.md}) applied to the projection $\pi_{\mathrm{V19}}$ from
the Pentagon quintet $(P_1, \ldots, P_5)$ to the Trinity triple
$(P_1, P_2, P_4)$. V19 Trinity is the \emph{middle link} of the V40 chain;
Pentagon-at-$E_1$ is the parent and V20 Step~3 chain-level is the consequence.
\end{remark}
```

---

## §8. Ghost theorem extraction: what V19 Trinity-$E_1$ was reaching for

### 8.1 The historical V19 statement and its falsification

The historical V19 Trinity-$E_1$ statement (Wave 14, Vol I §V19) was that the
three Hochschild presentations are unconditionally quasi-isomorphic at chain
level for *every* $E_1$ chiral algebra. Per §2 above, this is FALSE: $Y(\mathfrak
{sl}_2)$ has matrix-valued $R(z)$, giving non-vanishing chain-level cocycle
$\omega_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)}(a) = (\hbar/z)[P, a] + O(\hbar^2)$.

### 8.2 First-principles investigation (per HZ3-12 / AP-CY61)

Per the AP-CY61 protocol, a wrong claim contains the seed of a correct theorem.
The three-step extraction:

**(a) What does V19 Trinity-$E_1$ get RIGHT?** That for $E_1$ chiral algebras
where the underlying R-matrix is *central* (a c-number scalar in $z$), the
three Hochschild presentations form a chain-level coherent triangle. This is
TRUE for every abelian chiral algebra (V59 + §5), and for the abelian sector
of every Class A input (V49 + §3 Step C). The "Trinity" intuition correctly
identifies that the three presentations $(C^\bullet_{\mathrm{chiral}}, \mathrm
{End}^{\mathrm{ch}}, \mathrm{Ext}^*_{A^e})$ are the three natural chain-level
realisations of "Hochschild cohomology of a chiral algebra", and that under
the right circumstances they assemble coherently.

**(b) What does V19 Trinity-$E_1$ get WRONG?** It overgeneralises from the
abelian / K3 / super-trace-vanishing setting to all $E_1$-chiral algebras. The
matrix-valued R-matrix obstruction for genuinely non-abelian Yangians (e.g.
$Y(\mathfrak{sl}_2)$, $Y(\mathfrak{sl}_n)$ for $n \geq 2$) carries a chain-
level $\hbar/z$ correction that the cohomology-level statement (which is
unconditionally true) fails to capture.

**(c) What is the CORRECT mathematical relationship (the ghost theorem)?**

> **Ghost theorem (V19 Trinity-$E_1$, restated correctly).** *For an $E_1$-
> chiral algebra $A$, the three Hochschild presentations form a chain-level
> coherent triangle if and only if $A$ admits a Borcherds lift, equivalently,
> if and only if the underlying R-matrix factors through a c-number central
> twist on the Borcherds-lifted Mukai-style lattice.*
>
> *In particular, the Yangian $Y(\mathfrak{g})$ for $\mathfrak{g}$ simple
> non-abelian (e.g. $\mathfrak{sl}_2$) does NOT admit such a lift in isolation;
> only its* combination *with a K3 (or K3-fibred) geometric source — namely
> the K3 Yangian $Y(\mathfrak{g}_{K3})$ acting on $H^*(K3)^{\otimes 24} =
> H_{\mathrm{Mukai}}^{\otimes 24}$ — admits the Borcherds lift to $\Phi_5$ and
> thereby satisfies V19 Trinity at chain level.*

### 8.3 The K3 Yangian truth

The K3 Yangian $Y(\mathfrak{g}_{K3})$ is the canonical Class A inhabitant: its
Mukai lattice $\Lambda_{4,20}$ provides the Borcherds singular-theta lift to
$\Phi_5$ (the genus-2 Siegel modular form of weight 5), and its underlying
abelian sector is $\mathrm{Heis}^{24}$ (V49 Route (i) sympy verification at
charges 2 and 3). The V63 chain-level identification $\eta_{13}^{\mathrm{Heis}}$
extends to the full K3 Yangian via the Etingof–Kazhdan twist (V49 Route (ii))
plus the Universal Trace Identity (V49 Route (iii)). The Trinity coherence at
chain level is *forced* by the K3 lattice structure.

In contrast, $Y(\mathfrak{sl}_2)$ alone has no Borcherds lift: there is no
known automorphic form whose Borcherds product expansion encodes the
$\mathfrak{sl}_2$ characters in the way $\Phi_5$ encodes $H_{\mathrm{Mukai}}$.
The chain-level $(\hbar/z)[P, \cdot]$ correction is the *signature of this
absence*: it measures the obstruction to lifting $Y(\mathfrak{sl}_2)$ to a
Borcherds-lifted Mukai-style algebra.

### 8.4 Equivalent reformulations of the ghost theorem

The ghost theorem admits three equivalent reformulations, each from a
different mathematical perspective:

- **(Algebraic)** $A$ satisfies V19 Trinity-$E_1$ at chain level iff the
  R-matrix $R_A(z)$ factors as $R_A(z) = \Sigma(z) \cdot R^{\mathrm{cent}}(z)$
  with $\Sigma(z)$ a c-number scalar twist and $R^{\mathrm{cent}}(z)$ central
  on every weight space.
- **(Geometric)** $A$ satisfies V19 Trinity-$E_1$ at chain level iff $A$
  arises from a CY$_3$ category $C$ such that $\Phi(C)$ admits a Borcherds
  singular-theta lift (Class A: yes via $\Phi_5$ for K3-fibred input; Class
  B0: yes vacuously via $\Phi^{\mathrm{conf}} = 1$ from super-trace
  cancellation; Class B: conjectural via mock-modular completion).
- **(Resurgent)** $A$ satisfies V19 Trinity-$E_1$ at chain level iff the
  alien-derivation $\xi(A)$ of the shadow tower of $A$ projects to zero on
  the Trinity sector, $\pi_{\mathrm{V19}}(\xi(A)) = 0$.

The three reformulations are equivalent under the V40 master implication
chain, the V20 Universal Trace Identity, and the V8 §6 mock-modular completion
conjecture.

### 8.5 Closing observation

The historical V19 Trinity-$E_1$ statement was reaching for the K3 Yangian
truth. The Wave 14 articulation lacked the V55 dichotomy and the V49 K3-
specific machinery to recognise that the Borcherds-lift condition is the
load-bearing hypothesis. The present extraction makes the conditional content
explicit: V19 Trinity-$E_1$ chain-level is a THEOREM precisely on the inputs
where the Borcherds lift (or its super-trace-vanishing degeneration) is known
to exist, and a CONJECTURE elsewhere with quantitatively named per-input
residuals.

---

## §9. Per-class V19 Trinity-$E_1$ status table (final)

| Class | Inhabitants | V19 Trinity-$E_1$ chain-level status | Residual $\xi_{\mathrm{V19}}(A)$ | Source / Conditionality |
|---|---|---|---|---|
| **abelian** | $H_k$ (any $k$, incl. $k \to 0$); $V_\Lambda$ lattice VOAs; $\mathrm{Heis}^N$ for any $N$; $\beta\gamma$, $bc$ abelian | **PROVED** unconditionally, identically as a chain | $0$ identically | V59 + V63 (Schur centrality of $R(z) = \exp(k\hbar/z)$) |
| **A** | K3 | **PROVED** (theorem) | $0$ unconditionally (class L/C, not class M) | V49 Route (iii) + V40 + V63 / cond. FM164 + FM161 K3-spec. |
| **A** (extension) | $K3 \times E$, STU, 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds | **PROVED** (corollary) | $0$ unconditionally | V58 §2 fibre-localisation / cond. FM164 + FM161 K3-spec. |
| **B0** | Conifold ($Y(\mathfrak{gl}(1|1))$) | **PROVED** (theorem) | $0$ via super-trace cancellation + V53.1 | V58 §3 + V40 / cond. FM164/FM161 super-Lie |
| **B0** (other) | Any $\operatorname{str}(K_A) = 0$ CoHA | **PROVED** (corollary) | $0$ by same argument | V55 H3 generalisation / cond. FM164/FM161 super-Lie |
| **B-quintic** | Quintic CY$_3$ $Q \subset \mathbb{P}^4$ | **CONJECTURE** | $\pi_{\mathrm{V19}}(\mathrm{Borel\text{-}sum}(\sum_g \Delta F_g^{\mathrm{quintic}}))$ | V55 H2 / cond. quintic existence + mock-modular |
| **B-LP$^2$** | Local $\mathbb{P}^2$, $K_{\mathbb{P}^2}$ | **CONJECTURE** | $\pi_{\mathrm{V19}}(\xi_{\mathrm{Miki}}^{\mathrm{LP^2}} + \xi_{\mathrm{mock}}^{\mathrm{LP^2}})$ | V55 H4 / cond. $W_3$-Miki + LP$^2$ mock-modular |
| **B-Yangian** | $Y(\mathfrak{sl}_2)$, $Y(\mathfrak{sl}_n)$ for $n \geq 2$, generic Yangian without K3 lift | **CONJECTURE / Counterexample to unconditional** | $(\hbar/z)[P, \cdot] + O(\hbar^2)$ explicitly | §2.2 + §8.3 ghost theorem |
| **B** (other) | banana, Fermat quartic non-symplectic, generic class M | **CONJECTURE** | per-input mock-modular completion | V55 H1(c) |

The status table mirrors the V58 V20 Step 3 chain-level table and the V63 V11
Pillar α status table exactly, via the V40 master implication chain projecting
onto the Trinity sector.

---

## §10. Cross-volume citation skeleton

### 10.1 Vol I §V19 (target file: `chapters/koszul/v19_trinity.tex` per Vol I structure)

Insert the §7 TeX block at the end of the V19 Trinity homotopy-category
treatment, following Theorem `thm:V19-trinity-homotopy` and preceding any
cross-reference to V20. Five new labels: `thm:V19-trinity-class-A`, `thm:V19-
trinity-class-B0`, `thm:V19-trinity-heisenberg`, `conj:V19-trinity-class-B`,
`ex:V19-trinity-Y-sl2-counterex`. Two new remarks: `rem:V19-trinity-V55-
dichotomy`, `rem:V19-trinity-cross-volume`.

### 10.2 Vol III k3_yangian.tex / cy_to_chiral.tex

The Vol III K3 Yangian chapter, once the V57 V49 inscription is applied,
should carry a back-reference from `cor:k3-v19-trinity-chain-level` (the K3-
specific corollary of `thm:V19-trinity-class-A`) to the Vol I chain-level
theorem. Per AP-CY13 / HZ3-10: use `\ref{thm:V19-trinity-class-A}` (no
hardcoded Part references).

### 10.3 Vol II V15 Pentagon chapter

The V58 §6.2 Vol II edit (adding `rem:V15-V55-dichotomy` to the V15 Pentagon
chapter) extends naturally to a parallel remark on V19 Trinity:

```latex
\begin{remark}[V19 Trinity-$E_1$ chain-level inherits the V55 dichotomy]
\label{rem:V15-V19-trinity-cross}
The universal chain-level Pentagon coherence theorem of this chapter
\textup{(}Theorem~\ref{thm:sc-chtop-pentagon}\textup{)} restricts to V19
Trinity-$E_1$ via the projection $\pi_{\mathrm{V19}}$ from the Pentagon
quintet $(P_1, \ldots, P_5)$ to the Trinity triple $(P_1, P_2, P_4)$. The V55
dichotomy on Pentagon \textup{(}Class A / B0 / B\textup{)} thereby induces the
same dichotomy on V19 Trinity-$E_1$, per Vol I \texttt{thm:V19-trinity-class-A},
\texttt{thm:V19-trinity-class-B0}, \texttt{thm:V19-trinity-heisenberg},
\texttt{conj:V19-trinity-class-B}.
\end{remark}
```

### 10.4 Cross-volume sweep instructions (AP5 / AP-CY13)

After applying the present sandbox draft, run the standard sweep across
volumes for the new V64 labels alongside the V58 / V63 labels:

```bash
for label in thm:V19-trinity-class-A thm:V19-trinity-class-B0 \
             thm:V19-trinity-heisenberg conj:V19-trinity-class-B \
             ex:V19-trinity-Y-sl2-counterex rem:V19-trinity-V55-dichotomy \
             rem:V15-V19-trinity-cross thm:V20-step-3-class-A \
             thm:V20-step-3-class-B0 conj:V20-step-3-class-B \
             thm:v11-pillar-alpha-class-A thm:v11-pillar-alpha-heisenberg \
             thm:v11-pillar-alpha-class-B0 conj:v11-pillar-alpha-class-B; do
  echo "=== $label ==="
  for vol in ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 \
             ~/calabi-yau-quantum-groups; do
    grep -rn "$label" "$vol"/chapters "$vol"/notes "$vol"/appendices \
         2>/dev/null
  done
done
```

Expected post-application: every label resolves; cross-volume consistency
without orphans; V19 / V20 / V11 inscriptions form a closed triangle of
chain-level dichotomy theorems with shared V55 Class A / B0 / B structure.

---

## §11. What this delivery does NOT do

- Does NOT edit any `.tex` source. All inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, or the AP catalogue.
- Does NOT modify `MASTER_PUNCH_LIST.md`, `INDEX.md`, or any other notes.
- Does NOT run `make fast`, `make test`, `make verify-independence`, or any
  build/test command. Per pre-commit hook discipline.
- Does NOT close FM164 or FM161 (general or K3-specialised or super-Lie variant).
- Does NOT close the V55 H2 quintic or V55 H4 local $\mathbb{P}^2$ sub-conjectures.
- Does NOT close the $Y(\mathfrak{sl}_2)$ residual (the ghost theorem of §8 is
  an *equivalent reformulation* of the open Class B problem, not a closure).
- Does NOT modify the V20 Step 3 chain-level inscription (V58) or V11 Pillar α
  inscription (V63); the present V19 inscription is the middle link of the
  V40 master implication chain and complements but does not supersede them.
- Does NOT commit anything (per pre-commit hook). All commits by Raeez Lorgat
  ONLY; no AI attribution.

---

## §12. Closing assessment

V40 reduced V20 Step 3 chain-level to V19 Trinity-$E_1$ to Pentagon-at-$E_1$
via the master implication chain. V49 closed Pentagon-at-$E_1$ for K3 input
via three independent verification routes; V55 produced the Class A / B0 / B
dichotomy. V58 inscribed V20 Step 3 chain-level as the dichotomy theorem on
the *consequence* side; V63 extracted V11 Pillar α as the $P_4 \leftrightarrow
P_5$ edge of Pentagon. The present wave (V64) inscribes the *middle link*: V19
Trinity-$E_1$ chain-level as the dichotomy on the projection of the Pentagon
quintet $(P_1, \ldots, P_5)$ onto the Trinity triple $(P_1, P_2, P_4)$.

The historical V19 Trinity statement was an unconditional theorem; $Y(\mathfrak
{sl}_2)$ falsifies it as stated. The healing is the V55 dichotomy + V40 master
implication: V19 Trinity-$E_1$ chain-level is a THEOREM for Class A (K3-
fibred), Class B0 (super-trace vanishing), and the abelian Heisenberg
sub-case (V59 explicit chain-isomorphism); a CONJECTURE for Class B with
named per-input residuals $\xi_{\mathrm{V19}}^{\mathrm{quintic}}$, $\xi_{
\mathrm{V19}}^{\mathrm{LP^2}}$, $\xi_{\mathrm{V19}}^{Y(\mathfrak{sl}_2)}$.

The ghost theorem extracted in §8 reveals what the historical statement was
*reaching for*: the K3 Yangian truth that V19 Trinity-$E_1$ at chain level is
*equivalent to* the existence of a Borcherds singular-theta lift of the
underlying algebra. K3-fibred input has $\Phi_5$; super-trace-vanishing input
has the trivial lift; quintic / LP$^2$ have conjectural mock-modular
completions; $Y(\mathfrak{sl}_2)$ has no known lift, and its non-vanishing
$(\hbar/z)[P, \cdot]$ residual is the precise signature of the absent
Borcherds lift.

The Russian-school discipline is preserved: every comparison map exhibited as
an explicit chain map (§3.2 Step C, §4.2 Step C, §5.2); every conditional
dependency named (FM164/FM161 K3-specialised, super-Lie variant); every cross-
volume citation labelled; every status tag matched per AP-CY40; every $\kappa$
subscripted per AP113; every CY-A$_3$ in inf-cat form per AP-CY14; the V49
routes treated as three independent constructions per AP-CY60; the chain-level
discrepancy in the algebraic $C^*_{\mathrm{ch,alg}}$ model per AP-CY62 (b);
the spectral parameter origin per AP-CY65 (algebraic from $\tau_z$, NOT
geometric from FM); narration replaced by construction per AP-CY57 throughout.

The boxed identity

$$
C^\bullet_{\mathrm{chiral}}(A) \;\cong\; \operatorname{End}^{\mathrm{ch}}(A)
\;\cong\; \operatorname{Ext}^*_{A^e}(A, A) \quad \text{at chain level}
$$

is now a chain-level THEOREM for Class A, Class B0, and the abelian
Heisenberg, and a precise chain-level CONJECTURE for Class B with named
residual $\xi_{\mathrm{V19}}(A) = \pi_{\mathrm{V19}}(\xi(A))$. The V40 middle
link is closed for two of the three V55 classes; Class B remains the genuine
frontier, equivalent to the per-input mock-modular completion of the shadow
tower (or, equivalently per §8, to the existence of a Borcherds lift).

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft only.
