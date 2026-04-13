# F17_dangling_refs_v1 (966s)

- [CRITICAL] chapters/connections/outlook.tex:276 — PROBLEM: `\ref{thm:hook-type-transport-koszul-duality}` has no target, and the live local theorem is only the conditional `\label{thm:hook-transport-corridor}`. FIX: replace `Theorem~\ref{thm:hook-type-transport-koszul-duality}` with `Theorem~\ref{thm:hook-transport-corridor}` and rewrite `is the proved corridor` to `is the conditional corridor under DS--bar compatibility`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:5974 — PROBLEM: `\ref{part:gravity}` points into Volume II; this repo has no cross-volume `xr` bridge, so the Part reference cannot resolve here. FIX: replace `Part~\ref{part:gravity}` with `Part "Three-Dimensional Quantum Gravity" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7549 — PROBLEM: `\ref{part:e1-core}` points into Volume II and cannot resolve in this build. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7752 — PROBLEM: same broken cross-volume `\ref{part:e1-core}` as above. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/connections/thqg_open_closed_realization.tex:507 — PROBLEM: `\ref{prop:mixed-product-decomposition}` points only to a Volume II proposition, so the local build has no target. FIX: replace `Proposition~\ref{prop:mixed-product-decomposition}` with `the Volume II proposition "Product decomposition of mixed operations"`.
- [HIGH] chapters/connections/thqg_gravitational_s_duality.tex:559 — PROBLEM: `\ref{subsec:gravity-ainf}` points only to a Volume II subsection. FIX: replace `\S\ref{subsec:gravity-ainf}` with `the Volume II subsection "Movement I: the $\Ainf$ structure from the quartic pole"`.
- [HIGH] chapters/examples/free_fields.tex:5074 — PROBLEM: `\ref{thm:bar-cobar-path-integral-heisenberg}` has no target anywhere, so the theorem statement cites nonexistent support for item (iii). FIX: replace the parenthetical with `by direct Gaussian evaluation in the Heisenberg case`.
- [HIGH] chapters/examples/free_fields.tex:5085 — PROBLEM: the proof again cites nonexistent `thm:bar-cobar-path-integral-heisenberg`. FIX: replace `Theorem~\ref{thm:bar-cobar-path-integral-heisenberg}` with `a direct Gaussian computation in the Heisenberg case`.
- [HIGH] chapters/examples/yangians_foundations.tex:1347 — PROBLEM: `\ref{thm:dnp-bar-cobar-identification}` points only to Volume II/III, so the local theorem citation is unresolved. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package"`.
- [HIGH] chapters/theory/chiral_koszul_pairs.tex:2472 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}` in a load-bearing classification sentence. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/theory/three_invariants.tex:257 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}`. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/connections/twisted_holography_quantum_gravity.tex:183 — PROBLEM: `\ref{thm:lines_as_modules}` points only to Volume II, so the local proof chain breaks. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2025 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in live prose. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2253 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in a status table. FIX: replace `Proved (Thm~\ref{thm:lines_as_modules})` with `Proved in Volume II ("Lines as Modules for the Open-Colour Dual")`.
- [MEDIUM] chapters/theory/derived_langlands.tex:1515 — PROBLEM: `\ref{chap:modular-koszul}` has no target; the cited shadow-connection theorem lives in the shadow-metric section. FIX: replace `Chapter~\ref{chap:modular-koszul}` with `Section~\ref{sec:shadow-metric}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:27063 — PROBLEM: `\ref{def:glcm-classification}` has no target; the live definition is `\label{def:shadow-depth-classification}`. FIX: replace `Definition~\ref{def:glcm-classification}` with `Definition~\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `\ref{prop:heisenberg-kappa}` has no target; the explicit Heisenberg formula is already proved in `thm:genus-universality` part (i). FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:genus-universality}(i)`.
- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `\ref{prop:pixton-genus2-planted-forest}` has no target; the exact formula cited is the displayed equation `\label{eq:planted-forest-genus2-explicit-bridge}`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.
- [MEDIUM] chapters/connections/thqg_holographic_reconstruction.tex:1841 — PROBLEM: `\ref{rem:cubic-source-caveat}` has no target; the actual caveat appears in `prop:virasoro-shadow-coefficients`. FIX: replace `Remark~\ref{rem:cubic-source-caveat}` with `Proposition~\ref{prop:virasoro-shadow-coefficients}`.
- [MEDIUM] chapters/theory/higher_genus_foundations.tex:4777 — PROBLEM: `\ref{rem:feynman_genus_g}` is unresolved because the target remark is mislabeled as `\label{sec:feynman_genus_g}` in `chapters/theory/chiral_koszul_pairs.tex:4872`. FIX: rename that target label to `\label{rem:feynman_genus_g}` and cite it here as `Remark~\ref{rem:feynman_genus_g}`.
- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `\ref{rem:free-field-three-theorems}` has no target; the actual free-field synthesis remark is `\label{rem:free-fields-three-pillar}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
- [MEDIUM] chapters/examples/landscape_census.tex:3978 — PROBLEM: same broken `\ref{rem:free-field-three-theorems}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
- [MEDIUM] chapters/connections/thqg_perturbative_finiteness.tex:2104 — PROBLEM: `\ref{rem:thqg-I-spectral-finiteness}` has no target; the proved scalar convergence theorem is `\label{thm:thqg-I-absolute-convergence}`. FIX: replace it with `Theorem~\ref{thm:thqg-I-absolute-convergence}`.
- [MEDIUM] chapters/examples/landscape_census.tex:1467 — PROBLEM: `\ref{rem:w-algebra-three-theorems}` has no target; the live W-algebra synthesis remark is `\label{rem:w-three-pillar}`. FIX: replace it with `Remark~\ref{rem:w-three-pillar}`.
- [MEDIUM] chapters/examples/landscape_census.tex:4016 — PROBLEM: same broken `\ref{rem:w-algebra-three-theorems}`. FIX: replace it with `Remark~\ref{rem:w-three-pillar}`.
- [MEDIUM] chapters/connections/thqg_preface_supplement.tex:2047 — PROBLEM: `\ref{sec:completion-programme-overview}` has no target and points readers away from the actual chapter named in the row. FIX: replace `\S\ref{sec:completion-programme-overview}` with `\S\ref{sec:thqg-critical-string-dichotomy}`.
- [MEDIUM] chapters/examples/y_algebras.tex:855 — PROBLEM: `\ref{sec:concordance-holographic-programme}` has no target; the live concordance subsection is `\label{subsec:concordance-holographic-completion}`. FIX: replace it with `\S\ref{subsec:concordance-holographic-completion}`.
- [MEDIUM] chapters/examples/y_algebras.tex:640 — PROBLEM: `\ref{sec:concordance-three-tier-r-matrix}` has no target; the classification is given by `\label{def:three-tier-r-matrix}`. FIX: replace `\S\ref{sec:concordance-three-tier-r-matrix}` with `Definition~\ref{def:three-tier-r-matrix}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:20681 — PROBLEM: `\ref{sec:landscape-census}` has no target; the live label is the chapter label `\label{ch:landscape-census}`. FIX: replace `\S\ref{sec:landscape-census}` with `Chapter~\ref{ch:landscape-census}`.
- [MEDIUM] chapters/theory/e1_modular_koszul.tex:694 — PROBLEM: same stale `\ref{sec:landscape-census}` and the surrounding parenthesis is already chapter-level prose. FIX: replace `census~\S\ref{sec:landscape-census}` with `Chapter~\ref{ch:landscape-census}`.
- [MEDIUM] chapters/connections/holomorphic_topological.tex:653 — PROBLEM: `\ref{sec:shadow-depth-classification}` has no target; the live object is the definition `\label{def:shadow-depth-classification}`. FIX: replace `\S\ref{sec:shadow-depth-classification}` with `Definition~\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `\ref{sec:sl3-bar-table}` has no target; the stated `1,8,36,204,1352,9892,\ldots` sequence is actually recorded in `\label{rem:sl3-koszul-dual}`. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
- [MEDIUM] chapters/examples/bar_complex_tables.tex:4198 — PROBLEM: same broken `\ref{sec:sl3-bar-table}` in the table caption. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
- [MEDIUM] chapters/connections/outlook.tex:605 — PROBLEM: `\ref{subsec:dr-hierarchy-string}` has no target anywhere in the repo tree. FIX: replace `Section~\ref{subsec:dr-hierarchy-string}` with `Buryak's DR-hierarchy string-equation argument`.
- [MEDIUM] chapters/connections/thqg_open_closed_realization.tex:1239 — PROBLEM: `\ref{subsec:thqg-open-sector-factorization-category}` has no target; the subsection header only has `\label{subsec:thqg-ct2-cooperad-conjecture}`. FIX: add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header at line 1214.
- [MEDIUM] chapters/examples/heisenberg_eisenstein.tex:306 — PROBLEM: `\ref{thm:heisenberg-bar-complex-genus0}` has no target; the live theorem is `\label{thm:heisenberg-bar}`. FIX: replace it with `Theorem~\ref{thm:heisenberg-bar}`.
- [MEDIUM] chapters/examples/yangians_computations.tex:1150 — PROBLEM: `\ref{thm:rtt-all-types}` has no target; the live theorem is `\label{thm:rtt-all-classical-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}`.
- [MEDIUM] chapters/examples/yangians_foundations.tex:1228 — PROBLEM: same stale `\ref{thm:rtt-all-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}(iv)`.

## Summary
Checked: 38 | Findings: 38 | Verdict: FAIL


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
session id: 019d865c-d777-74d1-b54e-1ce88362b5d1
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


MISSION: FOUNDATION AUDIT of chapters/

Find all \ref{} that don't resolve. Run: grep -roh '\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Considering exploration strategy**

I need to start with a brief update: I don’t have permission to browse the internet, and that’s fine. I’ll focus on using commentary tools for shell commands. I’m thinking about updating the plan due to the substantial work involved.

For codebase questions, I should prefer using the explorer sub-agent over manual search or reading files directly. However, I might still need to read files myself since the user wants claims grounded in actual contents. The explorer could help locate issues quickly, and then I can access the files.
thinking
**Examining tools and strategy**

Since I only have the shell for file reading, I need to run the exact grep commands using exec_command. It might be helpful to use multi_tool_use.parallel for executing developer tools simultaneously. I should examine the repository structure and consider which files to read first, even though we’re not editing yet. The user mentioned a mission foundation audit of chapters, so opening the relevant skills might be necessary. I’ll start with a commentary update and then execute commands to read the necessary files.
codex
Auditing `chapters/` for unresolved `\ref{}` first, then I’ll read each flagged location in context and turn every verified break into a file:line finding with an exact replacement label or structural fix.
exec
/bin/zsh -lc "pwd && printf '\\n---\\n' && sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar

---
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
exec
/bin/zsh -lc "printf 'CLAUDE.md\\n'; sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'concordance.tex\\n'; sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "printf 'theorem_registry.md\\n'; sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
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
 succeeded in 51ms:
theorem_registry.md
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2836 |
| Total tagged claims | 3665 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
codex
I’ve loaded the audit protocol and constitutional files. Next I’m collecting the raw unresolved `\ref{}` surface from `chapters/`, then I’ll open every hit in context before I decide whether it is truly unresolved or only a local grep artifact.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sort -u > /tmp/refs.txt
grep -roh '\\\\label{["'^}]*}'"' chapters/ | sort -u > /tmp/labels.txt
comm -23 /tmp/refs.txt /tmp/labels.txt | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l /tmp/refs.txt /tmp/labels.txt' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
       0 /tmp/refs.txt
     519 /tmp/labels.txt
     519 total
 succeeded in 524ms:
\ref{D1}
\ref{D2}
\ref{D3}
\ref{D4}
\ref{D5}
\ref{D6}
\ref{D:genus-tower}
\ref{MK:koszul-htpy}
\ref{MK:koszul}
\ref{MK:modular-htpy}
\ref{MK:modular}
\ref{MK:verdier-htpy}
\ref{MK:verdier}
\ref{alg:NAP-koszul}
\ref{app:arnold-relations}
\ref{app:branch-line-reductions}
\ref{app:coderived-models}
\ref{app:coderived}
\ref{app:combinatorial-frontier}
\ref{app:curved-ainfty-formulas}




thinking
**Evaluating unresolved references**

I need to clarify what the user means by "Find all \ref{} that don't resolve". This sounds like it's about detecting unresolved references during compilation. I should look at the shell pipeline for that. Given that I have to audit thoroughly, I might consider using latexmk or grep for this task. My plan is to ensure that I count unresolved references specifically from the chapters-only command output. I'll need to refine my approach based on context before proceeding.
thinking
**Clarifying unresolved reference findings**

The user mentioned that every unresolved reference is a finding, which raises some questions. I need to ground my approach in the actual file contents, avoiding any guesses or inferences. If a label is in the appendices, it might resolve in a build, but I need to focus on the `chapters/` context the user specified. I might report as "no matching `\label` under chapters/", noting that fixes could include adding a label or retargeting to an existing one. I'll consider searching the entire repository to propose an existing label.
thinking
**Evaluating definitions and references**

I’m considering how each missing definition, hidden import, unresolved reference, or unjustified step can be a significant finding. While reviewing contexts, I should note any references that relate to these issues. However, it’s impractical to audit entire chapters exhaustively. The user asked for an audit focused on chapters and references, so I’ll try to search for unresolved references like `Definition\ref{...}` or `\eqref` as needed to cover what they requested.
thinking
**Planning the audit steps**

I need to create a detailed plan for the audit. It might include several steps like identifying candidate references, assessing the context, finding fixes, and optionally building a cross-check. I'll gather a complete list of unresolved references and could save the output to count the lines afterward. Using `wc -l` sounds useful. Also, I plan to gather reference occurrences with file and line numbers using a command like `rg -n '\\ref{label}' chapters`. Automating this process could save time. Let's focus on using "deep-beilinson-audit" as we move forward.
codex
Using `deep-beilinson-audit` on the reference surface. I have the constitutional layer loaded; now I’m converting the raw `comm` output into concrete file:line hits, checking whether each missing label exists elsewhere in the repo, and then I’ll assign the narrowest exact fix for each occurrence rather than hand-waving “add a label somewhere.”
Plan update
Audit scope is the `chapters/` unresolved `\ref{}` surface, with exact fixes grounded in the local TeX files and any matching labels elsewhere in the repo.
  → Generate the candidate unresolved `\ref{}` list from `chapters/` and count the surface
  • Locate every occurrence with file:line context and search for matching labels across the repo
  • Read the surrounding text for each verified miss and determine the exact fix
  • Re-verify the final findings list against live file contents and summarize counts/verdict
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sort -u > /tmp/refs.txt
grep -roh '\\\\label{["'^}]*}'"' chapters/ | sort -u > /tmp/labels.txt
comm -23 /tmp/refs.txt /tmp/labels.txt > /tmp/unresolved_refs.txt
printf 'refs %s\\n' \""'$(wc -l < /tmp/refs.txt)"
printf '"'labels %s\\n' \""'$(wc -l < /tmp/labels.txt)"
printf '"'unresolved %s\\n' \""'$(wc -l < /tmp/unresolved_refs.txt)"
sed -n '"'1,240p' /tmp/unresolved_refs.txt" in /Users/raeez/chiral-bar-cobar succeeded in 431ms:
refs     3917
labels    12467
unresolved     3917
\ref{D1}
\ref{D2}
\ref{D3}
\ref{D4}
\ref{D5}
\ref{D6}
\ref{D:genus-tower}
\ref{MK:koszul-htpy}
\ref{MK:koszul}
\ref{MK:modular-htpy}
\ref{MK:modular}
\ref{MK:verdier-htpy}
\ref{MK:verdier}
\ref{alg:NAP-koszul}
\ref{app:arnold-relations}
\ref{app:branch-line-reductions}
\ref{app:coderived-models}


thinking
**Identifying command flaws**

I'm noticing that the command shows unique refs at 3917 and labels at 12467, with unresolved refs also at 3917. It seems like the grep label regex didn’t match because it only extracts `\label{...}` instead of the entire string. The process specifically compares `\ref{foo}` to `\label{foo}`, so none actually match. This reveals that the user’s command is flawed; all refs will appear unresolved. I need to suggest correcting this by normalizing the command for accurate results.
thinking
**Finding unresolved references**

This is crucial! I need to consider including the finding about the command flaw. However, the user wants to ensure that every unresolved reference is correctly identified, not just the issue with the script itself. I should use a corrected pipeline to compute the raw label names. It might be useful to search through the `chapters/` directory for references vs. labels. So, I’ll run the corrected command to get counts from both `\ref` and `\label` for accurate results.
codex
The user-specified `comm` pipeline is itself broken: it compares literal `\ref{...}` strings against literal `\label{...}` strings, so it classifies every single reference as unresolved. I’m correcting the extraction to compare raw label names, then I’ll audit only the genuinely missing targets.
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sed -E 's/"'^'"\\\\ref\\{//; s/}"'$//'"' | sort -u > /tmp/ref_names.txt
grep -roh '\\\\label{["'^}]*}'"' chapters/ | sed -E 's/"'^'"\\\\label\\{//; s/}"'$//'"' | sort -u > /tmp/label_names.txt
comm -23 /tmp/ref_names.txt /tmp/label_names.txt > /tmp/unresolved_ref_names.txt
printf 'unique ref names %s\\n' \""'$(wc -l < /tmp/ref_names.txt)"
printf '"'unique label names %s\\n' \""'$(wc -l < /tmp/label_names.txt)"
printf '"'unresolved names %s\\n' \""'$(wc -l < /tmp/unresolved_ref_names.txt)"
sed -n '"'1,260p' /tmp/unresolved_ref_names.txt" in /Users/raeez/chiral-bar-cobar succeeded in 555ms:
unique ref names     3917
unique label names    12467
unresolved names      158
app:arnold-relations
app:branch-line-reductions
app:coderived-models
app:combinatorial-frontier
app:curved-ainfty-formulas
app:homotopy-transfer
app:koszul-reference
app:nonlinear-modular-shadows
app:sign-conventions
app:signs
app:theta
app:w3-jacobi-full
chap:modular-koszul
chap:ordered-associative-chiral-kd
comp:bp-shadow-tower
conj:nms-graph-completed-master-element
conj:nms-nonlinear-phase-standard

thinking
**Evaluating labels in LaTeX files**

I need to consider how many labels might be needed in the appendices or front matter. I'm thinking about searching through all the .tex files to check if a label exists for each unresolved name using a command like `rg -n "\\label\\{NAME\\}"`. Automating this with a shell loop could help, and I’d like to produce a CSV detailing names, reference occurrences in chapters, and global label occurrences. It's important to clarify that unresolved references shouldn't include appendices to avoid false positives. So, I'll compute those counts carefully.
exec
/bin/zsh -lc 'while IFS= read -r name; do
  ref_count=$(rg -n --glob '"'*.tex' \"\\\\\\\\ref\\\\{"'${name//./'"\\\\.}\\\\}\" chapters | wc -l | tr -d ' ')
  label_hits="'$(rg -n --glob '"'*.tex' \"\\\\\\\\label\\\\{"'${name//./'"\\\\.}\\\\}\" . | sed '/"'^$/d'"' | wc -l | tr -d ' ')
  printf '%s|%s|%s\\n' \""'$name" "$ref_count" "$label_hits"
done < /tmp/unresolved_ref_names.txt | tee /tmp/unresolved_ref_status.txt | sed -n '"'1,260p'" in /Users/raeez/chiral-bar-cobarcodex
I have the true candidate set down to 158 missing-in-`chapters/` labels. Now I’m separating real breakage from cross-surface imports by checking whether each target label exists anywhere else in the repo; only labels with zero global definitions survive as genuine unresolved references.
 succeeded in 5.73s:
app:arnold-relations|5|1
app:branch-line-reductions|4|1
app:coderived-models|3|1
app:combinatorial-frontier|2|2
app:curved-ainfty-formulas|1|1
app:homotopy-transfer|11|1
app:koszul-reference|2|1
app:nonlinear-modular-shadows|32|1
app:sign-conventions|7|1
app:signs|18|1
app:theta|2|1
app:w3-jacobi-full|1|2
chap:modular-koszul|1|0
chap:ordered-associative-chiral-kd|0|0
comp:bp-shadow-tower|1|1
conj:nms-graph-completed-master-element|1|1
conj:nms-nonlinear-phase-standard|1|1
conj:nms-rank2-isomonodromic|1|1
conj:superstring-degeneration|1|1
conj:w3-bar-gf|4|2
exec
/bin/zsh -lc "awk -F'|' '"'$2>0 && $3==0 {print $1}'"' /tmp/unresolved_ref_status.txt > /tmp/globally_unresolved_ref_names.txt
printf 'globally unresolved names %s\\n' \""'$(wc -l < /tmp/globally_unresolved_ref_names.txt)"
sed -n '"'1,260p' /tmp/globally_unresolved_ref_names.txt" in /Users/raeez/chiral-bar-cobar succeeded in 69ms:
globally unresolved names       28
chap:modular-koszul
def:glcm-classification
part:e1-core
part:gravity
prop:heisenberg-kappa
prop:mixed-product-decomposition
prop:pixton-genus2-planted-forest
rem:cubic-source-caveat
rem:feynman_genus_g
rem:free-field-three-theorems
rem:thqg-I-spectral-finiteness
rem:w-algebra-three-theorems
sec:completion-programme-overview
sec:concordance-holographic-programme
sec:concordance-three-tier-r-matrix
sec:landscape-census
sec:shadow-depth-classification
sec:sl3-bar-table
subsec:dr-hierarchy-string

thinking
**Determining label candidates**

I need to search the repository for similar label candidates using rg for each unresolved name. The user is looking for an exact fix, not just a diagnosis, so I'll have to figure out the intended label by reading the context and matching the text. This task involves 28 names, and I might encounter multiple occurrences. I'll probably create a table to capture all occurrences along with file line numbers and text for those names. I'll use a shell loop with rg -n -F for this.
codex
The candidate surface is now only 28 truly unresolved label names with at least one live `\ref{}` and zero matching `\label{}` anywhere in the repo. I’m reading each occurrence in context and matching it to the nearest existing theorem/section/part label so every finding ends with a concrete replacement, not “label missing.”
exec
/bin/zsh -lc "while IFS= read -r name; do
  printf '=== %s ===\\n' \""'$name"
  rg -n -F "'"\\\\ref{"'$name}" chapters || true
  printf '"'\\n'
done < /tmp/globally_unresolved_ref_names.txt" in /Users/raeez/chiral-bar-cobar succeeded in 325ms:

=== rem:cubic-source-caveat ===
chapters/connections/thqg_holographic_reconstruction.tex:1841:Remark~\textup{\ref{rem:cubic-source-caveat}}\textup{)}.

=== rem:feynman_genus_g ===
chapters/theory/higher_genus_foundations.tex:4777:(We use the closed-string convention $\hbar^{2g-2}$; the Feynman-diagram convention in \S\ref{rem:feynman_genus_g} uses $\hbar^{g-1}$, corresponding to $\hbar_{\text{there}} = \hbar_{\text{here}}^2$.)

=== rem:free-field-three-theorems ===
chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).

=== rem:thqg-I-spectral-finiteness ===
chapters/connections/thqg_perturbative_finiteness.tex:2104:scalar lane (Remark~\ref{rem:thqg-I-spectral-finiteness}).

=== rem:w-algebra-three-theorems ===
chapters/examples/landscape_census.tex:1467:Remark~\ref{rem:w-algebra-three-theorems} (W-algebras),
chapters/examples/landscape_census.tex:4016: (Remark~\ref{rem:w-algebra-three-theorems}).

=== sec:completion-programme-overview ===
chapters/connections/thqg_preface_supplement.tex:2047: & \S\ref{sec:completion-programme-overview}





thinking
**Inspecting context for labels**

I need to check the context around each occurrence and figure out the correct labels. There might be missing labels in Volume II because they only exist in that repo and not in the current one. User's build of Volume I may not include those, and unresolved references could stem from the TeX build. I think I’ll need to replace `\ref` with a textual citation from Volume II since cross-repo references don't resolve. I'll read around those references and see if I can search in Volume II.
thinking
**Searching for Volume II labels**

I’m thinking I might be able to read other directories, so I should check that. I need to search the Volume II repo for labels like `part:e1-core`. The exact fix might involve renaming to the actual label in Volume II or replacing it with more descriptive text specific to that volume. If accessible, I should use `rg` in `/chiral-bar-cobar-vol2`. Many missing labels seem to be external volume references, so I’ll look across sibling repos. It's essential to remember that LaTeX cross-repo references won’t resolve without special configurations.
thinking
**Inspecting cross-repo referencing**

I need to check if a cross-repo referencing mechanism is available. I should search for `xr` packages or instances of `externaldocument`. It’s possible that this repo contains cloned Volume II chapter files through symlinks, but I need to inspect `main.tex` for clarity. I can search for `externaldocument` there too. Compiling could be a straightforward way to confirm unresolved references, even if it might be heavy. I should identify candidate labels both in the current and external repos for any unresolved references.
thinking
**Assessing label names**

I’m trying to figure out if the likely chapter label is `chap:landscape-census` or `chap:landscape_census`. I should search for similar labels in the current repo, maybe using a script. 

We’re looking for an exact fix and considering if the “Pre-Edit Verification Protocol” is needed before editing, especially since we’re auditing. I realize that we might not need all 28 names if some are just comments. Comments don't affect the build, so I need to filter out those from our unresolved list.
thinking
**Identifying unresolved labels**

I need to detect unresolved references, and it seems the actual list is smaller than expected. I plan to read each occurrence in context to understand what's going on. I could find malformed references like `\S\ref{thm:frame-heisenberg-koszul-dual}` that might be using theorem labels incorrectly. If the label exists, we’re likely fine. 

My next step is to search through the entire repo and the sibling volumes for all 28 names or similar labels. I may create a small shell script to print the current context and any closely related labels.
codex
I’ve hit the second-order failure mode: several of these “missing” labels are not typos inside one file, they are cross-volume `\ref{}` calls into labels that live only in sibling repos. That does not excuse them; it means the exact fix has to be a repo-local citation or a mirrored label, because the current build cannot resolve a foreign label by magic.
exec
/bin/zsh -lc "while IFS= read -r name; do
  printf '=== %s ===\\n' \""'$name"
  rg -n -F "'"\\\\label{"'$name}" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups || true
  printf '"'\\n'
done < /tmp/globally_unresolved_ref_names.txt" in /Users/raeez/chiral-bar-cobar succeeded in 553ms:

=== prop:heisenberg-kappa ===

=== prop:mixed-product-decomposition ===
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1048:\label{prop:mixed-product-decomposition}

=== prop:pixton-genus2-planted-forest ===

=== rem:cubic-source-caveat ===

=== rem:feynman_genus_g ===

=== rem:free-field-three-theorems ===

=== rem:thqg-I-spectral-finiteness ===

=== rem:w-algebra-three-theorems ===

=== sec:completion-programme-overview ===


thinking
**Investigating label mapping**

I see that there are exact labels for some items, but for others, I might need to find equivalent labels in the current repository. I should inspect the contexts and search similar labels, potentially creating a mapping through a fuzzy candidate search. For each unresolved name, searching for similar substrings in labels could help. It’s vital to record findings for every unresolved occurrence, even if they aren't unique. However, managing duplicates will be a challenge. I'll need to compute the number of occurrences, which might be around 45.
exec
/bin/zsh -lc 'total=0
while IFS= read -r name; do
  c=$(rg -n -F "'"\\\\ref{"'$name}" chapters | wc -l | tr -d '"' ')
  total="'$((total + c))
done < /tmp/globally_unresolved_ref_names.txt
printf '"'occurrences %s\\n' \""'$total"' in /Users/raeez/chiral-bar-cobar succeeded in 446ms:
occurrences 39

thinking
**Planning typo correction**

I'm looking at 39 occurrences that need fixing, which feels manageable! I need to decide on a specific fix for each one. I might consider automating some corrections by mapping obvious typos, but I should also inspect the surrounding lines for context. Using `sed -n` could help, and maybe I can process multiple files in parallel, although it might be simpler to group and check them manually. There are 28 unique names, so I’ll make a list with the relevant lines using awk.
exec
/bin/zsh -lc "while IFS= read -r name; do
  rg -n -F \"\\\\ref{"'$name}" chapters | while IFS=: read -r file line rest; do
    start=$((line-2)); if [ $start -lt 1 ]; then start=1; fi
    end=$((line+2))
    printf '"'=== %s | %s:%s ===\\n' \""'$name" "$file" "$line"
    sed -n "${start},${end}p" "$file"
    printf '"'\\n'
  done
done < /tmp/globally_unresolved_ref_names.txt" in /Users/raeez/chiral-bar-cobar succeeded in 571ms:
=== prop:heisenberg-kappa | chapters/examples/y_algebras.tex:340 ===
 $\kappa_J = \Psi$. The Heisenberg current at level~$\Psi$
 contributes $\kappa = k$ by the Heisenberg formula
 \textup{(}Proposition~\textup{\ref{prop:heisenberg-kappa}}\textup{)}.
\item \emph{Total}: $\kappa = \kappa_T + \kappa_J = 0 + \Psi
 = \Psi$.

=== prop:mixed-product-decomposition | chapters/connections/thqg_open_closed_realization.tex:507 ===
$C_*(\FM_{k|m}(\Sigma_g, \partial))
\simeq C_*(\FM_k(\Sigma_g)) \times C_*(E_1(m))$
(Volume~II, Proposition~\ref{prop:mixed-product-decomposition} in the
modular Swiss-cheese chapter) holds at all genera.
The open colour $E_1(m)$ is genus-independent: the interval~$\mathbb{R}$

=== prop:pixton-genus2-planted-forest | chapters/examples/lattice_foundations.tex:1714 ===
Part~(iv) follows from the explicit formula
$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
(Proposition~\ref{prop:pixton-genus2-planted-forest})
with $S_3 = 0$.
Part~(v) is the lattice complementarity of

thinking
**Analyzing findings**

I'm thinking the actual findings might be 38 instead of 39, so I should exclude certain comments. I probably need to identify similar labels with ref_count 0 that came up due to comments, but we've already excluded those. The `thm:modular` comment should come off the audit surface. I'm realizing I need to search for any other comment occurrences among the 39, particularly focusing on things like `chap:ordered-associative-chiral-kd` since they might have a ref_count of 0 because of being commented.
codex
I’m in the line-by-line phase now. Some misses are pure typos against an existing local label, some are unlabeled theorem/section surfaces that need a label inserted, and some are illegal cross-volume `\ref{}` calls that need to be rewritten as plain Volume II/III citations because there is no cross-repo label bridge in this build.
exec
/bin/zsh -lc "rg -n \"\\\\label\\\\{(chap:|def:|prop:|rem:|sec:|subsec:|thm:)["'^}]*'"\\\\}\" chapters/examples chapters/theory chapters/connections | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "glcm|G/L/C/M classification|heisenberg.*kappa|mixed product|Pixton|cubic-source|free-field|W-algebra.*three|completion programme|holographic programme|three-tier.*r-matrix|landscape census|shadow depth classification|sl3 bar|DR hierarchy|open-sector factorization|path integral|all-types RTT|hook-type|line-operator category|modular characteristic|Heisenberg bar complex at genus" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:\label\{(chap:|def:|prop:|rem:|sec:|subsec:|thm:)[^}]*\})
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
Total output lines: 1112

chapters/examples/deformation_quantization.tex:57:where (see Cattaneo--Felder \cite{CattaneoFelder99} for the path integral interpretation):
chapters/examples/deformation_quantization.tex:699:The configuration space integrals underlying Kontsevich's formality theorem are the mathematical counterpart of path integral amplitudes.
chapters/examples/w3_holographic_datum.tex:60:). The modular characteristic $\kappa$ is
chapters/examples/w3_holographic_datum.tex:114:\subsection{The line-operator category \texorpdfstring{$\mathcal{C}$}{C}}
chapters/examples/w3_holographic_datum.tex:117:On the evaluation-generated core of the line-operator category,
chapters/examples/w3_holographic_datum.tex:171:\section{The modular characteristic \texorpdfstring{$\kappa(\Walg_3) = 5c/6$}{kappa(W3) = 5c/6}}
chapters/examples/w3_holographic_datum.tex:174:The modular characteristic of $\Walg_3$ is the genus-1 obstruction
chapters/examples/w3_holographic_datum.tex:191:The modular characteristic decomposes additively over the
chapters/examples/w3_holographic_datum.tex:197:The $T$-channel coincides with the Virasoro modular characteristic
chapters/examples/w3_holographic_datum.tex:228:(P5)~the modular characteristic computed from the
chapters/examples/w3_holographic_datum.tex:264:The modular characteristics of $\Walg_3$ and its Koszul dual sum to
chapters/examples/w3_holographic_datum.tex:277:Kac--Moody and free-field families only, where the Feigin--Frenkel
chapters/examples/w3_holographic_datum.tex:386:prior literature; the entry of the landscape census
chapters/examples/w3_holographic_datum.tex:574:$\kappa_i$ are the per-channel modular characteristics. For
chapters/examples/w3_holographic_datum.tex:792:of the holographic programme of
chapters/examples/w_algebras_deep.tex:30:\index{W-algebras@$\mathcal{W}$-algebras!three-pillar interpretation (deep)}
chapters/examples/w_algebras_deep.tex:230:computations and the hook-type family results provide the first
chapters/examples/w_algebras_deep.tex:358:is the free-field avatar of $\Theta$ factoring
exec
/bin/zsh -lc 'rg -n "externaldocument|xr-hyper|xr" main.tex chapters preamble* *.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: no matches found: preamble*


thinking
**Refining search strategy**

I see that the search output was truncated, which is a bit frustrating. I think I need to focus on a more targeted search approach instead of getting a massive output that might not be useful. There's also the issue that external documents don't seem to work properly. So, I’ll have to run another search with proper escaping and a more refined query. Let's see if that improves the results!
thinking
**Searching file labels**

I think it might be helpful to use file labels that list relevant files in a more targeted way. I'm considering searching labels by their exact titles or nearby names with the command `rg -n -F "\\label{...}"` instead of regex. For similar label names, I'll try using `rg -n "label\\{.*landscape.*\\}" chapters`, but I need to ensure I quote properly using single quotes. Smaller grouped searches could also make this more efficient.
exec
/bin/zsh -lc "rg -n 'label\\{["'^}]*landscape[''^}]*'"\\}|label\\{["'^}]*shadow-depth[''^}]*'"\\}|label\\{["'^}]*sl3[''^}]*bar[''^}]*'"\\}|label\\{["'^}]*completion[''^}]*overview[''^}]*'"\\}|label\\{["'^}]*three-tier[''^}]*r-matrix[''^}]*'"\\}|label\\{["'^}]*holographic[''^}]*programme[''^}]*'"\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/symmetric_orbifolds.tex:239:\section{Shadow depth inheritance}\label{sec:symn-shadow-depth}
chapters/examples/symmetric_orbifolds.tex:242:\ClaimStatusProvedHere]\label{prop:symn-shadow-depth}
chapters/examples/symmetric_orbifolds.tex:246:\begin{equation}\label{eq:symn-shadow-depth-bound}
chapters/examples/bar_complex_tables.tex:176:\begin{computation}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential]\label{comp:sl3-bar}
chapters/examples/bar_complex_tables.tex:3148:\label{tab:rmatrix-pole-landscape}
chapters/examples/landscape_census.tex:2:\label{ch:landscape-census}
chapters/examples/landscape_census.tex:587:\label{tab:free-energy-landscape}
chapters/examples/landscape_census.tex:674:\label{tab:shadow-invariants-landscape}
chapters/examples/landscape_census.tex:1102:\label{tab:koszulness-landscape-census}
chapters/examples/landscape_census.tex:2583:\begin{conjecture}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} bar generating function; \ClaimStatusConjectured]\label{conj:sl3-bar-gf}
chapters/examples/landscape_census.tex:2587:\begin{equation}\label{eq:sl3-bar-gf}
chapters/examples/landscape_census.tex:2592:\begin{equation}\label{eq:sl3-bar-recurrence}
chapters/connections/thqg_gravitational_yangian.tex:817:\label{rem:thqg-V-r-matrix-landscape}
chapters/examples/beta_gamma.tex:2643:\label{rem:betagamma-landscape-position}
chapters/connections/thqg_holographic_reconstruction.tex:205:\label{thm:shadow-depth-dichotomy}
chapters/connections/thqg_holographic_reconstruction.tex:208:\begin{equation}\label{eq:shadow-depth-definition-recall}
chapters/connections/thqg_holographic_reconstruction.tex:349:\label{subsec:shadow-depth-invariant}
chapters/connections/thqg_holographic_reconstruction.tex:359:\label{def:shadow-depth-holographic}
chapters/examples/yangians_drinfeld_kohno.tex:6919:\label{prop:rmatrix-pole-landscape}
chapters/examples/y_algebras.tex:491:\label{sec:y-shadow-depth}
exec
/bin/zsh -lc "rg -n 'label\\{["'^}]*free-field[''^}]*three[''^}]*'"\\}|label\\{["'^}]*w-algebra[''^}]*three[''^}]*'"\\}|label\\{["'^}]*cubic[''^}]*source[''^}]*'"\\}|label\\{["'^}]*feynman[''^}]*genus[''^}]*'"\\}|label\\{["'^}]*heisenberg[''^}]*kappa[''^}]*'"\\}|label\\{["'^}]*glcm[''^}]*'"\\}|label\\{["'^}]*Pixton[''^}]*'"\\}|label\\{["'^}]*pixton[''^}]*'"\\}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'externaldocument|xr-hyper|usepackage\\{xr\\}|usepackage\\{xr-hyper\\}' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:5429:\label{subsec:pixton-from-shadows}
chapters/examples/w_algebras_deep.tex:5446:\label{conj:pixton-from-shadows}
chapters/examples/w_algebras_deep.tex:5464:\begin{equation}\label{eq:pixton-MC}
chapters/examples/w_algebras_deep.tex:5480:\label{rem:pixton-genus2-verification}
chapters/examples/w_algebras_deep.tex:5501:\label{rem:pixton-class-m-only}
chapters/examples/w_algebras_deep.tex:5520:\label{rem:pixton-scope-converse}
chapters/examples/heisenberg_eisenstein.tex:1086:\begin{equation}\label{eq:heisenberg-kappa-formula}
chapters/examples/free_fields.tex:94:\label{rem:free-fields-three-pillar}
chapters/connections/thqg_holographic_reconstruction.tex:1103:\label{rem:cubic-permanent-source}
chapters/connections/thqg_soft_graviton_theorems.tex:1654:\label{rem:thqg-VI-cubic-source}
chapters/connections/concordance.tex:4050:\label{rem:pixton-from-mc}
chapters/connections/concordance.tex:4080:\label{thm:pixton-from-shadows}% NOTE: retains conj: prefix for backward compatibility; claim is ProvedHere
chapters/connections/concordance.tex:4109:\label{rem:pixton-conjecture-status}
chapters/connections/concordance.tex:4200:\label{rem:pixton-genus2-computation}
chapters/connections/thqg_gravitational_complexity.tex:243:\label{lem:thqg-cubic-source}
chapters/connections/thqg_gravitational_complexity.tex:249:\begin{equation}\label{eq:thqg-cubic-source-contribution}
chapters/connections/thqg_gravitational_complexity.tex:264:\begin{equation}\label{eq:thqg-cubic-source-explicit}
chapters/theory/higher_genus_foundations.tex:2168:\label{conv:heisenberg-kappa-notation}
chapters/theory/chiral_koszul_pairs.tex:4872:\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
chapters/theory/higher_genus_modular_koszul.tex:25258:\label{conj:pixton-from-shadows-hgmk}
 succeeded in 52ms:
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1423:/bin/zsh -lc "rg -n --no-heading 'xr|externaldocument|xr-hyper' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 76ms:
./wave2_audit_20260413_001942/C17_concordance.md:1840:/bin/zsh -lc "rg -n '\\\\externaldocument|xr-hyper|xr' main.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/C17_concordance.md:1910:Interesting that there’s no local label definition for ds-hpl-transfer or def:bordified-curve in this repository, yet there's a reference to `\ref{thm:ds-hpl-transfer}`. It could be resolved through build machinery outside of grep, possibly related to an aux import. I might need to check the main.tex or the preamble for any xr externaldocument. My earlier search didn’t reveal externaldocument, but it was truncated, so I'll perform a targeted grep in main.tex.
./wave2_audit_20260413_001942/C17_concordance.md:1914:/bin/zsh -lc "rg -n -F 'externaldocument' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./wave2_audit_20260413_001942/C17_concordance.md:1915:/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:17:\externaldocument{../main}
./wave2_audit_20260413_001942/C17_concordance.md:1917:/bin/zsh -lc "rg -n -F 'xr-hyper' /Users/raeez/chiral-bar-cobar -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./wave2_audit_20260413_001942/C17_concordance.md:1918:/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:16:\usepackage{xr-hyper}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:100:/bin/zsh -lc "rg -n 'externaldocument|xr-hyper|xr\\b|zexternaldocument' main.tex preamble.tex texmf -g '"'!**/*.pdf'"'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:170:/bin/zsh -lc "rg -n 'externaldocument|xr-hyper|\\\\usepackage\\{xr\\}|\\\\usepackage\\{xr-hyper\\}' ." in /Users/raeez/chiral-bar-cobar succeeded in 135ms:
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:171:./compute/audit/chriss_ginzburg_gap_inventory_2026_03_31.md:116:- **Action needed**: set up `xr-hyper` package in Vol II
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:172:./compute/audit/chriss_ginzburg_gap_inventory_2026_03_31.md:248:| S6 (77 cross-vol refs) | Open | Set up xr-hyper |
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:391:\usepackage{xr-hyper}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:392:\externaldocument{../main}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1586:/bin/zsh -lc "rg -n 'vol2|xrefs|externaldocument|xr-hyper|export_.*xrefs|part:e1-core|part:gravity|part:examples' scripts .latexmkrc latexmkrc Makefile makefile . -g '"'!wave*'"' -g '"'!audit*'"' -g '"'!compute/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./scripts/export_vol1_xrefs.py:2:"""Export Vol I cross-reference labels into a flat .aux file for Vol II xr-hyper.
./scripts/export_vol1_xrefs.py:6:and writes them into a single flat file vol1-xrefs.aux that xr-hyper can
./scripts/export_vol1_xrefs.py:75:    # but xr-hyper is fine with duplicates; we keep all for safety)
./tmp_standalone_audit/survey_v2_xr.tex:16:\usepackage{xr-hyper}
./tmp_standalone_audit/survey_v2_xr.tex:17:\externaldocument{../main}
./compute/audit/chriss_ginzburg_gap_inventory_2026_03_31.md:116:- **Action needed**: set up `xr-hyper` package in Vol II
exec
/bin/zsh -lc "sed -n '1,40p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,40p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

 succeeded in 51ms:
%% ════════════════════════════════════════════════════════════════════════
%% E₁ MODULAR KOSZUL DUALITY
%%
%% The ordered (associative) parallel to the commutative modular
%% Koszul theory. Extracted to a standalone chapter so that the
%% E₁/E_∞ parallelism is architecturally visible.
%% ════════════════════════════════════════════════════════════════════════

\chapter{\texorpdfstring{$E_1$}{E1} Modular Koszul Duality}
\label{chap:e1-modular-koszul}

The scalar curvature $\kappa(\cA)$ is a single number: the
$\Sigma_2$-coinvariant of a meromorphic function $r(z)$ that records
the full spectral scattering of the algebra. The cubic shadow
$\mathfrak{C}(\cA)$ is the $\Sigma_3$-coinvariant of the Drinfeld
associator $\Phi_{\mathrm{KZ}}$. At every degree the $E_\infty$
invariant is a scalar projection of an ordered object that carries
strictly more information, and the data killed by the coinvariant
projection is the associative factorization pattern governed by
Stasheff associahedra rather than symmetric groups.
exec
/bin/zsh -lc "sed -n '1490,1535p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\operatorname{av}^{(r)}$ project out precisely the weight-$r$ layer
of the fiber functor.
The degree-$2$ identity
$\operatorname{av}\bigl(r(z)\bigr) = \kappa^{\mathrm{KM}} =
\dim(\fg)\,(k + h^\vee)/(2h^\vee)$
%: kappa^{KM} from C3; k=0 -> dim(g)/2, k=-h^v -> 0 verified
is the rank recovery: the first nontrivial shadow invariant of the
$r$-matrix determines the categorical dimension of the fiber functor,
which is the rank of $G^\vee$.
From the perspective of the geometric Langlands
correspondence~\cite{BD04,FG06}, the bar complex at integral level
occupies a specific position: it is the vertex-algebraic avatar of the
de~Rham side, with the bar differential encoding the flat connection
on the critical-level Hecke eigensheaf, while the Koszul dual
$V_{k^\vee}(\fg^\vee)$ occupies the Betti side.
\end{remark}


\begin{remark}[Shadow connection, opers, and the Hitchin WKB]
\label{rem:shadow-hitchin-wkb}

thinking
**Clarifying chapter references**

I think `chap:modular-koszul` is probably meant to point to `chap:e1-modular-koszul`, but I wonder if the higher genus version is not labeled as a chapter? Actually, it appears that the higher genus modular Koszul starts with a section rather than a chapter. Maybe `chap:modular-koszul` was an old label for that section? I'll search for the correct chapter label near the main structure by looking for `\chapter{...Modular Koszul...}` in the current repository.
exec
/bin/zsh -lc "rg -n '\\\\chapter\\{.*Modular Koszul|\\\\label\\{chap:["'^}]*modular[''^}]*'"\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/semistrict_modular_higher_spin_w3.tex:6:\label{chap:semistrict-modular-W3}
chapters/connections/entanglement_modular_koszul.tex:14:\label{chap:entanglement-modular-koszul}
chapters/theory/e1_modular_koszul.tex:9:\chapter{\texorpdfstring{$E_1$}{E1} Modular Koszul Duality}
chapters/theory/e1_modular_koszul.tex:10:\label{chap:e1-modular-koszul}

thinking
**Considering chapter references**

I'm wondering if `Chapter\ref{chap:modular-koszul}` might be outdated and should actually be updated to `Chapter\ref{chap:e1-modular-koszul}`. But then again, the derived_langlands remark indicates that the shadow connection theorem is likely in the higher_genus_modular_koszul section rather than the e1. I should check the label `thm:shadow-connection` to clarify where everything fits! It’s all a bit convoluted, but I’m determined to sort it out.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:shadow-connection}' chapters && sed -n '28800,28930p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:18579:\label{thm:shadow-connection}
construction
(Definition~\ref{def:bar-differential-complete}).
The stable-graph coefficient algebra $\mathsf{G}_{\mathrm{mod}}$
(Definition~\ref{def:stable-graph-coefficient-algebra}) is a purely
combinatorial object built from the modular operad of stable curves.
Their tensor product carries a bar-cobar differential whose cobar
$\Omega(\barB^{\mathrm{ch}}(L) \otimes \mathsf{G}_{\mathrm{mod}})$
is a cyclic factorization algebra by
Theorem~\ref{thm:bar-modular-operad}. At genus~$0$,
$\mathsf{G}_{\mathrm{mod}}$ reduces to the trivial coefficient,
recovering the Nishinaka envelope. On the Koszul locus,
bar-cobar inversion
(Theorem~\ref{thm:higher-genus-inversion}) gives a
quasi-isomorphism back to~$L$, so the construction is faithful.

\smallskip\noindent\textup{(ii)}
Given $U^{(g')}_X(L)$ for all $g' < g$, the genus-$g$ contribution
is determined by sewing lower-genus amplitudes along stable-curve
degenerations. The HS-sewing criterion

thinking
**Evaluating chapter labels**

It looks like the chapter label might not exist because "higher_genus_modular_koszul" is a section, not a chapter. The remark in derived_LANGLANDS shows that "chapter" = "chap:e1-modular-koszul" may not relate to shadow connections. I need to check for a section label near the theorem for shadow connections. If there's no chapter label, I might just replace "Chapter\ref{chap:modular-koszul}" with "Theorem\ref{thm:shadow-connection}" or "Section\ref{sec:shadow-connections}". I’ll search the nearby lines for relevant section labels.
exec
/bin/zsh -lc "sed -n '18480,18610p' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,140p'
rg -n 'label\\{sec:["'^}]*shadow[''^}]*'"\\}|label\\{subsec:["'^}]*shadow[''^}]*'"\\}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
which vanishes at $\kappa = 0$ (trivially) and
$\kappa = 1$ (Heisenberg at $k = 1$). The anomaly
is the coefficient of the cubic term
$u^2 u_x$ that appears in the $\kappa$-deformed
Lax pair but not in the standard one.
For the standard landscape: $\kappa = 1$ occurs only for
Heisenberg at level~$1$ (class~$\mathbf{G}$, where the
tower terminates at degree~$2$ and the KdV flow is trivial).
For all other algebras, $\kappa \neq 1$ and the
$\kappa$-deformation is genuine.

\smallskip
\noindent\textbf{$\kappa$-Painlev\'e~I.}
The self-similar reduction of~\eqref{eq:kappa-deformed-kdv}
produces the $\kappa$-deformed Painlev\'e~I equation
\begin{equation}\label{eq:kappa-painleve-I}
 y''(x) = \frac{6}{\kappa}\,y(x)^2 + x,
\end{equation}
which reduces to standard Painlev\'e~I at $\kappa = 1$.

thinking
**Fixing references**

It seems I need to make a correction: the reference should be to a section rather than a chapter. I think I should replace `Chapter\ref{chap:modular-koszul}` with `Section\ref{sec:shadow-metric}` since the shadow connection theorem is likely in that section. I might need to check the lines around 17177 for more clarity. Also, for the `def:glcm-classification`, I should search for similar labels around classification. That might help streamline things!
exec
/bin/zsh -lc "rg -n 'label\\{["'^}]*glcm[''^}]*'"\\}|label\\{["'^}]*classification[''^}]*'"\\}|G/L/C/M classification' chapters/theory/higher_genus_modular_koszul.tex chapters/examples/landscape_census.tex chapters/theory/ordered_associative_chiral_kd.tex chapters/theory/en_koszul_duality.tex chapters/examples/logarithmic_w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/logarithmic_w_algebras.tex:447:% Section 6: Shadow depth and the G/L/C/M classification
chapters/examples/logarithmic_w_algebras.tex:450:\section{Shadow depth and the G/L/C/M classification}
chapters/examples/landscape_census.tex:2685:\label{thm:bar-gf-classification}
chapters/examples/landscape_census.tex:2728:\label{tab:bar-gf-classification}
chapters/theory/ordered_associative_chiral_kd.tex:5033:\label{rem:annular-pole-classification}
chapters/theory/ordered_associative_chiral_kd.tex:7184:\label{thm:drinfeld-classification}
chapters/theory/ordered_associative_chiral_kd.tex:7765:\label{rem:glcm-commentary}%
chapters/theory/ordered_associative_chiral_kd.tex:7766:\index{shadow depth!G/L/C/M classification|textbf}%
chapters/theory/en_koszul_duality.tex:886:\begin{remark}[The G/L/C/M classification under $\En$]
chapters/theory/en_koszul_duality.tex:887:\label{rem:glcm-en}
chapters/theory/en_koszul_duality.tex:3729:\label{lem:en-formality-deformation-classification}
chapters/theory/higher_genus_modular_koszul.tex:12126:\label{rem:depth-classification-holographic-truncation}
chapters/theory/higher_genus_modular_koszul.tex:14959:%% FORCED DICHOTOMY: the G/L/C/M classification is not a taxonomy
chapters/theory/higher_genus_modular_koszul.tex:16336:\label{def:shadow-depth-classification}
chapters/theory/higher_genus_modular_koszul.tex:16643:\label{thm:shadow-archetype-classification}
chapters/theory/higher_genus_modular_koszul.tex:16844:\label{fig:shadow-archetype-classification}
chapters/theory/higher_genus_modular_koszul.tex:22124:\index{G/L/C/M classification!free-field scalar exactness}
chapters/theory/higher_genus_modular_koszul.tex:27057:\label{conj:resurgent-shadow-classification}
chapters/theory/higher_genus_modular_koszul.tex:27062:The G/L/C/M classification
chapters/theory/higher_genus_modular_koszul.tex:27960:The G/L/C/M classification of

thinking
**Exploring classification details**

I think `def:shadow-depth-classification` could be the precise fix I need. I should check around line 16336 to confirm it's defined there. Line 27063 in `higher_genus_modular_koszul` should reference `def:shadow-depth-classification`, which looks promising. I noticed three `part:e1-core` and `part:gravity` cross-volume references; I want to ensure these are accurate. I might need to use either exact part numbers or `PartI` and `PartII` if I'm sure of them. I’ll have to search `main.tex` to clarify those labels.
exec
/bin/zsh -lc "sed -n '1240,1415p' /Users/raeez/chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\v{C}ech/Thom--Sullivan descent.

\input{chapters/theory/foundations}
\input{chapters/theory/locality}
\input{chapters/theory/axioms}
\input{chapters/theory/equivalence}
\input{chapters/theory/bv-construction}
\input{chapters/theory/factorization_swiss_cheese}
\input{chapters/theory/raviolo}
\input{chapters/theory/raviolo-restriction}
\input{chapters/theory/fm-calculus}
\input{chapters/theory/orientations}
\input{chapters/theory/fm-proofs}
\input{chapters/theory/pva-descent-repaired}
\input{chapters/theory/pva-expanded-repaired}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\part{The $E_1$ Core}
\label{part:e1-core}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
exec
/bin/zsh -lc "rg -n 'Heisenberg.*formula|Heisenberg.*kappa|kappa\\(\\cH|kappa\\(H_|Heisenberg current.*kappa|label\\{["'^}]*heisenberg[''^}]*kappa[''^}]*'"\\}' chapters/examples chapters/theory" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Heisenberg.*formula|Heisenberg.*kappa|kappa\(\cH|kappa\(H_|Heisenberg current.*kappa|label\{[^}]*heisenberg[^}]*kappa[^}]*\})
                                                    ^^
error: unrecognized escape sequence

thinking
**Simplifying strings**

I'm thinking that using simpler fixed strings could be a beneficial approach. It seems like it might help to make things clearer and easier to understand. I want to ensure that I'm using language that’s straightforward and accessible. This could also enhance usability, which is always a plus. I’ll keep this in mind while developing responses! It seems like a good way to improve communication.
exec
/bin/zsh -lc "rg -n -F 'Heisenberg current at level' chapters/examples/y_algebras.tex chapters/examples/free_fields.tex chapters/examples/heisenberg_eisenstein.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/y_algebras.tex:338: $\kappa_J = \Psi$. The Heisenberg current at level~$\Psi$
exec
/bin/zsh -lc "rg -n -F 'kappa(\\cH_' chapters/examples/free_fields.tex chapters/examples/heisenberg_eisenstein.tex chapters/theory/introduction.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{conv:heisenberg-kappa-notation}' chapters && sed -n '2160,2195p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/heisenberg_eisenstein.tex:23:\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
chapters/examples/heisenberg_eisenstein.tex:25:$\kappa(\cH_\kappa^!) = -\kappa$ \\
chapters/examples/heisenberg_eisenstein.tex:307:it has modular characteristic $\kappa(\cH_\kappa^!) = -\kappa$, giving
chapters/examples/free_fields.tex:1387:Modular characteristic $\kappa(\cH_k) = k$.
chapters/examples/free_fields.tex:2888:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/examples/free_fields.tex:4168:$\kappa(\cF)/\kappa(\cH_1) = (1/4)/1 = 1/4$.
chapters/examples/free_fields.tex:5440:$\kappa(\cH_k) = k$.
chapters/examples/free_fields.tex:5457: $\kappa(\cH_k) + \kappa(\cH_k^!) = 0$ &
chapters/examples/free_fields.tex:5461: $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
chapters/theory/introduction.tex:436:with $\kappa(\cH_k^!) = -k$.
chapters/theory/introduction.tex:450:$\kappa(\cH_k^!) = -k$, the opposite modular characteristic
chapters/theory/introduction.tex:464:The modular characteristic is $\kappa(\cH_k) = k$, and
chapters/theory/introduction.tex:465:$\kappa(\cH_k) + \kappa(\cH_k^!) = k + (-k) = 0$. The
chapters/theory/introduction.tex:493:$F_1 = \kappa(\cH_k)/24 = k/24$
chapters/theory/introduction.tex:1444:$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
chapters/theory/introduction.tex:1522:have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2168:\label{conv:heisenberg-kappa-notation}
reduces to the classical Yang--Baxter equation
$[r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0$
for~$r$.
\end{proposition}

\subsubsection{Example: Heisenberg deformation}

\begin{convention}[Heisenberg level notation]
\label{conv:heisenberg-kappa-notation}
We write $\mathcal{H}_\kappa$ for the Heisenberg vertex algebra at
level~$\kappa$, using the same letter as the modular characteristic
to emphasize the identity $\kappa(\mathcal{H}_\kappa) = \kappa$: for
the Heisenberg algebra, the level parameter coincides with the modular
characteristic (Theorem~\textup{\ref{thm:modular-characteristic}}).
\end{convention}

\begin{proposition}[Deforming Heisenberg; \ClaimStatusProvedHere]
\label{prop:deforming-heisenberg}
The Heisenberg algebra $\mathcal{H}_\kappa$ on a smooth curve~$X$ of

thinking
**Exploring theorem application**

I'm thinking about using the theorem `thm:modular-characteristic` instead of the missing property. In the y_algebras section, there's a statement about the Heisenberg current at level Ψ contributing κ = k. This might connect to the Heisenberg formula. Since the exact formula could fit into Theorem D, I plan to search for a specific theorem or proposition. I’ll also look into `kappa(\mathcal{H}_\kappa)=\kappa` in the context of free fields.
exec
/bin/zsh -lc "rg -n -F 'kappa(\\mathcal{H}_\\kappa) = \\kappa' chapters/theory/introduction.tex chapters/examples/heisenberg_eisenstein.tex chapters/examples/free_fields.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/heisenberg_eisenstein.tex:603:By Theorem~\ref{thm:genus-universality} with $\kappa(\mathcal{H}_\kappa) = \kappa$ and the Faber--Pandharipande $\lambda_g$ formula:
chapters/theory/higher_genus_foundations.tex:2171:to emphasize the identity $\kappa(\mathcal{H}_\kappa) = \kappa$: for
chapters/theory/higher_genus_foundations.tex:5344:$\kappa(\mathcal{H}_\kappa) = \kappa$,\;
chapters/theory/higher_genus_foundations.tex:5375:at $h^\vee = 0$; one defines $\kappa(\mathcal{H}_\kappa) = \kappa$ directly
exec
/bin/zsh -lc "sed -n '5318,5388p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{tabular}
\end{table}

\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a modular Koszul chiral algebra whose strong generators
all have the \emph{same} conformal weight. There exists a
genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
curvature, such that \begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
\quad \text{for all } g \geq 1,
\end{equation}
where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
\textup{(LOCAL)}
Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
For algebras with generators of \emph{several} conformal weights,
exec
/bin/zsh -lc "sed -n '1030,1065p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{Mixed operations:}
 $\SCmodmix(g, k, m)
 = C_\ast(\FM_{k|m}(\Sigma_g, \partial))$
 for $k$ closed (bulk) insertions on $\Sigma_g$ and $m$ open
 (boundary) insertions along a chosen boundary segment.

\item \emph{Directionality:}
 $\SCmod(\ldots, \mathrm{top}, \ldots; \mathrm{ch})
 = \varnothing$: no open inputs produce closed outputs.

\item \emph{Genus-$0$ reduction:}
 At $g = 0$, $\FM_k(\Sigma_0) = \FM_k(\C)$, and
 $\SCmod\big|_{g=0} = \SCchtop$
 (Definition~\ref{def:SC-operations}).
\end{enumerate}
\end{definition}

\begin{proposition}[Product decomposition of mixed operations]
\label{prop:mixed-product-decomposition}
\index{Swiss-cheese operad!mixed operations!product decomposition}
exec
/bin/zsh -lc "rg -n -F '\\delta_{\\mathrm{pf}}"'^{(2,0)} = S_3(10 S_3 - '"\\kappa)/48' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:1713:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:20116:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$:
chapters/theory/higher_genus_modular_koszul.tex:27752: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:31596:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/connections/concordance.tex:2109: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$;

thinking
**Looking into nearby theorems**

I need to check out any nearby theorems or properties related to the label around 20116. Maybe I should also inspect around the area of 20080. It sounds like there could be something of interest there, so I'll focus on gathering relevant information and ensuring I get the details right. I'll see what I can find in both locations and make sure to dig deeper into the specifics!
exec
/bin/zsh -lc "sed -n '20070,20155p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
sed -n '27720,27795p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
sed -n '31570,31620p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$1$ & $6.24$ & $1.25$ & $5.0$ & no \\
$2$ & $3.10$ & $0.48$ & $6.4$ & no \\
$6$ & $1.02$ & $0.08$ & $13$ & no \\
$13$ & $0.47$ & $0.017$ & $28$ & yes \\
$50$ (self-dual) & $0.12$ & $8\times 10^{-4}$ & $154$ & yes \\
\bottomrule
\end{tabular}
\end{center}
\noindent
The T-line dominates at all central charges:
$\rho_T/\rho_W^{\mathrm{aut}}
= (5c{+}22)\sqrt{(45c{+}218)/7680}$,
which grows as~$c^{3/2}$ for large~$c$.
The algebra-level growth rate
is $\rho(\cW_3) = \rho_T = \rho(\mathrm{Vir}_c)$
(Proposition~\ref{prop:virasoro-bottleneck}).
The same critical central charge $c_\star \approx 6.125$
governs both the Virasoro and~$\cW_3$ convergence
thresholds.
\end{remark}

thinking
**Searching for propositions**

I’m considering whether the proposition I’m looking for even exists, or if it might just be a remark or theorem instead. The lattice_foundations reference talks about a specific formula related to genus 2 planted-forest correction, but the current repository doesn’t have a prop label. I think it’s a good idea to search for the exact proposition, maybe checking concordance, while looking for the formula and any associated label as well.
exec
/bin/zsh -lc "rg -n -F 'planted-forest correction' chapters | sed -n '1,120p'
rg -n 'label\\{["'^}]*planted[''^}]*forest[''^}]*'"\\}' chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface_sections2_4_draft.tex:1112:by~$2$ and raising genus by~$1$; \emph{planted-forest corrections}
chapters/frame/guide_to_main_results.tex:112: At the ambient level (with planted-forest corrections),
chapters/examples/lattice_foundations.tex:1688:\item The planted-forest correction vanishes:
chapters/frame/preface.tex:2038:by~$2$ and raising genus by~$1$; \emph{planted-forest corrections}
chapters/frame/preface.tex:2501:quartic restricts with a planted-forest correction that is
chapters/frame/heisenberg_frame.tex:84:$d_{\mathrm{pf}} = 0$ (no planted-forest corrections).
chapters/frame/preface_sections5_9_draft.tex:317:quartic restricts with a planted-forest correction that is
chapters/examples/genus_expansions.tex:2914:planted-forest correction on the $T$-line is
chapters/examples/genus_expansions.tex:2930:\emph{Total planted-forest correction}.
chapters/examples/genus_expansions.tex:2941:The planted-forest correction is a within-channel effect from
chapters/examples/genus_expansions.tex:2956:The planted-forest correction
chapters/examples/genus_expansions.tex:2982:\index{planted-forest correction!genus-3 landscape}
chapters/examples/genus_expansions.tex:2984:At genus~$3$, the planted-forest correction
chapters/examples/genus_expansions.tex:2991:\begin{computation}[Genus-$3$ planted-forest corrections by shadow
chapters/examples/genus_expansions.tex:2993:\index{planted-forest correction!genus-3 by class}
chapters/examples/genus_expansions.tex:3000:planted-forest correction.
chapters/examples/genus_expansions.tex:3027:The planted-forest correction $\delta_{\mathrm{pf}}^{(g,0)}$ is an
chapters/examples/w_algebras.tex:185:$\Theta^{(2)}_{\mathrm{pf}}$ (planted-forest corrections from
chapters/examples/w_algebras.tex:196:planted-forest correction is the bar-side avatar of the nonlinear
chapters/examples/w_algebras.tex:199:the clutching bracket, and the planted-forest correction become
exec
/bin/zsh -lc "sed -n '24710,24745p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
sed -n '25970,25990p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
sed -n '4200,4220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}either non-separating, decreasing vertex genus by~$1$,
or separating, splitting a vertex\textup{)}.
Graph~E lies in $\overline\delta_{\mathrm{irr}} \cap
\overline\delta_1$; graph~G lies in the closure of both~D
and~E; graph~F lies only in the closure of~D.}%
\label{fig:boundary-poset-genus2}
\end{figure}

\begin{remark}[Explicit planted-forest correction]
\label{rem:planted-forest-correction-explicit}
\index{planted-forest correction!explicit formula|textbf}
\index{shadow depth!planted-forest contribution}
The planted-forest correction
in~\eqref{eq:mc-tautological-relation} is
\begin{equation}\label{eq:delta-pf-explicit}
\delta_{\mathrm{pf}}^{(g,n)}(\cA)
\;=\;
\sum_{F \in \mathrm{PF}_{g,n}}
\frac{1}{|\operatorname{Aut}(F)|}
\;\iota_{F,*}\!\Bigl(

thinking
**Reviewing reference corrections**

I think the best fix here is to replace `Proposition\ref{prop:pixton-genus2-planted-forest}` with either `equation\eqref{eq:planted-forest-genus2-explicit-bridge}` or `Remark\ref{rem:pixton-genus2-computation}` since it’s currently in parentheses after the formula. It seems I'll likely go with `equation\eqref{eq:planted-forest-genus2-explicit-bridge}`. I also need to search for a similar label, like `rem:cubic-source-caveat`, and check nearby references to ensure everything aligns correctly.
exec
/bin/zsh -lc "sed -n '1088,1116p' chapters/connections/thqg_holographic_reconstruction.tex
printf '\\n---\\n'
sed -n '1644,1665p' chapters/connections/thqg_soft_graviton_theorems.tex
printf '\\n---\\n'
sed -n '1828,1850p' chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Since $S_5 \neq 0$, the induction starts, and the
shadow recursion gives
\begin{equation}\label{eq:shadow-recursive-formula}
S_{r+1} = -\frac{6r}{c(r+1)}\,S_r,
\qquad r \geq 5.
\end{equation}
Since $6r/(c(r+1)) \neq 0$ for generic $c$ and all
$r \geq 5$, we have $S_r \neq 0$ for all $r \geq 5$
by induction.

Therefore $o_{r+1} \neq 0$ for all $r \geq 2$, and
$r_{\max}(\mathrm{Vir}_c) = \infty$.
\end{proof}

\begin{remark}[The cubic vertex as permanent source]
\label{rem:cubic-permanent-source}
\index{Virasoro algebra!cubic as permanent source}
The essential mechanism is that the cubic vertex
$\mathfrak{C} = 2x^3$ acts as a \emph{permanent source}
in the shadow obstruction tower: its bracket with any nonzero shadow
exec
/bin/zsh -lc "rg -n -F 'cubic-source approximation' chapters/connections/thqg_holographic_reconstruction.tex chapters/connections/thqg_soft_graviton_theorems.tex chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_holographic_reconstruction.tex:1320:cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1399:cubic-source approximation,
chapters/connections/thqg_holographic_reconstruction.tex:1448:degree~$10$, cubic-source approximation;
chapters/connections/thqg_holographic_reconstruction.tex:1839:\textup{(}cubic-source approximation; exact for
chapters/connections/thqg_holographic_reconstruction.tex:1872:\item For $r \geq 5$, the cubic-source approximation
chapters/connections/thqg_holographic_reconstruction.tex:2098:\textup{(}the cubic-source approximation, exact for
exec
/bin/zsh -lc "sed -n '1866,1905p' chapters/connections/thqg_holographic_reconstruction.tex
printf '\\n---\\n'
sed -n '2088,2108p' chapters/connections/thqg_holographic_reconstruction.tex
printf '\\n---\\n'
sed -n '1312,1336p' chapters/connections/thqg_holographic_reconstruction.tex
printf '\\n---\\n'
sed -n '1390,1412p' chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
For the Virasoro algebra, the shadow coefficient $S_r$
has poles at the zeros of the Shapovalov determinant
$\det S_h$ for $h \leq 2r$. Specifically:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $S_4 = 10/(c(5c+22))$ has poles at $c = 0$ and
 $c = -22/5$, from the weight-$4$ Shapovalov zeros.
\item For $r \geq 5$, the cubic-source approximation
 $S_r^{\mathrm{cub}}$ has poles at $c = 0$
 (of order $r - 3$) and $c = -22/5$ (of order~$1$).
 No new poles appear from the cubic-source recursion.
 The full recursion, which includes
 $\{\mathrm{Sh}_j, \mathrm{Sh}_k\}$ cross-terms
 for $r \geq 6$, introduces higher powers of
 $(5c+22)$ in the denominator; see
 Theorem~\textup{\ref{thm:thqg-virasoro-tower-explicit}}.
\end{enumerate}
\end{proposition}

\begin{proof}
The cubic-source recursion
exec
/bin/zsh -lc "rg -n -F 'exact for r <= 5' chapters/connections/thqg_holographic_reconstruction.tex chapters/connections/thqg_soft_graviton_theorems.tex chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F 'r \\leq 5' chapters/connections/thqg_holographic_reconstruction.tex chapters/connections/thqg_soft_graviton_theorems.tex chapters/connections/thqg_gravitational_complexity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_holographic_reconstruction.tex:1346:For $r \leq 5$ this agrees with the exact shadow
chapters/connections/thqg_holographic_reconstruction.tex:1456:For $r \leq 5$, these are the exact shadow coefficients.
chapters/connections/thqg_holographic_reconstruction.tex:1840:$r \leq 5$, see
chapters/connections/thqg_holographic_reconstruction.tex:2099:$r \leq 5$\textup{)} makes the infinite tower
exec
/bin/zsh -lc "sed -n '1338,1354p' chapters/connections/thqg_holographic_reconstruction.tex
printf '\\n---\\n'
sed -n '1448,1462p' chapters/connections/thqg_holographic_reconstruction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
S_5 &= -48/(c^2(5c+22)). \label{eq:s5}
\end{align}
For $r \geq 5$, the cubic-source closed form is
\begin{equation}\label{eq:virasoro-shadow-closed-form}
S_r^{\mathrm{cub}} =
\frac{(-1)^{r-4} \cdot 6^{r-5} \cdot 240}
{c^{r-3}(5c+22) \cdot r}.
\end{equation}
For $r \leq 5$ this agrees with the exact shadow
coefficients: $S_r^{\mathrm{cub}} = S_r$.
For $r \geq 6$, additional contributions from
$\{\mathrm{Sh}_j, \mathrm{Sh}_k\}$ bracket terms with
$j,k \geq 4$ enter the full recursion, and the exact
values differ; see
Theorem~\textup{\ref{thm:thqg-virasoro-tower-explicit}}
and~\S\textup{\ref{subsec:thqg-virasoro-tower}}.
\end{proposition}

---
degree~$10$, cubic-source approximation;
exec
/bin/zsh -lc "sed -n '4864,4880p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$W_N$ & $2N$ & I-adic & Complexity $\sim N^2$ \\
Affine Yangian & $\infty$ & Double (I + $\hbar$) & Spectral parameter \\
Bershadsky--Polyakov & 4 & I + $\sqrt{c}$-adic & Fractional exponents \\
$\mathcal{N}=2$ Super & 3 & I-adic (super) & Fermion signs \\
\hline
\end{tabular}
\end{table}

\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
The Feynman diagram interpretation of the bar-cobar complex (the identification
of bar chains with off-shell amplitudes and cobar chains with on-shell propagator
templates) is developed in Chapter~\ref{ch:feynman}.
\end{remark}

% Feynman diagram exposition (formerly ~210 lines) moved to Chapter~\ref{ch:feynman}.

% ================================================================


thinking
**Clarifying label references**

I’m looking at the label prefix `sec:` on the remark environment, which should actually be `rem:feynman_genus_g`. The user wants exact fixes for unresolved references. I could either change the label to `\label{rem:feynman_genus_g}` or update the reference to match `sec:feynman_genus_g`. Since there's one occurrence in higher_genus_foundations, I’m noting the mismatch in prefixes as a potential issue. I need to suggest renaming the label and updating the reference accurately.
thinking
**Addressing label prefixes**

I realize that using `\S` is semantically incorrect, which is great because it helps fix the prefix drift. I should look for other labels that might have the wrong prefixes too. For instance, there’s `sec:landscape-census` versus `ch:landscape-census`. The fix here would be to replace `sec:` with `ch:`, or better yet, cite it as `Chapter\ref{ch:landscape-census}`. I also need to systematically map other labels, like checking if `rem:free-field-three-theorems` corresponds to `rem:free-fields-three-pillar`.
exec
/bin/zsh -lc "rg -n -F 'three-theorem synthesis' chapters/examples/free_fields.tex chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex
printf '\\n---\\n'
rg -n 'label\\{["'^}]*three[''^}]*theorem[''^}]*'"\\}|label\\{["'^}]*three[''^}]*pillar[''^}]*'"\\}' chapters/examples/free_fields.tex chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/landscape_census.tex:3977: three-theorem synthesis
chapters/examples/landscape_census.tex:3996: three-theorem synthesis (Remark~\ref{rem:sl2-three-theorems}).
chapters/examples/landscape_census.tex:4015: three-theorem synthesis
chapters/examples/landscape_census.tex:4021: three-theorem synthesis
chapters/examples/landscape_census.tex:4028: three-theorem synthesis
chapters/examples/landscape_census.tex:4035: three-theorem synthesis

---
chapters/examples/free_fields.tex:94:\label{rem:free-fields-three-pillar}
chapters/examples/w_algebras.tex:148:\label{rem:w-three-pillar}
exec
/bin/zsh -lc "sed -n '88,108p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '142,160p' chapters/examples/w_algebras.tex
printf '\\n---\\n'
sed -n '3968,4040p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
exhibits the transition from the Gaussian to the contact/quartic
archetype within the shadow depth classification
(Table~\ref{tab:shadow-tower-census}).
\end{remark}

\begin{remark}[Three-pillar interpretation: free-field archetypes]
\label{rem:free-fields-three-pillar}
\index{free fields!three-pillar interpretation}
In the three-pillar architecture
(\S\ref{sec:concordance-three-pillars}):
(i)~free bosons produce a \emph{strict} homotopy chiral algebra
(Gaussian archetype, all secondary Borcherds operations
$j'_n = 0$ for $n \geq 3$;
Definition~\ref{def:secondary-borcherds},
cf.\ Example~\ref{ex:cech-hca-heisenberg}). The $\beta\gamma$--$bc$
pairs are non-strict: they carry $j'_3 \neq 0$ from the cubic OPE,
but the quartic contact invariant vanishes
($\mu_{\beta\gamma} = 0$,
Corollary~\ref{cor:nms-betagamma-mu-vanishing}), so the
\v{C}ech homotopy chiral algebra
exec
/bin/zsh -lc "rg -n 'spectral finiteness|label\\{["'^}]*spectral[''^}]*finiteness[''^}]*'"\\}' chapters/connections/thqg_perturbative_finiteness.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '2088,2112p' chapters/connections/thqg_perturbative_finiteness.tex
printf '\\n---\\n'
rg -n -F 'proved scalar lane' chapters/connections/thqg_perturbative_finiteness.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
\index{genus expansion!convergence}
\index{bosonic string!factorial growth}
The bosonic string partition function has
$F_g^{\mathrm{string}} \sim (2g-2)!\,\alpha'^{-g}$ (factorial growth
from the noncompactness of the $d$-dimensional target space
$\mathbb{R}^d$). On the proved scalar lane, the shadow obstruction tower genus
expansion satisfies
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ with
$\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot
\frac{|B_{2g}|}{(2g)!} \sim
\frac{2}{(2\pi)^{2g}}$, which decays exponentially. More generally, the
bar complex on compact Fulton--MacPherson spaces $\overline{C}_n(X)$
ensures genuswise finiteness without UV regularization, but the
higher-genus scalar convergence theorem is only asserted on that proved
scalar lane (Remark~\ref{rem:thqg-I-spectral-finiteness}).
\end{remark}

\subsubsection{Analytic continuation and the partition function at $\hbar > 4\pi^2$}
exec
/bin/zsh -lc "rg -n 'Exponential decay on the proved scalar lane|genus expansion converges|meromorphic continuation|scalar lane' chapters/connections/thqg_perturbative_finiteness.tex | sed -n '1,80p'
printf '\\n---\\n'
rg -n 'label\\{["'^}]*scalar[''^}]*partition[''^}]*'"\\}|label\\{["'^}]*finiteness[''^}]*'"\\}|label\\{["'^}]*convergence[''^}]*'"\\}' chapters/connections/thqg_perturbative_finiteness.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
425:On the scalar lane, genus universality identifies this
443:proved scalar lane, $F_g$ is determined exactly by the modular
494:scalar lane ($\mathrm{obs}_g = \kappa \cdot \lambda_g$, cf.\
503:On the scalar lane, the genus-$g$ free energy depends only on
512:shadows encode the additional nonlinear data beyond this scalar lane.
561:On the proved scalar lane, there are two natural generating functions
574:On the proved scalar lane, the generating function $x/(2\sin(x/2))$ is
587:\begin{theorem}[Absolute convergence of the scalar generating function on the scalar lane; \ClaimStatusProvedHere]
599:On the scalar lane, the asymptotic behavior of
632:number of Feynman diagrams. On the scalar lane, the
642:\begin{proposition}[Shadow free energies through genus $10$ on the scalar lane; \ClaimStatusProvedHere]
752:where on the scalar lane the closed form
785:\item \emph{Full partition function beyond the scalar lane.} The full degree-summed amplitude is well defined at each fixed genus. If $\cA$ is Gaussian, then the full partition function equals the scalar partition function and therefore converges for $|\hbar| < 4\pi^2$ with meromorphic continuation. No general lower bound on the full genus-sum radius is asserted here beyond the Gaussian case.
795:\emph{Part~(ii).} On the scalar lane this is
835:In string theory, genus-$g$ amplitudes are finite individually (after integration over $\overline{\mathcal{M}}_g$), but the genus expansion $\sum_g g_s^{2g-2} \mathcal{A}_g$ is asymptotic: it diverges factorially as $\mathcal{A}_g \sim (2g)! \cdot \alpha'^{-g}$. In the twisted holographic setting, the individual amplitudes are also finite (same reason: compactness of $\overline{\mathcal{M}}_g$). On the proved scalar lane the genus expansion \emph{converges}: $F_g \sim \kappa/(2\pi)^{2g}$ decays exponentially. The difference stems from the cohomological nature of the scalar shadow amplitudes: in string theory, the integrand over $\mathcal{M}_g$ is a genuine function that grows with $g$; on the scalar lane, the integrand is the fixed cohomology class $\kappa \cdot \lambda_g$ whose integral $\lambda_g^{\mathrm{FP}}$ decays.
887:$F_g^{(r)}$ is the degree-$r$ correction. On the scalar lane,
889:all $g \geq 1$ on the proved scalar lane. For arbitrary modular
905:scalar lane this equals
935:where $\det{}'_\zeta$ denotes the zeta-regularized determinant of the scalar Laplacian $\Delta_{\Sigma_g}$ on $\Sigma_g$ \textup{(}excluding the zero mode\textup{)}. On the Gaussian scalar lane one also has
1320:On the proved scalar lane \textup{(}here $\mathrm{Vir}_c$\textup{)}, the
exec
/bin/zsh -lc "rg -n 'completion programme|analytic completion programme|MC4 completion programme|label\\{["'^}]*completion[''^}]*programme[''^}]*'"\\}|label\\{["'^}]*completion[''^}]*overview[''^}]*'"\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:4428:for the MC4 completion programme
chapters/examples/w_algebras_deep.tex:4579:for the MC4 completion programme.
chapters/examples/heisenberg_eisenstein.tex:184:completion programme is explicit.
chapters/examples/yangians_foundations.tex:2575:Yangian completion programme (MC4 structural framework proved by Theorem~\ref{thm:completed-bar-cobar-strong}; the finite RTT stages lie in $\CompCl(\Fft)$). The evaluation-core comparison
chapters/frame/preface_sections10_13_draft.tex:602:\item the analytic completion programme asks when the algebraic
chapters/frame/preface.tex:4346:\item the analytic completion programme asks when the algebraic
chapters/examples/yangians_drinfeld_kohno.tex:4664:completion programme, now resolved by the strong completion-tower theorem (Theorem~\ref{thm:completed-bar-cobar-strong}), originally broke into four checks:
chapters/theory/hochschild_cohomology.tex:862:realization via the $W_\infty$ completion programme is treated in
chapters/connections/genus_complete.tex:1451:the MC4 completion programme
chapters/connections/thqg_entanglement_programme.tex:652:and the analytic completion programme.
chapters/connections/thqg_gravitational_s_duality.tex:2579:$\cA^{\mathrm{sew}}$ (via the analytic completion programme of
chapters/connections/concordance.tex:1539: (analytic completion programme)
chapters/connections/concordance.tex:5009:\label{subsec:completion-kinematics-programme}
chapters/connections/concordance.tex:5090:The platonic ideal of the completion programme is a single object
chapters/connections/concordance.tex:5163:\subsection{The analytic completion programme}
chapters/connections/concordance.tex:5164:\label{subsec:analytic-completion-programme}
chapters/connections/thqg_introduction_supplement_body.tex:1403:describes the analytic completion programme and its relation to the
chapters/connections/thqg_introduction_supplement_body.tex:1722:The analytic completion programme
chapters/connections/editorial_constitution.tex:2233:\label{subsec:analytic-completion-programme-editorial}
chapters/connections/editorial_constitution.tex:2236:\begin{conjecture}[Analytic completion programme;
exec
/bin/zsh -lc "sed -n '2038,2056p' chapters/connections/thqg_preface_supplement.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 & Chapter~\ref{chap:yangians}
 & Arnold $\Rightarrow$ CYBE \\[2pt]
Soft theorems
 & \S\ref{def:modular-shadow-connection}
 & shadow connection Ward identities \\[2pt]
Modular bootstrap
 & \S\ref{sec:genus-spectral-sequence}
 & genus spectral sequence \\[2pt]
Critical-string dichotomy
 & \S\ref{sec:completion-programme-overview}
 & transgression algebra
\end{tabular}
\end{center}

\medskip\noindent
The constructions of Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} provide the MC element, the
shadow obstruction tower, the Koszul dual, and the genus expansion. Part~\ref{part:seven-faces}
interprets these in the gravitational context. Part~\ref{part:v1-frontier} pushes
to the frontier. Volume~II descends to three dimensions.

thinking
**Searching for concepts**

I need to find the section about critical-string dichotomy and transgression algebra. My best approach is to search for labels, possibly in the thqg_introduction_supplement_body or a concordance. It sounds like there are some specific terms I’ll need to locate, so I'll make sure to delve into those sections closely and see if I can spot exactly where these concepts are discussed. Let’s get to searching!
exec
/bin/zsh -lc "rg -n -F 'transgression algebra' chapters | sed -n '1,120p'
printf '\\n---\\n'
rg -n -F 'Critical-string dichotomy' chapters | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_critical_string_dichotomy.tex:8:\index{transgression algebra|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:27:the transgression algebra $B_\Theta$ is the universal solution to the
chapters/connections/thqg_critical_string_dichotomy.tex:48:\subsection{The transgression algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:50:\index{transgression algebra!construction|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:83:\index{transgression algebra!definition|textbf}
chapters/connections/thqg_critical_string_dichotomy.tex:93:\emph{curvature}). The \emph{transgression algebra} of the pair
chapters/connections/thqg_critical_string_dichotomy.tex:127:\index{transgression algebra!kills curvature}
chapters/connections/thqg_critical_string_dichotomy.tex:187:\index{transgression algebra!module structure}
chapters/connections/thqg_critical_string_dichotomy.tex:204:\index{transgression algebra!quotient}
chapters/connections/thqg_critical_string_dichotomy.tex:225:\index{transgression algebra!bar complex specialization}
chapters/connections/thqg_critical_string_dichotomy.tex:258:\index{transgression algebra!MC element relation}
chapters/connections/thqg_critical_string_dichotomy.tex:263:The transgression algebra is the universal algebraic solution to
chapters/connections/thqg_critical_string_dichotomy.tex:291:The \emph{secondary anomaly element} of the transgression algebra
chapters/connections/thqg_critical_string_dichotomy.tex:372:The transgression algebra fits into a short exact sequence whose
chapters/connections/thqg_critical_string_dichotomy.tex:749:transgression algebra:
chapters/connections/thqg_critical_string_dichotomy.tex:807:Clifford completion to the transgression algebra at the cost of
chapters/connections/thqg_critical_string_dichotomy.tex:1048:Morita equivalent to the transgression algebra:
chapters/connections/thqg_critical_string_dichotomy.tex:1729:transgression algebra, Clifford completion, and two-regime dichotomy
chapters/connections/thqg_critical_string_dichotomy.tex:1876:\index{bialgebra!transgression algebra}
chapters/connections/thqg_critical_string_dichotomy.tex:1886:The transgression algebra $B_\Theta^{(g)}(\cA)$ carries a unique

thinking
**Checking chapter references**

I need to look at the chapter titled `thqg_critical_string_dichotomy.tex`. It would make sense to refer to its section label, which might be `sec:thqg-critical-string-dichotomy`, or I could use the chapter label instead. I'm thinking it’s important to inspect the beginning lines first to get a clearer idea of what I should include or reference from this chapter. Let's explore that!
exec
/bin/zsh -lc "sed -n '1,20p' chapters/connections/thqg_critical_string_dichotomy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Section file for Chapter: Twisted Holography and Quantum Gravity
% Result (G9): Critical String Dichotomy

\section{Critical string dichotomy}
\label{sec:thqg-critical-string-dichotomy}
\index{critical string!dichotomy|textbf}
\index{Virasoro!c=26@$c=26$ critical string}
\index{transgression algebra|textbf}
\index{Clifford completion|textbf}

The Virasoro algebra at $c = 26$ has appeared in three earlier contexts:
as the uncurved dual $\mathrm{Vir}_{26}^! \simeq \mathrm{Vir}_0$
(Proposition~\ref{prop:virasoro-c26-selfdual}),
as the endpoint of the complementarity sum
$\kappa + \kappa' = c/2 + (26-c)/2 = 13$
(Proposition~\ref{prop:vir-complementarity}),
and as the saturation point of the depth-zero resonance shadow
(Remark~\ref{rem:virasoro-resonance-model}).
These three facts coalesce into a single structural dichotomy,
controlled by a Clifford algebra built from the handle
exec
/bin/zsh -lc "rg -n 'holographic programme|three-tier r-matrix|three-tier-r-matrix|label\\{["'^}]*concordance[''^}]*three[''^}]*'"\\}|label\\{["'^}]*concordance[''^}]*holographic[''^}]*'"\\}|label\\{["'^}]*three-tier-r-matrix[''^}]*'"\\}' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/examples/y_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/y_algebras.tex:640:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
chapters/connections/concordance.tex:1194:\label{sec:concordance-three-pillars}
chapters/connections/concordance.tex:3684:\label{subsec:concordance-three-bar-complexes}
chapters/connections/concordance.tex:6455:\label{subsec:concordance-holographic-completion}
chapters/connections/concordance.tex:6564:\label{rem:c13-concordance-holographic}
chapters/connections/concordance.tex:6573:the holographic programme.
chapters/connections/concordance.tex:6732:\label{rem:concordance-g12-holographic-codes}
chapters/theory/introduction.tex:1610:\label{def:three-tier-r-matrix}
chapters/theory/introduction.tex:1699:tiers of Definition~\ref{def:three-tier-r-matrix} correspond to
chapters/theory/introduction.tex:2413: Definition~\ref{def:three-tier-r-matrix}, with $\Theta_\cA^{\Eone}$
exec
/bin/zsh -lc "sed -n '6438,6485p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{Summary}

The historical rhyme is this. Classical operadic Koszul duality
says: quadratic presentation plus bar-cobar formalism produces
homotopy theory. The theory sought here says: factorization
presentation on curves plus Verdier duality on modular
compactifications produces \emph{modular homotopy theory}. Just as
Drinfeld--Kohno related KZ monodromy to quantum groups, the theory
sought here would relate configuration-space/Deligne--Mumford
monodromy to curved chiral Koszul duality. And just as \'etale
cohomology supplied the correct ambient cohomology theory for
Frobenius and zeta functions, factorization homology on
$\operatorname{Ran}(X)$ together with Verdier duality on
$\overline{\mathcal{M}}_{g,n}$ is the correct ambient cohomology
theory for OPE, monodromy, and bar-cobar duality on curves.

\subsection{The holographic completion}
\label{subsec:concordance-holographic-completion}
\index{holographic modular Koszul datum!concordance}

exec
/bin/zsh -lc "rg -n -F '\\label{ch:landscape-census}' chapters && rg -n -F '\\label{chap:landscape-census}' chapters || true" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/landscape_census.tex:2:\label{ch:landscape-census}
chapters/theory/ordered_associative_chiral_kd.tex:11051:\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
exec
/bin/zsh -lc "sed -n '16320,16350p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathbf{L}$, $\mathbf{C}$, all three quantities vanish at
degrees $5$, $6$, $7$ because the tower terminates
earlier. For class $\mathbf{M}$, all three are nonzero
because $\Delta \neq 0$ forces $S_k \neq 0$ for all
$k \geq 4$
(Theorem~\ref{thm:single-line-dichotomy}).

The tree count at degree~$7$ for the stable-graph route is
$(2 \cdot 8 - 5)!! = 11!! = 10395$: this is the number of
trivalent trees with $8$ external legs, which are the
fully resolved genus-$0$ stable graphs contributing to the
bracket $\ell_7^{(0)}$. The agreement with the HPL
route ($C_6 = 132$ planar trees) and the Feynman transform
route ($C_7 = 429$ binary trees on $8$ leaves) is a
consequence of the universal property
(Theorem~\ref{thm:shadow-formality-identification},
Step~$3$).
\end{proof}

\begin{definition}[Shadow depth classification]
exec
/bin/zsh -lc "rg -n 'section\\{|label\\{["'^}]*sl3[''^}]*'"\\}' chapters/examples/bar_complex_tables.tex | sed -n '1,120p'
sed -n '4128,4204p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
14:\section{Heisenberg computations}
17:\subsection{Bar complex: degrees 3 and 4}
90:\subsection{Twisting morphism verification}
139:\section{Kac--Moody computations}
142:\begin{computation}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} OPE]\label{comp:sl3-ope}
176:\begin{computation}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential]\label{comp:sl3-bar}
203:\subsection{Acyclicity verification}
243:\section{$\mathcal{W}$-algebra computations}
246:\subsection{Virasoro bar complex through degree 3}
405:\subsection{\texorpdfstring{$\mathcal{W}_3$ bar complex: degree-2 computation}{W-3 bar complex: degree-2 computation}}
567:\section{\texorpdfstring{$\widehat{\mathfrak{sl}}_3$ bar complex: degree-3 Serre relations}{sl-3 bar complex: degree-3 Serre relations}}
568:\label{sec:sl3-degree3-details}
577:\label{comp:sl3-degree3-complete}
616:\begin{equation}\label{eq:sl3-deg3-cartan-root}
705:\label{prop:sl3-serre-cohomology}
750:bar complex]\label{comp:sl3-dim-table}
794:\subsection{Weight-decomposed modular rank}
798:\label{comp:sl3-modular-rank}
877:\label{comp:sl3-chiral-bracket-os}
925:\subsection{\texorpdfstring{$\widehat{\mathfrak{sl}}_3$ bar cohomology: spectral sequence approach}{sl-3 bar cohomology: spectral sequence approach}}

thinking
**Searching computation references**

I'm trying to figure out if this refers to computation `comp:sl3-bar` or to a section labeled `sec:sl3-degree3-details`. The context mentions dimensions like [1, 8, 36, 204, 1352, 9892...], which probably come from a specific computation table rather than a section. I think searching for a labeled table in the same file could help. I’ll look around lines 720-770 to see if I can find what I need.
exec
/bin/zsh -lc "sed -n '730,770p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(one for each pair of simple roots), giving a $2$-dimensional kernel
in the appropriate grading. The PBW filtration spectral sequence
(Computation~\ref{comp:km-acyclic}) identifies this $2$-dimensional
space with the cokernel of $d\colon \bar{B}^3 \to \bar{B}^2$ on the
associated graded. The computation of $d(S)$ and $d(\tilde{S})$ in
Computation~\ref{comp:sl3-degree3-complete} confirms that these
elements produce cycles in $\bar{B}^2$.

(iii): At $k = -3$ (critical level), the bar complex is uncurved ($\dfib^{\,2} = 0$ since $\kappa = 0$),
so the cycles $S$ and $\tilde{S}$ represent honest cohomology classes.
The Feigin--Frenkel theorem (Theorem~\ref{thm:critical-level-structure})
identifies $Z(\widehat{\mathfrak{sl}}_{3,-3})$ with a polynomial algebra
in two generators (degrees $2$ and $3$, corresponding to the fundamental
invariants of the Langlands dual $\mathfrak{sl}_3^\vee$). The degree-2
generator corresponds to the Casimir class in $H^2(\bar{B})$; the
degree-3 class arising from the Serre relations corresponds to the
cubic invariant.
\end{proof}

\begin{computation}[Dimension table for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3}

thinking
**Considering cohomology dimensions**

I think the user might have meant `comp:sl3-dim-table` instead of "section." The sequence [1, 8, 36, 204, 1352, 9892] represents bar cohomology dimensions. I’m wondering if there’s a computation label related to a cohomology generating function. I might need to search around 925 or directly look for `9892` to find more information. It’s interesting how these dimensions connect to the overall computations!
exec
/bin/zsh -lc "rg -n -F '9892' chapters/examples/bar_complex_tables.tex chapters/examples/yangians_computations.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:1094:conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
chapters/examples/bar_complex_tables.tex:4152:$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
exec
/bin/zsh -lc "sed -n '1084,1102p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
and mixed contractions.
\end{computation}

\begin{remark}[Koszul dual dimensions from bar cohomology]
\label{rem:sl3-koszul-dual}
\index{Koszul dual!sl3@$\mathfrak{sl}_3$}

Formal series inversion $H_A(t) \cdot H_{A^!}(-t) = 1$
(which is equivalent to Koszulness when it holds; here applied as a
consistency device to conjectured data) applied to the
conjectured bar cohomology sequence $1, 8, 36, 204, 1352, 9892, \ldots$
yields putative Koszul dual dimensions
$(A^!)_n = 1, 8, 28, 140, 392, \ldots$.
The ``chiral excess'' $(A^!)_n - \dim \Lambda^n(\mathfrak{g}^*)$ is
$0, 0, 0, 84, 322, \ldots$, measuring the departure of the chiral
Koszul dual from the classical exterior algebra. Positivity of the
Koszul dual dimensions through degree~$7$ (verified computationally)
is a necessary condition for the conjectured generating function
and a non-trivial consistency check on $H^4 = 1352$.
exec
/bin/zsh -lc "rg -n 'DR hierarchy|label\\{["'^}]*dr[''^}]*hierarchy[''^}]*'"\\}|string equation' chapters/connections/outlook.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/outlook.tex:517:D-module purity converse, CohFT string equation, Kontsevich graph
chapters/connections/outlook.tex:602:(string equation) requires the vacuum to lie in the generating
chapters/connections/outlook.tex:603:space~$V$. The rank-$1$ string equation is proved unconditionally via
chapters/connections/outlook.tex:604:the DR hierarchy (Buryak's forgetful property of DR cycles,
chapters/connections/outlook.tex:609:The modified string equation with $\psi$-class corrections from the
chapters/connections/concordance.tex:7049:Vol.~II, rank-$1$ DR string equation
chapters/connections/concordance.tex:7050: & CohFT string equation at rank $1$ & DR cycle forgetful $+$ Buryak DR/DZ \\
chapters/connections/outlook.tex:517:D-module purity converse, CohFT string equation, Kontsevich graph
chapters/connections/outlook.tex:602:(string equation) requires the vacuum to lie in the generating
chapters/connections/outlook.tex:603:space~$V$. The rank-$1$ string equation is proved unconditionally via
chapters/connections/outlook.tex:604:the DR hierarchy (Buryak's forgetful property of DR cycles,
chapters/connections/outlook.tex:609:The modified string equation with $\psi$-class corrections from the
chapters/connections/thqg_perturbative_finiteness.tex:469:The integral $\int_{\overline{\mathcal{M}}_g} \lambda_g$ is computed by localization on $\overline{\mathcal{M}}_g$ using the Mumford relation $\lambda_g = (-1)^g \kappa_{2g-2}/(2g-2)!$ and the Witten--Kontsevich theorem for intersection numbers of $\psi$-classes. The Bernoulli numbers arise through the Euler--Maclaurin formula applied to the localization integral. A detailed proof is in Faber--Pandharipande~\cite{FP03}; the formula also follows from the string equation and the topological recursion relation.
exec
/bin/zsh -lc "sed -n '592,615p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 for the physical members of class~$\mathbf{M}$) is
 the algebraic input that makes the bound non-vacuous.
\end{enumerate}
The passage from $\Delta = 0$ to $\Delta \ne 0$ is
the passage from gauge theory to gravity: the quartic
OPE pole that creates $S_4 \ne 0$ is the same pole
that forces the infinite $\Ainf$ tower and, on the
holographic side, finite scrambling.
\end{remark}

%====================================================================
% MOVEMENT I: THE A-INFINITY STRUCTURE
%====================================================================

\subsection{Movement I: the $\Ainf$ structure from the quartic pole}
\label{subsec:gravity-ainf}

\subsubsection*{The binary operation $m_2$}

The $\lambda$-bracket~\eqref{eq:gravity-input} IS the binary
exec
/bin/zsh -lc "rg -n 'open-sector factorization|factorization dg category of line operators|label\\{["'^}]*open-sector[''^}]*factorization[''^}]*'"\\}' chapters/connections/thqg_open_closed_realization.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:11274: The open-sector factorization dg-category
chapters/connections/thqg_open_closed_realization.tex:1220:The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
chapters/connections/thqg_open_closed_realization.tex:1237:$\mathcal{C}_{\mathrm{op}}$ denote the open-sector factorization
chapters/connections/thqg_open_closed_realization.tex:1220:The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
chapters/connections/thqg_open_closed_realization.tex:1237:$\mathcal{C}_{\mathrm{op}}$ denote the open-sector factorization

thinking
**Inspecting for missing labels**

I need to check around section 1215 for any missing labels. It seems there might be something important that hasn't been labeled correctly, which could lead to confusion or misinterpretation. It's essential to ensure everything is properly identified to maintain clarity. I suppose it’s just good practice to double-check these details, as skipping over them might create issues later on. So, I'll take a closer look there!
exec
/bin/zsh -lc "sed -n '1208,1246p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 consistency guarantees that such a computation, if carried out,
 \emph{must} agree; it does not construct the computation.
\end{enumerate}
\end{remark}

% -------------------------------------------------------------------
\subsection{CT-2: the modular cooperad conjecture for the open sector}
\label{subsec:thqg-ct2-cooperad-conjecture}
\index{CT-2 conjecture|textbf}
\index{modular cooperad!open sector|textbf}
% -------------------------------------------------------------------

The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
carries cocomposition maps read off from clutching on bordered
Fulton--MacPherson compactifications, and at genus~$1$ the
annulus trace recovers the open-closed identification proved in
Theorem~\ref{thm:thqg-mc-forced-consistency}. The structural question
left open by that theorem is whether these partial data assemble into
a \emph{modular cooperad} in the sense of Getzler--Kapranov
\cite{GetzlerKapranov98}, and whether the assembled structure is

thinking
**Considering audit output formats**

I think the simplest way to handle this audit output format is to follow the "file:line" structure, mentioning the specific issue and fix. For example, I can say to add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header without changing the existing reference. I also wonder if we should mention the same unresolved issue at line 1239. Additionally, I need to inspect theorem 17 `thm:bar-cobar-path-integral-heisenberg` around line 5050 to determine if it needs a label too.
exec
/bin/zsh -lc "sed -n '5038,5092p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 63ms:
$m_0 = c/24N$.
\end{example}

\begin{remark}[Scope]
Theorem~\ref{thm:genus-deformation-exact} is proved; the residual conjecture is
$\hbar = g_s = 1/N$, which requires AdS/CFT.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~IV
(trace/index). The identification $\hbar = g_s$ asserts that the
genus expansion parameter is the image of the universal deformation
object under a trace functor.
\end{remark}


\subsection{String amplitudes via bar complex}

\begin{theorem}[Bar classes on moduli and boundary factorization;
\ClaimStatusProvedHere]
\label{thm:bar-string-integrand}
\index{bar complex!moduli class}

thinking
**Locating the theorem**

I need to find the theorem, but it’s probably in another file or maybe I should create it here. I should search the current repository using the phrase about pairing the bar class with the Gaussian measure at all genera. That seems like a good keyword to start with; it might point me in the right direction for computing free boson correlation functions. Let’s see where this exploration takes me!
exec
/bin/zsh -lc "rg -n -F 'pairing the bar class with the Gaussian measure at all genera computes free boson correlation functions' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Searching for theorems**

I'm thinking I might want to search for theorems in Volume II, but I should also consider looking through all repositories. It seems like this could uncover some useful information or insights. I want to make sure I’m being thorough, so checking multiple sources is probably a good idea. Let's see what I can find! I’ll go ahead and get started on that search.
exec
/bin/zsh -lc "rg -n -F 'bar-cobar path integral' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 155ms:


thinking
**Searching for Gaussian measure**

I’m considering searching for "Gaussian measure" to find relevant theorems and information. This could lead to a better understanding of the topic. I wonder if I should also include the context or specific applications of the Gaussian measure to refine the search. Alright, let’s get some initial results and see where that leads. The more information I gather, the clearer the concepts will become for me!
exec
/bin/zsh -lc "rg -n 'Gaussian measure|free boson correlation functions|Dedekind \\\\eta-function' chapters/examples/free_fields.tex chapters/**/*.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:5072: class with the Gaussian measure at all genera computes free boson
chapters/frame/heisenberg_frame.tex:3498:the Gaussian measure on the boundary current is quadratic, and
chapters/frame/heisenberg_frame.tex:3507:graph sum against the Gaussian measure, weighted by $k$ per
chapters/examples/free_fields.tex:5072: class with the Gaussian measure at all genera computes free boson
chapters/examples/heisenberg_eisenstein.tex:1950:free rank-$1$ BV algebra with Gaussian measure. The flat connection
exec
/bin/zsh -lc "sed -n '3478,3522p' chapters/frame/heisenberg_frame.tex
printf '\\n---\\n'
rg -n 'Gaussian.*free boson|free boson|eta-function' chapters/frame/heisenberg_frame.tex chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
$\partial_{z_i}\eta_{ij}$ is a weight-$2$ object that looks like
the propagator but is in fact a different one-form
($d(-(z_i - z_j)^{-1})$, not $d\log(z_i - z_j)$). The correct
statement is~\eqref{eq:cs-hinge-propagator-forms}: the two
one-forms are distinct and serve distinct roles. The confusion
is an instance (connection one-form is $r(z)\,dz$, NOT
$r(z)\,d\log(z)$): the Arnold form is a bar-complex coefficient,
not the connection form of a flat bundle.
\end{remark}

At degree $n$, the perturbative amplitude on the disk takes the form
\begin{equation}\label{eq:cs-hinge-degree-n-amplitude}
\langle J(z_1)\cdots J(z_n)\rangle_{\mathrm{disk}}
\;=\;
\sum_{\pi \in \cP_n}\,
\prod_{\{i,j\} \in \pi}\,
\frac{k}{(z_i - z_j)^2},
\end{equation}
the sum over all perfect matchings $\pi$ of $\{1, \ldots, n\}$.
The formula is Wick's theorem: only matchings contribute because

thinking
**Evaluating theorem clarity**

I’m looking at a potential issue with an unresolved self-reference in a theorem that doesn’t seem to exist. It might help to insert a label for clarity on the current theorem. Yet, item (iii) cites another theorem, `thm:bar-cobar-path-integral-heisenberg`, which also doesn’t appear to exist. I wonder if the current theorem is intended to be it, but since it mentions item (iii) specifically, I think I need to check further for proof regarding Gaussian integrals and eta.
exec
/bin/zsh -lc "rg -n 'Gaussian integrals|Dedekind.*eta|free boson partition|Theorem\\[.*eta|Theorem\\[.*Gaussian|bar classes.*Gaussian' chapters/examples/heisenberg_eisenstein.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:381:\begin{definition}[Dedekind eta function]\label{def:eta-function}
chapters/examples/heisenberg_eisenstein.tex:382:\index{Dedekind eta function|textbf}
chapters/examples/heisenberg_eisenstein.tex:383:The Dedekind eta function is:
chapters/examples/heisenberg_eisenstein.tex:786:At genus~$1$, the Dedekind eta function appears via the operator formalism: $\mathrm{Tr}(q^{L_0 - c/24}) = 1/\eta(\tau)$ (holomorphic partition function).
chapters/examples/free_fields.tex:2395:Dedekind eta function. At $t = 1$, the series
chapters/examples/free_fields.tex:5086:direct computation using Gaussian integrals and the
chapters/examples/free_fields.tex:5087:Dedekind $\eta$-function.


thinking
**Considering theorem adjustments**

I’m thinking about potentially relabeling `thm:bar-string-integrand`, but line 5074 refers to an external theorem. Instead, I could just replace it with "by direct Gaussian computation," and I see a similar issue at line 5085. For that, I might say "the Gaussian free-boson computation of this subsection" or refer to Chapter\ref{chap:free-fields}. The user wants an exact fix, though, and relabeling the current theorem may not be the best choice since it could be circular. This is tricky!
thinking
**Exploring potential theorems**

I'm wondering if there might be another theorem that has been omitted later in the same subsection. It could be helpful to search for any missing references after line 5092. I should check whether there are gaps in the content that might need addressing, as that could clarify some of the issues I've been wrestling with. This could take a bit of time, but ensuring everything is complete is really important for the overall understanding!
exec
/bin/zsh -lc "sed -n '5092,5165p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For a general interacting chiral algebra $\cA$ at
$g \geq 1$:
\[
\mathcal{A}_{g,n}^{\mathrm{string}}(V_1, \ldots, V_n)
= \int_{\overline{\mathcal{M}}_{g,n}}
\langle \barBgeom^{(g)}_n
(V_1 \otimes \cdots \otimes V_n)
\rangle_{\mathrm{reg}}
\]
where $\langle \cdot \rangle_{\mathrm{reg}}$ denotes
Costello regularization of the string measure
$\det(\mathrm{Im}\,\Omega)^{-c/2}$.
(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
\end{conjecture}


\begin{theorem}[String amplitude factorization \cite{Pol98}; \ClaimStatusProvedElsewhere]\label{thm:amplitude-factorization}
String amplitudes satisfy the factorization property:
\[\mathcal{A}_{g,n}^{\mathrm{string}}(V_1, \ldots, V_n) = \sum_{\mathrm{partitions}} \mathcal{A}_{g_1,n_1}^{\mathrm{string}}(V_I) \times \mathcal{A}_{g_2,n_2}^{\mathrm{string}}(V_J) \times \mathrm{Propagator}\]
where the sum is over all ways of partitioning the genus and punctures.

thinking
**Editing references for clarity**

I need to fix references to nonexistent theorems. At line 5074, I could replace `\textup{(}Theorem\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}` with an appropriate remark like `by the Gaussian computation in the Heisenberg case`. For line 5085, I should change `Theorem\ref{thm:bar-cobar-path-integral-heisenberg}` to `a direct Gaussian computation in the Heisenberg case`. I also need to check line numbers and ensure cross-references exist in Vol II and Vol III—so looking at the title in Vol II around line 1715 is a good next step!
exec
/bin/zsh -lc "sed -n '1698,1738p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
simultaneously present lines.

For $\widehat{\mathfrak{sl}}_2$: the CDG line operators are
Wilson lines in 3d Chern--Simons, and $R(z)=1+k\,\Omega/z+\cdots$
is the perturbative expansion of the Chern--Simons $R$-matrix.
For Virasoro: the CDG lines are gravitational defects, and
the Laplace kernel $r^L_c(z)=\partial T/z+2T/z^2+c/(2z^4)$ has a
fourth-order pole from the conformal anomaly (the collision residue
$r^{\mathrm{coll}}_c(z) = (c/2)/z^3 + 2T/z$ has a cubic pole).
\end{remark}

\subsection{The DNP identification: meromorphic tensor product
from the ordered bar complex}
\label{subsec:dnp-identification}

\begin{theorem}[DNP line-operator package = bar-cobar twisting package;
\ClaimStatusProvedHere]
\label{thm:dnp-bar-cobar-identification}
\index{Dimofte--Niu--Py!bar-cobar identification|textbf}
\index{meromorphic tensor product!ordered bar coproduct|textbf}
exec
/bin/zsh -lc "sed -n '1404,1426p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '292,312p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
commutative chiral algebra $\mathrm{Sym}^{\mathrm{ch}}(V^*)$, not a
level-inverted Heisenberg.
 
\subsubsection{Bar complex computation}
\label{sec:heisenberg-bar-complex}
 
\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}
For $\mathcal{H}_k$ on $\mathbb{P}^1$:
\[
H^n(\bar{B}_{\text{geom}}(\mathcal{H}_k)) =
\begin{cases}
\mathbb{C} & n = 0 \\
0 & n = 1 \\
\mathbb{C} \cdot c_k & n = 2 \\
0 & n > 2
\end{cases}
\]
where $c_k$ is the central charge class. For genus $g \geq 1$, additional classes arise from $H^1(\Sigma_g)$; see Theorem~\ref{thm:heisenberg-higher-genus}.
\end{theorem}
 
exec
/bin/zsh -lc "rg -n 'hook-type.*transport.*Koszul|hook-type.*duality|label\\{["'^}]*hook[''^}]*transport[''^}]*'"\\}|label\\{["'^}]*hook[''^}]*koszul[''^}]*'"\\}' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex:930:\begin{equation}\label{eq:hook-koszul-duality}
chapters/examples/w_algebras.tex:523:Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
chapters/examples/w_algebras.tex:7172:\label{rem:hook-transport-corridor-shadow}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:963: the dual level determined by the hook-type duality.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1803:The hook-type Koszul duality
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2274:\index{W-algebra@$\mathcal{W}$-algebra!hook-type duality}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2275:For hook-type nilpotents in type $A$, the Koszul duality of
chapters/connections/outlook.tex:276: (Theorem~\ref{thm:hook-type-transport-koszul-duality}).
chapters/connections/concordance.tex:3384: hook-type duality statement is kept conditional on hook-wide
chapters/connections/subregular_hook_frontier.tex:191:full hook-type duality is proved by convolution; inverse reductions exist
chapters/connections/subregular_hook_frontier.tex:229:\label{thm:hook-transport-corridor}
chapters/connections/subregular_hook_frontier.tex:1005:\index{hook-type duality!self-transpose}
chapters/connections/subregular_hook_frontier.tex:1009:self-dual under the hook-type transport duality. The hook partition
chapters/connections/subregular_hook_frontier.tex:1038:The hook-type transport duality of \cite{FehilyHook} and
chapters/theory/koszul_pair_structure.tex:1218:mechanism, but the manuscript keeps the full hook-type duality
chapters/connections/frontier_modular_holography_platonic.tex:3912:Full hook-type duality is proved; inverse reductions connect all
exec
/bin/zsh -lc "sed -n '210,248p' chapters/connections/subregular_hook_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The first axis is now substantially theorematic in type~$A$ via
the hook-type corridor; the second remains the true frontier.
\end{principle}

\begin{definition}[Reduction graph]
\label{def:reduction-graph}
\index{reduction graph!$\Gamma_N$}
Let $\Gamma_N$ be the graph whose vertices are the partitions
$\lambda \vdash N$ (indexing nilpotent orbits in
$\mathfrak{sl}_N$), and whose edges are the proved
reduction or inverse-reduction functors between the corresponding
type-$A$ affine $\mathcal{W}$-algebras at generic level.
The \emph{hook vertices} are the partitions of hook type
$(N-r, 1^r)$, $0 \leq r \leq N-1$.
The \emph{transport-closure} of a set $S$ of vertices is the set
of all vertices reachable from $S$ by paths in $\Gamma_N$.
\end{definition}

\begin{theorem}[Hook-type transport corridor under DS--bar compatibility; \ClaimStatusConditional]
\label{thm:hook-transport-corridor}
exec
/bin/zsh -lc "rg -n 'line-operator category.*module category|open-colour module category|cA\\"'^!'"\\\\text\\{-\\\\mathsf\\{mod\\}|label\\{["'^}]*line[''^}]*module[''^}]*'"\\}|label\\{["'^}]*lines[''^}]*modules[''^}]*'"\\}' chapters/connections chapters/theory chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_gravitational_yangian.tex:2024:open-colour module category $\cC \simeq \cA^!\text{-}\mathsf{mod}$
chapters/connections/thqg_gravitational_yangian.tex:2038:\emph{line-operator category} is the module category
chapters/connections/semistrict_modular_higher_spin_w3.tex:742:\label{conj:line-operators-semistrict-modules}
chapters/connections/thqg_introduction_supplement.tex:112:The \emph{line-operator category} is the derived module category

thinking
**Inspecting theorem references**

I'm considering the possibility that there may be no local theorem. It seems the claims in Volume I could be referencing those from Volume II. I need a precise fix, probably by replacing the theorem reference with a direct cross-volume citation or the current local definition. I'm noticing that `thqg_introduction_supplement.tex:112` has no theorem. The user needs this exact content, so I'll search for the theorem in Volume II to cross-check the title.
exec
/bin/zsh -lc "sed -n '350,380p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{itemize}
\item Objects: Line operators $\ell_1, \ell_2, \ldots$ labeled by representations or charges;
\item Morphisms: $\Hom(\ell_1, \ell_2) = $ quantum mechanics of fields stretching between lines $\ell_1$ and $\ell_2$ (topological quantum mechanics in the $t$-direction).
\end{itemize}
\end{definition}

The category $\mathcal{C}_{\text{line}}$ is a \textbf{monoidal category} with tensor product given by:
\begin{equation}
\ell_1 \otimes \ell_2 := \text{(place lines $\ell_1$ and $\ell_2$ parallel in $\C_z$)}.
\end{equation}

\begin{theorem}[Lines as Modules for the Open-Colour Dual;
\ClaimStatusProvedHere]
\label{thm:lines_as_modules}
Let\/ $\cA$ be a chirally Koszul logarithmic $\SCchtop$-algebra
\textup{(}Definition~\textup{\ref{def:log-SC-algebra})}, that is,
$\cA$ satisfies the concentration condition
$H^{p,q}(\barB(\cA))=0$ for $q\neq 0$; see
Definition~\textup{\ref{def:chiral-koszul-geometric}} for the precise
statement. Let\/ $\cA^!_{\mathrm{line}}$ denote the open-colour
exec
/bin/zsh -lc "rg -n 'RTT.*all types|all-types RTT|label\\{["'^}]*rtt[''^}]*types[''^}]*'"\\}|label\\{["'^}]*all-types[''^}]*'"\\}' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:1138:\label{prop:w3-m4-all-types}
chapters/examples/yangians_foundations.tex:209:\label{thm:rtt-all-classical-types}
chapters/examples/yangians_foundations.tex:270:\begin{equation}\label{eq:ybe-all-types}
chapters/examples/yangians_foundations.tex:1044:\label{thm:all-types-yangian-structure}
chapters/examples/yangians_foundations.tex:1052: \begin{equation}\label{eq:r-matrix-all-types}
chapters/examples/yangians_computations.tex:1149:from the all-types RTT presentation
chapters/examples/yangians_computations.tex:1536:\label{cor:dk2-thick-generation-all-types}%
chapters/examples/yangians_computations.tex:2207:\label{comp:current-algebra-E1-all-types}
chapters/examples/yangians_computations.tex:2635:\ClaimStatusConjectured]\label{conj:mc3-sectorwise-all-types}
chapters/examples/yangians_computations.tex:3985:\label{thm:categorical-cg-all-types}%
chapters/examples/yangians_computations.tex:4131:\label{cor:mc3-all-types}%
chapters/examples/yangians_computations.tex:4216:\label{rem:mc3-cg-all-types-resolved}
chapters/examples/yangians_computations.tex:4286:\label{prop:character-cg-all-types}
chapters/examples/yangians_drinfeld_kohno.tex:878:\label{cor:dk23-all-types}
chapters/examples/yangians_drinfeld_kohno.tex:883:\begin{equation}\label{eq:dk23-all-types}
chapters/connections/thqg_gravitational_s_duality.tex:1620:\label{comp:koszul-conductor-all-types}

thinking
**Inspecting theorem titles**

I need to take a closer look at the titles of certain theorems. This feels important for ensuring I have a solid understanding of what each one entails. I wonder if there are any common themes or patterns in the titles that might point to their significance or applications. It might help to write down my observations to keep track of what stands out. Let's see what I can discover from this inspection!
exec
/bin/zsh -lc "sed -n '190,225p' chapters/examples/yangians_foundations.tex
printf '\\n---\\n'
sed -n '1036,1065p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Expanding in modes
$T_{ij}(u) = \delta_{ij} + \hbar \sum_{r \geq 0} T_{ij}^{(r)} u^{-r-1}$,
the RTT relation \eqref{eq:rtt-relation} is equivalent to:
\begin{equation}\label{eq:rtt-modes}
[T_{ij}^{(r+1)}, T_{kl}^{(s)}]
- [T_{ij}^{(r)}, T_{kl}^{(s+1)}]
\;=\; T_{kj}^{(r)} T_{il}^{(s)}
- T_{kj}^{(s)} T_{il}^{(r)}.
\end{equation}
The RTT relation is \emph{quadratic} in the entries of $T$, making
this presentation directly amenable to quadratic Koszul duality
(mechanism~(iii) of Remark~\ref{rem:three-koszul-mechanisms}).
The isomorphism with the Drinfeld presentation
(Definition~\ref{def:yangian}) is given by
$J_a^{(0)} = \sum_{i,j} \rho(e_a)_{ij}\, T_{ij}^{(0)}$
and higher modes from the coproduct structure.
\end{definition}

\begin{theorem}[RTT R-matrices for all classical types; \ClaimStatusProvedHere]
\label{thm:rtt-all-classical-types}
exec
/bin/zsh -lc "sed -n '225,285p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 The corresponding Casimir is $\Omega = P - \mathbb{1}/N$
 with $N = n+1$, so in the KZ normalisation the classical $r$-matrix at affine
 level $k$ reads
 $r(z) = \Omega/\bigl((k + h^\vee)\,z\bigr) = (P - \mathbb{1}/N)/\bigl((k + n + 1)\,z\bigr)$
 (Remark~\ref{rem:km-collision-residue-rmatrix}).
 At the critical level $k = -h^\vee$ the denominator vanishes,
 tracking the Sugawara singularity.

\item \emph{Type $B_n$ $(\mathfrak{so}_{2n+1}$, $V = \bC^{2n+1})$.}
 The $R$-matrix is%
 \footnote{The pole position of the $R$-matrix in types $B$, $C$, $D$
 is denoted~$\varkappa$ (following Molev~\cite{molev-yangians}) to
 avoid conflation with the modular characteristic~$\kappa(\cA)$
 of Theorem~\textup{\ref{thm:modular-characteristic}};
 these are unrelated quantities.}
 \begin{equation}\label{eq:rmatrix-type-b}
 R(u) = \mathbb{1} - \frac{P}{u} + \frac{Q}{u - \varkappa},
 \qquad \varkappa = n - \tfrac{1}{2},
 \end{equation}
 where $Q_{(ij),(kl)} = \delta_{ij}\delta_{kl}$ is the trace




thinking
**Organizing reference findings**

I’m considering how to address comments and occurrences of references like `\eqref`, `\autoref`, and others, but the user is focused on `\ref`. I think I might need to identify 28 unique names with 39 occurrences. To manage duplicates, I wonder if I can compress findings from the same label. The format says to provide a bullet for each finding, so I'll aim for 39 bullets and summaries that total around 42 lines, focusing on brevity. I also need exact line numbers, possibly using previous outputs.
thinking
**Gathering reference details**

I need to collect line numbers along with relative file paths, but they shouldn’t be clickable—just plain text. It’s important to verify each candidate's existing label and the external context, since some will require specific fixes. I think I should gather exact labels and titles for cross-volume items and their local equivalents. I could map everything systematically in my notes. Maybe I can utilize another script to generate labels along with similar hits, but I’ll need to think it through.
thinking
**Clarifying section reference**

It seems I need to correct the section title. The correct title is "Critical-string dichotomy," not "completion programme." So, the exact fix should be changing it to `\S\ref{sec:thqg-critical-string-dichotomy}` instead of the analytic completion programme. It's important to get these references right for clarity, and I can definitely see how this mix-up could lead to confusion! I'll make sure to fix that.
thinking
**Looking into cross-volume search**

I'm considering whether there's a label in Volume II that we haven't searched yet. It seems like we might be missing something important by not looking there. It sounds like a good idea to search through that volume just in case we find something valuable. I want to ensure I’m thorough in my approach, so let’s explore that option!
exec
/bin/zsh -lc "rg -n -F '\\label{subsec:dr-hierarchy-string}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups || true" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

codex
The remaining work is verification, not discovery. I have a candidate fix for each live broken reference; now I’m checking that every replacement label actually exists and that I’m not introducing a second failure by pointing to the wrong theorem/status surface.
exec
/bin/zsh -lc "for lbl in sec:shadow-metric def:shadow-depth-classification thm:genus-universality eq:planted-forest-genus2-explicit-bridge prop:virasoro-shadow-coefficients rem:free-fields-three-pillar rem:w-three-pillar sec:thqg-critical-string-dichotomy subsec:concordance-holographic-completion def:three-tier-r-matrix ch:landscape-census rem:sl3-koszul-dual thm:thqg-I-absolute-convergence thm:heisenberg-bar thm:hook-transport-corridor thm:rtt-all-classical-types; do
  printf '=== %s ===\\n' \""'$lbl"
  rg -n -F "'"\\\\label{"'$lbl}" chapters || true
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 134ms:
chapters/connections/concordance.tex:6455:\label{subsec:concordance-holographic-completion}

=== def:three-tier-r-matrix ===
chapters/theory/introduction.tex:1610:\label{def:three-tier-r-matrix}

=== ch:landscape-census ===
chapters/examples/landscape_census.tex:2:\label{ch:landscape-census}
chapters/theory/ordered_associative_chiral_kd.tex:11051:\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone

=== rem:sl3-koszul-dual ===
chapters/examples/bar_complex_tables.tex:1088:\label{rem:sl3-koszul-dual}

=== thm:thqg-I-absolute-convergence ===
chapters/connections/thqg_perturbative_finiteness.tex:588:\label{thm:thqg-I-absolute-convergence}

=== thm:heisenberg-bar ===
chapters/examples/free_fields.tex:1410:\begin{theorem}[Heisenberg bar complex at genus 0; \ClaimStatusProvedHere]\label{thm:heisenberg-bar}

=== thm:hook-transport-corridor ===
chapters/connections/subregular_hook_frontier.tex:229:\label{thm:hook-transport-corridor}



thinking
**Ensuring structured findings**

I need to ensure that there aren’t other comment-only occurrences that might create confusion. I could check if a line begins with “%” to help with this. I have 38 findings so far but should probably count how many have been checked, which is 39. My structured summary will likely need to reflect the findings that are still relevant, making sure everything is clear. Let's ensure it’s organized properly!
thinking
**Counting findings and references**

I’m noting that there are 39 references checked, with 38 leading to a verdict of "FAIL." However, the user might be saying that every unresolved reference counts as a finding, while the commented references don’t. So, it seems like there are 38 findings. I might need to consider mentioning a discarded false positive due to a commented-out reference. Should I include that comment-only references are excluded in the summary, or just list the findings? Let's tally duplicates to clarify.
thinking
**Updating statuses**

I need to focus on updating plan statuses. This task seems straightforward, but I want to ensure I'm tracking everything accurately. I want to consider what statuses need to be updated and make sure nothing gets overlooked. Should I maintain a list or keep it in a document? It’s important that I stay organized and that my updates reflect any changes accurately. I'll get started and make sure it’s done properly!
Plan update
All live unresolved `\ref{}` occurrences have been checked in context. I’m now collapsing them into the final verified findings list, excluding the one comment-only false positive.
  ✓ Generate the candidate unresolved `\ref{}` list from `chapters/` and count the surface
  ✓ Locate every occurrence with file:line context and search for matching labels across the repo
  ✓ Read the surrounding text for each verified miss and determine the exact fix
  → Re-verify the final findings list against live file contents and summarize counts/verdict
exec
/bin/zsh -lc "sed -n '688,698p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The strength of the obstruction is proportional to~$\kappa$:
at $\kappa = 0$ \textup{(}the uncurved case\textup{)}, $F_1 = 0$
and both the genus-$0$ and genus-$1$ obstructions survive through
the $\mathrm{GRT}_1$-torsor, but the quasi-modular channel closes.
For Heisenberg $\cH_\kappa$ at $\kappa \neq 0$
\textup{(}$\kappa(\cH_\kappa) = \kappa$, landscape
census~\S\textup{\ref{sec:landscape-census})}, all four
obstructions are simultaneously active.
\end{remark}

\begin{conjecture}[$E_1$ non-splitting at genus~$2$: seven stable-graph
exec
/bin/zsh -lc "sed -n '20676,20684p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 69ms:
The $\kappa$-conductor $\kappa(\cA) + \kappa(\cA^!)$ measures the
obstruction to extending complementarity
\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}
from genus~$0$ to higher genus without correction: the
cross-channel correction $\delta F_g^{\mathrm{cross}}$
\textup{(all-weight)} of
Theorem~\textup{\ref{thm:multi-generator-universality}} is
controlled by $\kappa + \kappa'$ and vanishes identically when
$\kappa + \kappa' = 0$. The full census of $\kappa$-conductor
exec
/bin/zsh -lc "sed -n '20684,20688p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa + \kappa' = 0$. The full census of $\kappa$-conductor
values appears in~\S\textup{\ref{sec:landscape-census}}.
\end{proposition}

\begin{proof}


thinking
**Reviewing text citations**

I’m noticing that there’s no label anywhere, which is okay for text citations. I think I should also point out that `sec:concordance-holographic-programme` actually needs to be changed to `subsec:concordance-holographic-completion`, not `section`. 

Additionally, I realize that the `thm:dnp-bar-cobar-identification` refers to an external theorem found in Vol II and Vol III, and since the current build lacks external cross-referencing, it’s a minimal fix to address that with the text. I might mention fixing line 1347 by replacing it with "the Volume II theorem..." and making similar adjustments for lines 2472 and 257.
thinking
**Verifying theorems and counts**

I’m realizing I need to exclude lines 5074 and 5085 since they reference a nonexistent theorem. Maybe one is a statement and the other a proof, so I should clarify that there are no unresolved issues in the comments. I could run a final re-verification script to ensure there are exactly 38 occurrences. I might use a command with `grep` to count lines, excluding comments. Let's conduct that check now.
exec
/bin/zsh -lc "{
  rg -n -F '\\ref{chap:modular-koszul}' chapters
  rg -n -F '\\ref{def:glcm-classification}' chapters
  rg -n -F '\\ref{part:e1-core}' chapters
  rg -n -F '\\ref{part:gravity}' chapters
  rg -n -F '\\ref{prop:heisenberg-kappa}' chapters
  rg -n -F '\\ref{prop:mixed-product-decomposition}' chapters
  rg -n -F '\\ref{prop:pixton-genus2-planted-forest}' chapters
  rg -n -F '\\ref{rem:cubic-source-caveat}' chapters
  rg -n -F '\\ref{rem:feynman_genus_g}' chapters
  rg -n -F '\\ref{rem:free-field-three-theorems}' chapters
  rg -n -F '\\ref{rem:thqg-I-spectral-finiteness}' chapters
  rg -n -F '\\ref{rem:w-algebra-three-theorems}' chapters
  rg -n -F '\\ref{sec:completion-programme-overview}' chapters
  rg -n -F '\\ref{sec:concordance-holographic-programme}' chapters
  rg -n -F '\\ref{sec:concordance-three-tier-r-matrix}' chapters
  rg -n -F '\\ref{sec:landscape-census}' chapters
  rg -n -F '\\ref{sec:shadow-depth-classification}' chapters
  rg -n -F '\\ref{sec:sl3-bar-table}' chapters
  rg -n -F '\\ref{subsec:dr-hierarchy-string}' chapters
  rg -n -F '\\ref{subsec:gravity-ainf}' chapters
  rg -n -F '\\ref{subsec:thqg-open-sector-factorization-category}' chapters
  rg -n -F '\\ref{thm:bar-cobar-path-integral-heisenberg}' chapters
  rg -n -F '\\ref{thm:dnp-bar-cobar-identification}' chapters
  rg -n -F '\\ref{thm:heisenberg-bar-complex-genus0}' chapters
  rg -n -F '\\ref{thm:hook-type-transport-koszul-duality}' chapters
  rg -n -F '\\ref{thm:lines_as_modules}' chapters
  rg -n -F '\\ref{thm:rtt-all-types}' chapters
} | tee /tmp/live_unresolved_occurrences.txt | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 370ms:
      38





thinking
**Considering output format**

I need to decide whether to include a summary referencing checked occurrences 38 or 39 since I have unresolved findings for 38. It could be helpful to state the checked statuses and verdict clearly, like "Checked: 38 | Findings: 38 | Verdict: FAIL." I should mention discarding one false positive for clarity, although a structured summary might not be strictly necessary. I can format the summary with simple bullet points, ensuring no nested bullets and using plain text paths as the user requested.
thinking
**Formatting bullet points**

I need to keep each bullet point short and precise. For example, I can say, "[HIGH] chapters/theory/ordered_associative_chiral_kd.tex:5974 — PROBLEM: \ref{part:gravity} points to Volume II, but there's no `xr` or `externaldocument` bridge here, so the reference can't resolve. FIX: replace `Part\ref{part:gravity}` with `Part ``Three-Dimensional Quantum Gravity'' of Volume II.`"

I should also mention exact external theorem titles in my fixes, ensuring that quotes are consistent, either plain double quotes or TeX quotes, since the final output should be plain text.
thinking
**Considering potential fixes**

I’m looking into a fix involving the nonexistent reference, and it seems like the `heisenberg_eisenstein` fix might be an option. Alternatively, there’s the `thm:heisenberg-bar` possibility that could work. It feels promising! I also think it’s critical to change both the label and wording related to `hook-type`. This seems essential to ensure clarity and accuracy. Overall, I’m feeling optimistic about these potential adjustments!
thinking
**Evaluating local labels**

I’m thinking there might be around 15 issues to count. For the MEDIUM category, it looks like all the local labels are stale. As for the LOW category, maybe none apply. However, there could be one HIGH issue related to a specific section in the summary table that’s incorrectly placed. Overall, it seems I need to double-check the local section for a more accurate overview.
thinking
**Organizing findings**

I'm thinking about how to structure my findings. I could use backticks around labels and replacements, like `FIX: replace \`Remark\ref{rem:free-field-three-theorems}\` with \`Remark\ref{rem:free-fields-three-pillar}\``. It seems I also need to include the path and line, ensuring I follow the output contract that specifies using relative paths rather than labels. I should mention that I checked 38, possibly stating: `Checked: 38 | Findings: 38 | Verdict: FAIL`. Let's keep one bullet per finding and ensure to start with bullets since the user wanted findings only. I’ll organize them correctly!
codex
- [CRITICAL] chapters/connections/outlook.tex:276 — PROBLEM: `\ref{thm:hook-type-transport-koszul-duality}` has no target, and the live local theorem is only the conditional `\label{thm:hook-transport-corridor}`. FIX: replace `Theorem~\ref{thm:hook-type-transport-koszul-duality}` with `Theorem~\ref{thm:hook-transport-corridor}` and rewrite `is the proved corridor` to `is the conditional corridor under DS--bar compatibility`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:5974 — PROBLEM: `\ref{part:gravity}` points into Volume II; this repo has no cross-volume `xr` bridge, so the Part reference cannot resolve here. FIX: replace `Part~\ref{part:gravity}` with `Part "Three-Dimensional Quantum Gravity" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7549 — PROBLEM: `\ref{part:e1-core}` points into Volume II and cannot resolve in this build. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/theory/ordered_associative_chiral_kd.tex:7752 — PROBLEM: same broken cross-volume `\ref{part:e1-core}` as above. FIX: replace `Part~\ref{part:e1-core}` with `Part "The $E_1$ Core" of Volume II`.
- [HIGH] chapters/connections/thqg_open_closed_realization.tex:507 — PROBLEM: `\ref{prop:mixed-product-decomposition}` points only to a Volume II proposition, so the local build has no target. FIX: replace `Proposition~\ref{prop:mixed-product-decomposition}` with `the Volume II proposition "Product decomposition of mixed operations"`.
- [HIGH] chapters/connections/thqg_gravitational_s_duality.tex:559 — PROBLEM: `\ref{subsec:gravity-ainf}` points only to a Volume II subsection. FIX: replace `\S\ref{subsec:gravity-ainf}` with `the Volume II subsection "Movement I: the $\Ainf$ structure from the quartic pole"`.
- [HIGH] chapters/examples/free_fields.tex:5074 — PROBLEM: `\ref{thm:bar-cobar-path-integral-heisenberg}` has no target anywhere, so the theorem statement cites nonexistent support for item (iii). FIX: replace the parenthetical with `by direct Gaussian evaluation in the Heisenberg case`.
- [HIGH] chapters/examples/free_fields.tex:5085 — PROBLEM: the proof again cites nonexistent `thm:bar-cobar-path-integral-heisenberg`. FIX: replace `Theorem~\ref{thm:bar-cobar-path-integral-heisenberg}` with `a direct Gaussian computation in the Heisenberg case`.
- [HIGH] chapters/examples/yangians_foundations.tex:1347 — PROBLEM: `\ref{thm:dnp-bar-cobar-identification}` points only to Volume II/III, so the local theorem citation is unresolved. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package"`.
- [HIGH] chapters/theory/chiral_koszul_pairs.tex:2472 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}` in a load-bearing classification sentence. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/theory/three_invariants.tex:257 — PROBLEM: same broken external `\ref{thm:dnp-bar-cobar-identification}`. FIX: replace it with `the Volume II theorem "DNP line-operator package = bar-cobar twisting package", part (iii)`.
- [HIGH] chapters/connections/twisted_holography_quantum_gravity.tex:183 — PROBLEM: `\ref{thm:lines_as_modules}` points only to Volume II, so the local proof chain breaks. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2025 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in live prose. FIX: replace it with `the Volume II theorem "Lines as Modules for the Open-Colour Dual"`.
- [HIGH] chapters/connections/thqg_gravitational_yangian.tex:2253 — PROBLEM: same broken external `\ref{thm:lines_as_modules}` in a status table. FIX: replace `Proved (Thm~\ref{thm:lines_as_modules})` with `Proved in Volume II ("Lines as Modules for the Open-Colour Dual")`.
- [MEDIUM] chapters/theory/derived_langlands.tex:1515 — PROBLEM: `\ref{chap:modular-koszul}` has no target; the cited shadow-connection theorem lives in the shadow-metric section. FIX: replace `Chapter~\ref{chap:modular-koszul}` with `Section~\ref{sec:shadow-metric}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:27063 — PROBLEM: `\ref{def:glcm-classification}` has no target; the live definition is `\label{def:shadow-depth-classification}`. FIX: replace `Definition~\ref{def:glcm-classification}` with `Definition~\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/examples/y_algebras.tex:340 — PROBLEM: `\ref{prop:heisenberg-kappa}` has no target; the explicit Heisenberg formula is already proved in `thm:genus-universality` part (i). FIX: replace `Proposition~\ref{prop:heisenberg-kappa}` with `Theorem~\ref{thm:genus-universality}(i)`.
- [MEDIUM] chapters/examples/lattice_foundations.tex:1714 — PROBLEM: `\ref{prop:pixton-genus2-planted-forest}` has no target; the exact formula cited is the displayed equation `\label{eq:planted-forest-genus2-explicit-bridge}`. FIX: replace `Proposition~\ref{prop:pixton-genus2-planted-forest}` with `equation~\eqref{eq:planted-forest-genus2-explicit-bridge}`.
- [MEDIUM] chapters/connections/thqg_holographic_reconstruction.tex:1841 — PROBLEM: `\ref{rem:cubic-source-caveat}` has no target; the actual caveat appears in `prop:virasoro-shadow-coefficients`. FIX: replace `Remark~\ref{rem:cubic-source-caveat}` with `Proposition~\ref{prop:virasoro-shadow-coefficients}`.
- [MEDIUM] chapters/theory/higher_genus_foundations.tex:4777 — PROBLEM: `\ref{rem:feynman_genus_g}` is unresolved because the target remark is mislabeled as `\label{sec:feynman_genus_g}` in `chapters/theory/chiral_koszul_pairs.tex:4872`. FIX: rename that target label to `\label{rem:feynman_genus_g}` and cite it here as `Remark~\ref{rem:feynman_genus_g}`.
- [MEDIUM] chapters/examples/landscape_census.tex:1465 — PROBLEM: `\ref{rem:free-field-three-theorems}` has no target; the actual free-field synthesis remark is `\label{rem:free-fields-three-pillar}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
- [MEDIUM] chapters/examples/landscape_census.tex:3978 — PROBLEM: same broken `\ref{rem:free-field-three-theorems}`. FIX: replace it with `Remark~\ref{rem:free-fields-three-pillar}`.
- [MEDIUM] chapters/connections/thqg_perturbative_finiteness.tex:2104 — PROBLEM: `\ref{rem:thqg-I-spectral-finiteness}` has no target; the proved scalar convergence theorem is `\label{thm:thqg-I-absolute-convergence}`. FIX: replace it with `Theorem~\ref{thm:thqg-I-absolute-convergence}`.
- [MEDIUM] chapters/examples/landscape_census.tex:1467 — PROBLEM: `\ref{rem:w-algebra-three-theorems}` has no target; the live W-algebra synthesis remark is `\label{rem:w-three-pillar}`. FIX: replace it with `Remark~\ref{rem:w-three-pillar}`.
- [MEDIUM] chapters/examples/landscape_census.tex:4016 — PROBLEM: same broken `\ref{rem:w-algebra-three-theorems}`. FIX: replace it with `Remark~\ref{rem:w-three-pillar}`.
- [MEDIUM] chapters/connections/thqg_preface_supplement.tex:2047 — PROBLEM: `\ref{sec:completion-programme-overview}` has no target and points readers away from the actual chapter named in the row. FIX: replace `\S\ref{sec:completion-programme-overview}` with `\S\ref{sec:thqg-critical-string-dichotomy}`.
- [MEDIUM] chapters/examples/y_algebras.tex:855 — PROBLEM: `\ref{sec:concordance-holographic-programme}` has no target; the live concordance subsection is `\label{subsec:concordance-holographic-completion}`. FIX: replace it with `\S\ref{subsec:concordance-holographic-completion}`.
- [MEDIUM] chapters/examples/y_algebras.tex:640 — PROBLEM: `\ref{sec:concordance-three-tier-r-matrix}` has no target; the classification is given by `\label{def:three-tier-r-matrix}`. FIX: replace `\S\ref{sec:concordance-three-tier-r-matrix}` with `Definition~\ref{def:three-tier-r-matrix}`.
- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:20681 — PROBLEM: `\ref{sec:landscape-census}` has no target; the live label is the chapter label `\label{ch:landscape-census}`. FIX: replace `\S\ref{sec:landscape-census}` with `Chapter~\ref{ch:landscape-census}`.
- [MEDIUM] chapters/theory/e1_modular_koszul.tex:694 — PROBLEM: same stale `\ref{sec:landscape-census}` and the surrounding parenthesis is already chapter-level prose. FIX: replace `census~\S\ref{sec:landscape-census}` with `Chapter~\ref{ch:landscape-census}`.
- [MEDIUM] chapters/connections/holomorphic_topological.tex:653 — PROBLEM: `\ref{sec:shadow-depth-classification}` has no target; the live object is the definition `\label{def:shadow-depth-classification}`. FIX: replace `\S\ref{sec:shadow-depth-classification}` with `Definition~\ref{def:shadow-depth-classification}`.
- [MEDIUM] chapters/examples/bar_complex_tables.tex:4153 — PROBLEM: `\ref{sec:sl3-bar-table}` has no target; the stated `1,8,36,204,1352,9892,\ldots` sequence is actually recorded in `\label{rem:sl3-koszul-dual}`. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
- [MEDIUM] chapters/examples/bar_complex_tables.tex:4198 — PROBLEM: same broken `\ref{sec:sl3-bar-table}` in the table caption. FIX: replace `Section~\ref{sec:sl3-bar-table}` with `Remark~\ref{rem:sl3-koszul-dual}`.
- [MEDIUM] chapters/connections/outlook.tex:605 — PROBLEM: `\ref{subsec:dr-hierarchy-string}` has no target anywhere in the repo tree. FIX: replace `Section~\ref{subsec:dr-hierarchy-string}` with `Buryak's DR-hierarchy string-equation argument`.
- [MEDIUM] chapters/connections/thqg_open_closed_realization.tex:1239 — PROBLEM: `\ref{subsec:thqg-open-sector-factorization-category}` has no target; the subsection header only has `\label{subsec:thqg-ct2-cooperad-conjecture}`. FIX: add `\label{subsec:thqg-open-sector-factorization-category}` to the subsection header at line 1214.
- [MEDIUM] chapters/examples/heisenberg_eisenstein.tex:306 — PROBLEM: `\ref{thm:heisenberg-bar-complex-genus0}` has no target; the live theorem is `\label{thm:heisenberg-bar}`. FIX: replace it with `Theorem~\ref{thm:heisenberg-bar}`.
- [MEDIUM] chapters/examples/yangians_computations.tex:1150 — PROBLEM: `\ref{thm:rtt-all-types}` has no target; the live theorem is `\label{thm:rtt-all-classical-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}`.
- [MEDIUM] chapters/examples/yangians_foundations.tex:1228 — PROBLEM: same stale `\ref{thm:rtt-all-types}`. FIX: replace it with `Theorem~\ref{thm:rtt-all-classical-types}(iv)`.

## Summary
Checked: 38 | Findings: 38 | Verdict: FAIL
tokens used
271,954
