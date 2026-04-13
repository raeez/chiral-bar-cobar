# New Anti-Patterns from 380-Agent Adversarial Campaign (2026-04-12/13)

Source: 105-agent Wave 1 audit + 250-agent Wave 2 deep audit + 25-agent rectification + 37-agent relaunch.
Total unique findings: 463 CRITICAL + 1,055 HIGH = 1,518 actionable items.
Method: GPT-5.4 at xhigh reasoning effort, adversarial falsification mode.

## I. Already Covered by Existing APs (no new AP needed, but evidence reinforces)

These categories are already well-described in CLAUDE.md but the campaign found NEW instances:

| Existing AP | Campaign Count | Notes |
|-------------|---------------|-------|
| AP126/AP141 (bare Omega/z) | 24 CRIT+HIGH | Still the most violated; new instances in standalones and Vol II |
| AP40 (env/tag mismatch) | 134 CRITICAL | Massive: 99 from F20_status_audit alone. Systemic across all chapters |
| AP4 (proof after conjecture) | 71 HIGH | D14 found 70 instances across all volumes |
| AP32 (uniform-weight tag) | 93 findings | D13 found 55 untagged obs_g/F_g formulas |
| AP113 (bare kappa Vol III) | 12 findings | AP14 sweep; still recurring |
| AP124/AP125 (duplicate/misprefix labels) | 51+49 | Systemic across volumes |
| AP29 (AI slop) | 4+ | Residual instances in connections chapters |
| AP176 (arity banned) | 118 | AP16 found 31 CRITICAL + 85 HIGH still in manuscript |
| AP142 (local-global conflation) | 14 | AP20 found 9 CRITICAL instances |
| AP165 (B(A) not SC-coalgebra) | 16 | AP19 found ongoing conflation language |
| AP166 (SC not self-dual) | 6 | AP18 found residual claims |
| AP168 (E_3 topologization naming ban) | 19 | AP17 found the banned label instead of E_3-topological |
| AP132 (augmentation ideal) | 12 | AP04 found T^c(s^{-1}A) without bar |
| AP22 (desuspension direction) | 12 | AP05 found residual +1 instances |
| AP117 (Arnold vs KZ) | 26 | F19 found d log used as connection form |
| AP120 (Cauchy 1/(2pi) missing i) | 19 | F16 found 1/(2pi) without i |
| AP137 (bc/bg swap) | 6 | F08/F09 found sign reversals |
| AP131 (d_gen vs d_alg) | implicit in D08 | Generating depth != algebraic depth confusion persists |
| AP10/AP128 (hardcoded oracles) | 219 | U11 found 61 HIGH test gaps + 157 MEDIUM |
| AP121 (markdown in LaTeX) | 12 | AP12 found backtick numerals |

**Action**: These existing APs are CONFIRMED ACTIVE. Enforcement must intensify. The counts above serve as a recurrence frequency table for prioritising sweeps.

## II. Specialized from Existing APs (existing AP too general, new specialized version)

### AP186: ClaimStatusProvedHere without accompanying proof block.
99 CRITICAL instances from F20_status_audit. The existing AP40 says "environment must match tag" but does not specifically flag ProvedHere theorems that LACK a \begin{proof}. This is the single largest category of CRITICAL findings.
**Rule**: Every \ClaimStatusProvedHere MUST be followed by a \begin{proof}...\end{proof} within 50 lines. If the proof is elsewhere, use \ClaimStatusProvedElsewhere. If no proof exists, downgrade to \ClaimStatusConjectured.
**Grep**: `grep -A50 'ClaimStatusProvedHere' FILE | grep -L 'begin{proof}'`
Evidence: F20_status_audit (99C), U06_incomplete_proofs_v1 (29C).

### AP187: Orphaned chapter files not in \input graph.
62 findings from U14_orphaned_chapters. Files exist in chapters/ but are not \input'd by main.tex. They contribute to page count illusions and stale-content risk.
**Rule**: Every .tex file in chapters/ must be in the \input graph of main.tex, or explicitly commented out with a reason. After any chapter migration or restructuring, verify the \input graph.
**Grep**: Compare `grep '\\input{' main.tex` against `ls chapters/**/*.tex`.
Evidence: U14_orphaned_chapters (4C, 34H).

### AP188: Empty or near-empty sections (<5 lines of content).
49 findings from U08_empty_sections. Section headers with no content create false structural promises.
**Rule**: Every \section{} must contain at least one paragraph of mathematical content or an explicit "This section is under development" remark. Remove empty sections rather than leaving placeholders.
Evidence: U08_empty_sections (14C, 14H, 21M).

### AP189: Dead labels (defined but never referenced).
51 findings from U13_dead_labels. Labels that are never \ref'd are either (a) stale from deleted content or (b) missing their cross-references.
**Rule**: Periodically audit for dead labels. A dead label in a theorem environment suggests the theorem may be unreferenced (structurally orphaned). Do NOT delete without checking cross-volume refs.
Evidence: U13_dead_labels (2C, 17H, 32M).

### AP190: Hidden import — cited result not proved or not proving what's claimed.
44+43+32 = 119 findings from F11/F12/F14 (hidden imports in bar, cobar, higher_genus_foundations). The existing AP2 says "read actual .tex proof" but does not flag the specific pattern: "by Theorem X" where Theorem X either (a) doesn't exist, (b) exists but proves something different, or (c) requires hypotheses not satisfied at the citation site.
**Rule**: Before writing "by Theorem X" or "follows from Proposition Y": (a) verify X/Y exists with grep, (b) read its statement to confirm it proves what you need, (c) verify all hypotheses of X/Y are satisfied in your context. If any fail, the citation is a hidden import.
**Grep after writing**: For each \ref{thm:X} in a proof, verify \label{thm:X} exists and the theorem statement covers the needed claim.
Evidence: F11 (19C, 18H), F12 (25C, 13H), F14 (13C, 19H).

### AP191: Circular proof chain (theorem X cites Y which cites X).
31 findings including 9C from D01_circular_proofs. The existing AP147 describes circular routing but doesn't give a systematic detection method.
**Rule**: After any proof is written, trace the citation chain 3 levels deep. If the same theorem label appears at level 0 and level 3, the chain is circular. Install a ROUTING REMARK (AP147) identifying the non-circular anchor.
**Detection**: For each thm:X, extract all \ref{thm:Y} in its proof, then all \ref{thm:Z} in Y's proof, then check if X appears in Z's proof.
Evidence: D01_circular_proofs (9C, 9H). Most critical: thm:genus-universality ↔ thm:family-index (Theorem D).

### AP192: Scope inflation in theorem statement vs proof.
25 findings from D02_scope_inflation (13C, 7H). The existing AP6/AP7 describe scope issues generically. This specialises: the theorem says "for all g" or "for all families" but the proof only covers specific cases.
**Rule**: After writing any universal quantifier in a theorem statement, verify the proof does not silently restrict to a subset. Grep the proof for "genus 0", "on the Koszul locus", "for affine KM", "at non-critical level" — any such restriction narrows the theorem's scope and must appear in the statement.
Evidence: D02 (13C, 7H). Critical examples: topologization stated universally but proved only for affine KM; Koszul equivalence (vii) stated unconditionally but proved only at g=0.

### AP193: Biconditional (iff) stated but only forward direction proved.
25 findings from D03_biconditional_drift (6C, 16H). The existing AP36 describes this but the campaign found it is SYSTEMIC — 25 instances.
**Rule**: Before writing \iff or "if and only if" in a theorem environment, write a two-line template: "Forward: ... proved in ___. Reverse: ... proved in ___." If the reverse line is blank, write \implies instead.
Evidence: D03 (6C, 16H).

### AP194: Curved complex treated with flat tools.
45 findings from D08_curved_vs_flat (21C, 13H). The existing AP46/AP49 describe curved A-inf and d^2=kappa*omega_g but do not specifically flag the pattern: applying ordinary cohomology, spectral sequences, or base-change theorems to a complex with d^2 ≠ 0.
**Rule**: Before applying H^*, R^*pi_*, spectral sequence, or EGA base change to any complex: verify d^2 = 0 for that complex. If d^2 = kappa*omega_g (curved): must either (a) use the flat piece d_g which IS d^2=0, (b) pass to the coderived category, or (c) restrict to kappa=0.
**Trigger**: Any spectral sequence or cohomology computation on a fiber bar object at genus >= 1.
Evidence: D08 (21C, 13H). Critical: Theorem C0 proof applies ordinary cohomology to curved fiber bar.

### AP195: Five-object conflation in prose.
47 findings from D09_five_objects_discipline (15C, 26H). The existing AP25/AP34/AP50 describe the four-functor discipline but the campaign found ongoing conflation in PROSE (not just formulas): "the bar complex produces the bulk", "Koszul dual equals bar complex", "bar-cobar gives the derived center."
**Rule**: In addition to checking formulas (AP25), audit PROSE around bar/cobar/Koszul/center discussions. Before any sentence mentioning two or more of {bar, cobar, Koszul dual, derived center, bulk}: write the four-object template and verify the sentence correctly distinguishes them.
Evidence: D09 (15C, 26H), XV14_five_objects_xvol (20 findings).

### AP196: SC^{ch,top} misattribution in non-formula contexts.
39 findings from D11_SC_discipline (9C, 23H). The existing AP165 covers B(A)-is-not-SC, but the campaign found subtler misattributions: SC structure described without specifying it lives on the PAIR (C^bullet_ch(A,A), A); topologization described without conformal vector hypothesis; SC^! described without the (Lie, Ass) structure.
**Rule**: Every sentence mentioning SC^{ch,top} must specify: (a) which object it's attributed to (the derived center PAIR, not B(A)), (b) whether topologization is claimed (requires conformal vector), (c) that SC^! = (Lie, Ass, shuffle-mixed), not self-dual.
Evidence: D11 (9C, 23H), AP17 (17 findings), AP18 (6 findings), AP19 (16 findings).

### AP197: Three Hochschild theories conflated in bare "Hochschild" usage.
89 findings from D12_hochschild_disambiguation (1C, 53H, 35M). The existing AP160 defines the three theories but the campaign found 89 instances of bare "Hochschild" without chiral/topological/categorical qualifier.
**Rule**: In mathematical contexts, NEVER write bare "Hochschild" without qualifier. The three theories give different answers: (i) topological HH: E_1→E_2, (ii) chiral ChirHoch: E_inf-chiral→{0,1,2}, (iii) categorical HH: dg cat→E_2+CY. The geometry determines which. Add qualifier at every occurrence.
**Grep**: `grep -rn 'Hochschild' FILE | grep -v 'chiral\|topological\|categorical\|ChirHoch'`
Evidence: D12 (1C, 53H, 35M).

### AP198: Whitehead lemma scope error.
From T08_MC1_PBW (5C). Whitehead's lemma for Lie algebra cohomology applies to finite-dimensional SEMISIMPLE Lie algebras g, not to truncated current algebras, loop algebras, or their modules without additional justification.
**Rule**: Before invoking Whitehead's lemma: verify the Lie algebra in question is (a) finite-dimensional, (b) semisimple. If the argument involves a current algebra g[[t]] or g[t]/t^N: the reduction to g must be made explicit (typically via a weight-graded decomposition where g acts on each graded piece).
Evidence: T08 (lines ~1011, 1027, 1294, 1776 of higher_genus_modular_koszul.tex).

### AP199: Strong filtration inequality direction.
From T11_MC4_completion (5C). The weight filtration on a chiral algebra can be INCREASING (by conformal weight) or DECREASING (by pole order). The strong-tower axiom wt(a*b) >= wt(a)+wt(b) is correct for an INCREASING filtration, but for affine currents J^a_{(n)}J^b with wt = h_a+h_b-n-1, the filtration by conformal weight is NOT multiplicative in the required sense: J^a_{(0)}J^b = [J^a,J^b] has weight 1, not >= h_a+h_b.
**Rule**: Before writing a strong-filtration axiom, verify the inequality direction matches the filtration. For weight-completion arguments on vertex algebras: the filtration by POLE ORDER (decreasing) is typically the correct choice, not conformal weight (increasing).
Evidence: T11 (lines ~1116-1153 of bar_cobar_adjunction_curved.tex).

### AP200: Transfer theorem gap — results on H*(A,m_1) applied to A without comparison.
From T11_MC4_completion. Transferred operations on homology H = H*(A,m_1) are used to conclude facts about the original algebra A without a comparison theorem connecting them.
**Rule**: When using the homological transfer theorem, the transfer data (retraction + homotopy) must be specified explicitly, and any conclusion about A from computations on H requires citing the specific transfer comparison that lifts the result. "H has property P" does NOT automatically imply "A has property P" without the transfer.
Evidence: T11 (lines ~1012-1168 of nilpotent_completion.tex).

### AP201: Baxter spectral constraint not vacuous at lambda=0.
From T10_MC3_thickgen. At lambda=0, the Baxter spectral constraint b = a - (lambda+1)/2 becomes b = a - 1/2, which is NOT vacuous. The constraint restricts to a codimension-1 locus in the (a,b)-plane.
**Rule**: Before claiming a spectral constraint "becomes vacuous" at a special parameter value: substitute and verify. "Vacuous" means the constraint is satisfied for ALL values of the free variables, not merely that one parameter vanishes.
Evidence: T10 (lines ~3071, 3222-3224 of yangians_computations.tex).

### AP202: Coderived category element-wise argument invalid.
From T12_MC5_BV_bar. The coderived category D^co is a Verdier quotient by coacyclic objects, NOT "complexes mod boundaries." An argument that "m_0*x = d^2(x) ∈ Im(d)" does not kill the obstruction in D^co, because curved objects are NOT zero in D^co (the manuscript itself states this elsewhere).
**Rule**: Before arguing "X = 0 in D^co": verify X is coacyclic (= a totalization of a short exact sequence), not merely in Im(d). The coderived category is the correct home for curved dg-modules, but its element-wise calculus differs from the derived category.
Evidence: T12 (lines ~1945 of bv_brst.tex, contradicting ~75 of coderived_models.tex).

### AP203: Class-M harmonic mechanism unproved.
From T12_MC5_BV_bar. The factorization delta_r^harm = c_r(A)*m_0^{floor(r/2)-1} is the ENGINE of the coderived BV/bar comparison for class M, but it appears without proof or citation.
**Rule**: Every mechanism that is the load-bearing step of a theorem must be either (a) proved in situ, (b) proved in a cited lemma, or (c) explicitly flagged as a gap with the theorem's status adjusted to Conditional.
Evidence: T12 (line ~1932 of bv_brst.tex).

### AP204: Genus-0 boundary case contradiction.
From T04_thm_C1. If a theorem claims "for all g >= 0" and produces Q_g(A) ≅ Q_g(A^!)^v, but Q_0(A) = Z(A) ≠ 0 while Q_0(A^!) = 0, the genus-0 case contradicts the duality. This is a BOUNDARY-VALUE failure of a universal claim.
**Rule**: After writing "for all g" or "for all g >= 0": substitute g=0 and verify the claim holds at the boundary. The genus-0 case is the simplest and most constraining; if it fails, add g >= 1 hypothesis.
Evidence: T04 (lines ~476, 694 of thqg_symplectic_polarization.tex).

### AP205: Reflexivity/perfectness assumption hidden in duality construction.
From T04_thm_C1. An involution sigma defined via ev: C_g(A)^{vv} -> C_g(A) requires reflexivity (V^{vv} ≅ V), which requires finite-dimensionality or perfectness of the fiber cohomology. If the theorem claims "no perfectness hypothesis," but the construction uses vv, the hypothesis is hidden.
**Rule**: Before using a double-dual evaluation map: state the reflexivity hypothesis explicitly. "No perfectness" and "uses vv" are contradictory.
Evidence: T04 (lines ~197, 220 of thqg_symplectic_polarization.tex).

### AP206: Object switch mid-proof (Verdier dual ≠ cobar).
From T05_thm_C2. A proof switches from D(bar B(A)) to Omega(A^!) mid-argument. These are different objects: D_Ran(bar B(A)) ≅ (A)^!_inf (Verdier dual of bar = Koszul dual algebra), while Omega(A^!) is the cobar of A^! (= bar-cobar INVERSION applied to A^!). Confusing them invalidates the nondegeneracy argument.
**Rule**: When a proof involves both Verdier duality (D_Ran) and cobar (Omega), verify at each step WHICH object is being used. Write: "At this step the object is [Verdier dual / cobar / bar], because [the preceding step applied D_Ran / Omega / B]."
Evidence: T05 (line ~1940 of higher_genus_complementarity.tex).

### AP207: Center-side vs bar-side lift missing.
From T05_thm_C2. A proposition about center-level eigenspaces Q_g(A), Q_g(A^!) (living in H*(M-bar_g, Z(A))) is cited to conclude bar-side eigenspace properties of L_g = bar B^(g)(A)[1]. No lift from center-level to bar-side is provided.
**Rule**: Results about the center local system Z(A) do NOT automatically lift to the bar complex B(A). The passage Z(A) <- H*(B(A)) requires the bar-center comparison (part of Theorem C0). Cite the comparison explicitly when lifting.
Evidence: T05 (line ~1970 of higher_genus_complementarity.tex).

### AP208: Theorem A Verdier half algebra/coalgebra flip.
From T01_thm_A. The proof defines A^!_inf as a factorization ALGEBRA via D_Ran(bar B), but then the theorem asserts equivalences at the COALGEBRA level (bar B(A_1) ≅ bar B(A_2)), and the proof concludes with "factorization algebra, not coalgebra." The convention flips mid-proof.
**Rule**: In any Verdier-intertwining statement, state ONCE at the beginning whether the equivalence is at the algebra level (post-D_Ran) or coalgebra level (pre-D_Ran), and maintain that convention throughout. The bar B is always a COALGEBRA; D_Ran(bar B) is always an ALGEBRA. Theorem A's Verdier statement should be at the algebra level.
Evidence: T01 (line ~3616 of chiral_koszul_pairs.tex).

### AP209: Missing lemma cited but never proved.
From T01_thm_A. "The bar-degree analogue of Lemma filtered-comparison" is invoked at line ~416 but does not exist anywhere in the repo. This is a MISSING DEPENDENCY that leaves one direction of the Koszul equivalence unproved.
**Rule**: Before citing "the analogue of Lemma X" or "by a similar argument to Proposition Y": verify the analogue is either (a) formally stated and proved, or (b) the similarity is mathematically trivial (not just visually similar). Missing analogues are the most dangerous form of hidden import because they LOOK like complete citations.
Evidence: T01 (line ~416 of chiral_koszul_pairs.tex; repo-wide grep returns only the invocation).

### AP210: Topologization: chain-level vs cohomological conflation.
From T14_topologization. The theorem is stated as proving chain-level E_3, but the proof only establishes [Q,G] = T_Sug + Q-exact, which gives E_3 on Q-COHOMOLOGY. The file itself concedes the chain-level gap at lines 3146-3176. The theorem statement does not reflect this.
**Rule**: When a proof works at the level of Q-cohomology (not cochains), the theorem must state "on H*(−, Q)" explicitly. Chain-level and cohomological results are different mathematical statements. "E_3 on cohomology" ≠ "E_3 on cochains."
Evidence: T14 (lines ~2947, 3307-3311, 3146-3176 of en_koszul_duality.tex).

## III. Genuinely New Anti-Patterns (not specializations of existing)

### AP211: Test file absent for compute engine (test gap).
219 findings from U11_test_gaps. Compute engines in compute/lib/ without matching test files in compute/tests/. This is the LARGEST single finding category by count.
**Rule**: EVERY compute engine file compute/lib/X.py MUST have a matching compute/tests/test_X.py. The test must import the engine, run at least 3 smoke tests with independently verified expected values (AP10/AP128), and pass. No engine without a test file.
**Grep**: `ls compute/lib/*.py | while read f; do test=compute/tests/test_$(basename $f); [ ! -f "$test" ] && echo "MISSING: $test"; done`
Evidence: U11 (1C, 61H, 157M).

### AP212: TODO/FIXME/RECTIFICATION-FLAG left unresolved.
38 findings from U03_todos_v3. Markers left in source indicate incomplete work that may be forgotten.
**Rule**: At session end, grep for TODO, FIXME, HACK, XXX, RECTIFICATION-FLAG across all volumes. Each must be either resolved or converted to an explicit \begin{remark}[Open problem] with a tracked scope.
Evidence: U03 (6C, 21H, 11M). Also found in Vol I and Vol II.

### AP213: Stub chapter (<100 lines, no theorems) contributing to false coverage.
38 findings from U05_stub_chapters_v3. Thin chapters create the illusion of completeness.
**Rule**: Every chapter that is \input'd must contain at least one theorem or proposition environment with a ClaimStatus tag. Chapters under development must be commented out of main.tex with a TODO. The existing AP114 states this but the campaign found 38 instances still active.
Evidence: U05 (3C, 17H, 18M). Also: U04_stub_chapters_v1 (1C, 7H, 11M).

### AP214: Cross-volume bridge claim outdated after rectification.
27 findings from S17_v1_to_v3_bridge (7C, 19H). Vol III cites Vol I theorems with stale scope or status, especially after the topologization split and Koszul equivalence narrowing.
**Rule**: After ANY rectification that narrows scope or changes status of a Vol I theorem, grep Vol II and Vol III for citations of that theorem and update them in the SAME session. The most fragile bridges: Theorem A Verdier scope, topologization scope, MC5 status, Koszul equivalence (vii)/(viii).
Evidence: S17 (7C, 19H). Also: S18_v2_to_v3_bridge (3C, 9H).

### AP215: Preface/introduction advertising stronger than body proves.
28 findings from S07_preface_to_intro (6C, 15H) + 24 from S06_intro_to_body (4C, 12H). The preface or introduction states theorems more broadly than they appear in the actual chapters.
**Rule**: After any theorem scope change, grep preface.tex and introduction.tex for the theorem name/label and verify the advertisement matches the current statement. The introduction is the MOST READ part of the manuscript; scope inflation there is the most damaging.
Evidence: S07 (6C, 15H), S06 (4C, 12H).

### AP216: Koszul equivalence (vii) genus-0 scope.
From T13_koszul_equivs. Equivalence (vii) is listed among the 10 unconditional equivalences but the proof restricts to g=0. The all-genera version is strictly stronger because Virasoro has nonzero delta_F_g^cross.
**Rule**: Each of the 10+1+1 Koszul equivalences must carry an explicit scope (all genera / genus 0 / conditional). If the proof only covers genus 0, the equivalence is genus-0, not unconditional.
Evidence: T13 (lines ~1998-2004 of chiral_koszul_pairs.tex).

### AP217: Koszul equivalence (viii) ChirHoch free-polynomial overclaim.
From T13_koszul_equivs. Equivalence (viii) claims ChirHoch*(A) is a free polynomial algebra with generators in {0,1,2}. The cited Hochschild theorems prove duality and concentration, NOT freeness. The (viii)⇒(v) direction uses this unproved claim.
**Rule**: Distinguish between "ChirHoch is concentrated in {0,1,2} with polynomial Hilbert series" (PROVED, Theorem H) and "ChirHoch is a FREE polynomial algebra" (STRONGER, not proved). The former is about the Hilbert series; the latter is about the algebra structure.
Evidence: T13 (lines ~2005-2008 of chiral_koszul_pairs.tex).

### AP218: SC-formality proof restricted to families with metric.
From T15_SC_formality. The converse proof (class G ⇒ SC-formal) uses C(x,y,z) = kappa(x,[y,z]) as a bilinear form, but kappa is a SCALAR invariant, not a bilinear form. The proof tacitly assumes an invariant metric (Killing form for KM, but absent for betagamma).
**Rule**: SC-formality proofs that use a bilinear form must explicitly state which form and verify it exists for the claimed family. Betagamma has "no metric, no Sugawara construction, no Casimir tensor" (preface.tex:2932).
Evidence: T15 (lines ~2539, 2532 of chiral_koszul_pairs.tex).

### AP219: Depth-gap d_alg=2 witness on wrong parameter line.
From T16_depth_gap. The betagamma witness for d_alg=2 is claimed on a line where the shadow tower vanishes (weight-changing line), contradicting the depth-gap claim.
**Rule**: When citing a specific family as a witness for a depth class, specify the EXACT parameter line/regime. If the shadow tower vanishes on one line but is nonzero on another, the witness is on the nonzero line.
Evidence: T16 (lines ~17115, 16414 of higher_genus_modular_koszul.tex; contradiction with free_fields.tex:1148-1166).

### AP220: D^2=0 proof uses wrong geometric space.
From T18_D2_moduli. The proof works on log FM for a fixed pair (X,D), which only has FM collisions and puncture collisions. But the proof claims curve-degeneration strata, which only exist in the UNIVERSAL FAMILY over M-bar_{g,n}.
**Rule**: When proving a result about moduli-level structure (curve degenerations, stable graph strata), use the universal family over M-bar_{g,n}, NOT the log FM for a fixed smooth curve. A fixed smooth curve does not degenerate; its configuration space only has point collisions.
Evidence: T18 (lines ~30863, 30882 of higher_genus_modular_koszul.tex; configuration_spaces.tex:1251, 1278).

### AP221: Gerstenhaber bracket defined with single insertion only.
From T20_gerstenhaber. The construction of the Gerstenhaber bracket at chiral_hochschild_koszul.tex:4855-4875 gives only a SINGLE insertion-residue sum, not the antisymmetrised pair of insertions that defines a Gerstenhaber bracket. The theorem is tagged ProvedHere but has no actual proof.
**Rule**: A Gerstenhaber bracket {f,g} is defined as f○g - (-1)^{|f||g|} g○f (two insertions, antisymmetrised). A single insertion ○ is a pre-Lie product, not a bracket. Verify both terms are present before claiming a Gerstenhaber structure.
Evidence: T20 (line ~4841 of chiral_hochschild_koszul.tex).

### AP222: Theorem H configuration-space collapse unjustified.
From T07_thm_H. The proof treats ChirHoch^n(A) as if it were D_X-module Ext on the base curve, but the bigraded definition places Hochschild cochains on varying configuration spaces FM_{p+2}(X) of dimension p+2. The collapse from configuration-space Ext to curve-level Ext is not justified.
**Rule**: When claiming concentration of chiral Hochschild cohomology in specific degrees, the proof must account for the configuration-space grading. A spectral sequence or filtration argument that reduces FM_{p+2}(X) contributions to the base curve X is required.
Evidence: T07 (line ~740 of chiral_hochschild_koszul.tex).

### AP223: Theorem H bar-coalgebra/Koszul-dual conflation in proof.
From T07_thm_H. The proof identifies bar B^ch(A)^v with A^! and replaces Omega^ch(bar B^ch(A)) with Omega^ch(A^!). The linear dual of the bar coalgebra is NOT the same as the Koszul dual algebra; the passage requires Verdier duality (not linear dual).
**Rule**: bar B(A)^v (linear dual) ≠ A^! (Koszul dual). The Koszul dual is A^! = ((A^i)^v) where A^i = H*(B(A)). The passage from bar B to A^! goes through bar cohomology, not linear duality. This is the four-functor discipline applied to the Hom computation.
Evidence: T07 (line ~618 of chiral_hochschild_koszul.tex).

### AP224: README/metadata scope inflation.
27 findings from S20_readme_to_manuscript (5C, 10H). README files claim stronger results than the manuscript proves, or cite stale page/test counts.
**Rule**: README claims must be independently verifiable: page counts from fresh build, test counts from `pytest --co -q | tail -1`, theorem status from concordance.tex. After any rectification session, update README in the same session.
Evidence: S20 (5C, 10H).

## IV. New Wrong Formulas (B-list additions)

### B74: Theorem A Verdier stated at coalgebra level.
WRONG: D_Ran(bar B(A_1)) ≅ bar B(A_2) (coalgebra). CORRECT: D_Ran(bar B(A)) ≅ (A)^!_inf (algebra). Evidence: T01, B01.

### B75: "av(r(z)) = kappa" for non-abelian KM without Sugawara qualifier.
Already B11 but found 18 new instances (F14_averaging). The qualifier "for abelian; add dim(g)/2 for non-abelian KM" must be present at EVERY occurrence.

### B76: "ChirHoch*(A) is a free polynomial algebra."
WRONG: only concentration in {0,1,2} and polynomial Hilbert series are proved. Freeness is unproved. Evidence: T13, T07.

### B77: "for all g >= 0" on Q_g duality when Q_0(A^!) = 0.
WRONG at g=0 unless Z(A)=0. CORRECT: "for all g >= 1" or with genus-0 exception. Evidence: T04.

### B78: ProvedHere without proof block.
Not a formula but a structural pattern: 99 instances of \ClaimStatusProvedHere not followed by \begin{proof}. Evidence: F20.

## V. New Failure Modes (FM-list additions)

### FM35: Rate-limit cascade in parallel agent campaigns.
Running >15 concurrent Codex agents hits OpenAI 429 rate limits, causing 70%+ failure rates. Counter: batch size ≤ 5, inter-batch delay 30s.
Evidence: Wave 2 campaign (172/250 failures, all from 429).

### FM36: Agent timeout on files >15,000 lines.
GPT-5.4 at xhigh times out (1200s) when asked to audit or rectify files >15K lines (chiral_koszul_pairs.tex, higher_genus_modular_koszul.tex). Counter: scope the agent to specific line ranges or specific theorem labels, not the whole file.
Evidence: R01, R04 rectification timeouts.

### FM37: Agent confabulation of "vacuous constraint."
GPT-5.4 claimed a spectral constraint "becomes vacuous" at a special parameter without checking. The constraint b=a-1/2 at lambda=0 is not vacuous. Counter: always substitute and verify before claiming a constraint is vacuous.
Evidence: T10 (MC3 Baxter).

### FM38: Agent fails to detect circular proof chains.
Standard audit prompts find local issues but miss multi-hop circularity (A cites B which cites C which cites A). Counter: dedicated proof-chain tracing agents with explicit DAG construction.
Evidence: D01 found 9C circular chains that T-series agents flagged individually but didn't connect.

## VI. Summary Statistics

| Category | New APs | Evidence Count |
|----------|---------|---------------|
| Specialized from existing | AP186-AP210 (25) | ~800 findings |
| Genuinely new | AP211-AP224 (14) | ~500 findings |
| New wrong formulas | B74-B78 (5) | ~130 findings |
| New failure modes | FM35-FM38 (4) | Campaign-level |
| **Total new declarations** | **48** | **~1,430 findings catalogued** |

Remaining ~88 findings are covered by existing APs without need for specialization.

## VII. Additional Anti-Patterns from Mega Rescue + Healing (2026-04-13)

### AP225: Genus-universality gap — the all-genera scalar factorization is NOT proved.
The proof of thm:genus-universality jumps from "one-variable recursion, same propagator, same Hodge bundle" to obs_g = kappa*lambda_g for ALL g, but no cited result proves those hypotheses UNIQUELY FORCE the lambda_g class. The same file (higher_genus_foundations.tex:5730-5776) later states that scalar saturation does NOT determine which genus-g class appears. This means Theorem D parts (i)(a) and (ii) are overstated on the all-genera lane. The genus-1 statement obs_1 = kappa*lambda_1 IS proved. The passage to all genera requires a separate CLUTCHING-UNIQUENESS proposition.
**Rule**: Split all-genera scalar claims into: (a) genus-1 (unconditional), (b) all-genera (conditional on clutching-uniqueness or independent GRR derivation). Never claim all-genera from genus-1 + "same recursion."
**Impact**: Theorem D status, thm:universal-generating-function, concordance, all surfaces advertising "obs_g=kappa*lambda_g for all g."
Evidence: mega_rescue H04, healing H04 (GRR alternative).

### AP226: K_0-class vs scalar confusion.
thm:family-index defines D_A^(g) := kappa(A)*E as a K_0-class, calling it "kappa copies of the Hodge bundle." But kappa is a COMPLEX SCALAR (not an integer), and K_0 requires integer multiplicities. A complex scalar cannot be a bundle multiplicity. The top Chern class does not uniquely determine a K-theory class either.
**Rule**: When defining K_0-classes, the multiplicity must be an integer. If kappa is not an integer, the K_0 interpretation must be replaced by a Chern character / cohomological statement. Delete "K_0-class" language and use the scalar GRR/Faber-Pandharipande identity directly.
Evidence: mega_rescue concordance agent, lines concordance.tex:5939-5947.

### AP227: ProvedHere forwarding — "proof" is just "By Theorem X."
Propositions/corollaries tagged ClaimStatusProvedHere whose proof block consists entirely of "By Theorem X" or "Follows from Theorem X" are NOT ProvedHere — they are ProvedElsewhere (in Theorem X). This creates false coverage: the proof surface appears complete but the actual work is in the forwarded theorem. Found in: prop:genus-g-curvature-package part (iv), cor:kappa-additivity, thm:universal-generating-function.
**Rule**: If the entire proof body is a single citation, use ClaimStatusProvedElsewhere. If the proof combines multiple results, ProvedHere is appropriate. A proof that says "By Theorem X and Lemma Y, the result follows by Z" is ProvedHere. A proof that says only "By Theorem X" is ProvedElsewhere.
Evidence: mega_rescue, higher_genus_foundations.tex:514-633, :5893.

### AP228: Anomaly-Koszul dependency inversion.
Theorem D cites thm:anomaly-koszul for general kappa additivity, but thm:anomaly-koszul is about the matter-ghost system and itself imports additivity from cor:kappa-additivity. The dependency is backwards.
**Rule**: Check dependency direction before citing. If Theorem X cites Corollary Y, do not cite Theorem X to prove Corollary Y. The correct direction: cor:kappa-additivity proves additivity; thm:anomaly-koszul specializes to matter-ghost.
Evidence: mega_rescue, higher_genus_modular_koszul.tex:2741-2744.

### AP229: SC-formality propagation debt across compute libraries.
Vol III compute libraries (swiss_cheese_cy3_e1.py:62-74) still carry the older "class G/L SC-formal" claim, which conflicts with the updated proof surface (class G ONLY). Any update to the SC-formality proof must be mirrored in: concordance, metadata, standalone summaries, Vol II prefaces/bridges, Vol III compute libraries.
**Rule**: After updating any classification result (G/L/C/M membership, SC-formality, depth), grep ALL compute libraries across all three volumes for hardcoded copies of that classification. Update them in the same session.
Evidence: mega_rescue healing, Vol III swiss_cheese_cy3_e1.py.

### AP230: Genus-1 sufficient but claimed all-genera.
Multiple theorems are stated "for all g" but their proofs only use genus-1 data. The passage from genus-1 to all genera is the universality gap (AP225). Affected: Theorem D, thm:universal-generating-function, cor:kappa-additivity (which only needs genus-1 curvature but cites all-genera universality).
**Rule**: When a proof only needs genus-1, cite the genus-1 result. Do not route through thm:genus-universality if only obs_1=kappa*lambda_1 is needed. This eliminates unnecessary dependence on the universality gap.
Evidence: mega_rescue, higher_genus_foundations.tex:5893-5894.

### AP231: Draft artifacts in theorem statements.
Raw markers like \textup{(LOCAL)} remain inside theorem/proposition statements. These are drafting artifacts, not mathematical scope qualifiers.
**Rule**: Grep for \textup{(LOCAL)}, \textup{(DRAFT)}, \textup{(TODO)}, and similar markers in theorem/proposition environments. Remove or replace with proper scope language.
Evidence: mega_rescue, higher_genus_foundations.tex:5312,594,4541,4545.

### AP232: Duality clause overclaiming family scope.
The duality clause of Theorem D says "affine KM and free-field algebras" but the proof only covers affine KM + principal W_N. The general W(g,f) statement is only the principal embedding, not general f. "kappa=0 iff critical level" is unscoped and wrong for W-algebras (where kappa=0 iff c=0).
**Rule**: Narrow duality clauses to the families ACTUALLY proved. Specify: "For affine KM, kappa=0 iff k=-h^v. For principal W^k(g,f_prin) at generic level, kappa=0 iff c=0." Do not merge these into a single unscoped statement.
Evidence: mega_rescue, higher_genus_modular_koszul.tex:2703-2716.

### AP233: Compact/completed comparison gap in MC3.
The shifted prefundamental generation (MC3) proves thick generation on finite-dimensional strata, then claims it extends to compact objects of the completed category. The extension to the completed/coderived MC3 domain is explicitly marked as conjectural in the same file. The gap is: the lift-and-lower (Lemma L) filtration needed to upgrade the ℓ-weight multiplicity-free decomposition to the derived shifted category.
**Rule**: When claiming generation in a COMPLETED category from generation in a BOUNDED subcategory, cite the specific compact-generation theorem that lifts the result. If no such theorem exists, mark the extension as conditional.
Evidence: mega_rescue, yangians_computations.tex:3068-3335, conj:rank-independence-step2.
