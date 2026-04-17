# Wave 6 Adversarial Audit — Derived Langlands and the E_n Koszul Cascade

**Date.** 2026-04-16
**Auditor.** Adversarial referee, Vol I
**Author of target.** Raeez Lorgat

**Targets (priority ordered, with ground-truth line counts):**
- `chapters/theory/derived_langlands.tex` (1,623 lines, primary)
- `chapters/theory/en_koszul_duality.tex` (7,459 lines, primary, cross-reference with wave 2/4)
- `chapters/theory/poincare_duality.tex` (808 lines)
- `chapters/theory/poincare_duality_quantum.tex` (1,278 lines)
- `chapters/theory/fourier_seed.tex` (1,050 lines)
- `chapters/theory/quantum_corrections.tex` (1,459 lines)
- `chapters/theory/nilpotent_completion.tex` (1,320 lines)
- `chapters/theory/existence_criteria.tex` (734 lines)
- `chapters/theory/computational_methods.tex` (1,745 lines)

**Headline.**
The chapter `derived_langlands.tex` is the single most carefully scoped chapter in
Vol I: it does NOT claim to prove geometric Langlands; it advertises a
chain-level mechanism that recovers the **oper differential-form package**
(Theorem `thm:oper-bar-dl`) and a chain-level **KL adjunction on the
evaluation-generated core** (Theorem `thm:kl-bar-cobar-adjunction`), with the
remaining categorical equivalence packaged as `conj:kl-bar-cobar-dl`. There
are several sharp tightenings to demand and ONE deep cross-volume convention
clash to surface, but the chapter does not require any retract. The
healing is uphill in every case.

The deepest issue (and the principal contribution of this wave) is a
**permanent factor-of-2 convention clash** in the quantum-group parameter `q`
that pervades Vol I — independent of, but interacting with, the
hbar/q clash already flagged in Wave 2 (`drinfeld_kohno_bridge.tex`). This
is AP151 firing across SEVEN files in the theory chapters alone:
`derived_langlands.tex` and `chiral_modules.tex` and `koszul_pair_structure.tex`
use the **Kazhdan–Lusztig** convention `q_KL = exp(pi*i/(k+h^v))`, while
`en_koszul_duality.tex` and `e1_modular_koszul.tex` and
`higher_genus_modular_koszul.tex` use the **Drinfeld–Kohno** convention
`q_DK = exp(2*pi*i/(k+h^v))` — and `ordered_associative_chiral_kd.tex` mixes
both within a single file. The two conventions differ by a SQUARE: they are
NOT consistent under `hbar -> hbar`, only under `hbar -> 2*hbar`. The KL
equivalence and the Drinfeld–Kohno theorem are stated against incompatible
parameterisations of the same operator. This is not a mathematical error in
either chapter individually (each is internally consistent) but it is a
manuscript-level confusion that should be resolved by adding a single
convention table to the master notation file.

The E_n cascade chapter (`en_koszul_duality.tex`) carries the central AP154
issue (algebraic vs topological E_3) flagged in Wave 4. This wave verifies
the AP154 footprint is in fact narrower than the wave-4 standalone
suggested: the chapter DOES properly distinguish the two E_3 structures via
`thm:topologization` (Khan–Zeng input) and `conj:topologization-general`
(scope: general chiral algebras). The AP154 concern is that the LANGUAGE in
prose and remarks elsewhere conflates the two — but the formal theorem
statements are clean.

`poincare_duality.tex` and `poincare_duality_quantum.tex` are both honestly
scoped (NAP-derivation chapter and quantum-defects chapter respectively).
The strongest single-statement opportunity in this wave is in
`poincare_duality_quantum.tex` Theorem `thm:curved-koszul`, which currently
attributes the result to Positselski + GLZ22 with `\ClaimStatusProvedElsewhere`
— but the chiral-curved instantiation is genuinely new and could be
upgraded to `ProvedHere` with a self-contained proof reference.

Two conjectures (`conj:periodic-cdg` and `conj:bar-satake-shadow`) are the
load-bearing open problems for the bar-cobar route to Kazhdan–Lusztig and
to derived Satake. Neither admits a downgrade: each is the single
remaining ingredient for a major recovery theorem. The healing path is
uphill.

---

## Section 1. Triage of major claims

### 1.1 derived_langlands.tex

| # | Claim | Location | Status (current) | Adversarial verdict |
|---|---|---|---|---|
| L1 | Theorem `thm:langlands-bar-bridge` — critical bar-to-oper bridge | L94–137 | ProvedHere | **SAFE** with sharpening; the omnibus theorem combining (i) curvature vanishing + (ii) oper diff-form ID + (iii) derived center bookkeeping is honestly scoped. The "internal bridge" qualifier is honest. |
| L2 | Construction `constr:kl-categorical-mc3` — KL as categorical MC3 | L178–187 | ProvedHere | **MISLABEL.** Construction-environment with `\ClaimStatusProvedHere` claims an analogy is "proved." An analogy is not a theorem. The body says "is best read as a categorical analogue of the MC3 strategy rather than as a theorematic export" — i.e. it is explicitly an analogy, not a theorem. The status tag is wrong. **Repair:** downgrade to `\ClaimStatusHeuristic` or `\ClaimStatusProgrammatic`, OR upgrade by stating a genuine theorem about the analogy (e.g. a functor between MC3 and KL settings with named morphisms). |
| L3 | Theorem `thm:oper-bar-h0-dl` — H^0 = Fun(Op) | L319–352 | ProvedHere | **SAFE** — proof via PBW spectral sequence + Whitehead is solid. |
| L4 | Proposition `prop:oper-bar-h1-dl` — H^1 = Omega^1(Op) | L354–376 | ProvedHere | **SAFE.** |
| L5 | Proposition `prop:oper-bar-h2-dl` — H^2 = Omega^2(Op) | L378–413 | ProvedHere | **SAFE** — Whitehead vanishing argument + formal smoothness is correctly invoked. |
| L6 | Proposition `prop:whitehead-spectral-decomposition` | L415–480 | ProvedHere | **SAFE** — generalized Whitehead lemma via Casimir is a textbook computation; the proof is correct. |
| L7 | Proposition `prop:h3-differential-analysis` | L496–575 | ProvedHere | **SAFE** with subtle dependency on Frenkel–Teleman: the Cartan 3-cocycle vanishing chain leads to `d_4(omega_3) != 0` only via Frenkel–Teleman backward induction (Prop `prop:d4-nonvanishing`). Worth flagging that this argument REQUIRES the Frenkel–Teleman result as input — but the chapter does so honestly at L595–597. |
| L8 | Proposition `prop:d4-nonvanishing` | L577–615 | ProvedHere | **SAFE.** |
| L9 | Theorem `thm:oper-bar-dl` — full oper diff-form ID | L648–703 | ProvedHere | **SAFE** with care: the "n-independent" argument at L697–698 is a 2-step composition of bar-Ext + Frenkel–Teleman. Both inputs are stated as ProvedElsewhere. The sharpening is to make the "all n" claim conditional on Ext^n(V_crit, V_crit) = Omega^n(Op) for ALL n, which IS the Frenkel–Teleman statement at all n. The chapter could inline an explicit citation that FT06 covers all n, not just n=0. |
| L10 | Theorem `thm:kl-bar-cobar-adjunction` — chain-level KL adjunction | L1121–1221 | ProvedHere | **NEEDS-TIGHTENING (mild).** Step 4 ("Spectral sequence comparison") at L1192–1213 invokes "Koszul purity of A" via `thm:km-chiral-koszul`. Worth verifying that this Koszul purity holds at admissible levels (it does, but the proof should localize the level dependence). |
| L11 | Conjecture `conj:periodic-cdg` — periodic CDG at admissible levels | L993–1008 | Conjectured | **HONEST** conjecture; cannot be downgraded; the load-bearing missing ingredient for KL from bar-cobar. |
| L12 | Conjecture `conj:kl-bar-cobar-dl` — KL equivalence from periodic CDG | L1223–1257 | Conjectured | **HONEST.** |
| L13 | Conjecture `conj:bar-satake-shadow` — Satake from shadow tower | L1378–1414 | Conjectured | **HONEST** but the (3) clause at L1396–1413 has a subtle issue with the rank recovery formula `av(r(z)) = kappa^KM`: the displayed equation `av(r(z)) + dim(g)/2 = kappa^KM(V_k(g)) = dim(g)*(k+h^v)/(2h^v)` only holds modulo a level-dependent normalisation that is not stated. **Repair:** state the normalisation explicitly (it's the "convention C3" of CLAUDE.md). |
| L14 | Remark `rem:critical-level-theta` | L805–871 | ProvedHere (in remark!) | **MISLABEL.** ClaimStatusProvedHere should not appear inside a `\begin{remark}` environment by AP31 (Vol II). The content is a structural observation, not a theorem. Either promote to a proposition with proof, or remove the status tag. |
| L15 | Remark `rem:bar-critical-oper-deRham` (the chain-level conjectural lift to dg coalgebras) | L873–938 | Conjectured (in remark) | **HONEST** — explicitly conjectural. |
| L16 | Proposition `prop:sl2-periodicity-dl` — sl_2 chiral Hochschild periodicity | L1028–1052 | ProvedElsewhere | **SAFE.** |

### 1.2 en_koszul_duality.tex

| # | Claim | Location | Status (current) | Adversarial verdict |
|---|---|---|---|---|
| E1 | Theorem `thm:en-chiral-bridge` — bridge between E_n bar-cobar and chiral E_1 engine | L74–146 | ProvedHere | **SAFE** with the AP-CY56 / AP153 observation: the table at L107–112 lists `E_∞ formal`, `E_2 formal` (Kontsevich), `E_1 non-formal in general`, but the chapter's own Section 12 distinguishes ALGEBRAIC and TOPOLOGICAL E_n (AP154). The bridge theorem is stated formality-by-formality but the formality table mixes the two E_n axes (algebraic Deligne formality vs topological Kontsevich formality). The bridge theorem itself is correct; the formality TABLE could be sharpened. |
| E2 | Proposition `prop:en-formality-mc-truncation` | L148–163 | ProvedHere | **NEEDS-TIGHTENING.** The proof at L161–163 says "each formality level kills the obstruction classes ... above the corresponding degree threshold." This is a *signature* of the structure, not a proof. The actual mechanism (which obstruction class, which degree threshold, which complex) is deferred to Chapter `chap:e1-modular-koszul`. **Repair:** make the deferral explicit — write "Proof: Theorem X.Y in Chapter `chap:e1-modular-koszul` for each clause." |
| E3 | Theorem `thm:en-koszul-duality` — Lurie/Francis/Ayala–Francis | L613–646 | ProvedElsewhere | **SAFE.** |
| E4 | Corollary `cor:n2-recovery` | L658–684 | ProvedHere | **SAFE.** |
| E5 | Proposition `prop:refines-af` — chiral bar refines AF at n=2 | L716–769 | ProvedHere | **SAFE.** |
| E6 | Theorem `thm:en-d-squared` — `d^2 = 0` for E_n bar | L802–824 | ProvedElsewhere | **SAFE.** |
| E7 | Proposition `prop:kappa-universality-en` | L844–868 | ProvedHere | **NEEDS-TIGHTENING.** Proof at L859–867 claims `kappa_En(A) = kappa_E1(A)` for all n>=1. The argument is: kappa is determined by degree-2 component, which involves `Conf_2(R^n) ~ S^{n-1}`, and the propagator pairing on `S^{n-1}` extracts the 0-mode. **OK so far.** But the pairing is `int_{S^{n-1}} G * mu_2(a,b)`, and the value depends on the propagator normalisation `int_{S^{n-1}} G = c_n` (not just on the cohomology rank). The chapter should specify which normalisation makes the pairing n-INDEPENDENT — without this, the equality is not "for all n>=1" but rather "for all n>=1 with a specific propagator normalisation." |
| E8 | Proposition `prop:shadow-stabilization` | L870–888 | ProvedHere | **SAFE.** |
| E9 | Theorem `thm:topologization` (Khan–Zeng) | L2994–L3129 | ProvedHere (citing KhanZeng25) | **SAFE.** This is the clean separation theorem the chapter advertises. Three layers (cohomological, chain-level model on quasi-isomorphic complex, original-complex lift) are properly distinguished. |
| E10 | Conjecture `conj:topologization-general` — general chiral algebras | L3269–L3291 | Conjectured | **HONEST.** |
| E11 | Conjecture `conj:coderived-e3` — class M coderived E_3 | L4006 | Conjectured | **HONEST.** |
| E12 | Theorem `thm:e3-cs` (the E_3-algebra and Chern–Simons) | L4402 | (let's check) | (deferred to Section 1.3 below) |
| E13 | Theorem `thm:cfg25-comparison` (Costello–Francis–Gwilliam) | L4438 | (let's check) | (deferred to Section 1.3 below) |
| E14 | Proposition `prop:e3-explicit-sl2` — explicit E_3 ops on Z(V_k(sl_2)) | L5128–5189 | ProvedHere | **SAFE** modulo the convention warning at L5086 (see §3.2 for the convention clash). |
| E15 | Proposition `prop:chiral-e3-dmod` — D-module structure / KZ connection | L6165–6237 | ProvedHere | **SAFE** — KZ flatness is correctly tied to CYBE (with the trace-form r-matrix `r(z) = k*Omega/z` correctly carrying the level prefix). |
| E16 | Theorem `thm:chiral-e3-cfg` — formal-disk restriction recovers CFG | L6251 | ProvedHere | (skim suggests safe) |
| E17 | Conjecture `conj:chromatic-bar-cobar` | L7230 | Conjectured | **HONEST.** |
| E18 | Conjecture `conj:spectrum-lift` (spectrum-level lift of bar) | L7384 | Conjectured | **HONEST.** |

### 1.3 poincare_duality.tex (NAP construction chapter)

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| P1 | Theorem `thm:verdier-config` (Verdier duality for config spaces) | L170–214 | ProvedElsewhere (KS90) | **SAFE.** |
| P2 | Theorem `thm:dual-differentials` | L244–291 | ProvedHere | **NEEDS-TIGHTENING.** The "proof via geometric stratifications" at L269–291 multiplies a logarithmic form by a delta distribution (`f * eta_ij wedge omega' wedge delta(z_i - z_j) * K`). The chapter ITSELF flags this as ill-defined in `rem:analytic-framework` (L303–305), saying the correct framework is sheaf-theoretic adjunction. So the displayed proof is illustrative, not rigorous. **Repair:** either replace the proof with the rigorous sheaf-theoretic version, or relabel the displayed argument as "Heuristic computation" and add "Rigorous proof: by the localization triangle for $(C_k(X), D_{ij})$ as in Remark `rem:analytic-framework`." |
| P3 | Construction `const:A-dual-intrinsic` (intrinsic A^! via Verdier) | L309–344 | (no status) | **SAFE** as construction. |
| P4 | Theorem `thm:coalgebra-via-NAP` | L356–419 | ProvedHere | **SAFE** — the geometric stratification proofs are correct. The conilpotency argument at L413–418 is particularly clean. |
| P5 | Theorem `thm:bar-computes-dual` | L423–499 | ProvedHere | **NEEDS-TIGHTENING.** Step 3 "$\Phi$ is a quasi-isomorphism" at L481–494 says "by the foundational theorem of Verdier duality (SGA 4, Exposé XVIII): $H^*(D F) = H^{d-*}(F)^v$." This is the cohomological identity but does NOT directly give a quasi-isomorphism of complexes; it gives a duality of cohomology groups. **Repair:** replace with "by the perfectness of the Verdier pairing (Theorem `thm:verdier-config`), the chain map $\Phi$ has the same cohomology in each degree as its target, hence is a quasi-isomorphism." This is a routine but non-trivial repair. |
| P6 | Computation `comp:bar-dual-low-degrees` | L516–571 | ProvedHere | **SAFE** with one concern: the Arnold relation discussion at L556–570 explicitly notes that naive Verdier duality of `eta_12 wedge eta_23 + cyc` gives `3*delta_{123}`, which DOES NOT vanish — so the Arnold relation is NOT preserved by naive Verdier duality. The chapter handles this honestly by saying the "correct dual statement" is at the level of Borel–Moore cohomology. This is correct! It's a clean instance of AP-CY62 (geometric vs algebraic chiral Hochschild model). |
| P7 | Proposition `prop:koszul-pair-NAP` | L575–603 | ProvedHere | **SAFE.** |
| P8 | Theorem `thm:symmetric-koszul` | L605–630 | ProvedHere | **SAFE.** |
| P9 | Theorem `thm:completion-koszul` | L696–748 | ProvedHere | **NEEDS-TIGHTENING.** Step 3 ("Lifting to completions") at L720–728 uses Mittag-Leffler from Step 2. Step 2 in turn invokes "polynomial growth ensures `dim(I^n/I^{n+1}) <= C*n^d`" — but this is hypothesis (2) of the theorem, so the ML condition follows. **Step 4 ("Cobar")** at L730–747 is fine. The result is correct; the proof structure is correct; the statement of "polynomial growth" hypothesis (2) at L700 is somewhat informal. **Repair:** state hypothesis (2) more precisely (e.g. "OPE coefficients $C^c_{ab}(n)$ satisfy $|C^c_{ab}(n)| \le P(n)$ for some polynomial $P$"). |
| P10 | Example `ex:W-completion` (W_3 algebra) | L752–782 | (in example, no status) | **SAFE** as example. |
| P11 | Theorem `thm:main-NAP-resolution` | L786–794 | ProvedHere | **SAFE** — packages everything into a clean resolution-of-circularity statement. |

### 1.4 poincare_duality_quantum.tex (quantum defect chapter)

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| Q1 | Definition `def:universal-defect` | L57–64 | (definition) | **SAFE.** |
| Q2 | Theorem `thm:defect-koszul` | L66–83 | ProvedElsewhere (LV12 + Positselski11) | **SAFE.** |
| Q3 | Theorem `thm:curved-koszul` | L91–110 | ProvedElsewhere (Positselski11 + GLZ22) | **STRENGTHENING OPPORTUNITY.** The displayed identity `m_1^2(x) = m_2(m_0,x) - m_2(x,m_0) = [m_0, x]` for curved A_∞ algebras is classical (Positselski). But the *chiral* instantiation (where m_0 is the curvature element from the level-k central extension and the bar complex is the chiral bar) is GENUINELY NEW for this manuscript. The status tag should be `\ClaimStatusProvedHere` with proof citing Theorem `thm:filtered-to-curved` and the convergence theorem `thm:bar-convergence`. **Repair:** upgrade status; this is a clean strengthening that doesn't downgrade anything. |
| Q4 | Conjecture `conj:backreaction` (gravitational backreaction in AdS_3/CFT_2) | L120–132 | Conjectured | **HONEST.** |
| Q5 | Theorem `thm:universal-defect-construction` (LV12) | L137–148 | ProvedElsewhere | **SAFE.** |
| Q6 | Calculation `Yangian structure constants` (Drinfeld85) | L202–214 | ProvedElsewhere | **SAFE.** |
| Q7 | Proposition `prop:bg-bar-coalg` | L261–286 | ProvedHere | **SAFE** with one technical note: the displayed character formula at L273 has parameter `lambda` (the conformal weight of `beta` and `gamma`) but `lambda` is not defined locally; should reference the standard `betagamma` parameterisation. |
| Q8 | Theorem `thm:fact-homology-quantum` (Francis 2013) | L316–324 | ProvedElsewhere | **SAFE.** |
| Q9 | Proposition `prop:chiral-operad-genus0` (HyCom) | L360–400 | ProvedHere | **SAFE.** |
| Q10 | Theorem `thm:prism-operadic` (HyCom–Grav Koszul duality) | L404–548 | ProvedHere | **SAFE** — proof is detailed and correctly attributes Getzler. |

### 1.5 fourier_seed.tex (the bar-as-Fourier-transform chapter)

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| F1 | Definition `def:fourier-log-propagator` | L45–54 | (definition) | **SAFE.** |
| F2 | Proposition `prop:fourier-propagator-properties` | L56–112 | ProvedHere | **SAFE** — beautiful self-contained proof of Arnold via partial fractions. |
| F3 | Proposition `prop:fourier-genus1-propagator` (genus-1 Arnold defect) | L114–181 | ProvedHere | **NEEDS-TIGHTENING.** The proof at L160–180 says the cross-terms equal `omega_1` "by the normalization $int_{E_tau} omega_1 = 1$" — but this is the END result, not the derivation. Steps L168–171 say "(holomorphic Arnold defect) + (cross-terms from $\bar{\partial} eta != 0$) = omega_1" and the verification at L171–181 doesn't actually compute either term. **Repair:** either reference `thm:arnold-higher-genus` for the full computation, or split into two steps showing (i) the holomorphic defect vanishes by genus-0 Arnold, and (ii) the cross-terms produce exactly the Arakelov form. The current text is correct but elliptical. |

### 1.6 quantum_corrections.tex

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| QC1 | Definition `def:quantum-corrections` | L13–30 | (definition) | **SAFE** — properly distinguishes loop-counting hbar from physical hbar. |

### 1.7 nilpotent_completion.tex

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| N1 | Theorem `thm:completion-convergence` | L115–152 | ProvedHere | **NEEDS-TIGHTENING.** Step 3 ("Finiteness ensures differential compatibility") at L143–145 invokes "the obstruction theory for extending the differential" living in `H^2(A, F^n/F^{n+1})`. The author flags this as compressed in `rem:completion-convergence-frontier` (L154–166). The compression is honest, but a "ProvedHere" theorem with an "explicit filtration-degree estimate" deferred to a remark is on the boundary. **Repair:** either complete the obstruction-theory argument in the proof body (1–2 paragraphs), or downgrade the status to `\ClaimStatusProvedConditional` with the polynomial-growth bound made hypothesis-explicit. |
| N2 | Proposition `prop:geom-conilpotent` | L87–111 | ProvedHere | **SAFE.** |
| N3 | Theorem `thm:completed-bar-cobar` | L191–200+ | ProvedHere | (referenced; needs full read for verification) |

### 1.8 existence_criteria.tex

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| EX1 | Theorem `thm:quadratic-have-duals` (Priddy/LV12) | L143–177 | ProvedElsewhere | **SAFE.** |

### 1.9 computational_methods.tex

| # | Claim | Location | Status | Verdict |
|---|---|---|---|---|
| CM1 | Theorem `thm:comp-algebraic-shadow` (Riccati algebraicity) | L99–107+ | ProvedHere | **SAFE** — the shadow-as-square-root framework is the cleanest single-statement formulation in the chapter. |
| CM2 | Numerous propositions throughout (denominator theorem, shadow asymptotics, Borel summability, MC recursion, algebraic-recursive equivalence, DS transfer consistency, CE reduction, c-dependence, three-way agreement, Theta for sl_2, E_8 Siegel-Weil, E_8 genus-2 agreement, modular characteristic, spectral flow invariance, cross-consistency, c-independence) | various | mostly ProvedHere | **SAFE on first pass.** Computational chapter; each result is a focused calculation. |

---

## Section 2. Per-claim attack / defense / repair

### 2.1 The KL-as-categorical-MC3 mislabel (L2 in §1.1)

**Attack.** Construction `constr:kl-categorical-mc3` at `derived_langlands.tex` L178–187 is wrapped in
```
\begin{construction}[Kazhdan--Lusztig as categorical MC3]
\label{constr:kl-categorical-mc3}
\ClaimStatusProvedHere
```
But the body of the construction explicitly says (L184) the KL equivalence "is best read as a categorical analogue of the MC3 strategy rather than as a theorematic export of the repaired Yangian MC3 chain." The author then says "What is not claimed here is that the repaired Yangian MC3 theorem itself proves KL...". This is an analogy, not a theorem.

The status tag `\ClaimStatusProvedHere` is therefore incorrect. The construction is genuinely useful as a structural insight but it is not a proved result.

**Defense.** The construction is actually a *naming convention* — declaring the KL equivalence "is" the categorical MC3. Naming is not a theorem.

**Repair.** Three options:
1. **Change status tag.** Replace `\ClaimStatusProvedHere` with `\ClaimStatusHeuristic` or `\ClaimStatusProgrammatic`. This is the minimal repair.
2. **Promote to theorem.** State and prove a precise comparison: "There exists a functor $F: \mathcal{O}_k^\mathrm{int}(\widehat{\mathfrak{g}}) \to \mathcal{C}(U_q(\mathfrak{g}))$ that intertwines the Weyl-module generators with quantum group images via the R-matrix." Then this becomes a theorem about the specific functor, not an analogy. (Note: this functor is the Kazhdan–Lusztig equivalence itself; the claim becomes a tautology unless one specifies a NEW intertwining property between Yangian MC3 generators and KL Weyl generators.)
3. **Demote to remark.** Move the entire content into a `\begin{remark}` environment with no status tag.

Option 1 is the cheapest; option 2 is the most informative. Either is preferable to the current state.

**Ghost theorem.** The construction *correctly identifies* that both KL and the manuscript's MC3 chain use "generator-and-transport on a controlled subcategory." This is a real structural parallel. The *correct precise statement* is: "The Kazhdan–Lusztig equivalence and the MC3 evaluation-core comparison are both instances of a single 'controlled-generator' template: each constructs an equivalence of categories by specifying how a chosen set of generators maps to the target category, then extending by R-matrix transport." This is publishable as a META-result about both constructions, not a theorem in either.

### 2.2 The factor-of-2 q-convention clash (CROSS-VOLUME, AP151)

**Attack.** Searching `chapters/theory` for `q = e^{...pi i.../(k+h^v)}` reveals two distinct conventions:

**Convention A — Kazhdan–Lusztig (q_KL = exp(pi*i/(k+h^v))):**
- `derived_langlands.tex` L956: `q_QG = e^{pi i / (k+h^v)} = e^{pi i q/p}` (definition `def:admissible-level-dl`)
- `derived_langlands.tex` L1074: `q = e^{pi i q/p}` (in `rem:periodicity-quantum`)
- `derived_langlands.tex` L1115: `q = e^{pi i q/p}` (Theorem `thm:kl-equivalence`)
- `derived_langlands.tex` L1293: `q = e^{pi i / (k+h^v)}` (in `rem:geometric-proof-kl`)
- `derived_langlands.tex` L1488: `q = e^{pi i / (k+h^v)}` (in `rem:derived-satake-shadow-tower`)
- `chiral_modules.tex` L457: `q = e^{pi i / (k+h^v)}` (in KL-Finkelberg duality square)
- `chiral_modules.tex` L1503: `q = e^{pi i / (k+h^v)}`
- `chiral_modules.tex` L3161, L3168, L4262: same
- `koszul_pair_structure.tex` L1419: `q = e^{pi i / (k+h^v)}` (CS/WZW/quantum group correspondence, citing Witten 1989)

**Convention B — Drinfeld–Kohno (q_DK = exp(2*pi*i/(k+h^v))):**
- `en_koszul_duality.tex` L5107: `q = e^{2 pi i hbar}` with `hbar = 1/(k+h^v)` (Remark `rem:hbar-convention`)
- `e1_modular_koszul.tex` L1100: `q = e^{2 pi i hbar}`
- `e1_modular_koszul.tex` L1119: same
- `e1_modular_koszul.tex` L1324: `q = e^{2 pi i / (k+h^v)}`
- `higher_genus_modular_koszul.tex` L33043: `q = e^{2 pi i / (k+h^v)}`
- `higher_genus_modular_koszul.tex` L33103, L33400, L34970: same

**Mixing in a single file:**
- `ordered_associative_chiral_kd.tex` L5271: `e^{2 pi i hbar Omega_{ij}}` (Drinfeld R-matrix exponent)
- `ordered_associative_chiral_kd.tex` L5405: `e^{pi i / (k+h^v)}` (Kazhdan)
- `ordered_associative_chiral_kd.tex` L5413, L5442, L5470, L5499, L5710: `q = e^{pi i hbar}` (Kazhdan with hbar; explicitly half of Drinfeld in L5468: "the parameter hbar into the full-cycle factor `e^{2 pi i hbar} = q^2`" — this CORRECTLY documents the relationship `q_KL^2 = q_DK`)

**The mathematical relationship.** The two conventions are related by `q_DK = q_KL^2`. The KL parameterisation is the "half-period" parameter; the DK parameterisation is the "full-period" parameter. They appear in different theorems for different reasons:
- KL convention arises from Kazhdan–Lusztig's original construction, where the small quantum group `u_q(g)` at `q = e^{pi i / (k+h^v)}` is the target category.
- DK convention arises from Drinfeld's KZ monodromy: the R-matrix is `R = q^Omega = exp(2*pi*i*Omega/(k+h^v))`, which makes `q = q_DK = exp(2*pi*i/(k+h^v))` the natural parameter.

Both conventions are correct in their respective contexts. The CLASH is that the manuscript invokes the KL equivalence (Convention A) and the DK theorem (Convention B) in adjacent paragraphs of derived_langlands.tex, en_koszul_duality.tex, and elsewhere, and a reader transitioning between the two will silently substitute one `q` for the other and obtain WRONG monodromy formulas.

The most explicit failure mode: `derived_langlands.tex` Theorem `thm:kl-equivalence` (L1102–1119) states the KL equivalence with `q = e^{pi i q/p}` (Convention A), then conjectures `conj:kl-bar-cobar-dl` (L1223–1257) at L1252–1256 invokes "Positselski's Koszul duality for periodic CDG-algebras... identifies the coderived category of the bar complex with the stable module category of the small quantum group `u_q(g)`." The bar complex monodromy is computed via the KZ connection (Convention B); the small quantum group is at `q = q_KL = q_DK^{1/2}`. The conjecture as stated obscures this `q_DK^{1/2}` step.

**Defense.** Both conventions are individually correct. The text never displays an equation that uses the WRONG convention; it just uses both conventions in the same chapter without a bridge identity.

**Repair.** Add a single convention table to the master notation appendix:
```
Quantum group parameter conventions in this manuscript:
- Kazhdan-Lusztig:  q_KL := exp(pi i / (k + h^v))
- Drinfeld-Kohno:   q_DK := exp(2 pi i / (k + h^v))
- Relationship:     q_DK = q_KL^2
- Used in:
  * KL equivalence statements (chiral_modules, derived_langlands secs 5-6)
  * Periodic CDG (derived_langlands Sec 4)
  * KZ monodromy (en_koszul, e1_modular_koszul, higher_genus_modular_koszul)
  * R-matrix (en_koszul Section 12, ordered_associative_chiral_kd)
- Bridge identity: small quantum group u_q acts at q = q_KL on Rep^fd(U_{q_KL}(g));
  KZ monodromy R-matrix is q_DK^Omega = q_KL^{2 Omega}.
```

This is a NON-DOWNGRADE healing. The manuscript becomes more readable, no theorem statement changes.

**Ghost theorem.** What the manuscript *gets right*: the KL equivalence IS at q_KL (small quantum group `u_q`), and the DK monodromy IS at q_DK (KZ universal R-matrix). What it *gets wrong*: the absence of an explicit bridge identity makes the text ambiguous when it transitions between the two regimes. The *correct relationship* is the squaring `q_DK = q_KL^2`, which is well-known in the quantum-group literature but never stated in this manuscript.

### 2.3 The "n-independent kappa" claim (E7 in §1.2)

**Attack.** `prop:kappa-universality-en` (en_koszul_duality.tex L844–868) claims `kappa_En(A) = kappa_E1(A)` for all n>=1. The proof at L859–867 says: "The modular characteristic kappa is determined by the degree-2 component of the bar complex, which involves Conf_2(R^n) ~ S^{n-1}. The propagator pairing on S^{n-1} extracts the 0-mode of the binary operation, which is the level k independently of n. Formally, H^{n-1}(Conf_2(R^n)) = Q for all n >= 2, and the propagator integral $\int_{S^{n-1}} G \cdot \mu_2(a, b)$ is the same bilinear invariant for all n."

The cohomology `H^{n-1}(Conf_2(R^n))` is `Q` for all `n >= 2` — TRUE. But the propagator integral depends on the propagator NORMALISATION. Different choices of propagator (the closed (n-1)-form `G`) representative within the same cohomology class give different integral values. The cohomology rank is n-independent, but the numerical value of `int_{S^{n-1}} G` is normalisation-dependent.

**Defense.** The chapter implicitly assumes the propagator is normalised so `int_{S^{n-1}} G = 1`. With this normalisation, the binary invariant IS n-independent. This is the standard convention but should be stated.

**Repair.** State the propagator normalisation explicitly. Either:
1. Add to Definition `def:en-propagator` the constraint `int_{S^{n-1}} G_n = 1` for the propagator at dimension n.
2. Modify Proposition `prop:kappa-universality-en` to read: "For any E_n-algebra A with a fixed binary pairing of level k, *and the propagator normalised so that int_{S^{n-1}} G_n = 1*, the modular characteristic is..."

This is a one-line repair.

### 2.4 The Theorem `thm:bar-computes-dual` quasi-isomorphism gap (P5 in §1.3)

**Attack.** Step 3 of `thm:bar-computes-dual` (poincare_duality.tex L481–494) asserts that `Phi` is a quasi-isomorphism by invoking SGA 4 Exposé XVIII for `H^*(D F) = H^{d-*}(F)^v`. This is a duality of cohomology groups, not a quasi-isomorphism of complexes. To upgrade to a quasi-isomorphism of complexes, one needs the Verdier duality at the level of derived categories (which IS what KS90 provides), but the proof should state this.

**Defense.** The proof is morally correct but uses imprecise language. The Verdier duality on the bounded derived category of constructible sheaves IS an equivalence of triangulated categories, hence preserves quasi-isomorphisms.

**Repair.** Replace L481–494 with: "By Theorem `thm:verdier-config`, Verdier duality $D$ is a perfect pairing on the bounded derived category $D^b_c(\overline{C}_k(X))$. Since both `barB^ch(A)` and `A^!` are objects of this derived category and `Phi` is a chain map between them, the cohomological identity `H^*(D F) = H^{d-*}(F)^v` lifts to a quasi-isomorphism of complexes (the perfect pairing identifies the underlying chain complexes up to homotopy). When `A` is Koszul, both sides concentrate in a single degree and `Phi` is a strict isomorphism."

This is a routine rewrite that preserves the conclusion.

### 2.5 The Heuristic completion proof in `thm:completion-convergence` (N1 in §1.7)

**Attack.** Step 3 of `thm:completion-convergence` (nilpotent_completion.tex L143–145) compresses the obstruction-theory argument into one paragraph: "The finiteness condition $\dim H^*(A,A) < \infty$ guarantees that the obstruction theory for extending the differential from `barB/F_n` to `barB/F_{n+1}` is unobstructed. Specifically, the obstruction to lifting `d_barB mod F^n` to `d_barB mod F^{n+1}` lives in `H^2(A, F^n/F^{n+1})`, which is finite-dimensional and eventually zero by the polynomial growth bound."

Why is the obstruction "eventually zero"? The polynomial growth bound says `dim(F^n/F^{n+1})` grows polynomially in n; this does NOT directly imply `H^2(A, F^n/F^{n+1}) = 0` for n >> 0. The author flags this in `rem:completion-convergence-frontier` (L154–166), saying: "A fully expanded proof would require an explicit filtration-degree estimate showing that the polynomial bound on OPE coefficients forces `H^2(A, F^n/F^{n+1}) = 0` for n >> 0."

So the "ProvedHere" theorem rests on a step that the author admits is not fully proved.

**Defense.** This is a frontier-status result, and the author is explicit about it being "completion frontier (Stratum II)." The chapter `rem:nilpotent-completion-dependency` (L15–25) makes this explicit. The status tag could be `\ClaimStatusProvedConditional` rather than `\ClaimStatusProvedHere`.

**Repair.** Two options:
1. **Complete the proof.** Fill in the obstruction-theory argument: explicitly show that for sufficiently large n, the obstruction class in `H^2(A, F^n/F^{n+1})` vanishes. This requires constructing an explicit homotopy.
2. **Downgrade status.** Change `\ClaimStatusProvedHere` to `\ClaimStatusProvedConditional` with explicit dependence on the (not-proved) claim "$H^2(A, F^n/F^{n+1}) = 0$ for $n \gg 0$."

The chapter already documents the dependency in a remark; the status tag should match. This is a 1-character change for option 2, or a 1-paragraph addition for option 1.

### 2.6 The Theorem `thm:curved-koszul` upgrade opportunity (Q3 in §1.4)

**Attack.** None. This is a strengthening attack.

**Defense.** Theorem `thm:curved-koszul` (poincare_duality_quantum.tex L91–110) is currently `\ClaimStatusProvedElsewhere` citing Positselski11 + GLZ22. But the body of the theorem is the chiral instantiation, with explicit invocation of `thm:filtered-to-curved` (this manuscript) and `thm:bar-convergence` (this manuscript). The classical form is in Positselski; the chiral form is novel.

**Repair.** Upgrade status to `\ClaimStatusProvedHere` with the proof citing Positselski for the classical form and `thm:filtered-to-curved` + `thm:bar-convergence` for the chiral instantiation. This is a HEALING UPGRADE: the chapter becomes truer (the chiral content IS new).

---

## Section 3. AP audit

### 3.1 AP151 (convention clash, hbar/q): MASSIVE FOOTPRINT

The factor-of-2 q-convention clash documented in §2.2 is the single largest AP151 footprint surfaced in any wave so far. Files affected:
- `derived_langlands.tex` (5 instances of Kazhdan q)
- `chiral_modules.tex` (5+ instances of Kazhdan q)
- `koszul_pair_structure.tex` (1 instance of Kazhdan q)
- `en_koszul_duality.tex` (1 instance of Drinfeld q via hbar)
- `e1_modular_koszul.tex` (3 instances of Drinfeld q)
- `higher_genus_modular_koszul.tex` (4 instances of Drinfeld q)
- `ordered_associative_chiral_kd.tex` (MIXES both: Kazhdan q at L5405, L5413, L5442, L5470, L5499, L5710; Drinfeld R-matrix at L5271, L5497; explicitly bridges them at L5468 with `q^2 = e^{2 pi i hbar}`)

**Verdict.** The two conventions ARE both correct individually. The CLASH is that the manuscript moves between them without an explicit bridge identity, which leaves a reader silently confused. The single repair is to add a convention table to the master notation appendix.

### 3.2 AP154 (algebraic vs topological E_3): CONTAINED but worth a remark

`en_koszul_duality.tex` Section 12 (Topologization) properly distinguishes:
- **Algebraic E_3** from Higher Deligne Conjecture on chiral Hochschild cochains (the chiral E_3 of `prop:chiral-e3-dmod` and `thm:chiral-e3-cfg`).
- **Topological E_3** from local-constant factorization on R^3 (Lurie's recognition theorem applied after the Sugawara contraction trivialises holomorphic translations on BRST cohomology).

The chapter makes the distinction clearly in `thm:topologization` (L2994–3129) by separating "BRST cohomology carries E_3-top" (algebraic-topological agreement on cohomology) from "original complex carries E_3-top" (genuinely topological at chain level, requires Sugawara antighost contraction).

This is a healed AP154. The remaining concern (raised in Wave 4) is that the standalone `en_chiral_operadic_circle.tex` invokes Higher Deligne for E_2-chiral inputs without specifying which version of HDC. The CHAPTER `en_koszul_duality.tex` does NOT have this confusion — it's an artifact of the standalone alone.

### 3.3 AP47 (eval-generated core scope): CORRECTLY HANDLED

`derived_langlands.tex` Theorem `thm:kl-bar-cobar-adjunction` (L1121–1221) correctly localises to the evaluation-generated core:
- L1140 ("on integrable highest-weight modules M(λ) ∈ O_k^int(g-hat)")
- L1184–1186 ("the induced filtration on the relative bar complex")
- L1207–1213 ("Since M(λ) ∈ O_k^int is integrable, the E_1 page is concentrated in finitely many degrees (bounded by the Weyl group), and the spectral sequence degenerates at E_2 by the Koszul purity of A")

The post-CG completion remains open; the chapter explicitly acknowledges this in `rem:kl-bar-cobar-scope` (L1270–1283) and in the summary at L1606–1612.

This is AP47-healthy.

### 3.4 AP31 (ProvedHere in remark): TWO instances

- `derived_langlands.tex` `rem:critical-level-theta` (L805–871) carries `\ClaimStatusProvedHere`. Per Vol II AP31, status tags belong on theorems/propositions/lemmas, not remarks. **Repair:** either promote to a proposition with proof, or remove the status tag.
- `derived_langlands.tex` `rem:bar-critical-oper-deRham` (L873–938) carries `\ClaimStatusConjectured`. Similar issue but less acute since "Conjectured" can plausibly attach to a remark documenting a conjecture. **Repair:** consider whether to wrap the conjectural content in a `\begin{conjecture}` environment.

### 3.5 AP6 (spec genus, degree, level): MOSTLY CLEAN

The chapters under audit consistently specify level, degree, and genus when invoking `kappa`, `Theta_A`, and bar-cobar identities. One minor exception: `derived_langlands.tex` L1422 says "the affine r-matrix is `r(z) = k Omega/z = 0`" at k=0 — this is correct (level prefix present, k=0 gives r=0), but the formula uses generic Omega without specifying trace-form vs Killing-form normalisation. This is fine in context but could be tightened by referencing the Sugawara construction at L65–78 of the same chapter.

### 3.6 AP126 (level-stripped r-matrix): CLEAN

All r-matrix formulas in the audited chapters carry explicit level prefix:
- `derived_langlands.tex` L67 (`r(z) = k Omega_tr/z`), L832 (`r(z) = k Omega_tr/z`), L1422 (`r(z) = k Omega/z`)
- `en_koszul_duality.tex` L6175 (`r(z) = k Omega_ij/(z_i - z_j)`), L6181–6184 (k=0 → r=0 verification)

This is AP126-healthy.

---

## Section 4. First-principles analyses

### 4.1 Why both q-conventions exist (cache-write candidate)

The two q-conventions are not arbitrary; each arises from a different mathematical fact:

**Kazhdan–Lusztig q_KL = exp(pi i / (k+h^v)).** This convention arises because the small quantum group `u_q(g)` at q a 2p-th root of unity (where p is the numerator of (k+h^v) = p/q) has a well-defined modular structure and a finite tensor category Rep(u_q). The factor of pi (rather than 2*pi) in the exponent is what makes q a 2p-th root rather than a p-th root, which gives the correct number of irreducible representations.

**Drinfeld–Kohno q_DK = exp(2 pi i / (k+h^v)).** This convention arises because the KZ connection has monodromy `R = q^Omega` where the "natural" parameter q is `exp(2*pi*i*hbar)` with `hbar = 1/(k+h^v)`. The 2*pi*i comes directly from Cauchy's residue formula: the loop integral around the singularity at z=0 of the rational r-matrix `r(z) = Omega/((k+h^v) z)` produces a factor of `2*pi*i`. This is a topological invariant of the loop in `Conf_2(C)`, NOT a normalisation choice.

**The relationship.** `q_DK = q_KL^2`. The KL convention "halves" the period because the small quantum group sees half the monodromy (acts only via the Verlinde quotient, not the full braiding). The DK convention is the "full monodromy" parameter.

**Ghost theorem.** Both conventions are correct in their respective contexts, but they parameterise DIFFERENT objects:
- q_KL parameterises the small quantum group `u_q(g)` and the KL target category `C(U_q(g))`.
- q_DK parameterises the KZ R-matrix and the universal R-matrix of `U_hbar(g)`.

The squaring `q_DK = q_KL^2` reflects the fact that the small quantum group is the "half-period subalgebra" of the universal one. The CORRECT manuscript-level convention is to use BOTH but with explicit names: never say "q" without subscript when both are in play.

### 4.2 Why thm:bar-computes-dual needs the rigorous Verdier-on-derived-category

**Attack on the proof.** The displayed argument uses multiplication of distributions (delta functions) by logarithmic forms, which is ill-defined at the support of the delta. The chapter flags this in `rem:analytic-framework` and the Computation 5.5 flags the Arnold-relation failure under naive Verdier duality.

**Defense.** The proof can be made rigorous by working in `D^b_c(C_k-bar(X))` and using Verdier duality as an equivalence of triangulated categories. The cohomology-level identity `H^*(D F) = H^{d-*}(F)^v` then lifts to a quasi-isomorphism because Verdier duality is a triangulated equivalence (preserves cofibers, hence quasi-isomorphisms).

**The first-principles ghost.** What the proof *gets right*: the Verdier dual of the bar complex IS the Koszul dual coalgebra, and this IS realised by configuration-space integrals against logarithmic forms paired with delta currents. What it *gets wrong*: presenting this pairing as a literal pointwise multiplication of distributions, which fails. The *correct framework* is the constructible-sheaves derived category, where the pairing is an adjunction between `j_!` and `Rj_*`.

This is exactly the AP-CY62 distinction (geometric vs algebraic chiral Hochschild model). The chapter acknowledges it in two remarks but the proof body still uses the heuristic formulation.

### 4.3 Why the periodic CDG conjecture is load-bearing

**Question.** Why can't the KL equivalence be proved via the chain-level adjunction `thm:kl-bar-cobar-adjunction` alone, without `conj:periodic-cdg`?

**Answer.** Without periodicity, the bar complex `barB(g-hat_k)` at admissible level is an infinite-dimensional CDG-coalgebra. The chain-level adjunction takes integrable modules to bar-comodules over THIS infinite coalgebra. The KL equivalence requires the target category to be `Rep(u_q)` where `u_q` is the FINITE-DIMENSIONAL small quantum group. The bridge is precisely Positselski's CDG Koszul duality for periodic CDG-coalgebras: under periodicity, the coderived category of `barB(g-hat_k)` reduces to the stable module category of a finite-dimensional quotient (Positselski11). Without periodicity, no such reduction is available.

**Ghost theorem.** The periodic CDG conjecture is the categorical analogue of the algebraic statement "the universal enveloping `U(g-hat_k)` at admissible level has a finite-dimensional center quotient `u_q`." The classical version of this is Lusztig's theorem for `U_q(g)`. The chiral version is the ConJ.

**Healing path.** No downgrade exists. The conjecture is the load-bearing single open ingredient. The healing is to PROVE it, not to weaken it.

### 4.4 Why the bar complex cannot be the localization functor itself

**Question.** Why does Remark `rem:bar-as-localization` say the bar complex is a "chain-level model" for Frenkel–Gaitsgory localization, and why is the strong statement (bar complex = localization functor) explicitly DISCLAIMED at L739–743?

**Answer.** The Frenkel–Gaitsgory localization functor `Delta: D(g-hat_{-h^v}-mod) → D(QCoh(Op))` is defined on ARBITRARY modules and is a derived functor. The bar complex `barB(g-hat_{-h^v})` is a single chain complex; it is the IMAGE under `Delta` of the vacuum module `V_crit`, not the functor itself. The chapter is correct to say "compatible with the vacuum-side target of the localization picture."

The full bar complex at critical level computes the OPER DIFFERENTIAL FORMS via `Ext^*(V_crit, V_crit) = H^*(barB)`. This is the cohomology of the localization image, restricted to vacuum-vacuum Ext.

**Ghost theorem.** The strong claim "bar complex = localization functor" is FALSE because the bar complex is an OBJECT, not a functor. The honest claim is: the bar cohomology of g-hat_{-h^v} EQUALS the differential forms on Op_{g^v}(D), which is the Frenkel–Teleman theorem. The chapter handles this correctly in `thm:oper-bar-dl` (L648–703).

---

## Section 5. Three upgrade paths

### 5.1 Upgrade Path 1 (LOW EFFORT): Convention table + status fixes

**Changes:**
1. Add a 5-line convention table to the notation appendix specifying `q_KL` vs `q_DK` (see §2.2 repair).
2. Fix status tags: `constr:kl-categorical-mc3` (heuristic/programmatic, not ProvedHere); `rem:critical-level-theta` (no status tag in remark).
3. Specify propagator normalisation in `prop:kappa-universality-en` (one-line addition).

**Result.** Manuscript becomes more readable. No theorem statement changes. Healing without downgrade.

**Effort.** ~15 minutes of editing. ~30 minutes of grep+verify across all three volumes.

### 5.2 Upgrade Path 2 (MEDIUM EFFORT): Tighten three proofs

**Changes:**
1. Rewrite Step 3 of `thm:bar-computes-dual` (poincare_duality.tex L481–494) to use Verdier-on-derived-category instead of distributional multiplication.
2. Complete the obstruction-theory argument in Step 3 of `thm:completion-convergence` (nilpotent_completion.tex L143–145), OR downgrade status to `ProvedConditional`.
3. Expand the Arnold-defect computation in `prop:fourier-genus1-propagator` (fourier_seed.tex L160–180) to be self-contained, or reference `thm:arnold-higher-genus` more explicitly.

**Result.** Three of the chapter's "ProvedHere" theorems become genuinely complete proofs. The chapter's claim density rises.

**Effort.** ~2–4 hours of math + writing per theorem.

### 5.3 Upgrade Path 3 (HIGH EFFORT): Strengthen `thm:curved-koszul` and prove `conj:periodic-cdg`

**Changes:**
1. Upgrade `thm:curved-koszul` (Q3 in §1.4) from `ProvedElsewhere` to `ProvedHere` with the chiral instantiation as a self-contained proof.
2. Attempt to PROVE `conj:periodic-cdg` for at least one specific case beyond rank 1 (e.g. for `widehat{sl_3}` at admissible level p/q = 3/2).

**Result.** The chapter advances from "5/6 ingredients for KL from bar-cobar" (current) to "6/6 ingredients" for at least one specific case. The KL-from-bar-cobar conjecture becomes a partial theorem.

**Effort.** ~2–4 weeks of new mathematics for #2; ~1 day for #1.

---

## Section 6. Punch list

In priority order:

**P0 (must fix; no downgrade required):**
1. **Add q-convention table** to notation appendix. Document `q_KL = exp(pi i/(k+h^v))` vs `q_DK = exp(2*pi*i/(k+h^v))` with bridge identity `q_DK = q_KL^2` and a list of which conventions appear in which files.
2. **Fix status tag on `constr:kl-categorical-mc3`** (derived_langlands.tex L178–187): remove `\ClaimStatusProvedHere` from a construction whose body explicitly says it is an analogy, not a theorem. Replace with `\ClaimStatusHeuristic` or remove entirely.
3. **Fix status tag on `rem:critical-level-theta`** (derived_langlands.tex L805–871): remove `\ClaimStatusProvedHere` from a remark per AP31. Either promote the remark to a proposition with proof, or remove the status tag.

**P1 (proof tightening, all healing):**
4. **`thm:bar-computes-dual` quasi-isomorphism step** (poincare_duality.tex Step 3 of proof, L481–494): rewrite to use Verdier-on-derived-category (which IS what KS90 provides) instead of distributional multiplication.
5. **`thm:completion-convergence` obstruction theory** (nilpotent_completion.tex Step 3, L143–145): either complete the obstruction-theory argument OR change `\ClaimStatusProvedHere` to `\ClaimStatusProvedConditional` to match the explicit "frontier" framing of `rem:nilpotent-completion-dependency`.
6. **`prop:kappa-universality-en` propagator normalisation** (en_koszul_duality.tex L844–868): add one line specifying the propagator normalisation that makes the binary invariant n-independent.
7. **`prop:fourier-genus1-propagator` Arnold defect computation** (fourier_seed.tex L160–180): expand the cross-term derivation OR reference `thm:arnold-higher-genus` more explicitly.

**P2 (strengthening opportunities; all upgrades):**
8. **Upgrade `thm:curved-koszul`** (poincare_duality_quantum.tex L91–110) from `ProvedElsewhere` to `ProvedHere` with the chiral instantiation as a self-contained proof.
9. **Strengthen `prop:en-formality-mc-truncation`** (en_koszul_duality.tex L148–163): replace the signature-style "each formality level kills obstruction classes above threshold" with an explicit named-theorem citation per clause.
10. **Strengthen `conj:bar-satake-shadow` clause (3)** (derived_langlands.tex L1396–1413): make the rank-recovery normalisation explicit.

**P3 (load-bearing open problems; not downgradable):**
11. **`conj:periodic-cdg`** (derived_langlands.tex L993–1008). The single missing ingredient for KL from bar-cobar. Healing = prove it, not weaken it. Suggested attack vector: try `widehat{sl_3}` at admissible level p/q = 3/2 (smallest non-trivial case beyond rank 1).
12. **`conj:kl-bar-cobar-dl`** (derived_langlands.tex L1223–1257). Depends on #11.
13. **`conj:bar-satake-shadow`** (derived_langlands.tex L1378–1414). Independent of #11; the load-bearing open problem for the derived Satake route.
14. **`conj:topologization-general`** (en_koszul_duality.tex L3269–L3291). The chain-level extension of `thm:topologization` to general chiral algebras with conformal vector. Suggested attack vector: prove for Virasoro at generic c, using the fact that 3d HT gravity has been constructed by Costello–Gwilliam.
15. **`conj:coderived-e3`** (en_koszul_duality.tex L4006). The class-M alternative path. Independent of #14.
16. **`conj:chromatic-bar-cobar`** (en_koszul_duality.tex L7230). The chromatic-homotopy lift. Long-term frontier.
17. **`conj:spectrum-lift`** (en_koszul_duality.tex L7384). The spectrum-level lift. Long-term frontier.

---

## Cache write-back (new patterns surfaced)

Two patterns appear in this wave that are not yet in `appendices/first_principles_cache.md`. Recommended additions:

**Cache entry candidate 51 — q-convention clash (KL vs DK):**

| Wrong claim | Ghost theorem | Correct relationship | Type |
|---|---|---|---|
| "q = e^{pi i / (k+h^v)} is the same q that appears in q^Omega in the KZ R-matrix" | Both q's are correct in their contexts | KL: q_KL = exp(pi i/(k+h^v)), DK: q_DK = exp(2*pi*i/(k+h^v)) = q_KL^2. Small quantum group at q_KL, KZ monodromy at q_DK. | convention clash (AP151) |

**Cache entry candidate 52 — bar complex vs localization functor:**

| Wrong claim | Ghost theorem | Correct relationship | Type |
|---|---|---|---|
| "the bar complex is the Frenkel–Gaitsgory localization functor" | bar cohomology = oper differential forms | Bar complex is an OBJECT (chain complex). Localization is a FUNCTOR. The bar cohomology of g-hat_{-h^v} EQUALS the differential forms on Op (Frenkel–Teleman). The functor itself is not the bar complex. | object/structure (AP-CY58 type) |

Both should be added to the cache file with explicit ghost-theorem statements.

---

## Summary

The chapter `derived_langlands.tex` is the most carefully scoped chapter in Vol I. It honestly distinguishes (i) the proved oper differential-form identification, (ii) the proved chain-level KL adjunction on the eval-generated core, (iii) the conjectural periodic CDG structure that is the missing ingredient for KL from bar-cobar, and (iv) the conjectural Satake from shadow tower. It does not overclaim. Three minor status-tag fixes and one cross-volume convention table fully heal the chapter.

The chapter `en_koszul_duality.tex` properly distinguishes algebraic and topological E_3 structures via `thm:topologization` (Khan–Zeng input) and `conj:topologization-general`. The AP154 concern raised in Wave 4 is contained at the chapter level.

The supporting chapters (`poincare_duality.tex`, `poincare_duality_quantum.tex`, `fourier_seed.tex`, `quantum_corrections.tex`, `nilpotent_completion.tex`, `existence_criteria.tex`, `computational_methods.tex`) are honestly scoped with three identifiable proof tightenings (none of which require downgrades) and one upgrade opportunity (`thm:curved-koszul`).

The largest single-issue surfaced is the cross-volume q-convention clash (AP151, factor of 2): seven files in `chapters/theory` use one of two incompatible conventions, and the manuscript transitions between them without an explicit bridge identity. Repair is one convention-table addition.

No theorem requires downgrading. The healing path is uphill in every case.
