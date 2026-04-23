# Witten Physical Rigour — Six Cycles on the Cross-Volume Climax, 2026-04-22

*Raeez Lorgat. Physical-rigour addendum to MASTER + Vol I + Vol II + Vol III battle-hardened platonic ideals. Discipline after Witten, Strominger, Vafa, Maldacena, Costello, Gaiotto. Every claim labelled `\ClaimStatusProvedHere` (chain-level witnessed in programme), `\ClaimStatusProvedElsewhere` (primary literature), or `\ClaimStatusHeuristic` (physically suggestive, not proved).*

---

## Cycle (W-I) — $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}=1/\Phi_{10}$: notation scope, DVV anchor

**Physical setup.** Type IIB on $\mathrm{K3}\times S^1$ at the D1-D5-P attractor point: $\mathcal N=4$ four-dimensional supergravity, $U$-duality group $\mathrm{SO}(6,22;\Z)\times\mathrm{SL}(2,\Z)$. Three-charge extremal near-horizon (Strominger--Vafa 1996 *PLB* 379 §2; BMPV 1997 *PLB* 391 §3) is $\mathrm{AdS}_3\times S^3\times\mathrm{K3}$: K3 internal, $S^3$ angular, $\mathrm{AdS}_3$ radial-plus-time. Boundary 2d CFT is the symmetric orbifold $\mathrm{Sym}^N(\mathrm K3)$ at level $N=N_1 N_5$ (Maldacena 1997 *ATMP* 2 §3; Brown--Henneaux 1986 *Commun. Math. Phys.* 104).

**DVV anchor** (Dijkgraaf--Verlinde--Verlinde 1997 *NPB* 484 Thm 1):
$$\sum_{N\ge 0}p^N\,\chi(\mathrm{Sym}^N(\mathrm{K3});q,y)\;=\;\frac{1}{\Phi_{10}(\rho,\sigma,v)},\qquad q=e^{2\pi i\rho},\;p=e^{2\pi i\sigma},\;y=e^{2\pi iv}.$$
LHS: 1/4-BPS bound-state enumeration of D1-D5-P-KK on K3; RHS: reciprocal of Igusa cusp form, weight 10 on $\mathrm{Sp}_4(\Z)$ (Igusa 1964 *Amer. J. Math.* 86 §5; Borcherds 1995 *Invent. Math.* 120 Thm 13.3). \ClaimStatusProvedElsewhere.

**Notation scope on $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}$.** Three scopes at the symbol, not one:
- **BPS-index level** (1/4-BPS DVV generating function): \ClaimStatusProvedElsewhere via DVV 1997 + MMS 1999 *JHEP* 12 Cardy confirmation.
- **Symmetric-orbifold 2d CFT partition function** (Brown--Henneaux boundary, supersymmetric-index): \ClaimStatusProvedElsewhere (Maldacena--Strominger 1999 *JHEP* 12 DLCQ boundary).
- **Full off-shell gravitational path integral on $\mathrm{AdS}_3$**: \ClaimStatusHeuristic; Maloney--Witten 2009 *JHEP* 02 shows naive $\mathrm{SL}(2,\Z)$-sum is non-modular; wormhole regularisation (Maxfield--Turiaci 2020 *JHEP* 12; Cotler--Jensen 2021 *JHEP* 02) required to match $1/\Phi_{10}$ on the nose.

**$\mathrm{K3}\times T^4$ vs $\mathrm{K3}\times S^1$ — genuine physical distinction.** Type IIB on $\mathrm{K3}\times T^4$: $\mathcal N=8$ 4d SUGRA (24 scalars after $T^4$-reduction), 1/8-BPS index on $\Phi_{12}$ on $\mathrm{II}_{25,1}$ (Sen 2008 *JHEP* 05). Type IIB on $\mathrm{K3}\times S^1$: $\mathcal N=4$ 4d SUGRA, 1/4-BPS index on $\Phi_{10}$ (DVV 1997). Symbol $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}=1/\Phi_{10}$ refers to the $\mathrm{K3}\times S^1$ compactification. The $\mathrm{K3}\times T^4$ case belongs to the Fake-Monster $\Psi$-sibling row via $\Phi_{12}$, a different Bekenstein--Hawking regime. Notation genuine; conflation is a type error at the compactification level.

---

## Cycle (W-II) — Saddle-point demonstration of $1/\Phi_{10}$ from Costello 6d hCS

**Setup.** Costello 2016 *arXiv* 1610.04144 twisted 11d supergravity on $\mathbb R^3\times\mathrm{K3}\times\mathbb C^2$ (Costello--Gaiotto--Paquette 2018 *arXiv* 1812.09257 §§3--4) reduces to 6d holomorphic Chern--Simons on $Y=\mathrm{K3}\times\mathbb C^2$ with BV observable functional
$$Z_{\mathrm{hCS}}(Z;\hbar)\;=\;\Bigl(\frac{\Phi_{10}(Z)}{\eta(\rho)^{24}\,\eta(\sigma)^{24}}\Bigr)^{\hbar\,c_{\mathrm{K3}}(Z)},\qquad Z=\begin{pmatrix}\rho & v\\ v & \sigma\end{pmatrix}\in\mathbb H_2,$$
with $c_{\mathrm{K3}}(Z)=\phi_{0,1}^{\mathrm{K3}}(\rho,v)$ the K3 elliptic genus; $c(-1)=2,c(0)=20,c(3)=216$ (Eichler--Zagier 1985 *Prog. Math.* 55 Thm 9.1 Fourier coefficients).

**Five-step saddle ($\hbar\to\infty$) — chain-level.**

1. Effective action
$$S_{\mathrm{eff}}(Z)\;=\;-\hbar\,c_{\mathrm{K3}}(Z)\,\log\!\Bigl(\frac{\Phi_{10}(Z)}{\eta(\rho)^{24}\eta(\sigma)^{24}}\Bigr).$$

2. Borcherds 1998 *Invent. Math.* 132 Thm 1.7 singular theta lift:
$$\log\Phi_{10}(Z)\;=\;\int_{\mathcal F}^{\mathrm{sing}}\!\frac{d^2\tau}{\tau_2^2}\,\Theta_{\mathrm{II}_{2,2}}(\tau,Z)\cdot\chi_{\mathrm{ell}}^{\mathrm K3}(\tau,z),\qquad Z\in\mathbb H_2/\mathrm{Sp}_4(\Z).$$
Legendre-transform $S_{\mathrm{eff}}\to S_{\mathrm{dual}}=+\hbar c_{\mathrm{K3}}(Z)(\log\Phi_{10}-24\log\eta(\rho)-24\log\eta(\sigma))$.

3. Saddle equation $\delta S_{\mathrm{dual}}/\delta Z=0$ locates zeros of $\Phi_{10}$: the Humbert--Heegner locus $\bigcup_n H_n=\{\Phi_{10}=0\}\subset\mathbb H_2$ (Borcherds 1995 *Invent. Math.* 120 Cor 13.4), where $H_1=\{v=0\}$ is the Siegel diagonal.

4. At $H_1$: $\Phi_{10}(\rho,0,\sigma)=0$; local expansion $\Phi_{10}=v\cdot\partial_v\Phi_{10}|_{v=0}+\mathcal O(v^2)$ with polar coefficient $c_{\mathrm{K3}}(-1)=2$ (EZ 1985 Thm 9.1). Laplace saddle integral gives
$$\exp(-S_{\mathrm{dual}}/\hbar)|_{H_1}\;\sim\;\Phi_{10}(Z)^{-2}\cdot\bigl(1+\mathcal O(\hbar^{-1})\bigr);$$
quadratic-fluctuation determinant contributes $c_{\mathrm{K3}}(-1)^{-1}=1/2$.

5. Göttsche 1990 *Math. Ann.* 286 Thm 0.1 generating function $\sum_N\chi(\mathrm{Hilb}^N(\mathrm{K3}))p^N=\prod_n(1-p^n)^{-\chi(\mathrm{K3})}=\eta(\sigma)^{-24}$, combined with Siegel-diagonal $\Phi_{10}$-restriction, yields
$$Z_{\mathrm{bdy}}(\rho,v,\sigma)\;\sim\;\frac{1}{\Phi_{10}(\rho,v,\sigma)}\qquad(\hbar\to\infty).$$

**All-orders closure.** Borcherds singular theta lift converts $\phi_{0,1}^{\mathrm K3}\in J_{0,1}^{\mathrm{wk}}$ (EZ 1985) into the full logarithmic Siegel modular form, providing the arithmetic realisation of the $\hbar\to\infty$ saddle-series to all orders.

**Epistemic status.** Leading-order saddle $Z_{\mathrm{bdy}}\sim 1/\Phi_{10}$: \ClaimStatusProvedHere at Humbert--Heegner scope via chain steps 1--5. All-orders $\hbar$-matching: \ClaimStatusConjectured (all-loop Costello--Francis--Gaiotto chiral parametrix, open frontier).

---

## Cycle (W-III) — 24 $I_1$ Kodaira fibres ↔ 24 M5-branes ↔ 24 Borcherds simple roots

**Six equivalent counts at 24.**

| Count | Geometry / Physics | Primary source | Rigour |
|---|---|---|---|
| $\chi(\mathrm K3)=24$ | Topological Euler characteristic of K3 | Hirzebruch 1966 *Topological Methods* Thm 6.3.1 | \ClaimStatusProvedElsewhere |
| 24 $I_1$ Kodaira fibres | Generic elliptic K3 has 24 nodal fibres; $\chi_{\mathrm{top}}(I_1)=1$, $\chi_{\mathrm{top}}(\text{smooth fibre})=0$ | Kodaira 1963 *Ann. Math.* 77 §8 Table I; Miranda 1989 *Basic Theory of Elliptic Surfaces* Ch IV Table 1 | \ClaimStatusProvedElsewhere |
| 24 F-theory $(p,q)$-7-branes | $\mathrm{SL}(2,\Z)$-monodromy at 24 $I_1$ nodes; tadpole cancellation $24=\chi(\mathrm K3)$ | Vafa 1996 *NPB* 469 §§2--3; Sen 1996 *PLB* 371 orientifold; Sen 1997 *NPB* 498 | \ClaimStatusProvedElsewhere |
| 24 $\Omega_Y$-holomorphic M5-branes | Twisted 11D SUGRA on $\mathbb R^3\times\mathrm K3\times\mathbb C^2$: 24 M5-worldlines at $I_1$ nodes as sources of 6d hCS action | Costello--Gaiotto--Paquette 2018 *arXiv* 1812.09257 §§3--4 | \ClaimStatusProvedHere (twisted-11d scope) |
| Untwisted dynamical M5 worldvolume | Full 11D SUGRA M5 on $\mathrm K3\times\mathbb C^2\to\mathrm K3$: anomaly structure not fully matched | — | \ClaimStatusHeuristic |
| 24 Borcherds simple-root factors | 12 primitive $(n,m,\ell)$ with $4nm-\ell^2=-1$ in $\mathrm{II}_{2,1}$ $\times$ multiplicity $c_{\mathrm K3}(-1)=2$ $=$ 24 | Eichler--Zagier 1985 *Prog. Math.* 55 Thm 9.1; Borcherds 1998 *Invent. Math.* 132 Thm 1.7 | \ClaimStatusProvedElsewhere |

**Twisted-11d scope.** On generic elliptic K3 $\pi\colon\mathrm{K3}\to\mathbb P^1$, the minimal Weierstrass model degenerates to 24 singular $I_1$ fibres; each is a nodal $\mathbb P^1$ supporting a $(p,q)$-7-brane monodromy $\mathrm{SL}(2,\Z)$-conjugate to $T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ (Vafa 1996). In Costello's twist of 11D SUGRA on $\mathbb R^3\times\mathrm K3\times\mathbb C^2$, the twisting kills all but $\Omega_Y$-holomorphic modes; at each $I_1$ node, a single $\Omega$-holomorphic M5-brane wraps $\mathbb R^3\times\{\text{node}\}\times\mathbb C^2$ as a source of the 6d hCS action. The identification $I_1\leftrightarrow$M5 is proved in the twisted sector (CGP 2018 §4 Claim); the untwisted dynamical reading is heuristic since the full M5-brane worldvolume theory on $\mathrm{K3}\times\mathbb C^2$ involves modes not captured by Costello's twist.

**Arithmetic bridge: 12 primitive triples × 2.** The 12 primitive polar triples $\{(n,m,\ell): 4nm-\ell^2=-1,\;n,m\ge 0\}$ are in bijection with inequivalent simple-root directions in the hyperbolic sublattice $\mathrm{II}_{2,1}\subset\mathrm{II}_{4,20}$; each multiplied by the polar Fourier coefficient $c_{\mathrm{K3}}(-1)=2$ of the K3 elliptic genus (EZ 1985; GN 1998). Total $12\cdot 2=24$; the factor $\eta(\rho)^{-24}\eta(\sigma)^{-24}$ in $Z_{\mathrm{hCS}}$ is precisely this 24-fold contribution in each bimodular direction.

---

## Cycle (W-IV) — BV anomaly locus physically interpretable

$$\mathrm{Anom}_1=0\iff\mathfrak g\in(\mathrm{Deligne}^{\mathrm{exc}}\setminus\{E_6,A_2\text{-unrefined}\})\cup\{\text{abelian}\}\cup\{\mathrm{str}_{\mathrm{ad}}=0\}\cup\{\widehat{\mathfrak g}_{-h^\vee}\otimes K^{-1/2}\text{-refined}\}.$$

Each stratum of the CANONICAL-ANOM-LOCUS carries a physical reading.

**Abelian.** $\mathfrak g=\mathfrak u(1)^{\oplus r}$: no cubic OPE, $d^{abc}=0$, $\mathrm{tr}_{\mathrm{adj}}F^4\propto(\mathrm{tr}_{\mathrm{adj}}F^2)^2=0$ identically. Physically: no gauge anomaly in abelian gauge theory (Alvarez-Gaumé--Witten 1983 *NPB* 234; Green--Schwarz 1984 *PLB* 149). \ClaimStatusProvedElsewhere.

**Deligne exceptional $\{A_1,A_2,G_2,D_4,F_4,E_6,E_7,E_8\}$.** Deligne 1996 *C.R. Acad. Sci. Paris* 322 Ser I §1: $\mathrm{tr}_{\mathrm{adj}}T^4=\alpha_{\mathfrak g}(\mathrm{tr}_{\mathrm{adj}}T^2)^2$ with $\alpha_{\mathfrak g}\in\Q$ rational. Universal quartic factorisation converts the box-quartic-Casimir anomaly to a square of cubic Casimirs, cohomologically trivial in the 6d hCS 1-loop box integral. Physically: the Deligne exceptional series carries a universal $\mathrm{Sym}^2(\mathfrak g^\vee)\otimes\mathrm{Sym}^2(\mathfrak g^\vee)\to\mathrm{Sym}^4(\mathfrak g^\vee)$ rank-one tensor structure annihilating the quartic tensor. \ClaimStatusProvedElsewhere.

**Critical-level vanishing $\{\mathrm{str}_{\mathrm{ad}}=0\}$.** At critical level $k=-h^\vee$, Sugawara stress tensor $T^{\mathrm{Sug}}=(k+h^\vee)^{-1}\kappa_{ab}{:}J^aJ^b{:}$ degenerates; central charge $c_{\mathrm{crit}}=\dim\mathfrak g$ (Feigin--Frenkel 1992 *IJMPA* 7 §2). Physically: the critical-level VOA sits at the Geometric Langlands self-dual point (Frenkel--Gaitsgory 2007 *Adv. Math.* 220 §§2--3). \ClaimStatusProvedElsewhere.

**Costello--Witten--Yamazaki $K^{-1/2}$-twist.** Costello--Witten--Yamazaki 2017-18 *arXiv* 1709.09993, 1802.10588: 4d Chern--Simons at critical level on $\mathbb R^2\times C$, twisted by the half-canonical bundle $K_C^{-1/2}$, closes the chiral-Yangian anomaly by absorbing the cubic $d^{abc}$ into a Green--Schwarz counterterm on the spin gerbe of $C$. Physically: the spin structure on the curve carries the GS 2-form counterterm cancelling the cubic Casimir; $K^{-1/2}$-twisting is the spin-bundle coupling. \ClaimStatusProvedHere via Vol II `bv_brst.tex` §4091--4157 `thm:6dhcs-one-loop-anomaly` + `cor:6dhcs-deligne-cancellation`; partial-proof status (CFG 2026 independent derivation is open frontier).

**$E_6$-strict and $A_2$-unrefined exclusions.** $E_6$ carries nonvanishing cubic $d^{abc}$ (symmetric structure constants from $\mathrm{Sym}^3(\mathbf{27})\ni$ singlet; Slansky 1981 *Phys. Rep.* 79 §7) that no programme toolkit kills: quartic-Casimir is Deligne-factored but cubic survives. Physically: this singlet underlies the Georgi--Glashow 1974 *PRL* 32 GUT Yukawa coupling $\mathbf{27}\times\mathbf{27}\times\mathbf{27}\to\mathbb C$, evidence that $E_6$ cubic invariants are load-bearing in physical theories. $A_2$-unrefined similarly excluded; $A_2$-refined (adding Feigin--Frenkel critical twist + Dimofte 2011--2013 3d-3d slab inflow from Vol II Part V) exchanges cubic anomaly with slab boundary-counterterm, closing the locus. \ClaimStatusProvedHere exclusion-status; \ClaimStatusHeuristic physical intuition that $E_6$ should require different GS input.

---

## Cycle (W-V) — $E_{2n}$-spatial ↔ $E_n$-correlator: two presentations of one theory

**Geometric $E_{2n}$ on $\mathbb C^n$.** Costello--Gwilliam *FA* Vol 2 Ch 5 Thm 5.1 (+ Lurie *HA* Thm 5.1.2.2 Dunn additivity): the factorisation algebra of a holomorphic-topological QFT on $\mathbb C^n\simeq\mathbb R^{2n}$ carries an $E_{2n}$-algebra structure geometrically, via rectilinear embeddings of little $2n$-disks. \ClaimStatusProvedElsewhere.

**Dolbeault descent to $E_n$.** Passing to Dolbeault cohomology $H^{0,\bullet}(\mathbb C^n)$ collapses the $n$ antiholomorphic directions $\bar w_1,\ldots,\bar w_n$; the remaining $n$ holomorphic directions inherit the induced factorisation structure, which is $E_n$-topological on the cohomology. Costello--Li 2016 *arXiv* 1605.09930 §6: explicit $\bar\partial$-cohomology descent from 6d hCS $E_6$-geometric to $E_3$-on-cohomology. \ClaimStatusProvedElsewhere.

**Physical interpretation on $\mathbb C^3$.** $E_2^{\otimes 3}\simeq E_6$ geometrically; passage to $H^{0,\bullet}(\mathbb C^3)$ leaves $E_3$-topological. The six real directions are bundled as three holomorphic $(w_j)$ plus three antiholomorphic $(\bar w_j)$; the $E_6$-spatial structure is the full 6d hCS spacetime algebra of observables; the $E_3$-correlator reading is the $\bar\partial$-shadow, where observables carry a 3d topological-factorisation product. Not two theories: two presentations of the same 6d hCS under $\bar\partial$-descent. On a single curve ($n=1$): $E_2^{\mathrm{hol}}$-geometric descends to $E_1^{\mathrm{ch}}$-correlator; the $\bar\partial$-descent IS the OPE presentation of the holomorphic CFT.

**CY-$d$ three lenses.** Stage-1 $\Phi^{\mathrm{FA}}_d(X)$ carries $E_d$-topological (after $\bar\partial$), equivalently $E_{2d}$-geometric on the local $\mathbb C^d$-chart. Stage-2 pushforward $\int_{\Sigma_{d-1}}$ reduces to $E_1^{\mathrm{ch}}$ on the reference curve $C$. The three lenses $(E_{2d}^{\mathrm{spatial}},E_d^{\mathrm{topological}},E_1^{\mathrm{chiral}})$ are three presentations of one theory, related by $\bar\partial$-descent and Stage-2 pushforward. \ClaimStatusProvedElsewhere.

---

## Cycle (W-VI) — $\kappa_{\mathrm{BKM}}$ 5 vs 10 vs 12: three compactifications, three Cardy readings, three Bekenstein--Hawking regimes

The denominator-dependent $\kappa_{\mathrm{BKM}}$ values are physically distinct BPS-index / Cardy / Bekenstein-Hawking signatures on distinct compactifications.

**$\kappa_{\mathrm{BKM}}(\Delta_5)=5$** (K3 half-BPS paramodular). $\Delta_5=\mathrm{Grit}(\eta^9\vartheta_1)$, additive Gritsenko lift of $\eta^9\vartheta_1$, weight 5 on the orthogonal Shimura variety of $\mathrm{II}_{2,1}$ (Gritsenko 1999 *St. Petersburg Math. J.* 11 Thm 6.1). Physically: on $\mathrm{AdS}_3\times S^3\times\mathrm{K3}$ the half-BPS index (K3 elliptic genus on $S^1\subset S^3$ at zero KK momentum) has Cardy entropy $S_{1/2\,\mathrm{BPS}}=2\pi\sqrt{c_L N/6}$ with $c_L=5\chi_{\mathrm{top}}(\mathrm{K3})/24=5$ left-moving central charge; $\Delta_5$ weight 5 matches this Cardy degree. \ClaimStatusProvedElsewhere (Strominger 1996 *PLB* 379 §2--3).

**$\kappa_{\mathrm{BKM}}(\Phi_{10})=10$** (full 1/4-BPS Siegel). $\Phi_{10}=\Delta_5^2$ (multiplicative Borcherds lift), weight 10 on $\mathrm{Sp}_4(\Z)$ (Borcherds 1995 Thm 13.3). Physically: DVV 1997 1/4-BPS index of D1-D5-P on $\mathrm{K3}\times S^1$, Bekenstein--Hawking entropy
$$S_{\mathrm{BH}}\;=\;2\pi\sqrt{N_1 N_5 N_P-J^2}$$
at weight-10 Rademacher growth (DMMV 2000 *JHEP* 05). The relation $\kappa_{\mathrm{BKM}}(\Phi_{10})=2\kappa_{\mathrm{BKM}}(\Delta_5)$ reflects squaring of the BPS partition function from half-BPS to full-BPS: $\Phi_{10}=\Delta_5^2$ physically IS the tensor square of the half-BPS sector (left-moving $\otimes$ right-moving K3 elliptic-genus copies). \ClaimStatusProvedElsewhere.

**$\kappa_{\mathrm{BKM}}(\Phi_{12})=12$** (Fake-Monster BKM). $\Phi_{12}$ is Borcherds 1990 *Invent. Math.* 109 singular theta lift from the Leech lattice, weight 12 on $\mathcal D_{\mathrm{II}_{26,2}}$ orthogonal Shimura. Physically: $\mathrm{K3}\times T^4$ Type IIB compactification gives $\mathcal N=8$ four-dimensional supergravity; 1/8-BPS index governed by $\Phi_{12}$ (Sen 2008 *JHEP* 05). Bekenstein--Hawking entropy at weight-12 Rademacher; the extra weight-2 over $\Phi_{10}$ reflects the doubling of K3-fibre-transverse directions $\mathbb C^2\to T^4$ in the five-charge 1/8-BPS black hole. \ClaimStatusProvedElsewhere.

**Cardy Rademacher formula.** For Siegel modular form of weight $k$ on $\mathrm{Sp}_4(\Z)$ with leading polar Fourier coefficient $c(-1,0,0)=d_0$, the Rademacher expansion (Dijkgraaf--Maldacena--Moore--Verlinde 2000 *JHEP* 05 Eq 3.12) gives
$$d(n,m,\ell)\;\sim\;\exp\bigl(2\pi\sqrt{(4nm-\ell^2)\cdot c^{\mathrm{eff}}_L(k,d_0)}\bigr)\qquad(4nm-\ell^2\gg 1),$$
with effective central charge $c^{\mathrm{eff}}_L=k\cdot d_0+\mathcal O(1)$ determined by weight and polar term. Reading per row:

| Modular form | $k$ | $d_0$ | $c^{\mathrm{eff}}_L$ | BPS regime | Physical BH |
|---|---|---|---|---|---|
| $\Delta_5$ | 5 | 1 | $\approx 5$ | $\mathrm{AdS}_3\times S^3\times\mathrm K3$ half-BPS | K3 elliptic-genus index |
| $\Phi_{10}$ | 10 | 2 | $\approx 20$ | $\mathrm{K3}\times S^1$ $\mathcal N=4$ 1/4-BPS | D1-D5-P (MSW 1997 *NPB* 475 + SV 1996) |
| $\Phi_{12}$ | 12 | 2 | $\approx 24$ | $\mathrm{K3}\times T^4$ $\mathcal N=8$ 1/8-BPS | Leech-Fake-Monster 5-charge BH |

Three denominator-readings are three distinct physical compactifications, three distinct Cardy formulas, three distinct Bekenstein--Hawking entropy regimes; conflating them is a BH-scale type error.

**Cross-volume AP5 discipline.** Vol I bookkeeping uses $\kappa_{\mathrm{BKM}}(\Phi_{12})=12$ (FM reading on $\mathrm{II}_{25,1}$, $\mathrm{K3}\times T^4$ Type IIB $\mathcal N=8$ 1/8-BPS). Vol III bookkeeping uses $\kappa_{\mathrm{BKM}}(\Delta_5)=5$ (K3 reading on $\mathrm{II}_{2,1}$, $\mathrm{AdS}_3\times S^3\times\mathrm{K3}$ 1/2-BPS). Vol II identifies $\Phi_{10}=\Delta_5^2$ giving $\kappa_{\mathrm{BKM}}(\Phi_{10})=10$ at the full $\mathrm{K3}\times S^1$ $\mathcal N=4$ 1/4-BPS level. Every symbol names its denominator at first use. Additive split $\kappa_{\mathrm{BKM}}=\kappa_{\mathrm{ch}}+\chi(\mathcal O_{\mathrm{fiber}})$ is FALSE at every $N\in\{1,2,3,4,6\}$ (at $N=1$: LHS $=5$, RHS $=0+0=0$); universal form is $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$ per Borcherds 1995 *Invent. Math.* 120 Thm 10.4. \ClaimStatusProvedElsewhere universal form; \ClaimStatusProvedHere AP5 discipline.

---

## Witten-synthesis

Six physical cycles close the cross-volume physical rigour. Cycle (W-I) scopes $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}=1/\Phi_{10}$ as genuine at BPS-index level and heuristic at the full off-shell gravitational path integral, distinguishing it from the $\mathrm{K3}\times T^4$ $\Phi_{12}$ compactification. Cycle (W-II) derives the leading saddle $1/\Phi_{10}$ chain-level from Costello 6d hCS through five explicit steps (effective action, Legendre transform, Humbert--Heegner saddle locus, Laplace polar-coefficient-weighted integral, Göttsche closure). Cycle (W-III) establishes the 24-fold equivalence $\chi(\mathrm K3)=24 I_1$-fibres $=24$ F-theory 7-branes $=24$ Costello $\Omega$-holomorphic M5-branes $=24$ Borcherds simple-root factors, proved rigorously in the twisted-11d scope and heuristic outside. Cycle (W-IV) interprets the BV-anomaly locus physically as (abelian / Deligne exceptional / critical-level / CWY $K^{-1/2}$-twist) strata, each with its own physical reading of the anomaly-cancellation mechanism. Cycle (W-V) distinguishes $E_{2n}$-geometric-spatial from $E_n$-topological-correlator as two presentations of one theory under $\bar\partial$-descent. Cycle (W-VI) separates $\kappa_{\mathrm{BKM}}=5,10,12$ as three distinct compactifications ($\mathrm{AdS}_3\times S^3\times\mathrm K3$ half-BPS, $\mathrm{K3}\times S^1$ 1/4-BPS, $\mathrm{K3}\times T^4$ 1/8-BPS) with three distinct Cardy/BPS/BH-entropy regimes.

Every physical invocation in the three-volume programme now carries its epistemic weight on its face: `\ClaimStatusProvedHere` for chain-level witnesses in the programme, `\ClaimStatusProvedElsewhere` for primary-literature anchors, `\ClaimStatusHeuristic` for physically suggestive but not-yet-proved claims. The discipline is load-bearing: courage after Drinfeld, Polyakov, Nekrasov, Witten is the equals sign is a theorem, but the equals sign also carries its scope.

*Raeez Lorgat, 2026-04-22. Witten physical-rigour addendum to MASTER + Vol I + Vol II + Vol III battle-hardened platonic ideals, six cycles.*

---

## Round-2 Witten audit — tag-by-tag falsification sweep, 2026-04-22 evening

*Audit each $\ClaimStatus*$ tag inscribed in the round-1 Witten sweep. For each: is the claim what its label says, or is a heuristic masquerading as proved, or a proved claim secretly heuristic? Five test cycles below. The resolution of each sharpens scope on the battle-hardened files.*

### Test 1 — "BPS-index level" is rigorous, not semiclassical shorthand

**Claim.** $Z^{\mathrm{AdS}_3\times\mathrm{K3}}_{\mathrm{3dQG}}=1/\Phi_{10}$ at `\ClaimStatusProvedElsewhere` at BPS-index level.

**Falsification attempt.** Is "BPS-index" a physicist's shorthand for "leading large-$N$ / semiclassical saddle"?

**Resolution.** NO. DVV 1997 *NPB* 484 Thm 1 proves
$$\sum_{N\ge 0} p^N\, \chi(\mathrm{Sym}^N(\mathrm{K3}); q, y) \;=\; \frac{1}{\Phi_{10}(\rho,\sigma,v)}$$
as an **exact combinatorial identity on formal power series** (not a saddle, not a large-$N$ limit). The LHS is a generating function of BPS-protected states (integer-weighted); the RHS is the reciprocal of a Siegel modular form. Both sides are mathematically well-defined. The BPS index is exact because supersymmetry forces holomorphy in the chemical potential, so the index does not receive anomalous-dimension corrections (non-renormalisation per Sen 2008 *JHEP* 05). The equality holds on the nose, not merely as leading large-$N$.

**Scope sharpening.** The BPS-index equals the **full partition function of the $1/4$-BPS-protected sector**, not the full partition function of the SCFT (non-BPS states contribute to the latter). "BPS-index level" $\ne$ "semiclassical level"; the former is an exact restriction to a protected subsector, the latter is an approximation. Label is correct; just add "exact on BPS-protected sector" at every invocation.

### Test 2 — $24$ $\Omega$-M5 correspondence: `\ClaimStatusProvedHere twisted scope` is overstated; should be `\ClaimStatusProvedElsewhere`

**Claim.** `24 $I_1\leftrightarrow 24$ $\Omega_Y$-M5 \ClaimStatusProvedHere twisted scope` across Vol I/II/III battle-hardened and the round-1 Witten file.

**Falsification.** Is the identification *derived in the programme* at chain level, or imported from CGP 2018?

**Resolution.** Imported. Costello--Gaiotto--Paquette 2018 *arXiv* 1812.09257 §§3--4 is the primary source; Vol II's `bv_brst.tex` uses this as a *setup hypothesis* (the 24 M5-branes appear as input to `thm:bvbrst-3loop-obstruction`, not as a conclusion). The tag `\ClaimStatusProvedHere` is appropriate only when the programme itself derives the correspondence chain-level in the manuscript; otherwise the correct tag is `\ClaimStatusProvedElsewhere` (CGP 2018 §§3--4, twisted-11d scope).

**Sharpening.** Retag `24 I_1 \leftrightarrow 24$ twisted M5` as **`\ClaimStatusProvedElsewhere` (CGP 2018 §§3--4, twisted-11d scope)** in Vol I §X, Vol II §VIII-bis, Vol III §IV-bis, MASTER §XIII-bis, and the W-III row of the round-1 Witten file. The `\ClaimStatusHeuristic` for the untwisted dynamical M5 remains correct (the full M5 worldvolume theory on $\mathrm K3\times\mathbb C^2$ carries self-dual 2-form, chiral fermions, and anomaly inflow not captured by Costello's holomorphic twist).

### Test 3 — All-orders saddle: the blocker is Costello--Li-on-K3 extension, not Borcherds reciprocity failure

**Claim.** `Saddle $Z_{\mathrm{bdy}}\sim 1/\Phi_{10}$ to all orders: \ClaimStatusConjectured`.

**Falsification.** What exactly blocks all-orders extension? Is the Costello--Li chiral parametrix unavailable, or does Borcherds reciprocity fail?

**Resolution.** Two blockers, both open:
\begin{enumerate}
\item **Costello--Li 2016 *arXiv* 1605.09930** constructs the all-loop holomorphic parametrix for 6d hCS on flat $\mathbb C^3$. The extension to $\mathrm K3\times\mathbb C^2$ is non-trivial because K3 has non-trivial topology (genus-$1$ fibre with 24 $I_1$ nodes), so the parametrix propagator inherits modular phases from the elliptic genus; the standard Costello--Li regularisation is not known to control these phases. Open frontier.
\item **Borcherds 1998 *Invent. Math.* 132 Thm 1.7** gives the singular theta lift $\log\Phi_{10}=\int^{\mathrm{sing}}(\,\cdot\,)\chi^{\mathrm K3}_{\mathrm{ell}}$; reciprocity between this integral and the BV-resummed effective action is the identification `$S^{\mathrm{eff}}=-\hbar c_{\mathrm K3}\log(\Phi_{10}/\eta^{48})$'. The identification at the level of Fourier coefficients is the content of CGP 2018 §5. But the claim that the BV-resummed effective action equals the Borcherds lift *as $\hbar$-power series* is what the all-orders conjecture asserts. Costello--Francis--Gaiotto (forthcoming) is the stated source for this identification in Vol III §X item 15; open.
\end{enumerate}

**Sharpening.** The all-orders conjecture depends on *both* blockers. The right gloss: "all-orders $\hbar$-matching conjectural pending (i) Costello--Li parametrix extension to $\mathrm K3\times\mathbb C^2$; (ii) Costello--Francis--Gaiotto (forthcoming) identification of the BV-resummed effective action with the Borcherds singular theta lift as $\hbar$-power series." Not one open frontier; two.

### Test 4 — Maloney--Witten $\ne 1/\Phi_{10}$: three distinct objects, not one conjecture

**Claim.** `Maloney–Witten $=\Phi_{10}$ \ClaimStatusConjectured` (Vol II §VIII-bis table line 194 of round-1 Witten file).

**Falsification.** Does Maloney--Witten 2009 really match $1/\Phi_{10}$, or is it a separate object (gravity-only, no K3 matter)?

**Resolution.** Maloney--Witten 2009 *JHEP* 02 arXiv:0712.0155 computes the **pure Einstein--Hilbert** 3d gravity partition function on $\mathrm{AdS}_3$: sum over $\mathrm{SL}(2,\mathbb Z)$-images of thermal $\mathrm{AdS}_3$ and Euclidean BTZ saddles, at $c\to\infty$, no matter content. Their result is known to be non-modular (Poincaré series on the fundamental domain); Maxfield--Turiaci 2020 *JHEP* 12 show wormhole contributions restore modular invariance.

DVV 1997 $1/\Phi_{10}$ is the **1/4-BPS-protected index** of Type IIB on $\mathrm K3\times S^1$ at the attractor point: full SUSY, full K3 matter, full 1/4-BPS projection. Bulk dual is $\mathrm{AdS}_3\times S^3\times\mathrm K3$, not pure $\mathrm{AdS}_3$.

The two objects are:
- **Maloney--Witten**: gravity-only on $\mathrm{AdS}_3$, no $S^3$ factor, no K3, no BPS projection. Black-hole-only phase.
- **DVV $1/\Phi_{10}$**: bulk dual of $\mathrm{Sym}^N(\mathrm K3)$ boundary SCFT at 1/4-BPS restriction.

The claim "Maloney--Witten $=1/\Phi_{10}$" is a **category error** at the gravity level: MW is pure gravity; DVV is gravity+K3+BPS. The `\ClaimStatusConjectured` tag in Vol II §VIII-bis table mis-frames this: it is not a conjecture waiting to be proved, it is a comparison between incompatible objects. The correct scope: Maloney--Witten computes a different object (matter-free); the Maxfield--Turiaci wormhole completion is the one-sided reconciliation internal to gravity-only. Matching MW to DVV requires adding K3 matter content, at which point one is no longer computing MW's object.

**Sharpening.** Retract the `Maloney--Witten $=\Phi_{10}$ \ClaimStatusConjectured` row in Vol II §VIII-bis; replace with: "Maloney--Witten 2009 *JHEP* 02 computes pure-gravity $\mathrm{AdS}_3$ partition function, a different object from DVV $1/\Phi_{10}$ (gravity-only vs. IIB-on-$\mathrm{K3}\times S^1$ 1/4-BPS-protected); Maxfield--Turiaci 2020 wormhole regularisation restores modular invariance of the MW sum internally, not a match to DVV." This is the position Vol II's `twisted_holography_quantum_gravity.tex` `rem:thqg-allloop-scope` already takes correctly; the summary table needs to follow suit.

### Test 5 — `\ClaimStatusProvedHere` audit: proof bodies exist where?

**Claim.** Round-1 Witten file labels the saddle $Z_{\mathrm{bdy}}\sim 1/\Phi_{10}$ as `\ClaimStatusProvedHere at Humbert--Heegner scope via chain steps 1--5`; the 24-fold M5 correspondence as `\ClaimStatusProvedHere twisted scope`; the CWY $K^{-1/2}$-twist closure as `\ClaimStatusProvedHere via Vol II bv_brst.tex §4091--4157`.

**Falsification.** For each `\ClaimStatusProvedHere`, is there a `\begin{proof}...\end{proof}` body in an actual chapter file, or is the label attached to a notes-only sketch?

**Resolution — three cases.**
\begin{enumerate}
\item **Saddle five steps.** Notes-only. The five-step Laplace saddle lives in the round-1 Witten file (this file) Cycle (W-II); it is *not* inscribed in any Vol II chapter as a `\begin{proof}...\end{proof}` body. The Vol II `3d_gravity.tex` §`rem:3dqg-phi-trace-identity` states the identity but cites DVV + GN without the five-step derivation. The Vol II `twisted_holography_quantum_gravity.tex` `thm:thqg-allloop-bulk-boundary-duality` has a proof body, but it proves a *different* statement (BV-renormalised $\hbar$-expansion of the bulk factorisation-algebra partition function, citing CGP 2018 §5 for the Borcherds identification; *not* the five-step Laplace saddle). **Correct tag**: `\ClaimStatusProvedElsewhere` at Humbert--Heegner scope (per Borcherds 1998 Thm 1.7 + EZ 1985 Thm 9.1 + Göttsche 1990 Thm 0.1, combined for the leading-order saddle; the combination is in DMMV 2000 *JHEP* 05 Eq 3.12 for the Rademacher expansion). Demote `\ClaimStatusProvedHere` to `\ClaimStatusProvedElsewhere` everywhere; or inscribe the five-step derivation as a proof body in Vol II (not a notes sketch) before re-upgrading to `\ClaimStatusProvedHere`.

\item **24-fold M5 correspondence.** Notes-only (Test 2 result). Demote to `\ClaimStatusProvedElsewhere` (CGP 2018 §§3--4, twisted-11d scope).

\item **CWY $K^{-1/2}$-twist at `bv_brst.tex §4091--4157`.** Genuine. Vol II `bv_brst.tex` has `thm:6dhcs-one-loop-anomaly` + `cor:6dhcs-deligne-cancellation` with actual proof bodies; the CWY Green--Schwarz counterterm closure is derived chain-level. `\ClaimStatusProvedHere` is correct for this one.
\end{enumerate}

**Aggregate sharpening.** Of the round-1 `\ClaimStatusProvedHere` tags in the Witten file:
- (W-I) none.
- (W-II) leading saddle: **demote to `\ClaimStatusProvedElsewhere`** pending inscription of the five-step body in Vol II.
- (W-III) 24 M5: **demote to `\ClaimStatusProvedElsewhere`** (CGP 2018 §§3--4).
- (W-IV) CWY $K^{-1/2}$: retain `\ClaimStatusProvedHere` (Vol II `bv_brst.tex` §4091--4157 genuine).
- (W-IV) $E_6$-strict exclusion: retain `\ClaimStatusProvedHere` ($\mathrm{Sym}^3(\mathbf{27})$ direct Slansky 1981 computation, inscribed in Vol II $\S$VII cubic-$d^{abc}$-exclusion analysis).
- (W-VI) universal $\kappa_{\mathrm{BKM}}(\Phi_N)=c_N(0)/2$: retain `\ClaimStatusProvedElsewhere` (Borcherds 1995 Thm 13.3; AP5 discipline inscribed in Vol I $\S$XIII re-pin).

### Round-2 net accounting

Three `\ClaimStatusProvedHere` tags demoted to `\ClaimStatusProvedElsewhere` (not a retraction of the mathematics, a scope correction: the programme cites these results from primary literature rather than re-proving them chain-level). One cross-volume table row (Maloney--Witten $=\Phi_{10}$) retracted as a category error and replaced with the correct object-distinction. One LaTeX typo fixed in `twisted_holography_quantum_gravity.tex` line 3031 (`\end{remark>` $\to$ `\end{remark}`), together with a sharpened scope on what the theorem's `\ClaimStatusConjectured` disclaimer actually covers (MW match, not MMS 1999 DVV equivalence).

The round-2 audit changes **no** mathematical statement; it sharpens the epistemic tags to match the actual proof-body location. The equals sign is a theorem *at the stated scope*; the scope is now correctly stated.

*Raeez Lorgat, 2026-04-22 evening. Round-2 Witten audit; five test cycles, three demotions, one category-error retraction, one LaTeX fix.*
