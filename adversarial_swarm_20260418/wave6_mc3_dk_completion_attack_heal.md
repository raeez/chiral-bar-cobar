# Wave 6 (2026-04-18) — Compact-completed MC3 comparison + conj:dk-compacts-completion scope

Target: Vol I `chapters/theory/compact_completed_mc3_comparison_platonic.tex` (666 lines, whole-file linear read completed in 250-line chunks).

Cross-reads: `chapters/theory/mc3_five_family_platonic.tex` (MC3 primary), `chapters/examples/yangians_computations.tex` (four conjectures inscribed at :2817, :3420, :3937, :4674; `thm:mc3-type-a-resolution` at :4165), `chapters/theory/en_koszul_duality.tex` (`thm:e3-identification` :5338, `rem:e3-non-simple` :5541, `rem:e3-non-simple-gl-N` :5576).

## Audit verdicts

- **Phantom-ref check**: `thm:e3-identification` + `rem:e3-non-simple` + `rem:e3-non-simple-gl-N` all resolve; the Wave-4 `thm:e3-identification-reductive` phantom-ref heal (retarget to rem:e3-non-simple/-gl-N) has LANDED. No AP255 residual in this file.
- **Conjecture inscription**: `conj:dk-compacts-completion` (yangians_computations.tex:3937), `conj:rank-independence-step2` (:3420), `conj:mc3-automatic-generalization` (:4674), `conj:mc3-sectorwise-all-types` (:2817), `thm:mc3-full-DK-conjectural` (mc3_five_family_platonic.tex:573), `thm:mc3-evaluation-core-five-family` (mc3_five_family_platonic.tex:102) — all inscribed as live labels with ClaimStatus tags.

## Findings (severity MEDIUM/HIGH)

- **F1 (MEDIUM; AP241/AP260) — Drinfeld-centre compatibility overclaim.** File:322-326 `rem:compatibility-drinfeld-centre` asserted "derived centre inherits E_3 structure that RESPECTS the truncation filtration" and named an unlabelled functor "Φ_DK". Neither `thm:e3-identification` nor the `rem:e3-non-simple(-gl-N)` pair proves respect-for-truncation-filtration; the statement is aspirational.
- **F2 (HIGH; AP255/AP266) — Type-A conjecture "resolution" overclaim.** File:389-404 `rem:type-A-completion-conjecture-resolved` claimed `conj:dk-compacts-completion` IS PROVED IN TYPE A via Kashiwara-Vasserot + KL-Finkelberg. But the conjecture concerns full $\mathrm{DK}_{\mathfrak{sl}_N}$ compact-identification; KL-F identifies the COMPLETED ambient, not the full DK. The remark resolves a different statement and labels it "the conjecture". Aspirational-heal drift.
- **F3 (MEDIUM; AP249) — "Uniform across five families" without filtration audit.** File:176-181 proof of clause (iii) asserted uniform $L_0$-truncation for all five families. Elliptic Yangians $E_{\rho,\eta}(\mathfrak{sl}_N)$ do not carry a global conformal vector; the theta-divisor height filtration plays $L_0$'s role, which is substitution (genuine extra work), not verbatim inheritance. Twisted BCD reflection-equation weight is a second substitution.
- **F4 (LOW; AP277) — HZ-IV decorators prose-only.** The three decorators (rem:hziv-decorator-*) carry sound disjoint_rationale but no wired test in `compute/tests/`. Structurally correct; marked as a follow-up inscription target, not a current violation (tautology body check N/A since no body exists).

## Surviving core (Drinfeld-tone)

The honest theorem is: **the evaluation-generated core is dense in the truncation-completed DK category, and thick generation lifts to the completed ambient by Neeman/Lurie**. This is an AMBIENT UPGRADE, unconditional for the three families (rational type A, uniform simple $\mathfrak{g}$, super $\mathfrak{gl}_{m|n}$) where $L_0$-grading is canonical; for twisted BCD and elliptic the truncation topology substitutes a different grading (reflection-equation weight; theta-divisor height), and the density + PBW argument applies once the substitution is made. Full-DK identification ($\mathrm{DK}^{\mathrm{completed}} \simeq \mathrm{DK}$) is a SEPARATE question; in type A it REDUCES to a single compact-object check (Neeman-Bondal-VdB) via KL-F, which is open.

## Heals inscribed in target file

- **H1 (F1)**: rewrote `rem:compatibility-drinfeld-centre` to scope-qualify compatibility to the abstract derived-centre level; dropped "respects the truncation filtration" and "Φ_DK" functor rhetoric; pointed to `sec:mc3-platonic-full-DK-conjectural` as the honest scope-articulation site. Status: ProvedHere at abstract level; truncation compatibility explicitly marked unverified in this chapter.
- **H2 (F2)**: rewrote `rem:type-A-completion-conjecture-resolved` as "Type-A reduction to a single compact-object check". Status: ProvedHere (reduction) + Conjectured (full-DK upgrade). Added AP266 sharpened-obstruction falsification test: exhibit a compact object of $\mathrm{DK}_{\mathfrak{sl}_N}$ not in the essential image of the completed category. Status table split into two rows accordingly. Coherence remark `rem:coherence-concordance-mc3-completed` rewritten to match.
- **H3 (F3)**: rewrote clause (iii) proof of `thm:compact-completed-mc3-comparison`; inscribed new `rem:per-family-truncation-filtrations` listing the canonical $L_0$-families (rational type A, uniform simple $\mathfrak{g}$, super $\mathfrak{gl}_{m|n}$) and the substituted-filtration families (twisted BCD reflection-equation weight; elliptic theta-divisor height). Density + PBW argument applies verbatim once the substitution is made.
- **H4 (F3)**: updated F3 falsification test in `rem:falsification-plan-comparison-gap-completed` to match the honest reduction-not-resolution framing.

## Commit plan (owner-authorised only)

All edits are in one file, `chapters/theory/compact_completed_mc3_comparison_platonic.tex`. Suggested single commit title: "Vol I Wave-6 MC3 completed-ambient scope honesty: reduction-not-resolution in type A + per-family truncation filtrations". Follow-up inscription targets: (a) `test_compact_completed_mc3_comparison.py` wiring the three HZ-IV decorators to `theorem_mc3_kl_rectification_engine` + `theorem_concordance_rectification_engine`; (b) CLAUDE.md MC3 row update — current row text "Extension to full DK_g unconditional only in type A modulo conj:dk-compacts-completion" is already accurate; no change needed.

## AP catalogue residual

No new AP surfaced in this wave. The pattern (chapter-level aspirational heal that promotes a conjecture-environment label via a remark) is already catalogued as AP256 aspirational-heal-status-drift; this wave is a concrete propagation of AP256 into completed-ambient scope claims, healed by AP266 sharpened-obstruction reframing.
