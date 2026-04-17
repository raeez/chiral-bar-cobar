# Volume I — Platonic Reconstitution
## Modular Koszul Duality

Volume I is the seed. Its subject is the bar complex of a chiral algebra on a smooth curve, the Koszul duality between algebra and cooperad that the bar mediates, and the modular curvature that obstructs flatness at positive genus. The five master theorems below are stated at their strongest honest form; all scope qualifiers are intrinsic, none imposed by technical malpractice.

---

## 1. The Five Master Theorems

**Theorem A (Bar–Cobar as (∞,2)-Categorical Properad Equivalence).**
In the Francis–Gaitsgory factorization ambient on $\mathrm{Ran}(X)$, the bar and cobar functors
$$
\overline{B}^{\,\mathrm{ch}}_X \;:\; \mathrm{Fact}^{\mathrm{aug}}(X) \;\rightleftarrows\; \mathrm{CoFact}^{\mathrm{conil},\mathrm{comp}}(X) \;:\; \Omega^{\mathrm{ch}}_X
$$
form an adjoint $(\infty,2)$-equivalence on the conilpotent-complete locus. The equivalence lifts to factorization *properads* (multi-input/multi-output operations) and restricts at the pole-free point to the classical Loday–Vallette pair $(\mathrm{Ass},\mathrm{Ass}^{!})$. The ordered bar and $\Sigma_n$-coinvariant bar are related by $R$-matrix twisted descent along the Ran-torsor $\mathrm{Ran}^{\mathrm{ord}}(X)\to\mathrm{Ran}(X)$, with Yang–Baxter guaranteeing codimension-two compatibility.

**Theorem B (Universal Bar–Cobar Inversion).**
On the Koszul locus — the full subcategory of chirally Koszul conilpotent-complete factorization algebras — the counit $\Omega^{\mathrm{ch}}\overline{B}^{\,\mathrm{ch}}(A)\to A$ is a weak equivalence for every family in the standard landscape: affine Kac–Moody at every level (including critical and admissible), Virasoro at every central charge (including minimal models), $W_N$-algebras, Heisenberg and lattice vertex algebras, all Drinfeld–Sokolov reductions, and Yangian-type ordered examples. The proof is uniform in a single Positselski curved pro-category, with critical level and minimal-model loci handled by Arakawa $C_2$-cofiniteness and admissible level by Adamović conilpotent completion.

**Theorem C (Shifted-Symplectic Lagrangian Complementarity on $\overline{\mathcal{M}}_{g,n}$).**
The total bar datum $(A,A^{!})$ of a Koszul pair is a global Lagrangian section of a $-(3g-3)$-shifted symplectic structure on the modular stack $\overline{\mathcal{M}}_{g,n}^{\,\mathrm{family}}$. Per-genus Lagrangian complementarity $Q_g(A)\oplus Q_g(A^{!})\simeq \mathrm{T}^{*}[-1]\overline{\mathcal{M}}_{g,n}$ coheres across clutching strata via the modular cooperad structure; the pair is a PTVV Lagrangian on the total stack, not merely stratum-by-stratum.

**Theorem D (Universal Arakelov Curvature).**
The chiral curvature $d_{\overline{B}}^{\,2}=\kappa\cdot\omega_g$ refines to a universal tensor-valued class
$$
\boldsymbol{\kappa} \;\in\; H^{2}\bigl(\overline{\mathcal{M}}_{g,n}^{\,\mathrm{family}},\;\mathrm{Sym}^{2}(\mathcal{F}) \otimes \Omega^{2}\bigr),
$$
whose scalarization recovers $\kappa\cdot\omega_g$ on the uniform-weight locus and whose tensor form captures cross-channel $\delta F_g^{\mathrm{cross}}$ data in the all-weight regime. Per-family specializations ($\mathrm{Heis}_k$: $\kappa=k$; $V_k(\mathfrak{g})$: $\kappa=\dim(\mathfrak{g})(k+h^{\vee})/(2h^{\vee})$; $\mathrm{Vir}_c$: $\kappa=c/2$; $W_N$: $\kappa=c(H_N-1)$) arise by pullback. A tensorial chiral Grothendieck–Riemann–Roch formula replaces the scalar Mumford identity.

**Theorem H (Hochschild Concentration via Chiral Higher Deligne).**
The chiral Hochschild complex $\mathrm{ChirHoch}^{\bullet}(A,A)$ carries a universal $E_3$-action via the Swiss-cheese presentations. Concentration in degrees $\{0,1,2\}$ is a *consequence* of $E_3$-rigidity at a point: the brace structure is the $E_2$-Gerstenhaber shadow, and the $E_3$-lift fixes the higher cohomology. At critical level, $\mathrm{ChirHoch}^{0}$ becomes the Feigin–Frenkel center (polynomial on opers) as a canonical companion statement, not an exclusion.

---

## 2. Infinite Fingerprint Classification

The invariant of a chirally Koszul algebra $A$ is the canonical fingerprint
$$
\varphi(A) \;=\; (p_{\max},\; r_{\max},\; \chi_{\mathrm{VOA}},\; n_{\mathrm{strong}},\; \mathrm{coset}),
$$
consisting of the OPE pole order, the shadow depth, the graded Euler character (detecting $\mathbb{Z}/2$-grading), the minimal strong-generator count, and the isomorphism class of the commutant pair. The four-class stratification G/L/C/M is the coarse projection $\Pi_{\mathrm{coarse}}\circ\varphi$ onto the $r_{\max}$ coordinate restricted to $\kappa\neq 0$. At $\kappa=0$, the canonical companion class **FF** (Feigin–Frenkel regime: critical-level Kac–Moody, Virasoro at $c=0$) completes the stratification with explicit infinite-dimensional shadow structure governed by the affine opers. The symplectic boson and symplectic fermion separate by $\chi_{\mathrm{VOA}}$ sign and coset type (symplectic vs orthosymplectic), resolving the apparent class collision. Pole order and shadow depth are *independent* coordinates, with witnesses at every combination.

---

## 3. Strictification

Complete strictification of the spectral Drinfeld associator to a strict dg-bialgebra is proved for every finite-dimensional simple Lie algebra: the root-multiplicity-one condition on the path sector combines with Jacobi collapse on star sectors to make all higher coherences redundant. For Kac–Moody and Borcherds–Kac–Moody algebras with imaginary roots of multiplicity greater than one, the strictification extends conjecturally via a Borcherds superalgebra framework that absorbs imaginary-root multiplicities into a super-Lie extension; Jacobi collapse at the super-level replaces the finite-simple argument, and the conjecture subsumes the monster Lie algebra case.

---

## 4. Three Derived Categories, Uniform

Volume I organizes its homological content through three canonical derived categories, each adapted to a regime of the modular tower:

- **$\mathcal{D}$ (genus zero).** Standard derived category of conilpotent factorization coalgebras on $X$; flat bar differential; Koszul duality manifestly Quillen.
- **$\mathcal{D}^{\mathrm{co}}$ (curved, genus $\geq 1$).** Positselski coderived category with curvature datum $\kappa\cdot\omega_g$; objects are curved bar coalgebras; Theorem D lives here; the universal $\boldsymbol{\kappa}$ class is the curvature of the tautological family.
- **$\mathcal{D}^{\mathrm{filt}}$ (modular bootstrap).** Filtered derived category with filtration by stable-graph depth on $\overline{\mathcal{M}}_{g,n}$; modular-bootstrap vanishing $H^{2}=0$ lives here; curved-Dunn twisting-cochain complex bridges into $\mathcal{D}^{\mathrm{co}}$ via the Jimbo–Miwa irregular-singular KZB framework.

These three categories refine into one another by forgetting curvature and flattening filtration; they are the three faces of a single factorization-enriched $(\infty,2)$-categorical presentation.

---

## 5. Inner Music

The bar complex is Volume I's primitive: the minimal homotopical shadow of a chiral algebra, the first place where Koszul duality is visible. Koszul duality is Volume I's heartbeat: every page pulses with an algebra/cooperad pair, a bar/cobar adjunction, a shadow and its source. The Arakelov form $\omega_g$ is Volume I's final cadence: the unavoidable curvature that closes the flat regime of genus zero and opens the modular tower; its universal lift $\boldsymbol{\kappa}$ is the chord that resolves the entire volume.

The seed opens. The bar complex is first-in/last-out: every subsequent construction — Swiss-cheese pair in Volume II, Calabi–Yau functor $\Phi_d$ in Volume III — factors through it.

---

## 6. Consequence Ledger

**Error catalogue healed or scope-clarified.** The adversarial campaign's findings against Volume I fall into three categories: technical malpractice (mis-citations, phantom labels, absent lemmas, ambient mis-specifications) healed by supplying the correct citation or construction; scope-clarification entries (UNIFORM-WEIGHT vs ALL-WEIGHT tagging, κ-subscripting conventions, level-stripped r-matrix) absorbed by the tensor Arakelov formulation and the fingerprint framework; and genuine research opens (admissible-level periodic Koszul duality, chain-level chiral Higher Deligne at full strength) which enter Volume I as named conjectures with explicit reduction to a single identified technical hypothesis.

**Cross-volume bridges.**
- **Volume I $\to$ Volume II.** The $E_\infty$-chiral and $E_1$-chiral specializations of Theorem A furnish the two pillars of Volume II's ladder. The $E_\infty$-chiral pillar (symmetric bar, $\Sigma_n$-coinvariant) supports the climb through Swiss-cheese and the $E_\infty$-topologization of the derived chiral center; the $E_1$-chiral pillar (ordered bar) supports the Yangian and quantum-group faces. Theorem H, via chiral Higher Deligne, is the engine of Volume II's universal holography.
- **Volume I $\to$ Volume III.** The Calabi–Yau functor $\Phi_d$ sends a Calabi–Yau category of dimension $d$ to an $E_n$-chiral algebra with $n=\max(1,3-d)$. Theorem A's properad form supplies the target; Theorem D's universal $\boldsymbol{\kappa}$ class pulls back to the categorical and BKM $\kappa$'s via the Borcherds weight identity $\kappa_{\mathrm{BKM}}=c_N(0)/2$; the fingerprint of $\Phi_d(\mathcal{C})$ is determined by the Hodge-theoretic invariants of $\mathcal{C}$.

Volume I, standing alone, is a self-contained theory of modular Koszul duality on curves. Volume I, standing with Volumes II and III, is the seed from which the holomorphic-topological ladder and the Calabi–Yau quantum groups grow.
