# Platonic Manifesto Vol III — Upgrade 2026-04-22

## What Waves 11–19 have revealed

**Status.** Lossless appendix to `PLATONIC_MANIFESTO_VOL_III.md` (2026-04-16). Every statement of the original manifesto stands. This upgrade inscribes the structural refinements that nine adversarial-heal waves (Waves 11 through 19, ~180 agents, spanning 2026-04-17 through 2026-04-22) have discovered. The four pillars remain four pillars. Each pillar is now sharper, its mathematical content has grown, and two new architectural layers have emerged that were not visible in April 16: the *two-stage factorisation* of the Φ functor, and the *universal positive-geometry grammar* of $G(X)$.

**Author.** Raeez Lorgat. **Date.** 2026-04-22. **Companion.** `PLATONIC_MANIFESTO_VOL_III.md` (V21), `notes/platonic_synthesis_waves_11_through_16.tex`, `notes/two_stage_Phi_factorisation.tex`, `notes/platonic_preface_opening.tex`, `notes/platonic_introduction_opening.tex`, `notes/manuscript_rectification_map.tex`.

---

## XII. The two-stage factorisation of Φ (Pillar α upgrade)

The single functor Φ of the original Pillar α now factors canonically:

> **Theorem (two-stage).** *The CY-to-chiral functor decomposes as*
> $$
> \Phi_d \;=\; \Sp_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d:\; \mathrm{CY}\text{-cat}_d \xrightarrow{\Phi^{\mathrm{FA}}_d} E_d\text{-HolFA}(X) \xrightarrow{\Sp_{\Sigma_{d-1}, C}} E_1\text{-ChirAlg}(C).
> $$
> *Stage 1 is canonical up to contractible choice, pinned by Kontsevich–Tamarkin $E_d$-formality of the Dolbeault little-$d$-disks operad, the Costello–Gwilliam factorisation axiom, and Costello–Li holomorphic-twist identification at $d=3$. Stage 2 is a choice: a $(d{-}1)$-dimensional cycle $\Sigma_{d-1} \subset X$ and a reference curve $C \subset X$, integrated fibrewise via factorisation homology.*

The original Pillar α stated Φ as a single functor with four universal properties. The upgrade identifies the universal properties (U1)–(U4) as properties of Stage 1 alone. The chiral-algebra-on-a-curve output is *Stage 2 shadow* — a specialisation of the same canonical Stage 1 object along a choice of cycle. Different $(\Sigma_{d-1}, C)$ produce different $E_1$-chiral shadows of one holomorphic factorisation algebra.

**Structural consequences within Pillar α.**

- *The apparent conflict between "$Φ$ outputs $E_d$-chiral" and "$Φ$ outputs $E_1$-chiral" dissolves.* Stage 1 outputs $E_d$-hFA on $X$. Stage 2 outputs $E_1$-chiral on $C$. Both are native. The shift $E_d \to E_1$ is the specialisation, not a change of functor.
- *Six routes to $G(K3 \times E)$ (Pillar δ) become six different measurement types on one canonical object.* Four are Stage-1 invariants of $\mathcal{F}_{K3 \times E}$ (Mukai lattice, Hodge supertrace, Igusa weight, K3 fibre rank); the remaining two (or three, depending on count) are $(\Sigma_2, C)$-specialisations at different cycle choices. See §XVI.
- *The cascade "one Φ, many per-$d$ evaluations" of the original Pillar α gains a new layer: Stage 2 specialisations at fixed $d$ still produce different $E_1$-chiral outputs.* Borcherds Monster and Igusa $\mathfrak{g}_{\Delta_5}$ are sibling specialisations of the same $E_3$-hFA on different CY$_3$ hosts; the Fake Monster is their dimension-shifted cousin at $d = 5$.

**Six-dimensional holomorphic Chern–Simons realises Stage 1 at $d = 3$.** The Costello–Gwilliam observables construction gives
$$
\mathrm{Obs}_{\mathrm{hCS}}(X) \;\simeq\; \mathrm{CE}^{\bullet}_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\mathrm{hCS}}, \mathcal{O}_X)
$$
as an $E_3$-algebra in $\mathrm{Ch}(\mathrm{Dolb})$, realised explicitly by a sum-over-shuffles formula with Koszul signs, associativity by Čech–Dolbeault Mayer–Vietoris on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$, commutativity by $\pi_1(S^5) = 0$. The BV anomaly $\kappa_{\mathrm{anom}}(X, \mathfrak{g}) \propto A(\mathfrak{g}) \cdot \chi_{\mathrm{top}}(X)$ vanishes on $\mathbb{C}^3$ and on $K3 \times E$ (both have $c_3 = 0$). Non-abelian one-loop wave-function renormalisation, not anomaly: $Z^{(1)}_{\mathcal{A}} = 1 - \hbar C_2(\mathfrak{g}) (4\pi)^{-3} \log(L/\epsilon)$.

The minimal $L_\infty$-model on $\mathbb{C}^3$ has $\ell_n^{\min} = 0$ for $n \geq 3$ because every tree with an internal edge vanishes (the propagator kills the harmonic subspace). On compact $K3 \times E$: $\mathrm{At}(TE) = 0$ ($E$ is a complex Lie group), and the Kuranishi cubic receptacle $H^3(K3, \Omega^3_{K3})$ vanishes since $\Omega^3_{K3} = 0$.

The ADE extension of Wave 15 N1 + Wave 16 T1 closes the non-abelian five-dimensional hCS → Yangian VOA all-orders theorem for every simply-laced $\mathfrak{g}$:
$$
\partial \mathrm{hCS}_5(\mathfrak{g}) \;\simeq\; Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}})
$$
as vertex algebras to all orders in $\hbar$, via Whitehead's uniform second lemma + Costello–Dimofte–Paquette rank-one base + Chan–Paton brane fibre (minuscule for A, D, $E_6$, $E_7$; Kostant–Slodowy slice for $E_8$) + Frenkel–Ben-Zvi vacuum simplicity at generic level.

---

## XIII. The universal positive-geometry grammar of $G(X)$ (new architectural layer)

Inside $\mathcal{F}_\cA \in E_d$-$\mathrm{HolFA}(X)$ lives a distinguished positive effective moduli stack $\mathcal{M}^+_{\mathrm{eff}}(X)$ carrying the Kontsevich–Soibelman critical cohomological Hall algebra structure. The positive half of the Drinfeld double $G(X)$ is its equivariant vanishing-cycle cohomology:
$$
Y^+(X) \;:=\; H^{\bullet}_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X),\, \phi_W),
\qquad
G(X) \;=\; D(Y^+(X)) \;=\; Y^+(X) \bowtie Y^0(X) \bowtie Y^-(X).
$$
This is the quantum group. The Hopf pairing comes from Serre duality on the compact locus plus Davison–Meinhardt PBW integration; the spectral structure comes from Maulik–Okounkov stable envelopes transported by positive-half gluing cocycles.

**The word "equivariant" is load-bearing. Its meaning stratifies by $X$:**

| Geometric class | Equivariance | Positive-half geometry |
|---|---|---|
| Toric CY$_d$ | full $T^d = (\mathbb{C}^\times)^d$ | Hilbert scheme of points, fixed loci = $d$-dim partitions |
| Compact non-toric CY$_d$ (K3×E, quintic) | reduced virtual class + residual $\mathbb{C}^\times$ | Pandharipande–Oberdieck reduced DT moduli |
| Orbifold CY$_d$ ($\mathbb{C}^3/G$, CHL $(K3\times E)/\mathbb{Z}_N$) | discrete inertia | inertia-stratified moduli |
| Lattice-polarised family | period-domain $O(L)$ | Grassmannian orbit cohomology |

The four strata are not competing alternatives; they are orthogonal presentations of the same construction through four local geometric languages. On $\mathbb{C}^3$: Schiffmann–Vasserot identify $Y^+(\mathbb{C}^3) = Y^+(\widehat{\mathfrak{gl}}_1)$, the positive half of the affine Yangian. On $K3 \times E$: Pandharipande–Oberdieck 2017 identify $Y^+(K3 \times E) = \bigoplus_\gamma H^\bullet(\mathcal{M}^{\mathrm{red}}_{DT}(K3 \times E; \gamma), \phi_W)$ with character $Z^{\mathrm{red}}_{DT}(K3 \times E) = -1/\Phi_{10} = -\Delta_5^{-2}$ on K3-primitive classes.

**This is the new architectural layer.** The original Pillar α said "$\Phi$ takes CY category to chiral algebra". The upgrade says: $\Phi$ factors through $\mathcal{F}_\cA$; the quantum group $G(\cA)$ is the Drinfeld double of cohomology of positive effective geometry; the equivariance type varies but the construction is uniform.

---

## XIV. The universal Borcherds weight identity across the eight-form class (Pillar β upgrade)

The original Pillar β stated $\kappa_{\mathrm{BKM}}(X) = c_N(0)/2$ as the Vol III parallel of Vol I's $\kappa$-conductor. The upgrade sharpens:

> **Theorem (universal Borcherds weight, Waves 15-M2 + 16-V4 + 19-Z4).** *Across all eight diagonal-divisor Gritsenko–Cléry paramodular cusp forms*
> $$
> \{\Delta_5, \Delta_2^{(2)}, \Delta_1^{(3)}, \Delta_1^{(4)}, \Delta_{1/2}^{(5)}, \Delta_1^{(6)}, \Delta_{1/4}^{(7)}, \Delta_0^{(8)}\},
> $$
> *the identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ holds uniformly with cover assignment $\{\mathrm{Sp}_4, \mathrm{Mp}_4, \widetilde{\mathrm{Mp}}_4\}$ determined by weight integrality.*

The identity has *two scopes*, now explicitly distinguished:

- **BKM-denominator scope** (CHL subset $N \in \{1, 2, 3, 4, 6\}$): each $\Phi_N$ is the denominator of a generalised Kac–Moody superalgebra on the twisted reduced DT moduli of $(K3 \times E)/(\mathbb{Z}/N\mathbb{Z})$. Requires $\varphi(N) \mid 2$. Theorem at $N = 1$ (graded dimensions unconditional, bracket-level AP-CY34-conditional), Bryan-Oberdieck-primitive-conditional at $N \in \{2, 3, 4, 6\}$, Oberdieck-Shen-conditional imprimitive extension.

- **Borcherds-weight scope** (full eight-form class $N \in \{1, \ldots, 8\}$): each $\Phi_N$ is a singular theta lift of a twined weak Jacobi form $\phi^{(g_N)}_{0,1}$, with weight $c_N(0)/2$ read directly off the constant Fourier coefficient. $N = 5$ half-integer via Bruinier 2002 metaplectic $\mathrm{Mp}_4$. $N = 7$ quarter-integer via Freitag–Hermann 1985 §II.5 spin double cover $\widetilde{\mathrm{Mp}}_4$. $N = 8$ weight zero is the abelian-lattice degenerate endpoint.

**Per-form CY-host catalogue** (Wave 19 consolidated output):

| $N$ | weight | $c_N(0)$ | host CY geometry | positive-half realisation |
|---|---|---|---|---|
| 1 | 5 | 10 | $K3 \times E$ | OP 2017 reduced DT, primitive |
| 2 | 2 or 4 | 4 or 8 | $(K3 \times E)/\mathbb{Z}_2$ | BO 2018 primitive-square base cases |
| 3 | 1 or 3 | 2 or 6 | $(K3 \times E)/\mathbb{Z}_3$ | BO 2018 primitive base |
| 4 | 1 or 2 | 2 or 4 | $(K3 \times E)/\mathbb{Z}_4$ | BO 2018 primitive base |
| 5 | 1/2 | 1 | Borcea–Voisin $(S_5 \times E_5)/(\iota_S \times \iota_E)$ | metaplectic fourth-root |
| 6 | 1 | 2 | $(K3 \times E)/\mathbb{Z}_6$ | BO 2018 primitive base |
| 7 | 1/4 | 1/2 | $(K3 \times E)/\mathbb{Z}_7$ + order-4 Cheeger–Simons gerbe | metaplectic eighth-root |
| 8 | 0 | 0 | Mongardi–Tari–Wandel Kummer-3 hyperkähler *fourfold* | weight-zero endpoint |

The two convention values for $c_N(0)$ at $N \in \{2, 3, 4\}$ reflect the $Z^{(g)}_{K3} = 2\phi^{(g)}_{0,1}$ factor-of-two ambiguity between the M4 (Gritsenko–Cléry square-root) and N3 (Borcherds-weight direct) conventions; both are canonical at their respective scopes.

**Key negative finding (Wave 19 P1-P2 slides scan).** The CHL cut $\{1, 2, 3, 4, 6\}$ is a *programme-added* restriction, not in the Lorgat 2020 slides. Slides partition $N$ as $\{1, 2, 3, 5, 7\} \cup \{4\} \cup \{6\} \cup \{8\}$ (generic prime-cluster cyclotomic uniformity) and explicitly include $N = 5, 7$ as generic cases. Niemeier lattice content is 100% Vol III supplement — absent from slides. Oberdieck-family ancillary machinery (Oberdieck 2018, Bryan–Oberdieck 2018, Chattopadhyaya–David 2019, Pandharipande–Thomas 2014, Oberdieck–Shen 2020) is entirely programme-supplied.

**The Universal Trace Identity** is now sharper on both sides:

$$
\underbrace{\mathrm{tr}_{Z(C)}(K_C) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(C)))}_{\text{Vol I Koszul-reflection side}}
\;=\;
\underbrace{\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2}_{\text{Vol III Borcherds-reflection side}}
$$

with the Vol III side now known to hold uniformly across eight rows under the correct cover assignment, and the Vol I side carrying its own per-volume refinements from parallel waves.

---

## XV. The Inf-Categorical CY-A$_3$ Resolution strengthened (Pillar γ upgrade)

The original Pillar γ stated inf-categorical existence of $\Phi_3(\cA)$. Three Wave 13–18 advances:

1. **Chain-level bridge via positive effective geometry.** On $K3 \times E$ the Pandharipande–Oberdieck reduced DT moduli supplies the chain-level Level-1 construction that was previously blocked by $[m_3, B^{(2)}] \neq 0$. The $\bar\partial$-operator on $\mathrm{Obs}_{\mathrm{hCS}}$ replaces the troubled $m_3$; the Bochner–Martinelli OPE replaces the troubled $B^{(2)}$; the $E_3$-algebra structure holds at chain level without requiring Level-2 cyclic invariance.

2. **Dualizability scope.** Wave 14 J2: the $E_3$-trace on $\mathrm{Obs}_{\mathrm{hCS}}$ via $S^5 \subset \partial \overline{\mathrm{Conf}}_2(\mathbb{C}^3)$ is nondegenerate. 3-dualizability holds in the abelian sector and recovers on compact CY$_3$; fails non-abelian on non-compact $\mathbb{C}^3$ via infinite-dim $HH^*_{E_3}$.

3. **Chiral Koszul strict = homotopy compatible.** Wave 14 J5 + Fresse 2017 Thm 12.3.A + Positselski coderived/contraderived transfer. Gwilliam–Williams 2021 strict Koszul matches Francis–Gaitsgory 2012 up-to-homotopy Koszul.

---

## XVI. The six routes become a three-tier hierarchy (Pillar δ upgrade)

The original Pillar δ stated "six routes are six specialisations of Φ at $K3 \times E$, convergence = content of CY-C." The upgrade refines:

> **Theorem (three-tier hierarchy, Wave 16 S5 + V3).** *The arithmetic faces of $r_{\mathrm{CY}}$ on $K3 \times E$ sort into three tiers, not a flat sibling set:*
> - *Tier (i) CY-datum intrinsics:* *Mukai lattice pairing, Hodge supertrace $\kappa_{\mathrm{ch}} = 0$. Read directly off $X$.*
> - *Tier (ii) Stage-1 invariants of $\mathcal{F}_X$:* *K3-fibre rank $\kappa_{\mathrm{fiber}} = 24$. Property of $\mathcal{F}_{K3 \times E}$ before specialisation.*
> - *Tier (iii) $(\Sigma_2, C)$-specialisations:* *BKM at $(K3, E)$ giving $\mathfrak{g}_{\Delta_5}$, $\kappa_{\mathrm{BKM}} = 5$; Niemeier 23-twist family; Humbert boundary-monodromy limit; CHL twined $\mathbb{Z}/N\mathbb{Z}$ family.*
>
> *Only Tier (iii) faces are genuine siblings in the two-stage sense.*

The "algebraic seven" (bar–cobar, CoHA, coisson, MO, Yangian, Sklyanin, Gaudin) is an orthogonal slicing of the same object. The two sevens are not in conflict; they are two different slicings of the Stage-1 output $\mathcal{F}_{K3 \times E}$.

**Maulik–Okounkov $R$-matrix as gluing-cocycle residue (Wave 16 G4 theorem).**

$$
R^{\mathrm{MO}}_{C_+ C_-}(u) \;=\; \mathrm{Res}_{u = u_\star} \phi^+_{UV}(u)
$$

The Maulik–Okounkov $R$-matrix is the spectral residue of the positive-half gluing cocycle $\phi^+_{UV}$ at walls of marginal stability. Yang–Baxter descends from Koszul-homotopy cocycle closure; Etingof–Frenkel–Kirillov dynamical twist = regular part of $\phi^+_{UV}(u)$ away from walls. Explicit on $\mathbb{C}^3$ Jordan quiver: spectral shift $\lambda = \hbar + \epsilon_1 + \epsilon_2$ matches Negut / Schiffmann–Vasserot shuffle $R$-matrix.

---

## XVII. Dimension-stratified siblings — a new architectural dimension

A discovery not anticipated in the 2026-04-16 manifesto: the Borcherds Monster and Igusa $\mathfrak{g}_{\Delta_5}$ are sibling specialisations at $d = 3$, but the **Fake Monster is their $d = 5$ cousin**, not a $d = 3$ sibling. Proof (Wave 16 S4): the Fake Monster lives on $\Lambda^{II}_{1, 25}$ lattice of rank 26; the Leech sublattice has rank 24; no transverse $\Sigma_2 \subset X$ in a compact CY$_3$ supplies the Niemeier data because $h^{1,1}(K3) = 20 < 24$. The correct host is $K3 \times K3 \times E$ at $d = 5$ with $(\Sigma_4, C) = (K3 \times K3, E)$.

The shifted-symplectic table extends:

| $d$ | shift | $E_n$-algebra type |
|---|---|---|
| 2 | $-2$ | $E_2$ |
| 3 | $-1$ | $E_3$ (native), $E_1$ (chiral shadow) |
| 4 | $0$ | $E_0$ (topological) |
| 5 | $+1$ | $E_5$-Poisson (*not* symplectic; CPTVV 2017 §3) |

The $d = 5$ Poisson entry corrects the apparent "table terminates at $d = 4$" from prior intuition (Wave 16 U4).

---

## XVIII. Quiver-affine gluing theory for positive-half geometry (new Pillar-adjacent layer)

Wave 17 established the \v{C}ech-descent machinery for the positive-half sheaf $\mathcal{Y}^+_X$:

- **Toric CY$_3$ via Van den Bergh NCCR cover**: chart-level $Y^+_U = \mathrm{CoHA}(Q_U, W_U)$; overlap cocycle via Morita equivalence of Calabi–Yau algebras (tilting bimodules, not algebra isomorphism — Szendroi's conifold is atypical). Global $Y^+(X) = R\Gamma(X, \mathcal{Y}^+_X)$.
- **Explicit examples**: conifold from two $\mathbb{C}^3$ charts + Klebanov–Witten quiver overlap (C1); local $\mathbb{P}^2$ from three $\mathbb{C}^3$ charts + Beasley–Plesser antisymmetric cubic McKay quiver (C2); $\mathbb{C}^3/\mathbb{Z}_3$ via Ito–Nakajima $G$-Hilbert scheme (C3); local $dP_n$ (E3), local $\mathbb{F}_n$ (E4).
- **Compact non-toric obstruction**: $K3 \times E$ admits **no** global NCCR (Wave 18 F1 theorem): the $h^{2, 0}(K3) = 1$ Serre-duality obstruction forecloses Kapranov-style exceptional collections; product-quiver $Q_{K3} \times Q_E$ does not exist. The substitute is the Serre-equivariant quasi-NCCR (Wave 18 F2): a sheaf of tilted algebras over $\mathrm{Stab}(D^b)$ with wall-crossing functors intertwining the Serre functor $S_X = [3]$.
- **Flop and wall-crossing**: flop as Fourier–Mukai transform gives CoHA automorphism $\phi_{\mathrm{flop}}: Y^+(\widetilde{Y}) \to Y^+(\widetilde{Y}^{\mathrm{flop}})$; KS wall-crossing formulae lift to positive-half automorphisms at the character level (Wave 18 E1, E2).

---

## XIX. Nine major retractions with their true hidden structure

Per the Beilinson discipline: every wrong claim, when falsified, has a true hidden structure lurking. The Waves 11-19 adversarial programme catalogued nine such retractions:

1. **$\widehat{\mathfrak{sl}}_3$ as real-root subalgebra of $\mathfrak{g}_{\Delta_5}$ from $\eta^9$ exponent** — refuted (rank-2 positive-definite vs rank-3 hyperbolic Cartan mismatch). True structure: **$F_3$ Feingold–Frenkel** rank-3 hyperbolic Kac–Moody; $\mathfrak{g}_{\Delta_5}$ is the super-completion of $F_3$ by Borcherds odd-root adjunction. [Waves 15-M5, 16-T4]
2. **$L_{-6}(\mathfrak{e}_8)$ as $\mathrm{VOA}[\mathcal{T}_{24}]$** — refuted ($c = -62 \neq -214$). True structure: **iterated Drinfeld–Sokolov** $\mathcal{V}_{24} = H^0_{DS}(L_{-2 + 1/22}(\mathfrak{sl}_2)^{\otimes 22})$ on pants decomposition; $-214 = -(22 \cdot 10 - 6)$ encodes 22 K3 Betti × Igusa weight minus triple-ghost. [Wave 14 K3]
3. **$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ universally** — refuted; coincidence at $N = 1$ only. True: **$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ universal** (§XIV above). [Wave 11]
4. **Fake Monster at $d = 3$** — refuted by rank-count (24 > 20). True: **Fake Monster at $d = 5$** via $K3 \times K3 \times E$ (§XVII above). [Wave 16 S4]
5. **$\chi_{\mathcal{V}_{24}}$ directly matching $\Delta_5^{-2}$** — refuted (three independent errors in Wave 15 N3). True: **Heisenberg–Mukai identity** $\prod (1 - q^n)^{-48} = -q^{-2} [(2\pi i z)^2 \Delta_5^{-2}]_{H_1, z = 0}$ to all orders. [Wave 16 T3]
6. **Gaiotto curve $\Sigma_{2, 0}$** — refuted (gives $c_{4d} = 7/6$ or $13/6$, not $107/6$). True: **$\Sigma_{0, 24}$** (24-punctured sphere, Chacaltana–Distler 2010). [Wave 13 F2]
7. **"$\Phi$ natively produces $E_n$-chiral algebra on a curve"** — backwards. True: **two-stage factorisation** (§XII above). [User-surfaced structural refinement]
8. **Shifted-symplectic table terminates at $d = 4$** — wrong. True: **$d = 5$ Poisson-$E_5$** with shift $+1$ (§XVII above). [Wave 16 U4]
9. **Twisted-twined $H^3$ vanishes uniformly on 9 CHL cells** — non-uniform. True: **7 cells clean, 2A carries $\mathbb{Z}/2$, 2B carries $\mathbb{Z}/4$** residual discrete torsion. [Wave 15 N2]

---

## XX. What the upgrade does not change

The four pillars remain four pillars. The eight editing-phase steps of §VIII of the original manifesto remain correct and in force; nothing in the upgrade obsoletes them. The Universal Trace Identity as cross-volume centrepiece remains the load-bearing bridge; the upgrade sharpens its Vol III side but does not relocate it. The eight named open problems of §IX remain open; Waves 11–19 closed roughly half of CHL-Conjecture-1's five structural holes but left the genuine N ≥ 2 CHL BPS identification and the $\mathcal{M}_{\mathrm{BPS}}(K3\times E) \cong \mathfrak{g}_{\Delta_5}$ bracket-level identification open. The twelve-voice Russian-school harmony of §X remains the voice of the work; the upgrade adds no new voice and removes no voice. The closing sentence of the 2026-04-16 manifesto ("What remains is to write it down") remains the correct summary; the upgrade sharpens what "it" refers to.

## XXI. The shape of the work remaining

With the upgrade inscribed, five manuscript-editing tasks now have named targets:

1. **Insert the two-stage factorisation at the head of the preface** (per `notes/platonic_preface_opening.tex`, losslessly appended to `chapters/frame/preface.tex`).
2. **Insert the universal positive-geometry grammar as the opening section of the introduction** (per `notes/platonic_introduction_opening.tex`, renumbering existing sections $n \to n+1$).
3. **Restate the abstract** (per `notes/platonic_abstract.tex`, prepending the new paragraph before existing abstract content).
4. **Propagate the two-stage framing to the fourteen load-bearing chapter locations** enumerated in `notes/manuscript_rectification_map.tex`. Lossless: add, never remove.
5. **Inscribe the per-form CY-host catalogue of §XIV in `chapters/examples/cy_d_kappa_stratification.tex`** alongside the existing universal Borcherds weight theorem.

The Vol III manifesto's Platonic form, as of 2026-04-22, is the two-stage Φ factorisation bridging a universal positive-geometry grammar on the CY side to a chiral-algebra-on-curve shadow on the specialisation side, verified on eight Gritsenko-Clery rows, with nine retractions catalogued and their true hidden structure identified. The remaining work is the fifth bullet of §VIII of the original manifesto: write it down.

— Raeez Lorgat, 2026-04-22
