# Cross-consistency audit: 6d hCS --> $E_3$ --> chiral FA --> BKM $\mathfrak g_{\Delta_5}$

Adversarial check against (i) CoHA --> $W_\infty$ treatise, (ii) Costello--Francis--
Gwilliam 2026 $E_3$ observables, (iii) platonic-ideal three-volume programme.

Evidence cited by absolute path:file:line. Seven ATTACK-HEAL cycles.

---

## Cycle 1 -- $E_3$ scope at the 6d site

**ATTACK.** `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:242,290,411` asserts "the $E_3$-factorization algebra of 6d holomorphic observables on $\C^3$"; line 290 further claims this is "via the Costello--Francis--Gwilliam algebraic formulation" and projects it to $E_2$ on $\C^2$ and $E_1$ on $C$. This collides with TOP-15 CACHED CONFUSION #3 (native/derived $E_n$): for $d \ge 3$, $A$ is natively only $E_1$; the $E_2$ structure appears on $\mathcal Z(\mathrm{Rep}(A))$, i.e. on the derived/chiral centre. The $E_3$ label applies to $\mathrm{Hoch}^\bullet$ of an $E_2$ input (higher Deligne), not to a factorisation algebra on $\C^3$ as a bare datum.

**GHOST THEOREM (false).** "Observables of 6d hCS on $\C^3$ form an $E_3$-chiral factorisation algebra, whose $E_1$-projection to a curve is $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$."

**PRECISE ERROR.** `quantum_chiral_algebras.tex:247--249` already concedes the 6d case is non-Lagrangian and routes through (c) "factorization homology of the $E_3$-algebra of local observables." The $E_3$-label here is the *operadic dimension of the ambient holomorphic stratum* (the $\mathbb{C}^3$-local disc), not an assertion that the *chiral* factorisation algebra on a curve carries an $E_3$-structure. The paragraph at line 290 presents the arrow $E_3 \to E_2 \to E_1$ as if it were a tower of *chiral* structures descending by projection; but there is no native $E_3$-chiral structure on a complex curve, only an $E_1$-chiral structure whose derived centre pair carries $\mathsf{SC}^{\mathrm{ch,top}}$ and whose iterated Drinfeld centre is $E_2$-braided. "Projection" from 6d is *specialisation along the normal bundle* (the $\mathrm{SpCh}_{N_{C/Y},C}$ functor of `e2_chiral_algebras.tex:22-44`), not a forgetful $E_3 \to E_2 \to E_1$ morphism of operads.

**CORRECT RELATIONSHIP.** The 6d site delivers an $E_3$-algebra of *local observables* in the Costello--Francis--Gwilliam sense on a disc $D^6 \subset \C^3$. Specialisation $\mathrm{SpCh}_{N_{C/\C^3},C}$ produces an $E_1$-chiral algebra on $C$; the $E_2$-*braided* structure lives on $\mathrm{Rep}^{E_1}(A)$ by the iterated Drinfeld centre, not on a $\C^2$-projection of the factorisation algebra. The `e2_chiral_algebras.tex:38-45` paragraph is correct ("At $d=3$, the stage-1 output $\PhiFA_3(\cC)$ is $E_1$...the $E_2$-chiral algebra $\Phi_{E_2}(\cC)$ is the chiral Drinfeld centre of the specialisation"); `quantum_chiral_algebras.tex:290` contradicts this by describing the $E_2$ layer as a *projection* of the 6d $E_3$ factorisation algebra. **HEAL:** rewrite line 290 to read "the $E_1$-chiral algebra on $C$ obtained by specialisation along $N_{C/\C^3}$; the $E_2$-braiding lives on $\mathrm{Rep}^{E_1}(A)$ via the Drinfeld centre (Chapter~\ref{ch:drinfeld-center}), not on a $\C^2$-projection of the 6d factorisation algebra."

---

## Cycle 2 -- CoHA vs bar complex: algebra/coalgebra conflation

**ATTACK.** `quantum_chiral_algebras.tex:240` reads "The positive half $Y^+(\widehat{\mathfrak{gl}}_1)$ is the CoHA (which is associative, not chiral:)." Good -- but `hochschild_calculus.tex:3418` then writes "The standard bar complex of the associative algebra $\CoHA(X)$. Its Euler product follows from the PBW filtration and the Hochschild--Kostant--Rosenberg theorem: $\sum_k (-1)^k \ch(B^k(A_X)) = 1/M_X(q)$." This pairs a CoHA (associative) with its *bar complex* $B(\CoHA)$ (coalgebra) and simultaneously with "HKR," which is a comparison for *smooth commutative* algebras, not for the associative non-commutative CoHA.

**GHOST THEOREM (false).** "$\sum_k (-1)^k \ch B^k(\CoHA(\C^3)) = 1/M(q)$ via HKR."

**PRECISE ERROR.** HKR compares Hochschild chains of a smooth commutative algebra to polyvector fields. The CoHA of $\C^3$ is associative but not commutative; its bar Euler characteristic is computed via PBW and the Feigin--Odesskii/Schiffmann--Vasserot shuffle presentation, which gives character $M(q)$ (MacMahon) for $Y^+$, and $M(q)^2$ for the Drinfeld double (as line 106 correctly states). The derivation at `hochschild_calculus.tex:3418` conflates two different Euler-characteristic routes, hedging with an "HKR" citation that does not apply.

**CORRECT RELATIONSHIP.** CoHA-as-associative-algebra -- bar-of-CoHA-as-$E_1$-coalgebra -- HKR-comparison (requires smoothness + commutativity, i.e. applies to $\HH^\bullet(D^b\mathrm{Coh}(X)) \simeq \bigoplus H^{\bullet-q}(X, \wedge^q T_X)$, *not* to $B(\CoHA)$). The correct statement is that $B(\CoHA(\C^3))$ carries the deconcatenation coproduct and its graded character equals $1/M(q)$ by the PBW filtration on the shuffle presentation -- HKR enters only for the *Hochschild* side of the categorical $\Phi_3$-input, not the chiral side. **HEAL:** at `hochschild_calculus.tex:3418` replace "HKR theorem" with "the PBW-shuffle presentation of Schiffmann--Vasserot~2013." Reserve HKR for the categorical $\HH^\bullet(D^b\mathrm{Coh}(X))$ computation.

---

## Cycle 3 -- $W_\infty$ vs $W_{1+\infty}$ vs $\mathcal W_\infty[\lambda]$

**ATTACK.** Three distinct vertex algebras appear interchangeably: (a) $W_\infty$ (the "classical" 1-parameter $c$-family, e.g. Bakas--Kiritsis), (b) $W_{1+\infty}$ (contains spin-1, Kac--Radul), (c) $\mathcal W_\infty[\lambda]$ (the 2-parameter universal algebra of Prochazka--Rapcak, containing the triality $\lambda \leftrightarrow \mu \leftrightarrow \nu$).
- `quantum_chiral_algebras.tex:92,104,284` asserts $Y(\widehat{\mathfrak{gl}}_1) \simeq W_{1+\infty}$ at $c=1$ via Prochazka--Rapcak. But Prochazka--Rapcak prove $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal W_\infty[\lambda]$ (2-parameter, Gaiotto--Rapcak triality) with a specific specialisation relating $\lambda$ to the Yangian structure function parameters.
- `quantum_chiral_algebras.tex:1178,2087,2114,2177,2187,3673,3677` then uses $W_{1+\infty}$ and $\mathcal W_{1+\infty}$ interchangeably, including "total $\kappa_{\mathrm{ch}}(W_{1+\infty})$ at $c=1$ diverges ($\sum 1/j$ harmonic series)."
- `chapters/examples/w_algebras_deep.tex:90,94` and `chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:386-401` use $\mathcal W_\infty$ (no "1+") as the "large-$N$ limit $\varprojlim_N \mathcal W_N$." This is the *2-parameter* universal algebra *before* truncation, not $W_{1+\infty}$.

**GHOST THEOREM (false).** "$W_\infty = W_{1+\infty} = \mathcal W_\infty[\lambda]$ -- all the same object."

**PRECISE ERROR.** $W_{1+\infty} = W_\infty \oplus \mathcal H$ (Heisenberg $U(1)$-current), so $W_{1+\infty}$ contains an extra spin-1 field; $\mathcal W_\infty[\lambda]$ is a 2-parameter universal algebra whose specialisations include *both* $W_\infty(c)$ (at the $\lambda \to N$ truncation of $\mathcal W_N$) and $W_{1+\infty}(c)$ (at a different specialisation). Identifying all three flattens the triality $\lambda \leftrightarrow \mu \leftrightarrow \nu$ that is the *content* of Gaiotto--Rapcak and therefore of the 6d-->defect story.

**CORRECT RELATIONSHIP.** Prochazka--Rapcak arXiv:1711.09993: $Y(\widehat{\mathfrak{gl}}_1)_{h_1,h_2,h_3} \simeq \mathcal W_\infty[\lambda]$ where $(h_1:h_2:h_3) \leftrightarrow (\lambda:\mu:\nu)$. Specialisation $h_3 \to 0$ (or fixing the Heisenberg direction) gives $W_{1+\infty}$; the *coset* $W_{1+\infty}/\mathcal H$ gives $W_\infty$. **HEAL:** at `quantum_chiral_algebras.tex:284` state the full Prochazka--Rapcak isomorphism as $Y \simeq \mathcal W_\infty[\lambda]$ with the triality; reserve "$W_{1+\infty}$ at $c=1$" for the *specific* specialisation used in the defect computation (`quantum_chiral_algebras.tex:485-517`). Audit each `\cW_\infty` vs `W_{1+\infty}` instance.

---

## Cycle 4 -- Chain-level vs $(\infty,1)$-categorical lane

**ATTACK.** `quantum_chiral_algebras.tex:1044` declares "the higher Deligne conjecture (now a theorem: Lurie, 2012; Costello, 2007) states that for an $E_n$ algebra $A$, the Hochschild cochains $\HH^\bullet(A,A)$ carry an $E_{n+1}$ structure. For $E_\infty$ input: $E_\infty$ on $\HH^\bullet$ (since $\infty + 1 = \infty$)." It then couples this to the chain-level assertion in `chiral-bar-cobar/chapters/theory/e3_identification_chain_level_platonic.tex:413` (thm:e3-identification-chain-level-associator-fixed), which constructs a chain-level $E_3$ quasi-iso rigidified by $\Phi_{\mathrm{KZ}}$. `mc5_class_m_chain_level_platonic.tex:229` further insists on the chain-level (pro-object/weight-completed ambient) statement vs the $(\infty,1)$-statement.

**GHOST THEOREM (false).** "The chain-level $E_3$-identification and the $(\infty,1)$-categorical higher Deligne theorem are the same theorem."

**PRECISE ERROR.** CLAUDE.md explicitly flags Pattern 269: these are *two different theorems about two different mathematical objects*. The chain-level $E_3$ identification depends on a choice of Drinfeld associator $\Phi_{\mathrm{KZ}}$ ("The chain-level identification rigidified by a different associator..." at `e3_identification_chain_level_platonic.tex:457`); different associators yield $E_2$-quasi-isomorphic but not $E_2$-equal structures (Tamarkin, GRT-torsor, `e2_chiral_algebras.tex:134`). The $(\infty,1)$-level statement abstracts over the GRT-torsor. Conflating the two in `quantum_chiral_algebras.tex:1044` loses the GRT-torsor content and misstates the higher Deligne conjecture as asserting an on-the-nose $E_{n+1}$ structure.

**CORRECT RELATIONSHIP.** At $(\infty,1)$-level: Lurie HA 5.3.1, $\HH^\bullet(A,A)$ carries a canonical $E_{n+1}$-algebra structure as the universal $E_n$-centraliser. At chain level: a *choice* of $E_{n+1}$-operadic resolution is required, parametrised by the GRT-torsor; different associators give different chain-level $E_{n+1}$-structures, all $(\infty,1)$-equivalent. For $E_\infty$ input the situation is $E_\infty$ at $(\infty,1)$-level (correct at line 1044) *but* chain-level is obstructed exactly because $E_\infty$ is not cofibrantly resolved on the nose -- a technical footnote missing from the sweeping "since $\infty+1=\infty$" hedge. **HEAL:** at `quantum_chiral_algebras.tex:1044` add an ambient-qualifier: "at the $(\infty,1)$-categorical level, $\HH^\bullet$ carries $E_{n+1}$; chain-level identification depends on an associator choice (GRT-torsor), see Chapter~\ref{chap:e3-identification-chain-level-platonic} of Vol~I."

---

## Cycle 5 -- 6d hCS vs chiral CS vs chiral factorisation algebra naming

**ATTACK.** Three names for related-but-not-identical objects:
- "6d hCS" (`quantum_chiral_algebras.tex:230-244`, `w_infty_e_infty_endpoint_platonic.tex:581-620`),
- "6d holomorphic theory on $\C^3$ (non-Lagrangian)" (`quantum_chiral_algebras.tex:247-249`),
- "Costello--Francis--Gwilliam factorisation algebra" (`topologization_chain_level_platonic.tex:151`, `spectral-braiding-core.tex:594-600`).

`quantum_chiral_algebras.tex:247-249` explicitly concedes "The 6d regime (iii) is not literally the holomorphic Chern--Simons action $S_{\mathrm{hCS}}$ on $\C^3$"; the "correct 6d formulation" routes through M5-brane $(2,0)$ or CFG factorisation homology. But *elsewhere* (line 243, 290, 411, 432, 447, 523, 572) the paper calls the object "6d holomorphic Chern--Simons" or "6d hCS," and `quantum_chiral_algebras.tex:444` is a proposition literally named "Defect algebra of 6d hCS on $\C^3$." The remark at line 247 *retracts* the Lagrangian interpretation; the theorem statements 100 lines later use "6d hCS" as if the action existed.

**GHOST THEOREM (false).** "6d hCS on $\C^3$ with Lagrangian $\int \Omega \wedge A\wedge \bar\partial A + \tfrac23 A^3$ produces $W_{1+\infty}$ on a codimension-2 defect."

**PRECISE ERROR.** For $\dim_\C M = 3$, $\Omega \wedge A \wedge \bar\partial A$ is a $(3,2)$-form, not top on a 6-real-manifold. The remark at line 247-249 notes this. The theorem statement `quantum_chiral_algebras.tex:447` nonetheless begins "The 6d holomorphic Chern--Simons action with gauge algebra $\mathfrak{gl}_1$... restricted to a tubular neighborhood $U = \C_{z_1} \times D^2_{z_2,z_3}$ of $C$, produces on $C$ the vertex algebra $W_{1+\infty}$..."

**CORRECT RELATIONSHIP.** The object is the CFG $E_3$-algebra of local observables on $\C^3$, with Omega-background parameters $(h_1,h_2,h_3)$ satisfying $h_1+h_2+h_3 = 0$, specialised along a codim-2 embedding $C \hookrightarrow \C^3$. It is *not* the Lagrangian $S_{\mathrm{hCS}}$ at $\dim_\C = 3$; the perturbative BV formulation is the M-theory Omega-background framework of Costello 2017 + CFG 2024/2026 factorisation homology. **HEAL:** rename Proposition `quantum_chiral_algebras.tex:444` to "Defect algebra of the 6d holomorphic CFG factorisation algebra on $\C^3$" and remove "hCS action with gauge algebra..." wording. Reserve "hCS" for the Lagrangian 3d and 5d cases (where it literally applies).

---

## Cycle 6 -- Drinfeld centre vs averaging

**ATTACK.** CLAUDE.md TOP-15 #7: do not conflate Drinfeld centre with averaging map $\mathrm{av}$. Two usages:
- `drinfeld_center.tex:4` correctly says "At $d=3$ the Drinfeld centre $\mathcal Z(\mathrm{Rep}(\Phi_3(\mathcal A)))$ is the right adjoint, not averaging." Good.
- `chiral_hochschild_koszul.tex:1590-1652` uses the averaging map $\mathrm{av}: \mathfrak g^{E_1} \to \mathfrak g^{\mathrm{mod}}$ from ordered to symmetric chiral convolution dGLA, and claims "$\mathrm{av}$ descends to a [something]" at line 1593, and "$\mathrm{av}$ is already acyclic" at line 1617.
- But `quantum_chiral_algebras.tex:81-106` says "The passage from $E_1$ to $E_2$ is realized by the Drinfeld center construction. For the CoHA of $\C^3$, this yields the full affine Yangian." This is the *Drinfeld double*, not the Drinfeld centre of the rep category.

**GHOST THEOREM (false).** "The passage from $E_1$ to $E_2$ is Drinfeld centre $=$ Drinfeld double $=$ averaging map."

**PRECISE ERROR.** Three different constructions:
(a) *Drinfeld centre* $\mathcal Z(\mathcal C)$: categorical; $\mathcal Z(\mathrm{Rep}(A))$ is the $E_2$-braided category whose objects are $A$-modules with half-braiding.
(b) *Drinfeld double* $D(Y^+) = Y^+ \otimes Y^-$ with a quasi-triangular pairing: algebraic; recovers the full Yangian from the positive half.
(c) *Averaging map* $\mathrm{av}: \mathfrak g^{E_1} \to \mathfrak g^{\mathrm{mod}}$: from ordered to symmetric chiral convolution, a surjection of dGLAs. Nothing to do with $E_1 \to E_2$ ascent; $\mathrm{av}$ is a descent within the same $E_1$-layer (ordered to symmetric).

**CORRECT RELATIONSHIP.** $E_1$ to $E_2$ is the Drinfeld *centre* of the rep category (categorical); Drinfeld *double* is an algebraic device producing an $E_1$-quasi-triangular Hopf algebra from a bialgebra; *averaging* relates ordered to symmetric chiral homology within a fixed operadic level. The text at `quantum_chiral_algebras.tex:81` "The passage from $E_1$ to $E_2$ is realized by the Drinfeld center construction. For the CoHA of $\C^3$, this yields the full affine Yangian" combines (a) (correct for Drinfeld centre of rep category) and (b) (Drinfeld double yields full Yangian from $Y^+$) into a single sentence that misattributes the full-Yangian construction to the Drinfeld centre. **HEAL:** split into two sentences: "The $E_2$-braided structure on $\mathrm{Rep}^{E_1}(Y^+)$ is the Drinfeld centre. The full Yangian is recovered from $Y^+$ by the Drinfeld *double* construction (a distinct operation: see `drinfeld_center.tex:95-140`)."

---

## Cycle 7 -- BKM $\mathfrak g_{\Delta_5}$ status and K3 $\times E$ $\kappa_{\mathrm{BKM}}=5$

**ATTACK.** `quantum_chiral_algebras.tex:408-418` (Conjecture 6d-k3xe) states "kappa-spectrum: $\kappa_{\mathrm{ch}}(A_X) = 3$, $\kappa_{\mathrm{BKM}}(X) = 5$, $\kappa_{\mathrm{cat}}(X) = 2$, $\kappa_{\mathrm{fiber}}(X) = 24$." And `derived_categories_cy.tex:747` derives $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E) = 3$ by additivity. But CLAUDE.md (cached confusion #11) flags $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})$ as a numerical *coincidence*, not an identity.

**GHOST THEOREM (oblique).** "$\kappa_{\mathrm{BKM}}(K3\times E) = \kappa_{\mathrm{ch}}(A_{K3\times E}) + \chi(\mathcal O_E)$ by Kunneth."

**PRECISE ERROR.** The equation $5 = 3 + 2$ is numerically true *if and only if* (a) $\kappa_{\mathrm{BKM}}$ is defined as the Borcherds-weight of $\mathfrak g_{\Delta_5}$ at the $\Delta_5$-locus, (b) $\kappa_{\mathrm{ch}}(A_{K3\times E}) = 3$ is additive in Kunneth (`derived_categories_cy.tex:747`, Beauville-kappa-formula subscript split), and (c) $\chi(\mathcal O_E) = 2$ *holds -- but $\chi(\mathcal O_E) = 0$, not 2*. An elliptic curve has $\chi(\mathcal O_E) = 1 - 1 = 0$. The "+2" is $\chi(\mathrm{top})$ not $\chi(\mathcal O)$, or it is $\dim H^0 + \dim H^1 = 2$, but this is *not* $\chi(\mathcal O_{\mathrm{fiber}})$.

**CORRECT RELATIONSHIP.** Read `derived_categories_cy.tex:747`: "$\chi(K3 \times E) = 2(h^{1,1} - h^{2,1}) = 0$, so the conjectural $d=3$ kappa-sum $\kappa_{\mathrm{ch}}(X) + \kappa_{\mathrm{ch}}(X^\vee) = 0$ is trivially satisfied. The Heisenberg-level chiral modular characteristic $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3$ by additivity ... and ... the Koszul sum $3 + 3 = 6 \neq 0$. This places $K3 \times E$ *outside* the free-field Koszul class at $d=3$, consistently with the nonzero Koszul conductor $K = \kappa_{\mathrm{BKM}} = 5$." This derivation is internally consistent at `derived_categories_cy.tex:747` (identifies $\kappa_{\mathrm{BKM}} = 5$ with the Koszul conductor), but the CLAUDE.md cache warning is that writing $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{fiber}})$ in a symbolic identity would be a false pattern -- there is no such universal formula, the coincidence is specific to the $K3 \times E$ Borcherds anchor. **HEAL:** at `quantum_chiral_algebras.tex:416` change "kappa-spectrum: $\kappa_{\mathrm{ch}}(A_X) = 3$, $\kappa_{\mathrm{BKM}}(X) = 5$, ..." to state explicitly "$\kappa_{\mathrm{BKM}} = 5$ is the Borcherds-weight of $\Delta_5$ (Gritsenko--Nikulin), not a multiplicative combination of $\kappa_{\mathrm{ch}}$ and $\chi(\mathcal O_E) = 0$; see `derived_categories_cy.tex:917-1051` for the primary attribution."

---

## Summary of ghost theorems flagged

| # | Ghost | File:line | Severity | Fix |
|---|-------|-----------|----------|-----|
| 1 | Projection $E_3 \to E_2 \to E_1$ chiral | `qca.tex:290` | HIGH | Replace "projection" with "specialisation"; $E_2$-braiding via Drinfeld centre |
| 2 | HKR on $B(\CoHA)$ | `hochschild_calculus.tex:3418` | MEDIUM | Replace HKR with PBW-shuffle |
| 3 | $W_\infty = W_{1+\infty} = \mathcal W_\infty[\lambda]$ | `qca.tex:92,284`+ | HIGH | State full Prochazka triality; reserve each name |
| 4 | Chain-level $E_3$ = $(\infty,1)$ higher Deligne | `qca.tex:1044` | MEDIUM | Add ambient qualifier; cite GRT-torsor |
| 5 | "6d hCS" Lagrangian | `qca.tex:444-523` | HIGH | Rename to "CFG factorisation algebra" |
| 6 | Drinfeld centre = double = averaging | `qca.tex:81` | HIGH | Split into three distinct constructions |
| 7 | $\kappa_{\mathrm{BKM}} = 5$ via $\chi(\mathcal O_E)$ | `qca.tex:416` | LOW (cached) | State Borcherds-anchor only |

## Cross-volume propagation checks (AP5)

- Vol~I `chiral_hochschild_koszul.tex:1590-1652` averaging-map scope is clean (ordered-to-symmetric, same operadic level). No $E_1 \to E_2$ drift.
- Vol~I `e3_identification_chain_level_platonic.tex` chain-level $E_3$-identification is chain-level-only, GRT-rigidified. Correct lane.
- Vol~II `w_infty_e_infty_endpoint_platonic.tex:43-216` uses $\mathcal W_\infty[\lambda]$ with the full triality. Correct.
- Vol~II `e2_chiral_algebras.tex:22-44` and Vol~III `drinfeld_center.tex:4,95-140` both correctly distinguish Drinfeld centre from averaging. Correct.
- Vol~III `quantum_chiral_algebras.tex` is the primary offender across cycles 1, 3, 4, 5, 6, 7.

## Verdict

The 6d hCS --> $E_3$ --> chiral FA --> BKM $\mathfrak g_{\Delta_5}$ story **survives adversarial attack at the $(\infty,1)$-categorical level** (CFG $E_3$-algebra of local observables on $\C^3$, specialisation to $E_1$-chiral on a curve, Drinfeld-centre $E_2$-braiding, Borcherds-anchor $\kappa_{\mathrm{BKM}}$) **but carries seven oblique framings in `quantum_chiral_algebras.tex` that collapse the distinction between**:
(a) native vs derived $E_n$ structures,
(b) CoHA vs its bar (algebra vs coalgebra),
(c) $W_\infty$ vs $W_{1+\infty}$ vs $\mathcal W_\infty[\lambda]$,
(d) chain-level vs $(\infty,1)$-level,
(e) Lagrangian "6d hCS" vs non-Lagrangian CFG factorisation,
(f) Drinfeld centre vs Drinfeld double vs averaging,
(g) symbolic $\kappa_{\mathrm{BKM}}$ identity vs numerical coincidence.

Each fix is local (rename, split sentence, add qualifier); the mathematics is intact. The platonic-ideal three-volume architecture (Vol~I $E_1$-chiral + bar-cobar; Vol~II $\mathsf{SC}^{\mathrm{ch,top}}$ + topologisation; Vol~III $\Phi_d$ + CY-to-chiral) absorbs the healed statements without structural shift.
