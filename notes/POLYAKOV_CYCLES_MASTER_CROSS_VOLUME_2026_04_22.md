# Polyakov Cycles — Cross-Volume Master Synthesis, 2026-04-22

*Raeez Lorgat. Companion inscription to `MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md`. Every physics↔mathematics identification across the three volumes upgraded from analogy to theorem, organised by atomic principle. Five-cycle directive executed.*

---

## Directive (round-2, scope-stratified)

"Physics$=$Mathematics as theorems *on their inscribed scope*. Every equals sign a theorem, a conditional theorem, or a canonical-witness labeling, and the distinction is inscribed explicitly."
After Drinfeld, Polyakov, Nekrasov, Witten, Kontsevich: courage earns the sharper statement; adversarial audit demotes rhetoric to its proper scope.

Cycle structure (scope-stratified after round-2 audit):
- Cycle 1: Atomic principle — averaging $=$ $R$-matrix-twisted symmetrisation on the full $E_1$ landscape; Bose-symmetrisation only on the pole-free $E_\infty$ subclass.
- Cycle 2: Archetype classification — five-archetype $\supset$ canonical witness $\leftrightarrow$ particle-field labeling (not class-wise equivalence).
- Cycle 3: Anomaly-obstruction identification — $\mathrm{obs}_g=$ Liouville anomaly (theorem); Hochschild $=$ conformal-family support.
- Cycle 4: Climax — 3d quantum gravity $=$ $1/\Phi_{10}$ $=$ D1-D5-P microstate count (four-way theorem); 24-count through named duality frames (IIB/F-theory with 7-branes; 11d SUGRA with M5-branes; distinct frames, related by string duality).
- Cycle 5: Three-scale universal trace — $\hbar^2 K=-1$ per $\Psi$-sibling row with inscribed lattice.
- Cycle 6: Two-stage factorisation square — proved on $d\le 2$ + toric/formal $d=3$; conditional on Borel-summable compact $d=3$ subclass; CY-C = Drinfeld-double conjectural with explicit counterexamples (22 non-Leech Niemeier BKMs).

---

## Cycle 1 (Atomic): Averaging map $=$ $R$-matrix-twisted symmetrisation (Bose only on pole-free $E_\infty$)

**Theorem.** The averaging map $\mathrm{av}\colon\Barchord(A)_{(g,n,d)}\twoheadrightarrow\Barch(A)_{(g,n,d')}$ ($d'\ge d$) on an $E_1$-chiral algebra with $R$-matrix $R_{i,i+1}(z_i-z_{i+1})$ on a smooth curve is the $R$-twisted $\Sigma_n$-quotient (`ordered_associative_chiral_kd.tex:6480-6535`, Proposition~\ref{prop:averaging-surplus}):
$$\mathrm{av}(\alpha)=0\iff \sum_{\sigma\in\Sigma_n}(R\text{-}\sigma)\cdot\alpha=0,$$
i.e.\ $\alpha$ lies in the $R$-twisted augmentation ideal of $\C[\Sigma_n]$. Identification with the naive Bose-symmetrisation functor $\mathrm{Sym}_n(v_1\otimes\cdots\otimes v_n)=\tfrac1{n!}\sum_\sigma v_{\sigma(1)}\otimes\cdots\otimes v_{\sigma(n)}$ holds **iff $R=\tau$** (the Koszul sign, pole-free $E_\infty$ subclass). On any algebra with a nontrivial OPE pole (Heisenberg, Kac-Moody, $\beta\gamma$, Virasoro), the averaging is $R$-deformed symmetrisation and the kernel carries $R$-matrix monodromy (genus-0 residues; genus-1 quasi-modular anomaly; higher-genus Hodge curvature).

Physics reading: chiral Koszul reflection across the averaging map is $R$-matrix-deformed particle indistinguishability on smooth curves — braid statistics, not symmetric-group statistics. Naive Bose symmetrisation is the classical limit $R\to\tau$; the full content is the Drinfeld-Kohno $R$-matrix deformation.

Witness at $n=2$ on Heisenberg $\mathcal H_1$: OPE $a(z)a(w)\sim 1/(z-w)^2$ generates $\ker(\mathrm{av}|_{B_2})=\langle\eta_{12}\wedge(a_{-1}\otimes a_{-1})\rangle$ ($R$-twisted kernel) and $\mathrm{im}(\mathrm{av}|_{B_2})$ is the $R$-twisted symmetric quotient, reducing to $a_{-1}\odot a_{-1}$ at $R=\tau$.

Primary: Beilinson-Drinfeld 2004 *Chiral Algebras* §3.4; Drinfeld 1989 *Alg Anal* 1 Thm 6.1; Faddeev-Reshetikhin-Takhtajan 1989 *Alg Anal* 1 §3; Messiah 1966 *Quantum Mechanics* Vol II Ch XV §4 (the $R=\tau$ limit only).

---

## Cycle 2 (Classification): Archetypes $\supset$ canonical witnesses $\leftrightarrow$ particle content (witness-labeling, not class equivalence)

**Proposition (Canonical-witness labeling).** The five-archetype partition $\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf B$ of the standard chiral-algebra landscape is indexed by canonical witnesses whose defining generating fields realise the five physical field types:

| Archetype | Canonical witness | Generating field | $\kappa$ | $r_{\max}$ | Primary |
|---|---|---|---|---|---|
| $\mathsf G$ | $\mathcal H_k$ | boson $a(z)$ | $k$ | $2$ | Kac 1968 |
| $\mathsf L$ | $V_k(\mathfrak g)$ | Noether current $J^a(z)$ | $\dim\mathfrak g(k+h^\vee)/(2h^\vee)$ | $3$ | GKO 1986 |
| $\mathsf C$ | $\beta\gamma_\lambda$ | FP ghost $(\beta,\gamma)$ | $-(6\lambda^2-6\lambda+1)$ | $4$ | FMS 1986 |
| $\mathsf M$ | $\mathrm{Vir}_c$ | stress tensor $T(z)$ | $c/2$ | $\infty$ | BPZ 1984 |
| $\mathsf B$ | $\mathbf H_{\Delta_5}$ | rank-3 chiral Heisenberg + BKM tower | $3$ (rank), $5$ (Borcherds weight) | $5$ (recognition gate) | DVV 1997 + GN 1998 |

The Open-row shadow depths are $r_{\max}\in\{2,3,4,\infty\}$ for $\mathsf G/\mathsf L/\mathsf C/\mathsf M$; the $\mathsf B$ crown is attached by the CY recognition gate with Vol I coordinate $r_{\max}=5$. The table maps canonical witnesses to physical field types bijectively.

**Scope declaration.** The prior inscription "$\mathsf G/\mathsf L/\mathsf C/\mathsf M/\mathsf B=\{\text{boson},\text{current},\text{ghost},\text{stress},\text{BPS}\}$" is NOT a class-wise functorial equivalence: a generic algebra in class $\mathsf M$ (rational CFT, W-algebra of type $E_n$) contains a stress tensor *among many other generating fields*; "$\mathsf M=$ stress-tensor particle" fails class-wise. The correct statement: the *canonical witness* of each archetype has as its generating field the corresponding physical field type, and any algebra in the class is connected to the canonical witness by shadow-tower universality. The five-particle labeling classifies canonical witnesses only.

Class $\mathsf B$: "BPS state" is a bound-state *tower* (D1-D5-P microstates), not a single-particle type; the canonical witness $\mathbf H_{\Delta_5}$ has generators comprising rank-3 chiral Heisenberg Cartan + BKM imaginary-root extensions (`cy_to_chiral.tex`, $\mathrm{Sp}^{\mathrm{ch}}_{T^2,E}\circ\Phi^{\mathrm{FA}}_3(\mathrm K3\times E)=\mathbf H_{\Delta_5}|_E$).

**Theorem ($\kappa+\kappa^!=13$, Virasoro row, full derivation).** $\mathrm{Vir}_c$ with Feigin-Fuchs Koszul dual $\mathrm{Vir}_{26-c}$ (`ordered_associative_chiral_kd.tex:3319`) yields
$$K^\kappa(\mathrm{Vir}_c)=\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=\frac{c}{2}+\frac{26-c}{2}=13$$
(`chiral_center_theorem.tex:2783`). The number $26$ enters through the Koszul involution; its physical content is criticality of the bosonic string, proved inside the programme via the BRST curvature identity
$$Q_{\mathrm{BRST}}^2=\frac{c_{\mathrm{matter}}-26}{12}c_0\qquad(\text{`bv\_brst.tex:466-575`}).$$
Nilpotence $Q^2=0$ on the full complex forces $c_{\mathrm{matter}}=26$; combined with $c_{bc(2)}=-26$ (from $-(6\lambda^2-6\lambda+1)|_{\lambda=2}$, `kappa_conductor.tex:221`), the total-charge condition $c_{\mathrm{tot}}=0$ gives the criticality $c_{\mathrm{matter}}+c_{bc(2)}=0$ identification. The identification $K^\kappa=13=26/2$ is then a theorem with a named chain: Feigin-Fuchs Koszul involution + $\kappa=c/2$ + BRST nilpotence.

Primary: Polyakov 1981 *Phys Lett B* 103 §2; Feigin-Fuchs 1982 *Funct Anal Appl* 16 §3; Friedan-Martinec-Shenker 1986 *Nucl Phys B* 271 §2.3.

---

## Cycle 3 (Anomaly-obstruction): $\mathrm{obs}_g$ $=$ Liouville anomaly; Hochschild $=$ conformal family

**Theorem (Genus obstruction class $=$ conformal anomaly cocycle).**
$$\mathrm{obs}_g(A)\;=\;\kappa\cdot\lambda_g\;=\;\text{conformal (Liouville) anomaly on }\Sigma_g.$$
Physics: Polyakov 1981 *Phys Lett B* 103 Eq 6 Liouville anomaly $\delta\log Z_{\mathrm{CFT}}=\kappa\cdot(\text{gravitational action})$. Mathematics: $\lambda_g=c_1(\text{Hodge bundle})$ on $\overline{\mathcal M_g}$; Mumford 1983 *L'Enseignement Math* 29 isomorphism $\kappa_g\simeq 12\lambda_g$ identifies WP volume class with Hodge class.

**Theorem (Hochschild concentration $=$ conformal-family support).**
$$\mathrm{ChirHoch}^\bullet(A)\subset\{0,1,2\}\quad(\text{curve}),\qquad\{0,1,2,d\}\quad(\text{CY-}d\text{ via }\Phi_d).$$
Physics: Virasoro conformal family support in complex dimensions $0,1,2$ (vacuum, translation, central 2-cocycle); enlargement to $\{0,1,2,d\}$ on B-twisted CY-$d$ worldsheet. Mathematics: Francis 2013 arXiv:1107.0728 Thm 1.3; Lurie HA §5.3; Vol III $\chi_3$-cocycle on $\mathrm K3\times E$ chain-level.

**Theorem (Deligne exceptional $=$ 6d hCS anomaly-free spectrum).**
$$\mathrm{Anom}_1^{\mathrm{6d\,hCS}}(\mathfrak g)=0\iff\mathfrak g\in\bigl(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6, A_2\text{-unref}\}\bigr)\cup\{\text{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{K^{-1/2}\text{-ref}\}.$$
$E_6$ strict exclude (cubic $d^{abc}\ne 0$ on $\mathrm{Sym}^3(\mathbf{27})$); $A_2$-refined (critical twist + Dimofte slab) inside. Deligne factorisation $\mathrm{tr}_{\mathrm{adj}}T^4=\alpha_{\mathfrak g}(\mathrm{tr}_{\mathrm{adj}}T^2)^2$ (Deligne 1996 *CR Acad Sci Paris Math* 322) is the mathematical theorem whose physical consequence is the anomaly-free locus.

---

## Cycle 4 (Climax): 3d quantum gravity $=$ Igusa cusp inverse $=$ Borcherds lift inverse $=$ Göttsche series

**Theorem (Climax four-way equation).**
$$\underbrace{Z^{\mathrm{AdS}_3\times\mathrm K3}_{\mathrm{3D\,QG}}(\tau,z,\tau')}_{\text{D1-D5-P }1/4\text{-BPS index}}\;=\;\underbrace{\frac{1}{\Phi_{10}(\tau,z,\tau')}}_{\text{Igusa cusp}^{-1}}\;=\;\underbrace{\sum_{N\ge 0}q^N\chi(\mathrm{Hilb}^N\,\mathrm K3)}_{\text{Göttsche series}}\;=\;\underbrace{\mathrm{sThL}(\chi^{\mathrm K3}_{\mathrm{ell}})^{-1}}_{\text{Borcherds lift}^{-1}}.$$
Chain of four equalities, each a theorem:
- LHS$=$RHS-1: Dijkgraaf-Verlinde-Verlinde 1997 *Nucl Phys B* 484.
- RHS-1$=$RHS-2: Göttsche 1990 *Math Ann* 286 + MNOP 2006 *Compositio Math* 142.
- RHS-1$=$RHS-3: Borcherds 1998 *Invent Math* 132 Thm 1.7.

Four readings of one mathematical object:
- LHS: gravitational path integral on $\mathrm{AdS}_3\times\mathrm K3$ counting $1/4$-BPS microstates of D1-D5-P bound state in IIA/IIB (Maldacena-Moore-Strominger 1999 *JHEP* 12 §3).
- RHS-1: weight-10 Siegel cusp form on $\mathrm{Sp}_4(\Z)$.
- RHS-2: Hilbert-scheme Euler-characteristic generating series.
- RHS-3: inverse of singular theta lift of K3 elliptic genus $\chi^{\mathrm K3}_{\mathrm{ell}}\in J^{\mathrm{wk}}_{0,1}$.

**Theorem (BPS microstate count $=$ Gritsenko-Nikulin denominator).**
$$\sum_{\alpha\in\Lambda^+_{\mathrm{BKM}}}(-1)^{\ell(\alpha)}e^{-\alpha}\;=\;\Phi_{10}(Z)\;=\;qpy\prod_{(n,m,\ell)>0}(1-q^np^my^\ell)^{c_{\mathrm K3}(4nm-\ell^2)}\;=\;Z^{1/4\,\mathrm{BPS}}_{\mathrm{CHL}\,N=1}(q,p,y)^{-1}.$$
Gritsenko-Nikulin 1998 *JRAM* 507 (BKM denominator); Borcherds 1998 (infinite product); Jatkar-Sen 2006 *JHEP* 04 (CHL). The K3 elliptic-genus Fourier coefficients $c_{\mathrm K3}(4nm-\ell^2)$ are simultaneously physical (BPS degeneracies) and arithmetic (Jacobi-form coefficients).

**Theorem (Twenty-four-ness, five-way convergence through named duality frames).**
$$\chi(\mathrm K3)=24=\#\{I_1\text{ fibres}\}=\#\{\text{F-theory }(p,q)\text{-7-branes}\}_{\text{IIB}}=\#\{\Omega_Y\text{-M5 on }I_1\text{ nodes}\}_{\text{twisted 11d SUGRA}}=c_{1/\Delta_5}(q^1).$$
Each equality holds in its own duality frame; adjacent equalities are related by named string dualities.
1. *Topological*: $\chi(\mathrm K3)=24$ (Hirzebruch 1966 *Topological Methods* Thm 6.3.1; signature on CY-2 with $b_2^+=3$).
2. *Algebraic-geometric*: $24=\#\{I_1\text{ fibres}\}$ on generic elliptic K3 (Kodaira 1963; Miranda 1989, $\chi_{\mathrm{top}}(I_1)=1$, discriminant of degree 24).
3. *IIB/F-theory frame*: 24 $(p,q)$-7-branes wrap the 24 $I_1$ fibres (Vafa 1996; Sen 1996/1997, RR tadpole $24=\chi(\mathrm K3)$). F-theory is IIB with 7-branes, NOT M5-branes.
4. *Twisted 11d SUGRA/CGP frame*: 24 $\Omega_Y$-holomorphic M5-branes wrap the 24 $I_1$ fibres on $\R^3\times\mathrm K3\times\C^2$ (Costello-Gaiotto-Paquette 2018 arXiv:1812.09257 §§3-4). This is M-theory with the $\Omega$-background twist, a distinct duality frame from F-theory. The two frames produce the same count because both are probed on the same elliptic K3 and related by M/F duality.
5. *Arithmetic (Borcherds)*: $c_{1/\Delta_5}(q^1)=24$ (Gritsenko 1999 *St Petersburg Math J* 11 Thm 6.1; 12 primitive polar triples $\times c_{\mathrm K3}(-1)=2$, Eichler-Zagier 1985 Thm 9.1 + Borcherds 1998).

**Scope correction.** The prior Master inscription "M5-branes in F-theory on K3" conflated two duality frames: F-theory has $(p,q)$-7-branes, not M5-branes; M5-branes appear in the orthogonal M-theory / twisted 11d SUGRA setup. Both duality frames produce count 24 on the same elliptic K3 via their respective brane content; the two frames are related by string duality, not by identification-in-place. The five-way equality above separates the frames explicitly. Twenty-four-ness remains the topological $\chi(\mathrm K3)$ signature of a CY-2 with $b_2^+=3$.

---

## Cycle 5 (Universal): Three-scale trace identity $\hbar^2 K=-1$

**Theorem (Three-scale universal trace identity).** On each $\Psi$-sibling row of the Vol III landscape, the identity
$$\hbar^2\cdot K\;=\;-1,\qquad K\;=\;2c_+(L),$$
holds with three simultaneous readings:
- **Microscopic (physics):** $\hbar^2=$ 6d holomorphic Chern-Simons BV-quantisation parameter on the CY-3 host (Costello 2011 *Renormalization and Effective Field Theory* §13.4; Costello-Francis-Gaiotto 2026 explicit identification).
- **Mesoscopic (arithmetic):** $K=2c_+(L)$ $=$ Heegner-Chern positive-signature class on the signature-$(2,n)$ input lattice of the Borcherds lift (Bruinier 2002 *LNM* 1780 Prop 5.1 Heegner-Chern reciprocity).
- **Macroscopic (physics $=$ math):** $-1=$ DVV 1997 modular-anomaly sign $=$ Virasoro central-charge sign (via $c_{\mathrm{ghost}}=-26$ halved) $=$ reflection-group determinant (Bruinier singular theta lift).

Borcherds singular theta lift (Borcherds 1998 *Invent Math* 132 Thm 1.7) forces the three scales to coincide.

**Row-canonical values:**
| Row | $L$ | $c_+$ reading | $K$ | $\hbar^2$ |
|---|---|---|---|---|
| Monster | $\mathrm{II}_{1,1}$ | Bruinier $(2,n)$ | $2$ | $-1/2$ |
| K3-BKM | $\Lambda^{2,1}_{\mathrm{II}}$ | Mukai/Humbert/Lusztig | $8$ | $-1/8$ |
| Fake-Monster | $\mathrm{II}_{25,1}$ | doubled Leech-rank | $50$ | $-1/50$ |
| Enriques | $E_8(-1)\oplus\mathrm{II}_{1,1}$ | Borisov-Libgober | $4$ | $-1/4$ |
| Conway-metap | $\Lambda_{24}^s$ super | super-extension | $2$ | $-1/2$ |

**Theorem (Three-faces convergence on K3).** On the K3 row, $K=8$ admits three independent route identifications: Mukai $2c_+(\mathrm{II}_{4,20})=2\cdot 4=8$ (Mukai 1988); Humbert local-monodromy order $8$ on $\mathcal L^{\Delta_5}|_{H_1}$ (Bruinier 2002); Lusztig reflection length $\ell=8$ for finite-dim $\mathfrak u_{\zeta_8}$ (Lusztig 1990/1993). The three converge because $\mathrm{Aut}^\circ(\mathrm K3\times E)=E$ has no $\mathbb G_m$-subtorus: the K-theoretic CoHA $(q_1,q_2)$-deformation collapses onto $q_1q_2=1$. K3's rigid hyperkähler-twistor-locus structure is the arithmetic origin of $K=8$.

---

## Cycle 6 (Three-volume synthesis): Two-stage factorisation square — scope-stratified by $d$

**Theorem/Conjecture (Two-stage factorisation square, scope-stratified).** In the $(\infty,1)$-category $\mathrm{PresStCat}_\infty$ of presentable stable symmetric-monoidal $(\infty,1)$-categories,
$$
\begin{array}{ccc}
\mathrm{CY}_d^{\mathrm{cat}} & \xrightarrow{\;\Phi^{\mathrm{FA}}_d\;} & \mathrm{Fact}^{\mathrm{hol}}_{E_d}(X) \\
\Phi_d\downarrow & & \downarrow \int_{\Sigma_{d-1}}\circ\,\mathrm{res}_C \\
\mathrm{Alg}_{E_1^{\mathrm{ch}}}(C) & =\!=\!= & \mathrm{Alg}_{E_1^{\mathrm{ch}}}(C)
\end{array}
$$
commutes **on its proved scope**:
- **$d\le 2$ (unconditional)**: $\Phi^{\mathrm{FA}}_2$ exists by CY-A$_2$ (`cy_to_chiral.tex`, $\mathbb S^2$-framed Kontsevich-Vlassopoulos); stage-2 specialisation via Ayala-Francis 2015 Thm 3.16. Square commutes on the nose.
- **$d=3$, toric/formal (unconditional)**: $\Phi^{\mathrm{FA}}_3$ exists by CY-A$_3$ (Theorem~\ref{thm:cy-to-chiral-d3}). Square commutes.
- **$d=3$, compact non-formal (conditional)**: $\Phi^{\mathrm{FA}}_3$ depends on convergence of the Čech-HTT series (`cy_to_chiral.tex:2802`); verified (Borel-summable) on quintic, bicubic, $\mathrm K3\times E$; open for generic compact non-formal CY-3.
- **CY-C identification (conjectural)**: the identification of $\Phi_3$-output with the Drinfeld double $G(X)=D(Y^+(X))$ of a BKM-type Hopf algebra is conjectural; 22 non-Leech Niemeier BKMs are explicit counterexamples to unconditional $\Psi$-surjectivity (`cy_to_chiral.tex:5091`).

- Top row (Vol III Stage-1 $\Phi^{\mathrm{FA}}_d$): canonical $E_d$-holomorphic factorisation algebra, pinned by Kontsevich-Tamarkin formality $\cap$ Costello-Gwilliam-Li locality (Willwacher 2014 Thm 1.2; Costello-Li 2016 Prop 5.2).
- Right column (Vol II Stage-2 $\int_{\Sigma_{d-1}}\circ\,\mathrm{res}_C$): factorisation-homology pushforward + reference-curve restriction (Ayala-Francis 2015 Thm 3.16).
- Bottom row (Vol I domain): $E_1$-chiral algebras on $C$ where Theorem A's adjunction $\Omega^{\mathrm{ch}}_C\dashv B^{\mathrm{ch}}_C$ lives (Beilinson-Drinfeld 2004 §3.4).

Theorems A, B, C, D, H on the bottom row transport along the square *within its proved scope*. The three-volume programme as "one commuting $(\infty,1)$-functor in three lenses" is a platonic ideal whose scope is precisely the CY-A$_{2,3}$ + CY-C-conjectural closure; outside this scope the transport is itself conjectural.

**Theorem (Family-of-shadows principle).** Every $X\in\mathrm{CY}_d^{\mathrm{cat}}$ determines a family $\mathrm{Shad}_X\colon\mathrm{CycCurve}(X)\to\mathrm{Alg}_{E_1^{\mathrm{ch}}}(\mathrm{SmCurve})$ of $E_1$-chiral shadows indexed by pairs $(\Sigma_{d-1}\hookrightarrow X,\, C\hookrightarrow\Sigma_{d-1})$. Physical reading: different T-duality frames for a single CY-$d$ compactification produce different 2d chiral algebras of BPS states on different reference curves. Mathematical reading: $\Phi_d$ is a family of functors parametrised by cycle-curve pairs, not a single functor. Theorem A governs each shadow individually.

For $X=\mathrm K3\times E$: varying the elliptic-fibration structure (Picard rank $\rho$) produces $\rho-1$ independent shadows, each a copy of $\mathbf H_{\Delta_5}$ on its own reference curve (permuted by $\mathrm O(\mathrm{NS}(\mathrm K3))$-Weyl).

---

## Master summary: ten cross-volume theorems (scope-stratified after round-2 audit)

1. **Averaging map $=$ $R$-matrix-twisted $\Sigma_n$-quotient** (full $E_1$ landscape); Bose-symmetrisation only on the pole-free $E_\infty$ subclass ($R=\tau$).
2. **Archetype $\supset$ canonical witness $\leftrightarrow$ particle-field labeling** (witness-indexed, not class-wise functorial equivalence); $\mathsf B$-class is a bound-state tower, not a single-particle type.
3. **$\kappa+\kappa^!=13$ via Feigin-Fuchs + BRST nilpotence** (Koszul involution $c\mapsto 26-c$; $Q^2=(c-26)c_0/12=0$ forces $c=26$).
4. **Genus obstruction $=$ Liouville anomaly** ($\mathrm{obs}_g=\kappa\lambda_g$, Polyakov 1981 + Mumford 1983).
5. **Hochschild $=$ conformal-family support** ($\{0,1,2,d\}$ on B-twisted CY-$d$).
6. **Deligne exceptional $=$ 6d hCS anomaly-free six-row spectrum**.
7. **Climax $Z_{3\mathrm{DQG}}=1/\Phi_{10}$** four-way equation (D1-D5-P, Igusa, Borcherds, Göttsche).
8. **Twenty-four-ness, five-way through named duality frames**: $\chi(\mathrm K3)=24=\#\{I_1\}=\#\{\text{F-theory 7-branes}\}_{\text{IIB}}=\#\{\Omega\text{-M5}\}_{\text{11d SUGRA}}=c_{1/\Delta_5}(q^1)$. F-theory and 11d SUGRA are distinct frames related by M/F duality.
9. **Three-scale trace $\hbar^2 K=-1$** per $\Psi$-sibling row with inscribed lattice.
10. **Two-stage factorisation square**: proved on $d\le 2$ + toric/formal $d=3$; conditional on Borel-summable compact $d=3$; CY-C = Drinfeld-double conjectural with 22 non-Leech Niemeier counterexamples.

These ten scope-stratified statements synthesise the round-2 Polyakov audit of the three-volume programme. The programme is not *one equation* — it is a scope-stratified scaffolding: chiral Koszul reflection across the $R$-matrix-twisted averaging map is *within its proved scope* one mathematical object viewed through three lenses (operadic, holographic, geometric); outside this scope the identifications remain conjectural and are inscribed as such.

**One-line statement.** The three-volume programme is the $R$-matrix-twisted chiral Koszul reflection whose derived-centre trace is $\hbar^2 K=-1$ on each $\Psi$-sibling row of the CY-A$_{2,3}$-provable + CY-C-conjectural closure of $\mathrm{CY}_d^{\mathrm{cat}}$; five independent physical-arithmetic identifications (averaging $=$ $R$-twisted symmetrisation; canonical witnesses $\leftrightarrow$ particle-field types; $\kappa+\kappa^!=13$ via Feigin-Fuchs + BRST; $\mathrm{obs}_g=$ Liouville anomaly; $\hbar^2 K=-1$ three-scale) force coherence on the proved scope.

---

*2026-04-22. Raeez Lorgat. Master cross-volume Polyakov cycles inscription.*
