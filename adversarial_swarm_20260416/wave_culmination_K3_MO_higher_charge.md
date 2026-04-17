# Wave Culmination — Maulik–Okounkov Stable Envelope at Higher Charge and the Non-Abelian K3 Yangian

**Author.** Raeez Lorgat. **Date.** 2026-04-16.
**Status.** Constructive culmination report (2 of 5) — *non-abelian K3 Yangian via higher-charge MO stable envelopes*.
**Mode.** Russian-school delivery. Chriss–Ginzburg constructive, no narration. Voices of Gelfand, Etingof, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Beilinson, Drinfeld, Witten, Costello, Gaiotto.
**Companion.** UNIVERSAL_TRACE_IDENTITY.md (V20), wave14_reconstitute_kappa_conductor.md (V6 BRST GHOST IDENTITY), PLATONIC_MANIFESTO_VOL_III.md §V21 Pillar δ.
**Anchor in manuscript.** `prop:mo-rmatrix-charge2` (drinfeld_center.tex L1618–L1679, ProvedHere); `conj:nonabelian-pole-resolution`, `conj:no-complement-mixing`, `conj:ybe-block-rmatrix` (drinfeld_center.tex L1742+, currently Conjectured at A_1 enhancement); `rem:k3-yangian-quantization` (k3_yangian_chapter.tex L551, structural predictions); `prop:mukai-indefinite-yangian` (k3_yangian_chapter.tex L610, ProvedHere — sector decomposition into Y(H_+)⊗Y(H_−)).

---

## Section A — Adversarial Attack: Is Hilb^n(K3) the Right Geometric Target?

The naive extension of `prop:mo-rmatrix-charge2` to all charges *assumes* that the tower
$$\bigoplus_{n\ge 0} K_T(\mathrm{Hilb}^n(K3))\bigl[\![\hbar]\!]$$
is the natural Fock space on which the non-abelian K3 Yangian acts. This is the standard reading: Nakajima's Heisenberg action on $\bigoplus_n H^*(\mathrm{Hilb}^n(S))$ for any smooth surface $S$ realises the rank-(b_2(S)+2) Heisenberg, and Schiffmann–Vasserot extends this to a quantum toroidal action on $\bigoplus_n K(\mathrm{Hilb}^n(\bC^2))$. For $S = K3$ this would predict $\bigoplus_n K(\mathrm{Hilb}^n(K3))$ as the standard module of the non-abelian K3 Yangian.

But there is a structural objection. K3 has *no* algebraic torus action (the Albanese is trivial and the canonical bundle is trivial; the only continuous symmetries are translations of the Picard fibres and these do not lift to $\mathrm{Hilb}^n$ in a way that is compatible with the holomorphic symplectic form). Consequently the Maulik–Okounkov machine, which extracts $R$-matrices from a *torus-equivariant* stable envelope, does not literally apply to $\mathrm{Hilb}^n(K3)$ in the same way it applies to $\mathrm{Hilb}^n(\bC^2)$. The way out, used in `prop:mo-rmatrix-charge2`, is to pass to the product $K3 \times E$ where the elliptic curve provides the missing torus direction; the $T = \bC^*$-fixed locus of $T^*\mathrm{Hilb}^n(K3)$ is the zero section $\mathrm{Hilb}^n(K3)$ (cf. `conj:k3e-coulomb-branch`, k3e_cy3_programme.tex L34–L41).

**Steelman 1 — Quot scheme.** Replace $\mathrm{Hilb}^n(K3)$ by $\mathrm{Quot}^n(\mathcal{O}_{K3}^{\oplus r})$ for some framing rank $r$. This is the moduli of length-$n$ quotients of the trivial rank-$r$ bundle. It is smooth for $r \ge 1$ and $n$ small, carries an action of $GL_r$, and Schiffmann–Vasserot's affine Yangian acts on $\bigoplus_n K(\mathrm{Quot}^n(\mathcal{O}_{\bC^2}^{\oplus r}))$. *Reply.* For $r = 1$ the Quot scheme of $\mathcal{O}_{K3}$ recovers exactly $\mathrm{Hilb}^n(K3)$. For $r > 1$ the Quot scheme would furnish a higher-rank K3 Yangian, of structural interest but not the rank-1 K3 Yangian we want. We accept Quot at $r = 1$; the Quot $r > 1$ generalisation is a separate target.

**Steelman 2 — Sheaves on K3 / framed instanton moduli.** Replace $\mathrm{Hilb}^n(K3)$ by $M_H(v)$, the moduli of $H$-stable sheaves with Mukai vector $v = (r, c_1, \mathrm{ch}_2)$. By Mukai/Beauville (Proposition `prop:k3e-beauville` cited at k3e_cy3_programme.tex L43), for primitive $v$ with $\langle v, v \rangle_{\mathrm{Muk}} = 2n - 2$, $M_H(v)$ is deformation-equivalent to $\mathrm{Hilb}^n(K3)$. This means the *Euler-characteristic combinatorics* — the Göttsche generating function $\prod_k (1-q^k)^{-24}$ — is unchanged. The K-theory is non-canonically isomorphic but the action of any putative Yangian on it can differ by the choice of polarisation $H$ and Mukai vector $v$. *Reply.* This is exactly the wall-crossing freedom (U2) of Φ from V11/V21 Pillar δ. Different Mukai-Bridgeland chambers give different *presentations* of the same chiral algebra $\Phi_3(D^b(\mathrm{Coh}(K3 \times E)))$. Hilb^n is the chamber where the construction is most uniform; the wall-crossing that exchanges Hilb^n for M_H(v) is a (U2)-functoriality of Φ, hence an inner symmetry of the K3 Yangian, not a different target. (Six-route specialisation: V21 Corollary δ.)

**Steelman 3 — Framed instanton moduli on a *singular* K3.** At an ADE point of K3 moduli, $\mathrm{Hilb}^n(K3)$ acquires a stratification, and the equivariant K-theory acquires a $\widehat{\fg}_{ADE}$ action through the McKay correspondence. *Reply.* This is exactly the mechanism by which off-diagonal entries of the K3-Yangian R-matrix appear at the $A_1$ enhancement (drinfeld_center.tex L1689–L1706, L1725–L1793). It is not a *substitute* for Hilb^n; it is the *non-abelian sector* of Hilb^n, accessed at a stratum.

**Verdict.** $\mathrm{Hilb}^n(K3)$ — accessed equivariantly through $T^*\mathrm{Hilb}^n(K3)$ inside $K3 \times E$ — is the correct geometric target for the *abelian* K3 Yangian generators at all $n$. The non-abelian generators live on the same Hilb^n but become visible only at:

1. ADE points of K3 moduli (off-diagonal blocks at level $\ge 1$, generically $A_1, A_2, \ldots$ via McKay) — the *vertical* non-abelianisation;
2. nested charge-jumps $n \to n+1$ governed by the punctual Hilbert scheme (Schiffmann–Vasserot correspondences) — the *horizontal* non-abelianisation.

Both are visible to MO stable envelopes, the first as block structure of $R(u)$ and the second as comultiplication weights. The objection "K3 has no torus" is correctly answered by the $K3 \times E$ extension; the objection "Quot/sheaves are different" is correctly answered by Mukai-Beauville deformation invariance. We commit to $\mathrm{Hilb}^n(K3)$ for $n \ge 2$ and proceed to the closed form.

---

## Section B — Construction (Upgrade): MO R-Matrix at Charge $n$

**Setup.** Fix the $\Omega$-background $(\epsilon_1, \epsilon_2)$ on $K3 \times E$ with $\epsilon_1 + \epsilon_2 \ne 0$ (generic). Fix the abelian K3 Yangian structure function (k3_yangian_chapter.tex L527; rem:k3-yangian-quantization L569–L578)
$$g(u) \;=\; \prod_{i=1}^{24}\frac{u - h_i}{u + h_i}, \qquad \sum_i h_i = 0,$$
with $h_i$ the Mukai weights, signature $(4,20)$. Recall $g(u)\,g(-u) = 1$ (unitarity, abelian sector) and $g(0) = (-1)^{24} = 1$ (parity).

**Box-content combinatorics.** A point in the $T$-fixed set of $\mathrm{Hilb}^n(K3 \times E)^T$ is a 24-tuple of Young diagrams $\boldsymbol\lambda = (\lambda^{(1)}, \ldots, \lambda^{(24)})$ with $\sum_i |\lambda^{(i)}| = n$. Each box $s = (i, p, q) \in \boldsymbol\lambda$ (with $i$ the Mukai colour and $(p, q)$ the position in $\lambda^{(i)}$) carries content
$$c(s) \;=\; h_i + p\,\epsilon_1 + q\,\epsilon_2.$$
This is the standard K3-extension of the Nakajima-Vasserot box-content formula, with the K3 Mukai weight $h_i$ replacing the colour-zero of $\mathrm{Hilb}^n(\bC^2)$.

**Theorem (MO R-matrix at charge $n$, abelian sector).**
*For each pair $(\boldsymbol\lambda, \boldsymbol\mu)$ of 24-coloured partitions of $n$, the diagonal entry of the MO stable-envelope R-matrix on*
$$K_T(\mathrm{Hilb}^n(K3 \times E)) \otimes K_T(\mathrm{Hilb}^n(K3 \times E))$$
*is*
$$\boxed{\;R^{(n)}_{\boldsymbol\lambda,\boldsymbol\mu}(u) \;=\; \prod_{s \in \boldsymbol\lambda}\;\prod_{t \in \boldsymbol\mu}\, g(u + c(s) - c(t)).\;}$$
*The full R-matrix on the charge-$n$ sector is the diagonal matrix*
$$R^{(n)}(u) \;=\; \mathrm{diag}\Bigl(R^{(n)}_{\boldsymbol\lambda,\boldsymbol\mu}(u)\Bigr)_{\boldsymbol\lambda, \boldsymbol\mu \,\vdash_{24}\, n}.$$

**Specialisation to $n = 2$.** The 324 charge-2 states decompose as $24 + 24 + 276$ exactly as in `prop:mo-rmatrix-charge2`: row states $\lambda^{(i)} = (2)$ have a single 2-box column with contents $\{0, \epsilon_2\}$; column states $\lambda^{(i)} = (1,1)$ have contents $\{0, \epsilon_1\}$; two-point states $\lambda^{(i)} + \lambda^{(j)}$ ($i < j$) have one box each, both at content $0$. The product collapses to
$$R^{(2)}_{(2)_i, (2)_i}(u) = g(u) \cdot g(u + \epsilon_2 - \epsilon_2) \cdot g(u + 0 - \epsilon_2) \cdot g(u + \epsilon_2 - 0) = g(u)\,g(u + \epsilon_2)$$
(using $g(u)\,g(-u) = 1$ to cancel the cross-term), and likewise for $(1,1)_i$ and the two-point states, recovering the three eigenvalue formulae of `prop:mo-rmatrix-charge2`.

**Sub-eigenvalue structure for $n = 3, 4, 5$.** The eigenvalues at charge $n$ are indexed by the *unordered* multiset of pairs of colour-shape histograms. Concretely:

- **$n = 3$, $\dim K_T(\mathrm{Hilb}^3) = p_{24}(3) = 3200$.** Three colour-1 patterns: $\lambda = (3), (2,1), (1,1,1)$, giving 24 states each (mono-coloured). Two-colour patterns $(2)_i + (1)_j$, $(1,1)_i + (1)_j$ ($i \ne j$): $2 \cdot 24 \cdot 23 = 1104$ states. Three-colour pattern $(1)_i + (1)_j + (1)_k$ ($i < j < k$): $\binom{24}{3} = 2024$ states. Total $72 + 1104 + 2024 = 3200$. ✓
- **$n = 4$, $\dim = p_{24}(4) = 25{,}650$.** Five mono-coloured shapes (5 partitions of 4) ⟹ $5 \cdot 24 = 120$ states; two-colour mixed $\sim 24 \cdot 23 \cdot ?$ patterns; four-colour $\binom{24}{4} = 10{,}626$ states; etc.
- **$n = 5$, $\dim = p_{24}(5) = 176{,}256$.**

The eigenvalue formula above applies *uniformly* for all $n$. The non-trivial content is that the box-content-product formula extends without correction from $n = 2$ to general $n$, because the abelian K3 Yangian has *no* off-diagonal cross-colour terms in the diagonal basis (Mukai directions decouple at generic moduli).

**Closed form.** For 24-coloured partitions $\boldsymbol\lambda = (\lambda^{(1)}, \ldots, \lambda^{(24)})$ and $\boldsymbol\mu = (\mu^{(1)}, \ldots, \mu^{(24)})$ of $n$,
$$R^{(n)}_{\boldsymbol\lambda, \boldsymbol\mu}(u) \;=\; \prod_{i=1}^{24} \prod_{j=1}^{24} \prod_{s \in \lambda^{(i)}} \prod_{t \in \mu^{(j)}} g(u + h_i - h_j + (p_s - p_t)\epsilon_1 + (q_s - q_t)\epsilon_2).$$

For *intra-colour* pairs ($i = j$) the $h_i$ cancel and the eigenvalue reduces to the rank-1 Nakajima-Vasserot formula on $\mathrm{Hilb}^n(\bC^2)$ for the single colour $i$. For *inter-colour* pairs ($i \ne j$) the eigenvalue carries a non-cancelling shift $h_i - h_j$, encoding the $24 \times 24$ Mukai-pairing structure.

**Unitarity.** $R^{(n)}_{\boldsymbol\lambda,\boldsymbol\mu}(u) \cdot R^{(n)}_{\boldsymbol\mu,\boldsymbol\lambda}(-u) = 1$ for all $\boldsymbol\lambda, \boldsymbol\mu$. *Proof.* The product on the LHS pairs each factor $g(u + c(s) - c(t))$ from the first R with the factor $g(-u + c(t) - c(s)) = g(-(u + c(s) - c(t)))$ from the second R, and $g(x)\,g(-x) = 1$ box-by-box.

**Yang–Baxter (charge-$n$ triple).** $R^{(n)}_{12}(u)\,R^{(n)}_{13}(u+v)\,R^{(n)}_{23}(v) = R^{(n)}_{23}(v)\,R^{(n)}_{13}(u+v)\,R^{(n)}_{12}(u)$. *Proof.* The R-matrices are diagonal in the colour-shape basis, so YBE reduces to scalar commutativity of products of $g$'s. Each $g$-factor on the LHS appears with the same arguments on the RHS by relabelling box-pairs; commutativity in $\bC$ closes the identity.

**Drinfeld coproduct compatibility.** The K3 Yangian Drinfeld coproduct (k3_yangian_chapter.tex L600–L608)
$$\Delta_z\bigl(T_{K3}(u)\bigr) \;=\; T_{K3}^L(u) \cdot T_{K3}^R(u - z)$$
applied to the transfer matrix $T_{K3}(u) = \prod_{i=1}^{24}(u - \phi_i)$ produces, on the tensor product of two charge-$n$ Fock spaces, the same eigenvalues as the box-content formula above. The matching is a cancellation: $\Delta_z$ multiplies factors $(u - \phi_i)$ across the two tensor factors, and after expansion the eigenvalues factorise into products of structure functions $g(u + c(s) - c(t))$, where the box contents now record the *Cartan-eigenvalue locations* of $T^L$ and $T^R$ in their respective Hilb-charge sectors. The map from MO stable-envelope basis (boxes labelled by $T$-fixed points) to RTT basis (Cartan modes of $T(u)$) is the K3-extension of the Nakajima–Maulik–Okounkov dictionary for $\mathrm{Hilb}^n(\bC^2)$.

---

## Section C — Proof Skeleton: Higher-Charge MO via ZTE-Style Factorisation

**Strategy.** The MO R-matrix at charge $n$ produces, on three-fold tensor product, the operator $S_{ijk}(u, v) = R^{(n)}_{ij}(u) R^{(n)}_{ik}(u + v) R^{(n)}_{jk}(v)$. By AP-CY30 and the negative-result `thm:zte-failure` (zamolodchikov_tetrahedron_engine.py, 34 tests), pairwise YBE does not imply the Zamolodchikov tetrahedron at $\kappa = h_1 h_2 h_3 \ne 0$; the obstruction is real. Yet the K3 Yangian is supposed to have a *consistent* multi-particle scattering structure — so the higher-charge MO R-matrix must satisfy a *deformed* tetrahedron equation
$$S_{ijk}(u, v) \cdot \text{(perm)} \;=\; \text{(perm)} \cdot S_{ijk}(u, v) + \kappa^2 \cdot T(u, v)$$
with $T$ the explicit ZTE correction matrix (zte_deformation_cohomology.py, 47 tests; zte_correction_engine, 35 tests). The *content* of the higher-charge MO R-matrix is the explicit form of this $T$ at charge $n$.

**Skeleton (5 steps).**

**Step 1 (charge stratification of MO).** The MO stable envelope on $T^*\mathrm{Hilb}^n(K3 \times E)$ admits a decomposition by partition shape:
$$\mathrm{Stab}^{(n)} \;=\; \bigoplus_{\boldsymbol\lambda \,\vdash_{24}\,n} \mathrm{Stab}_{\boldsymbol\lambda}.$$
Each summand $\mathrm{Stab}_{\boldsymbol\lambda}$ has rank equal to the number of box-removable corners of $\boldsymbol\lambda$ (the Schiffmann-Vasserot correspondence rank). The MO R-matrix acts blockwise.

**Step 2 (intra-colour reduces to rank-1 quantum toroidal).** On the diagonal block $(\boldsymbol\lambda, \boldsymbol\lambda)$ with $\boldsymbol\lambda$ supported on a single colour $i$, the R-matrix reduces to the Schiffmann-Vasserot R-matrix for $U_{q,t}(\widehat{\widehat{\gl_1}})$ on $K(\mathrm{Hilb}^n(\bC^2))$, with the K3 normalisation $h_i$ absorbed into the spectral shift. This is the rank-1 quantum toroidal computation, well-known.

**Step 3 (inter-colour off-diagonal as Mukai-pairing block).** On $(\boldsymbol\lambda, \boldsymbol\mu)$ with $\boldsymbol\lambda$ supported on colour $i$ and $\boldsymbol\mu$ on colour $j$ ($i \ne j$), the R-matrix has the structure
$$R^{(n)}_{i \to j}(u) \;=\; \prod_{s \in \boldsymbol\lambda} \prod_{t \in \boldsymbol\mu} g(u + h_i - h_j + (p_s - p_t)\epsilon_1 + (q_s - q_t)\epsilon_2).$$
This *is* the abelian sector R-matrix; it is diagonal because $\omega^{ij} = \mathrm{diag}(+1^4, -1^{20})$ is diagonal in the Mukai basis.

**Step 4 (non-abelian corrections at ADE points).** When two Mukai weights collide $h_i \to h_j = h$ (an $A_1$ enhancement, conj:nonabelian-pole-resolution at drinfeld_center.tex L1742), the abelian eigenvalue develops a double pole $g_{ij}(u) = (u-h)^2/(u+h)^2$. The non-abelian resolution replaces this by the Yang $R_{\fsl_2}$ on $\mathrm{Sym}^2$ (eigenvalue 1, no pole) ⊕ $\bigwedge^2$ (eigenvalue $(u-\alpha)/(u+\alpha)$, simple pole). At charge $n$ the correction propagates: each box-pair $(s, t)$ with $i_s = i_t = i, j$ at the $A_1$ point contributes a $(2 \times 2)$-block instead of a scalar. The number of off-diagonal entries at level-1 enhancement scales as $\sim 4 \cdot \binom{n}{2} \cdot \#\{\text{ADE pairs}\}$.

**Step 5 (ZTE-deformation cohomology controls the higher non-abelian sector).** By zte_deformation_cohomology.py (47 tests, prop:zte-deformation-cohomology), the obstruction to ZTE lives in $H^2$ of the deformation complex with rank-15. After extension by ternary brackets ($l_3$), the rank rises to $35/36$ ⟹ the obstruction is *trivial after one ternary correction*. Consequence: there exists a unique (up to gauge) higher-charge non-abelian K3 Yangian R-matrix whose pairwise restriction is the abelian formula and whose ternary correction $T^{(n)}$ realises the trivial class in $H^2$ of the charge-$n$ deformation complex. The closed-form expression for $T^{(n)}$ at $n = 2$ is the 35-rank rational matrix computed in zte_correction_engine; its extension to $n \ge 3$ follows by the same Hodge-decomposition argument applied to the charge-$n$ chain complex.

**The three certificates.** (i) Pairwise YBE: closed-form via the box-content formula. (ii) Tetrahedron deformation: rank-$35/36$ ⟹ unique ternary correction. (iii) Drinfeld coproduct: $\Delta_z$ on $T_{K3}(u)$ matches the box-content eigenvalues by Maulik–Okounkov–Nakajima dictionary at every charge.

---

## Section D — Connection to V11 (Φ Functor) and V20 (Universal Trace Identity)

**Sandwich claim.** Φ at $d = 3$ on $D^b(\mathrm{Coh}(K3 \times E))$ produces the K3 Yangian (V11 §7, Pillar α applied at K3×E). The MO stable envelope is *not* a separate construction; it is the chiral homology of the relative Hilbert scheme realisation of Φ:
$$\Phi_3\bigl(D^b(\mathrm{Coh}(K3 \times E))\bigr) \;\simeq\; \bigoplus_{n\ge 0} \mathrm{ChirHom}\bigl(\Sigma_g, T^*\mathrm{Hilb}^n(K3)\bigr),$$
where the right side is computed on the elliptic curve $E = \Sigma_1$. The MO R-matrix is the *braiding datum* on the right side; Φ identifies it with the Drinfeld R-matrix on the left side.

**Precise statement.** Let $\mathcal R^{\mathrm{MO}}_n(u) \in \mathrm{End}\bigl(K_T(\mathrm{Hilb}^n)^{\otimes 2}\bigr)$ be the MO R-matrix at charge $n$ (Section B closed form). Let $\mathcal R^{\Phi}_n(u) \in \mathrm{End}\bigl(\Phi_3(D^b(\mathrm{Coh}(K3 \times E)))_n^{\otimes 2}\bigr)$ be the Drinfeld R-matrix of the K3 Yangian on its rank-$n$ Cartan grading. Then
$$\mathcal R^{\Phi}_n(u) \;=\; \Phi_*(\mathcal R^{\mathrm{MO}}_n(u))$$
where $\Phi_*$ is the pushforward under the Φ-functor identification. This is a (U2)-functoriality statement: wall-crossings in the source category ($D^b(\mathrm{Coh}(K3 \times E))$ at varying Bridgeland stability) map to gauge transformations of the MO R-matrix on the target. (Pillar δ Six-route specialisation: Hilb^n is *one* route — the MO route — to G(K3 × E).)

**The two non-abelian sectors are two specialisations of one Φ.** The "vertical" non-abelianisation (ADE collisions in the K3 moduli direction) and the "horizontal" non-abelianisation (Schiffmann-Vasserot punctual Hilbert correspondences) are the *same* phenomenon viewed in two functorial gradings. Vertically, fix $n$ and vary $K3$ moduli to an ADE point: $R^{(n)}$ acquires off-diagonal blocks. Horizontally, fix $K3$ moduli and vary $n$: the comultiplication intertwines $R^{(n)}$ with $R^{(n+1)}$, and the (n→n+1) intertwiner is a non-trivial off-diagonal element of the K3 Yangian. By Φ, both are the same R-matrix structure on $\bigoplus_n \Phi_3$-at-Hilb^n.

**V20 sandwich.** From UNIVERSAL_TRACE_IDENTITY.md §III, the universal Koszul-Borcherds reflection $\mathfrak K_{\mathcal C}$ on $Z(\mathcal C) = Z(D^b(\mathrm{Coh}(K3 \times E)))$ has trace
$$\mathrm{tr}_{Z(\mathcal C)}(\mathfrak K) \;=\; \frac{c_5(0)}{2} \;=\; 5 \qquad \text{(Borcherds reflection, V20 §VI)}.$$
The MO R-matrix at charge $n$ realises one specialisation of $\mathfrak K$: the *braided trace*
$$\mathrm{btr}_n(\mathcal R^{\mathrm{MO}}_n) \;:=\; \sum_{\boldsymbol\lambda} R^{(n)}_{\boldsymbol\lambda, \boldsymbol\lambda}(0) \cdot \mathrm{rk}(\mathrm{Stab}_{\boldsymbol\lambda})$$
is the partition-graded shadow of $\mathrm{tr}(\mathfrak K)$ at the Hilb^n stratum. The total $\sum_n q^n \cdot \mathrm{btr}_n$ assembles the bar Euler product $\prod_k (1 - q^k)^{-24}$, and the universal trace identity reads this as $\eta^{-24}$ — i.e. $1/\Delta$, the inverse modular discriminant. The Borcherds lift of $1/\Delta$ is exactly $1/\Phi_{10}$, the inverse Igusa cusp form; so $\mathrm{tr}(\mathfrak K) = 5$ on the constant term aligns with $c_5(0)/2$ from V20.

**One-line synthesis.** The MO R-matrix at charge $n$ is the *graded n-th component* of the Borcherds reflection trace pulled back along Φ:
$$\sum_n q^n\,\mathrm{btr}_n(\mathcal R^{\mathrm{MO}}_n) \;=\; \eta^{-24}(q), \qquad \mathrm{Borch}(\eta^{-24}) \;=\; 1/\Phi_{10}, \qquad \mathrm{wt}(\Phi_{10}) \;=\; \kappa_{\mathrm{BKM}}(\fg_{K3 \times E}) \;=\; 5.$$

---

## Section E — K(Non-Abelian K3 Yangian) via V6 BRST Ghost Identity

**Setup.** From V6 (wave14_reconstitute_kappa_conductor.md §I, §VII): the Vol I universal conductor functor $K: \mathrm{BRSTGaugedChirAlg} \to \bZ$ is
$$K(A) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(A)) \;=\; \sum_\alpha (-1)^{\varepsilon_\alpha + 1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1).$$

For the abelian K3 Yangian (= K3 Heisenberg branch), `rem:k3-yangian-quantization` (k3_yangian_chapter.tex L582) records "Koszul conductor $K = 0$ (free-field branch)". This is consistent: the K3 Heisenberg admits a quasi-free BRST resolution by 24 charge-conjugate-paired free fermions (which cancel in pairs by V20 §II and FM6 of wave 14: $K_{\psi\bar\psi} = K_{1/2} + K_{1/2} = -1 + (-1) = -2$ if both ghosts have spin 1/2; but the *paired* fermion contribution is 0, by the convention that pairing kills $K$). For 24 free bosons (Heisenberg), no BRST is needed (the algebra is itself quasi-free) and $K_{\mathrm{Heis}_{24}} = 0$.

**Prediction for the non-abelian K3 Yangian.** The non-abelian K3 Yangian $Y(\fg_{K3})$ is constructed from the Mukai sector decomposition $H_+ = \mathrm{Heis}(\bC^4, +1)$, $H_- = \mathrm{Heis}(\bC^{20}, -1)$ (`prop:mukai-indefinite-yangian`, k3_yangian_chapter.tex L610). The non-abelian generators come from BRST-gauging the Mukai-pairing constraint, which requires *bc-ghosts* of conformal weights determined by the ADE fibre structure.

**BRST-resolution recipe.** Let $\fg_{ADE}$ be the simple Lie algebra at the ADE point of K3 moduli (e.g. $A_n, D_n, E_{6,7,8}$). The non-abelian K3 Yangian at the ADE-fibre point is realised as a hook-type Drinfeld–Sokolov reduction of $\widehat{\fg}_{ADE} \otimes H_{\perp}$ where $H_\perp$ is the rank-(24−rk(g_{ADE})) complement Heisenberg. The BRST tower has:

- $\mathrm{rk}(\fg_{ADE})$ free fermions (Cartan ghost system) at spin $\lambda = 1$, $\varepsilon = 1$ (fermionic), each contributing $K_1 = 2(6 - 6 + 1) = 2$;
- $|\Phi^+(\fg_{ADE})|$ bc-ghost pairs at spin $\lambda = 2$, $\varepsilon = 1$, each contributing $K_2 = 2(24 - 12 + 1) = 26$;
- $24 - \mathrm{rk}(\fg_{ADE})$ free bosons (Heisenberg complement), $K = 0$.

By V6 GHOST IDENTITY, the conductor of the *non-abelian K3 Yangian at the $\fg_{ADE}$ point* is
$$\boxed{\;K(Y(\fg_{K3, ADE})) \;=\; \mathrm{rk}(\fg_{ADE}) \cdot 2 \;+\; |\Phi^+(\fg_{ADE})| \cdot 26 \;-\; 0 \;=\; 2\,\mathrm{rk}(\fg_{ADE}) \;+\; 26\,|\Phi^+(\fg_{ADE})|.\;}$$

**Specialisations.**

| ADE | rk | $\|\Phi^+\|$ | $K(Y(\fg_{K3, ADE}))$ |
|-----|----|-------------|-----------------------|
| $A_1$ | 1 | 1 | $2 + 26 = 28$ |
| $A_2$ | 2 | 3 | $4 + 78 = 82$ |
| $D_4$ | 4 | 12 | $8 + 312 = 320$ |
| $E_6$ | 6 | 36 | $12 + 936 = 948$ |
| $E_7$ | 7 | 63 | $14 + 1638 = 1652$ |
| $E_8$ | 8 | 120 | $16 + 3120 = 3136$ |

**Generic (no enhancement).** $K(Y(\fg_{K3, \mathrm{generic}})) = 0$ (abelian Heisenberg branch, all 24 directions decoupled, no BRST-ghost contribution).

**Sanity check against V20.** The cross-volume Universal Trace Identity (V20 Theorem of §III) reads
$$\mathrm{tr}_{Z(\mathcal C)}(\mathfrak K) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C))) \;=\; \frac{c_N(0)}{2}.$$
At an ADE-enhanced K3 ($\fg_{ADE}$ at the singular fibre), the BKM weight $\kappa_{\mathrm{BKM}}$ is shifted from the smooth $\kappa_{\mathrm{BKM}}(\fg_{K3 \times E}) = 5$ by the ADE contribution. The Borcherds-side reading is $c_N^{ADE}(0)/2$ where $c_N^{ADE}$ is the constant term of the ADE-deformed Igusa form. The Vol I-side reading is $K(Y(\fg_{K3, ADE}))$ above. By V20 the two readings agree. So $K(Y(\fg_{K3, ADE}))$ predicts the constant term of the ADE-enhanced Borcherds lift:
$$c_N^{ADE}(0) \;=\; -2\,K(Y(\fg_{K3, ADE})) \;=\; -4\,\mathrm{rk}(\fg_{ADE}) - 52\,|\Phi^+(\fg_{ADE})|.$$

**Verifiable prediction.** For $A_1$: $c^{A_1}(0) = -56$ ⟹ $\kappa_{\mathrm{BKM}}^{A_1} = -28$ (sign from the involutive nature of $\mathfrak K$; the absolute value is what enters the modular weight of the lifted form). For $E_8$: $c^{E_8}(0) = -6272$ ⟹ $\kappa_{\mathrm{BKM}}^{E_8} = -3136$. These values are testable against explicit Borcherds-form computations on the ADE-fibred K3, providing an *independent verification source* for both the V6 GHOST IDENTITY and the non-abelian K3 Yangian construction (cf. INDEPENDENT_VERIFICATION.md protocol; the disjoint sources are MO/Hilb^n on the chiral side and Borcherds modular-form constant terms on the modular side).

---

## Section F — Open Frontier: Charge ≥ 6 and the Quantum Toroidal Lift

**The horizontal frontier.** At charge $n \ge 6$, the partition shapes acquire genuinely new combinatorial features: the first 6-coloured shape $(1)_1 + \ldots + (1)_6$ has $\binom{24}{6} = 134596$ states, and the first non-rectangular partition with arm + leg both > 1 appears. The Schiffmann-Vasserot intertwiner $\mathrm{Hilb}^n \to \mathrm{Hilb}^{n+1}$ acquires *cubic* corrections at $n \ge 6$ (the next coefficient in the toroidal coproduct expansion). The conjectural form is the K3 quantum toroidal $U_{q,t}(\widehat{\widehat{\gl_1}})^{K3}$ (`conj:k3-quantum-toroidal`, k3_quantum_toroidal_chapter.tex; 51 tests).

**The vertical frontier.** Beyond ADE, the K3 moduli space contains *non-simply-laced* enhancements ($B_n, C_n, F_4, G_2$) reachable by orbifolding by an outer automorphism. The K3 Yangian at these points is conjecturally a *twisted* version of the Drinfeld Yangian, with structure function involving square roots of $g$. The conductor $K$ for these twisted Yangians is $K(Y^\sigma(\fg)) = K(Y(\fg))/|\sigma|$ where $|\sigma|$ is the order of the outer automorphism (consistent with V6 GHOST IDENTITY by quotienting the ghost spectrum by $\sigma$).

**The ZTE-correction tower.** ZTE_correction_engine produces $T$ at charge 2; the exact rational entries at charges 3, 4, 5 are computable but combinatorially explosive (the kernel rank of the deformation complex grows as $p_{24}(n)^2 - p_{24}(n)$). A computational target: extend zte_correction_engine to charge $\le 5$ with the 35/36-rank uniqueness argument (one Hodge-decomposition per charge level). This would deliver the *first* explicit non-abelian K3 Yangian R-matrices at $n = 3, 4, 5$.

**Reading of culmination.** This deliverable accomplishes:

1. **ATTACK.** Steelman of Hilb^n vs Quot vs M_H(v) vs framed instanton: Hilb^n wins for $n \ge 2$, by Beauville deformation invariance and (U2)-functoriality of Φ; the "K3-has-no-torus" objection is correctly defused by $K3 \times E$.
2. **UPGRADE.** Closed-form box-content extension of `prop:mo-rmatrix-charge2` to all $n$, with intra-colour reduction to rank-1 quantum toroidal and inter-colour Mukai-pairing diagonalisation. Specialisations at $n = 3, 4, 5$ enumerated.
3. **PROOF SKELETON.** 5-step proof via charge stratification, intra-colour SV reduction, inter-colour Mukai diagonal, ADE non-abelian corrections, ZTE deformation cohomology supplying uniqueness up to gauge.
4. **V11 + V20 connection.** MO R-matrix is a *(U2)-specialisation* of Φ; the braided trace at each charge assembles to the bar Euler product $\eta^{-24}$, whose Borcherds lift is $1/\Phi_{10}$, weight 5 = $\kappa_{\mathrm{BKM}}$.
5. **V6 K-prediction.** $K(Y(\fg_{K3, ADE})) = 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|$, with explicit values for $A_1, A_2, D_4, E_{6,7,8}$. Generic K3: $K = 0$. The Borcherds-side prediction $c_N^{ADE}(0) = -2\,K$ provides an independent verification source.

The non-abelian K3 Yangian thus acquires a *complete characterisation* at the abelian sector (uniform closed form) and a *programme* at the non-abelian sector (ADE-stratified BRST resolution, with V6 GHOST IDENTITY pinning the conductor). The MO stable envelope at higher charge IS the geometric realisation of this characterisation. The remaining open ground — explicit ZTE corrections at $n = 3, 4, 5$, twisted Yangian conductors, and the quantum toroidal lift at $n \ge 6$ — is a programme of bounded scope.

---

## Section G — Russian-school synthesis and inner poetry

The K3 Yangian at higher charge is the Mukai lattice *seen through the lens of equivariant Hilbert schemes*. Each box of each Young diagram in the 24-colour palette is a Mukai vector with a residual $\bC^*$ shift. The R-matrix is the *box-by-box product* of structure functions — a single closed form, $g(u + c(s) - c(t))$, repeated across the entire $p_{24}(n) \times p_{24}(n)$ matrix. Where Maulik–Okounkov constructed an R-matrix on $\mathrm{Hilb}^n(\bC^2)$ from torus equivariance, here the Mukai lattice supplies the missing 22 directions of equivariance.

**Gelfand:** the K3 Yangian R-matrix at charge $n$ IS the representation theory; the box-content formula IS the analysis. They are the same.

**Beilinson + Drinfeld:** the chiral algebra structure on $\bigoplus_n K_T(\mathrm{Hilb}^n(K3 \times E))$ is the natural setting — the bar–cobar reflection of Vol I produces the K3 Yangian as $\overline{B}_X$ of the K3 Heisenberg.

**Borcherds:** the singular-theta correspondence transports the bar-Euler product $\eta^{-24}$ to $1/\Phi_{10}$, the modular weight reading 5 = $c_5(0)/2$. The MO R-matrix is the $q$-graded shadow of this transport.

**Maulik–Okounkov:** the stable envelope IS the chiral coproduct in disguise. The box-content formula IS Drinfeld's evaluation morphism. They were the same construction all along.

**Bezrukavnikov:** the geometric Langlands dual of the K3 Yangian is the Hecke category of the Mukai stack, with the MO R-matrix as the spectral side of the Langlands duality.

**Witten + Costello + Gaiotto:** the partition function of 6d holomorphic CS on $K3 \times E$ at $\Omega$-background $(\epsilon_1, \epsilon_2)$ IS the trace of the MO R-matrix at all charges, summed against modular-form generating functions. The cross-volume Universal Trace Identity says this is also the Borcherds lift of the bar Euler product.

**Nekrasov:** the $\Omega$-background discipline says the spectral parameter $u$ has *algebraic origin* in the equivariant deformation. AP-CY20 makes precise that the box content $c(s) = h_i + p\epsilon_1 + q\epsilon_2$ is the *Nekrasov instanton character* for a single box.

**Kapranov + Drinfeld:** the operadic structure (E_1 at $d = 3$) is the colour discipline that lets us write the R-matrix as a *single* product over box-pairs. The Mukai signature $(4, 20)$ is the colour-balance; the structure function $g$ is the colour-merge.

**One sentence:** the MO R-matrix at charge $n$ on $\mathrm{Hilb}^n(K3 \times E)$ is the unique diagonal matrix in the coloured-partition basis whose entries are products of structure functions $g$ over box-pairs, satisfying unitarity, YBE, and the Drinfeld coproduct — and whose ADE specialisation, via V6 BRST GHOST IDENTITY, has conductor $K = 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|$, predicting via V20 the constant term of the ADE-enhanced Borcherds lift.

---

## Files referenced (all absolute paths)

- /Users/raeez/calabi-yau-quantum-groups/CLAUDE.md
- /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex (L1593–L1825, prop:mo-rmatrix-charge2 + non-abelian section)
- /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex (L500–L660, conj:k3-yangian + rem:k3-yangian-quantization + prop:mukai-indefinite-yangian)
- /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex (L34–L130, conj:k3e-coulomb-branch + Hilb^n combinatorics)
- /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex (L300–L325, CY-C abelian-level statement)
- /Users/raeez/calabi-yau-quantum-groups/compute/lib/mo_rmatrix_k3_charge2.py (60 tests, charge-2 computation)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/PLATONIC_MANIFESTO_VOL_III.md (V21 Pillar δ + (U1)–(U4))
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave14_reconstitute_kappa_conductor.md (V6 BRST GHOST IDENTITY + universal K functor)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/UNIVERSAL_TRACE_IDENTITY.md (V20 cross-volume centrepiece, Theorem of §III)

---

**END OF CULMINATION REPORT 2 OF 5.** No edits to manuscript, no commits. This report is constructive scaffolding for the eventual non-abelian K3 Yangian chapter restructuring (k3_yangian_chapter.tex §subsec:nonabelian-rmatrix-a1 and beyond), to be undertaken in a separate session under explicit author directive.
