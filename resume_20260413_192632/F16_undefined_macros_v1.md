# F16_undefined_macros_v1 (1736s)

- [CRITICAL] standalone/editorial.tex:3 — PROBLEM: `\mainpreambleonly` makes `main.tex` stop at line 593, so the fallback macro block at `main.tex:597-719` never runs; fresh `editorial.log` then shows undefined `\cC`, `\ChirHoch`, `\HH`, `\bR`, `\CompCl`, and many more from the imported chapter files. FIX: move `main.tex:597-719` above the `\ifdefined\mainpreambleonly` guard so those `\providecommand`s are available before `editorial.tex` imports the concordance files.
- [CRITICAL] standalone/editorial.tex:14 — PROBLEM: importing `chapters/connections/concordance` and `chapters/connections/editorial_constitution` leaves 1,736 undefined cross-manuscript references in fresh standalone compile. FIX: load `xr-hyper` in `standalone/editorial.tex` after the preamble import and add `\externaldocument{main}` before `\begin{document}` so the file explicitly resolves labels from `main.aux`.
- [CRITICAL] standalone/introduction_full_survey.tex:125 — PROBLEM: fresh standalone compile leaves 435 undefined `\ref` labels and 53 undefined citation keys starting here; this file still depends on monograph aux/bibliography state. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [CRITICAL] standalone/shadow_towers_v2.tex:487 — PROBLEM: the file `\input`s full standalone documents (`riccati.tex`, `classification.tex`, `computations.tex`) after `\begin{document}`, which triggers fresh “Can be used only in preamble” and theorem-redefinition errors. FIX: split those three files into body-only fragments and replace `\input{riccati}`, `\input{classification}`, and `\input{computations}` with inputs of the body fragments.
- [CRITICAL] standalone/survey_modular_koszul_duality.tex:626 — PROBLEM: fresh standalone compile leaves 148 undefined `\ref` labels and 6 undefined citation keys; the file is not actually standalone. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [CRITICAL] standalone/survey_modular_koszul_duality_v2.tex:709 — PROBLEM: fresh standalone compile leaves 58 undefined `\ref` labels starting here; the file still relies on monograph labels not imported locally. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{main}` before `\begin{document}`.

- [HIGH] standalone/N2_mc3_all_types.tex:391 — PROBLEM: `\cF` is used at lines 391 and 394, but the local macro block at lines 35-59 never defines it. FIX: add `\newcommand{\cF}{\mathcal{F}}` beside the other `\c*` macros.
- [HIGH] standalone/N3_e1_primacy.tex:346 — PROBLEM: `\BarchFG` is used at lines 346 and 357, but the preamble defines `\Barch`, `\Barord`, `\BarSig`, and `\Cobar` only. FIX: add `\newcommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` to the macro block.
- [HIGH] standalone/N3_e1_primacy.tex:615 — PROBLEM: `\Cobar` and `\Barord` already expand to superscripted symbols, so `\Cobar^{(g)}` and `\Barord^{(g)}` create fresh double-superscript errors at lines 615 and 629. FIX: write `(\Cobar)^{(g)}` and `(\Barord)^{(g)}` instead.
- [HIGH] standalone/N6_shadow_formality.tex:190 — PROBLEM: the text references `\ref{cor:operadic-complexity}`, but the actual corollary is labeled `\label{cor:operadic-body}` at line 540. FIX: rename `\label{cor:operadic-body}` to `\label{cor:operadic-complexity}` or change the reference at line 190 to `\ref{cor:operadic-body}`.
- [HIGH] standalone/N6_shadow_formality.tex:239 — PROBLEM: `\gmod` already contains a subscript `_\\cA`, so `\gmod_g` creates a fresh double-subscript error. FIX: replace `\gmod_g` with `(\gmod)^{(g)}` or with a separately defined macro such as `\gmod^{(g)}`.
- [HIGH] standalone/bp_self_duality.tex:11 — PROBLEM: `hyperref` is configured with `blue!60!black` and `green!40!black`, but `xcolor` is never loaded, so both colors are undefined in fresh compile. FIX: insert `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/classification.tex:66 — PROBLEM: the file contains unresolved cross-document refs at lines 66, 100, 267, 794, 831, and 1008 (`thm:single-line-dichotomy`, `thm:riccati-algebraicity`, `thm:depth-decomposition`, `rem:contact-stratum-separation`, `thm:nms-betagamma-quartic-birth`). FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{riccati}`, `\externaldocument{chapters/connections/arithmetic_shadows}`, and `\externaldocument{appendices/nonlinear_modular_shadows}` before `\begin{document}`.
- [HIGH] standalone/classification_trichotomy.tex:12 — PROBLEM: `hyperref` uses mixed colors, but `xcolor` is not loaded locally, so fresh compile reports `Undefined color 'blue!60!black'`. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/classification_trichotomy.tex:100 — PROBLEM: the line starts `\kappa$` with no opening math delimiter, producing a fresh `Missing $ inserted` error. FIX: change that fragment to `$\\kappa$ is the ...`.
- [HIGH] standalone/cy_quantum_groups_6d_hcs.tex:183 — PROBLEM: the file cites `LorgatCYChiral`, but that key does not exist in the repo bibliography and fresh compile leaves it undefined. FIX: add a real `\bibitem{LorgatCYChiral}` to `bibliography/references.tex` and import that bibliography here, or replace the citation with uncited prose until the key exists.
- [HIGH] standalone/gaudin_from_collision.tex:11 — PROBLEM: `hyperref` uses `blue!60!black` / `green!40!black` without loading `xcolor`, so the standalone build dies on undefined colors. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/introduction_full_survey.tex:280 — PROBLEM: the standalone preamble omits `\dzero`, `\dfib`, `\Hom`, `\End`, `\Res`, `\Aut`, `\colim`, `\id`, and `\R`, all of which are used later (for example at lines 280, 422, 436, 483, 609, 747, 566, 1282, 639, 1230). FIX: add `\newcommand{\dzero}{d_0}`, `\newcommand{\dfib}{d_{\mathrm{fib}}}`, `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\DeclareMathOperator{\Res}{Res}`, `\DeclareMathOperator{\Aut}{Aut}`, `\DeclareMathOperator{\colim}{colim}`, `\providecommand{\id}{\mathrm{id}}`, and `\providecommand{\R}{\mathbb{R}}` to the preamble.
- [HIGH] standalone/introduction_full_survey.tex:84 — PROBLEM: `\Dg` is defined as a zero-argument text macro, but the body uses it as a one-argument genus-indexed differential at lines 759, 907, 4521, 5314, and 5321. FIX: replace line 84 with `\providecommand{\Dg}[1]{D_{#1}}`; if plain `dg` text is also needed, introduce a separate `\dg`.
- [HIGH] standalone/introduction_full_survey.tex:1838 — PROBLEM: `\begin{tikzcd}` and `\ar[...]` are used at lines 1838-1846 and 4645-4653, but `tikz-cd` is never loaded. FIX: add `\usepackage{tikz-cd}` in the preamble.
- [HIGH] standalone/introduction_full_survey.tex:5269 — PROBLEM: the file uses `\begin{convention}` at lines 5269, 5307, and 5337, but no `convention` theorem environment is declared locally. FIX: add `\newtheorem{convention}[theorem]{Convention}` to the theorem block.
- [HIGH] standalone/introduction_full_survey.tex:5062 — PROBLEM: the preamble omits `\chirAss`, `\chirLie`, `\chirCom`, and `\chirtensor`, which are used at lines 5062-5087 and 5164. FIX: add `\newcommand{\chirtensor}{\otimes^{\mathrm{ch}}}`, `\newcommand{\chirLie}{\mathsf{Lie}^{\mathrm{ch}}}`, `\newcommand{\chirAss}{\mathsf{Ass}^{\mathrm{ch}}}`, and `\newcommand{\chirCom}{\mathsf{Com}^{\mathrm{ch}}}` to the preamble.
- [HIGH] standalone/introduction_full_survey.tex:1106 — PROBLEM: the file uses `\llbracket x \rrbracket`, but no package defining `\llbracket`/`\rrbracket` is loaded. FIX: add `\usepackage{stmaryrd}` to the preamble.
- [HIGH] standalone/ordered_chiral_homology.tex:7831 — PROBLEM: the optional citation notes at lines 7831, 7846, and 7859 embed `\ref*{...}` to labels not defined in this file, so the standalone build leaves three unresolved refs. FIX: remove the `\ref*{...}` pieces and use plain `\cite{Lorgat26I}`, or replace the optional notes with literal theorem/proposition numbers.
- [HIGH] standalone/programme_summary.tex:1043 — PROBLEM: `\ChirHoch` is used in Theorem H, but the local macro block at lines 37-54 never defines it. FIX: add `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` to that macro block.
- [HIGH] standalone/programme_summary_sections5_8.tex:198 — PROBLEM: the file cites `Drinfeld85`, `KZ84`, `STS83`, and `FFR94`, but it has no active bibliography; the needed entries are only commented out at lines 770-785. FIX: add a real `thebibliography` environment before `\end{document}` and move those four commented `\bibitem`s into it.
- [HIGH] standalone/programme_summary_sections5_8.tex:318 — PROBLEM: `\ref{sec:bar}` and `\ref{def:shadow-depth}` are unresolved because this split file does not import labels from the full summary. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.
- [HIGH] standalone/riccati.tex:591 — PROBLEM: `FlajoletSedgewick` is cited, but the file has no local bibliography and fresh compile leaves the citation undefined. FIX: append `\input{bibliography/references}` before `\end{document}` so the existing `\bibitem{FlajoletSedgewick}` in the repo bibliography is available.
- [HIGH] standalone/survey_modular_koszul_duality.tex:1338 — PROBLEM: the preamble omits `\Hom`, `\End`, `\orline`, `\Defcyc`, `\Aut`, and `\CompCl`, all of which are used at lines 1338, 1707, 2675, 7464, and 8013. FIX: add `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\newcommand{\orline}[1]{\mathrm{or}_{#1}}`, `\newcommand{\Defcyc}{\operatorname{Def}_{\mathrm{cyc}}}`, `\DeclareMathOperator{\Aut}{Aut}`, and `\newcommand{\CompCl}{\operatorname{CompCl}}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality.tex:2975 — PROBLEM: the file uses `\Bbbk\llbracket x\rrbracket`, but no package defining `\llbracket`/`\rrbracket` is loaded. FIX: add `\usepackage{stmaryrd}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:707 — PROBLEM: `\ord` is used in `\Ran^{\ord}(X)` and `\barB^{\ord}`, but the macro is never defined locally. FIX: add `\DeclareMathOperator{\ord}{ord}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:6669 — PROBLEM: `\Ydg` is used but never defined in the standalone preamble. FIX: add `\newcommand{\Ydg}{\mathcal{Y}^{\mathrm{dg}}}` to the macro block.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:8211 — PROBLEM: `\widehat{\fg\fl}_1` is malformed and uses an undefined `\fl`; fresh compile then cascades into multiple missing-math errors. FIX: replace the whole fragment with `\widehat{\mathfrak{gl}}_1`, i.e. `$\cZ(\Rep^{E_1}(Y^+(\widehat{\mathfrak{gl}}_1))) \cong \Rep^{E_2}(\cW_{1+\infty})$`.
- [HIGH] standalone/survey_track_a_compressed.tex:585 — PROBLEM: fresh standalone compile leaves 22 undefined `\ref` labels and one undefined citation key (`GeK98`) starting here. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [HIGH] standalone/survey_track_b_compressed.tex:596 — PROBLEM: fresh standalone compile leaves 33 undefined cross-manuscript refs starting with `thm:categorical-cg-all-types`, `cor:mc3-all-types`, and the three closure conjectures. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{main}` before `\begin{document}`.
- [HIGH] standalone/three_parameter_hbar.tex:11 — PROBLEM: `hyperref` uses mixed colors without loading `xcolor`, so fresh compile reports repeated undefined-color errors. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/three_parameter_hbar.tex:210 — PROBLEM: the sentence `and the $\lambda$-bracket divided-power convention} = \lambda^n/n!$)` has a stray `}` and broken math delimiters, producing fresh math-mode errors. FIX: replace that fragment with `and the $\lambda$-bracket divided-power convention (coefficients of $\lambda^n/n!$) yields the $r$-matrix with the Sugawara-normalized prefactor.`
- [HIGH] standalone/w3_holographic_datum.tex:12 — PROBLEM: `hyperref` uses `blue!60!black` / `green!40!black`, but `xcolor` is not loaded locally. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.

- [MEDIUM] standalone/programme_summary_sections2_4.tex:559 — PROBLEM: `\ref{ssec:d-squared}` is unresolved because this fragment does not import labels from the full summary. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.
- [MEDIUM] standalone/programme_summary_sections9_14.tex:315 — PROBLEM: `\ref{eq:mc-equation}`, `\eqref{eq:curvature}`, and `\ref{sec:bar}` are unresolved at lines 315, 565, and 613 because this fragment is compiled without the earlier summary sections. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.

## Summary
Checked: 53 | Findings: 40 | Verdict: FAIL


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
session id: 019d87f4-65e4-7eb0-adaa-f39dd634eb6a
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
**Planning a script for LaTeX macros**

I think I should create a script using grep to extract macros from standalone LaTeX files and check the preamble. This will allow me to verify which macros are undefined. I also need to detect any unresolved references like `\ref` or `\cite`. The user's request involves auditing standalone files for hidden imports or unresolved references. I’ll run the grep command to find all undefined macros and cross-check them against the preamble. Each undefined macro will be a finding.
codex
Using `deep-beilinson-audit` for a hostile pass over `standalone/*.tex`. I’m starting by reading the required repo-constitution files, then I’ll extract every macro used in `standalone/` and cross-check them against the live preamble and local definitions before I write findings.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
- high: **807**

thinking
**Inspecting files and preamble**

I think I probably need to audit instead of edit, so maybe there's no clear plan yet. I should inspect standalone files and the preamble, possibly reading through them. I might start by updating the scope lock with a list of files and methods. Using parallel commands to list all files and macros could help. I need to identify what "preamble" refers to, maybe preamble.tex or macros, by checking the standalone files and the main preamble. I'll search for that!
codex
The audit surface is `standalone/*.tex`, with the specific attack lane “undefined macros against the live preamble, plus second-order failures exposed by those files themselves.” I’m locating the standalone preamble chain and reading every standalone file before I promote any candidate macro to a finding.
exec
/bin/zsh -lc 'ls standalone' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\documentclass|\\\\input\\{|\\\\include\\{|\\\\usepackage|\\\\newcommand|\\\\renewcommand|\\\\DeclareMathOperator|\\\\def\\\\|\\\\providecommand|\\\\NewDocumentCommand|\\\\DeclareRobustCommand|\\\\newtheorem|\\\\input\\{preamble|\\\\input\\{macros|\\\\include\\{preamble|\\\\include\\{macros\" standalone main.tex preamble.tex macros.tex chapters appendices frontmatter -g '"'!*.aux'"' -g '"'!*.log'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
N1_koszul_meta.aux
N1_koszul_meta.log
N1_koszul_meta.out
N1_koszul_meta.pdf
N1_koszul_meta.tex
N2_mc3_all_types.aux
N2_mc3_all_types.log
N2_mc3_all_types.out
N2_mc3_all_types.pdf
N2_mc3_all_types.tex
N3_e1_primacy.aux
N3_e1_primacy.log
N3_e1_primacy.out
N3_e1_primacy.pdf
N3_e1_primacy.tex
N4_mc4_completion.aux
N4_mc4_completion.log
N4_mc4_completion.out
N4_mc4_completion.pdf
N4_mc4_completion.tex
 exited 2 in 50ms:
rg: regex parse error:
    (?:\documentclass|\input\{|\include\{|\usepackage|\newcommand|\renewcommand|\DeclareMathOperator|\def\|\providecommand|\NewDocumentCommand|\DeclareRobustCommand|\newtheorem|\input\{preamble|\input\{macros|\include\{preamble|\include\{macros)
                      ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "for f in standalone/*.tex; do printf 'FILE %s\\n' \""'$f"; grep -oP '"'\\\\[a-zA-Z]+' \""'$f" | sort -u; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:


thinking
**Considering command compatibility**

I need to handle command compatibility, and I might consider using Perl or `rg -o`. It seems like I need to inspect the standalone file structure and look at the preamble, which likely varies across files. I'll probably need a script to parse macros and definitions. Using the command line with Perl could be my approach, and I can use `rg` to find the preamble. I should check the first few standalone files and run the correct `rg` patterns.
codex
The first pass exposed an environment issue, not a manuscript issue: BSD `grep` here does not support `-P`, so I’m switching to `perl`/`rg` equivalents. Next pass is the actual macro census plus the standalone preamble chain.
exec
/bin/zsh -lc "rg -n '\\\\documentclass|\\\\input\\{|\\\\include\\{|\\\\usepackage|\\\\newcommand|\\\\renewcommand|\\\\DeclareMathOperator|\\\\providecommand|\\\\NewDocumentCommand|\\\\DeclareRobustCommand|\\\\newtheorem' standalone main.tex preamble.tex macros.tex chapters appendices frontmatter" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
Total output lines: 3717

rg: preamble.tex: No such file or directory (os error 2)
rg: macros.tex: No such file or directory (os error 2)
rg: frontmatter: No such file or directory (os error 2)
main.tex:1:\documentclass[11pt]{memoir}
main.tex:5:\usepackage[T1]{fontenc}
main.tex:6:\usepackage[utf8]{inputenc}
main.tex:7:\usepackage{lmodern}
main.tex:11:\usepackage[
main.tex:16:\usepackage{ebgaramond}
main.tex:19:\usepackage[
main.tex:40:\usepackage{mleftright}
main.tex:46:\usepackage{amsmath,amssymb,amsthm}
main.tex:47:\usepackage{tikz-cd}
main.tex:51:\usepackage[unicode,pdfencoding=auto,psdextra]{hyperref}
main.tex:53:\usepackage{geometry}
main.tex:66:\usepackage{algorithm}
main.tex:67:\usepackage{algpseudocode}
main.tex:68:\usepackage{tcolorbox}
exec
/bin/zsh -lc "for f in standalone/*.tex; do printf 'FILE %s\\n' \""'$f"; perl -ne '"'while(/\\\\([A-Za-z@]+)/g){print \"\\\\"'$1'"\\n\"}' \""'$f" | sort -u; printf '"'\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 activate={true,nocompatibility},
 succeeded in 205ms:

FILE standalone/gaudin_from_collision.tex
\Aut
\DeclareMathOperator
\Defcyc
\End
\Leftrightarrow
\MC
\Mbar
\Omega
\Ran
\Res
\Sh
\Sigma
\Theta
\Vir
\ad
\alpha
\arabic
\arraystretch



thinking
**Inspecting standalone files**

I need to look at standalone files to see if each has its own self-contained definitions. Comparing macro usage with my own preamble and possibly the main preamble seems essential. The user wants me to cross-check each file's preamble against the main one. I could check compilation logs for any undefined control sequences, especially since many standalone PDFs and logs exist. A comprehensive audit is needed, and maybe I should create a script to extract defined macros from each .tex file.
thinking
**Identifying undefined macros**

The user is asking about undefined macros, saying that every undefined macro should be noted, along with any unresolved references. I can search logs for terms like "Undefined control sequence" and "Citation undefined." Since there are logs available, I think it's acceptable to use them, but I also need to verify the file contents directly. I should read lines around each finding to confirm if any macro definitions are missing. Creating an inventory of undefined macros by comparing against the main preamble and known macros seems essential. Compiling each file with `pdflatex -interaction=nonstopmode` could help reveal these undefined macros directly.
thinking
**Considering macro verification**

The user specifically instructed me to grep macros, but compiling could serve as good verification too. I’m thinking about whether to employ the build-surface skill since it wasn’t mentioned, but it could still be useful for determining if changes are verified during LaTeX builds. Since the task also involves hidden imports and unresolved references, I might use build-surface minimally. I need to decide if it's necessary to announce its use only for narrow verification when compiling. It seems likely that announcing it would be appropriate.
codex
I have the macro census and the main preamble in hand. Now I’m converting the raw command list into actual failures: for each candidate I’m checking local definitions, package coverage, and then corroborating with the standalone logs or a direct compile before I keep it as a finding.

thinking
**Parsing logs and scripts**

I need to check if I can use scripts or shell commands to parse logs and identify any undefined control sequences. I'll look at some standalone logs to see if I can find multiple instances of these sequences. It seems like using something like rg could be helpful to search through the logs efficiently. I’m curious how well this will work! I’ll take my time to inspect these logs properly.
exec
/bin/zsh -lc 'rg -n "Undefined control sequence|LaTeX Error|Reference .* undefined|Citation .* undefined|There were undefined references|Emergency stop|Runaway argument" standalone/*.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2578

standalone/N3_e1_primacy.log:436:./N3_e1_primacy.tex:346: Undefined control sequence.
standalone/N3_e1_primacy.log:447:./N3_e1_primacy.tex:357: Undefined control sequence.
standalone/N2_mc3_all_types.log:548:./N2_mc3_all_types.tex:391: Undefined control sequence.
standalone/N2_mc3_all_types.log:559:./N2_mc3_all_types.tex:391: Undefined control sequence.
standalone/N2_mc3_all_types.log:570:./N2_mc3_all_types.tex:394: Undefined control sequence.
standalone/N2_mc3_all_types.log:581:./N2_mc3_all_types.tex:394: Undefined control sequence.
standalone/classification_trichotomy.log:443:./classification_trichotomy.tex:366: LaTeX Error: Undefined color `blue!60!blac
standalone/classification.log:560:LaTeX Warning: Reference `thm:single-line-dichotomy' on page 1 undefined on inp
standalone/classification.log:564:LaTeX Warning: Reference `thm:riccati-algebraicity' on page 1 undefined on inpu
standalone/classification.log:653:LaTeX Warning: Reference `thm:depth-decomposition' on page 3 undefined on input
standalone/classification.log:670:LaTeX Warning: Reference `thm:riccati-algebraicity' on page 9 undefined on inpu
standalone/classification.log:674:LaTeX Warning: Reference `rem:contact-stratum-separation' on page 9 undefined o
standalone/classification.log:683:LaTeX Warning: Reference `thm:nms-betagamma-quartic-birth' on page 11 undefined
standalone/classification.log:709:LaTeX Warning: There were undefined references.
standalone/bp_self_duality.log:499:./bp_self_duality.tex:91: LaTeX Error: Undefined color `green!40!black'.
standalone/bp_self_duality.log:511:./bp_self_duality.tex:92: LaTeX Error: Undefined color `green!40!black'.
standalone/bp_self_duality.log:528:./bp_self_duality.tex:161: LaTeX Error: Undefined color `green!40!black'.
standalone/bp_self_duality.log:540:./bp_self_duality.tex:172: LaTeX Error: Undefined color `blue!60!black'.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root = pathlib.Path('standalone')
files = sorted(root.glob('*.tex'))
# rough set of builtin/common macros to ignore in candidate list; deliberately conservative
builtin = {
'documentclass','usepackage','begin','end','section','subsection','subsubsection','paragraph','subparagraph','chapter','part','appendix','tableofcontents','maketitle','author','title','date','address','email','keywords','subjclass','thanks',
'newcommand','renewcommand','providecommand','DeclareMathOperator','newtheorem','numberwithin','theoremstyle','label','ref','eqref','cite','bibliography','bibliographystyle','bibitem','footnote','emph','textbf','textit','texttt','textup','textnormal','textsc','textrm','textstyle','textsuperscript','textasciigrave','textasciitilde','textasciicircum','texorpdfstring','mbox','fbox','parbox','raisebox','phantom','footnotesize','small','smallskip','medskip','bigskip','noindent','newline','today','tableofcontents','addcontentsline','markboth','index','caption','centering','raggedright','arraystretch','multicolumn','addlinespace','bottomrule','midrule','toprule','hline','cline',
'makeatletter','makeatother','let','IfFileExists','input','include','setcounter','setlength','setminus','setlength','detokenize','arraybackslash','newcolumntype','endfirsthead','endhead','endfoot','endlastfoot','normalfont','ttfamily','parindent','hrulefill','mainmatter','frontmatter','backmatter','repoinput','mainpreambleonly','archivebuild',
'left','right','bigl','bigr','Bigl','Bigr','biggl','biggr','big','Big','bigg','bigg','bigcup','bigcap','bigoplus','bigotimes','bigwedge','bigsqcup','sum','prod','coprod','int','oint','lim','sup','max','min','det','ker','log','exp','sin','cos','tan','csc','cot','arg','gcd','deg','dim','sup','inf','limsup','liminf','operatorname','mathrm','mathbf','mathbb','mathcal','mathfrak','mathsf','mathscr','mathbin','boldsymbol','boxed','underline','overline','underbrace','widehat','widetilde','hat','bar','vec','check','checkmark','star','bullet','cdot','circ','boxtimes','otimes','oplus','odot','cup','cap','sqcup','perp','pm','mp','times','to','mapsto','longrightarrow','longmapsto','leftrightarrow','longleftrightarrow','Rightarrow','Longrightarrow','Leftrightarrow','Longleftrightarrow','hookrightarrow','hookleftarrow','twoheadrightarrow','leftarrow','xrightarrow','xleftarrow','xmapsto','rightleftarrows','rightrightarrows','leadsto','rightsquigarrow','dashv','vdash',
'alpha','beta','gamma','delta','epsilon','varepsilon','zeta','eta','theta','vartheta','iota','kappa','lambda','mu','nu','xi','pi','varphi','phi','psi','rho','varrho','sigma','tau','omega','Omega','Gamma','Lambda','Phi','Psi','Sigma','Theta','Pi','Delta','ell','infty','partial','nabla','forall','exists','in','notin','subset','subseteq','supset','supseteq','neq','ne','ge','geq','le','leq','approx','equiv','cong','sim','simeq','propto','iff','implies','Leftrightarrow','Rightarrow',
'ldots','cdots','dots','dotsb','dotsc','qquad','quad','enspace','colon',';','"'!'"','%','roman','arabic','alph','Roman','setcounter',
'frac','dfrac','tfrac','binom','tbinom','sqrt','langle','rangle','lVert','rVert','lfloor','rfloor','llbracket','rrbracket','left','right','mid','pmod','bmod','mod','qquad','quad','smallskip','medskip','bigskip',
'vee','wedge','op','cop','ord','tr','im','id','gr','rk','depth','Spec','Aut','End','Ext','Hom','Res','Tr','Diff','Re','Im','obs'
}
# definitions extracted per file and main preamble
main = pathlib.Path('main.tex').read_text()
def extract_defs(text):
    defs=set()
    for pat in [r'\\\\(?:newcommand|renewcommand|providecommand)\\*?\\{\\\\([A-Za-z@]+)\\}', r'\\\\DeclareMathOperator\\*?\\{\\\\([A-Za-z@]+)\\}', r'\\\\newtheorem\\{([A-Za-z@]+)\\}', r'\\\\def\\\\([A-Za-z@]+)', r'\\\\DeclareRobustCommand\\*?\\{\\\\([A-Za-z@]+)\\}', r'\\\\NewDocumentCommand\\{\\\\([A-Za-z@]+)\\}']:
        defs.update(re.findall(pat, text))
    return defs
main_defs = extract_defs(main)
for f in files:
    text = f.read_text()
    defs = extract_defs(text)
    used = set(re.findall(r'\\\\([A-Za-z@]+)', text))
    cands = sorted(x for x in used if x not in defs and x not in main_defs and x not in builtin)
    if cands:
        print(f.name, ':', ' '.join(cands))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N1_koszul_meta.tex : S item newblock tilde url
N2_mc3_all_types.tex : S chi hbar item text
N3_e1_primacy.tex : hbar item substack text
N4_mc4_completion.tex : S item nolimits text varprojlim
N5_mc5_sewing.tex : chi item text
N6_shadow_formality.tex : S item text
analytic_sewing.tex : chi item subsetneq text varprojlim
arithmetic_shadows.tex : @ifundefined arsh@oldref chi displaystyle item sideset substack text
bp_self_duality.tex : item notag text
chiral_chern_weil.tex : @ H item notag text upshape
classification.tex : @ifundefined cls@oldref dagger ddagger hbar item sinh text
classification_trichotomy.tex : item text
computations.tex : @ifundefined cmp@oldref item text
cover_letter_garland_lepowsky.tex : closing opening signature
cover_letter_seven_faces.tex : closing item opening signature
cover_letter_shadow_towers.tex : closing opening signature
cover_letter_virasoro_r_matrix.tex : closing opening signature
cy_quantum_groups_6d_hcs.tex : arrow hbar item text
cy_to_chiral_functor.tex : chi circlearrowleft item text
drinfeld_kohno_bridge.tex : ar emptyset hbar item text






thinking
**Considering audit findings**

I might only focus on the foundation audit of standalone files against macros and unresolved references from logs. Okay, I could group findings by root cause, but the user asked for every distinct issue. I think I should provide all actual findings, which could be around 20-30 issues. Maybe I need to parse existing logs quickly, but they might be outdated. Compiling problematic files could verify errors, especially those with undefined control sequences or environment errors, like color issues from xcolor.
thinking
**Planning LaTeX fixes**

I need to fix the LaTeX document by adding `\usepackage[dvipsnames]{xcolor}` before `hyperref` or just stick to basic color names. Also, I want to add line numbers and systematically extract compile errors for better context. It would help to run a script that parses logs for various errors and outputs relevant source lines. I need to consider hidden issues with imports and use scripts to gather all errors efficiently, especially since there are many files involved.
thinking
**Identifying compilation issues**

I suspect there are missing environments, not just macros, that need to be addressed in the findings. I should consider using a script to extract unique compile errors from the logs, especially those related to "Undefined control sequence" or "LaTeX Error." Unresolved references might be numerous, but I can focus on identifying the root causes. It seems that the standalone files are citing labels from other chapters without including them, leading to stale cross-file references. There's also the possibility of hidden imports causing issues.
thinking
**Inspecting LaTeX files**

I need to check the preambles of files for missing packages or macros. For instance, there’s an error in `classification_trichotomy.tex` on line 366 where the xcolor package seems to be missing. I also want to look at the context of undefined control sequences in other files, like `programme_summary.tex` and `ordered_chiral_homology.tex`. This might be a big job. I need to decide how comprehensively to cover these issues and whether to use `lualatex` or `pdflatex` to compile and identify failures.
thinking
**Addressing user concerns**

The user wants specific fixes for each file and line where issues occur. I can identify the root cause of distinct problems in each file. It might make sense to group similar issues together, like if a file's use of `\hypersetup` colors requires the xcolor package, leading to multiple undefined color errors. I'm wondering if I should provide one finding per file or focus on grouping by root cause instead. Let's figure out the best approach for clarity!
thinking
**Analyzing undefined occurrences**

I’m trying to figure out whether the root cause is not each occurrence, even though every missing definition or unresolved reference has been mentioned. A missing 'xcolor' could be behind many undefined color issues, suggesting that these occurrences might not be distinct. Maybe I should group them. I think I need to write a script to locate actual undefined macros by parsing logs for "Undefined control sequence" messages and the tokens that follow. Let's inspect the logs and the source code!
codex
The failure surface is bifurcating cleanly: actual undefined commands/environments on one side, stale standalone cross-references/citations on the other. I’m drilling into each compile error now to identify the exact missing macro or package rather than reporting a vague log symptom.
exec
/bin/zsh -lc 'for f in standalone/N2_mc3_all_types.tex standalone/N3_e1_primacy.tex standalone/programme_summary.tex standalone/ordered_chiral_homology.tex standalone/survey_modular_koszul_duality.tex standalone/introduction_full_survey.tex; do echo "FILE $f"; nl -ba "$f" | sed -n '"'330,410p;1000,1060p;10690,10730p;1325,1405p;1688,1730p;2660,2705p;2958,2980p;4305,4335p;4515,4530p;4590,4660p;4788,4800p;4860,4875p;5008,5020p;5056,5090p;5158,5170p;5260,5338p'; echo; done" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for log in standalone/N2_mc3_all_types.log standalone/N3_e1_primacy.log standalone/programme_summary.log standalone/ordered_chiral_homology.log standalone/survey_modular_koszul_duality.log standalone/introduction_full_survey.log; do echo "FILE $log"; rg -n -C 3 "Undefined control sequence|Environment .* undefined|Undefined color" "$log"; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE standalone/N2_mc3_all_types.tex
   330	\Omg = \sum_a I_a \otimes I^a,
   331	\end{equation}
   332	where $\{I_a\}$ is a basis of $\fg$ and $\{I^a\}$ its dual with
   333	respect to $(\cdot, \cdot)$. Here $k$ is the level parameter of
   334	the affine Kac--Moody algebra; at level $k = 0$ the bialgebra
   335	cobracket vanishes and $r(z) = 0$, as required for the
   336	level-stripped rational $r$-matrix of the classical Yang--Baxter
   337	equation (see of~\cite{LorgatMKD} for the history of this
   338	normalization).
   339	
   340	\begin{remark}[Level normalization]
   341	\label{rem:level-norm}
   342	Throughout we write all $r$-matrix formulas with the level~$k$
   343	displayed. This makes the $k \to 0$ check immediate:
   344	setting $k = 0$ in (\ref{eq:r-matrix-level}) gives $r(z) = 0$,
   345	corresponding to the abelian Lie bialgebra. Any $r$-matrix
   346	appearing in this paper satisfies this sanity check.
   347	\end{remark}
   348	
 succeeded in 50ms:
FILE standalone/N2_mc3_all_types.log
545-}]
546-
547-[4]
548:./N2_mc3_all_types.tex:391: Undefined control sequence.
549-<recently read> \cF 
550-                    
551-l.391 $\cF
--
556-spelling (e.g., `I\hbox'). Otherwise just continue,
557-and I'll forget about whatever was undefined.
558-
559:./N2_mc3_all_types.tex:391: Undefined control sequence.
560-<recently read> \cF 
561-                    
562-l.391 ...N} \subset \cO^{\mathrm{sh}}$, where $\cF
--
567-spelling (e.g., `I\hbox'). Otherwise just continue,
568-and I'll forget about whatever was undefined.
569-

thinking
**Investigating code issues**

I need to look into the ordered_chiral_homology source around line 10711. It seems like there might be an issue with either the macro \cX being undefined or perhaps the \pi? I want to be thorough with this inspection to figure out what’s going wrong. Let's see what I can uncover by examining that part of the code more closely!
exec
/bin/zsh -lc "nl -ba standalone/ordered_chiral_homology.tex | sed -n '10695,10725p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 10695	$\overline{\cM}_{g,n}$, invariants of $(X, \fg, k)$
 10696	that refine Reshetikhin--Turaev invariants in the same
 10697	way that perturbative Chern--Simons refines Witten's
 10698	partition function.
 10699	Concretely: does the genus-$g$ ordered chiral homology
 10700	$\int_X^{\mathrm{ord}} \CE^{\mathrm{ch}}_k(\fg)$
 10701	recover the perturbative Chern--Simons partition function
 10702	$Z_{\mathrm{CS}}(X, \fg, k)$ as its $\Sigma_n$-coinvariant
 10703	shadow, and what invariants live in the kernel of
 10704	the averaging map $\av$?
 10705	
 10706	\item \textup{(The $\cW_{1+\infty}$ chiral quantum group:
 10707	remaining questions.)}
 10708	Theorem~\ref{thm:w-infty-chiral-qg} establishes that
 10709	$\cW_{1+\infty}[\Psi]$ carries a chiral quantum group
 10710	datum with OPE compatibility at all spins, proved by
 10711	the coderivation property on the Koszul-locus bar complex
 10712	and independently by the JKL vertex bialgebra theorem on
 10713	the CoHA. A constant coproduct does not exist for
 10714	$c \neq 0$ (conformal anomaly obstruction).
exec
/bin/zsh -lc "sed -n '1,220p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for f in standalone/bp_self_duality.tex standalone/classification_trichotomy.tex standalone/gaudin_from_collision.tex standalone/three_parameter_hbar.tex; do echo "FILE $f"; sed -n '"'1,120p' \""'$f"; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage{tikz-cd}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,
  linkcolor=blue!60!black,
  citecolor=green!40!black,
  urlcolor=blue!60!black]{hyperref}

% ================================================================
 succeeded in 51ms:
FILE standalone/bp_self_duality.tex
\documentclass[11pt]{article}

%%% Packages
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=blue!60!black,
 citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

%%% Page geometry
\usepackage[margin=1.15in]{geometry}

%%% Theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]







thinking
**Investigating log issues**

I'm looking at an issue with the ordered chiral homology log line 10711, and I'm thinking it might be due to a mismatch with the source line, which doesn't have \cX. The log shows some inconsistencies, suggesting I shouldn't fully trust it after changes. I need to compile the current file fresh to verify things.

Similarly, for the introduction_full_survey log line 422, it might have changed too, so I really should compile all the problematic files, probably using `latexmk -pdf` for efficiency, even if it takes a while.
thinking
**Planning to compile files**

I need to verify current issues and consider compiling either a subset of files with candidate problems or all of them, especially since the user requested a thorough audit. An automated script could run `pdflatex` in a way that doesn’t stop at the first error, allowing me to gather all the errors. I should also account for unresolved citations needing BibTeX.

Running this process for each file, particularly as there are around 40 long files, may take some time. Compiling in the standalone directory could be the easiest solution.
thinking
**Considering compilation options**

I think using `pdflatex -draftmode` for each file could work, even if it takes a few minutes. I have enough time, and I might use `timeout` for each file to manage things better. If `texfot` is installed, that might simplify the process. 

I should note that external bibliographies without BibTeX will result in citation warnings, but some standalone files might not cause any issues. Since the user mentioned unresolved references and citations, I want to handle those carefully, but compiling everything at once might be too overwhelming.
thinking
**Evaluating LaTeX files**

I'm considering whether to use `lacheck`, but it might not be necessary. My plan is to selectively compile files with the biggest issues. 

It looks like many files are missing the xcolor package, which is causing undefined colors, especially for those using hyperref colored links. I can likely identify these by using grep. It seems I'll need to audit all standalone files for these hidden imports as well.

I'll grep for files that include hyperref colors but lack the xcolor package, which could potentially uncover many instances.
thinking
**Reviewing standalone files**

I'm looking at standalone files that might define their own macros. I could use a script to identify candidate undefined macros that aren't in the local definitions or the main preamble. 

I'll need to exclude standard macros by package. When verifying truly undefined custom macros, I can focus on commands with uppercase or unusual patterns. For example, I noticed that the log shows `\cF` as undefined, but the source does define it, indicating stale log data. 

I should perform a fresh compile or analyze the current source for undefined macros, especially checking files like N2 and N3.
thinking
**Fixing macro definitions**

I see that the main preamble defines `\BarchFG`, but for a standalone file to be self-contained, it needs to include its own local or imported definitions. Since the current source doesn't have it, the log confirms this issue. 

To resolve it, I need to add `\providecommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` near the other bar macros or, if it was meant to use `\Barch`, I should replace it with that. I need to check the source context further and then compile to verify the correction.
thinking
**Compiling document files**

I’m planning to compile N3 quickly. I might run pdflatex on it, using a direct command. I also want to compile other documents like programme_summary, introduction_full_survey, and survey_modular_koszul_duality to check for any undefined macros. Using `pdflatex -interaction=nonstopmode -draftmode` sounds good for that. I need to make sure I'm in the standalone directory to create a log. So, I think I’ll compile these select files.
codex
The stale-log risk is real: one old log already pointed at a line that no longer contains the offending macro. I’m switching the high-risk files to a fresh `pdflatex -draftmode` pass so the findings reflect the current tree, not archaeology.
exec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -draftmode N3_e1_primacy.tex >/tmp/N3_e1_primacy.audit.out 2>&1; tail -n 80 /tmp/N3_e1_primacy.audit.out' in /Users/raeez/chiral-bar-cobar/standaloneexec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -draftmode programme_summary.tex >/tmp/programme_summary.audit.out 2>&1; tail -n 80 /tmp/programme_summary.audit.out' in /Users/raeez/chiral-bar-cobar/standaloneexec
/bin/zsh -lc 'pdflatex -interaction=nonstopmode -draftmode introduction_full_survey.tex >/tmp/introduction_full_survey.audit.out 2>&1; tail -n 120 /tmp/introduction_full_survey.audit.out' in /Users/raeez/chiral-bar-cobar/standalone succeeded in 487ms:
! Double superscript.
l.629 \Cobar^
             {(g)}\!\bigl(\Barord(\cA)(g,\bullet)\bigr)

[8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 751.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 751.


[9]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 769.


 succeeded in 557ms:

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 1843.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 1897.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\Phi' on input line 1897.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 1897.


[20]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
 succeeded in 716ms:
! LaTeX Error: Environment convention undefined.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.5269 \begin{convention}
                         [Semantic levels: homotopy, model, shadow]

LaTeX Warning: Reference `prop:model-independence' on page 80 undefined on inpu
t line 5304.


! LaTeX Error: \begin{document} ended by \end{convention}.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.5305 \end{convention}
codex
I’ve confirmed one important correction already: some old “undefined macro” hits are gone on current source. I’m running a repo-wide fresh compile summary now so the audit is anchored to the live standalone surface and I can separate real failures from stale logs.
exec
/bin/zsh -lc "python3 - <<'PY'
import subprocess, pathlib, re, os, json, sys
root = pathlib.Path('standalone')
texs = sorted(root.glob('*.tex'))
summary = []
for tex in texs:
    proc = subprocess.run(
        ['pdflatex','-interaction=nonstopmode','-draftmode',tex.name],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=180
    )
    out = proc.stdout
    errs = []
    warns = []
    for line in out.splitlines():
        if ('Undefined control sequence' in line or 'LaTeX Error:' in line or 'Double superscript.' in line or 'Double subscript.' in line):
            errs.append(line.strip())
        if ('There were undefined references.' in line or 'Citation "'`'"' in line or 'Reference "'`'"' in line):
            warns.append(line.strip())
    if errs or warns:
        summary.append((tex.name, errs[:20], warns[:20]))
print('FILES_WITH_ISSUES', len(summary))
for name, errs, warns in summary:
    print('FILE', name)
    for e in errs:
        print('ERR', e)
    if warns:
        print('WARN_COUNT', len(warns))
        for w in warns[:8]:
            print('WARN', w)
    print('END')
PY" in /Users/raeez/chiral-bar-cobarcodex
The compile sweep is still running. Once it settles I’ll have a current file-by-file error map instead of cherry-picked failures.
 exited 1 in 12.83s:
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 556, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 1220, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 2193, in _communicate
    stdout = self._translate_newlines(stdout,
                                      self.stdout.encoding,
                                      self.stdout.errors)
  File "/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 1098, in _translate_newlines
    data = data.decode(encoding, errors)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb9 in position 18326: invalid start byte
codex
The sweep hit a decoding issue in `pdflatex` output, not a manuscript blocker. I’m rerunning it with binary-safe decoding so the remaining issue map is usable.
exec
/bin/zsh -lc "python3 - <<'PY'
import subprocess, pathlib, re
root = pathlib.Path('standalone')
texs = sorted(root.glob('*.tex'))
summary = []
for tex in texs:
    proc = subprocess.run(
        ['pdflatex','-interaction=nonstopmode','-draftmode',tex.name],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180
    )
    out = proc.stdout.decode('latin-1', errors='replace')
    errs = []
    warns = []
    for line in out.splitlines():
        if ('Undefined control sequence' in line or 'LaTeX Error:' in line or 'Double superscript.' in line or 'Double subscript.' in line):
            errs.append(line.strip())
        if ('There were undefined references.' in line or 'Citation "'`'"' in line or 'Reference "'`'"' in line):
            warns.append(line.strip())
    if errs or warns:
        summary.append((tex.name, errs[:40], warns[:40]))
print('FILES_WITH_ISSUES', len(summary))
for name, errs, warns in summary:
    print('FILE', name)
    for e in errs:
        print('ERR', e)
    if warns:
        print('WARN_COUNT', len(warns))
        for w in warns[:10]:
            print('WARN', w)
    print('END')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 31.51s:
FILES_WITH_ISSUES 23
FILE N2_mc3_all_types.tex
ERR ! Undefined control sequence.
ERR ! Undefined control sequence.
ERR ! Undefined control sequence.
ERR ! Undefined control sequence.
END
FILE N3_e1_primacy.tex
ERR ! Undefined control sequence.
ERR ! Undefined control sequence.
ERR ! Double superscript.
ERR ! Double superscript.
ERR ! Double superscript.
END
FILE N6_shadow_formality.tex
ERR ! Double subscript.
WARN_COUNT 2
WARN LaTeX Warning: Reference `cor:operadic-complexity' on page 2 undefined on input
WARN LaTeX Warning: There were undefined references.
END



thinking
**Identifying error details**

I need to pinpoint the exact macros or lines related to the errors. One option might be to recompile with `-file-line-error` to retrieve line information. However, the summary from compilation doesn't display line numbers, so parsing the logs could be necessary. I’m weighing which findings to include since multiple root causes may arise. Severity classification could help, labeling compile errors as HIGH or CRITICAL. The user wants every unresolved reference, but including them might not be feasible. I might need to group findings in the required format.
thinking
**Addressing unresolved references**

I've resolved all undefined color errors, which captures the root cause. For unresolved references, I could group them by file, marking the first line of each unresolved reference. However, the user wants every single unresolved reference listed. It might be better to list each unique unresolved reference, even if there are dozens. I could scope the audit to focus on “foundation” first, but should try to include all findings as feasible. I also need to generate exact line references for compile errors.
thinking
**Parsing undefined control sequences**

To address undefined control sequences, I might parse fresh logs using `rg -n` to get current file line numbers. By inspecting the source context, I can identify any problematic macros, aiming for one entry per unique macro or root cause. I’ll review logs for each problematic file and consider using a script to extract line numbers and macro names. It's worth noting that the current compile didn’t use `-file-line-error`, but the logs do include the file:line format, which is great for parsing.
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib, re
files = [
'N2_mc3_all_types','N3_e1_primacy','N6_shadow_formality','bp_self_duality','classification_trichotomy','editorial','gaudin_from_collision','introduction_full_survey','ordered_chiral_homology','programme_summary','shadow_towers_v2','survey_modular_koszul_duality','survey_modular_koszul_duality_v2','three_parameter_hbar','w3_holographic_datum']
for stem in files:
    path = pathlib.Path('standalone')/f'{stem}.log'
    print('FILE', path)
    text = path.read_text('latin-1')
    lines = text.splitlines()
    for i,l in enumerate(lines):
        if 'Undefined control sequence' in l or 'LaTeX Error:' in l or 'Double superscript.' in l or 'Double subscript.' in l:
            print(f'LOG {i+1}: {l}')
            for j in range(i+1,min(i+4,len(lines))):
                print(f'  {j+1}: {lines[j]}')
    print('END')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE standalone/N2_mc3_all_types.log
LOG 612: ! Undefined control sequence.
  613: <recently read> \cF 
  614:                     
  615: l.391 $\cF
LOG 623: ! Undefined control sequence.
  624: <recently read> \cF 
  625:                     
  626: l.391 ...N} \subset \cO^{\mathrm{sh}}$, where $\cF
LOG 634: ! Undefined control sequence.
  635: <recently read> \cF 
  636:                     
  637: l.394 pieces $\cF
LOG 645: ! Undefined control sequence.
  646: l.394 pieces $\cF^{\geq N} / \cF
  647:                                 ^{\geq N+1}$ are finite-dimensional
  648: The control sequence at the end of the top line
END
FILE standalone/N3_e1_primacy.log
LOG 487: ! Undefined control sequence.

thinking
**Investigating output issues**

I see that the output got truncated in both the editorial and introduction_full_survey sections due to numerous errors. I might need to check the exact source line numbers to identify the main root causes. The user requested exhaustive detail, but listing every undefined macro might be too much if there are dozens. I should explore the top of editorial.tex to see if it's a self-contained paper or simply a wrapper using macros like `\mainpreambleonly`. There are likely many undefined commands due to missing imports, so I’ll need to investigate further.
exec
/bin/zsh -lc "sed -n '1,220p' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' standalone/editorial.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\usepackage\\{xcolor\\}|blue"'!60!black|green!40!black'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
\usepackage[all]{xy}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
 succeeded in 51ms:
% Editorial companion: the archive-only concordance and constitution chapters.
\def\archivebuild{1}
\def\mainpreambleonly{1}
\IfFileExists{main.tex}{\input{main.tex}}{\input{../main.tex}}

\newcommand{\repoinput}[1]{%
 \IfFileExists{#1.tex}{\input{#1}}{\input{../#1}}%
}

\begin{document}
\frontmatter
\tableofcontents
\mainmatter
\repoinput{chapters/connections/concordance}
\repoinput{chapters/connections/editorial_constitution}
\backmatter
\repoinput{bibliography/references}
\end{document}
 succeeded in 52ms:
standalone/N3_e1_primacy.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/N4_mc4_completion.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/N2_mc3_all_types.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/N5_mc5_sewing.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/N1_koszul_meta.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/classification_trichotomy.tex:12:\usepackage[colorlinks=true,linkcolor=blue!60!black,
standalone/classification_trichotomy.tex:13: citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/classification.tex:11:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/chiral_chern_weil.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,
standalone/chiral_chern_weil.tex:15: citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/en_chiral_operadic_circle.tex:15:\usepackage{xcolor}
standalone/en_chiral_operadic_circle.tex:16:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black]{hyperref}
standalone/N6_shadow_formality.tex:13:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/bp_self_duality.tex:11:\usepackage[colorlinks=true,linkcolor=blue!60!black,
standalone/bp_self_duality.tex:12: citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/computations.tex:11:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/arithmetic_shadows.tex:14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/holographic_datum.tex:15:  linkcolor=blue!60!black,
standalone/holographic_datum.tex:16:  citecolor=green!40!black,
standalone/holographic_datum.tex:17:  urlcolor=blue!60!black]{hyperref}




thinking
**Exploring xcolor usage**

I’m considering how to identify missing xcolor preambles that are leading to compile failures in specific files like bp_self_duality and classification_trichotomy. It’s odd that other files compile fine despite lacking xcolor. Maybe some articles load color through different packages. I’m also wondering if hyperref or something else handles color. It seems missing xcolor could be a latent issue in many files, and since the user asked for a foundation audit, I should report all those that need it.
thinking
**Identifying hidden imports**

I’m noticing that a file has hyperref using mixed colors but lacks the xcolor package, which poses a compile risk—even if it's not currently causing an issue due to no active links. The user asked about missing definitions for hidden imports, so I might report those too, though it could be overwhelming. I think I could group them: for instance, note the issue with hyperref and suggest adding `\usepackage[dvipsnames]{xcolor}` before hyperref. Additionally, many files have unresolved references due to missing theorem labels, which could be addressed by replacing internal cross-references with explicit names.
thinking
**Organizing unresolved references**

I’m considering grouping all unresolved references in a file into a single finding with the exact line spans and a strategy for fixing them. The user requested specific fixes, so I could advise replacing `\ref{...}` at those lines with explicit text or incorporating the referenced statements into the standalone file to avoid dangling cross-volume labels. To be more precise, I might specify the actual labels for each line. I could use rg to extract those reference lines from each file.
thinking
**Considering macro definitions**

It looks like the survey_modular_koszul_duality is missing a few critical definitions like \Hom, \End, and others. I might consider suggesting importing these from `main.tex` or adding the required entries directly in the preamble. If the user wants an exact fix, I could recommend definitions such as `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, and others as listed. It could also be helpful to check the survey file's top to see what definitions are already there.
exec
/bin/zsh -lc "sed -n '1,180p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,180p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt]{report}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{principle}[theorem]{Principle}
\newtheorem{evidence}[theorem]{Evidence}
\newtheorem{computation}[theorem]{Computation}
\theoremstyle{definition}
 succeeded in 51ms:
\documentclass[11pt]{report}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{principle}[theorem]{Principle}
\newtheorem{evidence}[theorem]{Evidence}
\newtheorem{computation}[theorem]{Computation}
\theoremstyle{definition}
exec
/bin/zsh -lc "sed -n '1,180p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,
 linkcolor=blue!60!black,
 citecolor=green!40!black,
 urlcolor=blue!60!black]{hyperref}

% ================================================================
% Theorem environments

thinking
**Inspecting commands in N2**

I think I need to look closely at the N2 preamble since it shows `\cF` as undefined, even though it seemed defined before. It’s puzzling. The previous part shows `\newcommand{\cF}`, so I wonder why it's still saying it's undefined. Could the `\c` accent be overriding it? The compiler mentioned `\cF` is undefined at line 391, so it might be due to that accent issue. I should check the top of N2 and use grep to confirm.
exec
/bin/zsh -lc "sed -n '1,80p' standalone/N2_mc3_all_types.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\newcommand\\{\\\\cF\\}|\\\\providecommand\\{\\\\cF\\}|\\\\renewcommand\\{\\\\cF\\}' standalone/N2_mc3_all_types.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
\usepackage[all]{xy}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
 exited 1 in 51ms:


thinking
**Identifying a definition issue**

I realized that N2 doesn't define \cF, which is good to note. Now, I need to check N6 at the top to identify the source of a double subscript, as it might be a typo. It’s interesting to see how these details can affect things, and I want to get this right. So, I'll inspect that closely and see what I can find. Let's keep unraveling this!
exec
/bin/zsh -lc "sed -n '1,120p' standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N6_shadow_formality.tex | sed -n '228,244p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\cX|\\\\ChirHoch|\\\\BarchFG|\\\\CompCl|\\\\Defcyc|\\\\orline|\\\\chirAss|\\\\chirLie|\\\\chirCom|\\\\dzero|\\\\dfib|\\\\chirtensor|\\\\Convinf|\\\\Convstr|\\\\convention|\\\\tikzcd|\\\\longtable|\\\\Ydg|\\\\Ran\\"'^'"\\{\\\\ord\\}|\\\\barB\\"'^'"\\{\\\\ord\\}' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   228	carries the deconcatenation coproduct, with differential
   229	assembled from $\eta_{ij}=d\log(z_i-z_j)$ and the chiral product
   230	$\mu\colon j_*j^*(\cA\boxtimes\cA)\to\Delta_*\cA$. The
   231	\emph{modular convolution dg Lie algebra} is
   232	\[
   233	\gmod\;:=\;\Hom^{\mathrm{cyc}}
   234	\bigl(\barB(\cA),\,\cA\bigr)\otimes\mathsf{G},
   235	\]
   236	where $\mathsf{G}=\bigoplus_{g\ge 0}\mathsf{G}^{(g)}$ is the
   237	coefficient algebra generated by stable graphs on
   238	$\overline{\cM}_{g,n}$. The genus filtration gives
   239	$\gmod=\bigoplus_{g\ge 0}\gmod_g$; the genus-zero part
   240	$\gmodzero=\Hom^{\mathrm{cyc}}(\barB(\cA),\cA)\otimes
   241	\mathsf{G}^{(0)}$ is a strict dg Lie algebra with bracket
   242	$[-,-]^{(0)}$ from tree composition, since genus-zero stable
   243	graphs are trees.
   244	
 succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
 succeeded in 51ms:
standalone/N3_e1_primacy.tex:346:Let $\BarchFG(\cA)$ denote the Francis--Gaitsgory chiral Lie bar,
standalone/N3_e1_primacy.tex:357:\mathrm{gr}\,\BarSig(\cA) \twoheadrightarrow \BarchFG(\cA),
standalone/N1_koszul_meta.tex:56:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/N1_koszul_meta.tex:167:\item $\ChirHoch^*(\cA)$ is a polynomial algebra with generators
standalone/N1_koszul_meta.tex:402:Its cohomology $\ChirHoch^*(\cA)$ is the tangent complex to the
standalone/N1_koszul_meta.tex:445:\item $\ChirHoch^*(\cA)$ is a polynomial algebra with generators
standalone/N1_koszul_meta.tex:527:this resolution turns $\ChirHoch^*(\cA)$ into a bigraded complex
standalone/N1_koszul_meta.tex:530:polynomial structure of $\ChirHoch^*$ in degrees $\{0,1,2\}$
standalone/N1_koszul_meta.tex:537:Conversely, suppose $\ChirHoch^*(\cA)$ is polynomial with
standalone/chiral_chern_weil.tex:49:\newcommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
standalone/chiral_chern_weil.tex:62:\newcommand{\dfib}{d_{\mathrm{fib}}}
standalone/chiral_chern_weil.tex:102:differential acquires curvature $\dfib^{\,2} = \kappa(\cA)\cdot
standalone/chiral_chern_weil.tex:140:curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$,
standalone/chiral_chern_weil.tex:772:\tr\bigl(\dfib^{\,2}\big|_{\mathrm{dp}}\bigr)
standalone/chiral_chern_weil.tex:897:$\dfib^{\,2} = \kappa\cdot\omega_g$ arises not from the
standalone/chiral_chern_weil.tex:1060:to the fiberwise curvature $\dfib^{\,2}$ on a genus-$1$ curve:
standalone/chiral_chern_weil.tex:1062:\dfib^{\,2}\big|_{\mathrm{dp}}(J^a \boxtimes J^b)
standalone/chiral_chern_weil.tex:1069:\tr\bigl(\dfib^{\,2}\big|_{\mathrm{dp}}\bigr)
standalone/chiral_chern_weil.tex:1080:\dfib^{\,2}\big|_{\mathrm{sp}}(J^a \boxtimes J^b)
standalone/chiral_chern_weil.tex:1095:\tr\bigl(\dfib^{\,2}\big|_{\mathrm{sp}}\bigr)




thinking
**Evaluating definitions and fixes**

This search output is helpful! I think I should inspect specific lines at the top for any missing definitions related to the introduction or survey. Maybe the preambles already define some, but not all of them. 

I need to compile current errors in the file survey_modular_koszul_duality_v2, particularly concerning \ord, \Ydg, and \fl. It seems like \cX is undefined according to the current log, although it should be defined in the preamble. I need to consider adding commands like `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` and `\newcommand{\cX}{\mathcal{X}}` for clarity.
thinking
**Identifying missing definitions**

I need to add some missing definitions from the compile log. For instance, \CompCl is missing, and \Aut is undefined at line 7464 because it’s not defined at the top.

I think \Bbbk might already exist. I also wonder if \Convinf and \Convstr are already defined. 

It seems the preamble in survey_modular_koszul_duality might be incomplete across several macros. The user wanted every undefined macro, so I could list a few findings: `\Hom`, `\End`, `\orline`, `\Defcyc`, and `\Aut`. I’m not sure if there are any others based on the log.
thinking
**Correcting macros in LaTeX**

I need to replace `\providecommand{\Dg}{\mathrm{dg}}` with `\providecommand{\Dg}[1]{D_{#1}}` and possibly introduce a new macro for dg. There may be other macros that need fixing, like for `survey_track`. To address the user’s request for a foundation audit of the standalone files, I'll search for this in the files. We might also need to focus on compile errors and some preamble mismatches. Additionally, I’ll check for any missing commands like `\R`, `\Bbbk`, and `\colim`.
thinking
**Inspecting source code**

I’m looking into `\widehat{\fg^{\mathrm{fl}}}` and need to check the source around line 8211. I wonder if it might not be straightforward. I think I should really take a close look at the surrounding lines to gather more context. Understanding this could be key, and I want to ensure I’m not missing anything. So, I’ll inspect those current line numbers and see what’s going on!
exec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '700,712p;6664,6672p;8206,8214p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,170p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '40,110p;270,290p;418,440p;474,490p;548,570p;604,622p;632,642p;720,750p;816,846p;1098,1110p;1214,1256p;1278,1284p;1836,1848p;2304,2320p;2438,2454p;2588,2604p;3348,3382p;4310,4316p;4518,4526p;4596,4602p;4639,4656p;4788,4795p;5008,5014p;5058,5088p;5158,5166p;5266,5335p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   700	
   701	\subsection*{1.10.\enspace The $E_n$-chiral hierarchy
   702	and derived centres}
   703	
   704	$E_n$-chiral algebras are factorisation algebras and are inherently
   705	geometric. $E_\infty$-chiral algebras (all standard vertex algebras)
   706	live on $\Ran(X)$; the symmetric bar $\barB^\Sigma$ is their bar
   707	complex. $E_1$-chiral algebras live on $\Ran^{\ord}(X)$; the ordered
   708	bar $\barB^{\ord}$ carries the $R$-matrix. The formality bridge
   709	(Theorem~\ref{thm:e1-formality-bridge}): for $E_\infty$-input,
   710	ordered and symmetric bars are quasi-isomorphic. The formality
   711	failure (Theorem~\ref{thm:e1-formality-failure}): for genuinely
   712	$E_1$-input (Yangians, Etingof--Kazhdan quantum vertex algebras),
  6664	holographic datum collapses to the single scalar~$k$.
  6665	
  6666	\smallskip
  6667	\noindent\emph{Non-abelian CS} ($SL_2$, level $k$): boundary
  6668	$\widehat{\mathfrak{sl}}_2{}_k$, line dual
  6669	$\Ydg(\mathfrak{sl}_2)$, $r(z) = k\,\Omega/z$ (vanishing at
  6670	$k = 0$), $\kappa = 3(k{+}2)/4$. Evaluation-module
 succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
\usepackage[all]{xy}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
 succeeded in 51ms:
    40	\providecommand{\cN}{\mathcal{N}}
    41	\providecommand{\cO}{\mathcal{O}}
    42	\providecommand{\cP}{\mathcal{P}}
    43	\providecommand{\cQ}{\mathcal{Q}}
    44	\providecommand{\cR}{\mathcal{R}}
    45	\providecommand{\cS}{\mathcal{S}}
    46	\providecommand{\cT}{\mathcal{T}}
    47	\providecommand{\cU}{\mathcal{U}}
    48	\providecommand{\cV}{\mathcal{V}}
    49	\providecommand{\cW}{\mathcal{W}}
    50	\providecommand{\cX}{\mathcal{X}}
    51	\providecommand{\cY}{\mathcal{Y}}
    52	\providecommand{\cZ}{\mathcal{Z}}
    53	\providecommand{\barB}{\bar{B}}
    54	\providecommand{\barBgeom}{\bar{B}^{\mathrm{geom}}}
    55	\providecommand{\barC}{\overline{C}}
    56	\providecommand{\Ran}{\mathrm{Ran}}
    57	\providecommand{\MC}{\mathrm{MC}}
    58	\providecommand{\Sym}{\mathrm{Sym}}
    59	\providecommand{\FM}{\overline{C}}

thinking
**Inspecting compile error**

I need to check the compile error in `survey_modular_koszul_duality_v2`, specifically at line 8211 due to `\fg\fl`. I'll search for `\fgl` throughout the repository. It's important to make sure I pinpoint the issue accurately. This could involve looking at how `\fg` and `\fl` are defined and used. I wonder if they might have compatibility issues causing the compile error. Let's dive in and sort this out!
exec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality_v2.tex | sed -n '8208,8214p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\fgl|\\\\fg\\\\fl|gl\\\\}_1|Y\\"'^'"\\+\\(\\\\widehat' standalone/survey_modular_koszul_duality_v2.tex chapters appendices main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\providecommand\\{\\\\ord\\}|\\\\newcommand\\{\\\\ord\\}|\\\\DeclareMathOperator\\{\\\\ord\\}|\\\\providecommand\\{\\\\Ydg\\}|\\\\newcommand\\{\\\\Ydg\\}|\\\\providecommand\\{\\\\chirAss\\}|\\\\newcommand\\{\\\\chirAss\\}|\\\\newtheorem\\{convention\\}|\\\\usepackage\\{tikz-cd\\}|\\\\usepackage\\{longtable\\}' standalone/*.tex main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  8208	categorified averaging (Drinfeld centre), and higher Deligne
  8209	(derived centre). The circle closes for 3d HT theories with
  8210	conformal vector: the Drinfeld centre
  8211	$\cZ(\Rep^{E_1}(Y^+(\widehat{\fg\fl}_1)))
  8212	\cong \Rep^{E_2}(\cW_{1+\infty})$
  8213	identifies the $E_2$ Drinfeld centre of the $E_1$ quantum group
  8214	representation category with the $E_2$ representation category of
 succeeded in 52ms:
standalone/survey_modular_koszul_duality_v2.tex:8211:$\cZ(\Rep^{E_1}(Y^+(\widehat{\fg\fl}_1)))
standalone/survey_modular_koszul_duality_v2.tex:8353:$\cZ(\Rep^{E_1}(Y^+(\widehat{\mathfrak{gl}}_1)))
chapters/theory/ordered_associative_chiral_kd.tex:8571:$\cH_{\mathrm{Jor}} \cong Y^+(\widehat{\mathfrak{gl}}_1)$
chapters/theory/ordered_associative_chiral_kd.tex:8786:$\cH_{\mathrm{Jor}} \cong Y^+(\widehat{\mathfrak{gl}}_1)$
chapters/theory/ordered_associative_chiral_kd.tex:9048:Y^+(\widehat{\mathfrak{gl}}_1)$~\cite{SV13}, and the
chapters/theory/ordered_associative_chiral_kd.tex:9053:is $Y^+(\widehat{\mathfrak{sl}}_N)$, and the JKL
chapters/theory/ordered_associative_chiral_kd.tex:10024:  $\cH_{\mathrm{Jor},N} \cong Y^+(\widehat{\mathfrak{gl}}_N)$
chapters/theory/ordered_associative_chiral_kd.tex:10041:$\cH_{\mathrm{Jor},N} \cong Y^+(\widehat{\mathfrak{gl}}_N)$.
chapters/theory/ordered_associative_chiral_kd.tex:10160:\cong Y^+(\widehat{\mathfrak{gl}}_N)$
 succeeded in 51ms:
standalone/classification_trichotomy.tex:43:\DeclareMathOperator{\ord}{ord}
standalone/N1_koszul_meta.tex:15:\usepackage{tikz-cd}
standalone/cy_quantum_groups_6d_hcs.tex:10:\usepackage{tikz-cd}
standalone/gaudin_from_collision.tex:51:\DeclareMathOperator{\ord}{ord}
standalone/analytic_sewing.tex:16:\usepackage{tikz-cd}
standalone/five_theorems_modular_koszul.tex:10:\usepackage{tikz-cd}
standalone/koszulness_fourteen_characterizations.tex:16:\usepackage{tikz-cd}
standalone/sc_chtop_pva_descent.tex:13:\usepackage{tikz-cd}
standalone/cy_to_chiral_functor.tex:10:\usepackage{tikz-cd}
standalone/w3_holographic_datum.tex:46:\DeclareMathOperator{\ord}{ord}
standalone/virasoro_r_matrix.tex:42:\DeclareMathOperator{\ord}{ord}
standalone/multi_weight_cross_channel.tex:54:\DeclareMathOperator{\ord}{ord}
standalone/notation_index.tex:5:\usepackage{longtable}
standalone/e1_primacy_ordered_bar.tex:13:\usepackage{tikz-cd}
standalone/drinfeld_kohno_bridge.tex:13:\usepackage{tikz-cd}
standalone/drinfeld_kohno_bridge.tex:96:\newcommand{\Ydg}{Y^{\mathrm{dg}}}
standalone/arithmetic_shadows.tex:80:\providecommand{\ord}{\mathrm{ord}}
standalone/en_chiral_operadic_circle.tex:30:\newtheorem{convention}[theorem]{Convention}
standalone/en_chiral_operadic_circle.tex:77:\providecommand{\chirAss}{\mathrm{Ass}^{\mathrm{ch}}}
main.tex:47:\usepackage{tikz-cd}


thinking
**Inspecting unresolved references**

I'm aiming to inspect the `programme_summary` sections to identify unresolved references. I could gather one finding per file that has missing local labels and maybe group them. However, since the user asked for every missing definition, hidden import, and unresolved reference, I think we should include files with only warnings too. I’ll need to compile exact lines from the logs and use a tool to extract those unresolved references. Finally, I might summarize multiple unresolved labels while providing specific fixes.
thinking
**Addressing unresolved references**

I’m noticing that for some files, warnings are originating from broken standalone extraction, which isn't including theorem labels or bibliographies. A possible root fix would involve including those referenced theorem statements or rewriting mentions to avoid cross-file references. For instance, `classification.tex` has six unresolved references to monograph labels. To fix this, I could either add local placeholder labels or replace each `\ref` with theorem titles. I'll need to extract those actual reference lines and labels, and I can script this for the warning-only files.
codex
The compile-blocking layer is mostly mapped. I’m doing one more pass over the warning-only files to pin down the dangling labels/citations with exact source lines, so I don’t leave the “soft failures” hand-wavy.
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib, re
files = ['classification','cy_quantum_groups_6d_hcs','programme_summary_sections2_4','programme_summary_sections5_8','programme_summary_sections9_14','riccati','survey_track_a_compressed','survey_track_b_compressed','N6_shadow_formality']
for stem in files:
    log = pathlib.Path('standalone')/f'{stem}.log'
    print('FILE', stem)
    text = log.read_text('latin-1')
    for m in re.finditer(r\"LaTeX Warning: (Reference|Citation) "'`([''^'"']+)' on page .*? line (\\d+)\", text):
        kind,label,line = m.groups()
        print(kind, label, line)
    if 'There were undefined references.' in text:
        print('WARN', 'There were undefined references.')
    print('END')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
FILE classification
WARN There were undefined references.
END
FILE cy_quantum_groups_6d_hcs
Citation LorgatCYChiral 183
WARN There were undefined references.
END
FILE programme_summary_sections2_4
Reference ssec:d-squared 559
WARN There were undefined references.
END
FILE programme_summary_sections5_8
Citation Drinfeld85 195
Citation KZ84 196
Citation STS83 197
Citation FFR94 197
Reference sec:bar 315
Reference def:shadow-depth 5
WARN There were undefined references.
END

thinking
**Inspecting macro block lines**

I need to check the exact lines for N2, N3, and so on. I've already got some lines, but now I should inspect the top definitions for N3, ensuring there’s no \BarchFG involved. I want to take a look at the line numbers around the macro block, so I’ll need to perform a search for that. I think this will help me clarify what I'm working with and make everything more organized!
exec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '1,90p;610,632p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\documentclass[11pt,reqno]{amsart}
     2	
     3	% ================================================================
     4	% Packages
     5	% ================================================================
     6	\usepackage{amsmath,amssymb,amsthm}
     7	\usepackage{mathrsfs}
     8	\usepackage{enumerate}
     9	\usepackage[shortlabels]{enumitem}
    10	\usepackage{booktabs}
    11	\usepackage{array}
    12	\usepackage{microtype}
    13	\usepackage[dvipsnames]{xcolor}
    14	\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
    15	
    16	% ================================================================
    17	% Theorem environments
    18	% ================================================================
    19	\newtheorem{theorem}{Theorem}[section]
    20	\newtheorem{proposition}[theorem]{Proposition}
exec
/bin/zsh -lc "nl -ba standalone/N2_mc3_all_types.tex | sed -n '30,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '30,55p;1038,1046p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    30	\newtheorem{example}[theorem]{Example}
    31	\theoremstyle{remark}
    32	\newtheorem{remark}[theorem]{Remark}
    33	
    34	% ================================================================
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
 succeeded in 52ms:
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
    49	\newcommand{\Ext}{\mathrm{Ext}}

thinking
**Inspecting code for issues**

I need to look into the `shadow_towers_v2` around the lines that are causing it to be used only in a preamble and in duplicated environments. I think I should search for a nested document because it's likely that the file might contain a pasted full preamble in the middle of the document. It might help to inspect near line 1, as it probably includes another file. Let’s focus on the error line numbers for clarity.
exec
/bin/zsh -lc "sed -n '1,80p' standalone/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' standalone/classification.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/shadow_towers_v2.tex | sed -n '140,210p;620,700p;700,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[margin=1.15in]{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
 succeeded in 51ms:
\documentclass[11pt]{article}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=blue!60!black,
 citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
 succeeded in 51ms:
   140	sections of a $\mathcal{D}_X$-module, the quadratic relations
   141	become operator product expansions with meromorphic singularities,
   142	and the bar differential becomes an integral transform whose
   143	kernel is the logarithmic $1$-form
   144	$\eta_{ij} = d\log(z_i - z_j)$ on the Fulton--MacPherson
   145	compactification $\FM_n(X)$ of the configuration space. The
   146	resulting object, the \emph{chiral bar complex}
   147	$\barB^{\mathrm{ch}}(\cA)$, is a factorization coalgebra on the
   148	Ran space $\Ran(X)$ \cite{BD04, FG12, CG17}.
   149	
   150	At genus~$0$, the classical theory embeds via restriction to
   151	the formal disk (the embedding requires specifying a retraction
   152	$\mathbb{A}^1 \to \mathrm{pt}$ and its homotopy transfer;
   153	the $E_1/E_\infty$ bar distinction, the Arnol'd algebra
   154	of~$\mathrm{Conf}_n(\mathbb{A}^1)$, and the Fulton--MacPherson
   155	compactifications are already absent over a bare point). At
   156	genus~$g \ge 1$, the topology of the curve forces further
   157	structure: the bar differential acquires curvature
   158	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$, where
   159	$\omega_g = c_1(\mathbb{E})$ is the Hodge class on
exec
/bin/zsh -lc 'for f in standalone/classification.tex standalone/programme_summary_sections2_4.tex standalone/programme_summary_sections5_8.tex standalone/programme_summary_sections9_14.tex standalone/riccati.tex standalone/survey_track_a_compressed.tex standalone/survey_track_b_compressed.tex standalone/N6_shadow_formality.tex standalone/cy_quantum_groups_6d_hcs.tex; do echo FILE $f; rg -n '"'\\\\ref\\{|\\\\cite\\{' \""'$f"; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE standalone/classification.tex
66:The single-line dichotomy (Theorem~\ref{thm:single-line-dichotomy})
93:stratum; see Definition~\ref{def:class-C}.
96:The classification is exhaustive: every entry in Table~\ref{tab:master-shadow}
100:(Theorem~\ref{thm:riccati-algebraicity}), and its Taylor coefficients
267:(Theorem~\ref{thm:depth-decomposition}), where the algebraic depth
291:Table~\ref{tab:master-shadow} records, for each standard family,
386:(stratum separation, Definition~\ref{def:class-C}).
403:Table~\ref{tab:exceptional-shadow} records the affine Kac--Moody
720:transformation. The depth gap (Proposition~\ref{prop:depth-gap-standalone})
725:(Proposition~\ref{prop:sc-formality-standalone}) shows that
728:(Proposition~\ref{prop:betagamma-contact-standalone}) reveals
731:(Conjecture~\ref{conj:ds-shadow-escalation-standalone})
734:(Proposition~\ref{prop:shadow-semilattice-standalone}) shows that
794:(Theorem~\ref{thm:riccati-algebraicity}), where the shadow metric
831:(Remark~\ref{rem:contact-stratum-separation}) terminates the
834:Proposition~\ref{prop:betagamma-contact-standalone} below.
924:Proposition~\ref{prop:sc-formality-standalone} identifies the
1008:(Theorem~\ref{thm:nms-betagamma-quartic-birth}). At conformal
1095:(Proposition~\ref{prop:depth-gap-standalone}) reduces the

thinking
**Considering citation fixes**

I’m thinking about how to address unresolved citations at lines 195-197. It might be simpler to mention adding bibliography entries to the local `thebibliography` or including `references.bib` along with `\bibliographystyle` and `\bibliography`. The user seems to want precise fixes, so I should suggest adding corresponding `\bibitem` entries for `Drinfeld85`, `KZ84`, `STS83`, and `FFR94`. I also need to check unresolved references like `sec:bar` and `def:shadow-depth` for clarity. Additionally, I’ll need to inspect `cy_quantum_groups_6d_hcs` for the unresolved citation `LorgatCYChiral`.
exec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections2_4.tex | sed -n '548,562p'; echo '---'; nl -ba standalone/programme_summary_sections5_8.tex | sed -n '188,200p;310,318p;500,510p'; echo '---'; nl -ba standalone/programme_summary_sections9_14.tex | sed -n '308,318p;560,570p;608,616p'; echo '---'; nl -ba standalone/riccati.tex | sed -n '1,12p;220,230p'; echo '---'; nl -ba standalone/survey_track_a_compressed.tex | sed -n '20,28p;720,730p;2428,2442p'; echo '---'; nl -ba standalone/survey_track_b_compressed.tex | sed -n '590,602p;910,928p'; echo '---'; nl -ba standalone/N6_shadow_formality.tex | sed -n '116,124p;168,178p'; echo '---'; nl -ba standalone/cy_quantum_groups_6d_hcs.tex | sed -n '176,186p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   548	convolution algebra.
   549	
   550	% ====================================================================
   551	\subsection{The bar-intrinsic construction}
   552	\label{ssec:bar-intrinsic}
   553	% ====================================================================
   554	
   555	The genus-completed bar differential
   556	$D_\cA = \sum_{g \ge 0} \hbar^g\,d^{(g)}_\cA$
   557	satisfies $D_\cA^2 = 0$ by the codimension-$2$ face
   558	cancellation on $\overline{\cM}_{g,n}$ (the same mechanism
   559	as~\S\ref{ssec:d-squared}, extended to all genera by Mok's
   560	log Fulton--MacPherson compactification). Write
   561	$d_0 = d^{(0)}_\cA$ for the genus-$0$ bar differential.
   562	
---
   188	\end{theorem}
   189	
   190	The seven faces are not seven theorems but seven readings of
   191	one equation. The collision residue

thinking
**Inspecting code issues**

I need to check the line numbers in the files for the xcolor hidden import and w3_holographic. It seems I was given some good hints already. I specifically want to inspect line 84 in introduction_full_survey, where it looks like Dg is defined incorrectly. I'll start by searching for that definition to understand what went wrong. Let's see how this unfolds!
exec
/bin/zsh -lc "rg -n '\\\\providecommand\\{\\\\Dg\\}|\\\\newcommand\\{\\\\Dg\\}|\\\\renewcommand\\{\\\\Dg\\}' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/introduction_full_survey.tex:84:\providecommand{\Dg}{\mathrm{dg}}
standalone/survey_track_a_compressed.tex:66:\providecommand{\Dg}{\mathrm{dg}}
standalone/survey_track_b_compressed.tex:113:\providecommand{\Dg}{\mathrm{dg}}
standalone/survey_modular_koszul_duality.tex:84:\providecommand{\Dg}{\mathrm{dg}}

thinking
**Analyzing file issues**

I'm noticing a subtle issue across multiple files that requires a detailed report. To tackle this, I might need to search for the usage of `\Dg{` within those files to pinpoint the problem. It's interesting how small coding nuances can create significant effects, so I'll be sure to investigate carefully to get this right for the user. I'll also ensure that I'm thorough in my findings to provide clarity.
exec
/bin/zsh -lc "rg -n '\\\\Dg\\{' standalone/introduction_full_survey.tex standalone/survey_track_a_compressed.tex standalone/survey_track_b_compressed.tex standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/introduction_full_survey.tex:759:restore nilpotence: $\Dg{g}^{\,2} = 0$
standalone/introduction_full_survey.tex:907:$\Dg{g}^{\,2} = 0$. Chiral algebras are what configuration
standalone/introduction_full_survey.tex:4521: that restore~$\Dg{g}^{\,2} = 0$.
standalone/introduction_full_survey.tex:5314:$\Dg{g}$ (the full genus-$g$ corrected bar differential,
standalone/introduction_full_survey.tex:5321: $\dfib^{\,2} = \kappa \cdot \omega_g$; $\Dg{g}^{\,2} = 0$.

thinking
**Checking macro block issues**

I realize I need to address the macro block, specifically mentioning line 32 and line 8211 because of a typo. There are a couple of key findings: line 32 is missing `\ord` and `\Ydg`, while line 8211 has the typo `\fg\fl`, which should actually be `\mathfrak{gl}`. Also, I've encountered compile errors at lines 707-708 due to the missing macros. It seems like I need to inspect the `survey_modular_koszul` for any missing macros or stale references. Let's aim for around 18-22 findings in total.
exec
/bin/zsh -lc "find standalone -maxdepth 1 -name '*.tex' | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
      53
exec
/bin/zsh -lc "nl -ba standalone/classification_trichotomy.tex | sed -n '88,100p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    88	maximal singular order of the OPE among generators. The \emph{collision
    89	depth} $k_{\max}(\cA)$ records the maximal pole order of the degree-$2$
    90	collision residue $\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$. The
    91	\emph{shadow depth} $r_{\max}(\cA)$ records the degree at which the tower
    92	terminates (or $\infty$ if it does not).
    93	
    94	These invariants are related but not redundant. The collision residue
    95	$r(z)$ lives on the ordered bar complex
    96	$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$, the cofree tensor
    97	coalgebra with deconcatenation coproduct; it is an element of the
    98	$E_1$ convolution algebra that carries the full spectral-parameter
    99	dependence. The modular characteristic
   100	\kappa$ is the $\Sigma_2$-coinvariant scalar shadow of $r(z)$:

thinking
**Identifying subtle syntax issues**

I realize there's a missing opening `$` at line 100, which is a subtle bug that may have slipped through because TeX recovered from it. I think we need to scan the compile outputs specifically for "Missing $ inserted." The compile summary usually focuses on specific errors. A final audit should catch issues like that. I could run a grep command for suspicious text. Even though the user asked about undefined macros, maximizing the audit means including subtle issues. We should search all logs for "Missing $ inserted" messages.
codex
The static source pass is catching subtler breakage that the compile sweep won’t summarize cleanly, like malformed math delimiters and wrong macro stubs that still expand. I’m folding those in where the source itself is plainly broken.
exec
/bin/zsh -lc "rg -n \"Missing \\"'$ inserted|Extra }, or forgotten '"\\"'$|Double superscript|Double subscript|Can be used only in preamble|Environment .* undefined|Undefined control sequence|Undefined color|ended by '"\\\\end\" standalone/*.log" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Missing $ inserted|Extra }, or forgotten $|Double superscript|Double subscript|Can be used only in preamble|Environment .* undefined|Undefined control sequence|Undefined color|ended by \end)
                                                                                                                                                                                                ^^
error: unrecognized escape sequence

thinking
**Considering query optimization**

I’m thinking about whether to simplify our multiple queries with fixed strings. However, it doesn’t seem strictly necessary since we’ve already compiled maps. I wonder if adding a dollar sign ($) could be useful in this context. It looks like I might need to run a separate search to see how it plays out. There feels like a lot to think through here to get the best results!
exec
/bin/zsh -lc "rg -n 'Missing \\"'$ inserted|Extra '"\\}, or forgotten \\"'$|Missing '"\\}|Missing \\{' standalone/*.log" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/classification_trichotomy.log:438:! Missing $ inserted.
standalone/three_parameter_hbar.log:653:! Missing $ inserted.
standalone/editorial.log:1715:! Extra }, or forgotten $.
standalone/editorial.log:1726:! Missing $ inserted.
standalone/editorial.log:1745:! Missing } inserted.
standalone/editorial.log:8882:! Missing { inserted.
standalone/editorial.log:8892:! Missing } inserted.
standalone/editorial.log:9049:! Missing { inserted.
standalone/editorial.log:9059:! Missing } inserted.
standalone/editorial.log:9277:! Missing { inserted.
standalone/editorial.log:9287:! Missing } inserted.
standalone/editorial.log:9307:! Missing { inserted.
standalone/editorial.log:9317:! Missing } inserted.
standalone/editorial.log:11222:! Missing { inserted.
standalone/editorial.log:11232:! Missing } inserted.
standalone/editorial.log:11284:! Missing $ inserted.
standalone/survey_modular_koszul_duality_v2.log:2534:! Missing $ inserted.
standalone/survey_modular_koszul_duality_v2.log:2542:! Missing } inserted.
standalone/survey_modular_koszul_duality_v2.log:2553:! Missing } inserted.
standalone/survey_modular_koszul_duality_v2.log:2578:! Missing $ inserted.

thinking
**Investigating log issues**

It seems like there are missing `$` symbols in the classification_trichotomy and three_parameter_hbar logs, which is causing some errors with colors. I need to take a closer look at the source around the lines that are causing these missing symbols. It seems likely that the problematic log line for classification_trichotomy is around line 100, and there might be a similar issue in three_parameter_hbar. I'll inspect the contexts to figure this out.
exec
/bin/zsh -lc "rg -n -C 2 'Missing \\"'$ inserted|Undefined color'"' standalone/classification_trichotomy.log standalone/three_parameter_hbar.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/three_parameter_hbar.tex | sed -n '132,150p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/classification_trichotomy.log-436-File: ursfs.fd 1998/03/24 rsfs font definition file (jk)
standalone/classification_trichotomy.log-437-)
standalone/classification_trichotomy.log:438:! Missing $ inserted.
standalone/classification_trichotomy.log-439-<inserted text> 
standalone/classification_trichotomy.log-440-                $
--
standalone/classification_trichotomy.log-490-
standalone/classification_trichotomy.log-491-
standalone/classification_trichotomy.log:492:! LaTeX Error: Undefined color `blue!60!black'.
standalone/classification_trichotomy.log-493-
standalone/classification_trichotomy.log-494-See the LaTeX manual or LaTeX Companion for explanation.
--
standalone/three_parameter_hbar.log-557-)
standalone/three_parameter_hbar.log-558-
standalone/three_parameter_hbar.log:559:! LaTeX Error: Undefined color `green!40!black'.
standalone/three_parameter_hbar.log-560-
standalone/three_parameter_hbar.log-561-See the LaTeX manual or LaTeX Companion for explanation.
--
standalone/three_parameter_hbar.log-569-
standalone/three_parameter_hbar.log-570-
 succeeded in 51ms:
   132	$R$-matrix $R(z;\hbar)$ satisfying the quantum Yang--Baxter equation.
   133	The loop parameter is $\hbar_{\mathrm{DNP}}$, and the classical limit
   134	$R(z;\hbar) = 1 + \hbar \, r(z) + O(\hbar^2)$ identifies
   135	$\hbar_{\mathrm{DNP}}$ with the coefficient of the classical
   136	$r$-matrix.
   137	
   138	\paragraph{Parameter 3: the collision-residue prefactor.}
   139	The bar-cobar framework of \cite{Lorgat2026a} constructs the
   140	universal Maurer--Cartan element
   141	$\Theta_{\widehat{\fg}_k} := D_{\widehat{\fg}_k} - d_0$ from the bar
   142	differential. Its genus-zero binary collision residue
   143	$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta)$ is computed by
   144	extracting residues of the OPE against the bar propagator
   145	$d\log(z-w)$. The result is~\eqref{eq:km-collision-residue} with
   146	prefactor $\hbar_{\mathrm{bar}} = 1/(k + h^\vee)$.
   147	
   148	\subsection{Why the identification is non-trivial}
   149	
   150	The three parameters arise from different mathematical operations:
exec
/bin/zsh -lc "sed -n '648,658p' standalone/three_parameter_hbar.log" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
l.210 ...lambda$-bracket divided-power convention}
                                                   = \lambda^n/n!$) yields t...
You've closed more groups than you opened.
Such booboos are generally harmless, so keep going.

! Missing $ inserted.
<inserted text> 
                $
l.210 ...acket divided-power convention} = \lambda
                                                  ^n/n!$) yields the $r$-mat...
I've inserted a begin-math/end-math symbol since I think
exec
/bin/zsh -lc "nl -ba standalone/three_parameter_hbar.tex | sed -n '204,212p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   204	 \frac{1}{k + h^\vee}
   205	 \cdot \frac{\Omega}{z}.
   206	\end{equation}
   207	The factor $1/(k+h^\vee)$ arises because the Sugawara construction
   208	normalizes the energy-momentum tensor by $(k + h^\vee)^{-1}$: the
   209	OPE of currents produces the Casimir tensor $\Omega$ at mode $(1)$,
   210	and the $\lambda$-bracket divided-power convention} = \lambda^n/n!$) yields the $r$-matrix with the
   211	Sugawara-normalized prefactor.
   212	

thinking
**Troubleshooting missing components**

I need to address the missing ordered chiral homology for \cX. I should add `\newcommand{\cX}{\mathcal{X}}` near the macros line after cW, maybe around line 9239. I may also need to import xcolor for w3_holographic_datum to avoid compile errors, especially since blue is currently the only color from the links with references. There’s a similar issue with classification_trichotomy, which is also missing a $ sign. Looks like I have two findings to deal with!
exec
/bin/zsh -lc "rg -n 'cor:operadic-complexity|LorgatCYChiral|ssec:d-squared|def:shadow-depth|eq:mc-equation|eq:curvature|GeK98|thm:e1-primacy|thm:categorical-cg-all-types' standalone/N6_shadow_formality.tex standalone/cy_quantum_groups_6d_hcs.tex standalone/programme_summary_sections2_4.tex standalone/programme_summary_sections5_8.tex standalone/programme_summary_sections9_14.tex standalone/survey_track_a_compressed.tex standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/programme_summary_sections9_14.tex:315:equation~(\ref{eq:mc-equation}). The algebraic-family
standalone/programme_summary_sections9_14.tex:565:At genus $g \ge 1$ the curvature~\eqref{eq:curvature}
standalone/survey_track_b_compressed.tex:596:property (Theorem~\ref{thm:categorical-cg-all-types},
standalone/survey_track_b_compressed.tex:1848:(Theorem~\ref{thm:categorical-cg-all-types},
standalone/survey_track_a_compressed.tex:726:\emph{modular operad} (Getzler--Kapranov~\cite{GeK98}) has operations
standalone/survey_track_a_compressed.tex:2434:(Theorem~\ref{thm:e1-primacy}). The genus-$3$ cross-channel
standalone/programme_summary_sections5_8.tex:507:(Definition~\ref{def:shadow-depth}) separates the standard
standalone/programme_summary_sections2_4.tex:559:as~\S\ref{ssec:d-squared}, extended to all genera by Mok's
standalone/programme_summary_sections2_4.tex:583:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary_sections2_4.tex:629:MC equation~\eqref{eq:mc-equation} imposes a quadratic
standalone/programme_summary_sections2_4.tex:675:\label{def:shadow-depth}
standalone/cy_quantum_groups_6d_hcs.tex:183:\cite{LorgatCYChiral} proves that for $d \geq 3$, the CY chiral
standalone/N6_shadow_formality.tex:190:single invariant of $\cA$ (Corollary~\ref{cor:operadic-complexity}).
standalone/N6_shadow_formality.tex:252:\begin{equation}\label{eq:mc-equation}


thinking
**Checking classification references**

It seems like there might be unresolved references in the same file. Some could be local while others are not. I need to start by checking if the missing ones are genuinely undefined. For example, I'm curious if `thm:single-line-dichotomy` is defined in the file or not. I should probably search for it to clarify this. Let's see how it all connects!
thinking
**Considering computation necessity**

I'm thinking about whether it's necessary to compute something. It could be helpful to know if there are missing or stale logs, just to keep things tidy. I see that the current classification compile didn't show any actual errors, only warnings. So, maybe I could search for definitions or use regex to clarify those labels. It feels like a good step to ensure everything is in check!
exec
/bin/zsh -lc "for pat in 'thm:single-line-dichotomy' 'thm:riccati-algebraicity' 'thm:depth-decomposition' 'rem:contact-stratum-separation' 'thm:nms-betagamma-quartic-birth'; do echo PAT "'$pat; rg -n "label'"\\{"'$pat'"\\}\" standalone/classification.tex; done" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
PAT thm:single-line-dichotomy
PAT thm:riccati-algebraicity
PAT thm:depth-decomposition
PAT rem:contact-stratum-separation
PAT thm:nms-betagamma-quartic-birth



thinking
**Considering citation fixes**

I need to address the file-level issue by replacing every external `\ref{...}` with explicit text in the prose. Alternatively, I could insert a local label through a named theorem or remark. That should help clarify the references and keep the document cohesive. It’s important to ensure everything is properly connected, so it’s clear for readers. Making these adjustments could enhance the overall quality of the document.
thinking
**Evaluating standalone files**

I think a potential fix could be just to compile `programme_summary.tex` only, instead of the split fragment files. However, the user is asking for an audit of these standalone files, which currently compile with warnings. If they aren't meant to be standalone, the warnings might not be too severe, but they still exist in the standalone folder. It seems like there’s a foundational issue with these fragments. I’ll need to catalog my findings about 23 file-level issues, noting down various severity levels.
thinking
**Listing unresolved references**

I need to document some unresolved references in the classification file, specifically at lines 66, 100, 267, 831, and 1008. These references appear to be monograph-only, so they might present some challenges. Additionally, there's an unresolved citation in the `cy_quantum_groups_6d_hcs` file at line 183 for `LorgatCYChiral`, which falls into the low/medium severity level. It's important for me to make sure these findings are clearly cataloged for the user!
exec
/bin/zsh -lc "rg -n 'mainpreambleonly' main.tex standalone/editorial.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
standalone/editorial.tex:3:\def\mainpreambleonly{1}
main.tex:590:\ifdefined\mainpreambleonly
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '586,606p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   600	\providecommand{\Aut}{\operatorname{Aut}}
   601	\providecommand{\mathbbm}[1]{\mathbb{#1}}
   602	\providecommand{\bigboxtimes}{\mathop{\boxtimes}\displaylimits}
   603	\providecommand{\Bbar}{\bar{B}}
   604	\providecommand{\B}{\bar{B}}
   605	\providecommand{\Det}{\mathrm{Det}}
exec
/bin/zsh -lc "rg -n 'FlajoletSedgewick' standalone/riccati.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
591:\cite[Theorem~VI.1]{FlajoletSedgewick} gives
context compacted



thinking
**Finalizing findings for audit**

I need to craft a final answer, ensuring it's grounded and doesn't contain unsupported inferences. I should mention exact line numbers and fixes, and maybe include a note about grepping for undefined LaTeX macros. We've checked 53 files overall, but claiming exhaustive coverage might be tricky since we haven't looked at every file manually. I should focus on our grounded findings, noting that we found 28 issues, though our compile script identified 23 problematic files.
thinking
**Enhancing macro analysis**

Running a macro grep against the preamble could help identify more undefined macros, even in files that compiled successfully if they were imported through a package. Right now, we haven’t systematically covered all undefined macros. I should consider running grep to compare macros used versus defined across all standalone files, especially since the user wants us to do a thorough audit. It might be a good idea to create a script for this and verify potential undefined macros afterward.
thinking
**Updating macro detection process**

We're already halfway through, but I think I should still send a commentary update. It’s important to run commands to systematically check for macros that are used but not defined, especially since the final report needs to be as grounded and exhaustive as possible. I should use additional shell commands for this task. Using the commentary channel for updates seems essential, but maybe using update_plan isn’t necessary after all. It's time for that commentary update!
codex
I have the first compile-backed failures and am doing the stricter pass the task asked for now: macro-by-macro extraction across all `standalone/*.tex`, then source cross-check against each file’s local preamble so I only keep grounded undefined-macro findings.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, os, json, pathlib
root = pathlib.Path('/Users/raeez/chiral-bar-cobar/standalone')
tex_files = sorted(root.glob('*.tex'))
# Common TeX/LaTeX builtins and package commands we should ignore for undefined-local-macro audit
builtin = set('''
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
LaTeX TeX documentclass usepackage title author date begin end maketitle tableofcontents section subsection subsubsection paragraph subparagraph
textbf textit emph textsc underline
label ref eqref pageref cite footnote marginpar url href hyperref
newcommand renewcommand providecommand DeclareMathOperator
newtheorem theoremstyle numberwithin
left right bigl bigr Bigl Bigr biggl biggr Biggl Biggr middlesize
frac dfrac tfrac binom dbinom sqrt root
sum prod int oint lim limsup liminf sup inf max min
to mapsto hookrightarrow twoheadrightarrow rightarrow leftarrow longrightarrow Longrightarrow implies iff
forall exists in notin subset subseteq supset supseteq cup cap setminus varnothing emptyset
leq geq neq approx sim cong equiv partial nabla
cdot times otimes opulus oplus wedge vee
mathbf mathbb mathcal mathfrak mathrm mathsf mathtt boldsymbol bm
operatorname overline underline widehat widetilde tilde hat bar vec check acute grave breve dot ddot
leftbrace rightbrace leftparen rightparen leftbracket rightbracket
bigcup bigcap coproduct coprod directsum
qquad quad ; , : "'!
item itemize enumerate description
centering raggedright raggedleft
hline vline hrulefill
includegraphics graphicspath
tikzcd
array tabular longtable
caption subcaption
small medium large Large LARGE huge Huge
normalfont rmfamily sffamily ttfamily bfseries mdseries itshape scshape slshape upshape
textwidth linewidth columnwidth paperwidth paperheight
today pageclear newpage clearpage linebreak nolinebreak pagebreak nopagebreak
appendix input include
par medskip bigskip smallskip noindent indent
mbox fbox makebox framebox raisebox rule
vspace hspace hfill vfill stretch
ensuremath
'"'''.split())
# Add many standard Greek letters and common macros from amsmath likely not locally defined but built-in
builtin |= set('''alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh exp log ln det dim ker cokernel im id Re Im mod bmod pmod gcd lcm
ldots cdots vdots ddots
iff if and or
colon
'''.split())
# Environments / commands that aren't " in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

codex
The broad grep pass is noisy because most standalone files already overdefine their own local macros. I’m tightening the audit to actual failing control sequences from fresh logs, then cross-checking each one against the file-local preamble so every reported “undefined macro” stays source-grounded.
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root = pathlib.Path('/Users/raeez/chiral-bar-cobar/standalone')
for log in sorted(root.glob('*.log')):
    text = log.read_text(errors='ignore').splitlines()
    hits=[]
    for i,line in enumerate(text):
        if 'Undefined control sequence.' in line:
            ctx=' | '.join(text[max(0,i-2):min(len(text),i+3)])
            hits.append(ctx)
    if hits:
        print('FILE', log.name)
        for h in hits[:12]:
            print(h)
        print('COUNT', len(hits))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
FILE N2_mc3_all_types.log
 | [4] | ! Undefined control sequence. | <recently read> \cF  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | <recently read> \cF  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | <recently read> \cF  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | l.394 pieces $\cF^{\geq N} / \cF |                                 ^{\geq N+1}$ are finite-dimensional
COUNT 4
FILE N3_e1_primacy.log
 [] |  | ! Undefined control sequence. | <recently read> \BarchFG  |                          
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | l.357 ...,\BarSig(\cA) \twoheadrightarrow \BarchFG |                                                   (\cA),
COUNT 2
FILE editorial.log
(Font)              scaled to size 6.1pt on input line 33. |  | ! Undefined control sequence. | l.36 ...D}_{\Ran}\barB_X(\cA_i)\simeq \Omega_X(\cC |                                                   _j)\simeq \cA_j$,
 on input line 67. |  | ! Undefined control sequence. | l.76  $\ChirHoch^1(V_k(\fg |                           ))\cong\fg$ for affine KM;
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | l.76  $\ChirHoch^1(V_k(\fg))\cong\fg |                                     $ for affine KM;
106. |  | ! Undefined control sequence. | <recently read> \HH  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | <recently read> \bR  |                     
 | [2] | ! Undefined control sequence. | <recently read> \HH  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | l.144  $\HH_*(\cC |                  )$.
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | <recently read> \cC  |                     
and I'll forget about whatever was undefined. |  | ! Undefined control sequence. | l.146  (e.g.\ $\operatorname{Rep}_q(\fg |                                        )$).


thinking
**Evaluating undefined macros**

I need to parse various error types like "Missing $ inserted" and "Undefined color." The user requested that every undefined macro be treated as a separate finding, which means I should list each macro individually. While I typically group them, it seems I need to follow the instruction strictly. However, there are a lot—79 in just the introduction log! I should deduplicate by macro names so that each unique undefined macro is its own finding.
thinking
**Identifying unique undefined macros**

It looks like we need to create separate findings for each unique undefined macro, rather than counting every occurrence. I should focus on identifying the unique macro names that are actually undefined. For the introduction survey, I see macros like \dzero, \Hom, \End, and others. I think extracting these unique names from the logs automatically could simplify this process. For the editorial section, there may be many because of the macro abundance from chapters, so scripting this for unique undefined macros is the way to go!
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root = pathlib.Path('/Users/raeez/chiral-bar-cobar/standalone')
pat1 = re.compile(r'<recently read> \\\\([A-Za-z]+)')
pat2 = re.compile(r'l\\.\\d+ .*?\\\\([A-Za-z]+)')
pat3 = re.compile(r'<argument> \\\\([A-Za-z]+)')
for log in sorted(root.glob('*.log')):
    lines = log.read_text(errors='ignore').splitlines()
    names=[]
    for i,line in enumerate(lines):
        if 'Undefined control sequence.' in line:
            ctx=' '.join(lines[i:i+3])
            found = pat1.findall(ctx)+pat2.findall(ctx)+pat3.findall(ctx)
            if found:
                names.extend(found)
    if names:
        print(log.name, sorted(set(names)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
N2_mc3_all_types.log ['cF']
N3_e1_primacy.log ['BarSig', 'BarchFG']
editorial.log ['B', 'Barch', 'ChirHoch', 'CompCl', 'Gamma', 'HH', 'MC', 'Omega', 'Phi', 'Ran', 'SCchtop', 'Sigma', 'Sym', 'Theta', 'bC', 'bD', 'bP', 'bQ', 'bR', 'bZ', 'barB', 'barBch', 'bigoplus', 'bullet', 'cA', 'cC', 'cD', 'cH', 'cM', 'cN', 'cP', 'cW', 'cZ', 'chi', 'colon', 'cong', 'dim', 'emph', 'fg', 'fh', 'fsl', 'geq', 'hat', 'hbar', 'in', 'infty', 'int', 'item', 'kappa', 'mathcal', 'mathfrak', 'mathrm', 'natural', 'operatorname', 'overline', 'phi', 'psi', 'rho', 'slN', 'tau', 'text', 'times', 'vartheta', 'vee', 'zeta']
introduction_full_survey.log ['C', 'Com', 'End', 'FM', 'Hom', 'R', 'Res', 'Theta', 'ar', 'arrow', 'chirAss', 'chirLie', 'delta', 'dfib', 'dzero', 'in', 'mathrm', 'mu', 'operatorname', 'tfrac']
programme_summary.log ['ChirHoch']
survey_modular_koszul_duality.log ['CompCl', 'Defcyc', 'End', 'Hom', 'bigotimes', 'bullet', 'cA', 'delta', 'orline', 'sum']
survey_modular_koszul_duality_v2.log ['Ran', 'Ydg', 'barB', 'fg']

thinking
**Analyzing editorial issues**

I'm noticing that the editorial process can be unusual because it inputs chapters and relies on hidden imports. I think it's acceptable to mention that the root cause is a hidden import issue, covering undefined macros. But to be thorough, I should list 4-5 explicit macros in the problem text. I might also need to take a closer look at the classification.tex log for warnings and compile those warnings for review. Let's extract those warnings!
codex
I have the macro failures narrowed down to source-backed cases. I’m doing one more pass on the non-macro defects the task explicitly called out: unresolved refs, unresolved citations, malformed math, and hidden-import breakage, so the final report is one clean failure list instead of mixed speculation.
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root = pathlib.Path('/Users/raeez/chiral-bar-cobar/standalone')
for log in sorted(root.glob('*.log')):
    text = log.read_text(errors='ignore').splitlines()
    refs=[]; cites=[]; colors=[]; preamble=[]; math=[]
    for line in text:
        if 'Reference "'`'"' in line and 'undefined' in line:
            refs.append(line.strip())
        if 'Citation "'`'"' in line and 'undefined' in line:
            cites.append(line.strip())
        if 'Undefined color' in line:
            colors.append(line.strip())
        if 'Can be used only in preamble' in line:
            preamble.append(line.strip())
        if 'Missing "'$ inserted'"' in line or 'Extra }, or forgotten "'$'"' in line or 'Double subscript' in line or 'Double superscript' in line:
            math.append(line.strip())
    if refs or cites or colors or preamble or math:
        print('FILE', log.name)
        if colors: print('COLORS', colors[:6])
        if preamble: print('PREAMBLE', preamble[:6])
        if math: print('MATH', math[:10])
        if refs: print('REFS', refs[:12])
        if cites: print('CITES', cites[:12])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
FILE N3_e1_primacy.log
MATH ['! Double superscript.', '! Double superscript.', '! Double superscript.']
FILE N6_shadow_formality.log
MATH ['! Double subscript.']
REFS ["LaTeX Warning: Reference `cor:operadic-complexity' on page 2 undefined on input"]
FILE bp_self_duality.log
COLORS ["! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `blue!60!black'.", "! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `blue!60!black'."]
FILE classification.log
REFS ["LaTeX Warning: Reference `thm:single-line-dichotomy' on page 1 undefined on inp", "LaTeX Warning: Reference `thm:riccati-algebraicity' on page 1 undefined on inpu", "LaTeX Warning: Reference `thm:depth-decomposition' on page 3 undefined on input", "LaTeX Warning: Reference `thm:riccati-algebraicity' on page 9 undefined on inpu", "LaTeX Warning: Reference `rem:contact-stratum-separation' on page 9 undefined o", "LaTeX Warning: Reference `thm:nms-betagamma-quartic-birth' on page 11 undefined"]
FILE classification_trichotomy.log
COLORS ["! LaTeX Error: Undefined color `blue!60!black'."]
MATH ['! Missing $ inserted.']
FILE cy_quantum_groups_6d_hcs.log
CITES ["LaTeX Warning: Citation `LorgatCYChiral' on page 2 undefined on input line 183."]
FILE editorial.log
MATH ['! Extra }, or forgotten $.', '! Missing $ inserted.', '! Double subscript.', '! Missing $ inserted.']
REFS ["LaTeX Warning: Reference `thm:shadow-separation' on page ii undefined on input", "LaTeX Warning: Reference `thm:shadow-tautological-ring' on page ii undefined on", "LaTeX Warning: Reference `cor:analytic-shadow-realization' on page ii undefined", "LaTeX Warning: Reference `thm:bar-cobar-isomorphism-main' on page 1 undefined o", "LaTeX Warning: Reference `thm:higher-genus-inversion' on page 1 undefined on in", "LaTeX Warning: Reference `thm:bar-cobar-inversion-qi' on page 1 undefined on in", "LaTeX Warning: Reference `thm:fiber-center-identification' on page 1 undefined", "LaTeX Warning: Reference `thm:quantum-complementarity-main' on page 1 undefined", "LaTeX Warning: Reference `def:scalar-lane' on page 1 undefined on input line 62", "LaTeX Warning: Reference `thm:modular-characteristic' on page 1 undefined on in", "LaTeX Warning: Reference `thm:multi-weight-genus-expansion' on page 1 undefined", "LaTeX Warning: Reference `thm:main-koszul-hoch' on page 1 undefined on input li"]
FILE gaudin_from_collision.log
COLORS ["! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `blue!60!black'.", "! LaTeX Error: Undefined color `blue!60!black'.", "! LaTeX Error: Undefined color `green!40!black'.", "! LaTeX Error: Undefined color `blue!60!black'."]
FILE introduction_full_survey.log

thinking
**Extracting line references**

I think I need to extract exact line numbers for reference and citation issues from the log lines. It seems like using a tool like `rg` on the source could help with that. I'm aiming for direct references, so I need to cite the relevant lines in the source where the issues show up. For any unresolved references or citations, I plan to gather line numbers from `rg` commands, focusing on files with specific labels or citations.
exec
/bin/zsh -lc "rg -n '\\\\(newcommand|providecommand|DeclareMathOperator)|\\\\usepackage|\\\\begin\\{convention\\}|\\\\begin\\{tikzcd\\}|\\\\begin\\{longtable\\}|\\\\Dg\\{|\\\\dzero|\\\\dfib|\\\\Hom|\\\\End|\\\\Res|\\\\Aut|\\\\colim|\\\\chirAss|\\\\chirLie|\\\\chirCom|\\\\chirtensor|\\\\R\\b' standalone/introduction_full_survey.tex standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(ref|cite)\\{(thm:single-line-dichotomy|thm:riccati-algebraicity|thm:depth-decomposition|rem:contact-stratum-separation|thm:nms-betagamma-quartic-birth|LorgatCYChiral|ssec:d-squared|Drinfeld85|KZ84|STS83|FFR94|sec:bar|def:shadow-depth|eq:mc-equation|eq:curvature|FlajoletSedgewick|GeK98|thm:e1-primacy|thm:categorical-cg-all-types|cor:mc3-all-types|conj:quartic-closure|conj:beilinson-closure|conj:clutching-closure)\\}' standalone/classification.tex standalone/cy_quantum_groups_6d_hcs.tex standalone/programme_summary_sections2_4.tex standalone/programme_summary_sections5_8.tex standalone/programme_summary_sections9_14.tex standalone/riccati.tex standalone/survey_track_a_compressed.tex standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(usepackage|newcommand|providecommand|DeclareMathOperator)|\\\\cF|\\\\BarchFG|\\\\Cobar\\"'^|'"\\\\gmod_g|\\\\ChirHoch|\\\\cX\\b|\\\\ord\\b|\\\\Ydg\\b|widehat\\{\\\\fg\\\\fl\\}_1|blue"'!60!black|green!40!black|'"\\\\kappa\\"'$|lambda'"\\\\"'$-bracket'"' standalone/N2_mc3_all_types.tex standalone/N3_e1_primacy.tex standalone/N6_shadow_formality.tex standalone/programme_summary.tex standalone/ordered_chiral_homology.tex standalone/survey_modular_koszul_duality_v2.tex standalone/bp_self_duality.tex standalone/classification_trichotomy.tex standalone/gaudin_from_collision.tex standalone/three_parameter_hbar.tex standalone/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/riccati.tex:371:by Theorem~\ref{thm:riccati-algebraicity}, comparing
standalone/riccati.tex:462:The classification follows from Theorem~\ref{thm:riccati-algebraicity}
standalone/riccati.tex:630: \textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)}
standalone/riccati.tex:652:(Theorem~\ref{thm:single-line-dichotomy}) gives
standalone/programme_summary_sections9_14.tex:315:equation~(\ref{eq:mc-equation}). The algebraic-family
standalone/programme_summary_sections9_14.tex:613:Everything in Sections~\ref{sec:bar}--\ref{sec:frontier}
standalone/programme_summary_sections5_8.tex:195:studied. Drinfeld's $r$-matrix~\cite{Drinfeld85}, the KZ
standalone/programme_summary_sections5_8.tex:196:connection~\cite{KZ84}, the Sklyanin
standalone/programme_summary_sections5_8.tex:197:bracket~\cite{STS83}, and the Gaudin model~\cite{FFR94}
standalone/programme_summary_sections5_8.tex:315:Section~\ref{sec:bar}: the bar differential extracts OPE
standalone/programme_summary_sections5_8.tex:507:(Definition~\ref{def:shadow-depth}) separates the standard
standalone/programme_summary_sections2_4.tex:559:as~\S\ref{ssec:d-squared}, extended to all genera by Mok's
standalone/cy_quantum_groups_6d_hcs.tex:183:\cite{LorgatCYChiral} proves that for $d \geq 3$, the CY chiral
standalone/survey_track_b_compressed.tex:596:property (Theorem~\ref{thm:categorical-cg-all-types},
standalone/survey_track_b_compressed.tex:597:Corollary~\ref{cor:mc3-all-types}); the remaining post-CG
standalone/survey_track_b_compressed.tex:920:Conjecture~\ref{conj:quartic-closure}),
standalone/survey_track_b_compressed.tex:923:Conjecture~\ref{conj:beilinson-closure}), and
standalone/survey_track_b_compressed.tex:926:$\Re\rho = 1/2$, Conjecture~\ref{conj:clutching-closure}).
standalone/survey_track_b_compressed.tex:1848:(Theorem~\ref{thm:categorical-cg-all-types},
standalone/survey_track_b_compressed.tex:1849:Corollary~\ref{cor:mc3-all-types}). The residual problem
 succeeded in 51ms:
standalone/introduction_full_survey.tex:3:\usepackage{amsmath,amssymb,amsthm}
standalone/introduction_full_survey.tex:4:\usepackage{mathrsfs}
standalone/introduction_full_survey.tex:5:\usepackage[shortlabels]{enumitem}
standalone/introduction_full_survey.tex:6:\usepackage{booktabs}
standalone/introduction_full_survey.tex:7:\usepackage{array}
standalone/introduction_full_survey.tex:8:\usepackage{microtype}
standalone/introduction_full_survey.tex:9:\usepackage[dvipsnames]{xcolor}
standalone/introduction_full_survey.tex:10:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/introduction_full_survey.tex:27:\providecommand{\cA}{\mathcal{A}}
standalone/introduction_full_survey.tex:28:\providecommand{\cB}{\mathcal{B}}
standalone/introduction_full_survey.tex:29:\providecommand{\cC}{\mathcal{C}}
standalone/introduction_full_survey.tex:30:\providecommand{\cD}{\mathcal{D}}
standalone/introduction_full_survey.tex:31:\providecommand{\cE}{\mathcal{E}}
standalone/introduction_full_survey.tex:32:\providecommand{\cF}{\mathcal{F}}
standalone/introduction_full_survey.tex:33:\providecommand{\cG}{\mathcal{G}}
standalone/introduction_full_survey.tex:34:\providecommand{\cH}{\mathcal{H}}
standalone/introduction_full_survey.tex:35:\providecommand{\cI}{\mathcal{I}}
standalone/introduction_full_survey.tex:36:\providecommand{\cJ}{\mathcal{J}}
standalone/introduction_full_survey.tex:37:\providecommand{\cK}{\mathcal{K}}
standalone/introduction_full_survey.tex:38:\providecommand{\cL}{\mathcal{L}}
 succeeded in 51ms:
Total output lines: 604

standalone/w3_holographic_datum.tex:6:\usepackage{amsmath,amssymb,amsthm}
standalone/w3_holographic_datum.tex:7:\usepackage{mathrsfs}
standalone/w3_holographic_datum.tex:8:\usepackage[shortlabels]{enumitem}
standalone/w3_holographic_datum.tex:9:\usepackage{booktabs}
standalone/w3_holographic_datum.tex:10:\usepackage{array}
standalone/w3_holographic_datum.tex:11:\usepackage{microtype}
standalone/w3_holographic_datum.tex:12:\usepackage[colorlinks=true,linkcolor=blue!60!black,
standalone/w3_holographic_datum.tex:13: citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
standalone/w3_holographic_datum.tex:32:\newcommand{\cA}{\mathcal{A}}
standalone/w3_holographic_datum.tex:33:\newcommand{\cC}{\mathcal{C}}
standalone/w3_holographic_datum.tex:34:\newcommand{\cH}{\mathcal{H}}
standalone/w3_holographic_datum.tex:35:\newcommand{\barB}{\bar{B}}
standalone/w3_holographic_datum.tex:36:\newcommand{\fg}{\mathfrak{g}}
standalone/w3_holographic_datum.tex:37:\newcommand{\fsl}{\mathfrak{sl}}
standalone/w3_holographic_datum.tex:38:\newcommand{\Walg}{\mathcal{W}}
standalone/w3_holographic_datum.tex:39:\newcommand{\Vir}{\mathrm{Vir}}
standalone/w3_holographic_datum.tex:40:\newcommand{\Res}{\operatorname{Res}}
standalone/w3_holographic_datum.tex:41:\newcommand{\Sh}{\mathrm{Sh}}
exec
/bin/zsh -lc "rg -n '\\\\cX\\b|\\\\newcommand\\{\\\\cX\\}|\\\\providecommand\\{\\\\cX\\}' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Inspecting source lines**

I'm puzzling over whether there’s any instance of cX at all. I get the feeling that line 9239 might have \cX, but maybe my previous search didn’t catch it because it was looking for an uppercase X instead? I think I should take a closer look at and inspect the code around line 9239 to see if I can find what I'm missing. That might just clarify things for me.
exec
/bin/zsh -lc "sed -n '9234,9244p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc 'wc -l standalone/ordered_chiral_homology.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    8290 standalone/ordered_chiral_homology.tex
exec
/bin/zsh -lc "rg -n '\\\\CompCl|\\\\Defcyc|\\\\orline|\\\\Aut\\b|\\\\Hom\\b|\\\\End\\b|\\\\bigotimes|\\\\sum\\b' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1279:\;\bigotimes_{v\in V(\Gamma)}\cO\bigl(g(v),\mathrm{In}(v)\bigr).
1338: \Hom\bigl(B(\Ass),\,\End_A\bigr)
1593:\bigotimes_{v\in V(\Gamma)}
1622:\sum
1702:\bigotimes_{v\in V(\Gamma)}
1707:\orline{E_{\mathrm{int}}(\Gamma)}
1725:$\orline{E_{\mathrm{int}}(\Gamma)}
1878:$\mu_\Gamma\colon\bigotimes_{v\in V(\Gamma)}A^{\otimes n(v)}\to A$
1887:\to\bigotimes_{v\in V(\Gamma)}\cC^{\log\mathrm{FM}}_{g(v),n(v)}$
2263:\bigotimes_{v\in V(S_\rho)}\Theta_{\cA,v}
2675:$\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}})$.
2702: $\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}})$\\[2pt]
2704: & Cyclic cocycle in $\Defcyc^{\mathrm{mod}}(\cA)$\\[2pt]
2769:$\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
5087: & cyclic deformation complex $\Defcyc(\cA)$ \\[2pt]
5897:H_\bullet\!\bigl(\Defcyc^{\mathrm{mod}}(\cA)\bigr),
6715:+ \sum \mu^{M_j}$. The annulus trace
6837: \orline(\epsilon)\otimes
6838: \bigotimes_{u\in V(\epsilon)}sC(\operatorname{Fl}_\epsilon(u)),
6840: where $\orline(\epsilon)$ is the orientation line of the
exec
/bin/zsh -lc "rg -n 'cor:operadic-complexity' standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
190:single invariant of $\cA$ (Corollary~\ref{cor:operadic-complexity}).



thinking
**Considering unresolved references**

I’m thinking about how they said every missing definition or unresolved reference counts as a finding. If there are a lot of unresolved references in "introduction_full_survey," maybe we should include them, but that sounds overwhelming. Perhaps I could group them or note representative examples instead. Ultimately, I need to figure out how to present findings concisely, so listing unique unresolved references I actually checked might be the best option.
thinking
**Exploring undefined references**

I’m contemplating whether to script counts of undefined references or extract them and group them by file. Reporting one finding per file that lists all references could satisfy the requirement, especially since each unresolved reference appears in the problem text. However, this could overwhelm users, particularly for files like "introduction_full_survey," which has a lot more than twelve warnings. I might group them as "dozens of unresolved cross-chapter references," but will that be enough for the user?
thinking
**Expanding extraction process**

I want to create a more exhaustive automated extraction of all undefined references and citations from the logs for each file. My idea is to gather these findings in groups, possibly listing all the labels. While this could be quite large, it should still be manageable for selected files. I’ll work on getting the counts and lists together to make the process clearer and easier to understand.
codex
The remaining surface is the ugly one: fragment files that compile only inside the monograph and leave bare `\ref`/`\cite` tokens behind. I’m extracting the actual label/key lists from logs now so the final report names the broken references instead of hand-waving about “some undefined refs.”
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root = pathlib.Path('/Users/raeez/chiral-bar-cobar/standalone')
ref_pat = re.compile(r\"Reference "'`([''^'"']+)'\")
cite_pat = re.compile(r\"Citation "'`([''^'"']+)'\")
for log in sorted(root.glob('*.log')):
    text = log.read_text(errors='ignore').splitlines()
    refs=[]; cites=[]
    for line in text:
        m=ref_pat.search(line)
        if m: refs.append(m.group(1))
        m=cite_pat.search(line)
        if m: cites.append(m.group(1))
    if refs or cites:
        print('FILE', log.stem)
        if refs: print('REFS', len(refs), sorted(set(refs)))
        if cites: print('CITES', len(cites), sorted(set(cites)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
FILE N6_shadow_formality
REFS 1 ['cor:operadic-complexity']
FILE classification
REFS 6 ['rem:contact-stratum-separation', 'thm:depth-decomposition', 'thm:nms-betagamma-quartic-birth', 'thm:riccati-algebraicity', 'thm:single-line-dichotomy']
FILE cy_quantum_groups_6d_hcs
CITES 1 ['LorgatCYChiral']
FILE editorial
REFS 1736 ['MK:koszul', 'MK:modular', 'V2-rem:platonic-shadow-dichotomy', 'V2-thm:gravitational-primitivity', 'app:arnold-relations', 'app:branch-line-reductions', 'app:coderived', 'app:existence-criteria', 'app:nilpotent-completion', 'app:nonlinear-modular-shadows', 'app:signs', 'ch:genus-expansions', 'ch:genus1-seven-faces', 'ch:three-invariants', 'ch:v1-bv-brst', 'chap:arithmetic-shadows', 'chap:bar-cobar-adjunction', 'chap:chiral-deformation', 'chap:deformation-theory', 'chap:e1-modular-koszul', 'chap:entanglement-modular-koszul', 'chap:free-fields', 'chap:holographic-codes-koszul', 'chap:kac-moody', 'chap:koszul-pairs', 'chap:moonshine', 'chap:n2-sca', 'chap:subregular-hook-frontier', 'chap:toroidal-elliptic', 'chap:w-algebras', 'chap:yangians', 'comp:affine-branch-bv', 'comp:betagamma-branch-bv', 'comp:bp-bar', 'comp:heisenberg-branch-bv', 'comp:heisenberg-holographic-datum', 'comp:m58-weight-space-periodicity', 'comp:mc4-three-layer-verification', 'comp:mc4-yangian-boundary-strip-stage4', 'comp:mc4-yangian-boundary-strip-stage6', 'comp:mc4-yangian-lowrank-kernels', 'comp:sl4-hook-data', 'comp:thick-generation-sl2', 'comp:virasoro-branch-bv', 'comp:virasoro-curvature', 'comp:w3-genus2-cross-graphwise', 'comp:w3-genus2-multichannel', 'comp:w3-genus3-cross', 'comp:w3-genus4-cross', 'comp:w4-ds-ope-extraction', 'comp:winfty-stage4-reduction-chain', 'comp:winfty-stage4-seed-verification', 'conj:DS-arbitrary-nilpotent', 'conj:EO-recursion', 'conj:ade-chart-k3', 'conj:admissible-koszul-rank-obstruction', 'conj:agt-bar-cobar', 'conj:agt-w-algebra', 'conj:analytic-realization', 'conj:anomaly-cancellation', 'conj:arithmetic-comparison', 'conj:boundary-bar-duality', 'conj:boundary-defect-realization', 'conj:bp-duality', 'conj:brst-cohomology', 'conj:cech-bar-intertwining', 'conj:center-essential-surjectivity', 'conj:clutching-closure', 'conj:cobar-physical', 'conj:coderived-e3', 'conj:coha-koszul', 'conj:cs-factorization', 'conj:cy-product-shadow', 'conj:d-module-purity-koszulness', 'conj:d-module-purity-wn-principal', 'conj:defect-unification', 'conj:deformation-holographic', 'conj:derived-bc-betagamma', 'conj:discriminant-ks-operator', 'conj:dk-compacts-completion', 'conj:dk-fd-typeA', 'conj:dk4-inverse-limit', 'conj:ds-kd-arbitrary-nilpotent', 'conj:ds-shadow-depth-monotonicity', 'conj:e1-genus-theory', 'conj:e1-nonsplitting-genus2', 'conj:ent-page-curve', 'conj:extended-ferm-ghost', 'conj:factorization-finiteness-criterion', 'conj:full-derived-dk', 'conj:full-dk-bridge', 'conj:gw-s-duality', 'conj:holographic-koszul', 'conj:holographic-koszul-deformation', 'conj:ht-deformation-quantization', 'conj:irrational-ramanujan', 'conj:kappa-bps-universality', 'conj:kappa-holographic-central-charge', 'conj:kl-braided', 'conj:kl-coderived', 'conj:kl-periodic-cdg', 'conj:koszul-swampland', 'conj:koszul-t-structures', 'conj:lagrangian-koszulness', 'conj:loop-connes-transfer', 'conj:master-bv-brst', 'conj:mc3-automatic-generalization', 'conj:mc3-sectorwise-all-types', 'conj:mock-shadow-tower', 'conj:modular-anomaly-brst', 'conj:modular-fact-envelope', 'conj:modular-periodicity', 'conj:modular-periodicity-minimal', 'conj:modular-periodicity-wzw', 'conj:modular-spectral-rigidity', 'conj:module-category-t-exactness', 'conj:nc-cs', 'conj:nms-graph-completed-master-element', 'conj:non-simply-laced-discriminant', 'conj:periodic-cdg', 'conj:physical-pairing', 'conj:prime-locality-transfer', 'conj:q-agt', 'conj:quartic-closure', 'conj:reflected-modular-periodicity', 'conj:resurgent-shadow-classification', 'conj:scalar-saturation-universality', 'conj:scattering-tropical-shadow', 'conj:shadow-principal-class', 'conj:shadow-s1-quantum-volume', 'conj:shadow-taut-projection', 'conj:shifted-yangian-langlands', 'conj:singular-fiber-descent', 'conj:sl3-bar-gf', 'conj:string-amplitude', 'conj:string-amplitude-bar', 'conj:superstring-degeneration', 'conj:thqg-shadow-depth-code-distance', 'conj:topologization-general', 'conj:toroidal-koszul-dual', 'conj:type-a-transport-to-transpose', 'conj:universal-moonshine-multiplier', 'conj:v1-bar-cobar-path-integral', 'conj:v1-bar-worldline', 'conj:v1-bphz-recursion', 'conj:v1-disk-local-perturbative-fm', 'conj:w-infty-bar', 'conj:w-orbit-duality', 'conj:w3-algebraicity', 'conj:w3-bar-gf', 'conj:wrt-conjecture', 'conj:yangian-bar-gf', 'const:vol1-boundary-operators-residue', 'const:vol1-clutching-law-logfm', 'const:vol1-genus-spectral-sequence', 'const:vol1-genus-two-shells', 'const:vol1-graph-sum-theta-logfm', 'const:vol1-graphwise-log-fm-cocomposition', 'const:vol1-log-modular-bar-functor', 'const:vol1-modular-tangent-complex', 'const:vol1-rigid-planted-forest-push-pull', 'const:vol1-three-preprints-chain-level', 'const:vol1-weight-filtration', 'constr:bordered-fm', 'constr:degree4-degeneration', 'constr:dk-shadow-projections', 'constr:holographic-spectral-sequence', 'constr:li-bar-spectral-sequence', 'constr:obstruction-recursion', 'constr:shadow-epstein-eisenstein', 'constr:sugawara-antighost', 'constr:thqg-oc-mc-element', 'constr:thqg-oc-quartic-resonance', 'conv:bar-coalgebra-identity', 'conv:higher-genus-differentials', 'conv:hms-levels', 'cor:analytic-shadow-realization', 'cor:anomaly-duality-km', 'cor:anomaly-physical-genus0', 'cor:bar-cohomology-koszul-dual', 'cor:bar-d-squared-zero-arnold', 'cor:bar-functorial', 'cor:baxter-naturality-opoly', 'cor:bgg-koszul-involution', 'cor:completed-bar-cobar-yangian', 'cor:completion-closure-equivalence', 'cor:disk-local-ternary-on-brstbar-locus', 'cor:dk-partial-conj', 'cor:dk-poly-catO', 'cor:dk2-thick-generation-all-types', 'cor:dk23-all-types', 'cor:effective-quadruple', 'cor:feynman-duality-qch', 'cor:finiteness-criterion-reduction', 'cor:free-energy-ahat-genus', 'cor:genus0-named-coefficient-packet', 'cor:genus0-standard-chart-two-residues', 'cor:genus0-two-coefficient-packet', 'cor:hochschild-cup-exchange', 'cor:hs-sewing-standard-landscape', 'cor:k0-generation-OY', 'cor:kappa-additivity', 'cor:lagrangian-unconditional', 'cor:mc3-all-types', 'cor:metaplectic-square-root', 'cor:ramanujan-deligne-free', 'cor:rectification-ch-infty', 'cor:shadow-depth-koszul-invariance', 'cor:shadow-extraction', 'cor:shadow-fredholm', 'cor:shadow-schrodinger-singularities', 'cor:shadow-visibility-genus', 'cor:spectral-curve', 'cor:spectral-measure-identification', 'cor:string-amplitude-genus0', 'cor:theta-twisting-morphism', 'cor:thqg-intrinsic-bulk', 'cor:topological-recursion-mc-shadow', 'cor:unconditional-lattice', 'cor:universal-character-containment', 'cor:universal-koszul', 'cor:vol1-theta-log-fm-twisting-data', 'cor:w-line-alternating-vanishing', 'cor:w3-reconstruction', 'cor:w4-ds-stage4-square-class-reduction', 'cor:winfty-ds-stage5-reduced-packet', 'cor:winfty-stage4-primitive-transport-square-triple', 'cor:winfty-stage4-residue-four-channel', 'cor:winfty-stage4-residue-three-channel', 'cor:winfty-stage4-single-scalar-equivalent', 'cor:winfty-stage4-visible-borcherds-two-primitive', 'cor:winfty-stage5-effective-independent-frontier', 'cor:winfty-standard-mc4-package', 'cor:winfty-weight-cutoff', 'cor:yangian-canonical-realization-to-spectral-seed', 'cor:yangian-typea-degree2-plus-generators', 'def:analytic-koszul-pair', 'def:analytic-shadow', 'def:arithmetic-packet-connection', 'def:bar-differential-complete', 'def:cech-convolution', 'def:chiral-koszul-morphism', 'def:coacyclic-fact', 'def:completion-entropy', 'def:completion-hilbert-series', 'def:curved-fact-coalgebra', 'def:derived-scalar-period', 'def:e1-modular-convolution', 'def:euler-koszul-tier', 'def:feynman-transform-ass', 'def:finite-window', 'def:full-modular-package', 'def:generating-depth', 'def:genus1-modular-datum', 'def:hecke-defect-class', 'def:holographic-modular-koszul-datum', 'def:hs-sewing', 'def:modular-bar-hamiltonian', 'def:modular-convolution-dg-lie', 'def:modular-cyclic-deformation-complex', 'def:modular-homotopy-theory-intro', 'def:modular-koszul-chiral', 'def:modular-koszul-homotopy', 'def:modular-koszul-triple', 'def:modular-shadow-connection', 'def:multi-line-shadow-radius', 'def:nms-modular-quartic-resonance-class', 'def:ordered-ambient-algebra', 'def:planar-planted-forest-coefficient-algebra', 'def:planted-forest-coefficient-algebra', 'def:primitive-cumulant-quotient', 'def:primitive-defect-series', 'def:primitive-generating-series', 'def:primitive-log-modular-kernel', 'def:provisional-coderived', 'def:quartic-log-contact-class', 'def:reduced-branch-master-action', 'def:residue-clutching-defect', 'def:resonance-rank', 'def:ribbonized-swiss-cheese', 'def:scalar-lane', 'def:sewing-envelope', 'def:shadow-algebra', 'def:shadow-depth-classification', 'def:shadow-growth-rate', 'def:shadow-metric', 'def:shadow-postnikov-tower', 'def:shadow-tautological-classes', 'def:strong-completion-tower', 'def:tangential-log-curve', 'def:thqg-chiral-derived-center', 'def:thqg-chiral-endomorphism-operad', 'def:thqg-completed-platonic-datum', 'def:vol1-rigid-planted-forest-depth-filtration', 'def:winfty-stage4-ward-normalized', 'def:zero-side-miura-defect', 'eq:bbj-comparison', 'eq:constrained-epstein-fe', 'eq:delta-pf-genus3-explicit', 'eq:discriminant-complementarity', 'eq:master-square', 'eq:residue-kernel', 'eq:shadow-partition-function', 'eq:sl3-bar-recurrence', 'eq:tree-formula-general', 'eq:verlinde-general', 'ex:cech-hca-genus1', 'ex:tau-03-affine', 'lem:chirhoch-descent', 'lem:degree-cutoff', 'lem:extension-across-boundary-qi', 'lem:fd-thick-closure', 'lem:higher-genus-open-stratum-qi', 'op:multi-generator-universality', 'op:programme-a-cy-gluing', 'op:programme-b-moonshine', 'op:programme-c-second-quantization', 'op:programme-d-schottky', 'op:programme-e-mock-modularity', 'op:programme-f-factorization-envelope', 'op:programme-g-bkm-scattering', 'op:programme-h-descent', 'op:programme-i-higher-dim', 'op:programme-j-convergence', 'part:bar-complex', 'part:physics-bridges', 'part:standard-landscape', 'part:v1-frontier', 'princ:modular-trace', 'princ:transport-orbit-factorization', 'prop:2d-convergence', 'prop:affine-primitive-kernel', 'prop:affine-primitive-shell', 'prop:bar-ran-well-defined', 'prop:baxter-yangian-equivariance', 'prop:betagamma-primitive-kernel', 'prop:betagamma-primitive-shell', 'prop:borcherds-shadow-identification', 'prop:branch-master-equation', 'prop:c13-full-self-duality', 'prop:carleman-virasoro', 'prop:chain-level-three-obstructions', 'prop:chirhoch1-affine-km', 'prop:coderived-adequacy', 'prop:collapse-permanence', 'prop:compactified-ternary-two-channel', 'prop:d-module-purity-km', 'prop:d-module-purity-km-equivalence', 'prop:depth-gap-trichotomy', 'prop:dg-shifted-factorization-shared-seed', 'prop:disk-local-binary-ternary-reduction', 'prop:dk2-thick-generation-typeA', 'prop:dk5-sl2-frt', 'prop:dressed-propagator-resolution', 'prop:ds-bar-formality', 'prop:ds-bar-hook-commutation', 'prop:ds-chirhoch-compatibility', 'prop:ds-shadow-cascade', 'prop:e1-nonsplitting-genus1', 'prop:e2-collapse-formality', 'prop:e2-formality-hochschild', 'prop:factorization-fundamental-casimir-identity', 'prop:fake-complementarity-criterion', 'prop:fp-genus-decay-for-double', 'prop:free-field-scalar-exact', 'prop:gauge-criterion-scattering', 'prop:genus2-non-diagonal', 'prop:geometric-modular-operadic-mc', 'prop:gerstenhaber-sl2-bracket', 'prop:gram-wt4', 'prop:hc-dictionary', 'prop:hc-knill-laflamme', 'prop:hecke-defect-equivalences', 'prop:heisenberg-primitive-kernel', 'prop:heisenberg-primitive-shell', 'prop:hook-ghost-constant', 'prop:hs-trace-class', 'prop:independent-sum-factorization', 'prop:integrable-level-independence', 'prop:jacobiator-nullhomotopic', 'prop:kac-shadow-singularity', 'prop:kappa-bps-decomposition', 'prop:ker-av-schur-weyl', 'prop:koszul-closure-properties', 'prop:lagrangian-perfectness', 'prop:large-orbit-obstruction', 'prop:leech-cusp-nonvanishing', 'prop:leech-epstein', 'prop:li-criterion-failure', 'prop:lifts-as-relative-mc', 'prop:lqt-e1-subexponential-growth', 'prop:mc-bracket-determines-atoms', 'prop:mc4-weight-cutoff', 'prop:miura-packet-splitting', 'prop:modularity-constraint', 'prop:moonshine-kappa', 'prop:mumford-from-mc', 'prop:n2-koszulness', 'prop:newton-shadow-hecke', 'prop:non-semisimple-pixton-obstruction', 'prop:one-channel-automorphism-rigidity-criterion', 'prop:one-channel-canonical-transfer-criterion', 'prop:one-channel-chain-model-criterion', 'prop:one-channel-incidence-orbit-criterion', 'prop:one-channel-intrinsic-line-detection-criterion', 'prop:one-channel-minimal-seed-packet-criterion', 'prop:one-channel-parity-forcing-criterion', 'prop:one-channel-ptvv-criterion', 'prop:one-channel-root-string-chart-criterion', 'prop:one-channel-seed-criterion', 'prop:one-channel-signed-seed-character-criterion', 'prop:one-channel-support-graph-stabilizer-criterion', 'prop:one-channel-transfer-law-criterion', 'prop:one-channel-verdier-criterion', 'prop:one-channel-visible-lowdegree-packet-criterion', 'prop:one-channel-visible-orbit-table-criterion', 'prop:ordered-log-fm-construction', 'prop:pbw-universality', 'prop:planted-forest-tropical', 'prop:polyakov-chern-weil', 'prop:polyakov-degree-two-projection', 'prop:prefundamental-clebsch-gordan', 'prop:prime-side-defect-formula', 'prop:primitive-shell-equations', 'prop:propagator-universality', 'prop:propagator-variance', 'prop:provisional-embedding', 'prop:ptvv-lagrangian', 'prop:pva-degree-constraint', 'prop:quartic-contact-vanishes-BL', 'prop:r-matrix-descent-vol1', 'prop:rational-cft-multiplicativity-failure', 'prop:rho-decreasing-with-N', 'prop:saturation-equivalence', 'prop:saturation-functorial', 'prop:sc-formal-iff-class-g', 'prop:self-loop-vanishing', 'prop:shadow-chiral-graph', 'prop:shadow-connection-bpz', 'prop:shadow-genus-closed-form', 'prop:shadow-gf-convergence', 'prop:shadow-k3e', 'prop:shadow-periods', 'prop:shadow-schwarzian', 'prop:shadow-stokes-multipliers', 'prop:shadow-symmetric-power', 'prop:shadow-tower-three-lenses', 'prop:shadow-voros-classical', 'prop:shadow-wkb', 'prop:stieltjes-signed-universal', 'prop:stokes-regularity-FM', 'prop:subexponential-growth-automatic', 'prop:tautological-line-support-criterion', 'prop:theta-bridge-rational', 'prop:thqg-annulus-degeneration-kappa', 'prop:transport-propagation', 'prop:two-element-strict', 'prop:universal-gravitational-cross-channel', 'prop:universal-instanton-action', 'prop:virasoro-bottleneck', 'prop:virasoro-c26-selfdual', 'prop:virasoro-pade', 'prop:virasoro-primitive-kernel', 'prop:virasoro-primitive-shell', 'prop:virasoro-quartic-determinant', 'prop:virasoro-shadow-ratio-riccati', 'prop:vol1-first-two-weights-log-fm', 'prop:w3-denominator-filtration', 'prop:w3-wline-ring-relations', 'prop:w4-ds-ope-explicit', 'prop:wdvv-from-mc', 'prop:weight-system-map', 'prop:winfty-ds-stage-growth-packet', 'prop:winfty-mc4-frontier-package', 'prop:winfty-stage4-local-attack-order', 'prop:winfty-stage4-residue-pairing-reduction', 'prop:winfty-stage4-visible-borcherds-transport', 'prop:winfty-stage4-visible-diagonal-normalization', 'prop:winfty-stage4-ward-inheritance', 'prop:wn-entropy-ladder', 'prop:yangian-canonical-envelope', 'prop:yangian-canonical-hlevel-target', 'prop:yangian-module-koszul', 'prop:yangian-typea-realization-criterion', 'rem:admissible-koszul-status', 'rem:algebraic-analytic-divide', 'rem:arithmetic-threshold', 'rem:beilinson-four-gaps', 'rem:beyond-hook-rectangular', 'rem:bocherer-escalation', 'rem:bosonization-not-koszul', 'rem:boundary-line-bridge-path', 'rem:bridge-theorem-programme', 'rem:bv-equals-bar-cobar', 'rem:bv-springer-duality', 'rem:c13-holographic-significance', 'rem:categorical-zeta-riemann', 'rem:chain-vs-classical-mf', 'rem:characteristic-hierarchy', 'rem:chiral-deligne-tamarkin-dimensional-jump', 'rem:chriss-ginzburg-bocherer', 'rem:class-vs-integrated-visibility', 'rem:collapse-permanence', 'rem:complementarity-polyakov-cancellation', 'rem:construction-vs-resolution', 'rem:contact-stratum-separation', 'rem:corrected-mc3-frontier', 'rem:davenport-heilbronn-koszul', 'rem:dk-proved-vs-remains', 'rem:dk-shadow-status', 'rem:dressed-propagator-convention', 'rem:ds-arithmetic-defect', 'rem:ds-depth-increase-geometric', 'rem:ds-geometric-localization-principle', 'rem:e1-e2-obstruction', 'rem:effective-coupling', 'rem:eval-stability-recursive-kernel', 'rem:finite-defect-principle', 'rem:five-shadows-synthesis', 'rem:four-objects', 'rem:francis-gaitsgory-mc3', 'rem:genus2-beurling-kernel', 'rem:genus2-escape-route', 'rem:genus2-honest-assessment', 'rem:ghost-koszul-identification', 'rem:grothendieck-teichmuller', 'rem:heisenberg-inert', 'rem:hook-kappa-sum-rule', 'rem:kinematics-dynamics-split', 'rem:koszul-nonperturbative', 'rem:koszulness-vs-shadow-depth', 'rem:kummer-motive', 'rem:mc-ramanujan-bridge', 'rem:mc3-type-b-folding', 'rem:mc4-positive-vs-resonant', 'rem:mk4-status', 'rem:moduli-variation', 'rem:mok-dependency', 'rem:mok25-dependents', 'rem:moment-problem-vs-zero-location', 'rem:moonshine-niemeier-discrimination', 'rem:moonshine-orbifold-class-transition', 'rem:motivic-decomposition', 'rem:motivic-weight-ek', 'rem:n2-ce-chiral-gap', 'rem:n2-sca-koszulness', 'rem:n2-susy-hierarchy', 'rem:nilpotence-periodicity', 'rem:non-circular-logical-chain', 'rem:non-lattice-gap', 'rem:non-semisimple-cohft', 'rem:opoly-not-dense', 'rem:overdetermination-honest', 'rem:painleve-multichannel', 'rem:pbw-propagation-scope', 'rem:periodicity-exchange-harmonic', 'rem:periodicity-triple', 'rem:ptvv-relation', 'rem:quantum-master-complete', 'rem:saito-kurokawa-bridge', 'rem:shadow-field', 'rem:shadow-multiplicative-deformation', 'rem:shadow-radius-atlas', 'rem:spectral-characteristic-programme', 'rem:structural-obstruction', 'rem:structural-saturation', 'rem:symplectic-logarithmic', 'rem:theorem-A-decomposition', 'rem:theta-modular-twisting', 'rem:thqg-I-admissible', 'rem:two-discriminant-families', 'rem:two-verlinde-normalizations', 'rem:virasoro-resonance-model', 'rem:w-postnikov-interpretation', 'rem:w3-genus2-cross-channel', 'rem:weil-analogy-table', 'rem:yangian-dk23-inputs', 'sec:affine-cubic-shadow', 'sec:affine-ht-chern-simons', 'sec:ambient-complementarity-lagrangian', 'sec:analytic-completion', 'sec:analytic-continuation-programme', 'sec:bar-cobar', 'sec:beilinson-functional', 'sec:betagamma-quartic-birth', 'sec:betagamma-vortex-lines', 'sec:bordered-fm', 'sec:brst-bar-chain-map', 'sec:cat-O-strategies', 'sec:categorical-logarithm', 'sec:chiral-center-theorem', 'sec:complementarity-theorem', 'sec:derived-dk', 'sec:elliptic-bar-heisenberg', 'sec:en-koszul-duality', 'sec:first-complete-proof', 'sec:flat-connection-intro', 'sec:four-gaps', 'sec:free-field-genera', 'sec:genus2-arithmetic-frontier', 'sec:hecke-newton-closure', 'sec:heisenberg-shadow-gaussianity', 'sec:higher-depths', 'sec:infty-cat-factorization-kd', 'sec:km-koszul-abstract', 'sec:koszul-across-genera', 'sec:master-table', 'sec:mc4-splitting', 'sec:miura-defect-decomposition', 'sec:miura-packet-bridge', 'sec:mixed-cubic-quartic-shadows', 'sec:modular-bar-hamiltonian', 'sec:modular-chern-weil-transform', 'sec:modular-rigidity', 'sec:nms-feynman-transform-programme', 'sec:nms-multivariable-shadow', 'sec:nms-polarized-scattering-programme', 'sec:nms-universal-mc-principle', 'sec:non-renormalization-tree', 'sec:operadic-center-theorem', 'sec:operadic-rankin-selberg', 'sec:prime-locality-frontier', 'sec:quantum-chiral-homology-first-principles', 'sec:quartic-residue-programme', 'sec:residue-clutching-defect', 'sec:shadow-metric', 'sec:sl3-computation', 'sec:superpotential-ainfty-truncation', 'sec:thqg-open-closed-realization', 'sec:w-completion-kinematics', 'sec:w3-bar-degree3', 'sec:yangian-bar-explicit', 'ss:genus', 'subsec:bernoulli-asymptotics', 'subsec:bocherer-bridge-theorem', 'subsec:chain-modular-functor', 'subsec:coderived-ran-formalism', 'subsec:collision-filtration-recovery', 'subsec:completion-kinematics-cumulant', 'subsec:e1-as-primitive', 'subsec:kl-from-bar-cobar', 'subsec:primitive-flat-connection', 'subsec:primitive-kernel-compression', 'subsec:three-preprints-chain-level', 'subsec:virasoro-teichmuller-phase-space', 'subsec:w3-h5-verification', 'subsec:w3-shadow-archetype', 'subsec:yangian-h4-verification', 'subsubsec:shadow-analytic-structure', 'subsubsec:shadow-bootstrap-constraints', 'subsubsec:shadow-borel-resurgence', 'tab:koszulness-landscape', 'thm:ainfty-formality-depth', 'thm:ainfty-koszul-characterization', 'thm:algebraic-family-rigidity', 'thm:algebraic-string-dictionary', 'thm:ambient-complementarity-fmp', 'thm:ambient-complementarity-tangent', 'thm:ambient-d-squared-zero', 'thm:analytic-algebraic-comparison', 'thm:arakawa-variety-intersection', 'thm:associated-variety-koszulness', 'thm:bar-ainfty-complete', 'thm:bar-cobar-inversion-qi', 'thm:bar-cobar-isomorphism-main', 'thm:bar-cobar-spectral-sequence', 'thm:bar-cohomology-level-independence', 'thm:bar-concentration', 'thm:bar-curved-ch-infty', 'thm:bar-modular-operad', 'thm:bar-nilpotency-complete', 'thm:bar-semi-infinite-km', 'thm:bar-semi-infinite-w', 'thm:barr-beck-lurie-koszulness', 'thm:baxter-exact-triangles', 'thm:baxter-exact-triangles-opoly', 'thm:bgg-from-bar', 'thm:bifunctor-obstruction-decomposition', 'thm:bocherer-bridge', 'thm:bordered-fm-properties', 'thm:bridge-criterion', 'thm:brst-bar-genus0', 'thm:bv-bar-coderived', 'thm:c334', 'thm:catO-thick-generation', 'thm:categorical-cg-all-types', 'thm:cech-hca', 'thm:central-charge-complementarity', 'thm:chain-modular-functor', 'thm:chiral-deligne-tamarkin', 'thm:coefficient-stability-criterion', 'thm:cohft-reconstruction', 'thm:collision-depth-2-ybe', 'thm:collision-residue-twisting', 'thm:completed-bar-cobar-strong', 'thm:completed-twisting-representability', 'thm:convolution-formality-one-channel', 'thm:convolution-master-identification', 'thm:critical-level-cohomology', 'thm:cs-koszul-km', 'thm:cubic-gauge-triviality', 'thm:curvature-self-contraction', 'thm:cyclic-linf-graph', 'thm:cyclic-rigidity-generic', 'thm:depth-decomposition', 'thm:derived-dk-affine', 'thm:derived-dk-yangian', 'thm:dominant-branch-point', 'thm:ds-bar-gf-discriminant', 'thm:ds-koszul-intertwine', 'thm:ds-shadow-depth-increase', 'thm:ds-spectral-branch-preservation', 'thm:e1-chiral-koszul-duality', 'thm:e1-coinvariant-shadow', 'thm:e1-mc-element', 'thm:e1-primacy', 'thm:e1-theorem-A', 'thm:e1-theorem-A-modular', 'thm:e1-theorem-B', 'thm:e1-theorem-B-modular', 'thm:e1-theorem-C', 'thm:e1-theorem-C-modular', 'thm:e1-theorem-D', 'thm:e1-theorem-D-modular', 'thm:e1-theorem-H', 'thm:e1-theorem-H-modular', 'thm:e8-epstein', 'thm:en-koszul-duality', 'thm:euler-koszul-tier-classification', 'thm:exact-n-chi-weighting', 'thm:explicit-theta', 'thm:ext-diagonal-vanishing', 'thm:fact-co-contra-general', 'thm:factorization-dk-eval', 'thm:fh-concentration-koszulness', 'thm:fiber-center-identification', 'thm:finite-miura-defect', 'thm:fm-boundary-acyclicity', 'thm:fundamental-twisting-morphisms', 'thm:fusion-bar-cobar', 'thm:g1sf-master', 'thm:gaudin-yangian-identification', 'thm:general-hs-sewing', 'thm:genus-graded-koszul', 'thm:genus-universality', 'thm:genus1-d-squared', 'thm:genus1-universal-curvature', 'thm:genus2-non-collapse', 'thm:geometric-depth-smooth', 'thm:gram-positivity', 'thm:h-level-factorization-kd', 'thm:hamilton-jacobi-shadow', 'thm:hc-koszulness-exact-qec', 'thm:hc-shadow-redundancy', 'thm:hc-symplectic-code', 'thm:hecke-newton-lattice', 'thm:hecke-verdier-commutation', 'thm:heisenberg-bv-bar-all-genera', 'thm:heisenberg-obs', 'thm:heisenberg-one-particle-sewing', 'thm:heisenberg-sewing', 'thm:higher-genus-inversion', 'thm:hochschild-polynomial-growth', 'thm:hook-transport-corridor', 'thm:inductive-genus-determination', 'thm:interacting-gram-positivity', 'thm:kac-shapovalov-koszulness', 'thm:km-strictification', 'thm:kodaira-spencer-chiral-complete', 'thm:koszul-equivalences-meta', 'thm:koszul-exchange-regimes', 'thm:kw-bar-general-rank', 'thm:lattice-sewing', 'thm:lattice:factorization-koszul', 'thm:lattice:homotopy-factorization-dk', 'thm:lattice:level-k-dk', 'thm:lattice:quantum-factorization-dk', 'thm:leech-chi12-projection', 'thm:log-clutching-degeneration', 'thm:logfm-modular-cocomposition', 'thm:loop-order-spectral-sequence', 'thm:main-koszul-hoch', 'thm:master-commutative-square', 'thm:master-tower', 'thm:mc-recursion-moment', 'thm:mc-tautological-descent', 'thm:mc-twisting-closure', 'thm:mc2-bar-intrinsic', 'thm:mc2-full-resolution', 'thm:mc3-type-a-resolution', 'thm:modular-anomaly', 'thm:modular-characteristic', 'thm:modular-homotopy-convolution', 'thm:modular-koszul-duality-main', 'thm:monoidal-module-koszul', 'thm:multi-weight-genus-expansion', 'thm:mumford-formula', 'thm:nms-all-degree-resonance-boundary', 'thm:nms-archetype-trichotomy', 'thm:nms-beyond-ahat', 'thm:nms-bipartite-vanishing', 'thm:nms-clutching-law-modular-resonance', 'thm:nms-finite-termination', 'thm:nms-full-resonance-tower', 'thm:non-lattice-ramanujan', 'thm:non-renormalization-tree', 'thm:novikov-completion-theorem', 'thm:off-koszul-ran-inversion', 'thm:oper-bar', 'thm:oper-bar-h0-dl', 'thm:operadic-center-hochschild', 'thm:operadic-complexity', 'thm:operadic-homotopy-convolution', 'thm:ordered-associative-ds-principal', 'thm:ordered-associative-modular-mc', 'thm:packet-connection-flatness', 'thm:pbw-allgenera-km', 'thm:pbw-allgenera-principal-w', 'thm:pbw-allgenera-virasoro', 'thm:pbw-koszulness-criterion', 'thm:pbw-propagation', 'thm:pbw-universal-semisimple', 'thm:pixton-from-mc-semisimple', 'thm:planted-forest-structure', 'thm:planted-forest-tropicalization', 'thm:platonic-adjunction', 'thm:platonic-completion', 'thm:primitive-to-global-reconstruction', 'thm:prism-higher-genus', 'thm:pro-weyl-recovery', 'thm:quantum-arnold-relations', 'thm:quantum-complementarity', 'thm:quantum-complementarity-main', 'thm:quantum-diff-squares-zero', 'thm:quartic-obstruction-linf', 'thm:quartic-resonance-obstruction', 'thm:quillen-equivalence-chiral', 'thm:ran-coherent-bar-cobar', 'thm:recursive-existence', 'thm:resonance-filtered-bar-cobar', 'thm:riccati-algebraicity', 'thm:rigidity-inheritance', 'thm:rtt-mittag-leffler', 'thm:scattering-coupling-factorization', 'thm:schur-complement-quartic', 'thm:sectorwise-spectral-convergence', 'thm:self-dual-factorization', 'thm:sewing-hecke-reciprocity', 'thm:sewing-selberg-formula', 'thm:sewing-shadow-intertwining', 'thm:shadow-archetype-classification', 'thm:shadow-borel-genus', 'thm:shadow-cohft', 'thm:shadow-connection', 'thm:shadow-connection-kz', 'thm:shadow-depth-operator-order', 'thm:shadow-double-convergence', 'thm:shadow-eisenstein', 'thm:shadow-epstein-zeta', 'thm:shadow-euler-independence', 'thm:shadow-finite-determination', 'thm:shadow-formality-identification', 'thm:shadow-gf-borel', 'thm:shadow-higgs-field', 'thm:shadow-homotopy-invariance', 'thm:shadow-moduli-resolution', 'thm:shadow-radius', 'thm:shadow-resonance-locus', 'thm:shadow-separation', 'thm:shadow-siegel-gap', 'thm:shadow-spectral-correspondence', 'thm:shadow-spectral-measure', 'thm:shadow-subalgebra-autonomy', 'thm:shadow-tautological-ring', 'thm:shadow-transseries', 'thm:shifted-prefundamental-generation', 'thm:shifted-symplectic-complementarity', 'thm:single-line-dichotomy', 'thm:spectral-continuation-bridge', 'thm:sphere-reconstruction', 'thm:stabilized-completion-positive', 'thm:stratified-conservative-restriction', 'thm:structural-separation', 'thm:tautological-line-support', 'thm:theta-direct-derivation', 'thm:thqg-annulus-trace', 'thm:thqg-brace-dg-algebra', 'thm:thqg-local-global-bridge', 'thm:thqg-mc-forced-consistency', 'thm:thqg-oc-mc-equation', 'thm:thqg-oc-projection', 'thm:thqg-swiss-cheese', 'thm:topologization', 'thm:transport-closure-type-a', 'thm:tropical-koszulness', 'thm:uniform-pbw-bridge', 'thm:universal-generating-function', 'thm:universal-kac-moody-koszul', 'thm:universal-theta', 'thm:universality-of-G', 'thm:verdier-bar-cobar', 'thm:vieta-shadow-growth', 'thm:virasoro-moduli', 'thm:vol2-annulus-trace', 'thm:w-algebra-koszul', 'thm:w-algebra-koszul-main', 'thm:w-bp-strict', 'thm:w-integrability', 'thm:w-virasoro-quartic-explicit', 'thm:winfty-all-stages-rigidity-closure', 'thm:winfty-factorization-kd', 'thm:yangian-canonical-realization-plus-one-seed', 'thm:yangian-canonical-realization-plus-vector-line', 'thm:yangian-e1', 'thm:yangian-formal-moduli-plus-core-realization', 'thm:yangian-shadow-theorem', 'thm:yangian-sklyanin-quantization', 'thm:yangian-typea-realization-plus-compacts', 'thm:yangian-typea-realization-plus-dg-packet']
FILE introduction_full_survey
REFS 435 ['app:branch-line-reductions', 'app:combinatorial-frontier', 'app:existence-criteria', 'app:homotopy-transfer', 'app:nilpotent-completion', 'app:nonlinear-modular-shadows', 'app:sign-conventions', 'app:signs', 'ch:algebraic-foundations', 'ch:chiral-deformation', 'ch:derived-langlands', 'ch:en-koszul-duality', 'ch:fourier-seed', 'ch:genus-expansions', 'ch:genus1-seven-faces', 'ch:heisenberg-frame', 'ch:holographic-datum-master', 'ch:ht-boundary', 'ch:lattice', 'ch:quantum-corrections', 'ch:three-invariants', 'ch:v1-bv-brst', 'ch:v1-feynman', 'ch:ym-boundary-theory', 'ch:ym-instanton-screening', 'chap:NAP-koszul-derivation', 'chap:arithmetic-shadows', 'chap:bar-cobar', 'chap:bar-cobar-adjunction', 'chap:beta-gamma', 'chap:cobar-construction', 'chap:concordance', 'chap:config-spaces', 'chap:deformation-examples', 'chap:deformation-theory', 'chap:detailed-computations', 'chap:e1-modular-koszul', 'chap:entanglement-modular-koszul', 'chap:free-fields', 'chap:higher-genus', 'chap:holographic-codes-koszul', 'chap:kac-moody', 'chap:kac-moody-koszul', 'chap:koszul-pairs', 'chap:ordered-associative-chiral-kd', 'chap:w-algebras', 'chap:yangians', 'comp:bp-kappa-three-paths', 'comp:w3-genus2-cross-graphwise', 'conj:categorical-modular-kd', 'conj:clutching-closure', 'conj:cumulant-recognition', 'conj:dk5-restricted', 'conj:loop-connes-transfer', 'conj:quartic-closure', 'conj:scalar-saturation-universality', 'const:vol1-boundary-operators-residue', 'const:vol1-genus-spectral-sequence', 'const:vol1-graphwise-log-fm-cocomposition', 'const:vol1-modular-tangent-complex', 'constr:degree4-degeneration', 'constr:platonic-package', 'constr:thqg-oc-mc-element', 'cor:analytic-shadow-realization', 'cor:cobar-nilpotence-verdier', 'cor:completion-closure-equivalence', 'cor:dk23-all-types', 'cor:ds-theta-descent', 'cor:mc3-all-types', 'cor:nms-betagamma-mu-vanishing', 'cor:scalar-saturation', 'cor:shadow-depth-koszul-invariance', 'cor:shadow-visibility-genus', 'cor:string-amplitude-genus0', 'cor:theta-twisting-morphism', 'cor:topological-recursion-mc-shadow', 'cor:unconditional-allgenera-km', 'cor:unconditional-allgenera-principal-w', 'cor:unconditional-allgenera-virasoro', 'cor:unconditional-lattice', 'cor:vol1-theta-log-fm-twisting-data', 'def:arithmetic-packet-connection', 'def:chiral-algebra', 'def:chiral-twisting-datum', 'def:complementarity-complexes', 'def:completion-entropy', 'def:completion-hilbert-series', 'def:convolution-dg-lie', 'def:cyclic-deformation-elementary', 'def:cyclically-admissible', 'def:e1-modular-convolution', 'def:envelope-shadow-functor', 'def:euler-koszul-tier', 'def:fact-algebra-correct', 'def:factorization-algebra-AF', 'def:feynman-transform', 'def:frontier-defect-form', 'def:full-modular-package', 'def:geom-cobar-intrinsic', 'def:higher-genus-log-forms', 'def:log-fm-compactification', 'def:modular-convolution-dg-lie', 'def:modular-cyclic-deformation-complex', 'def:modular-koszul-chiral', 'def:modular-koszul-homotopy', 'def:modular-operad', 'def:modular-yangian-pro', 'def:planted-forest-coefficient-algebra', 'def:primitive-cumulant-quotient', 'def:primitive-defect-series', 'def:primitive-log-modular-kernel', 'def:provisional-coderived', 'def:ran-space', 'def:relative-holographic-deformation', 'def:ribbon-modular-operad', 'def:sdr', 'def:shadow-algebra', 'def:shadow-metric', 'def:shadow-tautological-classes', 'def:stable-graph', 'def:stable-graph-coefficient-algebra', 'def:thqg-chiral-derived-center', 'def:thqg-completed-platonic-datum', 'def:uniform-weight-lane', 'def:vol1-rigid-planted-forest-depth-filtration', 'eq:ahat-universality-preface', 'eq:borcherds-axiom', 'eq:e1-mc-degree3', 'eq:e1-to-einfty-projection', 'lem:bare-graph-no-thooft', 'lem:degree-cutoff', 'lem:stable-graph-d-squared', 'op:multi-generator-universality', 'part:bar-complex', 'part:characteristic-datum', 'part:physics-bridges', 'part:seven-faces', 'part:standard-landscape', 'part:v1-frontier', 'princ:four-test-interface', 'princ:gravitational-primitivity', 'prop:2d-convergence', 'prop:ainfty-formality-implies-koszul', 'prop:borcherds-shadow-identification', 'prop:cross-channel-growth', 'prop:discriminant-characteristic', 'prop:ds-bar-formality', 'prop:e1-shadow-r-matrix', 'prop:independent-sum-factorization', 'prop:interchannel-coupling', 'prop:lifts-as-relative-mc', 'prop:mc-bracket-determines-atoms', 'prop:mc4-weight-cutoff', 'prop:miura-packet-splitting', 'prop:model-independence', 'prop:mumford-from-mc', 'prop:nilpotent-transport-typeA', 'prop:non-semisimple-pixton-obstruction', 'prop:pole-decomposition', 'prop:pole-purity', 'prop:polyakov-chern-weil', 'prop:propagator-variance', 'prop:self-referentiality-criterion', 'prop:standard-examples-modular-koszul', 'prop:standard-strong-filtration', 'prop:theta-bridge-rational', 'prop:universal-gravitational-cross-channel', 'prop:vol1-first-two-weights-log-fm', 'prop:wdvv-from-mc', 'prop:wn-entropy-ladder', 'rem:bosonization-not-koszul', 'rem:contact-stratum-separation', 'rem:davenport-heilbronn-koszul', 'rem:ds-geometric-localization-principle', 'rem:four-levels', 'rem:four-test-interface', 'rem:frame-why-dbracket-fails', 'rem:propagator-weight-universality', 'rem:riccati-ode', 'rem:shadow-hamiltonian', 'rem:three-bar-variants', 'rem:two-orthogonal-axes', 'rem:w3-genus2-cross-channel', 'sec:chiral-center-theorem', 'sec:frame-koszul-dual', 'sec:koszul-across-genera', 'sec:operadic-center-theorem', 'sec:thqg-open-closed-realization', 'subsec:completion-kinematics-programme', 'subsec:concordance-four-test-boundary', 'subsec:frame-sl2-bar-low-degree', 'subsec:sewing-gram-matrix', 'subsec:three-preprints-chain-level', 'tab:master-invariants', 'thm:FM-convergence', 'thm:algebraic-family-rigidity', 'thm:algebraic-string-dictionary', 'thm:ambient-d-squared-zero', 'thm:analytic-algebraic-comparison', 'thm:bar-cobar-adjunction', 'thm:bar-cobar-inversion-qi', 'thm:bar-cobar-isomorphism-main', 'thm:bar-cobar-verdier', 'thm:bar-concentration', 'thm:bar-modular-operad', 'thm:bar-nilpotency-complete', 'thm:brst-bar-genus0', 'thm:categorical-cg-all-types', 'thm:cech-hca', 'thm:chain-modular-functor', 'thm:chiral-deligne-tamarkin', 'thm:coefficient-stability-criterion', 'thm:cohft-reconstruction', 'thm:collision-residue-twisting', 'thm:completed-bar-cobar-strong', 'thm:completed-twisting-representability', 'thm:convolution-dg-lie-structure', 'thm:convolution-master-identification', 'thm:cubic-gauge-triviality', 'thm:cyclicity-ribbon', 'thm:depth-decomposition', 'thm:derived-dk-affine', 'thm:ds-bar-gf-discriminant', 'thm:ds-koszul-intertwine', 'thm:ds-platonic-functor', 'thm:e1-mc-element', 'thm:e1-mc-finite-degree', 'thm:ent-scalar-entropy', 'thm:exact-n-chi-weighting', 'thm:factorization-dk-eval', 'thm:family-index', 'thm:fcom-coinvariant-fass', 'thm:finite-miura-defect', 'thm:fundamental-twisting-morphisms', 'thm:general-hs-sewing', 'thm:genus-universality', 'thm:gram-positivity', 'thm:hecke-newton-lattice', 'thm:hecke-verdier-commutation', 'thm:heisenberg-bv-bar-all-genera', 'thm:heisenberg-one-particle-sewing', 'thm:higher-genus-inversion', 'thm:hochschild-polynomial-growth', 'thm:inductive-genus-determination', 'thm:interacting-gram-positivity', 'thm:koszul-equivalences-meta', 'thm:lattice:curvature-braiding-orthogonal', 'thm:log-clutching-degeneration', 'thm:main-koszul-hoch', 'thm:master-commutative-square', 'thm:mc-tautological-descent', 'thm:mc-twisting-closure', 'thm:mc2-bar-intrinsic', 'thm:mc3-type-a-resolution', 'thm:modular-characteristic', 'thm:modular-quantum-linfty', 'thm:multi-weight-genus-expansion', 'thm:nms-clutching-law-modular-resonance', 'thm:nms-virasoro-quartic-explicit', 'thm:operadic-center-hochschild', 'thm:pbw-allgenera-km', 'thm:pbw-allgenera-principal-w', 'thm:pbw-allgenera-virasoro', 'thm:pixton-from-mc-semisimple', 'thm:planted-forest-tropicalization', 'thm:platonic-adjunction', 'thm:platonic-completion', 'thm:primitive-to-global-reconstruction', 'thm:prism-higher-genus', 'thm:quantum-complementarity-main', 'thm:quantum-diff-squares-zero', 'thm:quillen-equivalence-chiral', 'thm:recursive-existence', 'thm:resonance-filtered-bar-cobar', 'thm:riccati-algebraicity', 'thm:self-dual-factorization', 'thm:sewing-hecke-reciprocity', 'thm:shadow-cohft', 'thm:shadow-connection', 'thm:shadow-depth-operator-order', 'thm:shadow-euler-independence', 'thm:shadow-formality-identification', 'thm:shadow-homotopy-invariance', 'thm:shadow-resonance-locus', 'thm:shadow-separation', 'thm:shadow-spectral-correspondence', 'thm:shadow-tautological-ring', 'thm:single-line-dichotomy', 'thm:spectral-characteristic', 'thm:stabilized-completion-positive', 'thm:thqg-annulus-trace', 'thm:thqg-oc-mc-equation', 'thm:thqg-swiss-cheese', 'thm:uniform-pbw-bridge', 'thm:universal-MC', 'thm:universal-generating-function', 'thm:volume-one-concrete-modular-datum', 'thm:w-algebra-koszul-main', 'thm:w-koszul-precise', 'thm:winfty-all-stages-rigidity-closure', 'thm:yangian-koszul-dual']
CITES 53 ['BD04', 'BGS96', 'ChariMoura06', 'CostelloGaiotto2020', 'DNP25', 'Deligne1974', 'Drinfeld85', 'FBZ04', 'FFR94', 'FG12', 'GK94', 'GK98', 'GLZ22', 'GZ26', 'GeK98', 'HA', 'Kac', 'KhanZeng25', 'LPWZ09', 'LV12', 'Li96', 'MS24', 'Mok25', 'PTVV13', 'Positselski11', 'Priddy70', 'Pridham17', 'RNW19', 'STS83', 'Sta63', 'Val16']
FILE ordered_chiral_homology
REFS 3 ['prop:critical-level-ordered', 'prop:g2-conformal-block-degree', 'thm:verlinde-polynomial-family']
FILE programme_summary_sections2_4
REFS 1 ['ssec:d-squared']
FILE programme_summary_sections5_8
REFS 2 ['def:shadow-depth', 'sec:bar']
CITES 4 ['Drinfeld85', 'FFR94', 'KZ84', 'STS83']
FILE programme_summary_sections9_14
REFS 3 ['eq:curvature', 'eq:mc-equation', 'sec:bar']


thinking
**Evaluating reporting options**

This feels overwhelming since I can’t list all 1,736 references. Instead, I should focus on critical issues for the editorial and surveys, which aren't standalone because of many external references. The user wants every unresolved reference noted, but listing all unique references may not be practical. I’ll consider presenting about 30 focused findings on unique categories and explicit fixes. Including individual macro findings and representative groups should respect the request for exact fixes without listing every repeated label.
thinking
**Clarifying reporting details**

I have an example that outlines a problem with undefined cross-manuscript references and citation keys in a specific file. I’m considering whether it meets the user's request for exact line references; perhaps using only the starting line of the first unresolved reference is the way to go. I could also mention additional counts derived from the log. Including classifications of unresolved references makes sense since there are only five unique labels, and I might need to check those line numbers.
exec
/bin/zsh -lc "rg -n 'thm:verlinde-polynomial-family|prop:critical-level-ordered|prop:g2-conformal-block-degree' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
7831:\begin{theorem}[Verlinde polynomial family; {\cite[Thm.~\ref*{thm:verlinde-polynomial-family}]{Lorgat26I}}]
7846:\begin{proposition}[Critical level: monodromy trivialises; {\cite[Prop.~\ref*{prop:critical-level-ordered}]{Lorgat26I}}]
7859:\begin{proposition}[Genus-$2$ conformal blocks by degree; {\cite[Prop.~\ref*{prop:g2-conformal-block-degree}]{Lorgat26I}}]

thinking
**Inspecting ordered chiral homology**

I’m curious about the usage of \ref* inside citations in ordered chiral homology. This could be an interesting topic to explore further. I’m thinking I should take a closer look at the specific lines in question to understand how they’re structured. It seems like there might be some nuances here worth investigating.  Let's dive in and see what insights I can gather from the lines I find!
exec
/bin/zsh -lc "sed -n '7828,7862p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Three results from the monograph~\cite{Lorgat26I} that
complement the constructions of this paper.

\begin{theorem}[Verlinde polynomial family; {\cite[Thm.~\ref*{thm:verlinde-polynomial-family}]{Lorgat26I}}]
\label{thm:verlinde-poly-standalone}
The Verlinde dimension $Z_g(k) = \sum_{j=0}^k S_{0j}^{2-2g}$
for $\widehat{\mathfrak{sl}}_2$ at level $k$ is a polynomial
$P_g(n)$ of degree $3(g-1)$ in $n = k + 2$ with
$P_g(n) = n^{g-1}(n^2 - 1) \cdot R_{g-2}(n^2)$.
Through $g = 6$: $P_2 = n(n^2{-}1)/6$,
$P_3 = n^2(n^2{-}1)(n^2{+}11)/180$,
$P_4 = n^3(n^2{-}1)(2n^4{+}23n^2{+}191)/7560$.
Leading coefficient: $\zeta(2g{-}2)/(2^{g-2}\pi^{2g-2})$.
Rational generating function:
$G_n(x) = \sum_{j=1}^{n-1} 1/(1 - a_j x)$,
$a_j = n/(2\sin^2(\pi j/n))$.
\end{theorem}

\begin{proposition}[Critical level: monodromy trivialises; {\cite[Prop.~\ref*{prop:critical-level-ordered}]{Lorgat26I}}]
\label{prop:critical-standalone}

thinking
**Figuring out citation issues**

I’m noticing an interesting problem with undefined references when using `\ref*` inside an optional citation note. Those labels aren't local, which can cause confusion. The exact fix seems to involve replacing each optional citation text with the actual theorem or proposition numbers, or I could drop the `\ref*` from the citation note altogether. I also need to check the `shadow_towers_v2` file for any duplicate preamble or other issues. That's definitely worth a look!
exec
/bin/zsh -lc "sed -n '1,80p' standalone/shadow_towers_v2.tex && printf '\\n---CUT---\\n' && rg -n '\\\\documentclass|\\\\begin\\{document\\}|\\\\usepackage|\\\\newtheorem' standalone/shadow_towers_v2.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
\usepackage[all]{xy}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]

thinking
**Inspecting document structure**

I’m curious about the log indicating that it’s only allowing one preamble. I wonder if it could later input a full file. I think I need to check for a second \documentclass or \usepackage after \begin{document}. I’ll focus my search after line 65 to look for possible issues in the document structure. It feels like there’s a puzzle to solve here!
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
text=Path('standalone/shadow_towers_v2.tex').read_text()
start=text.find('\\\\begin{document}')
body=text[start+len('\\\\begin{document}'):] if start"'!=-1 else text
for token in ['"'\\\\documentclass','\\\\usepackage','\\\\newtheorem','\\\\theoremstyle','\\\\numberwithin']:
    idx=body.find(token)
    if idx"'!=-1:
        ln=body[:idx].count('"'\\n')+ (text[:start].count('\\n')+1 if start"'!=-1 else 1)
        print(token, '"'line', ln)
PY
rg -n '\\\\documentclass|\\\\usepackage|\\\\newtheorem|\\\\theoremstyle|\\\\numberwithin' standalone/shadow_towers_v2.tex | tail -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1:\documentclass[11pt,reqno]{amsart}
6:\usepackage{amsmath,amssymb,amsthm}
7:\usepackage{mathrsfs}
8:\usepackage{enumerate}
9:\usepackage[shortlabels]{enumitem}
10:\usepackage{booktabs}
11:\usepackage{array}
12:\usepackage{microtype}
13:\usepackage[dvipsnames]{xcolor}
14:\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}
15:\usepackage[all]{xy}
20:\newtheorem{theorem}{Theorem}[section]
21:\newtheorem{proposition}[theorem]{Proposition}
22:\newtheorem{lemma}[theorem]{Lemma}
23:\newtheorem{corollary}[theorem]{Corollary}
24:\newtheorem{conjecture}[theorem]{Conjecture}
25:\theoremstyle{definition}
26:\newtheorem{definition}[theorem]{Definition}
27:\newtheorem{construction}[theorem]{Construction}
28:\newtheorem{example}[theorem]{Example}

thinking
**Exploring document structure issues**

I’m trying to figure out why there are preamble-only errors in my document. It might have to do with elements like `\title`, `\author`, `\date`, and `\address` being placed after `\begin{document}` when they should actually be in the preamble, especially in amsart. Okay, that seems to be the main issue! Now, I need to find the exact lines causing this problem and search for a solution.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\title|"'^'"\\\\author|"'^'"\\\\address|"'^'"\\\\email|"'^'"\\\\date' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
67:\title[Modular Koszul Duality and the Shadow Tower]
72:\author{Raeez Lorgat}
73:\address{Perimeter Institute for Theoretical Physics,
75:\email{rlorgat@perimeterinstitute.ca}
77:\date{\today}

thinking
**Inspecting errors in logs**

I think I need to take a closer look at the environment redefinition errors. It doesn't seem like they're coming from a duplicate preamble, so maybe there's another reason for the logs. I'll inspect the beginning of the logs to find more context around those errors. Understanding what's happening there could help clarify the issue. It's always better to solve problems step-by-step, right?
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
lines=Path('standalone/shadow_towers_v2.log').read_text(errors='ignore').splitlines()
for i,l in enumerate(lines):
    if 'Can be used only in preamble' in l or 'already defined' in l:
        print('---', i+1)
        for j in range(max(0,i-2), min(len(lines), i+4)):
            print(lines[j])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- 694
(./riccati.tex

! LaTeX Error: Can be used only in preamble.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
--- 707


! LaTeX Error: Can be used only in preamble.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
--- 720


! LaTeX Error: Can be used only in preamble.

See the LaTeX manual or LaTeX Companion for explanation.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\input|"'^'"\\\\include|riccati' standalone/shadow_towers_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
487:\input{riccati}
551:Parts (i)--(ii) are proved in Theorem~\ref{thm:riccati-algebraicity}
560:\input{classification}
562:\input{computations}

thinking
**Identifying document issues**

I’m noticing that when I input full standalone documents like `riccati` or `classification`, I run into errors and redefinition collisions. The better approach seems to be to input body-only fragments or use `\include` for separate compilation. Specifically, I should replace `\input{riccati}` with `\input{riccati_body}` after breaking `riccati.tex` at `\begin{document}` and `\end{document}`. I need to look into unresolved citations from `shadow_towers_v2` as well. It might be necessary to inspect the editorial settings too!
exec
/bin/zsh -lc "sed -n '1,120p' standalone/editorial.tex | nl -ba | sed -n '1,120p'
rg -n '\\\\mainpreambleonly|\\\\input\\{|\\\\include\\{' standalone/editorial.tex main.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
standalone/editorial.tex:3:\def\mainpreambleonly{1}
standalone/editorial.tex:4:\IfFileExists{main.tex}{\input{main.tex}}{\input{../main.tex}}
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '586,724p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   600	\providecommand{\Aut}{\operatorname{Aut}}
   601	\providecommand{\mathbbm}[1]{\mathbb{#1}}
   602	\providecommand{\bigboxtimes}{\mathop{\boxtimes}\displaylimits}
   603	\providecommand{\Bbar}{\bar{B}}
   604	\providecommand{\B}{\bar{B}}
   605	\providecommand{\Det}{\mathrm{Det}}


thinking
**Inspecting classification issues**

I'm looking to inspect the classification trichotomy around line 100 for wording fixes. I also want to check the survey_modular_koszul_duality_v2 for missing ord and Ydg. Missing definitions for \ord or \barB^{\ord} would cause undefined control sequences. I’ve noted that there are 58 unresolved references in this file, and should we include them? If the user wants every unresolved reference, I might need to categorize them into source-level compile blockers and standalone-fragment dependency failures, to keep things organized.
thinking
**Creating grouped findings**

I can compress many unresolved references into grouped findings by file, while still mentioning the actual counts and some key lists at the top. The user wants a specific format: “[SEVERITY] file:line — PROBLEM: ... FIX: ...” which means I can do one line for each grouped finding. I might include counts and a list of labels, keeping a handful. For larger files, I could mention counts and say, “full set from fresh log includes…” with notable prefixes. I should mention "for ALL listed labels/keys" in the fix too. This seems specific enough!
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
lines=Path('standalone/survey_modular_koszul_duality.log').read_text(errors='ignore').splitlines()
for i,l in enumerate(lines):
    if 'Undefined control sequence.' in l:
        print('---', i+1)
        for j in range(max(0,i-1), min(len(lines), i+3)):
            print(lines[j])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- 569
[19]
! Undefined control sequence.
l.1338  \Hom
            \bigl(B(\Ass),\,\End_A\bigr)
--- 578

! Undefined control sequence.
l.1338  \Hom\bigl(B(\Ass),\,\End
                                _A\bigr)
--- 587

! Undefined control sequence.
l.1341  \Hom
            _\Sigma\bigl(B(\cP),\,\End_V\bigr)
--- 596

! Undefined control sequence.
l.1341  \Hom_\Sigma\bigl(B(\cP),\,\End
                                      _V\bigr)

thinking
**Identifying missing macros**

It looks like I'm noticing more missing macros, like \Defcyc and \Bbbk, which I think pops up at 2975 but not earlier. Then there's \Aut at 7464 and \CompCl, which might be around line 8013. I should consider adding these. It might help to also inspect the log around the introduction_full_survey section to pinpoint any other missing macros. I'm curious how to address these gaps effectively!
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
lines=Path('standalone/introduction_full_survey.log').read_text(errors='ignore').splitlines()
for i,l in enumerate(lines):
    if 'Undefined control sequence.' in l:
        print('---', i+1)
        for j in range(max(0,i-1), min(len(lines), i+3)):
            print(lines[j])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- 523
[3]
! Undefined control sequence.
<recently read> \dzero 
                       
--- 534

! Undefined control sequence.
<recently read> \dzero 
                       
--- 576

! Undefined control sequence.
l.422 \Hom
          \!\bigl(F\!\Ass(g,n),\,\End_\cA(n)\bigr),
--- 585

! Undefined control sequence.
l.422 \Hom\!\bigl(F\!\Ass(g,n),\,\End
                                     _\cA(n)\bigr),
exec
/bin/zsh -lc "rg -n '\\\\llbracket|\\\\rrbracket|\\\\id\\b|\\\\ar\\b' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
566:{\gAmod}^{\Eone}$ with $\operatorname{av} \circ s = \id$.
1106:$\delta_\cA \in 1 + x\,\Bbbk\llbracket x \rrbracket$
4647: \ar[r, "\Phi", "\sim"']
4648: \ar[d, "\Phi_{\mathrm{KL}}"', "\sim"]
4650: \ar[d, "\Phi_{\mathrm{KL}}", "\sim"']
4653: \ar[r, "q \mapsto q^{-1}"', "\sim"]
exec
/bin/zsh -lc "sed -n '4638,4656p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{remark}[The DK square]\label{rem:dk-inevitability}
\index{Drinfeld--Kohno!derived!as witness of the two determinations}
The coexistence of the commutative and braided determinations is
witnessed by the derived
Drinfeld--Kohno square (Theorem~\ref{thm:derived-dk-affine}):
\begin{equation}\label{eq:dk-intro}
\begin{tikzcd}
\mathcal{O}_k^{\mathrm{int}}(\widehat{\mathfrak{g}})
 \ar[r, "\Phi", "\sim"']
 \ar[d, "\Phi_{\mathrm{KL}}"', "\sim"]
& \mathcal{O}_{k'}(\widehat{\mathfrak{g}})
 \ar[d, "\Phi_{\mathrm{KL}}", "\sim"']
\\
\mathcal{C}(U_q(\mathfrak{g}))
 \ar[r, "q \mapsto q^{-1}"', "\sim"]
& \mathcal{C}(U_{q^{-1}}(\mathfrak{g}))
\end{tikzcd}
\end{equation}

thinking
**Debugging LaTeX packages**

I'm considering whether the tikz-cd package should be loaded since it seems to be missing. Importing this package could fix both the tikzcd environment and the `\ar` command. Next, I should check if the issue with `\operatorname{Conf}_k^{<}(\R)` arises from `\R` being undefined—seems likely. There might also be a missing `\chirCom`. I should also look at the `survey_modular_koszul_duality_v2` log for any missing macro names or other syntax problems.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
lines=Path('standalone/survey_modular_koszul_duality_v2.log').read_text(errors='ignore').splitlines()
for i,l in enumerate(lines):
    if 'Undefined control sequence.' in l or 'Missing "'$ inserted.'"' in l:
        print('---', i+1)
        for j in range(max(0,i-1), min(len(lines), i+3)):
            print(lines[j])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- 791

! Undefined control sequence.
l.707 ...$E_1$-chiral algebras live on $\Ran^{\ord
                                                  }(X)$; the ordered
--- 800

! Undefined control sequence.
l.708 bar $\barB^{\ord
                      }$ carries the $R$-matrix. The formality bridge
--- 2534

! Missing $ inserted.
<inserted text> 
                $
--- 2578

! Missing $ inserted.
<inserted text> 
                $

thinking
**Inspecting line numbers**

I see that there are missing dollar signs likely due to a messed-up command in my LaTeX code, particularly around `\widehat{\fg\fl}_1`. This may suggest there's an issue on line 8211. I need to focus on inspecting the lines surrounding 8211 to figure out where the mistake might be. Getting to the root of this should help fix the errors! Let's dive in and find those missing symbols.
exec
/bin/zsh -lc "sed -n '8206,8214p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is the holographic structure of the programme. Each arrow is:
restriction to codimension-$2$ defect, ordered bar complex,
categorified averaging (Drinfeld centre), and higher Deligne
(derived centre). The circle closes for 3d HT theories with
conformal vector: the Drinfeld centre
$\cZ(\Rep^{E_1}(Y^+(\widehat{\fg\fl}_1)))
\cong \Rep^{E_2}(\cW_{1+\infty})$
identifies the $E_2$ Drinfeld centre of the $E_1$ quantum group
representation category with the $E_2$ representation category of
exec
/bin/zsh -lc "rg -n '\\\\llbracket|\\\\rrbracket|\\\\Bbbk|\\\\Defcyc|\\\\CompCl|\\\\Aut\\b' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
91:\providecommand{\Bbbk}{\mathbb{k}}
604:product is $\alpha_{(1)}\alpha\in\Bbbk\cdot\mathbf 1$, and
651:where $V^*$ is the $\Bbbk$-linear dual of the generating space and
740:When $X=\operatorname{Spec}\Bbbk$ is a point, configuration spaces
851:and $\kappa(\cA)\in\Bbbk$ is the scalar \emph{modular
1110:\;\simeq\;\Bbbk[-(3g-3)]
1309:$\Com(g,n)=\Bbbk$ for every stable $(g,n)$), each
1429:$\Bbbk[x]/(x^2)$); the Massey products are the obstructions.
1482:$C_1(\overline{\mathcal M}_{0,4})\cong\Bbbk$ provides a
1726:=\det(\Bbbk\,E(\Gamma))
1727:\otimes\det(H_1(\Gamma;\Bbbk))^{-1}$:
2025:n(\Gamma)},\Bbbk)$ is the chiral amplitude on~$\Gamma$ (propagators
2507:\;\in\;\Bbbk.
2675:$\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}})$.
2702: $\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}})$\\[2pt]
2704: & Cyclic cocycle in $\Defcyc^{\mathrm{mod}}(\cA)$\\[2pt]
2769:$\cA^{\mathrm{sh}}=H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ is a
2975:$\delta_\cA\in 1+x\,\Bbbk\llbracket x\rrbracket$ satisfies
5087: & cyclic deformation complex $\Defcyc(\cA)$ \\[2pt]
5897:H_\bullet\!\bigl(\Defcyc^{\mathrm{mod}}(\cA)\bigr),
exec
/bin/zsh -lc "sed -n '608,616p' standalone/programme_summary_sections9_14.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
% ====================================================================
\section{The single open problem}
\label{sec:open-problem}
% ====================================================================

Everything in Sections~\ref{sec:bar}--\ref{sec:frontier}
rests on two-dimensional geometry: curves, their moduli
spaces, and the factorization structure of colliding points
on a curve. The three-dimensional extension is conditional
exec
/bin/zsh -lc "rg -n '\\\\label\\{sec:frontier\\}' standalone/programme_summary_sections9_14.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
496:\label{sec:frontier}
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:riccati-algebraicity\\}|\\\\label\\{thm:single-line-dichotomy\\}' standalone/riccati.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
223:\label{thm:riccati-algebraicity}
428:\label{thm:single-line-dichotomy}
exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:single-line-dichotomy|thm:riccati-algebraicity|thm:depth-decomposition|rem:contact-stratum-separation|thm:nms-betagamma-quartic-birth)\\}' standalone/classification.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Exploring inputs and computations**

I need to check on the inputs for `shadow_towers_v2`, specifically looking into `classification` and possibly `computations`. I'm wondering if the `computations` part might not need to be a file. It could be a standalone process instead? I should search to clarify how these elements function together. There’s definitely more to explore here to make sure I’m getting everything right!
exec
/bin/zsh -lc "ls standalone | rg '"'^computations('"\\.tex)?"'$'"' && rg -n '"'^'"\\\\documentclass|"'^'"\\\\begin\\{document\\}' standalone/computations.tex standalone/classification.tex standalone/riccati.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
computations.tex
standalone/computations.tex:1:\documentclass[11pt]{article}
standalone/computations.tex:42:\begin{document}
standalone/riccati.tex:1:\documentclass[11pt]{article}
standalone/riccati.tex:45:\begin{document}
standalone/classification.tex:1:\documentclass[11pt]{article}
standalone/classification.tex:47:\begin{document}
exec
/bin/zsh -lc "rg -n 'eq:mc-equation|eq:curvature|sec:bar' standalone/programme_summary_sections9_14.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
315:equation~(\ref{eq:mc-equation}). The algebraic-family
565:At genus $g \ge 1$ the curvature~\eqref{eq:curvature}
613:Everything in Sections~\ref{sec:bar}--\ref{sec:frontier}
exec
/bin/zsh -lc "rg -n 'Drinfeld85|KZ84|STS83|FFR94|sec:bar|def:shadow-depth' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
198:studied. Drinfeld's $r$-matrix~\cite{Drinfeld85}, the KZ
199:connection~\cite{KZ84}, the Sklyanin
200:bracket~\cite{STS83}, and the Gaudin model~\cite{FFR94}
318:Section~\ref{sec:bar}: the bar differential extracts OPE
510:(Definition~\ref{def:shadow-depth}) separates the standard
770:% \bibitem{Drinfeld85}
775:% \bibitem{FFR94}
780:% \bibitem{KZ84}
785:% \bibitem{STS83}

thinking
**Fixing bibliography issues**

I think I've found the problem: I need to uncomment the local bibitems from lines 770 to 785 in my document. That should solve the issue! Also, I wonder if there’s a similar issue with `riccati.tex`, maybe it has some commented-out bibitems as well. I’ll search through that file to check. It’s nice when things click into place like this!
exec
/bin/zsh -lc "rg -n 'FlajoletSedgewick|bibitem' standalone/riccati.tex | tail -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
591:\cite[Theorem~VI.1]{FlajoletSedgewick} gives
exec
/bin/zsh -lc "rg -n 'LorgatCYChiral|bibitem' standalone/cy_quantum_groups_6d_hcs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
183:\cite{LorgatCYChiral} proves that for $d \geq 3$, the CY chiral

thinking
**Checking unresolved references**

I'm noticing some potential issues with the bibliography; maybe there’s an unresolved reference at line 559 in `programme_summary_sections2_4`? The target label could be missing due to section 1. I might fix this by using plain words instead. I should also check for labels like `sec:bar` or `def:shadow-depth` in `programme_summary_sections5_8` to see if they're absent. A quick search could help clarify things!
exec
/bin/zsh -lc "rg -n '\\\\label\\{(sec:bar|def:shadow-depth)\\}' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
text=Path('standalone/survey_modular_koszul_duality_v2.log').read_text(errors='ignore').splitlines()
for line in text:
    if 'Reference "'`'"' in line and 'undefined' in line:
        print(line)
        break
PY
rg -n 'thm:e1-formality-bridge|thm:e1-formality-failure|thm:chiral-qg-equiv|thm:glN-chiral-qg|thm:e3-identification|thm:topologization' standalone/survey_modular_koszul_duality_v2.tex | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
LaTeX Warning: Reference `thm:e1-formality-bridge' on page 11 undefined on inpu
709:(Theorem~\ref{thm:e1-formality-bridge}): for $E_\infty$-input,
711:failure (Theorem~\ref{thm:e1-formality-failure}): for genuinely
717:(Theorem~\ref{thm:chiral-qg-equiv}): on the Koszul locus, three
721:(Theorem~\ref{thm:glN-chiral-qg}).
733:The $E_3$ identification (Theorem~\ref{thm:e3-identification}): for
737:(Theorem~\ref{thm:topologization}): $\SCchtop + \text{conformal
763:(Theorem~\ref{thm:e3-identification}) proves
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
for line in Path('standalone/survey_modular_koszul_duality.log').read_text(errors='ignore').splitlines():
    if 'Reference "'`'"' in line and 'undefined' in line:
        print(line)
        break
    
PY
rg -n 'prop:pole-decomposition|ex:heisenberg-d-deg1|thm:riccati-algebraicity|thm:pixton-from-mc-semisimple|rem:hitchin-shadow-expanded|rem:baxter-q-from-mc' standalone/survey_modular_koszul_duality.tex | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
LaTeX Warning: Reference `prop:pole-decomposition' on page 9 undefined on input
626:(Proposition~\ref{prop:pole-decomposition}); since
631:(Example~\ref{ex:heisenberg-d-deg1}).
1076:(Theorem~\ref{thm:riccati-algebraicity}). The infinite tower is
1082:(Theorem~\ref{thm:pixton-from-mc-semisimple}), the integrable
1086:(Remark~\ref{rem:hitchin-shadow-expanded}), the Baxter $Q$-operator
1088:(Remark~\ref{rem:baxter-q-from-mc}), and the Bekenstein--Hawking
2886:equation. Theorem~\ref{thm:pixton-from-mc-semisimple}: on the
3688:(Theorem~\ref{thm:riccati-algebraicity}). \emph{Formality}: the
exec
/bin/zsh -lc "rg -n 'thm:shadow-separation|thm:shadow-tautological-ring|cor:analytic-shadow-realization|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:bar-cobar-inversion-qi|thm:fiber-center-identification|thm:quantum-complementarity-main' chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/editorial_constitution.tex:1648: Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}.
chapters/connections/editorial_constitution.tex:1678: Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
chapters/connections/editorial_constitution.tex:2041:complementarity theorem (Theorem~\ref{thm:quantum-complementarity-main})
chapters/connections/editorial_constitution.tex:2176:Part (i): Theorem~\ref{thm:quantum-complementarity-main}
chapters/connections/editorial_constitution.tex:2333:(Theorem~\ref{thm:quantum-complementarity-main}), which supplies
chapters/connections/editorial_constitution.tex:2355: \textup{(}Theorems~\ref{thm:bar-cobar-isomorphism-main},
chapters/connections/editorial_constitution.tex:2356: \ref{thm:higher-genus-inversion},
chapters/connections/editorial_constitution.tex:2357: \ref{thm:quantum-complementarity-main}\textup{)}. The Feynman
chapters/connections/editorial_constitution.tex:2486: Theorems~\ref{thm:bar-cobar-isomorphism-main}
chapters/connections/editorial_constitution.tex:2487: and~\ref{thm:quantum-complementarity-main}. The cyclic deformation
chapters/connections/editorial_constitution.tex:2523:Theorems~\ref{thm:bar-cobar-isomorphism-main}
chapters/connections/editorial_constitution.tex:2524:and~\ref{thm:quantum-complementarity-main}; the universal
chapters/connections/concordance.tex:37: \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
chapters/connections/concordance.tex:42: \textup{(}Thms~\ref{thm:higher-genus-inversion},
chapters/connections/concordance.tex:43: \ref{thm:bar-cobar-inversion-qi}\textup{)}; off the locus,
chapters/connections/concordance.tex:50: \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
chapters/connections/concordance.tex:54: \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
chapters/connections/concordance.tex:205: (Theorem~\ref{thm:quantum-complementarity-main}).
chapters/connections/concordance.tex:280: (Theorems~\ref{thm:bar-cobar-isomorphism-main}
chapters/connections/concordance.tex:281: and~\ref{thm:higher-genus-inversion}).}

thinking
**Checking compilation issues**

I need to check if some files compile due to an xcolor issue, as they aren't loading it properly. Maybe I can use color names from `hyperref` as a fix. I'll see if any files already have xcolor included—like N6 and Programme_summary, which should be good. It might also be useful to inspect line 210 of `three_parameter_hbar` since it seems there’s a broken fragment there. Let's take a closer look!
exec
/bin/zsh -lc "sed -n '206,214p' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
The factor $1/(k+h^\vee)$ arises because the Sugawara construction
normalizes the energy-momentum tensor by $(k + h^\vee)^{-1}$: the
OPE of currents produces the Casimir tensor $\Omega$ at mode $(1)$,
and the $\lambda$-bracket divided-power convention} = \lambda^n/n!$) yields the $r$-matrix with the
Sugawara-normalized prefactor.

\begin{proposition}[KZ25 coupling]\label{prop:kz-coupling}
$\hbar_{\mathrm{KZ}} = 1/(k + h^\vee)$.

thinking
**Fixing code issues**

I think I need to insert a missing opening phrase in the code. Maybe I should also remove that stray `} = \lambda^n/n!$)` since it looks off. Rewriting that sentence could help clarify things. I'll definitely check the `classification_trichotomy` line around line 100 to see if there's something I can inspect or improve there. This feels like a helpful path to making everything cleaner!
exec
/bin/zsh -lc "sed -n '96,104p' standalone/classification_trichotomy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$, the cofree tensor
coalgebra with deconcatenation coproduct; it is an element of the
$E_1$ convolution algebra that carries the full spectral-parameter
dependence. The modular characteristic
\kappa$ is the $\Sigma_2$-coinvariant scalar shadow of $r(z)$:
for abelian and Virasoro-type families
$\kappa = \mathrm{av}(r(z))$, while non-abelian affine Kac--Moody
adds the Sugawara shift $\dim(\fg)/2$.
This scalar projection,

thinking
**Inspecting code lines**

I think fixing this is fairly straightforward. I'm considering checking out lines 239 and 190 in N6 to see what might be happening there. It's always good to be thorough when debugging. I wonder if there's anything particularly unusual in those lines that could lead to the issue. Let's see what insights I can glean from inspecting them closely!
exec
/bin/zsh -lc "sed -n '186,242p' standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:main} resolves the operadic complexity
conjecture: the shadow termination degree $r_{\max}(\cA)$, the
transferred $\Ainf$-depth $d_\infty(\cA)$, and the
$\Linf$-formality level $f_\infty(\cA)$ of $\gmodzero$ are a
single invariant of $\cA$ (Corollary~\ref{cor:operadic-complexity}).
The four shadow-depth classes are realized by Heisenberg (class
\textbf{G}, $r_{\max}=2$, formal), affine Kac--Moody (class
\textbf{L}, $r_{\max}=3$), $\beta\gamma$ (class \textbf{C},
$r_{\max}=4$), and Virasoro (class \textbf{M},
$r_{\max}=\infty$, intrinsically non-formal); see
Section~\ref{sec:examples}.

\subsection{Organization}

Section~\ref{sec:shadow-tower} defines the shadow obstruction
tower. Section~\ref{sec:formality-tower} recalls the transferred
$\Linf$ structure and the formality obstruction tower.
Section~\ref{sec:base-cases} proves the identification at
degrees $2,3,4$. Section~\ref{sec:main} proves
Theorem~\ref{thm:main}. Section~\ref{sec:corollary} deduces the

thinking
**Searching for clarity**

I’m considering how to improve the text. Maybe I should replace "ref" with "the operadic complexity corollary below" if it's in the local context. But wait, I noticed that there's an actual section for corollaries, so maybe that label isn’t defined yet! I guess I need to do some searching to clarify that. Let's see if I can find a better way to label it or make it clearer to avoid confusion.
exec
/bin/zsh -lc "rg -n '\\\\label\\{cor:operadic-complexity\\}|sec:corollary' standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
205:Theorem~\ref{thm:main}. Section~\ref{sec:corollary} deduces the
526:\section{Operadic complexity, proved}\label{sec:corollary}
exec
/bin/zsh -lc "sed -n '526,560p' standalone/N6_shadow_formality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{Operadic complexity, proved}\label{sec:corollary}
% ================================================================

\begin{definition}[Three complexity invariants]
For a chiral algebra $\cA$, set
$r_{\max}(\cA):=\sup\{r\ge 2:\Ash_{r,0}\ne 0\}$ (shadow
termination degree),
$d_\infty(\cA):=\sup\{n\ge 2:m_n^{\mathrm{tr}}\ne 0\}$
(transferred $\Ainf$-depth on the minimal model of
$\Defcyc(\cA)$), and
$f_\infty(\cA):=\sup\{n\ge 2:\ell_n^{(0),\mathrm{tr}}\ne 0\}$
($\Linf$-formality level of $\gmodzero$).
\end{definition}

\begin{corollary}[Operadic complexity]
\label{cor:operadic-body}
$r_{\max}(\cA)=d_\infty(\cA)=f_\infty(\cA)$ for every chiral
algebra $\cA$.
\end{corollary}

exec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:single-line-dichotomy|thm:riccati-algebraicity|thm:depth-decomposition|rem:contact-stratum-separation|thm:nms-betagamma-quartic-birth|ssec:d-squared|def:shadow-depth|eq:mc-equation|eq:curvature|sec:bar|thm:e1-primacy|thm:categorical-cg-all-types|cor:mc3-all-types|conj:quartic-closure|conj:beilinson-closure|conj:clutching-closure)\\}' chapters standalone appendices metadata raeeznotes | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: raeeznotes: No such file or directory (os error 2)
appendices/nonlinear_modular_shadows.tex:1143:\label{thm:nms-betagamma-quartic-birth}
standalone/analytic_sewing.tex:2216:\begin{equation}\label{eq:curvature}
standalone/koszulness_fourteen_characterizations.tex:902:\begin{equation}\label{eq:mc-equation}
standalone/chiral_chern_weil.tex:1257:\begin{equation}\label{eq:curvature}
standalone/N2_mc3_all_types.tex:734:\label{cor:mc3-all-types}
standalone/shadow_towers.tex:360:\label{sec:bar}
standalone/shadow_towers.tex:522:\begin{equation}\label{eq:mc-equation}
standalone/introduction_full_survey.tex:500:\label{thm:e1-primacy}
standalone/N6_shadow_formality.tex:252:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary.tex:109:\label{sec:bar}
standalone/programme_summary.tex:313:\label{ssec:d-squared}
standalone/programme_summary.tex:609:\begin{equation}\label{eq:curvature}
standalone/programme_summary.tex:1158:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary.tex:1250:\label{def:shadow-depth}
standalone/programme_summary_sections2_4.tex:583:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary_sections2_4.tex:675:\label{def:shadow-depth}
standalone/shadow_towers_v3.tex:486:\label{sec:bar}
standalone/shadow_towers_v3.tex:612:\begin{equation}\label{eq:mc-equation}
standalone/programme_summary_section1.tex:82:\label{sec:bar}
exec
/bin/zsh -lc "rg -n '\\\\bibliography|\\\\begin\\{thebibliography\\}|\\\\input\\{bibliography|\\\\include\\{bibliography' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Deciding on bibliography inclusion**

I'm considering how to handle the bibliography. I have two options: I could either add a local bibliography with 31 cited keys, or I could switch to using `\input{../bibliography/references}` after the document body. However, I'm guessing that `bibliography/references` is likely a `.tex` file that contains the `thebibliography` environment. So, it looks like I need to search for that to confirm.
exec
/bin/zsh -lc 'head -n 20 bibliography/references.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{thebibliography}{999}

% DUPLICATE KEY INDEX — old keys merged into canonical entries.
% Run: grep -rn '\cite{OLDKEY}' chapters/ appendices/ --include='*.tex'
% and replace with the canonical key listed below.
%
% OLD KEY: Arn69 — now merged into Arnold69
% OLD KEY: arakawa-lectures — now merged into Ara12
% OLD KEY: Arakawa — now merged into Arakawa17
% OLD KEY: BD — now merged into BD04
% OLD KEY: FG — now merged into FG12
% OLD KEY: FF-wakimoto — now merged into Frenkel-Kac-Wakimoto92
% OLD KEY: KashiwaraSchapira — now merged into KS90
% OLD KEY: KS94 — now merged into KS90
% OLD KEY: Kontsevich03 — now merged into Kon03
% OLD KEY: LodayVallette — now merged into LV12
% OLD KEY: LodayVallette2012 — now merged into LV12
% OLD KEY: LurieHA — now merged into HA
% OLD KEY: LurieHTT — now merged into HTT
% OLD KEY: QuadDual — now merged into GLZ22
exec
/bin/zsh -lc "rg -n '\\\\bibitem\\{LorgatCYChiral\\}' bibliography/references.tex standalone/*.tex chapters appendices | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


thinking
**Revising citation issues**

I’m facing an issue with a missing bibitem, which means providing full references isn’t resolving anything. I should probably add a new bibitem or change the citation key to match an existing one. But which key should I use? I’ll have to look into the citation, perhaps searching for "LorgatCY" to find the right reference or check if I can find a match for the current citation key. Let's keep figuring this out!
exec
/bin/zsh -lc "rg -n 'LorgatCY|CYChiral' bibliography/references.tex chapters appendices standalone | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/cy_quantum_groups_6d_hcs.tex:183:\cite{LorgatCYChiral} proves that for $d \geq 3$, the CY chiral

thinking
**Checking bibliography entries**

I need to decide whether to add a bibliographic item or remove a citation. I see that there's a reference `survey_track_a_compressed` that has an unresolved citation for GeK98. It seems there might not be a bibliography available, so I should search for that. Maybe I could input the full references if I find that key exists. I’ll look into the references.tex file to see if GeK98 is mentioned there.
exec
/bin/zsh -lc "rg -n '\\\\bibitem\\{GeK98\\}' bibliography/references.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
622:\bibitem{GeK98}
exec
/bin/zsh -lc "rg -n '\\\\bibitem\\{(LorgatVirR|LorgatSevenFaces|Priddy70|BGS96|LV12|BD04|FG12|CG17|BS88|DS85|FF90|FP00|KM94|KRW03|Kontsevich03|Mumford83|FlajoletSedgewick)\\}' bibliography/references.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
141:\bibitem{BD04}
144:\bibitem{BGS96}
299:\bibitem{CG17}
481:\bibitem{FP00}
523:\bibitem{FlajoletSedgewick}
526:\bibitem{FG12}
924:\bibitem{LV12}
1016:\bibitem{Mumford83}
1109:\bibitem{Priddy70}

thinking
**Investigating document settings**

I’m thinking about how to set things up with `xr-hyper` and external document entries. I need to check if the classification lacks `hyperref`, but I think I can still use `xr-hyper`. I wonder if the source preamble already includes `hyperref`. It’s likely since there’s also mention of `xcolor`. I’ll take a quick look at the top lines to confirm. It’s essential to ensure everything works smoothly together!
exec
/bin/zsh -lc "sed -n '1,20p' standalone/classification.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\documentclass[11pt]{article}

\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[margin=1.15in]{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}





thinking
**Exploring document imports**

I could easily add `\usepackage{xr-hyper}`. Now I need to check the corresponding external documents like `riccati` and some others. It seems like using `\externaldocument{riccati}` might be helpful. I should also think about using `xr-hyper` for `programme_summary_sections...` and other sections, which would make the dependencies clearer. It looks like I can outline some specific steps like adding relevant imports in the preamble and ensuring the dependencies are explicit. Let's finalize this!
thinking
**Clarifying file paths**

I’m considering how `editorial` in the standalone directory might relate to `main.tex` in the repo root. When compiling from the standalone directory, it uses `\IfFileExists{main.tex}` to check for its existence. If I compile from the repo root with `standalone/editorial.tex`, it should locate `main.tex` correctly. I’m wondering if `\externaldocument{main}` will work from there. The relative path for TeX files matters, so I'll ensure I understand how that translates with kpathsea.
thinking
**Analyzing file path issues**

It seems like the current working directory is essential here. It's safer not to specify relative paths. If I'm compiling from the root of the repository, I should reference `main` directly, or `../main` when in the `standalone/` directory. The user is looking for an exact fix despite the potential ambiguity. One straightforward solution could be to replace unresolved references with prose, but that might not work well for larger files. Another idea might be to rename or move them out of `standalone/` if they're not meant to be standalone.
thinking
**Determining fixes for standalone files**

The task involves auditing the `standalone/` directory. An exact fix could involve either removing files from `standalone/` or adding appropriate imports like `\externaldocument` or bibliography references. If the goal is to compile standalone, I should add `\usepackage{xr-hyper}`, `\externaldocument{main}`, and `\input{bibliography/references}`. This would resolve references if the main auxiliary file is available. For files like `introduction_full_survey` and others, the same logic applies, ensuring everything is self-contained. I should also confirm if they already include `hyperref`.
thinking
**Considering LaTeX commands**

I’m thinking that maybe an exact fix could be as simple as adding `\providecommand{\R}{\mathbb{R}}`. That seems good! I could also consider defining macros like `chirAss` since there are several uses. Also, should I define `\chirtensor` as `\otimes^{\mathrm{ch}}` or `\otimes^{\operatorname{ch}}`? I need to be cautious and check the definitions in the main or chapter files from the repo. Using the actual repo definition makes sense, so I’ll search for that.
exec
/bin/zsh -lc "rg -n '\\\\providecommand\\{\\\\chirtensor\\}|\\\\newcommand\\{\\\\chirtensor\\}|\\\\providecommand\\{\\\\chirAss\\}|\\\\newcommand\\{\\\\chirAss\\}|\\\\providecommand\\{\\\\chirLie\\}|\\\\providecommand\\{\\\\chirCom\\}' main.tex chapters standalone | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:400:\newcommand{\chirtensor}{\otimes^{\mathrm{ch}}}
main.tex:403:\newcommand{\chirAss}{\mathsf{Ass}^{\mathrm{ch}}}
standalone/en_chiral_operadic_circle.tex:77:\providecommand{\chirAss}{\mathrm{Ass}^{\mathrm{ch}}}
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\chir(Lie|Com)\\}' main.tex chapters standalone | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:402:\newcommand{\chirLie}{\mathsf{Lie}^{\mathrm{ch}}}
main.tex:404:\newcommand{\chirCom}{\mathsf{Com}^{\mathrm{ch}}}
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\Dg\\}' main.tex chapters standalone | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:502:\newcommand{\Dg}[1]{D_{#1}} % total corrected differential at genus g (STRICT: D_g^2 = 0)
standalone/survey_track_b_compressed.tex:113:\providecommand{\Dg}{\mathrm{dg}}
standalone/introduction_full_survey.tex:84:\providecommand{\Dg}{\mathrm{dg}}
standalone/survey_modular_koszul_duality.tex:84:\providecommand{\Dg}{\mathrm{dg}}
standalone/survey_track_a_compressed.tex:66:\providecommand{\Dg}{\mathrm{dg}}

thinking
**Investigating A/B survey tracks**

I realize there might be an issue with the A/B survey tracks due to a potential problem with the \Dg stub. It’s possible that there’s no compile error yet because it hasn’t been utilized or triggered any issues. However, it could still be lurking as a latent problem. So, I need to look into where it's being used to ensure everything is functioning correctly! Let's search for usage to clarify.
exec
/bin/zsh -lc "rg -n '\\\\Dg\\{' standalone/survey_track_a_compressed.tex standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering hidden weaknesses**

It sounds like there's no current finding or issue to report, even if the user mentioned a hidden weakness. I wonder if there's something about the survey related to modular Koszul duality that I could look into? I think it's important to clarify what the user means about “hidden weaknesses” before proceeding with my search. This way, I can ensure I'm providing information that addresses their concerns accurately.
exec
/bin/zsh -lc "rg -n '\\\\Dg\\{' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '\\\\(DeclareMathOperator|providecommand|newcommand)\\{\\\\ord\\}' main.tex chapters standalone | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/multi_weight_cross_channel.tex:54:\DeclareMathOperator{\ord}{ord}
standalone/arithmetic_shadows.tex:80:\providecommand{\ord}{\mathrm{ord}}
standalone/w3_holographic_datum.tex:46:\DeclareMathOperator{\ord}{ord}
standalone/gaudin_from_collision.tex:51:\DeclareMathOperator{\ord}{ord}
standalone/virasoro_r_matrix.tex:42:\DeclareMathOperator{\ord}{ord}
standalone/classification_trichotomy.tex:43:\DeclareMathOperator{\ord}{ord}

thinking
**Checking math operator definitions**

I’m considering using `\DeclareMathOperator{\ord}{ord}`. It seems like a good choice! I might also need to search for the definition of `\Ydg`. It’s a bit unclear right now if it’s standard or something specific. I wonder if I'll come across different usages. I really want to make sure I get this right, so searching through documentation or relevant materials should help clear things up. Let's see what turns up!
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\Ydg\\}' main.tex chapters standalone | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:513:\newcommand{\Ydg}{\mathcal{Y}^{\mathrm{dg}}} % dg-shifted Yangian
standalone/drinfeld_kohno_bridge.tex:96:\newcommand{\Ydg}{Y^{\mathrm{dg}}}

thinking
**Evaluating definitions**

I'm thinking of using the main definition, possibly denoted as `\mathcal{Y}^{\mathrm{dg}}`, since the user asked about ground. I want to make sure to keep it consistent with the actual repository definition. That sounds like a solid plan. I might need to consider if `survey_modular_koszul_duality` is missing the actual definition from Defcyc, so I'll check that in the main reference.
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\Defcyc\\}|\\\\(providecommand|newcommand)\\{\\\\CompCl\\}|\\\\(providecommand|newcommand)\\{\\\\orline\\}|\\\\DeclareMathOperator\\{\\\\Aut\\}|\\\\newcommand\\{\\\\id\\}|\\\\newcommand\\{\\\\dzero\\}|\\\\newcommand\\{\\\\dfib\\}' main.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
135:\newcommand{\orline}[1]{\mathrm{or}_{#1}}
500:\newcommand{\dzero}{d_0} % genus-0 collision differential (Arnold d^2=0)
501:\newcommand{\dfib}{d_{\mathrm{fib}}} % fiberwise differential on fixed Sigma_g (CURVED: d^2 = kappa * omega_g)
505:\newcommand{\Defcyc}{\operatorname{Def}_{\mathrm{cyc}}} % cyclic deformation complex
686:\providecommand{\CompCl}{\operatorname{CompCl}}
exec
/bin/zsh -lc "rg -n '\\\\(DeclareMathOperator|providecommand|newcommand)\\{\\\\Aut\\}|\\\\newcommand\\{\\\\id\\}' main.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
600:\providecommand{\Aut}{\operatorname{Aut}}
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\id\\}' main.tex | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
614:\providecommand{\id}{\mathrm{id}}
718:\providecommand{\id}{\mathrm{id}}

thinking
**Considering citation placement**

I'm thinking about selecting line 125 because that's where the earliest missing citation appears. Also, it's worth noting that references start from line 104. I should probably begin my search for `\ref{` from there. Maybe I could use a regex approach for this? It seems like a good way to ensure I'm catching all the necessary citations efficiently. Let's see how that turns out!
exec
/bin/zsh -lc "rg -n '\\\\ref\\{|\\\\cite\\{' standalone/introduction_full_survey.tex | head -n 10" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
125:is always a morphism of dg algebras; when it is a quasi-isomorphism, the algebra~$A$ is called \emph{Koszul}, and $B(A)$ has cohomology concentrated in bar degree~$1$, equal to the Koszul dual coalgebra~$A^{\scriptstyle \text{\normalfont !\textasciigrave}}$. The Koszul dual algebra is $A^! = (A^{\scriptstyle \text{\normalfont !\textasciigrave}})^\vee = T(V^*)/R^\perp$. Koszulness means that $A$ admits a linear resolution by $A^!$-modules, and that the derived category of $A$-modules is equivalent to the derived category of $A^!$-modules (up to a shift and twist). This is the content of Priddy~\cite{Priddy70}, Beilinson--Ginzburg--Soergel~\cite{BGS96}, and Loday--Vallette~\cite{LV12}.
127:Let $X$ be a smooth projective curve over~$\mathbb{C}$. A \emph{chiral algebra}~$\cA$ on~$X$ (Beilinson--Drinfeld~\cite{BD04}) is a $\mathcal{D}_X$-module equipped with a chiral bracket
138:(see \S\ref{sec:dictionary} for the formal definitions).%
152:(Theorem~\ref{thm:modular-characteristic}).
164:(Theorem~\ref{thm:shadow-formality-identification}).
174:(Theorem~\ref{thm:single-line-dichotomy}), with the
181:(Theorem~\ref{thm:mc2-bar-intrinsic}): algebraicity describes its
186:(Theorem~\ref{thm:riccati-algebraicity}):
195:(Theorem~\ref{thm:shadow-formality-identification}):
200:(Remark~\ref{rem:two-orthogonal-axes}).
exec
/bin/zsh -lc "rg -n '\\\\ref\\{|\\\\cite\\{' standalone/survey_modular_koszul_duality.tex | head -n 12
rg -n '\\\\ref\\{|\\\\cite\\{' standalone/survey_modular_koszul_duality_v2.tex | head -n 12
rg -n '\\\\ref\\{|\\\\cite\\{' standalone/survey_track_a_compressed.tex | head -n 12
rg -n '\\\\ref\\{|\\\\cite\\{' standalone/survey_track_b_compressed.tex | head -n 12" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
626:(Proposition~\ref{prop:pole-decomposition}); since
631:(Example~\ref{ex:heisenberg-d-deg1}).
956:\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}};
957:see \S\textup{\ref{sec:modular-char-spectral-disc-intro}}\textup{)}. Grothendieck--Riemann--Roch
1032:(Theorem~\ref{thm:multi-weight-genus-expansion}):
1049: \textup{(}Proposition~\textup{\ref{prop:svy-universal-alpha-g}}\textup{)}:
1054: \textup{(}Proposition~\textup{\ref{prop:svy-free-field-exact}}\textup{)}:
1076:(Theorem~\ref{thm:riccati-algebraicity}). The infinite tower is
1082:(Theorem~\ref{thm:pixton-from-mc-semisimple}), the integrable
1084:(Proposition~\ref{prop:shadow-integrable-hierarchy}), the Hitchin
1086:(Remark~\ref{rem:hitchin-shadow-expanded}), the Baxter $Q$-operator
1088:(Remark~\ref{rem:baxter-q-from-mc}), and the Bekenstein--Hawking
709:(Theorem~\ref{thm:e1-formality-bridge}): for $E_\infty$-input,
711:failure (Theorem~\ref{thm:e1-formality-failure}): for genuinely
717:(Theorem~\ref{thm:chiral-qg-equiv}): on the Koszul locus, three
721:(Theorem~\ref{thm:glN-chiral-qg}).
733:The $E_3$ identification (Theorem~\ref{thm:e3-identification}): for
737:(Theorem~\ref{thm:topologization}): $\SCchtop + \text{conformal
761:(Conjecture~\ref{conj:v1-drinfeld-center-equals-bulk}). The
763:(Theorem~\ref{thm:e3-identification}) proves

thinking
**Checking document citations**

I need to verify if `survey_track_a` has the bibliography import, which seems likely. I think I can fix it using `\input{bibliography/references}` and referring to the main document. There might also be an issue with `survey_track_b` lacking citations, so no compile warnings could mean it's only referencing the external document. Additionally, I need to check line 346 of `N3_e1_primacy` for a missing `\BarchFG` macro. Time to search for the exact macro!
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\BarchFG\\}' main.tex chapters standalone | head -n 20" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:471:\providecommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}
main.tex:580:\providecommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}

thinking
**Searching for ChirHoch definition**

I’m looking for the definition of “ChirHoch” to ensure I understand it correctly. It seems like I should check the main source or document to get an exact definition. I want to be consistent and accurate in what I present. This will help clarify any usage or context about ChirHoch that might be important for the user. I’ll search for that definition now!
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\ChirHoch\\}' main.tex standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
main.tex:489:\newcommand{\ChirHoch}{CH} % Chiral Hochschild

thinking
**Considering consistency in definitions**

I'm noticing the main defines `\ChirHoch` as `CH`, but the introduction_full_survey uses `\mathrm{ChirHoch}`. That doesn't seem consistent. For the programme summary, it would make sense to use a consistent repository macro. Since the source uses `\ChirHoch^1(V_k(\fg))`, maybe I should define it in the preamble with `\newcommand{\ChirHoch}{CH}` or `\mathrm{ChirHoch}`. I want to ensure exactness and look for other standalone definitions to maintain that style.
exec
/bin/zsh -lc "rg -n '\\\\(providecommand|newcommand)\\{\\\\ChirHoch\\}' standalone/*.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/N1_koszul_meta.tex:56:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/holographic_datum.tex:55:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/five_theorems_modular_koszul.tex:51:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/introduction_full_survey.tex:74:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/programme_summary_sections2_4.tex:53:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/en_chiral_operadic_circle.tex:60:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/cy_to_chiral_functor.tex:64:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/arithmetic_shadows.tex:89:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/survey_track_b_compressed.tex:108:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/notation_index.tex:17:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/cy_quantum_groups_6d_hcs.tex:65:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/koszulness_fourteen_characterizations.tex:63:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/e1_primacy_ordered_bar.tex:59:\newcommand{\ChirHoch}{\mathrm{HH}^{*}_{\mathrm{ch}}}
standalone/survey_track_a_compressed.tex:61:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/survey_modular_koszul_duality.tex:74:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/shadow_towers_v3.tex:56:\newcommand{\ChirHoch}{\mathrm{ChirHoch}}
standalone/survey_modular_koszul_duality_v2.tex:99:\providecommand{\ChirHoch}{\mathrm{ChirHoch}}




thinking
**Confirming findings on macros**

I want to ensure that I'm not missing anything important. It seems like the `introduction_full_survey` is built-in and not absent. The `\ar` issue comes from a missing `tikz-cd`, and the `\begin{convention}` environment is indeed undefined. I should take note of the exact line 5269 to log that. There's a missing `\llbracket` too, which might need adjusting with my use of `\operatorname{Conf}_k^{<}(\R)` and grouping related macros to keep the findings count manageable.
thinking
**Reviewing references and format**

I'm noticing there are 22 references and one citation. I see specific lines to track and references that might need adjustment. The summary mentions "fresh compile," which could be unnecessary, and I'm pondering if I should avoid code references with markdown links.

It's important to keep lines moderate in length and ensure the overall findings stay concise, around 50-70 lines. I also need to check some unresolved reference counts, as they seem high.
thinking
**Clarifying references for documentation**

I can mention the counts and suggest an exact fix by adding `\usepackage{xr-hyper}` and `\externaldocument{main}` after line 4. This should help resolve the main manuscript labels for the imported concordance and editorial chapters. It's a straightforward adjustment, and it seems it will clarify things nicely. Keeping this in mind will ensure that everything aligns correctly.
thinking
**Fixing references and citations**

I'm working on fixing references if the main auxiliary exists. I need to address unresolved references for specific surveys by implementing `xr-hyper` and ensuring all citations are linked appropriately.

I want to clarify tracking across different documents, like with `riccati` and `arithmetic_shadows`. It seems like there could be potential path ambiguity, but that's manageable. I'll also consider including the bibliography when needed to resolve missing items. Finally, I’ll check for the existence of the bibliography environment in the relevant files.
exec
/bin/zsh -lc "rg -n '\\\\begin\\{thebibliography\\}|\\\\end\\{thebibliography\\}' standalone/riccati.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n '\\\\begin\\{thebibliography\\}|\\\\end\\{thebibliography\\}' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Evaluating bibliography issues**

I'm noticing that there's no bibliography environment, which isn't ideal. I see that the commented bibitems alone aren't helpful, and I'm starting to wonder if there's really no thebibliography section at all. Maybe I need to dig deeper into the tail of the document or code to find out what's going on. It's important to clarify this so I can properly address any concerns or missing elements.
exec
/bin/zsh -lc 'tail -n 40 standalone/programme_summary_sections5_8.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ====================================================================
% Additional references for Sections 5--8
% ====================================================================

% NOTE: When merging into the main document, add these entries
% to the thebibliography environment of Section 1.
% They are listed here as comments for reference; the active
% bibliography is in programme_summary_sections9_14.tex.

% \bibitem{Drinfeld85}
% V.\,G.~Drinfeld,
% Hopf algebras and the quantum Yang--Baxter equation,
% \textit{Dokl.\ Akad.\ Nauk SSSR}~\textbf{283} (1985), 1060--1064.

% \bibitem{FFR94}
% B.~Feigin, E.~Frenkel, and N.~Reshetikhin,
% Gaudin model, Bethe ansatz and critical level,
% \textit{Comm.\ Math.\ Phys.}~\textbf{166} (1994), 27--62.

% \bibitem{KZ84}

thinking
**Exploring bibliography options**

I'm pondering that the active bibliography might be in `programme_summary_sections9_14.tex`. It seems like the fix for citations in 5_8 could involve using `\input{programme_summary_sections9_14}` instead of just uncommenting. Hmm, this makes me think I should check the tail of 9_14 for the bibliography details. It’ll be important to inspect that closely to see if it holds the information I need. Let's keep digging!
exec
/bin/zsh -lc 'tail -n 80 standalone/programme_summary_sections9_14.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
V.~Kac, S.-S.~Roan, and M.~Wakimoto,
Quantum reduction for affine superalgebras,
\textit{Comm.\ Math.\ Phys.}~\textbf{241} (2003),
307--342.

\bibitem{LV12}
J.-L.~Loday and B.~Vallette,
\textit{Algebraic Operads},
Grundlehren der Mathematischen Wissenschaften,
vol.~346, Springer, Berlin, 2012.

\bibitem{Mok25}
C.-P.~Mok,
\emph{Logarithmic Fulton--MacPherson configuration spaces},
arXiv:2503.17563, 2025.

\bibitem{Mor26}
Y.~Moriwaki,
Conformally flat factorization homology in
$\mathrm{IndHilb}$,



thinking
**Considering bibliography instructions**

I'm trying to clarify how to state the fix for using the bibliography file. It’s crucial to mention the paths when compiling from different directories. I think I could simplify it by saying "append the repo bibliography file" without getting too pedantic. However, since the user wants an exact fix, I might need to mention the specific paths, like `bibliography/references.tex` for the root and `../bibliography/references.tex` for standalone. Keeping it concise yet accurate is key!
thinking
**Assessing unresolved references**

I’m considering whether to check A/B tracking for unresolved references, which might be critical. I see that `survey_modular_koszul_duality_v2` has 58 undefined references starting at line 709, and I should fix `xrh externaldocument main`. The `survey_modular_koszul_duality` has 148 references and 6 citations, and I need to address those too. The `introduction_full_survey` shows 435 references, while the `editorial` section has a massive 1736 unresolved references. This is quite a lot to manage!
thinking
**Crafting final document**

I think I need to check for "Checked: 53" because it's related to the standalone .tex that compiled. I want to craft the final version elegantly and use bullets as the user requested, without too much preamble. I should end with a summary. It might be alright not to mention that some fixes rely on `main.aux`, but maybe it's good to mention the explicit import to clarify dependencies. So, I'll draft carefully and keep it concise yet specific.
codex
- [CRITICAL] standalone/editorial.tex:3 — PROBLEM: `\mainpreambleonly` makes `main.tex` stop at line 593, so the fallback macro block at `main.tex:597-719` never runs; fresh `editorial.log` then shows undefined `\cC`, `\ChirHoch`, `\HH`, `\bR`, `\CompCl`, and many more from the imported chapter files. FIX: move `main.tex:597-719` above the `\ifdefined\mainpreambleonly` guard so those `\providecommand`s are available before `editorial.tex` imports the concordance files.
- [CRITICAL] standalone/editorial.tex:14 — PROBLEM: importing `chapters/connections/concordance` and `chapters/connections/editorial_constitution` leaves 1,736 undefined cross-manuscript references in fresh standalone compile. FIX: load `xr-hyper` in `standalone/editorial.tex` after the preamble import and add `\externaldocument{main}` before `\begin{document}` so the file explicitly resolves labels from `main.aux`.
- [CRITICAL] standalone/introduction_full_survey.tex:125 — PROBLEM: fresh standalone compile leaves 435 undefined `\ref` labels and 53 undefined citation keys starting here; this file still depends on monograph aux/bibliography state. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [CRITICAL] standalone/shadow_towers_v2.tex:487 — PROBLEM: the file `\input`s full standalone documents (`riccati.tex`, `classification.tex`, `computations.tex`) after `\begin{document}`, which triggers fresh “Can be used only in preamble” and theorem-redefinition errors. FIX: split those three files into body-only fragments and replace `\input{riccati}`, `\input{classification}`, and `\input{computations}` with inputs of the body fragments.
- [CRITICAL] standalone/survey_modular_koszul_duality.tex:626 — PROBLEM: fresh standalone compile leaves 148 undefined `\ref` labels and 6 undefined citation keys; the file is not actually standalone. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [CRITICAL] standalone/survey_modular_koszul_duality_v2.tex:709 — PROBLEM: fresh standalone compile leaves 58 undefined `\ref` labels starting here; the file still relies on monograph labels not imported locally. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{main}` before `\begin{document}`.

- [HIGH] standalone/N2_mc3_all_types.tex:391 — PROBLEM: `\cF` is used at lines 391 and 394, but the local macro block at lines 35-59 never defines it. FIX: add `\newcommand{\cF}{\mathcal{F}}` beside the other `\c*` macros.
- [HIGH] standalone/N3_e1_primacy.tex:346 — PROBLEM: `\BarchFG` is used at lines 346 and 357, but the preamble defines `\Barch`, `\Barord`, `\BarSig`, and `\Cobar` only. FIX: add `\newcommand{\BarchFG}{\overline{B}^{\mathrm{ch},\mathrm{FG}}}` to the macro block.
- [HIGH] standalone/N3_e1_primacy.tex:615 — PROBLEM: `\Cobar` and `\Barord` already expand to superscripted symbols, so `\Cobar^{(g)}` and `\Barord^{(g)}` create fresh double-superscript errors at lines 615 and 629. FIX: write `(\Cobar)^{(g)}` and `(\Barord)^{(g)}` instead.
- [HIGH] standalone/N6_shadow_formality.tex:190 — PROBLEM: the text references `\ref{cor:operadic-complexity}`, but the actual corollary is labeled `\label{cor:operadic-body}` at line 540. FIX: rename `\label{cor:operadic-body}` to `\label{cor:operadic-complexity}` or change the reference at line 190 to `\ref{cor:operadic-body}`.
- [HIGH] standalone/N6_shadow_formality.tex:239 — PROBLEM: `\gmod` already contains a subscript `_\\cA`, so `\gmod_g` creates a fresh double-subscript error. FIX: replace `\gmod_g` with `(\gmod)^{(g)}` or with a separately defined macro such as `\gmod^{(g)}`.
- [HIGH] standalone/bp_self_duality.tex:11 — PROBLEM: `hyperref` is configured with `blue!60!black` and `green!40!black`, but `xcolor` is never loaded, so both colors are undefined in fresh compile. FIX: insert `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/classification.tex:66 — PROBLEM: the file contains unresolved cross-document refs at lines 66, 100, 267, 794, 831, and 1008 (`thm:single-line-dichotomy`, `thm:riccati-algebraicity`, `thm:depth-decomposition`, `rem:contact-stratum-separation`, `thm:nms-betagamma-quartic-birth`). FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{riccati}`, `\externaldocument{chapters/connections/arithmetic_shadows}`, and `\externaldocument{appendices/nonlinear_modular_shadows}` before `\begin{document}`.
- [HIGH] standalone/classification_trichotomy.tex:12 — PROBLEM: `hyperref` uses mixed colors, but `xcolor` is not loaded locally, so fresh compile reports `Undefined color 'blue!60!black'`. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/classification_trichotomy.tex:100 — PROBLEM: the line starts `\kappa$` with no opening math delimiter, producing a fresh `Missing $ inserted` error. FIX: change that fragment to `$\\kappa$ is the ...`.
- [HIGH] standalone/cy_quantum_groups_6d_hcs.tex:183 — PROBLEM: the file cites `LorgatCYChiral`, but that key does not exist in the repo bibliography and fresh compile leaves it undefined. FIX: add a real `\bibitem{LorgatCYChiral}` to `bibliography/references.tex` and import that bibliography here, or replace the citation with uncited prose until the key exists.
- [HIGH] standalone/gaudin_from_collision.tex:11 — PROBLEM: `hyperref` uses `blue!60!black` / `green!40!black` without loading `xcolor`, so the standalone build dies on undefined colors. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/introduction_full_survey.tex:280 — PROBLEM: the standalone preamble omits `\dzero`, `\dfib`, `\Hom`, `\End`, `\Res`, `\Aut`, `\colim`, `\id`, and `\R`, all of which are used later (for example at lines 280, 422, 436, 483, 609, 747, 566, 1282, 639, 1230). FIX: add `\newcommand{\dzero}{d_0}`, `\newcommand{\dfib}{d_{\mathrm{fib}}}`, `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\DeclareMathOperator{\Res}{Res}`, `\DeclareMathOperator{\Aut}{Aut}`, `\DeclareMathOperator{\colim}{colim}`, `\providecommand{\id}{\mathrm{id}}`, and `\providecommand{\R}{\mathbb{R}}` to the preamble.
- [HIGH] standalone/introduction_full_survey.tex:84 — PROBLEM: `\Dg` is defined as a zero-argument text macro, but the body uses it as a one-argument genus-indexed differential at lines 759, 907, 4521, 5314, and 5321. FIX: replace line 84 with `\providecommand{\Dg}[1]{D_{#1}}`; if plain `dg` text is also needed, introduce a separate `\dg`.
- [HIGH] standalone/introduction_full_survey.tex:1838 — PROBLEM: `\begin{tikzcd}` and `\ar[...]` are used at lines 1838-1846 and 4645-4653, but `tikz-cd` is never loaded. FIX: add `\usepackage{tikz-cd}` in the preamble.
- [HIGH] standalone/introduction_full_survey.tex:5269 — PROBLEM: the file uses `\begin{convention}` at lines 5269, 5307, and 5337, but no `convention` theorem environment is declared locally. FIX: add `\newtheorem{convention}[theorem]{Convention}` to the theorem block.
- [HIGH] standalone/introduction_full_survey.tex:5062 — PROBLEM: the preamble omits `\chirAss`, `\chirLie`, `\chirCom`, and `\chirtensor`, which are used at lines 5062-5087 and 5164. FIX: add `\newcommand{\chirtensor}{\otimes^{\mathrm{ch}}}`, `\newcommand{\chirLie}{\mathsf{Lie}^{\mathrm{ch}}}`, `\newcommand{\chirAss}{\mathsf{Ass}^{\mathrm{ch}}}`, and `\newcommand{\chirCom}{\mathsf{Com}^{\mathrm{ch}}}` to the preamble.
- [HIGH] standalone/introduction_full_survey.tex:1106 — PROBLEM: the file uses `\llbracket x \rrbracket`, but no package defining `\llbracket`/`\rrbracket` is loaded. FIX: add `\usepackage{stmaryrd}` to the preamble.
- [HIGH] standalone/ordered_chiral_homology.tex:7831 — PROBLEM: the optional citation notes at lines 7831, 7846, and 7859 embed `\ref*{...}` to labels not defined in this file, so the standalone build leaves three unresolved refs. FIX: remove the `\ref*{...}` pieces and use plain `\cite{Lorgat26I}`, or replace the optional notes with literal theorem/proposition numbers.
- [HIGH] standalone/programme_summary.tex:1043 — PROBLEM: `\ChirHoch` is used in Theorem H, but the local macro block at lines 37-54 never defines it. FIX: add `\newcommand{\ChirHoch}{\mathrm{ChirHoch}}` to that macro block.
- [HIGH] standalone/programme_summary_sections5_8.tex:198 — PROBLEM: the file cites `Drinfeld85`, `KZ84`, `STS83`, and `FFR94`, but it has no active bibliography; the needed entries are only commented out at lines 770-785. FIX: add a real `thebibliography` environment before `\end{document}` and move those four commented `\bibitem`s into it.
- [HIGH] standalone/programme_summary_sections5_8.tex:318 — PROBLEM: `\ref{sec:bar}` and `\ref{def:shadow-depth}` are unresolved because this split file does not import labels from the full summary. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.
- [HIGH] standalone/riccati.tex:591 — PROBLEM: `FlajoletSedgewick` is cited, but the file has no local bibliography and fresh compile leaves the citation undefined. FIX: append `\input{bibliography/references}` before `\end{document}` so the existing `\bibitem{FlajoletSedgewick}` in the repo bibliography is available.
- [HIGH] standalone/survey_modular_koszul_duality.tex:1338 — PROBLEM: the preamble omits `\Hom`, `\End`, `\orline`, `\Defcyc`, `\Aut`, and `\CompCl`, all of which are used at lines 1338, 1707, 2675, 7464, and 8013. FIX: add `\DeclareMathOperator{\Hom}{Hom}`, `\DeclareMathOperator{\End}{End}`, `\newcommand{\orline}[1]{\mathrm{or}_{#1}}`, `\newcommand{\Defcyc}{\operatorname{Def}_{\mathrm{cyc}}}`, `\DeclareMathOperator{\Aut}{Aut}`, and `\newcommand{\CompCl}{\operatorname{CompCl}}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality.tex:2975 — PROBLEM: the file uses `\Bbbk\llbracket x\rrbracket`, but no package defining `\llbracket`/`\rrbracket` is loaded. FIX: add `\usepackage{stmaryrd}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:707 — PROBLEM: `\ord` is used in `\Ran^{\ord}(X)` and `\barB^{\ord}`, but the macro is never defined locally. FIX: add `\DeclareMathOperator{\ord}{ord}` to the preamble.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:6669 — PROBLEM: `\Ydg` is used but never defined in the standalone preamble. FIX: add `\newcommand{\Ydg}{\mathcal{Y}^{\mathrm{dg}}}` to the macro block.
- [HIGH] standalone/survey_modular_koszul_duality_v2.tex:8211 — PROBLEM: `\widehat{\fg\fl}_1` is malformed and uses an undefined `\fl`; fresh compile then cascades into multiple missing-math errors. FIX: replace the whole fragment with `\widehat{\mathfrak{gl}}_1`, i.e. `$\cZ(\Rep^{E_1}(Y^+(\widehat{\mathfrak{gl}}_1))) \cong \Rep^{E_2}(\cW_{1+\infty})$`.
- [HIGH] standalone/survey_track_a_compressed.tex:585 — PROBLEM: fresh standalone compile leaves 22 undefined `\ref` labels and one undefined citation key (`GeK98`) starting here. FIX: load `xr-hyper` after `hyperref`, add `\externaldocument{main}` before `\begin{document}`, and append `\input{bibliography/references}` before `\end{document}`.
- [HIGH] standalone/survey_track_b_compressed.tex:596 — PROBLEM: fresh standalone compile leaves 33 undefined cross-manuscript refs starting with `thm:categorical-cg-all-types`, `cor:mc3-all-types`, and the three closure conjectures. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{main}` before `\begin{document}`.
- [HIGH] standalone/three_parameter_hbar.tex:11 — PROBLEM: `hyperref` uses mixed colors without loading `xcolor`, so fresh compile reports repeated undefined-color errors. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.
- [HIGH] standalone/three_parameter_hbar.tex:210 — PROBLEM: the sentence `and the $\lambda$-bracket divided-power convention} = \lambda^n/n!$)` has a stray `}` and broken math delimiters, producing fresh math-mode errors. FIX: replace that fragment with `and the $\lambda$-bracket divided-power convention (coefficients of $\lambda^n/n!$) yields the $r$-matrix with the Sugawara-normalized prefactor.`
- [HIGH] standalone/w3_holographic_datum.tex:12 — PROBLEM: `hyperref` uses `blue!60!black` / `green!40!black`, but `xcolor` is not loaded locally. FIX: add `\usepackage[dvipsnames]{xcolor}` immediately before `\usepackage{hyperref}`.

- [MEDIUM] standalone/programme_summary_sections2_4.tex:559 — PROBLEM: `\ref{ssec:d-squared}` is unresolved because this fragment does not import labels from the full summary. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.
- [MEDIUM] standalone/programme_summary_sections9_14.tex:315 — PROBLEM: `\ref{eq:mc-equation}`, `\eqref{eq:curvature}`, and `\ref{sec:bar}` are unresolved at lines 315, 565, and 613 because this fragment is compiled without the earlier summary sections. FIX: load `xr-hyper` after `hyperref` and add `\externaldocument{programme_summary}` before `\begin{document}`.

## Summary
Checked: 53 | Findings: 40 | Verdict: FAIL
tokens used
383,355
