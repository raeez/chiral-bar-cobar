# 1. Executive verdict
Verdict class: **(2) FORMAL-LOCUS ONLY**. The current Vol III Stage-1 claim is over-scoped: the cited Kontsevich and Tamarkin theorems are affine/local statements and do not, by themselves, prove canonical `E_d`-lifts for arbitrary compact CY\(_d\) categories. The manuscript itself is internally inconsistent on this point: it simultaneously asserts Stage-1 canonicity as proved (e.g. `cy_to_chiral.tex:14,145`) and marks key Stage-1/Stage-1-to-holomorphic steps conjectural for `d\ge 3` (`cy_to_chiral.tex:159-170`). The sharp proved scope is the affine/formal-disk locus (notably `\mathbb C^d`-type models, including the `\mathbb C^3` test case modulo identification gaps below). For generic compact CY\(_3\) inputs (quintic, `K3\times E`) the Stage-1 canonicality claim is presently conjectural.

**Accessibility note.** `Costello-Francis-Gwilliam (2026)` appears accessible (arXiv:2602.12412), but I did not find in it a theorem that closes the compact-CY Stage-1 formality gap used here.

---

# 2. Attack vectors (a)-(f)

## (a) Kontsevich-Tamarkin `E_d`-formality scope
**Verdict: FALSE** (as currently asserted in Vol III Stage-1 theorem statements).

**Primary-literature citation (precise):**
- Kontsevich 1997 (`q-alg/9709040`), **Theorem 4.6.2**: existence of an `L_\infty` morphism `Tpoly(X)\to Dpoly(X)`; Section 6.4 proves the flat-space formula for `X=\mathbb R^d`, then Section 7 globalizes.
- Tamarkin 1998 (`math/9803025`), **Theorem 2.1**: operad morphism `HE_2\to B_\infty`; Section 2.2.3 applies to `A=S(V)` (and analogous formal/`C^\infty` settings), i.e. affine-type Hochschild context.

**Repository line anchors:**
- Overclaim: `chapters/theory/cy_to_chiral.tex:14,103,120,145,170`.
- Same overclaim in two-stage note: `notes/platonic_synthesis_waves_11_through_16.tex:58-60`.

The text repeatedly states Stage-1 canonicity for `\CY_d` is obtained by “Kontsevich-Tamarkin + Costello-Gwilliam-Li” without an affine/local qualifier. That is stronger than what the cited primary theorems prove. Kontsevich’s theorem is a formality theorem for polyvectors vs polydifferential operators (with local/coordinate constructions and globalization), not a theorem that Hochschild cochains of every compact CY category are `E_d`-formal in the claimed sense.

Tamarkin 1998 is likewise not a theorem that all compact CY\(_d\) categories admit canonical `E_d`-lifts. The explicit theorem in that paper is the `HE_2\to B_\infty` operadic statement (Theorem 2.1), with formality consequences for Hochschild cochains in polynomial/affine-style settings. Therefore the Stage-1 global claim is mathematically over-scoped as written.

## (b) Atiyah-class formality obstruction and compact CY\(_3\)
**Verdict: CONJECTURAL** (outside a formal locus; manuscript currently overstates).

**Primary-literature citation (precise):**
- Kapranov 1999 (Compositio 115): obstruction-to-connection statement in §1.1; **Theorem 2.3** (Atiyah-class-induced Lie structure); §1.4 formula `c_m(E)=Alt(tr(At(E)^m))`.
- Markarian 2009 (`math/0610553`): Definition 1; “Atiyah class is the only obstruction to existence of a connection” (Def. 1 discussion).
- Calaque-Căldăraru-Tu 2008 (`arXiv:0708.2725`), **Theorem 1.3**: HKR twisted by `td^{1/2}` restores Gerstenhaber compatibility.

**Repository line anchors:**
- Stage-1 claims quintic and `K3\times E` as S1 existence instances: `chapters/theory/cy_to_chiral.tex:59-61`.
- Same file explicitly acknowledges Atiyah obstruction machinery elsewhere: `chapters/theory/cy_to_chiral.tex:6426-6428,6445-6448`.
- K3xE side marked open/conjectural in treatise: `notes/CoHA_to_W_infty_treatise.tex:630-642,670-672,674-694,785-788,835-842,846-850`.

For compact CY\(_3\), `c_1=0` does **not** imply `At(T_X)=0`. This is standard from Kapranov/Markarian: scalar Chern classes are traces of Atiyah powers, but vanishing trace data is weaker than vanishing class. Direct derivation for the quintic `X_5\subset\mathbb P^4`: `c(TX_5)=(1+H)^5/(1+5H)=1+10H^2-40H^3`, hence `c_2(TX_5)=10H^2\neq0`; by Kapranov §1.4 this forces nontrivial Atiyah data.

For `K3\times E`, `T_{K3\times E}=p_1^*T_{K3}\oplus p_2^*T_E`, and `T_E` is trivial so its Atiyah class vanishes; but `c_2(T_{K3\times E})=p_1^*c_2(T_{K3})\neq0` (directly from `c_2(K3)=24`), so the total Atiyah obstruction does not vanish. Therefore Stage-1 canonicity on generic compact CY\(_3\) is not proved by a blanket “KT formality + locality” argument; at best it is presently a formal-locus statement plus conjectural extension.

## (c) “Canonical up to contractible choice” — ambient category and locus
**Verdict: UNDERSPECIFIED**.

**Primary-literature citation (precise):**
- Kontsevich 1997 (`q-alg/9709040`), **Theorem 4.6.2** + non-uniqueness discussion: quasi-isomorphisms are canonical only up to higher-homotopy/contractible-choice data.
- Costello-Gwilliam Vol I (as quoted in the FA text), **Theorem 6.2.0.2** (locally constant FA on `\mathbb R^n` ↔ `E_n`-algebras, via Lurie’s theorem), which gives the right ambient for “space of structures”.

**Repository line anchors:**
- Claim language without explicit locus in headline theorem: `chapters/theory/cy_to_chiral.tex:14,145`.
- Partial categorical ambient provided but not tied to a formal locus in claim: `chapters/theory/cy_to_chiral.tex:239-247,256-263`.
- Shadow-functor framing in memory text: `.../memory/platonic_ideal_reconstituted_2026_04_17.md:390-395`.
- Same memory file states broad one-functor claims without a compact-formality theorem citation: `.../memory/platonic_ideal_reconstituted_2026_04_17.md:258-267,601-604,632-633`.

The phrase “canonical up to contractible choice” is meaningful only after fixing the mapping space where choices live (e.g., a fiber in an `\infty`-groupoid of `E_d`-algebra structures or factorization-algebra lifts). The current statement does not explicitly identify this fiber nor the exact subcategory where contractibility is asserted.

Given the scope gap in (a), contractibility should be stated as: contractibility **on the formal/affine locus where formality input exists**, not globally on all compact CY\(_d\). Without this restriction, the canonicity claim is mathematically under-specified.

## (d) `\Phi_3` on `\CoHA(\mathbb C^3)=Y^+(\widehat{\mathfrak{gl}}_1)` test case
**Verdict: CONJECTURAL** (strong evidence, but one identification step is missing in cited primary chain).

**Primary-literature citation (precise):**
- Kontsevich-Soibelman 2008 (`arXiv:0811.2435`), Section 6; **Theorem 8** (Hall-to-quantum-torus map in §6.3), examples in §6.4, D0-D6 in §6.5.
- Schiffmann-Vasserot 2013, **Theorem 1.1** (shuffle realization used in the treatise).
- Tamarkin 1998, **Theorem 2.1** (affine-formality ingredient).

**Repository line anchors:**
- Stage-1+Stage-2 equality claim in chapter: `chapters/theory/cy_to_chiral.tex:68-70,87`.
- Two-stage synthesis claim: `notes/platonic_synthesis_waves_11_through_16.tex:50-63`.
- Treatise CoHA(C^3) setup: `notes/CoHA_to_W_infty_treatise.tex:91-103,124-130`.

This is the cleanest test vector and the one place where Stage-1 should work most directly (affine `\mathbb C^3`). The algebraic side (`\CoHA(\mathbb C^3)` to shuffle/`Y^+`) is strong. The gap is bibliographic/mathematical glue: KS 2008 §6 is primarily motivic Hall infrastructure and does not itself supply the full modern `\CoHA(\mathbb C^3)=Y^+` identification as a theorem in the exact Stage-1 form used here.

So the test case is plausible and likely true in practice, but the current Vol III citation chain does not fully prove the strict equality “Stage-1 output equals KS CoHA object” without additional explicit bridge theorems (hCS observables ↔ CoHA model ↔ same `E_3`-FA object).

## (e) `\Phi^{FA}_3` on `D^b(K3\times E)` and expected BKM/chiral output
**Verdict: CONJECTURAL**.

**Primary-literature citation (precise):**
- Kapranov 1999, **Theorem 2.3** and §1.4 (Atiyah/Chern control).
- Calaque-Căldăraru-Tu 2008, **Theorem 1.3** (HKR + Todd correction; nontrivial compact corrections).
- Kontsevich-Soibelman 2008, Section 6 (no compact `K3\times E` Stage-1 canonicity theorem of this form).

**Repository line anchors:**
- Vol III chapter claims K3xE S1 existence and BKM specialisation: `chapters/theory/cy_to_chiral.tex:60,184,205,213,460-462`.
- Same project’s treatise marks bracket-level/K3xE identifications open/conjectural: `notes/CoHA_to_W_infty_treatise.tex:630-642,663-672,674-694,760-762,785-788,835-842,846-850`.

`K3\times E` is not in a vanishing-Atiyah locus: the elliptic factor is trivial but the K3 factor contributes nontrivial `c_2`, hence nontrivial Atiyah-class data. That does not automatically forbid Stage-1 existence, but it does block the simplistic “affine-formality therefore canonical” logic.

The manuscript currently states theorem-level outcomes in some places while companion notes explicitly label the key identification steps open. The mathematically consistent status is conjectural for this vector unless and until a compact-CY\(_3\) Stage-1 theorem is supplied with full chain-level proof.

## (f) Wave-15 M5 refutation interaction (`F_3` vs `E_{10}/DE_{10}` patterns)
**Verdict: SOUND** (the likely separation is correct).

**Primary-literature citation (precise):**
- Feingold-Frenkel 1983 (rank-3 hyperbolic real-root structure; as cited in Wave-15).
- Stage-1 input side remains Kontsevich 1997 **Theorem 4.6.2** + Tamarkin 1998 **Theorem 2.1**, which are independent of post-specialisation BKM root-pattern choices.

**Repository line anchors:**
- Wave-15 refutation: `notes/wave15_m5_eta9_sl3_real_roots.tex:32-39,113-119,158-167`.
- Stage-1 definition independent of BKM root ID: `chapters/theory/cy_to_chiral.tex:116-121,145,170`.
- BKM data enters Stage-2/specialisation side: `chapters/theory/cy_to_chiral.tex:184-205,460-462`.

Wave-15 changes the **interpretation of the specialised BKM/chiral output**, not the formality/locality input used to define Stage-1. So `F_3` vs `E_{10}` does not, by itself, refute Stage-1.

The impact is downstream: any Stage-2/BKM narrative that previously relied on the wrong real-root ansatz must be corrected. Stage-1 remains agnostic to that classification error.

---

# 3. Cross-volume consistency check
Vol III itself says one Stage-1 object yields a family of Stage-2 shadows indexed by `(\Sigma_{d-1},C)` (`chapters/theory/cy_to_chiral.tex:105,201-205,210-217`). The same architecture is codified in the memory note’s shadow functor `Sh(\mathcal C,\Sigma,C)=Sp^{ch}_{\Sigma,C}(\Phi_d^{FA}(\mathcal C))` (`.../memory/platonic_ideal_reconstituted_2026_04_17.md:390-395,425-427`) and reiterated in its Vol III summary (`.../memory/platonic_ideal_reconstituted_2026_04_17.md:601-604,632-633`). Therefore any Stage-1 obstruction propagates uniformly to the full shadow family; it is not a per-route bookkeeping issue.

Vol I and Vol II stay structurally consistent with this: Vol I Theorem A is a theorem about bar-cobar for an already-given chiral/factorization algebra (`/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:5089-5101`), and Vol II identifies the SC\(^{ch,top}\)-bar differential from FM/OPE factorization data on a curve/time-slice (`/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:402,611-616,633-641`). Those theorems remain valid; what changes is the claimed universality of obtaining such inputs from Stage-1 for all compact CY\(_d\).

---

# 4. Final verdict (class + sharp scope)
**Final class: (2) FORMAL-LOCUS ONLY.**

Sharp scope actually proved from the cited chain: Stage-1 canonicity up to contractible choice is justified on affine/formal-disk loci where Kontsevich/Tamarkin formality input is available (e.g. polynomial/`\mathbb C^d` models) and then assembled by factorization-locality machinery. For generic compact CY\(_3\) categories (including quintic and `K3\times E`), the current text does not provide a primary-theorem chain establishing the same canonicality claim; in those cases Stage-1 is conjectural unless explicit compact-CY formality/obstruction control is added.

---

# 5. Recommended corrections to `cy_to_chiral.tex` (since verdict is not SOUND)
1. **Downgrade and scope Stage-1 theorem statements.**
Replace unconditional Stage-1 canonicity wording in `thm:phi-two-stage-factorisation-headline` and `thm:phi-two-stage-factorisation` (`cy_to_chiral.tex:4-15,133-146`) with an explicit formal-locus scope clause, and mark compact `d\ge 3` extension as conjectural.

2. **Split Step-(a) into “proved affine” vs “compact extension hypothesis”.**
In `prop:phi-fa-three-step-assembly` (`cy_to_chiral.tex:157-170`), separate the proven affine/local formality theorem (Kontsevich Thm 4.6.2; Tamarkin Thm 2.1 scope) from a clearly tagged **HYPOTHESIS** for compact CY categories.

3. **Define the contractible-choice space and list open compact cases explicitly.**
Add a definition giving the exact `\infty`-groupoid where “contractible choice” lives, then add a short status table (e.g. `\mathbb C^3`: proved modulo identification bridge; `K3\times E`, quintic: conjectural). Align this with existing open markers in `notes/CoHA_to_W_infty_treatise.tex:630-642,785-788,835-842` to remove internal status drift.
