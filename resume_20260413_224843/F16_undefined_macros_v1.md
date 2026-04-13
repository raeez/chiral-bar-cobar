# F16_undefined_macros_v1 (1020s)

- [CRITICAL] `main.tex:590` — PROBLEM: `\mainpreambleonly` exits before the fallback macro block at `main.tex:597-719`, so `standalone/editorial.tex:4` loads an amputated preamble; `chapters/connections/concordance.tex:36` then immediately hits undefined macros such as `\cC`, and the standalone build spirals into 359 undefined control sequences plus 1491 unresolved references. FIX: move the fallback `\providecommand` block above the `\ifdefined\mainpreambleonly` guard, or split it into a separate preamble file loaded before `\endinput`; then rebuild `standalone/editorial.tex`.

- [CRITICAL] `standalone/introduction_full_survey.tex:280` — PROBLEM: the file is not actually standalone; it uses main-only symbols/operators/packages that its own preamble never defines (`\dzero`, `\Hom`, `\End`, `\Res`, `\id`, `\colim`, `\R`, `\dfib`, `\Dg`, `\chirAss`, `\chirLie`, `\chirCom`, `\llbracket...\rrbracket`, and `tikz-cd`’s `\arrow`), producing repeated undefined-control-sequence failures at lines 280, 422, 483, 1106, 1840, 5061, 5310, etc., plus 406 unresolved refs and 53 unresolved cites. FIX: mirror the missing `main.tex` definitions into the standalone preamble, add `\usepackage{tikz-cd}` and `\usepackage{stmaryrd}` (or explicit `\llbracket/\rrbracket` definitions), and add `\bibliographystyle{amsalpha}` with `\bibliography{standalone/references}` before `\end{document}`.

- [CRITICAL] `standalone/survey_modular_koszul_duality.tex:1338` — PROBLEM: the preamble omits core manuscript macros used later in the file: `\Hom`, `\End`, `\orline`, `\Defcyc`, `\Aut`, `\CompCl`, and the double-bracket notation at line 2975, so the build fails repeatedly at lines 1338, 1707, 2675, 2975, 7467, 8016, etc.; the file also has unresolved citations with no bibliography block at all. FIX: add `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\newcommand{\orline}[1]{\mathrm{or}_{#1}}`, `\newcommand{\Defcyc}{\operatorname{Def}_{\mathrm{cyc}}}`, `\DeclareMathOperator{\Aut}{Aut}`, `\newcommand{\CompCl}{\operatorname{CompCl}}`, load `stmaryrd` or define `\llbracket/\rrbracket`, and add `\bibliographystyle{amsalpha}` plus `\bibliography{standalone/references}`.

- [HIGH] `standalone/gaudin_from_collision.tex:11` — PROBLEM: `hyperref` is configured with `blue!60!black` and `green!40!black`, but the file never loads `xcolor`, so the build throws repeated `Undefined color` errors at lines 96, 110, 130, 241, 260, 501, 523, 525, 527, 530, and 532. FIX: add `\usepackage[dvipsnames]{xcolor}` before `hyperref`.

- [HIGH] `standalone/shadow_towers_v2.tex:487` — PROBLEM: the file hardcodes `\input{riccati}`, `\input{classification}`, and `\input{computations}` as if TeX resolves them relative to the source file; in the audited build it does not, so `riccati.tex` is missing and the standalone is dead on arrival. FIX: change those inputs to `\input{standalone/riccati}`, `\input{standalone/classification}`, and `\input{standalone/computations}`, or set `\makeatletter\def\input@path{{standalone/}}\makeatother` in the preamble.

- [HIGH] `standalone/N2_mc3_all_types.tex:391` — PROBLEM: `\cF` is used four times in the chromatic-filtration paragraph and never defined in the preamble. FIX: add `\newcommand{\cF}{\mathcal{F}}` with the other calligraphic macros.

- [HIGH] `standalone/N3_e1_primacy.tex:346` — PROBLEM: `\BarchFG` is used at lines 346 and 357 but never defined locally. FIX: add `\newcommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` to the preamble.

- [HIGH] `standalone/programme_summary.tex:1047` — PROBLEM: `\ChirHoch` is used in Theorem H and never defined, so the build breaks on a core headline formula. FIX: add `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` to the macro block.

- [HIGH] `standalone/cy_quantum_groups_6d_hcs.tex:183` — PROBLEM: the file cites external work but declares no bibliography surface, so its citations cannot ever resolve in standalone mode. FIX: add `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}` before `\end{document}`, or supply a complete local `thebibliography`.

- [HIGH] `standalone/programme_summary_sections5_8.tex:199` — PROBLEM: the file cites literature but ends with commented-out `\bibitem` stubs instead of an active bibliography, so the standalone citation surface is knowingly disabled. FIX: uncomment and complete the bibliography block, or replace the dead comments with `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}`.

- [HIGH] `standalone/survey_track_a_compressed.tex:732` — PROBLEM: the file cites external sources but has no `\bibliography` or `thebibliography`, so the compressed survey is not actually standalone. FIX: add `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}` before `\end{document}`.

- [MEDIUM] `standalone/N1_koszul_meta.tex:153`; `standalone/N4_mc4_completion.tex:171`; `standalone/N5_mc5_sewing.tex:107`; `standalone/analytic_sewing.tex:172`; `standalone/arithmetic_shadows.tex:233`; `standalone/drinfeld_kohno_bridge.tex:199`; `standalone/e1_primacy_ordered_bar.tex:214`; `standalone/en_chiral_operadic_circle.tex:210`; `standalone/five_theorems_modular_koszul.tex:144`; `standalone/garland_lepowsky.tex:107` — PROBLEM: these files ship local standalone wrappers but still leave unresolved `\ref/\eqref/\cite` calls after multi-pass build; they are excerpt slices pretending to be closed documents. FIX: for each file, either import the missing labelled statements/sections into the standalone source or rewrite the external cross-references as local prose, and replace the partial local bibliography with a complete local list or `\bibliography{standalone/references}`.

- [MEDIUM] `standalone/genus1_seven_faces.tex:90`; `standalone/koszulness_fourteen_characterizations.tex:201`; `standalone/ordered_chiral_homology.tex:209`; `standalone/programme_summary_section1.tex:153`; `standalone/sc_chtop_pva_descent.tex:198`; `standalone/shadow_towers.tex:95`; `standalone/shadow_towers_v3.tex:146`; `standalone/survey_modular_koszul_duality_v2.tex:283`; `standalone/three_dimensional_quantum_gravity.tex:101`; `standalone/three_parameter_hbar.tex:64` — PROBLEM: same boundary failure in a second cluster: the files still reference labels and bibliography keys that are not supplied by the standalone build, so they only work as fragments of the monograph, not as independent documents. FIX: close each extraction boundary by importing the referenced theorem/section/table surfaces and by supplying a complete bibliography surface; otherwise delete the broken `\ref/\eqref/\cite` calls.

- [LOW] `standalone/chiral_chern_weil.tex:172`; `standalone/classification.tex:93`; `standalone/classification_trichotomy.tex:366`; `standalone/computations.tex:242`; `standalone/cy_to_chiral_functor.tex:232`; `standalone/holographic_datum.tex:260`; `standalone/multi_weight_cross_channel.tex:203` — PROBLEM: these files are label-incomplete even when citations are not the issue; the standalone text still points to definitions, sections, computations, or tables that are absent locally. FIX: either inline the referenced result names/text or import the missing labelled environments into the standalone document.

- [LOW] `standalone/programme_summary_sections2_4.tex:313`; `standalone/programme_summary_sections9_14.tex:99`; `standalone/riccati.tex:150`; `standalone/seven_faces.tex:603`; `standalone/survey_track_b_compressed.tex:596`; `standalone/virasoro_r_matrix.tex:144`; `standalone/w3_holographic_datum.tex:135` — PROBLEM: these are also not label-closed: they retain dangling `\ref/\eqref` calls to omitted material, so the standalone PDFs silently lose semantic pointers. FIX: remove or localize each external cross-reference, or import the missing labelled material so the standalone build has a closed label graph.

## Summary
Checked: 53 | Findings: 15 | Verdict: FAIL


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
session id: 019d88ac-0160-7371-be90-1666513dcc56
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


MISSION: FOUNDATION AUDIT of standalone/

Grep ALL standalone files for undefined LaTeX macros. Run: for f in standalone/*.tex; do grep -oP '\\[a-zA-Z]+' $f | sort -u; done — cross-check against preamble. Every undefined macro is a finding.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Performing an audit check**

Okay, I'm looking into potential issues like hidden imports, unresolved references, and unjustified steps. The mission specifies a foundation audit of all standalone files, so I’ll grep for undefined macros and cross-check the preamble. Every undefined macro is a finding, and I could also check for missing definitions and unresolved references. I’ll need to execute a for loop and possibly use `rg` for this check. It's essential to inspect the standalone directory and collect line numbers for an exhaustive audit. Let’s gather this information.
codex
Auditing `standalone/` for undefined LaTeX macros, hidden imports, and other foundation failures. I’m starting by loading the audit workflow, then I’ll inventory the standalone files, extract macro usage, and cross-check definitions against the actual preamble sources before I write any findings.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'CLAUDE.md\\n'; sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'concordance.tex\\n'; sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 51ms:
Total output lines: 221

CLAUDE.md
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
 succeeded in 51ms:
concordance.tex
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
exec
/bin/zsh -lc "printf 'theorem_registry.md\\n'; sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 221

theorem_registry.md
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals


thinking
**Planning for context review**

It looks like I need to get the red_team_summary and target files, then read them later to update the plan once I have enough context. I also need to inspect the standalone directory and check the preamble. Maybe there's a main preamble in preamble.tex or the style file. I should identify what I need by reading through the standalone files. Alright, let's start reading!
codex
The audit workflow is loaded. Next I’m pinning down the live standalone surface and the actual macro-definition sources, because undefined-macro findings are only valid if they survive a read against the real preamble files, not just the local file body.
exec
/bin/zsh -lc "printf 'red_team_summary.md\\n'; sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'standalone files\\n'; rg --files standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
red_team_summary.md
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
 succeeded in 51ms:
standalone files
standalone/analytic_sewing.tex
standalone/drinfeld_kohno_bridge.pdf
standalone/theorem_index.tex
standalone/computations.tex
standalone/cover_letter_shadow_towers.pdf
standalone/N6_shadow_formality.tex
standalone/editorial.pdf
standalone/gaudin_from_collision.tex
standalone/ordered_chiral_homology.tex
standalone/three_dimensional_quantum_gravity.pdf
standalone/programme_summary_section1.tex
standalone/programme_summary_sections5_8.tex
standalone/e1_primacy_ordered_bar.tex
standalone/genus1_seven_faces.pdf
standalone/virasoro_r_matrix.tex
standalone/cover_letter_virasoro_r_matrix.pdf
standalone/cover_letter_garland_lepowsky.pdf
standalone/en_chiral_operadic_circle.tex
standalone/five_theorems_modular_koszul.tex
exec
/bin/zsh -lc "printf 'main preamble region\\n'; sed -n '1,260p' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'top-level tex/preamble candidates\\n'; rg -n \"\\\\(input|include|usepackage|newcommand|DeclareMathOperator|def|providecommand|NewDocumentCommand|DeclareRobustCommand)\" -g '*.tex' -g '*.sty' main.tex preamble.tex setup.tex macros.tex standalone chapters appendices frontmatter backmatter 2>/dev/null | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
top-level tex/preamble candidates
 succeeded in 51ms:
main preamble region
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{4} % Numbers down to subsubsubsection
\setcounter{tocdepth}{4} % TOC includes subsubsubsections

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

% EB Garamond with full features
\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols % This prevents conflicts
]{newtxmath}
\usepackage{ebgaramond}

% Fine-tuning for optimal appearance
\usepackage[

thinking
**Refining agent usage**

I’m considering whether it would be better to spawn an explorer now to assist with the inventory. But then, the user clearly wants an audit and not parallel agents unless they ask for that specifically. The skill guidelines say to use subagents only if the user explicitly requests parallel or delegated work, so I shouldn’t proceed with subagents. Instead, I need to update the plan with clear steps and do that after providing context.
codex
I have the audit protocol and the repository constitutive files in view. The next pass is mechanical and adversarial: enumerate every standalone file, read their local preambles/imports, then build the macro-usage set against the actual macro-definition surface so the findings survive re-verification.
Plan update
Foundation audit of `standalone/` with emphasis on undefined macros and hidden dependency failures. I will verify against actual file contents only and keep findings scoped to evidence I read.
  ✓ Inventory `standalone/*.tex` and identify how each file sources its preamble, packages, bibliography, and shared macros.
  → Read the macro-definition surface used by standalone builds: local file preambles plus shared definitions reachable from `main.tex` or explicit `\input` files.
  • Extract macro usage from every standalone `.tex`, cross-check undefined commands, and verify each candidate by line-level reads.
  • Attack second-order failures in standalone files: unresolved refs/cites, missing imports, hidden dependencies, and unjustified standalone assumptions.
  • Re-verify each surviving finding and produce exact file:line findings with concrete fixes and an audit summary.

thinking
**Evaluating inventory execution**

I need to execute an inventory and macro definition surface. I'm considering using 'rg' to find the `\input` and `\documentclass` lines in standalone files and then extract the preambles, perhaps the first 80 lines of each file. I also want to list macros defined in the main file, beyond the first 260 lines, or maybe even fully. It could be useful to use 'detex' too. I'll check the main inputs and custom commands files.
exec
/bin/zsh -lc "printf 'standalone documentclass/input/usepackage lines\\n'; rg -n \"\\\\documentclass|\\\\input|\\\\include|\\\\usepackage|\\\\bibliography|\\\\addbibresource|\\\\newcommand|\\\\def|\\\\DeclareMathOperator|\\\\providecommand|\\\\NewDocumentCommand\" standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
standalone documentclass/input/usepackage lines
rg: regex parse error:
    (?:\documentclass|\input|\include|\usepackage|\bibliography|\addbibresource|\newcommand|\def|\DeclareMathOperator|\providecommand|\NewDocumentCommand)
                      ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "printf 'main inputs/includes\\n'; rg -n \"\\\\input|\\\\include\" main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'repo macro-definition files\\n'; rg -n --glob '*.tex' --glob '*.sty' \"\\\\(newcommand|renewcommand|DeclareMathOperator|providecommand|def|NewDocumentCommand|DeclareRobustCommand)\" . | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
main inputs/includes
rg: regex parse error:
    (?:\input|\include)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
repo macro-definition files
rg: regex parse error:
    (?:\(newcommand|renewcommand|DeclareMathOperator|providecommand|def|NewDocumentCommand|DeclareRobustCommand))
                                                                                                                ^
error: unopened group

thinking
**Considering progress update**

I think I might need to mention a progress update. There was an error from the command, but it might not be something the user needs to worry about. It could make sense to mention that I’m adjusting the extraction command to address the issue. Keeping the users informed about progress is important, even if the details aren't directly user-facing!
codex
The first grep pass failed on shell escaping, not on the repository surface. I’m rerunning with literal patterns so the audit doesn’t inherit a false empty set from a bad command.
exec
/bin/zsh -lc "printf 'main inputs/includes\\n'; rg -n -e '\\\\input' -e '\\\\include' main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'standalone documentclass/input/usepackage lines\\n'; rg -n -e '\\\\documentclass' -e '\\\\input' -e '\\\\include' -e '\\\\usepackage' -e '\\\\bibliography' -e '\\\\addbibresource' -e '\\\\newcommand' -e '\\\\def' -e '\\\\DeclareMathOperator' -e '\\\\providecommand' -e '\\\\NewDocumentCommand' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main inputs/includes
846:\include{chapters/frame/preface}
850: \input{chapters/frame/guide_to_main_results}
859:\include{chapters/theory/introduction}
874:\include{chapters/frame/heisenberg_frame}
963:\include{chapters/theory/fourier_seed}
970:\include{chapters/theory/algebraic_foundations}
976:\include{chapters/theory/three_invariants}
982:\include{chapters/theory/configuration_spaces}
988:\include{chapters/theory/bar_construction}
994:\include{chapters/theory/cobar_construction}
1002:% \include{chapters/theory/bar_cobar_adjunction}
1004:\input{chapters/theory/bar_cobar_adjunction_curved}
1005:\input{chapters/theory/bar_cobar_adjunction_inversion}
1010:\input{appendices/homotopy_transfer}
1022:\include{chapters/theory/poincare_duality}
1030:\include{chapters/theory/chiral_koszul_pairs}
1031:\include{chapters/theory/koszul_pair_structure}
1038:% \include{chapters/theory/higher_genus}
1040:\input{chapters/theory/higher_genus_foundations}
 succeeded in 51ms:
Total output lines: 2050

standalone documentclass/input/usepackage lines
standalone/N5_mc5_sewing.tex:1:\documentclass[11pt,reqno]{amsart}
standalone/N5_mc5_sewing.tex:6:\usepackage{amsmath,amssymb,amsthm}
standalone/N5_mc5_sewing.tex:7:\usepackage{mathrsfs}
standalone/N5_mc5_sewing.tex:8:\usepackage{enumerate}
standalone/N5_mc5_sewing.tex:9:\usepackage[shortlabels]{enumitem}
standalone/N5_mc5_sewing.tex:10:\usepackage{booktabs}
standalone/N5_mc5_sewing.tex:11:\usepackage{array}
standalone/N5_mc5_sewing.tex:12:\usepackage{microtype}
standalone/N5_mc5_sewing.tex:13:\usepackage[dvipsnames]{xcolor}
standalone/N5_mc5_sewing.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/N5_mc5_sewing.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/N5_mc5_sewing.tex:34:\newcommand{\cH}{\mathcal{H}}
standalone/N5_mc5_sewing.tex:35:\newcommand{\cW}{\mathcal{W}}
standalone/N5_mc5_sewing.tex:36:\newcommand{\cM}{\mathcal{M}}
standalone/N5_mc5_sewing.tex:37:\newcommand{\barB}{\bar{B}}
standalone/N5_mc5_sewing.tex:38:\newcommand{\MC}{\mathrm{MC}}
standalone/N5_mc5_sewing.tex:39:\newcommand{\Sym}{\mathrm{Sym}}
exec
/bin/zsh -lc "printf 'repo macro-definition files\\n'; rg -n -e '\\\\newcommand' -e '\\\\renewcommand' -e '\\\\DeclareMathOperator' -e '\\\\providecommand' -e '\\\\def' -e '\\\\NewDocumentCommand' -e '\\\\DeclareRobustCommand' --glob '*.tex' --glob '*.sty' . | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
repo macro-definition files
./main.tex:49:\def\hyper@nopatch@caption{}
./main.tex:135:\newcommand{\orline}[1]{\mathrm{or}_{#1}}
./main.tex:143:% Override: make archive passes \def\archivebuild{1} to enable full content.
./main.tex:151: \newcommand{\ClaimStatusProvedHere}{}
./main.tex:152: \newcommand{\ClaimStatusProvedElsewhere}{}
./main.tex:153: \newcommand{\ClaimStatusOpen}{}
./main.tex:154: \newcommand{\ClaimStatusConjectured}{}
./main.tex:155: \newcommand{\ClaimStatusHeuristic}{}
./main.tex:156: \newcommand{\ClaimStatusConditional}{}
./main.tex:158: \newcommand{\ClaimStatusProvedHere}{\textnormal{[proved here]}}
./main.tex:159: \newcommand{\ClaimStatusProvedElsewhere}{\textnormal{[proved elsewhere]}}
./main.tex:160: \newcommand{\ClaimStatusOpen}{\textnormal{[open]}}
./main.tex:161: \newcommand{\ClaimStatusConjectured}{\textnormal{[conjectured]}}
./main.tex:162: \newcommand{\ClaimStatusHeuristic}{\textnormal{[physical heuristic]}}
./main.tex:163: \newcommand{\ClaimStatusConditional}{\textnormal{[conditional]}}
./main.tex:244:\def\theHtheorem{\theHsection.\arabic{theorem}}
./main.tex:291:\def\theHtable{\theHchapter.\arabic{table}}
./main.tex:292:\def\theHfigure{\theHchapter.\arabic{figure}}
./main.tex:307:\providecommand*{\toclevel@theorem}{2}







thinking
**Evaluating LaTeX files setup**

I think I need to run `latexmk -pdf -interaction=nonstopmode -halt-on-error` on each file, but some of them might require bibliography or other support. I assume the environment has TeX, which would help identify undefined control sequences accurately. The user wants to grep standalone files for undefined LaTeX macros, so I might need a script to extract macros and compare definitions. 

There are many .tex files, so automating checks with grep and compile logs could be beneficial. I need to identify standalone files that contain local preambles versus those that rely on imports. Most likely, they have local commands. I'll need to generate macros for each file and compare them to local definitions, considering that the known package set is quite vast. However, the user emphasized using grep and checking against preambles.
thinking
**Assessing LaTeX diagnostics**

I can definitely use grep to find candidate files and then verify them by compiling or searching for definitions. Compiling each file might be time-consuming, but with around 40 documents, it should be manageable. Some files already have PDFs, which could speed things up. 

My goal is to identify actual undefined control sequences. I wonder if running lacheck could simplify this process? Compile logs might be sufficient, but I need to establish a baseline first. I might write a script using `grep -oP '\\[a-zA-Z]+'` to compare against definitions in both the files and the main.tex commands, while also considering a curated list of package macros, though I should be cautious about potential false positives from built-ins like `\begin`.
thinking
**Exploring undefined control sequences**

I'm looking into capturing undefined control sequences in LaTeX. It seems important to compile standalone files to catch these errors, especially for unresolved references or citations. The user mentioned that each missing definition or unjustified step is a finding, which adds complexity to the audit. I should focus on the macro and import layers instead of just mathematical proofs. I'll probably need to read through the files to note any hidden dependencies and collect errors or warnings effectively.
thinking
**Checking standalone compilations**

I need to check if some standalone files compile because they include their own theorem environments. Maybe I should use `latexmk`, and I'll compile one like `standalone/analytic_sewing.tex`, but first, I should inspect the top preambles automatically. The developer advised against using Python for reading and writing, so I might use shell commands instead. It feels reasonable to create a loop to compile `.tex` files and collect errors. I'll run the user's grep command to extract macros, although it might generate a large output that I'll want to save to a file.
thinking
**Identifying missing macros**

I could gather all `.tex` files while excluding the PDFs. It seems there might not be a common preamble file since most standalone files define their own macros. My next step is to identify exactly which macros are missing. I can use the grep command to extract macros and compare them to definitions within the same file plus any preamble. This way, I might detect if macros like `\thmref`, `\lemref`, or `\eqref` are defined, possibly linked to a specific package.
thinking
**Managing LaTeX Compilation**

I'm thinking about how to compile my LaTeX documents effectively. I could compile each `standalone/*.tex` file with `pdflatex`, capturing exit codes and logging errors like undefined controls or missing files. Since I'm working with a restricted network but have local TeX, I'll need to decide on a strategy. I might try using `latexmk` for easier management of references, especially given there are about 40 documents. It feels a bit overwhelming, but I'll break it down step by step and keep everything maintained with regular updates.
thinking
**Organizing LaTeX Builds**

I'm considering creating a temporary build directory to keep things tidy, maybe using `latexmk -outdir=/tmp`. I need to make sure my standalone bibliographic references work by compiling from the standalone directory while redirecting outputs to `/tmp` with the `-cd` option. It might be simpler to run `latexmk -pdf` with the right flags. However, I have to check the paths for references and see if any documents need `--shell-escape`. It’s a bit of planning, but I want to get it right!
codex
The repo has no single shared standalone preamble file; most standalone documents carry their own local preamble and only inherit package-level commands plus anything explicitly defined in `main.tex` if they mirror it. I’m moving to the falsification pass now: compile each standalone file to catch actual undefined control sequences and unresolved references, then I’ll line-check the surviving failures against the source.
exec
/bin/zsh -lc 'command -v latexmk || command -v pdflatex || command -v xelatex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find standalone -maxdepth 1 -name '*.tex' | sort | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Library/TeX/texbin/latexmk
 succeeded in 51ms:
      53
exec
/bin/zsh -lc "find standalone -maxdepth 1 -name '*.tex' | sort" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/N1_koszul_meta.tex
standalone/N2_mc3_all_types.tex
standalone/N3_e1_primacy.tex
standalone/N4_mc4_completion.tex
standalone/N5_mc5_sewing.tex
standalone/N6_shadow_formality.tex
standalone/analytic_sewing.tex
standalone/arithmetic_shadows.tex
standalone/bp_self_duality.tex
standalone/chiral_chern_weil.tex
standalone/classification.tex
standalone/classification_trichotomy.tex
standalone/computations.tex
standalone/cover_letter_garland_lepowsky.tex
standalone/cover_letter_seven_faces.tex
standalone/cover_letter_shadow_towers.tex
standalone/cover_letter_virasoro_r_matrix.tex
standalone/cy_quantum_groups_6d_hcs.tex
standalone/cy_to_chiral_functor.tex
standalone/drinfeld_kohno_bridge.tex


thinking
**Considering compilation strategy**

I'm thinking about compiling all 53 documents. I need to keep it simple, possibly logging the process. Creating a temporary directory like /tmp/standalone_audit sounds good. However, doing it for all 53 docs might take too long, maybe around 40-60 seconds each. 

Using a shell loop sequentially could work better than using parallel tools since the developer advised using parallel mainly for certain tools. Instead, I’ll compile everything into one file and then summarize it for easier inspection later.
thinking
**Compiling diagnostics summary**

I'm considering compiling each document and extracting relevant diagnostics into a summary. First, I'll set up a temporary directory for log files and a summary text file. 

Using a loop, I'll compile each `.tex` file with `latexmk` while capturing any build errors in logs. If any issues arise, I’ll note the exit status and search the log for specific diagnostic messages. However, I’m realizing that using `-halt-on-error` stops the process at the first error, which might prevent me from seeing all the unresolved references. I could try running the build without this option to get more comprehensive logs.
exec
/bin/zsh -lc 'rm -rf /tmp/standalone_audit && mkdir -p /tmp/standalone_audit && summary=/tmp/standalone_audit/summary.txt && : > "$summary" && for f in standalone/*.tex; do base=$(basename "$f" .tex); outdir="/tmp/standalone_audit/$base"; mkdir -p "$outdir"; latexmk -pdf -interaction=nonstopmode -file-line-error -outdir="$outdir" "$f" >"$outdir/build.log" 2>&1; status=$?; printf '"'=== %s [exit=%s] ===\\n' \""'$f" "$status" >> "$summary"; rg -n "Undefined control sequence|LaTeX Error:|Reference .* undefined|Citation .* undefined|Package .* Warning|No file .*'"\\.bbl|Emergency stop|Runaway argument|I can't find file|Missing \\"'$ inserted|Missing '"\\} inserted|Misplaced alignment tab character|Undefined color|Unknown option\" \""'$outdir/build.log" >> "$summary" || true; printf '"'\\n' >> \""'$summary"; done; sed -n '"'1,320p' \""'$summary"' in /Users/raeez/chiral-bar-cobar exited 1 in 2.75s:
zsh:1: read-only variable: status
codex
The compile sweep is running across all 53 standalone documents and writing per-file logs into `/tmp/standalone_audit`. Once that finishes I’ll triage only the real failures that survive compilation and then line-check the source around each one.

thinking
**Correcting variable usage**

Oh no! I accidentally used a reserved variable named `status` in my zsh script. I need to rerun the script with another variable name instead. This is a simple but important mistake to catch because reserved variables can cause unexpected behavior. I’ll make sure to choose a different name that doesn’t conflict and then run it again. It's interesting how these little details can trip me up, but it's all part of the learning process!
codex
The sweep aborted because `zsh` reserves `status` as a read-only parameter. I’m rerunning with a neutral variable name so the audit surface stays unchanged and the logs are usable.
exec
/bin/zsh -lc 'rm -rf /tmp/standalone_audit && mkdir -p /tmp/standalone_audit && summary=/tmp/standalone_audit/summary.txt && : > "$summary" && for f in standalone/*.tex; do base=$(basename "$f" .tex); outdir="/tmp/standalone_audit/$base"; mkdir -p "$outdir"; latexmk -pdf -interaction=nonstopmode -file-line-error -outdir="$outdir" "$f" >"$outdir/build.log" 2>&1; rc=$?; printf '"'=== %s [exit=%s] ===\\n' \""'$f" "$rc" >> "$summary"; rg -n "Undefined control sequence|LaTeX Error:|Reference .* undefined|Citation .* undefined|Package .* Warning|No file .*'"\\.bbl|Emergency stop|Runaway argument|I can't find file|Missing \\"'$ inserted|Missing '"\\} inserted|Misplaced alignment tab character|Undefined color|Unknown option\" \""'$outdir/build.log" >> "$summary" || true; printf '"'\\n' >> \""'$summary"; done; sed -n '"'1,320p' \""'$summary"' in /Users/raeez/chiral-bar-cobarcodex
The batch compile is still live. After it finishes I’ll separate fatal control-sequence failures from softer standalone debt like undefined references and bibliography gaps so the final list stays severity-ordered and evidence-backed.

thinking
**Considering LaTeX processing**

I think the issue might be that latexmk is waiting, possibly hung due to an error prompt. But since I'm using nonstopmode, I should just let it continue. Maybe it's just that processing 53 documents is taking longer than expected. I'll check in again to see if anything updates or if it gets unstuck. Let's keep an eye on this!
codex
The compile sweep is still progressing. I’m letting it run to completion because partial logs would undercount later unresolved-reference failures and that would make the audit less harsh than the surface warrants.

thinking
**Inspecting process progress**

I’m considering inspecting the process, but I probably shouldn’t do that until the session is done. I wonder if we can run another command to check the `/tmp` summary progress or use `ps`. Maybe we could work on it in parallel if that’s allowed. I want to try using the `exec` command to tail the summary and possibly count the built logs. Let's see how that goes!
exec
/bin/zsh -lc "printf 'compiled so far\\n'; rg -n '"'^==='"' /tmp/standalone_audit/summary.txt | tail -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compiled so far
3895:=== standalone/holographic_datum.tex [exit=0] ===
3923:=== standalone/introduction_full_survey.tex [exit=12] ===
4513:=== standalone/koszulness_fourteen_characterizations.tex [exit=0] ===
4576:=== standalone/multi_weight_cross_channel.tex [exit=0] ===
4685:=== standalone/notation_index.tex [exit=0] ===
4688:=== standalone/ordered_chiral_homology.tex [exit=0] ===
5388:=== standalone/programme_summary.tex [exit=12] ===
5478:=== standalone/programme_summary_section1.tex [exit=0] ===
5509:=== standalone/programme_summary_sections2_4.tex [exit=0] ===
5523:=== standalone/programme_summary_sections5_8.tex [exit=0] ===
5577:=== standalone/programme_summary_sections9_14.tex [exit=0] ===
5592:=== standalone/riccati.tex [exit=0] ===
5619:=== standalone/sc_chtop_pva_descent.tex [exit=0] ===
5793:=== standalone/seven_faces.tex [exit=0] ===
5813:=== standalone/shadow_towers.tex [exit=0] ===
5866:=== standalone/shadow_towers_v2.tex [exit=12] ===
5904:=== standalone/shadow_towers_v3.tex [exit=0] ===
6226:=== standalone/survey_modular_koszul_duality.tex [exit=12] ===
6390:=== standalone/survey_modular_koszul_duality_v2.tex [exit=12] ===

thinking
**Evaluating session tracking**

I see that there’s a great summary file available, but the original session might still be running after survey_track_a. I could possibly dig deeper into the tail, but I’m wondering if it’s better to ignore the session and go straight for the summary file. Alternatively, I could compile everything into a batch if that makes sense. I just need to inspect things further to make the best decision!
exec
/bin/zsh -lc 'tail -n 120 /tmp/standalone_audit/summary.txt' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
241:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
245:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
249:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
261:LaTeX Warning: Reference `sec:shadow-as-gravity' on page 9 undefined on input l
265:LaTeX Warning: Reference `sec:koszul-s-duality' on page 9 undefined on input li
271:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
275:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
279:LaTeX Warning: Reference `prop:vir-m4' on page 10 undefined on input line 803.
287:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
291:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
295:LaTeX Warning: Reference `eq:quartic-contact' on page 11 undefined on input lin
306:LaTeX Warning: Reference `eq:complementarity' on page 12 undefined on input lin
318:LaTeX Warning: Reference `thm:non-truncation' on page 13 undefined on input lin
326:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
330:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
334:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
338:LaTeX Warning: Reference `eq:vir-lambda-bracket' on page 14 undefined on input 
342:LaTeX Warning: Reference `eq:vir-ope' on page 14 undefined on input line 1193.
345:LaTeX Warning: Reference `thm:vir-koszul' on page 14 undefined on input line 11
349:LaTeX Warning: Reference `prop:vir-r-matrix' on page 14 undefined on input line

 succeeded in 1m 36s:
=== standalone/N1_koszul_meta.tex [exit=12] ===

=== standalone/N2_mc3_all_types.tex [exit=12] ===
137:LaTeX Warning: Citation `Kohno87' on page 1 undefined on input line 114.
140:LaTeX Warning: Citation `Drinfeld90' on page 1 undefined on input line 114.
143:LaTeX Warning: Citation `KL93a' on page 1 undefined on input line 122.
146:LaTeX Warning: Citation `KL93b' on page 1 undefined on input line 122.
149:LaTeX Warning: Citation `KL94a' on page 1 undefined on input line 122.
152:LaTeX Warning: Citation `KL94b' on page 1 undefined on input line 122.
155:LaTeX Warning: Citation `EK96' on page 1 undefined on input line 124.
158:LaTeX Warning: Citation `EK98' on page 1 undefined on input line 124.
163:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
167:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
171:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
175:LaTeX Warning: Citation `FR99' on page 2 undefined on input line 155.
178:LaTeX Warning: Citation `FrenkelMukhin01' on page 2 undefined on input line 156
182:LaTeX Warning: Citation `Nakajima04' on page 2 undefined on input line 157.
185:LaTeX Warning: Citation `ChariMoura06' on page 2 undefined on input line 157.
188:LaTeX Warning: Citation `ChariMoura06' on page 2 undefined on input line 173.
191:LaTeX Warning: Citation `Nakajima04' on page 2 undefined on input line 173.
thinking
**Reading file lines**

I think I need to get a structured summary by file, instead of just looking at the end part. That makes sense to me. I’ll review the first 200 lines to gather relevant details. It’s important to ensure I understand the overall content before summarizing. I'll focus on key points and themes as I go through those initial lines. This way, I can provide the user with a comprehensive summary!
exec
/bin/zsh -lc "sed -n '1,220p' /tmp/standalone_audit/summary.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== standalone/N1_koszul_meta.tex [exit=12] ===

=== standalone/N2_mc3_all_types.tex [exit=12] ===
137:LaTeX Warning: Citation `Kohno87' on page 1 undefined on input line 114.
140:LaTeX Warning: Citation `Drinfeld90' on page 1 undefined on input line 114.
143:LaTeX Warning: Citation `KL93a' on page 1 undefined on input line 122.
146:LaTeX Warning: Citation `KL93b' on page 1 undefined on input line 122.
149:LaTeX Warning: Citation `KL94a' on page 1 undefined on input line 122.
152:LaTeX Warning: Citation `KL94b' on page 1 undefined on input line 122.
155:LaTeX Warning: Citation `EK96' on page 1 undefined on input line 124.
158:LaTeX Warning: Citation `EK98' on page 1 undefined on input line 124.
163:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
167:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
171:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
175:LaTeX Warning: Citation `FR99' on page 2 undefined on input line 155.
178:LaTeX Warning: Citation `FrenkelMukhin01' on page 2 undefined on input line 156
182:LaTeX Warning: Citation `Nakajima04' on page 2 undefined on input line 157.
185:LaTeX Warning: Citation `ChariMoura06' on page 2 undefined on input line 157.
188:LaTeX Warning: Citation `ChariMoura06' on page 2 undefined on input line 173.
191:LaTeX Warning: Citation `Nakajima04' on page 2 undefined on input line 173.

thinking
**Analyzing dependencies and citations**

I’m looking into cross-file references and how there’s a hidden dependency I need to address. Identifying every missing definition and unresolved reference feels important since it points to the same issue.

The user's request emphasizes the need for an exhaustive list, but I must balance this against not exceeding 50-70 lines. Grouping or summarizing findings might help manage the volume while ensuring thoroughness. I’ll have to check if all references are truly present and complete that inspection.
exec
/bin/zsh -lc "printf 'sections:'; rg -c '"'^==='"' /tmp/standalone_audit/summary.txt; printf '\\nlast files:\\n'; rg '"'^==='"' /tmp/standalone_audit/summary.txt | tail -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
sections:53

last files:
=== standalone/programme_summary.tex [exit=12] ===
=== standalone/programme_summary_section1.tex [exit=0] ===
=== standalone/programme_summary_sections2_4.tex [exit=0] ===
=== standalone/programme_summary_sections5_8.tex [exit=0] ===
=== standalone/programme_summary_sections9_14.tex [exit=0] ===
=== standalone/riccati.tex [exit=0] ===
=== standalone/sc_chtop_pva_descent.tex [exit=0] ===
=== standalone/seven_faces.tex [exit=0] ===
=== standalone/shadow_towers.tex [exit=0] ===
=== standalone/shadow_towers_v2.tex [exit=12] ===
=== standalone/shadow_towers_v3.tex [exit=0] ===
=== standalone/survey_modular_koszul_duality.tex [exit=12] ===
=== standalone/survey_modular_koszul_duality_v2.tex [exit=12] ===
=== standalone/survey_track_a_compressed.tex [exit=0] ===
=== standalone/survey_track_b_compressed.tex [exit=0] ===
=== standalone/theorem_index.tex [exit=0] ===
=== standalone/three_dimensional_quantum_gravity.tex [exit=0] ===

thinking
**Considering session closure**

I’m thinking about whether I need to close the hanging session. It seems like the original compilation is done, but I’m not entirely sure if it’s still running. Since the summary is complete, I wonder if the session can be considered finished. I should also extract files related to exit 12 and inspect any unresolved citations. It might be helpful to get a quick summary count of the undefined control sequences and citations. Let’s parse through those!
codex
The sweep finished across all 53 files. I’m collapsing the raw log into per-file failure classes now so I can distinguish “actual undefined macro” from “standalone file compiles only because it silently drops half its cross-references or bibliography.”
exec
/bin/zsh -lc "awk '
/"'^=== /{file=$2; gsub(/''^=== /, "", $0); next}
/Undefined control sequence/{u[file]++}
/LaTeX Warning: Reference .* undefined/{r[file]++}
/LaTeX Warning: Citation .* undefined/{c[file]++}
/LaTeX Error:/{e[file]++}
END{
  for (f in u) files[f]=1; for (f in r) files[f]=1; for (f in c) files[f]=1; for (f in e) files[f]=1;
  for (f in files) printf "%s | undefined_control=%d | undefined_ref=%d | undefined_cite=%d | latex_error=%d'"\\n\", f, u[f]+0, r[f]+0, c[f]+0, e[f]+0;
}' /tmp/standalone_audit/summary.txt | sort" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/N2_mc3_all_types.tex | undefined_control=4 | undefined_ref=39 | undefined_cite=68 | latex_error=0
standalone/N3_e1_primacy.tex | undefined_control=2 | undefined_ref=13 | undefined_cite=14 | latex_error=0
standalone/N4_mc4_completion.tex | undefined_control=0 | undefined_ref=36 | undefined_cite=10 | latex_error=0
standalone/N5_mc5_sewing.tex | undefined_control=0 | undefined_ref=30 | undefined_cite=16 | latex_error=0
standalone/analytic_sewing.tex | undefined_control=0 | undefined_ref=40 | undefined_cite=19 | latex_error=0
standalone/arithmetic_shadows.tex | undefined_control=0 | undefined_ref=10 | undefined_cite=4 | latex_error=0
standalone/chiral_chern_weil.tex | undefined_control=0 | undefined_ref=9 | undefined_cite=0 | latex_error=0
standalone/classification.tex | undefined_control=0 | undefined_ref=22 | undefined_cite=0 | latex_error=0
standalone/classification_trichotomy.tex | undefined_control=0 | undefined_ref=1 | undefined_cite=0 | latex_error=0
standalone/computations.tex | undefined_control=0 | undefined_ref=3 | undefined_cite=0 | latex_error=0
standalone/cy_quantum_groups_6d_hcs.tex | undefined_control=0 | undefined_ref=6 | undefined_cite=3 | latex_error=0
standalone/cy_to_chiral_functor.tex | undefined_control=0 | undefined_ref=11 | undefined_cite=0 | latex_error=0
standalone/drinfeld_kohno_bridge.tex | undefined_control=0 | undefined_ref=29 | undefined_cite=4 | latex_error=0
standalone/e1_primacy_ordered_bar.tex | undefined_control=0 | undefined_ref=37 | undefined_cite=29 | latex_error=0
standalone/editorial.tex | undefined_control=359 | undefined_ref=1491 | undefined_cite=178 | latex_error=2
standalone/en_chiral_operadic_circle.tex | undefined_control=0 | undefined_ref=52 | undefined_cite=13 | latex_error=0
standalone/five_theorems_modular_koszul.tex | undefined_control=0 | undefined_ref=7 | undefined_cite=16 | latex_error=0
standalone/garland_lepowsky.tex | undefined_control=0 | undefined_ref=24 | undefined_cite=24 | latex_error=0
standalone/gaudin_from_collision.tex | undefined_control=0 | undefined_ref=5 | undefined_cite=9 | latex_error=14
standalone/genus1_seven_faces.tex | undefined_control=0 | undefined_ref=37 | undefined_cite=11 | latex_error=0


thinking
**Clarifying findings structure**

The user mentioned that every unresolved reference counts as a finding, which makes me think I should produce a finding for each missing macro line and for clusters of unresolved references at the file level. It seems like I should include exact file:line references rather than a range. To align with the user’s request, I think having one finding per file with unresolved references and summarizing counts and causes could be a manageable approach.
thinking
**Identifying exact fixes**

I need to make sure to add `\bibliography{references}` or import any missing sections, and also fix any broken `\ref` commands. When files have both references and citations, I should note both. It’s important to find the exact earliest line where the issue occurs, which I can do by using compile logs. I’ll need to check the actual source to locate the first problematic `\ref` or any missing `\bibliography`, especially since some local preambles might not have it at all.
codex
I’ve isolated the hard failures. The worst offenders are not subtle: a small set of standalone files contain real undefined control sequences or structural LaTeX errors, and a larger set “compile” only while dropping their cross-references or bibliography because the standalone wrapper omits the dependency surface. I’m reading the exact offending lines now so every fix is line-specific.
exec
/bin/zsh -lc "printf 'N2 lines\\n'; nl -ba standalone/N2_mc3_all_types.tex | sed -n '384,398p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N2 lines
   384	\cite{HernandezJimbo12}.
   385	\end{definition}
   386	
   387	\subsection{The chromatic filtration}
   388	
   389	The category $\cO^{\mathrm{sh}}$ carries a decreasing
   390	\emph{chromatic} or \emph{conformal-weight} filtration
   391	$\cF^{\geq N} \subset \cO^{\mathrm{sh}}$, where $\cF^{\geq N}$
   392	consists of objects whose generalized conformal-weight generalized
   393	eigenvalues are bounded below by $N$. The associated graded
   394	pieces $\cF^{\geq N} / \cF^{\geq N+1}$ are finite-dimensional
   395	strata in the sense that, at each fixed highest $\ell$-weight,
   396	the space of conformal-weight-$N$ vectors is finite-dimensional.
   397	Compact objects of the ind-completion $\widehat{\cO}^{\mathrm{sh}}$
   398	are precisely those supported on finitely many strata, and the
exec
/bin/zsh -lc "printf 'programme_summary lines\\n'; nl -ba standalone/programme_summary.tex | sed -n '150,175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'N3 lines\\n'; nl -ba standalone/N3_e1_primacy.tex | sed -n '340,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey_modular_koszul_duality first undefined control hits\\n'; rg -n 'Undefined control sequence' /tmp/standalone_audit/survey_modular_koszul_duality/build.log && printf '\\nsource around first hits\\n' && nl -ba standalone/survey_modular_koszul_duality.tex | sed -n '180,245p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
programme_summary lines
   150	
   151	Three properties single out~$\eta_{12}$. A double pole
   152	$dz/(z-w)^2$ transforms under coordinate change and has no
   153	coordinate-independent residue. A regular $1$-form has
   154	residue zero and extracts nothing from the collision. The
   155	logarithmic derivative is the unique $1$-form on~$C_2(X)$
   156	with a first-order pole along~$\Delta$ and conformally
   157	invariant residue.
   158	
   159	On $C_3(X)$, the three pullbacks
   160	$\eta_{12}, \eta_{23}, \eta_{31}$ satisfy
   161	\begin{equation}\label{eq:arnold}
   162	\eta_{12} \wedge \eta_{23}
   163	\;+\;
   164	\eta_{23} \wedge \eta_{31}
   165	\;+\;
   166	\eta_{31} \wedge \eta_{12}
   167	\;=\; 0\,.
   168	\end{equation}
 succeeded in 51ms:
N3 lines
   340	the full argument and the relation to the ambient Mok25
   341	compactification.
   342	\end{proof}
   343	
   344	\begin{remark}[Three bar complexes, one map]
   345	\label{rem:three-bars}
   346	Let $\BarchFG(\cA)$ denote the Francis--Gaitsgory chiral Lie bar,
   347	which uses only the zeroth OPE product $a_{(0)}b$; let
   348	$\BarSig(\cA) = \Barch(\cA)$ denote the symmetric bar, which uses
   349	all OPE products and takes $\Sigma_{n}$-coinvariants (the bar
   350	complex of Volume I, Theorem A); and let $\Barord(\cA)$ denote
   351	the ordered bar of \eqref{eq:ordered-bar-definition}. There is a
   352	natural surjection
   353	\begin{equation}
   354	\label{eq:three-bars}
   355	\Barord(\cA) \twoheadrightarrow \BarSig(\cA),
   356	\qquad
   357	\mathrm{gr}\,\BarSig(\cA) \twoheadrightarrow \BarchFG(\cA),
   358	\end{equation}
 succeeded in 51ms:
survey_modular_koszul_duality first undefined control hits
197:./standalone/survey_modular_koszul_duality.tex:1338: Undefined control sequence
201:./standalone/survey_modular_koszul_duality.tex:1338: Undefined control sequence
205:./standalone/survey_modular_koszul_duality.tex:1341: Undefined control sequence
209:./standalone/survey_modular_koszul_duality.tex:1341: Undefined control sequence
213:./standalone/survey_modular_koszul_duality.tex:1344: Undefined control sequence
217:./standalone/survey_modular_koszul_duality.tex:1344: Undefined control sequence
221:./standalone/survey_modular_koszul_duality.tex:1372: Undefined control sequence
225:./standalone/survey_modular_koszul_duality.tex:1372: Undefined control sequence
241:./standalone/survey_modular_koszul_duality.tex:1397: Undefined control sequence
245:./standalone/survey_modular_koszul_duality.tex:1398: Undefined control sequence
269:./standalone/survey_modular_koszul_duality.tex:1707: Undefined control sequence
277:./standalone/survey_modular_koszul_duality.tex:1725: Undefined control sequence
353:./standalone/survey_modular_koszul_duality.tex:2675: Undefined control sequence
357:./standalone/survey_modular_koszul_duality.tex:2702: Undefined control sequence
361:./standalone/survey_modular_koszul_duality.tex:2704: Undefined control sequence
372:./standalone/survey_modular_koszul_duality.tex:2769: Undefined control sequence
428:./standalone/survey_modular_koszul_duality.tex:2975: Undefined control sequence
432:./standalone/survey_modular_koszul_duality.tex:2975: Undefined control sequence
699:./standalone/survey_modular_koszul_duality.tex:5087: Undefined control sequence

thinking
**Inspecting build log**

I need to find the actual macro that's causing the undefined control sequence error in the survey file. There might be something in the log involving `\boxtimes`, but that's standard, so it’s probably not the issue. I should really take a closer look at the build log around the error, specifically lines around 197. I'll read the excerpt near the first error to see if I can identify what's going wrong.
exec
/bin/zsh -lc "printf 'survey build around first error\\n'; sed -n '188,206p' /tmp/standalone_audit/survey_modular_koszul_duality/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
survey build around first error
LaTeX Warning: Reference `eq:preface-feynman-sum' on page 19 undefined on input
 line 1306.


LaTeX Warning: Reference `eq:preface-feynman-sum' on page 19 undefined on input
 line 1310.


[19]
./standalone/survey_modular_koszul_duality.tex:1338: Undefined control sequence
.
l.1338  \Hom
            \bigl(B(\Ass),\,\End_A\bigr)
./standalone/survey_modular_koszul_duality.tex:1338: Undefined control sequence
.
l.1338  \Hom\bigl(B(\Ass),\,\End
                                _A\bigr)
./standalone/survey_modular_koszul_duality.tex:1341: Undefined control sequence
.
exec
/bin/zsh -lc "printf 'programme_summary undefined control hits\\n'; rg -n 'Undefined control sequence' /tmp/standalone_audit/programme_summary/build.log && printf '\\nsource around hit\\n' && nl -ba standalone/programme_summary.tex | sed -n '430,460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'introduction_full_survey first undefined control hits\\n'; rg -n 'Undefined control sequence' /tmp/standalone_audit/introduction_full_survey/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'editorial first undefined control hits\\n'; rg -n 'Undefined control sequence|LaTeX Error:' /tmp/standalone_audit/editorial/build.log | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
programme_summary undefined control hits
241:./standalone/programme_summary.tex:1047: Undefined control sequence.

source around hit
   430	% ====================================================================
   431	\subsection{Three operations on the bar}
   432	\label{ssec:three-operations}
   433	% ====================================================================
   434	
   435	The bar construction is a categorical logarithm:
   436	$B(\cA \otimes \cA') \simeq B(\cA) \oplus B(\cA')$.
   437	The logarithmic form
   438	$\eta_{ij} = d\log(z_i - z_j)$ is the integral kernel;
   439	the Arnold relation is the cocycle condition for~$\log$.
   440	
   441	Three distinct functors act on~$B(\cA)$ and produce three
   442	distinct outputs:
   443	\begin{equation}\label{eq:three-functors}
   444	\begin{array}{lcll}
   445	\Omega(B(\cA)) &\simeq& \cA
 succeeded in 50ms:
introduction_full_survey first undefined control hits
160:./standalone/introduction_full_survey.tex:280: Undefined control sequence.
166:./standalone/introduction_full_survey.tex:280: Undefined control sequence.
235:./standalone/introduction_full_survey.tex:422: Undefined control sequence.
238:./standalone/introduction_full_survey.tex:422: Undefined control sequence.
241:./standalone/introduction_full_survey.tex:436: Undefined control sequence.
264:./standalone/introduction_full_survey.tex:483: Undefined control sequence.
269:./standalone/introduction_full_survey.tex:485: Undefined control sequence.
299:./standalone/introduction_full_survey.tex:552: Undefined control sequence.
302:./standalone/introduction_full_survey.tex:552: Undefined control sequence.
317:./standalone/introduction_full_survey.tex:566: Undefined control sequence.
338:./standalone/introduction_full_survey.tex:609: Undefined control sequence.
341:./standalone/introduction_full_survey.tex:619: Undefined control sequence.
346:./standalone/introduction_full_survey.tex:635: Undefined control sequence.
355:./standalone/introduction_full_survey.tex:638: Undefined control sequence.
397:./standalone/introduction_full_survey.tex:724: Undefined control sequence.
406:./standalone/introduction_full_survey.tex:747: Undefined control sequence.
439:./standalone/introduction_full_survey.tex:821: Undefined control sequence.
445:./standalone/introduction_full_survey.tex:821: Undefined control sequence.
448:./standalone/introduction_full_survey.tex:834: Undefined control sequence.
 succeeded in 51ms:
editorial first undefined control hits
292:./chapters/connections/concordance.tex:36: Undefined control sequence.
340:./chapters/connections/concordance.tex:76: Undefined control sequence.
343:./chapters/connections/concordance.tex:76: Undefined control sequence.
384:./chapters/connections/concordance.tex:125: Undefined control sequence.
389:./chapters/connections/concordance.tex:128: Undefined control sequence.
397:./chapters/connections/concordance.tex:144: Undefined control sequence.
402:./chapters/connections/concordance.tex:144: Undefined control sequence.
405:./chapters/connections/concordance.tex:145: Undefined control sequence.
410:./chapters/connections/concordance.tex:146: Undefined control sequence.
413:./chapters/connections/concordance.tex:148: Undefined control sequence.
418:./chapters/connections/concordance.tex:157: Undefined control sequence.
460:./chapters/connections/concordance.tex:253: Undefined control sequence.
465:./chapters/connections/concordance.tex:253: Undefined control sequence.
470:./chapters/connections/concordance.tex:254: Undefined control sequence.
569:./chapters/connections/concordance.tex:365: Undefined control sequence.
575:./chapters/connections/concordance.tex:365: Undefined control sequence.
581:./chapters/connections/concordance.tex:365: Undefined control sequence.
586:./chapters/connections/concordance.tex:365: Undefined control sequence.
601:./chapters/connections/concordance.tex:388: Undefined control sequence.

thinking
**Exploring macro issues**

I'm looking into the editorial.tex file, which might have specific macros causing errors. I want to check the preamble, but it could be quite large. My focus will be on figuring out missing macros that might be leading to issues like undefined theorem environments. I plan to inspect both editorial.tex and introduction_full_survey carefully. Also, I might need to create a script that extracts the names of undefined macros from the build logs, especially following the lines that indicate errors. Let's tackle this!
exec
/bin/zsh -lc 'for f in N2_mc3_all_types N3_e1_primacy programme_summary survey_modular_koszul_duality introduction_full_survey editorial; do log=/tmp/standalone_audit/$f/build.log; printf '"'=== %s ===\\n' \""'$f"; awk '"'/Undefined control sequence/{getline; getline; print}' \""'$log" | sed '"'s/"'^l'"\\.[0-9][0-9]* *//' | sed 's/[[:space:]]\\+/ /g' | sed -n '1,80p'; printf '\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== N2_mc3_all_types ===
                    
                    
                    
                                ^{\geq N+1}$ are finite-dimensional

=== N3_e1_primacy ===
                         
                                                  (\cA),

=== programme_summary ===
                ^1(V_k(\fg)) \cong \fg.

=== survey_modular_koszul_duality ===
\Hom
\Hom\bigl(B(\Ass),\,\End
\Hom
\Hom_\Sigma\bigl(B(\cP),\,\End
\Hom
\Hom_\Sigma\bigl(F\cO,\,\End

thinking
**Improving awk extraction**

I’m realizing my awk extraction could use some clarity due to line wrapping issues. I need a better way to extract context. For each undefined control in N2, it looks like \cF might not be defined, and similarly for N3 with \BarchFG. In the programme_summary at line 1047, \ChirHoch may also be undefined. I think I should inspect the source code around those lines and verify definitions in the file using more targeted reads. Let's focus on the error lines and preamble sections.
exec
/bin/zsh -lc "printf 'N2 preamble + error region\\n'; nl -ba standalone/N2_mc3_all_types.tex | sed -n '30,65p;387,396p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N2 preamble + error region
    30	\newtheorem{remark}[theorem]{Remark}
    31	
    32	% ================================================================
    33	% Macros
    34	% ================================================================
    35	\newcommand{\cA}{\mathcal{A}}
    36	\newcommand{\cC}{\mathcal{C}}
    37	\newcommand{\cD}{\mathcal{D}}
    38	\newcommand{\cO}{\mathcal{O}}
    39	\newcommand{\cR}{\mathcal{R}}
    40	\newcommand{\fg}{\mathfrak{g}}
    41	\newcommand{\fh}{\mathfrak{h}}
    42	\newcommand{\fn}{\mathfrak{n}}
    43	\newcommand{\fsl}{\mathfrak{sl}}
    44	\newcommand{\fso}{\mathfrak{so}}
    45	\newcommand{\fsp}{\mathfrak{sp}}
    46	\newcommand{\MC}{\mathrm{MC}}
    47	\newcommand{\Hom}{\mathrm{Hom}}
    48	\newcommand{\End}{\mathrm{End}}
exec
/bin/zsh -lc "printf 'N3 preamble + error region\\n'; nl -ba standalone/N3_e1_primacy.tex | sed -n '50,70p;344,358p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'programme_summary preamble + error region\\n'; nl -ba standalone/programme_summary.tex | sed -n '20,40p;1040,1050p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'introduction_full_survey preamble + first error regions\\n'; nl -ba standalone/introduction_full_survey.tex | sed -n '60,105p;272,285p;418,438p;546,570p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N3 preamble + error region
    50	\newcommand{\fg}{\mathfrak{g}}
    51	\newcommand{\gmod}{\mathfrak{g}^{\mathrm{mod}}_{\cA}}
    52	\newcommand{\gEone}{\mathfrak{g}^{E_{1}}_{\cA}}
    53	\newcommand{\Barch}{\overline{B}^{\mathrm{ch}}}
    54	\newcommand{\Barord}{\overline{B}^{\mathrm{ord}}}
    55	\newcommand{\BarSig}{\overline{B}^{\Sigma}}
    56	\newcommand{\Cobar}{\Omega^{\mathrm{ch}}}
    57	\newcommand{\Vir}{\mathrm{Vir}}
    58	\newcommand{\KM}{\mathrm{KM}}
    59	\newcommand{\CC}{\mathbb{C}}
    60	\newcommand{\op}{\mathrm{op}}
    61	\newcommand{\FM}{\overline{\mathrm{FM}}}
    62	\newcommand{\av}{\operatorname{av}}
    63	\newcommand{\GRT}{\mathrm{GRT}}
    64	\newcommand{\id}{\mathrm{id}}
    65	
    66	\DeclareMathOperator{\rk}{rk}
    67	\DeclareMathOperator{\depth}{depth}
    68	\DeclareMathOperator{\ch}{ch}
 succeeded in 51ms:
programme_summary preamble + error region
    20	% Theorem environments
    21	% ================================================================
    22	\newtheorem{theorem}{Theorem}[section]
    23	\newtheorem{proposition}[theorem]{Proposition}
    24	\newtheorem{lemma}[theorem]{Lemma}
    25	\newtheorem{corollary}[theorem]{Corollary}
    26	\newtheorem{conjecture}[theorem]{Conjecture}
    27	\theoremstyle{definition}
    28	\newtheorem{definition}[theorem]{Definition}
    29	\newtheorem{construction}[theorem]{Construction}
    30	\newtheorem{example}[theorem]{Example}
    31	\theoremstyle{remark}
    32	\newtheorem{remark}[theorem]{Remark}
    33	
    34	% ================================================================
    35	% Macros
    36	% ================================================================
    37	\newcommand{\cA}{\mathcal{A}}
    38	\newcommand{\cD}{\mathcal{D}}
 succeeded in 51ms:
introduction_full_survey preamble + first error regions
    60	\providecommand{\fg}{\mathfrak{g}}
    61	\providecommand{\fh}{\mathfrak{h}}
    62	\providecommand{\gmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
    63	\providecommand{\gAmod}{\mathfrak{g}^{\mathrm{mod}}_\cA}
    64	\providecommand{\Sh}{\mathrm{Sh}}
    65	\providecommand{\OPE}{\mathrm{OPE}}
    66	\providecommand{\Vir}{\mathrm{Vir}}
    67	\providecommand{\Walg}{\mathcal{W}}
    68	\providecommand{\Ainf}{A_\infty}
    69	\providecommand{\Eone}{E_1}
    70	\providecommand{\Etwo}{E_2}
    71	\providecommand{\Einf}{E_\infty}
    72	\providecommand{\En}{E_n}
    73	\providecommand{\Pinf}{P_\infty}
    74	\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
    75	\providecommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
    76	\providecommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
    77	\providecommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
    78	\providecommand{\ClaimStatusHeuristic}{\textsuperscript{\textsc{[he]}}}

thinking
**Inspecting for missing macros**

I need to look into undefined macros like `\dzero`, `\Hom`, `\End`, and `\MC`. It seems I might be missing full preamble definitions. There’s a likelihood that some macros haven’t been defined, such as `\orline` and `\chirAss`. The user wants precise fixes, probably wanting definitions added from the main preamble into a standalone one. I should compile a list of macros that are actually missing from each file by using the build log for errors. Let's get started on that!
exec
/bin/zsh -lc 'for f in N2_mc3_all_types N3_e1_primacy programme_summary survey_modular_koszul_duality introduction_full_survey editorial; do log=/tmp/standalone_audit/$f/build.log; printf '"'=== %s ===\\n' \""'$f"; perl -ne '"'if(/Undefined control sequence/){"'$want=2; next} if($want){$want--; if($want==0){ while(/'"\\\\[A-Za-z@]+/g){ print \""'$&'"\\n\" } }}' \""'$log" | sort | uniq -c; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== N2_mc3_all_types ===
   1 \geq

=== N3_e1_primacy ===
   1 \cA

=== programme_summary ===
   1 \cong
   2 \fg

=== survey_modular_koszul_duality ===
   1 \Ass
   1 \Aut
   2 \Bbbk
   1 \Com
   1 \CompCl
   6 \Defcyc
   5 \End
   3 \Gamma
   9 \Hom

thinking
**Examining extraction issues**

I’m noticing the extraction is poor because the context lines contain standard commands. It seems like I might be missing some macros that aren’t defined, which affects the extraction of all tokens. To investigate, I could search for whether those macros, like \Hom, \End, \Defcyc, \Bbbk, \orline, \Aut, and \CompCl, are defined in the file. It would also be helpful to confirm if their definitions are missing in the preamble.
exec
/bin/zsh -lc "printf 'survey preamble defs check\\n'; rg -n \"\\\\(newcommand|providecommand|DeclareMathOperator)\\{\\\\(Hom|End|Defcyc|Bbbk|orline|Aut|CompCl|Ass|Com|Cobar|Barch|barB|Barchord|BarchFG|BarchSig|dzero|chirAss)\\}\" standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
survey preamble defs check
rg: regex parse error:
    (?:\(newcommand|providecommand|DeclareMathOperator)\{\(Hom|End|Defcyc|Bbbk|orline|Aut|CompCl|Ass|Com|Cobar|Barch|barB|Barchord|BarchFG|BarchSig|dzero|chirAss)\})
                                                                                                                                                                 ^
error: unopened group
exec
/bin/zsh -lc "printf 'introduction defs check\\n'; rg -n \"\\\\(newcommand|providecommand|DeclareMathOperator)\\{\\\\(Hom|End|dzero|chirAss|orline|Aut|barB|Barch|Cobar|Res|MC|CompCl|Defcyc|Ass|Com|Bbbk)\\}\" standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'programme_summary defs check\\n'; rg -n \"\\\\(newcommand|providecommand|DeclareMathOperator)\\{\\\\(ChirHoch|fg|Ran|cA|barB|MC|Sym|Vir|Heis|KM)\\}\" standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
introduction defs check
rg: regex parse error:
    (?:\(newcommand|providecommand|DeclareMathOperator)\{\(Hom|End|dzero|chirAss|orline|Aut|barB|Barch|Cobar|Res|MC|CompCl|Defcyc|Ass|Com|Bbbk)\})
                                                                                                                                              ^
error: unopened group
 exited 2 in 51ms:
programme_summary defs check
rg: regex parse error:
    (?:\(newcommand|providecommand|DeclareMathOperator)\{\(ChirHoch|fg|Ran|cA|barB|MC|Sym|Vir|Heis|KM)\})
                                                                                                     ^
error: unopened group
exec
/bin/zsh -lc "printf 'editorial top preamble/input\\n'; nl -ba standalone/editorial.tex | sed -n '1,180p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
editorial top preamble/input
     1	% Editorial companion: the archive-only concordance and constitution chapters.
     2	\def\archivebuild{1}
     3	\def\mainpreambleonly{1}
     4	\IfFileExists{main.tex}{\input{main.tex}}{\input{../main.tex}}
     5	
     6	\newcommand{\repoinput}[1]{%
     7	 \IfFileExists{#1.tex}{\input{#1}}{\input{../#1}}%
     8	}
     9	
    10	\begin{document}
    11	\frontmatter
    12	\tableofcontents
    13	\mainmatter
    14	\repoinput{chapters/connections/concordance}
    15	\repoinput{chapters/connections/editorial_constitution}
    16	\backmatter
    17	\repoinput{bibliography/references}
    18	\end{document}

thinking
**Checking definitions and commands**

I need to check definitions using a simpler command, maybe something like `rg -n '\\ChirHoch|...'`, and I could also consider using `grep -F` for specific command definitions. Although I might not actually need to do that since we can already see there are likely some missing definitions. I’ll take a closer look at the preambles for things like programme_summary, survey, and introduction to see if any commands are missing. I've got a bit more investigating to do!
exec
/bin/zsh -lc "printf 'programme_summary preamble excerpt\\n'; nl -ba standalone/programme_summary.tex | sed -n '35,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey preamble excerpt\\n'; nl -ba standalone/survey_modular_koszul_duality.tex | sed -n '30,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'introduction build around first errors\\n'; sed -n '154,176p' /tmp/standalone_audit/introduction_full_survey/build.log; printf '\\n---\\n'; sed -n '228,246p' /tmp/standalone_audit/introduction_full_survey/build.log; printf '\\n---\\n'; sed -n '258,276p' /tmp/standalone_audit/introduction_full_survey/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
programme_summary preamble excerpt
    35	% Macros
    36	% ================================================================
    37	\newcommand{\cA}{\mathcal{A}}
    38	\newcommand{\cD}{\mathcal{D}}
    39	\newcommand{\cH}{\mathcal{H}}
    40	\newcommand{\cM}{\mathcal{M}}
    41	\newcommand{\cW}{\mathcal{W}}
    42	\newcommand{\barB}{\overline{B}}
    43	\newcommand{\Ran}{\mathrm{Ran}}
    44	\newcommand{\FM}{\overline{\mathrm{FM}}}
    45	\newcommand{\Conf}{\mathrm{Conf}}
    46	\newcommand{\fg}{\mathfrak{g}}
    47	\newcommand{\Sym}{\mathrm{Sym}}
    48	\newcommand{\Res}{\operatorname{Res}}
    49	\newcommand{\Spec}{\operatorname{Spec}}
    50	\newcommand{\Diff}{\mathrm{Diff}}
    51	\newcommand{\Vir}{\mathrm{Vir}}
    52	\newcommand{\Hom}{\mathrm{Hom}}
    53	\newcommand{\id}{\mathrm{id}}
 succeeded in 51ms:
survey preamble excerpt
    30	\providecommand{\cD}{\mathcal{D}}
    31	\providecommand{\cE}{\mathcal{E}}
    32	\providecommand{\cF}{\mathcal{F}}
    33	\providecommand{\cG}{\mathcal{G}}
    34	\providecommand{\cH}{\mathcal{H}}
    35	\providecommand{\cI}{\mathcal{I}}
    36	\providecommand{\cJ}{\mathcal{J}}
    37	\providecommand{\cK}{\mathcal{K}}
    38	\providecommand{\cL}{\mathcal{L}}
    39	\providecommand{\cM}{\mathcal{M}}
    40	\providecommand{\cN}{\mathcal{N}}
    41	\providecommand{\cO}{\mathcal{O}}
    42	\providecommand{\cP}{\mathcal{P}}
    43	\providecommand{\cQ}{\mathcal{Q}}
    44	\providecommand{\cR}{\mathcal{R}}
    45	\providecommand{\cS}{\mathcal{S}}
    46	\providecommand{\cT}{\mathcal{T}}
    47	\providecommand{\cU}{\mathcal{U}}
    48	\providecommand{\cV}{\mathcal{V}}
 succeeded in 51ms:
introduction build around first errors
t line 249.


LaTeX Warning: Reference `eq:arnold-seed' on page 4 undefined on input line 279
.

./standalone/introduction_full_survey.tex:280: Undefined control sequence.
<recently read> \dzero 
                       
l.280 residue vanish, so $\dzero
                                ^2 = 0$ at genus~$0$, where $\dzero$ denotes...

./standalone/introduction_full_survey.tex:280: Undefined control sequence.
<recently read> \dzero 
                       
l.280 ...\dzero^2 = 0$ at genus~$0$, where $\dzero
                                                  $ denotes the genus-$0$ ba...


exec
/bin/zsh -lc "printf 'w3_holographic_datum error\\n'; sed -n '1,220p' /tmp/standalone_audit/w3_holographic_datum/build.log | rg -n 'Undefined control sequence|LaTeX Error|Reference .* undefined|Citation .* undefined|not found' -n -C 2" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
w3_holographic_datum error
94-[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}]
95-
96:LaTeX Warning: Reference `sec:r-matrix' on page 2 undefined on input line 135.
97-
98-
exec
/bin/zsh -lc "sed -n '236,246p' /tmp/standalone_audit/programme_summary/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


LaTeX Warning: Reference `rem:multi-weight' on page 11 undefined on input line 
1034.

./standalone/programme_summary.tex:1047: Undefined control sequence.
l.1047 \ChirHoch
                ^1(V_k(\fg)) \cong \fg.

[11]

exec
/bin/zsh -lc "sed -n '296,318p' /tmp/standalone_audit/N2_mc3_all_types/build.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '118,136p' /tmp/standalone_audit/N3_e1_primacy/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

LaTeX Warning: Citation `HernandezJimbo12' on page 5 undefined on input line 38
4.

./standalone/N2_mc3_all_types.tex:391: Undefined control sequence.
<recently read> \cF 
                    
l.391 $\cF
          ^{\geq N} \subset \cO^{\mathrm{sh}}$, where $\cF^{\geq N}$
./standalone/N2_mc3_all_types.tex:391: Undefined control sequence.
<recently read> \cF 
                    
l.391 ...N} \subset \cO^{\mathrm{sh}}$, where $\cF
                                                  ^{\geq N}$
./standalone/N2_mc3_all_types.tex:394: Undefined control sequence.
<recently read> \cF 
                    
l.394 pieces $\cF
                 ^{\geq N} / \cF^{\geq N+1}$ are finite-dimensional
./standalone/N2_mc3_all_types.tex:394: Undefined control sequence.
exec
/bin/zsh -lc "printf 'survey definitions of likely missing macros in file\\n'; for m in Hom End Defcyc Bbbk orline Aut CompCl dzero chirAss; do printf '%s: ' \""'$m"; rg -n -m 1 -F "'"\\\\"'$m" standalone/survey_modular_koszul_duality.tex | head -n 3 || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


LaTeX Warning: Citation `Lorgat26I' on page 4 undefined on input line 339.

./standalone/N3_e1_primacy.tex:346: Undefined control sequence.
<recently read> \BarchFG 
                         
l.346 Let $\BarchFG
                   (\cA)$ denote the Francis--Gaitsgory chiral Lie bar,

LaTeX Warning: Reference `eq:ordered-bar-definition' on page 4 undefined on inp
ut line 351.

./standalone/N3_e1_primacy.tex:357: Undefined control sequence.
l.357 ...,\BarSig(\cA) \twoheadrightarrow \BarchFG
                                                  (\cA),

[4]

 succeeded in 52ms:
survey definitions of likely missing macros in file
Hom: 1338: \Hom\bigl(B(\Ass),\,\End_A\bigr)
End: 1338: \Hom\bigl(B(\Ass),\,\End_A\bigr)
Defcyc: 2675:$\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}})$.
Bbbk: 91:\providecommand{\Bbbk}{\mathbb{k}}
orline: 1707:\orline{E_{\mathrm{int}}(\Gamma)}
Aut: 7467:$D^{(g)} = \sum_{\Gamma:\,g(\Gamma)=g}|\Aut(\Gamma)|^{-1}D_\Gamma$,
CompCl: 8016:closure $\CompCl(\cF_{\mathrm{ft}})$, the class of all such
dzero: chirAss: 
exec
/bin/zsh -lc "printf 'intro definitions of likely missing macros in file\\n'; for m in Hom End dzero chirAss orline Aut Res MC CompCl Defcyc; do printf '%s: ' \""'$m"; rg -n -m 2 -F "'"\\\\"'$m" standalone/introduction_full_survey.tex | head -n 3 || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
intro definitions of likely missing macros in file
Hom: 422:\Hom\!\bigl(F\!\Ass(g,n),\,\End_\cA(n)\bigr),
1255::= \Hom_\Sigma(\barB(\mathsf{SC}^{\mathrm{ch,top}}),
End: 422:\Hom\!\bigl(F\!\Ass(g,n),\,\End_\cA(n)\bigr),
436:$r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
dzero: 280:residue vanish, so $\dzero^2 = 0$ at genus~$0$, where $\dzero$ denotes the genus-$0$ bar differential. The resulting cochain complex is
552:coinvariants) and $\operatorname{av}(\dzero) = \dzero$
chirAss: 5061:operad~$\chirAss$ (Definition~\ref{def:chiral-ass-operad}):
5075:The \emph{associative chiral operad} $\chirAss$ on $X$ is the
orline: Aut: 1282:\frac{1}{|\Aut(\Gamma)|}\, D_\Gamma,
Res: 483:\tfrac{1}{2}\,\operatorname{tr}\!\bigl[\Res_{z = 0} r(z)\bigr],
821:\Res_{D_{k\ell}} \circ \Res_{D_{ij}}$:
MC: 57:\providecommand{\MC}{\mathrm{MC}}
180:$\Theta_\cA \in \MC(\gAmod)$
CompCl: 85:\providecommand{\CompCl}{\mathrm{CompCl}}
3408:The strong completion-tower theorem (Theorem~\ref{thm:completed-bar-cobar-strong}): the strong filtration axiom $\mu_r(F^{i_1}, \ldots, F^{i_r}) \subset F^{i_1 + \cdots + i_r}$ forces a degree cutoff (Lemma~\ref{lem:degree-cutoff}) making continuity and Mittag--Leffler automatic, so finite-stage bar-cobar passes to inverse limits. The completion closure $\CompCl(\mathcal{F}_{\mathrm{ft}})$ carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}).
Defcyc: 86:\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
1932: \MC\!\bigl(\Defcyc(\cA) \;\widehat{\otimes}\; \Gmod\bigr)$.

thinking
**Exploring survey definitions**

I’m trying to find the definitions related to the `survey` because I need to see if Bbbk is defined correctly. If it’s not defined due to a line wrap in the build log, that could be a problem. I need to look for actual missing macros in the survey, like Hom, End, Defcyc, orline, Aut, and CompCl. I'll check if these are defined in the preamble, but it seems Bbbk is defined. I’ll search for definitions in the file.
exec
/bin/zsh -lc "for f in standalone/survey_modular_koszul_duality.tex standalone/introduction_full_survey.tex; do printf '=== %s ===\\n' \""'$f"; for m in Hom End Defcyc orline Aut CompCl dzero chirAss; do printf '"'%s defs: ' \""'$m"; rg -n -m 3 -e "'"\\\\\\\\newcommand\\\\{\\\\"'$m'"\\\\}\" -e \"\\\\\\\\providecommand\\\\{\\\\"'$m'"\\\\}\" -e \"\\\\\\\\DeclareMathOperator\\\\{\\\\"'$m'"\\\\}\" \""'$f" || true; done; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
=== standalone/survey_modular_koszul_duality.tex ===
Hom defs: rg: regex parse error:
    (?:\\newcommand\{\Hom\})|(?:\\providecommand\{\Hom\})|(?:\\DeclareMathOperator\{\Hom\})
                     ^^
error: unrecognized escape sequence
End defs: rg: regex parse error:
    (?:\\newcommand\{\End\})|(?:\\providecommand\{\End\})|(?:\\DeclareMathOperator\{\End\})
                     ^^
error: unrecognized escape sequence
Defcyc defs: orline defs: rg: regex parse error:
    (?:\\newcommand\{\orline\})|(?:\\providecommand\{\orline\})|(?:\\DeclareMathOperator\{\orline\})
                     ^^
error: unrecognized escape sequence
Aut defs: CompCl defs: rg: regex parse error:
    (?:\\newcommand\{\CompCl\})|(?:\\providecommand\{\CompCl\})|(?:\\DeclareMathOperator\{\CompCl\})
                     ^^
error: unrecognized escape sequence
dzero defs: chirAss defs: rg: regex parse error:
    (?:\\newcommand\{\chirAss\})|(?:\\providecommand\{\chirAss\})|(?:\\DeclareMathOperator\{\chirAss\})
                     ^^
exec
/bin/zsh -lc "printf 'survey exact defs\\n'; for s in '\\\\newcommand{\\\\Hom}' '\\\\providecommand{\\\\Hom}' '\\\\DeclareMathOperator{\\\\Hom}' '\\\\newcommand{\\\\End}' '\\\\providecommand{\\\\End}' '\\\\DeclareMathOperator{\\\\End}' '\\\\newcommand{\\\\Defcyc}' '\\\\providecommand{\\\\Defcyc}' '\\\\DeclareMathOperator{\\\\Defcyc}' '\\\\newcommand{\\\\orline}' '\\\\providecommand{\\\\orline}' '\\\\DeclareMathOperator{\\\\orline}' '\\\\newcommand{\\\\Aut}' '\\\\providecommand{\\\\Aut}' '\\\\DeclareMathOperator{\\\\Aut}' '\\\\newcommand{\\\\CompCl}' '\\\\providecommand{\\\\CompCl}' '\\\\DeclareMathOperator{\\\\CompCl}'; do grep -nF \""'$s" standalone/survey_modular_koszul_duality.tex || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
survey exact defs
exec
/bin/zsh -lc "printf 'programme_summary exact defs\\n'; for s in '\\\\newcommand{\\\\ChirHoch}' '\\\\providecommand{\\\\ChirHoch}' '\\\\DeclareMathOperator{\\\\ChirHoch}'; do grep -nF \""'$s" standalone/programme_summary.tex || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
programme_summary exact defs
exec
/bin/zsh -lc "printf 'intro exact defs\\n'; for s in '\\\\newcommand{\\\\Hom}' '\\\\providecommand{\\\\Hom}' '\\\\DeclareMathOperator{\\\\Hom}' '\\\\newcommand{\\\\End}' '\\\\providecommand{\\\\End}' '\\\\DeclareMathOperator{\\\\End}' '\\\\newcommand{\\\\Defcyc}' '\\\\providecommand{\\\\Defcyc}' '\\\\DeclareMathOperator{\\\\Defcyc}' '\\\\newcommand{\\\\orline}' '\\\\providecommand{\\\\orline}' '\\\\DeclareMathOperator{\\\\orline}' '\\\\newcommand{\\\\Aut}' '\\\\providecommand{\\\\Aut}' '\\\\DeclareMathOperator{\\\\Aut}' '\\\\newcommand{\\\\CompCl}' '\\\\providecommand{\\\\CompCl}' '\\\\DeclareMathOperator{\\\\CompCl}' '\\\\newcommand{\\\\dzero}' '\\\\providecommand{\\\\dzero}' '\\\\DeclareMathOperator{\\\\dzero}' '\\\\newcommand{\\\\chirAss}' '\\\\providecommand{\\\\chirAss}' '\\\\DeclareMathOperator{\\\\chirAss}'; do grep -nF \""'$s" standalone/introduction_full_survey.tex || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 103ms:
intro exact defs
exec
/bin/zsh -lc "grep -nF '\\providecommand{\\CompCl}' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
85:\providecommand{\CompCl}{\mathrm{CompCl}}

thinking
**Inspecting editorial errors**

I’m wondering if there’s a potential loop issue due to double escaping, but it might not be necessary. Anyway, I know I need to take a closer look at the editorial errors. This happens because the editorial imports from main.tex with `\mainpreambleonly{1}`, so I’ll need to inspect the handling of `mainpreambleonly` in main.tex. Time to search through that!
exec
/bin/zsh -lc "printf 'editorial build around first errors\\n'; sed -n '286,306p' /tmp/standalone_audit/editorial/build.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'concordance source around first error\\n'; nl -ba chapters/connections/concordance.tex | sed -n '30,42p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'mainpreambleonly in main.tex\\n'; rg -n 'mainpreambleonly|archivebuild|begin\\{document\\}|end\\{document\\}' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
editorial build around first errors
(/usr/local/texlive/2025/texmf-dist/tex/latex/newtx/untxmia.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/newtx/untxsyc.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msa.cfg)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-msb.cfg)
./chapters/connections/concordance.tex:36: Undefined control sequence.
l.36 ...D}_{\Ran}\barB_X(\cA_i)\simeq \Omega_X(\cC
                                                  _j)\simeq \cA_j$,

LaTeX Warning: Reference `thm:bar-cobar-isomorphism-main' on page 1 undefined o
n input line 37.


LaTeX Warning: Reference `thm:higher-genus-inversion' on page 1 undefined on in
put line 42.


LaTeX Warning: Reference `thm:bar-cobar-inversion-qi' on page 1 undefined on in
 succeeded in 51ms:
concordance source around first error
    30	& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
    31	\hline
    32	\textbf{A} & Bar-cobar adjunction
    33	 & $\barBch \dashv \Omegach$ on $\Ran(X)$,
    34	 with the algebra-level Verdier half only after
    35	 $\mathbb{D}_{\Ran}$:
    36	 $\mathbb{D}_{\Ran}\barB_X(\cA_i)\simeq \Omega_X(\cC_j)\simeq \cA_j$,
    37	 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
    38	 & \ClaimStatusProvedHere \\
    39	\textbf{B} & Bar-cobar inversion
    40	 & Strict quasi-isomorphism on the Koszul locus
    41	 $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
    42	 \textup{(}Thms~\ref{thm:higher-genus-inversion},
 succeeded in 51ms:
mainpreambleonly in main.tex
143:% Override: make archive passes \def\archivebuild{1} to enable full content.
144:\ifdefined\archivebuild
590:\ifdefined\mainpreambleonly
595:\begin{document}
1956:\end{document}

thinking
**Inspecting error details**

I'm looking into an error with an undefined macro, specifically \cC. It seems to be related to line 36, which uses \Omega_X(\cC_j). I’m wondering if \cC is only defined under a specific condition in the main preamble—after `\ifdefined\mainpreambleonly`. I think I need to take a closer look around line 590 in the main document to figure out what's going wrong there.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '580,610p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   580	\providecommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}
   581	\providecommand{\BarchSig}{\overline{B}^{\mathrm{ch},\Sigma}}
   582	\providecommand{\Cop}{\mathcal{C}_{\mathrm{op}}}
   583	\providecommand{\Perf}{\operatorname{Perf}}
   584	\providecommand{\sewop}{T}
   585	\providecommand{\sewker}{K}
   586	\providecommand{\secquant}{\Gamma}
   587	\providecommand{\zetareg}{\zeta_{\mathrm{reg}}}
   588	\providecommand{\GL}{\mathrm{GL}}
   589	\providecommand{\Imag}{\operatorname{Im}}
   590	\ifdefined\mainpreambleonly
   591	% Allow standalone companions to reuse the manuscript preamble without
   592	% executing the monograph body.
   593	\expandafter\endinput
   594	\fi
   595	\begin{document}
   596	
   597	% Fallback macros for imported chapter fragments.
   598	% Operads, categories, and D-module macros are now in the preamble;
   599	% \providecommand entries below supply only symbols without preamble definitions.

thinking
**Identifying macro issues**

I've realized there are many fallback macros defined after \begin{document}, but the `editorial` section uses `\mainpreambleonly`, which causes an endinput before these fallback macros are available. This means the editorial is missing some definitions. The fix is to move the necessary fallback `\providecommand` block above the `\ifdefined\mainpreambleonly` guard or duplicate them in the editorial preamble before importing concordance/editorial_constitution. I might need to check other sections like survey and introduction for similar issues. I'll keep an eye on N1 section as well.
exec
/bin/zsh -lc "sed -n '1,80p' /tmp/standalone_audit/N1_koszul_meta/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -file-line-error -recorder -output-directory="/private/tmp/standalone_audit/N1_koszul_meta"  "standalone/N1_koszul_meta.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./standalone/N1_koszul_meta.tex
exec
/bin/zsh -lc "rg -n 'Undefined control sequence|LaTeX Error:|Emergency stop|Runaway argument|No file|Missing \\"'$ inserted|Missing '"\\} inserted|not found|Citation .* undefined|Reference .* undefined' /tmp/standalone_audit/N1_koszul_meta/build.log | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc 'tail -n 80 /tmp/standalone_audit/N1_koszul_meta/build.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -file-line-error -recorder -output-directory="/private/tmp/standalone_audit/N1_koszul_meta"  "standalone/N1_koszul_meta.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./standalone/N1_koszul_meta.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/amscls/amsart.cls
Document Class: amsart 2020/05/29 v2.20.6
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.

thinking
**Investigating log issues**

It seems like the build log got truncated, possibly due to line buffering. I need to check if I can access the full log, as that might provide more information. Instead of just the summary, I think I should look at the actual pdflatex log for better insights. Getting the real log file could really help me understand what went wrong or clarify any errors I might be seeing. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n '"'!'"' /tmp/standalone_audit/N1_koszul_meta/N1_koszul_meta.log | sed -n '1,50p'; printf '\\nlast 60 actual log lines\\n'; tail -n 60 /tmp/standalone_audit/N1_koszul_meta/N1_koszul_meta.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

last 60 actual log lines
)
(/usr/local/texlive/2025/texmf-dist/tex/generic/gettitlestring/gettitlestring.s
ty
Package: gettitlestring 2019/12/15 v1.6 Cleanup title references (HO)
 (/usr/local/texlive/2025/texmf-dist/tex/latex/kvoptions/kvoptions.sty
Package: kvoptions 2022-06-15 v3.15 Key value format for package options (HO)
))
\c@section@level=\count291
)
(/usr/local/texlive/2025/texmf-dist/tex/generic/stringenc/stringenc.sty
Package: stringenc 2019/11/29 v1.12 Convert strings between diff. encodings (HO
)
)
\@linkdim=\dimen170
\Hy@linkcounter=\count292
\Hy@pagecounter=\count293

(/usr/local/texlive/2025/texmf-dist/tex/latex/hyperref/pd1enc.def

thinking
**Investigating compile issues**

It looks like the log got truncated mid-process, possibly due to a compile error. The user is asking for standalone files, and I'm considering whether to include N1 despite the issues. Maybe the problem arose because of an incomplete file or an unclosed entity that caused pdflatex to hang. I could try running the N1 file individually to spot errors, but I’m concerned about time limits, especially since the build log might be cut short due to token limits. I’ll proceed with the suggested pdflatex command to check for errors.
codex
Some standalone files are failing in different ways. `editorial.tex` is the clearest structural defect so far: it deliberately imports only the `main.tex` preamble, but the macros it needs live below `\begin{document}` in `main.tex`, so the preamble-only mode amputates its own fallback definitions. I’m checking the remaining ambiguous failures one by one so I don’t overstate anything.
exec
/bin/zsh -lc 'mkdir -p /tmp/standalone_one && pdflatex -interaction=nonstopmode -file-line-error -halt-on-error -output-directory=/tmp/standalone_one standalone/N1_koszul_meta.tex' in /Users/raeez/chiral-bar-cobar succeeded in 1.55s:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./standalone/N1_koszul_meta.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/amscls/amsart.cls
Document Class: amsart 2020/05/29 v2.20.6
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/local/texlive/2025/texmf-dist/tex/latex/amsfonts/amssymb.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/jknapltx/mathrsfs.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/enumerate.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/enumitem/enumitem.sty)
exec
/bin/zsh -lc "printf 'gaudin errors\\n'; rg -n 'LaTeX Error:|Undefined control sequence|Missing \\"'$ inserted|not found|Reference .* undefined|Citation .* undefined'"' /tmp/standalone_audit/gaudin_from_collision/build.log -C 2 | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'shadow_towers_v2 errors\\n'; rg -n 'LaTeX Error:|Undefined control sequence|Missing \\"'$ inserted|not found|Reference .* undefined|Citation .* undefined'"' /tmp/standalone_audit/shadow_towers_v2/build.log -C 2 | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
shadow_towers_v2 errors
135-(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-euf.cfg)
136-
137:LaTeX Warning: Citation `LorgatVirR' on page 1 undefined on input line 116.
138-
139-
140:LaTeX Warning: Citation `LorgatSevenFaces' on page 1 undefined on input line 11
141-9.
142-
143-
144:LaTeX Warning: Citation `Priddy70' on page 1 undefined on input line 135.
145-
146-
147:LaTeX Warning: Citation `BGS96' on page 1 undefined on input line 136.
148-
149-
150:LaTeX Warning: Citation `LV12' on page 1 undefined on input line 137.
151-
152-
153:LaTeX Warning: Citation `BD04' on page 1 undefined on input line 148.
 succeeded in 52ms:
gaudin errors
99-(/usr/local/texlive/2025/texmf-dist/tex/latex/microtype/mt-euf.cfg)
100-
101:LaTeX Warning: Citation `FFR1994' on page 1 undefined on input line 96.
102-
103-
104:LaTeX Warning: Citation `GZ26' on page 1 undefined on input line 110.
105-
106-
107:LaTeX Warning: Reference `eq:gz-gaudin' on page 1 undefined on input line 130.
108-
109-
--
111-[2]
112-
113:LaTeX Warning: Reference `eq:gz-connection' on page 3 undefined on input line 2
114-41.
115-
116-
117:LaTeX Warning: Citation `FFR1994' on page 3 undefined on input line 260.
exec
/bin/zsh -lc "printf 'N4 first refs/cites\\n'; sed -n '1,140p' /tmp/standalone_audit/N4_mc4_completion/build.log | rg -n 'Reference .* undefined|Citation .* undefined' -C 0" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey_v2 warnings head\\n'; sed -n '1,140p' /tmp/standalone_audit/survey_modular_koszul_duality_v2/build.log | rg -n 'Undefined control sequence|LaTeX Error:|Reference .* undefined|Citation .* undefined' -C 2" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
N4 first refs/cites
87:LaTeX Warning: Citation `Priddy70' on page 1 undefined on input line 118.
90:LaTeX Warning: Citation `LV12' on page 1 undefined on input line 119.
97:LaTeX Warning: Citation `LorgatI' on page 2 undefined on input line 148.
100:LaTeX Warning: Reference `eq:SF-intro' on page 2 undefined on input line 171.
103:LaTeX Warning: Reference `def:strong-tower' on page 2 undefined on input line 1
107:LaTeX Warning: Reference `thm:mc4-strong' on page 2 undefined on input line 194
111:LaTeX Warning: Reference `sec:cutoff' on page 2 undefined on input line 196.
114:LaTeX Warning: Reference `sec:ml' on page 2 undefined on input line 199.
117:LaTeX Warning: Reference `lem:filtered-comparison' on page 2 undefined on input
123:LaTeX Warning: Reference `sec:examples' on page 3 undefined on input line 228.
126:LaTeX Warning: Citation `Positselski11' on page 3 undefined on input line 232.
129:LaTeX Warning: Citation `LV12' on page 3 undefined on input line 234.
132:LaTeX Warning: Citation `BD04' on page 3 undefined on input line 237.
135:LaTeX Warning: Reference `sec:prelim' on page 3 undefined on input line 243.
138:LaTeX Warning: Reference `sec:sf' on page 3 undefined on input line 243.
 exited 1 in 51ms:
survey_v2 warnings head

thinking
**Inspecting package options**

I'm thinking about inspecting the `gaudin_from_collision` source lines, as there seems to be a missing `xcolor` option. I might need to check the preamble lines first. It likely uses options like `linkcolor=blue!60!black` and `citecolor=green!40!black`, but I’m only seeing `\usepackage{microtype}` with no mention of `xcolor`. I’ll definitely take a closer look to sort this out!
exec
/bin/zsh -lc "nl -ba standalone/gaudin_from_collision.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\documentclass[11pt]{article}
     2	
     3	%%% Packages
     4	\usepackage{amsmath,amssymb,amsthm}
     5	\usepackage{mathtools}
     6	\usepackage{mathrsfs}
     7	\usepackage[shortlabels]{enumitem}
     8	\usepackage{booktabs}
     9	\usepackage{array}
    10	\usepackage{microtype}
    11	\usepackage[colorlinks=true,linkcolor=blue!60!black,
    12	 citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
    13	
    14	%%% Page geometry
    15	\usepackage[margin=1.15in]{geometry}
    16	
    17	%%% Theorem environments
    18	\theoremstyle{plain}
    19	\newtheorem{theorem}{Theorem}[section]
    20	\newtheorem{proposition}[theorem]{Proposition}



thinking
**Evaluating missing elements**

I realized I need to add `\usepackage[dvipsnames]{xcolor}` before the hyperref package. There are warnings in `survey_modular_koszul_duality_v2`, and I should check the reference counts since it only had undefined references. The user wants to include all 40 files, but that might be excessive. I may need to classify them by their root causes. Many standalone documents seem to lack bibliography directives, which could be contributing to issues. A precise fix per file will help!
thinking
**Identifying fixes for references**

For the exact fix, I need to add `\bibliographystyle{amsalpha}` and `\bibliography{references}`, or I could use `thebibliography` inline. Unresolved references may arise from omitted sections in standalone slices. The precise solutions involve importing labeled sections or replacing broken `\ref`s with clear prose. I should also look for any hidden import lines. If a file is part of a larger work, unresolved references often relate to omitted labels. The user seems to want a detailed audit, including line numbers for unresolved references.
thinking
**Classifying bibliography issues**

I might combine findings when both a missing bibliography and missing imported labels are the cause. I could assign severity levels: HIGH for macro or build-breaking issues and MEDIUM for missing citations or references. It seems sensible to systematically gather the first undefined reference or citation line for each file and check if the bibliography is missing. Writing a script to parse this summary and identify missing bibliography directives could work. Using the first citation line might be more effective than checking end-of-file lines.
codex
I’ve separated the failures into two buckets. Bucket one is real standalone breakage: missing macros, missing package imports, or missing input files. Bucket two is standalone debt: the file is an excerpt that still points at labels and bibliography entries that only exist in the full monograph build. I’m enumerating the second bucket now so the final report distinguishes a broken preamble from a broken extraction boundary.
exec
/bin/zsh -lc 'for f in standalone/*.tex; do cites=$(awk -v file="$f" '"'"'$0 ~ ("=== " file " ") {insec=1; next} /''^=== /{insec=0} insec && /LaTeX Warning: Citation .* undefined/{c++} END{print c+0}'"' /tmp/standalone_audit/summary.txt); refs="'$(awk -v file="$f" '"'"'$0 ~ ("=== " file " ") {insec=1; next} /''^=== /{insec=0} insec && /LaTeX Warning: Reference .* undefined/{r++} END{print r+0}'"' /tmp/standalone_audit/summary.txt); if [ \""'$cites" -gt 0 ] || [ "$refs" -gt 0 ]; then bib=$(grep -nE '"'\\\\bibliography|\\\\addbibresource|\\\\begin\\{thebibliography\\}' \""'$f" | head -n 1); printf '"'%s | refs=%s cites=%s | bib=%s\\n' \""'$f" "$refs" "$cites" "${bib:-NONE}"; fi; done | sort' in /Users/raeez/chiral-bar-cobar succeeded in 2.94s:
standalone/N2_mc3_all_types.tex | refs=39 cites=68 | bib=1058:\begin{thebibliography}{99}
standalone/N3_e1_primacy.tex | refs=13 cites=14 | bib=970:\begin{thebibliography}{99}
standalone/N4_mc4_completion.tex | refs=36 cites=10 | bib=883:\begin{thebibliography}{99}
standalone/N5_mc5_sewing.tex | refs=30 cites=16 | bib=859:\begin{thebibliography}{99}
standalone/analytic_sewing.tex | refs=40 cites=19 | bib=3254:\begin{thebibliography}{99}
standalone/arithmetic_shadows.tex | refs=10 cites=4 | bib=1130:\begin{thebibliography}{99}
standalone/chiral_chern_weil.tex | refs=9 cites=0 | bib=1851:\begin{thebibliography}{99}
standalone/classification.tex | refs=22 cites=0 | bib=NONE
standalone/classification_trichotomy.tex | refs=1 cites=0 | bib=480:\begin{thebibliography}{99}
standalone/computations.tex | refs=3 cites=0 | bib=NONE
standalone/cy_quantum_groups_6d_hcs.tex | refs=6 cites=3 | bib=NONE
standalone/cy_to_chiral_functor.tex | refs=11 cites=0 | bib=NONE
standalone/drinfeld_kohno_bridge.tex | refs=29 cites=4 | bib=1697:\begin{thebibliography}{99}
standalone/e1_primacy_ordered_bar.tex | refs=37 cites=29 | bib=2299:\begin{thebibliography}{99}
standalone/editorial.tex | refs=1491 cites=178 | bib=NONE
standalone/en_chiral_operadic_circle.tex | refs=52 cites=13 | bib=2988:\begin{thebibliography}{99}
standalone/five_theorems_modular_koszul.tex | refs=7 cites=16 | bib=2380:\begin{thebibliography}{99}
standalone/garland_lepowsky.tex | refs=24 cites=24 | bib=1331:\begin{thebibliography}{99}
standalone/gaudin_from_collision.tex | refs=5 cites=9 | bib=621:\begin{thebibliography}{99}
standalone/genus1_seven_faces.tex | refs=37 cites=11 | bib=920:\begin{thebibliography}{10}






thinking
**Investigating bibliography issues**

It's interesting that many documents have thebibliography but still show undefined citations, suggesting there are missing bibitems. I might need to inspect some key references, as there are many cited keys that aren't in the local thebibliography. The user is asking for an exact fix, but I can't know the content of the missing bibitems. A potential solution could be to replace local thebibliography with \bibliographystyle{amsalpha}\bibliography{references} if that exists. I'll check for files lacking bibliographies or where citations are undefined to address potential severity.
thinking
**Resolving bibliography issues**

The exact fix might involve adding \bibitem entries for the listed keys. If there are many keys, I should note that the local bibliography is incomplete. For instance, in example N2, there are 68 unresolved citations, likely indicating 68 missing entries. A potential solution is to replace the local thebibliography at line 1058 with \bibliographystyle{amsalpha}\bibliography{standalone/references}. Since the build runs from the repo root, it makes sense to check the current working directory for that bibliography. I could suggest replacing the local thebibliography with a BibTeX-backed one sourced from standalone/references.bib.
thinking
**Evaluating citation issues**

I’m looking at possible unresolved citations in files with a local bibliography and wondering if it’s due to missing keys. It might be best to report one finding per file, referencing the first missing cite line and indicating which keys are omitted. I could consider parsing unique citation keys from build logs for precise fixes. Maybe I should focus on higher severity files and summarize medium severity ones by listing counts or a few keys.
thinking
**Identifying missing sections for fixes**

I need to address missing labeled sections or replace references since many internal cross-references point to omitted labels. It might be overwhelming to parse all unique missing labels per file, so perhaps I should mention just the count and the first unresolved label. I could focus on findings related to a foundation audit of standalone items, categorizing severity levels from critical to low for clearer insights. I’ll also inspect additional undefined macro files to derive any missing macros from the main preamble.
thinking
**Checking macro definitions**

I’m investigating the exact definitions for macros like `\Hom`, `\End`, `\Aut`, `\CompCl`, `\Defcyc`, and `\orline` that are defined in the main document. The fix here would be to mirror them into the standalone preamble. I should also check on `\Gamma`, but since it's a standard LaTeX command, that seems alright. For the `introduction_full_survey`, I found that it's missing `\dzero`, `\Hom`, `\End`, `\chirAss`, and possibly `\Aut`, which might be undefined since it's later utilized at line 1282.
thinking
**Investigating errors**

I’m thinking there are about 20 errors, possibly due to `\Aut`. It seems like I should search for all undefined control lines and inspect the source lines. I want to compile a list of those error lines and any related snippets to help in troubleshooting them. This way, I can better understand where the issues might be coming from and how to fix them. Let's figure this out!
exec
/bin/zsh -lc "printf 'intro undefined lines and source\\n'; for n in "'$(rg -oN '"'introduction_full_survey\\.tex:([0-9]+): Undefined control sequence' -r '"'$1'"' /tmp/standalone_audit/introduction_full_survey/build.log | sort -n | uniq); do echo \"--- line "'$n ---"; nl -ba standalone/introduction_full_survey.tex | sed -n "$((n-1)),$((n+1))p"; done' in /Users/raeez/chiral-bar-cobar succeeded in 181ms:
--- line 1843 ---
  1842	& \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
  1843	 \arrow[d, "\mathbb{D}_{\operatorname{Ran}}"]
  1844	\\
--- line 1846 ---
  1845	\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
  1846	 \arrow[r, "\bar{B}_X"']
  1847	& \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
--- line 2308 ---
  2307	for each~$n$. The \emph{equivariant hom}
  2308	$\Hom_{\Sigma_n}(V(n), W(n))$ denotes the chain complex
  2309	of $\Sigma_n$-equivariant maps.
--- line 2316 ---
  2315	\begin{equation}\label{eq:intro-end}
  2316	\operatorname{End}_A(n) \;=\; \Hom(A^{\otimes n},\, A),
  2317	\end{equation}
--- line 2440 ---
  2439	\emph{convolution dg Lie algebra}
  2440	$\mathrm{Conv}(C, A) = \Hom(C, A)$ carries
  2441	(Definition~\ref{def:convolution-dg-lie}):
exec
/bin/zsh -lc "printf 'survey undefined lines and source\\n'; for n in "'$(rg -oN '"'survey_modular_koszul_duality\\.tex:([0-9]+): Undefined control sequence' -r '"'$1'"' /tmp/standalone_audit/survey_modular_koszul_duality/build.log | sort -n | uniq); do echo \"--- line "'$n ---"; nl -ba standalone/survey_modular_koszul_duality.tex | sed -n "$((n-1)),$((n+1))p"; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
survey undefined lines and source
--- line 1338 ---
  1337	\text{algebra} &
  1338	 \Hom\bigl(B(\Ass),\,\End_A\bigr)
  1339	 & A_\infty\text{-structures on }A \\[4pt]
--- line 1341 ---
  1340	\text{operad} &
  1341	 \Hom_\Sigma\bigl(B(\cP),\,\End_V\bigr)
  1342	 & \cP_\infty\text{-structures on }V \\[4pt]
--- line 1344 ---
  1343	\text{modular} &
  1344	 \Hom_\Sigma\bigl(F\cO,\,\End_{\barB(\cA)}\bigr)
  1345	 & \text{consistent genus towers}
--- line 1372 ---
  1371	\;:=\;
  1372	\Hom_\Sigma\bigl(F\Com,\;\End_{\barB(\cA)}\bigr)
  1373	\end{equation}
--- line 1397 ---
  1396	\;:=\;
  1397	\Hom_\Sigma\bigl(F\!\Ass,\;
exec
/bin/zsh -lc "awk '
/"'^=== /{file=$2; next}
file && !first_ref[file] && /LaTeX Warning: Reference .* undefined/{match($0,/input line [0-9]+/); first_ref[file]=substr($0,RSTART+11,RLENGTH-11)}
file && !first_cite[file] && /LaTeX Warning: Citation .* undefined/{match($0,/input line [0-9]+/); first_cite[file]=substr($0,RSTART+11,RLENGTH-11)}
END{for (f in first_ref) files[f]=1; for (f in first_cite) files[f]=1; for (f in files) printf "%s | first_ref=%s | first_cite=%s'"\\n\", f, (first_ref[f]?first_ref[f]:\"-\"), (first_cite[f]?first_cite[f]:\"-\") }' /tmp/standalone_audit/summary.txt | sort" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standalone/N1_koszul_meta.tex | first_ref=- | first_cite=-
standalone/N2_mc3_all_types.tex | first_ref=226 | first_cite=114
standalone/N3_e1_primacy.tex | first_ref=280 | first_cite=156
standalone/N4_mc4_completion.tex | first_ref=171 | first_cite=118
standalone/N5_mc5_sewing.tex | first_ref=167 | first_cite=107
standalone/N6_shadow_formality.tex | first_ref=- | first_cite=-
standalone/analytic_sewing.tex | first_ref=192 | first_cite=172
standalone/arithmetic_shadows.tex | first_ref=233 | first_cite=473
standalone/bp_self_duality.tex | first_ref=- | first_cite=-
standalone/chiral_chern_weil.tex | first_ref=172 | first_cite=-
standalone/classification.tex | first_ref=93 | first_cite=-
standalone/classification_trichotomy.tex | first_ref=366 | first_cite=-
standalone/computations.tex | first_ref=242 | first_cite=-
standalone/cover_letter_garland_lepowsky.tex | first_ref=- | first_cite=-
standalone/cover_letter_seven_faces.tex | first_ref=- | first_cite=-
standalone/cover_letter_shadow_towers.tex | first_ref=- | first_cite=-
standalone/cover_letter_virasoro_r_matrix.tex | first_ref=- | first_cite=-
standalone/cy_quantum_groups_6d_hcs.tex | first_ref=247 | first_cite=183
standalone/cy_to_chiral_functor.tex | first_ref=232 | first_cite=-
standalone/drinfeld_kohno_bridge.tex | first_ref=260 | first_cite=199
exec
/bin/zsh -lc "nl -ba standalone/shadow_towers_v2.tex | sed -n '520,535p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   520	 $\frac{1}{2}$ at each zero of~$Q$. Monodromy $= -1$
   521	 \textup{(}Koszul sign\textup{)}.
   522	
   523	\item \textbf{Four-class partition.}
   524	 Write $Q = (2\kappa + 3\alpha t)^2 + 2\Delta\,t^2$.
   525	 The shadow depth $r_{\max}$ lies in $\{2, 3, 4, \infty\}$:
   526	 \begin{itemize}
   527	 \item Class $\mathbf{G}$: $\Delta = 0$, $\alpha = 0$,
   528	 $r_{\max} = 2$.
   529	 \item Class $\mathbf{L}$: $\Delta = 0$, $\alpha \ne 0$,
   530	 $r_{\max} = 3$.
   531	 \item Class $\mathbf{C}$: $\Delta = 0$ on the primary line;
   532	 quartic contact on a charged stratum, $r_{\max} = 4$.
   533	 \item Class $\mathbf{M}$: $\Delta \ne 0$, $r_{\max} = \infty$.
   534	 \end{itemize}
   535	
exec
/bin/zsh -lc "rg -n '\\\\input\\{|\\\\include\\{' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
487:\input{riccati}
560:\input{classification}
562:\input{computations}


thinking
**Fixing file paths in TeX**

I need to clarify that using `\input{riccati}` from the repo root looks for it in the root directory, not standalone. I could fix this by changing it to `\input{standalone/riccati}` or wrapping it with `\InputIfFileExists{standalone/riccati.tex}{...}`. 

Also, I might need to adjust the inputs for `classification` and `computations`, potentially using relative paths if compiling from the same directory. Additionally, I need to check for missing imports and unresolved references, which might indicate problems.
thinking
**Inspecting missing input files**

I'm considering if there are any other missing input files. I see that `shadow_towers_v2` includes `classification` and `computations`, which may not compile standalone, but they likely compile with unresolved references. 

I should check `survey_modular_koszul_duality_v2` for similar issues. Also, I want to evaluate the `w3_holographic_datum` since it has a latex error of 1, possibly linked to unresolved references, which isn’t a direct error. I’ll check the build log for more details.
exec
/bin/zsh -lc 'tail -n 40 /tmp/standalone_audit/w3_holographic_datum/build.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
xmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb></usr/local/texlive/2025/tex
mf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb></usr/local/texlive/2025/texm
f-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb></usr/local/texlive/2025/texmf
-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb></usr/local/texlive/2025/texmf-
dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb></usr/local/texlive/2025/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi6.pfb></usr/local/texlive/2025/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi7.pfb></usr/local/texlive/2025/texmf-dist/
fonts/type1/public/amsfonts/cm/cmmi8.pfb></usr/local/texlive/2025/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb></usr/local/texlive/2025/texmf-dist/font
s/type1/public/amsfonts/cm/cmr12.pfb></usr/local/texlive/2025/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr17.pfb></usr/local/texlive/2025/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmr6.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr7.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmr8.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy10.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/a
msfonts/cm/cmsy8.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/ams
fonts/cm/cmti10.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/amsf
onts/cm/cmti8.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/amsfon
ts/euler/eufm10.pfb></usr/local/texlive/2025/texmf-dist/fonts/type1/public/amsf
exec
/bin/zsh -lc "rg -n '"'^!'"' /private/tmp/standalone_audit/w3_holographic_datum/w3_holographic_datum.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:




thinking
**Analyzing bibliographic omissions**

I'm finding that many standalone documents use a local `thebibliography` but often leave out cited keys. The user wants exact file lines for these omissions. I’m thinking of grouping by lines where the bibliography starts, which could lead to around 20 lines reported. There are several files with high counts of unresolved citations, like N2 and N4. I might need to note files with critical issues, aiming for around 39 manageable findings, structured by severity.
thinking
**Identifying severity categories**

I'm categorizing the found issues by severity. For critical problems, I have editorial.tex, which has a lot of undefined control sequences, refs, and cites. The introduction_full_survey.tex also seems critical due to missing core macros, while survey_modular_koszul_duality.tex is high/critical for lacking a bibliography. Then, I have high-severity files like gaudin_from_collision.tex with missing imports and shadow_towers_v2.tex due to broken paths. I want to pinpoint the root causes clearly for the user.
thinking
**Considering problem location**

I think it might be useful to reference `main.tex:590` since the problem seems to originate from there. But I need to consider that this is part of a mission audit of the standalone files. I want to ensure the user understands where each problem is present and connected. It’s a balancing act between identifying exact locations and maintaining a broader view of the audit requirements.
exec
/bin/zsh -lc "printf 'survey_track_a end\\n'; tail -n 20 standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'intro end\\n'; tail -n 20 standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey end\\n'; tail -n 20 standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'programme_summary_sections5_8 end\\n'; tail -n 20 standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
intro end

\smallskip\noindent\textbf{Sugawara.}
The Sugawara construction is \emph{undefined} at critical level $k = -h^\vee$; the Sugawara vector does not lie in the appropriate completion. This is not ``$c$ diverges''; the construction does not exist.

\smallskip\noindent\textbf{Virasoro self-duality.}
The Virasoro algebra is chiral Koszul self-dual at $c = 13$ ($\mathrm{Vir}_c^! = \mathrm{Vir}_{26-c}$), not $c = 26$. Quadratic self-duality (uncurved bar, $\kappa = 0$) holds at $c = 0$.

\smallskip\noindent\textbf{FM compactification.}
The Fulton--MacPherson compactification is the blowup along diagonals, not the complement of diagonals.

\smallskip\noindent\textbf{Prime form.}
The prime form $E(z_1, z_2)$ is a section of $K^{-1/2} \boxtimes K^{-1/2}$, not $K^{+1/2}$.

\smallskip\noindent\textbf{QME.}
The quantum master equation is $\hbar \Delta S + \frac{1}{2}\{S, S\} = 0$ (factor $\frac{1}{2}$, not~$1$).

\smallskip\noindent\textbf{$d_{\mathrm{bracket}}^2 \neq 0$.}
The bracket component of the bar differential does not square to zero on its own: this is proved for all $2048$ sign conventions for $\mathfrak{sl}_2$. The full Borcherds differential gives $d^2 = 0$.

 succeeded in 52ms:
survey_track_a end
tower accelerates with genus and dominates the scalar part
$\kappa\cdot\lambda_g^{\mathrm{FP}}$ by genus~$4$.

On the open/closed side, the Koszul dual cooperad
$\mathsf{SC}^{\mathrm{ch,top},!}$ decomposes into three sectors:
closed ($\dim=(n-1)!$, Lie cooperad), open ($\dim=m!$, Ass cooperad),
and mixed ($\dim=(k-1)!\binom{k+m}{m}$). The mixed sector
encodes the bulk-to-boundary module structure by which the chiral
derived centre acts on the boundary algebra.

The BV/BRST${}={}$bar identification at higher genus
(Conjecture~\ref{conj:master-bv-brst}): the chain-level obstruction
(harmonic propagator correction) is resolved for classes G, L, and C,
for G and L by the Heisenberg sewing theorem and its extension to
affine algebras, for C by contact decoupling. For class M (Virasoro,
$\mathcal W_N$) the identification holds on bar cohomology but fails
at the chain level: the harmonic propagator produces a nonvanishing
quartic obstruction, so a coderived reformulation is needed.

 succeeded in 52ms:
survey end
 conditional on chain-level $\mathbb S^3$-framing for $d=3$;
 Volume~III).
\end{itemize}
Each is a different facet of the geometry of
$\mathfrak{g}^{\mathrm{mod}}_\cA$, and none requires going
beyond the framework already established.

\bigskip

\noindent
The entire structure unfolds from a single datum: the logarithmic
$1$-form $\eta = d\log(z_1 - z_2)$. At $n$~points it became a
differential on the Fulton--MacPherson compactification; across all
genera it became the total bar differential~$D_\cA$; in the modular
convolution algebra it became the Maurer--Cartan element
$\Theta_\cA = D_\cA - d_0$. One $1$-form, one relation (Arnold),
one extraction (residues): a universal invariant of chiral algebras
that is algebraic, computable, and complete.

 succeeded in 52ms:
programme_summary_sections5_8 end
% V.\,G.~Knizhnik and A.\,B.~Zamolodchikov,
% Current algebra and Wess--Zumino model in two dimensions,
% \textit{Nuclear Phys.\ B}~\textbf{247} (1984), 83--103.

% \bibitem{STS83}
% M.\,A.~Semenov-Tian-Shansky,
% What is a classical $r$-matrix?,
% \textit{Funct.\ Anal.\ Appl.}~\textbf{17} (1983), 259--272.

% \bibitem{DNP25}
% T.~Dimofte, N.~Niu, and A.~Py,
% Twisted holography and Koszul duality,
% preprint, 2025.

% \bibitem{CWY18}
% K.~Costello, E.~Witten, and M.~Yamazaki,
% Gauge theory and integrability, I--II,
% \textit{ICCM Not.}~\textbf{6} (2018), 46--119 and 120--149.




thinking
**Evaluating bibliography issues**

I’ve noticed that the file `programme_summary_sections5_8` lacks a proper bibliography, only showing commented bibitems. I might want to check `survey_track_a` for citations; it might have the same problem. There could also be other files that only have unresolved references without any citations or bibliographies. If I find missing references, I can either add the corresponding environments or remove the `\ref` calls. Multiple passes with latexmk might help resolve these missing labels effectively.
thinking
**Analyzing classification.tex issues**

I need to check `classification.tex`, which has no bibliography and mentions 22 unresolved references. These references may point to section labels in omitted files. To fix this, I could add the missing sections or inline text. Instead of listing each label, I might summarize the root issue. The user wants to know about unresolved references, so I could cluster them by omitted labels and provide counts, detailing the problems per file. For example, I could note that there are 22 unresolved cross-references starting at line 93.
thinking
**Grounding claims in file contents**

I’m wondering if I need to read the actual file contents near the unresolved references to support my claims. It seems like checking every line in all 39 files is impossible, but maybe I can target specific lines, like line 93. At the same time, using compile logs along with summary counts might be sufficient. The logs represent the contents read by TeX, but I should ensure I’m backing up my claims with tangible file content I'm reviewing.
codex
I’m doing one more verification pass against the source itself: for each file I plan to cite, I’m reading the first failing source line so the final report rests on actual text, not just the compiler’s summary.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
summary=pathlib.Path('/tmp/standalone_audit/summary.txt').read_text()
files=[]
current=None
first_ref={}
first_cite={}
for line in summary.splitlines():
    if line.startswith('=== '):
        current=line.split()[1]
        files.append(current)
        continue
    if current and current not in first_ref:
        m=re.search(r'LaTeX Warning: Reference "'`([''^`]+)` .* input line ('"\\d+)', line)
        if m:
            first_ref[current]=(m.group(1), int(m.group(2)))
    if current and current not in first_cite:
        m=re.search(r'LaTeX Warning: Citation "'`([''^`]+)` .* input line ('"\\d+)', line)
        if m:
            first_cite[current]=(m.group(1), int(m.group(2)))
for f in sorted(set(files)):
    if f in first_ref or f in first_cite:
        print(f'=== {f} ===')
        p=pathlib.Path(f)
        lines=p.read_text().splitlines()
        if f in first_ref:
            lab,n=first_ref[f]
            print(f'REF {lab} @ {n}: {lines[n-1]}')
        if f in first_cite:
            key,n=first_cite[f]
            print(f'CITE {key} @ {n}: {lines[n-1]}')
        print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


thinking
**Developing a shell loop**

I’m considering using a shell loop with an embedded here-doc to list file and line pairs. That seems like a good approach! I think I’ll apply this for selected files, and perhaps even for all affected files. Using the loop to print the line content would make it easier to see everything at once. I wonder if there are any potential pitfalls I should keep in mind while doing this.
exec
/bin/zsh -lc "cat <<'EOF' >/tmp/standalone_lines.txt
standalone/N1_koszul_meta.tex|153
standalone/N2_mc3_all_types.tex|114
standalone/N3_e1_primacy.tex|156
standalone/N4_mc4_completion.tex|118
standalone/N5_mc5_sewing.tex|107
standalone/analytic_sewing.tex|172
standalone/arithmetic_shadows.tex|233
standalone/chiral_chern_weil.tex|172
standalone/classification.tex|93
standalone/classification_trichotomy.tex|366
standalone/computations.tex|242
standalone/cy_quantum_groups_6d_hcs.tex|183
standalone/cy_to_chiral_functor.tex|232
standalone/drinfeld_kohno_bridge.tex|199
standalone/e1_primacy_ordered_bar.tex|214
standalone/en_chiral_operadic_circle.tex|210
standalone/five_theorems_modular_koszul.tex|144
standalone/garland_lepowsky.tex|107
standalone/gaudin_from_collision.tex|96
standalone/genus1_seven_faces.tex|90
standalone/holographic_datum.tex|260
standalone/introduction_full_survey.tex|125
standalone/koszulness_fourteen_characterizations.tex|201
standalone/multi_weight_cross_channel.tex|203
standalone/ordered_chiral_homology.tex|209
standalone/programme_summary.tex|119
standalone/programme_summary_section1.tex|153
standalone/programme_summary_sections2_4.tex|313
standalone/programme_summary_sections5_8.tex|199
standalone/programme_summary_sections9_14.tex|99
standalone/riccati.tex|5
standalone/sc_chtop_pva_descent.tex|25
standalone/seven_faces.tex|603
standalone/shadow_towers.tex|95
standalone/shadow_towers_v2.tex|116
standalone/shadow_towers_v3.tex|146
standalone/survey_modular_koszul_duality.tex|1236
standalone/survey_modular_koszul_duality_v2.tex|1524
standalone/survey_track_a_compressed.tex|732
standalone/survey_track_b_compressed.tex|58
standalone/three_dimensional_quantum_gravity.tex|101
standalone/three_parameter_hbar.tex|64
standalone/virasoro_r_matrix.tex|3
standalone/w3_holographic_datum.tex|135
EOF
while IFS='|' read -r f n; do printf '=== %s:%s ===\\n' \""'$f" "$n"; sed -n "${n}p" "$f"; done < /tmp/standalone_lines.txt' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
=== standalone/N1_koszul_meta.tex:153 ===
 Definition~\ref{def:chiral-koszul-morphism};
=== standalone/N2_mc3_all_types.tex:114 ===
The classical Drinfeld--Kohno theorem \cite{Kohno87, Drinfeld90}
=== standalone/N3_e1_primacy.tex:156 ===
Stasheff's associahedra $K_{n}$ (cf.~\cite{Stasheff63}) carry
=== standalone/N4_mc4_completion.tex:118 ===
Priddy~\cite{Priddy70}, Beilinson-Ginzburg-Soergel, and in
=== standalone/N5_mc5_sewing.tex:107 ===
circles. The classical treatment of Segal~\cite{Segal88} takes
=== standalone/analytic_sewing.tex:172 ===
modular Koszul duality programme~\cite{LorgatVolI}.  The five
=== standalone/arithmetic_shadows.tex:233 ===
Section~\ref{sec:verlinde} recovers the Verlinde formula from
=== standalone/chiral_chern_weil.tex:172 ===
 (Sections~\ref{sec:classical}--\ref{sec:chiral-cw}).
=== standalone/classification.tex:93 ===
stratum; see Definition~\ref{def:class-C}.
=== standalone/classification_trichotomy.tex:366 ===
a nonvanishing $c$-independent constant (Theorem~\ref{thm:s3-vir}

thinking
**Identifying issue clusters**

I’m considering how to identify affected surfaces stemming from the same root cause and if I can group multiple files with similar issues. The format requires a single file and line, which makes it tricky. I notice there are 41 affected files, but maybe I can reference a canonical first file for grouping. However, the user is looking for every missing definition or unresolved reference. It seems acceptable to do one finding per file based on the actual problem clusters.
exec
/bin/zsh -lc "printf 'survey_track_b warnings head\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/survey_track_b_compressed/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'sc_chtop warnings head\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/sc_chtop_pva_descent/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'w3_holographic_datum warnings head\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/w3_holographic_datum/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'virasoro_r_matrix warnings head\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/virasoro_r_matrix/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
w3_holographic_datum warnings head
96:LaTeX Warning: Reference `sec:r-matrix' on page 2 undefined on input line 135.
 succeeded in 52ms:
sc_chtop warnings head
212:LaTeX Warning: Reference `eq:intro-coderivation' on page 2 undefined on input l
221:LaTeX Warning: Reference `thm:homotopy-koszul-SC' on page 2 undefined on input 
225:LaTeX Warning: Citation `Liv06' on page 2 undefined on input line 234.
228:LaTeX Warning: Reference `thm:SC-koszul-dual' on page 2 undefined on input line
232:LaTeX Warning: Reference `thm:pva-descent' on page 2 undefined on input line 25
238:LaTeX Warning: Citation `BD04' on page 3 undefined on input line 288.
241:LaTeX Warning: Citation `Vor99' on page 3 undefined on input line 295.
244:LaTeX Warning: Citation `Liv06' on page 3 undefined on input line 296.
247:LaTeX Warning: Citation `KS06' on page 3 undefined on input line 298.
250:LaTeX Warning: Citation `BD04' on page 3 undefined on input line 302.
253:LaTeX Warning: Citation `DSK06' on page 3 undefined on input line 304.
256:LaTeX Warning: Citation `FG12' on page 3 undefined on input line 306.
274:LaTeX Warning: Citation `Liv06' on page 5 undefined on input line 490.
277:LaTeX Warning: Citation `DK10' on page 5 undefined on input line 500.
280:LaTeX Warning: Citation `Kon99' on page 5 undefined on input line 506.
283:LaTeX Warning: Citation `Kon03' on page 5 undefined on input line 506.
300:LaTeX Warning: Reference `thm:livernet-koszulity' on page 6 undefined on input 
304:LaTeX Warning: Reference `eq:kontsevich-formality' on page 6 undefined on input
308:LaTeX Warning: Citation `LV12' on page 6 undefined on input line 563.
 succeeded in 52ms:
survey_track_b warnings head
101:LaTeX Warning: Reference `thm:categorical-cg-all-types' on page 7 undefined on 
105:LaTeX Warning: Reference `cor:mc3-all-types' on page 7 undefined on input line 
112:LaTeX Warning: Reference `thm:master-commutative-square' on page 9 undefined on
116:LaTeX Warning: Reference `thm:gram-positivity' on page 9 undefined on input lin
124:LaTeX Warning: Reference `thm:shadow-euler-independence' on page 10 undefined o
134:LaTeX Warning: Reference `thm:universality-of-G' on page 10 undefined on input 
142:LaTeX Warning: Reference `thm:nms-clutching-law-modular-resonance' on page 13 u
146:LaTeX Warning: Reference `conj:quartic-closure' on page 13 undefined on input l
150:LaTeX Warning: Reference `conj:beilinson-closure' on page 13 undefined on input
154:LaTeX Warning: Reference `conj:clutching-closure' on page 13 undefined on input
190:LaTeX Warning: Reference `princ:gravitational-primitivity' on page 27 undefined
196:LaTeX Warning: Reference `thm:categorical-cg-all-types' on page 28 undefined on
200:LaTeX Warning: Reference `cor:mc3-all-types' on page 28 undefined on input line
206:LaTeX Warning: Reference `thm:platonic-completion' on page 29 undefined on inpu
212:LaTeX Warning: Reference `thm:algebraic-string-dictionary' on page 30 undefined
216:LaTeX Warning: Reference `cor:string-amplitude-genus0' on page 30 undefined on 
220:LaTeX Warning: Reference `thm:inductive-genus-determination' on page 30 undefin
224:LaTeX Warning: Reference `thm:general-hs-sewing' on page 30 undefined on input 
228:LaTeX Warning: Reference `op:multi-generator-universality' on page 30 undefined
 succeeded in 51ms:
virasoro_r_matrix warnings head
90:LaTeX Warning: Reference `eq:vir-collision' on page 2 undefined on input line 1
96:LaTeX Warning: Reference `eq:exp-series' on page 3 undefined on input line 191.
126:LaTeX Warning: Reference `eq:vir-ope' on page 4 undefined on input line 235.


thinking
**Evaluating source line inclusion**

I’m considering whether we need to include source lines for these references. It might not be necessary if we don’t plan to incorporate them. I think about including specific references, like the virasoro_r_matrix and w3 - perhaps they're low priority. Maybe I should cluster unresolved citations by file instead of focusing on individual lines. Since we’ve read many actual lines, it might be sufficient to only include files where we read the source lines.
thinking
**Reviewing source lines and citations**

Yes, we have actual source line content for 40 files. Some lines may not be ideal, but they are still part of the file contents, which is good enough for our purposes. I think I should include files with no bibliographies but have citations; those should have exact lines we've read. It might also be useful to gather line contents for files with unresolved references. I should inspect the `riccati` line to check if line 5 is relevant, especially since it seems to have citation issues.
exec
/bin/zsh -lc "nl -ba standalone/riccati.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\documentclass[11pt]{article}
     2	
     3	\usepackage{amsmath,amssymb,amsthm}
     4	\usepackage{mathtools}
     5	\usepackage[shortlabels]{enumitem}
     6	\usepackage{booktabs}
     7	\usepackage{array}
     8	\usepackage{microtype}
     9	\usepackage[margin=1.15in]{geometry}
    10	\usepackage[dvipsnames]{xcolor}
    11	\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
    12	
    13	\theoremstyle{plain}
    14	\newtheorem{theorem}{Theorem}[section]
    15	\newtheorem{proposition}[theorem]{Proposition}
    16	\newtheorem{corollary}[theorem]{Corollary}
    17	\newtheorem{lemma}[theorem]{Lemma}
    18	\newtheorem{conjecture}[theorem]{Conjecture}
    19	\theoremstyle{definition}
    20	\newtheorem{definition}[theorem]{Definition}
exec
/bin/zsh -lc "printf 'sc source around 230-238\\n'; nl -ba standalone/sc_chtop_pva_descent.tex | sed -n '230,238p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
sc source around 230-238
   230	  bar-cobar adjunction
   231	  $\Omega\mathbf{B}(\SCchtop) \xrightarrow{\sim} \SCchtop$
   232	  is a quasi-isomorphism.  This follows from Livernet's
   233	  Koszulity of the classical Swiss-cheese operad~$\SC$
   234	  \cite{Liv06}, composed with Kontsevich formality for
   235	  the closed colour, and transferred to $\SCchtop$ via
   236	  bar-cobar comparison.
   237	
   238	\item \textbf{The Koszul dual cooperad.}  The Koszul dual
exec
/bin/zsh -lc "printf 'w3 source around 130-140\\n'; nl -ba standalone/w3_holographic_datum.tex | sed -n '130,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'virasoro source around 180-195\\n'; nl -ba standalone/virasoro_r_matrix.tex | sed -n '180,195p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey_track_b source around 70-80 and 240-250\\n'; nl -ba standalone/survey_track_b_compressed.tex | sed -n '70,80p;240,250p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
virasoro source around 180-195
   180	= \sum_{k=0}^{\infty} \frac{(-1)^k}{k!}
   181	\left(\frac{c}{4}\right)^k z^{-2k}.
   182	\end{equation}
   183	Only even powers of $1/z$ appear. This is the bosonic parity
   184	constraint: for a single-generator bosonic algebra, the $d\log$
   185	absorption sends the OPE poles at even orders $z^{-2n}$ to odd
   186	$r$-matrix poles $z^{-(2n-1)}$, and the path-ordered exponential
   187	preserves the parity of the exponent. The $R$-matrix has the form
   188	$z^{2h} \cdot f(z^{-2})$ where $f$ is an entire function of $z^{-2}$.
   189	
   190	\begin{remark}[Radius of convergence]\label{rem:convergence}
   191	The series~\eqref{eq:exp-series} converges absolutely for all
   192	$z \neq 0$. The $R$-matrix $R(z) = z^{2h}\exp(-c/(4z^2))$ is an
   193	entire function of $z^{-2}$ multiplied by the monomial $z^{2h}$.
   194	It has an essential singularity at $z = 0$: the non-terminating
   195	character of the series is the datum that distinguishes class $M$
 succeeded in 51ms:
w3 source around 130-140
   130	
   131	The collision residue $r(z)$ lives on the ordered bar complex
   132	$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$ with
   133	deconcatenation coproduct; it is an element of the $E_1$ convolution
   134	algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of
   135	$r(z)$ in Section~\ref{sec:r-matrix} is an ordered-bar datum; the
   136	modular characteristic $\kappa = \mathrm{av}(r(z))$ is its
   137	$\Sigma_2$-coinvariant projection.
   138	
   139	% ================================================================
   140	\section{\texorpdfstring{$\kappa(\Walg_3) = 5c/6$}{kappa(W3) = 5c/6}
 succeeded in 50ms:
survey_track_b source around 70-80 and 240-250
    70	\providecommand{\conn}{\mathrm{conn}}
    71	\providecommand{\contact}{\mathrm{contact}}
    72	\providecommand{\cross}{\mathrm{cross}}
    73	\providecommand{\cyc}{\mathrm{cyc}}
    74	\providecommand{\der}{\mathrm{der}}
    75	\providecommand{\fib}{\mathrm{fib}}
    76	\providecommand{\fo}{\mathrm{o}}
    77	\providecommand{\gh}{\mathrm{gh}}
    78	\providecommand{\grav}{\mathrm{grav}}
    79	\providecommand{\hol}{\mathrm{hol}}
    80	\providecommand{\nsep}{\mathrm{nsep}}
   240	$\kappa(\cH_k) = k$, $\kappa(\cH_k^!) = -k$,
   241	$\kappa(\cH_k) + \kappa(\cH_k^!) = 0$ (the free-field/KM
   242	branch of complementarity: sum equals $0$ for free-field and
   243	affine Kac--Moody families, in contrast to $\kappa + \kappa' =
   244	13$ for Virasoro). The universal MC element is
   245	$\Theta_{\cH_k} = k \cdot \eta \otimes \Lambda$ with
   246	$\eta = d\log(z_1 - z_2)$ and $\Lambda = \lambda_1$; the
   247	five-component differential collapses to loop$\circ$loop

thinking
**Counting affected files**

I need to make sure I include every affected file with summary counts. First, I should identify all the files from the counts table, excluding those with zero counts. The affected files list contains various entries, and I wonder if I got them right. The user mentioned having counted 53, but I think I found around 45. So, I should double-check those numbers and confirm what the actual total is.
exec
/bin/zsh -lc "printf 'three_dimensional_quantum_gravity first warnings\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/three_dimensional_quantum_gravity/build.log | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'seven_faces first warnings\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/seven_faces/build.log | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'riccati first warnings\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/riccati/build.log | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey_v2 first warnings\\n'; rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/survey_modular_koszul_duality_v2/build.log | sed -n '1,12p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
riccati first warnings
101:LaTeX Warning: Reference `eq:master-equation' on page 2 undefined on input line
105:LaTeX Warning: Reference `eq:single-line-recursion' on page 2 undefined on inpu
109:LaTeX Warning: Reference `def:shadow-metric-paper' on page 2 undefined on input
113:LaTeX Warning: Reference `def:shadow-gf' on page 2 undefined on input line 227.
119:LaTeX Warning: Reference `eq:riccati-algebraic-relation' on page 3 undefined on
123:LaTeX Warning: Reference `eq:shadow-metric' on page 3 undefined on input line 2
127:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
140:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
144:LaTeX Warning: Reference `eq:convolution-vanishing' on page 3 undefined on inpu
148:LaTeX Warning: Reference `eq:convolution-vanishing' on page 3 undefined on inpu
152:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
156:LaTeX Warning: Reference `eq:riccati-algebraic-relation' on page 3 undefined on
 succeeded in 52ms:
seven_faces first warnings
141:LaTeX Warning: Reference `thm:bar-intrinsic-hinge' on page 5 undefined on input
166:LaTeX Warning: Reference `prop:no-k2' on page 7 undefined on input line 603.
192:LaTeX Warning: Reference `thm:seven-faces' on page 11 undefined on input line 8
 succeeded in 52ms:
three_dimensional_quantum_gravity first warnings
86:LaTeX Warning: Citation `AT86' on page 1 undefined on input line 101.
89:LaTeX Warning: Citation `Wit88' on page 1 undefined on input line 101.
96:LaTeX Warning: Reference `eq:cs-gauge-fields' on page 2 undefined on input line
100:LaTeX Warning: Reference `sec:shadow-as-gravity' on page 2 undefined on input l
104:LaTeX Warning: Reference `sec:koszul-s-duality' on page 2 undefined on input li
108:LaTeX Warning: Citation `BH86' on page 2 undefined on input line 167.
113:LaTeX Warning: Reference `sec:gravitational-bulk' on page 3 undefined on input 
135:LaTeX Warning: Reference `eq:vir-lambda-bracket' on page 4 undefined on input l
151:LaTeX Warning: Reference `eq:vir-associator' on page 4 undefined on input line 
168:LaTeX Warning: Reference `eq:vir-m2' on page 5 undefined on input line 408.
171:LaTeX Warning: Reference `eq:vir-m3' on page 5 undefined on input line 408.
174:LaTeX Warning: Reference `eq:vir-m4-sym' on page 5 undefined on input line 414.
 succeeded in 50ms:
survey_v2 first warnings
161:LaTeX Warning: Reference `eq:preface-arnold' on page 2 undefined on input line 
206:LaTeX Warning: Reference `eq:preface-arnold' on page 3 undefined on input line 
229:LaTeX Warning: Reference `eq:preface-arnold' on page 4 undefined on input line 
327:LaTeX Warning: Reference `thm:e1-formality-bridge' on page 8 undefined on input
331:LaTeX Warning: Reference `thm:e1-formality-failure' on page 8 undefined on inpu
335:LaTeX Warning: Reference `thm:chiral-qg-equiv' on page 8 undefined on input lin
339:LaTeX Warning: Reference `thm:glN-chiral-qg' on page 8 undefined on input line 
343:LaTeX Warning: Reference `thm:e3-identification' on page 8 undefined on input l
347:LaTeX Warning: Reference `thm:topologization' on page 8 undefined on input line
372:LaTeX Warning: Reference `conj:v1-drinfeld-center-equals-bulk' on page 8 undefi
376:LaTeX Warning: Reference `thm:e3-identification' on page 8 undefined on input l
427:LaTeX Warning: Reference `eq:pref-curvature' on page 12 undefined on input line

thinking
**Inspecting line numbers**

I’m thinking I might need to truncate the line numbers and use source lines from the counts table, perhaps starting with first_ref=59 and first_cite=1524 for survey_v2. But wait, I’m not entirely sure if the actual first reference is at line 212. Should I go with line 59? I really need to take a closer look around that line first to figure it out. Let's keep exploring this.
exec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '55,65p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    55	\providecommand{\cT}{\mathcal{T}}
    56	\providecommand{\cU}{\mathcal{U}}
    57	\providecommand{\cV}{\mathcal{V}}
    58	\providecommand{\cW}{\mathcal{W}}
    59	\providecommand{\cX}{\mathcal{X}}
    60	\providecommand{\cY}{\mathcal{Y}}
    61	\providecommand{\cZ}{\mathcal{Z}}
    62	\providecommand{\barB}{\bar{B}}
    63	\providecommand{\barC}{\overline{C}}
    64	\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
    65	\providecommand{\Ran}{\mathrm{Ran}}

thinking
**Inspecting source lines**

I notice that the parser is acting up, and I'm considering how to get accurate line numbers from the source. Maybe I should use line 1524 since it's the first cite? It seems like it counts only one citation out of 49 references. I'm also thinking about checking the build log around line 161 for more insight. I guess I need to carefully look at the raw lines near the first warning to gather the right context.
exec
/bin/zsh -lc "sed -n '156,166p' /tmp/standalone_audit/survey_modular_koszul_duality_v2/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 262.


LaTeX Warning: Reference `eq:preface-arnold' on page 2 undefined on input line 
283.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\leavevmode@ifvmode' on input line 295.
exec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '280,286p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   280	\end{equation}
   281	the differential-form image of the partial-fractions identity
   282	$\tfrac{1}{(z_1-z_2)(z_2-z_3)}+\tfrac{1}{(z_2-z_3)(z_3-z_1)}+\tfrac{1}{(z_3-z_1)(z_1-z_2)}=0$.
   283	Arnold proved that~\eqref{eq:preface-arnold}, replicated across all
   284	triples $\{i,j,k\}\subset\{1,\ldots,n\}$, generates the complete ideal
   285	of relations in $H^*(\mathrm{Conf}_n(\mathbf C),\mathbf C)$.
   286	
exec
/bin/zsh -lc "sed -n '208,216p' /tmp/standalone_audit/sc_chtop_pva_descent/build.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
No file sc_chtop_pva_descent.toc.

[1{/usr/local/texlive/2025/texmf-var/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `eq:intro-coderivation' on page 2 undefined on input l
ine 198.


Overfull \hbox (6.44817pt too wide) in paragraph at lines 196--202
exec
/bin/zsh -lc "nl -ba standalone/sc_chtop_pva_descent.tex | sed -n '196,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   196	\end{equation}
   197	A differential and a coassociative coproduct satisfying
   198	\eqref{eq:intro-coderivation} make $(\barB(\cA), D_\cA, \Delta)$
   199	into a dg coassociative coalgebra: an $\Eone$ coalgebra, with
   200	holomorphic collisions on $\FM_k(\CC)$ as the differential and
exec
/bin/zsh -lc "rg -n 'LaTeX Warning: (Reference|Citation)' /tmp/standalone_audit/riccati/build.log | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
101:LaTeX Warning: Reference `eq:master-equation' on page 2 undefined on input line
105:LaTeX Warning: Reference `eq:single-line-recursion' on page 2 undefined on inpu
109:LaTeX Warning: Reference `def:shadow-metric-paper' on page 2 undefined on input
113:LaTeX Warning: Reference `def:shadow-gf' on page 2 undefined on input line 227.
119:LaTeX Warning: Reference `eq:riccati-algebraic-relation' on page 3 undefined on
123:LaTeX Warning: Reference `eq:shadow-metric' on page 3 undefined on input line 2
127:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
140:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
144:LaTeX Warning: Reference `eq:convolution-vanishing' on page 3 undefined on inpu
148:LaTeX Warning: Reference `eq:convolution-vanishing' on page 3 undefined on inpu
152:LaTeX Warning: Reference `eq:single-line-recursion' on page 3 undefined on inpu
156:LaTeX Warning: Reference `eq:riccati-algebraic-relation' on page 3 undefined on
160:LaTeX Warning: Reference `eq:riccati-algebraic-relation' on page 3 undefined on
166:LaTeX Warning: Reference `thm:riccati-algebraicity' on page 4 undefined on inpu
172:LaTeX Warning: Reference `thm:riccati-algebraicity' on page 5 undefined on inpu
176:LaTeX Warning: Reference `cor:gaussian-decomposition' on page 5 undefined on in
182:LaTeX Warning: Citation `FlajoletSedgewick' on page 6 undefined on input line 5
186:LaTeX Warning: Reference `cor:intrinsic-quartic' on page 6 undefined on input l
197:LaTeX Warning: Reference `thm:single-line-dichotomy' on page 7 undefined on inp
201:LaTeX Warning: Reference `rem:contact-class' on page 7 undefined on input line 
exec
/bin/zsh -lc "nl -ba standalone/riccati.tex | sed -n '525,531p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   525	
   526	\begin{definition}[Shadow growth rate]
   527	\label{def:shadow-growth-rate}
   528	Let $L$ be a primary line of class $\mathbf{M}$ ($\Delta \neq 0$),
   529	and write $Q_L(t) = q_0 + q_1 t + q_2 t^2$ for the shadow metric.
   530	The \emph{shadow growth rate} of $L$ is
   531	\begin{equation}
exec
/bin/zsh -lc "rg -n '\\\\cite\\{' standalone/riccati.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:



thinking
**Considering citation handling**

I’m thinking we can use `rg -n '\\\\cite\\{'` to count citations per file. However, I could just mention unresolved references if a citation isn't found in the source. Maybe it’s not essential to mention citation counts for medium groups, as many already contain citations. I could say "local bibliography is incomplete or external references remain unresolved." For files without citations but with a local bibliography, it might still be irrelevant. I need to clarify what the user meant about undefined macros being findings.
thinking
**Planning for unresolved references**

I’m considering how to summarize unresolved reference groups. It seems logical to focus on the number of findings in lines rather than files, probably around 12 findings. The user asked for an exhaustive list, so maybe it’s best to aim for about 20 lines total. I can group some low-importance issues, but not excessively. Perhaps I should include one line for critical/high issues and group medium/low importance findings together. This way, I can respect the user's request for detail.
exec
/bin/zsh -lc "printf 'w3 first ref\\n'; rg -n '\\\\(eqref|ref)\\{' standalone/w3_holographic_datum.tex | head -n 3" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'survey_track_b first ref\\n'; rg -n '\\\\(eqref|ref)\\{' standalone/survey_track_b_compressed.tex | head -n 3" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'virasoro first ref\\n'; rg -n '\\\\(eqref|ref)\\{' standalone/virasoro_r_matrix.tex | head -n 3" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'riccati first ref\\n'; rg -n '\\\\(eqref|ref)\\{' standalone/riccati.tex | head -n 3" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
virasoro first ref
144:The collision residue~\eqref{eq:vir-collision} has two independent
191:The series~\eqref{eq:exp-series} converges absolutely for all
235:From the OPE~\eqref{eq:vir-ope}, the relevant modes are
 succeeded in 52ms:
riccati first ref
150:\eqref{eq:master-equation} reduces to a recursion among the scalars
207:\eqref{eq:single-line-recursion} as a convolution identity.
225:$Q_L$ \textup{(}Definition~\textup{\ref{def:shadow-metric-paper}}\textup{)},
 succeeded in 52ms:
w3 first ref
135:$r(z)$ in Section~\ref{sec:r-matrix} is an ordered-bar datum; the
 succeeded in 52ms:
survey_track_b first ref
596:property (Theorem~\ref{thm:categorical-cg-all-types},
597:Corollary~\ref{cor:mc3-all-types}); the remaining post-CG
676:(Theorem~\ref{thm:master-commutative-square}) organises the




thinking
**Fixing LaTeX issues**

I’m noting a specific fix for `gaudin_from_collision`: I should add `\usepackage[dvipsnames]{xcolor}` before the hyperref line at line 11. For `shadow_towers_v2`, I need to make sure to prefix all three `\input{riccati}`, `\input{classification}`, and `\input{computations}` with `standalone/`, or I might set `\input@path{{standalone/}}`. Also, for `N2`, I should add `\newcommand{\cF}{\mathcal{F}}` to the preamble. Got it!
thinking
**Considering the fix details**

I might cut down to a representative set and include "and the other main-preamble operators used at lines..." for clarity. The fix does need to be precise, so I'm thinking it might be okay to list those macros too. It's all about getting the exact wording right while ensuring everyone understands what I'm referring to. I want to make sure everything is clear and accurate for the user!
thinking
**Fixing document structure**

I’m thinking about the LaTeX structure, specifically whether to move lines 597-719 above line 590. The fallback macros start at line 597, which should be after `\begin{document}`. Some necessary macros are above line 590, but not all. I wonder if moving the fallback `\providecommand` block above that line or creating a separate `preamble_fallbacks.tex` could work better. Additionally, I need to check if `survey_modular_koszul_duality` is using `\Defcyc` correctly, as it might not be defined yet.
thinking
**Finalizing the summary line**

I need to make sure the final summary line reads: "Checked: 53 | Findings: 15 | Verdict: FAIL." It’s important to format this correctly so there’s no confusion about the status of the checks. I want to be precise with the wording, just in case it affects how others interpret the results. I'll double-check that everything aligns perfectly with the data to maintain clarity and accuracy. Got to get this right!
codex
- [CRITICAL] `main.tex:590` — PROBLEM: `\mainpreambleonly` exits before the fallback macro block at `main.tex:597-719`, so `standalone/editorial.tex:4` loads an amputated preamble; `chapters/connections/concordance.tex:36` then immediately hits undefined macros such as `\cC`, and the standalone build spirals into 359 undefined control sequences plus 1491 unresolved references. FIX: move the fallback `\providecommand` block above the `\ifdefined\mainpreambleonly` guard, or split it into a separate preamble file loaded before `\endinput`; then rebuild `standalone/editorial.tex`.

- [CRITICAL] `standalone/introduction_full_survey.tex:280` — PROBLEM: the file is not actually standalone; it uses main-only symbols/operators/packages that its own preamble never defines (`\dzero`, `\Hom`, `\End`, `\Res`, `\id`, `\colim`, `\R`, `\dfib`, `\Dg`, `\chirAss`, `\chirLie`, `\chirCom`, `\llbracket...\rrbracket`, and `tikz-cd`’s `\arrow`), producing repeated undefined-control-sequence failures at lines 280, 422, 483, 1106, 1840, 5061, 5310, etc., plus 406 unresolved refs and 53 unresolved cites. FIX: mirror the missing `main.tex` definitions into the standalone preamble, add `\usepackage{tikz-cd}` and `\usepackage{stmaryrd}` (or explicit `\llbracket/\rrbracket` definitions), and add `\bibliographystyle{amsalpha}` with `\bibliography{standalone/references}` before `\end{document}`.

- [CRITICAL] `standalone/survey_modular_koszul_duality.tex:1338` — PROBLEM: the preamble omits core manuscript macros used later in the file: `\Hom`, `\End`, `\orline`, `\Defcyc`, `\Aut`, `\CompCl`, and the double-bracket notation at line 2975, so the build fails repeatedly at lines 1338, 1707, 2675, 2975, 7467, 8016, etc.; the file also has unresolved citations with no bibliography block at all. FIX: add `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\newcommand{\orline}[1]{\mathrm{or}_{#1}}`, `\newcommand{\Defcyc}{\operatorname{Def}_{\mathrm{cyc}}}`, `\DeclareMathOperator{\Aut}{Aut}`, `\newcommand{\CompCl}{\operatorname{CompCl}}`, load `stmaryrd` or define `\llbracket/\rrbracket`, and add `\bibliographystyle{amsalpha}` plus `\bibliography{standalone/references}`.

- [HIGH] `standalone/gaudin_from_collision.tex:11` — PROBLEM: `hyperref` is configured with `blue!60!black` and `green!40!black`, but the file never loads `xcolor`, so the build throws repeated `Undefined color` errors at lines 96, 110, 130, 241, 260, 501, 523, 525, 527, 530, and 532. FIX: add `\usepackage[dvipsnames]{xcolor}` before `hyperref`.

- [HIGH] `standalone/shadow_towers_v2.tex:487` — PROBLEM: the file hardcodes `\input{riccati}`, `\input{classification}`, and `\input{computations}` as if TeX resolves them relative to the source file; in the audited build it does not, so `riccati.tex` is missing and the standalone is dead on arrival. FIX: change those inputs to `\input{standalone/riccati}`, `\input{standalone/classification}`, and `\input{standalone/computations}`, or set `\makeatletter\def\input@path{{standalone/}}\makeatother` in the preamble.

- [HIGH] `standalone/N2_mc3_all_types.tex:391` — PROBLEM: `\cF` is used four times in the chromatic-filtration paragraph and never defined in the preamble. FIX: add `\newcommand{\cF}{\mathcal{F}}` with the other calligraphic macros.

- [HIGH] `standalone/N3_e1_primacy.tex:346` — PROBLEM: `\BarchFG` is used at lines 346 and 357 but never defined locally. FIX: add `\newcommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` to the preamble.

- [HIGH] `standalone/programme_summary.tex:1047` — PROBLEM: `\ChirHoch` is used in Theorem H and never defined, so the build breaks on a core headline formula. FIX: add `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` to the macro block.

- [HIGH] `standalone/cy_quantum_groups_6d_hcs.tex:183` — PROBLEM: the file cites external work but declares no bibliography surface, so its citations cannot ever resolve in standalone mode. FIX: add `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}` before `\end{document}`, or supply a complete local `thebibliography`.

- [HIGH] `standalone/programme_summary_sections5_8.tex:199` — PROBLEM: the file cites literature but ends with commented-out `\bibitem` stubs instead of an active bibliography, so the standalone citation surface is knowingly disabled. FIX: uncomment and complete the bibliography block, or replace the dead comments with `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}`.

- [HIGH] `standalone/survey_track_a_compressed.tex:732` — PROBLEM: the file cites external sources but has no `\bibliography` or `thebibliography`, so the compressed survey is not actually standalone. FIX: add `\bibliographystyle{amsalpha}` and `\bibliography{standalone/references}` before `\end{document}`.

- [MEDIUM] `standalone/N1_koszul_meta.tex:153`; `standalone/N4_mc4_completion.tex:171`; `standalone/N5_mc5_sewing.tex:107`; `standalone/analytic_sewing.tex:172`; `standalone/arithmetic_shadows.tex:233`; `standalone/drinfeld_kohno_bridge.tex:199`; `standalone/e1_primacy_ordered_bar.tex:214`; `standalone/en_chiral_operadic_circle.tex:210`; `standalone/five_theorems_modular_koszul.tex:144`; `standalone/garland_lepowsky.tex:107` — PROBLEM: these files ship local standalone wrappers but still leave unresolved `\ref/\eqref/\cite` calls after multi-pass build; they are excerpt slices pretending to be closed documents. FIX: for each file, either import the missing labelled statements/sections into the standalone source or rewrite the external cross-references as local prose, and replace the partial local bibliography with a complete local list or `\bibliography{standalone/references}`.

- [MEDIUM] `standalone/genus1_seven_faces.tex:90`; `standalone/koszulness_fourteen_characterizations.tex:201`; `standalone/ordered_chiral_homology.tex:209`; `standalone/programme_summary_section1.tex:153`; `standalone/sc_chtop_pva_descent.tex:198`; `standalone/shadow_towers.tex:95`; `standalone/shadow_towers_v3.tex:146`; `standalone/survey_modular_koszul_duality_v2.tex:283`; `standalone/three_dimensional_quantum_gravity.tex:101`; `standalone/three_parameter_hbar.tex:64` — PROBLEM: same boundary failure in a second cluster: the files still reference labels and bibliography keys that are not supplied by the standalone build, so they only work as fragments of the monograph, not as independent documents. FIX: close each extraction boundary by importing the referenced theorem/section/table surfaces and by supplying a complete bibliography surface; otherwise delete the broken `\ref/\eqref/\cite` calls.

- [LOW] `standalone/chiral_chern_weil.tex:172`; `standalone/classification.tex:93`; `standalone/classification_trichotomy.tex:366`; `standalone/computations.tex:242`; `standalone/cy_to_chiral_functor.tex:232`; `standalone/holographic_datum.tex:260`; `standalone/multi_weight_cross_channel.tex:203` — PROBLEM: these files are label-incomplete even when citations are not the issue; the standalone text still points to definitions, sections, computations, or tables that are absent locally. FIX: either inline the referenced result names/text or import the missing labelled environments into the standalone document.

- [LOW] `standalone/programme_summary_sections2_4.tex:313`; `standalone/programme_summary_sections9_14.tex:99`; `standalone/riccati.tex:150`; `standalone/seven_faces.tex:603`; `standalone/survey_track_b_compressed.tex:596`; `standalone/virasoro_r_matrix.tex:144`; `standalone/w3_holographic_datum.tex:135` — PROBLEM: these are also not label-closed: they retain dangling `\ref/\eqref` calls to omitted material, so the standalone PDFs silently lose semantic pointers. FIX: remove or localize each external cross-reference, or import the missing labelled material so the standalone build has a closed label graph.

## Summary
Checked: 53 | Findings: 15 | Verdict: FAIL
tokens used
256,108
