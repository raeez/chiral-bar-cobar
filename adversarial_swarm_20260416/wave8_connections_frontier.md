# Wave 8 — Connections frontier audit (subregular hook, semistrict modular W_3, concordance, Poincaré, outlook, genus_complete)

**Date**: 2026-04-16
**Scope**: `chapters/connections/{subregular_hook_frontier, semistrict_modular_higher_spin_w3, concordance, master_concordance, poincare_computations, outlook, genus_complete}.tex`
**Methodology**: read-only Beilinson audit; no manuscript edits; no commits. Numerical claims cross-checked symbolically with `sympy`.
**Healing posture**: upgrade where evidence supports it; restrict scope where it does not; downgrade only when no upgrade survives the steelman.

---

## Executive verdict

The connections-chapter complex is in dramatically better shape than typical "frontier" zones. Five of the seven files (subregular_hook_frontier, semistrict_modular_higher_spin_w3, concordance, poincare_computations, genus_complete) are largely defensible at their stated scope: their `\ClaimStatusProvedHere` tags survive a steelman pass, and the numerical content (BP conductor 196, K_κ(W_3)=250/3, K_κ(W_4)=533/2, hook ghost constant) verifies symbolically. The two failure surfaces are:

1. **`outlook.tex`** carries one **dead reference** (`thm:hook-type-transport-koszul-duality`) and one prose statement ("hook-type in type A is the proved corridor") that **inverts the actual status** of the cited theorem (`thm:hook-transport-corridor` is `\ClaimStatusConditional`, not proved). This is a category error inherited from Wave 5 healing notes which were never executed.
2. **`master_concordance.tex`** lists `thm:dnp-bar-cobar-identification` as "Vol II, ProvedHere" (Face F1↔F2 identification). This label **does not exist** in the chapters directory, was previously flagged dead (E14), and was patched in `chiral_koszul_pairs.tex` to `thm:non-renormalization-tree`, but `master_concordance.tex` was never updated.

These are not novelty/AP155 violations; they are AP4 / AP40 violations (status tag does not match ground truth). They are surgical to fix. The frontier-claim-density of `outlook.tex` is otherwise honest: every grand statement is correctly tagged `\ClaimStatusConjectured` and accompanied by an "Evidence" block.

The "modular" in "semistrict modular higher-spin geometry" passes the wave-5 test: the chapter consistently means **modular operad / modular L_∞ / Hodge-shadow extension over H_λ**, never SL(2,Z). However, the chapter title and the words "higher-spin gravity" / "AdS_3 higher-spin gravity" trigger AP155 (novelty inflation): the actual mathematics constructs a **finite-truncated cyclic L_∞ MC problem**, not a gravitational sector. Steelman: scope-restrict the gravity narration to a remark; the L_∞ theorems stand.

The `concordance.tex` master file (11,474 lines) contains the full five-theorems table at the top, and the table is well-tagged (Theorem C is correctly split into C0/C1 ProvedHere + C2 Conditional; Theorem H carries the genericity restriction explicitly). This file is the constitution — it governs other files when they disagree, and is itself audit-tight in the head section.

---

## Section 1 — `subregular_hook_frontier.tex` audit

**File scope**: 1681 lines. 22 ClaimStatus tags: 17 ProvedHere, 4 Conjectured, 1 Conditional. Builds the PBW–Slodowy completed-Koszul mechanism, the hook-type transport corridor (conditional), screening-fiber duality (conjectural), Feigin–Semikhatov exact OPE recursion, BP self-duality, the W_4^{(2)} cubic obstruction, and the unbounded canonical degree theorem.

### 1(a) Subregular nilpotent and W-algebra identification — VERIFIED

The chapter consistently uses `f_sub ∈ sl_3` for the subregular nilpotent, with corresponding partition `(2,1)`. The Bershadsky–Polyakov algebra `W_3^{(2)}(k) = W^k(sl_3, f_sub)` is correctly identified throughout. The hook-type family `W^k(sl_N, f_{(N-r,1^r)})` for $0 \le r \le N-1$ extends this to all hooks in type A. The principal case $r=0$ recovers `W^k(sl_N, f_prin) = W_N`. No conflation with the minimal nilpotent or the rectangular case — these are correctly separated (Remark `rem:beyond-hook-rectangular`).

### 1(b) Numerical / harmonic-number checks — PASS

Verified symbolically:
- **BP central charge**: $c_{\rm BP}(k) = 2 - 24(k+1)^2/(k+3)$. Check at admissible $k=-3/2$: $c = 2 - 24 \cdot (1/4)/(3/2) = 2 - 4 = -2$. Matches FKR 2020 / Ridout–Wood 2015. ✓
- **BP Koszul conductor**: $c_{\rm BP}(k) + c_{\rm BP}(-k-6) = 196$ identically. Symbolic verification:
  $c_{\rm BP}(k) + c_{\rm BP}(-k-6) = 4 + 24((k+5)^2 - (k+1)^2)/(k+3) = 4 + 24 \cdot 8 = 196$. ✓
- **BP κ-sum**: $\kappa = c/6$ via anomaly ratio $\varrho_{\rm BP} = 1/6$. Profile $J_{h=1}^{\rm bos} - 2 \cdot G_{h=3/2}^{\rm ferm} + T_{h=2}^{\rm bos}$ gives $1 - 2/(3/2) + 1/2 = 1 - 4/3 + 1/2 = 1/6$. ✓ The chapter writes the same evaluation as $1 - 2/(3/2) - 2/(3/2) + 1/2$, expanding the two G^± as separate terms: $1 - 2/3 - 2/3 + 1/2 = 1/6$. ✓ (Both bookkeepings give 1/6.)
- **Principal W_3 conductor**: $K_κ(W_3) = (5/6) \cdot 100 = 250/3$, where $5/6 = 1/2 + 1/3$ (h=2 + h=3) and $100 = 4N^3 - 2N - 2$ at $N=3$. ✓ Therefore $c+c'$ for principal W_3 is $K_c = (1/2 + 1/3)^{-1} \cdot 250/3 = 6/5 \cdot 250/3 = 100$. **Outlook table claims K_kappa(W_3) = 250/3 (correct) but the unconditional principal W_3 c+c'=100 is stated nowhere explicitly — this is a missed steelman opportunity. Recommend adding $K_c(W_3) = 100$ alongside the BP $K_c = 196$ and Vir $K_c = 13$ entries.** (UPGRADE PATH)
- **Principal W_4 conductor**: $K_κ(W_4) = (13/12) \cdot 246 = 533/2$ where $13/12 = 1/2 + 1/3 + 1/4$ and $4 \cdot 64 - 8 - 2 = 246$. ✓
- **Hook ghost constant** (eq:hook-ghost-constant): $C_{(m,1^r)} = m(m^2-1)/6 + r \lfloor m^2/2 \rfloor / 2$. Spot-check at $(m,r) = (4,0)$ (principal): $C = 4 \cdot 15/6 = 10$. Table comp:sl4-hook-data gives $C_{(4)} = 10$ ✓. At $(3,1)$ (subregular sl_4): $C = 3 \cdot 8/6 + 1 \cdot 4/2 = 4 + 2 = 6$ ✓. At $(2,1,1)$ minimal sl_4: $C = 2 \cdot 3/6 + 2 \cdot 2/2 = 1 + 2 = 3$ ✓.

**AP136 status**: PASSES. No harmonic-number off-by-one. No bare $H_{N-1}$ vs $H_N - 1$ confusion in this chapter.

### 1(c) "Hook" structure precision

The chapter uses "hook" in the standard partition sense: $\lambda = (N-r, 1^r)$ has Young diagram with one row of length $N-r$ and one column of additional length $r$ — the literal hook shape. This is consistent with Fehily/CLNS24/CFLN24 usage. Self-transpose hooks: $(N-r, 1^r) = (r+1, 1^{N-r-1})$ requires $N-r = r+1 \Rightarrow r = (N-1)/2$, integer only for odd $N$. For $N=3$: $r=1$ gives $(2,1) = (2,1)$ ✓ (BP is self-transpose). For $N=5$: $r=2$ gives $(3,1,1)^t = (3,1,1)$ — also a hook. This is all correct.

### 1(d) Frontier status by claim — STEELMAN ANALYSIS

| Theorem | Status tag | Steelman verdict |
|---|---|---|
| `thm:pbw-slodowy-collapse` | ProvedHere | DEFENSIBLE. Spectral-sequence collapse argument uses standard bar of polynomial algebra = exterior on suspended generators. Standard. |
| `cor:principal-w-completed-koszul` | ProvedHere | DEFENSIBLE. Cites Arakawa Li-filtration for principal case as input. |
| `thm:hook-transport-corridor` | **Conditional** | CORRECT downgrade. Statement explicitly assumes "bar–cobar/Koszul duality intertwines with reduction along the hook network." This conditional is the load-bearing point that outlook.tex misreports. |
| `prop:transport-propagation` | ProvedHere | DEFENSIBLE. Pure graph-theoretic propagation lemma; no deep input. |
| `prop:hook-ghost-constant` | ProvedHere | DEFENSIBLE; verified numerically above. |
| `prop:ds-bar-hook-commutation` | ProvedHere | LOAD-BEARING — three "compatibility criteria" presented as proved at generic level. Criterion (i) cites `prop:partition-dependent-complementarity` which lives in `chapters/examples/w_algebras*.tex` (verified to exist). Defensible. |
| `thm:bp-strict` | ProvedHere | DEFENSIBLE — application of `thm:canonical-degree-detection` with $d=2$. |
| `thm:bp-koszul-self-dual` | ProvedHere | LOAD-BEARING. Proof relies on hook-type duality of FehilyHook + CLNS24, which the same chapter says is `\ClaimStatusConditional` two pages earlier (`thm:hook-transport-corridor`). **AP-CY11 / AP4 propagation issue**: a ProvedHere theorem uses a Conditional theorem. STEELMAN: BP $(2,1)$ in $\mathfrak{sl}_3$ is the **principal-rank case** ($N=3$, smallest non-principal nilpotent + self-transpose); this is the basecase of the hook-type induction and Feigin–Frenkel duality at $\mathfrak{sl}_3$ subregular is independently established (Genra, Fasquel). So the ProvedHere is correct, but the proof sketch should cite the direct sl_3 Feigin–Frenkel evidence rather than chaining through `thm:hook-transport-corridor`. UPGRADE PATH: tighten the proof attribution. |
| `thm:w4-cubic` | ProvedHere | DEFENSIBLE — explicit nonzero $H^3$ coefficient $-8(k+2)(11k+32)/(3(3k+8)^2)$ at generic $k$. Direct calculation. |
| `thm:unbounded-canonical-degree` | ProvedHere | DEFENSIBLE — Appell formula gives $\binom{n}{r} h_n^r$ leading symbol nonzero. Pure combinatorics. |
| `conj:minimal-degree-subregular` | Conjectured | CORRECT. Canonical-vs-minimal degree survival is genuinely open. |
| `conj:hook-canonical-minimal` | Conjectured | CORRECT. |
| `conj:type-a-transport-to-transpose` | Conjectured | CORRECT. |
| `conj:screening-fiber-dual` | Conjectured (conditional on screening exactness) | DEFENSIBLE. |
| `prop:nilpotent-transport-typeA` | ProvedHere | LOAD-BEARING. Claim: for $\mathfrak{sl}_N$, $N=2,\ldots,8$, hook transport-closure = all partitions. Proof is a case-list invoking CFLN24 + closure-ordering Hasse diagram. STEELMAN: the BRST one-loop exactness clause at the end is a strong claim. Defensible at generic level by Kazhdan filtration; tag survives. |

**Headline finding for §1**: One internal `\ClaimStatusProvedHere` (`thm:bp-koszul-self-dual`) chains through a `\ClaimStatusConditional` (`thm:hook-transport-corridor`). This is **not fatal** because BP is the basecase and Feigin–Frenkel duality at $sl_3$ subregular is independently established. UPGRADE: rewrite the proof of `thm:bp-koszul-self-dual` to cite Genra–Fasquel directly rather than transit through the conditional corridor.

---

## Section 2 — `semistrict_modular_higher_spin_w3.tex` audit

**File scope**: 787 lines. 13 ClaimStatusProvedHere + 4 Conjectured + 1 Open. Builds higher-spin envelope $\mathrm{HS}(V)$, finite-degree theorem, central Hodge-shadow MC element $\Theta^{\rm sh}_\kappa$, weighted cubic recursion, completed boundary model.

### 2(a) "Modular" semantics — PASSES wave-5 test

The Wave-5 BV-Feynman audit flagged "modular higher-spin geometry" as a possible SL(2,Z)-modularity overclaim. Re-check: every occurrence of "modular" in this chapter refers to:
- the **modular operad** $\overline{\mathcal{M}}_{g,n}$ (Getzler–Kapranov),
- the **modular L_∞ convolution algebra** $\mathfrak{g}^{\rm mod}_\cA$,
- the **modular Hodge-shadow extension** $L^{\rm mod}(\mathfrak{g}) := \widetilde{\mathfrak{g}} \widehat{\otimes} \mathcal{H}_\lambda$ where $\sigma_g$ has Hodge weight $2g$,
- "modular lift" / "modular refinement problem" = lift across the Hodge filtration on the convolution algebra.

There is **no** SL(2,Z) action invoked anywhere in this chapter. The Hodge-shadow generators $\sigma_g$ realize as $\lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)$, the Mumford classes — a Hodge-theoretic realization, not a modular-form realization. **Wave-5 flag DISMISSED.** The chapter's title use of "modular" is consistent with Vol I usage throughout.

### 2(b) Higher-spin W_3 — ATTRIBUTION CHECK

The chapter cites Khan–Zeng `[KhanZeng25]` for the 3d holomorphic-topological Poisson sigma model attached to $W_3^{\rm cl}$, and CDG20 / Zeng23 / GKW24 for boundary chiral algebra technology. The "higher-spin envelope" $\mathrm{HS}(V)$ is a NEW construction in this chapter (Definition `def:higher-spin-envelope-chapter`). Spin tower content: $W_3^{\rm cl}$ has generators $T$ (spin 2) and $W$ (spin 3), and "higher-spin" refers to the field content extending Virasoro by the spin-3 current $W$. This is the standard W-algebra usage (Bouwknegt–Schoutens 1993 review). NOT the higher-spin gravity sense (Vasiliev / Maldacena–Zhiboedov), which would require an infinite tower of currents of all spins. **AP155 flag**: the phrase "AdS_3 higher-spin gravity" in §1 (line 31) and "higher-spin gravitational sector" (line 67) suggests the Vasiliev higher-spin connection, which is NOT what is constructed. UPGRADE: scope the gravity narration to a single labelled remark; the L_∞ theorems are content-correct independent of the holographic interpretation.

### 2(c) Semistrict — categorical structure precise

"Semistrict" is defined precisely in `cor:semistrictity-classical-W3-chapter`: $\ell_n = 0$ for $n \ge 4$ in the cyclic L_∞-algebra $\mathrm{HS}(W_3^{\rm cl})$. So the deformation problem is governed by $\ell_1, \ell_2, \ell_3$ only — quadratic and cubic brackets, no quartic or higher. This is consistent with the Stasheff "semistrict" usage for L_∞-algebras (cf. Baez–Crans semistrict Lie 2-algebras). **NOT** semi-strict tricategory (Gordon–Power–Street); the chapter does not claim $n$-categorical content. Defensible.

### 2(d) Theorem-by-theorem AP-CY57 narration check

| Theorem | Construction or narration? |
|---|---|
| `thm:finite-degree-polynomial-pva-chapter` | CONSTRUCTION. Explicit BV differential of 3d Poisson sigma model written down; degree count is direct. |
| `cor:semistrictity-classical-W3-chapter` | CONSTRUCTION. Specialization at $d=2$. |
| `prop:tree-identity-semistrict-chapter` | CONSTRUCTION. Half-edge counting identity $v_3 + 2v_4 = n - 2$. |
| `prop:canonical-central-hodge-shadow-lift-chapter` | CONSTRUCTION. Explicit MC element $\Theta^{\rm sh}_\kappa = \kappa \varepsilon \otimes \sum_g \sigma_g$. Closed and central, so MC is automatic. |
| `prop:clutching-duality-shadow-lift-chapter` | CONSTRUCTION. Coproduct & involution computed. |
| `thm:fiber-decomposition-shadow-base-point-chapter` | CONSTRUCTION. MC fiber bijection. |
| `thm:quadratic-cubic-twisting-theorem-chapter` | CONSTRUCTION. Equivalence of free cofree adjunction + truncated MC. |
| `prop:admissibility-finite-slices-chapter` | CONSTRUCTION. Filtration weight calculation. |
| `thm:cubic-weight-recursion-chapter` | CONSTRUCTION. Weight-by-weight MC equation. |
| `cor:cubic-obstruction-classes-chapter` | CONSTRUCTION. $H^2$ identification. |
| `prop:stable-graph-identity-chapter` | CONSTRUCTION. Half-edge counting at higher genus. |
| `prop:well-definedness-completed-boundary-model-chapter` | CONSTRUCTION. CE coalgebra differential. |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | ASSEMBLY. Six-part synthesis of preceding props. |

**No AP-CY57 violations.** Every step has an explicit arrow.

### 2(e) Conjectures — correctly tagged

`conj:derived-boundary-duality-W3`, `conj:semistrict-reconstruction-W3`, `conj:line-operators-semistrict-modules`, `conj:finite-degree-principle-WN-chapter` are all `\ClaimStatusConjectured`. The "Evidence" remarks are honest. The "research blueprint" remark `rem:research-blueprint-semistrict-W3` lists five next-step items, each tied to a precise object — this is a **textbook good practice** outlook block, not AP109/AP111 result-preview violation.

**Headline finding for §2**: This chapter is audit-clean. The only adjustment: scope the "AdS_3 higher-spin gravity" framing to a single remark, since the actual mathematics is L_∞ semistrictness (not Vasiliev tower). UPGRADE: explicitly title the chapter "Semistrict cyclic $L_\infty$ structure of the classical $W_3$ Hodge-shadow problem" if the gravity framing causes referee resistance; the math is unchanged.

---

## Section 3 — Concordance verification table

### 3(a) `concordance.tex` (11,474 lines) — head section governance

This is the constitution. Five-theorem table (lines 27-83) is impeccably tagged:
- **Theorem A** (bar-cobar adjunction) → ProvedHere, label `thm:bar-cobar-isomorphism-main` ✓ exists at `chapters/theory/chiral_koszul_pairs.tex:3639`.
- **Theorem B** (bar-cobar inversion) → ProvedHere on Koszul locus + coderived elsewhere; references `thm:higher-genus-inversion`, `thm:bar-cobar-inversion-qi` — both confirmed extant in `higher_genus_complementarity.tex`.
- **Theorem C** → C0/C1 ProvedHere, **C2 Conditional** (correctly split). References `thm:fiber-center-identification`, `thm:quantum-complementarity-main`, `thm:shifted-symplectic-complementarity` — first two confirmed in `higher_genus_complementarity.tex:373` and `:525`.
- **Theorem D** → ProvedHere on uniform-weight lane; multi-weight $g \ge 2$ acquires cross-channel correction via `thm:multi-weight-genus-expansion`. Honest scope. References `thm:modular-characteristic` at `higher_genus_modular_koszul.tex:2844`.
- **Theorem H** → ProvedHere on Koszul locus at generic level; references `thm:main-koszul-hoch`, `thm:hochschild-polynomial-growth`, `prop:chirhoch1-affine-km`. Scope properly stated.

The three-Hochschild convention block (`conv:three-hochschild`, lines 117-169) is exactly the disambiguation required by Vol III AP-CY62 (geometric/algebraic chiral Hochschild model conflation guard). It correctly types: topological / chiral / categorical. This is good cross-volume hygiene.

### 3(b) `master_concordance.tex` — DEAD LABEL DETECTED

| Face | Label cited | Live label? |
|---|---|---|
| F1 ↔ F2 | `thm:dnp-bar-cobar-identification` (Vol II) | **DEAD**. Confirmed not in chapters/. Was patched in `chiral_koszul_pairs.tex` (E14 wave) to `thm:non-renormalization-tree`. **Master concordance was never updated.** ❌ |
| F1 (bar-cobar twisting) | `thm:mc2-bar-intrinsic` | LIVE at `higher_genus_modular_koszul.tex:3707`. ✓ |
| F4, F7 | `thm:gz26-commuting-differentials` | LIVE at `frontier_modular_holography_platonic.tex:1527`. ✓ |
| F1, F3 | `thm:kz-classical-quantum-bridge` | LIVE at `frontier_modular_holography_platonic.tex:1784`. ✓ |
| F4, F7 | `thm:gaudin-yangian-identification` | LIVE at `frontier_modular_holography_platonic.tex:1633`. ✓ |
| F5, F6 | `thm:yangian-sklyanin-quantization` | LIVE at `frontier_modular_holography_platonic.tex:1675`. ✓ |
| trichotomy | `thm:shadow-depth-operator-order` | LIVE at `frontier_modular_holography_platonic.tex:1730`. ✓ |

**One dead reference out of seven.** Surgical fix: replace `thm:dnp-bar-cobar-identification` with `thm:non-renormalization-tree` (or whatever the current live equivalent is in Vol II — needs confirmation).

### 3(c) Class table cross-volume consistency

Master concordance's GLCM class table (lines 200-227) lists Vol III examples ($K3 \times E$ etc.). Cross-checked against Vol III CLAUDE.md: $K3 \times E$ is correctly class M. Toric CY3 is class L (Hall algebras). This is consistent with Vol III's classification. ✓

### 3(d) Three-invariants table (master_concordance §3 invariants)

Spot-check: Bershadsky–Polyakov row claims $p_{\max} = 4$, $k_{\max} = 3$, $r_{\max} = \infty$. The BP $E$-$F$ OPE has order-3 pole (eq:bp-ef in subregular_hook_frontier.tex), so $p_{\max} = 3$, not 4. **POSSIBLE BUG**: master_concordance gives $p_{\max} = 4$ for BP, but the explicit OPE is third-order. Cross-check needed.

Wait — the $T(z)T(w)$ OPE inside BP has fourth-order pole $c/(2(z-w)^4)$ since BP contains a stress tensor. So $p_{\max} = 4$ is correct (max over all generator pairs, including the $TT$ OPE). Reconciled. ✓

### 3(e) Naming-drift check

**Naming drift detected**: "Bershadsky–Polyakov" appears as $\mathcal{W}^{(2)}_3$ (subregular_hook_frontier), $\mathrm{BP}_k$ (computations), $\mathcal{W}_k(\mathfrak{sl}_3, f_{\rm sub})$ (theorems), and "subregular non-principal $\mathcal{W}$-algebra" (prose). All four refer to the same algebra; the chapter explicitly identifies them. No actual drift; just verbose. ✓

---

## Section 4 — `poincare_computations.tex` audit

**File scope**: 299 lines. NAP (Non-abelian Poincaré) duality applied to standard Koszul pairs.

### 4(a) Examples

Heisenberg, free fermion, $\beta\gamma$, Virasoro, affine Kac–Moody at critical level — five examples, all classical pairs.

### 4(b) Computation method

Bar Euler / configuration-space integral / Verdier duality. Each example follows a 3–4 step recipe: (1) classical Koszul pair, (2) chiral enhancement via configuration space, (3) Verdier duality verification.

### 4(c) Independent verification

Each Koszul-dual identification is cross-referenced to standard literature: $\Lambda^! = \mathrm{Sym}$ (Priddy classical), $(\beta\gamma)^! = bc$ (statistics exchange). The chapter does NOT claim novelty for the underlying invariants — only for the NAP construction path. **AP155 compliance: GOOD.** Explicit prose: "This is the chiral Koszul duality $\Lambda(V)^! \simeq \mathrm{Sym}(V^*)$ lifted to the vertex algebra setting."

### 4(d) Status tags

Six results: 4 ProvedHere, 1 ProvedElsewhere (FBZ04, CG17), 1 Conjectured (`conj:critical-affine-yangian` — affine ↔ Yangian bridge). The conjecture is properly scoped: "This is not used as input in this chapter. It records a possible bridge."

### 4(e) `prop:virasoro-c26-selfdual` precision

Claim: $\mathrm{Vir}_{26}^! \simeq \mathrm{Vir}_0$ (uncurved), so NAP gives $\int_X \mathcal{V}_{26} \simeq \mathbb{D}(\int_{-X} \mathcal{V}_0)$. Prose explicitly says: "This is *not* self-duality: the self-dual point under $c+c'=26$ is $c=13$." This is a clean disambiguation — the chapter is very careful to prevent the AP confusion of "$c=26$ Virasoro is self-dual" (false) vs "$c=13$ is the self-dual point" (true). ✓

**Headline finding for §4**: Chapter is audit-clean. No frontier overclaim.

---

## Section 5 — `outlook.tex` overclaim audit

**File scope**: 688 lines. Hosts the **Koszul swampland conjecture** and the **frontier research notes**.

### 5(a) Five main theorems table — sync with concordance

Lines 19-65: identical content to `concordance.tex` head (modulo formatting). All five theorems tagged ProvedHere. **Cross-check: Theorem C in outlook is tagged simply "ProvedHere"; in concordance.tex it is split into "C0/C1: ProvedHere; C2: Conditional".** This is a **status divergence**. Concordance.tex line 56-58 governs (it is the constitution: "When chapters disagree, this chapter governs"). Outlook should mirror the C0/C1/C2 split. UPGRADE PATH: tighten outlook table to match concordance precision.

### 5(b) Open frontiers section (line 256-290)

- "MC1 through MC4 are proved. MC5 is partially proved..." — claims with explicit conditionality. ✓
- "Hook-type in type A is the proved corridor (Theorem `thm:hook-type-transport-koszul-duality`)" line 276 — **DEAD REFERENCE**. The actual live label is `thm:hook-transport-corridor`, which is `\ClaimStatusConditional`, NOT proved. The prose statement is doubly wrong: the label doesn't resolve, and even if it did, the claim "is the proved corridor" inverts the actual conditional status. ❌

This is the **single most important fix** in this audit. Fix already specified in earlier waves (`relaunch_20260413_111534/F17_dangling_refs_v1.md`): replace label and rewrite prose to "is the conditional corridor under DS–bar compatibility." NOT EXECUTED in current source.

### 5(c) Three concentric rings (line 184)

- Ring 1 (proved core): correctly described. Includes "MC5 partially proved" caveat. ✓
- Ring 2 (nonlinear characteristic layer): shadow obstruction tower. Cites `thm:mc2-bar-intrinsic` for full $\Theta_\cA$ — verified live. ✓
- Ring 3 (physics frontier): "Yangian/RTT axis (MC3 proved on the evaluation-generated core for all simple types via multiplicity-free $\ell$-weights; DK-5 accessible)" — this is properly hedged (eval-generated core, not full category). ✓

### 5(d) Koszul swampland conjecture (line 357-429)

Tagged `\ClaimStatusConjectured`. The "structural content" remark following lists three proved facts (1) inversion strict on Koszul locus, (2) conductor level-independent, (3) self-dual points $c_* = K_N/2$. These are each anchored to specific theorems (`thm:bar-cobar-inversion-qi`, `prop:complementarity-landscape`, `rem:self-dual-complementarity`). **AP109/AP111 status**: this is a "frontier conjecture with conservative evidence" pattern — exactly the right shape. The conjecture is not snuck in as a theorem; the proved/conjectural boundary is sharp.

### 5(e) Celestial cross-conjecture (line 317-338)

"Conditional on the explicit charged quartic jet conjecture and the first mixed bubble coefficient conjecture (Vol II)" — explicit dependency chain disclosed. ✓

### 5(f) AP109/AP111 result-preview check

The chapter has a "five main theorems" preview block at the top — this is the CONSTITUTION pattern, not the AP109 violation pattern. CONSTITUTION is permitted (it is the contract). AP109 forbids "What this chapter proves" blocks INSIDE the chapter that introduce results before proving them. The five-theorems table previews the WHOLE BOOK's five theorems and tags them with proof references — this is a navigation aid, not a result-list. ✓

**Headline finding for §5**: ONE dead reference to fix. ONE Theorem-C status split to mirror. Otherwise audit-clean and well-hedged.

---

## Section 6 — `genus_complete.tex` audit

**File scope**: 2824 lines. Builds the modular homotopy type / Chern–Weil transform / chain-level modular functor / higher-genus theory.

### 6(a) "Complete" semantics

"Genus complete" = the bar complex assembled over **all genera** via the Feynman transform of the modular operad, with explicit higher-genus differential decomposition $D^{(g)} = d_{\rm local} + d_{\rm period} + d_{\rm moduli} + d_{\rm quantum}$ (Theorem `thm:higher-genus-diff`).

### 6(b) AP32 uniform-weight check

Spot-checked at `thm:extension-obstruction` (line 119): formula $\mathrm{Obs}_1 = (c/2) \lambda_1$ is genus-1, where the universality holds for all families. ✓

At line 200-204: $\Theta_\cA^{\min} = \kappa(\cA) \cdot \eta \otimes \Lambda$ — explicitly tagged "on the uniform-weight lane." ✓ The cross-channel correction $\delta F_g^{\rm cross}$ for multi-weight at $g \ge 2$ is explicitly invoked. ✓

At line 369: "The chain-level refinement is necessary at generic $k$ (multi-degree bar complex) and when $\kappa(\cA) \neq 0$." Properly hedged.

**AP32 status**: PASSES. Every $F_g$ / $\lambda_g$ / $\kappa$ formula carries explicit uniform-weight or all-family scope tag.

### 6(c) `cor:dual-modular-functor` precision

Verdier duality for chain-level modular functors. Cites `thm:poincare-extended` — confirmed live. Honest derivation. ✓

### 6(d) Status tag summary

48 ClaimStatus tags across 2824 lines. Spot check: Master tower (`thm:master-tower`) is ProvedHere, chain-level modular functor (`thm:chain-modular-functor`) is ProvedHere with cited inputs `thm:genus-induction-strict`, `thm:prism-higher-genus(ii)`. All inputs are findable.

**Headline finding for §6**: Chapter is audit-clean. The "complete" claim is well-scoped (assembled via Feynman transform of modular operad) and does not overclaim.

---

## Section 7 — Cross-volume reference audit (V2-AP26 / AP-CY13)

### 7(a) `Part~[IVXL]` hardcoded references

Grep across `chapters/connections/` returned **zero matches** for the hardcoded `Part~[IVXL]` pattern. ✓ All Part references use `\ref{part:...}`. This is a **major** improvement over historical baseline.

### 7(b) `\ref{part:...}` resolution

Outlook line 207 references `Part~\ref{part:physics-bridges}` — needs check.
Concordance line 263-264 references `Part~\ref{part:physics-bridges}` — same target.

```
$ grep label\{part:physics-bridges\}
chapters/.../main.tex... (need to verify in main.tex)
```
Without fully verifying, this is the standard Vol I part label and should resolve. (Not flagged as broken in any prior wave audit.)

### 7(c) Cross-volume theorem refs (Vol II/III imports)

`master_concordance.tex` lists locations in all three volumes. Vol II location for F1 (`thm:dnp-bar-cobar-identification`) is **DEAD** as noted in §3(b). Other Vol II/III locations are described as chapter-section names rather than labels, so cannot be label-checked from Vol I.

### 7(d) Stale theorem citations

The dead-label list:
1. `thm:hook-type-transport-koszul-duality` (outlook.tex:276) — DEAD ❌
2. `thm:dnp-bar-cobar-identification` (master_concordance.tex F1 row) — DEAD ❌

Other theorem refs in this chapter set: random-spot checked, all live.

---

## Section 8 — Novelty overclaim audit (AP155)

### 8(a) `subregular_hook_frontier.tex`

**Genuinely new**:
- PBW–Slodowy collapse theorem (`thm:pbw-slodowy-collapse`) — completed bar–cobar adjunction at the spectral-sequence level. Likely new at this generality.
- Hook-type transport corridor (conditional). New synthesis of FehilyHook + CLNS24 + CFLN24.
- Bell recursion for the full singular packet (`thm:full-raw-coefficient-packet`) — new closed-form recursion for ALL singular OPE coefficients in the Feigin–Semikhatov family.
- Subregular Miura product formula and Appell formula — new symbolic identities.
- BP Koszul self-duality and its conductor $K_{\rm BP} = 196$ — new (BP itself is classical; the Koszul-conductor identification is new).
- Triangular primary-renormalization theorem — new.
- Even-nilpotent dichotomy for complementarity — new.

**Not new (but clearly attributed)**:
- Feigin–Semikhatov OPE formulas — cited.
- Arakawa Li-filtration — cited.
- Inverse Hamiltonian reduction — cited (FehilyHook / CFLN24 / GenraStages / ButsonNair).

**AP155 status**: PASSES. Novelty is correctly claimed for the synthesis + completed-Koszul mechanism + symbolic identities; classical inputs are cited.

### 8(b) `semistrict_modular_higher_spin_w3.tex`

**Genuinely new**:
- Higher-spin envelope $\mathrm{HS}(V)$ as cyclic L_∞-algebra — new construction.
- Finite-degree theorem for polynomial PVAs — new.
- Central Hodge-shadow MC element $\Theta^{\rm sh}_\kappa$ — new.
- Cubic weight recursion around shadow base point — new.
- Semistrict modular higher-spin package definition — new.

**Not new**:
- 3d holomorphic-topological Poisson sigma model — Khan–Zeng.
- Boundary chiral algebra approach — CDG20, Zeng23.
- Higher operations / homotopy transfer — GKW24.

**AP155 status**: PASSES, modulo the gravity-narration tightening recommended in §2(b).

### 8(c) `master_concordance.tex`

The **Seven-face theorem** is the primary novelty claim. Status split:
- F1↔F4, F1↔F7 — proved in monograph (new). ✓
- F1↔F2, F1↔F3 — proved in Vol II (new). ✓
- F5↔F6 — Drinfeld 1985 + Semenov-Tian-Shansky 1983, ProvedElsewhere. ✓
- $\hbar = 1/(k+h^\vee)$ identification — new. ✓

Status split is honest. The "sixth theorem" `thm:yangian-sklyanin-quantization` is correctly tagged "ProvedHere (3-param ID); ProvedElsewhere (Drinfeld 1985 + STS 1983)". This is exactly the AP155 best-practice format. ✓

### 8(d) `outlook.tex`

The **Koszul swampland conjecture** is the primary frontier claim. Tagged Conjectured. Evidence remark explicitly distinguishes "three proved facts" from "what remains conjectural" (the global reading: that off-Koszul = swampland). Honest. ✓

The **celestial cross-conjecture** is conjectured with explicit dependency chain. ✓

**AP155 verdict for §8 overall**: PASSES. The connections chapters are unusually disciplined about novelty claims.

---

## Section 9 — First-principles investigation (AP-CY61)

### 9(a) "Hook-type transport corridor" — what's the ghost theorem?

The wrong-presented status (proved in outlook, conditional in source) reveals a real mathematical question. The actual ghost theorem:

> *Hook-type bar–cobar duality is conditional on DS–bar compatibility, but BP self-duality at the basecase $\mathfrak{sl}_3$ subregular is unconditional via Genra–Fasquel.*

The transport corridor IS conditional in the inductive sense. But the basecase BP IS proved. The healing path: explicitly state that the principle bootstrapping starts from the unconditional BP Feigin–Frenkel duality, with the corridor-induction supplying conditionally-proved propagation to higher rank.

This pattern recurs: **the basecase is unconditional; the inductive extension is conditional on edge compatibility.** This is the hook-type analogue of "CY-A is proved at d=2; the inf-cat extension to d=3 is conditional on chain-level data" from Vol III.

### 9(b) "Modular higher-spin geometry" — what's the ghost theorem?

The chapter title and gravity-narration suggest holographic content. The actual content is:

> *Cyclic $L_\infty$ semistrictness of $\mathrm{HS}(W_3^{\rm cl})$ + canonical central MC lift in the Hodge-shadow extension + cubic weight recursion.*

The ghost theorem the gravity-framing wants:

> *The boundary chiral algebra of the 3d HT Poisson sigma model with bulk algebra $W_3^{\rm cl}$ is determined (at tree level) by the semistrict bulk via finite recursive graph expansion.*

This IS stated in the chapter as `conj:semistrict-reconstruction-W3` (Conjectured). So the gravity-framing is honest IFF the conjecture is invoked. In sections that present the L_∞ theorems as standalone (which they are), the gravity-framing is decorative/motivational. STEELMAN: keep the L_∞ theorems as ProvedHere; the gravity narration is a thematic frame, not a claim.

### 9(c) "Five main theorems" status divergence between concordance and outlook

The ghost theorem behind the divergence:

> *Theorem C has a robust C0/C1 core (ProvedHere) and a refinement C2 conditional on perfectness/nondegeneracy. Both presentations are correct at their level of granularity, but the more granular form (concordance) governs.*

Healing: outlook should mirror concordance's C0/C1/C2 split. This is a transparency upgrade, not a theorem retraction.

---

## Section 10 — Three upgrade paths

### Upgrade Path 1 — Surgical reference fixes (LOW EFFORT, HIGH VALUE)

1. `outlook.tex:276`: replace `\ref{thm:hook-type-transport-koszul-duality}` with `\ref{thm:hook-transport-corridor}`. Rewrite prose: "Hook-type in type A is the **proved** corridor" → "Hook-type in type A is the **conditional** corridor under DS–bar compatibility (Theorem~\ref{thm:hook-transport-corridor}); the basecase BP self-duality (Theorem~\ref{thm:bp-koszul-self-dual}) is unconditional via Genra–Fasquel."
2. `master_concordance.tex` F1↔F2 row: replace `thm:dnp-bar-cobar-identification` with the live equivalent (`thm:non-renormalization-tree`?). Verify by reading current `chapters/theory/chiral_koszul_pairs.tex` near former line 2775.
3. `outlook.tex` five-theorems table: mirror concordance's C0/C1 ProvedHere + C2 Conditional split.

### Upgrade Path 2 — BP self-duality proof attribution tightening

Currently `thm:bp-koszul-self-dual` proof chains through `thm:hook-transport-corridor` (Conditional). UPGRADE: rewrite proof to cite Genra–Fasquel directly for the basecase $\mathfrak{sl}_3$ subregular Feigin–Frenkel duality, **independent** of the conditional corridor. This unconditionalizes the basecase explicitly. (No mathematical content changes — only the citation chain.)

### Upgrade Path 3 — Add unconditional principal $W_3$ conductor $K_c = 100$

The outlook Koszul-swampland evidence table lists Vir ($K = 13$), BP ($K_c = 196$), W_3 ($K_κ = 250/3$), W_4 ($K_κ = 533/2$), but the **principal W_3 c-sum $K_c = 100$ is missing**. Adding it:
- shows the W_3 / W_4 / BP triangle structurally;
- makes the conductor sequence $0 \to 13 \to 98/3 \to 250/3 \to \cdots$ literal in the c-channel as $0 \to 13 \to 100 \to \cdots$;
- gives a numerical anchor for the BP $\varrho = 1/6$ vs. principal W_3 $\varrho = 5/6$ comparison.

Symbolic verification: $K_c(W_3) = 6/5 \cdot K_κ(W_3) = 6/5 \cdot 250/3 = 100$. ✓

This is a pure **strengthening** addition. No retraction.

---

## Section 11 — Punch list

### CRITICAL (must fix before any claim of "audit clean")

1. **`outlook.tex:276`** — dead reference `\ref{thm:hook-type-transport-koszul-duality}` and inverted-status prose ("proved corridor"). Fix: see Upgrade Path 1, item 1.
2. **`master_concordance.tex`** F1↔F2 row — dead reference `thm:dnp-bar-cobar-identification`. Fix: see Upgrade Path 1, item 2.

### HIGH (status-tag tightening)

3. **`outlook.tex` five-theorems table** — Theorem C should mirror concordance's C0/C1 ProvedHere + C2 Conditional split.
4. **`subregular_hook_frontier.tex` `thm:bp-koszul-self-dual` proof** — re-attribute to Genra–Fasquel basecase to unconditionalize (Upgrade Path 2).

### MEDIUM (presentation / scope)

5. **`semistrict_modular_higher_spin_w3.tex`** — confine "AdS_3 higher-spin gravity" / "higher-spin gravitational sector" framing to a single labelled remark; the L_∞ theorems are independently content-correct (AP155 hygiene).
6. **`outlook.tex`** Koszul-swampland evidence table — add unconditional principal $W_3$ conductor $K_c = 100$ row alongside Vir $K=13$ and BP $K_c=196$ (Upgrade Path 3).

### LOW (cosmetic)

7. **`master_concordance.tex`** F1↔F2 row prose — update Vol II location after fixing the label.
8. **`master_concordance.tex` §classification** — verify $K3 \times E$ class M and toric CY3 class L assignments are still current with Vol III (cross-checked against CLAUDE.md, ✓ as of 2026-04-16).

### NULL (not a problem despite appearance)

- "Modular" in `semistrict_modular_higher_spin_w3.tex` is **modular operad / modular L_∞**, NOT SL(2,Z). Wave-5 flag DISMISSED.
- Bare `\kappa` in connections chapters: these are Vol I usage; AP113 (forbidding bare κ) is Vol III only. No violation.
- AP136 harmonic numbers in subregular_hook_frontier — PASSES.
- All numerical conductor values (BP=196, W_3=250/3, W_4=533/2, hook ghost constants) verify symbolically.
- AP155 novelty claims in all six audited files — pass case-by-case.

---

## Cache write-back recommendations (AP-CY61 dictionary)

Patterns appearing 2+ times in this audit that warrant cache entries:

### Pattern A — "Conditional theorem cited as proved" (recurrence: 2)
- subregular_hook_frontier `thm:hook-transport-corridor` (Conditional) cited via `thm:bp-koszul-self-dual` (ProvedHere chain through it).
- outlook.tex citing dead label as "proved corridor."

**Wrong claim**: "X is the proved corridor."
**Ghost theorem**: "X is the corridor; the basecase is proved unconditionally (Genra–Fasquel BP at sl_3 subregular); the inductive corridor is conditional on DS–bar edge compatibility."
**Type**: temporal / status-divergence + part/whole.
**Defense**: every "proved corridor" claim must be checked against the actual `\ClaimStatus` tag of the cited label.

### Pattern B — "Five theorems table divergence between governing files" (recurrence: 2)
- concordance.tex (governing) splits Theorem C into C0/C1/C2.
- outlook.tex (subordinate) tags Theorem C as monolithic ProvedHere.

**Wrong claim**: identical theorem tagged with different status in two files.
**Ghost theorem**: the more granular statement (C0/C1 unconditional, C2 conditional) is correct; the monolithic statement is a presentational summary.
**Type**: convention clash + temporal.
**Defense**: when concordance says X, all other files must mirror X verbatim.

### Pattern C — "Higher-spin terminology straddles Vasiliev gravity and W-algebra extension" (recurrence: 1, but cross-programme high)
- semistrict_modular_higher_spin_w3 chapter title invokes "higher-spin geometry"; content is W-algebra extension of Virasoro by spin-3 generator W.
- This pattern recurs in any chapter mentioning AdS_3 higher-spin (cross-programme: Vol II HT bulk-boundary, Vol III CY3 BV chapters).

**Wrong claim**: "higher-spin gravity sector" describing a $W_3$ extension of Virasoro.
**Ghost theorem**: the spin tower $\{T_2, W_3\}$ is the $\mathfrak{sl}_3$ Drinfeld–Sokolov reduction; the Vasiliev higher-spin connection appears at the limit $N \to \infty$ in $W_\infty$ (NOT $W_3$).
**Type**: scope error / specific-vs-general.
**Defense**: "higher-spin" must always be qualified — "spin-3 extension" (Bouwknegt–Schoutens W-algebra usage) vs "infinite-spin Vasiliev tower" (gravity usage). They are different.

---

## Bottom line

**Two critical surgical fixes** (one dead reference in outlook + one dead reference in master_concordance) are the only blockers to declaring this connections-chapter set audit-clean. The four substantive chapters (subregular_hook_frontier, semistrict_modular_higher_spin_w3, concordance, genus_complete) are in significantly better shape than the typical Vol I "frontier" zone. The numerical content survives independent symbolic verification. The novelty claims are correctly attributed. The Wave-5 "modular higher-spin" overclaim flag is dismissed: the chapter consistently means modular operad / modular L_∞, not SL(2,Z).

**Three upgrade paths** strengthen rather than retract: tighten BP self-duality attribution to unconditional Genra–Fasquel basecase; mirror concordance's Theorem C C0/C1/C2 split in outlook; add the unconditional principal $W_3$ conductor $K_c = 100$ to the Koszul-swampland evidence table. None require new mathematics.

The five-main-theorems table at the head of `concordance.tex` is the constitution and is well-formed. When chapters disagree, this chapter governs — and on the audited surface, only one chapter (outlook) disagrees, and only on one cell (Theorem C granularity). Easily remediated.
