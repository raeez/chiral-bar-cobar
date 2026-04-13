# S14_standalone_to_main (793s)

- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:2364) — PROBLEM: the Swiss-cheese/bulk-boundary scoping drifts in three places: line 2364 reverses the pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, line 6193 says “The bar complex carrying both structures is an `SC^{ch,top}`-algebra,” and line 7758 repeats the reversed pair after assigning the closed/open colours to the bar differential/coproduct. That contradicts the same file at lines 6070–6071 and [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466). FIX: normalize every occurrence to `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)` or `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )`, and replace the stale SC-on-bar sentences with “the bar complex supplies the `E_1` differential and deconcatenation coproduct; `SC^{ch,top}` emerges on the derived center pair.”
- [HIGH] [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:1515) — PROBLEM: line 1515 reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and line 3658 later says the bar differential/coproduct encode the closed/open colours. The corrected manuscript surface uses `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )` and keeps `SC^{ch,top}` off the bar complex: see [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466) and [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247). FIX: swap the pair order at line 1515, and replace the line-3658 sentence with “the bar complex is the `E_1` coalgebraic engine; the closed/open Swiss-cheese colours live on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) — PROBLEM: lines 995–997 say the bar differential “encodes the closed colour” and the coproduct “the open colour.” That is exactly the AP165/ B55–B56 retracted formulation; the corrected rule is in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1257). FIX: replace those lines with “the bar complex classifies twisting morphisms and carries an `E_1` differential plus deconcatenation coproduct; the Swiss-cheese closed/open colours belong to the derived center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [MEDIUM] [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:1395) — PROBLEM: this line reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, but the same file already gives the corrected order at lines 663–664, and the main introduction fixes the order at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466). FIX: change the phrase to “the derived center pair `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)`,” and, if desired, append “closed/bulk first, open/boundary second” once to lock the convention.
- [MEDIUM] [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:1317) — PROBLEM: the pair is written in the wrong order as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, drifting from the main manuscript convention `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )`. FIX: swap the order and rewrite the sentence as “the derived center pair `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)` carries the `\SCchtop`-algebra structure.”
- [HIGH] [computations.tex](/Users/raeez/chiral-bar-cobar/standalone/computations.tex:33) — PROBLEM: this file, plus [classification.tex](/Users/raeez/chiral-bar-cobar/standalone/classification.tex:38), [programme_summary_sections2_4.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:63), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:62), [programme_summary_sections9_14.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections9_14.tex:61), [riccati.tex](/Users/raeez/chiral-bar-cobar/standalone/riccati.tex:36), [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:107), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:94), [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:149), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:102), and [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:165), overrides `\ref` globally with `\renewcommand{\ref}`. If any of these files are input into the manuscript, they silently mutate the main reference macro. FIX: delete every `\renewcommand{\ref}` block; introduce a local wrapper instead, e.g. `\providecommand{\localref}[1]{\hyperref[#1]{\textup{\ref*{#1}}}}`, and update local calls from `\ref{...}` to `\localref{...}`.
- [MEDIUM] [N1_koszul_meta.tex](/Users/raeez/chiral-bar-cobar/standalone/N1_koszul_meta.tex:34) — PROBLEM: unconditional `\newcommand`/` \DeclareMathOperator` preamble blocks remain widespread across the standalone surface: [N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:35), [N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:34), [N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:33), [N5_mc5_sewing.tex](/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:33), [N6_shadow_formality.tex](/Users/raeez/chiral-bar-cobar/standalone/N6_shadow_formality.tex:33), [bp_self_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/bp_self_duality.tex:36), [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:37), [classification_trichotomy.tex](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:33), [gaudin_from_collision.tex](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:36), [garland_lepowsky.tex](/Users/raeez/chiral-bar-cobar/standalone/garland_lepowsky.tex:36), [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/genus1_seven_faces.tex:33), [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:39), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:37), [programme_summary_section1.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex:36), [seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/seven_faces.tex:32), [shadow_towers.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:32), [shadow_towers_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v2.tex:35), [three_parameter_hbar.tex](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:34), [virasoro_r_matrix.tex](/Users/raeez/chiral-bar-cobar/standalone/virasoro_r_matrix.tex:33), and [w3_holographic_datum.tex](/Users/raeez/chiral-bar-cobar/standalone/w3_holographic_datum.tex:32). This violates the import-safe seam contract. FIX: change every custom symbol macro from `\newcommand` to `\providecommand`; replace shared-macro mutations like `\renewcommand{\Bbbk}`/`\renewcommand{\SS}` with local names; guard operator declarations with `\@ifundefined{...}{\DeclareMathOperator...}{}` or rewrite them as `\providecommand{\Res}{\operatorname{Res}}`.

## Summary
Checked: 16 | Findings: 9 | Verdict: FAIL


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
session id: 019d8744-634d-7660-94be-fa0bba6d654b
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


MISSION: SEAM AUDIT between standalone/ and chapters/.

Standalones→Main manuscript. Check: (a) formulas in standalone papers match the main text, (b) no convention drift, (c) macros defined via providecommand, (d) no stale claims

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers

thinking
**Planning file access**

I need to read certain files for AGENTS, and possibly use the explorer to gather them. Before diving into substantive work, I should do a commentary update. It might be good to update the plan too, although that's not strictly necessary. I also want to read relevant skill files, and maybe use multi_tool_use.parallel for reading in parallel. So, starting with a commentary update and acknowledging the first step sounds like a good plan; I'll mention using deep-beilinson-audit.
codex
I’m auditing the `standalone/` to `chapters/` seam for formula, convention, macro, and stale-claim drift. I’m starting by loading the required constitutional files and the audit skill, then I’ll map which standalone files actually overlap the main manuscript before reading transition points in detail.
Plan update
  → Read required repo constitution files and the deep-beilinson-audit skill
  • Map standalone files to overlapping chapter surfaces and identify transition points
  • Read overlapping sources carefully and record seam inconsistencies with exact fixes
  • Re-verify findings and deliver severity-ranked audit summary
exec
/bin/zsh -lc "pwd && rg --files -g 'AGENTS.md' -g 'CLAUDE.md' -g 'chapters/connections/concordance.tex' -g 'metadata/theorem_registry.md' -g 'raeeznotes/raeeznotes100/red_team_summary.md' -g 'archive/raeeznotes/raeeznotes100/red_team_summary.md' -g '.agents/skills/deep-beilinson-audit/SKILL.md' -g 'standalone/**' -g 'chapters/**'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
AGENTS.md
chapters/examples/n2_superconformal.tex
chapters/examples/level1_bridge.tex
chapters/examples/minimal_model_examples.tex
chapters/examples/yangians_computations.tex
chapters/examples/free_fields.aux
chapters/frame/preface_sections10_13_draft.tex
chapters/frame/preface_sections2_4_draft.tex
chapters/frame/guide_to_main_results.tex
chapters/frame/preface.tex
chapters/frame/heisenberg_frame.tex
chapters/frame/preface_section1_v2.tex
chapters/frame/preface_section1_draft.tex
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
chapters/frame/preface_sections5_9_draft.tex
chapters/frame/heisenberg_frame.aux
chapters/frame/preface.aux
codex
I’ve mapped the repo surface. Next I’m reading the audit skill and the required constitutional files, then I’ll isolate which `standalone/*.tex` surfaces are genuinely duplicated or mirrored in `chapters/` so the seam audit stays evidence-driven rather than broad speculation.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
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
 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |


thinking
**Organizing Chapters and Standalones**

I’m mapping relevant standalones to chapters, possibly using filename similarities to find connections. I might search for standalone names within the chapters to find overlaps. Each standalone paper could fit into its own chapter, especially if they share similar titles. Identifying these files will be key, like matching `genus1_seven_faces.tex` with its related chapter file. I should consider all standalone papers and see how they can overlap across multiple chapters while checking for label duplicates.
thinking
**Mapping Theorem Labels**

I’m considering searching for identical theorem labels across the standalone files and chapters, which could create a useful mapping. It might be helpful to extract filenames along with their \title or \chapter elements. I could use a script to search for these specific patterns in both standalone and chapter files. However, this could produce a lot of data, so I should focus on creating a list of standalone tex files and then check for matching basenames in the chapters. A structured loop could help with this!
codex
The seam is broad enough that filename overlap alone will miss drift. I’m now extracting direct duplication signals: shared basenames, reused labels, and repeated named formulas between `standalone/*.tex` and `chapters/**` so I can read the actual collision surfaces rather than random files.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
standalones=sorted(Path('standalone').glob('*.tex'))
chapters=[p for p in Path('chapters').rglob('*.tex')]
chapter_bases={p.stem:str(p) for p in chapters}
for s in standalones:
    base=s.stem
    matches=[str(p) for p in chapters if p.stem==base]
    if matches:
        print(f'{s}:')
        for m in matches:
            print('  ',m)
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
standalones=sorted(Path('standalone').glob('*.tex'))
chapters=[p for p in Path('chapters').rglob('*.tex')]
for s in standalones:
    base=s.stem
    matches=[str(p) for p in chapters if p.stem==base]
    if matches:
        print(f'{s}:')
        for m in matches:
            print('  ',m)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/genus1_seven_faces.tex:
   chapters/connections/genus1_seven_faces.tex
standalone/w3_holographic_datum.tex:
   chapters/examples/w3_holographic_datum.tex
exec
/bin/zsh -lc 'for f in standalone/*.tex; do echo "FILE: $f"; rg -n '"'"'^'"\\\\title|"'^'"\\\\chapter|"'^'"\\\\section\\*?\\{|"'^'"\\\\subsection\\*?\\{|"'^'"\\\\begin\\{(theorem|proposition|lemma|conjecture|definition|remark|corollary)\\}|"'^'"\\\\label\\{' \""'$f" | head -n 40; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 89ms:
48:\title{Shadow obstruction towers and the algebraicity of chiral deformation invariants}
93:\begin{remark}[Relationship to companion papers]
105:\section{Introduction}\label{sec:intro}
107:\subsection{Vertex algebras and moduli of curves}
127:\subsection{The bar construction and the shadow obstruction tower}
180:\subsection{Main results}
186:\begin{theorem}[Riccati algebraicity; Theorem~\ref{thm:riccati}]
187:\label{thm:intro-riccati}
213:\begin{theorem}[Four-class partition; Theorem~\ref{thm:dichotomy}]
214:\label{thm:intro-classification}
240:\begin{theorem}[Shadow connection; Theorem~\ref{thm:connection}]
241:\label{thm:intro-connection}
259:\begin{theorem}[Genus-$2$ universality; Theorem~\ref{thm:genus2}]
260:\label{thm:intro-genus2}
291:\subsection{Context}
322:\subsection{Notation and conventions}
359:\section{Chiral Koszul pairs and the bar construction}
360:\label{sec:bar}
362:\subsection{The chiral bar complex}
375:\begin{definition}[Chiral bar complex]

thinking
**Evaluating file outputs**

I’ve noticed that the output is truncated for genus1 and possibly other large files. I need to focus on mapping these carefully, especially the seam inconsistencies. I might be able to automate comparisons for shared labels or unique formulas. I want to ground this work in the actual lines I've read. Using diff tools on relevant overlapping pairs could help as well. I'll extract all labels from standalone papers and find matches in chapters to identify overlaps.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
import re
standalone_labels={}
for f in Path('standalone').glob('*.tex'):
    text=f.read_text(errors='ignore')
    standalone_labels[f]=re.findall(r'\\\\label\\{(["'^}]+)'"\\}', text)
chapters_text={p:p.read_text(errors='ignore') for p in Path('chapters').rglob('*.tex')}
for f, labels in sorted(standalone_labels.items()):
    hits=[]
    for lab in labels:
        ms=[str(p) for p,t in chapters_text.items() if f'\\\\label{{{lab}}}' in t or f'\\\\ref{{{lab}}}' in t]
        if ms:
            hits.append((lab, ms[:6]))
    if hits:
        print(f'FILE: {f}')
        for lab, ms in hits[:25]:
            print(' ', lab)
            for m in ms:
                print('    ', m)
        if len(hits)>25:
            print('  ...', len(hits)-25, 'more')
        print()
PY" in /Users/raeez/chiral-bar-cobarcodex
The overlap map is now label-based rather than filename-based. I’m waiting on that scan, then I’ll read the highest-collision pairs directly and only keep findings that survive line-by-line verification on both sides of the seam.
 succeeded in 9.28s:
FILE: standalone/N1_koszul_meta.tex
  def:chiral-koszul-morphism
     chapters/theory/algebraic_foundations.tex
     chapters/theory/chiral_hochschild_koszul.tex
     chapters/theory/chiral_koszul_pairs.tex
     chapters/theory/higher_genus_foundations.tex
     chapters/theory/bar_cobar_adjunction_inversion.tex
     chapters/connections/concordance.tex
  thm:koszul-equivalences-meta
     chapters/theory/algebraic_foundations.tex
     chapters/theory/chiral_hochschild_koszul.tex
     chapters/theory/introduction.tex
     chapters/theory/chiral_koszul_pairs.tex
     chapters/theory/higher_genus_foundations.tex
     chapters/theory/bar_cobar_adjunction_inversion.tex
  rem:d-module-purity-content
     chapters/theory/chiral_koszul_pairs.tex
  sec:examples
     chapters/theory/en_koszul_duality.tex







thinking
**Audit considerations for content seams**

I need to audit the transitions between standalone sections and chapters. This involves checking formulas, identifying any convention drifts, and reviewing macros through providecommand. I might want to focus on matching labels and duplicate statements while ensuring thoroughness. It could be helpful to run automated checks on defined macros, record exact findings without edits, and carefully read through transition points. I also need to determine the approach by identifying the most significant overlaps between standalone files and their respective chapters.
thinking
**Comparing macro definitions**

I’m considering using a script to compare macro definitions in several categories, like checking if formulas match, identifying convention drift, and confirming macros defined with providecommand. I can use grep to search for `\newcommand` or `\def` in standalone papers. These macros should ideally use `\providecommand` to avoid conflicts. I really need to inspect preambles in standalone files carefully, focusing on exact lines that could cause issues when imported into the main manuscript.
thinking
**Identifying seam issues with macros**

If there's a use of `\newcommand`, it indicates a seam issue. Since the user wants clarity between standalones and the main manuscript, I must pinpoint the exact files and lines causing problems. The fix would involve replacing `\newcommand` with `\providecommand` or applying a guard. However, I might not need to worry about every `\newcommand` if they're part of standard packages. Still, I should focus on custom macros in relevant standalones that could potentially collide.
thinking
**Evaluating audit procedures**

I need to conduct an exhaust audit on the surface, focusing on standalone tex preambles for macro definitions. Automating the count sounds good, but that could lead to a huge output, so I'll aim for concise but complete reporting on every issue found.

Identifying significant seam inconsistencies is crucial. I might use automated comparisons for shared labels and formulas between standalone sections and chapters, checking for mismatches. A script could help compare label definitions and verify potential issues based on known architectural mismatches.
thinking
**Checking for stale claims**

I need to check if the standalone claims are still stale, particularly looking for forbidden formulas or issues with the SC on bar. This might indicate problems directly related to seams versus chapters and concordance.

I can compare files like `survey_track_b_compressed.tex` for references to Swiss-cheese on bar or E3-chiral with the main text. I'll search standalone files for forbidden phrases and confirm against the chapters to ensure any corrections were made. Using grep for blacklist patterns across standalone documents will help surface potential issues. The same goes for specific formulas in `chiral_chern_weil.tex`, `garland_lepowsky.tex`, and others. I'll perform targeted searches with rg to streamline the process.
thinking
**Inspecting macro definitions**

I need to ensure that the macros in the standalone documents are correctly defined. First, I should create a list by searching for lines containing `\newcommand`, `\def`, `\DeclareMathOperator`, and others. It seems like there might be a requirement for custom macro definitions only through providecommand, but perhaps using `\newtheorem` is acceptable. I want to inspect these carefully to clarify what's applicable and ensure everything is in order.
codex
I’ve got the overlap graph. I’m now running two adversarial passes: one on copied mathematical surfaces (shared labels/formulas), and one on standalone preambles for import-safety, because stale math and macro collisions are different failure modes at this seam.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\(newcommand|renewcommand|def|gdef|DeclareMathOperator|DeclareMathOperator\\*)' standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'SC\\"'^'"\\{ch,top\\}|Swiss|E_3-chiral|bar complex is an SC|SC-coalgebra|over a point is over P\\"'^1|B'"\\(A\\) is (an )?SC|bare \\\\Omega/z|\\\\Omega/z|kappa\\(W_N\\)|H_\\{N-1\\}|S_2 = c/12|r\\"'^Vir'"\\(z\\) = \\(c/2\\)/z\\"'^4|r'"\\"'^Vir'"\\(z\\) = \\(c/2\\)/z\\"'^2|d'"\\"'^2='"\\\\kappa\\\\omega_g|d\\"'^2_bar=|d_fib'"\\"'^2'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/computations.tex:33:\renewcommand{\ref}[1]{%
standalone/computations.tex:138:\renewcommand{\arraystretch}{1.3}
standalone/computations.tex:467:\renewcommand{\arraystretch}{1.3}
standalone/computations.tex:697:\renewcommand{\arraystretch}{1.3}
standalone/computations.tex:803:\renewcommand{\arraystretch}{1.15}
standalone/classification.tex:38:\renewcommand{\ref}[1]{%
standalone/classification.tex:78:\renewcommand{\arraystretch}{1.4}
standalone/classification.tex:300:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:410:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:468:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:551:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:583:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:629:\renewcommand{\arraystretch}{1.35}
standalone/classification.tex:674:\renewcommand{\arraystretch}{1.35}
standalone/classification_trichotomy.tex:33:\newcommand{\cA}{\mathcal{A}}
standalone/classification_trichotomy.tex:34:\newcommand{\cM}{\mathcal{M}}
standalone/classification_trichotomy.tex:35:\newcommand{\barB}{\bar{B}}
standalone/classification_trichotomy.tex:36:\newcommand{\fg}{\mathfrak{g}}
standalone/classification_trichotomy.tex:37:\newcommand{\Walg}{\mathcal{W}}
standalone/classification_trichotomy.tex:38:\newcommand{\Vir}{\mathrm{Vir}}
exec
/bin/zsh -lc "rg -n '\\\\ClaimStatus|\\\\begin\\{(theorem|proposition|lemma|conjecture|remark|corollary)\\}|SC\\"'^'"\\{ch,top\\}|Swiss|E_3-chiral|B\\(A\\) is (an )?SC|\\\\Omega/z|kappa\\(W_N\\)|H_\\{N-1\\}|S_2 = c/12|d\\"'^2='"\\\\kappa\\\\omega_g|d_fib\\"'^2'"' chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/classification.tex:858:A stronger condition does. Swiss-cheese formality asks that the
standalone/classification.tex:871:Then $\cA$ is Swiss-cheese formal if and only if $\cA$ belongs
standalone/programme_summary_section1.tex:525:\mathrm{av}(k\,\Omega/z)
standalone/chiral_chern_weil.tex:146:$r(z) = k\,\Omega/z$ is valued in $\fg \otimes \fg$, and
standalone/chiral_chern_weil.tex:762:The $r$-matrix is $r(z) = k\,\Omega/z$.
standalone/chiral_chern_weil.tex:840:The $r$-matrix is $r(z) = k\,\Omega/z$ with $\Omega = \sum_{a=1}^8
standalone/chiral_chern_weil.tex:1039:$H_{N-1} \neq H_N - 1$. At $N = 2$: $H_1 = 1$ but
standalone/chiral_chern_weil.tex:1041:integer~$1$ from the $N$-th harmonic number), not $H_{N-1}$
standalone/chiral_chern_weil.tex:1049:$r(z) = k\,\Omega/z$ (trace-form convention). The averaging
standalone/chiral_chern_weil.tex:1199:$V_k(\fg)$ & $k\,\Omega/z$ &
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary_sections5_8.tex:211:\mathrm{av}(k\,\Omega/z)
standalone/programme_summary_sections5_8.tex:267:\section{The Swiss-cheese realization}
standalone/programme_summary_sections5_8.tex:278:on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
standalone/programme_summary_sections5_8.tex:290:This product is the operadic fingerprint of the Swiss-cheese
standalone/programme_summary_sections5_8.tex:322:The directionality of the Swiss-cheese operad is strict:
standalone/programme_summary_sections5_8.tex:378:The cohomology of a Swiss-cheese algebra carries a Poisson
standalone/programme_summary_sections5_8.tex:382:the full quantum Swiss-cheese structure.
standalone/programme_summary_sections5_8.tex:403:resolution of the Swiss-cheese operad. It is proved by Weiss
standalone/programme_summary_sections5_8.tex:409:classical Swiss-cheese operad (Livernet). This removes all
 succeeded in 52ms:
Total output lines: 8319

chapters/connections/dg_shifted_factorization_bridge.tex:39:\begin{remark}[Yangian as the ordered boundary face]
chapters/connections/dg_shifted_factorization_bridge.tex:134:\begin{theorem}[Derived additive KZ connection]
chapters/connections/dg_shifted_factorization_bridge.tex:135:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:192:\begin{corollary}[Derived Drinfeld--Kohno shadow]
chapters/connections/dg_shifted_factorization_bridge.tex:193:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:200:\begin{theorem}[Boundary residue theorem]
chapters/connections/dg_shifted_factorization_bridge.tex:201:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:242:\begin{theorem}[Transfer of flat spectral connections]
chapters/connections/dg_shifted_factorization_bridge.tex:243:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:309:\begin{theorem}[Quasi-factorization theorem]
chapters/connections/dg_shifted_factorization_bridge.tex:310:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:368:\begin{theorem}[Strictification by spectral cohomology]
chapters/connections/dg_shifted_factorization_bridge.tex:369:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:415:\begin{proposition}[Quadratic hexagon obstruction]
chapters/connections/dg_shifted_factorization_bridge.tex:416:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:444:\begin{proposition}[Three-particle obstruction identity]
chapters/connections/dg_shifted_factorization_bridge.tex:445:\ClaimStatusProvedHere
chapters/connections/dg_shifted_factorization_bridge.tex:480:\begin{theorem}[Abelian strictification theorem]



thinking
**Searching for formula drift**

I think this might be about kappa formula drift. I need to search for known incorrect variants in standalone formulas. I'll look specifically for H_{N-1} and see if they only appear in contexts like chiral_chern_weil or survey_modular_v2, which should mention the correct formula instead of the wrong one. This should help clarify the situation! I just want to make sure I find the accurate information.
thinking
**Evaluating reporting format**

I’m considering how to report on macro issues. Should I use `\newcommand` for each file? That seems like a lot. Maybe grouping would work, but the format needs each finding to specify file and line. I could provide multiple low severity findings for representative issues, but I want to cover every inconsistency. Maybe I can aggregate similar issues by file or line start, focusing on the first instance to keep it clear. Exact fixes with specific line ranges might work too!
thinking
**Exploring macro replacements and mismatches**

I could suggest replacing `\newcommand` with `\providecommand` in lines 34–68, focusing on specific commands rather than general fixes. Listing representative commands would be helpful, like changing `\newcommand{\cA}{\mathcal A}` to `\providecommand{\cA}{\mathcal A}`. It might still lead to one finding per preamble block. However, I should prioritize identifying mathematical mismatches. I want to compare direct basenames and inspect potential stale claim files. Using `diff` or a side-by-side comparison could help locate any mismatches effectively!
codex
I’ve got one broad seam failure already: many standalone preambles are not import-safe because they use `\newcommand` instead of guarded definitions. I’m keeping that separate and now reading the direct chapter-paper pairs to find higher-severity mathematical drift rather than stopping at the easy preamble defects.
exec
/bin/zsh -lc "sed -n '130,420p' standalone/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/w3_holographic_datum.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '160,420p' standalone/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The collision residue $r(z)$ lives on the ordered bar complex
$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$ with
deconcatenation coproduct; it is an element of the $E_1$ convolution
algebra $\mathfrak{g}^{E_1}_\cA$. The four-channel decomposition of
$r(z)$ in Section~\ref{sec:r-matrix} is an ordered-bar datum; the
modular characteristic $\kappa = \mathrm{av}(r(z))$ is its
$\Sigma_2$-coinvariant projection.

% ================================================================
\section{\texorpdfstring{$\kappa(\Walg_3) = 5c/6$}{kappa(W3) = 5c/6}
and channel decomposition}\label{sec:kappa}
% ================================================================

\begin{theorem}[Modular characteristic]\label{thm:kappa}
For $\Walg_3$ at generic central charge $c \neq 0$,
\begin{equation}\label{eq:kappa}
\kappa(\Walg_3) = \frac{5c}{6}.
\end{equation}
Equivalently, $\kappa(\Walg_3) = c \cdot (H_3 - 1)$ where
 succeeded in 51ms:
% =====================================================================
% Phase 1 of the platonic restructuring: elevation of the W_3 holographic
% modular Koszul datum from compute layer to flagship Vol I example.
%
% Source: compute/lib/theorem_w3_holographic_datum_engine.py (83 tests).
% Multi-path verification: 5+ independent paths per numerical claim.
% =====================================================================

\chapter{The first rank-2 holographic datum: \texorpdfstring{$H(\Walg_3)$}{H(W3)}}
\label{ch:w3-holographic-datum}

The platonic programme requires a working example of a holographic
modular Koszul datum at rank exceeding one. Heisenberg supplies the
rank-1 Gaussian archetype, the affine $\widehat{\mathfrak{sl}}_2$
supplies a rank-1 Lie/tree archetype, and Virasoro supplies the
rank-1 mixed (class~M) prototype, but each is single-generator
or scalar. The first algebra in the standard landscape that
exhibits genuine multi-channel structure is $\Walg_3$. Its
holographic modular Koszul datum
$H(\Walg_3) = (\cA, \cA^!, \mathcal{C}, r(z), \Theta_\cA,
 succeeded in 51ms:
Section~\ref{sec:compute} describes the computational verification.


%%% ================================================================
%%% 2. THE ELLIPTIC COLLISION RESIDUE
%%% ================================================================

\section{The elliptic collision residue}\label{sec:propagator}

\subsection{The genus-$1$ bar propagator}

At genus~$0$ the bar propagator is $\eta_{12} = d\log(z_1 - z_2)$: a
meromorphic one-form on $\mathbb{P}^1$ with a simple pole along the
diagonal. On the elliptic curve $E_\tau$, Liouville's theorem forbids
a meromorphic function with a single simple pole that is doubly
periodic. The propagator must be replaced by a quasi-periodic object.

\begin{definition}[Genus-$1$ bar propagator]\label{def:bar-propagator}
The \emph{genus-$1$ bar propagator} on $E_\tau$ is the logarithmic
derivative of the prime form:
 succeeded in 51ms:
\chapter{The genus-$1$ seven faces: elliptic collision residues}
\label{ch:genus1-seven-faces}

\begin{abstract}
At genus~$0$, the collision residue $r_\cA(z)$ has one face: the
bar-cobar twisting morphism on $\mathbb{P}^1$. Rational functions on
$\mathbb{P}^1$ are determined by their poles; the seven faces of
Theorem~\ref{thm:hdm-seven-way-master} are seven names for the same
Laurent data. At genus~$1$, this degeneracy breaks. The elliptic
curve $E_\tau$ carries a period matrix $\tau$, quasi-periodic
functions, and modular forms; these three structures force the single
genus-$0$ collision residue to split into seven genuinely distinct
objects. The splitting is not a choice: it is the geometric content
of replacing $\mathbb{P}^1$ by $E_\tau$.

For affine Kac--Moody algebras $\cA = \widehat\fg_k$, the seven
genus-$1$ faces are: the elliptic twisting morphism (F1), the
DNP25 elliptic line-operator $r$-matrix (F2), the elliptic
$\lambda$-bracket (F3), the
Knizhnik--Zamolodchikov--Bernard connection (F4), the
exec
/bin/zsh -lc "rg -n -C 2 'bar complex.*Swiss|Swiss-cheese.*bar complex|bar complex.*SC|SC.*bar complex|Swiss-cheese-formal bar|bar complexes; algebras|bar complex is.*coalgebra|bar complex.*coalgebra' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/chiral_chern_weil.tex-381-\end{warning}
standalone/chiral_chern_weil.tex-382-
standalone/chiral_chern_weil.tex:383:On a curve~$X$, the bar complex is a factorization coalgebra
standalone/chiral_chern_weil.tex-384-on the Ran space $\Ran(X) = \bigsqcup_{n \ge 1}\Conf_n(X)$.
standalone/chiral_chern_weil.tex-385-The bar differential uses the logarithmic propagator
--
standalone/programme_summary.tex-1430-collision residue has at most a simple pole (classes~$\mathbf{G}$
standalone/programme_summary.tex-1431-and~$\mathbf{L}$) have finite shadow depth and
standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary.tex-1433-poles (class~$\mathbf{M}$) have infinite shadow towers and
standalone/programme_summary.tex-1434-genuinely non-formal $A_\infty$-structure.
--
standalone/programme_summary.tex-1810-\begin{enumerate}[(a)]
standalone/programme_summary.tex-1811-\item \emph{Gauge theories} (classes~$\mathbf{G}$,
standalone/programme_summary.tex:1812: $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
standalone/programme_summary.tex-1813- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
standalone/programme_summary.tex-1814- The collision residue has at most a simple pole.
--
standalone/programme_summary_sections5_8.tex-132-collision residue has at most a simple pole (classes~$\mathbf{G}$
standalone/programme_summary_sections5_8.tex-133-and~$\mathbf{L}$) have finite shadow depth and

thinking
**Inspecting code lines**

I find this interesting! I need to take a closer look at lines 659 and so on. It seems there might be something not stale with the bar complex E1, which could lead to a Swiss-cheese effect emerging at the derived center. I want to carefully inspect those lines to understand what's happening around there. Let's see if I can uncover something important or if my assumptions need adjustment!
exec
/bin/zsh -lc "sed -n '652,676p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '990,1003p' standalone/survey_track_b_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3654,3666p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 'SC\\"'^'"\\{ch,top\\}|derived center|bar complex remains|not the bulk|not the bulk object itself|SC.*pair|bar complex.*E_1' chapters/theory/en_koszul_duality.tex chapters/connections/concordance.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
algebra $A_b = \End_\cC(b)$ only up to Morita equivalence. The
governing operad is $\SCchtop$; it is homotopy-Koszul (proved
via Kontsevich formality), so the bar-cobar adjunction on
$\SCchtop$-algebras is a Quillen equivalence.

The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
its differential encodes the closed colour, and its coproduct
the open colour. Three objects must never be conflated:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the \emph{bar complex} $\barB(A_b)$ classifies twisting
morphisms, universal couplings between $A_b$ and $A_b^!$;
\item the \emph{chiral derived centre}
$\cZ^{\der}_{\ch}(\cC) =
R\Hom_{\Fun(\cC,\cC)}(\Id, \Id)$ is the universal bulk,
 succeeded in 51ms:
constants are matrix-valued and obey ordered identities (CYBE,
pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
categories are obtained from braided ones by the
$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
exactly the categorical analogue of the averaging
map~\eqref{eq:intro-averaging}.

\textsc{Operadic primacy of Swiss-cheese.} The bar complex
$B(\cA)$ is an $E_1$ chiral coassociative coalgebra over
$(\mathrm{ChirAss})^!$; the two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ organizes the
open/closed derived center pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not the bar
complex itself
(Theorem~\ref{thm:thqg-swiss-cheese}). The operad takes $\Eone$-data as its
input colour: the open colour is associative, the closed colour
appears only as a retract. The closed sector of any
Swiss-cheese algebra is recovered from the open sector by passing
to $\Sigma_n$-coinvariants along the open-to-closed boundary
operator. The closed sector is intrinsically a quotient of the
 succeeded in 51ms:
governing operad is $\SCchtop$; it is homotopy-Koszul (proved
via Kontsevich formality), so the bar-cobar adjunction on
$\SCchtop$-algebras is a Quillen equivalence.

The bar complex of Volume~I is the coalgebraic shadow of $\cC$:
its differential encodes the closed colour, and its coproduct
the open colour. Three objects must never be conflated:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the \emph{bar complex} $\barB(A_b)$ classifies twisting
morphisms, universal couplings between $A_b$ and $A_b^!$;
\item the \emph{chiral derived centre}
$\cZ^{\der}_{\ch}(\cC) =
R\Hom_{\Fun(\cC,\cC)}(\Id, \Id)$ is the universal bulk,
 succeeded in 51ms:
\chapter{\texorpdfstring{$\En$ Koszul duality and higher-dimensional bar complexes}{En Koszul duality and higher-dimensional bar complexes}}
\label{ch:en-koszul-duality}

\index{En algebra@$\En$ algebra!Koszul duality|textbf}
\index{bar complex!higher-dimensional|textbf}

For $\En$ algebras, the bar-cobar adjunction replaces the logarithmic
propagator $d\log(z-w)$ with a closed $(n{-}1)$-form, the Arnold
relations with the Totaro relations, and chiral Koszul duality with
$\En$ Koszul duality. The underlying construction is the same:
duality is mediated by a convolution algebra on a compactified
configuration space. The passage from $n = 1$
(associative/$A_\infty$) through $n = 2$ (the holomorphic refinement
recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
Vassiliev invariants) and beyond exhibits bar-cobar duality as a
single construction parametrised by manifold dimension, with the
formality phenomena of Kontsevich and Tamarkin as shadows of the
Koszul property in each dimension.

The chapter culminates in the chiral center theorem
 succeeded in 51ms:
chapters/theory/introduction.tex-422-which packages boundary data (twisting morphisms
chapters/theory/introduction.tex-423-between~$\cA$ and~$\cA^!$) and bulk data
chapters/theory/introduction.tex:424:(the chiral derived center
chapters/theory/introduction.tex-425-$\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)$).
chapters/theory/introduction.tex-426-The five theorems characterize the closed projection
--
chapters/theory/introduction.tex-663-\item \emph{Theorem~H} (Chiral Hochschild cohomology,
chapters/theory/introduction.tex-664- Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/theory/introduction.tex:665: The deficiency is coefficient blow-up: the bulk derived center could
chapters/theory/introduction.tex-666- a priori live in arbitrarily high degrees. Theorem~H says that on the
chapters/theory/introduction.tex-667- Koszul locus it does not. One has
--
chapters/theory/introduction.tex-1464-\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
chapters/theory/introduction.tex-1465-operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
chapters/theory/introduction.tex:1466:open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
chapters/theory/introduction.tex-1467-(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself
chapters/theory/introduction.tex-1468-is a single-coloured $\Eone$-chiral coassociative coalgebra
chapters/theory/introduction.tex-1469-over $(\mathrm{ChirAss})^!$. The SC structure emerges on the
chapters/theory/introduction.tex:1470:derived center, not on the bar complex. The closed sector of any
chapters/theory/introduction.tex-1471-Swiss-cheese algebra is recovered from the open sector by passing
exec
/bin/zsh -lc "rg -n -C 2 'homotopy-Koszul|Quillen equivalence|SCchtop-algebras|bar-cobar adjunction on .*SC|classical Swiss-cheese operad.*Koszul|SC\\"'^!|self-dual'"' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex-2044-$S_{\mathrm{EE}} = \tfrac{c}{3}\log(L/\varepsilon)$, recovered as the genus-$1$ shadow of~$\Theta_\cA$ on the replica orbifold (Theorem~\ref{thm:ent-scalar-entropy}; Chapter~\ref{chap:entanglement-modular-koszul}).
chapters/theory/introduction.tex-2045-
chapters/theory/introduction.tex:2046:Complementarity sharpens this for Virasoro: the sum $S_{\mathrm{EE}}(\mathrm{Vir}_c) + S_{\mathrm{EE}}(\mathrm{Vir}_{26-c}) = \tfrac{26}{3}\log(L/\varepsilon)$ is a shadow of Theorem~C via the central-charge complementarity $c + c' = 26$ (Theorem~\ref{thm:central-charge-complementarity}), saturated at the self-dual point $c = 13$ where $\kappa + \kappa' = 13$.
chapters/theory/introduction.tex-2047-
chapters/theory/introduction.tex-2048-Beyond the scalar level, the four shadow-depth classes G/L/C/M produce distinct entanglement complexity: class~G (Heisenberg) has Gaussian entanglement with no subleading corrections; class~L (Kac--Moody) acquires a single logarithmic correction from the cubic shadow; class~C ($\beta\gamma$) adds a quartic contact channel; class~M (Virasoro, $\mathcal{W}_N$) produces an infinite tower of R\'enyi corrections controlled by the shadow growth rate~$\rho(\cA)$. The full Knill--Laflamme condition for the holographic code requires the physical inner product and is conjectured at higher genus; at genus~$1$ it is automatic.
--
chapters/theory/introduction.tex-2280- Five theorems; three pillars; three rings; Koszulness programme; open frontiers \\
chapters/theory/introduction.tex-2281-Volume~II &
chapters/theory/introduction.tex:2282: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/introduction.tex-2283-\end{longtable}
chapters/theory/introduction.tex-2284-}
--
chapters/theory/introduction.tex-2505- $\Eone$-chiral bar on $\FM_k(\C) \times \operatorname{Conf}_k(\R)$;
chapters/theory/introduction.tex-2506- $\SCchtop$ on the derived center pair; curved at
chapters/theory/introduction.tex:2507: $g \geq 1$; homotopy-Koszulity of
chapters/theory/introduction.tex-2508- $\mathrm{SC}^{\mathrm{ch,top}}$; the bulk/boundary/line triangle
chapters/theory/introduction.tex-2509- that propagates $\Theta_\cA$ to Volume~II and Volume~III.
--
chapters/theory/introduction.tex-2688-bracket in all convolution computations
chapters/theory/introduction.tex-2689-(Appendix~\ref{app:signs}, Pitfall~9).
exec
/bin/zsh -lc "rg -n -C 2 'E_3-chiral|E3-chiral|topologization|proved for all|for all chiral algebras|Sugawara|SC\\"'^'"\\{ch,top\\} \\+ inner conformal vector|E_3-TOPOLOGICAL|E_3 with conformal vector|without conformal vector' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex-246-
standalone/programme_summary_sections5_8.tex-247-\noindent
standalone/programme_summary_sections5_8.tex:248:The Sugawara construction generates a Virasoro field
standalone/programme_summary_sections5_8.tex-249-$T(z)$ from the affine currents $J^a(z)$. The OPE
standalone/programme_summary_sections5_8.tex-250-$T(z)\,T(w)$ has a quartic pole; DS reduction extends
--
standalone/programme_summary_sections5_8.tex-531-transports affine Kac--Moody (class~$\mathbf{L}$, gauge) to
standalone/programme_summary_sections5_8.tex-532-$\mathcal{W}$-algebras (class~$\mathbf{M}$, gravity) by
standalone/programme_summary_sections5_8.tex:533:raising the pole order through the Sugawara construction.
standalone/programme_summary_sections5_8.tex:534:The physical content: the Sugawara stress tensor converts
standalone/programme_summary_sections5_8.tex-535-gauge currents into a metric, and the bar complex detects
standalone/programme_summary_sections5_8.tex-536-this conversion as the appearance of higher collision poles.
--
standalone/classification_trichotomy.tex-101-for abelian and Virasoro-type families
standalone/classification_trichotomy.tex-102-$\kappa = \mathrm{av}(r(z))$, while non-abelian affine Kac--Moody
standalone/classification_trichotomy.tex:103:adds the Sugawara shift $\dim(\fg)/2$.
standalone/classification_trichotomy.tex-104-This scalar projection,
standalone/classification_trichotomy.tex-105-and the shadow depth $r_{\max}$ is computed from the
--
standalone/bp_self_duality.tex-169-of the Levi subalgebra. For the minimal nilpotent of $\fsl_3$:
exec
/bin/zsh -lc "rg -n -C 2 'differential encodes the closed colour|coproduct the open colour|closed colour|open colour' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex-312-
standalone/programme_summary_sections5_8.tex-313-\noindent
standalone/programme_summary_sections5_8.tex:314:The closed colour is the holomorphic factorization of
standalone/programme_summary_sections5_8.tex-315-Section~\ref{sec:bar}: the bar differential extracts OPE
standalone/programme_summary_sections5_8.tex-316-residues, produces $d^2 = 0$ at genus~$0$, and acquires
standalone/programme_summary_sections5_8.tex-317-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
standalone/programme_summary_sections5_8.tex:318:open colour is the topological factorization: the
standalone/programme_summary_sections5_8.tex-319-deconcatenation coproduct splits an ordered sequence at every
standalone/programme_summary_sections5_8.tex-320-consecutive position, producing the cofree tensor coalgebra.
--
standalone/programme_summary.tex-1612-
standalone/programme_summary.tex-1613-\noindent
standalone/programme_summary.tex:1614:The closed colour is the holomorphic factorization of
standalone/programme_summary.tex-1615-Section~\ref{sec:bar}: the bar differential extracts OPE
standalone/programme_summary.tex-1616-residues, produces $d^2 = 0$ at genus~$0$, and acquires
standalone/programme_summary.tex-1617-curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
standalone/programme_summary.tex:1618:open colour is the topological factorization: the
standalone/programme_summary.tex-1619-deconcatenation coproduct splits an ordered sequence at every
standalone/programme_summary.tex-1620-consecutive position, producing the cofree tensor coalgebra.
--
exec
/bin/zsh -lc "sed -n '308,322p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1608,1624p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7750,7761p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1458,1473p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1247,1287p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Deconcatenation ($n+1$ terms) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The closed colour is the holomorphic factorization of
Section~\ref{sec:bar}: the bar differential extracts OPE
residues, produces $d^2 = 0$ at genus~$0$, and acquires
curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
open colour is the topological factorization: the
deconcatenation coproduct splits an ordered sequence at every
consecutive position, producing the cofree tensor coalgebra.

The directionality of the Swiss-cheese operad is strict:
 succeeded in 51ms:
the arithmetic packet connection.
Section~9 proved one-channel line concentration on the
simple-Lie-symmetry locus, the scalar package on the proved scalar
lane, and assembled the Koszulness programme.
Sections~10--11 transported the machine to three dimensions:
the bar differential became holomorphic factorization on the closed
colour, the deconcatenation coproduct became topological factorization
on the open colour, and the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
$\SCchtop$-algebra structure whose PVA shadow governs the deformation
quantization of Poisson vertex algebras to vertex algebras.
Section~12 packaged the entire holographic correspondence into a
 succeeded in 51ms:
 Deconcatenation ($n+1$ terms) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The closed colour is the holomorphic factorization of
Section~\ref{sec:bar}: the bar differential extracts OPE
residues, produces $d^2 = 0$ at genus~$0$, and acquires
curvature $\kappa(\cA) \cdot \omega_g$ at higher genus. The
open colour is the topological factorization: the
deconcatenation coproduct splits an ordered sequence at every
consecutive position, producing the cofree tensor coalgebra.

The directionality of the Swiss-cheese operad is strict:
\emph{no open inputs produce closed outputs}. Bulk operators
restrict to boundary operators, but not conversely. The open
 succeeded in 52ms:
pentagon, hexagon, mixed Yang--Baxter). Symmetric monoidal
categories are obtained from braided ones by the
$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
exactly the categorical analogue of the averaging
map~\eqref{eq:intro-averaging}.

\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself
is a single-coloured $\Eone$-chiral coassociative coalgebra
over $(\mathrm{ChirAss})^!$. The SC structure emerges on the
derived center, not on the bar complex. The closed sector of any
Swiss-cheese algebra is recovered from the open sector by passing
to $\Sigma_n$-coinvariants along the open-to-closed boundary
operator. The closed sector is intrinsically a quotient of the
 succeeded in 51ms:
\begin{principle}[The bar complex is $\Eone$-chiral coassociative;
$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
\label{princ:sc-two-incarnations}
\index{Swiss-cheese operad!on derived center, NOT on bar}
\index{bar complex!is E1 coassociative, NOT SC}
The ordered bar complex
$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$
is an $\Eone$-chiral coassociative coalgebra: a coalgebra
over the Koszul dual cooperad
$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
It has a differential (from OPE collision residues) and a
coassociative deconcatenation coproduct. These are the two
structures of a dg coalgebra. The bar complex does \emph{not}
carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.

The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
the \emph{derived chiral center}
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
= C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$,
computed \emph{using} the bar complex as a resolution.

thinking
**Exploring contradictions in findings**

I see there's a clear contradiction regarding the survey_modular_koszul_duality text at line 7755; it could be a stale summary. It might be worth reporting as a separate finding. There’s also a possibility that the pair order is reversed at lines 2365 or 1318, but that's not necessarily a problem. I need to look for more high-severity issues. Searching for SC self-duality could help clarify any inconsistencies, particularly since some chapters still refer to these concepts.
exec
/bin/zsh -lc "rg -n -C 2 'SC["'^a-zA-Z]|Swiss-cheese.*self-dual|self-dual.*Swiss-cheese|Koszul self-dual|SC'"\\"'^!'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 720

standalone/classification.tex-722-no intermediate values: the classification is forced by the
standalone/classification.tex-723-arithmetic of a single quadratic polynomial.
standalone/classification.tex:724:The SC-formality characterisation
standalone/classification.tex-725-(Proposition~\ref{prop:sc-formality-standalone}) shows that
standalone/classification.tex-726-class~$\mathbf{G}$ is distinguished by a sharp operadic property.
--
standalone/classification.tex-846-
standalone/classification.tex-847-
standalone/classification.tex:848:\subsection{SC-formality characterises class G}
standalone/classification.tex-849-\label{ssec:sc-formality}
standalone/classification.tex-850-
--
standalone/classification.tex-857-
standalone/classification.tex-858-A stronger condition does. Swiss-cheese formality asks that the
standalone/classification.tex:859:higher SC-operations on $\cA$ \emph{itself} vanish:
standalone/classification.tex:860:$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$. This is a
standalone/classification.tex-861-condition on the algebra, not on its bar cohomology; the common
standalone/classification.tex-862-notation $m_k$ for both is a source of systematic confusion.

thinking
**Inspecting contradictions and issues**

I'm noticing that some standalones have been corrected while others haven't. I think we should focus on the contradictions that arise. There's another issue around `survey_modular_koszul_duality.tex:6193-6194` where it states that "The bar complex carrying both structures is an SC-algebra," which appears to be directly forbidden. I need to compare it with the corrected chapter and inspect the details around lines 6188-6195 to clarify what's going on.
exec
/bin/zsh -lc "sed -n '6188,6196p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
factors at a point of the second factor: an element
$a_1\otimes\cdots\otimes a_k$ with ordering
$t_1<\cdots<t_k$ on $\mathbb R$ is decomposed at a cut point
$t_p<c<t_{p+1}$ into
$(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
The bar complex carrying both structures is an
$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.

\subsection*{10.2.\enspace Homotopy-Koszulity of $\mathsf{SC}^{\mathrm{ch,top}}$}

thinking
**Checking for inconsistencies**

I need to see if the chapters in question have been corrected. The lines around 1247+ in "en_koszul_duality" should be checked closely. Also, it appears that the `programme_summary_sections5_8` file might already have some corrections, but line 314 misstates some colors, which shows inconsistency. I could also look for contradictions in "survey_modular_koszul_duality.tex." It might be important to search for more specific phrases like `B(A)` SC, `SC-algebra`, or `SC coalgebra` to clarify any issues.
exec
/bin/zsh -lc "rg -n -C 1 'SC\\}-algebra|SC\\)-algebra|SC-algebra|SC-coalgebra|Swiss-cheese.*pair|The bar complex carrying both structures|bar complex.*SC|B\\(\\cA\\).*SC|\\"'$B'"\\(\\cA\\)\\"'$.*SC'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:SC\}-algebra|SC\)-algebra|SC-algebra|SC-coalgebra|Swiss-cheese.*pair|The bar complex carrying both structures|bar complex.*SC|B\(\cA\).*SC|\$B\(\cA\)\$.*SC)
                                                                                                                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -C 1 'SC-algebra|SC-coalgebra|The bar complex carrying both structures|bar complex.*Swiss-cheese|bar complex.*SC|Swiss-cheese.*pair' standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/survey_track_b_compressed.tex-1488-shadow connection. Every ingredient constructed so far (the
standalone/survey_track_b_compressed.tex:1489:bar complex, the shadow tower, the Swiss-cheese structure, the
standalone/survey_track_b_compressed.tex-1490-PVA descent, the genus expansion) is a projection of this
--
standalone/N3_e1_primacy.tex-945-Promotion from a single-colour $E_{1}$-chiral algebra to the
standalone/N3_e1_primacy.tex:946:Swiss-cheese setting takes $\cA$ to the pair $(\cA, \cA)$ with
standalone/N3_e1_primacy.tex-947-closed sector $B_{\Com}(\cA)$ and open sector $B_{\Ass}(\cA)$
--
standalone/survey_modular_koszul_duality_v2.tex-4151-shadow connection. Every ingredient constructed so far (the
standalone/survey_modular_koszul_duality_v2.tex:4152:bar complex, the shadow tower, the Swiss-cheese structure, the
standalone/survey_modular_koszul_duality_v2.tex-4153-PVA descent, the genus expansion) is a projection of this
--
standalone/introduction_full_survey.tex-1986- $(C^{\bullet}_{\mathrm{ch}}(\cA, \cA),\, \cA)$ is the
standalone/introduction_full_survey.tex:1987: terminal local chiral Swiss-cheese pair over~$\cA$
standalone/introduction_full_survey.tex-1988- \textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}},
--
standalone/survey_modular_koszul_duality.tex-6192-$(a_1\otimes\cdots\otimes a_p)\otimes(a_{p+1}\otimes\cdots\otimes a_k)$.
standalone/survey_modular_koszul_duality.tex:6193:The bar complex carrying both structures is an
standalone/survey_modular_koszul_duality.tex-6194-$\mathsf{SC}^{\mathrm{ch,top}}$-algebra.
--

thinking
**Inspecting code lines**

I’m noticing that lines 946-947 in the N3_e1_primacy could be outdated if the promotion pair utilizes B_Com(A) and B_Ass(A). I think it's necessary to check that, since it might explain why AGENTS indicates a one-color input promotion A→(A,A) and SC structure isn't evident on the bar. So, I’ll focus on inspecting lines 940-949 to get clearer insights on potential issues.
exec
/bin/zsh -lc "sed -n '940,951p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection*{The Swiss-cheese and curved sectors}

The Swiss-cheese operad $\mathrm{SC}^{\mathrm{ch,top}}$, in its
two-coloured open-closed form, is the natural habitat of the
averaging map when one works with both sectors simultaneously.
Promotion from a single-colour $E_{1}$-chiral algebra to the
Swiss-cheese setting takes $\cA$ to the pair $(\cA, \cA)$ with
closed sector $B_{\Com}(\cA)$ and open sector $B_{\Ass}(\cA)$
plus a mixed sector of dimension $(k-1)!\binom{k+m}{m}$ at
Swiss-cheese degree $(k,m)$. The averaging map restricted to the
open sector is the subject of the present paper; the analogous
statement in the mixed sector, which governs brane boundaries
exec
/bin/zsh -lc "rg -n -C 2 'Promotion from a single-colour|pair \\(\\\\cA, \\\\cA\\)|closed sector .*open sector|B_\\{\\\\Com\\}|B_\\{\\\\Ass\\}|mixed sector of dimension \\(k-1\\)"'!'"' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex-2879-  braces): the pair
chapters/theory/en_koszul_duality.tex-2880-  $(Z_{\mathsf{SC}}(\cA), \cA)_{\leq 2}$ forgets the entire
chapters/theory/en_koszul_duality.tex:2881:  shadow tower. The closed sector acts on the open sector
chapters/theory/en_koszul_duality.tex-2882-  only through the cup product and identity.
chapters/theory/en_koszul_duality.tex-2883-  This is the maximally deficient case.

thinking
**Searching for formulas**

I'm thinking I should look for the exact dimension formula, perhaps in specific chapters or sections. I need to ensure I'm getting the right context and details. It's important to check reliable sources or textbooks that detail these formulas so I can provide accurate information. I wonder if there’s a particular chapter that focuses on this, or if it’s spread across multiple sections. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n -C 2 '\\(k-1\\)"'!.*binom'"\\{k\\+m\\}\\{m\\}|mixed sector|closed sector .*open sector' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex-1628-The open sector is $\operatorname{Ass}^{!,c} =
chapters/theory/en_koszul_duality.tex-1629-\operatorname{Ass}^c$ with $\dim = m!$ (self-duality).
chapters/theory/en_koszul_duality.tex:1630:The mixed sector is computed by the K\"unneth
chapters/theory/en_koszul_duality.tex-1631-factorization: $\operatorname{Lie}^c(k)$ contributes
chapters/theory/en_koszul_duality.tex-1632-$(k{-}1)!$, and the $(k,m)$-shuffle count
--
chapters/theory/en_koszul_duality.tex-1659-controls the open direction
chapters/theory/en_koszul_duality.tex-1660-($r$-matrix, KZ associator, Yangian deformation).
chapters/theory/en_koszul_duality.tex:1661:The two factors commute. The mixed sector
chapters/theory/en_koszul_duality.tex-1662-\textup{(}Proposition~\textup{\ref{prop:sc-koszul-dual-three-sectors}(iii)}\textup{)}
chapters/theory/en_koszul_duality.tex-1663-governs their interaction: bulk operators acting on boundary
--
chapters/theory/en_koszul_duality.tex-2879-  braces): the pair
chapters/theory/en_koszul_duality.tex-2880-  $(Z_{\mathsf{SC}}(\cA), \cA)_{\leq 2}$ forgets the entire
chapters/theory/en_koszul_duality.tex:2881:  shadow tower. The closed sector acts on the open sector
chapters/theory/en_koszul_duality.tex-2882-  only through the cup product and identity.
chapters/theory/en_koszul_duality.tex-2883-  This is the maximally deficient case.

thinking
**Inspecting relevant lines**

I need to take a closer look at the lines around 1628 since they might hold some relevant information. It's always good to double-check specific areas where important details could be hiding. I'll focus my attention there to see if anything stands out or if I can glean insights that could help clarify things. Making sure I capture all necessary details is key! Let's see what I find!
exec
/bin/zsh -lc "sed -n '1624,1635p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The closed sector is $\operatorname{Com}^{!,c} =
\operatorname{Lie}^c$ with $\dim\operatorname{Lie}(n) = (n{-}1)!$
(partition-lattice calculation,
Theorem~\ref{thm:com-lie}).
The open sector is $\operatorname{Ass}^{!,c} =
\operatorname{Ass}^c$ with $\dim = m!$ (self-duality).
The mixed sector is computed by the K\"unneth
factorization: $\operatorname{Lie}^c(k)$ contributes
$(k{-}1)!$, and the $(k,m)$-shuffle count
$\binom{k+m}{m}$ arises from interleaving $k$ closed
leaves among $m$ ordered open leaves on the
$\operatorname{FM}_k(\mathbb{C}) \times E_1(m)$

thinking
**Exploring equation differences**

I’m considering using an automated textual diff to identify differences in equations or statuses between overlapping labels. There might be too many to process at once, but it could help highlight mismatches. I think comparing key formulas, like `eq:elliptic-rmatrix`, between standalone versions and those in a chapter could be insightful. I’ll need to search within the chapter for clarity. It feels like a systematic approach to uncover discrepancies.
exec
/bin/zsh -lc "rg -n -C 2 'elliptic-rmatrix|kzb-full|g1sf-elliptic-rmatrix|w3hol-kappa-w3|deltaF2|critical-discriminant|shadow-metric|riccati-algebraicity|heisenberg-sewing' chapters/**/*.tex standalone/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1146

chapters/connections/thqg_fredholm_partition_functions.tex-58-algebra $\cH_\kappa$, the sewing envelope is the symmetric algebra
chapters/connections/thqg_fredholm_partition_functions.tex-59-of the Bergman space $A^2(D)$ of the disk
chapters/connections/thqg_fredholm_partition_functions.tex:60:(Theorem~\ref{thm:heisenberg-sewing}\,(i)), and the genus-$g$
chapters/connections/thqg_fredholm_partition_functions.tex-61-partition function is the Fredholm determinant of an explicit
chapters/connections/thqg_fredholm_partition_functions.tex-62-trace-class sewing operator on $A^2(D)$. The HS-sewing criterion
--
chapters/connections/thqg_fredholm_partition_functions.tex-76-\item The Heisenberg sewing theorem in full:
chapters/connections/thqg_fredholm_partition_functions.tex-77- four clauses with complete proofs
chapters/connections/thqg_fredholm_partition_functions.tex:78: (\S\ref{subsec:thqg-X-heisenberg-sewing}).
chapters/connections/thqg_fredholm_partition_functions.tex-79-\item One-particle reduction, trace-class estimates,
chapters/connections/thqg_fredholm_partition_functions.tex-80- and the Dedekind eta derivation
--
chapters/connections/thqg_fredholm_partition_functions.tex-243-\begin{proposition}[Heisenberg sewing envelope = $\operatorname{Sym} A^2(D)$;
chapters/connections/thqg_fredholm_partition_functions.tex-244-\ClaimStatusProvedElsewhere{} Moriwaki~\cite{Moriwaki26b}]%
chapters/connections/thqg_fredholm_partition_functions.tex:245:\label{prop:thqg-X-heisenberg-sewing-envelope}%
chapters/connections/thqg_fredholm_partition_functions.tex-246-\index{Heisenberg!sewing envelope}%
chapters/connections/thqg_fredholm_partition_functions.tex-247-\index{sewing envelope!Heisenberg}%
--

thinking
**Verifying terms and concentrations**

I’m considering if the term “MC1” is stale or only applies to certain standard families. I think I should search for the concordance or status to clarify what it represents. It might stand for PBW concentration, but I need to verify that it’s proven across the board. So, I’ll look into searching “MC1” in the concordance or editorial to get clearer information!
codex
I’ve isolated a real contradiction class now: several standalone summaries still assign Swiss-cheese colours directly to bar differential/coproduct, while the main manuscript explicitly retracts that and places `SC^{ch,top}` on the derived center pair. I’m checking for a second class of seam failures now: standalone summaries that overstate theorem status relative to concordance.
exec
/bin/zsh -lc "rg -n -C 2 'MC1|PBW concentration|proved for all standard families|all standard families|standard landscape' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/connections/editorial_constitution.tex standalone/introduction_full_survey.tex standalone/programme_summary*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 2 'Conjecture|ClaimStatusConjectured|Conditional|ClaimStatusConditional|proved' standalone/programme_summary*.tex standalone/introduction_full_survey.tex standalone/survey_track_*.tex standalone/survey_modular_koszul_duality*.tex | head -n 300" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex-110-
standalone/programme_summary_sections5_8.tex-111-The maximal pole order of the collision residue separates the
standalone/programme_summary_sections5_8.tex:112:standard landscape into two regimes:
standalone/programme_summary_sections5_8.tex-113-
standalone/programme_summary_sections5_8.tex-114-\begin{center}
--
standalone/programme_summary_sections9_14.tex-80-
standalone/programme_summary_sections9_14.tex-81-% ====================================================================
standalone/programme_summary_sections9_14.tex:82:\section{The standard landscape}
standalone/programme_summary_sections9_14.tex-83-\label{sec:landscape}
standalone/programme_summary_sections9_14.tex-84-% ====================================================================
--
standalone/programme_summary_sections9_14.tex-87-structure, and the collision residue are not abstractions
standalone/programme_summary_sections9_14.tex-88-awaiting examples: they were \emph{found} by computing
standalone/programme_summary_sections9_14.tex:89:examples. The standard landscape is the testing ground
standalone/programme_summary_sections9_14.tex-90-where the theory proves itself.
standalone/programme_summary_sections9_14.tex-91-
--
standalone/programme_summary_sections9_14.tex-101-\begin{table}[ht]
standalone/programme_summary_sections9_14.tex-102-\centering
 succeeded in 51ms:
standalone/programme_summary_sections9_14.tex-23-\newtheorem{lemma}[theorem]{Lemma}
standalone/programme_summary_sections9_14.tex-24-\newtheorem{corollary}[theorem]{Corollary}
standalone/programme_summary_sections9_14.tex:25:\newtheorem{conjecture}[theorem]{Conjecture}
standalone/programme_summary_sections9_14.tex-26-\theoremstyle{definition}
standalone/programme_summary_sections9_14.tex-27-\newtheorem{definition}[theorem]{Definition}
--
standalone/programme_summary_sections9_14.tex-279-PBW concentration, bar-intrinsic existence, categorical
standalone/programme_summary_sections9_14.tex-280-generation, inverse-limit completion, and analytic sewing.
standalone/programme_summary_sections9_14.tex:281:MC1 through MC4 are proved; MC5 is partially proved, with
standalone/programme_summary_sections9_14.tex-282-the analytic HS-sewing package established at all genera
standalone/programme_summary_sections9_14.tex-283-and the genuswise BV/BRST/bar identification conjectural.
--
standalone/programme_summary_sections9_14.tex-300-$\cW^k(\fg)$ at all levels~$k$ (Feigin--Frenkel free
standalone/programme_summary_sections9_14.tex-301-generation). The simple quotient $L_k(\fg)$ at admissible
standalone/programme_summary_sections9_14.tex:302:levels has Koszulness proved for $\fg = \mathfrak{sl}_2$
standalone/programme_summary_sections9_14.tex-303-at all admissible levels; higher rank is open.
standalone/programme_summary_sections9_14.tex-304-
--
standalone/programme_summary_sections9_14.tex-540-algebras to vertex algebras; and the non-principal
standalone/programme_summary_sections9_14.tex-541-$\cW$-algebra corridor, where hook-type nilpotent orbits

thinking
**Analyzing macro definitions**

I’m thinking through the need to systematically report files with `\newcommand` blocks. It might help to group them by file or mention all custom preamble macros in those files. The goal is to convert each `\newcommand` and `\DeclareMathOperator` into guarded forms. There are around 15 files, which seems manageable for low-severity findings. I should also search for any stale formulas and forbidden phrases from AGENTS using regular expressions. This will ensure thoroughness without overwhelming with too many lines.
exec
/bin/zsh -lc "rg -n -C 2 'B\\(A\\) is a coalgebra over SC|bar differential is the closed color|bar coproduct is the open color|SC\\"'^'"\\{ch,top\\} is Koszul self-dual|E_3-chiral|Topologization proved for all|A\\"'^! is an SC-algebra|bar-cobar produces bulk|Omega'"\\(B\\(A\\)\\) is the Koszul dual|the Koszul dual equals the bar complex|D_Ran\\(B\\(A\\)\\) is the cobar complex|the bar complex carrying both structures' standalone/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n 'S_2\\s*=\\s*c/12|H_\\{N-1\\}|kappa\\(W_N\\)\\s*=\\s*c\\*H_\\{N-1\\}|kappa\\s*=\\s*c/2 unqualified|r\\"'^Vir'"\\(z\\)\\s*=\\s*\\(c/2\\)/z\\"'^4|r'"\\"'^Vir'"\\(z\\)\\s*=\\s*\\(c/2\\)/z\\"'^2|T'"\\"'^c'"\\(s A\\)|\\|s\\"'^{-1}v'"\\|\\s*=\\s*\\|v\\|\\+1|eta\\s*=\\s*prod|F_2\\s*=\\s*1/5760|7/2880|pi_3\\(BU\\)\\s*=\\s*Z|kappa\\+kappa\\'=0|kappa\\(BP\\)\\+kappa\\(BP\\"'^!'"\\)=1/3|genus-2 stable graphs = 6|sl_2 bar H\\"'^2 = 6'"' standalone/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'S_2\\s*=\\s*c/12|kappa\\(BP\\)\\+kappa\\(BP\\"'^!'"\\)=1/3|genus-2 stable graphs = 6|sl_2 bar H\\"'^2 = 6'"' chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: unmatched '
 exited 1 in 51ms:


thinking
**Considering comparison methods**

I'm thinking about whether I could compare selective sections, but it seems like a large task. Maybe I could use `diff -u <(sed...)`, but I can't really rely on a rough diff for accuracy. I wonder if it might be better to find specific lines in a standalone introduction that match stale phrases not used in the chapter. There’s a lot to consider here in terms of clarity and effectiveness!
exec
/bin/zsh -lc "sed -n '1216,1238p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The bar differential extracts residues in~$\C$; the bar coproduct
splits ordered sequences in~$\R$. The bar complex $B(\cA)$ is an
$E_1$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$:
its differential encodes holomorphic factorization on~$\C$, its
deconcatenation coproduct encodes topological factorization
on~$\R$. The two-coloured $\mathsf{SC}^{\mathrm{ch,top}}$ structure
of Volume~II emerges on the chiral derived center pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$ itself.
The \emph{holomorphic-topological Swiss-cheese
operad} $\mathsf{SC}^{\mathrm{ch,top}}$ has
\emph{closed-colour} operations parametrised by
$\operatorname{FM}_k(\C)$ (Fulton--MacPherson
configurations of $k$~points in~$\C$),
\emph{open-colour} operations parametrised by
$\operatorname{Conf}_k^{<}(\R)$
(ordered configurations of $k$~points in~$\R$), and
mixed operations encoding the bulk-boundary
interaction. It is \emph{homotopy-Koszul}
(i.e.\ the bar-cobar resolution is a quasi-isomorphism:
Kontsevich formality + classical Swiss-cheese Koszulity +

thinking
**Evaluating access to volume II**

I'm considering whether volume II is needed if it’s not in the current working directory. The network might not be an option, but I wonder if I could read volume II locally if it's accessible. I think about whether it's writable or just readable. It looks like I'm limited to the current working directory and writable roots. So, I’m concluding that I probably don’t need to access volume II after all.
exec
/bin/zsh -lc "rg -n -C 2 'Swiss-cheese-formal bar|SC-formal bar|SC-formality.*bar|bar complex \\(\\"'$m_k'"\\"'^'"\\{SC\\}\\"'$'"' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections5_8.tex-132-collision residue has at most a simple pole (classes~$\mathbf{G}$
standalone/programme_summary_sections5_8.tex-133-and~$\mathbf{L}$) have finite shadow depth and
standalone/programme_summary_sections5_8.tex:134:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary_sections5_8.tex-135-poles (class~$\mathbf{M}$) have infinite shadow towers and
standalone/programme_summary_sections5_8.tex-136-genuinely non-formal $A_\infty$-structure.
--
standalone/programme_summary.tex-1430-collision residue has at most a simple pole (classes~$\mathbf{G}$
standalone/programme_summary.tex-1431-and~$\mathbf{L}$) have finite shadow depth and
standalone/programme_summary.tex:1432:Swiss-cheese-formal bar complexes; algebras with higher-order
standalone/programme_summary.tex-1433-poles (class~$\mathbf{M}$) have infinite shadow towers and
standalone/programme_summary.tex-1434-genuinely non-formal $A_\infty$-structure.
--
standalone/programme_summary.tex-1810-\begin{enumerate}[(a)]
standalone/programme_summary.tex-1811-\item \emph{Gauge theories} (classes~$\mathbf{G}$,
standalone/programme_summary.tex:1812: $\mathbf{L}$): finite shadow depth, Swiss-cheese-formal bar
standalone/programme_summary.tex-1813- complex ($m_k^{\mathrm{SC}} = 0$ for $k$ sufficiently large).
standalone/programme_summary.tex-1814- The collision residue has at most a simple pole.

thinking
**Comparing chapter classifications**

I think I should compare this with classification.tex or specific chapters. It would be useful to look closely at the main chapters to ensure that the SC-formality property is correctly applied. By doing this comparison, I can confirm that everything aligns with the expected standards. This should help clarify any inconsistencies or necessary adjustments! I'll dive into that now.
exec
/bin/zsh -lc "rg -n -C 2 'SC-formality|Swiss-cheese formality|m_k\\"'^'"\\{SC\\}|class~\\\\mathbf\\{G\\}|class G' chapters/**/*.tex standalone/classification.tex standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/holographic_datum_master.tex-1135-$\cA$ but failed to match the Vol.~II line-operator computation for
chapters/connections/holographic_datum_master.tex-1136-$\beta\gamma$; the discrepancy was traced to the conflation of bar
chapters/connections/holographic_datum_master.tex:1137:formality with Swiss-cheese formality. In each case, the
chapters/connections/holographic_datum_master.tex-1138-disagreement between two faces was the diagnostic signal that
chapters/connections/holographic_datum_master.tex-1139-identified the error.
--
chapters/connections/arithmetic_shadows.tex-3498-Bernoulli-Dirichlet identification: the earlier formulation
chapters/connections/arithmetic_shadows.tex-3499-%: The false Bernoulli-Dirichlet identity equated the shadow L-function
chapters/connections/arithmetic_shadows.tex:3500:% L^sh(s) = sum S_r r^{-s} (which is ENTIRE for class G/L) with the
chapters/connections/arithmetic_shadows.tex-3501-% meromorphic function -kappa*zeta(s)*zeta(s-1) (which has poles at s=1,2).
chapters/connections/arithmetic_shadows.tex-3502-% An identity between an entire function and a meromorphic function with
--
chapters/connections/thqg_fredholm_partition_functions.tex-1500-scalar lane; \ClaimStatusProvedHere]%
chapters/connections/thqg_fredholm_partition_functions.tex-1501-\label{thm:thqg-X-class-G-fredholm}%
chapters/connections/thqg_fredholm_partition_functions.tex:1502:\index{partition function!class G}%
chapters/connections/thqg_fredholm_partition_functions.tex-1503-\index{scalar saturation!Fredholm determinant}%
chapters/connections/thqg_fredholm_partition_functions.tex-1504-Let $\cA$ be a class-G Gaussian chiral algebra on the proved
--
chapters/connections/thqg_fredholm_partition_functions.tex-2106-\ClaimStatusProvedHere]%
chapters/connections/thqg_fredholm_partition_functions.tex-2107-\label{prop:thqg-X-coderived-fredholm-G}%
exec
/bin/zsh -lc "sed -n '1576,1581p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
differential encodes holomorphic factorization on~$\mathbb{C}$, the
deconcatenation coproduct encodes topological factorization
on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ emerges on the chiral derived center
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

thinking
**Evaluating color issues**

It seems there might be some confusion with colors. I can reference lines 1578 and 1614, but the user wants specific issues noted by file and line number. It looks like line 1614 contradicts the information from lines 1578-1580 and also some chapters. There might be a similar issue in sections 5-8; for instance, line 279 appears correct while line 314 seems wrong. I should also check the survey_modular_koszul_duality_v2 for further corrections in line 1514-1517 regarding the SC structure. I need to inspect those exact lines closely.
exec
/bin/zsh -lc "sed -n '1512,1518p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
packaging the holomorphic-topological QFT on
$\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
(Volume~II).
exec
/bin/zsh -lc "rg -n '\\(\\\\cA, \\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)|\\(\\\\cA, \\\\mathcal\\{Z\\}\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\)\\)' standalone/*.tex chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/introduction_full_survey.tex:1395:derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
standalone/survey_modular_koszul_duality.tex:2364:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
standalone/survey_modular_koszul_duality.tex:7758:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
standalone/survey_modular_koszul_duality_v2.tex:1515:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
standalone/survey_track_a_compressed.tex:1317:$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the

thinking
**Verifying chapter order**

I think the main chapters likely follow the order `(Z^{der}, A)`. However, there seems to be a seam mismatch I need to check. I’ll verify the chapter lines to ensure everything aligns correctly. I’m curious if I can find the exact open/closed pair order. This will help clarify any inconsistencies. Let’s explore this together and ensure I don’t miss anything important!
exec
/bin/zsh -lc "rg -n -C 1 '\\(\\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\), \\\\cA\\)|\\(C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\),\\\\ \\\\cA\\)' chapters/theory/introduction.tex chapters/theory/en_koszul_duality.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex-1465-operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
chapters/theory/introduction.tex:1466:open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
chapters/theory/introduction.tex-1467-(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself

thinking
**Identifying seams and inconsistencies**

I noticed that standalone files seem to have a reverse pair order, which is an inconsistency in the seams. I need to fix it by swapping the order everywhere to `( \cZ^{der}_{ch}(\cA), \cA )`. If any prose mentions open/closed pairs, I should clarify that closed/bulk should come first, followed by open/boundary. I think there could be about four separate findings across different files like survey_modular, v2, track_a, and introduction_full_survey. I'll also need to check for other seam mismatches.
exec
/bin/zsh -lc "rg -n '\\(\\\\cA, ?C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\)|\\(C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\), ?\\\\cA\\)|derived center pair' standalone/programme_summary*.tex standalone/introduction_full_survey.tex standalone/survey_track_*.tex standalone/survey_modular_koszul_duality*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/programme_summary_sections9_14.tex:588:derived center pair
standalone/survey_track_a_compressed.tex:1316:supplies the holomorphic factorization data; the derived center pair
standalone/introduction_full_survey.tex:663:open/closed derived center pair
standalone/introduction_full_survey.tex:1222:of Volume~II emerges on the chiral derived center pair
standalone/introduction_full_survey.tex:1395:derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
standalone/introduction_full_survey.tex:1977: emerges on the chiral derived center pair, not on $\barB_X(\cA)$
standalone/survey_modular_koszul_duality_v2.tex:1514:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality.tex:2363:supplies the holomorphic factorization data; the derived center pair
standalone/survey_modular_koszul_duality.tex:6070:structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:6071:$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$, not on the bar complex
standalone/survey_modular_koszul_duality.tex:7110: structure emerges on the derived center pair
standalone/survey_modular_koszul_duality.tex:7757:on the open colour, and the derived center pair

thinking
**Inspecting order issues**

I need to look into the files with incorrect order, specifically starting at line 1395. I think I should check more files too. There might be an issue with `programme_summary_sections9_14`, as it could be paired incorrectly. Also, `survey_track_a` seems to be out of order. I'll need to extract those specific lines to get a clearer understanding of the problem.
exec
/bin/zsh -lc "sed -n '1389,1398p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(the chiral derived center
$\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, governing operators
in the interior).
The five theorems characterize the closed projection
$\Theta_\cA = \pi_{\mathrm{cl}}(\Theta^{\mathrm{oc}}_\cA)$; the bulk
projection is controlled by the $\SCchtop$-algebra structure on the
derived center pair $(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$
(Theorem~\ref{thm:thqg-swiss-cheese}).
Modularity (the genus expansion and its
tautological descent to~$\overline{\mathcal{M}}_g$) belongs to the
exec
/bin/zsh -lc "sed -n '1314,1319p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
packaging the holomorphic-topological QFT on
$\mathbb C_z\times\mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
exec
/bin/zsh -lc "sed -n '2361,2366p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7755,7760p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
that packages the complete holomorphic-topological quantum field
theory on $\mathbb C_z \times \mathbb R_t$: the bar complex $B(\cA)$, coassociative over $(\mathrm{ChirAss})^!$,
supplies the holomorphic factorization data; the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ carries the
$\SCchtop$-algebra structure encoding both closed and open colours;
and $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ is the universal bulk
 succeeded in 52ms:
the bar differential became holomorphic factorization on the closed
colour, the deconcatenation coproduct became topological factorization
on the open colour, and the derived center pair
$(\cA, \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))$ acquired an
$\SCchtop$-algebra structure whose PVA shadow governs the deformation
quantization of Poisson vertex algebras to vertex algebras.

thinking
**Investigating classification issues**

I see that the chapter classification states SC-formality applies only to class G, which implies there are two problems: class L being incorrectly included and issues with the bar complex object. I need to find the exact fixes. Additionally, line 1432 suggests that collision residue has at most a simple pole for classes G and L, but class L has finite depth and isn't SC-formal. I'll check classification lines and chapters to confirm these mismatches. It seems like I need to focus on specific portions of the main chapters.
exec
/bin/zsh -lc "sed -n '2893,2904p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proposition}[SC-formality characterises class~$G$; \ClaimStatusProvedHere]
\label{prop:sc-formal-iff-class-g}
\index{Swiss-cheese operad!formality characterisation}
\index{class G@class~$G$!characterised by SC-formality}
Let~$\cA$ be a chiral algebra in the standard landscape.
Then~$\cA$ is Swiss-cheese formal
\textup{(}$m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$\textup{)}
if and only if~$\cA$ belongs to class~$G$.
\end{proposition}

\begin{proof}
The forward direction \textup{(}class~$G$ $\Longrightarrow$


thinking
**Assessing findings and format**

I’m contemplating the need to compare with the chapter introductions. If we have enough high and medium findings, maybe we can skip potential status drift. The user asked for an exhaustive list, so we might need more than five findings. We can mention the number of files checked and findings found. The final format should only include the findings without mentioning empty results, unless in the summary.  

I need to check for potential issues like reversed pair orders in some files.
thinking
**Evaluating potential order issues**

I’m noticing that in the introduction_full_survey, line 1395 has a reversed order, while line 663 might be derived without an explicit order. Line 663 does show the correct order with the pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)`, which contrasts with the later line. That’s a clear self-contradiction! I might cite the earlier lines and chapters as evidence.  
Also, I’ll check if survey_track_a has any other correct orders. It could help to search for the exact `C^\bullet` pair as well.
exec
/bin/zsh -lc "rg -n -C 1 '\\(C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\),\\\\ \\\\cA\\)|\\(\\\\cZ\\"'^'"\\{\\\\mathrm\\{der\\}\\}_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA\\), \\\\cA\\)' standalone/survey_track_a_compressed.tex standalone/introduction_full_survey.tex standalone/survey_modular_koszul_duality.tex standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '660,665p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$B(\cA)$ is an $E_1$ chiral coassociative coalgebra over
$(\mathrm{ChirAss})^!$; the two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ organizes the
open/closed derived center pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not the bar
complex itself

thinking
**Inspecting survey modularity**

I'm considering inspecting the survey modularity and specifically looking into the Koszul duality in the correct order elsewhere, especially focusing on lines 6070-6071. I think it’s important to double-check that part to ensure everything aligns correctly. I wonder if there’s something specific I need to note about it. It's good to take a closer look, just to be thorough!
exec
/bin/zsh -lc "sed -n '6067,6072p' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
OPE collision residues along divisors of $\operatorname{FM}_k(\mathbb C)$,
and its deconcatenation coproduct records the ordered splitting of
the topological direction. The $\mathsf{SC}^{\mathrm{ch,top}}$
structure emerges on the derived center pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA), \cA)$, not on the bar complex
itself. The bar complex classifies \emph{twisting morphisms},








thinking
**Evaluating survey structure**

I'm considering how to combine the reversed order and potentially stale elements in the survey modular version. It sounds like a good idea! Maybe the introduction full survey is corrected and has the reversed order, but I’m not sure if the color conflation is a significant issue. I wonder if I can highlight a single medium finding. It looks like survey track A has only reversed order as well.
thinking
**Identifying issues and potential fixes**

I’ve noticed a color issue with Survey_track_b and possibly an order problem. There’s also a formal bar complexity in the program summary and sections 5-8 that may relate to color confusion. I think multiple standalone summary files are overriding references, creating import problems. For the macros, I’ll need to convert `\newcommand` to `\providecommand`, and `\DeclareMathOperator` should be checked too. Maybe I could consolidate the file-line pairs and summarize concisely. There’s a lot to consider!
thinking
**Organizing findings on macros**

I might be okay with a flat list of about 10 lines. I should identify the files with `\newcommand` and group the findings by their file-line pairs. For example, I could create a medium-effect finding with entries like `standalone/N1_koszul_meta.tex:34; standalone/N2_mc3_all_types.tex:35`, totaling about 16 pairs. The problem is with custom macros violating safety. I need to change `\newcommand` to `\providecommand` and check on `\renewcommand`, too. Should I treat those separately since they worsen the issue?
thinking
**Evaluating file groupings**

I’m thinking about how to group file:line pairs concisely, particularly those with newcommand. I want to focus on files likely imported into chapters, especially summary and survey files. I’m hesitant about standalone research papers since they might not fit in the import. However, since the seam contract prohibits macros via newcommand, including those files seems useful. I also need to address a factorization algebra issue in the theorem and inspect specific lines for consistency and contradictions.
thinking
**Clarifying file counts**

I'm figuring out that we should only count files that are actually read, instead of including anything irrelevant. This makes sense because focusing only on the pertinent files will give a more accurate representation of what we're working with. It seems like a straightforward approach, but I want to ensure that nothing is overlooked in the process. It's important to keep things clear and organized as I go along!
thinking
**Evaluating findings overview**

I’m thinking about summarizing the standalone chapters I've inspected through direct reads or grep hits—maybe I have 23 in total. I don't want to over-precise things. I could establish something like: "Checked: 23 | Findings: 11 | Verdict: FAIL." That means I need to list the 11 findings.

For instance, I’ve identified a high-priority problem where the program assigns Swiss-cheese formality to bar complexes and classes G/L, which then highlights issues with SC colors.
thinking
**Addressing survey issues**

I’m noticing a few problems with the survey documents, particularly around the color conflation and pair order. There’s a mention of potentially combining aspects at location 1515, but I might need to keep some things separate. Also, there's inconsistency in the derived center pair order across different files, which is confusing. I’ll need to fix the order and clarify how closed and open pairs are presented in the summaries.
thinking
**Organizing systemic findings**

I think I can consolidate my findings by listing representative line starts for the identified issues and noting that "the same issue recurs in every file listed below." It might be too lengthy to list everything, so I could just choose the first line of each file. I might also need to group terms like `\renewcommand{\Bbbk}` and `\SS`, but they could be of lower importance than `\newcommand`. Combining them into a systemic finding about non-guarded preambles could work, so I’ll mention the file list as well.
exec
/bin/zsh -lc "sed -n '276,281p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
differential encodes holomorphic factorization on~$\mathbb{C}$, the
deconcatenation coproduct encodes topological factorization
on~$\mathbb{R}$. The two-coloured Swiss-cheese operad
$\mathrm{SC}^{\mathrm{ch,top}}$ emerges on the chiral derived center
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, not on $B(\cA)$
itself.

thinking
**Analyzing macro findings**

I think it might be better to break down the macro findings into categories. For the high category, I’ll note that there's a `\renewcommand{\ref}` appearing in 11 files. In the medium category, I'll highlight the unconditional `\newcommand` blocks present in all non-summary standalone papers. Since there are quite a few of those, I should mention a representative sample and say, "the same issue recurs in..." followed by the file list. That sounds good!
codex
- [HIGH] [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:134) — PROBLEM: line 134 says classes `G/L` have “Swiss-cheese-formal bar complexes,” and line 314 later identifies the bar differential/coproduct with the closed/open Swiss-cheese colours. That conflicts with [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2893), which proves SC-formality iff class `G`, and with [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247), which says the bar complex is only the `E_1` coalgebraic engine while `SC^{ch,top}` lives on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`. FIX: replace the class sentence by “classes `G` and `L` have finite shadow depth; only class `G` is Swiss-cheese formal,” and replace the colour sentence by “the bar differential and deconcatenation coproduct are the two `E_1` dg-coalgebra operations on `B(\cA)`; the Swiss-cheese closed/open colours belong to the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:1432) — PROBLEM: this file repeats the same seam error three times: “Swiss-cheese-formal bar complexes” at lines 1432 and 1812, and explicit colour-assignment to the bar differential/coproduct at line 1614, even though the same file already states the corrected rule at lines 1579–1580 (“`SC^{ch,top}` emerges on the derived center pair, not on `B(\cA)` itself”). FIX: make lines 1432/1812 say “finite shadow depth for classes `G/L`, but SC-formality only for class `G`,” and rewrite line 1614 exactly as “the bar complex carries the `E_1` differential and deconcatenation coproduct; the Swiss-cheese structure is on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:2364) — PROBLEM: the Swiss-cheese/bulk-boundary scoping drifts in three places: line 2364 reverses the pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, line 6193 says “The bar complex carrying both structures is an `SC^{ch,top}`-algebra,” and line 7758 repeats the reversed pair after assigning the closed/open colours to the bar differential/coproduct. That contradicts the same file at lines 6070–6071 and [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466). FIX: normalize every occurrence to `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)` or `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )`, and replace the stale SC-on-bar sentences with “the bar complex supplies the `E_1` differential and deconcatenation coproduct; `SC^{ch,top}` emerges on the derived center pair.”
- [HIGH] [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:1515) — PROBLEM: line 1515 reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, and line 3658 later says the bar differential/coproduct encode the closed/open colours. The corrected manuscript surface uses `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )` and keeps `SC^{ch,top}` off the bar complex: see [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466) and [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1247). FIX: swap the pair order at line 1515, and replace the line-3658 sentence with “the bar complex is the `E_1` coalgebraic engine; the closed/open Swiss-cheese colours live on `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [HIGH] [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:995) — PROBLEM: lines 995–997 say the bar differential “encodes the closed colour” and the coproduct “the open colour.” That is exactly the AP165/ B55–B56 retracted formulation; the corrected rule is in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1257). FIX: replace those lines with “the bar complex classifies twisting morphisms and carries an `E_1` differential plus deconcatenation coproduct; the Swiss-cheese closed/open colours belong to the derived center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`.”
- [MEDIUM] [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:1395) — PROBLEM: this line reverses the derived-center pair as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, but the same file already gives the corrected order at lines 663–664, and the main introduction fixes the order at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1466). FIX: change the phrase to “the derived center pair `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)`,” and, if desired, append “closed/bulk first, open/boundary second” once to lock the convention.
- [MEDIUM] [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:1317) — PROBLEM: the pair is written in the wrong order as `(\cA,\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA))`, drifting from the main manuscript convention `( \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA )`. FIX: swap the order and rewrite the sentence as “the derived center pair `(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)` carries the `\SCchtop`-algebra structure.”
- [HIGH] [computations.tex](/Users/raeez/chiral-bar-cobar/standalone/computations.tex:33) — PROBLEM: this file, plus [classification.tex](/Users/raeez/chiral-bar-cobar/standalone/classification.tex:38), [programme_summary_sections2_4.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections2_4.tex:63), [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:62), [programme_summary_sections9_14.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections9_14.tex:61), [riccati.tex](/Users/raeez/chiral-bar-cobar/standalone/riccati.tex:36), [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:107), [survey_track_a_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_a_compressed.tex:94), [survey_track_b_compressed.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:149), [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:102), and [survey_modular_koszul_duality_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:165), overrides `\ref` globally with `\renewcommand{\ref}`. If any of these files are input into the manuscript, they silently mutate the main reference macro. FIX: delete every `\renewcommand{\ref}` block; introduce a local wrapper instead, e.g. `\providecommand{\localref}[1]{\hyperref[#1]{\textup{\ref*{#1}}}}`, and update local calls from `\ref{...}` to `\localref{...}`.
- [MEDIUM] [N1_koszul_meta.tex](/Users/raeez/chiral-bar-cobar/standalone/N1_koszul_meta.tex:34) — PROBLEM: unconditional `\newcommand`/` \DeclareMathOperator` preamble blocks remain widespread across the standalone surface: [N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:35), [N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:34), [N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:33), [N5_mc5_sewing.tex](/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:33), [N6_shadow_formality.tex](/Users/raeez/chiral-bar-cobar/standalone/N6_shadow_formality.tex:33), [bp_self_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/bp_self_duality.tex:36), [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:37), [classification_trichotomy.tex](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:33), [gaudin_from_collision.tex](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:36), [garland_lepowsky.tex](/Users/raeez/chiral-bar-cobar/standalone/garland_lepowsky.tex:36), [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/genus1_seven_faces.tex:33), [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:39), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:37), [programme_summary_section1.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex:36), [seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/seven_faces.tex:32), [shadow_towers.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:32), [shadow_towers_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v2.tex:35), [three_parameter_hbar.tex](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:34), [virasoro_r_matrix.tex](/Users/raeez/chiral-bar-cobar/standalone/virasoro_r_matrix.tex:33), and [w3_holographic_datum.tex](/Users/raeez/chiral-bar-cobar/standalone/w3_holographic_datum.tex:32). This violates the import-safe seam contract. FIX: change every custom symbol macro from `\newcommand` to `\providecommand`; replace shared-macro mutations like `\renewcommand{\Bbbk}`/`\renewcommand{\SS}` with local names; guard operator declarations with `\@ifundefined{...}{\DeclareMathOperator...}{}` or rewrite them as `\providecommand{\Res}{\operatorname{Res}}`.

## Summary
Checked: 16 | Findings: 9 | Verdict: FAIL
tokens used
698,002
