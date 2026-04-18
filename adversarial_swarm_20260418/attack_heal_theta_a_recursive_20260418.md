# Attack-and-Heal: `thm:recursive-existence` (Theta_A all-degree inverse limit)

Date: 2026-04-18
AP block reserved: AP861-AP880
Target: Vol I `chapters/theory/higher_genus_modular_koszul.tex` `thm:recursive-existence` (line 13520)
Consumers surveyed: 24 `\ref{thm:recursive-existence}` sites in-chapter + `prop:depth-gap-trichotomy` (line 18217) which invokes the tower.

## Phase 1: Mission questions

(i) Locate `thm:recursive-existence`. Read statement + proof. What ambient does it claim convergence in? pro-Ch(Vect)? chain-level Ch(Vect)? both?

(ii) Verify the operadic weight filtration $w(g,r,d) = 2g-2+r+d$ genuinely has surjective transitions (strongest ML). For class M, is the transition $\gAmod / F^{N+2} \twoheadrightarrow \gAmod / F^{N+1}$ surjective in every $w$-stratum, or only some?

(iii) Step 4 ML argument: finite-dim (Weibel 3.5.7) or filtration-piece stabilisation? Does the theorem route the same way as MC5 Wave-12b heal?

(iv) "Chain-level termination class-dependent": is each class G/L/C/M inscribed with explicit finite-vs-transfinite statement in `thm:recursive-existence` itself?

## Phase 2: Findings

### F1. Ambient: the theorem lives in the weight-completion $\widehat{\gAmod}$ (pro-object), not in $\gAmod$ (chain-level).

The statement says verbatim (13535-13539):

> (ii) Convergence. The inverse limit $\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists in the weight-completion $\widehat{\gAmod}$ and satisfies the full Maurer-Cartan equation.

$\widehat{\gAmod} := \varprojlim_N \gAmod / F^{N+1} \gAmod$ is the pro-Artinian completion along the weight filtration. Step 1 of the proof (13547-13574) is explicit: the filtration is exhaustive, separated, complete, pronilpotent; each quotient $\gAmod / F^{N+1}$ is finite-dimensional. Step 4 (13624-13671) says verbatim

> The inverse system $\{\gAmod/F^{N+1}\gAmod\}_{N \geq 1}$ consists of surjections of finite-dimensional vector spaces (Step 1).

The theorem never makes a claim about chain-level termination in $\gAmod$ itself. It is a pro-object statement throughout. Clarifying remark `rem:recursive-existence-clarification` (13687-13712) reinforces: "the bar-intrinsic construction provides an explicit element in the completed space, and its weight-truncations are the recursive tower." This is the correct scope.

VERDICT: No ambient confusion inside the theorem. Status-table banner "all-degree inverse limit" is compatible with the pro-object reading.

### F2. Surjectivity is structural, not class-dependent.

Step 4 at 13628-13631 claims each transition map $\pi_{N+1,N}$ is surjective. This is correct and uniform: for any descending filtration, the quotient map $\gAmod / F^{N+2} \twoheadrightarrow \gAmod / F^{N+1}$ factors through the short exact sequence $0 \to F^{N+1}/F^{N+2} \to \gAmod/F^{N+2} \to \gAmod/F^{N+1} \to 0$ and is surjective by construction. No class hypothesis enters.

The $w$-strata do differ in class: each $F^N / F^{N+1}$ is a direct sum over tridegrees $(g, r, d)$ with $w = 2g - 2 + r + d = N$, and for class M (Virasoro, W_N) the operadic bar can have nonzero components at more combinatorial types than for class G (Heisenberg). But the quotient MAP $\gAmod / F^{N+2} \to \gAmod / F^{N+1}$ is surjective for all classes because it is a quotient map, independent of whether the strata are finite- or "richly"-populated.

VERDICT: Strongest form of ML (surjective transitions) holds uniformly across all four classes.

### F3. ML route: belt-and-suspenders (BOTH finite-dim AND surjective).

Step 1 bullet 3 establishes finite-dimensionality of each $\gAmod / F^{N+1}$:

> At each fixed weight $w$, there are finitely many triples $(g,r,d)$ with $2g-2+r+d = w$, $r \geq 2$, $d \geq 0$, $g \geq 0$, and for each such triple the space of stable graphs is finite. Therefore $\gAmod / F^{N+1} \gAmod$ is a finite-dimensional quotient.

Step 4 then invokes surjectivity. Both conditions together suffice independently for $\varprojlim^1 = 0$: Weibel 3.5.7 uses finite-dim; the surjective-transition variant uses Mittag-Leffler in its classical form (images stabilise since they ARE the target at each stage). The theorem deploys both, so the ML argument is robust under weakening either hypothesis.

This is STRONGER than the MC5 Wave-12b heal (cache Pattern 223) which relied on finite-dim only. `thm:recursive-existence` does not share the AP261/AP296 exposure of MC5 Step 3 because it does NOT use a product-decomposition-over-weight argument: the surjections are on the quotient-by-filtration, not on the graded pieces. No AP296 risk.

VERDICT: ML route correctly deployed. No Wave-12b-style vulnerability.

### F4. Class-dependence is absent from the theorem, by design.

`thm:recursive-existence` nowhere mentions classes G/L/C/M. The theorem makes a single uniform claim: pro-object convergence in $\widehat{\gAmod}$. It does NOT claim that the chain-level bar complex $\gAmod$ itself stabilises at finite $N$ for class G/L/C or that any subset of the truncations $\Theta_\cA^{\leq N}$ plateaus.

The class-dependent story is: for class G (Heisenberg, $r=2$), the shadow tower genuinely terminates at degree 2; for class L (affine KM, $r=3$) at degree 3; for class C ($\beta\gamma$, $r=4$) at degree 4; for class M (Vir, W_N), the tower is transfinite and only converges as a pro-object. This distinction lives in `thm:shadow-archetype-classification` and neighbouring results (`prop:sc-formal-iff-class-g`, `prop:depth-gap-trichotomy`), not in `thm:recursive-existence`.

This is a SCOPE CLARITY issue, not a conflation inside the theorem body. The theorem is clean; the surrounding prose and the CLAUDE.md status-table banner ("all-degree inverse limit") do not carry the pro-vs-chain-level distinction audibly, which admits misreading by downstream consumers.

## Phase 3: Attack verdict

Of the four questions, zero surface a proof-body defect. The theorem handles pro-object convergence correctly and unconditionally; the ML argument is robust (both finite-dim and surjective transitions); no class-dependence is claimed or conflated inside the theorem.

The residual finding is SCOPE DISCIPLINE (not a mathematical defect): `thm:recursive-existence` lacks an explicit scope remark distinguishing

- (a) pro-object convergence in $\widehat{\gAmod}$ (what this theorem proves, uniform across all four classes, unconditional);

from

- (b) chain-level termination in $\gAmod$ (class-dependent: G/L/C finite at $r = 2, 3, 4$; class M transfinite).

Without (a)/(b) separation inscribed locally, downstream consumers (25+ `\ref{thm:recursive-existence}` sites in-chapter, plus `prop:depth-gap-trichotomy`) inherit a silent ambiguity: a reader relying on the banner to finish a class-M chain-level argument hits a scope mismatch without warning. This is an AP271-adjacent reverse-drift risk and an AP287 cross-volume-attribution-discipline risk at the same time: the theorem is correct at its stated scope but the scope is not stated explicitly.

Analogous inscription pattern: `rem:mc5-honest-weight-filtration` (MC5 Wave-12b heal, `mc5_class_m_chain_level_platonic.tex`) which distinguishes filtration-preservation from grading-preservation. Here the analogue distinguishes pro-object convergence from chain-level termination.

## Phase 4: Heal

Inscribe `rem:recursive-existence-scope-ambient` immediately after the theorem (following the existing `rem:recursive-existence-clarification`) separating the pro-object claim (unconditional) from chain-level termination (class-dependent, cross-referenced to `prop:depth-gap-trichotomy` and `thm:shadow-archetype-classification`). No downgrade of status tag; the theorem remains `\ClaimStatusProvedHere` at its correct scope.

Edit: add remark block after line 13712 (end of `rem:recursive-existence-clarification`).

## Phase 5: Verification

After inscription:

1. `\ref{rem:recursive-existence-scope-ambient}` is a new label; grep all three volumes for collision before first use (HZ-5). Expected: zero hits, safe.

2. No existing theorem statement is altered; no downstream ref needs retargeting.

3. No AI attribution anywhere; all authorship Raeez Lorgat only.

4. No bulk replace; single block insert. No AP42 risk.

## AP registry entries (reserved block AP861-AP880)

AP861 (CLAIMED): Pro-object-vs-chain-level-convergence scope ambiguity in shadow-tower convergence theorems. When a theorem proves MC convergence in the weight-completion $\widehat{\gAmod}$ without a scope remark distinguishing pro-object convergence (class-uniform) from chain-level termination in $\gAmod$ itself (class-dependent: G/L/C finite at ranks 2/3/4, M transfinite), downstream consumers inherit an unstated ambiguity. Counter: for every inverse-limit MC theorem in a pronilpotent dg Lie setting, inscribe a scope remark naming the ambient ($\widehat{\gAmod}$ versus $\gAmod$), the uniformity (class-uniform for pro-object), and the class-dependent finite-termination status cross-referenced to the archetype classification. Distinct from AP261 (single-vs-bigraded ML — wrong arity of grading), AP296 (exact-weight vs filtration-level bigrading — wrong object of bigrading), AP299 (filtration-type bridge elision): AP861 is a scope-remark omission where the ML machinery is correctly deployed but pro-vs-chain-level ambient is not audibly separated. Related AP271 (reverse drift) at the within-theorem-body level.

Remaining AP862-AP880: unused; release for future waves.

## Cache entry (first-principles-cache)

Pattern 226 (session 2026-04-18). Pro-object limit of an MC element in a pronilpotent weight-filtered dg Lie algebra is class-uniform; chain-level termination in the unfiltered algebra is class-dependent. Trigger: any theorem of the form "$\Theta = \varprojlim_N \Theta^{\leq N}$ exists in $\widehat{\mathfrak{g}}$" without a scope remark separating pro-object convergence (unconditional, follows from exhaustive-separated-complete-pronilpotent filtration) from chain-level termination (finite at rank $r$ for shadow-class of rank $r$; transfinite for class M). Counter-derivation: substitute Virasoro (class M, $r = \infty$) and compute $S_5, S_6, \ldots$ explicitly — the chain-level tower does NOT terminate, yet the pro-object limit exists. Substitute Heisenberg (class G, $r = 2$) and check that $\Theta_\cA^{(g, r \geq 3)} = 0$ — chain-level termination at degree 2. Both are consistent with the same pro-object convergence theorem; only the chain-level rider differs. Primary source: `chapters/theory/higher_genus_modular_koszul.tex` thm:recursive-existence (13520) + prop:depth-gap-trichotomy (18217) + thm:shadow-archetype-classification.

## Audit trail

Loci inspected:
- `chapters/theory/higher_genus_modular_koszul.tex` lines 12650-12790 (definitions), 13480-13720 (theorem + existing clarification), 4033-4094 (input thm:mc2-bar-intrinsic).
- CLAUDE.md Structural Facts paragraph (line ~370 of Structural Facts section) and Theorem Status Theta_A row.

Verdicts:
- Theorem body: CLEAN at its stated (pro-object) scope.
- ML route: ROBUST (belt-and-suspenders, finite-dim + surjective).
- Class-dependence: NOT conflated inside theorem; class-uniform pro-object claim only.
- Scope remark: MISSING — heal by inscription.

No retraction, no downgrade, no status-tag change. Single remark-inscription heal. Report authored by Raeez Lorgat.
