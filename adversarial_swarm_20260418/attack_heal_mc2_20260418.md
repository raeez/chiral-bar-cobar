# MC2 + H06 attack-and-heal (2026-04-18)

Author: Raeez Lorgat.

Target: `thm:mc2-bar-intrinsic` (Vol I `chapters/theory/higher_genus_modular_koszul.tex:4033`) and its advertised alternative H06 (Kontsevich--Soibelman scattering diagram) at `rem:mc2-scattering-diagram` (same file, line 4421).

AP block: AP741-AP760 reserved per mission.

## Mission findings (four questions)

### (i) Where is `thm:mc2-bar-intrinsic` and what does "all-degree convergence" mean?

Canonical inscription: `chapters/theory/higher_genus_modular_koszul.tex:4033-4094` (statement), `:4096-4267` (proof). Secondary convergence witness at `thm:recursive-existence`, same file `:13510-13677`. Phantom/secondary labels exist in `chapters/connections/concordance.tex`, `chapters/theory/introduction.tex`, and cross-volume in Vol II `main.tex:715` (phantomsection). Only the Vol I inscription at `:4033` is load-bearing.

Statement (four clauses):
- (i) $\Theta_\cA := D_\cA - d_0$ is MC in the coinvariant modular convolution dg-Lie algebra $\gAmod \cong \operatorname{Def}^{\mathrm{cyc}}(\cA)\widehat{\otimes}\mathcal{G}^{\mathrm{mod}}$.
- (ii) Scalar trace: genus-1 unconditional, all-genus on the UNIFORM-WEIGHT lane.
- (iii) Clutching factorization across separating / non-separating boundary strata of $\overline{\mathcal{M}}_{g,n}$.
- (iv) Verdier duality: $\mathbb{D}(\Theta_\cA) = \Theta_{\cA^!}$.

"All-degree convergence" is defined twice in the chapter, at two DIFFERENT levels of resolution, and the CLAUDE.md status-table claim "All-degree convergence PROVED" compresses both into one unqualified banner. The two meanings:

**Meaning A (weight-filtration pronilpotent limit, PROVED unconditional).** `thm:recursive-existence` Step 4 (`:13616-13663`) constructs $\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ as the inverse limit of the compatible system $\{\Theta_\cA^{\leq N}\}$ in the weight-filtration quotients $\gAmod / F^{N+1}\gAmod$, where $w(g,r,d) = 2g-2+r+d$ (`def:weight-filtration-tower`, `:12665-12700`). Each transition is a surjection of finite-dimensional vector spaces (graph-finiteness bound $|V(\Gamma)| \leq 2g-2+n$, $|E(\Gamma)| \leq 3g-3+n$ from `thm:stable-graph-pronilpotent-completion`, `:14016`); Mittag-Leffler is satisfied in its strongest form (surjective transitions ⇒ $\varprojlim^1 = 0$); the limit is a complete Hausdorff pronilpotent dg-Lie algebra (Goldman-Millson / Manetti standard setup). This meaning of "all-degree convergence" is genuinely proved unconditional.

**Meaning B (chain-level convergence of the recursive shadow in $\gAmod$, NOT $\widehat{\gAmod}$).** The shadow obstruction tower `def:shadow-postnikov-tower` (`:12718-12780`) defines $\Theta_\cA^{\leq 2}, \Theta_\cA^{\leq 3}, \ldots$ and states the tower condition (compatibility under quotient maps). The limit $\Theta_\cA$ lives in $\widehat{\gAmod}$, NOT in $\gAmod$ on the nose. Termination at finite degree (`d_{\mathrm{alg}} < \infty$) is a CLASS property: class G ($d_{\mathrm{alg}}=0$: Heisenberg), class L ($d_{\mathrm{alg}}=1$: affine KM), class C ($d_{\mathrm{alg}}=2$: $\beta\gamma$, Virasoro c=1 lane); class M ($d_{\mathrm{alg}}=\infty$: generic Virasoro, principal $\mathcal{W}_N$) does NOT terminate and lives only in the completed space. The depth-gap trichotomy (`prop:depth-gap-trichotomy`) proves no family has $d_{\mathrm{alg}} = 3$.

So "all-degree convergence" in the CLAUDE.md Structural Facts section should read: convergence AS PRO-OBJECT LIMIT in $\widehat{\gAmod}$, unconditional; TERMINATION at finite degree in $\gAmod$, class-dependent (finite for G/L/C, genuinely transfinite for M). The two are distinct facts; the bar-intrinsic MC element $\Theta_\cA$ itself is always a completed-limit object.

### (ii) Does the $\Theta_\cA$ recursion terminate at finite degree?

Directly answered in `rem:mc2-bar-intrinsic-perspective` (`:4568-4615`), which is the most honest passage in the chapter:

> "Even in the one-channel regime ($\dim H^2_{\mathrm{cyc}} = 1$: Heisenberg, affine Kac-Moody, Virasoro, principal $\mathcal{W}_N$), the chain-level MC element $\Theta_\cA = D_\cA - \dzero$ has components at ALL DEGREES... Scalar saturation guarantees that these shadows are DETERMINED by $\kappa$ and the structural constants, NOT that they vanish. The tower terminates at different degrees for different families (Heisenberg at 2, affine at 3, $\beta\gamma$ at 4; Virasoro at $\infty$)."

So:
- Class G: $\Theta_\cA$ supported in degree 2 only ($\kappa$ and nothing higher). Recursion terminates after ONE step.
- Class L: supported in degrees $\{2,3\}$. Cubic shadow $\mathfrak{C}$ nonzero; degree 4 zero.
- Class C: supported in degrees $\{2,3,4\}$. Quartic resonance $\mathfrak{Q}$ nonzero; degree 5 zero.
- Class M: unbounded support. Genuine pro-object limit.

The inverse limit is GENUINELY NEEDED for class M. For G/L/C it is a trivial limit that stabilises after finitely many steps. The $\Theta_\cA$ construction is uniform (it is the positive-genus part of $D_\cA$, not a case-by-case recursion), so there is no family-specific gain from early termination; the uniformity is itself the theorem.

### (iii) Is convergence pro-object or chain-level? Filtration-vs-grading check (AP296 companion).

Pro-object convergence in $\pro\text{-}Ch(\Vect)$, NOT chain-level in $Ch(\Vect)$. Specifically:

- The ambient $\widehat{\gAmod}$ is defined as $\varprojlim_N \gAmod / F^{N+1}\gAmod$ (`def:weight-filtration-tower:12692`, `thm:recursive-existence` Step 4(c) `:13645`).
- The weight filtration $F^N$ is indexed by $w(g,r,d) = 2g-2+r+d$, a COMBINATORIAL / OPERADIC weight (stability exponent of stable graphs), NOT the OPE conformal weight on bar-words that AP296 forbids bigrading by.
- AP296 cross-check: is this MC2 construction exposed to the Wave-14 weight-preservation fallacy? Answer: NO. The AP296 failure mode is "bar differential on bar-words drops conformal weight via simple-pole summands"; the MC2 weight filtration is OPERADIC (Euler-characteristic of stable graphs), not conformal-weight on bar-words. The bracket `$[F^{N_1}, F^{N_2}] \subseteq F^{N_1+N_2-2}$` at `:12697` is the standard operadic degree-gluing shift, and the differential preserves the filtration because edge contraction cannot decrease $2g-2+n$ (see `thm:stable-graph-pronilpotent-completion` proof at `:14051-14065`). MC2 is filtration-preserving on the right filtration; MC5 class-M chain-level was filtration-preserving on a wrong filtration (exact OPE weight) and was healed via the FILTRATION-level bigrading at `prop:standard-strong-filtration`. No AP296 propagation.
- Mittag-Leffler quality: SURJECTIVE-transitions ML (Step 4 at `:13620-13625`), the strongest form. No $\varprojlim^1$ gap.

Verdict: pro-object convergence is clean. The claim "chain-level MC element" in `rem:mc2-bar-intrinsic-perspective:4595` is HONESTLY SCOPED: it says $\Theta_\cA$ has components at all degrees, not that those components assemble to a chain-level object in $Ch(\Vect)$; the assembly is in $\pro\text{-}Ch(\Vect)$ via the weight filtration.

One load-bearing but unqualified claim: Step 2 of `thm:recursive-existence` (`:13569-13603`) writes "the bar-intrinsic construction... produces a canonical MC element $\Theta_\cA$ in the COMPLETED algebra $\widehat{\gAmod}$". This is correct. The downstream claim in `rem:non-circular-logical-chain` (`:4665-4719`) Tier 1 and the CLAUDE.md status-table "All-degree convergence PROVED" are honestly in $\widehat{\gAmod}$.

### (iv) H06: inscribed or remark? Support-property comparison open?

H06 is a REMARK, not a theorem. Specifically `rem:mc2-scattering-diagram` (`:4421-4505`) and its companion `rem:v1-mc2-ks-comparison` (`:4507-4566`). Status declared honestly in both:

`:4501-4504`: "The missing manuscript-level input is the full construction of the scattering diagram attached to $\cA$ together with the comparison between its wall data and the primitive shadows extracted from $D_\cA$. Once that package is installed, it gives a redundant proof path to MC2."

`:4553-4564`: "The missing theorem is the construction, for an arbitrary modular Koszul chiral algebra $\cA$, of a KS support-property package whose ray data are exactly the primitive shadows extracted from $D_\cA$. Until that comparison is proved, `thm:mc2-bar-intrinsic` remains the primary proof of MC2 and `rem:mc2-scattering-diagram` is a redundant route only at the level of a sketched alternative."

So H06 is a proof SKETCH. The CLAUDE.md status-table row "MC2 ALT H06 (KS scattering) conditional on support-property comparison (open)" matches source — the word "conditional" understates; H06 is more accurately "SKETCHED" with two missing packages:

1. **Construction package.** For each modular Koszul chiral algebra $\cA$, construct the central-charge map $Z : \bigoplus_r \mathbb{Z} e_r \to \mathbb{C}$ and the primitive wall data $\{\sigma_r\}$. The central-charge map is free in the current formulation (no canonicalisation).
2. **Comparison package.** Verify that the wall data satisfies the KS support property (Kontsevich-Soibelman 2008, Def. 1 + Remark 1), which gives a discrete active-charge set with polynomial density in the central-charge plane. This is the "support property" the CLAUDE.md row names.

The shadow asymptotic bound $|S_r(L)| \sim A(L)\,\rho_L^r\,r^{-5/2}$ from `thm:shadow-radius`(ii) is stronger than the KS polynomial-density support property; it already gives local finiteness on autonomous primary lines. But on a general modular Koszul chiral algebra without a T-line restriction, whether the primitive shadows satisfy the KS support property is OPEN. This is the precise content of the "support-property comparison" phrase in CLAUDE.md.

The KS comparison remark is CAREFULLY scoped: it claims structural match (MC element ↔ log of sector-element product; BPS phase order ↔ product order; MC equation ↔ infinitesimal factorization), NOT an identification of Lie algebras. "Convention check: KS work with a lattice Lie algebra and its pronilpotent group; this chapter works with the completed modular convolution dg Lie algebra $\widehat{\gAmod}$. The match is structural, not an identification of Lie algebras." (`:4523-4526`).

What CLAUDE.md gets right and wrong on the H06 row:
- CORRECT: "KS scattering; conditional on support-property comparison (open)".
- UNDERSTATED: H06 is a REMARK, not an inscribed alternative theorem. "MC2 ALT H06" in the status-table "Alternative Proofs Secured" block suggests an inscribed alternative; the inscription is a sketch with two named missing packages. Closer CLAUDE.md language: "MC2 alt H06 (KS scattering): SKETCHED at `rem:mc2-scattering-diagram`; central-charge + support-property comparison uninscribed".

## Atoms of honest status

| Aspect | Claim in CLAUDE.md status-table | Inscribed truth | Heal |
|---|---|---|---|
| MC2 bar-intrinsic | PROVED | PROVED at `thm:mc2-bar-intrinsic` with 4-pillar proof chain (F1-F4) | Unchanged |
| All-degree convergence | PROVED (unqualified) | PROVED as pro-object limit in $\widehat{\gAmod}$; class-dependent termination in $\gAmod$ | Qualify: "pro-object limit in $\widehat{\gAmod}$; class-dependent chain-level termination in $\gAmod$" |
| $\Theta_\cA$ at all degrees | Implicit | EXPLICITLY present at all degrees for class M; determined by $\kappa$ + structural constants on one-channel | Unchanged |
| MC2 alt H06 | conditional on support-property comparison (open) | SKETCHED at remark level; two missing packages (central-charge canonicalisation + KS support property) | Rename "conditional" → "sketched; support-property + central-charge comparison OPEN" |
| Filtration used | Not stated | $w(g,r,d) = 2g-2+r+d$ (Euler-characteristic operadic weight, NOT OPE conformal weight) | Note AP296 cross-check: MC2's filtration is the RIGHT filtration for ML; no class-M drift |
| Mittag-Leffler quality | Not stated | Surjective-transitions ML (strongest form) at `thm:recursive-existence` Step 4 | Note "ML in its strongest form (surjective transitions)" |

## Patch plan

Two minimal edits to CLAUDE.md:

1. **Structural facts section** (line 584-604 approx): qualify "All-degree convergence PROVED" with pro-object/completed-limit scope, and add an AP296 cross-check note that the operadic weight filtration $w(g,r,d) = 2g-2+r+d$ is distinct from the OPE conformal weight that AP296 forbids.

2. **Alternative Proofs Secured table** (line ~735, "H06" row): rename "KS scattering diagram" status from "conditional on support-property comparison (open)" to "SKETCHED at `rem:mc2-scattering-diagram`; two uninscribed packages (central-charge canonicalisation + KS support-property comparison per Kontsevich-Soibelman 2008 Def. 1 + Remark 1)".

Also: add a scope remark to the manuscript at `rem:mc2-bar-intrinsic-perspective` (line 4589 area) making the pro-object-limit-vs-chain-level distinction explicit. The honesty is already in prose; the remark should state the distinction in terms of the ambient category ($\pro\text{-}Ch(\Vect)$ vs $Ch(\Vect)$). This avoids a future AP271 reverse-drift (CLAUDE.md lagging manuscript) or AP256 aspirational heal.

No theorem downgrades required. MC2 proof is structurally sound; the heal is SCOPE QUALIFICATION, not retraction.

## New anti-patterns surfaced

**AP741 (Pro-object-limit-vs-chain-level ambient drift in MC status-table).** Status-table row reads "all-degree convergence PROVED" without naming the ambient category. For a class-M chiral algebra, $\Theta_\cA$ exists as an object in $\pro\text{-}Ch(\Vect)$ (pro-object over the weight filtration), NOT in $Ch(\Vect)$ on the nose; the MC equation holds in the completed dg-Lie algebra $\widehat{\gAmod}$, not in $\gAmod$. Bare "all-degree convergence" invites confusion with chain-level existence of the positive-genus MC element as a genuine chain complex, which is FALSE for class M (infinite support, no termination) and only TRUE for class G/L/C. Counter: every convergence status claim must name the ambient category and the limit mechanism (inverse limit, filtered colimit, bar-length completion, etc.). Distinct from AP296 (weight-preservation fallacy on bar differentials where OPE simple-pole summands strictly drop weight): AP296 catches a specific bigrading error; AP741 catches the broader practice of stating chain-level results without ambient-category qualification. Related: AP261 (single-index ML vs bigraded ML — correct arity of grading), AP258 (cohomological-vs-chain status drift — correct level of resolution). AP741 is the ambient-category sibling.

**AP742 (Alt-proof SKETCHED mislabelled as "conditional").** The "Alternative Proofs Secured" block in CLAUDE.md lists H06 (KS scattering) as "conditional on support-property comparison (open)". The word "conditional" invites a reader to treat H06 as a proof waiting on a single missing input. The source reality is a REMARK with a PROOF SKETCH and TWO uninscribed packages: (a) construction of the central-charge map $Z$ (free variable in current formulation, no canonicalisation), and (b) comparison between primitive shadows and KS support property (Kontsevich-Soibelman 2008, Def. 1 + Remark 1). "Conditional" silently promotes "sketched remark with two open packages" to "theorem waiting on one lemma". Counter: for every "Alternative Proofs Secured" entry, distinguish INSCRIBED (theorem body exists, cited lemma missing), SKETCHED (remark with named missing packages), CONJECTURAL (scaffolding only, no proof trajectory), and PROPOSED (mentioned in passing, no construction). Apply to ALL eleven H-rows in the Alternative Proofs Secured block; several may be sketched-not-secured. Distinct from AP280 (three-step epistemic inflation: remark → standalone → headline): AP742 is inflation-within-status-table, from "sketch in a remark" to "conditional alt-proof" in a single banner without propagation to a standalone. Related: AP255 (phantom-file), AP305 (pessimistic drift — AP742 is optimistic-drift sibling at the alt-proof layer).

## Independent-verification note (HZ-IV)

MC2 carries two genuinely disjoint proof paths to its core identity (i):

Path A (BAR-INTRINSIC): $D_\cA^2 = 0$ at operadic level (`thm:convolution-d-squared-zero`, ultimately from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$ codim-2 stratification), expanded at $D_\cA = d_0 + \Theta_\cA$ gives MC.

Path B (RECURSIVE LIFT): weight-filtration Mittag-Leffler on surjective finite-dim transitions, obstruction classes $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanish at each $N$.

Path A supplies the element; Path B constructs the tower and shows the limit exists. They are NOT disjoint (Path B's Step 2 uses Path A to produce the MC element that projects to the tower). This is `thm:recursive-existence:13569-13603`. For a clean HZ-IV two-path decoration, one needs a path that constructs the tower WITHOUT appealing to $D_\cA^2 = 0$ (e.g., the KS scattering path IF the support-property package is installed); H06 is therefore the natural HZ-IV disjoint partner, and this motivates closing the support-property comparison even though MC2 itself is already proved.

A third path via Costello-Gwilliam factorization homology (H08, adjacent in the table) would give a second genuinely disjoint construction. H08 is also a remark; same inscription obligation.

## Summary

MC2 core theorem is structurally sound. The heal is SCOPE QUALIFICATION in CLAUDE.md (pro-object-limit semantics, AP296 cross-check note, H06 "SKETCHED" rather than "conditional"), plus a one-sentence scope remark in the manuscript at `rem:mc2-bar-intrinsic-perspective` making the $\pro\text{-}Ch$ vs $Ch$ distinction explicit. Two new anti-patterns (AP741, AP742) for programme-wide use. No theorem downgrades. No commit.

Patch file: `adversarial_swarm_20260418/patches/mc2_20260418.patch`.

## Files touched (planning only; no commit)

- `CLAUDE.md` Structural Facts section (qualification of "all-degree convergence")
- `CLAUDE.md` Alternative Proofs Secured table (H06 rename)
- `CLAUDE.md` AP section (append AP741, AP742)
- `chapters/theory/higher_genus_modular_koszul.tex` `rem:mc2-bar-intrinsic-perspective` area (scope remark; one sentence)

No AI attribution anywhere.
