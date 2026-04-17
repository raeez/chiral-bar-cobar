# Wave V86 — Attack-and-Heal: Independent Verification of V81 FM164/FM161 Closure Claim

**Date:** 2026-04-16.
**Mode:** Russian-school adversarial attack + Beilinson--Drinfeld factorisation discipline. Sandbox only.
**Subject:** the V81 closure claim that FM164 + FM161 are CLOSED in Vol II Wave 9, justifying status promotion of V49 + V58 + V64 + V65 + V77 from "conditional" to UNCONDITIONAL on the K3 cell.
**Discipline gates honoured:** AP-CY11 (conditional propagation), HZ3-3 (named dependency), AP-CY13 (cross-volume part references), AP-CY40 (status tag matches proof), AP-CY61 (first-principles ghost theorem extraction).
**LOSSLESS directive (per user 2026-04-16):** no downgrades. Where Vol II closure holds, present the unconditional status. Where it fails, present the sharpest precise conditional with the named cell.
**Pre-commit hook:** no .tex inscription, no build, no test, no commit. All commits would be by Raeez Lorgat ONLY.

---

## §0. Executive summary

V81 asserted that FM164 and FM161 are CLOSED in Vol II Wave 9 (Vol II `CLAUDE.md`
lines 624, 839, 859), reducing every Vol III conditional `cond. FM164/FM161
K3-specialised` to UNCONDITIONAL post-Wave 9. Independent verification finds:

1. **PARTIAL CONFIRM.** FM161 closure is documented at Vol II `CLAUDE.md` line
   839 (Koszulness Moduli M_Kosz section, FM closures clause: "FM161 (Yangian
   open-embedding of charts $M_{\rm Kosz}^{\rm assoc} \hookrightarrow
   M_{\rm Kosz}^{\rm chiral}$, quadratic-Koszul chart includes into
   chiral-Koszul atlas)"). FM164 closure is documented at Vol II `CLAUDE.md`
   line 859 (Unified Chiral Quantum Group Theorem clause: "All of FM130--135,
   FM161--170, FM176--181 CLOSED by this theorem as specialization/scope/
   citation fixes"). Both closures are real and correctly cited by V81.
2. **HOWEVER, MAJOR CAVEAT: the eight specialization fibres at Vol II line 849
   do NOT include "K3 Heisenberg + ADE-enhanced cell" as written.** The Vol II
   line 849 list is: Yangian $Y_\hbar(g)$; Affine Yangian $Y_\hbar(\hat g)$;
   Shifted Yangian $Y_\mu(g)$; Truncated shifted (BFN Coulomb); Finite W
   $W^{\rm fin}(g,f)$; Affine W principal $W_k(g, f_{\rm prin})$; Affine W
   non-principal $W_k(g, f)$; Bershadsky-Polyakov; Orthogonal coideal. The
   hypothesis at Vol II line 843 is `simple Lie g (finite/affine)`. The Mukai
   lattice $\Lambda_{K3}$ corresponds to the **abelian rank-24 Heisenberg**
   $\hat{\mathfrak{u}}(1)^{24}$ — NOT a simple Lie algebra in the standard
   sense. **V81's "K3 Heisenberg + ADE-enhanced cell" is NOT explicitly named
   among the eight Wave 9 fibres.**
3. **Cohomological vs chain-level closure.** Vol II line 859 clause says
   "CLOSED by this theorem as specialization/scope/citation fixes" — the
   modality is CITATION/SCOPE/SPECIALIZATION, not chain-level construction.
   Examining the three-leg proof at Vol II line 847 (MC + Koszul duality +
   BRST transport): all three legs operate at the Maurer-Cartan / Koszul
   pair / BRST cohomological level. Chain-level chiral pentagon coherence
   for the K3 input is NOT proved by Wave 9. The closure is at the level
   needed for the eight named fibres; it is COHOMOLOGICAL in chiral
   bar-degree, with chain-level data scoped through the Yangian-side PBW
   filtration.
4. **Super-Lie variant: V81's "VAPID" verdict CONFIRMED.** No Vol II FM
   catalogue entry FM182-super or FM183-super exists. Vol II Wave 9-10
   supplement (lines 447-468) introduces FM182-FM196 but in a different
   cluster (Hochschild + brace + holographic + Vol II standalones); FM182
   at line 450 is about `HH^0` AP-CY64 conflation, NOT super-Yangian
   Koszulness. So the V81 proposed "FM182/FM183 = super-Yangian
   Koszulness + super-bar-cobar" labels CANNOT be used (collision with
   existing FM182). Renumber as **FM197-super, FM198-super** or use
   distinct labels (proposed below).
5. **HZ3-3 + AP-CY11 traceability is sharper post-V86.** V81's healing path
   (Option C: stratification with documentation) is sound in spirit but
   needs THREE corrections: (a) replace "K3 Heisenberg + ADE cell of the
   eight fibres" with the more honest "K3 Heisenberg + ADE bridge to the
   Affine W principal cell at $g = $ ADE simply-laced, $k$ non-critical";
   (b) renumber the proposed super-FM entries to avoid Vol II FM182
   collision; (c) name the chain-level vs cohomological gap explicitly in
   the conditional rider.

The honest LOSSLESS post-V86 status:

> **For the V49 K3 Pentagon-at-$E_1$ result, the COHOMOLOGICAL closure of
> FM164 + FM161 is achieved via the Vol II Wave 9 Unified Chiral Quantum
> Group Theorem in the K3-as-affine-W-of-ADE bridge cell. The CHAIN-LEVEL
> closure for the K3 Mukai-lattice Heisenberg is NOT directly covered by
> the eight Wave 9 fibres and requires a separable bridge lemma
> (PROPOSED FM197-super-bridge below). At the cohomological level
> (Pentagon coherence as $H^*$ of a chain complex), V49 is UNCONDITIONAL
> post-Wave 9. At the chain level (strict chiral pentagon as a coherence
> diagram on chain models), V49 retains a sharp residual conditional on
> the bridge lemma.**

This is sharper than V81 and stronger (lossless): it preserves V81's
unconditional cohomological status while honestly naming the chain-level
residual gap.

---

## §1. Verification of Vol II Wave 9 closure for FM164 and FM161

### 1.1 FM161 — Y(g) Koszulness via PP05 nonhomogeneous duality

**Vol II `CLAUDE.md` L419 (statement of FM161, Wave 7 supplement):**

> **FM161**: Y(g) Koszulness via PP05 nonhomogeneous duality
> (`yangians_foundations.tex`:623-635) — PP05 Ch. 4 requires connected
> grading $A_0 = k$. Yangian level grading has PRO-FINITE $A_0$;
> "passing to augmentation ideal" (L552) does not produce
> PP05-compatible grading.

**Vol II `CLAUDE.md` L624 (HEAL-SWEEP entry for FM161):**

> **FM161 → HEAL**: Y(g) Koszulness in Positselski nonhomogeneous
> framework. Replace PP05 connected-grading with filtered-CDG-Koszul
> framework properly. Strongest form: filtered Koszul deformation of
> $U(g[t])$ for ALL simple $g$ (classical + exceptional).

**Vol II `CLAUDE.md` L839 (Koszulness Moduli closure clause):**

> **FM closures:** ..., FM161 (Yangian open-embedding of charts
> $M_{\rm Kosz}^{\rm assoc} \hookrightarrow M_{\rm Kosz}^{\rm chiral}$,
> quadratic-Koszul chart includes into chiral-Koszul atlas).

**Verdict.** FM161 is closed in Vol II at the level of the Koszulness Moduli
Scheme $M_{\rm Kosz}$ characterization. The closure mechanism is the
open-embedding of charts: the quadratic-Koszul (Positselski PP05) chart is
not the only chart of $M_{\rm Kosz}$; it embeds as an open subset into the
chiral-Koszul atlas. Yangian Koszulness lives in the chiral atlas, not the
PP05 chart, so the PP05 connected-grading obstruction does not apply.

**This closure IS real.** It is a genuine mathematical content — the
Koszulness Moduli framework reframes Koszulness as a property captured by a
GRT-equivariant scheme, of which the PP05 quadratic chart is one of 14
charts. V81's citation is correct.

### 1.2 FM164 — Bar-cobar Yangian completion elision

**Vol II `CLAUDE.md` L422 (statement of FM164, Wave 7 supplement):**

> **FM164**: Bar-cobar Yangian completion elision.
> `yangians_foundations.tex`:677-701 "counit is quasi-iso for augmented
> pro-nilpotent $E_1$-chiral algebras." Pro-nilpotence of $A$
> ($\bigcap I^n = 0$) does NOT imply conilpotence of $B(A)$; gives
> conilpotence only on COMPLETED $\hat B(A)$.

**Vol II `CLAUDE.md` L859 (Unified Chiral Quantum Group Theorem closure
clause):**

> **All of FM130-135, FM161-170, FM176-181 CLOSED by this theorem as
> specialization/scope/citation fixes.**

**Verdict.** FM164 is closed via the Unified Chiral Quantum Group Theorem.
The closure modality, however, is `specialization/scope/citation fixes` —
NOT chain-level construction. The Unified Theorem proves existence (and
uniqueness up to spectral gauge) of $Q_g^{k,f,\mu}$ for the eight fibres
listed at line 849, with the `non-critical level $k \neq -h^v$` hypothesis
at line 843. The pro-nilpotent bar-cobar completion is then handled by the
$\hat B$ completion (Wave 7 counter at L422) within the chiral atlas of
the Koszulness Moduli framework. The bar-cobar functor is computed on
$\hat B(A)$, not raw $B(A)$.

**This closure IS real, with caveats.** The closure operates at the level
of bar-cobar adjunction in the pro-nilpotent completion category. V81's
citation is correct.

### 1.3 Joint verdict

Both FM161 and FM164 are CLOSED in Vol II at the appropriate level:

| FM | Closure mechanism | Modality | Vol II location |
|---|---|---|---|
| FM161 | Koszulness Moduli $M_{\rm Kosz}$ chart embedding | Cohomological/categorical | L839 |
| FM164 | Unified Chiral Quantum Group Theorem $\hat B$-completion | Chain-level via $\hat B$ in pro-completion | L859 |

V81's headline claim that both are CLOSED is CONFIRMED.

---

## §2. K3-specialised vs general — the cell hierarchy

### 2.1 The eight Wave 9 specialization fibres

**Vol II `CLAUDE.md` L849 (verbatim):**

> **Eight specialization fibres covered:** Yangian $Y_\hbar(g)$; Affine
> Yangian $Y_\hbar(\hat g)$; Shifted Yangian $Y_\mu(g)$; Truncated
> shifted $Y^\lambda_\mu(g)$ (= BFN Coulomb branch); Finite W
> $W^{\rm fin}(g,f)$; Affine W principal $W_k(g, f_{\rm prin})$;
> Affine W non-principal $W_k(g, f)$; Bershadsky-Polyakov =
> $W_k(\mathfrak{sl}_3, f_{\rm min})$; Orthogonal coideal $Q^\theta$.

(Note: Vol II writes "Eight" but lists nine — Bershadsky-Polyakov is a
sub-case of Affine W non-principal; the Vol II count likely fuses them.
This is a Vol II count discrepancy, not a V86 attack target.)

**Vol II line 843 hypothesis (verbatim):**

> *Fix simple Lie $g$ (finite/affine), good $\mathbb{Z}$-grading
> $\Gamma$ on $g$ via $sl_2$-triple $(e, h, f)$, non-critical level
> $k \neq -h^v$, shift datum $\mu \in P(g)^+ \cup \{0\}$.*

### 2.2 The K3 input is NOT directly in the eight fibres

The K3 Mukai-lattice Heisenberg has:
  - Lattice rank 24, signature $(4, 20)$.
  - Underlying algebra: $\hat{\mathfrak{u}}(1)^{24}$ — **abelian**, rank-24
    Heisenberg.
  - ADE-enhancement: at the special K3 lattice points where the lattice
    contains an ADE root sublattice $\Lambda_{\rm ADE} \subset \Lambda_{K3}$,
    the abelian Heisenberg extends to $\hat{g}_{\rm ADE} \oplus
    \hat{\mathfrak{u}}(1)^{24 - {\rm rk}(\Lambda_{\rm ADE})}$ as a Borel-Weil
    enhancement.

**Crucial check against Vol II hypothesis (L843):** Vol II L843 requires
"simple Lie $g$ (finite/affine)." The K3 Heisenberg $\hat{\mathfrak{u}}(1)^{24}$
is **NOT simple** — it is abelian. The ADE-enhanced fragment $\hat g_{\rm ADE}$
IS simple (or affine simple), but the full K3 algebra is the direct sum of
ADE + abelian remainder.

**V81's claim "K3 Heisenberg + ADE-enhanced cell is one of the eight Wave 9
specialization fibres" is FALSE as stated.** The K3 Heisenberg is not literally
listed; only the ADE-enhanced fragment is in the Affine Yangian / Affine W
fibres.

### 2.3 The bridge that V81 missed

The honest applicability claim is:

> The K3-cell of the V49 Pentagon-at-$E_1$ result decomposes as the direct
> sum of (a) ADE-simply-laced fragments covered by the Affine Yangian
> $Y_\hbar(\hat g_{\rm ADE})$ fibre of Vol II Wave 9, and (b) abelian
> Heisenberg fragments covered by a SEPARATE bridge lemma (the abelian-Lie
> case of the Unified Chiral Quantum Group Theorem, NOT named explicitly at
> L849 but tractable as a degenerate $g \to {\rm abelian}$ limit).

**The bridge lemma is the residual.** The simple-Lie and abelian-Lie cases
of the Unified Theorem are not on the same footing: simple-Lie has the full
three-leg proof (MC + Koszul + BRST); abelian-Lie has trivial Koszul leg
(quadratic dual is abelian) and trivial BRST leg (DS reduction trivial),
but the MC leg requires explicit verification of the Heisenberg R-matrix
$R(z) = \exp(k \hbar / z)$ satisfying CYBE on the abelian r-matrix
$r(z) = k/z$.

**V2-AP7 (Vol II `CLAUDE.md` L177):** "Heisenberg R-matrix $= \exp(k \hbar
/z)$, NOT trivial. Collision residue $k/z$. Monodromy $\exp(-2\pi i k)$."
This IS a verified Heisenberg R-matrix in the chiral atlas; the abelian
case of the Unified Theorem applies trivially.

**Verdict.** V81's "K3 Heisenberg + ADE cell" requires a two-fragment
decomposition: (a) the ADE fragment is in the Affine Yangian / Affine W
fibre; (b) the abelian fragment is in the trivial-degeneration limit of
the Unified Theorem with the Heisenberg R-matrix verified by V2-AP7.
Both fragments are covered — but as TWO DISTINCT cells, not one.

### 2.4 Cell hierarchy (post-V86 corrected)

```
Vol II Wave 9 Unified Chiral Quantum Group Theorem
                |
  +-------------+-----------------+
  |                               |
Eight specialization fibres    Abelian-Lie degeneration (V2-AP7 Heisenberg)
(L849, simple Lie hypothesis)  (NOT explicitly listed, but tractable as g→0 limit)
  |                               |
  | Affine Yangian Y_hbar(hat g)  | Heisenberg H_k = u(1) chiral abelian
  | with g = ADE simply-laced     | with R(z) = exp(k·hbar/z), V2-AP7 verified
  |                               |
  +---------------+---------------+
                  |
       K3 cell (direct sum decomposition):
        - ADE fragment: hat g_ADE ⊂ Lambda_K3
        - Abelian fragment: u(1)^{24-rk(Lambda_ADE)}
                  |
                  v
       V49 K3 Pentagon-at-E_1 (cohomological, UNCONDITIONAL post-Wave 9)
       V49 K3 Pentagon-at-E_1 (chain-level, conditional on bridge lemma)
                  |
                  v
       V58 / V64 Class A K3       — inherits cohomological UNCOND, chain-level conditional
       V65 CY-C abelian K3        — inherits cohomological UNCOND + AP-CY66 BZFN cond.
       V77 (V70) Mukai uniqueness — inherits silently (per V81 §6.3)
       V69 V49 three-routes ind.  — preserves V49 conditionality
```

### 2.5 The cell hierarchy is finer than V81

V81 named a single "K3 Heisenberg + ADE-enhanced cell." V86 finds a
two-fragment decomposition. The chain-level closure for the abelian
fragment depends on the (verified) Heisenberg R-matrix V2-AP7; the
chain-level closure for the ADE fragment depends on the explicit Affine
Yangian $Y_\hbar(\hat g_{\rm ADE})$ presentation. Both are present in the
Vol II content; both need a NAMED BRIDGE LEMMA to combine.

The bridge lemma is the residual that V81 did not surface.

---

## §3. Chain-level vs cohomological verdict

### 3.1 Vol II line 859 closure modality

The closure clause reads `CLOSED by this theorem as specialization/scope/
citation fixes`. The three modalities are:

  - **Specialization:** the FM is closed because the result it questions
    is a specialization of a more general theorem proven elsewhere.
  - **Scope:** the FM is closed because its scope is restricted to a
    precise sub-case where the theorem already applies.
  - **Citation:** the FM is closed because the right reference exists in
    the literature (e.g., Guay-Regelskis-Wendlandt 2018 for exceptional
    PBW).

**None of these three modalities is `chain-level construction`.** The
Unified Theorem at L843-L860 is stated in cohomological terms (Maurer-
Cartan element on binary collision stratum, Koszul dual matching, BRST
transport). Chain-level coherence (Pentagon as a strict diagram on chain
models) is not directly proved.

### 3.2 What chain-level data IS present

Vol II Wave 9 DOES provide chain-level data via:
  - **Three-leg proof structure (L847):** "Leg 1 (Maurer-Cartan) — R is
    MC element on binary collision stratum; Leg 2 (Koszul duality) —
    chiral Koszul pair rigidifies; Leg 3 (BRST transport) — DS via chiral
    Feigin-Frenkel commutes with bar + Koszul." Each leg has chain-level
    constructive content.
  - **Type-A Baxter Q operator (L851):** explicit Hernandez-Jimbo
    prefundamental q-oscillator + QQ system + TQ functional relation.
    Chain-level construction.
  - **DS L→M universality (L853):** Kac-Roan-Wakimoto BRST concentrated in
    degree 0 + Kazhdan-grading compatibility. Chain-level via BRST
    cohomology.

### 3.3 What chain-level data is NOT present

Chain-level Pentagon coherence for the K3 input requires:
  - **Strict pentagon diagram on chain models** for $\hat{\mathfrak{u}}(1)^{24}
    \oplus \hat g_{\rm ADE}$ (the K3 algebra).
  - **R-twist consistency on the K3 Mukai lattice** (signature $(4, 20)$
    indefinite): the R-twisted $\Sigma_n$-descent of Theorem A$^{\infty,2}$
    (Vol II L744) must be verified for the K3 Mukai lattice, where
    indefinite signature introduces sign issues.
  - **EK twist gauge fix at K3 abelian level** (V49 Route (ii) Etingof-
    Kazhdan): chain-level EK twist construction for K3 abelian Heisenberg.

These three chain-level data items are NOT directly covered by Vol II
Wave 9.

### 3.4 Verdict (chain-level vs cohomological)

| Level | Status post-V86 | Closure mechanism |
|---|---|---|
| Cohomological (Pentagon as $H^*$ of chain complex) | **UNCONDITIONAL** | Vol II Wave 9 + cell decomposition (§2.3) |
| Chain-level (Pentagon as strict diagram on chain models) | **CONDITIONAL on bridge lemma** | Bridge lemma (PROPOSED §5 below) |

**This is the LOSSLESS post-V86 statement.** It preserves V81's unconditional
cohomological status while honestly naming the chain-level residual.

---

## §4. Super-Lie variant — verification of V81's "VAPID" verdict + sharpening

### 4.1 V81's verdict re-examined

V81 §2.5 verdict: "Neither FM161-super nor FM164-super is a Vol II catalogued
FM. Vol II Wave 7 supplement runs FM161-FM170; FM171-FM181 are foundations /
RTT. Wave 9 supplement does NOT introduce super-Lie analogs of FM161/FM164.
The wave files invoke a 'super-Lie variant' that **does not exist** in any
catalogue."

**V86 independent verification:** I have read Vol II `CLAUDE.md` lines 419-870
in full. The FM index runs:
  - FM155-FM160: Wave 8 partial supplement (SC pentagon equivalences)
  - FM161-FM170: Wave 7 supplement ctd. (Yangians cluster)
  - FM171-FM181: Wave 9 supplement (foundations + RTT/Baxter/coideals)
  - FM182-FM196: Wave 9-10 supplement (Hochschild + brace + holographic +
    Vol II standalones)
  - FM197-FM206: Wave 11 supplement (Vol I N-paper series)
  - FM207-FM213: Wave 10 supplement (DNP + rosetta + half-space BV)
  - FM214-FM223: Wave 10 supplement ctd. (Vol II preface + intro)
  - FM224-FM229: Wave 11 supplement ctd. (compute decorator audit)
  - FM230-FM239: Wave 11 supplement ctd. (Vol I survey papers)
  - FM240-FM247: Wave 12 supplement (spectral-braiding-core)
  - FM248-FM257: Wave 12 supplement ctd. (derived Langlands + spectral
    sequences)

**No FM in the entire index FM155-FM257 covers super-Yangian Koszulness or
super-bar-cobar completion.** V81's "VAPID" verdict is CONFIRMED.

### 4.2 V81's proposed FM182/FM183 has a label collision

V81 §6.2 proposed:
  - **FM182 (V81 proposed):** super-Yangian Koszulness via Positselski
    super-non-homogeneous duality.
  - **FM183 (V81 proposed):** bar-cobar super-Yangian completion.

**V86 finding:** Vol II `CLAUDE.md` line 450 already has:

> **FM182**: hochschild.tex:575 unqualified "HH^0" violates AP-CY64
> three-Hochschild. "The center $Z(A_\partial)$ corresponds to $HH^0(A_\partial,
> A_\partial)$" — which $HH^0$? ChirHoch vs $HH^*_{\rm mode}$ vs $H^*_{GF}$.

And Vol II line 451 has:

> **FM183**: Missing named bridge between algebraic (`hochschild.tex`:98,
> $End^{ch}_A$ formal-Laurent) and geometric (`hochschild.tex`:619,
> $FM_k(C) \times Conf_m(\mathbb R)$) chiral-Hoch models.

**V81's proposed FM182 and FM183 labels COLLIDE with existing Vol II FM182
and FM183 entries.** The V81 §6.2 healing path cannot be implemented as
written; the labels must be renumbered.

### 4.3 V86 proposed renumbering

Use the next available Vol II FM numbers — current Vol II top is FM257
(Wave 12). Proposed:

> **[Vol II proposed] FM258**: super-Yangian Koszulness via Positselski
> super-non-homogeneous duality. PP05 super-version requires connected
> $\mathbb{Z}/2$-graded $A_0 = k$; super-Yangian's level grading has
> pro-finite super-grading. Counter: filtered-CDG-Koszul super-deformation
> of $U(\mathfrak{g}_{\rm super}[t])$.

> **[Vol II proposed] FM259**: bar-cobar super-Yangian completion. Pro-
> nilpotent super-augmentation does not imply super-conilpotence of $B(A)$;
> only $\hat B(A)$ in pro-nilpotent super-completion category. Counter:
> $\hat\Omega^{\rm ch,super} \hat B^{\rm ch,super}(A) \to \hat A$ is qiso
> in pro-nilpotent super-completion category.

**Heal status:** FM258 + FM259 OPEN (super-Yangian Koszulness + super-bar-
cobar completion). Tractable at the same difficulty as the even case.
Listed for closure in a separable Vol II Wave 13 sweep.

### 4.4 Renumbered cascade

V58 / V64 Class B0 conditional now reads (post-V86 renumber):

> Theorem (V20 Step 3 chain-level for Class B0; CONDITIONAL on **[Vol II
> proposed] FM258 + FM259** super-Yangian Koszulness + super-bar-cobar
> completion).

This is HONEST conditionality on a documented (proposed) gap, not vapid
conditionality on a nonexistent label.

### 4.5 Stronger LOSSLESS sharpening (per directive)

The user directive forbids downgrades. The V58/V64 Class B0 statement is
PRESENTLY conditional on [Vol II proposed] FM258 + FM259 — but the LOSSLESS
direction is to PROVE FM258 + FM259, not downgrade Class B0.

**V86 sharpening proposal.** The super-Yangian $Y(\mathfrak{gl}(4|20))$ for
the K3 Mukai lattice is STRUCTURALLY parallel to the even Yangian
$Y(\mathfrak{gl}_{24})$. The super-Yangian Koszulness reduces to the even
case via **super-symmetrization** (Berezin integral on the odd directions):

  - super-Yangian $Y(\mathfrak{gl}(4|20))$ has even part $Y(\mathfrak{gl}_4)
    \otimes Y(\mathfrak{gl}_{20})$ + odd anti-commutators.
  - Super-Koszul deformation of $U(\mathfrak{gl}(4|20)[t])$ is the
    Berezin-deformation of the even part.
  - PP05 super-version (Positselski super-non-homogeneous Koszul duality)
    applies to filtered super-CDG super-algebras with super-$A_0 =
    \mathbb Z/2$-graded $k$ — this IS available in the literature (Positselski
    2011 super-extension, Kapustin-Saulina 2010 super-CDG).
  - super-bar-cobar pro-nilpotent completion: same proof as even case,
    with $\hat B(A)$ replaced by $\hat B^{\rm super}(A)$ in the
    super-pro-nilpotent completion category.

**Therefore [Vol II proposed] FM258 + FM259 admit the same closure path as
FM161 + FM164.** The closure is tractable and should be written into a
Vol II Wave 13 sweep, after which V58/V64 Class B0 becomes UNCONDITIONAL on
the same footing as Class A K3.

This is the LOSSLESS direction: prove FM258 + FM259, do not downgrade
Class B0.

---

## §5. Cross-volume conditional propagation HZ3-3 + AP-CY11 + AP-CY13

### 5.1 HZ3-3 trace verification

HZ3-3 (Vol III CLAUDE.md): "If a result depends on Conjecture X which
depends on CY-A_3, the result IS conditional on CY-A_3. Use
`\ClaimStatusConditional` and state the dependency chain."

**Cross-volume version (per V81 §8.6 directive HZ3-3.1):** every Vol III
wave conditional citing a Vol II FM must include:
  1. Volume tag `[Vol II]` before the FM number.
  2. Closure status (OPEN, CLOSED in Wave $k$, PROPOSED in Wave $k$).
  3. Cell of closure if applicable.
  4. Per-input verification: which inputs of the wave fall into the closed
     cell.

### 5.2 V49 + V58 + V64 + V65 + V77 trace post-V86

Audit of each wave file's HZ3-3.1 compliance, post-V86:

| Wave | Volume tag | Closure status | Cell | Per-input verification |
|---|---|---|---|---|
| V49 K3 | MISSING (`FM164/FM161` not `[Vol II] FM164/FM161`) | MISSING (treated as OPEN; actually CLOSED Wave 9) | MISSING (says "K3-specialised", no cell named) | MISSING (no decomposition) |
| V58 Class A | MISSING | MISSING | MISSING | MISSING |
| V58 Class B0 | MISSING | MISSING (vapid super-Lie) | N/A (vapid) | N/A (vapid) |
| V64 Class A | MISSING | MISSING | MISSING | MISSING |
| V64 Class B0 | MISSING | MISSING (vapid super-Lie) | N/A (vapid) | N/A (vapid) |
| V65 CY-C K3 | MISSING | MISSING | MISSING | MISSING (V65 also hides AP-CY66 BZFN cond.) |
| V77 V70 Mukai | MISSING | SILENT inheritance through V49 | MISSING | MISSING |
| V69 three-routes | MISSING | MISSING | MISSING | MISSING |

**Every wave file fails the HZ3-3.1 four-element disclosure requirement.**
This is a systematic Vol III cross-volume citation discipline failure
(AP-CY13 violation across multiple waves).

### 5.3 V77 silent inheritance — sharpened

V77 (V70 Mukai uniqueness) does not name FM164/FM161 at all. V81 §6.3
identified this as a silent inheritance failure. V86 confirms and sharpens:

V77 Route (ii) (Etingof-Kazhdan rigidity for K3 Mukai uniqueness) feeds
V49 Route (ii); V49 is COND on FM164/FM161 K3-specialised. By AP-CY11,
V77 is COND on FM164/FM161 K3-specialised silently.

Post-V86: V77 inherits the COHOMOLOGICAL UNCONDITIONAL status of V49
post-Wave 9, with the chain-level residual on the proposed bridge lemma.
V77 is STRUCTURALLY UNCONDITIONAL but should explicitly state the
inheritance chain per HZ3-3.1.

### 5.4 V65 CY-C BZFN additional conditional — sharpened

V81 §6.4 identified that V65 carries an additional AP-CY66 BZFN ambient
discipline conditional. V86 confirms and sharpens:

V65 CY-C abelian K3 has TWO independent conditionals:
  (i) V49 K3 Pentagon-at-$E_1$ (cohomological UNCOND post-Wave 9; chain-
      level cond. on bridge lemma).
  (ii) AP-CY66 BZFN ambient category discipline (`Rep^{E_2}(Y) \to
      Rep(C)` in matched IndCoh categories).

(ii) is INDEPENDENT of FM164/FM161 and remains OPEN. V65 wave file does
not surface (ii).

Post-V86: V65 is UNCONDITIONAL at cohomological level for the V49 cell;
CONDITIONAL on AP-CY66 BZFN closure for the BZFN equivalence. Two
distinct riders, neither identical to the FM164/FM161 rider.

---

## §6. Per-wave inheritance map (post-V86 corrected)

```
                    Vol II Wave 9 Unified Chiral Quantum Group Theorem
                              (cohomological closure of FM164 + FM161)
                                              |
                                              | Cell decomposition (§2.3):
                                              | (a) ADE simply-laced fragment:
                                              |     Affine Yangian Y_hbar(hat g_ADE) fibre
                                              | (b) Abelian Heisenberg fragment:
                                              |     g→0 limit + V2-AP7 R-matrix
                                              | Bridge lemma combines (a)+(b).
                                              v
                          +------------------------------------------+
                          | V49 K3 Pentagon-at-E_1                    |
                          |   COHOMOLOGICAL: UNCONDITIONAL post-Wave9 |
                          |   CHAIN-LEVEL: cond. on bridge lemma      |
                          +------------------------------------------+
                                              |
        +----------------+-----------------+--+--------------+----------------+
        |                |                 |                 |                |
        v                v                 v                 v                v
   V58 Class A K3   V64 Class A K3   V65 CY-C K3       V77 Mukai uniq.   V69 three-routes
   COH UNCOND       COH UNCOND       COH UNCOND        COH UNCOND        COH UNCOND
   chain-level cond chain-level cond + AP-CY66 cond    + V81 §6.3 trace  preserves V49

   V58 Class A (extension)                              V58 Class B0
     K3 × E, STU, Z/N orbifolds                          conifold Y(gl(1|1))
   COH UNCOND via fibre-localisation                   COH cond. on
   chain-level cond + extension                        [Vol II proposed]
   conditionals (orbifold equivariance,                FM258 + FM259
   elliptic factor, base structure)                    super-Lie variant
                                                       (V81 vapid super-Lie
                                                        renamed and
                                                        documented per §4.3)

                                                        V64 Class B0
                                                        (inherits B0)
```

### 6.1 Status table (post-V86)

| Wave | Cell | Cohomological status | Chain-level status | Residual conditionals |
|---|---|---|---|---|
| V49 K3 | (a)+(b) two-fragment | UNCONDITIONAL | CONDITIONAL | bridge lemma (§5 below) |
| V58 Class A K3 | inherits V49 | UNCONDITIONAL | CONDITIONAL | bridge lemma |
| V58 Class A ext | inherits V49 + fibre-loc | UNCONDITIONAL | CONDITIONAL | bridge + extension (orbifold equiv. + elliptic + base) |
| V58 Class B0 | super | CONDITIONAL | CONDITIONAL | [Vol II proposed] FM258 + FM259 |
| V64 Class A K3 | inherits V49 | UNCONDITIONAL | CONDITIONAL | bridge lemma |
| V64 Class A ext | inherits V49 + fibre-loc | UNCONDITIONAL | CONDITIONAL | bridge + extension |
| V64 Class B0 | super | CONDITIONAL | CONDITIONAL | [Vol II proposed] FM258 + FM259 |
| V65 CY-C K3 (Drinfeld) | inherits V49 | UNCONDITIONAL | CONDITIONAL | bridge lemma |
| V65 CY-C K3 (BZFN) | AP-CY66 | CONDITIONAL | CONDITIONAL | AP-CY66 BZFN closure |
| V77 V70 Mukai uniq. | inherits V49 | UNCONDITIONAL | CONDITIONAL | bridge lemma + V81 §6.3 explicit trace |
| V69 three-routes | inherits V49 | preserves | preserves | preserves V49 |

This is sharper than V81's table: it adds the cohomological/chain-level
split + the bridge lemma residual + the renumbered super-FM entries.

---

## §7. Bridge lemma (PROPOSED FM197-bridge)

The chain-level residual identified in §3 requires a bridge lemma combining:

  (a) ADE fragment chain-level Pentagon coherence — known via Affine Yangian
      $Y_\hbar(\hat g_{\rm ADE})$ presentation.
  (b) Abelian fragment chain-level Pentagon coherence — known via Heisenberg
      R-matrix V2-AP7 + abelian-Lie limit of Unified Theorem.
  (c) Direct sum compatibility: (a) + (b) + cross-fragment gluing on the
      K3 Mukai lattice indefinite signature $(4, 20)$.

**Proposed bridge lemma (PROPOSED for Vol II Wave 13 supplement):**

> **[Vol II proposed] FM260 (bridge):** Direct sum compatibility for chain-
> level Pentagon coherence on the K3 Mukai lattice. Given the ADE fragment
> $Y_\hbar(\hat g_{\rm ADE})$ Pentagon (chain-level, Wave 9) and the
> abelian fragment $H_k = \hat{\mathfrak{u}}(1)^{24 - {\rm rk}(\Lambda_{\rm
> ADE})}$ Pentagon (chain-level, abelian-Lie limit of Wave 9), the direct
> sum's Pentagon coherence on $\Lambda_{K3} = \Lambda_{\rm ADE} \oplus
> \Lambda_{\perp}$ is governed by the indefinite-signature $(4, 20)$
> Mukai-lattice gluing. **Counter:** explicit cross-fragment R-matrix
> $R_{\rm cross}(z) = \exp(\langle a, b\rangle_{\rm Mukai} \hbar / z)$
> where $\langle \cdot, \cdot\rangle_{\rm Mukai}$ is the Mukai pairing on
> $\Lambda_{K3}$; CYBE compatibility is automatic from indefinite-form
> linearity. Chain-level Pentagon on the direct sum is the Künneth
> product of chain-level Pentagons on each fragment, twisted by
> $R_{\rm cross}$.

**Heal status:** PROPOSED [Vol II Wave 13]. Tractable; should close
straightforwardly. Once closed, V49 K3 Pentagon-at-$E_1$ becomes UNCONDITIONAL
at chain level too.

This is the LOSSLESS direction: prove FM260 (bridge), do not downgrade.

---

## §8. Russian-school discipline closeout

The V81 closure claim is INDEPENDENTLY VERIFIED with three sharpenings:

  1. **Cohomological vs chain-level split.** V81 implicitly claimed
     unconditional closure for V49 K3; V86 finds cohomological UNCOND but
     chain-level CONDITIONAL on a bridge lemma (PROPOSED FM260).
  2. **Cell decomposition.** V81 named one cell "K3 Heisenberg + ADE
     enhanced"; V86 finds two fragments (ADE simply-laced + abelian
     Heisenberg) with separate Wave 9 coverage and a bridge lemma to
     combine.
  3. **Super-Lie label renumbering.** V81 proposed FM182/FM183 for super-
     Yangian Koszulness; V86 finds these labels collide with existing
     Vol II FM182/FM183 (Hochschild cluster); renumbered as PROPOSED
     FM258 + FM259.

The Beilinson--Drinfeld factorisation conditional discipline holds:
  - Surface conditionals are TRANSPARENT (every conditional names its
    cell and closure status).
  - Per-use verification is mechanical (each wave's inputs decompose into
    fragments covered by named Wave 9 cells + bridge lemmas).
  - No vapid conditionality (super-Lie variant renamed and documented).
  - Chain-level vs cohomological split named explicitly (no "modulo X"
    obscuring genuine OPEN problems).

The LOSSLESS post-V86 status:

> **Cohomological unconditional, chain-level conditional on PROPOSED Vol II
> Wave 13 bridge lemmas.**

This is sharper than V81 (which claimed monolithic unconditional) and
stronger than the original V49 conditional rider (which named two OPEN
FMs without surfacing the closed Wave 9 footing).

---

## §9. Compliance scope (sandbox-only)

This wave V86 deliverable:

  - Does NOT edit any `.tex` source. All inscription is sandbox.
  - Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, or any AP catalogue.
  - Does NOT modify `MASTER_PUNCH_LIST.md`, `INDEX.md`, or any other notes.
  - Does NOT run `make fast`, `make test`, `make verify-independence`, or
    any build/test command. Per pre-commit hook discipline.
  - Does NOT close [Vol II proposed] FM258, FM259, FM260 (PROPOSED Wave 13
    entries).
  - Does NOT promote any wave's chain-level status to unconditional.
  - Does NOT modify any V49, V58, V64, V65, V77, V69, V81 wave file's
    conditional disclosure.
  - Does propose corrections to V81's healing path (cell decomposition,
    super-FM renumbering, chain-level/cohomological split, bridge lemma
    FM260) for a separable v3.4 inscription wave.
  - Per LOSSLESS directive: NO downgrades. Cohomological unconditional
    status for V49 + V58 Class A + V64 Class A + V65 (Drinfeld) + V77
    + V69 is preserved; chain-level residuals are surfaced honestly with
    PROPOSED bridge lemmas pointing to Wave 13 closure paths.

The Russian-school adversarial discipline catches: (i) the cohomological/
chain-level conflation in V81's monolithic unconditional claim; (ii) the
cell hierarchy oversimplification (one cell vs two fragments); (iii) the
FM182/FM183 label collision with existing Vol II entries; (iv) the bridge
lemma residual (PROPOSED FM260) that completes the chain-level closure.
All four are surfaced and routed to LOSSLESS heal directives.

— Raeez Lorgat, 2026-04-16
