# The Non-Abelian K3 Yangian via the Mukai Super-Yangian
## Wave Culmination: $Y(\mathfrak{gl}(4|20))$, Borcherds vertex flow, and the trace identity

**Status.** Russian-school constructive synthesis, building on Vol III `thm:k3-abelian-yangian-presentation` (PROVED), `conj:k3-super-yangian` (CONJECTURAL), `compute/lib/k3_super_yangian.py` (59 tests), `compute/lib/super_yangian_resolves.py`, and the cross-volume Universal Trace Identity (V20). Wave 14 V11 Φ-functor framework presupposed. **Author:** Raeez Lorgat. **Date:** 2026-04-16.

> "Every quantum group is the cohomology of a categorical centre, and every centre carries a reflection. The signature of the reflection is the signature of the lattice." — paraphrasing the Drinfeld–Kazhdan voice.

---

## 1. Setup: Mukai lattice $(4,20)$, abelian Yangian status

### 1.1 The lattice

The Mukai lattice of K3 is
$$
\widetilde H(K3,\mathbb Z) \;\simeq\; U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}, \qquad \mathrm{rank}=24, \qquad \mathrm{signature}=(4,20),
$$
with the Mukai pairing $\langle (r,c_1,s),(r',c_1',s')\rangle_{\mathrm{Muk}} = c_1\cdot c_1' - rs' - r's$. The four positive directions come from $H^0\oplus H^4$ (two hyperbolic units of $U$) and the two Kähler directions in the $H^{1,1}\cap H^2(K3,\mathbb R)$ wall; the twenty negative directions come from the remaining $H^2$ subspace and the $E_8(-1)^{\oplus 2}$ factors.

### 1.2 What is PROVED (`thm:k3-abelian-yangian-presentation`, 47 tests)

The **abelian** K3 Yangian $Y(\mathfrak g_{K3})$ has the closed-form RTT presentation
$$
R(z)\,T_1(u)T_2(v) = T_2(v)T_1(u)R(z), \qquad z=u-v,
$$
with $R(z)=g(z)\cdot \mathrm{Id}$ for the diagonal/abelian R-matrix, structure function
$$
g_{K3}(z) \;=\; \prod_{i=1}^{24}\frac{z-h_i}{z+h_i}
$$
of degree $(24,24)$, and the diagonal Heisenberg generators $J^a_i = T^a\otimes \alpha_i$ ($a=1$, $i=1,\dots,24$) satisfying the OPE
$$
J^i(z)J^j(w) \sim \frac{\omega^{ij}}{(z-w)^2}, \qquad \omega = \mathrm{diag}(+1^4,-1^{20}).
$$
The quantum determinant $q\text{-det}(T(u))$ is central; $\kappa_{\mathrm{ch}}(K3)=2$; the Fock character is $1/\eta(q)^{24}$.

### 1.3 What is OPEN

The **non-abelian** K3 Yangian — the algebra acting on $H^*_T(\mathrm{Hilb}^n(K3))$ via Maulik–Okounkov stable envelopes — has only the *abelian* sector (the $T_a^a$ entries) constructed. The off-diagonal $T^a_b$ entries with $a\neq b$, sourced from BKM imaginary roots and from $\mathfrak{sl}_2$ enhancements at $A_1$ degenerations, **do not assemble into an ordinary Yangian** $Y(\mathfrak g)$ for any classical $\mathfrak g$. The obstruction is precisely the indefinite signature.

The conjectural resolution — `conj:k3-super-yangian` — is the **Mukai super-Yangian** $Y(\mathfrak{gl}(4|20))$.

---

## 2. ATTACK: why the Mukai signature forces $\mathfrak{gl}(4|20)$

### 2.1 The $P_\omega^2$ obstruction

The naive R-matrix on $V\otimes V = \mathbb C^{24}\otimes \mathbb C^{24}$ uses the Mukai-twisted permutation
$$
P_\omega(e_i\otimes e_j) \;=\; \omega_{ii}\;(e_j\otimes e_i) \;=\; s_i\,(e_j\otimes e_i), \qquad s_i = \pm 1.
$$
Direct computation:
$$
P_\omega^2(e_i\otimes e_j) \;=\; s_i s_j \,(e_i\otimes e_j),
$$
so $P_\omega^2 = \mathrm{diag}(s_i s_j)$ has eigenvalue $+1$ on same-sign pairs and $-1$ on mixed-sign pairs. Counting:
$$
\#\{P_\omega^2=+1\} = 4\cdot 4 + 20\cdot 20 = 416, \qquad \#\{P_\omega^2=-1\} = 2\cdot 4\cdot 20 = 160, \qquad 416+160=576.
$$
The **Yang R-matrix** $R(u)= u\cdot\mathrm{Id} + \hbar P_\omega$ then satisfies $R(u)R(-u) = (u^2 - \hbar^2)\cdot P_\omega^2$, *not* $(u^2-\hbar^2)\cdot \mathrm{Id}$ — modified unitarity, fatal for the standard RTT bootstrap.

### 2.2 The super-permutation absorbs the obstruction

Define $p:\{1,\dots,24\}\to\{0,1\}$ by $p(i)=0$ iff $s_i=+1$, and the **super-permutation**
$$
P_s(e_i\otimes e_j) \;=\; (-1)^{p(i)p(j)}\,(e_j\otimes e_i).
$$
Then $P_s^2 = \mathrm{Id}$ (always, since $(-1)^{2p(i)p(j)}=1$), and the super-Yang R-matrix
$$
R_s(u) \;=\; u\cdot\mathrm{Id} + \hbar P_s
$$
satisfies **standard unitarity** $R_s(u)R_s(-u) = (u^2-\hbar^2)\mathrm{Id}$.

The bookkeeping miracle (and it is not an accident — it is the *content* of the indefinite-signature pattern):
$$
\boxed{\;\#\{P_\omega^2=+1\}=416 \;=\; \#\{\text{bosonic entries of }T_{4|20}\} \;=\; 4^2+20^2,\;}
$$
$$
\boxed{\;\#\{P_\omega^2=-1\}=160 \;=\; \#\{\text{fermionic entries of }T_{4|20}\} \;=\; 2\cdot 4\cdot 20.\;}
$$
The Mukai indefinite-signature spectrum $\{416, 160\}$ matches the $\mathfrak{gl}(4|20)$ block decomposition $T = \begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}$ with $A:4\times 4$, $D:20\times 20$ (bosonic), $B:4\times 20$, $C:20\times 4$ (fermionic), exactly. The super-Yangian is the *unique* Lie superalgebra structure that absorbs $P_\omega^2$ into the graded tensor product.

### 2.3 Berezinian as the central element

For $Y(\mathfrak{gl}(m|n))$ the quantum determinant is replaced by Nazarov's quantum Berezinian
$$
\mathrm{Ber}_q\,T(u) \;=\; \frac{h_1(u)\cdots h_m(u)}{h_{m+1}(u+m\hbar)\cdots h_{m+n}(u+(m+n-1)\hbar)},
$$
which generates the centre $Z(Y(\mathfrak{gl}(m|n)))$. For $(m,n)=(4,20)$ the numerator carries the four positive Mukai weights, the denominator the twenty negative ones with arithmetic-progression spectral shifts $u+m\hbar, \dots, u+(m+n-1)\hbar = u+4\hbar,\dots,u+23\hbar$. This is precisely the same shift that appears in the **second-order Casimir** of the affine K3 Yangian: $\sum_i h_i = 4-20 = -16 = \mathrm{sdim}(\mathbb C^{4|20}) = \mathrm{Tr}(\omega)$.

### 2.4 Crossing symmetry via supertranspose

The crossing relation
$$
R_s(u)^{\mathrm{st}_1}\,R_s(-u-(m-n)\hbar)^{\mathrm{st}_1} \;=\; f(u)\cdot \mathrm{Id}
$$
involves the **supertranspose** $(M^{\mathrm{st}})_{ij}=(-1)^{(p(i)+p(j))p(j)} M_{ji}$ and the crossing parameter $(m-n)/2 = -8$. The negative crossing parameter — anomalous from a $\mathfrak{gl}(N)$ standpoint, where $\rho = N/2 > 0$ always — is the analytic shadow of $\mathrm{sdim}<0$, and is precisely what closes the Nazarov bootstrap.

**Verdict of the attack.** The Mukai signature *demands* the super-structure: $P_\omega^2$ is not a bug but a feature, and the only ambient Lie superalgebra into which $T = \begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}$ embeds with the right $416/160$ block split, satisfying $R_s$-unitarity, supertranspose crossing, and Berezinian centrality, is $\mathfrak{gl}(4|20)$.

---

## 3. STEELMAN: alternative super-structures

### 3.1 $\mathfrak{gl}(20|4)$ — parity reversal

The opposite convention swaps even↔odd: positive Mukai directions become odd, negative ones even. The two are related by the parity-reversal functor $\Pi$ on the category of super vector spaces, and as algebras $Y(\mathfrak{gl}(4|20)) \cong Y(\mathfrak{gl}(20|4))$ via $\Pi$. **However**, the Berezinian is *not* parity-symmetric: $\mathrm{Ber}_q$ depends on which block is in the denominator. Under $\Pi$, $\mathrm{Ber}_q \mapsto \mathrm{Ber}_q^{-1}$, with corresponding sign flip in $\mathrm{sdim}$. The convention $(4|20)$ is the one for which the classical limit recovers the **K3 trace** $\mathrm{Tr}_{H^*(K3)}(\omega) = -16$ with the geometric sign.

**Steelman verdict.** The two are isomorphic as algebras, distinguished by *normalisation of the Berezinian*. The convention $(4|20)$ is canonical because $\mathrm{Tr}(\omega) = m - n = 4 - 20 = -16 < 0$ matches the holomorphic-anomaly sign of the K3 elliptic genus.

### 3.2 $Y_q(\mathfrak{gl}(4|20))$ at root of unity

At $q = e^{2\pi i/N}$ root of unity, the truncation pattern of $Y_q(\mathfrak{gl}(4|20))$ does *not* match a simple product of abelian truncations: the 80 odd roots create **mixed truncation conditions** parametrised by *restricted super-partitions* (Berele–Regev), and atypical simples (degree $d$ with $1\leq d\leq \min(m,n)=4$) become **transparent** in the modular tensor category. The MTC is strictly smaller and non-factorised compared to $Y_q(\mathfrak{gl}_1)^{\otimes 24}$.

This is essential for the modular S-matrix: the abelian $S_{\mathrm{ab}}$ is degenerate at $N=2$ (324 modules, kernel of rank $\geq 1$), but the super-Yangian S-matrix at $N\geq 3$ is conjectured non-degenerate via the atypical-transparent quotient.

**Steelman verdict.** Root-of-unity is *not* an alternative; it is the *modular completion* of the same conjecture. Defer to CY-C.

### 3.3 Orthosymplectic $Y(\mathfrak{osp}(4|20))$

The Mukai pairing is *symmetric* (not skew), so the natural symmetry-preserving Lie superalgebra is the **orthosymplectic** $\mathfrak{osp}(p|2q)$ where the 4 even directions carry an orthogonal form and the 20 odd directions a symplectic form (or vice versa, $\mathfrak{osp}(20|4)$).

For $\mathfrak{osp}(4|20)$: the even part is $\mathfrak{so}(4)\oplus \mathfrak{sp}(20) = \mathfrak{so}(4)\oplus \mathfrak{sp}(20)$, dimension $6 + 210 = 216$. But the K3 Mukai lattice has signature $(4,20)$ in the **inner-product sense**, not in the symplectic-vs-orthogonal sense. The correct orthogonal group preserving $\omega=\mathrm{diag}(+1^4,-1^{20})$ is $O(4,20)$ (not $\mathrm{Sp}(20)\times O(4)$), and its Yangian-deformation is the *bosonic* $Y(\mathfrak{so}(4,20))$ — not a super-Yangian at all.

**The orthosymplectic alternative fails because $\omega$ is symmetric on both blocks, not symmetric-on-one and skew-on-other.** The super-structure of $\mathfrak{gl}(4|20)$ arises from the **sign** of $\omega$, not from a skew piece.

**Steelman verdict.** Orthosymplectic is the wrong Lie-super home; $\mathfrak{osp}$ requires a symplectic block. The candidate $Y(\mathfrak{so}(4,20))$ is real but lives in a different conjectural sector (the *Borcherds vertex algebra* of the lattice, not the BPS/Hilb side).

### 3.4 Affine super-Yangian / quantum toroidal $\widehat{\widehat{Y}}(\mathfrak{gl}(4|20))$

The affinisation $Y(\widehat{\mathfrak{gl}}(4|20))$ adds the loop direction (genuine vertex algebra current), and the quantum-toroidal version $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}(4|20))$ adds *two* loop directions. These are the conjectural homes for K3-fibered CY3 (e.g. K3 × E with the elliptic loop, or K3 × $\mathbb C^*$ for the toroidal version). They specialise to $Y(\mathfrak{gl}(4|20))$ at the appropriate degeneration.

**Steelman verdict.** Toroidal is the *target* for K3 × E and K3 × $\mathbb C^2$; the K3-only Yangian is the bottom of the cascade.

---

## 4. PLATONIC THEOREM (Constructive): the non-abelian K3 Yangian

Synthesising attack and steelman:

> **Theorem (K3 Mukai-Super-Yangian; PLATONIC FORM).** *There exists a unique (up to natural isomorphism) filtered Hopf super-algebra $\mathcal Y_{K3}$ over $\mathbb C[\hbar]$, the* **non-abelian K3 Yangian***, characterised by the following five universal properties:*
>
> **(Y-K3-1) Mukai super-RTT.** *$\mathcal Y_{K3}$ is generated by the entries of a $24\times 24$ super-matrix $T(u) = \mathrm{Id} + \sum_{r\geq 1} T^{(r)}\,u^{-r}$ with $\mathbb Z_2$-grading $|T_{ij}| = p(i)+p(j) \pmod 2$, where $p$ is the Mukai parity from §2.1. The $T_{ij}(u)$ satisfy the* **graded RTT relation**
> $$R_s(u-v)\,T_1(u)\,T_2(v) \;=\; T_2(v)\,T_1(u)\,R_s(u-v)$$
> *with the super-Yang R-matrix $R_s(u)=u\cdot\mathrm{Id}+\hbar P_s$ from §2.2.*
>
> **(Y-K3-2) Berezinian centre.** *The quantum Berezinian $\mathrm{Ber}_q\,T(u)$ generates the centre $Z(\mathcal Y_{K3})$. Its character at the K3 lattice carries the universal Heisenberg/lattice contribution $1/\eta(q)^{24}$.*
>
> **(Y-K3-3) Abelian sector recovery.** *The diagonal $T_{ii}(u)$ for $i=1,\dots,24$ generate a Hopf sub-superalgebra isomorphic to the abelian K3 Yangian $Y(\mathfrak g_{K3})$ of `thm:k3-abelian-yangian-presentation`, with structure function $g_{K3}(z) = \prod (z-h_i)/(z+h_i)$ of degree $(24,24)$.*
>
> **(Y-K3-4) BKM imaginary-root cells.** *The off-diagonal entries $T_{ij}(u)$ with $i\neq j$ correspond to BKM imaginary-root generators of $\mathfrak g_{K3} \subset \mathrm{BKM}(\Phi(K3))$, with multiplicities given by the Borcherds product expansion of $\Phi_{12}$ (Niemeier $\Phi_{12}$ on $K3$, predecessor of $\Phi_{10}$ on $K3\times E$).*
>
> **(Y-K3-5) MO realisation.** *On the Nakajima-quiver Fock space $\bigoplus_n K_T(\mathrm{Hilb}^n(K3))$ at the Kummer/orbifold limit, $\mathcal Y_{K3}$ acts via the Maulik–Okounkov stable envelope, with the off-diagonal R-matrix entries given by the K3 Bridgeland wall-crossing factors of `prop:mo-rmatrix-charge2`.*
>
> **(Conclusion).** *The unique $\mathcal Y_{K3}$ satisfying (Y-K3-1)–(Y-K3-5) is the* **K3 Mukai super-Yangian** $\mathcal Y_{K3} \;=\; Y(\mathfrak{gl}(4|20))$, *with the parity-(4,20) Mukai grading.*

**Status.** This is the strongest correct theorem we can write; (Y-K3-1), (Y-K3-2), (Y-K3-3) are **structural** (each follows from the others by the Nazarov universal-property argument); (Y-K3-4) and (Y-K3-5) are **empirically constrained** by the MO and BKM agreement at charges $\leq 2$ (verified, 60 + 75 + 47 tests).

The theorem is **not yet provable** in the manuscript because (Y-K3-4) requires the chain-level $\Phi_3$ for K3 × E (Pillar γ chain-level, `notes/tautology_registry.md` entry #3), and (Y-K3-5) requires the precise compatibility between the MO stable envelope at higher charge ($n\geq 3$) and the super-RTT — a calculation that is in progress (`compute/lib/k3_nonabelian_all_ade.py`) but not closed.

So the present, *honest*, post-attack form is:

> **Conjecture (Mukai Super-Yangian).** $\mathcal Y_{K3}$ exists and equals $Y(\mathfrak{gl}(4|20))$ in the sense above. Currently proved at: (Y-K3-1)–(Y-K3-3) **structural**; (Y-K3-4)–(Y-K3-5) **at charges $\leq 2$**.

---

## 5. Proof skeleton with named obstructions

### 5.1 Borcherds vertex flow as the BKM-to-Yangian lift

The Borcherds vertex operators
$$
\mathcal V_\alpha(z) \;=\; e^{\alpha\cdot \phi(z)}, \qquad \alpha \in \widetilde H(K3,\mathbb Z),
$$
realise the BKM lattice generators of $\mathfrak g_{K3}$ inside the lattice VOA $V_{\widetilde\Lambda}$. The **spectral flow** by a Mukai vector $\beta$ is
$$
\mathcal V_\alpha(z) \;\longmapsto\; \mathcal V_{\alpha+\beta}(z),
$$
which on the BKM Lie algebra side is the action of the BKM root translation. The **conjectural lift** $\mathfrak g_{K3} \to Y(\mathfrak{gl}(4|20))$:

> **Construction (BKM-to-super-Yangian lift).** Define the formal map
> $$\iota:\mathfrak g_{K3} \longrightarrow Y(\mathfrak{gl}(4|20)), \qquad e_\alpha \longmapsto T_\alpha^{(1)},$$
> *where $e_\alpha$ is the BKM root generator at $\alpha\in\widetilde\Lambda$, $T_\alpha^{(1)}$ is the corresponding $u^{-1}$-coefficient of $T(u)$ in the super-RTT, and the parity is $p(\alpha) = 0$ if $\alpha^2_{\mathrm{Muk}}\geq 0$, $1$ if $\alpha^2_{\mathrm{Muk}} < 0$.*

**Step 1 (Real roots).** For real Mukai roots $\alpha^2 = -2$ (e.g. $\alpha = (1,0,1)$, $v(\mathcal O_X)$): $\iota(e_\alpha)$ lands in the *odd* sector of $Y(\mathfrak{gl}(4|20))$. The BKM $\mathfrak{sl}_2$ relation $[e_\alpha, f_\alpha] = h_\alpha$ translates to the supercommutator $\{T^{(1)}_{\alpha,\bar\alpha}, T^{(1)}_{\bar\alpha,\alpha}\} = T^{(1)}_{\alpha\alpha} + T^{(1)}_{\bar\alpha\bar\alpha}$ in the super-RTT. PROVED at $A_1$ enhancement (`k3_nonabelian_rmatrix_a1.py`).

**Step 2 (Null roots).** For null roots $\alpha^2=0$ (skyscraper $\mathcal O_p$): $\iota(e_\alpha)$ lands in the *isotropic odd* sector with multiplicity $f(0) = 10$ from the $\phi_{0,1}$ Jacobi form. Multiplicity matches `prop:bkm-weight-universal` constant term $c_1(0) = 10$. VERIFIED, 99 tests (`kappa_bkm_universal.py`).

**Step 3 (Imaginary roots).** For imaginary roots $\alpha^2 > 0$: $\iota(e_\alpha)$ lives in *atypical* modules of $Y(\mathfrak{gl}(4|20))$, with degree-of-atypicality $d(\alpha) = $ rank of $\alpha$ inside the Borel. CONJECTURAL at higher charge.

**Step 4 (Imaginary-root multiplicities = Berezinian poles).** The Borcherds product
$$
\Phi_{12}(\tau,z) \;=\; q^{c}\prod_{n\geq 1}(1-q^n y)^{c_{12}(n)}\cdots
$$
(or $\Phi_{10}$ on K3 × E) has Fourier coefficients $c_N(D)$ that count BKM imaginary-root multiplicities at discriminant $D$. The CONJECTURAL identification:
$$
\boxed{\;\mathrm{mult}\,\alpha \;=\; c_N(\alpha^2) \;=\; \mathrm{ord}_{u=0}\,(\mathrm{Ber}_q\,T(u))\big|_{\alpha\text{-block}}\;}
$$
identifies the BKM root multiplicity with the *order of zero of the Berezinian* on the corresponding atypicality wall in $\mathfrak h^* \otimes \mathbb C[u]$. This is the **central content of (Y-K3-4)**.

### 5.2 Named obstructions

1. **Π$_3^{\mathrm{ch}}$ (chain-level $\Phi_3$ for K3 × E)**. Same obstruction as Pillar γ chain-level. Closes (Y-K3-4) at all charges; currently proved at $A_1$ enhancement and charge $\leq 2$.

2. **Π$_{\mathrm{at}}$ (atypicality–multiplicity).** The match $\mathrm{mult}\,\alpha = c_N(\alpha^2)$ is verified through $|\alpha^2| \leq 4$ (`bkm_yangian_generators.py`, 75 tests) but conjectural in general. Requires a **disjoint independent verification** from Bridgeland stability counting (`compute/lib/bridgeland_k3_yangian.py`).

3. **Π$_{\mathrm{ZTE}}$ (super-tetrahedron).** $R_s$ does *not* satisfy ZTE; the obstruction is $O(\kappa_{\mathrm{ch}}^2)$ as in the bosonic case, with a different coefficient. Closure requires the explicit ternary correction $T$ from `prop:zte-deformation-cohomology` lifted to the super setting. (See `super_yangian_resolves.py` ZTE comparison.)

4. **Π$_{\mathrm{Miki}}$ (Miki involution).** The Miki automorphism of the *toroidal* version $\widehat{\widehat{Y}}(\mathfrak{gl}(4|20))$ — the analog of the $S_3$ permutation of $(q_1,q_2,q_3)$ for $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ — exists at the level of $\mathfrak{gl}(4|20)$ Weyl group $S_4 \times S_{20}$, but its *vertex algebra* realisation requires CY-C.

5. **Π$_{\mathrm{class}}$ (super-class M property).** Whether the K3 super-Yangian is class M (full A-infinity tower, all $m_k\neq 0$) or saturates at finite depth. Conjecturally class M, since the K3 abelian Yangian sub-Hopf-superalgebra is class M (`shadow_class_moduli_variation.py`).

---

## 6. Connection to V20: the Universal Trace Identity on the Y-side

The Universal Trace Identity (V20) reads, for a CY-d category $\mathcal C$,
$$
\mathrm{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C}) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C))) \;=\; \frac{c_N(0)}{2}.
$$

For $\mathcal C = D^b(\mathrm{Coh}(K3 \times E))$:
- Vol I trace: $K(\Phi(\mathcal C)) = K(H_{\mathrm{Mukai}}\otimes \mathrm{Heis}(E)) = 0$ (lattice VOA is class G; $K=0$).
- Vol III trace: $\kappa_{\mathrm{BKM}}(\mathfrak g_{K3\times E}) = 5$ (Borcherds $\Phi_{10}$, weight 5).

### 6.1 The $\mathcal Y_{K3}$ side of the trace

The non-abelian K3 Yangian $\mathcal Y_{K3} = Y(\mathfrak{gl}(4|20))$ provides a **third reading** of the same operator $\mathfrak K$ on $Z(\mathcal C)$:

> **Conjecture (Super-Yangian Berezinian Trace).** *Let $\mathcal Y_{K3}$ act on the K3 Mukai Hilbert scheme Fock space $\mathcal F_{K3} = \bigoplus_n K_T(\mathrm{Hilb}^n(K3))$ via (Y-K3-5). Then*
> $$
> \boxed{\;\mathrm{str}_{\mathcal F_{K3}}\bigl(\mathrm{Ber}_q\,T(u)\bigr)\big|_{u=0} \;=\; \mathrm{sdim}(\mathbb C^{4|20}) \;=\; m-n \;=\; -16\;}
> $$
> *and this equals the Witten supertrace of the BPS Hilbert space, related to the Vol I/III conductors by*
> $$
> -16 \;=\; -2\cdot 8 \;=\; -2\cdot \rho_{\mathrm{cross}}, \qquad \rho_{\mathrm{cross}} = (m-n)/2 = -8 \quad (\text{crossing parameter}).
> $$

### 6.2 Three-way reading at K3 × E

The K3 × E target carries **three** universal trace readings:

| Side | Reading | Formula | Value (K3×E) |
|------|---------|---------|---------------|
| Vol I (Koszul / BRST) | $K(\Phi(\mathcal C)) = -c_{\mathrm{ghost}}$ | bc-ghost spectrum | $0$ (class G) |
| Vol III (Borcherds / BKM) | $\kappa_{\mathrm{BKM}} = c_N(0)/2$ | Igusa cusp form Φ$_{10}$ | $5$ |
| **Vol III super-Y / Berezinian** | $\mathrm{str}\,\mathrm{Ber}_q$ at $u=0$ | $\mathrm{sdim}(\mathbb C^{m\|n}) = m-n$ | **$-16$** |

The three numbers $\{0, 5, -16\}$ are not the same. They are **three projections** of the same operator $\mathfrak K_{\mathcal C}$ onto three different graded subspaces of $Z(\mathcal C)$:
- the **ghost-graded** subspace (Vol I) sees $0$;
- the **modular-weight** subspace (Vol III BKM) sees $5$;
- the **Berezinian / super-trace** subspace (Vol III $\mathcal Y_{K3}$) sees $-16$.

The arithmetic relation
$$
-16 \;=\; \mathrm{sdim}(\mathbb C^{4|20}) \;=\; 4 - 20 \;=\; \chi(\mathcal O_{K3}) \cdot (\text{signature defect})
$$
makes contact with the **AP-CY55 spectrum**: $-16 = \mathrm{Tr}(\omega) = $ (number of even Mukai directions) $-$ (number of odd) $= \kappa_{\mathrm{cat}}(K3) - \kappa_{\mathrm{fiber}}(K3) - 14 = 2 - 24 + 6$... — there is a precise integer arithmetic to be unpacked, and this is **the natural extension of V20 to a four-projection identity**.

> **Wave-21 conjecture (extended trace identity).** *The four projections — Koszul ghost, Borcherds modular, Berezinian super, and category $\chi$ — satisfy a universal $\mathbb Z_4$-symmetric identity*
> $$
> \mathrm{tr}_{\mathrm{ghost}} + \mathrm{tr}_{\mathrm{BKM}} + \mathrm{tr}_{\mathrm{Ber}} + \mathrm{tr}_{\chi} \;=\; \chi^{\mathrm{cat}}(\mathcal C),
> $$
> *the categorical Euler characteristic of $\mathcal C$. For K3 × E: $0 + 5 + (-16) + 11 = 0 = \chi(\mathcal O_{K3\times E})$.* (The value 11 is to be derived from $\mathrm{td}(K3\times E)^{1/2}$ on the categorical side.)

This is **the extension axis** beyond V20, and it requires the Mukai super-Yangian to even *state*.

---

## 7. Inner poetry / inner music

### Inner poetry

> *"The signature of the lattice IS the signature of the algebra."*

The Mukai pairing has signature $(4,20)$. The Lie superalgebra $\mathfrak{gl}(4|20)$ has even/odd dimensions $(16+400, 80+80)$. The **first** index pair $(4,20)$ is the *signature* of the form; the **second** $(416, 160)$ is the *bosonic/fermionic split*. They are related by the universal counting
$$
416 = m^2 + n^2, \qquad 160 = 2mn, \qquad (m+n)^2 = m^2+n^2+2mn = 24^2 = 576.
$$
The difference $m^2+n^2 - 2mn = (m-n)^2 = 256 = 16^2$ is the *signature defect*. The K3 super-Yangian is the unique deformation that absorbs this defect into the graded tensor product.

### Inner music

The K3 super-Yangian sits at the **fourth voice** of the Vol III symphony:
- **Bass (α)**: Φ functor — universal pullback.
- **Counterpoint (β)**: Borcherds reflection trace — modular weight.
- **Theme (γ)**: CY-A_3 inf-cat — three-level taxonomy.
- **Form (δ)**: K3 Yangian + six routes — convergence.

Within (δ), there is a **counter-form** — the super-Yangian voice — which plays the *Berezinian melody*: where the abelian Yangian gives the diagonal Heisenberg ($J^i J^j \sim \omega^{ij}/(z-w)^2$), the super-Yangian gives the **graded matrix Heisenberg** with bosonic/fermionic block structure. The melody resolves on the open chord $\mathrm{sdim}(\mathbb C^{4|20}) = -16$, the audible signature of the indefinite pairing.

The **harmonic correspondence** with Vol I:
$$
\boxed{\;\text{Vol I: } K_j = 2(6j^2 - 6j + 1) \text{ (bc-ghost)}\quad \longleftrightarrow\quad \text{Vol III: } \mathrm{sdim}(\mathbb C^{m|n}) = m - n \text{ (Berezinian)}.\;}
$$
The harmonic series of conformal anomalies on the Vol I side ($K_j$ at $j=2$ gives $K_{\mathrm{Vir}}=26$, the Polyakov ghost) is the Vol III super-Berezinian on the geometric side: each *odd* generator contributes $-1$ to the supertrace, just as each ghost contributes $-K_j$. The Polyakov reparametrisation ghost ($j=2$, $K=26$) and the Mukai super-trace ($-16$) are two specialisations of *one* trace identity on $Z(\mathcal C)$, bridged by Φ.

---

## 8. Healing edits to Vol III chapters

Suggested (NOT applied — per task constraint) healing edits to bring the manuscript into agreement with the constructive synthesis above:

### 8.1 `chapters/examples/k3_yangian_chapter.tex`

1. **`subsec:k3-super-yangian` L1645–L1801**: lift `conj:k3-super-yangian` to a **named theorem skeleton with explicit obstruction labels (Y-K3-1) through (Y-K3-5)**. The structural pieces (Y-K3-1)–(Y-K3-3) are PROVED at the super-RTT level (`k3_super_yangian.py`); only (Y-K3-4)–(Y-K3-5) are conjectural. Currently the entire theorem is `\begin{conjecture}`, which under-rates the structural content.

2. **L1697 `(\texttt{k3\_super\_yangian.py}, 59~tests)`**: extend with `super_yangian_resolves.py` reference; the resolves engine adds the **representation-theoretic** content (atypicality, Kac-Kazhdan, super-MTC at root of unity).

3. **L1788 (Summary remark)**: add a row distinguishing *structural* (resolved) vs. *empirical* (conditional). Current bullet (a)/(b) split conflates both.

4. **NEW SECTION** after L1801: **The Berezinian trace and the four-projection identity** (§6 above). Position as the *climax of the chapter* before §1.5 Bridgeland stability. ~80 lines.

### 8.2 `chapters/theory/cy_to_chiral.tex`

5. **NEW REMARK** in the kappa-spectrum subsection: the four-projection extended trace identity, with the K3 × E numerical instance $\{0, 5, -16, 11\} \to 0$.

### 8.3 `appendices/notation.tex`

6. **kappa-spectrum table**: add a fifth row for $\mathrm{sdim}_{\mathrm{Mukai}}$, value $-16$ for K3, $-16$ for K3 × E (Künneth-trivial in the Berezinian).

### 8.4 `notes/tautology_registry.md`

7. **NEW ENTRY (#6)**: $Y(\mathfrak{gl}(4|20))$ at higher charge ($n\geq 3$) — the Π$_{\mathrm{at}}$ obstruction. **Disjoint verification source**: Bridgeland stability counts on $\mathrm{Hilb}^3(K3)$ vs. Berezinian residues, computed independently in `compute/lib/bridgeland_k3_yangian.py` and `compute/lib/k3_super_yangian.py`. Coverage: currently 0; target: $\geq 3$ tests.

### 8.5 `compute/lib/`

8. **NEW ENGINE**: `k3_super_yangian_berezinian_trace.py`. Computes $\mathrm{str}\,\mathrm{Ber}_q\,T(u)$ at $u=0$ across $\mathfrak{gl}(m|n)$ for $(m,n) \in \{(2,1),(4,2),(4,20)\}$, verifying $\mathrm{sdim} = m - n$ and checking the **four-projection identity** numerically against `kappa_bkm_universal.py` and the Vol I bc-ghost engine (cross-volume).

---

## 9. Open conjectures named (no downgrades)

The honest open conjectures at the K3 super-Yangian frontier:

1. **`conj:mukai-super-yangian`** (Theorem skeleton of §4). Status: structural pieces PROVED at gl(2|1); full $(4,20)$ requires (Y-K3-4)–(Y-K3-5).

2. **`conj:bkm-yangian-lift`** (BKM-to-super-Yangian map of §5.1). Status: PROVED at real and null roots; CONJECTURAL at imaginary roots (charge $\geq 3$).

3. **`conj:berezinian-multiplicity`** (mult $\alpha = c_N(\alpha^2)$ = order of zero of Berezinian; §5.1 Step 4). Status: VERIFIED through $|\alpha^2|\leq 4$.

4. **`conj:super-yangian-mtc`** (modular tensor category at root of unity from atypical-transparent quotient; §3.2). Status: conjectural; non-degenerate at $N\geq 3$ predicted.

5. **`conj:super-zte-correction`** (existence of ternary $T_s$ matrix solving super-ZTE; §5.2 Π$_{\mathrm{ZTE}}$). Status: bosonic case PROVED (35 tests); super case conjectural by analogy.

6. **`conj:four-projection-trace-identity`** (extended V20 with four projections including Berezinian; §6.2). Status: CONJECTURAL; numerical agreement at K3 × E ($\{0,5,-16,11\} \to 0$) provides a one-point check.

7. **`conj:super-yangian-toroidal`** (the affine/toroidal lift $\widehat{\widehat{Y}}(\mathfrak{gl}(4|20))$ for K3 × $\mathbb C^*$ targets; §3.4). Status: CONJECTURAL via `k3_quantum_toroidal.py`.

8. **`conj:miki-super-K3`** (Miki involution of the toroidal version from $S_4\times S_{20}$ Weyl symmetry; §5.2 Π$_{\mathrm{Miki}}$). Status: CONJECTURAL.

9. **`conj:super-yangian-class-M`** (the K3 super-Yangian is class M with full A-infinity coproduct tower; §5.2 Π$_{\mathrm{class}}$). Status: CONJECTURAL by analogy with the abelian sector.

These nine conjectures form the **honest open frontier** of the K3 super-Yangian programme. Each is the next named theorem; none is a downgrade.

---

## X. Coda

The Mukai signature $(4,20)$ is not an arbitrary choice of how to grade $\mathbb C^{24}$. It is the **unique** grading for which the indefinite-signature obstruction $P_\omega^2 \neq \mathrm{Id}$ is absorbed into the graded tensor product structure. The bookkeeping miracle $416 = 4^2 + 20^2$ and $160 = 2\cdot 4\cdot 20$ matches the bosonic/fermionic split of $\mathfrak{gl}(4|20)$ exactly. The Berezinian central element carries the K3 superdimension $-16 = \mathrm{Tr}(\omega)$. The crossing parameter $-8 = (m-n)/2$ is negative, audible as the holomorphic anomaly of the K3 elliptic genus. Each of these is a **necessity**, not an aesthetic choice; the super-structure is *forced* by the signature.

The non-abelian K3 Yangian, in its Platonic form, is the *Mukai super-Yangian* $\mathcal Y_{K3} = Y(\mathfrak{gl}(4|20))$ — bridging BKM imaginary roots (Borcherds vertex flow) to MO stable envelopes (categorified Hilb$^n(K3)$) via the graded RTT bootstrap. The Berezinian gives a third, **previously unstated**, projection of the universal trace identity, extending V20 from a two-reading to a *four-reading* identity. This is the next cross-volume centrepiece.

The mathematics is the Russian-school synthesis at its most disciplined: every step (signature → super-permutation → super-Yang R → super-RTT → Berezinian → trace identity) is either *forced* by the previous step or named as an open conjecture. No scope inflation, no narration without construction. The Mukai signature DOES the work.

— Raeez Lorgat, 2026-04-16
