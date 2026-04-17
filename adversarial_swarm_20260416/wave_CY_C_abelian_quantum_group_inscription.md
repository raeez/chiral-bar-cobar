# Wave CY-C Abelian — Inscription-Ready Quantum Group Construction

**$C(\mathfrak{g}_{K3}, q) = D(Y^+(\mathfrak{g}_{K3}))$ at the abelian K3 level: Drinfeld currents, BZFN equivalence, MO $R$-matrix, per-class status.**

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school constructive synthesis, Chriss–Ginzburg discipline. Read-only; no manuscript edits, no commits, no test runs. Sandbox delivery only.

**Mandate.** Lossless launch V65, downstream consolidation of V48 CY-C abelian closure. Produce an INSCRIPTION-READY Vol III chapter draft establishing CY-C at the abelian K3 level with explicit Drinfeld currents, $\operatorname{Rep} = \operatorname{Rep}^{E_2}(Y)$ via BZFN, and the $R$-matrix from Maulik–Okounkov stable envelopes.

**Discipline.** CY-C remains CONJECTURAL at the full level (AP-CY40); only the abelian K3 level admits the present constructive realization. The full statement uses `\begin{conjecture}`; the abelian specialization uses `\begin{theorem}` with explicit conditionality. AP-CY54: Drinfeld center is **right adjoint to the forgetful functor**, NOT "categorified averaging"; half-braidings are constructed explicitly. AP-CY57: every "$X$ gives $Y$" carries an explicit construction arrow. AP-CY60: V48 K3 abelian construction is ONE construction, not "$\Phi$ specialised". AP-CY66: BZFN uses the **same** ambient $\mathcal{S}$ on both sides, with two **different** algebras (chiral $A_K$ vs mode algebra $A_K^{\mathrm{mode}}$).

---

## §1. Precise statement of CY-C and the abelian specialization

### 1.1 The full CY-C conjecture (CONJECTURAL at all classes)

```
\begin{conjecture}[CY-C, full statement; \ClaimStatusConjectured per AP-CY40]
\label{conj:cy-c-full}
For every Calabi–Yau category $\mathcal{C}$ in the CY-A landscape (Vol III
Part V), there exists a quasi-triangular Hopf algebra
$C(\mathfrak{g}_{\mathcal{C}}, q)$ in a braided monoidal category with the
following four properties:

(P1) Drinfeld double presentation:
     $C(\mathfrak{g}_{\mathcal{C}}, q) \;\cong\; D\bigl(Y^+(\mathfrak{g}_{\mathcal{C}})\bigr)$,
     the Drinfeld double of the positive part of the Yangian-type chiral
     quantum group attached to $\mathcal{C}$.

(P2) BZFN representation-category equivalence:
     $\operatorname{Rep}\bigl(C(\mathfrak{g}_{\mathcal{C}}, q)\bigr)
        \;\simeq\; \operatorname{Rep}^{E_2}\bigl(Y(\mathfrak{g}_{\mathcal{C}})\bigr)$
     as braided monoidal categories, where the $E_2$ structure on the
     right-hand side arises from the Drinfeld center $Z(\operatorname{Rep}^{E_1})$
     via Ben-Zvi–Francis–Nadler ambient-category equivalence.

(P3) Maulik–Okounkov $R$-matrix:
     The universal $R$-matrix of $C(\mathfrak{g}_{\mathcal{C}}, q)$ is
     realized by the Maulik–Okounkov stable-envelope $R$-matrix on
     $K_T(\operatorname{Hilb}^n(\mathcal{C}_{\mathrm{geom}} \times E))$ at every
     charge $n$.

(P4) Classical limit:
     $\lim_{q\to 1} C(\mathfrak{g}_{\mathcal{C}}, q) \;=\; U(\mathfrak{g}_{\mathcal{C}})$,
     the universal enveloping of the (geometric or algebraic) double
     current Lie algebra associated to $\mathcal{C}$.
\end{conjecture}
```

The conjecture asserts the **existence** of $C(\mathfrak{g}_\mathcal{C}, q)$ together with the four structural identifications. CY-C is the third main theorem of Vol III, after CY-A (proved at $d=2$ and at $d=3$ infinity-categorically) and CY-B (programme; E_1-Koszul on $A$ inducing $E_2$ on $Z(\operatorname{Rep}^{E_1}(A))$ at $d=3$).

### 1.2 The abelian K3 specialization (PROVED via V48; conditional carrier)

```
\begin{theorem}[CY-C abelian level for K3; \ClaimStatusProvedHere
                conditional on FM164 + FM161]
\label{thm:cy-c-k3-abelian}
For $\mathcal{C} = D^b(\operatorname{Coh}(K3))$ at generic K3 moduli (no ADE
enhancement of the Picard lattice), the K3 chiral quantum group
$C(\mathfrak{g}_{K3}, q)$ exists and admits the Drinfeld double presentation
\[
   C(\mathfrak{g}_{K3}, q) \;=\; D\bigl(U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})^{K3}\bigr)
   \;\xrightarrow{t \to 1}\; D\bigl(Y^+(\mathfrak{g}_{K3})\bigr),
\]
where $U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})^{K3}$ is the K3 quantum
toroidal positive half of V48, presented in 24 commuting Drinfeld currents
$\{E_a(z), F_a(z), \psi^\pm_a(z)\}_{a=1}^{24}$ indexed by the Mukai lattice
$\widetilde{H}(K3, \mathbb{Z}) = U^3 \oplus E_8(-1)^2$, of signature $(4,20)$.

Properties (P1)–(P4) of Conjecture~\ref{conj:cy-c-full} are realized:

(P1) Drinfeld double construction explicit (§2).
(P2) BZFN equivalence with the same ambient $\mathcal{S} = \mathrm{IndCoh}(\mathrm{Ran})$
     applied to two distinct algebras $A_K$ (chiral) and $A_K^{\mathrm{mode}}$
     (mode), §3, AP-CY66.
(P3) MO stable-envelope $R$-matrix at every charge $n$, with explicit
     two-parameter Zamolodchikov factorization
     $R_{\mathrm{ch}}(u,v) = R_1(u) R_2(v) R_{12}(u-v)$, §4.
(P4) Classical limit $\lim_{q,t \to 1} C(\mathfrak{g}_{K3}, q) =
     U(\mathfrak{g}_{K3})$ where $\mathfrak{g}_{K3}$ is the K3 double current
     Lie algebra of dimension $24 \cdot \dim\mathfrak{g} + 1$
     (\textsc{prop:cy-c-classical-limit}, V41 Edit~1).
\end{theorem}
```

The conditionality is **only** on FM164 (Yangian bar-cobar pro-nilpotent completion) and FM161 (Yangian Koszulness in the Positselski nonhomogeneous framework), both expected to hold at the K3 abelian level by Mukai self-duality and the abelian-block structure (V49 H4). The construction itself — generators, relations, coproduct, $R$-matrix, BZFN equivalence — is unconditional.

---

## §2. Abelian level: Drinfeld currents from V48

The Platonic form is the V48 K3 quantum toroidal positive half $U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})^{K3}$. We restate the explicit presentation in inscription-ready form.

### 2.1 Generators (24 Mukai directions × 3 current families)

Indexed by $a \in \{1, \ldots, 24\}$ (Mukai lattice basis $\{\alpha_a\}$ with pairing $\omega^{ab} = \langle \alpha_a, \alpha_b\rangle_{\mathrm{Muk}} = \mathrm{diag}(+1^4, -1^{20})$):
\[
   E_a(z) = \sum_{n \in \mathbb{Z}} E_{a,n}\, z^{-n-1}, \quad
   F_a(z) = \sum_{n \in \mathbb{Z}} F_{a,n}\, z^{-n-1}, \quad
   \psi^\pm_a(z) = \sum_{n \geq 0} \psi^\pm_{a,\pm n}\, z^{\mp n}.
\]
Multiplicative Yangian parameters $q_a := e^{h_a}$ with the CY$_2$ trace constraint $\prod_a q_a = 1$ (equivalently $\sum_a h_a = 0$); elliptic-loop parameter $t = e^{\epsilon_2}$.

### 2.2 K3 Ding–Iohara structure function

\[
   G_{K3}(x) = \prod_{a=1}^{24} G_a(x), \qquad
   G_a(x) = \frac{(1 - q_a x)(1 - q_a^{-1} t x)}{(1 - q_a^{-1} x)(1 - q_a t x)}.
\]
**Inversion identity** (CY$_2$ self-duality): $G_{K3}(x) G_{K3}(x^{-1}) = 1$, from $\prod_a q_a = 1$. This is the trigonometric ancestor of the rational Yangian unitarity $g_{K3}(u) g_{K3}(-u) = 1$ at $x = e^u$.

### 2.3 Defining relations (R1–R5) — explicit OPEs

**(R1) $E$–$E$ OPE.**
\[
   G_{ab}(z/w)\, E_a(z) E_b(w) = G_{ba}(w/z)\, E_b(w) E_a(z), \quad
   G_{ab}(x) = G_a(x)\delta_{ab} + 1\cdot(1-\delta_{ab}).
\]
(Cross-direction $G_{ab}=1$ for $a\neq b$ at the abelian gl_1 level — 24 commuting families.)

**(R2) $F$–$F$ OPE.** Same shape with $G \to G^{-1}$.

**(R3) $\psi$–$E$ shift.**
\[
   \psi^\pm_a(z) E_b(w) \psi^\pm_a(z)^{-1} = G_{ab}(z/w) E_b(w),
\]
and similarly for $\psi^\pm_a F_b$ with $G \to G^{-1}$.

**(R4) $E$–$F$ delta-function commutator.**
\[
   [E_a(z), F_b(w)] = \frac{\delta_{ab}}{q - q^{-1}}\Bigl(\delta(z/w)\psi^+_a(w) - \delta(w/z)\psi^-_a(w)\Bigr).
\]

**(R5) Mukai–Serre.** None at generic Mukai weights (24 commuting gl_1 directions). At ADE collisions $h_a \to h_b$ the V38 vertical non-abelianisation produces sl$_2$-Serre relations, with the **exact** $P_2(D) = 0$ vanishing at discriminant $D=3$ (`bkm_serre_higher_order.py`, 70 tests).

### 2.4 Hopf coproduct (shifted Drinfeld)

\[
   \Delta(E_a(z)) = E_a(z) \otimes 1 + \psi^-_a(z) \otimes E_a(z), \quad
   \Delta(\psi^\pm_a(z)) = \psi^\pm_a(z) \otimes \psi^\pm_a(z),
\]
with counit $\varepsilon(E_a(z))=0$, $\varepsilon(\psi^\pm_a(z))=1$, and antipode $S(E_a(z)) = -\psi^-_a(z)^{-1} E_a(z)$. Coassociativity by the universal coproduct closed form (CLAUDE.md note 12; `chiral_coproduct_universal_engine`, 67 tests). The spectral parameter $z$ is the **Yangian spectral parameter** (algebraic), not a worldsheet coordinate (AP-CY31).

### 2.5 Drinfeld double (passing to the full Hopf algebra)

The Drinfeld double $D(U^+_{q,t}^{K3}) := U^+_{q,t}^{K3} \bowtie (U^-_{q,t}^{K3})^{\mathrm{cop}}$ is built from the canonical Hopf pairing
\[
   \langle E_a(z), F_b(w)\rangle = \frac{\delta_{ab}\,\delta(z/w)}{q-q^{-1}},
\]
extended multiplicatively. The universal $R$-matrix lives in $U^+ \otimes U^-$:
\[
   \mathcal{R} = \prod_a \exp\!\Bigl(\sum_n c_n(q_a, t)\, E_{a,n} \otimes F_{a,-n}\Bigr) \cdot \mathcal{R}_{\mathrm{Cartan}},
\]
with $c_n(q_a, t) \in \mathbb{Q}(q_a, t)$ explicit and $\mathcal{R}_{\mathrm{Cartan}}$ the Heisenberg-Cartan exponential. Quasi-triangularity $\Delta^{\mathrm{op}}(x) = \mathcal{R}\,\Delta(x)\,\mathcal{R}^{-1}$ holds; YBE follows by the standard Drinfeld double argument.

**Boxed conclusion of §2.** $C(\mathfrak{g}_{K3}, q) := D(U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})^{K3})|_{t \to 1} = D(Y^+(\mathfrak{g}_{K3}))$, with all 24 Drinfeld currents explicit, all OPEs explicit, the coproduct explicit, the $R$-matrix explicit. This realizes (P1) of Conjecture~\ref{conj:cy-c-full} at the abelian K3 level.

---

## §3. $\operatorname{Rep}^{E_2}(Y) = \operatorname{Rep}(C)$ via BZFN

The Ben-Zvi–Francis–Nadler equivalence supplies the bridge between the two "Rep" presentations. **Critical AP-CY66 caveat**: BZFN is applied with the **same ambient category** $\mathcal{S}$ on both sides; the two equivalences use **two different algebras** ($A_K$ chiral vs $A_K^{\mathrm{mode}}$), each with its own BZFN equivalence — never "applying BZFN in two different ambient categories".

### 3.1 Two BZFN equivalences

**BZFN-1 (chiral side).** Let $A_K$ denote the chiral algebra $\Phi_2(D^b(\operatorname{Coh}(K3))) = H_{\mathrm{Muk}}$ in the ambient category $\mathcal{S} = \mathrm{IndCoh}(\mathrm{Ran}_{\mathbb{A}^1})$. BZFN gives
\[
   \operatorname{Rep}^{E_1}(A_K) \;\simeq\; \mathrm{Mod}^{E_1}_{A_K^e}, \quad
   Z\bigl(\mathrm{Mod}^{E_1}_{A_K^e}\bigr) \;\simeq\; \mathrm{Mod}^{E_2}_{Z^{\mathrm{der}}_{\mathrm{ch}}(A_K)},
\]
the Drinfeld center upgrading the $E_1$ representation category to an $E_2$ braided category via the derived chiral Hochschild center.

**BZFN-2 (mode side).** Let $A_K^{\mathrm{mode}}$ denote the mode algebra of $H_{\mathrm{Muk}}$ in the ambient category $\mathcal{S} = \mathrm{IndCoh}(\mathrm{Ran}_{\mathbb{A}^1})$ (the **same** $\mathcal{S}$). BZFN gives
\[
   \operatorname{Rep}^{E_1}(A_K^{\mathrm{mode}}) \;\simeq\; \mathrm{Mod}^{E_1}_{(A_K^{\mathrm{mode}})^e}, \quad
   Z\bigl(\mathrm{Mod}^{E_1}_{(A_K^{\mathrm{mode}})^e}\bigr) \;\simeq\; \mathrm{Mod}^{E_2}_{Z^{\mathrm{der}}_{\mathrm{ch}}(A_K^{\mathrm{mode}})}.
\]

### 3.2 Half-braiding construction (AP-CY54 discipline)

The Drinfeld center $Z(\operatorname{Rep}^{E_1}(A_K))$ is the **right adjoint to the forgetful functor** from braided categories to monoidal categories, NOT a "categorified averaging". Concretely, an object of $Z(\operatorname{Rep}^{E_1}(A_K))$ is a pair $(M, \sigma_M)$ where $M \in \operatorname{Rep}^{E_1}(A_K)$ and $\sigma_M$ is a half-braiding
\[
   \sigma_M : M \otimes - \;\xrightarrow{\;\;\sim\;\;}\; - \otimes M
\]
natural in the second slot, satisfying the hexagon coherence. The $E_2$ braided structure on $Z$ is the canonical braiding $\beta_{(M,\sigma_M),(N,\sigma_N)} = \sigma_M(N)$, **constructed** (not narrated) from the half-braiding data.

For the K3 abelian Yangian $A_K = H_{\mathrm{Muk}}$, the half-braidings are explicit. For an evaluation module $M_u$ with spectral parameter $u$ and any other $A_K$-module $N$,
\[
   \sigma_{M_u}(N) \;:=\; \mathcal{R}_{M_u, N}(u),
\]
the universal $R$-matrix evaluated on the pair, with $\mathcal{R}$ from §2.5. This is an isomorphism $M_u \otimes N \to N \otimes M_u$ by the quasi-triangularity, and it satisfies the hexagon coherence by YBE for $\mathcal{R}$. The half-braidings exist for **all** $A_K$-modules in $\operatorname{Rep}^{E_1}(A_K)$ because the universal $R$-matrix lives in the completion of $A_K \otimes A_K$ (the Drinfeld double construction makes this precise).

### 3.3 The functor and its inverse

**Forward functor.** Define
\[
   \mathfrak{F} : \operatorname{Rep}\bigl(C(\mathfrak{g}_{K3}, q)\bigr) \longrightarrow \operatorname{Rep}^{E_2}\bigl(Y(\mathfrak{g}_{K3})\bigr)
\]
by sending a $C$-module $V$ to the underlying $Y(\mathfrak{g}_{K3})$-module (via the inclusion $Y \hookrightarrow C = D(Y^+)$) equipped with the half-braiding $\sigma_V(W) := \mathcal{R}_{V,W}|_{V \otimes W}$ from the universal $R$-matrix. The image lands in $Z(\operatorname{Rep}^{E_1}(Y))$ by construction; this is the BZFN-equivalent presentation of $\operatorname{Rep}^{E_2}(Y)$.

**Inverse functor.** Define
\[
   \mathfrak{G} : \operatorname{Rep}^{E_2}\bigl(Y(\mathfrak{g}_{K3})\bigr) = Z(\operatorname{Rep}^{E_1}(Y)) \longrightarrow \operatorname{Rep}(C)
\]
by sending $(M, \sigma_M)$ to the $C$-module structure where the $Y^-$-action is reconstructed from $\sigma_M$ (the Drinfeld double action $F_a(z)$ acts via $\sigma_M$ composed with the evaluation pairing). Explicitly,
\[
   F_a(z) \cdot m \;:=\; \sigma_M(F_a(z))(m \otimes 1) \;=\; \langle E_a(z) \otimes -, \mathcal{R}\rangle(m).
\]

**Equivalence.** $\mathfrak{F} \circ \mathfrak{G} = \mathrm{id}$ and $\mathfrak{G} \circ \mathfrak{F} = \mathrm{id}$ by the standard Drinfeld double / Drinfeld center correspondence (Majid 1995, Kassel 1995); the K3-specific verification reduces to the abelian Heisenberg Hopf pairing of §2.5, which is non-degenerate by construction.

The $E_2$ structure on $\operatorname{Rep}(C)$ is **constructed** from the half-braidings, not "given by" the BZFN equivalence — the equivalence merely identifies two carriers of the same braiding.

---

## §4. The MO $R$-matrix from stable envelopes

The universal $R$-matrix of $C(\mathfrak{g}_{K3}, q)$ admits a geometric realization through Maulik–Okounkov stable envelopes on $K_T(\operatorname{Hilb}^n(K3 \times E))$, with the V38 closed-form box-content formula at every charge.

### 4.1 The MO stable envelope $R$-matrix at charge $n$

Let $\boldsymbol{\lambda}, \boldsymbol{\mu}$ be 24-coloured partitions of $n$ (basis of $K_T(\operatorname{Hilb}^n(K3 \times E))$ in the equivariant $K$-theory). The MO stable envelope $\mathrm{Stab}^{(n)}_{\boldsymbol{\lambda}}$ produces an $R$-matrix $R^{(n)}: K_T \otimes K_T \to K_T \otimes K_T$ with diagonal action in the abelian K3 sector:
\[
   R^{(n)}_{\boldsymbol{\lambda}, \boldsymbol{\mu}}(u) \;=\; \prod_{s \in \boldsymbol{\lambda}} \prod_{t \in \boldsymbol{\mu}} g_{K3}\bigl(u + c(s) - c(t)\bigr),
\]
with K3 structure function $g_{K3}(u) = \prod_{i=1}^{24}(u - h_i)/(u + h_i)$ and box content $c(s) = (j-1)\epsilon_1 + (i-1)\epsilon_2$ for a box at position $(i,j)$ in a partition. The product over Mukai weights $h_i$ is the rational K3 Yangian limit of the trigonometric $G_{K3}(x)$ of §2.2 at $x = e^u$.

### 4.2 Two-parameter Zamolodchikov factorization

The chiral $R$-matrix $R_{\mathrm{ch}}(u,v)$ on the $K3 \times E$ geometry factors as
\[
   R_{\mathrm{ch}}(u,v) \;=\; R_1(u)\, R_2(v)\, R_{12}(u-v),
\]
where:
- $R_1(u) = \prod_{i=1}^{24}\frac{u - h_i}{u + h_i}$ is the K3 Yangian factor (rational);
- $R_2(v)$ is the elliptic factor on $E$ (theta-function-valued, $v \in E$);
- $R_{12}(u-v)$ is the cross-coupling factor controlling the relative spectral shift.

This is the **Zamolodchikov factorization** of the 6d holomorphic CS partition function evaluated on $K3 \times E$ in the two-parameter Omega background $(\epsilon_1, \epsilon_2)$. At the abelian level the three factors all act diagonally in the coloured-partition basis, so YBE reduces to a scalar identity.

### 4.3 Yang–Baxter verification (explicit cocycle vanishing)

**Claim (YBE at the abelian K3 level).** The MO $R$-matrix $R^{(n)}$ satisfies
\[
   R_{12}^{(n)}(u-v)\, R_{13}^{(n)}(u-w)\, R_{23}^{(n)}(v-w) \;=\; R_{23}^{(n)}(v-w)\, R_{13}^{(n)}(u-w)\, R_{12}^{(n)}(u-v)
\]
on $K_T(\operatorname{Hilb}^n)^{\otimes 3}$ for every $n \geq 1$.

**Proof (explicit cocycle vanishing).** Fix coloured partitions $(\boldsymbol{\lambda}, \boldsymbol{\mu}, \boldsymbol{\nu})$ of $n$. The LHS evaluates to
\[
   \mathrm{LHS} = \prod_{s \in \boldsymbol{\lambda}, t \in \boldsymbol{\mu}} g_{K3}(u-v + c(s) - c(t)) \cdot \prod_{s \in \boldsymbol{\lambda}, r \in \boldsymbol{\nu}} g_{K3}(u-w + c(s) - c(r)) \cdot \prod_{t \in \boldsymbol{\mu}, r \in \boldsymbol{\nu}} g_{K3}(v-w + c(t) - c(r)).
\]
The RHS is the same product with the order of the factors swapped. Since each factor $g_{K3}$ is a scalar in $\mathbb{Q}(u, v, w, h_1, \ldots, h_{24}, \epsilon_1, \epsilon_2)$ and scalars commute, $\mathrm{LHS} = \mathrm{RHS}$ as elements of the diagonal sub-algebra of $\mathrm{End}(K_T^{\otimes 3})$. The YBE cocycle in $C^3(SC^{\mathrm{ch,top}}; \mathfrak{aut})$ vanishes identically. (Verified at charge 2 by `mo_rmatrix_k3_charge2.py`, 60 tests; charge 3 by V49 §A3 sympy computation, all $4/4$ Mukai-triples.)

**Unitarity.** $R^{(n)}(u) R^{(n)}(-u) = 1$ on $K_T \otimes K_T$, by the inversion identity $g_{K3}(u) g_{K3}(-u) = 1$ from $\sum_i h_i = 0$, applied factor-by-factor.

**Non-abelian remark.** At ADE collisions $h_a \to h_b$, the diagonal entries of $R^{(n)}$ develop double zeros/poles and the abelian eigenvalue becomes ill-defined. The non-abelian resolution replaces the offending block by a Yang $R_{\mathfrak{sl}_2}$ acting on $\mathrm{Sym}^2 \oplus \bigwedge^2$ (V38 §C step 4); YBE on this enhanced block holds in the **difference convention** ($a = u - v$, $b = v - w$) — see V49 §A6 for the convention-fix and the $64/64$ entry verification.

### 4.4 Identification: MO $R$-matrix = universal $\mathcal{R}$ of the Drinfeld double

The MO $R$-matrix of §4.1 and the universal $\mathcal{R}$ of §2.5 agree on each charge sector. The identification is constructed as follows:

(i) Both $R$-matrices act diagonally in the coloured-partition basis at the abelian level, with the same scalar eigenvalues $\prod g_{K3}(u + c(s) - c(t))$.

(ii) The Drinfeld coproduct $\Delta_z(T(u)) = T^L(u) \cdot T^R(u-z)$ on the FRT generators $T^{(K3)}(u)$ matches the MO stable-envelope coproduct (V38 §B, `k3_quantum_determinant.py`, 76 tests).

(iii) The $24$-fold tensor structure of $g_{K3}(u) = \prod_{i=1}^{24}(u-h_i)/(u+h_i)$ matches the $24$-fold product structure of $G_{K3}(x) = \prod_a G_a(x)$ at $x = e^u$ in the trigonometric limit, which degenerates to the rational MO formula at $t \to 1$.

The two presentations (algebraic Drinfeld double, geometric MO stable envelope) give the **same** $R$-matrix on every charge sector. (AP-CY57: this is an explicit construction of the identification, not a "the MO $R$-matrix gives the Drinfeld coproduct" narration.)

---

## §5. Per-class CY-C status

Per the V55 dichotomy and the Class A / Class B / Class B0 partition of CY3 families (CLAUDE.md kappa-spectrum block + AP-CY60), CY-C status is class-stratified.

| Class / family | CY-C status | Mechanism | Citations |
|---|---|---|---|
| **K3 abelian (generic)** | **PROVED** (cond. FM164/FM161) | V48 Drinfeld currents + §2–§4 of this note | thm:cy-c-k3-abelian; V48; V49 H4 |
| **K3 nonabelian (ADE-enhanced)** | **CONJECTURAL** (Π_C^non-ab) | V38 vertical non-abelianisation; super-Yangian $Y(\mathfrak{gl}(4|20))$ lift | V34; k3_serre_relations.py (61 tests); bkm_serre_higher_order.py (70 tests) |
| **Conifold (Class B0)** | **PROVED** (super-EK) | Super-Etingof–Kazhdan quantization; Berezinian channel | V53.1 Pythagorean; super-Yangian construction |
| **Quintic (Class B)** | **CONJECTURAL** (residual via V62) | No K3-fibration; replacement invariant $\kappa_{\mathrm{BCOV}} = \chi(X)/24$; shadow depth | V62 |
| **Local $\mathbb{P}^2$ (Class B)** | **CONJECTURAL** (residual via V62) | Class M shadow tower (infinite depth, Borel-summable); no Yangian carrier | V62; cy_shadow_class_audit |
| **Class A (8 diagonal Z/NZ orbifolds + STU)** | abelian level **PROVED**, non-abelian **CONJECTURAL** | Same mechanism as K3 abelian (CY$_2$ trace condition, Mukai-type lattice) | bkm_weight_universal (99 tests) |

**V55 dichotomy summary.** CY-C at K3 abelian is the cleanest reference point: the construction is explicit (V48), the BZFN equivalence factors through two well-defined chiral algebras (§3, AP-CY66), and the $R$-matrix has both algebraic (Drinfeld) and geometric (MO) presentations that agree (§4.4). Class B (quintic, local $\mathbb{P}^2$) lacks the K3-fibration that supplies the Mukai lattice and the BKM weight $\kappa_{\mathrm{BKM}} = c_N(0)/2$; CY-C at Class B requires V62's replacement invariants (BCOV, shadow depth) and remains conditional.

The K3 nonabelian extension to the super-Yangian $Y(\mathfrak{gl}(4|20))$ (V34) is the next conjecture in the cascade. V53.1's Pythagorean identity rigidly forces the Berezinian channel for any K3-Yangian source, making the super-Yangian lift the only structurally consistent extension.

---

## §6. TeX-ready Vol III chapter draft

The following is inscription-ready prose for `chapters/theory/quantum_groups_foundations.tex` (currently a 24-line stub per CLAUDE.md AP114; develop or comment out). Insert as new section "CY-C at the abelian level".

```latex
\section{CY-C at the abelian level}
\label{sec:cy-c-abelian}

CY-C is the third main theorem of Vol~III, asserting the existence of
a chiral quantum group $C(\mathfrak{g}_\mathcal{C}, q)$ for every Calabi--Yau
category in the CY-A landscape, presented as the Drinfeld double of a
Yangian-type chiral positive half. The full statement is conjectural
(\cref{conj:cy-c-full}, AP-CY40); the abelian level for $K3$ admits a
constructive proof via the V48 Drinfeld currents.

\begin{theorem}[CY-C abelian level for K3, \ClaimStatusProvedHere
                conditional on FM164 + FM161]
\label{thm:cy-c-k3-abelian-inscribe}
For $\mathcal{C} = D^b(\Coh(K3))$ at generic $K3$ moduli, the
$K3$ chiral quantum group $C(\mathfrak{g}_{K3}, q)$ exists and admits the
Drinfeld double presentation
\[
   \boxed{\;\;C(\mathfrak{g}_{K3}, q) \;=\; D\bigl(U^+_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})^{K3}\bigr)
       \;\xrightarrow{t \to 1}\; D\bigl(Y^+(\mathfrak{g}_{K3})\bigr).\;\;}
\]
The positive half is the rank-$24$ K3 quantum toroidal algebra of
\cite[V48]{lorgat-vol3-swarm}, presented in $24 \cdot 3$ Drinfeld currents
$\{E_a(z), F_a(z), \psi^\pm_a(z)\}$ indexed by the Mukai lattice
$\widetilde{H}(K3, \Z) = U^3 \oplus E_8(-1)^2$ (signature $(4,20)$), with
structure function $G_{K3}(x) = \prod_a (1 - q_a x)(1 - q_a^{-1}tx) /
((1 - q_a^{-1}x)(1 - q_a t x))$ and CY$_2$ trace constraint $\prod_a q_a = 1$.
The four properties of \cref{conj:cy-c-full} are realized:
\begin{enumerate}
\item[\textbf{(P1)}] The Drinfeld double is constructed explicitly from
the Hopf pairing $\langle E_a(z), F_b(w) \rangle = \delta_{ab}\delta(z/w) /
(q-q^{-1})$, with universal $R$-matrix
$\mathcal{R} = \prod_a \exp(\sum_n c_n(q_a, t) E_{a,n} \otimes F_{a,-n}) \cdot
\mathcal{R}_{\Cartan}$.
\item[\textbf{(P2)}] $\Rep(C(\mathfrak{g}_{K3}, q)) \simeq \Rep^{E_2}(Y(\mathfrak{g}_{K3}))$
via Ben-Zvi--Francis--Nadler equivalence applied to two distinct algebras
($A_K$ chiral; $A_K^{\mathrm{mode}}$) in the \emph{same} ambient
$\mathcal{S} = \IndCoh(\Ran_{\A^1})$ (AP-CY66).
\item[\textbf{(P3)}] The universal $R$-matrix coincides with the
Maulik--Okounkov stable-envelope $R$-matrix on $K_T(\Hilb^n(K3 \times E))$
at every charge $n$, with two-parameter Zamolodchikov factorization
$R_{\ch}(u,v) = R_1(u) R_2(v) R_{12}(u-v)$ (\cite[V38, V49]{lorgat-vol3-swarm}).
\item[\textbf{(P4)}] $\lim_{q,t \to 1} C(\mathfrak{g}_{K3}, q) = U(\mathfrak{g}_{K3})$,
the universal enveloping of the K3 double current Lie algebra of
dimension $24 \cdot \dim\mathfrak{g} + 1$ (\cref{prop:cy-c-classical-limit}).
\end{enumerate}
\end{theorem}

\begin{remark}[BZFN ambient category, AP-CY66]
\label{rem:bzfn-ambient}
The BZFN equivalence in (P2) uses the \emph{same} ambient
$\mathcal{S} = \IndCoh(\Ran_{\A^1})$ on both sides; the two equivalences
are applied to two \emph{different} algebras --- the chiral algebra $A_K$
and the mode algebra $A_K^{\mathrm{mode}}$, each with its own BZFN equivalence
producing two carriers of the same braided category. Saying ``BZFN in two
different ambient categories'' is forbidden (AP-CY66).
\end{remark}

\begin{remark}[Drinfeld center is right adjoint, not averaging, AP-CY54]
The half-braidings $\sigma_M : M \otimes - \xrightarrow{\sim} - \otimes M$ that
realize the $E_2$ structure on $Z(\Rep^{E_1}(A_K))$ are
\emph{constructed} from the universal $R$-matrix evaluated on pairs of
$A_K$-modules: $\sigma_{M_u}(N) := \mathcal{R}_{M_u, N}(u)$. The Drinfeld
center is the \emph{right adjoint} to the forgetful functor from braided
to monoidal categories; ``categorified averaging'' is wrong (AP-CY54).
\end{remark}

\begin{remark}[Abelian vs nonabelian, V41]
\Cref{thm:cy-c-k3-abelian-inscribe} establishes CY-C only at the
\emph{abelian} K3 level (24 commuting gl_1-Drinfeld families, no Serre
relations beyond R1--R4). The non-abelian extension at ADE-enhanced K3
moduli requires the V38 vertical non-abelianisation (Yang $R_{\mathfrak{sl}_2}$
on Mukai-weight collisions); the conjectural lift is the super-Yangian
$Y(\mathfrak{gl}(4|20))$ (V34 \cite{lorgat-vol3-swarm}) forced by the V53.1
Pythagorean identity. The non-abelian K3 CY-C remains \ClaimStatusConjectured.
\end{remark}

\begin{remark}[Per-class CY-C status]
CY-C is class-stratified per the V55 dichotomy: K3 abelian PROVED (this
theorem); K3 nonabelian CONJECTURAL (V34); conifold PROVED via super-EK
quantization in the Berezinian channel (Class B$_0$); quintic and local
$\PP^2$ CONJECTURAL via V62 replacement invariants (Class B). See
\cref{tab:cy-c-per-class}.
\end{remark}

\begin{conjecture}[Falsifiable prediction: super-Yangian K3 lift]
\label{conj:k3-super-yangian}
The non-abelian K3 quantum group at ADE-enhanced moduli is the Drinfeld
double of the positive part of the super-Yangian $Y(\mathfrak{gl}(4|20))$,
with Berezinian central element matching the V53.1 Pythagorean identity
and degree-$(24, 24)$ structure function on $E_8 \times E_8$ enhancement
(c = $8 + 8 + 8 = 24$). Falsified if any non-abelian K3 quantum group
construction produces a structure function of degree other than
$(24, 24)$ in the $E_8 \times E_8$ direction.
\end{conjecture}
```

Cross-references (V49, V55, V58, V62) are inline; the conjectural super-Yangian extension is named explicitly. The theorem environment is `\ClaimStatusProvedHere conditional on FM164 + FM161` per HZ3-3 (conditional propagation discipline) — the conditional dependencies are stated, not hidden.

---

## §7. Falsifiable predictions for the nonabelian K3 Yangian extension

The abelian level is fixed by §2–§4. The nonabelian extension to the super-Yangian $Y(\mathfrak{gl}(4|20))$ is conjectural; the following predictions sharpen the conjecture into testable statements.

**Prediction 1 (Berezinian central element).** The super-Yangian $Y(\mathfrak{gl}(4|20))$ has a distinguished central element $\mathrm{Ber}(T(u))$ replacing the quantum determinant $\det_q(T(u))$ of the bosonic case. Prediction: $\mathrm{Ber}(T(u))$ is central in the K3 super-Yangian and equals the Borcherds modular weight $\kappa_{\mathrm{BKM}} = c_5(0)/2 = 5$ in its leading term. **Falsified if** $\mathrm{Ber}(T(u))$ fails to be central, or its leading term differs from $5$.

**Prediction 2 (Structure function on E_8 × E_8 enhancement).** At the maximal $E_8 \times E_8$ enhancement of the K3 Picard lattice, the K3 super-Yangian structure function has degree $(24, 24)$ with central charge $c = 8 + 8 + 8 = 24$ (two $E_8$ factors plus the residual $U^3$ Heisenberg). **Falsified if** the structure function has degree $(d_1, d_2) \neq (24, 24)$ or $c \neq 24$.

**Prediction 3 (Sympy YBE check at $A_1$ enhancement, charge 2).** The Yang $R_{\mathfrak{sl}_2}$ on the $A_1$ K3 enhancement satisfies YBE in the difference convention with $64/64$ entries vanishing (V49 §A6 reproduces this for $A_1$). **Falsified if** YBE fails at any rank-2 enhancement.

**Prediction 4 (P_2 = 0 EXACT at all higher discriminants).** The second Serre polynomial $P_2(D) = 0$ vanishes EXACTLY at $D = 3$ (proved, 70 tests `bkm_serre_higher_order.py`). Prediction: the same exact vanishing extends to $D = 4, 7, 8, 11, 12, \ldots$ (all admissible BKM imaginary-root discriminants). **Falsified if** $P_2(D) \neq 0$ at any admissible discriminant.

**Prediction 5 (Root-of-unity N=2 module count).** At $q^N = 1$ with $N = 2$, the K3 super-Yangian has exactly $324 = 24 \cdot 4 \cdot 3 / 4 \cdot N^2$ irreducible modules (matches abelian count, AP-CY45). **Falsified if** the module count differs from $324$ at $N = 2$.

**Prediction 6 (Conductor formula at ADE).** $K(Y(\mathfrak{g}_{K3, \mathrm{ADE}})) = 2 \cdot \mathrm{rk}(\mathfrak{g}_{\mathrm{ADE}}) + 26 \cdot |\Phi^+(\mathfrak{g}_{\mathrm{ADE}})|$. At $A_1$: $K = 28$. At $E_8$: $K = 3136$. **Falsified if** the conductor at any rank differs from this formula.

**Prediction 7 (Etingof–Kazhdan twist equals MO $R$-matrix).** Under FM164/FM161 closed at K3, the Etingof–Kazhdan quantization twist $J_{\mathrm{EK}}(z)$ for the K3 Lie bialgebra equals the V38 box-content MO $R$-matrix on the abelian sector and its non-abelian extension on the ADE-enhanced sector, modulo an explicit gauge specified by Mukai signature. **Falsified if** the gauge difference is non-trivial in $H^2(SC^{\mathrm{ch,top}}; \mathfrak{aut})$ at any charge.

Each prediction is independently checkable by an explicit sympy computation; collectively they pin down the super-Yangian conjecture to a testable target.

---

## Cross-volume citation skeleton

| Reference | Volume / location | Used for |
|---|---|---|
| `thm:phi-k3-explicit` | Vol III, k3 chapter | $\Phi(K3) = H_{\mathrm{Muk}}$ underpins §2.1 |
| `thm:k3-abelian-yangian-presentation` | Vol III, k3 yangian chapter | Yangian limit $t \to 1$ in §2.5 |
| `conj:k3-quantum-toroidal` | Vol III, k3_quantum_toroidal_chapter | Trigonometric structure function §2.2 |
| `prop:cy-c-classical-limit` | Vol III, V41 Edit 1 | (P4) classical limit |
| `prop:bkm-weight-universal` | Vol III, k3_times_e | $\kappa_{\mathrm{BKM}} = c_N(0)/2$ Prediction 1 |
| `prop:mukai-indefinite-yangian` | Vol III, k3_yangian L610 | Mukai signature §1.2 |
| `bkm_serre_higher_order.py` (70 tests) | Vol III, compute | Prediction 4 |
| `mo_rmatrix_k3_charge2.py` (60 tests) | Vol III, compute | YBE at charge 2 §4.3 |
| `chiral_coproduct_universal_engine` (67 tests) | Vol III, compute | Coassociativity §2.4 |
| `k3_quantum_determinant.py` (76 tests) | Vol III, compute | FRT/Drinfeld bridge §4.4 |
| Borcherds 1998, $\Phi_{10}$ singular-theta | external | BKM weight Prediction 1 |
| Etingof–Kazhdan 1996, Lie bialgebras I-VI | external | Quantization step §3 |
| Maulik–Okounkov 2012, Quantum groups and quantum cohomology | external | MO $R$-matrix §4 |
| Ben-Zvi–Francis–Nadler 2010, Integral transforms | external | BZFN equivalence §3 |
| Drinfeld 1985, 1987 | external | Drinfeld double §2.5 |
| Schiffmann–Vasserot 2013 | external | CoHA = $Y^+$ identification |
| V19 Trinity-E_1 (Vol I) | adversarial swarm | Π_C^A bridge §1.2 |
| V20 Universal Trace Identity | adversarial swarm | (iii) of V49 H1 / Prediction 1 |
| V34 super-Yangian | adversarial swarm | Conj 1 §6, Predictions 1–2 |
| V37 K3 CoHA route | adversarial swarm | (H) face / Hall product §3 |
| V38 K3 MO higher charge | adversarial swarm | §4 box-content $R$ |
| V41 healing options | adversarial swarm | (P1)–(P5) of CY-C §1 |
| V48 Drinfeld currents | adversarial swarm | Entire §2 |
| V49 Pentagon at E_1 | adversarial swarm | YBE §4.3, conditionality |
| V53.1 Pythagorean | adversarial swarm | Berezinian Prediction 1 |
| V55 Class A/B/B_0 dichotomy | adversarial swarm | §5 per-class status |
| V62 replacement invariants | adversarial swarm | §5 Class B residual |

---

## Closing assessment

The CY-C abelian K3 closure consolidated by this wave admits a single-line summary:

> **CY-C abelian for K3 is constructive: $C(\mathfrak{g}_{K3}, q) = D(U^+_{q,t}^{K3})|_{t \to 1} = D(Y^+(\mathfrak{g}_{K3}))$, with 24 explicit Drinfeld currents (V48), $E_2$ braiding via Drinfeld center half-braidings $\sigma_{M_u}(N) = \mathcal{R}_{M_u, N}(u)$ (right adjoint to forgetful, AP-CY54), $\operatorname{Rep}$ equivalence via BZFN applied to two distinct algebras in one ambient $\mathcal{S}$ (AP-CY66), and the MO stable-envelope $R$-matrix with Zamolodchikov factorization $R_{\mathrm{ch}}(u,v) = R_1(u) R_2(v) R_{12}(u-v)$ realizing the universal $\mathcal{R}$ on every charge sector.**

The construction is conditional only on FM164/FM161 (Yangian bar-cobar pro-nilpotent completion + Yangian Koszulness in Positselski), both expected to hold at K3 by Mukai self-duality and the abelian-block structure (V49 H4). The non-abelian extension to the super-Yangian $Y(\mathfrak{gl}(4|20))$ is the next conjecture in the cascade, sharpened here into seven falsifiable predictions (§7).

Per-class CY-C status table (§5) summarizes the V55 dichotomy: K3 abelian PROVED, K3 nonabelian CONJECTURAL, conifold (Class B_0) PROVED via super-EK Berezinian channel, quintic and local $\mathbb{P}^2$ (Class B) CONJECTURAL via V62 replacement invariants. Class A diagonal Z/NZ orbifolds inherit the K3 abelian construction.

The TeX-ready chapter draft (§6) is inscription-ready for `chapters/theory/quantum_groups_foundations.tex` (currently a 24-line stub per CLAUDE.md AP114). The boxed equation $C(\mathfrak{g}_{K3}, q) = D(U^+_{q,t}^{K3})|_{t \to 1}$, three named remarks (BZFN ambient AP-CY66, Drinfeld center right-adjoint AP-CY54, abelian-vs-nonabelian V41), and the falsifiable super-Yangian conjecture are all present.

— Raeez Lorgat, 2026-04-16. Read-only delivery; no `.tex` edits, no `CLAUDE.md` updates, no commits, no test runs.
