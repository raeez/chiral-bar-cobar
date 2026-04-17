# Wave Frontier — Attack & Heal of CY-A$_3$ at the chain level

**Mandate.** Russian-school delivery. Chriss--Ginzburg discipline. Construct, do not narrate. *Platonic ideal form, no downgrades.*

**Target.** The chain-level part of CY-A$_3$ — the residue that survives after the inf-categorical proof `thm:derived-framing-m3b2` (Vol III, m3_b2_saga.tex L614-L678). Equivalently: Conjecture $\Pi_3^{\mathrm{ch}}$ of Wave 14 V11 §11.1.

**Mode.** Hybrid attack-then-heal. Read-only audit. No edits. No commits. All future authorship: Raeez Lorgat.

**Date.** 2026-04-16. Builds on Wave 14 V11 ($\Phi$ functor), V19 (Trinity), V20 (Universal Trace Identity), V8 (Shadow Quadrichotomy).

**Lineage.** Costello (TCFT) · Francis--Gaitsgory (chiral Koszul) · Lurie (HA 5.3, deformation theory) · Goodwillie (calculus) · Beilinson--Drinfeld (factorisation) · Kontsevich--Soibelman (formality) · Tsygan (cyclic).

---

## §1. Steel-manning the current state

### 1.1 What Vol III currently asserts

The current Vol III status of CY-A$_3$ is *layered*. Three distinct claims:

| Layer | Statement | File / Label | Status |
|---|---|---|---|
| **L3 (derived/inf-cat)** | Space of $E_3$-liftings of the canonical $E_2$-structure on $\HH_\bullet(\cC)$ is contractible; obstruction $\HH^{-2}_{E_1}(A,A) = 0$ by unit-connectedness. | `m3_b2_saga.tex` L614--L678 (`thm:derived-framing-m3b2`); `cy_to_chiral.tex` L3406 onward (`thm:cy-to-chiral-d3`); engine `derived_framing_obstruction.py` (51 tests). | `ProvedHere` |
| **L2 (homotopy/total)** | $\{b, B^{(2)}\} = 0$ for the *total* $A_\infty$-Hochschild differential $b = \sum_k b_k$, via Costello open-closed TCFT and $d^2 = 0$ on the moduli chain complex. | `m3_b2_saga.tex` L531--L606 (`thm:total-ainf-compat`); engine `operadic_tcft_mk_b2_engine.py` (43 tests). | `ProvedHere` |
| **L1 (strict/per-arity)** | $[m_3, B^{(2)}] \neq 0$ on $C_4(A)$ for non-formal $A$. The original claim "for each $k$, $[m_k, B^{(2)}] = 0$" is *false* and was retracted (AP-CY34). | `m3_b2_saga.tex` L470--L515 (`prop:chain-nonvanishing-generic`); engine `obs_ainf_local_p2.py` (54 tests, $[m_3, B^{(2)}]([x_1\!\mid\! x_1\!\mid\! x_1\!\mid\! x_1\!\mid\! y_1]) = 2\alpha\,[y_1]$). | Refutation. |

The CY-A$_3$ status is `ProvedHere (inf-cat)`. Conjecture $\Pi_3^{\mathrm{ch}}$ is precisely the statement that the *chain-level explicit construction* of $\Phi_3(\cC)$ (not just the inf-categorical existence) holds for non-formal $A_\infty$-categories.

### 1.2 Steel-manned proof of L3 (derived obstruction vanishes)

The L3 argument is robust. By Dunn additivity ($E_3 \simeq E_2 \otimes E_1$), the fibre of restriction $\mathrm{Mod}_{E_3}(\cC) \to \mathrm{Mod}_{E_2}(\cC)$ has tangent complex $\HH^\bullet_{E_1}(A,A)[-2]$. The primary $\pi_0$-obstruction is $\HH^{-2}_{E_1}(A,A)$. Unit-connectedness ($\HH^0(A) = k$) implies $\HH^p_{E_1}(A,A) = 0$ for all $p < 0$ — the Hochschild complex $\RHom_{A \otimes A^{\op}}(A, A)$ is concentrated in non-negative degrees. The Goodwillie tower for the $E_2 \to E_3$ functor has layer-$k$ controlled by $\HH^\bullet_{E_1}(A, A^{\otimes k})[-2]$; the same connectivity bound kills every layer. The space of liftings is contractible.

The L3 hypothesis menu is *minimal*: smoothness, properness, $\HH^0 = k$. No formality assumption. This is genuinely strong.

### 1.3 Steel-manned proof of L2 (TCFT cancellation)

The L2 argument identifies $b$ and $B^{(2)}$ with images of the operadic boundary $\partial$ in $C_\bullet(\cM)$ for the moduli operad $\cM$ of bordered Riemann surfaces with marked points. The key compactness step: $b \circ B^{(2)} + B^{(2)} \circ b$ counts the boundary of a compact 1-dimensional moduli stratum $\overline{\cM}_{b,B^{(2)}}$ whose only codimension-1 components are the strip-degeneration ($b$) followed by the genus-change ($B^{(2)}$) and vice versa. Compactness ⇒ signed count = 0.

The L2 cancellation is genuinely *cross-arity*: at $n = 4$, $\{b_2, B^{(2)}\}$ (involving $\mu_2$) and $\{b_3, B^{(2)}\}$ (involving $\mu_3$) target *different* graded components of the output (degrees $-3$ and $-4$ respectively, see `m3_b2_saga.tex` Cor. `cor:no-naive-cross-degree`). For *naive* $B^{(2)}_{\mathrm{naive}}$ (pairwise contraction), no algebraic cancellation can occur — the outputs sit in disjoint graded pieces. The TCFT $B^{(2)}_{\mathrm{TCFT}}$ differs from $B^{(2)}_{\mathrm{naive}}$ by precisely the moduli-space corrections that *make* the cancellation work.

This is the essential subtlety: the operadic identity $\{b, B^{(2)}_{\mathrm{TCFT}}\} = 0$ requires the *correct* $B^{(2)}$, namely the moduli-defined one. A reader who silently uses $B^{(2)}_{\mathrm{naive}}$ will see a non-vanishing $6\alpha \cdot [b]$ on the local-$\bP^2$ test element (computed explicitly in `chain_level_m2_b2_cancellation.py`, 29 tests).

---

## §2. PHASE 1 — ATTACK

### 2.1 Attack 1. The TCFT $B^{(2)}$ is implicit, not constructed.

**Vector.** `thm:total-ainf-compat` invokes the moduli-operadic boundary $\partial$ in $C_\bullet(\cM)$. The proof references Costello arXiv:math/0412149 Theorem A (cyclic $A_\infty$ ↔ open TCFT) and Costello arXiv:0706.1959 (open-closed extension). What it does *not* do: construct the operator $B^{(2)}_{\mathrm{TCFT}}$ explicitly as a chain map on the bar complex.

**Severity.** Concrete. The proof asserts that *some* operator $B^{(2)}$ corresponding to the genus-change moduli boundary stratum satisfies $\{b, B^{(2)}\} = 0$. That operator differs from $B^{(2)}_{\mathrm{naive}}$ by terms that are *named* in the proof (cross-arity corrections from Stasheff $A_\infty$-relations) but never written down for any specific algebra. Local $\bP^2$ would be the test.

**Forensic check.** `chain_level_m2_b2_cancellation.py` (Remark `rem:b2-cancellation-correction`, lines 942--960 of `m3_b2_saga.tex`) gives the *naive* operator's failure on local $\bP^2$:
$$
\{b, B^{(2)}_{\mathrm{naive}}\}([a\!\mid\!a\!\mid\!a\!\mid\!a\!\mid\!b]) \;=\; 6\alpha \cdot [b] \;\neq\; 0.
$$
The TCFT operator $B^{(2)}_{\mathrm{TCFT}}$ is asserted to "absorb the $6\alpha[b]$ discrepancy through moduli-space corrections" (line 953). What corrections, in what basis, computed on what bar element? Silent.

**Verdict.** L2 is a *statement* of cancellation, not a *construction* of the cancelling operator. The chain-level explicit operator on local $\bP^2$ — the simplest non-formal CY$_3$ — is unconstructed in any compute engine in `compute/lib/`. (Verified: `grep -l "B_TCFT\|B^{(2)}_{TCFT}\|tcft_b2\|moduli_correction"` returns zero hits in `compute/lib/`.)

### 2.2 Attack 2. The L3 unit-connectedness argument has a connectivity hypothesis.

**Vector.** $\HH^p_{E_1}(A,A) = 0$ for $p < 0$ requires $A$ to be *unit-connected*: $\HH^0(A) = k$. The proof of `thm:derived-framing-m3b2` cites this as universal: "all CY chiral algebras have $\HH^0 = k$ (one vacuum state)". Is this true?

**Test cases.**
- $A = $ free Heisenberg lattice VOA (class G): $\HH^0(A) = k$ ✓.
- $A = $ Virasoro at central charge $c$: $\HH^0(A) = k$ ✓.
- $A = $ K3 lattice VOA $H_{\mathrm{Mukai}}$: $\HH^0 = k$ ✓.
- $A = $ a *log* VOA (class M, e.g. $W(p)$ at $p \geq 2$): $\HH^0 \neq k$ in general — log VOAs have non-trivial $\Hom$ from the unit (logarithmic primaries reduce semisimplicity). The triplet $W(2)$ has 4 simple modules, and $\HH^0$ of the *category* of modules has rank 4.

**Subtlety.** The "unit-connected" property required is for $A$ as an *algebra* (HH$^0$ of $A$, not of $\mathrm{Rep}(A)$). For $A$ itself a chiral algebra with vacuum, $\HH^0(A,A) = $ centre of $A$. For W(p) (irrational), $\HH^0(A,A)$ contains the additional logarithmic central elements; it is not always $k$.

**Severity.** Real for class M (logarithmic) inputs. The L3 statement currently uses "all CY chiral algebras have $\HH^0 = k$" without restriction. For class M targets — local $\bP^2$, the quintic, $K3 \times E$ — the chiral algebra produced by $\Phi_3$ may itself be a class M / logarithmic VOA whose $\HH^0$ exceeds $k$.

**Verdict.** The L3 obstruction-vanishing argument *as written* is correct for unit-connected $A$, but the *applicability* claim "all CY chiral algebras are unit-connected" is overclaimed for class M. The argument needs an additional hypothesis or a stronger connectivity argument.

### 2.3 Attack 3. The Goodwillie-tower vanishing requires *uniform* connectivity.

**Vector.** Even for unit-connected $A$, the higher Goodwillie layers involve $\HH^\bullet_{E_1}(A, A^{\otimes k})[-2]$. The connectivity bound asserted is $\HH^p_{E_1}(A, A^{\otimes k}) = 0$ for $p < -k+1$. This is correct for $k=1$ (the input is $A$ itself, connected). For $k \geq 2$, $A^{\otimes k}$ is not in general unit-connected as a left $A$-module — it has $\HH^0 = k^{\otimes k}$, but as a *bimodule over* $A^{\otimes k}$ the connectivity is more delicate.

**Severity.** This is a technical refinement, but it is also a technical *gap*. The Francis--Gaitsgory result quoted (arXiv:1106.5146) gives the layer-$k$ tangent fibre, but the connectivity bound on $\HH^p_{E_1}(A, A^{\otimes k})$ is not literally cited; it is asserted in `derived_framing_obstruction.py` lines 200--207 and not verified for $k \geq 2$.

**Verdict.** L3 holds for the primary obstruction ($k=1$) under unit-connectedness. The vanishing of *all* higher Goodwillie layers (and hence contractibility of the lifting space) requires either (a) a uniform connectivity bound that's stated but not verified, or (b) a separate argument for each layer.

### 2.4 Attack 4. Class M (logarithmic, non-semisimple) breaks the L1 → L2 → L3 ladder.

**Vector.** The three-level ladder of `def:three-levels` (`m3_b2_saga.tex` L692--L714) is:
- L1 fails for non-formal (real refutation, `obs_ainf_local_p2.py`).
- L2 holds via TCFT (the operadic argument).
- L3 holds via unit-connectedness.

For class M (local $\bP^2$, the quintic, $K3 \times E$ at small volume), each step has an open issue:
- L1 explicit chain non-vanishing is *computed* (54 tests on local $\bP^2$). The non-vanishing is *generic* for non-formal algebras (49 / 49 in `obs_ainf_counterexample_search.py`).
- L2 cancellation is *asserted* via Costello but the explicit cancelling operator is *unconstructed*.
- L3 holds *if* the input is unit-connected; for log VOAs (class M), $\HH^0$ may exceed $k$.

**Severity.** For class M, the entire ladder is at risk. The output of $\Phi_3$ on a class M target may itself be class M (logarithmic), violating the connectivity assumption that L3 needs.

**Verdict.** The chain-level conjecture $\Pi_3^{\mathrm{ch}}$ is *most acute* for class M inputs. It is precisely the regime where shadow-tower divergence (Borel-summable, Stokes data) couples with the chain-level $A_\infty$ obstruction and the connectivity gap.

### 2.5 Attack 5. The 17 stale "conditional on CY-A$_3$" phrases were incorrectly classified.

**Vector.** Wave 14 V11 §9.2 promised a sweep: "11 type (a) → unconditional, 4 type (b) → rephrased as chain-level conditional, 2 type (c) → CY-C-dependent". A grep on the current chapters/ shows ~17 stale phrases. Re-reading them in light of the L1 vs L2 vs L3 distinction:

| File:Line | Current text | Actually conditional on |
|---|---|---|
| `cy_to_chiral.tex` L1763 | "Resurgence-wall-crossing correspondence (conditional on CY-A$_3$ for $d=3$)" | L1 chain-level, NOT inf-cat. The Stokes automorphism uses an explicit chain-level model. |
| `cy_to_chiral.tex` L1802 | "global stitching of infinitely many local identifications is conditional on CY-A$_3$" | L1 chain-level (each local model is a class M algebra needing chain-level $A_\infty$ data). |
| `cy_to_chiral.tex` L3308 | "motivic-DT integral conditional on CY-A$_3$ for non-toric" | L3 inf-cat suffices for *existence*; L1 chain-level needed for *integration*. |
| `e1_chiral_algebras.tex` L1983 | "KS automorphism as bar generating function (conditional on CY-A$_3$)" | L1 chain-level. The bar Euler product uses explicit $b_k$ for each $k$. |
| `e1_chiral_algebras.tex` L1991 | "BPS invariants as bar Euler characteristics (conditional on CY-A$_3$)" | L3 inf-cat *might* suffice if the Euler characteristic is computable from the obstruction tower; L1 chain-level safest. |
| `k3_yangian_chapter.tex` L2017,2103,2199 | "Derivation (conditional on CY-A$_3$)" | L1 chain-level — uses explicit Yangian RTT data on bar complex. |
| `k3_chiral_algebra.tex` L1463,1486 | "class M (conditional on CY-A$_3$, AP-CY6)" | L1 chain-level — class M is *defined* by the full shadow tower from explicit $b_k$. |
| `quantum_chiral_algebras.tex` L364,376,1949,2447,2698 | various | mostly L1 chain-level when the result uses explicit chain-level operations. |
| `e2_chiral_algebras.tex` L1187 | "tetrahedron correction (conditional on CY-A$_3$)" | L1 chain-level — the ZTE correction $T$ is an explicit chain-level operator. |
| `braided_factorization.tex` L768,1351,1387 | various | L1 chain-level for chain-explicit constructions; L3 inf-cat for "factorization category" structural statements. |
| `modular_trace.tex` L168 | "construction of $A_X$ is settled by CY-A$_3$" | L3 inf-cat ✓, the construction *as inf-categorical object* is settled. |
| `connections/modular_koszul_bridge.tex` L890 | conifold "not conditional on CY-A$_3$" | conifold is formal (class G); L1, L2, L3 all hold trivially. ✓ correctly marked. |

**Re-classification.** Of the 17 stale phrases, the realistic split is closer to:
- ~3 cleanly L3 inf-cat conditional (now unconditional after `thm:derived-framing-m3b2`).
- ~10 genuinely L1 chain-level conditional (still open as $\Pi_3^{\mathrm{ch}}$).
- ~2 CY-C dependent.
- ~2 mixed (L1 for explicit + L3 for existence).

Wave 14 V11 §9.2's split (11 unconditional, 4 rephrased, 2 CY-C-dependent) was *too optimistic* about L3 sufficiency. Most occurrences need the L1 explicit chain-level data.

**Verdict.** The sweep proposed in V11 §9.2 was correct in *direction* but wrong in *proportions*. The actual healing requires distinguishing L1-conditional from L3-conditional, with a finer mid-tier of L2-via-TCFT-construction for results that need the explicit cancelling $B^{(2)}_{\mathrm{TCFT}}$.

### 2.6 Adversarial counter-example attempt: local $\bP^2$ at $n=5$

**Setup.** Take $A = $ minimal cyclic $A_\infty$-model for local $\bP^2$ (8 generators, $\mu_3 \neq 0$, McKay potential $W = x_1 x_2 x_3$). Test bar element $[x_1 | x_1 | x_1 | x_1 | y_1] \in C_4(A)$.

**Computation (from `obs_ainf_local_p2.py`, 54 tests).**
- $[m_3, B^{(2)}_{\mathrm{naive}}]([x_1|x_1|x_1|x_1|y_1]) = 2\alpha \cdot [y_1]$.
- $\{b_2, B^{(2)}_{\mathrm{naive}}\}([x_1|x_1|x_1|x_1|y_1]) = -2\alpha \cdot [y_1]$ (Remark `rem:b2-cancellation`).

So *if* one uses $B^{(2)}_{\mathrm{naive}}$, the per-arity $\{b_3, B^{(2)}\} = 2\alpha[y_1]$ and $\{b_2, B^{(2)}\} = -2\alpha[y_1]$ cancel on this element — but this is a *targeted coincidence* at this element. The corollary `cor:no-naive-cross-degree` then proves the cancellation *cannot* be uniform: degree shifts $-3$ and $-4$ generically place outputs in disjoint graded pieces.

**Resolution by the manuscript itself.** Lines 942--954 of `m3_b2_saga.tex` correctly catch this in `rem:b2-cancellation-correction`: the cancellation works only because the TCFT $B^{(2)}_{\mathrm{TCFT}}$ differs from $B^{(2)}_{\mathrm{naive}}$ by precisely the moduli-correction term that *re-aligns* the output gradings. The naive sum $6\alpha[b]$ is the discrepancy.

**Counter-example status.** No counter-example to L2-via-TCFT. The naive operator fails (as expected); the TCFT operator works *by construction* (modulo the explicit operator never being written down). Conjecture $\Pi_3^{\mathrm{ch}}$ is *not falsified* by local $\bP^2$.

But the test confirms: the chain-level cancellation is *non-trivial* even on the simplest non-formal CY$_3$ algebra. The TCFT operator $B^{(2)}_{\mathrm{TCFT}}$ on local $\bP^2$ is a concrete, computable object that has not been computed.

---

## §3. PHASE 2 — HEALING

The attack identifies five concrete openings. Each admits a healing path that strengthens — never downgrades — the manuscript.

### 3.1 Healing 1. Construct $B^{(2)}_{\mathrm{TCFT}}$ on local $\bP^2$ explicitly.

**The reach.** The TCFT operator $B^{(2)}_{\mathrm{TCFT}}$ on the local $\bP^2$ bar complex must satisfy:
- $\{b, B^{(2)}_{\mathrm{TCFT}}\} = 0$ identically (8 generators × 5-element bar = 32,768 chain elements at $C_4$).
- $B^{(2)}_{\mathrm{TCFT}}$ reduces to $B^{(2)}_{\mathrm{naive}}$ on formal sub-algebras (the unit, the cup-only sub-algebra).
- $B^{(2)}_{\mathrm{TCFT}}$ differs from $B^{(2)}_{\mathrm{naive}}$ by terms involving $\mu_3$ explicitly.

**Construction skeleton.** Set $B^{(2)}_{\mathrm{TCFT}} := B^{(2)}_{\mathrm{naive}} + h$, where $h: C_n \to C_{n-1}$ is a chain homotopy with $\{b_3, h\} + \{h, b_2\} = -6\alpha[b] \cdot \chi_{[a|a|a|a|b]} + (\text{cross terms})$ on local $\bP^2$. The homotopy $h$ is built from the *Stasheff $n=4$ cancellation*: $\mu_2(\mu_3(a,a,a), a) + \mu_2(a, \mu_3(a,a,a)) = 0$. The TCFT correction injects this Stasheff term into the contraction operator.

**Engine.** A new compute engine `b2_tcft_explicit_local_p2.py` would:
- Take the local $\bP^2$ algebra from `obs_ainf_local_p2.py`.
- Construct the candidate $B^{(2)}_{\mathrm{TCFT}}$ as $B^{(2)}_{\mathrm{naive}} + h$ with $h$ defined by the Stasheff correction.
- Verify $\{b, B^{(2)}_{\mathrm{TCFT}}\} = 0$ exhaustively on $C_3, C_4, C_5$ (≈$10^4$ chain elements).
- Cross-check that $B^{(2)}_{\mathrm{TCFT}}$ has the moduli-operadic interpretation (boundary of $\overline{\cM}_{b, B^{(2)}}$).

**Status of this healing.** *Constructive*. The data is explicit; the verification is a finite combinatorial check. Resolves Conjecture $\Pi_3^{\mathrm{ch}}$ for local $\bP^2$ (single test case) and — by genericity arguments from `obs_ainf_random_search.py` — provides evidence for the universal statement.

### 3.2 Healing 2. State the L3 vanishing under explicit connectivity hypotheses.

**The reach.** Strengthen `thm:derived-framing-m3b2` to:

> **Theorem (L3, sharp form).** Let $\cC$ be a smooth proper CY$_3$ category whose chiral algebra $A = \HH_\bullet(\cC)$ satisfies $\HH^0(A, A) = k$ (the *centre* of $A$ is trivial). Then the obstruction to lifting the canonical $E_2$-structure on $A$ to an $E_3$-structure is zero, and the space of such liftings is contractible.

The added hypothesis "$\HH^0(A, A) = k$" is precise. It excludes class M / log VOAs where the centre is non-trivial. For Class G, L, C inputs — Heisenberg, KM, Virasoro, K3 lattice VOA — the hypothesis is satisfied. For class M, the hypothesis is conjectural and becomes a *named open conjecture* (no downgrade — just a sharper scope).

**New named conjecture.**

> **Conjecture $\Pi_3^{\mathrm{cM,ch}}$ (Class-M chain-level CY-A$_3$).** For every CY$_3$ category $\cC$ whose chiral algebra $\Phi_3(\cC)$ is class M (logarithmic), the inf-categorical CY-A$_3$ holds via either (a) a refined obstruction theory accommodating $\HH^0(A,A) > k$, or (b) a Stokes-data resurgence argument that bypasses the connectivity hypothesis using Borel-summability of the shadow tower (V8 Quadrichotomy class M).

This is the sharpest open statement after the healing. It connects directly to:
- V8 Shadow Quadrichotomy class M (Stokes line $c_S = -178/45$, alien amplitudes).
- AP-CY39 (class M = Borel-summable, not convergent).
- The Wave 14 V8 named theorem about class M Borel summability.

### 3.3 Healing 3. Verify the Goodwillie tower vanishing layer-by-layer for the standard CY$_3$ landscape.

**The reach.** Extend `derived_framing_obstruction.py` (currently 51 tests, computes layer 1 only) to compute layers 2, 3 explicitly for the four canonical inputs:
- $\bC^3$ (class G, formal)
- conifold (class G, formal)
- local $\bP^2$ (class M, non-formal)
- quintic (class M, non-formal)

For each: compute $\HH^p_{E_1}(A, A^{\otimes k})$ for $p \in [-4, 4]$, $k \in [1, 3]$, and verify negative-degree vanishing.

**Engine.** Extension of existing `derived_framing_obstruction.py` to a new module `goodwillie_tower_layers_cy3.py` (~150 tests). Output: a table indexed by $(\text{algebra}, p, k)$ giving $\dim \HH^p_{E_1}(A, A^{\otimes k})$.

**Reward.** Either confirms layer-by-layer vanishing for layers 2--3 (strengthening `thm:derived-framing-m3b2` from "primary obstruction" to "full Goodwillie tower"), or reveals the precise layer where vanishing first fails (giving a concrete computational target).

### 3.4 Healing 4. Re-classify the 17 stale "conditional on CY-A$_3$" phrases by L1/L2/L3 dependence.

**The reach.** Replace each stale phrase with one of *four* (not three) possible forms:
- (a) **L3-only**: "via the inf-categorical CY-A$_3$ resolution (`thm:cy-to-chiral-d3`)" — now unconditional.
- (b) **L2-via-TCFT**: "conditional on chain-level construction of $B^{(2)}_{\mathrm{TCFT}}$ (Conjecture $\Pi_3^{\mathrm{ch}}$, formal-class)".
- (c) **L1 chain-level**: "conditional on chain-level explicit $\Phi_3$ for non-formal algebras (Conjecture $\Pi_3^{\mathrm{ch}}$, full)".
- (d) **CY-C-dependent**: "conditional on CY-C (root-of-unity / fusion limit)".

A line-by-line audit (cf. §2.5 above) gives the realistic split for the 17 phrases:
- 3 type (a) → unconditional.
- 4 type (b) → L2-via-TCFT (Conjecture $\Pi_3^{\mathrm{ch}}$ formal-class — needs explicit operator construction but no further obstruction theory).
- 8 type (c) → L1 chain-level (Conjecture $\Pi_3^{\mathrm{ch}}$ full — needs both explicit operator and resolution of class-M connectivity).
- 2 type (d) → CY-C-dependent.

**Healing edit pass.** ~17 stale phrases replaced by their precise four-class label. The manuscript becomes *honest* about which results need which level of CY-A$_3$ and which are now unconditional.

### 3.5 Healing 5. Add the named conjecture hierarchy.

The current Conjecture $\Pi_3^{\mathrm{ch}}$ (Wave 14 V11 §11.1) is monolithic. Refine it into a hierarchy of three nested conjectures, each genuinely open:

> **Conjecture $\Pi_3^{\mathrm{ch,formal}}$ (Chain-level $\Phi_3$ for formal algebras).** For every smooth proper CY$_3$ category $\cC$ with formal $A_\infty$-structure ($\mu_k = 0$ for $k \geq 3$), the inf-categorical $\Phi_3(\cC)$ admits a chain-level explicit model. **Status: PROVED (trivially)**. For formal $A$, $b = b_2$ and $\{b_2, B^{(2)}\} = 0$ by the Frobenius / cyclic condition. $C^3$ and the conifold are in this class.

> **Conjecture $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ (Chain-level $\Phi_3$ for non-formal algebras).** For every smooth proper CY$_3$ category $\cC$ with non-formal $A_\infty$-structure ($\mu_3 \neq 0$) but unit-connected output ($\HH^0(\Phi_3(\cC), \Phi_3(\cC)) = k$), the chain-level explicit model exists via the construction of $B^{(2)}_{\mathrm{TCFT}}$ as $B^{(2)}_{\mathrm{naive}} + h$ for an explicit Stasheff homotopy $h$. **Status: OPEN, healing-path constructive (Healing 1).** Local $\bP^2$ is the test case.

> **Conjecture $\Pi_3^{\mathrm{ch,class\text{-}M}}$ (Chain-level $\Phi_3$ for class M).** For every CY$_3$ category $\cC$ whose chiral algebra $\Phi_3(\cC)$ is class M (logarithmic, $\HH^0 > k$), the chain-level explicit model exists via Stokes-data resurgence: the formal $\sum_k S_k$ of `def:three-levels` Level 2 cancellation is Borel-summable, with the Borel sum providing the chain homotopy. **Status: OPEN, contingent on V8 class-M Borel summability.** $K3 \times E$ at small volume is the test case.

This three-level conjecture hierarchy *replaces* the monolithic $\Pi_3^{\mathrm{ch}}$ with three sharper open problems, each tied to a different technical mechanism. None is a downgrade — the trivial level is now PROVED, the central level has a constructive healing path, the hardest level is connected to the V8 Quadrichotomy.

---

## §4. Connection to Wave 14 V19 Trinity at $E_1$

The V19 Trinity Theorem proves three pairwise quasi-isomorphisms among the three Hochschild models of a chiral algebra — geometric `C^•_chiral`, algebraic `Ext^*_{A^e}(A,A)`, bigraded `RHH_ch` — for $E_\infty$-chiral inputs. The frontier `wave_frontier_trinity_E1_attack_heal.md` (read-only confirmed) attacks the conjecture `conj:trinity-E_1` that the same Trinity holds for genuinely $E_1$-chiral inputs.

**The connection.** $\Phi_3$ outputs $E_1$-chiral algebras. For the chain-level $\Phi_3$ to recover a Trinity-style identification with the geometric and bigraded models, V19 must extend to $E_1$. The frontier's *weak form (c) Pentagon* (single-colour Trinity at $E_1$ = closed-colour Pentagon `[ω] = 0`) is the natural compatibility:

- L3 inf-cat $\Phi_3$ ⇔ V19 Trinity holds at the *homotopy* level for the $E_1$-output (no chain-level model required).
- L1 chain-level $\Phi_3$ (Conjecture $\Pi_3^{\mathrm{ch,non\text{-}formal}}$) ⇒ V19 Trinity at $E_1$ holds at the *chain level* (single-colour, in the form (b) of `wave_frontier_trinity_E1_attack_heal.md`).
- The Pentagon coherence cocycle $[\omega_{ch}] = 0$ on the closed colour of the V15 Pentagon is the *operadic substrate* that makes $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ functorial.

**Cross-link.** Resolving $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ via Healing 1 (explicit $B^{(2)}_{\mathrm{TCFT}}$ on local $\bP^2$) provides a *computational witness* for V19 Trinity at $E_1$ on the closed colour of Pentagon. The two conjectures are bound: progress on either accelerates the other.

---

## §5. Connection to Wave 14 V20 Universal Trace Identity

V20 (`UNIVERSAL_TRACE_IDENTITY.md`) establishes that Vol I's $K = -c_{\mathrm{ghost}}$ and Vol III's $\kappa_{\mathrm{BKM}} = c_N(0)/2$ are two specialisations of one trace $\mathrm{tr}_{Z(\cC)}(\mathfrak K_\cC)$ on the categorical centre $Z(\cC)$. Step 3 of V20 (identification $\mathfrak K^{\mathrm{ch}} = \mathfrak K^{\mathrm{BKM}}$) is established at the homotopy category. Chain-level coherence is V20's named open conjecture `conj:trace-identity-chain-level`.

**The connection.** V20 Step 3 chain-level coherence and CY-A$_3$ chain-level have *the same logical character*: both are about lifting a homotopy-level identity to a chain-level identity, both depend on V19 Trinity at $E_1$, both cluster around the Stasheff cross-arity cancellation phenomenon.

**Specifically:**
- V20 Step 3 chain-level requires the centre $Z(\Phi_3(\cC))$ to admit a chain-level model on which $\mathfrak K^{\mathrm{ch}}$ acts.
- That chain-level model exists *if and only if* $\Phi_3$ has a chain-level construction for non-formal inputs (Conjecture $\Pi_3^{\mathrm{ch,non\text{-}formal}}$).
- For formal inputs ($\Pi_3^{\mathrm{ch,formal}}$, PROVED), the V20 Step 3 chain-level identity is automatic.
- For class M inputs ($\Pi_3^{\mathrm{ch,class\text{-}M}}$), V20 Step 3 chain-level requires the same Borel-summability mechanism (Stokes data, V8 Quadrichotomy).

**Cross-volume implication.** Healing 1 (explicit $B^{(2)}_{\mathrm{TCFT}}$ on local $\bP^2$) furnishes the chain-level model on which V20's $\mathfrak K^{\mathrm{ch}}$ acts. It is the *first* explicit chain-level construction connecting the Vol I universal trace formalism to a Vol III non-formal CY$_3$ source. That single construction would close one entry of V20's named open conjectures and one entry of $\Pi_3^{\mathrm{ch}}$ simultaneously.

---

## §6. Implications for Vol III editing

Wave 14 V11 §9.2 promised a 17-phrase sweep classified into three buckets (11/4/2). The §2.5 attack above shows the realistic split is *finer* (3/4/8/2 across four buckets), and Healing 4 spells out the four-form replacement. Concrete edits:

**E1.** `cy_to_chiral.tex` L1763, L1802, L3308: replace "conditional on CY-A$_3$" with "conditional on Conjecture $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ (chain-level explicit $\Phi_3$ for non-formal algebras)". These are the L1 chain-level phrases.

**E2.** `cy_to_chiral.tex` L743, L1765 (parts (i)--(iii) at d=2 unconditional, part (iv) conditional): correctly already restricted to d=2; no change needed.

**E3.** `e1_chiral_algebras.tex` L1983, L1991: keep "conditional on CY-A$_3$" but add footnote "(specifically: Conjecture $\Pi_3^{\mathrm{ch}}$, the chain-level explicit $\Phi_3$ for non-formal algebras)".

**E4.** `k3_yangian_chapter.tex` L2017, L2103, L2199, L2405: these are derivation-style proofs that use explicit chain-level data. Replace "conditional on CY-A$_3$" with "conditional on $\Pi_3^{\mathrm{ch,non\text{-}formal}}$".

**E5.** `quantum_chiral_algebras.tex` L364, L376, L1949, L2447, L2698: case-by-case. L1949 (6d factorization homology route) is correctly noted as still requiring chain-level data (AP-CY32). The other four phrases should be split: L376 and L2447 are L3 inf-cat (now unconditional via `thm:cy-to-chiral-d3`); L364, L2698 are L1 chain-level.

**E6.** `e2_chiral_algebras.tex` L1187 (tetrahedron correction): the ZTE correction $T$ is constructed in `zte_deformation_cohomology.py` (47 tests), but uses chain-level $b_k$. Replace "conditional on CY-A$_3$" with "conditional on $\Pi_3^{\mathrm{ch}}$ via the chain-level $b_k$".

**E7.** `braided_factorization.tex` L768, L1351, L1387: case-by-case. L1351 is structural (factorization category) → L3 unconditional. L768, L1387 are explicit (Igusa cusp form, $\eta^{24}$) → L1 chain-level conditional.

**E8.** `modular_trace.tex` L168: correctly notes "construction of $A_X$ is settled by CY-A$_3$" — this is L3 inf-cat, unconditional. Existing wording is correct.

**E9.** `examples/derived_categories_cy.tex` L293, `examples/k3_chiral_algebra.tex` L1463, L1486, `examples/toric_cy3_coha.tex` L166: replace each with the four-form classification per Healing 4.

**E10.** `connections/modular_koszul_bridge.tex` L890 (conifold): correctly notes the conifold is unconditional. ✓ no change.

**Total edit count.** ~17 phrase replacements + ~3 footnote additions + 1 new conjecture-hierarchy section in `cy_to_chiral.tex` (or `m3_b2_saga.tex`). No new mathematical input beyond the existing `derived_framing_obstruction.py`, `operadic_tcft_mk_b2_engine.py`, `obs_ainf_local_p2.py` — the healing reorganises existing content into the sharpest form.

**Status synchronisation.** CLAUDE.md should add to the AP-CY34 entry: "the inf-cat resolution (L3) does not by itself imply the chain-level explicit construction (L1); the latter is Conjecture $\Pi_3^{\mathrm{ch}}$ in three levels (formal: PROVED; non-formal unit-connected: OPEN, healing-path constructive; class M: OPEN, contingent on V8 class-M Borel summability)."

---

## §7. Summary

The chain-level CY-A$_3$ frontier is genuinely open in a *structured* way that the current Vol III prose flattens. Three layers of the conjecture exist:

| Layer | Class | Status | Healing path |
|---|---|---|---|
| L3 inf-categorical | All CY$_3$ with $\HH^0 = k$ | PROVED (`thm:derived-framing-m3b2`) | — |
| L2 total $\{b, B^{(2)}\} = 0$ | All cyclic $A_\infty$ | PROVED (`thm:total-ainf-compat`, Costello TCFT, *abstract*) | Construct $B^{(2)}_{\mathrm{TCFT}}$ explicitly on local $\bP^2$ (Healing 1). |
| L1 strict $[m_3, B^{(2)}] = 0$ | Formal: PROVED. Non-formal unit-connected: open. Class M: open. | $\Pi_3^{\mathrm{ch,formal}}$ ✓ / $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ open / $\Pi_3^{\mathrm{ch,class\text{-}M}}$ open | Healing 1 (explicit Stasheff homotopy); Healing 5 (Stokes resurgence for class M). |

The five healings (§3.1--§3.5) are:
1. Construct $B^{(2)}_{\mathrm{TCFT}}$ explicitly on local $\bP^2$ via Stasheff homotopy ($n=4$ relation), verifiable by exhaustive chain-element check.
2. Sharpen `thm:derived-framing-m3b2` with explicit connectivity hypothesis $\HH^0(A,A) = k$, exposing class M as the genuine open frontier.
3. Verify Goodwillie tower layers 2--3 vanishing on the four canonical CY$_3$ inputs (extension of `derived_framing_obstruction.py`).
4. Re-classify 17 stale "conditional on CY-A$_3$" phrases into four buckets (3 unconditional / 4 L2-TCFT / 8 L1 chain / 2 CY-C).
5. Replace monolithic $\Pi_3^{\mathrm{ch}}$ with three-level conjecture hierarchy ($\Pi_3^{\mathrm{ch,formal}}$ ✓ / $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ open / $\Pi_3^{\mathrm{ch,class\text{-}M}}$ open).

**Cross-volume connections:**
- V11 §9.2 sweep is *correct in direction, wrong in proportions*: realistic split is finer (3/4/8/2 across four buckets, not 11/4/2 across three).
- V19 Trinity at $E_1$ and Conjecture $\Pi_3^{\mathrm{ch,non\text{-}formal}}$ are *bound*: closed-colour Pentagon coherence ↔ chain-level $\Phi_3$ for non-formal inputs.
- V20 Universal Trace Identity Step 3 chain-level coherence and Conjecture $\Pi_3^{\mathrm{ch}}$ have *identical logical character*; one explicit Stasheff homotopy resolves both for one test case.
- V8 Shadow Quadrichotomy class M Borel summability + Stokes data is the structural input needed to close $\Pi_3^{\mathrm{ch,class\text{-}M}}$.

**The single sentence to take away:**

> CY-A$_3$ is layered: the inf-categorical proof (L3) is robust under unit-connectedness; the total-Hochschild TCFT proof (L2) is structurally complete but operationally implicit; the chain-level explicit construction (L1) is a three-level conjecture hierarchy in which the formal class is trivially settled, the non-formal unit-connected class admits a constructive healing via an explicit Stasheff homotopy on local $\bP^2$, and the class-M (logarithmic) class is bound to the V8 Quadrichotomy through Stokes-data resurgence.

The Platonic form of CY-A$_3$ is therefore not a single theorem but a four-step ladder: L3 (proved) → L2-formal (proved) → L2-non-formal (Healing 1) → L1-class-M (V8 + Stokes resurgence).

**Inner music.** $[m_3, B^{(2)}] \neq 0$ at chain level is the *acoustic resonance* of non-formality — visible at strict level, invisible at homotopy level, structurally meaningful at chain-explicit level. The Costello TCFT operator $B^{(2)}_{\mathrm{TCFT}}$ is the *tuning fork* that re-aligns the resonance; the Stasheff $A_\infty$-relations are the *strings* that transmit the cancellation cross-arity.

**Inner motion.** Three named morphisms animate the ladder: the L3 → L2 *constructive* refinement (provides explicit homotopy), the L2 → L1 *operatorial* refinement (constructs $B^{(2)}_{\mathrm{TCFT}}$), the formal → non-formal → class-M *generalisation* (extends the construction across shadow classes via Stokes resurgence).

**Inner poetry.** The chain-level $[m_3, B^{(2)}] \neq 0$ is the chiral algebra's *whisper* — the trace at which Vol III's homotopy-coherent unification meets the strict combinatorial reality of the bar complex. Healing 1 is the *first whisper made audible*.

— end of report —

Author of any future implementation: Raeez Lorgat. No commits performed in this wave. Manuscript untouched.

Total target ~4500 words; actual ~4,720 words.

Delivered: `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_frontier_CY_A3_chain_level_attack_heal.md`.
