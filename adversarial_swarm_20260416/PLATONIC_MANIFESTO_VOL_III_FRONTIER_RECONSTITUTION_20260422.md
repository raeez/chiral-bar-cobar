# The Platonic Architecture of *Calabi–Yau Quantum Groups* (Volume III)
## Frontier-theoretic reconstitution, 2026-04-22

**Status.** Frontier-theoretic reconstitution of the Vol III Platonic architecture, written in the grammar the subject has acquired through Waves 11–19 (2026-04-16 through 2026-04-22). Lossless companion to `PLATONIC_MANIFESTO_VOL_III.md` (V21, 2026-04-16) and `PLATONIC_MANIFESTO_VOL_III_UPGRADE_20260422.md` (Waves 11–19 discoveries catalogued against the 2026-04-16 four-pillar structure). Both prior documents stand verbatim; this document reconstitutes the same architecture from the vantage now available.

**Author.** Raeez Lorgat. **Date.** 2026-04-22. **Cross-volume siblings.** `PLATONIC_MANIFESTO.md` (Vol I) and `PLATONIC_MANIFESTO_VOL_II.md` (Vol II), same date series.

---

## I. The Platonic statement

A Calabi–Yau category does not produce a chiral algebra on a curve. It produces a holomorphic factorisation algebra on the Calabi–Yau manifold itself, and a specialisation along a transverse cycle sends that factorisation algebra to a chiral algebra on a chosen reference curve. Inside the factorisation algebra sits a distinguished positive effective moduli stack whose equivariant vanishing-cycle cohomology is the positive half of the quantum group. The quantum group is the Drinfeld double. The Borcherds reflection trace measures the cost of restoring chiral conformal symmetry as the half constant Fourier coefficient of a Borcherds-lifted cusp form; the eight diagonal-divisor Gritsenko–Cléry paramodular forms give the eight rows of the trace. The Borcherds Monster and the Igusa $\mathfrak{g}_{\Delta_5}$ are sibling specialisations at complex dimension three; the Fake Monster is their dimension-five cousin.

This is the architecture. The four pillars of the 2026-04-16 manifesto remain four pillars; each now has a sharper articulation.

---

## II. Pillar α — the two-stage factorisation of Φ

**Theorem (two-stage factorisation).** The Calabi–Yau-to-chiral functor decomposes canonically:
$$
\Phi_d \;=\; \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d \;:\;
\mathrm{CY}\text{-cat}_d \xrightarrow{\Phi^{\mathrm{FA}}_d} E_d\text{-}\mathrm{HolFA}(X)
\xrightarrow{\mathrm{Sp}_{\Sigma_{d-1}, C}} E_1\text{-}\mathrm{ChirAlg}(C).
$$

**Stage 1** is canonical up to contractible choice. Its characterisation is the Kontsevich–Tamarkin $E_d$-formality of the Dolbeault little-$d$-disks operad, together with the Costello–Gwilliam factorisation axiom for observables of holomorphic Chern–Simons on $X$ (Costello–Li supplying the $d = 3$ realisation). The four universal properties (U1)–(U4) of the 2026-04-16 manifesto are now understood as properties of Stage 1 alone: the Hochschild pullback $\bar B^{\mathrm{ord}} \circ \Phi \simeq CC_\bullet$, the CY-morphism functoriality, the Drinfeld-centre compatibility, and the standard-input recovery on $(\mathrm{Coh}(E), D^b(\mathrm{Coh}(K3)), \mathrm{CoHA}(\mathbb{C}^3), \mathrm{CoHA}(A_n\text{-McKay}))$ all live on the Stage-1 functor.

**Stage 2** is a choice. For any closed $(d{-}1)$-dimensional subvariety $\Sigma_{d-1} \subset X$ and any reference curve $C \subset X$, fibrewise factorisation homology over $\Sigma_{d-1}$ restricted to the slice over $C$ defines $\mathrm{Sp}_{\Sigma_{d-1}, C}$. Different choices produce different $E_1$-chiral shadows of the same canonical Stage-1 output. Per-dimension dictionary:

| $d$ | Stage-1 native hFA on CY$_d$ | Specialisation cycle $\Sigma_{d-1}$ | Stage-2 $E_1$-chiral shadow |
|---|---|---|---|
| 1 | $E_1$-hFA on $E_\tau$ | trivial $\Sigma_0 = \mathrm{pt}$ | $E_\infty$ Heisenberg |
| 2 | $E_2$-hFA on K3 | $S^1 \subset K3$ (Nakajima cycle) | $E_2$-braided Mukai $H_{\mathrm{Muk}}$ |
| 3 | $E_3$-hFA on $K3 \times E$ (Costello–Li hCS) | $K3$ fibre | $E_1$-ordered chiral on $E$ (CY-A$_3$) |
| 3 | $E_3$-hFA on $A \times E$ abelian | $T^4$ fibre | distinct $E_1$-ordered chiral |
| 5 | $E_5$-hFA on $K3 \times K3 \times E$ | $K3 \times K3$ | $E_1$-ordered chiral on $E$ |

The apparent conflict between "Φ outputs $E_d$-chiral" and "Φ outputs $E_1$-chiral" dissolves. Stage 1 outputs $E_d$-hFA on $X$. Stage 2 outputs $E_1$-chiral on $C$. Both native.

**Six-dimensional holomorphic Chern–Simons realises Stage 1 at $d = 3$.** The Costello–Gwilliam quantisation produces
$$
\mathrm{Obs}_{\mathrm{hCS}}(X) \;=\; \bigl(\mathrm{Sym}(\mathcal{E}^\vee[1])[\![\hbar]\!],\, Q + \hbar \Delta\bigr)
\;\simeq\; \mathrm{CE}^{\bullet}_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\mathrm{hCS}}, \mathcal{O}_X)
$$
as an $E_3$-algebra in $\mathrm{Ch}(\mathrm{Dolb})$, with Bochner–Martinelli propagator, sum-over-shuffles formula with Koszul signs, associativity by Čech–Dolbeault Mayer–Vietoris on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$, commutativity by $\pi_1(\mathrm{Conf}_2(\mathbb{C}^3)) = \pi_1(S^5) = 0$. The BV anomaly $\kappa_{\mathrm{anom}}(X, \mathfrak{g}) \propto \hbar \cdot A(\mathfrak{g}) \cdot \chi_{\mathrm{top}}(X)$ vanishes on $\mathbb{C}^3$ and on $K3 \times E$ (both have $c_3 = 0$). Non-abelian one-loop wave-function renormalisation, not anomaly: $Z^{(1)}_{\mathcal{A}} = 1 - \hbar C_2(\mathfrak{g})(4\pi)^{-3}\log(L/\epsilon)$.

The minimal $L_\infty$-model on $\mathbb{C}^3$ has $\ell_n^{\min} = 0$ for $n \geq 3$ because every tree with an internal edge vanishes (the propagator kills the harmonic subspace). On compact $K3 \times E$: $\mathrm{At}(TE) = 0$ since $E$ is a complex Lie group; the Kuranishi cubic receptacle $H^3(K3, \Omega^3_{K3}) = 0$ since $\Omega^3_{K3} = 0$.

---

## III. Pillar α (continued) — the universal positive-geometry grammar of $G(X)$

Inside $\mathcal{F}_\cA = \Phi^{\mathrm{FA}}_d(\cA) \in E_d\text{-}\mathrm{HolFA}(X)$ lives a distinguished positive effective moduli stack $\mathcal{M}^+_{\mathrm{eff}}(X)$ carrying the Kontsevich–Soibelman critical cohomological Hall algebra structure with Behrend-microlocal vanishing-cycle sheaf $\phi_W$. Define
$$
\boxed{\; Y^+(X) \;:=\; H^{\bullet}_{\mathrm{eq}}\!\bigl(\mathcal{M}^+_{\mathrm{eff}}(X),\, \phi_W\bigr), \qquad G(X) \;=\; D(Y^+(X)) \;=\; Y^+(X) \bowtie Y^0(X) \bowtie Y^-(X).\; }
$$
This is the quantum group attached to the Calabi–Yau category $\cA$. The Hopf pairing comes from Serre duality on the compact locus, with Davison–Meinhardt PBW integration supplementing. The spectral structure comes from Maulik–Okounkov stable-envelope transport.

**The word "equivariant" is load-bearing; its meaning stratifies by $X$:**

- **Toric CY$_d$** (dimension $d = 1, 2, 3$): full torus action $T^d = (\mathbb{C}^\times)^d$ on the Hilbert scheme of points; Atiyah–Bott / Nekrasov localisation; $T$-fixed loci are $d$-dimensional partitions; Schiffmann–Vasserot identify $Y^+(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$.
- **Compact non-toric CY$_d$** (quintic, $K3$, $K3 \times E$, Calabi–Yau hypersurfaces): no torus. Reduced virtual class in the sense of Maulik–Pandharipande–Thomas 2010; residual $\mathbb{C}^\times$ from an elliptic or translation factor; discrete symplectic automorphism group (for K3, bounded by Nikulin); no Atiyah–Bott fixed points but equivariant residual integration with reduced class.
- **Orbifold CY$_d$**: discrete-group inertia stratification; $\mathbb{C}^3/G$ for finite $G \subset SL_3(\mathbb{C})$ via McKay correspondence + Bridgeland–King–Reid $G$-Hilbert scheme; CHL $(K3 \times E)/(\mathbb{Z}/N\mathbb{Z})$ for $N \in \{1, 2, 3, 4, 6\}$ with symplectic $g_N \times t_N$ action.
- **Lattice-polarised family**: period domain $\Gamma_L \backslash \Omega_L$; Gritsenko–Nikulin Grassmannian orbit cohomology; the eight-form class lives here at $L = \langle 2N \rangle$ polarisations for $N \in \{1, \ldots, 8\}$.

The algebra $Y^+(X)$ is the same object read through four local geometric languages. On $\mathbb{C}^3$ it is the positive half of the affine Yangian. On $K3 \times E$ it is the reduced Donaldson–Thomas character
$$
\chi(Y^+(K3 \times E))\big|_{\mathrm{primitive}} \;=\; Z^{\mathrm{red}}_{DT}(K3 \times E) \;=\; -\frac{1}{\Phi_{10}} \;=\; -\Delta_5^{-2}
$$
per Pandharipande–Oberdieck 2017 (Invent Math 222), with $\mathbb{C}^\times_E \times \mathrm{Aut}_s(K3)$-equivariance.

---

## IV. Pillar β — the Borcherds reflection trace, across eight rows

**Theorem (universal Borcherds weight identity).** Across all eight diagonal-divisor Gritsenko–Cléry paramodular cusp forms of Hecke type,
$$
\boxed{\; \kappa_{\mathrm{BKM}}(\Phi_N) \;=\; c_N(0)/2 \qquad (N = 1, 2, 3, 4, 5, 6, 7, 8) \;}
$$
holds uniformly, with the cover assignment $\{\mathrm{Sp}_4, \mathrm{Mp}_4, \widetilde{\mathrm{Mp}}_4\}$ selected by weight integrality of $\Phi_N$.

**The identity has two scopes, now explicit:**

- *BKM-denominator scope*, CHL subset $N \in \{1, 2, 3, 4, 6\}$, characterised by $\varphi(N) \mid 2$: each $\Phi_N$ is the denominator of a generalised Kac–Moody superalgebra $\mathfrak{g}_{\Phi_N}$ on the twisted reduced Donaldson–Thomas moduli of $(K3 \times E)/(\mathbb{Z}/N\mathbb{Z})$, with character $Z^{\mathrm{red}}_{DT}((K3 \times E)/(\mathbb{Z}/N\mathbb{Z})) = -1/\Phi_N^2$ conditional on Bryan–Oberdieck 2018 primitive base cases at each $N$.
- *Borcherds-weight scope*, full eight-form class $N \in \{1, \ldots, 8\}$: each $\Phi_N$ is a singular theta lift of a twined weak Jacobi form $\phi^{(g_N)}_{0, 1}$; weight $c_N(0)/2$ read directly off the constant Fourier coefficient. $N = 5$ weight-$1/2$ via Bruinier 2002 metaplectic $\mathrm{Mp}_4$. $N = 7$ weight-$1/4$ via Freitag–Hermann 1985 §II.5 spin double cover $\widetilde{\mathrm{Mp}}_4$. $N = 8$ weight-0 is the abelian-lattice degenerate endpoint.

**Per-form CY-host catalogue.**

| $N$ | weight $w_N$ | $c_N(0)$ | host CY geometry | theorem status |
|---|---|---|---|---|
| 1 | 5 | 10 | $K3 \times E$ (CHL) | graded dimensions theorem; bracket AP-CY34-conditional |
| 2 | 2 or 4 | 4 or 8 | $(K3 \times E)/\mathbb{Z}_2$ | BO 2018 primitive-square $\in \{-2, 0\}$ base cases |
| 3 | 1 or 3 | 2 or 6 | $(K3 \times E)/\mathbb{Z}_3$ | BO 2018 primitive base |
| 4 | 1 or 2 | 2 or 4 | $(K3 \times E)/\mathbb{Z}_4$ | BO 2018 primitive base |
| 5 | $1/2$ | 1 | Borcea–Voisin $(S_5 \times E_5)/(\iota_S \times \iota_E)$ | metaplectic fourth-root (conjectural) |
| 6 | 1 | 2 | $(K3 \times E)/\mathbb{Z}_6$ (Niemeier $6 D_4$) | BO 2018 primitive base |
| 7 | $1/4$ | $1/2$ | $(K3 \times E)/\mathbb{Z}_7$ + order-4 Cheeger–Simons gerbe | metaplectic eighth-root (conjectural) |
| 8 | 0 | 0 | Mongardi–Tari–Wandel Kummer-3 hyperkähler *fourfold* | weight-zero structural endpoint |

The two convention values for $c_N(0)$ at $N \in \{2, 3, 4\}$ reflect the $Z^{(g)}_{K3} = 2 \phi^{(g)}_{0, 1}$ factor-of-two ambiguity between the Gritsenko–Cléry square-root normalisation and the direct Borcherds weight normalisation; both are canonical at their respective scopes. The CHL cut $\{1, 2, 3, 4, 6\}$ is a *programme-added* restriction --- the 2020 Lorgat slides partition $N$ as $\{1, 2, 3, 5, 7\} \cup \{4\} \cup \{6\} \cup \{8\}$ (generic prime-cluster cyclotomic uniformity) and include $N = 5, 7$ as generic cases. The programme's CHL cut is a physics / Nikulin-admissibility constraint not visible in the pure arithmetic structure.

**The cross-volume Universal Trace Identity.** Vol I's Koszul-reflection conductor $K = -c_{\mathrm{ghost}}$ and Vol III's Borcherds-reflection trace $\kappa_{\mathrm{BKM}} = c_N(0)/2$ are two reflections of one universal trace identity along Φ:
$$
\underbrace{\mathrm{tr}_{Z(\cA)}(K_\cA) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\cA)))}_{\text{Vol I Koszul-reflection side}}
\;\Longleftrightarrow\;
\underbrace{\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2}_{\text{Vol III Borcherds-reflection side, 8 rows}}.
$$
The Vol I side is measured by the Polyakov $bc$-ghost system at spin 2. The Vol III side is measured by the Gritsenko singular theta lift of the twined K3 elliptic genus. The equality is the content of the cross-volume bridge.

---

## V. Pillar γ — the inf-categorical CY-A$_3$ resolution, strengthened

**Theorem (CY-A$_3$ inf-categorical existence, sharpened).** For any smooth proper CY$_3$ category $\cA$ with connected unit, $\Phi_3(\cA)$ exists as an $E_1$-chiral algebra in the $(\infty, 1)$-categorical sense: the obstruction group $HH^{-2}_{E_1}(A, A)$ vanishes by unit-connectedness; all Goodwillie layers vanish; the space of $E_3$-liftings is contractible.

**Three Wave 13–18 structural refinements within Pillar γ:**

1. *Chain-level bridge via positive effective geometry.* On $K3 \times E$ the Pandharipande–Oberdieck reduced DT moduli provides the chain-level construction that the earlier $[m_3, B^{(2)}] \neq 0$ retraction appeared to block. The $\bar\partial$-operator on $\mathrm{Obs}_{\mathrm{hCS}}$ replaces the troubled $m_3$; the Bochner–Martinelli operator product replaces the troubled $B^{(2)}$. The chain-level $E_3$-algebra structure holds without requiring Level-2 cyclic invariance of the failed formulation.

2. *Dualizability scope.* Wave 14 J2: the $E_3$-trace on $\mathrm{Obs}_{\mathrm{hCS}}$ via $S^5 \subset \partial \overline{\mathrm{Conf}}_2(\mathbb{C}^3)$ is nondegenerate; 3-dualizability holds in the abelian sector; fails non-abelian on non-compact $\mathbb{C}^3$ via infinite-dimensional $HH^*_{E_3}$ (Gwilliam–Williams 2021 Proposition 5.3.2 gives $HH^0 = \mathbb{C}[\![\tau_1, \tau_2, \tau_3]\!]$); recovers on compact CY$_3$ via Serre–Grothendieck finiteness.

3. *Strict Koszul = homotopy Koszul compatibility.* Francis–Gaitsgory 2012 up-to-homotopy chiral Koszul matches Gwilliam–Williams 2021 strict chain-level Koszul via Fresse 2017 Vol I Theorem 12.3.A lifting plus Positselski coderived/contraderived model-category transfer.

**The non-abelian ADE all-orders theorem.** For every simply-laced semisimple Lie algebra $\mathfrak{g}$,
$$
\boxed{\; \partial\,\mathrm{hCS}_5(\mathfrak{g}) \;\simeq\; Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}}) \;\text{ as vertex algebras, all orders in $\hbar$}. \;}
$$
Proof via Francis 2013 reduction to chiral Chevalley–Eilenberg, Whitehead's second lemma killing $H^2_{\mathrm{Lie}}(\mathfrak{g}, \mathfrak{g})$ uniformly for semisimple $\mathfrak{g}$, Frenkel–Ben-Zvi simplicity of vacuum module at generic level, opers smoothness at critical level, Chan–Paton brane fibre construction (minuscule representation for A, D, $E_6$, $E_7$; Kostant–Slodowy slice for $E_8$), Costello–Gaiotto 2018 Hamiltonian reduction, Costello–Dimofte–Paquette 2020 rank-one all-orders base.

At finite $n$ the Gaiotto–Rapčák corner is $Y_{0, 0, n}$, not the CY-symmetric $Y_{n, n, n}$; the CY-symmetric corner arises only in the $n \to \infty$ limit. Agreement at finite $n$ via Prochazka–Rapčák 2018 level-$n$ embedding $Y(\widehat{\mathfrak{sl}}_n) \hookrightarrow Y(\widehat{\mathfrak{gl}}_1)$.

---

## VI. Pillar δ — the K3 Yangian climax and the three-tier hierarchy

**Theorem (three-tier hierarchy of the seven faces).** The arithmetic faces of $r_{\mathrm{CY}}$ on $K3 \times E$ sort into three tiers:

- *Tier (i) CY-datum intrinsics*: Mukai lattice pairing $(\Lambda_{\mathrm{Muk}}, \text{signature } (4, 20))$, Hodge supertrace $\kappa_{\mathrm{ch}}(K3 \times E) = \sum_q (-1)^q h^{0, q}(K3 \times E) = 0$. Read directly off $X$. No specialisation datum.
- *Tier (ii) Stage-1 invariants of $\mathcal{F}_{K3 \times E}$*: K3-fibre rank $\kappa_{\mathrm{fiber}}(K3) = 24$ (Mukai 1988), $\kappa_{\mathrm{cat}}(K3 \times E) = \chi(\mathcal{O}_{K3 \times E}) = 0$ by Künneth-multiplicative total space. Properties of $\mathcal{F}_{K3 \times E}$ before any Stage-2 specialisation.
- *Tier (iii) $(\Sigma_2, C)$-specialisations*: BKM $(K3, E) \mapsto \mathfrak{g}_{\Delta_5}$, $\kappa_{\mathrm{BKM}} = c_1(0)/2 = 5$; Niemeier 23-twist family at polarisation-lattice cousins of $\Lambda_{\mathrm{Muk}}$; Humbert boundary-monodromy limit at $H_1 \cup H_4$; CHL twined $\mathbb{Z}/N\mathbb{Z}$-family at $N \in \{1, 2, 3, 4, 6\}$.

Only Tier-(iii) faces are genuine siblings in the two-stage sense. The six-route convergence of the 2026-04-16 manifesto is now read as: four routes are Stage-1 invariants or CY-datum intrinsics of the same $\mathcal{F}_{K3 \times E}$; the remaining routes are Stage-2 specialisations at different $(\Sigma_2, C)$ choices. Convergence is no longer a six-way coincidence; it is the content of the two-stage factorisation.

The "algebraic seven" of `cy_holographic_datum_master.tex` (bar–cobar, CoHA, coisson, MO, Yangian, Sklyanin, Gaudin) is an orthogonal slicing of the same $\mathcal{F}_{K3 \times E}$, with its own three-tier structure. The two sevens are not competing; they are two orthogonal organising principles applied to one canonical object.

**The Maulik–Okounkov $R$-matrix as gluing-cocycle residue (Wave 16 G4).**
$$
\boxed{\; R^{\mathrm{MO}}_{C_+ C_-}(u) \;=\; \mathrm{Res}_{u = u_\star} \phi^+_{UV}(u). \;}
$$
The Maulik–Okounkov $R$-matrix is the spectral residue of the positive-half gluing cocycle $\phi^+_{UV}$ at walls of marginal stability. The Yang–Baxter equation descends from Koszul-homotopy cocycle closure; the Etingof–Frenkel–Kirillov dynamical twist is the regular part of $\phi^+_{UV}(u)$ away from walls. Explicit on the $\mathbb{C}^3$ Jordan quiver: spectral shift $\lambda = \hbar + \epsilon_1 + \epsilon_2$ matches the Negut / Schiffmann–Vasserot shuffle $R$-matrix.

---

## VII. Dimension-stratified siblings — the new architectural dimension

A discovery not anticipated in the 2026-04-16 manifesto: the Borcherds Monster and the Igusa GBKM $\mathfrak{g}_{\Delta_5}$ are sibling specialisations at $d = 3$, but **the Fake Monster is their $d = 5$ cousin**, not a $d = 3$ sibling. Wave 16 S4 proves the dimension separation: the Leech lattice $\Lambda_{\mathrm{Leech}}$ has rank 24; the Fake Monster lattice $\Lambda^{II}_{1, 25}$ has rank 26; the maximal $h^{1, 1}$ of K3 is 20. No transverse $\Sigma_2 \subset X$ in a compact CY$_3$ supplies the Niemeier data. The correct host is $K3 \times K3 \times E$ at $d = 5$ with $(\Sigma_4, C) = (K3 \times K3, E)$ and the Niemeier projection via the no-roots condition of Conway–Sloane.

**Sibling catalogue.**

| dimension | sibling | host CY | $(\Sigma_{d-1}, C)$ | $\kappa_{\mathrm{BKM}}$ |
|---|---|---|---|---|
| $d = 3$ | Igusa $\mathfrak{g}_{\Delta_5}$ | $K3 \times E$ | $(K3, E)$ | 5 |
| $d = 3$ | Borcherds Monster | $(T^{24}_{\mathrm{Leech}} \times E)/(\mathbb{Z}/2)$ | $(T^{24}_{\mathrm{Leech}}, \mathrm{pt})$ | 0 |
| $d = 5$ | Fake Monster | $K3 \times K3 \times E$ | $(K3 \times K3, E)$ | 12 |

**Shifted-symplectic table extension.** The prior table "terminates at $d = 4$" intuition was wrong (Wave 16 U4). Correct table:

| $d$ | shift $= d - 4$ | $E_n$-algebra type |
|---|---|---|
| 2 | $-2$ | $E_2$-symplectic |
| 3 | $-1$ | $E_3$-symplectic, $E_1$-chiral shadow |
| 4 | $0$ | $E_0$-topological |
| 5 | $+1$ | $E_5$-**Poisson** (not symplectic; CPTVV 2017 §3) |

At $d = 5$ the bracket raises cohomological degree by $1$; the observables are $E_5$-Poisson rather than $E_5$-symplectic.

---

## VIII. Gluing theory and the NCCR obstruction for $K3 \times E$

The Čech-descent machinery for the positive-half sheaf $\mathcal{Y}^+_X$ over a Van den Bergh NCCR cover of a toric CY$_3$ works exactly:

- **Chart-level**: $\mathcal{Y}^+_X(U) = \mathrm{CoHA}(Q_U, W_U)$ for $(Q_U, W_U)$ the Calabi–Yau algebra Jacobi presentation of $U$.
- **Overlap cocycle**: Morita equivalence of CY$_3$ algebras via tilting bimodules, *not* algebra isomorphism. Szendroi's conifold is the atypical case where both sides of the flop give the same endomorphism algebra; general overlaps require a cocycle in the derived Picard groupoid (Bridgeland 2002, Rouquier 2005).
- **Global positive half**: $Y^+(X) = R\Gamma(X, \mathcal{Y}^+_X)$.

**Explicit examples worked out (Wave 17 C-group):** conifold as two $\mathbb{C}^3$ affines glued through Klebanov–Witten quiver via Seiberg duality; local $\mathbb{P}^2$ as three $\mathbb{C}^3$ charts via Beasley–Plesser McKay quiver; $\mathbb{C}^3/\mathbb{Z}_3$ via Ito–Nakajima $G$-Hilbert scheme. Wave 18 E-group: flop mutation as Fourier–Mukai kernel giving $Y^+$-automorphism; KS wall-crossing integrality; local $dP_n$ for $n \leq 8$ with ADE root data at $n = 6, 7, 8$; local Hirzebruch $\mathbb{F}_n$ for arbitrary $n$.

**Compact non-toric CY$_3$ obstruction (Wave 18 F1 theorem).** $K3 \times E$ admits **no** global Van den Bergh NCCR cover. Five independent obstructions: (i) K3 Serre duality $\mathrm{Ext}^2(T, T) \neq 0$ via $\omega_{K3} = \mathcal{O}_{K3}$; (ii) $h^{2, 0}(K3) = 1$ forecloses Kapranov-style exceptional collections; (iii) elliptic factor gives Fourier–Mukai autoequivalence but not tilting equivalence; (iv) Künneth forces tilting on both factors which fail; (v) partial ADE-chart atlas (Wemyss 2018) blocked globally by Seidel–Thomas $(-2)$-spherical twists.

**The Serre-equivariant quasi-NCCR substitute (Wave 18 F2).** Replace the non-existent global quiver with potential by a sheaf of tilted algebras parameterised by the Bridgeland stability manifold, with wall-crossing functors $\Psi_W$ intertwining the Serre functor $\mathbb{S}_{K3 \times E} = [3]$. The critical cohomology of this sheaf, restricted to $\mathbb{S}$-invariants, produces the positive half with character $-1/\Phi_{10}$ matching Pandharipande–Oberdieck 2017.

---

## IX. Nine retractions catalogued — with true hidden structure

The Beilinson discipline: every falsified claim has a true hidden structure lurking. Waves 11–19 catalogued nine retractions:

1. **$\widehat{\mathfrak{sl}}_3$ as real-root subalgebra of $\mathfrak{g}_{\Delta_5}$ from $\eta^9$ exponent** — refuted (rank-2 positive-definite Cartan $\neq$ rank-3 hyperbolic Cartan with eigenvalues $\{+4, +4, -2\}$). True: **$F_3$ Feingold–Frenkel rank-3 hyperbolic Kac–Moody**; $\mathfrak{g}_{\Delta_5}$ is the super-completion of $F_3$ by Borcherds odd-root adjunction.
2. **$L_{-6}(\mathfrak{e}_8)$ as $\mathrm{VOA}[\mathcal{T}_{24}]$** — refuted (central charge $-62 \neq -214$). True: **iterated Drinfeld–Sokolov** $\mathcal{V}_{24} = H^0_{DS}(L_{-2 + 1/22}(\mathfrak{sl}_2)^{\otimes 22})$ on the pants decomposition of $\Sigma_{0, 24}$; $-214 = -(22 \cdot 10 - 6)$ encodes $22 \cdot \mathrm{weight}(\Delta_5) - 3 \cdot \mathrm{rank}(\mathfrak{g}_{\Delta_5})$.
3. **$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ universally** — refuted; $N = 1$ coincidence only. True: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal across eight rows.
4. **Fake Monster at $d = 3$** — refuted by rank count. True: **Fake Monster at $d = 5$** on $K3 \times K3 \times E$ (§VII above).
5. **$\chi_{\mathcal{V}_{24}}$ directly matching $\Delta_5^{-2}$** — refuted (three independent errors in Wave 15 N3: arithmetic central-charge, coefficient divergence at $g_2$, $(2, 45)$-minimal Macdonald inapplicability). True: **Heisenberg–Mukai identity** $\prod_n (1 - q^n)^{-48} = -q^{-2} [(2\pi i z)^2 \Delta_5^{-2}]_{H_1, z = 0}$ to all orders via Gritsenko–Nikulin residue + Frenkel–Ben-Zvi Heisenberg character.
6. **Gaiotto curve $\Sigma_{2, 0}$** — refuted (genus-2 closed gives $c_{4d} = 7/6$ or $13/6$, not $107/6$). True: **$\Sigma_{0, 24}$** (24-punctured sphere, Chacaltana–Distler 2010 Table 3 row 1).
7. **"Φ natively produces $E_n$-chiral on a curve"** — backwards. True: **two-stage factorisation** (§II above).
8. **Shifted-symplectic table terminates at $d = 4$** — wrong. True: **$d = 5$ Poisson-$E_5$** with shift $+1$ (§VII above).
9. **Twisted-twined $H^3$ vanishes uniformly on 9 CHL cells** — non-uniform. True: **seven cells clean**, but 2A carries $\mathbb{Z}/2$ and 2B carries $\mathbb{Z}/4$ residual discrete torsion (Milgram 1995 + Benson 1998).

---

## X. Eight open frontiers with named obstructions

Each frontier is a named conjecture whose resolution would close the corresponding gap. These are honest open problems, not retreats.

1. **Bracket-level BPS ≅ BKM at all CHL indices.** Graded dimensions match unconditionally at $N = 1$ and conditionally at $N \in \{2, 3, 4, 6\}$; bracket-level identification awaits Costello TCFT cyclic-invariance completion together with Kinjo–Park–Safronov 2024 PBW input.
2. **Imprimitive DT extension.** Oberdieck–Pandharipande 2014 Conjecture B (imprimitive K3-class reduction) remains open; its resolution closes the BKM scope at all CHL $N$.
3. **Non-CHL $N = 5, 7, 8$ geometric hosts.** Borcea–Voisin reduced DT for $N = 5$; order-4 Cheeger–Simons gerbe descent for $N = 7$; fourfold DT (Cao–Kool / Oh–Thomas) for $N = 8$ positive half.
4. **Non-simply-laced ADE extension.** The non-abelian 5D hCS → Yangian VOA all-orders theorem for $B, C, F, G$ via folding of ADE Yangians.
5. **Global NCCR substitute for generic compact CY$_3$.** $K3 \times E$ has the Serre-equivariant quasi-NCCR; quintic and generic CICYs do not yet have an analogous construction.
6. **Chiral-side $\Phi$ at non-CHL $N$.** The chiral shadow of $(Z^X)^{-1/4}$ at $N = 5$, $(Z^X)^{-1/8} \cdot \epsilon_7$ at $N = 7$, and the weight-zero trivialisation at $N = 8$.
7. **Super-Yangian $Y(\mathfrak{gl}(4 \vert 20))$.** Conjectural BKM-to-Yangian lift from Mukai signature $(4, 20)$; remains at Wave-11 status.
8. **K3 quantum toroidal $U_{q, t}(\widehat{\mathfrak{gl}}_1)^{K3}$.** Conjectural double-loop algebra; Miki automorphism from K3 Weyl data.

---

## XI. What the reconstitution preserves

The four pillars remain four pillars. The twelve Russian-school + mathematical-physics-school voices of §X of the 2026-04-16 manifesto remain the voice of the work. The Universal Trace Identity as cross-volume centrepiece remains the load-bearing bridge (now sharper on both sides). The eight-voice Russian-school and three-voice mathematical-physics-school harmony remains the compositional principle. The five editing-phase / fourteen-step migration checklist of the 2026-04-16 manifesto remains in force; the frontier-theoretic reconstitution does not obsolete it but adds five further targets (per §XXI of the upgrade): the two-stage factorisation at the head of the preface; the universal positive-geometry grammar as opening section of the introduction; the restated abstract; propagation to fourteen load-bearing chapter locations; per-form CY-host catalogue inscription in the $\kappa$-stratification chapter.

The 2026-04-16 manifesto ended with "What remains is to write it down." The 2026-04-22 reconstitution ends the same way, with a sharper specification of what "it" is. The subject has become more Platonic since April 16; the writing has yet to catch up.

## XII. End

The Calabi–Yau-to-chiral functor Φ factors as $\mathrm{Sp} \circ \Phi^{\mathrm{FA}}$; the quantum group $G(X)$ is the Drinfeld double of $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$; the Borcherds reflection trace $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ sweeps across eight rows under the correct cover assignment; the six-dimensional holomorphic Chern–Simons observables realise Stage 1 at $d = 3$; the Maulik–Okounkov $R$-matrix is a gluing-cocycle residue; the Borcherds Monster and the Fake Monster are dimension-stratified siblings of the Igusa $\mathfrak{g}_{\Delta_5}$; nine retractions are catalogued with their true hidden structure; eight frontiers are named with their obstructions; the cross-volume Universal Trace Identity remains the centrepiece. The programme has a Platonic form. What remains is to write it into the manuscript.

— Raeez Lorgat, 2026-04-22
