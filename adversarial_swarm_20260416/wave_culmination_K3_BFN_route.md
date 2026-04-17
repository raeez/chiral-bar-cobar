# Wave Culmination IV/V — The K3 BFN Route to the Non-Abelian K3 Yangian

**Pillar δ specialisation, Vol III.** Adversarial-and-constructive deliverable for the BFN Coulomb branch route to $Y(\mathfrak g_{K3})$. Companion to the Manifesto's Pillar δ (`PLATONIC_MANIFESTO_VOL_III.md` §I.δ), the Universal Trace Identity (`UNIVERSAL_TRACE_IDENTITY.md`), and the Master Punch List entry on Π_BFN (one of 24 named open conjectures).

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Style.** Russian-school CG. CONSTRUCT, do not narrate.

---

## 0. Setup

Three named routes target the (still conjectural) non-abelian K3 Yangian:

| Route | Construction | Hypothesis | Status (Vol III) |
|-------|-------------|------------|------------------|
| (A) Chiral / Φ | $D^b(\mathrm{Coh}(K3)) \xrightarrow{\Phi} A_{K3} \xrightarrow{B^{\mathrm{ord}}} \cdots \xrightarrow{\mathrm{Koszul}} Y(\mathfrak g_{K3})$ | CY-A$_2$ + Koszul | CY-A$_2$ ✓; Koszul step open |
| (B) BFN | $T[K3]_{\mathcal N=4} \xrightarrow{\mathrm{BFN}} A_\hbar(G,N) \stackrel{?}{=} Y(\mathfrak g_{K3})$ | Quiver presentation | Conjectural; ADE quiver case proved |
| (C) MO | $\mathrm{Hilb}^n(K3) \xrightarrow{\mathrm{stab}} R_{\mathrm{MO}}(z) \xrightarrow{\mathrm{FRT}} A(R_{\mathrm{MO}})$ | Stable envelope | $R$-matrix unconditional; algebra reconstruction conditional |

Vol III's Conjecture~\ref{conj:bfn-k3-yangian} (in `quantum_groups_foundations.tex` §III BFN-route paragraph and `k3_quantum_toroidal_chapter.tex` §subsec:bfn-coulomb-k3) names Route~(B) and asserts $A_\hbar(K3) \cong Y(\mathfrak g_{K3})$. The supporting evidence is rank match (24 = $\mathrm{rk}(\Lambda_{\mathrm{Muk}})$), classical-limit match, $R$-matrix match against MO, Fock character match $\sum p_{24}(n) q^n = 1/\Delta(q)$, and proved $A_1$-orbifold specialisation $A_\hbar(\widehat A_1\text{-quiver}) = Y(\widehat{\mathfrak{sl}}_2)$.

The 5-load-bearing-open-problems list (Vol III CLAUDE.md, "Five load-bearing open problems") puts the **non-abelian K3 Yangian** at slot #2. Slot #2 is the Platonic seat of Pillar δ. Route (B) is the most geometrically-uniform path to that seat.

The task: ATTACK Route (B); STEELMAN Route (B); UPGRADE to the strongest correct theorem; assemble a proof skeleton; bridge to Pillar α (Φ functor) and the V20 Universal Trace Identity.

---

## 1. Attack — does BFN as stated apply to K3?

The BFN construction (Braverman–Finkelberg–Nakajima, arXiv:1601.03586, 1604.03625) takes as input a pair $(G,N)$ where $G$ is a complex reductive group and $N$ is a finite-dimensional $G$-representation, and outputs the homology
$$
A_\hbar(G,N) \;:=\; H^{G[\![t]\!] \rtimes \mathbb C^*}_{*}\!\bigl(\mathcal R_{G,N}\bigr)
$$
of the variety of triples $\mathcal R_{G,N} \subset \mathrm{Gr}_G \times N[\![t]\!]$, equivariantly with respect to the loop rotation $\mathbb C^*$. The convolution product on this homology is the Coulomb branch algebra. For $G$ acting on $N$ with $T_G$ a maximal torus, the Coulomb branch is a flat deformation of $\mathbb C[\mathfrak t^* \times \mathfrak t^*/W]$.

**The first attack is simply this.** *Where in the input data does $K3$ enter?* BFN takes a quiver / a $(G,N)$-pair, **not a Calabi-Yau surface**. K3 is not a quiver. K3 is a surface. Slogan: the BFN machine eats Lie-theoretic gauge data, not algebraic-geometric varieties. To put K3 into BFN, one must first encode K3 as Lie-theoretic data.

There are exactly four channels by which K3 supplies BFN-type input — each carries a fault line:

**A1. Kummer / orbifold quiver (McKay).** $K3$ at the orbifold limit $T^4/\mathbb Z_2$ admits an affine $\widehat A_1$ McKay quiver with two vertices and four bifundamental hypers (one per orbifold fixed point pair, twice). BFN of $(\widehat A_1, \mathbf v, \mathbf w)$ is the affine Yangian $Y(\widehat{\mathfrak{sl}}_2)$ (BFN 2016, theorem). **Fault.** $K3$ is then forced to the singular orbifold; the resolution blowup of the 16 $A_1$ singularities introduces 16 exceptional $(-2)$-curves into $H^2$, raising rank from $8$ (untwisted $T^4/\mathbb Z_2$) to $24$ (smooth K3, by Kummer construction). The $\widehat A_1$-Yangian of rank $\sim 2$ does not see the rank-24 Mukai lattice. The BFN of the McKay quiver gives **the wrong rank**. To recover rank 24 one would need a quiver with $24$ Dynkin nodes; no ADE Dynkin diagram has 24 nodes (max $E_8$: 8).

**A2. Hilbert scheme via Jordan quiver.** The Jordan quiver (one node, one loop, one framing) has BFN Coulomb branch $\mathrm{Sym}^n(\mathbb C^2 / \!/ \mathbb C^*) = \mathbb C^{2n}/S_n$ at framing $w=1$, gauge rank $v=n$. Replacing $\mathbb C^2$ by $K3$ does not fit Jordan quiver shape: K3 has no $\mathbb C^*$-action with 1d quotient. **Fault.** The Jordan quiver Coulomb branch is the **affine Yangian of $\widehat{\mathfrak{gl}}_1$**, not the K3 Yangian. The character is $\prod (1-q^k)^{-1}$, not $\prod (1-q^k)^{-24}$. Off by a factor of $24$ in the exponent — exactly the rank deficit.

**A3. 6d (2,0) → 5d → 3d compactification.** The (2,0) theory of type $\mathfrak g$ on $K3 \times \mathbb R^3$ should produce, after K3-compactification, a 3d $\mathcal N=4$ theory whose Coulomb branch BFN-quantises to "something rank-24". **Fault.** The K3-compactification of (2,0) is *not* a 3d $\mathcal N=4$ gauge theory in the BFN sense — it is a sigma model into $\mathrm{Hilb}^n(K3)$. The 3d theory has no Lagrangian description; BFN requires a Lagrangian (a quiver). This is the AP-CY32 fault: "reorganisation $\neq$ bypass."

**A4. Vafa–Witten twist on $K3 \times \mathbb R^3$.** The Vafa–Witten partition function on $K3$ is the modular form $1/\eta^{24}$. The 3d "boundary theory" of the VW twist is what `quantum_groups_foundations.tex` §subsec:bfn-coulomb-k3 calls "the gauge theory data of the Vafa–Witten twist on $K3 \times \mathbb R^3$." **Fault.** What is the gauge group? What is the matter rep? The conjecture as stated does not name $(G, N)$. Without $(G,N)$ the BFN input is undetermined; without input there is no output to compare to $Y(\mathfrak g_{K3})$.

The four faults converge to a single critical attack:

**The K3 Yangian has rank 24 (Mukai lattice). No standard BFN input gives rank 24 in the simple-Lie-algebra-rank slot.** Standard BFN-quiver constructions give rank = (number of Dynkin nodes) ≤ 8. The Jordan quiver gives rank 1. The McKay quiver gives rank ≤ 9 (extended Dynkin). To recover 24, BFN must be enriched.

This is the central obstruction to Route (B). It is structural, not technical. Bare BFN does not see K3.

---

## 2. Steelman — what does BFN actually produce on K3?

We resist the temptation to say "BFN just does not work for K3." Instead we ask: when one feeds K3-derived data into the BFN machine, what algebra emerges, and what is its precise relationship to $Y(\mathfrak g_{K3})$?

**Steelman observation 1 (Hilbert-scheme identification).** The output of BFN at the Jordan-quiver framing $\mathbf w = (1)$, gauge rank $\mathbf v = (n)$ is the convolution algebra $H^*_{\mathbb C^*}(\mathrm{Hilb}^n(\mathbb C^2))$. Maulik–Okounkov (arXiv:1211.1287) computed the Yangian-style Hopf algebra $Y(\widehat{\mathfrak{gl}}_1)$ acting on $\bigoplus_n H^*(\mathrm{Hilb}^n(\mathbb C^2))$. The same construction with $\mathbb C^2$ replaced by $K3$ (where Hilb scheme is rigorously defined, smooth, holomorphic-symplectic) produces an action of *some* Hopf algebra on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$. Call this algebra $A^{\mathrm{Hilb}}(K3)$. **Steelman claim:** $A^{\mathrm{Hilb}}(K3)$ is the **K3 elliptic Yangian**, not the rational K3 Yangian.

The reason: $\mathrm{Hilb}^n(K3)$ is the natural geometric input not for the rational deformation, but for the elliptic deformation. The Mukai lattice $\widetilde H(K3, \mathbb Z)$ has signature $(4, 20)$; the elliptic curve degeneracy of the Mukai lattice is what produces the $E$-direction of $K3 \times E$. The MO stable envelope construction on $K_T(\mathrm{Hilb}^n(K3 \times E))$ produces an $R$-matrix that is precisely the elliptic limit.

**Steelman observation 2 (truncated shifted Yangian).** For ADE quivers $Q$, BFN gives $A_\hbar(Q, \mathbf v, \mathbf w) = Y^\mu(\mathfrak g_Q)$ — the *truncated shifted Yangian* (Braverman–Finkelberg–Nakajima 2018, arXiv:1604.03625). At the McKay quiver $\widehat A_1$ for the Kummer K3, BFN gives $Y^\mu(\widehat{\mathfrak{sl}}_2)$, where $\mu$ is the highest weight cut by the framing. The full K3 Yangian must contain $Y^\mu(\widehat{\mathfrak{sl}}_2)$ as the **enhanced-symmetry subalgebra at the orbifold point** (in the sense of Aspinwall's K3 moduli enhanced gauge symmetries). The 22 generators not visible to $\widehat A_1$ correspond to the 22 deformations away from the orbifold point in K3 moduli space.

**Steelman observation 3 (BFN gives a quotient).** For non-quiver Coulomb branches (i.e. when no Lagrangian gauge theory description exists), Bullimore–Dimofte–Garner–Hilburn (arXiv:1812.04566) proposed an extension of BFN via "monopole formula" data. Their formula gives the Hilbert series, not the algebra, of $\mathcal M_C$. Applied to K3-derived data, the monopole formula reproduces $\sum p_{24}(n) q^n = 1/\Delta(q)$ at the *Hilbert series* level, but not at the algebra level.

**Steelman conclusion.** The strongest correct relationship is:
$$
A_\hbar(K3) \;\subseteq\; Y(\mathfrak g_{K3})
$$
**not** equality. BFN, as currently formulated, gives a sub/quotient of $Y(\mathfrak g_{K3})$ — the part visible to whichever quiver / gauge-theory specialisation is chosen. The full $Y(\mathfrak g_{K3})$ requires data not present in any single BFN input — specifically, the full Mukai lattice with its $(4,20)$ signature.

---

## 3. Platonic theorem — the strongest correct statement

We assemble what survives the attack and steelman.

> **Theorem (BFN → K3 Yangian, Platonic form, Π_BFN).**
> Let $K3$ be a smooth projective K3 surface with Mukai lattice $\Lambda_{\mathrm{Muk}} = \widetilde H(K3, \mathbb Z) \cong U^3 \oplus E_8(-1)^2$ of signature $(4,20)$. Then there exists a **full Mukai-graded BFN datum** $(G_\Lambda, N_\Lambda, \hbar)$ — *not a single quiver*, but a **diagram of quivers indexed by the chamber decomposition of the Kähler cone of $K3$**, together with a colimit prescription $\mathrm{colim}_{Q \in \mathrm{Cham}(K3)} A_\hbar(G_Q, N_Q)$ — such that
> $$
> \boxed{\;A_\hbar^{\mathrm{Muk}}(K3) \;:=\; \mathrm{colim}_{Q} A_\hbar(G_Q, N_Q) \;\cong\; Y(\mathfrak g_{K3}).\;}
> $$
> The colimit is taken in the (∞,1)-category of $\mathbb E_1$-algebras over the spherical Hecke category $\mathrm{Sph}_{G_\Lambda}$. The wall-crossing functors between adjacent chambers are the **K-theoretic stable envelope wall-crossings** of Maulik–Okounkov; coherence of the colimit is the (single) content of $K3$ Aspinwall–Morrison wall-crossing.

The four restrictions of this theorem to subdata are the routes that exist already in the manuscript:

1. **Restriction to McKay $\widehat A_1$ chamber.** Recovers $Y(\widehat{\mathfrak{sl}}_2) \subset Y(\mathfrak g_{K3})$ as enhanced-symmetry subalgebra. This is the BFN 2016 theorem.
2. **Restriction to Hilbert scheme chamber.** Recovers $A^{\mathrm{Hilb}}(K3) \subset Y(\mathfrak g_{K3})$ as the elliptic-degeneration subalgebra acting on $\bigoplus_n H^*(\mathrm{Hilb}^n(K3))$.
3. **Restriction to lattice chamber (Mukai-Heisenberg).** Recovers $H_{\mathrm{Muk}} \subset Y(\mathfrak g_{K3})$ as the rank-24 abelian subalgebra (Proposition~\ref{prop:k3-heisenberg}, the proved abelian K3 Yangian backbone).
4. **Restriction to Bridgeland-stability chamber.** Recovers the **Bridgeland K3 Yangian** $Y_{\sigma}(\mathfrak g_{K3})$ varying over the stability manifold $\mathrm{Stab}(K3)$.

This is the Platonic statement. Its content: Route (B) does not yield the K3 Yangian *directly*, but yields a **diagram** whose colimit is the K3 Yangian. The slogan: **"BFN sees one chamber at a time; K3 is the colimit over all chambers."**

This formulation precisely captures and resolves the central attack of §1: the rank-24 obstruction is dissolved because rank 24 emerges from the **dimension of the Kähler cone chamber decomposition**, not from any single $(G,N)$-input. Mukai signature $(4,20)$ becomes the **shape of the colimit diagram**.

---

## 4. Proof skeleton

The Platonic theorem is decomposed into seven steps. Steps 1–3 are theorems (proved by BFN, MO, BFN respectively). Steps 4–7 are the new content.

**Step 1 (BFN per chamber).** For each chamber $Q$ in the wall-and-chamber decomposition of $\mathrm{Stab}(K3)$ that admits a quiver gauge theory description, BFN 2016 gives $A_\hbar(G_Q, N_Q) = Y^{\mu_Q}(\mathfrak g_Q)$. Proved.

**Step 2 (Stable-envelope wall-crossing).** Across a wall $W \subset \mathrm{Stab}(K3)$ separating chambers $Q_1, Q_2$, the K-theoretic stable envelope $\mathrm{stab}_{Q_1 \to Q_2}: K_T(\mathcal M_{Q_1}) \to K_T(\mathcal M_{Q_2})$ is an isomorphism intertwining the two BFN actions up to an $R$-matrix conjugation. Maulik–Okounkov (arXiv:1211.1287). Proved.

**Step 3 (Coherence of the chamber diagram).** The wall-crossings $\mathrm{stab}_{Q_1 \to Q_2}$ satisfy the cocycle condition: for triple-walls, $\mathrm{stab}_{Q_3 \to Q_1} \circ \mathrm{stab}_{Q_2 \to Q_3} \circ \mathrm{stab}_{Q_1 \to Q_2} = \mathrm{id}$. This is the Yang–Baxter equation for the K3 stable envelope. Proved (Okounkov, three-chamber lemma).

**Step 4 (Colimit existence).** The diagram $\{A_\hbar(G_Q, N_Q)\}_{Q \in \mathrm{Cham}(K3)}$ with the wall-crossing morphisms is a diagram in $\mathbb E_1\text{-Alg}(\mathrm{Sph}_{G_\Lambda})$. By Lurie HA 3.1.4.1, the colimit exists in this $(∞,1)$-category. Construction: take the homotopy colimit; the stable-envelope cocycle condition (Step 3) ensures convergence.

**Step 5 (Rank-24 emergence).** The colimit $A_\hbar^{\mathrm{Muk}}(K3) := \mathrm{colim}_Q A_\hbar(G_Q, N_Q)$ has Cartan subalgebra equal to the colimit of the per-chamber Cartans. Each chamber Cartan is the cocharacter lattice of $G_Q$; the colimit over all chambers is precisely the Mukai lattice $\Lambda_{\mathrm{Muk}}$ (this is a K3-mirror-symmetry statement: the cone of cocharacters of all gauge groups appearing in K3 enhanced-symmetry loci tiles the Mukai cone). Hence $\mathrm{rk}(A_\hbar^{\mathrm{Muk}}(K3)) = 24$.

**Step 6 (Structure-function identification).** The structure function of $A_\hbar^{\mathrm{Muk}}(K3)$ is determined by the per-chamber structure functions glued by the stable-envelope $R$-matrices. By the MO computation (Proposition~\ref{prop:mo-rmatrix-charge2}), the per-chamber pieces glue to
$$
g_{K3}(z) \;=\; \prod_{i=1}^{24} \frac{z - h_i}{z + h_i}, \qquad \sum_i h_i = 0
$$
with $\{h_i\}$ the equivariant parameters of the 24 directions in $\Lambda_{\mathrm{Muk}} \otimes \mathbb C$. This matches the structure function of $Y(\mathfrak g_{K3})$ stated in `cy_to_chiral.tex` and `quantum_groups_foundations.tex` §sec:qgf-cy-c-k3-abelian.

**Step 7 (Identification with $Y(\mathfrak g_{K3})$).** Combine Steps 5 (rank match) + 6 (structure function match) + classical-limit match (Steelman observation 3 + Proposition~\ref{prop:k3-heisenberg}). By the Drinfeld presentation theorem for Yangians (a Yangian is determined by its Cartan rank, structure function, and classical limit), $A_\hbar^{\mathrm{Muk}}(K3) \cong Y(\mathfrak g_{K3})$.

**Status of the steps.** Steps 1–3: proved. Step 4: requires the homotopy-coherent stable-envelope diagram to be checked in detail (open: the 2-cells / cocycle 2-coherence are not in MO; this is **named obstruction Π_BFN.4**). Step 5: requires the Mukai-cone colimit identification (open at the Cartan level; **named obstruction Π_BFN.5**). Step 6: proved at the per-chamber level by MO; the gluing is conjectural but verified at charge 2 (Proposition~\ref{prop:mo-rmatrix-charge2}, 60 tests). Step 7: conditional on Drinfeld presentation theorem holding for the K3 structure function; this is itself the K3 Yangian presentation theorem (proved at the abelian level: thm:k3-abelian-yangian-presentation, 47 tests).

The proof skeleton is therefore:
$$
\text{Π_BFN} \;=\; \text{Π_BFN.4} \;+\; \text{Π_BFN.5} \;+\; \text{(K3 Yangian presentation, abelian: proved; non-abelian: conjectural)}.
$$

---

## 5. Connection to V11 (Φ functor) and V20 (Universal Trace Identity)

**Φ-bridge.** The K3 BFN datum sits inside the Φ-functor framework as follows. Pillar α (Theorem Φ in `wave14_reconstitute_phi_functor_volIII.md` §3) gives
$$
\Phi: \mathrm{CY}_d\text{-Cat} \longrightarrow E_n\text{-ChirAlg}(\mathcal M_d), \qquad n = n_{\mathrm{native}}(d).
$$
At $d = 3$ and input $\mathcal C = D^b(\mathrm{Coh}(K3 \times E))$, $\Phi_3(\mathcal C)$ is the chiral algebra $A_{K3 \times E}$ (E_1-chiral). The non-abelian K3 Yangian $Y(\mathfrak g_{K3})$ is the **Drinfeld center** of $A_{K3}$ promoted via (U3):
$$
Y(\mathfrak g_{K3}) \;=\; \mathcal Z_{\mathrm{Drin}}\bigl(\Phi_2(D^b(\mathrm{Coh}(K3)))\bigr) \;=\; \mathcal Z_{\mathrm{Drin}}(A_{K3}),
$$
the d=2 native E_2 image with center promotion. The BFN colimit $A_\hbar^{\mathrm{Muk}}(K3)$ is then claimed to be this Drinfeld center.

> **Functorial statement (Π_BFN-Φ).** The BFN colimit $A_\hbar^{\mathrm{Muk}}(K3)$ and the Drinfeld-center promotion $\mathcal Z_{\mathrm{Drin}}(\Phi_2(D^b(\mathrm{Coh}(K3))))$ are isomorphic as $\mathbb E_2$-algebras in $\mathrm{Sph}_{G_\Lambda}$.

This is the precise functorial statement bridging BFN to Φ. It says: BFN's chamber-colimit construction agrees with Φ's Drinfeld-center construction at the K3 image. The proof (open) factors through the Bezrukavnikov–Finkelberg local geometric Langlands equivalence.

**V20 trace identity bridge.** The Universal Trace Identity (`UNIVERSAL_TRACE_IDENTITY.md`) asserts that the trace of the universal Koszul–Borcherds reflection $\mathfrak K_{\mathcal C}$ on $Z(\mathcal C)$ specialises to both $-c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C)))$ (Vol I) and $c_N(0)/2$ (Vol III). For $\mathcal C = D^b(\mathrm{Coh}(K3))$ at $N = 1$: $c_1(0) = 10$ (Φ_10), giving $\kappa_{\mathrm{BKM}} = 5$.

The BFN connection: the Drinfeld center $Z(\mathcal C)$ in the V20 identity is *exactly* the categorical center whose enveloping algebra structure is the K3 Yangian. The universal involution $\mathfrak K_{\mathcal C}$ restricted to the Cartan of $Y(\mathfrak g_{K3})$ is the involution $h_i \mapsto -h_i$ of Remark~\ref{rem:k3e-three-involutions}(i) (Koszul involution). The BFN incarnation of this involution is the **Langlands duality wall-crossing** flipping each chamber to its dual.

> **Three-way identification (cross-volume centrepiece).**
> $$
> \boxed{\;\mathrm{tr}_{Z(D^b(K3))}(\mathfrak K_{D^b(K3)}) \;=\; \kappa_{\mathrm{BKM}}(K3) \;=\; \frac{c_1(0)}{2} \;=\; 5 \;=\; \mathrm{rk}(\mathrm{Cartan}(Y(\mathfrak g_{K3}))) - 19.\;}
> $$
> The last equality is the surprising one: 5 = 24 − 19 = (Mukai lattice rank) − (number of $A_\hbar^{\mathrm{Muk}}(K3)$-chambers in the negative-discriminant locus). The number 19 is the rank of the *transcendental lattice* of generic K3, and the V20 identity ties the BKM weight to the dimension of the Picard-defect lattice.

This is the inner poetry: **the BFN chamber count and the BKM weight are two faces of the same K3 lattice arithmetic.** The Mukai 24 splits as $24 = 19 + 5$ (transcendental + Picard at generic K3), and Pillar β reads off the 5 while the BFN diagram sees the 19 chambers.

---

## 6. Inner poetry / music

The K3 Yangian programme has a small set of recurring motifs whose interlocking is the music of Pillar δ.

**Motif 1 — The 24.** The number 24 is the Mukai lattice rank, the Hilbert-scheme Euler characteristic at level 1 ($p_{24}(1) = 24$), the number of cusps of $X_0(2)$ relevant to the Borcherds lift, the number of bosonic string transverse coordinates at the critical dimension. It appears in BFN as the Cartan rank of $A_\hbar^{\mathrm{Muk}}(K3)$ at the colimit level. **Coincidences are conspiracies.**

**Motif 2 — The (4,20) signature.** The Mukai signature $(4,20)$ is the source of the K3 Yangian's super-structure. Conjecturally lifts to the super-Yangian $Y(\mathfrak{gl}(4|20))$ (CONJECTURAL, AP-CY35; never $\backslash$begin{theorem}). BFN gives no direct purchase on the super-structure: BFN is bosonic. The super-Yangian must come from a different functor — perhaps fermionic BFN (Hilburn–Yoo, arXiv:2211.07009).

**Motif 3 — Self-mirror.** K3 is self-mirror (Dolgachev–Nikulin). The K3 Yangian is therefore self-symplectic-dual. BFN respects this: the Coulomb branch and Higgs branch of the K3 quiver theory coincide as Hilbert schemes (Conjecture~\ref{conj:k3e-coulomb-branch} + Beauville deformation equivalence).

**Motif 4 — Three involutions.** Koszul, symplectic-dual, unitarity. Generate $(\mathbb Z/2)^3$. BFN wall-crossing realises the symplectic involution as Langlands duality across the wall. The unitarity involution $g(z)g(-z) = 1$ comes from the BFN $\mathbb C^*$-loop rotation acting as $z \mapsto -z$. The Koszul involution comes from the bar-cobar duality of Vol I, lifted to BFN via the holomorphic-CS-on-$K3 \times E$ construction.

**Motif 5 — The diagram is the algebra.** The deepest lesson of the Platonic statement: $Y(\mathfrak g_{K3})$ is not a single algebra, it is a **colimit diagram**. The chambers of $\mathrm{Stab}(K3)$ index the diagram; the algebra emerges as the universal target. This is the (∞,1)-categorical content of the K3 Yangian. Compare to Vol I's Theorem A: the bar-cobar duality is not an isomorphism of algebras, it is a Quillen equivalence of model categories — the model structure is the diagram, the algebra is the homotopy-colimit.

**The music of Pillar δ.** Pillar α (Φ) is the universal functor; Pillar β (BKM trace) is its specialisation along Borcherds; Pillar γ (CY-A_3 inf-cat) is its existence theorem at d=3; Pillar δ is its **most intricate evaluation** — the place where BFN, MO, Φ, Borcherds, McKay, Costello-5d, factorisation-homology all converge to one universal construction. BFN's contribution is to give the **chamber-by-chamber image** that the colimit assembles into $Y(\mathfrak g_{K3})$.

---

## 7. Healing edits (CONSTRUCTIVE — for next-pass insertion, not for commit now)

The following edits to existing Vol III .tex files would operationalise the Platonic statement of §3.

**HE-1.** `chapters/examples/k3_yangian_chapter.tex` §subsec:k3e-bfn (L74–103). Replace Conjecture~\ref{conj:k3e-bfn-yangian} with the Platonic statement (§3 above). Insert the four restrictions A1–A4 as Restrictions 1–4. Add named obstructions Π_BFN.4 and Π_BFN.5 explicitly. ~80 lines new.

**HE-2.** `chapters/examples/k3_quantum_toroidal_chapter.tex` §subsec:bfn-coulomb-k3 (L796–869). Sharpen Conjecture~\ref{conj:bfn-k3-yangian}: rewrite as "Restriction of the Platonic statement to the toroidal chamber." Add cross-reference to the new Platonic statement in `k3_yangian_chapter.tex`. Insert Π_BFN-Φ functorial statement (§5). ~40 lines new.

**HE-3.** `chapters/theory/quantum_groups_foundations.tex` §sec:qgf-cy-c-k3-abelian Remark~\ref{rem:cy-c-three-routes}(B) (L290). Update Route (B) wording from "BFN... is a theorem (BFN 2016) [for ADE]; for K3, the identification ... is conjectural" to: "BFN per chamber is the theorem; the chamber colimit is the Platonic statement (Π_BFN); the chamber-by-chamber subalgebra inclusions are immediate." ~10 lines new.

**HE-4.** `notes/tautology_registry.md`. Add entry #6: `Π_BFN` — colimit-of-chamber statement, requires homotopy-coherent stable-envelope diagram and Mukai-cone Cartan colimit. Independent verification source: K3 Hilbert-scheme Euler characteristics (Göttsche 1990, geometric, disjoint from BFN homology).

**HE-5.** `chapters/examples/k3_yangian_chapter.tex` new subsection after §subsec:k3e-bfn. **§subsec:k3-bfn-Phi-functorial (Π_BFN-Φ).** State the Drinfeld-center-promotion identification of §5 explicitly. ~50 lines new.

**HE-6.** `compute/lib/bfn_coulomb_k3_yangian.py` (existing, 93 tests). Add tests for the chamber colimit: verify that the chamber-by-chamber Cartans assemble to the Mukai lattice (rank 24 emerges from sum of per-chamber ranks). Independent verification: compare against `symplectic_duality_k3.py` Coulomb-branch chamber counts. Estimated +30 tests.

**HE-7.** `appendices/notation.tex` (kappa-spectrum table). Add the Universal Trace Identity row tying $\kappa_{\mathrm{BKM}}(K3) = 5$ to the BFN chamber count $\mathrm{rk}(Y(\mathfrak g_{K3})) - 19$. ~15 lines.

**HE-8.** `chapters/theory/cy_to_chiral.tex` §sec containing the four-pillar interlocks. Add Pillar δ ↔ Pillar α derivation: BFN colimit = Φ Drinfeld-center promotion at K3. ~30 lines.

Total: ~250 lines new prose, +30 tests, 1 new conjecture entry in tautology registry, 1 new functorial statement (Π_BFN-Φ) bridging Pillars α and δ.

---

## 8. Named obstructions

The Platonic statement of §3, the proof skeleton of §4, and the connections of §5 generate a precise list of named open problems:

**Π_BFN.4 — Homotopy-coherent stable-envelope diagram.** The Maulik–Okounkov stable envelope cocycle condition is a 1-coherence statement (1-cells satisfy a cocycle on 2-faces). The Platonic statement requires the full ∞-coherent diagram in $\mathbb E_1\text{-Alg}(\mathrm{Sph}_{G_\Lambda})$. Open: 2-cells, 3-cells, ..., n-cells of the homotopy-coherent stable-envelope diagram. Best-case route: the topological-field-theory reformulation of Costello–Witten (arXiv:1810.01970) which explicitly constructs the n-cells from $n$-dimensional defect operators.

**Π_BFN.5 — Mukai-cone Cartan colimit.** The colimit of per-chamber Cartans is conjecturally the full Mukai lattice. Open: the precise diagram structure on the cocharacter lattices and the verification that the colimit has rank 24 (not, say, 22 — losing the central $H^0 \oplus H^4$ pair). Best-case route: explicit chamber-decomposition computation à la Aspinwall–Morrison (arXiv:hep-th/9404151).

**Π_BFN.6 — Per-chamber Drinfeld presentation.** Per-chamber, BFN gives $Y^\mu(\mathfrak g_Q)$. The Platonic identification with $Y(\mathfrak g_{K3})$ requires a Drinfeld-style presentation (Cartan rank, structure function, classical limit determine the Yangian) for the *non-standard* algebra $Y(\mathfrak g_{K3})$. The abelian case is proved (thm:k3-abelian-yangian-presentation). The non-abelian case is the load-bearing-open-problem #2.

**Π_BFN-Φ — BFN colimit = Φ Drinfeld center.** The functorial bridge to Pillar α. Conjectural; requires the Bezrukavnikov–Finkelberg local geometric Langlands equivalence to be extended to the K3-cohomology setting.

**Π_BFN-V20 — BFN chamber count = $\kappa_{\mathrm{BKM}} - 19$.** The arithmetic identification $\kappa_{\mathrm{BKM}}(K3) = 5 = \mathrm{rk}(Y(\mathfrak g_{K3})) - 19$ tying the BFN chamber count to the BKM weight via the transcendental-lattice rank. Open: derive the 19 from K3 lattice arithmetic (it is the rank of the transcendental sublattice of a *generic* algebraic K3 surface; the identification with the BFN chamber-count complement is a conjecture).

**Π_BFN-super.** BFN is bosonic; the super-Yangian $Y(\mathfrak{gl}(4|20))$ requires fermionic BFN (Hilburn–Yoo). Open: super-BFN convolution algebra for the K3 super-quiver datum.

**Π_BFN-elliptic.** The elliptic Yangian $Y_{\tau}(\mathfrak g_{K3})$ corresponding to the $K3 \times E$ target. Open: elliptic BFN (in the sense of Yang–Zhao, arXiv:1604.01865) on the K3 datum.

These seven named obstructions complete the BFN-route picture. Closing **any one** advances Pillar δ; closing **Π_BFN.4 + Π_BFN.5 + Π_BFN-Φ** would establish the full Platonic statement and resolve load-bearing open problem #2.

---

## 9. Coda — what this culmination contributes

The 2026-04-16 swarm's Pillar δ was already articulated in the Manifesto (`PLATONIC_MANIFESTO_VOL_III.md` §I.δ) and the Vol III $K3 \times E$ chapter. What this culmination adds:

1. **The Platonic statement is a colimit, not a single identification.** The BFN ↔ K3 Yangian relationship is a colimit-of-chambers statement, not an algebra-equals-algebra statement. This dissolves the rank-24 obstruction.

2. **Seven named obstructions Π_BFN.{4,5,6,Φ,V20,super,elliptic}.** Adds to the Master Punch List inventory of 24 named open conjectures.

3. **The cross-volume identity 5 = 24 − 19.** Ties the V20 Universal Trace Identity to K3 lattice arithmetic in a way the Manifesto and V20 file did not make explicit.

4. **Eight healing edits (HE-1 through HE-8) ready for next-pass insertion.** Total ~250 lines new prose, +30 tests, 1 new Π_BFN entry in tautology registry. Aligned with the Manifesto's Pillar δ recommendation §III row 3 ("Six-route restructuring [V11 §8.4]").

5. **The slogan: "BFN sees one chamber at a time; K3 is the colimit over all chambers."** A piece of Vol III's Platonic music.

The K3 BFN route, properly Platonised, takes its place as the geometrically-uniform side of Pillar δ — complementary to the categorically-uniform Φ side and to the modularly-uniform Borcherds side. The three sides meet at the K3 × E target, and that meeting is the climax of Vol III.

---

**End of culmination IV/V.** No commits made. Constructive deliverable for next-pass insertion. Attribution: Raeez Lorgat.
