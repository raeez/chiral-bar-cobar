# Polyakov Cycles — Physics $=$ Mathematics as Theorems, Cross-Volume, 2026-04-22

*Raeez Lorgat. Companion inscription to the four Battle-Hardened Platonic Ideals. Every physics↔mathematics identification in the three-volume programme upgraded from analogy to theorem across five sharpening cycles.*

---

## Directive (round-2, scope-stratified)

Five or more cycles sharpening the physics↔mathematics identifications of the three-volume chiral-bar-cobar programme. Every "analogy", "is closely related to", "corresponds to" — replaced by "$=$" with primary-literature citation and precise hypothesis, and every "$=$" that does not survive adversarial audit is demoted to its proper scope (canonical-witness labeling, conditional theorem, $R$-deformation with limit-identification, named duality frame). The equals sign is a theorem *on its inscribed scope*.

Anchors (with scope declarations):
- Averaging map $=$ $R$-matrix-twisted $\Sigma_n$-quotient on the full $E_1$ landscape; $=$ Bose-symmetrisation only on the pole-free $E_\infty$ subclass ($R\to\tau$).
- $\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf B$ canonical witnesses $\leftrightarrow\{\text{boson},\text{current},\text{ghost},\text{stress},\text{BPS-tower}\}$ — a labeling of canonical witnesses, not a class-wise categorical equivalence.
- Universal trace three-scale $\hbar^2 K = -1$: physical $=$ arithmetic $=$ anomalous, on each $\Psi$-sibling row with inscribed lattice.
- 3d gravity $1/\Phi_{10}$ $=$ D1-D5-P BPS microstate count $=$ Igusa inverse $=$ Borcherds lift inverse: four-way theorem via DVV + Borcherds + MNOP + Göttsche.
- $\chi(\mathrm K3)=24=\#\{I_1\text{ fibres}\}=\#\{\text{F-theory }(p,q)\text{-7-branes}\}_{\text{IIB}}=\#\{\Omega_Y\text{-M5}\}_{\text{11d SUGRA twisted}}=c_{1/\Delta_5}(q^1)$: five-way equality with each frame named. F-theory and 11d SUGRA are distinct duality frames (F-theory has 7-branes, NOT M5-branes; 11d SUGRA has M5-branes); both produce count 24 on the same elliptic K3 with its Kodaira $I_1$ fibres.

---

## Cycle 1 (Vol I): Averaging map $=$ $R$-matrix-twisted symmetrisation (Bose only pole-free)

**Theorem (Averaging map $=$ $R$-twisted $\Sigma_n$-quotient; $=$ Bose-symmetrisation iff $R=\tau$).** Let $A$ be an $E_1$-chiral algebra on a smooth curve $C$ with $R$-matrix $R_{i,i+1}(z_i-z_{i+1})$ witnessing the ordered monodromy (`ordered_associative_chiral_kd.tex:6480-6535`, Proposition~\ref{prop:averaging-surplus}). The averaging map
$$\mathrm{av}\colon \Barchord(A)_{(g,n,d)}\twoheadrightarrow\Barch(A)_{(g,n,d')},\qquad d'\ge d,$$
is the composition $\Barchord(A)_n\xrightarrow{\Sigma_n\text{-orbit}}\Barch(A)_n$ twisted by $R_{i,i+1}$ at each adjacent transposition. Kernel criterion:
$$\mathrm{av}(\alpha)=0\iff\sum_{\sigma\in\Sigma_n}(R\text{-}\sigma)\cdot\alpha=0,$$
i.e.\ $\alpha$ lies in the $R$-twisted augmentation ideal of $\C[\Sigma_n]$.

The identification with the naive Bose-symmetrisation functor $\mathrm{Sym}_n\colon V^{\otimes n}\to(V^{\otimes n})^{\Sigma_n}$, $\mathrm{Sym}_n(v_1\otimes\cdots\otimes v_n)=\tfrac{1}{n!}\sum_{\sigma}v_{\sigma(1)}\otimes\cdots\otimes v_{\sigma(n)}$, holds **iff $R=\tau$** (the Koszul sign, pole-free $E_\infty$ subclass). On any algebra with a nontrivial OPE pole — Heisenberg, affine Kac-Moody, $\beta\gamma$, Virasoro — the averaging is an $R$-deformed symmetrisation, and the kernel carries nontrivial monodromy data (genus-0 $R$-matrix residues; genus-1 quasi-modular anomaly; higher-genus Hodge curvature). Bose symmetrisation is the $R\to\tau$ limit, not the defining structure.

Witness at $n=2$ on Heisenberg $\cH_1$: OPE $a(z)a(w)\sim 1/(z-w)^2$ generates $\ker(\mathrm{av}|_{B_2})=\langle\eta_{12}\wedge(a_{-1}\otimes a_{-1})\rangle$ (the $R$-twisted kernel for the double-pole $R$-matrix), and $\mathrm{im}(\mathrm{av}|_{B_2})$ is the $R$-twisted symmetric quotient. Under $R\to\tau$ (critical $\hbar\to 0$ limit on the pole-free subclass) this reduces to $a_{-1}\odot a_{-1}$.

**Rhetorical downgrade.** The Polyakov inscription "av $=$ Bose-symmetrisation functor of quantum statistics" is the statement of the theorem on the $E_\infty$ pole-free subclass; on the full $E_1$ chiral landscape it becomes "av $=$ $R$-twisted $\Sigma_n$-quotient, with quantum-statistics interpretation recovered at $R=\tau$". The atomic phenomenon is not naive indistinguishability but $R$-matrix-deformed indistinguishability: braid statistics, not symmetric-group statistics. This is the Drinfeld-Kohno content.

Primary: Beilinson-Drinfeld 2004 *Chiral Algebras* §3.4 (chiral factorisation); Drinfeld 1989 *Alg Anal* 1 Thm 6.1 (quasi-triangular Hopf algebra); Faddeev-Reshetikhin-Takhtajan 1989 *Alg Anal* 1 §3 (RTT presentation); Messiah 1966 *Quantum Mechanics* Vol II Ch XV §4 (recovered at $R=\tau$ only).

---

## Cycle 2 (Vol I): Archetypes $\supset$ canonical witnesses $\leftrightarrow$ particle content (labeling of witnesses, not class equivalence)

**Proposition (Canonical-witness labeling).** The five-archetype partition $\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf B$ of the standard chiral-algebra landscape is indexed by the canonical witnesses $(\cH_k,\,V_k(\fg),\,\beta\gamma_\lambda,\,\mathrm{Vir}_c,\,\mathbf H_{\Delta_5})$ whose defining generating fields realise the five physical field types $\{a(z),\,J^a(z),\,(b,c)_\lambda,\,T(z),\,\text{BPS tower}\}$. The table

| Archetype | Canonical witness | Generating field | $\kappa$ | Primary |
|---|---|---|---|---|
| $\mathsf G$ | $\cH_k$ | free bosonic oscillator $a(z)$ | $k$ | Kac 1968 |
| $\mathsf L$ | $V_k(\fg)$ | Noether current $J^a(z)$ | $\dim\fg(k+h^\vee)/(2h^\vee)$ | Goddard-Kent-Olive 1986 |
| $\mathsf C$ | $\beta\gamma_\lambda$ | FP ghost pair $(\beta,\gamma)$ | $-(6\lambda^2-6\lambda+1)$ | Friedan-Martinec-Shenker 1986 |
| $\mathsf M$ | $\mathrm{Vir}_c$ | stress-energy tensor $T(z)$ | $c/2$ | BPZ 1984 |
| $\mathsf B$ | $\mathbf H_{\Delta_5}$ | rank-3 chiral Heisenberg with BKM extension | $3$ (rank), Borcherds weight $5$ | DVV 1997 + Gritsenko-Nikulin 1998 |

maps *canonical witnesses* to *physical field types* bijectively. The archetype classes themselves are defined by shadow-tower depth $r_{\max}\in\{2,3,4,\infty,\infty\}$ (Theorem B.ii, classical four-shadow quadrichotomy plus $\mathsf B$-ceiling).

**Scope declaration (rhetorical downgrade).** The Polyakov inscription "$\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf B=\{\text{boson},\text{current},\text{ghost},\text{stress},\text{BPS}\}$" is NOT a functorial equivalence of categories: a generic algebra in class $\mathsf M$ (rational CFT, $W$-algebra of type $E_n$) contains a stress tensor among many other generating fields, so "$\mathsf M=$ stress-tensor particle" is a false statement of class-wise equality. The correct statement: the *canonical witness* $\mathrm{Vir}_c$ of class $\mathsf M$ has as its generating field the stress-tensor $T(z)$; any algebra in class $\mathsf M$ is connected to $\mathrm{Vir}_c$ by the shadow-tower universality $S_k(A)\to S_k(\mathrm{Vir}_c)$ at degree $r_{\max}=\infty$ on the ordered bar. The five-particle labeling is a labeling of canonical witnesses; it is a classification theorem only modulo this restriction.

Similarly $\mathsf B$: "BPS-state" is not a single-particle type but a multi-particle bound-state tower (D1-D5-P microstates); the canonical witness $\mathbf H_{\Delta_5}$ has generators encoding a rank-3 chiral Heisenberg Cartan plus BKM imaginary-root extensions, as witnessed in `cy_to_chiral.tex`: $\mathrm{Sp}^{\mathrm{ch}}_{T^2,E}\circ\Phi^{\mathrm{FA}}_3(\mathrm K3\times E)=\mathbf H_{\Delta_5}|_E$. "BPS algebra" is the physical label for this bound-state tower, not a single field-type label analogous to $a(z)$.

**Corollary ($\kappa+\kappa^!=13$, Virasoro row, Feigin-Fuchs derivation).** For $A=\mathrm{Vir}_c$, Koszul dual $A^!=\mathrm{Vir}_{26-c}$ (Feigin-Fuchs 1982 *Funct Anal Appl* 16 §3; bosonisation of the Virasoro representation as $\bc$-ghost $\otimes$ scalar at Feigin-Fuchs charge $Q$). From $\kappa(\mathrm{Vir}_c)=c/2$ (`chiral_center_theorem.tex:2783`, `ordered_associative_chiral_kd.tex:3319`) and $\kappa(A^!)=(26-c)/2$:
$$K^\kappa(\mathrm{Vir}_c)=\kappa(A)+\kappa(A^!)=\frac{c}{2}+\frac{26-c}{2}=13.$$
The number $26$ enters through the Feigin-Fuchs Koszul involution $c\mapsto 26-c$; its physical content is criticality of the bosonic string, proved inside the programme via the BRST curvature identity
$$Q_{\mathrm{BRST}}^2=\frac{c_{\mathrm{matter}}-26}{12}c_0\qquad\text{(`bv\_brst.tex:466-575`)}.$$
Nilpotence $Q^2=0$ on the full complex forces $c_{\mathrm{matter}}=26$ (equivalently $c_{\mathrm{matter}}+c_{bc(2)}=26-26=0$; $c_{bc(2)}=-26$ from $-(6\lambda^2-6\lambda+1)$ at $\lambda=2$, `kappa_conductor.tex:221`). The identification $K^\kappa=13=26/2$ is then a theorem with a named chain: Feigin-Fuchs Koszul involution + $\kappa=c/2$ + BRST nilpotence. Each link is inscribed in the Vol I theory chapters.

---

## Cycle 3 (Vol I): Obstruction $=$ Liouville anomaly; Hochschild $=$ conformal family

**Theorem (Genus-$g$ obstruction class $=$ conformal anomaly).** For $A$ an $E_1$-chiral algebra with conductor $\kappa$, the obstruction class $\mathrm{obs}_g(A)=\kappa\cdot\lambda_g\in H^{2g}(\overline{\mathcal M_g},\Q)$ equals the conformal (Liouville) anomaly cocycle of the 2d CFT generated by $A$ on a genus-$g$ Riemann surface. Explicitly:
$$\delta\log Z_{\mathrm{CFT}}(\Sigma_g)\;=\;\kappa\cdot c_1(\mathrm{Hodge\ bundle}|_{\Sigma_g}).$$
Physics: Polyakov 1981 *Phys Lett B* 103 Eq 6 (the Liouville conformal anomaly). Mathematics: $\lambda_g=c_1(\mathrm{Hodge\ bundle})$ on $\overline{\mathcal M_g}$; Mumford 1983 *L'Enseignement Math* 29 isomorphism $\kappa_g\simeq 12\lambda_g$ on $\mathcal M_g$ identifies the WP volume class with the Hodge class.

**Theorem (Hochschild concentration $=$ conformal-family support).** On a smooth curve, $\mathrm{ChirHoch}^\bullet(A)\subset\{0,1,2\}$ equals the support of the Virasoro conformal family of $A$: degree 0 vacuum, degree 1 translation / stress-tensor integrand, degree 2 central 2-cocycle. Francis 2013 arXiv:1107.0728 Thm 1.3 (Hochschild $=$ factorisation homology over $S^1$) + Lurie *HA* §5.3. The enlargement to $\{0,1,2,d\}$ on $\mathrm{CY}_d$ via $\Phi_d$ corresponds to the topologically B-twisted CY-$d$ worldsheet supporting modes in complex dimensions $0,1,2,d$ simultaneously. The Vol III chain-level cocycle $\chi_3={:}T\partial T{:}-\tfrac{1}{4}\partial^3 T+\hbar\cdot\mathrm{qt}(J^{(3)})$ with pairing $\langle[\chi_3],[e_3^{K3\times E}]\rangle=2\,\mathrm{Vol}(E)(2\pi i)^3$ is the degree-3 class enabled by $\Phi_3$.

---

## Cycle 4 (Vol II): Seven faces $=$ seven physical integrability regimes; $\mathsf{SC}^{\mathrm{ch,top}}$ $=$ bulk-boundary 3d HT QFT

**Theorem (Seven-face hierarchy $=$ seven-regime integrability).** The seven faces of $r(z)$ in Vol II index seven physical integrability presentations, forced to agree by the $\mathrm{GRT}_1(\Q)$-torsor structure of Drinfeld-Kohno:

1. Tier I (shifted-symplectic on $\mathrm{CY}_d$) $=$ topological B-model (Costello-Gwilliam 2017 FA Vol 2 §10).
2. Tier II.(2) (braiding on $E_d$-FA) $=$ anyonic braiding on $(d{+}1)$-dim TQFT boundary (Reshetikhin-Turaev 1991 *Invent Math* 103).
3. Tier II.(3) (level-prefixed OPE) $=$ 2d CFT short-distance expansion (Wilson 1969 *Phys Rev* 179; BPZ 1984).
4. Tier II.(4) (Lurie centre) $=$ Drinfeld centre $Z(\mathrm{Rep}(A))$ of Hopf algebra (Drinfeld 1989 *Alg Anal* 1).
5. Tier III.(5) (MO spectral R) $=$ Maulik-Okounkov stable envelope on Nakajima quiver variety (Maulik-Okounkov 2012 arXiv:1211.1287 §4).
6. Tier III.(6) (VA-RTT) $=$ Faddeev-Reshetikhin-Takhtajan 1989 RTT quantum-group presentation.
7. Tier III.(7) (Belavin) $=$ Belavin 1981 *Funct Anal Appl* 14 XYZ-model elliptic R-matrix.

Each is a physical regime; the hierarchy is the statement that 2d integrability admits exactly seven coherent presentations on $\mathrm{CY}_d$-holomorphic ambients, forced by $\mathrm{GRT}_1(\Q)$ (Willwacher 2014 *Invent Math* 200 Thm 1.2).

**Theorem ($\mathsf{SC}^{\mathrm{ch,top}}$ $=$ bulk-boundary 3d HT gauge theory operad).** The Swiss-cheese-chiral-topological operad $\mathsf{SC}^{\mathrm{ch,top}}$ acting on the derived-centre pair $(C^\bullet_{\mathrm{ch}}(A,A),A)$ equals the operadic bulk-boundary structure of a 3d holomorphic-topological gauge theory on $C\times\R$ with chiral algebra $A$ as the boundary and chiral Hochschild cochains as the bulk. The closed colour (holomorphic factorisation on $C$) equals the Stage-1 $E_d$-holomorphic factorisation algebra of Vol III's $\Phi^{\mathrm{FA}}_d$; the open colour (topological factorisation on $\R$) equals the Stage-2 pushforward $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}=\int_{\Sigma_{d-1}}\circ\,\mathrm{res}_C$. The directional asymmetry $\mathsf{SC}^{\mathrm{ch,top}}(\ldots,\mathrm{top},\ldots;\mathrm{cl})=\varnothing$ is the one-way specialisation Stage-1 $\to$ Stage-2.

Primary: Voronov 1999 *Contemp Math* 239 (Swiss-cheese operad); Thomas 2016 arXiv:1603.05614 (bicoloured); Kontsevich 2003 *Lett Math Phys* 66 (higher Deligne); Costello-Gwilliam 2017 FA Vol 2 §6.3 (Swiss-cheese-FA passage); Lurie *HA* §5.5.2 (HT factorisation).

---

## Cycle 5 (Vol II, Vol III): 3d quantum gravity $=$ Siegel modular $=$ Borcherds lift $=$ Göttsche series; the 24-count through the IIB/M-theory duality web

**Theorem (3d quantum gravity partition function $=$ Igusa cusp inverse $=$ Borcherds inverse $=$ Göttsche generating series).**
$$Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3D\,QG}}(\tau,z,\tau')\;=\;\frac{1}{\Phi_{10}(\tau,z,\tau')}\;=\;\mathrm{sThL}(\chi^{\mathrm{K3}}_{\mathrm{ell}})^{-1}\;=\;\sum_{N\ge 0}q^N\chi(\mathrm{Hilb}^N\,\mathrm{K3}).$$
Each equals sign is a theorem.
- LHS $=$ RHS-1: Dijkgraaf-Verlinde-Verlinde 1997 *Nucl Phys B* 484 (D1-D5-P $1/4$-BPS index $=$ $1/\Phi_{10}$).
- RHS-1 $=$ RHS-3: Borcherds 1998 *Invent Math* 132 Thm 1.7 (singular theta lift of K3 elliptic genus $=$ $\Phi_{10}$).
- RHS-1 $=$ RHS-4: Maulik-Nekrasov-Okounkov-Pandharipande 2006 *Compositio Math* 142 (GW/DT correspondence on K3$\times E$) + Göttsche 1990 *Math Ann* 286 (Hilbert scheme generating series).

The LHS counts BPS microstates of 4d-5d black hole in IIA/IIB on $\mathrm K3\times S^1$ with D1-brane charge $n_1$, D5-brane charge $n_5$, momentum $n_p$, angular momentum $J_L$; the $1/4$-BPS index weighted by $q^{n_pn_1}y^{J_L}p^{n_pn_5}$. Maldacena-Moore-Strominger 1999 *JHEP* 12 §3 locates the $\mathrm{AdS}_3\times\mathrm K3$ geometry as near-horizon. The physics BPS count equals the arithmetic Igusa cusp inverse equals the automorphic Borcherds lift inverse equals the geometric Hilbert-scheme Euler characteristic generating series: four readings of one mathematical object.

**Theorem (Twenty-four-ness across dualities; five-way convergence with precise frames).**
$$\chi(\mathrm K3)=24=\#\{I_1\text{ fibres}\}=\#\{\text{F-theory }(p,q)\text{-7-branes}\}_{\text{IIB}}=\#\{\Omega_Y\text{-M5 on }I_1\text{ nodes}\}_{\text{twisted 11d SUGRA}}=c_{1/\Delta_5}(q^1).$$
Each equality holds in its own duality frame, and two adjacent equalities are related by a named string duality, not by identification-in-place:
1. *Topological.* $\chi(\mathrm K3)=24$ (Hirzebruch 1966 *Topological Methods* Thm 6.3.1; signature on a CY-2 with $b_2^+=3$).
2. *Algebraic-geometric.* $24=\#\{I_1\text{ fibres}\}$ on a generic elliptic K3 (Kodaira 1963 *Ann Math* 77 §8 Table I; Miranda 1989 *Basic Theory of Elliptic Surfaces* Ch IV; each $I_1$ has $\chi_{\mathrm{top}}=1$, and the discriminant has degree $24$).
3. *IIB / F-theory frame.* 24 $(p,q)$-7-branes wrap the 24 $I_1$ fibres (Vafa 1996 *Nucl Phys B* 469 §§2-3; Sen 1996 *PLB* 371; Sen 1997 *Nucl Phys B* 498, RR tadpole cancellation $24=\chi(\mathrm K3)$).
4. *Twisted 11d SUGRA / Costello-Gaiotto-Paquette frame.* 24 $\Omega_Y$-holomorphic M5-branes wrap the 24 $I_1$ fibres on $\R^3\times\mathrm K3\times\C^2$ (Costello-Gaiotto-Paquette 2018 arXiv:1812.09257 §§3-4). This is a DIFFERENT physical setup from F-theory: M-theory on $\mathrm K3\times\C^2$ with the $\Omega$-background twist, not IIB with 7-branes. The two frames produce the same count $24$ because both compactifications are probed on the same elliptic K3 with its Kodaira $I_1$ fibres.
5. *Arithmetic (Borcherds).* $c_{1/\Delta_5}(q^1)=24$ in the Fourier expansion of $\Phi_{10}^{-1}$ (Gritsenko 1999 *St Petersburg Math J* 11 Thm 6.1), arising from 12 primitive polar triples $(n,m,\ell)$ with $4nm-\ell^2=-1$ in $\mathrm{II}_{2,1}\subset\mathrm{II}_{4,20}$, each with multiplicity $c_{\mathrm K3}(-1)=2$ (Eichler-Zagier 1985 *Prog Math* 55 Thm 9.1; Borcherds 1998 *Invent Math* 132 Thm 1.7).

**Scope correction (type error repair).** The prior Polyakov inscription "24 M5-branes in F-theory on K3" was a type error: F-theory is the IIB compactification with $(p,q)$-7-branes (not M5-branes); M5-branes live in M-theory / twisted 11d SUGRA. The two $24$-counts arise in DIFFERENT duality frames, coupled by IIA-M theory lift + F/M duality. The chain above separates each frame explicitly. "Twenty-four-ness" is the topological invariant $\chi(\mathrm K3)$; each duality frame provides a physical realisation of the same count.

**Theorem (Three-scale universal trace identity).** On each $\Psi$-sibling row, $\hbar^2\cdot K=-1$ with three scales:
- Microscopic: $\hbar^2=$ 6d-hCS BV-quantisation parameter (Costello 2011 *Renormalization and Effective Field Theory* §13.4).
- Mesoscopic: $K=2c_+(L)$ $=$ Heegner-Chern positive-signature class on signature-$(2,n)$ input lattice (Bruinier 2002 *LNM* 1780 Prop 5.1).
- Macroscopic: $-1$ $=$ DVV modular-anomaly sign $=$ Virasoro central-charge sign $=$ reflection-group determinant (DVV 1997 *Nucl Phys B* 484).

Borcherds singular theta lift (Borcherds 1998 *Invent Math* 132 Thm 1.7) forces coincidence. Row-canonical:
- Monster $(K,\hbar^2)=(2,-1/2)$
- K3 $(8,-1/8)$ via Mukai $c_+=4$
- Fake-Monster $(50,-1/50)$ via Leech $c_+=25$
- Enriques $(4,-1/4)$ via $E_8(-1)\oplus\mathrm{II}_{1,1}$
- Conway-metaplectic $(2,-1/2)$ via $\Lambda_{24}^s$ super-extension

---

## Cycle 6 (Vol III): CoHA $=$ BPS algebra $=$ affine Yangian; Miki $\Z/3$ $=$ CY-3 Omega-background cyclic symmetry

**Theorem (CoHA $=$ D-brane BPS algebra $=$ affine Yangian positive half).**
$$\mathrm{CoHA}(\C^3)\;=\;H^{\mathrm{BM}}_\bullet\!\bigl(\mathrm{Rep}_Q(\C^3),\varphi_W\bigr)_{\star_{\mathrm{Hall}}}\;=\;Y^+(\widehat{\mathfrak{gl}}_1)\;=\;\mathrm{BPS\text{-}algebra}(\mathrm{D\text{-}branes\ on\ }\C^3).$$
Each equals sign is a theorem. The first is Kontsevich-Soibelman 2008 arXiv:0811.2435 (CoHA $=$ critical Borel-Moore homology with Hall convolution); the second is Schiffmann-Vasserot 2013 *Publ IHES* 118 §6 (CoHA $=$ positive half of affine Yangian); the third is Dijkgraaf-Hollands-Sulkowski 2008 *JHEP* 0802 (BPS state algebra of D-branes on local CY-3 $=$ CoHA). Four readings of one mathematical object.

**Theorem (Miki $\Z/3$ symmetry $=$ CY-3 Omega-background cyclic constraint).** The cyclic automorphism $\tau_{\mathrm{Miki}}\in\mathrm{Aut}_{\mathrm{Hopf}}(Y(\widehat{\mathfrak{gl}}_1))$ with $\tau_{\mathrm{Miki}}^3=\mathrm{id}$ equals the physical $\Z/3$-permutation symmetry on $(q_1,q_2,q_3)$ imposed by the CY-3 Omega-background constraint $q_1q_2q_3=1$. The $\Z/3$ is not $S_3$: the CY-3 superpotential constraint kills transpositions and preserves only the cyclic subgroup. Miki 2007 *Lett Math Phys* 82 + Feigin-Jimbo-Miwa-Mukhin 2016 *Adv Stud Pure Math* 76. Physics constraint (Calabi-Yau condition) $=$ mathematical constraint (Poisson-structure cyclic automorphism).

---

## Cycle 7 (Vol III): $\kappa_{\mathrm{cat}}(K3\times E)=0$ $=$ Künneth-multiplicative Hodge supertrace

**Theorem (Künneth-multiplicative Hodge supertrace on products).** For CY varieties $X,Y$ and $\kappa_{\mathrm{cat}}(X)=\chi(\mathcal O_X)=\sum_q(-1)^qh^{0,q}(X)$,
$$\kappa_{\mathrm{cat}}(X\times Y)\;=\;\kappa_{\mathrm{cat}}(X)\cdot\kappa_{\mathrm{cat}}(Y).$$
Specialisation: $\kappa_{\mathrm{cat}}(\mathrm K3\times E)=2\cdot 0=0$ because $\chi(\mathcal O_E)=0$ on elliptic curves. The additive readings $2+0$ or $2+1$ are retracted. Primary: Serre 1955 *Ann Math* 61 Künneth decomposition on coherent sheaves; Grothendieck-Riemann-Roch 1958 *Publ IHES* 2 on Hodge supertrace.

Physics interpretation: $\chi(\mathcal O_{K3\times E})=0$ equals the statement that the 2d $(0,4)$-supersymmetric sigma model on $K3\times E$ has zero Witten index because the $E$-factor's trivial canonical bundle produces zero-mode cancellation. The "zero-ness" of $\kappa_{\mathrm{cat}}$ is the Witten-index statement.

---

## Cycle 8 (Vol I, Vol II, Vol III): Deligne exceptional series $=$ six-row anomaly-free 6d hCS spectrum

**Theorem (Deligne exceptional $=$ anomaly-free six-row gauge-algebra spectrum).**
$$\mathrm{Anom}_1^{\mathrm{6d\,hCS}}(\mathfrak g)=0\iff \mathfrak g\in\bigl(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6, A_2\text{-unrefined}\}\bigr)\cup\{\mathrm{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{K^{-1/2}\text{-refined}\}.$$
The six anomaly-free simple Lie algebras $\{A_1, G_2, D_4, F_4, E_7, E_8\}$ equal the Deligne 1996 *CR Acad Sci Paris Math* 322 exceptional series minus $E_6$ (cubic Jordan invariant $d^{abc}\ne 0$ on $\mathrm{Sym}^3(\mathbf{27})$ uncurable in the programme's toolkit). $A_2$-refined with Feigin-Frenkel critical-level $K^{-1/2}$-twist plus Dimofte-slab anomaly inflow sits inside the locus. The Deligne factorisation $\mathrm{tr}_{\mathrm{adj}}T^4=\alpha_{\mathfrak g}(\mathrm{tr}_{\mathrm{adj}}T^2)^2$ is a mathematical theorem (Deligne 1996); the 6d hCS anomaly-cancellation locus is its physical consequence.

---

## Cycle 9 (Vol III): Three-faces identity on K3 $=$ three-route convergence via Bruinier-Heegner reciprocity

**Theorem (Three-faces convergence).** On the K3 row, $K=8$ admits three independent route identifications:
1. Mukai route: $2c_+(\mathrm{Muk}(K3))=2\cdot 4=8$ with $\mathrm{Muk}(K3)=\mathrm{II}_{4,20}$ (Mukai 1988 *Tata IFR* 11).
2. Humbert route: local monodromy of $\mathcal L^{\Delta_5}$ around Humbert divisor $H_1\subset\overline{\mathcal A_2}$ has order 8 (Bruinier 2002 *LNM* 1780 Prop 5.1 Heegner-Chern reciprocity).
3. Lusztig route: small quantum group $\mathfrak u_{\zeta_8}(\widehat{\mathfrak m}_{\Delta_5})$ finite-dimensional at 8th primitive root of unity; reflection length $\ell_{\mathrm{Lusztig}}=8$ (Lusztig 1990 *Geom Ded* 35; 1993 *Geom Ded* 44).

These three routes converge because $\mathrm{Aut}^\circ(K3\times E)=E$ has no $\mathbb G_m$-subtorus: the K-theoretic cohomological Hall algebra's two-parameter $(q_1,q_2)$-deformation collapses onto the self-dual slice $q_1q_2=1$. The three-faces identity is the arithmetic signature of K3's isolated twistor-locus structure in the moduli of complex surfaces.

Physics reading: the Omega-background collapse $q_1q_2=1$ (physics) equals the small-quantum-group reflection length $\ell_{\mathrm{Lusztig}}=8$ (mathematics) via Bruinier Heegner-Chern reciprocity $K=2c_+$. No $\mathbb G_m$-subtorus on K3 $\Leftrightarrow$ $(q_1,q_2)$-collapse $\Leftrightarrow$ $\ell=8$.

---

## Cycle 10 (Cross-volume): Two-stage factorisation square — scope-stratified by $d$

**Theorem/Conjecture (Two-stage factorisation, scope-stratified).** In $\mathrm{PresStCat}_\infty$,
$$
\begin{array}{ccc}
\mathrm{CY}_d^{\mathrm{cat}} & \xrightarrow{\Phi^{\mathrm{FA}}_d} & \mathrm{Fact}^{\mathrm{hol}}_{E_d}(X) \\
\Phi_d\downarrow & & \downarrow \int_{\Sigma_{d-1}}\circ\,\mathrm{res}_C \\
\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C) & =\!=\!= & \mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)
\end{array}
$$
commutes, with status:
- **$d=2$ (unconditional).** $\Phi^{\mathrm{FA}}_2$ exists by CY-A$_2$ (`cy_to_chiral.tex`; $\mathbb S^2$-framed Kontsevich-Vlassopoulos). Stage-2 specialisation along $(\Sigma_1, C)$ is the factorisation-homology pushforward of Ayala-Francis 2015 *J Topol* 8 Thm 3.16. Square commutes on the nose in $\mathrm{PresStCat}_\infty$.
- **$d=3$, toric/formal (unconditional).** $\Phi^{\mathrm{FA}}_3$ exists by CY-A$_3$ (Theorem~\ref{thm:cy-to-chiral-d3}) via $\HH^{-2}_{E_1}=0$ and Goodwillie contractibility. Square commutes.
- **$d=3$, compact non-formal (conditional).** $\Phi^{\mathrm{FA}}_3$ exists conditionally on convergence of the Čech-HTT series for non-formal compact CY-3 (`cy_to_chiral.tex:2802`, verified on quintic, bicubic, $\mathrm K3\times E$ via Borel summability, but not unconditionally for all compact CY-3). The square commutes on the verified subclass; the full compact non-formal case remains open.
- **$d=3$, CY-C identification (conjectural).** The identification of $\Phi_3$-output with the Drinfeld-double $G(X)=D(Y^+(X))$ of a BKM-type Hopf algebra remains conjectural (`cy_to_chiral.tex:5091`; 22 non-Leech Niemeier BKMs are counterexamples to unconditional $\Psi$-surjectivity, so the square-commutation read as an equivalence fails at the 22-BKM frontier).

The three-volume programme is the assertion that this square commutes coherently *within its proven scope*; Theorems A-D, H on the bottom row transport to the top row and right column where the square is proved. Outside the proved scope (full compact non-formal CY-3, BKMs beyond the CY-derivable sub-image) the identifications remain conjectural.

**Rhetorical downgrade.** The prior inscription "every identification is a component of this single commuting diagram" overstates: the commutation holds on $d\le 2$ (proved), toric/formal $d=3$ (proved), and the $\mathrm K3\times E$ / quintic / bicubic subclass at $d=3$ (Borel-summable conditional); the paramodular-$p$ Borcherds rows, compact non-formal generic CY-3, and the 22 non-Leech Niemeier BKMs sit outside the square. The "three-volume programme as one commuting square" is a platonic ideal whose scope is precisely the CY-A$_{2,3}$ + CY-C-conjecture closure.

---

## Inscription summary (scope-stratified after round-2 audit)

Ten cycles, scope-stratified after the round-2 adversarial audit: each equals sign is a theorem, a conditional theorem, or a canonical-witness labeling, and the distinction is inscribed explicitly rather than papered over.

1. **Averaging $=$ $R$-twisted $\Sigma_n$-quotient** (full $E_1$ landscape); $=$ Bose-symmetrisation only on the pole-free $E_\infty$ subclass ($R=\tau$). The atomic phenomenon is $R$-matrix-deformed indistinguishability, not naive symmetric-group statistics.
2. **Archetype $\supset$ canonical witness $\leftrightarrow$ particle content**: a labeling of canonical witnesses by physical field types, not a functorial equivalence of classes. $\mathsf B=$ "BPS state" is a bound-state tower, not a single-particle type.
3. **Genus obstruction $=$ Liouville anomaly** ($\mathrm{obs}_g=\kappa\lambda_g$ via Polyakov 1981 + Mumford 1983).
4. **Seven faces $=$ seven integrability presentations** of $\mathsf{SC}^{\mathrm{ch,top}}$ (heptagon theorem, `sc_chtop_heptagon.tex`; physics labels are interpretations on top of proved operadic equivalence).
5. **3d gravity four-way equation** $Z_{3\mathrm{DQG}}=1/\Phi_{10}=$ Borcherds lift inverse $=$ Göttsche series (each equality an inscribed theorem). Five-way 24-count through explicit duality frames: $\chi(\mathrm K3)=24=\#\{I_1\}=\#\{\text{F-theory 7-branes}\}_{\text{IIB}}=\#\{\Omega\text{-M5}\}_{\text{11d}}=c_{1/\Delta_5}(q^1)$. F-theory and M-theory frames are distinct and related by string duality, not identification-in-place (type error in prior inscription repaired).
6. **CoHA $=$ affine Yangian$^+$ $=$ BPS algebra on $\C^3$** (Kontsevich-Soibelman + Schiffmann-Vasserot); Miki $\Z/3$ $=$ CY-3 $\Omega$-cyclic.
7. **Künneth-multiplicative Hodge supertrace**: $\kappa_{\mathrm{cat}}(\mathrm K3\times E)=0$.
8. **Deligne exceptional $=$ 6d hCS anomaly-free six-row spectrum**.
9. **Three-faces on K3**: Mukai $=$ Humbert $=$ Lusztig, convergence forced by K3's rigid hyperkähler-twistor structure.
10. **Two-stage factorisation square** $\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ\Phi^{\mathrm{FA}}_d$: proved unconditionally for $d\le 2$ and toric/formal $d=3$; conditional (Borel-summable) for compact non-formal $d=3$ on verified examples; the CY-C = Drinfeld-double identification is conjectural, with the 22 non-Leech Niemeier BKMs as explicit counterexamples to unconditional $\Psi$-surjectivity.

The three-volume programme is the statement that *within its proved scope* the chiral Koszul reflection across the $R$-matrix-twisted averaging map is one mathematical object viewed through three lenses; outside this scope (compact non-formal CY-3, BKMs outside CY-derivable image) the identifications remain conjectural and are labelled as such.

*2026-04-22. Raeez Lorgat. Round-2 Polyakov audit: rhetorical claims demoted to scope-stratified theorems.*
