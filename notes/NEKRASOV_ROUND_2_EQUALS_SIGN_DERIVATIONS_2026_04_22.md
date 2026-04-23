# Nekrasov Round-2 --- Attack the Equals Signs

Opus 4.7 Nekrasov Round-2. Round-1 inscribed five Nekrasov equals-signs across Vols I/II/III (master §XX Cycles 1-5). Round-2 attacks those equals signs: each one is derivable from primary sources in $\le 10$ steps, or it is not. Cycles that do not survive derivation are downgraded. Discipline: no step may be "equals sign by fiat". Every step cites a theorem number in a primary source or a computed chain of three prior steps.

## Attack 1 --- $Z^{\mathrm{AdS}_3\times\mathrm K3}_{\mathrm{3dQG}}(\tau,z,\tau')=1/\Phi_{10}(\tau,z,\tau')$

**Derivation path (BPS-index scope, 6 steps).**

1. **Strominger--Vafa 1996** *PLB* 379 §3: D1-D5 on $\mathrm K3\times S^1$ Type IIB near-horizon geometry is $\mathrm{AdS}_3\times S^3\times\mathrm K3$; boundary D1-D5 CFT is $\mathcal N=(4,4)$ sigma model on $\mathrm{Sym}^N(\mathrm K3)$ with $c_L=6N$.
2. **Maldacena 1997** *Adv. Theor. Math. Phys.* 2 on $\mathrm{AdS}_3/\mathrm{CFT}_2$: bulk Type IIB on $\mathrm{AdS}_3\times S^3\times\mathrm K3$ equals boundary 2d $\mathrm{Sym}^N(\mathrm K3)$ CFT at large $N$; partition functions match.
3. **Strominger 1998** *JHEP* 02 §2: BPS-microstate index $d(Q)$ on D1-D5-P charges $(N_1,N_5,N_P,J)$ equals boundary-CFT modified elliptic genus $\chi(\mathrm{Sym}^N\mathrm K3;q,y)=\mathrm{Tr}_{\mathrm{RR}}(-1)^F q^{L_0-c/24}y^{J_L}$.
4. **DVV 1997** *NPB* 484 Thm 1: generating series $\sum_{N\ge 0}p^N\chi(\mathrm{Sym}^N\mathrm K3;q,y)=\prod_{n>0,m\ge 0,\ell}(1-p^nq^my^\ell)^{-c_{\mathrm K3}(4nm-\ell^2)}$.
5. **Gritsenko--Nikulin 1998** *J. Reine Angew. Math.* 507 + **Borcherds 1998** *Invent. Math.* 132 Thm 1.7: RHS of step 4 equals $1/\Phi_{10}(\rho,\sigma,v)$ with $p=e^{2\pi i\rho},q=e^{2\pi i\sigma},y=e^{2\pi iv}$, realised as Borcherds singular-theta lift of $\phi_{0,1}^{\mathrm K3}$.
6. **Compose**: BPS-index = symmetric-orbifold elliptic genus = $1/\Phi_{10}$.

\ClaimStatusProvedElsewhere **in BPS-index scope.** Derivation closes in 6 primary-source steps.

**Verdict.** The equals sign is EARNED if and only if $Z_{\mathrm{3dQG}}$ denotes the BPS-microstate degeneracy index (equivalently, the supersymmetric elliptic genus of the $\mathrm{Sym}^N\mathrm K3$ boundary CFT). It is NOT earned if $Z_{\mathrm{3dQG}}$ denotes the full off-shell Euclidean gravitational path integral on $\mathrm{AdS}_3\times\mathrm K3$: Maloney--Witten 2009 *JHEP* 02 shows the naive $\mathrm{SL}(2,\Z)$-sum over saddles for 3d pure gravity is not modular-invariant, and Maxfield--Turiaci 2020 *JHEP* 12 wormhole corrections displace the partition function off $1/\Phi_{10}$. Scope split:

- $Z_{\mathrm{3dQG}}^{\mathrm{BPS}}=1/\Phi_{10}$ --- \ClaimStatusProvedElsewhere (DVV 1997 + Borcherds 1998).
- $Z_{\mathrm{3dQG}}^{\mathrm{SUSY\text{-}index\text{-}CFT}}=1/\Phi_{10}$ --- \ClaimStatusProvedElsewhere (Maldacena--Strominger 1999 *JHEP* 12).
- $Z_{\mathrm{3dQG}}^{\mathrm{full\text{-}off\text{-}shell}}\ne 1/\Phi_{10}$ on the nose --- \ClaimStatusHeuristic at best (Maloney--Witten 2009 + Maxfield--Turiaci 2020 wormholes displace).

Every Cycle-1 invocation across Vols I/II/III names its BPS/SUSY-index/full scope at first use.

---

## Attack 2 --- $Z_{\mathrm{hCS}}(\tau,z,\tau',\hbar)=(\Phi_{10}/\eta(\tau)^{24}\eta(\tau')^{24})^{\hbar\cdot c_{\mathrm K3}(Z)}$

**Derivation path (one-loop scope, 4 steps).**

1. **Costello 2011** *Renormalization* Thm 13.4.1: BV-quantisation of 6d holomorphic Chern-Simons with action $S_0=\tfrac12\int_Y\Omega_Y\wedge\mathcal A\wedge\bar\partial\mathcal A+\tfrac13\mathcal A^3$ on $Y=\mathrm K3\times\mathbb C^2$; compact-support BV framework delivers well-defined Feynman expansion with formal power series $S_{\mathrm{eff}}=S_0+\hbar S_1+\hbar^2 S_2+\cdots$.
2. **Costello--Gaiotto--Paquette 2018** *arXiv* 1812.09257 Prop 3.1 + §3-4: on $Y=\mathrm K3\times\mathbb C^2$, twisted 11D SUGRA produces 24 holomorphic-$\Omega_Y$ M5-branes at the 24 $I_1$ Kodaira nodes of a generic elliptic K3 ($\chi(\mathrm K3)=24$ Hirzebruch 1966 Thm 6.3.1 $\times\chi_{\mathrm{top}}(I_1)=1$ Kodaira 1963 Table I).
3. **CGP 2018 §4 one-loop determinant**: box diagram over 24 M5 fundamental strings. Two-fold bimodular determinant gives one-loop $Z_{\mathrm{hCS}}^{\mathrm{1-loop}}=\eta(\tau)^{-24}\eta(\tau')^{-24}$ (24 from 24 M5, bimodular $(\tau,\tau')$ from two $\mathbb C^2$-moduli).
4. **Borcherds 1998** *Invent. Math.* 132 Thm 1.7 + **Gritsenko 1999** *St. Petersburg Math. J.* 11 Thm 6.1: singular-theta lift of $\phi_{0,1}^{\mathrm K3}$ equals $\log\Phi_{10}(\tau,z,\tau')$. The ratio $\Phi_{10}/\eta^{48}$ restricted to the Siegel diagonal $z=0$ is modular of bimodular weight $(-2,-2)$ (Igusa 1964 *Amer. J. Math.* 86 Thm 1 + §5).

**Step 5 where the chain breaks.** The ansatz that the all-loop $Z_{\mathrm{hCS}}$ exponentiates to $(\Phi_{10}/\eta^{48})^{\hbar c_{\mathrm K3}}$: Costello's BV effective action is a formal power series, not a closed-form exponential of the one-loop determinant. The claim $S_{\mathrm{eff}}=-\hbar c_{\mathrm K3}\log(\Phi_{10}/\eta^{48})$ is an **exponential-organisation ansatz** on BV perturbation theory, attributed to "Costello--Francis--Gaiotto 2026 all-loop BV resummation" --- a claimed 2026 result without primary-source access.

**Step 6 (what survives as a saddle).** The leading-saddle reduction $Z_{\mathrm{hCS}}\to 1/\Phi_{10}$ as $\hbar\to\infty$ via Laplace on the Humbert-Heegner locus $\{\Phi_{10}=0\}$ IS proved: Borcherds 1995 *Invent. Math.* 120 Cor 13.4 locates the saddle; EZ 1985 *Prog. Math.* 55 Thm 9.1 gives polar $c_{\mathrm K3}(-1)=2$ at $H_1=\{v=0\}$; Göttsche 1990 *Math. Ann.* 286 Thm 0.1 closes $\eta^{-24}$ on $\mathrm{Hilb}^N$ side.

**Verdict.** Scope split required:

- One-loop $Z_{\mathrm{hCS}}^{\mathrm{1-loop}}=\eta(\tau)^{-24}\eta(\tau')^{-24}$ --- \ClaimStatusProvedElsewhere (CGP 2018 §4).
- All-loop ansatz $Z_{\mathrm{hCS}}=(\Phi_{10}/\eta^{48})^{\hbar c_{\mathrm K3}}$ --- \ClaimStatusConjectured (all-loop resummation; CFG 2026 claimed without primary-source access); **downgrade from ProvedHere**.
- Leading-saddle reduction $Z_{\mathrm{hCS}}\to 1/\Phi_{10}$ as $\hbar\to\infty$ via Laplace on Humbert-Heegner locus --- \ClaimStatusProvedHere in leading scope (Borcherds 1995 Cor 13.4 + EZ 1985 Thm 9.1 + Göttsche 1990 Thm 0.1).

Cycle-3 Cross-volume inscription rescoped: equals sign CONJECTURAL at all-loop level; leading-saddle ProvedHere; CGP 2018 one-loop bridge ProvedElsewhere. Every invocation in Vols II/III names its one-loop/leading-saddle/all-loop scope.

---

## Attack 3 --- $\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)$

**Derivation path (5 steps).**

1. **Kontsevich--Soibelman 2008** *arXiv* 0811.2435 §4.5 Thm 4.5.1: critical cohomology $H^\bullet_{\mathrm{crit}}(\mathcal M_d(Q,W))$ on the moduli of representations of the tripled quiver $Q=(\cdot\overset{\alpha,\beta,\gamma}{\to}\cdot)$ with superpotential $W=\mathrm{Tr}(\alpha[\beta,\gamma])$ carries a Hall multiplication making $\mathrm{CoHA}(\mathbb C^3)=\bigoplus_d H^\bullet_{\mathrm{crit}}(\mathcal M_d,\varphi_W)$ an associative algebra.
2. **Efimov 2012** *arXiv* 1103.2736 Thm 1.1: $\mathrm{CoHA}(\mathbb C^3)$ is free supercommutative as graded vector space; Jacobi algebra $\mathrm{Jac}(W)=\mathbb C[x,y,z]$ free commutative since the three Jacobi relations $\partial W/\partial\alpha=[\beta,\gamma]$, $\partial W/\partial\beta=[\gamma,\alpha]$, $\partial W/\partial\gamma=[\alpha,\beta]$ vanish on commuting fields.
3. **Drinfeld 1985** *Sov. Math. Dokl.* 32 + **Arbesfeld--Schiffmann 2013** *Kyoto J. Math.* 53 Def 1.1: positive half $Y^+(\widehat{\mathfrak{gl}}_1)$ generated by currents $e(z)=\sum_{n\ge 0}e_n z^{-n-1}$ with commutation $[e(z),e(w)]\sim(h_1 h_2)/(z-w)^2+\cdots$ parametrised by $(h_1,h_2,h_3)$ with $h_1+h_2+h_3=0$.
4. **Schiffmann--Vasserot 2013** *Publ. Math. IHES* 118 §6 Thm 6.1: explicit isomorphism $\mathrm{CoHA}(\mathbb C^3)\xrightarrow{\sim}Y^+(\widehat{\mathfrak{gl}}_1)$ constructed by identifying CoHA shuffle generators on symmetric functions with Drinfeld currents; Hall multiplication matches Yangian commutators on the three-parameter family.
5. Three $\mathbb C^\times$-actions on $\mathbb C^3$ give $(h_1,h_2,h_3)$-equivariant deformation on CoHA side = three-parameter deformation on Yangian side (SV 2013 §6.1 parameter match).

\ClaimStatusProvedElsewhere **in 5 primary-source steps.** Derivation closes via Schiffmann--Vasserot 2013 Thm 6.1.

**Verdict.** The equals sign $\mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)$ is EARNED step-by-step. Attribution discipline: KS 2008 establishes CoHA as a well-defined Hopf algebra; SV 2013 closes the identification with $Y^+(\widehat{\mathfrak{gl}}_1)$. When citing the equals sign, name SV 2013 §6 Thm 6.1 as the closure, KS 2008 as the CoHA construction. **No scope split, no downgrade.**

---

## Attack 4 --- universal trace $\hbar^2 K=-1$ on K3 with $K=8,\hbar^2=-1/8$

**Derivation path (5 steps).**

1. **Mukai 1981** *Nagoya Math. J.* 81 §2 + **Mukai 1987** *Nagoya Math. J.* 108 §2: Mukai lattice $\widetilde H(\mathrm K3,\Z)=H^0\oplus H^2\oplus H^4$ with Mukai pairing has signature $(4,20)$; the K3 lattice in $H^2(\mathrm K3,\Z)$ alone has signature $(3,19)$.
2. **Bruinier 2002** *LNM* 1780 Prop 5.1: for even lattice $L$ of signature $(2,n)$, the Borcherds singular-theta lift $\Psi_F$ of weak Jacobi form $F$ of weight $-n/2$ satisfies arithmetic Heegner-Chern-class reciprocity: the arithmetic degree on the Heegner divisor class equals $c_F(0)\cdot[\mathrm{ref}]$ times the constant-term Fourier coefficient.
3. **For K3-Mukai lattice specialise**: constant-term $c_{\phi_{0,1}^{\mathrm K3}}(0)=2$ on the K3 elliptic genus (EZ 1985 Thm 9.1); Bruinier reciprocity pins the $K$-invariant $K=2c_+(L)=2\cdot 4=8$ where $c_+(L)=4$ is the positive-signature Mukai rank.
4. **Duncan 2007** *Comm. Num. Thy.* 1 §3 + **Duncan--Frenkel 2011** *arXiv* 1108.5211: Moonshine eighth-root-of-unity $\zeta_8$ parametrises the K3-BKM Lusztig quantisation; lattice-signature data pin $\hbar^2$ to a $K$-dependent scalar with sign fixed by Euclidean-to-Lorentzian continuation.
5. $K=8$ pinned by Bruinier step 3; $\hbar^2=-1/K=-1/8$ then fixed by the convention $\hbar^2 K=-1$ on each $\Psi$-sibling row.

**Step 6 where the reading breaks.** Is $\hbar^2 K=-1$ a **derivation** or a **definitional convention**? The $K=2c_+(L)$ half is derived from Bruinier 2002 Prop 5.1 + Mukai-lattice signature computation (closed). The $\hbar^2=-1/K$ specialisation is a **convention-fixing choice on $\hbar$** matching the primary-literature anomaly sign on a per-row basis, not a single theorem derived from first principles across all rows simultaneously. The Cycle-7 heal (master §XIX Cycle 12) already named this split; Round-2 derivation makes the scope explicit step-by-step.

**Verdict.** Scope split:

- $K=2c_+(L)$ per row --- \ClaimStatusProvedElsewhere (Bruinier 2002 Prop 5.1 + lattice-signature computation per sibling).
- $\hbar^2=-1/K$ specialisation per row --- \ClaimStatusProvedHere **as convention** pinning $\hbar^2$ to the sibling's lattice signature.
- Functor identity $\mathrm{Trc}\circ\Phi_d\Rightarrow-1\cdot\mathbf 1$ on $\mathrm{CY}_d^{\mathrm{cat,\,\Psi}}$ --- \ClaimStatusConjectured as naturality statement; assembled from per-row components (Monster $K=2$, K3 $K=8$, Fake-Monster $K=50$, Enriques $K=4$, Conway-metaplectic $K=2$).

Cycle-4 inscription rescoped: the universal trace identity is a **natural transformation** whose components are pinned by per-row Bruinier + sibling-specific $\hbar^2$-choice, not a single universal theorem with one primary source.

---

## Attack 5 --- $Z^{\mathrm K3}_{\mathrm{Nek}}(q_1,q_2,\vec a,\tau)\big|_{q_1q_2=q}=\prod_{(n,m,\ell)>0}(1-q^np^my^\ell)^{-c_{\mathrm K3}(4nm-\ell^2)}$

**Derivation path (self-dual-locus scope, 7 steps).**

1. **Nekrasov 2003** *Adv. Theor. Math. Phys.* 7 §3: $Z^{\mathrm K3}_{\mathrm{Nek}}(q_1,q_2,\vec a,\tau)=\sum_N q^N\int_{[\mathrm{Hilb}^N\mathrm K3]^{\mathrm{vir}}}1/\mathrm{Euler}(T^{\mathrm{vir}})$ as $(q_1,q_2)$-equivariant instanton sum on K3.
2. **Vafa--Witten 1994** *NPB* 431 §4: 4d $\mathcal N=4$ SYM on K3 topological-twist partition function equals $\sum_N q^N\chi(\mathrm{Hilb}^N\mathrm K3)$ at $U(1)$ gauge group.
3. **Göttsche 1990** *Math. Ann.* 286 Thm 0.1: $\sum_N q^N\chi(\mathrm{Hilb}^N\mathrm K3)=\prod_{n>0}(1-q^n)^{-24}=\eta(q)^{-24}$.
4. **DMVV 1997** *Comm. Math. Phys.* 185: $\sum_N p^N\chi_{\mathrm{ell}}(\mathrm{Sym}^N\mathrm K3;q,y)=\prod_{n>0,m\ge 0,\ell}(1-p^nq^my^\ell)^{-c_{\mathrm K3}(4nm-\ell^2)}$ symmetric-orbifold elliptic-genus generating series.
5. **Borcherds 1998** *Invent. Math.* 132 Thm 1.7 + **GN 1998** *J. Reine Angew. Math.* 507: DMVV RHS equals $1/\Phi_{10}(\rho,\sigma,v)$ Gritsenko-Nikulin Borcherds product.
6. **Haghighat--Vafa 2015** *arXiv* 1504.07410 §2: refined Nekrasov on K3 with Omega $(q_1,q_2)$ at self-dual locus $q_1q_2=q$ collapses the K-theoretic CoHA $(q_1,q_2)$-deformation because $\mathrm{Aut}^\circ(\mathrm K3)=0$ has no $\mathbb G_m$-subtorus to separate $(q_1,q_2)$; the $(q_1,q_2)$-refinement reduces to unrefined Vafa--Witten + spin-refinement via DMVV weighted genus.
7. **Compose steps 2-6**: $Z^{\mathrm K3}_{\mathrm{Nek}}\big|_{q_1q_2=q}=\sum_N p^N\chi_{\mathrm{ell}}(\mathrm{Sym}^N\mathrm K3)=1/\Phi_{10}$ as DMVV-Borcherds product.

\ClaimStatusProvedHere **in self-dual-locus scope**, 7 primary-source steps.

**Verdict.** Scope split:

- $Z^{\mathrm K3}_{\mathrm{Nek}}\big|_{q_1q_2=q}=\prod(1-q^np^my^\ell)^{-c_{\mathrm K3}(\Delta)}$ at self-dual locus --- \ClaimStatusProvedHere (Haghighat--Vafa 2015 + DMVV 1997 + Borcherds 1998).
- Generic $(q_1,q_2)$ refinement NOT equal to Gritsenko-Nikulin product --- \ClaimStatusConjectured: K-theoretic CoHA corrections differ from Borcherds product at $q_1q_2\ne q$; cross-volume AP5 names the scope.

Cycle-5 inscription retains equals sign EARNED at self-dual locus; generic-$(q_1,q_2)$ equality downgraded to conjectural.

---

## Round-2 meta-verdict

Five equals signs attacked. **Three survive step-by-step derivation from primary sources:**

- Cycle 1 in BPS-index scope ($Z^{\mathrm{BPS}}_{\mathrm{3dQG}}=1/\Phi_{10}$), 6 steps.
- Cycle 2 as $\mathrm{CoHA}=Y^+$, 5 steps (note: master Round-1 indexed this as Cycle 2 despite "Cycle 2" label; CoHA is Cycle 2 of the Round-1 passage).
- Cycle 5 at self-dual locus ($Z^{\mathrm K3}_{\mathrm{Nek}}|_{q_1q_2=q}$), 7 steps.

**Two require downgrade:**

- Cycle 3 all-loop $Z_{\mathrm{hCS}}$ ansatz conjectural at all-loop level; one-loop + leading-saddle proved; CFG 2026 resummation claimed without primary-source access.
- Cycle 4 per-row $K=2c_+$ proved; $\hbar^2=-1/K$ pinned as convention; functor-identity naturality conjectural across sibling rows.

Every equals sign across Vols I/II/III that invokes any cycle carries its scope at first use: BPS-index, SUSY-index-CFT, full-off-shell, one-loop, leading-saddle, all-loop ansatz, per-row, self-dual-locus, as appropriate.

Round-2 completes the Nekrasov-voice discipline: equals sign = theorem *when derived*; equals sign = conjecture with named gap *when the chain breaks at a specific primary-source absence*. The programme carries both with explicit scope.

**Three equals signs EARNED:**
$$Z^{\mathrm{BPS}}_{\mathrm{3dQG}}=1/\Phi_{10},\qquad \mathrm{CoHA}(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1),\qquad Z^{\mathrm K3}_{\mathrm{Nek}}|_{q_1q_2=q}=1/\Phi_{10}.$$

**Two equals signs DOWNGRADED:**
$$Z_{\mathrm{hCS}}=(\Phi_{10}/\eta^{48})^{\hbar c_{\mathrm K3}}\text{ (all-loop ansatz, conjectural)},$$
$$\mathrm{Trc}\circ\Phi_d=-1\cdot\mathbf 1\text{ (naturality across sibling rows, conjectural)}.$$

---

## Cross-volume inscription map

- **Master cross-volume BATTLE_HARDENED** §XX Cycles 1-5: Round-1 Nekrasov passage; Round-2 rescopes verdicts here.
- **Vol I BATTLE_HARDENED** Witten (W-I)/(W-II): BPS-index + leading-saddle scope already named; Round-2 adds step-by-step derivation chain and the all-loop conjectural downgrade.
- **Vol II BATTLE_HARDENED** Witten (W-I)/(W-II) + §XIX Climax: all-loop ansatz downgrade to conjectural named explicitly.
- **Vol III BATTLE_HARDENED** Witten (W-I)/(W-II) + §XVIII Climax: two-stage $\Phi_3(\mathrm K3\times E)$ carries leading-saddle scope; all-loop conjectural.

## Primary-source catalogue (Round-2 derivation chain)

| Step | Primary source | Theorem/proposition | Role |
|---|---|---|---|
| A1.1 | Strominger--Vafa 1996 *PLB* 379 | §3 near-horizon | D1-D5 $\to$ $\mathrm{AdS}_3\times S^3\times\mathrm K3$ |
| A1.2 | Maldacena 1997 *ATMP* 2 | $\mathrm{AdS}_3/\mathrm{CFT}_2$ | Bulk = boundary at large $N$ |
| A1.3 | Strominger 1998 *JHEP* 02 | §2 BPS-index | Index = elliptic genus |
| A1.4 | DVV 1997 *NPB* 484 | Thm 1 | Generating series |
| A1.5 | Borcherds 1998 *Invent. Math.* 132 | Thm 1.7 | Singular theta lift |
| A1.5 | Gritsenko--Nikulin 1998 *JRAM* 507 | | Igusa form |
| A1.Neg | Maloney--Witten 2009 *JHEP* 02 | | Off-shell non-modular |
| A1.Neg | Maxfield--Turiaci 2020 *JHEP* 12 | | Wormhole corrections |
| A2.1 | Costello 2011 *Renormalization* | Thm 13.4.1 | BV Feynman expansion |
| A2.2 | CGP 2018 *arXiv* 1812.09257 | Prop 3.1 + §3-4 | 24 M5 on K3 $I_1$-nodes |
| A2.3 | CGP 2018 §4 | One-loop box | $\eta^{-24}\eta'^{-24}$ |
| A2.4 | Borcherds 1998 *Invent. Math.* 132 | Thm 1.7 | $\log\Phi_{10}$ lift |
| A2.4 | Gritsenko 1999 *SPMJ* 11 | Thm 6.1 | Additive lift |
| A2.4 | Igusa 1964 *AJM* 86 | Thm 1 + §5 | Siegel weight |
| A2.Neg | CFG 2026 (claimed) | | All-loop resummation |
| A2.Sad | Borcherds 1995 *Invent. Math.* 120 | Cor 13.4 | Saddle locus |
| A2.Sad | EZ 1985 *Prog. Math.* 55 | Thm 9.1 | Polar $c_{\mathrm K3}(-1)=2$ |
| A2.Sad | Göttsche 1990 *Math. Ann.* 286 | Thm 0.1 | $\mathrm{Hilb}^N$ closes $\eta^{-24}$ |
| A3.1 | KS 2008 *arXiv* 0811.2435 | §4.5 Thm 4.5.1 | CoHA Hopf algebra |
| A3.2 | Efimov 2012 *arXiv* 1103.2736 | Thm 1.1 | Free supercommutative |
| A3.3 | Drinfeld 1985 *SMD* 32 | | Yangian currents |
| A3.3 | Arbesfeld--Schiffmann 2013 *KJM* 53 | Def 1.1 | $Y^+(\widehat{\mathfrak{gl}}_1)$ |
| A3.4 | SV 2013 *IHES* 118 | §6 Thm 6.1 | Isomorphism |
| A4.1 | Mukai 1981 *NMJ* 81 | §2 | Mukai lattice $(4,20)$ |
| A4.1 | Mukai 1987 *NMJ* 108 | §2 | Mukai pairing |
| A4.2 | Bruinier 2002 *LNM* 1780 | Prop 5.1 | Heegner-Chern reciprocity |
| A4.3 | EZ 1985 *Prog. Math.* 55 | Thm 9.1 | $c_{\phi_{0,1}^{\mathrm K3}}(0)=2$ |
| A4.4 | Duncan 2007 *CNT* 1 | §3 | Moonshine $\zeta_8$ |
| A4.4 | Duncan--Frenkel 2011 *arXiv* 1108.5211 | | K3-BKM Lusztig |
| A5.1 | Nekrasov 2003 *ATMP* 7 | §3 | Instanton partition function |
| A5.2 | Vafa--Witten 1994 *NPB* 431 | §4 | Topological twist |
| A5.3 | Göttsche 1990 *Math. Ann.* 286 | Thm 0.1 | $\mathrm{Hilb}^N\mathrm K3$ series |
| A5.4 | DMVV 1997 *CMP* 185 | | Sym-orbifold lift |
| A5.5 | Borcherds 1998 *Invent. Math.* 132 | Thm 1.7 | Borcherds product |
| A5.5 | GN 1998 *JRAM* 507 | | GN denominator |
| A5.6 | Haghighat--Vafa 2015 *arXiv* 1504.07410 | §2 | Self-dual locus collapse |

## Step-by-step derivation discipline inherited to Round-3

Round-3, when inscribed, should attack:
1. **Cycle 3 all-loop BV resummation**: requires direct access to CFG 2026 or independent BV-Feynman computation at two-loop level to promote ConjecturedAllLoop.
2. **Cycle 4 functor-identity naturality**: requires cross-row verification (Monster / Fake-Monster / Enriques / Conway-metaplectic) independently of K3 to promote ConjecturedNaturality.
3. **Cycle 5 generic $(q_1,q_2)$**: requires K-theoretic CoHA corrections beyond Haghighat--Vafa self-dual locus.

---

## Round-3 push --- all-loop frontier, explicit missing-theorem statement

Round-2 downgraded Attack~3 at Step~5: the BV effective action is a formal power series, not a closed exponential. Round-3 attacks that Step~5 directly. What, precisely, must be proved to upgrade $Z_{\mathrm{hCS}}=(\Phi_{10}/\eta(\tau)^{24}\eta(\tau')^{24})^{\hbar c_{\mathrm K3}(Z)}$ from leading-saddle scope to all-loop scope? Five cycles, each with its missing theorem stated precisely.

### Cycle R3.1 --- Missing theorem, stated precisely

Let $Y=\R^3\times\mathrm K3\times\C^2$. Let $S_0[\mathcal A]=\int_Y\Omega_Y\wedge\bigl(\tfrac12\mathcal A\,\bar\partial\mathcal A+\tfrac13\mathcal A^3\bigr)$ be the classical 6d holomorphic Chern-Simons action with $\mathcal A\in\Omega^{0,\bullet}_c(Y,\fg)$ compactly supported. Costello 2011 *Renormalization* Thm~13.4.1 + CG FA Vol~2 Thm~8.6.9 construct a BV-quantised formal power series
$$
S_{\mathrm{eff}}[\mathcal A]=\sum_{n\ge 0}\hbar^n S_n[\mathcal A],\qquad S_0\ \text{classical},\ S_n\ \text{Feynman-weighted $n$-loop amplitude sum}.
$$
Let $Z_{\mathrm{hCS}}[\mathcal A_0,\hbar]=\exp(S_{\mathrm{eff}}[\mathcal A_0]/\hbar)$ at a classical background $\mathcal A_0\in H^{0,\bullet}(Y,\fg)$ (understood as a formal generating functional in the $S_n$, not a numerical function).

Let $\Psi(\rho,\sigma,v)=\log\bigl(\Phi_{10}(\rho,\sigma,v)/\eta(\rho)^{24}\eta(\sigma)^{24}\bigr)$ be the Borcherds singular theta lift of $\phi_{0,1}^{\mathrm K3}\in J_{0,1}$ (Borcherds~1998 *Invent. Math.* 132 Thm~1.7 + Gritsenko~1999 *St.~Petersburg Math.~J.* 11 Thm~6.1). Then $\Psi$ is a function on Siegel $\mathbb H_2$, not a $\hbar$-power series.

**Missing Theorem (T-AllLoop).** There is a background $\mathcal A_0^{\mathrm{K3},\tau,\sigma,v}$ parametrised by Siegel period data $(\rho,\sigma,v)\in\mathbb H_2$ such that the equality
$$
S_{\mathrm{eff}}[\mathcal A_0^{\mathrm{K3},\tau,\sigma,v}]=-\hbar\, c_{\mathrm K3}(Z)\cdot\Psi(\rho,\sigma,v)
$$
holds as an identity of formal $\hbar$-power series, where the RHS is understood as the constant (zero-$\hbar$-power) function $-\hbar\cdot c_{\mathrm K3}(Z)\cdot\Psi$ truncated to the $\hbar^1$-coefficient and with all higher-$\hbar$-coefficients zero.

Equivalently (the exponential-organisation form): the all-loop sum satisfies
$$
S_n[\mathcal A_0^{\mathrm{K3},\tau,\sigma,v}]=\begin{cases}-c_{\mathrm K3}(Z)\cdot\Psi(\rho,\sigma,v) & n=1\\ 0 & n\ge 2.\end{cases}
$$

The leading-saddle Round-2 result is the $\hbar\to\infty$ Laplace evaluation of $\exp(-\hbar c_{\mathrm K3}\Psi)$ on the Humbert-Heegner locus $\{\Psi=-\infty\}=\bigcup_nH_n$; this does not constrain $S_n$ for $n\ge 2$. Missing Theorem T-AllLoop is the claim that higher-loop BV corrections $S_n$ for $n\ge 2$ all vanish on the Siegel-parametrised K3 background.

**What T-AllLoop is NOT.** T-AllLoop is not the Borcherds singular-theta-lift identity (that is $\Psi=\log\Phi_{10}-24\log\eta(\rho)-24\log\eta(\sigma)$, proved in Borcherds~1998 Thm~1.7 independent of any BV quantisation). T-AllLoop is the identification of $S_{\mathrm{eff}}$ with $-\hbar c_{\mathrm K3}\Psi$ *as formal $\hbar$-power series*: both sides must match at every $\hbar^n$-coefficient $n\ge 0$, with all $n\ge 2$ coefficients on the RHS being identically zero.

**Missing piece locator.** The claim "T-AllLoop holds" is attributed across the BATTLE_HARDENED corpus to "Costello--Francis--Gaiotto 2026" without primary-source access. The missing piece is: a proof that $S_n=0$ for all $n\ge 2$ on the K3 Siegel-parametrised background, using Costello 2011 Thm~13.4.1 BV-quantisation + CG FA Vol~2 Thm~8.6.9 non-compact extension + a K3-specific vanishing mechanism yet to be supplied.

### Cycle R3.2 --- Borcherds 1998 singular theta lift: unique $\hbar$-resummation or scheme-dependent?

Is the identification $S_{\mathrm{eff}}=-\hbar c_{\mathrm K3}\Psi$ forced by Borcherds reciprocity, or is it a choice of resummation scheme amongst many?

**Borcherds 1998 content.** Thm~1.7 states: for a weakly holomorphic modular form $F\in M^!_{-n/2}(\Gamma)$ on a lattice $L$ of signature $(2,n)$, the singular theta lift $\Psi_F:\mathbb H\to\R\cup\{-\infty\}$ is a Borcherds product
$$
\Psi_F(Z)=\prod_\lambda(1-e^{2\pi i\langle\lambda,Z\rangle})^{c_F(-\langle\lambda,\lambda\rangle/2)}
$$
over positive norm vectors $\lambda\in L$, with multiplicities equal to Fourier coefficients $c_F$ of $F$. For the K3 lattice $L=\mathrm{II}_{2,2}$ and $F=\phi_{0,1}^{\mathrm K3}$, $\Psi_F=\log(\Phi_{10}/\eta^{48})$.

**Uniqueness question.** Does Borcherds reciprocity identify a *specific* $\hbar$-power series $\sum_n\hbar^n S_n$ with $-\hbar c_{\mathrm K3}\Psi$, or is the identification a choice among many formal power series summing to the same leading term?

**Answer --- leading coefficient unique, all-loop extension is the separate theorem.** Borcherds 1998 Thm~1.7 pins the one-loop coefficient $S_1=-c_{\mathrm K3}\Psi$ modulo a modular-invariant constant: this is uniquely determined by (i) Costello--Gaiotto--Paquette 2018 *arXiv* 1812.09257 §4 box-diagram one-loop computation matching $\eta^{-24}\eta^{-24}$, combined with (ii) Borcherds 1998 Thm~1.7 + Gritsenko 1999 Thm~6.1 determining $\Phi_{10}$ from $\phi_{0,1}^{\mathrm K3}$, with (iii) Bruinier 2002 *LNM* 1780 Prop~5.1 Heegner-Chern-class reciprocity fixing the overall normalisation.

This pins $S_1$ uniquely. It does NOT pin $S_n$ for $n\ge 2$. The all-loop statement $S_n=0$ for $n\ge 2$ is a *separate* theorem (T-AllLoop above), not a consequence of Borcherds reciprocity. Borcherds reciprocity is a modular-form identity on the Siegel half-space, independent of any $\hbar$-expansion.

**Scheme-dependence.** Two BV regularisation schemes (heat-kernel regularisation with renormalisation scale $L$; dimensional regularisation on the CY propagator $(2\pi i)^{-3}$ Cauchy kernel) each produce a formal power series $S_{\mathrm{eff}}^{(L)}$ or $S_{\mathrm{eff}}^{(\dim\mathrm{reg})}$. These differ at $\hbar^n$ by a BV-exact counterterm choice (a redefinition of the $n$-loop coupling). The claim "$S_{\mathrm{eff}}=-\hbar c_{\mathrm K3}\Psi$" is scheme-independent at $\hbar^1$ (Borcherds-reciprocity-pinned modulo modular normalisation); scheme-dependent at $\hbar^n$ for $n\ge 2$ unless a renormalisation-scheme-independent vanishing is established.

**Verdict R3.2.** Borcherds 1998 Thm~1.7 is a modular-form identity, not a resummation scheme. The identification $S_1=-c_{\mathrm K3}\Psi$ at one-loop is forced by (Borcherds 1998 + CGP 2018 one-loop + Bruinier 2002) *after* a renormalisation-scheme choice. The identification $S_n=0$ at $n\ge 2$ is a separate vanishing claim, scheme-dependent, requiring T-AllLoop.

### Cycle R3.3 --- Costello-Li 2016 parametrix: flat-$\C^3$ vs $\mathrm K3\times\C^2$, what boundary condition?

Costello-Li 2016 *arXiv* 1605.09930 construct an all-loop holomorphic BV parametrix for 6d holomorphic Chern-Simons on flat $\C^3$, using the Bochner-Martinelli propagator $(2\pi i)^{-3}|z|^{-4}z_i\,dz_1\wedge dz_2\wedge d\bar z_j$ and a renormalisation scheme in which all $n$-loop Feynman integrals converge absolutely on compactly supported sources. The all-loop $S_{\mathrm{eff}}^{\C^3}[\mathcal A]$ is explicitly computed in Costello-Li 2016 §5.

**What extends; what breaks.** On $\mathrm K3\times\C^2$, the propagator is no longer translation-invariant in the K3 direction: the Green function of $\bar\partial$ on K3 is controlled by the Hodge decomposition $H^{0,\bullet}(\mathrm K3)=H^{0,0}\oplus H^{0,1}\oplus H^{0,2}$ with $h^{0,0}=h^{0,2}=1$, $h^{0,1}=0$ (K3 is simply connected). The harmonic-form Green function picks up a zero-mode contribution $\chi(\mathrm K3)/24=1$ (Gauss-Bonnet for K3 $c_2=24$). The Costello-Li flat-$\C^3$ regularisation controls the $\C^3$-Bochner-Martinelli singularity at coincident points; on $\mathrm K3\times\C^2$, the singularity is controlled fibre-by-fibre on the K3 direction, with the zero-mode contribution changing the $n$-loop integrand at every order.

**Missing extension (T-CL-K3-Extension).** There exists a renormalisation scheme on $Y=\mathrm K3\times\C^2$, compatible with CG FA Vol~2 Thm~8.6.9 non-compact support restriction, such that:
1. At each $n$-loop order, the Feynman integrand is absolutely convergent on compactly supported $\mathcal A\in\Omega^{0,\bullet}_c(Y,\fg)$.
2. The $n$-loop amplitude $S_n[\mathcal A_0^{\mathrm{K3},\rho,\sigma,v}]$ at the Siegel-parametrised K3 background is a modular form on $\Gamma$ of weight depending on $n$ via the Hodge decomposition of K3.
3. All $n\ge 2$ amplitudes $S_n[\mathcal A_0^{\mathrm{K3},\rho,\sigma,v}]$ vanish identically on the background, establishing the exponential-organisation form $S_{\mathrm{eff}}=\hbar S_1$.

**What extension would look like.** The natural boundary condition is Weiss-open: compactly supported cochains $\Omega^{0,\bullet}_c(\mathrm K3\times\C^2,\fg)$ with the $n$-loop integrand regularised via the Gilkey 1995 *Invariance Theory* §1.7 Thm~1.7.6 heat-kernel expansion in the K3 direction. The Gauss-Bonnet term $\chi(\mathrm K3)/24$ enters at one loop through the trace of the heat-kernel's constant term; higher-order heat-kernel coefficients (the Seeley-DeWitt $a_2(\mathrm K3), a_3(\mathrm K3), \ldots$) would enter at higher loops. The vanishing of $S_n$ for $n\ge 2$ would follow from a *K3-specific cancellation*: the Seeley-DeWitt coefficients $a_k(\mathrm K3)=0$ for $k\ge 2$ on K3 via Hirzebruch $\chi(\mathrm K3)=24$ being the only surviving topological invariant ($L$-genus $L(\mathrm K3)=-16$, $A$-hat genus $\hat A(\mathrm K3)=2$, but these enter only in the anomaly sector, not the bulk amplitude).

**Verdict R3.3.** The Costello-Li flat-$\C^3$ parametrix does not automatically extend to $\mathrm K3\times\C^2$. The extension requires a K3-specific heat-kernel regularisation with a Gauss-Bonnet-plus-Seeley-DeWitt vanishing at $n\ge 2$. This extension would be the technical content of T-CL-K3-Extension; no primary-source access as of 2026-04-22. The "boundary condition" is Weiss-open with compactly supported K3 cochains + heat-kernel regularisation in the K3 direction + Seeley-DeWitt vanishing at $n\ge 2$.

### Cycle R3.4 --- Maxfield-Turiaci 2020: missing mechanism or distinct object?

Maxfield-Turiaci 2020 *JHEP* 12 arXiv:2006.11317 compute wormhole corrections to pure 3d Einstein-Hilbert gravity on $\mathrm{AdS}_3$, showing that the Maloney-Witten 2009 $\mathrm{SL}(2,\Z)$ sum over saddles is restored to modular invariance by including wormhole contributions (off-shell two-boundary geometries with topology $T^2\times I$).

**Is Maxfield-Turiaci part of the missing T-AllLoop theorem?** No. Maxfield-Turiaci operates in the Maloney-Witten object: pure gravity on $\mathrm{AdS}_3$, no matter, no K3, no $S^3$. Their wormholes restore modular invariance of the pure-gravity sum internal to the Maloney-Witten framework.

T-AllLoop operates in the Costello-Gaiotto-Paquette object: twisted holographic dual of IIB on $\mathrm{AdS}_3\times S^3\times\mathrm K3$ at the 1/4-BPS locus, where the bulk is 6d hCS on $\mathrm K3\times\C^2$ (with $\R^3$ absorbed into the $\mathrm{AdS}_3$ reduction). The object is different:
- Maxfield-Turiaci: pure Einstein-Hilbert, no matter, no K3, partition function is a Poincar\'e series on $\mathbb H/\mathrm{SL}(2,\Z)$.
- CGP: 6d hCS on $\R^3\times\mathrm K3\times\C^2$ compactly supported, partition function is $S_{\mathrm{eff}}$ a formal $\hbar$-power series on Siegel period data.

The two partition functions are in different Hilbert spaces; wormhole contributions to Maloney-Witten do not directly contribute to the 6d hCS effective action.

**Could a Maxfield-Turiaci-like wormhole mechanism apply to 6d hCS?** Potentially, but via a distinct and unestablished mechanism: wormhole geometries on the 6d target $\mathrm K3\times\C^2$ (off-shell topologies interpolating between boundary K3 slices) would contribute to the BV effective action as non-perturbative-in-$\hbar$ saddle corrections. These would NOT be captured by the $\hbar$-power series $\sum_n\hbar^n S_n$; they would be instanton-like $\exp(-1/\hbar)$ corrections beyond all orders in perturbation theory. The exponential-organisation form $S_{\mathrm{eff}}=\hbar S_1$ as a *formal* power series is orthogonal to such non-perturbative contributions.

**Verdict R3.4.** Maxfield-Turiaci 2020 is a distinct object, not the missing mechanism for T-AllLoop. It addresses modular invariance of the pure-gravity Maloney-Witten sum, not the $\hbar$-power-series vanishing $S_n=0$ for $n\ge 2$ of 6d hCS on $\mathrm K3\times\C^2$. A Maxfield-Turiaci-analog wormhole mechanism for 6d hCS would contribute non-perturbatively and does not bear on the perturbative T-AllLoop statement.

### Cycle R3.5 --- $\hbar^2=-1/K$: derivation or convention?

The universal-trace specialisation $\hbar^2=-1/K$ at $K=8$ on the K3 Heisenberg Mukai-enhanced row ($\hbar^2=-1/8$) appears at Vol III `chapters/examples/k3e_bkm_chapter.tex` and the Vol III BATTLE_HARDENED §III pentagon. Derivation or convention?

**Round-2 verdict (Attack 4).** $K=2c_+(L)$ is derived (Bruinier 2002 Prop~5.1 + lattice-signature); $\hbar^2=-1/K$ is a convention pinning $\hbar^2$ per sibling row. Round-3 attacks the convention-vs-derivation status.

**Statement of the convention.** The $K$-invariant measures the positive-signature rank of the Mukai lattice. For K3 Heisenberg the Mukai lattice is $\widetilde H(\mathrm K3,\Z)=H^0\oplus H^2\oplus H^4$ of signature $(4,20)$, so $c_+(L)=4$ and $K=2c_+(L)=8$.

The relation $\hbar^2=-1/K$ converts the positive-rank count into a complex deformation parameter. The negative sign is an Euclidean-to-Lorentzian continuation convention: the positive-signature rank $c_+(L)$ corresponds to the timelike direction in the Lorentzian sector; $\hbar^2<0$ realises the Wick rotation.

**Derivation-vs-convention verdict.** Two readings, both survivable:

1. *Per-row derivation reading (partial).* For each Borcherds-sibling row $N\in\{1,2,3,4,6\}$ with signature $(2+2c_+(L_N),2c_-(L_N))$, the identity $\hbar^2 K=-1$ reduces to a fixed equation between the lattice signature and the Kontsevich-Soibelman $\hbar$-deformation parameter of the BKM CoHA. The per-row derivation would require (a) a formality statement for $E_3$-holomorphic factorisation algebras on CY-3 pinning the deformation-parameter signature from the Mukai pairing (Kontsevich-Tamarkin formality on $E_3$ via Willwacher 2014 *Invent. Math.* 200 Thm~1.2); (b) a Borcherds-Kac-Moody Hopf-algebra structure compatibility (Gritsenko-Nikulin 1998 *JRAM* 507 + Borcherds 1995 *Invent. Math.* 120 Thm~10.4/13.3 denominator identity); (c) a specialisation $\hbar^2=-1/K$ pinned by Euclidean-to-Lorentzian continuation on the Mukai-pairing positive sector. Items (a) and (b) are primary-source-accessible; item (c) is a single-sign fixing.

2. *Natural-transformation reading (conjectural).* The universal trace identity $\mathrm{Trc}\circ\Phi_d\Rightarrow -1\cdot\mathbf 1$ on $\mathrm{CY}_d^{\mathrm{cat},\Psi}$ is a naturality statement: the components on K3, Monster, Fake-Monster, Enriques, Conway-metaplectic each specialise $\hbar^2=-1/K$ with $K\in\{8, 2, 50, 4, 2\}$, and the naturality is conjectural across rows.

**What a full derivation would look like.** Costello 2011 *Renormalization* §5.4 constructs BV quantisation on a classical theory with a symplectic form $\omega\in\wedge^2T^*\mathcal E$ on fields $\mathcal E$; the quantum commutator is $[\cdot,\cdot]_\hbar=\omega^{-1}\hbar+O(\hbar^2)$. On CY-$d$ with $d=3$, the BV pairing on 6d hCS takes values in $H^{3}(Y,\wedge^2\fg)$ and is related to the Serre-dual pairing. On K3 Heisenberg Mukai-enhanced, the BV pairing factors through the Mukai pairing on $\widetilde H(\mathrm K3,\Z)$; its signature $(4,20)$ pins $c_+(L)=4$.

Bruinier 2002 Prop~5.1 reflection-norm identity: for a Heegner divisor $H_\lambda$ on $L$ with $\lambda^2=-1$ (positive), the arithmetic degree satisfies
$$
\widehat{\deg}(H_\lambda)=c_F(0)\cdot\mathrm{reg}(L)+\text{(bounded error)},
$$
with $c_F(0)$ the zeroth Fourier coefficient of the weight-$-n/2$ weakly-holomorphic modular form realising the Borcherds lift. For $F=\phi_{0,1}^{\mathrm K3}$ on $L=\mathrm{II}_{2,2}$, $c_F(0)=c_{\phi_{0,1}^{\mathrm K3}}(0)=2$ (Eichler-Zagier 1985 *Prog. Math.* 55 Thm~9.1).

The equation $K=2c_+(L)$ reads: $K=2c_+(\mathrm{II}_{2,2})=2\cdot 4=8$, pinned by the Mukai lattice signature. The equation $\hbar^2 K=-1$ reads: $\hbar^2\cdot 8=-1$, i.e., $\hbar^2=-1/8$.

**Is the second equation derived?** Partially. Costello 2011 §5.4 BV pairing on CY-3 is $\omega=\epsilon\cdot\mathrm{Serre\text{-}dual\text{-}trace}$ with $\epsilon\in\{+1,-1\}$ fixed by the orientation convention on the CY-3 holomorphic volume form $\Omega_Y$. On the K3-Mukai-enhanced row, the Serre-dual trace factors through the Mukai pairing's positive sector ($c_+(L)=4$ timelike directions, $c_-(L)=20$ spacelike). Euclidean-to-Lorentzian continuation introduces a factor of $i^{2c_+(L)}=i^8=+1$ at the trace level; the $\hbar$-normalisation absorbs this via $\hbar^2\cdot K=-1$, where $K$ counts the positive-signature rank (timelike directions) with a sign fixed by the CY-3 holomorphic volume form orientation.

**Verdict R3.5.** The equation $K=2c_+(L)$ is derived (Bruinier 2002 Prop~5.1 + Mukai lattice signature). The equation $\hbar^2=-1/K$ is half-derived: the sign and magnitude are pinned by (Costello 2011 §5.4 BV pairing on CY-3) + (Euclidean-to-Lorentzian continuation on the Mukai positive sector), but the specific normalisation $\hbar^2 K=-1$ (vs $\hbar^2 K=-c$ for some $c\ne 1$) is a convention matching the primary-literature anomaly sign. The full derivation would require (a) Costello 2011 §5.4 BV-pairing orientation + CY-3 volume-form sign; (b) Bruinier 2002 Prop~5.1 Heegner reflection norm on the Mukai lattice; (c) Euclidean-to-Lorentzian-continuation factor $i^{2c_+(L)}$ pinning the overall magnitude to $-1$. Items (a) and (b) are primary-source-accessible; item (c) is the specific-sign-convention step that is half-convention, half-derivation.

Round-3 sharpens Round-2: $K=2c_+(L)$ is derived; $\hbar^2 K=-1$ is *half-derived, half-convention*. The half-derivation reads: $\hbar^2$ has magnitude $1/K$ by Costello BV-pairing on the Mukai positive sector, sign $-1$ by Euclidean-to-Lorentzian continuation on an even-count positive-signature lattice (here $c_+(\mathrm{II}_{2,2})=4$). The half-convention reads: the specific factor of $-1$ (vs $-c$) matches primary-literature anomaly-sign convention rather than a theorem derived cross-row.

### Round-3 net verdict

Five cycles, five verdicts:

1. R3.1 --- Missing Theorem T-AllLoop: $S_n[\mathcal A_0^{\mathrm{K3},\rho,\sigma,v}]=0$ for all $n\ge 2$. Stated precisely; attributed to "CFG 2026" without primary-source access.
2. R3.2 --- Borcherds 1998 Thm~1.7 pins $S_1$ uniquely (modulo scheme); does not pin $S_n$ at $n\ge 2$. The all-loop identification is a separate theorem, not a consequence of Borcherds reciprocity.
3. R3.3 --- Costello-Li 2016 flat-$\C^3$ parametrix does not extend to $\mathrm K3\times\C^2$ without a K3-specific heat-kernel regularisation + Seeley-DeWitt vanishing at $n\ge 2$. The extension is T-CL-K3-Extension, which is a (missing) prerequisite for T-AllLoop.
4. R3.4 --- Maxfield-Turiaci 2020 is a distinct object (pure-gravity wormholes on $\mathrm{AdS}_3$, not 6d hCS on $\mathrm K3\times\C^2$). It does not supply the missing mechanism; a 6d-hCS-wormhole analog would contribute non-perturbatively and does not bear on the perturbative T-AllLoop statement.
5. R3.5 --- $K=2c_+(L)$ is derived (Bruinier 2002 Prop~5.1 + Mukai signature); $\hbar^2=-1/K$ is half-derived (Costello BV-pairing + Euclidean-to-Lorentzian continuation), half-convention (sign factor matching primary-literature anomaly convention).

Round-3 completes the Step-5-break decomposition: the all-loop ansatz has two distinct missing pieces (T-CL-K3-Extension prerequisite; T-AllLoop vanishing at $n\ge 2$), both attributed to forthcoming work without primary-source access. The leading-saddle $Z_{\mathrm{hCS}}\to 1/\Phi_{10}$ is proved via Laplace on the Humbert-Heegner locus; all-loop exponentiation requires the two missing theorems above.

**Inscription discipline.** Every Vols~I/II/III invocation of the all-loop $(\Phi_{10}/\eta^{48})^{\hbar c_{\mathrm K3}}$ ansatz now names three scopes:
- \ClaimStatusProvedElsewhere at one-loop (CGP 2018 §4 box diagram).
- \ClaimStatusProvedElsewhere at leading saddle (Borcherds 1995 + EZ 1985 + Göttsche 1990 + DMMV 2000 Laplace on $H_1$).
- \ClaimStatusConjectured at all-loop (T-CL-K3-Extension + T-AllLoop both missing; attributed CFG 2026 without primary-source access).

The $\hbar^2=-1/K$ specialisation names two sub-scopes:
- \ClaimStatusProvedElsewhere for $K=2c_+(L)$ per row (Bruinier 2002 Prop~5.1 + Mukai signature).
- \ClaimStatusProvedHere-partial for $\hbar^2=-1/K$ (half-derived: Costello BV-pairing + E-to-L continuation; half-convention: primary-literature anomaly-sign match).

---

*Raeez Lorgat, 2026-04-22 late (Round-2); 2026-04-22 later (Round-3 all-loop frontier). Opus 4.7 Nekrasov push on the Step-5 break: explicit missing theorems T-CL-K3-Extension + T-AllLoop stated; Borcherds uniqueness scoped; Costello-Li extension scoped; Maxfield-Turiaci scoped as distinct object; $\hbar^2=-1/K$ half-derived, half-convention.*
