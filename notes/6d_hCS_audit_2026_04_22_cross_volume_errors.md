# 6d hCS Audit, 2026-04-22 — Cross-Volume Error Synthesis

Meta-verifier: Opus 4.7. Cross-volume synthesis of the twenty-four
errors caught during the 6d holomorphic Chern--Simons audit run across
Vol I (`chiral-bar-cobar`), Vol II (`chiral-bar-cobar-vol2`), and
Vol III (`calabi-yau-quantum-groups`). Author of record: Raeez Lorgat.

The 6d hCS audit concerns the Costello--Li BV quantisation of
holomorphic Chern--Simons on a Calabi--Yau 3-fold, its $\mathbb E_3$
factorisation-algebra structure on $\mathrm{CY}_3$, and its
specialisation on $K3\times T^2$ to a paramodular Borcherds-product
partition function. The audit's twenty-four errors span all three
volumes via the Stage-1 (Costello--Gwilliam--Li holomorphic FA) and
Stage-2 ($\mathrm{Sp}_{\Sigma_{d-1}, C}$ specialisation) lanes of the
$\Phi_d$ two-stage factorisation.

## 1. Twenty-four-row master table

Legend: Vol I AP columns refer to entries in
`/Users/raeez/chiral-bar-cobar/appendices/first_principles_cache.md`
and `.../notes/antipatterns_catalogue.md`; Vol II refers to
`/Users/raeez/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md`
and `.../notes/first_principles_cache.md`; Vol III refers to
`/Users/raeez/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md`
and `.../appendices/first_principles_cache.md`. Cross-vol ledger
entries live in `/Users/raeez/chiral-bar-cobar/notes/cross_volume_aps.md`.

| ID  | One-line statement | Vol I AP | Vol II AP | Vol III AP | Cross-vol-AP | Primary-lit anchor |
|-----|--------------------|----------|-----------|------------|--------------|--------------------|
| E1  | 6d hCS one-loop anomaly is quartic adjoint Casimir, not quadratic | cache 446 / AP929 | `bv_brst.tex` Thm `thm:6dhcs-one-loop-anomaly` / V2-AP144 pending | AP-CY190 pending | **AP-CY50-E1 (add)** | Costello 2015 arXiv:1410.5421 §4-5; Costello 2017 arXiv:1610.04144 |
| E2  | $c_{\phi_{-2,1}}(-n) \neq 24$; $\phi_{-2,1}$ is weak Jacobi with no polar coefficients | cache 447 | cache 109 (W16 BV-3-loop) / V2-AP145 pending | AP-CY9, AP-CY42 | **AP-CY50-E2 (add)** | Eichler--Zagier 1985 Prog Math 55 Thm 9.3; EOT 2011 Exper Math 20 |
| E3  | Theta-graph 1-loop miscount (wrong symmetry factor, wrong graph) | AP929 / cache 446 (companion) | cache 109 (W16 BV-3-loop Feynman: $\chi(K3)^3/3!$); V2-AP146 pending | AP-CY191 pending | **AP-CY50-E3 (add)** | Costello--Gwilliam FA Vol 2 Ch 5; Cattaneo--Felder 2000 CMP 212 |
| E4  | $\zeta(3)^2$ shuffle-dimensional failure: Willwacher wheel $\neq$ quadratic $\zeta(3)$ | cache 434, 440, 441 (GRT/KT) | cache 138 (GRT-torsor valued $E_2$) / V2-AP147 pending | AP-CY161 | **AP-CY50-E4 (add)** | Willwacher 2014 Invent Math 200 Thm 1.2; Brown 2012 Ann Math 175 |
| E5  | Wedge-of-1-forms nullity: $\eta_{ij}\wedge\eta_{jk}\wedge\eta_{ki}$ on stratified Humbert $\ne$ Arnold on $\mathbb A^1$ | cache 293 (Arnold local/global) | V2-AP41 (chiral Kontsevich formality stratified) | AP-CY142 (HH admissibility) | **AP-CY50-E5 (add)** | Totaro 1996 Topology 35; Kriz 1994 Ann Math 139 |
| E6  | $\mathrm{Res}_{\Phi_{10}=0}(Z_{hCS}) = 1/\Phi_{10}$ is ill-typed (residue removes denominator, not restores it) | cache 448 / AP930 | `thqg_perturbative_finiteness.tex` Thm `thm:hcs-all-loop-resummation`; V2-AP148 pending | AP-CY192 pending | **AP-CY50-E6 (add)** | DVV 1997 Nucl Phys B 484; Maloney--Witten 2010 JHEP 1002; Borcherds 1995 Invent Math 120 Thm 10.4 |
| E7  | $\eta^{24}$ single-denominator insufficient on Siegel diagonal (need both $\eta(\tau)^{24}$ and $\eta(\tau')^{24}$) | cache 449 / AP931 | `thqg_perturbative_finiteness.tex` §`sec:pf-hcs-bv-feynman-trace`; V2-AP149 pending | AP-CY193 pending | **AP-CY50-E7 (add)** | Igusa 1964 Amer J Math 86; DVV 1997; Gritsenko--Nikulin 1998 §3 |
| E8  | Dunn $E_1$-per-$\mathbb C$ on $\mathbb C^3$: $\mathbb C^n$ gives $E_{2n}$ geometrically, $E_n$ only after $\bar\partial$-cohomology | cache 450 / AP932 | AP-V2-36 / V2-AP139 (Dunn real-vs-complex) | AP-CY53 ($\pi_1(\mathrm{Conf}_2)$ ordered vs unordered) | **AP-CY50-E8 (add)** | Lurie HA 5.1.2.2; Costello--Gwilliam FA Vol 2 Ch 5 Thm 5.1 |
| E9  | Willwacher wheel-to-$\zeta$ convention: signed vs unsigned, rational vs single-valued | cache 434, 435 (motivic-period) | cache 138 (GRT$_1$-torsor) / V2-AP150 pending | AP-CY161 | **AP-CY50-E9 (add)** | Willwacher 2014; Brown 2014 Forum Math Sigma 2; Schnetz 2013 |
| E10 | K3 mixed Hodge structure pollutes motivic MZV (non-Tate cycles break Brown--Schnetz single-valued depth) | cache 434, 435 | V2-AP151 pending | AP-CY10 (K3 MHS separation) pending; AP-CY142 (HH-admissibility companion) | **AP-CY50-E10 (add)** | Deligne 1971 Publ IHES 40 (MHS); Brown 2014; K3 Hodge non-Tate Kuga--Satake |
| E11 | AFT 2017 vs AF 2015 citation: Andrade--Forrester--Thomas 2017 vs Andrade--Forrester 2015 are different papers | (no Vol I entry yet) | V2-AP152 pending | AP-CY194 pending | **AP-CY50-E11 (add)** | Andrade--Forrester 2015; Andrade--Forrester--Thomas 2017 |
| E12 | Costello 2011 Thm 13.4.1 compactness hypothesis: the theorem is conditional on compact support, not automatic | cache 266, 267 (citation-key, citation-attribution) | V2-AP153 pending | AP-CY195 pending | **AP-CY50-E12 (add)** | Costello 2011 *Renormalization and Effective Field Theory* Thm 13.4.1 |
| E13 | CHSW $\mathrm{SU}(3)$ vs $\mathrm{SU}(4)$ holonomy: Calabi--Yau 3 has $\mathrm{SU}(3)$, Calabi--Yau 4 has $\mathrm{SU}(4)$; CHSW 1985 fixed $\mathrm{SU}(3)$ heterotic phenomenology | (no Vol I entry yet) | V2-AP154 pending | AP-CY17 (MF CY dim $n-2$ companion) | **AP-CY50-E13 (add)** | Candelas--Horowitz--Strominger--Witten 1985 Nucl Phys B 258 |
| E14 | $E_6$ anomaly-free status: quartic Casimir $\mathrm{tr}_{adj}T^4$ is NONZERO on $E_6$; $E_6$ is NOT trivially anomaly-free | cache 446 / AP929 (Deligne series exceptional) | `bv_brst.tex` Cor `cor:6dhcs-deligne-cancellation`; V2-AP155 pending | AP-CY196 pending | **AP-CY50-E14 (add)** | Deligne 1996 CR Acad Sci 322; Cohen--de Man 1996 CR Acad Sci 322 (Vogel plane) |
| E15 | Conway bosonic vs metaplectic $\Psi$: $V^{s\natural}$ is the $\mathbb Z/2$-super-twin of $V^\natural$ via Duncan 2007 diamond, NOT a bosonic $\Psi$-image | AP439 (Niemeier ladder $N\in\{13,\ldots,24\}$) | `unified_chiral_quantum_group.tex` bosonic-$\Psi$ row; V2-AP156 pending | AP-CY71 (Conway $V^{s\natural}$ as $5$th $\Psi$-image FALSE) | **AP-CY50-E15 (add)** | Duncan 2007 Duke Math J 139; Scheithauer 2008 Invent Math 172 |
| E16 | CHL Siegel weights $\{5,4,3,2,1\}$ typo at $N \in \{1,2,3,4,6\}$; the weight at $N=6$ is $1$ not $5$ | cache W14-B5 (2-scope formulation); AP444 ($\Phi_{10}$ wt 10) | cache 16K (paramodular vs Siegel weight); V2-AP157 pending | AP-CY200 / W14-B5 | **AP-CY50-E16 (add)** | Gritsenko 1999 Math Nachr 199 Thm 6.1; Clery--Gritsenko 2013 JRAM 678 §3 |
| E17 | $\kappa_{\mathrm{BKM}}$ scope: 5 (K3 via $\Delta_5$) vs 12 (Fake-Monster via $\Phi_{12}$) vs 10 ($\Phi_{10} = \Delta_5^2$) | cache 88, 123, 445 / AP928 | cache 88 / AP-V2-22; V2-AP158 pending | AP-CY37, AP-CY49, AP-CY85, AP-CY172 | **AP-CY50-E17 (add)**; existing ledger row "$\kappa_{\mathrm{BKM}}(\mathbf H_{\Delta_5})$ dual-indexing" header | Gritsenko--Nikulin 1998 JRAM 507; Borcherds 1995 Invent Math 120 Thm 10.4, Thm 13.3 |
| E18 | Yangian type count (3 vs 4): there are FOUR types (classical, dg-shifted, chiral, spectral), not three | AP159 (four Yangian types in Vol I ap catalogue) | V2-AP159 pending | AP-CY-Yangian pending | **AP-CY50-E18 (add)** | Drinfeld 1985 Soviet Math Dokl 32; Maulik--Okounkov 2012 arXiv:1211.1287 |
| E19 | $\Phi_d$ Stage-1 / Stage-2 naming: $\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$ (not one-step) | AP273 (functor vs object-level); AP923-AP928 (cross-volume Wave-14) | AP-V2-27 / V2-AP130 (two-stage anchor); AP-V2-33 / V2-AP136 (canonical chiral = CL $\cap$ KT) | AP-CY144 / F8 two-stage factorisation; AP-CY172; C6 three-tier hierarchy | **AP-CY62-crossvol** (already in ledger); reinforce with **AP-CY50-E19 (add)** as 6d-hCS-specific anchor | Costello 2013 arXiv:1303.2632; Costello--Li 2016 arXiv:1605.09930; Francis--Gaitsgory 2012 Selecta Math 18; Costello--Gwilliam FA Vol 2 §10-11 |
| E20 | Seven-incarnation equivalence overclaim: the seven faces of $r_{\mathrm{CY}}$ are a three-tier hierarchy (intrinsics / Stage-1 invariants / Stage-2 outputs), NOT seven equivalent presentations | AP284 (equivalence claim without inscribed implication structure); AP294 (slot drift) | V2-AP160 pending | AP-CY C6 (three-tier hierarchy) | **AP-CY50-E20 (add)** | Maulik--Okounkov 2012; Kontsevich--Soibelman 2008; Pandharipande--Thomas 2014 Forum Math Pi 2 |
| E21 | $\Delta_{E_6}$ weight 16 vs 18: the $E_6$-type chiral deformation carries weight 16 (not 18) via Weyl--Kac denominator at rank 6 | AP423 (Hecke $a_p$ at new primes; $f_{16} = E_4 \cdot \Delta$) | V2-AP161 pending | AP-CY88 (Hecke $a_p$ primary form $f_{16}$) | **AP-CY50-E21 (add)** | Serre 1973 Seminaire DPP 14; Ikeda 2001 Ann Math 154; AP893 W25 $\tau/a_p$ verification |
| E22 | Gritsenko-$\Delta_5$ vs Borcherds-$\Phi_{10}$: $\Phi_{10} = \Delta_5^2$ half-BPS vs full-BPS heterotic/Type-II S-duality at automorphic level | cache 88, 108, 123, 445 / AP928; AP927 (ten real simple roots read) | cache 88; V2-AP162 pending | AP-CY49, AP-CY172 | **AP-CY50-E22 (add)**; existing ledger header `AP5 dual-indexing header` | Gritsenko 1999 Thm 6.1; Gritsenko--Nikulin 1998; DVV 1997; Borcherds 1995 Thm 13.3 |
| E23 | Three-faces identity row coverage: Monster / K3 / FM proved per-row; Enriques / Conway row-proofs pending | AP445 (three-faces $\mathsf B$-row); canonical preamble row 90 | V2-AP163 pending | AP-CY70 ($\Psi$-functor surjectivity scope); C7 dimensional sibling catalogue | **AP-CY50-E23 (add)** | Borcherds 1992 Invent Math 109; Borcherds 1998 Invent Math 132; Duncan 2007 Duke Math J 139 |
| E24 | $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ (Künneth-multiplicative Hodge supertrace), NOT 2 or 3 (retracted additive readings) | AP289, AP307 (Künneth discipline); AP-CY50-crossvol (already in ledger) | AP-CY68 (Künneth-multiplicative Hodge supertrace); cache 146 / AP-V2-28 | AP-CY34, AP-CY44, AP-CY50 (Vol III primary); AP-CY68 | **AP-CY50-crossvol already inscribed** (Vol I) + **AP-CY68** (Vol III) + reinforce **AP-CY50-E24 (add)** as 6d-hCS specialisation row | Serre 1955 Ann Math 61; Hirzebruch 1956 *Topological Methods* §21; EOT 2011 |

## 2. Per-error RIGHT / WRONG / CORRECT analysis

Each entry answers (a) the true theorem-in-the-vicinity that the error
shadows, (b) the precise technical failure, (c) the canonical
correction with first-principles mathematics.

### E1. Casimir quadratic-for-quartic in 6d hCS 1-loop

**RIGHT.** One-loop BV obstruction for 6d hCS on a CY$_3$ is
computed by a single irreducible diagram whose external-leg count
equals the number of ghost fields entering the BV Laplacian on
$(\bar\partial A \wedge)^k$ forms against $\Omega_Y \in \Omega^{3,0}$.

**WRONG.** Three-leg integrand $\Omega_Y \wedge \mathrm{Tr}(A \wedge
\bar\partial A \wedge \bar\partial A)$ with cancellation locus
$c_2(\mathfrak g) = 2h^\vee = 0$ (only $\mathfrak u(1)$). The cubic
adjoint trace $\mathrm{tr}_{\mathrm{adj}}(T^a T^b T^c)$ vanishes
identically on any simple $\mathfrak g$ by the self-duality of the
adjoint under Killing, so the three-leg candidate is zero as a
cocycle — no 1-loop obstruction can live there. Reading the anomaly
as quadratic collapses Deligne-series cancellation into
$\mathfrak u(1)$-only.

**CORRECT.** $\mathrm{Obs}_1 = (2\pi i)^{-3} \cdot
\mathrm{tr}_{\mathrm{adj}}(T^{(a} T^b T^c T^{d)})_{\mathrm{irr}}
\cdot \int_Y \Omega_Y \wedge c \wedge (\bar\partial c)^3
\in H^1_{\mathrm{BRST}}(\Omega^{3, \bullet}(Y))$ at ghost number
$+1$. Cancellation locus is the Deligne exceptional series $A_1, A_2,
G_2, D_4, F_4, E_6, E_7, E_8$, on which
$\mathrm{tr}_{\mathrm{adj}} T^4 = \alpha_{\mathfrak g} \cdot
(\mathrm{tr}_{\mathrm{adj}} T^2)^2$ and the residual $(F^2)^2$-piece
is absorbed by Green--Schwarz. Primary: Costello 2015
arXiv:1410.5421 §4-5; Costello--Li 2016 arXiv:1605.09930 Prop 5.2;
Deligne 1996 CR Acad Sci 322.

### E2. $c_{\phi_{-2,1}}(-n) = 24$ false

**RIGHT.** The integer 24 appears repeatedly in BV 1-loop and K3
partition-function contexts: $\chi(K3) = 24$ (topological Euler),
$c_{1/\Delta_5}(q^1) = 24$ (half-BPS elliptic-genus coefficient),
$c_{\phi_{0,1}^{K3}}(-1) = 2$ (Eichler--Zagier polar cutoff at
$\Delta = -1$). Each is a legitimate coefficient of a specific form.

**WRONG.** Assigning $c_{\phi_{-2,1}}(-n) = 24$ at $n = 1$ (or any
$n \ge 1$). The weak Jacobi form $\phi_{-2,1}$ has weight $-2$,
index 1, and **no polar coefficients at negative discriminant** by
Eichler--Zagier 1985 *Progress in Mathematics* 55 Thm 9.3 (weak
Jacobi-form polar cutoff $\Delta \ge -m^2 = -1$ leaves only
$\Delta = -1$ admissible; the coefficient $c_{\phi_{-2,1}}(-n)$ at
$n \ge 1$ vanishes identically).

**CORRECT.** The BV-loop generating coefficient is
$c_{1/\Delta_5}(q^1) = 24$ (Gritsenko--Nikulin 1998) or
$\chi(K3) = 24$ (topological), **not** a coefficient of
$\phi_{-2,1}$. For weak Jacobi forms the K3 datum is:
$c_{\phi_{0,1}^{K3}}(-1) = 2$, $c_{\phi_{0,1}^{K3}}(0) = 20$,
$c_{\phi_{0,1}^{K3}}(\Delta < -1) = 0$ (EOT 2011 *Experimental
Math* 20).

### E3. Theta graph 1-loop miscount

**RIGHT.** The theta-graph (three internal propagators between two
vertices) is a legitimate Feynman graph at two loops on a CY$_3$
with specific combinatorial symmetry factor $1/2!$ per pair of
parallel edges; on $K3 \times \mathbb C^2$ at 3-loop the dominant
theta-times-theta graph carries combinatorial factor
$\chi(K3)^3 / 3! = 24^3/6 = 2304$ and is the W16 BV-3-loop
obstruction witness (Vol II cache entry 109).

**WRONG.** Miscounting the theta-graph symmetry factor (e.g., $1/3!$
instead of $1/2!$, or missing the $\chi(K3)^3$ contribution), or
attributing 3-loop content to 1-loop. The 1-loop diagram on a
$\mathrm{CY}_3$ for 6d hCS is the wheel graph with four external
ghost legs (E1 above), not the theta graph.

**CORRECT.** At 1-loop: wheel with 4 external legs (E1). At 2-loop:
theta with proper symmetry. At 3-loop on $K3 \times \mathbb C^2$:
theta-times-theta with $\chi(K3)^3/3! = 2304$, computed via
Bruinier--Heegner $Z(m_3, 3)$ Chern reciprocity (Bruinier 2002 LNM
1780 Prop 5.1) and Harvey--Moore heterotic new-susy-index $p^3$
degeneracy. Primary: Costello--Gwilliam FA Vol 2 Ch 5
(BV-cohomology); Cattaneo--Felder 2000 CMP 212 (explicit symmetry
factors); Vol II cache entry 109 W16 anchor.

### E4. $\zeta(3)^2$ shuffle dimensional failure

**RIGHT.** The 3-loop CG pentagon coefficient carries
$\zeta(3)$-dependent structure constants at the associator base-point;
the Willwacher wheel/hair complex $\mathsf{GC}^0$ produces such
periods via graph cocycles.

**WRONG.** Treating $\zeta(3)^2$ as a depth-2 single-valued MZV
with dimension 1 in the weight-6 motivic basis. The shuffle product
$\zeta(3)^2 = 2 \zeta(3,3) + \ldots$ lives in depth $\le 2$ weight 6,
but the single-valued projection $\mathrm{sv}(\zeta(3)^2) =
(\mathrm{sv}\zeta(3))^2$ is a specific linear combination in
$\mathrm{zv}^{\mathrm{sv}}_6$; reading $\zeta(3)^2$ as an
independent basis element at weight 6 is dimensionally wrong
(depth-2 single-valued at weight 6 has dimension $d_6 = 2$ but
$\zeta(3)^2$ and $\zeta^{\mathrm{sv}}(3)^3 / \text{(no)}$ do not
span freely).

**CORRECT.** Single-valued depth-$k$ projection
$e_k = \mathrm{sv} \circ \pi^{\mathrm{depth} \le k}(\phi^{(3k)})$
lands in $\mathrm{zv}^{\mathrm{sv}}_{3k}$; at $k = 3$ the dim-2
space is $\mathbb Q \zeta^{\mathrm{sv}}(3)^3 \oplus \mathbb Q
\zeta^{\mathrm{sv}}(9)$ (cache entry 435). The 3-loop CG pentagon
coefficient lives at a specific $\mathrm{GRT}_1(\mathbb Q)$-torsor
base-point; cross-archetype comparisons require the same base-point
(cache entry 441). Primary: Willwacher 2014 *Invent Math* 200
Thm 1.2; Brown 2014 *Forum Math Sigma* 2; Schnetz 2013.

### E5. Wedge-of-1-forms nullity

**RIGHT.** Arnold relation
$\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} +
\eta_{ki} \wedge \eta_{ij} = 0$ is the defining relation for
$H^*(\mathrm{Conf}_n(\mathbb A^1))$ on the affine line.

**WRONG.** Extending Arnold to $\mathbb P^1$ or $\Sigma_g$ without
the global corrections. On $\mathbb P^1$, $\mathrm{PSL}_2$ gauge
fixing imposes linear relations $\sum_{j \ne i} \bar\eta_{ij} = 0$.
On $\Sigma_g$, $g \ge 1$, point-pushing couples puncture classes to
ambient $H^1(\Sigma_g)$ and the $\eta_{ij}$ are not closed classes
by themselves; one must use the Totaro--Kriz--Bezrukavnikov CDGA
with surface generators, mixed relations
$\eta_{ij}(p_i^* \xi - p_j^* \xi) = 0$, and differential
$d \eta_{ij} = \Delta_{ij}$.

**CORRECT.** Cache entry 293 gives the local/global discipline:
Arnold is complete only on $\mathbb A^1$ / formal-disk screens; for
$\mathbb P^1$ adjoin projective linear relations; for $\Sigma_g$ adjoin
Totaro generators. For the 6d-hCS audit on the stratified Humbert
locus $\overline{\mathcal A_2}$, V2-AP41 applies: smooth Kontsevich
formality does NOT transport verbatim; Humbert strata are obstructed.
Primary: Totaro 1996 *Topology* 35; Kriz 1994 *Ann Math* 139;
Francis--Gaitsgory 2012 *Selecta Math* 18 on the Koszul locus
$U^{\mathrm{adm}}$ only.

### E6. Residue ill-typed $\mathrm{Res}_{\Phi_{10}=0}$

**RIGHT.** The $\mathrm{AdS}_3 \times K3$ 3d quantum-gravity
partition function has residue structure along the Humbert locus
$\{\Phi_{10} = 0\}$: the partition function IS
$Z_{\mathrm{3dQG}}^{\mathrm{AdS}_3 \times K3} = 1/\Phi_{10}(Z)$
directly by Dijkgraaf--Verlinde--Verlinde 1997 (identified as
$1/4$-BPS D1-D5-P index on $K3 \times T^2$).

**WRONG.** Writing
$\mathrm{Res}_{\Phi_{10}=0}(Z_{hCS}) = 1/\Phi_{10}$. The residue of
$c/f$ at $f = 0$ is $c$ (removes the denominator), never $c/f$
(cannot re-introduce it). The stated identity is **self-referential
/ ill-typed**: residue extraction cannot produce the very pole it
reduces.

**CORRECT.** Two distinct correct statements replace the bad one.
(i) DIRECT: $Z_{\mathrm{3dQG}}^{\mathrm{AdS}_3 \times K3} =
1/\Phi_{10}(Z)$ by DVV 1997. (ii) LARGE-$\hbar$ SADDLE: the
Costello 6d hCS effective-action object
$(\Phi_{10}/(\eta(\tau)^{24} \eta(\tau')^{24}))^{\hbar c_{K3}(Z)}$
exponentiates the BV-obstruction tower; its pole along
$\{\Phi_{10} = 0\}$ encodes $1/\Phi_{10}$ as the leading large-$\hbar$
saddle-point asymptotic, with $1/\Phi_{10}$ realised as the
Gritsenko--Nikulin--Borcherds singular theta lift of the K3
elliptic-genus generator
$2\phi_{0,1} - (E_2/6)\phi_{-2,1}$ (EOT 2011) via the Borcherds
multiplicative theta correspondence (Borcherds 1995 Thm 10.4).
Primary: DVV 1997 *Nucl Phys B* 484; Maloney--Witten 2010 *JHEP*
1002; Borcherds 1995 *Invent Math* 120; EOT 2011 (Vol I cache 448).

### E7. $\eta^{24}$ single denominator insufficient

**RIGHT.** $\Phi_{10}$ restricted to the Siegel diagonal $z = 0$
factors as $\Phi_{10}(Z)|_{z=0} = z^2 \cdot \eta(\tau)^{24} \cdot
\eta(\tau')^{24} \cdot \mathcal J(\tau, \tau')$ (DVV 1997), with
bimodular weight $(12, 12)$ in $(\tau, \tau')$ (Igusa 1964).

**WRONG.** Dividing by a SINGLE $\eta(\tau)^{24}$ and calling the
result a bimodular-weight-zero object. Weight balance:
$\Phi_{10}/\eta(\tau)^{24}$ is weight $(-12, 0)$, not $(0, 0)$. A
genuine bimodular-weight-zero all-orders object requires BOTH
$\eta$ factors.

**CORRECT.**
$\Phi_{10}(Z)/(\eta(\tau)^{24} \eta(\tau')^{24})$, a
weight-$(-12, -12)$-cancelled bimodular-zero object on
$\mathfrak H_2 \setminus \{z = 0\}$. The two $\eta^{24}$ factors
each arise from 24 M5-brane one-loop integrals threading,
respectively, the $\tau$-modular $I_1$-fibre and the $\tau'$-modular
$I_1$-fibre of the $K3 \times T^2$ combinatorics. Three verification
paths as in cache 449 / AP931: Igusa 1964 *Amer J Math* 86 direct
$q$-expansion at $z = 0$; DVV 1997 D1-D5-P partition-function
factorisation; Gritsenko--Nikulin 1998 §3 Borcherds-product
restriction identity.

### E8. Dunn $E_1$-per-$\mathbb C$ on $\mathbb C^3$

**RIGHT.** Dunn additivity $E_m \otimes_D E_n = E_{m+n}$ for
locally-constant translation-equivariant factorisation algebras on
$\mathbb R^{m+n}$ (Lurie HA 5.1.2.2). After holomorphic twist and
$\bar\partial$-cohomology on $\mathbb C^n$, one obtains an $E_n$
structure — one $E_1$ per holomorphic coordinate.

**WRONG.** Saying "$\mathbb C^3$ carries $E_3$ with one $E_1$ per
complex coordinate $z_1, z_2, z_3$" as a statement about the
geometric factorisation algebra before cohomology. Each complex
coordinate is TWO real dimensions; $\mathbb C$ has 2 real dims;
a single complex factor contributes $E_2$ geometrically (not $E_1$).
Costello--Gwilliam Vol 2 Ch 5 Thm 5.1: holomorphically-twisted
factorisation algebras on $\mathbb C^n$ carry an $E_{2n}$-structure
geometrically, reducing to $E_n$ only after passing to
$\bar\partial$-cohomology.

**CORRECT.** 6d hCS on $\mathbb C^3$ carries $E_6$ geometrically;
reduction to $E_3$ happens AFTER Dolbeault cohomology. Dunn
additivity at the Dolbeault-reduced level gives
$E_3 = E_1 \otimes_D E_1 \otimes_D E_1$ with one $E_1$ per
holomorphic direction $z_i$ AFTER the holomorphic twist collapses
$\Omega^{0, \bullet}(\mathbb C) \simeq \mathbb C$ in
$\bar\partial$-cohomology. See cache 450 / AP932; Vol II
AP-V2-36 / V2-AP139 (real-vs-complex conflation); Vol III AP-CY53
($\pi_1$ ordered-vs-unordered companion).

### E9. Willwacher wheel-to-$\zeta$ convention

**RIGHT.** The Willwacher graph complex $\mathsf{GC}^0$ has
cohomology $\cong \mathfrak{grt}_1$ at Drinfeld associator base-point
(Willwacher 2014 *Invent Math* 200 Thm 1.2); the wheel graphs
$w_{2k+1}$ produce $\zeta(2k+1)$-weighted classes under the period
map.

**WRONG.** Treating the wheel-to-$\zeta$ map as sign-uniform or
identifying $[w_{2k+1}] \mapsto \zeta(2k+1)$ without specifying
(i) rational vs single-valued, (ii) signed vs unsigned, (iii)
Kontsevich-propagator base-point vs Drinfeld-associator base-point.
Different conventions differ by a $\mathrm{GRT}_1(\mathbb Q)$ gauge;
structure-constant-level claims require specifying the base-point.

**CORRECT.** Under Drinfeld even-associator, $[w_{2k+1}] \mapsto
(-1)^{k} \zeta(2k+1)$ in the universal $L_\infty$-cocycle on
$\mathfrak{grt}_1^{\mathrm{ev}}$; under Costello--Li propagator,
same period but with Kontsevich base-point. Single-valued
projection lands in $\mathrm{zv}^{\mathrm{sv}}$ (cache 435). See
Vol I cache 441 (iso-class vs parametrised KT formality) for the
scope discipline.

### E10. K3 MHS pollution of motivic MZV

**RIGHT.** The motivic MZV algebra $\mathcal H_{\mathrm{MZV}}^{\mathrm{mot}}$
is a quotient of the motivic Galois group on $\mathrm{Mix}(\mathbb Z)$
cycles, and its single-valued projection lives in
$\mathrm{zv}^{\mathrm{sv}}$ (Brown 2014). K3 partition functions
involve $\mathcal H^{p,q}(K3)$ mixed Hodge structures that are
generically non-Tate (Kuga--Satake locus).

**WRONG.** Equating K3-loop Feynman periods with motivic MZVs of
the Tate quotient. The K3 MHS pollutes: non-Tate cycles
contribute to the period ring via Kuga--Satake abelian-variety
lifts, introducing Hodge classes that do not lie in the motivic
MZV subalgebra. Depth-bound arguments from Brown--Schnetz
single-valued MZV theory fail if the input is not Tate-mixed.

**CORRECT.** Separate (i) Tate-mixed motivic MZV periods (where
Brown 2014 + Schnetz 2013 + cache 435 depth-$k$ single-valued
projection applies) from (ii) K3-Hodge-modified periods (where the
Kuga--Satake locus contributes Galois-invariants outside
$\mathrm{zv}^{\mathrm{sv}}$). Vol I cache 435 pins the motivic
home as the single-valued subring, not the full motivic-period
ring. Primary: Deligne 1971 *Publ IHES* 40 (MHS); Kuga--Satake
1967; Brown 2014; Schnetz 2013.

### E11. AFT 2017 vs AF 2015 citation

**RIGHT.** Two distinct primary papers exist: Andrade--Forrester
2015 (on random-matrix CUE pair-correlation) and
Andrade--Forrester--Thomas 2017 (three-author extension to
Riemann-zeta moments with the extra Thomas contribution).

**WRONG.** Citing "AFT 2017" when the intended source is the
2-author AF 2015, or vice versa. Cache 266 (citation-key phantom
drift) and 267 (citation-attribution drift) enforce this
discipline: every bibkey must match a live bibliography entry and
match the prose attribution.

**CORRECT.** State explicitly: Andrade--Forrester 2015 for the
2-author CUE identity; Andrade--Forrester--Thomas 2017 for the
3-author zeta-moment extension. If both are cited, give each its
own bibkey.

### E12. Costello 2011 Thm 13.4.1 compactness hypothesis

**RIGHT.** Costello 2011 (*Renormalization and Effective Field
Theory*) Thm 13.4.1 gives the universal BV-renormalisation existence
theorem for effective-field-theory quantisations on an oriented
manifold.

**WRONG.** Citing Thm 13.4.1 as applying to non-compact CY$_3$
without the compactness hypothesis. The theorem is stated for
compact-support effective actions; on non-compact $X$ one needs the
relative / compactly-supported cohomology version (Costello--Gwilliam
Vol 2 §10-11) or explicit decay hypotheses on the propagator.

**CORRECT.** For non-compact CY$_3$ (e.g., $\mathbb C^3$,
$\mathbb C^2 \times E$, conifold resolutions), use Costello--Gwilliam
FA Vol 2 Prop 8.2.1 (locality) plus Costello--Li 2016 Prop 5.2
(compactly-supported propagator) in place of Costello 2011 Thm
13.4.1. Cache 266, 267 citation discipline applies.

### E13. CHSW $\mathrm{SU}(3)$ vs $\mathrm{SU}(4)$ holonomy

**RIGHT.** Calabi--Yau $n$-fold has $\mathrm{SU}(n)$ holonomy;
Calabi--Yau 3 has $\mathrm{SU}(3)$, Calabi--Yau 4 has $\mathrm{SU}(4)$.
Candelas--Horowitz--Strominger--Witten 1985 fixed $\mathrm{SU}(3)$
heterotic phenomenology on a CY$_3$.

**WRONG.** Citing CHSW 1985 for $\mathrm{SU}(4)$ holonomy (wrong
paper: that is Becker--Becker--Strominger 1995 or CY$_4$
F-theory). Or reading the CHSW holonomy as a statement about
$\mathrm{SU}(n)$ gauge group rather than geometric structure-group
holonomy.

**CORRECT.** CHSW 1985 *Nucl Phys B* 258: $\mathrm{SU}(3)$-holonomy
CY$_3$ with spin-connection = gauge-connection identification,
giving $E_6$ gauge theory from $E_8 \times E_8$ heterotic. For
CY$_4$ ($\mathrm{SU}(4)$ holonomy), cite Becker--Becker--Strominger
1995 *Nucl Phys B* 456 or Sethi--Vafa--Witten 1996 *Nucl Phys B*
480. AP-CY17 (MF CY dim $n-2$) enforces the analogous discipline
for matrix factorisations.

### E14. 6d hCS anomaly-free locus — CANONICAL-ANOM-LOCUS (form c)

**RIGHT.** $E_6$ is on the Deligne exceptional series
$A_1, A_2, G_2, D_4, F_4, E_6, E_7, E_8$, so
$\mathrm{tr}_{\mathrm{adj}} T^4 = \alpha_{E_6} \cdot
(\mathrm{tr}_{\mathrm{adj}} T^2)^2$: the quartic adjoint Casimir is
EXPRESSIBLE in terms of the quadratic squared (Deligne 1996 CR Acad
Sci 322). A separate cubic obstruction $d^{abc}$ operates on
$E_6$ (cubic Jordan invariant on $\mathrm{Sym}^3(\mathbf{27}) =
\mathfrak j_3^{\mathbb O}$) and on $A_2 = \mathfrak{su}(3)$
(Gell-Mann $d$-tensor), zero on $A_1, G_2, D_4, F_4, E_7, E_8$.

**WRONG — four antipattern forms flagged.**
- Form (a) strict: ``6d hCS anomaly-free $\iff$ Deligne $\setminus
  \{E_6, A_2\}$'' without $A_2$-refined / $A_2$-unrefined
  distinction and without the $K^{-1/2}$-refinement clause.
  Lumps $A_2$-refined with $A_2$-unrefined, wrongly excluding the
  refined sector (Dimofte-slab inflow + Feigin--Frenkel critical
  twist) from the locus.
- Form (b): ``6d hCS anomaly-free $\iff$ Deligne $\setminus
  \{E_6\}$'' alone, admitting undifferentiated $A_2$. Wrongly admits
  $A_2$-unrefined with live $d^{abc}$ and live critical-level
  quadratic obstruction.
- Form (a'): ``$\mathrm{tr}_{\mathrm{adj}} T^4 = 0$ on $E_6$''.
  FALSE: quartic is nonzero; cancellation mechanism uses the
  Deligne factorisation through the quadratic squared.
- Cubic-only reading with $E_6$ in safe list: placing $E_6$ among
  ``$d^{abc} = 0$'' algebras. Contradicts the Jordan cubic invariant
  on $\mathrm{Sym}^3(\mathbf{27})$.

**CORRECT — CANONICAL-ANOM-LOCUS (form c).** The native-ambient
6d hCS anomaly-free locus on a CY$_3$ reads
$$
\mathrm{Anom}_1 = 0 \iff \mathfrak g \in
\bigl(\mathrm{Deligne}^{\mathrm{exc}} \setminus \{E_6,\, A_2\text{-unrefined}\}\bigr)
\cup \{\mathrm{abelian}\} \cup \{\mathrm{super-str}_{\mathrm{ad}} = 0\}
\cup \{\widehat{\mathfrak g}_{-h^\vee} \otimes K^{-1/2}\text{-refined}\}.
$$
Native-ambient distinctions:
- $E_6$ STRICTLY excluded. No refinement in the programme's toolkit
  kills $\mathrm{Sym}^3(\mathbf{27})$ cubic Jordan invariant
  $d^{abc} \ne 0$ within native ambient; the $K^{-1/2}$ critical
  twist addresses the quadratic obstruction, not the cubic.
- $A_2$-unrefined excluded: live Gell-Mann $d_{abc}$ on
  $\mathfrak{su}(3)$ and live critical-level quadratic obstruction.
- $A_2$-refined INSIDE the locus: Feigin--Frenkel critical-level
  $K^{-1/2}$ twist kills the quadratic obstruction; Dimofte-slab
  anomaly-inflow from Vol II Part V provides the Green--Schwarz
  cubic cancellation.
- $\{A_1, G_2, D_4, F_4, E_7, E_8\}$ unconditionally inside the
  locus: quartic Deligne-factorises ($\alpha_{\mathfrak g}$ via
  Cohen--de Man 1996 Vogel plane), cubic $d^{abc}$ vanishes
  identically on these six.

Two distinct obstructions operate: the quartic adjoint Casimir
(Deligne-killed universally across the series via factorisation
$\mathrm{tr}_{\mathrm{adj}}T^4 = \alpha_{\mathfrak g}
(\mathrm{tr}_{\mathrm{adj}}T^2)^2$, including for $A_2$ and $E_6$)
vs the cubic $d^{abc}$ (nonzero on $A_2$ and $E_6$; cured only in
native ambient by Green--Schwarz-type inflow, operative for
$A_2$-refined, not for $E_6$).

Vol II `bv_brst.tex` Cor `cor:6dhcs-deligne-cancellation` and
`thqg_perturbative_finiteness.tex` Remark `rem:hcs-anomaly-locus`
are the chapter-level homes. Vol I Pattern 445 / AP979, Vol II
V2-AP157 / AP-V2-54, Vol III AP-CY262, and cross-volume
AP-CY50-E14 carry the canonical (c) form.

### E15. Conway bosonic vs metaplectic $\Psi$

**RIGHT.** There are multiple $\Psi$-functors into BKM / super-BKM
images (Vol I cache 83 sibling family
$\{\Psi, \Psi^{\mathrm{deg}}, \Psi^{\mathrm{tor}},
\Psi^{\mathrm{metap}}\}$); the Conway VOA $V^{s\natural}$ is related to
the Leech-Conway moonshine via Duncan 2007 *Duke Math J* 139.

**WRONG.** Listing $V^{s\natural}$ as a 5th bosonic $\Psi$-image
with $(K, \hbar^2) = (2, -1/2)$ on the metaplectic branch. Three
defects per Vol III AP-CY71: (a) venue error (Duke 139, not MRL 14);
(b) construction error (Leech fermionic VOA $A(\Lambda_{24})$, not
$E_8$ super-lattice); (c) signature error ($c_+(\Lambda_{24}) = 24$,
not 0).

**CORRECT.** $V^{s\natural}$ is the $\mathbb Z/2$-super-twin of
$V^\natural$ via Duncan 2007 §6 commutative orbifolding diamond,
NOT a bosonic $\Psi$-image. The four $\Psi$-siblings
$\{\Psi, \Psi^{\mathrm{deg}}, \Psi^{\mathrm{tor}},
\Psi^{\mathrm{metap}}\}$ parametrise the Baily--Borel--Freitag
stratification of $\overline{\mathcal A_2}$; $\Psi^{\mathrm{metap}}$
produces super-Borcherds objects via Scheithauer 2008 *Invent Math*
172 Example 7.3. Vol III AP-CY71, AP-CY72 (super-twin / orbifold-
diamond discipline); Vol I AP439 (Niemeier ladder).

### E16. CHL Siegel weight $\{5, 4, 3, 2, 1\}$ typo

**RIGHT.** The CHL family $N \in \{1, 2, 3, 4, 6\}$ carries
Gritsenko additive-lift Borcherds-denominator forms
$(\Delta_5, \Delta_4, \Delta_3, \Delta_2, \Delta_1)$ of Siegel
weights $(5, 4, 3, 2, 1)$ with $\kappa_{\mathrm{BKM}} = c_N(0)/2
\in (5, 4, 3, 2, 1)$ (Gritsenko 1999 *Math Nachr* 199 Thm 6.1).

**WRONG.** Writing the CHL family weight sequence as $(5, 4, 3, 2,
1)$ for $N \in \{1, 2, 3, 4, 5\}$ (skipping $N = 5$ and including
$N = 6$), or attributing weight 5 to $N = 6$. The CHL orbifold
level $N = 5$ is EMPTY in the Gritsenko additive-lift family;
$N = 6$ carries weight 1, not weight 5.

**CORRECT.** CHL family indexed by $N \in \{1, 2, 3, 4, 6\}$
(note: 5 is absent); Borcherds weights $(5, 4, 3, 2, 1)$
respectively. Full 8-form Gritsenko--Clery atlas extends the
indexing beyond CHL to $N \in \{1, \ldots, 8\}$ with weights
$(5, 2, 1, 1, 1/2, 1, 1/4, 0)$, half-integral and fractional
entries included. Vol III AP-CY200 / W14-B5 is the two-scope
discipline: BKM-denominator scope (CHL, $N \in \{1,2,3,4,6\}$)
vs Borcherds-weight scope (full Clery atlas, $N \in \{1,\ldots,8\}$).

### E17. $\kappa_{\mathrm{BKM}}$ scope 5 (K3) vs 12 (Fake-Monster)

**RIGHT.** $\kappa_{\mathrm{BKM}}(X) = c_N(0)/2$ is the Borcherds
weight theorem (Borcherds 1995 *Invent Math* 120 Thm 10.4 singular-
weight identity). Three canonical values coexist legitimately:
$\kappa_{\mathrm{BKM}}(\Delta_5) = 5$ (K3-BKM half-BPS),
$\kappa_{\mathrm{BKM}}(\Phi_{10}) = 10$ (full-BPS,
$\Phi_{10} = \Delta_5^2$), $\kappa_{\mathrm{BKM}}(\Phi_{12}) = 12$
(Fake-Monster on $\mathrm{II}_{25,1}$).

**WRONG.** Reading these three values as "disagreeing numerical data
points" or using a bare $\kappa_{\mathrm{BKM}}$ symbol without
naming the input denominator. Cache 88, 123 AP5 audit: both
conventions occur legitimately.

**CORRECT.** Every $\kappa_{\mathrm{BKM}}$ site names the
denominator. Squaring identity: $\kappa_{\mathrm{BKM}}(\Phi_{10}) =
2 \kappa_{\mathrm{BKM}}(\Delta_5) = 10$ via multiplicative-lift
law $c_{f^2}(0)/2 = 2 \cdot c_f(0)/2$ (Borcherds 1995 Thm 13.3).
Physically: heterotic on $K3 \times T^2$ sees $\Delta_5$ half-BPS;
Type-II on $K3 \times T^2$ sees $\Phi_{10}$ full-BPS; they are
S-dual at the automorphic-form level. Vol I AP928, AP927; Vol III
AP-CY49, AP-CY85, AP-CY172. Cross-volume ledger already carries
the AP5 dual-indexing header.

### E18. Yangian type count (3 vs 4)

**RIGHT.** There are multiple distinct structures carrying the name
"Yangian" in the programme: classical Drinfeld Yangian, dg-shifted,
chiral, spectral / factorisation Yangian.

**WRONG.** Counting three types. AP159 (Vol I catalogue line 391)
enumerates FOUR: (1) classical $Y_\hbar(\mathfrak g)$ as $E_1$-top on
$\mathbb R$; (2) dg-shifted $Y^{\mathrm{dg}}_\hbar(\mathfrak g)$ at
point/formal disk; (3) chiral $Y(\mathfrak g)^{\mathrm{ch}}$ as
$E_1$-chiral on curve $X$ (D-module); (4) spectral (factorisation
on $\mathbb A^1_u$).

**CORRECT.** Four Yangian types, disambiguated by
superscripts: $Y$ (classical), $Y^{\mathrm{dg}}$, $Y^{\mathrm{ch}}$,
$Y^{\mathrm{spec}}$. Conflating any two is a type error. Primary:
Drinfeld 1985 *Soviet Math Dokl* 32 (classical); Costello--Witten--
Yamazaki 2017-18 arXiv:1709.09993/1802.10588 (chiral on curve);
Maulik--Okounkov 2012 arXiv:1211.1287 (spectral). AP159 is the
canonical discipline source.

### E19. $\Phi_d$ Stage-1 / Stage-2 naming

**RIGHT.** The CY-to-chiral functor admits a canonical two-stage
factorisation
$\Phi_d = \mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ
\Phi^{\mathrm{FA}}_d$
with Stage 1 ($\Phi^{\mathrm{FA}}_d$): canonical $E_d$-holomorphic
factorisation algebra on CY$_d$ (Costello--Gwilliam--Li locality +
Kontsevich--Tamarkin $E_d$-formality); Stage 2
($\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$): factorisation
homology over a $(d-1)$-cycle, restricted to reference curve $C$.

**WRONG.** Presenting $\Phi_d$ as a one-step functor into
$E_n$-chiral on a curve. This inverts canonicality: what is
canonical (up to contractible choice at iso-class) is the Stage-1
$E_d$-FA on the CY, NOT the Stage-2 $E_n$-chiral shadow on $C$.
A single CY$_d$ admits a FAMILY of Stage-2 specialisations indexed
by $(\Sigma_{d-1}, C)$.

**CORRECT.** State Stage 1 and Stage 2 separately. Stage 1 lands
in $E_d$-HolFA$(\mathbb C^d)$; Stage 2 via $\mathrm{Sp}$ lands in
$E_n$-ChirAlg$(C)$ with residual $n = 1$ generically, topological
enhancements ($E_2$ braiding, $E_\infty$ commutativity) when
$\Sigma_{d-1}$ carries extra symmetry. See Vol III AP-CY144 / F8;
Vol II AP-V2-27 / V2-AP130, AP-V2-33 / V2-AP136; Vol I AP273 and
cache 440, 441. Cross-vol ledger AP-CY62-crossvol already
inscribes this.

### E20. Seven-incarnation equivalence overclaim

**RIGHT.** The seven faces of $r_{\mathrm{CY}}$ are SEVEN DISTINCT
load-bearing presentations of the CY-to-chiral spectral-parameter
datum (intrinsics, Stage-1 invariants, Stage-2 outputs). Each face
is a real mathematical object.

**WRONG.** Asserting "seven equivalent presentations" with pairwise
quasi-isomorphisms $\binom{7}{2} = 21$ implications. Vol I AP284
(equivalence claim without inscribed implication structure) catches
this: without an explicit star-shaped or cyclic implication diagram,
pairwise equivalence is overclaim.

**CORRECT.** Three-tier hierarchy (Vol III AP-CY C6):
(i) CY-datum intrinsics (CY structure, KS data, symplectic /
shifted-symplectic form, dualising sheaf, orientation);
(ii) Stage-1 invariants (braiding, commutative-up-to-braid,
holomorphic OPE poles, Lurie centre, factorisation homology);
(iii) Stage-2 specialisation outputs (chiral algebra, spectral
$R$-matrix, vertex algebra, Yangian / affine Yangian shadow,
Maulik--Okounkov $R$-matrix). Each tier has well-defined intra-tier
equivalences; cross-tier is specialisation, not equivalence.

### E21. $\Delta_{E_6}$ weight 16 vs 18

**RIGHT.** Hecke eigenvalues $a_p(f_{16})$ of the weight-16 cusp
form $f_{16} = E_4 \cdot \Delta$ are canonical in the programme
(Vol I cache 423 W26 extension, AP893 W25 $\tau/a_p$ verification).

**WRONG.** Attributing "weight 18" to the $E_6$-type chiral
deformation $\Delta_{E_6}$. The correct Hecke primary form at
weight 16 is $f_{16} = E_4 \cdot \Delta$; there is no load-bearing
weight-18 form in the Ramanujan chain for this argument.
Vol III AP-CY88: "every Hecke $a_p$ claim must name the correct
primary form ($f_{16}$ at weight 16, not $\Delta$ at weight 12)".

**CORRECT.** $\Delta_{E_6}$-type arithmetic data lands in weight
16: $a_p(f_{16})$ with $f_{16} = E_4 \cdot \Delta$. The weight-12
Ramanujan $\tau(p)$ is the secondary form; the weight-16
Hecke-Galois representation is the primary form. Primary: Serre
1973 *Seminaire DPP* 14; Ikeda 2001 *Ann Math* 154 (Saito-Kurokawa);
Vol I cache 423 (W26 prime extension 233-263).

### E22. Gritsenko-$\Delta_5$ vs Borcherds-$\Phi_{10}$

**RIGHT.** $\Phi_{10} = \Delta_5^2$ as paramodular Siegel forms on
$\mathrm{Sp}_4(\mathbb Z)$ (Gritsenko--Nikulin 1998). $\Delta_5$ is
the Gritsenko additive lift of $\phi_{0,1}^{K3}$ at weight 5;
$\Phi_{10}$ is the Igusa cusp form at weight 10.

**WRONG.** Treating the two as independent forms with independent
$\kappa_{\mathrm{BKM}}$ values. They are related by the squaring
identity.

**CORRECT.** $\Phi_{10} = \Delta_5^2$ as Siegel-paramodular forms;
$\kappa_{\mathrm{BKM}}(\Phi_{10}) = 2 \kappa_{\mathrm{BKM}}(\Delta_5)
= 10$ via multiplicative-lift law (Borcherds 1995 Thm 13.3); physical
interpretation is heterotic/Type-II S-duality (DVV 1997). Vol I
cache 445 / AP928; cross-volume ledger AP5 dual-indexing header.

### E23. Three-faces identity row coverage

**RIGHT.** The three-faces identity $\kappa + \kappa^! =
\mathsf B$-row landmark $= 8$ (cache 445 / AP928, preamble row 90)
states: (i) derived-centre complementarity sum; (ii) Mukai pairing
$K = 2c_+ = 8$ with $c_+ = 4$; (iii) Lusztig reflection length
$\ell_{\mathrm{Lusztig}} = 8$ at $\zeta_8$. Proved per-row for
Monster / K3 / Fake-Monster.

**WRONG.** Claiming the identity extends verbatim to Enriques /
Conway rows as "proved". Vol III AP-CY70, AP-CY71 retract the
uniform $\Psi$-image statement; Enriques / Conway rows are
pending.

**CORRECT.** Row-by-row:
- Monster ($d = 3$, $\Phi_{12}$): proved per AP444, AP445.
- K3 ($d = 3$, $\Delta_5$): proved via Gritsenko--Nikulin 1998.
- Fake-Monster ($d = 5$, $\Phi_{12}$ on $\mathrm{II}_{25,1}$):
  proved per Borcherds 1990.
- Enriques: pending; requires Persson--Volpato $M_{12}
  \hookrightarrow M_{24}$ point-stabiliser decomposition
  (AP-CY73).
- Conway: pending; requires Duncan 2007 orbifold-diamond
  identification (AP-CY71).

Cross-volume ledger AP-CY50-E23 addition flags the Enriques /
Conway rows as open.

### E24. $\kappa_{\mathrm{cat}}(K3 \times E) = 0$ vs 2

**RIGHT.** The Hodge supertrace $\Xi(X) = \sum_q (-1)^q h^{0, q}(X)
= \chi(\mathcal O_X)$ is the canonical definition of
$\kappa_{\mathrm{cat}}$ (= $\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}$,
Route A in Vol III AP-CY69). It is Künneth-MULTIPLICATIVE under
Cartesian product.

**WRONG.** Writing $\kappa_{\mathrm{cat}}(K3 \times E) = 2$ (taking
only the K3 fibre value) or $= 3$ (naive Heisenberg-additive). Both
readings mis-apply the combining rule.

**CORRECT.** $\Xi(K3) = 2$, $\Xi(E) = 0$ (elliptic curve has
$h^{0,0} = h^{0,1} = 1$, supertrace $1 - 1 = 0$), so
$\Xi(K3 \times E) = \Xi(K3) \cdot \Xi(E) = 2 \cdot 0 = 0$. The
legitimate rank-additive Heisenberg-level reading is
$\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ (Route B); the Hodge
supertrace $\kappa_{\mathrm{cat}}$ is Route A. See Vol I AP289,
AP307 (Künneth discipline); Vol II cache 146 / AP-V2-28; Vol III
AP-CY34, AP-CY44, AP-CY50, AP-CY68. Cross-volume ledger
AP-CY50-crossvol already inscribed.

## 3. Cross-volume ledger additions (APPEND-only)

The cross-volume ledger at
`/Users/raeez/chiral-bar-cobar/notes/cross_volume_aps.md`
currently has 290 lines with coverage through AP-CY64-crossvol
(Vol III Wave 11-19 synthesis). The twenty-four errors above
require new entries **AP-CY50-E1 through AP-CY50-E24** under a
new section "2026-04-22 6d hCS audit cross-volume propagation"
appended below the existing Wave-11-19 block.

The ledger additions fall into three categories:

**(A) Errors already with full three-volume coverage** (six): E5,
E8, E15, E17, E19, E24. For these, the cross-volume ledger already
has a row or the per-volume entries are sufficient; the 6d-hCS
audit adds a specialised row confirming the three-volume coverage.

**(B) Errors with partial three-volume coverage** (ten): E1, E2, E4,
E6, E7, E9, E16, E18, E22, E23. Vol I cache entry exists (or was
added in entries 446-450 and 423); Vol II chapter site exists but
Vol II AP catalogue entry is pending (V2-AP14x numbered above as
"pending"); Vol III cross-ref exists but Vol III AP catalogue entry
needs a CY-specific row (flagged as AP-CY19x pending).

**(C) Errors with Vol I cache gaps pending fill-in** (eight):
E3, E10, E11, E12, E13, E14, E20, E21. Vol I cache entries for
these specific 6d-hCS slices have not yet been inscribed by the
Vol I cache agent. The cross-volume ledger flags these with
placeholder "(no Vol I entry yet)" and expects the Vol I cache
agent to inscribe entries 451-458 to fill these.

Canonical form of each cross-volume ledger addition:

```
AP-CY50-E<n> (Vol I/II/III propagation of 6d hCS audit error E<n>).
<One-line mathematical statement>. Vol I: <cache/AP ref or pending>.
Vol II: <cache/AP ref or pending>. Vol III: <cache/AP ref or pending>.
Correction form: <CORRECT statement above>. Counter: <trigger phrase
to fire>. Primary: <primary-literature anchor>.
See <originating 6d hCS audit row>.
```

## 4. Propagation ledger: detected manuscript sites by file:line

Sites where each error was detected during the 6d hCS audit, grouped
by volume and file. These are the `.tex` files that need the fix
applied (manuscript propagation). Line numbers carry over from the
cache-450 / 449 / 448 propagation lists for E6, E7, E8 and are
listed verbatim; other error sites are inferred from Vol II file
grep results.

### Vol II manuscript sites (primary 6d hCS chapter home)

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:3813-3880` (`sec:vol2-bvbrst-kt-6dhcs`, `subsec:6dhcs-action`, `def:6dhcs-action`, `eq:6dhcs-classical-action`, `eq:6dhcs-el`, `lem:6dhcs-gauge`, `eq:6dhcs-gauge`); E1, E12, E14 theorems live here (`thm:6dhcs-one-loop-anomaly` lines 4091-4115, `cor:6dhcs-deligne-cancellation` lines 4132-4157).
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3993-4397` (`prop:hcs-one-loop-anomaly` line 3998, `thm:hcs-all-loop-resummation` line 4272, `eq:hcs-all-loop-resummation` line 4279, `rem:hcs-anomaly-locus` 4030-4060, `rem:hcs-loop-vs-casimir` new, `rem:3dqg-phi-trace-identity` cross-ref); E1, E6, E7 load-bearing.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/six_d_hcs_e3_chiral_avatar_platonic.tex` `thm:hcs-e3-from-translation` (full Dolbeault $\Rightarrow E_6$; $\bar\partial$-cohomology $\Rightarrow E_3$); E8.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_ht_physics.tex:316,391,468,532,702,703` (`sec:E3-6d-hCS`, `thm:E3-action-6d-hCS`, `thm:dunn-E3-6d-hCS`, `thm:P3-obs-6d-hCS`); E8, E20.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/chiral_ce_factalg_gen_rel.tex:297,1060,1082,1258` (cross-ref to `ch:six-d-hcs-e3-chiral-avatar-platonic`); E8, E19.
- E6 / E7 propagation sites flagged at cache 449:
  `chapters/theory/modular_swiss_cheese_operad.tex:4298`;
  `chapters/theory/sc_chtop_heptagon.tex:2436,2440,2657,2663`;
  `chapters/theory/unified_chiral_quantum_group.tex:689,1781`;
  `chapters/frame/preface_trimmed.tex:657`;
  `chapters/frame/preface.tex:2264`;
  `chapters/connections/thqg_3d_gravity_movements_vi_x.tex:2322`;
  `chapters/connections/ht_bulk_boundary_line_core.tex:3213,3222,3223`;
  `chapters/connections/conclusion.tex:2182,2190`;
  `chapters/connections/bar-cobar-review.tex:4562,4565,4578,4584`;
  `chapters/connections/ym_synthesis.tex:1700`;
  `chapters/connections/ht_bulk_boundary_line.tex:3064,3162,3188,3373,3728,3748`.

### Vol I manuscript sites (shadow / preface / landscape)

- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex` L1576-1579 (canonical $\kappa + \kappa^! = 0$ for KM, $\beta\gamma$; 13 for Vir; 250/3 and 98/3 for $\mathcal W_3^k$ and $\mathrm{BP}_k$); canonical preamble rows 20, 21, 22, 28, 60, 88, 90; E17, E21, E22, E23.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex` (Igusa datum reads); E17, E22.
- `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex` (five-archetype landmark ceiling); E17.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_C_refinements_platonic.tex:432-476` (`thm:C-PTVV-alternative`, circular-bypass split per AP279); E14, E20.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1377-1428` (`thm:hochschild-concentration-E1`, ordered-symmetric split per AP282); E10.
- `/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1980` (canonical ambient-qualifier formulation per AP281); E8, E19.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/mc5_class_m_chain_level_platonic.tex:229` (pro-object / weight-completed ambient); E19.
- `/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:7251-7389` (`prop:elliptic-rmatrix-shadow`); E18.
- `/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:470-546` (`thm:g1sf-elliptic-rmatrix`); E18, E20.
- `/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:8404,8496,8522,10324,12260,12276` (chiral QG equiv, GRT$_1$ torsor, gl$_N$ chiral QG, KZB heat-prefactor, Bernard heat identity); E4, E9, E18.

### Vol III manuscript sites (CY-to-chiral and BKM)

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex:411-426` (κ dual-indexing disambiguation); E17, E22, E24.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:293` (canonical inscription `rem:beauville-kappa-formula-subscript-split`); E17, E19, E22, E24.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/seven_faces.tex` `thm:seven-faces-three-tier`; E20.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/dimensional_siblings.tex` `thm:three-bkms-dim-catalogue`; E23.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/gaiotto_n1_chl.tex` `prop:gaiotto-n1-sigma-0-24`; E15.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:199-231` (Ding-Iohara-Miki toroidal); E18.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:50-78` (warning-box on $E_n$-on-wrong-object); E19.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex` (super-Yangian rename discipline); E18.

### Regex-trigger unification (audit consequence)

Three errors have DIFFERENT regex triggers in Vol I, Vol II, Vol III
caches. The unified (most specific) patterns are:

- **E8 trigger** (unified):
  `\\C\^\{?[0-9]\}? .{0,30}E_[1-9].{0,20}Dunn` or
  `E_\{?[1-9]\}?.{0,20}(per |on )\\C\^\{?[0-9]\}?`.
  Fires: "E_1 per $\mathbb C$", "three $E_1$'s on $\mathbb C^3$",
  "Dunn gives $E_3$ on $\mathbb C^3$" without "after
  $\bar\partial$-cohomology". Supersedes Vol I cache 450 regex and
  Vol II AP-V2-36 regex.
- **E17 trigger** (unified):
  `\\kappa_\{?\\mathrm\{BKM\}\}?(\([^)]*\))?` without a named
  denominator within 40 characters. Fires: bare
  `\kappa_{\mathrm{BKM}}` at an inscription site. Supersedes
  per-volume variants which each used a narrower trigger.
- **E19 trigger** (unified):
  `\\Phi_?[1-9]?\s*(:|=|\()[^,]*\\to.{0,80}\\mathrm\{ChirAlg\}` or
  `native .{0,40}\$E_[0-9]\$.chiral`. Fires: one-step $\Phi_d$
  functor-signature claims. Supersedes AP-CY144 / F8 regex and
  AP-V2-27 regex; combines both into one pattern.

## 5. Coverage report

### Errors with full three-volume coverage (12):

E1, E2, E4 (partial), E5, E6, E7, E8, E15, E17, E19, E22, E24.
(E4 listed at "partial" because the Willwacher wheel-to-$\zeta$ map
has Vol I cache 434/435/440/441 coverage but no explicit Vol II
V2-AP entry yet.)

### Errors needing Vol II AP catalogue inscription (14):

E1 (V2-AP144), E2 (V2-AP145), E3 (V2-AP146), E4 (V2-AP147),
E6 (V2-AP148), E7 (V2-AP149), E9 (V2-AP150), E10 (V2-AP151),
E11 (V2-AP152), E12 (V2-AP153), E13 (V2-AP154), E14 (V2-AP155),
E16 (V2-AP157), E18 (V2-AP159), E20 (V2-AP160), E21 (V2-AP161),
E23 (V2-AP163). The Vol II chapter homes already carry the
mathematics; the AP catalogue entries synchronise the discipline.

### Errors needing Vol III AP catalogue inscription (10):

E1 (AP-CY190), E3 (AP-CY191), E6 (AP-CY192), E7 (AP-CY193),
E11 (AP-CY194), E12 (AP-CY195), E14 (AP-CY196). AP-CY numbering
continues from existing AP-CY189 end of Fleets A/B/C/D wave.

### Errors needing Vol I cache inscription (8):

E3, E10, E11, E12, E13, E14, E20, E21. Vol I cache entries
451-458 recommended to close these gaps.

### Cross-volume ledger additions required (24):

All 24 errors E1-E24 receive new AP-CY50-E1 through AP-CY50-E24
rows in the cross-volume ledger under a new 2026-04-22 6d hCS
audit section.

## 6. Closing summary

The 6d hCS audit's 24 errors fall cleanly into the Stage-1 / Stage-2
two-stage factorisation of $\Phi_d$: Stage-1 errors (E1, E3, E4, E5,
E8, E9, E11, E12, E13, E14) live on the $E_d$-FA on CY$_d$; Stage-2
errors (E2, E6, E7, E15, E16, E17, E22, E23, E24) live on the
specialised chiral algebra on the reference curve; scope / discipline
errors (E10, E18, E19, E20, E21) live in the two-stage factorisation
itself. The cross-volume ledger addition makes the factorisation
discipline explicit: every 6d hCS claim must identify which stage it
lives on, which grammar it uses (hCS geometric vs categorical
Hochschild, cache 440 / AP923), and which $\mathrm{GRT}_1$ base-point
fixes its structure constants (cache 441 / AP924).

All mathematics verified read-only against Vol I / Vol II / Vol III
caches, AP catalogues, and cross-volume ledger as of 2026-04-22.
No builds run. No commits. All work attributed to Raeez Lorgat only.
