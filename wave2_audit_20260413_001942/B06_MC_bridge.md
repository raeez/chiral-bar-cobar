# B06_MC_bridge (589s)

- [CRITICAL] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1943), [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1981), [Vol I README.md](/Users/raeez/chiral-bar-cobar/README.md:26) — PROBLEM: the canonical source says MC5 is only partially proved: analytic HS-sewing and coderived BV=bar are proved, but the genuswise chain-level BV/BRST/bar identification remains conjectural. The README still says “All five master conjectures MC1-MC5 are proved,” and it also flattens MC3 into a type-A/non-type-A split instead of the evaluation-core/post-core split recorded in the concordance. FIX: replace the whole README sentence with: `MC1 through MC4 are proved. MC3 is proved for all simple types on the evaluation-generated core; the post-core MC3c packet is unconditional in type A and conditional outside type A. MC5 is partially proved: analytic HS-sewing at all genera, the genus-0 algebraic BRST/bar comparison, and D^{co}-level BV=bar for all shadow classes are proved; the genuswise chain-level BV/BRST/bar identification remains conjectural (class M chain-level false), and the tree-level amplitude pairing is conditional.`

- [CRITICAL] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1850), [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1985), [Vol III introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:391), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:181), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:201), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:581) — PROBLEM: Vol III upgrades MC3 from “proved on the evaluation-generated core; DK-4/5 downstream” to “full categorical equivalence,” “horizontal equivalence at the level of compact objects,” and “reconstruction solved.” That is broader than the live Vol I status surface. FIX: narrow every one of these to the evaluation-generated core. Concretely: at `introduction.tex:391` replace `MC3 for all simple types` with `MC3 on the evaluation-generated core for all simple types, with extension beyond evaluation modules deferred to DK-4/5`; at `quantum_group_reps.tex:181-183` replace `extends this to the full categorical equivalence` with `extends this to the evaluation-generated-core DK comparison`; at `quantum_group_reps.tex:201-202` replace `at the level of compact objects` with `on the evaluation-generated core`; at `quantum_group_reps.tex:581-583` replace `solved ... uniquely determines the chiral algebra` with `partially reconstructed on the evaluation-generated core; the full post-core extension is the downstream DK-4/5/completion packet`.

- [HIGH] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:81), [Vol I higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10566), [Vol III modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:29), [Vol III modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:33) — PROBLEM: Vol III cites “Vol I Theorem MC3” for the strict dg-Lie/\(L_\infty\) comparison and “Vol I Theorem MC4” for MC-moduli coincidence. That is a wrong dependency map: MC3 is the categorical Clebsch-Gordan package, MC4 is completion towers, while the strict-model statement lives in `thm:modular-homotopy-convolution`. FIX: at line 29 replace the parenthetical with `Vol~I, Theorem~\ref*{V1-thm:modular-homotopy-convolution}`; at line 33 replace the first two sentences with `The strict dg Lie / L_\infty comparison, and the coincidence of Maurer--Cartan moduli for the strict model and the homotopy-invariant deformation object, are the content of Vol~I Theorem~\ref*{V1-thm:modular-homotopy-convolution}. The one-slot warning is the separate RNW19 bifunctoriality obstruction recorded in Vol~I's three-pillar constraint.`

- [HIGH] [Vol I holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:1046), [Vol II holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1088), [Vol I FRONTIER.md](/Users/raeez/chiral-bar-cobar/FRONTIER.md:198), [Vol I working_notes_frontier_2026_04.tex](/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:324), [Vol I N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:257), [Vol I N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:733) — PROBLEM: these summary surfaces drop the evaluation-core qualifier and advertise bare “MC3 for all simple types” / `MC3 (all simple types)`. That is exactly the scope drift the concordance forbids. FIX: in both `holomorphic_topological.tex` files replace `MC3 (all simple types)` with `MC3 (evaluation-generated core, all simple types; post-core DK-4/5 downstream)`; in `FRONTIER.md` rename the entry to `MC3 on the evaluation-generated core for all simple types`; in `working_notes_frontier_2026_04.tex:324` replace the parenthetical with `proved on the evaluation-generated core for all simple types`; in both `N2_mc3_all_types.tex` headings replace `MC3 for all simple types` with `MC3 on the evaluation-generated core for all simple types`.

- [HIGH] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4713), [Vol II examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:97), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:264), [Vol III drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:432) — PROBLEM: Vol III uses `MC3` as the label for the Yangian/ordered-bar residue lane. The canonical DK ladder does not do that: Yangian-from-\(r(z)\) is DK-0/DK-1 material; MC3 is the later categorical Clebsch-Gordan stage. FIX: in `quantum_group_reps.tex:264-266` replace `This is the content of Volume~II, MC3` with `This is the DK-0/DK-1 ordered-bar/Yangian lane of Volume~II; MC3 enters later at the categorical Clebsch--Gordan stage on the evaluation-generated core`; in `drinfeld_center.tex:432` replace `Volume~II, MC3` with `Volume~II, DK-0/DK-1 ordered-bar/Yangian lane`.

## Summary
Checked: 26 | Findings: 5 | Verdict: FAIL


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8426-71f6-7113-b425-612b8f408719
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: CROSS-VOLUME BRIDGE AUDIT.

Same for MC1-MC5. Are the MC theorem statuses correctly cited? Is MC5 chain-level conjectural status propagated?

Search across all three repos:
- ~/chiral-bar-cobar/
- ~/chiral-bar-cobar-vol2/
- ~/calabi-yau-quantum-groups/

For each finding: exact file:line in EACH volume, PROBLEM, and EXACT FIX.
mcp startup: no servers


thinking
**Planning parallel explorations**

I’m considering the need for multiple explorations in parallel for each volume. First, I should read skill files and provide the user with an update before doing substantial work. Frequent commentary updates might be necessary due to the complexity. I can use developer tools and multi_tool_use.parallel for efficient reads. Since I’m restricted from the web, I need to figure out what "MC" refers to—possibly "main conjecture?" I'll also need to search across repositories for relevant content and inspect exact lines.
thinking
**Searching for MC statuses**

I need to find where the statuses for MC1 to MC5 are defined, possibly in the concordance or theorem registry in Volume I, but they could be in any of the volumes. I should approach this systematically and might use explorer subagents for searching across the volumes. It seems beneficial to have one explorer per repository for relevant MC references. I shouldn't reread coverage because explorers are authoritative. I’ll trust their results without needing to verify manually.
codex
Using `deep-beilinson-audit` plus `cross-volume-propagation` workflow. I’m locating the canonical MC1–MC5 status surface first, then I’ll trace every cross-volume citation and compare wording against the live source.
exec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

 succeeded in 52ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

exec
/bin/zsh -lc 'pwd && rg -n "MC[1-5]|MC theorem|chain-level conject|chain level conject|conjectural status|MC5|Main Conjecture" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 68ms:
/Users/raeez/chiral-bar-cobar/compute/audit/platonic_rewrite_2026_03_28/03_PLATONIC_SEQUENCING.md:86:MC3 beyond type A. Non-principal W-duality. Factorization envelopes.
/Users/raeez/chiral-bar-cobar/compute/audit/platonic_rewrite_2026_03_28/03_PLATONIC_SEQUENCING.md:331:  MC3 beyond type A.
/Users/raeez/chiral-bar-cobar/compute/tests/test_mv_positivity_sl3.py:14:  - concordance.tex: MC3 status (DK-2/3 for fd type A)
/Users/raeez/chiral-bar-cobar/compute/tests/test_categorical_cg_typeA.py:313:# ---------- Cross-check: MC3 dependency verification ----------
/Users/raeez/chiral-bar-cobar/compute/tests/test_categorical_cg_typeA.py:315:class TestMC3Dependency:
/Users/raeez/chiral-bar-cobar/compute/tests/test_categorical_cg_typeA.py:318:    suffices for the MC3 proof step (i).
/Users/raeez/chiral-bar-cobar/compute/audit/platonic_rewrite_2026_03_28/10_CROSS_VOLUME_BRIDGES.md:52:DK-4/5 conditional on MC3 (type A proved; arbitrary type open).
/Users/raeez/chiral-bar-cobar/compute/tests/test_w4_ope_miura.py:670:# MC4 concordance formula verification
/Users/raeez/chiral-bar-cobar/compute/tests/test_w4_ope_miura.py:683:class TestMC4ConcordanceFormulas:
/Users/raeez/chiral-bar-cobar/compute/tests/test_w4_ope_miura.py:716:        is the key remaining step for MC4 W∞ stage-4 computational closure.
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_moriwaki_analytic_bridge_engine.py:5:and the monograph's sewing programme (MC5).
/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_categorical_zeta_engine.py:21:    concordance.tex: MC3 (all simple types, cor:mc3-all-types)
/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_categorical_zeta_engine.py:469:# Section 9: MC3 thick generation
/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_categorical_zeta_engine.py:472:class TestMC3Generation:
/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_categorical_zeta_engine.py:473:    """MC3 thick generation function and its zeta."""
/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_categorical_zeta_engine.py:493:        """For all sl_N, MC3 gives g(n) = 1 for n >= 1."""
/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rtt_typeD.py:3:Verifies the FRONTIER computation for MC3 extension to orthogonal Dynkin
/Users/raeez/chiral-bar-cobar/compute/tests/test_w4_normalization_ratio.py:1:"""Tests for MC4 normalization ratio R(t).
/Users/raeez/chiral-bar-cobar/compute/tests/test_w4_normalization_ratio.py:8:  concordance.tex (MC4 stage-4 packet)
/Users/raeez/chiral-bar-cobar/compute/tests/test_lattice_bridge.py:194:        This is WHY the lattice route resolves MC3 unconditionally.
codex
I have the skill instructions and the first sweep. Next I’m locking the canonical source of truth for MC1–MC5, then I’ll compare every cross-volume citation against that instead of against folklore.
exec
/bin/zsh -lc "sed -n '470,520p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC1|MC2|MC3|MC4|MC5|master conjecture|master conjectures|analytic HS-sewing|chain-level" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
**FM30. Lambda-bracket divided-power coefficient conflation.** Opus wrote the lambda-bracket coefficient c/12 where the shadow invariant S_2 = c/2 was required. The lambda-bracket {T_λ T} = (c/12)λ^3 uses divided powers (T_{(3)}T/3! = (c/2)/6 = c/12). Opus confused the PRESENTATION-DEPENDENT coefficient c/12 with the PRESENTATION-INDEPENDENT invariant S_2 = κ = c/2. The error was compounded by writing "which is the Virasoro central charge itself" (c/12 is NOT c). Counter: shadow invariants S_r are NUMBERS (family invariants), not convention-dependent coefficients. S_2 = κ ALWAYS. After writing any S_r value, verify against Vol I census: S_2(Vir) = c/2.

**FM32. Homotopy group computation from wrong space (BU vs U).** Opus computed pi_3(BU) = Z, confusing BU with U. The loop space relation pi_k(BU) = pi_{k-1}(U) was not applied: pi_3(BU) = pi_2(U) = 0 (Bott periodicity, even homotopy of U vanishes). The confusion is natural because pi_3(U) = Z IS the standard result, but the classifying space BU shifts the index by one. Counter: ALWAYS write the fiber sequence X -> EX -> BX and the resulting pi_k(BX) = pi_{k-1}(X) before computing any homotopy group of a classifying space. Check Bott periodicity PARITY after the shift.

**FM33. Formula applied outside its hypothesis domain.** Opus applied kappa_ch = chi(S)/2 (valid for local surfaces Tot(K_S -> S)) to the conifold (Tot(O(-1)^2 -> P^1), which is NOT Tot(K_S -> S) since K_{P^1} = O(-2) != O(-1)^2). The formula gave the correct numerical answer (kappa = 1) by coincidence, but the derivation is mathematically invalid. Counter: before applying ANY formula, verify the input satisfies the stated hypotheses. A correct answer from an invalid argument is worse than a wrong answer from a valid one — it masks the error.

**FM34. Excision/coproduct categorical level confusion.** Opus conflated two operations at different categorical levels: (a) excision (a gluing/descent property, produces one object from two halves via tensor product OVER A), and (b) the coproduct (a coalgebra structure map, produces the tensor product of two copies as a plain tensor product). The confusion is natural because both involve "cutting" and "tensor products," but excision is a SHEAF property (works over the algebra) while the coproduct is a COALGEBRA structure (works in the category of vector spaces). Counter: when writing a coproduct interpretation, verify the codomain is B(A) ⊗ B(A) (plain), not B_L ⊗_A B_R (over A).

**FM31. Asymptotic cancellation failure.** Opus wrote 10/(5c^2) = 2/(5c^2) instead of 2/c^2. The error: failing to cancel the common factor 5 between numerator 10 and denominator 5c^2. This is an ARITHMETIC error, not a conceptual one, but it propagates silently because 2/(5c^2) "looks like" a valid large-c asymptotic. Counter: after writing ANY asymptotic a/f(c), substitute c=100 and verify the numerical value matches the exact formula.

**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."

## Theorem Status

| Thm | Status | Key result |
|-----|--------|------------|
| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
 succeeded in 52ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 51ms:
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:480:**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
CLAUDE.md:499:| Topologization | PROVED (affine KM); CONJECTURAL (general) | SC^{ch,top} + Sugawara = E_3 for V_k(g) at k != -h^v (thm:topologization). General chiral algebras with conformal vector: conj:topologization-general. Proof cohomological; class M chain-level open. |
CLAUDE.md:539:**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
CLAUDE.md:571:AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
CLAUDE.md:834:AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; their identification as families over hbar*H^3(g)[[hbar]] is CONJECTURAL (conj:e3-identification). Topological E_3 (b): PROVED for affine KM at non-critical level (thm:topologization); CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general in Vol I, conj:E3-topological-climax in Vol II). Proof is cohomological; for class M, chain-level E_3 may fail. COUNTER: always specify which E_3 and whether the claim requires Sugawara.
CLAUDE.md:842:AP162: E_3 requires conformal vector. NEVER claim E_3 structure without stating: (a) the conformal vector exists, (b) the level is non-critical, (c) T(z) is Q-exact in the bulk. At critical level k = -h^v: Sugawara undefined, topologization fails, stuck at SC^{ch,top}. Status: PROVED for affine KM (thm:topologization); CONJECTURAL for general (conj:topologization-general). The proof is cohomological; for class M algebras the chain-level E_3 structure is open.
CLAUDE.md:849:AP167: Topologization scope. thm:topologization is PROVED for affine KM V_k(g) at non-critical level k != -h^v (where Sugawara T = {Q,G} is explicit). For general chiral algebras with conformal vector: CONJECTURAL (conj:topologization-general). The proof is COHOMOLOGICAL (works on Q-cohomology, not on cochains). For class M (Virasoro), where chain-level BV/bar is false, the E_3 may exist only on cohomology. COUNTER: every topologization reference must carry scope qualifier "(proved for affine KM at non-critical level)."
CLAUDE.md:853:AP171: Associator dependence dichotomy. The chiral QG equivalence (R-matrix <-> A_inf <-> coproduct) holds "up to choice of Drinfeld associator Phi." COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (proved for sl_2: GRT_1 shifts P_3 by coboundaries). COCHAIN-LEVEL derived center = ASSOCIATOR-DEPENDENT (the cochain-level E_3 carries the quantum group structure). Bar-side invariants (kappa, shadow tower) are associator-FREE. Cobar-side and coproduct-side depend on Phi. Analogous to deformation quantization: gauge-equivalent star products.
CLAUDE.md:919:**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).
metadata/theorem_registry.md:133:| `prop:mc4-reduction-principle` | `proposition` | 1154 | Reduction of MC4 to finite-stage compatibility |
metadata/theorem_registry.md:134:| `cor:mc4-degreewise-stabilization` | `corollary` | 1219 | Degreewise stabilization criterion for MC4 |
metadata/theorem_registry.md:135:| `cor:mc4-surjective-criterion` | `corollary` | 1256 | Finite-dimensional surjectivity criterion for MC4 |
metadata/theorem_registry.md:136:| `prop:mc4-weight-cutoff` | `proposition` | 1294 | Weight-cutoff criterion for MC4 |
metadata/theorem_registry.md:140:| `cor:winfty-standard-mc4-package` | `corollary` | 1521 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1919 | Uniform PBW bridge from MC1 to MC4 |
metadata/theorem_registry.md:179:| `prop:winfty-mc4-frontier-package` | `proposition` | 3179 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
codex
The canonical surface is already nontrivial: MC5 is explicitly split into analytic proved, coderived proved, chain-level conjectural; MC3 is not a flat one-line “proved” statement without scope. I’m drilling into the precise concordance wording now so the later findings use the manuscript’s own truth hierarchy.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1836,1962p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1978,1990p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3260,3295p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1978	The monograph is organized in three concentric rings.
  1979	
  1980	\subsection*{Ring~1: The proved modular Koszul core}
  1981	Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
  1982	\textup{(}analytic HS-sewing at all genera, genus-$0$ algebraic
  1983	BRST/bar, $D^{\mathrm{co}}$-level BV=bar for all shadow classes;
  1984	chain-level BV/BRST/bar conjectural\textup{)},
  1985	MC3 \textup{(}three-layer split: MC3a evaluation core all types unconditional,
  1986	MC3b categorical thick generation all types unconditional,
  1987	MC3c full Cat~O type~A unconditional / other types conditional on
  1988	Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
  1989	DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
  1990	and the Koszulness characterization programme
 succeeded in 51ms:
  3260	 $\mathrm{rk}(\fg)$-dimensional bar cohomology in~$H^2$
  3261	 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}) \\
  3262	MC2 & $D^2 = 0$ & Bar-intrinsic MC element: $\Theta_\cA := D_\cA - d_0$
  3263	 is automatically MC because $D_\cA^2 = 0$
  3264	 (Theorem~\ref{thm:mc2-bar-intrinsic}).
  3265	 No homotopy correction needed \\
  3266	MC3 & Prefundamental CG & \textbf{Proved for all simple types on the evaluation-generated core}.
  3267	 All-types package~(i) is proved
  3268	 (Theorem~\ref{thm:categorical-cg-all-types}),
  3269	 and the generated-core DK comparison surface
  3270	 \textup{(}traditionally packaged as DK-2/3\textup{)}
  3271	 on the evaluation-generated core is proved separately
  3272	 (Corollary~\ref{cor:dk23-all-types}).
  3273	 Extension beyond evaluation modules is DK-4/5 (downstream, not part of MC3).
  3274	 Key input: multiplicity-free $q$-characters for fundamental reps
  3275	 \cite{ChariMoura06} replace the minuscule hypothesis.
  3276	 Type~$A$ identifies the remaining post-CG completion packet
  3277	 (Theorem~\ref{thm:mc3-type-a-resolution});
  3278	 no global all-types closure is claimed on this row \\
  3279	MC4 & Strong filtration & Completion is formal inverse limit: the strong
 succeeded in 51ms:
  1836	The three-pillar architecture determines the MC resolution strategy:
  1837	\begin{itemize}
  1838	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1839	 element in the modular convolution $sL_\infty$-algebra; the
  1840	 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
  1841	 obstruction tower) are the constructive content.
  1842	 MC1 (PBW concentration) holds unconditionally for universal
  1843	 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
  1844	 (Proposition~\ref{prop:pbw-universality}). For simple quotients
  1845	 $L_k(\fg)$ at admissible levels, PBW concentration fails at
  1846	 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
  1847	 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
  1848	 to $H^2(\barB)$
  1849	 (Conjecture~\ref{conj:admissible-koszul-rank-obstruction}).
  1850	\item \emph{MC3}: MC3 is \textbf{proved} for all simple types on the
  1851	evaluation-generated core. The categorical CG decomposition is proved via
  1852	multiplicity-free $\ell$-weights
  1853	\textup{(}Theorem~\ref{thm:categorical-cg-all-types}\textup{)}, and
  1854	the DK comparison on the
  1855	evaluation-generated core is proved

thinking
**Considering MC statuses**

I’m thinking about inspecting the red_team_summary for the MC statuses. It might not be strictly necessary, but it could be a helpful first read to understand context better. I wonder if I should search for specific relevant lines within that summary. It's probably important to clarify the statuses before proceeding, just to make sure I'm not missing anything critical. It feels like a step worth taking!
exec
/bin/zsh -lc 'rg -n "MC1|MC2|MC3|MC4|MC5|chain-level" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC3|MC5|chain-level" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
791:| `prop:chain-level-curvature-operator` | `proposition` | 626 | Chain-level curvature operator |
1994:| `thm:mc3-type-a-resolution` | `theorem` | 3761 | Type-$A$ MC3 reduction to the compact-completion packet |
1996:| `cor:mc3-all-types` | `corollary` | 3987 | Three-layer MC3 status after categorical CG closure |
2123:| `thm:rtt-all-types` | `theorem` | 1174 | RTT presentation and MC3 for all simple types |
2315:| `prop:chain-level-three-obstructions` | `proposition` | 1646 | Three chain-level obstructions |
2895:| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2108 | Type-$A$ MC3 reduction via the gravitational Yangian |


thinking
**Checking counts and references**

I need to check the count, which might be the number of files or candidate citation sites. I’ll compute something related to searching for cross-volume references in Vol II and III, looking for phrases like "Vol I MC5." I should also inspect Volume I's outward-facing summaries for any mismatches. For example, there seems to be inconsistency regarding the master conjectures, specifically about MC5, and I'll need to find a precise fix for that inconsistency.
thinking
**Identifying MC3 mismatches**

I need to look for possible mismatches related to MC3. The README indicates that MC3 should work for all simple types, specifying type A as unconditional while other types are conditional on Lemma L for the rank-independence step. However, the concordance states that MC3 is proved for all simple types based on the evaluation-generated core, with MC3c being a full Cat O type A unconditional while others remain conditional. I've got to clarify this inconsistency.
codex
The first hard failure is already visible in Vol I: at least one public-facing status summary says “all five master conjectures are proved” while also admitting the genuswise chain-level part of MC5 remains conjectural. That kind of self-contradiction is exactly the propagation failure I’m now tracing through Vol II and Vol III.
exec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' --glob 'README.md' --glob 'FRONTIER.md' --glob 'CLAUDE.md' --glob 'AGENTS.md' --hidden -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"' 'all five master conjectures|MC1 through MC5|MC1-MC5|MC1-5|all master conjectures|master conjectures MC1' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' --glob 'README.md' --glob 'FRONTIER.md' --glob 'CLAUDE.md' --glob 'AGENTS.md' --hidden -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"' 'MC5|MC\\.5' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' --glob 'README.md' --glob 'FRONTIER.md' --glob 'CLAUDE.md' --glob 'AGENTS.md' --hidden -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"' 'MC3' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4512:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1856:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1856:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/README.md:26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4503:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:1685:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/CE02_central_charge.md:1148:"""Computational checks for independent conjectures (not subsumed by MC1-MC5).
 succeeded in 52ms:
Total output lines: 340

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:312:| W-algebras | Feynman-diag m_k matches bar diff | MC5 | (1) Analytic HS-sewing proved at all genera; (2) genus-0 algebraic BRST/bar proved; (3) D^co-level BV=bar proved for all shadow classes including class M; (4) genuswise chain-level BV/BRST/bar conjectural (class M chain-level false); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:321:| 3D gravity | Part VI: 3d quantum gravity = derived center of boundary chiral algebra; W-algebra Hochschild bulk reconstruction | Thm H + MC5 | Boundary-linear bulk = Hochschild proved; full global triangle (boundary -> bulk -> boundary) conjectural beyond the Koszul locus |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:315: MC5 analytic HS-sewing lane) to handle the non-compact directions.
/Users/raeez/calabi-yau-quantum-groups/chapters/frame/preface.tex:259:\item \emph{Sewing parameter} (Vol~I, MC5 analytic
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:200:The scope is perturbative: the \v{C}ech homotopy produces an algebraic $A_\infty$-structure on the Ext algebra, but convergence of the resulting series to holomorphic functions (the non-perturbative statement) requires separate input from the analytic completion programme of Volume~I (MC5, \S\ref{sec:analytic-sewing}). The perturbative statement suffices for the formal CY-to-chiral functor and for all combinatorial applications in this volume. The full construction, including the proof that the SDR conditions hold and the scope qualification, is Theorem~\ref{thm:cech-contracting-homotopy} in Chapter~\ref{ch:cy-to-chiral}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:559:the analytic completion programme (MC5,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:783: \item \emph{Gluing = sewing.} The toric diagram gluing rules (one vertex factor $C_{\lambda\mu\nu}$ per trivalent node, one propagator $(-q)^{|\lambda|}/z_\lambda$ per internal edge, sum over internal partitions) are the $\Eone$ sewing rules (Vol~I, MC5 analytic HS-sewing lane). The edge propagator $(-q)^{|\lambda|}/z_\lambda$ is the $\Eone$ bar complex pairing on $H^1(B^1)$.
/Users/raeez/chiral-bar-cobar/appendices/spectral_higher_genus.tex:4:\begin{construction}[Spectral theory at higher genus as MC5]
/Users/raeez/chiral-bar-cobar/appendices/spectral_higher_genus.tex:24: converges by bounded filtration. The MC5 content is
/Users/raeez/chiral-bar-cobar/appendices/spectral_higher_genus.tex:121:Conjecture~\textup{\ref{conj:master-bv-brst}} \textup{(MC5: BV/BRST = bar).}
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:1:# Vol III MC5 Status Sweep
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:5:MC5 is not fully proved. What IS proved at all genera is the analytic HS-sewing package. The remaining genuswise BV/BRST/bar identification is still conjectural; at genus 0 the algebraic BRST/bar comparison is proved; tree-level amplitude pairing is conditional on `cor:string-amplitude-genus0`.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:13:Vol III contains NO "MC5 PROVED" assertion anywhere. Every MC5 mention is a forward reference into Vol I for the sewing-mechanism content (analytic HS-sewing lane), which IS the proved lane per canonical truth. No Vol III theorem, proposition, remark, or status table claims MC5 as a whole is proved. The Vol III frontier line at `working_notes.tex:3328-3330` was already in canonical form prior to this sweep:
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:15:> "The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural)."
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:17:The sweep added the explicit qualifier "MC5 analytic HS-sewing lane" (or equivalent) at every Vol III citation site where a bare "(Vol I, MC5)" reference could be misread as citing MC5 as a whole. Two sites were already explicitly scoped to "analytic completion programme" and needed no edit.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:22:   - Line 2253: "sewing envelope A^sew (MC5)" to "sewing envelope A^sew (MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:23:   - Line 2630: "Sewing parameter space (Vol I, MC5)" to "Sewing parameter space (Vol I, MC5 analytic HS-sewing lane)"
 succeeded in 52ms:
Total output lines: 642

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:310:| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
/Users/raeez/chiral-bar-cobar/CLAUDE.md:571:AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:919:**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:118:**What is proved**: MC3 for all simple types on the evaluation-generated core (thm:categorical-cg-all-types). The reduction chain (prop:yangian-dk4-typea-frontier) for type A reduces DK-4 to a single mixed-tensor coefficient identity, which IS satisfied on the factorization side.
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:132:**What is proved**: MC3 on the evaluation-generated core. The Bridge Criterion Theorem (thm:bridge-criterion): B1+B2+B4 => full bridge.
/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:118:**What is proved**: MC3 for all simple types on the evaluation-generated core (thm:categorical-cg-all-types). The reduction chain (prop:yangian-dk4-typea-frontier) for type A reduces DK-4 to a single mixed-tensor coefficient identity, which IS satisfied on the factorization side.
/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:132:**What is proved**: MC3 on the evaluation-generated core. The Bridge Criterion Theorem (thm:bridge-criterion): B1+B2+B4 => full bridge.
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:1156:MC3 categorical lift proceeds one slot at a time. The bar-cobar
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:2872:\medskip\noindent\textbf{MC3 and all-types CG.} On the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4515:conjectural.} MC3 holds for all simple types on the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4546:\medskip\noindent\textbf{MC3} (thick generation). On the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:4547:type-$A$ Yangian module surface, the four-package MC3 problem
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:600:\medskip\noindent\textbf{MC3 and all-types CG.} On the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1859:conjectural.} MC3 holds for all simple types on the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1890:\medskip\noindent\textbf{MC3} (thick generation). On the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1891:type-$A$ Yangian module surface, the four-package MC3 problem

thinking
**Considering volume and categories**

I’m looking at the introduction for Volume 3, focusing on various sections like quantum group representations, which are around 170 to 210. Also, I see categories for Fukaya and modular Koszul bridge mentioned. It seems like they span different ranges, maybe 220-270 and 575-585, respectively. I’m also curious if the working notes are live — should I consider including those too? It feels like there's a lot to encompass here!
codex
I’m past the broad grep stage. Now I’m reading the exact paragraphs that look risky, because several of the remaining candidates are subtle scope leaks rather than obvious “MC5 proved” blunders.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex | sed -n '488,506p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex | sed -n '1078,1094p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1078	 & \checkmark\;\cite{CostelloP2201}
  1079	 & \checkmark\;$\mathrm{Sh}_{0,n}(\Theta_\cA)$ \\
  1080	$R$-matrix from gauge propagator
  1081	 & \checkmark\;\cite{CWY18}
  1082	 & \checkmark\;$\operatorname{Res}^{\mathrm{coll}}_{0,2}$ \\
  1083	YBE from CYBE
  1084	 & \checkmark\;\cite{CWY18}
  1085	 & \checkmark\;Arnold relation on $\overline{\mathcal{M}}_{0,4}$ \\
  1086	Yangian symmetry
  1087	 & \checkmark\;\cite{CWY18}
  1088	 & \checkmark\;MC3 (all simple types) \\
  1089	BCFW recursion
  1090	 & \checkmark\;\cite{CostelloP2201}
  1091	 & \checkmark\;MC recursion \\
  1092	Celestial OPE associativity
  1093	 & \checkmark\;\cite{Costello2302}
  1094	 & \checkmark\;MC equation at genus $0$ \\
 succeeded in 52ms:
   488	\textbf{MC} & \textbf{Status} \\
   489	\hline
   490	MC1 & \textbf{Proved.} PBW concentration for all standard families
   491	 (Vol~I, Theorem~\ref*{V1-thm:pbw-koszulness-criterion}). \\
   492	MC2 & \textbf{Proved.} Bar-intrinsic construction
   493	 $\Theta_\cA := D_\cA - d_0$ is MC because $D_\cA^2 = 0$
   494	 (Vol~I, Theorem~\ref*{V1-thm:mc2-bar-intrinsic}).
   495	 Algebraic-family rigidity
   496	 (Vol~I, Theorem~\ref*{V1-thm:algebraic-family-rigidity})
   497	 covers the standard Lie-theoretic landscape. \\
   498	MC3 & \textbf{Proved for all simple types} on the
   499	 evaluation-generated core
   500	 (Vol~I, Corollary~\ref*{V1-cor:mc3-all-types}).
   501	 DK-4/5 (extension beyond evaluation modules)
   502	 is downstream, not a component of MC3. \\
   503	MC4 & \textbf{Proved.} Strong completion towers
   504	 (Vol~I, Theorem~\ref*{V1-thm:completed-bar-cobar-strong});
   505	 MC4${}^+$ solved by weight stabilization,
   506	 MC4${}^0$ reduced to finite resonance
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1586,1598p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '24,42p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '176,210p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex | sed -n '384,398p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1586	
  1587	The full genus tower is developed in Section~\ref{sec:bar_cobar}
  1588	and Part~\ref{part:examples} (Section~\ref{ch:modular-pva-quantization}). The
  1589	curvature at genus~$g \geq 2$ is resolved in Volume~I by
  1590	inductive genus determination
  1591	along with $2$D convergence and the analytic-algebraic comparison;
  1592	the analytic lane of MC5 is proved at all genera; BV=bar in
  1593	the coderived category is proved for all shadow classes
  1594	(Volume~I, Theorem~
  1595	ef*{V1-thm:bv-bar-coderived}); the genuswise
  1596	chain-level BV/BRST/bar identification remains conjectural
  1597	(class~M chain-level false).
  1598	
 succeeded in 51ms:
   384	
   385	\emph{Fukaya categories} (Chapter~\ref{ch:fukaya}). The symplectic input. For an elliptic curve $E_\tau$, the Fukaya category $\Fuk(E_\tau)$ is CY of dimension~$1$ and $\Phi$ produces the Heisenberg vertex algebra $H_k$ at level $k = \mathrm{vol}(E_\tau)$. For a K3 surface~$S$, $\Fuk(S)$ is CY of dimension~$2$ and $\Phi$ produces an $E_2$-chiral algebra with $\kappa_{\mathrm{ch}} = \chi(\mathcal{O}_S) = 2$. For compact CY threefolds, the Fukaya-side functor is conditional on the chain-level $\mathbb{S}^3$-framing (Conjecture~CY-A$_3$); the open-string sector ($\Fuk(X)$ with Lagrangian boundary conditions) connects to the Volume~II Swiss-cheese structure. Wrapped Fukaya categories $\mathcal{W}(X)$ of Liouville manifolds provide the non-compact analogue: for cotangent bundles $T^*M$, Abouzaid's equivalence $\mathcal{W}(T^*M) \simeq \mathrm{Mod}(C_*(\Omega M))$ reduces the CY-to-chiral functor to the based loop space.
   386	
   387	\emph{Derived categories of coherent sheaves}. The algebraic input. For a smooth projective CY manifold $X$, the bounded derived category $D^b(\mathrm{Coh}(X))$ is CY of dimension~$d$ with the CY trace induced by Serre duality. Homological mirror symmetry identifies $\Fuk(X) \simeq D^b(\mathrm{Coh}(X^\vee))$; under $\Phi$, this becomes an equivalence $A_{\Fuk(X)} \simeq A_{D^b(\mathrm{Coh}(X^\vee))}$ of quantum chiral algebras, providing a consistency check between the symplectic and algebraic sides. When $D^b(\mathrm{Coh}(X))$ admits a full exceptional collection, the CY-to-chiral functor reduces to a quiver-with-potential computation: the critical CoHA of the quiver (Chapter~\ref{ch:toric-coha}). Bridgeland stability conditions parametrize the space of t-structures on $D^b(\mathrm{Coh}(X))$; wall-crossing in the stability manifold corresponds to mutations of the bar complex, and the global chiral algebra is assembled as a homotopy colimit over stability chambers (Programme~A).
   388	
   389	\emph{Matrix factorizations}. The Landau--Ginzburg input. A polynomial $W \colon \mathbb{C}^n \to \mathbb{C}$ gives a CY category $\mathrm{MF}(W)$ of dimension $n - 2$. For ADE singularities $W = x^N + y^2 + z^2 + w^2$ in four variables, $\mathrm{MF}(W)$ is CY of dimension~$2$ and $\Phi$ (Theorem~CY-A$_2$) produces chiral algebras related to $\mathcal{W}_N$-algebras. The LG/CY correspondence $\mathrm{MF}(W) \simeq D^b(\mathrm{Coh}(X_W))$ provides a further consistency check against the derived-category side. For non-ADE singularities (unimodal, bimodal), the resulting chiral algebras are expected to be new objects not realized by the standard Lie-theoretic landscape of Volume~I.
   390	
   391	\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
   392	
   393	In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$ (Chapter~\ref{ch:k3-times-e}, Definition~\ref{def:k3-double-current-algebra}) provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.
   394	
   395	\section{Guide for the reader}
   396	\label{sec:guide}
   397	
   398	Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the central result. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. The working notes (\S\ref{sec:working-notes}) record the research frontier.
 succeeded in 51ms:
    24	\end{definition}
    25	
    26	\begin{proposition}[Strict dg Lie structure on $\mathrm{Conv}_{\mathrm{str}}$]
    27	\label{prop:cy-conv-dglie}
    28	\ClaimStatusProvedElsewhere
    29	On the Koszul locus of $A_\cC$, the convolution bracket $[\cdot, \cdot]_{\mathrm{Conv}}$ on $\mathrm{Conv}_{\mathrm{str}}(B(A_\cC), A_\cC)$ satisfies the graded Jacobi identity strictly, and $\delta$ is a derivation of this bracket. The pair $(\mathrm{Conv}_{\mathrm{str}}, \delta, [\cdot, \cdot])$ is a dg Lie algebra; it is a strict model of an $L_\infty$ algebra $\mathrm{Conv}_{\infty}(B(A_\cC), A_\cC)$, and the two share the same Maurer--Cartan moduli space (Vol~I, three-pillar constraint, \S MC3).
    30	\end{proposition}
    31	
    32	\begin{proof}[Attribution]
    33	The strict-versus-$L_\infty$ comparison is Vol~I Theorem~MC3 (Robalo--Nick\-erson--Welch\-er 2019 bifunctoriality failure in both slots resolves by treating one slot at a time). The MC moduli coincidence is Vol~I Theorem~MC4. Here we only transport the statement: $\Phi$ sends cyclic $A_\infty$-objects to chiral algebras compatibly with the bar construction (Theorem~CY-A(ii)), so the convolution bracket on the CY side is pulled back from the chiral convolution bracket of Vol~I.
    34	\end{proof}
    35	
    36	\begin{remark}[Bifunctoriality warning]
    37	\label{rem:conv-bifunctor-warning}
    38	The convolution $\Hom_\alpha(C, A)$ is \emph{not} a bifunctor in both slots simultaneously (Vol~I, three-pillar constraint~(2); Robalo--Nickerson--Welcher 2019). MC3 holds one slot at a time. In the CY setting this means: varying $\cC$ along a path of CY categories while holding $\Phi(\cC)$ fixed, or varying $A_\cC$ along a chain homotopy while holding $\cC$ fixed, each gives a homotopy equivalence of MC moduli; the simultaneous variation does not (\emph{a priori}) define a coherent bifunctor.
    39	\end{remark}
    40	
    41	\begin{theorem}[CY shadow obstruction tower as MC element]
    42	\label{thm:cy-theta-mc}
 succeeded in 51ms:
   176	\label{rem:kl-bar-complex}
   177	From the bar-complex perspective, the KL equivalence states that
   178	the $\Eone$-representation category of the affine vertex algebra
   179	$V_k(\frakg)$ recovers the quantum group representation category.
   180	The Volume~I bar complex $B(V_k(\frakg))$ encodes the quantum group
   181	$R$-matrix in its degree-$(1,1)$ component; the DK bridge (Volume~II,
   182	MC3 for all simple types) extends this to the full categorical
   183	equivalence.
   184	\end{remark}
   185	
   186	\begin{proposition}[KL and the DK bridge]
   187	\label{prop:kl-dk-bridge}
   188	\ClaimStatusProvedElsewhere
   189	The Kazhdan--Lusztig equivalence factors through the Drinfeld--Kohno
   190	bridge (Volume~II):
   191	\[
   192	\begin{tikzcd}[column sep=large]
   193	 \mathrm{KL}_k(\frakg) \ar[r, "\sim", "\text{KL}"'] &
   194	 \cC_q(\frakg) \\
   195	 \Rep^{E_1}(V_k(\frakg)) \ar[u, hook] \ar[r, "\text{DK}"] &
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex | sed -n '426,438p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex | sed -n '248,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '224,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex | sed -n '574,586p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex | sed -n '1558,1568p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex | sed -n '434,444p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   248	The configuration space identification
   249	(Proposition~\ref{prop:config-space-id}) is proved. The full
   250	identification $Z_{\Ainf} = Z$ requires verifying that the
   251	combinatorial coefficients (signs, symmetry factors, and
   252	normalizations) match at all orders. At genus~$0$ and for the
   253	abelian case $G = \mathrm{U}(1)$, this is verified below. The
   254	nonabelian case requires the full MC5 identification
   255	(Theorem~\ref{rem:mc5-genus-zero-bridge}) applied to
   256	$\widehat{\mathfrak{g}}_k$, contingent on the genuswise BV/BRST/bar
   257	identification of MC5 which remains conjectural in Volume~I beyond
   258	the analytic HS-sewing lane.
   259	\end{remark}
   260	
 succeeded in 52ms:
   426	\ClaimStatusConjectured
   427	For a CY$_2$ category $\cC$ with $\frakg$-symmetry, the Drinfeld
   428	center $\cZ(\Rep^{\Eone}(\Phi(\cC)))$ determines a quantum vertex
   429	chiral group $G(\cC)$ unifying four algebraic structures:
   430	\begin{enumerate}[label=(\roman*)]
   431	 \item $\Uq(\frakg)$: the quantum group (fiber at a point);
   432	 \item $Y(\frakg)$: the Yangian ($\Eone$-sector, Volume~II, MC3);
   433	 \item $\Uq(\widehat{\frakg})$: the affine quantum group
   434	 (loop algebra sector);
   435	 \item The Etingof--Kazhdan quantum vertex algebra (the genuinely
   436	 nonlocal atom, Volume~II).
   437	\end{enumerate}
   438	The four incarnations arise from different geometric
 succeeded in 50ms:
   224	\end{conjecture}
   225	
   226	\begin{remark}[Status of Conjecture CY-C]
   227	\label{rem:cy-c-status}
   228	Item (i) is constructed for $\frakg = \fsl_N$ via the Bridgeland
   229	stability conditions on the CY$_2$ resolution of the $A_{N-1}$
   230	surface singularity. Item (ii) at the $\Eone$ level is the content
   231	of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
   232	upgrade requires the Drinfeld center passage
   233	(Chapter~\ref{ch:drinfeld-center}). Item (iii) follows from
   234	Theorem~CY-D (Theorem~\ref{thm:cy-modular-characteristic}) when
   235	the CY category is constructed.
   236	\end{remark}
   237	
   238	
   239	\section{Yangian and RTT realizations}
   240	\label{sec:yangian-rtt}
   241	
   242	%: Three distinct algebraic operations must be kept separate:
   243	% Koszul duality, FF involution, and Langlands duality.
 succeeded in 52ms:
  1558	\textbf{DK level} & \textbf{MC input} \\
  1559	\hline
  1560	DK-0 & MC2 (bar-intrinsic MC element) \\
  1561	DK-1 & MC2 + analytic continuation \\
  1562	DK-2 & MC1 (PBW concentration) + DK-1 \\
  1563	DK-3 & MC3 (categorical CG) \\
  1564	DK-4 & MC4 (completion towers) \\
  1565	DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
  1566	\end{tabular}
  1567	\end{center}
  1568	The MC hierarchy provides the algebraic inputs; the DK
 succeeded in 52ms:
   574	\label{rem:qg-to-shadow}
   575	The passage from quantum group data to the shadow obstruction tower
   576	inverts the construction of this chapter: the quantum group
   577	$\Uq(\frakg)$ determines the $R$-matrix, which is the degree-$(1,1)$
   578	component of the $\Eone$ MC element $\Theta^{E_1}$, whose
   579	$\Sigma_n$-coinvariant projections are the shadow tower. The
   580	reconstruction problem (from quantum group to chiral algebra) is
   581	solved by the DK bridge (MC3 for all simple types): the categorical
   582	data of $\Rep_q(\frakg)$ uniquely determines the chiral algebra
   583	$V_k(\frakg)$ up to the completion issues of MC4.
   584	\end{remark}
 succeeded in 52ms:
   434	\begin{remark}[Evidence]
   435	Chirality requires: (1) the twist preserves a holomorphic structure on the Coulomb branch \cite{Gai19}; (2) $T(z)$ survives the twist with vanishing anomalies; (3) the factorization algebra extends to a $\mathcal{D}$-module on $\mathrm{Ran}(X)$ (automatic for chiral algebras by \BDref{Chapter 3}, requires verification for twisted gauge theories).
   436	\end{remark}
   437	
   438	\begin{remark}[Scope]
   439	Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
   440	\end{remark}
   441	
   442	\subsubsection{Costello--Li conditions: from factorization to chiral}
   443	
   444	\begin{theorem}[CL chirality for \texorpdfstring{$\mathcal{N}=4$}{N=4}; \ClaimStatusProvedElsewhere]

thinking
**Investigating volume files**

I need to make a precise edit by changing it to “MC3 (evaluation-generated core, all simple types; post-core DK-4/5 downstream).” I'm thinking about checking other Volume II files that might have similar issues. I can search for exact phrases like “MC3 (all simple types)” or “MC3 for all simple types” and also consider using regex. I should also look in Volume III for targeted searches, focusing on problematic patterns and citations to ensure everything is accurate.
codex
The clean surfaces are starting to separate from the dirty ones. Vol II mostly carries the MC5 caveat correctly, but I’m finding quieter MC3 scope leaks and at least one Vol III bridge paragraph that cites “Theorem MC3” for something MC3 is not.
exec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -g '"'!compute/**'"' -g '"'!**/.claude/**'"' 'MC3 for all simple types|MC3 \\(all simple types\\)|Theorem~MC3|Theorem MC3|MC3 holds for all simple types|MC3 is proved for all simple types|MC3 \\(proved' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -g '"'!compute/**'"' -g '"'!**/.claude/**'"' 'Vol~I, MC5|Volume~I, MC5|MC5 analytic HS-sewing lane|analytic lane of MC5|analytic HS-sewing lane of MC5|MC5 remains conjectural|chain-level BV/BRST/bar identification remains conjectural|MC5 is partially proved|MC5 is not fully proved' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -g '"'!compute/**'"' -g '"'!**/.claude/**'"' 'MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera|MC5 \\(all genera|full MC5 identification|MC5 \\)' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md:118:**What is proved**: MC3 for all simple types on the evaluation-generated core (thm:categorical-cg-all-types). The reduction chain (prop:yangian-dk4-typea-frontier) for type A reduces DK-4 to a single mixed-tensor coefficient identity, which IS satisfied on the factorization side.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:182:MC3 for all simple types) extends this to the full categorical
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:231:of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:581:solved by the DK bridge (MC3 for all simple types): the categorical
/Users/raeez/chiral-bar-cobar-vol2/FRONTIER.md:118:**What is proved**: MC3 for all simple types on the evaluation-generated core (thm:categorical-cg-all-types). The reduction chain (prop:yangian-dk4-typea-frontier) for type A reduces DK-4 to a single mixed-tensor coefficient identity, which IS satisfied on the factorization side.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:33:The strict-versus-$L_\infty$ comparison is Vol~I Theorem~MC3 (Robalo--Nick\-erson--Welch\-er 2019 bifunctoriality failure in both slots resolves by treating one slot at a time). The MC moduli coincidence is Vol~I Theorem~MC4. Here we only transport the statement: $\Phi$ sends cyclic $A_\infty$-objects to chiral algebras compatibly with the bar construction (Theorem~CY-A(ii)), so the convolution bracket on the CY side is pulled back from the chiral convolution bracket of Vol~I.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:391:\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2313:\begin{remark}[MC3 for all simple types: evaluation core proved, post-core conditional]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1088: & \checkmark\;MC3 (all simple types) \\
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:254:nonabelian case requires the full MC5 identification
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1565:DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex:1922:nonabelian case requires the full MC5 identification
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:5:MC5 is not fully proved. What IS proved at all genera is the analytic HS-sewing package. The remaining genuswise BV/BRST/bar identification is still conjectural; at genus 0 the algebraic BRST/bar comparison is proved; tree-level amplitude pairing is conditional on `cor:string-amplitude-genus0`.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:15:> "The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural)."
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:17:The sweep added the explicit qualifier "MC5 analytic HS-sewing lane" (or equivalent) at every Vol III citation site where a bare "(Vol I, MC5)" reference could be misread as citing MC5 as a whole. Two sites were already explicitly scoped to "analytic completion programme" and needed no edit.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:22:   - Line 2253: "sewing envelope A^sew (MC5)" to "sewing envelope A^sew (MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:23:   - Line 2630: "Sewing parameter space (Vol I, MC5)" to "Sewing parameter space (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:24:   - Line 2641: "sewing mechanism of MC5" to "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:27:   - Line 319: "sewing envelope of Volume I, MC5" to "sewing envelope of Volume I, MC5 analytic HS-sewing lane"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:30:   - Line 196: "Sewing parameter (Vol I, MC5)" to "Sewing parameter (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:33:   - Line 526: "E_1 sewing rules (Vol I, MC5)" to "E_1 sewing rules (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:61:- `chapters/examples/fukaya_categories.tex:319`: "MC5 analytic HS-sewing lane"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:62:- `working_notes.tex:2253`: "(MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:63:- `working_notes.tex:2630`: "(Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:64:- `working_notes.tex:2641`: "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:65:- `working_notes.tex:3328`: "the analytic HS-sewing lane of MC5" (pre-existing canonical)
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:66:- `working_notes.tex:3330`: "of MC5 remains conjectural" (pre-existing canonical)
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:69:- `chapters/theory/cy_to_chiral.tex:526`: "E_1 sewing rules (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:70:- `chapters/frame/preface.tex:196`: "(Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:5:> MC5 is not fully proved. What is proved at all genera is the analytic
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:61:    \emph{Status: Resolved at all genera} (Volume~I, MC5 proved).
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:75:  ("The analytic lane of MC5 is therefore proved at all genera; the

thinking
**Investigating file issues**

I'm looking into a command that used a volume2 path, and I’m wondering if that’s okay since the search output shows the same file in volume1. Should I inspect both? Maybe I should check with `ls` to see if they’re the same, but that might not be necessary. It seems I found line 1088 in volume2, but the search output is from volume1. If both volumes have the same file, that could be a problem! I'll need to check volume1's file and confirm the paths, maybe using `rg -n`.
codex
I found a second-order pattern: some bridge tables compress “MC3” into a bare success badge and drop the evaluation-core qualifier. That is exactly how scope drift re-enters after the main concordance was fixed.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex | sed -n '318,328p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex | sed -n '1038,1052p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'MC3 \\(all simple types\\)|MC3 for all simple types|Theorem~MC3|Theorem MC3|MC3 holds for all simple types|MC3 is proved for all simple types|MC3 \\(proved' /Users/raeez/chiral-bar-cobar -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!tmp_standalone_audit/**'"' -g '"'!audit_campaign_*/**'"' -g '"'!rectification_*/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   318	
   319	
   320	\section{DK-4 and DK-5: Extending the Drinfeld--Kohno bridge}
   321	
   322	\subsection{DK-4: Beyond the evaluation core}
   323	
   324	MC3 (proved for all simple types) establishes thick generation
   325	of the DK category by evaluation modules. DK-4 asks whether
   326	this extends to the full module category.
   327	
   328	\begin{problem}[DK-4]
 succeeded in 53ms:
  1038	$R$-matrix from gauge propagator
  1039	 & \checkmark\;\cite{CWY18}
  1040	 & \checkmark\;$\operatorname{Res}^{\mathrm{coll}}_{0,2}$ \\
  1041	YBE from CYBE
  1042	 & \checkmark\;\cite{CWY18}
  1043	 & \checkmark\;Arnold relation on $\overline{\mathcal{M}}_{0,4}$ \\
  1044	Yangian symmetry
  1045	 & \checkmark\;\cite{CWY18}
  1046	 & \checkmark\;MC3 (all simple types) \\
  1047	BCFW recursion
  1048	 & \checkmark\;\cite{CostelloP2201}
  1049	 & \checkmark\;MC recursion \\
  1050	Celestial OPE associativity
  1051	 & \checkmark\;\cite{Costello2302}
  1052	 & \checkmark\;MC equation at genus $0$ \\
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/FRONTIER.md:198:| 4 | MC3 for all simple types | JAMS | Thick generation via multiplicity-free ell-weights |
/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:324:MC3 (proved for all simple types) establishes thick generation
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:241:\subsection{Consequence: MC3 for all simple types}
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:257:\begin{corollary}[MC3 for all simple types]
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:710:\section{Corollary: MC3 for all simple types}\label{sec:mc3}
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:733:\begin{corollary}[MC3 for all simple types]
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7780:Master conjectures MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural. MC3 holds for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual problem DK-4/5 (extension beyond evaluation modules) is downstream.
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4841:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera while the genuswise BV/BRST/bar identification remains conjectural. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:1688:conjectural.} MC3 holds for all simple types on the
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4506:conjectural.} MC3 holds for all simple types on the
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:1046: & \checkmark\;MC3 (all simple types) \\
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1887:\textbf{MC3 is proved for all simple types on the
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1737:MC3 is proved for all simple types on the evaluation-generated core
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2066:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/README.md | sed -n '20,32p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/FRONTIER.md | sed -n '192,202p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'All five master conjectures MC1-MC5 are proved|MC3 \\(thick generation, all simple types; type A unconditional, other types conditional|MC5 \\(analytic HS-sewing at all genera\\)' /Users/raeez/chiral-bar-cobar/README.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   192	
   193	| # | Title | Venue | Core content |
   194	|---|-------|-------|-------------|
   195	| 1 | The ordered bar complex of a chiral algebra | Inventiones | E1-as-primitive, 6-object web, five E1 theorems |
   196	| 2 | Modular Koszul duality I: the five theorems | Annals | Theorems A-D+H, self-contained |
   197	| 3 | Modular Koszul duality II: the shadow tower | Annals | Full obstruction tower, Riccati, depth classification |
   198	| 4 | MC3 for all simple types | JAMS | Thick generation via multiplicity-free ell-weights |
   199	| 5 | The Drinfeld-Kohno bridge for chiral algebras | Duke | DK-0 through DK-3, Yangian identification |
   200	| 6 | Arithmetic shadows of chiral algebras | Compositio | Shadow Eisenstein, categorical zeta, depth decomposition |
   201	| 7 | Swiss-cheese structure of chiral Koszul pairs | Selecta | SC^{ch,top} operadic structure, PVA descent |
   202	| 8 | Analytic sewing for chiral algebras | Adv. Math. | HS-sewing criterion, Heisenberg Fredholm determinant |
 succeeded in 53ms:
    20	| **(A)** | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
    21	| **(B)** | Bar-cobar inversion: quasi-isomorphism on the Koszul locus |
    22	| **(C)** | Complementarity: deformations of A and obstructions of A^! are Lagrangian complements |
    23	| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g at all genera (uniform-weight lane) |
    24	| **(H)** | Hochschild duality: ChirHoch*(A) polynomial, Koszul-functorial |
    25	
    26	All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
    27	
    28	## The Six-Object Web
    29	
    30	Six objects built from the bar complex B(A), connected by three functors:
    31	
    32	- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
 succeeded in 53ms:
26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
codex
One candidate has escalated from scope drift to outright miscitation: Vol III cites “Vol I Theorem MC3” for the strict dg Lie / \(L_\infty\) comparison, but the concordance does not state MC3 that way. I’m pinning down the correct Vol I source before I write that finding.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '1312,1332p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '912,924p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'modular-homotopy-convolution|Convstr|strict model|same Maurer--Cartan moduli space|MC moduli space|three-pillar constraint|bifunctor in both slots|Robalo--Nickerson|strict model of an L_?infty|strict-versus-\\"'$L_'"\\\\infty\\"'$ comparison'"' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md /Users/raeez/chiral-bar-cobar/CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '80,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    80	\medskip\noindent
    81	All five descend from a single object. The modular $L_\infty$
    82	convolution algebra
    83	$\mathfrak{g}^{\mathrm{mod}}_\cA$ carries its $L_\infty$
    84	structure from the Feynman transform of the modular operad;
    85	the dg~Lie algebra of Definition~\ref{def:modular-convolution-dg-lie}
    86	is its strict model $\Convstr$, and the homotopy-invariant object
    87	is $\Definfmod(\cA)$
    88	(Theorem~\ref{thm:modular-homotopy-convolution}). The universal
    89	MC element $\Theta_\cA \in \MC(\gAmod)$ exists by the bar-intrinsic
    90	construction (Theorem~\ref{thm:mc2-bar-intrinsic}:
    91	$\Theta_\cA := D_\cA - d_0$ is MC because $D_\cA^2 = 0$).
    92	The shadow obstruction tower
    93	$\Theta_\cA^{\le 2} \to \Theta_\cA^{\le 3} \to \Theta_\cA^{\le 4}
    94	\to \cdots$ consists of its finite-order projections.
    95	Theorems~A--C are consequences of the MC package;
    96	Theorems~D and~H are scalar and Hochschild outputs.
    97	The governing equation is
    98	$D_\cA(\Theta_\cA) + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$.
    99	
 succeeded in 53ms:
  1312	 Theorem~\ref{thm:planted-forest-tropicalization}).
  1313	\item $\barB(\cA)$ is a $\mathrm{Ch}_\infty$-algebra
  1314	 (Theorem~\ref{thm:cech-hca}).
  1315	\item $B_\kappa \dashv \Omega_\kappa$ is a Quillen equivalence
  1316	 (Theorem~\ref{thm:quillen-equivalence-chiral}).
  1317	\item The shadow algebra $\cA^{\mathrm{sh}}$ is a homotopy invariant
  1318	 (Theorem~\ref{thm:shadow-homotopy-invariance}).
  1319	\item The one-slot obstruction constrains the MC3 categorical lift:
  1320	 $\operatorname{hom}_\alpha$ accepts $\infty$-morphisms in either slot
  1321	 separately but not both simultaneously
  1322	 (\cite[Theorem~6.6]{RNW19}).
  1323	\item The secondary Borcherds operations $F_n$ of \cite{MS24} at
  1324	 degree $n \geq 3$ are identified with the shadow obstruction tower obstruction
  1325	 classes $o_n(\cA)$
  1326	 (Proposition~\ref{prop:borcherds-shadow-identification}):
  1327	 $F_3 = o_3$ (cubic shadow), $F_4 = o_4$ (quartic resonance),
  1328	 $F_n = o_n$ (higher obstructions). The identification is
  1329	 structural at genus~$0$; at genus $g \geq 1$ the bar side
  1330	 acquires modular corrections with no \v{C}ech counterpart
  1331	 in~\cite{MS24}.
 succeeded in 53ms:
   912	\begin{remark}[Envelope-shadow complexity of standard families]
   913	\label{rem:envelope-shadow-complexity-standard}
   914	The envelope-shadow complexity recovers the shadow depth
   915	classification
   916	(Definition~\ref{def:shadow-depth-classification}):
   917	\begin{center}
   918	\renewcommand{\arraystretch}{1.15}
   919	\begin{tabular}{@{}llcl@{}}
   920	\toprule
   921	\textbf{$R$} & \textbf{$\Uvert(R)$}
   922	 & $\chienv(R)$ & \textbf{Class} \\
   923	\midrule
   924	$R$ abelian & Heisenberg & $2$ & $\mathbf{G}$ \\
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar/CLAUDE.md:915:**Convolution**: dg Lie Conv_str is strict model of L-inf Conv_inf. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:919:**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:939:| `thm:modular-homotopy-convolution` | `theorem` | 10383 | Modular homotopy convolution |
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:81:(strict model $\Convstr$);
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:125:brackets that $\Convstr$ truncates. The tower
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:199:(ii)~the bar complex with quartic contacts (strict model
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:200:$\Convstr$);
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:203:resonance, so the strict model is a genuine truncation;
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:2935:$\Convstr(\bar{B}^{\mathrm{ch}}(\cA),\, \cA^!)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/w3_holographic_datum.tex:151:$\Convstr(C^!_{\mathrm{ch}}, P^{\mathrm{ch}})$ because
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:144:(strict model $\Convstr$);
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:147:the strict model is already the homotopy-invariant object
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:23:$\Convstr(\barB^{\Eone}(\cA), \chirLie)$ on ordered configurations,
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:91:(strict model $\Convstr$);
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:5931:(the strict model $\Convstr$ of $\Convinf$; Convention~\ref{rem:two-level-convention})
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:137:$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$. The strict model $\Convstr$ carries a nonzero cubic shadow at degree~$3$
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:260:(ii)~the CE complex and bar resolution (strict model $\Convstr$);
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:27:$\Pinf$-deformation complex (the strict model of the corresponding
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:36:convolution model $\Convstr$ is a proper truncation: all transferred
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:190:that have no counterpart in the strict model.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '10549,10606p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 10549	$\Convstr(C,P) := \operatorname{Hom}_{\mathbb{S}}(C,P)$ is a
 10550	strict model: $\ell_1 = D$, $\ell_2 = [-,-]$,
 10551	$\ell_n = 0$ for $n \geq 3$.
 10552	The full chiral operadic identification, including
 10553	functoriality with respect to $\infty$-morphisms
 10554	and the one-slot obstruction, is
 10555	Theorem~\textup{\ref{thm:operadic-homotopy-convolution}}.
 10556	\end{theorem}
 10557	
 10558	\begin{proof}[References]
 10559	The operadic $L_\infty$ structure is constructed via homotopy
 10560	transfer through the $\operatorname{Hom}$~functor
 10561	(Loday--Vallette~\cite[Thm~10.3.8]{LV12}; Robert-Nicoud--Wierstra~\cite[Thm~4.1]{RNW19}); the explicit
 10562	transferred brackets are given by van~der~Laan~\cite{vdL03}.
 10563	The strict dg~Lie algebra is the binary truncation.
 10564	\end{proof}
 10565	
 10566	\begin{theorem}[Modular homotopy convolution;
 10567	\ClaimStatusProvedHere]
 10568	\label{thm:modular-homotopy-convolution}
exec
/bin/zsh -lc "rg -n 'MC4 is solved|MC4 is proved|MC4 proved|MC5 proved|MC5 is proved|MC5 resolved|MC5 partially proved|analytic HS-sewing package established|analytic part proved' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '"'!compute/**'"' -g '"'!**/.claude/**'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~MC4|Theorem MC4|Vol~I Theorem~MC4|Vol~I Theorem MC4|Vol~I Theorem~MC3|Vol~I Theorem MC3|Theorem~MC5|Theorem MC5' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!tmp_standalone_audit/**'"' -g '"'!audit_campaign_*/**'"' -g '"'!rectification_*/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"' -g '"'!**/.claude/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:700: ; already a central object in Volume~I, where MC4 is solved by weight
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:49:The full affine Yangian $Y(\widehat{\mathfrak{gl}}_1) \cong \mathcal{W}_{1+\infty}$ at the self-dual level is a key object in the Volume~I landscape, where MC4 is solved by weight stabilization. The Yangian $R$-matrix is the DK-0 shadow.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:390:and MC4 is solved by weight stabilization).
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:72:Every Vol III MC5 citation is now either explicitly scoped to the analytic HS-sewing lane, explicitly scoped to the analytic completion programme, or carries the full canonical caveat about the conjectural genuswise BV/BRST/bar identification. No Vol III location claims MC5 proved as a whole.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:26:and this is the form in which MC4 is proved. At the noncompact scale,
/Users/raeez/calabi-yau-quantum-groups/notes/VISION.md:138:- Connection to Vol I: W_{1+infty} is already in the standard landscape! Its MC4 is solved by weight stabilization. The Yangian R-matrix is DK-0.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:439:Chirality is proved for $\mathcal{N}=4$ SYM (Theorem~\ref{thm:cl-n4-chirality}); the general case remains conjectural. See \cite{CDG20,GKW24,Zeng23} for related work. The analytic HS-sewing lane of MC5 is proved at all genera in Volume~I (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the remaining obstruction is the chirality verification for general twisted gauge theories.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:807:Individual levels are established \cite{BD04,CG17,CWY18}; the analytic HS-sewing lane of MC5 is proved at all genera in Volume~I, while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes, so the bar-cobar side of the iterated identification is accessible subject to that conjectural step.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:21:All other occurrences of "MC5" / "MC5 proved" in Vol II were already
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:61:    \emph{Status: Resolved at all genera} (Volume~I, MC5 proved).
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:65:    \emph{Status: Analytic lane of MC5 proved at all genera; the
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/vol2_mc5_status_sweep.md:82:  of MC5 is proved at all genera ... the full genuswise BV/BRST/bar
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:661:\item \textbf{Higher-genus $A_\infty$ structure}: This paper works on $\C \times \R$ (genus 0 in $\C$). The monograph's genus tower should lift to $A_\infty$ with spectral parameters. \emph{Status: Analytic lane of MC5 proved at all genera; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; genuswise chain-level BV/BRST/bar identification conjectural (class~M chain-level false).} The genus-$1$ spectral braiding is treated by the elliptic spectral dichotomy (Theorem~\ref{thm:elliptic-spectral-dichotomy}): the Coisson bracket $c_0 = \{a{}_0 b\}$ controls whether curvature and braiding decouple (Cartan type) or entangle (Yangian type). At genus~$g \geq 2$, the Feynman-diagrammatic identification with the algebraic bar differential is established by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}) and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}), subject to the conjectural genuswise chain-level BV/BRST/bar identification ($D^{\mathrm{co}}$-level proved).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1592:the analytic lane of MC5 is proved at all genera; BV=bar in
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:705:Theorem MC4 of the monograph~\cite{LorgatVolI}.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:33:The strict-versus-$L_\infty$ comparison is Vol~I Theorem~MC3 (Robalo--Nick\-erson--Welch\-er 2019 bifunctoriality failure in both slots resolves by treating one slot at a time). The MC moduli coincidence is Vol~I Theorem~MC4. Here we only transport the statement: $\Phi$ sends cyclic $A_\infty$-objects to chiral algebras compatibly with the bar construction (Theorem~CY-A(ii)), so the convolution bracket on the CY side is pulled back from the chiral convolution bracket of Vol~I.





thinking
**Inspecting audit scope**

I need to consider whether the standalone N2_mc3_all_types section titles should be included, even though they might be outdated and broader. The user is looking for an exhaustive audit surface. I should search the output for N2_mc3_all_types.tex and FRONTIER to see if there's any overclaim. The scope of the audit might become large, so I need to decide if we include all live files with misstatements and inspect for patterns regarding MC3 overclaims.
thinking
**Clarifying evaluation content**

I'm looking at the title in FRONTIER.md at line 198, which mentions "MC3 for all simple types | JAMS | Thick generation via multiplicity-free ell-weights." I wonder if the core content clarifies the evaluation-generated core, but it doesn’t seem to do so, and I think it could mislead. Additionally, line 324 of working_notes_frontier notes that "MC3 (proved for all simple types)" establishes thick generation by evaluation modules, which may imply the evaluation core. I need to address these potential misleading points.
thinking
**Searching MC5 Conjectural Status**

I see that the user is asking about the "MC5 chain-level conjectural status propagated." To respond effectively, I need to determine if this information is primarily found in the Volume I README; that seems likely, but there might be more to uncover. I'll need to search for "MC5 analytic HS-sewing at all genera" across volumes 1, 2, and 3 while excluding compute artifacts. The user is particularly interested in a cross-volume bridge audit.
thinking
**Considering findings and details**

I’ve got five findings, but the user is asking for "exact file:line in EACH volume.” I should think about whether I can include line references for each finding across volumes. If some findings only show up once, it might work to give just that specific volume's details. But then again, "in EACH volume" sounds like they want complete coverage. To be thorough, I’ll look at cross-volume grouped findings as well, ensuring an exhaustive audit.
thinking
**Inspecting lines and content**

I need to check specific lines in the document, like lines 181-183 and 201-202 of the "calabi-yau-quantum-groups" section. There's a mention that relates to Volume II, MC3, discussing the Yangian and how it might connect to the degree-(1,1) collision residue. However, it feels like there's some confusion since MC3 operates differently than the Yangian mentioned. I’ll need to verify these details and search both volumes for related theorems, focusing on the Yangian from collision residue for accuracy.
codex
Another subtle one surfaced in Vol III: a paragraph now uses “MC3” as shorthand for “Yangian from the degree-(1,1) bar residue.” That is not what MC3 is in the concordance. I’m tracing the correct DK label before I count it as a finding.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '4708,4720p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex | sed -n '136,146p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Yangian from collision residue|degree-\\(1,1\\)|ordered bar complex.*Yangian|DK-0|DK-1|Yangian identification|r\\"'^'"\\{coll\\}|Res\\"'^'"\\{coll\\}|categorical CG' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:derived-dk-affine|cor:dk23-all-types|cor:dk2-thick-generation-all-types|thm:rtt-all-types' /Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4708	$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\
  4709	 & persistence off it & coderived persistence conjectural & \S\ref{subsec:coderived-ran} \\[2pt]
  4710	$C_{\mathrm{mod}}$ & Shifted symplectic complementarity & \textbf{Proved} & Thms~\ref{thm:quantum-complementarity-main}, \\
  4711	 & (PTVV Lagrangian embedding) & & \ref{thm:ambient-complementarity-fmp} \\[2pt]
  4712	Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
  4713	DK & DK-0/1/$1\frac{1}{2}$: chain-level, eval-locus, lattice; & DK-0/1/$1\frac{1}{2}$: proved (all types); & Thms~\ref{thm:derived-dk-affine}, \\
  4714	 & DK-2/3: generated-core DK comparison; & DK-2/3: \textbf{proved} (eval-gen.\ core, all types; $\mathcal{O}_{\mathrm{poly}}$ only on the separate type-$A$ thick-generation lane; & \ref{thm:derived-dk-yangian}, \ref{thm:factorization-dk-eval}, \\
  4715	 & DK-4/5: dg-shifted/triple bridge & uses Molev PBW \cite{molev-yangians}); DK-4: ML proved, alg.\ id.\ open; DK-5: \textbf{proved for $\mathfrak{sl}_2$} (FRT, Prop.~\ref{prop:dk5-sl2-frt}); general: conj. & \ref{conj:dk-fd-typeA}, \ref{cor:dk23-all-types}, \ref{thm:rtt-mittag-leffler}; Conj.~\ref{conj:full-dk-bridge} \\[2pt]
  4716	$H$ & Chiral Hochschild: $\ChirHoch^n = 0$ for $n > 2$, $P(t) = 1+t^2$; & \textbf{Proved} (generic level, & Thms~\ref{thm:w-algebra-hochschild}, \\
  4717	 & concentration in $\{0,1,2\}$ (de~Rham bound on curve); & critical level: ProvedElsewhere) & \ref{thm:virasoro-hochschild}, \ref{thm:critical-level-cohomology}; \\
  4718	 & Koszul functoriality via Connes~$S$ & & Thm~\ref{thm:main-koszul-hoch} \\
  4719	\bottomrule
  4720	\end{tabular}
 succeeded in 52ms:
   136	\hline
   137	Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
   138	DS-bar & Bar-cobar commutes with DS reduction (monograph Thm~ds-koszul-intertwine) & Proved (Vol~I) & W-algebra axis \\
   139	Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
   140	DK/YBE & $r(z) = \int_0^\infty e^{-\lambda z}\{\cdot_\lambda\cdot\}\,d\lambda$ provides DK-0 shadow & Proved (Laplace) & MC3 (all-types evaluation-core DK comparison proved; post-core extension still frontier) \\
   141	MC2 & Bar-intrinsic $\Theta_\cA$ (Vol~I Thm~\ref*{V1-thm:mc2-bar-intrinsic}) & Proved & Shadow obstruction tower \\
   142	MC4 & Strong completion towers (Vol~I Thm~\ref*{V1-thm:completed-bar-cobar-strong}) & Proved & $\mathcal{W}_\infty$ unconditional \\
   143	PVA-Coisson & PVA descent at $X = \mathrm{pt}$ recovers Coisson structure & Proved & Deformation theory \\
   144	W-algebras & Feynman-diagrammatic $m_k$ matches bar differential at genus 0 & Proved (genus 0) & MC5 (analytic HS-sewing proved at all genera, Vol~I Thm~\ref*{thm:general-hs-sewing}; genuswise BV/BRST/bar identification conjectural; $D^{\mathrm{co}}$-level comparison for all shadow classes, Vol~I Thm~\ref*{V1-thm:bv-bar-coderived}; chain-level false for class~M) \\
   145	Genus-1 curvature & $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ from Feynman Arnold defect & Proved (genus 1) & MC5 (analytic HS-sewing proved at all genera, Vol~I; genus-$0$ algebraic BRST/bar proved; $D^{\mathrm{co}}$-level BV=bar proved for all shadow classes; chain-level BV/BRST/bar conjectural) \\
   146	(H1)--(H4) & Analytic hypotheses define physics-to-algebra functor & Programme & Programme VI \\
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:1996:| `cor:mc3-all-types` | `corollary` | 3987 | Three-layer MC3 status after categorical CG closure |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:2472:| `thm:gaudin-yangian-identification` | `theorem` | 1631 | Gaudin--Yangian identification |
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:503:%: This is the Laplace kernel r^L(z), not the collision residue r^{coll}(z).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:504:% Collision residue: r^{coll}(z) = (c/2)/z^3 + 2T/z (poles at odd orders).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:8:$\Ainf$ operations and DK-0 bridge; \emph{dualities}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:94:\subsection{DK-0 Laplace verification: the standard landscape}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:95:\label{sec:DK-0}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:97:\begin{proposition}[DK-0 Laplace bridge for five families; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:163:entry in the DK-0 table above. Since
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:885:\begin{remark}[DK-0 bridge for the DDCA]
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:906:DK-0 bridge, extending
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1473:Item (v) follows from the DK-0 Laplace verification
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3727:the DK-0 Laplace bridge
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:727:The Yangian identification
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:310:The open-colour Yangian identification
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3354:(equation~\eqref{eq:betagamma-R}). The DK-0 Laplace
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3961:(MC3 categorical CG closure and the generated-core DK comparison are
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3998:\textup{(}categorical CG closure plus the generated-core DK comparison\textup{)}
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4266:DK-0/1 (chain/eval) & Proved & Proved (subsumed) \\
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4547:DK-0/1 for level-$1$ KM algebras, obtained without the RTT
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:1972:| `cor:dk2-thick-generation-all-types` | `corollary` | 1532 | Thick generation for all simple types |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:2013:| `thm:derived-dk-affine` | `theorem` | 162 | Chain-level derived Drinfeld--Kohno for affine algebras |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:2020:| `cor:dk23-all-types` | `corollary` | 878 | Evaluation-generated-core DK comparison for all simple types via sectorwise convergence |
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:2123:| `thm:rtt-all-types` | `theorem` | 1174 | RTT presentation and MC3 for all simple types |
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1856:\textup{(}Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1895:(Corollary~\ref{cor:dk2-thick-generation-all-types}).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3272: (Corollary~\ref{cor:dk23-all-types}).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4574:monodromy comparison (Theorem~\ref{thm:derived-dk-affine}).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4713:DK & DK-0/1/$1\frac{1}{2}$: chain-level, eval-locus, lattice; & DK-0/1/$1\frac{1}{2}$: proved (all types); & Thms~\ref{thm:derived-dk-affine}, \\
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4715: & DK-4/5: dg-shifted/triple bridge & uses Molev PBW \cite{molev-yangians}); DK-4: ML proved, alg.\ id.\ open; DK-5: \textbf{proved for $\mathfrak{sl}_2$} (FRT, Prop.~\ref{prop:dk5-sl2-frt}); general: conj. & \ref{conj:dk-fd-typeA}, \ref{cor:dk23-all-types}, \ref{thm:rtt-mittag-leffler}; Conj.~\ref{conj:full-dk-bridge} \\[2pt]
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6279:\textup{(}Theorems~\ref{thm:derived-dk-affine}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6340: Theorems~\ref{thm:derived-dk-affine}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6361: \textup{(}Corollary~\ref{cor:dk23-all-types}\textup{)}
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7806: (Corollary~\ref{cor:dk23-all-types}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2234: Theorem~\ref{V1-thm:derived-dk-affine}).

thinking
**Exploring theorem labeling**

I’m looking into the theorem registry for `thm:rtt-all-types`. The title could potentially be broader, but it might be specific to internal purposes. I’m also considering if the canonical evaluation is still core. Perhaps the theorem label should be placed in volume 1 chapters; it may need some corrections. I think I should inspect the theorem statement in that context and do a search to clarify things. It’s a bit of a puzzle!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '4070,4090p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '3998,4044p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4070	\end{remark}
  4071	
  4072	\subsection{Landscape of the MC3 extension}
  4073	\label{sec:mc3-extension-landscape}
  4074	
  4075	\begin{conjecture}[Type-independence of the remaining MC3 completion mechanisms;
  4076	 \ClaimStatusConjectured]
  4077	\label{conj:mc3-automatic-generalization}
  4078	\label{conj:mc3-proof-step-analysis}% backward compatibility (renamed from prop:)
  4079	Let~$\mathfrak{g}$ be simple. Assume that, beyond the all-types
  4080	categorical CG theorem and the evaluation-generated-core DK
  4081	equivalence, the following packets are available in the relevant
  4082	shifted/completed category:
  4083	\begin{enumerate}[label=\textup{(\roman*)}]
  4084	\item shifted-prefundamental generation on the relevant compact core;
  4085	\item the Mittag--Leffler / pro-Weyl hypotheses on the Weyl truncation
  4086	 towers;
  4087	\item a compatible compact-completion formalism carrying compact-core
  4088	 equivalences to the desired completed category.
  4089	\end{enumerate}
 succeeded in 52ms:
  3998	criterion for category~$\mathcal{O}$
  3999	\cite{Hernandez05, HJZ25}, and \textup{(c)}~the
  4000	Gautam--Toledano Laredo equivalence~\cite{GTL17}
  4001	identifying Drinfeld polynomial data between quantum
  4002	loop algebras and Yangians.
  4003	The new content is the observation
  4004	that these three inputs, combined with the character identity
  4005	(Proposition~\ref{prop:character-cg-all-types}), yield the
  4006	categorical CG decomposition for \emph{all} types, replacing
  4007	the minuscule hypothesis of
  4008	Proposition~\ref{prop:categorical-cg-typeA}.
  4009	The multiplicity-free property is not contained in a single
  4010	reference: for simply-laced types it follows from
  4011	$(q,t)$-character theory~\cite{Nakajima04}; for classical types
  4012	from explicit formulas~\cite{ChariMoura06}; for all types the
  4013	Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} computes the
  4014	$q$-character and confirms multiplicity-freeness.
  4015	The block criterion transfers from quantum affine to Yangian
  4016	because it is purely combinatorial, depending only on Drinfeld
  4017	polynomial data identified by~\cite{GTL17}.
exec
/bin/zsh -lc "rg -n 'MC3|DK bridge|evaluation-generated core|compact objects|full categorical equivalence|categorical structure|uniquely determines the chiral algebra' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
181:$R$-matrix in its degree-$(1,1)$ component; the DK bridge (Volume~II,
182:MC3 for all simple types) extends this to the full categorical
186:\begin{proposition}[KL and the DK bridge]
201:(right). The DK bridge (MC3) provides the horizontal equivalence
202:at the level of compact objects.
231:of MC3 (proved on the evaluation-generated core for all simple types, Volume~I/II). The $\Etwo$
264:This is the content of Volume~II, MC3: the ordered bar complex
581:solved by the DK bridge (MC3 for all simple types): the categorical
582:data of $\Rep_q(\frakg)$ uniquely determines the chiral algebra
codex
Vol III’s quantum-group chapter is dirtier than the first pass suggested. It uses “MC3” for three different things: evaluation-core categorical CG, full categorical equivalence, and even the Yangian-from-bar-residue statement. Those are not the same claim.
exec
/bin/zsh -lc "rg -n 'Volume~II, MC3|Vol~I/II|DK bridge \\(MC3|MC3\\) provides|MC3: the ordered bar complex|MC3 for all simple types|MC3 \\)' /Users/raeez/calabi-yau-quantum-groups/chapters -g '"'!compute/**'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'MC3 \\(all simple types\\)|MC3 for all simple types|MC3 \\(proved for all simple types\\)|MC3 \\(categorical CG\\)|MC3 proved on the evaluation-generated core|post-core conditional|evaluation core proved' /Users/raeez/chiral-bar-cobar-vol2/chapters -g '"'!compute/**'"' -g '"'!**/.claude/**'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'MC3 for all simple types|MC3 \\(proved for all simple types\\)|MC3 \\(all simple types\\)|all five master conjectures MC1-MC5 are proved|MC5 analytic HS-sewing at all genera' /Users/raeez/chiral-bar-cobar -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!tmp_standalone_audit/**'"' -g '"'!audit_campaign_*/**'"' -g '"'!rectification_*/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1232:\item MC3 (categorical CG): tensor products of
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1563:DK-3 & MC3 (categorical CG) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1088: & \checkmark\;MC3 (all simple types) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_yangian.tex:2313:\begin{remark}[MC3 for all simple types: evaluation core proved, post-core conditional]
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:182:MC3 for all simple types) extends this to the full categorical
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:201:(right). The DK bridge (MC3) provides the horizontal equivalence
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:264:This is the content of Volume~II, MC3: the ordered bar complex
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:581:solved by the DK bridge (MC3 for all simple types): the categorical
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:237:Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in the Vol~II 3D quantum gravity treatment, \ref{part:3d-qg} there). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality on propagates from Theorem~\ref{thm:cy-shadow-cohft}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:432: \item $Y(\frakg)$: the Yangian ($\Eone$-sector, Volume~II, MC3);
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:391:\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:324:MC3 (proved for all simple types) establishes thick generation
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:241:\subsection{Consequence: MC3 for all simple types}
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:257:\begin{corollary}[MC3 for all simple types]
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:710:\section{Corollary: MC3 for all simple types}\label{sec:mc3}
/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:733:\begin{corollary}[MC3 for all simple types]
/Users/raeez/chiral-bar-cobar/FRONTIER.md:198:| 4 | MC3 for all simple types | JAMS | Thick generation via multiplicity-free ell-weights |
/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:1046: & \checkmark\;MC3 (all simple types) \\

thinking
**Evaluating findings in documents**

I’m looking into potential findings in "volume1 standalone N2_mc3_all_types.tex" and "working_notes_frontier." I need to check the context of "N2_mc3_all_types" and figure out if it’s a standalone preprint or paper—maybe it's live now? I should include relevant information. Alright, let’s search for any open resources or updates related to this topic.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex | sed -n '248,266p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex | sed -n '728,742p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex | sed -n '1038,1048p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex | sed -n '322,326p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   248	\cite[Vol.\ I]{LorgatMKD}. The third master conjecture (MC3) of
   249	the modular Koszul duality programme asserts that the degree-$3$
   250	component of $\Theta_\cA$, when restricted to the
   251	evaluation-generated core, determines all higher-degree
   252	components through thick generation and pro-nilpotent completion
   253	of the ambient factorization category. The present paper
   254	removes the only remaining Lie-type obstacle to MC3 for Yangian
   255	targets:
   256	
   257	\begin{corollary}[MC3 for all simple types]
   258	\label{cor:mc3-all-types-intro}
   259	For every finite-dimensional simple Lie algebra $\fg$, the
   260	categorical Clebsch--Gordan step of MC3 for the Yangian
   261	$\Yh$-target holds: the degree-$3$ shadow projection
   262	$\pi_{3,0}(\Theta_\cA^{\Eone})$, combined with the
   263	evaluation-core Drinfeld--Kohno comparison, determines all
   264	higher-degree projections of the Maurer--Cartan element on the
   265	thick subcategory generated by the fundamental evaluation
   266	modules and the prefundamental simples.
 succeeded in 52ms:
   728	\]
   729	whose degree-$r$ projection $\pi_{r,0}(\Theta_\cA)$ is the
   730	shadow datum at depth $r$; see~\cite{LorgatMKD} for the detailed
   731	construction.
   732	
   733	\begin{corollary}[MC3 for all simple types]
   734	\label{cor:mc3-all-types}
   735	Let $\fg$ be any finite-dimensional simple Lie algebra and let
   736	$\cA_\fg = V_k(\fg)$ be the affine vertex algebra at level $k$
   737	away from the critical level $k = -h^\vee$. The degree-$3$
   738	shadow projection $\pi_{3,0}(\Theta_{\cA_\fg})$, together with
   739	the evaluation-core Drinfeld--Kohno comparison, determines all
   740	higher-degree projections $\pi_{r,0}(\Theta_{\cA_\fg})$ for
   741	$r \geq 4$ on the thick closure of fundamental evaluation
   742	modules and negative prefundamental simples in $\DK_\fg$.
 succeeded in 51ms:
  1038	$R$-matrix from gauge propagator
  1039	 & \checkmark\;\cite{CWY18}
  1040	 & \checkmark\;$\operatorname{Res}^{\mathrm{coll}}_{0,2}$ \\
  1041	YBE from CYBE
  1042	 & \checkmark\;\cite{CWY18}
  1043	 & \checkmark\;Arnold relation on $\overline{\mathcal{M}}_{0,4}$ \\
  1044	Yangian symmetry
  1045	 & \checkmark\;\cite{CWY18}
  1046	 & \checkmark\;MC3 (all simple types) \\
  1047	BCFW recursion
  1048	 & \checkmark\;\cite{CostelloP2201}
 succeeded in 51ms:
   322	\subsection{DK-4: Beyond the evaluation core}
   323	
   324	MC3 (proved for all simple types) establishes thick generation
   325	of the DK category by evaluation modules. DK-4 asks whether
   326	this extends to the full module category.


thinking
**Searching for connections**

I need to search Volume II for potential omissions related to holomorphic topology since the output only shows that section. The thqg_gravitational_yangian remark seems correct. I found lines in `vol2/connections/concordance.tex`. Next, I should check Volume III for similar issues regarding quantum group representations. I’m also looking for distinctions in propositions regarding compact objects. It seems there might be a difference between “evaluation-generated core” and all compact objects. I'll clarify this by searching in Volume I or II.
thinking
**Clarifying terminology**

I need to make an exact fix by replacing “at the level of compact objects” with either “on the evaluation-generated core” or “on the thick subcategory generated by evaluation modules.” The theorem statement earlier in standalone N2 mentions the "thick closure of fundamental evaluation modules and negative prefundamental simples in DK_g," which might relate to the evaluation-generated core. It seems important to use the exact phrase “evaluation-generated core” to ensure alignment. Let's get this right!
exec
/bin/zsh -lc "rg -n 'MC5 is proved|MC5 proved|all five master conjectures MC1-MC5 are proved|MC5 \\(analytic HS-sewing at all genera\\)|MC5 \\(sewing\\)|MC5 analytic HS-sewing at all genera|MC1 through MC5 are proved|MC5 resolved' /Users/raeez/chiral-bar-cobar -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!tmp_standalone_audit/**'"' -g '"'!audit_campaign_*/**'"' -g '"'!rectification_*/**'"' -g '"'!metadata/**'"' -g '"'!**/.git/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/README.md:26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex:911:MC5 (sewing) feed into the replica structure (G16).

thinking
**Looking into search volume**

I think I need to search for volume data regarding "MC5 proved." It seems there aren't any strong results besides compute audits. I should also consider searching for the broader term "MC5" to gather more insights. It feels like there's potential here, and I'm curious about what I might find. Let's see what the numbers say, as they could really shape my understanding!
exec
/bin/zsh -lc "rg -n 'MC5 is proved|MC5 proved|MC5 \\) provides|MC5 analytic HS-sewing lane|Vol~I, MC5\\)|Volume~I, MC5\\)|MC5 for all genera|MC5 \\(analytic|MC5 remains conjectural|MC5 is partially proved|MC5 is not fully proved' /Users/raeez/calabi-yau-quantum-groups -g '"'!compute/**'"' -g '"'!**/.git/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/topological_vertex_e1_engine.py:41:    the content of MC5 (analytic sewing) specialized to the E_1 sector.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex:315: MC5 analytic HS-sewing lane) to handle the non-compact directions.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2257: The sewing envelope $A^{\mathrm{sew}}$ (MC5 analytic HS-sewing lane) produces IndHilb-valued
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2634:\item \emph{Sewing parameter space} (Vol~I, MC5 analytic HS-sewing lane). The modular parameter $\tau$ of $E$ is the sewing parameter for the genus-1 Hilbert-Schmidt kernel. The genus-1 amplitude $F_1(A) = \kappa_{\mathrm{ch}}(A) \cdot \lambda_1^{\mathrm{FP}}$ is a function on $\cM_{1,1} = \cH/\mathrm{SL}_2(\Z)$ via $q = e^{2\pi i \tau}$.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2645:The recurrence is not ornamental. Every time the elliptic curve appears, it brings the same structural package: a modular parameter $\tau$, an $\mathrm{SL}_2(\Z)$ symmetry, a $q$-expansion, and a sewing/product/lift functor that converts genus-0 data into genus-1 data. The deeper observation is that $E$ serves as the \emph{modular clock} of the theory: it converts algebraic data (OPE coefficients, shadow invariants, root multiplicities) into analytic data (partition functions, automorphic forms, $L$-values) via the analytic HS-sewing lane of MC5 (the proved lane of Vol~I; the genuswise BV/BRST/bar identification of MC5 remains conjectural).
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3334:of MC5 remains conjectural). The frontier is the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:783: \item \emph{Gluing = sewing.} The toric diagram gluing rules (one vertex factor $C_{\lambda\mu\nu}$ per trivalent node, one propagator $(-q)^{|\lambda|}/z_\lambda$ per internal edge, sum over internal partitions) are the $\Eone$ sewing rules (Vol~I, MC5 analytic HS-sewing lane). The edge propagator $(-q)^{|\lambda|}/z_\lambda$ is the $\Eone$ bar complex pairing on $H^1(B^1)$.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:5:MC5 is not fully proved. What IS proved at all genera is the analytic HS-sewing package. The remaining genuswise BV/BRST/bar identification is still conjectural; at genus 0 the algebraic BRST/bar comparison is proved; tree-level amplitude pairing is conditional on `cor:string-amplitude-genus0`.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:15:> "The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural)."
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:17:The sweep added the explicit qualifier "MC5 analytic HS-sewing lane" (or equivalent) at every Vol III citation site where a bare "(Vol I, MC5)" reference could be misread as citing MC5 as a whole. Two sites were already explicitly scoped to "analytic completion programme" and needed no edit.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:22:   - Line 2253: "sewing envelope A^sew (MC5)" to "sewing envelope A^sew (MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:23:   - Line 2630: "Sewing parameter space (Vol I, MC5)" to "Sewing parameter space (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:24:   - Line 2641: "sewing mechanism of MC5" to "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:27:   - Line 319: "sewing envelope of Volume I, MC5" to "sewing envelope of Volume I, MC5 analytic HS-sewing lane"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:30:   - Line 196: "Sewing parameter (Vol I, MC5)" to "Sewing parameter (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:33:   - Line 526: "E_1 sewing rules (Vol I, MC5)" to "E_1 sewing rules (Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:61:- `chapters/examples/fukaya_categories.tex:319`: "MC5 analytic HS-sewing lane"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:62:- `working_notes.tex:2253`: "(MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:63:- `working_notes.tex:2630`: "(Vol I, MC5 analytic HS-sewing lane)"
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:64:- `working_notes.tex:2641`: "analytic HS-sewing lane of MC5 (the proved lane of Vol I; the genuswise BV/BRST/bar identification of MC5 remains conjectural)"





thinking
**Evaluating search output**

I noticed that the search output didn't show any live notes, which seems odd. The user mentioned looking across repositories, but I think focusing on main chapters and top-level documents could be sufficient. I wonder if I'll still need to note in the summary that I checked the live `.tex` and `.md` surfaces while excluding archived audit artifacts. There could be useful info in those areas, so it's worth considering!
thinking
**Considering title issues**

I'm wondering if there could be a problem with the title of volume 1's standalone N2 paper. Maybe we should check if the title matches the content. If the proposed title is "MC3 for all simple types," it might need renaming. If it’s the actual preprint title, it could be okay, but I’m concerned since it claims beyond evaluation core, which might be misleading. I’m checking possible issues with volume 2 too, but it seems fine. Also need to verify line 29 in volume 3.
thinking
**Checking citation concerns**

I’m realizing that the three-pillar constraint in the CLAUDE section isn’t necessarily wrong, but the user wanted to see the actual file contents. It might be a weak source. In the live volume, the strict model and homotopy-invariant object are part of the modular-homotopy-convolution theorem. So, I think lines 29 and 33 should reference that theorem instead of just citing "§ MC3." I'm eager to make that adjustment for clarity!
thinking
**Analyzing findings**

I’m considering whether the introduction line 391 and the quantum_group_reps line 181 can be grouped together under one heading. Especially since volume 3 seems to make claims that go beyond just dropping a qualifier. I need to see if the README contradiction in volume 1 is unique, as it presents both MC3 and MC5 issues. Separating it into two findings might work better since there are independent problems on one line. I want to ensure everything is accurately captured!
thinking
**Inspecting document status**

Since the user is looking for an exact fix, I think rewriting the line will address both issues. Now, I need to check volumes 1, 2, and 3 to see if any status tables or documents mistakenly claim MC5 is fully proved. I’ll search through the live surfaces in volumes 2 and 3. So far, it looks like there might not be any other findings related to MC5. I should note in the summary that the MC5 chain-level caveat appears in the examined volumes, while the failure only persists in the volume 1 README.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex | sed -n '1070,1090p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex | sed -n '1028,1048p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1028	\begin{tabular}{@{}p{5.2cm}@{\;\;}c@{\;\;}c@{}}
  1029	\toprule
  1030	\textbf{Result / structure}
  1031	 & \textbf{Costello et al.}
  1032	 & \textbf{This monograph} \\
  1033	\midrule
  1034	\multicolumn{3}{@{}l}{\emph{Genus $0$}} \\[2pt]
  1035	Tree-level $n$-point amplitudes
  1036	 & \checkmark\;\cite{CostelloP2201}
  1037	 & \checkmark\;$\mathrm{Sh}_{0,n}(\Theta_\cA)$ \\
  1038	$R$-matrix from gauge propagator
  1039	 & \checkmark\;\cite{CWY18}
  1040	 & \checkmark\;$\operatorname{Res}^{\mathrm{coll}}_{0,2}$ \\
  1041	YBE from CYBE
  1042	 & \checkmark\;\cite{CWY18}
  1043	 & \checkmark\;Arnold relation on $\overline{\mathcal{M}}_{0,4}$ \\
  1044	Yangian symmetry
  1045	 & \checkmark\;\cite{CWY18}
  1046	 & \checkmark\;MC3 (all simple types) \\
  1047	BCFW recursion
 succeeded in 52ms:
  1070	\begin{tabular}{@{}p{5.2cm}@{\;\;}c@{\;\;}c@{}}
  1071	\toprule
  1072	\textbf{Result / structure}
  1073	 & \textbf{Costello et al.}
  1074	 & \textbf{This monograph} \\
  1075	\midrule
  1076	\multicolumn{3}{@{}l}{\emph{Genus $0$}} \\[2pt]
  1077	Tree-level $n$-point amplitudes
  1078	 & \checkmark\;\cite{CostelloP2201}
  1079	 & \checkmark\;$\mathrm{Sh}_{0,n}(\Theta_\cA)$ \\
  1080	$R$-matrix from gauge propagator
  1081	 & \checkmark\;\cite{CWY18}
  1082	 & \checkmark\;$\operatorname{Res}^{\mathrm{coll}}_{0,2}$ \\
  1083	YBE from CYBE
  1084	 & \checkmark\;\cite{CWY18}
  1085	 & \checkmark\;Arnold relation on $\overline{\mathcal{M}}_{0,4}$ \\
  1086	Yangian symmetry
  1087	 & \checkmark\;\cite{CWY18}
  1088	 & \checkmark\;MC3 (all simple types) \\
  1089	BCFW recursion
codex
I’ve covered MC3 and MC5 deeply. I’m doing a quick status sanity pass on MC1, MC2, and MC4 now so the final report doesn’t miss a quieter drift while focusing on the headline failures.
exec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -g '"'!compute/**'"' -g '"'!wave*/**'"' -g '"'!archive/**'"' -g '"'!tmp_standalone_audit/**'"' -g '"'!audit_campaign_*/**'"' -g '"'!rectification_*/**'"' -g '"'!metadata/**'"' 'MC1|MC2|MC4' /Users/raeez/chiral-bar-cobar | rg 'proved|conditional|conject|solved|resolved|open|partial|partially'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -g '"'!compute/**'"' -g '"'!**/.claude/**'"' 'MC1|MC2|MC4' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | rg 'proved|conditional|conject|solved|resolved|open|partial|partially'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
/Users/raeez/chiral-bar-cobar/README.md:26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
/Users/raeez/chiral-bar-cobar/FRONTIER.md:21:### MC1-MC4 proved; MC5 partially proved
/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:2229:MC1 through MC4 are proved; MC5 is partially proved, with
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:3401:The MC4 splitting: MC4${}^+$ (positive towers, including $\cW_{1+\infty}$, affine Yangians, and RTT, solved by weight stabilisation) vs.\ MC4${}^0$ (resonant towers, including Virasoro and non-quadratic $\cW_N$, reduced to finite resonance by Theorem~\ref{thm:resonance-filtered-bar-cobar}). The resonance rank~$\rho(\cA)$ classifies completion difficulty. The resonance completion theorem (Theorem~\ref{thm:platonic-completion}): the positive-energy axiom gives finite-dimensional weight spaces, so weight-compatible SDR and finiteness of the weight-zero resonance space force $\rho(\cA) < \infty$.
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4795: MC4 is proved: the strong completion-tower theorem
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4841:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera while the genuswise BV/BRST/bar identification remains conjectural. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4847:MC1 & PBW concentration & \textbf{proved} & all standard families \\[2pt]
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4848:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4850:MC4 & $\mathcal{W}_\infty$ closure & \textbf{proved} & completion towers + weight cutoff \\[2pt]
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4855:\noindent\textbf{MC1} (PBW concentration): Bar cohomology of every standard-landscape chiral algebra concentrates in PBW degrees, proved for all standard families by explicit computation.
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:4873:The coefficient-stability criterion (Theorem~\ref{thm:coefficient-stability-criterion}) reduces convergence to finite matrix stabilization; the uniform PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1 to MC4. The problem splits into MC4$^+$ (positive towers, solved by weight stabilization; Theorem~\ref{thm:stabilized-completion-positive}) and MC4$^0$ (resonant towers, reduced to a finite-dimensional problem by Theorem~\ref{thm:resonance-filtered-bar-cobar}). The remaining example-specific task is coefficient stabilization on finite windows and H-level target identification.
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1404:MC4 is already solved by the chain-level content of
/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:941:Master conjectures MC1 through MC4 are \emph{proved} (PBW
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7780:Master conjectures MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural. MC3 holds for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual problem DK-4/5 (extension beyond evaluation modules) is downstream.
/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:85:The result upgrades the previously conjectural MC4 completion
/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:211:unconditionally solved. We call this the \emph{MC4${}^+$
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4503:\noindent\textsc{Status: master conjectures MC1 through MC4 are
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4563:MC4 splits into two sub-problems, both proved:
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:1685:\noindent\textsc{Status: master conjectures MC1 through MC4 are
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:49:The full affine Yangian $Y(\widehat{\mathfrak{gl}}_1) \cong \mathcal{W}_{1+\infty}$ at the self-dual level is a key object in the Volume~I landscape, where MC4 is solved by weight stabilization. The Yangian $R$-matrix is the DK-0 shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:228:Conjecture~\ref{conj:toroidal-e1} is conjectural (\ClaimStatusConjectured): a complete proof requires verifying associativity of the $\Eone$-chiral product directly from the OPE relations, since the BD locality approach applies only to commutative chiral algebras. The $\bC^* \times \bC^*$ realization (Conjecture~\ref{conj:toroidal-surface-factorization}) is a separate surface-factorization problem within the MC4 elliptic/double-affine extension problem.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:9:% Note: MC4 is now proved (thm:winfty-all-stages-rigidity-closure).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:26:and this is the form in which MC4 is proved. At the noncompact scale,
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:42:MC4 is now proved unconditionally via $W_N$ rigidity
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:496:This is the form in which MC4 was proved
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:700: ; already a central object in Volume~I, where MC4 is solved by weight
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:142:MC4 & Strong completion towers (Vol~I Thm~\ref*{V1-thm:completed-bar-cobar-strong}) & Proved & $\mathcal{W}_\infty$ unconditional \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:476:Master conjectures MC1 through MC4 of Volume~I are proved;
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:505: MC4${}^+$ solved by weight stabilization,
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:390:and MC4 is solved by weight stabilization).
/Users/raeez/calabi-yau-quantum-groups/compute/audit/vol3_mc5_status_sweep.md:15:> "The modular Koszul duality engine is now proved (Theorems A--D+H, MC1 through MC4, the analytic HS-sewing lane of MC5, and the 12-fold Koszulness characterization; the genuswise BV/BRST/bar identification of MC5 remains conjectural)."
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1565:DK-5 & MC3 + MC4 + MC5 (all genera; analytic and $D^{\mathrm{co}}$ lanes proved, chain-level conjectural)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:759:Open-string side proved (Theorems~\ref*{V1-thm:bar-semi-infinite-km}, \ref*{V1-thm:bar-semi-infinite-w}). MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes); the closed-string identification is now accessible via the all-genera bar-cobar framework, subject to that conjectural step.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex:1203:The 2D side is proved (Theorem~\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \cite{SV13,MO19}. MC4 is proved in Volume~I and the analytic lane of MC5 is proved at all genera (Chapter~\ref*{V1-chap:concordance}), while the genuswise chain-level BV/BRST/bar identification remains conjectural; $D^{\mathrm{co}}$-level BV=bar is proved for all shadow classes; the remaining obstruction is the 4D--2D bridge for general gauge groups.
/Users/raeez/calabi-yau-quantum-groups/notes/VISION.md:138:- Connection to Vol I: W_{1+infty} is already in the standard landscape! Its MC4 is solved by weight stabilization. The Yangian R-matrix is DK-0.



thinking
**Evaluating the theorem's credibility**

I'm considering if the importance of the theorem could be high, maybe even critical. It cites MC3/MC4 as evidence for a strict model and MC moduli, but perhaps it's misattributed, and the proof is valid elsewhere. If it's just the references that are incorrect, there might still be a way to preserve the theorem's validity. So, I'm leaning toward it being high in significance.
thinking
**Evaluating findings and sources**

I'm considering how to strengthen the findings by including canonical sources in Volume I and noting incorrect sites in other volumes. It's essential to pinpoint whether any findings are exclusive to Volume II, particularly regarding the holomorphic topological tables. The summary should note that I found 5 valid entries out of 26 checked. I need to ensure there are no false positives, so I'm re-evaluating each finding and confirming the details.
thinking
**Drafting final answer**

The user mentioned something about ground claims in the actual file contents. The search output shows that the content is read, and it looks like there are 26, including the rg surfaces. That sounds good! I should create a final answer with bullet points, possibly five of them. Each bullet can have clickable links separated by commas. I’ll make sure to be concise but still provide enough detail to be clear. Let's get to crafting that!
codex
I have the likely final set. I’m doing one last grounding pass on the DK-stage labels so the “MC3 vs DK-0/1” findings quote the right canonical source instead of relying on memory.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '94,104p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex | sed -n '4713,4715p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex | sed -n '138,141p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4713	DK & DK-0/1/$1\frac{1}{2}$: chain-level, eval-locus, lattice; & DK-0/1/$1\frac{1}{2}$: proved (all types); & Thms~\ref{thm:derived-dk-affine}, \\
  4714	 & DK-2/3: generated-core DK comparison; & DK-2/3: \textbf{proved} (eval-gen.\ core, all types; $\mathcal{O}_{\mathrm{poly}}$ only on the separate type-$A$ thick-generation lane; & \ref{thm:derived-dk-yangian}, \ref{thm:factorization-dk-eval}, \\
  4715	 & DK-4/5: dg-shifted/triple bridge & uses Molev PBW \cite{molev-yangians}); DK-4: ML proved, alg.\ id.\ open; DK-5: \textbf{proved for $\mathfrak{sl}_2$} (FRT, Prop.~\ref{prop:dk5-sl2-frt}); general: conj. & \ref{conj:dk-fd-typeA}, \ref{cor:dk23-all-types}, \ref{thm:rtt-mittag-leffler}; Conj.~\ref{conj:full-dk-bridge} \\[2pt]
 succeeded in 52ms:
    94	\subsection{DK-0 Laplace verification: the standard landscape}
    95	\label{sec:DK-0}
    96	
    97	\begin{proposition}[DK-0 Laplace bridge for five families; \ClaimStatusProvedHere]
    98	\label{prop:dk0-laplace-five-families}
    99	For each of the five standard families
   100	$\cA \in \{\mathcal{H}_k,\;
   101	\widehat{\mathfrak{sl}}_2,\;
   102	\mathrm{Vir}_c,\;
   103	\beta\gamma\text{/}bc,\;
   104	\mathcal{W}_3\}$,
 succeeded in 52ms:
   138	DS-bar & Bar-cobar commutes with DS reduction (monograph Thm~ds-koszul-intertwine) & Proved (Vol~I) & W-algebra axis \\
   139	Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
   140	DK/YBE & $r(z) = \int_0^\infty e^{-\lambda z}\{\cdot_\lambda\cdot\}\,d\lambda$ provides DK-0 shadow & Proved (Laplace) & MC3 (all-types evaluation-core DK comparison proved; post-core extension still frontier) \\
   141	MC2 & Bar-intrinsic $\Theta_\cA$ (Vol~I Thm~\ref*{V1-thm:mc2-bar-intrinsic}) & Proved & Shadow obstruction tower \\
codex
- [CRITICAL] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1943), [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1981), [Vol I README.md](/Users/raeez/chiral-bar-cobar/README.md:26) — PROBLEM: the canonical source says MC5 is only partially proved: analytic HS-sewing and coderived BV=bar are proved, but the genuswise chain-level BV/BRST/bar identification remains conjectural. The README still says “All five master conjectures MC1-MC5 are proved,” and it also flattens MC3 into a type-A/non-type-A split instead of the evaluation-core/post-core split recorded in the concordance. FIX: replace the whole README sentence with: `MC1 through MC4 are proved. MC3 is proved for all simple types on the evaluation-generated core; the post-core MC3c packet is unconditional in type A and conditional outside type A. MC5 is partially proved: analytic HS-sewing at all genera, the genus-0 algebraic BRST/bar comparison, and D^{co}-level BV=bar for all shadow classes are proved; the genuswise chain-level BV/BRST/bar identification remains conjectural (class M chain-level false), and the tree-level amplitude pairing is conditional.`

- [CRITICAL] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1850), [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1985), [Vol III introduction.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:391), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:181), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:201), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:581) — PROBLEM: Vol III upgrades MC3 from “proved on the evaluation-generated core; DK-4/5 downstream” to “full categorical equivalence,” “horizontal equivalence at the level of compact objects,” and “reconstruction solved.” That is broader than the live Vol I status surface. FIX: narrow every one of these to the evaluation-generated core. Concretely: at `introduction.tex:391` replace `MC3 for all simple types` with `MC3 on the evaluation-generated core for all simple types, with extension beyond evaluation modules deferred to DK-4/5`; at `quantum_group_reps.tex:181-183` replace `extends this to the full categorical equivalence` with `extends this to the evaluation-generated-core DK comparison`; at `quantum_group_reps.tex:201-202` replace `at the level of compact objects` with `on the evaluation-generated core`; at `quantum_group_reps.tex:581-583` replace `solved ... uniquely determines the chiral algebra` with `partially reconstructed on the evaluation-generated core; the full post-core extension is the downstream DK-4/5/completion packet`.

- [HIGH] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:81), [Vol I higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:10566), [Vol III modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:29), [Vol III modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:33) — PROBLEM: Vol III cites “Vol I Theorem MC3” for the strict dg-Lie/\(L_\infty\) comparison and “Vol I Theorem MC4” for MC-moduli coincidence. That is a wrong dependency map: MC3 is the categorical Clebsch-Gordan package, MC4 is completion towers, while the strict-model statement lives in `thm:modular-homotopy-convolution`. FIX: at line 29 replace the parenthetical with `Vol~I, Theorem~\ref*{V1-thm:modular-homotopy-convolution}`; at line 33 replace the first two sentences with `The strict dg Lie / L_\infty comparison, and the coincidence of Maurer--Cartan moduli for the strict model and the homotopy-invariant deformation object, are the content of Vol~I Theorem~\ref*{V1-thm:modular-homotopy-convolution}. The one-slot warning is the separate RNW19 bifunctoriality obstruction recorded in Vol~I's three-pillar constraint.`

- [HIGH] [Vol I holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holomorphic_topological.tex:1046), [Vol II holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1088), [Vol I FRONTIER.md](/Users/raeez/chiral-bar-cobar/FRONTIER.md:198), [Vol I working_notes_frontier_2026_04.tex](/Users/raeez/chiral-bar-cobar/working_notes_frontier_2026_04.tex:324), [Vol I N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:257), [Vol I N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:733) — PROBLEM: these summary surfaces drop the evaluation-core qualifier and advertise bare “MC3 for all simple types” / `MC3 (all simple types)`. That is exactly the scope drift the concordance forbids. FIX: in both `holomorphic_topological.tex` files replace `MC3 (all simple types)` with `MC3 (evaluation-generated core, all simple types; post-core DK-4/5 downstream)`; in `FRONTIER.md` rename the entry to `MC3 on the evaluation-generated core for all simple types`; in `working_notes_frontier_2026_04.tex:324` replace the parenthetical with `proved on the evaluation-generated core for all simple types`; in both `N2_mc3_all_types.tex` headings replace `MC3 for all simple types` with `MC3 on the evaluation-generated core for all simple types`.

- [HIGH] [Vol I concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4713), [Vol II examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:97), [Vol III quantum_group_reps.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:264), [Vol III drinfeld_center.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:432) — PROBLEM: Vol III uses `MC3` as the label for the Yangian/ordered-bar residue lane. The canonical DK ladder does not do that: Yangian-from-\(r(z)\) is DK-0/DK-1 material; MC3 is the later categorical Clebsch-Gordan stage. FIX: in `quantum_group_reps.tex:264-266` replace `This is the content of Volume~II, MC3` with `This is the DK-0/DK-1 ordered-bar/Yangian lane of Volume~II; MC3 enters later at the categorical Clebsch--Gordan stage on the evaluation-generated core`; in `drinfeld_center.tex:432` replace `Volume~II, MC3` with `Volume~II, DK-0/DK-1 ordered-bar/Yangian lane`.

## Summary
Checked: 26 | Findings: 5 | Verdict: FAIL
tokens used
168,039
